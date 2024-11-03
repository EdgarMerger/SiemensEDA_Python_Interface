# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.11.6 (tags/v3.11.6:8b6ee5b, Oct  2 2023, 14:57:12) [MSC v.1935 64 bit (AMD64)]
# From type library 'viewdraw.tlb'
# On Tue Oct 29 09:13:36 2024
''
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

CLSID = IID('{4ADEF4E1-690A-11CE-9261-0020C5E26659}')
MajorVersion = 119
MinorVersion = 0
LibraryFlags = 8
LCID = 0x0

class constants:
	ARM_Add_Prefix                =4          # from enum AddReuseModifierType
	ARM_Add_Suffix                =3          # from enum AddReuseModifierType
	ARM_Increment_By              =1          # from enum AddReuseModifierType
	ARM_Renumber_As_Needed        =0          # from enum AddReuseModifierType
	ARM_Renumber_From             =2          # from enum AddReuseModifierType
	ART_Logical_Only              =0          # from enum AddReuseType
	ART_Logical_Physical          =1          # from enum AddReuseType
	AS_ForcePaint_dispid          =6          # from enum AddinInfoDispIDs
	AS_Group_dispid               =4          # from enum AddinInfoDispIDs
	AS_InitiallyDisabled_dispid   =11         # from enum AddinInfoDispIDs
	AS_InitiallyVisible_dispid    =12         # from enum AddinInfoDispIDs
	AS_LicenseFeature_dispid      =10         # from enum AddinInfoDispIDs
	AS_Name_dispid                =1          # from enum AddinInfoDispIDs
	AS_Placement_dispid           =5          # from enum AddinInfoDispIDs
	AS_ProgId_dispid              =2          # from enum AddinInfoDispIDs
	AS_RuntimeCreateDecision_dispid=9          # from enum AddinInfoDispIDs
	AS_Script_dispid              =3          # from enum AddinInfoDispIDs
	AS_ShortCutKey_dispid         =7          # from enum AddinInfoDispIDs
	AS_ToolbarButton_dispid       =8          # from enum AddinInfoDispIDs
	DumpOutputWindow              =11         # from enum ApplicationAtTestDispIDs
	ExtractReuseCircuits          =1          # from enum ApplicationAtTestDispIDs
	GetProjectIntegrationStatus   =7          # from enum ApplicationAtTestDispIDs
	ImportEDXFileDownloadedFromPartQuestSite=12         # from enum ApplicationAtTestDispIDs
	ImportNetlistProject          =5          # from enum ApplicationAtTestDispIDs
	PropagateFpgaSignalNames      =8          # from enum ApplicationAtTestDispIDs
	PublishBlocks                 =10         # from enum ApplicationAtTestDispIDs
	ReplaceConnector              =2          # from enum ApplicationAtTestDispIDs
	ReplaceSymbol                 =3          # from enum ApplicationAtTestDispIDs
	RunProjectIntegrationTask     =6          # from enum ApplicationAtTestDispIDs
	RunSchematicTest              =9          # from enum ApplicationAtTestDispIDs
	UpdateDRBs                    =4          # from enum ApplicationAtTestDispIDs
	CO_B_dispid                   =3          # from enum ColorDispIDs
	CO_G_dispid                   =2          # from enum ColorDispIDs
	CO_R_dispid                   =1          # from enum ColorDispIDs
	CM_CommandDisable_dispid      =324        # from enum CommandsManagerIDs
	CM_CommandEnable_dispid       =323        # from enum CommandsManagerIDs
	CM_CommandRemove_dispid       =325        # from enum CommandsManagerIDs
	CM_ExecuteCommandByID_dispid  =328        # from enum CommandsManagerIDs
	CM_ExecuteCommand_dispid      =327        # from enum CommandsManagerIDs
	CM_ExecuteMenuCommand_dispid  =326        # from enum CommandsManagerIDs
	CM_RegisterOLECommand_dispid  =321        # from enum CommandsManagerIDs
	CM_UnregisterOLECommand_dispid=322        # from enum CommandsManagerIDs
	DESSRCHOBJ_DUMP               =1          # from enum DesignSearcherEnum
	DESSRCHOBJ_DUMP_ALL           =2          # from enum DesignSearcherEnum
	DESSRCHOBJ_DUMP_NO_BUS_RIPPERS=3          # from enum DesignSearcherEnum
	DESSRCHOBJ_QUERY              =4          # from enum DesignSearcherEnum
	DesignerErrCodeDataManagementAuthorizationFailed=-2147220987 # from enum DesignerErrCode
	DesignerErrCodeDataManagementChangeServerWhileEditing=-2147220980 # from enum DesignerErrCode
	DesignerErrCodeDataManagementEntityTypeProductMismatch=-2147220982 # from enum DesignerErrCode
	DesignerErrCodeDataManagementInvalidDirectory=-2147220985 # from enum DesignerErrCode
	DesignerErrCodeDataManagementNoWritePermission=-2147220984 # from enum DesignerErrCode
	DesignerErrCodeDataManagementOtherError=-2147220983 # from enum DesignerErrCode
	DesignerErrCodeDataManagementReadonlySetting=-2147220977 # from enum DesignerErrCode
	DesignerErrCodeDataManagementServiceFailed=-2147220986 # from enum DesignerErrCode
	DesignerErrCodeDataManagementServiceNotConnected=-2147220988 # from enum DesignerErrCode
	DesignerErrCodeDataManagementUnknownSetting=-2147220979 # from enum DesignerErrCode
	DesignerErrCodeDataManagementValueNotInRange=-2147220978 # from enum DesignerErrCode
	DesignerErrCodeFunctionNotSupported=-2147220981 # from enum DesignerErrCode
	DesignerErrCodeInternalError  =-2147220990 # from enum DesignerErrCode
	DesignerErrCodeInvalidParameter=-2147220991 # from enum DesignerErrCode
	DesignerErrOutOfRange         =-2147220989 # from enum DesignerErrCode
	GSIC_Green                    =2          # from enum GenericStatusIndicatorColor
	GSIC_Grey                     =4          # from enum GenericStatusIndicatorColor
	GSIC_Red                      =1          # from enum GenericStatusIndicatorColor
	GSIC_Yellow                   =3          # from enum GenericStatusIndicatorColor
	GetSegmentX_dispid            =8          # from enum HighPrecisionObjectDispIDs
	GetSegmentY_dispid            =9          # from enum HighPrecisionObjectDispIDs
	GetSize_dispid                =6          # from enum HighPrecisionObjectDispIDs
	GetX_dispid                   =2          # from enum HighPrecisionObjectDispIDs
	GetY_dispid                   =3          # from enum HighPrecisionObjectDispIDs
	SetObject_dispid              =1          # from enum HighPrecisionObjectDispIDs
	SetSegmentX_dispid            =10         # from enum HighPrecisionObjectDispIDs
	SetSegmentY_dispid            =11         # from enum HighPrecisionObjectDispIDs
	SetSize_dispid                =7          # from enum HighPrecisionObjectDispIDs
	SetX_dispid                   =4          # from enum HighPrecisionObjectDispIDs
	SetY_dispid                   =5          # from enum HighPrecisionObjectDispIDs
	ICTDOC_Activate_dispid        =105        # from enum ICTDocumentDispIDs
	ICTDOC_Application_dispid     =101        # from enum ICTDocumentDispIDs
	ICTDOC_Close_dispid           =106        # from enum ICTDocumentDispIDs
	ICTDOC_FullName_dispid        =103        # from enum ICTDocumentDispIDs
	ICTDOC_GetViews_dispid        =108        # from enum ICTDocumentDispIDs
	ICTDOC_IsReadOnly_dispid      =116        # from enum ICTDocumentDispIDs
	ICTDOC_Name_dispid            =102        # from enum ICTDocumentDispIDs
	ICTDOC_Parent_dispid          =104        # from enum ICTDocumentDispIDs
	ICTDOC_Print_dispid           =107        # from enum ICTDocumentDispIDs
	ICTDOC_SetReadOnly_dispid     =117        # from enum ICTDocumentDispIDs
	ICTD_Close_dispid             =2          # from enum ICTDocumentsIDs
	ICTD_GetAvailableICTs_dispid  =3          # from enum ICTDocumentsIDs
	ICTD_GetOpenedCount_dispid    =5          # from enum ICTDocumentsIDs
	ICTD_GetOpenedICTs_dispid     =4          # from enum ICTDocumentsIDs
	ICTD_GetOpenedItem_dispid     =6          # from enum ICTDocumentsIDs
	ICTD_Open_dispid              =1          # from enum ICTDocumentsIDs
	DESIGNERDATAMANAGMENTADDITIONALPROPERTIES_COUNT=1          # from enum IMGCDesignerDataManagementAdditionalPropertiesEnum
	DESIGNERDATAMANAGMENTADDITIONALPROPERTIES_ITEM=3          # from enum IMGCDesignerDataManagementAdditionalPropertiesEnum
	DESIGNERDATAMANAGMENTADDITIONALPROPERTIES_REMOVE=2          # from enum IMGCDesignerDataManagementAdditionalPropertiesEnum
	DESIGNERDATAMANAGMENTADDITIONALPROPERTY_ID=1          # from enum IMGCDesignerDataManagementAdditionalPropertyEnum
	DESIGNERDATAMANAGMENTADDITIONALPROPERTY_LABEL=2          # from enum IMGCDesignerDataManagementAdditionalPropertyEnum
	DESIGNERDATAMANAGMENTENTITIES_COUNT=1          # from enum IMGCDesignerDataManagementEntitiesEnum
	DESIGNERDATAMANAGMENTENTITIES_ITEM=3          # from enum IMGCDesignerDataManagementEntitiesEnum
	DESIGNERDATAMANAGMENTENTITIES_REMOVE=2          # from enum IMGCDesignerDataManagementEntitiesEnum
	DESIGNERDATAMANAGMENTENTITY_ACCESSTYPE=4          # from enum IMGCDesignerDataManagementEntityEnum
	DESIGNERDATAMANAGMENTENTITY_ADDITIONALPROPERTYVALUE=16         # from enum IMGCDesignerDataManagementEntityEnum
	DESIGNERDATAMANAGMENTENTITY_CANCELEDITING=23         # from enum IMGCDesignerDataManagementEntityEnum
	DESIGNERDATAMANAGMENTENTITY_CHECKEDINDATE=8          # from enum IMGCDesignerDataManagementEntityEnum
	DESIGNERDATAMANAGMENTENTITY_CHECKIN=14         # from enum IMGCDesignerDataManagementEntityEnum
	DESIGNERDATAMANAGMENTENTITY_DUMPPROPERTIES=18         # from enum IMGCDesignerDataManagementEntityEnum
	DESIGNERDATAMANAGMENTENTITY_EDITEXCLUSIVE=10         # from enum IMGCDesignerDataManagementEntityEnum
	DESIGNERDATAMANAGMENTENTITY_EDITSHARED=9          # from enum IMGCDesignerDataManagementEntityEnum
	DESIGNERDATAMANAGMENTENTITY_EXPORT=13         # from enum IMGCDesignerDataManagementEntityEnum
	DESIGNERDATAMANAGMENTENTITY_LAUNCHWEBVIEW=15         # from enum IMGCDesignerDataManagementEntityEnum
	DESIGNERDATAMANAGMENTENTITY_LOCALPATH=22         # from enum IMGCDesignerDataManagementEntityEnum
	DESIGNERDATAMANAGMENTENTITY_NAME=2          # from enum IMGCDesignerDataManagementEntityEnum
	DESIGNERDATAMANAGMENTENTITY_OPENREFERENCE=11         # from enum IMGCDesignerDataManagementEntityEnum
	DESIGNERDATAMANAGMENTENTITY_PATH=1          # from enum IMGCDesignerDataManagementEntityEnum
	DESIGNERDATAMANAGMENTENTITY_PROJECTNAME=17         # from enum IMGCDesignerDataManagementEntityEnum
	DESIGNERDATAMANAGMENTENTITY_PROPERTYVALUEBYID=25         # from enum IMGCDesignerDataManagementEntityEnum
	DESIGNERDATAMANAGMENTENTITY_RELATEDENTITIES=21         # from enum IMGCDesignerDataManagementEntityEnum
	DESIGNERDATAMANAGMENTENTITY_RUNCONFIGURATIONRULES=19         # from enum IMGCDesignerDataManagementEntityEnum
	DESIGNERDATAMANAGMENTENTITY_STATUS=5          # from enum IMGCDesignerDataManagementEntityEnum
	DESIGNERDATAMANAGMENTENTITY_TYPE=3          # from enum IMGCDesignerDataManagementEntityEnum
	DESIGNERDATAMANAGMENTENTITY_UNLOCK=24         # from enum IMGCDesignerDataManagementEntityEnum
	DESIGNERDATAMANAGMENTENTITY_USERS=6          # from enum IMGCDesignerDataManagementEntityEnum
	DESIGNERDATAMANAGMENTENTITY_VERSION=7          # from enum IMGCDesignerDataManagementEntityEnum
	DESIGNERDATAMANAGMENTENTITY_VIEW=12         # from enum IMGCDesignerDataManagementEntityEnum
	DESIGNERDATAMANAGMENTENTITY_VIEWFOROUTPUTSGENERATION=20         # from enum IMGCDesignerDataManagementEntityEnum
	DESIGNERDATAMANAGMENT_ADDITIONALPROPERTIES=6          # from enum IMGCDesignerDataManagementEnum
	DESIGNERDATAMANAGMENT_CONNECT =4          # from enum IMGCDesignerDataManagementEnum
	DESIGNERDATAMANAGMENT_ENTITIES=1          # from enum IMGCDesignerDataManagementEnum
	DESIGNERDATAMANAGMENT_FINDENTITYBYPATH=3          # from enum IMGCDesignerDataManagementEnum
	DESIGNERDATAMANAGMENT_FINDENTITYBYPATHANDVERSION=7          # from enum IMGCDesignerDataManagementEnum
	DESIGNERDATAMANAGMENT_ISCONNECTED=5          # from enum IMGCDesignerDataManagementEnum
	DESIGNERDATAMANAGMENT_LASTERRORMESSAGE=10         # from enum IMGCDesignerDataManagementEnum
	DESIGNERDATAMANAGMENT_OPENCOMPONENTVIEW=12         # from enum IMGCDesignerDataManagementEnum
	DESIGNERDATAMANAGMENT_OPENMANAGEDBLOCKVIEW=13         # from enum IMGCDesignerDataManagementEnum
	DESIGNERDATAMANAGMENT_OPTION  =8          # from enum IMGCDesignerDataManagementEnum
	DESIGNERDATAMANAGMENT_OPTIONISREADONLY=9          # from enum IMGCDesignerDataManagementEnum
	DESIGNERDATAMANAGMENT_RECENTENTITIES=2          # from enum IMGCDesignerDataManagementEnum
	DESIGNERDATAMANAGMENT_VALIDENTITYTYPES=11         # from enum IMGCDesignerDataManagementEnum
	IOPD_GetFPGAs_dispid          =301        # from enum IODProjectDataDispIDs
	IOPD_SetFPGAs_dispid          =302        # from enum IODProjectDataDispIDs
	MD_GetAvailableTargetGlobals_dispid=11         # from enum MergeDataDispIDs
	MD_GetAvailableTargetLayers_dispid=7          # from enum MergeDataDispIDs
	MD_GetBusContents_dispid      =5          # from enum MergeDataDispIDs
	MD_GetBusNames_dispid         =1          # from enum MergeDataDispIDs
	MD_GetSourceBusContents_dispid=2          # from enum MergeDataDispIDs
	MD_GetSourceGlobals_dispid    =10         # from enum MergeDataDispIDs
	MD_GetSourceLayers_dispid     =6          # from enum MergeDataDispIDs
	MD_GetTargetBusContents_dispid=3          # from enum MergeDataDispIDs
	MD_GetTargetGlobal_dispid     =12         # from enum MergeDataDispIDs
	MD_GetTargetLayer_dispid      =8          # from enum MergeDataDispIDs
	MD_SetBusContents_dispid      =4          # from enum MergeDataDispIDs
	MD_SetTargetGlobal_dispid     =13         # from enum MergeDataDispIDs
	MD_SetTargetLayer_dispid      =9          # from enum MergeDataDispIDs
	PP_AppendPartition_dispid     =204        # from enum PDBPartitionsDispIDs
	PP_GetPartition_dispid        =200        # from enum PDBPartitionsDispIDs
	PP_GetPartitionsArray_dispid  =202        # from enum PDBPartitionsDispIDs
	PP_GetPartitionsCount_dispid  =201        # from enum PDBPartitionsDispIDs
	PP_InsertPartition_dispid     =203        # from enum PDBPartitionsDispIDs
	PP_PartitionExists_dispid     =207        # from enum PDBPartitionsDispIDs
	PP_RemovePartitionByIndex_dispid=206        # from enum PDBPartitionsDispIDs
	PP_RemovePartitionByName_dispid=205        # from enum PDBPartitionsDispIDs
	PinMT_ByName                  =1          # from enum PinMappingType
	PinMT_ByPinNumber             =2          # from enum PinMappingType
	PD_AddNetlistLib_dispid       =48         # from enum ProjectDataDispIDs
	PD_AddiCDBDesign_dispid       =36         # from enum ProjectDataDispIDs
	PD_CentralLibraryPath_dispid  =5          # from enum ProjectDataDispIDs
	PD_FindNetlistLibPos_dispid   =46         # from enum ProjectDataDispIDs
	PD_GetBordersFilePath_dispid  =14         # from enum ProjectDataDispIDs
	PD_GetBusContentsFilePath_dispid=29         # from enum ProjectDataDispIDs
	PD_GetFlowType_dispid         =39         # from enum ProjectDataDispIDs
	PD_GetFrontEndSnapshot_dispid =31         # from enum ProjectDataDispIDs
	PD_GetIODProjectData_dispid   =35         # from enum ProjectDataDispIDs
	PD_GetNetlistLibCount_dispid  =44         # from enum ProjectDataDispIDs
	PD_GetNetlistLib_dispid       =45         # from enum ProjectDataDispIDs
	PD_GetPCBDesignPath_dispid    =33         # from enum ProjectDataDispIDs
	PD_GetPDBPartitions_dispid    =22         # from enum ProjectDataDispIDs
	PD_GetPinComponentsFilePath_dispid=18         # from enum ProjectDataDispIDs
	PD_GetPinNumbers_dispid       =42         # from enum ProjectDataDispIDs
	PD_GetProjectFilePath_dispid  =3          # from enum ProjectDataDispIDs
	PD_GetProjectName_dispid      =2          # from enum ProjectDataDispIDs
	PD_GetProjectPath_dispid      =1          # from enum ProjectDataDispIDs
	PD_GetSearchPathScheme_dispid =23         # from enum ProjectDataDispIDs
	PD_GetSlotsCount_dispid       =41         # from enum ProjectDataDispIDs
	PD_GetSnapshotName_dispid     =6          # from enum ProjectDataDispIDs
	PD_GetSymbolPartitions_dispid =7          # from enum ProjectDataDispIDs
	PD_GetiCDBDesignRootBlock_dispid=12         # from enum ProjectDataDispIDs
	PD_GetiCDBDesignType_dispid   =10         # from enum ProjectDataDispIDs
	PD_GetiCDBDesigns_dispid      =9          # from enum ProjectDataDispIDs
	PD_GetiCDBDiscardFilePath_dispid=20         # from enum ProjectDataDispIDs
	PD_GetiCDBServerName_dispid   =25         # from enum ProjectDataDispIDs
	PD_GetiCDBServerPortsFilePath_dispid=27         # from enum ProjectDataDispIDs
	PD_RemoveNetlistLib_dispid    =47         # from enum ProjectDataDispIDs
	PD_RemoveiCDBDesign_dispid    =37         # from enum ProjectDataDispIDs
	PD_RenameiCDBDesign_dispid    =38         # from enum ProjectDataDispIDs
	PD_SaveNetlistLibs_dispid     =49         # from enum ProjectDataDispIDs
	PD_SetBordersFilePath_dispid  =15         # from enum ProjectDataDispIDs
	PD_SetBusContentsFilePath_dispid=30         # from enum ProjectDataDispIDs
	PD_SetFlowType_dispid         =40         # from enum ProjectDataDispIDs
	PD_SetFrontEndSnapshot_dispid =32         # from enum ProjectDataDispIDs
	PD_SetPCBDesignPath_dispid    =34         # from enum ProjectDataDispIDs
	PD_SetPinComponentsFilePath_dispid=19         # from enum ProjectDataDispIDs
	PD_SetSearchPathScheme_dispid =24         # from enum ProjectDataDispIDs
	PD_SetiCDBDesignRootBlock_dispid=13         # from enum ProjectDataDispIDs
	PD_SetiCDBDesignType_dispid   =11         # from enum ProjectDataDispIDs
	PD_SetiCDBDiscardFilePath_dispid=21         # from enum ProjectDataDispIDs
	PD_SetiCDBServerName_dispid   =26         # from enum ProjectDataDispIDs
	PD_SetiCDBServerPortsFilePath_dispid=28         # from enum ProjectDataDispIDs
	PD_UpdateOtherObjects_dispid  =43         # from enum ProjectDataDispIDs
	PD_iCDBDir_dispid             =4          # from enum ProjectDataDispIDs
	PIIC_Green                    =2          # from enum ProjectIntegrationIndicatorColor
	PIIC_Grey                     =1          # from enum ProjectIntegrationIndicatorColor
	PIIC_Red                      =4          # from enum ProjectIntegrationIndicatorColor
	PIIC_Yellow                   =3          # from enum ProjectIntegrationIndicatorColor
	PropMT_LibraryOnly            =1          # from enum PropertyMappingType
	PropMT_LibraryWins            =3          # from enum PropertyMappingType
	PropMT_SchematicWins          =2          # from enum PropertyMappingType
	RI_GetConnectedObject_dispid  =1          # from enum RipperDispIDs
	RI_GetConnectedObjects_dispid =2          # from enum RipperDispIDs
	RI_GetMappedSignal_dispid     =3          # from enum RipperDispIDs
	SDD_GetReadWriteRights_dispid =118        # from enum SchematicSheetDocumentDispIDs
	SSD_AcquireReadWriteRights_dispid=119        # from enum SchematicSheetDocumentDispIDs
	SSD_Activate_dispid           =105        # from enum SchematicSheetDocumentDispIDs
	SSD_Application_dispid        =101        # from enum SchematicSheetDocumentDispIDs
	SSD_CancelSave_dispid         =113        # from enum SchematicSheetDocumentDispIDs
	SSD_Close_dispid              =106        # from enum SchematicSheetDocumentDispIDs
	SSD_DataType_dispid           =112        # from enum SchematicSheetDocumentDispIDs
	SSD_DeleteSheet_dispid        =115        # from enum SchematicSheetDocumentDispIDs
	SSD_DiscardSymbolChanges_dispid=123        # from enum SchematicSheetDocumentDispIDs
	SSD_ExportMetafile_dispid     =110        # from enum SchematicSheetDocumentDispIDs
	SSD_FullName_dispid           =103        # from enum SchematicSheetDocumentDispIDs
	SSD_GetViews_dispid           =108        # from enum SchematicSheetDocumentDispIDs
	SSD_InsertSheet_dispid        =114        # from enum SchematicSheetDocumentDispIDs
	SSD_IsAccess_dispid           =111        # from enum SchematicSheetDocumentDispIDs
	SSD_IsReadOnly_dispid         =116        # from enum SchematicSheetDocumentDispIDs
	SSD_Name_dispid               =102        # from enum SchematicSheetDocumentDispIDs
	SSD_Parent_dispid             =104        # from enum SchematicSheetDocumentDispIDs
	SSD_Print_dispid              =107        # from enum SchematicSheetDocumentDispIDs
	SSD_ReRead_dispid             =109        # from enum SchematicSheetDocumentDispIDs
	SSD_SaveAs_dispid             =125        # from enum SchematicSheetDocumentDispIDs
	SSD_Save_dispid               =124        # from enum SchematicSheetDocumentDispIDs
	SSD_SetFollowingSheetRange_dispid=120        # from enum SchematicSheetDocumentDispIDs
	SSD_SetReadOnly_dispid        =117        # from enum SchematicSheetDocumentDispIDs
	SSD_SetSheetName_dispid       =121        # from enum SchematicSheetDocumentDispIDs
	SSD_UpdateSymbolInDesign_dispid=122        # from enum SchematicSheetDocumentDispIDs
	SSDS_Add_dispid               =105        # from enum SchematicSheetDocumentsDispIDs
	SSDS_Application_dispid       =102        # from enum SchematicSheetDocumentsDispIDs
	SSDS_Close_dispid             =106        # from enum SchematicSheetDocumentsDispIDs
	SSDS_CopyBlocksToClipboard_dispid=114        # from enum SchematicSheetDocumentsDispIDs
	SSDS_CopySheetsToClipboard_dispid=111        # from enum SchematicSheetDocumentsDispIDs
	SSDS_CopyToClipboard_dispid   =119        # from enum SchematicSheetDocumentsDispIDs
	SSDS_Count_dispid             =101        # from enum SchematicSheetDocumentsDispIDs
	SSDS_DeleteSheet_dispid       =118        # from enum SchematicSheetDocumentsDispIDs
	SSDS_DetermineClipboardContent_dispid=116        # from enum SchematicSheetDocumentsDispIDs
	SSDS_GetAvailableSchematics_dispid=108        # from enum SchematicSheetDocumentsDispIDs
	SSDS_GetAvailableSheets_dispid=109        # from enum SchematicSheetDocumentsDispIDs
	SSDS_GetSheetOrder_dispid     =121        # from enum SchematicSheetDocumentsDispIDs
	SSDS_InsertSheet_dispid       =117        # from enum SchematicSheetDocumentsDispIDs
	SSDS_IsSheetsClipboardEmpty_dispid=113        # from enum SchematicSheetDocumentsDispIDs
	SSDS_IsSymbolUnderEdition_dispid=124        # from enum SchematicSheetDocumentsDispIDs
	SSDS_Item_dispid              =104        # from enum SchematicSheetDocumentsDispIDs
	SSDS_OpenSymbol_dispid        =123        # from enum SchematicSheetDocumentsDispIDs
	SSDS_Open_Hierarchically_dispid=107        # from enum SchematicSheetDocumentsDispIDs
	SSDS_Open_dispid              =110        # from enum SchematicSheetDocumentsDispIDs
	SSDS_Parent_dispid            =103        # from enum SchematicSheetDocumentsDispIDs
	SSDS_PasteBlocksFromClipboard_dispid=115        # from enum SchematicSheetDocumentsDispIDs
	SSDS_PasteFromClipboard_dispid=120        # from enum SchematicSheetDocumentsDispIDs
	SSDS_PasteSheetsFromClipboard_dispid=112        # from enum SchematicSheetDocumentsDispIDs
	SSDS_SetSheetOrder_dispid     =122        # from enum SchematicSheetDocumentsDispIDs
	SRC_Design                    =1          # from enum ScopeReplaceConnector
	SRC_Selection                 =3          # from enum ScopeReplaceConnector
	SRC_Sheet                     =2          # from enum ScopeReplaceConnector
	SRP_Board                     =2          # from enum ScopeReplacePart
	SRP_Project                   =1          # from enum ScopeReplacePart
	SRP_Schematic                 =3          # from enum ScopeReplacePart
	SRP_Selection                 =5          # from enum ScopeReplacePart
	SRP_Sheet                     =4          # from enum ScopeReplacePart
	SRS_Board                     =2          # from enum ScopeReplaceSymbol
	SRS_Project                   =1          # from enum ScopeReplaceSymbol
	SRS_Schematic                 =3          # from enum ScopeReplaceSymbol
	SRS_Selection                 =5          # from enum ScopeReplaceSymbol
	SRS_Sheet                     =4          # from enum ScopeReplaceSymbol
	SL_Append_dispid              =3          # from enum StringListDispIDs
	SL_Clear_dispid               =6          # from enum StringListDispIDs
	SL_GetCount_dispid            =1          # from enum StringListDispIDs
	SL_GetItem_dispid             =2          # from enum StringListDispIDs
	SL_Insert_dispid              =4          # from enum StringListDispIDs
	SL_Remove_dispid              =5          # from enum StringListDispIDs
	SP_AppendPartition_dispid     =104        # from enum SymbolPartitionsDispIDs
	SP_GetPartition_dispid        =100        # from enum SymbolPartitionsDispIDs
	SP_GetPartitionsArray_dispid  =102        # from enum SymbolPartitionsDispIDs
	SP_GetPartitionsCount_dispid  =101        # from enum SymbolPartitionsDispIDs
	SP_InsertPartition_dispid     =103        # from enum SymbolPartitionsDispIDs
	SP_PartitionExists_dispid     =107        # from enum SymbolPartitionsDispIDs
	SP_RemovePartitionByIndex_dispid=106        # from enum SymbolPartitionsDispIDs
	SP_RemovePartitionByName_dispid=105        # from enum SymbolPartitionsDispIDs
	VD_ALL                        =0          # from enum VdAllOrSelected
	VD_SELECTED                   =1          # from enum VdAllOrSelected
	AnnoObjCOMPONENT              =0          # from enum VdAnnoObject
	AnnoObjCOMPONENT_PIN          =1          # from enum VdAnnoObject
	AnnoObjNET                    =2          # from enum VdAnnoObject
	AnnoObjPIN                    =3          # from enum VdAnnoObject
	AnnoObjWINDOW                 =4          # from enum VdAnnoObject
	AnnoPosCENTER                 =4          # from enum VdAnnoPos
	AnnoPosLOWERLEFT              =0          # from enum VdAnnoPos
	AnnoPosLOWERRIGHT             =1          # from enum VdAnnoPos
	AnnoPosUPPERLEFT              =2          # from enum VdAnnoPos
	AnnoPosUPPERRIGHT             =3          # from enum VdAnnoPos
	AnnoBOX                       =0          # from enum VdAnnoType
	AnnoNOBOX                     =1          # from enum VdAnnoType
	AnnoNOSELECT                  =3          # from enum VdAnnoType
	AnnoSELECT                    =2          # from enum VdAnnoType
	AppEventACTIVATE_VIEW         =3          # from enum VdAppEventDispatchID
	AppEventACTIVATE_VIEW2        =20         # from enum VdAppEventDispatchID
	AppEventAFTERDOCUMENTSAVED    =18         # from enum VdAppEventDispatchID
	AppEventAFTERSHEETREAD        =19         # from enum VdAppEventDispatchID
	AppEventAFTER_DOCUMENT_OPENED =6          # from enum VdAppEventDispatchID
	AppEventAFTER_DOCUMENT_SAVE   =18         # from enum VdAppEventDispatchID
	AppEventAFTER_PRINT_PROJECT   =28         # from enum VdAppEventDispatchID
	AppEventAFTER_SAVE_AND_CHECK  =24         # from enum VdAppEventDispatchID
	AppEventAFTER_SHEET_READ      =19         # from enum VdAppEventDispatchID
	AppEventAFTER_SHEET_REREAD    =37         # from enum VdAppEventDispatchID
	AppEventAFTER_SYMBOL_DEFINITION_REFRESH=55         # from enum VdAppEventDispatchID
	AppEventAfter_FA_Finished     =46         # from enum VdAppEventDispatchID
	AppEventBATCH_ATTRIBUTES_ADDED=51         # from enum VdAppEventDispatchID
	AppEventBEFOREDOCUMENTSAVED   =17         # from enum VdAppEventDispatchID
	AppEventBEFORE_DOCUMENT_CLOSE =54         # from enum VdAppEventDispatchID
	AppEventBEFORE_DOCUMENT_OPENED=5          # from enum VdAppEventDispatchID
	AppEventBEFORE_DOCUMENT_SAVE  =17         # from enum VdAppEventDispatchID
	AppEventBEFORE_PRINT_PROJECT  =27         # from enum VdAppEventDispatchID
	AppEventBEFORE_PROJECT_CHANGED=41         # from enum VdAppEventDispatchID
	AppEventBEFORE_PROJECT_MODIFIED=38         # from enum VdAppEventDispatchID
	AppEventBEFORE_SAVE_AND_CHECK =23         # from enum VdAppEventDispatchID
	AppEventBLOCK_LOCKED          =52         # from enum VdAppEventDispatchID
	AppEventBLOCK_MODIFIED        =22         # from enum VdAppEventDispatchID
	AppEventBefore_FA_Started     =45         # from enum VdAppEventDispatchID
	AppEventCENTRAL_LIBRARY_CHANGED=43         # from enum VdAppEventDispatchID
	AppEventCLEAR_EEVM_MODE       =42         # from enum VdAppEventDispatchID
	AppEventCLOSE                 =14         # from enum VdAppEventDispatchID
	AppEventCONSTRAINTS_MODE_CHANGED=32         # from enum VdAppEventDispatchID
	AppEventCREATE_ICT_OBJECT     =48         # from enum VdAppEventDispatchID
	AppEventCREATE_OBJECT         =9          # from enum VdAppEventDispatchID
	AppEventDBCONFIG_MODIFIED     =56         # from enum VdAppEventDispatchID
	AppEventDEACTIVATE_VIEW       =4          # from enum VdAppEventDispatchID
	AppEventDEACTIVATE_VIEW2      =21         # from enum VdAppEventDispatchID
	AppEventDELETE                =12         # from enum VdAppEventDispatchID
	AppEventDOCUMENT_CLOSE        =33         # from enum VdAppEventDispatchID
	AppEventDOCUMENT_MODIFIED     =8          # from enum VdAppEventDispatchID
	AppEventDOCUMENT_SAVE         =7          # from enum VdAppEventDispatchID
	AppEventDOCUMENT_SAVEAS       =30         # from enum VdAppEventDispatchID
	AppEventITC_COMMAND           =34         # from enum VdAppEventDispatchID
	AppEventLOCKREQUEST           =15         # from enum VdAppEventDispatchID
	AppEventLOCK_REQUEST          =15         # from enum VdAppEventDispatchID
	AppEventMOUSE_MOVED           =13         # from enum VdAppEventDispatchID
	AppEventOAT_ADDED             =25         # from enum VdAppEventDispatchID
	AppEventPAINT                 =11         # from enum VdAppEventDispatchID
	AppEventPAINT_REGION          =26         # from enum VdAppEventDispatchID
	AppEventPRINT_FILE            =29         # from enum VdAppEventDispatchID
	AppEventPRODUCTION_LIBRARY_LIMITATIONS_CHANGED=57         # from enum VdAppEventDispatchID
	AppEventPROJECT_CHANGED       =40         # from enum VdAppEventDispatchID
	AppEventPROJECT_CLOSED        =49         # from enum VdAppEventDispatchID
	AppEventPROJECT_MODIFIED      =31         # from enum VdAppEventDispatchID
	AppEventREUSE_BLOCK_ADDED     =53         # from enum VdAppEventDispatchID
	AppEventSELECT                =10         # from enum VdAppEventDispatchID
	AppEventSETTINGS_CHANGED      =47         # from enum VdAppEventDispatchID
	AppEventSHUTDOWN              =2          # from enum VdAppEventDispatchID
	AppEventSOURCEDOCUMENT_SAVE   =36         # from enum VdAppEventDispatchID
	AppEventSOURCE_FILE_MODIFIED  =39         # from enum VdAppEventDispatchID
	AppEventSTARTUP               =1          # from enum VdAppEventDispatchID
	AppEventSYMBOL_PREVIEWED      =35         # from enum VdAppEventDispatchID
	AppEventSYMBOL_UPDATE_STARTED =50         # from enum VdAppEventDispatchID
	AppEventSearch_Path_Scheme_Changed=44         # from enum VdAppEventDispatchID
	AppEventUNLOCK                =16         # from enum VdAppEventDispatchID
	APP_Activate_dispid           =201        # from enum VdAppIDs
	APP_ActiveDocument_dispid     =208        # from enum VdAppIDs
	APP_ActiveICTView_dispid      =269        # from enum VdAppIDs
	APP_ActiveView_dispid         =207        # from enum VdAppIDs
	APP_AddAddin_dispid           =273        # from enum VdAppIDs
	APP_Addins_dispid             =216        # from enum VdAppIDs
	APP_AppendOutput_dispid       =223        # from enum VdAppIDs
	APP_Bindings_dispid           =219        # from enum VdAppIDs
	APP_BroadcastDBConfigModified_dispid=298        # from enum VdAppIDs
	APP_ClearEEVMMode_dispid      =248        # from enum VdAppIDs
	APP_CloseProject_dispid       =274        # from enum VdAppIDs
	APP_CommandBars_dispid        =215        # from enum VdAppIDs
	APP_CommandLineArguments_dispid=210        # from enum VdAppIDs
	APP_CommandsManager_dispid    =220        # from enum VdAppIDs
	APP_ConvertSchematicToICT_dispid=286        # from enum VdAppIDs
	APP_ConvertSymbol_dispid      =252        # from enum VdAppIDs
	APP_CreateProjectLibrary_dispid=304        # from enum VdAppIDs
	APP_CreateToolbar_dispid      =255        # from enum VdAppIDs
	APP_DataTag_dispid            =291        # from enum VdAppIDs
	APP_DeleteBlock_dispid        =256        # from enum VdAppIDs
	APP_DesignNets_dispid         =276        # from enum VdAppIDs
	APP_DesignSearcher_dispid     =297        # from enum VdAppIDs
	APP_DisableSelectionBroadcast_dispid=272        # from enum VdAppIDs
	APP_EDXEngine_dispid          =281        # from enum VdAppIDs
	APP_EnableEEVMMode_dispid     =247        # from enum VdAppIDs
	APP_EnableSelectionBroadcast_dispid=271        # from enum VdAppIDs
	APP_ExecuteCommandByID_dispid =307        # from enum VdAppIDs
	APP_ExportForeignDatabase_dispid=264        # from enum VdAppIDs
	APP_ExportSymbol_dispid       =280        # from enum VdAppIDs
	APP_ExtractPCB_dispid         =275        # from enum VdAppIDs
	APP_FireCentralLibraryReload_dispid=257        # from enum VdAppIDs
	APP_GenStatusIndicatorState_dispid=277        # from enum VdAppIDs
	APP_GetActiveiCDBDesign_dispid=229        # from enum VdAppIDs
	APP_GetCommonPropertyManager_dispid=243        # from enum VdAppIDs
	APP_GetConfigurationProperty_dispid=244        # from enum VdAppIDs
	APP_GetCurrentProdLib_dispid  =312        # from enum VdAppIDs
	APP_GetDefaultColor_dispid    =261        # from enum VdAppIDs
	APP_GetDefaultProdLib_dispid  =313        # from enum VdAppIDs
	APP_GetFramework_dispid       =242        # from enum VdAppIDs
	APP_GetICTContents_dispid     =258        # from enum VdAppIDs
	APP_GetICTDocuments_dispid    =259        # from enum VdAppIDs
	APP_GetLastErrorId_dispid     =240        # from enum VdAppIDs
	APP_GetLastErrorString_dispid =239        # from enum VdAppIDs
	APP_GetLibSpec_dispid         =317        # from enum VdAppIDs
	APP_GetPEFlowMode_dispid      =283        # from enum VdAppIDs
	APP_GetProdLibReadOnly_dispid =315        # from enum VdAppIDs
	APP_GetProdLibs_dispid        =310        # from enum VdAppIDs
	APP_GetProjectData_dispid     =228        # from enum VdAppIDs
	APP_GetProjectType_dispid     =299        # from enum VdAppIDs
	APP_GetProtectionProxy_dispid =268        # from enum VdAppIDs
	APP_GetSystemDesign_dispid    =287        # from enum VdAppIDs
	APP_HTMLDocuments_dispid      =213        # from enum VdAppIDs
	APP_HideModelProperties       =302        # from enum VdAppIDs
	APP_ImportEEToPE_dispid       =296        # from enum VdAppIDs
	APP_ImportForeignDatabase_dispid=265        # from enum VdAppIDs
	APP_ImportPADS_dispid         =314        # from enum VdAppIDs
	APP_ImportPadsPE_dispid       =288        # from enum VdAppIDs
	APP_Initialize_dispid         =203        # from enum VdAppIDs
	APP_Interactive_dispid        =205        # from enum VdAppIDs
	APP_IsAppStarted_dispid       =294        # from enum VdAppIDs
	APP_IsEEVMModeEnabled_dispid  =249        # from enum VdAppIDs
	APP_IsManagedBlockSource_dispid=306        # from enum VdAppIDs
	APP_IsManagedBlock_dispid     =305        # from enum VdAppIDs
	APP_IsProdLibSet_dispid       =316        # from enum VdAppIDs
	APP_IsProjectOpened_dispid    =295        # from enum VdAppIDs
	APP_IsReadOnlyMode_dispid     =293        # from enum VdAppIDs
	APP_IsReferenceApplication_dispid=290        # from enum VdAppIDs
	APP_LMGetSymbolLibPath_dispid =284        # from enum VdAppIDs
	APP_LMSetSymbolLibPath_dispid =285        # from enum VdAppIDs
	APP_LaunchSymbolEditor_dispid =263        # from enum VdAppIDs
	APP_MGCDesignerDataManagement_dispid=303        # from enum VdAppIDs
	APP_NewProject_dispid         =251        # from enum VdAppIDs
	APP_OpenDetailedComponentView_dispid=319        # from enum VdAppIDs
	APP_OpenDetailedManagedBlockView_dispid=320        # from enum VdAppIDs
	APP_OpenProject_dispid        =227        # from enum VdAppIDs
	APP_OpenReference_dispid      =292        # from enum VdAppIDs
	APP_OpenURL_dispid            =225        # from enum VdAppIDs
	APP_PrintProject_dispid       =221        # from enum VdAppIDs
	APP_ProductionLibraryLimitationsChanged_dispid=308        # from enum VdAppIDs
	APP_QueueDatabaseUpdates_dispid=278        # from enum VdAppIDs
	APP_QueueSelectEvents_dispid  =224        # from enum VdAppIDs
	APP_Quit_dispid               =226        # from enum VdAppIDs
	APP_ReadIni_dispid            =202        # from enum VdAppIDs
	APP_ReplacePart               =300        # from enum VdAppIDs
	APP_RunDesignIntegrityChecks_dispid=270        # from enum VdAppIDs
	APP_RunISE_dispid             =289        # from enum VdAppIDs
	APP_SchematicSheetDocuments_dispid=212        # from enum VdAppIDs
	APP_SelectComponent_dispid    =266        # from enum VdAppIDs
	APP_SelectNet_dispid          =267        # from enum VdAppIDs
	APP_SetButtonBitmap_dispid    =253        # from enum VdAppIDs
	APP_SetButtonResourceDLL_dispid=254        # from enum VdAppIDs
	APP_SetConfigurationProperty_dispid=245        # from enum VdAppIDs
	APP_SetDefaultColor_dispid    =260        # from enum VdAppIDs
	APP_SetEnvVariable_dispid     =211        # from enum VdAppIDs
	APP_SetProdLib_dispid         =311        # from enum VdAppIDs
	APP_SetRedraw_dispid          =222        # from enum VdAppIDs
	APP_SheetsEditMode_dispid     =279        # from enum VdAppIDs
	APP_ShellCmd_dispid           =218        # from enum VdAppIDs
	APP_ShouldProvideDetailedComponentView_dispid=318        # from enum VdAppIDs
	APP_SilentMode_dispid         =250        # from enum VdAppIDs
	APP_SourceDocuments_dispid    =214        # from enum VdAppIDs
	APP_StartMigration_dispid     =246        # from enum VdAppIDs
	APP_StartVNSD                 =301        # from enum VdAppIDs
	APP_StatusBarText_dispid      =206        # from enum VdAppIDs
	APP_SupportsProdLibLimitation_dispid=309        # from enum VdAppIDs
	APP_ToolbarAction_dispid      =262        # from enum VdAppIDs
	APP_UpdateMenuBar_dispid      =282        # from enum VdAppIDs
	APP_Version_dispid            =209        # from enum VdAppIDs
	APP_Visible_dispid            =204        # from enum VdAppIDs
	APP_PROXY_Activate_dispid     =201        # from enum VdAppProtectionProxyIDs
	APP_PROXY_ActiveDocument_dispid=208        # from enum VdAppProtectionProxyIDs
	APP_PROXY_ActiveICTView_dispid=269        # from enum VdAppProtectionProxyIDs
	APP_PROXY_ActiveViewHandle_dispid=40         # from enum VdAppProtectionProxyIDs
	APP_PROXY_ActiveView_dispid   =207        # from enum VdAppProtectionProxyIDs
	APP_PROXY_AddAddin_dispid     =273        # from enum VdAppProtectionProxyIDs
	APP_PROXY_AddLibraryAndSaveIni_dispid=104        # from enum VdAppProtectionProxyIDs
	APP_PROXY_AddLibrary_dispid   =25         # from enum VdAppProtectionProxyIDs
	APP_PROXY_Addins_dispid       =216        # from enum VdAppProtectionProxyIDs
	APP_PROXY_AnnoDisplayTime_dispid=85         # from enum VdAppProtectionProxyIDs
	APP_PROXY_AnnoDisplayValue_dispid=86         # from enum VdAppProtectionProxyIDs
	APP_PROXY_AppendOutput_dispid =223        # from enum VdAppProtectionProxyIDs
	APP_PROXY_Application_dispid  =3          # from enum VdAppProtectionProxyIDs
	APP_PROXY_AttributeCanHaveOatValue_dispid=74         # from enum VdAppProtectionProxyIDs
	APP_PROXY_AttributeValueMustBeUpper_dispid=77         # from enum VdAppProtectionProxyIDs
	APP_PROXY_Bindings_dispid     =219        # from enum VdAppProtectionProxyIDs
	APP_PROXY_BroadcastDBConfigModified_dispid=298        # from enum VdAppProtectionProxyIDs
	APP_PROXY_BrowseForSymbol_dispid=72         # from enum VdAppProtectionProxyIDs
	APP_PROXY_BusyCursor_dispid   =61         # from enum VdAppProtectionProxyIDs
	APP_PROXY_CheckIfNavigatorAddinsOpen_dispid=107        # from enum VdAppProtectionProxyIDs
	APP_PROXY_ClearAllLibraries_dispid=28         # from enum VdAppProtectionProxyIDs
	APP_PROXY_ClearEEVMMode_dispid=248        # from enum VdAppProtectionProxyIDs
	APP_PROXY_ClientAdvisorFlags_dispid=9          # from enum VdAppProtectionProxyIDs
	APP_PROXY_CloseNavigatorAddins_dispid=108        # from enum VdAppProtectionProxyIDs
	APP_PROXY_CloseProject_dispid =274        # from enum VdAppProtectionProxyIDs
	APP_PROXY_CnsFileString_dispid=102        # from enum VdAppProtectionProxyIDs
	APP_PROXY_CommandBars_dispid  =215        # from enum VdAppProtectionProxyIDs
	APP_PROXY_CommandDisable_dispid=43         # from enum VdAppProtectionProxyIDs
	APP_PROXY_CommandEnable_dispid=42         # from enum VdAppProtectionProxyIDs
	APP_PROXY_CommandLineArguments_dispid=210        # from enum VdAppProtectionProxyIDs
	APP_PROXY_CommandRemove_dispid=44         # from enum VdAppProtectionProxyIDs
	APP_PROXY_CommandsManager_dispid=220        # from enum VdAppProtectionProxyIDs
	APP_PROXY_ConvertSchematicToICT_dispid=286        # from enum VdAppProtectionProxyIDs
	APP_PROXY_ConvertSymbol_dispid=252        # from enum VdAppProtectionProxyIDs
	APP_PROXY_Cookies_dispid      =94         # from enum VdAppProtectionProxyIDs
	APP_PROXY_CreateProjectLibrary_dispid=304        # from enum VdAppProtectionProxyIDs
	APP_PROXY_CreateToolbar_dispid=255        # from enum VdAppProtectionProxyIDs
	APP_PROXY_CurrentProject_dispid=55         # from enum VdAppProtectionProxyIDs
	APP_PROXY_DataObjExists_dispid=37         # from enum VdAppProtectionProxyIDs
	APP_PROXY_DataObjGetPath_dispid=38         # from enum VdAppProtectionProxyIDs
	APP_PROXY_DataTag_dispid      =291        # from enum VdAppProtectionProxyIDs
	APP_PROXY_DeleteBlock_dispid  =256        # from enum VdAppProtectionProxyIDs
	APP_PROXY_DeleteLibraryAndSaveIni_dispid=105        # from enum VdAppProtectionProxyIDs
	APP_PROXY_DeleteLibrary_dispid=26         # from enum VdAppProtectionProxyIDs
	APP_PROXY_DeleteSheet_dispid  =76         # from enum VdAppProtectionProxyIDs
	APP_PROXY_DesignBlocks_dispid =50         # from enum VdAppProtectionProxyIDs
	APP_PROXY_DesignComponents_dispid=59         # from enum VdAppProtectionProxyIDs
	APP_PROXY_DesignNets_dispid   =276        # from enum VdAppProtectionProxyIDs
	APP_PROXY_DesignPaths_dispid  =54         # from enum VdAppProtectionProxyIDs
	APP_PROXY_DesignSearcher_dispid=297        # from enum VdAppProtectionProxyIDs
	APP_PROXY_DisableSelectionBroadcast_dispid=272        # from enum VdAppProtectionProxyIDs
	APP_PROXY_Documents_dispid    =1          # from enum VdAppProtectionProxyIDs
	APP_PROXY_EDXEngine_dispid    =281        # from enum VdAppProtectionProxyIDs
	APP_PROXY_EnableEEVMMode_dispid=247        # from enum VdAppProtectionProxyIDs
	APP_PROXY_EnableSelectionBroadcast_dispid=271        # from enum VdAppProtectionProxyIDs
	APP_PROXY_ExecuteCommandByID_dispid=307        # from enum VdAppProtectionProxyIDs
	APP_PROXY_ExecuteCommand_dispid=29         # from enum VdAppProtectionProxyIDs
	APP_PROXY_ExecuteMenuCommand_dispid=89         # from enum VdAppProtectionProxyIDs
	APP_PROXY_ExportForeignDatabase_dispid=264        # from enum VdAppProtectionProxyIDs
	APP_PROXY_ExportSymbol_dispid =280        # from enum VdAppProtectionProxyIDs
	APP_PROXY_ExtractPCB_dispid   =275        # from enum VdAppProtectionProxyIDs
	APP_PROXY_FireCentralLibraryReload_dispid=257        # from enum VdAppProtectionProxyIDs
	APP_PROXY_Flows_dispid        =98         # from enum VdAppProtectionProxyIDs
	APP_PROXY_FullName_dispid     =4          # from enum VdAppProtectionProxyIDs
	APP_PROXY_GenStatusIndicatorState_dispid=277        # from enum VdAppProtectionProxyIDs
	APP_PROXY_GetActiveiCDBDesign_dispid=229        # from enum VdAppProtectionProxyIDs
	APP_PROXY_GetClassDefinitions_dispid=79         # from enum VdAppProtectionProxyIDs
	APP_PROXY_GetCommonPropertyManager_dispid=243        # from enum VdAppProtectionProxyIDs
	APP_PROXY_GetConfigurationProperty_dispid=244        # from enum VdAppProtectionProxyIDs
	APP_PROXY_GetCurrentProdLib_dispid=312        # from enum VdAppProtectionProxyIDs
	APP_PROXY_GetDefaultColor_dispid=261        # from enum VdAppProtectionProxyIDs
	APP_PROXY_GetDefaultProdLib_dispid=313        # from enum VdAppProtectionProxyIDs
	APP_PROXY_GetFramework_dispid =242        # from enum VdAppProtectionProxyIDs
	APP_PROXY_GetICTContents_dispid=258        # from enum VdAppProtectionProxyIDs
	APP_PROXY_GetICTDocuments_dispid=259        # from enum VdAppProtectionProxyIDs
	APP_PROXY_GetLastErrorId_dispid=240        # from enum VdAppProtectionProxyIDs
	APP_PROXY_GetLastErrorString_dispid=239        # from enum VdAppProtectionProxyIDs
	APP_PROXY_GetLibSpec_dispid   =317        # from enum VdAppProtectionProxyIDs
	APP_PROXY_GetLibraries_dispid =30         # from enum VdAppProtectionProxyIDs
	APP_PROXY_GetPEFlowMode_dispid=283        # from enum VdAppProtectionProxyIDs
	APP_PROXY_GetProdLibReadOnly_dispid=315        # from enum VdAppProtectionProxyIDs
	APP_PROXY_GetProdLibs_dispid  =310        # from enum VdAppProtectionProxyIDs
	APP_PROXY_GetProjectData_dispid=228        # from enum VdAppProtectionProxyIDs
	APP_PROXY_GetProjectType_dispid=299        # from enum VdAppProtectionProxyIDs
	APP_PROXY_GetTypeFromIDispatch_dispid=20         # from enum VdAppProtectionProxyIDs
	APP_PROXY_Guid_dispid         =22         # from enum VdAppProtectionProxyIDs
	APP_PROXY_HTMLDocuments_dispid=213        # from enum VdAppProtectionProxyIDs
	APP_PROXY_HideModelProperties =302        # from enum VdAppProtectionProxyIDs
	APP_PROXY_ImportEEToPE_dispid =296        # from enum VdAppProtectionProxyIDs
	APP_PROXY_ImportForeignDatabase_dispid=265        # from enum VdAppProtectionProxyIDs
	APP_PROXY_ImportPADS_dispid   =314        # from enum VdAppProtectionProxyIDs
	APP_PROXY_ImportPadsPE_dispid =288        # from enum VdAppProtectionProxyIDs
	APP_PROXY_Initialize_dispid   =203        # from enum VdAppProtectionProxyIDs
	APP_PROXY_InsertSheet_dispid  =75         # from enum VdAppProtectionProxyIDs
	APP_PROXY_Interactive_dispid  =205        # from enum VdAppProtectionProxyIDs
	APP_PROXY_IsAppStarted_dispid =294        # from enum VdAppProtectionProxyIDs
	APP_PROXY_IsEEVMModeEnabled_dispid=249        # from enum VdAppProtectionProxyIDs
	APP_PROXY_IsLibDeletable_dispid=24         # from enum VdAppProtectionProxyIDs
	APP_PROXY_IsManagedBlockSource_dispid=306        # from enum VdAppProtectionProxyIDs
	APP_PROXY_IsManagedBlock_dispid=305        # from enum VdAppProtectionProxyIDs
	APP_PROXY_IsProdLibSet_dispid =316        # from enum VdAppProtectionProxyIDs
	APP_PROXY_IsProjectOpened_dispid=295        # from enum VdAppProtectionProxyIDs
	APP_PROXY_IsReadOnlyMode_dispid=293        # from enum VdAppProtectionProxyIDs
	APP_PROXY_IsReferenceApplication_dispid=290        # from enum VdAppProtectionProxyIDs
	APP_PROXY_KickViewbase_dispid =97         # from enum VdAppProtectionProxyIDs
	APP_PROXY_LMGetSymbolLibPath_dispid=284        # from enum VdAppProtectionProxyIDs
	APP_PROXY_LMSetSymbolLibPath_dispid=285        # from enum VdAppProtectionProxyIDs
	APP_PROXY_LaunchSymbolEditor_dispid=263        # from enum VdAppProtectionProxyIDs
	APP_PROXY_LicenseMode_dispid  =91         # from enum VdAppProtectionProxyIDs
	APP_PROXY_MGCDesignerDataManagement_dispid=303        # from enum VdAppProtectionProxyIDs
	APP_PROXY_MakeReusableBlock_dispid=103        # from enum VdAppProtectionProxyIDs
	APP_PROXY_MoveLibraryAndSaveIni_dispid=106        # from enum VdAppProtectionProxyIDs
	APP_PROXY_MoveLibrary_dispid  =27         # from enum VdAppProtectionProxyIDs
	APP_PROXY_Name_dispid         =5          # from enum VdAppProtectionProxyIDs
	APP_PROXY_NewProject_dispid   =251        # from enum VdAppProtectionProxyIDs
	APP_PROXY_ObjectColor_dispid  =65         # from enum VdAppProtectionProxyIDs
	APP_PROXY_OpenBlocks_dispid   =82         # from enum VdAppProtectionProxyIDs
	APP_PROXY_OpenDetailedComponentView_dispid=319        # from enum VdAppProtectionProxyIDs
	APP_PROXY_OpenDetailedManagedBlockView_dispid=320        # from enum VdAppProtectionProxyIDs
	APP_PROXY_OpenProject_dispid  =227        # from enum VdAppProtectionProxyIDs
	APP_PROXY_OpenReference_dispid=292        # from enum VdAppProtectionProxyIDs
	APP_PROXY_OpenURL_dispid      =225        # from enum VdAppProtectionProxyIDs
	APP_PROXY_OptionLevel_dispid  =73         # from enum VdAppProtectionProxyIDs
	APP_PROXY_ParamAddListName_dispid=39         # from enum VdAppProtectionProxyIDs
	APP_PROXY_ParamGetListNames_dispid=84         # from enum VdAppProtectionProxyIDs
	APP_PROXY_ParamGetMode_dispid =14         # from enum VdAppProtectionProxyIDs
	APP_PROXY_ParamGetValue_dispid=13         # from enum VdAppProtectionProxyIDs
	APP_PROXY_ParamSetMode_dispid =15         # from enum VdAppProtectionProxyIDs
	APP_PROXY_ParamSetValue_dispid=12         # from enum VdAppProtectionProxyIDs
	APP_PROXY_Parent_dispid       =6          # from enum VdAppProtectionProxyIDs
	APP_PROXY_PreviewDecal_dispid =78         # from enum VdAppProtectionProxyIDs
	APP_PROXY_PrimaryDirectory_dispid=56         # from enum VdAppProtectionProxyIDs
	APP_PROXY_PrintProject_dispid =221        # from enum VdAppProtectionProxyIDs
	APP_PROXY_ProductionLibraryLimitationsChanged_dispid=308        # from enum VdAppProtectionProxyIDs
	APP_PROXY_ProjMan_dispid      =88         # from enum VdAppProtectionProxyIDs
	APP_PROXY_Project_dispid      =101        # from enum VdAppProtectionProxyIDs
	APP_PROXY_PushPath_dispid     =69         # from enum VdAppProtectionProxyIDs
	APP_PROXY_QueryBlocks_dispid  =45         # from enum VdAppProtectionProxyIDs
	APP_PROXY_QueryPages_dispid   =46         # from enum VdAppProtectionProxyIDs
	APP_PROXY_Query_dispid        =83         # from enum VdAppProtectionProxyIDs
	APP_PROXY_QueueSelectEvents_dispid=224        # from enum VdAppProtectionProxyIDs
	APP_PROXY_Quit_dispid         =226        # from enum VdAppProtectionProxyIDs
	APP_PROXY_ReadIni_dispid      =202        # from enum VdAppProtectionProxyIDs
	APP_PROXY_RegisterOLECommand_dispid=33         # from enum VdAppProtectionProxyIDs
	APP_PROXY_RemoveProjectSettingTab_dispid=51         # from enum VdAppProtectionProxyIDs
	APP_PROXY_ReplacePart         =300        # from enum VdAppProtectionProxyIDs
	APP_PROXY_RunISE_dispid       =289        # from enum VdAppProtectionProxyIDs
	APP_PROXY_SaveIni_dispid      =34         # from enum VdAppProtectionProxyIDs
	APP_PROXY_SchematicSheetDocuments_dispid=212        # from enum VdAppProtectionProxyIDs
	APP_PROXY_SelectComponent_dispid=266        # from enum VdAppProtectionProxyIDs
	APP_PROXY_SelectNet_dispid    =267        # from enum VdAppProtectionProxyIDs
	APP_PROXY_SelectPathCompPin_dispid=68         # from enum VdAppProtectionProxyIDs
	APP_PROXY_SelectPath_dispid   =67         # from enum VdAppProtectionProxyIDs
	APP_PROXY_SetButtonBitmap_dispid=253        # from enum VdAppProtectionProxyIDs
	APP_PROXY_SetButtonResourceDLL_dispid=254        # from enum VdAppProtectionProxyIDs
	APP_PROXY_SetClientAdvisor_dispid=11         # from enum VdAppProtectionProxyIDs
	APP_PROXY_SetConfigurationProperty_dispid=245        # from enum VdAppProtectionProxyIDs
	APP_PROXY_SetDefaultColor_dispid=260        # from enum VdAppProtectionProxyIDs
	APP_PROXY_SetEnvVariable_dispid=211        # from enum VdAppProtectionProxyIDs
	APP_PROXY_SetLibAddComp_dispid=49         # from enum VdAppProtectionProxyIDs
	APP_PROXY_SetLibFileNew_dispid=47         # from enum VdAppProtectionProxyIDs
	APP_PROXY_SetLibFileOpen_dispid=48         # from enum VdAppProtectionProxyIDs
	APP_PROXY_SetProdLib_dispid   =311        # from enum VdAppProtectionProxyIDs
	APP_PROXY_SetRedraw_dispid    =222        # from enum VdAppProtectionProxyIDs
	APP_PROXY_SetViewAnalogFlag_dispid=52         # from enum VdAppProtectionProxyIDs
	APP_PROXY_SheetsEditMode_dispid=279        # from enum VdAppProtectionProxyIDs
	APP_PROXY_ShellCmd_dispid     =218        # from enum VdAppProtectionProxyIDs
	APP_PROXY_ShouldProvideDetailedComponentView_dispid=318        # from enum VdAppProtectionProxyIDs
	APP_PROXY_SilentMode_dispid   =250        # from enum VdAppProtectionProxyIDs
	APP_PROXY_SourceDocuments_dispid=214        # from enum VdAppProtectionProxyIDs
	APP_PROXY_StartMigration_dispid=246        # from enum VdAppProtectionProxyIDs
	APP_PROXY_StartVNSD           =301        # from enum VdAppProtectionProxyIDs
	APP_PROXY_StatusBarText_dispid=206        # from enum VdAppProtectionProxyIDs
	APP_PROXY_SupportsProdLibLimitation_dispid=309        # from enum VdAppProtectionProxyIDs
	APP_PROXY_SynchronizesViewBase_dispid=66         # from enum VdAppProtectionProxyIDs
	APP_PROXY_TextViews_dispid    =57         # from enum VdAppProtectionProxyIDs
	APP_PROXY_ToolbarAction_dispid=262        # from enum VdAppProtectionProxyIDs
	APP_PROXY_UnloadClassDefinitions_dispid=81         # from enum VdAppProtectionProxyIDs
	APP_PROXY_UnregisterOLECommand_dispid=36         # from enum VdAppProtectionProxyIDs
	APP_PROXY_UpdateMenuBar_dispid=282        # from enum VdAppProtectionProxyIDs
	APP_PROXY_UserControl_dispid  =21         # from enum VdAppProtectionProxyIDs
	APP_PROXY_Validate_dispid     =268        # from enum VdAppProtectionProxyIDs
	APP_PROXY_Version_dispid      =209        # from enum VdAppProtectionProxyIDs
	APP_PROXY_ViewBaseSession_dispid=64         # from enum VdAppProtectionProxyIDs
	APP_PROXY_Visible_dispid      =204        # from enum VdAppProtectionProxyIDs
	VDARC_PT_ONE                  =0          # from enum VdArcPoint
	VDARC_PT_THREE                =2          # from enum VdArcPoint
	VDARC_PT_TWO                  =1          # from enum VdArcPoint
	VGARROWNONE                   =3          # from enum VdArrowType
	VGARROWPOINT1                 =0          # from enum VdArrowType
	VGARROWPOINT12                =2          # from enum VdArrowType
	VGARROWPOINT2                 =1          # from enum VdArrowType
	BL_AddArc_dispid              =15         # from enum VdBlockDispIDs
	BL_AddAttribute_dispid        =23         # from enum VdBlockDispIDs
	BL_AddBatchAttributes_dispid  =28         # from enum VdBlockDispIDs
	BL_AddBox_dispid              =16         # from enum VdBlockDispIDs
	BL_AddCircle_dispid           =17         # from enum VdBlockDispIDs
	BL_AddComponentMoveModeEx_dispid=51         # from enum VdBlockDispIDs
	BL_AddComponentMoveMode_dispid=25         # from enum VdBlockDispIDs
	BL_AddComponent_dispid        =18         # from enum VdBlockDispIDs
	BL_AddCompositeComponentMoveMode=72         # from enum VdBlockDispIDs
	BL_AddFrameBoard_dispid       =75         # from enum VdBlockDispIDs
	BL_AddFub_dispid              =19         # from enum VdBlockDispIDs
	BL_AddLine2_dispid            =70         # from enum VdBlockDispIDs
	BL_AddLine_dispid             =29         # from enum VdBlockDispIDs
	BL_AddNetEx_dispid            =77         # from enum VdBlockDispIDs
	BL_AddNet_dispid              =20         # from enum VdBlockDispIDs
	BL_AddPartInstance_dispid     =59         # from enum VdBlockDispIDs
	BL_AddPinAtLocation_dispid    =57         # from enum VdBlockDispIDs
	BL_AddPin_dispid              =21         # from enum VdBlockDispIDs
	BL_AddReuseBlockInstanceEx_dispid=64         # from enum VdBlockDispIDs
	BL_AddReuseBlockInstance_dispid=63         # from enum VdBlockDispIDs
	BL_AddSymbolInstance_dispid   =58         # from enum VdBlockDispIDs
	BL_AddText_dispid             =22         # from enum VdBlockDispIDs
	BL_Application_dispid         =3          # from enum VdBlockDispIDs
	BL_ApplySymbolUpdate_dispid   =34         # from enum VdBlockDispIDs
	BL_ArraySelected_dispid       =76         # from enum VdBlockDispIDs
	BL_Attributes_dispid          =1          # from enum VdBlockDispIDs
	BL_ChangeBorder_dispid        =40         # from enum VdBlockDispIDs
	BL_ChangeComponentPreserveRefdes_dispid=42         # from enum VdBlockDispIDs
	BL_ChangeComponent_dispid     =24         # from enum VdBlockDispIDs
	BL_CheckIfWirUpToDateWithCDB_dispid=55         # from enum VdBlockDispIDs
	BL_ClearHighlight_dispid      =37         # from enum VdBlockDispIDs
	BL_ConstraintObjectDefinitions_dispid=50         # from enum VdBlockDispIDs
	BL_DataType_dispid            =5          # from enum VdBlockDispIDs
	BL_DeSelectAll_dispid         =14         # from enum VdBlockDispIDs
	BL_DeleteAttribute_dispid     =48         # from enum VdBlockDispIDs
	BL_DeleteBorder_dispid        =39         # from enum VdBlockDispIDs
	BL_DeletePackagedAttribute_dispid=45         # from enum VdBlockDispIDs
	BL_DeleteSelected_dispid      =26         # from enum VdBlockDispIDs
	BL_DisableUpdateStoring_dispid=67         # from enum VdBlockDispIDs
	BL_DisplayType_dispid         =69         # from enum VdBlockDispIDs
	BL_DissolveReuseBlock_dispid  =78         # from enum VdBlockDispIDs
	BL_EnableUpdateStoring_dispid =68         # from enum VdBlockDispIDs
	BL_EndUndoTransaction_dispid  =53         # from enum VdBlockDispIDs
	BL_FindAttribute_dispid       =30         # from enum VdBlockDispIDs
	BL_GetAttributeValues_dispid  =46         # from enum VdBlockDispIDs
	BL_GetBatchAttributes_dispid  =27         # from enum VdBlockDispIDs
	BL_GetBboxPoint_dispid        =12         # from enum VdBlockDispIDs
	BL_GetChildBlock_dispid       =60         # from enum VdBlockDispIDs
	BL_GetForwardPCB              =73         # from enum VdBlockDispIDs
	BL_GetName_dispid             =11         # from enum VdBlockDispIDs
	BL_GetPackagedAttributeValues_dispid=43         # from enum VdBlockDispIDs
	BL_GetPackagedName_dispid     =49         # from enum VdBlockDispIDs
	BL_GetReuseBlockMergeData_dispid=65         # from enum VdBlockDispIDs
	BL_InsertBorder_dispid        =38         # from enum VdBlockDispIDs
	BL_IsBorderSymbol_dispid      =61         # from enum VdBlockDispIDs
	BL_IsFub_dispid               =54         # from enum VdBlockDispIDs
	BL_IsReadOnly_dispid          =66         # from enum VdBlockDispIDs
	BL_IsValid_dispid             =62         # from enum VdBlockDispIDs
	BL_LibraryName_dispid         =6          # from enum VdBlockDispIDs
	BL_LibraryType_dispid         =33         # from enum VdBlockDispIDs
	BL_MoveSelected_dispid        =71         # from enum VdBlockDispIDs
	BL_OpenMode_dispid            =8          # from enum VdBlockDispIDs
	BL_Parent_dispid              =4          # from enum VdBlockDispIDs
	BL_Path_dispid                =31         # from enum VdBlockDispIDs
	BL_PromoteSymbolNumbers_dispid=35         # from enum VdBlockDispIDs
	BL_RepositionAttributesAsOnSymbol_dispid=36         # from enum VdBlockDispIDs
	BL_SetAttributeValue_dispid   =47         # from enum VdBlockDispIDs
	BL_SetBoundingBox_dispid      =56         # from enum VdBlockDispIDs
	BL_SetPackagedAttributeValue_dispid=44         # from enum VdBlockDispIDs
	BL_SetZSheetSize_dispid       =13         # from enum VdBlockDispIDs
	BL_SheetNum_dispid            =10         # from enum VdBlockDispIDs
	BL_SheetSize_dispid           =9          # from enum VdBlockDispIDs
	BL_StartUndoTransaction_dispid=52         # from enum VdBlockDispIDs
	BL_SymbolType_dispid          =7          # from enum VdBlockDispIDs
	BL_Type_dispid                =2          # from enum VdBlockDispIDs
	BL_UpdateBorder_dispid        =41         # from enum VdBlockDispIDs
	BL_UpdateOutline_dispid       =74         # from enum VdBlockDispIDs
	BL_UserData_dispid            =32         # from enum VdBlockDispIDs
	VD_FALSE                      =0          # from enum VdBoolean
	VD_TRUE                       =1          # from enum VdBoolean
	VD_BUS                        =1          # from enum VdBusOrWire
	VD_SD_WIRE                    =2          # from enum VdBusOrWire
	VD_SD_WIRE_BUS                =3          # from enum VdBusOrWire
	VD_WIRE                       =0          # from enum VdBusOrWire
	VGCOLORBACKGROUND             =67108869   # from enum VdColor
	VGCOLORBASE                   =67108866   # from enum VdColor
	VGCOLORBLACK                  =0          # from enum VdColor
	VGCOLORBLUE                   =8388608    # from enum VdColor
	VGCOLORBROWN                  =32896      # from enum VdColor
	VGCOLORCYAN                   =8421376    # from enum VdColor
	VGCOLORDARK_GREY              =8421504    # from enum VdColor
	VGCOLORFOREGROUND             =67108870   # from enum VdColor
	VGCOLORGREEN                  =32768      # from enum VdColor
	VGCOLORHIGHLIGHT              =67108865   # from enum VdColor
	VGCOLORINDENTED               =67108867   # from enum VdColor
	VGCOLORLT_BLUE                =16711680   # from enum VdColor
	VGCOLORLT_CYAN                =16776960   # from enum VdColor
	VGCOLORLT_GREEN               =65280      # from enum VdColor
	VGCOLORLT_GREY                =12632256   # from enum VdColor
	VGCOLORLT_MAGENTA             =16711935   # from enum VdColor
	VGCOLORLT_RED                 =255        # from enum VdColor
	VGCOLORMAGENTA                =8388736    # from enum VdColor
	VGCOLORRED                    =128        # from enum VdColor
	VGCOLORSHADOWED               =67108868   # from enum VdColor
	VGCOLORWHITE                  =16777215   # from enum VdColor
	VGCOLORYELLOW                 =65535      # from enum VdColor
	VdCompInstance_FALSE          =1          # from enum VdCompInstanceForwardPCB
	VdCompInstance_FromSymbol     =2          # from enum VdCompInstanceForwardPCB
	VdCompInstance_TRUE           =0          # from enum VdCompInstanceForwardPCB
	VDLOWERLEFT                   =0          # from enum VdCorner
	VDUPPERRIGHT                  =1          # from enum VdCorner
	VDCREATE_AFTER_NOTIFY         =1          # from enum VdCreateTime
	VDCREATE_BEFORE_NOTIFY        =0          # from enum VdCreateTime
	VDDMDUMPFILTER_ALL            =0          # from enum VdDMDumpPropertiesFilter
	VDDMDUMPFILTER_CUSTOM         =2          # from enum VdDMDumpPropertiesFilter
	VDDMDUMPFILTER_DEFINED_AS_ARGUMENT=3          # from enum VdDMDumpPropertiesFilter
	VDDMDUMPFILTER_VISIBLE        =1          # from enum VdDMDumpPropertiesFilter
	VDACCES_NONE                  =0          # from enum VdDMEntityAccessType
	VDACCES_READONLY              =1          # from enum VdDMEntityAccessType
	VDACCES_READWRITE             =2          # from enum VdDMEntityAccessType
	VDES_LAYOUT                   =1          # from enum VdDMEntityType
	VDES_SCHEMATIC                =2          # from enum VdDMEntityType
	VPADSPRO_DES_SCHEMATIC        =256        # from enum VdDMEntityType
	VSYS_DESIGN                   =4          # from enum VdDMEntityType
	VDDT_DOCUMENTATION            =2          # from enum VdDataType
	VDDT_PIN                      =4          # from enum VdDataType
	VDDT_SCHEMATIC                =0          # from enum VdDataType
	VDDT_SYMBOL                   =1          # from enum VdDataType
	VDDT_WIRELIST                 =3          # from enum VdDataType
	VDDIT_ICT                     =1          # from enum VdDisplayType
	VDDIT_SCHEMATIC               =0          # from enum VdDisplayType
	VDDA_BLOCK_WRITABLE           =0          # from enum VdDocumentAccess
	VDDA_OAT_READ_ONLY            =6          # from enum VdDocumentAccess
	VDDA_OAT_WRITABLE             =2          # from enum VdDocumentAccess
	VDDA_SCH_READ_LOCK            =9          # from enum VdDocumentAccess
	VDDA_SCH_READ_ONLY            =5          # from enum VdDocumentAccess
	VDDA_SCH_WRITABLE             =1          # from enum VdDocumentAccess
	VDDA_SYM_READ_LOCK            =10         # from enum VdDocumentAccess
	VDDA_SYM_READ_ONLY            =7          # from enum VdDocumentAccess
	VDDA_SYM_WRITABLE             =3          # from enum VdDocumentAccess
	VDDA_WIR_READ_ONLY            =8          # from enum VdDocumentAccess
	VDDA_WIR_WRITABLE             =4          # from enum VdDocumentAccess
	VDFILL_DIAGDN1                =2          # from enum VdFillStyle
	VDFILL_DIAGDN2                =5          # from enum VdFillStyle
	VDFILL_DIAGUP1                =6          # from enum VdFillStyle
	VDFILL_DIAGUP2                =3          # from enum VdFillStyle
	VDFILL_GREY04                 =15         # from enum VdFillStyle
	VDFILL_GREY08                 =4          # from enum VdFillStyle
	VDFILL_GREY50                 =13         # from enum VdFillStyle
	VDFILL_GREY92                 =14         # from enum VdFillStyle
	VDFILL_GRID1                  =10         # from enum VdFillStyle
	VDFILL_GRID2                  =9          # from enum VdFillStyle
	VDFILL_HOLLOW                 =0          # from enum VdFillStyle
	VDFILL_HORIZ                  =7          # from enum VdFillStyle
	VDFILL_SOLID                  =1          # from enum VdFillStyle
	VDFILL_VERT                   =8          # from enum VdFillStyle
	VDFILL_X1                     =12         # from enum VdFillStyle
	VDFILL_X2                     =11         # from enum VdFillStyle
	VDFONT_FIXED                  =0          # from enum VdFont
	VDFONT_GOTHIC                 =9          # from enum VdFont
	VDFONT_KANJI                  =11         # from enum VdFont
	VDFONT_OLD_ENGLISH            =10         # from enum VdFont
	VDFONT_PLOT                   =12         # from enum VdFont
	VDFONT_ROMAN                  =1          # from enum VdFont
	VDFONT_ROMAN_B                =3          # from enum VdFont
	VDFONT_ROMAN_BI               =4          # from enum VdFont
	VDFONT_ROMAN_I                =2          # from enum VdFont
	VDFONT_SANS_SERIF             =5          # from enum VdFont
	VDFONT_SANS_SERIF_B           =7          # from enum VdFont
	VDFONT_SCRIPT                 =6          # from enum VdFont
	VDFONT_SCRIPT_B               =8          # from enum VdFont
	VDGRADIENT_DIAGONAL1          =3          # from enum VdGradientType
	VDGRADIENT_DIAGONAL2          =4          # from enum VdGradientType
	VDGRADIENT_HORIZONTAL         =2          # from enum VdGradientType
	VDGRADIENT_NONE               =0          # from enum VdGradientType
	VDGRADIENT_VERTICAL           =1          # from enum VdGradientType
	VDICTATTR_PARENT              =100        # from enum VdICTAttrEnum
	VDICTBLOCK_ADDINSTANCE        =101        # from enum VdICTBlockEnum
	VDICTBLOCK_ADDNET             =102        # from enum VdICTBlockEnum
	VDICTBLOCK_CONNECTOBJS        =107        # from enum VdICTBlockEnum
	VDICTBLOCK_DISCONNECTOBJS     =108        # from enum VdICTBlockEnum
	VDICTBLOCK_GETINSTANCES       =105        # from enum VdICTBlockEnum
	VDICTBLOCK_GETNETS            =104        # from enum VdICTBlockEnum
	VDICTBLOCK_PARENT             =100        # from enum VdICTBlockEnum
	VDICTBLOCK_PROMOTESYMNO       =103        # from enum VdICTBlockEnum
	VDICTBLOCK_REMOVEOBJ          =106        # from enum VdICTBlockEnum
	VDICTBLOCK_SETOBJNAME         =109        # from enum VdICTBlockEnum
	VDICTCOMP_GETATTRSNAMES       =101        # from enum VdICTCompEnum
	VDICTCOMP_GETATTRVALUE        =102        # from enum VdICTCompEnum
	VDICTCOMP_GETDEFNAME          =105        # from enum VdICTCompEnum
	VDICTCOMP_GETLIBRARYNAME      =106        # from enum VdICTCompEnum
	VDICTCOMP_GETPINS             =108        # from enum VdICTCompEnum
	VDICTCOMP_PARENT              =100        # from enum VdICTCompEnum
	VDICTCOMP_REMATTRVALUE        =104        # from enum VdICTCompEnum
	VDICTCOMP_SETATTRVALUE        =103        # from enum VdICTCompEnum
	VDICTNET_GETPINS              =101        # from enum VdICTNetEnum
	VDICTNET_PARENT               =100        # from enum VdICTNetEnum
	VDICTOBJ_GETNAME              =2          # from enum VdICTObjEnum
	VDICTOBJ_GETUID               =3          # from enum VdICTObjEnum
	VDICTOBJ_PARENT               =1          # from enum VdICTObjEnum
	VDICTPin_GETNETS              =101        # from enum VdICTPinEnum
	VDICTPin_PARENT               =100        # from enum VdICTPinEnum
	VDICTV_ADD_REUSE_BLOCK        =108        # from enum VdICTViewEnum
	VDICTV_BLOCK                  =100        # from enum VdICTViewEnum
	VDICTV_GET_NAME               =105        # from enum VdICTViewEnum
	VDICTV_QUERY                  =107        # from enum VdICTViewEnum
	VDICTV_SELECT_BY_NAME         =106        # from enum VdICTViewEnum
	VDICTV_SET_SIGNALS_VIEW       =102        # from enum VdICTViewEnum
	VDICTV_SET_SYMBOLS_VIEW       =103        # from enum VdICTViewEnum
	VDICTV_TOPBLOCK               =101        # from enum VdICTViewEnum
	VDICTV_TOP_LEVEL_NAME         =104        # from enum VdICTViewEnum
	VDJT_BUS                      =6          # from enum VdJointType
	VDJT_BUSCORNER                =9          # from enum VdJointType
	VDJT_BUSPIN                   =8          # from enum VdJointType
	VDJT_BUSSINGLE                =7          # from enum VdJointType
	VDJT_BUSSOLDER                =11         # from enum VdJointType
	VDJT_BUSSTRAIGHT              =10         # from enum VdJointType
	VDJT_CORNER                   =3          # from enum VdJointType
	VDJT_LONER                    =0          # from enum VdJointType
	VDJT_PIN                      =2          # from enum VdJointType
	VDJT_SINGLE                   =1          # from enum VdJointType
	VDJT_SOLDER                   =5          # from enum VdJointType
	VDJT_STRAIGHT                 =4          # from enum VdJointType
	VDLABELINVISIBLE              =0          # from enum VdLabelVisibility
	VDLABELVISIBLE                =1          # from enum VdLabelVisibility
	VDLT_MEGAFILE                 =3          # from enum VdLibraryType
	VDLT_PRIMARY                  =0          # from enum VdLibraryType
	VDLT_READONLY                 =2          # from enum VdLibraryType
	VDLT_WRITEABLE                =1          # from enum VdLibraryType
	VGLINECAPBUTT                 =0          # from enum VdLineCap
	VGLINECAPNOT_LAST             =3          # from enum VdLineCap
	VGLINECAPPROJECTING           =2          # from enum VdLineCap
	VGLINECAPROUND                =1          # from enum VdLineCap
	VGLINEJOINBEVEL               =2          # from enum VdLineJoin
	VGLINEJOINMITER               =0          # from enum VdLineJoin
	VGLINEJOINROUND               =1          # from enum VdLineJoin
	VGLINEPATTERNBIGDASH          =4          # from enum VdLinePattern
	VGLINEPATTERNCENTER           =2          # from enum VdLinePattern
	VGLINEPATTERNDASH             =1          # from enum VdLinePattern
	VGLINEPATTERNDASHDOT          =6          # from enum VdLinePattern
	VGLINEPATTERNDOT              =5          # from enum VdLinePattern
	VGLINEPATTERNMEDDASH          =7          # from enum VdLinePattern
	VGLINEPATTERNPHANTOM          =3          # from enum VdLinePattern
	VGLINEPATTERNSOLID            =0          # from enum VdLinePattern
	VDLINE_BIGDASH                =4          # from enum VdLineStyle
	VDLINE_CENTER                 =2          # from enum VdLineStyle
	VDLINE_DASH                   =1          # from enum VdLineStyle
	VDLINE_DASHDOT                =6          # from enum VdLineStyle
	VDLINE_DOT                    =5          # from enum VdLineStyle
	VDLINE_MEDDASH                =7          # from enum VdLineStyle
	VDLINE_PHANTOM                =3          # from enum VdLineStyle
	VDLINE_SOLID                  =0          # from enum VdLineStyle
	FULL_PATH_FROM_BLOCK          =2          # from enum VdNameType
	FULL_PATH_NAME                =0          # from enum VdNameType
	ICDB_FULL_PATH_NAME           =3          # from enum VdNameType
	SHORT_NAME                    =1          # from enum VdNameType
	VDCN_APP_QUIT_AFTER           =131072     # from enum VdNotifyFlag
	VDCN_APP_QUIT_BEFORE          =65536      # from enum VdNotifyFlag
	VDCN_CREATE_AFTER             =4          # from enum VdNotifyFlag
	VDCN_CREATE_BEFORE            =2          # from enum VdNotifyFlag
	VDCN_DOC_CLOSE_AFTER          =32768      # from enum VdNotifyFlag
	VDCN_DOC_CLOSE_BEFORE         =16384      # from enum VdNotifyFlag
	VDCN_DOC_SAVEAS_AFTER         =8192       # from enum VdNotifyFlag
	VDCN_DOC_SAVEAS_BEFORE        =4096       # from enum VdNotifyFlag
	VDCN_DOC_SAVE_AFTER           =2048       # from enum VdNotifyFlag
	VDCN_DOC_SAVE_BEFORE          =256        # from enum VdNotifyFlag
	VDCN_LOAD_AFTER               =64         # from enum VdNotifyFlag
	VDCN_LOAD_BEFORE              =32         # from enum VdNotifyFlag
	VDCN_OBJ_COPY                 =262144     # from enum VdNotifyFlag
	VDCN_OBJ_CUT                  =524288     # from enum VdNotifyFlag
	VDCN_ONACTIVATE               =128        # from enum VdNotifyFlag
	VDCN_ONBUFFERPASTE            =1024       # from enum VdNotifyFlag
	VDCN_ONDELETE                 =512        # from enum VdNotifyFlag
	VDCN_SELECT                   =1          # from enum VdNotifyFlag
	VDCN_UPDATE                   =8          # from enum VdNotifyFlag
	ClassBOARD                    =11         # from enum VdObjectClass
	ClassDLY                      =10         # from enum VdObjectClass
	ClassOAT                      =4          # from enum VdObjectClass
	ClassPIN                      =3          # from enum VdObjectClass
	ClassPKT                      =5          # from enum VdObjectClass
	ClassSCH_PAGE                 =0          # from enum VdObjectClass
	ClassSPICE_MODEL              =12         # from enum VdObjectClass
	ClassSYMBOL                   =1          # from enum VdObjectClass
	ClassVHDL                     =6          # from enum VdObjectClass
	ClassWIRELIST                 =2          # from enum VdObjectClass
	ClassWVCWDFILE                =7          # from enum VdObjectClass
	ClassWVFILE                   =9          # from enum VdObjectClass
	ClassWVWDIRFILE               =8          # from enum VdObjectClass
	VDTL_ANNOTATION               =1036       # from enum VdObjectType
	VDTL_BACKGROUND               =1038       # from enum VdObjectType
	VDTL_BORDER                   =1040       # from enum VdObjectType
	VDTL_HIGHLIGHT                =1041       # from enum VdObjectType
	VDTL_SELECTION                =1037       # from enum VdObjectType
	VDTL_VALUE                    =1039       # from enum VdObjectType
	VDTS_ARC                      =4          # from enum VdObjectType
	VDTS_ATTRIBUTE                =6          # from enum VdObjectType
	VDTS_BLOCK                    =11         # from enum VdObjectType
	VDTS_BOX                      =1          # from enum VdObjectType
	VDTS_CIRCLE                   =3          # from enum VdObjectType
	VDTS_COMPONENT                =7          # from enum VdObjectType
	VDTS_COMPPIN                  =12         # from enum VdObjectType
	VDTS_CONNECTION               =14         # from enum VdObjectType
	VDTS_DESIGN                   =17         # from enum VdObjectType
	VDTS_FRAMEBOARD               =19         # from enum VdObjectType
	VDTS_LABEL                    =8          # from enum VdObjectType
	VDTS_LIBRARY                  =15         # from enum VdObjectType
	VDTS_LINE                     =0          # from enum VdObjectType
	VDTS_NET                      =5          # from enum VdObjectType
	VDTS_OATTRIBUTE               =10         # from enum VdObjectType
	VDTS_PIN                      =9          # from enum VdObjectType
	VDTS_POINT                    =16         # from enum VdObjectType
	VDTS_RIPPER                   =18         # from enum VdObjectType
	VDTS_SEGMENT                  =13         # from enum VdObjectType
	VDTS_TEXT                     =2          # from enum VdObjectType
	VDM_ALL                       =16384      # from enum VdObjectTypeMask
	VDM_ARC                       =16         # from enum VdObjectTypeMask
	VDM_ATTR                      =64         # from enum VdObjectTypeMask
	VDM_BLOCK                     =2048       # from enum VdObjectTypeMask
	VDM_BOX                       =2          # from enum VdObjectTypeMask
	VDM_CIRCLE                    =8          # from enum VdObjectTypeMask
	VDM_COMP                      =128        # from enum VdObjectTypeMask
	VDM_COMPPIN                   =4096       # from enum VdObjectTypeMask
	VDM_FRAMEBOARD                =524288     # from enum VdObjectTypeMask
	VDM_LABEL                     =256        # from enum VdObjectTypeMask
	VDM_LINE                      =1          # from enum VdObjectTypeMask
	VDM_NET                       =32         # from enum VdObjectTypeMask
	VDM_OAT                       =1024       # from enum VdObjectTypeMask
	VDM_PIN                       =512        # from enum VdObjectTypeMask
	VDM_SEGMENT                   =8192       # from enum VdObjectTypeMask
	VDM_TEXT                      =4          # from enum VdObjectTypeMask
	VDMD_OFF                      =0          # from enum VdOnOff
	VDMD_ON                       =1          # from enum VdOnOff
	VDM_READ_LOCK                 =1          # from enum VdOpenMode
	VDM_READ_ONLY                 =2          # from enum VdOpenMode
	VDM_READ_WRITE                =0          # from enum VdOpenMode
	VDORIENT_IDENTITY             =0          # from enum VdOrientation
	VDORIENT_MX                   =4          # from enum VdOrientation
	VDORIENT_MX180                =6          # from enum VdOrientation
	VDORIENT_MX270                =7          # from enum VdOrientation
	VDORIENT_MX90                 =5          # from enum VdOrientation
	VDORIENT_ROT180               =2          # from enum VdOrientation
	VDORIENT_ROT270               =3          # from enum VdOrientation
	VDORIENT_ROT90                =1          # from enum VdOrientation
	VDALIGN_LC                    =6          # from enum VdOrigin
	VDALIGN_LL                    =3          # from enum VdOrigin
	VDALIGN_LR                    =9          # from enum VdOrigin
	VDALIGN_MC                    =5          # from enum VdOrigin
	VDALIGN_ML                    =2          # from enum VdOrigin
	VDALIGN_MR                    =8          # from enum VdOrigin
	VDALIGN_NONE                  =0          # from enum VdOrigin
	VDALIGN_UC                    =4          # from enum VdOrigin
	VDALIGN_UL                    =1          # from enum VdOrigin
	VDALIGN_UR                    =7          # from enum VdOrigin
	VDPADSPRO_SE                  =2          # from enum VdPEFlowMode
	VDPE_BASE                     =1          # from enum VdPEFlowMode
	VDPE_NONE                     =0          # from enum VdPEFlowMode
	VDMD_ABSOLUTE_OATS            =52         # from enum VdParamMode
	VDMD_ARROWHEADS               =40         # from enum VdParamMode
	VDMD_AUTOPAN                  =26         # from enum VdParamMode
	VDMD_AUTO_RIPPER_BUS_SEGMENT  =30         # from enum VdParamMode
	VDMD_AUTO_TEXT_ORIEN          =29         # from enum VdParamMode
	VDMD_BELL                     =5          # from enum VdParamMode
	VDMD_BIGCROSS                 =48         # from enum VdParamMode
	VDMD_BORDER_ON                =1          # from enum VdParamMode
	VDMD_BUS                      =0          # from enum VdParamMode
	VDMD_CABLING                  =61         # from enum VdParamMode
	VDMD_CHECK_COMPDATES          =46         # from enum VdParamMode
	VDMD_CHECK_REUSEBLOCK_DATES   =63         # from enum VdParamMode
	VDMD_COARSE_GRID              =19         # from enum VdParamMode
	VDMD_COMPDEF_ON               =16         # from enum VdParamMode
	VDMD_COMPTEXT_ON              =4          # from enum VdParamMode
	VDMD_CONSTRAINT               =54         # from enum VdParamMode
	VDMD_CONTEXT_WINDOW           =10         # from enum VdParamMode
	VDMD_DBOX_ON                  =17         # from enum VdParamMode
	VDMD_DB_ERR_VERBOSE           =23         # from enum VdParamMode
	VDMD_DEF_USESHEET1            =44         # from enum VdParamMode
	VDMD_DETAIL                   =6          # from enum VdParamMode
	VDMD_DYNAMIC_PANNING          =57         # from enum VdParamMode
	VDMD_DYNAMIC_PLOTSIZE         =36         # from enum VdParamMode
	VDMD_DYNAMIC_XY               =20         # from enum VdParamMode
	VDMD_EURODATE_ON              =51         # from enum VdParamMode
	VDMD_EXCLUDE_GLOBALS_FM_UNIQUE_ON_COPY=55         # from enum VdParamMode
	VDMD_EXPEDITION_ZOOM          =59         # from enum VdParamMode
	VDMD_FUB_PINTYPE_ON           =25         # from enum VdParamMode
	VDMD_FULL_VHDL_CHECKS         =28         # from enum VdParamMode
	VDMD_GRID_ON                  =2          # from enum VdParamMode
	VDMD_HEADER_ON                =3          # from enum VdParamMode
	VDMD_LABELBRACKETS            =50         # from enum VdParamMode
	VDMD_LOAD_OLE_OBJECTS         =62         # from enum VdParamMode
	VDMD_MAPTOBLACK               =27         # from enum VdParamMode
	VDMD_MIDSTROKE                =58         # from enum VdParamMode
	VDMD_NAME                     =12         # from enum VdParamMode
	VDMD_NETS_IN_SPACE            =21         # from enum VdParamMode
	VDMD_NON_UNDOABLE_MOVE        =39         # from enum VdParamMode
	VDMD_OATCHECK                 =49         # from enum VdParamMode
	VDMD_OATS                     =22         # from enum VdParamMode
	VDMD_OLD_UNLIMITED_TEXT       =34         # from enum VdParamMode
	VDMD_OTO_BYPASS               =35         # from enum VdParamMode
	VDMD_PIN_TOOLTIPS             =47         # from enum VdParamMode
	VDMD_PLACEHOLDER              =32         # from enum VdParamMode
	VDMD_PNUMS_ON                 =13         # from enum VdParamMode
	VDMD_PROJECT_PLOT_ON_PC       =53         # from enum VdParamMode
	VDMD_RIPPERS_ON               =901        # from enum VdParamMode
	VDMD_RNUMS_ON                 =15         # from enum VdParamMode
	VDMD_SCHEMATIC_TABS           =60         # from enum VdParamMode
	VDMD_SELNAME_ON               =24         # from enum VdParamMode
	VDMD_SNAP_PIN                 =7          # from enum VdParamMode
	VDMD_SORT_ON                  =14         # from enum VdParamMode
	VDMD_STROKES                  =56         # from enum VdParamMode
	VDMD_THICKNETS_ON             =900        # from enum VdParamMode
	VDMD_UNDO                     =11         # from enum VdParamMode
	VDMD_UNIQUE_LABEL             =8          # from enum VdParamMode
	VDMD_UNLIMITED_TEXT           =31         # from enum VdParamMode
	VDMD_VALUES_ON                =9          # from enum VdParamMode
	VDMD_WIR_CONT_CHAR            =33         # from enum VdParamMode
	VDMD_XTRAERRS_ON              =18         # from enum VdParamMode
	VDVAL_ADISTANCE               =10         # from enum VdParamValue
	VDVAL_ANNO_SIZE               =16         # from enum VdParamValue
	VDVAL_ATTR_ON_SPLIT           =29         # from enum VdParamValue
	VDVAL_AUTOLOG                 =2          # from enum VdParamValue
	VDVAL_AUTO_RIPPER_BUS_SEGMENT_LENGTH=19         # from enum VdParamValue
	VDVAL_BLOCK_TYPE              =15         # from enum VdParamValue
	VDVAL_BOX_SIZE                =12         # from enum VdParamValue
	VDVAL_BUBBLE_SIZE             =8          # from enum VdParamValue
	VDVAL_BUS_DOT_SIZE            =17         # from enum VdParamValue
	VDVAL_DEFMETHOD               =22         # from enum VdParamValue
	VDVAL_DOTSIZE_THREE_SEGMENT   =28         # from enum VdParamValue
	VDVAL_DOT_SIZE                =1          # from enum VdParamValue
	VDVAL_GRID                    =0          # from enum VdParamValue
	VDVAL_GRID_HIGHLIGHT_INTERVAL =26         # from enum VdParamValue
	VDVAL_LABELTHRESHOLD          =24         # from enum VdParamValue
	VDVAL_LABEL_ON_SPLIT          =30         # from enum VdParamValue
	VDVAL_LONG_LINE_ERRORS        =20         # from enum VdParamValue
	VDVAL_MRU_SIZE                =31         # from enum VdParamValue
	VDVAL_NET_LENGTH              =27         # from enum VdParamValue
	VDVAL_NET_SPACING             =25         # from enum VdParamValue
	VDVAL_NEW_ATTR_VIS            =14         # from enum VdParamValue
	VDVAL_NO_UNDO_CBA_MOVE        =21         # from enum VdParamValue
	VDVAL_ORIENTATION             =23         # from enum VdParamValue
	VDVAL_ROUTE_MODE              =9          # from enum VdParamValue
	VDVAL_SCOPE                   =11         # from enum VdParamValue
	VDVAL_SELECTION               =7          # from enum VdParamValue
	VDVAL_SHEET_SIZE              =6          # from enum VdParamValue
	VDVAL_STROKE_DELAY            =32         # from enum VdParamValue
	VDVAL_TEXT_THRESHOLD          =13         # from enum VdParamValue
	VDVAL_TORIGIN                 =4          # from enum VdParamValue
	VDVAL_TSIZE                   =3          # from enum VdParamValue
	VDVAL_UNDO                    =18         # from enum VdParamValue
	VDVAL_WIDTH                   =5          # from enum VdParamValue
	VDPIN_BOUNDARY                =1          # from enum VdPinEndType
	VDPIN_INTERIOR                =0          # from enum VdPinEndType
	VDSETTING_ATTR                =16         # from enum VdProjectSettingTab
	VDSETTING_BLOCK               =2          # from enum VdProjectSettingTab
	VDSETTING_COLOR               =128        # from enum VdProjectSettingTab
	VDSETTING_COMP                =4          # from enum VdProjectSettingTab
	VDSETTING_FONT                =512        # from enum VdProjectSettingTab
	VDSETTING_LABEL               =32         # from enum VdProjectSettingTab
	VDSETTING_NET                 =8          # from enum VdProjectSettingTab
	VDSETTING_PALETTE             =256        # from enum VdProjectSettingTab
	VDSETTING_PROJ                =1          # from enum VdProjectSettingTab
	VDSETTING_STARTUP             =1024       # from enum VdProjectSettingTab
	VDSETTING_TEXT                =64         # from enum VdProjectSettingTab
	ATTR_PROMO                    =1          # from enum VdPromoteType
	ATTR_RESET                    =2          # from enum VdPromoteType
	BINDING_FILE                  =7          # from enum VdPromoteType
	FILTER_LIST                   =6          # from enum VdPromoteType
	GLOBAL_NETNAMES               =3          # from enum VdPromoteType
	MIXED_LIST                    =5          # from enum VdPromoteType
	UPPER_LIST                    =4          # from enum VdPromoteType
	VGMODEAND                     =7          # from enum VdRasterop
	VGMODENAND                    =3          # from enum VdRasterop
	VGMODENOR                     =5          # from enum VdRasterop
	VGMODENREP                    =4          # from enum VdRasterop
	VGMODENXOR                    =6          # from enum VdRasterop
	VGMODEOR                      =1          # from enum VdRasterop
	VGMODEREPLACE                 =0          # from enum VdRasterop
	VGMODEXOR                     =2          # from enum VdRasterop
	VDGLOBAL_SCOPE                =1          # from enum VdScope
	VDLOCAL_SCOPE                 =0          # from enum VdScope
	VDSEG_PTHIGH                  =1          # from enum VdSegmentEndType
	VDSEG_PTLOW                   =0          # from enum VdSegmentEndType
	VDSELECT_NOTIFY               =0          # from enum VdSelectionType
	VDSELECT_NOTIFY_ADD           =1          # from enum VdSelectionType
	VDSELECT_NOTIFY_REMOVE        =2          # from enum VdSelectionType
	VDINVERTED                    =1          # from enum VdSense
	VDNOTINVERTED                 =0          # from enum VdSense
	VDSHEET_A0L_SIZE              =20         # from enum VdSheetSize
	VDSHEET_A0P_SIZE              =30         # from enum VdSheetSize
	VDSHEET_A0_SIZE               =9          # from enum VdSheetSize
	VDSHEET_A1L_SIZE              =19         # from enum VdSheetSize
	VDSHEET_A1P_SIZE              =29         # from enum VdSheetSize
	VDSHEET_A1_SIZE               =8          # from enum VdSheetSize
	VDSHEET_A2L_SIZE              =18         # from enum VdSheetSize
	VDSHEET_A2P_SIZE              =28         # from enum VdSheetSize
	VDSHEET_A2_SIZE               =7          # from enum VdSheetSize
	VDSHEET_A3L_SIZE              =17         # from enum VdSheetSize
	VDSHEET_A3P_SIZE              =27         # from enum VdSheetSize
	VDSHEET_A3_SIZE               =6          # from enum VdSheetSize
	VDSHEET_A4L_SIZE              =16         # from enum VdSheetSize
	VDSHEET_A4P_SIZE              =26         # from enum VdSheetSize
	VDSHEET_A4_SIZE               =5          # from enum VdSheetSize
	VDSHEET_AL_SIZE               =11         # from enum VdSheetSize
	VDSHEET_AP_SIZE               =21         # from enum VdSheetSize
	VDSHEET_ASIZE                 =0          # from enum VdSheetSize
	VDSHEET_BL_SIZE               =12         # from enum VdSheetSize
	VDSHEET_BP_SIZE               =22         # from enum VdSheetSize
	VDSHEET_BSIZE                 =1          # from enum VdSheetSize
	VDSHEET_CL_SIZE               =13         # from enum VdSheetSize
	VDSHEET_CP_SIZE               =23         # from enum VdSheetSize
	VDSHEET_CSIZE                 =2          # from enum VdSheetSize
	VDSHEET_DL_SIZE               =14         # from enum VdSheetSize
	VDSHEET_DP_SIZE               =24         # from enum VdSheetSize
	VDSHEET_DSIZE                 =3          # from enum VdSheetSize
	VDSHEET_EL_SIZE               =15         # from enum VdSheetSize
	VDSHEET_EP_SIZE               =25         # from enum VdSheetSize
	VDSHEET_ESIZE                 =4          # from enum VdSheetSize
	VDSHEET_ZSIZE                 =10         # from enum VdSheetSize
	VDBOTTOM                      =1          # from enum VdSide
	VDLEFT                        =2          # from enum VdSide
	VDRIGHT                       =3          # from enum VdSide
	VDTOP                         =0          # from enum VdSide
	VDSM_ALL                      =1          # from enum VdSilentMode
	VDSM_NONE                     =0          # from enum VdSilentMode
	VDSOURCE_SPICE                =3          # from enum VdSourceDocumentType
	VDSOURCE_TEXT                 =0          # from enum VdSourceDocumentType
	VDSOURCE_VERILOG              =2          # from enum VdSourceDocumentType
	VDSOURCE_VHDL                 =1          # from enum VdSourceDocumentType
	VGSPLINEROUND                 =5          # from enum VdSplineOrder
	VGSPLINESHARP                 =3          # from enum VdSplineOrder
	VGSPLINESMOOTH                =4          # from enum VdSplineOrder
	VGSPLINECLOSED                =1          # from enum VdSplineType
	VGSPLINEOPEN                  =0          # from enum VdSplineType
	VDB_ANNOTATE                  =3          # from enum VdSymbolType
	VDB_COMPOSITE                 =0          # from enum VdSymbolType
	VDB_MODULE                    =1          # from enum VdSymbolType
	VDB_PIN                       =4          # from enum VdSymbolType
	vgTextMIRROR_FLAG             =32         # from enum VdTextFlags
	vgTextNORMAL                  =0          # from enum VdTextFlags
	vgTextOVERSCORE_FLAG          =16         # from enum VdTextFlags
	vgTextUNDERSCORE_FLAG         =64         # from enum VdTextFlags
	VDUNIT_CM                     =1          # from enum VdUnit
	VDUNIT_INCH                   =2          # from enum VdUnit
	VDUNIT_MM                     =0          # from enum VdUnit
	VDUOO_BOARD                   =1          # from enum VdUpdateOOScope
	VDUOO_PROJECT                 =0          # from enum VdUpdateOOScope
	VDUOO_SCHEMATIC               =2          # from enum VdUpdateOOScope
	VDUOO_SHEET                   =3          # from enum VdUpdateOOScope
	VDUOO_BORDERS                 =32         # from enum VdUpdateOtherObjects
	VDUOO_BUSRIPPERS              =4          # from enum VdUpdateOtherObjects
	VDUOO_BUSSIGNALS              =2          # from enum VdUpdateOtherObjects
	VDUOO_CROSS_REFERENCE         =8          # from enum VdUpdateOtherObjects
	VDUOO_PRINT_ORDER             =16         # from enum VdUpdateOtherObjects
	VDUOO_PROPERTIES              =1          # from enum VdUpdateOtherObjects
	VDINVISIBLE                   =0          # from enum VdVisibilityFlag
	VDNAMEVISIBLE                 =2          # from enum VdVisibilityFlag
	VDSAMEVISIBLE                 =4          # from enum VdVisibilityFlag
	VDVALUEVISIBLE                =3          # from enum VdVisibilityFlag
	VDVISIBLE                     =1          # from enum VdVisibilityFlag
	VDJ_HIGH                      =1          # from enum VdWhichJoint
	VDJ_LOW                       =0          # from enum VdWhichJoint

from win32com.client import DispatchBaseClass
class IAddinInfo(DispatchBaseClass):
	CLSID = IID('{9D83C992-3682-4D94-9727-EFBB5C0FB74C}')
	coclass_clsid = IID('{8B362D9C-6CF5-1014-9D62-FFC3EECCF0AC}')

	_prop_map_get_ = {
		"InitiallyDisabled": (11, 2, (11, 0), (), "InitiallyDisabled", None),
		"InitiallyVisible": (12, 2, (11, 0), (), "InitiallyVisible", None),
		"LicenseFeature": (10, 2, (8, 0), (), "LicenseFeature", None),
		"Name": (1, 2, (8, 0), (), "Name", None),
		"Placement": (5, 2, (8, 0), (), "Placement", None),
		"ProgId": (2, 2, (8, 0), (), "ProgId", None),
		"RuntimeCreateDecision": (9, 2, (11, 0), (), "RuntimeCreateDecision", None),
		"Script": (3, 2, (8, 0), (), "Script", None),
		"ShortCutKey": (7, 2, (8, 0), (), "ShortCutKey", None),
		"ToolbarButton": (8, 2, (11, 0), (), "ToolbarButton", None),
	}
	_prop_map_put_ = {
		"InitiallyDisabled": ((11, LCID, 4, 0),()),
		"InitiallyVisible": ((12, LCID, 4, 0),()),
		"LicenseFeature": ((10, LCID, 4, 0),()),
		"Name": ((1, LCID, 4, 0),()),
		"Placement": ((5, LCID, 4, 0),()),
		"ProgId": ((2, LCID, 4, 0),()),
		"RuntimeCreateDecision": ((9, LCID, 4, 0),()),
		"Script": ((3, LCID, 4, 0),()),
		"ShortCutKey": ((7, LCID, 4, 0),()),
		"ToolbarButton": ((8, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IAutoString(DispatchBaseClass):
	CLSID = IID('{7BB17D66-FAE6-11D1-BE10-00A0C9204FDC}')
	coclass_clsid = IID('{8B36C22C-6CF5-1014-9D62-FFC3EECCF0AC}')

	_prop_map_get_ = {
		"Text": (1, 2, (8, 0), (), "Text", None),
		"_Text": (0, 2, (8, 0), (), "_Text", None),
	}
	_prop_map_put_ = {
		"Text": ((1, LCID, 4, 0),()),
	}
	# Default property for this class is '_Text'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "_Text", None))
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

class IColor(DispatchBaseClass):
	CLSID = IID('{C1031A0C-15BD-4897-A3E5-4C615CDEA684}')
	coclass_clsid = IID('{8B362A2D-6CF5-1014-9D62-FFC3EECCF0AC}')

	_prop_map_get_ = {
		"b": (3, 2, (3, 0), (), "b", None),
		"g": (2, 2, (3, 0), (), "g", None),
		"r": (1, 2, (3, 0), (), "r", None),
	}
	_prop_map_put_ = {
		"b": ((3, LCID, 4, 0),()),
		"g": ((2, LCID, 4, 0),()),
		"r": ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ICommandsManager(DispatchBaseClass):
	CLSID = IID('{AA7F70A6-2F0E-417C-A1D2-C1621D728EB0}')
	coclass_clsid = IID('{8B364617-6CF5-1014-9D62-FFC3EECCF0AC}')

	def CommandDisable(self, CommandName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(324, LCID, 1, (11, 0), ((8, 1),),CommandName
			)

	def CommandEnable(self, CommandName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(323, LCID, 1, (11, 0), ((8, 1),),CommandName
			)

	def CommandRemove(self, CommandName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(325, LCID, 1, (11, 0), ((8, 1),),CommandName
			)

	def ExecuteCommand(self, CommandString=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(327, LCID, 1, (11, 0), ((8, 1),),CommandString
			)

	def ExecuteCommandByID(self, command_Id=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(328, LCID, 1, (24, 0), ((3, 1),),command_Id
			)

	def ExecuteMenuCommand(self, command_name=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(326, LCID, 1, (24, 0), ((8, 1),),command_name
			)

	def RegisterOLECommand(self, CommandName=defaultNamedNotOptArg, CommandDescription=defaultNamedNotOptArg, bModifiesData=defaultNamedNotOptArg, pDispatch=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(321, LCID, 1, (11, 0), ((8, 1), (8, 1), (11, 1), (9, 1)),CommandName
			, CommandDescription, bModifiesData, pDispatch)

	def UnregisterOLECommand(self, CommandName=defaultNamedNotOptArg, ClientDispatch=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(322, LCID, 1, (11, 0), ((8, 1), (9, 1)),CommandName
			, ClientDispatch)

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

class ICommonPropertyDefinition(DispatchBaseClass):
	CLSID = IID('{2A69C05E-34EA-46FE-B44C-FE3A217D3C86}')
	coclass_clsid = IID('{8B363F3D-6CF5-1014-9D62-FFC3EECCF0AC}')

	def AreMultipleEntriesOK(self):
		return self._oleobj_.InvokeTypes(4, LCID, 1, (11, 0), (),)

	def CanBeOverriden(self):
		return self._oleobj_.InvokeTypes(5, LCID, 1, (11, 0), (),)

	def CheckPropertyValue(self, Value=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(13, LCID, 1, (11, 0), ((8, 1),),Value
			)

	def GetFontColor(self):
		return self._oleobj_.InvokeTypes(15, LCID, 1, (2, 0), (),)

	def GetFontHeight(self):
		return self._oleobj_.InvokeTypes(16, LCID, 1, (3, 0), (),)

	def GetFontName(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(17, LCID, 1, (8, 0), (),)

	def GetId(self):
		return self._oleobj_.InvokeTypes(1, LCID, 1, (3, 0), (),)

	def GetMaxNumberOfChars(self):
		return self._oleobj_.InvokeTypes(9, LCID, 1, (3, 0), (),)

	def GetMaxNumberOfLines(self):
		return self._oleobj_.InvokeTypes(10, LCID, 1, (3, 0), (),)

	def GetName(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(2, LCID, 1, (8, 0), (),)

	def GetOrignalRegularExp(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(7, LCID, 1, (8, 0), (),)

	def GetOwnerTypes(self):
		return self._oleobj_.InvokeTypes(3, LCID, 1, (2, 0), (),)

	def GetRegularExp(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(8, LCID, 1, (8, 0), (),)

	def GetStorageType(self):
		return self._oleobj_.InvokeTypes(11, LCID, 1, (2, 0), (),)

	def IsNotationInvalid(self):
		return self._oleobj_.InvokeTypes(12, LCID, 1, (11, 0), (),)

	def IsTransferredFromPDB(self):
		return self._oleobj_.InvokeTypes(6, LCID, 1, (11, 0), (),)

	def IsVisible(self):
		return self._oleobj_.InvokeTypes(14, LCID, 1, (11, 0), (),)

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

class ICommonPropertyManager(DispatchBaseClass):
	CLSID = IID('{E8758B51-DEBB-46FD-A192-962B14F57FA4}')
	coclass_clsid = IID('{8B36429D-6CF5-1014-9D62-FFC3EECCF0AC}')

	def CheckPropertyValue(self, Name=defaultNamedNotOptArg, Value=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((8, 1), (8, 1)),Name
			, Value)

	# Result is of type IStringList
	def GetCompPropertyNames(self):
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetCompPropertyNames', '{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')
		return ret

	def GetLoadedFile(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1, LCID, 1, (8, 0), (),)

	# Result is of type IStringList
	def GetLoosePropertyNames(self):
		ret = self._oleobj_.InvokeTypes(7, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetLoosePropertyNames', '{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')
		return ret

	# Result is of type IStringList
	def GetNetPropertyNames(self):
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetNetPropertyNames', '{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')
		return ret

	# Result is of type IStringList
	def GetPinPropertyNames(self):
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetPinPropertyNames', '{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')
		return ret

	# Result is of type ICommonPropertyDefinition
	def GetPropertyDefinition(self, Name=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(8, LCID, 1, (9, 0), ((8, 1),),Name
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetPropertyDefinition', '{2A69C05E-34EA-46FE-B44C-FE3A217D3C86}')
		return ret

	# Result is of type IStringList
	def GetPropertyNames(self):
		ret = self._oleobj_.InvokeTypes(2, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetPropertyNames', '{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')
		return ret

	# Result is of type IStringList
	def GetTransPropertyNames(self):
		ret = self._oleobj_.InvokeTypes(6, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetTransPropertyNames', '{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')
		return ret

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

class IDesignSearcherAutomation(DispatchBaseClass):
	CLSID = IID('{3EBAD6B7-B757-4A57-9657-DD43BF86A526}')
	coclass_clsid = None

	def Dump(self, Directory=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1, LCID, 1, (11, 0), ((8, 1),),Directory
			)

	def DumpAll(self, Directory=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(2, LCID, 1, (11, 0), ((8, 1),),Directory
			)

	def DumpNoBusRippers(self, Directory=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), ((8, 1),),Directory
			)

	def Query(self, Query=defaultNamedNotOptArg, ResultsFile=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(4, LCID, 1, (11, 0), ((8, 1), (8, 1)),Query
			, ResultsFile)

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

class IFramework(DispatchBaseClass):
	CLSID = IID('{77CD6602-703B-4AFA-A4C1-B1652A257F15}')
	coclass_clsid = IID('{8B363BA5-6CF5-1014-9D62-FFC3EECCF0AC}')

	def RunTcl(self, tclCommand=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1, LCID, 1, (11, 0), ((8, 1),),tclCommand
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

class IHDLSourceDocument(DispatchBaseClass):
	CLSID = IID('{8C395488-EC22-4C81-8F13-7061A7594657}')
	coclass_clsid = IID('{8B36C3DE-6CF5-1014-9D62-FFC3EECCF0AC}')

	def BookmarkLine(self, Index=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(2, LCID, 1, (24, 0), ((3, 0),),Index
			)

	def GotoLine(self, Index=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1, LCID, 1, (24, 0), ((3, 0),),Index
			)

	_prop_map_get_ = {
		"Name": (3, 2, (8, 0), (), "Name", None),
		"Path": (4, 2, (8, 0), (), "Path", None),
	}
	_prop_map_put_ = {
		"Name" : ((3, LCID, 4, 0),()),
		"Path" : ((4, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IHDLSourceDocuments(DispatchBaseClass):
	CLSID = IID('{AC6510A1-83C5-4486-9154-CE74592F9A48}')
	coclass_clsid = IID('{8B36C5D2-6CF5-1014-9D62-FFC3EECCF0AC}')

	# Result is of type IHDLSourceDocument
	def Item(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((12, 0),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{8C395488-EC22-4C81-8F13-7061A7594657}')
		return ret

	# Result is of type IHDLSourceDocument
	def New(self, DocType=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), ((3, 0),),DocType
			)
		if ret is not None:
			ret = Dispatch(ret, 'New', '{8C395488-EC22-4C81-8F13-7061A7594657}')
		return ret

	# Result is of type IHDLSourceDocument
	def Open(self, DocumentPath=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), ((8, 0),),DocumentPath
			)
		if ret is not None:
			ret = Dispatch(ret, 'Open', '{8C395488-EC22-4C81-8F13-7061A7594657}')
		return ret

	def Remove(self, Index=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(2, LCID, 1, (24, 0), ((3, 0),),Index
			)

	def RemoveAll(self):
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), (),)

	def SaveAll(self):
		return self._oleobj_.InvokeTypes(6, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
		"Count" : ((1, LCID, 4, 0),()),
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((12, 0),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{8C395488-EC22-4C81-8F13-7061A7594657}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,1,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{8C395488-EC22-4C81-8F13-7061A7594657}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IHTMLSourceDocument(DispatchBaseClass):
	CLSID = IID('{AA54312B-698C-473D-ABDE-F4A4C9DCD0DD}')
	coclass_clsid = IID('{8B36C967-6CF5-1014-9D62-FFC3EECCF0AC}')

	_prop_map_get_ = {
		"Document": (3, 2, (9, 0), (), "Document", None),
		"Name": (1, 2, (8, 0), (), "Name", None),
		"URL": (2, 2, (8, 0), (), "URL", None),
	}
	_prop_map_put_ = {
		"Document" : ((3, LCID, 4, 0),()),
		"Name" : ((1, LCID, 4, 0),()),
		"URL" : ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IHTMLSourceDocuments(DispatchBaseClass):
	CLSID = IID('{7D50CA6D-07DB-4BE0-AD95-563DED3F9157}')
	coclass_clsid = IID('{8B36CB16-6CF5-1014-9D62-FFC3EECCF0AC}')

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
		"Count" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IICTDocuments(DispatchBaseClass):
	CLSID = IID('{2A3CCA57-9C38-4484-A6A3-7521DDF7DAD0}')
	coclass_clsid = IID('{8B3669A8-6CF5-1014-9D62-FFC3EECCF0AC}')

	def Close(self, ICTName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(2, LCID, 1, (24, 0), ((8, 1),),ICTName
			)

	# Result is of type IStringList
	def GetAvailableICTs(self):
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetAvailableICTs', '{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')
		return ret

	def GetOpenedCount(self):
		return self._oleobj_.InvokeTypes(5, LCID, 1, (3, 0), (),)

	# Result is of type IStringList
	def GetOpenedICTs(self):
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetOpenedICTs', '{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')
		return ret

	# Result is of type IVdICTDocument
	def GetOpenedItem(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(6, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetOpenedItem', '{E947B7EF-5E39-42FD-A351-400BFEFCF49D}')
		return ret

	# Result is of type IVdICTDocument
	def Open(self, ICTName=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(1, LCID, 1, (9, 0), ((8, 1),),ICTName
			)
		if ret is not None:
			ret = Dispatch(ret, 'Open', '{E947B7EF-5E39-42FD-A351-400BFEFCF49D}')
		return ret

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

class IMGCDesignerDataManagement(DispatchBaseClass):
	'MGCDesigner Data Managment Object.'
	CLSID = IID('{96EB093C-B1E3-444B-B39D-08D05CB0DF06}')
	coclass_clsid = IID('{8B3726C8-6CF5-1014-9D62-FFC3EECCF0AC}')

	# Result is of type IMGCDesignerDataManagementAdditionalProperties
	def AdditionalProperties(self, Type=defaultNamedNotOptArg):
		'Find additional properties available for entities of given types.'
		ret = self._oleobj_.InvokeTypes(6, LCID, 1, (9, 0), ((3, 1),),Type
			)
		if ret is not None:
			ret = Dispatch(ret, 'AdditionalProperties', '{4E66A337-C45F-4BEA-9089-3E64D3270531}')
		return ret

	def Connect(self, server_address=defaultNamedNotOptArg, server_port=defaultNamedNotOptArg):
		'Connect to a Data Management server.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (24, 0), ((8, 1), (8, 1)),server_address
			, server_port)

	# Result is of type IMGCDesignerDataManagementEntity
	def FindEntityByPath(self, Path=defaultNamedNotOptArg):
		'Find entity by path.'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), ((8, 1),),Path
			)
		if ret is not None:
			ret = Dispatch(ret, 'FindEntityByPath', '{03BE5928-2002-4CCB-818D-775ED6115A41}')
		return ret

	# Result is of type IMGCDesignerDataManagementEntity
	def FindEntityByPathAndVersion(self, Path=defaultNamedNotOptArg, Version=defaultNamedNotOptArg):
		'Find entity by path and version.'
		ret = self._oleobj_.InvokeTypes(7, LCID, 1, (9, 0), ((8, 1), (8, 1)),Path
			, Version)
		if ret is not None:
			ret = Dispatch(ret, 'FindEntityByPathAndVersion', '{03BE5928-2002-4CCB-818D-775ED6115A41}')
		return ret

	def IsConnected(self):
		'Check Data Management connection status.'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (11, 0), (),)

	def LastErrorMessage(self):
		'Get last error message.'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(10, LCID, 1, (8, 0), (),)

	def OpenComponentView(self, partNumber=defaultNamedNotOptArg):
		'Open component view.'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (24, 0), ((8, 1),),partNumber
			)

	def OpenManagedBlockView(self, Name=defaultNamedNotOptArg, Version=defaultNamedNotOptArg):
		'Open managed block view.'
		return self._oleobj_.InvokeTypes(13, LCID, 1, (24, 0), ((8, 1), (8, 1)),Name
			, Version)

	# The method Option is actually a property, but must be used as a method to correctly pass the arguments
	def Option(self, Name=defaultNamedNotOptArg):
		'Get data management related option value.'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(8, LCID, 2, (8, 0), ((8, 1),),Name
			)

	# The method OptionIsReadonly is actually a property, but must be used as a method to correctly pass the arguments
	def OptionIsReadonly(self, Name=defaultNamedNotOptArg):
		'Check if a given data management related option is readonly.'
		return self._oleobj_.InvokeTypes(9, LCID, 2, (11, 0), ((8, 1),),Name
			)

	# Result is of type IMGCDesignerDataManagementEntities
	def RecentEntities(self):
		'Get recently used entities.'
		ret = self._oleobj_.InvokeTypes(2, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'RecentEntities', '{3C8285AF-A900-4537-B9BA-C44223D0B380}')
		return ret

	# The method SetOption is actually a property, but must be used as a method to correctly pass the arguments
	def SetOption(self, Name=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		'Get data management related option value.'
		return self._oleobj_.InvokeTypes(8, LCID, 4, (24, 0), ((8, 1), (8, 0)),Name
			, arg1)

	def ValidEntityTypes(self):
		'Get vaild entity types.'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (3, 0), (),)

	# Result is of type IMGCDesignerDataManagementEntities
	def entities(self, Type=defaultNamedNotOptArg):
		'Find all entities.'
		ret = self._oleobj_.InvokeTypes(1, LCID, 1, (9, 0), ((3, 1),),Type
			)
		if ret is not None:
			ret = Dispatch(ret, 'entities', '{3C8285AF-A900-4537-B9BA-C44223D0B380}')
		return ret

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

class IMGCDesignerDataManagementAdditionalProperties(DispatchBaseClass):
	'MGCDesigner Data Management Additional Properties Collection Object.'
	CLSID = IID('{4E66A337-C45F-4BEA-9089-3E64D3270531}')
	coclass_clsid = IID('{8B372E3C-6CF5-1014-9D62-FFC3EECCF0AC}')

	def Count(self):
		'Returns number of objects in this collection.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (3, 0), (),)

	# Result is of type IMGCDesignerDataManagementAdditionalProperty
	def Item(self, vIndex=defaultNamedNotOptArg):
		'Returns the additional property of a given index in the entities collection.'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), ((12, 1),),vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{787D1D50-FC6C-478A-84CB-2FD200799E22}')
		return ret

	def Remove(self, vIndex=defaultNamedNotOptArg):
		'Removes an object from this collection.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (24, 0), ((12, 1),),vIndex
			)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{787D1D50-FC6C-478A-84CB-2FD200799E22}')
	#This class has Item property/method which allows indexed access with the object[key] syntax.
	#Some objects will accept a string or other type of key in addition to integers.
	#Note that many Office objects do not use zero-based indexing.
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(3, LCID, 1, 1, key)), "Item", '{787D1D50-FC6C-478A-84CB-2FD200799E22}')
	#This class has Count() method - allow len(ob) to provide this
	def __len__(self):
		'Returns number of objects in this collection.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (3, 0), (),)

	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IMGCDesignerDataManagementAdditionalProperty(DispatchBaseClass):
	'MGCDesigner Data Management Additional Property Object.'
	CLSID = IID('{787D1D50-FC6C-478A-84CB-2FD200799E22}')
	coclass_clsid = IID('{8B372C67-6CF5-1014-9D62-FFC3EECCF0AC}')

	def Id(self):
		"Returns Additional Property's Id."
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1, LCID, 1, (8, 0), (),)

	def Label(self):
		"Returns Additional Property's Label."
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(2, LCID, 1, (8, 0), (),)

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

class IMGCDesignerDataManagementEntities(DispatchBaseClass):
	'MGCDesigner Data Management Entities Collection.'
	CLSID = IID('{3C8285AF-A900-4537-B9BA-C44223D0B380}')
	coclass_clsid = IID('{8B372A86-6CF5-1014-9D62-FFC3EECCF0AC}')

	def Count(self):
		'Returns number of objects in this collection.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (3, 0), (),)

	# Result is of type IMGCDesignerDataManagementEntity
	def Item(self, vIndex=defaultNamedNotOptArg):
		'Returns the entity of a given index in the entities collection.'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), ((12, 1),),vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{03BE5928-2002-4CCB-818D-775ED6115A41}')
		return ret

	def Remove(self, vIndex=defaultNamedNotOptArg):
		'Removes an object from this collection.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (24, 0), ((12, 1),),vIndex
			)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{03BE5928-2002-4CCB-818D-775ED6115A41}')
	#This class has Item property/method which allows indexed access with the object[key] syntax.
	#Some objects will accept a string or other type of key in addition to integers.
	#Note that many Office objects do not use zero-based indexing.
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(3, LCID, 1, 1, key)), "Item", '{03BE5928-2002-4CCB-818D-775ED6115A41}')
	#This class has Count() method - allow len(ob) to provide this
	def __len__(self):
		'Returns number of objects in this collection.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (3, 0), (),)

	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IMGCDesignerDataManagementEntity(DispatchBaseClass):
	'MGCDesigner Data Management Entity Object.'
	CLSID = IID('{03BE5928-2002-4CCB-818D-775ED6115A41}')
	coclass_clsid = IID('{8B372899-6CF5-1014-9D62-FFC3EECCF0AC}')

	def AccessType(self):
		"Returns Entity's Access Type."
		return self._oleobj_.InvokeTypes(4, LCID, 1, (3, 0), (),)

	def AdditionalPropertyValue(self, property=defaultNamedNotOptArg):
		'Returns the value of an additional property available on the entity'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(16, LCID, 1, (8, 0), ((9, 1),),property
			)

	def CancelEditing(self):
		'Cancels Editing of Entity.'
		return self._oleobj_.InvokeTypes(23, LCID, 1, (24, 0), (),)

	def CheckIn(self, comment=defaultNamedNotOptArg):
		'Checks in a checked out entity. The entity cannot be actively edited'
		return self._oleobj_.InvokeTypes(14, LCID, 1, (24, 0), ((8, 1),),comment
			)

	def CheckedInDate(self):
		"Returns Entity's checked in date."
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(8, LCID, 1, (8, 0), (),)

	def DumpProperties(self, outputDirectory=defaultNamedNotOptArg, filter=0, includeParents=False):
		'Dumps entity properties to output json file.'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(18, LCID, 1, (8, 0), ((8, 1), (3, 49), (11, 49)),outputDirectory
			, filter, includeParents)

	def EditExclusive(self):
		'Opens Entity for Edit Exclusive.'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (11, 0), (),)

	def EditShared(self):
		'Opens Entity for Edit Shared.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), (),)

	def Export(self, destination=defaultNamedNotOptArg):
		'Exports Entity to passed destination.'
		return self._oleobj_.InvokeTypes(13, LCID, 1, (24, 0), ((8, 1),),destination
			)

	def LaunchWebView(self):
		'Launches a web view for the entity'
		return self._oleobj_.InvokeTypes(15, LCID, 1, (24, 0), (),)

	def LocalPath(self):
		"Returns Entity's local path."
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(22, LCID, 1, (8, 0), (),)

	def Name(self):
		"Returns Entity's name."
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(2, LCID, 1, (8, 0), (),)

	def OpenReference(self):
		'Opens Reference of Entity.'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (24, 0), (),)

	def Path(self):
		"Returns Entity's path."
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1, LCID, 1, (8, 0), (),)

	def ProjectName(self):
		"Returns Entity's Project Name."
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(17, LCID, 1, (8, 0), (),)

	def PropertyValueById(self, Id=defaultNamedNotOptArg):
		'Returns the value of a property available on the entity'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(25, LCID, 1, (8, 0), ((8, 1),),Id
			)

	# Result is of type IMGCDesignerDataManagementEntities
	def RelatedEntities(self, types=defaultNamedNotOptArg):
		'Finds all related entities.'
		ret = self._oleobj_.InvokeTypes(21, LCID, 1, (9, 0), ((3, 1),),types
			)
		if ret is not None:
			ret = Dispatch(ret, 'RelatedEntities', '{3C8285AF-A900-4537-B9BA-C44223D0B380}')
		return ret

	def RunConfigurationRules(self, detailsFilePath=defaultNamedNotOptArg):
		'Runs entity configuration rules.'
		return self._oleobj_.InvokeTypes(19, LCID, 1, (24, 0), ((8, 1),),detailsFilePath
			)

	def Status(self):
		"Returns Entity's status."
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(5, LCID, 1, (8, 0), (),)

	def Type(self):
		"Returns Entity's Type."
		return self._oleobj_.InvokeTypes(3, LCID, 1, (3, 0), (),)

	def Unlock(self):
		'Unlocks Entity.'
		return self._oleobj_.InvokeTypes(24, LCID, 1, (24, 0), (),)

	def Users(self):
		"Returns Entity's users."
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(6, LCID, 1, (8, 0), (),)

	def Version(self):
		"Returns Entity's version."
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(7, LCID, 1, (8, 0), (),)

	def View(self):
		'Opens Entity for View.'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (11, 0), (),)

	def ViewForOutputsGeneration(self):
		'Opens entity for view and outputs generation.'
		return self._oleobj_.InvokeTypes(20, LCID, 1, (11, 0), (),)

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

class IMergeData(DispatchBaseClass):
	CLSID = IID('{4584E756-C172-4389-AD41-AEE82CB45759}')
	coclass_clsid = IID('{8B362BED-6CF5-1014-9D62-FFC3EECCF0AC}')

	# Result is of type IStringList
	def GetAvailableTargetGlobals(self):
		ret = self._oleobj_.InvokeTypes(11, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetAvailableTargetGlobals', '{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')
		return ret

	# Result is of type IStringList
	def GetAvailableTargetLayers(self):
		ret = self._oleobj_.InvokeTypes(7, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetAvailableTargetLayers', '{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')
		return ret

	def GetBusContents(self, sBusName=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(5, LCID, 1, (8, 0), ((8, 1),),sBusName
			)

	# Result is of type IStringList
	def GetBusNames(self):
		ret = self._oleobj_.InvokeTypes(1, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetBusNames', '{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')
		return ret

	def GetSourceBusContents(self, sBusName=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(2, LCID, 1, (8, 0), ((8, 1),),sBusName
			)

	# Result is of type IStringList
	def GetSourceGlobals(self):
		ret = self._oleobj_.InvokeTypes(10, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetSourceGlobals', '{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')
		return ret

	# Result is of type IStringList
	def GetSourceLayers(self):
		ret = self._oleobj_.InvokeTypes(6, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetSourceLayers', '{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')
		return ret

	def GetTargetBusContents(self, sBusName=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(3, LCID, 1, (8, 0), ((8, 1),),sBusName
			)

	def GetTargetGlobal(self, sSourceGlobal=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(12, LCID, 1, (8, 0), ((8, 1),),sSourceGlobal
			)

	def GetTargetLayer(self, sSourceLayer=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(8, LCID, 1, (8, 0), ((8, 1),),sSourceLayer
			)

	def SetBusContents(self, sBusName=defaultNamedNotOptArg, sBusContents=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(4, LCID, 1, (24, 0), ((8, 1), (8, 1)),sBusName
			, sBusContents)

	def SetTargetGlobal(self, sSourceGlobal=defaultNamedNotOptArg, sTargetGlobal=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(13, LCID, 1, (24, 0), ((8, 1), (8, 1)),sSourceGlobal
			, sTargetGlobal)

	def SetTargetLayer(self, sSourceLayer=defaultNamedNotOptArg, sTargetLayer=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(9, LCID, 1, (24, 0), ((8, 1), (8, 1)),sSourceLayer
			, sTargetLayer)

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

class IODProjectData(DispatchBaseClass):
	CLSID = IID('{3D2B940D-C2B5-440E-AB57-E8C6F3FB34C9}')
	coclass_clsid = IID('{8B3637D0-6CF5-1014-9D62-FFC3EECCF0AC}')

	# Result is of type IStringList
	def GetIODesignerFPGAs(self, siCDBDesign=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(301, LCID, 1, (9, 0), ((8, 1),),siCDBDesign
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetIODesignerFPGAs', '{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')
		return ret

	def SetIODesignerFPGAs(self, listOfFPGAs=defaultNamedNotOptArg, siCDBDesign=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(302, LCID, 1, (24, 0), ((9, 1), (8, 1)),listOfFPGAs
			, siCDBDesign)

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

class IPDBPartitions(DispatchBaseClass):
	CLSID = IID('{D17E5439-1B5A-40D5-A115-1E4656FB102B}')
	coclass_clsid = IID('{8B363464-6CF5-1014-9D62-FFC3EECCF0AC}')

	def AppendPDBPartition(self, sPartition=defaultNamedNotOptArg, siCDBDesign=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(204, LCID, 1, (24, 0), ((8, 1), (8, 1)),sPartition
			, siCDBDesign)

	def GetPDBPartition(self, Index=defaultNamedNotOptArg, siCDBDesign=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(200, LCID, 1, (8, 0), ((3, 1), (8, 1)),Index
			, siCDBDesign)

	# Result is of type IStringList
	def GetPDBPartitionsArray(self, siCDBDesign=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(202, LCID, 1, (9, 0), ((8, 1),),siCDBDesign
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetPDBPartitionsArray', '{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')
		return ret

	def GetPDBPartitionsCount(self, siCDBDesign=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(201, LCID, 1, (3, 0), ((8, 1),),siCDBDesign
			)

	def InsertPDBPartition(self, sPartition=defaultNamedNotOptArg, Index=defaultNamedNotOptArg, siCDBDesign=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(203, LCID, 1, (24, 0), ((8, 1), (3, 1), (8, 1)),sPartition
			, Index, siCDBDesign)

	def PDBPartitionExists(self, sPartition=defaultNamedNotOptArg, siCDBDesign=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(207, LCID, 1, (11, 0), ((8, 1), (8, 1)),sPartition
			, siCDBDesign)

	def RemovePDBPartitionByIndex(self, Index=defaultNamedNotOptArg, siCDBDesign=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(206, LCID, 1, (24, 0), ((3, 1), (8, 1)),Index
			, siCDBDesign)

	def RemovePDBPartitionByName(self, sPartition=defaultNamedNotOptArg, siCDBDesign=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(205, LCID, 1, (24, 0), ((8, 1), (8, 1)),sPartition
			, siCDBDesign)

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

class IPredicate(DispatchBaseClass):
	CLSID = IID('{230DA384-5030-11D3-8851-0060B0EF0A25}')
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

class IProjectData(DispatchBaseClass):
	CLSID = IID('{956DD308-D5ED-40A1-83F2-84113B8937C1}')
	coclass_clsid = IID('{8B3637D0-6CF5-1014-9D62-FFC3EECCF0AC}')

	def AddNetlistLib(self, nAtPos=defaultNamedNotOptArg, sAlias=defaultNamedNotOptArg, sPath=defaultNamedNotOptArg, Type=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(48, LCID, 1, (11, 0), ((3, 1), (8, 1), (8, 1), (3, 1)),nAtPos
			, sAlias, sPath, Type)

	def AddiCDBDesign(self, sTopBlockName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(36, LCID, 1, (11, 0), ((8, 1),),sTopBlockName
			)

	def FindNetlistLibPos(self, sAlias=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(46, LCID, 1, (3, 0), ((8, 1),),sAlias
			)

	def GetBordersFilePath(self, resolveSoftPrefix=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(14, LCID, 1, (8, 0), ((11, 1),),resolveSoftPrefix
			)

	def GetBusContentsFilePath(self, resolveSoftPrefix=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(29, LCID, 1, (8, 0), ((11, 1),),resolveSoftPrefix
			)

	def GetFlowType(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(39, LCID, 1, (8, 0), (),)

	def GetFrontEndSnapshot(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(31, LCID, 1, (8, 0), (),)

	# Result is of type IODProjectData
	def GetIODProjectData(self):
		ret = self._oleobj_.InvokeTypes(35, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetIODProjectData', '{3D2B940D-C2B5-440E-AB57-E8C6F3FB34C9}')
		return ret

	# Result is of type IVdLibrary
	def GetNetlistLib(self, nPos=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(45, LCID, 1, (9, 0), ((3, 1),),nPos
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetNetlistLib', '{28D40DF1-22F3-11D0-91AB-58F3E7000000}')
		return ret

	def GetNetlistLibCount(self):
		return self._oleobj_.InvokeTypes(44, LCID, 1, (3, 0), (),)

	def GetPCBDesignPath(self, siCDBDesign=defaultNamedNotOptArg, resolveSoftPrefix=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(33, LCID, 1, (8, 0), ((8, 1), (11, 1)),siCDBDesign
			, resolveSoftPrefix)

	# Result is of type IPDBPartitions
	def GetPDBPartitions(self):
		ret = self._oleobj_.InvokeTypes(22, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetPDBPartitions', '{D17E5439-1B5A-40D5-A115-1E4656FB102B}')
		return ret

	def GetPinComponentsFilePath(self, resolveSoftPrefix=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(18, LCID, 1, (8, 0), ((11, 1),),resolveSoftPrefix
			)

	# Result is of type IStringList
	def GetPinNumbers(self, sPartitionName=defaultNamedNotOptArg, sSymbolName=defaultNamedNotOptArg, sPartNumber=defaultNamedNotOptArg, lSlot=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(42, LCID, 1, (9, 0), ((8, 1), (8, 1), (8, 1), (3, 1)),sPartitionName
			, sSymbolName, sPartNumber, lSlot)
		if ret is not None:
			ret = Dispatch(ret, 'GetPinNumbers', '{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')
		return ret

	def GetProjectFilePath(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(3, LCID, 1, (8, 0), (),)

	def GetProjectName(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(2, LCID, 1, (8, 0), (),)

	def GetProjectPath(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1, LCID, 1, (8, 0), (),)

	def GetSearchPathScheme(self, siCDBDesign=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(23, LCID, 1, (8, 0), ((8, 1),),siCDBDesign
			)

	def GetSlotsCount(self, sPartitionName=defaultNamedNotOptArg, sSymbolName=defaultNamedNotOptArg, sPartNumber=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(41, LCID, 1, (3, 0), ((8, 1), (8, 1), (8, 1)),sPartitionName
			, sSymbolName, sPartNumber)

	def GetSnapshotName(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(6, LCID, 1, (8, 0), (),)

	# Result is of type ISymbolPartitions
	def GetSymbolPartitions(self):
		ret = self._oleobj_.InvokeTypes(7, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetSymbolPartitions', '{8DE1FE34-146C-4C91-8B52-EE97F9292EEF}')
		return ret

	def GetiCDBDesignRootBlock(self, siCDBDesign=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(12, LCID, 1, (8, 0), ((8, 1),),siCDBDesign
			)

	def GetiCDBDesignType(self, siCDBDesign=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(10, LCID, 1, (8, 0), ((8, 1),),siCDBDesign
			)

	# Result is of type IStringList
	def GetiCDBDesigns(self):
		ret = self._oleobj_.InvokeTypes(9, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetiCDBDesigns', '{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')
		return ret

	def GetiCDBDiscardFilePath(self, resolveSoftPrefix=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(20, LCID, 1, (8, 0), ((11, 1),),resolveSoftPrefix
			)

	def GetiCDBServerName(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(25, LCID, 1, (8, 0), (),)

	def GetiCDBServerPortsFilePath(self, resolveSoftPrefix=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(27, LCID, 1, (8, 0), ((11, 1),),resolveSoftPrefix
			)

	def RemoveNetlistLib(self, nPos=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(47, LCID, 1, (11, 0), ((3, 1),),nPos
			)

	def RemoveiCDBDesign(self, sTopBlockName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(37, LCID, 1, (11, 0), ((8, 1),),sTopBlockName
			)

	def RenameiCDBDesign(self, sOldName=defaultNamedNotOptArg, sNewName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(38, LCID, 1, (11, 0), ((8, 1), (8, 1)),sOldName
			, sNewName)

	def SaveNetlistLibs(self):
		return self._oleobj_.InvokeTypes(49, LCID, 1, (24, 0), (),)

	def SetBordersFilePath(self, sBordersFilePath=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(15, LCID, 1, (24, 0), ((8, 1),),sBordersFilePath
			)

	def SetBusContentsFilePath(self, sBusContentsFilePath=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(30, LCID, 1, (24, 0), ((8, 1),),sBusContentsFilePath
			)

	def SetFlowType(self, sFlowType=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(40, LCID, 1, (24, 0), ((8, 1),),sFlowType
			)

	def SetFrontEndSnapshot(self, sFrontEndSnapshot=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(32, LCID, 1, (24, 0), ((8, 1),),sFrontEndSnapshot
			)

	def SetPCBDesignPath(self, sPCBDesignPath=defaultNamedNotOptArg, siCDBDesign=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(34, LCID, 1, (24, 0), ((8, 1), (8, 1)),sPCBDesignPath
			, siCDBDesign)

	def SetPinComponentsFilePath(self, sPinComponentsFilePath=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(19, LCID, 1, (24, 0), ((8, 1),),sPinComponentsFilePath
			)

	def SetSearchPathScheme(self, sSearchPathScheme=defaultNamedNotOptArg, siCDBDesign=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(24, LCID, 1, (24, 0), ((8, 1), (8, 1)),sSearchPathScheme
			, siCDBDesign)

	def SetiCDBDesignRootBlock(self, siCDBDesignRootBlock=defaultNamedNotOptArg, siCDBDesign=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(13, LCID, 1, (24, 0), ((8, 1), (8, 1)),siCDBDesignRootBlock
			, siCDBDesign)

	def SetiCDBDesignType(self, siCDBDesignType=defaultNamedNotOptArg, siCDBDesign=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(11, LCID, 1, (24, 0), ((8, 1), (8, 1)),siCDBDesignType
			, siCDBDesign)

	def SetiCDBDiscardFilePath(self, siCDBDiscardFilePath=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(21, LCID, 1, (24, 0), ((8, 1),),siCDBDiscardFilePath
			)

	def SetiCDBServerName(self, siCDBServerName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(26, LCID, 1, (24, 0), ((8, 1),),siCDBServerName
			)

	def SetiCDBServerPortsFilePath(self, siCDBServerPortsFilePath=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(28, LCID, 1, (24, 0), ((8, 1),),siCDBServerPortsFilePath
			)

	def UpdateOtherObjects(self, eWhatToUpdate=defaultNamedNotOptArg, eUpdateScope=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(43, LCID, 1, (24, 0), ((3, 1), (3, 1)),eWhatToUpdate
			, eUpdateScope)

	_prop_map_get_ = {
		"CentralLibraryPath": (5, 2, (8, 0), (), "CentralLibraryPath", None),
		"iCDBDir": (4, 2, (8, 0), (), "iCDBDir", None),
	}
	_prop_map_put_ = {
		"CentralLibraryPath": ((5, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IProjectManagerEventSink(DispatchBaseClass):
	CLSID = IID('{B635CF94-49E3-454C-B5C3-1ECD6AE4AA50}')
	coclass_clsid = IID('{8B36C7B3-6CF5-1014-9D62-FFC3EECCF0AC}')

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

class IRipper(DispatchBaseClass):
	CLSID = IID('{FE3DB4AE-6C5C-426D-93A7-1308F624DDD9}')
	coclass_clsid = IID('{8B36ACFF-6CF5-1014-9D62-FFC3EECCF0AC}')

	# Result is of type IVdNet
	def GetConnectedObject(self, Net=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(1, LCID, 1, (9, 0), ((9, 1),),Net
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetConnectedObject', '{AE729492-9683-11CE-8246-00001B4D36B5}')
		return ret

	# Result is of type IVdObjs
	def GetConnectedObjects(self):
		ret = self._oleobj_.InvokeTypes(2, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetConnectedObjects', '{BD2EDF77-7E28-11CE-822D-00001B4D36B7}')
		return ret

	def GetMappedSignal(self, Net=defaultNamedNotOptArg, sSignal=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(3, LCID, 1, (8, 0), ((9, 1), (8, 1)),Net
			, sSignal)

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

class IStringCollection(DispatchBaseClass):
	CLSID = IID('{7BB17D63-FAE6-11D1-BE10-00A0C9204FDC}')
	coclass_clsid = IID('{8B36C077-6CF5-1014-9D62-FFC3EECCF0AC}')

	def Item(self, Index=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(2, LCID, 1, (8, 0), ((3, 1),),Index
			)

	def Remove(self, Index=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((3, 1),),Index
			)

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
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
	#This class has Item property/method which allows indexed access with the object[key] syntax.
	#Some objects will accept a string or other type of key in addition to integers.
	#Note that many Office objects do not use zero-based indexing.
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(2, LCID, 1, 1, key)), "Item", None)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IStringList(DispatchBaseClass):
	CLSID = IID('{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')
	coclass_clsid = IID('{8B3630F8-6CF5-1014-9D62-FFC3EECCF0AC}')

	def Append(self, sItem=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((8, 1),),sItem
			)

	def Clear(self):
		return self._oleobj_.InvokeTypes(6, LCID, 1, (24, 0), (),)

	def GetCount(self):
		return self._oleobj_.InvokeTypes(1, LCID, 1, (3, 0), (),)

	def GetItem(self, Index=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(2, LCID, 1, (8, 0), ((3, 1),),Index
			)

	def Insert(self, sItem=defaultNamedNotOptArg, Index=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(4, LCID, 1, (24, 0), ((8, 1), (3, 1)),sItem
			, Index)

	def Remove(self, Index=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(5, LCID, 1, (24, 0), ((3, 1),),Index
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

class ISymbolPartitions(DispatchBaseClass):
	CLSID = IID('{8DE1FE34-146C-4C91-8B52-EE97F9292EEF}')
	coclass_clsid = IID('{8B3632A1-6CF5-1014-9D62-FFC3EECCF0AC}')

	def AppendSymbolPartition(self, sPartition=defaultNamedNotOptArg, siCDBDesign=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(104, LCID, 1, (24, 0), ((8, 1), (8, 1)),sPartition
			, siCDBDesign)

	def GetSymbolPartition(self, Index=defaultNamedNotOptArg, siCDBDesign=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(100, LCID, 1, (8, 0), ((3, 1), (8, 1)),Index
			, siCDBDesign)

	# Result is of type IStringList
	def GetSymbolPartitionsArray(self, siCDBDesign=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(102, LCID, 1, (9, 0), ((8, 1),),siCDBDesign
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetSymbolPartitionsArray', '{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')
		return ret

	def GetSymbolPartitionsCount(self, siCDBDesign=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(101, LCID, 1, (3, 0), ((8, 1),),siCDBDesign
			)

	def InsertSymbolPartition(self, sPartition=defaultNamedNotOptArg, Index=defaultNamedNotOptArg, siCDBDesign=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(103, LCID, 1, (24, 0), ((8, 1), (3, 1), (8, 1)),sPartition
			, Index, siCDBDesign)

	def RemoveSymbolPartitionByIndex(self, Index=defaultNamedNotOptArg, siCDBDesign=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(106, LCID, 1, (24, 0), ((3, 1), (8, 1)),Index
			, siCDBDesign)

	def RemoveSymbolPartitionByName(self, sPartition=defaultNamedNotOptArg, siCDBDesign=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(105, LCID, 1, (24, 0), ((8, 1), (8, 1)),sPartition
			, siCDBDesign)

	def SymbolPartitionExists(self, sPartition=defaultNamedNotOptArg, siCDBDesign=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(107, LCID, 1, (11, 0), ((8, 1), (8, 1)),sPartition
			, siCDBDesign)

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

class IVdApp(DispatchBaseClass):
	CLSID = IID('{EA4ABD71-84B0-11CE-8237-00001B4D36B5}')
	coclass_clsid = IID('{8B364B47-6CF5-1014-9D62-FFC3EECCF0AC}')

	def Activate(self):
		return self._oleobj_.InvokeTypes(201, LCID, 1, (24, 0), (),)

	def AddAddin(self, pAddinInfo=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(273, LCID, 1, (11, 0), ((9, 1),),pAddinInfo
			)

	def AddLibrary(self, LibraryPath=defaultNamedNotOptArg, LibraryAlias=defaultNamedNotOptArg, LibraryAccess=defaultNamedNotOptArg, Position=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(25, LCID, 1, (11, 0), ((8, 1), (8, 1), (3, 1), (3, 1)),LibraryPath
			, LibraryAlias, LibraryAccess, Position)

	def AddLibraryAndSaveIni(self, LibraryPath=defaultNamedNotOptArg, LibraryAlias=defaultNamedNotOptArg, LibraryAccess=defaultNamedNotOptArg, Position=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(104, LCID, 1, (11, 0), ((8, 1), (8, 1), (3, 1), (3, 1)),LibraryPath
			, LibraryAlias, LibraryAccess, Position)

	def AnnoDisplayTime(self, Context=defaultNamedNotOptArg, Position=defaultNamedNotOptArg, Timestring=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(85, LCID, 1, (24, 0), ((8, 1), (3, 1), (8, 1)),Context
			, Position, Timestring)

	def AnnoDisplayValue(self, Context=defaultNamedNotOptArg, DesignPath=defaultNamedNotOptArg, AnnType=defaultNamedNotOptArg, AnnObject=defaultNamedNotOptArg
			, ObjName=defaultNamedNotOptArg, ObjValue=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(86, LCID, 1, (24, 0), ((8, 1), (8, 1), (3, 1), (3, 1), (8, 1), (8, 1)),Context
			, DesignPath, AnnType, AnnObject, ObjName, ObjValue
			)

	def AppendOutput(self, TabName=defaultNamedNotOptArg, String=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(223, LCID, 1, (24, 0), ((8, 1), (8, 1)),TabName
			, String)

	def AttributeCanHaveOatValue(self, AttributeName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(74, LCID, 1, (11, 0), ((8, 1),),AttributeName
			)

	def AttributeValueMustBeUpper(self, AttributeName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(77, LCID, 1, (11, 0), ((8, 1),),AttributeName
			)

	# Result is of type IBindingTables
	def Bindings(self, BindingTable=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(219, LCID, 1, (9, 0), ((8, 1),),BindingTable
			)
		if ret is not None:
			ret = Dispatch(ret, 'Bindings', '{A73EBAD3-B3F1-11D2-99AE-00A0C966477E}')
		return ret

	def BroadcastDBConfigModified(self, sSource=defaultNamedNotOptArg, sPath=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(298, LCID, 1, (24, 0), ((8, 1), (8, 1)),sSource
			, sPath)

	def BrowseForSymbol(self, OnlyBorders=defaultNamedNotOptArg, Title=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(72, LCID, 1, (8, 0), ((11, 1), (8, 1)),OnlyBorders
			, Title)

	def CheckIfNavigatorAddinsOpen(self):
		return self._oleobj_.InvokeTypes(107, LCID, 1, (11, 0), (),)

	def ClearAllLibraries(self):
		return self._oleobj_.InvokeTypes(28, LCID, 1, (11, 0), (),)

	def ClearEEVMMode(self):
		return self._oleobj_.InvokeTypes(248, LCID, 1, (24, 0), (),)

	def CloseNavigatorAddins(self):
		return self._oleobj_.InvokeTypes(108, LCID, 1, (24, 0), (),)

	def CloseProject(self):
		return self._oleobj_.InvokeTypes(274, LCID, 1, (11, 0), (),)

	def CommandDisable(self, CommandName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(43, LCID, 1, (11, 0), ((8, 1),),CommandName
			)

	def CommandEnable(self, CommandName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(42, LCID, 1, (11, 0), ((8, 1),),CommandName
			)

	def CommandRemove(self, CommandName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(44, LCID, 1, (11, 0), ((8, 1),),CommandName
			)

	# Result is of type ICommandsManager
	def CommandsManager(self):
		ret = self._oleobj_.InvokeTypes(220, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'CommandsManager', '{AA7F70A6-2F0E-417C-A1D2-C1621D728EB0}')
		return ret

	def ConvertSchematicToICT(self, sSchName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(286, LCID, 1, (11, 0), ((8, 1),),sSchName
			)

	def ConvertSymbol(self, sSymbol=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(252, LCID, 1, (11, 0), ((8, 1),),sSymbol
			)

	def CreateProjectLibrary(self):
		return self._oleobj_.InvokeTypes(304, LCID, 1, (11, 0), (),)

	def CreateToolbar(self, Name=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(255, LCID, 1, (11, 0), ((8, 1),),Name
			)

	def DataObjExists(self, Library=defaultNamedNotOptArg, Name=defaultNamedNotOptArg, Extension=defaultNamedNotOptArg, Class=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(37, LCID, 1, (11, 0), ((8, 1), (8, 1), (8, 1), (3, 1)),Library
			, Name, Extension, Class)

	def DataObjGetPath(self, Library=defaultNamedNotOptArg, Name=defaultNamedNotOptArg, Extension=defaultNamedNotOptArg, Class=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(38, LCID, 1, (8, 0), ((8, 1), (8, 1), (8, 1), (3, 1)),Library
			, Name, Extension, Class)

	def DataTag(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(291, LCID, 1, (8, 0), (),)

	def DeleteBlock(self, Name=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(256, LCID, 1, (11, 0), ((8, 1),),Name
			)

	def DeleteLibrary(self, Position=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(26, LCID, 1, (11, 0), ((3, 1),),Position
			)

	def DeleteLibraryAndSaveIni(self, Position=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(105, LCID, 1, (11, 0), ((3, 1),),Position
			)

	def DeleteSheet(self, DesignName=defaultNamedNotOptArg, SheetNumber=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(76, LCID, 1, (11, 0), ((8, 1), (3, 1)),DesignName
			, SheetNumber)

	# Result is of type IVdObjs
	def DesignBlocks(self, Library=defaultNamedNotOptArg, Name=defaultNamedNotOptArg, SheetNumber=defaultNamedNotOptArg, LevelString=defaultNamedNotOptArg
			, RecurseDown=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(50, LCID, 1, (9, 0), ((8, 1), (8, 1), (8, 1), (8, 1), (11, 1)),Library
			, Name, SheetNumber, LevelString, RecurseDown)
		if ret is not None:
			ret = Dispatch(ret, 'DesignBlocks', '{BD2EDF77-7E28-11CE-822D-00001B4D36B7}')
		return ret

	# Result is of type IVdObjs
	def DesignComponents(self, Library=defaultNamedNotOptArg, Name=defaultNamedNotOptArg, EndSheet='', LevelString=''
			, RecurseDown=True):
		return self._ApplyTypes_(59, 1, (9, 32), ((8, 1), (8, 1), (8, 49), (8, 49), (11, 49)), 'DesignComponents', '{BD2EDF77-7E28-11CE-822D-00001B4D36B7}',Library
			, Name, EndSheet, LevelString, RecurseDown)

	# Result is of type IVdObjs
	def DesignNets(self, Library=defaultNamedNotOptArg, Name=defaultNamedNotOptArg, EndSheet='', LevelString=''
			, RecurseDown=True):
		return self._ApplyTypes_(276, 1, (9, 32), ((8, 1), (8, 1), (8, 49), (8, 49), (11, 49)), 'DesignNets', '{BD2EDF77-7E28-11CE-822D-00001B4D36B7}',Library
			, Name, EndSheet, LevelString, RecurseDown)

	# Result is of type IStringCollection
	def DesignPaths(self, Library=defaultNamedNotOptArg, Name=defaultNamedNotOptArg, LevelString=defaultNamedNotOptArg, RecurseDown=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(54, LCID, 1, (9, 0), ((8, 1), (8, 1), (8, 1), (11, 1)),Library
			, Name, LevelString, RecurseDown)
		if ret is not None:
			ret = Dispatch(ret, 'DesignPaths', '{7BB17D63-FAE6-11D1-BE10-00A0C9204FDC}')
		return ret

	# Result is of type IDesignSearcherAutomation
	def DesignSearcher(self):
		ret = self._oleobj_.InvokeTypes(297, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'DesignSearcher', '{3EBAD6B7-B757-4A57-9657-DD43BF86A526}')
		return ret

	def DisableSelectionBroadcast(self):
		return self._oleobj_.InvokeTypes(272, LCID, 1, (24, 0), (),)

	def EnableEEVMMode(self, eevmDataFile=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(247, LCID, 1, (24, 0), ((8, 1),),eevmDataFile
			)

	def EnableSelectionBroadcast(self):
		return self._oleobj_.InvokeTypes(271, LCID, 1, (24, 0), (),)

	def ExecuteCommand(self, CommandString=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(29, LCID, 1, (11, 0), ((8, 1),),CommandString
			)

	def ExecuteCommandByID(self, command_Id=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(307, LCID, 1, (24, 0), ((3, 1),),command_Id
			)

	def ExecuteMenuCommand(self, command_name=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(89, LCID, 1, (24, 0), ((8, 1),),command_name
			)

	def ExportForeignDatabase(self, sPath=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(264, LCID, 1, (11, 0), ((8, 1),),sPath
			)

	def ExportSymbol(self, sSymbolName=defaultNamedNotOptArg, sTargetDir=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(280, LCID, 1, (11, 0), ((8, 1), (8, 1)),sSymbolName
			, sTargetDir)

	def ExtractPCB(self, sPath=defaultNamedNotOptArg, sDetailedWiring=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(275, LCID, 1, (11, 0), ((8, 1), (8, 1)),sPath
			, sDetailedWiring)

	def FireCentralLibraryReload(self):
		return self._oleobj_.InvokeTypes(257, LCID, 1, (24, 0), (),)

	def GetActiveDesign(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(229, LCID, 1, (8, 0), (),)

	def GetClassDefinitions(self, CreateIfNotDefined=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(79, LCID, 1, (9, 0), ((11, 1),),CreateIfNotDefined
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetClassDefinitions', None)
		return ret

	# Result is of type ICommonPropertyManager
	def GetCommonPropertyManager(self):
		ret = self._oleobj_.InvokeTypes(243, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetCommonPropertyManager', '{E8758B51-DEBB-46FD-A192-962B14F57FA4}')
		return ret

	# Result is of type IStringList
	def GetConfigurationProperty(self, Name=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(244, LCID, 1, (9, 0), ((8, 1),),Name
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetConfigurationProperty', '{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')
		return ret

	def GetCurrentProdLib(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(312, LCID, 1, (8, 0), (),)

	# Result is of type IColor
	def GetDefaultColor(self, ObjectType=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(261, LCID, 1, (9, 0), ((3, 1),),ObjectType
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetDefaultColor', '{C1031A0C-15BD-4897-A3E5-4C615CDEA684}')
		return ret

	def GetDefaultProdLib(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(313, LCID, 1, (8, 0), (),)

	# Result is of type IFramework
	def GetFramework(self):
		ret = self._oleobj_.InvokeTypes(242, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetFramework', '{77CD6602-703B-4AFA-A4C1-B1652A257F15}')
		return ret

	def GetICTContents(self, ICTName=defaultNamedNotOptArg, outputFilePath=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(258, LCID, 1, (11, 0), ((8, 1), (8, 1)),ICTName
			, outputFilePath)

	# Result is of type IICTDocuments
	def GetICTDocuments(self):
		ret = self._oleobj_.InvokeTypes(259, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetICTDocuments', '{2A3CCA57-9C38-4484-A6A3-7521DDF7DAD0}')
		return ret

	def GetLastErrorId(self):
		return self._oleobj_.InvokeTypes(240, LCID, 1, (3, 0), (),)

	def GetLastErrorString(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(239, LCID, 1, (8, 0), (),)

	def GetLibSpec(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(317, LCID, 1, (8, 0), (),)

	# Result is of type IVdObjs
	def GetLibraries(self):
		ret = self._oleobj_.InvokeTypes(30, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetLibraries', '{BD2EDF77-7E28-11CE-822D-00001B4D36B7}')
		return ret

	def GetPEFlowMode(self):
		return self._oleobj_.InvokeTypes(283, LCID, 1, (3, 0), (),)

	def GetProdLibReadOnly(self):
		return self._oleobj_.InvokeTypes(315, LCID, 1, (11, 0), (),)

	# Result is of type IStringList
	def GetProdLibs(self, libSpec=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(310, LCID, 1, (9, 0), ((8, 1),),libSpec
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetProdLibs', '{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')
		return ret

	# Result is of type IProjectData
	def GetProjectData(self):
		ret = self._oleobj_.InvokeTypes(228, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetProjectData', '{956DD308-D5ED-40A1-83F2-84113B8937C1}')
		return ret

	def GetProjectType(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(299, LCID, 1, (8, 0), (),)

	# Result is of type IVdAppProtectionProxy
	def GetProtectionProxy(self):
		ret = self._oleobj_.InvokeTypes(268, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetProtectionProxy', '{8E0609DD-208C-42B6-A1B0-00DAA3E45423}')
		return ret

	# Result is of type ISystemDesign
	def GetSystemDesign(self):
		ret = self._oleobj_.InvokeTypes(287, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetSystemDesign', '{C8B527DC-E1E6-439B-8C7F-D55BACC1D5F1}')
		return ret

	def GetTypeFromIDispatch(self, Dispatch=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(20, LCID, 1, (3, 0), ((9, 1),),Dispatch
			)

	def Guid(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(22, LCID, 1, (8, 0), (),)

	def HideModelProperties(self, mode=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(302, LCID, 1, (24, 0), ((11, 1),),mode
			)

	def ImportEEToPE(self, sEEPrj=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(296, LCID, 1, (11, 0), ((8, 1),),sEEPrj
			)

	def ImportForeignDatabase(self, sPath=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(265, LCID, 1, (11, 0), ((8, 1),),sPath
			)

	def ImportPADS(self, ProjectPath=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(314, LCID, 1, (11, 0), ((8, 1),),ProjectPath
			)

	def ImportPadsPE(self, sPrj=defaultNamedNotOptArg, sPcb=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(288, LCID, 1, (11, 0), ((8, 1), (8, 1)),sPrj
			, sPcb)

	def Initialize(self, WDIRPath=defaultNamedNotOptArg, LicensePath=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(203, LCID, 1, (3, 0), ((8, 1), (8, 1)),WDIRPath
			, LicensePath)

	def InsertSheet(self, DesignName=defaultNamedNotOptArg, SheetNumber=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(75, LCID, 1, (11, 0), ((8, 1), (3, 1)),DesignName
			, SheetNumber)

	def IsAppStarted(self):
		return self._oleobj_.InvokeTypes(294, LCID, 1, (11, 0), (),)

	def IsEEVMModeEnabled(self):
		return self._oleobj_.InvokeTypes(249, LCID, 1, (11, 0), (),)

	def IsLibDeletable(self, Position=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(24, LCID, 1, (11, 0), ((3, 1),),Position
			)

	def IsManagedBlock(self, sMBName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(305, LCID, 1, (11, 0), ((8, 1),),sMBName
			)

	def IsManagedBlockSource(self, sMBName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(306, LCID, 1, (11, 0), ((8, 1),),sMBName
			)

	def IsProdLibSet(self):
		return self._oleobj_.InvokeTypes(316, LCID, 1, (11, 0), (),)

	def IsProjectOpened(self):
		return self._oleobj_.InvokeTypes(295, LCID, 1, (11, 0), (),)

	def IsReadOnlyMode(self):
		return self._oleobj_.InvokeTypes(293, LCID, 1, (11, 0), (),)

	def IsReferenceApplication(self):
		return self._oleobj_.InvokeTypes(290, LCID, 1, (11, 0), (),)

	def KickViewbase(self, ForceReload=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(97, LCID, 1, (24, 0), ((11, 1),),ForceReload
			)

	def LMGetSymbolLibPath(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(284, LCID, 1, (8, 0), (),)

	def LMSetSymbolLibPath(self, sPath=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(285, LCID, 1, (11, 0), ((8, 1),),sPath
			)

	def LaunchSymbolEditor(self, sSymbolName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(263, LCID, 1, (24, 0), ((8, 1),),sSymbolName
			)

	# Result is of type IMGCDesignerDataManagement
	def MGCDesignerDataManagement(self):
		ret = self._oleobj_.InvokeTypes(303, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'MGCDesignerDataManagement', '{96EB093C-B1E3-444B-B39D-08D05CB0DF06}')
		return ret

	def MakeReusableBlock(self, ProjectName=defaultNamedNotOptArg, SchematicRoot=defaultNamedNotOptArg, DestDir=defaultNamedNotOptArg, RBName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(103, LCID, 1, (24, 0), ((8, 1), (8, 1), (8, 1), (8, 1)),ProjectName
			, SchematicRoot, DestDir, RBName)

	def MoveLibrary(self, FromPosition=defaultNamedNotOptArg, ToPosition=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(27, LCID, 1, (11, 0), ((3, 1), (3, 1)),FromPosition
			, ToPosition)

	def MoveLibraryAndSaveIni(self, FromPosition=defaultNamedNotOptArg, ToPosition=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(106, LCID, 1, (11, 0), ((3, 1), (3, 1)),FromPosition
			, ToPosition)

	def NewProject(self, ProjectPath=defaultNamedNotOptArg, CentralLibraryPath=defaultNamedNotOptArg, ServerName=defaultNamedNotOptArg, ProjectTemplatePath=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(251, LCID, 1, (11, 0), ((8, 1), (8, 1), (8, 1), (8, 1)),ProjectPath
			, CentralLibraryPath, ServerName, ProjectTemplatePath)

	# The method ObjectColor is actually a property, but must be used as a method to correctly pass the arguments
	def ObjectColor(self, ObjectType=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(65, LCID, 2, (3, 0), ((3, 1),),ObjectType
			)

	# Result is of type IVdObjs
	def OpenBlocks(self, BlockType=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(82, LCID, 1, (9, 0), ((3, 1),),BlockType
			)
		if ret is not None:
			ret = Dispatch(ret, 'OpenBlocks', '{BD2EDF77-7E28-11CE-822D-00001B4D36B7}')
		return ret

	def OpenDetailedComponentView(self, LibraryPath=defaultNamedNotOptArg, partNumber=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(319, LCID, 1, (24, 0), ((8, 1), (8, 1)),LibraryPath
			, partNumber)

	def OpenDetailedManagedBlockView(self, Name=defaultNamedNotOptArg, Version=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(320, LCID, 1, (24, 0), ((8, 1), (8, 1)),Name
			, Version)

	def OpenProject(self, ProjectPath=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(227, LCID, 1, (11, 0), ((8, 1),),ProjectPath
			)

	# Result is of type IVdApp
	def OpenReference(self, sProjectPath=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(292, LCID, 1, (9, 0), ((8, 1),),sProjectPath
			)
		if ret is not None:
			ret = Dispatch(ret, 'OpenReference', '{EA4ABD71-84B0-11CE-8237-00001B4D36B5}')
		return ret

	def OpenURL(self, URL=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(225, LCID, 1, (24, 0), ((8, 1),),URL
			)

	def ParamAddListName(self, which_param=defaultNamedNotOptArg, new_name=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(39, LCID, 1, (24, 0), ((3, 1), (8, 1)),which_param
			, new_name)

	# Result is of type IStringCollection
	def ParamGetListNames(self, which_param=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(84, LCID, 1, (9, 0), ((3, 1),),which_param
			)
		if ret is not None:
			ret = Dispatch(ret, 'ParamGetListNames', '{7BB17D63-FAE6-11D1-BE10-00A0C9204FDC}')
		return ret

	def ParamGetMode(self, Index=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(14, LCID, 1, (3, 0), ((3, 1),),Index
			)

	def ParamGetValue(self, Index=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(13, LCID, 1, (3, 0), ((3, 1),),Index
			)

	def ParamSetMode(self, Index=defaultNamedNotOptArg, NewValue=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(15, LCID, 1, (24, 0), ((3, 1), (3, 1)),Index
			, NewValue)

	def ParamSetValue(self, Index=defaultNamedNotOptArg, NewValue=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(12, LCID, 1, (24, 0), ((3, 1), (3, 1)),Index
			, NewValue)

	def PreviewDecal(self, DecalName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(78, LCID, 1, (11, 0), ((8, 1),),DecalName
			)

	def PrintProject(self, DesignName=defaultNamedNotOptArg, LevelStrings=defaultNamedNotOptArg, PrintSymbols=defaultNamedNotOptArg, ShowOrderDialog=defaultNamedNotOptArg
			, PPOFile=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(221, LCID, 1, (24, 0), ((8, 1), (8, 1), (11, 1), (11, 1), (8, 1)),DesignName
			, LevelStrings, PrintSymbols, ShowOrderDialog, PPOFile)

	def ProductionLibraryLimitationsChanged(self):
		return self._oleobj_.InvokeTypes(308, LCID, 1, (24, 0), (),)

	def PushPath(self, Top=defaultNamedNotOptArg, HierPath=defaultNamedNotOptArg, SheetNumber=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(69, LCID, 1, (11, 0), ((8, 1), (8, 1), (8, 1)),Top
			, HierPath, SheetNumber)

	# Result is of type IVdObjs
	def Query(self, Flags=defaultNamedNotOptArg, Selected=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(83, LCID, 1, (9, 0), ((3, 1), (3, 1)),Flags
			, Selected)
		if ret is not None:
			ret = Dispatch(ret, 'Query', '{BD2EDF77-7E28-11CE-822D-00001B4D36B7}')
		return ret

	# Result is of type IVdObjs
	def QueryBlocks(self, BlockType=defaultNamedNotOptArg, Library=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(45, LCID, 1, (9, 0), ((3, 1), (8, 1)),BlockType
			, Library)
		if ret is not None:
			ret = Dispatch(ret, 'QueryBlocks', '{BD2EDF77-7E28-11CE-822D-00001B4D36B7}')
		return ret

	# Result is of type IVdObjs
	def QueryPages(self, Name=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(46, LCID, 1, (9, 0), ((8, 1),),Name
			)
		if ret is not None:
			ret = Dispatch(ret, 'QueryPages', '{BD2EDF77-7E28-11CE-822D-00001B4D36B7}')
		return ret

	def QueueDatabaseUpdates(self, bQueue=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(278, LCID, 1, (24, 0), ((11, 1),),bQueue
			)

	def Quit(self):
		return self._oleobj_.InvokeTypes(226, LCID, 1, (24, 0), (),)

	def ReadIni(self, Inifilename=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(202, LCID, 1, (11, 0), ((8, 1),),Inifilename
			)

	def RegisterOLECommand(self, CommandName=defaultNamedNotOptArg, CommandDescription=defaultNamedNotOptArg, bModifiesData=defaultNamedNotOptArg, pDispatch=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(33, LCID, 1, (11, 0), ((8, 1), (8, 1), (11, 1), (9, 1)),CommandName
			, CommandDescription, bModifiesData, pDispatch)

	def RemoveProjectSettingTab(self, TabIndicator=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(51, LCID, 1, (24, 0), ((3, 1),),TabIndicator
			)

	def ReplacePart(self, SourcePart=defaultNamedNotOptArg, Scope=defaultNamedNotOptArg, DestinationPart=defaultNamedNotOptArg, PinMapping=defaultNamedNotOptArg
			, PropertyMapping=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(300, LCID, 1, (11, 0), ((8, 1), (3, 1), (8, 1), (3, 1), (3, 1)),SourcePart
			, Scope, DestinationPart, PinMapping, PropertyMapping)

	def RunDesignIntegrityChecks(self, bNewPass=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(270, LCID, 1, (11, 0), ((11, 1),),bNewPass
			)

	def RunISE(self, sPath=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(289, LCID, 1, (11, 0), ((8, 1),),sPath
			)

	def SaveIni(self):
		return self._oleobj_.InvokeTypes(34, LCID, 1, (11, 0), (),)

	# Result is of type IVdSchematicSheetDocuments
	def SchematicSheetDocuments(self):
		ret = self._oleobj_.InvokeTypes(212, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'SchematicSheetDocuments', '{608CA7F4-A52A-4206-9580-3BEB17CE0073}')
		return ret

	def SelectComponent(self, sSchName=defaultNamedNotOptArg, sSheetName=defaultNamedNotOptArg, sCompUID=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(266, LCID, 1, (11, 0), ((8, 1), (8, 1), (8, 1)),sSchName
			, sSheetName, sCompUID)

	def SelectNet(self, sSchName=defaultNamedNotOptArg, sSheetName=defaultNamedNotOptArg, sNetUID=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(267, LCID, 1, (11, 0), ((8, 1), (8, 1), (8, 1)),sSchName
			, sSheetName, sNetUID)

	def SelectPath(self, FileName=defaultNamedNotOptArg, HierPath=defaultNamedNotOptArg, SheetNumber=defaultNamedNotOptArg, Type=defaultNamedNotOptArg
			, AddSelected=defaultNamedNotOptArg, SearchBus=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(67, LCID, 1, (11, 0), ((8, 1), (8, 1), (8, 1), (3, 1), (11, 1), (11, 1)),FileName
			, HierPath, SheetNumber, Type, AddSelected, SearchBus
			)

	def SelectPathCompPin(self, FileName=defaultNamedNotOptArg, HierPath=defaultNamedNotOptArg, SheetNumber=defaultNamedNotOptArg, PinNumber=defaultNamedNotOptArg
			, SelectType=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(68, LCID, 1, (11, 0), ((8, 1), (8, 1), (8, 1), (8, 1), (3, 1)),FileName
			, HierPath, SheetNumber, PinNumber, SelectType)

	def SetButtonBitmap(self, CommandID=defaultNamedNotOptArg, BitmapFilePath=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(253, LCID, 1, (11, 0), ((19, 1), (8, 1)),CommandID
			, BitmapFilePath)

	def SetButtonResourceDLL(self, CommandID=defaultNamedNotOptArg, DllFilePath=defaultNamedNotOptArg, resID=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(254, LCID, 1, (11, 0), ((19, 1), (8, 1), (3, 1)),CommandID
			, DllFilePath, resID)

	def SetClientAdvisor(self, Advisor=defaultNamedNotOptArg, Flags=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(11, LCID, 1, (11, 0), ((9, 1), (3, 1)),Advisor
			, Flags)

	def SetConfigurationProperty(self, Name=defaultNamedNotOptArg, val=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(245, LCID, 1, (24, 0), ((8, 1), (9, 1)),Name
			, val)

	def SetDefaultColor(self, ObjectType=defaultNamedNotOptArg, Color=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(260, LCID, 1, (24, 0), ((3, 1), (9, 1)),ObjectType
			, Color)

	def SetEnvVariable(self, pName=defaultNamedNotOptArg, pValue=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(211, LCID, 1, (11, 0), ((8, 1), (8, 1)),pName
			, pValue)

	def SetGenericStatusIndicatorState(self, eIndicatorColor=defaultNamedNotOptArg, sToolTipText=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(277, LCID, 1, (11, 0), ((3, 1), (8, 1)),eIndicatorColor
			, sToolTipText)

	def SetLibAddComp(self, DirPath=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(49, LCID, 1, (11, 0), ((8, 1),),DirPath
			)

	def SetLibFileNew(self, DirPath=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(47, LCID, 1, (11, 0), ((8, 1),),DirPath
			)

	def SetLibFileOpen(self, DirPath=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(48, LCID, 1, (11, 0), ((8, 1),),DirPath
			)

	# The method SetObjectColor is actually a property, but must be used as a method to correctly pass the arguments
	def SetObjectColor(self, ObjectType=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(65, LCID, 4, (24, 0), ((3, 1), (3, 1)),ObjectType
			, arg1)

	def SetProdLib(self, dbcPath=defaultNamedNotOptArg, prodLibName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(311, LCID, 1, (11, 0), ((8, 1), (8, 1)),dbcPath
			, prodLibName)

	def SetRedraw(self, Redraw=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(222, LCID, 1, (24, 0), ((11, 1),),Redraw
			)

	def SetViewAnalogFlag(self, state=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(52, LCID, 1, (24, 0), ((11, 1),),state
			)

	def ShouldProvideDetailedComponentView(self, LibraryPath=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(318, LCID, 1, (11, 0), ((8, 1),),LibraryPath
			)

	def StartMigration(self, ProjectPath=defaultNamedNotOptArg, CentralLibPath=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(246, LCID, 1, (11, 0), ((8, 1), (8, 1)),ProjectPath
			, CentralLibPath)

	def StartVNSD(self):
		return self._oleobj_.InvokeTypes(301, LCID, 1, (24, 0), (),)

	def SupportsProdLibLimitation(self):
		return self._oleobj_.InvokeTypes(309, LCID, 1, (11, 0), (),)

	def TextViews(self):
		ret = self._oleobj_.InvokeTypes(57, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'TextViews', None)
		return ret

	def ToolbarAction(self, Handle=defaultNamedNotOptArg, Msg=defaultNamedNotOptArg, wParam=defaultNamedNotOptArg, lParam=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(262, LCID, 1, (3, 0), ((3, 1), (3, 1), (3, 1), (3, 1)),Handle
			, Msg, wParam, lParam)

	def UnloadClassDefinitions(self):
		return self._oleobj_.InvokeTypes(81, LCID, 1, (24, 0), (),)

	def UnregisterOLECommand(self, CommandName=defaultNamedNotOptArg, ClientDispatch=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(36, LCID, 1, (11, 0), ((8, 1), (9, 1)),CommandName
			, ClientDispatch)

	def UpdateMenuBar(self, menuBarParentWnd=defaultNamedNotOptArg, hMenu=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(282, LCID, 1, (3, 0), ((3, 1), (3, 1)),menuBarParentWnd
			, hMenu)

	def UserControl(self):
		return self._oleobj_.InvokeTypes(21, LCID, 1, (11, 0), (),)

	def _GetCurrentProject(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(31, LCID, 1, (8, 0), (),)

	def _GetPrimaryDirectory(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(35, LCID, 1, (8, 0), (),)

	def _SetCurrentProject(self, ProjectFilename=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(32, LCID, 1, (24, 0), ((8, 1),),ProjectFilename
			)

	_prop_map_get_ = {
		"ActiveDocument": (208, 2, (9, 0), (), "ActiveDocument", None),
		# Method 'ActiveICTView' returns object of type 'IVdICTView'
		"ActiveICTView": (269, 2, (9, 0), (), "ActiveICTView", '{848E324F-125D-4236-981D-0EB202E628DA}'),
		# Method 'ActiveView' returns object of type 'IVdView'
		"ActiveView": (207, 2, (9, 0), (), "ActiveView", '{0892A013-86BC-11CE-8238-00001B4D36B5}'),
		"ActiveViewHandle": (40, 2, (3, 0), (), "ActiveViewHandle", None),
		"Addins": (216, 2, (9, 0), (), "Addins", None),
		# Method 'Application' returns object of type 'IVdApp'
		"Application": (3, 2, (9, 0), (), "Application", '{EA4ABD71-84B0-11CE-8237-00001B4D36B5}'),
		"BusyCursor": (61, 2, (3, 0), (), "BusyCursor", None),
		"ClientAdvisorFlags": (9, 2, (3, 0), (), "ClientAdvisorFlags", None),
		"CnsFileString": (102, 2, (8, 0), (), "CnsFileString", None),
		# Method 'CommandBars' returns object of type 'ICommandBars'
		"CommandBars": (215, 2, (9, 0), (), "CommandBars", '{91818215-A01E-11D2-8F30-0060B0EF0A25}'),
		"CommandLineArguments": (210, 2, (8, 0), (), "CommandLineArguments", None),
		"Cookies": (94, 2, (9, 0), (), "Cookies", None),
		"CurrentProject": (55, 2, (8, 0), (), "CurrentProject", None),
		# Method 'Documents' returns object of type 'IVdDocs'
		"Documents": (1, 2, (9, 0), (), "Documents", '{BD2EDF77-7E28-11CE-822D-00001B4D36B5}'),
		"EDXEngine": (281, 2, (9, 0), (), "EDXEngine", None),
		"Flows": (98, 2, (9, 0), (), "Flows", None),
		"FullName": (4, 2, (8, 0), (), "FullName", None),
		# Method 'HTMLDocuments' returns object of type 'IHTMLSourceDocuments'
		"HTMLDocuments": (213, 2, (9, 0), (), "HTMLDocuments", '{7D50CA6D-07DB-4BE0-AD95-563DED3F9157}'),
		"Interactive": (205, 2, (11, 0), (), "Interactive", None),
		"LicenseMode": (91, 2, (3, 0), (), "LicenseMode", None),
		"Name": (5, 2, (8, 0), (), "Name", None),
		"OptionLevel": (73, 2, (8, 0), (), "OptionLevel", None),
		# Method 'Parent' returns object of type 'IVdApp'
		"Parent": (6, 2, (9, 0), (), "Parent", '{EA4ABD71-84B0-11CE-8237-00001B4D36B5}'),
		"PrimaryDirectory": (56, 2, (8, 0), (), "PrimaryDirectory", None),
		"ProjMan": (88, 2, (9, 0), (), "ProjMan", None),
		"QueueSelectEvents": (224, 2, (3, 0), (), "QueueSelectEvents", None),
		"SheetsEditMode": (279, 2, (11, 0), (), "SheetsEditMode", None),
		"ShellCmd": (218, 2, (9, 0), (), "ShellCmd", None),
		"SilentMode": (250, 2, (3, 0), (), "SilentMode", None),
		# Method 'SourceDocuments' returns object of type 'IHDLSourceDocuments'
		"SourceDocuments": (214, 2, (9, 0), (), "SourceDocuments", '{AC6510A1-83C5-4486-9154-CE74592F9A48}'),
		"StatusBarText": (206, 2, (8, 0), (), "StatusBarText", None),
		"SynchronizesViewBase": (66, 2, (11, 0), (), "SynchronizesViewBase", None),
		"Version": (209, 2, (8, 0), (), "Version", None),
		"ViewBaseSession": (64, 2, (9, 0), (), "ViewBaseSession", None),
		"Visible": (204, 2, (11, 0), (), "Visible", None),
		"project": (101, 2, (9, 0), (), "project", None),
	}
	_prop_map_put_ = {
		"BusyCursor": ((61, LCID, 4, 0),()),
		"ClientAdvisorFlags": ((9, LCID, 4, 0),()),
		"CurrentProject": ((55, LCID, 4, 0),()),
		"Interactive": ((205, LCID, 4, 0),()),
		"QueueSelectEvents": ((224, LCID, 4, 0),()),
		"SheetsEditMode": ((279, LCID, 4, 0),()),
		"SilentMode": ((250, LCID, 4, 0),()),
		"StatusBarText": ((206, LCID, 4, 0),()),
		"SynchronizesViewBase": ((66, LCID, 4, 0),()),
		"Visible": ((204, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IVdAppEvents:
	'Event interface for ViewDraw Application Object'
	CLSID = CLSID_Sink = IID('{B8CC7991-E03E-11D1-BE05-00A0C9204FDC}')
	coclass_clsid = IID('{8B364B47-6CF5-1014-9D62-FFC3EECCF0AC}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnStartup",
		        2 : "OnShutdown",
		        3 : "OnActivateView",
		        4 : "OnDeactivateView",
		        5 : "OnBeforeDocumentOpened",
		        6 : "OnAfterDocumentOpened",
		        7 : "OnDocumentSave",
		        8 : "OnDocumentModified",
		        9 : "OnCreateObject",
		       10 : "OnSelect",
		       11 : "OnPaint",
		       12 : "OnDelete",
		       13 : "OnMouseMoved",
		       14 : "OnClose",
		       15 : "OnLockRequest",
		       16 : "OnUnlock",
		       17 : "OnBeforeDocumentSave",
		       18 : "OnAfterDocumentSave",
		       19 : "OnAfterSheetRead",
		       20 : "OnActivateView2",
		       21 : "OnDeactivateView2",
		       22 : "OnBlockModified",
		       23 : "OnBeforeSaveAndCheck",
		       24 : "OnAfterSaveAndCheck",
		       25 : "OnOatAdded",
		       26 : "OnPaintRegion",
		       27 : "OnBeforePrintProject",
		       28 : "OnAfterPrintProject",
		       29 : "OnPrintFile",
		       30 : "OnDocumentSaveAs",
		       31 : "OnProjectModified",
		       32 : "OnConstraintsModeChanged",
		       33 : "OnDocumentClose",
		       34 : "OnITCCommand",
		       35 : "OnSymbolPreviewed",
		       36 : "OnSourceDocumentSave",
		       37 : "OnAfterSheetReRead",
		       38 : "OnBeforeProjectModified",
		       39 : "OnSourceFileModified",
		       40 : "OnProjectChanged",
		       41 : "OnBeforeProjectChanged",
		       42 : "OnClearEEVMMode",
		       43 : "OnCentralLibraryChanged",
		       44 : "OnSearchPathSchemeChanged",
		       45 : "OnBeforeFAStarted",
		       46 : "OnAfterFAFinished",
		       47 : "OnSettingsChanged",
		       48 : "OnCreateICTObject",
		       49 : "OnProjectClosed",
		       50 : "OnSymbolUpdateStarted",
		       51 : "OnBatchAttributesAdded",
		       52 : "OnBlockLocked",
		       53 : "OnReuseBlockAdded",
		       55 : "OnAfterSymbolDefinitionRefresh",
		       56 : "OnDBConfigModified",
		       57 : "OnProductionLibraryLimitationsChanged",
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
#	def OnStartup(self):
#	def OnShutdown(self):
#	def OnActivateView(self):
#	def OnDeactivateView(self):
#	def OnBeforeDocumentOpened(self, DocumentType=defaultNamedNotOptArg, LibraryAlias=defaultNamedNotOptArg, Name=defaultNamedNotOptArg):
#	def OnAfterDocumentOpened(self, DocumentType=defaultNamedNotOptArg, LibraryAlias=defaultNamedNotOptArg, Name=defaultNamedNotOptArg):
#	def OnDocumentSave(self):
#	def OnDocumentModified(self):
#	def OnCreateObject(self, ReasonFlag=defaultNamedNotOptArg, ObjectType=defaultNamedNotOptArg, Block=defaultNamedNotOptArg, Object=defaultNamedNotOptArg):
#	def OnSelect(self, SelectionType=defaultNamedNotOptArg, Block=defaultNamedNotOptArg):
#	def OnPaint(self):
#	def OnDelete(self):
#	def OnMouseMoved(self, Flags=defaultNamedNotOptArg, X=defaultNamedNotOptArg, Y=defaultNamedNotOptArg):
#	def OnClose(self):
#	def OnLockRequest(self, Block=defaultNamedNotOptArg, Success=defaultNamedNotOptArg):
#	def OnUnlock(self, Block=defaultNamedNotOptArg):
#	def OnBeforeDocumentSave(self, Doc=defaultNamedNotOptArg):
#	def OnAfterDocumentSave(self, Doc=defaultNamedNotOptArg):
#	def OnAfterSheetRead(self, DocumentType=defaultNamedNotOptArg, LibraryAlias=defaultNamedNotOptArg, Name=defaultNamedNotOptArg):
#	def OnActivateView2(self, View=defaultNamedNotOptArg):
#	def OnDeactivateView2(self, View=defaultNamedNotOptArg):
#	def OnBlockModified(self, Block=defaultNamedNotOptArg):
#	def OnBeforeSaveAndCheck(self, Reserved=defaultNamedNotOptArg):
#	def OnAfterSaveAndCheck(self):
#	def OnOatAdded(self):
#	def OnPaintRegion(self, View=defaultNamedNotOptArg, LowerLeftx=defaultNamedNotOptArg, LowerLefty=defaultNamedNotOptArg, UpperRightx=defaultNamedNotOptArg
#			, UpperRighty=defaultNamedNotOptArg):
#	def OnBeforePrintProject(self, FileList=defaultNamedNotOptArg):
#	def OnAfterPrintProject(self):
#	def OnPrintFile(self, BlockName=defaultNamedNotOptArg, Path=defaultNamedNotOptArg, TopBlock=defaultNamedNotOptArg):
#	def OnDocumentSaveAs(self, Library=defaultNamedNotOptArg, Name=defaultNamedNotOptArg):
#	def OnProjectModified(self, NewProject=defaultNamedNotOptArg):
#	def OnConstraintsModeChanged(self, enabled=defaultNamedNotOptArg):
#	def OnDocumentClose(self, Doc=defaultNamedNotOptArg):
#	def OnITCCommand(self, Command=defaultNamedNotOptArg, CommandString=defaultNamedNotOptArg):
#	def OnSymbolPreviewed(self, SymbolBlock=defaultNamedNotOptArg):
#	def OnSourceDocumentSave(self, DocumentName=defaultNamedNotOptArg):
#	def OnAfterSheetReRead(self, Block=defaultNamedNotOptArg):
#	def OnBeforeProjectModified(self):
#	def OnSourceFileModified(self, FileName=defaultNamedNotOptArg):
#	def OnProjectChanged(self, ProjectData=defaultNamedNotOptArg):
#	def OnBeforeProjectChanged(self):
#	def OnClearEEVMMode(self):
#	def OnCentralLibraryChanged(self, sNewLMCDir=defaultNamedNotOptArg):
#	def OnSearchPathSchemeChanged(self):
#	def OnBeforeFAStarted(self):
#	def OnAfterFAFinished(self):
#	def OnSettingsChanged(self):
#	def OnCreateICTObject(self, ReasonFlag=defaultNamedNotOptArg, ObjectType=defaultNamedNotOptArg, Block=defaultNamedNotOptArg, Object=defaultNamedNotOptArg):
#	def OnProjectClosed(self):
#	def OnSymbolUpdateStarted(self):
#	def OnBatchAttributesAdded(self, comp=defaultNamedNotOptArg, AttributeListString=defaultNamedNotOptArg):
#	def OnBlockLocked(self, Block=defaultNamedNotOptArg):
#	def OnReuseBlockAdded(self, comp=defaultNamedNotOptArg):
#	def OnAfterSymbolDefinitionRefresh(self):
#	def OnDBConfigModified(self, sSource=defaultNamedNotOptArg, sPath=defaultNamedNotOptArg):
#	def OnProductionLibraryLimitationsChanged(self):


class IVdAppProtectionProxy(DispatchBaseClass):
	CLSID = IID('{8E0609DD-208C-42B6-A1B0-00DAA3E45423}')
	coclass_clsid = IID('{8B3647CF-6CF5-1014-9D62-FFC3EECCF0AC}')

	def Activate(self):
		return self._oleobj_.InvokeTypes(201, LCID, 1, (24, 0), (),)

	def AddLibrary(self, LibraryPath=defaultNamedNotOptArg, LibraryAlias=defaultNamedNotOptArg, LibraryAccess=defaultNamedNotOptArg, Position=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(25, LCID, 1, (11, 0), ((8, 1), (8, 1), (3, 1), (3, 1)),LibraryPath
			, LibraryAlias, LibraryAccess, Position)

	def AddLibraryAndSaveIni(self, LibraryPath=defaultNamedNotOptArg, LibraryAlias=defaultNamedNotOptArg, LibraryAccess=defaultNamedNotOptArg, Position=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(104, LCID, 1, (11, 0), ((8, 1), (8, 1), (3, 1), (3, 1)),LibraryPath
			, LibraryAlias, LibraryAccess, Position)

	def AnnoDisplayTime(self, Context=defaultNamedNotOptArg, Position=defaultNamedNotOptArg, Timestring=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(85, LCID, 1, (24, 0), ((8, 1), (3, 1), (8, 1)),Context
			, Position, Timestring)

	def AnnoDisplayValue(self, Context=defaultNamedNotOptArg, DesignPath=defaultNamedNotOptArg, AnnType=defaultNamedNotOptArg, AnnObject=defaultNamedNotOptArg
			, ObjName=defaultNamedNotOptArg, ObjValue=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(86, LCID, 1, (24, 0), ((8, 1), (8, 1), (3, 1), (3, 1), (8, 1), (8, 1)),Context
			, DesignPath, AnnType, AnnObject, ObjName, ObjValue
			)

	def AppendOutput(self, TabName=defaultNamedNotOptArg, String=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(223, LCID, 1, (24, 0), ((8, 1), (8, 1)),TabName
			, String)

	def AttributeCanHaveOatValue(self, AttributeName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(74, LCID, 1, (11, 0), ((8, 1),),AttributeName
			)

	def AttributeValueMustBeUpper(self, AttributeName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(77, LCID, 1, (11, 0), ((8, 1),),AttributeName
			)

	# Result is of type IBindingTables
	def Bindings(self, BindingTable=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(219, LCID, 1, (9, 0), ((8, 1),),BindingTable
			)
		if ret is not None:
			ret = Dispatch(ret, 'Bindings', '{A73EBAD3-B3F1-11D2-99AE-00A0C966477E}')
		return ret

	def BroadcastDBConfigModified(self, sSource=defaultNamedNotOptArg, sPath=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(298, LCID, 1, (24, 0), ((8, 1), (8, 1)),sSource
			, sPath)

	def BrowseForSymbol(self, OnlyBorders=defaultNamedNotOptArg, Title=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(72, LCID, 1, (8, 0), ((11, 1), (8, 1)),OnlyBorders
			, Title)

	def CheckIfNavigatorAddinsOpen(self):
		return self._oleobj_.InvokeTypes(107, LCID, 1, (11, 0), (),)

	def ClearAllLibraries(self):
		return self._oleobj_.InvokeTypes(28, LCID, 1, (11, 0), (),)

	def ClearEEVMMode(self):
		return self._oleobj_.InvokeTypes(248, LCID, 1, (24, 0), (),)

	def CloseNavigatorAddins(self):
		return self._oleobj_.InvokeTypes(108, LCID, 1, (24, 0), (),)

	def CloseProject(self):
		return self._oleobj_.InvokeTypes(274, LCID, 1, (11, 0), (),)

	def CommandDisable(self, CommandName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(43, LCID, 1, (11, 0), ((8, 1),),CommandName
			)

	def CommandEnable(self, CommandName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(42, LCID, 1, (11, 0), ((8, 1),),CommandName
			)

	def CommandRemove(self, CommandName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(44, LCID, 1, (11, 0), ((8, 1),),CommandName
			)

	# Result is of type ICommandsManager
	def CommandsManager(self):
		ret = self._oleobj_.InvokeTypes(220, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'CommandsManager', '{AA7F70A6-2F0E-417C-A1D2-C1621D728EB0}')
		return ret

	def ConvertSchematicToICT(self, sSchName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(286, LCID, 1, (11, 0), ((8, 1),),sSchName
			)

	def ConvertSymbol(self, sSymbol=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(252, LCID, 1, (11, 0), ((8, 1),),sSymbol
			)

	def CreateProjectLibrary(self):
		return self._oleobj_.InvokeTypes(304, LCID, 1, (11, 0), (),)

	def CreateToolbar(self, Name=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(255, LCID, 1, (11, 0), ((8, 1),),Name
			)

	def DataObjExists(self, Library=defaultNamedNotOptArg, Name=defaultNamedNotOptArg, Extension=defaultNamedNotOptArg, Class=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(37, LCID, 1, (11, 0), ((8, 1), (8, 1), (8, 1), (3, 1)),Library
			, Name, Extension, Class)

	def DataObjGetPath(self, Library=defaultNamedNotOptArg, Name=defaultNamedNotOptArg, Extension=defaultNamedNotOptArg, Class=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(38, LCID, 1, (8, 0), ((8, 1), (8, 1), (8, 1), (3, 1)),Library
			, Name, Extension, Class)

	def DataTag(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(291, LCID, 1, (8, 0), (),)

	def DeleteBlock(self, Name=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(256, LCID, 1, (11, 0), ((8, 1),),Name
			)

	def DeleteLibrary(self, Position=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(26, LCID, 1, (11, 0), ((3, 1),),Position
			)

	def DeleteLibraryAndSaveIni(self, Position=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(105, LCID, 1, (11, 0), ((3, 1),),Position
			)

	def DeleteSheet(self, DesignName=defaultNamedNotOptArg, SheetNumber=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(76, LCID, 1, (11, 0), ((8, 1), (3, 1)),DesignName
			, SheetNumber)

	# Result is of type IVdObjs
	def DesignBlocks(self, Library=defaultNamedNotOptArg, Name=defaultNamedNotOptArg, SheetNumber=defaultNamedNotOptArg, LevelString=defaultNamedNotOptArg
			, RecurseDown=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(50, LCID, 1, (9, 0), ((8, 1), (8, 1), (8, 1), (8, 1), (11, 1)),Library
			, Name, SheetNumber, LevelString, RecurseDown)
		if ret is not None:
			ret = Dispatch(ret, 'DesignBlocks', '{BD2EDF77-7E28-11CE-822D-00001B4D36B7}')
		return ret

	# Result is of type IVdObjs
	def DesignComponents(self, Library=defaultNamedNotOptArg, Name=defaultNamedNotOptArg, EndSheet='', LevelString=''
			, RecurseDown=True):
		return self._ApplyTypes_(59, 1, (9, 32), ((8, 1), (8, 1), (8, 49), (8, 49), (11, 49)), 'DesignComponents', '{BD2EDF77-7E28-11CE-822D-00001B4D36B7}',Library
			, Name, EndSheet, LevelString, RecurseDown)

	# Result is of type IVdObjs
	def DesignNets(self, Library=defaultNamedNotOptArg, Name=defaultNamedNotOptArg, EndSheet='', LevelString=''
			, RecurseDown=True):
		return self._ApplyTypes_(276, 1, (9, 32), ((8, 1), (8, 1), (8, 49), (8, 49), (11, 49)), 'DesignNets', '{BD2EDF77-7E28-11CE-822D-00001B4D36B7}',Library
			, Name, EndSheet, LevelString, RecurseDown)

	# Result is of type IStringCollection
	def DesignPaths(self, Library=defaultNamedNotOptArg, Name=defaultNamedNotOptArg, LevelString=defaultNamedNotOptArg, RecurseDown=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(54, LCID, 1, (9, 0), ((8, 1), (8, 1), (8, 1), (11, 1)),Library
			, Name, LevelString, RecurseDown)
		if ret is not None:
			ret = Dispatch(ret, 'DesignPaths', '{7BB17D63-FAE6-11D1-BE10-00A0C9204FDC}')
		return ret

	# Result is of type IDesignSearcherAutomation
	def DesignSearcher(self):
		ret = self._oleobj_.InvokeTypes(297, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'DesignSearcher', '{3EBAD6B7-B757-4A57-9657-DD43BF86A526}')
		return ret

	def DisableSelectionBroadcast(self):
		return self._oleobj_.InvokeTypes(272, LCID, 1, (24, 0), (),)

	def EnableEEVMMode(self, eevmDataFile=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(247, LCID, 1, (24, 0), ((8, 1),),eevmDataFile
			)

	def EnableSelectionBroadcast(self):
		return self._oleobj_.InvokeTypes(271, LCID, 1, (24, 0), (),)

	def ExecuteCommand(self, CommandString=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(29, LCID, 1, (11, 0), ((8, 1),),CommandString
			)

	def ExecuteCommandByID(self, command_Id=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(307, LCID, 1, (24, 0), ((3, 1),),command_Id
			)

	def ExecuteMenuCommand(self, command_name=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(89, LCID, 1, (24, 0), ((8, 1),),command_name
			)

	def ExportForeignDatabase(self, sPath=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(264, LCID, 1, (11, 0), ((8, 1),),sPath
			)

	def ExportSymbol(self, sSymbolName=defaultNamedNotOptArg, sTargetDir=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(280, LCID, 1, (11, 0), ((8, 1), (8, 1)),sSymbolName
			, sTargetDir)

	def ExtractPCB(self, sPath=defaultNamedNotOptArg, sDetailedWiring=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(275, LCID, 1, (11, 0), ((8, 1), (8, 1)),sPath
			, sDetailedWiring)

	def FireCentralLibraryReload(self):
		return self._oleobj_.InvokeTypes(257, LCID, 1, (24, 0), (),)

	def GetActiveDesign(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(229, LCID, 1, (8, 0), (),)

	def GetClassDefinitions(self, CreateIfNotDefined=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(79, LCID, 1, (9, 0), ((11, 1),),CreateIfNotDefined
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetClassDefinitions', None)
		return ret

	# Result is of type ICommonPropertyManager
	def GetCommonPropertyManager(self):
		ret = self._oleobj_.InvokeTypes(243, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetCommonPropertyManager', '{E8758B51-DEBB-46FD-A192-962B14F57FA4}')
		return ret

	# Result is of type IStringList
	def GetConfigurationProperty(self, Name=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(244, LCID, 1, (9, 0), ((8, 1),),Name
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetConfigurationProperty', '{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')
		return ret

	def GetCurrentProdLib(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(312, LCID, 1, (8, 0), (),)

	# Result is of type IColor
	def GetDefaultColor(self, ObjectType=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(261, LCID, 1, (9, 0), ((3, 1),),ObjectType
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetDefaultColor', '{C1031A0C-15BD-4897-A3E5-4C615CDEA684}')
		return ret

	def GetDefaultProdLib(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(313, LCID, 1, (8, 0), (),)

	# Result is of type IFramework
	def GetFramework(self):
		ret = self._oleobj_.InvokeTypes(242, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetFramework', '{77CD6602-703B-4AFA-A4C1-B1652A257F15}')
		return ret

	def GetICTContents(self, ICTName=defaultNamedNotOptArg, outputFilePath=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(258, LCID, 1, (11, 0), ((8, 1), (8, 1)),ICTName
			, outputFilePath)

	# Result is of type IICTDocuments
	def GetICTDocuments(self):
		ret = self._oleobj_.InvokeTypes(259, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetICTDocuments', '{2A3CCA57-9C38-4484-A6A3-7521DDF7DAD0}')
		return ret

	def GetLastErrorId(self):
		return self._oleobj_.InvokeTypes(240, LCID, 1, (3, 0), (),)

	def GetLastErrorString(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(239, LCID, 1, (8, 0), (),)

	def GetLibSpec(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(317, LCID, 1, (8, 0), (),)

	# Result is of type IVdObjs
	def GetLibraries(self):
		ret = self._oleobj_.InvokeTypes(30, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetLibraries', '{BD2EDF77-7E28-11CE-822D-00001B4D36B7}')
		return ret

	def GetPEFlowMode(self):
		return self._oleobj_.InvokeTypes(283, LCID, 1, (3, 0), (),)

	def GetProdLibReadOnly(self):
		return self._oleobj_.InvokeTypes(315, LCID, 1, (11, 0), (),)

	# Result is of type IStringList
	def GetProdLibs(self, libSpec=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(310, LCID, 1, (9, 0), ((8, 1),),libSpec
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetProdLibs', '{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')
		return ret

	# Result is of type IProjectData
	def GetProjectData(self):
		ret = self._oleobj_.InvokeTypes(228, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetProjectData', '{956DD308-D5ED-40A1-83F2-84113B8937C1}')
		return ret

	def GetProjectType(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(299, LCID, 1, (8, 0), (),)

	def GetTypeFromIDispatch(self, Dispatch=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(20, LCID, 1, (3, 0), ((9, 1),),Dispatch
			)

	def Guid(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(22, LCID, 1, (8, 0), (),)

	def HideModelProperties(self, bHide=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(302, LCID, 1, (24, 0), ((11, 1),),bHide
			)

	def ImportEEToPE(self, sEEPrj=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(296, LCID, 1, (11, 0), ((8, 1),),sEEPrj
			)

	def ImportForeignDatabase(self, sPath=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(265, LCID, 1, (11, 0), ((8, 1),),sPath
			)

	def ImportPadsPE(self, sPrj=defaultNamedNotOptArg, sPcb=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(288, LCID, 1, (11, 0), ((8, 1), (8, 1)),sPrj
			, sPcb)

	def Initialize(self, WDIRPath=defaultNamedNotOptArg, LicensePath=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(203, LCID, 1, (3, 0), ((8, 1), (8, 1)),WDIRPath
			, LicensePath)

	def InsertSheet(self, DesignName=defaultNamedNotOptArg, SheetNumber=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(75, LCID, 1, (11, 0), ((8, 1), (3, 1)),DesignName
			, SheetNumber)

	def IsAppStarted(self):
		return self._oleobj_.InvokeTypes(294, LCID, 1, (11, 0), (),)

	def IsEEVMModeEnabled(self):
		return self._oleobj_.InvokeTypes(249, LCID, 1, (11, 0), (),)

	def IsLibDeletable(self, Position=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(24, LCID, 1, (11, 0), ((3, 1),),Position
			)

	def IsManagedBlock(self, sMBName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(305, LCID, 1, (11, 0), ((8, 1),),sMBName
			)

	def IsManagedBlockSource(self, sMBName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(306, LCID, 1, (11, 0), ((8, 1),),sMBName
			)

	def IsProdLibSet(self):
		return self._oleobj_.InvokeTypes(316, LCID, 1, (11, 0), (),)

	def IsProjectOpened(self):
		return self._oleobj_.InvokeTypes(295, LCID, 1, (11, 0), (),)

	def IsReadOnlyMode(self):
		return self._oleobj_.InvokeTypes(293, LCID, 1, (11, 0), (),)

	def IsReferenceApplication(self):
		return self._oleobj_.InvokeTypes(290, LCID, 1, (11, 0), (),)

	def KickViewbase(self, ForceReload=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(97, LCID, 1, (24, 0), ((11, 1),),ForceReload
			)

	def LMGetSymbolLibPath(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(284, LCID, 1, (8, 0), (),)

	def LMSetSymbolLibPath(self, sPath=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(285, LCID, 1, (11, 0), ((8, 1),),sPath
			)

	def LaunchSymbolEditor(self, sSymbolName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(263, LCID, 1, (24, 0), ((8, 1),),sSymbolName
			)

	# Result is of type IMGCDesignerDataManagement
	def MGCDesignerDataManagement(self):
		ret = self._oleobj_.InvokeTypes(303, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'MGCDesignerDataManagement', '{96EB093C-B1E3-444B-B39D-08D05CB0DF06}')
		return ret

	def MakeReusableBlock(self, ProjectName=defaultNamedNotOptArg, SchematicRoot=defaultNamedNotOptArg, DestDir=defaultNamedNotOptArg, RBName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(103, LCID, 1, (24, 0), ((8, 1), (8, 1), (8, 1), (8, 1)),ProjectName
			, SchematicRoot, DestDir, RBName)

	def MoveLibrary(self, FromPosition=defaultNamedNotOptArg, ToPosition=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(27, LCID, 1, (11, 0), ((3, 1), (3, 1)),FromPosition
			, ToPosition)

	def MoveLibraryAndSaveIni(self, FromPosition=defaultNamedNotOptArg, ToPosition=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(106, LCID, 1, (11, 0), ((3, 1), (3, 1)),FromPosition
			, ToPosition)

	def NewProject(self, ProjectPath=defaultNamedNotOptArg, CentralLibraryPath=defaultNamedNotOptArg, ServerName=defaultNamedNotOptArg, ProjectTemplatePath=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(251, LCID, 1, (11, 0), ((8, 1), (8, 1), (8, 1), (8, 1)),ProjectPath
			, CentralLibraryPath, ServerName, ProjectTemplatePath)

	# The method ObjectColor is actually a property, but must be used as a method to correctly pass the arguments
	def ObjectColor(self, ObjectType=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(65, LCID, 2, (3, 0), ((3, 1),),ObjectType
			)

	# Result is of type IVdObjs
	def OpenBlocks(self, BlockType=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(82, LCID, 1, (9, 0), ((3, 1),),BlockType
			)
		if ret is not None:
			ret = Dispatch(ret, 'OpenBlocks', '{BD2EDF77-7E28-11CE-822D-00001B4D36B7}')
		return ret

	def OpenDetailedComponentView(self, LibraryPath=defaultNamedNotOptArg, partNumber=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(319, LCID, 1, (24, 0), ((8, 1), (8, 1)),LibraryPath
			, partNumber)

	def OpenDetailedManagedBlockView(self, Name=defaultNamedNotOptArg, Version=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(320, LCID, 1, (24, 0), ((8, 1), (8, 1)),Name
			, Version)

	def OpenProject(self, ProjectPath=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(227, LCID, 1, (11, 0), ((8, 1),),ProjectPath
			)

	# Result is of type IVdApp
	def OpenReference(self, sProjectPath=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(292, LCID, 1, (9, 0), ((8, 1),),sProjectPath
			)
		if ret is not None:
			ret = Dispatch(ret, 'OpenReference', '{EA4ABD71-84B0-11CE-8237-00001B4D36B5}')
		return ret

	def OpenURL(self, URL=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(225, LCID, 1, (24, 0), ((8, 1),),URL
			)

	def ParamAddListName(self, which_param=defaultNamedNotOptArg, new_name=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(39, LCID, 1, (24, 0), ((3, 1), (8, 1)),which_param
			, new_name)

	# Result is of type IStringCollection
	def ParamGetListNames(self, which_param=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(84, LCID, 1, (9, 0), ((3, 1),),which_param
			)
		if ret is not None:
			ret = Dispatch(ret, 'ParamGetListNames', '{7BB17D63-FAE6-11D1-BE10-00A0C9204FDC}')
		return ret

	def ParamGetMode(self, Index=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(14, LCID, 1, (3, 0), ((3, 1),),Index
			)

	def ParamGetValue(self, Index=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(13, LCID, 1, (3, 0), ((3, 1),),Index
			)

	def ParamSetMode(self, Index=defaultNamedNotOptArg, NewValue=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(15, LCID, 1, (24, 0), ((3, 1), (3, 1)),Index
			, NewValue)

	def ParamSetValue(self, Index=defaultNamedNotOptArg, NewValue=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(12, LCID, 1, (24, 0), ((3, 1), (3, 1)),Index
			, NewValue)

	def PreviewDecal(self, DecalName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(78, LCID, 1, (11, 0), ((8, 1),),DecalName
			)

	def PrintProject(self, DesignName=defaultNamedNotOptArg, LevelStrings=defaultNamedNotOptArg, PrintSymbols=defaultNamedNotOptArg, ShowOrderDialog=defaultNamedNotOptArg
			, PPOFile=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(221, LCID, 1, (24, 0), ((8, 1), (8, 1), (11, 1), (11, 1), (8, 1)),DesignName
			, LevelStrings, PrintSymbols, ShowOrderDialog, PPOFile)

	def ProductionLibraryLimitationsChanged(self):
		return self._oleobj_.InvokeTypes(308, LCID, 1, (24, 0), (),)

	def PushPath(self, Top=defaultNamedNotOptArg, HierPath=defaultNamedNotOptArg, SheetNumber=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(69, LCID, 1, (11, 0), ((8, 1), (8, 1), (8, 1)),Top
			, HierPath, SheetNumber)

	# Result is of type IVdObjs
	def Query(self, Flags=defaultNamedNotOptArg, Selected=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(83, LCID, 1, (9, 0), ((3, 1), (3, 1)),Flags
			, Selected)
		if ret is not None:
			ret = Dispatch(ret, 'Query', '{BD2EDF77-7E28-11CE-822D-00001B4D36B7}')
		return ret

	# Result is of type IVdObjs
	def QueryBlocks(self, BlockType=defaultNamedNotOptArg, Library=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(45, LCID, 1, (9, 0), ((3, 1), (8, 1)),BlockType
			, Library)
		if ret is not None:
			ret = Dispatch(ret, 'QueryBlocks', '{BD2EDF77-7E28-11CE-822D-00001B4D36B7}')
		return ret

	# Result is of type IVdObjs
	def QueryPages(self, Name=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(46, LCID, 1, (9, 0), ((8, 1),),Name
			)
		if ret is not None:
			ret = Dispatch(ret, 'QueryPages', '{BD2EDF77-7E28-11CE-822D-00001B4D36B7}')
		return ret

	def Quit(self):
		return self._oleobj_.InvokeTypes(226, LCID, 1, (24, 0), (),)

	def ReadIni(self, Inifilename=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(202, LCID, 1, (11, 0), ((8, 1),),Inifilename
			)

	def RegisterOLECommand(self, CommandName=defaultNamedNotOptArg, CommandDescription=defaultNamedNotOptArg, bModifiesData=defaultNamedNotOptArg, pDispatch=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(33, LCID, 1, (11, 0), ((8, 1), (8, 1), (11, 1), (9, 1)),CommandName
			, CommandDescription, bModifiesData, pDispatch)

	def RemoveProjectSettingTab(self, TabIndicator=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(51, LCID, 1, (24, 0), ((3, 1),),TabIndicator
			)

	def ReplacePart(self, SourcePart=defaultNamedNotOptArg, Scope=defaultNamedNotOptArg, DestinationPart=defaultNamedNotOptArg, PinMapping=defaultNamedNotOptArg
			, PropertyMapping=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(300, LCID, 1, (11, 0), ((8, 1), (3, 1), (8, 1), (3, 1), (3, 1)),SourcePart
			, Scope, DestinationPart, PinMapping, PropertyMapping)

	def RunISE(self, sPath=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(289, LCID, 1, (11, 0), ((8, 1),),sPath
			)

	def SaveIni(self):
		return self._oleobj_.InvokeTypes(34, LCID, 1, (11, 0), (),)

	# Result is of type IVdSchematicSheetDocuments
	def SchematicSheetDocuments(self):
		ret = self._oleobj_.InvokeTypes(212, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'SchematicSheetDocuments', '{608CA7F4-A52A-4206-9580-3BEB17CE0073}')
		return ret

	def SelectComponent(self, sSchName=defaultNamedNotOptArg, sSheetName=defaultNamedNotOptArg, sCompUID=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(266, LCID, 1, (11, 0), ((8, 1), (8, 1), (8, 1)),sSchName
			, sSheetName, sCompUID)

	def SelectNet(self, sSchName=defaultNamedNotOptArg, sSheetName=defaultNamedNotOptArg, sNetUID=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(267, LCID, 1, (11, 0), ((8, 1), (8, 1), (8, 1)),sSchName
			, sSheetName, sNetUID)

	def SelectPath(self, FileName=defaultNamedNotOptArg, HierPath=defaultNamedNotOptArg, SheetNumber=defaultNamedNotOptArg, Type=defaultNamedNotOptArg
			, AddSelected=defaultNamedNotOptArg, SearchBus=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(67, LCID, 1, (11, 0), ((8, 1), (8, 1), (8, 1), (3, 1), (11, 1), (11, 1)),FileName
			, HierPath, SheetNumber, Type, AddSelected, SearchBus
			)

	def SelectPathCompPin(self, FileName=defaultNamedNotOptArg, HierPath=defaultNamedNotOptArg, SheetNumber=defaultNamedNotOptArg, PinNumber=defaultNamedNotOptArg
			, SelectType=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(68, LCID, 1, (11, 0), ((8, 1), (8, 1), (8, 1), (8, 1), (3, 1)),FileName
			, HierPath, SheetNumber, PinNumber, SelectType)

	def SetButtonBitmap(self, CommandID=defaultNamedNotOptArg, BitmapFilePath=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(253, LCID, 1, (11, 0), ((19, 1), (8, 1)),CommandID
			, BitmapFilePath)

	def SetButtonResourceDLL(self, CommandID=defaultNamedNotOptArg, DllFilePath=defaultNamedNotOptArg, resID=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(254, LCID, 1, (11, 0), ((19, 1), (8, 1), (3, 1)),CommandID
			, DllFilePath, resID)

	def SetClientAdvisor(self, Advisor=defaultNamedNotOptArg, Flags=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(11, LCID, 1, (11, 0), ((9, 1), (3, 1)),Advisor
			, Flags)

	def SetConfigurationProperty(self, Name=defaultNamedNotOptArg, val=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(245, LCID, 1, (24, 0), ((8, 1), (9, 1)),Name
			, val)

	def SetDefaultColor(self, ObjectType=defaultNamedNotOptArg, Color=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(260, LCID, 1, (24, 0), ((3, 1), (9, 1)),ObjectType
			, Color)

	def SetEnvVariable(self, pName=defaultNamedNotOptArg, pValue=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(211, LCID, 1, (11, 0), ((8, 1), (8, 1)),pName
			, pValue)

	def SetGenericStatusIndicatorState(self, eIndicatorColor=defaultNamedNotOptArg, sToolTipText=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(277, LCID, 1, (11, 0), ((3, 1), (8, 1)),eIndicatorColor
			, sToolTipText)

	def SetLibAddComp(self, DirPath=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(49, LCID, 1, (11, 0), ((8, 1),),DirPath
			)

	def SetLibFileNew(self, DirPath=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(47, LCID, 1, (11, 0), ((8, 1),),DirPath
			)

	def SetLibFileOpen(self, DirPath=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(48, LCID, 1, (11, 0), ((8, 1),),DirPath
			)

	# The method SetObjectColor is actually a property, but must be used as a method to correctly pass the arguments
	def SetObjectColor(self, ObjectType=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(65, LCID, 4, (24, 0), ((3, 1), (3, 1)),ObjectType
			, arg1)

	def SetProdLib(self, dbcPath=defaultNamedNotOptArg, prodLibName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(311, LCID, 1, (11, 0), ((8, 1), (8, 1)),dbcPath
			, prodLibName)

	def SetRedraw(self, Redraw=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(222, LCID, 1, (24, 0), ((11, 1),),Redraw
			)

	def SetViewAnalogFlag(self, state=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(52, LCID, 1, (24, 0), ((11, 1),),state
			)

	def ShouldProvideDetailedComponentView(self, LibraryPath=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(318, LCID, 1, (11, 0), ((8, 1),),LibraryPath
			)

	def StartMigration(self, ProjectPath=defaultNamedNotOptArg, CentralLibPath=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(246, LCID, 1, (11, 0), ((8, 1), (8, 1)),ProjectPath
			, CentralLibPath)

	def StartVNSD(self):
		return self._oleobj_.InvokeTypes(301, LCID, 1, (24, 0), (),)

	def SupportsProdLibLimitation(self):
		return self._oleobj_.InvokeTypes(309, LCID, 1, (11, 0), (),)

	def TextViews(self):
		ret = self._oleobj_.InvokeTypes(57, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'TextViews', None)
		return ret

	def ToolbarAction(self, Handle=defaultNamedNotOptArg, Msg=defaultNamedNotOptArg, wParam=defaultNamedNotOptArg, lParam=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(262, LCID, 1, (3, 0), ((3, 1), (3, 1), (3, 1), (3, 1)),Handle
			, Msg, wParam, lParam)

	def UnloadClassDefinitions(self):
		return self._oleobj_.InvokeTypes(81, LCID, 1, (24, 0), (),)

	def UnregisterOLECommand(self, CommandName=defaultNamedNotOptArg, ClientDispatch=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(36, LCID, 1, (11, 0), ((8, 1), (9, 1)),CommandName
			, ClientDispatch)

	def UpdateMenuBar(self, menuBarParentWnd=defaultNamedNotOptArg, hMenu=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(282, LCID, 1, (3, 0), ((3, 1), (3, 1)),menuBarParentWnd
			, hMenu)

	def UserControl(self):
		return self._oleobj_.InvokeTypes(21, LCID, 1, (11, 0), (),)

	def Validate(self, _lLicenseToken=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(268, LCID, 1, (3, 0), ((3, 1),),_lLicenseToken
			)

	_prop_map_get_ = {
		"ActiveDocument": (208, 2, (9, 0), (), "ActiveDocument", None),
		# Method 'ActiveICTView' returns object of type 'IVdICTView'
		"ActiveICTView": (269, 2, (9, 0), (), "ActiveICTView", '{848E324F-125D-4236-981D-0EB202E628DA}'),
		# Method 'ActiveView' returns object of type 'IVdView'
		"ActiveView": (207, 2, (9, 0), (), "ActiveView", '{0892A013-86BC-11CE-8238-00001B4D36B5}'),
		"ActiveViewHandle": (40, 2, (3, 0), (), "ActiveViewHandle", None),
		"Addins": (216, 2, (9, 0), (), "Addins", None),
		# Method 'Application' returns object of type 'IVdApp'
		"Application": (3, 2, (9, 0), (), "Application", '{EA4ABD71-84B0-11CE-8237-00001B4D36B5}'),
		"BusyCursor": (61, 2, (3, 0), (), "BusyCursor", None),
		"ClientAdvisorFlags": (9, 2, (3, 0), (), "ClientAdvisorFlags", None),
		"CnsFileString": (102, 2, (8, 0), (), "CnsFileString", None),
		# Method 'CommandBars' returns object of type 'ICommandBars'
		"CommandBars": (215, 2, (9, 0), (), "CommandBars", '{91818215-A01E-11D2-8F30-0060B0EF0A25}'),
		"CommandLineArguments": (210, 2, (8, 0), (), "CommandLineArguments", None),
		"Cookies": (94, 2, (9, 0), (), "Cookies", None),
		"CurrentProject": (55, 2, (8, 0), (), "CurrentProject", None),
		# Method 'Documents' returns object of type 'IVdDocs'
		"Documents": (1, 2, (9, 0), (), "Documents", '{BD2EDF77-7E28-11CE-822D-00001B4D36B5}'),
		"EDXEngine": (281, 2, (9, 0), (), "EDXEngine", None),
		"Flows": (98, 2, (9, 0), (), "Flows", None),
		"FullName": (4, 2, (8, 0), (), "FullName", None),
		# Method 'HTMLDocuments' returns object of type 'IHTMLSourceDocuments'
		"HTMLDocuments": (213, 2, (9, 0), (), "HTMLDocuments", '{7D50CA6D-07DB-4BE0-AD95-563DED3F9157}'),
		"Interactive": (205, 2, (11, 0), (), "Interactive", None),
		"LicenseMode": (91, 2, (3, 0), (), "LicenseMode", None),
		"Name": (5, 2, (8, 0), (), "Name", None),
		"OptionLevel": (73, 2, (8, 0), (), "OptionLevel", None),
		# Method 'Parent' returns object of type 'IVdApp'
		"Parent": (6, 2, (9, 0), (), "Parent", '{EA4ABD71-84B0-11CE-8237-00001B4D36B5}'),
		"PrimaryDirectory": (56, 2, (8, 0), (), "PrimaryDirectory", None),
		"ProjMan": (88, 2, (9, 0), (), "ProjMan", None),
		"QueueSelectEvents": (224, 2, (3, 0), (), "QueueSelectEvents", None),
		"SheetsEditMode": (279, 2, (11, 0), (), "SheetsEditMode", None),
		"ShellCmd": (218, 2, (9, 0), (), "ShellCmd", None),
		"SilentMode": (250, 2, (3, 0), (), "SilentMode", None),
		# Method 'SourceDocuments' returns object of type 'IHDLSourceDocuments'
		"SourceDocuments": (214, 2, (9, 0), (), "SourceDocuments", '{AC6510A1-83C5-4486-9154-CE74592F9A48}'),
		"StatusBarText": (206, 2, (8, 0), (), "StatusBarText", None),
		"SynchronizesViewBase": (66, 2, (11, 0), (), "SynchronizesViewBase", None),
		"Version": (209, 2, (8, 0), (), "Version", None),
		"ViewBaseSession": (64, 2, (9, 0), (), "ViewBaseSession", None),
		"Visible": (204, 2, (11, 0), (), "Visible", None),
		"project": (101, 2, (9, 0), (), "project", None),
	}
	_prop_map_put_ = {
		"BusyCursor": ((61, LCID, 4, 0),()),
		"ClientAdvisorFlags": ((9, LCID, 4, 0),()),
		"CurrentProject": ((55, LCID, 4, 0),()),
		"Interactive": ((205, LCID, 4, 0),()),
		"QueueSelectEvents": ((224, LCID, 4, 0),()),
		"SheetsEditMode": ((279, LCID, 4, 0),()),
		"SilentMode": ((250, LCID, 4, 0),()),
		"StatusBarText": ((206, LCID, 4, 0),()),
		"SynchronizesViewBase": ((66, LCID, 4, 0),()),
		"Visible": ((204, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IVdApplicationAtTest(DispatchBaseClass):
	CLSID = IID('{341E1868-20BA-4B3C-8778-EBEEE6021C42}')
	coclass_clsid = IID('{8B370C04-6CF5-1014-9D62-FFC3EECCF0AC}')

	def DumpOutputWindow(self, TabName=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(11, LCID, 1, (8, 0), ((8, 1),),TabName
			)

	def ExtractReuseCircuits(self):
		return self._oleobj_.InvokeTypes(1, LCID, 1, (24, 0), (),)

	def GetProjectIntegrationStatus(self, taskName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(7, LCID, 1, (3, 0), ((8, 1),),taskName
			)

	def ImportEDXFileDownloadedFromPartQuestSite(self, EDXFilePath=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(12, LCID, 1, (11, 0), ((8, 1),),EDXFilePath
			)

	def ImportNetlistProject(self, ProjectPath=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(5, LCID, 1, (11, 0), ((8, 1),),ProjectPath
			)

	def PropagateFpgaSignalNames(self):
		return self._oleobj_.InvokeTypes(8, LCID, 1, (24, 0), (),)

	def PublishBlocks(self, names=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(10, LCID, 1, (11, 0), ((9, 1),),names
			)

	def ReplaceConnector(self, SourceConnector=defaultNamedNotOptArg, Scope=defaultNamedNotOptArg, DestinationConnector=defaultNamedNotOptArg, PinMapping=defaultNamedNotOptArg
			, PropertyMapping=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(2, LCID, 1, (11, 0), ((8, 1), (3, 1), (8, 1), (3, 1), (3, 1)),SourceConnector
			, Scope, DestinationConnector, PinMapping, PropertyMapping)

	def ReplaceSymbol(self, SourceSymbol=defaultNamedNotOptArg, Scope=defaultNamedNotOptArg, DestinationSymbol=defaultNamedNotOptArg, PinMapping=defaultNamedNotOptArg
			, PropertyMapping=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), ((8, 1), (3, 1), (8, 1), (3, 1), (3, 1)),SourceSymbol
			, Scope, DestinationSymbol, PinMapping, PropertyMapping)

	def RunProjectIntegrationTask(self, taskName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(6, LCID, 1, (24, 0), ((8, 1),),taskName
			)

	def RunSchematicTest(self, testName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((8, 1),),testName
			)

	def UpdateDRBs(self):
		return self._oleobj_.InvokeTypes(4, LCID, 1, (24, 0), (),)

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

class IVdArc(DispatchBaseClass):
	CLSID = IID('{AE729480-9683-11CE-8246-00001B4D36B5}')
	coclass_clsid = IID('{8B365D33-6CF5-1014-9D62-FFC3EECCF0AC}')

	# Result is of type IVdPoint
	def GetLocation(self, WhichPoint=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(6, LCID, 1, (9, 0), ((3, 1),),WhichPoint
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetLocation', '{AE729498-9683-11CE-8246-00001B4D36B5}')
		return ret

	# Result is of type IColor
	def GetObjectColor(self):
		ret = self._oleobj_.InvokeTypes(13, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjectColor', '{C1031A0C-15BD-4897-A3E5-4C615CDEA684}')
		return ret

	def IsColorAutomatic(self):
		return self._oleobj_.InvokeTypes(15, LCID, 1, (11, 0), (),)

	def SetAutomaticColor(self, bAutomatic=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(14, LCID, 1, (24, 0), ((11, 1),),bAutomatic
			)

	def SetLocation(self, X1=defaultNamedNotOptArg, Y1=defaultNamedNotOptArg, X2=defaultNamedNotOptArg, Y2=defaultNamedNotOptArg
			, X3=defaultNamedNotOptArg, Y3=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(7, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1)),X1
			, Y1, X2, Y2, X3, Y3
			)

	def SetObjectColor(self, newColor=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(12, LCID, 1, (24, 0), ((9, 1),),newColor
			)

	def _GetColor(self):
		return self._oleobj_.InvokeTypes(8, LCID, 1, (3, 0), (),)

	def _SetColor(self, newColor=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(9, LCID, 1, (24, 0), ((3, 1),),newColor
			)

	def _SetSelected(self, Flag=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(5, LCID, 1, (24, 0), ((11, 1),),Flag
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'IVdApp'
		"Application": (3, 2, (9, 0), (), "Application", '{EA4ABD71-84B0-11CE-8237-00001B4D36B5}'),
		"Color": (10, 2, (3, 0), (), "Color", None),
		"LineStyle": (2, 2, (3, 0), (), "LineStyle", None),
		# Method 'Parent' returns object of type 'IVdBlock'
		"Parent": (4, 2, (9, 0), (), "Parent", '{AE729484-9683-11CE-8246-00001B4D36B5}'),
		"Type": (1, 2, (3, 0), (), "Type", None),
	}
	_prop_map_put_ = {
		"Color": ((10, LCID, 4, 0),()),
		"LineStyle": ((2, LCID, 4, 0),()),
		"Selected": ((11, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IVdAttr(DispatchBaseClass):
	CLSID = IID('{AE729482-9683-11CE-8246-00001B4D36B5}')
	coclass_clsid = IID('{8B36723A-6CF5-1014-9D62-FFC3EECCF0AC}')

	def Delete(self):
		return self._oleobj_.InvokeTypes(27, LCID, 1, (24, 0), (),)

	def DeleteInstanceValue(self):
		return self._oleobj_.InvokeTypes(33, LCID, 1, (24, 0), (),)

	# Result is of type IVdPoint
	def GetLocation(self):
		ret = self._oleobj_.InvokeTypes(13, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetLocation', '{AE729498-9683-11CE-8246-00001B4D36B5}')
		return ret

	def GetOatFull(self, toplevel=defaultNamedNotOptArg, pathvalue=defaultNamedNotOptArg, full_or_not=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(26, LCID, 1, (8, 0), ((8, 1), (8, 1), (3, 1)),toplevel
			, pathvalue, full_or_not)

	# Result is of type IColor
	def GetObjectColor(self):
		ret = self._oleobj_.InvokeTypes(29, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjectColor', '{C1031A0C-15BD-4897-A3E5-4C615CDEA684}')
		return ret

	def IsColorAutomatic(self):
		return self._oleobj_.InvokeTypes(32, LCID, 1, (11, 0), (),)

	def SetAutomaticColor(self, bAutomatic=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(31, LCID, 1, (24, 0), ((11, 1),),bAutomatic
			)

	def SetLocation(self, X=defaultNamedNotOptArg, Y=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(14, LCID, 1, (24, 0), ((3, 1), (3, 1)),X
			, Y)

	def SetObjectColor(self, newColor=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(28, LCID, 1, (24, 0), ((9, 1),),newColor
			)

	def _GetColor(self):
		return self._oleobj_.InvokeTypes(15, LCID, 1, (3, 0), (),)

	def _GetEitherValue(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(18, LCID, 1, (8, 0), (),)

	def _GetOatValue(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(20, LCID, 1, (8, 0), (),)

	def _SetColor(self, newColor=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(16, LCID, 1, (24, 0), ((3, 1),),newColor
			)

	def _SetEitherValue(self, Value=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(17, LCID, 1, (24, 0), ((8, 1),),Value
			)

	def _SetOatValue(self, Value=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(19, LCID, 1, (24, 0), ((8, 1),),Value
			)

	def _SetSelected(self, Flag=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(12, LCID, 1, (24, 0), ((3, 1),),Flag
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'IVdApp'
		"Application": (10, 2, (9, 0), (), "Application", '{EA4ABD71-84B0-11CE-8237-00001B4D36B5}'),
		"Child": (21, 2, (9, 0), (), "Child", None),
		"Color": (22, 2, (3, 0), (), "Color", None),
		"EitherValue": (24, 2, (8, 0), (), "EitherValue", None),
		"Font": (6, 2, (3, 0), (), "Font", None),
		"InstanceValue": (30, 2, (8, 0), (), "InstanceValue", None),
		"Name": (3, 2, (8, 0), (), "Name", None),
		"OatValue": (25, 2, (8, 0), (), "OatValue", None),
		"Orientation": (8, 2, (3, 0), (), "Orientation", None),
		"Origin": (7, 2, (3, 0), (), "Origin", None),
		"Parent": (11, 2, (9, 0), (), "Parent", None),
		"Printable": (34, 2, (11, 0), (), "Printable", None),
		"Size": (9, 2, (3, 0), (), "Size", None),
		"TextString": (1, 2, (8, 0), (), "TextString", None),
		"Type": (5, 2, (3, 0), (), "Type", None),
		"Value": (2, 2, (8, 0), (), "Value", None),
		"Visible": (4, 2, (3, 0), (), "Visible", None),
	}
	_prop_map_put_ = {
		"Color": ((22, LCID, 4, 0),()),
		"EitherValue": ((24, LCID, 4, 0),()),
		"Font": ((6, LCID, 4, 0),()),
		"InstanceValue": ((30, LCID, 4, 0),()),
		"OatValue": ((25, LCID, 4, 0),()),
		"Orientation": ((8, LCID, 4, 0),()),
		"Origin": ((7, LCID, 4, 0),()),
		"Printable": ((34, LCID, 4, 0),()),
		"Selected": ((23, LCID, 4, 0),()),
		"Size": ((9, LCID, 4, 0),()),
		"TextString": ((1, LCID, 4, 0),()),
		"Value": ((2, LCID, 4, 0),()),
		"Visible": ((4, LCID, 4, 0),()),
	}
	# Default property for this class is 'Value'
	def __call__(self):
		return self._ApplyTypes_(*(2, 2, (8, 0), (), "Value", None))
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

class IVdBlock(DispatchBaseClass):
	CLSID = IID('{AE729484-9683-11CE-8246-00001B4D36B5}')
	coclass_clsid = IID('{8B367622-6CF5-1014-9D62-FFC3EECCF0AC}')

	# Result is of type IVdArc
	def AddArc(self, X1=defaultNamedNotOptArg, Y1=defaultNamedNotOptArg, X2=defaultNamedNotOptArg, Y2=defaultNamedNotOptArg
			, X3=defaultNamedNotOptArg, Y3=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(15, LCID, 1, (9, 0), ((3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1)),X1
			, Y1, X2, Y2, X3, Y3
			)
		if ret is not None:
			ret = Dispatch(ret, 'AddArc', '{AE729480-9683-11CE-8246-00001B4D36B5}')
		return ret

	# Result is of type IVdAttr
	def AddAttribute(self, String=defaultNamedNotOptArg, X=defaultNamedNotOptArg, Y=defaultNamedNotOptArg, Visibility=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(23, LCID, 1, (9, 0), ((8, 1), (3, 1), (3, 1), (3, 1)),String
			, X, Y, Visibility)
		if ret is not None:
			ret = Dispatch(ret, 'AddAttribute', '{AE729482-9683-11CE-8246-00001B4D36B5}')
		return ret

	def AddBatchAttributes(self, AttributeListString=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(28, LCID, 1, (11, 0), ((8, 1),),AttributeListString
			)

	# Result is of type IVdBox
	def AddBox(self, LowerLeftx=defaultNamedNotOptArg, LowerLefty=defaultNamedNotOptArg, UpperRightx=defaultNamedNotOptArg, UpperRighty=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(16, LCID, 1, (9, 0), ((3, 1), (3, 1), (3, 1), (3, 1)),LowerLeftx
			, LowerLefty, UpperRightx, UpperRighty)
		if ret is not None:
			ret = Dispatch(ret, 'AddBox', '{AE729486-9683-11CE-8246-00001B4D36B5}')
		return ret

	# Result is of type IVdCircle
	def AddCircle(self, Centerx=defaultNamedNotOptArg, Centery=defaultNamedNotOptArg, Radius=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(17, LCID, 1, (9, 0), ((3, 1), (3, 1), (3, 1)),Centerx
			, Centery, Radius)
		if ret is not None:
			ret = Dispatch(ret, 'AddCircle', '{AE729488-9683-11CE-8246-00001B4D36B5}')
		return ret

	# Result is of type IVdComp
	def AddComponent(self, SymbolName=defaultNamedNotOptArg, Locationx=defaultNamedNotOptArg, Locationy=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(18, LCID, 1, (9, 0), ((8, 1), (3, 1), (3, 1)),SymbolName
			, Locationx, Locationy)
		if ret is not None:
			ret = Dispatch(ret, 'AddComponent', '{AE72948A-9683-11CE-8246-00001B4D36B5}')
		return ret

	# Result is of type IVdComp
	def AddComponentMoveMode(self, SymbolName=defaultNamedNotOptArg, InitialLocationX=defaultNamedNotOptArg, InitialLocationY=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(25, LCID, 1, (9, 0), ((8, 1), (3, 1), (3, 1)),SymbolName
			, InitialLocationX, InitialLocationY)
		if ret is not None:
			ret = Dispatch(ret, 'AddComponentMoveMode', '{AE72948A-9683-11CE-8246-00001B4D36B5}')
		return ret

	# Result is of type IVdComp
	def AddComponentMoveModeEx(self, SymbolName=defaultNamedNotOptArg, InitialLocationX=defaultNamedNotOptArg, InitialLocationY=defaultNamedNotOptArg, bAddNets=defaultNamedNotOptArg
			, bLabelNets=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(51, LCID, 1, (9, 0), ((8, 1), (3, 1), (3, 1), (11, 1), (11, 1)),SymbolName
			, InitialLocationX, InitialLocationY, bAddNets, bLabelNets)
		if ret is not None:
			ret = Dispatch(ret, 'AddComponentMoveModeEx', '{AE72948A-9683-11CE-8246-00001B4D36B5}')
		return ret

	# Result is of type IVdComp
	def AddCompositeComponentMoveMode(self, SymbolPath=defaultNamedNotOptArg, ProjectFilePath=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(72, LCID, 1, (9, 0), ((8, 1), (8, 1)),SymbolPath
			, ProjectFilePath)
		if ret is not None:
			ret = Dispatch(ret, 'AddCompositeComponentMoveMode', '{AE72948A-9683-11CE-8246-00001B4D36B5}')
		return ret

	# Result is of type IVdFrameBoard
	def AddFrameBoard(self, LowerLeftx=defaultNamedNotOptArg, LowerLefty=defaultNamedNotOptArg, UpperRightx=defaultNamedNotOptArg, UpperRighty=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(75, LCID, 1, (9, 0), ((3, 1), (3, 1), (3, 1), (3, 1)),LowerLeftx
			, LowerLefty, UpperRightx, UpperRighty)
		if ret is not None:
			ret = Dispatch(ret, 'AddFrameBoard', '{EB52D85C-D244-4993-9FF6-5B3167ACDE01}')
		return ret

	# Result is of type IVdComp
	def AddFub(self, FubName=defaultNamedNotOptArg, LowerLeftx=defaultNamedNotOptArg, LowerLefty=defaultNamedNotOptArg, UpperRightx=defaultNamedNotOptArg
			, UpperRighty=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(19, LCID, 1, (9, 0), ((8, 1), (3, 1), (3, 1), (3, 1), (3, 1)),FubName
			, LowerLeftx, LowerLefty, UpperRightx, UpperRighty)
		if ret is not None:
			ret = Dispatch(ret, 'AddFub', '{AE72948A-9683-11CE-8246-00001B4D36B5}')
		return ret

	# Result is of type IVdLine
	def AddLine(self, Pt1=defaultNamedNotOptArg, Pt2=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(29, LCID, 1, (9, 0), ((3, 1), (3, 1)),Pt1
			, Pt2)
		if ret is not None:
			ret = Dispatch(ret, 'AddLine', '{AE729490-9683-11CE-8246-00001B4D36B5}')
		return ret

	# Result is of type IVdLine
	def AddLine2(self, X1=defaultNamedNotOptArg, Y1=defaultNamedNotOptArg, X2=defaultNamedNotOptArg, Y2=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(70, LCID, 1, (9, 0), ((3, 1), (3, 1), (3, 1), (3, 1)),X1
			, Y1, X2, Y2)
		if ret is not None:
			ret = Dispatch(ret, 'AddLine2', '{AE729490-9683-11CE-8246-00001B4D36B5}')
		return ret

	# Result is of type IVdNet
	def AddNet(self, Locationx1=defaultNamedNotOptArg, Locationy1=defaultNamedNotOptArg, Locationx2=defaultNamedNotOptArg, Locationy2=defaultNamedNotOptArg
			, CompPin1=defaultNamedNotOptArg, CompPin2=defaultNamedNotOptArg, BusOrWire=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(20, LCID, 1, (9, 0), ((3, 1), (3, 1), (3, 1), (3, 1), (9, 1), (9, 1), (3, 1)),Locationx1
			, Locationy1, Locationx2, Locationy2, CompPin1, CompPin2
			, BusOrWire)
		if ret is not None:
			ret = Dispatch(ret, 'AddNet', '{AE729492-9683-11CE-8246-00001B4D36B5}')
		return ret

	# Result is of type IVdNet
	def AddNetEx(self, Locationx1=defaultNamedNotOptArg, Locationy1=defaultNamedNotOptArg, Locationx2=defaultNamedNotOptArg, Locationy2=defaultNamedNotOptArg
			, CompPin1=defaultNamedNotOptArg, CompPin2=defaultNamedNotOptArg, BusOrWire=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(77, LCID, 1, (9, 0), ((3, 1), (3, 1), (3, 1), (3, 1), (9, 1), (9, 1), (3, 1)),Locationx1
			, Locationy1, Locationx2, Locationy2, CompPin1, CompPin2
			, BusOrWire)
		if ret is not None:
			ret = Dispatch(ret, 'AddNetEx', '{AE729492-9683-11CE-8246-00001B4D36B5}')
		return ret

	# Result is of type IVdComp
	def AddPartInstance(self, PartPartitionName=defaultNamedNotOptArg, DeviceName=defaultNamedNotOptArg, SymbolName=defaultNamedNotOptArg, Locationx=defaultNamedNotOptArg
			, Locationy=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(59, LCID, 1, (9, 0), ((8, 1), (8, 1), (8, 1), (3, 1), (3, 1)),PartPartitionName
			, DeviceName, SymbolName, Locationx, Locationy)
		if ret is not None:
			ret = Dispatch(ret, 'AddPartInstance', '{AE72948A-9683-11CE-8246-00001B4D36B5}')
		return ret

	# Result is of type IVdPin
	def AddPin(self, X=defaultNamedNotOptArg, Y=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(21, LCID, 1, (9, 0), ((3, 1), (3, 1)),X
			, Y)
		if ret is not None:
			ret = Dispatch(ret, 'AddPin', '{AE729496-9683-11CE-8246-00001B4D36B5}')
		return ret

	# Result is of type IVdPin
	def AddPinAtLocation(self, X1=defaultNamedNotOptArg, Y1=defaultNamedNotOptArg, X2=defaultNamedNotOptArg, Y2=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(57, LCID, 1, (9, 0), ((3, 1), (3, 1), (3, 1), (3, 1)),X1
			, Y1, X2, Y2)
		if ret is not None:
			ret = Dispatch(ret, 'AddPinAtLocation', '{AE729496-9683-11CE-8246-00001B4D36B5}')
		return ret

	# Result is of type IVdComp
	def AddReuseBlockInstance(self, ReuseType=defaultNamedNotOptArg, RBSymbolName=defaultNamedNotOptArg, ModifierType=defaultNamedNotOptArg, ModifierValue=defaultNamedNotOptArg
			, bAddNets=defaultNamedNotOptArg, bLabelNets=defaultNamedNotOptArg, Locationx=defaultNamedNotOptArg, Locationy=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(63, LCID, 1, (9, 0), ((3, 1), (8, 1), (3, 1), (8, 1), (11, 1), (11, 1), (3, 1), (3, 1)),ReuseType
			, RBSymbolName, ModifierType, ModifierValue, bAddNets, bLabelNets
			, Locationx, Locationy)
		if ret is not None:
			ret = Dispatch(ret, 'AddReuseBlockInstance', '{AE72948A-9683-11CE-8246-00001B4D36B5}')
		return ret

	# Result is of type IVdComp
	def AddReuseBlockInstanceEx(self, ReuseType=defaultNamedNotOptArg, RBSymbolName=defaultNamedNotOptArg, pMergeData=defaultNamedNotOptArg, ModifierType=defaultNamedNotOptArg
			, ModifierValue=defaultNamedNotOptArg, bAddNets=defaultNamedNotOptArg, bLabelNets=defaultNamedNotOptArg, Locationx=defaultNamedNotOptArg, Locationy=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(64, LCID, 1, (9, 0), ((3, 1), (8, 1), (9, 1), (3, 1), (8, 1), (11, 1), (11, 1), (3, 1), (3, 1)),ReuseType
			, RBSymbolName, pMergeData, ModifierType, ModifierValue, bAddNets
			, bLabelNets, Locationx, Locationy)
		if ret is not None:
			ret = Dispatch(ret, 'AddReuseBlockInstanceEx', '{AE72948A-9683-11CE-8246-00001B4D36B5}')
		return ret

	# Result is of type IVdComp
	def AddSymbolInstance(self, SymbolPartitionName=defaultNamedNotOptArg, SymbolName=defaultNamedNotOptArg, Locationx=defaultNamedNotOptArg, Locationy=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(58, LCID, 1, (9, 0), ((8, 1), (8, 1), (3, 1), (3, 1)),SymbolPartitionName
			, SymbolName, Locationx, Locationy)
		if ret is not None:
			ret = Dispatch(ret, 'AddSymbolInstance', '{AE72948A-9683-11CE-8246-00001B4D36B5}')
		return ret

	# Result is of type IVdText
	def AddText(self, TextString=defaultNamedNotOptArg, X=defaultNamedNotOptArg, Y=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(22, LCID, 1, (9, 0), ((8, 1), (3, 1), (3, 1)),TextString
			, X, Y)
		if ret is not None:
			ret = Dispatch(ret, 'AddText', '{AE72949C-9683-11CE-8246-00001B4D36B5}')
		return ret

	def ApplySymbolUpdate(self, SelectedOnly=defaultNamedNotOptArg, Slot=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(34, LCID, 1, (24, 0), ((3, 1), (3, 1)),SelectedOnly
			, Slot)

	def ArraySelected(self, nRows=defaultNamedNotOptArg, nColumns=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(76, LCID, 1, (24, 0), ((3, 1), (3, 1)),nRows
			, nColumns)

	def ChangeBorder(self, NewBorder=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(40, LCID, 1, (24, 0), ((8, 1),),NewBorder
			)

	def ChangeComponent(self, OldComp=defaultNamedNotOptArg, NewComp=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(24, LCID, 1, (11, 0), ((8, 1), (8, 1)),OldComp
			, NewComp)

	def ChangeComponentPreserveRefdes(self, OldComp=defaultNamedNotOptArg, NewComp=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(42, LCID, 1, (11, 0), ((8, 1), (8, 1)),OldComp
			, NewComp)

	def CheckIfWirUpToDateWithCDB(self):
		return self._oleobj_.InvokeTypes(55, LCID, 1, (11, 0), (),)

	def ClearHighlight(self, SelectedOnly=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(37, LCID, 1, (24, 0), ((3, 1),),SelectedOnly
			)

	def DeSelectAll(self):
		return self._oleobj_.InvokeTypes(14, LCID, 1, (24, 0), (),)

	def DeleteAttribute(self, ObjectName=defaultNamedNotOptArg, ObjectType=defaultNamedNotOptArg, AttributeName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(48, LCID, 1, (11, 0), ((8, 1), (3, 1), (8, 1)),ObjectName
			, ObjectType, AttributeName)

	def DeleteBorder(self):
		return self._oleobj_.InvokeTypes(39, LCID, 1, (24, 0), (),)

	def DeletePackagedAttribute(self, ObjectName=defaultNamedNotOptArg, ObjectType=defaultNamedNotOptArg, AttributeName=defaultNamedNotOptArg, SyncCms=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(45, LCID, 1, (11, 0), ((8, 1), (3, 1), (8, 1), (11, 1)),ObjectName
			, ObjectType, AttributeName, SyncCms)

	def DeleteSelected(self, delUnc=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(26, LCID, 1, (24, 0), ((11, 1),),delUnc
			)

	def DisableUpdateStoring(self):
		return self._oleobj_.InvokeTypes(67, LCID, 1, (24, 0), (),)

	def DissolveReuseBlock(self, PartitionName=defaultNamedNotOptArg, SymbolName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(78, LCID, 1, (24, 0), ((8, 1), (8, 1)),PartitionName
			, SymbolName)

	def EnableUpdateStoring(self):
		return self._oleobj_.InvokeTypes(68, LCID, 1, (24, 0), (),)

	def EndUndoTransaction(self):
		return self._oleobj_.InvokeTypes(53, LCID, 1, (24, 0), (),)

	# Result is of type IVdAttr
	def FindAttribute(self, AttributeName=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(30, LCID, 1, (9, 0), ((8, 1),),AttributeName
			)
		if ret is not None:
			ret = Dispatch(ret, 'FindAttribute', '{AE729482-9683-11CE-8246-00001B4D36B5}')
		return ret

	def GetAttributeValues(self, ObjectName=defaultNamedNotOptArg, ObjectType=defaultNamedNotOptArg, AttributeNameList=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(46, LCID, 1, (8, 0), ((8, 1), (3, 1), (8, 1)),ObjectName
			, ObjectType, AttributeNameList)

	def GetBatchAttributes(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(27, LCID, 1, (8, 0), (),)

	# Result is of type IVdPoint
	def GetBboxPoint(self, Location=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(12, LCID, 1, (9, 0), ((3, 1),),Location
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetBboxPoint', '{AE729498-9683-11CE-8246-00001B4D36B5}')
		return ret

	# Result is of type IVdBlock
	def GetChildBlock(self):
		ret = self._oleobj_.InvokeTypes(60, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetChildBlock', '{AE729484-9683-11CE-8246-00001B4D36B5}')
		return ret

	def GetForwardPCB(self):
		return self._oleobj_.InvokeTypes(73, LCID, 1, (11, 0), (),)

	def GetName(self, Flag=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(11, LCID, 1, (8, 0), ((3, 1),),Flag
			)

	def GetPackagedAttributeValues(self, ObjectName=defaultNamedNotOptArg, ObjectType=defaultNamedNotOptArg, AttributeNameList=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(43, LCID, 1, (8, 0), ((8, 1), (3, 1), (8, 1)),ObjectName
			, ObjectType, AttributeNameList)

	def GetPackagedName(self, GraphicalName=defaultNamedNotOptArg, ObjectType=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(49, LCID, 1, (8, 0), ((8, 1), (3, 1)),GraphicalName
			, ObjectType)

	# Result is of type IMergeData
	def GetReuseBlockMergeData(self, ReuseType=defaultNamedNotOptArg, RBSymbolName=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(65, LCID, 1, (9, 0), ((3, 1), (8, 1)),ReuseType
			, RBSymbolName)
		if ret is not None:
			ret = Dispatch(ret, 'GetReuseBlockMergeData', '{4584E756-C172-4389-AD41-AEE82CB45759}')
		return ret

	def InsertBorder(self):
		return self._oleobj_.InvokeTypes(38, LCID, 1, (24, 0), (),)

	def IsReadOnly(self):
		return self._oleobj_.InvokeTypes(66, LCID, 1, (11, 0), (),)

	def IsValid(self):
		return self._oleobj_.InvokeTypes(62, LCID, 1, (11, 0), (),)

	def MoveSelected(self, dx=defaultNamedNotOptArg, dy=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(71, LCID, 1, (24, 0), ((3, 1), (3, 1)),dx
			, dy)

	def PromoteSymbolNumbers(self, SelectedOnly=defaultNamedNotOptArg, Slot=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(35, LCID, 1, (24, 0), ((3, 1), (3, 1)),SelectedOnly
			, Slot)

	def RepositionAttributesAsOnSymbol(self, SelectedOnly=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(36, LCID, 1, (24, 0), ((3, 1),),SelectedOnly
			)

	def SetAttributeValue(self, ObjectName=defaultNamedNotOptArg, ObjectType=defaultNamedNotOptArg, AttributeName=defaultNamedNotOptArg, AttributeValue=defaultNamedNotOptArg
			, IsOat=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(47, LCID, 1, (11, 0), ((8, 1), (3, 1), (8, 1), (8, 1), (11, 1)),ObjectName
			, ObjectType, AttributeName, AttributeValue, IsOat)

	def SetBoundingBox(self, OriginX=defaultNamedNotOptArg, OriginY=defaultNamedNotOptArg, Width=defaultNamedNotOptArg, Height=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(56, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1), (3, 1)),OriginX
			, OriginY, Width, Height)

	def SetPackagedAttributeValue(self, ObjectName=defaultNamedNotOptArg, ObjectType=defaultNamedNotOptArg, AttributeName=defaultNamedNotOptArg, AttributeValue=defaultNamedNotOptArg
			, IsOat=defaultNamedNotOptArg, SyncCms=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(44, LCID, 1, (11, 0), ((8, 1), (3, 1), (8, 1), (8, 1), (11, 1), (11, 1)),ObjectName
			, ObjectType, AttributeName, AttributeValue, IsOat, SyncCms
			)

	def SetZSheetSize(self, Width=defaultNamedNotOptArg, Height=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(13, LCID, 1, (24, 0), ((3, 1), (3, 1)),Width
			, Height)

	def StartUndoTransaction(self):
		return self._oleobj_.InvokeTypes(52, LCID, 1, (24, 0), (),)

	def UpdateBorder(self):
		return self._oleobj_.InvokeTypes(41, LCID, 1, (24, 0), (),)

	def UpdateOutline(self):
		return self._oleobj_.InvokeTypes(74, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'IVdApp'
		"Application": (3, 2, (9, 0), (), "Application", '{EA4ABD71-84B0-11CE-8237-00001B4D36B5}'),
		# Method 'Attributes' returns object of type 'IVdObjs'
		"Attributes": (1, 2, (9, 0), (), "Attributes", '{BD2EDF77-7E28-11CE-822D-00001B4D36B7}'),
		"ConstraintObjectDefinitions": (50, 2, (9, 0), (), "ConstraintObjectDefinitions", None),
		"DataType": (5, 2, (3, 0), (), "DataType", None),
		"DisplayType": (69, 2, (3, 0), (), "DisplayType", None),
		"IsBorderSymbol": (61, 2, (11, 0), (), "IsBorderSymbol", None),
		"IsFub": (54, 2, (11, 0), (), "IsFub", None),
		"LibraryName": (6, 2, (8, 0), (), "LibraryName", None),
		"LibraryType": (33, 2, (3, 0), (), "LibraryType", None),
		"OpenMode": (8, 2, (3, 0), (), "OpenMode", None),
		# Method 'Parent' returns object of type 'IVdView'
		"Parent": (4, 2, (9, 0), (), "Parent", '{0892A013-86BC-11CE-8238-00001B4D36B5}'),
		"Path": (31, 2, (8, 0), (), "Path", None),
		"SheetNum": (10, 2, (8, 0), (), "SheetNum", None),
		"SheetSize": (9, 2, (3, 0), (), "SheetSize", None),
		"SymbolType": (7, 2, (3, 0), (), "SymbolType", None),
		"Type": (2, 2, (3, 0), (), "Type", None),
		# Method 'UserData' returns object of type 'IStruct'
		"UserData": (32, 2, (9, 0), (), "UserData", '{33C2B049-DADF-11D2-882A-0060B0EF0A25}'),
	}
	_prop_map_put_ = {
		"DisplayType": ((69, LCID, 4, 0),()),
		"SheetSize": ((9, LCID, 4, 0),()),
		"SymbolType": ((7, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IVdBox(DispatchBaseClass):
	CLSID = IID('{AE729486-9683-11CE-8246-00001B4D36B5}')
	coclass_clsid = IID('{8B368EF8-6CF5-1014-9D62-FFC3EECCF0AC}')

	def GetDropShadow(self):
		return self._oleobj_.InvokeTypes(27, LCID, 1, (11, 0), (),)

	def GetGradientType(self):
		return self._oleobj_.InvokeTypes(21, LCID, 1, (3, 0), (),)

	# Result is of type IVdPoint
	def GetLocation(self, Flag=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(8, LCID, 1, (9, 0), ((3, 1),),Flag
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetLocation', '{AE729498-9683-11CE-8246-00001B4D36B5}')
		return ret

	# Result is of type IColor
	def GetObjectColor(self):
		ret = self._oleobj_.InvokeTypes(14, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjectColor', '{C1031A0C-15BD-4897-A3E5-4C615CDEA684}')
		return ret

	# Result is of type IColor
	def GetObjectFillColor(self):
		ret = self._oleobj_.InvokeTypes(18, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjectFillColor', '{C1031A0C-15BD-4897-A3E5-4C615CDEA684}')
		return ret

	# Result is of type IColor
	def GetObjectGradientPrimaryColor(self):
		ret = self._oleobj_.InvokeTypes(23, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjectGradientPrimaryColor', '{C1031A0C-15BD-4897-A3E5-4C615CDEA684}')
		return ret

	# Result is of type IColor
	def GetObjectGradientSecondaryColor(self):
		ret = self._oleobj_.InvokeTypes(25, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjectGradientSecondaryColor', '{C1031A0C-15BD-4897-A3E5-4C615CDEA684}')
		return ret

	def GetShadowOpacity(self):
		return self._oleobj_.InvokeTypes(29, LCID, 1, (3, 0), (),)

	def IsColorAutomatic(self):
		return self._oleobj_.InvokeTypes(16, LCID, 1, (11, 0), (),)

	def IsFillColorAutomatic(self):
		return self._oleobj_.InvokeTypes(20, LCID, 1, (11, 0), (),)

	def SetAutomaticColor(self, bAutomatic=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(15, LCID, 1, (24, 0), ((11, 1),),bAutomatic
			)

	def SetAutomaticFillColor(self, bAutomatic=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(19, LCID, 1, (24, 0), ((11, 1),),bAutomatic
			)

	def SetDropShadow(self, bDropShadow=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(28, LCID, 1, (24, 0), ((11, 1),),bDropShadow
			)

	def SetGradientType(self, newType=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(22, LCID, 1, (24, 0), ((3, 1),),newType
			)

	def SetLocation(self, X1=defaultNamedNotOptArg, Y1=defaultNamedNotOptArg, X2=defaultNamedNotOptArg, Y2=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(7, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1), (3, 1)),X1
			, Y1, X2, Y2)

	def SetObjectColor(self, newColor=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(13, LCID, 1, (24, 0), ((9, 1),),newColor
			)

	def SetObjectFillColor(self, newColor=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(17, LCID, 1, (24, 0), ((9, 1),),newColor
			)

	def SetObjectGradientPrimaryColor(self, newColor=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(24, LCID, 1, (24, 0), ((9, 1),),newColor
			)

	def SetObjectGradientSecondaryColor(self, newColor=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(26, LCID, 1, (24, 0), ((9, 1),),newColor
			)

	def SetShadowOpacity(self, newOpacity=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(30, LCID, 1, (24, 0), ((3, 1),),newOpacity
			)

	def _GetColor(self):
		return self._oleobj_.InvokeTypes(9, LCID, 1, (3, 0), (),)

	def _SetColor(self, newColor=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(10, LCID, 1, (24, 0), ((3, 1),),newColor
			)

	def _SetSelected(self, Flag=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(6, LCID, 1, (24, 0), ((3, 1),),Flag
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'IVdApp'
		"Application": (4, 2, (9, 0), (), "Application", '{EA4ABD71-84B0-11CE-8237-00001B4D36B5}'),
		"Color": (11, 2, (3, 0), (), "Color", None),
		"FillStyle": (2, 2, (3, 0), (), "FillStyle", None),
		"LineStyle": (3, 2, (3, 0), (), "LineStyle", None),
		# Method 'Parent' returns object of type 'IVdBlock'
		"Parent": (5, 2, (9, 0), (), "Parent", '{AE729484-9683-11CE-8246-00001B4D36B5}'),
		"Type": (1, 2, (3, 0), (), "Type", None),
	}
	_prop_map_put_ = {
		"Color": ((11, LCID, 4, 0),()),
		"FillStyle": ((2, LCID, 4, 0),()),
		"LineStyle": ((3, LCID, 4, 0),()),
		"Selected": ((12, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IVdCircle(DispatchBaseClass):
	CLSID = IID('{AE729488-9683-11CE-8246-00001B4D36B5}')
	coclass_clsid = IID('{8B36932D-6CF5-1014-9D62-FFC3EECCF0AC}')

	# Result is of type IVdPoint
	def GetCenter(self):
		ret = self._oleobj_.InvokeTypes(8, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetCenter', '{AE729498-9683-11CE-8246-00001B4D36B5}')
		return ret

	# Result is of type IColor
	def GetObjectColor(self):
		ret = self._oleobj_.InvokeTypes(15, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjectColor', '{C1031A0C-15BD-4897-A3E5-4C615CDEA684}')
		return ret

	# Result is of type IColor
	def GetObjectFillColor(self):
		ret = self._oleobj_.InvokeTypes(19, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjectFillColor', '{C1031A0C-15BD-4897-A3E5-4C615CDEA684}')
		return ret

	def IsColorAutomatic(self):
		return self._oleobj_.InvokeTypes(17, LCID, 1, (11, 0), (),)

	def IsFillColorAutomatic(self):
		return self._oleobj_.InvokeTypes(21, LCID, 1, (11, 0), (),)

	def SetAutomaticColor(self, bAutomatic=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(16, LCID, 1, (24, 0), ((11, 1),),bAutomatic
			)

	def SetAutomaticFillColor(self, bAutomatic=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(20, LCID, 1, (24, 0), ((11, 1),),bAutomatic
			)

	def SetCenter(self, X=defaultNamedNotOptArg, Y=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(9, LCID, 1, (24, 0), ((3, 1), (3, 1)),X
			, Y)

	def SetObjectColor(self, newColor=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(14, LCID, 1, (24, 0), ((9, 1),),newColor
			)

	def SetObjectFillColor(self, newColor=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(18, LCID, 1, (24, 0), ((9, 1),),newColor
			)

	def _GetColor(self):
		return self._oleobj_.InvokeTypes(11, LCID, 1, (3, 0), (),)

	def _SetColor(self, newColor=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(10, LCID, 1, (24, 0), ((3, 1),),newColor
			)

	def _SetSelected(self, Flag=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(7, LCID, 1, (24, 0), ((3, 1),),Flag
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'IVdApp'
		"Application": (4, 2, (9, 0), (), "Application", '{EA4ABD71-84B0-11CE-8237-00001B4D36B5}'),
		"Color": (12, 2, (3, 0), (), "Color", None),
		"FillStyle": (2, 2, (3, 0), (), "FillStyle", None),
		"LineStyle": (3, 2, (3, 0), (), "LineStyle", None),
		# Method 'Parent' returns object of type 'IVdBlock'
		"Parent": (5, 2, (9, 0), (), "Parent", '{AE729484-9683-11CE-8246-00001B4D36B5}'),
		"Radius": (6, 2, (3, 0), (), "Radius", None),
		"Type": (1, 2, (3, 0), (), "Type", None),
	}
	_prop_map_put_ = {
		"Color": ((12, LCID, 4, 0),()),
		"FillStyle": ((2, LCID, 4, 0),()),
		"LineStyle": ((3, LCID, 4, 0),()),
		"Radius": ((6, LCID, 4, 0),()),
		"Selected": ((13, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IVdCmpPin(DispatchBaseClass):
	CLSID = IID('{AE72948C-9683-11CE-8246-00001B4D36B5}')
	coclass_clsid = IID('{8B369E7F-6CF5-1014-9D62-FFC3EECCF0AC}')

	# Result is of type IVdAttr
	def AddAttribute(self, String=defaultNamedNotOptArg, X=defaultNamedNotOptArg, Y=defaultNamedNotOptArg, Visibility=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(9, LCID, 1, (9, 0), ((8, 1), (3, 1), (3, 1), (3, 1)),String
			, X, Y, Visibility)
		if ret is not None:
			ret = Dispatch(ret, 'AddAttribute', '{AE729482-9683-11CE-8246-00001B4D36B5}')
		return ret

	# Result is of type IVdAttr
	def AddOat(self, String=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(10, LCID, 1, (9, 0), ((8, 1),),String
			)
		if ret is not None:
			ret = Dispatch(ret, 'AddOat', '{AE729482-9683-11CE-8246-00001B4D36B5}')
		return ret

	# Result is of type IVdAttr
	def FindAttribute(self, AttributeName=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(13, LCID, 1, (9, 0), ((8, 1),),AttributeName
			)
		if ret is not None:
			ret = Dispatch(ret, 'FindAttribute', '{AE729482-9683-11CE-8246-00001B4D36B5}')
		return ret

	# Result is of type IVdPoint
	def GetLocation(self):
		ret = self._oleobj_.InvokeTypes(8, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetLocation', '{AE729498-9683-11CE-8246-00001B4D36B5}')
		return ret

	# Result is of type IVdComp
	def _GetComp(self):
		ret = self._oleobj_.InvokeTypes(12, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, '_GetComp', '{AE72948A-9683-11CE-8246-00001B4D36B5}')
		return ret

	# Result is of type IVdPin
	def _GetPin(self):
		ret = self._oleobj_.InvokeTypes(11, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, '_GetPin', '{AE729496-9683-11CE-8246-00001B4D36B5}')
		return ret

	def _SetSelected(self, Flag=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(7, LCID, 1, (24, 0), ((3, 1),),Flag
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'IVdApp'
		"Application": (3, 2, (9, 0), (), "Application", '{EA4ABD71-84B0-11CE-8237-00001B4D36B5}'),
		# Method 'Attributes' returns object of type 'IVdObjs'
		"Attributes": (1, 2, (9, 0), (), "Attributes", '{BD2EDF77-7E28-11CE-822D-00001B4D36B7}'),
		# Method 'Component' returns object of type 'IVdComp'
		"Component": (15, 2, (9, 0), (), "Component", '{AE72948A-9683-11CE-8246-00001B4D36B5}'),
		# Method 'Connection' returns object of type 'IVdConnection'
		"Connection": (17, 2, (9, 0), (), "Connection", '{1446F3C0-2169-11D0-91A7-7A9695000000}'),
		"Number": (5, 2, (8, 0), (), "Number", None),
		# Method 'Parent' returns object of type 'IVdComp'
		"Parent": (4, 2, (9, 0), (), "Parent", '{AE72948A-9683-11CE-8246-00001B4D36B5}'),
		# Method 'Pin' returns object of type 'IVdPin'
		"Pin": (16, 2, (9, 0), (), "Pin", '{AE729496-9683-11CE-8246-00001B4D36B5}'),
		"Side": (6, 2, (3, 0), (), "Side", None),
		"Type": (2, 2, (3, 0), (), "Type", None),
	}
	_prop_map_put_ = {
		"Number": ((5, LCID, 4, 0),()),
		"Selected": ((14, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IVdComp(DispatchBaseClass):
	CLSID = IID('{AE72948A-9683-11CE-8246-00001B4D36B5}')
	coclass_clsid = IID('{8B36976A-6CF5-1014-9D62-FFC3EECCF0AC}')

	def ActivateMoveMode(self):
		return self._oleobj_.InvokeTypes(27, LCID, 1, (11, 0), (),)

	# Result is of type IVdAttr
	def AddAttribute(self, String=defaultNamedNotOptArg, X=defaultNamedNotOptArg, Y=defaultNamedNotOptArg, Visibility=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(17, LCID, 1, (9, 0), ((8, 1), (3, 1), (3, 1), (3, 1)),String
			, X, Y, Visibility)
		if ret is not None:
			ret = Dispatch(ret, 'AddAttribute', '{AE729482-9683-11CE-8246-00001B4D36B5}')
		return ret

	def AddBatchAttributes(self, AttributeListSting=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(20, LCID, 1, (11, 0), ((8, 1),),AttributeListSting
			)

	def AddBatchOats(self, AttributeListSting=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(24, LCID, 1, (11, 0), ((8, 1),),AttributeListSting
			)

	# Result is of type IVdLabel
	def AddLabel(self, String=defaultNamedNotOptArg, X=defaultNamedNotOptArg, Y=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(18, LCID, 1, (9, 0), ((8, 1), (3, 1), (3, 1)),String
			, X, Y)
		if ret is not None:
			ret = Dispatch(ret, 'AddLabel', '{AE72948E-9683-11CE-8246-00001B4D36B5}')
		return ret

	# Result is of type IVdAttr
	def AddOat(self, String=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(19, LCID, 1, (9, 0), ((8, 1),),String
			)
		if ret is not None:
			ret = Dispatch(ret, 'AddOat', '{AE729482-9683-11CE-8246-00001B4D36B5}')
		return ret

	def ExtractSchematic(self):
		return self._oleobj_.InvokeTypes(30, LCID, 1, (24, 0), (),)

	# Result is of type IVdAttr
	def FindAttribute(self, AttributeString=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(23, LCID, 1, (9, 0), ((8, 1),),AttributeString
			)
		if ret is not None:
			ret = Dispatch(ret, 'FindAttribute', '{AE729482-9683-11CE-8246-00001B4D36B5}')
		return ret

	def GetBatchAttributes(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(21, LCID, 1, (8, 0), (),)

	def GetBatchOats(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(25, LCID, 1, (8, 0), (),)

	# Result is of type IVdPoint
	def GetBboxPoint(self, Location=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(16, LCID, 1, (9, 0), ((3, 1),),Location
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetBboxPoint', '{AE729498-9683-11CE-8246-00001B4D36B5}')
		return ret

	# Result is of type IVdObjs
	def GetConnections(self):
		ret = self._oleobj_.InvokeTypes(22, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetConnections', '{BD2EDF77-7E28-11CE-822D-00001B4D36B7}')
		return ret

	def GetForwardPCB(self):
		return self._oleobj_.InvokeTypes(28, LCID, 1, (3, 0), (),)

	# Result is of type IVdPoint
	def GetLocation(self):
		ret = self._oleobj_.InvokeTypes(13, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetLocation', '{AE729498-9683-11CE-8246-00001B4D36B5}')
		return ret

	def GetName(self, Flag=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(15, LCID, 1, (8, 0), ((3, 1),),Flag
			)

	def SetForwardPCB(self, forwardPCBValue=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(29, LCID, 1, (24, 0), ((3, 1),),forwardPCBValue
			)

	def SetLocation(self, X=defaultNamedNotOptArg, Y=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(14, LCID, 1, (24, 0), ((3, 1), (3, 1)),X
			, Y)

	def _SetSelected(self, Flag=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(12, LCID, 1, (24, 0), ((3, 1),),Flag
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'IVdApp'
		"Application": (9, 2, (9, 0), (), "Application", '{EA4ABD71-84B0-11CE-8237-00001B4D36B5}'),
		# Method 'Attributes' returns object of type 'IVdObjs'
		"Attributes": (1, 2, (9, 0), (), "Attributes", '{BD2EDF77-7E28-11CE-822D-00001B4D36B7}'),
		"Id": (6, 2, (3, 0), (), "Id", None),
		# Method 'Label' returns object of type 'IVdLabel'
		"Label": (2, 2, (9, 0), (), "Label", '{AE72948E-9683-11CE-8246-00001B4D36B5}'),
		"Orientation": (4, 2, (3, 0), (), "Orientation", None),
		# Method 'Parent' returns object of type 'IVdBlock'
		"Parent": (10, 2, (9, 0), (), "Parent", '{AE729484-9683-11CE-8246-00001B4D36B5}'),
		"Refdes": (8, 2, (8, 0), (), "Refdes", None),
		"Scale": (7, 2, (5, 0), (), "Scale", None),
		# Method 'SymbolBlock' returns object of type 'IVdBlock'
		"SymbolBlock": (11, 2, (9, 0), (), "SymbolBlock", '{AE729484-9683-11CE-8246-00001B4D36B5}'),
		"Type": (3, 2, (3, 0), (), "Type", None),
		"UID": (5, 2, (8, 0), (), "UID", None),
	}
	_prop_map_put_ = {
		"Orientation": ((4, LCID, 4, 0),()),
		"Refdes": ((8, LCID, 4, 0),()),
		"Scale": ((7, LCID, 4, 0),()),
		"Selected": ((26, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IVdConnection(DispatchBaseClass):
	CLSID = IID('{1446F3C0-2169-11D0-91A7-7A9695000000}')
	coclass_clsid = IID('{8B36BB3F-6CF5-1014-9D62-FFC3EECCF0AC}')

	# Result is of type IVdCmpPin
	def _GetCompPin(self):
		ret = self._oleobj_.InvokeTypes(1, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, '_GetCompPin', '{AE72948C-9683-11CE-8246-00001B4D36B5}')
		return ret

	# Result is of type IVdNet
	def _GetNet(self):
		ret = self._oleobj_.InvokeTypes(2, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, '_GetNet', '{AE729492-9683-11CE-8246-00001B4D36B5}')
		return ret

	# Result is of type IVdSegment
	def _GetSegment(self):
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, '_GetSegment', '{AE72949A-9683-11CE-8246-00001B4D36B5}')
		return ret

	_prop_map_get_ = {
		# Method 'CompPin' returns object of type 'IVdCmpPin'
		"CompPin": (4, 2, (9, 0), (), "CompPin", '{AE72948C-9683-11CE-8246-00001B4D36B5}'),
		# Method 'Net' returns object of type 'IVdNet'
		"Net": (5, 2, (9, 0), (), "Net", '{AE729492-9683-11CE-8246-00001B4D36B5}'),
		# Method 'Ripper' returns object of type 'IRipper'
		"Ripper": (7, 2, (9, 0), (), "Ripper", '{FE3DB4AE-6C5C-426D-93A7-1308F624DDD9}'),
		# Method 'Segment' returns object of type 'IVdSegment'
		"Segment": (6, 2, (9, 0), (), "Segment", '{AE72949A-9683-11CE-8246-00001B4D36B5}'),
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

class IVdDoc(DispatchBaseClass):
	CLSID = IID('{4ADEF4E2-690A-11CE-9261-0020C5E26659}')
	coclass_clsid = IID('{8B3660B9-6CF5-1014-9D62-FFC3EECCF0AC}')

	def Activate(self):
		return self._oleobj_.InvokeTypes(8, LCID, 1, (24, 0), (),)

	def CancelSave(self, DoNotWarn=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(21, LCID, 1, (24, 0), ((11, 1),),DoNotWarn
			)

	def Close(self, SaveChanges=defaultNamedNotOptArg, FileName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(9, LCID, 1, (24, 0), ((11, 1), (8, 1)),SaveChanges
			, FileName)

	# Result is of type IMGCDesignerDataManagementEntity
	def DataManagementEntity(self):
		ret = self._oleobj_.InvokeTypes(24, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'DataManagementEntity', '{03BE5928-2002-4CCB-818D-775ED6115A41}')
		return ret

	def DiscardSymbolChanges(self):
		return self._oleobj_.InvokeTypes(23, LCID, 1, (24, 0), (),)

	def ExportMetafile(self, OutputName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(18, LCID, 1, (24, 0), ((8, 1),),OutputName
			)

	# Result is of type IVdViews
	def GetViews(self):
		ret = self._oleobj_.InvokeTypes(14, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetViews', '{DC3A8AF0-91B4-11CE-8243-00001B4D36B5}')
		return ret

	def IsAccess(self, AccessType=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(19, LCID, 1, (11, 0), ((3, 1),),AccessType
			)

	def Open(self, FileName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(16, LCID, 1, (11, 0), ((8, 1),),FileName
			)

	def Print(self, From=defaultNamedNotOptArg, To=defaultNamedNotOptArg, Copies=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(10, LCID, 1, (24, 0), ((2, 1), (2, 1), (2, 1)),From
			, To, Copies)

	def PrintOut(self, From=defaultNamedNotOptArg, To=defaultNamedNotOptArg, Copies=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(11, LCID, 1, (24, 0), ((2, 1), (2, 1), (2, 1)),From
			, To, Copies)

	def ReRead(self, SheetNumber=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(15, LCID, 1, (11, 0), ((8, 1),),SheetNumber
			)

	def Save(self):
		return self._oleobj_.InvokeTypes(12, LCID, 1, (24, 0), (),)

	def SaveAndCheck(self):
		return self._oleobj_.InvokeTypes(17, LCID, 1, (24, 0), (),)

	def SaveAs(self, FileName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(13, LCID, 1, (24, 0), ((8, 1),),FileName
			)

	def UpdateSymbolInDesign(self):
		return self._oleobj_.InvokeTypes(22, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'IVdApp'
		"Application": (1, 2, (9, 0), (), "Application", '{EA4ABD71-84B0-11CE-8237-00001B4D36B5}'),
		"DataType": (20, 2, (3, 0), (), "DataType", None),
		"FullName": (3, 2, (8, 0), (), "FullName", None),
		"Name": (4, 2, (8, 0), (), "Name", None),
		# Method 'Parent' returns object of type 'IVdDocs'
		"Parent": (5, 2, (9, 0), (), "Parent", '{BD2EDF77-7E28-11CE-822D-00001B4D36B5}'),
		"Path": (6, 2, (8, 0), (), "Path", None),
		"Saved": (7, 2, (11, 0), (), "Saved", None),
		"Visible": (2, 2, (11, 0), (), "Visible", None),
	}
	_prop_map_put_ = {
		"Visible": ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IVdDocs(DispatchBaseClass):
	CLSID = IID('{BD2EDF77-7E28-11CE-822D-00001B4D36B5}')
	coclass_clsid = IID('{8B36663A-6CF5-1014-9D62-FFC3EECCF0AC}')

	# Result is of type IVdDoc
	def Add(self):
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{4ADEF4E2-690A-11CE-9261-0020C5E26659}')
		return ret

	def Close(self):
		return self._oleobj_.InvokeTypes(6, LCID, 1, (24, 0), (),)

	# Result is of type IVdDoc
	def Item(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{4ADEF4E2-690A-11CE-9261-0020C5E26659}')
		return ret

	# Result is of type IVdDoc
	def Open(self, FileName=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(7, LCID, 1, (9, 0), ((8, 1),),FileName
			)
		if ret is not None:
			ret = Dispatch(ret, 'Open', '{4ADEF4E2-690A-11CE-9261-0020C5E26659}')
		return ret

	def SaveAll(self):
		return self._oleobj_.InvokeTypes(10, LCID, 1, (24, 0), (),)

	def SelectPath(self, FileName=defaultNamedNotOptArg, HierPath=defaultNamedNotOptArg, SheetNumber=defaultNamedNotOptArg, Type=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(8, LCID, 1, (3, 0), ((8, 1), (8, 1), (8, 1), (3, 1)),FileName
			, HierPath, SheetNumber, Type)

	def SelectPathCompPin(self, FileName=defaultNamedNotOptArg, HierPath=defaultNamedNotOptArg, SheetNumber=defaultNamedNotOptArg, PinNumber=defaultNamedNotOptArg
			, SelectType=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((8, 1), (8, 1), (8, 1), (8, 1), (3, 1)),FileName
			, HierPath, SheetNumber, PinNumber, SelectType)

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'IVdApp'
		"Application": (2, 2, (9, 0), (), "Application", '{EA4ABD71-84B0-11CE-8237-00001B4D36B5}'),
		"Count": (1, 2, (3, 0), (), "Count", None),
		# Method 'Parent' returns object of type 'IVdApp'
		"Parent": (3, 2, (9, 0), (), "Parent", '{EA4ABD71-84B0-11CE-8237-00001B4D36B5}'),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{4ADEF4E2-690A-11CE-9261-0020C5E26659}')
	#This class has Item property/method which allows indexed access with the object[key] syntax.
	#Some objects will accept a string or other type of key in addition to integers.
	#Note that many Office objects do not use zero-based indexing.
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(4, LCID, 1, 1, key)), "Item", '{4ADEF4E2-690A-11CE-9261-0020C5E26659}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IVdFrameBoard(DispatchBaseClass):
	CLSID = IID('{EB52D85C-D244-4993-9FF6-5B3167ACDE01}')
	coclass_clsid = IID('{8B36CE74-6CF5-1014-9D62-FFC3EECCF0AC}')

	def GetFrameBoardName(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(12, LCID, 1, (8, 0), (),)

	# Result is of type IVdPoint
	def GetLocation(self, Flag=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(10, LCID, 1, (9, 0), ((3, 1),),Flag
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetLocation', '{AE729498-9683-11CE-8246-00001B4D36B5}')
		return ret

	def IsClone(self):
		return self._oleobj_.InvokeTypes(13, LCID, 1, (11, 0), (),)

	def SetFrameBoardName(self, NewName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(11, LCID, 1, (24, 0), ((8, 1),),NewName
			)

	def SetLocation(self, X1=defaultNamedNotOptArg, Y1=defaultNamedNotOptArg, X2=defaultNamedNotOptArg, Y2=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(9, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1), (3, 1)),X1
			, Y1, X2, Y2)

	def _SetSelected(self, Flag=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(8, LCID, 1, (24, 0), ((11, 1),),Flag
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'IVdApp'
		"Application": (5, 2, (9, 0), (), "Application", '{EA4ABD71-84B0-11CE-8237-00001B4D36B5}'),
		# Method 'Attributes' returns object of type 'IVdObjs'
		"Attributes": (1, 2, (9, 0), (), "Attributes", '{BD2EDF77-7E28-11CE-822D-00001B4D36B7}'),
		"Id": (4, 2, (3, 0), (), "Id", None),
		# Method 'Parent' returns object of type 'IVdBlock'
		"Parent": (6, 2, (9, 0), (), "Parent", '{AE729484-9683-11CE-8246-00001B4D36B5}'),
		"Type": (2, 2, (3, 0), (), "Type", None),
		"UID": (3, 2, (8, 0), (), "UID", None),
	}
	_prop_map_put_ = {
		"Selected": ((7, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IVdHighPrecisionObject(DispatchBaseClass):
	CLSID = IID('{B3EC8244-3A42-4E18-9667-2A54BC66EABF}')
	coclass_clsid = IID('{8B37081F-6CF5-1014-9D62-FFC3EECCF0AC}')

	def GetSegmentX(self, WhichJoint=defaultNamedNotOptArg, _unit=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(8, LCID, 1, (5, 0), ((3, 1), (3, 1)),WhichJoint
			, _unit)

	def GetSegmentY(self, WhichJoint=defaultNamedNotOptArg, _unit=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(9, LCID, 1, (5, 0), ((3, 1), (3, 1)),WhichJoint
			, _unit)

	def GetSize(self, _unit=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(6, LCID, 1, (5, 0), ((3, 1),),_unit
			)

	def GetX(self, _unit=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(2, LCID, 1, (5, 0), ((3, 1),),_unit
			)

	def GetY(self, _unit=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(3, LCID, 1, (5, 0), ((3, 1),),_unit
			)

	def SetObject(self, pObject=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1, LCID, 1, (24, 0), ((9, 1),),pObject
			)

	def SetSegmentX(self, WhichJoint=defaultNamedNotOptArg, _unit=defaultNamedNotOptArg, retval=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(10, LCID, 1, (24, 0), ((3, 1), (3, 1), (5, 1)),WhichJoint
			, _unit, retval)

	def SetSegmentY(self, WhichJoint=defaultNamedNotOptArg, _unit=defaultNamedNotOptArg, retval=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(11, LCID, 1, (24, 0), ((3, 1), (3, 1), (5, 1)),WhichJoint
			, _unit, retval)

	def SetSize(self, _unit=defaultNamedNotOptArg, retval=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(7, LCID, 1, (24, 0), ((3, 1), (5, 1)),_unit
			, retval)

	def SetX(self, _unit=defaultNamedNotOptArg, retval=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(4, LCID, 1, (24, 0), ((3, 1), (5, 1)),_unit
			, retval)

	def SetY(self, _unit=defaultNamedNotOptArg, retval=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(5, LCID, 1, (24, 0), ((3, 1), (5, 1)),_unit
			, retval)

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

class IVdICTAttr(DispatchBaseClass):
	CLSID = IID('{F7EC3A7D-851C-4C1D-ABAF-FBDB3C38D29B}')
	coclass_clsid = IID('{8B367F7F-6CF5-1014-9D62-FFC3EECCF0AC}')

	_prop_map_get_ = {
		"Parent": (100, 2, (9, 0), (), "Parent", None),
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

class IVdICTBlock(DispatchBaseClass):
	CLSID = IID('{C64B5D5C-66D5-41FE-B4B3-EFC664EAED1B}')
	coclass_clsid = IID('{8B3681F1-6CF5-1014-9D62-FFC3EECCF0AC}')

	# Result is of type IVdICTComp
	def AddInstance(self, PartitionName=defaultNamedNotOptArg, SymbolName=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(101, LCID, 1, (9, 0), ((8, 1), (8, 1)),PartitionName
			, SymbolName)
		if ret is not None:
			ret = Dispatch(ret, 'AddInstance', '{4945AC27-6ADD-462C-B3F6-239842AFFEB9}')
		return ret

	# Result is of type IVdICTNet
	def AddNet(self, Name=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(102, LCID, 1, (9, 0), ((8, 1),),Name
			)
		if ret is not None:
			ret = Dispatch(ret, 'AddNet', '{9ED04F47-52F4-476A-8100-B8990AFE3ACD}')
		return ret

	def ConnectObjects(self, _MIDL__IVdICTBlock0001_=defaultNamedNotOptArg, _MIDL__IVdICTBlock0002_=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(107, LCID, 1, (11, 0), ((9, 1), (9, 1)),_MIDL__IVdICTBlock0001_
			, _MIDL__IVdICTBlock0002_)

	def DisconnectObjects(self, _MIDL__IVdICTBlock0003_=defaultNamedNotOptArg, _MIDL__IVdICTBlock0004_=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(108, LCID, 1, (11, 0), ((9, 1), (9, 1)),_MIDL__IVdICTBlock0003_
			, _MIDL__IVdICTBlock0004_)

	# Result is of type IVdObjs
	def GetInstances(self):
		ret = self._oleobj_.InvokeTypes(105, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetInstances', '{BD2EDF77-7E28-11CE-822D-00001B4D36B7}')
		return ret

	def GetName(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(2, LCID, 1, (8, 0), (),)

	# Result is of type IVdObjs
	def GetNets(self):
		ret = self._oleobj_.InvokeTypes(104, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetNets', '{BD2EDF77-7E28-11CE-822D-00001B4D36B7}')
		return ret

	def GetUID(self):
		return self._oleobj_.InvokeTypes(3, LCID, 1, (3, 0), (),)

	def PromoteSymbolNumbers(self, SelectedOnly=defaultNamedNotOptArg, Slot=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(103, LCID, 1, (24, 0), ((3, 1), (3, 1)),SelectedOnly
			, Slot)

	def RemoveObject(self, _MIDL__IVdICTBlock0000_=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(106, LCID, 1, (11, 0), ((9, 1),),_MIDL__IVdICTBlock0000_
			)

	def SetObjectName(self, Name=defaultNamedNotOptArg, _MIDL__IVdICTBlock0005_=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(109, LCID, 1, (11, 0), ((8, 1), (9, 1)),Name
			, _MIDL__IVdICTBlock0005_)

	_prop_map_get_ = {
		# Method 'Parent' returns object of type 'IVdICTView'
		"Parent": (100, 2, (9, 0), (), "Parent", '{848E324F-125D-4236-981D-0EB202E628DA}'),
		# Method 'ParentObject' returns object of type 'IVdICTObj'
		"ParentObject": (1, 2, (9, 0), (), "ParentObject", '{F692CCBA-DA51-43FB-B8D6-79EEA84B59CA}'),
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

class IVdICTComp(DispatchBaseClass):
	CLSID = IID('{4945AC27-6ADD-462C-B3F6-239842AFFEB9}')
	coclass_clsid = IID('{8B36843C-6CF5-1014-9D62-FFC3EECCF0AC}')

	def GetAttributeValue(self, AttrType=defaultNamedNotOptArg, Name=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(102, LCID, 1, (8, 0), ((3, 1), (8, 1)),AttrType
			, Name)

	# Result is of type IStringList
	def GetAttributesNames(self, AttrType=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(101, LCID, 1, (9, 0), ((3, 1),),AttrType
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetAttributesNames', '{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')
		return ret

	def GetDefName(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(105, LCID, 1, (8, 0), (),)

	def GetLibraryName(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(106, LCID, 1, (8, 0), (),)

	def GetName(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(2, LCID, 1, (8, 0), (),)

	# Result is of type IVdObjs
	def GetPins(self):
		ret = self._oleobj_.InvokeTypes(108, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetPins', '{BD2EDF77-7E28-11CE-822D-00001B4D36B7}')
		return ret

	def GetUID(self):
		return self._oleobj_.InvokeTypes(3, LCID, 1, (3, 0), (),)

	def RemAttributeValue(self, AttrType=defaultNamedNotOptArg, Name=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(104, LCID, 1, (11, 0), ((3, 1), (8, 1)),AttrType
			, Name)

	def SetAttributeValue(self, AttrType=defaultNamedNotOptArg, Name=defaultNamedNotOptArg, Value=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(103, LCID, 1, (11, 0), ((3, 1), (8, 1), (8, 1)),AttrType
			, Name, Value)

	_prop_map_get_ = {
		# Method 'Parent' returns object of type 'IVdICTBlock'
		"Parent": (100, 2, (9, 0), (), "Parent", '{C64B5D5C-66D5-41FE-B4B3-EFC664EAED1B}'),
		# Method 'ParentObject' returns object of type 'IVdICTObj'
		"ParentObject": (1, 2, (9, 0), (), "ParentObject", '{F692CCBA-DA51-43FB-B8D6-79EEA84B59CA}'),
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

class IVdICTDocument(DispatchBaseClass):
	CLSID = IID('{E947B7EF-5E39-42FD-A351-400BFEFCF49D}')
	coclass_clsid = IID('{8B3662D5-6CF5-1014-9D62-FFC3EECCF0AC}')

	def Activate(self):
		return self._oleobj_.InvokeTypes(105, LCID, 1, (24, 0), (),)

	def Close(self, SaveChanges=defaultNamedNotOptArg, FileName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(106, LCID, 1, (24, 0), ((11, 1), (8, 1)),SaveChanges
			, FileName)

	# Result is of type IVdICTViews
	def GetViews(self):
		ret = self._oleobj_.InvokeTypes(108, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetViews', '{EA874DB4-9B4D-4E7F-BE4F-D41AD4A560DE}')
		return ret

	def IsReadOnly(self):
		return self._oleobj_.InvokeTypes(116, LCID, 1, (11, 0), (),)

	def Print(self, From=defaultNamedNotOptArg, To=defaultNamedNotOptArg, Copies=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(107, LCID, 1, (24, 0), ((2, 1), (2, 1), (2, 1)),From
			, To, Copies)

	def SetReadOnly(self, ReadOnlyFlag=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(117, LCID, 1, (24, 0), ((11, 1),),ReadOnlyFlag
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'IVdApp'
		"Application": (101, 2, (9, 0), (), "Application", '{EA4ABD71-84B0-11CE-8237-00001B4D36B5}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Name": (102, 2, (8, 0), (), "Name", None),
		# Method 'Parent' returns object of type 'IICTDocuments'
		"Parent": (104, 2, (9, 0), (), "Parent", '{2A3CCA57-9C38-4484-A6A3-7521DDF7DAD0}'),
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

class IVdICTNet(DispatchBaseClass):
	CLSID = IID('{9ED04F47-52F4-476A-8100-B8990AFE3ACD}')
	coclass_clsid = IID('{8B368664-6CF5-1014-9D62-FFC3EECCF0AC}')

	def GetName(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(2, LCID, 1, (8, 0), (),)

	# Result is of type IVdObjs
	def GetPins(self):
		ret = self._oleobj_.InvokeTypes(101, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetPins', '{BD2EDF77-7E28-11CE-822D-00001B4D36B7}')
		return ret

	def GetUID(self):
		return self._oleobj_.InvokeTypes(3, LCID, 1, (3, 0), (),)

	_prop_map_get_ = {
		# Method 'Parent' returns object of type 'IVdICTBlock'
		"Parent": (100, 2, (9, 0), (), "Parent", '{C64B5D5C-66D5-41FE-B4B3-EFC664EAED1B}'),
		# Method 'ParentObject' returns object of type 'IVdICTObj'
		"ParentObject": (1, 2, (9, 0), (), "ParentObject", '{F692CCBA-DA51-43FB-B8D6-79EEA84B59CA}'),
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

class IVdICTObj(DispatchBaseClass):
	CLSID = IID('{F692CCBA-DA51-43FB-B8D6-79EEA84B59CA}')
	coclass_clsid = IID('{8B368AA4-6CF5-1014-9D62-FFC3EECCF0AC}')

	def GetName(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(2, LCID, 1, (8, 0), (),)

	def GetUID(self):
		return self._oleobj_.InvokeTypes(3, LCID, 1, (3, 0), (),)

	_prop_map_get_ = {
		# Method 'ParentObject' returns object of type 'IVdICTObj'
		"ParentObject": (1, 2, (9, 0), (), "ParentObject", '{F692CCBA-DA51-43FB-B8D6-79EEA84B59CA}'),
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

class IVdICTPin(DispatchBaseClass):
	CLSID = IID('{2645E45F-3981-4BA3-ADE4-EFB2AD5A1CCB}')
	coclass_clsid = IID('{8B368887-6CF5-1014-9D62-FFC3EECCF0AC}')

	def GetName(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(2, LCID, 1, (8, 0), (),)

	# Result is of type IVdObjs
	def GetNets(self):
		ret = self._oleobj_.InvokeTypes(101, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetNets', '{BD2EDF77-7E28-11CE-822D-00001B4D36B7}')
		return ret

	def GetUID(self):
		return self._oleobj_.InvokeTypes(3, LCID, 1, (3, 0), (),)

	_prop_map_get_ = {
		# Method 'Parent' returns object of type 'IVdICTComp'
		"Parent": (100, 2, (9, 0), (), "Parent", '{4945AC27-6ADD-462C-B3F6-239842AFFEB9}'),
		# Method 'ParentObject' returns object of type 'IVdICTObj'
		"ParentObject": (1, 2, (9, 0), (), "ParentObject", '{F692CCBA-DA51-43FB-B8D6-79EEA84B59CA}'),
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

class IVdICTView(DispatchBaseClass):
	CLSID = IID('{848E324F-125D-4236-981D-0EB202E628DA}')
	coclass_clsid = IID('{8B36267B-6CF5-1014-9D62-FFC3EECCF0AC}')

	def AddReuseBlock(self, partName=defaultNamedNotOptArg, SymbolName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(108, LCID, 1, (11, 0), ((8, 1), (8, 1)),partName
			, SymbolName)

	def GetName(self, Flag=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(105, LCID, 1, (8, 0), ((3, 1),),Flag
			)

	def GetTopLevelDesignName(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(104, LCID, 1, (8, 0), (),)

	# Result is of type IVdObjs
	def Query(self, Flags=defaultNamedNotOptArg, Selected=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(107, LCID, 1, (9, 0), ((3, 1), (3, 1)),Flags
			, Selected)
		if ret is not None:
			ret = Dispatch(ret, 'Query', '{BD2EDF77-7E28-11CE-822D-00001B4D36B7}')
		return ret

	def SelectByName(self, Name=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(106, LCID, 1, (11, 0), ((8, 1),),Name
			)

	def SetSignalsView(self):
		return self._oleobj_.InvokeTypes(102, LCID, 1, (24, 0), (),)

	def SetSymbolsView(self):
		return self._oleobj_.InvokeTypes(103, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Block' returns object of type 'IVdICTBlock'
		"Block": (100, 2, (9, 0), (), "Block", '{C64B5D5C-66D5-41FE-B4B3-EFC664EAED1B}'),
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

class IVdICTViews(DispatchBaseClass):
	CLSID = IID('{EA874DB4-9B4D-4E7F-BE4F-D41AD4A560DE}')
	coclass_clsid = IID('{8B366ED1-6CF5-1014-9D62-FFC3EECCF0AC}')

	# Result is of type IVdICTView
	def Item(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{848E324F-125D-4236-981D-0EB202E628DA}')
		return ret

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'IVdApp'
		"Application": (2, 2, (9, 0), (), "Application", '{EA4ABD71-84B0-11CE-8237-00001B4D36B5}'),
		"Count": (1, 2, (3, 0), (), "Count", None),
		# Method 'Parent' returns object of type 'IVdDoc'
		"Parent": (3, 2, (9, 0), (), "Parent", '{4ADEF4E2-690A-11CE-9261-0020C5E26659}'),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{848E324F-125D-4236-981D-0EB202E628DA}')
	#This class has Item property/method which allows indexed access with the object[key] syntax.
	#Some objects will accept a string or other type of key in addition to integers.
	#Note that many Office objects do not use zero-based indexing.
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(4, LCID, 1, 1, key)), "Item", '{848E324F-125D-4236-981D-0EB202E628DA}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IVdLabel(DispatchBaseClass):
	CLSID = IID('{AE72948E-9683-11CE-8246-00001B4D36B5}')
	coclass_clsid = IID('{8B36A221-6CF5-1014-9D62-FFC3EECCF0AC}')

	# Result is of type IVdPoint
	def GetLocation(self):
		ret = self._oleobj_.InvokeTypes(13, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetLocation', '{AE729498-9683-11CE-8246-00001B4D36B5}')
		return ret

	# Result is of type IColor
	def GetObjectColor(self):
		ret = self._oleobj_.InvokeTypes(21, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjectColor', '{C1031A0C-15BD-4897-A3E5-4C615CDEA684}')
		return ret

	def IsColorAutomatic(self):
		return self._oleobj_.InvokeTypes(23, LCID, 1, (11, 0), (),)

	def SetAutomaticColor(self, bAutomatic=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(22, LCID, 1, (24, 0), ((11, 1),),bAutomatic
			)

	def SetLocation(self, X=defaultNamedNotOptArg, Y=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(14, LCID, 1, (24, 0), ((3, 1), (3, 1)),X
			, Y)

	def SetObjectColor(self, newColor=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(20, LCID, 1, (24, 0), ((9, 1),),newColor
			)

	def _GetColor(self):
		return self._oleobj_.InvokeTypes(15, LCID, 1, (3, 0), (),)

	def _SetColor(self, newColor=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(16, LCID, 1, (24, 0), ((3, 1),),newColor
			)

	def _SetSelected(self, Flag=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(12, LCID, 1, (24, 0), ((3, 1),),Flag
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'IVdApp'
		"Application": (9, 2, (9, 0), (), "Application", '{EA4ABD71-84B0-11CE-8237-00001B4D36B5}'),
		"Color": (17, 2, (3, 0), (), "Color", None),
		"Font": (4, 2, (3, 0), (), "Font", None),
		"Orientation": (6, 2, (3, 0), (), "Orientation", None),
		"Origin": (5, 2, (3, 0), (), "Origin", None),
		"Parent": (10, 2, (9, 0), (), "Parent", None),
		"Printable": (24, 2, (11, 0), (), "Printable", None),
		"ResolvedName": (19, 2, (8, 0), (), "ResolvedName", None),
		"Scope": (11, 2, (3, 0), (), "Scope", None),
		"Sense": (8, 2, (3, 0), (), "Sense", None),
		"Size": (7, 2, (3, 0), (), "Size", None),
		"TextString": (1, 2, (8, 0), (), "TextString", None),
		"Type": (3, 2, (3, 0), (), "Type", None),
		"Visible": (2, 2, (3, 0), (), "Visible", None),
	}
	_prop_map_put_ = {
		"Color": ((17, LCID, 4, 0),()),
		"Font": ((4, LCID, 4, 0),()),
		"Orientation": ((6, LCID, 4, 0),()),
		"Origin": ((5, LCID, 4, 0),()),
		"Printable": ((24, LCID, 4, 0),()),
		"Scope": ((11, LCID, 4, 0),()),
		"Selected": ((18, LCID, 4, 0),()),
		"Sense": ((8, LCID, 4, 0),()),
		"Size": ((7, LCID, 4, 0),()),
		"TextString": ((1, LCID, 4, 0),()),
		"Visible": ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IVdLibrary(DispatchBaseClass):
	CLSID = IID('{28D40DF1-22F3-11D0-91AB-58F3E7000000}')
	coclass_clsid = IID('{8B36BEBC-6CF5-1014-9D62-FFC3EECCF0AC}')

	_prop_map_get_ = {
		"Alias": (2, 2, (8, 0), (), "Alias", None),
		"Path": (1, 2, (8, 0), (), "Path", None),
		"Type": (3, 2, (3, 0), (), "Type", None),
	}
	_prop_map_put_ = {
		"Alias": ((2, LCID, 4, 0),()),
		"Path": ((1, LCID, 4, 0),()),
		"Type": ((3, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IVdLine(DispatchBaseClass):
	CLSID = IID('{AE729490-9683-11CE-8246-00001B4D36B5}')
	coclass_clsid = IID('{8B36A61A-6CF5-1014-9D62-FFC3EECCF0AC}')

	def AddPoint(self, NewPoint=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(10, LCID, 1, (11, 0), ((3, 1),),NewPoint
			)

	def GetNumPoints(self):
		return self._oleobj_.InvokeTypes(9, LCID, 1, (3, 0), (),)

	# Result is of type IColor
	def GetObjectColor(self):
		ret = self._oleobj_.InvokeTypes(15, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjectColor', '{C1031A0C-15BD-4897-A3E5-4C615CDEA684}')
		return ret

	# Result is of type IColor
	def GetObjectFillColor(self):
		ret = self._oleobj_.InvokeTypes(19, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjectFillColor', '{C1031A0C-15BD-4897-A3E5-4C615CDEA684}')
		return ret

	# Result is of type IVdPoint
	def GetPoint(self, PointNumber=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(11, LCID, 1, (9, 0), ((3, 1),),PointNumber
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetPoint', '{AE729498-9683-11CE-8246-00001B4D36B5}')
		return ret

	def IsColorAutomatic(self):
		return self._oleobj_.InvokeTypes(17, LCID, 1, (11, 0), (),)

	def IsFillColorAutomatic(self):
		return self._oleobj_.InvokeTypes(21, LCID, 1, (11, 0), (),)

	def SetAutomaticColor(self, bAutomatic=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(16, LCID, 1, (24, 0), ((11, 1),),bAutomatic
			)

	def SetAutomaticFillColor(self, bAutomatic=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(20, LCID, 1, (24, 0), ((11, 1),),bAutomatic
			)

	def SetObjectColor(self, newColor=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(14, LCID, 1, (24, 0), ((9, 1),),newColor
			)

	def SetObjectFillColor(self, newColor=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(18, LCID, 1, (24, 0), ((9, 1),),newColor
			)

	def _GetColor(self):
		return self._oleobj_.InvokeTypes(7, LCID, 1, (3, 0), (),)

	def _SetColor(self, newColor=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(8, LCID, 1, (2, 0), ((3, 1),),newColor
			)

	def _SetSelected(self, Flag=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(6, LCID, 1, (24, 0), ((3, 1),),Flag
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'IVdApp'
		"Application": (5, 2, (9, 0), (), "Application", '{EA4ABD71-84B0-11CE-8237-00001B4D36B5}'),
		"Color": (12, 2, (3, 0), (), "Color", None),
		"FillStyle": (2, 2, (3, 0), (), "FillStyle", None),
		"LineStyle": (3, 2, (3, 0), (), "LineStyle", None),
		# Method 'Parent' returns object of type 'IVdBlock'
		"Parent": (4, 2, (9, 0), (), "Parent", '{AE729484-9683-11CE-8246-00001B4D36B5}'),
		"Type": (1, 2, (3, 0), (), "Type", None),
	}
	_prop_map_put_ = {
		"Color": ((12, LCID, 4, 0),()),
		"FillStyle": ((2, LCID, 4, 0),()),
		"LineStyle": ((3, LCID, 4, 0),()),
		"Selected": ((13, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IVdNet(DispatchBaseClass):
	CLSID = IID('{AE729492-9683-11CE-8246-00001B4D36B5}')
	coclass_clsid = IID('{8B36A986-6CF5-1014-9D62-FFC3EECCF0AC}')

	# Result is of type IVdAttr
	def AddAttribute(self, Segment=defaultNamedNotOptArg, String=defaultNamedNotOptArg, X=defaultNamedNotOptArg, Y=defaultNamedNotOptArg
			, Visibility=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(11, LCID, 1, (9, 0), ((9, 1), (8, 1), (3, 1), (3, 1), (3, 1)),Segment
			, String, X, Y, Visibility)
		if ret is not None:
			ret = Dispatch(ret, 'AddAttribute', '{AE729482-9683-11CE-8246-00001B4D36B5}')
		return ret

	# Result is of type IVdLabel
	def AddLabel(self, Segment=defaultNamedNotOptArg, String=defaultNamedNotOptArg, X=defaultNamedNotOptArg, Y=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(12, LCID, 1, (9, 0), ((9, 1), (8, 1), (3, 1), (3, 1)),Segment
			, String, X, Y)
		if ret is not None:
			ret = Dispatch(ret, 'AddLabel', '{AE72948E-9683-11CE-8246-00001B4D36B5}')
		return ret

	# Result is of type IVdAttr
	def AddOat(self, String=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(10, LCID, 1, (9, 0), ((8, 1),),String
			)
		if ret is not None:
			ret = Dispatch(ret, 'AddOat', '{AE729482-9683-11CE-8246-00001B4D36B5}')
		return ret

	# Result is of type IVdObjs
	def Connections(self, PinNameFilter=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(23, LCID, 1, (9, 0), ((12, 17),),PinNameFilter
			)
		if ret is not None:
			ret = Dispatch(ret, 'Connections', '{BD2EDF77-7E28-11CE-822D-00001B4D36B7}')
		return ret

	# Result is of type IVdAttr
	def FindAttribute(self, AttributeName=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(17, LCID, 1, (9, 0), ((8, 1),),AttributeName
			)
		if ret is not None:
			ret = Dispatch(ret, 'FindAttribute', '{AE729482-9683-11CE-8246-00001B4D36B5}')
		return ret

	# Result is of type IVdLabel
	def GetConnectedLabel(self, Segment=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(24, LCID, 1, (9, 0), ((9, 1),),Segment
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetConnectedLabel', '{AE72948E-9683-11CE-8246-00001B4D36B5}')
		return ret

	def GetConnectedNetName(self, Segment=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(26, LCID, 1, (8, 0), ((9, 1),),Segment
			)

	# Result is of type IVdLabel
	def GetLabel(self, Segment=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(13, LCID, 1, (9, 0), ((9, 1),),Segment
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetLabel', '{AE72948E-9683-11CE-8246-00001B4D36B5}')
		return ret

	# Result is of type IColor
	def GetObjectColor(self):
		ret = self._oleobj_.InvokeTypes(30, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjectColor', '{C1031A0C-15BD-4897-A3E5-4C615CDEA684}')
		return ret

	# Result is of type IVdObjs
	def GetRippers(self):
		ret = self._oleobj_.InvokeTypes(28, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetRippers', '{BD2EDF77-7E28-11CE-822D-00001B4D36B7}')
		return ret

	# Result is of type IVdObjs
	def GetSegments(self):
		ret = self._oleobj_.InvokeTypes(14, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetSegments', '{BD2EDF77-7E28-11CE-822D-00001B4D36B7}')
		return ret

	# Result is of type IStringList
	def GetSignals(self):
		ret = self._oleobj_.InvokeTypes(27, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetSignals', '{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')
		return ret

	def GetSingleJointLocs(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(18, LCID, 1, (8, 0), (),)

	def IsColorAutomatic(self):
		return self._oleobj_.InvokeTypes(32, LCID, 1, (11, 0), (),)

	def IsSegmentSelected(self, Segment=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(25, LCID, 1, (11, 0), ((9, 1),),Segment
			)

	def SelectSegment(self, Segment=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(19, LCID, 1, (24, 0), ((9, 1),),Segment
			)

	def SelectSegmentByJointLoc(self, XCoordinate=defaultNamedNotOptArg, YCoordinate=defaultNamedNotOptArg, JointType=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(20, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1)),XCoordinate
			, YCoordinate, JointType)

	def SetAutomaticColor(self, bAutomatic=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(31, LCID, 1, (24, 0), ((11, 1),),bAutomatic
			)

	def SetObjectColor(self, newColor=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(29, LCID, 1, (24, 0), ((9, 1),),newColor
			)

	def _GetColor(self):
		return self._oleobj_.InvokeTypes(16, LCID, 1, (3, 0), (),)

	def _SetColor(self, newColor=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(15, LCID, 1, (24, 0), ((3, 1),),newColor
			)

	def _SetSelected(self, Flag=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(9, LCID, 1, (24, 0), ((3, 1),),Flag
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'IVdApp'
		"Application": (7, 2, (9, 0), (), "Application", '{EA4ABD71-84B0-11CE-8237-00001B4D36B5}'),
		# Method 'Attributes' returns object of type 'IVdObjs'
		"Attributes": (1, 2, (9, 0), (), "Attributes", '{BD2EDF77-7E28-11CE-822D-00001B4D36B7}'),
		"Color": (21, 2, (3, 0), (), "Color", None),
		"FillStyle": (3, 2, (3, 0), (), "FillStyle", None),
		"Id": (6, 2, (3, 0), (), "Id", None),
		"LineStyle": (4, 2, (3, 0), (), "LineStyle", None),
		"LogicalNetName": (33, 2, (8, 0), (), "LogicalNetName", None),
		# Method 'Parent' returns object of type 'IVdBlock'
		"Parent": (8, 2, (9, 0), (), "Parent", '{AE729484-9683-11CE-8246-00001B4D36B5}'),
		"Type": (2, 2, (3, 0), (), "Type", None),
		"UID": (5, 2, (8, 0), (), "UID", None),
		"Width": (34, 2, (3, 0), (), "Width", None),
	}
	_prop_map_put_ = {
		"Color": ((21, LCID, 4, 0),()),
		"FillStyle": ((3, LCID, 4, 0),()),
		"LineStyle": ((4, LCID, 4, 0),()),
		"Selected": ((22, LCID, 4, 0),()),
		"Width": ((34, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IVdObjs(DispatchBaseClass):
	CLSID = IID('{BD2EDF77-7E28-11CE-822D-00001B4D36B7}')
	coclass_clsid = IID('{8B3650E2-6CF5-1014-9D62-FFC3EECCF0AC}')

	def GetType(self, Index=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(5, LCID, 1, (3, 0), ((3, 1),),Index
			)

	def Item(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', None)
		return ret

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'IVdApp'
		"Application": (2, 2, (9, 0), (), "Application", '{EA4ABD71-84B0-11CE-8237-00001B4D36B5}'),
		"Count": (1, 2, (3, 0), (), "Count", None),
		"Parent": (3, 2, (9, 0), (), "Parent", None),
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
	#This class has Item property/method which allows indexed access with the object[key] syntax.
	#Some objects will accept a string or other type of key in addition to integers.
	#Note that many Office objects do not use zero-based indexing.
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(4, LCID, 1, 1, key)), "Item", None)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IVdPin(DispatchBaseClass):
	CLSID = IID('{AE729496-9683-11CE-8246-00001B4D36B5}')
	coclass_clsid = IID('{8B36B079-6CF5-1014-9D62-FFC3EECCF0AC}')

	# Result is of type IVdAttr
	def AddAttribute(self, String=defaultNamedNotOptArg, X=defaultNamedNotOptArg, Y=defaultNamedNotOptArg, Visibility=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(14, LCID, 1, (9, 0), ((8, 1), (3, 1), (3, 1), (3, 1)),String
			, X, Y, Visibility)
		if ret is not None:
			ret = Dispatch(ret, 'AddAttribute', '{AE729482-9683-11CE-8246-00001B4D36B5}')
		return ret

	# Result is of type IVdLabel
	def AddLabel(self, String=defaultNamedNotOptArg, X=defaultNamedNotOptArg, Y=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(15, LCID, 1, (9, 0), ((8, 1), (3, 1), (3, 1)),String
			, X, Y)
		if ret is not None:
			ret = Dispatch(ret, 'AddLabel', '{AE72948E-9683-11CE-8246-00001B4D36B5}')
		return ret

	# Result is of type IVdAttr
	def FindAttribute(self, AttributeName=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(18, LCID, 1, (9, 0), ((8, 1),),AttributeName
			)
		if ret is not None:
			ret = Dispatch(ret, 'FindAttribute', '{AE729482-9683-11CE-8246-00001B4D36B5}')
		return ret

	# Result is of type IVdPoint
	def GetLocation(self, Flag=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(13, LCID, 1, (9, 0), ((3, 1),),Flag
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetLocation', '{AE729498-9683-11CE-8246-00001B4D36B5}')
		return ret

	def GetName(self, Flag=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(11, LCID, 1, (8, 0), ((3, 1),),Flag
			)

	# Result is of type IColor
	def GetObjectColor(self):
		ret = self._oleobj_.InvokeTypes(21, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjectColor', '{C1031A0C-15BD-4897-A3E5-4C615CDEA684}')
		return ret

	def SetLocation(self, XInterior=defaultNamedNotOptArg, YInterior=defaultNamedNotOptArg, XBoundary=defaultNamedNotOptArg, YBoundary=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(12, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1), (3, 1)),XInterior
			, YInterior, XBoundary, YBoundary)

	def _GetColor(self):
		return self._oleobj_.InvokeTypes(16, LCID, 1, (3, 0), (),)

	def _SetColor(self, newColor=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(17, LCID, 1, (24, 0), ((3, 1),),newColor
			)

	def _SetSelected(self, Flag=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(10, LCID, 1, (24, 0), ((3, 1),),Flag
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'IVdApp'
		"Application": (7, 2, (9, 0), (), "Application", '{EA4ABD71-84B0-11CE-8237-00001B4D36B5}'),
		# Method 'Attributes' returns object of type 'IVdObjs'
		"Attributes": (1, 2, (9, 0), (), "Attributes", '{BD2EDF77-7E28-11CE-822D-00001B4D36B7}'),
		"Color": (19, 2, (3, 0), (), "Color", None),
		"Id": (5, 2, (3, 0), (), "Id", None),
		# Method 'Label' returns object of type 'IVdLabel'
		"Label": (2, 2, (9, 0), (), "Label", '{AE72948E-9683-11CE-8246-00001B4D36B5}'),
		# Method 'Parent' returns object of type 'IVdBlock'
		"Parent": (8, 2, (9, 0), (), "Parent", '{AE729484-9683-11CE-8246-00001B4D36B5}'),
		"Sense": (6, 2, (3, 0), (), "Sense", None),
		"Side": (9, 2, (3, 0), (), "Side", None),
		"Type": (3, 2, (3, 0), (), "Type", None),
		"UID": (4, 2, (8, 0), (), "UID", None),
	}
	_prop_map_put_ = {
		"Color": ((19, LCID, 4, 0),()),
		"Selected": ((20, LCID, 4, 0),()),
		"Sense": ((6, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IVdPoint(DispatchBaseClass):
	CLSID = IID('{AE729498-9683-11CE-8246-00001B4D36B5}')
	coclass_clsid = IID('{8B365518-6CF5-1014-9D62-FFC3EECCF0AC}')

	_prop_map_get_ = {
		"X": (1, 2, (3, 0), (), "X", None),
		"Y": (2, 2, (3, 0), (), "Y", None),
	}
	_prop_map_put_ = {
		"X": ((1, LCID, 4, 0),()),
		"Y": ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IVdRect(DispatchBaseClass):
	CLSID = IID('{A4E20F1C-89F1-40CE-B92A-7373BCA0EEF5}')
	coclass_clsid = IID('{8B36599B-6CF5-1014-9D62-FFC3EECCF0AC}')

	_prop_map_get_ = {
		"Bottom": (2, 2, (3, 0), (), "Bottom", None),
		"Left": (1, 2, (3, 0), (), "Left", None),
		"Right": (3, 2, (3, 0), (), "Right", None),
		"Top": (4, 2, (3, 0), (), "Top", None),
	}
	_prop_map_put_ = {
		"Bottom": ((2, LCID, 4, 0),()),
		"Left": ((1, LCID, 4, 0),()),
		"Right": ((3, LCID, 4, 0),()),
		"Top": ((4, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IVdSchematicSheetDocument(DispatchBaseClass):
	CLSID = IID('{D8B95AF2-D943-4295-8D86-71B4F904C3AA}')
	coclass_clsid = IID('{8B3660B9-6CF5-1014-9D62-FFC3EECCF0AC}')

	def AcquireReadWriteRights(self, AllowRights=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(119, LCID, 1, (24, 0), ((11, 1),),AllowRights
			)

	def Activate(self):
		return self._oleobj_.InvokeTypes(105, LCID, 1, (24, 0), (),)

	def CancelSave(self, DoNotWarn=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(113, LCID, 1, (24, 0), ((11, 1),),DoNotWarn
			)

	def Close(self, SaveChanges=defaultNamedNotOptArg, FileName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(106, LCID, 1, (24, 0), ((11, 1), (8, 1)),SaveChanges
			, FileName)

	def DeleteSheet(self, DesignName=defaultNamedNotOptArg, SheetNumber=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(115, LCID, 1, (11, 0), ((8, 1), (8, 1)),DesignName
			, SheetNumber)

	def DiscardSymbolChanges(self):
		return self._oleobj_.InvokeTypes(123, LCID, 1, (24, 0), (),)

	def ExportMetafile(self, OutputName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(110, LCID, 1, (24, 0), ((8, 1),),OutputName
			)

	def GetReadWriteRights(self):
		return self._oleobj_.InvokeTypes(118, LCID, 1, (11, 0), (),)

	# Result is of type IVdViews
	def GetViews(self):
		ret = self._oleobj_.InvokeTypes(108, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetViews', '{DC3A8AF0-91B4-11CE-8243-00001B4D36B5}')
		return ret

	def InsertSheet(self, DesignName=defaultNamedNotOptArg, SheetNumber=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(114, LCID, 1, (11, 0), ((8, 1), (8, 1)),DesignName
			, SheetNumber)

	def IsAccess(self, AccessType=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(111, LCID, 1, (11, 0), ((3, 1),),AccessType
			)

	def IsReadOnly(self):
		return self._oleobj_.InvokeTypes(116, LCID, 1, (11, 0), (),)

	def Print(self, From=defaultNamedNotOptArg, To=defaultNamedNotOptArg, Copies=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(107, LCID, 1, (24, 0), ((2, 1), (2, 1), (2, 1)),From
			, To, Copies)

	def ReRead(self, SheetNumber=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(109, LCID, 1, (11, 0), ((8, 1),),SheetNumber
			)

	def Save(self):
		return self._oleobj_.InvokeTypes(124, LCID, 1, (24, 0), (),)

	def SaveAs(self, FileName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(125, LCID, 1, (24, 0), ((8, 1),),FileName
			)

	def SetFollowingSheetRange(self, Sheets=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(120, LCID, 1, (24, 0), ((9, 1),),Sheets
			)

	def SetReadOnly(self, ReadOnlyFlag=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(117, LCID, 1, (24, 0), ((11, 1),),ReadOnlyFlag
			)

	def SetSheetName(self, Name=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(121, LCID, 1, (24, 0), ((8, 1),),Name
			)

	def UpdateSymbolInDesign(self):
		return self._oleobj_.InvokeTypes(122, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'IVdApp'
		"Application": (101, 2, (9, 0), (), "Application", '{EA4ABD71-84B0-11CE-8237-00001B4D36B5}'),
		"DataType": (112, 2, (3, 0), (), "DataType", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Name": (102, 2, (8, 0), (), "Name", None),
		# Method 'Parent' returns object of type 'IVdSchematicSheetDocuments'
		"Parent": (104, 2, (9, 0), (), "Parent", '{608CA7F4-A52A-4206-9580-3BEB17CE0073}'),
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

class IVdSchematicSheetDocuments(DispatchBaseClass):
	CLSID = IID('{608CA7F4-A52A-4206-9580-3BEB17CE0073}')
	coclass_clsid = IID('{8B36663A-6CF5-1014-9D62-FFC3EECCF0AC}')

	# Result is of type IVdSchematicSheetDocument
	def Add(self):
		ret = self._oleobj_.InvokeTypes(105, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{D8B95AF2-D943-4295-8D86-71B4F904C3AA}')
		return ret

	def Close(self):
		return self._oleobj_.InvokeTypes(106, LCID, 1, (24, 0), (),)

	def CopyBlocksToClipboard(self, Blocks=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(114, LCID, 1, (24, 0), ((9, 1),),Blocks
			)

	def CopySheetsToClipboard(self, Schematic=defaultNamedNotOptArg, Sheets=defaultNamedNotOptArg, srcPaths=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(111, LCID, 1, (24, 0), ((8, 1), (9, 1), (9, 1)),Schematic
			, Sheets, srcPaths)

	def CopyToClipboard(self, SchematicName=defaultNamedNotOptArg, SheetsToCopy=defaultNamedNotOptArg, srcPath=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(119, LCID, 1, (24, 0), ((8, 1), (9, 1), (9, 1)),SchematicName
			, SheetsToCopy, srcPath)

	def DeleteSheet(self, SchematicName=defaultNamedNotOptArg, SheetNumber=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(118, LCID, 1, (11, 0), ((8, 1), (8, 1)),SchematicName
			, SheetNumber)

	def DetermineClipboardContent(self):
		return self._oleobj_.InvokeTypes(116, LCID, 1, (3, 0), (),)

	# Result is of type IStringList
	def GetAvailableSchematics(self):
		ret = self._oleobj_.InvokeTypes(108, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetAvailableSchematics', '{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')
		return ret

	# Result is of type IStringList
	def GetAvailableSheets(self, Schematic=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(109, LCID, 1, (9, 0), ((8, 1),),Schematic
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetAvailableSheets', '{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')
		return ret

	# Result is of type IStringList
	def GetSheetOrder(self, SchematicName=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(121, LCID, 1, (9, 0), ((8, 1),),SchematicName
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetSheetOrder', '{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')
		return ret

	def InsertSheet(self, SchematicName=defaultNamedNotOptArg, SheetNumber=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(117, LCID, 1, (11, 0), ((8, 1), (8, 1)),SchematicName
			, SheetNumber)

	def IsSheetsClipboardEmpty(self):
		return self._oleobj_.InvokeTypes(113, LCID, 1, (3, 0), (),)

	def IsSymbolUnderEdit(self, sSymbolName=defaultNamedNotOptArg, sSymbolExtension=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(124, LCID, 1, (3, 0), ((8, 1), (8, 1)),sSymbolName
			, sSymbolExtension)

	# Result is of type IVdSchematicSheetDocument
	def Item(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(104, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{D8B95AF2-D943-4295-8D86-71B4F904C3AA}')
		return ret

	# Result is of type IVdSchematicSheetDocument
	def Open(self, SchematicName=defaultNamedNotOptArg, SheetName=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(110, LCID, 1, (9, 0), ((8, 1), (8, 1)),SchematicName
			, SheetName)
		if ret is not None:
			ret = Dispatch(ret, 'Open', '{D8B95AF2-D943-4295-8D86-71B4F904C3AA}')
		return ret

	# Result is of type IVdSchematicSheetDocument
	def OpenSymbol(self, sSymbolName=defaultNamedNotOptArg, sSymbolExtension=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(123, LCID, 1, (9, 0), ((8, 1), (8, 1)),sSymbolName
			, sSymbolExtension)
		if ret is not None:
			ret = Dispatch(ret, 'OpenSymbol', '{D8B95AF2-D943-4295-8D86-71B4F904C3AA}')
		return ret

	# Result is of type IVdSchematicSheetDocument
	def Open_Hierarchically(self, SchematicName=defaultNamedNotOptArg, SheetName=defaultNamedNotOptArg, HierPath=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(107, LCID, 1, (9, 0), ((8, 1), (8, 1), (9, 1)),SchematicName
			, SheetName, HierPath)
		if ret is not None:
			ret = Dispatch(ret, 'Open_Hierarchically', '{D8B95AF2-D943-4295-8D86-71B4F904C3AA}')
		return ret

	def PasteBlocksFromClipboard(self):
		return self._oleobj_.InvokeTypes(115, LCID, 1, (24, 0), (),)

	def PasteFromClipboard(self, SchematicName=defaultNamedNotOptArg, dstPath=defaultNamedNotOptArg, SheetsToBeReplaced=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(120, LCID, 1, (24, 0), ((8, 1), (9, 1), (9, 1)),SchematicName
			, dstPath, SheetsToBeReplaced)

	def PasteSheetsFromClipboard(self, Schematic=defaultNamedNotOptArg, dstPaths=defaultNamedNotOptArg, replaceWithSheets=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(112, LCID, 1, (24, 0), ((8, 1), (9, 1), (9, 1)),Schematic
			, dstPaths, replaceWithSheets)

	def SetSheetOrder(self, SchematicName=defaultNamedNotOptArg, sheetRange=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(122, LCID, 1, (24, 0), ((8, 1), (9, 1)),SchematicName
			, sheetRange)

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'IVdApp'
		"Application": (102, 2, (9, 0), (), "Application", '{EA4ABD71-84B0-11CE-8237-00001B4D36B5}'),
		"Count": (101, 2, (3, 0), (), "Count", None),
		# Method 'Parent' returns object of type 'IVdApp'
		"Parent": (103, 2, (9, 0), (), "Parent", '{EA4ABD71-84B0-11CE-8237-00001B4D36B5}'),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{D8B95AF2-D943-4295-8D86-71B4F904C3AA}')
	#This class has Item property/method which allows indexed access with the object[key] syntax.
	#Some objects will accept a string or other type of key in addition to integers.
	#Note that many Office objects do not use zero-based indexing.
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(104, LCID, 1, 1, key)), "Item", '{D8B95AF2-D943-4295-8D86-71B4F904C3AA}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(101, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IVdSegment(DispatchBaseClass):
	CLSID = IID('{AE72949A-9683-11CE-8246-00001B4D36B5}')
	coclass_clsid = IID('{8B36B3E7-6CF5-1014-9D62-FFC3EECCF0AC}')

	def GetJointType(self, WhichJoint=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(7, LCID, 1, (3, 0), ((3, 1),),WhichJoint
			)

	def IsBus(self):
		return self._oleobj_.InvokeTypes(5, LCID, 1, (11, 0), (),)

	# Result is of type IVdPoint
	def Location(self, WhichJoint=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(6, LCID, 1, (9, 0), ((3, 1),),WhichJoint
			)
		if ret is not None:
			ret = Dispatch(ret, 'Location', '{AE729498-9683-11CE-8246-00001B4D36B5}')
		return ret

	def SetLocation(self, WhichJoint=defaultNamedNotOptArg, newCoord=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(8, LCID, 1, (24, 0), ((3, 1), (9, 1)),WhichJoint
			, newCoord)

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'IVdApp'
		"Application": (3, 2, (9, 0), (), "Application", '{EA4ABD71-84B0-11CE-8237-00001B4D36B5}'),
		# Method 'Attributes' returns object of type 'IVdObjs'
		"Attributes": (2, 2, (9, 0), (), "Attributes", '{BD2EDF77-7E28-11CE-822D-00001B4D36B7}'),
		# Method 'Parent' returns object of type 'IVdNet'
		"Parent": (4, 2, (9, 0), (), "Parent", '{AE729492-9683-11CE-8246-00001B4D36B5}'),
		"Type": (1, 2, (3, 0), (), "Type", None),
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

class IVdText(DispatchBaseClass):
	CLSID = IID('{AE72949C-9683-11CE-8246-00001B4D36B5}')
	coclass_clsid = IID('{8B36B75E-6CF5-1014-9D62-FFC3EECCF0AC}')

	# Result is of type IVdPoint
	def GetLocation(self):
		ret = self._oleobj_.InvokeTypes(10, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetLocation', '{AE729498-9683-11CE-8246-00001B4D36B5}')
		return ret

	# Result is of type IColor
	def GetObjectColor(self):
		ret = self._oleobj_.InvokeTypes(17, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjectColor', '{C1031A0C-15BD-4897-A3E5-4C615CDEA684}')
		return ret

	def IsColorAutomatic(self):
		return self._oleobj_.InvokeTypes(19, LCID, 1, (11, 0), (),)

	def SetAutomaticColor(self, bAutomatic=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(18, LCID, 1, (24, 0), ((11, 1),),bAutomatic
			)

	def SetLocation(self, X=defaultNamedNotOptArg, Y=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(11, LCID, 1, (24, 0), ((3, 1), (3, 1)),X
			, Y)

	def SetObjectColor(self, newColor=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(16, LCID, 1, (24, 0), ((9, 1),),newColor
			)

	def _GetColor(self):
		return self._oleobj_.InvokeTypes(12, LCID, 1, (3, 0), (),)

	def _SetColor(self, newColor=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(13, LCID, 1, (24, 0), ((3, 1),),newColor
			)

	def _SetSelected(self, Flag=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(9, LCID, 1, (24, 0), ((3, 1),),Flag
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'IVdApp'
		"Application": (8, 2, (9, 0), (), "Application", '{EA4ABD71-84B0-11CE-8237-00001B4D36B5}'),
		"Color": (15, 2, (3, 0), (), "Color", None),
		"Font": (3, 2, (3, 0), (), "Font", None),
		"Orientation": (5, 2, (3, 0), (), "Orientation", None),
		"Origin": (4, 2, (3, 0), (), "Origin", None),
		# Method 'Parent' returns object of type 'IVdBlock'
		"Parent": (7, 2, (9, 0), (), "Parent", '{AE729484-9683-11CE-8246-00001B4D36B5}'),
		"Printable": (20, 2, (11, 0), (), "Printable", None),
		"Size": (6, 2, (3, 0), (), "Size", None),
		"TextString": (1, 2, (8, 0), (), "TextString", None),
		"Type": (2, 2, (3, 0), (), "Type", None),
	}
	_prop_map_put_ = {
		"Color": ((15, LCID, 4, 0),()),
		"Font": ((3, LCID, 4, 0),()),
		"Orientation": ((5, LCID, 4, 0),()),
		"Origin": ((4, LCID, 4, 0),()),
		"Printable": ((20, LCID, 4, 0),()),
		"Selected": ((14, LCID, 4, 0),()),
		"Size": ((6, LCID, 4, 0),()),
		"TextString": ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IVdView(DispatchBaseClass):
	CLSID = IID('{0892A013-86BC-11CE-8238-00001B4D36B5}')
	coclass_clsid = IID('{8B3624C8-6CF5-1014-9D62-FFC3EECCF0AC}')

	def Activate(self):
		return self._oleobj_.InvokeTypes(11, LCID, 1, (24, 0), (),)

	# Result is of type IVdBlock
	def ActiveBlock(self):
		ret = self._oleobj_.InvokeTypes(8, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'ActiveBlock', '{AE729484-9683-11CE-8246-00001B4D36B5}')
		return ret

	def AddAttributeMoveMode(self, AttributeString=defaultNamedNotOptArg, Visibility=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(20, LCID, 1, (24, 0), ((8, 1), (3, 1)),AttributeString
			, Visibility)

	def AddMissingPorts(self):
		return self._oleobj_.InvokeTypes(32, LCID, 1, (24, 0), (),)

	def AddReuseBlock(self, partName=defaultNamedNotOptArg, SymbolName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(31, LCID, 1, (11, 0), ((8, 1), (8, 1)),partName
			, SymbolName)

	# Result is of type IVdApp
	def Application(self):
		ret = self._oleobj_.InvokeTypes(9, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Application', '{EA4ABD71-84B0-11CE-8237-00001B4D36B5}')
		return ret

	def BufferCopy(self):
		return self._oleobj_.InvokeTypes(13, LCID, 1, (24, 0), (),)

	def BufferCut(self):
		return self._oleobj_.InvokeTypes(14, LCID, 1, (24, 0), (),)

	def BufferPaste(self):
		return self._oleobj_.InvokeTypes(15, LCID, 1, (24, 0), (),)

	def BufferPasteXY(self, PasteX=defaultNamedNotOptArg, PasteY=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(22, LCID, 1, (11, 0), ((3, 1), (3, 1)),PasteX
			, PasteY)

	def ComputeMBB(self, OLEItems=defaultNamedNotOptArg, Xmin=defaultNamedNotOptArg, Ymin=defaultNamedNotOptArg, Xmax=defaultNamedNotOptArg
			, Ymax=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(16, LCID, 1, (24, 0), ((11, 1), (16387, 1), (16387, 1), (16387, 1), (16387, 1)),OLEItems
			, Xmin, Ymin, Xmax, Ymax)

	# Result is of type IVdSchematicSheetDocument
	def Document(self):
		ret = self._oleobj_.InvokeTypes(10, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Document', '{D8B95AF2-D943-4295-8D86-71B4F904C3AA}')
		return ret

	def DumpImage(self, FileName=defaultNamedNotOptArg, Width=-1, Height=-1):
		return self._oleobj_.InvokeTypes(33, LCID, 1, (24, 0), ((8, 1), (3, 49), (3, 49)),FileName
			, Width, Height)

	def GetJointLocs(self, AllOrSelected=defaultNamedNotOptArg, JointType=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(23, LCID, 1, (8, 0), ((3, 1), (3, 1)),AllOrSelected
			, JointType)

	def GetName(self, Flag=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(28, LCID, 1, (8, 0), ((3, 1),),Flag
			)

	def GetSelectedNetName(self, bRetFullPath=defaultNamedNotOptArg, bRetInternalName=defaultNamedNotOptArg, Index=1):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(18, LCID, 1, (8, 0), ((11, 1), (11, 1), (3, 49)),bRetFullPath
			, bRetInternalName, Index)

	def GetTopBlockName(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(34, LCID, 1, (8, 0), (),)

	def GetTopLevelDesignName(self):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(29, LCID, 1, (8, 0), (),)

	def ModifyVisibility(self, SelectString=defaultNamedNotOptArg, Visibility=defaultNamedNotOptArg, ApplyToSelected=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(19, LCID, 1, (24, 0), ((8, 1), (3, 1), (3, 1)),SelectString
			, Visibility, ApplyToSelected)

	# Result is of type IVdObjs
	def Query(self, Flags=defaultNamedNotOptArg, Selected=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(2, LCID, 1, (9, 0), ((3, 1), (3, 1)),Flags
			, Selected)
		if ret is not None:
			ret = Dispatch(ret, 'Query', '{BD2EDF77-7E28-11CE-822D-00001B4D36B7}')
		return ret

	def Refresh(self):
		return self._oleobj_.InvokeTypes(6, LCID, 1, (24, 0), (),)

	def SelectByName(self, Name=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1, LCID, 1, (11, 0), ((8, 1),),Name
			)

	def SelectByName2(self, lpszObjName=defaultNamedNotOptArg, bAddSelect=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(17, LCID, 1, (11, 0), ((8, 1), (11, 1)),lpszObjName
			, bAddSelect)

	def SelectObject(self, ObjectType=defaultNamedNotOptArg, Expression=defaultNamedNotOptArg, SelectOwner=defaultNamedNotOptArg, RegExp=defaultNamedNotOptArg
			, AddSelect=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(12, LCID, 1, (3, 0), ((3, 1), (8, 1), (11, 1), (11, 1), (11, 1)),ObjectType
			, Expression, SelectOwner, RegExp, AddSelect)

	def SelectSegmentByJointLoc(self, XCoordinate=defaultNamedNotOptArg, YCoordinate=defaultNamedNotOptArg, JointType=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(24, LCID, 1, (11, 0), ((3, 1), (3, 1), (3, 1)),XCoordinate
			, YCoordinate, JointType)

	def SelectText(self, Pattern=defaultNamedNotOptArg, Type=defaultNamedNotOptArg, ApplyToSelected=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(21, LCID, 1, (24, 0), ((8, 1), (3, 1), (3, 1)),Pattern
			, Type, ApplyToSelected)

	def SetCenter(self, X=defaultNamedNotOptArg, Y=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(30, LCID, 1, (24, 0), ((3, 1), (3, 0)),X
			, Y)

	def ViewFull(self):
		return self._oleobj_.InvokeTypes(7, LCID, 1, (24, 0), (),)

	def ZoomIn(self):
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), (),)

	def ZoomOut(self):
		return self._oleobj_.InvokeTypes(4, LCID, 1, (11, 0), (),)

	def ZoomSelect(self):
		return self._oleobj_.InvokeTypes(5, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		# Method 'Block' returns object of type 'IVdBlock'
		"Block": (26, 2, (9, 0), (), "Block", '{AE729484-9683-11CE-8246-00001B4D36B5}'),
		# Method 'TopBlock' returns object of type 'IVdBlock'
		"TopBlock": (27, 2, (9, 0), (), "TopBlock", '{AE729484-9683-11CE-8246-00001B4D36B5}'),
		# Method 'Viewport' returns object of type 'IViewport'
		"Viewport": (25, 2, (9, 0), (), "Viewport", '{02768321-EB56-11D1-BE0C-00A0C9204FDC}'),
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

class IVdViewEvents:
	'Event interface for ViewDraw View'
	CLSID = CLSID_Sink = IID('{648981C1-A956-11D1-80F2-00A0C97221DB}')
	coclass_clsid = IID('{8B3624C8-6CF5-1014-9D62-FFC3EECCF0AC}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnSelect",
		        2 : "OnModify",
		        3 : "OnActivate",
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
#	def OnSelect(self, View=defaultNamedNotOptArg):
#	def OnModify(self, View=defaultNamedNotOptArg, Block=defaultNamedNotOptArg):
#	def OnActivate(self):


class IVdViews(DispatchBaseClass):
	CLSID = IID('{DC3A8AF0-91B4-11CE-8243-00001B4D36B5}')
	coclass_clsid = IID('{8B366D22-6CF5-1014-9D62-FFC3EECCF0AC}')

	# Result is of type IVdView
	def Item(self, Index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{0892A013-86BC-11CE-8238-00001B4D36B5}')
		return ret

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'IVdApp'
		"Application": (2, 2, (9, 0), (), "Application", '{EA4ABD71-84B0-11CE-8237-00001B4D36B5}'),
		"Count": (1, 2, (3, 0), (), "Count", None),
		# Method 'Parent' returns object of type 'IVdDoc'
		"Parent": (3, 2, (9, 0), (), "Parent", '{4ADEF4E2-690A-11CE-9261-0020C5E26659}'),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{0892A013-86BC-11CE-8238-00001B4D36B5}')
	#This class has Item property/method which allows indexed access with the object[key] syntax.
	#Some objects will accept a string or other type of key in addition to integers.
	#Note that many Office objects do not use zero-based indexing.
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(4, LCID, 1, 1, key)), "Item", '{0892A013-86BC-11CE-8238-00001B4D36B5}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IViewport(DispatchBaseClass):
	CLSID = IID('{02768321-EB56-11D1-BE0C-00A0C9204FDC}')
	coclass_clsid = IID('{8B362142-6CF5-1014-9D62-FFC3EECCF0AC}')

	def Arc(self, X1=defaultNamedNotOptArg, Y1=defaultNamedNotOptArg, X2=defaultNamedNotOptArg, Y2=defaultNamedNotOptArg
			, X3=defaultNamedNotOptArg, Y3=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(21, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1)),X1
			, Y1, X2, Y2, X3, Y3
			)

	def Arrow(self, X1=defaultNamedNotOptArg, Y1=defaultNamedNotOptArg, X2=defaultNamedNotOptArg, Y2=defaultNamedNotOptArg
			, Arrowhead=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(18, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1), (3, 1), (3, 1)),X1
			, Y1, X2, Y2, Arrowhead)

	def Box(self, Left=defaultNamedNotOptArg, Top=defaultNamedNotOptArg, Right=defaultNamedNotOptArg, Bottom=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(20, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1), (3, 1)),Left
			, Top, Right, Bottom)

	def Circle(self, X=defaultNamedNotOptArg, Y=defaultNamedNotOptArg, Radius=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(19, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1)),X
			, Y, Radius)

	def Ellipse(self, X=defaultNamedNotOptArg, Y=defaultNamedNotOptArg, XRadius=defaultNamedNotOptArg, YRadius=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(22, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1), (3, 1)),X
			, Y, XRadius, YRadius)

	def EraseRectangle(self, Left=defaultNamedNotOptArg, Top=defaultNamedNotOptArg, Right=defaultNamedNotOptArg, Bottom=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(16, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1), (3, 1)),Left
			, Top, Right, Bottom)

	# Result is of type IColor
	def GetObjectColor(self):
		ret = self._oleobj_.InvokeTypes(28, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjectColor', '{C1031A0C-15BD-4897-A3E5-4C615CDEA684}')
		return ret

	def Line(self, X1=defaultNamedNotOptArg, Y1=defaultNamedNotOptArg, X2=defaultNamedNotOptArg, Y2=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(17, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1), (3, 1)),X1
			, Y1, X2, Y2)

	def PixelRectangle(self, Left=defaultNamedNotOptArg, Top=defaultNamedNotOptArg, Right=defaultNamedNotOptArg, Bottom=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(14, LCID, 1, (24, 0), ((16396, 1), (16396, 1), (16396, 1), (16396, 1)),Left
			, Top, Right, Bottom)

	def PixelToUser(self, XCoordinate=defaultNamedNotOptArg, YCoordinate=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(11, LCID, 1, (24, 0), ((16396, 1), (16396, 1)),XCoordinate
			, YCoordinate)

	def Point(self, X=defaultNamedNotOptArg, Y=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(23, LCID, 1, (24, 0), ((3, 1), (3, 1)),X
			, Y)

	def PolyLine(self, ArrayOfXValues=defaultNamedNotOptArg, ArrayOfYValues=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(13, LCID, 1, (11, 0), ((12, 1), (12, 1)),ArrayOfXValues
			, ArrayOfYValues)

	# Result is of type IVdRect
	def SetClipRectangle(self, Left=defaultNamedNotOptArg, Top=defaultNamedNotOptArg, Right=defaultNamedNotOptArg, Bottom=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(26, LCID, 1, (9, 0), ((3, 1), (3, 1), (3, 1), (3, 1)),Left
			, Top, Right, Bottom)
		if ret is not None:
			ret = Dispatch(ret, 'SetClipRectangle', '{A4E20F1C-89F1-40CE-B92A-7373BCA0EEF5}')
		return ret

	def SetObjectColor(self, newColor=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(27, LCID, 1, (24, 0), ((9, 1),),newColor
			)

	def Spline(self, Type=defaultNamedNotOptArg, Order=defaultNamedNotOptArg, Granularity=defaultNamedNotOptArg, XArrayOfPoints=defaultNamedNotOptArg
			, YArrayOfPoints=defaultNamedNotOptArg, Arrowhead=defaultNamedNotOptArg, ArrowWidth=defaultNamedNotOptArg, ArrowLength=defaultNamedNotOptArg, ArrowFill=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(24, LCID, 1, (24, 0), ((3, 1), (3, 1), (2, 1), (12, 1), (12, 1), (3, 1), (2, 1), (2, 1), (3, 1)),Type
			, Order, Granularity, XArrayOfPoints, YArrayOfPoints, Arrowhead
			, ArrowWidth, ArrowLength, ArrowFill)

	def Text(self, X=defaultNamedNotOptArg, Y=defaultNamedNotOptArg, String=defaultNamedNotOptArg, Flags=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(25, LCID, 1, (24, 0), ((3, 1), (3, 1), (8, 1), (3, 1)),X
			, Y, String, Flags)

	def UserRectangle(self, Left=defaultNamedNotOptArg, Top=defaultNamedNotOptArg, Right=defaultNamedNotOptArg, Bottom=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(15, LCID, 1, (24, 0), ((16396, 1), (16396, 1), (16396, 1), (16396, 1)),Left
			, Top, Right, Bottom)

	def UserToPixel(self, XCoordinate=defaultNamedNotOptArg, YCoordinate=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(12, LCID, 1, (24, 0), ((16396, 1), (16396, 1)),XCoordinate
			, YCoordinate)

	_prop_map_get_ = {
		"Color": (4, 2, (3, 0), (), "Color", None),
		"FillStyle": (2, 2, (3, 0), (), "FillStyle", None),
		"LineCap": (6, 2, (3, 0), (), "LineCap", None),
		"LineJoin": (7, 2, (3, 0), (), "LineJoin", None),
		"LinePattern": (3, 2, (3, 0), (), "LinePattern", None),
		"LineThickness": (1, 2, (3, 0), (), "LineThickness", None),
		"RasterMode": (5, 2, (3, 0), (), "RasterMode", None),
	}
	_prop_map_put_ = {
		"Color": ((4, LCID, 4, 0),()),
		"FillStyle": ((2, LCID, 4, 0),()),
		"LineCap": ((6, LCID, 4, 0),()),
		"LineJoin": ((7, LCID, 4, 0),()),
		"LinePattern": ((3, LCID, 4, 0),()),
		"LineThickness": ((1, LCID, 4, 0),()),
		"RasterMode": ((5, LCID, 4, 0),()),
		"TextAngle": ((10, LCID, 4, 0),()),
		"TextFont": ((8, LCID, 4, 0),()),
		"TextSize": ((9, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

from win32com.client import CoClassBaseClass
# This CoClass is known by the name 'ViewDraw.AddinInfo.119'
class AddinInfo(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B362D9C-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IAddinInfo,
	]
	default_interface = IAddinInfo

class Application(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B364984-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
		IVdAppEvents,
	]
	default_source = IVdAppEvents
	coclass_interfaces = [
		IVdApp,
	]
	default_interface = IVdApp

class ApplicationAtTest(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B3709E0-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVdApplicationAtTest,
	]
	default_interface = IVdApplicationAtTest

class ApplicationProtectionProxy(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B3647CF-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVdAppProtectionProxy,
	]
	default_interface = IVdAppProtectionProxy

class Arc(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B365B5C-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVdArc,
	]
	default_interface = IVdArc

class Attribute(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B367087-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVdAttr,
	]
	default_interface = IVdAttr

class AutoString(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B36C22C-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IAutoString,
	]
	default_interface = IAutoString

class Block(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B367462-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVdBlock,
	]
	default_interface = IVdBlock

class Box(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B368CC3-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVdBox,
	]
	default_interface = IVdBox

class CCmdMgr(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B364617-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ICommandsManager,
	]
	default_interface = ICommandsManager

# This CoClass is known by the name 'ViewDraw.Color.119'
class CColor(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B362829-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IColor,
	]
	default_interface = IColor

class CComFrameworkAdapter(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B363BA5-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IFramework,
	]
	default_interface = IFramework

class CCommPropDef(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B363F3D-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ICommonPropertyDefinition,
	]
	default_interface = ICommonPropertyDefinition

class CCommPropMgr(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B36429D-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ICommonPropertyManager,
	]
	default_interface = ICommonPropertyManager

class CICTDocs(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B3669A8-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IICTDocuments,
	]
	default_interface = IICTDocuments

class CProjectData(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B3637D0-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IProjectData,
		IODProjectData,
	]
	default_interface = IProjectData

class CRipper(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B36ACFF-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IRipper,
	]
	default_interface = IRipper

class CStringList(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B3630F8-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IStringList,
	]
	default_interface = IStringList

# This CoClass is known by the name 'Viewdraw.Application.119'
class CVdApp(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B364B47-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
		IVdAppEvents,
	]
	default_source = IVdAppEvents
	coclass_interfaces = [
		IVdApp,
	]
	default_interface = IVdApp

# This CoClass is known by the name 'Viewdraw.ApplicationAtTest.119'
class CVdApplicationAtTest(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B370C04-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVdApplicationAtTest,
	]
	default_interface = IVdApplicationAtTest

class CVdArc(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B365D33-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVdArc,
	]
	default_interface = IVdArc

class CVdAttr(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B36723A-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVdAttr,
	]
	default_interface = IVdAttr

class CVdBlock(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B367622-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVdBlock,
	]
	default_interface = IVdBlock

class CVdBox(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B368EF8-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVdBox,
	]
	default_interface = IVdBox

class CVdCircle(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B36932D-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVdCircle,
	]
	default_interface = IVdCircle

class CVdCmpPin(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B369E7F-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVdCmpPin,
	]
	default_interface = IVdCmpPin

class CVdComp(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B36976A-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVdComp,
	]
	default_interface = IVdComp

class CVdConnection(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B36BB3F-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVdConnection,
	]
	default_interface = IVdConnection

# This CoClass is known by the name 'ViewDraw.Document'
class CVdDoc(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B3660B9-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVdSchematicSheetDocument,
		IVdDoc,
	]
	default_interface = IVdSchematicSheetDocument

class CVdDocs(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B36663A-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVdSchematicSheetDocuments,
		IVdDocs,
	]
	default_interface = IVdSchematicSheetDocuments

class CVdFrameBoard(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B36CE74-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVdFrameBoard,
	]
	default_interface = IVdFrameBoard

# This CoClass is known by the name 'Viewdraw.HighPrecisionObject.119'
class CVdHighPrecisionObject(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B37081F-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVdHighPrecisionObject,
	]
	default_interface = IVdHighPrecisionObject

class CVdICTAttr(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B367F7F-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVdICTAttr,
	]
	default_interface = IVdICTAttr

class CVdICTObjs(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B3650E2-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVdObjs,
	]
	default_interface = IVdObjs

class CVdICTViews(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B366ED1-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVdICTViews,
	]
	default_interface = IVdICTViews

class CVdLabel(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B36A221-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVdLabel,
	]
	default_interface = IVdLabel

class CVdLibrary(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B36BEBC-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVdLibrary,
	]
	default_interface = IVdLibrary

class CVdLine(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B36A61A-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVdLine,
	]
	default_interface = IVdLine

class CVdNet(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B36A986-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVdNet,
	]
	default_interface = IVdNet

class CVdObjs(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B364EBC-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVdObjs,
	]
	default_interface = IVdObjs

class CVdPin(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B36B079-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVdPin,
	]
	default_interface = IVdPin

class CVdPoint(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B365518-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVdPoint,
	]
	default_interface = IVdPoint

class CVdRect(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B36599B-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVdRect,
	]
	default_interface = IVdRect

class CVdSegment(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B36B3E7-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVdSegment,
	]
	default_interface = IVdSegment

class CVdText(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B36B75E-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVdText,
	]
	default_interface = IVdText

class CVdViews(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B366D22-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVdViews,
	]
	default_interface = IVdViews

class CViewDrawView(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B3624C8-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
		IVdViewEvents,
	]
	default_source = IVdViewEvents
	coclass_interfaces = [
		IVdView,
	]
	default_interface = IVdView

class Circle(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B369114-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVdCircle,
	]
	default_interface = IVdCircle

class ComFrameworAdapter(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B363980-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IFramework,
	]
	default_interface = IFramework

class CommandsManager(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B36444B-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ICommandsManager,
	]
	default_interface = ICommandsManager

class CommonPropertyDefinition(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B363D89-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ICommonPropertyDefinition,
	]
	default_interface = ICommonPropertyDefinition

class CommonPropertyManager(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B3640F0-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ICommonPropertyManager,
	]
	default_interface = ICommonPropertyManager

class Component(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B36954D-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVdComp,
	]
	default_interface = IVdComp

class ComponentPin(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B3699A8-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVdCmpPin,
	]
	default_interface = IVdCmpPin

class Connection(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B36B90B-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVdConnection,
	]
	default_interface = IVdConnection

class DesignerDataManagement(CoClassBaseClass): # A CoClass
	# MGCDesigner Data Managment Class.
	CLSID = IID('{8B3726C8-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCDesignerDataManagement,
	]
	default_interface = IMGCDesignerDataManagement

class DesignerDataManagementAdditionalProperties(CoClassBaseClass): # A CoClass
	# MGCDesigner Data Managment Additional Properties Collection Class.
	CLSID = IID('{8B372E3C-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCDesignerDataManagementAdditionalProperties,
	]
	default_interface = IMGCDesignerDataManagementAdditionalProperties

class DesignerDataManagementAdditionalProperty(CoClassBaseClass): # A CoClass
	# MGCDesigner Data Management Additional Property Class.
	CLSID = IID('{8B372C67-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCDesignerDataManagementAdditionalProperty,
	]
	default_interface = IMGCDesignerDataManagementAdditionalProperty

class DesignerDataManagementEntities(CoClassBaseClass): # A CoClass
	# MGCDesigner Data Managment Collection Object.
	CLSID = IID('{8B372A86-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCDesignerDataManagementEntities,
	]
	default_interface = IMGCDesignerDataManagementEntities

class DesignerDataManagementEntity(CoClassBaseClass): # A CoClass
	# MGCDesigner Board Data Managment Class.
	CLSID = IID('{8B372899-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMGCDesignerDataManagementEntity,
	]
	default_interface = IMGCDesignerDataManagementEntity

class FrameBoard(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B36CCC6-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVdFrameBoard,
	]
	default_interface = IVdFrameBoard

class HDLSourceDocument(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B36C3DE-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IHDLSourceDocument,
	]
	default_interface = IHDLSourceDocument

class HDLSourceDocuments(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B36C5D2-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IHDLSourceDocuments,
	]
	default_interface = IHDLSourceDocuments

class HTMLSourceDocument(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B36C967-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IHTMLSourceDocument,
	]
	default_interface = IHTMLSourceDocument

class HTMLSourceDocuments(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B36CB16-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IHTMLSourceDocuments,
	]
	default_interface = IHTMLSourceDocuments

class HighPrecisionObject(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B370649-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVdHighPrecisionObject,
	]
	default_interface = IVdHighPrecisionObject

class ICTAttribute(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B367A2D-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVdICTAttr,
	]
	default_interface = IVdICTAttr

class ICTBlock(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B3681F1-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVdICTBlock,
	]
	default_interface = IVdICTBlock

class ICTComp(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B36843C-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVdICTComp,
	]
	default_interface = IVdICTComp

class ICTDocument(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B3662D5-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVdICTDocument,
	]
	default_interface = IVdICTDocument

class ICTDocuments(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B3667E8-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IICTDocuments,
	]
	default_interface = IICTDocuments

class ICTNet(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B368664-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVdICTNet,
	]
	default_interface = IVdICTNet

class ICTObject(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B368AA4-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVdICTObj,
	]
	default_interface = IVdICTObj

class ICTPin(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B368887-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVdICTPin,
	]
	default_interface = IVdICTPin

class ICTView(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B36267B-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVdICTView,
	]
	default_interface = IVdICTView

class Label(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B36A05C-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVdLabel,
	]
	default_interface = IVdLabel

class Library(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B36BCF2-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVdLibrary,
	]
	default_interface = IVdLibrary

class Line(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B36A402-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVdLine,
	]
	default_interface = IVdLine

# This CoClass is known by the name 'ViewDraw.MergeData.119'
class MergeData(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B362BED-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMergeData,
	]
	default_interface = IMergeData

class Net(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B36A7CA-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVdNet,
	]
	default_interface = IVdNet

class Objects(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B364CF9-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVdObjs,
	]
	default_interface = IVdObjs

class PDBPartitions(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B363464-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IPDBPartitions,
	]
	default_interface = IPDBPartitions

class Pin(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B36AEBD-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVdPin,
	]
	default_interface = IVdPin

class Point(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B3652FF-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVdPoint,
	]
	default_interface = IVdPoint

class ProjectData(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B363620-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IProjectData,
		IODProjectData,
	]
	default_interface = IProjectData

class ProjectManagerEventSink(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B36C7B3-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IProjectManagerEventSink,
	]
	default_interface = IProjectManagerEventSink

class Rect(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B36573C-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVdRect,
	]
	default_interface = IVdRect

class Ripper(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B36AB36-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IRipper,
	]
	default_interface = IRipper

class SchematicSheetDocument(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B365EF0-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVdSchematicSheetDocument,
		IVdDoc,
	]
	default_interface = IVdSchematicSheetDocument

class SchematicSheetDocuments(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B366486-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVdSchematicSheetDocuments,
		IVdDocs,
	]
	default_interface = IVdSchematicSheetDocuments

class Segment(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B36B22E-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVdSegment,
	]
	default_interface = IVdSegment

class StringCollection(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B36C077-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IStringCollection,
	]
	default_interface = IStringCollection

# This CoClass is known by the name 'ViewDraw.StringList.119'
class StringList(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B362F49-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IStringList,
	]
	default_interface = IStringList

class SymbolPartitions(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B3632A1-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISymbolPartitions,
	]
	default_interface = ISymbolPartitions

class Text(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B36B5B3-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVdText,
	]
	default_interface = IVdText

class View(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B3622FE-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
		IVdViewEvents,
	]
	default_source = IVdViewEvents
	coclass_interfaces = [
		IVdView,
	]
	default_interface = IVdView

class Viewport(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B362142-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IViewport,
	]
	default_interface = IViewport

class Views(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B366B73-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVdViews,
	]
	default_interface = IVdViews

class _CColor(CoClassBaseClass): # A CoClass
	CLSID = IID('{8B362A2D-6CF5-1014-9D62-FFC3EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IColor,
	]
	default_interface = IColor

IAddinInfo_vtables_dispatch_ = 1
IAddinInfo_vtables_ = [
	(( 'Name' , 'sName' , ), 1, (1, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'sName' , ), 1, (1, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'ProgId' , 'sProgId' , ), 2, (2, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'ProgId' , 'sProgId' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Script' , 'sScript' , ), 3, (3, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 64 , )),
	(( 'Script' , 'sScript' , ), 3, (3, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 64 , )),
	(( 'Placement' , 'sPlacement' , ), 5, (5, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Placement' , 'sPlacement' , ), 5, (5, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'ShortCutKey' , 'sShortCutKey' , ), 7, (7, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'ShortCutKey' , 'sShortCutKey' , ), 7, (7, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'ToolbarButton' , 'bToolbarButton' , ), 8, (8, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'ToolbarButton' , 'bToolbarButton' , ), 8, (8, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'RuntimeCreateDecision' , 'bRuntimeCreateDecision' , ), 9, (9, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'RuntimeCreateDecision' , 'bRuntimeCreateDecision' , ), 9, (9, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'LicenseFeature' , 'sLicenseFeature' , ), 10, (10, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'LicenseFeature' , 'sLicenseFeature' , ), 10, (10, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'InitiallyDisabled' , 'bInitiallyDisabled' , ), 11, (11, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'InitiallyDisabled' , 'bInitiallyDisabled' , ), 11, (11, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'InitiallyVisible' , 'bInitiallyVisible' , ), 12, (12, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'InitiallyVisible' , 'bInitiallyVisible' , ), 12, (12, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
]

IAutoString_vtables_dispatch_ = 1
IAutoString_vtables_ = [
	(( 'Text' , 'retval' , ), 1, (1, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Text' , 'retval' , ), 1, (1, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_Text' , 'retval' , ), 0, (0, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IColor_vtables_dispatch_ = 1
IColor_vtables_ = [
	(( 'r' , 'lR' , ), 1, (1, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'r' , 'lR' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'g' , 'lG' , ), 2, (2, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'g' , 'lG' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'b' , 'lB' , ), 3, (3, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'b' , 'lB' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

ICommandsManager_vtables_dispatch_ = 1
ICommandsManager_vtables_ = [
	(( 'RegisterOLECommand' , 'CommandName' , 'CommandDescription' , 'bModifiesData' , 'pDispatch' , 
			 'retval' , ), 321, (321, (), [ (8, 1, None, None) , (8, 1, None, None) , (11, 1, None, None) , 
			 (9, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'UnregisterOLECommand' , 'CommandName' , 'ClientDispatch' , 'retval' , ), 322, (322, (), [ 
			 (8, 1, None, None) , (9, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'CommandEnable' , 'CommandName' , 'retval' , ), 323, (323, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'CommandDisable' , 'CommandName' , 'retval' , ), 324, (324, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'CommandRemove' , 'CommandName' , 'retval' , ), 325, (325, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'ExecuteMenuCommand' , 'command_name' , ), 326, (326, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'ExecuteCommand' , 'CommandString' , 'retval' , ), 327, (327, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'ExecuteCommandByID' , 'command_Id' , ), 328, (328, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 64 , )),
]

ICommonPropertyDefinition_vtables_dispatch_ = 1
ICommonPropertyDefinition_vtables_ = [
	(( 'GetId' , 'retval' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'GetName' , 'retval' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'GetOwnerTypes' , 'retval' , ), 3, (3, (), [ (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'AreMultipleEntriesOK' , 'retval' , ), 4, (4, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'CanBeOverriden' , 'retval' , ), 5, (5, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'IsTransferredFromPDB' , 'retval' , ), 6, (6, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'GetOrignalRegularExp' , 'retval' , ), 7, (7, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'GetRegularExp' , 'retval' , ), 8, (8, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'GetMaxNumberOfChars' , 'retval' , ), 9, (9, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'GetMaxNumberOfLines' , 'retval' , ), 10, (10, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'GetStorageType' , 'retval' , ), 11, (11, (), [ (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'IsNotationInvalid' , 'retval' , ), 12, (12, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'CheckPropertyValue' , 'Value' , 'retval' , ), 13, (13, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'IsVisible' , 'retval' , ), 14, (14, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'GetFontColor' , 'retval' , ), 15, (15, (), [ (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'GetFontHeight' , 'retval' , ), 16, (16, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'GetFontName' , 'retval' , ), 17, (17, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
]

ICommonPropertyManager_vtables_dispatch_ = 1
ICommonPropertyManager_vtables_ = [
	(( 'GetLoadedFile' , 'retval' , ), 1, (1, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'GetPropertyNames' , 'arrayOfNames' , ), 2, (2, (), [ (16393, 10, None, "IID('{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')") , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'GetCompPropertyNames' , 'arrayOfNames' , ), 3, (3, (), [ (16393, 10, None, "IID('{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')") , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'GetPinPropertyNames' , 'arrayOfNames' , ), 4, (4, (), [ (16393, 10, None, "IID('{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')") , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'GetNetPropertyNames' , 'arrayOfNames' , ), 5, (5, (), [ (16393, 10, None, "IID('{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'GetTransPropertyNames' , 'arrayOfNames' , ), 6, (6, (), [ (16393, 10, None, "IID('{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')") , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'GetLoosePropertyNames' , 'arrayOfNames' , ), 7, (7, (), [ (16393, 10, None, "IID('{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')") , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'GetPropertyDefinition' , 'Name' , 'retval' , ), 8, (8, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{2A69C05E-34EA-46FE-B44C-FE3A217D3C86}')") , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'CheckPropertyValue' , 'Name' , 'Value' , 'retval' , ), 9, (9, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
]

IDesignSearcherAutomation_vtables_dispatch_ = 1
IDesignSearcherAutomation_vtables_ = [
	(( 'Dump' , 'Directory' , 'retval' , ), 1, (1, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'DumpAll' , 'Directory' , 'retval' , ), 2, (2, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'DumpNoBusRippers' , 'Directory' , 'retval' , ), 3, (3, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Query' , 'Query' , 'ResultsFile' , 'retval' , ), 4, (4, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

IFramework_vtables_dispatch_ = 1
IFramework_vtables_ = [
	(( 'RunTcl' , 'tclCommand' , 'result' , ), 1, (1, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
]

IICTDocuments_vtables_dispatch_ = 1
IICTDocuments_vtables_ = [
	(( 'Open' , 'ICTName' , 'retval' , ), 1, (1, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{E947B7EF-5E39-42FD-A351-400BFEFCF49D}')") , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Close' , 'ICTName' , ), 2, (2, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'GetAvailableICTs' , 'AvailableICTs' , ), 3, (3, (), [ (16393, 10, None, "IID('{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')") , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'GetOpenedICTs' , 'OpenedICTs' , ), 4, (4, (), [ (16393, 10, None, "IID('{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')") , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'GetOpenedCount' , 'retval' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'GetOpenedItem' , 'Index' , 'retval' , ), 6, (6, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{E947B7EF-5E39-42FD-A351-400BFEFCF49D}')") , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IMGCDesignerDataManagement_vtables_dispatch_ = 1
IMGCDesignerDataManagement_vtables_ = [
	(( 'entities' , 'Type' , 'entities' , ), 1, (1, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{3C8285AF-A900-4537-B9BA-C44223D0B380}')") , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'RecentEntities' , 'entities' , ), 2, (2, (), [ (16393, 10, None, "IID('{3C8285AF-A900-4537-B9BA-C44223D0B380}')") , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'FindEntityByPath' , 'Path' , 'entity' , ), 3, (3, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{03BE5928-2002-4CCB-818D-775ED6115A41}')") , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Connect' , 'server_address' , 'server_port' , ), 4, (4, (), [ (8, 1, None, None) , 
			 (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'IsConnected' , 'Value' , ), 5, (5, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'AdditionalProperties' , 'Type' , 'AdditionalProperties' , ), 6, (6, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{4E66A337-C45F-4BEA-9089-3E64D3270531}')") , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'FindEntityByPathAndVersion' , 'Path' , 'Version' , 'entity' , ), 7, (7, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (16393, 10, None, "IID('{03BE5928-2002-4CCB-818D-775ED6115A41}')") , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Option' , 'Name' , 'Value' , ), 8, (8, (), [ (8, 1, None, None) , 
			 (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Option' , 'Name' , 'Value' , ), 8, (8, (), [ (8, 1, None, None) , 
			 (8, 0, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'OptionIsReadonly' , 'Name' , 'Value' , ), 9, (9, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'LastErrorMessage' , 'errorMessage' , ), 10, (10, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'ValidEntityTypes' , 'Type' , ), 11, (11, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'OpenComponentView' , 'partNumber' , ), 12, (12, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'OpenManagedBlockView' , 'Name' , 'Version' , ), 13, (13, (), [ (8, 1, None, None) , 
			 (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
]

IMGCDesignerDataManagementAdditionalProperties_vtables_dispatch_ = 1
IMGCDesignerDataManagementAdditionalProperties_vtables_ = [
	(( 'Count' , 'pCount' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Remove' , 'vIndex' , ), 2, (2, (), [ (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'vIndex' , 'additionalProperty' , ), 3, (3, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{787D1D50-FC6C-478A-84CB-2FD200799E22}')") , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'unknown' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 65 , )),
]

IMGCDesignerDataManagementAdditionalProperty_vtables_dispatch_ = 1
IMGCDesignerDataManagementAdditionalProperty_vtables_ = [
	(( 'Id' , 'propId' , ), 1, (1, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Label' , 'propLabel' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

IMGCDesignerDataManagementEntities_vtables_dispatch_ = 1
IMGCDesignerDataManagementEntities_vtables_ = [
	(( 'Count' , 'pCount' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Remove' , 'vIndex' , ), 2, (2, (), [ (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'vIndex' , 'project' , ), 3, (3, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{03BE5928-2002-4CCB-818D-775ED6115A41}')") , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'unknown' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 65 , )),
]

IMGCDesignerDataManagementEntity_vtables_dispatch_ = 1
IMGCDesignerDataManagementEntity_vtables_ = [
	(( 'Path' , 'Path' , ), 1, (1, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'Name' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'Type' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'AccessType' , 'AccessType' , ), 4, (4, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Status' , 'Status' , ), 5, (5, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Users' , 'Users' , ), 6, (6, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Version' , 'Version' , ), 7, (7, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'CheckedInDate' , 'CheckedInDate' , ), 8, (8, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'EditShared' , 'retval' , ), 9, (9, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'EditExclusive' , 'pSucc' , ), 10, (10, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'OpenReference' , ), 11, (11, (), [ ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'View' , 'retval' , ), 12, (12, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Export' , 'destination' , ), 13, (13, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'CheckIn' , 'comment' , ), 14, (14, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'LaunchWebView' , ), 15, (15, (), [ ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'AdditionalPropertyValue' , 'property' , 'Value' , ), 16, (16, (), [ (9, 1, None, "IID('{787D1D50-FC6C-478A-84CB-2FD200799E22}')") , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'PropertyValueById' , 'Id' , 'Value' , ), 25, (25, (), [ (8, 1, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'ProjectName' , 'ProjectName' , ), 17, (17, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'DumpProperties' , 'outputDirectory' , 'filter' , 'includeParents' , 'outputFilePath' , 
			 ), 18, (18, (), [ (8, 1, None, None) , (3, 49, '0', None) , (11, 49, 'False', None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'RunConfigurationRules' , 'detailsFilePath' , ), 19, (19, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'ViewForOutputsGeneration' , 'retval' , ), 20, (20, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'RelatedEntities' , 'types' , 'entities' , ), 21, (21, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{3C8285AF-A900-4537-B9BA-C44223D0B380}')") , ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'LocalPath' , 'Path' , ), 22, (22, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 64 , )),
	(( 'CancelEditing' , ), 23, (23, (), [ ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Unlock' , ), 24, (24, (), [ ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
]

IMergeData_vtables_dispatch_ = 1
IMergeData_vtables_ = [
	(( 'GetSourceLayers' , 'pSourceLayers' , ), 6, (6, (), [ (16393, 10, None, "IID('{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')") , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'GetAvailableTargetLayers' , 'pAvailableTargetLayers' , ), 7, (7, (), [ (16393, 10, None, "IID('{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')") , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'GetTargetLayer' , 'sSourceLayer' , 'sTargetLayer' , ), 8, (8, (), [ (8, 1, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'SetTargetLayer' , 'sSourceLayer' , 'sTargetLayer' , ), 9, (9, (), [ (8, 1, None, None) , 
			 (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'GetSourceGlobals' , 'pSourceGlobals' , ), 10, (10, (), [ (16393, 10, None, "IID('{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'GetAvailableTargetGlobals' , 'pAvailableTargetGlobals' , ), 11, (11, (), [ (16393, 10, None, "IID('{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')") , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'GetTargetGlobal' , 'sSourceGlobal' , 'sTargetGlobal' , ), 12, (12, (), [ (8, 1, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'SetTargetGlobal' , 'sSourceGlobal' , 'sTargetGlobal' , ), 13, (13, (), [ (8, 1, None, None) , 
			 (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'GetBusNames' , 'pBusNames' , ), 1, (1, (), [ (16393, 10, None, "IID('{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')") , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'GetSourceBusContents' , 'sBusName' , 'sSourceBusContents' , ), 2, (2, (), [ (8, 1, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'GetTargetBusContents' , 'sBusName' , 'sTargetBusContents' , ), 3, (3, (), [ (8, 1, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'SetBusContents' , 'sBusName' , 'sBusContents' , ), 4, (4, (), [ (8, 1, None, None) , 
			 (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'GetBusContents' , 'sBusName' , 'sBusContents' , ), 5, (5, (), [ (8, 1, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
]

IODProjectData_vtables_dispatch_ = 1
IODProjectData_vtables_ = [
	(( 'GetIODesignerFPGAs' , 'siCDBDesign' , 'listOfFPGAs' , ), 301, (301, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')") , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'SetIODesignerFPGAs' , 'listOfFPGAs' , 'siCDBDesign' , ), 302, (302, (), [ (9, 1, None, "IID('{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')") , 
			 (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

IPDBPartitions_vtables_dispatch_ = 1
IPDBPartitions_vtables_ = [
	(( 'GetPDBPartition' , 'Index' , 'siCDBDesign' , 'sItem' , ), 200, (200, (), [ 
			 (3, 1, None, None) , (8, 1, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'GetPDBPartitionsCount' , 'siCDBDesign' , 'lCount' , ), 201, (201, (), [ (8, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'GetPDBPartitionsArray' , 'siCDBDesign' , 'arrayOfPartitions' , ), 202, (202, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')") , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'InsertPDBPartition' , 'sPartition' , 'Index' , 'siCDBDesign' , ), 203, (203, (), [ 
			 (8, 1, None, None) , (3, 1, None, None) , (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'AppendPDBPartition' , 'sPartition' , 'siCDBDesign' , ), 204, (204, (), [ (8, 1, None, None) , 
			 (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'RemovePDBPartitionByName' , 'sPartition' , 'siCDBDesign' , ), 205, (205, (), [ (8, 1, None, None) , 
			 (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'RemovePDBPartitionByIndex' , 'Index' , 'siCDBDesign' , ), 206, (206, (), [ (3, 1, None, None) , 
			 (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'PDBPartitionExists' , 'sPartition' , 'siCDBDesign' , 'bExists' , ), 207, (207, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
]

IPredicate_vtables_dispatch_ = 1
IPredicate_vtables_ = [
]

IProjectData_vtables_dispatch_ = 1
IProjectData_vtables_ = [
	(( 'GetProjectPath' , 'sProjectPath' , ), 1, (1, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'GetProjectName' , 'sProjectName' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'GetProjectFilePath' , 'sProjectFilePath' , ), 3, (3, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'iCDBDir' , 'siCDBDir' , ), 4, (4, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'CentralLibraryPath' , 'sCentralLibraryPath' , ), 5, (5, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'CentralLibraryPath' , 'sCentralLibraryPath' , ), 5, (5, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'GetSnapshotName' , 'sSnapshotName' , ), 6, (6, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 64 , )),
	(( 'GetSymbolPartitions' , 'pPartitions' , ), 7, (7, (), [ (16393, 10, None, "IID('{8DE1FE34-146C-4C91-8B52-EE97F9292EEF}')") , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'GetiCDBDesigns' , 'arrayOfDesigns' , ), 9, (9, (), [ (16393, 10, None, "IID('{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')") , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'GetiCDBDesignType' , 'siCDBDesign' , 'siCDBDesignType' , ), 10, (10, (), [ (8, 1, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'SetiCDBDesignType' , 'siCDBDesignType' , 'siCDBDesign' , ), 11, (11, (), [ (8, 1, None, None) , 
			 (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'GetiCDBDesignRootBlock' , 'siCDBDesign' , 'siCDBDesignRootBlock' , ), 12, (12, (), [ (8, 1, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'SetiCDBDesignRootBlock' , 'siCDBDesignRootBlock' , 'siCDBDesign' , ), 13, (13, (), [ (8, 1, None, None) , 
			 (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'GetBordersFilePath' , 'resolveSoftPrefix' , 'sBordersFilePath' , ), 14, (14, (), [ (11, 1, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'SetBordersFilePath' , 'sBordersFilePath' , ), 15, (15, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'GetPinComponentsFilePath' , 'resolveSoftPrefix' , 'sPinComponentsFilePath' , ), 18, (18, (), [ (11, 1, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'SetPinComponentsFilePath' , 'sPinComponentsFilePath' , ), 19, (19, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'GetiCDBDiscardFilePath' , 'resolveSoftPrefix' , 'siCDBDiscardFilePath' , ), 20, (20, (), [ (11, 1, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'SetiCDBDiscardFilePath' , 'siCDBDiscardFilePath' , ), 21, (21, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'GetPDBPartitions' , 'pPartitions' , ), 22, (22, (), [ (16393, 10, None, "IID('{D17E5439-1B5A-40D5-A115-1E4656FB102B}')") , ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'GetSearchPathScheme' , 'siCDBDesign' , 'sSearchPathScheme' , ), 23, (23, (), [ (8, 1, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'SetSearchPathScheme' , 'sSearchPathScheme' , 'siCDBDesign' , ), 24, (24, (), [ (8, 1, None, None) , 
			 (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'GetiCDBServerName' , 'siCDBServerName' , ), 25, (25, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 64 , )),
	(( 'SetiCDBServerName' , 'siCDBServerName' , ), 26, (26, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 64 , )),
	(( 'GetiCDBServerPortsFilePath' , 'resolveSoftPrefix' , 'siCDBServerPortsFilePath' , ), 27, (27, (), [ (11, 1, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 64 , )),
	(( 'SetiCDBServerPortsFilePath' , 'siCDBServerPortsFilePath' , ), 28, (28, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 256 , (3, 0, None, None) , 64 , )),
	(( 'GetBusContentsFilePath' , 'resolveSoftPrefix' , 'sBusContentsFilePath' , ), 29, (29, (), [ (11, 1, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'SetBusContentsFilePath' , 'sBusContentsFilePath' , ), 30, (30, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'GetFrontEndSnapshot' , 'sFrontEndSnapshot' , ), 31, (31, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 280 , (3, 0, None, None) , 64 , )),
	(( 'SetFrontEndSnapshot' , 'sFrontEndSnapshot' , ), 32, (32, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'GetPCBDesignPath' , 'siCDBDesign' , 'resolveSoftPrefix' , 'sPCBDesignPath' , ), 33, (33, (), [ 
			 (8, 1, None, None) , (11, 1, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'SetPCBDesignPath' , 'sPCBDesignPath' , 'siCDBDesign' , ), 34, (34, (), [ (8, 1, None, None) , 
			 (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'GetIODProjectData' , 'pIODProjectData' , ), 35, (35, (), [ (16393, 10, None, "IID('{3D2B940D-C2B5-440E-AB57-E8C6F3FB34C9}')") , ], 1 , 1 , 4 , 0 , 312 , (3, 0, None, None) , 64 , )),
	(( 'AddiCDBDesign' , 'sTopBlockName' , 'result' , ), 36, (36, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'RemoveiCDBDesign' , 'sTopBlockName' , 'result' , ), 37, (37, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'RenameiCDBDesign' , 'sOldName' , 'sNewName' , 'result' , ), 38, (38, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'GetFlowType' , 'sFlowType' , ), 39, (39, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 344 , (3, 0, None, None) , 64 , )),
	(( 'SetFlowType' , 'sFlowType' , ), 40, (40, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 352 , (3, 0, None, None) , 64 , )),
	(( 'GetSlotsCount' , 'sPartitionName' , 'sSymbolName' , 'sPartNumber' , 'lSlotCount' , 
			 ), 41, (41, (), [ (8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 360 , (3, 0, None, None) , 64 , )),
	(( 'GetPinNumbers' , 'sPartitionName' , 'sSymbolName' , 'sPartNumber' , 'lSlot' , 
			 'pPinNumbers' , ), 42, (42, (), [ (8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , 
			 (3, 1, None, None) , (16393, 10, None, "IID('{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')") , ], 1 , 1 , 4 , 0 , 368 , (3, 0, None, None) , 64 , )),
	(( 'UpdateOtherObjects' , 'eWhatToUpdate' , 'eUpdateScope' , ), 43, (43, (), [ (3, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'GetNetlistLibCount' , 'nCount' , ), 44, (44, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 384 , (3, 0, None, None) , 64 , )),
	(( 'GetNetlistLib' , 'nPos' , 'pVdLib' , ), 45, (45, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{28D40DF1-22F3-11D0-91AB-58F3E7000000}')") , ], 1 , 1 , 4 , 0 , 392 , (3, 0, None, None) , 64 , )),
	(( 'FindNetlistLibPos' , 'sAlias' , 'nPos' , ), 46, (46, (), [ (8, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 400 , (3, 0, None, None) , 64 , )),
	(( 'RemoveNetlistLib' , 'nPos' , 'bRemoved' , ), 47, (47, (), [ (3, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 408 , (3, 0, None, None) , 64 , )),
	(( 'AddNetlistLib' , 'nAtPos' , 'sAlias' , 'sPath' , 'Type' , 
			 'bAdded' , ), 48, (48, (), [ (3, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , 
			 (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 416 , (3, 0, None, None) , 64 , )),
	(( 'SaveNetlistLibs' , ), 49, (49, (), [ ], 1 , 1 , 4 , 0 , 424 , (3, 0, None, None) , 64 , )),
]

IRipper_vtables_dispatch_ = 1
IRipper_vtables_ = [
	(( 'GetConnectedObject' , 'Net' , 'retval' , ), 1, (1, (), [ (9, 1, None, "IID('{AE729492-9683-11CE-8246-00001B4D36B5}')") , 
			 (16393, 10, None, "IID('{AE729492-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'GetConnectedObjects' , 'retval' , ), 2, (2, (), [ (16393, 10, None, "IID('{BD2EDF77-7E28-11CE-822D-00001B4D36B7}')") , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'GetMappedSignal' , 'Net' , 'sSignal' , 'retval' , ), 3, (3, (), [ 
			 (9, 1, None, "IID('{AE729492-9683-11CE-8246-00001B4D36B5}')") , (8, 1, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IStringCollection_vtables_dispatch_ = 1
IStringCollection_vtables_ = [
	(( 'Count' , 'retval' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Index' , 'retval' , ), 2, (2, (), [ (3, 1, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Remove' , 'Index' , ), 3, (3, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IStringList_vtables_dispatch_ = 1
IStringList_vtables_ = [
	(( 'GetCount' , 'lCount' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'GetItem' , 'Index' , 'sItem' , ), 2, (2, (), [ (3, 1, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Append' , 'sItem' , ), 3, (3, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Insert' , 'sItem' , 'Index' , ), 4, (4, (), [ (8, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Remove' , 'Index' , ), 5, (5, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Clear' , ), 6, (6, (), [ ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

ISymbolPartitions_vtables_dispatch_ = 1
ISymbolPartitions_vtables_ = [
	(( 'GetSymbolPartition' , 'Index' , 'siCDBDesign' , 'sItem' , ), 100, (100, (), [ 
			 (3, 1, None, None) , (8, 1, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'GetSymbolPartitionsCount' , 'siCDBDesign' , 'lCount' , ), 101, (101, (), [ (8, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'GetSymbolPartitionsArray' , 'siCDBDesign' , 'arrayOfPartitions' , ), 102, (102, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')") , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'InsertSymbolPartition' , 'sPartition' , 'Index' , 'siCDBDesign' , ), 103, (103, (), [ 
			 (8, 1, None, None) , (3, 1, None, None) , (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'AppendSymbolPartition' , 'sPartition' , 'siCDBDesign' , ), 104, (104, (), [ (8, 1, None, None) , 
			 (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'RemoveSymbolPartitionByName' , 'sPartition' , 'siCDBDesign' , ), 105, (105, (), [ (8, 1, None, None) , 
			 (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'RemoveSymbolPartitionByIndex' , 'Index' , 'siCDBDesign' , ), 106, (106, (), [ (3, 1, None, None) , 
			 (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'SymbolPartitionExists' , 'sPartition' , 'siCDBDesign' , 'bExists' , ), 107, (107, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
]

IVdApp_vtables_dispatch_ = 1
IVdApp_vtables_ = [
	(( 'Documents' , 'retval' , ), 1, (1, (), [ (16393, 10, None, "IID('{BD2EDF77-7E28-11CE-822D-00001B4D36B5}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 64 , )),
	(( 'Visible' , 'retval' , ), 204, (204, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Visible' , 'retval' , ), 204, (204, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Application' , 'retval' , ), 3, (3, (), [ (16393, 10, None, "IID('{EA4ABD71-84B0-11CE-8237-00001B4D36B5}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 64 , )),
	(( 'FullName' , 'retval' , ), 4, (4, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 64 , )),
	(( 'Name' , 'retval' , ), 5, (5, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 64 , )),
	(( 'Parent' , 'retval' , ), 6, (6, (), [ (16393, 10, None, "IID('{EA4ABD71-84B0-11CE-8237-00001B4D36B5}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 64 , )),
	(( 'Interactive' , 'retval' , ), 205, (205, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Interactive' , 'retval' , ), 205, (205, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'ActiveView' , 'retval' , ), 207, (207, (), [ (16393, 10, None, "IID('{0892A013-86BC-11CE-8238-00001B4D36B5}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'ClientAdvisorFlags' , 'retval' , ), 9, (9, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 64 , )),
	(( 'ClientAdvisorFlags' , 'retval' , ), 9, (9, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 64 , )),
	(( 'ActiveViewHandle' , 'retval' , ), 40, (40, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 64 , )),
	(( 'CommandBars' , 'retval' , ), 215, (215, (), [ (16393, 10, None, "IID('{91818215-A01E-11D2-8F30-0060B0EF0A25}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'StatusBarText' , 'retval' , ), 206, (206, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'StatusBarText' , 'retval' , ), 206, (206, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'BusyCursor' , 'retval' , ), 61, (61, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 64 , )),
	(( 'BusyCursor' , 'retval' , ), 61, (61, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 64 , )),
	(( 'Version' , 'retval' , ), 209, (209, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Addins' , 'retval' , ), 216, (216, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'OptionLevel' , 'retval' , ), 73, (73, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 64 , )),
	(( 'CommandLineArguments' , 'retval' , ), 210, (210, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Quit' , ), 226, (226, (), [ ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'SetClientAdvisor' , 'Advisor' , 'Flags' , 'retval' , ), 11, (11, (), [ 
			 (9, 1, None, None) , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 64 , )),
	(( 'ParamSetValue' , 'Index' , 'NewValue' , ), 12, (12, (), [ (3, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'ParamGetValue' , 'Index' , 'retval' , ), 13, (13, (), [ (3, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'ParamGetMode' , 'Index' , 'retval' , ), 14, (14, (), [ (3, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'ParamSetMode' , 'Index' , 'NewValue' , ), 15, (15, (), [ (3, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'GetLastErrorString' , 'retval' , ), 239, (239, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 280 , (3, 0, None, None) , 64 , )),
	(( 'GetLastErrorId' , 'retval' , ), 240, (240, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 288 , (3, 0, None, None) , 64 , )),
	(( 'SetEnvVariable' , 'pName' , 'pValue' , 'retval' , ), 211, (211, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 296 , (3, 0, None, None) , 64 , )),
	(( 'Initialize' , 'WDIRPath' , 'LicensePath' , 'retval' , ), 203, (203, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'GetTypeFromIDispatch' , 'Dispatch' , 'retval' , ), 20, (20, (), [ (9, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 312 , (3, 0, None, None) , 64 , )),
	(( 'UserControl' , 'retval' , ), 21, (21, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 320 , (3, 0, None, None) , 64 , )),
	(( 'Guid' , 'retval' , ), 22, (22, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 328 , (3, 0, None, None) , 64 , )),
	(( 'Activate' , ), 201, (201, (), [ ], 1 , 1 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'ExecuteCommand' , 'CommandString' , 'retval' , ), 29, (29, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 344 , (3, 0, None, None) , 64 , )),
	(( 'RegisterOLECommand' , 'CommandName' , 'CommandDescription' , 'bModifiesData' , 'pDispatch' , 
			 'retval' , ), 33, (33, (), [ (8, 1, None, None) , (8, 1, None, None) , (11, 1, None, None) , 
			 (9, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 352 , (3, 0, None, None) , 64 , )),
	(( 'UnregisterOLECommand' , 'CommandName' , 'ClientDispatch' , 'retval' , ), 36, (36, (), [ 
			 (8, 1, None, None) , (9, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 360 , (3, 0, None, None) , 64 , )),
	(( 'DataObjExists' , 'Library' , 'Name' , 'Extension' , 'Class' , 
			 'retval' , ), 37, (37, (), [ (8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , 
			 (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 368 , (3, 0, None, None) , 64 , )),
	(( 'DataObjGetPath' , 'Library' , 'Name' , 'Extension' , 'Class' , 
			 'retval' , ), 38, (38, (), [ (8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , 
			 (3, 1, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 376 , (3, 0, None, None) , 64 , )),
	(( 'ParamAddListName' , 'which_param' , 'new_name' , ), 39, (39, (), [ (3, 1, None, None) , 
			 (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 384 , (3, 0, None, None) , 64 , )),
	(( 'CommandEnable' , 'CommandName' , 'retval' , ), 42, (42, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 392 , (3, 0, None, None) , 64 , )),
	(( 'CommandDisable' , 'CommandName' , 'retval' , ), 43, (43, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 400 , (3, 0, None, None) , 64 , )),
	(( 'CommandRemove' , 'CommandName' , 'retval' , ), 44, (44, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 408 , (3, 0, None, None) , 64 , )),
	(( 'QueryBlocks' , 'BlockType' , 'Library' , 'retval' , ), 45, (45, (), [ 
			 (3, 1, None, None) , (8, 1, None, None) , (16393, 10, None, "IID('{BD2EDF77-7E28-11CE-822D-00001B4D36B7}')") , ], 1 , 1 , 4 , 0 , 416 , (3, 0, None, None) , 64 , )),
	(( 'QueryPages' , 'Name' , 'retval' , ), 46, (46, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{BD2EDF77-7E28-11CE-822D-00001B4D36B7}')") , ], 1 , 1 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'SetLibFileNew' , 'DirPath' , 'retval' , ), 47, (47, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 432 , (3, 0, None, None) , 64 , )),
	(( 'SetLibFileOpen' , 'DirPath' , 'retval' , ), 48, (48, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 440 , (3, 0, None, None) , 64 , )),
	(( 'SetLibAddComp' , 'DirPath' , 'retval' , ), 49, (49, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 448 , (3, 0, None, None) , 64 , )),
	(( 'DesignBlocks' , 'Library' , 'Name' , 'SheetNumber' , 'LevelString' , 
			 'RecurseDown' , 'retval' , ), 50, (50, (), [ (8, 1, None, None) , (8, 1, None, None) , 
			 (8, 1, None, None) , (8, 1, None, None) , (11, 1, None, None) , (16393, 10, None, "IID('{BD2EDF77-7E28-11CE-822D-00001B4D36B7}')") , ], 1 , 1 , 4 , 0 , 456 , (3, 0, None, None) , 64 , )),
	(( 'SetViewAnalogFlag' , 'state' , ), 52, (52, (), [ (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 464 , (3, 0, None, None) , 64 , )),
	(( 'ReadIni' , 'Inifilename' , 'retval' , ), 202, (202, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 472 , (3, 0, None, None) , 64 , )),
	(( 'DesignPaths' , 'Library' , 'Name' , 'LevelString' , 'RecurseDown' , 
			 'retval' , ), 54, (54, (), [ (8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , 
			 (11, 1, None, None) , (16393, 10, None, "IID('{7BB17D63-FAE6-11D1-BE10-00A0C9204FDC}')") , ], 1 , 1 , 4 , 0 , 480 , (3, 0, None, None) , 64 , )),
	(( 'TextViews' , 'retval' , ), 57, (57, (), [ (16393, 10, None, None) , ], 1 , 1 , 4 , 0 , 488 , (3, 0, None, None) , 64 , )),
	(( 'Bindings' , 'BindingTable' , 'retval' , ), 219, (219, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{A73EBAD3-B3F1-11D2-99AE-00A0C966477E}')") , ], 1 , 1 , 4 , 0 , 496 , (3, 0, None, None) , 64 , )),
	(( 'DesignComponents' , 'Library' , 'Name' , 'EndSheet' , 'LevelString' , 
			 'RecurseDown' , 'retval' , ), 59, (59, (), [ (8, 1, None, None) , (8, 1, None, None) , 
			 (8, 49, "''", None) , (8, 49, "''", None) , (11, 49, 'True', None) , (16393, 10, None, "IID('{BD2EDF77-7E28-11CE-822D-00001B4D36B7}')") , ], 1 , 1 , 4 , 0 , 504 , (3, 32, None, None) , 0 , )),
	(( 'SelectPath' , 'FileName' , 'HierPath' , 'SheetNumber' , 'Type' , 
			 'AddSelected' , 'SearchBus' , 'retval' , ), 67, (67, (), [ (8, 1, None, None) , 
			 (8, 1, None, None) , (8, 1, None, None) , (3, 1, None, None) , (11, 1, None, None) , (11, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 512 , (3, 0, None, None) , 0 , )),
	(( 'SelectPathCompPin' , 'FileName' , 'HierPath' , 'SheetNumber' , 'PinNumber' , 
			 'SelectType' , 'retval' , ), 68, (68, (), [ (8, 1, None, None) , (8, 1, None, None) , 
			 (8, 1, None, None) , (8, 1, None, None) , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
	(( 'PushPath' , 'Top' , 'HierPath' , 'SheetNumber' , 'retval' , 
			 ), 69, (69, (), [ (8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 528 , (3, 0, None, None) , 0 , )),
	(( 'PrintProject' , 'DesignName' , 'LevelStrings' , 'PrintSymbols' , 'ShowOrderDialog' , 
			 'PPOFile' , ), 221, (221, (), [ (8, 1, None, None) , (8, 1, None, None) , (11, 1, None, None) , 
			 (11, 1, None, None) , (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 536 , (3, 0, None, None) , 0 , )),
	(( 'SetRedraw' , 'Redraw' , ), 222, (222, (), [ (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 544 , (3, 0, None, None) , 0 , )),
	(( 'BrowseForSymbol' , 'OnlyBorders' , 'Title' , 'retval' , ), 72, (72, (), [ 
			 (11, 1, None, None) , (8, 1, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 552 , (3, 0, None, None) , 64 , )),
	(( 'InsertSheet' , 'DesignName' , 'SheetNumber' , 'retval' , ), 75, (75, (), [ 
			 (8, 1, None, None) , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 560 , (3, 0, None, None) , 64 , )),
	(( 'DeleteSheet' , 'DesignName' , 'SheetNumber' , 'retval' , ), 76, (76, (), [ 
			 (8, 1, None, None) , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 568 , (3, 0, None, None) , 64 , )),
	(( 'PreviewDecal' , 'DecalName' , 'retval' , ), 78, (78, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 576 , (3, 0, None, None) , 64 , )),
	(( 'GetClassDefinitions' , 'CreateIfNotDefined' , 'retval' , ), 79, (79, (), [ (11, 1, None, None) , 
			 (16393, 10, None, None) , ], 1 , 1 , 4 , 0 , 584 , (3, 0, None, None) , 64 , )),
	(( 'UnloadClassDefinitions' , ), 81, (81, (), [ ], 1 , 1 , 4 , 0 , 592 , (3, 0, None, None) , 64 , )),
	(( 'OpenBlocks' , 'BlockType' , 'retval' , ), 82, (82, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{BD2EDF77-7E28-11CE-822D-00001B4D36B7}')") , ], 1 , 1 , 4 , 0 , 600 , (3, 0, None, None) , 0 , )),
	(( 'Query' , 'Flags' , 'Selected' , 'retval' , ), 83, (83, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (16393, 10, None, "IID('{BD2EDF77-7E28-11CE-822D-00001B4D36B7}')") , ], 1 , 1 , 4 , 0 , 608 , (3, 0, None, None) , 0 , )),
	(( 'ParamGetListNames' , 'which_param' , 'retval' , ), 84, (84, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{7BB17D63-FAE6-11D1-BE10-00A0C9204FDC}')") , ], 1 , 1 , 4 , 0 , 616 , (3, 0, None, None) , 64 , )),
	(( 'AnnoDisplayTime' , 'Context' , 'Position' , 'Timestring' , ), 85, (85, (), [ 
			 (8, 1, None, None) , (3, 1, None, None) , (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 624 , (3, 0, None, None) , 64 , )),
	(( 'AnnoDisplayValue' , 'Context' , 'DesignPath' , 'AnnType' , 'AnnObject' , 
			 'ObjName' , 'ObjValue' , ), 86, (86, (), [ (8, 1, None, None) , (8, 1, None, None) , 
			 (3, 1, None, None) , (3, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 632 , (3, 0, None, None) , 64 , )),
	(( 'SourceDocuments' , 'retval' , ), 214, (214, (), [ (16393, 10, None, "IID('{AC6510A1-83C5-4486-9154-CE74592F9A48}')") , ], 1 , 2 , 4 , 0 , 640 , (3, 0, None, None) , 0 , )),
	(( 'ExecuteMenuCommand' , 'command_name' , ), 89, (89, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 648 , (3, 0, None, None) , 64 , )),
	(( 'SilentMode' , 'retval' , ), 250, (250, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 656 , (3, 0, None, None) , 0 , )),
	(( 'SilentMode' , 'retval' , ), 250, (250, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 664 , (3, 0, None, None) , 0 , )),
	(( 'LicenseMode' , 'retval' , ), 91, (91, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 672 , (3, 0, None, None) , 64 , )),
	(( 'ShellCmd' , 'retval' , ), 218, (218, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 680 , (3, 0, None, None) , 0 , )),
	(( 'OpenURL' , 'URL' , ), 225, (225, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 688 , (3, 0, None, None) , 0 , )),
	(( 'Cookies' , 'retval' , ), 94, (94, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 696 , (3, 0, None, None) , 64 , )),
	(( 'ActiveDocument' , 'retval' , ), 208, (208, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 704 , (3, 0, None, None) , 0 , )),
	(( 'AppendOutput' , 'TabName' , 'String' , ), 223, (223, (), [ (8, 1, None, None) , 
			 (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 712 , (3, 0, None, None) , 0 , )),
	(( 'HTMLDocuments' , 'retval' , ), 213, (213, (), [ (16393, 10, None, "IID('{7D50CA6D-07DB-4BE0-AD95-563DED3F9157}')") , ], 1 , 2 , 4 , 0 , 720 , (3, 0, None, None) , 64 , )),
	(( 'QueueSelectEvents' , 'bQueue' , ), 224, (224, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 728 , (3, 0, None, None) , 0 , )),
	(( 'QueueSelectEvents' , 'bQueue' , ), 224, (224, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 736 , (3, 0, None, None) , 0 , )),
	(( 'CurrentProject' , 'retval' , ), 55, (55, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 744 , (3, 0, None, None) , 64 , )),
	(( 'CurrentProject' , 'retval' , ), 55, (55, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 752 , (3, 0, None, None) , 64 , )),
	(( '_GetCurrentProject' , 'retval' , ), 31, (31, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 760 , (3, 0, None, None) , 64 , )),
	(( '_SetCurrentProject' , 'ProjectFilename' , ), 32, (32, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 768 , (3, 0, None, None) , 64 , )),
	(( '_GetPrimaryDirectory' , 'retval' , ), 35, (35, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 776 , (3, 0, None, None) , 64 , )),
	(( 'PrimaryDirectory' , 'retval' , ), 56, (56, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 784 , (3, 0, None, None) , 64 , )),
	(( 'ObjectColor' , 'ObjectType' , 'retval' , ), 65, (65, (), [ (3, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 792 , (3, 0, None, None) , 64 , )),
	(( 'ObjectColor' , 'ObjectType' , 'retval' , ), 65, (65, (), [ (3, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 800 , (3, 0, None, None) , 64 , )),
	(( 'ViewBaseSession' , 'retval' , ), 64, (64, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 808 , (3, 0, None, None) , 64 , )),
	(( 'SynchronizesViewBase' , 'retval' , ), 66, (66, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 816 , (3, 0, None, None) , 64 , )),
	(( 'SynchronizesViewBase' , 'retval' , ), 66, (66, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 824 , (3, 0, None, None) , 64 , )),
	(( 'KickViewbase' , 'ForceReload' , ), 97, (97, (), [ (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 832 , (3, 0, None, None) , 64 , )),
	(( 'IsLibDeletable' , 'Position' , 'retval' , ), 24, (24, (), [ (3, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 840 , (3, 0, None, None) , 64 , )),
	(( 'AddLibrary' , 'LibraryPath' , 'LibraryAlias' , 'LibraryAccess' , 'Position' , 
			 'retval' , ), 25, (25, (), [ (8, 1, None, None) , (8, 1, None, None) , (3, 1, None, None) , 
			 (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 848 , (3, 0, None, None) , 64 , )),
	(( 'DeleteLibrary' , 'Position' , 'retval' , ), 26, (26, (), [ (3, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 856 , (3, 0, None, None) , 64 , )),
	(( 'MoveLibrary' , 'FromPosition' , 'ToPosition' , 'retval' , ), 27, (27, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 864 , (3, 0, None, None) , 64 , )),
	(( 'ClearAllLibraries' , 'retval' , ), 28, (28, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 872 , (3, 0, None, None) , 64 , )),
	(( 'GetLibraries' , 'retval' , ), 30, (30, (), [ (16393, 10, None, "IID('{BD2EDF77-7E28-11CE-822D-00001B4D36B7}')") , ], 1 , 1 , 4 , 0 , 880 , (3, 0, None, None) , 64 , )),
	(( 'AddLibraryAndSaveIni' , 'LibraryPath' , 'LibraryAlias' , 'LibraryAccess' , 'Position' , 
			 'retval' , ), 104, (104, (), [ (8, 1, None, None) , (8, 1, None, None) , (3, 1, None, None) , 
			 (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 888 , (3, 0, None, None) , 64 , )),
	(( 'DeleteLibraryAndSaveIni' , 'Position' , 'retval' , ), 105, (105, (), [ (3, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 896 , (3, 0, None, None) , 64 , )),
	(( 'MoveLibraryAndSaveIni' , 'FromPosition' , 'ToPosition' , 'retval' , ), 106, (106, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 904 , (3, 0, None, None) , 64 , )),
	(( 'SaveIni' , 'retval' , ), 34, (34, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 912 , (3, 0, None, None) , 64 , )),
	(( 'RemoveProjectSettingTab' , 'TabIndicator' , ), 51, (51, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 920 , (3, 0, None, None) , 64 , )),
	(( 'AttributeCanHaveOatValue' , 'AttributeName' , 'retval' , ), 74, (74, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 928 , (3, 0, None, None) , 64 , )),
	(( 'AttributeValueMustBeUpper' , 'AttributeName' , 'retval' , ), 77, (77, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 936 , (3, 0, None, None) , 64 , )),
	(( 'Flows' , 'retval' , ), 98, (98, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 944 , (3, 0, None, None) , 64 , )),
	(( 'ProjMan' , 'retval' , ), 88, (88, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 952 , (3, 0, None, None) , 64 , )),
	(( 'project' , 'retval' , ), 101, (101, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 960 , (3, 0, None, None) , 64 , )),
	(( 'CnsFileString' , 'retval' , ), 102, (102, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 968 , (3, 0, None, None) , 64 , )),
	(( 'MakeReusableBlock' , 'ProjectName' , 'SchematicRoot' , 'DestDir' , 'RBName' , 
			 ), 103, (103, (), [ (8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 976 , (3, 0, None, None) , 64 , )),
	(( 'CheckIfNavigatorAddinsOpen' , 'retval' , ), 107, (107, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 984 , (3, 0, None, None) , 64 , )),
	(( 'CloseNavigatorAddins' , ), 108, (108, (), [ ], 1 , 1 , 4 , 0 , 992 , (3, 0, None, None) , 64 , )),
	(( 'GetProjectData' , 'retval' , ), 228, (228, (), [ (16393, 10, None, "IID('{956DD308-D5ED-40A1-83F2-84113B8937C1}')") , ], 1 , 1 , 4 , 0 , 1000 , (3, 0, None, None) , 0 , )),
	(( 'SchematicSheetDocuments' , 'retval' , ), 212, (212, (), [ (16393, 10, None, "IID('{608CA7F4-A52A-4206-9580-3BEB17CE0073}')") , ], 1 , 1 , 4 , 0 , 1008 , (3, 0, None, None) , 0 , )),
	(( 'CommandsManager' , 'retval' , ), 220, (220, (), [ (16393, 10, None, "IID('{AA7F70A6-2F0E-417C-A1D2-C1621D728EB0}')") , ], 1 , 1 , 4 , 0 , 1016 , (3, 0, None, None) , 0 , )),
	(( 'GetCommonPropertyManager' , 'retval' , ), 243, (243, (), [ (16393, 10, None, "IID('{E8758B51-DEBB-46FD-A192-962B14F57FA4}')") , ], 1 , 1 , 4 , 0 , 1024 , (3, 0, None, None) , 64 , )),
	(( 'OpenProject' , 'ProjectPath' , 'retval' , ), 227, (227, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1032 , (3, 0, None, None) , 0 , )),
	(( 'NewProject' , 'ProjectPath' , 'CentralLibraryPath' , 'ServerName' , 'ProjectTemplatePath' , 
			 'retval' , ), 251, (251, (), [ (8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , 
			 (8, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1040 , (3, 0, None, None) , 0 , )),
	(( 'GetActiveDesign' , 'sActiveiCDBDesign' , ), 229, (229, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 1048 , (3, 0, None, None) , 0 , )),
	(( 'GetFramework' , 'retval' , ), 242, (242, (), [ (16393, 10, None, "IID('{77CD6602-703B-4AFA-A4C1-B1652A257F15}')") , ], 1 , 1 , 4 , 0 , 1056 , (3, 0, None, None) , 64 , )),
	(( 'GetConfigurationProperty' , 'Name' , 'val' , ), 244, (244, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')") , ], 1 , 1 , 4 , 0 , 1064 , (3, 0, None, None) , 64 , )),
	(( 'SetConfigurationProperty' , 'Name' , 'val' , ), 245, (245, (), [ (8, 1, None, None) , 
			 (9, 1, None, "IID('{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')") , ], 1 , 1 , 4 , 0 , 1072 , (3, 0, None, None) , 64 , )),
	(( 'StartMigration' , 'ProjectPath' , 'CentralLibPath' , 'retval' , ), 246, (246, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1080 , (3, 0, None, None) , 0 , )),
	(( 'EnableEEVMMode' , 'eevmDataFile' , ), 247, (247, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 1088 , (3, 0, None, None) , 64 , )),
	(( 'ClearEEVMMode' , ), 248, (248, (), [ ], 1 , 1 , 4 , 0 , 1096 , (3, 0, None, None) , 64 , )),
	(( 'IsEEVMModeEnabled' , 'bEnabled' , ), 249, (249, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1104 , (3, 0, None, None) , 64 , )),
	(( 'ConvertSymbol' , 'sSymbol' , 'retval' , ), 252, (252, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1112 , (3, 0, None, None) , 64 , )),
	(( 'SetButtonBitmap' , 'CommandID' , 'BitmapFilePath' , 'retval' , ), 253, (253, (), [ 
			 (19, 1, None, None) , (8, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1120 , (3, 0, None, None) , 64 , )),
	(( 'SetButtonResourceDLL' , 'CommandID' , 'DllFilePath' , 'resID' , 'retval' , 
			 ), 254, (254, (), [ (19, 1, None, None) , (8, 1, None, None) , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1128 , (3, 0, None, None) , 64 , )),
	(( 'CreateToolbar' , 'Name' , 'retval' , ), 255, (255, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1136 , (3, 0, None, None) , 64 , )),
	(( 'DeleteBlock' , 'Name' , 'retval' , ), 256, (256, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1144 , (3, 0, None, None) , 64 , )),
	(( 'FireCentralLibraryReload' , ), 257, (257, (), [ ], 1 , 1 , 4 , 0 , 1152 , (3, 0, None, None) , 64 , )),
	(( 'GetICTContents' , 'ICTName' , 'outputFilePath' , 'retval' , ), 258, (258, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1160 , (3, 0, None, None) , 64 , )),
	(( 'GetICTDocuments' , 'retval' , ), 259, (259, (), [ (16393, 10, None, "IID('{2A3CCA57-9C38-4484-A6A3-7521DDF7DAD0}')") , ], 1 , 1 , 4 , 0 , 1168 , (3, 0, None, None) , 64 , )),
	(( 'SetDefaultColor' , 'ObjectType' , 'Color' , ), 260, (260, (), [ (3, 1, None, None) , 
			 (9, 1, None, "IID('{C1031A0C-15BD-4897-A3E5-4C615CDEA684}')") , ], 1 , 1 , 4 , 0 , 1176 , (3, 0, None, None) , 0 , )),
	(( 'GetDefaultColor' , 'ObjectType' , 'retval' , ), 261, (261, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{C1031A0C-15BD-4897-A3E5-4C615CDEA684}')") , ], 1 , 1 , 4 , 0 , 1184 , (3, 0, None, None) , 0 , )),
	(( 'ToolbarAction' , 'Handle' , 'Msg' , 'wParam' , 'lParam' , 
			 'retval' , ), 262, (262, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , 
			 (3, 1, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 1192 , (3, 0, None, None) , 64 , )),
	(( 'LaunchSymbolEditor' , 'sSymbolName' , ), 263, (263, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 1200 , (3, 0, None, None) , 64 , )),
	(( 'ExportForeignDatabase' , 'sPath' , 'retval' , ), 264, (264, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1208 , (3, 0, None, None) , 64 , )),
	(( 'ImportForeignDatabase' , 'sPath' , 'retval' , ), 265, (265, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1216 , (3, 0, None, None) , 64 , )),
	(( 'SelectComponent' , 'sSchName' , 'sSheetName' , 'sCompUID' , 'retval' , 
			 ), 266, (266, (), [ (8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1224 , (3, 0, None, None) , 64 , )),
	(( 'SelectNet' , 'sSchName' , 'sSheetName' , 'sNetUID' , 'retval' , 
			 ), 267, (267, (), [ (8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1232 , (3, 0, None, None) , 64 , )),
	(( 'GetProtectionProxy' , 'retval' , ), 268, (268, (), [ (16393, 10, None, "IID('{8E0609DD-208C-42B6-A1B0-00DAA3E45423}')") , ], 1 , 1 , 4 , 0 , 1240 , (3, 0, None, None) , 64 , )),
	(( 'ActiveICTView' , 'retval' , ), 269, (269, (), [ (16393, 10, None, "IID('{848E324F-125D-4236-981D-0EB202E628DA}')") , ], 1 , 2 , 4 , 0 , 1248 , (3, 0, None, None) , 0 , )),
	(( 'RunDesignIntegrityChecks' , 'bNewPass' , 'bRetval' , ), 270, (270, (), [ (11, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1256 , (3, 0, None, None) , 64 , )),
	(( 'EnableSelectionBroadcast' , ), 271, (271, (), [ ], 1 , 1 , 4 , 0 , 1264 , (3, 0, None, None) , 64 , )),
	(( 'DisableSelectionBroadcast' , ), 272, (272, (), [ ], 1 , 1 , 4 , 0 , 1272 , (3, 0, None, None) , 64 , )),
	(( 'AddAddin' , 'pAddinInfo' , 'bRetval' , ), 273, (273, (), [ (9, 1, None, "IID('{9D83C992-3682-4D94-9727-EFBB5C0FB74C}')") , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1280 , (3, 0, None, None) , 0 , )),
	(( 'CloseProject' , 'bRetval' , ), 274, (274, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1288 , (3, 0, None, None) , 0 , )),
	(( 'ExtractPCB' , 'sPath' , 'sDetailedWiring' , 'retval' , ), 275, (275, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1296 , (3, 0, None, None) , 64 , )),
	(( 'DesignNets' , 'Library' , 'Name' , 'EndSheet' , 'LevelString' , 
			 'RecurseDown' , 'retval' , ), 276, (276, (), [ (8, 1, None, None) , (8, 1, None, None) , 
			 (8, 49, "''", None) , (8, 49, "''", None) , (11, 49, 'True', None) , (16393, 10, None, "IID('{BD2EDF77-7E28-11CE-822D-00001B4D36B7}')") , ], 1 , 1 , 4 , 0 , 1304 , (3, 32, None, None) , 0 , )),
	(( 'SetGenericStatusIndicatorState' , 'eIndicatorColor' , 'sToolTipText' , 'retval' , ), 277, (277, (), [ 
			 (3, 1, None, None) , (8, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1312 , (3, 0, None, None) , 64 , )),
	(( 'QueueDatabaseUpdates' , 'bQueue' , ), 278, (278, (), [ (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 1320 , (3, 0, None, None) , 64 , )),
	(( 'SheetsEditMode' , 'retval' , ), 279, (279, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 1328 , (3, 0, None, None) , 64 , )),
	(( 'SheetsEditMode' , 'retval' , ), 279, (279, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 1336 , (3, 0, None, None) , 64 , )),
	(( 'ExportSymbol' , 'sSymbolName' , 'sTargetDir' , 'retval' , ), 280, (280, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1344 , (3, 0, None, None) , 0 , )),
	(( 'EDXEngine' , 'retval' , ), 281, (281, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 1352 , (3, 0, None, None) , 64 , )),
	(( 'UpdateMenuBar' , 'menuBarParentWnd' , 'hMenu' , 'retval' , ), 282, (282, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 1360 , (3, 0, None, None) , 64 , )),
	(( 'GetPEFlowMode' , 'retval' , ), 283, (283, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 1368 , (3, 0, None, None) , 64 , )),
	(( 'LMGetSymbolLibPath' , 'sPath' , ), 284, (284, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 1376 , (3, 0, None, None) , 64 , )),
	(( 'LMSetSymbolLibPath' , 'sPath' , 'retval' , ), 285, (285, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1384 , (3, 0, None, None) , 64 , )),
	(( 'ConvertSchematicToICT' , 'sSchName' , 'retval' , ), 286, (286, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1392 , (3, 0, None, None) , 64 , )),
	(( 'GetSystemDesign' , 'retval' , ), 287, (287, (), [ (16393, 10, None, "IID('{C8B527DC-E1E6-439B-8C7F-D55BACC1D5F1}')") , ], 1 , 1 , 4 , 0 , 1400 , (3, 0, None, None) , 64 , )),
	(( 'ImportPadsPE' , 'sPrj' , 'sPcb' , 'retval' , ), 288, (288, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1408 , (3, 0, None, None) , 64 , )),
	(( 'RunISE' , 'sPath' , 'retval' , ), 289, (289, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1416 , (3, 0, None, None) , 0 , )),
	(( 'IsReferenceApplication' , 'retval' , ), 290, (290, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1424 , (3, 0, None, None) , 64 , )),
	(( 'DataTag' , 'retval' , ), 291, (291, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 1432 , (3, 0, None, None) , 64 , )),
	(( 'OpenReference' , 'sProjectPath' , 'vdApp' , ), 292, (292, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{EA4ABD71-84B0-11CE-8237-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 1440 , (3, 0, None, None) , 64 , )),
	(( 'IsReadOnlyMode' , 'retval' , ), 293, (293, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1448 , (3, 0, None, None) , 64 , )),
	(( 'IsAppStarted' , 'retval' , ), 294, (294, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1456 , (3, 0, None, None) , 64 , )),
	(( 'IsProjectOpened' , 'retval' , ), 295, (295, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1464 , (3, 0, None, None) , 64 , )),
	(( 'ImportEEToPE' , 'sEEPrj' , 'retval' , ), 296, (296, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1472 , (3, 0, None, None) , 64 , )),
	(( 'DesignSearcher' , 'retval' , ), 297, (297, (), [ (16393, 10, None, "IID('{3EBAD6B7-B757-4A57-9657-DD43BF86A526}')") , ], 1 , 1 , 4 , 0 , 1480 , (3, 0, None, None) , 0 , )),
	(( 'BroadcastDBConfigModified' , 'sSource' , 'sPath' , ), 298, (298, (), [ (8, 1, None, None) , 
			 (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 1488 , (3, 0, None, None) , 64 , )),
	(( 'GetProjectType' , 'retval' , ), 299, (299, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 1496 , (3, 0, None, None) , 64 , )),
	(( 'ReplacePart' , 'SourcePart' , 'Scope' , 'DestinationPart' , 'PinMapping' , 
			 'PropertyMapping' , 'retval' , ), 300, (300, (), [ (8, 1, None, None) , (3, 1, None, None) , 
			 (8, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1504 , (3, 0, None, None) , 64 , )),
	(( 'StartVNSD' , ), 301, (301, (), [ ], 1 , 1 , 4 , 0 , 1512 , (3, 0, None, None) , 64 , )),
	(( 'HideModelProperties' , 'mode' , ), 302, (302, (), [ (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 1520 , (3, 0, None, None) , 64 , )),
	(( 'MGCDesignerDataManagement' , 'retval' , ), 303, (303, (), [ (16393, 10, None, "IID('{96EB093C-B1E3-444B-B39D-08D05CB0DF06}')") , ], 1 , 1 , 4 , 0 , 1528 , (3, 0, None, None) , 0 , )),
	(( 'CreateProjectLibrary' , 'retval' , ), 304, (304, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1536 , (3, 0, None, None) , 64 , )),
	(( 'IsManagedBlock' , 'sMBName' , 'retval' , ), 305, (305, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1544 , (3, 0, None, None) , 64 , )),
	(( 'IsManagedBlockSource' , 'sMBName' , 'retval' , ), 306, (306, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1552 , (3, 0, None, None) , 64 , )),
	(( 'ExecuteCommandByID' , 'command_Id' , ), 307, (307, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 1560 , (3, 0, None, None) , 64 , )),
	(( 'ProductionLibraryLimitationsChanged' , ), 308, (308, (), [ ], 1 , 1 , 4 , 0 , 1568 , (3, 0, None, None) , 0 , )),
	(( 'SupportsProdLibLimitation' , 'retval' , ), 309, (309, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1576 , (3, 0, None, None) , 64 , )),
	(( 'GetProdLibs' , 'libSpec' , 'pProdLibs' , ), 310, (310, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')") , ], 1 , 1 , 4 , 0 , 1584 , (3, 0, None, None) , 64 , )),
	(( 'SetProdLib' , 'dbcPath' , 'prodLibName' , 'retval' , ), 311, (311, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1592 , (3, 0, None, None) , 64 , )),
	(( 'GetCurrentProdLib' , 'retval' , ), 312, (312, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 1600 , (3, 0, None, None) , 64 , )),
	(( 'GetDefaultProdLib' , 'retval' , ), 313, (313, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 1608 , (3, 0, None, None) , 64 , )),
	(( 'ImportPADS' , 'ProjectPath' , 'retval' , ), 314, (314, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1616 , (3, 0, None, None) , 64 , )),
	(( 'GetProdLibReadOnly' , 'retval' , ), 315, (315, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1624 , (3, 0, None, None) , 64 , )),
	(( 'IsProdLibSet' , 'retval' , ), 316, (316, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1632 , (3, 0, None, None) , 64 , )),
	(( 'GetLibSpec' , 'retval' , ), 317, (317, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 1640 , (3, 0, None, None) , 64 , )),
	(( 'ShouldProvideDetailedComponentView' , 'LibraryPath' , 'retval' , ), 318, (318, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1648 , (3, 0, None, None) , 64 , )),
	(( 'OpenDetailedComponentView' , 'LibraryPath' , 'partNumber' , ), 319, (319, (), [ (8, 1, None, None) , 
			 (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 1656 , (3, 0, None, None) , 64 , )),
	(( 'OpenDetailedManagedBlockView' , 'Name' , 'Version' , ), 320, (320, (), [ (8, 1, None, None) , 
			 (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 1664 , (3, 0, None, None) , 64 , )),
]

IVdAppProtectionProxy_vtables_dispatch_ = 1
IVdAppProtectionProxy_vtables_ = [
	(( 'Documents' , 'retval' , ), 1, (1, (), [ (16393, 10, None, "IID('{BD2EDF77-7E28-11CE-822D-00001B4D36B5}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Visible' , 'retval' , ), 204, (204, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Visible' , 'retval' , ), 204, (204, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Application' , 'retval' , ), 3, (3, (), [ (16393, 10, None, "IID('{EA4ABD71-84B0-11CE-8237-00001B4D36B5}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'FullName' , 'retval' , ), 4, (4, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'retval' , ), 5, (5, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'retval' , ), 6, (6, (), [ (16393, 10, None, "IID('{EA4ABD71-84B0-11CE-8237-00001B4D36B5}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Interactive' , 'retval' , ), 205, (205, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Interactive' , 'retval' , ), 205, (205, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'ActiveView' , 'retval' , ), 207, (207, (), [ (16393, 10, None, "IID('{0892A013-86BC-11CE-8238-00001B4D36B5}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'ClientAdvisorFlags' , 'retval' , ), 9, (9, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'ClientAdvisorFlags' , 'retval' , ), 9, (9, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'ActiveViewHandle' , 'retval' , ), 40, (40, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'CommandBars' , 'retval' , ), 215, (215, (), [ (16393, 10, None, "IID('{91818215-A01E-11D2-8F30-0060B0EF0A25}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'StatusBarText' , 'retval' , ), 206, (206, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'StatusBarText' , 'retval' , ), 206, (206, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'BusyCursor' , 'retval' , ), 61, (61, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'BusyCursor' , 'retval' , ), 61, (61, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Version' , 'retval' , ), 209, (209, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Addins' , 'retval' , ), 216, (216, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'OptionLevel' , 'retval' , ), 73, (73, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'CommandLineArguments' , 'retval' , ), 210, (210, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Quit' , ), 226, (226, (), [ ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'SetClientAdvisor' , 'Advisor' , 'Flags' , 'retval' , ), 11, (11, (), [ 
			 (9, 1, None, None) , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'ParamSetValue' , 'Index' , 'NewValue' , ), 12, (12, (), [ (3, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'ParamGetValue' , 'Index' , 'retval' , ), 13, (13, (), [ (3, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'ParamGetMode' , 'Index' , 'retval' , ), 14, (14, (), [ (3, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'ParamSetMode' , 'Index' , 'NewValue' , ), 15, (15, (), [ (3, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'GetLastErrorString' , 'retval' , ), 239, (239, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'GetLastErrorId' , 'retval' , ), 240, (240, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'SetEnvVariable' , 'pName' , 'pValue' , 'retval' , ), 211, (211, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'Initialize' , 'WDIRPath' , 'LicensePath' , 'retval' , ), 203, (203, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'GetTypeFromIDispatch' , 'Dispatch' , 'retval' , ), 20, (20, (), [ (9, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'UserControl' , 'retval' , ), 21, (21, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'Guid' , 'retval' , ), 22, (22, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'Activate' , ), 201, (201, (), [ ], 1 , 1 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'ExecuteCommand' , 'CommandString' , 'retval' , ), 29, (29, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'RegisterOLECommand' , 'CommandName' , 'CommandDescription' , 'bModifiesData' , 'pDispatch' , 
			 'retval' , ), 33, (33, (), [ (8, 1, None, None) , (8, 1, None, None) , (11, 1, None, None) , 
			 (9, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'UnregisterOLECommand' , 'CommandName' , 'ClientDispatch' , 'retval' , ), 36, (36, (), [ 
			 (8, 1, None, None) , (9, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'DataObjExists' , 'Library' , 'Name' , 'Extension' , 'Class' , 
			 'retval' , ), 37, (37, (), [ (8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , 
			 (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'DataObjGetPath' , 'Library' , 'Name' , 'Extension' , 'Class' , 
			 'retval' , ), 38, (38, (), [ (8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , 
			 (3, 1, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'ParamAddListName' , 'which_param' , 'new_name' , ), 39, (39, (), [ (3, 1, None, None) , 
			 (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'CommandEnable' , 'CommandName' , 'retval' , ), 42, (42, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'CommandDisable' , 'CommandName' , 'retval' , ), 43, (43, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'CommandRemove' , 'CommandName' , 'retval' , ), 44, (44, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'QueryBlocks' , 'BlockType' , 'Library' , 'retval' , ), 45, (45, (), [ 
			 (3, 1, None, None) , (8, 1, None, None) , (16393, 10, None, "IID('{BD2EDF77-7E28-11CE-822D-00001B4D36B7}')") , ], 1 , 1 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'QueryPages' , 'Name' , 'retval' , ), 46, (46, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{BD2EDF77-7E28-11CE-822D-00001B4D36B7}')") , ], 1 , 1 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'SetLibFileNew' , 'DirPath' , 'retval' , ), 47, (47, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'SetLibFileOpen' , 'DirPath' , 'retval' , ), 48, (48, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'SetLibAddComp' , 'DirPath' , 'retval' , ), 49, (49, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'DesignBlocks' , 'Library' , 'Name' , 'SheetNumber' , 'LevelString' , 
			 'RecurseDown' , 'retval' , ), 50, (50, (), [ (8, 1, None, None) , (8, 1, None, None) , 
			 (8, 1, None, None) , (8, 1, None, None) , (11, 1, None, None) , (16393, 10, None, "IID('{BD2EDF77-7E28-11CE-822D-00001B4D36B7}')") , ], 1 , 1 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'SetViewAnalogFlag' , 'state' , ), 52, (52, (), [ (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'ReadIni' , 'Inifilename' , 'retval' , ), 202, (202, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'DesignPaths' , 'Library' , 'Name' , 'LevelString' , 'RecurseDown' , 
			 'retval' , ), 54, (54, (), [ (8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , 
			 (11, 1, None, None) , (16393, 10, None, "IID('{7BB17D63-FAE6-11D1-BE10-00A0C9204FDC}')") , ], 1 , 1 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'TextViews' , 'retval' , ), 57, (57, (), [ (16393, 10, None, None) , ], 1 , 1 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'Bindings' , 'BindingTable' , 'retval' , ), 219, (219, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{A73EBAD3-B3F1-11D2-99AE-00A0C966477E}')") , ], 1 , 1 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( 'DesignComponents' , 'Library' , 'Name' , 'EndSheet' , 'LevelString' , 
			 'RecurseDown' , 'retval' , ), 59, (59, (), [ (8, 1, None, None) , (8, 1, None, None) , 
			 (8, 49, "''", None) , (8, 49, "''", None) , (11, 49, 'True', None) , (16393, 10, None, "IID('{BD2EDF77-7E28-11CE-822D-00001B4D36B7}')") , ], 1 , 1 , 4 , 0 , 504 , (3, 32, None, None) , 0 , )),
	(( 'SelectPath' , 'FileName' , 'HierPath' , 'SheetNumber' , 'Type' , 
			 'AddSelected' , 'SearchBus' , 'retval' , ), 67, (67, (), [ (8, 1, None, None) , 
			 (8, 1, None, None) , (8, 1, None, None) , (3, 1, None, None) , (11, 1, None, None) , (11, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 512 , (3, 0, None, None) , 0 , )),
	(( 'SelectPathCompPin' , 'FileName' , 'HierPath' , 'SheetNumber' , 'PinNumber' , 
			 'SelectType' , 'retval' , ), 68, (68, (), [ (8, 1, None, None) , (8, 1, None, None) , 
			 (8, 1, None, None) , (8, 1, None, None) , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
	(( 'PushPath' , 'Top' , 'HierPath' , 'SheetNumber' , 'retval' , 
			 ), 69, (69, (), [ (8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 528 , (3, 0, None, None) , 0 , )),
	(( 'PrintProject' , 'DesignName' , 'LevelStrings' , 'PrintSymbols' , 'ShowOrderDialog' , 
			 'PPOFile' , ), 221, (221, (), [ (8, 1, None, None) , (8, 1, None, None) , (11, 1, None, None) , 
			 (11, 1, None, None) , (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 536 , (3, 0, None, None) , 0 , )),
	(( 'SetRedraw' , 'Redraw' , ), 222, (222, (), [ (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 544 , (3, 0, None, None) , 0 , )),
	(( 'BrowseForSymbol' , 'OnlyBorders' , 'Title' , 'retval' , ), 72, (72, (), [ 
			 (11, 1, None, None) , (8, 1, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 552 , (3, 0, None, None) , 0 , )),
	(( 'InsertSheet' , 'DesignName' , 'SheetNumber' , 'retval' , ), 75, (75, (), [ 
			 (8, 1, None, None) , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 560 , (3, 0, None, None) , 0 , )),
	(( 'DeleteSheet' , 'DesignName' , 'SheetNumber' , 'retval' , ), 76, (76, (), [ 
			 (8, 1, None, None) , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 568 , (3, 0, None, None) , 0 , )),
	(( 'PreviewDecal' , 'DecalName' , 'retval' , ), 78, (78, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 576 , (3, 0, None, None) , 0 , )),
	(( 'GetClassDefinitions' , 'CreateIfNotDefined' , 'retval' , ), 79, (79, (), [ (11, 1, None, None) , 
			 (16393, 10, None, None) , ], 1 , 1 , 4 , 0 , 584 , (3, 0, None, None) , 0 , )),
	(( 'UnloadClassDefinitions' , ), 81, (81, (), [ ], 1 , 1 , 4 , 0 , 592 , (3, 0, None, None) , 0 , )),
	(( 'OpenBlocks' , 'BlockType' , 'retval' , ), 82, (82, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{BD2EDF77-7E28-11CE-822D-00001B4D36B7}')") , ], 1 , 1 , 4 , 0 , 600 , (3, 0, None, None) , 0 , )),
	(( 'Query' , 'Flags' , 'Selected' , 'retval' , ), 83, (83, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (16393, 10, None, "IID('{BD2EDF77-7E28-11CE-822D-00001B4D36B7}')") , ], 1 , 1 , 4 , 0 , 608 , (3, 0, None, None) , 0 , )),
	(( 'ParamGetListNames' , 'which_param' , 'retval' , ), 84, (84, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{7BB17D63-FAE6-11D1-BE10-00A0C9204FDC}')") , ], 1 , 1 , 4 , 0 , 616 , (3, 0, None, None) , 0 , )),
	(( 'AnnoDisplayTime' , 'Context' , 'Position' , 'Timestring' , ), 85, (85, (), [ 
			 (8, 1, None, None) , (3, 1, None, None) , (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 624 , (3, 0, None, None) , 0 , )),
	(( 'AnnoDisplayValue' , 'Context' , 'DesignPath' , 'AnnType' , 'AnnObject' , 
			 'ObjName' , 'ObjValue' , ), 86, (86, (), [ (8, 1, None, None) , (8, 1, None, None) , 
			 (3, 1, None, None) , (3, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 632 , (3, 0, None, None) , 0 , )),
	(( 'SourceDocuments' , 'retval' , ), 214, (214, (), [ (16393, 10, None, "IID('{AC6510A1-83C5-4486-9154-CE74592F9A48}')") , ], 1 , 2 , 4 , 0 , 640 , (3, 0, None, None) , 0 , )),
	(( 'ExecuteMenuCommand' , 'command_name' , ), 89, (89, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 648 , (3, 0, None, None) , 0 , )),
	(( 'SilentMode' , 'retval' , ), 250, (250, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 656 , (3, 0, None, None) , 0 , )),
	(( 'SilentMode' , 'retval' , ), 250, (250, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 664 , (3, 0, None, None) , 0 , )),
	(( 'LicenseMode' , 'retval' , ), 91, (91, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 672 , (3, 0, None, None) , 0 , )),
	(( 'ShellCmd' , 'retval' , ), 218, (218, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 680 , (3, 0, None, None) , 0 , )),
	(( 'OpenURL' , 'URL' , ), 225, (225, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 688 , (3, 0, None, None) , 0 , )),
	(( 'Cookies' , 'retval' , ), 94, (94, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 696 , (3, 0, None, None) , 0 , )),
	(( 'ActiveDocument' , 'retval' , ), 208, (208, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 704 , (3, 0, None, None) , 0 , )),
	(( 'AppendOutput' , 'TabName' , 'String' , ), 223, (223, (), [ (8, 1, None, None) , 
			 (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 712 , (3, 0, None, None) , 0 , )),
	(( 'HTMLDocuments' , 'retval' , ), 213, (213, (), [ (16393, 10, None, "IID('{7D50CA6D-07DB-4BE0-AD95-563DED3F9157}')") , ], 1 , 2 , 4 , 0 , 720 , (3, 0, None, None) , 0 , )),
	(( 'QueueSelectEvents' , 'bQueue' , ), 224, (224, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 728 , (3, 0, None, None) , 0 , )),
	(( 'QueueSelectEvents' , 'bQueue' , ), 224, (224, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 736 , (3, 0, None, None) , 0 , )),
	(( 'CurrentProject' , 'retval' , ), 55, (55, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 744 , (3, 0, None, None) , 0 , )),
	(( 'CurrentProject' , 'retval' , ), 55, (55, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 752 , (3, 0, None, None) , 0 , )),
	(( 'PrimaryDirectory' , 'retval' , ), 56, (56, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 760 , (3, 0, None, None) , 0 , )),
	(( 'ObjectColor' , 'ObjectType' , 'retval' , ), 65, (65, (), [ (3, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 768 , (3, 0, None, None) , 0 , )),
	(( 'ObjectColor' , 'ObjectType' , 'retval' , ), 65, (65, (), [ (3, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 776 , (3, 0, None, None) , 0 , )),
	(( 'ViewBaseSession' , 'retval' , ), 64, (64, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 784 , (3, 0, None, None) , 0 , )),
	(( 'SynchronizesViewBase' , 'retval' , ), 66, (66, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 792 , (3, 0, None, None) , 0 , )),
	(( 'SynchronizesViewBase' , 'retval' , ), 66, (66, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 800 , (3, 0, None, None) , 0 , )),
	(( 'KickViewbase' , 'ForceReload' , ), 97, (97, (), [ (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 808 , (3, 0, None, None) , 0 , )),
	(( 'IsLibDeletable' , 'Position' , 'retval' , ), 24, (24, (), [ (3, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 816 , (3, 0, None, None) , 0 , )),
	(( 'AddLibrary' , 'LibraryPath' , 'LibraryAlias' , 'LibraryAccess' , 'Position' , 
			 'retval' , ), 25, (25, (), [ (8, 1, None, None) , (8, 1, None, None) , (3, 1, None, None) , 
			 (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 824 , (3, 0, None, None) , 0 , )),
	(( 'DeleteLibrary' , 'Position' , 'retval' , ), 26, (26, (), [ (3, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 832 , (3, 0, None, None) , 0 , )),
	(( 'MoveLibrary' , 'FromPosition' , 'ToPosition' , 'retval' , ), 27, (27, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 840 , (3, 0, None, None) , 0 , )),
	(( 'ClearAllLibraries' , 'retval' , ), 28, (28, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 848 , (3, 0, None, None) , 0 , )),
	(( 'GetLibraries' , 'retval' , ), 30, (30, (), [ (16393, 10, None, "IID('{BD2EDF77-7E28-11CE-822D-00001B4D36B7}')") , ], 1 , 1 , 4 , 0 , 856 , (3, 0, None, None) , 0 , )),
	(( 'AddLibraryAndSaveIni' , 'LibraryPath' , 'LibraryAlias' , 'LibraryAccess' , 'Position' , 
			 'retval' , ), 104, (104, (), [ (8, 1, None, None) , (8, 1, None, None) , (3, 1, None, None) , 
			 (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 864 , (3, 0, None, None) , 0 , )),
	(( 'DeleteLibraryAndSaveIni' , 'Position' , 'retval' , ), 105, (105, (), [ (3, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 872 , (3, 0, None, None) , 0 , )),
	(( 'MoveLibraryAndSaveIni' , 'FromPosition' , 'ToPosition' , 'retval' , ), 106, (106, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 880 , (3, 0, None, None) , 0 , )),
	(( 'SaveIni' , 'retval' , ), 34, (34, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 888 , (3, 0, None, None) , 0 , )),
	(( 'RemoveProjectSettingTab' , 'TabIndicator' , ), 51, (51, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 896 , (3, 0, None, None) , 0 , )),
	(( 'AttributeCanHaveOatValue' , 'AttributeName' , 'retval' , ), 74, (74, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 904 , (3, 0, None, None) , 0 , )),
	(( 'AttributeValueMustBeUpper' , 'AttributeName' , 'retval' , ), 77, (77, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 912 , (3, 0, None, None) , 0 , )),
	(( 'Flows' , 'retval' , ), 98, (98, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 920 , (3, 0, None, None) , 0 , )),
	(( 'ProjMan' , 'retval' , ), 88, (88, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 928 , (3, 0, None, None) , 0 , )),
	(( 'project' , 'retval' , ), 101, (101, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 936 , (3, 0, None, None) , 0 , )),
	(( 'CnsFileString' , 'retval' , ), 102, (102, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 944 , (3, 0, None, None) , 0 , )),
	(( 'MakeReusableBlock' , 'ProjectName' , 'SchematicRoot' , 'DestDir' , 'RBName' , 
			 ), 103, (103, (), [ (8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 952 , (3, 0, None, None) , 0 , )),
	(( 'CheckIfNavigatorAddinsOpen' , 'retval' , ), 107, (107, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 960 , (3, 0, None, None) , 0 , )),
	(( 'CloseNavigatorAddins' , ), 108, (108, (), [ ], 1 , 1 , 4 , 0 , 968 , (3, 0, None, None) , 0 , )),
	(( 'GetProjectData' , 'retval' , ), 228, (228, (), [ (16393, 10, None, "IID('{956DD308-D5ED-40A1-83F2-84113B8937C1}')") , ], 1 , 1 , 4 , 0 , 976 , (3, 0, None, None) , 0 , )),
	(( 'SchematicSheetDocuments' , 'retval' , ), 212, (212, (), [ (16393, 10, None, "IID('{608CA7F4-A52A-4206-9580-3BEB17CE0073}')") , ], 1 , 1 , 4 , 0 , 984 , (3, 0, None, None) , 0 , )),
	(( 'CommandsManager' , 'retval' , ), 220, (220, (), [ (16393, 10, None, "IID('{AA7F70A6-2F0E-417C-A1D2-C1621D728EB0}')") , ], 1 , 1 , 4 , 0 , 992 , (3, 0, None, None) , 0 , )),
	(( 'GetCommonPropertyManager' , 'retval' , ), 243, (243, (), [ (16393, 10, None, "IID('{E8758B51-DEBB-46FD-A192-962B14F57FA4}')") , ], 1 , 1 , 4 , 0 , 1000 , (3, 0, None, None) , 0 , )),
	(( 'OpenProject' , 'ProjectPath' , 'retval' , ), 227, (227, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1008 , (3, 0, None, None) , 0 , )),
	(( 'NewProject' , 'ProjectPath' , 'CentralLibraryPath' , 'ServerName' , 'ProjectTemplatePath' , 
			 'retval' , ), 251, (251, (), [ (8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , 
			 (8, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1016 , (3, 0, None, None) , 0 , )),
	(( 'GetActiveDesign' , 'sActiveiCDBDesign' , ), 229, (229, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 1024 , (3, 0, None, None) , 0 , )),
	(( 'GetFramework' , 'retval' , ), 242, (242, (), [ (16393, 10, None, "IID('{77CD6602-703B-4AFA-A4C1-B1652A257F15}')") , ], 1 , 1 , 4 , 0 , 1032 , (3, 0, None, None) , 0 , )),
	(( 'GetConfigurationProperty' , 'Name' , 'val' , ), 244, (244, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')") , ], 1 , 1 , 4 , 0 , 1040 , (3, 0, None, None) , 0 , )),
	(( 'SetConfigurationProperty' , 'Name' , 'val' , ), 245, (245, (), [ (8, 1, None, None) , 
			 (9, 1, None, "IID('{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')") , ], 1 , 1 , 4 , 0 , 1048 , (3, 0, None, None) , 0 , )),
	(( 'StartMigration' , 'ProjectPath' , 'CentralLibPath' , 'retval' , ), 246, (246, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1056 , (3, 0, None, None) , 0 , )),
	(( 'EnableEEVMMode' , 'eevmDataFile' , ), 247, (247, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 1064 , (3, 0, None, None) , 0 , )),
	(( 'ClearEEVMMode' , ), 248, (248, (), [ ], 1 , 1 , 4 , 0 , 1072 , (3, 0, None, None) , 0 , )),
	(( 'IsEEVMModeEnabled' , 'bEnabled' , ), 249, (249, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1080 , (3, 0, None, None) , 0 , )),
	(( 'ConvertSymbol' , 'sSymbol' , 'retval' , ), 252, (252, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1088 , (3, 0, None, None) , 0 , )),
	(( 'SetButtonBitmap' , 'CommandID' , 'BitmapFilePath' , 'retval' , ), 253, (253, (), [ 
			 (19, 1, None, None) , (8, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1096 , (3, 0, None, None) , 0 , )),
	(( 'SetButtonResourceDLL' , 'CommandID' , 'DllFilePath' , 'resID' , 'retval' , 
			 ), 254, (254, (), [ (19, 1, None, None) , (8, 1, None, None) , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1104 , (3, 0, None, None) , 0 , )),
	(( 'CreateToolbar' , 'Name' , 'retval' , ), 255, (255, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1112 , (3, 0, None, None) , 0 , )),
	(( 'DeleteBlock' , 'Name' , 'retval' , ), 256, (256, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1120 , (3, 0, None, None) , 0 , )),
	(( 'FireCentralLibraryReload' , ), 257, (257, (), [ ], 1 , 1 , 4 , 0 , 1128 , (3, 0, None, None) , 0 , )),
	(( 'GetICTContents' , 'ICTName' , 'outputFilePath' , 'retval' , ), 258, (258, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1136 , (3, 0, None, None) , 0 , )),
	(( 'GetICTDocuments' , 'retval' , ), 259, (259, (), [ (16393, 10, None, "IID('{2A3CCA57-9C38-4484-A6A3-7521DDF7DAD0}')") , ], 1 , 1 , 4 , 0 , 1144 , (3, 0, None, None) , 0 , )),
	(( 'SetDefaultColor' , 'ObjectType' , 'Color' , ), 260, (260, (), [ (3, 1, None, None) , 
			 (9, 1, None, "IID('{C1031A0C-15BD-4897-A3E5-4C615CDEA684}')") , ], 1 , 1 , 4 , 0 , 1152 , (3, 0, None, None) , 0 , )),
	(( 'GetDefaultColor' , 'ObjectType' , 'retval' , ), 261, (261, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{C1031A0C-15BD-4897-A3E5-4C615CDEA684}')") , ], 1 , 1 , 4 , 0 , 1160 , (3, 0, None, None) , 0 , )),
	(( 'ToolbarAction' , 'Handle' , 'Msg' , 'wParam' , 'lParam' , 
			 'retval' , ), 262, (262, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , 
			 (3, 1, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 1168 , (3, 0, None, None) , 0 , )),
	(( 'LaunchSymbolEditor' , 'sSymbolName' , ), 263, (263, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 1176 , (3, 0, None, None) , 0 , )),
	(( 'ExportForeignDatabase' , 'sPath' , 'retval' , ), 264, (264, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1184 , (3, 0, None, None) , 0 , )),
	(( 'ImportForeignDatabase' , 'sPath' , 'retval' , ), 265, (265, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1192 , (3, 0, None, None) , 0 , )),
	(( 'SelectComponent' , 'sSchName' , 'sSheetName' , 'sCompUID' , 'retval' , 
			 ), 266, (266, (), [ (8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1200 , (3, 0, None, None) , 0 , )),
	(( 'SelectNet' , 'sSchName' , 'sSheetName' , 'sNetUID' , 'retval' , 
			 ), 267, (267, (), [ (8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1208 , (3, 0, None, None) , 0 , )),
	(( 'Validate' , '_lLicenseToken' , '_plLicenseToken' , ), 268, (268, (), [ (3, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 1216 , (3, 0, None, None) , 0 , )),
	(( 'ActiveICTView' , 'retval' , ), 269, (269, (), [ (16393, 10, None, "IID('{848E324F-125D-4236-981D-0EB202E628DA}')") , ], 1 , 2 , 4 , 0 , 1224 , (3, 0, None, None) , 0 , )),
	(( 'EnableSelectionBroadcast' , ), 271, (271, (), [ ], 1 , 1 , 4 , 0 , 1232 , (3, 0, None, None) , 0 , )),
	(( 'DisableSelectionBroadcast' , ), 272, (272, (), [ ], 1 , 1 , 4 , 0 , 1240 , (3, 0, None, None) , 0 , )),
	(( 'CloseProject' , 'retval' , ), 274, (274, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1248 , (3, 0, None, None) , 0 , )),
	(( 'ExtractPCB' , 'sPath' , 'sDetailedWiring' , 'retval' , ), 275, (275, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1256 , (3, 0, None, None) , 0 , )),
	(( 'DesignNets' , 'Library' , 'Name' , 'EndSheet' , 'LevelString' , 
			 'RecurseDown' , 'retval' , ), 276, (276, (), [ (8, 1, None, None) , (8, 1, None, None) , 
			 (8, 49, "''", None) , (8, 49, "''", None) , (11, 49, 'True', None) , (16393, 10, None, "IID('{BD2EDF77-7E28-11CE-822D-00001B4D36B7}')") , ], 1 , 1 , 4 , 0 , 1264 , (3, 32, None, None) , 0 , )),
	(( 'SetGenericStatusIndicatorState' , 'eIndicatorColor' , 'sToolTipText' , 'retval' , ), 277, (277, (), [ 
			 (3, 1, None, None) , (8, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1272 , (3, 0, None, None) , 64 , )),
	(( 'SheetsEditMode' , 'retval' , ), 279, (279, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 1280 , (3, 0, None, None) , 64 , )),
	(( 'SheetsEditMode' , 'retval' , ), 279, (279, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 1288 , (3, 0, None, None) , 64 , )),
	(( 'ExportSymbol' , 'sSymbolName' , 'sTargetDir' , 'retval' , ), 280, (280, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1296 , (3, 0, None, None) , 0 , )),
	(( 'EDXEngine' , 'retval' , ), 281, (281, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 1304 , (3, 0, None, None) , 64 , )),
	(( 'UpdateMenuBar' , 'menuBarParentWnd' , 'hMenu' , 'retval' , ), 282, (282, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 1312 , (3, 0, None, None) , 0 , )),
	(( 'GetPEFlowMode' , 'retval' , ), 283, (283, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 1320 , (3, 0, None, None) , 64 , )),
	(( 'LMGetSymbolLibPath' , 'sPath' , ), 284, (284, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 1328 , (3, 0, None, None) , 64 , )),
	(( 'LMSetSymbolLibPath' , 'sPath' , 'retval' , ), 285, (285, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1336 , (3, 0, None, None) , 64 , )),
	(( 'ConvertSchematicToICT' , 'sSchName' , 'retval' , ), 286, (286, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1344 , (3, 0, None, None) , 64 , )),
	(( 'ImportPadsPE' , 'sPrj' , 'sPcb' , 'retval' , ), 288, (288, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1352 , (3, 0, None, None) , 64 , )),
	(( 'RunISE' , 'sPath' , 'retval' , ), 289, (289, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1360 , (3, 0, None, None) , 0 , )),
	(( 'IsReferenceApplication' , 'retval' , ), 290, (290, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1368 , (3, 0, None, None) , 64 , )),
	(( 'DataTag' , 'retval' , ), 291, (291, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 1376 , (3, 0, None, None) , 64 , )),
	(( 'OpenReference' , 'sProjectPath' , 'vdApp' , ), 292, (292, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{EA4ABD71-84B0-11CE-8237-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 1384 , (3, 0, None, None) , 64 , )),
	(( 'IsReadOnlyMode' , 'retval' , ), 293, (293, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1392 , (3, 0, None, None) , 64 , )),
	(( 'IsAppStarted' , 'retval' , ), 294, (294, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1400 , (3, 0, None, None) , 64 , )),
	(( 'IsProjectOpened' , 'retval' , ), 295, (295, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1408 , (3, 0, None, None) , 64 , )),
	(( 'ImportEEToPE' , 'sEEPrj' , 'retval' , ), 296, (296, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1416 , (3, 0, None, None) , 64 , )),
	(( 'DesignSearcher' , 'retval' , ), 297, (297, (), [ (16393, 10, None, "IID('{3EBAD6B7-B757-4A57-9657-DD43BF86A526}')") , ], 1 , 1 , 4 , 0 , 1424 , (3, 0, None, None) , 0 , )),
	(( 'BroadcastDBConfigModified' , 'sSource' , 'sPath' , ), 298, (298, (), [ (8, 1, None, None) , 
			 (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 1432 , (3, 0, None, None) , 64 , )),
	(( 'GetProjectType' , 'retval' , ), 299, (299, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 1440 , (3, 0, None, None) , 64 , )),
	(( 'ReplacePart' , 'SourcePart' , 'Scope' , 'DestinationPart' , 'PinMapping' , 
			 'PropertyMapping' , 'retval' , ), 300, (300, (), [ (8, 1, None, None) , (3, 1, None, None) , 
			 (8, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1448 , (3, 0, None, None) , 64 , )),
	(( 'StartVNSD' , ), 301, (301, (), [ ], 1 , 1 , 4 , 0 , 1456 , (3, 0, None, None) , 64 , )),
	(( 'HideModelProperties' , 'bHide' , ), 302, (302, (), [ (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 1464 , (3, 0, None, None) , 64 , )),
	(( 'MGCDesignerDataManagement' , 'retval' , ), 303, (303, (), [ (16393, 10, None, "IID('{96EB093C-B1E3-444B-B39D-08D05CB0DF06}')") , ], 1 , 1 , 4 , 0 , 1472 , (3, 0, None, None) , 0 , )),
	(( 'CreateProjectLibrary' , 'retval' , ), 304, (304, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1480 , (3, 0, None, None) , 64 , )),
	(( 'IsManagedBlock' , 'sMBName' , 'retval' , ), 305, (305, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1488 , (3, 0, None, None) , 64 , )),
	(( 'IsManagedBlockSource' , 'sMBName' , 'retval' , ), 306, (306, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1496 , (3, 0, None, None) , 64 , )),
	(( 'ExecuteCommandByID' , 'command_Id' , ), 307, (307, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 1504 , (3, 0, None, None) , 64 , )),
	(( 'ProductionLibraryLimitationsChanged' , ), 308, (308, (), [ ], 1 , 1 , 4 , 0 , 1512 , (3, 0, None, None) , 0 , )),
	(( 'SupportsProdLibLimitation' , 'retval' , ), 309, (309, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1520 , (3, 0, None, None) , 64 , )),
	(( 'GetProdLibs' , 'libSpec' , 'pProdLibs' , ), 310, (310, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')") , ], 1 , 1 , 4 , 0 , 1528 , (3, 0, None, None) , 64 , )),
	(( 'SetProdLib' , 'dbcPath' , 'prodLibName' , 'retval' , ), 311, (311, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1536 , (3, 0, None, None) , 64 , )),
	(( 'GetCurrentProdLib' , 'retval' , ), 312, (312, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 1544 , (3, 0, None, None) , 64 , )),
	(( 'GetDefaultProdLib' , 'retval' , ), 313, (313, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 1552 , (3, 0, None, None) , 64 , )),
	(( 'GetProdLibReadOnly' , 'retval' , ), 315, (315, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1560 , (3, 0, None, None) , 64 , )),
	(( 'IsProdLibSet' , 'retval' , ), 316, (316, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1568 , (3, 0, None, None) , 64 , )),
	(( 'GetLibSpec' , 'retval' , ), 317, (317, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 1576 , (3, 0, None, None) , 64 , )),
	(( 'ShouldProvideDetailedComponentView' , 'LibraryPath' , 'retval' , ), 318, (318, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1584 , (3, 0, None, None) , 64 , )),
	(( 'OpenDetailedComponentView' , 'LibraryPath' , 'partNumber' , ), 319, (319, (), [ (8, 1, None, None) , 
			 (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 1592 , (3, 0, None, None) , 64 , )),
	(( 'OpenDetailedManagedBlockView' , 'Name' , 'Version' , ), 320, (320, (), [ (8, 1, None, None) , 
			 (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 1600 , (3, 0, None, None) , 64 , )),
]

IVdApplicationAtTest_vtables_dispatch_ = 1
IVdApplicationAtTest_vtables_ = [
	(( 'ExtractReuseCircuits' , ), 1, (1, (), [ ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'ReplaceConnector' , 'SourceConnector' , 'Scope' , 'DestinationConnector' , 'PinMapping' , 
			 'PropertyMapping' , 'retval' , ), 2, (2, (), [ (8, 1, None, None) , (3, 1, None, None) , 
			 (8, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'ReplaceSymbol' , 'SourceSymbol' , 'Scope' , 'DestinationSymbol' , 'PinMapping' , 
			 'PropertyMapping' , 'retval' , ), 3, (3, (), [ (8, 1, None, None) , (3, 1, None, None) , 
			 (8, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'UpdateDRBs' , ), 4, (4, (), [ ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'ImportNetlistProject' , 'ProjectPath' , 'retval' , ), 5, (5, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'RunProjectIntegrationTask' , 'taskName' , ), 6, (6, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'GetProjectIntegrationStatus' , 'taskName' , 'retval' , ), 7, (7, (), [ (8, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'PropagateFpgaSignalNames' , ), 8, (8, (), [ ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'RunSchematicTest' , 'testName' , 'retval' , ), 9, (9, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'PublishBlocks' , 'names' , 'retval' , ), 10, (10, (), [ (9, 1, None, "IID('{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')") , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'DumpOutputWindow' , 'TabName' , 'retval' , ), 11, (11, (), [ (8, 1, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'ImportEDXFileDownloadedFromPartQuestSite' , 'EDXFilePath' , 'retval' , ), 12, (12, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
]

IVdArc_vtables_dispatch_ = 1
IVdArc_vtables_ = [
	(( 'Type' , 'retval' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'LineStyle' , 'retval' , ), 2, (2, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'LineStyle' , 'retval' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Application' , 'retval' , ), 3, (3, (), [ (16393, 10, None, "IID('{EA4ABD71-84B0-11CE-8237-00001B4D36B5}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'retval' , ), 4, (4, (), [ (16393, 10, None, "IID('{AE729484-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'retval' , ), 10, (10, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 64 , )),
	(( 'Color' , 'retval' , ), 10, (10, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 64 , )),
	(( 'Selected' , ), 11, (11, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( '_SetSelected' , 'Flag' , ), 5, (5, (), [ (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 64 , )),
	(( 'GetLocation' , 'WhichPoint' , 'retval' , ), 6, (6, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{AE729498-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'SetLocation' , 'X1' , 'Y1' , 'X2' , 'Y2' , 
			 'X3' , 'Y3' , ), 7, (7, (), [ (3, 1, None, None) , (3, 1, None, None) , 
			 (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( '_GetColor' , 'retval' , ), 8, (8, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 64 , )),
	(( '_SetColor' , 'newColor' , ), 9, (9, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 64 , )),
	(( 'SetObjectColor' , 'newColor' , ), 12, (12, (), [ (9, 1, None, "IID('{C1031A0C-15BD-4897-A3E5-4C615CDEA684}')") , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'GetObjectColor' , 'retval' , ), 13, (13, (), [ (16393, 10, None, "IID('{C1031A0C-15BD-4897-A3E5-4C615CDEA684}')") , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'SetAutomaticColor' , 'bAutomatic' , ), 14, (14, (), [ (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'IsColorAutomatic' , 'retval' , ), 15, (15, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
]

IVdAttr_vtables_dispatch_ = 1
IVdAttr_vtables_ = [
	(( 'TextString' , 'retval' , ), 1, (1, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'TextString' , 'retval' , ), 1, (1, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Value' , 'retval' , ), 2, (2, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Value' , 'retval' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'retval' , ), 3, (3, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Visible' , 'retval' , ), 4, (4, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Visible' , 'retval' , ), 4, (4, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'retval' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Font' , 'retval' , ), 6, (6, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Font' , 'retval' , ), 6, (6, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Origin' , 'retval' , ), 7, (7, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Origin' , 'retval' , ), 7, (7, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Orientation' , 'retval' , ), 8, (8, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Orientation' , 'retval' , ), 8, (8, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Size' , 'retval' , ), 9, (9, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Size' , 'retval' , ), 9, (9, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Application' , 'retval' , ), 10, (10, (), [ (16393, 10, None, "IID('{EA4ABD71-84B0-11CE-8237-00001B4D36B5}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'retval' , ), 11, (11, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Child' , 'retval' , ), 21, (21, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'retval' , ), 22, (22, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 64 , )),
	(( 'Color' , 'retval' , ), 22, (22, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 64 , )),
	(( 'Selected' , ), 23, (23, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'EitherValue' , 'retval' , ), 24, (24, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'EitherValue' , 'retval' , ), 24, (24, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'OatValue' , 'retval' , ), 25, (25, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 248 , (3, 0, None, None) , 64 , )),
	(( 'OatValue' , 'retval' , ), 25, (25, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 64 , )),
	(( 'InstanceValue' , 'retval' , ), 30, (30, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'InstanceValue' , 'retval' , ), 30, (30, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'Printable' , 'retval' , ), 34, (34, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 280 , (3, 0, None, None) , 64 , )),
	(( 'Printable' , 'retval' , ), 34, (34, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 64 , )),
	(( '_SetSelected' , 'Flag' , ), 12, (12, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 296 , (3, 0, None, None) , 64 , )),
	(( 'GetLocation' , 'retval' , ), 13, (13, (), [ (16393, 10, None, "IID('{AE729498-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'SetLocation' , 'X' , 'Y' , ), 14, (14, (), [ (3, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( '_GetColor' , 'retval' , ), 15, (15, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 320 , (3, 0, None, None) , 64 , )),
	(( '_SetColor' , 'newColor' , ), 16, (16, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 328 , (3, 0, None, None) , 64 , )),
	(( '_SetEitherValue' , 'Value' , ), 17, (17, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 336 , (3, 0, None, None) , 64 , )),
	(( '_GetEitherValue' , 'retval' , ), 18, (18, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 344 , (3, 0, None, None) , 64 , )),
	(( '_SetOatValue' , 'Value' , ), 19, (19, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 352 , (3, 0, None, None) , 64 , )),
	(( '_GetOatValue' , 'retval' , ), 20, (20, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 360 , (3, 0, None, None) , 64 , )),
	(( 'GetOatFull' , 'toplevel' , 'pathvalue' , 'full_or_not' , 'retval' , 
			 ), 26, (26, (), [ (8, 1, None, None) , (8, 1, None, None) , (3, 1, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'Delete' , ), 27, (27, (), [ ], 1 , 1 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'SetObjectColor' , 'newColor' , ), 28, (28, (), [ (9, 1, None, "IID('{C1031A0C-15BD-4897-A3E5-4C615CDEA684}')") , ], 1 , 1 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'GetObjectColor' , 'retval' , ), 29, (29, (), [ (16393, 10, None, "IID('{C1031A0C-15BD-4897-A3E5-4C615CDEA684}')") , ], 1 , 1 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'SetAutomaticColor' , 'bAutomatic' , ), 31, (31, (), [ (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'IsColorAutomatic' , 'retval' , ), 32, (32, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'DeleteInstanceValue' , ), 33, (33, (), [ ], 1 , 1 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
]

IVdBlock_vtables_dispatch_ = 1
IVdBlock_vtables_ = [
	(( 'Attributes' , 'retval' , ), 1, (1, (), [ (16393, 10, None, "IID('{BD2EDF77-7E28-11CE-822D-00001B4D36B7}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'retval' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Application' , 'retval' , ), 3, (3, (), [ (16393, 10, None, "IID('{EA4ABD71-84B0-11CE-8237-00001B4D36B5}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'retval' , ), 4, (4, (), [ (16393, 10, None, "IID('{0892A013-86BC-11CE-8238-00001B4D36B5}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'DataType' , 'retval' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'LibraryName' , 'retval' , ), 6, (6, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'SymbolType' , 'retval' , ), 7, (7, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'SymbolType' , 'retval' , ), 7, (7, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'OpenMode' , 'retval' , ), 8, (8, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'SheetSize' , 'retval' , ), 9, (9, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'SheetSize' , 'retval' , ), 9, (9, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'SheetNum' , 'retval' , ), 10, (10, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Path' , 'retval' , ), 31, (31, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 64 , )),
	(( 'UserData' , 'retval' , ), 32, (32, (), [ (16393, 10, None, "IID('{33C2B049-DADF-11D2-882A-0060B0EF0A25}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 64 , )),
	(( 'LibraryType' , 'retval' , ), 33, (33, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 64 , )),
	(( 'ConstraintObjectDefinitions' , 'retval' , ), 50, (50, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 64 , )),
	(( 'GetName' , 'Flag' , 'retval' , ), 11, (11, (), [ (3, 1, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'GetBboxPoint' , 'Location' , 'retval' , ), 12, (12, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{AE729498-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'SetZSheetSize' , 'Width' , 'Height' , ), 13, (13, (), [ (3, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'DeSelectAll' , ), 14, (14, (), [ ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'AddArc' , 'X1' , 'Y1' , 'X2' , 'Y2' , 
			 'X3' , 'Y3' , 'retval' , ), 15, (15, (), [ (3, 1, None, None) , 
			 (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , 
			 (16393, 10, None, "IID('{AE729480-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'AddBox' , 'LowerLeftx' , 'LowerLefty' , 'UpperRightx' , 'UpperRighty' , 
			 'retval' , ), 16, (16, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , 
			 (3, 1, None, None) , (16393, 10, None, "IID('{AE729486-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'AddCircle' , 'Centerx' , 'Centery' , 'Radius' , 'retval' , 
			 ), 17, (17, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16393, 10, None, "IID('{AE729488-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'AddComponent' , 'SymbolName' , 'Locationx' , 'Locationy' , 'retval' , 
			 ), 18, (18, (), [ (8, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16393, 10, None, "IID('{AE72948A-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 64 , )),
	(( 'AddFub' , 'FubName' , 'LowerLeftx' , 'LowerLefty' , 'UpperRightx' , 
			 'UpperRighty' , 'retval' , ), 19, (19, (), [ (8, 1, None, None) , (3, 1, None, None) , 
			 (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16393, 10, None, "IID('{AE72948A-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'AddNet' , 'Locationx1' , 'Locationy1' , 'Locationx2' , 'Locationy2' , 
			 'CompPin1' , 'CompPin2' , 'BusOrWire' , 'retval' , ), 20, (20, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (9, 1, None, "IID('{AE72948C-9683-11CE-8246-00001B4D36B5}')") , 
			 (9, 1, None, "IID('{AE72948C-9683-11CE-8246-00001B4D36B5}')") , (3, 1, None, None) , (16393, 10, None, "IID('{AE729492-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'AddPin' , 'X' , 'Y' , 'retval' , ), 21, (21, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (16393, 10, None, "IID('{AE729496-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'AddText' , 'TextString' , 'X' , 'Y' , 'retval' , 
			 ), 22, (22, (), [ (8, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16393, 10, None, "IID('{AE72949C-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'AddAttribute' , 'String' , 'X' , 'Y' , 'Visibility' , 
			 'retval' , ), 23, (23, (), [ (8, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , 
			 (3, 1, None, None) , (16393, 10, None, "IID('{AE729482-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'ChangeComponent' , 'OldComp' , 'NewComp' , 'retval' , ), 24, (24, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'AddComponentMoveMode' , 'SymbolName' , 'InitialLocationX' , 'InitialLocationY' , 'retval' , 
			 ), 25, (25, (), [ (8, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16393, 10, None, "IID('{AE72948A-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 296 , (3, 0, None, None) , 64 , )),
	(( 'DeleteSelected' , 'delUnc' , ), 26, (26, (), [ (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'GetBatchAttributes' , 'retval' , ), 27, (27, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'AddBatchAttributes' , 'AttributeListString' , 'retval' , ), 28, (28, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'AddLine' , 'Pt1' , 'Pt2' , 'retval' , ), 29, (29, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (16393, 10, None, "IID('{AE729490-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'FindAttribute' , 'AttributeName' , 'retval' , ), 30, (30, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{AE729482-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'ApplySymbolUpdate' , 'SelectedOnly' , 'Slot' , ), 34, (34, (), [ (3, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'PromoteSymbolNumbers' , 'SelectedOnly' , 'Slot' , ), 35, (35, (), [ (3, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'RepositionAttributesAsOnSymbol' , 'SelectedOnly' , ), 36, (36, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'ClearHighlight' , 'SelectedOnly' , ), 37, (37, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'InsertBorder' , ), 38, (38, (), [ ], 1 , 1 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'DeleteBorder' , ), 39, (39, (), [ ], 1 , 1 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'ChangeBorder' , 'NewBorder' , ), 40, (40, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'UpdateBorder' , ), 41, (41, (), [ ], 1 , 1 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'ChangeComponentPreserveRefdes' , 'OldComp' , 'NewComp' , 'retval' , ), 42, (42, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'GetPackagedAttributeValues' , 'ObjectName' , 'ObjectType' , 'AttributeNameList' , 'retval' , 
			 ), 43, (43, (), [ (8, 1, None, None) , (3, 1, None, None) , (8, 1, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 416 , (3, 0, None, None) , 64 , )),
	(( 'SetPackagedAttributeValue' , 'ObjectName' , 'ObjectType' , 'AttributeName' , 'AttributeValue' , 
			 'IsOat' , 'SyncCms' , 'retval' , ), 44, (44, (), [ (8, 1, None, None) , 
			 (3, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , (11, 1, None, None) , (11, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 424 , (3, 0, None, None) , 64 , )),
	(( 'DeletePackagedAttribute' , 'ObjectName' , 'ObjectType' , 'AttributeName' , 'SyncCms' , 
			 'retval' , ), 45, (45, (), [ (8, 1, None, None) , (3, 1, None, None) , (8, 1, None, None) , 
			 (11, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 432 , (3, 0, None, None) , 64 , )),
	(( 'GetAttributeValues' , 'ObjectName' , 'ObjectType' , 'AttributeNameList' , 'retval' , 
			 ), 46, (46, (), [ (8, 1, None, None) , (3, 1, None, None) , (8, 1, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 440 , (3, 0, None, None) , 64 , )),
	(( 'SetAttributeValue' , 'ObjectName' , 'ObjectType' , 'AttributeName' , 'AttributeValue' , 
			 'IsOat' , 'retval' , ), 47, (47, (), [ (8, 1, None, None) , (3, 1, None, None) , 
			 (8, 1, None, None) , (8, 1, None, None) , (11, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 448 , (3, 0, None, None) , 64 , )),
	(( 'DeleteAttribute' , 'ObjectName' , 'ObjectType' , 'AttributeName' , 'retval' , 
			 ), 48, (48, (), [ (8, 1, None, None) , (3, 1, None, None) , (8, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 456 , (3, 0, None, None) , 64 , )),
	(( 'GetPackagedName' , 'GraphicalName' , 'ObjectType' , 'retval' , ), 49, (49, (), [ 
			 (8, 1, None, None) , (3, 1, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 464 , (3, 0, None, None) , 64 , )),
	(( 'AddComponentMoveModeEx' , 'SymbolName' , 'InitialLocationX' , 'InitialLocationY' , 'bAddNets' , 
			 'bLabelNets' , 'retval' , ), 51, (51, (), [ (8, 1, None, None) , (3, 1, None, None) , 
			 (3, 1, None, None) , (11, 1, None, None) , (11, 1, None, None) , (16393, 10, None, "IID('{AE72948A-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 472 , (3, 0, None, None) , 64 , )),
	(( 'StartUndoTransaction' , ), 52, (52, (), [ ], 1 , 1 , 4 , 0 , 480 , (3, 0, None, None) , 64 , )),
	(( 'EndUndoTransaction' , ), 53, (53, (), [ ], 1 , 1 , 4 , 0 , 488 , (3, 0, None, None) , 64 , )),
	(( 'IsFub' , 'retval' , ), 54, (54, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( 'CheckIfWirUpToDateWithCDB' , 'retval' , ), 55, (55, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 504 , (3, 0, None, None) , 64 , )),
	(( 'SetBoundingBox' , 'OriginX' , 'OriginY' , 'Width' , 'Height' , 
			 ), 56, (56, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 512 , (3, 0, None, None) , 64 , )),
	(( 'AddPinAtLocation' , 'X1' , 'Y1' , 'X2' , 'Y2' , 
			 'retval' , ), 57, (57, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , 
			 (3, 1, None, None) , (16393, 10, None, "IID('{AE729496-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
	(( 'AddSymbolInstance' , 'SymbolPartitionName' , 'SymbolName' , 'Locationx' , 'Locationy' , 
			 'retval' , ), 58, (58, (), [ (8, 1, None, None) , (8, 1, None, None) , (3, 1, None, None) , 
			 (3, 1, None, None) , (16393, 10, None, "IID('{AE72948A-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 528 , (3, 0, None, None) , 0 , )),
	(( 'AddPartInstance' , 'PartPartitionName' , 'DeviceName' , 'SymbolName' , 'Locationx' , 
			 'Locationy' , 'retval' , ), 59, (59, (), [ (8, 1, None, None) , (8, 1, None, None) , 
			 (8, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16393, 10, None, "IID('{AE72948A-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 536 , (3, 0, None, None) , 0 , )),
	(( 'GetChildBlock' , 'retval' , ), 60, (60, (), [ (16393, 10, None, "IID('{AE729484-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 544 , (3, 0, None, None) , 0 , )),
	(( 'IsBorderSymbol' , 'retval' , ), 61, (61, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 552 , (3, 0, None, None) , 64 , )),
	(( 'IsValid' , 'retval' , ), 62, (62, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 560 , (3, 0, None, None) , 64 , )),
	(( 'AddReuseBlockInstance' , 'ReuseType' , 'RBSymbolName' , 'ModifierType' , 'ModifierValue' , 
			 'bAddNets' , 'bLabelNets' , 'Locationx' , 'Locationy' , 'retval' , 
			 ), 63, (63, (), [ (3, 1, None, None) , (8, 1, None, None) , (3, 1, None, None) , (8, 1, None, None) , 
			 (11, 1, None, None) , (11, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16393, 10, None, "IID('{AE72948A-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 568 , (3, 0, None, None) , 64 , )),
	(( 'AddReuseBlockInstanceEx' , 'ReuseType' , 'RBSymbolName' , 'pMergeData' , 'ModifierType' , 
			 'ModifierValue' , 'bAddNets' , 'bLabelNets' , 'Locationx' , 'Locationy' , 
			 'retval' , ), 64, (64, (), [ (3, 1, None, None) , (8, 1, None, None) , (9, 1, None, "IID('{4584E756-C172-4389-AD41-AEE82CB45759}')") , 
			 (3, 1, None, None) , (8, 1, None, None) , (11, 1, None, None) , (11, 1, None, None) , (3, 1, None, None) , 
			 (3, 1, None, None) , (16393, 10, None, "IID('{AE72948A-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 576 , (3, 0, None, None) , 64 , )),
	(( 'GetReuseBlockMergeData' , 'ReuseType' , 'RBSymbolName' , 'retval' , ), 65, (65, (), [ 
			 (3, 1, None, None) , (8, 1, None, None) , (16393, 10, None, "IID('{4584E756-C172-4389-AD41-AEE82CB45759}')") , ], 1 , 1 , 4 , 0 , 584 , (3, 0, None, None) , 64 , )),
	(( 'IsReadOnly' , 'retval' , ), 66, (66, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 592 , (3, 0, None, None) , 64 , )),
	(( 'DisableUpdateStoring' , ), 67, (67, (), [ ], 1 , 1 , 4 , 0 , 600 , (3, 0, None, None) , 64 , )),
	(( 'EnableUpdateStoring' , ), 68, (68, (), [ ], 1 , 1 , 4 , 0 , 608 , (3, 0, None, None) , 64 , )),
	(( 'DisplayType' , 'retval' , ), 69, (69, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 616 , (3, 0, None, None) , 64 , )),
	(( 'DisplayType' , 'retval' , ), 69, (69, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 624 , (3, 0, None, None) , 64 , )),
	(( 'AddLine2' , 'X1' , 'Y1' , 'X2' , 'Y2' , 
			 'retval' , ), 70, (70, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , 
			 (3, 1, None, None) , (16393, 10, None, "IID('{AE729490-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 632 , (3, 0, None, None) , 0 , )),
	(( 'MoveSelected' , 'dx' , 'dy' , ), 71, (71, (), [ (3, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 640 , (3, 0, None, None) , 64 , )),
	(( 'AddCompositeComponentMoveMode' , 'SymbolPath' , 'ProjectFilePath' , 'retval' , ), 72, (72, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (16393, 10, None, "IID('{AE72948A-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 648 , (3, 0, None, None) , 64 , )),
	(( 'GetForwardPCB' , 'retval' , ), 73, (73, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 656 , (3, 0, None, None) , 64 , )),
	(( 'UpdateOutline' , 'retval' , ), 74, (74, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 664 , (3, 0, None, None) , 0 , )),
	(( 'AddFrameBoard' , 'LowerLeftx' , 'LowerLefty' , 'UpperRightx' , 'UpperRighty' , 
			 'retval' , ), 75, (75, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , 
			 (3, 1, None, None) , (16393, 10, None, "IID('{EB52D85C-D244-4993-9FF6-5B3167ACDE01}')") , ], 1 , 1 , 4 , 0 , 672 , (3, 0, None, None) , 64 , )),
	(( 'ArraySelected' , 'nRows' , 'nColumns' , ), 76, (76, (), [ (3, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 680 , (3, 0, None, None) , 64 , )),
	(( 'AddNetEx' , 'Locationx1' , 'Locationy1' , 'Locationx2' , 'Locationy2' , 
			 'CompPin1' , 'CompPin2' , 'BusOrWire' , 'retval' , ), 77, (77, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (9, 1, None, "IID('{AE72948C-9683-11CE-8246-00001B4D36B5}')") , 
			 (9, 1, None, "IID('{AE72948C-9683-11CE-8246-00001B4D36B5}')") , (3, 1, None, None) , (16393, 10, None, "IID('{AE729492-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 688 , (3, 0, None, None) , 0 , )),
	(( 'DissolveReuseBlock' , 'PartitionName' , 'SymbolName' , ), 78, (78, (), [ (8, 1, None, None) , 
			 (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 696 , (3, 0, None, None) , 64 , )),
]

IVdBox_vtables_dispatch_ = 1
IVdBox_vtables_ = [
	(( 'Type' , 'retval' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'FillStyle' , 'retval' , ), 2, (2, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'FillStyle' , 'retval' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'LineStyle' , 'retval' , ), 3, (3, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'LineStyle' , 'retval' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Application' , 'retval' , ), 4, (4, (), [ (16393, 10, None, "IID('{EA4ABD71-84B0-11CE-8237-00001B4D36B5}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'retval' , ), 5, (5, (), [ (16393, 10, None, "IID('{AE729484-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'retval' , ), 11, (11, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 64 , )),
	(( 'Color' , 'retval' , ), 11, (11, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 64 , )),
	(( 'Selected' , ), 12, (12, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( '_SetSelected' , 'Flag' , ), 6, (6, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 64 , )),
	(( 'SetLocation' , 'X1' , 'Y1' , 'X2' , 'Y2' , 
			 ), 7, (7, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'GetLocation' , 'Flag' , 'retval' , ), 8, (8, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{AE729498-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( '_GetColor' , 'retval' , ), 9, (9, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 64 , )),
	(( '_SetColor' , 'newColor' , ), 10, (10, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 64 , )),
	(( 'SetObjectColor' , 'newColor' , ), 13, (13, (), [ (9, 1, None, "IID('{C1031A0C-15BD-4897-A3E5-4C615CDEA684}')") , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'GetObjectColor' , 'retval' , ), 14, (14, (), [ (16393, 10, None, "IID('{C1031A0C-15BD-4897-A3E5-4C615CDEA684}')") , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'SetAutomaticColor' , 'bAutomatic' , ), 15, (15, (), [ (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'IsColorAutomatic' , 'retval' , ), 16, (16, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'SetObjectFillColor' , 'newColor' , ), 17, (17, (), [ (9, 1, None, "IID('{C1031A0C-15BD-4897-A3E5-4C615CDEA684}')") , ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'GetObjectFillColor' , 'retval' , ), 18, (18, (), [ (16393, 10, None, "IID('{C1031A0C-15BD-4897-A3E5-4C615CDEA684}')") , ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'SetAutomaticFillColor' , 'bAutomatic' , ), 19, (19, (), [ (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'IsFillColorAutomatic' , 'retval' , ), 20, (20, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'GetGradientType' , 'retval' , ), 21, (21, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 64 , )),
	(( 'SetGradientType' , 'newType' , ), 22, (22, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 64 , )),
	(( 'GetObjectGradientPrimaryColor' , 'retval' , ), 23, (23, (), [ (16393, 10, None, "IID('{C1031A0C-15BD-4897-A3E5-4C615CDEA684}')") , ], 1 , 1 , 4 , 0 , 256 , (3, 0, None, None) , 64 , )),
	(( 'SetObjectGradientPrimaryColor' , 'newColor' , ), 24, (24, (), [ (9, 1, None, "IID('{C1031A0C-15BD-4897-A3E5-4C615CDEA684}')") , ], 1 , 1 , 4 , 0 , 264 , (3, 0, None, None) , 64 , )),
	(( 'GetObjectGradientSecondaryColor' , 'retval' , ), 25, (25, (), [ (16393, 10, None, "IID('{C1031A0C-15BD-4897-A3E5-4C615CDEA684}')") , ], 1 , 1 , 4 , 0 , 272 , (3, 0, None, None) , 64 , )),
	(( 'SetObjectGradientSecondaryColor' , 'newColor' , ), 26, (26, (), [ (9, 1, None, "IID('{C1031A0C-15BD-4897-A3E5-4C615CDEA684}')") , ], 1 , 1 , 4 , 0 , 280 , (3, 0, None, None) , 64 , )),
	(( 'GetDropShadow' , 'retval' , ), 27, (27, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 288 , (3, 0, None, None) , 64 , )),
	(( 'SetDropShadow' , 'bDropShadow' , ), 28, (28, (), [ (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 296 , (3, 0, None, None) , 64 , )),
	(( 'GetShadowOpacity' , 'retval' , ), 29, (29, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 304 , (3, 0, None, None) , 64 , )),
	(( 'SetShadowOpacity' , 'newOpacity' , ), 30, (30, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 312 , (3, 0, None, None) , 64 , )),
]

IVdCircle_vtables_dispatch_ = 1
IVdCircle_vtables_ = [
	(( 'Type' , 'retval' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'FillStyle' , 'retval' , ), 2, (2, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'FillStyle' , 'retval' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'LineStyle' , 'retval' , ), 3, (3, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'LineStyle' , 'retval' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Application' , 'retval' , ), 4, (4, (), [ (16393, 10, None, "IID('{EA4ABD71-84B0-11CE-8237-00001B4D36B5}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'retval' , ), 5, (5, (), [ (16393, 10, None, "IID('{AE729484-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Radius' , 'retval' , ), 6, (6, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Radius' , 'retval' , ), 6, (6, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'retval' , ), 12, (12, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 64 , )),
	(( 'Color' , 'retval' , ), 12, (12, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 64 , )),
	(( 'Selected' , ), 13, (13, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( '_SetSelected' , 'Flag' , ), 7, (7, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 64 , )),
	(( 'GetCenter' , 'retval' , ), 8, (8, (), [ (16393, 10, None, "IID('{AE729498-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'SetCenter' , 'X' , 'Y' , ), 9, (9, (), [ (3, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( '_SetColor' , 'newColor' , ), 10, (10, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 64 , )),
	(( '_GetColor' , 'retval' , ), 11, (11, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 64 , )),
	(( 'SetObjectColor' , 'newColor' , ), 14, (14, (), [ (9, 1, None, "IID('{C1031A0C-15BD-4897-A3E5-4C615CDEA684}')") , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'GetObjectColor' , 'retval' , ), 15, (15, (), [ (16393, 10, None, "IID('{C1031A0C-15BD-4897-A3E5-4C615CDEA684}')") , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'SetAutomaticColor' , 'bAutomatic' , ), 16, (16, (), [ (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'IsColorAutomatic' , 'retval' , ), 17, (17, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'SetObjectFillColor' , 'newColor' , ), 18, (18, (), [ (9, 1, None, "IID('{C1031A0C-15BD-4897-A3E5-4C615CDEA684}')") , ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'GetObjectFillColor' , 'retval' , ), 19, (19, (), [ (16393, 10, None, "IID('{C1031A0C-15BD-4897-A3E5-4C615CDEA684}')") , ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'SetAutomaticFillColor' , 'bAutomatic' , ), 20, (20, (), [ (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'IsFillColorAutomatic' , 'retval' , ), 21, (21, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
]

IVdCmpPin_vtables_dispatch_ = 1
IVdCmpPin_vtables_ = [
	(( 'Attributes' , 'retval' , ), 1, (1, (), [ (16393, 10, None, "IID('{BD2EDF77-7E28-11CE-822D-00001B4D36B7}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'retval' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Application' , 'retval' , ), 3, (3, (), [ (16393, 10, None, "IID('{EA4ABD71-84B0-11CE-8237-00001B4D36B5}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'retval' , ), 4, (4, (), [ (16393, 10, None, "IID('{AE72948A-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Number' , 'retval' , ), 5, (5, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Number' , 'retval' , ), 5, (5, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Side' , 'retval' , ), 6, (6, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Selected' , ), 14, (14, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Component' , 'retval' , ), 15, (15, (), [ (16393, 10, None, "IID('{AE72948A-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Pin' , 'retval' , ), 16, (16, (), [ (16393, 10, None, "IID('{AE729496-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( '_SetSelected' , 'Flag' , ), 7, (7, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 64 , )),
	(( 'GetLocation' , 'retval' , ), 8, (8, (), [ (16393, 10, None, "IID('{AE729498-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'AddAttribute' , 'String' , 'X' , 'Y' , 'Visibility' , 
			 'retval' , ), 9, (9, (), [ (8, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , 
			 (3, 1, None, None) , (16393, 10, None, "IID('{AE729482-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'AddOat' , 'String' , 'retval' , ), 10, (10, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{AE729482-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( '_GetPin' , 'retval' , ), 11, (11, (), [ (16393, 10, None, "IID('{AE729496-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 64 , )),
	(( '_GetComp' , 'retval' , ), 12, (12, (), [ (16393, 10, None, "IID('{AE72948A-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 64 , )),
	(( 'FindAttribute' , 'AttributeName' , 'retval' , ), 13, (13, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{AE729482-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Connection' , 'retval' , ), 17, (17, (), [ (16393, 10, None, "IID('{1446F3C0-2169-11D0-91A7-7A9695000000}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
]

IVdComp_vtables_dispatch_ = 1
IVdComp_vtables_ = [
	(( 'Attributes' , 'retval' , ), 1, (1, (), [ (16393, 10, None, "IID('{BD2EDF77-7E28-11CE-822D-00001B4D36B7}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Label' , 'retval' , ), 2, (2, (), [ (16393, 10, None, "IID('{AE72948E-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'retval' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Orientation' , 'retval' , ), 4, (4, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Orientation' , 'retval' , ), 4, (4, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'UID' , 'retval' , ), 5, (5, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Id' , 'retval' , ), 6, (6, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Scale' , 'retval' , ), 7, (7, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Scale' , 'retval' , ), 7, (7, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Refdes' , 'retval' , ), 8, (8, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Refdes' , 'retval' , ), 8, (8, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Application' , 'retval' , ), 9, (9, (), [ (16393, 10, None, "IID('{EA4ABD71-84B0-11CE-8237-00001B4D36B5}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'retval' , ), 10, (10, (), [ (16393, 10, None, "IID('{AE729484-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'SymbolBlock' , 'retval' , ), 11, (11, (), [ (16393, 10, None, "IID('{AE729484-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Selected' , ), 26, (26, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( '_SetSelected' , 'Flag' , ), 12, (12, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 64 , )),
	(( 'GetLocation' , 'retval' , ), 13, (13, (), [ (16393, 10, None, "IID('{AE729498-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'SetLocation' , 'X' , 'Y' , ), 14, (14, (), [ (3, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'GetName' , 'Flag' , 'retval' , ), 15, (15, (), [ (3, 1, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'GetBboxPoint' , 'Location' , 'retval' , ), 16, (16, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{AE729498-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'AddAttribute' , 'String' , 'X' , 'Y' , 'Visibility' , 
			 'retval' , ), 17, (17, (), [ (8, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , 
			 (3, 1, None, None) , (16393, 10, None, "IID('{AE729482-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'AddLabel' , 'String' , 'X' , 'Y' , 'retval' , 
			 ), 18, (18, (), [ (8, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16393, 10, None, "IID('{AE72948E-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'AddOat' , 'String' , 'retval' , ), 19, (19, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{AE729482-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'AddBatchAttributes' , 'AttributeListSting' , 'retval' , ), 20, (20, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'GetBatchAttributes' , 'retval' , ), 21, (21, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'GetConnections' , 'retval' , ), 22, (22, (), [ (16393, 10, None, "IID('{BD2EDF77-7E28-11CE-822D-00001B4D36B7}')") , ], 1 , 1 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'FindAttribute' , 'AttributeString' , 'retval' , ), 23, (23, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{AE729482-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'AddBatchOats' , 'AttributeListSting' , 'retval' , ), 24, (24, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'GetBatchOats' , 'retval' , ), 25, (25, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'ActivateMoveMode' , 'retval' , ), 27, (27, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 288 , (3, 0, None, None) , 64 , )),
	(( 'GetForwardPCB' , 'retval' , ), 28, (28, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'SetForwardPCB' , 'forwardPCBValue' , ), 29, (29, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 304 , (3, 0, None, None) , 64 , )),
	(( 'ExtractSchematic' , ), 30, (30, (), [ ], 1 , 1 , 4 , 0 , 312 , (3, 0, None, None) , 64 , )),
]

IVdConnection_vtables_dispatch_ = 1
IVdConnection_vtables_ = [
	(( 'CompPin' , 'retval' , ), 4, (4, (), [ (16393, 10, None, "IID('{AE72948C-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Net' , 'retval' , ), 5, (5, (), [ (16393, 10, None, "IID('{AE729492-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Segment' , 'retval' , ), 6, (6, (), [ (16393, 10, None, "IID('{AE72949A-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( '_GetCompPin' , 'retval' , ), 1, (1, (), [ (16393, 10, None, "IID('{AE72948C-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 64 , )),
	(( '_GetNet' , 'retval' , ), 2, (2, (), [ (16393, 10, None, "IID('{AE729492-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 64 , )),
	(( '_GetSegment' , 'retval' , ), 3, (3, (), [ (16393, 10, None, "IID('{AE72949A-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 64 , )),
	(( 'Ripper' , 'retval' , ), 7, (7, (), [ (16393, 10, None, "IID('{FE3DB4AE-6C5C-426D-93A7-1308F624DDD9}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
]

IVdDoc_vtables_dispatch_ = 1
IVdDoc_vtables_ = [
	(( 'Application' , 'retval' , ), 1, (1, (), [ (16393, 10, None, "IID('{EA4ABD71-84B0-11CE-8237-00001B4D36B5}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Visible' , 'retval' , ), 2, (2, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Visible' , 'retval' , ), 2, (2, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'FullName' , 'retval' , ), 3, (3, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'retval' , ), 4, (4, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'retval' , ), 5, (5, (), [ (16393, 10, None, "IID('{BD2EDF77-7E28-11CE-822D-00001B4D36B5}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Path' , 'retval' , ), 6, (6, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 64 , )),
	(( 'Saved' , 'retval' , ), 7, (7, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 64 , )),
	(( 'Activate' , ), 8, (8, (), [ ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Close' , 'SaveChanges' , 'FileName' , ), 9, (9, (), [ (11, 1, None, None) , 
			 (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Print' , 'From' , 'To' , 'Copies' , ), 10, (10, (), [ 
			 (2, 1, None, None) , (2, 1, None, None) , (2, 1, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'PrintOut' , 'From' , 'To' , 'Copies' , ), 11, (11, (), [ 
			 (2, 1, None, None) , (2, 1, None, None) , (2, 1, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Save' , ), 12, (12, (), [ ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 64 , )),
	(( 'SaveAs' , 'FileName' , ), 13, (13, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 64 , )),
	(( 'GetViews' , 'retval' , ), 14, (14, (), [ (16393, 10, None, "IID('{DC3A8AF0-91B4-11CE-8243-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'ReRead' , 'SheetNumber' , 'retval' , ), 15, (15, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Open' , 'FileName' , 'retval' , ), 16, (16, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 64 , )),
	(( 'SaveAndCheck' , ), 17, (17, (), [ ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 64 , )),
	(( 'ExportMetafile' , 'OutputName' , ), 18, (18, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'IsAccess' , 'AccessType' , 'retval' , ), 19, (19, (), [ (3, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'DataType' , 'retval' , ), 20, (20, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'CancelSave' , 'DoNotWarn' , ), 21, (21, (), [ (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'UpdateSymbolInDesign' , ), 22, (22, (), [ ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'DiscardSymbolChanges' , ), 23, (23, (), [ ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'DataManagementEntity' , '__MIDL__IVdDoc0000' , ), 24, (24, (), [ (16393, 10, None, "IID('{03BE5928-2002-4CCB-818D-775ED6115A41}')") , ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
]

IVdDocs_vtables_dispatch_ = 1
IVdDocs_vtables_ = [
	(( 'Count' , 'retval' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Application' , 'retval' , ), 2, (2, (), [ (16393, 10, None, "IID('{EA4ABD71-84B0-11CE-8237-00001B4D36B5}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'retval' , ), 3, (3, (), [ (16393, 10, None, "IID('{EA4ABD71-84B0-11CE-8237-00001B4D36B5}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Index' , 'retval' , ), 4, (4, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{4ADEF4E2-690A-11CE-9261-0020C5E26659}')") , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'retval' , ), 5, (5, (), [ (16393, 10, None, "IID('{4ADEF4E2-690A-11CE-9261-0020C5E26659}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Close' , ), 6, (6, (), [ ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Open' , 'FileName' , 'retval' , ), 7, (7, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{4ADEF4E2-690A-11CE-9261-0020C5E26659}')") , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'SelectPath' , 'FileName' , 'HierPath' , 'SheetNumber' , 'Type' , 
			 'retval' , ), 8, (8, (), [ (8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , 
			 (3, 1, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'SelectPathCompPin' , 'FileName' , 'HierPath' , 'SheetNumber' , 'PinNumber' , 
			 'SelectType' , 'retval' , ), 9, (9, (), [ (8, 1, None, None) , (8, 1, None, None) , 
			 (8, 1, None, None) , (8, 1, None, None) , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'SaveAll' , ), 10, (10, (), [ ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
]

IVdFrameBoard_vtables_dispatch_ = 1
IVdFrameBoard_vtables_ = [
	(( 'Attributes' , 'retval' , ), 1, (1, (), [ (16393, 10, None, "IID('{BD2EDF77-7E28-11CE-822D-00001B4D36B7}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'retval' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'UID' , 'retval' , ), 3, (3, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Id' , 'retval' , ), 4, (4, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Application' , 'retval' , ), 5, (5, (), [ (16393, 10, None, "IID('{EA4ABD71-84B0-11CE-8237-00001B4D36B5}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'retval' , ), 6, (6, (), [ (16393, 10, None, "IID('{AE729484-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Selected' , ), 7, (7, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( '_SetSelected' , 'Flag' , ), 8, (8, (), [ (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 64 , )),
	(( 'SetLocation' , 'X1' , 'Y1' , 'X2' , 'Y2' , 
			 ), 9, (9, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'GetLocation' , 'Flag' , 'retval' , ), 10, (10, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{AE729498-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'SetFrameBoardName' , 'NewName' , ), 11, (11, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'GetFrameBoardName' , 'retval' , ), 12, (12, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'IsClone' , 'retval' , ), 13, (13, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
]

IVdHighPrecisionObject_vtables_dispatch_ = 1
IVdHighPrecisionObject_vtables_ = [
	(( 'SetObject' , 'pObject' , ), 1, (1, (), [ (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'GetX' , '_unit' , 'retval' , ), 2, (2, (), [ (3, 1, None, None) , 
			 (16389, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'GetY' , '_unit' , 'retval' , ), 3, (3, (), [ (3, 1, None, None) , 
			 (16389, 10, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'SetX' , '_unit' , 'retval' , ), 4, (4, (), [ (3, 1, None, None) , 
			 (5, 1, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'SetY' , '_unit' , 'retval' , ), 5, (5, (), [ (3, 1, None, None) , 
			 (5, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'GetSize' , '_unit' , 'retval' , ), 6, (6, (), [ (3, 1, None, None) , 
			 (16389, 10, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'SetSize' , '_unit' , 'retval' , ), 7, (7, (), [ (3, 1, None, None) , 
			 (5, 1, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'GetSegmentX' , 'WhichJoint' , '_unit' , 'retval' , ), 8, (8, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (16389, 10, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'GetSegmentY' , 'WhichJoint' , '_unit' , 'retval' , ), 9, (9, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (16389, 10, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'SetSegmentX' , 'WhichJoint' , '_unit' , 'retval' , ), 10, (10, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (5, 1, None, None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'SetSegmentY' , 'WhichJoint' , '_unit' , 'retval' , ), 11, (11, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (5, 1, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
]

IVdICTAttr_vtables_dispatch_ = 1
IVdICTAttr_vtables_ = [
	(( 'Parent' , 'retval' , ), 100, (100, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
]

IVdICTBlock_vtables_dispatch_ = 1
IVdICTBlock_vtables_ = [
	(( 'Parent' , 'retval' , ), 100, (100, (), [ (16393, 10, None, "IID('{848E324F-125D-4236-981D-0EB202E628DA}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'AddInstance' , 'PartitionName' , 'SymbolName' , 'retval' , ), 101, (101, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (16393, 10, None, "IID('{4945AC27-6ADD-462C-B3F6-239842AFFEB9}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'AddNet' , 'Name' , 'retval' , ), 102, (102, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{9ED04F47-52F4-476A-8100-B8990AFE3ACD}')") , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'PromoteSymbolNumbers' , 'SelectedOnly' , 'Slot' , ), 103, (103, (), [ (3, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'GetNets' , 'retval' , ), 104, (104, (), [ (16393, 10, None, "IID('{BD2EDF77-7E28-11CE-822D-00001B4D36B7}')") , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'GetInstances' , 'retval' , ), 105, (105, (), [ (16393, 10, None, "IID('{BD2EDF77-7E28-11CE-822D-00001B4D36B7}')") , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'RemoveObject' , '__MIDL__IVdICTBlock0000' , 'retval' , ), 106, (106, (), [ (9, 1, None, "IID('{F692CCBA-DA51-43FB-B8D6-79EEA84B59CA}')") , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'ConnectObjects' , '__MIDL__IVdICTBlock0001' , '__MIDL__IVdICTBlock0002' , 'retval' , ), 107, (107, (), [ 
			 (9, 1, None, "IID('{F692CCBA-DA51-43FB-B8D6-79EEA84B59CA}')") , (9, 1, None, "IID('{F692CCBA-DA51-43FB-B8D6-79EEA84B59CA}')") , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'DisconnectObjects' , '__MIDL__IVdICTBlock0003' , '__MIDL__IVdICTBlock0004' , 'retval' , ), 108, (108, (), [ 
			 (9, 1, None, "IID('{F692CCBA-DA51-43FB-B8D6-79EEA84B59CA}')") , (9, 1, None, "IID('{F692CCBA-DA51-43FB-B8D6-79EEA84B59CA}')") , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'SetObjectName' , 'Name' , '__MIDL__IVdICTBlock0005' , 'retval' , ), 109, (109, (), [ 
			 (8, 1, None, None) , (9, 1, None, "IID('{F692CCBA-DA51-43FB-B8D6-79EEA84B59CA}')") , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
]

IVdICTComp_vtables_dispatch_ = 1
IVdICTComp_vtables_ = [
	(( 'Parent' , 'retval' , ), 100, (100, (), [ (16393, 10, None, "IID('{C64B5D5C-66D5-41FE-B4B3-EFC664EAED1B}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'GetAttributesNames' , 'AttrType' , 'retval' , ), 101, (101, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'GetAttributeValue' , 'AttrType' , 'Name' , 'retval' , ), 102, (102, (), [ 
			 (3, 1, None, None) , (8, 1, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'SetAttributeValue' , 'AttrType' , 'Name' , 'Value' , 'retval' , 
			 ), 103, (103, (), [ (3, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'RemAttributeValue' , 'AttrType' , 'Name' , 'retval' , ), 104, (104, (), [ 
			 (3, 1, None, None) , (8, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'GetDefName' , 'retval' , ), 105, (105, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'GetLibraryName' , 'retval' , ), 106, (106, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'GetPins' , 'retval' , ), 108, (108, (), [ (16393, 10, None, "IID('{BD2EDF77-7E28-11CE-822D-00001B4D36B7}')") , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
]

IVdICTDocument_vtables_dispatch_ = 1
IVdICTDocument_vtables_ = [
	(( 'Application' , 'retval' , ), 101, (101, (), [ (16393, 10, None, "IID('{EA4ABD71-84B0-11CE-8237-00001B4D36B5}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'retval' , ), 102, (102, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'FullName' , 'retval' , ), 103, (103, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'retval' , ), 104, (104, (), [ (16393, 10, None, "IID('{2A3CCA57-9C38-4484-A6A3-7521DDF7DAD0}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Activate' , ), 105, (105, (), [ ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Close' , 'SaveChanges' , 'FileName' , ), 106, (106, (), [ (11, 1, None, None) , 
			 (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Print' , 'From' , 'To' , 'Copies' , ), 107, (107, (), [ 
			 (2, 1, None, None) , (2, 1, None, None) , (2, 1, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'GetViews' , 'retval' , ), 108, (108, (), [ (16393, 10, None, "IID('{EA874DB4-9B4D-4E7F-BE4F-D41AD4A560DE}')") , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'IsReadOnly' , 'retval' , ), 116, (116, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'SetReadOnly' , 'ReadOnlyFlag' , ), 117, (117, (), [ (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
]

IVdICTNet_vtables_dispatch_ = 1
IVdICTNet_vtables_ = [
	(( 'Parent' , 'retval' , ), 100, (100, (), [ (16393, 10, None, "IID('{C64B5D5C-66D5-41FE-B4B3-EFC664EAED1B}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'GetPins' , 'retval' , ), 101, (101, (), [ (16393, 10, None, "IID('{BD2EDF77-7E28-11CE-822D-00001B4D36B7}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IVdICTObj_vtables_dispatch_ = 1
IVdICTObj_vtables_ = [
	(( 'ParentObject' , 'retval' , ), 1, (1, (), [ (16393, 10, None, "IID('{F692CCBA-DA51-43FB-B8D6-79EEA84B59CA}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'GetName' , 'retval' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'GetUID' , 'retval' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IVdICTPin_vtables_dispatch_ = 1
IVdICTPin_vtables_ = [
	(( 'Parent' , 'retval' , ), 100, (100, (), [ (16393, 10, None, "IID('{4945AC27-6ADD-462C-B3F6-239842AFFEB9}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'GetNets' , 'retval' , ), 101, (101, (), [ (16393, 10, None, "IID('{BD2EDF77-7E28-11CE-822D-00001B4D36B7}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IVdICTView_vtables_dispatch_ = 1
IVdICTView_vtables_ = [
	(( 'Block' , 'retval' , ), 100, (100, (), [ (16393, 10, None, "IID('{C64B5D5C-66D5-41FE-B4B3-EFC664EAED1B}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'AddReuseBlock' , 'partName' , 'SymbolName' , 'retval' , ), 108, (108, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 64 , )),
	(( 'SetSignalsView' , ), 102, (102, (), [ ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'SetSymbolsView' , ), 103, (103, (), [ ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'GetTopLevelDesignName' , 'retval' , ), 104, (104, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'GetName' , 'Flag' , 'retval' , ), 105, (105, (), [ (3, 1, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'SelectByName' , 'Name' , 'retval' , ), 106, (106, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Query' , 'Flags' , 'Selected' , 'retval' , ), 107, (107, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (16393, 10, None, "IID('{BD2EDF77-7E28-11CE-822D-00001B4D36B7}')") , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
]

IVdICTViews_vtables_dispatch_ = 1
IVdICTViews_vtables_ = [
	(( 'Count' , 'retval' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Application' , 'retval' , ), 2, (2, (), [ (16393, 10, None, "IID('{EA4ABD71-84B0-11CE-8237-00001B4D36B5}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'retval' , ), 3, (3, (), [ (16393, 10, None, "IID('{4ADEF4E2-690A-11CE-9261-0020C5E26659}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Index' , 'retval' , ), 4, (4, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{848E324F-125D-4236-981D-0EB202E628DA}')") , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

IVdLabel_vtables_dispatch_ = 1
IVdLabel_vtables_ = [
	(( 'TextString' , 'retval' , ), 1, (1, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'TextString' , 'retval' , ), 1, (1, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Visible' , 'retval' , ), 2, (2, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Visible' , 'retval' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'retval' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Font' , 'retval' , ), 4, (4, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Font' , 'retval' , ), 4, (4, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Origin' , 'retval' , ), 5, (5, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Origin' , 'retval' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Orientation' , 'retval' , ), 6, (6, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Orientation' , 'retval' , ), 6, (6, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Size' , 'retval' , ), 7, (7, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Size' , 'retval' , ), 7, (7, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Sense' , 'retval' , ), 8, (8, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Sense' , 'retval' , ), 8, (8, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Application' , 'retval' , ), 9, (9, (), [ (16393, 10, None, "IID('{EA4ABD71-84B0-11CE-8237-00001B4D36B5}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'retval' , ), 10, (10, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Scope' , 'retval' , ), 11, (11, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Scope' , 'retval' , ), 11, (11, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'retval' , ), 17, (17, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 64 , )),
	(( 'Color' , 'retval' , ), 17, (17, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 64 , )),
	(( 'Selected' , ), 18, (18, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'ResolvedName' , 'retval' , ), 19, (19, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Printable' , 'retval' , ), 24, (24, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 64 , )),
	(( 'Printable' , 'retval' , ), 24, (24, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 64 , )),
	(( '_SetSelected' , 'Flag' , ), 12, (12, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 256 , (3, 0, None, None) , 64 , )),
	(( 'GetLocation' , 'retval' , ), 13, (13, (), [ (16393, 10, None, "IID('{AE729498-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'SetLocation' , 'X' , 'Y' , ), 14, (14, (), [ (3, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( '_GetColor' , 'retval' , ), 15, (15, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 280 , (3, 0, None, None) , 64 , )),
	(( '_SetColor' , 'newColor' , ), 16, (16, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 288 , (3, 0, None, None) , 64 , )),
	(( 'SetObjectColor' , 'newColor' , ), 20, (20, (), [ (9, 1, None, "IID('{C1031A0C-15BD-4897-A3E5-4C615CDEA684}')") , ], 1 , 1 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'GetObjectColor' , 'retval' , ), 21, (21, (), [ (16393, 10, None, "IID('{C1031A0C-15BD-4897-A3E5-4C615CDEA684}')") , ], 1 , 1 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'SetAutomaticColor' , 'bAutomatic' , ), 22, (22, (), [ (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'IsColorAutomatic' , 'retval' , ), 23, (23, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
]

IVdLibrary_vtables_dispatch_ = 1
IVdLibrary_vtables_ = [
	(( 'Path' , 'retval' , ), 1, (1, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Path' , 'retval' , ), 1, (1, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Alias' , 'retval' , ), 2, (2, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Alias' , 'retval' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'retval' , ), 3, (3, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'retval' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IVdLine_vtables_dispatch_ = 1
IVdLine_vtables_ = [
	(( 'Type' , 'retval' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'FillStyle' , 'retval' , ), 2, (2, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 64 , )),
	(( 'FillStyle' , 'retval' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 64 , )),
	(( 'LineStyle' , 'retval' , ), 3, (3, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'LineStyle' , 'retval' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'retval' , ), 4, (4, (), [ (16393, 10, None, "IID('{AE729484-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Application' , 'retval' , ), 5, (5, (), [ (16393, 10, None, "IID('{EA4ABD71-84B0-11CE-8237-00001B4D36B5}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'retval' , ), 12, (12, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 64 , )),
	(( 'Color' , 'retval' , ), 12, (12, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 64 , )),
	(( 'Selected' , ), 13, (13, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( '_SetSelected' , 'Flag' , ), 6, (6, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 64 , )),
	(( '_GetColor' , 'retval' , ), 7, (7, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 64 , )),
	(( '_SetColor' , 'newColor' , 'retval' , ), 8, (8, (), [ (3, 1, None, None) , 
			 (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 64 , )),
	(( 'GetNumPoints' , 'retval' , ), 9, (9, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'AddPoint' , 'NewPoint' , 'retval' , ), 10, (10, (), [ (3, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'GetPoint' , 'PointNumber' , 'retval' , ), 11, (11, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{AE729498-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'SetObjectColor' , 'newColor' , ), 14, (14, (), [ (9, 1, None, "IID('{C1031A0C-15BD-4897-A3E5-4C615CDEA684}')") , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'GetObjectColor' , 'retval' , ), 15, (15, (), [ (16393, 10, None, "IID('{C1031A0C-15BD-4897-A3E5-4C615CDEA684}')") , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'SetAutomaticColor' , 'bAutomatic' , ), 16, (16, (), [ (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'IsColorAutomatic' , 'retval' , ), 17, (17, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'SetObjectFillColor' , 'newColor' , ), 18, (18, (), [ (9, 1, None, "IID('{C1031A0C-15BD-4897-A3E5-4C615CDEA684}')") , ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'GetObjectFillColor' , 'retval' , ), 19, (19, (), [ (16393, 10, None, "IID('{C1031A0C-15BD-4897-A3E5-4C615CDEA684}')") , ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'SetAutomaticFillColor' , 'bAutomatic' , ), 20, (20, (), [ (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'IsFillColorAutomatic' , 'retval' , ), 21, (21, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
]

IVdNet_vtables_dispatch_ = 1
IVdNet_vtables_ = [
	(( 'Attributes' , 'retval' , ), 1, (1, (), [ (16393, 10, None, "IID('{BD2EDF77-7E28-11CE-822D-00001B4D36B7}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'retval' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'FillStyle' , 'retval' , ), 3, (3, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 64 , )),
	(( 'FillStyle' , 'retval' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 64 , )),
	(( 'LineStyle' , 'retval' , ), 4, (4, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'LineStyle' , 'retval' , ), 4, (4, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'UID' , 'retval' , ), 5, (5, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Id' , 'retval' , ), 6, (6, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Application' , 'retval' , ), 7, (7, (), [ (16393, 10, None, "IID('{EA4ABD71-84B0-11CE-8237-00001B4D36B5}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'retval' , ), 8, (8, (), [ (16393, 10, None, "IID('{AE729484-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'retval' , ), 21, (21, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 64 , )),
	(( 'Color' , 'retval' , ), 21, (21, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 64 , )),
	(( 'Selected' , ), 22, (22, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( '_SetSelected' , 'Flag' , ), 9, (9, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 64 , )),
	(( 'AddOat' , 'String' , 'retval' , ), 10, (10, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{AE729482-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 64 , )),
	(( 'AddAttribute' , 'Segment' , 'String' , 'X' , 'Y' , 
			 'Visibility' , 'retval' , ), 11, (11, (), [ (9, 1, None, "IID('{AE72949A-9683-11CE-8246-00001B4D36B5}')") , (8, 1, None, None) , 
			 (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16393, 10, None, "IID('{AE729482-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'AddLabel' , 'Segment' , 'String' , 'X' , 'Y' , 
			 'retval' , ), 12, (12, (), [ (9, 1, None, "IID('{AE72949A-9683-11CE-8246-00001B4D36B5}')") , (8, 1, None, None) , (3, 1, None, None) , 
			 (3, 1, None, None) , (16393, 10, None, "IID('{AE72948E-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'GetLabel' , 'Segment' , 'retval' , ), 13, (13, (), [ (9, 1, None, "IID('{AE72949A-9683-11CE-8246-00001B4D36B5}')") , 
			 (16393, 10, None, "IID('{AE72948E-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'GetSegments' , 'retval' , ), 14, (14, (), [ (16393, 10, None, "IID('{BD2EDF77-7E28-11CE-822D-00001B4D36B7}')") , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( '_SetColor' , 'newColor' , ), 15, (15, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 64 , )),
	(( '_GetColor' , 'retval' , ), 16, (16, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 64 , )),
	(( 'FindAttribute' , 'AttributeName' , 'retval' , ), 17, (17, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{AE729482-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'GetSingleJointLocs' , 'retval' , ), 18, (18, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'SelectSegment' , 'Segment' , ), 19, (19, (), [ (9, 1, None, "IID('{AE72949A-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'SelectSegmentByJointLoc' , 'XCoordinate' , 'YCoordinate' , 'JointType' , ), 20, (20, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Connections' , 'PinNameFilter' , 'retval' , ), 23, (23, (), [ (12, 17, None, None) , 
			 (16393, 10, None, "IID('{BD2EDF77-7E28-11CE-822D-00001B4D36B7}')") , ], 1 , 1 , 4 , 1 , 256 , (3, 0, None, None) , 0 , )),
	(( 'GetConnectedLabel' , 'Segment' , 'retval' , ), 24, (24, (), [ (9, 1, None, "IID('{AE72949A-9683-11CE-8246-00001B4D36B5}')") , 
			 (16393, 10, None, "IID('{AE72948E-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'IsSegmentSelected' , 'Segment' , 'retval' , ), 25, (25, (), [ (9, 1, None, "IID('{AE72949A-9683-11CE-8246-00001B4D36B5}')") , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'GetConnectedNetName' , 'Segment' , 'retval' , ), 26, (26, (), [ (9, 1, None, "IID('{AE72949A-9683-11CE-8246-00001B4D36B5}')") , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'GetSignals' , 'retval' , ), 27, (27, (), [ (16393, 10, None, "IID('{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')") , ], 1 , 1 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'GetRippers' , 'retval' , ), 28, (28, (), [ (16393, 10, None, "IID('{BD2EDF77-7E28-11CE-822D-00001B4D36B7}')") , ], 1 , 1 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'SetObjectColor' , 'newColor' , ), 29, (29, (), [ (9, 1, None, "IID('{C1031A0C-15BD-4897-A3E5-4C615CDEA684}')") , ], 1 , 1 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'GetObjectColor' , 'retval' , ), 30, (30, (), [ (16393, 10, None, "IID('{C1031A0C-15BD-4897-A3E5-4C615CDEA684}')") , ], 1 , 1 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'SetAutomaticColor' , 'bAutomatic' , ), 31, (31, (), [ (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'IsColorAutomatic' , 'retval' , ), 32, (32, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'LogicalNetName' , 'retval' , ), 33, (33, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 64 , )),
	(( 'Width' , 'retval' , ), 34, (34, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 344 , (3, 0, None, None) , 64 , )),
	(( 'Width' , 'retval' , ), 34, (34, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 64 , )),
]

IVdObjs_vtables_dispatch_ = 1
IVdObjs_vtables_ = [
	(( 'Count' , 'retval' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Application' , 'retval' , ), 2, (2, (), [ (16393, 10, None, "IID('{EA4ABD71-84B0-11CE-8237-00001B4D36B5}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'retval' , ), 3, (3, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Index' , 'retval' , ), 4, (4, (), [ (3, 1, None, None) , 
			 (16393, 10, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'GetType' , 'Index' , 'retval' , ), 5, (5, (), [ (3, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IVdPin_vtables_dispatch_ = 1
IVdPin_vtables_ = [
	(( 'Attributes' , 'retval' , ), 1, (1, (), [ (16393, 10, None, "IID('{BD2EDF77-7E28-11CE-822D-00001B4D36B7}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Label' , 'retval' , ), 2, (2, (), [ (16393, 10, None, "IID('{AE72948E-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'retval' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'UID' , 'retval' , ), 4, (4, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Id' , 'retval' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Sense' , 'retval' , ), 6, (6, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Sense' , 'retval' , ), 6, (6, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Application' , 'retval' , ), 7, (7, (), [ (16393, 10, None, "IID('{EA4ABD71-84B0-11CE-8237-00001B4D36B5}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'retval' , ), 8, (8, (), [ (16393, 10, None, "IID('{AE729484-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Side' , 'retval' , ), 9, (9, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'retval' , ), 19, (19, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 64 , )),
	(( 'Color' , 'retval' , ), 19, (19, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 64 , )),
	(( 'Selected' , ), 20, (20, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( '_SetSelected' , 'Flag' , ), 10, (10, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 64 , )),
	(( 'GetName' , 'Flag' , 'retval' , ), 11, (11, (), [ (3, 1, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'SetLocation' , 'XInterior' , 'YInterior' , 'XBoundary' , 'YBoundary' , 
			 ), 12, (12, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'GetLocation' , 'Flag' , 'retval' , ), 13, (13, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{AE729498-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'AddAttribute' , 'String' , 'X' , 'Y' , 'Visibility' , 
			 'retval' , ), 14, (14, (), [ (8, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , 
			 (3, 1, None, None) , (16393, 10, None, "IID('{AE729482-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'AddLabel' , 'String' , 'X' , 'Y' , 'retval' , 
			 ), 15, (15, (), [ (8, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16393, 10, None, "IID('{AE72948E-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 64 , )),
	(( '_GetColor' , 'retval' , ), 16, (16, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 64 , )),
	(( '_SetColor' , 'newColor' , ), 17, (17, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 64 , )),
	(( 'FindAttribute' , 'AttributeName' , 'retval' , ), 18, (18, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{AE729482-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'GetObjectColor' , 'retval' , ), 21, (21, (), [ (16393, 10, None, "IID('{C1031A0C-15BD-4897-A3E5-4C615CDEA684}')") , ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
]

IVdPoint_vtables_dispatch_ = 1
IVdPoint_vtables_ = [
	(( 'X' , 'retval' , ), 1, (1, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'X' , 'retval' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Y' , 'retval' , ), 2, (2, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Y' , 'retval' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

IVdRect_vtables_dispatch_ = 1
IVdRect_vtables_ = [
	(( 'Left' , 'retval' , ), 1, (1, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Left' , 'retval' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Bottom' , 'retval' , ), 2, (2, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Bottom' , 'retval' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Right' , 'retval' , ), 3, (3, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Right' , 'retval' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Top' , 'retval' , ), 4, (4, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Top' , 'retval' , ), 4, (4, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
]

IVdSchematicSheetDocument_vtables_dispatch_ = 1
IVdSchematicSheetDocument_vtables_ = [
	(( 'Application' , 'retval' , ), 101, (101, (), [ (16393, 10, None, "IID('{EA4ABD71-84B0-11CE-8237-00001B4D36B5}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'retval' , ), 102, (102, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'FullName' , 'retval' , ), 103, (103, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'retval' , ), 104, (104, (), [ (16393, 10, None, "IID('{608CA7F4-A52A-4206-9580-3BEB17CE0073}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Activate' , ), 105, (105, (), [ ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Close' , 'SaveChanges' , 'FileName' , ), 106, (106, (), [ (11, 1, None, None) , 
			 (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Print' , 'From' , 'To' , 'Copies' , ), 107, (107, (), [ 
			 (2, 1, None, None) , (2, 1, None, None) , (2, 1, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'GetViews' , 'retval' , ), 108, (108, (), [ (16393, 10, None, "IID('{DC3A8AF0-91B4-11CE-8243-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'ReRead' , 'SheetNumber' , 'retval' , ), 109, (109, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'ExportMetafile' , 'OutputName' , ), 110, (110, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'IsAccess' , 'AccessType' , 'retval' , ), 111, (111, (), [ (3, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 64 , )),
	(( 'DataType' , 'retval' , ), 112, (112, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 64 , )),
	(( 'CancelSave' , 'DoNotWarn' , ), 113, (113, (), [ (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 64 , )),
	(( 'InsertSheet' , 'DesignName' , 'SheetNumber' , 'retval' , ), 114, (114, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 64 , )),
	(( 'DeleteSheet' , 'DesignName' , 'SheetNumber' , 'retval' , ), 115, (115, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 64 , )),
	(( 'IsReadOnly' , 'retval' , ), 116, (116, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'SetReadOnly' , 'ReadOnlyFlag' , ), 117, (117, (), [ (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 64 , )),
	(( 'GetReadWriteRights' , 'retval' , ), 118, (118, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 64 , )),
	(( 'AcquireReadWriteRights' , 'AllowRights' , ), 119, (119, (), [ (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 64 , )),
	(( 'SetFollowingSheetRange' , 'Sheets' , ), 120, (120, (), [ (9, 1, None, "IID('{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')") , ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 64 , )),
	(( 'SetSheetName' , 'Name' , ), 121, (121, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 64 , )),
	(( 'UpdateSymbolInDesign' , ), 122, (122, (), [ ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'DiscardSymbolChanges' , ), 123, (123, (), [ ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Save' , ), 124, (124, (), [ ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'SaveAs' , 'FileName' , ), 125, (125, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
]

IVdSchematicSheetDocuments_vtables_dispatch_ = 1
IVdSchematicSheetDocuments_vtables_ = [
	(( 'Count' , 'retval' , ), 101, (101, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Application' , 'retval' , ), 102, (102, (), [ (16393, 10, None, "IID('{EA4ABD71-84B0-11CE-8237-00001B4D36B5}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'retval' , ), 103, (103, (), [ (16393, 10, None, "IID('{EA4ABD71-84B0-11CE-8237-00001B4D36B5}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Index' , 'retval' , ), 104, (104, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{D8B95AF2-D943-4295-8D86-71B4F904C3AA}')") , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'retval' , ), 105, (105, (), [ (16393, 10, None, "IID('{D8B95AF2-D943-4295-8D86-71B4F904C3AA}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 64 , )),
	(( 'Close' , ), 106, (106, (), [ ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Open_Hierarchically' , 'SchematicName' , 'SheetName' , 'HierPath' , 'retval' , 
			 ), 107, (107, (), [ (8, 1, None, None) , (8, 1, None, None) , (9, 1, None, "IID('{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')") , (16393, 10, None, "IID('{D8B95AF2-D943-4295-8D86-71B4F904C3AA}')") , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Open' , 'SchematicName' , 'SheetName' , 'retval' , ), 110, (110, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (16393, 10, None, "IID('{D8B95AF2-D943-4295-8D86-71B4F904C3AA}')") , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'OpenSymbol' , 'sSymbolName' , 'sSymbolExtension' , 'retval' , ), 123, (123, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (16393, 10, None, "IID('{D8B95AF2-D943-4295-8D86-71B4F904C3AA}')") , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'IsSymbolUnderEdit' , 'sSymbolName' , 'sSymbolExtension' , 'retval' , ), 124, (124, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'GetAvailableSchematics' , 'Schematics' , ), 108, (108, (), [ (16393, 10, None, "IID('{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')") , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'GetAvailableSheets' , 'Schematic' , 'Sheets' , ), 109, (109, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')") , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'CopySheetsToClipboard' , 'Schematic' , 'Sheets' , 'srcPaths' , ), 111, (111, (), [ 
			 (8, 1, None, None) , (9, 1, None, "IID('{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')") , (9, 1, None, "IID('{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')") , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 64 , )),
	(( 'PasteSheetsFromClipboard' , 'Schematic' , 'dstPaths' , 'replaceWithSheets' , ), 112, (112, (), [ 
			 (8, 1, None, None) , (9, 1, None, "IID('{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')") , (9, 1, None, "IID('{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')") , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 64 , )),
	(( 'IsSheetsClipboardEmpty' , 'bIsEmpty' , ), 113, (113, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 64 , )),
	(( 'CopyBlocksToClipboard' , 'Blocks' , ), 114, (114, (), [ (9, 1, None, "IID('{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')") , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 64 , )),
	(( 'PasteBlocksFromClipboard' , ), 115, (115, (), [ ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 64 , )),
	(( 'DetermineClipboardContent' , 'nContentType' , ), 116, (116, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 64 , )),
	(( 'InsertSheet' , 'SchematicName' , 'SheetNumber' , 'retval' , ), 117, (117, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'DeleteSheet' , 'SchematicName' , 'SheetNumber' , 'retval' , ), 118, (118, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'CopyToClipboard' , 'SchematicName' , 'SheetsToCopy' , 'srcPath' , ), 119, (119, (), [ 
			 (8, 1, None, None) , (9, 1, None, "IID('{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')") , (9, 1, None, "IID('{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')") , ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'PasteFromClipboard' , 'SchematicName' , 'dstPath' , 'SheetsToBeReplaced' , ), 120, (120, (), [ 
			 (8, 1, None, None) , (9, 1, None, "IID('{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')") , (9, 1, None, "IID('{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')") , ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'GetSheetOrder' , 'SchematicName' , 'sheetRange' , ), 121, (121, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')") , ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 64 , )),
	(( 'SetSheetOrder' , 'SchematicName' , 'sheetRange' , ), 122, (122, (), [ (8, 1, None, None) , 
			 (9, 1, None, "IID('{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}')") , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 64 , )),
]

IVdSegment_vtables_dispatch_ = 1
IVdSegment_vtables_ = [
	(( 'Type' , 'retval' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Attributes' , 'retval' , ), 2, (2, (), [ (16393, 10, None, "IID('{BD2EDF77-7E28-11CE-822D-00001B4D36B7}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Application' , 'retval' , ), 3, (3, (), [ (16393, 10, None, "IID('{EA4ABD71-84B0-11CE-8237-00001B4D36B5}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'retval' , ), 4, (4, (), [ (16393, 10, None, "IID('{AE729492-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'IsBus' , 'retval' , ), 5, (5, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Location' , 'WhichJoint' , 'retval' , ), 6, (6, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{AE729498-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'GetJointType' , 'WhichJoint' , 'retval' , ), 7, (7, (), [ (3, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'SetLocation' , 'WhichJoint' , 'newCoord' , ), 8, (8, (), [ (3, 1, None, None) , 
			 (9, 1, None, "IID('{AE729498-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 64 , )),
]

IVdText_vtables_dispatch_ = 1
IVdText_vtables_ = [
	(( 'TextString' , 'retval' , ), 1, (1, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'TextString' , 'retval' , ), 1, (1, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'retval' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Font' , 'retval' , ), 3, (3, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Font' , 'retval' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Origin' , 'retval' , ), 4, (4, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Origin' , 'retval' , ), 4, (4, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Orientation' , 'retval' , ), 5, (5, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Orientation' , 'retval' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Size' , 'retval' , ), 6, (6, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Size' , 'retval' , ), 6, (6, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'retval' , ), 7, (7, (), [ (16393, 10, None, "IID('{AE729484-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Application' , 'retval' , ), 8, (8, (), [ (16393, 10, None, "IID('{EA4ABD71-84B0-11CE-8237-00001B4D36B5}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Selected' , ), 14, (14, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'retval' , ), 15, (15, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 64 , )),
	(( 'Color' , 'retval' , ), 15, (15, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 64 , )),
	(( 'Printable' , 'retval' , ), 20, (20, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 64 , )),
	(( 'Printable' , 'retval' , ), 20, (20, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 64 , )),
	(( '_SetSelected' , 'Flag' , ), 9, (9, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 64 , )),
	(( 'GetLocation' , 'retval' , ), 10, (10, (), [ (16393, 10, None, "IID('{AE729498-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'SetLocation' , 'X' , 'Y' , ), 11, (11, (), [ (3, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( '_GetColor' , 'retval' , ), 12, (12, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 64 , )),
	(( '_SetColor' , 'newColor' , ), 13, (13, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 64 , )),
	(( 'SetObjectColor' , 'newColor' , ), 16, (16, (), [ (9, 1, None, "IID('{C1031A0C-15BD-4897-A3E5-4C615CDEA684}')") , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'GetObjectColor' , 'retval' , ), 17, (17, (), [ (16393, 10, None, "IID('{C1031A0C-15BD-4897-A3E5-4C615CDEA684}')") , ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'SetAutomaticColor' , 'bAutomatic' , ), 18, (18, (), [ (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'IsColorAutomatic' , 'retval' , ), 19, (19, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
]

IVdView_vtables_dispatch_ = 1
IVdView_vtables_ = [
	(( 'Viewport' , 'retval' , ), 25, (25, (), [ (16393, 10, None, "IID('{02768321-EB56-11D1-BE0C-00A0C9204FDC}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Block' , 'retval' , ), 26, (26, (), [ (16393, 10, None, "IID('{AE729484-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'TopBlock' , 'retval' , ), 27, (27, (), [ (16393, 10, None, "IID('{AE729484-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'SelectByName' , 'Name' , 'retval' , ), 1, (1, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Query' , 'Flags' , 'Selected' , 'retval' , ), 2, (2, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (16393, 10, None, "IID('{BD2EDF77-7E28-11CE-822D-00001B4D36B7}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'ZoomIn' , 'retval' , ), 3, (3, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'ZoomOut' , 'retval' , ), 4, (4, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'ZoomSelect' , 'retval' , ), 5, (5, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Refresh' , ), 6, (6, (), [ ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'ViewFull' , ), 7, (7, (), [ ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'ActiveBlock' , 'retval' , ), 8, (8, (), [ (16393, 10, None, "IID('{AE729484-9683-11CE-8246-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 64 , )),
	(( 'Application' , 'retval' , ), 9, (9, (), [ (16393, 10, None, "IID('{EA4ABD71-84B0-11CE-8237-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Document' , 'retval' , ), 10, (10, (), [ (16393, 10, None, "IID('{D8B95AF2-D943-4295-8D86-71B4F904C3AA}')") , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Activate' , ), 11, (11, (), [ ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'SelectObject' , 'ObjectType' , 'Expression' , 'SelectOwner' , 'RegExp' , 
			 'AddSelect' , 'retval' , ), 12, (12, (), [ (3, 1, None, None) , (8, 1, None, None) , 
			 (11, 1, None, None) , (11, 1, None, None) , (11, 1, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'BufferCopy' , ), 13, (13, (), [ ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'BufferCut' , ), 14, (14, (), [ ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'BufferPaste' , ), 15, (15, (), [ ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'ComputeMBB' , 'OLEItems' , 'Xmin' , 'Ymin' , 'Xmax' , 
			 'Ymax' , ), 16, (16, (), [ (11, 1, None, None) , (16387, 1, None, None) , (16387, 1, None, None) , 
			 (16387, 1, None, None) , (16387, 1, None, None) , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'SelectByName2' , 'lpszObjName' , 'bAddSelect' , 'retval' , ), 17, (17, (), [ 
			 (8, 1, None, None) , (11, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'GetSelectedNetName' , 'bRetFullPath' , 'bRetInternalName' , 'Index' , 'retval' , 
			 ), 18, (18, (), [ (11, 1, None, None) , (11, 1, None, None) , (3, 49, '1', None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'ModifyVisibility' , 'SelectString' , 'Visibility' , 'ApplyToSelected' , ), 19, (19, (), [ 
			 (8, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'AddAttributeMoveMode' , 'AttributeString' , 'Visibility' , ), 20, (20, (), [ (8, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'SelectText' , 'Pattern' , 'Type' , 'ApplyToSelected' , ), 21, (21, (), [ 
			 (8, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'BufferPasteXY' , 'PasteX' , 'PasteY' , 'retval' , ), 22, (22, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'GetJointLocs' , 'AllOrSelected' , 'JointType' , 'retval' , ), 23, (23, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'SelectSegmentByJointLoc' , 'XCoordinate' , 'YCoordinate' , 'JointType' , 'retval' , 
			 ), 24, (24, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'GetName' , 'Flag' , 'retval' , ), 28, (28, (), [ (3, 1, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'GetTopLevelDesignName' , 'retval' , ), 29, (29, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'SetCenter' , 'X' , 'Y' , ), 30, (30, (), [ (3, 1, None, None) , 
			 (3, 0, None, None) , ], 1 , 1 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'AddReuseBlock' , 'partName' , 'SymbolName' , 'retval' , ), 31, (31, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 296 , (3, 0, None, None) , 64 , )),
	(( 'AddMissingPorts' , ), 32, (32, (), [ ], 1 , 1 , 4 , 0 , 304 , (3, 0, None, None) , 64 , )),
	(( 'DumpImage' , 'FileName' , 'Width' , 'Height' , ), 33, (33, (), [ 
			 (8, 1, None, None) , (3, 49, '-1', None) , (3, 49, '-1', None) , ], 1 , 1 , 4 , 0 , 312 , (3, 0, None, None) , 64 , )),
	(( 'GetTopBlockName' , 'retval' , ), 34, (34, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 320 , (3, 0, None, None) , 64 , )),
]

IVdViews_vtables_dispatch_ = 1
IVdViews_vtables_ = [
	(( 'Count' , 'retval' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Application' , 'retval' , ), 2, (2, (), [ (16393, 10, None, "IID('{EA4ABD71-84B0-11CE-8237-00001B4D36B5}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'retval' , ), 3, (3, (), [ (16393, 10, None, "IID('{4ADEF4E2-690A-11CE-9261-0020C5E26659}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'Index' , 'retval' , ), 4, (4, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{0892A013-86BC-11CE-8238-00001B4D36B5}')") , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

IViewport_vtables_dispatch_ = 1
IViewport_vtables_ = [
	(( 'LineThickness' , 'retval' , ), 1, (1, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'LineThickness' , 'retval' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'FillStyle' , 'retval' , ), 2, (2, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'FillStyle' , 'retval' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'LinePattern' , 'retval' , ), 3, (3, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'LinePattern' , 'retval' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'retval' , ), 4, (4, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 64 , )),
	(( 'Color' , 'retval' , ), 4, (4, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 64 , )),
	(( 'RasterMode' , 'retval' , ), 5, (5, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'RasterMode' , 'retval' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'LineCap' , 'retval' , ), 6, (6, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'LineCap' , 'retval' , ), 6, (6, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'LineJoin' , 'retval' , ), 7, (7, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'LineJoin' , 'retval' , ), 7, (7, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'TextFont' , ), 8, (8, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'TextSize' , ), 9, (9, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'TextAngle' , ), 10, (10, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'PixelToUser' , 'XCoordinate' , 'YCoordinate' , ), 11, (11, (), [ (16396, 1, None, None) , 
			 (16396, 1, None, None) , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'UserToPixel' , 'XCoordinate' , 'YCoordinate' , ), 12, (12, (), [ (16396, 1, None, None) , 
			 (16396, 1, None, None) , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'PolyLine' , 'ArrayOfXValues' , 'ArrayOfYValues' , 'retval' , ), 13, (13, (), [ 
			 (12, 1, None, None) , (12, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'PixelRectangle' , 'Left' , 'Top' , 'Right' , 'Bottom' , 
			 ), 14, (14, (), [ (16396, 1, None, None) , (16396, 1, None, None) , (16396, 1, None, None) , (16396, 1, None, None) , ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'UserRectangle' , 'Left' , 'Top' , 'Right' , 'Bottom' , 
			 ), 15, (15, (), [ (16396, 1, None, None) , (16396, 1, None, None) , (16396, 1, None, None) , (16396, 1, None, None) , ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'EraseRectangle' , 'Left' , 'Top' , 'Right' , 'Bottom' , 
			 ), 16, (16, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Line' , 'X1' , 'Y1' , 'X2' , 'Y2' , 
			 ), 17, (17, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Arrow' , 'X1' , 'Y1' , 'X2' , 'Y2' , 
			 'Arrowhead' , ), 18, (18, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , 
			 (3, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Circle' , 'X' , 'Y' , 'Radius' , ), 19, (19, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Box' , 'Left' , 'Top' , 'Right' , 'Bottom' , 
			 ), 20, (20, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'Arc' , 'X1' , 'Y1' , 'X2' , 'Y2' , 
			 'X3' , 'Y3' , ), 21, (21, (), [ (3, 1, None, None) , (3, 1, None, None) , 
			 (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'Ellipse' , 'X' , 'Y' , 'XRadius' , 'YRadius' , 
			 ), 22, (22, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'Point' , 'X' , 'Y' , ), 23, (23, (), [ (3, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'Spline' , 'Type' , 'Order' , 'Granularity' , 'XArrayOfPoints' , 
			 'YArrayOfPoints' , 'Arrowhead' , 'ArrowWidth' , 'ArrowLength' , 'ArrowFill' , 
			 ), 24, (24, (), [ (3, 1, None, None) , (3, 1, None, None) , (2, 1, None, None) , (12, 1, None, None) , 
			 (12, 1, None, None) , (3, 1, None, None) , (2, 1, None, None) , (2, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'Text' , 'X' , 'Y' , 'String' , 'Flags' , 
			 ), 25, (25, (), [ (3, 1, None, None) , (3, 1, None, None) , (8, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'SetClipRectangle' , 'Left' , 'Top' , 'Right' , 'Bottom' , 
			 'retval' , ), 26, (26, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , 
			 (3, 1, None, None) , (16393, 10, None, "IID('{A4E20F1C-89F1-40CE-B92A-7373BCA0EEF5}')") , ], 1 , 1 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'SetObjectColor' , 'newColor' , ), 27, (27, (), [ (9, 1, None, "IID('{C1031A0C-15BD-4897-A3E5-4C615CDEA684}')") , ], 1 , 1 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'GetObjectColor' , 'retval' , ), 28, (28, (), [ (16393, 10, None, "IID('{C1031A0C-15BD-4897-A3E5-4C615CDEA684}')") , ], 1 , 1 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
]

RecordMap = {
}

CLSIDToClassMap = {
	'{BD2EDF77-7E28-11CE-822D-00001B4D36B7}' : IVdObjs,
	'{EA4ABD71-84B0-11CE-8237-00001B4D36B5}' : IVdApp,
	'{BD2EDF77-7E28-11CE-822D-00001B4D36B5}' : IVdDocs,
	'{4ADEF4E2-690A-11CE-9261-0020C5E26659}' : IVdDoc,
	'{DC3A8AF0-91B4-11CE-8243-00001B4D36B5}' : IVdViews,
	'{0892A013-86BC-11CE-8238-00001B4D36B5}' : IVdView,
	'{02768321-EB56-11D1-BE0C-00A0C9204FDC}' : IViewport,
	'{A4E20F1C-89F1-40CE-B92A-7373BCA0EEF5}' : IVdRect,
	'{C1031A0C-15BD-4897-A3E5-4C615CDEA684}' : IColor,
	'{AE729484-9683-11CE-8246-00001B4D36B5}' : IVdBlock,
	'{AE729498-9683-11CE-8246-00001B4D36B5}' : IVdPoint,
	'{AE729480-9683-11CE-8246-00001B4D36B5}' : IVdArc,
	'{AE729486-9683-11CE-8246-00001B4D36B5}' : IVdBox,
	'{AE729488-9683-11CE-8246-00001B4D36B5}' : IVdCircle,
	'{AE72948A-9683-11CE-8246-00001B4D36B5}' : IVdComp,
	'{AE72948E-9683-11CE-8246-00001B4D36B5}' : IVdLabel,
	'{AE729482-9683-11CE-8246-00001B4D36B5}' : IVdAttr,
	'{AE72948C-9683-11CE-8246-00001B4D36B5}' : IVdCmpPin,
	'{AE729496-9683-11CE-8246-00001B4D36B5}' : IVdPin,
	'{1446F3C0-2169-11D0-91A7-7A9695000000}' : IVdConnection,
	'{AE729492-9683-11CE-8246-00001B4D36B5}' : IVdNet,
	'{AE72949A-9683-11CE-8246-00001B4D36B5}' : IVdSegment,
	'{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}' : IStringList,
	'{FE3DB4AE-6C5C-426D-93A7-1308F624DDD9}' : IRipper,
	'{AE72949C-9683-11CE-8246-00001B4D36B5}' : IVdText,
	'{AE729490-9683-11CE-8246-00001B4D36B5}' : IVdLine,
	'{4584E756-C172-4389-AD41-AEE82CB45759}' : IMergeData,
	'{EB52D85C-D244-4993-9FF6-5B3167ACDE01}' : IVdFrameBoard,
	'{D8B95AF2-D943-4295-8D86-71B4F904C3AA}' : IVdSchematicSheetDocument,
	'{608CA7F4-A52A-4206-9580-3BEB17CE0073}' : IVdSchematicSheetDocuments,
	'{03BE5928-2002-4CCB-818D-775ED6115A41}' : IMGCDesignerDataManagementEntity,
	'{787D1D50-FC6C-478A-84CB-2FD200799E22}' : IMGCDesignerDataManagementAdditionalProperty,
	'{3C8285AF-A900-4537-B9BA-C44223D0B380}' : IMGCDesignerDataManagementEntities,
	'{7BB17D63-FAE6-11D1-BE10-00A0C9204FDC}' : IStringCollection,
	'{AC6510A1-83C5-4486-9154-CE74592F9A48}' : IHDLSourceDocuments,
	'{8C395488-EC22-4C81-8F13-7061A7594657}' : IHDLSourceDocument,
	'{7D50CA6D-07DB-4BE0-AD95-563DED3F9157}' : IHTMLSourceDocuments,
	'{956DD308-D5ED-40A1-83F2-84113B8937C1}' : IProjectData,
	'{8DE1FE34-146C-4C91-8B52-EE97F9292EEF}' : ISymbolPartitions,
	'{D17E5439-1B5A-40D5-A115-1E4656FB102B}' : IPDBPartitions,
	'{3D2B940D-C2B5-440E-AB57-E8C6F3FB34C9}' : IODProjectData,
	'{28D40DF1-22F3-11D0-91AB-58F3E7000000}' : IVdLibrary,
	'{AA7F70A6-2F0E-417C-A1D2-C1621D728EB0}' : ICommandsManager,
	'{E8758B51-DEBB-46FD-A192-962B14F57FA4}' : ICommonPropertyManager,
	'{2A69C05E-34EA-46FE-B44C-FE3A217D3C86}' : ICommonPropertyDefinition,
	'{77CD6602-703B-4AFA-A4C1-B1652A257F15}' : IFramework,
	'{2A3CCA57-9C38-4484-A6A3-7521DDF7DAD0}' : IICTDocuments,
	'{E947B7EF-5E39-42FD-A351-400BFEFCF49D}' : IVdICTDocument,
	'{EA874DB4-9B4D-4E7F-BE4F-D41AD4A560DE}' : IVdICTViews,
	'{848E324F-125D-4236-981D-0EB202E628DA}' : IVdICTView,
	'{C64B5D5C-66D5-41FE-B4B3-EFC664EAED1B}' : IVdICTBlock,
	'{F692CCBA-DA51-43FB-B8D6-79EEA84B59CA}' : IVdICTObj,
	'{4945AC27-6ADD-462C-B3F6-239842AFFEB9}' : IVdICTComp,
	'{9ED04F47-52F4-476A-8100-B8990AFE3ACD}' : IVdICTNet,
	'{8E0609DD-208C-42B6-A1B0-00DAA3E45423}' : IVdAppProtectionProxy,
	'{3EBAD6B7-B757-4A57-9657-DD43BF86A526}' : IDesignSearcherAutomation,
	'{96EB093C-B1E3-444B-B39D-08D05CB0DF06}' : IMGCDesignerDataManagement,
	'{4E66A337-C45F-4BEA-9089-3E64D3270531}' : IMGCDesignerDataManagementAdditionalProperties,
	'{9D83C992-3682-4D94-9727-EFBB5C0FB74C}' : IAddinInfo,
	'{230DA384-5030-11D3-8851-0060B0EF0A25}' : IPredicate,
	'{2645E45F-3981-4BA3-ADE4-EFB2AD5A1CCB}' : IVdICTPin,
	'{8B362142-6CF5-1014-9D62-FFC3EECCF0AC}' : Viewport,
	'{648981C1-A956-11D1-80F2-00A0C97221DB}' : IVdViewEvents,
	'{8B3622FE-6CF5-1014-9D62-FFC3EECCF0AC}' : View,
	'{8B3624C8-6CF5-1014-9D62-FFC3EECCF0AC}' : CViewDrawView,
	'{8B36267B-6CF5-1014-9D62-FFC3EECCF0AC}' : ICTView,
	'{8B362829-6CF5-1014-9D62-FFC3EECCF0AC}' : CColor,
	'{8B362A2D-6CF5-1014-9D62-FFC3EECCF0AC}' : _CColor,
	'{8B362BED-6CF5-1014-9D62-FFC3EECCF0AC}' : MergeData,
	'{8B362D9C-6CF5-1014-9D62-FFC3EECCF0AC}' : AddinInfo,
	'{8B362F49-6CF5-1014-9D62-FFC3EECCF0AC}' : StringList,
	'{8B3630F8-6CF5-1014-9D62-FFC3EECCF0AC}' : CStringList,
	'{8B3632A1-6CF5-1014-9D62-FFC3EECCF0AC}' : SymbolPartitions,
	'{8B363464-6CF5-1014-9D62-FFC3EECCF0AC}' : PDBPartitions,
	'{8B363620-6CF5-1014-9D62-FFC3EECCF0AC}' : ProjectData,
	'{8B3637D0-6CF5-1014-9D62-FFC3EECCF0AC}' : CProjectData,
	'{8B363980-6CF5-1014-9D62-FFC3EECCF0AC}' : ComFrameworAdapter,
	'{8B363BA5-6CF5-1014-9D62-FFC3EECCF0AC}' : CComFrameworkAdapter,
	'{8B363D89-6CF5-1014-9D62-FFC3EECCF0AC}' : CommonPropertyDefinition,
	'{8B363F3D-6CF5-1014-9D62-FFC3EECCF0AC}' : CCommPropDef,
	'{8B3640F0-6CF5-1014-9D62-FFC3EECCF0AC}' : CommonPropertyManager,
	'{8B36429D-6CF5-1014-9D62-FFC3EECCF0AC}' : CCommPropMgr,
	'{8B36444B-6CF5-1014-9D62-FFC3EECCF0AC}' : CommandsManager,
	'{8B364617-6CF5-1014-9D62-FFC3EECCF0AC}' : CCmdMgr,
	'{341E1868-20BA-4B3C-8778-EBEEE6021C42}' : IVdApplicationAtTest,
	'{8B3709E0-6CF5-1014-9D62-FFC3EECCF0AC}' : ApplicationAtTest,
	'{8B370C04-6CF5-1014-9D62-FFC3EECCF0AC}' : CVdApplicationAtTest,
	'{8B3647CF-6CF5-1014-9D62-FFC3EECCF0AC}' : ApplicationProtectionProxy,
	'{B8CC7991-E03E-11D1-BE05-00A0C9204FDC}' : IVdAppEvents,
	'{8B364984-6CF5-1014-9D62-FFC3EECCF0AC}' : Application,
	'{8B364B47-6CF5-1014-9D62-FFC3EECCF0AC}' : CVdApp,
	'{8B364CF9-6CF5-1014-9D62-FFC3EECCF0AC}' : Objects,
	'{8B364EBC-6CF5-1014-9D62-FFC3EECCF0AC}' : CVdObjs,
	'{8B3650E2-6CF5-1014-9D62-FFC3EECCF0AC}' : CVdICTObjs,
	'{8B3652FF-6CF5-1014-9D62-FFC3EECCF0AC}' : Point,
	'{8B365518-6CF5-1014-9D62-FFC3EECCF0AC}' : CVdPoint,
	'{8B36573C-6CF5-1014-9D62-FFC3EECCF0AC}' : Rect,
	'{8B36599B-6CF5-1014-9D62-FFC3EECCF0AC}' : CVdRect,
	'{8B365B5C-6CF5-1014-9D62-FFC3EECCF0AC}' : Arc,
	'{8B365D33-6CF5-1014-9D62-FFC3EECCF0AC}' : CVdArc,
	'{8B365EF0-6CF5-1014-9D62-FFC3EECCF0AC}' : SchematicSheetDocument,
	'{8B3660B9-6CF5-1014-9D62-FFC3EECCF0AC}' : CVdDoc,
	'{8B3662D5-6CF5-1014-9D62-FFC3EECCF0AC}' : ICTDocument,
	'{8B366486-6CF5-1014-9D62-FFC3EECCF0AC}' : SchematicSheetDocuments,
	'{8B36663A-6CF5-1014-9D62-FFC3EECCF0AC}' : CVdDocs,
	'{8B3667E8-6CF5-1014-9D62-FFC3EECCF0AC}' : ICTDocuments,
	'{8B3669A8-6CF5-1014-9D62-FFC3EECCF0AC}' : CICTDocs,
	'{8B366B73-6CF5-1014-9D62-FFC3EECCF0AC}' : Views,
	'{8B366D22-6CF5-1014-9D62-FFC3EECCF0AC}' : CVdViews,
	'{8B366ED1-6CF5-1014-9D62-FFC3EECCF0AC}' : CVdICTViews,
	'{8B367087-6CF5-1014-9D62-FFC3EECCF0AC}' : Attribute,
	'{8B36723A-6CF5-1014-9D62-FFC3EECCF0AC}' : CVdAttr,
	'{B3EC8244-3A42-4E18-9667-2A54BC66EABF}' : IVdHighPrecisionObject,
	'{8B370649-6CF5-1014-9D62-FFC3EECCF0AC}' : HighPrecisionObject,
	'{8B37081F-6CF5-1014-9D62-FFC3EECCF0AC}' : CVdHighPrecisionObject,
	'{8B367462-6CF5-1014-9D62-FFC3EECCF0AC}' : Block,
	'{8B367622-6CF5-1014-9D62-FFC3EECCF0AC}' : CVdBlock,
	'{F7EC3A7D-851C-4C1D-ABAF-FBDB3C38D29B}' : IVdICTAttr,
	'{8B367A2D-6CF5-1014-9D62-FFC3EECCF0AC}' : ICTAttribute,
	'{8B367F7F-6CF5-1014-9D62-FFC3EECCF0AC}' : CVdICTAttr,
	'{8B368AA4-6CF5-1014-9D62-FFC3EECCF0AC}' : ICTObject,
	'{8B3681F1-6CF5-1014-9D62-FFC3EECCF0AC}' : ICTBlock,
	'{8B36843C-6CF5-1014-9D62-FFC3EECCF0AC}' : ICTComp,
	'{8B368664-6CF5-1014-9D62-FFC3EECCF0AC}' : ICTNet,
	'{8B368887-6CF5-1014-9D62-FFC3EECCF0AC}' : ICTPin,
	'{8B368CC3-6CF5-1014-9D62-FFC3EECCF0AC}' : Box,
	'{8B368EF8-6CF5-1014-9D62-FFC3EECCF0AC}' : CVdBox,
	'{8B369114-6CF5-1014-9D62-FFC3EECCF0AC}' : Circle,
	'{8B36932D-6CF5-1014-9D62-FFC3EECCF0AC}' : CVdCircle,
	'{8B36954D-6CF5-1014-9D62-FFC3EECCF0AC}' : Component,
	'{8B36976A-6CF5-1014-9D62-FFC3EECCF0AC}' : CVdComp,
	'{8B3699A8-6CF5-1014-9D62-FFC3EECCF0AC}' : ComponentPin,
	'{8B369E7F-6CF5-1014-9D62-FFC3EECCF0AC}' : CVdCmpPin,
	'{8B36A05C-6CF5-1014-9D62-FFC3EECCF0AC}' : Label,
	'{8B36A221-6CF5-1014-9D62-FFC3EECCF0AC}' : CVdLabel,
	'{8B36A402-6CF5-1014-9D62-FFC3EECCF0AC}' : Line,
	'{8B36A61A-6CF5-1014-9D62-FFC3EECCF0AC}' : CVdLine,
	'{8B36A7CA-6CF5-1014-9D62-FFC3EECCF0AC}' : Net,
	'{8B36A986-6CF5-1014-9D62-FFC3EECCF0AC}' : CVdNet,
	'{8B36AB36-6CF5-1014-9D62-FFC3EECCF0AC}' : Ripper,
	'{8B36ACFF-6CF5-1014-9D62-FFC3EECCF0AC}' : CRipper,
	'{8B36AEBD-6CF5-1014-9D62-FFC3EECCF0AC}' : Pin,
	'{8B36B079-6CF5-1014-9D62-FFC3EECCF0AC}' : CVdPin,
	'{8B36B22E-6CF5-1014-9D62-FFC3EECCF0AC}' : Segment,
	'{8B36B3E7-6CF5-1014-9D62-FFC3EECCF0AC}' : CVdSegment,
	'{8B36B5B3-6CF5-1014-9D62-FFC3EECCF0AC}' : Text,
	'{8B36B75E-6CF5-1014-9D62-FFC3EECCF0AC}' : CVdText,
	'{8B36B90B-6CF5-1014-9D62-FFC3EECCF0AC}' : Connection,
	'{8B36BB3F-6CF5-1014-9D62-FFC3EECCF0AC}' : CVdConnection,
	'{8B36BCF2-6CF5-1014-9D62-FFC3EECCF0AC}' : Library,
	'{8B36BEBC-6CF5-1014-9D62-FFC3EECCF0AC}' : CVdLibrary,
	'{8B36C077-6CF5-1014-9D62-FFC3EECCF0AC}' : StringCollection,
	'{7BB17D66-FAE6-11D1-BE10-00A0C9204FDC}' : IAutoString,
	'{8B36C22C-6CF5-1014-9D62-FFC3EECCF0AC}' : AutoString,
	'{8B36C3DE-6CF5-1014-9D62-FFC3EECCF0AC}' : HDLSourceDocument,
	'{8B36C5D2-6CF5-1014-9D62-FFC3EECCF0AC}' : HDLSourceDocuments,
	'{B635CF94-49E3-454C-B5C3-1ECD6AE4AA50}' : IProjectManagerEventSink,
	'{8B36C7B3-6CF5-1014-9D62-FFC3EECCF0AC}' : ProjectManagerEventSink,
	'{AA54312B-698C-473D-ABDE-F4A4C9DCD0DD}' : IHTMLSourceDocument,
	'{8B36C967-6CF5-1014-9D62-FFC3EECCF0AC}' : HTMLSourceDocument,
	'{8B36CB16-6CF5-1014-9D62-FFC3EECCF0AC}' : HTMLSourceDocuments,
	'{8B36CCC6-6CF5-1014-9D62-FFC3EECCF0AC}' : FrameBoard,
	'{8B36CE74-6CF5-1014-9D62-FFC3EECCF0AC}' : CVdFrameBoard,
	'{8B3726C8-6CF5-1014-9D62-FFC3EECCF0AC}' : DesignerDataManagement,
	'{8B372899-6CF5-1014-9D62-FFC3EECCF0AC}' : DesignerDataManagementEntity,
	'{8B372A86-6CF5-1014-9D62-FFC3EECCF0AC}' : DesignerDataManagementEntities,
	'{8B372C67-6CF5-1014-9D62-FFC3EECCF0AC}' : DesignerDataManagementAdditionalProperty,
	'{8B372E3C-6CF5-1014-9D62-FFC3EECCF0AC}' : DesignerDataManagementAdditionalProperties,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
	'{BD2EDF77-7E28-11CE-822D-00001B4D36B7}' : 'IVdObjs',
	'{EA4ABD71-84B0-11CE-8237-00001B4D36B5}' : 'IVdApp',
	'{BD2EDF77-7E28-11CE-822D-00001B4D36B5}' : 'IVdDocs',
	'{4ADEF4E2-690A-11CE-9261-0020C5E26659}' : 'IVdDoc',
	'{DC3A8AF0-91B4-11CE-8243-00001B4D36B5}' : 'IVdViews',
	'{0892A013-86BC-11CE-8238-00001B4D36B5}' : 'IVdView',
	'{02768321-EB56-11D1-BE0C-00A0C9204FDC}' : 'IViewport',
	'{A4E20F1C-89F1-40CE-B92A-7373BCA0EEF5}' : 'IVdRect',
	'{C1031A0C-15BD-4897-A3E5-4C615CDEA684}' : 'IColor',
	'{AE729484-9683-11CE-8246-00001B4D36B5}' : 'IVdBlock',
	'{AE729498-9683-11CE-8246-00001B4D36B5}' : 'IVdPoint',
	'{AE729480-9683-11CE-8246-00001B4D36B5}' : 'IVdArc',
	'{AE729486-9683-11CE-8246-00001B4D36B5}' : 'IVdBox',
	'{AE729488-9683-11CE-8246-00001B4D36B5}' : 'IVdCircle',
	'{AE72948A-9683-11CE-8246-00001B4D36B5}' : 'IVdComp',
	'{AE72948E-9683-11CE-8246-00001B4D36B5}' : 'IVdLabel',
	'{AE729482-9683-11CE-8246-00001B4D36B5}' : 'IVdAttr',
	'{AE72948C-9683-11CE-8246-00001B4D36B5}' : 'IVdCmpPin',
	'{AE729496-9683-11CE-8246-00001B4D36B5}' : 'IVdPin',
	'{1446F3C0-2169-11D0-91A7-7A9695000000}' : 'IVdConnection',
	'{AE729492-9683-11CE-8246-00001B4D36B5}' : 'IVdNet',
	'{AE72949A-9683-11CE-8246-00001B4D36B5}' : 'IVdSegment',
	'{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}' : 'IStringList',
	'{FE3DB4AE-6C5C-426D-93A7-1308F624DDD9}' : 'IRipper',
	'{AE72949C-9683-11CE-8246-00001B4D36B5}' : 'IVdText',
	'{AE729490-9683-11CE-8246-00001B4D36B5}' : 'IVdLine',
	'{4584E756-C172-4389-AD41-AEE82CB45759}' : 'IMergeData',
	'{EB52D85C-D244-4993-9FF6-5B3167ACDE01}' : 'IVdFrameBoard',
	'{D8B95AF2-D943-4295-8D86-71B4F904C3AA}' : 'IVdSchematicSheetDocument',
	'{608CA7F4-A52A-4206-9580-3BEB17CE0073}' : 'IVdSchematicSheetDocuments',
	'{03BE5928-2002-4CCB-818D-775ED6115A41}' : 'IMGCDesignerDataManagementEntity',
	'{787D1D50-FC6C-478A-84CB-2FD200799E22}' : 'IMGCDesignerDataManagementAdditionalProperty',
	'{3C8285AF-A900-4537-B9BA-C44223D0B380}' : 'IMGCDesignerDataManagementEntities',
	'{7BB17D63-FAE6-11D1-BE10-00A0C9204FDC}' : 'IStringCollection',
	'{956DD308-D5ED-40A1-83F2-84113B8937C1}' : 'IProjectData',
	'{8DE1FE34-146C-4C91-8B52-EE97F9292EEF}' : 'ISymbolPartitions',
	'{D17E5439-1B5A-40D5-A115-1E4656FB102B}' : 'IPDBPartitions',
	'{3D2B940D-C2B5-440E-AB57-E8C6F3FB34C9}' : 'IODProjectData',
	'{28D40DF1-22F3-11D0-91AB-58F3E7000000}' : 'IVdLibrary',
	'{AA7F70A6-2F0E-417C-A1D2-C1621D728EB0}' : 'ICommandsManager',
	'{E8758B51-DEBB-46FD-A192-962B14F57FA4}' : 'ICommonPropertyManager',
	'{2A69C05E-34EA-46FE-B44C-FE3A217D3C86}' : 'ICommonPropertyDefinition',
	'{77CD6602-703B-4AFA-A4C1-B1652A257F15}' : 'IFramework',
	'{2A3CCA57-9C38-4484-A6A3-7521DDF7DAD0}' : 'IICTDocuments',
	'{E947B7EF-5E39-42FD-A351-400BFEFCF49D}' : 'IVdICTDocument',
	'{EA874DB4-9B4D-4E7F-BE4F-D41AD4A560DE}' : 'IVdICTViews',
	'{848E324F-125D-4236-981D-0EB202E628DA}' : 'IVdICTView',
	'{C64B5D5C-66D5-41FE-B4B3-EFC664EAED1B}' : 'IVdICTBlock',
	'{F692CCBA-DA51-43FB-B8D6-79EEA84B59CA}' : 'IVdICTObj',
	'{4945AC27-6ADD-462C-B3F6-239842AFFEB9}' : 'IVdICTComp',
	'{9ED04F47-52F4-476A-8100-B8990AFE3ACD}' : 'IVdICTNet',
	'{8E0609DD-208C-42B6-A1B0-00DAA3E45423}' : 'IVdAppProtectionProxy',
	'{3EBAD6B7-B757-4A57-9657-DD43BF86A526}' : 'IDesignSearcherAutomation',
	'{96EB093C-B1E3-444B-B39D-08D05CB0DF06}' : 'IMGCDesignerDataManagement',
	'{4E66A337-C45F-4BEA-9089-3E64D3270531}' : 'IMGCDesignerDataManagementAdditionalProperties',
	'{9D83C992-3682-4D94-9727-EFBB5C0FB74C}' : 'IAddinInfo',
	'{230DA384-5030-11D3-8851-0060B0EF0A25}' : 'IPredicate',
	'{2645E45F-3981-4BA3-ADE4-EFB2AD5A1CCB}' : 'IVdICTPin',
	'{341E1868-20BA-4B3C-8778-EBEEE6021C42}' : 'IVdApplicationAtTest',
	'{B3EC8244-3A42-4E18-9667-2A54BC66EABF}' : 'IVdHighPrecisionObject',
	'{F7EC3A7D-851C-4C1D-ABAF-FBDB3C38D29B}' : 'IVdICTAttr',
	'{7BB17D66-FAE6-11D1-BE10-00A0C9204FDC}' : 'IAutoString',
}


NamesToIIDMap = {
	'IVdObjs' : '{BD2EDF77-7E28-11CE-822D-00001B4D36B7}',
	'IVdApp' : '{EA4ABD71-84B0-11CE-8237-00001B4D36B5}',
	'IVdDocs' : '{BD2EDF77-7E28-11CE-822D-00001B4D36B5}',
	'IVdDoc' : '{4ADEF4E2-690A-11CE-9261-0020C5E26659}',
	'IVdViews' : '{DC3A8AF0-91B4-11CE-8243-00001B4D36B5}',
	'IVdView' : '{0892A013-86BC-11CE-8238-00001B4D36B5}',
	'IViewport' : '{02768321-EB56-11D1-BE0C-00A0C9204FDC}',
	'IVdRect' : '{A4E20F1C-89F1-40CE-B92A-7373BCA0EEF5}',
	'IColor' : '{C1031A0C-15BD-4897-A3E5-4C615CDEA684}',
	'IVdBlock' : '{AE729484-9683-11CE-8246-00001B4D36B5}',
	'IVdPoint' : '{AE729498-9683-11CE-8246-00001B4D36B5}',
	'IVdArc' : '{AE729480-9683-11CE-8246-00001B4D36B5}',
	'IVdBox' : '{AE729486-9683-11CE-8246-00001B4D36B5}',
	'IVdCircle' : '{AE729488-9683-11CE-8246-00001B4D36B5}',
	'IVdComp' : '{AE72948A-9683-11CE-8246-00001B4D36B5}',
	'IVdLabel' : '{AE72948E-9683-11CE-8246-00001B4D36B5}',
	'IVdAttr' : '{AE729482-9683-11CE-8246-00001B4D36B5}',
	'IVdCmpPin' : '{AE72948C-9683-11CE-8246-00001B4D36B5}',
	'IVdPin' : '{AE729496-9683-11CE-8246-00001B4D36B5}',
	'IVdConnection' : '{1446F3C0-2169-11D0-91A7-7A9695000000}',
	'IVdNet' : '{AE729492-9683-11CE-8246-00001B4D36B5}',
	'IVdSegment' : '{AE72949A-9683-11CE-8246-00001B4D36B5}',
	'IStringList' : '{3566B3FB-97C7-4F45-B1A6-E5469271F9AC}',
	'IRipper' : '{FE3DB4AE-6C5C-426D-93A7-1308F624DDD9}',
	'IVdText' : '{AE72949C-9683-11CE-8246-00001B4D36B5}',
	'IVdLine' : '{AE729490-9683-11CE-8246-00001B4D36B5}',
	'IMergeData' : '{4584E756-C172-4389-AD41-AEE82CB45759}',
	'IVdFrameBoard' : '{EB52D85C-D244-4993-9FF6-5B3167ACDE01}',
	'IVdSchematicSheetDocument' : '{D8B95AF2-D943-4295-8D86-71B4F904C3AA}',
	'IVdSchematicSheetDocuments' : '{608CA7F4-A52A-4206-9580-3BEB17CE0073}',
	'IMGCDesignerDataManagementEntity' : '{03BE5928-2002-4CCB-818D-775ED6115A41}',
	'IMGCDesignerDataManagementAdditionalProperty' : '{787D1D50-FC6C-478A-84CB-2FD200799E22}',
	'IMGCDesignerDataManagementEntities' : '{3C8285AF-A900-4537-B9BA-C44223D0B380}',
	'IStringCollection' : '{7BB17D63-FAE6-11D1-BE10-00A0C9204FDC}',
	'IHDLSourceDocuments' : '{AC6510A1-83C5-4486-9154-CE74592F9A48}',
	'IHDLSourceDocument' : '{8C395488-EC22-4C81-8F13-7061A7594657}',
	'IHTMLSourceDocuments' : '{7D50CA6D-07DB-4BE0-AD95-563DED3F9157}',
	'IProjectData' : '{956DD308-D5ED-40A1-83F2-84113B8937C1}',
	'ISymbolPartitions' : '{8DE1FE34-146C-4C91-8B52-EE97F9292EEF}',
	'IPDBPartitions' : '{D17E5439-1B5A-40D5-A115-1E4656FB102B}',
	'IODProjectData' : '{3D2B940D-C2B5-440E-AB57-E8C6F3FB34C9}',
	'IVdLibrary' : '{28D40DF1-22F3-11D0-91AB-58F3E7000000}',
	'ICommandsManager' : '{AA7F70A6-2F0E-417C-A1D2-C1621D728EB0}',
	'ICommonPropertyManager' : '{E8758B51-DEBB-46FD-A192-962B14F57FA4}',
	'ICommonPropertyDefinition' : '{2A69C05E-34EA-46FE-B44C-FE3A217D3C86}',
	'IFramework' : '{77CD6602-703B-4AFA-A4C1-B1652A257F15}',
	'IICTDocuments' : '{2A3CCA57-9C38-4484-A6A3-7521DDF7DAD0}',
	'IVdICTDocument' : '{E947B7EF-5E39-42FD-A351-400BFEFCF49D}',
	'IVdICTViews' : '{EA874DB4-9B4D-4E7F-BE4F-D41AD4A560DE}',
	'IVdICTView' : '{848E324F-125D-4236-981D-0EB202E628DA}',
	'IVdICTBlock' : '{C64B5D5C-66D5-41FE-B4B3-EFC664EAED1B}',
	'IVdICTObj' : '{F692CCBA-DA51-43FB-B8D6-79EEA84B59CA}',
	'IVdICTComp' : '{4945AC27-6ADD-462C-B3F6-239842AFFEB9}',
	'IVdICTNet' : '{9ED04F47-52F4-476A-8100-B8990AFE3ACD}',
	'IVdAppProtectionProxy' : '{8E0609DD-208C-42B6-A1B0-00DAA3E45423}',
	'IDesignSearcherAutomation' : '{3EBAD6B7-B757-4A57-9657-DD43BF86A526}',
	'IMGCDesignerDataManagement' : '{96EB093C-B1E3-444B-B39D-08D05CB0DF06}',
	'IMGCDesignerDataManagementAdditionalProperties' : '{4E66A337-C45F-4BEA-9089-3E64D3270531}',
	'IAddinInfo' : '{9D83C992-3682-4D94-9727-EFBB5C0FB74C}',
	'IPredicate' : '{230DA384-5030-11D3-8851-0060B0EF0A25}',
	'IVdICTPin' : '{2645E45F-3981-4BA3-ADE4-EFB2AD5A1CCB}',
	'IVdViewEvents' : '{648981C1-A956-11D1-80F2-00A0C97221DB}',
	'IVdApplicationAtTest' : '{341E1868-20BA-4B3C-8778-EBEEE6021C42}',
	'IVdAppEvents' : '{B8CC7991-E03E-11D1-BE05-00A0C9204FDC}',
	'IVdHighPrecisionObject' : '{B3EC8244-3A42-4E18-9667-2A54BC66EABF}',
	'IVdICTAttr' : '{F7EC3A7D-851C-4C1D-ABAF-FBDB3C38D29B}',
	'IAutoString' : '{7BB17D66-FAE6-11D1-BE10-00A0C9204FDC}',
	'IProjectManagerEventSink' : '{B635CF94-49E3-454C-B5C3-1ECD6AE4AA50}',
	'IHTMLSourceDocument' : '{AA54312B-698C-473D-ABDE-F4A4C9DCD0DD}',
}

win32com.client.constants.__dicts__.append(constants.__dict__)

