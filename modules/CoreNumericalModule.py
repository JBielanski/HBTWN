#!/bin/python3

'''
HBTWN - CoreNumericalModule
Module storage primary numerical functions.
HBTWN CoreNumericalModule  Copyright (C) 2021  Jan Bielański
'''
# 3-RD party dependency
import numpy as np
from enum import Enum

# Project modules
import modules.UnitsConstantsModule as HBTWN_UCM

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
def calculate_telescope_size(_target_obj_physical_size, _target_obj_physical_dist , _object_shape = HBTWN_UCM.ObjectShape.SPHERICAL, _number_of_pixels = 100, _wavelength = [522.0, 'nm'], _telescope_size_unit = 'mm'):

    try:
        size_m = HBTWN_UCM.dist_units_converter(_target_obj_physical_size[0], _target_obj_physical_size[1], 'm')
        size_scaled_m = [ size_m[0]*(1.0/_number_of_pixels), size_m[1] ]
        dist_m = HBTWN_UCM.dist_units_converter(_target_obj_physical_dist[0], _target_obj_physical_dist[1], 'm')

        '''
        Angular size of objects in radians and arcsec
        delta [rad] = 2*arctan(diameter [m] / (2*distance [m]))
        delta [rad] = 2*arcsin(diameter [m] / (2*distance [m]))
        '''
        angular_size_in_rads = 0.0
        angular_size_in_rads_for_pixel = 0.0
        if _object_shape is HBTWN_UCM.ObjectShape.FLAT:
            angular_size_in_rads = 2.0 * np.arctan(size_m[0]/(dist_m[0]+dist_m[0]))
            angular_size_in_rads_for_pixel = 2.0 * np.arctan(size_scaled_m[0]/(dist_m[0]+dist_m[0]))
        else:
            _object_shape = HBTWN_UCM.ObjectShape.SPHERICAL
            angular_size_in_rads = 2.0 * np.arcsin(size_m[0]/(dist_m[0]+dist_m[0]))
            angular_size_in_rads_for_pixel = 2.0 * np.arcsin(size_scaled_m[0]/(dist_m[0]+dist_m[0]))

        angular_size_in_arcsec = HBTWN_UCM.angle_units_converter(angular_size_in_rads, 'rad', 'arcsec')[0]
        angular_size_in_arcsec_for_pixel = HBTWN_UCM.angle_units_converter(angular_size_in_rads_for_pixel, 'rad', 'arcsec')[0]

        '''
        Telescope angular resolution
        theta [rad] = 1.22 * ( lambda [m] / D [m] ), where lambda - wavelength, D - telescope diameter
        D = 1.22 * (lambda/theta)
        '''

        wavelength_m = HBTWN_UCM.dist_units_converter(_wavelength[0],_wavelength[1],'m')

        D = 1.22*(wavelength_m[0]/angular_size_in_rads_for_pixel)
        telescope_diameter = HBTWN_UCM.dist_units_converter(D,'m',_telescope_size_unit)

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

        size_m = HBTWN_UCM.dist_units_converter(_telescope_parameters[0], _telescope_parameters[1], 'm')
        wavelength_m = HBTWN_UCM.dist_units_converter(_wavelength[0],_wavelength[1],'m')

        '''
        Telescope angular resolution
        theta [rad] = 1.22 * ( lambda [m] / D [m] ), where lambda - wavelength, D - telescope diameter
        '''
        theta = 1.22*(wavelength_m[0]/size_m[0])

        print(theta)

        telescope_resolution = HBTWN_UCM.angle_units_converter(theta, 'rad', 'arcsec')
        return telescope_resolution

    except TypeError as e:
        print('Calculation failure!!!')
        return None

