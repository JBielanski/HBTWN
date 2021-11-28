#!/bin/python3

'''
HBTWN - UnitsConstantsModule
Module storage units and constants used in project.
HBTWN UnitsConstantsModule  Copyright (C) 2021  Jan Bielański
'''

# 3-RD party dependency
import numpy as np
from enum import Enum

'''
ObjectShape - object shape type, storage three values:
UNDEFINED - unknowt object type (usage if some errors happened)
FLAT - flat objects for all non spherical objects such as gas cloud, nebulas etc.
SPHERICAL - spherical object for all spherical objects such as planets, stars
Methods:
get - return Enum object
get_str - return string name: UNDEFINED/FLAT/SPHERICAL
__int__ - via int() function return numerical value: -1/1/2
'''
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
