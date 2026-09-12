# Catch Notes 5.2.8 Teardown

Research notes on the final iOS build of Catch Notes, recovered from the Internet
Archive. The notes record where the artifact came from, which analysis tools work
against a 2013 armv7 binary, and what the first static pass recovered.

## Provenance

| Property | Value |
|---|---|
| Internet Archive item | `CatchiPA`, "Catch Notes iPhone App" |
| Item page | https://archive.org/details/CatchiPA |
| File | `Catch-E03D11BF-B1E7-4617-A604-D14A48A8559A.ipa` |
| Size | 3,821,714 bytes |
| MD5 | `9a891d439c74198cfa32e39a37e6bb34` |
| SHA-1 | `ed6adee7acd7a799cb8b628ba71552fbce4069d4` |
| Uploaded | 2019-06-17, collections `ipaarchive` and `phonesoftware` |

The download hash matches the hash the Internet Archive publishes in item metadata.
A second source corroborates the artifact. The Wayback Machine holds the App Store
listing for app ID 355424047, captured 2013-07-31, which advertises version 5.2.5
updated on 2013 May 14. The archived binary reports 5.2.8, so the archive preserves
a build at or after the last listing snapshot.

## Legal position

Catch.com shut the sync service down on 2013-08-30 and the vendor no longer
distributes the application. The archived binary carries `cryptid 0`, so a prior
party already removed the FairPlay encryption layer. Analysis here covers
interoperability and software preservation, and it targets a service with no
running infrastructure.

Two handling rules follow from that position. Do not commit the IPA or any
extracted payload to this repository, because the binary remains under copyright.
Do not republish credentials if a later pass recovers any. The first pass recovered
none, as recorded below.

## Binary facts

| Property | Value |
|---|---|
| Bundle identifier | `com.snaptic.-banana` |
| Version | 5.2.8 |
| Architecture | armv7 only, 32-bit, not a fat binary |
| Minimum OS | iOS 5.0 |
| Built against | iOS 6.1 SDK, Xcode 4.6.3 |
| Device family | iPhone and iPod touch |
| Encryption | `LC_ENCRYPTION_INFO` present with `cryptid 0`, meaning decrypted |
| URL schemes | `catch`, `snaptic`, `fb156453657732073` |
| Facebook app ID | `156453657732073` |
| Localizations | English, French, German, Japanese, Korean, Spanish |

The bundle identifier preserves the original Snaptic and 3banana lineage. The
product shipped under three names across its life, and the code kept the first one.

Two consequences constrain any attempt to run the application. The armv7 slice
will not launch on iOS 11 or later, so execution requires a device on iOS 10.3.x
or earlier. The iOS Simulator will not help, because the Simulator executes x86
code and this bundle contains no x86 slice.

## Toolchain

### Tier 1: Apple command line tools

The Xcode command line tools answer most structural questions and require no
installation beyond `xcode-select --install`.

```sh
unzip -q Catch.ipa -d ipa
plutil -convert xml1 -o - ipa/Payload/Catch.app/Info.plist   # bundle metadata
otool -L  ipa/Payload/Catch.app/Catch                        # linked frameworks
otool -l  ipa/Payload/Catch.app/Catch | grep -A4 ENCRYPTION  # cryptid check
otool -v -s __TEXT __objc_classname ipa/Payload/Catch.app/Catch
otool -v -s __TEXT __objc_methname  ipa/Payload/Catch.app/Catch
strings -a ipa/Payload/Catch.app/Catch
```

The `__objc_classname` and `__objc_methname` sections carry every class name and
every selector the binary references. Those two sections alone reveal the internal
architecture, because Objective-C stores its metadata in cleartext.

### Tier 2: Objective-C class dump

Two established tools fail against this specific binary.

`class-dump` loads the target through the Objective-C runtime and therefore needs
a host of the same architecture. An Apple Silicon Mac cannot host armv7.

`ktool` version 2.0.0, installed with `pipx install k2l`, requires two fixes and
still fails. The package imports `pkg_resources`, which Python 3.12 removed, so
the virtual environment needs `pipx runpip k2l install "setuptools<81"`. After
that fix `ktool` parses the Mach-O header but mis-resolves the armv7 protocol
table, emitting `Failed to load a protocol with Address 0x0 not in VA Table` for
every protocol and producing no headers.

`tools/objc_dump32.py` in this repository solves the problem directly. The script
walks `__objc_classlist`, reads each `class_ro_t`, and follows the method and
ivar lists using the 32-bit Objective-C 2.0 structure layouts. It needs no runtime
and no network.

```sh
python3 tools/objc_dump32.py ipa/Payload/Catch.app/Catch --headers dump_headers
# 264 classes, 6938 methods, 1706 ivars
```

### Tier 3: disassembly and decompilation

Ghidra is the practical choice for this binary. Ghidra decompiles armv7 to C,
runs free, and applies Objective-C metadata to name the functions. Import the
Mach-O, select ARM v7 little endian as the language, and run auto-analysis with
the Objective-C analyzers enabled.

Hopper Disassembler offers a paid macOS-native alternative with strong ARM32
support and a faster interface for small binaries.

Radare2 and its Cutter front end read the binary and disassemble it, though the
decompiler quality on armv7 Objective-C trails Ghidra.

### Tier 4: resources

The bundle holds 546 PNG files, 17 compiled NIB files, seven `.strings` files,
four JavaScript files, four CSS files, and one TrueType font. The note editor
renders through a web view, which explains the CSS and JavaScript. Those files
read as plain text and document the editor behavior without any disassembly.

Compiled NIB files use the NIBArchive format rather than a property list, so
`plutil` will not convert them. A dedicated NIBArchive parser recovers the view
hierarchy when the interface layout matters.

### Tier 5: dynamic analysis

Frida attaches to the process on a jailbroken device running iOS 10.3.x or
earlier and traces the Objective-C methods that the class dump names. The method
names recovered in tier 2 supply the trace filters directly.

touchHLE emulates 32-bit iPhone applications on a modern desktop. The project
targets games and does not support UIKit completely, so treat it as experimental
for this application.

## Findings from the first static pass

### Application architecture

The class dump separates the application into four layers.

**Transport.** `CatchClient` owns the HTTP surface. It holds an access token, an
API scheme, and an API server as instance variables, and it exposes 69 methods.
`SnapticAPI` wraps `CatchClient` as a singleton and selects the server through
`serverForServerOption:`.

**API models.** `CatchApiNote`, `CatchApiStream`, `CatchApiActivity`,
`CatchApiCheckItem`, `CatchApiMediaRef`, and `CatchApiNoteRef` represent the wire
format.

**Local models.** `CatchNote`, `CatchStream`, `CatchMedia`, `CatchCheckItem`,
`CatchComment`, `CatchTag`, `CatchLocation`, and `CatchAccount` represent stored
state. `CatchNote` carries a `syncState_` integer, a `remoteId_` string, and a
`serverModified_` string, which together drive reconciliation.

**Persistence.** `CatchSyncStore` mediates between the local models and SQLite.
The application links `libsqlite3` and bundles FMDB, visible as `FMDatabase`,
`FMResultSet`, and `FMStatement`.

The product calls a notebook a **stream** in code and a **Space** in the user
interface. Every table, endpoint, and class uses the internal term.

### REST API surface

The binary contains these path templates, where `%@` marks a runtime substitution.

```
/v2/user
/v3/activities
/v3/activities/%@
/v3/auth/facebook
/v3/devices
/v3/devices/%@
/v3/invites
/v3/invites/%@/claim
/v3/streams
/v3/streams/%@
/v3/streams/%@/%@
/v3/streams/%@/%@/image
/v3/streams/%@/%@/raw
/v3/streams/%@/contributors/%@
/v3/streams/positions
/v3/streams/sync
/v3/streams/sync/%@
```

`/v3/streams/%@/%@` addresses a note inside a stream. The `image` and `raw`
suffixes retrieve a rendered image and the original attachment bytes.

Authentication uses a separate path family.

```
/login/api/access_token
/login/api/bouncer
/login/api/catch
/login/api/create
```

The default host is `api.catch.com`.

### Authentication flow

`CatchClient` declares the sequence in its method names.

```objc
- getAuthTicket;
- getAuthCodeWithEmail:password:client_id:ticket:createAccount:;
- requestAccessTokenWithCode:client_id:client_secret:;
- facebookSignIn:;
```

The client fetches a ticket, exchanges an email address, a password, and that
ticket for an authorization code, then exchanges the code for an access token.
The pattern follows the OAuth 2.0 authorization code grant with a vendor-specific
ticket step in front. The binary also contains the literal `Basic %@`, so some
requests carry HTTP Basic credentials instead.

The Google sign-in path appears as a full template:

```
https://%@/login/google?redirect_uri=catch://&client_id=catch_iphone&response_type=token&display=wap
```

The client identifier is `catch_iphone`. A string search recovered no client
secret value. The token `client_secret` appears only as a format-string key, as a
method parameter name, and inside Facebook SDK test-harness boilerplate.

### Local SQLite schema

`CatchSyncStore` creates these tables. The schema is the highest-value artifact
for anyone importing an old Catch export, because it names every field the client
tracked.

```sql
CREATE TABLE note (note_id INTEGER PRIMARY KEY, remote_id TEXT, sync_state INTEGER,
  server_modified TEXT, text TEXT, created INTEGER, modified INTEGER, reminder INTEGER,
  privacy_mode INTEGER, browser_url TEXT, owner_name TEXT, owner_id TEXT, source TEXT,
  source_url TEXT);

CREATE TABLE stream (stream_id INTEGER PRIMARY KEY, remote_id TEXT, sync_state INTEGER,
  server_modified TEXT, display_type INTEGER, created_by INTEGER, name TEXT,
  description TEXT, created INTEGER, modified INTEGER, annotation_json TEXT);

CREATE TABLE stream_note (stream_id INTEGER, note_id INTEGER, sync_state INTEGER);
CREATE TABLE stream_contributor (stream_id INTEGER, user_id INTEGER);

CREATE TABLE media (media_id INTEGER PRIMARY KEY, remote_id TEXT, sync_state INTEGER,
  note_id INTEGER, created INTEGER, filename TEXT, mime_type TEXT, display_type INTEGER,
  size INTEGER, path TEXT, thumbnail_path TEXT, space_saver_path TEXT, display_hint TEXT);

CREATE TABLE checkitem (item_id INTEGER PRIMARY KEY, remote_id TEXT, sync_state INTEGER,
  note_id INTEGER, text TEXT, checked BOOL, created INTEGER, modified INTEGER,
  owner_name TEXT, owner_id TEXT, checked_by_name TEXT, checked_by_id TEXT,
  server_modified TEXT, remote_note_id TEXT);

CREATE TABLE comment (comment_id INTEGER PRIMARY KEY, remote_id TEXT, sync_state INTEGER,
  note_id INTEGER, text TEXT, created INTEGER, modified INTEGER, owner_name TEXT,
  owner_id TEXT, source TEXT, source_url TEXT);

CREATE TABLE location (note_id INTEGER PRIMARY KEY, latitude REAL, longitude REAL,
  altitude REAL, speed REAL, bearing REAL, accuracy_position REAL, accuracy_altitude REAL);

CREATE TABLE tag (lc_name TEXT PRIMARY KEY, display_name TEXT);
CREATE TABLE tagged (lc_name TEXT, note_id INTEGER, comment_id INTEGER);

CREATE TABLE activities (activity_id INTEGER PRIMARY KEY, remote_id TEXT, type INTEGER,
  action INTEGER, read BOOL, activity_at INTEGER, stream_id INTEGER, object_id INTEGER,
  parent_id INTEGER, pending_sync INTEGER DEFAULT 0 NOT NULL);

CREATE TABLE sync_info (key TEXT, value TEXT);
```

Three design decisions stand out. Tags live in a normalized `tagged` join table
keyed on a lowercased name, so tag matching is case-insensitive by construction.
Every syncable row carries both a local integer key and a `remote_id` string, which
lets the client create objects offline and reconcile them later. The `sync_state`
column appears on every syncable table and encodes the pending operation.

The binary also carries the `ALTER TABLE` statements from every prior migration,
including `ALTER TABLE note_images RENAME TO note_media`. The migration history
documents the schema evolution across the 3banana, Snaptic, and Catch eras.

### Third-party SDKs

| SDK | Role |
|---|---|
| ASIHTTPRequest | HTTP transport, including `ASIFormDataRequest` and `ASIDownloadCache` |
| FMDB | SQLite wrapper |
| Facebook iOS SDK | Login and sharing |
| Crittercism | Crash reporting and handled exceptions |
| PLCrashReporter | Crash capture underneath Crittercism |
| Mixpanel | Product analytics |
| Google Analytics, as `GANTracker` | Additional analytics |
| Appirater | App Store rating prompt |
| MBProgressHUD | Progress overlay |
| TTTAttributedLabel | Rich text label |
| MGSplitViewController | iPad split view |
| RegexKitLite | Regular expressions |
| ATSDragToReorderTableView | Drag-to-reorder lists |

The Foursquare Places API supplies location names through
`https://api.foursquare.com/v2/venues/search`, wrapped by `FoursquareLookup` and
`FoursquareVenue`.

### Debug affordances

The binary contains four command paths that read as hidden developer controls.

```
/showServerOption
/hideServerOption
/enableLoggingAll
/disableLoggingAll
```

`SettingsServerOptionViewController` exists as a class, and the binary names three
hosts: `api.catch.com`, `catch-trunk.com`, and `catch-branch.com`. The trunk and
branch hosts were staging environments. Anyone reconstructing the protocol should
test whether the `catch://` URL scheme triggers these paths, because
`showServerOption` would expose the host picker in Settings.

## Open questions

The static pass leaves four questions that need disassembly or a live trace.

1. Which HTTP verb each endpoint accepts. The path templates appear as strings,
   while `executeHttpMethod:endpoint:parameters:` selects the verb at the call site.
2. The JSON request and response shapes. The `CatchApi*` classes hold the field
   names in their ivar lists, and `dump_headers/CatchApiNote.h` is the entry point.
3. The `sync_state` enumeration values. The integers drive reconciliation and the
   meanings live in the compiled code.
4. Whether a client secret is derived at runtime. No literal value appears in the
   string table.

## Reproduction

```sh
# Fetch and verify
curl -L -o Catch.ipa \
  https://archive.org/download/CatchiPA/Catch-E03D11BF-B1E7-4617-A604-D14A48A8559A.ipa
md5 Catch.ipa   # expect 9a891d439c74198cfa32e39a37e6bb34

# Unpack
unzip -q Catch.ipa -d ipa

# Class dump
python3 tools/objc_dump32.py ipa/Payload/Catch.app/Catch --headers dump_headers

# Schema
strings -a ipa/Payload/Catch.app/Catch | grep -iE 'create table|create index|alter table'

# Endpoints
strings -a ipa/Payload/Catch.app/Catch | grep -aE '^/(v[0-9]|login)'
```

## References

- Internet Archive item: https://archive.org/details/CatchiPA
- Archived App Store listing, captured 2013-07-31:
  https://web.archive.org/web/20130731102052/https://itunes.apple.com/us/app/catch-notes/id355424047?mt=8
- Archived catch.com home page, captured 2013-07-02:
  https://web.archive.org/web/20130702231250/https://catch.com/
- Shutdown coverage, TechCrunch, 2013-07-31:
  https://techcrunch.com/2013/07/31/evernote-competitor-catch-com-shuts-down-its-note-taking-apps-company-heading-in-different-direction/
