# ReminderCaptureViewController_iPhone

Recovered layout for `ReminderCaptureViewController_iPhone.nib`. Every interpreted value appears beside the
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

- **UIBarButtonItem** (object 13)
  - class: `UIBarButtonItem`
  - target/action: `cancelAndDismissAction:` from object 13 (UIBarButtonItem) to object 49 (UIProxyObject), event mask not encoded
  - raw values:
    - `UIEnabled` (type 5): `False`
    - `UIIsSystemItem` (type 5): `False`
    - `UISystemItem` (type 0): `1`
    - `UIStyle` (type 0): `1`

- **UIView** (object 21)
  - class: `UIView`
  - frame: (0, 0, 320, 460)
  - raw UIBounds: (0, 0, 320, 460)
  - raw UICenter: (160, 230)
  - autoresizing mask: 18
  - background color: rgba(0.94902, 0.94902, 0.94902, 1)
  - hidden: not encoded
  - opaque: false
  - tag: not encoded
  - raw values:
    - `UIBounds` (type 8): `{'$data_hex': '0600000000000000000000a0430000e643', '$floats': [0.0, 0.0, 320.0, 460.0]}`
    - `UICenter` (type 8): `{'$data_hex': '060000204300006643', '$floats': [160.0, 230.0]}`
    - `UISubviews` (type 10): `{'$ref': 12}`
    - `UIBackgroundColor` (type 10): `{'$ref': 41}`
    - `UIOpaque` (type 5): `False`
    - `UIAutoresizeSubviews` (type 5): `False`
    - `UIAutoresizingMask` (type 0): `18`
  - **UIToolbar** (object 51)
    - class: `UIToolbar`
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
      - `UIClearsContextBeforeDrawing` (type 4): `True`
      - `UIViewContentHuggingPriority` (type 10): `{'$ref': 35}`
      - `UIItems` (type 10): `{'$ref': 77}`
  - **UIView** (object 104)
    - class: `UIView`
    - frame: (0, 44, 320, 306)
    - raw UIBounds: (0, 0, 320, 306)
    - raw UICenter: (160, 197)
    - autoresizing mask: 10
    - background color: rgba(0.94902, 0.94902, 0.94902, 1)
    - hidden: not encoded
    - opaque: false
    - tag: not encoded
    - raw values:
      - `UIBounds` (type 8): `{'$data_hex': '0600000000000000000000a04300009943', '$floats': [0.0, 0.0, 320.0, 306.0]}`
      - `UICenter` (type 8): `{'$data_hex': '060000204300004543', '$floats': [160.0, 197.0]}`
      - `UISubviews` (type 10): `{'$ref': 56}`
      - `UIBackgroundColor` (type 10): `{'$ref': 41}`
      - `UIOpaque` (type 5): `False`
      - `UIAutoresizeSubviews` (type 5): `False`
      - `UIAutoresizingMask` (type 0): `10`
    - **UIScrollView** (object 10)
      - class: `UIScrollView`
      - frame: (0, 0, 320, 306)
      - raw UIBounds: (0, 0, 320, 306)
      - raw UICenter: (160, 153)
      - autoresizing mask: 18
      - background color: rgba(0, 0, 0, 0)
      - hidden: not encoded
      - opaque: not encoded
      - tag: not encoded
      - raw values:
        - `UIBounds` (type 8): `{'$data_hex': '0600000000000000000000a04300009943', '$floats': [0.0, 0.0, 320.0, 306.0]}`
        - `UICenter` (type 8): `{'$data_hex': '060000204300001943', '$floats': [160.0, 153.0]}`
        - `UISubviews` (type 10): `{'$ref': 7}`
        - `UIBackgroundColor` (type 10): `{'$ref': 38}`
        - `UIMultipleTouchEnabled` (type 5): `False`
        - `UIAutoresizeSubviews` (type 5): `False`
        - `UIAutoresizingMask` (type 0): `18`
        - `UIClipsToBounds` (type 5): `False`
        - `UIBouncesZoom` (type 5): `False`
      - **UIButton** (object 50)
        - class: `UIButton`
        - frame: (20, 20, 280, 47)
        - raw UIBounds: (0, 0, 280, 47)
        - raw UICenter: (160, 43.5)
        - autoresizing mask: 34
        - background color: not encoded
        - hidden: not encoded
        - opaque: not encoded
        - tag: not encoded
        - target/action: `setReminderDateAction:` from object 50 (UIButton) to object 49 (UIProxyObject), event mask 64
        - raw values:
          - `UIBounds` (type 8): `{'$data_hex': '06000000000000000000008c4300003c42', '$floats': [0.0, 0.0, 280.0, 47.0]}`
          - `UICenter` (type 8): `{'$data_hex': '060000204300002e42', '$floats': [160.0, 43.5]}`
          - `UIAutoresizeSubviews` (type 5): `False`
          - `UIAutoresizingMask` (type 0): `34`
          - `UIContentHorizontalAlignment` (type 0): `1`
          - `UIButtonStatefulContent` (type 10): `{'$ref': 8}`
          - `UIReversesTitleShadowWhenHighlighted` (type 5): `False`
          - `UIAdjustsImageWhenHighlighted` (type 5): `False`
          - `UIAdjustsImageWhenDisabled` (type 5): `False`
          - `UIContentEdgeInsets` (type 8): `{'$data_hex': '060000a0400000a0400000a0400000a040', '$floats': [5.0, 5.0, 5.0, 5.0]}`
          - `UITitleEdgeInsets` (type 8): `{'$data_hex': '0600000000000080410000000000000000', '$floats': [0.0, 16.0, 0.0, 0.0]}`
          - `UITitleShadowOffset` (type 8): `{'$data_hex': '06000000000000803f', '$floats': [0.0, 1.0]}`
          - `UIImageEdgeInsets` (type 8): `{'$data_hex': '06000000000000a0400000000000000000', '$floats': [0.0, 5.0, 0.0, 0.0]}`
      - **UIButton** (object 28)
        - class: `UIButton`
        - frame: (20, 75, 280, 47)
        - raw UIBounds: (0, 0, 280, 47)
        - raw UICenter: (160, 98.5)
        - autoresizing mask: 34
        - background color: not encoded
        - hidden: not encoded
        - opaque: not encoded
        - tag: not encoded
        - target/action: `deleteAction:` from object 28 (UIButton) to object 49 (UIProxyObject), event mask 64
        - raw values:
          - `UIBounds` (type 8): `{'$data_hex': '06000000000000000000008c4300003c42', '$floats': [0.0, 0.0, 280.0, 47.0]}`
          - `UICenter` (type 8): `{'$data_hex': '06000020430000c542', '$floats': [160.0, 98.5]}`
          - `UIAutoresizeSubviews` (type 5): `False`
          - `UIAutoresizingMask` (type 0): `34`
          - `UIButtonStatefulContent` (type 10): `{'$ref': 18}`
          - `UIReversesTitleShadowWhenHighlighted` (type 5): `False`
          - `UIAdjustsImageWhenHighlighted` (type 5): `False`
          - `UIAdjustsImageWhenDisabled` (type 5): `False`
          - `UITitleShadowOffset` (type 8): `{'$data_hex': '06000000000000803f', '$floats': [0.0, 1.0]}`
      - **UIPlaceHolderTextView** (object 91)
        - class: `UIPlaceHolderTextView`
        - encoded as: `UIClassSwapper` swapping `UITextView`
        - frame: (11, 75, 298, 211)
        - raw UIBounds: (0, 0, 298, 211)
        - raw UICenter: (160, 180.5)
        - autoresizing mask: 34
        - background color: rgba(0.94902, 0.94902, 0.94902, 1)
        - font: Helvetica 16pt
        - hidden: not encoded
        - opaque: false
        - tag: not encoded
        - outlet: `delegate` to object 49 (UIProxyObject)
        - raw values:
          - `UIBounds` (type 8): `{'$data_hex': '0600000000000000000000954300005343', '$floats': [0.0, 0.0, 298.0, 211.0]}`
          - `UICenter` (type 8): `{'$data_hex': '060000204300803443', '$floats': [160.0, 180.5]}`
          - `UISubviews` (type 10): `{'$ref': 88}`
          - `UIBackgroundColor` (type 10): `{'$ref': 41}`
          - `UIOpaque` (type 5): `False`
          - `UIMultipleTouchEnabled` (type 5): `False`
          - `UIAutoresizeSubviews` (type 5): `False`
          - `UIAutoresizingMask` (type 0): `34`
          - `UIClipsToBounds` (type 5): `False`
          - `UIShowsHorizontalScrollIndicator` (type 4): `True`
          - `UIShowsVerticalScrollIndicator` (type 4): `True`
          - `UIScrollDisabled` (type 5): `False`
          - `UIBouncesZoom` (type 5): `False`
          - `UIContentSize` (type 8): `{'$data_hex': '060000954300001042', '$floats': [298.0, 36.0]}`
          - `UIFont` (type 10): `{'$ref': 62}`
          - `UITextColor` (type 10): `{'$ref': 111}`
          - `UITextAlignment` (type 0): `0`
          - `UIClassName` (type 10): `{'$ref': 9}`
          - `UIOriginalClassName` (type 10): `{'$ref': 27}`
        - **UITextSelectionView** (object 71)
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
  - **UIRoundedRectButton** (object 121)
    - class: `UIRoundedRectButton`
    - frame: (20, 358, 280, 37)
    - raw UIBounds: (0, 0, 280, 37)
    - raw UICenter: (160, 376.5)
    - autoresizing mask: 36
    - background color: not encoded
    - font: Helvetica-Bold 15pt
    - hidden: not encoded
    - opaque: not encoded
    - tag: not encoded
    - target/action: `setLocationAction:` from object 121 (UIRoundedRectButton) to object 49 (UIProxyObject), event mask 64
    - raw values:
      - `UIBounds` (type 8): `{'$data_hex': '06000000000000000000008c4300001442', '$floats': [0.0, 0.0, 280.0, 37.0]}`
      - `UICenter` (type 8): `{'$data_hex': '06000020430040bc43', '$floats': [160.0, 376.5]}`
      - `UIAutoresizeSubviews` (type 5): `False`
      - `UIAutoresizingMask` (type 0): `36`
      - `UIButtonStatefulContent` (type 10): `{'$ref': 98}`
      - `UIAdjustsImageWhenHighlighted` (type 5): `False`
      - `UIAdjustsImageWhenDisabled` (type 5): `False`
      - `UIButtonType` (type 0): `1`
      - `UIFont` (type 10): `{'$ref': 93}`
  - **UIRoundedRectButton** (object 75)
    - class: `UIRoundedRectButton`
    - frame: (20, 403, 280, 37)
    - raw UIBounds: (0, 0, 280, 37)
    - raw UICenter: (160, 421.5)
    - autoresizing mask: 36
    - background color: not encoded
    - font: Helvetica-Bold 15pt
    - hidden: not encoded
    - opaque: not encoded
    - tag: not encoded
    - target/action: `setSpaceAction:` from object 75 (UIRoundedRectButton) to object 49 (UIProxyObject), event mask 64
    - raw values:
      - `UIBounds` (type 8): `{'$data_hex': '06000000000000000000008c4300001442', '$floats': [0.0, 0.0, 280.0, 37.0]}`
      - `UICenter` (type 8): `{'$data_hex': '060000204300c0d243', '$floats': [160.0, 421.5]}`
      - `UIAutoresizeSubviews` (type 5): `False`
      - `UIAutoresizingMask` (type 0): `36`
      - `UIButtonStatefulContent` (type 10): `{'$ref': 55}`
      - `UIAdjustsImageWhenHighlighted` (type 5): `False`
      - `UIAdjustsImageWhenDisabled` (type 5): `False`
      - `UIButtonType` (type 0): `1`
      - `UIFont` (type 10): `{'$ref': 93}`
  - **UIToolbar** (object 24)
    - class: `UIToolbar`
    - frame: (0, 200, 320, 44)
    - raw UIBounds: (0, 0, 320, 44)
    - raw UICenter: (160, 222)
    - autoresizing mask: 10
    - background color: not encoded
    - hidden: not encoded
    - opaque: false
    - tag: not encoded
    - raw values:
      - `UIBounds` (type 8): `{'$data_hex': '0600000000000000000000a04300003042', '$floats': [0.0, 0.0, 320.0, 44.0]}`
      - `UICenter` (type 8): `{'$data_hex': '060000204300005e43', '$floats': [160.0, 222.0]}`
      - `UIOpaque` (type 5): `False`
      - `UIAutoresizeSubviews` (type 5): `False`
      - `UIAutoresizingMask` (type 0): `10`
      - `UIClearsContextBeforeDrawing` (type 4): `True`
      - `UIViewContentHuggingPriority` (type 10): `{'$ref': 35}`
      - `UIItems` (type 10): `{'$ref': 30}`
  - **UIDatePicker** (object 3)
    - class: `UIDatePicker`
    - frame: (0, 244, 320, 216)
    - raw UIBounds: (0, 0, 320, 216)
    - raw UICenter: (160, 352)
    - autoresizing mask: 10
    - background color: not encoded
    - hidden: not encoded
    - opaque: false
    - tag: not encoded
    - target/action: `datePickerChanged:` from object 3 (UIDatePicker) to object 49 (UIProxyObject), event mask 4096
    - raw values:
      - `UIBounds` (type 8): `{'$data_hex': '0600000000000000000000a04300005843', '$floats': [0.0, 0.0, 320.0, 216.0]}`
      - `UICenter` (type 8): `{'$data_hex': '06000020430000b043', '$floats': [160.0, 352.0]}`
      - `UIOpaque` (type 5): `False`
      - `UIAutoresizeSubviews` (type 5): `False`
      - `UIAutoresizingMask` (type 0): `10`
      - `UIViewContentHuggingPriority` (type 10): `{'$ref': 35}`
      - `UILocale` (type 10): `{'$ref': 63}`
      - `UIDate` (type 10): `{'$ref': 57}`
      - `UIMinuteInterval` (type 0): `5`

- **UIBarButtonItem** (object 42)
  - class: `UIBarButtonItem`
  - target/action: `saveAndDismissAction:` from object 42 (UIBarButtonItem) to object 49 (UIProxyObject), event mask not encoded
  - raw values:
    - `UIEnabled` (type 5): `False`
    - `UIIsSystemItem` (type 5): `False`
    - `UISystemItem` (type 0): `3`
    - `UIStyle` (type 0): `1`

- **UIBarButtonItem** (object 46)
  - class: `UIBarButtonItem`
  - target/action: `closeDatePickerAction:` from object 46 (UIBarButtonItem) to object 49 (UIProxyObject), event mask not encoded
  - raw values:
    - `UIEnabled` (type 5): `False`
    - `UIIsSystemItem` (type 5): `False`
    - `UISystemItem` (type 0): `0`
    - `UIStyle` (type 0): `1`

- **UIProxyObject** (object 49)
  - class: `UIProxyObject`
  - outlet: `setLocationButton` to object 121 (UIRoundedRectButton)
  - outlet: `textAccessoryView` to object 70 (PhoneNoteViewInputAccessory)
  - outlet: `datePicker` to object 3 (UIDatePicker)
  - outlet: `toolbar` to object 51 (UIToolbar)
  - outlet: `deleteButton` to object 28 (UIButton)
  - outlet: `pickerToolbar` to object 24 (UIToolbar)
  - outlet: `scrollView` to object 10 (UIScrollView)
  - outlet: `setSpaceButton` to object 75 (UIRoundedRectButton)
  - outlet: `textContainerView` to object 104 (UIView)
  - outlet: `view` to object 21 (UIView)
  - outlet: `noteTextView` to object 91 (UIPlaceHolderTextView)
  - outlet: `reminderButton` to object 50 (UIButton)
  - target/action: `cancelAndDismissAction:` from object 59 (UIBarButtonItem) to object 49 (UIProxyObject), event mask not encoded
  - target/action: `setReminderDateAction:` from object 50 (UIButton) to object 49 (UIProxyObject), event mask 64
  - target/action: `datePickerChanged:` from object 3 (UIDatePicker) to object 49 (UIProxyObject), event mask 4096
  - target/action: `saveAndDismissAction:` from object 42 (UIBarButtonItem) to object 49 (UIProxyObject), event mask not encoded
  - target/action: `cancelAndDismissAction:` from object 13 (UIBarButtonItem) to object 49 (UIProxyObject), event mask not encoded
  - target/action: `doneEditingAction:` from object 86 (UIBarButtonItem) to object 49 (UIProxyObject), event mask not encoded
  - target/action: `setSpaceAction:` from object 75 (UIRoundedRectButton) to object 49 (UIProxyObject), event mask 64
  - target/action: `closeDatePickerAction:` from object 46 (UIBarButtonItem) to object 49 (UIProxyObject), event mask not encoded
  - target/action: `setLocationAction:` from object 121 (UIRoundedRectButton) to object 49 (UIProxyObject), event mask 64
  - target/action: `deleteAction:` from object 28 (UIButton) to object 49 (UIProxyObject), event mask 64
  - raw values:
    - `UIProxiedObjectIdentifier` (type 10): `{'$ref': 81}`

- **UIBarButtonItem** (object 59)
  - class: `UIBarButtonItem`
  - target/action: `cancelAndDismissAction:` from object 59 (UIBarButtonItem) to object 49 (UIProxyObject), event mask not encoded
  - raw values:
    - `UIEnabled` (type 5): `False`
    - `UIIsSystemItem` (type 5): `False`
    - `UISystemItem` (type 0): `1`
    - `UIStyle` (type 0): `1`

- **PhoneNoteViewInputAccessory** (object 70)
  - class: `PhoneNoteViewInputAccessory`
  - encoded as: `UIClassSwapper` swapping `UIToolbar`
  - frame: (0, 0, 320, 44)
  - raw UIBounds: (0, 0, 320, 44)
  - raw UICenter: (160, 22)
  - autoresizing mask: 10
  - background color: not encoded
  - hidden: not encoded
  - opaque: false
  - tag: not encoded
  - outlet: `delegate` to object 49 (UIProxyObject)
  - raw values:
    - `UIBounds` (type 8): `{'$data_hex': '0600000000000000000000a04300003042', '$floats': [0.0, 0.0, 320.0, 44.0]}`
    - `UICenter` (type 8): `{'$data_hex': '06000020430000b041', '$floats': [160.0, 22.0]}`
    - `UIOpaque` (type 5): `False`
    - `UIAutoresizeSubviews` (type 5): `False`
    - `UIAutoresizingMask` (type 0): `10`
    - `UIClearsContextBeforeDrawing` (type 4): `True`
    - `UIViewContentHuggingPriority` (type 10): `{'$ref': 35}`
    - `UIItems` (type 10): `{'$ref': 64}`
    - `UIClassName` (type 10): `{'$ref': 80}`
    - `UIOriginalClassName` (type 10): `{'$ref': 31}`

- **UIBarButtonItem** (object 86)
  - class: `UIBarButtonItem`
  - target/action: `doneEditingAction:` from object 86 (UIBarButtonItem) to object 49 (UIProxyObject), event mask not encoded
  - raw values:
    - `UIEnabled` (type 5): `False`
    - `UIIsSystemItem` (type 5): `False`
    - `UISystemItem` (type 0): `0`
    - `UIStyle` (type 0): `2`

## Supporting objects

These objects carry no geometry, contain no view, and hold no
connection. They remain here because a reader auditing an
interpretation follows a reference into them.

- **NSObject** (object 0)
  - class: `NSObject`
  - raw values:
    - `UINibTopLevelObjectsKey` (type 10): `{'$ref': 90}`
    - `UINibObjectsKey` (type 10): `{'$ref': 15}`
    - `UINibConnectionsKey` (type 10): `{'$ref': 76}`
    - `UINibVisibleWindowsKey` (type 10): `{'$ref': 109}`
    - `UINibAccessibilityConfigurationsKey` (type 10): `{'$ref': 109}`
    - `UINibKeyValuePairsKey` (type 10): `{'$ref': 109}`

- **NSString** (object 1)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '64656c657465427574746f6e', '$text': 'deleteButton'}`

- **NSString** (object 2)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '73617665416e644469736d697373416374696f6e3a', '$text': 'saveAndDismissAction:'}`

- **UIRuntimeOutletConnection** (object 4)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 54}`
    - `UISource` (type 10): `{'$ref': 49}`
    - `UIDestination` (type 10): `{'$ref': 121}`

- **UIButtonContent** (object 5)
  - class: `UIButtonContent`
  - raw values:
    - `UITitleColor` (type 10): `{'$ref': 117}`
    - `UIShadowColor` (type 10): `{'$ref': 111}`

- **UIButtonContent** (object 6)
  - class: `UIButtonContent`
  - raw values:
    - `UITitle` (type 10): `{'$ref': 94}`
    - `UIImage` (type 10): `{'$ref': 115}`
    - `UITitleColor` (type 10): `{'$ref': 111}`
    - `UIShadowColor` (type 10): `{'$ref': 26}`

- **NSMutableArray** (object 7)
  - class: `NSMutableArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 50}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 28}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 91}`

- **NSMutableDictionary** (object 8)
  - class: `NSMutableDictionary`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 74}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 6}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 36}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 5}`

- **NSString** (object 9)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '5549506c616365486f6c6465725465787456696577', '$text': 'UIPlaceHolderTextView'}`

- **NSString** (object 11)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '7363726f6c6c56696577', '$text': 'scrollView'}`

- **NSMutableArray** (object 12)
  - class: `NSMutableArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 51}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 104}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 121}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 75}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 24}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 3}`

- **NSString** (object 14)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '646174655069636b6572', '$text': 'datePicker'}`

- **NSArray** (object 15)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 49}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 48}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 21}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 70}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 51}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 104}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 121}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 75}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 24}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 3}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 122}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 96}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 86}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 13}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 34}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 42}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 10}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 59}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 29}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 46}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 50}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 28}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 91}`

- **UIRuntimeEventConnection** (object 16)
  - class: `UIRuntimeEventConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 119}`
    - `UISource` (type 10): `{'$ref': 59}`
    - `UIDestination` (type 10): `{'$ref': 49}`

- **NSString** (object 17)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '646174655069636b65724368616e6765643a', '$text': 'datePickerChanged:'}`

- **NSMutableDictionary** (object 18)
  - class: `NSMutableDictionary`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 74}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 52}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 36}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 22}`

- **UIRuntimeOutletConnection** (object 19)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 120}`
    - `UISource` (type 10): `{'$ref': 49}`
    - `UIDestination` (type 10): `{'$ref': 70}`

- **UIRuntimeEventConnection** (object 20)
  - class: `UIRuntimeEventConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 84}`
    - `UISource` (type 10): `{'$ref': 50}`
    - `UIDestination` (type 10): `{'$ref': 49}`
    - `UIEventMask` (type 0): `64`

- **UIButtonContent** (object 22)
  - class: `UIButtonContent`
  - raw values:
    - `UITitleColor` (type 10): `{'$ref': 117}`
    - `UIShadowColor` (type 10): `{'$ref': 111}`

- **UIRuntimeOutletConnection** (object 23)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 79}`
    - `UISource` (type 10): `{'$ref': 91}`
    - `UIDestination` (type 10): `{'$ref': 49}`

- **UIRuntimeOutletConnection** (object 25)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 14}`
    - `UISource` (type 10): `{'$ref': 49}`
    - `UIDestination` (type 10): `{'$ref': 3}`

- **UIColor** (object 26)
  - class: `UIColor`
  - raw values:
    - `UIColorComponentCount` (type 0): `4`
    - `UIRed` (type 6): `1.0`
    - `UIGreen` (type 6): `1.0`
    - `UIBlue` (type 6): `1.0`
    - `UIAlpha` (type 6): `1.0`
    - `NSRGB` (type 8): `{'$data_hex': '3120312031', '$text': '1 1 1'}`
    - `NSColorSpace` (type 0): `2`

- **NSString** (object 27)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '55495465787456696577', '$text': 'UITextView'}`

- **UIBarButtonItem** (object 29)
  - class: `UIBarButtonItem`
  - raw values:
    - `UIEnabled` (type 5): `False`
    - `UIIsSystemItem` (type 5): `False`
    - `UISystemItem` (type 0): `5`

- **NSArray** (object 30)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 59}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 29}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 46}`

- **NSString** (object 31)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '5549546f6f6c626172', '$text': 'UIToolbar'}`

- **NSString** (object 32)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '74657874436f6e7461696e657256696577', '$text': 'textContainerView'}`

- **UIRuntimeEventConnection** (object 33)
  - class: `UIRuntimeEventConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 17}`
    - `UISource` (type 10): `{'$ref': 3}`
    - `UIDestination` (type 10): `{'$ref': 49}`
    - `UIEventMask` (type 1): `4096`

- **UIBarButtonItem** (object 34)
  - class: `UIBarButtonItem`
  - raw values:
    - `UIEnabled` (type 5): `False`
    - `UIIsSystemItem` (type 5): `False`
    - `UISystemItem` (type 0): `5`

- **NSString** (object 35)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '7b3235302c203235307d', '$text': '{250, 250}'}`

- **NSNumber** (object 36)
  - class: `NSNumber`
  - raw values:
    - `NS.intval` (type 0): `1`

- **UIRuntimeOutletConnection** (object 37)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 68}`
    - `UISource` (type 10): `{'$ref': 49}`
    - `UIDestination` (type 10): `{'$ref': 51}`

- **UIColor** (object 38)
  - class: `UIColor`
  - raw values:
    - `UIColorComponentCount` (type 0): `4`
    - `UIRed` (type 6): `0.0`
    - `UIGreen` (type 6): `0.0`
    - `UIBlue` (type 6): `0.0`
    - `UIAlpha` (type 6): `0.0`
    - `NSRGB` (type 8): `{'$data_hex': '30203020302030', '$text': '0 0 0 0'}`
    - `NSColorSpace` (type 0): `2`

- **UIRuntimeOutletConnection** (object 39)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 1}`
    - `UISource` (type 10): `{'$ref': 49}`
    - `UIDestination` (type 10): `{'$ref': 28}`

- **NSString** (object 40)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '656e5f5553', '$text': 'en_US'}`

- **UIColor** (object 41)
  - class: `UIColor`
  - raw values:
    - `UIColorComponentCount` (type 0): `4`
    - `UIRed` (type 6): `0.9490196108818054`
    - `UIGreen` (type 6): `0.9490196108818054`
    - `UIBlue` (type 6): `0.9490196108818054`
    - `UIAlpha` (type 6): `1.0`
    - `NSRGB` (type 8): `{'$data_hex': '302e39343920302e39343920302e393439', '$text': '0.949 0.949 0.949'}`
    - `NSColorSpace` (type 0): `2`

- **NSString** (object 43)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '49424669727374526573706f6e646572', '$text': 'IBFirstResponder'}`

- **NSString** (object 44)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '6e6f74655465787456696577', '$text': 'noteTextView'}`

- **UIRuntimeEventConnection** (object 45)
  - class: `UIRuntimeEventConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 2}`
    - `UISource` (type 10): `{'$ref': 42}`
    - `UIDestination` (type 10): `{'$ref': 49}`

- **NSString** (object 47)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '7365744c6f636174696f6e416374696f6e3a', '$text': 'setLocationAction:'}`

- **UIProxyObject** (object 48)
  - class: `UIProxyObject`
  - raw values:
    - `UIProxiedObjectIdentifier` (type 10): `{'$ref': 43}`

- **UIButtonContent** (object 52)
  - class: `UIButtonContent`
  - raw values:
    - `UITitle` (type 10): `{'$ref': 69}`
    - `UITitleColor` (type 10): `{'$ref': 111}`
    - `UIShadowColor` (type 10): `{'$ref': 26}`

- **UIRuntimeOutletConnection** (object 53)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 72}`
    - `UISource` (type 10): `{'$ref': 49}`
    - `UIDestination` (type 10): `{'$ref': 24}`

- **NSString** (object 54)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '7365744c6f636174696f6e427574746f6e', '$text': 'setLocationButton'}`

- **NSMutableDictionary** (object 55)
  - class: `NSMutableDictionary`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 74}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 95}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 36}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 89}`

- **NSMutableArray** (object 56)
  - class: `NSMutableArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 10}`

- **NSDate** (object 57)
  - class: `NSDate`
  - raw values:
    - `NS.time` (type 7): `362628988.476194`

- **UIRuntimeEventConnection** (object 58)
  - class: `UIRuntimeEventConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 119}`
    - `UISource` (type 10): `{'$ref': 13}`
    - `UIDestination` (type 10): `{'$ref': 49}`

- **NSString** (object 60)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '48656c766574696361', '$text': 'Helvetica'}`

- **UIColor** (object 61)
  - class: `UIColor`
  - raw values:
    - `UIColorComponentCount` (type 0): `4`
    - `UIRed` (type 6): `0.5`
    - `UIGreen` (type 6): `0.5`
    - `UIBlue` (type 6): `0.5`
    - `UIAlpha` (type 6): `1.0`
    - `NSRGB` (type 8): `{'$data_hex': '302e3520302e3520302e35', '$text': '0.5 0.5 0.5'}`
    - `NSColorSpace` (type 0): `2`

- **UIFont** (object 62)
  - class: `UIFont`
  - raw values:
    - `UIFontName` (type 10): `{'$ref': 60}`
    - `UIFontPointSize` (type 7): `16.0`
    - `UIFontTraits` (type 0): `0`
    - `UISystemFont` (type 5): `False`
    - `NSName` (type 10): `{'$ref': 60}`
    - `NSSize` (type 7): `16.0`

- **NSLocale** (object 63)
  - class: `NSLocale`
  - raw values:
    - `NS.identifier` (type 10): `{'$ref': 40}`

- **NSArray** (object 64)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 122}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 96}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 86}`

- **NSString** (object 65)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '64656c657465416374696f6e3a', '$text': 'deleteAction:'}`

- **UIRuntimeOutletConnection** (object 66)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 11}`
    - `UISource` (type 10): `{'$ref': 49}`
    - `UIDestination` (type 10): `{'$ref': 10}`

- **UIButtonContent** (object 67)
  - class: `UIButtonContent`
  - raw values:
    - `UITitleColor` (type 10): `{'$ref': 26}`

- **NSString** (object 68)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '746f6f6c626172', '$text': 'toolbar'}`

- **NSString** (object 69)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '64656c657465', '$text': 'delete'}`

- **NSString** (object 72)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '7069636b6572546f6f6c626172', '$text': 'pickerToolbar'}`

- **UIRuntimeEventConnection** (object 73)
  - class: `UIRuntimeEventConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 102}`
    - `UISource` (type 10): `{'$ref': 86}`
    - `UIDestination` (type 10): `{'$ref': 49}`

- **NSNumber** (object 74)
  - class: `NSNumber`
  - raw values:
    - `NS.intval` (type 0): `0`

- **NSArray** (object 76)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 58}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 16}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 87}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 33}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 106}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 73}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 45}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 100}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 20}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 85}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 25}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 23}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 99}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 39}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 110}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 53}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 118}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 66}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 4}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 78}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 19}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 97}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 37}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 108}`

- **NSArray** (object 77)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 13}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 34}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 42}`

- **UIRuntimeOutletConnection** (object 78)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 92}`
    - `UISource` (type 10): `{'$ref': 49}`
    - `UIDestination` (type 10): `{'$ref': 75}`

- **NSString** (object 79)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '64656c6567617465', '$text': 'delegate'}`

- **NSString** (object 80)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '50686f6e654e6f746556696577496e7075744163636573736f7279', '$text': 'PhoneNoteViewInputAccessory'}`

- **NSString** (object 81)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '494246696c65734f776e6572', '$text': 'IBFilesOwner'}`

- **NSString** (object 82)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '696d675f636c6f636b2e706e67', '$text': 'img_clock.png'}`

- **NSString** (object 83)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '48656c7665746963612d426f6c64', '$text': 'Helvetica-Bold'}`

- **NSString** (object 84)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '73657452656d696e64657244617465416374696f6e3a', '$text': 'setReminderDateAction:'}`

- **UIRuntimeEventConnection** (object 85)
  - class: `UIRuntimeEventConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 113}`
    - `UISource` (type 10): `{'$ref': 75}`
    - `UIDestination` (type 10): `{'$ref': 49}`
    - `UIEventMask` (type 0): `64`

- **UIRuntimeEventConnection** (object 87)
  - class: `UIRuntimeEventConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 107}`
    - `UISource` (type 10): `{'$ref': 46}`
    - `UIDestination` (type 10): `{'$ref': 49}`

- **NSMutableArray** (object 88)
  - class: `NSMutableArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 71}`

- **UIButtonContent** (object 89)
  - class: `UIButtonContent`
  - raw values:
    - `UITitleColor` (type 10): `{'$ref': 26}`

- **NSArray** (object 90)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 49}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 48}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 21}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 70}`

- **NSString** (object 92)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '7365745370616365427574746f6e', '$text': 'setSpaceButton'}`

- **UIFont** (object 93)
  - class: `UIFont`
  - raw values:
    - `UIFontName` (type 10): `{'$ref': 83}`
    - `UIFontPointSize` (type 7): `15.0`
    - `UIFontTraits` (type 0): `2`
    - `UISystemFont` (type 5): `False`
    - `NSName` (type 10): `{'$ref': 83}`
    - `NSSize` (type 7): `15.0`

- **NSString** (object 94)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '64617465', '$text': 'date'}`

- **UIButtonContent** (object 95)
  - class: `UIButtonContent`
  - raw values:
    - `UITitle` (type 10): `{'$ref': 114}`
    - `UITitleColor` (type 10): `{'$ref': 105}`
    - `UIShadowColor` (type 10): `{'$ref': 61}`

- **UIBarButtonItem** (object 96)
  - class: `UIBarButtonItem`
  - raw values:
    - `UIEnabled` (type 5): `False`
    - `UIIsSystemItem` (type 5): `False`
    - `UISystemItem` (type 0): `5`

- **UIRuntimeOutletConnection** (object 97)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 32}`
    - `UISource` (type 10): `{'$ref': 49}`
    - `UIDestination` (type 10): `{'$ref': 104}`

- **NSMutableDictionary** (object 98)
  - class: `NSMutableDictionary`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 74}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 116}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 36}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 67}`

- **UIRuntimeOutletConnection** (object 99)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 79}`
    - `UISource` (type 10): `{'$ref': 70}`
    - `UIDestination` (type 10): `{'$ref': 49}`

- **UIRuntimeEventConnection** (object 100)
  - class: `UIRuntimeEventConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 47}`
    - `UISource` (type 10): `{'$ref': 121}`
    - `UIDestination` (type 10): `{'$ref': 49}`
    - `UIEventMask` (type 0): `64`

- **NSString** (object 101)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '536574204c6f636174696f6e', '$text': 'Set Location'}`

- **NSString** (object 102)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '646f6e6545646974696e67416374696f6e3a', '$text': 'doneEditingAction:'}`

- **NSString** (object 103)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '76696577', '$text': 'view'}`

- **UIColor** (object 105)
  - class: `UIColor`
  - raw values:
    - `UIColorComponentCount` (type 0): `4`
    - `UIRed` (type 6): `0.19607843458652496`
    - `UIGreen` (type 6): `0.30980393290519714`
    - `UIBlue` (type 6): `0.5215686559677124`
    - `UIAlpha` (type 6): `1.0`
    - `NSRGB` (type 8): `{'$data_hex': '302e31393620302e333120302e353232', '$text': '0.196 0.31 0.522'}`
    - `NSColorSpace` (type 0): `2`

- **UIRuntimeEventConnection** (object 106)
  - class: `UIRuntimeEventConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 65}`
    - `UISource` (type 10): `{'$ref': 28}`
    - `UIDestination` (type 10): `{'$ref': 49}`
    - `UIEventMask` (type 0): `64`

- **NSString** (object 107)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '636c6f7365446174655069636b6572416374696f6e3a', '$text': 'closeDatePickerAction:'}`

- **UIRuntimeOutletConnection** (object 108)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 103}`
    - `UISource` (type 10): `{'$ref': 49}`
    - `UIDestination` (type 10): `{'$ref': 21}`

- **NSArray** (object 109)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`

- **UIRuntimeOutletConnection** (object 110)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 44}`
    - `UISource` (type 10): `{'$ref': 49}`
    - `UIDestination` (type 10): `{'$ref': 91}`

- **UIColor** (object 111)
  - class: `UIColor`
  - raw values:
    - `UIColorComponentCount` (type 0): `4`
    - `UIRed` (type 6): `0.3333333432674408`
    - `UIGreen` (type 6): `0.3333333432674408`
    - `UIBlue` (type 6): `0.3333333432674408`
    - `UIAlpha` (type 6): `1.0`
    - `NSRGB` (type 8): `{'$data_hex': '302e33333320302e33333320302e333333', '$text': '0.333 0.333 0.333'}`
    - `NSColorSpace` (type 0): `2`

- **NSString** (object 112)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '72656d696e646572427574746f6e', '$text': 'reminderButton'}`

- **NSString** (object 113)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '7365745370616365416374696f6e3a', '$text': 'setSpaceAction:'}`

- **NSString** (object 114)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '536574205370616365', '$text': 'Set Space'}`

- **UIImageNibPlaceholder** (object 115)
  - class: `UIImageNibPlaceholder`
  - raw values:
    - `UIImageWidth` (type 6): `1.0`
    - `UIImageHeight` (type 6): `1.0`
    - `UIResourceName` (type 10): `{'$ref': 82}`

- **UIButtonContent** (object 116)
  - class: `UIButtonContent`
  - raw values:
    - `UITitle` (type 10): `{'$ref': 101}`
    - `UITitleColor` (type 10): `{'$ref': 105}`
    - `UIShadowColor` (type 10): `{'$ref': 61}`

- **UIColor** (object 117)
  - class: `UIColor`
  - raw values:
    - `UIColorComponentCount` (type 0): `4`
    - `UIRed` (type 6): `0.6666666865348816`
    - `UIGreen` (type 6): `0.6666666865348816`
    - `UIBlue` (type 6): `0.6666666865348816`
    - `UIAlpha` (type 6): `1.0`
    - `NSRGB` (type 8): `{'$data_hex': '302e36363720302e36363720302e363637', '$text': '0.667 0.667 0.667'}`
    - `NSColorSpace` (type 0): `2`

- **UIRuntimeOutletConnection** (object 118)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 112}`
    - `UISource` (type 10): `{'$ref': 49}`
    - `UIDestination` (type 10): `{'$ref': 50}`

- **NSString** (object 119)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '63616e63656c416e644469736d697373416374696f6e3a', '$text': 'cancelAndDismissAction:'}`

- **NSString** (object 120)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '746578744163636573736f727956696577', '$text': 'textAccessoryView'}`

- **UIBarButtonItem** (object 122)
  - class: `UIBarButtonItem`
  - raw values:
    - `UIEnabled` (type 5): `False`
    - `UIIsSystemItem` (type 5): `False`
    - `UISystemItem` (type 0): `6`
    - `UIWidth` (type 6): `42.0`

