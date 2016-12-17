"""
Author: Glenn Sweeney
Date: 2016/12/17
"""

class Facet(object):
    """ A facet is a triangle positioned in 3D space. It is the fundamental particle of rendering.

    A facet is defined by three coordinates denoting its corners. It is assumed to be infinitely
    thin, and has no distinction between sides. The surface has a spectral reflectance, which
    describes how it interacts with lights (and other light rays) in the scene.
    """

    def __init__(self, p1, p2, p3, spectral_reflectance):
        """ Initialize a Facet with corner Points and a SpectralReflectance.

        Args:
            p1: first corner Point
            p2: second corner Point
            p3: third corner Point
            spectral_reflectance: the surface SpectralReflectance

        """
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.spectral_reflectance = spectral_reflectance # Need to define how this will be stored later.

    #enddef

    def intersect_ray(self, ray):
        """ Test if a Ray intersects the facet in 3D.

        Args:
            ray: a Ray to be tested

        Returns:
            The double-precision distance along the ray where intersection occured.
            If the ray did not intersect (or intersected behind the ray origin), 0 is returned
            to indicate nonintersection.
        """
        pass

    #enddef

    def get_color(self, point, lights):
        """ Compute the Facet color at a Point, given scene lighting.

        Args:
            point: the location at which to compute lighting interaction
            lights: an iterable of lights to consider for interaction

        Returns:
            The SpectralPowerDistribution of the Facet at the selected Point
        """
        pass

    #enddef

    def apply_transform(self, tform):
        """ Apply a rigid-body transformation to the Facet.

        Args:
            tform: the Transform to be applied
        """
        pass

    #enddef

#endclass


if __name__ == "__main__":
    pass
#endif
