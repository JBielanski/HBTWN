# HBTWN v. 0.05
Project with application which allow to calculate telescope size which is needed to achieve expected angular resolution.
HBTWN  Copyright (C) 2021  Jan Bielański

Requirements:
- python 3 (https://www.python.org/)
- NumPy (https://numpy.org/)

Application usage:
python HBTWN.py

Changes:

--- 0.05 ---
- added algorithm which allow to calculate object size visible by telescope

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

APPLICATION DEVELOPMENT PLAN, TODO:

--> Mathematical models:
- better calculations model, consider of camera behaviour, image reconstruction such as Event Horizon Telescope – EHT
- [optional] calculate SNR (signal to noise ratio)
- [optional] calculate exposition time which is needed to get useful SNR ratio

--> GUI
- application graphics GUI (QT)
- application tex UI (simple text interface)

--> Visualizations
- telescope visualization
- angular resolution plot for selected wavelengths range with selected telescope size (GNUPLOT - for text mode, MATPLOTLIB)
- [optional] simulation of star gravity lenses
- [optional] simulate image in telescope

--> Database
- database for specific wavelengths
- datebase for celestial objects
- database for predefined telescopes

--> Operation system support
- stand alone application for Linux/Windows/MacOS
- phone application (Android)

