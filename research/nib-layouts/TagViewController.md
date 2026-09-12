# TagViewController

Recovered layout for `TagViewController.nib`. Every interpreted value appears beside the
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

- **UITableView** (object 4)
  - class: `UITableView`
  - frame: (0, 0, 320, 460)
  - raw UIBounds: (0, 0, 320, 460)
  - raw UICenter: (160, 230)
  - autoresizing mask: 18
  - background color: system color tableBackgroundColor
  - hidden: not encoded
  - opaque: not encoded
  - tag: not encoded
  - outlet: `dataSource` to object 27 (UIProxyObject)
  - outlet: `delegate` to object 27 (UIProxyObject)
  - raw values:
    - `UIBounds` (type 8): `{'$data_hex': '0600000000000000000000a0430000e643', '$floats': [0.0, 0.0, 320.0, 460.0]}`
    - `UICenter` (type 8): `{'$data_hex': '060000204300006643', '$floats': [160.0, 230.0]}`
    - `UISubviews` (type 10): `{'$ref': 28}`
    - `UIBackgroundColor` (type 10): `{'$ref': 6}`
    - `UIAutoresizeSubviews` (type 5): `False`
    - `UIAutoresizingMask` (type 0): `18`
    - `UIClearsContextBeforeDrawing` (type 4): `True`
    - `UIClipsToBounds` (type 5): `False`
    - `UIContentSize` (type 8): `{'$data_hex': '060000a0430000fc43', '$floats': [320.0, 504.0]}`
    - `UISeparatorStyle` (type 0): `1`
    - `UISeparatorStyleIOS5AndLater` (type 0): `1`
    - `UIShowsSelectionImmediatelyOnTouchBegin` (type 5): `False`
    - `UITableHeaderView` (type 10): `{'$ref': 3}`
  - **UISearchBar** (object 3)
    - class: `UISearchBar`
    - frame: (0, 0, 320, 44)
    - raw UIBounds: (0, 0, 320, 44)
    - raw UICenter: (160, 22)
    - autoresizing mask: 34
    - background color: not encoded
    - hidden: not encoded
    - opaque: false
    - tag: not encoded
    - outlet: `delegate` to object 27 (UIProxyObject)
    - raw values:
      - `UIBounds` (type 8): `{'$data_hex': '0600000000000000000000a04300003042', '$floats': [0.0, 0.0, 320.0, 44.0]}`
      - `UICenter` (type 8): `{'$data_hex': '06000020430000b041', '$floats': [160.0, 22.0]}`
      - `UIOpaque` (type 5): `False`
      - `UIAutoresizeSubviews` (type 5): `False`
      - `UIAutoresizingMask` (type 0): `34`
      - `UIContentMode` (type 0): `3`
      - `UIViewContentHuggingPriority` (type 10): `{'$ref': 1}`

- **UISearchDisplayController** (object 23)
  - class: `UISearchDisplayController`
  - outlet: `delegate` to object 27 (UIProxyObject)
  - outlet: `searchBar` to object 3 (UISearchBar)
  - outlet: `searchResultsDelegate` to object 27 (UIProxyObject)
  - outlet: `searchResultsDataSource` to object 27 (UIProxyObject)
  - outlet: `searchContentsController` to object 27 (UIProxyObject)
  - raw values:

- **UIProxyObject** (object 27)
  - class: `UIProxyObject`
  - outlet: `searchDisplayController` to object 23 (UISearchDisplayController)
  - outlet: `view` to object 4 (UITableView)
  - raw values:
    - `UIProxiedObjectIdentifier` (type 10): `{'$ref': 10}`

## Supporting objects

These objects carry no geometry, contain no view, and hold no
connection. They remain here because a reader auditing an
interpretation follows a reference into them.

- **NSObject** (object 0)
  - class: `NSObject`
  - raw values:
    - `UINibTopLevelObjectsKey` (type 10): `{'$ref': 19}`
    - `UINibObjectsKey` (type 10): `{'$ref': 17}`
    - `UINibConnectionsKey` (type 10): `{'$ref': 26}`
    - `UINibVisibleWindowsKey` (type 10): `{'$ref': 11}`
    - `UINibAccessibilityConfigurationsKey` (type 10): `{'$ref': 11}`
    - `UINibKeyValuePairsKey` (type 10): `{'$ref': 11}`

- **NSString** (object 1)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '7b3235302c203235307d', '$text': '{250, 250}'}`

- **NSString** (object 2)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '49424669727374526573706f6e646572', '$text': 'IBFirstResponder'}`

- **UIRuntimeOutletConnection** (object 5)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 20}`
    - `UISource` (type 10): `{'$ref': 23}`
    - `UIDestination` (type 10): `{'$ref': 27}`

- **UIColor** (object 6)
  - class: `UIColor`
  - raw values:
    - `UISystemColorName` (type 10): `{'$ref': 21}`
    - `UIColorComponentCount` (type 0): `4`
    - `UIRed` (type 6): `1.0`
    - `UIGreen` (type 6): `1.0`
    - `UIBlue` (type 6): `1.0`
    - `UIAlpha` (type 6): `1.0`
    - `NSRGB` (type 8): `{'$data_hex': '3120312031', '$text': '1 1 1'}`
    - `NSColorSpace` (type 0): `2`

- **UIRuntimeOutletConnection** (object 7)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 9}`
    - `UISource` (type 10): `{'$ref': 4}`
    - `UIDestination` (type 10): `{'$ref': 27}`

- **NSString** (object 8)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '736561726368526573756c747344617461536f75726365', '$text': 'searchResultsDataSource'}`

- **NSString** (object 9)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '64617461536f75726365', '$text': 'dataSource'}`

- **NSString** (object 10)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '494246696c65734f776e6572', '$text': 'IBFilesOwner'}`

- **NSArray** (object 11)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`

- **NSString** (object 12)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '736561726368426172', '$text': 'searchBar'}`

- **UIRuntimeOutletConnection** (object 13)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 12}`
    - `UISource` (type 10): `{'$ref': 23}`
    - `UIDestination` (type 10): `{'$ref': 3}`

- **NSString** (object 14)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '736561726368446973706c6179436f6e74726f6c6c6572', '$text': 'searchDisplayController'}`

- **UIRuntimeOutletConnection** (object 15)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 24}`
    - `UISource` (type 10): `{'$ref': 23}`
    - `UIDestination` (type 10): `{'$ref': 27}`

- **UIRuntimeOutletConnection** (object 16)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 14}`
    - `UISource` (type 10): `{'$ref': 27}`
    - `UIDestination` (type 10): `{'$ref': 23}`

- **NSArray** (object 17)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 27}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 29}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 4}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 23}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 3}`

- **UIRuntimeOutletConnection** (object 18)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 20}`
    - `UISource` (type 10): `{'$ref': 4}`
    - `UIDestination` (type 10): `{'$ref': 27}`

- **NSArray** (object 19)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 27}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 29}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 4}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 23}`

- **NSString** (object 20)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '64656c6567617465', '$text': 'delegate'}`

- **NSString** (object 21)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '7461626c654261636b67726f756e64436f6c6f72', '$text': 'tableBackgroundColor'}`

- **NSString** (object 22)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '76696577', '$text': 'view'}`

- **NSString** (object 24)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '736561726368526573756c747344656c6567617465', '$text': 'searchResultsDelegate'}`

- **UIRuntimeOutletConnection** (object 25)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 20}`
    - `UISource` (type 10): `{'$ref': 3}`
    - `UIDestination` (type 10): `{'$ref': 27}`

- **NSArray** (object 26)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 7}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 18}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 5}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 25}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 13}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 31}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 16}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 30}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 15}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 32}`

- **NSMutableArray** (object 28)
  - class: `NSMutableArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 3}`

- **UIProxyObject** (object 29)
  - class: `UIProxyObject`
  - raw values:
    - `UIProxiedObjectIdentifier` (type 10): `{'$ref': 2}`

- **UIRuntimeOutletConnection** (object 30)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 8}`
    - `UISource` (type 10): `{'$ref': 23}`
    - `UIDestination` (type 10): `{'$ref': 27}`

- **UIRuntimeOutletConnection** (object 31)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 33}`
    - `UISource` (type 10): `{'$ref': 23}`
    - `UIDestination` (type 10): `{'$ref': 27}`

- **UIRuntimeOutletConnection** (object 32)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 22}`
    - `UISource` (type 10): `{'$ref': 27}`
    - `UIDestination` (type 10): `{'$ref': 4}`

- **NSString** (object 33)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '736561726368436f6e74656e7473436f6e74726f6c6c6572', '$text': 'searchContentsController'}`

