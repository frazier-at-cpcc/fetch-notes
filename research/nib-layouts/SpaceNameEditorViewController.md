# SpaceNameEditorViewController

Recovered layout for `SpaceNameEditorViewController.nib`. Every interpreted value appears beside the
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

- **UIView** (object 1)
  - class: `UIView`
  - frame: (0, 0, 320, 416)
  - raw UIBounds: (0, 0, 320, 416)
  - raw UICenter: (160, 208)
  - autoresizing mask: 18
  - background color: rgba(0.917647, 0.917647, 0.917647, 1)
  - hidden: not encoded
  - opaque: false
  - tag: not encoded
  - raw values:
    - `UIBounds` (type 8): `{'$data_hex': '0600000000000000000000a0430000d043', '$floats': [0.0, 0.0, 320.0, 416.0]}`
    - `UICenter` (type 8): `{'$data_hex': '060000204300005043', '$floats': [160.0, 208.0]}`
    - `UISubviews` (type 10): `{'$ref': 11}`
    - `UIBackgroundColor` (type 10): `{'$ref': 6}`
    - `UIOpaque` (type 5): `False`
    - `UIAutoresizeSubviews` (type 5): `False`
    - `UIAutoresizingMask` (type 0): `18`
  - **UITextField** (object 16)
    - class: `UITextField`
    - frame: (20, 20, 280, 31)
    - raw UIBounds: (0, 0, 280, 31)
    - raw UICenter: (160, 35.5)
    - autoresizing mask: 34
    - background color: not encoded
    - font: Helvetica 14pt
    - hidden: not encoded
    - opaque: not encoded
    - tag: not encoded
    - outlet: `delegate` to object 10 (UIProxyObject)
    - raw values:
      - `UIBounds` (type 8): `{'$data_hex': '06000000000000000000008c430000f841', '$floats': [0.0, 0.0, 280.0, 31.0]}`
      - `UICenter` (type 8): `{'$data_hex': '060000204300000e42', '$floats': [160.0, 35.5]}`
      - `UIAutoresizeSubviews` (type 5): `False`
      - `UIAutoresizingMask` (type 0): `34`
      - `UIClipsToBounds` (type 5): `False`
      - `UIContentHorizontalAlignment` (type 0): `1`
      - `UIFont` (type 10): `{'$ref': 17}`
      - `UIText` (type 10): `{'$ref': 27}`
      - `UITextColor` (type 10): `{'$ref': 4}`
      - `UIBorderStyle` (type 0): `3`
      - `UIAdjustsFontSizeToFit` (type 5): `False`
      - `UIMinimumFontSize` (type 6): `17.0`
      - `UIClearButtonOffset` (type 8): `{'$data_hex': '06000040400000803f', '$floats': [3.0, 1.0]}`
  - **UILabel** (object 7)
    - class: `UILabel`
    - frame: (20, 68, 280, 31)
    - raw UIBounds: (0, 0, 280, 31)
    - raw UICenter: (160, 83.5)
    - autoresizing mask: 34
    - background color: rgba(0.666667, 0.666667, 0.666667, 1)
    - font: Helvetica 13pt
    - hidden: false
    - opaque: not encoded
    - tag: not encoded
    - raw values:
      - `UIBounds` (type 8): `{'$data_hex': '06000000000000000000008c430000f841', '$floats': [0.0, 0.0, 280.0, 31.0]}`
      - `UICenter` (type 8): `{'$data_hex': '06000020430000a742', '$floats': [160.0, 83.5]}`
      - `UIBackgroundColor` (type 10): `{'$ref': 25}`
      - `UIHidden` (type 5): `False`
      - `UIUserInteractionDisabled` (type 5): `False`
      - `UIAutoresizeSubviews` (type 5): `False`
      - `UIAutoresizingMask` (type 0): `34`
      - `UIContentMode` (type 0): `7`
      - `UIClipsToBounds` (type 5): `False`
      - `UIText` (type 10): `{'$ref': 5}`
      - `UIFont` (type 10): `{'$ref': 29}`
      - `UITextColor` (type 10): `{'$ref': 26}`
      - `UIShadowOffset` (type 8): `{'$data_hex': '0600000000000080bf', '$floats': [0.0, -1.0]}`
      - `UIAdjustsFontSizeToFit` (type 5): `False`
      - `UIMinimumFontSize` (type 6): `10.0`
      - `UITextAlignment` (type 0): `1`
      - `UIMinimumScaleFactor` (type 6): `0.7692307829856873`

- **UIProxyObject** (object 10)
  - class: `UIProxyObject`
  - outlet: `spaceName` to object 16 (UITextField)
  - outlet: `view` to object 1 (UIView)
  - outlet: `blurb` to object 7 (UILabel)
  - raw values:
    - `UIProxiedObjectIdentifier` (type 10): `{'$ref': 14}`

## Supporting objects

These objects carry no geometry, contain no view, and hold no
connection. They remain here because a reader auditing an
interpretation follows a reference into them.

- **NSObject** (object 0)
  - class: `NSObject`
  - raw values:
    - `UINibTopLevelObjectsKey` (type 10): `{'$ref': 23}`
    - `UINibObjectsKey` (type 10): `{'$ref': 13}`
    - `UINibConnectionsKey` (type 10): `{'$ref': 21}`
    - `UINibVisibleWindowsKey` (type 10): `{'$ref': 19}`
    - `UINibAccessibilityConfigurationsKey` (type 10): `{'$ref': 19}`
    - `UINibKeyValuePairsKey` (type 10): `{'$ref': 19}`

- **UIProxyObject** (object 2)
  - class: `UIProxyObject`
  - raw values:
    - `UIProxiedObjectIdentifier` (type 10): `{'$ref': 3}`

- **NSString** (object 3)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '49424669727374526573706f6e646572', '$text': 'IBFirstResponder'}`

- **UIColor** (object 4)
  - class: `UIColor`
  - raw values:
    - `UIColorComponentCount` (type 0): `4`
    - `UIRed` (type 6): `0.0`
    - `UIGreen` (type 6): `0.0`
    - `UIBlue` (type 6): `0.0`
    - `UIAlpha` (type 6): `1.0`
    - `NSRGB` (type 8): `{'$data_hex': '3020302030', '$text': '0 0 0'}`
    - `NSColorSpace` (type 0): `2`

- **NSMutableString** (object 5)
  - class: `NSMutableString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '4c6162656c', '$text': 'Label'}`

- **UIColor** (object 6)
  - class: `UIColor`
  - raw values:
    - `UIColorComponentCount` (type 0): `4`
    - `UIRed` (type 6): `0.9176470637321472`
    - `UIGreen` (type 6): `0.9176470637321472`
    - `UIBlue` (type 6): `0.9176470637321472`
    - `UIAlpha` (type 6): `1.0`
    - `NSRGB` (type 8): `{'$data_hex': '302e39313820302e39313820302e393138', '$text': '0.918 0.918 0.918'}`
    - `NSColorSpace` (type 0): `2`

- **NSString** (object 8)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '64656c6567617465', '$text': 'delegate'}`

- **NSString** (object 9)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '73706163654e616d65', '$text': 'spaceName'}`

- **NSMutableArray** (object 11)
  - class: `NSMutableArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 16}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 7}`

- **UIRuntimeOutletConnection** (object 12)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 8}`
    - `UISource` (type 10): `{'$ref': 16}`
    - `UIDestination` (type 10): `{'$ref': 10}`

- **NSArray** (object 13)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 10}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 2}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 1}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 16}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 7}`

- **NSString** (object 14)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '494246696c65734f776e6572', '$text': 'IBFilesOwner'}`

- **NSString** (object 15)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '76696577', '$text': 'view'}`

- **UIFont** (object 17)
  - class: `UIFont`
  - raw values:
    - `UIFontName` (type 10): `{'$ref': 18}`
    - `UIFontPointSize` (type 7): `14.0`
    - `UIFontTraits` (type 0): `0`
    - `UISystemFont` (type 5): `False`
    - `NSName` (type 10): `{'$ref': 18}`
    - `NSSize` (type 7): `14.0`

- **NSString** (object 18)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '48656c766574696361', '$text': 'Helvetica'}`

- **NSArray** (object 19)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`

- **NSString** (object 20)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '626c61636b436f6c6f72', '$text': 'blackColor'}`

- **NSArray** (object 21)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 30}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 12}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 24}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 28}`

- **NSString** (object 22)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '626c757262', '$text': 'blurb'}`

- **NSArray** (object 23)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 10}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 2}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 1}`

- **UIRuntimeOutletConnection** (object 24)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 9}`
    - `UISource` (type 10): `{'$ref': 10}`
    - `UIDestination` (type 10): `{'$ref': 16}`

- **UIColor** (object 25)
  - class: `UIColor`
  - raw values:
    - `UIColorComponentCount` (type 0): `4`
    - `UIRed` (type 6): `0.6666666865348816`
    - `UIGreen` (type 6): `0.6666666865348816`
    - `UIBlue` (type 6): `0.6666666865348816`
    - `UIAlpha` (type 6): `1.0`
    - `NSRGB` (type 8): `{'$data_hex': '302e36363720302e36363720302e363637', '$text': '0.667 0.667 0.667'}`
    - `NSColorSpace` (type 0): `2`

- **UIColor** (object 26)
  - class: `UIColor`
  - raw values:
    - `UISystemColorName` (type 10): `{'$ref': 20}`
    - `UIColorComponentCount` (type 0): `2`
    - `UIWhite` (type 6): `0.0`
    - `UIAlpha` (type 6): `1.0`
    - `NSWhite` (type 8): `{'$data_hex': '30', '$text': '0'}`
    - `NSColorSpace` (type 0): `4`

- **NSString** (object 27)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '', '$text': ''}`

- **UIRuntimeOutletConnection** (object 28)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 15}`
    - `UISource` (type 10): `{'$ref': 10}`
    - `UIDestination` (type 10): `{'$ref': 1}`

- **UIFont** (object 29)
  - class: `UIFont`
  - raw values:
    - `UIFontName` (type 10): `{'$ref': 18}`
    - `UIFontPointSize` (type 7): `13.0`
    - `UIFontTraits` (type 0): `0`
    - `UISystemFont` (type 5): `False`
    - `NSName` (type 10): `{'$ref': 18}`
    - `NSSize` (type 7): `13.0`

- **UIRuntimeOutletConnection** (object 30)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 22}`
    - `UISource` (type 10): `{'$ref': 10}`
    - `UIDestination` (type 10): `{'$ref': 7}`

