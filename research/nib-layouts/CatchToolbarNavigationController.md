# CatchToolbarNavigationController

Recovered layout for `CatchToolbarNavigationController.nib`. Every interpreted value appears beside the
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

- **CatchToolbarNavigationController** (object 7)
  - class: `CatchToolbarNavigationController`
  - encoded as: `UIClassSwapper` swapping `UINavigationController`
  - raw values:
    - `UIDefinesPresentationContext` (type 5): `False`
    - `UINavigationBar` (type 10): `{'$ref': 3}`
    - `UIClassName` (type 10): `{'$ref': 1}`
    - `UIOriginalClassName` (type 10): `{'$ref': 9}`
  - **CatchToolbarNavigationBar** (object 3)
    - class: `CatchToolbarNavigationBar`
    - encoded as: `UIClassSwapper` swapping `UINavigationBar`
    - frame: (0, 0, 320, 44)
    - raw UIBounds: (0, 0, 320, 44)
    - raw UICenter: (160, 22)
    - autoresizing mask: 2
    - background color: not encoded
    - hidden: not encoded
    - opaque: not encoded
    - tag: not encoded
    - raw values:
      - `UIBounds` (type 8): `{'$data_hex': '0600000000000000000000a04300003042', '$floats': [0.0, 0.0, 320.0, 44.0]}`
      - `UICenter` (type 8): `{'$data_hex': '06000020430000b041', '$floats': [160.0, 22.0]}`
      - `UIMultipleTouchEnabled` (type 5): `False`
      - `UIAutoresizeSubviews` (type 5): `False`
      - `UIAutoresizingMask` (type 0): `2`
      - `UIClipsToBounds` (type 5): `False`
      - `UIViewContentHuggingPriority` (type 10): `{'$ref': 11}`
      - `UIDelegate` (type 10): `{'$ref': 7}`
      - `UIClassName` (type 10): `{'$ref': 12}`
      - `UIOriginalClassName` (type 10): `{'$ref': 13}`

## Supporting objects

These objects carry no geometry, contain no view, and hold no
connection. They remain here because a reader auditing an
interpretation follows a reference into them.

- **NSObject** (object 0)
  - class: `NSObject`
  - raw values:
    - `UINibTopLevelObjectsKey` (type 10): `{'$ref': 10}`
    - `UINibObjectsKey` (type 10): `{'$ref': 4}`
    - `UINibConnectionsKey` (type 10): `{'$ref': 2}`
    - `UINibVisibleWindowsKey` (type 10): `{'$ref': 2}`
    - `UINibAccessibilityConfigurationsKey` (type 10): `{'$ref': 2}`
    - `UINibKeyValuePairsKey` (type 10): `{'$ref': 2}`

- **NSString** (object 1)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '4361746368546f6f6c6261724e617669676174696f6e436f6e74726f6c6c6572', '$text': 'CatchToolbarNavigationController'}`

- **NSArray** (object 2)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`

- **NSArray** (object 4)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 6}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 5}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 7}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 3}`

- **UIProxyObject** (object 5)
  - class: `UIProxyObject`
  - raw values:
    - `UIProxiedObjectIdentifier` (type 10): `{'$ref': 14}`

- **UIProxyObject** (object 6)
  - class: `UIProxyObject`
  - raw values:
    - `UIProxiedObjectIdentifier` (type 10): `{'$ref': 8}`

- **NSString** (object 8)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '494246696c65734f776e6572', '$text': 'IBFilesOwner'}`

- **NSString** (object 9)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '55494e617669676174696f6e436f6e74726f6c6c6572', '$text': 'UINavigationController'}`

- **NSArray** (object 10)
  - class: `NSArray`
  - raw values:
    - `NSInlinedValue` (type 5): `False`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 6}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 5}`
    - `UINibEncoderEmptyKey` (type 10): `{'$ref': 7}`

- **NSString** (object 11)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '7b3235302c203235307d', '$text': '{250, 250}'}`

- **NSString** (object 12)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '4361746368546f6f6c6261724e617669676174696f6e426172', '$text': 'CatchToolbarNavigationBar'}`

- **NSString** (object 13)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '55494e617669676174696f6e426172', '$text': 'UINavigationBar'}`

- **NSString** (object 14)
  - class: `NSString`
  - raw values:
    - `NS.bytes` (type 8): `{'$data_hex': '49424669727374526573706f6e646572', '$text': 'IBFirstResponder'}`

