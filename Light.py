"""
Author: Alexandra Booth
Date: 12/22/16
"""

class Light(object):

    def __init__(self, position, spectrum, brightness):
        """ Initialize a Light with a location, (normalized) spectrum, and brightness

        Args:
            positon:     a Point defining the light origin
            spectrum:    the source intensity as a Spectrum

        """
        pass

    #enddef

    def apply_transform(self, tform):
        """ Apply a rigid-body transformation to the Light.

        Args:
            tform: the Transform to be applied
        """
        pass

    #enddef

    def set_intensity(self, intensity):
        """ Adjust the intensity of the light spectrum to a target value

        Args:
            intensity: the new target intensity for the light (W/sr)

        """
        pass

    #enddef

#endclass


if __name__ == "__main__":
    pass
#endif