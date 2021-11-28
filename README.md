# HBTWN v. 0.04
Project with application which allow to calculate telescope size which is needed to achieve expected angular resolution.
HBTWN  Copyright (C) 2021  Jan Bielański

Requirements:
- python 3 (https://www.python.org/)
- NumPy (https://numpy.org/)

Application usage:
python HBTWN.py

Changes:

--- 0.04 ---
- prepare for GUI version
- code refactoring, added modules
-- UnitsConstantsModule - module with constants, units and units converion functions
-- CoreNumericalModule - numerical core module, all calculations doing here 

--- 0.03 ---
- GUI initial files in project (not connected to application yet)

--- 0.02 ---
- fixed formulas
- added object shape selection for spherical and flat objects

--- 0.01 ---
- initial version of application
- initial calculation core
- initial test inside the code

TODO:
- better calculations model, consider of camera behaviour, image reconstruction such as Event Horizon Telescope – EHT
- application GUI
- telescope visualization
- stand alone application for Linux/Windows/MacOS
- [optional] SNR (signal to noise ratio)
- [optional] calculate exposition time which is needed to get useful SNR ratio
- [optional] simulation of star gravity lenses
