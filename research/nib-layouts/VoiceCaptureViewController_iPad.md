# VoiceCaptureViewController_iPad

Recovered layout for `VoiceCaptureViewController_iPad.nib`. Every interpreted value appears beside the
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

- **PadNoteViewInputAccessory** (object 18)
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
  - outlet: `delegate` to object 47 (UIProxyObject)
  - raw values:
    - `UIBounds` (type 8): `{'$data_hex': '0600000000000000000000a04300003042', '$floats': [0.0, 0.0, 320.0, 44.0]}`
    - `UICenter` (type 8): `{'$data_hex': '06000020430000b041', '$floats': [160.0, 22.0]}`
    - `UIOpaque` (type 5): `False`
    - `UIAutoresizeSubviews` (type 5): `False`
    - `UIAutoresizingMask` (type 0): `10`
    - `UIClearsContextBeforeDrawing` (type 4): `True`
    - `UIViewContentHuggingPriority` (type 10): `{'$ref': 21}`
    - `UIItems` (type 10): `{'$ref': 69}`
    - `UIClassName` (type 10): `{'$ref': 17}`
    - `UIOriginalClassName` (type 10): `{'$ref': 5}`

- **UIView** (object 39)
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
    - `UISubviews` (type 10): `{'$ref': 20}`
    - `UIBackgroundColor` (type 10): `{'$ref': 125}`
    - `UIOpaque` (type 5): `False`
    - `UIAutoresizeSubviews` (type 5): `False`
    - `UIAutoresizingMask` (type 0): `18`
  - **UIToolbar** (object 73)
    - class: `UIToolbar`
    - frame: (0, 0, 540, 44)
    - raw UIBounds: (0, 0, 540, 44)
    - raw UICenter: (270, 22)
    - autoresizing mask: 34
    - background color: rgba(0.746363, 0.746341, 0.746354, 1)
    - hidden: not encoded
    - opaque: false
    - tag: not encoded
    - raw values:
      - `UIBounds` (type 8): `{'$data_hex': '0600000000000000000000074400003042', '$floats': [0.0, 0.0, 540.0, 44.0]}`
      - `UICenter` (type 8): `{'$data_hex': '06000087430000b041', '$floats': [270.0, 22.0]}`
      - `UIBackgroundColor` (type 10): `{'$ref': 96}`
      - `UIOpaque` (type 5): `False`
      - `UIAutoresizeSubviews` (type 5): `False`
      - `UIAutoresizingMask` (type 0): `34`
      - `UIClearsContextBeforeDrawing` (type 4): `True`
      - `UIViewContentHuggingPriority` (type 10): `{'$ref': 21}`
      - `UIItems` (type 10): `{'$ref': 59}`
  - **UIView** (object 86)
    - class: `UIView`
    - frame: (0, 44, 540, 200)
    - raw UIBounds: (0, 0, 540, 200)
    - raw UICenter: (270, 144)
    - autoresizing mask: 34
    - background color: rgba(0.243137, 0.243137, 0.243137, 1)
    - hidden: not encoded
    - opaque: false
    - tag: not encoded
    - raw values:
      - `UIBounds` (type 8): `{'$data_hex': '0600000000000000000000074400004843', '$floats': [0.0, 0.0, 540.0, 200.0]}`
      - `UICenter` (type 8): `{'$data_hex': '060000874300001043', '$floats': [270.0, 144.0]}`
      - `UISubviews` (type 10): `{'$ref': 31}`
      - `UIBackgroundColor` (type 10): `{'$ref': 124}`
      - `UIOpaque` (type 5): `False`
      - `UIAutoresizeSubviews` (type 5): `False`
      - `UIAutoresizingMask` (type 0): `34`
    - **MicMeterView** (object 35)
      - class: `MicMeterView`
      - encoded as: `UIClassSwapper` swapping `UIView`
      - frame: (141, 15, 140, 170)
      - raw UIBounds: (0, 0, 140, 170)
      - raw UICenter: (211, 100)
      - autoresizing mask: 36
      - background color: rgba(0, 0, 0, 0)
      - hidden: not encoded
      - opaque: not encoded
      - tag: not encoded
      - raw values:
        - `UIBounds` (type 8): `{'$data_hex': '06000000000000000000000c4300002a43', '$floats': [0.0, 0.0, 140.0, 170.0]}`
        - `UICenter` (type 8): `{'$data_hex': '06000053430000c842', '$floats': [211.0, 100.0]}`
        - `UIBackgroundColor` (type 10): `{'$ref': 94}`
        - `UIAutoresizeSubviews` (type 5): `False`
        - `UIAutoresizingMask` (type 0): `36`
        - `UIContentMode` (type 0): `3`
        - `UIClassName` (type 10): `{'$ref': 26}`
        - `UIOriginalClassName` (type 10): `{'$ref': 93}`
    - **UILabel** (object 105)
      - class: `UILabel`
      - frame: (294, 47, 105, 21)
      - raw UIBounds: (0, 0, 105, 21)
      - raw UICenter: (346.5, 57.5)
      - autoresizing mask: 36
      - background color: not encoded
      - font: Helvetica 15pt
      - hidden: not encoded
      - opaque: not encoded
      - tag: not encoded
      - raw values:
        - `UIBounds` (type 8): `{'$data_hex': '0600000000000000000000d2420000a841', '$floats': [0.0, 0.0, 105.0, 21.0]}`
        - `UICenter` (type 8): `{'$data_hex': '060040ad4300006642', '$floats': [346.5, 57.5]}`
        - `UIUserInteractionDisabled` (type 5): `False`
        - `UIAutoresizeSubviews` (type 5): `False`
        - `UIAutoresizingMask` (type 0): `36`
        - `UIContentMode` (type 0): `7`
        - `UIClipsToBounds` (type 5): `False`
        - `UIText` (type 10): `{'$ref': 75}`
        - `UIFont` (type 10): `{'$ref': 44}`
        - `UITextColor` (type 10): `{'$ref': 71}`
        - `UIShadowOffset` (type 8): `{'$data_hex': '0600000000000080bf', '$floats': [0.0, -1.0]}`
    - **UILabel** (object 113)
      - class: `UILabel`
      - frame: (294, 76, 105, 21)
      - raw UIBounds: (0, 0, 105, 21)
      - raw UICenter: (346.5, 86.5)
      - autoresizing mask: 36
      - background color: not encoded
      - font: Helvetica-Bold 24pt
      - hidden: not encoded
      - opaque: not encoded
      - tag: not encoded
      - raw values:
        - `UIBounds` (type 8): `{'$data_hex': '0600000000000000000000d2420000a841', '$floats': [0.0, 0.0, 105.0, 21.0]}`
        - `UICenter` (type 8): `{'$data_hex': '060040ad430000ad42', '$floats': [346.5, 86.5]}`
        - `UIUserInteractionDisabled` (type 5): `False`
        - `UIAutoresizeSubviews` (type 5): `False`
        - `UIAutoresizingMask` (type 0): `36`
        - `UIContentMode` (type 0): `7`
        - `UIClipsToBounds` (type 5): `False`
        - `UIText` (type 10): `{'$ref': 3}`
        - `UIFont` (type 10): `{'$ref': 102}`
        - `UITextColor` (type 10): `{'$ref': 71}`
        - `UIShadowOffset` (type 8): `{'$data_hex': '0600000000000080bf', '$floats': [0.0, -1.0]}`
    - **UIButton** (object 110)
      - class: `UIButton`
      - frame: (294, 116, 105, 37)
      - raw UIBounds: (0, 0, 105, 37)
      - raw UICenter: (346.5, 134.5)
      - autoresizing mask: 36
      - background color: not encoded
      - font: Helvetica-Bold 15pt
      - hidden: not encoded
      - opaque: not encoded
      - tag: not encoded
      - target/action: `pauseResumeAction:` from object 110 (UIButton) to object 47 (UIProxyObject), event mask 64
      - raw values:
        - `UIBounds` (type 8): `{'$data_hex': '0600000000000000000000d24200001442', '$floats': [0.0, 0.0, 105.0, 37.0]}`
        - `UICenter` (type 8): `{'$data_hex': '060040ad4300800643', '$floats': [346.5, 134.5]}`
        - `UIAutoresizeSubviews` (type 5): `False`
        - `UIAutoresizingMask` (type 0): `36`
        - `UIButtonStatefulContent` (type 10): `{'$ref': 84}`
        - `UIAdjustsImageWhenHighlighted` (type 5): `False`
        - `UIAdjustsImageWhenDisabled` (type 5): `False`
        - `UIFont` (type 10): `{'$ref': 10}`
        - `UITitleShadowOffset` (type 8): `{'$data_hex': '06000000000000803f', '$floats': [0.0, 1.0]}`
  - **UIView** (object 41)
    - class: `UIView`
    - frame: (0, 384, 540, 106)
    - raw UIBounds: (0, 0, 540, 106)
    - raw UICenter: (270, 437)
    - autoresizing mask: 10
    - background color: rgba(0, 0, 0, 0)
    - hidden: not encoded
    - opaque: not encoded
    - tag: not encoded
    - raw values:
      - `UIBounds` (type 8): `{'$data_hex': '060000000000000000000007440000d442', '$floats': [0.0, 0.0, 540.0, 106.0]}`
      - `UICenter` (type 8): `{'$data_hex': '06000087430080da43', '$floats': [270.0, 437.0]}`
      - `UISubviews` (type 10): `{'$ref': 80}`
      - `UIBackgroundColor` (type 10): `{'$ref': 94}`
      - `UIAutoresizeSubviews` (type 5): `False`
      - `UIAutoresizingMask` (type 0): `10`
    - **UIPlaceHolderTextView** (object 68)
      - class: `UIPlaceHolderTextView`
      - encoded as: `UIClassSwapper` swapping `UITextView`
      - frame: (15, 10, 510, 91)
      - raw UIBounds: (0, 0, 510, 91)
      - raw UICenter: (270, 55.5)
      - autoresizing mask: 18
      - background color: rgba(0.94902, 0.94902, 0.94902, 1)
      - font: Helvetica 16pt
      - hidden: not encoded
      - opaque: false
      - tag: not encoded
      - outlet: `delegate` to object 47 (UIProxyObject)
      - raw values:
        - `UIBounds` (type 8): `{'$data_hex': '0600000000000000000000ff430000b642', '$floats': [0.0, 0.0, 510.0, 91.0]}`
        - `UICenter` (type 8): `{'$data_hex': '060000874300005e42', '$floats': [270.0, 55.5]}`
        - `UISubviews` (type 10): `{'$ref': 63}`
        - `UIBackgroundColor` (type 10): `{'$ref': 125}`
        - `UIOpaque` (type 5): `False`
        - `UIMultipleTouchEnabled` (type 5): `False`
        - `UIAutoresizeSubviews` (type 5): `False`
        - `UIAutoresizingMask` (type 0): `18`
        - `UIClipsToBounds` (type 5): `False`
        - `UIBouncesZoom` (type 5): `False`
        - `UIContentSize` (type 8): `{'$data_hex': '060000ff4300001042', '$floats': [510.0, 36.0]}`
        - `UIFont` (type 10): `{'$ref': 119}`
        - `UITextColor` (type 10): `{'$ref': 90}`
        - `UITextAlignment` (type 0): `0`
        - `UIClassName` (type 10): `{'$ref': 12}`
        - `UIOriginalClassName` (type 10): `{'$ref': 36}`
      - **UITextSelectionView** (object 121)
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
    - **UIButton** (object 122)
      - class: `UIButton`
      - frame: (492, 10, 37, 37)
      - raw UIBounds: (0, 0, 37, 37)
      - raw UICenter: (510.5, 28.5)
      - autoresizing mask: 33
      - background color: not encoded
      - font: Helvetica-Bold 15pt
      - hidden: not encoded
      - opaque: not encoded
      - tag: not encoded
      - target/action: `pauseResumeAction:` from object 122 (UIButton) to object 47 (UIProxyObject), event mask 64
      - raw values:
        - `UIBounds` (type 8): `{'$data_hex': '0600000000000000000000144200001442', '$floats': [0.0, 0.0, 37.0, 37.0]}`
        - `UICenter` (type 8): `{'$data_hex': '060040ff430000e441', '$floats': [510.5, 28.5]}`
        - `UIAutoresizeSubviews` (type 5): `False`
        - `UIAutoresizingMask` (type 0): `33`
        - `UIButtonStatefulContent` (type 10): `{'$ref': 99}`
        - `UIAdjustsImageWhenHighlighted` (type 5): `False`
        - `UIAdjustsImageWhenDisabled` (type 5): `False`
        - `UIFont` (type 10): `{'$ref': 10}`
  - **UIRoundedRectButton** (object 74)
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
    - target/action: `setLocationAction:` from object 74 (UIRoundedRectButton) to object 47 (UIProxyObject), event mask 64
    - raw values:
      - `UIBounds` (type 8): `{'$data_hex': '06000000000000000000008c4300001442', '$floats': [0.0, 0.0, 280.0, 37.0]}`
      - `UICenter` (type 8): `{'$data_hex': '06000020430040bc43', '$floats': [160.0, 376.5]}`
      - `UIAutoresizeSubviews` (type 5): `False`
      - `UIAutoresizingMask` (type 0): `36`
      - `UIButtonStatefulContent` (type 10): `{'$ref': 32}`
      - `UIAdjustsImageWhenHighlighted` (type 5): `False`
      - `UIAdjustsImageWhenDisabled` (type 5): `False`
      - `UIButtonType` (type 0): `1`
      - `UIFont` (type 10): `{'$ref': 10}`
  - **UIRoundedRectButton** (object 8)
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
    - target/action: `setSpaceAction:` from object 8 (UIRoundedRectButton) to object 47 (UIProxyObject), event mask 64
    - raw values:
      - `UIBounds` (type 8): `{'$data_hex': '06000000000000000000008c4300001442', '$floats': [0.0, 0.0, 280.0, 37.0]}`
      - `UICenter` (type 8): `{'$data_hex': '060000204300c0d243', '$floats': [160.0, 421.5]}`
      - `UIAutoresizeSubviews` (type 5): `False`
      - `UIAutoresizingMask` (type 0): `36`
      - `UIButtonStatefulContent` (type 10): `{'$ref': 65}`
      - `UIAdjustsImageWhenHighlighted` (type 5): `False`
      - `UIAdjustsImageWhenDisabled` (type 5): `False`
      - `UIButtonType` (type 0): `1`
      - `UIFont` (type 10): `{'$ref': 10}`

- **UIBarButtonItem** (object 43)
  - class: `UIBarButtonItem`
  - target/action: `saveAndDismissAction:` from object 43 (UIBarButtonItem) to object 47 (UIProxyObject), event mask not encoded
  - raw values:
    - `UIEnabled` (type 5): `False`
    - `UIIsSystemItem` (type 5): `False`
    - `UISystemItem` (type 0): `3`
    - `UIStyle` (type 0): `1`

- **UIBarButtonItem** (object 46)
  - class: `UIBarButtonItem`
  - target/action: `doneEditingAction:` from object 46 (UIBarButtonItem) to object 47 (UIProxyObject), event mask not encoded
  - raw values:
    - `UIEnabled` (type 5): `False`
    - `UIIsSystemItem` (type 5): `False`
    - `UISystemItem` (type 0): `0`
    - `UIStyle` (type 0): `2`

- **UIProxyObject** (object 47)
  - class: `UIProxyObject`
  - outlet: `miniPauseResumeButton` to object 122 (UIButton)
  - outlet: `textAccessoryView` to object 18 (PadNoteViewInputAccessory)
  - outlet: `view` to object 39 (UIView)
  - outlet: `setSpaceButton` to object 8 (UIRoundedRectButton)
  - outlet: `textContainerView` to object 41 (UIView)
  - outlet: `pauseResumeButton` to object 110 (UIButton)
  - outlet: `controlContainerView` to object 86 (UIView)
  - outlet: `durationLabel` to object 113 (UILabel)
  - outlet: `statusLabel` to object 105 (UILabel)
  - outlet: `toolbar` to object 73 (UIToolbar)
  - outlet: `setLocationButton` to object 74 (UIRoundedRectButton)
  - outlet: `noteTextView` to object 68 (UIPlaceHolderTextView)
  - outlet: `micView` to object 35 (MicMeterView)
  - target/action: `pauseResumeAction:` from object 110 (UIButton) to object 47 (UIProxyObject), event mask 64
  - target/action: `saveAndDismissAction:` from object 43 (UIBarButtonItem) to object 47 (UIProxyObject), event mask not encoded
  - target/action: `setSpaceAction:` from object 8 (UIRoundedRectButton) to object 47 (UIProxyObject), event mask 64
  - target/action: `doneEditingAction:` from object 46 (UIBarButtonItem) to object 47 (UIProxyObject), event mask not encoded
  - target/action: `pauseResumeAction:` from object 122 (UIButton) to object 47 (UIProxyObject), event mask 64
  - target/action: `cancelAndDismissAction:` from object 100 (UIBarButtonItem) to object 47 (UIProxyObject), event mask not encoded
  - target/action: `setLocationAction:` from object 74 (UIRoundedRectButton) to object 47 (UIProxyObject), event mask 64
  - raw values:
    - `UIProxiedObjectIdentifier` (type 10): `{'$ref': 56}`

- **UIBarButtonItem** (object 100)
  - class: `UIBarButtonItem`
  - target/action: `cancelAndDismissAction:` from object 100 (UIBarButtonItem) to object 47 (UIProxyObject), event mask not encoded
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
    - `UINibTopLevelObjectsKey` (type 10): `{'$ref': 54}`
    - `UINibObjectsKey` (type 10): `{'$ref': 25}`
    - `UINibConnectionsKey` (type 10): `{'$ref': 87}`
    - `UINibVisibleWindowsKey` (type 10): `{'$ref': 30}`
    - `UINibAccessibilityConfigurationsKey` (type 10): `{'$ref': 30}`
    - `UINibKeyValuePairsKey` (type 10): `{'$ref': 30}`

- **NSString** (object 1)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '64656c6567617465', '$text': 'delegate'}`

- **NSString** (object 2)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '48656c766574696361', '$text': 'Helvetica'}`

- **NSMutableString** (object 3)
  - class: `NSMutableString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '303a30303a3030', '$text': '0:00:00'}`

- **UIButtonContent** (object 4)
  - class: `UIButtonContent`
  - raw values:
    - `UITitleColor` (type 10): `{'$ref': 112}`

- **NSString** (object 5)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '5549546f6f6c626172', '$text': 'UIToolbar'}`

- **UIRuntimeOutletConnection** (object 6)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 1}`
    - `UISource` (type 10): `{'$ref': 18}`
    - `UIDestination` (type 10): `{'$ref': 47}`

- **UIRuntimeOutletConnection** (object 7)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 120}`
    - `UISource` (type 10): `{'$ref': 47}`
    - `UIDestination` (type 10): `{'$ref': 122}`

- **NSString** (object 9)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '7365745370616365427574746f6e', '$text': 'setSpaceButton'}`

- **UIFont** (object 10)
  - class: `UIFont`
  - raw values:
    - `UIFontName` (type 10): `{'$ref': 109}`
    - `UIFontPointSize` (type 7): `15.0`
    - `UIFontTraits` (type 0): `2`
    - `UISystemFont` (type 5): `False`
    - `NSName` (type 10): `{'$ref': 109}`
    - `NSSize` (type 7): `15.0`

- **UIRuntimeOutletConnection** (object 11)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 78}`
    - `UISource` (type 10): `{'$ref': 47}`
    - `UIDestination` (type 10): `{'$ref': 18}`

- **NSString** (object 12)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '5549506c616365486f6c6465725465787456696577', '$text': 'UIPlaceHolderTextView'}`

- **UIRuntimeOutletConnection** (object 13)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 57}`
    - `UISource` (type 10): `{'$ref': 47}`
    - `UIDestination` (type 10): `{'$ref': 39}`

- **UIButtonContent** (object 14)
  - class: `UIButtonContent`
  - raw values:
    - `UITitleColor` (type 10): `{'$ref': 71}`

- **NSString** (object 15)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '49424669727374526573706f6e646572', '$text': 'IBFirstResponder'}`

- **UIRuntimeEventConnection** (object 16)
  - class: `UIRuntimeEventConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 38}`
    - `UISource` (type 10): `{'$ref': 110}`
    - `UIDestination` (type 10): `{'$ref': 47}`
    - `UIEventMask` (type 0): `64`

- **NSString** (object 17)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '5061644e6f746556696577496e7075744163636573736f7279', '$text': 'PadNoteViewInputAccessory'}`

- **NSString** (object 19)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '746f6f6c626172', '$text': 'toolbar'}`

- **NSMutableArray** (object 20)
  - class: `NSMutableArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 73}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 86}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 41}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 74}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 8}`

- **NSString** (object 21)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '7b3235302c203235307d', '$text': '{250, 250}'}`

- **UIButtonContent** (object 22)
  - class: `UIButtonContent`
  - raw values:
    - `UITitle` (type 10): `{'$ref': 85}`
    - `UITitleColor` (type 10): `{'$ref': 116}`
    - `UIShadowColor` (type 10): `{'$ref': 88}`

- **UIRuntimeOutletConnection** (object 23)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 9}`
    - `UISource` (type 10): `{'$ref': 47}`
    - `UIDestination` (type 10): `{'$ref': 8}`

- **UIImageNibPlaceholder** (object 24)
  - class: `UIImageNibPlaceholder`
  - raw values:
    - `UIImageWidth` (type 6): `1.0`
    - `UIImageHeight` (type 6): `1.0`
    - `UIResourceName` (type 10): `{'$ref': 114}`

- **NSArray** (object 25)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 47}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 60}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 39}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 18}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 73}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 86}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 41}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 74}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 8}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 67}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 64}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 46}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 100}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 27}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 43}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 35}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 105}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 113}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 110}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 68}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 122}`

- **NSString** (object 26)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '4d69634d6574657256696577', '$text': 'MicMeterView'}`

- **UIBarButtonItem** (object 27)
  - class: `UIBarButtonItem`
  - raw values:
    - `UIEnabled` (type 5): `False`
    - `UIIsSystemItem` (type 5): `False`
    - `UISystemItem` (type 0): `5`

- **UIRuntimeOutletConnection** (object 28)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 111}`
    - `UISource` (type 10): `{'$ref': 47}`
    - `UIDestination` (type 10): `{'$ref': 41}`

- **NSString** (object 29)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '63616e63656c416e644469736d697373416374696f6e3a', '$text': 'cancelAndDismissAction:'}`

- **NSArray** (object 30)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`

- **NSMutableArray** (object 31)
  - class: `NSMutableArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 35}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 105}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 113}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 110}`

- **NSMutableDictionary** (object 32)
  - class: `NSMutableDictionary`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 62}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 22}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 51}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 14}`

- **NSString** (object 33)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '6e6f74655465787456696577', '$text': 'noteTextView'}`

- **NSString** (object 34)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '7365745370616365416374696f6e3a', '$text': 'setSpaceAction:'}`

- **NSString** (object 36)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '55495465787456696577', '$text': 'UITextView'}`

- **UIRuntimeEventConnection** (object 37)
  - class: `UIRuntimeEventConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 92}`
    - `UISource` (type 10): `{'$ref': 43}`
    - `UIDestination` (type 10): `{'$ref': 47}`

- **NSString** (object 38)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '7061757365526573756d65416374696f6e3a', '$text': 'pauseResumeAction:'}`

- **UIButtonContent** (object 40)
  - class: `UIButtonContent`
  - raw values:
    - `UITitleColor` (type 10): `{'$ref': 71}`

- **UIRuntimeOutletConnection** (object 42)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 70}`
    - `UISource` (type 10): `{'$ref': 47}`
    - `UIDestination` (type 10): `{'$ref': 110}`

- **UIFont** (object 44)
  - class: `UIFont`
  - raw values:
    - `UIFontName` (type 10): `{'$ref': 2}`
    - `UIFontPointSize` (type 7): `15.0`
    - `UIFontTraits` (type 0): `0`
    - `UISystemFont` (type 5): `False`
    - `NSName` (type 10): `{'$ref': 2}`
    - `NSSize` (type 7): `15.0`

- **NSString** (object 45)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '7374617475734c6162656c', '$text': 'statusLabel'}`

- **UIButtonContent** (object 48)
  - class: `UIButtonContent`
  - raw values:
    - `UITitleColor` (type 10): `{'$ref': 90}`

- **UIButtonContent** (object 49)
  - class: `UIButtonContent`
  - raw values:
    - `UITitleColor` (type 10): `{'$ref': 101}`
    - `UIShadowColor` (type 10): `{'$ref': 90}`

- **UIRuntimeOutletConnection** (object 50)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 72}`
    - `UISource` (type 10): `{'$ref': 47}`
    - `UIDestination` (type 10): `{'$ref': 86}`

- **NSNumber** (object 51)
  - class: `NSNumber`
  - raw values:
    - `NS.intval` (type 0): `1`

- **NSString** (object 52)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '6475726174696f6e4c6162656c', '$text': 'durationLabel'}`

- **UIRuntimeEventConnection** (object 53)
  - class: `UIRuntimeEventConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 34}`
    - `UISource` (type 10): `{'$ref': 8}`
    - `UIDestination` (type 10): `{'$ref': 47}`
    - `UIEventMask` (type 0): `64`

- **NSArray** (object 54)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 47}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 60}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 39}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 18}`

- **UIButtonContent** (object 55)
  - class: `UIButtonContent`
  - raw values:
    - `UIImage` (type 10): `{'$ref': 24}`
    - `UITitleColor` (type 10): `{'$ref': 90}`
    - `UIShadowColor` (type 10): `{'$ref': 88}`

- **NSString** (object 56)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '494246696c65734f776e6572', '$text': 'IBFilesOwner'}`

- **NSString** (object 57)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '76696577', '$text': 'view'}`

- **NSNumber** (object 58)
  - class: `NSNumber`
  - raw values:
    - `NS.intval` (type 0): `2`

- **NSArray** (object 59)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 100}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 27}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 43}`

- **UIProxyObject** (object 60)
  - class: `UIProxyObject`
  - raw values:
    - `UIProxiedObjectIdentifier` (type 10): `{'$ref': 15}`

- **UIButtonContent** (object 61)
  - class: `UIButtonContent`
  - raw values:
    - `UITitleColor` (type 10): `{'$ref': 90}`

- **NSNumber** (object 62)
  - class: `NSNumber`
  - raw values:
    - `NS.intval` (type 0): `0`

- **NSMutableArray** (object 63)
  - class: `NSMutableArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 121}`

- **UIBarButtonItem** (object 64)
  - class: `UIBarButtonItem`
  - raw values:
    - `UIEnabled` (type 5): `False`
    - `UIIsSystemItem` (type 5): `False`
    - `UISystemItem` (type 0): `5`

- **NSMutableDictionary** (object 65)
  - class: `NSMutableDictionary`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 62}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 81}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 51}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 77}`

- **UIRuntimeOutletConnection** (object 66)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 52}`
    - `UISource` (type 10): `{'$ref': 47}`
    - `UIDestination` (type 10): `{'$ref': 113}`

- **UIBarButtonItem** (object 67)
  - class: `UIBarButtonItem`
  - raw values:
    - `UIEnabled` (type 5): `False`
    - `UIIsSystemItem` (type 5): `False`
    - `UISystemItem` (type 0): `6`
    - `UIWidth` (type 6): `42.0`

- **NSArray** (object 69)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 67}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 64}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 46}`

- **NSString** (object 70)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '7061757365526573756d65427574746f6e', '$text': 'pauseResumeButton'}`

- **UIColor** (object 71)
  - class: `UIColor`
  - raw values:
    - `UIColorComponentCount` (type 0): `4`
    - `UIRed` (type 6): `1.0`
    - `UIGreen` (type 6): `1.0`
    - `UIBlue` (type 6): `1.0`
    - `UIAlpha` (type 6): `1.0`
    - `NSRGB` (type 8): `{'$data_hex': '3120312031', '$text': '1 1 1'}`
    - `NSColorSpace` (type 0): `2`

- **NSString** (object 72)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '636f6e74726f6c436f6e7461696e657256696577', '$text': 'controlContainerView'}`

- **NSMutableString** (object 75)
  - class: `NSMutableString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '5265636f7264696e67', '$text': 'Recording'}`

- **UIRuntimeOutletConnection** (object 76)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 1}`
    - `UISource` (type 10): `{'$ref': 68}`
    - `UIDestination` (type 10): `{'$ref': 47}`

- **UIButtonContent** (object 77)
  - class: `UIButtonContent`
  - raw values:
    - `UITitleColor` (type 10): `{'$ref': 71}`

- **NSString** (object 78)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '746578744163636573736f727956696577', '$text': 'textAccessoryView'}`

- **UIRuntimeEventConnection** (object 79)
  - class: `UIRuntimeEventConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 115}`
    - `UISource` (type 10): `{'$ref': 46}`
    - `UIDestination` (type 10): `{'$ref': 47}`

- **NSMutableArray** (object 80)
  - class: `NSMutableArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 68}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 122}`

- **UIButtonContent** (object 81)
  - class: `UIButtonContent`
  - raw values:
    - `UITitle` (type 10): `{'$ref': 103}`
    - `UITitleColor` (type 10): `{'$ref': 116}`
    - `UIShadowColor` (type 10): `{'$ref': 88}`

- **UIRuntimeOutletConnection** (object 82)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 45}`
    - `UISource` (type 10): `{'$ref': 47}`
    - `UIDestination` (type 10): `{'$ref': 105}`

- **UIRuntimeOutletConnection** (object 83)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 19}`
    - `UISource` (type 10): `{'$ref': 47}`
    - `UIDestination` (type 10): `{'$ref': 73}`

- **NSMutableDictionary** (object 84)
  - class: `NSMutableDictionary`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 62}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 98}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 126}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 61}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 51}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 49}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 58}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 4}`

- **NSString** (object 85)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '536574204c6f636174696f6e', '$text': 'Set Location'}`

- **NSArray** (object 87)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 95}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 79}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 16}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 91}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 37}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 108}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 53}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 50}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 76}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 6}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 66}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 118}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 7}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 107}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 42}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 97}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 23}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 82}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 11}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 28}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 83}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 13}`

- **UIColor** (object 88)
  - class: `UIColor`
  - raw values:
    - `UIColorComponentCount` (type 0): `4`
    - `UIRed` (type 6): `0.5`
    - `UIGreen` (type 6): `0.5`
    - `UIBlue` (type 6): `0.5`
    - `UIAlpha` (type 6): `1.0`
    - `NSRGB` (type 8): `{'$data_hex': '302e3520302e3520302e35', '$text': '0.5 0.5 0.5'}`
    - `NSColorSpace` (type 0): `2`

- **NSString** (object 89)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '6d696356696577', '$text': 'micView'}`

- **UIColor** (object 90)
  - class: `UIColor`
  - raw values:
    - `UIColorComponentCount` (type 0): `4`
    - `UIRed` (type 6): `0.3333333432674408`
    - `UIGreen` (type 6): `0.3333333432674408`
    - `UIBlue` (type 6): `0.3333333432674408`
    - `UIAlpha` (type 6): `1.0`
    - `NSRGB` (type 8): `{'$data_hex': '302e33333320302e33333320302e333333', '$text': '0.333 0.333 0.333'}`
    - `NSColorSpace` (type 0): `2`

- **UIRuntimeEventConnection** (object 91)
  - class: `UIRuntimeEventConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 38}`
    - `UISource` (type 10): `{'$ref': 122}`
    - `UIDestination` (type 10): `{'$ref': 47}`
    - `UIEventMask` (type 0): `64`

- **NSString** (object 92)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '73617665416e644469736d697373416374696f6e3a', '$text': 'saveAndDismissAction:'}`

- **NSString** (object 93)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '554956696577', '$text': 'UIView'}`

- **UIColor** (object 94)
  - class: `UIColor`
  - raw values:
    - `UIColorComponentCount` (type 0): `4`
    - `UIRed` (type 6): `0.0`
    - `UIGreen` (type 6): `0.0`
    - `UIBlue` (type 6): `0.0`
    - `UIAlpha` (type 6): `0.0`
    - `NSRGB` (type 8): `{'$data_hex': '30203020302030', '$text': '0 0 0 0'}`
    - `NSColorSpace` (type 0): `2`

- **UIRuntimeEventConnection** (object 95)
  - class: `UIRuntimeEventConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 29}`
    - `UISource` (type 10): `{'$ref': 100}`
    - `UIDestination` (type 10): `{'$ref': 47}`

- **UIColor** (object 96)
  - class: `UIColor`
  - raw values:
    - `UIColorComponentCount` (type 0): `4`
    - `UIRed` (type 6): `0.7463634014129639`
    - `UIGreen` (type 6): `0.7463411092758179`
    - `UIBlue` (type 6): `0.7463537454605103`
    - `UIAlpha` (type 6): `1.0`
    - `NSRGB` (type 8): `{'$data_hex': '302e37343620302e37343620302e373436', '$text': '0.746 0.746 0.746'}`
    - `NSColorSpace` (type 0): `2`

- **UIRuntimeOutletConnection** (object 97)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 104}`
    - `UISource` (type 10): `{'$ref': 47}`
    - `UIDestination` (type 10): `{'$ref': 74}`

- **UIButtonContent** (object 98)
  - class: `UIButtonContent`
  - raw values:
    - `UITitle` (type 10): `{'$ref': 106}`
    - `UITitleColor` (type 10): `{'$ref': 90}`
    - `UIShadowColor` (type 10): `{'$ref': 101}`

- **NSMutableDictionary** (object 99)
  - class: `NSMutableDictionary`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 62}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 55}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 126}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 48}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 51}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 40}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 58}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 117}`

- **UIColor** (object 101)
  - class: `UIColor`
  - raw values:
    - `UIColorComponentCount` (type 0): `4`
    - `UIRed` (type 6): `0.8999999761581421`
    - `UIGreen` (type 6): `0.8999999761581421`
    - `UIBlue` (type 6): `0.8999999761581421`
    - `UIAlpha` (type 6): `1.0`
    - `NSRGB` (type 8): `{'$data_hex': '302e3920302e3920302e39', '$text': '0.9 0.9 0.9'}`
    - `NSColorSpace` (type 0): `2`

- **UIFont** (object 102)
  - class: `UIFont`
  - raw values:
    - `UIFontName` (type 10): `{'$ref': 109}`
    - `UIFontPointSize` (type 7): `24.0`
    - `UIFontTraits` (type 0): `2`
    - `UISystemFont` (type 5): `False`
    - `NSName` (type 10): `{'$ref': 109}`
    - `NSSize` (type 7): `24.0`

- **NSString** (object 103)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '536574205370616365', '$text': 'Set Space'}`

- **NSString** (object 104)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '7365744c6f636174696f6e427574746f6e', '$text': 'setLocationButton'}`

- **NSString** (object 106)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '526573756d65', '$text': 'Resume'}`

- **UIRuntimeOutletConnection** (object 107)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 33}`
    - `UISource` (type 10): `{'$ref': 47}`
    - `UIDestination` (type 10): `{'$ref': 68}`

- **UIRuntimeEventConnection** (object 108)
  - class: `UIRuntimeEventConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 123}`
    - `UISource` (type 10): `{'$ref': 74}`
    - `UIDestination` (type 10): `{'$ref': 47}`
    - `UIEventMask` (type 0): `64`

- **NSString** (object 109)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '48656c7665746963612d426f6c64', '$text': 'Helvetica-Bold'}`

- **NSString** (object 111)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '74657874436f6e7461696e657256696577', '$text': 'textContainerView'}`

- **UIColor** (object 112)
  - class: `UIColor`
  - raw values:
    - `UIColorComponentCount` (type 0): `4`
    - `UIRed` (type 6): `0.6666666865348816`
    - `UIGreen` (type 6): `0.6666666865348816`
    - `UIBlue` (type 6): `0.6666666865348816`
    - `UIAlpha` (type 6): `1.0`
    - `NSRGB` (type 8): `{'$data_hex': '302e36363720302e36363720302e363637', '$text': '0.667 0.667 0.667'}`
    - `NSColorSpace` (type 0): `2`

- **NSString** (object 114)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '62746e5f70617573655f746578745f6c616e642e706e67', '$text': 'btn_pause_text_land.png'}`

- **NSString** (object 115)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '646f6e6545646974696e67416374696f6e3a', '$text': 'doneEditingAction:'}`

- **UIColor** (object 116)
  - class: `UIColor`
  - raw values:
    - `UIColorComponentCount` (type 0): `4`
    - `UIRed` (type 6): `0.19607843458652496`
    - `UIGreen` (type 6): `0.30980393290519714`
    - `UIBlue` (type 6): `0.5215686559677124`
    - `UIAlpha` (type 6): `1.0`
    - `NSRGB` (type 8): `{'$data_hex': '302e31393620302e333120302e353232', '$text': '0.196 0.31 0.522'}`
    - `NSColorSpace` (type 0): `2`

- **UIButtonContent** (object 117)
  - class: `UIButtonContent`
  - raw values:
    - `UITitleColor` (type 10): `{'$ref': 112}`

- **UIRuntimeOutletConnection** (object 118)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 89}`
    - `UISource` (type 10): `{'$ref': 47}`
    - `UIDestination` (type 10): `{'$ref': 35}`

- **UIFont** (object 119)
  - class: `UIFont`
  - raw values:
    - `UIFontName` (type 10): `{'$ref': 2}`
    - `UIFontPointSize` (type 7): `16.0`
    - `UIFontTraits` (type 0): `0`
    - `UISystemFont` (type 5): `False`
    - `NSName` (type 10): `{'$ref': 2}`
    - `NSSize` (type 7): `16.0`

- **NSString** (object 120)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '6d696e695061757365526573756d65427574746f6e', '$text': 'miniPauseResumeButton'}`

- **NSString** (object 123)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '7365744c6f636174696f6e416374696f6e3a', '$text': 'setLocationAction:'}`

- **UIColor** (object 124)
  - class: `UIColor`
  - raw values:
    - `UIColorComponentCount` (type 0): `4`
    - `UIRed` (type 6): `0.24313725531101227`
    - `UIGreen` (type 6): `0.24313725531101227`
    - `UIBlue` (type 6): `0.24313725531101227`
    - `UIAlpha` (type 6): `1.0`
    - `NSRGB` (type 8): `{'$data_hex': '302e32343320302e32343320302e323433', '$text': '0.243 0.243 0.243'}`
    - `NSColorSpace` (type 0): `2`

- **UIColor** (object 125)
  - class: `UIColor`
  - raw values:
    - `UIColorComponentCount` (type 0): `4`
    - `UIRed` (type 6): `0.9490196108818054`
    - `UIGreen` (type 6): `0.9490196108818054`
    - `UIBlue` (type 6): `0.9490196108818054`
    - `UIAlpha` (type 6): `1.0`
    - `NSRGB` (type 8): `{'$data_hex': '302e39343920302e39343920302e393439', '$text': '0.949 0.949 0.949'}`
    - `NSColorSpace` (type 0): `2`

- **NSNumber** (object 126)
  - class: `NSNumber`
  - raw values:
    - `NS.intval` (type 0): `4`

