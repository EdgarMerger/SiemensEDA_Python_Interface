import win32com.client as win32
import sys, os, subprocess
from variantmanager_ifc import constants as c
from variantmanager_ifc import *

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
    # the following annotation establishes the classes and definitions from designer_ifc.py to the IDE (VScode, Pycharm, etc.) and thus enables autocompletion  
    objDocument : IMGCVariantMgrDocument = None
    
    # the following is an example of how to access the constants
    #print(f'enum example: {c.VDM_BLOCK}')

    objDocument = win32.Dispatch('MGCVariantMgr.Document', 'IVdApp')

    # Here custom code can be entered
    # e.g. retrieve the number of Variants 

    intNumVariants = objDocument.Variants.Count
    print(f'number of Variants: {intNumVariants}')
    pass
    

if (__name__ == '__main__'):
#    init() #run only when not having running makepy.py previously on your computer
    main()

    
