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
		"ChangeOperation": ((102, LCID, 4, 0),()),
		"Parent": ((1, LCID, 8, 0),()),
		"Variant": ((104, LCID, 4, 0),()),
		"VariantGroup": ((105, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMGCVariantMgrBlockDataModifications(DispatchBaseClass):
	'Variant manager block data modifications collection'
	CLSID = IID('{45742780-B379-49F9-8431-16CB70520F9C}')
	coclass_clsid = IID('{19BDB78E-F30F-4F0E-A43E-E87E33F9995D}')

	def Add(self, pPackMod=defaultNamedNotOptArg):
		'Adds a block data modification object to the collection.'
		return self._oleobj_.InvokeTypes(102, LCID, 1, (24, 0), ((9, 1),),pPackMod
			)

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

	# Result is of type IMGCVariantMgrBlockDataModification
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, index=defaultNamedNotOptArg):
		'Returns a block data modification object at a given index.'
		ret = self._oleobj_.InvokeTypes(101, LCID, 2, (9, 0), ((12, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{5F556342-9E5E-4B96-9002-9B148BA114DD}')
		return ret

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
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{5F556342-9E5E-4B96-9002-9B148BA114DD}')
	#This class has Item property/method which allows indexed access with the object[key] syntax.
	#Some objects will accept a string or other type of key in addition to integers.
	#Note that many Office objects do not use zero-based indexing.
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(101, LCID, 2, 1, key)), "Item", '{5F556342-9E5E-4B96-9002-9B148BA114DD}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(30, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IMGCVariantMgrBlocks(DispatchBaseClass):
	'Variant manager block'
	CLSID = IID('{F74277DE-9533-4D61-A84B-44D4A326B316}')
	coclass_clsid = IID('{BE31CD71-78CF-4C67-A875-77F5E1297B47}')

	def Add(self, pBlock=defaultNamedNotOptArg):
		'Adds a block to the collection.'
		return self._oleobj_.InvokeTypes(102, LCID, 1, (24, 0), ((9, 1),),pBlock
			)

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

	# Result is of type IMGCVariantMgrBlock
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, index=defaultNamedNotOptArg):
		'Returns a block definition'
		ret = self._oleobj_.InvokeTypes(101, LCID, 2, (9, 0), ((12, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{E2CD1C5F-0EE9-4349-B08A-FA34A84CB2F1}')
		return ret

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
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{E2CD1C5F-0EE9-4349-B08A-FA34A84CB2F1}')
	#This class has Item property/method which allows indexed access with the object[key] syntax.
	#Some objects will accept a string or other type of key in addition to integers.
	#Note that many Office objects do not use zero-based indexing.
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(101, LCID, 2, 1, key)), "Item", '{E2CD1C5F-0EE9-4349-B08A-FA34A84CB2F1}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(30, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IMGCVariantMgrBorderPropModification(DispatchBaseClass):
	CLSID = IID('{22D9A8DA-F507-43FD-BA22-6DB8FEA436F2}')
	coclass_clsid = IID('{F7DCE892-A986-480A-9A79-26879868C4C2}')

	def CompareUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Compares a UID with the UID of the object. Returns true if equal.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((19, 1), (19, 1), (19, 1)),userID
			, objectID, objectType)

	def Delete(self):
		'Deletes the border prop modification.'
		return self._oleobj_.InvokeTypes(104, LCID, 1, (11, 0), (),)

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
		# Method 'Symbol' returns object of type 'IMGCVariantMgrSymbol'
		"Symbol": (102, 2, (9, 0), (), "Symbol", '{786637F4-9407-11D2-89D9-0020184077E1}'),
		# Method 'Variant' returns object of type 'IMGCVariantMgrVariant'
		"Variant": (103, 2, (9, 0), (), "Variant", '{78663802-9407-11D2-89D9-0020184077E1}'),
		"value": (101, 2, (8, 0), (), "value", None),
	}
	_prop_map_put_ = {
		"AccessLock": ((5, LCID, 4, 0),()),
		"ModificationCount": ((20, LCID, 4, 0),()),
		"ModificationCountEx": ((24, LCID, 4, 0),()),
		"ModificationCountLock": ((21, LCID, 4, 0),()),
		"Name": ((30, LCID, 4, 0),()),
		"Parent": ((1, LCID, 8, 0),()),
		"Symbol": ((102, LCID, 8, 0),()),
		"Variant": ((103, LCID, 8, 0),()),
		"value": ((101, LCID, 4, 0),()),
	}
	# Default property for this class is 'value'
	def __call__(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "value", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMGCVariantMgrBorderPropModificationFilter(DispatchBaseClass):
	CLSID = IID('{1158040D-F8C4-4865-A4A6-F42D11C258BA}')
	coclass_clsid = IID('{C1027159-081D-460B-9420-DC3A23ACE84D}')

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
		"InternalIndex": (2, 2, (3, 0), (), "InternalIndex", None),
		"Name": (102, 2, (8, 0), (), "Name", None),
		"Parent": (1, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
		"AccessLock": ((5, LCID, 4, 0),()),
		"Name": ((102, LCID, 4, 0),()),
		"Parent": ((1, LCID, 8, 0),()),
		"Symbol": ((105, LCID, 4, 0),()),
		"Variant": ((104, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMGCVariantMgrBorderPropModifications(DispatchBaseClass):
	'Variant manager border property modifications collection'
	CLSID = IID('{72982CC0-8617-400A-9772-5DF126EA582A}')
	coclass_clsid = IID('{A1C6B0A5-F25F-41EC-BBB7-F4CE90E80F41}')

	def Add(self, pPackMod=defaultNamedNotOptArg):
		'Adds a border property modification object to the collection.'
		return self._oleobj_.InvokeTypes(102, LCID, 1, (24, 0), ((9, 1),),pPackMod
			)

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

	# Result is of type IMGCVariantMgrBorderPropModification
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, index=defaultNamedNotOptArg):
		'Returns a border property modification object at a given index.'
		ret = self._oleobj_.InvokeTypes(101, LCID, 2, (9, 0), ((12, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{22D9A8DA-F507-43FD-BA22-6DB8FEA436F2}')
		return ret

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
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{22D9A8DA-F507-43FD-BA22-6DB8FEA436F2}')
	#This class has Item property/method which allows indexed access with the object[key] syntax.
	#Some objects will accept a string or other type of key in addition to integers.
	#Note that many Office objects do not use zero-based indexing.
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(101, LCID, 2, 1, key)), "Item", '{22D9A8DA-F507-43FD-BA22-6DB8FEA436F2}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(30, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IMGCVariantMgrConnectivity(DispatchBaseClass):
	'The connectivity information of the document'
	CLSID = IID('{82CD5AA6-9407-11D2-89D9-0020184077E1}')
	coclass_clsid = IID('{82CD5AAA-9407-11D2-89D9-0020184077E1}')

	def CheckNotMarkedPackages(self):
		'Check marked packages.'
		return self._oleobj_.InvokeTypes(120, LCID, 1, (2, 0), (),)

	def CompareUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Compares a UID with the UID of the object. Returns true if equal.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((19, 1), (19, 1), (19, 1)),userID
			, objectID, objectType)

	# Result is of type IMGCVariantMgrPackage
	def FindPackage(self, packName=defaultNamedNotOptArg):
		'Returns a package object for the requested package'
		ret = self._oleobj_.InvokeTypes(112, LCID, 1, (9, 0), ((8, 1),),packName
			)
		if ret is not None:
			ret = Dispatch(ret, 'FindPackage', '{786637F5-9407-11D2-89D9-0020184077E1}')
		return ret

	# Result is of type IMGCVariantMgrPackage
	def FindPackageBySID(self, SID=defaultNamedNotOptArg):
		'Returns a package object by its sid'
		ret = self._oleobj_.InvokeTypes(119, LCID, 1, (9, 0), ((8, 1),),SID
			)
		if ret is not None:
			ret = Dispatch(ret, 'FindPackageBySID', '{786637F5-9407-11D2-89D9-0020184077E1}')
		return ret

	# Result is of type IMGCVariantMgrPackage
	def FindPackageByUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Returns a package object by its id'
		ret = self._oleobj_.InvokeTypes(117, LCID, 1, (9, 0), ((3, 1), (3, 1), (3, 1)),userID
			, objectID, objectType)
		if ret is not None:
			ret = Dispatch(ret, 'FindPackageByUID', '{786637F5-9407-11D2-89D9-0020184077E1}')
		return ret

	# Result is of type IMGCVariantMgrSymbol
	def FindSymbol(self, symbolNameAndPath=defaultNamedNotOptArg):
		'Returns a symbol object using full name'
		ret = self._oleobj_.InvokeTypes(118, LCID, 1, (9, 0), ((8, 1),),symbolNameAndPath
			)
		if ret is not None:
			ret = Dispatch(ret, 'FindSymbol', '{786637F4-9407-11D2-89D9-0020184077E1}')
		return ret

	# Result is of type IMGCVariantMgrSymbol
	def FindSymbolByUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Returns a symbol by its UID.'
		ret = self._oleobj_.InvokeTypes(114, LCID, 1, (9, 0), ((3, 1), (3, 1), (3, 1)),userID
			, objectID, objectType)
		if ret is not None:
			ret = Dispatch(ret, 'FindSymbolByUID', '{786637F4-9407-11D2-89D9-0020184077E1}')
		return ret

	# Result is of type IMGCVariantMgrBlocks
	# The method GetBlocks is actually a property, but must be used as a method to correctly pass the arguments
	def GetBlocks(self, filter=defaultNamedOptArg):
		'Returns a collection of blocks in the design.'
		ret = self._oleobj_.InvokeTypes(104, LCID, 2, (9, 0), ((12, 17),),filter
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetBlocks', '{F74277DE-9533-4D61-A84B-44D4A326B316}')
		return ret

	# Result is of type IMGCVariantMgrEquivalentBlockGroups
	# The method GetEquivalentBlockGroups is actually a property, but must be used as a method to correctly pass the arguments
	def GetEquivalentBlockGroups(self, filter=defaultNamedOptArg):
		'Returns a collection of symbol locations'
		ret = self._oleobj_.InvokeTypes(106, LCID, 2, (9, 0), ((12, 17),),filter
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetEquivalentBlockGroups', '{98301621-82F9-4458-996F-46739708B82C}')
		return ret

	# Result is of type IMGCVariantMgrPackages
	# The method GetPackages is actually a property, but must be used as a method to correctly pass the arguments
	def GetPackages(self, filter=defaultNamedOptArg):
		'Returns a collection of packages in the design'
		ret = self._oleobj_.InvokeTypes(102, LCID, 2, (9, 0), ((12, 17),),filter
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetPackages', '{786637F6-9407-11D2-89D9-0020184077E1}')
		return ret

	# Result is of type IMGCVariantMgrReusedBlocks
	# The method GetReusedBlocks is actually a property, but must be used as a method to correctly pass the arguments
	def GetReusedBlocks(self, filter=defaultNamedOptArg):
		'Returns a collection of reused blocks in the design.'
		ret = self._oleobj_.InvokeTypes(103, LCID, 2, (9, 0), ((12, 17),),filter
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetReusedBlocks', '{82CD5AA5-9407-11D2-89D9-0020184077E1}')
		return ret

	def GetSymbolBorderProperties(self, pSymbol=defaultNamedNotOptArg, commonProp=defaultNamedNotOptArg, borderProps=pythoncom.Missing, num=pythoncom.Missing):
		'Get the list of border symbol properties'
		return self._ApplyTypes_(121, 1, (11, 0), ((9, 1), (12, 1), (16396, 2), (16387, 2)), 'GetSymbolBorderProperties', None,pSymbol
			, commonProp, borderProps, num)

	# Result is of type IMGCVariantMgrSymbolLocations
	# The method GetSymbolLocations is actually a property, but must be used as a method to correctly pass the arguments
	def GetSymbolLocations(self, filter=defaultNamedOptArg):
		'Returns a collection of symbol locations'
		ret = self._oleobj_.InvokeTypes(105, LCID, 2, (9, 0), ((12, 17),),filter
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetSymbolLocations', '{786637F8-9407-11D2-89D9-0020184077E1}')
		return ret

	# Result is of type IMGCVariantMgrSymbols
	# The method GetSymbols is actually a property, but must be used as a method to correctly pass the arguments
	def GetSymbols(self, filter=defaultNamedOptArg):
		'Returns a collection of symbols in the design'
		ret = self._oleobj_.InvokeTypes(101, LCID, 2, (9, 0), ((12, 17),),filter
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetSymbols', '{786637F7-9407-11D2-89D9-0020184077E1}')
		return ret

	def GetUID(self, userID=pythoncom.Missing, objectID=pythoncom.Missing, objectType=pythoncom.Missing):
		'Gets the UID of an object. Returns false if the UID is invalid.'
		return self._ApplyTypes_(6, 1, (11, 0), ((16403, 2), (16403, 2), (16403, 2)), 'GetUID', None,userID
			, objectID, objectType)

	def GetUserDefinedPropertiesForBOM(self, inProps=defaultNamedNotOptArg, propInfo=pythoncom.Missing):
		'Get the list of user defined properties for BOM'
		return self._ApplyTypes_(122, 1, (2, 0), ((8, 1), (16396, 2)), 'GetUserDefinedPropertiesForBOM', None,inProps
			, propInfo)

	def IsValid(self):
		'Returns the internal (CPP) index of the X-Object'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), (),)

	def Load(self, fileName=defaultNamedNotOptArg, connSource=defaultNamedNotOptArg, logFileName=defaultNamedNotOptArg, addiParm=''):
		'Loads the data from a connectivity source'
		return self._ApplyTypes_(107, 1, (2, 32), ((8, 1), (3, 1), (8, 1), (8, 49)), 'Load', None,fileName
			, connSource, logFileName, addiParm)

	def ReLoadPropertiesForBOM(self, xmlConfigurationFile=defaultNamedNotOptArg):
		'Reopen iCDB and check properties'
		return self._oleobj_.InvokeTypes(116, LCID, 1, (2, 0), ((8, 1),),xmlConfigurationFile
			)

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
		"AppName": (115, 2, (8, 0), (), "AppName", None),
		# Method 'Blocks' returns object of type 'IMGCVariantMgrBlocks'
		"Blocks": (104, 2, (9, 0), ((12, 17),), "Blocks", '{F74277DE-9533-4D61-A84B-44D4A326B316}'),
		"ConnectivitySource": (109, 2, (8, 0), (), "ConnectivitySource", None),
		"ConnectivitySourceDate": (111, 2, (3, 0), (), "ConnectivitySourceDate", None),
		"ConnectivitySourceType": (108, 2, (3, 0), (), "ConnectivitySourceType", None),
		# Method 'EquivalentBlockGroups' returns object of type 'IMGCVariantMgrEquivalentBlockGroups'
		"EquivalentBlockGroups": (106, 2, (9, 0), ((12, 17),), "EquivalentBlockGroups", '{98301621-82F9-4458-996F-46739708B82C}'),
		"InternalIndex": (2, 2, (3, 0), (), "InternalIndex", None),
		# Method 'Packages' returns object of type 'IMGCVariantMgrPackages'
		"Packages": (102, 2, (9, 0), ((12, 17),), "Packages", '{786637F6-9407-11D2-89D9-0020184077E1}'),
		"Parent": (1, 2, (9, 0), (), "Parent", None),
		# Method 'ReusedBlocks' returns object of type 'IMGCVariantMgrReusedBlocks'
		"ReusedBlocks": (103, 2, (9, 0), ((12, 17),), "ReusedBlocks", '{82CD5AA5-9407-11D2-89D9-0020184077E1}'),
		# Method 'RootBlock' returns object of type 'IMGCVariantMgrBlock'
		"RootBlock": (110, 2, (9, 0), (), "RootBlock", '{E2CD1C5F-0EE9-4349-B08A-FA34A84CB2F1}'),
		"SnapshotName": (113, 2, (8, 0), (), "SnapshotName", None),
		# Method 'SymbolLocations' returns object of type 'IMGCVariantMgrSymbolLocations'
		"SymbolLocations": (105, 2, (9, 0), ((12, 17),), "SymbolLocations", '{786637F8-9407-11D2-89D9-0020184077E1}'),
		# Method 'Symbols' returns object of type 'IMGCVariantMgrSymbols'
		"Symbols": (101, 2, (9, 0), ((12, 17),), "Symbols", '{786637F7-9407-11D2-89D9-0020184077E1}'),
	}
	_prop_map_put_ = {
		"AccessLock": ((5, LCID, 4, 0),()),
		"AppName": ((115, LCID, 4, 0),()),
		"Parent": ((1, LCID, 8, 0),()),
		"SnapshotName": ((113, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMGCVariantMgrDocument(DispatchBaseClass):
	'Variant manager document object'
	CLSID = IID('{78663807-9407-11D2-89D9-0020184077E1}')
	coclass_clsid = IID('{8B45CE2D-6CF5-1014-857A-77B9EECCF0AC}')

	def AcquireSessionWriteMode(self, requestForRelease=defaultNamedNotOptArg, currentEditUser=pythoncom.Missing, returnStatusInfo=pythoncom.Missing):
		'Tries to acquire a session edit mode privilege'
		return self._ApplyTypes_(140, 1, (11, 0), ((11, 1), (16392, 2), (16392, 2)), 'AcquireSessionWriteMode', None,requestForRelease
			, currentEditUser, returnStatusInfo)

	def ApplyBorderPropModsToAllSymbols(self, pVariant=defaultNamedNotOptArg):
		'Apply Border Prop modification to all border symbols.'
		return self._oleobj_.InvokeTypes(175, LCID, 1, (24, 0), ((9, 1),),pVariant
			)

	def Close(self):
		'Closes the document'
		return self._oleobj_.InvokeTypes(111, LCID, 1, (2, 0), (),)

	def CloseICDB(self):
		'Closes the iCDB database'
		return self._oleobj_.InvokeTypes(179, LCID, 1, (2, 0), (),)

	def CompareUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Compares a UID with the UID of the object. Returns true if equal.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((19, 1), (19, 1), (19, 1)),userID
			, objectID, objectType)

	def CreateDxdFunViewDefFile(self, outFileName=defaultNamedNotOptArg, pObj=defaultNamedNotOptArg, symbDispMode=defaultNamedNotOptArg, unplaceColorRed=defaultNamedNotOptArg
			, unplaceColorGreen=defaultNamedNotOptArg, unplaceColorBlue=defaultNamedNotOptArg, pnumInfoData=defaultNamedNotOptArg, rplStrings=defaultNamedNotOptArg, result=defaultNamedNotOptArg):
		'Construct a Dxd function viewdef file'
		return self._oleobj_.InvokeTypes(158, LCID, 1, (24, 0), ((8, 1), (9, 1), (3, 1), (3, 1), (3, 1), (3, 1), (8, 1), (8, 1), (16386, 1)),outFileName
			, pObj, symbDispMode, unplaceColorRed, unplaceColorGreen, unplaceColorBlue
			, pnumInfoData, rplStrings, result)

	def CreateDxdViewDefFile(self, outFileName=defaultNamedNotOptArg, pObj=defaultNamedNotOptArg, symbDispMode=defaultNamedNotOptArg, unplaceColorRed=defaultNamedNotOptArg
			, unplaceColorGreen=defaultNamedNotOptArg, unplaceColorBlue=defaultNamedNotOptArg, pnumInfoData=defaultNamedNotOptArg, rplStrings=defaultNamedNotOptArg, borderProps=defaultNamedNotOptArg
			, result=defaultNamedNotOptArg):
		'Construct a Dxd viewdef file'
		return self._oleobj_.InvokeTypes(138, LCID, 1, (24, 0), ((8, 1), (9, 1), (3, 1), (3, 1), (3, 1), (3, 1), (8, 1), (8, 1), (12, 1), (16386, 1)),outFileName
			, pObj, symbDispMode, unplaceColorRed, unplaceColorGreen, unplaceColorBlue
			, pnumInfoData, rplStrings, borderProps, result)

	def DeleteBorderPropModsFromAllSymbols(self, propName=defaultNamedNotOptArg, pVariant=defaultNamedNotOptArg):
		'Delete Border Prop modification from all border symbols.'
		return self._oleobj_.InvokeTypes(176, LCID, 1, (24, 0), ((8, 1), (9, 1)),propName
			, pVariant)

	def DumpDB(self, Path=defaultNamedNotOptArg):
		'Dump database into file.'
		return self._oleobj_.InvokeTypes(170, LCID, 1, (2, 0), ((8, 1),),Path
			)

	# Result is of type IMGCVariantMgrFMVFunction
	def FindFMVFunction(self, Name=defaultNamedNotOptArg):
		'Finds an FMV function object'
		ret = self._oleobj_.InvokeTypes(136, LCID, 1, (9, 0), ((8, 1),),Name
			)
		if ret is not None:
			ret = Dispatch(ret, 'FindFMVFunction', '{786637FB-9407-11D2-89D9-0020184077E1}')
		return ret

	# Result is of type IMGCVariantMgrFMVFunction
	def FindFMVFunctionByUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Finds a FMV function object bu UID'
		ret = self._oleobj_.InvokeTypes(153, LCID, 1, (9, 0), ((3, 1), (3, 1), (3, 1)),userID
			, objectID, objectType)
		if ret is not None:
			ret = Dispatch(ret, 'FindFMVFunctionByUID', '{786637FB-9407-11D2-89D9-0020184077E1}')
		return ret

	# Result is of type IMGCVariantMgrVariant
	def FindVariant(self, Name=defaultNamedNotOptArg):
		'Finds a variant object'
		ret = self._oleobj_.InvokeTypes(117, LCID, 1, (9, 0), ((8, 1),),Name
			)
		if ret is not None:
			ret = Dispatch(ret, 'FindVariant', '{78663802-9407-11D2-89D9-0020184077E1}')
		return ret

	# Result is of type IMGCVariantMgrVariant
	def FindVariantByUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Finds a variant object bu UID'
		ret = self._oleobj_.InvokeTypes(152, LCID, 1, (9, 0), ((3, 1), (3, 1), (3, 1)),userID
			, objectID, objectType)
		if ret is not None:
			ret = Dispatch(ret, 'FindVariantByUID', '{78663802-9407-11D2-89D9-0020184077E1}')
		return ret

	def GetErrorString(self, Type=defaultNamedNotOptArg):
		'Returns the error string for the given type.'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(181, LCID, 1, (8, 0), ((3, 1),),Type
			)

	# Result is of type IMGCVariantMgrFMVFunctions
	# The method GetFMVFunctions is actually a property, but must be used as a method to correctly pass the arguments
	def GetFMVFunctions(self, filter=defaultNamedOptArg):
		"Returns a collection of FMV's."
		ret = self._oleobj_.InvokeTypes(103, LCID, 2, (9, 0), ((12, 17),),filter
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetFMVFunctions', '{786637FC-9407-11D2-89D9-0020184077E1}')
		return ret

	def GetPathIndex(self, pagename=defaultNamedNotOptArg):
		'The page name of the schematic'
		return self._oleobj_.InvokeTypes(159, LCID, 1, (2, 0), ((8, 1),),pagename
			)

	def GetPlacedVariants(self, packName=defaultNamedNotOptArg, cleanupNames=defaultNamedNotOptArg, allPlacedReturnsEmpty=defaultNamedNotOptArg, arrayOfVariants=pythoncom.Missing
			, numVariants=pythoncom.Missing):
		'Returns the variants in which a given package is placed.'
		return self._ApplyTypes_(144, 1, (2, 0), ((8, 1), (11, 1), (11, 1), (16396, 2), (16387, 2)), 'GetPlacedVariants', None,packName
			, cleanupNames, allPlacedReturnsEmpty, arrayOfVariants, numVariants)

	def GetSessionsStatus(self, numSessions=pythoncom.Missing, editingUserName=pythoncom.Missing):
		'Return the sessions information status.'
		return self._ApplyTypes_(142, 1, (24, 0), ((16387, 2), (16392, 2)), 'GetSessionsStatus', None,numSessions
			, editingUserName)

	def GetUID(self, userID=pythoncom.Missing, objectID=pythoncom.Missing, objectType=pythoncom.Missing):
		'Gets the UID of an object. Returns false if the UID is invalid.'
		return self._ApplyTypes_(6, 1, (11, 0), ((16403, 2), (16403, 2), (16403, 2)), 'GetUID', None,userID
			, objectID, objectType)

	# Result is of type IMGCVariantMgrVariants
	# The method GetVariants is actually a property, but must be used as a method to correctly pass the arguments
	def GetVariants(self, filter=defaultNamedOptArg):
		'Returns the collection of variants.'
		ret = self._oleobj_.InvokeTypes(104, LCID, 2, (9, 0), ((12, 17),),filter
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetVariants', '{78663803-9407-11D2-89D9-0020184077E1}')
		return ret

	def IncModificationCount(self, value=1):
		'Increments the modification count'
		return self._oleobj_.InvokeTypes(23, LCID, 1, (2, 0), ((2, 49),),value
			)

	def IsICDBNewFormat(self):
		'Returns whether VM data is in new format.'
		return self._oleobj_.InvokeTypes(172, LCID, 1, (11, 0), (),)

	def IsRepackagingNeeded(self):
		'Check if repackaging is needed'
		return self._oleobj_.InvokeTypes(156, LCID, 1, (11, 0), (),)

	def IsReusedBlock(self):
		'Checks if the document represents a reused block.'
		return self._oleobj_.InvokeTypes(133, LCID, 1, (11, 0), (),)

	def IsUpdateRBPending(self, pObj=defaultNamedNotOptArg):
		'Returns whether the selected RB has an update pending.'
		return self._oleobj_.InvokeTypes(177, LCID, 1, (11, 0), ((9, 1),),pObj
			)

	def IsUpgradeFwdBackAnnoNeeded(self, otherSnapshot=defaultNamedNotOptArg):
		'Returns whether FA or BA is needed before opening VM.'
		return self._oleobj_.InvokeTypes(173, LCID, 1, (11, 0), ((8, 1),),otherSnapshot
			)

	def IsValid(self):
		'Returns the internal (CPP) index of the X-Object'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), (),)

	def Load(self, dataSource=defaultNamedNotOptArg, logFile=defaultNamedNotOptArg, variantsDBType=2):
		'Loads the data from a data source'
		return self._oleobj_.InvokeTypes(116, LCID, 1, (2, 0), ((8, 1), (8, 1), (3, 49)),dataSource
			, logFile, variantsDBType)

	def LoadForPCBDesign(self, pcbFilePath=defaultNamedNotOptArg, logFile=defaultNamedNotOptArg, useLayout_Temp=defaultNamedNotOptArg):
		'Loads the data based on a PCB file spec'
		return self._oleobj_.InvokeTypes(139, LCID, 1, (2, 0), ((8, 1), (8, 1), (11, 1)),pcbFilePath
			, logFile, useLayout_Temp)

	def LoadSelective(self, dataSource=defaultNamedNotOptArg, logFile=defaultNamedNotOptArg, loadSelection=268435455, variantsDBType=2):
		'Loads the data from a data source (allowing a load selection filter)'
		return self._oleobj_.InvokeTypes(131, LCID, 1, (2, 0), ((8, 1), (8, 1), (3, 49), (3, 49)),dataSource
			, logFile, loadSelection, variantsDBType)

	def LoadTestData(self, dataSet=defaultNamedNotOptArg):
		'Loads test data set for testing.'
		return self._oleobj_.InvokeTypes(113, LCID, 1, (24, 0), ((2, 1),),dataSet
			)

	# Result is of type IMGCVariantMgrFMVFunction
	def PutFMVFunction(self, functionName=defaultNamedNotOptArg, functionNumber=defaultNamedNotOptArg, functionDescription=defaultNamedNotOptArg, sourceForContents=defaultNamedOptArg):
		'Creates a new FMV function.'
		ret = self._oleobj_.InvokeTypes(135, LCID, 1, (9, 0), ((8, 1), (8, 1), (8, 1), (12, 17)),functionName
			, functionNumber, functionDescription, sourceForContents)
		if ret is not None:
			ret = Dispatch(ret, 'PutFMVFunction', '{786637FB-9407-11D2-89D9-0020184077E1}')
		return ret

	# Result is of type IMGCVariantMgrPackage
	def PutPackage(self):
		'Creates a new package.'
		ret = self._oleobj_.InvokeTypes(167, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'PutPackage', '{786637F5-9407-11D2-89D9-0020184077E1}')
		return ret

	# Result is of type IMGCVariantMgrSymbol
	def PutSymbol(self):
		'Creates a new symbol.'
		ret = self._oleobj_.InvokeTypes(168, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'PutSymbol', '{786637F4-9407-11D2-89D9-0020184077E1}')
		return ret

	# Result is of type IMGCVariantMgrVariant
	def PutVariant(self, variantName=defaultNamedNotOptArg, variantNumber=defaultNamedNotOptArg, variantDescription=defaultNamedNotOptArg, sourceForContents=defaultNamedOptArg):
		'Creates a new variant.'
		ret = self._oleobj_.InvokeTypes(122, LCID, 1, (9, 0), ((8, 1), (8, 1), (8, 1), (12, 17)),variantName
			, variantNumber, variantDescription, sourceForContents)
		if ret is not None:
			ret = Dispatch(ret, 'PutVariant', '{78663802-9407-11D2-89D9-0020184077E1}')
		return ret

	def ReleaseSession(self):
		'Releases a session in the sessions file.'
		return self._oleobj_.InvokeTypes(148, LCID, 1, (11, 0), (),)

	def ReleaseSessionWriteMode(self, notifyOtherUsers=defaultNamedNotOptArg):
		'Releases the session write mode.'
		return self._oleobj_.InvokeTypes(141, LCID, 1, (11, 0), ((11, 1),),notifyOtherUsers
			)

	def Save(self):
		'Saves the document'
		return self._oleobj_.InvokeTypes(128, LCID, 1, (2, 0), (),)

	def SaveAs(self, fileName=defaultNamedNotOptArg, dbType=1):
		'Saves the document under a different name.'
		return self._oleobj_.InvokeTypes(129, LCID, 1, (2, 0), ((8, 1), (3, 49)),fileName
			, dbType)

	def SaveNotesLayers(self):
		'Saves Notes Layers changes.'
		return self._oleobj_.InvokeTypes(186, LCID, 1, (2, 0), (),)

	def SaveVariantsInfoFile(self, fileName=defaultNamedNotOptArg):
		'Saves the variant info file (used by FablinkXE)'
		return self._oleobj_.InvokeTypes(149, LCID, 1, (2, 0), ((8, 1),),fileName
			)

	def SetInternalValue(self, id=defaultNamedNotOptArg, parm1=defaultNamedOptArg, parm2=defaultNamedOptArg, parm3=defaultNamedOptArg):
		'Sets an internal value on an object'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (2, 0), ((8, 1), (12, 17), (12, 17), (12, 17)),id
			, parm1, parm2, parm3)

	def SetReuseBlockParams(self, reuseBlockName=defaultNamedNotOptArg, iCDBDir=defaultNamedNotOptArg, snapshot=defaultNamedNotOptArg, RootBlock=defaultNamedNotOptArg):
		'Stores reuse database params'
		return self._oleobj_.InvokeTypes(165, LCID, 1, (24, 0), ((8, 1), (8, 1), (8, 1), (8, 1)),reuseBlockName
			, iCDBDir, snapshot, RootBlock)

	# The method SetTimeStamp is actually a property, but must be used as a method to correctly pass the arguments
	def SetTimeStamp(self, tsType=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		'Returns or sets the timestamp of a given type.'
		return self._oleobj_.InvokeTypes(145, LCID, 4, (24, 0), ((3, 1), (3, 1)),tsType
			, arg1)

	def SetUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Sets the UID of an object. Returns false if the UID is invalid.'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (11, 0), ((19, 1), (19, 1), (19, 1)),userID
			, objectID, objectType)

	# The method TimeStamp is actually a property, but must be used as a method to correctly pass the arguments
	def TimeStamp(self, tsType=defaultNamedNotOptArg):
		'Returns or sets the timestamp of a given type.'
		return self._oleobj_.InvokeTypes(145, LCID, 2, (3, 0), ((3, 1),),tsType
			)

	# The method TimeStampString is actually a property, but must be used as a method to correctly pass the arguments
	def TimeStampString(self, tsType=defaultNamedNotOptArg):
		'Returns or sets the timestamp string of a given type.'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(146, LCID, 2, (8, 0), ((3, 1),),tsType
			)

	def TransactionEnd(self, transActionID=defaultNamedNotOptArg, commitChanges=True):
		'Ends a transaction on the document.'
		return self._oleobj_.InvokeTypes(121, LCID, 1, (11, 0), ((3, 1), (11, 49)),transActionID
			, commitChanges)

	def TransactionStart(self):
		'Starts a transaction on the document.'
		return self._oleobj_.InvokeTypes(120, LCID, 1, (3, 0), (),)

	def UpdateCentralLibProps(self, CentLibPropsList=defaultNamedNotOptArg):
		'Updates the list of central library properties selected for display in the grid.'
		return self._oleobj_.InvokeTypes(183, LCID, 1, (2, 0), ((8, 1),),CentLibPropsList
			)

	_prop_map_get_ = {
		"AccessLock": (5, 2, (3, 0), (), "AccessLock", None),
		"AliasPartNumberAttribute": (185, 2, (8, 0), (), "AliasPartNumberAttribute", None),
		"AttributePartName": (163, 2, (8, 0), (), "AttributePartName", None),
		# Method 'BPropModsUtility' returns object of type 'IMGCVariantMgrBPropModsUtility'
		"BPropModsUtility": (174, 2, (9, 0), (), "BPropModsUtility", '{BC1CC3A2-E4A4-4A3D-B400-50F80D7D8A39}'),
		"CentralLibProps": (182, 2, (8, 0), (), "CentralLibProps", None),
		# Method 'Connectivity' returns object of type 'IMGCVariantMgrConnectivity'
		"Connectivity": (105, 2, (9, 0), (), "Connectivity", '{82CD5AA6-9407-11D2-89D9-0020184077E1}'),
		"Description": (101, 2, (8, 0), (), "Description", None),
		# Method 'FMVFunctions' returns object of type 'IMGCVariantMgrFMVFunctions'
		"FMVFunctions": (103, 2, (9, 0), ((12, 17),), "FMVFunctions", '{786637FC-9407-11D2-89D9-0020184077E1}'),
		"FXEGenerateSilkscreenFlag": (157, 2, (11, 0), (), "FXEGenerateSilkscreenFlag", None),
		"FlowID": (161, 2, (3, 0), (), "FlowID", None),
		# Method 'Groupings' returns object of type 'IMGCVariantMgrGroupings'
		"Groupings": (106, 2, (9, 0), (), "Groupings", '{82CD5AA7-9407-11D2-89D9-0020184077E1}'),
		"ICDBOfflineMode": (147, 2, (11, 0), (), "ICDBOfflineMode", None),
		"InternalIndex": (2, 2, (3, 0), (), "InternalIndex", None),
		"LauncherAddress": (160, 2, (8, 0), (), "LauncherAddress", None),
		# Method 'MessageMgr' returns object of type 'IMGCVariantMgrMessageMgr'
		"MessageMgr": (137, 2, (9, 0), (), "MessageMgr", '{F22A8EE1-16C5-47E6-A722-C17868D6B486}'),
		"ModificationCount": (20, 2, (2, 0), (), "ModificationCount", None),
		"ModificationCountEx": (24, 2, (3, 0), (), "ModificationCountEx", None),
		"ModificationCountLock": (21, 2, (11, 0), (), "ModificationCountLock", None),
		"Name": (30, 2, (8, 0), (), "Name", None),
		"NotesLayers": (184, 2, (8, 0), (), "NotesLayers", None),
		# Method 'PModsUtility' returns object of type 'IMGCVariantMgrPModsUtility'
		"PModsUtility": (150, 2, (9, 0), (), "PModsUtility", '{D391142F-058C-49E2-85CF-30DA3D2886BA}'),
		"Parent": (1, 2, (9, 0), (), "Parent", None),
		"ProjectFile": (178, 2, (8, 0), (), "ProjectFile", None),
		"ReadOnly": (166, 2, (11, 0), (), "ReadOnly", None),
		"RefDesName": (164, 2, (8, 0), (), "RefDesName", None),
		# Method 'Reporter' returns object of type 'IMGCVariantMgrReporter'
		"Reporter": (132, 2, (9, 0), (), "Reporter", '{017BAF92-95BB-4AD2-BCF6-43DC7A60BAA8}'),
		"ReusedBlocksLibTopDir": (130, 2, (8, 0), (), "ReusedBlocksLibTopDir", None),
		"RootBlockName": (154, 2, (8, 0), (), "RootBlockName", None),
		# Method 'RootIF' returns object of type 'IMGCVariantMgrDocument'
		"RootIF": (22, 2, (9, 0), (), "RootIF", '{78663807-9407-11D2-89D9-0020184077E1}'),
		"RunEventObserver": (169, 2, (11, 0), (), "RunEventObserver", None),
		# Method 'SInfoRecsUtility' returns object of type 'IMGCVariantMgrSInfoRecsUtility'
		"SInfoRecsUtility": (151, 2, (9, 0), (), "SInfoRecsUtility", '{7D8CEF26-776A-40B2-A99C-C6B2358E0C60}'),
		# Method 'Settings' returns object of type 'IMGCVariantMgrSettings'
		"Settings": (109, 2, (9, 0), (), "Settings", '{7866380B-9407-11D2-89D9-0020184077E1}'),
		"ShowSymbolReplacements": (180, 2, (11, 0), (), "ShowSymbolReplacements", None),
		"TemporaryDatabase": (155, 2, (11, 0), (), "TemporaryDatabase", None),
		"UserName": (143, 2, (8, 0), (), "UserName", None),
		# Method 'Utility' returns object of type 'IMGCVariantMgrUtility'
		"Utility": (125, 2, (9, 0), (), "Utility", '{EE5CB44B-13CF-480C-B096-5A2D731A9535}'),
		# Method 'VariantInfoRecsUtility' returns object of type 'IMGCVariantMgrVariantInfoRecsUtility'
		"VariantInfoRecsUtility": (162, 2, (9, 0), (), "VariantInfoRecsUtility", '{138F998B-642F-436E-BEA2-986E1B29A353}'),
		# Method 'Variants' returns object of type 'IMGCVariantMgrVariants'
		"Variants": (104, 2, (9, 0), ((12, 17),), "Variants", '{78663803-9407-11D2-89D9-0020184077E1}'),
		"VariantsDBFilename": (126, 2, (8, 0), (), "VariantsDBFilename", None),
		"iCDBClientName": (171, 2, (8, 0), (), "iCDBClientName", None),
		"variantsDBType": (127, 2, (3, 0), (), "variantsDBType", None),
	}
	_prop_map_put_ = {
		"AccessLock": ((5, LCID, 4, 0),()),
		"AliasPartNumberAttribute": ((185, LCID, 4, 0),()),
		"AttributePartName": ((163, LCID, 4, 0),()),
		"CentralLibProps": ((182, LCID, 4, 0),()),
		"Description": ((101, LCID, 4, 0),()),
		"FXEGenerateSilkscreenFlag": ((157, LCID, 4, 0),()),
		"FlowID": ((161, LCID, 4, 0),()),
		"ICDBOfflineMode": ((147, LCID, 4, 0),()),
		"LauncherAddress": ((160, LCID, 4, 0),()),
		"ModificationCount": ((20, LCID, 4, 0),()),
		"ModificationCountEx": ((24, LCID, 4, 0),()),
		"ModificationCountLock": ((21, LCID, 4, 0),()),
		"Name": ((30, LCID, 4, 0),()),
		"Parent": ((1, LCID, 8, 0),()),
		"ProjectFile": ((178, LCID, 4, 0),()),
		"RefDesName": ((164, LCID, 4, 0),()),
		"ReusedBlocksLibTopDir": ((130, LCID, 4, 0),()),
		"RootBlockName": ((154, LCID, 4, 0),()),
		"RunEventObserver": ((169, LCID, 4, 0),()),
		"ShowSymbolReplacements": ((180, LCID, 4, 0),()),
		"TemporaryDatabase": ((155, LCID, 4, 0),()),
		"UserName": ((143, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMGCVariantMgrDocuments(DispatchBaseClass):
	'Variant manager collection of open documents'
	CLSID = IID('{7866380E-9407-11D2-89D9-0020184077E1}')
	coclass_clsid = IID('{7866380E-9407-20D2-89D9-0020184077E1}')

	def Add(self, pVariant=defaultNamedNotOptArg):
		'Adds a variant to the collection.'
		return self._oleobj_.InvokeTypes(102, LCID, 1, (24, 0), ((9, 1),),pVariant
			)

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
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, index=defaultNamedNotOptArg):
		'Returns a document object at a given index.'
		ret = self._oleobj_.InvokeTypes(101, LCID, 2, (9, 0), ((12, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{78663807-9407-11D2-89D9-0020184077E1}')
		return ret

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
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{78663807-9407-11D2-89D9-0020184077E1}')
	#This class has Item property/method which allows indexed access with the object[key] syntax.
	#Some objects will accept a string or other type of key in addition to integers.
	#Note that many Office objects do not use zero-based indexing.
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(101, LCID, 2, 1, key)), "Item", '{78663807-9407-11D2-89D9-0020184077E1}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(30, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IMGCVariantMgrEditor(DispatchBaseClass):
	'Variant manager editor object'
	CLSID = IID('{82CD5AAD-9407-11D2-89D9-0020184077E1}')
	coclass_clsid = IID('{82CD5AAE-9407-11D2-89D9-0020184077E1}')

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
		"EditorApplication": (101, 2, (9, 0), (), "EditorApplication", None),
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
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMGCVariantMgrEditors(DispatchBaseClass):
	'Variant manager editors collection'
	CLSID = IID('{34842ABE-9E81-4B7D-A5D3-35C68F327A36}')
	coclass_clsid = IID('{FFA514B3-BAE3-4AF0-8611-E2FF01E3C9D1}')

	def CompareUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Compares a UID with the UID of the object. Returns true if equal.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((19, 1), (19, 1), (19, 1)),userID
			, objectID, objectType)

	# Result is of type IMGCVariantMgrEditor
	def CreateInstance(self, pEditorHost=defaultNamedNotOptArg):
		'Adds a variant to the collection.'
		ret = self._oleobj_.InvokeTypes(102, LCID, 1, (9, 0), ((9, 1),),pEditorHost
			)
		if ret is not None:
			ret = Dispatch(ret, 'CreateInstance', '{82CD5AAD-9407-11D2-89D9-0020184077E1}')
		return ret

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

	# Result is of type IMGCVariantMgrEditor
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, index=defaultNamedNotOptArg):
		'Returns an object at a given index.'
		ret = self._oleobj_.InvokeTypes(101, LCID, 2, (9, 0), ((12, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{82CD5AAD-9407-11D2-89D9-0020184077E1}')
		return ret

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
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{82CD5AAD-9407-11D2-89D9-0020184077E1}')
	#This class has Item property/method which allows indexed access with the object[key] syntax.
	#Some objects will accept a string or other type of key in addition to integers.
	#Note that many Office objects do not use zero-based indexing.
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(101, LCID, 2, 1, key)), "Item", '{82CD5AAD-9407-11D2-89D9-0020184077E1}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(30, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IMGCVariantMgrEquivPartsSettings(DispatchBaseClass):
	'Defines the settings to be used for equivalent part retrieval'
	CLSID = IID('{82CD5AB2-9407-11D2-89D9-0020184077E1}')
	coclass_clsid = IID('{82CD5AB5-9407-11D2-89D9-0020184077E1}')

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
		# Method 'Parameters' returns object of type 'IMGCVariantMgrParameters'
		"Parameters": (101, 2, (9, 0), (), "Parameters", '{82CD5AB0-9407-11D2-89D9-0020184077E1}'),
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
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMGCVariantMgrEquivalentBlock(DispatchBaseClass):
	'Describes an equivalent block.'
	CLSID = IID('{AA3E0FAD-2AD6-4FE3-93CC-98A117DC9F0D}')
	coclass_clsid = IID('{C8379667-6E7B-4C72-ADA1-EB298F1019EF}')

	def CompareUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Compares a UID with the UID of the object. Returns true if equal.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((19, 1), (19, 1), (19, 1)),userID
			, objectID, objectType)

	def GetUID(self, userID=pythoncom.Missing, objectID=pythoncom.Missing, objectType=pythoncom.Missing):
		'Gets the UID of an object. Returns false if the UID is invalid.'
		return self._ApplyTypes_(6, 1, (11, 0), ((16403, 2), (16403, 2), (16403, 2)), 'GetUID', None,userID
			, objectID, objectType)

	def IsTemplateBlock(self):
		'Checks if the block is the the template block'
		return self._oleobj_.InvokeTypes(100, LCID, 1, (11, 0), (),)

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
		# Method 'Block' returns object of type 'IMGCVariantMgrBlock'
		"Block": (101, 2, (9, 0), (), "Block", '{E2CD1C5F-0EE9-4349-B08A-FA34A84CB2F1}'),
		"InternalIndex": (2, 2, (3, 0), (), "InternalIndex", None),
		"KeepInSyncWithTemplate": (102, 2, (11, 0), (), "KeepInSyncWithTemplate", None),
		"Parent": (1, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
		"AccessLock": ((5, LCID, 4, 0),()),
		"KeepInSyncWithTemplate": ((102, LCID, 4, 0),()),
		"Parent": ((1, LCID, 8, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMGCVariantMgrEquivalentBlockGroup(DispatchBaseClass):
	'Describes an equivalent block group.'
	CLSID = IID('{4FC18EAE-75C9-4A49-9E38-20ADD79456B5}')
	coclass_clsid = IID('{9E3B1A5B-EE91-4D46-A4C9-C08E93177145}')

	def CompareUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Compares a UID with the UID of the object. Returns true if equal.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((19, 1), (19, 1), (19, 1)),userID
			, objectID, objectType)

	# Result is of type IMGCVariantMgrEquivalentBlocks
	# The method GetEquivalentBlocks is actually a property, but must be used as a method to correctly pass the arguments
	def GetEquivalentBlocks(self, filter=defaultNamedOptArg):
		'Returns a collection of equivalent blocks for this equivalent block group.'
		ret = self._oleobj_.InvokeTypes(102, LCID, 2, (9, 0), ((12, 17),),filter
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetEquivalentBlocks', '{CD2C5AF6-5000-4C95-9879-2F7FB2BA85DD}')
		return ret

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
		# Method 'EquivalentBlocks' returns object of type 'IMGCVariantMgrEquivalentBlocks'
		"EquivalentBlocks": (102, 2, (9, 0), ((12, 17),), "EquivalentBlocks", '{CD2C5AF6-5000-4C95-9879-2F7FB2BA85DD}'),
		"InternalIndex": (2, 2, (3, 0), (), "InternalIndex", None),
		"Parent": (1, 2, (9, 0), (), "Parent", None),
		"SchematicName": (100, 2, (8, 0), (), "SchematicName", None),
		# Method 'TemplateBlock' returns object of type 'IMGCVariantMgrEquivalentBlock'
		"TemplateBlock": (101, 2, (9, 0), (), "TemplateBlock", '{AA3E0FAD-2AD6-4FE3-93CC-98A117DC9F0D}'),
	}
	_prop_map_put_ = {
		"AccessLock": ((5, LCID, 4, 0),()),
		"Parent": ((1, LCID, 8, 0),()),
		"TemplateBlock": ((101, LCID, 8, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMGCVariantMgrEquivalentBlockGroups(DispatchBaseClass):
	'Describes a collection of equivalent block groups.'
	CLSID = IID('{98301621-82F9-4458-996F-46739708B82C}')
	coclass_clsid = IID('{710F3F51-7D50-4A3C-B171-E9F1BBBF5530}')

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

	# Result is of type IMGCVariantMgrEquivalentBlockGroup
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, index=defaultNamedNotOptArg):
		'Returns an equivalent block group definition.'
		ret = self._oleobj_.InvokeTypes(101, LCID, 2, (9, 0), ((12, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{4FC18EAE-75C9-4A49-9E38-20ADD79456B5}')
		return ret

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
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{4FC18EAE-75C9-4A49-9E38-20ADD79456B5}')
	#This class has Item property/method which allows indexed access with the object[key] syntax.
	#Some objects will accept a string or other type of key in addition to integers.
	#Note that many Office objects do not use zero-based indexing.
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(101, LCID, 2, 1, key)), "Item", '{4FC18EAE-75C9-4A49-9E38-20ADD79456B5}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(30, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IMGCVariantMgrEquivalentBlocks(DispatchBaseClass):
	'Describes a collection of equivalent blocks.'
	CLSID = IID('{CD2C5AF6-5000-4C95-9879-2F7FB2BA85DD}')
	coclass_clsid = IID('{3E00E7A9-47FF-4E25-B76E-BECE98E42007}')

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

	# Result is of type IMGCVariantMgrEquivalentBlock
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, index=defaultNamedNotOptArg):
		'Returns an equivalent block definition.'
		ret = self._oleobj_.InvokeTypes(101, LCID, 2, (9, 0), ((12, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{AA3E0FAD-2AD6-4FE3-93CC-98A117DC9F0D}')
		return ret

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
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{AA3E0FAD-2AD6-4FE3-93CC-98A117DC9F0D}')
	#This class has Item property/method which allows indexed access with the object[key] syntax.
	#Some objects will accept a string or other type of key in addition to integers.
	#Note that many Office objects do not use zero-based indexing.
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(101, LCID, 2, 1, key)), "Item", '{AA3E0FAD-2AD6-4FE3-93CC-98A117DC9F0D}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(30, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IMGCVariantMgrFMVFunction(DispatchBaseClass):
	'Variant manager function object'
	CLSID = IID('{786637FB-9407-11D2-89D9-0020184077E1}')
	coclass_clsid = IID('{786637FB-9407-20D2-89D9-0020184077E1}')

	def CompareUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Compares a UID with the UID of the object. Returns true if equal.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((19, 1), (19, 1), (19, 1)),userID
			, objectID, objectType)

	def Delete(self):
		'Deletes the FMV function'
		return self._oleobj_.InvokeTypes(111, LCID, 1, (11, 0), (),)

	def DeleteVariantAssignment(self, variantDefinition=defaultNamedNotOptArg):
		'Delete a variant assignment.'
		return self._oleobj_.InvokeTypes(110, LCID, 1, (2, 0), ((12, 1),),variantDefinition
			)

	# Result is of type IMGCVariantMgrVariantAssignment
	def FindVariantAssignment(self, variantDefinition=defaultNamedNotOptArg):
		'Find a variant assignment for a variant.'
		ret = self._oleobj_.InvokeTypes(109, LCID, 1, (9, 0), ((12, 1),),variantDefinition
			)
		if ret is not None:
			ret = Dispatch(ret, 'FindVariantAssignment', '{874DEFFA-9480-4725-BCE3-06FE0427B1CA}')
		return ret

	def GetUID(self, userID=pythoncom.Missing, objectID=pythoncom.Missing, objectType=pythoncom.Missing):
		'Gets the UID of an object. Returns false if the UID is invalid.'
		return self._ApplyTypes_(6, 1, (11, 0), ((16403, 2), (16403, 2), (16403, 2)), 'GetUID', None,userID
			, objectID, objectType)

	# Result is of type IMGCVariantMgrVariantAssignments
	# The method GetVariantAssignments is actually a property, but must be used as a method to correctly pass the arguments
	def GetVariantAssignments(self, filter=defaultNamedOptArg):
		'Returns a collection of variants that are assigned to this function'
		ret = self._oleobj_.InvokeTypes(106, LCID, 2, (9, 0), ((12, 17),),filter
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetVariantAssignments', '{7255B70F-5A93-4770-8D66-A32C07310BA1}')
		return ret

	def IncModificationCount(self, value=1):
		'Increments the modification count'
		return self._oleobj_.InvokeTypes(23, LCID, 1, (2, 0), ((2, 49),),value
			)

	def IsValid(self):
		'Returns the internal (CPP) index of the X-Object'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), (),)

	def IsVariantAssigned(self, variantName=defaultNamedNotOptArg):
		'Returs a collection of variants that are assigned to this function'
		return self._oleobj_.InvokeTypes(107, LCID, 1, (11, 0), ((8, 1),),variantName
			)

	# Result is of type IMGCVariantMgrVariantAssignment
	def PutVariantAssignment(self, variantDefinition=defaultNamedNotOptArg, position=-1):
		'Adds a new variant assignment to the function'
		ret = self._oleobj_.InvokeTypes(108, LCID, 1, (9, 0), ((12, 1), (2, 49)),variantDefinition
			, position)
		if ret is not None:
			ret = Dispatch(ret, 'PutVariantAssignment', '{874DEFFA-9480-4725-BCE3-06FE0427B1CA}')
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
		"Description": (101, 2, (8, 0), (), "Description", None),
		"FunctionType": (104, 2, (3, 0), (), "FunctionType", None),
		"Hyperlink": (112, 2, (8, 0), (), "Hyperlink", None),
		"InternalIndex": (2, 2, (3, 0), (), "InternalIndex", None),
		"ModificationCount": (20, 2, (2, 0), (), "ModificationCount", None),
		"ModificationCountEx": (24, 2, (3, 0), (), "ModificationCountEx", None),
		"ModificationCountLock": (21, 2, (11, 0), (), "ModificationCountLock", None),
		"Name": (30, 2, (8, 0), (), "Name", None),
		"Parent": (1, 2, (9, 0), (), "Parent", None),
		# Method 'RootIF' returns object of type 'IMGCVariantMgrDocument'
		"RootIF": (22, 2, (9, 0), (), "RootIF", '{78663807-9407-11D2-89D9-0020184077E1}'),
		# Method 'VariantAssignments' returns object of type 'IMGCVariantMgrVariantAssignments'
		"VariantAssignments": (106, 2, (9, 0), ((12, 17),), "VariantAssignments", '{7255B70F-5A93-4770-8D66-A32C07310BA1}'),
	}
	_prop_map_put_ = {
		"AccessLock": ((5, LCID, 4, 0),()),
		"Description": ((101, LCID, 4, 0),()),
		"FunctionType": ((104, LCID, 4, 0),()),
		"Hyperlink": ((112, LCID, 4, 0),()),
		"ModificationCount": ((20, LCID, 4, 0),()),
		"ModificationCountEx": ((24, LCID, 4, 0),()),
		"ModificationCountLock": ((21, LCID, 4, 0),()),
		"Name": ((30, LCID, 4, 0),()),
		"Parent": ((1, LCID, 8, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMGCVariantMgrFMVFunctionAssignment(DispatchBaseClass):
	CLSID = IID('{B531AD99-09B2-4D15-AC0D-8F3A75F64A14}')
	coclass_clsid = IID('{6E1379A7-5ADF-4FCE-AF36-168E470CF199}')

	def CompareUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Compares a UID with the UID of the object. Returns true if equal.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((19, 1), (19, 1), (19, 1)),userID
			, objectID, objectType)

	def Delete(self):
		'Deletes the FMVFunction assignment.'
		return self._oleobj_.InvokeTypes(102, LCID, 1, (11, 0), (),)

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
		# Method 'FMVFunction' returns object of type 'IMGCVariantMgrFMVFunction'
		"FMVFunction": (101, 2, (9, 0), (), "FMVFunction", '{786637FB-9407-11D2-89D9-0020184077E1}'),
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
		"FMVFunction": ((101, LCID, 8, 0),()),
		"ModificationCount": ((20, LCID, 4, 0),()),
		"ModificationCountEx": ((24, LCID, 4, 0),()),
		"ModificationCountLock": ((21, LCID, 4, 0),()),
		"Parent": ((1, LCID, 8, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMGCVariantMgrFMVFunctionAssignments(DispatchBaseClass):
	'Variant assignments collection'
	CLSID = IID('{58977901-B0FA-491B-9F30-75EBA4E8D3C8}')
	coclass_clsid = IID('{ED096F00-ED2B-468F-9E18-C01EF9CB2BEA}')

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

	# Result is of type IMGCVariantMgrFMVFunctionAssignment
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, index=defaultNamedNotOptArg):
		'Returns a package object at a given index.'
		ret = self._oleobj_.InvokeTypes(101, LCID, 2, (9, 0), ((12, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{B531AD99-09B2-4D15-AC0D-8F3A75F64A14}')
		return ret

	def MoveDown(self, pObj=defaultNamedNotOptArg, moveDelta=1):
		'Moves a variant down in the list of variant'
		return self._oleobj_.InvokeTypes(103, LCID, 1, (2, 0), ((9, 1), (2, 49)),pObj
			, moveDelta)

	def MoveUp(self, pObj=defaultNamedNotOptArg, moveDelta=1):
		'Moves a variant up in the list of variant'
		return self._oleobj_.InvokeTypes(102, LCID, 1, (2, 0), ((9, 1), (2, 49)),pObj
			, moveDelta)

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
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{B531AD99-09B2-4D15-AC0D-8F3A75F64A14}')
	#This class has Item property/method which allows indexed access with the object[key] syntax.
	#Some objects will accept a string or other type of key in addition to integers.
	#Note that many Office objects do not use zero-based indexing.
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(101, LCID, 2, 1, key)), "Item", '{B531AD99-09B2-4D15-AC0D-8F3A75F64A14}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(30, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IMGCVariantMgrFMVFunctionGroup(DispatchBaseClass):
	CLSID = IID('{6320E666-2421-4912-AEE9-CFC712EE05C0}')
	coclass_clsid = IID('{5E7CEF6B-E5A9-452B-B757-7ABA3826CBD3}')

	def CompareUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Compares a UID with the UID of the object. Returns true if equal.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((19, 1), (19, 1), (19, 1)),userID
			, objectID, objectType)

	def Delete(self):
		'Deletes the FMV function group.'
		return self._oleobj_.InvokeTypes(105, LCID, 1, (11, 0), (),)

	# Result is of type IMGCVariantMgrFMVFunctionAssignment
	def FindFMVFunctionAssignment(self, variantDefinition=defaultNamedNotOptArg):
		'Find a variant assignment for a variant.'
		ret = self._oleobj_.InvokeTypes(104, LCID, 1, (9, 0), ((12, 1),),variantDefinition
			)
		if ret is not None:
			ret = Dispatch(ret, 'FindFMVFunctionAssignment', '{B531AD99-09B2-4D15-AC0D-8F3A75F64A14}')
		return ret

	# Result is of type IMGCVariantMgrFMVFunctionAssignments
	# The method GetFMVFunctionAssignments is actually a property, but must be used as a method to correctly pass the arguments
	def GetFMVFunctionAssignments(self, filter=defaultNamedOptArg):
		'Returns a collection of functions that are part of the group.'
		ret = self._oleobj_.InvokeTypes(102, LCID, 2, (9, 0), ((12, 17),),filter
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetFMVFunctionAssignments', '{58977901-B0FA-491B-9F30-75EBA4E8D3C8}')
		return ret

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

	# Result is of type IMGCVariantMgrFMVFunctionAssignment
	def PutFMVFunctionAssignment(self, variantDefinition=defaultNamedNotOptArg, position=-1):
		'Adds a new FMVFunction assignment to the group.'
		ret = self._oleobj_.InvokeTypes(103, LCID, 1, (9, 0), ((12, 1), (2, 49)),variantDefinition
			, position)
		if ret is not None:
			ret = Dispatch(ret, 'PutFMVFunctionAssignment', '{B531AD99-09B2-4D15-AC0D-8F3A75F64A14}')
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
		"Description": (101, 2, (8, 0), (), "Description", None),
		# Method 'FMVFunctionAssignments' returns object of type 'IMGCVariantMgrFMVFunctionAssignments'
		"FMVFunctionAssignments": (102, 2, (9, 0), ((12, 17),), "FMVFunctionAssignments", '{58977901-B0FA-491B-9F30-75EBA4E8D3C8}'),
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
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMGCVariantMgrFMVFunctionGroups(DispatchBaseClass):
	'Variant manager variant groups collection'
	CLSID = IID('{AF197ECE-D3D5-4720-AB62-F3F2E0CB52F4}')
	coclass_clsid = IID('{E30ED752-1FD3-4294-AE8D-E8C96944F104}')

	def Add(self, pGroup=defaultNamedNotOptArg):
		'Adds a group to the collection.'
		return self._oleobj_.InvokeTypes(102, LCID, 1, (24, 0), ((9, 1),),pGroup
			)

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

	# Result is of type IMGCVariantMgrFMVFunctionGroup
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, index=defaultNamedNotOptArg):
		'Returns a group object at a given index.'
		ret = self._oleobj_.InvokeTypes(101, LCID, 2, (9, 0), ((12, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{6320E666-2421-4912-AEE9-CFC712EE05C0}')
		return ret

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
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{6320E666-2421-4912-AEE9-CFC712EE05C0}')
	#This class has Item property/method which allows indexed access with the object[key] syntax.
	#Some objects will accept a string or other type of key in addition to integers.
	#Note that many Office objects do not use zero-based indexing.
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(101, LCID, 2, 1, key)), "Item", '{6320E666-2421-4912-AEE9-CFC712EE05C0}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(30, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IMGCVariantMgrFMVFunctions(DispatchBaseClass):
	'Variant manager function collection'
	CLSID = IID('{786637FC-9407-11D2-89D9-0020184077E1}')
	coclass_clsid = IID('{786637FC-9407-20D2-89D9-0020184077E1}')

	def Add(self, pFunction=defaultNamedNotOptArg):
		'Adds a function to the collection.'
		return self._oleobj_.InvokeTypes(102, LCID, 1, (24, 0), ((9, 1),),pFunction
			)

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

	# Result is of type IMGCVariantMgrFMVFunction
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, index=defaultNamedNotOptArg):
		'Returns a function object at a given index.'
		ret = self._oleobj_.InvokeTypes(101, LCID, 2, (9, 0), ((12, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{786637FB-9407-11D2-89D9-0020184077E1}')
		return ret

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
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{786637FB-9407-11D2-89D9-0020184077E1}')
	#This class has Item property/method which allows indexed access with the object[key] syntax.
	#Some objects will accept a string or other type of key in addition to integers.
	#Note that many Office objects do not use zero-based indexing.
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(101, LCID, 2, 1, key)), "Item", '{786637FB-9407-11D2-89D9-0020184077E1}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(30, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IMGCVariantMgrFMVProperties(DispatchBaseClass):
	'Variant manager FMV properties collection'
	CLSID = IID('{3C44AB05-4C95-4984-BD98-135CDD2B39C1}')
	coclass_clsid = IID('{91CE081D-69DF-4940-B2E0-4F304D4E8E62}')

	def Add(self, pSymbIRec=defaultNamedNotOptArg):
		'Adds a symbol info record to the collection.'
		return self._oleobj_.InvokeTypes(102, LCID, 1, (24, 0), ((9, 1),),pSymbIRec
			)

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

	# Result is of type IMGCVariantMgrFMVProperty
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, index=defaultNamedNotOptArg):
		'Returns a symbol modification object at a given index.'
		ret = self._oleobj_.InvokeTypes(101, LCID, 2, (9, 0), ((12, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{DD445D35-DC4B-413A-8781-F561D40D4CC5}')
		return ret

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
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{DD445D35-DC4B-413A-8781-F561D40D4CC5}')
	#This class has Item property/method which allows indexed access with the object[key] syntax.
	#Some objects will accept a string or other type of key in addition to integers.
	#Note that many Office objects do not use zero-based indexing.
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(101, LCID, 2, 1, key)), "Item", '{DD445D35-DC4B-413A-8781-F561D40D4CC5}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(30, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IMGCVariantMgrFMVProperty(DispatchBaseClass):
	'Variant manager FMV property object'
	CLSID = IID('{DD445D35-DC4B-413A-8781-F561D40D4CC5}')
	coclass_clsid = IID('{7B540F5C-2F96-4EEE-8894-F4970320B0D4}')

	def CompareUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Compares a UID with the UID of the object. Returns true if equal.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((19, 1), (19, 1), (19, 1)),userID
			, objectID, objectType)

	def Delete(self):
		'Deletes the symbol modification.'
		return self._oleobj_.InvokeTypes(106, LCID, 1, (11, 0), (),)

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
		"ChangeOperation": (102, 2, (3, 0), (), "ChangeOperation", None),
		# Method 'FMVFunction' returns object of type 'IMGCVariantMgrFMVFunction'
		"FMVFunction": (105, 2, (9, 0), (), "FMVFunction", '{786637FB-9407-11D2-89D9-0020184077E1}'),
		"InternalIndex": (2, 2, (3, 0), (), "InternalIndex", None),
		"ModificationCount": (20, 2, (2, 0), (), "ModificationCount", None),
		"ModificationCountEx": (24, 2, (3, 0), (), "ModificationCountEx", None),
		"ModificationCountLock": (21, 2, (11, 0), (), "ModificationCountLock", None),
		"Name": (30, 2, (8, 0), (), "Name", None),
		"NewAliasPartNumber": (110, 2, (8, 0), (), "NewAliasPartNumber", None),
		"NewCell": (104, 2, (8, 0), (), "NewCell", None),
		"NewPartNumber": (103, 2, (8, 0), (), "NewPartNumber", None),
		"Parent": (1, 2, (9, 0), (), "Parent", None),
		"ReuseAccessMode": (107, 2, (3, 0), (), "ReuseAccessMode", None),
		# Method 'RootIF' returns object of type 'IMGCVariantMgrDocument'
		"RootIF": (22, 2, (9, 0), (), "RootIF", '{78663807-9407-11D2-89D9-0020184077E1}'),
		# Method 'Symbol' returns object of type 'IMGCVariantMgrSymbol'
		"Symbol": (108, 2, (9, 0), (), "Symbol", '{786637F4-9407-11D2-89D9-0020184077E1}'),
	}
	_prop_map_put_ = {
		"AccessLock": ((5, LCID, 4, 0),()),
		"ChangeOperation": ((102, LCID, 4, 0),()),
		"FMVFunction": ((105, LCID, 8, 0),()),
		"MarkForCheckingConflicts": ((109, LCID, 4, 0),()),
		"ModificationCount": ((20, LCID, 4, 0),()),
		"ModificationCountEx": ((24, LCID, 4, 0),()),
		"ModificationCountLock": ((21, LCID, 4, 0),()),
		"Name": ((30, LCID, 4, 0),()),
		"NewAliasPartNumber": ((110, LCID, 4, 0),()),
		"NewCell": ((104, LCID, 4, 0),()),
		"NewPartNumber": ((103, LCID, 4, 0),()),
		"Parent": ((1, LCID, 8, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMGCVariantMgrFilters(DispatchBaseClass):
	'Variant manager filters object'
	CLSID = IID('{C9D96C16-A541-4DA9-97E0-902FCD6C2412}')
	coclass_clsid = IID('{09EDE838-98B4-4D93-A40C-3F43E642EAE1}')

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

	# Result is of type IMGCVariantMgrBlockDataModificationFilter
	def NewBlockDataModificationFilter(self):
		'Finds a variant object'
		ret = self._oleobj_.InvokeTypes(118, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'NewBlockDataModificationFilter', '{761BC783-46D2-4961-835B-653901ED7E7F}')
		return ret

	# Result is of type IMGCVariantMgrBorderPropModificationFilter
	def NewBorderPropModificationFilter(self):
		'Create new border prop modification filter'
		ret = self._oleobj_.InvokeTypes(120, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'NewBorderPropModificationFilter', '{1158040D-F8C4-4865-A4A6-F42D11C258BA}')
		return ret

	# Result is of type IMGCVariantMgrPackageFilter
	def NewPackageFilter(self):
		'Finds a packages object'
		ret = self._oleobj_.InvokeTypes(119, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'NewPackageFilter', '{B01F00BE-D881-46C2-B841-82D35B117ED4}')
		return ret

	# Result is of type IMGCVariantMgrPackageModificationFilter
	def NewPackageModificationFilter(self):
		'Finds a variant object'
		ret = self._oleobj_.InvokeTypes(117, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'NewPackageModificationFilter', '{7E1CD29C-D3B5-4690-91D5-415965F42BA6}')
		return ret

	# Result is of type IMGCVariantMgrSymbolFilter
	def NewSymbolFilter(self):
		'Finds a symbols object'
		ret = self._oleobj_.InvokeTypes(121, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'NewSymbolFilter', '{9ADE593A-D453-4433-B7EF-281D82D31EAD}')
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
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMGCVariantMgrGroupings(DispatchBaseClass):
	'Variant manager groupings objects'
	CLSID = IID('{82CD5AA7-9407-11D2-89D9-0020184077E1}')
	coclass_clsid = IID('{82CD5AAB-9407-11D2-89D9-0020184077E1}')

	def CompareUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Compares a UID with the UID of the object. Returns true if equal.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((19, 1), (19, 1), (19, 1)),userID
			, objectID, objectType)

	# Result is of type IMGCVariantMgrFMVFunctionGroup
	def FindFMVFunctionGroup(self, groupName=defaultNamedNotOptArg):
		'Find a FMV function group in the list of FMV function groups.'
		ret = self._oleobj_.InvokeTypes(105, LCID, 1, (9, 0), ((8, 1),),groupName
			)
		if ret is not None:
			ret = Dispatch(ret, 'FindFMVFunctionGroup', '{6320E666-2421-4912-AEE9-CFC712EE05C0}')
		return ret

	# Result is of type IMGCVariantMgrFMVFunctionGroup
	def FindFMVFunctionGroupByUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Find a FMV function group in the list of FMV function groups.'
		ret = self._oleobj_.InvokeTypes(108, LCID, 1, (9, 0), ((3, 1), (3, 1), (3, 1)),userID
			, objectID, objectType)
		if ret is not None:
			ret = Dispatch(ret, 'FindFMVFunctionGroupByUID', '{6320E666-2421-4912-AEE9-CFC712EE05C0}')
		return ret

	# Result is of type IMGCVariantMgrVariantGroup
	def FindVariantGroup(self, groupName=defaultNamedNotOptArg):
		'Find a variant group in the list of variant groups.'
		ret = self._oleobj_.InvokeTypes(104, LCID, 1, (9, 0), ((8, 1),),groupName
			)
		if ret is not None:
			ret = Dispatch(ret, 'FindVariantGroup', '{3809BA4C-72E2-436F-B258-88EBA46444C8}')
		return ret

	# Result is of type IMGCVariantMgrVariantGroup
	def FindVariantGroupByUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Find a variant group in the list of variant groups.'
		ret = self._oleobj_.InvokeTypes(107, LCID, 1, (9, 0), ((3, 1), (3, 1), (3, 1)),userID
			, objectID, objectType)
		if ret is not None:
			ret = Dispatch(ret, 'FindVariantGroupByUID', '{3809BA4C-72E2-436F-B258-88EBA46444C8}')
		return ret

	# Result is of type IMGCVariantMgrFMVFunctionGroups
	# The method GetFMVFunctionGroups is actually a property, but must be used as a method to correctly pass the arguments
	def GetFMVFunctionGroups(self, filter=defaultNamedOptArg):
		'Returns a collection of FMV function groups.'
		ret = self._oleobj_.InvokeTypes(101, LCID, 2, (9, 0), ((12, 17),),filter
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetFMVFunctionGroups', '{AF197ECE-D3D5-4720-AB62-F3F2E0CB52F4}')
		return ret

	def GetUID(self, userID=pythoncom.Missing, objectID=pythoncom.Missing, objectType=pythoncom.Missing):
		'Gets the UID of an object. Returns false if the UID is invalid.'
		return self._ApplyTypes_(6, 1, (11, 0), ((16403, 2), (16403, 2), (16403, 2)), 'GetUID', None,userID
			, objectID, objectType)

	# Result is of type IMGCVariantMgrVariantGroups
	# The method GetVariantGroups is actually a property, but must be used as a method to correctly pass the arguments
	def GetVariantGroups(self, filter=defaultNamedOptArg):
		'Returns a collection of variant groups.'
		ret = self._oleobj_.InvokeTypes(102, LCID, 2, (9, 0), ((12, 17),),filter
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetVariantGroups', '{19DBCD8C-D9AF-4B85-8439-89F12F23F406}')
		return ret

	def IncModificationCount(self, value=1):
		'Increments the modification count'
		return self._oleobj_.InvokeTypes(23, LCID, 1, (2, 0), ((2, 49),),value
			)

	def IsValid(self):
		'Returns the internal (CPP) index of the X-Object'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), (),)

	# Result is of type IMGCVariantMgrFMVFunctionGroup
	def PutFMVFunctionGroup(self, groupName=defaultNamedNotOptArg, groupDescription=defaultNamedNotOptArg, sourceForContents=defaultNamedOptArg):
		'Creates a new FMV Function group.'
		ret = self._oleobj_.InvokeTypes(106, LCID, 1, (9, 0), ((8, 1), (8, 1), (12, 17)),groupName
			, groupDescription, sourceForContents)
		if ret is not None:
			ret = Dispatch(ret, 'PutFMVFunctionGroup', '{6320E666-2421-4912-AEE9-CFC712EE05C0}')
		return ret

	# Result is of type IMGCVariantMgrVariantGroup
	def PutVariantGroup(self, groupName=defaultNamedNotOptArg, groupDescription=defaultNamedNotOptArg, sourceForContents=defaultNamedOptArg):
		'Creates a new variant group.'
		ret = self._oleobj_.InvokeTypes(103, LCID, 1, (9, 0), ((8, 1), (8, 1), (12, 17)),groupName
			, groupDescription, sourceForContents)
		if ret is not None:
			ret = Dispatch(ret, 'PutVariantGroup', '{3809BA4C-72E2-436F-B258-88EBA46444C8}')
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
		# Method 'FMVFunctionGroups' returns object of type 'IMGCVariantMgrFMVFunctionGroups'
		"FMVFunctionGroups": (101, 2, (9, 0), ((12, 17),), "FMVFunctionGroups", '{AF197ECE-D3D5-4720-AB62-F3F2E0CB52F4}'),
		"InternalIndex": (2, 2, (3, 0), (), "InternalIndex", None),
		"ModificationCount": (20, 2, (2, 0), (), "ModificationCount", None),
		"ModificationCountEx": (24, 2, (3, 0), (), "ModificationCountEx", None),
		"ModificationCountLock": (21, 2, (11, 0), (), "ModificationCountLock", None),
		"Parent": (1, 2, (9, 0), (), "Parent", None),
		# Method 'RootIF' returns object of type 'IMGCVariantMgrDocument'
		"RootIF": (22, 2, (9, 0), (), "RootIF", '{78663807-9407-11D2-89D9-0020184077E1}'),
		# Method 'VariantGroups' returns object of type 'IMGCVariantMgrVariantGroups'
		"VariantGroups": (102, 2, (9, 0), ((12, 17),), "VariantGroups", '{19DBCD8C-D9AF-4B85-8439-89F12F23F406}'),
	}
	_prop_map_put_ = {
		"AccessLock": ((5, LCID, 4, 0),()),
		"ModificationCount": ((20, LCID, 4, 0),()),
		"ModificationCountEx": ((24, LCID, 4, 0),()),
		"ModificationCountLock": ((21, LCID, 4, 0),()),
		"Parent": ((1, LCID, 8, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMGCVariantMgrMessageMgr(DispatchBaseClass):
	'Variant manager message manager object'
	CLSID = IID('{F22A8EE1-16C5-47E6-A722-C17868D6B486}')
	coclass_clsid = IID('{86B24400-555D-49A9-BD72-49260A34A59C}')

	def AddPackageToSendList(self, pPack=defaultNamedNotOptArg):
		'Add a package to the send list'
		return self._oleobj_.InvokeTypes(102, LCID, 1, (24, 0), ((9, 1),),pPack
			)

	def AddPackageToSendListUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Add a package to the send list'
		return self._oleobj_.InvokeTypes(104, LCID, 1, (24, 0), ((19, 1), (19, 1), (19, 1)),userID
			, objectID, objectType)

	def AddSymbolToSendList(self, pSymbol=defaultNamedNotOptArg):
		'Add a symbol to the send list'
		return self._oleobj_.InvokeTypes(101, LCID, 1, (24, 0), ((9, 1),),pSymbol
			)

	def AddSymbolToSendListUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Add a symbol to the send list (UID version)'
		return self._oleobj_.InvokeTypes(103, LCID, 1, (24, 0), ((19, 1), (19, 1), (19, 1)),userID
			, objectID, objectType)

	def BroadcastMessage(self, messageToSend=defaultNamedNotOptArg, categoryID=defaultNamedNotOptArg):
		'Returns the number of items in the send list.'
		return self._oleobj_.InvokeTypes(110, LCID, 1, (2, 0), ((8, 1), (19, 1)),messageToSend
			, categoryID)

	def ClearSendList(self):
		'Clear the list of items to send'
		return self._oleobj_.InvokeTypes(100, LCID, 1, (24, 0), (),)

	def CompareUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Compares a UID with the UID of the object. Returns true if equal.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((19, 1), (19, 1), (19, 1)),userID
			, objectID, objectType)

	def ExecuteSend(self):
		'Returns the number of items in the send list.'
		return self._oleobj_.InvokeTypes(106, LCID, 1, (2, 0), (),)

	def GetUID(self, userID=pythoncom.Missing, objectID=pythoncom.Missing, objectType=pythoncom.Missing):
		'Gets the UID of an object. Returns false if the UID is invalid.'
		return self._ApplyTypes_(6, 1, (11, 0), ((16403, 2), (16403, 2), (16403, 2)), 'GetUID', None,userID
			, objectID, objectType)

	def IsListenerActive(self):
		'Returns the number of items in the send list.'
		return self._oleobj_.InvokeTypes(109, LCID, 1, (11, 0), (),)

	def IsValid(self):
		'Returns the internal (CPP) index of the X-Object'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), (),)

	def PauseListener(self):
		'Pause xprobing.'
		return self._oleobj_.InvokeTypes(111, LCID, 1, (11, 0), (),)

	def RestartListener(self):
		'Restart xprobing.'
		return self._oleobj_.InvokeTypes(112, LCID, 1, (11, 0), (),)

	def SetCrossProbeSnapshot(self, snapshot=defaultNamedNotOptArg):
		'Set name of cross probe snapshot.'
		return self._oleobj_.InvokeTypes(113, LCID, 1, (24, 0), ((8, 1),),snapshot
			)

	def SetInternalValue(self, id=defaultNamedNotOptArg, parm1=defaultNamedOptArg, parm2=defaultNamedOptArg, parm3=defaultNamedOptArg):
		'Sets an internal value on an object'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (2, 0), ((8, 1), (12, 17), (12, 17), (12, 17)),id
			, parm1, parm2, parm3)

	def SetUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Sets the UID of an object. Returns false if the UID is invalid.'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (11, 0), ((19, 1), (19, 1), (19, 1)),userID
			, objectID, objectType)

	def StartListener(self):
		'Starts the message listener.'
		return self._oleobj_.InvokeTypes(107, LCID, 1, (2, 0), (),)

	def StopListener(self):
		'Starts the message listener.'
		return self._oleobj_.InvokeTypes(108, LCID, 1, (2, 0), (),)

	_prop_map_get_ = {
		"AccessLock": (5, 2, (3, 0), (), "AccessLock", None),
		"CountSendList": (105, 2, (3, 0), (), "CountSendList", None),
		"InternalIndex": (2, 2, (3, 0), (), "InternalIndex", None),
		"Parent": (1, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
		"AccessLock": ((5, LCID, 4, 0),()),
		"Parent": ((1, LCID, 8, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMGCVariantMgrOutputGenerator(DispatchBaseClass):
	'Defines the methods and properties of an output generator'
	CLSID = IID('{82CD5AB1-9407-11D2-89D9-0020184077E1}')
	coclass_clsid = IID('{82CD5AB6-9407-11D2-89D9-0020184077E1}')

	def GenerateOutput(self, VariantID=defaultNamedNotOptArg):
		'Generate the output for a variant '
		return self._oleobj_.InvokeTypes(101, LCID, 1, (2, 0), ((8, 1),),VariantID
			)

	def ResetToMaster(self):
		'Reset the client to master mode '
		return self._oleobj_.InvokeTypes(104, LCID, 1, (2, 0), (),)

	def ViewVariant(self, VariantID=defaultNamedNotOptArg):
		'View a variant in the client '
		return self._oleobj_.InvokeTypes(102, LCID, 1, (2, 0), ((8, 1),),VariantID
			)

	_prop_map_get_ = {
		"ErrorCode": (106, 2, (2, 0), (), "ErrorCode", None),
		"ErrorDescription": (107, 2, (8, 0), (), "ErrorDescription", None),
		"MustGeneratebeforeView": (103, 2, (11, 0), (), "MustGeneratebeforeView", None),
		# Method 'Parameters' returns object of type 'IMGCVariantMgrParameters'
		"Parameters": (105, 2, (9, 0), (), "Parameters", '{82CD5AB0-9407-11D2-89D9-0020184077E1}'),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMGCVariantMgrPModsUtility(DispatchBaseClass):
	'Variant manager package modifications utitity object.'
	CLSID = IID('{D391142F-058C-49E2-85CF-30DA3D2886BA}')
	coclass_clsid = IID('{5455892B-A0D3-498F-97D2-4C3F243B276E}')

	def CompareUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Compares a UID with the UID of the object. Returns true if equal.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((19, 1), (19, 1), (19, 1)),userID
			, objectID, objectType)

	# Result is of type IMGCVariantMgrBlockDataModification
	def FindBlockDataModification(self, variantDef=defaultNamedNotOptArg, blockDataDef=defaultNamedNotOptArg):
		'Finds a package modification record'
		ret = self._oleobj_.InvokeTypes(106, LCID, 1, (9, 0), ((12, 1), (12, 1)),variantDef
			, blockDataDef)
		if ret is not None:
			ret = Dispatch(ret, 'FindBlockDataModification', '{5F556342-9E5E-4B96-9002-9B148BA114DD}')
		return ret

	# Result is of type IMGCVariantMgrBlockDataModification
	def FindBlockDataModificationByUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Finds a block data modification record'
		ret = self._oleobj_.InvokeTypes(108, LCID, 1, (9, 0), ((3, 1), (3, 1), (3, 1)),userID
			, objectID, objectType)
		if ret is not None:
			ret = Dispatch(ret, 'FindBlockDataModificationByUID', '{5F556342-9E5E-4B96-9002-9B148BA114DD}')
		return ret

	# Result is of type IMGCVariantMgrPackageModification
	def FindPackageModification(self, variantDef=defaultNamedNotOptArg, packageDef=defaultNamedNotOptArg):
		'Finds a package modification record'
		ret = self._oleobj_.InvokeTypes(102, LCID, 1, (9, 0), ((12, 1), (12, 1)),variantDef
			, packageDef)
		if ret is not None:
			ret = Dispatch(ret, 'FindPackageModification', '{786637FD-9407-11D2-89D9-0020184077E1}')
		return ret

	# Result is of type IMGCVariantMgrPackageModification
	def FindPackageModificationByUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Finds a package modification record'
		ret = self._oleobj_.InvokeTypes(104, LCID, 1, (9, 0), ((3, 1), (3, 1), (3, 1)),userID
			, objectID, objectType)
		if ret is not None:
			ret = Dispatch(ret, 'FindPackageModificationByUID', '{786637FD-9407-11D2-89D9-0020184077E1}')
		return ret

	# Result is of type IMGCVariantMgrBlockDataModifications
	# The method GetBlockDataModifications is actually a property, but must be used as a method to correctly pass the arguments
	def GetBlockDataModifications(self, filter=defaultNamedOptArg):
		'Returns the block data modifications for the variants.'
		ret = self._oleobj_.InvokeTypes(107, LCID, 2, (9, 0), ((12, 17),),filter
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetBlockDataModifications', '{45742780-B379-49F9-8431-16CB70520F9C}')
		return ret

	# Result is of type IMGCVariantMgrPackageModifications
	# The method GetPackageModifications is actually a property, but must be used as a method to correctly pass the arguments
	def GetPackageModifications(self, filter=defaultNamedOptArg):
		'Returns the package modifications for the variants.'
		ret = self._oleobj_.InvokeTypes(103, LCID, 2, (9, 0), ((12, 17),),filter
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetPackageModifications', '{786637FE-9407-11D2-89D9-0020184077E1}')
		return ret

	def GetUID(self, userID=pythoncom.Missing, objectID=pythoncom.Missing, objectType=pythoncom.Missing):
		'Gets the UID of an object. Returns false if the UID is invalid.'
		return self._ApplyTypes_(6, 1, (11, 0), ((16403, 2), (16403, 2), (16403, 2)), 'GetUID', None,userID
			, objectID, objectType)

	def IsLOBlockDataEditable(self, variantDef=defaultNamedNotOptArg, blockDataDef=defaultNamedNotOptArg):
		'Check if block is editable.'
		return self._oleobj_.InvokeTypes(110, LCID, 1, (11, 0), ((12, 1), (12, 1)),variantDef
			, blockDataDef)

	def IsLOPackageEditable(self, variantDef=defaultNamedNotOptArg, packageDef=defaultNamedNotOptArg):
		'Check if package is editable.'
		return self._oleobj_.InvokeTypes(109, LCID, 1, (11, 0), ((12, 1), (12, 1)),variantDef
			, packageDef)

	def IsValid(self):
		'Returns the internal (CPP) index of the X-Object'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), (),)

	# Result is of type IMGCVariantMgrBlockDataModification
	def PutBlockDataModification(self, variantDefinition=defaultNamedNotOptArg, blockDataDefinition=defaultNamedNotOptArg, changeOper=defaultNamedNotOptArg, SubVariantName=''):
		'Creates a new block data modification.'
		return self._ApplyTypes_(105, 1, (9, 32), ((12, 1), (12, 1), (3, 1), (8, 49)), 'PutBlockDataModification', '{5F556342-9E5E-4B96-9002-9B148BA114DD}',variantDefinition
			, blockDataDefinition, changeOper, SubVariantName)

	# Result is of type IMGCVariantMgrPackageModification
	def PutPackageModification(self, variantDefinition=defaultNamedNotOptArg, packageDefinition=defaultNamedNotOptArg, changeOper=defaultNamedNotOptArg, PartNumber=''
			, cellName=''):
		'Creates a new package modification.'
		return self._ApplyTypes_(101, 1, (9, 32), ((12, 1), (12, 1), (3, 1), (8, 49), (8, 49)), 'PutPackageModification', '{786637FD-9407-11D2-89D9-0020184077E1}',variantDefinition
			, packageDefinition, changeOper, PartNumber, cellName)

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
		# Method 'BlockDataModifications' returns object of type 'IMGCVariantMgrBlockDataModifications'
		"BlockDataModifications": (107, 2, (9, 0), ((12, 17),), "BlockDataModifications", '{45742780-B379-49F9-8431-16CB70520F9C}'),
		"InternalIndex": (2, 2, (3, 0), (), "InternalIndex", None),
		# Method 'PackageModifications' returns object of type 'IMGCVariantMgrPackageModifications'
		"PackageModifications": (103, 2, (9, 0), ((12, 17),), "PackageModifications", '{786637FE-9407-11D2-89D9-0020184077E1}'),
		"Parent": (1, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
		"AccessLock": ((5, LCID, 4, 0),()),
		"Parent": ((1, LCID, 8, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMGCVariantMgrPackage(DispatchBaseClass):
	'Variant manager package'
	CLSID = IID('{786637F5-9407-11D2-89D9-0020184077E1}')
	coclass_clsid = IID('{786637F5-9407-20D2-89D9-0020184077E1}')

	# The method CentLibPropValue is actually a property, but must be used as a method to correctly pass the arguments
	def CentLibPropValue(self, propName=defaultNamedNotOptArg):
		'Value of central library property to be shown in the grid.'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(120, LCID, 2, (8, 0), ((8, 1),),propName
			)

	def CompareUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Compares a UID with the UID of the object. Returns true if equal.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((19, 1), (19, 1), (19, 1)),userID
			, objectID, objectType)

	def FindSymbolInstanceNames(self, SymbolPath=defaultNamedNotOptArg, value=pythoncom.Missing):
		'Returns a list of symbol instance names (| separated) based on the supplied path.'
		return self._ApplyTypes_(106, 1, (2, 0), ((8, 1), (16392, 2)), 'FindSymbolInstanceNames', None,SymbolPath
			, value)

	# Result is of type IMGCVariantMgrSymbols
	# The method GetSymbols is actually a property, but must be used as a method to correctly pass the arguments
	def GetSymbols(self, filter=defaultNamedOptArg):
		'Gets the symbols that are assigned to the package'
		ret = self._oleobj_.InvokeTypes(101, LCID, 2, (9, 0), ((12, 17),),filter
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
		"AliasPartNumber": (121, 2, (8, 0), (), "AliasPartNumber", None),
		"Cell": (103, 2, (8, 0), (), "Cell", None),
		"FMVDriven": (108, 2, (11, 0), (), "FMVDriven", None),
		"ForwardPCBFlag": (119, 2, (11, 0), (), "ForwardPCBFlag", None),
		"HKPFlag": (116, 2, (11, 0), (), "HKPFlag", None),
		"IncludedInBOM": (112, 2, (11, 0), (), "IncludedInBOM", None),
		"InternalIndex": (2, 2, (3, 0), (), "InternalIndex", None),
		"IsLogicalOnlyPartModificationAllowed": (122, 2, (11, 0), (), "IsLogicalOnlyPartModificationAllowed", None),
		"IsParentLogicalReusedBlock": (117, 2, (11, 0), (), "IsParentLogicalReusedBlock", None),
		"IsParentReusedBlock": (110, 2, (11, 0), (), "IsParentReusedBlock", None),
		"ModificationCount": (20, 2, (2, 0), (), "ModificationCount", None),
		"ModificationCountEx": (24, 2, (3, 0), (), "ModificationCountEx", None),
		"ModificationCountLock": (21, 2, (11, 0), (), "ModificationCountLock", None),
		"Name": (30, 2, (8, 0), (), "Name", None),
		"PackageState": (107, 2, (3, 0), (), "PackageState", None),
		"Parent": (1, 2, (9, 0), (), "Parent", None),
		"ParentDynamicReuseBlockName": (118, 2, (8, 0), (), "ParentDynamicReuseBlockName", None),
		# Method 'ParentPackage' returns object of type 'IMGCVariantMgrPackage'
		"ParentPackage": (114, 2, (9, 0), (), "ParentPackage", '{786637F5-9407-11D2-89D9-0020184077E1}'),
		"PartNumber": (102, 2, (8, 0), (), "PartNumber", None),
		"RFComponent": (111, 2, (11, 0), (), "RFComponent", None),
		"ReuseAccessMode": (105, 2, (3, 0), (), "ReuseAccessMode", None),
		# Method 'RootIF' returns object of type 'IMGCVariantMgrDocument'
		"RootIF": (22, 2, (9, 0), (), "RootIF", '{78663807-9407-11D2-89D9-0020184077E1}'),
		"SID": (115, 2, (8, 0), (), "SID", None),
		"SymbolPath": (104, 2, (8, 0), (), "SymbolPath", None),
		# Method 'Symbols' returns object of type 'IMGCVariantMgrSymbols'
		"Symbols": (101, 2, (9, 0), ((12, 17),), "Symbols", '{786637F7-9407-11D2-89D9-0020184077E1}'),
		"Type": (113, 2, (3, 0), (), "Type", None),
		"UnplaceFromNewVars": (109, 2, (11, 0), (), "UnplaceFromNewVars", None),
	}
	_prop_map_put_ = {
		"AccessLock": ((5, LCID, 4, 0),()),
		"AliasPartNumber": ((121, LCID, 4, 0),()),
		"Cell": ((103, LCID, 4, 0),()),
		"FMVDriven": ((108, LCID, 4, 0),()),
		"ForwardPCBFlag": ((119, LCID, 4, 0),()),
		"HKPFlag": ((116, LCID, 4, 0),()),
		"IncludedInBOM": ((112, LCID, 4, 0),()),
		"ModificationCount": ((20, LCID, 4, 0),()),
		"ModificationCountEx": ((24, LCID, 4, 0),()),
		"ModificationCountLock": ((21, LCID, 4, 0),()),
		"Name": ((30, LCID, 4, 0),()),
		"Parent": ((1, LCID, 8, 0),()),
		"ParentPackage": ((114, LCID, 8, 0),()),
		"PartNumber": ((102, LCID, 4, 0),()),
		"RFComponent": ((111, LCID, 4, 0),()),
		"SID": ((115, LCID, 4, 0),()),
		"Type": ((113, LCID, 4, 0),()),
		"UnplaceFromNewVars": ((109, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMGCVariantMgrPackageFilter(DispatchBaseClass):
	CLSID = IID('{B01F00BE-D881-46C2-B841-82D35B117ED4}')
	coclass_clsid = IID('{1CA65166-6233-45DE-A7F9-8327E263DBA5}')

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
		return self._oleobj_.InvokeTypes(103, LCID, 1, (24, 0), (),)

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
		"Type": (102, 2, (3, 0), (), "Type", None),
	}
	_prop_map_put_ = {
		"AccessLock": ((5, LCID, 4, 0),()),
		"Parent": ((1, LCID, 8, 0),()),
		"ParentPackage": ((101, LCID, 4, 0),()),
		"Type": ((102, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMGCVariantMgrPackageModification(DispatchBaseClass):
	'Variant manager schematic symbol object'
	CLSID = IID('{786637FD-9407-11D2-89D9-0020184077E1}')
	coclass_clsid = IID('{786637FD-9407-20D2-89D9-0020184077E1}')

	def CompareUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Compares a UID with the UID of the object. Returns true if equal.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((19, 1), (19, 1), (19, 1)),userID
			, objectID, objectType)

	def Delete(self):
		'Deletes the symbol modification.'
		return self._oleobj_.InvokeTypes(106, LCID, 1, (11, 0), (),)

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
		"ChangeOperation": (102, 2, (3, 0), (), "ChangeOperation", None),
		"InternalIndex": (2, 2, (3, 0), (), "InternalIndex", None),
		"ModificationCount": (20, 2, (2, 0), (), "ModificationCount", None),
		"ModificationCountEx": (24, 2, (3, 0), (), "ModificationCountEx", None),
		"ModificationCountLock": (21, 2, (11, 0), (), "ModificationCountLock", None),
		"Name": (30, 2, (8, 0), (), "Name", None),
		"NewAliasPartNumber": (108, 2, (8, 0), (), "NewAliasPartNumber", None),
		"NewCell": (104, 2, (8, 0), (), "NewCell", None),
		"NewPartNumber": (103, 2, (8, 0), (), "NewPartNumber", None),
		# Method 'Package' returns object of type 'IMGCVariantMgrPackage'
		"Package": (101, 2, (9, 0), (), "Package", '{786637F5-9407-11D2-89D9-0020184077E1}'),
		"Parent": (1, 2, (9, 0), (), "Parent", None),
		"ReuseAccessMode": (107, 2, (3, 0), (), "ReuseAccessMode", None),
		# Method 'RootIF' returns object of type 'IMGCVariantMgrDocument'
		"RootIF": (22, 2, (9, 0), (), "RootIF", '{78663807-9407-11D2-89D9-0020184077E1}'),
		# Method 'Variant' returns object of type 'IMGCVariantMgrVariant'
		"Variant": (105, 2, (9, 0), (), "Variant", '{78663802-9407-11D2-89D9-0020184077E1}'),
	}
	_prop_map_put_ = {
		"AccessLock": ((5, LCID, 4, 0),()),
		"ChangeOperation": ((102, LCID, 4, 0),()),
		"ModificationCount": ((20, LCID, 4, 0),()),
		"ModificationCountEx": ((24, LCID, 4, 0),()),
		"ModificationCountLock": ((21, LCID, 4, 0),()),
		"Name": ((30, LCID, 4, 0),()),
		"NewAliasPartNumber": ((108, LCID, 4, 0),()),
		"NewCell": ((104, LCID, 4, 0),()),
		"NewPartNumber": ((103, LCID, 4, 0),()),
		"Parent": ((1, LCID, 8, 0),()),
		"Variant": ((105, LCID, 8, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMGCVariantMgrPackageModificationFilter(DispatchBaseClass):
	CLSID = IID('{7E1CD29C-D3B5-4690-91D5-415965F42BA6}')
	coclass_clsid = IID('{26D8C861-04AF-4273-9875-A8EF996FD14B}')

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
		"NewPartNumber": (103, 2, (8, 0), (), "NewPartNumber", None),
		"Parent": (1, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
		"AccessLock": ((5, LCID, 4, 0),()),
		"ChangeOperation": ((102, LCID, 4, 0),()),
		"NewPartNumber": ((103, LCID, 4, 0),()),
		"Package": ((101, LCID, 4, 0),()),
		"Parent": ((1, LCID, 8, 0),()),
		"Variant": ((104, LCID, 4, 0),()),
		"VariantGroup": ((105, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMGCVariantMgrPackageModifications(DispatchBaseClass):
	'Variant manager package modifications collection'
	CLSID = IID('{786637FE-9407-11D2-89D9-0020184077E1}')
	coclass_clsid = IID('{786637FE-9407-20D2-89D9-0020184077E1}')

	def Add(self, pPackMod=defaultNamedNotOptArg):
		'Adds a package modification object to the collection.'
		return self._oleobj_.InvokeTypes(102, LCID, 1, (24, 0), ((9, 1),),pPackMod
			)

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

	# Result is of type IMGCVariantMgrPackageModification
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, index=defaultNamedNotOptArg):
		'Returns a package modification object at a given index.'
		ret = self._oleobj_.InvokeTypes(101, LCID, 2, (9, 0), ((12, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{786637FD-9407-11D2-89D9-0020184077E1}')
		return ret

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
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{786637FD-9407-11D2-89D9-0020184077E1}')
	#This class has Item property/method which allows indexed access with the object[key] syntax.
	#Some objects will accept a string or other type of key in addition to integers.
	#Note that many Office objects do not use zero-based indexing.
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(101, LCID, 2, 1, key)), "Item", '{786637FD-9407-11D2-89D9-0020184077E1}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(30, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IMGCVariantMgrPackages(DispatchBaseClass):
	'Variant manager packages collection'
	CLSID = IID('{786637F6-9407-11D2-89D9-0020184077E1}')
	coclass_clsid = IID('{786637F6-9407-20D2-89D9-0020184077E1}')

	def Add(self, pPackage=defaultNamedNotOptArg):
		'Adds a package to the collection.'
		return self._oleobj_.InvokeTypes(102, LCID, 1, (24, 0), ((9, 1),),pPackage
			)

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

	# Result is of type IMGCVariantMgrPackage
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, index=defaultNamedNotOptArg):
		'Returns a package object at a given index.'
		ret = self._oleobj_.InvokeTypes(101, LCID, 2, (9, 0), ((12, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{786637F5-9407-11D2-89D9-0020184077E1}')
		return ret

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
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{786637F5-9407-11D2-89D9-0020184077E1}')
	#This class has Item property/method which allows indexed access with the object[key] syntax.
	#Some objects will accept a string or other type of key in addition to integers.
	#Note that many Office objects do not use zero-based indexing.
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(101, LCID, 2, 1, key)), "Item", '{786637F5-9407-11D2-89D9-0020184077E1}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(30, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IMGCVariantMgrParameter(DispatchBaseClass):
	'Defines a parameter used by the Vmgr XE model'
	CLSID = IID('{82CD5AAF-9407-11D2-89D9-0020184077E1}')
	coclass_clsid = IID('{82CD5AB3-9407-11D2-89D9-0020184077E1}')

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
		"value": (102, 2, (8, 0), (), "value", None),
	}
	_prop_map_put_ = {
		"AccessLock": ((5, LCID, 4, 0),()),
		"ModificationCount": ((20, LCID, 4, 0),()),
		"ModificationCountEx": ((24, LCID, 4, 0),()),
		"ModificationCountLock": ((21, LCID, 4, 0),()),
		"Name": ((30, LCID, 4, 0),()),
		"Parent": ((1, LCID, 8, 0),()),
		"value": ((102, LCID, 4, 0),()),
	}
	# Default property for this class is 'value'
	def __call__(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "value", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMGCVariantMgrParameters(DispatchBaseClass):
	'Variant manager parameters collection'
	CLSID = IID('{82CD5AB0-9407-11D2-89D9-0020184077E1}')
	coclass_clsid = IID('{82CD5AB4-9407-11D2-89D9-0020184077E1}')

	def Add(self, Name=defaultNamedNotOptArg, value=defaultNamedNotOptArg):
		'Adds a parameter to the collection.'
		return self._oleobj_.InvokeTypes(102, LCID, 1, (24, 0), ((8, 1), (8, 1)),Name
			, value)

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

	# Result is of type IMGCVariantMgrParameter
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, index=defaultNamedNotOptArg):
		'Returns a parameter object'
		ret = self._oleobj_.InvokeTypes(101, LCID, 2, (9, 0), ((12, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{82CD5AAF-9407-11D2-89D9-0020184077E1}')
		return ret

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
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{82CD5AAF-9407-11D2-89D9-0020184077E1}')
	#This class has Item property/method which allows indexed access with the object[key] syntax.
	#Some objects will accept a string or other type of key in addition to integers.
	#Note that many Office objects do not use zero-based indexing.
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(101, LCID, 2, 1, key)), "Item", '{82CD5AAF-9407-11D2-89D9-0020184077E1}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(30, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IMGCVariantMgrParent(DispatchBaseClass):
	CLSID = IID('{C68512CD-1296-48BC-A69D-B7DFF5816DA5}')
	coclass_clsid = None

	def GetHierObjectContext(self, functionID=defaultNamedNotOptArg, result=defaultNamedNotOptArg):
		'Get the hierarchical object context of an object.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (24, 0), ((8, 0), (16392, 0)),functionID
			, result)

	def GetParent(self, pParentObj=pythoncom.Missing):
		'Get the parent.'
		return self._ApplyTypes_(2, 1, (24, 0), ((16393, 2),), 'GetParent', None,pParentObj
			)

	def GetRootIF(self, ppDocObj=pythoncom.Missing):
		'Get the document object.'
		return self._ApplyTypes_(3, 1, (24, 0), ((16393, 2),), 'GetRootIF', None,ppDocObj
			)

	def SetParent(self, pParentObj=defaultNamedNotOptArg):
		'Set the parent.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (24, 0), ((9, 1),),pParentObj
			)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMGCVariantMgrProperties(DispatchBaseClass):
	'Variant manager properties collection'
	CLSID = IID('{FA1219FB-D82D-47B6-815F-F786F347E6E6}')
	coclass_clsid = IID('{1101A6F0-EA66-43DC-849E-906E36A0A734}')

	def Add(self, pPropRec=defaultNamedNotOptArg):
		'Adds a property record to the collection.'
		return self._oleobj_.InvokeTypes(102, LCID, 1, (24, 0), ((9, 1),),pPropRec
			)

	def CompareUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Compares a UID with the UID of the object. Returns true if equal.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((19, 1), (19, 1), (19, 1)),userID
			, objectID, objectType)

	# Result is of type IMGCVariantMgrProperty
	def Find(self, Name=defaultNamedNotOptArg):
		'Returns a property object using name.'
		ret = self._oleobj_.InvokeTypes(103, LCID, 1, (9, 0), ((8, 1),),Name
			)
		if ret is not None:
			ret = Dispatch(ret, 'Find', '{6ABBB0DE-2FAC-45DB-90CA-E90A630B0FBB}')
		return ret

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

	# Result is of type IMGCVariantMgrProperty
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, index=defaultNamedNotOptArg):
		'Returns a property object at a given index.'
		ret = self._oleobj_.InvokeTypes(101, LCID, 2, (9, 0), ((12, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{6ABBB0DE-2FAC-45DB-90CA-E90A630B0FBB}')
		return ret

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
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{6ABBB0DE-2FAC-45DB-90CA-E90A630B0FBB}')
	#This class has Item property/method which allows indexed access with the object[key] syntax.
	#Some objects will accept a string or other type of key in addition to integers.
	#Note that many Office objects do not use zero-based indexing.
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(101, LCID, 2, 1, key)), "Item", '{6ABBB0DE-2FAC-45DB-90CA-E90A630B0FBB}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(30, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IMGCVariantMgrProperty(DispatchBaseClass):
	'Variant manager property object'
	CLSID = IID('{6ABBB0DE-2FAC-45DB-90CA-E90A630B0FBB}')
	coclass_clsid = IID('{4BCB2183-E92C-4465-8652-62AE02E8672A}')

	def CompareUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Compares a UID with the UID of the object. Returns true if equal.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((19, 1), (19, 1), (19, 1)),userID
			, objectID, objectType)

	def Delete(self):
		'Deletes the property.'
		return self._oleobj_.InvokeTypes(103, LCID, 1, (11, 0), (),)

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
		"ReadOnly": (102, 2, (11, 0), (), "ReadOnly", None),
		# Method 'RootIF' returns object of type 'IMGCVariantMgrDocument'
		"RootIF": (22, 2, (9, 0), (), "RootIF", '{78663807-9407-11D2-89D9-0020184077E1}'),
		"value": (101, 2, (8, 0), (), "value", None),
	}
	_prop_map_put_ = {
		"AccessLock": ((5, LCID, 4, 0),()),
		"ModificationCount": ((20, LCID, 4, 0),()),
		"ModificationCountEx": ((24, LCID, 4, 0),()),
		"ModificationCountLock": ((21, LCID, 4, 0),()),
		"Name": ((30, LCID, 4, 0),()),
		"Parent": ((1, LCID, 8, 0),()),
		"value": ((101, LCID, 4, 0),()),
	}
	# Default property for this class is 'value'
	def __call__(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "value", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMGCVariantMgrReporter(DispatchBaseClass):
	'Defines the methods and properties of the reporter object'
	CLSID = IID('{017BAF92-95BB-4AD2-BCF6-43DC7A60BAA8}')
	coclass_clsid = IID('{8B707D43-7C93-4D09-BE09-EE1B0498E345}')

	def CompareUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Compares a UID with the UID of the object. Returns true if equal.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((19, 1), (19, 1), (19, 1)),userID
			, objectID, objectType)

	def GenDelimitedTextReport(self):
		'Generates a delimited text report.'
		return self._oleobj_.InvokeTypes(103, LCID, 1, (2, 0), (),)

	def GenExcelReport(self):
		'Generates an Excel report.'
		return self._oleobj_.InvokeTypes(105, LCID, 1, (2, 0), (),)

	def GenFormattedLogReport(self):
		'Generates a formatted log report.'
		return self._oleobj_.InvokeTypes(104, LCID, 1, (2, 0), (),)

	def GenHTMLReport(self):
		'Generates a HTML report.'
		return self._oleobj_.InvokeTypes(102, LCID, 1, (2, 0), (),)

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

	def WriteDelimitedTextReport(self):
		'Writes a delimited text report.'
		return self._oleobj_.InvokeTypes(109, LCID, 1, (2, 0), (),)

	def WriteExcelReport(self):
		'Writes an Excel report.'
		return self._oleobj_.InvokeTypes(107, LCID, 1, (2, 0), (),)

	def WriteFormattedLogReport(self):
		'Writes a formatted log report.'
		return self._oleobj_.InvokeTypes(110, LCID, 1, (2, 0), (),)

	def WriteHTMLReport(self):
		'Writes a HTML report.'
		return self._oleobj_.InvokeTypes(108, LCID, 1, (2, 0), (),)

	_prop_map_get_ = {
		"AccessLock": (5, 2, (3, 0), (), "AccessLock", None),
		# Method 'DataMatrix' returns object of type 'IMGCVariantMgrReporterDataMatrix'
		"DataMatrix": (106, 2, (9, 0), (), "DataMatrix", '{9E5DF0FC-CE34-409A-B257-AD8E39BBD95E}'),
		"InternalIndex": (2, 2, (3, 0), (), "InternalIndex", None),
		"Parent": (1, 2, (9, 0), (), "Parent", None),
		# Method 'Settings' returns object of type 'IMGCVariantMgrReporterSettings'
		"Settings": (101, 2, (9, 0), (), "Settings", '{353E3059-2914-4F62-AD38-D61BD61F620F}'),
	}
	_prop_map_put_ = {
		"AccessLock": ((5, LCID, 4, 0),()),
		"Parent": ((1, LCID, 8, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMGCVariantMgrReporterDataMatrix(DispatchBaseClass):
	'Exposes the data of the reporter data matrix'
	CLSID = IID('{9E5DF0FC-CE34-409A-B257-AD8E39BBD95E}')
	coclass_clsid = IID('{1E60DA28-0E2A-4C52-9432-575F66713702}')

	def CompareUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Compares a UID with the UID of the object. Returns true if equal.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((19, 1), (19, 1), (19, 1)),userID
			, objectID, objectType)

	def GetCellValue(self, columnIndex=defaultNamedNotOptArg, rowIndex=defaultNamedNotOptArg):
		'Returns the value of a cell'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(105, LCID, 1, (8, 0), ((3, 1), (3, 1)),columnIndex
			, rowIndex)

	def GetHeaderValue(self, columnIndex=defaultNamedNotOptArg):
		'Returns the value of a column header'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(103, LCID, 1, (8, 0), ((3, 1),),columnIndex
			)

	def GetMaxColumnWidth(self, columnIndex=defaultNamedNotOptArg):
		'Returns the maximum column width for a column (num chars)'
		return self._oleobj_.InvokeTypes(104, LCID, 1, (3, 0), ((3, 1),),columnIndex
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

	def SetCellValue(self, columnIndex=defaultNamedNotOptArg, rowIndex=defaultNamedNotOptArg, value=defaultNamedNotOptArg):
		'Sets the value of a cell'
		return self._oleobj_.InvokeTypes(107, LCID, 1, (24, 0), ((3, 1), (3, 1), (8, 1)),columnIndex
			, rowIndex, value)

	def SetHeaderData(self, columnIndex=defaultNamedNotOptArg, value=defaultNamedNotOptArg):
		'Sets the value of a header'
		return self._oleobj_.InvokeTypes(108, LCID, 1, (24, 0), ((3, 1), (8, 1)),columnIndex
			, value)

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
		"NumColumns": (101, 2, (3, 0), (), "NumColumns", None),
		"NumRows": (102, 2, (3, 0), (), "NumRows", None),
		"Parent": (1, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
		"AccessLock": ((5, LCID, 4, 0),()),
		"NumColumns": ((101, LCID, 4, 0),()),
		"NumRows": ((102, LCID, 4, 0),()),
		"Parent": ((1, LCID, 8, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMGCVariantMgrReporterSettings(DispatchBaseClass):
	'Defines the settings of the reporter'
	CLSID = IID('{353E3059-2914-4F62-AD38-D61BD61F620F}')
	coclass_clsid = IID('{22912830-6A46-4B8E-998C-1812ABCEEC4E}')

	def AddFMVFunctionGroupToList(self, groupSpec=defaultNamedNotOptArg):
		'Adds an FMV function group to the list of functions.'
		return self._oleobj_.InvokeTypes(113, LCID, 1, (24, 0), ((12, 1),),groupSpec
			)

	def AddFMVFunctionToList(self, functionSpec=defaultNamedNotOptArg):
		'Adds an FMV function to the list of functions.'
		return self._oleobj_.InvokeTypes(112, LCID, 1, (24, 0), ((12, 1),),functionSpec
			)

	def AddVariantGroupToList(self, groupSpec=defaultNamedNotOptArg):
		'Add a variant group to the list.'
		return self._oleobj_.InvokeTypes(108, LCID, 1, (24, 0), ((12, 1),),groupSpec
			)

	def AddVariantToList(self, variantSpec=defaultNamedNotOptArg):
		'Add a variant to the list of variants.'
		return self._oleobj_.InvokeTypes(107, LCID, 1, (24, 0), ((12, 1),),variantSpec
			)

	def CompareUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Compares a UID with the UID of the object. Returns true if equal.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((19, 1), (19, 1), (19, 1)),userID
			, objectID, objectType)

	def GetUID(self, userID=pythoncom.Missing, objectID=pythoncom.Missing, objectType=pythoncom.Missing):
		'Gets the UID of an object. Returns false if the UID is invalid.'
		return self._ApplyTypes_(6, 1, (11, 0), ((16403, 2), (16403, 2), (16403, 2)), 'GetUID', None,userID
			, objectID, objectType)

	def Initialize(self):
		'Initializes the object.'
		return self._oleobj_.InvokeTypes(109, LCID, 1, (24, 0), (),)

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
		"Date": (105, 2, (8, 0), (), "Date", None),
		"DifferencesOnly": (106, 2, (11, 0), (), "DifferencesOnly", None),
		"FieldDelimiter": (111, 2, (8, 0), (), "FieldDelimiter", None),
		"IncludeGroupName": (117, 2, (11, 0), (), "IncludeGroupName", None),
		"IncludeMasterPartNumber": (110, 2, (11, 0), (), "IncludeMasterPartNumber", None),
		"IncludeRefdesForFMVs": (114, 2, (11, 0), (), "IncludeRefdesForFMVs", None),
		"InternalIndex": (2, 2, (3, 0), (), "InternalIndex", None),
		"OutputFile": (101, 2, (8, 0), (), "OutputFile", None),
		"Parent": (1, 2, (9, 0), (), "Parent", None),
		"ReportDataType": (115, 2, (3, 0), (), "ReportDataType", None),
		"Title": (104, 2, (8, 0), (), "Title", None),
		"UnplacedKW": (102, 2, (8, 0), (), "UnplacedKW", None),
		"groupName": (116, 2, (8, 0), (), "groupName", None),
	}
	_prop_map_put_ = {
		"AccessLock": ((5, LCID, 4, 0),()),
		"Date": ((105, LCID, 4, 0),()),
		"DifferencesOnly": ((106, LCID, 4, 0),()),
		"FieldDelimiter": ((111, LCID, 4, 0),()),
		"IncludeGroupName": ((117, LCID, 4, 0),()),
		"IncludeMasterPartNumber": ((110, LCID, 4, 0),()),
		"IncludeRefdesForFMVs": ((114, LCID, 4, 0),()),
		"OutputFile": ((101, LCID, 4, 0),()),
		"Parent": ((1, LCID, 8, 0),()),
		"ReportDataType": ((115, LCID, 4, 0),()),
		"Title": ((104, LCID, 4, 0),()),
		"UnplacedKW": ((102, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMGCVariantMgrReuseSettings(DispatchBaseClass):
	'Defines the settings to be used when using a design as a reused block'
	CLSID = IID('{CA185E0D-76D0-43D5-A215-F301941E074F}')
	coclass_clsid = IID('{2CA0D3A4-696A-4927-85D6-D0421E343252}')

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
		"AllowAccessOverwrite": (102, 2, (11, 0), (), "AllowAccessOverwrite", None),
		"AllowMergeModeOverwrite": (103, 2, (11, 0), (), "AllowMergeModeOverwrite", None),
		"DefaultAccessMode": (100, 2, (3, 0), (), "DefaultAccessMode", None),
		"DefaultMergeMode": (101, 2, (3, 0), (), "DefaultMergeMode", None),
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
		"AllowAccessOverwrite": ((102, LCID, 4, 0),()),
		"AllowMergeModeOverwrite": ((103, LCID, 4, 0),()),
		"DefaultAccessMode": ((100, LCID, 4, 0),()),
		"DefaultMergeMode": ((101, LCID, 4, 0),()),
		"ModificationCount": ((20, LCID, 4, 0),()),
		"ModificationCountEx": ((24, LCID, 4, 0),()),
		"ModificationCountLock": ((21, LCID, 4, 0),()),
		"Parent": ((1, LCID, 8, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMGCVariantMgrReusedBlock(DispatchBaseClass):
	'Describes a reused lock'
	CLSID = IID('{82CD5AA4-9407-11D2-89D9-0020184077E1}')
	coclass_clsid = IID('{82CD5AA8-9407-11D2-89D9-0020184077E1}')

	def CompareUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Compares a UID with the UID of the object. Returns true if equal.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((19, 1), (19, 1), (19, 1)),userID
			, objectID, objectType)

	# Result is of type IMGCVariantMgrVariantMapping
	def FindVariantMapping(self, mappingDefinition=defaultNamedNotOptArg):
		'Finds a variant mapping in the list of mappings.'
		ret = self._oleobj_.InvokeTypes(126, LCID, 1, (9, 0), ((12, 1),),mappingDefinition
			)
		if ret is not None:
			ret = Dispatch(ret, 'FindVariantMapping', '{746F9DCE-E85C-4BA5-BE14-FEF24731222A}')
		return ret

	# Result is of type IMGCVariantMgrVariants
	# The method GetReusedVariants is actually a property, but must be used as a method to correctly pass the arguments
	def GetReusedVariants(self, filter=defaultNamedOptArg):
		'Returns a collection of variants of the reused block.'
		ret = self._oleobj_.InvokeTypes(127, LCID, 2, (9, 0), ((12, 17),),filter
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetReusedVariants', '{78663803-9407-11D2-89D9-0020184077E1}')
		return ret

	def GetUID(self, userID=pythoncom.Missing, objectID=pythoncom.Missing, objectType=pythoncom.Missing):
		'Gets the UID of an object. Returns false if the UID is invalid.'
		return self._ApplyTypes_(6, 1, (11, 0), ((16403, 2), (16403, 2), (16403, 2)), 'GetUID', None,userID
			, objectID, objectType)

	# Result is of type IMGCVariantMgrVariantMappings
	# The method GetVariantMappings is actually a property, but must be used as a method to correctly pass the arguments
	def GetVariantMappings(self, filter=defaultNamedOptArg):
		'Get the collection of variant mappings for the reused block.'
		ret = self._oleobj_.InvokeTypes(124, LCID, 2, (9, 0), ((12, 17),),filter
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetVariantMappings', '{5F5FA27B-9A28-4A84-BE9A-7460F1D6D54B}')
		return ret

	def IncModificationCount(self, value=1):
		'Increments the modification count'
		return self._oleobj_.InvokeTypes(23, LCID, 1, (2, 0), ((2, 49),),value
			)

	def IsValid(self):
		'Returns the internal (CPP) index of the X-Object'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), (),)

	def MergeFromLibrary(self, logFilesDir=defaultNamedNotOptArg):
		'Merge the reused block data contained in the library'
		return self._oleobj_.InvokeTypes(123, LCID, 1, (2, 0), ((8, 1),),logFilesDir
			)

	# Result is of type IMGCVariantMgrVariantMapping
	def PutVariantMapping(self, originalVariantName=defaultNamedNotOptArg, newVariantName=defaultNamedNotOptArg, MappingFlags=defaultNamedNotOptArg):
		'Adds a new variant mapping to the variant mappings collection.'
		ret = self._oleobj_.InvokeTypes(125, LCID, 1, (9, 0), ((8, 1), (8, 1), (3, 1)),originalVariantName
			, newVariantName, MappingFlags)
		if ret is not None:
			ret = Dispatch(ret, 'PutVariantMapping', '{746F9DCE-E85C-4BA5-BE14-FEF24731222A}')
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
		# Method 'BlockData' returns object of type 'IMGCVariantMgrBlockData'
		"BlockData": (101, 2, (9, 0), (), "BlockData", '{7FE7FAB6-7B3B-46CB-970A-0010103AD7E3}'),
		"Flattened": (129, 2, (11, 0), (), "Flattened", None),
		"InternalIndex": (2, 2, (3, 0), (), "InternalIndex", None),
		"LibraryName": (120, 2, (8, 0), (), "LibraryName", None),
		"LogicalOnly": (131, 2, (11, 0), (), "LogicalOnly", None),
		"LogicalOnlyPartModificationAllowed": (132, 2, (11, 0), (), "LogicalOnlyPartModificationAllowed", None),
		"MergeMode": (122, 2, (3, 0), (), "MergeMode", None),
		"MergeStatus": (128, 2, (3, 0), (), "MergeStatus", None),
		"ModificationCount": (20, 2, (2, 0), (), "ModificationCount", None),
		"ModificationCountEx": (24, 2, (3, 0), (), "ModificationCountEx", None),
		"ModificationCountLock": (21, 2, (11, 0), (), "ModificationCountLock", None),
		"Name": (30, 2, (8, 0), (), "Name", None),
		"Parent": (1, 2, (9, 0), (), "Parent", None),
		# Method 'ReuseBlockDocument' returns object of type 'IMGCVariantMgrDocument'
		"ReuseBlockDocument": (130, 2, (9, 0), (), "ReuseBlockDocument", '{78663807-9407-11D2-89D9-0020184077E1}'),
		# Method 'ReusedVariants' returns object of type 'IMGCVariantMgrVariants'
		"ReusedVariants": (127, 2, (9, 0), ((12, 17),), "ReusedVariants", '{78663803-9407-11D2-89D9-0020184077E1}'),
		# Method 'RootIF' returns object of type 'IMGCVariantMgrDocument'
		"RootIF": (22, 2, (9, 0), (), "RootIF", '{78663807-9407-11D2-89D9-0020184077E1}'),
		# Method 'VariantMappings' returns object of type 'IMGCVariantMgrVariantMappings'
		"VariantMappings": (124, 2, (9, 0), ((12, 17),), "VariantMappings", '{5F5FA27B-9A28-4A84-BE9A-7460F1D6D54B}'),
		"accessMode": (121, 2, (3, 0), (), "accessMode", None),
	}
	_prop_map_put_ = {
		"AccessLock": ((5, LCID, 4, 0),()),
		"Flattened": ((129, LCID, 4, 0),()),
		"LibraryName": ((120, LCID, 4, 0),()),
		"LogicalOnly": ((131, LCID, 4, 0),()),
		"LogicalOnlyPartModificationAllowed": ((132, LCID, 4, 0),()),
		"MergeMode": ((122, LCID, 4, 0),()),
		"ModificationCount": ((20, LCID, 4, 0),()),
		"ModificationCountEx": ((24, LCID, 4, 0),()),
		"ModificationCountLock": ((21, LCID, 4, 0),()),
		"Name": ((30, LCID, 4, 0),()),
		"Parent": ((1, LCID, 8, 0),()),
		"accessMode": ((121, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMGCVariantMgrReusedBlocks(DispatchBaseClass):
	'Variant manager reusedblocks'
	CLSID = IID('{82CD5AA5-9407-11D2-89D9-0020184077E1}')
	coclass_clsid = IID('{82CD5AA9-9407-11D2-89D9-0020184077E1}')

	def Add(self, pReusedBlock=defaultNamedNotOptArg):
		'Adds a reused block to the collection.'
		return self._oleobj_.InvokeTypes(102, LCID, 1, (24, 0), ((9, 1),),pReusedBlock
			)

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

	# Result is of type IMGCVariantMgrReusedBlock
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, index=defaultNamedNotOptArg):
		'Returns a reused block definition'
		ret = self._oleobj_.InvokeTypes(101, LCID, 2, (9, 0), ((12, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{82CD5AA4-9407-11D2-89D9-0020184077E1}')
		return ret

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
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{82CD5AA4-9407-11D2-89D9-0020184077E1}')
	#This class has Item property/method which allows indexed access with the object[key] syntax.
	#Some objects will accept a string or other type of key in addition to integers.
	#Note that many Office objects do not use zero-based indexing.
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(101, LCID, 2, 1, key)), "Item", '{82CD5AA4-9407-11D2-89D9-0020184077E1}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(30, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IMGCVariantMgrSInfoRecsUtility(DispatchBaseClass):
	'Variant manager symbol inforec utility.'
	CLSID = IID('{7D8CEF26-776A-40B2-A99C-C6B2358E0C60}')
	coclass_clsid = IID('{B15661E9-0393-42DE-A5C4-4EA1C899AF71}')

	def CheckConflict(self, symbolDefinition=defaultNamedNotOptArg, funcDefinition=defaultNamedNotOptArg, changeOper=defaultNamedNotOptArg, rplPartNumber=defaultNamedNotOptArg
			, rplCell=defaultNamedNotOptArg, conflictingFunc=pythoncom.Missing, errStr=pythoncom.Missing):
		'Checks if an entry on the function assignment tab creates a conflict.'
		return self._ApplyTypes_(107, 1, (3, 0), ((12, 1), (12, 1), (3, 1), (8, 1), (8, 1), (16392, 2), (16392, 2)), 'CheckConflict', None,symbolDefinition
			, funcDefinition, changeOper, rplPartNumber, rplCell, conflictingFunc
			, errStr)

	def CheckVariantMatrixConflict(self, funcDef=defaultNamedNotOptArg, variantDef=defaultNamedNotOptArg, errStr=pythoncom.Missing):
		'Checks if two functions are conflicting in the variant/function matrix.'
		return self._ApplyTypes_(108, 1, (3, 0), ((12, 1), (12, 1), (16392, 2)), 'CheckVariantMatrixConflict', None,funcDef
			, variantDef, errStr)

	def CompareUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Compares a UID with the UID of the object. Returns true if equal.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((19, 1), (19, 1), (19, 1)),userID
			, objectID, objectType)

	# Result is of type IMGCVariantMgrFMVProperty
	def FindFMVPropertyByUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Finds a fmv property record'
		ret = self._oleobj_.InvokeTypes(110, LCID, 1, (9, 0), ((3, 1), (3, 1), (3, 1)),userID
			, objectID, objectType)
		if ret is not None:
			ret = Dispatch(ret, 'FindFMVPropertyByUID', '{DD445D35-DC4B-413A-8781-F561D40D4CC5}')
		return ret

	# Result is of type IMGCVariantMgrSymbolInfoRec
	def FindSymbolInfoRec(self, symbolSpec=defaultNamedNotOptArg):
		'Find a symbol information record'
		ret = self._oleobj_.InvokeTypes(103, LCID, 1, (9, 0), ((12, 1),),symbolSpec
			)
		if ret is not None:
			ret = Dispatch(ret, 'FindSymbolInfoRec', '{A34D9F27-362F-45AA-9F73-CBC28DF7645E}')
		return ret

	def FinishCheckingConflicts(self, bConfirm=defaultNamedNotOptArg):
		'Finds a fmv property record'
		return self._oleobj_.InvokeTypes(111, LCID, 1, (2, 0), ((11, 1),),bConfirm
			)

	# Result is of type IMGCVariantMgrSymbolInfoRecs
	# The method GetSymbolInfoRecs is actually a property, but must be used as a method to correctly pass the arguments
	def GetSymbolInfoRecs(self, filter=defaultNamedOptArg):
		'Returns the symbol modifications for the variants.'
		ret = self._oleobj_.InvokeTypes(101, LCID, 2, (9, 0), ((12, 17),),filter
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetSymbolInfoRecs', '{A6C3A4DE-6048-492D-AA03-EC268CCC73D4}')
		return ret

	def GetUID(self, userID=pythoncom.Missing, objectID=pythoncom.Missing, objectType=pythoncom.Missing):
		'Gets the UID of an object. Returns false if the UID is invalid.'
		return self._ApplyTypes_(6, 1, (11, 0), ((16403, 2), (16403, 2), (16403, 2)), 'GetUID', None,userID
			, objectID, objectType)

	def IsValid(self):
		'Returns the internal (CPP) index of the X-Object'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), (),)

	# Result is of type IMGCVariantMgrSymbolInfoRec
	def PutSymbolInfoRec(self, symbolDefinition=defaultNamedNotOptArg):
		'Creates a new symbol modification.'
		ret = self._oleobj_.InvokeTypes(102, LCID, 1, (9, 0), ((12, 1),),symbolDefinition
			)
		if ret is not None:
			ret = Dispatch(ret, 'PutSymbolInfoRec', '{A34D9F27-362F-45AA-9F73-CBC28DF7645E}')
		return ret

	def RecalculatePackmods(self):
		'Recalculate the package modifications.'
		return self._oleobj_.InvokeTypes(109, LCID, 1, (2, 0), (),)

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
		"RequiresMatrixCheck": (106, 2, (11, 0), (), "RequiresMatrixCheck", None),
		"RequiresPackModRecalc": (104, 2, (11, 0), (), "RequiresPackModRecalc", None),
		"RequiresRepackage": (105, 2, (11, 0), (), "RequiresRepackage", None),
		# Method 'SymbolInfoRecs' returns object of type 'IMGCVariantMgrSymbolInfoRecs'
		"SymbolInfoRecs": (101, 2, (9, 0), ((12, 17),), "SymbolInfoRecs", '{A6C3A4DE-6048-492D-AA03-EC268CCC73D4}'),
	}
	_prop_map_put_ = {
		"AccessLock": ((5, LCID, 4, 0),()),
		"Parent": ((1, LCID, 8, 0),()),
		"RequiresMatrixCheck": ((106, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMGCVariantMgrSettings(DispatchBaseClass):
	'Defines the settings of the document object.'
	CLSID = IID('{7866380B-9407-11D2-89D9-0020184077E1}')
	coclass_clsid = IID('{7866380B-9407-20D2-89D9-0020184077E1}')

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
		# Method 'ReuseSettings' returns object of type 'IMGCVariantMgrReuseSettings'
		"ReuseSettings": (103, 2, (9, 0), (), "ReuseSettings", '{CA185E0D-76D0-43D5-A215-F301941E074F}'),
		# Method 'RootIF' returns object of type 'IMGCVariantMgrDocument'
		"RootIF": (22, 2, (9, 0), (), "RootIF", '{78663807-9407-11D2-89D9-0020184077E1}'),
		# Method 'Statistics' returns object of type 'IMGCVariantMgrStatistics'
		"Statistics": (102, 2, (9, 0), (), "Statistics", '{8F683CE7-08DB-45B8-B4EA-E27982CF0995}'),
	}
	_prop_map_put_ = {
		"AccessLock": ((5, LCID, 4, 0),()),
		"ModificationCount": ((20, LCID, 4, 0),()),
		"ModificationCountEx": ((24, LCID, 4, 0),()),
		"ModificationCountLock": ((21, LCID, 4, 0),()),
		"Parent": ((1, LCID, 8, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMGCVariantMgrStatistics(DispatchBaseClass):
	'Variant manager document statistics object'
	CLSID = IID('{8F683CE7-08DB-45B8-B4EA-E27982CF0995}')
	coclass_clsid = IID('{332154D8-A5F8-41A2-BE78-2841D50143F6}')

	# The method CountInfo is actually a property, but must be used as a method to correctly pass the arguments
	def CountInfo(self, statType=defaultNamedNotOptArg):
		'Get count info of different doc data.'
		return self._oleobj_.InvokeTypes(101, LCID, 2, (3, 0), ((3, 1),),statType
			)

	def IsFlatDesign(self):
		'Checks if this is a flat design'
		return self._oleobj_.InvokeTypes(102, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMGCVariantMgrSymbol(DispatchBaseClass):
	'Variant manager schematic symbol object'
	CLSID = IID('{786637F4-9407-11D2-89D9-0020184077E1}')
	coclass_clsid = IID('{786637F4-9407-20D2-89D9-0020184077E1}')

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

	def IsArrayedSymbol(self):
		'Checks if symbol is arrayed component or not.'
		return self._oleobj_.InvokeTypes(114, LCID, 1, (11, 0), (),)

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
		"AliasPartNumber": (117, 2, (8, 0), (), "AliasPartNumber", None),
		"ArrayCompName": (115, 2, (8, 0), (), "ArrayCompName", None),
		# Method 'Block' returns object of type 'IMGCVariantMgrBlock'
		"Block": (112, 2, (9, 0), (), "Block", '{E2CD1C5F-0EE9-4349-B08A-FA34A84CB2F1}'),
		"Cell": (106, 2, (8, 0), (), "Cell", None),
		"InternalIndex": (2, 2, (3, 0), (), "InternalIndex", None),
		"ModificationCount": (20, 2, (2, 0), (), "ModificationCount", None),
		"ModificationCountEx": (24, 2, (3, 0), (), "ModificationCountEx", None),
		"ModificationCountLock": (21, 2, (11, 0), (), "ModificationCountLock", None),
		"Name": (30, 2, (8, 0), (), "Name", None),
		"NameAndPath": (104, 2, (8, 0), (), "NameAndPath", None),
		# Method 'Package' returns object of type 'IMGCVariantMgrPackage'
		"Package": (102, 2, (9, 0), (), "Package", '{786637F5-9407-11D2-89D9-0020184077E1}'),
		"Page": (108, 2, (8, 0), (), "Page", None),
		"PageIndex": (109, 2, (2, 0), (), "PageIndex", None),
		"Parent": (1, 2, (9, 0), (), "Parent", None),
		# Method 'ParentBlock' returns object of type 'IMGCVariantMgrBlock'
		"ParentBlock": (110, 2, (9, 0), (), "ParentBlock", '{E2CD1C5F-0EE9-4349-B08A-FA34A84CB2F1}'),
		"ParentDynamicReuseBlockName": (116, 2, (8, 0), (), "ParentDynamicReuseBlockName", None),
		# Method 'ParentReusedBlock' returns object of type 'IMGCVariantMgrReusedBlock'
		"ParentReusedBlock": (111, 2, (9, 0), (), "ParentReusedBlock", '{82CD5AA4-9407-11D2-89D9-0020184077E1}'),
		"PartNumber": (107, 2, (8, 0), (), "PartNumber", None),
		"ReuseAccessMode": (105, 2, (3, 0), (), "ReuseAccessMode", None),
		# Method 'ReusedBlock' returns object of type 'IMGCVariantMgrReusedBlock'
		"ReusedBlock": (113, 2, (9, 0), (), "ReusedBlock", '{82CD5AA4-9407-11D2-89D9-0020184077E1}'),
		# Method 'RootIF' returns object of type 'IMGCVariantMgrDocument'
		"RootIF": (22, 2, (9, 0), (), "RootIF", '{78663807-9407-11D2-89D9-0020184077E1}'),
		# Method 'SymbolLocation' returns object of type 'IMGCVariantMgrSymbolLocation'
		"SymbolLocation": (101, 2, (9, 0), (), "SymbolLocation", '{786637F3-9407-11D2-89D9-0020184077E1}'),
		"SymbolType": (103, 2, (3, 0), (), "SymbolType", None),
	}
	_prop_map_put_ = {
		"AccessLock": ((5, LCID, 4, 0),()),
		"AliasPartNumber": ((117, LCID, 4, 0),()),
		"ArrayCompName": ((115, LCID, 4, 0),()),
		"Cell": ((106, LCID, 4, 0),()),
		"ModificationCount": ((20, LCID, 4, 0),()),
		"ModificationCountEx": ((24, LCID, 4, 0),()),
		"ModificationCountLock": ((21, LCID, 4, 0),()),
		"Name": ((30, LCID, 4, 0),()),
		"Parent": ((1, LCID, 8, 0),()),
		"PartNumber": ((107, LCID, 4, 0),()),
		"SymbolType": ((103, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMGCVariantMgrSymbolFilter(DispatchBaseClass):
	CLSID = IID('{9ADE593A-D453-4433-B7EF-281D82D31EAD}')
	coclass_clsid = IID('{3D8BA603-4843-461C-8153-D64FE1DF8380}')

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
		return self._oleobj_.InvokeTypes(103, LCID, 1, (24, 0), (),)

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
		"OnlyBorderSymbols": (102, 2, (11, 0), (), "OnlyBorderSymbols", None),
		"Parent": (1, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
		"AccessLock": ((5, LCID, 4, 0),()),
		"OnlyBorderSymbols": ((102, LCID, 4, 0),()),
		"Parent": ((1, LCID, 8, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMGCVariantMgrSymbolInfoRec(DispatchBaseClass):
	'Variant manager symbol info record'
	CLSID = IID('{A34D9F27-362F-45AA-9F73-CBC28DF7645E}')
	coclass_clsid = IID('{68DE764E-F9B0-4B22-897E-CB0392034977}')

	def CompareUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Compares a UID with the UID of the object. Returns true if equal.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((19, 1), (19, 1), (19, 1)),userID
			, objectID, objectType)

	def CreatePackModData(self):
		'Creates the package mod data for the symbol info rec.'
		return self._oleobj_.InvokeTypes(105, LCID, 1, (2, 0), (),)

	def Delete(self):
		'Deletes the symbol info record.'
		return self._oleobj_.InvokeTypes(103, LCID, 1, (11, 0), (),)

	# Result is of type IMGCVariantMgrFMVProperty
	def FindFMVProperty(self, functionDefinition=defaultNamedNotOptArg):
		'Finds an FMV property based on a function spec.'
		ret = self._oleobj_.InvokeTypes(107, LCID, 1, (9, 0), ((12, 1),),functionDefinition
			)
		if ret is not None:
			ret = Dispatch(ret, 'FindFMVProperty', '{DD445D35-DC4B-413A-8781-F561D40D4CC5}')
		return ret

	# Result is of type IMGCVariantMgrFMVProperties
	# The method GetFMVProperties is actually a property, but must be used as a method to correctly pass the arguments
	def GetFMVProperties(self, filter=defaultNamedOptArg):
		'Returns a collection of FMV properties'
		ret = self._oleobj_.InvokeTypes(102, LCID, 2, (9, 0), ((12, 17),),filter
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetFMVProperties', '{3C44AB05-4C95-4984-BD98-135CDD2B39C1}')
		return ret

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

	# Result is of type IMGCVariantMgrFMVProperty
	def PutFMVProperty(self, functionDefinition=defaultNamedNotOptArg, changeOper=defaultNamedNotOptArg, PartNumber='', cellName=''):
		'Creates a FMV property.'
		return self._ApplyTypes_(106, 1, (9, 32), ((12, 1), (3, 1), (8, 49), (8, 49)), 'PutFMVProperty', '{DD445D35-DC4B-413A-8781-F561D40D4CC5}',functionDefinition
			, changeOper, PartNumber, cellName)

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
		# Method 'FMVProperties' returns object of type 'IMGCVariantMgrFMVProperties'
		"FMVProperties": (102, 2, (9, 0), ((12, 17),), "FMVProperties", '{3C44AB05-4C95-4984-BD98-135CDD2B39C1}'),
		"InternalIndex": (2, 2, (3, 0), (), "InternalIndex", None),
		"ModificationCount": (20, 2, (2, 0), (), "ModificationCount", None),
		"ModificationCountEx": (24, 2, (3, 0), (), "ModificationCountEx", None),
		"ModificationCountLock": (21, 2, (11, 0), (), "ModificationCountLock", None),
		"Name": (30, 2, (8, 0), (), "Name", None),
		"Parent": (1, 2, (9, 0), (), "Parent", None),
		"ReuseAccessMode": (104, 2, (3, 0), (), "ReuseAccessMode", None),
		# Method 'RootIF' returns object of type 'IMGCVariantMgrDocument'
		"RootIF": (22, 2, (9, 0), (), "RootIF", '{78663807-9407-11D2-89D9-0020184077E1}'),
		# Method 'Symbol' returns object of type 'IMGCVariantMgrSymbol'
		"Symbol": (101, 2, (9, 0), (), "Symbol", '{786637F4-9407-11D2-89D9-0020184077E1}'),
	}
	_prop_map_put_ = {
		"AccessLock": ((5, LCID, 4, 0),()),
		"ModificationCount": ((20, LCID, 4, 0),()),
		"ModificationCountEx": ((24, LCID, 4, 0),()),
		"ModificationCountLock": ((21, LCID, 4, 0),()),
		"Name": ((30, LCID, 4, 0),()),
		"Parent": ((1, LCID, 8, 0),()),
		"Symbol": ((101, LCID, 8, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMGCVariantMgrSymbolInfoRecs(DispatchBaseClass):
	'Variant manager symbol info recs collection'
	CLSID = IID('{A6C3A4DE-6048-492D-AA03-EC268CCC73D4}')
	coclass_clsid = IID('{B1A416FE-D9E6-4653-B05F-DE31BFE31772}')

	def Add(self, pSymbIRec=defaultNamedNotOptArg):
		'Adds a symbol info record to the collection.'
		return self._oleobj_.InvokeTypes(102, LCID, 1, (24, 0), ((9, 1),),pSymbIRec
			)

	def CompareUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Compares a UID with the UID of the object. Returns true if equal.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((19, 1), (19, 1), (19, 1)),userID
			, objectID, objectType)

	def CreatePackModData(self):
		'Creates the package mod data for the symbol info recs.'
		return self._oleobj_.InvokeTypes(105, LCID, 1, (2, 0), (),)

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

	# Result is of type IMGCVariantMgrSymbolInfoRec
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, index=defaultNamedNotOptArg):
		'Returns a symbol modification object at a given index.'
		ret = self._oleobj_.InvokeTypes(101, LCID, 2, (9, 0), ((12, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{A34D9F27-362F-45AA-9F73-CBC28DF7645E}')
		return ret

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
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{A34D9F27-362F-45AA-9F73-CBC28DF7645E}')
	#This class has Item property/method which allows indexed access with the object[key] syntax.
	#Some objects will accept a string or other type of key in addition to integers.
	#Note that many Office objects do not use zero-based indexing.
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(101, LCID, 2, 1, key)), "Item", '{A34D9F27-362F-45AA-9F73-CBC28DF7645E}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(30, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IMGCVariantMgrSymbolLocation(DispatchBaseClass):
	'Variant manager schematic location object'
	CLSID = IID('{786637F3-9407-11D2-89D9-0020184077E1}')
	coclass_clsid = IID('{786637F3-9407-20D2-89D9-0020184077E1}')

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
		"Page": (102, 2, (8, 0), (), "Page", None),
		"PageIndex": (105, 2, (2, 0), (), "PageIndex", None),
		"Parent": (1, 2, (9, 0), (), "Parent", None),
		"Path": (101, 2, (8, 0), (), "Path", None),
		"PathIndex": (104, 2, (2, 0), (), "PathIndex", None),
		"id": (103, 2, (3, 0), (), "id", None),
	}
	_prop_map_put_ = {
		"AccessLock": ((5, LCID, 4, 0),()),
		"Page": ((102, LCID, 4, 0),()),
		"Parent": ((1, LCID, 8, 0),()),
		"Path": ((101, LCID, 4, 0),()),
		"id": ((103, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMGCVariantMgrSymbolLocations(DispatchBaseClass):
	'Variant manager symbol locations'
	CLSID = IID('{786637F8-9407-11D2-89D9-0020184077E1}')
	coclass_clsid = IID('{786637F8-9407-20D2-89D9-0020184077E1}')

	def Add(self, pLoc=defaultNamedNotOptArg):
		'Adds a schema location object to the collection.'
		return self._oleobj_.InvokeTypes(102, LCID, 1, (24, 0), ((9, 1),),pLoc
			)

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

	# Result is of type IMGCVariantMgrSymbolLocation
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, index=defaultNamedNotOptArg):
		'Returns a schema location object at a given index.'
		ret = self._oleobj_.InvokeTypes(101, LCID, 2, (9, 0), ((12, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{786637F3-9407-11D2-89D9-0020184077E1}')
		return ret

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
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{786637F3-9407-11D2-89D9-0020184077E1}')
	#This class has Item property/method which allows indexed access with the object[key] syntax.
	#Some objects will accept a string or other type of key in addition to integers.
	#Note that many Office objects do not use zero-based indexing.
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(101, LCID, 2, 1, key)), "Item", '{786637F3-9407-11D2-89D9-0020184077E1}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(30, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IMGCVariantMgrSymbols(DispatchBaseClass):
	'Variant manager schematic symbols collection'
	CLSID = IID('{786637F7-9407-11D2-89D9-0020184077E1}')
	coclass_clsid = IID('{786637F7-9407-20D2-89D9-0020184077E1}')

	def Add(self, pSymbol=defaultNamedNotOptArg):
		'Adds a symbol to the collection.'
		return self._oleobj_.InvokeTypes(102, LCID, 1, (24, 0), ((9, 1),),pSymbol
			)

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

	# Result is of type IMGCVariantMgrSymbol
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, index=defaultNamedNotOptArg):
		'Returns a symbol object at a given index.'
		ret = self._oleobj_.InvokeTypes(101, LCID, 2, (9, 0), ((12, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{786637F4-9407-11D2-89D9-0020184077E1}')
		return ret

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
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{786637F4-9407-11D2-89D9-0020184077E1}')
	#This class has Item property/method which allows indexed access with the object[key] syntax.
	#Some objects will accept a string or other type of key in addition to integers.
	#Note that many Office objects do not use zero-based indexing.
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(101, LCID, 2, 1, key)), "Item", '{786637F4-9407-11D2-89D9-0020184077E1}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(30, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IMGCVariantMgrUID(DispatchBaseClass):
	'Variant manager utility UID object.'
	CLSID = IID('{D9AA5BF5-2389-40CA-9E58-8A7A59B2AF31}')
	coclass_clsid = IID('{8B45CF63-6CF5-1014-857A-77B9EECCF0AC}')

	def CompareObj(self, obj=defaultNamedNotOptArg):
		'Compare the UIDs using object .'
		return self._oleobj_.InvokeTypes(106, LCID, 1, (11, 0), ((9, 1),),obj
			)

	def GetValue(self, userID=pythoncom.Missing, objectID=pythoncom.Missing, objectType=pythoncom.Missing):
		'Initializes the UID.'
		return self._ApplyTypes_(104, 1, (24, 0), ((16403, 2), (16403, 2), (16403, 2)), 'GetValue', None,userID
			, objectID, objectType)

	def Initialize(self, userID=0, objectID=0, objectType=0):
		'Initializes the UID.'
		return self._oleobj_.InvokeTypes(103, LCID, 1, (24, 0), ((19, 49), (19, 49), (19, 49)),userID
			, objectID, objectType)

	def InitializeObj(self, obj=defaultNamedNotOptArg):
		'Initializes the UID using object .'
		return self._oleobj_.InvokeTypes(105, LCID, 1, (24, 0), ((9, 1),),obj
			)

	_prop_map_get_ = {
		"objectID": (101, 2, (19, 0), (), "objectID", None),
		"objectType": (102, 2, (19, 0), (), "objectType", None),
		"userID": (100, 2, (19, 0), (), "userID", None),
	}
	_prop_map_put_ = {
		"objectID": ((101, LCID, 4, 0),()),
		"objectType": ((102, LCID, 4, 0),()),
		"userID": ((100, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMGCVariantMgrUtility(DispatchBaseClass):
	'Variant manager utility object'
	CLSID = IID('{EE5CB44B-13CF-480C-B096-5A2D731A9535}')
	coclass_clsid = IID('{E08A46A8-C405-4073-ABB1-FB2B94A45C5F}')

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
		# Method 'Filters' returns object of type 'IMGCVariantMgrFilters'
		"Filters": (100, 2, (9, 0), (), "Filters", '{C9D96C16-A541-4DA9-97E0-902FCD6C2412}'),
		"InternalIndex": (2, 2, (3, 0), (), "InternalIndex", None),
		"Parent": (1, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
		"AccessLock": ((5, LCID, 4, 0),()),
		"Parent": ((1, LCID, 8, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMGCVariantMgrVariant(DispatchBaseClass):
	'Variant manager variant object'
	CLSID = IID('{78663802-9407-11D2-89D9-0020184077E1}')
	coclass_clsid = IID('{78663802-9407-20D2-89D9-0020184077E1}')

	def CompareUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Compares a UID with the UID of the object. Returns true if equal.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((19, 1), (19, 1), (19, 1)),userID
			, objectID, objectType)

	def Delete(self):
		'Deletes the variant'
		return self._oleobj_.InvokeTypes(108, LCID, 1, (11, 0), (),)

	# Result is of type IMGCVariantMgrPackageModifications
	# The method GetPackageModifications is actually a property, but must be used as a method to correctly pass the arguments
	def GetPackageModifications(self, filter=defaultNamedOptArg):
		'Gets the collection of packages that are to be modified for this variant'
		ret = self._oleobj_.InvokeTypes(104, LCID, 2, (9, 0), ((12, 17),),filter
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetPackageModifications', '{786637FE-9407-11D2-89D9-0020184077E1}')
		return ret

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
		"BOMInclude": (110, 2, (11, 0), (), "BOMInclude", None),
		"Description": (101, 2, (8, 0), (), "Description", None),
		"FXEInclude": (109, 2, (11, 0), (), "FXEInclude", None),
		"FuncAttached": (111, 2, (11, 0), (), "FuncAttached", None),
		"Hyperlink": (112, 2, (8, 0), (), "Hyperlink", None),
		"InternalIndex": (2, 2, (3, 0), (), "InternalIndex", None),
		"ModificationCount": (20, 2, (2, 0), (), "ModificationCount", None),
		"ModificationCountEx": (24, 2, (3, 0), (), "ModificationCountEx", None),
		"ModificationCountLock": (21, 2, (11, 0), (), "ModificationCountLock", None),
		"Name": (30, 2, (8, 0), (), "Name", None),
		"NotesLayers": (113, 2, (8, 0), (), "NotesLayers", None),
		"Number": (102, 2, (8, 0), (), "Number", None),
		# Method 'PackageModifications' returns object of type 'IMGCVariantMgrPackageModifications'
		"PackageModifications": (104, 2, (9, 0), ((12, 17),), "PackageModifications", '{786637FE-9407-11D2-89D9-0020184077E1}'),
		"Parent": (1, 2, (9, 0), (), "Parent", None),
		# Method 'RootIF' returns object of type 'IMGCVariantMgrDocument'
		"RootIF": (22, 2, (9, 0), (), "RootIF", '{78663807-9407-11D2-89D9-0020184077E1}'),
		"Type": (106, 2, (3, 0), (), "Type", None),
	}
	_prop_map_put_ = {
		"AccessLock": ((5, LCID, 4, 0),()),
		"BOMInclude": ((110, LCID, 4, 0),()),
		"Description": ((101, LCID, 4, 0),()),
		"FXEInclude": ((109, LCID, 4, 0),()),
		"FuncAttached": ((111, LCID, 4, 0),()),
		"Hyperlink": ((112, LCID, 4, 0),()),
		"ModificationCount": ((20, LCID, 4, 0),()),
		"ModificationCountEx": ((24, LCID, 4, 0),()),
		"ModificationCountLock": ((21, LCID, 4, 0),()),
		"Name": ((30, LCID, 4, 0),()),
		"NotesLayers": ((113, LCID, 4, 0),()),
		"Number": ((102, LCID, 4, 0),()),
		"Parent": ((1, LCID, 8, 0),()),
		"Type": ((106, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMGCVariantMgrVariantAssignment(DispatchBaseClass):
	CLSID = IID('{874DEFFA-9480-4725-BCE3-06FE0427B1CA}')
	coclass_clsid = IID('{C1F669F9-84C7-480A-AF88-6A601077674A}')

	def CompareUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Compares a UID with the UID of the object. Returns true if equal.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((19, 1), (19, 1), (19, 1)),userID
			, objectID, objectType)

	def Delete(self):
		'Deletes the variant assignment.'
		return self._oleobj_.InvokeTypes(102, LCID, 1, (11, 0), (),)

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
		# Method 'Variant' returns object of type 'IMGCVariantMgrVariant'
		"Variant": (101, 2, (9, 0), (), "Variant", '{78663802-9407-11D2-89D9-0020184077E1}'),
	}
	_prop_map_put_ = {
		"AccessLock": ((5, LCID, 4, 0),()),
		"ModificationCount": ((20, LCID, 4, 0),()),
		"ModificationCountEx": ((24, LCID, 4, 0),()),
		"ModificationCountLock": ((21, LCID, 4, 0),()),
		"Parent": ((1, LCID, 8, 0),()),
		"Variant": ((101, LCID, 8, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMGCVariantMgrVariantAssignments(DispatchBaseClass):
	'Variant assignments collection'
	CLSID = IID('{7255B70F-5A93-4770-8D66-A32C07310BA1}')
	coclass_clsid = IID('{5A99035D-F675-4DE5-9A15-9EB193E5B9FE}')

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

	# Result is of type IMGCVariantMgrVariantAssignment
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, index=defaultNamedNotOptArg):
		'Returns a package object at a given index.'
		ret = self._oleobj_.InvokeTypes(101, LCID, 2, (9, 0), ((12, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{874DEFFA-9480-4725-BCE3-06FE0427B1CA}')
		return ret

	def MoveDown(self, pObj=defaultNamedNotOptArg, moveDelta=1):
		'Moves a variant down in the list of variant'
		return self._oleobj_.InvokeTypes(103, LCID, 1, (2, 0), ((9, 1), (2, 49)),pObj
			, moveDelta)

	def MoveUp(self, pObj=defaultNamedNotOptArg, moveDelta=1):
		'Moves a variant up in the list of variant'
		return self._oleobj_.InvokeTypes(102, LCID, 1, (2, 0), ((9, 1), (2, 49)),pObj
			, moveDelta)

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
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{874DEFFA-9480-4725-BCE3-06FE0427B1CA}')
	#This class has Item property/method which allows indexed access with the object[key] syntax.
	#Some objects will accept a string or other type of key in addition to integers.
	#Note that many Office objects do not use zero-based indexing.
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(101, LCID, 2, 1, key)), "Item", '{874DEFFA-9480-4725-BCE3-06FE0427B1CA}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(30, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IMGCVariantMgrVariantGroup(DispatchBaseClass):
	CLSID = IID('{3809BA4C-72E2-436F-B258-88EBA46444C8}')
	coclass_clsid = IID('{F15DA467-46F8-449D-97B4-0C929B7DF4E8}')

	def CompareUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Compares a UID with the UID of the object. Returns true if equal.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((19, 1), (19, 1), (19, 1)),userID
			, objectID, objectType)

	def Delete(self):
		'Deletes the variant group.'
		return self._oleobj_.InvokeTypes(103, LCID, 1, (11, 0), (),)

	# Result is of type IMGCVariantMgrVariantAssignment
	def FindVariantAssignment(self, variantDefinition=defaultNamedNotOptArg):
		'Find a variant assignment for a variant.'
		ret = self._oleobj_.InvokeTypes(105, LCID, 1, (9, 0), ((12, 1),),variantDefinition
			)
		if ret is not None:
			ret = Dispatch(ret, 'FindVariantAssignment', '{874DEFFA-9480-4725-BCE3-06FE0427B1CA}')
		return ret

	def GetUID(self, userID=pythoncom.Missing, objectID=pythoncom.Missing, objectType=pythoncom.Missing):
		'Gets the UID of an object. Returns false if the UID is invalid.'
		return self._ApplyTypes_(6, 1, (11, 0), ((16403, 2), (16403, 2), (16403, 2)), 'GetUID', None,userID
			, objectID, objectType)

	# Result is of type IMGCVariantMgrVariantAssignments
	# The method GetVariantAssignments is actually a property, but must be used as a method to correctly pass the arguments
	def GetVariantAssignments(self, filter=defaultNamedOptArg):
		'Returns a collection of variants that are part of the group.'
		ret = self._oleobj_.InvokeTypes(102, LCID, 2, (9, 0), ((12, 17),),filter
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetVariantAssignments', '{7255B70F-5A93-4770-8D66-A32C07310BA1}')
		return ret

	def IncModificationCount(self, value=1):
		'Increments the modification count'
		return self._oleobj_.InvokeTypes(23, LCID, 1, (2, 0), ((2, 49),),value
			)

	def IsValid(self):
		'Returns the internal (CPP) index of the X-Object'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), (),)

	# Result is of type IMGCVariantMgrVariantAssignment
	def PutVariantAssignment(self, variantDefinition=defaultNamedNotOptArg, position=-1):
		'Adds a new variant assignment to the group.'
		ret = self._oleobj_.InvokeTypes(104, LCID, 1, (9, 0), ((12, 1), (2, 49)),variantDefinition
			, position)
		if ret is not None:
			ret = Dispatch(ret, 'PutVariantAssignment', '{874DEFFA-9480-4725-BCE3-06FE0427B1CA}')
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
		"Description": (101, 2, (8, 0), (), "Description", None),
		"InternalIndex": (2, 2, (3, 0), (), "InternalIndex", None),
		"ModificationCount": (20, 2, (2, 0), (), "ModificationCount", None),
		"ModificationCountEx": (24, 2, (3, 0), (), "ModificationCountEx", None),
		"ModificationCountLock": (21, 2, (11, 0), (), "ModificationCountLock", None),
		"Name": (30, 2, (8, 0), (), "Name", None),
		"Parent": (1, 2, (9, 0), (), "Parent", None),
		# Method 'RootIF' returns object of type 'IMGCVariantMgrDocument'
		"RootIF": (22, 2, (9, 0), (), "RootIF", '{78663807-9407-11D2-89D9-0020184077E1}'),
		# Method 'VariantAssignments' returns object of type 'IMGCVariantMgrVariantAssignments'
		"VariantAssignments": (102, 2, (9, 0), ((12, 17),), "VariantAssignments", '{7255B70F-5A93-4770-8D66-A32C07310BA1}'),
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
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMGCVariantMgrVariantGroups(DispatchBaseClass):
	'Variant manager variant groups collection'
	CLSID = IID('{19DBCD8C-D9AF-4B85-8439-89F12F23F406}')
	coclass_clsid = IID('{C65DD74F-E63D-4B2C-BF64-932CEA392102}')

	def Add(self, pGroup=defaultNamedNotOptArg):
		'Adds a group to the collection.'
		return self._oleobj_.InvokeTypes(102, LCID, 1, (24, 0), ((9, 1),),pGroup
			)

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

	# Result is of type IMGCVariantMgrVariantGroup
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, index=defaultNamedNotOptArg):
		'Returns a group object at a given index.'
		ret = self._oleobj_.InvokeTypes(101, LCID, 2, (9, 0), ((12, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{3809BA4C-72E2-436F-B258-88EBA46444C8}')
		return ret

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
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{3809BA4C-72E2-436F-B258-88EBA46444C8}')
	#This class has Item property/method which allows indexed access with the object[key] syntax.
	#Some objects will accept a string or other type of key in addition to integers.
	#Note that many Office objects do not use zero-based indexing.
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(101, LCID, 2, 1, key)), "Item", '{3809BA4C-72E2-436F-B258-88EBA46444C8}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(30, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IMGCVariantMgrVariantInfoRec(DispatchBaseClass):
	'Variant manager variant info record'
	CLSID = IID('{162B6B80-35C5-4FE7-A1C8-62D9FE3DADD3}')
	coclass_clsid = IID('{17760C13-0FFB-4577-A56E-4A558EAD2B31}')

	def CompareUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Compares a UID with the UID of the object. Returns true if equal.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((19, 1), (19, 1), (19, 1)),userID
			, objectID, objectType)

	# Result is of type IMGCVariantMgrProperties
	# The method GetProperties is actually a property, but must be used as a method to correctly pass the arguments
	def GetProperties(self, filter=defaultNamedOptArg):
		'Returns a collection of properties'
		ret = self._oleobj_.InvokeTypes(101, LCID, 2, (9, 0), ((12, 17),),filter
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetProperties', '{FA1219FB-D82D-47B6-815F-F786F347E6E6}')
		return ret

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

	# Result is of type IMGCVariantMgrProperty
	def PutProperty(self, key=defaultNamedNotOptArg, value=defaultNamedNotOptArg):
		'Adds/changes a property record to the collection.'
		ret = self._oleobj_.InvokeTypes(102, LCID, 1, (9, 0), ((8, 1), (8, 1)),key
			, value)
		if ret is not None:
			ret = Dispatch(ret, 'PutProperty', '{6ABBB0DE-2FAC-45DB-90CA-E90A630B0FBB}')
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
		"ModificationCount": (20, 2, (2, 0), (), "ModificationCount", None),
		"ModificationCountEx": (24, 2, (3, 0), (), "ModificationCountEx", None),
		"ModificationCountLock": (21, 2, (11, 0), (), "ModificationCountLock", None),
		"Name": (30, 2, (8, 0), (), "Name", None),
		"Parent": (1, 2, (9, 0), (), "Parent", None),
		# Method 'Properties' returns object of type 'IMGCVariantMgrProperties'
		"Properties": (101, 2, (9, 0), ((12, 17),), "Properties", '{FA1219FB-D82D-47B6-815F-F786F347E6E6}'),
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
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMGCVariantMgrVariantInfoRecs(DispatchBaseClass):
	'Variant manager variant info recs collection'
	CLSID = IID('{F7FF7F27-3A87-458B-9C36-934DBF14A287}')
	coclass_clsid = IID('{4E6C1C8E-542F-4561-ADD3-ADA3C4E2B323}')

	def Add(self, pSymbIRec=defaultNamedNotOptArg):
		'Adds a variant info record to the collection.'
		return self._oleobj_.InvokeTypes(102, LCID, 1, (24, 0), ((9, 1),),pSymbIRec
			)

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

	# Result is of type IMGCVariantMgrVariantInfoRec
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, index=defaultNamedNotOptArg):
		'Returns a symbol modification object at a given index.'
		ret = self._oleobj_.InvokeTypes(101, LCID, 2, (9, 0), ((12, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{162B6B80-35C5-4FE7-A1C8-62D9FE3DADD3}')
		return ret

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
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{162B6B80-35C5-4FE7-A1C8-62D9FE3DADD3}')
	#This class has Item property/method which allows indexed access with the object[key] syntax.
	#Some objects will accept a string or other type of key in addition to integers.
	#Note that many Office objects do not use zero-based indexing.
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(101, LCID, 2, 1, key)), "Item", '{162B6B80-35C5-4FE7-A1C8-62D9FE3DADD3}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(30, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IMGCVariantMgrVariantInfoRecsUtility(DispatchBaseClass):
	'Variant manager variant inforec utility.'
	CLSID = IID('{138F998B-642F-436E-BEA2-986E1B29A353}')
	coclass_clsid = IID('{180960C2-CD47-4C0C-B446-8C558D69CA0E}')

	def CompareUID(self, userID=defaultNamedNotOptArg, objectID=defaultNamedNotOptArg, objectType=defaultNamedNotOptArg):
		'Compares a UID with the UID of the object. Returns true if equal.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((19, 1), (19, 1), (19, 1)),userID
			, objectID, objectType)

	# Result is of type IMGCVariantMgrVariantInfoRec
	def FindVariantInfoRec(self, variantSpec=defaultNamedNotOptArg):
		'Find a variant information record'
		ret = self._oleobj_.InvokeTypes(101, LCID, 1, (9, 0), ((12, 1),),variantSpec
			)
		if ret is not None:
			ret = Dispatch(ret, 'FindVariantInfoRec', '{162B6B80-35C5-4FE7-A1C8-62D9FE3DADD3}')
		return ret

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
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMGCVariantMgrVariantMapping(DispatchBaseClass):
	'Variant manager variant mapping object.'
	CLSID = IID('{746F9DCE-E85C-4BA5-BE14-FEF24731222A}')
	coclass_clsid = IID('{9424AF28-132F-4123-9124-395F25BD960B}')

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
		"MappingFlags": (102, 2, (3, 0), (), "MappingFlags", None),
		"ModificationCount": (20, 2, (2, 0), (), "ModificationCount", None),
		"ModificationCountEx": (24, 2, (3, 0), (), "ModificationCountEx", None),
		"ModificationCountLock": (21, 2, (11, 0), (), "ModificationCountLock", None),
		"NewName": (101, 2, (8, 0), (), "NewName", None),
		"OriginalName": (100, 2, (8, 0), (), "OriginalName", None),
		"Parent": (1, 2, (9, 0), (), "Parent", None),
		# Method 'RootIF' returns object of type 'IMGCVariantMgrDocument'
		"RootIF": (22, 2, (9, 0), (), "RootIF", '{78663807-9407-11D2-89D9-0020184077E1}'),
	}
	_prop_map_put_ = {
		"AccessLock": ((5, LCID, 4, 0),()),
		"MappingFlags": ((102, LCID, 4, 0),()),
		"ModificationCount": ((20, LCID, 4, 0),()),
		"ModificationCountEx": ((24, LCID, 4, 0),()),
		"ModificationCountLock": ((21, LCID, 4, 0),()),
		"NewName": ((101, LCID, 4, 0),()),
		"OriginalName": ((100, LCID, 4, 0),()),
		"Parent": ((1, LCID, 8, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMGCVariantMgrVariantMappings(DispatchBaseClass):
	'Variant manager variant mappings collection'
	CLSID = IID('{5F5FA27B-9A28-4A84-BE9A-7460F1D6D54B}')
	coclass_clsid = IID('{47653D5E-3982-45EE-8711-A5130875EB1C}')

	def Add(self, pVariantMapping=defaultNamedNotOptArg):
		'Adds a variant mapping to its collection.'
		return self._oleobj_.InvokeTypes(102, LCID, 1, (24, 0), ((9, 1),),pVariantMapping
			)

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

	# Result is of type IMGCVariantMgrVariantMapping
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, index=defaultNamedNotOptArg):
		'Returns a variant mapping object at a given index.'
		ret = self._oleobj_.InvokeTypes(101, LCID, 2, (9, 0), ((12, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{746F9DCE-E85C-4BA5-BE14-FEF24731222A}')
		return ret

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
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{746F9DCE-E85C-4BA5-BE14-FEF24731222A}')
	#This class has Item property/method which allows indexed access with the object[key] syntax.
	#Some objects will accept a string or other type of key in addition to integers.
	#Note that many Office objects do not use zero-based indexing.
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(101, LCID, 2, 1, key)), "Item", '{746F9DCE-E85C-4BA5-BE14-FEF24731222A}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(30, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IMGCVariantMgrVariants(DispatchBaseClass):
	'Variant manager variants collection'
	CLSID = IID('{78663803-9407-11D2-89D9-0020184077E1}')
	coclass_clsid = IID('{78663803-9407-20D2-89D9-0020184077E1}')

	def Add(self, pVariant=defaultNamedNotOptArg):
		'Adds a variant to the collection.'
		return self._oleobj_.InvokeTypes(102, LCID, 1, (24, 0), ((9, 1),),pVariant
			)

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

	# Result is of type IMGCVariantMgrVariant
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, index=defaultNamedNotOptArg):
		'Returns a variant object at a given index.'
		ret = self._oleobj_.InvokeTypes(101, LCID, 2, (9, 0), ((12, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{78663802-9407-11D2-89D9-0020184077E1}')
		return ret

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
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{78663802-9407-11D2-89D9-0020184077E1}')
	#This class has Item property/method which allows indexed access with the object[key] syntax.
	#Some objects will accept a string or other type of key in addition to integers.
	#Note that many Office objects do not use zero-based indexing.
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(101, LCID, 2, 1, key)), "Item", '{78663802-9407-11D2-89D9-0020184077E1}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(30, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ITest(DispatchBaseClass):
	'ITest Interface'
	CLSID = IID('{8ADA56FC-3345-41CA-B16B-AB446D82790D}')
	coclass_clsid = None

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _IMGCVariantMgrBaseDummy(DispatchBaseClass):
	'The base dummy interface'
	CLSID = IID('{DA637EAA-704A-4A97-9C0E-F7B4D07751E2}')
	coclass_clsid = IID('{C1453F6A-07E7-42F1-B7A6-1F6B698798E6}')

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _IMGCVariantMgrDocumentEvents:
	'Event interface for variant document.'
	CLSID = CLSID_Sink = IID('{FFD61045-44FD-4F80-995C-6C6F0AE1DEB0}')
	coclass_clsid = IID('{8B45CE2D-6CF5-1014-857A-77B9EECCF0AC}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnDocumentChanged",
		        2 : "OnFMVFunctionDataChanged",
		        3 : "OnFMVFunctionDefChanged",
		        4 : "OnVariantGroupDataChanged",
		        5 : "OnVariantGroupDefChanged",
		        6 : "OnFMVFunctionGroupDataChanged",
		        7 : "OnFMVFunctionGroupDefChanged",
		        8 : "OnVariantDataChanged",
		        9 : "OnVariantDefChanged",
		       10 : "OnShowEquivalentParts",
		       11 : "OnICDBEvent",
		       12 : "OnICDBBroadcastEvent",
		       13 : "OnSymbolSelect",
		       14 : "OnSymbolUnselect",
		       15 : "OnPackageSelect",
		       16 : "OnPackageUnselect",
		       17 : "OnPackagerStateChange",
		       18 : "OnNotifyChanges",
		       19 : "OnChange",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnDocumentChanged(self, modCount=defaultNamedNotOptArg):
#		'Fired when something has changed in the document'
#	def OnFMVFunctionDataChanged(self, pFMVFunction=defaultNamedNotOptArg, pPackMod=defaultNamedNotOptArg, pSymbolMod=defaultNamedNotOptArg, typeOfChange=defaultNamedNotOptArg):
#		'Fired when the contents of an FMV function has changed'
#	def OnFMVFunctionDefChanged(self, pFMVFunction=defaultNamedNotOptArg, typeOfChange=defaultNamedNotOptArg):
#		'Fired when a function definition has changed'
#	def OnVariantGroupDataChanged(self, pGroup=defaultNamedNotOptArg, typeOfChange=defaultNamedNotOptArg):
#		'Fired when the data of a group has been changed'
#	def OnVariantGroupDefChanged(self, pGroup=defaultNamedNotOptArg, typeOfChange=defaultNamedNotOptArg):
#		'Fired when a group definition has been changed'
#	def OnFMVFunctionGroupDataChanged(self, pGroup=defaultNamedNotOptArg, typeOfChange=defaultNamedNotOptArg):
#		'Fired when the data of a group has been changed'
#	def OnFMVFunctionGroupDefChanged(self, pGroup=defaultNamedNotOptArg, typeOfChange=defaultNamedNotOptArg):
#		'Fired when a group definition has been changed'
#	def OnVariantDataChanged(self, pVariant=defaultNamedNotOptArg, typeOfChange=defaultNamedNotOptArg):
#		'Fired when the data of a variant has been changed'
#	def OnVariantDefChanged(self, pGroup=defaultNamedNotOptArg, typeOfChange=defaultNamedNotOptArg):
#		'Fired when a variant definition has been changed'
#	def OnShowEquivalentParts(self, pGroup=defaultNamedNotOptArg, pSymbol=defaultNamedNotOptArg):
#		'Fired when a list of equivalent parts must be composed.'
#	def OnICDBEvent(self, eventType=defaultNamedNotOptArg, userID1=defaultNamedNotOptArg, objectID1=defaultNamedNotOptArg, objectType1=defaultNamedNotOptArg
#			, userID2=defaultNamedNotOptArg, objectID2=defaultNamedNotOptArg, objectType2=defaultNamedNotOptArg):
#		'Fired when the ICDB has fired an event.'
#	def OnICDBBroadcastEvent(self, messContent=defaultNamedNotOptArg, categoryID=defaultNamedNotOptArg):
#		'Fired when the ICDB has broadcast an event.'
#	def OnSymbolSelect(self, source=defaultNamedNotOptArg, Count=defaultNamedNotOptArg, totalCount=defaultNamedNotOptArg, clear_previous=defaultNamedNotOptArg
#			, symb_userID=defaultNamedNotOptArg, symb_objectID=defaultNamedNotOptArg, symb_objectType=defaultNamedNotOptArg, path_userID=defaultNamedNotOptArg, path_objectID=defaultNamedNotOptArg
#			, path_objectType=defaultNamedNotOptArg):
#		'Fired when a symbol has been selected.'
#	def OnSymbolUnselect(self, source=defaultNamedNotOptArg, Count=defaultNamedNotOptArg, totalCount=defaultNamedNotOptArg, clear_previous=defaultNamedNotOptArg
#			, symb_userID=defaultNamedNotOptArg, symb_objectID=defaultNamedNotOptArg, symb_objectType=defaultNamedNotOptArg, path_userID=defaultNamedNotOptArg, path_objectID=defaultNamedNotOptArg
#			, path_objectType=defaultNamedNotOptArg):
#		'Fired when a symbol has been unselected.'
#	def OnPackageSelect(self, source=defaultNamedNotOptArg, packName=defaultNamedNotOptArg, Count=defaultNamedNotOptArg, totalCount=defaultNamedNotOptArg
#			, clear_previous=defaultNamedNotOptArg, package_userID=defaultNamedNotOptArg, package_objectID=defaultNamedNotOptArg, package_objectType=defaultNamedNotOptArg):
#		'Fired when a package has been selected.'
#	def OnPackageUnselect(self, source=defaultNamedNotOptArg, packName=defaultNamedNotOptArg, Count=defaultNamedNotOptArg, totalCount=defaultNamedNotOptArg
#			, clear_previous=defaultNamedNotOptArg, package_userID=defaultNamedNotOptArg, package_objectID=defaultNamedNotOptArg, package_objectType=defaultNamedNotOptArg):
#		'Fired when a package has been unselected.'
#	def OnPackagerStateChange(self, procState=defaultNamedNotOptArg):
#		'Fired when the packager process changes state.'
#	def OnNotifyChanges(self, _userID=defaultNamedNotOptArg, _objectID=defaultNamedNotOptArg, _objectType=defaultNamedNotOptArg, objType=defaultNamedNotOptArg):
#		'Fired when something has changed in the document'
#	def OnChange(self, _objectType=defaultNamedNotOptArg, name1=defaultNamedNotOptArg, name2=defaultNamedNotOptArg, objType=defaultNamedNotOptArg):
#		'General event fired on changes'


from win32com.client import CoClassBaseClass
class Application(CoClassBaseClass): # A CoClass
	# Defines the properties and members of the application object.
	CLSID = IID('{7866380D-9407-20D2-89D9-0020184077E1}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrApplication,
	]
	default_interface = IMGCVariantMgrApplication

class BPropModsUtility(CoClassBaseClass): # A CoClass
	# Defines the properties and members of the border property modifications utility object.
	CLSID = IID('{9664D362-EAD1-41A5-B465-7D71FE1527F1}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrBPropModsUtility,
	]
	default_interface = IMGCVariantMgrBPropModsUtility

class Block(CoClassBaseClass): # A CoClass
	# Defines the properties and members of the Block object.
	CLSID = IID('{463130F2-CF4B-49B8-9376-FD86C3AECA74}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrBlock,
	]
	default_interface = IMGCVariantMgrBlock

class BlockData(CoClassBaseClass): # A CoClass
	# Defines the properties and members of the ReusedBlock object.
	CLSID = IID('{1AEE4AD1-C054-4533-BF0E-1D6ED8BBD173}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrBlockData,
	]
	default_interface = IMGCVariantMgrBlockData

class BlockDataModification(CoClassBaseClass): # A CoClass
	# Defines the properties and members of the block data modification object.
	CLSID = IID('{6DA2DE93-5489-4171-BAD6-E836390A07C2}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrBlockDataModification,
	]
	default_interface = IMGCVariantMgrBlockDataModification

class BlockDataModificationFilter(CoClassBaseClass): # A CoClass
	# Defines the properties and members of the block data modification filter object.
	CLSID = IID('{0397654E-7091-4683-9FF8-D064B20281FB}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrBlockDataModificationFilter,
	]
	default_interface = IMGCVariantMgrBlockDataModificationFilter

class BlockDataModifications(CoClassBaseClass): # A CoClass
	# Defines a collection of bloc data modification objects.
	CLSID = IID('{19BDB78E-F30F-4F0E-A43E-E87E33F9995D}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrBlockDataModifications,
	]
	default_interface = IMGCVariantMgrBlockDataModifications

class Blocks(CoClassBaseClass): # A CoClass
	# Defines a collection of Block objects.
	CLSID = IID('{BE31CD71-78CF-4C67-A875-77F5E1297B47}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrBlocks,
	]
	default_interface = IMGCVariantMgrBlocks

class BorderPropModification(CoClassBaseClass): # A CoClass
	# Defines the properties and members of the border property modification object.
	CLSID = IID('{F7DCE892-A986-480A-9A79-26879868C4C2}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrBorderPropModification,
	]
	default_interface = IMGCVariantMgrBorderPropModification

class BorderPropModificationFilter(CoClassBaseClass): # A CoClass
	# Defines the properties and members of the border property modification filter object.
	CLSID = IID('{C1027159-081D-460B-9420-DC3A23ACE84D}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrBorderPropModificationFilter,
	]
	default_interface = IMGCVariantMgrBorderPropModificationFilter

class BorderPropModifications(CoClassBaseClass): # A CoClass
	# Defines a collection of Border property modification objects.
	CLSID = IID('{A1C6B0A5-F25F-41EC-BBB7-F4CE90E80F41}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrBorderPropModifications,
	]
	default_interface = IMGCVariantMgrBorderPropModifications

class Connectivity(CoClassBaseClass): # A CoClass
	# Defines the connectivity object.
	CLSID = IID('{82CD5AAA-9407-11D2-89D9-0020184077E1}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrConnectivity,
	]
	default_interface = IMGCVariantMgrConnectivity

# This CoClass is known by the name 'MGCVariantMgr.Document.119'
class Document(CoClassBaseClass): # A CoClass
	# Defines the properties and members of the document object.
	CLSID = IID('{8B45CE2D-6CF5-1014-857A-77B9EECCF0AC}')
	coclass_sources = [
		_IMGCVariantMgrDocumentEvents,
	]
	default_source = _IMGCVariantMgrDocumentEvents
	coclass_interfaces = [
		IMGCVariantMgrDocument,
	]
	default_interface = IMGCVariantMgrDocument

class Documents(CoClassBaseClass): # A CoClass
	# Defines a collection of document objects.
	CLSID = IID('{7866380E-9407-20D2-89D9-0020184077E1}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrDocuments,
	]
	default_interface = IMGCVariantMgrDocuments

class Editor(CoClassBaseClass): # A CoClass
	# Defines a class for the editor.
	CLSID = IID('{82CD5AAE-9407-11D2-89D9-0020184077E1}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrEditor,
	]
	default_interface = IMGCVariantMgrEditor

class Editors(CoClassBaseClass): # A CoClass
	# Defines a class for a collection of editors
	CLSID = IID('{FFA514B3-BAE3-4AF0-8611-E2FF01E3C9D1}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrEditors,
	]
	default_interface = IMGCVariantMgrEditors

class EquivPartsSettings(CoClassBaseClass): # A CoClass
	CLSID = IID('{82CD5AB5-9407-11D2-89D9-0020184077E1}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrEquivPartsSettings,
	]
	default_interface = IMGCVariantMgrEquivPartsSettings

class EquivalentBlock(CoClassBaseClass): # A CoClass
	# Defines the properties and members of the Equivalent Block object.
	CLSID = IID('{C8379667-6E7B-4C72-ADA1-EB298F1019EF}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrEquivalentBlock,
	]
	default_interface = IMGCVariantMgrEquivalentBlock

class EquivalentBlockGroup(CoClassBaseClass): # A CoClass
	# Defines the properties and members of the EquivalentBlockGroup object.
	CLSID = IID('{9E3B1A5B-EE91-4D46-A4C9-C08E93177145}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrEquivalentBlockGroup,
	]
	default_interface = IMGCVariantMgrEquivalentBlockGroup

class EquivalentBlockGroups(CoClassBaseClass): # A CoClass
	# Defines a collection of EquivalentBlockGroup objects.
	CLSID = IID('{710F3F51-7D50-4A3C-B171-E9F1BBBF5530}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrEquivalentBlockGroups,
	]
	default_interface = IMGCVariantMgrEquivalentBlockGroups

class EquivalentBlocks(CoClassBaseClass): # A CoClass
	# Defines a collection of EquivalentBlock objects.
	CLSID = IID('{3E00E7A9-47FF-4E25-B76E-BECE98E42007}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrEquivalentBlocks,
	]
	default_interface = IMGCVariantMgrEquivalentBlocks

class FMVFunction(CoClassBaseClass): # A CoClass
	# Defines the properties and members of the function object.
	CLSID = IID('{786637FB-9407-20D2-89D9-0020184077E1}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrFMVFunction,
	]
	default_interface = IMGCVariantMgrFMVFunction

class FMVFunctionAssignment(CoClassBaseClass): # A CoClass
	# Defines an FMV function assignment.
	CLSID = IID('{6E1379A7-5ADF-4FCE-AF36-168E470CF199}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrFMVFunctionAssignment,
	]
	default_interface = IMGCVariantMgrFMVFunctionAssignment

class FMVFunctionAssignments(CoClassBaseClass): # A CoClass
	# Defines a collection of FMV function assignments.
	CLSID = IID('{ED096F00-ED2B-468F-9E18-C01EF9CB2BEA}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrFMVFunctionAssignments,
	]
	default_interface = IMGCVariantMgrFMVFunctionAssignments

class FMVFunctionGroup(CoClassBaseClass): # A CoClass
	# Defines the properties and members of the FMV function group object.
	CLSID = IID('{5E7CEF6B-E5A9-452B-B757-7ABA3826CBD3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrFMVFunctionGroup,
	]
	default_interface = IMGCVariantMgrFMVFunctionGroup

class FMVFunctionGroups(CoClassBaseClass): # A CoClass
	# Defines a collection of group objects.
	CLSID = IID('{E30ED752-1FD3-4294-AE8D-E8C96944F104}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrFMVFunctionGroups,
	]
	default_interface = IMGCVariantMgrFMVFunctionGroups

class FMVFunctions(CoClassBaseClass): # A CoClass
	# Defines a collection of function objects.
	CLSID = IID('{786637FC-9407-20D2-89D9-0020184077E1}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrFMVFunctions,
	]
	default_interface = IMGCVariantMgrFMVFunctions

class FMVProperties(CoClassBaseClass): # A CoClass
	# Defines the properties and members of the FMV properties collection.
	CLSID = IID('{91CE081D-69DF-4940-B2E0-4F304D4E8E62}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrFMVProperties,
	]
	default_interface = IMGCVariantMgrFMVProperties

class FMVProperty(CoClassBaseClass): # A CoClass
	# Defines the properties and members of the FMV properties collection.
	CLSID = IID('{7B540F5C-2F96-4EEE-8894-F4970320B0D4}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrFMVProperty,
	]
	default_interface = IMGCVariantMgrFMVProperty

class Filters(CoClassBaseClass): # A CoClass
	# Defines the properties and members of the filters object.
	CLSID = IID('{09EDE838-98B4-4D93-A40C-3F43E642EAE1}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrFilters,
	]
	default_interface = IMGCVariantMgrFilters

class Groupings(CoClassBaseClass): # A CoClass
	# Defines the Groupings object.
	CLSID = IID('{82CD5AAB-9407-11D2-89D9-0020184077E1}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrGroupings,
	]
	default_interface = IMGCVariantMgrGroupings

class MessageMgr(CoClassBaseClass): # A CoClass
	# Defines the properties and members of the message manager object.
	CLSID = IID('{86B24400-555D-49A9-BD72-49260A34A59C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrMessageMgr,
	]
	default_interface = IMGCVariantMgrMessageMgr

class OutputGenerator(CoClassBaseClass): # A CoClass
	# Defines an output generator object.
	CLSID = IID('{82CD5AB6-9407-11D2-89D9-0020184077E1}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrOutputGenerator,
	]
	default_interface = IMGCVariantMgrOutputGenerator

class PModsUtility(CoClassBaseClass): # A CoClass
	# Defines the properties and members of the package modifications utility object.
	CLSID = IID('{5455892B-A0D3-498F-97D2-4C3F243B276E}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrPModsUtility,
	]
	default_interface = IMGCVariantMgrPModsUtility

class Package(CoClassBaseClass): # A CoClass
	# Defines the properties and members of the package object.
	CLSID = IID('{786637F5-9407-20D2-89D9-0020184077E1}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrPackage,
	]
	default_interface = IMGCVariantMgrPackage

class PackageFilter(CoClassBaseClass): # A CoClass
	# Defines the properties and members of the package filter object.
	CLSID = IID('{1CA65166-6233-45DE-A7F9-8327E263DBA5}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrPackageFilter,
	]
	default_interface = IMGCVariantMgrPackageFilter

class PackageModification(CoClassBaseClass): # A CoClass
	# Defines the properties and members of the package modification object.
	CLSID = IID('{786637FD-9407-20D2-89D9-0020184077E1}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrPackageModification,
	]
	default_interface = IMGCVariantMgrPackageModification

class PackageModificationFilter(CoClassBaseClass): # A CoClass
	# Defines the properties and members of the package modification filter object.
	CLSID = IID('{26D8C861-04AF-4273-9875-A8EF996FD14B}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrPackageModificationFilter,
	]
	default_interface = IMGCVariantMgrPackageModificationFilter

class PackageModifications(CoClassBaseClass): # A CoClass
	# Defines a collection of package modification objects.
	CLSID = IID('{786637FE-9407-20D2-89D9-0020184077E1}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrPackageModifications,
	]
	default_interface = IMGCVariantMgrPackageModifications

class Packages(CoClassBaseClass): # A CoClass
	# Defines a collection of package objects.
	CLSID = IID('{786637F6-9407-20D2-89D9-0020184077E1}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrPackages,
	]
	default_interface = IMGCVariantMgrPackages

class Parameter(CoClassBaseClass): # A CoClass
	CLSID = IID('{82CD5AB3-9407-11D2-89D9-0020184077E1}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrParameter,
	]
	default_interface = IMGCVariantMgrParameter

class Parameters(CoClassBaseClass): # A CoClass
	CLSID = IID('{82CD5AB4-9407-11D2-89D9-0020184077E1}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrParameters,
	]
	default_interface = IMGCVariantMgrParameters

class Reporter(CoClassBaseClass): # A CoClass
	# Defines the properties and members of the reporter object.
	CLSID = IID('{8B707D43-7C93-4D09-BE09-EE1B0498E345}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrReporter,
	]
	default_interface = IMGCVariantMgrReporter

class ReporterDataMatrix(CoClassBaseClass): # A CoClass
	# Exposes that data of the reporter data matrix.
	CLSID = IID('{1E60DA28-0E2A-4C52-9432-575F66713702}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrReporterDataMatrix,
	]
	default_interface = IMGCVariantMgrReporterDataMatrix

class ReporterSettings(CoClassBaseClass): # A CoClass
	# Defines the settings of the reporter object.
	CLSID = IID('{22912830-6A46-4B8E-998C-1812ABCEEC4E}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrReporterSettings,
	]
	default_interface = IMGCVariantMgrReporterSettings

class ReuseSettings(CoClassBaseClass): # A CoClass
	# Defines the properties and members of the reuse settings object.
	CLSID = IID('{2CA0D3A4-696A-4927-85D6-D0421E343252}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrReuseSettings,
	]
	default_interface = IMGCVariantMgrReuseSettings

class ReusedBlock(CoClassBaseClass): # A CoClass
	# Defines the properties and members of the ReusedBlock object.
	CLSID = IID('{82CD5AA8-9407-11D2-89D9-0020184077E1}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrReusedBlock,
	]
	default_interface = IMGCVariantMgrReusedBlock

class ReusedBlocks(CoClassBaseClass): # A CoClass
	# Defines a collection of ReusedBlock objects.
	CLSID = IID('{82CD5AA9-9407-11D2-89D9-0020184077E1}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrReusedBlocks,
	]
	default_interface = IMGCVariantMgrReusedBlocks

class SInfoRecsUtility(CoClassBaseClass): # A CoClass
	# Defines the properties and members of the symbol rec utility object.
	CLSID = IID('{B15661E9-0393-42DE-A5C4-4EA1C899AF71}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrSInfoRecsUtility,
	]
	default_interface = IMGCVariantMgrSInfoRecsUtility

class Settings(CoClassBaseClass): # A CoClass
	# Defines the properties and members of the settings object.
	CLSID = IID('{7866380B-9407-20D2-89D9-0020184077E1}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrSettings,
	]
	default_interface = IMGCVariantMgrSettings

class Statistics(CoClassBaseClass): # A CoClass
	# Defines the properties and members of the statistics object.
	CLSID = IID('{332154D8-A5F8-41A2-BE78-2841D50143F6}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrStatistics,
	]
	default_interface = IMGCVariantMgrStatistics

class Symbol(CoClassBaseClass): # A CoClass
	# Defines the properties and members of the symbol object.
	CLSID = IID('{786637F4-9407-20D2-89D9-0020184077E1}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrSymbol,
	]
	default_interface = IMGCVariantMgrSymbol

class SymbolFilter(CoClassBaseClass): # A CoClass
	# Defines the properties and members of the filters object..
	CLSID = IID('{3D8BA603-4843-461C-8153-D64FE1DF8380}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrSymbolFilter,
	]
	default_interface = IMGCVariantMgrSymbolFilter

class SymbolInfoRec(CoClassBaseClass): # A CoClass
	# Defines the properties and members of the symbol modification object.
	CLSID = IID('{68DE764E-F9B0-4B22-897E-CB0392034977}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrSymbolInfoRec,
	]
	default_interface = IMGCVariantMgrSymbolInfoRec

class SymbolInfoRecs(CoClassBaseClass): # A CoClass
	# Defines a collection of symbol modification objects.
	CLSID = IID('{B1A416FE-D9E6-4653-B05F-DE31BFE31772}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrSymbolInfoRecs,
	]
	default_interface = IMGCVariantMgrSymbolInfoRecs

class SymbolLocation(CoClassBaseClass): # A CoClass
	# Defines the properties and members of the symbol location object.
	CLSID = IID('{786637F3-9407-20D2-89D9-0020184077E1}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrSymbolLocation,
	]
	default_interface = IMGCVariantMgrSymbolLocation

class SymbolLocations(CoClassBaseClass): # A CoClass
	# Defines a collection of symbol locations objects.
	CLSID = IID('{786637F8-9407-20D2-89D9-0020184077E1}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrSymbolLocations,
	]
	default_interface = IMGCVariantMgrSymbolLocations

class Symbols(CoClassBaseClass): # A CoClass
	# Defines a collection of symbol objects.
	CLSID = IID('{786637F7-9407-20D2-89D9-0020184077E1}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrSymbols,
	]
	default_interface = IMGCVariantMgrSymbols

# This CoClass is known by the name 'MGCVariantMgr.UID.119'
class UID(CoClassBaseClass): # A CoClass
	# Defines the properties and members of the UID object.
	CLSID = IID('{8B45CF63-6CF5-1014-857A-77B9EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrUID,
	]
	default_interface = IMGCVariantMgrUID

class Utility(CoClassBaseClass): # A CoClass
	# Defines the properties and members of the utility object.
	CLSID = IID('{E08A46A8-C405-4073-ABB1-FB2B94A45C5F}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrUtility,
	]
	default_interface = IMGCVariantMgrUtility

class VMProperties(CoClassBaseClass): # A CoClass
	# Defines the properties collection.
	CLSID = IID('{1101A6F0-EA66-43DC-849E-906E36A0A734}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrProperties,
	]
	default_interface = IMGCVariantMgrProperties

class VMProperty(CoClassBaseClass): # A CoClass
	# Defines the property.
	CLSID = IID('{4BCB2183-E92C-4465-8652-62AE02E8672A}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrProperty,
	]
	default_interface = IMGCVariantMgrProperty

class Variant(CoClassBaseClass): # A CoClass
	# Defines the properties and members of the variant object.
	CLSID = IID('{78663802-9407-20D2-89D9-0020184077E1}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrVariant,
	]
	default_interface = IMGCVariantMgrVariant

class VariantAssignment(CoClassBaseClass): # A CoClass
	# Defines a variant assignment.
	CLSID = IID('{C1F669F9-84C7-480A-AF88-6A601077674A}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrVariantAssignment,
	]
	default_interface = IMGCVariantMgrVariantAssignment

class VariantAssignments(CoClassBaseClass): # A CoClass
	# Defines a collection of variant assignments.
	CLSID = IID('{5A99035D-F675-4DE5-9A15-9EB193E5B9FE}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrVariantAssignments,
	]
	default_interface = IMGCVariantMgrVariantAssignments

class VariantGroup(CoClassBaseClass): # A CoClass
	# Defines the properties and members of the variant group object.
	CLSID = IID('{F15DA467-46F8-449D-97B4-0C929B7DF4E8}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrVariantGroup,
	]
	default_interface = IMGCVariantMgrVariantGroup

class VariantGroups(CoClassBaseClass): # A CoClass
	# Defines a collection of group objects.
	CLSID = IID('{C65DD74F-E63D-4B2C-BF64-932CEA392102}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrVariantGroups,
	]
	default_interface = IMGCVariantMgrVariantGroups

class VariantInfoRec(CoClassBaseClass): # A CoClass
	# Defines the properties and members of the variant object.
	CLSID = IID('{17760C13-0FFB-4577-A56E-4A558EAD2B31}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrVariantInfoRec,
	]
	default_interface = IMGCVariantMgrVariantInfoRec

class VariantInfoRecs(CoClassBaseClass): # A CoClass
	# Defines a collection of variant modification objects.
	CLSID = IID('{4E6C1C8E-542F-4561-ADD3-ADA3C4E2B323}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrVariantInfoRecs,
	]
	default_interface = IMGCVariantMgrVariantInfoRecs

class VariantInfoRecsUtility(CoClassBaseClass): # A CoClass
	# Defines the properties and members of the variant rec utility object.
	CLSID = IID('{180960C2-CD47-4C0C-B446-8C558D69CA0E}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrVariantInfoRecsUtility,
	]
	default_interface = IMGCVariantMgrVariantInfoRecsUtility

class VariantMapping(CoClassBaseClass): # A CoClass
	# Defines the properties and members of the variant mapping object.
	CLSID = IID('{9424AF28-132F-4123-9124-395F25BD960B}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrVariantMapping,
	]
	default_interface = IMGCVariantMgrVariantMapping

class VariantMappings(CoClassBaseClass): # A CoClass
	# Defines a collection of variant mapping objects.
	CLSID = IID('{47653D5E-3982-45EE-8711-A5130875EB1C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrVariantMappings,
	]
	default_interface = IMGCVariantMgrVariantMappings

class Variants(CoClassBaseClass): # A CoClass
	# Defines a collection of variant objects.
	CLSID = IID('{78663803-9407-20D2-89D9-0020184077E1}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCVariantMgrVariants,
	]
	default_interface = IMGCVariantMgrVariants

class _DocumentEvents(CoClassBaseClass): # A CoClass
	# Defines the properties and members of the document object.
	CLSID = IID('{C1453F6A-07E7-42F1-B7A6-1F6B698798E6}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_IMGCVariantMgrBaseDummy,
	]
	default_interface = _IMGCVariantMgrBaseDummy

IMGCVariantMgrApplication_vtables_dispatch_ = 1
IMGCVariantMgrApplication_vtables_ = [
	(( 'OpenDocument' , 'jobPath' , 'revision' , 'clientType' , 'ppDocument' , 
			 ), 101, (101, (), [ (8, 1, None, None) , (8, 1, None, None) , (3, 49, '0', None) , (16393, 10, None, "IID('{78663807-9407-11D2-89D9-0020184077E1}')") , ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Documents' , 'ppDocsColl' , ), 103, (103, (), [ (16393, 10, None, "IID('{7866380E-9407-11D2-89D9-0020184077E1}')") , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrBPropModsUtility_vtables_dispatch_ = 1
IMGCVariantMgrBPropModsUtility_vtables_ = [
	(( 'PutBorderPropModification' , 'variantDefinition' , 'symbolDefinition' , 'prpName' , 'prpValue' , 
			 'ppObj' , ), 101, (101, (), [ (12, 1, None, None) , (12, 1, None, None) , (8, 1, None, None) , 
			 (8, 1, None, None) , (16393, 10, None, "IID('{22D9A8DA-F507-43FD-BA22-6DB8FEA436F2}')") , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'FindBorderPropModification' , 'prpName' , 'variantDef' , 'symbolDef' , 'ppObj' , 
			 ), 102, (102, (), [ (8, 1, None, None) , (12, 1, None, None) , (12, 1, None, None) , (16393, 10, None, "IID('{22D9A8DA-F507-43FD-BA22-6DB8FEA436F2}')") , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'BorderPropModifications' , 'filter' , 'ppBorderPropMods' , ), 103, (103, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{72982CC0-8617-400A-9772-5DF126EA582A}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'FindBorderPropModificationByUID' , 'userID' , 'objectID' , 'objectType' , 'ppObj' , 
			 ), 104, (104, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16393, 10, None, "IID('{22D9A8DA-F507-43FD-BA22-6DB8FEA436F2}')") , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrBaseBlock_vtables_dispatch_ = 1
IMGCVariantMgrBaseBlock_vtables_ = [
	(( 'BlockData' , 'ppObj' , ), 101, (101, (), [ (16393, 10, None, "IID('{7FE7FAB6-7B3B-46CB-970A-0010103AD7E3}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrBaseCollection_vtables_dispatch_ = 1
IMGCVariantMgrBaseCollection_vtables_ = [
	(( '_NewEnum' , 'retval' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 1 , )),
	(( 'Count' , 'pCount' , ), 30, (30, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Remove' , 'index' , ), 31, (31, (), [ (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Sort' , 'sortKey' , ), 32, (32, (), [ (12, 17, None, None) , ], 1 , 1 , 4 , 1 , 224 , (3, 0, None, None) , 64 , )),
]

IMGCVariantMgrBaseGroup_vtables_dispatch_ = 1
IMGCVariantMgrBaseGroup_vtables_ = [
	(( 'Description' , 'desc' , ), 101, (101, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Description' , 'desc' , ), 101, (101, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrBaseModNameObject_vtables_dispatch_ = 1
IMGCVariantMgrBaseModNameObject_vtables_ = [
	(( 'Name' , 'Name' , ), 30, (30, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'Name' , ), 30, (30, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrBaseModObject_vtables_dispatch_ = 1
IMGCVariantMgrBaseModObject_vtables_ = [
	(( 'ModificationCount' , 'pValue' , ), 20, (20, (), [ (2, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 64 , )),
	(( 'ModificationCount' , 'pValue' , ), 20, (20, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 64 , )),
	(( 'ModificationCountLock' , 'pValue' , ), 21, (21, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 64 , )),
	(( 'ModificationCountLock' , 'pValue' , ), 21, (21, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 64 , )),
	(( 'RootIF' , 'ppDocIF' , ), 22, (22, (), [ (16393, 10, None, "IID('{78663807-9407-11D2-89D9-0020184077E1}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 64 , )),
	(( 'IncModificationCount' , 'value' , 'newValue' , ), 23, (23, (), [ (2, 49, '1', None) , 
			 (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 64 , )),
	(( 'ModificationCountEx' , 'pValue' , ), 24, (24, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 64 , )),
	(( 'ModificationCountEx' , 'pValue' , ), 24, (24, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 64 , )),
]

IMGCVariantMgrBaseNameObject_vtables_dispatch_ = 1
IMGCVariantMgrBaseNameObject_vtables_ = [
	(( 'Name' , 'Name' , ), 35, (35, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'Name' , ), 35, (35, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrBaseObject_vtables_dispatch_ = 1
IMGCVariantMgrBaseObject_vtables_ = [
	(( 'Parent' , 'ppParent' , ), 1, (1, (), [ (9, 1, None, None) , ], 1 , 8 , 4 , 0 , 56 , (3, 0, None, None) , 64 , )),
	(( 'Parent' , 'ppParent' , ), 1, (1, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 64 , )),
	(( 'InternalIndex' , 'value' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 64 , )),
	(( 'IsValid' , 'pValue' , ), 3, (3, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 64 , )),
	(( 'SetInternalValue' , 'id' , 'parm1' , 'parm2' , 'parm3' , 
			 'result' , ), 4, (4, (), [ (8, 1, None, None) , (12, 17, None, None) , (12, 17, None, None) , 
			 (12, 17, None, None) , (16386, 10, None, None) , ], 1 , 1 , 4 , 3 , 88 , (3, 0, None, None) , 64 , )),
	(( 'AccessLock' , 'lockValue' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 64 , )),
	(( 'AccessLock' , 'lockValue' , ), 5, (5, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 64 , )),
	(( 'GetUID' , 'userID' , 'objectID' , 'objectType' , 'result' , 
			 ), 6, (6, (), [ (16403, 2, None, None) , (16403, 2, None, None) , (16403, 2, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 64 , )),
	(( 'SetUID' , 'userID' , 'objectID' , 'objectType' , 'result' , 
			 ), 7, (7, (), [ (19, 1, None, None) , (19, 1, None, None) , (19, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 64 , )),
	(( 'CompareUID' , 'userID' , 'objectID' , 'objectType' , 'result' , 
			 ), 9, (9, (), [ (19, 1, None, None) , (19, 1, None, None) , (19, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 64 , )),
]

IMGCVariantMgrBlock_vtables_dispatch_ = 1
IMGCVariantMgrBlock_vtables_ = [
	(( 'ContainsReusedBlocks' , 'traverseHierarchy' , 'result' , ), 102, (102, (), [ (11, 49, 'True', None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'DynamicReuseName' , 'value' , ), 103, (103, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'DynamicReuseName' , 'value' , ), 103, (103, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrBlockData_vtables_dispatch_ = 1
IMGCVariantMgrBlockData_vtables_ = [
	(( 'BlockSymbol' , 'symbolObj' , ), 101, (101, (), [ (16393, 10, None, "IID('{786637F4-9407-11D2-89D9-0020184077E1}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Symbols' , 'filter' , 'symbolsColl' , ), 102, (102, (), [ (12, 17, None, None) , 
			 (16393, 10, None, "IID('{786637F7-9407-11D2-89D9-0020184077E1}')") , ], 1 , 2 , 4 , 1 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Symbols' , 'filter' , 'symbolsColl' , ), 102, (102, (), [ (12, 17, None, None) , 
			 (16393, 10, None, "IID('{786637F7-9407-11D2-89D9-0020184077E1}')") , ], 1 , 2 , 4 , 1 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Packages' , 'filter' , 'packagesColl' , ), 103, (103, (), [ (12, 17, None, None) , 
			 (16393, 10, None, "IID('{786637F6-9407-11D2-89D9-0020184077E1}')") , ], 1 , 2 , 4 , 1 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Packages' , 'filter' , 'packagesColl' , ), 103, (103, (), [ (12, 17, None, None) , 
			 (16393, 10, None, "IID('{786637F6-9407-11D2-89D9-0020184077E1}')") , ], 1 , 2 , 4 , 1 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Blocks' , 'filter' , 'ppChildBlocks' , ), 104, (104, (), [ (12, 17, None, None) , 
			 (16393, 10, None, "IID('{F74277DE-9533-4D61-A84B-44D4A326B316}')") , ], 1 , 2 , 4 , 1 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Blocks' , 'filter' , 'ppChildBlocks' , ), 104, (104, (), [ (12, 17, None, None) , 
			 (16393, 10, None, "IID('{F74277DE-9533-4D61-A84B-44D4A326B316}')") , ], 1 , 2 , 4 , 1 , 240 , (3, 0, None, None) , 0 , )),
	(( 'ReusedBlocks' , 'filter' , 'ppChildReused' , ), 105, (105, (), [ (12, 17, None, None) , 
			 (16393, 10, None, "IID('{82CD5AA5-9407-11D2-89D9-0020184077E1}')") , ], 1 , 2 , 4 , 1 , 248 , (3, 0, None, None) , 0 , )),
	(( 'ReusedBlocks' , 'filter' , 'ppChildReused' , ), 105, (105, (), [ (12, 17, None, None) , 
			 (16393, 10, None, "IID('{82CD5AA5-9407-11D2-89D9-0020184077E1}')") , ], 1 , 2 , 4 , 1 , 248 , (3, 0, None, None) , 0 , )),
	(( 'IsReusedBlock' , 'result' , ), 106, (106, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'ContainsPackageModifications' , 'includeSubBlocks' , 'packModfilter' , 'result' , ), 107, (107, (), [ 
			 (11, 49, 'True', None) , (12, 17, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 1 , 264 , (3, 0, None, None) , 0 , )),
	(( 'ContainsReusedBlocks' , 'traverseHierarchy' , 'result' , ), 108, (108, (), [ (11, 49, 'True', None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'IsParentReusedBlock' , 'value' , ), 109, (109, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 64 , )),
	(( 'IsParentLogicalReusedBlock' , 'value' , ), 110, (110, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 64 , )),
	(( 'ContainsModifications' , 'variantDef' , 'value' , ), 111, (111, (), [ (12, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 296 , (3, 0, None, None) , 64 , )),
	(( 'AllPackages' , 'bIncludeRBs' , 'filter' , 'packagesColl' , ), 112, (112, (), [ 
			 (11, 1, None, None) , (12, 17, None, None) , (16393, 10, None, "IID('{786637F6-9407-11D2-89D9-0020184077E1}')") , ], 1 , 2 , 4 , 1 , 304 , (3, 0, None, None) , 64 , )),
	(( 'ParentDynamicReuseBlockName' , 'DRBName' , ), 113, (113, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'IsLogicalOnlyPartModificationAllowed' , 'value' , ), 114, (114, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 64 , )),
]

IMGCVariantMgrBlockDataModification_vtables_dispatch_ = 1
IMGCVariantMgrBlockDataModification_vtables_ = [
	(( 'BlockData' , 'ppBlockData' , ), 101, (101, (), [ (16393, 10, None, "IID('{7FE7FAB6-7B3B-46CB-970A-0010103AD7E3}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'ChangeOperation' , 'value' , ), 102, (102, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'ChangeOperation' , 'value' , ), 102, (102, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Variant' , 'ppVariant' , ), 103, (103, (), [ (16393, 10, None, "IID('{78663802-9407-11D2-89D9-0020184077E1}')") , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Variant' , 'ppVariant' , ), 103, (103, (), [ (9, 1, None, "IID('{78663802-9407-11D2-89D9-0020184077E1}')") , ], 1 , 8 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Delete' , 'result' , ), 104, (104, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'SubVariantName' , 'ppVariant' , ), 105, (105, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'SubVariantName' , 'ppVariant' , ), 105, (105, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'SetSubVariantUID' , 'userID' , 'objectID' , 'objectType' , 'result' , 
			 ), 106, (106, (), [ (19, 1, None, None) , (19, 1, None, None) , (19, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'GetSubVariantUID' , 'userID' , 'objectID' , 'objectType' , 'result' , 
			 ), 107, (107, (), [ (16403, 2, None, None) , (16403, 2, None, None) , (16403, 2, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'Merge' , 'result' , ), 108, (108, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'GetParentUID' , 'userID' , 'objectID' , 'objectType' , 'result' , 
			 ), 109, (109, (), [ (16403, 2, None, None) , (16403, 2, None, None) , (16403, 2, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 304 , (3, 0, None, None) , 64 , )),
]

IMGCVariantMgrBlockDataModificationFilter_vtables_dispatch_ = 1
IMGCVariantMgrBlockDataModificationFilter_vtables_ = [
	(( 'GetRootIF' , 'ppDocObj' , ), 100, (100, (), [ (16393, 2, None, "IID('{78663807-9407-11D2-89D9-0020184077E1}')") , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'BlockData' , ), 101, (101, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'ChangeOperation' , 'value' , ), 102, (102, (), [ (3, 49, '0', None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'ChangeOperation' , 'value' , ), 102, (102, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Variant' , ), 104, (104, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'VariantGroup' , ), 105, (105, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Initialize' , ), 106, (106, (), [ ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrBlockDataModifications_vtables_dispatch_ = 1
IMGCVariantMgrBlockDataModifications_vtables_ = [
	(( 'Item' , 'index' , 'ppPackMod' , ), 101, (101, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{5F556342-9E5E-4B96-9002-9B148BA114DD}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'pPackMod' , ), 102, (102, (), [ (9, 1, None, "IID('{5F556342-9E5E-4B96-9002-9B148BA114DD}')") , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrBlocks_vtables_dispatch_ = 1
IMGCVariantMgrBlocks_vtables_ = [
	(( 'Item' , 'index' , 'ppBlock' , ), 101, (101, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{E2CD1C5F-0EE9-4349-B08A-FA34A84CB2F1}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'pBlock' , ), 102, (102, (), [ (9, 1, None, "IID('{E2CD1C5F-0EE9-4349-B08A-FA34A84CB2F1}')") , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrBorderPropModification_vtables_dispatch_ = 1
IMGCVariantMgrBorderPropModification_vtables_ = [
	(( 'value' , 'value' , ), 101, (101, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'value' , 'value' , ), 101, (101, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Symbol' , 'ppSymbol' , ), 102, (102, (), [ (16393, 10, None, "IID('{786637F4-9407-11D2-89D9-0020184077E1}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Symbol' , 'ppSymbol' , ), 102, (102, (), [ (9, 1, None, "IID('{786637F4-9407-11D2-89D9-0020184077E1}')") , ], 1 , 8 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Variant' , 'ppVariant' , ), 103, (103, (), [ (16393, 10, None, "IID('{78663802-9407-11D2-89D9-0020184077E1}')") , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Variant' , 'ppVariant' , ), 103, (103, (), [ (9, 1, None, "IID('{78663802-9407-11D2-89D9-0020184077E1}')") , ], 1 , 8 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Delete' , 'result' , ), 104, (104, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrBorderPropModificationFilter_vtables_dispatch_ = 1
IMGCVariantMgrBorderPropModificationFilter_vtables_ = [
	(( 'GetRootIF' , 'ppDocObj' , ), 100, (100, (), [ (16393, 2, None, "IID('{78663807-9407-11D2-89D9-0020184077E1}')") , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'value' , ), 102, (102, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'value' , ), 102, (102, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Variant' , ), 104, (104, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Symbol' , ), 105, (105, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Initialize' , ), 106, (106, (), [ ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrBorderPropModifications_vtables_dispatch_ = 1
IMGCVariantMgrBorderPropModifications_vtables_ = [
	(( 'Item' , 'index' , 'ppPackMod' , ), 101, (101, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{22D9A8DA-F507-43FD-BA22-6DB8FEA436F2}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'pPackMod' , ), 102, (102, (), [ (9, 1, None, "IID('{22D9A8DA-F507-43FD-BA22-6DB8FEA436F2}')") , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrConnectivity_vtables_dispatch_ = 1
IMGCVariantMgrConnectivity_vtables_ = [
	(( 'Symbols' , 'filter' , 'ppSymbColl' , ), 101, (101, (), [ (12, 17, None, None) , 
			 (16393, 10, None, "IID('{786637F7-9407-11D2-89D9-0020184077E1}')") , ], 1 , 2 , 4 , 1 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Symbols' , 'filter' , 'ppSymbColl' , ), 101, (101, (), [ (12, 17, None, None) , 
			 (16393, 10, None, "IID('{786637F7-9407-11D2-89D9-0020184077E1}')") , ], 1 , 2 , 4 , 1 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Packages' , 'filter' , 'ppPackColl' , ), 102, (102, (), [ (12, 17, None, None) , 
			 (16393, 10, None, "IID('{786637F6-9407-11D2-89D9-0020184077E1}')") , ], 1 , 2 , 4 , 1 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Packages' , 'filter' , 'ppPackColl' , ), 102, (102, (), [ (12, 17, None, None) , 
			 (16393, 10, None, "IID('{786637F6-9407-11D2-89D9-0020184077E1}')") , ], 1 , 2 , 4 , 1 , 144 , (3, 0, None, None) , 0 , )),
	(( 'ReusedBlocks' , 'filter' , 'ppBlocksColl' , ), 103, (103, (), [ (12, 17, None, None) , 
			 (16393, 10, None, "IID('{82CD5AA5-9407-11D2-89D9-0020184077E1}')") , ], 1 , 2 , 4 , 1 , 152 , (3, 0, None, None) , 0 , )),
	(( 'ReusedBlocks' , 'filter' , 'ppBlocksColl' , ), 103, (103, (), [ (12, 17, None, None) , 
			 (16393, 10, None, "IID('{82CD5AA5-9407-11D2-89D9-0020184077E1}')") , ], 1 , 2 , 4 , 1 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Blocks' , 'filter' , 'ppBlocksColl' , ), 104, (104, (), [ (12, 17, None, None) , 
			 (16393, 10, None, "IID('{F74277DE-9533-4D61-A84B-44D4A326B316}')") , ], 1 , 2 , 4 , 1 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Blocks' , 'filter' , 'ppBlocksColl' , ), 104, (104, (), [ (12, 17, None, None) , 
			 (16393, 10, None, "IID('{F74277DE-9533-4D61-A84B-44D4A326B316}')") , ], 1 , 2 , 4 , 1 , 160 , (3, 0, None, None) , 0 , )),
	(( 'SymbolLocations' , 'filter' , 'ppSymbLocColl' , ), 105, (105, (), [ (12, 17, None, None) , 
			 (16393, 10, None, "IID('{786637F8-9407-11D2-89D9-0020184077E1}')") , ], 1 , 2 , 4 , 1 , 168 , (3, 0, None, None) , 0 , )),
	(( 'SymbolLocations' , 'filter' , 'ppSymbLocColl' , ), 105, (105, (), [ (12, 17, None, None) , 
			 (16393, 10, None, "IID('{786637F8-9407-11D2-89D9-0020184077E1}')") , ], 1 , 2 , 4 , 1 , 168 , (3, 0, None, None) , 0 , )),
	(( 'EquivalentBlockGroups' , 'filter' , 'ppObj' , ), 106, (106, (), [ (12, 17, None, None) , 
			 (16393, 10, None, "IID('{98301621-82F9-4458-996F-46739708B82C}')") , ], 1 , 2 , 4 , 1 , 176 , (3, 0, None, None) , 64 , )),
	(( 'EquivalentBlockGroups' , 'filter' , 'ppObj' , ), 106, (106, (), [ (12, 17, None, None) , 
			 (16393, 10, None, "IID('{98301621-82F9-4458-996F-46739708B82C}')") , ], 1 , 2 , 4 , 1 , 176 , (3, 0, None, None) , 64 , )),
	(( 'Load' , 'fileName' , 'connSource' , 'logFileName' , 'addiParm' , 
			 'result' , ), 107, (107, (), [ (8, 1, None, None) , (3, 1, None, None) , (8, 1, None, None) , 
			 (8, 49, "''", None) , (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 184 , (3, 32, None, None) , 64 , )),
	(( 'ConnectivitySourceType' , 'connSource' , ), 108, (108, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 64 , )),
	(( 'ConnectivitySource' , 'value' , ), 109, (109, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 64 , )),
	(( 'RootBlock' , 'ppBlockObj' , ), 110, (110, (), [ (16393, 10, None, "IID('{E2CD1C5F-0EE9-4349-B08A-FA34A84CB2F1}')") , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 64 , )),
	(( 'ConnectivitySourceDate' , 'value' , ), 111, (111, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 64 , )),
	(( 'FindPackage' , 'packName' , 'ppObj' , ), 112, (112, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{786637F5-9407-11D2-89D9-0020184077E1}')") , ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'SnapshotName' , 'value' , ), 113, (113, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 64 , )),
	(( 'SnapshotName' , 'value' , ), 113, (113, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 64 , )),
	(( 'FindSymbolByUID' , 'userID' , 'objectID' , 'objectType' , 'ppObj' , 
			 ), 114, (114, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16393, 10, None, "IID('{786637F4-9407-11D2-89D9-0020184077E1}')") , ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 64 , )),
	(( 'AppName' , 'value' , ), 115, (115, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 64 , )),
	(( 'AppName' , 'value' , ), 115, (115, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 264 , (3, 0, None, None) , 64 , )),
	(( 'ReLoadPropertiesForBOM' , 'xmlConfigurationFile' , 'result' , ), 116, (116, (), [ (8, 1, None, None) , 
			 (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 272 , (3, 0, None, None) , 64 , )),
	(( 'FindPackageByUID' , 'userID' , 'objectID' , 'objectType' , 'ppObj' , 
			 ), 117, (117, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16393, 10, None, "IID('{786637F5-9407-11D2-89D9-0020184077E1}')") , ], 1 , 1 , 4 , 0 , 280 , (3, 0, None, None) , 64 , )),
	(( 'FindSymbol' , 'symbolNameAndPath' , 'ppObj' , ), 118, (118, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{786637F4-9407-11D2-89D9-0020184077E1}')") , ], 1 , 1 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'FindPackageBySID' , 'SID' , 'ppObj' , ), 119, (119, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{786637F5-9407-11D2-89D9-0020184077E1}')") , ], 1 , 1 , 4 , 0 , 296 , (3, 0, None, None) , 64 , )),
	(( 'CheckNotMarkedPackages' , 'result' , ), 120, (120, (), [ (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 304 , (3, 0, None, None) , 64 , )),
	(( 'GetSymbolBorderProperties' , 'pSymbol' , 'commonProp' , 'borderProps' , 'num' , 
			 'result' , ), 121, (121, (), [ (9, 1, None, "IID('{786637F4-9407-11D2-89D9-0020184077E1}')") , (12, 1, None, None) , (16396, 2, None, None) , 
			 (16387, 2, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'GetUserDefinedPropertiesForBOM' , 'inProps' , 'propInfo' , 'result' , ), 122, (122, (), [ 
			 (8, 1, None, None) , (16396, 2, None, None) , (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrDocument_vtables_dispatch_ = 1
IMGCVariantMgrDocument_vtables_ = [
	(( 'Description' , 'desc' , ), 101, (101, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Description' , 'desc' , ), 101, (101, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'FMVFunctions' , 'filter' , 'ppFuncColl' , ), 103, (103, (), [ (12, 17, None, None) , 
			 (16393, 10, None, "IID('{786637FC-9407-11D2-89D9-0020184077E1}')") , ], 1 , 2 , 4 , 1 , 232 , (3, 0, None, None) , 0 , )),
	(( 'FMVFunctions' , 'filter' , 'ppFuncColl' , ), 103, (103, (), [ (12, 17, None, None) , 
			 (16393, 10, None, "IID('{786637FC-9407-11D2-89D9-0020184077E1}')") , ], 1 , 2 , 4 , 1 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Variants' , 'filter' , 'ppVariantColl' , ), 104, (104, (), [ (12, 17, None, None) , 
			 (16393, 10, None, "IID('{78663803-9407-11D2-89D9-0020184077E1}')") , ], 1 , 2 , 4 , 1 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Variants' , 'filter' , 'ppVariantColl' , ), 104, (104, (), [ (12, 17, None, None) , 
			 (16393, 10, None, "IID('{78663803-9407-11D2-89D9-0020184077E1}')") , ], 1 , 2 , 4 , 1 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Connectivity' , 'ppConnectivity' , ), 105, (105, (), [ (16393, 10, None, "IID('{82CD5AA6-9407-11D2-89D9-0020184077E1}')") , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Groupings' , 'ppGroupings' , ), 106, (106, (), [ (16393, 10, None, "IID('{82CD5AA7-9407-11D2-89D9-0020184077E1}')") , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Settings' , 'ppSettings' , ), 109, (109, (), [ (16393, 10, None, "IID('{7866380B-9407-11D2-89D9-0020184077E1}')") , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'Close' , 'result' , ), 111, (111, (), [ (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'LoadTestData' , 'dataSet' , ), 113, (113, (), [ (2, 1, None, None) , ], 1 , 1 , 4 , 0 , 280 , (3, 0, None, None) , 64 , )),
	(( 'Load' , 'dataSource' , 'logFile' , 'variantsDBType' , 'result' , 
			 ), 116, (116, (), [ (8, 1, None, None) , (8, 1, None, None) , (3, 49, '2', None) , (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 288 , (3, 0, None, None) , 64 , )),
	(( 'FindVariant' , 'Name' , 'ppObj' , ), 117, (117, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{78663802-9407-11D2-89D9-0020184077E1}')") , ], 1 , 1 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'TransactionStart' , 'transActionID' , ), 120, (120, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 304 , (3, 0, None, None) , 64 , )),
	(( 'TransactionEnd' , 'transActionID' , 'commitChanges' , 'result' , ), 121, (121, (), [ 
			 (3, 1, None, None) , (11, 49, 'True', None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 312 , (3, 0, None, None) , 64 , )),
	(( 'PutVariant' , 'variantName' , 'variantNumber' , 'variantDescription' , 'sourceForContents' , 
			 'ppObj' , ), 122, (122, (), [ (8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , 
			 (12, 17, None, None) , (16393, 10, None, "IID('{78663802-9407-11D2-89D9-0020184077E1}')") , ], 1 , 1 , 4 , 1 , 320 , (3, 0, None, None) , 0 , )),
	(( 'Utility' , 'ppObj' , ), 125, (125, (), [ (16393, 10, None, "IID('{EE5CB44B-13CF-480C-B096-5A2D731A9535}')") , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 64 , )),
	(( 'VariantsDBFilename' , 'fullPath' , ), 126, (126, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 64 , )),
	(( 'variantsDBType' , 'value' , ), 127, (127, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 64 , )),
	(( 'Save' , 'result' , ), 128, (128, (), [ (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 352 , (3, 0, None, None) , 64 , )),
	(( 'SaveAs' , 'fileName' , 'dbType' , 'result' , ), 129, (129, (), [ 
			 (8, 1, None, None) , (3, 49, '1', None) , (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 360 , (3, 0, None, None) , 64 , )),
	(( 'ReusedBlocksLibTopDir' , 'value' , ), 130, (130, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 64 , )),
	(( 'ReusedBlocksLibTopDir' , 'value' , ), 130, (130, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 376 , (3, 0, None, None) , 64 , )),
	(( 'LoadSelective' , 'dataSource' , 'logFile' , 'loadSelection' , 'variantsDBType' , 
			 'result' , ), 131, (131, (), [ (8, 1, None, None) , (8, 1, None, None) , (3, 49, '268435455', None) , 
			 (3, 49, '2', None) , (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 384 , (3, 0, None, None) , 64 , )),
	(( 'Reporter' , 'ppReporter' , ), 132, (132, (), [ (16393, 10, None, "IID('{017BAF92-95BB-4AD2-BCF6-43DC7A60BAA8}')") , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'IsReusedBlock' , 'value' , ), 133, (133, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 400 , (3, 0, None, None) , 64 , )),
	(( 'PutFMVFunction' , 'functionName' , 'functionNumber' , 'functionDescription' , 'sourceForContents' , 
			 'ppObj' , ), 135, (135, (), [ (8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , 
			 (12, 17, None, None) , (16393, 10, None, "IID('{786637FB-9407-11D2-89D9-0020184077E1}')") , ], 1 , 1 , 4 , 1 , 408 , (3, 0, None, None) , 0 , )),
	(( 'FindFMVFunction' , 'Name' , 'ppObj' , ), 136, (136, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{786637FB-9407-11D2-89D9-0020184077E1}')") , ], 1 , 1 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'MessageMgr' , 'ppMessMgr' , ), 137, (137, (), [ (16393, 10, None, "IID('{F22A8EE1-16C5-47E6-A722-C17868D6B486}')") , ], 1 , 2 , 4 , 0 , 424 , (3, 0, None, None) , 64 , )),
	(( 'CreateDxdViewDefFile' , 'outFileName' , 'pObj' , 'symbDispMode' , 'unplaceColorRed' , 
			 'unplaceColorGreen' , 'unplaceColorBlue' , 'pnumInfoData' , 'rplStrings' , 'borderProps' , 
			 'result' , ), 138, (138, (), [ (8, 1, None, None) , (9, 1, None, "IID('{78663802-9407-11D2-89D9-0020184077E1}')") , (3, 1, None, None) , 
			 (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , 
			 (12, 1, None, None) , (16386, 1, None, None) , ], 1 , 1 , 4 , 0 , 432 , (3, 0, None, None) , 64 , )),
	(( 'LoadForPCBDesign' , 'pcbFilePath' , 'logFile' , 'useLayout_Temp' , 'result' , 
			 ), 139, (139, (), [ (8, 1, None, None) , (8, 1, None, None) , (11, 1, None, None) , (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 440 , (3, 0, None, None) , 64 , )),
	(( 'AcquireSessionWriteMode' , 'requestForRelease' , 'currentEditUser' , 'returnStatusInfo' , 'succeeded' , 
			 ), 140, (140, (), [ (11, 1, None, None) , (16392, 2, None, None) , (16392, 2, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 448 , (3, 0, None, None) , 64 , )),
	(( 'ReleaseSessionWriteMode' , 'notifyOtherUsers' , 'succeeded' , ), 141, (141, (), [ (11, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 456 , (3, 0, None, None) , 64 , )),
	(( 'GetSessionsStatus' , 'numSessions' , 'editingUserName' , ), 142, (142, (), [ (16387, 2, None, None) , 
			 (16392, 2, None, None) , ], 1 , 1 , 4 , 0 , 464 , (3, 0, None, None) , 64 , )),
	(( 'UserName' , 'UserName' , ), 143, (143, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 472 , (3, 0, None, None) , 64 , )),
	(( 'UserName' , 'UserName' , ), 143, (143, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 480 , (3, 0, None, None) , 64 , )),
	(( 'GetPlacedVariants' , 'packName' , 'cleanupNames' , 'allPlacedReturnsEmpty' , 'arrayOfVariants' , 
			 'numVariants' , 'result' , ), 144, (144, (), [ (8, 1, None, None) , (11, 1, None, None) , 
			 (11, 1, None, None) , (16396, 2, None, None) , (16387, 2, None, None) , (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 488 , (3, 0, None, None) , 64 , )),
	(( 'TimeStamp' , 'tsType' , 'value' , ), 145, (145, (), [ (3, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 496 , (3, 0, None, None) , 64 , )),
	(( 'TimeStamp' , 'tsType' , 'value' , ), 145, (145, (), [ (3, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 504 , (3, 0, None, None) , 64 , )),
	(( 'TimeStampString' , 'tsType' , 'value' , ), 146, (146, (), [ (3, 1, None, None) , 
			 (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 512 , (3, 0, None, None) , 64 , )),
	(( 'ICDBOfflineMode' , 'value' , ), 147, (147, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 520 , (3, 0, None, None) , 64 , )),
	(( 'ICDBOfflineMode' , 'value' , ), 147, (147, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 528 , (3, 0, None, None) , 64 , )),
	(( 'ReleaseSession' , 'succeeded' , ), 148, (148, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 536 , (3, 0, None, None) , 64 , )),
	(( 'SaveVariantsInfoFile' , 'fileName' , 'result' , ), 149, (149, (), [ (8, 1, None, None) , 
			 (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 544 , (3, 0, None, None) , 64 , )),
	(( 'PModsUtility' , 'ppObj' , ), 150, (150, (), [ (16393, 10, None, "IID('{D391142F-058C-49E2-85CF-30DA3D2886BA}')") , ], 1 , 2 , 4 , 0 , 552 , (3, 0, None, None) , 0 , )),
	(( 'SInfoRecsUtility' , 'ppObj' , ), 151, (151, (), [ (16393, 10, None, "IID('{7D8CEF26-776A-40B2-A99C-C6B2358E0C60}')") , ], 1 , 2 , 4 , 0 , 560 , (3, 0, None, None) , 0 , )),
	(( 'FindVariantByUID' , 'userID' , 'objectID' , 'objectType' , 'ppObj' , 
			 ), 152, (152, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16393, 10, None, "IID('{78663802-9407-11D2-89D9-0020184077E1}')") , ], 1 , 1 , 4 , 0 , 568 , (3, 0, None, None) , 64 , )),
	(( 'FindFMVFunctionByUID' , 'userID' , 'objectID' , 'objectType' , 'ppObj' , 
			 ), 153, (153, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16393, 10, None, "IID('{786637FB-9407-11D2-89D9-0020184077E1}')") , ], 1 , 1 , 4 , 0 , 576 , (3, 0, None, None) , 64 , )),
	(( 'RootBlockName' , 'Name' , ), 154, (154, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 584 , (3, 0, None, None) , 64 , )),
	(( 'RootBlockName' , 'Name' , ), 154, (154, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 592 , (3, 0, None, None) , 64 , )),
	(( 'TemporaryDatabase' , 'value' , ), 155, (155, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 600 , (3, 0, None, None) , 64 , )),
	(( 'TemporaryDatabase' , 'value' , ), 155, (155, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 608 , (3, 0, None, None) , 64 , )),
	(( 'IsRepackagingNeeded' , 'value' , ), 156, (156, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 616 , (3, 0, None, None) , 0 , )),
	(( 'FXEGenerateSilkscreenFlag' , 'value' , ), 157, (157, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 624 , (3, 0, None, None) , 64 , )),
	(( 'FXEGenerateSilkscreenFlag' , 'value' , ), 157, (157, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 632 , (3, 0, None, None) , 64 , )),
	(( 'CreateDxdFunViewDefFile' , 'outFileName' , 'pObj' , 'symbDispMode' , 'unplaceColorRed' , 
			 'unplaceColorGreen' , 'unplaceColorBlue' , 'pnumInfoData' , 'rplStrings' , 'result' , 
			 ), 158, (158, (), [ (8, 1, None, None) , (9, 1, None, "IID('{786637FB-9407-11D2-89D9-0020184077E1}')") , (3, 1, None, None) , (3, 1, None, None) , 
			 (3, 1, None, None) , (3, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , (16386, 1, None, None) , ], 1 , 1 , 4 , 0 , 640 , (3, 0, None, None) , 64 , )),
	(( 'GetPathIndex' , 'pagename' , 'value' , ), 159, (159, (), [ (8, 1, None, None) , 
			 (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 648 , (3, 0, None, None) , 64 , )),
	(( 'LauncherAddress' , 'address' , ), 160, (160, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 656 , (3, 0, None, None) , 64 , )),
	(( 'LauncherAddress' , 'address' , ), 160, (160, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 664 , (3, 0, None, None) , 64 , )),
	(( 'FlowID' , 'flow' , ), 161, (161, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 672 , (3, 0, None, None) , 64 , )),
	(( 'FlowID' , 'flow' , ), 161, (161, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 680 , (3, 0, None, None) , 64 , )),
	(( 'VariantInfoRecsUtility' , 'ppObj' , ), 162, (162, (), [ (16393, 10, None, "IID('{138F998B-642F-436E-BEA2-986E1B29A353}')") , ], 1 , 2 , 4 , 0 , 688 , (3, 0, None, None) , 0 , )),
	(( 'AttributePartName' , 'Name' , ), 163, (163, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 696 , (3, 0, None, None) , 64 , )),
	(( 'AttributePartName' , 'Name' , ), 163, (163, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 704 , (3, 0, None, None) , 64 , )),
	(( 'RefDesName' , 'Name' , ), 164, (164, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 712 , (3, 0, None, None) , 64 , )),
	(( 'RefDesName' , 'Name' , ), 164, (164, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 720 , (3, 0, None, None) , 64 , )),
	(( 'SetReuseBlockParams' , 'reuseBlockName' , 'iCDBDir' , 'snapshot' , 'RootBlock' , 
			 ), 165, (165, (), [ (8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 728 , (3, 0, None, None) , 64 , )),
	(( 'ReadOnly' , 'ro' , ), 166, (166, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 736 , (3, 0, None, None) , 64 , )),
	(( 'PutPackage' , 'ppObj' , ), 167, (167, (), [ (16393, 10, None, "IID('{786637F5-9407-11D2-89D9-0020184077E1}')") , ], 1 , 1 , 4 , 0 , 744 , (3, 0, None, None) , 0 , )),
	(( 'PutSymbol' , 'ppObj' , ), 168, (168, (), [ (16393, 10, None, "IID('{786637F4-9407-11D2-89D9-0020184077E1}')") , ], 1 , 1 , 4 , 0 , 752 , (3, 0, None, None) , 0 , )),
	(( 'RunEventObserver' , 'bValue' , ), 169, (169, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 760 , (3, 0, None, None) , 64 , )),
	(( 'RunEventObserver' , 'bValue' , ), 169, (169, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 768 , (3, 0, None, None) , 64 , )),
	(( 'DumpDB' , 'Path' , 'result' , ), 170, (170, (), [ (8, 1, None, None) , 
			 (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 776 , (3, 0, None, None) , 64 , )),
	(( 'iCDBClientName' , 'clientName' , ), 171, (171, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 784 , (3, 0, None, None) , 64 , )),
	(( 'IsICDBNewFormat' , 'bValue' , ), 172, (172, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 792 , (3, 0, None, None) , 64 , )),
	(( 'IsUpgradeFwdBackAnnoNeeded' , 'otherSnapshot' , 'bValue' , ), 173, (173, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 800 , (3, 0, None, None) , 64 , )),
	(( 'BPropModsUtility' , 'ppObj' , ), 174, (174, (), [ (16393, 10, None, "IID('{BC1CC3A2-E4A4-4A3D-B400-50F80D7D8A39}')") , ], 1 , 2 , 4 , 0 , 808 , (3, 0, None, None) , 0 , )),
	(( 'ApplyBorderPropModsToAllSymbols' , 'pVariant' , ), 175, (175, (), [ (9, 1, None, "IID('{78663802-9407-11D2-89D9-0020184077E1}')") , ], 1 , 1 , 4 , 0 , 816 , (3, 0, None, None) , 64 , )),
	(( 'DeleteBorderPropModsFromAllSymbols' , 'propName' , 'pVariant' , ), 176, (176, (), [ (8, 1, None, None) , 
			 (9, 1, None, "IID('{78663802-9407-11D2-89D9-0020184077E1}')") , ], 1 , 1 , 4 , 0 , 824 , (3, 0, None, None) , 64 , )),
	(( 'IsUpdateRBPending' , 'pObj' , 'bValue' , ), 177, (177, (), [ (9, 1, None, "IID('{82CD5AA4-9407-11D2-89D9-0020184077E1}')") , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 832 , (3, 0, None, None) , 64 , )),
	(( 'ProjectFile' , 'ProjectFileName' , ), 178, (178, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 840 , (3, 0, None, None) , 64 , )),
	(( 'ProjectFile' , 'ProjectFileName' , ), 178, (178, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 848 , (3, 0, None, None) , 64 , )),
	(( 'CloseICDB' , 'result' , ), 179, (179, (), [ (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 856 , (3, 0, None, None) , 0 , )),
	(( 'ShowSymbolReplacements' , 'bValue' , ), 180, (180, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 864 , (3, 0, None, None) , 0 , )),
	(( 'ShowSymbolReplacements' , 'bValue' , ), 180, (180, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 872 , (3, 0, None, None) , 0 , )),
	(( 'GetErrorString' , 'Type' , 'errorString' , ), 181, (181, (), [ (3, 1, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 880 , (3, 0, None, None) , 64 , )),
	(( 'CentralLibProps' , 'CentLibPropsList' , ), 182, (182, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 888 , (3, 0, None, None) , 64 , )),
	(( 'CentralLibProps' , 'CentLibPropsList' , ), 182, (182, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 896 , (3, 0, None, None) , 64 , )),
	(( 'UpdateCentralLibProps' , 'CentLibPropsList' , 'result' , ), 183, (183, (), [ (8, 1, None, None) , 
			 (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 904 , (3, 0, None, None) , 64 , )),
	(( 'NotesLayers' , 'NotesLayers' , ), 184, (184, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 912 , (3, 0, None, None) , 0 , )),
	(( 'AliasPartNumberAttribute' , 'aliasPN' , ), 185, (185, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 920 , (3, 0, None, None) , 64 , )),
	(( 'AliasPartNumberAttribute' , 'aliasPN' , ), 185, (185, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 928 , (3, 0, None, None) , 64 , )),
	(( 'SaveNotesLayers' , 'result' , ), 186, (186, (), [ (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 936 , (3, 0, None, None) , 64 , )),
]

IMGCVariantMgrDocuments_vtables_dispatch_ = 1
IMGCVariantMgrDocuments_vtables_ = [
	(( 'Item' , 'index' , 'ppDocument' , ), 101, (101, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{78663807-9407-11D2-89D9-0020184077E1}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'pVariant' , ), 102, (102, (), [ (9, 1, None, "IID('{78663807-9407-11D2-89D9-0020184077E1}')") , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrEditor_vtables_dispatch_ = 1
IMGCVariantMgrEditor_vtables_ = [
	(( 'EditorApplication' , 'ppEditorApp' , ), 101, (101, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrEditors_vtables_dispatch_ = 1
IMGCVariantMgrEditors_vtables_ = [
	(( 'Item' , 'index' , 'ppEditor' , ), 101, (101, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{82CD5AAD-9407-11D2-89D9-0020184077E1}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'CreateInstance' , 'pEditorHost' , 'ppEditor' , ), 102, (102, (), [ (9, 1, None, None) , 
			 (16393, 10, None, "IID('{82CD5AAD-9407-11D2-89D9-0020184077E1}')") , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrEquivPartsSettings_vtables_dispatch_ = 1
IMGCVariantMgrEquivPartsSettings_vtables_ = [
	(( 'Parameters' , 'parametersColl' , ), 101, (101, (), [ (16393, 10, None, "IID('{82CD5AB0-9407-11D2-89D9-0020184077E1}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrEquivalentBlock_vtables_dispatch_ = 1
IMGCVariantMgrEquivalentBlock_vtables_ = [
	(( 'IsTemplateBlock' , 'result' , ), 100, (100, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Block' , 'ppObj' , ), 101, (101, (), [ (16393, 10, None, "IID('{E2CD1C5F-0EE9-4349-B08A-FA34A84CB2F1}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'KeepInSyncWithTemplate' , 'flagValue' , ), 102, (102, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'KeepInSyncWithTemplate' , 'flagValue' , ), 102, (102, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrEquivalentBlockGroup_vtables_dispatch_ = 1
IMGCVariantMgrEquivalentBlockGroup_vtables_ = [
	(( 'SchematicName' , 'Name' , ), 100, (100, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'TemplateBlock' , 'ppObj' , ), 101, (101, (), [ (9, 1, None, "IID('{AA3E0FAD-2AD6-4FE3-93CC-98A117DC9F0D}')") , ], 1 , 8 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'TemplateBlock' , 'ppObj' , ), 101, (101, (), [ (16393, 10, None, "IID('{AA3E0FAD-2AD6-4FE3-93CC-98A117DC9F0D}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'EquivalentBlocks' , 'filter' , 'ppObj' , ), 102, (102, (), [ (12, 17, None, None) , 
			 (16393, 10, None, "IID('{CD2C5AF6-5000-4C95-9879-2F7FB2BA85DD}')") , ], 1 , 2 , 4 , 1 , 160 , (3, 0, None, None) , 0 , )),
	(( 'EquivalentBlocks' , 'filter' , 'ppObj' , ), 102, (102, (), [ (12, 17, None, None) , 
			 (16393, 10, None, "IID('{CD2C5AF6-5000-4C95-9879-2F7FB2BA85DD}')") , ], 1 , 2 , 4 , 1 , 160 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrEquivalentBlockGroups_vtables_dispatch_ = 1
IMGCVariantMgrEquivalentBlockGroups_vtables_ = [
	(( 'Item' , 'index' , 'ppObj' , ), 101, (101, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{4FC18EAE-75C9-4A49-9E38-20ADD79456B5}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrEquivalentBlocks_vtables_dispatch_ = 1
IMGCVariantMgrEquivalentBlocks_vtables_ = [
	(( 'Item' , 'index' , 'ppObj' , ), 101, (101, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{AA3E0FAD-2AD6-4FE3-93CC-98A117DC9F0D}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrFMVFunction_vtables_dispatch_ = 1
IMGCVariantMgrFMVFunction_vtables_ = [
	(( 'Description' , 'desc' , ), 101, (101, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Description' , 'desc' , ), 101, (101, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'FunctionType' , 'fType' , ), 104, (104, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'FunctionType' , 'fType' , ), 104, (104, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'VariantAssignments' , 'filter' , 'ppVariantColl' , ), 106, (106, (), [ (12, 17, None, None) , 
			 (16393, 10, None, "IID('{7255B70F-5A93-4770-8D66-A32C07310BA1}')") , ], 1 , 2 , 4 , 1 , 248 , (3, 0, None, None) , 0 , )),
	(( 'VariantAssignments' , 'filter' , 'ppVariantColl' , ), 106, (106, (), [ (12, 17, None, None) , 
			 (16393, 10, None, "IID('{7255B70F-5A93-4770-8D66-A32C07310BA1}')") , ], 1 , 2 , 4 , 1 , 248 , (3, 0, None, None) , 0 , )),
	(( 'IsVariantAssigned' , 'variantName' , 'result' , ), 107, (107, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'PutVariantAssignment' , 'variantDefinition' , 'position' , 'ppObj' , ), 108, (108, (), [ 
			 (12, 1, None, None) , (2, 49, '-1', None) , (16393, 10, None, "IID('{874DEFFA-9480-4725-BCE3-06FE0427B1CA}')") , ], 1 , 1 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'FindVariantAssignment' , 'variantDefinition' , 'ppObj' , ), 109, (109, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{874DEFFA-9480-4725-BCE3-06FE0427B1CA}')") , ], 1 , 1 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'DeleteVariantAssignment' , 'variantDefinition' , 'result' , ), 110, (110, (), [ (12, 1, None, None) , 
			 (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'Delete' , 'result' , ), 111, (111, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'Hyperlink' , 'hyplnk' , ), 112, (112, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'Hyperlink' , 'hyplnk' , ), 112, (112, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrFMVFunctionAssignment_vtables_dispatch_ = 1
IMGCVariantMgrFMVFunctionAssignment_vtables_ = [
	(( 'FMVFunction' , 'ppObj' , ), 101, (101, (), [ (16393, 10, None, "IID('{786637FB-9407-11D2-89D9-0020184077E1}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'FMVFunction' , 'ppObj' , ), 101, (101, (), [ (9, 1, None, "IID('{786637FB-9407-11D2-89D9-0020184077E1}')") , ], 1 , 8 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Delete' , 'result' , ), 102, (102, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrFMVFunctionAssignments_vtables_dispatch_ = 1
IMGCVariantMgrFMVFunctionAssignments_vtables_ = [
	(( 'Item' , 'index' , 'ppObj' , ), 101, (101, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{B531AD99-09B2-4D15-AC0D-8F3A75F64A14}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'MoveUp' , 'pObj' , 'moveDelta' , 'result' , ), 102, (102, (), [ 
			 (9, 1, None, "IID('{B531AD99-09B2-4D15-AC0D-8F3A75F64A14}')") , (2, 49, '1', None) , (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'MoveDown' , 'pObj' , 'moveDelta' , 'result' , ), 103, (103, (), [ 
			 (9, 1, None, "IID('{B531AD99-09B2-4D15-AC0D-8F3A75F64A14}')") , (2, 49, '1', None) , (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrFMVFunctionGroup_vtables_dispatch_ = 1
IMGCVariantMgrFMVFunctionGroup_vtables_ = [
	(( 'FMVFunctionAssignments' , 'filter' , 'ppFunctAssColl' , ), 102, (102, (), [ (12, 17, None, None) , 
			 (16393, 10, None, "IID('{58977901-B0FA-491B-9F30-75EBA4E8D3C8}')") , ], 1 , 2 , 4 , 1 , 232 , (3, 0, None, None) , 0 , )),
	(( 'FMVFunctionAssignments' , 'filter' , 'ppFunctAssColl' , ), 102, (102, (), [ (12, 17, None, None) , 
			 (16393, 10, None, "IID('{58977901-B0FA-491B-9F30-75EBA4E8D3C8}')") , ], 1 , 2 , 4 , 1 , 232 , (3, 0, None, None) , 0 , )),
	(( 'PutFMVFunctionAssignment' , 'variantDefinition' , 'position' , 'ppObj' , ), 103, (103, (), [ 
			 (12, 1, None, None) , (2, 49, '-1', None) , (16393, 10, None, "IID('{B531AD99-09B2-4D15-AC0D-8F3A75F64A14}')") , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'FindFMVFunctionAssignment' , 'variantDefinition' , 'ppObj' , ), 104, (104, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{B531AD99-09B2-4D15-AC0D-8F3A75F64A14}')") , ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Delete' , 'result' , ), 105, (105, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrFMVFunctionGroups_vtables_dispatch_ = 1
IMGCVariantMgrFMVFunctionGroups_vtables_ = [
	(( 'Item' , 'index' , 'ppGroup' , ), 101, (101, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{6320E666-2421-4912-AEE9-CFC712EE05C0}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'pGroup' , ), 102, (102, (), [ (9, 1, None, "IID('{6320E666-2421-4912-AEE9-CFC712EE05C0}')") , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrFMVFunctions_vtables_dispatch_ = 1
IMGCVariantMgrFMVFunctions_vtables_ = [
	(( 'Item' , 'index' , 'ppFunction' , ), 101, (101, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{786637FB-9407-11D2-89D9-0020184077E1}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'pFunction' , ), 102, (102, (), [ (9, 1, None, "IID('{786637FB-9407-11D2-89D9-0020184077E1}')") , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrFMVProperties_vtables_dispatch_ = 1
IMGCVariantMgrFMVProperties_vtables_ = [
	(( 'Item' , 'index' , 'ppFMVProp' , ), 101, (101, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{DD445D35-DC4B-413A-8781-F561D40D4CC5}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'pSymbIRec' , ), 102, (102, (), [ (9, 1, None, "IID('{DD445D35-DC4B-413A-8781-F561D40D4CC5}')") , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrFMVProperty_vtables_dispatch_ = 1
IMGCVariantMgrFMVProperty_vtables_ = [
	(( 'ChangeOperation' , 'value' , ), 102, (102, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'ChangeOperation' , 'value' , ), 102, (102, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'NewPartNumber' , 'value' , ), 103, (103, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'NewPartNumber' , 'value' , ), 103, (103, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'NewCell' , 'cellName' , ), 104, (104, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'NewCell' , 'cellName' , ), 104, (104, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'FMVFunction' , 'ppFunc' , ), 105, (105, (), [ (16393, 10, None, "IID('{786637FB-9407-11D2-89D9-0020184077E1}')") , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'FMVFunction' , 'ppFunc' , ), 105, (105, (), [ (9, 1, None, "IID('{786637FB-9407-11D2-89D9-0020184077E1}')") , ], 1 , 8 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'Delete' , 'result' , ), 106, (106, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'ReuseAccessMode' , 'accessMode' , ), 107, (107, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 64 , )),
	(( 'Symbol' , 'ppFunc' , ), 108, (108, (), [ (16393, 10, None, "IID('{786637F4-9407-11D2-89D9-0020184077E1}')") , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'MarkForCheckingConflicts' , ), 109, (109, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 304 , (3, 0, None, None) , 64 , )),
	(( 'NewAliasPartNumber' , 'value' , ), 110, (110, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'NewAliasPartNumber' , 'value' , ), 110, (110, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrFilters_vtables_dispatch_ = 1
IMGCVariantMgrFilters_vtables_ = [
	(( 'NewPackageModificationFilter' , 'ppObj' , ), 117, (117, (), [ (16393, 10, None, "IID('{7E1CD29C-D3B5-4690-91D5-415965F42BA6}')") , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'NewBlockDataModificationFilter' , 'ppObj' , ), 118, (118, (), [ (16393, 10, None, "IID('{761BC783-46D2-4961-835B-653901ED7E7F}')") , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'NewPackageFilter' , 'ppObj' , ), 119, (119, (), [ (16393, 10, None, "IID('{B01F00BE-D881-46C2-B841-82D35B117ED4}')") , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'NewBorderPropModificationFilter' , 'ppObj' , ), 120, (120, (), [ (16393, 10, None, "IID('{1158040D-F8C4-4865-A4A6-F42D11C258BA}')") , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'NewSymbolFilter' , 'ppObj' , ), 121, (121, (), [ (16393, 10, None, "IID('{9ADE593A-D453-4433-B7EF-281D82D31EAD}')") , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrGroupings_vtables_dispatch_ = 1
IMGCVariantMgrGroupings_vtables_ = [
	(( 'FMVFunctionGroups' , 'filter' , 'ppGroupColl' , ), 101, (101, (), [ (12, 17, None, None) , 
			 (16393, 10, None, "IID('{AF197ECE-D3D5-4720-AB62-F3F2E0CB52F4}')") , ], 1 , 2 , 4 , 1 , 200 , (3, 0, None, None) , 0 , )),
	(( 'FMVFunctionGroups' , 'filter' , 'ppGroupColl' , ), 101, (101, (), [ (12, 17, None, None) , 
			 (16393, 10, None, "IID('{AF197ECE-D3D5-4720-AB62-F3F2E0CB52F4}')") , ], 1 , 2 , 4 , 1 , 200 , (3, 0, None, None) , 0 , )),
	(( 'VariantGroups' , 'filter' , 'ppGroupColl' , ), 102, (102, (), [ (12, 17, None, None) , 
			 (16393, 10, None, "IID('{19DBCD8C-D9AF-4B85-8439-89F12F23F406}')") , ], 1 , 2 , 4 , 1 , 208 , (3, 0, None, None) , 0 , )),
	(( 'VariantGroups' , 'filter' , 'ppGroupColl' , ), 102, (102, (), [ (12, 17, None, None) , 
			 (16393, 10, None, "IID('{19DBCD8C-D9AF-4B85-8439-89F12F23F406}')") , ], 1 , 2 , 4 , 1 , 208 , (3, 0, None, None) , 0 , )),
	(( 'PutVariantGroup' , 'groupName' , 'groupDescription' , 'sourceForContents' , 'ppObj' , 
			 ), 103, (103, (), [ (8, 1, None, None) , (8, 1, None, None) , (12, 17, None, None) , (16393, 10, None, "IID('{3809BA4C-72E2-436F-B258-88EBA46444C8}')") , ], 1 , 1 , 4 , 1 , 216 , (3, 0, None, None) , 0 , )),
	(( 'FindVariantGroup' , 'groupName' , 'ppObj' , ), 104, (104, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{3809BA4C-72E2-436F-B258-88EBA46444C8}')") , ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'FindFMVFunctionGroup' , 'groupName' , 'ppObj' , ), 105, (105, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{6320E666-2421-4912-AEE9-CFC712EE05C0}')") , ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'PutFMVFunctionGroup' , 'groupName' , 'groupDescription' , 'sourceForContents' , 'ppObj' , 
			 ), 106, (106, (), [ (8, 1, None, None) , (8, 1, None, None) , (12, 17, None, None) , (16393, 10, None, "IID('{6320E666-2421-4912-AEE9-CFC712EE05C0}')") , ], 1 , 1 , 4 , 1 , 240 , (3, 0, None, None) , 0 , )),
	(( 'FindVariantGroupByUID' , 'userID' , 'objectID' , 'objectType' , 'ppObj' , 
			 ), 107, (107, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16393, 10, None, "IID('{3809BA4C-72E2-436F-B258-88EBA46444C8}')") , ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 64 , )),
	(( 'FindFMVFunctionGroupByUID' , 'userID' , 'objectID' , 'objectType' , 'ppObj' , 
			 ), 108, (108, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16393, 10, None, "IID('{6320E666-2421-4912-AEE9-CFC712EE05C0}')") , ], 1 , 1 , 4 , 0 , 256 , (3, 0, None, None) , 64 , )),
]

IMGCVariantMgrMessageMgr_vtables_dispatch_ = 1
IMGCVariantMgrMessageMgr_vtables_ = [
	(( 'ClearSendList' , ), 100, (100, (), [ ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'AddSymbolToSendList' , 'pSymbol' , ), 101, (101, (), [ (9, 1, None, "IID('{786637F4-9407-11D2-89D9-0020184077E1}')") , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'AddPackageToSendList' , 'pPack' , ), 102, (102, (), [ (9, 1, None, "IID('{786637F5-9407-11D2-89D9-0020184077E1}')") , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'AddSymbolToSendListUID' , 'userID' , 'objectID' , 'objectType' , ), 103, (103, (), [ 
			 (19, 1, None, None) , (19, 1, None, None) , (19, 1, None, None) , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'AddPackageToSendListUID' , 'userID' , 'objectID' , 'objectType' , ), 104, (104, (), [ 
			 (19, 1, None, None) , (19, 1, None, None) , (19, 1, None, None) , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'CountSendList' , 'desc' , ), 105, (105, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'ExecuteSend' , 'result' , ), 106, (106, (), [ (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'StartListener' , 'result' , ), 107, (107, (), [ (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'StopListener' , 'result' , ), 108, (108, (), [ (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'IsListenerActive' , 'result' , ), 109, (109, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'BroadcastMessage' , 'messageToSend' , 'categoryID' , 'result' , ), 110, (110, (), [ 
			 (8, 1, None, None) , (19, 1, None, None) , (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'PauseListener' , 'result' , ), 111, (111, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'RestartListener' , 'result' , ), 112, (112, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'SetCrossProbeSnapshot' , 'snapshot' , ), 113, (113, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 64 , )),
]

IMGCVariantMgrOutputGenerator_vtables_dispatch_ = 1
IMGCVariantMgrOutputGenerator_vtables_ = [
	(( 'GenerateOutput' , 'VariantID' , 'result' , ), 101, (101, (), [ (8, 1, None, None) , 
			 (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'ViewVariant' , 'VariantID' , 'result' , ), 102, (102, (), [ (8, 1, None, None) , 
			 (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'MustGeneratebeforeView' , 'pFlag' , ), 103, (103, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'ResetToMaster' , 'result' , ), 104, (104, (), [ (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Parameters' , 'parametersColl' , ), 105, (105, (), [ (16393, 10, None, "IID('{82CD5AB0-9407-11D2-89D9-0020184077E1}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'ErrorCode' , 'pCode' , ), 106, (106, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'ErrorDescription' , 'pDesc' , ), 107, (107, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrPModsUtility_vtables_dispatch_ = 1
IMGCVariantMgrPModsUtility_vtables_ = [
	(( 'PutPackageModification' , 'variantDefinition' , 'packageDefinition' , 'changeOper' , 'PartNumber' , 
			 'cellName' , 'ppObj' , ), 101, (101, (), [ (12, 1, None, None) , (12, 1, None, None) , 
			 (3, 1, None, None) , (8, 49, "''", None) , (8, 49, "''", None) , (16393, 10, None, "IID('{786637FD-9407-11D2-89D9-0020184077E1}')") , ], 1 , 1 , 4 , 0 , 136 , (3, 32, None, None) , 0 , )),
	(( 'FindPackageModification' , 'variantDef' , 'packageDef' , 'ppObj' , ), 102, (102, (), [ 
			 (12, 1, None, None) , (12, 1, None, None) , (16393, 10, None, "IID('{786637FD-9407-11D2-89D9-0020184077E1}')") , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'PackageModifications' , 'filter' , 'ppSymbMods' , ), 103, (103, (), [ (12, 17, None, None) , 
			 (16393, 10, None, "IID('{786637FE-9407-11D2-89D9-0020184077E1}')") , ], 1 , 2 , 4 , 1 , 152 , (3, 0, None, None) , 0 , )),
	(( 'PackageModifications' , 'filter' , 'ppSymbMods' , ), 103, (103, (), [ (12, 17, None, None) , 
			 (16393, 10, None, "IID('{786637FE-9407-11D2-89D9-0020184077E1}')") , ], 1 , 2 , 4 , 1 , 152 , (3, 0, None, None) , 0 , )),
	(( 'FindPackageModificationByUID' , 'userID' , 'objectID' , 'objectType' , 'ppObj' , 
			 ), 104, (104, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16393, 10, None, "IID('{786637FD-9407-11D2-89D9-0020184077E1}')") , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'PutBlockDataModification' , 'variantDefinition' , 'blockDataDefinition' , 'changeOper' , 'SubVariantName' , 
			 'ppObj' , ), 105, (105, (), [ (12, 1, None, None) , (12, 1, None, None) , (3, 1, None, None) , 
			 (8, 49, "''", None) , (16393, 10, None, "IID('{5F556342-9E5E-4B96-9002-9B148BA114DD}')") , ], 1 , 1 , 4 , 0 , 168 , (3, 32, None, None) , 0 , )),
	(( 'FindBlockDataModification' , 'variantDef' , 'blockDataDef' , 'ppObj' , ), 106, (106, (), [ 
			 (12, 1, None, None) , (12, 1, None, None) , (16393, 10, None, "IID('{5F556342-9E5E-4B96-9002-9B148BA114DD}')") , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'BlockDataModifications' , 'filter' , 'ppBlockDataMods' , ), 107, (107, (), [ (12, 17, None, None) , 
			 (16393, 10, None, "IID('{45742780-B379-49F9-8431-16CB70520F9C}')") , ], 1 , 2 , 4 , 1 , 184 , (3, 0, None, None) , 0 , )),
	(( 'BlockDataModifications' , 'filter' , 'ppBlockDataMods' , ), 107, (107, (), [ (12, 17, None, None) , 
			 (16393, 10, None, "IID('{45742780-B379-49F9-8431-16CB70520F9C}')") , ], 1 , 2 , 4 , 1 , 184 , (3, 0, None, None) , 0 , )),
	(( 'FindBlockDataModificationByUID' , 'userID' , 'objectID' , 'objectType' , 'ppObj' , 
			 ), 108, (108, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16393, 10, None, "IID('{5F556342-9E5E-4B96-9002-9B148BA114DD}')") , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'IsLOPackageEditable' , 'variantDef' , 'packageDef' , 'value' , ), 109, (109, (), [ 
			 (12, 1, None, None) , (12, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 64 , )),
	(( 'IsLOBlockDataEditable' , 'variantDef' , 'blockDataDef' , 'value' , ), 110, (110, (), [ 
			 (12, 1, None, None) , (12, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 64 , )),
]

IMGCVariantMgrPackage_vtables_dispatch_ = 1
IMGCVariantMgrPackage_vtables_ = [
	(( 'Symbols' , 'filter' , 'symbolsColl' , ), 101, (101, (), [ (12, 17, None, None) , 
			 (16393, 10, None, "IID('{786637F7-9407-11D2-89D9-0020184077E1}')") , ], 1 , 2 , 4 , 1 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Symbols' , 'filter' , 'symbolsColl' , ), 101, (101, (), [ (12, 17, None, None) , 
			 (16393, 10, None, "IID('{786637F7-9407-11D2-89D9-0020184077E1}')") , ], 1 , 2 , 4 , 1 , 216 , (3, 0, None, None) , 0 , )),
	(( 'PartNumber' , 'pnName' , ), 102, (102, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'PartNumber' , 'pnName' , ), 102, (102, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Cell' , 'cellName' , ), 103, (103, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 64 , )),
	(( 'Cell' , 'cellName' , ), 103, (103, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 64 , )),
	(( 'SymbolPath' , 'value' , ), 104, (104, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 64 , )),
	(( 'ReuseAccessMode' , 'accessMode' , ), 105, (105, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 64 , )),
	(( 'FindSymbolInstanceNames' , 'SymbolPath' , 'value' , 'numSymbols' , ), 106, (106, (), [ 
			 (8, 1, None, None) , (16392, 2, None, None) , (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 272 , (3, 0, None, None) , 64 , )),
	(( 'PackageState' , 'state' , ), 107, (107, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 64 , )),
	(( 'FMVDriven' , 'value' , ), 108, (108, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 64 , )),
	(( 'FMVDriven' , 'value' , ), 108, (108, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 64 , )),
	(( 'UnplaceFromNewVars' , 'value' , ), 109, (109, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 304 , (3, 0, None, None) , 64 , )),
	(( 'UnplaceFromNewVars' , 'value' , ), 109, (109, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 64 , )),
	(( 'IsParentReusedBlock' , 'value' , ), 110, (110, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 64 , )),
	(( 'RFComponent' , 'value' , ), 111, (111, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 328 , (3, 0, None, None) , 64 , )),
	(( 'RFComponent' , 'value' , ), 111, (111, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 64 , )),
	(( 'IncludedInBOM' , 'value' , ), 112, (112, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 344 , (3, 0, None, None) , 64 , )),
	(( 'IncludedInBOM' , 'value' , ), 112, (112, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 64 , )),
	(( 'Type' , 'value' , ), 113, (113, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 360 , (3, 0, None, None) , 64 , )),
	(( 'Type' , 'value' , ), 113, (113, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 64 , )),
	(( 'ParentPackage' , 'pPackage' , ), 114, (114, (), [ (16393, 10, None, "IID('{786637F5-9407-11D2-89D9-0020184077E1}')") , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'ParentPackage' , 'pPackage' , ), 114, (114, (), [ (9, 1, None, "IID('{786637F5-9407-11D2-89D9-0020184077E1}')") , ], 1 , 8 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'SID' , 'value' , ), 115, (115, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'SID' , 'value' , ), 115, (115, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'HKPFlag' , 'value' , ), 116, (116, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 408 , (3, 0, None, None) , 64 , )),
	(( 'HKPFlag' , 'value' , ), 116, (116, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 416 , (3, 0, None, None) , 64 , )),
	(( 'IsParentLogicalReusedBlock' , 'value' , ), 117, (117, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 424 , (3, 0, None, None) , 64 , )),
	(( 'ParentDynamicReuseBlockName' , 'DRBName' , ), 118, (118, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'ForwardPCBFlag' , 'value' , ), 119, (119, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 440 , (3, 0, None, None) , 64 , )),
	(( 'ForwardPCBFlag' , 'value' , ), 119, (119, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 448 , (3, 0, None, None) , 64 , )),
	(( 'CentLibPropValue' , 'propName' , 'propVal' , ), 120, (120, (), [ (8, 1, None, None) , 
			 (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 456 , (3, 0, None, None) , 64 , )),
	(( 'AliasPartNumber' , 'aliasPN' , ), 121, (121, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'AliasPartNumber' , 'aliasPN' , ), 121, (121, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'IsLogicalOnlyPartModificationAllowed' , 'value' , ), 122, (122, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 480 , (3, 0, None, None) , 64 , )),
]

IMGCVariantMgrPackageFilter_vtables_dispatch_ = 1
IMGCVariantMgrPackageFilter_vtables_ = [
	(( 'GetRootIF' , 'ppDocObj' , ), 100, (100, (), [ (16393, 2, None, "IID('{78663807-9407-11D2-89D9-0020184077E1}')") , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'ParentPackage' , ), 101, (101, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'value' , ), 102, (102, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'value' , ), 102, (102, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Initialize' , ), 103, (103, (), [ ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrPackageModification_vtables_dispatch_ = 1
IMGCVariantMgrPackageModification_vtables_ = [
	(( 'Package' , 'ppPackage' , ), 101, (101, (), [ (16393, 10, None, "IID('{786637F5-9407-11D2-89D9-0020184077E1}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'ChangeOperation' , 'value' , ), 102, (102, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'ChangeOperation' , 'value' , ), 102, (102, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'NewPartNumber' , 'value' , ), 103, (103, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'NewPartNumber' , 'value' , ), 103, (103, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'NewCell' , 'cellName' , ), 104, (104, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'NewCell' , 'cellName' , ), 104, (104, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'Variant' , 'ppVariant' , ), 105, (105, (), [ (16393, 10, None, "IID('{78663802-9407-11D2-89D9-0020184077E1}')") , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'Variant' , 'ppVariant' , ), 105, (105, (), [ (9, 1, None, "IID('{78663802-9407-11D2-89D9-0020184077E1}')") , ], 1 , 8 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'Delete' , 'result' , ), 106, (106, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'ReuseAccessMode' , 'accessMode' , ), 107, (107, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 64 , )),
	(( 'NewAliasPartNumber' , 'value' , ), 108, (108, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'NewAliasPartNumber' , 'value' , ), 108, (108, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrPackageModificationFilter_vtables_dispatch_ = 1
IMGCVariantMgrPackageModificationFilter_vtables_ = [
	(( 'GetRootIF' , 'ppDocObj' , ), 100, (100, (), [ (16393, 2, None, "IID('{78663807-9407-11D2-89D9-0020184077E1}')") , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Package' , ), 101, (101, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'ChangeOperation' , 'value' , ), 102, (102, (), [ (3, 49, '0', None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'ChangeOperation' , 'value' , ), 102, (102, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'NewPartNumber' , 'nameExpression' , ), 103, (103, (), [ (8, 49, "'*'", None) , ], 1 , 4 , 4 , 0 , 168 , (3, 32, None, None) , 0 , )),
	(( 'NewPartNumber' , 'nameExpression' , ), 103, (103, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Variant' , ), 104, (104, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'VariantGroup' , ), 105, (105, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Initialize' , ), 106, (106, (), [ ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrPackageModifications_vtables_dispatch_ = 1
IMGCVariantMgrPackageModifications_vtables_ = [
	(( 'Item' , 'index' , 'ppPackMod' , ), 101, (101, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{786637FD-9407-11D2-89D9-0020184077E1}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'pPackMod' , ), 102, (102, (), [ (9, 1, None, "IID('{786637FD-9407-11D2-89D9-0020184077E1}')") , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrPackages_vtables_dispatch_ = 1
IMGCVariantMgrPackages_vtables_ = [
	(( 'Item' , 'index' , 'ppPackage' , ), 101, (101, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{786637F5-9407-11D2-89D9-0020184077E1}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'pPackage' , ), 102, (102, (), [ (9, 1, None, "IID('{786637F5-9407-11D2-89D9-0020184077E1}')") , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrParameter_vtables_dispatch_ = 1
IMGCVariantMgrParameter_vtables_ = [
	(( 'value' , 'valStr' , ), 102, (102, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'value' , 'valStr' , ), 102, (102, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrParameters_vtables_dispatch_ = 1
IMGCVariantMgrParameters_vtables_ = [
	(( 'Item' , 'index' , 'ppParm' , ), 101, (101, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{82CD5AAF-9407-11D2-89D9-0020184077E1}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'Name' , 'value' , ), 102, (102, (), [ (8, 1, None, None) , 
			 (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrParent_vtables_dispatch_ = 0
IMGCVariantMgrParent_vtables_ = [
	(( 'SetParent' , 'pParentObj' , ), 1, (1, (), [ (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 24 , (3, 0, None, None) , 0 , )),
	(( 'GetParent' , 'pParentObj' , ), 2, (2, (), [ (16393, 2, None, None) , ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'GetRootIF' , 'ppDocObj' , ), 3, (3, (), [ (16393, 2, None, "IID('{78663807-9407-11D2-89D9-0020184077E1}')") , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'GetHierObjectContext' , 'functionID' , 'result' , ), 4, (4, (), [ (8, 0, None, None) , 
			 (16392, 0, None, None) , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrProperties_vtables_dispatch_ = 1
IMGCVariantMgrProperties_vtables_ = [
	(( 'Item' , 'index' , 'ppProp' , ), 101, (101, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{6ABBB0DE-2FAC-45DB-90CA-E90A630B0FBB}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'pPropRec' , ), 102, (102, (), [ (9, 1, None, "IID('{6ABBB0DE-2FAC-45DB-90CA-E90A630B0FBB}')") , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Find' , 'Name' , 'ppProp' , ), 103, (103, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{6ABBB0DE-2FAC-45DB-90CA-E90A630B0FBB}')") , ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrProperty_vtables_dispatch_ = 1
IMGCVariantMgrProperty_vtables_ = [
	(( 'value' , 'pnName' , ), 101, (101, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'value' , 'pnName' , ), 101, (101, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'ReadOnly' , 'pnName' , ), 102, (102, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Delete' , 'result' , ), 103, (103, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrReporter_vtables_dispatch_ = 1
IMGCVariantMgrReporter_vtables_ = [
	(( 'Settings' , 'ppObj' , ), 101, (101, (), [ (16393, 10, None, "IID('{353E3059-2914-4F62-AD38-D61BD61F620F}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'GenHTMLReport' , 'result' , ), 102, (102, (), [ (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'GenDelimitedTextReport' , 'result' , ), 103, (103, (), [ (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'GenFormattedLogReport' , 'result' , ), 104, (104, (), [ (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'GenExcelReport' , 'result' , ), 105, (105, (), [ (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'DataMatrix' , 'ppObj' , ), 106, (106, (), [ (16393, 10, None, "IID('{9E5DF0FC-CE34-409A-B257-AD8E39BBD95E}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 64 , )),
	(( 'WriteExcelReport' , 'result' , ), 107, (107, (), [ (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'WriteHTMLReport' , 'result' , ), 108, (108, (), [ (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'WriteDelimitedTextReport' , 'result' , ), 109, (109, (), [ (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'WriteFormattedLogReport' , 'result' , ), 110, (110, (), [ (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrReporterDataMatrix_vtables_dispatch_ = 1
IMGCVariantMgrReporterDataMatrix_vtables_ = [
	(( 'NumColumns' , 'value' , ), 101, (101, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'NumColumns' , 'value' , ), 101, (101, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'NumRows' , 'value' , ), 102, (102, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'NumRows' , 'value' , ), 102, (102, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'GetHeaderValue' , 'columnIndex' , 'value' , ), 103, (103, (), [ (3, 1, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'GetMaxColumnWidth' , 'columnIndex' , 'value' , ), 104, (104, (), [ (3, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'GetCellValue' , 'columnIndex' , 'rowIndex' , 'value' , ), 105, (105, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'SetCellValue' , 'columnIndex' , 'rowIndex' , 'value' , ), 107, (107, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Initialize' , ), 106, (106, (), [ ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'SetHeaderData' , 'columnIndex' , 'value' , ), 108, (108, (), [ (3, 1, None, None) , 
			 (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrReporterSettings_vtables_dispatch_ = 1
IMGCVariantMgrReporterSettings_vtables_ = [
	(( 'OutputFile' , 'value' , ), 101, (101, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'OutputFile' , 'value' , ), 101, (101, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'UnplacedKW' , 'value' , ), 102, (102, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'UnplacedKW' , 'value' , ), 102, (102, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Title' , 'value' , ), 104, (104, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Title' , 'value' , ), 104, (104, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Date' , 'value' , ), 105, (105, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Date' , 'value' , ), 105, (105, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'DifferencesOnly' , 'value' , ), 106, (106, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'DifferencesOnly' , 'value' , ), 106, (106, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'AddVariantToList' , 'variantSpec' , ), 107, (107, (), [ (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'AddVariantGroupToList' , 'groupSpec' , ), 108, (108, (), [ (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Initialize' , ), 109, (109, (), [ ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'IncludeMasterPartNumber' , 'value' , ), 110, (110, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'IncludeMasterPartNumber' , 'value' , ), 110, (110, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'FieldDelimiter' , 'value' , ), 111, (111, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'FieldDelimiter' , 'value' , ), 111, (111, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'AddFMVFunctionToList' , 'functionSpec' , ), 112, (112, (), [ (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'AddFMVFunctionGroupToList' , 'groupSpec' , ), 113, (113, (), [ (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'IncludeRefdesForFMVs' , 'value' , ), 114, (114, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'IncludeRefdesForFMVs' , 'value' , ), 114, (114, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'ReportDataType' , 'value' , ), 115, (115, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'ReportDataType' , 'value' , ), 115, (115, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'groupName' , 'value' , ), 116, (116, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'IncludeGroupName' , 'value' , ), 117, (117, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'IncludeGroupName' , 'value' , ), 117, (117, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrReuseSettings_vtables_dispatch_ = 1
IMGCVariantMgrReuseSettings_vtables_ = [
	(( 'DefaultAccessMode' , 'bflag' , ), 100, (100, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 64 , )),
	(( 'DefaultAccessMode' , 'bflag' , ), 100, (100, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 64 , )),
	(( 'DefaultMergeMode' , 'bflag' , ), 101, (101, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'DefaultMergeMode' , 'bflag' , ), 101, (101, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'AllowAccessOverwrite' , 'value' , ), 102, (102, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'AllowAccessOverwrite' , 'value' , ), 102, (102, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'AllowMergeModeOverwrite' , 'value' , ), 103, (103, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'AllowMergeModeOverwrite' , 'value' , ), 103, (103, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrReusedBlock_vtables_dispatch_ = 1
IMGCVariantMgrReusedBlock_vtables_ = [
	(( 'LibraryName' , 'value' , ), 120, (120, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'LibraryName' , 'value' , ), 120, (120, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'accessMode' , 'bflag' , ), 121, (121, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 64 , )),
	(( 'accessMode' , 'bflag' , ), 121, (121, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 64 , )),
	(( 'MergeMode' , 'bflag' , ), 122, (122, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'MergeMode' , 'bflag' , ), 122, (122, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'MergeFromLibrary' , 'logFilesDir' , 'result' , ), 123, (123, (), [ (8, 1, None, None) , 
			 (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'VariantMappings' , 'filter' , 'ppColl' , ), 124, (124, (), [ (12, 17, None, None) , 
			 (16393, 10, None, "IID('{5F5FA27B-9A28-4A84-BE9A-7460F1D6D54B}')") , ], 1 , 2 , 4 , 1 , 280 , (3, 0, None, None) , 0 , )),
	(( 'VariantMappings' , 'filter' , 'ppColl' , ), 124, (124, (), [ (12, 17, None, None) , 
			 (16393, 10, None, "IID('{5F5FA27B-9A28-4A84-BE9A-7460F1D6D54B}')") , ], 1 , 2 , 4 , 1 , 280 , (3, 0, None, None) , 0 , )),
	(( 'PutVariantMapping' , 'originalVariantName' , 'newVariantName' , 'MappingFlags' , 'ppObj' , 
			 ), 125, (125, (), [ (8, 1, None, None) , (8, 1, None, None) , (3, 1, None, None) , (16393, 10, None, "IID('{746F9DCE-E85C-4BA5-BE14-FEF24731222A}')") , ], 1 , 1 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'FindVariantMapping' , 'mappingDefinition' , 'ppObj' , ), 126, (126, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{746F9DCE-E85C-4BA5-BE14-FEF24731222A}')") , ], 1 , 1 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'ReusedVariants' , 'filter' , 'ppVariantColl' , ), 127, (127, (), [ (12, 17, None, None) , 
			 (16393, 10, None, "IID('{78663803-9407-11D2-89D9-0020184077E1}')") , ], 1 , 2 , 4 , 1 , 304 , (3, 0, None, None) , 0 , )),
	(( 'ReusedVariants' , 'filter' , 'ppVariantColl' , ), 127, (127, (), [ (12, 17, None, None) , 
			 (16393, 10, None, "IID('{78663803-9407-11D2-89D9-0020184077E1}')") , ], 1 , 2 , 4 , 1 , 304 , (3, 0, None, None) , 0 , )),
	(( 'MergeStatus' , 'value' , ), 128, (128, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'Flattened' , 'value' , ), 129, (129, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 64 , )),
	(( 'Flattened' , 'value' , ), 129, (129, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 328 , (3, 0, None, None) , 64 , )),
	(( 'ReuseBlockDocument' , 'ppDocIF' , ), 130, (130, (), [ (16393, 10, None, "IID('{78663807-9407-11D2-89D9-0020184077E1}')") , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 64 , )),
	(( 'LogicalOnly' , 'value' , ), 131, (131, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 64 , )),
	(( 'LogicalOnly' , 'value' , ), 131, (131, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 352 , (3, 0, None, None) , 64 , )),
	(( 'LogicalOnlyPartModificationAllowed' , 'value' , ), 132, (132, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 64 , )),
	(( 'LogicalOnlyPartModificationAllowed' , 'value' , ), 132, (132, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 368 , (3, 0, None, None) , 64 , )),
]

IMGCVariantMgrReusedBlocks_vtables_dispatch_ = 1
IMGCVariantMgrReusedBlocks_vtables_ = [
	(( 'Item' , 'index' , 'ppObj' , ), 101, (101, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{82CD5AA4-9407-11D2-89D9-0020184077E1}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'pReusedBlock' , ), 102, (102, (), [ (9, 1, None, "IID('{82CD5AA4-9407-11D2-89D9-0020184077E1}')") , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrSInfoRecsUtility_vtables_dispatch_ = 1
IMGCVariantMgrSInfoRecsUtility_vtables_ = [
	(( 'SymbolInfoRecs' , 'filter' , 'ppSymbIRecs' , ), 101, (101, (), [ (12, 17, None, None) , 
			 (16393, 10, None, "IID('{A6C3A4DE-6048-492D-AA03-EC268CCC73D4}')") , ], 1 , 2 , 4 , 1 , 136 , (3, 0, None, None) , 0 , )),
	(( 'SymbolInfoRecs' , 'filter' , 'ppSymbIRecs' , ), 101, (101, (), [ (12, 17, None, None) , 
			 (16393, 10, None, "IID('{A6C3A4DE-6048-492D-AA03-EC268CCC73D4}')") , ], 1 , 2 , 4 , 1 , 136 , (3, 0, None, None) , 0 , )),
	(( 'PutSymbolInfoRec' , 'symbolDefinition' , 'ppObj' , ), 102, (102, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{A34D9F27-362F-45AA-9F73-CBC28DF7645E}')") , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'FindSymbolInfoRec' , 'symbolSpec' , 'ppObj' , ), 103, (103, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{A34D9F27-362F-45AA-9F73-CBC28DF7645E}')") , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'RequiresPackModRecalc' , 'value' , ), 104, (104, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'RequiresRepackage' , 'value' , ), 105, (105, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'RequiresMatrixCheck' , 'value' , ), 106, (106, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'RequiresMatrixCheck' , 'value' , ), 106, (106, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'CheckConflict' , 'symbolDefinition' , 'funcDefinition' , 'changeOper' , 'rplPartNumber' , 
			 'rplCell' , 'conflictingFunc' , 'errStr' , 'errStatus' , ), 107, (107, (), [ 
			 (12, 1, None, None) , (12, 1, None, None) , (3, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , 
			 (16392, 2, None, None) , (16392, 2, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'CheckVariantMatrixConflict' , 'funcDef' , 'variantDef' , 'errStr' , 'errStatus' , 
			 ), 108, (108, (), [ (12, 1, None, None) , (12, 1, None, None) , (16392, 2, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'RecalculatePackmods' , 'retval' , ), 109, (109, (), [ (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'FindFMVPropertyByUID' , 'userID' , 'objectID' , 'objectType' , 'ppObj' , 
			 ), 110, (110, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16393, 10, None, "IID('{DD445D35-DC4B-413A-8781-F561D40D4CC5}')") , ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 64 , )),
	(( 'FinishCheckingConflicts' , 'bConfirm' , 'result' , ), 111, (111, (), [ (11, 1, None, None) , 
			 (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 64 , )),
]

IMGCVariantMgrSettings_vtables_dispatch_ = 1
IMGCVariantMgrSettings_vtables_ = [
	(( 'Statistics' , 'ppCapaObj' , ), 102, (102, (), [ (16393, 10, None, "IID('{8F683CE7-08DB-45B8-B4EA-E27982CF0995}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'ReuseSettings' , 'ppRSettingsObj' , ), 103, (103, (), [ (16393, 10, None, "IID('{CA185E0D-76D0-43D5-A215-F301941E074F}')") , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrStatistics_vtables_dispatch_ = 1
IMGCVariantMgrStatistics_vtables_ = [
	(( 'CountInfo' , 'statType' , 'countVal' , ), 101, (101, (), [ (3, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'IsFlatDesign' , 'value' , ), 102, (102, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrSymbol_vtables_dispatch_ = 1
IMGCVariantMgrSymbol_vtables_ = [
	(( 'SymbolLocation' , 'ppLoc' , ), 101, (101, (), [ (16393, 10, None, "IID('{786637F3-9407-11D2-89D9-0020184077E1}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 64 , )),
	(( 'Package' , 'ppPack' , ), 102, (102, (), [ (16393, 10, None, "IID('{786637F5-9407-11D2-89D9-0020184077E1}')") , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'SymbolType' , 'SymbolType' , ), 103, (103, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'SymbolType' , 'SymbolType' , ), 103, (103, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'NameAndPath' , 'result' , ), 104, (104, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 64 , )),
	(( 'ReuseAccessMode' , 'accessMode' , ), 105, (105, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 64 , )),
	(( 'Cell' , 'cellName' , ), 106, (106, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'Cell' , 'cellName' , ), 106, (106, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'PartNumber' , 'value' , ), 107, (107, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'PartNumber' , 'value' , ), 107, (107, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'Page' , 'Page' , ), 108, (108, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 64 , )),
	(( 'PageIndex' , 'value' , ), 109, (109, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 64 , )),
	(( 'ParentBlock' , 'ppLoc' , ), 110, (110, (), [ (16393, 10, None, "IID('{E2CD1C5F-0EE9-4349-B08A-FA34A84CB2F1}')") , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 64 , )),
	(( 'ParentReusedBlock' , 'ppLoc' , ), 111, (111, (), [ (16393, 10, None, "IID('{82CD5AA4-9407-11D2-89D9-0020184077E1}')") , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 64 , )),
	(( 'Block' , 'ppLoc' , ), 112, (112, (), [ (16393, 10, None, "IID('{E2CD1C5F-0EE9-4349-B08A-FA34A84CB2F1}')") , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 64 , )),
	(( 'ReusedBlock' , 'ppLoc' , ), 113, (113, (), [ (16393, 10, None, "IID('{82CD5AA4-9407-11D2-89D9-0020184077E1}')") , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 64 , )),
	(( 'IsArrayedSymbol' , 'value' , ), 114, (114, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'ArrayCompName' , 'compName' , ), 115, (115, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'ArrayCompName' , 'compName' , ), 115, (115, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'ParentDynamicReuseBlockName' , 'DRBName' , ), 116, (116, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'AliasPartNumber' , 'value' , ), 117, (117, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'AliasPartNumber' , 'value' , ), 117, (117, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrSymbolFilter_vtables_dispatch_ = 1
IMGCVariantMgrSymbolFilter_vtables_ = [
	(( 'GetRootIF' , 'ppDocObj' , ), 100, (100, (), [ (16393, 2, None, "IID('{78663807-9407-11D2-89D9-0020184077E1}')") , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'OnlyBorderSymbols' , 'pValue' , ), 102, (102, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'OnlyBorderSymbols' , 'pValue' , ), 102, (102, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Initialize' , ), 103, (103, (), [ ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrSymbolInfoRec_vtables_dispatch_ = 1
IMGCVariantMgrSymbolInfoRec_vtables_ = [
	(( 'Symbol' , 'ppSymbol' , ), 101, (101, (), [ (16393, 10, None, "IID('{786637F4-9407-11D2-89D9-0020184077E1}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Symbol' , 'ppSymbol' , ), 101, (101, (), [ (9, 1, None, "IID('{786637F4-9407-11D2-89D9-0020184077E1}')") , ], 1 , 8 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'FMVProperties' , 'filter' , 'ppFMVPropColl' , ), 102, (102, (), [ (12, 17, None, None) , 
			 (16393, 10, None, "IID('{3C44AB05-4C95-4984-BD98-135CDD2B39C1}')") , ], 1 , 2 , 4 , 1 , 232 , (3, 0, None, None) , 0 , )),
	(( 'FMVProperties' , 'filter' , 'ppFMVPropColl' , ), 102, (102, (), [ (12, 17, None, None) , 
			 (16393, 10, None, "IID('{3C44AB05-4C95-4984-BD98-135CDD2B39C1}')") , ], 1 , 2 , 4 , 1 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Delete' , 'result' , ), 103, (103, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'ReuseAccessMode' , 'accessMode' , ), 104, (104, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 64 , )),
	(( 'CreatePackModData' , 'result' , ), 105, (105, (), [ (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'PutFMVProperty' , 'functionDefinition' , 'changeOper' , 'PartNumber' , 'cellName' , 
			 'ppObj' , ), 106, (106, (), [ (12, 1, None, None) , (3, 1, None, None) , (8, 49, "''", None) , 
			 (8, 49, "''", None) , (16393, 10, None, "IID('{DD445D35-DC4B-413A-8781-F561D40D4CC5}')") , ], 1 , 1 , 4 , 0 , 264 , (3, 32, None, None) , 0 , )),
	(( 'FindFMVProperty' , 'functionDefinition' , 'ppObj' , ), 107, (107, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{DD445D35-DC4B-413A-8781-F561D40D4CC5}')") , ], 1 , 1 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrSymbolInfoRecs_vtables_dispatch_ = 1
IMGCVariantMgrSymbolInfoRecs_vtables_ = [
	(( 'Item' , 'index' , 'ppSymbInfoRec' , ), 101, (101, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{A34D9F27-362F-45AA-9F73-CBC28DF7645E}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'pSymbIRec' , ), 102, (102, (), [ (9, 1, None, "IID('{A34D9F27-362F-45AA-9F73-CBC28DF7645E}')") , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'CreatePackModData' , 'result' , ), 105, (105, (), [ (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrSymbolLocation_vtables_dispatch_ = 1
IMGCVariantMgrSymbolLocation_vtables_ = [
	(( 'Path' , 'Path' , ), 101, (101, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Path' , 'Path' , ), 101, (101, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Page' , 'Page' , ), 102, (102, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Page' , 'Page' , ), 102, (102, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'id' , 'idOfPage' , ), 103, (103, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'id' , 'idOfPage' , ), 103, (103, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'PathIndex' , 'value' , ), 104, (104, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 64 , )),
	(( 'PageIndex' , 'value' , ), 105, (105, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrSymbolLocations_vtables_dispatch_ = 1
IMGCVariantMgrSymbolLocations_vtables_ = [
	(( 'Item' , 'index' , 'ppLoc' , ), 101, (101, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{786637F3-9407-11D2-89D9-0020184077E1}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'pLoc' , ), 102, (102, (), [ (9, 1, None, "IID('{786637F3-9407-11D2-89D9-0020184077E1}')") , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrSymbols_vtables_dispatch_ = 1
IMGCVariantMgrSymbols_vtables_ = [
	(( 'Item' , 'index' , 'ppSymbol' , ), 101, (101, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{786637F4-9407-11D2-89D9-0020184077E1}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'pSymbol' , ), 102, (102, (), [ (9, 1, None, "IID('{786637F4-9407-11D2-89D9-0020184077E1}')") , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrUID_vtables_dispatch_ = 1
IMGCVariantMgrUID_vtables_ = [
	(( 'userID' , 'value' , ), 100, (100, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'userID' , 'value' , ), 100, (100, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'objectID' , 'value' , ), 101, (101, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'objectID' , 'value' , ), 101, (101, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'objectType' , 'value' , ), 102, (102, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'objectType' , 'value' , ), 102, (102, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Initialize' , 'userID' , 'objectID' , 'objectType' , ), 103, (103, (), [ 
			 (19, 49, '0', None) , (19, 49, '0', None) , (19, 49, '0', None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'GetValue' , 'userID' , 'objectID' , 'objectType' , ), 104, (104, (), [ 
			 (16403, 2, None, None) , (16403, 2, None, None) , (16403, 2, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'InitializeObj' , 'obj' , ), 105, (105, (), [ (9, 1, None, "IID('{786637F0-9407-11D2-89D9-0020184077E1}')") , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'CompareObj' , 'obj' , 'result' , ), 106, (106, (), [ (9, 1, None, "IID('{786637F0-9407-11D2-89D9-0020184077E1}')") , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrUtility_vtables_dispatch_ = 1
IMGCVariantMgrUtility_vtables_ = [
	(( 'Filters' , 'ppObj' , ), 100, (100, (), [ (16393, 10, None, "IID('{C9D96C16-A541-4DA9-97E0-902FCD6C2412}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrVariant_vtables_dispatch_ = 1
IMGCVariantMgrVariant_vtables_ = [
	(( 'Description' , 'desc' , ), 101, (101, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Description' , 'desc' , ), 101, (101, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Number' , 'numberStr' , ), 102, (102, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Number' , 'numberStr' , ), 102, (102, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'PackageModifications' , 'filter' , 'ppPackModColl' , ), 104, (104, (), [ (12, 17, None, None) , 
			 (16393, 10, None, "IID('{786637FE-9407-11D2-89D9-0020184077E1}')") , ], 1 , 2 , 4 , 1 , 248 , (3, 0, None, None) , 0 , )),
	(( 'PackageModifications' , 'filter' , 'ppPackModColl' , ), 104, (104, (), [ (12, 17, None, None) , 
			 (16393, 10, None, "IID('{786637FE-9407-11D2-89D9-0020184077E1}')") , ], 1 , 2 , 4 , 1 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'vType' , ), 106, (106, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'vType' , ), 106, (106, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'Delete' , 'result' , ), 108, (108, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'FXEInclude' , 'value' , ), 109, (109, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 280 , (3, 0, None, None) , 64 , )),
	(( 'FXEInclude' , 'value' , ), 109, (109, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 64 , )),
	(( 'BOMInclude' , 'value' , ), 110, (110, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 296 , (3, 0, None, None) , 64 , )),
	(( 'BOMInclude' , 'value' , ), 110, (110, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 64 , )),
	(( 'FuncAttached' , 'value' , ), 111, (111, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 312 , (3, 0, None, None) , 64 , )),
	(( 'FuncAttached' , 'value' , ), 111, (111, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 64 , )),
	(( 'Hyperlink' , 'hyplnk' , ), 112, (112, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'Hyperlink' , 'hyplnk' , ), 112, (112, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'NotesLayers' , 'NotesLayers' , ), 113, (113, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'NotesLayers' , 'NotesLayers' , ), 113, (113, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrVariantAssignment_vtables_dispatch_ = 1
IMGCVariantMgrVariantAssignment_vtables_ = [
	(( 'Variant' , 'ppObj' , ), 101, (101, (), [ (16393, 10, None, "IID('{78663802-9407-11D2-89D9-0020184077E1}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Variant' , 'ppObj' , ), 101, (101, (), [ (9, 1, None, "IID('{78663802-9407-11D2-89D9-0020184077E1}')") , ], 1 , 8 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Delete' , 'result' , ), 102, (102, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrVariantAssignments_vtables_dispatch_ = 1
IMGCVariantMgrVariantAssignments_vtables_ = [
	(( 'Item' , 'index' , 'ppObj' , ), 101, (101, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{874DEFFA-9480-4725-BCE3-06FE0427B1CA}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'MoveUp' , 'pObj' , 'moveDelta' , 'result' , ), 102, (102, (), [ 
			 (9, 1, None, "IID('{874DEFFA-9480-4725-BCE3-06FE0427B1CA}')") , (2, 49, '1', None) , (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'MoveDown' , 'pObj' , 'moveDelta' , 'result' , ), 103, (103, (), [ 
			 (9, 1, None, "IID('{874DEFFA-9480-4725-BCE3-06FE0427B1CA}')") , (2, 49, '1', None) , (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrVariantGroup_vtables_dispatch_ = 1
IMGCVariantMgrVariantGroup_vtables_ = [
	(( 'VariantAssignments' , 'filter' , 'ppVariantColl' , ), 102, (102, (), [ (12, 17, None, None) , 
			 (16393, 10, None, "IID('{7255B70F-5A93-4770-8D66-A32C07310BA1}')") , ], 1 , 2 , 4 , 1 , 232 , (3, 0, None, None) , 0 , )),
	(( 'VariantAssignments' , 'filter' , 'ppVariantColl' , ), 102, (102, (), [ (12, 17, None, None) , 
			 (16393, 10, None, "IID('{7255B70F-5A93-4770-8D66-A32C07310BA1}')") , ], 1 , 2 , 4 , 1 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Delete' , 'result' , ), 103, (103, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'PutVariantAssignment' , 'variantDefinition' , 'position' , 'ppObj' , ), 104, (104, (), [ 
			 (12, 1, None, None) , (2, 49, '-1', None) , (16393, 10, None, "IID('{874DEFFA-9480-4725-BCE3-06FE0427B1CA}')") , ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'FindVariantAssignment' , 'variantDefinition' , 'ppObj' , ), 105, (105, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{874DEFFA-9480-4725-BCE3-06FE0427B1CA}')") , ], 1 , 1 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrVariantGroups_vtables_dispatch_ = 1
IMGCVariantMgrVariantGroups_vtables_ = [
	(( 'Item' , 'index' , 'ppGroup' , ), 101, (101, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{3809BA4C-72E2-436F-B258-88EBA46444C8}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'pGroup' , ), 102, (102, (), [ (9, 1, None, "IID('{3809BA4C-72E2-436F-B258-88EBA46444C8}')") , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrVariantInfoRec_vtables_dispatch_ = 1
IMGCVariantMgrVariantInfoRec_vtables_ = [
	(( 'Properties' , 'filter' , 'ppPropColl' , ), 101, (101, (), [ (12, 17, None, None) , 
			 (16393, 10, None, "IID('{FA1219FB-D82D-47B6-815F-F786F347E6E6}')") , ], 1 , 2 , 4 , 1 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Properties' , 'filter' , 'ppPropColl' , ), 101, (101, (), [ (12, 17, None, None) , 
			 (16393, 10, None, "IID('{FA1219FB-D82D-47B6-815F-F786F347E6E6}')") , ], 1 , 2 , 4 , 1 , 216 , (3, 0, None, None) , 0 , )),
	(( 'PutProperty' , 'key' , 'value' , 'ppProp' , ), 102, (102, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (16393, 10, None, "IID('{6ABBB0DE-2FAC-45DB-90CA-E90A630B0FBB}')") , ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrVariantInfoRecs_vtables_dispatch_ = 1
IMGCVariantMgrVariantInfoRecs_vtables_ = [
	(( 'Item' , 'index' , 'ppVariantInfoRec' , ), 101, (101, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{162B6B80-35C5-4FE7-A1C8-62D9FE3DADD3}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'pSymbIRec' , ), 102, (102, (), [ (9, 1, None, "IID('{162B6B80-35C5-4FE7-A1C8-62D9FE3DADD3}')") , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrVariantInfoRecsUtility_vtables_dispatch_ = 1
IMGCVariantMgrVariantInfoRecsUtility_vtables_ = [
	(( 'FindVariantInfoRec' , 'variantSpec' , 'ppObj' , ), 101, (101, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{162B6B80-35C5-4FE7-A1C8-62D9FE3DADD3}')") , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrVariantMapping_vtables_dispatch_ = 1
IMGCVariantMgrVariantMapping_vtables_ = [
	(( 'OriginalName' , 'valStr' , ), 100, (100, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'OriginalName' , 'valStr' , ), 100, (100, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'NewName' , 'valStr' , ), 101, (101, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'NewName' , 'valStr' , ), 101, (101, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'MappingFlags' , 'value' , ), 102, (102, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'MappingFlags' , 'value' , ), 102, (102, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrVariantMappings_vtables_dispatch_ = 1
IMGCVariantMgrVariantMappings_vtables_ = [
	(( 'Item' , 'index' , 'ppVariantMapping' , ), 101, (101, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{746F9DCE-E85C-4BA5-BE14-FEF24731222A}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'pVariantMapping' , ), 102, (102, (), [ (9, 1, None, "IID('{746F9DCE-E85C-4BA5-BE14-FEF24731222A}')") , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
]

IMGCVariantMgrVariants_vtables_dispatch_ = 1
IMGCVariantMgrVariants_vtables_ = [
	(( 'Item' , 'index' , 'ppVariant' , ), 101, (101, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{78663802-9407-11D2-89D9-0020184077E1}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'pVariant' , ), 102, (102, (), [ (9, 1, None, "IID('{78663802-9407-11D2-89D9-0020184077E1}')") , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
]

ITest_vtables_dispatch_ = 1
ITest_vtables_ = [
]

_IMGCVariantMgrBaseDummy_vtables_dispatch_ = 1
_IMGCVariantMgrBaseDummy_vtables_ = [
]

RecordMap = {
}

CLSIDToClassMap = {
	'{C68512CD-1296-48BC-A69D-B7DFF5816DA5}' : IMGCVariantMgrParent,
	'{78663807-9407-11D2-89D9-0020184077E1}' : IMGCVariantMgrDocument,
	'{82CD5AB9-9407-11D2-89D9-0020184077E1}' : IMGCVariantMgrBaseModNameObject,
	'{786637EF-9407-11D2-89D9-0020184077E1}' : IMGCVariantMgrBaseModObject,
	'{786637F0-9407-11D2-89D9-0020184077E1}' : IMGCVariantMgrBaseObject,
	'{786637FC-9407-11D2-89D9-0020184077E1}' : IMGCVariantMgrFMVFunctions,
	'{786637F1-9407-11D2-89D9-0020184077E1}' : IMGCVariantMgrBaseCollection,
	'{786637FB-9407-11D2-89D9-0020184077E1}' : IMGCVariantMgrFMVFunction,
	'{7255B70F-5A93-4770-8D66-A32C07310BA1}' : IMGCVariantMgrVariantAssignments,
	'{874DEFFA-9480-4725-BCE3-06FE0427B1CA}' : IMGCVariantMgrVariantAssignment,
	'{78663802-9407-11D2-89D9-0020184077E1}' : IMGCVariantMgrVariant,
	'{786637FE-9407-11D2-89D9-0020184077E1}' : IMGCVariantMgrPackageModifications,
	'{786637FD-9407-11D2-89D9-0020184077E1}' : IMGCVariantMgrPackageModification,
	'{786637F5-9407-11D2-89D9-0020184077E1}' : IMGCVariantMgrPackage,
	'{786637F7-9407-11D2-89D9-0020184077E1}' : IMGCVariantMgrSymbols,
	'{786637F4-9407-11D2-89D9-0020184077E1}' : IMGCVariantMgrSymbol,
	'{786637F3-9407-11D2-89D9-0020184077E1}' : IMGCVariantMgrSymbolLocation,
	'{E2CD1C5F-0EE9-4349-B08A-FA34A84CB2F1}' : IMGCVariantMgrBlock,
	'{D1B4AC05-40EE-4F0E-8C27-49D6BEC83908}' : IMGCVariantMgrBaseBlock,
	'{7FE7FAB6-7B3B-46CB-970A-0010103AD7E3}' : IMGCVariantMgrBlockData,
	'{786637F6-9407-11D2-89D9-0020184077E1}' : IMGCVariantMgrPackages,
	'{F74277DE-9533-4D61-A84B-44D4A326B316}' : IMGCVariantMgrBlocks,
	'{82CD5AA5-9407-11D2-89D9-0020184077E1}' : IMGCVariantMgrReusedBlocks,
	'{82CD5AA4-9407-11D2-89D9-0020184077E1}' : IMGCVariantMgrReusedBlock,
	'{5F5FA27B-9A28-4A84-BE9A-7460F1D6D54B}' : IMGCVariantMgrVariantMappings,
	'{746F9DCE-E85C-4BA5-BE14-FEF24731222A}' : IMGCVariantMgrVariantMapping,
	'{78663803-9407-11D2-89D9-0020184077E1}' : IMGCVariantMgrVariants,
	'{82CD5AA6-9407-11D2-89D9-0020184077E1}' : IMGCVariantMgrConnectivity,
	'{786637F8-9407-11D2-89D9-0020184077E1}' : IMGCVariantMgrSymbolLocations,
	'{98301621-82F9-4458-996F-46739708B82C}' : IMGCVariantMgrEquivalentBlockGroups,
	'{4FC18EAE-75C9-4A49-9E38-20ADD79456B5}' : IMGCVariantMgrEquivalentBlockGroup,
	'{AA3E0FAD-2AD6-4FE3-93CC-98A117DC9F0D}' : IMGCVariantMgrEquivalentBlock,
	'{CD2C5AF6-5000-4C95-9879-2F7FB2BA85DD}' : IMGCVariantMgrEquivalentBlocks,
	'{82CD5AA7-9407-11D2-89D9-0020184077E1}' : IMGCVariantMgrGroupings,
	'{AF197ECE-D3D5-4720-AB62-F3F2E0CB52F4}' : IMGCVariantMgrFMVFunctionGroups,
	'{6320E666-2421-4912-AEE9-CFC712EE05C0}' : IMGCVariantMgrFMVFunctionGroup,
	'{BFA4726B-E7D0-48E5-A73A-B5C216E8A3BA}' : IMGCVariantMgrBaseGroup,
	'{58977901-B0FA-491B-9F30-75EBA4E8D3C8}' : IMGCVariantMgrFMVFunctionAssignments,
	'{B531AD99-09B2-4D15-AC0D-8F3A75F64A14}' : IMGCVariantMgrFMVFunctionAssignment,
	'{19DBCD8C-D9AF-4B85-8439-89F12F23F406}' : IMGCVariantMgrVariantGroups,
	'{3809BA4C-72E2-436F-B258-88EBA46444C8}' : IMGCVariantMgrVariantGroup,
	'{7866380B-9407-11D2-89D9-0020184077E1}' : IMGCVariantMgrSettings,
	'{8F683CE7-08DB-45B8-B4EA-E27982CF0995}' : IMGCVariantMgrStatistics,
	'{CA185E0D-76D0-43D5-A215-F301941E074F}' : IMGCVariantMgrReuseSettings,
	'{EE5CB44B-13CF-480C-B096-5A2D731A9535}' : IMGCVariantMgrUtility,
	'{C9D96C16-A541-4DA9-97E0-902FCD6C2412}' : IMGCVariantMgrFilters,
	'{7E1CD29C-D3B5-4690-91D5-415965F42BA6}' : IMGCVariantMgrPackageModificationFilter,
	'{761BC783-46D2-4961-835B-653901ED7E7F}' : IMGCVariantMgrBlockDataModificationFilter,
	'{B01F00BE-D881-46C2-B841-82D35B117ED4}' : IMGCVariantMgrPackageFilter,
	'{1158040D-F8C4-4865-A4A6-F42D11C258BA}' : IMGCVariantMgrBorderPropModificationFilter,
	'{9ADE593A-D453-4433-B7EF-281D82D31EAD}' : IMGCVariantMgrSymbolFilter,
	'{017BAF92-95BB-4AD2-BCF6-43DC7A60BAA8}' : IMGCVariantMgrReporter,
	'{353E3059-2914-4F62-AD38-D61BD61F620F}' : IMGCVariantMgrReporterSettings,
	'{9E5DF0FC-CE34-409A-B257-AD8E39BBD95E}' : IMGCVariantMgrReporterDataMatrix,
	'{F22A8EE1-16C5-47E6-A722-C17868D6B486}' : IMGCVariantMgrMessageMgr,
	'{D391142F-058C-49E2-85CF-30DA3D2886BA}' : IMGCVariantMgrPModsUtility,
	'{5F556342-9E5E-4B96-9002-9B148BA114DD}' : IMGCVariantMgrBlockDataModification,
	'{45742780-B379-49F9-8431-16CB70520F9C}' : IMGCVariantMgrBlockDataModifications,
	'{7D8CEF26-776A-40B2-A99C-C6B2358E0C60}' : IMGCVariantMgrSInfoRecsUtility,
	'{A6C3A4DE-6048-492D-AA03-EC268CCC73D4}' : IMGCVariantMgrSymbolInfoRecs,
	'{A34D9F27-362F-45AA-9F73-CBC28DF7645E}' : IMGCVariantMgrSymbolInfoRec,
	'{3C44AB05-4C95-4984-BD98-135CDD2B39C1}' : IMGCVariantMgrFMVProperties,
	'{DD445D35-DC4B-413A-8781-F561D40D4CC5}' : IMGCVariantMgrFMVProperty,
	'{138F998B-642F-436E-BEA2-986E1B29A353}' : IMGCVariantMgrVariantInfoRecsUtility,
	'{162B6B80-35C5-4FE7-A1C8-62D9FE3DADD3}' : IMGCVariantMgrVariantInfoRec,
	'{FA1219FB-D82D-47B6-815F-F786F347E6E6}' : IMGCVariantMgrProperties,
	'{6ABBB0DE-2FAC-45DB-90CA-E90A630B0FBB}' : IMGCVariantMgrProperty,
	'{BC1CC3A2-E4A4-4A3D-B400-50F80D7D8A39}' : IMGCVariantMgrBPropModsUtility,
	'{22D9A8DA-F507-43FD-BA22-6DB8FEA436F2}' : IMGCVariantMgrBorderPropModification,
	'{72982CC0-8617-400A-9772-5DF126EA582A}' : IMGCVariantMgrBorderPropModifications,
	'{DA637EAA-704A-4A97-9C0E-F7B4D07751E2}' : _IMGCVariantMgrBaseDummy,
	'{82CD5AB8-9407-11D2-89D9-0020184077E1}' : IMGCVariantMgrBaseNameObject,
	'{F7FF7F27-3A87-458B-9C36-934DBF14A287}' : IMGCVariantMgrVariantInfoRecs,
	'{82CD5AAF-9407-11D2-89D9-0020184077E1}' : IMGCVariantMgrParameter,
	'{82CD5AB0-9407-11D2-89D9-0020184077E1}' : IMGCVariantMgrParameters,
	'{82CD5AB1-9407-11D2-89D9-0020184077E1}' : IMGCVariantMgrOutputGenerator,
	'{82CD5AB2-9407-11D2-89D9-0020184077E1}' : IMGCVariantMgrEquivPartsSettings,
	'{D9AA5BF5-2389-40CA-9E58-8A7A59B2AF31}' : IMGCVariantMgrUID,
	'{7866380E-9407-11D2-89D9-0020184077E1}' : IMGCVariantMgrDocuments,
	'{7866380D-9407-11D2-89D9-0020184077E1}' : IMGCVariantMgrApplication,
	'{34842ABE-9E81-4B7D-A5D3-35C68F327A36}' : IMGCVariantMgrEditors,
	'{82CD5AAD-9407-11D2-89D9-0020184077E1}' : IMGCVariantMgrEditor,
	'{8ADA56FC-3345-41CA-B16B-AB446D82790D}' : ITest,
	'{FFD61045-44FD-4F80-995C-6C6F0AE1DEB0}' : _IMGCVariantMgrDocumentEvents,
	'{786637F3-9407-20D2-89D9-0020184077E1}' : SymbolLocation,
	'{786637F8-9407-20D2-89D9-0020184077E1}' : SymbolLocations,
	'{786637F4-9407-20D2-89D9-0020184077E1}' : Symbol,
	'{786637F7-9407-20D2-89D9-0020184077E1}' : Symbols,
	'{786637F5-9407-20D2-89D9-0020184077E1}' : Package,
	'{786637F6-9407-20D2-89D9-0020184077E1}' : Packages,
	'{1CA65166-6233-45DE-A7F9-8327E263DBA5}' : PackageFilter,
	'{82CD5AA8-9407-11D2-89D9-0020184077E1}' : ReusedBlock,
	'{82CD5AA9-9407-11D2-89D9-0020184077E1}' : ReusedBlocks,
	'{463130F2-CF4B-49B8-9376-FD86C3AECA74}' : Block,
	'{1AEE4AD1-C054-4533-BF0E-1D6ED8BBD173}' : BlockData,
	'{BE31CD71-78CF-4C67-A875-77F5E1297B47}' : Blocks,
	'{C8379667-6E7B-4C72-ADA1-EB298F1019EF}' : EquivalentBlock,
	'{3E00E7A9-47FF-4E25-B76E-BECE98E42007}' : EquivalentBlocks,
	'{9E3B1A5B-EE91-4D46-A4C9-C08E93177145}' : EquivalentBlockGroup,
	'{710F3F51-7D50-4A3C-B171-E9F1BBBF5530}' : EquivalentBlockGroups,
	'{82CD5AAA-9407-11D2-89D9-0020184077E1}' : Connectivity,
	'{82CD5AAB-9407-11D2-89D9-0020184077E1}' : Groupings,
	'{786637FB-9407-20D2-89D9-0020184077E1}' : FMVFunction,
	'{786637FC-9407-20D2-89D9-0020184077E1}' : FMVFunctions,
	'{82CD5AAE-9407-11D2-89D9-0020184077E1}' : Editor,
	'{FFA514B3-BAE3-4AF0-8611-E2FF01E3C9D1}' : Editors,
	'{78663802-9407-20D2-89D9-0020184077E1}' : Variant,
	'{78663803-9407-20D2-89D9-0020184077E1}' : Variants,
	'{9424AF28-132F-4123-9124-395F25BD960B}' : VariantMapping,
	'{47653D5E-3982-45EE-8711-A5130875EB1C}' : VariantMappings,
	'{82CD5AB6-9407-11D2-89D9-0020184077E1}' : OutputGenerator,
	'{26D8C861-04AF-4273-9875-A8EF996FD14B}' : PackageModificationFilter,
	'{786637FD-9407-20D2-89D9-0020184077E1}' : PackageModification,
	'{786637FE-9407-20D2-89D9-0020184077E1}' : PackageModifications,
	'{0397654E-7091-4683-9FF8-D064B20281FB}' : BlockDataModificationFilter,
	'{6DA2DE93-5489-4171-BAD6-E836390A07C2}' : BlockDataModification,
	'{19BDB78E-F30F-4F0E-A43E-E87E33F9995D}' : BlockDataModifications,
	'{C1027159-081D-460B-9420-DC3A23ACE84D}' : BorderPropModificationFilter,
	'{F7DCE892-A986-480A-9A79-26879868C4C2}' : BorderPropModification,
	'{A1C6B0A5-F25F-41EC-BBB7-F4CE90E80F41}' : BorderPropModifications,
	'{17760C13-0FFB-4577-A56E-4A558EAD2B31}' : VariantInfoRec,
	'{4E6C1C8E-542F-4561-ADD3-ADA3C4E2B323}' : VariantInfoRecs,
	'{68DE764E-F9B0-4B22-897E-CB0392034977}' : SymbolInfoRec,
	'{B1A416FE-D9E6-4653-B05F-DE31BFE31772}' : SymbolInfoRecs,
	'{F15DA467-46F8-449D-97B4-0C929B7DF4E8}' : VariantGroup,
	'{C65DD74F-E63D-4B2C-BF64-932CEA392102}' : VariantGroups,
	'{5E7CEF6B-E5A9-452B-B757-7ABA3826CBD3}' : FMVFunctionGroup,
	'{E30ED752-1FD3-4294-AE8D-E8C96944F104}' : FMVFunctionGroups,
	'{C1F669F9-84C7-480A-AF88-6A601077674A}' : VariantAssignment,
	'{5A99035D-F675-4DE5-9A15-9EB193E5B9FE}' : VariantAssignments,
	'{6E1379A7-5ADF-4FCE-AF36-168E470CF199}' : FMVFunctionAssignment,
	'{ED096F00-ED2B-468F-9E18-C01EF9CB2BEA}' : FMVFunctionAssignments,
	'{8B45CE2D-6CF5-1014-857A-77B9EECCF0AC}' : Document,
	'{C1453F6A-07E7-42F1-B7A6-1F6B698798E6}' : _DocumentEvents,
	'{7866380E-9407-20D2-89D9-0020184077E1}' : Documents,
	'{8B707D43-7C93-4D09-BE09-EE1B0498E345}' : Reporter,
	'{22912830-6A46-4B8E-998C-1812ABCEEC4E}' : ReporterSettings,
	'{1E60DA28-0E2A-4C52-9432-575F66713702}' : ReporterDataMatrix,
	'{332154D8-A5F8-41A2-BE78-2841D50143F6}' : Statistics,
	'{E08A46A8-C405-4073-ABB1-FB2B94A45C5F}' : Utility,
	'{09EDE838-98B4-4D93-A40C-3F43E642EAE1}' : Filters,
	'{82CD5AB3-9407-11D2-89D9-0020184077E1}' : Parameter,
	'{82CD5AB4-9407-11D2-89D9-0020184077E1}' : Parameters,
	'{82CD5AB5-9407-11D2-89D9-0020184077E1}' : EquivPartsSettings,
	'{86B24400-555D-49A9-BD72-49260A34A59C}' : MessageMgr,
	'{7866380B-9407-20D2-89D9-0020184077E1}' : Settings,
	'{2CA0D3A4-696A-4927-85D6-D0421E343252}' : ReuseSettings,
	'{7B540F5C-2F96-4EEE-8894-F4970320B0D4}' : FMVProperty,
	'{91CE081D-69DF-4940-B2E0-4F304D4E8E62}' : FMVProperties,
	'{7866380D-9407-20D2-89D9-0020184077E1}' : Application,
	'{B15661E9-0393-42DE-A5C4-4EA1C899AF71}' : SInfoRecsUtility,
	'{180960C2-CD47-4C0C-B446-8C558D69CA0E}' : VariantInfoRecsUtility,
	'{5455892B-A0D3-498F-97D2-4C3F243B276E}' : PModsUtility,
	'{8B45CF63-6CF5-1014-857A-77B9EECCF0AC}' : UID,
	'{4BCB2183-E92C-4465-8652-62AE02E8672A}' : VMProperty,
	'{1101A6F0-EA66-43DC-849E-906E36A0A734}' : VMProperties,
	'{9664D362-EAD1-41A5-B465-7D71FE1527F1}' : BPropModsUtility,
	'{3D8BA603-4843-461C-8153-D64FE1DF8380}' : SymbolFilter,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
	'{C68512CD-1296-48BC-A69D-B7DFF5816DA5}' : 'IMGCVariantMgrParent',
	'{78663807-9407-11D2-89D9-0020184077E1}' : 'IMGCVariantMgrDocument',
	'{82CD5AB9-9407-11D2-89D9-0020184077E1}' : 'IMGCVariantMgrBaseModNameObject',
	'{786637EF-9407-11D2-89D9-0020184077E1}' : 'IMGCVariantMgrBaseModObject',
	'{786637F0-9407-11D2-89D9-0020184077E1}' : 'IMGCVariantMgrBaseObject',
	'{786637FC-9407-11D2-89D9-0020184077E1}' : 'IMGCVariantMgrFMVFunctions',
	'{786637F1-9407-11D2-89D9-0020184077E1}' : 'IMGCVariantMgrBaseCollection',
	'{786637FB-9407-11D2-89D9-0020184077E1}' : 'IMGCVariantMgrFMVFunction',
	'{7255B70F-5A93-4770-8D66-A32C07310BA1}' : 'IMGCVariantMgrVariantAssignments',
	'{874DEFFA-9480-4725-BCE3-06FE0427B1CA}' : 'IMGCVariantMgrVariantAssignment',
	'{78663802-9407-11D2-89D9-0020184077E1}' : 'IMGCVariantMgrVariant',
	'{786637FE-9407-11D2-89D9-0020184077E1}' : 'IMGCVariantMgrPackageModifications',
	'{786637FD-9407-11D2-89D9-0020184077E1}' : 'IMGCVariantMgrPackageModification',
	'{786637F5-9407-11D2-89D9-0020184077E1}' : 'IMGCVariantMgrPackage',
	'{786637F7-9407-11D2-89D9-0020184077E1}' : 'IMGCVariantMgrSymbols',
	'{786637F4-9407-11D2-89D9-0020184077E1}' : 'IMGCVariantMgrSymbol',
	'{786637F3-9407-11D2-89D9-0020184077E1}' : 'IMGCVariantMgrSymbolLocation',
	'{E2CD1C5F-0EE9-4349-B08A-FA34A84CB2F1}' : 'IMGCVariantMgrBlock',
	'{D1B4AC05-40EE-4F0E-8C27-49D6BEC83908}' : 'IMGCVariantMgrBaseBlock',
	'{7FE7FAB6-7B3B-46CB-970A-0010103AD7E3}' : 'IMGCVariantMgrBlockData',
	'{786637F6-9407-11D2-89D9-0020184077E1}' : 'IMGCVariantMgrPackages',
	'{F74277DE-9533-4D61-A84B-44D4A326B316}' : 'IMGCVariantMgrBlocks',
	'{82CD5AA5-9407-11D2-89D9-0020184077E1}' : 'IMGCVariantMgrReusedBlocks',
	'{82CD5AA4-9407-11D2-89D9-0020184077E1}' : 'IMGCVariantMgrReusedBlock',
	'{5F5FA27B-9A28-4A84-BE9A-7460F1D6D54B}' : 'IMGCVariantMgrVariantMappings',
	'{746F9DCE-E85C-4BA5-BE14-FEF24731222A}' : 'IMGCVariantMgrVariantMapping',
	'{78663803-9407-11D2-89D9-0020184077E1}' : 'IMGCVariantMgrVariants',
	'{82CD5AA6-9407-11D2-89D9-0020184077E1}' : 'IMGCVariantMgrConnectivity',
	'{786637F8-9407-11D2-89D9-0020184077E1}' : 'IMGCVariantMgrSymbolLocations',
	'{98301621-82F9-4458-996F-46739708B82C}' : 'IMGCVariantMgrEquivalentBlockGroups',
	'{4FC18EAE-75C9-4A49-9E38-20ADD79456B5}' : 'IMGCVariantMgrEquivalentBlockGroup',
	'{AA3E0FAD-2AD6-4FE3-93CC-98A117DC9F0D}' : 'IMGCVariantMgrEquivalentBlock',
	'{CD2C5AF6-5000-4C95-9879-2F7FB2BA85DD}' : 'IMGCVariantMgrEquivalentBlocks',
	'{82CD5AA7-9407-11D2-89D9-0020184077E1}' : 'IMGCVariantMgrGroupings',
	'{AF197ECE-D3D5-4720-AB62-F3F2E0CB52F4}' : 'IMGCVariantMgrFMVFunctionGroups',
	'{6320E666-2421-4912-AEE9-CFC712EE05C0}' : 'IMGCVariantMgrFMVFunctionGroup',
	'{BFA4726B-E7D0-48E5-A73A-B5C216E8A3BA}' : 'IMGCVariantMgrBaseGroup',
	'{58977901-B0FA-491B-9F30-75EBA4E8D3C8}' : 'IMGCVariantMgrFMVFunctionAssignments',
	'{B531AD99-09B2-4D15-AC0D-8F3A75F64A14}' : 'IMGCVariantMgrFMVFunctionAssignment',
	'{19DBCD8C-D9AF-4B85-8439-89F12F23F406}' : 'IMGCVariantMgrVariantGroups',
	'{3809BA4C-72E2-436F-B258-88EBA46444C8}' : 'IMGCVariantMgrVariantGroup',
	'{7866380B-9407-11D2-89D9-0020184077E1}' : 'IMGCVariantMgrSettings',
	'{8F683CE7-08DB-45B8-B4EA-E27982CF0995}' : 'IMGCVariantMgrStatistics',
	'{CA185E0D-76D0-43D5-A215-F301941E074F}' : 'IMGCVariantMgrReuseSettings',
	'{EE5CB44B-13CF-480C-B096-5A2D731A9535}' : 'IMGCVariantMgrUtility',
	'{C9D96C16-A541-4DA9-97E0-902FCD6C2412}' : 'IMGCVariantMgrFilters',
	'{7E1CD29C-D3B5-4690-91D5-415965F42BA6}' : 'IMGCVariantMgrPackageModificationFilter',
	'{761BC783-46D2-4961-835B-653901ED7E7F}' : 'IMGCVariantMgrBlockDataModificationFilter',
	'{B01F00BE-D881-46C2-B841-82D35B117ED4}' : 'IMGCVariantMgrPackageFilter',
	'{1158040D-F8C4-4865-A4A6-F42D11C258BA}' : 'IMGCVariantMgrBorderPropModificationFilter',
	'{9ADE593A-D453-4433-B7EF-281D82D31EAD}' : 'IMGCVariantMgrSymbolFilter',
	'{017BAF92-95BB-4AD2-BCF6-43DC7A60BAA8}' : 'IMGCVariantMgrReporter',
	'{353E3059-2914-4F62-AD38-D61BD61F620F}' : 'IMGCVariantMgrReporterSettings',
	'{9E5DF0FC-CE34-409A-B257-AD8E39BBD95E}' : 'IMGCVariantMgrReporterDataMatrix',
	'{F22A8EE1-16C5-47E6-A722-C17868D6B486}' : 'IMGCVariantMgrMessageMgr',
	'{D391142F-058C-49E2-85CF-30DA3D2886BA}' : 'IMGCVariantMgrPModsUtility',
	'{5F556342-9E5E-4B96-9002-9B148BA114DD}' : 'IMGCVariantMgrBlockDataModification',
	'{45742780-B379-49F9-8431-16CB70520F9C}' : 'IMGCVariantMgrBlockDataModifications',
	'{7D8CEF26-776A-40B2-A99C-C6B2358E0C60}' : 'IMGCVariantMgrSInfoRecsUtility',
	'{A6C3A4DE-6048-492D-AA03-EC268CCC73D4}' : 'IMGCVariantMgrSymbolInfoRecs',
	'{A34D9F27-362F-45AA-9F73-CBC28DF7645E}' : 'IMGCVariantMgrSymbolInfoRec',
	'{3C44AB05-4C95-4984-BD98-135CDD2B39C1}' : 'IMGCVariantMgrFMVProperties',
	'{DD445D35-DC4B-413A-8781-F561D40D4CC5}' : 'IMGCVariantMgrFMVProperty',
	'{138F998B-642F-436E-BEA2-986E1B29A353}' : 'IMGCVariantMgrVariantInfoRecsUtility',
	'{162B6B80-35C5-4FE7-A1C8-62D9FE3DADD3}' : 'IMGCVariantMgrVariantInfoRec',
	'{FA1219FB-D82D-47B6-815F-F786F347E6E6}' : 'IMGCVariantMgrProperties',
	'{6ABBB0DE-2FAC-45DB-90CA-E90A630B0FBB}' : 'IMGCVariantMgrProperty',
	'{BC1CC3A2-E4A4-4A3D-B400-50F80D7D8A39}' : 'IMGCVariantMgrBPropModsUtility',
	'{22D9A8DA-F507-43FD-BA22-6DB8FEA436F2}' : 'IMGCVariantMgrBorderPropModification',
	'{72982CC0-8617-400A-9772-5DF126EA582A}' : 'IMGCVariantMgrBorderPropModifications',
	'{DA637EAA-704A-4A97-9C0E-F7B4D07751E2}' : '_IMGCVariantMgrBaseDummy',
	'{82CD5AB8-9407-11D2-89D9-0020184077E1}' : 'IMGCVariantMgrBaseNameObject',
	'{F7FF7F27-3A87-458B-9C36-934DBF14A287}' : 'IMGCVariantMgrVariantInfoRecs',
	'{82CD5AAF-9407-11D2-89D9-0020184077E1}' : 'IMGCVariantMgrParameter',
	'{82CD5AB0-9407-11D2-89D9-0020184077E1}' : 'IMGCVariantMgrParameters',
	'{82CD5AB1-9407-11D2-89D9-0020184077E1}' : 'IMGCVariantMgrOutputGenerator',
	'{82CD5AB2-9407-11D2-89D9-0020184077E1}' : 'IMGCVariantMgrEquivPartsSettings',
	'{D9AA5BF5-2389-40CA-9E58-8A7A59B2AF31}' : 'IMGCVariantMgrUID',
	'{7866380E-9407-11D2-89D9-0020184077E1}' : 'IMGCVariantMgrDocuments',
	'{7866380D-9407-11D2-89D9-0020184077E1}' : 'IMGCVariantMgrApplication',
	'{34842ABE-9E81-4B7D-A5D3-35C68F327A36}' : 'IMGCVariantMgrEditors',
	'{82CD5AAD-9407-11D2-89D9-0020184077E1}' : 'IMGCVariantMgrEditor',
	'{8ADA56FC-3345-41CA-B16B-AB446D82790D}' : 'ITest',
}


NamesToIIDMap = {
	'IMGCVariantMgrParent' : '{C68512CD-1296-48BC-A69D-B7DFF5816DA5}',
	'IMGCVariantMgrDocument' : '{78663807-9407-11D2-89D9-0020184077E1}',
	'IMGCVariantMgrBaseModNameObject' : '{82CD5AB9-9407-11D2-89D9-0020184077E1}',
	'IMGCVariantMgrBaseModObject' : '{786637EF-9407-11D2-89D9-0020184077E1}',
	'IMGCVariantMgrBaseObject' : '{786637F0-9407-11D2-89D9-0020184077E1}',
	'IMGCVariantMgrFMVFunctions' : '{786637FC-9407-11D2-89D9-0020184077E1}',
	'IMGCVariantMgrBaseCollection' : '{786637F1-9407-11D2-89D9-0020184077E1}',
	'IMGCVariantMgrFMVFunction' : '{786637FB-9407-11D2-89D9-0020184077E1}',
	'IMGCVariantMgrVariantAssignments' : '{7255B70F-5A93-4770-8D66-A32C07310BA1}',
	'IMGCVariantMgrVariantAssignment' : '{874DEFFA-9480-4725-BCE3-06FE0427B1CA}',
	'IMGCVariantMgrVariant' : '{78663802-9407-11D2-89D9-0020184077E1}',
	'IMGCVariantMgrPackageModifications' : '{786637FE-9407-11D2-89D9-0020184077E1}',
	'IMGCVariantMgrPackageModification' : '{786637FD-9407-11D2-89D9-0020184077E1}',
	'IMGCVariantMgrPackage' : '{786637F5-9407-11D2-89D9-0020184077E1}',
	'IMGCVariantMgrSymbols' : '{786637F7-9407-11D2-89D9-0020184077E1}',
	'IMGCVariantMgrSymbol' : '{786637F4-9407-11D2-89D9-0020184077E1}',
	'IMGCVariantMgrSymbolLocation' : '{786637F3-9407-11D2-89D9-0020184077E1}',
	'IMGCVariantMgrBlock' : '{E2CD1C5F-0EE9-4349-B08A-FA34A84CB2F1}',
	'IMGCVariantMgrBaseBlock' : '{D1B4AC05-40EE-4F0E-8C27-49D6BEC83908}',
	'IMGCVariantMgrBlockData' : '{7FE7FAB6-7B3B-46CB-970A-0010103AD7E3}',
	'IMGCVariantMgrPackages' : '{786637F6-9407-11D2-89D9-0020184077E1}',
	'IMGCVariantMgrBlocks' : '{F74277DE-9533-4D61-A84B-44D4A326B316}',
	'IMGCVariantMgrReusedBlocks' : '{82CD5AA5-9407-11D2-89D9-0020184077E1}',
	'IMGCVariantMgrReusedBlock' : '{82CD5AA4-9407-11D2-89D9-0020184077E1}',
	'IMGCVariantMgrVariantMappings' : '{5F5FA27B-9A28-4A84-BE9A-7460F1D6D54B}',
	'IMGCVariantMgrVariantMapping' : '{746F9DCE-E85C-4BA5-BE14-FEF24731222A}',
	'IMGCVariantMgrVariants' : '{78663803-9407-11D2-89D9-0020184077E1}',
	'IMGCVariantMgrConnectivity' : '{82CD5AA6-9407-11D2-89D9-0020184077E1}',
	'IMGCVariantMgrSymbolLocations' : '{786637F8-9407-11D2-89D9-0020184077E1}',
	'IMGCVariantMgrEquivalentBlockGroups' : '{98301621-82F9-4458-996F-46739708B82C}',
	'IMGCVariantMgrEquivalentBlockGroup' : '{4FC18EAE-75C9-4A49-9E38-20ADD79456B5}',
	'IMGCVariantMgrEquivalentBlock' : '{AA3E0FAD-2AD6-4FE3-93CC-98A117DC9F0D}',
	'IMGCVariantMgrEquivalentBlocks' : '{CD2C5AF6-5000-4C95-9879-2F7FB2BA85DD}',
	'IMGCVariantMgrGroupings' : '{82CD5AA7-9407-11D2-89D9-0020184077E1}',
	'IMGCVariantMgrFMVFunctionGroups' : '{AF197ECE-D3D5-4720-AB62-F3F2E0CB52F4}',
	'IMGCVariantMgrFMVFunctionGroup' : '{6320E666-2421-4912-AEE9-CFC712EE05C0}',
	'IMGCVariantMgrBaseGroup' : '{BFA4726B-E7D0-48E5-A73A-B5C216E8A3BA}',
	'IMGCVariantMgrFMVFunctionAssignments' : '{58977901-B0FA-491B-9F30-75EBA4E8D3C8}',
	'IMGCVariantMgrFMVFunctionAssignment' : '{B531AD99-09B2-4D15-AC0D-8F3A75F64A14}',
	'IMGCVariantMgrVariantGroups' : '{19DBCD8C-D9AF-4B85-8439-89F12F23F406}',
	'IMGCVariantMgrVariantGroup' : '{3809BA4C-72E2-436F-B258-88EBA46444C8}',
	'IMGCVariantMgrSettings' : '{7866380B-9407-11D2-89D9-0020184077E1}',
	'IMGCVariantMgrStatistics' : '{8F683CE7-08DB-45B8-B4EA-E27982CF0995}',
	'IMGCVariantMgrReuseSettings' : '{CA185E0D-76D0-43D5-A215-F301941E074F}',
	'IMGCVariantMgrUtility' : '{EE5CB44B-13CF-480C-B096-5A2D731A9535}',
	'IMGCVariantMgrFilters' : '{C9D96C16-A541-4DA9-97E0-902FCD6C2412}',
	'IMGCVariantMgrPackageModificationFilter' : '{7E1CD29C-D3B5-4690-91D5-415965F42BA6}',
	'IMGCVariantMgrBlockDataModificationFilter' : '{761BC783-46D2-4961-835B-653901ED7E7F}',
	'IMGCVariantMgrPackageFilter' : '{B01F00BE-D881-46C2-B841-82D35B117ED4}',
	'IMGCVariantMgrBorderPropModificationFilter' : '{1158040D-F8C4-4865-A4A6-F42D11C258BA}',
	'IMGCVariantMgrSymbolFilter' : '{9ADE593A-D453-4433-B7EF-281D82D31EAD}',
	'IMGCVariantMgrReporter' : '{017BAF92-95BB-4AD2-BCF6-43DC7A60BAA8}',
	'IMGCVariantMgrReporterSettings' : '{353E3059-2914-4F62-AD38-D61BD61F620F}',
	'IMGCVariantMgrReporterDataMatrix' : '{9E5DF0FC-CE34-409A-B257-AD8E39BBD95E}',
	'IMGCVariantMgrMessageMgr' : '{F22A8EE1-16C5-47E6-A722-C17868D6B486}',
	'IMGCVariantMgrPModsUtility' : '{D391142F-058C-49E2-85CF-30DA3D2886BA}',
	'IMGCVariantMgrBlockDataModification' : '{5F556342-9E5E-4B96-9002-9B148BA114DD}',
	'IMGCVariantMgrBlockDataModifications' : '{45742780-B379-49F9-8431-16CB70520F9C}',
	'IMGCVariantMgrSInfoRecsUtility' : '{7D8CEF26-776A-40B2-A99C-C6B2358E0C60}',
	'IMGCVariantMgrSymbolInfoRecs' : '{A6C3A4DE-6048-492D-AA03-EC268CCC73D4}',
	'IMGCVariantMgrSymbolInfoRec' : '{A34D9F27-362F-45AA-9F73-CBC28DF7645E}',
	'IMGCVariantMgrFMVProperties' : '{3C44AB05-4C95-4984-BD98-135CDD2B39C1}',
	'IMGCVariantMgrFMVProperty' : '{DD445D35-DC4B-413A-8781-F561D40D4CC5}',
	'IMGCVariantMgrVariantInfoRecsUtility' : '{138F998B-642F-436E-BEA2-986E1B29A353}',
	'IMGCVariantMgrVariantInfoRec' : '{162B6B80-35C5-4FE7-A1C8-62D9FE3DADD3}',
	'IMGCVariantMgrProperties' : '{FA1219FB-D82D-47B6-815F-F786F347E6E6}',
	'IMGCVariantMgrProperty' : '{6ABBB0DE-2FAC-45DB-90CA-E90A630B0FBB}',
	'IMGCVariantMgrBPropModsUtility' : '{BC1CC3A2-E4A4-4A3D-B400-50F80D7D8A39}',
	'IMGCVariantMgrBorderPropModification' : '{22D9A8DA-F507-43FD-BA22-6DB8FEA436F2}',
	'IMGCVariantMgrBorderPropModifications' : '{72982CC0-8617-400A-9772-5DF126EA582A}',
	'_IMGCVariantMgrBaseDummy' : '{DA637EAA-704A-4A97-9C0E-F7B4D07751E2}',
	'IMGCVariantMgrBaseNameObject' : '{82CD5AB8-9407-11D2-89D9-0020184077E1}',
	'IMGCVariantMgrVariantInfoRecs' : '{F7FF7F27-3A87-458B-9C36-934DBF14A287}',
	'IMGCVariantMgrParameter' : '{82CD5AAF-9407-11D2-89D9-0020184077E1}',
	'IMGCVariantMgrParameters' : '{82CD5AB0-9407-11D2-89D9-0020184077E1}',
	'IMGCVariantMgrOutputGenerator' : '{82CD5AB1-9407-11D2-89D9-0020184077E1}',
	'IMGCVariantMgrEquivPartsSettings' : '{82CD5AB2-9407-11D2-89D9-0020184077E1}',
	'IMGCVariantMgrUID' : '{D9AA5BF5-2389-40CA-9E58-8A7A59B2AF31}',
	'IMGCVariantMgrDocuments' : '{7866380E-9407-11D2-89D9-0020184077E1}',
	'IMGCVariantMgrApplication' : '{7866380D-9407-11D2-89D9-0020184077E1}',
	'IMGCVariantMgrEditors' : '{34842ABE-9E81-4B7D-A5D3-35C68F327A36}',
	'IMGCVariantMgrEditor' : '{82CD5AAD-9407-11D2-89D9-0020184077E1}',
	'ITest' : '{8ADA56FC-3345-41CA-B16B-AB446D82790D}',
	'_IMGCVariantMgrDocumentEvents' : '{FFD61045-44FD-4F80-995C-6C6F0AE1DEB0}',
}

win32com.client.constants.__dicts__.append(constants.__dict__)

