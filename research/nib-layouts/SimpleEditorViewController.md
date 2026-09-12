# SimpleEditorViewController

Recovered layout for `SimpleEditorViewController.nib`. Every interpreted value appears beside the
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

- **UIProxyObject** (object 12)
  - class: `UIProxyObject`
  - outlet: `view` to object 13 (UIView)
  - outlet: `editor` to object 5 (UITextView)
  - raw values:
    - `UIProxiedObjectIdentifier` (type 10): `{'$ref': 16}`

- **UIView** (object 13)
  - class: `UIView`
  - frame: (0, 0, 320, 416)
  - raw UIBounds: (0, 0, 320, 416)
  - raw UICenter: (160, 208)
  - autoresizing mask: 18
  - background color: rgba(1, 1, 1, 1)
  - hidden: not encoded
  - opaque: false
  - tag: not encoded
  - raw values:
    - `UIBounds` (type 8): `{'$data_hex': '0600000000000000000000a0430000d043', '$floats': [0.0, 0.0, 320.0, 416.0]}`
    - `UICenter` (type 8): `{'$data_hex': '060000204300005043', '$floats': [160.0, 208.0]}`
    - `UISubviews` (type 10): `{'$ref': 3}`
    - `UIBackgroundColor` (type 10): `{'$ref': 7}`
    - `UIOpaque` (type 5): `False`
    - `UIAutoresizeSubviews` (type 5): `False`
    - `UIAutoresizingMask` (type 0): `18`
  - **UITextView** (object 5)
    - class: `UITextView`
    - frame: (0, 0, 320, 416)
    - raw UIBounds: (0, 0, 320, 416)
    - raw UICenter: (160, 208)
    - autoresizing mask: 18
    - background color: rgba(1, 1, 1, 1)
    - font: Helvetica 14pt
    - hidden: not encoded
    - opaque: false
    - tag: not encoded
    - raw values:
      - `UIBounds` (type 8): `{'$data_hex': '0600000000000000000000a0430000d043', '$floats': [0.0, 0.0, 320.0, 416.0]}`
      - `UICenter` (type 8): `{'$data_hex': '060000204300005043', '$floats': [160.0, 208.0]}`
      - `UISubviews` (type 10): `{'$ref': 10}`
      - `UIBackgroundColor` (type 10): `{'$ref': 7}`
      - `UIOpaque` (type 5): `False`
      - `UIMultipleTouchEnabled` (type 5): `False`
      - `UIAutoresizeSubviews` (type 5): `False`
      - `UIAutoresizingMask` (type 0): `18`
      - `UIClipsToBounds` (type 5): `False`
      - `UIBouncesZoom` (type 5): `False`
      - `UIContentSize` (type 8): `{'$data_hex': '060000a04300000842', '$floats': [320.0, 34.0]}`
      - `UIFont` (type 10): `{'$ref': 11}`
      - `UITextColor` (type 10): `{'$ref': 15}`
      - `UITextAlignment` (type 0): `0`
    - **UITextSelectionView** (object 18)
      - class: `UITextSelectionView`
      - autoresizing mask: not encoded
      - background color: not encoded
      - hidden: not encoded
      - opaque: false
      - tag: not encoded
      - raw values:
        - `UIOpaque` (type 5): `False`
        - `UIUserInteractionDisabled` (type 5): `False`
        - `UIAutoresizeSubviews` (type 5): `False`

## Supporting objects

These objects carry no geometry, contain no view, and hold no
connection. They remain here because a reader auditing an
interpretation follows a reference into them.

- **NSObject** (object 0)
  - class: `NSObject`
  - raw values:
    - `UINibTopLevelObjectsKey` (type 10): `{'$ref': 4}`
    - `UINibObjectsKey` (type 10): `{'$ref': 8}`
    - `UINibConnectionsKey` (type 10): `{'$ref': 21}`
    - `UINibVisibleWindowsKey` (type 10): `{'$ref': 1}`
    - `UINibAccessibilityConfigurationsKey` (type 10): `{'$ref': 1}`
    - `UINibKeyValuePairsKey` (type 10): `{'$ref': 1}`

- **NSArray** (object 1)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`

- **NSString** (object 2)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '49424669727374526573706f6e646572', '$text': 'IBFirstResponder'}`

- **NSMutableArray** (object 3)
  - class: `NSMutableArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 5}`

- **NSArray** (object 4)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 12}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 14}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 13}`

- **UIRuntimeOutletConnection** (object 6)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 17}`
    - `UISource` (type 10): `{'$ref': 12}`
    - `UIDestination` (type 10): `{'$ref': 13}`

- **UIColor** (object 7)
  - class: `UIColor`
  - raw values:
    - `UIColorComponentCount` (type 0): `4`
    - `UIRed` (type 6): `1.0`
    - `UIGreen` (type 6): `1.0`
    - `UIBlue` (type 6): `1.0`
    - `UIAlpha` (type 6): `1.0`
    - `NSRGB` (type 8): `{'$data_hex': '3120312031', '$text': '1 1 1'}`
    - `NSColorSpace` (type 0): `2`

- **NSArray** (object 8)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 12}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 14}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 13}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 5}`

- **NSString** (object 9)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '626c61636b436f6c6f72', '$text': 'blackColor'}`

- **NSMutableArray** (object 10)
  - class: `NSMutableArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 18}`

- **UIFont** (object 11)
  - class: `UIFont`
  - raw values:
    - `UIFontName` (type 10): `{'$ref': 20}`
    - `UIFontPointSize` (type 7): `14.0`
    - `UIFontTraits` (type 0): `0`
    - `UISystemFont` (type 5): `False`
    - `NSName` (type 10): `{'$ref': 20}`
    - `NSSize` (type 7): `14.0`

- **UIProxyObject** (object 14)
  - class: `UIProxyObject`
  - raw values:
    - `UIProxiedObjectIdentifier` (type 10): `{'$ref': 2}`

- **UIColor** (object 15)
  - class: `UIColor`
  - raw values:
    - `UISystemColorName` (type 10): `{'$ref': 9}`
    - `UIColorComponentCount` (type 0): `2`
    - `UIWhite` (type 6): `0.0`
    - `UIAlpha` (type 6): `1.0`
    - `NSWhite` (type 8): `{'$data_hex': '30', '$text': '0'}`
    - `NSColorSpace` (type 0): `4`

- **NSString** (object 16)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '494246696c65734f776e6572', '$text': 'IBFilesOwner'}`

- **NSString** (object 17)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '76696577', '$text': 'view'}`

- **UIRuntimeOutletConnection** (object 19)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 22}`
    - `UISource` (type 10): `{'$ref': 12}`
    - `UIDestination` (type 10): `{'$ref': 5}`

- **NSString** (object 20)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '48656c766574696361', '$text': 'Helvetica'}`

- **NSArray** (object 21)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 19}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 6}`

- **NSString** (object 22)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '656469746f72', '$text': 'editor'}`

