# MainWindow_iPhone

Recovered layout for `MainWindow_iPhone.nib`. Every interpreted value appears beside the
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

- **UIWindow** (object 11)
  - class: `UIWindow`
  - frame: (0, 0, 320, 480)
  - raw UIBounds: (0, 0, 320, 480)
  - raw UICenter: (160, 240)
  - autoresizing mask: 36
  - background color: rgba(1, 1, 1, 1)
  - hidden: not encoded
  - opaque: not encoded
  - tag: not encoded
  - raw values:
    - `UIBounds` (type 8): `{'$data_hex': '0600000000000000000000a0430000f043', '$floats': [0.0, 0.0, 320.0, 480.0]}`
    - `UICenter` (type 8): `{'$data_hex': '060000204300007043', '$floats': [160.0, 240.0]}`
    - `UIBackgroundColor` (type 10): `{'$ref': 6}`
    - `UIAutoresizeSubviews` (type 5): `False`
    - `UIAutoresizingMask` (type 0): `36`
    - `UIClearsContextBeforeDrawing` (type 4): `True`
    - `UIResizesToFullScreen` (type 5): `False`

- **UINavigationController** (object 13)
  - class: `UINavigationController`
  - raw values:
    - `UINavigationBar` (type 10): `{'$ref': 8}`
  - **UINavigationBar** (object 8)
    - class: `UINavigationBar`
    - frame: (0, 0, 320, 44)
    - raw UIBounds: (0, 0, 320, 44)
    - raw UICenter: (160, 22)
    - autoresizing mask: 2
    - background color: not encoded
    - hidden: not encoded
    - opaque: not encoded
    - tag: not encoded
    - raw values:
      - `UIBounds` (type 8): `{'$data_hex': '0600000000000000000000a04300003042', '$floats': [0.0, 0.0, 320.0, 44.0]}`
      - `UICenter` (type 8): `{'$data_hex': '06000020430000b041', '$floats': [160.0, 22.0]}`
      - `UIMultipleTouchEnabled` (type 5): `False`
      - `UIAutoresizeSubviews` (type 5): `False`
      - `UIAutoresizingMask` (type 0): `2`
      - `UIClipsToBounds` (type 5): `False`
      - `UIViewContentHuggingPriority` (type 10): `{'$ref': 2}`
      - `UIDelegate` (type 10): `{'$ref': 13}`

- **UIProxyObject** (object 17)
  - class: `UIProxyObject`
  - outlet: `delegate` to object 20 (CatchNotesAppDelegate_iPhone)
  - raw values:
    - `UIProxiedObjectIdentifier` (type 10): `{'$ref': 16}`

- **CatchNotesAppDelegate_iPhone** (object 20)
  - class: `CatchNotesAppDelegate_iPhone`
  - encoded as: `UIClassSwapper` swapping `UICustomObject`
  - outlet: `window` to object 11 (UIWindow)
  - raw values:
    - `UIClassName` (type 10): `{'$ref': 14}`
    - `UIOriginalClassName` (type 10): `{'$ref': 15}`

## Supporting objects

These objects carry no geometry, contain no view, and hold no
connection. They remain here because a reader auditing an
interpretation follows a reference into them.

- **NSObject** (object 0)
  - class: `NSObject`
  - raw values:
    - `UINibTopLevelObjectsKey` (type 10): `{'$ref': 19}`
    - `UINibObjectsKey` (type 10): `{'$ref': 1}`
    - `UINibConnectionsKey` (type 10): `{'$ref': 9}`
    - `UINibVisibleWindowsKey` (type 10): `{'$ref': 3}`
    - `UINibAccessibilityConfigurationsKey` (type 10): `{'$ref': 3}`
    - `UINibKeyValuePairsKey` (type 10): `{'$ref': 3}`

- **NSArray** (object 1)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 17}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 4}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 20}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 11}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 13}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 8}`

- **NSString** (object 2)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '7b3235302c203235307d', '$text': '{250, 250}'}`

- **NSArray** (object 3)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`

- **UIProxyObject** (object 4)
  - class: `UIProxyObject`
  - raw values:
    - `UIProxiedObjectIdentifier` (type 10): `{'$ref': 18}`

- **UIRuntimeOutletConnection** (object 5)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 10}`
    - `UISource` (type 10): `{'$ref': 17}`
    - `UIDestination` (type 10): `{'$ref': 20}`

- **UIColor** (object 6)
  - class: `UIColor`
  - raw values:
    - `UIColorComponentCount` (type 0): `4`
    - `UIRed` (type 6): `1.0`
    - `UIGreen` (type 6): `1.0`
    - `UIBlue` (type 6): `1.0`
    - `UIAlpha` (type 6): `1.0`
    - `NSRGB` (type 8): `{'$data_hex': '3120312031', '$text': '1 1 1'}`
    - `NSColorSpace` (type 0): `2`

- **NSString** (object 7)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '77696e646f77', '$text': 'window'}`

- **NSArray** (object 9)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 5}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 12}`

- **NSString** (object 10)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '64656c6567617465', '$text': 'delegate'}`

- **UIRuntimeOutletConnection** (object 12)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 7}`
    - `UISource` (type 10): `{'$ref': 20}`
    - `UIDestination` (type 10): `{'$ref': 11}`

- **NSString** (object 14)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '43617463684e6f74657341707044656c65676174655f6950686f6e65', '$text': 'CatchNotesAppDelegate_iPhone'}`

- **NSString** (object 15)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '5549437573746f6d4f626a656374', '$text': 'UICustomObject'}`

- **NSString** (object 16)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '494246696c65734f776e6572', '$text': 'IBFilesOwner'}`

- **NSString** (object 18)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '49424669727374526573706f6e646572', '$text': 'IBFirstResponder'}`

- **NSArray** (object 19)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 17}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 4}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 20}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 11}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 13}`

