from fablink_ifc import *
from fablink_ifc import constants as c

import os, sys, pythoncom
import win32com.client as win32

def GetLicensedDoc(appObj):
        try:
            docObj = appObj.ActiveDocument
            #print docObj
            
        except pythoncom.com_error(hr, msg, exc, arg):
            sys.exit("Terminating script, unable to obtain PCB Document.")

        key = docObj.Validate(0)
        #licenseServer = win32com.client.gencache.EnsureDispatch("MGCPCBAutomationLicensing.Application")
        licenseServer = win32.Dispatch("MGCPCBAutomationLicensing.Application")
        licenseToken = licenseServer.GetToken(key)

        try:
            docObj.Validate(licenseToken)
        except pythoncom.com_error(hr, msg, exc, arg):
            sys.exit("Terminating script, unable to obtain Automation license.")

        return docObj

def run():
    # this is simple IntelliSense usage example
    print(f'enum example: {c.epcbAcceptAll}')
    # this is a number of Annotations so that autocompletion works
    objApplicationpnl : IMGCPCBApplication = None
    pnlDoc : IMGCPCBDocument = None
    objFiducial : IMGCPCBFiducial = None
    objCell : IMGCPCBCell = None
    objCellComp : IMGCPCBComponent = None
    objboard : IMGCPCBBoard = None
    colBoards :IMGCPCBBoards = None                                                 
    objApplicationpcb : IMGCPCBApplication = None
    pcbDoc : IMGCPCBDocument = None                                   
    objApplication : IMGCPCBApplication = None
    pcbDoc : IMGCPCBDocument = None
    
    # PCB Layout project object
    objApplicationpcb = win32.Dispatch('MGCPCB.ExpeditionPCBApplication', 'IVdApp')
    pcbDoc = GetLicensedDoc(objApplicationpcb)

    # FabLink project object
    objApplicationpnl = win32.Dispatch('MGCPCB.FablinkXEApplication', 'IVdApp')
    pnlDoc = GetLicensedDoc(objApplicationpnl)
    
    #Start programming here:
    #This sample script prints the Path of the Fablink project
    path = pnlDoc.Path +'Output'
    print(path)                               
    
def main():
    # optional TBD init
    # init()
    run()

if __name__ == "__main__":        
    main()
