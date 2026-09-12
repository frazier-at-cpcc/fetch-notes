# VoiceCaptureViewController_iPhone

Recovered layout for `VoiceCaptureViewController_iPhone.nib`. Every interpreted value appears beside the
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

- **UIBarButtonItem** (object 47)
  - class: `UIBarButtonItem`
  - target/action: `doneEditingAction:` from object 47 (UIBarButtonItem) to object 64 (UIProxyObject), event mask not encoded
  - raw values:
    - `UIEnabled` (type 5): `False`
    - `UIIsSystemItem` (type 5): `False`
    - `UISystemItem` (type 0): `0`
    - `UIStyle` (type 0): `2`

- **UIBarButtonItem** (object 48)
  - class: `UIBarButtonItem`
  - target/action: `saveAndDismissAction:` from object 48 (UIBarButtonItem) to object 64 (UIProxyObject), event mask not encoded
  - raw values:
    - `UIEnabled` (type 5): `False`
    - `UIIsSystemItem` (type 5): `False`
    - `UISystemItem` (type 0): `3`
    - `UIStyle` (type 0): `1`

- **UIProxyObject** (object 64)
  - class: `UIProxyObject`
  - outlet: `toolbar` to object 38 (UIToolbar)
  - outlet: `textAccessoryView` to object 81 (PhoneNoteViewInputAccessory)
  - outlet: `setSpaceButton` to object 13 (UIRoundedRectButton)
  - outlet: `pauseResumeButton` to object 91 (UIButton)
  - outlet: `micView` to object 120 (MicMeterView)
  - outlet: `view` to object 75 (UIView)
  - outlet: `textContainerView` to object 108 (UIView)
  - outlet: `statusLabel` to object 115 (UILabel)
  - outlet: `setLocationButton` to object 50 (UIRoundedRectButton)
  - outlet: `controlContainerView` to object 18 (UIView)
  - outlet: `noteTextView` to object 93 (UIPlaceHolderTextView)
  - outlet: `durationLabel` to object 74 (UILabel)
  - outlet: `miniPauseResumeButton` to object 121 (UIButton)
  - target/action: `doneEditingAction:` from object 47 (UIBarButtonItem) to object 64 (UIProxyObject), event mask not encoded
  - target/action: `pauseResumeAction:` from object 121 (UIButton) to object 64 (UIProxyObject), event mask 64
  - target/action: `cancelAndDismissAction:` from object 98 (UIBarButtonItem) to object 64 (UIProxyObject), event mask not encoded
  - target/action: `setLocationAction:` from object 50 (UIRoundedRectButton) to object 64 (UIProxyObject), event mask 64
  - target/action: `pauseResumeAction:` from object 91 (UIButton) to object 64 (UIProxyObject), event mask 64
  - target/action: `saveAndDismissAction:` from object 48 (UIBarButtonItem) to object 64 (UIProxyObject), event mask not encoded
  - target/action: `setSpaceAction:` from object 13 (UIRoundedRectButton) to object 64 (UIProxyObject), event mask 64
  - raw values:
    - `UIProxiedObjectIdentifier` (type 10): `{'$ref': 27}`

- **UIView** (object 75)
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
    - `UISubviews` (type 10): `{'$ref': 37}`
    - `UIBackgroundColor` (type 10): `{'$ref': 119}`
    - `UIOpaque` (type 5): `False`
    - `UIAutoresizeSubviews` (type 5): `False`
    - `UIAutoresizingMask` (type 0): `18`
  - **UIToolbar** (object 38)
    - class: `UIToolbar`
    - frame: (0, 0, 320, 44)
    - raw UIBounds: (0, 0, 320, 44)
    - raw UICenter: (160, 22)
    - autoresizing mask: 34
    - background color: rgba(0.746363, 0.746341, 0.746354, 1)
    - hidden: not encoded
    - opaque: false
    - tag: not encoded
    - raw values:
      - `UIBounds` (type 8): `{'$data_hex': '0600000000000000000000a04300003042', '$floats': [0.0, 0.0, 320.0, 44.0]}`
      - `UICenter` (type 8): `{'$data_hex': '06000020430000b041', '$floats': [160.0, 22.0]}`
      - `UIBackgroundColor` (type 10): `{'$ref': 95}`
      - `UIOpaque` (type 5): `False`
      - `UIAutoresizeSubviews` (type 5): `False`
      - `UIAutoresizingMask` (type 0): `34`
      - `UIClearsContextBeforeDrawing` (type 4): `True`
      - `UIViewContentHuggingPriority` (type 10): `{'$ref': 25}`
      - `UIItems` (type 10): `{'$ref': 103}`
  - **UIView** (object 18)
    - class: `UIView`
    - frame: (0, 44, 320, 200)
    - raw UIBounds: (0, 0, 320, 200)
    - raw UICenter: (160, 144)
    - autoresizing mask: 34
    - background color: rgba(0.243137, 0.243137, 0.243137, 1)
    - hidden: not encoded
    - opaque: false
    - tag: not encoded
    - raw values:
      - `UIBounds` (type 8): `{'$data_hex': '0600000000000000000000a04300004843', '$floats': [0.0, 0.0, 320.0, 200.0]}`
      - `UICenter` (type 8): `{'$data_hex': '060000204300001043', '$floats': [160.0, 144.0]}`
      - `UISubviews` (type 10): `{'$ref': 14}`
      - `UIBackgroundColor` (type 10): `{'$ref': 105}`
      - `UIOpaque` (type 5): `False`
      - `UIAutoresizeSubviews` (type 5): `False`
      - `UIAutoresizingMask` (type 0): `34`
    - **MicMeterView** (object 120)
      - class: `MicMeterView`
      - encoded as: `UIClassSwapper` swapping `UIView`
      - frame: (20, 15, 140, 170)
      - raw UIBounds: (0, 0, 140, 170)
      - raw UICenter: (90, 100)
      - autoresizing mask: 36
      - background color: rgba(0, 0, 0, 0)
      - hidden: not encoded
      - opaque: not encoded
      - tag: not encoded
      - raw values:
        - `UIBounds` (type 8): `{'$data_hex': '06000000000000000000000c4300002a43', '$floats': [0.0, 0.0, 140.0, 170.0]}`
        - `UICenter` (type 8): `{'$data_hex': '060000b4420000c842', '$floats': [90.0, 100.0]}`
        - `UIBackgroundColor` (type 10): `{'$ref': 12}`
        - `UIAutoresizeSubviews` (type 5): `False`
        - `UIAutoresizingMask` (type 0): `36`
        - `UIContentMode` (type 0): `3`
        - `UIClassName` (type 10): `{'$ref': 61}`
        - `UIOriginalClassName` (type 10): `{'$ref': 92}`
    - **UILabel** (object 115)
      - class: `UILabel`
      - frame: (173, 47, 105, 21)
      - raw UIBounds: (0, 0, 105, 21)
      - raw UICenter: (225.5, 57.5)
      - autoresizing mask: 36
      - background color: not encoded
      - font: Helvetica 15pt
      - hidden: not encoded
      - opaque: not encoded
      - tag: not encoded
      - raw values:
        - `UIBounds` (type 8): `{'$data_hex': '0600000000000000000000d2420000a841', '$floats': [0.0, 0.0, 105.0, 21.0]}`
        - `UICenter` (type 8): `{'$data_hex': '060080614300006642', '$floats': [225.5, 57.5]}`
        - `UIUserInteractionDisabled` (type 5): `False`
        - `UIAutoresizeSubviews` (type 5): `False`
        - `UIAutoresizingMask` (type 0): `36`
        - `UIContentMode` (type 0): `7`
        - `UIClipsToBounds` (type 5): `False`
        - `UIText` (type 10): `{'$ref': 6}`
        - `UIFont` (type 10): `{'$ref': 52}`
        - `UITextColor` (type 10): `{'$ref': 23}`
        - `UIShadowOffset` (type 8): `{'$data_hex': '0600000000000080bf', '$floats': [0.0, -1.0]}`
    - **UILabel** (object 74)
      - class: `UILabel`
      - frame: (173, 76, 105, 21)
      - raw UIBounds: (0, 0, 105, 21)
      - raw UICenter: (225.5, 86.5)
      - autoresizing mask: 36
      - background color: not encoded
      - font: Helvetica-Bold 24pt
      - hidden: not encoded
      - opaque: not encoded
      - tag: not encoded
      - raw values:
        - `UIBounds` (type 8): `{'$data_hex': '0600000000000000000000d2420000a841', '$floats': [0.0, 0.0, 105.0, 21.0]}`
        - `UICenter` (type 8): `{'$data_hex': '06008061430000ad42', '$floats': [225.5, 86.5]}`
        - `UIUserInteractionDisabled` (type 5): `False`
        - `UIAutoresizeSubviews` (type 5): `False`
        - `UIAutoresizingMask` (type 0): `36`
        - `UIContentMode` (type 0): `7`
        - `UIClipsToBounds` (type 5): `False`
        - `UIText` (type 10): `{'$ref': 82}`
        - `UIFont` (type 10): `{'$ref': 59}`
        - `UITextColor` (type 10): `{'$ref': 23}`
        - `UIShadowOffset` (type 8): `{'$data_hex': '0600000000000080bf', '$floats': [0.0, -1.0]}`
    - **UIButton** (object 91)
      - class: `UIButton`
      - frame: (173, 116, 105, 37)
      - raw UIBounds: (0, 0, 105, 37)
      - raw UICenter: (225.5, 134.5)
      - autoresizing mask: 36
      - background color: not encoded
      - font: Helvetica-Bold 15pt
      - hidden: not encoded
      - opaque: not encoded
      - tag: not encoded
      - target/action: `pauseResumeAction:` from object 91 (UIButton) to object 64 (UIProxyObject), event mask 64
      - raw values:
        - `UIBounds` (type 8): `{'$data_hex': '0600000000000000000000d24200001442', '$floats': [0.0, 0.0, 105.0, 37.0]}`
        - `UICenter` (type 8): `{'$data_hex': '060080614300800643', '$floats': [225.5, 134.5]}`
        - `UIAutoresizeSubviews` (type 5): `False`
        - `UIAutoresizingMask` (type 0): `36`
        - `UIButtonStatefulContent` (type 10): `{'$ref': 1}`
        - `UIAdjustsImageWhenHighlighted` (type 5): `False`
        - `UIAdjustsImageWhenDisabled` (type 5): `False`
        - `UIFont` (type 10): `{'$ref': 67}`
        - `UITitleShadowOffset` (type 8): `{'$data_hex': '06000000000000803f', '$floats': [0.0, 1.0]}`
  - **UIView** (object 108)
    - class: `UIView`
    - frame: (0, 244, 320, 106)
    - raw UIBounds: (0, 0, 320, 106)
    - raw UICenter: (160, 297)
    - autoresizing mask: 10
    - background color: rgba(0, 0, 0, 0)
    - hidden: not encoded
    - opaque: not encoded
    - tag: not encoded
    - raw values:
      - `UIBounds` (type 8): `{'$data_hex': '0600000000000000000000a0430000d442', '$floats': [0.0, 0.0, 320.0, 106.0]}`
      - `UICenter` (type 8): `{'$data_hex': '060000204300809443', '$floats': [160.0, 297.0]}`
      - `UISubviews` (type 10): `{'$ref': 113}`
      - `UIBackgroundColor` (type 10): `{'$ref': 12}`
      - `UIAutoresizeSubviews` (type 5): `False`
      - `UIAutoresizingMask` (type 0): `10`
    - **UIPlaceHolderTextView** (object 93)
      - class: `UIPlaceHolderTextView`
      - encoded as: `UIClassSwapper` swapping `UITextView`
      - frame: (15, 10, 290, 91)
      - raw UIBounds: (0, 0, 290, 91)
      - raw UICenter: (160, 55.5)
      - autoresizing mask: 18
      - background color: rgba(0.94902, 0.94902, 0.94902, 1)
      - font: Helvetica 16pt
      - hidden: not encoded
      - opaque: false
      - tag: not encoded
      - outlet: `delegate` to object 64 (UIProxyObject)
      - raw values:
        - `UIBounds` (type 8): `{'$data_hex': '060000000000000000000091430000b642', '$floats': [0.0, 0.0, 290.0, 91.0]}`
        - `UICenter` (type 8): `{'$data_hex': '060000204300005e42', '$floats': [160.0, 55.5]}`
        - `UISubviews` (type 10): `{'$ref': 55}`
        - `UIBackgroundColor` (type 10): `{'$ref': 119}`
        - `UIOpaque` (type 5): `False`
        - `UIMultipleTouchEnabled` (type 5): `False`
        - `UIAutoresizeSubviews` (type 5): `False`
        - `UIAutoresizingMask` (type 0): `18`
        - `UIClipsToBounds` (type 5): `False`
        - `UIBouncesZoom` (type 5): `False`
        - `UIContentSize` (type 8): `{'$data_hex': '060000914300001042', '$floats': [290.0, 36.0]}`
        - `UIFont` (type 10): `{'$ref': 71}`
        - `UITextColor` (type 10): `{'$ref': 72}`
        - `UITextAlignment` (type 0): `0`
        - `UIClassName` (type 10): `{'$ref': 96}`
        - `UIOriginalClassName` (type 10): `{'$ref': 63}`
      - **UITextSelectionView** (object 104)
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
    - **UIButton** (object 121)
      - class: `UIButton`
      - frame: (272, 10, 37, 37)
      - raw UIBounds: (0, 0, 37, 37)
      - raw UICenter: (290.5, 28.5)
      - autoresizing mask: 33
      - background color: not encoded
      - font: Helvetica-Bold 15pt
      - hidden: not encoded
      - opaque: not encoded
      - tag: not encoded
      - target/action: `pauseResumeAction:` from object 121 (UIButton) to object 64 (UIProxyObject), event mask 64
      - raw values:
        - `UIBounds` (type 8): `{'$data_hex': '0600000000000000000000144200001442', '$floats': [0.0, 0.0, 37.0, 37.0]}`
        - `UICenter` (type 8): `{'$data_hex': '06004091430000e441', '$floats': [290.5, 28.5]}`
        - `UIAutoresizeSubviews` (type 5): `False`
        - `UIAutoresizingMask` (type 0): `33`
        - `UIButtonStatefulContent` (type 10): `{'$ref': 3}`
        - `UIAdjustsImageWhenHighlighted` (type 5): `False`
        - `UIAdjustsImageWhenDisabled` (type 5): `False`
        - `UIFont` (type 10): `{'$ref': 67}`
  - **UIRoundedRectButton** (object 50)
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
    - target/action: `setLocationAction:` from object 50 (UIRoundedRectButton) to object 64 (UIProxyObject), event mask 64
    - raw values:
      - `UIBounds` (type 8): `{'$data_hex': '06000000000000000000008c4300001442', '$floats': [0.0, 0.0, 280.0, 37.0]}`
      - `UICenter` (type 8): `{'$data_hex': '06000020430040bc43', '$floats': [160.0, 376.5]}`
      - `UIAutoresizeSubviews` (type 5): `False`
      - `UIAutoresizingMask` (type 0): `36`
      - `UIButtonStatefulContent` (type 10): `{'$ref': 90}`
      - `UIAdjustsImageWhenHighlighted` (type 5): `False`
      - `UIAdjustsImageWhenDisabled` (type 5): `False`
      - `UIButtonType` (type 0): `1`
      - `UIFont` (type 10): `{'$ref': 67}`
  - **UIRoundedRectButton** (object 13)
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
    - target/action: `setSpaceAction:` from object 13 (UIRoundedRectButton) to object 64 (UIProxyObject), event mask 64
    - raw values:
      - `UIBounds` (type 8): `{'$data_hex': '06000000000000000000008c4300001442', '$floats': [0.0, 0.0, 280.0, 37.0]}`
      - `UICenter` (type 8): `{'$data_hex': '060000204300c0d243', '$floats': [160.0, 421.5]}`
      - `UIAutoresizeSubviews` (type 5): `False`
      - `UIAutoresizingMask` (type 0): `36`
      - `UIButtonStatefulContent` (type 10): `{'$ref': 4}`
      - `UIAdjustsImageWhenHighlighted` (type 5): `False`
      - `UIAdjustsImageWhenDisabled` (type 5): `False`
      - `UIButtonType` (type 0): `1`
      - `UIFont` (type 10): `{'$ref': 67}`

- **PhoneNoteViewInputAccessory** (object 81)
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
  - outlet: `delegate` to object 64 (UIProxyObject)
  - raw values:
    - `UIBounds` (type 8): `{'$data_hex': '0600000000000000000000a04300003042', '$floats': [0.0, 0.0, 320.0, 44.0]}`
    - `UICenter` (type 8): `{'$data_hex': '06000020430000b041', '$floats': [160.0, 22.0]}`
    - `UIOpaque` (type 5): `False`
    - `UIAutoresizeSubviews` (type 5): `False`
    - `UIAutoresizingMask` (type 0): `10`
    - `UIClearsContextBeforeDrawing` (type 4): `True`
    - `UIViewContentHuggingPriority` (type 10): `{'$ref': 25}`
    - `UIItems` (type 10): `{'$ref': 11}`
    - `UIClassName` (type 10): `{'$ref': 21}`
    - `UIOriginalClassName` (type 10): `{'$ref': 76}`

- **UIBarButtonItem** (object 98)
  - class: `UIBarButtonItem`
  - target/action: `cancelAndDismissAction:` from object 98 (UIBarButtonItem) to object 64 (UIProxyObject), event mask not encoded
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
    - `UINibTopLevelObjectsKey` (type 10): `{'$ref': 56}`
    - `UINibObjectsKey` (type 10): `{'$ref': 7}`
    - `UINibConnectionsKey` (type 10): `{'$ref': 83}`
    - `UINibVisibleWindowsKey` (type 10): `{'$ref': 116}`
    - `UINibAccessibilityConfigurationsKey` (type 10): `{'$ref': 116}`
    - `UINibKeyValuePairsKey` (type 10): `{'$ref': 116}`

- **NSMutableDictionary** (object 1)
  - class: `NSMutableDictionary`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 24}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 77}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 15}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 44}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 36}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 33}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 45}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 118}`

- **UIRuntimeOutletConnection** (object 2)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 117}`
    - `UISource` (type 10): `{'$ref': 64}`
    - `UIDestination` (type 10): `{'$ref': 38}`

- **NSMutableDictionary** (object 3)
  - class: `NSMutableDictionary`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 24}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 28}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 15}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 122}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 36}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 111}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 45}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 65}`

- **NSMutableDictionary** (object 4)
  - class: `NSMutableDictionary`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 24}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 54}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 36}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 51}`

- **NSString** (object 5)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '7061757365526573756d65427574746f6e', '$text': 'pauseResumeButton'}`

- **NSMutableString** (object 6)
  - class: `NSMutableString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '5265636f7264696e67', '$text': 'Recording'}`

- **NSArray** (object 7)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 64}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 80}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 75}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 81}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 38}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 18}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 108}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 50}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 13}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 89}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 49}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 47}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 98}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 39}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 48}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 120}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 115}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 74}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 91}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 93}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 121}`

- **UIRuntimeOutletConnection** (object 8)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 26}`
    - `UISource` (type 10): `{'$ref': 64}`
    - `UIDestination` (type 10): `{'$ref': 81}`

- **UIRuntimeEventConnection** (object 9)
  - class: `UIRuntimeEventConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 88}`
    - `UISource` (type 10): `{'$ref': 47}`
    - `UIDestination` (type 10): `{'$ref': 64}`

- **NSString** (object 10)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '62746e5f70617573655f746578745f6c616e642e706e67', '$text': 'btn_pause_text_land.png'}`

- **NSArray** (object 11)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 89}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 49}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 47}`

- **UIColor** (object 12)
  - class: `UIColor`
  - raw values:
    - `UIColorComponentCount` (type 0): `4`
    - `UIRed` (type 6): `0.0`
    - `UIGreen` (type 6): `0.0`
    - `UIBlue` (type 6): `0.0`
    - `UIAlpha` (type 6): `0.0`
    - `NSRGB` (type 8): `{'$data_hex': '30203020302030', '$text': '0 0 0 0'}`
    - `NSColorSpace` (type 0): `2`

- **NSMutableArray** (object 14)
  - class: `NSMutableArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 120}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 115}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 74}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 91}`

- **NSNumber** (object 15)
  - class: `NSNumber`
  - raw values:
    - `NS.intval` (type 0): `4`

- **UIRuntimeEventConnection** (object 16)
  - class: `UIRuntimeEventConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 42}`
    - `UISource` (type 10): `{'$ref': 121}`
    - `UIDestination` (type 10): `{'$ref': 64}`
    - `UIEventMask` (type 0): `64`

- **UIRuntimeOutletConnection** (object 17)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 102}`
    - `UISource` (type 10): `{'$ref': 64}`
    - `UIDestination` (type 10): `{'$ref': 13}`

- **UIRuntimeEventConnection** (object 19)
  - class: `UIRuntimeEventConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 30}`
    - `UISource` (type 10): `{'$ref': 98}`
    - `UIDestination` (type 10): `{'$ref': 64}`

- **NSString** (object 20)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '6475726174696f6e4c6162656c', '$text': 'durationLabel'}`

- **NSString** (object 21)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '50686f6e654e6f746556696577496e7075744163636573736f7279', '$text': 'PhoneNoteViewInputAccessory'}`

- **NSString** (object 22)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '48656c7665746963612d426f6c64', '$text': 'Helvetica-Bold'}`

- **UIColor** (object 23)
  - class: `UIColor`
  - raw values:
    - `UIColorComponentCount` (type 0): `4`
    - `UIRed` (type 6): `1.0`
    - `UIGreen` (type 6): `1.0`
    - `UIBlue` (type 6): `1.0`
    - `UIAlpha` (type 6): `1.0`
    - `NSRGB` (type 8): `{'$data_hex': '3120312031', '$text': '1 1 1'}`
    - `NSColorSpace` (type 0): `2`

- **NSNumber** (object 24)
  - class: `NSNumber`
  - raw values:
    - `NS.intval` (type 0): `0`

- **NSString** (object 25)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '7b3235302c203235307d', '$text': '{250, 250}'}`

- **NSString** (object 26)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '746578744163636573736f727956696577', '$text': 'textAccessoryView'}`

- **NSString** (object 27)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '494246696c65734f776e6572', '$text': 'IBFilesOwner'}`

- **UIButtonContent** (object 28)
  - class: `UIButtonContent`
  - raw values:
    - `UIImage` (type 10): `{'$ref': 87}`
    - `UITitleColor` (type 10): `{'$ref': 72}`
    - `UIShadowColor` (type 10): `{'$ref': 29}`

- **UIColor** (object 29)
  - class: `UIColor`
  - raw values:
    - `UIColorComponentCount` (type 0): `4`
    - `UIRed` (type 6): `0.5`
    - `UIGreen` (type 6): `0.5`
    - `UIBlue` (type 6): `0.5`
    - `UIAlpha` (type 6): `1.0`
    - `NSRGB` (type 8): `{'$data_hex': '302e3520302e3520302e35', '$text': '0.5 0.5 0.5'}`
    - `NSColorSpace` (type 0): `2`

- **NSString** (object 30)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '63616e63656c416e644469736d697373416374696f6e3a', '$text': 'cancelAndDismissAction:'}`

- **UIRuntimeOutletConnection** (object 31)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 5}`
    - `UISource` (type 10): `{'$ref': 64}`
    - `UIDestination` (type 10): `{'$ref': 91}`

- **NSString** (object 32)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '636f6e74726f6c436f6e7461696e657256696577', '$text': 'controlContainerView'}`

- **UIButtonContent** (object 33)
  - class: `UIButtonContent`
  - raw values:
    - `UITitleColor` (type 10): `{'$ref': 79}`
    - `UIShadowColor` (type 10): `{'$ref': 72}`

- **UIButtonContent** (object 34)
  - class: `UIButtonContent`
  - raw values:
    - `UITitleColor` (type 10): `{'$ref': 23}`

- **UIRuntimeEventConnection** (object 35)
  - class: `UIRuntimeEventConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 70}`
    - `UISource` (type 10): `{'$ref': 50}`
    - `UIDestination` (type 10): `{'$ref': 64}`
    - `UIEventMask` (type 0): `64`

- **NSNumber** (object 36)
  - class: `NSNumber`
  - raw values:
    - `NS.intval` (type 0): `1`

- **NSMutableArray** (object 37)
  - class: `NSMutableArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 38}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 18}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 108}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 50}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 13}`

- **UIBarButtonItem** (object 39)
  - class: `UIBarButtonItem`
  - raw values:
    - `UIEnabled` (type 5): `False`
    - `UIIsSystemItem` (type 5): `False`
    - `UISystemItem` (type 0): `5`

- **NSString** (object 40)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '48656c766574696361', '$text': 'Helvetica'}`

- **UIRuntimeOutletConnection** (object 41)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 125}`
    - `UISource` (type 10): `{'$ref': 64}`
    - `UIDestination` (type 10): `{'$ref': 120}`

- **NSString** (object 42)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '7061757365526573756d65416374696f6e3a', '$text': 'pauseResumeAction:'}`

- **NSString** (object 43)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '76696577', '$text': 'view'}`

- **UIButtonContent** (object 44)
  - class: `UIButtonContent`
  - raw values:
    - `UITitleColor` (type 10): `{'$ref': 72}`

- **NSNumber** (object 45)
  - class: `NSNumber`
  - raw values:
    - `NS.intval` (type 0): `2`

- **NSString** (object 46)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '73617665416e644469736d697373416374696f6e3a', '$text': 'saveAndDismissAction:'}`

- **UIBarButtonItem** (object 49)
  - class: `UIBarButtonItem`
  - raw values:
    - `UIEnabled` (type 5): `False`
    - `UIIsSystemItem` (type 5): `False`
    - `UISystemItem` (type 0): `5`

- **UIButtonContent** (object 51)
  - class: `UIButtonContent`
  - raw values:
    - `UITitleColor` (type 10): `{'$ref': 23}`

- **UIFont** (object 52)
  - class: `UIFont`
  - raw values:
    - `UIFontName` (type 10): `{'$ref': 40}`
    - `UIFontPointSize` (type 7): `15.0`
    - `UIFontTraits` (type 0): `0`
    - `UISystemFont` (type 5): `False`
    - `NSName` (type 10): `{'$ref': 40}`
    - `NSSize` (type 7): `15.0`

- **UIRuntimeOutletConnection** (object 53)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 100}`
    - `UISource` (type 10): `{'$ref': 81}`
    - `UIDestination` (type 10): `{'$ref': 64}`

- **UIButtonContent** (object 54)
  - class: `UIButtonContent`
  - raw values:
    - `UITitle` (type 10): `{'$ref': 126}`
    - `UITitleColor` (type 10): `{'$ref': 124}`
    - `UIShadowColor` (type 10): `{'$ref': 29}`

- **NSMutableArray** (object 55)
  - class: `NSMutableArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 104}`

- **NSArray** (object 56)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 64}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 80}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 75}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 81}`

- **NSString** (object 57)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '7365745370616365416374696f6e3a', '$text': 'setSpaceAction:'}`

- **NSString** (object 58)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '7374617475734c6162656c', '$text': 'statusLabel'}`

- **UIFont** (object 59)
  - class: `UIFont`
  - raw values:
    - `UIFontName` (type 10): `{'$ref': 22}`
    - `UIFontPointSize` (type 7): `24.0`
    - `UIFontTraits` (type 0): `2`
    - `UISystemFont` (type 5): `False`
    - `NSName` (type 10): `{'$ref': 22}`
    - `NSSize` (type 7): `24.0`

- **UIRuntimeOutletConnection** (object 60)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 43}`
    - `UISource` (type 10): `{'$ref': 64}`
    - `UIDestination` (type 10): `{'$ref': 75}`

- **NSString** (object 61)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '4d69634d6574657256696577', '$text': 'MicMeterView'}`

- **UIButtonContent** (object 62)
  - class: `UIButtonContent`
  - raw values:
    - `UITitle` (type 10): `{'$ref': 107}`
    - `UITitleColor` (type 10): `{'$ref': 124}`
    - `UIShadowColor` (type 10): `{'$ref': 29}`

- **NSString** (object 63)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '55495465787456696577', '$text': 'UITextView'}`

- **UIButtonContent** (object 65)
  - class: `UIButtonContent`
  - raw values:
    - `UITitleColor` (type 10): `{'$ref': 99}`

- **NSString** (object 66)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '74657874436f6e7461696e657256696577', '$text': 'textContainerView'}`

- **UIFont** (object 67)
  - class: `UIFont`
  - raw values:
    - `UIFontName` (type 10): `{'$ref': 22}`
    - `UIFontPointSize` (type 7): `15.0`
    - `UIFontTraits` (type 0): `2`
    - `UISystemFont` (type 5): `False`
    - `NSName` (type 10): `{'$ref': 22}`
    - `NSSize` (type 7): `15.0`

- **UIRuntimeEventConnection** (object 68)
  - class: `UIRuntimeEventConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 42}`
    - `UISource` (type 10): `{'$ref': 91}`
    - `UIDestination` (type 10): `{'$ref': 64}`
    - `UIEventMask` (type 0): `64`

- **UIRuntimeOutletConnection** (object 69)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 66}`
    - `UISource` (type 10): `{'$ref': 64}`
    - `UIDestination` (type 10): `{'$ref': 108}`

- **NSString** (object 70)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '7365744c6f636174696f6e416374696f6e3a', '$text': 'setLocationAction:'}`

- **UIFont** (object 71)
  - class: `UIFont`
  - raw values:
    - `UIFontName` (type 10): `{'$ref': 40}`
    - `UIFontPointSize` (type 7): `16.0`
    - `UIFontTraits` (type 0): `0`
    - `UISystemFont` (type 5): `False`
    - `NSName` (type 10): `{'$ref': 40}`
    - `NSSize` (type 7): `16.0`

- **UIColor** (object 72)
  - class: `UIColor`
  - raw values:
    - `UIColorComponentCount` (type 0): `4`
    - `UIRed` (type 6): `0.3333333432674408`
    - `UIGreen` (type 6): `0.3333333432674408`
    - `UIBlue` (type 6): `0.3333333432674408`
    - `UIAlpha` (type 6): `1.0`
    - `NSRGB` (type 8): `{'$data_hex': '302e33333320302e33333320302e333333', '$text': '0.333 0.333 0.333'}`
    - `NSColorSpace` (type 0): `2`

- **UIRuntimeOutletConnection** (object 73)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 58}`
    - `UISource` (type 10): `{'$ref': 64}`
    - `UIDestination` (type 10): `{'$ref': 115}`

- **NSString** (object 76)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '5549546f6f6c626172', '$text': 'UIToolbar'}`

- **UIButtonContent** (object 77)
  - class: `UIButtonContent`
  - raw values:
    - `UITitle` (type 10): `{'$ref': 109}`
    - `UITitleColor` (type 10): `{'$ref': 72}`
    - `UIShadowColor` (type 10): `{'$ref': 79}`

- **NSString** (object 78)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '49424669727374526573706f6e646572', '$text': 'IBFirstResponder'}`

- **UIColor** (object 79)
  - class: `UIColor`
  - raw values:
    - `UIColorComponentCount` (type 0): `4`
    - `UIRed` (type 6): `0.8999999761581421`
    - `UIGreen` (type 6): `0.8999999761581421`
    - `UIBlue` (type 6): `0.8999999761581421`
    - `UIAlpha` (type 6): `1.0`
    - `NSRGB` (type 8): `{'$data_hex': '302e3920302e3920302e39', '$text': '0.9 0.9 0.9'}`
    - `NSColorSpace` (type 0): `2`

- **UIProxyObject** (object 80)
  - class: `UIProxyObject`
  - raw values:
    - `UIProxiedObjectIdentifier` (type 10): `{'$ref': 78}`

- **NSMutableString** (object 82)
  - class: `NSMutableString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '303a30303a3030', '$text': '0:00:00'}`

- **NSArray** (object 83)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 19}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 9}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 68}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 16}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 86}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 35}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 110}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 97}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 123}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 53}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 112}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 41}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 114}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 101}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 31}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 85}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 17}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 73}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 8}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 69}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 2}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 60}`

- **NSString** (object 84)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '6e6f74655465787456696577', '$text': 'noteTextView'}`

- **UIRuntimeOutletConnection** (object 85)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 94}`
    - `UISource` (type 10): `{'$ref': 64}`
    - `UIDestination` (type 10): `{'$ref': 50}`

- **UIRuntimeEventConnection** (object 86)
  - class: `UIRuntimeEventConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 46}`
    - `UISource` (type 10): `{'$ref': 48}`
    - `UIDestination` (type 10): `{'$ref': 64}`

- **UIImageNibPlaceholder** (object 87)
  - class: `UIImageNibPlaceholder`
  - raw values:
    - `UIImageWidth` (type 6): `1.0`
    - `UIImageHeight` (type 6): `1.0`
    - `UIResourceName` (type 10): `{'$ref': 10}`

- **NSString** (object 88)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '646f6e6545646974696e67416374696f6e3a', '$text': 'doneEditingAction:'}`

- **UIBarButtonItem** (object 89)
  - class: `UIBarButtonItem`
  - raw values:
    - `UIEnabled` (type 5): `False`
    - `UIIsSystemItem` (type 5): `False`
    - `UISystemItem` (type 0): `6`
    - `UIWidth` (type 6): `42.0`

- **NSMutableDictionary** (object 90)
  - class: `NSMutableDictionary`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 24}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 62}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 36}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 34}`

- **NSString** (object 92)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '554956696577', '$text': 'UIView'}`

- **NSString** (object 94)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '7365744c6f636174696f6e427574746f6e', '$text': 'setLocationButton'}`

- **UIColor** (object 95)
  - class: `UIColor`
  - raw values:
    - `UIColorComponentCount` (type 0): `4`
    - `UIRed` (type 6): `0.7463634014129639`
    - `UIGreen` (type 6): `0.7463411092758179`
    - `UIBlue` (type 6): `0.7463537454605103`
    - `UIAlpha` (type 6): `1.0`
    - `NSRGB` (type 8): `{'$data_hex': '302e37343620302e37343620302e373436', '$text': '0.746 0.746 0.746'}`
    - `NSColorSpace` (type 0): `2`

- **NSString** (object 96)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '5549506c616365486f6c6465725465787456696577', '$text': 'UIPlaceHolderTextView'}`

- **UIRuntimeOutletConnection** (object 97)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 32}`
    - `UISource` (type 10): `{'$ref': 64}`
    - `UIDestination` (type 10): `{'$ref': 18}`

- **UIColor** (object 99)
  - class: `UIColor`
  - raw values:
    - `UIColorComponentCount` (type 0): `4`
    - `UIRed` (type 6): `0.6666666865348816`
    - `UIGreen` (type 6): `0.6666666865348816`
    - `UIBlue` (type 6): `0.6666666865348816`
    - `UIAlpha` (type 6): `1.0`
    - `NSRGB` (type 8): `{'$data_hex': '302e36363720302e36363720302e363637', '$text': '0.667 0.667 0.667'}`
    - `NSColorSpace` (type 0): `2`

- **NSString** (object 100)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '64656c6567617465', '$text': 'delegate'}`

- **UIRuntimeOutletConnection** (object 101)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 84}`
    - `UISource` (type 10): `{'$ref': 64}`
    - `UIDestination` (type 10): `{'$ref': 93}`

- **NSString** (object 102)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '7365745370616365427574746f6e', '$text': 'setSpaceButton'}`

- **NSArray** (object 103)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 98}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 39}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 48}`

- **UIColor** (object 105)
  - class: `UIColor`
  - raw values:
    - `UIColorComponentCount` (type 0): `4`
    - `UIRed` (type 6): `0.24313725531101227`
    - `UIGreen` (type 6): `0.24313725531101227`
    - `UIBlue` (type 6): `0.24313725531101227`
    - `UIAlpha` (type 6): `1.0`
    - `NSRGB` (type 8): `{'$data_hex': '302e32343320302e32343320302e323433', '$text': '0.243 0.243 0.243'}`
    - `NSColorSpace` (type 0): `2`

- **NSString** (object 106)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '6d696e695061757365526573756d65427574746f6e', '$text': 'miniPauseResumeButton'}`

- **NSString** (object 107)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '536574204c6f636174696f6e', '$text': 'Set Location'}`

- **NSString** (object 109)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '526573756d65', '$text': 'Resume'}`

- **UIRuntimeEventConnection** (object 110)
  - class: `UIRuntimeEventConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 57}`
    - `UISource` (type 10): `{'$ref': 13}`
    - `UIDestination` (type 10): `{'$ref': 64}`
    - `UIEventMask` (type 0): `64`

- **UIButtonContent** (object 111)
  - class: `UIButtonContent`
  - raw values:
    - `UITitleColor` (type 10): `{'$ref': 23}`

- **UIRuntimeOutletConnection** (object 112)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 20}`
    - `UISource` (type 10): `{'$ref': 64}`
    - `UIDestination` (type 10): `{'$ref': 74}`

- **NSMutableArray** (object 113)
  - class: `NSMutableArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 93}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 121}`

- **UIRuntimeOutletConnection** (object 114)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 106}`
    - `UISource` (type 10): `{'$ref': 64}`
    - `UIDestination` (type 10): `{'$ref': 121}`

- **NSArray** (object 116)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`

- **NSString** (object 117)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '746f6f6c626172', '$text': 'toolbar'}`

- **UIButtonContent** (object 118)
  - class: `UIButtonContent`
  - raw values:
    - `UITitleColor` (type 10): `{'$ref': 99}`

- **UIColor** (object 119)
  - class: `UIColor`
  - raw values:
    - `UIColorComponentCount` (type 0): `4`
    - `UIRed` (type 6): `0.9490196108818054`
    - `UIGreen` (type 6): `0.9490196108818054`
    - `UIBlue` (type 6): `0.9490196108818054`
    - `UIAlpha` (type 6): `1.0`
    - `NSRGB` (type 8): `{'$data_hex': '302e39343920302e39343920302e393439', '$text': '0.949 0.949 0.949'}`
    - `NSColorSpace` (type 0): `2`

- **UIButtonContent** (object 122)
  - class: `UIButtonContent`
  - raw values:
    - `UITitleColor` (type 10): `{'$ref': 72}`

- **UIRuntimeOutletConnection** (object 123)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 100}`
    - `UISource` (type 10): `{'$ref': 93}`
    - `UIDestination` (type 10): `{'$ref': 64}`

- **UIColor** (object 124)
  - class: `UIColor`
  - raw values:
    - `UIColorComponentCount` (type 0): `4`
    - `UIRed` (type 6): `0.19607843458652496`
    - `UIGreen` (type 6): `0.30980393290519714`
    - `UIBlue` (type 6): `0.5215686559677124`
    - `UIAlpha` (type 6): `1.0`
    - `NSRGB` (type 8): `{'$data_hex': '302e31393620302e333120302e353232', '$text': '0.196 0.31 0.522'}`
    - `NSColorSpace` (type 0): `2`

- **NSString** (object 125)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '6d696356696577', '$text': 'micView'}`

- **NSString** (object 126)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '536574205370616365', '$text': 'Set Space'}`

