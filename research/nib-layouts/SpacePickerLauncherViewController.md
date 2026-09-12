# SpacePickerLauncherViewController

Recovered layout for `SpacePickerLauncherViewController.nib`. Every interpreted value appears beside the
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

- **UIView** (object 29)
  - class: `UIView`
  - frame: (0, 0, 320, 416)
  - raw UIBounds: (0, 0, 320, 416)
  - raw UICenter: (160, 208)
  - autoresizing mask: 18
  - background color: rgba(0.92, 0.92, 0.92, 1)
  - hidden: not encoded
  - opaque: false
  - tag: not encoded
  - raw values:
    - `UIBounds` (type 8): `{'$data_hex': '0600000000000000000000a0430000d043', '$floats': [0.0, 0.0, 320.0, 416.0]}`
    - `UICenter` (type 8): `{'$data_hex': '060000204300005043', '$floats': [160.0, 208.0]}`
    - `UISubviews` (type 10): `{'$ref': 34}`
    - `UIBackgroundColor` (type 10): `{'$ref': 23}`
    - `UIOpaque` (type 5): `False`
    - `UIAutoresizeSubviews` (type 5): `False`
    - `UIAutoresizingMask` (type 0): `18`
  - **UIView** (object 52)
    - class: `UIView`
    - frame: (20, 20, 280, 40)
    - raw UIBounds: (0, 0, 280, 40)
    - raw UICenter: (160, 40)
    - autoresizing mask: 34
    - background color: rgba(0.847059, 0.847059, 0.847059, 1)
    - hidden: not encoded
    - opaque: false
    - tag: not encoded
    - raw values:
      - `UIBounds` (type 8): `{'$data_hex': '06000000000000000000008c4300002042', '$floats': [0.0, 0.0, 280.0, 40.0]}`
      - `UICenter` (type 8): `{'$data_hex': '060000204300002042', '$floats': [160.0, 40.0]}`
      - `UISubviews` (type 10): `{'$ref': 24}`
      - `UIBackgroundColor` (type 10): `{'$ref': 26}`
      - `UIOpaque` (type 5): `False`
      - `UIAutoresizeSubviews` (type 5): `False`
      - `UIAutoresizingMask` (type 0): `34`
    - **UILabel** (object 5)
      - class: `UILabel`
      - frame: (20, 10, 240, 19)
      - raw UIBounds: (0, 0, 240, 19)
      - raw UICenter: (140, 19.5)
      - autoresizing mask: 18
      - background color: rgba(0.847059, 0.847059, 0.847059, 1)
      - font: Helvetica 15pt
      - hidden: not encoded
      - opaque: not encoded
      - tag: not encoded
      - raw values:
        - `UIBounds` (type 8): `{'$data_hex': '0600000000000000000000704300009841', '$floats': [0.0, 0.0, 240.0, 19.0]}`
        - `UICenter` (type 8): `{'$data_hex': '0600000c4300009c41', '$floats': [140.0, 19.5]}`
        - `UIBackgroundColor` (type 10): `{'$ref': 26}`
        - `UIUserInteractionDisabled` (type 5): `False`
        - `UIAutoresizeSubviews` (type 5): `False`
        - `UIAutoresizingMask` (type 0): `18`
        - `UIContentMode` (type 0): `7`
        - `UIClipsToBounds` (type 5): `False`
        - `UIText` (type 10): `{'$ref': 42}`
        - `UIFont` (type 10): `{'$ref': 58}`
        - `UITextColor` (type 10): `{'$ref': 12}`
        - `UIShadowOffset` (type 8): `{'$data_hex': '0600000000000080bf', '$floats': [0.0, -1.0]}`
        - `UINumberOfLines` (type 0): `0`
        - `UITextAlignment` (type 0): `1`
        - `UIPreferredMaxLayoutWidth` (type 6): `240.0`
  - **UILabel** (object 54)
    - class: `UILabel`
    - frame: (20, 68, 280, 20)
    - raw UIBounds: (0, 0, 280, 20)
    - raw UICenter: (160, 78)
    - autoresizing mask: 34
    - background color: not encoded
    - font: Helvetica-Bold 15pt
    - hidden: not encoded
    - opaque: not encoded
    - tag: not encoded
    - raw values:
      - `UIBounds` (type 8): `{'$data_hex': '06000000000000000000008c430000a041', '$floats': [0.0, 0.0, 280.0, 20.0]}`
      - `UICenter` (type 8): `{'$data_hex': '060000204300009c42', '$floats': [160.0, 78.0]}`
      - `UIUserInteractionDisabled` (type 5): `False`
      - `UIAutoresizeSubviews` (type 5): `False`
      - `UIAutoresizingMask` (type 0): `34`
      - `UIContentMode` (type 0): `7`
      - `UIClipsToBounds` (type 5): `False`
      - `UIText` (type 10): `{'$ref': 53}`
      - `UIFont` (type 10): `{'$ref': 27}`
      - `UITextColor` (type 10): `{'$ref': 60}`
      - `UIShadowColor` (type 10): `{'$ref': 30}`
      - `UIShadowOffset` (type 8): `{'$data_hex': '06000000000000803f', '$floats': [0.0, 1.0]}`
      - `UIAdjustsFontSizeToFit` (type 5): `False`
      - `UIMinimumFontSize` (type 6): `10.0`
      - `UIMinimumScaleFactor` (type 6): `0.6666666865348816`
  - **UIButton** (object 21)
    - class: `UIButton`
    - frame: (20, 96, 280, 44)
    - raw UIBounds: (0, 0, 280, 44)
    - raw UICenter: (160, 118)
    - autoresizing mask: 34
    - background color: rgba(0.666667, 0.666667, 0.666667, 1)
    - font: Helvetica-Bold 18pt
    - hidden: not encoded
    - opaque: not encoded
    - tag: not encoded
    - target/action: `buttonAction:` from object 21 (UIButton) to object 33 (UIProxyObject), event mask 64
    - raw values:
      - `UIBounds` (type 8): `{'$data_hex': '06000000000000000000008c4300003042', '$floats': [0.0, 0.0, 280.0, 44.0]}`
      - `UICenter` (type 8): `{'$data_hex': '06000020430000ec42', '$floats': [160.0, 118.0]}`
      - `UIBackgroundColor` (type 10): `{'$ref': 59}`
      - `UIAutoresizeSubviews` (type 5): `False`
      - `UIAutoresizingMask` (type 0): `34`
      - `UIContentHorizontalAlignment` (type 0): `1`
      - `UIButtonStatefulContent` (type 10): `{'$ref': 63}`
      - `UIAdjustsImageWhenHighlighted` (type 5): `False`
      - `UIAdjustsImageWhenDisabled` (type 5): `False`
      - `UIFont` (type 10): `{'$ref': 3}`
      - `UITitleEdgeInsets` (type 8): `{'$data_hex': '0600000000000020410000000000000000', '$floats': [0.0, 10.0, 0.0, 0.0]}`
  - **UIView** (object 19)
    - class: `UIView`
    - frame: (20, 164, 280, 65)
    - raw UIBounds: (0, 0, 280, 65)
    - raw UICenter: (160, 196.5)
    - autoresizing mask: 34
    - background color: rgba(0.847059, 0.847059, 0.847059, 1)
    - hidden: not encoded
    - opaque: false
    - tag: not encoded
    - raw values:
      - `UIBounds` (type 8): `{'$data_hex': '06000000000000000000008c4300008242', '$floats': [0.0, 0.0, 280.0, 65.0]}`
      - `UICenter` (type 8): `{'$data_hex': '060000204300804443', '$floats': [160.0, 196.5]}`
      - `UISubviews` (type 10): `{'$ref': 47}`
      - `UIBackgroundColor` (type 10): `{'$ref': 26}`
      - `UIOpaque` (type 5): `False`
      - `UIAutoresizeSubviews` (type 5): `False`
      - `UIAutoresizingMask` (type 0): `34`
    - **UILabel** (object 61)
      - class: `UILabel`
      - frame: (20, 10, 240, 21)
      - raw UIBounds: (0, 0, 240, 21)
      - raw UICenter: (140, 20.5)
      - autoresizing mask: 34
      - background color: not encoded
      - font: Helvetica-Bold 15pt
      - hidden: not encoded
      - opaque: not encoded
      - tag: not encoded
      - raw values:
        - `UIBounds` (type 8): `{'$data_hex': '060000000000000000000070430000a841', '$floats': [0.0, 0.0, 240.0, 21.0]}`
        - `UICenter` (type 8): `{'$data_hex': '0600000c430000a441', '$floats': [140.0, 20.5]}`
        - `UIUserInteractionDisabled` (type 5): `False`
        - `UIAutoresizeSubviews` (type 5): `False`
        - `UIAutoresizingMask` (type 0): `34`
        - `UIContentMode` (type 0): `7`
        - `UIClipsToBounds` (type 5): `False`
        - `UIText` (type 10): `{'$ref': 39}`
        - `UIFont` (type 10): `{'$ref': 27}`
        - `UITextColor` (type 10): `{'$ref': 12}`
        - `UIShadowOffset` (type 8): `{'$data_hex': '0600000000000080bf', '$floats': [0.0, -1.0]}`
        - `UIAdjustsFontSizeToFit` (type 5): `False`
        - `UIMinimumFontSize` (type 6): `10.0`
        - `UITextAlignment` (type 0): `1`
        - `UIMinimumScaleFactor` (type 6): `0.6666666865348816`
    - **UILabel** (object 20)
      - class: `UILabel`
      - frame: (20, 32, 240, 21)
      - raw UIBounds: (0, 0, 240, 21)
      - raw UICenter: (140, 42.5)
      - autoresizing mask: 18
      - background color: not encoded
      - font: Helvetica 15pt
      - hidden: not encoded
      - opaque: not encoded
      - tag: not encoded
      - raw values:
        - `UIBounds` (type 8): `{'$data_hex': '060000000000000000000070430000a841', '$floats': [0.0, 0.0, 240.0, 21.0]}`
        - `UICenter` (type 8): `{'$data_hex': '0600000c4300002a42', '$floats': [140.0, 42.5]}`
        - `UIUserInteractionDisabled` (type 5): `False`
        - `UIAutoresizeSubviews` (type 5): `False`
        - `UIAutoresizingMask` (type 0): `18`
        - `UIContentMode` (type 0): `7`
        - `UIClipsToBounds` (type 5): `False`
        - `UIText` (type 10): `{'$ref': 22}`
        - `UIFont` (type 10): `{'$ref': 58}`
        - `UITextColor` (type 10): `{'$ref': 12}`
        - `UIShadowOffset` (type 8): `{'$data_hex': '0600000000000080bf', '$floats': [0.0, -1.0]}`
        - `UINumberOfLines` (type 0): `0`
        - `UITextAlignment` (type 0): `1`
        - `UIPreferredMaxLayoutWidth` (type 6): `240.0`

- **UIProxyObject** (object 33)
  - class: `UIProxyObject`
  - outlet: `bottomBlurbHeader` to object 61 (UILabel)
  - outlet: `topContainer` to object 52 (UIView)
  - outlet: `topBlurb` to object 5 (UILabel)
  - outlet: `bottomBlurb` to object 20 (UILabel)
  - outlet: `buttonHeader` to object 54 (UILabel)
  - outlet: `view` to object 29 (UIView)
  - outlet: `button` to object 21 (UIButton)
  - outlet: `bottomContainer` to object 19 (UIView)
  - target/action: `buttonAction:` from object 21 (UIButton) to object 33 (UIProxyObject), event mask 64
  - raw values:
    - `UIProxiedObjectIdentifier` (type 10): `{'$ref': 31}`

## Supporting objects

These objects carry no geometry, contain no view, and hold no
connection. They remain here because a reader auditing an
interpretation follows a reference into them.

- **NSObject** (object 0)
  - class: `NSObject`
  - raw values:
    - `UINibTopLevelObjectsKey` (type 10): `{'$ref': 51}`
    - `UINibObjectsKey` (type 10): `{'$ref': 25}`
    - `UINibConnectionsKey` (type 10): `{'$ref': 1}`
    - `UINibVisibleWindowsKey` (type 10): `{'$ref': 50}`
    - `UINibAccessibilityConfigurationsKey` (type 10): `{'$ref': 50}`
    - `UINibKeyValuePairsKey` (type 10): `{'$ref': 50}`

- **NSArray** (object 1)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 2}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 32}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 4}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 62}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 49}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 38}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 28}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 16}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 43}`

- **UIRuntimeEventConnection** (object 2)
  - class: `UIRuntimeEventConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 36}`
    - `UISource` (type 10): `{'$ref': 21}`
    - `UIDestination` (type 10): `{'$ref': 33}`
    - `UIEventMask` (type 0): `64`

- **UIFont** (object 3)
  - class: `UIFont`
  - raw values:
    - `UIFontName` (type 10): `{'$ref': 44}`
    - `UIFontPointSize` (type 7): `18.0`
    - `UIFontTraits` (type 0): `2`
    - `UISystemFont` (type 5): `False`
    - `NSName` (type 10): `{'$ref': 44}`
    - `NSSize` (type 7): `18.0`

- **UIRuntimeOutletConnection** (object 4)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 8}`
    - `UISource` (type 10): `{'$ref': 33}`
    - `UIDestination` (type 10): `{'$ref': 61}`

- **NSString** (object 6)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '746f70426c757262', '$text': 'topBlurb'}`

- **NSString** (object 7)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '76696577', '$text': 'view'}`

- **NSString** (object 8)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '626f74746f6d426c757262486561646572', '$text': 'bottomBlurbHeader'}`

- **NSNumber** (object 9)
  - class: `NSNumber`
  - raw values:
    - `NS.intval` (type 0): `1`

- **NSString** (object 10)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '627574746f6e', '$text': 'button'}`

- **NSString** (object 11)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '66616b655f7461626c657669657763656c6c2e706e67', '$text': 'fake_tableviewcell.png'}`

- **UIColor** (object 12)
  - class: `UIColor`
  - raw values:
    - `UIColorComponentCount` (type 0): `4`
    - `UIRed` (type 6): `0.46666666865348816`
    - `UIGreen` (type 6): `0.46666666865348816`
    - `UIBlue` (type 6): `0.46666666865348816`
    - `UIAlpha` (type 6): `1.0`
    - `NSRGB` (type 8): `{'$data_hex': '302e34363720302e34363720302e343637', '$text': '0.467 0.467 0.467'}`
    - `NSColorSpace` (type 0): `2`

- **UIProxyObject** (object 13)
  - class: `UIProxyObject`
  - raw values:
    - `UIProxiedObjectIdentifier` (type 10): `{'$ref': 18}`

- **UIButtonContent** (object 14)
  - class: `UIButtonContent`
  - raw values:
    - `UIBackgroundImage` (type 10): `{'$ref': 17}`
    - `UITitleColor` (type 10): `{'$ref': 30}`

- **UIButtonContent** (object 15)
  - class: `UIButtonContent`
  - raw values:
    - `UITitle` (type 10): `{'$ref': 48}`
    - `UIBackgroundImage` (type 10): `{'$ref': 35}`
    - `UITitleColor` (type 10): `{'$ref': 59}`
    - `UIShadowColor` (type 10): `{'$ref': 37}`

- **UIRuntimeOutletConnection** (object 16)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 41}`
    - `UISource` (type 10): `{'$ref': 33}`
    - `UIDestination` (type 10): `{'$ref': 52}`

- **UIImageNibPlaceholder** (object 17)
  - class: `UIImageNibPlaceholder`
  - raw values:
    - `UIImageWidth` (type 6): `1.0`
    - `UIImageHeight` (type 6): `1.0`
    - `UIResourceName` (type 10): `{'$ref': 46}`

- **NSString** (object 18)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '49424669727374526573706f6e646572', '$text': 'IBFirstResponder'}`

- **NSMutableString** (object 22)
  - class: `NSMutableString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '416e796f6e65206d657373616765', '$text': 'Anyone message'}`

- **UIColor** (object 23)
  - class: `UIColor`
  - raw values:
    - `UIColorComponentCount` (type 0): `4`
    - `UIRed` (type 6): `0.9200000166893005`
    - `UIGreen` (type 6): `0.9200000166893005`
    - `UIBlue` (type 6): `0.9200000166893005`
    - `UIAlpha` (type 6): `1.0`
    - `NSRGB` (type 8): `{'$data_hex': '302e393220302e393220302e3932', '$text': '0.92 0.92 0.92'}`
    - `NSColorSpace` (type 0): `2`

- **NSMutableArray** (object 24)
  - class: `NSMutableArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 5}`

- **NSArray** (object 25)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 33}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 13}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 29}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 52}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 54}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 21}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 19}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 5}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 61}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 20}`

- **UIColor** (object 26)
  - class: `UIColor`
  - raw values:
    - `UIColorComponentCount` (type 0): `4`
    - `UIRed` (type 6): `0.8470588326454163`
    - `UIGreen` (type 6): `0.8470588326454163`
    - `UIBlue` (type 6): `0.8470588326454163`
    - `UIAlpha` (type 6): `1.0`
    - `NSRGB` (type 8): `{'$data_hex': '302e38343720302e38343720302e383437', '$text': '0.847 0.847 0.847'}`
    - `NSColorSpace` (type 0): `2`

- **UIFont** (object 27)
  - class: `UIFont`
  - raw values:
    - `UIFontName` (type 10): `{'$ref': 44}`
    - `UIFontPointSize` (type 7): `15.0`
    - `UIFontTraits` (type 0): `2`
    - `UISystemFont` (type 5): `False`
    - `NSName` (type 10): `{'$ref': 44}`
    - `NSSize` (type 7): `15.0`

- **UIRuntimeOutletConnection** (object 28)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 6}`
    - `UISource` (type 10): `{'$ref': 33}`
    - `UIDestination` (type 10): `{'$ref': 5}`

- **UIColor** (object 30)
  - class: `UIColor`
  - raw values:
    - `UIColorComponentCount` (type 0): `4`
    - `UIRed` (type 6): `1.0`
    - `UIGreen` (type 6): `1.0`
    - `UIBlue` (type 6): `1.0`
    - `UIAlpha` (type 6): `1.0`
    - `NSRGB` (type 8): `{'$data_hex': '3120312031', '$text': '1 1 1'}`
    - `NSColorSpace` (type 0): `2`

- **NSString** (object 31)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '494246696c65734f776e6572', '$text': 'IBFilesOwner'}`

- **UIRuntimeOutletConnection** (object 32)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 55}`
    - `UISource` (type 10): `{'$ref': 33}`
    - `UIDestination` (type 10): `{'$ref': 20}`

- **NSMutableArray** (object 34)
  - class: `NSMutableArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 52}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 54}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 21}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 19}`

- **UIImageNibPlaceholder** (object 35)
  - class: `UIImageNibPlaceholder`
  - raw values:
    - `UIImageWidth` (type 6): `1.0`
    - `UIImageHeight` (type 6): `1.0`
    - `UIResourceName` (type 10): `{'$ref': 11}`

- **NSString** (object 36)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '627574746f6e416374696f6e3a', '$text': 'buttonAction:'}`

- **UIColor** (object 37)
  - class: `UIColor`
  - raw values:
    - `UIColorComponentCount` (type 0): `4`
    - `UIRed` (type 6): `0.5`
    - `UIGreen` (type 6): `0.5`
    - `UIBlue` (type 6): `0.5`
    - `UIAlpha` (type 6): `1.0`
    - `NSRGB` (type 8): `{'$data_hex': '302e3520302e3520302e35', '$text': '0.5 0.5 0.5'}`
    - `NSColorSpace` (type 0): `2`

- **UIRuntimeOutletConnection** (object 38)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 40}`
    - `UISource` (type 10): `{'$ref': 33}`
    - `UIDestination` (type 10): `{'$ref': 54}`

- **NSMutableString** (object 39)
  - class: `NSMutableString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '49423a2041626f75742053686172656420436865636b6c697374733a', '$text': 'IB: About Shared Checklists:'}`

- **NSString** (object 40)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '627574746f6e486561646572', '$text': 'buttonHeader'}`

- **NSString** (object 41)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '746f70436f6e7461696e6572', '$text': 'topContainer'}`

- **NSMutableString** (object 42)
  - class: `NSMutableString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '436f6c6c61626f72617465206d657373616765', '$text': 'Collaborate message'}`

- **UIRuntimeOutletConnection** (object 43)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 7}`
    - `UISource` (type 10): `{'$ref': 33}`
    - `UIDestination` (type 10): `{'$ref': 29}`

- **NSString** (object 44)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '48656c7665746963612d426f6c64', '$text': 'Helvetica-Bold'}`

- **NSString** (object 45)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '626f74746f6d436f6e7461696e6572', '$text': 'bottomContainer'}`

- **NSString** (object 46)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '66616b655f7461626c657669657763656c6c5f707265737365642e706e67', '$text': 'fake_tableviewcell_pressed.png'}`

- **NSMutableArray** (object 47)
  - class: `NSMutableArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 61}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 20}`

- **NSString** (object 48)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '7469746c65', '$text': 'title'}`

- **UIRuntimeOutletConnection** (object 49)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 10}`
    - `UISource` (type 10): `{'$ref': 33}`
    - `UIDestination` (type 10): `{'$ref': 21}`

- **NSArray** (object 50)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`

- **NSArray** (object 51)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 33}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 13}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 29}`

- **NSMutableString** (object 53)
  - class: `NSMutableString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '49423a20536861726520436865636b6c69737420496e3a', '$text': 'IB: Share Checklist In:'}`

- **NSString** (object 55)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '626f74746f6d426c757262', '$text': 'bottomBlurb'}`

- **NSNumber** (object 56)
  - class: `NSNumber`
  - raw values:
    - `NS.intval` (type 0): `0`

- **NSString** (object 57)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '48656c766574696361', '$text': 'Helvetica'}`

- **UIFont** (object 58)
  - class: `UIFont`
  - raw values:
    - `UIFontName` (type 10): `{'$ref': 57}`
    - `UIFontPointSize` (type 7): `15.0`
    - `UIFontTraits` (type 0): `0`
    - `UISystemFont` (type 5): `False`
    - `NSName` (type 10): `{'$ref': 57}`
    - `NSSize` (type 7): `15.0`

- **UIColor** (object 59)
  - class: `UIColor`
  - raw values:
    - `UIColorComponentCount` (type 0): `4`
    - `UIRed` (type 6): `0.6666666865348816`
    - `UIGreen` (type 6): `0.6666666865348816`
    - `UIBlue` (type 6): `0.6666666865348816`
    - `UIAlpha` (type 6): `1.0`
    - `NSRGB` (type 8): `{'$data_hex': '302e36363720302e36363720302e363637', '$text': '0.667 0.667 0.667'}`
    - `NSColorSpace` (type 0): `2`

- **UIColor** (object 60)
  - class: `UIColor`
  - raw values:
    - `UIColorComponentCount` (type 0): `4`
    - `UIRed` (type 6): `0.3333333432674408`
    - `UIGreen` (type 6): `0.3333333432674408`
    - `UIBlue` (type 6): `0.3333333432674408`
    - `UIAlpha` (type 6): `1.0`
    - `NSRGB` (type 8): `{'$data_hex': '302e33333320302e33333320302e333333', '$text': '0.333 0.333 0.333'}`
    - `NSColorSpace` (type 0): `2`

- **UIRuntimeOutletConnection** (object 62)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 45}`
    - `UISource` (type 10): `{'$ref': 33}`
    - `UIDestination` (type 10): `{'$ref': 19}`

- **NSMutableDictionary** (object 63)
  - class: `NSMutableDictionary`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 56}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 15}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 9}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 14}`

