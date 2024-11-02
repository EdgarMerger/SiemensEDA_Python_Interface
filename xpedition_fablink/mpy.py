import sys
from win32com.client import makepy

# sys.argv.append('HyperLynxDRC 7.96 Type Library')
sys.argv.append('MGCPCB (AutoActive series) Type Library')
# sys.argv.append('MGCPCBLibDataGrid Active X Control module')
# sys.argv.append('MGCPCBAutomationLicensing Type Library')
# sys.argv.append('MGCPCBEngines Type Library')
# sys.argv.append('MGCPCBReleaseEnvironment 1.0 Type Library')
# sys.argv.append('MGCSDDAddin Tree Type Library')
# sys.argv.append('MGCPCBReleaseEnvironment 1.0 Type Library')
# sys.argv.append('MGCSDDKeyBindSvr')

makepy.main()

# import win32com.client.gencache as gc

# def run():
    # mod = gc.GetModuleForCLSID('{635AAC32-343B-49CE-BED7-37FC07236ED1}')
    # if (mod != None):
    #     print(mod)
