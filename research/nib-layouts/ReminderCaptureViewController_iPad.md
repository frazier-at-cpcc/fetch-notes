# ReminderCaptureViewController_iPad

Recovered layout for `ReminderCaptureViewController_iPad.nib`. Every interpreted value appears beside the
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

- **UIView** (object 15)
  - class: `UIView`
  - frame: (0, 0, 540, 600)
  - raw UIBounds: (0, 0, 540, 600)
  - raw UICenter: (270, 300)
  - autoresizing mask: 18
  - background color: rgba(0.94902, 0.94902, 0.94902, 1)
  - hidden: not encoded
  - opaque: false
  - tag: not encoded
  - raw values:
    - `UIBounds` (type 8): `{'$data_hex': '0600000000000000000000074400001644', '$floats': [0.0, 0.0, 540.0, 600.0]}`
    - `UICenter` (type 8): `{'$data_hex': '060000874300009643', '$floats': [270.0, 300.0]}`
    - `UISubviews` (type 10): `{'$ref': 3}`
    - `UIBackgroundColor` (type 10): `{'$ref': 124}`
    - `UIOpaque` (type 5): `False`
    - `UIAutoresizeSubviews` (type 5): `False`
    - `UIAutoresizingMask` (type 0): `18`
  - **UIView** (object 101)
    - class: `UIView`
    - frame: (0, 184, 540, 306)
    - raw UIBounds: (0, 0, 540, 306)
    - raw UICenter: (270, 337)
    - autoresizing mask: 10
    - background color: rgba(0.94902, 0.94902, 0.94902, 1)
    - hidden: not encoded
    - opaque: false
    - tag: not encoded
    - raw values:
      - `UIBounds` (type 8): `{'$data_hex': '0600000000000000000000074400009943', '$floats': [0.0, 0.0, 540.0, 306.0]}`
      - `UICenter` (type 8): `{'$data_hex': '06000087430080a843', '$floats': [270.0, 337.0]}`
      - `UIBackgroundColor` (type 10): `{'$ref': 124}`
      - `UIOpaque` (type 5): `False`
      - `UIAutoresizeSubviews` (type 5): `False`
      - `UIAutoresizingMask` (type 0): `10`
  - **UIRoundedRectButton** (object 16)
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
    - target/action: `setLocationAction:` from object 16 (UIRoundedRectButton) to object 23 (UIProxyObject), event mask 64
    - raw values:
      - `UIBounds` (type 8): `{'$data_hex': '06000000000000000000008c4300001442', '$floats': [0.0, 0.0, 280.0, 37.0]}`
      - `UICenter` (type 8): `{'$data_hex': '06000020430040bc43', '$floats': [160.0, 376.5]}`
      - `UIAutoresizeSubviews` (type 5): `False`
      - `UIAutoresizingMask` (type 0): `36`
      - `UIButtonStatefulContent` (type 10): `{'$ref': 114}`
      - `UIAdjustsImageWhenHighlighted` (type 5): `False`
      - `UIAdjustsImageWhenDisabled` (type 5): `False`
      - `UIButtonType` (type 0): `1`
      - `UIFont` (type 10): `{'$ref': 85}`
  - **UIRoundedRectButton** (object 104)
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
    - target/action: `setSpaceAction:` from object 104 (UIRoundedRectButton) to object 23 (UIProxyObject), event mask 64
    - raw values:
      - `UIBounds` (type 8): `{'$data_hex': '06000000000000000000008c4300001442', '$floats': [0.0, 0.0, 280.0, 37.0]}`
      - `UICenter` (type 8): `{'$data_hex': '060000204300c0d243', '$floats': [160.0, 421.5]}`
      - `UIAutoresizeSubviews` (type 5): `False`
      - `UIAutoresizingMask` (type 0): `36`
      - `UIButtonStatefulContent` (type 10): `{'$ref': 17}`
      - `UIAdjustsImageWhenHighlighted` (type 5): `False`
      - `UIAdjustsImageWhenDisabled` (type 5): `False`
      - `UIButtonType` (type 0): `1`
      - `UIFont` (type 10): `{'$ref': 85}`
  - **UIToolbar** (object 107)
    - class: `UIToolbar`
    - frame: (0, 340, 540, 44)
    - raw UIBounds: (0, 0, 540, 44)
    - raw UICenter: (270, 362)
    - autoresizing mask: 10
    - background color: not encoded
    - hidden: false
    - opaque: false
    - tag: not encoded
    - raw values:
      - `UIBounds` (type 8): `{'$data_hex': '0600000000000000000000074400003042', '$floats': [0.0, 0.0, 540.0, 44.0]}`
      - `UICenter` (type 8): `{'$data_hex': '06000087430000b543', '$floats': [270.0, 362.0]}`
      - `UIOpaque` (type 5): `False`
      - `UIHidden` (type 5): `False`
      - `UIAutoresizeSubviews` (type 5): `False`
      - `UIAutoresizingMask` (type 0): `10`
      - `UIClearsContextBeforeDrawing` (type 4): `True`
      - `UIViewContentHuggingPriority` (type 10): `{'$ref': 7}`
      - `UIItems` (type 10): `{'$ref': 50}`
  - **UIDatePicker** (object 73)
    - class: `UIDatePicker`
    - frame: (0, 384, 540, 216)
    - raw UIBounds: (0, 0, 540, 216)
    - raw UICenter: (270, 492)
    - autoresizing mask: 10
    - background color: not encoded
    - hidden: not encoded
    - opaque: false
    - tag: not encoded
    - target/action: `datePickerChanged:` from object 73 (UIDatePicker) to object 23 (UIProxyObject), event mask 4096
    - raw values:
      - `UIBounds` (type 8): `{'$data_hex': '0600000000000000000000074400005843', '$floats': [0.0, 0.0, 540.0, 216.0]}`
      - `UICenter` (type 8): `{'$data_hex': '06000087430000f643', '$floats': [270.0, 492.0]}`
      - `UIOpaque` (type 5): `False`
      - `UIAutoresizeSubviews` (type 5): `False`
      - `UIAutoresizingMask` (type 0): `10`
      - `UIViewContentHuggingPriority` (type 10): `{'$ref': 7}`
      - `UILocale` (type 10): `{'$ref': 25}`
      - `UIDate` (type 10): `{'$ref': 29}`
      - `UIMinuteInterval` (type 0): `5`
  - **UIScrollView** (object 95)
    - class: `UIScrollView`
    - frame: (0, 44, 540, 296)
    - raw UIBounds: (0, 0, 540, 296)
    - raw UICenter: (270, 192)
    - autoresizing mask: 18
    - background color: rgba(0, 0, 0, 0)
    - hidden: not encoded
    - opaque: not encoded
    - tag: not encoded
    - raw values:
      - `UIBounds` (type 8): `{'$data_hex': '0600000000000000000000074400009443', '$floats': [0.0, 0.0, 540.0, 296.0]}`
      - `UICenter` (type 8): `{'$data_hex': '060000874300004043', '$floats': [270.0, 192.0]}`
      - `UISubviews` (type 10): `{'$ref': 112}`
      - `UIBackgroundColor` (type 10): `{'$ref': 84}`
      - `UIMultipleTouchEnabled` (type 5): `False`
      - `UIAutoresizeSubviews` (type 5): `False`
      - `UIAutoresizingMask` (type 0): `18`
      - `UIClipsToBounds` (type 5): `False`
      - `UIBouncesZoom` (type 5): `False`
    - **UIButton** (object 69)
      - class: `UIButton`
      - frame: (20, 20, 500, 47)
      - raw UIBounds: (0, 0, 500, 47)
      - raw UICenter: (270, 43.5)
      - autoresizing mask: 34
      - background color: not encoded
      - hidden: not encoded
      - opaque: not encoded
      - tag: not encoded
      - target/action: `setReminderDateAction:` from object 69 (UIButton) to object 23 (UIProxyObject), event mask 64
      - raw values:
        - `UIBounds` (type 8): `{'$data_hex': '0600000000000000000000fa4300003c42', '$floats': [0.0, 0.0, 500.0, 47.0]}`
        - `UICenter` (type 8): `{'$data_hex': '060000874300002e42', '$floats': [270.0, 43.5]}`
        - `UIAutoresizeSubviews` (type 5): `False`
        - `UIAutoresizingMask` (type 0): `34`
        - `UIContentHorizontalAlignment` (type 0): `1`
        - `UIButtonStatefulContent` (type 10): `{'$ref': 111}`
        - `UIReversesTitleShadowWhenHighlighted` (type 5): `False`
        - `UIAdjustsImageWhenHighlighted` (type 5): `False`
        - `UIAdjustsImageWhenDisabled` (type 5): `False`
        - `UIContentEdgeInsets` (type 8): `{'$data_hex': '060000a0400000a0400000a0400000a040', '$floats': [5.0, 5.0, 5.0, 5.0]}`
        - `UITitleEdgeInsets` (type 8): `{'$data_hex': '0600000000000080410000000000000000', '$floats': [0.0, 16.0, 0.0, 0.0]}`
        - `UITitleShadowOffset` (type 8): `{'$data_hex': '06000000000000803f', '$floats': [0.0, 1.0]}`
        - `UIImageEdgeInsets` (type 8): `{'$data_hex': '06000000000000a0400000000000000000', '$floats': [0.0, 5.0, 0.0, 0.0]}`
    - **UIButton** (object 74)
      - class: `UIButton`
      - frame: (20, 75, 500, 47)
      - raw UIBounds: (0, 0, 500, 47)
      - raw UICenter: (270, 98.5)
      - autoresizing mask: 34
      - background color: not encoded
      - hidden: not encoded
      - opaque: not encoded
      - tag: not encoded
      - target/action: `deleteAction:` from object 74 (UIButton) to object 23 (UIProxyObject), event mask 64
      - raw values:
        - `UIBounds` (type 8): `{'$data_hex': '0600000000000000000000fa4300003c42', '$floats': [0.0, 0.0, 500.0, 47.0]}`
        - `UICenter` (type 8): `{'$data_hex': '06000087430000c542', '$floats': [270.0, 98.5]}`
        - `UIAutoresizeSubviews` (type 5): `False`
        - `UIAutoresizingMask` (type 0): `34`
        - `UIButtonStatefulContent` (type 10): `{'$ref': 34}`
        - `UIReversesTitleShadowWhenHighlighted` (type 5): `False`
        - `UIAdjustsImageWhenHighlighted` (type 5): `False`
        - `UIAdjustsImageWhenDisabled` (type 5): `False`
        - `UITitleShadowOffset` (type 8): `{'$data_hex': '06000000000000803f', '$floats': [0.0, 1.0]}`
    - **UIPlaceHolderTextView** (object 118)
      - class: `UIPlaceHolderTextView`
      - encoded as: `UIClassSwapper` swapping `UITextView`
      - frame: (11, 75, 518, 211)
      - raw UIBounds: (0, 0, 518, 211)
      - raw UICenter: (270, 180.5)
      - autoresizing mask: 34
      - background color: rgba(0.94902, 0.94902, 0.94902, 1)
      - font: Helvetica 16pt
      - hidden: not encoded
      - opaque: false
      - tag: not encoded
      - outlet: `delegate` to object 23 (UIProxyObject)
      - raw values:
        - `UIBounds` (type 8): `{'$data_hex': '0600000000000000000080014400005343', '$floats': [0.0, 0.0, 518.0, 211.0]}`
        - `UICenter` (type 8): `{'$data_hex': '060000874300803443', '$floats': [270.0, 180.5]}`
        - `UISubviews` (type 10): `{'$ref': 66}`
        - `UIBackgroundColor` (type 10): `{'$ref': 124}`
        - `UIOpaque` (type 5): `False`
        - `UIMultipleTouchEnabled` (type 5): `False`
        - `UIAutoresizeSubviews` (type 5): `False`
        - `UIAutoresizingMask` (type 0): `34`
        - `UIClipsToBounds` (type 5): `False`
        - `UIShowsHorizontalScrollIndicator` (type 4): `True`
        - `UIShowsVerticalScrollIndicator` (type 4): `True`
        - `UIScrollDisabled` (type 5): `False`
        - `UIBouncesZoom` (type 5): `False`
        - `UIContentSize` (type 8): `{'$data_hex': '060080014400001042', '$floats': [518.0, 36.0]}`
        - `UIFont` (type 10): `{'$ref': 11}`
        - `UITextColor` (type 10): `{'$ref': 52}`
        - `UITextAlignment` (type 0): `0`
        - `UIClassName` (type 10): `{'$ref': 81}`
        - `UIOriginalClassName` (type 10): `{'$ref': 103}`
      - **UITextSelectionView** (object 92)
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
  - **UINavigationBar** (object 108)
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
      - `UIViewContentHuggingPriority` (type 10): `{'$ref': 7}`
      - `UIItems` (type 10): `{'$ref': 86}`

- **UIProxyObject** (object 23)
  - class: `UIProxyObject`
  - outlet: `textContainerView` to object 101 (UIView)
  - outlet: `setSpaceButton` to object 104 (UIRoundedRectButton)
  - outlet: `scrollView` to object 95 (UIScrollView)
  - outlet: `pickerToolbar` to object 107 (UIToolbar)
  - outlet: `toolbar` to object 108 (UINavigationBar)
  - outlet: `textAccessoryView` to object 61 (PadNoteViewInputAccessory)
  - outlet: `setLocationButton` to object 16 (UIRoundedRectButton)
  - outlet: `deleteButton` to object 74 (UIButton)
  - outlet: `reminderButton` to object 69 (UIButton)
  - outlet: `noteTextView` to object 118 (UIPlaceHolderTextView)
  - outlet: `view` to object 15 (UIView)
  - outlet: `datePicker` to object 73 (UIDatePicker)
  - target/action: `closeDatePickerAction:` from object 93 (UIBarButtonItem) to object 23 (UIProxyObject), event mask not encoded
  - target/action: `doneEditingAction:` from object 57 (UIBarButtonItem) to object 23 (UIProxyObject), event mask not encoded
  - target/action: `cancelAndDismissAction:` from object 62 (UIBarButtonItem) to object 23 (UIProxyObject), event mask not encoded
  - target/action: `cancelAndDismissAction:` from object 68 (UIBarButtonItem) to object 23 (UIProxyObject), event mask not encoded
  - target/action: `deleteAction:` from object 74 (UIButton) to object 23 (UIProxyObject), event mask 64
  - target/action: `setLocationAction:` from object 16 (UIRoundedRectButton) to object 23 (UIProxyObject), event mask 64
  - target/action: `datePickerChanged:` from object 73 (UIDatePicker) to object 23 (UIProxyObject), event mask 4096
  - target/action: `saveAndDismissAction:` from object 98 (UIBarButtonItem) to object 23 (UIProxyObject), event mask not encoded
  - target/action: `setSpaceAction:` from object 104 (UIRoundedRectButton) to object 23 (UIProxyObject), event mask 64
  - target/action: `setReminderDateAction:` from object 69 (UIButton) to object 23 (UIProxyObject), event mask 64
  - raw values:
    - `UIProxiedObjectIdentifier` (type 10): `{'$ref': 54}`

- **UIBarButtonItem** (object 57)
  - class: `UIBarButtonItem`
  - target/action: `doneEditingAction:` from object 57 (UIBarButtonItem) to object 23 (UIProxyObject), event mask not encoded
  - raw values:
    - `UIEnabled` (type 5): `False`
    - `UIIsSystemItem` (type 5): `False`
    - `UISystemItem` (type 0): `0`
    - `UIStyle` (type 0): `2`

- **PadNoteViewInputAccessory** (object 61)
  - class: `PadNoteViewInputAccessory`
  - encoded as: `UIClassSwapper` swapping `UIToolbar`
  - frame: (0, 0, 320, 44)
  - raw UIBounds: (0, 0, 320, 44)
  - raw UICenter: (160, 22)
  - autoresizing mask: 10
  - background color: not encoded
  - hidden: not encoded
  - opaque: false
  - tag: not encoded
  - outlet: `delegate` to object 23 (UIProxyObject)
  - raw values:
    - `UIBounds` (type 8): `{'$data_hex': '0600000000000000000000a04300003042', '$floats': [0.0, 0.0, 320.0, 44.0]}`
    - `UICenter` (type 8): `{'$data_hex': '06000020430000b041', '$floats': [160.0, 22.0]}`
    - `UIOpaque` (type 5): `False`
    - `UIAutoresizeSubviews` (type 5): `False`
    - `UIAutoresizingMask` (type 0): `10`
    - `UIClearsContextBeforeDrawing` (type 4): `True`
    - `UIViewContentHuggingPriority` (type 10): `{'$ref': 7}`
    - `UIItems` (type 10): `{'$ref': 45}`
    - `UIClassName` (type 10): `{'$ref': 33}`
    - `UIOriginalClassName` (type 10): `{'$ref': 90}`

- **UIBarButtonItem** (object 62)
  - class: `UIBarButtonItem`
  - target/action: `cancelAndDismissAction:` from object 62 (UIBarButtonItem) to object 23 (UIProxyObject), event mask not encoded
  - raw values:
    - `UIEnabled` (type 5): `False`
    - `UIIsSystemItem` (type 5): `False`
    - `UISystemItem` (type 0): `1`
    - `UIStyle` (type 0): `1`

- **UIBarButtonItem** (object 68)
  - class: `UIBarButtonItem`
  - target/action: `cancelAndDismissAction:` from object 68 (UIBarButtonItem) to object 23 (UIProxyObject), event mask not encoded
  - raw values:
    - `UIEnabled` (type 5): `False`
    - `UIIsSystemItem` (type 5): `False`
    - `UISystemItem` (type 0): `1`
    - `UIStyle` (type 0): `1`

- **UIBarButtonItem** (object 93)
  - class: `UIBarButtonItem`
  - target/action: `closeDatePickerAction:` from object 93 (UIBarButtonItem) to object 23 (UIProxyObject), event mask not encoded
  - raw values:
    - `UIEnabled` (type 5): `False`
    - `UIIsSystemItem` (type 5): `False`
    - `UISystemItem` (type 0): `0`
    - `UIStyle` (type 0): `1`

- **UIBarButtonItem** (object 98)
  - class: `UIBarButtonItem`
  - target/action: `saveAndDismissAction:` from object 98 (UIBarButtonItem) to object 23 (UIProxyObject), event mask not encoded
  - raw values:
    - `UIEnabled` (type 5): `False`
    - `UIIsSystemItem` (type 5): `False`
    - `UISystemItem` (type 0): `3`
    - `UIStyle` (type 0): `1`

## Supporting objects

These objects carry no geometry, contain no view, and hold no
connection. They remain here because a reader auditing an
interpretation follows a reference into them.

- **NSObject** (object 0)
  - class: `NSObject`
  - raw values:
    - `UINibTopLevelObjectsKey` (type 10): `{'$ref': 22}`
    - `UINibObjectsKey` (type 10): `{'$ref': 89}`
    - `UINibConnectionsKey` (type 10): `{'$ref': 39}`
    - `UINibVisibleWindowsKey` (type 10): `{'$ref': 121}`
    - `UINibAccessibilityConfigurationsKey` (type 10): `{'$ref': 121}`
    - `UINibKeyValuePairsKey` (type 10): `{'$ref': 121}`

- **NSString** (object 1)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '7365745370616365427574746f6e', '$text': 'setSpaceButton'}`

- **UIRuntimeOutletConnection** (object 2)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 64}`
    - `UISource` (type 10): `{'$ref': 23}`
    - `UIDestination` (type 10): `{'$ref': 101}`

- **NSMutableArray** (object 3)
  - class: `NSMutableArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 101}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 16}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 104}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 107}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 73}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 95}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 108}`

- **UIBarButtonItem** (object 4)
  - class: `UIBarButtonItem`
  - raw values:
    - `UIEnabled` (type 5): `False`
    - `UIIsSystemItem` (type 5): `False`
    - `UISystemItem` (type 0): `6`
    - `UIWidth` (type 6): `42.0`

- **NSString** (object 5)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '5469746c65', '$text': 'Title'}`

- **NSString** (object 6)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '656e5f5553', '$text': 'en_US'}`

- **NSString** (object 7)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '7b3235302c203235307d', '$text': '{250, 250}'}`

- **NSString** (object 8)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '696d675f636c6f636b2e706e67', '$text': 'img_clock.png'}`

- **NSString** (object 9)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '646f6e6545646974696e67416374696f6e3a', '$text': 'doneEditingAction:'}`

- **NSString** (object 10)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '76696577', '$text': 'view'}`

- **UIFont** (object 11)
  - class: `UIFont`
  - raw values:
    - `UIFontName` (type 10): `{'$ref': 65}`
    - `UIFontPointSize` (type 7): `16.0`
    - `UIFontTraits` (type 0): `0`
    - `UISystemFont` (type 5): `False`
    - `NSName` (type 10): `{'$ref': 65}`
    - `NSSize` (type 7): `16.0`

- **UIRuntimeOutletConnection** (object 12)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 1}`
    - `UISource` (type 10): `{'$ref': 23}`
    - `UIDestination` (type 10): `{'$ref': 104}`

- **NSString** (object 13)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '636c6f7365446174655069636b6572416374696f6e3a', '$text': 'closeDatePickerAction:'}`

- **UIRuntimeEventConnection** (object 14)
  - class: `UIRuntimeEventConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 13}`
    - `UISource` (type 10): `{'$ref': 93}`
    - `UIDestination` (type 10): `{'$ref': 23}`

- **NSMutableDictionary** (object 17)
  - class: `NSMutableDictionary`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 36}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 41}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 80}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 35}`

- **UIRuntimeEventConnection** (object 18)
  - class: `UIRuntimeEventConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 9}`
    - `UISource` (type 10): `{'$ref': 57}`
    - `UIDestination` (type 10): `{'$ref': 23}`

- **NSString** (object 19)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '72656d696e646572427574746f6e', '$text': 'reminderButton'}`

- **NSString** (object 20)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '7365745370616365416374696f6e3a', '$text': 'setSpaceAction:'}`

- **NSString** (object 21)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '49424669727374526573706f6e646572', '$text': 'IBFirstResponder'}`

- **NSArray** (object 22)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 23}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 32}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 15}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 61}`

- **UIRuntimeOutletConnection** (object 24)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 47}`
    - `UISource` (type 10): `{'$ref': 23}`
    - `UIDestination` (type 10): `{'$ref': 95}`

- **NSLocale** (object 25)
  - class: `NSLocale`
  - raw values:
    - `NS.identifier` (type 10): `{'$ref': 6}`

- **NSString** (object 26)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '63616e63656c416e644469736d697373416374696f6e3a', '$text': 'cancelAndDismissAction:'}`

- **NSArray** (object 27)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 62}`

- **NSString** (object 28)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '746578744163636573736f727956696577', '$text': 'textAccessoryView'}`

- **NSDate** (object 29)
  - class: `NSDate`
  - raw values:
    - `NS.time` (type 7): `362628988.476194`

- **UIRuntimeEventConnection** (object 30)
  - class: `UIRuntimeEventConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 26}`
    - `UISource` (type 10): `{'$ref': 62}`
    - `UIDestination` (type 10): `{'$ref': 23}`

- **UIRuntimeOutletConnection** (object 31)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 120}`
    - `UISource` (type 10): `{'$ref': 61}`
    - `UIDestination` (type 10): `{'$ref': 23}`

- **UIProxyObject** (object 32)
  - class: `UIProxyObject`
  - raw values:
    - `UIProxiedObjectIdentifier` (type 10): `{'$ref': 21}`

- **NSString** (object 33)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '5061644e6f746556696577496e7075744163636573736f7279', '$text': 'PadNoteViewInputAccessory'}`

- **NSMutableDictionary** (object 34)
  - class: `NSMutableDictionary`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 36}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 43}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 80}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 96}`

- **UIButtonContent** (object 35)
  - class: `UIButtonContent`
  - raw values:
    - `UITitleColor` (type 10): `{'$ref': 70}`

- **NSNumber** (object 36)
  - class: `NSNumber`
  - raw values:
    - `NS.intval` (type 0): `0`

- **UIRuntimeOutletConnection** (object 37)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 116}`
    - `UISource` (type 10): `{'$ref': 23}`
    - `UIDestination` (type 10): `{'$ref': 107}`

- **NSString** (object 38)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '64656c657465427574746f6e', '$text': 'deleteButton'}`

- **NSArray** (object 39)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 30}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 51}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 14}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 75}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 60}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 18}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 88}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 71}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 122}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 110}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 123}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 58}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 31}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 94}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 115}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 37}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 100}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 24}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 82}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 12}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 67}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 2}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 56}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 119}`

- **NSString** (object 40)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '73617665416e644469736d697373416374696f6e3a', '$text': 'saveAndDismissAction:'}`

- **UIButtonContent** (object 41)
  - class: `UIButtonContent`
  - raw values:
    - `UITitle` (type 10): `{'$ref': 49}`
    - `UITitleColor` (type 10): `{'$ref': 83}`
    - `UIShadowColor` (type 10): `{'$ref': 109}`

- **NSString** (object 42)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '64617465', '$text': 'date'}`

- **UIButtonContent** (object 43)
  - class: `UIButtonContent`
  - raw values:
    - `UITitle` (type 10): `{'$ref': 97}`
    - `UITitleColor` (type 10): `{'$ref': 52}`
    - `UIShadowColor` (type 10): `{'$ref': 70}`

- **NSString** (object 44)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '536574204c6f636174696f6e', '$text': 'Set Location'}`

- **NSArray** (object 45)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 4}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 63}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 57}`

- **UINavigationItem** (object 46)
  - class: `UINavigationItem`
  - raw values:
    - `UITitle` (type 10): `{'$ref': 5}`
    - `UILeftBarButtonItem` (type 10): `{'$ref': 62}`
    - `UIRightBarButtonItem` (type 10): `{'$ref': 98}`
    - `UILeftBarButtonItems` (type 10): `{'$ref': 27}`
    - `UIRightBarButtonItems` (type 10): `{'$ref': 87}`
    - `UINavigationBar` (type 10): `{'$ref': 108}`

- **NSString** (object 47)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '7363726f6c6c56696577', '$text': 'scrollView'}`

- **UIButtonContent** (object 48)
  - class: `UIButtonContent`
  - raw values:
    - `UITitle` (type 10): `{'$ref': 42}`
    - `UIImage` (type 10): `{'$ref': 72}`
    - `UITitleColor` (type 10): `{'$ref': 52}`
    - `UIShadowColor` (type 10): `{'$ref': 70}`

- **NSString** (object 49)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '536574205370616365', '$text': 'Set Space'}`

- **NSArray** (object 50)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 68}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 79}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 93}`

- **UIRuntimeEventConnection** (object 51)
  - class: `UIRuntimeEventConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 26}`
    - `UISource` (type 10): `{'$ref': 68}`
    - `UIDestination` (type 10): `{'$ref': 23}`

- **UIColor** (object 52)
  - class: `UIColor`
  - raw values:
    - `UIColorComponentCount` (type 0): `4`
    - `UIRed` (type 6): `0.3333333432674408`
    - `UIGreen` (type 6): `0.3333333432674408`
    - `UIBlue` (type 6): `0.3333333432674408`
    - `UIAlpha` (type 6): `1.0`
    - `NSRGB` (type 8): `{'$data_hex': '302e33333320302e33333320302e333333', '$text': '0.333 0.333 0.333'}`
    - `NSColorSpace` (type 0): `2`

- **NSString** (object 53)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '646174655069636b65724368616e6765643a', '$text': 'datePickerChanged:'}`

- **NSString** (object 54)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '494246696c65734f776e6572', '$text': 'IBFilesOwner'}`

- **NSString** (object 55)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '646174655069636b6572', '$text': 'datePicker'}`

- **UIRuntimeOutletConnection** (object 56)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 106}`
    - `UISource` (type 10): `{'$ref': 23}`
    - `UIDestination` (type 10): `{'$ref': 108}`

- **UIRuntimeOutletConnection** (object 58)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 120}`
    - `UISource` (type 10): `{'$ref': 118}`
    - `UIDestination` (type 10): `{'$ref': 23}`

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

- **UIRuntimeEventConnection** (object 60)
  - class: `UIRuntimeEventConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 105}`
    - `UISource` (type 10): `{'$ref': 74}`
    - `UIDestination` (type 10): `{'$ref': 23}`
    - `UIEventMask` (type 0): `64`

- **UIBarButtonItem** (object 63)
  - class: `UIBarButtonItem`
  - raw values:
    - `UIEnabled` (type 5): `False`
    - `UIIsSystemItem` (type 5): `False`
    - `UISystemItem` (type 0): `5`

- **NSString** (object 64)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '74657874436f6e7461696e657256696577', '$text': 'textContainerView'}`

- **NSString** (object 65)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '48656c766574696361', '$text': 'Helvetica'}`

- **NSMutableArray** (object 66)
  - class: `NSMutableArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 92}`

- **UIRuntimeOutletConnection** (object 67)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 28}`
    - `UISource` (type 10): `{'$ref': 23}`
    - `UIDestination` (type 10): `{'$ref': 61}`

- **UIColor** (object 70)
  - class: `UIColor`
  - raw values:
    - `UIColorComponentCount` (type 0): `4`
    - `UIRed` (type 6): `1.0`
    - `UIGreen` (type 6): `1.0`
    - `UIBlue` (type 6): `1.0`
    - `UIAlpha` (type 6): `1.0`
    - `NSRGB` (type 8): `{'$data_hex': '3120312031', '$text': '1 1 1'}`
    - `NSColorSpace` (type 0): `2`

- **UIRuntimeEventConnection** (object 71)
  - class: `UIRuntimeEventConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 78}`
    - `UISource` (type 10): `{'$ref': 16}`
    - `UIDestination` (type 10): `{'$ref': 23}`
    - `UIEventMask` (type 0): `64`

- **UIImageNibPlaceholder** (object 72)
  - class: `UIImageNibPlaceholder`
  - raw values:
    - `UIImageWidth` (type 6): `1.0`
    - `UIImageHeight` (type 6): `1.0`
    - `UIResourceName` (type 10): `{'$ref': 8}`

- **UIRuntimeEventConnection** (object 75)
  - class: `UIRuntimeEventConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 53}`
    - `UISource` (type 10): `{'$ref': 73}`
    - `UIDestination` (type 10): `{'$ref': 23}`
    - `UIEventMask` (type 1): `4096`

- **NSString** (object 76)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '6e6f74655465787456696577', '$text': 'noteTextView'}`

- **UIButtonContent** (object 77)
  - class: `UIButtonContent`
  - raw values:
    - `UITitleColor` (type 10): `{'$ref': 59}`
    - `UIShadowColor` (type 10): `{'$ref': 52}`

- **NSString** (object 78)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '7365744c6f636174696f6e416374696f6e3a', '$text': 'setLocationAction:'}`

- **UIBarButtonItem** (object 79)
  - class: `UIBarButtonItem`
  - raw values:
    - `UIEnabled` (type 5): `False`
    - `UIIsSystemItem` (type 5): `False`
    - `UISystemItem` (type 0): `5`

- **NSNumber** (object 80)
  - class: `NSNumber`
  - raw values:
    - `NS.intval` (type 0): `1`

- **NSString** (object 81)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '5549506c616365486f6c6465725465787456696577', '$text': 'UIPlaceHolderTextView'}`

- **UIRuntimeOutletConnection** (object 82)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 91}`
    - `UISource` (type 10): `{'$ref': 23}`
    - `UIDestination` (type 10): `{'$ref': 16}`

- **UIColor** (object 83)
  - class: `UIColor`
  - raw values:
    - `UIColorComponentCount` (type 0): `4`
    - `UIRed` (type 6): `0.19607843458652496`
    - `UIGreen` (type 6): `0.30980393290519714`
    - `UIBlue` (type 6): `0.5215686559677124`
    - `UIAlpha` (type 6): `1.0`
    - `NSRGB` (type 8): `{'$data_hex': '302e31393620302e333120302e353232', '$text': '0.196 0.31 0.522'}`
    - `NSColorSpace` (type 0): `2`

- **UIColor** (object 84)
  - class: `UIColor`
  - raw values:
    - `UIColorComponentCount` (type 0): `4`
    - `UIRed` (type 6): `0.0`
    - `UIGreen` (type 6): `0.0`
    - `UIBlue` (type 6): `0.0`
    - `UIAlpha` (type 6): `0.0`
    - `NSRGB` (type 8): `{'$data_hex': '30203020302030', '$text': '0 0 0 0'}`
    - `NSColorSpace` (type 0): `2`

- **UIFont** (object 85)
  - class: `UIFont`
  - raw values:
    - `UIFontName` (type 10): `{'$ref': 113}`
    - `UIFontPointSize` (type 7): `15.0`
    - `UIFontTraits` (type 0): `2`
    - `UISystemFont` (type 5): `False`
    - `NSName` (type 10): `{'$ref': 113}`
    - `NSSize` (type 7): `15.0`

- **NSMutableArray** (object 86)
  - class: `NSMutableArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 46}`

- **NSArray** (object 87)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 98}`

- **UIRuntimeEventConnection** (object 88)
  - class: `UIRuntimeEventConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 40}`
    - `UISource` (type 10): `{'$ref': 98}`
    - `UIDestination` (type 10): `{'$ref': 23}`

- **NSArray** (object 89)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 23}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 32}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 15}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 61}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 101}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 16}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 104}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 107}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 73}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 95}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 108}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 4}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 63}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 57}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 68}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 79}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 93}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 69}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 74}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 118}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 46}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 62}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 98}`

- **NSString** (object 90)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '5549546f6f6c626172', '$text': 'UIToolbar'}`

- **NSString** (object 91)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '7365744c6f636174696f6e427574746f6e', '$text': 'setLocationButton'}`

- **UIRuntimeOutletConnection** (object 94)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 38}`
    - `UISource` (type 10): `{'$ref': 23}`
    - `UIDestination` (type 10): `{'$ref': 74}`

- **UIButtonContent** (object 96)
  - class: `UIButtonContent`
  - raw values:
    - `UITitleColor` (type 10): `{'$ref': 59}`
    - `UIShadowColor` (type 10): `{'$ref': 52}`

- **NSString** (object 97)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '64656c657465', '$text': 'delete'}`

- **UIButtonContent** (object 99)
  - class: `UIButtonContent`
  - raw values:
    - `UITitleColor` (type 10): `{'$ref': 70}`

- **UIRuntimeOutletConnection** (object 100)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 19}`
    - `UISource` (type 10): `{'$ref': 23}`
    - `UIDestination` (type 10): `{'$ref': 69}`

- **UIButtonContent** (object 102)
  - class: `UIButtonContent`
  - raw values:
    - `UITitle` (type 10): `{'$ref': 44}`
    - `UITitleColor` (type 10): `{'$ref': 83}`
    - `UIShadowColor` (type 10): `{'$ref': 109}`

- **NSString** (object 103)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '55495465787456696577', '$text': 'UITextView'}`

- **NSString** (object 105)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '64656c657465416374696f6e3a', '$text': 'deleteAction:'}`

- **NSString** (object 106)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '746f6f6c626172', '$text': 'toolbar'}`

- **UIColor** (object 109)
  - class: `UIColor`
  - raw values:
    - `UIColorComponentCount` (type 0): `4`
    - `UIRed` (type 6): `0.5`
    - `UIGreen` (type 6): `0.5`
    - `UIBlue` (type 6): `0.5`
    - `UIAlpha` (type 6): `1.0`
    - `NSRGB` (type 8): `{'$data_hex': '302e3520302e3520302e35', '$text': '0.5 0.5 0.5'}`
    - `NSColorSpace` (type 0): `2`

- **UIRuntimeEventConnection** (object 110)
  - class: `UIRuntimeEventConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 20}`
    - `UISource` (type 10): `{'$ref': 104}`
    - `UIDestination` (type 10): `{'$ref': 23}`
    - `UIEventMask` (type 0): `64`

- **NSMutableDictionary** (object 111)
  - class: `NSMutableDictionary`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 36}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 48}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 80}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 77}`

- **NSMutableArray** (object 112)
  - class: `NSMutableArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 69}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 74}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 118}`

- **NSString** (object 113)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '48656c7665746963612d426f6c64', '$text': 'Helvetica-Bold'}`

- **NSMutableDictionary** (object 114)
  - class: `NSMutableDictionary`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 36}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 102}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 80}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 99}`

- **UIRuntimeOutletConnection** (object 115)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 76}`
    - `UISource` (type 10): `{'$ref': 23}`
    - `UIDestination` (type 10): `{'$ref': 118}`

- **NSString** (object 116)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '7069636b6572546f6f6c626172', '$text': 'pickerToolbar'}`

- **NSString** (object 117)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '73657452656d696e64657244617465416374696f6e3a', '$text': 'setReminderDateAction:'}`

- **UIRuntimeOutletConnection** (object 119)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 10}`
    - `UISource` (type 10): `{'$ref': 23}`
    - `UIDestination` (type 10): `{'$ref': 15}`

- **NSString** (object 120)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '64656c6567617465', '$text': 'delegate'}`

- **NSArray** (object 121)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`

- **UIRuntimeEventConnection** (object 122)
  - class: `UIRuntimeEventConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 117}`
    - `UISource` (type 10): `{'$ref': 69}`
    - `UIDestination` (type 10): `{'$ref': 23}`
    - `UIEventMask` (type 0): `64`

- **UIRuntimeOutletConnection** (object 123)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 55}`
    - `UISource` (type 10): `{'$ref': 23}`
    - `UIDestination` (type 10): `{'$ref': 73}`

- **UIColor** (object 124)
  - class: `UIColor`
  - raw values:
    - `UIColorComponentCount` (type 0): `4`
    - `UIRed` (type 6): `0.9490196108818054`
    - `UIGreen` (type 6): `0.9490196108818054`
    - `UIBlue` (type 6): `0.9490196108818054`
    - `UIAlpha` (type 6): `1.0`
    - `NSRGB` (type 8): `{'$data_hex': '302e39343920302e39343920302e393439', '$text': '0.949 0.949 0.949'}`
    - `NSColorSpace` (type 0): `2`

