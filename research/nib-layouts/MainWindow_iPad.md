# MainWindow_iPad

Recovered layout for `MainWindow_iPad.nib`. Every interpreted value appears beside the
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

- **PadNoteViewController** (object 4)
  - class: `PadNoteViewController`
  - encoded as: `UIClassSwapper` swapping `UIViewController`
  - outlet: `delegate` to object 11 (CatchNotesAppDelegate_iPad)
  - raw values:
    - `UINibName` (type 10): `{'$ref': 34}`
    - `UIClassName` (type 10): `{'$ref': 34}`
    - `UIOriginalClassName` (type 10): `{'$ref': 3}`

- **CatchNotesAppDelegate_iPad** (object 11)
  - class: `CatchNotesAppDelegate_iPad`
  - encoded as: `UIClassSwapper` swapping `UICustomObject`
  - outlet: `splitViewController` to object 14 (MGSplitViewController)
  - outlet: `primaryNoteViewController` to object 4 (PadNoteViewController)
  - outlet: `primaryNavigationController` to object 36 (UINavigationController)
  - outlet: `window` to object 18 (UIWindow)
  - raw values:
    - `UIClassName` (type 10): `{'$ref': 16}`
    - `UIOriginalClassName` (type 10): `{'$ref': 26}`

- **MGSplitViewController** (object 14)
  - class: `MGSplitViewController`
  - encoded as: `UIClassSwapper` swapping `UIViewController`
  - outlet: `detailViewController` to object 4 (PadNoteViewController)
  - outlet: `masterViewController` to object 36 (UINavigationController)
  - raw values:
    - `UIClassName` (type 10): `{'$ref': 21}`
    - `UIOriginalClassName` (type 10): `{'$ref': 3}`

- **UIWindow** (object 18)
  - class: `UIWindow`
  - frame: (0, 0, 768, 1024)
  - raw UIBounds: (0, 0, 768, 1024)
  - raw UICenter: (384, 512)
  - autoresizing mask: 36
  - background color: rgba(1, 1, 1, 1)
  - hidden: not encoded
  - opaque: not encoded
  - tag: not encoded
  - raw values:
    - `UIBounds` (type 8): `{'$data_hex': '0600000000000000000000404400008044', '$floats': [0.0, 0.0, 768.0, 1024.0]}`
    - `UICenter` (type 8): `{'$data_hex': '060000c04300000044', '$floats': [384.0, 512.0]}`
    - `UIBackgroundColor` (type 10): `{'$ref': 2}`
    - `UIAutoresizeSubviews` (type 5): `False`
    - `UIAutoresizingMask` (type 0): `36`
    - `UIClearsContextBeforeDrawing` (type 4): `True`
    - `UIResizesToFullScreen` (type 5): `False`

- **UIProxyObject** (object 29)
  - class: `UIProxyObject`
  - outlet: `delegate` to object 11 (CatchNotesAppDelegate_iPad)
  - raw values:
    - `UIProxiedObjectIdentifier` (type 10): `{'$ref': 35}`

- **UINavigationController** (object 36)
  - class: `UINavigationController`
  - raw values:
    - `UINavigationBar` (type 10): `{'$ref': 17}`
  - **UINavigationBar** (object 17)
    - class: `UINavigationBar`
    - frame: (0, 0, 320, 44)
    - raw UIBounds: (0, 0, 320, 44)
    - raw UICenter: (160, 22)
    - autoresizing mask: 2
    - background color: not encoded
    - hidden: not encoded
    - opaque: false
    - tag: not encoded
    - raw values:
      - `UIBounds` (type 8): `{'$data_hex': '0600000000000000000000a04300003042', '$floats': [0.0, 0.0, 320.0, 44.0]}`
      - `UICenter` (type 8): `{'$data_hex': '06000020430000b041', '$floats': [160.0, 22.0]}`
      - `UIOpaque` (type 5): `False`
      - `UIMultipleTouchEnabled` (type 5): `False`
      - `UIAutoresizeSubviews` (type 5): `False`
      - `UIAutoresizingMask` (type 0): `2`
      - `UIClipsToBounds` (type 5): `False`
      - `UIViewContentHuggingPriority` (type 10): `{'$ref': 12}`
      - `UIDelegate` (type 10): `{'$ref': 36}`

## Supporting objects

These objects carry no geometry, contain no view, and hold no
connection. They remain here because a reader auditing an
interpretation follows a reference into them.

- **NSObject** (object 0)
  - class: `NSObject`
  - raw values:
    - `UINibTopLevelObjectsKey` (type 10): `{'$ref': 20}`
    - `UINibObjectsKey` (type 10): `{'$ref': 33}`
    - `UINibConnectionsKey` (type 10): `{'$ref': 7}`
    - `UINibVisibleWindowsKey` (type 10): `{'$ref': 5}`
    - `UINibAccessibilityConfigurationsKey` (type 10): `{'$ref': 5}`
    - `UINibKeyValuePairsKey` (type 10): `{'$ref': 5}`

- **UIRuntimeOutletConnection** (object 1)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 27}`
    - `UISource` (type 10): `{'$ref': 29}`
    - `UIDestination` (type 10): `{'$ref': 11}`

- **UIColor** (object 2)
  - class: `UIColor`
  - raw values:
    - `UIColorComponentCount` (type 0): `4`
    - `UIRed` (type 6): `1.0`
    - `UIGreen` (type 6): `1.0`
    - `UIBlue` (type 6): `1.0`
    - `UIAlpha` (type 6): `1.0`
    - `NSRGB` (type 8): `{'$data_hex': '3120312031', '$text': '1 1 1'}`
    - `NSColorSpace` (type 0): `2`

- **NSString** (object 3)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '554956696577436f6e74726f6c6c6572', '$text': 'UIViewController'}`

- **NSArray** (object 5)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`

- **NSString** (object 6)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '73706c697456696577436f6e74726f6c6c6572', '$text': 'splitViewController'}`

- **NSArray** (object 7)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 1}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 13}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 9}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 30}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 28}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 15}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 10}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 32}`

- **NSString** (object 8)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '6d617374657256696577436f6e74726f6c6c6572', '$text': 'masterViewController'}`

- **UIRuntimeOutletConnection** (object 9)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 23}`
    - `UISource` (type 10): `{'$ref': 14}`
    - `UIDestination` (type 10): `{'$ref': 4}`

- **UIRuntimeOutletConnection** (object 10)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 6}`
    - `UISource` (type 10): `{'$ref': 11}`
    - `UIDestination` (type 10): `{'$ref': 14}`

- **NSString** (object 12)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '7b3235302c203235307d', '$text': '{250, 250}'}`

- **UIRuntimeOutletConnection** (object 13)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 27}`
    - `UISource` (type 10): `{'$ref': 4}`
    - `UIDestination` (type 10): `{'$ref': 11}`

- **UIRuntimeOutletConnection** (object 15)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 19}`
    - `UISource` (type 10): `{'$ref': 11}`
    - `UIDestination` (type 10): `{'$ref': 4}`

- **NSString** (object 16)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '43617463684e6f74657341707044656c65676174655f69506164', '$text': 'CatchNotesAppDelegate_iPad'}`

- **NSString** (object 19)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '7072696d6172794e6f746556696577436f6e74726f6c6c6572', '$text': 'primaryNoteViewController'}`

- **NSArray** (object 20)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 29}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 31}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 11}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 18}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 36}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 4}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 14}`

- **NSString** (object 21)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '4d4753706c697456696577436f6e74726f6c6c6572', '$text': 'MGSplitViewController'}`

- **NSString** (object 22)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '77696e646f77', '$text': 'window'}`

- **NSString** (object 23)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '64657461696c56696577436f6e74726f6c6c6572', '$text': 'detailViewController'}`

- **NSString** (object 24)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '7072696d6172794e617669676174696f6e436f6e74726f6c6c6572', '$text': 'primaryNavigationController'}`

- **NSString** (object 25)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '49424669727374526573706f6e646572', '$text': 'IBFirstResponder'}`

- **NSString** (object 26)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '5549437573746f6d4f626a656374', '$text': 'UICustomObject'}`

- **NSString** (object 27)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '64656c6567617465', '$text': 'delegate'}`

- **UIRuntimeOutletConnection** (object 28)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 24}`
    - `UISource` (type 10): `{'$ref': 11}`
    - `UIDestination` (type 10): `{'$ref': 36}`

- **UIRuntimeOutletConnection** (object 30)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 8}`
    - `UISource` (type 10): `{'$ref': 14}`
    - `UIDestination` (type 10): `{'$ref': 36}`

- **UIProxyObject** (object 31)
  - class: `UIProxyObject`
  - raw values:
    - `UIProxiedObjectIdentifier` (type 10): `{'$ref': 25}`

- **UIRuntimeOutletConnection** (object 32)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 22}`
    - `UISource` (type 10): `{'$ref': 11}`
    - `UIDestination` (type 10): `{'$ref': 18}`

- **NSArray** (object 33)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 29}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 31}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 11}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 18}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 36}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 4}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 14}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 17}`

- **NSString** (object 34)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '5061644e6f746556696577436f6e74726f6c6c6572', '$text': 'PadNoteViewController'}`

- **NSString** (object 35)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '494246696c65734f776e6572', '$text': 'IBFilesOwner'}`

