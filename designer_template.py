import win32com.client as win32
import sys, os, subprocess
from designer_ifc import constants as c
from designer_ifc import *

WHERE_AM_I, WHO_AM_I=os.path.split(os.path.realpath(__file__))
sys.path.append(WHERE_AM_I)

i = 0
idx = 0

def init():
    print('Running makepy ...')
    result = subprocess.run(['python', f'{WHERE_AM_I}\\mpy.py'], capture_output=True, text=True)
    # print(result)
    
def GetProgIDVersion():
    version_string = ''
    dllApp = win32.Dispatch('MGCPCBReleaseEnvironmentlib.MGCPCBReleaseEnvServer')
    colReleases = dllApp.GetInstalledReleases()
    for objRelease in colReleases:
        print(f'objRel.3 = {objRelease[3]}')
        if (objRelease[3] == 'EEVX.2.13'):
            version_string = objRelease[0]
        
    return version_string


def main():
    
    # this is a simple IntelliSense usage example
    # the following annotation establishes the classes and definitions from designer_ifc.py to the IDE (VScode, Pycharm, etc.) and thus enables autocompletion  
    objApplication : IVdApp = None
    objComponent : IVdComp = None
    
    # the following is an example of how to access the constants
    print(f'enum example: {c.VDM_BLOCK}')

    #objApplication = win32.Dispatch('ViewDraw.Application' + '.' + GetProgIDVersion(), 'IVdApp')
    objApplication = win32.Dispatch('ViewDraw.Application', 'IVdApp')
    strDesignPath = objApplication.GetProjectData().GetProjectPath()
    
    # get name of the design
    strDesign = objApplication.GetProjectData().GetiCDBDesignRootBlock(objApplication.GetActiveDesign())

    if (len(strDesign) == 0):
        strList = objApplication.GetProjectData().GetiCDBDesigns()
        if (len(strList) == 1):
            strDesign = strList[0]
        else:
            print_override('No design open!\nPlease open a schematic of the Board to be processed!\nYour project contains more than one Boards and no schematic is open.')
            exit(-1)
    
    objProjectData = objApplication.GetProjectData()
    objActiveView = objApplication.ActiveView
        
    # Here custom code can be entered
    # e.g. Generate a list of all components from the design and retrieve name of the first component
    lstComponents = objApplication.DesignComponents("", strDesign, "-1", "STD", True)
    objComponent = lstComponents[1] 
    strCompName = objComponent.GetName()

if (__name__ == '__main__'):
#    init() #run only when not having running makepy.py previously on your computer
    main()

    
