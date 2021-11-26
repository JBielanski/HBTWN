#!/bin/python3

'''
HBTWN v. 0.02
Project with application which allow to calculate telescope size which is needed to achieve expected angular resolution.
HBTWN  Copyright (C) 2021  Jan Bielański
'''
print("------------------------------------------------------------------------------------------------------------")
print("                                             HBTWN v. 0.02                                                  ")
print("Application allow to calculate telescope size which is needed to achieve expected angular resolution.       ")
print("                              HBTWN  Copyright (C) 2021  Jan Bielański                                      ")
print("------------------------------------------------------------------------------------------------------------")
print("")

import numpy as np
from enum import Enum

class ObjectShape(Enum):
    UNDEFINED = -1
    FLAT = 1
    SPHERICAL = 2
    def get(self):
        return self.value
    def get_str(self):
        return { -1:"UNDEFINED", 1:"FLAT", 2:"SPHERICAL" }[self.value]
    def __int__(self):
        return self.value

'''
dist_units_converter - convert distance value in selected units to other unit (default unit in function is [m])
_input_value - value as number ex. _input_value = 66.6
_input_unit - one of the unit symbol: m/cm/mm/um/nm/km/inch/au/ly/pc if it wrong the function return None, ex. _input_unit = 'ly'
_output_unit - one of the unit symbol: m/cm/mm/um/nm/km/inch/au/ly/pc if it wrong the function return None, ex. _input_unit = 'pc'
@return return array with calculated value and unit as array
'''
def dist_units_converter(_input_value, _input_unit, _output_unit):
    dist_units_conversion = dict([('m',np.float64(1.0)),('cm',np.float64(0.01)),('mm',np.float64(0.001)),('um',np.float64(0.000001)),('nm',np.float64(0.000000001)),('km',np.float64(1000.0)),('inch',np.float64(0.0254)),('au',np.float64(149597870700.0)),('ly',np.float64(149597870700.0*63241.0)),('pc',np.float64(149597870700.0*206264.8))])
    a_scale = dist_units_conversion.get(_input_unit)
    b_scale = dist_units_conversion.get(_output_unit)
    try:
        res = (_input_value*a_scale)/b_scale
    except TypeError as e:
        print('Unsupported UNIT symbol!!!')
        return [None, None]
    return [res, _output_unit]


'''
angle_units_converter - convert angle value in selected units to other unit (default unit in function is [deg])
_input_value - value as number ex. _input_value = 66.6
_input_unit - one of the unit symbol: deg/amin/arcmin/am/MOA/asec/arcsec/as/mas/uas/rad if it wrong the function return None, ex. _input_unit = 'rad'
_output_unit - one of the unit symbol: deg/amin/arcmin/am/MOA/asec/arcsec/as/mas/uas/rad if it wrong the function return None, ex. _input_unit = 'deg'
@return return array with calculated value and unit as array
'''
def angle_units_converter(_input_value, _input_unit, _output_unit):
    angle_units_conversion = dict([('deg',np.float64(1.0)),('amin',np.float64(1.0/60.0)),('arcmin',np.float64(1.0/60.0)),('am',np.float64(1.0/60.0)),('MOA',np.float64(1.0/60.0)),('asec',np.float64(1.0/3600.0)),('arcsec',np.float64(1.0/3600.0)),('as',np.float64(1.0/3600.0)),('mas',np.float64(1.0/3600000.0)),('uas',np.float64(1.0/3600000000.0)),('rad',np.float64(180.0/np.pi))])
    a_scale = angle_units_conversion.get(_input_unit)
    b_scale = angle_units_conversion.get(_output_unit)
    try:
        res = (_input_value*a_scale)/b_scale
    except TypeError as e:
        print('Unsupported UNIT symbol!!!')
        return [None, None]
    return [res, _output_unit]


'''
calculate_telescope_size - calculate telescope size which is needed to see object in input resolution
_target_obj_physical_size - target object physical size as array: [ size, unit ]
_target_obj_physical_dist - target object physical distance as array: [ distance, unit ]
_object_shape - object shape (default: ObjectShape.SPHERICAL)
_number_of_pixels - number of pixels on image (default: 100)
_wavelength - wavelength value (default: [522.0, nm])
_telescope_size_unit - telescope size unit (default: mm)
@return calculated telescope size value and unit as array and object size in arcsec
'''
def calculate_telescope_size(_target_obj_physical_size, _target_obj_physical_dist , _object_shape = ObjectShape.SPHERICAL, _number_of_pixels = 100, _wavelength = [522.0, 'nm'], _telescope_size_unit = 'mm'):

    try:
        size_m = dist_units_converter(_target_obj_physical_size[0], _target_obj_physical_size[1], 'm')
        size_scaled_m = [ size_m[0]*(1.0/_number_of_pixels), size_m[1] ]
        dist_m = dist_units_converter(_target_obj_physical_dist[0], _target_obj_physical_dist[1], 'm')

        '''
        Angular size of objects in radians and arcsec
        delta [rad] = 2*arctan(diameter [m] / (2*distance [m]))
        delta [rad] = 2*arcsin(diameter [m] / (2*distance [m]))
        '''
        angular_size_in_rads = 0.0
        angular_size_in_rads_for_pixel = 0.0
        if _object_shape is ObjectShape.FLAT:
            angular_size_in_rads = 2.0 * np.arctan(size_m[0]/(dist_m[0]+dist_m[0]))
            angular_size_in_rads_for_pixel = 2.0 * np.arctan(size_scaled_m[0]/(dist_m[0]+dist_m[0]))
        else:
            _object_shape = ObjectShape.SPHERICAL
            angular_size_in_rads = 2.0 * np.arcsin(size_m[0]/(dist_m[0]+dist_m[0]))
            angular_size_in_rads_for_pixel = 2.0 * np.arcsin(size_scaled_m[0]/(dist_m[0]+dist_m[0]))

        angular_size_in_arcsec = angle_units_converter(angular_size_in_rads, 'rad', 'arcsec')[0]
        angular_size_in_arcsec_for_pixel = angle_units_converter(angular_size_in_rads_for_pixel, 'rad', 'arcsec')[0]

        '''
        Telescope angular resolution
        theta [rad] = 1.22 * ( lambda [m] / D [m] ), where lambda - wavelength, D - telescope diameter
        D = 1.22 * (lambda/theta)
        '''

        wavelength_m = dist_units_converter(_wavelength[0],_wavelength[1],'m')

        D = 1.22*(wavelength_m[0]/angular_size_in_rads_for_pixel)
        telescope_diameter = dist_units_converter(D,'m',_telescope_size_unit)

        return telescope_diameter, [ angular_size_in_arcsec, 'arcsec' ]

    except TypeError as e:
        print('Calculation failure!!!')
        return None, None

'''
calculate_telescope_resolution - calculate telescope angular resolution
_telescope_parameters - telescope size as array: [size, unit]
_wavelength - wavelength value (default: [522.0, nm])
_resolution_unit - telescope resolution unit (default: arcsec)
@return telescope resolution as array resolution and unit
'''
def calculate_telescope_resolution(_telescope_parameters, _wavelength = [522.0, 'nm'], _resolution_unit = 'arcsec'):
    try:

        size_m = dist_units_converter(_telescope_parameters[0], _telescope_parameters[1], 'm')
        wavelength_m = dist_units_converter(_wavelength[0],_wavelength[1],'m')

        '''
        Telescope angular resolution
        theta [rad] = 1.22 * ( lambda [m] / D [m] ), where lambda - wavelength, D - telescope diameter
        '''
        theta = 1.22*(wavelength_m[0]/size_m[0])

        print(theta)

        telescope_resolution = angle_units_converter(theta, 'rad', 'arcsec')
        return telescope_resolution

    except TypeError as e:
        print('Calculation failure!!!')
        return None





# JUPITER
obj_name = "Jupiter"
obj_size = [ 2*69911.0, 'km' ]
obj_dist = [ 600000000.0, 'km' ]
obj_dist_au = dist_units_converter(obj_dist[0], obj_dist[1], 'au')
obj_shape = ObjectShape.SPHERICAL
number_of_pixels = 100
wavelength = [522.0, 'nm']
telescope_size_unit = 'mm'

print(str(obj_name) + " diameter: " + str(obj_size[0]) + " " + str(obj_size[1]))
print(str(obj_name) + " distance: " + str(obj_dist[0]) + " " + str(obj_dist[1]) + " / " + str(obj_dist_au[0]) + " " + str(obj_dist_au[1]))
print("Expected size on image: " + str(number_of_pixels) + " pixels")
print("Light wavelength: " + str(wavelength[0]) + str(wavelength[1]))
telescope_size, object_size = calculate_telescope_size(obj_size, obj_dist, obj_dist, number_of_pixels, wavelength, telescope_size_unit)
print("Mirror/lens size in telescope: " + str(telescope_size[0]) + " " + str(telescope_size[1]) + ", object size on sky: " + str(object_size[0]) + " " + str(object_size[1]))

print("")
print("-----------------------------------------------------------------------------")
print("")

# EARTH from 1 au
obj_name = "Earth"
obj_size = [ 2*6371.0, 'km' ]
obj_dist = [ 1.0, 'au' ]
obj_dist_au = dist_units_converter(obj_dist[0], obj_dist[1], 'au')
obj_shape = ObjectShape.SPHERICAL
number_of_pixels = 100
wavelength = [522.0, 'nm']
telescope_size_unit = 'mm'

print(str(obj_name) + " diameter: " + str(obj_size[0]) + " " + str(obj_size[1]))
print(str(obj_name) + " distance: " + str(obj_dist[0]) + " " + str(obj_dist[1]) + " / " + str(obj_dist_au[0]) + " " + str(obj_dist_au[1]))
print("Expected size on image: " + str(number_of_pixels) + " pixels")
print("Light wavelength: " + str(wavelength[0]) + str(wavelength[1]))
telescope_size, object_size = calculate_telescope_size(obj_size, obj_dist, obj_dist, number_of_pixels, wavelength, telescope_size_unit)
print("Mirror/lens size in telescope: " + str(telescope_size[0]) + " " + str(telescope_size[1]) + ", object size on sky: " + str(object_size[0]) + " " + str(object_size[1]))

print("")
print("-----------------------------------------------------------------------------")
print("")

# EARTH from 1 ly
obj_name = "Earth"
obj_size = [ 2*6371.0, 'km' ]
obj_dist = [ 1.0, 'ly' ]
obj_dist_au = dist_units_converter(obj_dist[0], obj_dist[1], 'au')
obj_shape = ObjectShape.SPHERICAL
number_of_pixels = 100
wavelength = [522.0, 'nm']
telescope_size_unit = 'km'

print(str(obj_name) + " diameter: " + str(obj_size[0]) + " " + str(obj_size[1]))
print(str(obj_name) + " distance: " + str(obj_dist[0]) + " " + str(obj_dist[1]) + " / " + str(obj_dist_au[0]) + " " + str(obj_dist_au[1]))
print("Expected size on image: " + str(number_of_pixels) + " pixels")
print("Light wavelength: " + str(wavelength[0]) + str(wavelength[1]))
telescope_size, object_size = calculate_telescope_size(obj_size, obj_dist, obj_dist, number_of_pixels, wavelength, telescope_size_unit)
print("Mirror/lens size in telescope: " + str(telescope_size[0]) + " " + str(telescope_size[1]) + ", object size on sky: " + str(object_size[0]) + " " + str(object_size[1]))

print("")
print("-----------------------------------------------------------------------------")
print("")

# EARTH from 100 ly
# Article test: Slava G. Turyshev, "DIRECT MULTIPIXEL IMAGING AND SPECTROSCOPY OF AN EXOPLANET WITH A SOLAR GRAVITY LENS MISSION"
obj_name = "Earth"
obj_size = [ 2*6371.0, 'km' ]
obj_dist = [ 30, 'pc' ]
obj_dist_au = dist_units_converter(obj_dist[0], obj_dist[1], 'ly')
obj_shape = ObjectShape.SPHERICAL
number_of_pixels = 1
wavelength = [1.0, 'um']
telescope_size_unit = 'km'

print(str(obj_name) + " diameter: " + str(obj_size[0]) + " " + str(obj_size[1]))
print(str(obj_name) + " distance: " + str(obj_dist[0]) + " " + str(obj_dist[1]) + " / " + str(obj_dist_au[0]) + " " + str(obj_dist_au[1]))
print("Expected size on image: " + str(number_of_pixels) + " pixels")
print("Light wavelength: " + str(wavelength[0]) + str(wavelength[1]))
telescope_size, object_size = calculate_telescope_size(obj_size, obj_dist, obj_dist, number_of_pixels, wavelength, telescope_size_unit)
print("Mirror/lens size in telescope: " + str(telescope_size[0]) + " " + str(telescope_size[1]) + ", object size on sky: " + str(object_size[0]) + " " + str(object_size[1]))

print("")
print("-----------------------------------------------------------------------------")
print("")

# EARTH from 22180 ly im M13
obj_name = "Earth"
obj_size = [ 2*6371.0, 'km' ]
obj_dist = [ 22180.0, 'ly' ]
obj_dist_au = dist_units_converter(obj_dist[0], obj_dist[1], 'au')
obj_shape = ObjectShape.SPHERICAL
number_of_pixels = 100
wavelength = [522.0, 'nm']
telescope_size_unit = 'km'

print(str(obj_name) + " diameter: " + str(obj_size[0]) + " " + str(obj_size[1]))
print(str(obj_name) + " distance: " + str(obj_dist[0]) + " " + str(obj_dist[1]) + " / " + str(obj_dist_au[0]) + " " + str(obj_dist_au[1]))
print("Expected size on image: " + str(number_of_pixels) + " pixels")
print("Light wavelength: " + str(wavelength[0]) + str(wavelength[1]))
telescope_size, object_size = calculate_telescope_size(obj_size, obj_dist, obj_dist, number_of_pixels, wavelength, telescope_size_unit)
print("Mirror/lens size in telescope: " + str(telescope_size[0]) + " " + str(telescope_size[1]) + ", object size on sky: " + str(object_size[0]) + " " + str(object_size[1]))

print("")
print("-----------------------------------------------------------------------------")
print("")

# Tennis ball on the Moon
obj_name = "Tennis ball"
obj_size = [ 6.86, 'cm' ]
obj_dist = [ 384400, 'km' ]
obj_dist_au = dist_units_converter(obj_dist[0], obj_dist[1], 'au')
obj_shape = ObjectShape.SPHERICAL
number_of_pixels = 100
wavelength = [1.3, 'mm']
telescope_size_unit = 'km'

print(str(obj_name) + " diameter: " + str(obj_size[0]) + " " + str(obj_size[1]))
print(str(obj_name) + " distance: " + str(obj_dist[0]) + " " + str(obj_dist[1]) + " / " + str(obj_dist_au[0]) + " " + str(obj_dist_au[1]))
print("Expected size on image: " + str(number_of_pixels) + " pixels")
print("Light wavelength: " + str(wavelength[0]) + str(wavelength[1])) 
telescope_size, object_size = calculate_telescope_size(obj_size, obj_dist, obj_shape, number_of_pixels, wavelength, telescope_size_unit)
print("Mirror/lens size in telescope: " + str(telescope_size[0]) + " " + str(telescope_size[1]) + ", object size on sky: " + str(object_size[0]) + " " + str(object_size[1]))

print("")
print("-----------------------------------------------------------------------------")
print("")

'''
print("Telescope resolution 5\" (127mm): " + str(calculate_telescope_resolution([5,'inch'])))
print("Telescope resolution 8\" (203.2mm): " + str(calculate_telescope_resolution([8,'inch'])))
print("Telescope resolution 10\" (254mm): " + str(calculate_telescope_resolution([10,'inch'])))
print("Telescope resolution 16\" (406.4mm): " + str(calculate_telescope_resolution([16,'inch'])))
'''











