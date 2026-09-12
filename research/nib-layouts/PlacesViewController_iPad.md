# PlacesViewController_iPad

Recovered layout for `PlacesViewController_iPad.nib`. Every interpreted value appears beside the
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

- **UIProxyObject** (object 4)
  - class: `UIProxyObject`
  - outlet: `view` to object 8 (UIView)
  - outlet: `navItem` to object 30 (UINavigationItem)
  - outlet: `tableView` to object 26 (UITableView)
  - target/action: `refreshAction:` from object 29 (UIBarButtonItem) to object 4 (UIProxyObject), event mask not encoded
  - target/action: `cancelAction:` from object 23 (UIBarButtonItem) to object 4 (UIProxyObject), event mask not encoded
  - raw values:
    - `UIProxiedObjectIdentifier` (type 10): `{'$ref': 31}`

- **UIView** (object 8)
  - class: `UIView`
  - frame: (0, 0, 540, 600)
  - raw UIBounds: (0, 0, 540, 600)
  - raw UICenter: (270, 300)
  - autoresizing mask: 18
  - background color: system color tableBackgroundColor
  - hidden: not encoded
  - opaque: false
  - tag: not encoded
  - raw values:
    - `UIBounds` (type 8): `{'$data_hex': '0600000000000000000000074400001644', '$floats': [0.0, 0.0, 540.0, 600.0]}`
    - `UICenter` (type 8): `{'$data_hex': '060000874300009643', '$floats': [270.0, 300.0]}`
    - `UISubviews` (type 10): `{'$ref': 36}`
    - `UIBackgroundColor` (type 10): `{'$ref': 10}`
    - `UIOpaque` (type 5): `False`
    - `UIAutoresizeSubviews` (type 5): `False`
    - `UIAutoresizingMask` (type 0): `18`
  - **UITableView** (object 26)
    - class: `UITableView`
    - frame: (0, 44, 540, 556)
    - raw UIBounds: (0, 0, 540, 556)
    - raw UICenter: (270, 322)
    - autoresizing mask: 18
    - background color: system color tableBackgroundColor
    - hidden: not encoded
    - opaque: false
    - tag: not encoded
    - outlet: `dataSource` to object 4 (UIProxyObject)
    - outlet: `delegate` to object 4 (UIProxyObject)
    - raw values:
      - `UIBounds` (type 8): `{'$data_hex': '0600000000000000000000074400000b44', '$floats': [0.0, 0.0, 540.0, 556.0]}`
      - `UICenter` (type 8): `{'$data_hex': '06000087430000a143', '$floats': [270.0, 322.0]}`
      - `UIBackgroundColor` (type 10): `{'$ref': 10}`
      - `UIOpaque` (type 5): `False`
      - `UIAutoresizeSubviews` (type 5): `False`
      - `UIAutoresizingMask` (type 0): `18`
      - `UIClipsToBounds` (type 5): `False`
      - `UIBouncesZoom` (type 5): `False`
      - `UIAlwaysBounceVertical` (type 5): `False`
      - `UIContentSize` (type 8): `{'$data_hex': '060000074400000000', '$floats': [540.0, 0.0]}`
      - `UISeparatorStyle` (type 0): `1`
      - `UISeparatorStyleIOS5AndLater` (type 0): `1`
      - `UIShowsSelectionImmediatelyOnTouchBegin` (type 5): `False`
  - **UINavigationBar** (object 6)
    - class: `UINavigationBar`
    - frame: (0, 0, 540, 44)
    - raw UIBounds: (0, 0, 540, 44)
    - raw UICenter: (270, 22)
    - autoresizing mask: 34
    - background color: not encoded
    - hidden: not encoded
    - opaque: false
    - tag: not encoded
    - raw values:
      - `UIBounds` (type 8): `{'$data_hex': '0600000000000000000000074400003042', '$floats': [0.0, 0.0, 540.0, 44.0]}`
      - `UICenter` (type 8): `{'$data_hex': '06000087430000b041', '$floats': [270.0, 22.0]}`
      - `UIOpaque` (type 5): `False`
      - `UIAutoresizeSubviews` (type 5): `False`
      - `UIAutoresizingMask` (type 0): `34`
      - `UIViewContentHuggingPriority` (type 10): `{'$ref': 24}`
      - `UIItems` (type 10): `{'$ref': 9}`

- **UIBarButtonItem** (object 23)
  - class: `UIBarButtonItem`
  - target/action: `cancelAction:` from object 23 (UIBarButtonItem) to object 4 (UIProxyObject), event mask not encoded
  - raw values:
    - `UIEnabled` (type 5): `False`
    - `UIIsSystemItem` (type 5): `False`
    - `UISystemItem` (type 0): `1`
    - `UIStyle` (type 0): `1`

- **UIBarButtonItem** (object 29)
  - class: `UIBarButtonItem`
  - target/action: `refreshAction:` from object 29 (UIBarButtonItem) to object 4 (UIProxyObject), event mask not encoded
  - raw values:
    - `UIEnabled` (type 5): `False`
    - `UIIsSystemItem` (type 5): `False`
    - `UISystemItem` (type 0): `13`
    - `UIStyle` (type 0): `1`

## Supporting objects

These objects carry no geometry, contain no view, and hold no
connection. They remain here because a reader auditing an
interpretation follows a reference into them.

- **NSObject** (object 0)
  - class: `NSObject`
  - raw values:
    - `UINibTopLevelObjectsKey` (type 10): `{'$ref': 28}`
    - `UINibObjectsKey` (type 10): `{'$ref': 18}`
    - `UINibConnectionsKey` (type 10): `{'$ref': 13}`
    - `UINibVisibleWindowsKey` (type 10): `{'$ref': 7}`
    - `UINibAccessibilityConfigurationsKey` (type 10): `{'$ref': 7}`
    - `UINibKeyValuePairsKey` (type 10): `{'$ref': 7}`

- **NSString** (object 1)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '49424669727374526573706f6e646572', '$text': 'IBFirstResponder'}`

- **UIRuntimeOutletConnection** (object 2)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 12}`
    - `UISource` (type 10): `{'$ref': 26}`
    - `UIDestination` (type 10): `{'$ref': 4}`

- **NSArray** (object 3)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 23}`

- **UIRuntimeOutletConnection** (object 5)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 34}`
    - `UISource` (type 10): `{'$ref': 4}`
    - `UIDestination` (type 10): `{'$ref': 8}`

- **NSArray** (object 7)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`

- **NSMutableArray** (object 9)
  - class: `NSMutableArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 30}`

- **UIColor** (object 10)
  - class: `UIColor`
  - raw values:
    - `UISystemColorName` (type 10): `{'$ref': 25}`
    - `UIColorComponentCount` (type 0): `4`
    - `UIRed` (type 6): `1.0`
    - `UIGreen` (type 6): `1.0`
    - `UIBlue` (type 6): `1.0`
    - `UIAlpha` (type 6): `1.0`
    - `NSRGB` (type 8): `{'$data_hex': '3120312031', '$text': '1 1 1'}`
    - `NSColorSpace` (type 0): `2`

- **UIRuntimeEventConnection** (object 11)
  - class: `UIRuntimeEventConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 27}`
    - `UISource` (type 10): `{'$ref': 29}`
    - `UIDestination` (type 10): `{'$ref': 4}`

- **NSString** (object 12)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '64617461536f75726365', '$text': 'dataSource'}`

- **NSArray** (object 13)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 21}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 11}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 2}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 22}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 16}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 35}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 5}`

- **NSArray** (object 14)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 29}`

- **NSString** (object 15)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '506c61636573', '$text': 'Places'}`

- **UIRuntimeOutletConnection** (object 16)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 33}`
    - `UISource` (type 10): `{'$ref': 4}`
    - `UIDestination` (type 10): `{'$ref': 30}`

- **NSString** (object 17)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '64656c6567617465', '$text': 'delegate'}`

- **NSArray** (object 18)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 4}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 20}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 8}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 26}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 6}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 30}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 23}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 29}`

- **NSString** (object 19)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '7461626c6556696577', '$text': 'tableView'}`

- **UIProxyObject** (object 20)
  - class: `UIProxyObject`
  - raw values:
    - `UIProxiedObjectIdentifier` (type 10): `{'$ref': 1}`

- **UIRuntimeEventConnection** (object 21)
  - class: `UIRuntimeEventConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 32}`
    - `UISource` (type 10): `{'$ref': 23}`
    - `UIDestination` (type 10): `{'$ref': 4}`

- **UIRuntimeOutletConnection** (object 22)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 17}`
    - `UISource` (type 10): `{'$ref': 26}`
    - `UIDestination` (type 10): `{'$ref': 4}`

- **NSString** (object 24)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '7b3235302c203235307d', '$text': '{250, 250}'}`

- **NSString** (object 25)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '7461626c654261636b67726f756e64436f6c6f72', '$text': 'tableBackgroundColor'}`

- **NSString** (object 27)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '72656672657368416374696f6e3a', '$text': 'refreshAction:'}`

- **NSArray** (object 28)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 4}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 20}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 8}`

- **UINavigationItem** (object 30)
  - class: `UINavigationItem`
  - raw values:
    - `UITitle` (type 10): `{'$ref': 15}`
    - `UILeftBarButtonItem` (type 10): `{'$ref': 23}`
    - `UIRightBarButtonItem` (type 10): `{'$ref': 29}`
    - `UILeftBarButtonItems` (type 10): `{'$ref': 3}`
    - `UIRightBarButtonItems` (type 10): `{'$ref': 14}`
    - `UINavigationBar` (type 10): `{'$ref': 6}`

- **NSString** (object 31)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '494246696c65734f776e6572', '$text': 'IBFilesOwner'}`

- **NSString** (object 32)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '63616e63656c416374696f6e3a', '$text': 'cancelAction:'}`

- **NSString** (object 33)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '6e61764974656d', '$text': 'navItem'}`

- **NSString** (object 34)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '76696577', '$text': 'view'}`

- **UIRuntimeOutletConnection** (object 35)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 19}`
    - `UISource` (type 10): `{'$ref': 4}`
    - `UIDestination` (type 10): `{'$ref': 26}`

- **NSMutableArray** (object 36)
  - class: `NSMutableArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 26}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 6}`

