from layout_ifc import *
from layout_ifc import constants as const

import os,win32com,sys,pythoncom,subprocess
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

def main():
    # optional TBD init
    # this is simple IntelliSense usage example
    # connection to Xpedition Layout usind COM ifc is not established!
    print(f'enum example: {const.epcbAcceptAll}')
    objPcbHazardExplorer : IMGCPCBHazardExplorer = None
    objApplication : IMGCPCBApplication = None
    pcbDoc : IMGCPCBDocument = None
    gfx : IMGCPCBUserLayerGfx = None
    #gfx.Geometry

    objApplication = win32.Dispatch('MGCPCB.ExpeditionPCBApplication', 'IVdApp')
    pcbDoc = GetLicensedDoc(objApplication)

    #Start programming here:
    #This sample script prints the names of all User Layers
    for gfx in pcbDoc.UserLayerGfxs:
         print(f'User Layer Name: {gfx.LayerName}')

if __name__ == "__main__":      
    main()
