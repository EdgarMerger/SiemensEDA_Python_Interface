import win32com.client as win32
import sys, os, subprocess
from constraintmanager_ifc import constants as c
from constraintmanager_ifc import *

WHERE_AM_I, WHO_AM_I=os.path.split(os.path.realpath(__file__))
sys.path.append(WHERE_AM_I)

i = 0
idx = 0

def init():
    print('Running makepy ...')
    result = subprocess.run(['python', f'{WHERE_AM_I}\\mpy.py'], capture_output=True, text=True)
    # print(result)

def main():
    
    # this is a simple IntelliSense usage example
    # the following annotation establishes the classes and definitions from constraintmanager_ifc.py to the IDE (VScode, Pycharm, etc.) and thus enables autocompletion  
    objConstraintsAuto : IConstraintsAuto = None

    objConstraintsAuto = win32.Dispatch('ConstraintsAuto', 'IConstraintsAuto')
	
    # Validate a license for Constraints Automation
    oSeed = objConstraintsAuto.Validate(0)
    objConstraintsAuto.Validate(oSeed)

    # Here custom code can be entered
    objDesign = objConstraintsAuto.Design
    objDesignParams = objDesign.CreateDesignParams()
    objDesignParams.ProjectFile = "C:\\Users\\Z0118870\\OneDrive - ZF Friedrichshafen AG\\Desktop\\mentor_project\\A0079K6529.prj"
    pass
    

if (__name__ == '__main__'):
#    init() #run only when not having running makepy.py previously on your computer
    main()

    
