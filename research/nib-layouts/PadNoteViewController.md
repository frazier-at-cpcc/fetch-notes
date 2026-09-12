# PadNoteViewController

Recovered layout for `PadNoteViewController.nib`. Every interpreted value appears beside the
raw decoded value, so a disputed reading stays auditable.

The frame is computed, not stored. `UIBounds` carries the size and an
origin that is always 0, and `UICenter` carries the position, so the frame
is origin = center - size / 2 with the size taken from the bounds. Both
source values appear beside every frame.

A view is nested under another view only through a containment key: `UISubviews`, `UIContentView`, `UITableHeaderView`, `UINavigationBar`.
The flat registries, among them `UINibObjectsKey` and
`UINibTopLevelObjectsKey`, name every archived object and describe no
containment, so they parent nothing.

## Interface

- **UIBarButtonItem** (object 5)
  - class: `UIBarButtonItem`
  - target/action: `attachPhoto:` from object 5 (UIBarButtonItem) to object 36 (UIProxyObject), event mask not encoded
  - raw values:
    - `UIEnabled` (type 5): `False`
    - `UIStyle` (type 0): `1`
    - `UITitle` (type 10): `{'$ref': 67}`

- **UIView** (object 14)
  - class: `UIView`
  - frame: (0, 0, 768, 1004)
  - raw UIBounds: (0, 0, 768, 1004)
  - raw UICenter: (384, 502)
  - autoresizing mask: 36
  - background color: rgba(1, 1, 1, 1)
  - hidden: not encoded
  - opaque: false
  - tag: not encoded
  - raw values:
    - `UIBounds` (type 8): `{'$data_hex': '0600000000000000000000404400007b44', '$floats': [0.0, 0.0, 768.0, 1004.0]}`
    - `UICenter` (type 8): `{'$data_hex': '060000c0430000fb43', '$floats': [384.0, 502.0]}`
    - `UISubviews` (type 10): `{'$ref': 87}`
    - `UIBackgroundColor` (type 10): `{'$ref': 39}`
    - `UIOpaque` (type 5): `False`
    - `UIAutoresizeSubviews` (type 5): `False`
    - `UIAutoresizingMask` (type 0): `36`
    - `UIClearsContextBeforeDrawing` (type 4): `True`
  - **UIToolbar** (object 69)
    - class: `UIToolbar`
    - frame: (0, 0, 768, 44)
    - raw UIBounds: (0, 0, 768, 44)
    - raw UICenter: (384, 22)
    - autoresizing mask: 34
    - background color: not encoded
    - hidden: not encoded
    - opaque: false
    - tag: not encoded
    - raw values:
      - `UIBounds` (type 8): `{'$data_hex': '0600000000000000000000404400003042', '$floats': [0.0, 0.0, 768.0, 44.0]}`
      - `UICenter` (type 8): `{'$data_hex': '060000c0430000b041', '$floats': [384.0, 22.0]}`
      - `UIOpaque` (type 5): `False`
      - `UIAutoresizeSubviews` (type 5): `False`
      - `UIAutoresizingMask` (type 0): `34`
      - `UIClearsContextBeforeDrawing` (type 4): `True`
      - `UIViewContentHuggingPriority` (type 10): `{'$ref': 15}`
      - `UIItems` (type 10): `{'$ref': 85}`
  - **PadTouchToEditTextView** (object 16)
    - class: `PadTouchToEditTextView`
    - encoded as: `UIClassSwapper` swapping `UIView`
    - frame: (0, 44, 768, 960)
    - raw UIBounds: (0, 0, 768, 960)
    - raw UICenter: (384, 524)
    - autoresizing mask: 18
    - background color: rgba(1, 1, 1, 1)
    - hidden: not encoded
    - opaque: false
    - tag: not encoded
    - outlet: `delegate` to object 36 (UIProxyObject)
    - raw values:
      - `UIBounds` (type 8): `{'$data_hex': '0600000000000000000000404400007044', '$floats': [0.0, 0.0, 768.0, 960.0]}`
      - `UICenter` (type 8): `{'$data_hex': '060000c04300000344', '$floats': [384.0, 524.0]}`
      - `UIBackgroundColor` (type 10): `{'$ref': 39}`
      - `UIOpaque` (type 5): `False`
      - `UIAutoresizeSubviews` (type 5): `False`
      - `UIAutoresizingMask` (type 0): `18`
      - `UIClassName` (type 10): `{'$ref': 92}`
      - `UIOriginalClassName` (type 10): `{'$ref': 59}`
  - **UIView** (object 43)
    - class: `UIView`
    - frame: (0, 44, 768, 960)
    - raw UIBounds: (0, 0, 768, 960)
    - raw UICenter: (384, 524)
    - autoresizing mask: 18
    - background color: rgba(0.132256, 0.129286, 0.129353, 1)
    - hidden: not encoded
    - opaque: false
    - tag: not encoded
    - raw values:
      - `UIBounds` (type 8): `{'$data_hex': '0600000000000000000000404400007044', '$floats': [0.0, 0.0, 768.0, 960.0]}`
      - `UICenter` (type 8): `{'$data_hex': '060000c04300000344', '$floats': [384.0, 524.0]}`
      - `UIBackgroundColor` (type 10): `{'$ref': 22}`
      - `UIOpaque` (type 5): `False`
      - `UIAutoresizeSubviews` (type 5): `False`
      - `UIAutoresizingMask` (type 0): `18`

- **UIBarButtonItem** (object 32)
  - class: `UIBarButtonItem`
  - target/action: `stopEditing:` from object 32 (UIBarButtonItem) to object 36 (UIProxyObject), event mask not encoded
  - raw values:
    - `UIEnabled` (type 5): `False`
    - `UIIsSystemItem` (type 5): `False`
    - `UISystemItem` (type 0): `0`
    - `UIStyle` (type 0): `2`

- **UIProxyObject** (object 36)
  - class: `UIProxyObject`
  - outlet: `padMasterToggleSpacer` to object 46 (UIBarButtonItem)
  - outlet: `trashItem` to object 81 (UIBarButtonItem)
  - outlet: `dividerItem` to object 61 (UIBarButtonItem)
  - outlet: `contentView` to object 16 (PadTouchToEditTextView)
  - outlet: `attachItem` to object 88 (UIBarButtonItem)
  - outlet: `streamsItem` to object 47 (UIBarButtonItem)
  - outlet: `inputAccessoryToolbar` to object 40 (PadNoteViewInputAccessory)
  - outlet: `padMasterToggleItem` to object 1 (UIBarButtonItem)
  - outlet: `actionItem` to object 54 (UIBarButtonItem)
  - outlet: `starItem` to object 23 (UIBarButtonItem)
  - outlet: `createNoteItem` to object 95 (UIBarButtonItem)
  - outlet: `blockerView` to object 43 (UIView)
  - outlet: `toolbar` to object 69 (UIToolbar)
  - outlet: `view` to object 14 (UIView)
  - target/action: `attachPhoto:` from object 5 (UIBarButtonItem) to object 36 (UIProxyObject), event mask not encoded
  - target/action: `stopEditing:` from object 32 (UIBarButtonItem) to object 36 (UIProxyObject), event mask not encoded
  - target/action: `attachVoice:` from object 64 (UIBarButtonItem) to object 36 (UIProxyObject), event mask not encoded
  - raw values:
    - `UIProxiedObjectIdentifier` (type 10): `{'$ref': 35}`

- **PadNoteViewInputAccessory** (object 40)
  - class: `PadNoteViewInputAccessory`
  - encoded as: `UIClassSwapper` swapping `UIToolbar`
  - frame: (0, 0, 768, 44)
  - raw UIBounds: (0, 0, 768, 44)
  - raw UICenter: (384, 22)
  - autoresizing mask: 10
  - background color: not encoded
  - hidden: not encoded
  - opaque: false
  - tag: not encoded
  - outlet: `camAttachItem` to object 5 (UIBarButtonItem)
  - outlet: `fixedSpaceItem` to object 9 (UIBarButtonItem)
  - outlet: `micAttachItem` to object 64 (UIBarButtonItem)
  - outlet: `delegate` to object 36 (UIProxyObject)
  - raw values:
    - `UIBounds` (type 8): `{'$data_hex': '0600000000000000000000404400003042', '$floats': [0.0, 0.0, 768.0, 44.0]}`
    - `UICenter` (type 8): `{'$data_hex': '060000c0430000b041', '$floats': [384.0, 22.0]}`
    - `UIOpaque` (type 5): `False`
    - `UIAutoresizeSubviews` (type 5): `False`
    - `UIAutoresizingMask` (type 0): `10`
    - `UIClearsContextBeforeDrawing` (type 4): `True`
    - `UIViewContentHuggingPriority` (type 10): `{'$ref': 15}`
    - `UIItems` (type 10): `{'$ref': 49}`
    - `UIClassName` (type 10): `{'$ref': 84}`
    - `UIOriginalClassName` (type 10): `{'$ref': 66}`

- **UIBarButtonItem** (object 64)
  - class: `UIBarButtonItem`
  - target/action: `attachVoice:` from object 64 (UIBarButtonItem) to object 36 (UIProxyObject), event mask not encoded
  - raw values:
    - `UIEnabled` (type 5): `False`
    - `UIStyle` (type 0): `1`
    - `UITitle` (type 10): `{'$ref': 2}`

## Supporting objects

These objects carry no geometry, contain no view, and hold no
connection. They remain here because a reader auditing an
interpretation follows a reference into them.

- **NSObject** (object 0)
  - class: `NSObject`
  - raw values:
    - `UINibTopLevelObjectsKey` (type 10): `{'$ref': 91}`
    - `UINibObjectsKey` (type 10): `{'$ref': 53}`
    - `UINibConnectionsKey` (type 10): `{'$ref': 41}`
    - `UINibVisibleWindowsKey` (type 10): `{'$ref': 30}`
    - `UINibAccessibilityConfigurationsKey` (type 10): `{'$ref': 30}`
    - `UINibKeyValuePairsKey` (type 10): `{'$ref': 30}`

- **UIBarButtonItem** (object 1)
  - class: `UIBarButtonItem`
  - raw values:
    - `UIEnabled` (type 5): `False`
    - `UIImage` (type 10): `{'$ref': 75}`

- **NSString** (object 2)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '4d6963', '$text': 'Mic'}`

- **NSString** (object 3)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '61747461636850686f746f3a', '$text': 'attachPhoto:'}`

- **UIRuntimeOutletConnection** (object 4)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 38}`
    - `UISource` (type 10): `{'$ref': 36}`
    - `UIDestination` (type 10): `{'$ref': 46}`

- **NSString** (object 6)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '646976696465724974656d', '$text': 'dividerItem'}`

- **UIRuntimeOutletConnection** (object 7)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 21}`
    - `UISource` (type 10): `{'$ref': 36}`
    - `UIDestination` (type 10): `{'$ref': 81}`

- **NSString** (object 8)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '6d69634174746163684974656d', '$text': 'micAttachItem'}`

- **UIBarButtonItem** (object 9)
  - class: `UIBarButtonItem`
  - raw values:
    - `UIEnabled` (type 5): `False`
    - `UIIsSystemItem` (type 5): `False`
    - `UISystemItem` (type 0): `6`
    - `UIWidth` (type 6): `42.0`

- **UIProxyObject** (object 10)
  - class: `UIProxyObject`
  - raw values:
    - `UIProxiedObjectIdentifier` (type 10): `{'$ref': 90}`

- **UIBarButtonItem** (object 11)
  - class: `UIBarButtonItem`
  - raw values:
    - `UIEnabled` (type 5): `False`
    - `UIIsSystemItem` (type 5): `False`
    - `UISystemItem` (type 0): `6`
    - `UIWidth` (type 6): `1.0`

- **UIRuntimeOutletConnection** (object 12)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 6}`
    - `UISource` (type 10): `{'$ref': 36}`
    - `UIDestination` (type 10): `{'$ref': 61}`

- **NSString** (object 13)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '737461724974656d', '$text': 'starItem'}`

- **NSString** (object 15)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '7b3235302c203235307d', '$text': '{250, 250}'}`

- **UIRuntimeEventConnection** (object 17)
  - class: `UIRuntimeEventConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 3}`
    - `UISource` (type 10): `{'$ref': 5}`
    - `UIDestination` (type 10): `{'$ref': 36}`

- **UIRuntimeOutletConnection** (object 18)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 50}`
    - `UISource` (type 10): `{'$ref': 36}`
    - `UIDestination` (type 10): `{'$ref': 16}`

- **UIBarButtonItem** (object 19)
  - class: `UIBarButtonItem`
  - raw values:
    - `UIEnabled` (type 5): `False`
    - `UIIsSystemItem` (type 5): `False`
    - `UISystemItem` (type 0): `6`
    - `UIWidth` (type 6): `8.0`

- **UIRuntimeOutletConnection** (object 20)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 45}`
    - `UISource` (type 10): `{'$ref': 36}`
    - `UIDestination` (type 10): `{'$ref': 88}`

- **NSString** (object 21)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '74726173684974656d', '$text': 'trashItem'}`

- **UIColor** (object 22)
  - class: `UIColor`
  - raw values:
    - `UIColorComponentCount` (type 0): `4`
    - `UIRed` (type 6): `0.13225606083869934`
    - `UIGreen` (type 6): `0.1292855143547058`
    - `UIBlue` (type 6): `0.12935300171375275`
    - `UIAlpha` (type 6): `1.0`
    - `NSRGB` (type 8): `{'$data_hex': '302e31333220302e31323920302e313239', '$text': '0.132 0.129 0.129'}`
    - `NSColorSpace` (type 0): `2`

- **UIBarButtonItem** (object 23)
  - class: `UIBarButtonItem`
  - raw values:
    - `UIEnabled` (type 5): `False`
    - `UIIsSystemItem` (type 5): `False`
    - `UISystemItem` (type 0): `14`

- **NSString** (object 24)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '626c6f636b657256696577', '$text': 'blockerView'}`

- **UIRuntimeEventConnection** (object 25)
  - class: `UIRuntimeEventConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 83}`
    - `UISource` (type 10): `{'$ref': 32}`
    - `UIDestination` (type 10): `{'$ref': 36}`

- **NSString** (object 26)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '6372656174654e6f74654974656d', '$text': 'createNoteItem'}`

- **NSString** (object 27)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '617474616368566f6963653a', '$text': 'attachVoice:'}`

- **UIRuntimeOutletConnection** (object 28)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 74}`
    - `UISource` (type 10): `{'$ref': 36}`
    - `UIDestination` (type 10): `{'$ref': 47}`

- **UIBarButtonItem** (object 29)
  - class: `UIBarButtonItem`
  - raw values:
    - `UIEnabled` (type 5): `False`
    - `UIIsSystemItem` (type 5): `False`
    - `UISystemItem` (type 0): `6`
    - `UIWidth` (type 6): `5.0`

- **NSArray** (object 30)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`

- **UIRuntimeOutletConnection** (object 31)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 37}`
    - `UISource` (type 10): `{'$ref': 36}`
    - `UIDestination` (type 10): `{'$ref': 40}`

- **UIRuntimeOutletConnection** (object 33)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 80}`
    - `UISource` (type 10): `{'$ref': 16}`
    - `UIDestination` (type 10): `{'$ref': 36}`

- **UIImageNibPlaceholder** (object 34)
  - class: `UIImageNibPlaceholder`
  - raw values:
    - `UIImageWidth` (type 6): `1.0`
    - `UIImageHeight` (type 6): `1.0`
    - `UIResourceName` (type 10): `{'$ref': 51}`

- **NSString** (object 35)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '494246696c65734f776e6572', '$text': 'IBFilesOwner'}`

- **NSString** (object 37)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '696e7075744163636573736f7279546f6f6c626172', '$text': 'inputAccessoryToolbar'}`

- **NSString** (object 38)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '7061644d6173746572546f67676c65537061636572', '$text': 'padMasterToggleSpacer'}`

- **UIColor** (object 39)
  - class: `UIColor`
  - raw values:
    - `UIColorComponentCount` (type 0): `4`
    - `UIRed` (type 6): `1.0`
    - `UIGreen` (type 6): `1.0`
    - `UIBlue` (type 6): `1.0`
    - `UIAlpha` (type 6): `1.0`
    - `NSRGB` (type 8): `{'$data_hex': '3120312031', '$text': '1 1 1'}`
    - `NSColorSpace` (type 0): `2`

- **NSArray** (object 41)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 17}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 48}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 25}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 60}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 20}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 72}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 56}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 18}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 70}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 33}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 82}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 12}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 68}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 31}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 79}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 42}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 4}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 62}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 28}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 76}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 7}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 94}`

- **UIRuntimeOutletConnection** (object 42)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 73}`
    - `UISource` (type 10): `{'$ref': 36}`
    - `UIDestination` (type 10): `{'$ref': 1}`

- **NSString** (object 44)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '746f6f6c626172', '$text': 'toolbar'}`

- **NSString** (object 45)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '6174746163684974656d', '$text': 'attachItem'}`

- **UIBarButtonItem** (object 46)
  - class: `UIBarButtonItem`
  - raw values:
    - `UIEnabled` (type 5): `False`
    - `UIIsSystemItem` (type 5): `False`
    - `UISystemItem` (type 0): `6`
    - `UIWidth` (type 6): `5.0`

- **UIBarButtonItem** (object 47)
  - class: `UIBarButtonItem`
  - raw values:
    - `UIImage` (type 10): `{'$ref': 34}`

- **UIRuntimeEventConnection** (object 48)
  - class: `UIRuntimeEventConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 27}`
    - `UISource` (type 10): `{'$ref': 64}`
    - `UIDestination` (type 10): `{'$ref': 36}`

- **NSArray** (object 49)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 9}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 5}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 64}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 89}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 32}`

- **NSString** (object 50)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '636f6e74656e7456696577', '$text': 'contentView'}`

- **NSString** (object 51)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '4e6f7465566965775f546f6f6c6261725f53747265616d732e706e67', '$text': 'NoteView_Toolbar_Streams.png'}`

- **UIImageNibPlaceholder** (object 52)
  - class: `UIImageNibPlaceholder`
  - raw values:
    - `UIImageWidth` (type 6): `1.0`
    - `UIImageHeight` (type 6): `1.0`
    - `UIResourceName` (type 10): `{'$ref': 63}`

- **NSArray** (object 53)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 36}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 10}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 14}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 40}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 69}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 16}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 43}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 9}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 5}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 64}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 89}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 32}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 46}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 1}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 93}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 47}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 86}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 54}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 58}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 88}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 19}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 23}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 55}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 81}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 29}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 61}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 11}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 95}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 96}`

- **UIBarButtonItem** (object 54)
  - class: `UIBarButtonItem`
  - raw values:
    - `UIIsSystemItem` (type 5): `False`
    - `UISystemItem` (type 0): `9`

- **UIBarButtonItem** (object 55)
  - class: `UIBarButtonItem`
  - raw values:
    - `UIEnabled` (type 5): `False`
    - `UIIsSystemItem` (type 5): `False`
    - `UISystemItem` (type 0): `6`
    - `UIWidth` (type 6): `10.0`

- **UIRuntimeOutletConnection** (object 56)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 78}`
    - `UISource` (type 10): `{'$ref': 40}`
    - `UIDestination` (type 10): `{'$ref': 5}`

- **NSString** (object 57)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '616374696f6e4974656d', '$text': 'actionItem'}`

- **UIBarButtonItem** (object 58)
  - class: `UIBarButtonItem`
  - raw values:
    - `UIEnabled` (type 5): `False`
    - `UIIsSystemItem` (type 5): `False`
    - `UISystemItem` (type 0): `6`
    - `UIWidth` (type 6): `7.0`

- **NSString** (object 59)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '554956696577', '$text': 'UIView'}`

- **UIRuntimeOutletConnection** (object 60)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 57}`
    - `UISource` (type 10): `{'$ref': 36}`
    - `UIDestination` (type 10): `{'$ref': 54}`

- **UIBarButtonItem** (object 61)
  - class: `UIBarButtonItem`
  - raw values:
    - `UIEnabled` (type 5): `False`
    - `UIImage` (type 10): `{'$ref': 52}`

- **UIRuntimeOutletConnection** (object 62)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 13}`
    - `UISource` (type 10): `{'$ref': 36}`
    - `UIDestination` (type 10): `{'$ref': 23}`

- **NSString** (object 63)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '726f77315f636f6c325f646976696465722e706e67', '$text': 'row1_col2_divider.png'}`

- **NSString** (object 65)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '726f77315f636f6c325f69636f6e5f6c6566746172726f772e706e67', '$text': 'row1_col2_icon_leftarrow.png'}`

- **NSString** (object 66)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '5549546f6f6c626172', '$text': 'UIToolbar'}`

- **NSString** (object 67)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '43616d', '$text': 'Cam'}`

- **UIRuntimeOutletConnection** (object 68)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 71}`
    - `UISource` (type 10): `{'$ref': 40}`
    - `UIDestination` (type 10): `{'$ref': 9}`

- **UIRuntimeOutletConnection** (object 70)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 26}`
    - `UISource` (type 10): `{'$ref': 36}`
    - `UIDestination` (type 10): `{'$ref': 95}`

- **NSString** (object 71)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '666978656453706163654974656d', '$text': 'fixedSpaceItem'}`

- **UIRuntimeOutletConnection** (object 72)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 24}`
    - `UISource` (type 10): `{'$ref': 36}`
    - `UIDestination` (type 10): `{'$ref': 43}`

- **NSString** (object 73)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '7061644d6173746572546f67676c654974656d', '$text': 'padMasterToggleItem'}`

- **NSString** (object 74)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '73747265616d734974656d', '$text': 'streamsItem'}`

- **UIImageNibPlaceholder** (object 75)
  - class: `UIImageNibPlaceholder`
  - raw values:
    - `UIImageWidth` (type 6): `1.0`
    - `UIImageHeight` (type 6): `1.0`
    - `UIResourceName` (type 10): `{'$ref': 65}`

- **UIRuntimeOutletConnection** (object 76)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 44}`
    - `UISource` (type 10): `{'$ref': 36}`
    - `UIDestination` (type 10): `{'$ref': 69}`

- **NSString** (object 77)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '76696577', '$text': 'view'}`

- **NSString** (object 78)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '63616d4174746163684974656d', '$text': 'camAttachItem'}`

- **UIRuntimeOutletConnection** (object 79)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 8}`
    - `UISource` (type 10): `{'$ref': 40}`
    - `UIDestination` (type 10): `{'$ref': 64}`

- **NSString** (object 80)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '64656c6567617465', '$text': 'delegate'}`

- **UIBarButtonItem** (object 81)
  - class: `UIBarButtonItem`
  - raw values:
    - `UIIsSystemItem` (type 5): `False`
    - `UISystemItem` (type 0): `16`

- **UIRuntimeOutletConnection** (object 82)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 80}`
    - `UISource` (type 10): `{'$ref': 40}`
    - `UIDestination` (type 10): `{'$ref': 36}`

- **NSString** (object 83)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '73746f7045646974696e673a', '$text': 'stopEditing:'}`

- **NSString** (object 84)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '5061644e6f746556696577496e7075744163636573736f7279', '$text': 'PadNoteViewInputAccessory'}`

- **NSArray** (object 85)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 46}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 1}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 93}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 47}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 86}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 54}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 58}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 88}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 19}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 23}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 55}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 81}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 29}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 61}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 11}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 95}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 96}`

- **UIBarButtonItem** (object 86)
  - class: `UIBarButtonItem`
  - raw values:
    - `UIEnabled` (type 5): `False`
    - `UIIsSystemItem` (type 5): `False`
    - `UISystemItem` (type 0): `6`
    - `UIWidth` (type 6): `11.0`

- **NSMutableArray** (object 87)
  - class: `NSMutableArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 69}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 16}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 43}`

- **UIBarButtonItem** (object 88)
  - class: `UIBarButtonItem`
  - raw values:
    - `UIEnabled` (type 5): `False`
    - `UIIsSystemItem` (type 5): `False`
    - `UISystemItem` (type 0): `15`

- **UIBarButtonItem** (object 89)
  - class: `UIBarButtonItem`
  - raw values:
    - `UIEnabled` (type 5): `False`
    - `UIIsSystemItem` (type 5): `False`
    - `UISystemItem` (type 0): `5`

- **NSString** (object 90)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '49424669727374526573706f6e646572', '$text': 'IBFirstResponder'}`

- **NSArray** (object 91)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 36}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 10}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 14}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 40}`

- **NSString** (object 92)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '506164546f756368546f456469745465787456696577', '$text': 'PadTouchToEditTextView'}`

- **UIBarButtonItem** (object 93)
  - class: `UIBarButtonItem`
  - raw values:
    - `UIEnabled` (type 5): `False`
    - `UIIsSystemItem` (type 5): `False`
    - `UISystemItem` (type 0): `5`

- **UIRuntimeOutletConnection** (object 94)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 77}`
    - `UISource` (type 10): `{'$ref': 36}`
    - `UIDestination` (type 10): `{'$ref': 14}`

- **UIBarButtonItem** (object 95)
  - class: `UIBarButtonItem`
  - raw values:
    - `UIEnabled` (type 5): `False`
    - `UIIsSystemItem` (type 5): `False`
    - `UISystemItem` (type 0): `4`

- **UIBarButtonItem** (object 96)
  - class: `UIBarButtonItem`
  - raw values:
    - `UIEnabled` (type 5): `False`
    - `UIIsSystemItem` (type 5): `False`
    - `UISystemItem` (type 0): `6`
    - `UIWidth` (type 6): `2.0`

