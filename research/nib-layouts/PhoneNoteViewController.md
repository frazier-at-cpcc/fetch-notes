# PhoneNoteViewController

Recovered layout for `PhoneNoteViewController.nib`. Every interpreted value appears beside the
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

- **PhoneNoteViewInputAccessory** (object 7)
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
  - outlet: `fixedSpaceItem` to object 52 (UIBarButtonItem)
  - outlet: `camAttachItem` to object 34 (UIBarButtonItem)
  - outlet: `delegate` to object 21 (UIProxyObject)
  - outlet: `micAttachItem` to object 38 (UIBarButtonItem)
  - raw values:
    - `UIBounds` (type 8): `{'$data_hex': '0600000000000000000000a04300003042', '$floats': [0.0, 0.0, 320.0, 44.0]}`
    - `UICenter` (type 8): `{'$data_hex': '06000020430000b041', '$floats': [160.0, 22.0]}`
    - `UIOpaque` (type 5): `False`
    - `UIAutoresizeSubviews` (type 5): `False`
    - `UIAutoresizingMask` (type 0): `10`
    - `UIClearsContextBeforeDrawing` (type 4): `True`
    - `UIViewContentHuggingPriority` (type 10): `{'$ref': 42}`
    - `UIItems` (type 10): `{'$ref': 22}`
    - `UIClassName` (type 10): `{'$ref': 17}`
    - `UIOriginalClassName` (type 10): `{'$ref': 27}`

- **UIBarButtonItem** (object 14)
  - class: `UIBarButtonItem`
  - target/action: `stopEditing:` from object 14 (UIBarButtonItem) to object 21 (UIProxyObject), event mask not encoded
  - raw values:
    - `UIEnabled` (type 5): `False`
    - `UIIsSystemItem` (type 5): `False`
    - `UISystemItem` (type 0): `0`
    - `UIStyle` (type 0): `2`

- **UIProxyObject** (object 21)
  - class: `UIProxyObject`
  - outlet: `contentView` to object 37 (PhoneTouchToEditTextView)
  - outlet: `view` to object 33 (UIView)
  - outlet: `blockerView` to object 15 (UIView)
  - outlet: `inputAccessoryToolbar` to object 7 (PhoneNoteViewInputAccessory)
  - target/action: `attachPhoto:` from object 34 (UIBarButtonItem) to object 21 (UIProxyObject), event mask not encoded
  - target/action: `stopEditing:` from object 14 (UIBarButtonItem) to object 21 (UIProxyObject), event mask not encoded
  - target/action: `attachVoice:` from object 38 (UIBarButtonItem) to object 21 (UIProxyObject), event mask not encoded
  - raw values:
    - `UIProxiedObjectIdentifier` (type 10): `{'$ref': 9}`

- **UIView** (object 33)
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
    - `UISubviews` (type 10): `{'$ref': 40}`
    - `UIBackgroundColor` (type 10): `{'$ref': 36}`
    - `UIOpaque` (type 5): `False`
    - `UIAutoresizeSubviews` (type 5): `False`
    - `UIAutoresizingMask` (type 0): `18`
  - **PhoneTouchToEditTextView** (object 37)
    - class: `PhoneTouchToEditTextView`
    - encoded as: `UIClassSwapper` swapping `UIView`
    - frame: (0, 0, 320, 416)
    - raw UIBounds: (0, 0, 320, 416)
    - raw UICenter: (160, 208)
    - autoresizing mask: 18
    - background color: rgba(1, 1, 1, 1)
    - hidden: not encoded
    - opaque: false
    - tag: not encoded
    - outlet: `delegate` to object 21 (UIProxyObject)
    - raw values:
      - `UIBounds` (type 8): `{'$data_hex': '0600000000000000000000a0430000d043', '$floats': [0.0, 0.0, 320.0, 416.0]}`
      - `UICenter` (type 8): `{'$data_hex': '060000204300005043', '$floats': [160.0, 208.0]}`
      - `UIBackgroundColor` (type 10): `{'$ref': 36}`
      - `UIOpaque` (type 5): `False`
      - `UIAutoresizeSubviews` (type 5): `False`
      - `UIAutoresizingMask` (type 0): `18`
      - `UIClassName` (type 10): `{'$ref': 49}`
      - `UIOriginalClassName` (type 10): `{'$ref': 11}`
  - **UIView** (object 15)
    - class: `UIView`
    - frame: (0, 0, 320, 416)
    - raw UIBounds: (0, 0, 320, 416)
    - raw UICenter: (160, 208)
    - autoresizing mask: 18
    - background color: rgba(0.132256, 0.129286, 0.129353, 1)
    - hidden: not encoded
    - opaque: false
    - tag: not encoded
    - raw values:
      - `UIBounds` (type 8): `{'$data_hex': '0600000000000000000000a0430000d043', '$floats': [0.0, 0.0, 320.0, 416.0]}`
      - `UICenter` (type 8): `{'$data_hex': '060000204300005043', '$floats': [160.0, 208.0]}`
      - `UIBackgroundColor` (type 10): `{'$ref': 32}`
      - `UIOpaque` (type 5): `False`
      - `UIAutoresizeSubviews` (type 5): `False`
      - `UIAutoresizingMask` (type 0): `18`

- **UIBarButtonItem** (object 34)
  - class: `UIBarButtonItem`
  - target/action: `attachPhoto:` from object 34 (UIBarButtonItem) to object 21 (UIProxyObject), event mask not encoded
  - raw values:
    - `UIEnabled` (type 5): `False`
    - `UIStyle` (type 0): `1`
    - `UITitle` (type 10): `{'$ref': 4}`
    - `UITintColor` (type 10): `{'$ref': 2}`

- **UIBarButtonItem** (object 38)
  - class: `UIBarButtonItem`
  - target/action: `attachVoice:` from object 38 (UIBarButtonItem) to object 21 (UIProxyObject), event mask not encoded
  - raw values:
    - `UIEnabled` (type 5): `False`
    - `UIStyle` (type 0): `1`
    - `UITitle` (type 10): `{'$ref': 20}`
    - `UITintColor` (type 10): `{'$ref': 2}`

## Supporting objects

These objects carry no geometry, contain no view, and hold no
connection. They remain here because a reader auditing an
interpretation follows a reference into them.

- **NSObject** (object 0)
  - class: `NSObject`
  - raw values:
    - `UINibTopLevelObjectsKey` (type 10): `{'$ref': 3}`
    - `UINibObjectsKey` (type 10): `{'$ref': 35}`
    - `UINibConnectionsKey` (type 10): `{'$ref': 8}`
    - `UINibVisibleWindowsKey` (type 10): `{'$ref': 43}`
    - `UINibAccessibilityConfigurationsKey` (type 10): `{'$ref': 43}`
    - `UINibKeyValuePairsKey` (type 10): `{'$ref': 43}`

- **UIRuntimeEventConnection** (object 1)
  - class: `UIRuntimeEventConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 46}`
    - `UISource` (type 10): `{'$ref': 34}`
    - `UIDestination` (type 10): `{'$ref': 21}`

- **UIColor** (object 2)
  - class: `UIColor`
  - raw values:
    - `UIColorComponentCount` (type 0): `4`
    - `UIRed` (type 6): `0.5`
    - `UIGreen` (type 6): `0.5`
    - `UIBlue` (type 6): `0.5`
    - `UIAlpha` (type 6): `1.0`
    - `NSRGB` (type 8): `{'$data_hex': '302e3520302e3520302e35', '$text': '0.5 0.5 0.5'}`
    - `NSColorSpace` (type 0): `2`

- **NSArray** (object 3)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 21}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 50}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 33}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 7}`

- **NSString** (object 4)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '43616d', '$text': 'Cam'}`

- **NSString** (object 5)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '626c6f636b657256696577', '$text': 'blockerView'}`

- **NSString** (object 6)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '49424669727374526573706f6e646572', '$text': 'IBFirstResponder'}`

- **NSArray** (object 8)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 1}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 41}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 23}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 30}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 25}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 16}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 51}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 26}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 18}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 39}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 31}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 29}`

- **NSString** (object 9)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '494246696c65734f776e6572', '$text': 'IBFilesOwner'}`

- **UIBarButtonItem** (object 10)
  - class: `UIBarButtonItem`
  - raw values:
    - `UIEnabled` (type 5): `False`
    - `UIIsSystemItem` (type 5): `False`
    - `UISystemItem` (type 0): `5`

- **NSString** (object 11)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '554956696577', '$text': 'UIView'}`

- **NSString** (object 12)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '76696577', '$text': 'view'}`

- **NSString** (object 13)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '636f6e74656e7456696577', '$text': 'contentView'}`

- **UIRuntimeOutletConnection** (object 16)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 13}`
    - `UISource` (type 10): `{'$ref': 21}`
    - `UIDestination` (type 10): `{'$ref': 37}`

- **NSString** (object 17)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '50686f6e654e6f746556696577496e7075744163636573736f7279', '$text': 'PhoneNoteViewInputAccessory'}`

- **UIRuntimeOutletConnection** (object 18)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 48}`
    - `UISource` (type 10): `{'$ref': 7}`
    - `UIDestination` (type 10): `{'$ref': 52}`

- **NSString** (object 19)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '696e7075744163636573736f7279546f6f6c626172', '$text': 'inputAccessoryToolbar'}`

- **NSString** (object 20)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '4d6963', '$text': 'Mic'}`

- **NSArray** (object 22)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 52}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 34}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 38}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 10}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 14}`

- **UIRuntimeEventConnection** (object 23)
  - class: `UIRuntimeEventConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 24}`
    - `UISource` (type 10): `{'$ref': 14}`
    - `UIDestination` (type 10): `{'$ref': 21}`

- **NSString** (object 24)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '73746f7045646974696e673a', '$text': 'stopEditing:'}`

- **UIRuntimeOutletConnection** (object 25)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 28}`
    - `UISource` (type 10): `{'$ref': 7}`
    - `UIDestination` (type 10): `{'$ref': 34}`

- **UIRuntimeOutletConnection** (object 26)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 47}`
    - `UISource` (type 10): `{'$ref': 7}`
    - `UIDestination` (type 10): `{'$ref': 21}`

- **NSString** (object 27)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '5549546f6f6c626172', '$text': 'UIToolbar'}`

- **NSString** (object 28)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '63616d4174746163684974656d', '$text': 'camAttachItem'}`

- **UIRuntimeOutletConnection** (object 29)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 12}`
    - `UISource` (type 10): `{'$ref': 21}`
    - `UIDestination` (type 10): `{'$ref': 33}`

- **UIRuntimeOutletConnection** (object 30)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 5}`
    - `UISource` (type 10): `{'$ref': 21}`
    - `UIDestination` (type 10): `{'$ref': 15}`

- **UIRuntimeOutletConnection** (object 31)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 44}`
    - `UISource` (type 10): `{'$ref': 7}`
    - `UIDestination` (type 10): `{'$ref': 38}`

- **UIColor** (object 32)
  - class: `UIColor`
  - raw values:
    - `UIColorComponentCount` (type 0): `4`
    - `UIRed` (type 6): `0.13225606083869934`
    - `UIGreen` (type 6): `0.1292855143547058`
    - `UIBlue` (type 6): `0.12935300171375275`
    - `UIAlpha` (type 6): `1.0`
    - `NSRGB` (type 8): `{'$data_hex': '302e31333220302e31323920302e313239', '$text': '0.132 0.129 0.129'}`
    - `NSColorSpace` (type 0): `2`

- **NSArray** (object 35)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 21}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 50}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 33}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 7}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 37}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 15}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 52}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 34}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 38}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 10}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 14}`

- **UIColor** (object 36)
  - class: `UIColor`
  - raw values:
    - `UIColorComponentCount` (type 0): `4`
    - `UIRed` (type 6): `1.0`
    - `UIGreen` (type 6): `1.0`
    - `UIBlue` (type 6): `1.0`
    - `UIAlpha` (type 6): `1.0`
    - `NSRGB` (type 8): `{'$data_hex': '3120312031', '$text': '1 1 1'}`
    - `NSColorSpace` (type 0): `2`

- **UIRuntimeOutletConnection** (object 39)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 19}`
    - `UISource` (type 10): `{'$ref': 21}`
    - `UIDestination` (type 10): `{'$ref': 7}`

- **NSMutableArray** (object 40)
  - class: `NSMutableArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 37}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 15}`

- **UIRuntimeEventConnection** (object 41)
  - class: `UIRuntimeEventConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 45}`
    - `UISource` (type 10): `{'$ref': 38}`
    - `UIDestination` (type 10): `{'$ref': 21}`

- **NSString** (object 42)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '7b3235302c203235307d', '$text': '{250, 250}'}`

- **NSArray** (object 43)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`

- **NSString** (object 44)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '6d69634174746163684974656d', '$text': 'micAttachItem'}`

- **NSString** (object 45)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '617474616368566f6963653a', '$text': 'attachVoice:'}`

- **NSString** (object 46)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '61747461636850686f746f3a', '$text': 'attachPhoto:'}`

- **NSString** (object 47)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '64656c6567617465', '$text': 'delegate'}`

- **NSString** (object 48)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '666978656453706163654974656d', '$text': 'fixedSpaceItem'}`

- **NSString** (object 49)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '50686f6e65546f756368546f456469745465787456696577', '$text': 'PhoneTouchToEditTextView'}`

- **UIProxyObject** (object 50)
  - class: `UIProxyObject`
  - raw values:
    - `UIProxiedObjectIdentifier` (type 10): `{'$ref': 6}`

- **UIRuntimeOutletConnection** (object 51)
  - class: `UIRuntimeOutletConnection`
  - raw values:
    - `UILabel` (type 10): `{'$ref': 47}`
    - `UISource` (type 10): `{'$ref': 37}`
    - `UIDestination` (type 10): `{'$ref': 21}`

- **UIBarButtonItem** (object 52)
  - class: `UIBarButtonItem`
  - raw values:
    - `UIEnabled` (type 5): `False`
    - `UIIsSystemItem` (type 5): `False`
    - `UISystemItem` (type 0): `6`
    - `UIWidth` (type 6): `42.0`

