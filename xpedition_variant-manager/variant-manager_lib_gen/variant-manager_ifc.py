# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.11.6 (tags/v3.11.6:8b6ee5b, Oct  2 2023, 14:57:12) [MSC v.1935 64 bit (AMD64)]
# On Sun Nov  3 00:39:58 2024
'MGCVARIANTMGR Variant Manager Type Library'
makepy_version = '0.5.01'
python_version = 0x30b06f0

import win32com.client.CLSIDToClass, pythoncom, pywintypes
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch

# The following 3 lines may need tweaking for the particular server
# Candidates are pythoncom.Missing, .Empty and .ArgNotFound
defaultNamedOptArg=pythoncom.Empty
defaultNamedNotOptArg=pythoncom.Empty
defaultUnnamedArg=pythoncom.Empty

CLSID = IID('{786637F2-9407-11D2-89D9-0020184077E1}')
MajorVersion = 119
MinorVersion = 0
LibraryFlags = 8
LCID = 0x0

class constants:
	evmgrAccLockConCurrErr        =64         # from enum EVMGRAccessLock
	evmgrAccLockConCurrInfo       =16         # from enum EVMGRAccessLock
	evmgrAccLockConCurrWarn       =32         # from enum EVMGRAccessLock
	evmgrAccLockFMVCtrl           =128        # from enum EVMGRAccessLock
	evmgrAccLockHide              =2          # from enum EVMGRAccessLock
	evmgrAccLockInherit           =8          # from enum EVMGRAccessLock
	evmgrAccLockNone              =1          # from enum EVMGRAccessLock
	evmgrAccLockReadOnly          =4          # from enum EVMGRAccessLock
	evmgrEvChangedChangeType      =3          # from enum EVMGRChangeEventType
	evmgrEvChangedName            =1          # from enum EVMGRChangeEventType
	evmgrEvChangedPartName        =2          # from enum EVMGRChangeEventType
	evmgrEvNewlyAdded             =5          # from enum EVMGRChangeEventType
	evmgrEvRemoved                =4          # from enum EVMGRChangeEventType
	evmgrChangeOperAll            =0          # from enum EVMGRChangeOperation
	evmgrChangeOperReplace        =2          # from enum EVMGRChangeOperation
	evmgrChangeOperUnplace        =1          # from enum EVMGRChangeOperation
	evmgrClientBA                 =7          # from enum EVMGRClientType
	evmgrClientBoardStationRE     =3          # from enum EVMGRClientType
	evmgrClientDA                 =6          # from enum EVMGRClientType
	evmgrClientDC                 =4          # from enum EVMGRClientType
	evmgrClientDV                 =5          # from enum EVMGRClientType
	evmgrClientDxD                =2          # from enum EVMGRClientType
	evmgrClientExpedition         =1          # from enum EVMGRClientType
	evmgrClientGeneric            =0          # from enum EVMGRClientType
	evmgrConCurrRead              =2          # from enum EVMGRConcurrentMode
	evmgrConCurrWrite             =1          # from enum EVMGRConcurrentMode
	evmgrConnSourceCDB            =1          # from enum EVMGRConnectivitySource
	evmgrConnSourceDxdPrj         =4          # from enum EVMGRConnectivitySource
	evmgrConnSourceICDB           =5          # from enum EVMGRConnectivitySource
	evmgrConnSourcePCB            =2          # from enum EVMGRConnectivitySource
	evmgrConnSourcePRJ            =3          # from enum EVMGRConnectivitySource
	evmgrConnSourceUndef          =0          # from enum EVMGRConnectivitySource
	evmgrDStatAllCount            =65535      # from enum EVMGRDocStatisticType
	evmgrDStatFMVCount            =4          # from enum EVMGRDocStatisticType
	evmgrDStatFMVDataCount        =64         # from enum EVMGRDocStatisticType
	evmgrDStatFMVGroupCount       =8          # from enum EVMGRDocStatisticType
	evmgrDStatVariantCount        =1          # from enum EVMGRDocStatisticType
	evmgrDStatVariantDataCount    =16         # from enum EVMGRDocStatisticType
	evmgrDStatVariantGroupCount   =2          # from enum EVMGRDocStatisticType
	evmgrDocumentVmgrDx           =2          # from enum EVMGRDocumentType
	evmgrDocumentVmgrEn           =3          # from enum EVMGRDocumentType
	evmgrDocumentVmgrExp          =1          # from enum EVMGRDocumentType
	evmgrDocumentVmgrRE           =4          # from enum EVMGRDocumentType
	evmgrDialogFMVDefinitions     =2          # from enum EVMGREditorDialog
	evmgrDialogFMVGrid            =1          # from enum EVMGREditorDialog
	evmgrDialogFMVGroups          =3          # from enum EVMGREditorDialog
	evmgrDialogOutputCAD          =8          # from enum EVMGREditorDialog
	evmgrDialogOutputCAE          =7          # from enum EVMGREditorDialog
	evmgrDialogOutputReports      =9          # from enum EVMGREditorDialog
	evmgrDialogVariantDefinitions =5          # from enum EVMGREditorDialog
	evmgrDialogVariantGrid        =4          # from enum EVMGREditorDialog
	evmgrDialogVariantGroups      =6          # from enum EVMGREditorDialog
	evmgrErrBlockCannotReplace    =-2147220827 # from enum EVMGRErrCode
	evmgrErrBlockDataDoesNotExist =-2147220829 # from enum EVMGRErrCode
	evmgrErrBlockDataModCannotCreate=-2147220828 # from enum EVMGRErrCode
	evmgrErrBorderPropModCannotCreate=-2147220826 # from enum EVMGRErrCode
	evmgrErrCannotChangeDefaultGroup=-2147220830 # from enum EVMGRErrCode
	evmgrErrCollAlreadyAdded      =-2147220978 # from enum EVMGRErrCode
	evmgrErrCollIndexOutOfRange   =-2147220979 # from enum EVMGRErrCode
	evmgrErrCollInvalidIndex      =-2147220980 # from enum EVMGRErrCode
	evmgrErrCollItemNotFound      =-2147220977 # from enum EVMGRErrCode
	evmgrErrCollNameNotFound      =-2147220981 # from enum EVMGRErrCode
	evmgrErrCollStringNotAdded    =-2147220976 # from enum EVMGRErrCode
	evmgrErrFMVFunctionAssignmentCannotCreate=-2147220881 # from enum EVMGRErrCode
	evmgrErrFMVFunctionAssignmentDoesNotExist=-2147220880 # from enum EVMGRErrCode
	evmgrErrFMVFunctionAssignmentNotOnDefault=-2147220879 # from enum EVMGRErrCode
	evmgrErrFMVFunctionCannotCreate=-2147220899 # from enum EVMGRErrCode
	evmgrErrFMVFunctionDoesNotExist=-2147220900 # from enum EVMGRErrCode
	evmgrErrFMVFunctionExists     =-2147220901 # from enum EVMGRErrCode
	evmgrErrFMVFunctionGroupCannotCreate=-2147220889 # from enum EVMGRErrCode
	evmgrErrFMVFunctionGroupDoesNotExist=-2147220890 # from enum EVMGRErrCode
	evmgrErrFMVFunctionGroupExists=-2147220891 # from enum EVMGRErrCode
	evmgrErrFMVMatrixConflict1    =-2147220831 # from enum EVMGRErrCode
	evmgrErrFMVPropertyCannotCreate=-2147220859 # from enum EVMGRErrCode
	evmgrErrFMVPropertyConflict1  =-2147220850 # from enum EVMGRErrCode
	evmgrErrFMVPropertyConflict2  =-2147220849 # from enum EVMGRErrCode
	evmgrErrFMVPropertyConflict3  =-2147220848 # from enum EVMGRErrCode
	evmgrErrFMVPropertyConflict4  =-2147220847 # from enum EVMGRErrCode
	evmgrErrFMVPropertyConflict5  =-2147220846 # from enum EVMGRErrCode
	evmgrErrFMVPropertyDoesNotExist=-2147220860 # from enum EVMGRErrCode
	evmgrErrFMVPropertyExists     =-2147220861 # from enum EVMGRErrCode
	evmgrErrInvalidObject         =-2147220990 # from enum EVMGRErrCode
	evmgrErrNoError               =-2147220991 # from enum EVMGRErrCode
	evmgrErrNoModsInReadOnly      =-2147220988 # from enum EVMGRErrCode
	evmgrErrNotesLayersChangeFailed=-2147220825 # from enum EVMGRErrCode
	evmgrErrObjectWasDeleted      =-2147220989 # from enum EVMGRErrCode
	evmgrErrPackageDoesNotExist   =-2147220936 # from enum EVMGRErrCode
	evmgrErrPackageModCannotCreate=-2147220915 # from enum EVMGRErrCode
	evmgrErrPackageModDoesNotExist=-2147220916 # from enum EVMGRErrCode
	evmgrErrSymbolDoesNotExist    =-2147220941 # from enum EVMGRErrCode
	evmgrErrSymbolInfoRecCannotCreate=-2147220869 # from enum EVMGRErrCode
	evmgrErrSymbolInfoRecDoesNotExist=-2147220870 # from enum EVMGRErrCode
	evmgrErrSymbolInfoRecExists   =-2147220871 # from enum EVMGRErrCode
	evmgrErrSymbolModCannotCreate =-2147220929 # from enum EVMGRErrCode
	evmgrErrSymbolModDoesNotExist =-2147220930 # from enum EVMGRErrCode
	evmgrErrUndefinedError        =-2147220987 # from enum EVMGRErrCode
	evmgrErrVariantAssignmentCannotCreate=-2147220911 # from enum EVMGRErrCode
	evmgrErrVariantAssignmentDoesNotExist=-2147220910 # from enum EVMGRErrCode
	evmgrErrVariantAssignmentNotOnDefault=-2147220909 # from enum EVMGRErrCode
	evmgrErrVariantCannotCreate   =-2147220959 # from enum EVMGRErrCode
	evmgrErrVariantDoesNotExist   =-2147220960 # from enum EVMGRErrCode
	evmgrErrVariantExists         =-2147220961 # from enum EVMGRErrCode
	evmgrErrVariantGroupCannotCreate=-2147220949 # from enum EVMGRErrCode
	evmgrErrVariantGroupDoesNotExist=-2147220950 # from enum EVMGRErrCode
	evmgrErrVariantGroupExists    =-2147220951 # from enum EVMGRErrCode
	evmgrFlowDefault              =0          # from enum EVMGRFlowID
	eymgrFlowPADS                 =1          # from enum EVMGRFlowID
	evmgrFMVFuncExclude           =2          # from enum EVMGRFuncChangeOperation
	evmgrFMVFuncInclude           =1          # from enum EVMGRFuncChangeOperation
	evmgrFMVFuncNone              =0          # from enum EVMGRFuncChangeOperation
	evmgrFMVFuncPNRpl             =4          # from enum EVMGRFuncChangeOperation
	evmgrFMVFunction              =1          # from enum EVMGRFunctionType
	evmgrInternalFunction         =2          # from enum EVMGRFunctionType
	evmgrGroupTypeFunction        =1          # from enum EVMGRGroupType
	evmgrGroupTypeVariant         =2          # from enum EVMGRGroupType
	evmgrITEvAddBlock             =1          # from enum EVMGRITEventType
	evmgrITEvAddCesComp           =2          # from enum EVMGRITEventType
	evmgrITEvAddComp              =3          # from enum EVMGRITEventType
	evmgrITEvBroadcastMessage     =50         # from enum EVMGRITEventType
	evmgrITEvChange               =80         # from enum EVMGRITEventType
	evmgrITEvDeleteAllCESComps    =21         # from enum EVMGRITEventType
	evmgrITEvDeleteAttribute      =14         # from enum EVMGRITEventType
	evmgrITEvDeleteBlock          =11         # from enum EVMGRITEventType
	evmgrITEvDeleteCesComp        =12         # from enum EVMGRITEventType
	evmgrITEvDeleteComp           =13         # from enum EVMGRITEventType
	evmgrITEvFlattenNetlist       =40         # from enum EVMGRITEventType
	evmgrITEvSetCompAttr          =30         # from enum EVMGRITEventType
	evmgrITEvUndefined            =0          # from enum EVMGRITEventType
	evmgrITMessExitGUI            =41         # from enum EVMGRITMessageType
	evmgrITMessOpenGUI            =40         # from enum EVMGRITMessageType
	evmgrITMessQryEditMode        =20         # from enum EVMGRITMessageType
	evmgrITMessReplyQryEditMode   =21         # from enum EVMGRITMessageType
	evmgrITMessReplyReqEditDenied =12         # from enum EVMGRITMessageType
	evmgrITMessReplyReqEditGranted=11         # from enum EVMGRITMessageType
	evmgrITMessReqEdit            =10         # from enum EVMGRITMessageType
	evmgrITMessSaveToDMS          =30         # from enum EVMGRITMessageType
	evmgrITMessStoppedEdit        =13         # from enum EVMGRITMessageType
	evmgrITMessUndefined          =0          # from enum EVMGRITMessageType
	evmgrLoadSelectAll            =268435455  # from enum EVMGRLoadSelection
	evmgrLoadSelectFunctionGroups =32         # from enum EVMGRLoadSelection
	evmgrLoadSelectFunctionMods   =64         # from enum EVMGRLoadSelection
	evmgrLoadSelectFunctions      =16         # from enum EVMGRLoadSelection
	evmgrLoadSelectReuseBlockProps=128        # from enum EVMGRLoadSelection
	evmgrLoadSelectTimeStamps     =1          # from enum EVMGRLoadSelection
	evmgrLoadSelectVariantGroups  =4          # from enum EVMGRLoadSelection
	evmgrLoadSelectVariantMods    =8          # from enum EVMGRLoadSelection
	evmgrLoadSelectVariants       =2          # from enum EVMGRLoadSelection
	evmgrMapAllFlags              =16777215   # from enum EVMGRMappingFlags
	evmgrMapDoNotMerge            =1          # from enum EVMGRMappingFlags
	evmgrMapNoAction              =0          # from enum EVMGRMappingFlags
	evmgrMapOrgToNew              =2          # from enum EVMGRMappingFlags
	evmgrNewIndex                 =16         # from enum EVMGRObjectOperation
	evmgrOperAssChange            =6          # from enum EVMGRObjectOperation
	evmgrOperAssignmentChange     =11         # from enum EVMGRObjectOperation
	evmgrOperAssignmentDelete     =14         # from enum EVMGRObjectOperation
	evmgrOperBlockDataModDelete   =15         # from enum EVMGRObjectOperation
	evmgrOperChange               =1          # from enum EVMGRObjectOperation
	evmgrOperDelete               =3          # from enum EVMGRObjectOperation
	evmgrOperDescChange           =4          # from enum EVMGRObjectOperation
	evmgrOperNameChange           =1          # from enum EVMGRObjectOperation
	evmgrOperNew                  =2          # from enum EVMGRObjectOperation
	evmgrOperNumberChange         =5          # from enum EVMGRObjectOperation
	evmgrOperPackModDelete        =9          # from enum EVMGRObjectOperation
	evmgrOperSymbolModDelete      =9          # from enum EVMGRObjectOperation
	evmgrOperTransactionEnd       =8          # from enum EVMGRObjectOperation
	evmgrOperTransactionStart     =7          # from enum EVMGRObjectOperation
	evmgrOperTypeChange           =10         # from enum EVMGRObjectOperation
	evmgrParam1                   =12         # from enum EVMGRObjectOperation
	evmgrParam2                   =13         # from enum EVMGRObjectOperation
	evmgrObjBlock                 =114        # from enum EVMGRObjectType
	evmgrObjBlockDataMod          =14         # from enum EVMGRObjectType
	evmgrObjBlockDataModEx        =76         # from enum EVMGRObjectType
	evmgrObjBorderAttributeModification=81         # from enum EVMGRObjectType
	evmgrObjBorderProperty        =116        # from enum EVMGRObjectType
	evmgrObjCLProperty            =15         # from enum EVMGRObjectType
	evmgrObjConfig                =73         # from enum EVMGRObjectType
	evmgrObjDocument              =10         # from enum EVMGRObjectType
	evmgrObjFMVProperty           =13         # from enum EVMGRObjectType
	evmgrObjFMVPropertyEx         =79         # from enum EVMGRObjectType
	evmgrObjFuncionAssignment     =12         # from enum EVMGRObjectType
	evmgrObjFunction              =4          # from enum EVMGRObjectType
	evmgrObjFunctionEx            =78         # from enum EVMGRObjectType
	evmgrObjFunctionGroup         =5          # from enum EVMGRObjectType
	evmgrObjGeneric               =1          # from enum EVMGRObjectType
	evmgrObjGroup                 =69         # from enum EVMGRObjectType
	evmgrObjItemColl              =9          # from enum EVMGRObjectType
	evmgrObjMechanicalComponentDefinition=80         # from enum EVMGRObjectType
	evmgrObjMechanicalComponentModification=74         # from enum EVMGRObjectType
	evmgrObjPackage               =113        # from enum EVMGRObjectType
	evmgrObjPackageMod            =6          # from enum EVMGRObjectType
	evmgrObjPackageModEx          =75         # from enum EVMGRObjectType
	evmgrObjReusedBlock           =115        # from enum EVMGRObjectType
	evmgrObjSymbInfo              =7          # from enum EVMGRObjectType
	evmgrObjSymbol                =8          # from enum EVMGRObjectType
	evmgrObjSymbolLocation        =112        # from enum EVMGRObjectType
	evmgrObjVariant               =2          # from enum EVMGRObjectType
	evmgrObjVariantAssignment     =11         # from enum EVMGRObjectType
	evmgrObjVariantEx             =77         # from enum EVMGRObjectType
	evmgrObjVariantGroup          =3          # from enum EVMGRObjectType
	evmgrPackProcBegin            =1          # from enum EVMGRPackProcessState
	evmgrPackProcEndError         =3          # from enum EVMGRPackProcessState
	evmgrPackProcEndOk            =2          # from enum EVMGRPackProcessState
	evmgrPackProcUndefined        =0          # from enum EVMGRPackProcessState
	evmgrPackStateOK              =0          # from enum EVMGRPackageState
	evmgrPackStateRemoved         =1          # from enum EVMGRPackageState
	evmgrPackStateRepackaged      =2          # from enum EVMGRPackageState
	evmgrPackStateRequiresRepackage=3          # from enum EVMGRPackageState
	evmgrJumper                   =4          # from enum EVMGRPackageType
	evmgrMechanicalCell           =1          # from enum EVMGRPackageType
	evmgrMechanicalCellNested     =3          # from enum EVMGRPackageType
	evmgrNested                   =2          # from enum EVMGRPackageType
	evmgrPackage                  =0          # from enum EVMGRPackageType
	evmgrReconAsk                 =3          # from enum EVMGRReconsileMode
	evmgrReconBEWins              =6          # from enum EVMGRReconsileMode
	evmgrReconDefault             =4          # from enum EVMGRReconsileMode
	evmgrReconFEWins              =5          # from enum EVMGRReconsileMode
	evmgrRptDataFMV               =1          # from enum EVMGRReportDataType
	evmgrRptDataFMVMatrix         =2          # from enum EVMGRReportDataType
	evmgrRptDataPhysical          =0          # from enum EVMGRReportDataType
	evmgrRptDataUser              =3          # from enum EVMGRReportDataType
	evmgrReuseAccessRead          =1          # from enum EVMGRReuseAccessMode
	evmgrReuseAccessWrite         =2          # from enum EVMGRReuseAccessMode
	evmgrReuseMergeNever          =0          # from enum EVMGRReuseMergeMode
	evmgrReuseMergeOnce           =1          # from enum EVMGRReuseMergeMode
	evmgrReuseMergeResync         =2          # from enum EVMGRReuseMergeMode
	evmgrMergeStatInvalidLibSource=3          # from enum EVMGRReuseMergeStatus
	evmgrMergeStatMustMerge       =2          # from enum EVMGRReuseMergeStatus
	evmgrMergeStatMustUpdate      =1          # from enum EVMGRReuseMergeStatus
	evmgrMergeStatNotRequired     =4          # from enum EVMGRReuseMergeStatus
	evmgrMergeStatOK              =0          # from enum EVMGRReuseMergeStatus
	eVmgrDSymbDashLS              =6          # from enum EVMGRSymbDisplay
	eVmgrDSymbMarkup              =4          # from enum EVMGRSymbDisplay
	eVmgrDSymbPropsUpdate         =5          # from enum EVMGRSymbDisplay
	eVmgrDSymbReplace             =7          # from enum EVMGRSymbDisplay
	evmgrDSymbColor               =3          # from enum EVMGRSymbDisplay
	evmgrDSymbNoAction            =0          # from enum EVMGRSymbDisplay
	evmgrDSymbRemCleanWires       =2          # from enum EVMGRSymbDisplay
	evmgrDSymbRemKeepWires        =1          # from enum EVMGRSymbDisplay
	evmgrSymbolTypeBlock          =2          # from enum EVMGRSymbolType
	evmgrSymbolTypeBorder         =4          # from enum EVMGRSymbolType
	evmgrSymbolTypeReusedBlock    =3          # from enum EVMGRSymbolType
	evmgrSymbolTypeSymbol         =1          # from enum EVMGRSymbolType
	evmgrTstampDocument           =0          # from enum EVMGRTimestampType
	evmgrTstampVariantDRC         =1          # from enum EVMGRTimestampType
	evmgrFMVVariant               =1          # from enum EVMGRVariantType
	evmgrPhysicalVariant          =2          # from enum EVMGRVariantType
	evmgrDBTypeCDB                =2          # from enum EVMGRVariantsDBType
	evmgrDBTypeCurrent            =1          # from enum EVMGRVariantsDBType
	evmgrDBTypeUndefined          =0          # from enum EVMGRVariantsDBType
	evmgrDBTypeVarHKP             =4          # from enum EVMGRVariantsDBType
	evmgrDBTypeiCDB               =3          # from enum EVMGRVariantsDBType
	evmgrDBTypeiCDB2              =5          # from enum EVMGRVariantsDBType
	evmgrDBTypeiCDBHKP            =6          # from enum EVMGRVariantsDBType
	evmgrWriteFmtHKP              =0          # from enum EVMGRWriteFormat
	evmgrWriteFmtTabular          =1          # from enum EVMGRWriteFormat

from win32com.client import DispatchBaseClass
class IMGCVariantMgrApplication(DispatchBaseClass):
	'Variant manager application object'
	CLSID = IID('{7866380D-9407-11D2-89D9-0020184077E1}')
	coclass_clsid = IID('{7866380D-9407-20D2-89D9-0020184077E1}')

	def CompareUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Compares a UID with the UID of the object. Returns true if equal.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((19, 1), (19, 1), (19, 1)),userID
			, objectID, objectType)

	def GetUID(self, userID=pythoncom.Missing, objectID=pythoncom.Missing, objectType=pythoncom.Missing):
		'Gets the UID of an object. Returns false if the UID is invalid.'
		return self._ApplyTypes_(6, 1, (11, 0), ((16403, 2), (16403, 2), (16403, 2)), 'GetUID', None,userID
			, objectID, objectType)

	def IncModificationCount(self, value=1):
		'Increments the modification count'
		return self._oleobj_.InvokeTypes(23, LCID, 1, (2, 0), ((2, 49),),value
			)

	def IsValid(self):
		'Returns the internal (CPP) index of the X-Object'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), (),)

	# Result is of type IMGCVariantMgrDocument
	def OpenDocument(self, jobPath=defaultNamedNotOptArg, revision=defaultNamedNotOptArg, clientType=0):
		'Opens a document'
		ret = self._oleobj_.InvokeTypes(101, LCID, 1, (9, 0), ((8, 1), (8, 1), (3, 49)),jobPath
			, revision, clientType)
		if ret is not None:
			ret = Dispatch(ret, 'OpenDocument', '{78663807-9407-11D2-89D9-0020184077E1}')
		return ret

	def SetInternalValue(self, id=defaultNamedNotOptArg, parm1=defaultNamedOptArg, parm2=defaultNamedOptArg, parm3=defaultNamedOptArg):
		'Sets an internal value on an object'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (2, 0), ((8, 1), (12, 17), (12, 17), (12, 17)),id
			, parm1, parm2, parm3)

	def SetUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Sets the UID of an object. Returns false if the UID is invalid.'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (11, 0), ((19, 1), (19, 1), (19, 1)),userID
			, objectID, objectType)

	_prop_map_get_ = {
		"AccessLock": (5, 2, (3, 0), (), "AccessLock", None),
		# Method 'Documents' returns object of type 'IMGCVariantMgrDocuments'
		"Documents": (103, 2, (9, 0), (), "Documents", '{7866380E-9407-11D2-89D9-0020184077E1}'),
		"InternalIndex": (2, 2, (3, 0), (), "InternalIndex", None),
		"ModificationCount": (20, 2, (2, 0), (), "ModificationCount", None),
		"ModificationCountEx": (24, 2, (3, 0), (), "ModificationCountEx", None),
		"ModificationCountLock": (21, 2, (11, 0), (), "ModificationCountLock", None),
		"Name": (30, 2, (8, 0), (), "Name", None),
		"Parent": (1, 2, (9, 0), (), "Parent", None),
		# Method 'RootIF' returns object of type 'IMGCVariantMgrDocument'
		"RootIF": (22, 2, (9, 0), (), "RootIF", '{78663807-9407-11D2-89D9-0020184077E1}'),
	}
	_prop_map_put_ = {
		"AccessLock": ((5, LCID, 4, 0),()),
		"ModificationCount": ((20, LCID, 4, 0),()),
		"ModificationCountEx": ((24, LCID, 4, 0),()),
		"ModificationCountLock": ((21, LCID, 4, 0),()),
		"Name": ((30, LCID, 4, 0),()),
		"Parent": ((1, LCID, 8, 0),()),
	}

	AccessLock: str # read/write
	Documents: str # IMGCVariantMgrDocuments; read_only
	InternalIndex: str # read_only
	ModificationCount: str # read/write
	ModificationCountEx: str # read/write
	ModificationCountLock: str # read/write
	Name: str # read/write
	Parent: str # read/write
	RootIF: str # IMGCVariantMgrDocument; read_only

	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMGCVariantMgrBPropModsUtility(DispatchBaseClass):
	'Variant manager border property modifications utitity object.'
	CLSID = IID('{BC1CC3A2-E4A4-4A3D-B400-50F80D7D8A39}')
	coclass_clsid = IID('{9664D362-EAD1-41A5-B465-7D71FE1527F1}')

	# Result is of type IMGCVariantMgrBorderPropModifications
	# The method BorderPropModifications is actually a property, but must be used as a method to correctly pass the arguments
	def BorderPropModifications(self, filter=defaultNamedNotOptArg):
		'Returns the package modifications for the variants.'
		ret = self._oleobj_.InvokeTypes(103, LCID, 2, (9, 0), ((12, 1),),filter
			)
		if ret is not None:
			ret = Dispatch(ret, 'BorderPropModifications', '{72982CC0-8617-400A-9772-5DF126EA582A}')
		return ret

	def CompareUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Compares a UID with the UID of the object. Returns true if equal.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((19, 1), (19, 1), (19, 1)),userID
			, objectID, objectType)

	# Result is of type IMGCVariantMgrBorderPropModification
	def FindBorderPropModification(self, prpName=defaultNamedNotOptArg, variantDef=defaultNamedNotOptArg, symbolDef=defaultNamedNotOptArg):
		'Finds a symbol modification record'
		ret = self._oleobj_.InvokeTypes(102, LCID, 1, (9, 0), ((8, 1), (12, 1), (12, 1)),prpName
			, variantDef, symbolDef)
		if ret is not None:
			ret = Dispatch(ret, 'FindBorderPropModification', '{22D9A8DA-F507-43FD-BA22-6DB8FEA436F2}')
		return ret

	# Result is of type IMGCVariantMgrBorderPropModification
	def FindBorderPropModificationByUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Finds a package modification record'
		ret = self._oleobj_.InvokeTypes(104, LCID, 1, (9, 0), ((3, 1), (3, 1), (3, 1)),userID
			, objectID, objectType)
		if ret is not None:
			ret = Dispatch(ret, 'FindBorderPropModificationByUID', '{22D9A8DA-F507-43FD-BA22-6DB8FEA436F2}')
		return ret

	def GetUID(self, userID=pythoncom.Missing, objectID=pythoncom.Missing, objectType=pythoncom.Missing):
		'Gets the UID of an object. Returns false if the UID is invalid.'
		return self._ApplyTypes_(6, 1, (11, 0), ((16403, 2), (16403, 2), (16403, 2)), 'GetUID', None,userID
			, objectID, objectType)

	def IsValid(self):
		'Returns the internal (CPP) index of the X-Object'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), (),)

	# Result is of type IMGCVariantMgrBorderPropModification
	def PutBorderPropModification(self, variantDefinition=defaultNamedNotOptArg, symbolDefinition=defaultNamedNotOptArg, prpName=defaultNamedNotOptArg, prpValue=defaultNamedNotOptArg):
		'Creates a new border property modification.'
		ret = self._oleobj_.InvokeTypes(101, LCID, 1, (9, 0), ((12, 1), (12, 1), (8, 1), (8, 1)),variantDefinition
			, symbolDefinition, prpName, prpValue)
		if ret is not None:
			ret = Dispatch(ret, 'PutBorderPropModification', '{22D9A8DA-F507-43FD-BA22-6DB8FEA436F2}')
		return ret

	def SetInternalValue(self, id=defaultNamedNotOptArg, parm1=defaultNamedOptArg, parm2=defaultNamedOptArg, parm3=defaultNamedOptArg):
		'Sets an internal value on an object'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (2, 0), ((8, 1), (12, 17), (12, 17), (12, 17)),id
			, parm1, parm2, parm3)

	def SetUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Sets the UID of an object. Returns false if the UID is invalid.'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (11, 0), ((19, 1), (19, 1), (19, 1)),userID
			, objectID, objectType)

	_prop_map_get_ = {
		"AccessLock": (5, 2, (3, 0), (), "AccessLock", None),
		"InternalIndex": (2, 2, (3, 0), (), "InternalIndex", None),
		"Parent": (1, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
		"AccessLock": ((5, LCID, 4, 0),()),
		"Parent": ((1, LCID, 8, 0),()),
	}

	AccessLock: str # read/write
	InternalIndex: str # read_only
	Parent: str # read/write

	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMGCVariantMgrBaseBlock(DispatchBaseClass):
	'Base block interface definition'
	CLSID = IID('{D1B4AC05-40EE-4F0E-8C27-49D6BEC83908}')
	coclass_clsid = None

	def CompareUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Compares a UID with the UID of the object. Returns true if equal.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((19, 1), (19, 1), (19, 1)),userID
			, objectID, objectType)

	def GetUID(self, userID=pythoncom.Missing, objectID=pythoncom.Missing, objectType=pythoncom.Missing):
		'Gets the UID of an object. Returns false if the UID is invalid.'
		return self._ApplyTypes_(6, 1, (11, 0), ((16403, 2), (16403, 2), (16403, 2)), 'GetUID', None,userID
			, objectID, objectType)

	def IncModificationCount(self, value=1):
		'Increments the modification count'
		return self._oleobj_.InvokeTypes(23, LCID, 1, (2, 0), ((2, 49),),value
			)

	def IsValid(self):
		'Returns the internal (CPP) index of the X-Object'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), (),)

	def SetInternalValue(self, id=defaultNamedNotOptArg, parm1=defaultNamedOptArg, parm2=defaultNamedOptArg, parm3=defaultNamedOptArg):
		'Sets an internal value on an object'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (2, 0), ((8, 1), (12, 17), (12, 17), (12, 17)),id
			, parm1, parm2, parm3)

	def SetUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Sets the UID of an object. Returns false if the UID is invalid.'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (11, 0), ((19, 1), (19, 1), (19, 1)),userID
			, objectID, objectType)

	_prop_map_get_ = {
		"AccessLock": (5, 2, (3, 0), (), "AccessLock", None),
		# Method 'BlockData' returns object of type 'IMGCVariantMgrBlockData'
		"BlockData": (101, 2, (9, 0), (), "BlockData", '{7FE7FAB6-7B3B-46CB-970A-0010103AD7E3}'),
		"InternalIndex": (2, 2, (3, 0), (), "InternalIndex", None),
		"ModificationCount": (20, 2, (2, 0), (), "ModificationCount", None),
		"ModificationCountEx": (24, 2, (3, 0), (), "ModificationCountEx", None),
		"ModificationCountLock": (21, 2, (11, 0), (), "ModificationCountLock", None),
		"Name": (30, 2, (8, 0), (), "Name", None),
		"Parent": (1, 2, (9, 0), (), "Parent", None),
		# Method 'RootIF' returns object of type 'IMGCVariantMgrDocument'
		"RootIF": (22, 2, (9, 0), (), "RootIF", '{78663807-9407-11D2-89D9-0020184077E1}'),
	}
	_prop_map_put_ = {
		"AccessLock": ((5, LCID, 4, 0),()),
		"ModificationCount": ((20, LCID, 4, 0),()),
		"ModificationCountEx": ((24, LCID, 4, 0),()),
		"ModificationCountLock": ((21, LCID, 4, 0),()),
		"Name": ((30, LCID, 4, 0),()),
		"Parent": ((1, LCID, 8, 0),()),
	}

	AccessLock: str # read/write
	BlockData: str # IMGCVariantMgrBlockData; read_only
	InternalIndex: str # read_only
	ModificationCount: str # read/write
	ModificationCountEx: str # read/write
	ModificationCountLock: str # read/write
	Name: str # read/write
	Parent: str # read/write
	RootIF: str # IMGCVariantMgrDocument; read_only

	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMGCVariantMgrBaseCollection(DispatchBaseClass):
	'Variant manager base collection object'
	CLSID = IID('{786637F1-9407-11D2-89D9-0020184077E1}')
	coclass_clsid = None

	def CompareUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Compares a UID with the UID of the object. Returns true if equal.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((19, 1), (19, 1), (19, 1)),userID
			, objectID, objectType)

	def GetUID(self, userID=pythoncom.Missing, objectID=pythoncom.Missing, objectType=pythoncom.Missing):
		'Gets the UID of an object. Returns false if the UID is invalid.'
		return self._ApplyTypes_(6, 1, (11, 0), ((16403, 2), (16403, 2), (16403, 2)), 'GetUID', None,userID
			, objectID, objectType)

	def IncModificationCount(self, value=1):
		'Increments the modification count'
		return self._oleobj_.InvokeTypes(23, LCID, 1, (2, 0), ((2, 49),),value
			)

	def IsValid(self):
		'Returns the internal (CPP) index of the X-Object'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), (),)

	def Remove(self, index=defaultNamedNotOptArg):
		'Removes an object from the collection.'
		return self._oleobj_.InvokeTypes(31, LCID, 1, (24, 0), ((12, 1),),index
			)

	def SetInternalValue(self, id=defaultNamedNotOptArg, parm1=defaultNamedOptArg, parm2=defaultNamedOptArg, parm3=defaultNamedOptArg):
		'Sets an internal value on an object'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (2, 0), ((8, 1), (12, 17), (12, 17), (12, 17)),id
			, parm1, parm2, parm3)

	def SetUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Sets the UID of an object. Returns false if the UID is invalid.'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (11, 0), ((19, 1), (19, 1), (19, 1)),userID
			, objectID, objectType)

	def Sort(self, sortKey=defaultNamedOptArg):
		'Sorts the collection.'
		return self._oleobj_.InvokeTypes(32, LCID, 1, (24, 0), ((12, 17),),sortKey
			)

	_prop_map_get_ = {
		"AccessLock": (5, 2, (3, 0), (), "AccessLock", None),
		"Count": (30, 2, (3, 0), (), "Count", None),
		"InternalIndex": (2, 2, (3, 0), (), "InternalIndex", None),
		"ModificationCount": (20, 2, (2, 0), (), "ModificationCount", None),
		"ModificationCountEx": (24, 2, (3, 0), (), "ModificationCountEx", None),
		"ModificationCountLock": (21, 2, (11, 0), (), "ModificationCountLock", None),
		"Parent": (1, 2, (9, 0), (), "Parent", None),
		# Method 'RootIF' returns object of type 'IMGCVariantMgrDocument'
		"RootIF": (22, 2, (9, 0), (), "RootIF", '{78663807-9407-11D2-89D9-0020184077E1}'),
	}
	_prop_map_put_ = {
		"AccessLock": ((5, LCID, 4, 0),()),
		"ModificationCount": ((20, LCID, 4, 0),()),
		"ModificationCountEx": ((24, LCID, 4, 0),()),
		"ModificationCountLock": ((21, LCID, 4, 0),()),
		"Parent": ((1, LCID, 8, 0),()),
	}

	AccessLock: str # read/write
	Count: int # read_only
	InternalIndex: str # read_only
	ModificationCount: str # read/write
	ModificationCountEx: str # read/write
	ModificationCountLock: str # read/write
	Parent: str # read/write
	RootIF: str # IMGCVariantMgrDocument; read_only

	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(30, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IMGCVariantMgrBaseGroup(DispatchBaseClass):
	'Variant manager base group object'
	CLSID = IID('{BFA4726B-E7D0-48E5-A73A-B5C216E8A3BA}')
	coclass_clsid = None

	def CompareUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Compares a UID with the UID of the object. Returns true if equal.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((19, 1), (19, 1), (19, 1)),userID
			, objectID, objectType)

	def GetUID(self, userID=pythoncom.Missing, objectID=pythoncom.Missing, objectType=pythoncom.Missing):
		'Gets the UID of an object. Returns false if the UID is invalid.'
		return self._ApplyTypes_(6, 1, (11, 0), ((16403, 2), (16403, 2), (16403, 2)), 'GetUID', None,userID
			, objectID, objectType)

	def IncModificationCount(self, value=1):
		'Increments the modification count'
		return self._oleobj_.InvokeTypes(23, LCID, 1, (2, 0), ((2, 49),),value
			)

	def IsValid(self):
		'Returns the internal (CPP) index of the X-Object'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), (),)

	def SetInternalValue(self, id=defaultNamedNotOptArg, parm1=defaultNamedOptArg, parm2=defaultNamedOptArg, parm3=defaultNamedOptArg):
		'Sets an internal value on an object'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (2, 0), ((8, 1), (12, 17), (12, 17), (12, 17)),id
			, parm1, parm2, parm3)

	def SetUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Sets the UID of an object. Returns false if the UID is invalid.'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (11, 0), ((19, 1), (19, 1), (19, 1)),userID
			, objectID, objectType)

	_prop_map_get_ = {
		"AccessLock": (5, 2, (3, 0), (), "AccessLock", None),
		"Description": (101, 2, (8, 0), (), "Description", None),
		"InternalIndex": (2, 2, (3, 0), (), "InternalIndex", None),
		"ModificationCount": (20, 2, (2, 0), (), "ModificationCount", None),
		"ModificationCountEx": (24, 2, (3, 0), (), "ModificationCountEx", None),
		"ModificationCountLock": (21, 2, (11, 0), (), "ModificationCountLock", None),
		"Name": (30, 2, (8, 0), (), "Name", None),
		"Parent": (1, 2, (9, 0), (), "Parent", None),
		# Method 'RootIF' returns object of type 'IMGCVariantMgrDocument'
		"RootIF": (22, 2, (9, 0), (), "RootIF", '{78663807-9407-11D2-89D9-0020184077E1}'),
	}
	_prop_map_put_ = {
		"AccessLock": ((5, LCID, 4, 0),()),
		"Description": ((101, LCID, 4, 0),()),
		"ModificationCount": ((20, LCID, 4, 0),()),
		"ModificationCountEx": ((24, LCID, 4, 0),()),
		"ModificationCountLock": ((21, LCID, 4, 0),()),
		"Name": ((30, LCID, 4, 0),()),
		"Parent": ((1, LCID, 8, 0),()),
	}

	AccessLock: str # read/write
	Description: str # read/write
	InternalIndex: str # read_only
	ModificationCount: str # read/write
	ModificationCountEx: str # read/write
	ModificationCountLock: str # read/write
	Name: str # read/write
	Parent: str # read/write
	RootIF: str # IMGCVariantMgrDocument; read_only

	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMGCVariantMgrBaseModNameObject(DispatchBaseClass):
	'The base object for all variant manager objects with name and mod support'
	CLSID = IID('{82CD5AB9-9407-11D2-89D9-0020184077E1}')
	coclass_clsid = None

	def CompareUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Compares a UID with the UID of the object. Returns true if equal.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((19, 1), (19, 1), (19, 1)),userID
			, objectID, objectType)

	def GetUID(self, userID=pythoncom.Missing, objectID=pythoncom.Missing, objectType=pythoncom.Missing):
		'Gets the UID of an object. Returns false if the UID is invalid.'
		return self._ApplyTypes_(6, 1, (11, 0), ((16403, 2), (16403, 2), (16403, 2)), 'GetUID', None,userID
			, objectID, objectType)

	def IncModificationCount(self, value=1):
		'Increments the modification count'
		return self._oleobj_.InvokeTypes(23, LCID, 1, (2, 0), ((2, 49),),value
			)

	def IsValid(self):
		'Returns the internal (CPP) index of the X-Object'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), (),)

	def SetInternalValue(self, id=defaultNamedNotOptArg, parm1=defaultNamedOptArg, parm2=defaultNamedOptArg, parm3=defaultNamedOptArg):
		'Sets an internal value on an object'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (2, 0), ((8, 1), (12, 17), (12, 17), (12, 17)),id
			, parm1, parm2, parm3)

	def SetUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Sets the UID of an object. Returns false if the UID is invalid.'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (11, 0), ((19, 1), (19, 1), (19, 1)),userID
			, objectID, objectType)

	_prop_map_get_ = {
		"AccessLock": (5, 2, (3, 0), (), "AccessLock", None),
		"InternalIndex": (2, 2, (3, 0), (), "InternalIndex", None),
		"ModificationCount": (20, 2, (2, 0), (), "ModificationCount", None),
		"ModificationCountEx": (24, 2, (3, 0), (), "ModificationCountEx", None),
		"ModificationCountLock": (21, 2, (11, 0), (), "ModificationCountLock", None),
		"Name": (30, 2, (8, 0), (), "Name", None),
		"Parent": (1, 2, (9, 0), (), "Parent", None),
		# Method 'RootIF' returns object of type 'IMGCVariantMgrDocument'
		"RootIF": (22, 2, (9, 0), (), "RootIF", '{78663807-9407-11D2-89D9-0020184077E1}'),
	}
	_prop_map_put_ = {
		"AccessLock": ((5, LCID, 4, 0),()),
		"ModificationCount": ((20, LCID, 4, 0),()),
		"ModificationCountEx": ((24, LCID, 4, 0),()),
		"ModificationCountLock": ((21, LCID, 4, 0),()),
		"Name": ((30, LCID, 4, 0),()),
		"Parent": ((1, LCID, 8, 0),()),
	}

	AccessLock: str # read/write
	InternalIndex: str # read_only
	ModificationCount: str # read/write
	ModificationCountEx: str # read/write
	ModificationCountLock: str # read/write
	Name: str # read/write
	Parent: str # read/write
	RootIF: str # IMGCVariantMgrDocument; read_only

	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMGCVariantMgrBaseModObject(DispatchBaseClass):
	'The base object for all variant manager objects (with modification support)'
	CLSID = IID('{786637EF-9407-11D2-89D9-0020184077E1}')
	coclass_clsid = None

	def CompareUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Compares a UID with the UID of the object. Returns true if equal.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((19, 1), (19, 1), (19, 1)),userID
			, objectID, objectType)

	def GetUID(self, userID=pythoncom.Missing, objectID=pythoncom.Missing, objectType=pythoncom.Missing):
		'Gets the UID of an object. Returns false if the UID is invalid.'
		return self._ApplyTypes_(6, 1, (11, 0), ((16403, 2), (16403, 2), (16403, 2)), 'GetUID', None,userID
			, objectID, objectType)

	def IncModificationCount(self, value=1):
		'Increments the modification count'
		return self._oleobj_.InvokeTypes(23, LCID, 1, (2, 0), ((2, 49),),value
			)

	def IsValid(self):
		'Returns the internal (CPP) index of the X-Object'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), (),)

	def SetInternalValue(self, id=defaultNamedNotOptArg, parm1=defaultNamedOptArg, parm2=defaultNamedOptArg, parm3=defaultNamedOptArg):
		'Sets an internal value on an object'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (2, 0), ((8, 1), (12, 17), (12, 17), (12, 17)),id
			, parm1, parm2, parm3)

	def SetUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Sets the UID of an object. Returns false if the UID is invalid.'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (11, 0), ((19, 1), (19, 1), (19, 1)),userID
			, objectID, objectType)

	_prop_map_get_ = {
		"AccessLock": (5, 2, (3, 0), (), "AccessLock", None),
		"InternalIndex": (2, 2, (3, 0), (), "InternalIndex", None),
		"ModificationCount": (20, 2, (2, 0), (), "ModificationCount", None),
		"ModificationCountEx": (24, 2, (3, 0), (), "ModificationCountEx", None),
		"ModificationCountLock": (21, 2, (11, 0), (), "ModificationCountLock", None),
		"Parent": (1, 2, (9, 0), (), "Parent", None),
		# Method 'RootIF' returns object of type 'IMGCVariantMgrDocument'
		"RootIF": (22, 2, (9, 0), (), "RootIF", '{78663807-9407-11D2-89D9-0020184077E1}'),
	}
	_prop_map_put_ = {
		"AccessLock": ((5, LCID, 4, 0),()),
		"ModificationCount": ((20, LCID, 4, 0),()),
		"ModificationCountEx": ((24, LCID, 4, 0),()),
		"ModificationCountLock": ((21, LCID, 4, 0),()),
		"Parent": ((1, LCID, 8, 0),()),
	}

	AccessLock: str # read/write
	InternalIndex: str # read_only
	ModificationCount: str # read/write
	ModificationCountEx: str # read/write
	ModificationCountLock: str # read/write
	Parent: str # read/write
	RootIF: str # IMGCVariantMgrDocument; read_only

	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMGCVariantMgrBaseNameObject(DispatchBaseClass):
	'The base object that provides a name'
	CLSID = IID('{82CD5AB8-9407-11D2-89D9-0020184077E1}')
	coclass_clsid = None

	def CompareUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Compares a UID with the UID of the object. Returns true if equal.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((19, 1), (19, 1), (19, 1)),userID
			, objectID, objectType)

	def GetUID(self, userID=pythoncom.Missing, objectID=pythoncom.Missing, objectType=pythoncom.Missing):
		'Gets the UID of an object. Returns false if the UID is invalid.'
		return self._ApplyTypes_(6, 1, (11, 0), ((16403, 2), (16403, 2), (16403, 2)), 'GetUID', None,userID
			, objectID, objectType)

	def IsValid(self):
		'Returns the internal (CPP) index of the X-Object'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), (),)

	def SetInternalValue(self, id=defaultNamedNotOptArg, parm1=defaultNamedOptArg, parm2=defaultNamedOptArg, parm3=defaultNamedOptArg):
		'Sets an internal value on an object'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (2, 0), ((8, 1), (12, 17), (12, 17), (12, 17)),id
			, parm1, parm2, parm3)

	def SetUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Sets the UID of an object. Returns false if the UID is invalid.'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (11, 0), ((19, 1), (19, 1), (19, 1)),userID
			, objectID, objectType)

	_prop_map_get_ = {
		"AccessLock": (5, 2, (3, 0), (), "AccessLock", None),
		"InternalIndex": (2, 2, (3, 0), (), "InternalIndex", None),
		"Name": (35, 2, (8, 0), (), "Name", None),
		"Parent": (1, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
		"AccessLock": ((5, LCID, 4, 0),()),
		"Name": ((35, LCID, 4, 0),()),
		"Parent": ((1, LCID, 8, 0),()),
	}

	AccessLock: str # read/write
	InternalIndex: str # read_only
	Name: str # read/write
	Parent: str # read/write

	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMGCVariantMgrBaseObject(DispatchBaseClass):
	'The base object for all variant manager objects'
	CLSID = IID('{786637F0-9407-11D2-89D9-0020184077E1}')
	coclass_clsid = None

	def CompareUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Compares a UID with the UID of the object. Returns true if equal.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((19, 1), (19, 1), (19, 1)),userID
			, objectID, objectType)

	def GetUID(self, userID=pythoncom.Missing, objectID=pythoncom.Missing, objectType=pythoncom.Missing):
		'Gets the UID of an object. Returns false if the UID is invalid.'
		return self._ApplyTypes_(6, 1, (11, 0), ((16403, 2), (16403, 2), (16403, 2)), 'GetUID', None,userID
			, objectID, objectType)

	def IsValid(self):
		'Returns the internal (CPP) index of the X-Object'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), (),)

	def SetInternalValue(self, id=defaultNamedNotOptArg, parm1=defaultNamedOptArg, parm2=defaultNamedOptArg, parm3=defaultNamedOptArg):
		'Sets an internal value on an object'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (2, 0), ((8, 1), (12, 17), (12, 17), (12, 17)),id
			, parm1, parm2, parm3)

	def SetUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Sets the UID of an object. Returns false if the UID is invalid.'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (11, 0), ((19, 1), (19, 1), (19, 1)),userID
			, objectID, objectType)

	_prop_map_get_ = {
		"AccessLock": (5, 2, (3, 0), (), "AccessLock", None),
		"InternalIndex": (2, 2, (3, 0), (), "InternalIndex", None),
		"Parent": (1, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
		"AccessLock": ((5, LCID, 4, 0),()),
		"Parent": ((1, LCID, 8, 0),()),
	}

	AccessLock: str # read/write
	InternalIndex: str # read_only
	Parent: str # read/write

	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMGCVariantMgrBlock(DispatchBaseClass):
	'Describes a hierarchical block'
	CLSID = IID('{E2CD1C5F-0EE9-4349-B08A-FA34A84CB2F1}')
	coclass_clsid = IID('{463130F2-CF4B-49B8-9376-FD86C3AECA74}')

	def CompareUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Compares a UID with the UID of the object. Returns true if equal.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((19, 1), (19, 1), (19, 1)),userID
			, objectID, objectType)

	def ContainsReusedBlocks(self, traverseHierarchy=True):
		'Checks if the block contains reused blocks in the sub level(s)'
		return self._oleobj_.InvokeTypes(102, LCID, 1, (11, 0), ((11, 49),),traverseHierarchy
			)

	def GetUID(self, userID=pythoncom.Missing, objectID=pythoncom.Missing, objectType=pythoncom.Missing):
		'Gets the UID of an object. Returns false if the UID is invalid.'
		return self._ApplyTypes_(6, 1, (11, 0), ((16403, 2), (16403, 2), (16403, 2)), 'GetUID', None,userID
			, objectID, objectType)

	def IncModificationCount(self, value=1):
		'Increments the modification count'
		return self._oleobj_.InvokeTypes(23, LCID, 1, (2, 0), ((2, 49),),value
			)

	def IsValid(self):
		'Returns the internal (CPP) index of the X-Object'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), (),)

	def SetInternalValue(self, id=defaultNamedNotOptArg, parm1=defaultNamedOptArg, parm2=defaultNamedOptArg, parm3=defaultNamedOptArg):
		'Sets an internal value on an object'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (2, 0), ((8, 1), (12, 17), (12, 17), (12, 17)),id
			, parm1, parm2, parm3)

	def SetUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Sets the UID of an object. Returns false if the UID is invalid.'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (11, 0), ((19, 1), (19, 1), (19, 1)),userID
			, objectID, objectType)

	_prop_map_get_ = {
		"AccessLock": (5, 2, (3, 0), (), "AccessLock", None),
		# Method 'BlockData' returns object of type 'IMGCVariantMgrBlockData'
		"BlockData": (101, 2, (9, 0), (), "BlockData", '{7FE7FAB6-7B3B-46CB-970A-0010103AD7E3}'),
		"DynamicReuseName": (103, 2, (8, 0), (), "DynamicReuseName", None),
		"InternalIndex": (2, 2, (3, 0), (), "InternalIndex", None),
		"ModificationCount": (20, 2, (2, 0), (), "ModificationCount", None),
		"ModificationCountEx": (24, 2, (3, 0), (), "ModificationCountEx", None),
		"ModificationCountLock": (21, 2, (11, 0), (), "ModificationCountLock", None),
		"Name": (30, 2, (8, 0), (), "Name", None),
		"Parent": (1, 2, (9, 0), (), "Parent", None),
		# Method 'RootIF' returns object of type 'IMGCVariantMgrDocument'
		"RootIF": (22, 2, (9, 0), (), "RootIF", '{78663807-9407-11D2-89D9-0020184077E1}'),
	}
	_prop_map_put_ = {
		"AccessLock": ((5, LCID, 4, 0),()),
		"DynamicReuseName": ((103, LCID, 4, 0),()),
		"ModificationCount": ((20, LCID, 4, 0),()),
		"ModificationCountEx": ((24, LCID, 4, 0),()),
		"ModificationCountLock": ((21, LCID, 4, 0),()),
		"Name": ((30, LCID, 4, 0),()),
		"Parent": ((1, LCID, 8, 0),()),
	}

	AccessLock: str # read/write
	BlockData: str # IMGCVariantMgrBlockData; read_only
	DynamicReuseName: str # read/write
	InternalIndex: str # read_only
	ModificationCount: str # read/write
	ModificationCountEx: str # read/write
	ModificationCountLock: str # read/write
	Name: str # read/write
	Parent: str # read/write
	RootIF: str # IMGCVariantMgrDocument; read_only

	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMGCVariantMgrBlockData(DispatchBaseClass):
	'Describes the data of a block type object (block or reused)'
	CLSID = IID('{7FE7FAB6-7B3B-46CB-970A-0010103AD7E3}')
	coclass_clsid = IID('{1AEE4AD1-C054-4533-BF0E-1D6ED8BBD173}')

	# Result is of type IMGCVariantMgrPackages
	# The method AllPackages is actually a property, but must be used as a method to correctly pass the arguments
	def AllPackages(self, bIncludeRBs=defaultNamedNotOptArg, filter=defaultNamedOptArg):
		'Returns the all packages that are part of the block and all sub-blocks'
		ret = self._oleobj_.InvokeTypes(112, LCID, 2, (9, 0), ((11, 1), (12, 17)),bIncludeRBs
			, filter)
		if ret is not None:
			ret = Dispatch(ret, 'AllPackages', '{786637F6-9407-11D2-89D9-0020184077E1}')
		return ret

	def CompareUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Compares a UID with the UID of the object. Returns true if equal.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((19, 1), (19, 1), (19, 1)),userID
			, objectID, objectType)

	def ContainsModifications(self, variantDef=defaultNamedNotOptArg):
		'Check if there are any modifications in RB.'
		return self._oleobj_.InvokeTypes(111, LCID, 1, (11, 0), ((12, 1),),variantDef
			)

	def ContainsPackageModifications(self, includeSubBlocks=True, packModfilter=defaultNamedOptArg):
		'Checks if the block data is defined for a reused block'
		return self._oleobj_.InvokeTypes(107, LCID, 1, (11, 0), ((11, 49), (12, 17)),includeSubBlocks
			, packModfilter)

	def ContainsReusedBlocks(self, traverseHierarchy=True):
		'Checks if the parent (reused) block contains reused blocks in the sub level(s)'
		return self._oleobj_.InvokeTypes(108, LCID, 1, (11, 0), ((11, 49),),traverseHierarchy
			)

	# Result is of type IMGCVariantMgrBlocks
	# The method GetBlocks is actually a property, but must be used as a method to correctly pass the arguments
	def GetBlocks(self, filter=defaultNamedOptArg):
		'Returns the blocks that are part of the block'
		ret = self._oleobj_.InvokeTypes(104, LCID, 2, (9, 0), ((12, 17),),filter
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetBlocks', '{F74277DE-9533-4D61-A84B-44D4A326B316}')
		return ret

	# Result is of type IMGCVariantMgrPackages
	# The method GetPackages is actually a property, but must be used as a method to correctly pass the arguments
	def GetPackages(self, filter=defaultNamedOptArg):
		'Returns the packages that are part of the block'
		ret = self._oleobj_.InvokeTypes(103, LCID, 2, (9, 0), ((12, 17),),filter
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetPackages', '{786637F6-9407-11D2-89D9-0020184077E1}')
		return ret

	# Result is of type IMGCVariantMgrReusedBlocks
	# The method GetReusedBlocks is actually a property, but must be used as a method to correctly pass the arguments
	def GetReusedBlocks(self, filter=defaultNamedOptArg):
		'Returns the reused blocks taht are part of the block'
		ret = self._oleobj_.InvokeTypes(105, LCID, 2, (9, 0), ((12, 17),),filter
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetReusedBlocks', '{82CD5AA5-9407-11D2-89D9-0020184077E1}')
		return ret

	# Result is of type IMGCVariantMgrSymbols
	# The method GetSymbols is actually a property, but must be used as a method to correctly pass the arguments
	def GetSymbols(self, filter=defaultNamedOptArg):
		'Returns the packages that are part of the block'
		ret = self._oleobj_.InvokeTypes(102, LCID, 2, (9, 0), ((12, 17),),filter
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetSymbols', '{786637F7-9407-11D2-89D9-0020184077E1}')
		return ret

	def GetUID(self, userID=pythoncom.Missing, objectID=pythoncom.Missing, objectType=pythoncom.Missing):
		'Gets the UID of an object. Returns false if the UID is invalid.'
		return self._ApplyTypes_(6, 1, (11, 0), ((16403, 2), (16403, 2), (16403, 2)), 'GetUID', None,userID
			, objectID, objectType)

	def IncModificationCount(self, value=1):
		'Increments the modification count'
		return self._oleobj_.InvokeTypes(23, LCID, 1, (2, 0), ((2, 49),),value
			)

	def IsReusedBlock(self):
		'Checks if the block data is defined for a reused block'
		return self._oleobj_.InvokeTypes(106, LCID, 1, (11, 0), (),)

	def IsValid(self):
		'Returns the internal (CPP) index of the X-Object'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), (),)

	def SetInternalValue(self, id=defaultNamedNotOptArg, parm1=defaultNamedOptArg, parm2=defaultNamedOptArg, parm3=defaultNamedOptArg):
		'Sets an internal value on an object'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (2, 0), ((8, 1), (12, 17), (12, 17), (12, 17)),id
			, parm1, parm2, parm3)

	def SetUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Sets the UID of an object. Returns false if the UID is invalid.'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (11, 0), ((19, 1), (19, 1), (19, 1)),userID
			, objectID, objectType)

	_prop_map_get_ = {
		"AccessLock": (5, 2, (3, 0), (), "AccessLock", None),
		# Method 'BlockSymbol' returns object of type 'IMGCVariantMgrSymbol'
		"BlockSymbol": (101, 2, (9, 0), (), "BlockSymbol", '{786637F4-9407-11D2-89D9-0020184077E1}'),
		# Method 'Blocks' returns object of type 'IMGCVariantMgrBlocks'
		"Blocks": (104, 2, (9, 0), ((12, 17),), "Blocks", '{F74277DE-9533-4D61-A84B-44D4A326B316}'),
		"InternalIndex": (2, 2, (3, 0), (), "InternalIndex", None),
		"IsLogicalOnlyPartModificationAllowed": (114, 2, (11, 0), (), "IsLogicalOnlyPartModificationAllowed", None),
		"IsParentLogicalReusedBlock": (110, 2, (11, 0), (), "IsParentLogicalReusedBlock", None),
		"IsParentReusedBlock": (109, 2, (11, 0), (), "IsParentReusedBlock", None),
		"ModificationCount": (20, 2, (2, 0), (), "ModificationCount", None),
		"ModificationCountEx": (24, 2, (3, 0), (), "ModificationCountEx", None),
		"ModificationCountLock": (21, 2, (11, 0), (), "ModificationCountLock", None),
		"Name": (30, 2, (8, 0), (), "Name", None),
		# Method 'Packages' returns object of type 'IMGCVariantMgrPackages'
		"Packages": (103, 2, (9, 0), ((12, 17),), "Packages", '{786637F6-9407-11D2-89D9-0020184077E1}'),
		"Parent": (1, 2, (9, 0), (), "Parent", None),
		"ParentDynamicReuseBlockName": (113, 2, (8, 0), (), "ParentDynamicReuseBlockName", None),
		# Method 'ReusedBlocks' returns object of type 'IMGCVariantMgrReusedBlocks'
		"ReusedBlocks": (105, 2, (9, 0), ((12, 17),), "ReusedBlocks", '{82CD5AA5-9407-11D2-89D9-0020184077E1}'),
		# Method 'RootIF' returns object of type 'IMGCVariantMgrDocument'
		"RootIF": (22, 2, (9, 0), (), "RootIF", '{78663807-9407-11D2-89D9-0020184077E1}'),
		# Method 'Symbols' returns object of type 'IMGCVariantMgrSymbols'
		"Symbols": (102, 2, (9, 0), ((12, 17),), "Symbols", '{786637F7-9407-11D2-89D9-0020184077E1}'),
	}
	_prop_map_put_ = {
		"AccessLock": ((5, LCID, 4, 0),()),
		"ModificationCount": ((20, LCID, 4, 0),()),
		"ModificationCountEx": ((24, LCID, 4, 0),()),
		"ModificationCountLock": ((21, LCID, 4, 0),()),
		"Name": ((30, LCID, 4, 0),()),
		"Parent": ((1, LCID, 8, 0),()),
	}

	AccessLock: str # read/write
	BlockSymbol: str # IMGCVariantMgrSymbol; read_only
	Blocks: str # IMGCVariantMgrBlocks; read_only
	InternalIndex: str # read_only
	IsLogicalOnlyPartModificationAllowed: str # read_only
	IsParentLogicalReusedBlock: str # read_only
	IsParentReusedBlock: str # read_only
	ModificationCount: str # read/write
	ModificationCountEx: str # read/write
	ModificationCountLock: str # read/write
	Name: str # read/write
	Packages: str # IMGCVariantMgrPackages; read_only
	Parent: str # read/write
	ParentDynamicReuseBlockName: str # read_only
	ReusedBlocks: str # IMGCVariantMgrReusedBlocks; read_only
	RootIF: str # IMGCVariantMgrDocument; read_only
	Symbols: str # IMGCVariantMgrSymbols; read_only

	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMGCVariantMgrBlockDataModification(DispatchBaseClass):
	CLSID = IID('{5F556342-9E5E-4B96-9002-9B148BA114DD}')
	coclass_clsid = IID('{6DA2DE93-5489-4171-BAD6-E836390A07C2}')

	def CompareUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Compares a UID with the UID of the object. Returns true if equal.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((19, 1), (19, 1), (19, 1)),userID
			, objectID, objectType)

	def Delete(self):
		'Deletes the symbol modification.'
		return self._oleobj_.InvokeTypes(104, LCID, 1, (11, 0), (),)

	def GetParentUID(self, userID=pythoncom.Missing, objectID=pythoncom.Missing, objectType=pythoncom.Missing):
		'Gets the UID of an parent object. Returns false if the UID is invalid.'
		return self._ApplyTypes_(109, 1, (11, 0), ((16403, 2), (16403, 2), (16403, 2)), 'GetParentUID', None,userID
			, objectID, objectType)

	def GetSubVariantUID(self, userID=pythoncom.Missing, objectID=pythoncom.Missing, objectType=pythoncom.Missing):
		'Returns or sets the sub variant uid  to which the package modification applies.'
		return self._ApplyTypes_(107, 1, (11, 0), ((16403, 2), (16403, 2), (16403, 2)), 'GetSubVariantUID', None,userID
			, objectID, objectType)

	def GetUID(self, userID=pythoncom.Missing, objectID=pythoncom.Missing, objectType=pythoncom.Missing):
		'Gets the UID of an object. Returns false if the UID is invalid.'
		return self._ApplyTypes_(6, 1, (11, 0), ((16403, 2), (16403, 2), (16403, 2)), 'GetUID', None,userID
			, objectID, objectType)

	def IncModificationCount(self, value=1):
		'Increments the modification count'
		return self._oleobj_.InvokeTypes(23, LCID, 1, (2, 0), ((2, 49),),value
			)

	def IsValid(self):
		'Returns the internal (CPP) index of the X-Object'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), (),)

	def Merge(self):
		'Merge changes.'
		return self._oleobj_.InvokeTypes(108, LCID, 1, (11, 0), (),)

	def SetInternalValue(self, id=defaultNamedNotOptArg, parm1=defaultNamedOptArg, parm2=defaultNamedOptArg, parm3=defaultNamedOptArg):
		'Sets an internal value on an object'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (2, 0), ((8, 1), (12, 17), (12, 17), (12, 17)),id
			, parm1, parm2, parm3)

	def SetSubVariantUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Returns or sets the sub variant uid to which the block data modification applies.'
		return self._oleobj_.InvokeTypes(106, LCID, 1, (11, 0), ((19, 1), (19, 1), (19, 1)),userID
			, objectID, objectType)

	def SetUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Sets the UID of an object. Returns false if the UID is invalid.'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (11, 0), ((19, 1), (19, 1), (19, 1)),userID
			, objectID, objectType)

	_prop_map_get_ = {
		"AccessLock": (5, 2, (3, 0), (), "AccessLock", None),
		# Method 'BlockData' returns object of type 'IMGCVariantMgrBlockData'
		"BlockData": (101, 2, (9, 0), (), "BlockData", '{7FE7FAB6-7B3B-46CB-970A-0010103AD7E3}'),
		"ChangeOperation": (102, 2, (3, 0), (), "ChangeOperation", None),
		"InternalIndex": (2, 2, (3, 0), (), "InternalIndex", None),
		"ModificationCount": (20, 2, (2, 0), (), "ModificationCount", None),
		"ModificationCountEx": (24, 2, (3, 0), (), "ModificationCountEx", None),
		"ModificationCountLock": (21, 2, (11, 0), (), "ModificationCountLock", None),
		"Name": (30, 2, (8, 0), (), "Name", None),
		"Parent": (1, 2, (9, 0), (), "Parent", None),
		# Method 'RootIF' returns object of type 'IMGCVariantMgrDocument'
		"RootIF": (22, 2, (9, 0), (), "RootIF", '{78663807-9407-11D2-89D9-0020184077E1}'),
		"SubVariantName": (105, 2, (8, 0), (), "SubVariantName", None),
		# Method 'Variant' returns object of type 'IMGCVariantMgrVariant'
		"Variant": (103, 2, (9, 0), (), "Variant", '{78663802-9407-11D2-89D9-0020184077E1}'),
	}
	_prop_map_put_ = {
		"AccessLock": ((5, LCID, 4, 0),()),
		"ChangeOperation": ((102, LCID, 4, 0),()),
		"ModificationCount": ((20, LCID, 4, 0),()),
		"ModificationCountEx": ((24, LCID, 4, 0),()),
		"ModificationCountLock": ((21, LCID, 4, 0),()),
		"Name": ((30, LCID, 4, 0),()),
		"Parent": ((1, LCID, 8, 0),()),
		"SubVariantName": ((105, LCID, 4, 0),()),
		"Variant": ((103, LCID, 8, 0),()),
	}

	AccessLock: str # read/write
	BlockData: str # IMGCVariantMgrBlockData; read_only
	ChangeOperation: str # read/write
	InternalIndex: str # read_only
	ModificationCount: str # read/write
	ModificationCountEx: str # read/write
	ModificationCountLock: str # read/write
	Name: str # read/write
	Parent: str # read/write
	RootIF: str # IMGCVariantMgrDocument; read_only
	SubVariantName: str # read/write
	Variant: str # read/write

	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMGCVariantMgrBlockDataModificationFilter(DispatchBaseClass):
	CLSID = IID('{761BC783-46D2-4961-835B-653901ED7E7F}')
	coclass_clsid = IID('{0397654E-7091-4683-9FF8-D064B20281FB}')

	def CompareUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Compares a UID with the UID of the object. Returns true if equal.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((19, 1), (19, 1), (19, 1)),userID
			, objectID, objectType)

	def GetRootIF(self, ppDocObj=pythoncom.Missing):
		'Get the document object for the filter.'
		return self._ApplyTypes_(100, 1, (24, 0), ((16393, 2),), 'GetRootIF', None,ppDocObj
			)

	def GetUID(self, userID=pythoncom.Missing, objectID=pythoncom.Missing, objectType=pythoncom.Missing):
		'Gets the UID of an object. Returns false if the UID is invalid.'
		return self._ApplyTypes_(6, 1, (11, 0), ((16403, 2), (16403, 2), (16403, 2)), 'GetUID', None,userID
			, objectID, objectType)

	def Initialize(self):
		'Initializes the object.'
		return self._oleobj_.InvokeTypes(106, LCID, 1, (24, 0), (),)

	def IsValid(self):
		'Returns the internal (CPP) index of the X-Object'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), (),)

	def SetInternalValue(self, id=defaultNamedNotOptArg, parm1=defaultNamedOptArg, parm2=defaultNamedOptArg, parm3=defaultNamedOptArg):
		'Sets an internal value on an object'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (2, 0), ((8, 1), (12, 17), (12, 17), (12, 17)),id
			, parm1, parm2, parm3)

	def SetUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Sets the UID of an object. Returns false if the UID is invalid.'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (11, 0), ((19, 1), (19, 1), (19, 1)),userID
			, objectID, objectType)

	_prop_map_get_ = {
		"AccessLock": (5, 2, (3, 0), (), "AccessLock", None),
		"ChangeOperation": (102, 2, (3, 0), (), "ChangeOperation", None),
		"InternalIndex": (2, 2, (3, 0), (), "InternalIndex", None),
		"Parent": (1, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
		"AccessLock": ((5, LCID, 4, 0),()),
		"BlockData": ((101, LCID, 4, 0),()),
