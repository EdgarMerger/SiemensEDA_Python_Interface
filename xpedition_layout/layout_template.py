from layout_ifc import *
import enum_constants as c
from layout_ifc import constants as const

import os,win32com,sys,pythoncom,subprocess
import win32com.client as win32


def run():
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

    const.epcbAcceptAll
    
    cnt = 0
    flag = False

    #Start programming here:
    #This sample script deletes cutouts in a User Layer 
    for gfx in pcbDoc.UserLayerGfxs:
         if flag == True:
             break
         if gfx.LayerName == "planedata_l3": #Sample name of a User_Layer
            if gfx.Geometry.Cutouts.Count > 0:
                 for cutout in gfx.Geometry.Cutouts:                   
                    cutout.Delete() #Delete the cutout. Script is incapable to Delete multiple cutouts for some reason. Script needs to be called as many times as cutouts exist.
                    cnt = cnt + 1
                    print(cnt)
                    
                    flag = True
                    break #Because script can only delete one cutout at a time
                #pass
    #print cnt

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
    run()

if __name__ == "__main__":      
    main()
