# StreamsTableViewController

Recovered layout for `StreamsTableViewController.nib`. Every interpreted value appears beside the
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

- **UIProxyObject** (object 1)
  - class: `UIProxyObject`
  - outlet: `view` to object 8 (ATSDragToReorderTableView)
  - raw values:
    - `UIProxiedObjectIdentifier` (type 10): `{'$ref': 5}`

- **ATSDragToReorderTableView** (object 8)
  - class: `ATSDragToReorderTableView`
  - encoded as: `UIClassSwapper` swapping `UITableView`
  - frame: (0, 0, 320, 460)
  - raw UIBounds: (0, 0, 320, 460)
  - raw UICenter: (160, 230)
  - autoresizing mask: 18
  - background color: system color tableBackgroundColor
  - hidden: not encoded
  - opaque: not encoded
  - tag: not encoded
  - outlet: `delegate` to object 1 (UIProxyObject)
  - outlet: `dataSource` to object 1 (UIProxyObject)
  - raw values:
    - `UIBounds` (type 8): `{'$data_hex': '0600000000000000000000a0430000e643', '$floats': [0.0, 0.0, 320.0, 460.0]}`
    - `UICenter` (type 8): `{'$data_hex': '060000204300006643', '$floats': [160.0, 230.0]}`
    - `UIBackgroundColor` (type 10): `{'$ref': 3}`
    - `UIAutoresizeSubviews` (type 5): `False`
    - `UIAutoresizingMask` (type 0): `18`
    - `UIClearsContextBeforeDrawing` (type 4): `True`
    - `UIClipsToBounds` (type 5): `False`
    - `UIContentSize` (type 8): `{'$data_hex': '060000a04300000000', '$floats': [320.0, 0.0]}`
    - `UISeparatorStyle` (type 0): `1`
    - `UISeparatorStyleIOS5AndLater` (type 0): `1`
    - `UIShowsSelectionImmediatelyOnTouchBegin` (type 5): `False`
    - `UIClassName` (type 10): `{'$ref': 15}`
    - `UIOriginalClassName` (type 10): `{'$ref': 7}`

## Supporting objects

These objects carry no geometry, contain no view, and hold no
connection. They remain here because a reader auditing an
interpretation follows a reference into them.

- **NSObject** (object 0)
  - class: `NSObject`
  - raw values:
    - `UINibTopLevelObjectsKey` (type 10): `{'$ref': 12}`
    - `UINibObjectsKey` (type 10): `{'$ref': 13}`
    - `UINibConnectionsKey` (type 10): `{'$ref': 14}`
    - `UINibVisibleWindowsKey` (type 10): `{'$ref': 4}`
    - `UINibAccessibilityConfigurationsKey` (type 10): `{'$ref': 4}`
    - `UINibKeyValuePairsKey` (type 10): `{'$ref': 4}`

- **NSString** (object 2)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '64617461536f75726365', '$text': 'dataSource'}`

- **UIColor** (object 3)
  - class: `UIColor`
  - raw values:
    - `UISystemColorName` (type 10): `{'$ref': 17}`
    - `UIColorComponentCount` (type 0): `4`
    - `UIRed` (type 6): `1.0`
    - `UIGreen` (type 6): `1.0`
    - `UIBlue` (type 6): `1.0`
    - `UIAlpha` (type 6): `1.0`
    - `NSRGB` (type 8): `{'$data_hex': '3120312031', '$text': '1 1 1'}`
    - `NSColorSpace` (type 0): `2`

- **NSArray** (object 4)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`

- **NSString** (object 5)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '494246696c65734f776e6572', '$text': 'IBFilesOwner'}`

- **NSString** (object 6)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '76696577', '$text': 'view'}`

- **NSString** (object 7)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '55495461626c6556696577', '$text': 'UITableView'}`

- **UIRuntimeOutletConnection** (object 9)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 10}`
    - `UISource` (type 10): `{'$ref': 8}`
    - `UIDestination` (type 10): `{'$ref': 1}`

- **NSString** (object 10)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '64656c6567617465', '$text': 'delegate'}`

- **UIRuntimeOutletConnection** (object 11)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 2}`
    - `UISource` (type 10): `{'$ref': 8}`
    - `UIDestination` (type 10): `{'$ref': 1}`

- **NSArray** (object 12)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 1}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 16}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 8}`

- **NSArray** (object 13)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 1}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 16}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 8}`

- **NSArray** (object 14)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 11}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 9}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 18}`

- **NSString** (object 15)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '41545344726167546f52656f726465725461626c6556696577', '$text': 'ATSDragToReorderTableView'}`

- **UIProxyObject** (object 16)
  - class: `UIProxyObject`
  - raw values:
    - `UIProxiedObjectIdentifier` (type 10): `{'$ref': 19}`

- **NSString** (object 17)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '7461626c654261636b67726f756e64436f6c6f72', '$text': 'tableBackgroundColor'}`

- **UIRuntimeOutletConnection** (object 18)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 6}`
    - `UISource` (type 10): `{'$ref': 1}`
    - `UIDestination` (type 10): `{'$ref': 8}`

- **NSString** (object 19)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '49424669727374526573706f6e646572', '$text': 'IBFirstResponder'}`

