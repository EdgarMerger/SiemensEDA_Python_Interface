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
    # 1. Dispatch the Release Environment Server
    env_server = win32.Dispatch("MGCPCBReleaseEnvironmentLib.MGCPCBReleaseEnvServer")
    
    # 2. Set the desired environment (point to your SDD_HOME folder)
    env_server.SetEnvironment(r"C:\MentorGraphics\EEVX.2.12\SDD_HOME")

    # this is a simple IntelliSense usage example
    # the following annotation establishes the classes and definitions from constraintmanager_ifc.py to the IDE (VScode, Pycharm, etc.) and thus enables autocompletion  
    objConstraintsAuto : IConstraintsAuto = None

    # 3. Now create your ConstraintsAuto application
    objConstraintsAuto = win32.Dispatch('ConstraintsAuto', 'IConstraintsAuto')
	
    # Validate a license for Constraints Automation
    oSeed = objConstraintsAuto.Validate(0)
    objConstraintsAuto.Validate(oSeed)

    # 4. Use 'app' methods normally
    objConstraintsAuto.OpenDatabase("some_design_file")

    # Here custom code can be entered
    objDesign = objConstraintsAuto.Settings
    objDesignParams = objDesign.CreateDesignParams()
    objDesignParams.ProjectFile = "C:\\Users\\Z0118870\\OneDrive - ZF Friedrichshafen AG\\Desktop\\mentor_project\\A0079K6529.prj"
    pass
    

if (__name__ == '__main__'):
#    init() #run only when not having running makepy.py previously on your computer
    main()

    
