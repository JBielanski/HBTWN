#!/bin/python3

'''
HBTWN v. 0.04
Project with application which allow to calculate telescope size which is needed to achieve expected angular resolution.
HBTWN  Copyright (C) 2021  Jan Bielański
'''
print("------------------------------------------------------------------------------------------------------------")
print("                                             HBTWN v. 0.04                                                  ")
print("Application allow to calculate telescope size which is needed to achieve expected angular resolution.       ")
print("                              HBTWN  Copyright (C) 2021  Jan Bielański                                      ")
print("------------------------------------------------------------------------------------------------------------")
print("")

# 3-RD party dependency
import numpy as np
from enum import Enum

# Project modules
import modules.UnitsConstantsModule as HBTWN_UCM
import modules.CoreNumericalModule as HBTWN_CNM


# JUPITER
obj_name = "Jupiter"
obj_size = [ 2*69911.0, 'km' ]
obj_dist = [ 600000000.0, 'km' ]
obj_dist_au = HBTWN_UCM.dist_units_converter(obj_dist[0], obj_dist[1], 'au')
obj_shape = HBTWN_UCM.ObjectShape.SPHERICAL
number_of_pixels = 100
wavelength = [522.0, 'nm']
telescope_size_unit = 'mm'

print(str(obj_name) + " diameter: " + str(obj_size[0]) + " " + str(obj_size[1]))
print(str(obj_name) + " distance: " + str(obj_dist[0]) + " " + str(obj_dist[1]) + " / " + str(obj_dist_au[0]) + " " + str(obj_dist_au[1]))
print("Expected size on image: " + str(number_of_pixels) + " pixels")
print("Light wavelength: " + str(wavelength[0]) + str(wavelength[1]))
telescope_size, object_size = HBTWN_CNM.calculate_telescope_size(obj_size, obj_dist, obj_dist, number_of_pixels, wavelength, telescope_size_unit)
print("Mirror/lens size in telescope: " + str(telescope_size[0]) + " " + str(telescope_size[1]) + ", object size on sky: " + str(object_size[0]) + " " + str(object_size[1]))

print("")
print("-----------------------------------------------------------------------------")
print("")

# EARTH from 1 au
obj_name = "Earth"
obj_size = [ 2*6371.0, 'km' ]
obj_dist = [ 1.0, 'au' ]
obj_dist_au = HBTWN_UCM.dist_units_converter(obj_dist[0], obj_dist[1], 'au')
obj_shape = HBTWN_UCM.ObjectShape.SPHERICAL
number_of_pixels = 100
wavelength = [522.0, 'nm']
telescope_size_unit = 'mm'

print(str(obj_name) + " diameter: " + str(obj_size[0]) + " " + str(obj_size[1]))
print(str(obj_name) + " distance: " + str(obj_dist[0]) + " " + str(obj_dist[1]) + " / " + str(obj_dist_au[0]) + " " + str(obj_dist_au[1]))
print("Expected size on image: " + str(number_of_pixels) + " pixels")
print("Light wavelength: " + str(wavelength[0]) + str(wavelength[1]))
telescope_size, object_size = HBTWN_CNM.calculate_telescope_size(obj_size, obj_dist, obj_dist, number_of_pixels, wavelength, telescope_size_unit)
print("Mirror/lens size in telescope: " + str(telescope_size[0]) + " " + str(telescope_size[1]) + ", object size on sky: " + str(object_size[0]) + " " + str(object_size[1]))

print("")
print("-----------------------------------------------------------------------------")
print("")

# EARTH from 1 ly
obj_name = "Earth"
obj_size = [ 2*6371.0, 'km' ]
obj_dist = [ 1.0, 'ly' ]
obj_dist_au = HBTWN_UCM.dist_units_converter(obj_dist[0], obj_dist[1], 'au')
obj_shape = HBTWN_UCM.ObjectShape.SPHERICAL
number_of_pixels = 100
wavelength = [522.0, 'nm']
telescope_size_unit = 'km'

print(str(obj_name) + " diameter: " + str(obj_size[0]) + " " + str(obj_size[1]))
print(str(obj_name) + " distance: " + str(obj_dist[0]) + " " + str(obj_dist[1]) + " / " + str(obj_dist_au[0]) + " " + str(obj_dist_au[1]))
print("Expected size on image: " + str(number_of_pixels) + " pixels")
print("Light wavelength: " + str(wavelength[0]) + str(wavelength[1]))
telescope_size, object_size = HBTWN_CNM.calculate_telescope_size(obj_size, obj_dist, obj_dist, number_of_pixels, wavelength, telescope_size_unit)
print("Mirror/lens size in telescope: " + str(telescope_size[0]) + " " + str(telescope_size[1]) + ", object size on sky: " + str(object_size[0]) + " " + str(object_size[1]))

print("")
print("-----------------------------------------------------------------------------")
print("")

# EARTH from 100 ly
# Article test: Slava G. Turyshev, "DIRECT MULTIPIXEL IMAGING AND SPECTROSCOPY OF AN EXOPLANET WITH A SOLAR GRAVITY LENS MISSION"
obj_name = "Earth"
obj_size = [ 2*6371.0, 'km' ]
obj_dist = [ 30, 'pc' ]
obj_dist_au = HBTWN_UCM.dist_units_converter(obj_dist[0], obj_dist[1], 'ly')
obj_shape = HBTWN_UCM.ObjectShape.SPHERICAL
number_of_pixels = 1
wavelength = [1.0, 'um']
telescope_size_unit = 'km'

print(str(obj_name) + " diameter: " + str(obj_size[0]) + " " + str(obj_size[1]))
print(str(obj_name) + " distance: " + str(obj_dist[0]) + " " + str(obj_dist[1]) + " / " + str(obj_dist_au[0]) + " " + str(obj_dist_au[1]))
print("Expected size on image: " + str(number_of_pixels) + " pixels")
print("Light wavelength: " + str(wavelength[0]) + str(wavelength[1]))
telescope_size, object_size = HBTWN_CNM.calculate_telescope_size(obj_size, obj_dist, obj_dist, number_of_pixels, wavelength, telescope_size_unit)
print("Mirror/lens size in telescope: " + str(telescope_size[0]) + " " + str(telescope_size[1]) + ", object size on sky: " + str(object_size[0]) + " " + str(object_size[1]))

print("")
print("-----------------------------------------------------------------------------")
print("")

# EARTH from 22180 ly im M13
obj_name = "Earth"
obj_size = [ 2*6371.0, 'km' ]
obj_dist = [ 22180.0, 'ly' ]
obj_dist_au = HBTWN_UCM.dist_units_converter(obj_dist[0], obj_dist[1], 'au')
obj_shape = HBTWN_UCM.ObjectShape.SPHERICAL
number_of_pixels = 100
wavelength = [522.0, 'nm']
telescope_size_unit = 'km'

print(str(obj_name) + " diameter: " + str(obj_size[0]) + " " + str(obj_size[1]))
print(str(obj_name) + " distance: " + str(obj_dist[0]) + " " + str(obj_dist[1]) + " / " + str(obj_dist_au[0]) + " " + str(obj_dist_au[1]))
print("Expected size on image: " + str(number_of_pixels) + " pixels")
print("Light wavelength: " + str(wavelength[0]) + str(wavelength[1]))
telescope_size, object_size = HBTWN_CNM.calculate_telescope_size(obj_size, obj_dist, obj_dist, number_of_pixels, wavelength, telescope_size_unit)
print("Mirror/lens size in telescope: " + str(telescope_size[0]) + " " + str(telescope_size[1]) + ", object size on sky: " + str(object_size[0]) + " " + str(object_size[1]))

print("")
print("-----------------------------------------------------------------------------")
print("")

# Tennis ball on the Moon
obj_name = "Tennis ball"
obj_size = [ 6.86, 'cm' ]
obj_dist = [ 384400, 'km' ]
obj_dist_au = HBTWN_UCM.dist_units_converter(obj_dist[0], obj_dist[1], 'au')
obj_shape = HBTWN_UCM.ObjectShape.SPHERICAL
number_of_pixels = 100
wavelength = [1.3, 'mm']
telescope_size_unit = 'km'

print(str(obj_name) + " diameter: " + str(obj_size[0]) + " " + str(obj_size[1]))
print(str(obj_name) + " distance: " + str(obj_dist[0]) + " " + str(obj_dist[1]) + " / " + str(obj_dist_au[0]) + " " + str(obj_dist_au[1]))
print("Expected size on image: " + str(number_of_pixels) + " pixels")
print("Light wavelength: " + str(wavelength[0]) + str(wavelength[1]))
telescope_size, object_size = HBTWN_CNM.calculate_telescope_size(obj_size, obj_dist, obj_shape, number_of_pixels, wavelength, telescope_size_unit)
print("Mirror/lens size in telescope: " + str(telescope_size[0]) + " " + str(telescope_size[1]) + ", object size on sky: " + str(object_size[0]) + " " + str(object_size[1]))

print("")
print("-----------------------------------------------------------------------------")
print("")

'''
print("Telescope resolution 5\" (127mm): " + str(HBTWN_CNM.calculate_telescope_resolution([5,'inch'])))
print("Telescope resolution 8\" (203.2mm): " + str(HBTWN_CNM.calculate_telescope_resolution([8,'inch'])))
print("Telescope resolution 10\" (254mm): " + str(HBTWN_CNM.calculate_telescope_resolution([10,'inch'])))
print("Telescope resolution 16\" (406.4mm): " + str(HBTWN_CNM.calculate_telescope_resolution([16,'inch'])))
'''











