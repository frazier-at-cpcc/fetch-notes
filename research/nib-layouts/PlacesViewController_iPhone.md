# PlacesViewController_iPhone

Recovered layout for `PlacesViewController_iPhone.nib`. Every interpreted value appears beside the
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

- **UINavigationItem** (object 1)
  - class: `UINavigationItem`
  - raw values:
    - `UITitle` (type 10): `{'$ref': 2}`
    - `UILeftBarButtonItem` (type 10): `{'$ref': 25}`
    - `UIRightBarButtonItem` (type 10): `{'$ref': 9}`
    - `UILeftBarButtonItems` (type 10): `{'$ref': 10}`
    - `UIRightBarButtonItems` (type 10): `{'$ref': 26}`
    - `UINavigationBar` (type 10): `{'$ref': 8}`
  - **UINavigationBar** (object 8)
    - class: `UINavigationBar`
    - frame: (0, 0, 320, 44)
    - raw UIBounds: (0, 0, 320, 44)
    - raw UICenter: (160, 22)
    - autoresizing mask: 34
    - background color: not encoded
    - hidden: not encoded
    - opaque: false
    - tag: not encoded
    - raw values:
      - `UIBounds` (type 8): `{'$data_hex': '0600000000000000000000a04300003042', '$floats': [0.0, 0.0, 320.0, 44.0]}`
      - `UICenter` (type 8): `{'$data_hex': '06000020430000b041', '$floats': [160.0, 22.0]}`
      - `UIOpaque` (type 5): `False`
      - `UIAutoresizeSubviews` (type 5): `False`
      - `UIAutoresizingMask` (type 0): `34`
      - `UIViewContentHuggingPriority` (type 10): `{'$ref': 30}`
      - `UIItems` (type 10): `{'$ref': 34}`

- **UIBarButtonItem** (object 9)
  - class: `UIBarButtonItem`
  - target/action: `refreshAction:` from object 9 (UIBarButtonItem) to object 11 (UIProxyObject), event mask not encoded
  - raw values:
    - `UIEnabled` (type 5): `False`
    - `UIIsSystemItem` (type 5): `False`
    - `UISystemItem` (type 0): `13`
    - `UIStyle` (type 0): `1`

- **UIProxyObject** (object 11)
  - class: `UIProxyObject`
  - outlet: `view` to object 17 (UIView)
  - outlet: `navItem` to object 1 (UINavigationItem)
  - outlet: `tableView` to object 32 (UITableView)
  - target/action: `cancelAction:` from object 25 (UIBarButtonItem) to object 11 (UIProxyObject), event mask not encoded
  - target/action: `refreshAction:` from object 9 (UIBarButtonItem) to object 11 (UIProxyObject), event mask not encoded
  - raw values:
    - `UIProxiedObjectIdentifier` (type 10): `{'$ref': 31}`

- **UIView** (object 17)
  - class: `UIView`
  - frame: (0, 0, 320, 460)
  - raw UIBounds: (0, 0, 320, 460)
  - raw UICenter: (160, 230)
  - autoresizing mask: 18
  - background color: system color tableBackgroundColor
  - hidden: not encoded
  - opaque: false
  - tag: not encoded
  - raw values:
    - `UIBounds` (type 8): `{'$data_hex': '0600000000000000000000a0430000e643', '$floats': [0.0, 0.0, 320.0, 460.0]}`
    - `UICenter` (type 8): `{'$data_hex': '060000204300006643', '$floats': [160.0, 230.0]}`
    - `UISubviews` (type 10): `{'$ref': 28}`
    - `UIBackgroundColor` (type 10): `{'$ref': 27}`
    - `UIOpaque` (type 5): `False`
    - `UIAutoresizeSubviews` (type 5): `False`
    - `UIAutoresizingMask` (type 0): `18`
  - **UITableView** (object 32)
    - class: `UITableView`
    - frame: (0, 44, 320, 416)
    - raw UIBounds: (0, 0, 320, 416)
    - raw UICenter: (160, 252)
    - autoresizing mask: 18
    - background color: system color tableBackgroundColor
    - hidden: not encoded
    - opaque: false
    - tag: not encoded
    - outlet: `delegate` to object 11 (UIProxyObject)
    - outlet: `dataSource` to object 11 (UIProxyObject)
    - raw values:
      - `UIBounds` (type 8): `{'$data_hex': '0600000000000000000000a0430000d043', '$floats': [0.0, 0.0, 320.0, 416.0]}`
      - `UICenter` (type 8): `{'$data_hex': '060000204300007c43', '$floats': [160.0, 252.0]}`
      - `UIBackgroundColor` (type 10): `{'$ref': 27}`
      - `UIOpaque` (type 5): `False`
      - `UIAutoresizeSubviews` (type 5): `False`
      - `UIAutoresizingMask` (type 0): `18`
      - `UIClipsToBounds` (type 5): `False`
      - `UIBouncesZoom` (type 5): `False`
      - `UIAlwaysBounceVertical` (type 5): `False`
      - `UIContentSize` (type 8): `{'$data_hex': '060000a04300000000', '$floats': [320.0, 0.0]}`
      - `UISeparatorStyle` (type 0): `1`
      - `UISeparatorStyleIOS5AndLater` (type 0): `1`
      - `UIShowsSelectionImmediatelyOnTouchBegin` (type 5): `False`

- **UIBarButtonItem** (object 25)
  - class: `UIBarButtonItem`
  - target/action: `cancelAction:` from object 25 (UIBarButtonItem) to object 11 (UIProxyObject), event mask not encoded
  - raw values:
    - `UIEnabled` (type 5): `False`
    - `UIIsSystemItem` (type 5): `False`
    - `UISystemItem` (type 0): `1`
    - `UIStyle` (type 0): `1`

## Supporting objects

These objects carry no geometry, contain no view, and hold no
connection. They remain here because a reader auditing an
interpretation follows a reference into them.

- **NSObject** (object 0)
  - class: `NSObject`
  - raw values:
    - `UINibTopLevelObjectsKey` (type 10): `{'$ref': 12}`
    - `UINibObjectsKey` (type 10): `{'$ref': 18}`
    - `UINibConnectionsKey` (type 10): `{'$ref': 29}`
    - `UINibVisibleWindowsKey` (type 10): `{'$ref': 3}`
    - `UINibAccessibilityConfigurationsKey` (type 10): `{'$ref': 3}`
    - `UINibKeyValuePairsKey` (type 10): `{'$ref': 3}`

- **NSString** (object 2)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '506c61636573', '$text': 'Places'}`

- **NSArray** (object 3)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`

- **UIRuntimeOutletConnection** (object 4)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 14}`
    - `UISource` (type 10): `{'$ref': 32}`
    - `UIDestination` (type 10): `{'$ref': 11}`

- **UIRuntimeOutletConnection** (object 5)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 6}`
    - `UISource` (type 10): `{'$ref': 32}`
    - `UIDestination` (type 10): `{'$ref': 11}`

- **NSString** (object 6)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '64617461536f75726365', '$text': 'dataSource'}`

- **NSString** (object 7)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '7461626c654261636b67726f756e64436f6c6f72', '$text': 'tableBackgroundColor'}`

- **NSArray** (object 10)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 25}`

- **NSArray** (object 12)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 11}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 22}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 17}`

- **UIRuntimeOutletConnection** (object 13)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 36}`
    - `UISource` (type 10): `{'$ref': 11}`
    - `UIDestination` (type 10): `{'$ref': 17}`

- **NSString** (object 14)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '64656c6567617465', '$text': 'delegate'}`

- **NSString** (object 15)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '72656672657368416374696f6e3a', '$text': 'refreshAction:'}`

- **NSString** (object 16)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '7461626c6556696577', '$text': 'tableView'}`

- **NSArray** (object 18)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 11}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 22}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 17}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 32}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 8}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 1}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 25}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 9}`

- **UIRuntimeOutletConnection** (object 19)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 35}`
    - `UISource` (type 10): `{'$ref': 11}`
    - `UIDestination` (type 10): `{'$ref': 1}`

- **UIRuntimeOutletConnection** (object 20)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 16}`
    - `UISource` (type 10): `{'$ref': 11}`
    - `UIDestination` (type 10): `{'$ref': 32}`

- **NSString** (object 21)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '63616e63656c416374696f6e3a', '$text': 'cancelAction:'}`

- **UIProxyObject** (object 22)
  - class: `UIProxyObject`
  - raw values:
    - `UIProxiedObjectIdentifier` (type 10): `{'$ref': 33}`

- **UIRuntimeEventConnection** (object 23)
  - class: `UIRuntimeEventConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 21}`
    - `UISource` (type 10): `{'$ref': 25}`
    - `UIDestination` (type 10): `{'$ref': 11}`

- **UIRuntimeEventConnection** (object 24)
  - class: `UIRuntimeEventConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 15}`
    - `UISource` (type 10): `{'$ref': 9}`
    - `UIDestination` (type 10): `{'$ref': 11}`

- **NSArray** (object 26)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 9}`

- **UIColor** (object 27)
  - class: `UIColor`
  - raw values:
    - `UISystemColorName` (type 10): `{'$ref': 7}`
    - `UIColorComponentCount` (type 0): `4`
    - `UIRed` (type 6): `1.0`
    - `UIGreen` (type 6): `1.0`
    - `UIBlue` (type 6): `1.0`
    - `UIAlpha` (type 6): `1.0`
    - `NSRGB` (type 8): `{'$data_hex': '3120312031', '$text': '1 1 1'}`
    - `NSColorSpace` (type 0): `2`

- **NSMutableArray** (object 28)
  - class: `NSMutableArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 32}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 8}`

- **NSArray** (object 29)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 23}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 24}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 5}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 4}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 19}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 20}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 13}`

- **NSString** (object 30)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '7b3235302c203235307d', '$text': '{250, 250}'}`

- **NSString** (object 31)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '494246696c65734f776e6572', '$text': 'IBFilesOwner'}`

- **NSString** (object 33)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '49424669727374526573706f6e646572', '$text': 'IBFirstResponder'}`

- **NSMutableArray** (object 34)
  - class: `NSMutableArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 1}`

- **NSString** (object 35)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '6e61764974656d', '$text': 'navItem'}`

- **NSString** (object 36)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '76696577', '$text': 'view'}`

