# raytrace_py

Classes:
ray
world
camera
light
mesh
facet

Milestones:
define class structures (Dec 23rd)
implement:
light ray cast
camera ray cast
ray triangle intersection

Facet:
Position (3 points)
spectralReflectance
- doesCameraRayIntersect
- doesRayHitLight
- applyTransform

Light: (point source)
position
normalized spectrum
brightness
- getSpectralPowerDistribution
- applyTransform

Camera:
resolution (number of pixels)
angularFOV (measured to where?)
opticalAxisDirection
position
someUndeterminedTransformToDecideCameraSensitivityWhichIncludesExposureTimeAndStuff
colorTransformFromSpectraToDisplayRGB
-applyTransform
-takeAPicture
-adjustExposure

Ray:
origin
direction
maybeOtherStuff?
- applyTransform

Mesh:
list of Facets
-facetsWhichCameraRayIntersects
-applyTransform

Scene:
Mesh(es)
Light(s)
- interactRay
