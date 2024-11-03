# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.9.10 (tags/v3.9.10:f2f3f53, Jan 17 2022, 15:14:21) [MSC v.1929 64 bit (AMD64)]
# From type library 'ConstraintsAuto70.dll'
# On Sun Nov  3 23:01:02 2024
'Constraints Automation Type Library.'
makepy_version = '0.5.01'
python_version = 0x3090af0

import win32com.client.CLSIDToClass, pythoncom, pywintypes
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch

# The following 3 lines may need tweaking for the particular server
# Candidates are pythoncom.Missing, .Empty and .ArgNotFound
defaultNamedOptArg=pythoncom.Empty
defaultNamedNotOptArg=pythoncom.Empty
defaultUnnamedArg=pythoncom.Empty

CLSID = IID('{8B0AE4B7-6CF5-1014-9B55-8BB0EECCF0AC}')
MajorVersion = 119
MinorVersion = 0
LibraryFlags = 8
LCID = 0x0

class constants:
	CCM_AllClassClearances        =3          # from enum EClassClearanceMask
	CCM_Standard                  =1          # from enum EClassClearanceMask
	CCM_ZAxis                     =2          # from enum EClassClearanceMask
	CCT_Standard                  =0          # from enum EClassClearanceType
	CCT_ZAxis                     =1          # from enum EClassClearanceType
	CLM_3D                        =2          # from enum EClearanceMask
	CLM_AllClearances             =3          # from enum EClearanceMask
	CLM_Standard                  =1          # from enum EClearanceMask
	CRT_Standard                  =0          # from enum EClearanceRuleType
	CRT_ZAxis                     =1          # from enum EClearanceRuleType
	CLT_3D                        =1          # from enum EClearanceType
	CLT_Standard                  =0          # from enum EClearanceType
	CF_Hex                        =1          # from enum EColorFormat
	CF_Int                        =0          # from enum EColorFormat
	CF_Name                       =3          # from enum EColorFormat
	CF_RGB                        =2          # from enum EColorFormat
	CM_AllConstraints             =7          # from enum EConstraintMask
	CM_DefaultConstraints         =1          # from enum EConstraintMask
	CM_NonDefaultConstraints      =2          # from enum EConstraintMask
	CT_Aggressor                  =344        # from enum EConstraintType
	CT_AttachedDielectric         =58         # from enum EConstraintType
	CT_AutoCalculateEr            =160        # from enum EConstraintType
	CT_Backdrill                  =60         # from enum EConstraintType
	CT_BondFingerToBondFinger     =66         # from enum EConstraintType
	CT_BondFingerToPad            =67         # from enum EConstraintType
	CT_BondFingerToPlane          =68         # from enum EConstraintType
	CT_BondFingerToSMDPad         =69         # from enum EConstraintType
	CT_BondFingerToTrace          =70         # from enum EConstraintType
	CT_BondFingerToVia            =71         # from enum EConstraintType
	CT_BulkResistance             =73         # from enum EConstraintType
	CT_Clearance                  =347        # from enum EConstraintType
	CT_ClearanceMinimumXY         =486        # from enum EConstraintType
	CT_ClearanceMinimumZ          =487        # from enum EConstraintType
	CT_ClearanceOptimalXY         =488        # from enum EConstraintType
	CT_ClearanceOptimalZ          =489        # from enum EConstraintType
	CT_Color                      =215        # from enum EConstraintType
	CT_ConvergenceToleranceMax    =147        # from enum EConstraintType
	CT_CrosstalkLevel             =133        # from enum EConstraintType
	CT_CrosstalkMax               =340        # from enum EConstraintType
	CT_DelayMax                   =257        # from enum EConstraintType
	CT_DelayMin                   =277        # from enum EConstraintType
	CT_DelayType                  =140        # from enum EConstraintType
	CT_Description                =216        # from enum EConstraintType
	CT_DifferentialImpedanceTarget=148        # from enum EConstraintType
	CT_DifferentialImpedanceTolerance=151        # from enum EConstraintType
	CT_DifferentialPairPhaseToleranceDistanceMax=154        # from enum EConstraintType
	CT_DifferentialPairPhaseToleranceMax=155        # from enum EConstraintType
	CT_DifferentialPairToleranceMax=157        # from enum EConstraintType
	CT_DifferentialSpacing        =144        # from enum EConstraintType
	CT_DifferentialTypicalImpedance=143        # from enum EConstraintType
	CT_DifferentialViaSpacing     =424        # from enum EConstraintType
	CT_Direction                  =293        # from enum EConstraintType
	CT_DisplayPattern             =479        # from enum EConstraintType
	CT_DistanceToConvergenceMax   =152        # from enum EConstraintType
	CT_EPMaskToPad                =247        # from enum EConstraintType
	CT_EPMaskToResistor           =248        # from enum EConstraintType
	CT_EPMaskToTrace              =249        # from enum EConstraintType
	CT_EPMaskToVia                =250        # from enum EConstraintType
	CT_EdgeToEdgeClearance        =179        # from enum EConstraintType
	CT_EmbeddedResistorToPad      =354        # from enum EConstraintType
	CT_EmbeddedResistorToResistor =355        # from enum EConstraintType
	CT_EmbeddedResistorToTrace    =356        # from enum EConstraintType
	CT_EmbeddedResistorToVia      =357        # from enum EConstraintType
	CT_Er                         =142        # from enum EConstraintType
	CT_EtchFactor                 =219        # from enum EConstraintType
	CT_ExternalNetDelay           =497        # from enum EConstraintType
	CT_ExternalNetLength          =496        # from enum EConstraintType
	CT_Formula                    =126        # from enum EConstraintType
	CT_Gap                        =190        # from enum EConstraintType
	CT_HierarchicalPath           =307        # from enum EConstraintType
	CT_IBISModel                  =303        # from enum EConstraintType
	CT_IBISModelDefault           =137        # from enum EConstraintType
	CT_IBISPinType                =202        # from enum EConstraintType
	CT_IOStandard                 =213        # from enum EConstraintType
	CT_LayerIndex                 =220        # from enum EConstraintType
	CT_LayerType                  =230        # from enum EConstraintType
	CT_LayerUsage                 =231        # from enum EConstraintType
	CT_LossTangent                =233        # from enum EConstraintType
	CT_MatchGroup                 =252        # from enum EConstraintType
	CT_MatchGroupTolerance        =253        # from enum EConstraintType
	CT_MaxCurrentDensity          =256        # from enum EConstraintType
	CT_MaxLayerDepth              =108        # from enum EConstraintType
	CT_MaxParallelLength          =271        # from enum EConstraintType
	CT_MaxViaCurrent              =275        # from enum EConstraintType
	CT_MaxVoltageDrop             =276        # from enum EConstraintType
	CT_MeasurementFrequency       =181        # from enum EConstraintType
	CT_Metal                      =127        # from enum EConstraintType
	CT_NarrowSide                 =222        # from enum EConstraintType
	CT_NetClass                   =316        # from enum EConstraintType
	CT_NoiseRuleType              =345        # from enum EConstraintType
	CT_ObjectName                 =32767      # from enum EConstraintType
	CT_PCBTechnology              =478        # from enum EConstraintType
	CT_PadToPad                   =300        # from enum EConstraintType
	CT_PadToPlane                 =301        # from enum EConstraintType
	CT_PadToVia                   =302        # from enum EConstraintType
	CT_ParallelismRule            =343        # from enum EConstraintType
	CT_PartNumber                 =141        # from enum EConstraintType
	CT_PartType                   =306        # from enum EConstraintType
	CT_PatternIndex               =481        # from enum EConstraintType
	CT_PatternOutline             =483        # from enum EConstraintType
	CT_PatternTransparency        =484        # from enum EConstraintType
	CT_PatternTransparent         =482        # from enum EConstraintType
	CT_PinCount                   =318        # from enum EConstraintType
	CT_PinPackageDelay            =319        # from enum EConstraintType
	CT_PinPackageLength           =320        # from enum EConstraintType
	CT_PlaneToPlane               =323        # from enum EConstraintType
	CT_PlaneToSMDPad              =505        # from enum EConstraintType
	CT_PourDrawStyle              =333        # from enum EConstraintType
	CT_PowerNet                   =336        # from enum EConstraintType
	CT_Process                    =224        # from enum EConstraintType
	CT_Quantity                   =350        # from enum EConstraintType
	CT_RestrictedLayerLengthExternalMax=185        # from enum EConstraintType
	CT_RestrictedLayerLengthInternalMax=208        # from enum EConstraintType
	CT_Roughness                  =175        # from enum EConstraintType
	CT_RoughnessModel             =472        # from enum EConstraintType
	CT_RoughnessModelFactor       =473        # from enum EConstraintType
	CT_RoughnessParameter         =176        # from enum EConstraintType
	CT_Route                      =363        # from enum EConstraintType
	CT_SchematicPinType           =317        # from enum EConstraintType
	CT_SeparationDistanceMax      =153        # from enum EConstraintType
	CT_Series                     =368        # from enum EConstraintType
	CT_Side                       =295        # from enum EConstraintType
	CT_SingleEndedCharacteristicImpedanceTolerance=207        # from enum EConstraintType
	CT_SingleEndedCharacteristicImpedanceValue=204        # from enum EConstraintType
	CT_StubLengthMax              =396        # from enum EConstraintType
	CT_SupplyVoltage              =397        # from enum EConstraintType
	CT_TargetZ0                   =398        # from enum EConstraintType
	CT_Technology                 =305        # from enum EConstraintType
	CT_TechnologyDefault          =138        # from enum EConstraintType
	CT_TemperatureCoefficient     =401        # from enum EConstraintType
	CT_TestPointsRequired         =474        # from enum EConstraintType
	CT_TestWidth                  =436        # from enum EConstraintType
	CT_ThermalCasingTemperatureLimit=195        # from enum EConstraintType
	CT_ThermalConductivity        =402        # from enum EConstraintType
	CT_ThermalJunctionTemperatureLimit=198        # from enum EConstraintType
	CT_ThermalPowerDissipation    =199        # from enum EConstraintType
	CT_ThermalPowerScalingFactor  =200        # from enum EConstraintType
	CT_ThermalThetaJC             =201        # from enum EConstraintType
	CT_Thickness                  =192        # from enum EConstraintType
	CT_TopologyOrdered            =411        # from enum EConstraintType
	CT_TopologyPinType            =57         # from enum EConstraintType
	CT_TopologyType               =290        # from enum EConstraintType
	CT_TraceToPad                 =432        # from enum EConstraintType
	CT_TraceToPlane               =433        # from enum EConstraintType
	CT_TraceToSMDPad              =390        # from enum EConstraintType
	CT_TraceToTrace               =434        # from enum EConstraintType
	CT_TraceToVia                 =435        # from enum EConstraintType
	CT_TraceWidthExpansion        =183        # from enum EConstraintType
	CT_TraceWidthMinimum          =283        # from enum EConstraintType
	CT_TraceWidthTypical          =439        # from enum EConstraintType
	CT_TrapezoidalTraceShapes     =177        # from enum EConstraintType
	CT_TreatedSide                =229        # from enum EConstraintType
	CT_TypicalImpedance           =438        # from enum EConstraintType
	CT_Value                      =456        # from enum EConstraintType
	CT_ValueDefault               =139        # from enum EConstraintType
	CT_ViaToPlane                 =459        # from enum EConstraintType
	CT_ViaToSMDPad                =391        # from enum EConstraintType
	CT_ViaToVia                   =460        # from enum EConstraintType
	CT_ViasMax                    =274        # from enum EConstraintType
	CT_Victim                     =341        # from enum EConstraintType
	CT_Width                      =466        # from enum EConstraintType
	DRCS_Error                    =2          # from enum EDRCStatus
	DRCS_Success                  =0          # from enum EDRCStatus
	DRCS_Warning                  =1          # from enum EDRCStatus
	DT_Length                     =0          # from enum EDelayType
	DT_TOF                        =1          # from enum EDelayType
	DC_Layout                     =2          # from enum EDesignContext
	DC_Schematic                  =1          # from enum EDesignContext
	DC_Unknown                    =0          # from enum EDesignContext
	EC_ErrorClassClearanceAdd     =-2147220889 # from enum EErrorCode
	EC_ErrorClassClearanceClearanceRuleSet=-2147220887 # from enum EErrorCode
	EC_ErrorClassClearanceDelete  =-2147220888 # from enum EErrorCode
	EC_ErrorClassClearanceTypeNotSupported=-2147220886 # from enum EErrorCode
	EC_ErrorClearanceRuleAdd      =-2147220892 # from enum EErrorCode
	EC_ErrorClearanceRuleDelete   =-2147220890 # from enum EErrorCode
	EC_ErrorClearanceRuleRename   =-2147220891 # from enum EErrorCode
	EC_ErrorClearanceTypeNotSupported=-2147220868 # from enum EErrorCode
	EC_ErrorCommentDelete         =-2147220874 # from enum EErrorCode
	EC_ErrorCommentReadValue      =-2147220875 # from enum EErrorCode
	EC_ErrorCommentSetValue       =-2147220876 # from enum EErrorCode
	EC_ErrorConstantAdd           =-2147220902 # from enum EErrorCode
	EC_ErrorConstantDelete        =-2147220901 # from enum EErrorCode
	EC_ErrorConstantRename        =-2147220900 # from enum EErrorCode
	EC_ErrorConstantSetValue      =-2147220899 # from enum EErrorCode
	EC_ErrorConstraintClassAdd    =-2147220960 # from enum EErrorCode
	EC_ErrorConstraintClassAssignNet=-2147220956 # from enum EErrorCode
	EC_ErrorConstraintClassDelete =-2147220958 # from enum EErrorCode
	EC_ErrorConstraintClassInsert =-2147220878 # from enum EErrorCode
	EC_ErrorConstraintClassMove   =-2147220957 # from enum EErrorCode
	EC_ErrorConstraintClassRemove =-2147220877 # from enum EErrorCode
	EC_ErrorConstraintClassRename =-2147220959 # from enum EErrorCode
	EC_ErrorConstraintDelete      =-2147220971 # from enum EErrorCode
	EC_ErrorConstraintDeleteDefault=-2147220970 # from enum EErrorCode
	EC_ErrorConstraintInvalidInput=-2147220974 # from enum EErrorCode
	EC_ErrorConstraintManagerConnection=-2147220948 # from enum EErrorCode
	EC_ErrorConstraintManagerReadOnly=-2147220947 # from enum EErrorCode
	EC_ErrorConstraintNotSupported=-2147220975 # from enum EErrorCode
	EC_ErrorConstraintReadValue   =-2147220973 # from enum EErrorCode
	EC_ErrorConstraintSetValue    =-2147220972 # from enum EErrorCode
	EC_ErrorConstraintUnknown     =-2147220976 # from enum EErrorCode
	EC_ErrorDelayTypeNotSupported =-2147220969 # from enum EErrorCode
	EC_ErrorDelayTypeSet          =-2147220968 # from enum EErrorCode
	EC_ErrorDesignLoad            =-2147220987 # from enum EErrorCode
	EC_ErrorDesignLock            =-2147220985 # from enum EErrorCode
	EC_ErrorDesignUnload          =-2147220986 # from enum EErrorCode
	EC_ErrorDifferentialPairAdd   =-2147220965 # from enum EErrorCode
	EC_ErrorDifferentialPairDelete=-2147220963 # from enum EErrorCode
	EC_ErrorDifferentialPairRename=-2147220964 # from enum EErrorCode
	EC_ErrorDisplayPatternAdd     =-2147220883 # from enum EErrorCode
	EC_ErrorDisplayPatternDelete  =-2147220881 # from enum EErrorCode
	EC_ErrorDisplayPatternRename  =-2147220882 # from enum EErrorCode
	EC_ErrorFormulaBegin          =-2147220923 # from enum EErrorCode
	EC_ErrorFormulaChange         =-2147220920 # from enum EErrorCode
	EC_ErrorFormulaClear          =-2147220919 # from enum EErrorCode
	EC_ErrorFormulaCommit         =-2147220922 # from enum EErrorCode
	EC_ErrorFormulaRollback       =-2147220921 # from enum EErrorCode
	EC_ErrorFromToAdd             =-2147220941 # from enum EErrorCode
	EC_ErrorFromToDelete          =-2147220940 # from enum EErrorCode
	EC_ErrorGeneralClearanceAdd   =-2147220867 # from enum EErrorCode
	EC_ErrorGeneralClearanceDelete=-2147220863 # from enum EErrorCode
	EC_ErrorGeneralClearanceDeleteDefault=-2147220864 # from enum EErrorCode
	EC_ErrorGeneralClearanceIsAlreadyDefined=-2147220865 # from enum EErrorCode
	EC_ErrorGeneralClearanceNotSupported=-2147220862 # from enum EErrorCode
	EC_ErrorGeneralClearanceUnknown=-2147220866 # from enum EErrorCode
	EC_ErrorIncorrectDecimalSymbol=-2147220978 # from enum EErrorCode
	EC_ErrorIncorrectGroupDigitsCount=-2147220961 # from enum EErrorCode
	EC_ErrorIncorrectGroupSymbol  =-2147220962 # from enum EErrorCode
	EC_ErrorIncorrectPrecision    =-2147220977 # from enum EErrorCode
	EC_ErrorInvalidColorValue     =-2147220884 # from enum EErrorCode
	EC_ErrorInvalidObject         =-2147220990 # from enum EErrorCode
	EC_ErrorInvalidParameter      =-2147220991 # from enum EErrorCode
	EC_ErrorInvalidProjectFile    =-2147220984 # from enum EErrorCode
	EC_ErrorItemNotFound          =-2147220967 # from enum EErrorCode
	EC_ErrorMatchGroupAdd         =-2147220931 # from enum EErrorCode
	EC_ErrorMatchGroupDelete      =-2147220929 # from enum EErrorCode
	EC_ErrorMatchGroupRename      =-2147220930 # from enum EErrorCode
	EC_ErrorMatchGroupTypeNotSupported=-2147220932 # from enum EErrorCode
	EC_ErrorMissingBoardName      =-2147220982 # from enum EErrorCode
	EC_ErrorMissingContext        =-2147220980 # from enum EErrorCode
	EC_ErrorNetClassAdd           =-2147220955 # from enum EErrorCode
	EC_ErrorNetClassAssignConstraintClass=-2147220950 # from enum EErrorCode
	EC_ErrorNetClassAssignNet     =-2147220951 # from enum EErrorCode
	EC_ErrorNetClassDelete        =-2147220953 # from enum EErrorCode
	EC_ErrorNetClassInsert        =-2147220880 # from enum EErrorCode
	EC_ErrorNetClassMove          =-2147220952 # from enum EErrorCode
	EC_ErrorNetClassRemove        =-2147220879 # from enum EErrorCode
	EC_ErrorNetClassRename        =-2147220954 # from enum EErrorCode
	EC_ErrorNetInsert             =-2147220928 # from enum EErrorCode
	EC_ErrorNetRemove             =-2147220927 # from enum EErrorCode
	EC_ErrorNetTypeChange         =-2147220924 # from enum EErrorCode
	EC_ErrorNoiseRuleAdd          =-2147220911 # from enum EErrorCode
	EC_ErrorNoiseRuleAggressorSet =-2147220906 # from enum EErrorCode
	EC_ErrorNoiseRuleDelete       =-2147220910 # from enum EErrorCode
	EC_ErrorNoiseRuleParallelismRuleSet=-2147220905 # from enum EErrorCode
	EC_ErrorNoiseRuleRename       =-2147220909 # from enum EErrorCode
	EC_ErrorNoiseRuleTypeNotSupported=-2147220908 # from enum EErrorCode
	EC_ErrorNoiseRuleVictimSet    =-2147220907 # from enum EErrorCode
	EC_ErrorObjectGet             =-2147220918 # from enum EErrorCode
	EC_ErrorObjectNotCommentable  =-2147220873 # from enum EErrorCode
	EC_ErrorObjectNotConstrainable=-2147220949 # from enum EErrorCode
	EC_ErrorPackageClearanceAdd   =-2147220870 # from enum EErrorCode
	EC_ErrorPackageClearanceDelete=-2147220869 # from enum EErrorCode
	EC_ErrorPackageTypeAdd        =-2147220872 # from enum EErrorCode
	EC_ErrorPackageTypeDelete     =-2147220871 # from enum EErrorCode
	EC_ErrorParallelismRuleAdd    =-2147220917 # from enum EErrorCode
	EC_ErrorParallelismRuleDelete =-2147220916 # from enum EErrorCode
	EC_ErrorParallelismRuleRename =-2147220915 # from enum EErrorCode
	EC_ErrorParallelismRuleSegmentAdd=-2147220914 # from enum EErrorCode
	EC_ErrorParallelismRuleSegmentDelete=-2147220913 # from enum EErrorCode
	EC_ErrorParallelismRuleSegmentTypeNotSupported=-2147220912 # from enum EErrorCode
	EC_ErrorPartPinPairAdd        =-2147220904 # from enum EErrorCode
	EC_ErrorPartPinPairDelete     =-2147220903 # from enum EErrorCode
	EC_ErrorPinInsert             =-2147220936 # from enum EErrorCode
	EC_ErrorPinPairAdd            =-2147220934 # from enum EErrorCode
	EC_ErrorPinPairDelete         =-2147220933 # from enum EErrorCode
	EC_ErrorPinPairInsert         =-2147220926 # from enum EErrorCode
	EC_ErrorPinPairRemove         =-2147220925 # from enum EErrorCode
	EC_ErrorPinRemove             =-2147220935 # from enum EErrorCode
	EC_ErrorPinSetAdd             =-2147220938 # from enum EErrorCode
	EC_ErrorPinSetDelete          =-2147220937 # from enum EErrorCode
	EC_ErrorPinSetTypeNotSupported=-2147220939 # from enum EErrorCode
	EC_ErrorReadBoardName         =-2147220981 # from enum EErrorCode
	EC_ErrorReadPCBFile           =-2147220966 # from enum EErrorCode
	EC_ErrorReadProjectFile       =-2147220983 # from enum EErrorCode
	EC_ErrorSchemeAdd             =-2147220895 # from enum EErrorCode
	EC_ErrorSchemeDelete          =-2147220893 # from enum EErrorCode
	EC_ErrorSchemeRename          =-2147220894 # from enum EErrorCode
	EC_ErrorSetColorFormat        =-2147220885 # from enum EErrorCode
	EC_ErrorSetUnit               =-2147220979 # from enum EErrorCode
	EC_ErrorTopologyBegin         =-2147220944 # from enum EErrorCode
	EC_ErrorTopologyChange        =-2147220945 # from enum EErrorCode
	EC_ErrorTopologyCommit        =-2147220943 # from enum EErrorCode
	EC_ErrorTopologyRollback      =-2147220942 # from enum EErrorCode
	EC_ErrorTopologyTypeNotSupported=-2147220946 # from enum EErrorCode
	EC_ErrorUnknown               =-2147220992 # from enum EErrorCode
	EC_ErrorValidation            =-2147220989 # from enum EErrorCode
	EC_ErrorValidationRequired    =-2147220988 # from enum EErrorCode
	EC_ErrorVariableAdd           =-2147220898 # from enum EErrorCode
	EC_ErrorVariableDelete        =-2147220897 # from enum EErrorCode
	EC_ErrorVariableRename        =-2147220896 # from enum EErrorCode
	FO_Equal                      =1          # from enum EFormulaOperator
	FO_Greater                    =2          # from enum EFormulaOperator
	FO_Hash                       =6          # from enum EFormulaOperator
	FO_Less                       =3          # from enum EFormulaOperator
	FO_Minus                      =5          # from enum EFormulaOperator
	FO_Plus                       =4          # from enum EFormulaOperator
	FO_PlusMinus                  =7          # from enum EFormulaOperator
	GC3D_ActiveBoardToAssembly    =0          # from enum EGeneralClearanceType
	GC3D_AnyToAny                 =1          # from enum EGeneralClearanceType
	GC3D_BondWireToAssembly       =2          # from enum EGeneralClearanceType
	GC3D_BondWireToBoardEdge      =3          # from enum EGeneralClearanceType
	GC3D_BondWireToComponent      =4          # from enum EGeneralClearanceType
	GC3D_BondWireToPCBAssembly    =5          # from enum EGeneralClearanceType
	GC3D_ComponentToAssembly      =6          # from enum EGeneralClearanceType
	GC3D_ComponentToBoardEdge     =7          # from enum EGeneralClearanceType
	GC3D_ComponentToComponent     =8          # from enum EGeneralClearanceType
	GC3D_ComponentToMechanical    =9          # from enum EGeneralClearanceType
	GC3D_ComponentToPCBAssembly   =10         # from enum EGeneralClearanceType
	GC3D_MechanicalToAssembly     =11         # from enum EGeneralClearanceType
	GC3D_MechanicalToMechanical   =12         # from enum EGeneralClearanceType
	GC3D_MechanicalToPCBAssembly  =13         # from enum EGeneralClearanceType
	GC3D_PCBAssemblyToAssembly    =14         # from enum EGeneralClearanceType
	GC3D_PCBAssemblyToPCBAssembly =15         # from enum EGeneralClearanceType
	GC_AdditionalDrillHoleConductorClearance=16         # from enum EGeneralClearanceType
	GC_AdditionalLaserHoleConductorClearance=17         # from enum EGeneralClearanceType
	GC_AdditionalPhotoHoleConductorClearance=18         # from enum EGeneralClearanceType
	GC_AdditionalPunchedHoleConductorClearance=19         # from enum EGeneralClearanceType
	GC_CavityEdgeToCavityEdge     =20         # from enum EGeneralClearanceType
	GC_CavityInsideEdgeToParts    =21         # from enum EGeneralClearanceType
	GC_CavityOutsideEdgeToNonPlaneConductor=22         # from enum EGeneralClearanceType
	GC_CavityOutsideEdgeToPlaneConductor=23         # from enum EGeneralClearanceType
	GC_ContourCavityMountingHoleToMountingHole=24         # from enum EGeneralClearanceType
	GC_ContourMountingHoleToNonPlaneConductor=25         # from enum EGeneralClearanceType
	GC_PadToResistor              =26         # from enum EGeneralClearanceType
	GC_PlacementOutlineToDesignEdge=27         # from enum EGeneralClearanceType
	GC_PlacementOutlineToPlacementObstruct=28         # from enum EGeneralClearanceType
	GC_PlacementOutlineToPlacementOutline=29         # from enum EGeneralClearanceType
	GC_TestpointCenterToTestpointCenter=30         # from enum EGeneralClearanceType
	GC_TraceToResistor            =31         # from enum EGeneralClearanceType
	LAD_Above                     =1          # from enum ELayerAttachedDielectric
	LAD_Below                     =2          # from enum ELayerAttachedDielectric
	LAD_None                      =0          # from enum ELayerAttachedDielectric
	LM_Aluminum                   =2          # from enum ELayerMetal
	LM_Copper                     =1          # from enum ELayerMetal
	LM_Custom                     =7          # from enum ELayerMetal
	LM_Gold                       =5          # from enum ELayerMetal
	LM_None                       =0          # from enum ELayerMetal
	LM_Platinum                   =6          # from enum ELayerMetal
	LM_Silver                     =4          # from enum ELayerMetal
	LM_Tin                        =3          # from enum ELayerMetal
	LNS_Bottom                    =1          # from enum ELayerNarrowSide
	LNS_Top                       =0          # from enum ELayerNarrowSide
	LPDS_Hatched                  =2          # from enum ELayerPourDrawStyle
	LPDS_None                     =0          # from enum ELayerPourDrawStyle
	LPDS_Outline                  =3          # from enum ELayerPourDrawStyle
	LPDS_Solid                    =1          # from enum ELayerPourDrawStyle
	LP_Custom                     =3          # from enum ELayerProcess
	LP_Electrodeposit             =1          # from enum ELayerProcess
	LP_None                       =0          # from enum ELayerProcess
	LP_Rolling                    =2          # from enum ELayerProcess
	LTE_Core                      =1          # from enum ELayerTechnology
	LTE_FlexCore                  =3          # from enum ELayerTechnology
	LTE_None                      =0          # from enum ELayerTechnology
	LTE_Prepreg                   =2          # from enum ELayerTechnology
	LTS_Both                      =3          # from enum ELayerTreatedSide
	LTS_Bottom                    =2          # from enum ELayerTreatedSide
	LTS_None                      =0          # from enum ELayerTreatedSide
	LTS_Top                       =1          # from enum ELayerTreatedSide
	LT_Dielectric                 =1          # from enum ELayerType
	LT_Metallic                   =0          # from enum ELayerType
	LT_Unknown                    =-1         # from enum ELayerType
	LU_Adhesive                   =8          # from enum ELayerUsage
	LU_CoverLayer                 =9          # from enum ELayerUsage
	LU_Flexible                   =7          # from enum ELayerUsage
	LU_FloodedSignal              =3          # from enum ELayerUsage
	LU_Mixed                      =2          # from enum ELayerUsage
	LU_Plane                      =1          # from enum ELayerUsage
	LU_Plating                    =6          # from enum ELayerUsage
	LU_Signal                     =0          # from enum ELayerUsage
	LU_SolderMask                 =5          # from enum ELayerUsage
	LU_Stiffener                  =10         # from enum ELayerUsage
	LU_Substrate                  =4          # from enum ELayerUsage
	LU_Unknown                    =-1         # from enum ELayerUsage
	MGM_AllMatchGroups            =3          # from enum EMatchGroupMask
	MGM_Hierarchical              =2          # from enum EMatchGroupMask
	MGM_Standard                  =1          # from enum EMatchGroupMask
	MGT_Hierarchical              =1          # from enum EMatchGroupType
	MGT_Standard                  =0          # from enum EMatchGroupType
	NM_AllNets                    =15         # from enum ENetMask
	NM_DifferentialPairs          =8          # from enum ENetMask
	NM_ElectricalNets             =2          # from enum ENetMask
	NM_Nets                       =1          # from enum ENetMask
	NM_PowerNets                  =4          # from enum ENetMask
	NT_DifferentialPair           =3          # from enum ENetType
	NT_ElectricalNet              =1          # from enum ENetType
	NT_Last                       =4          # from enum ENetType
	NT_Net                        =0          # from enum ENetType
	NT_PowerNet                   =2          # from enum ENetType
	NRC_All                       =6          # from enum ENoiseRuleCrosstalk
	NRC_High                      =1          # from enum ENoiseRuleCrosstalk
	NRC_HighLow                   =3          # from enum ENoiseRuleCrosstalk
	NRC_HighTristate              =4          # from enum ENoiseRuleCrosstalk
	NRC_Low                       =0          # from enum ENoiseRuleCrosstalk
	NRC_LowTristate               =5          # from enum ENoiseRuleCrosstalk
	NRC_Tristate                  =2          # from enum ENoiseRuleCrosstalk
	NRM_AllNoiseRules             =3          # from enum ENoiseRuleMask
	NRM_ClassToClass              =1          # from enum ENoiseRuleMask
	NRM_NetToNet                  =2          # from enum ENoiseRuleMask
	NRT_ClassToClass              =1          # from enum ENoiseRuleType
	NRT_NetToNet                  =0          # from enum ENoiseRuleType
	OM_All                        =2          # from enum EObjectMask
	OM_Top                        =1          # from enum EObjectMask
	OT_Any                        =0          # from enum EObjectType
	OT_ClassClearance             =31         # from enum EObjectType
	OT_ClearanceRule              =25         # from enum EObjectType
	OT_Component                  =51         # from enum EObjectType
	OT_Constant                   =30         # from enum EObjectType
	OT_ConstraintClass            =26         # from enum EObjectType
	OT_DifferentialPair           =46         # from enum EObjectType
	OT_DisplayPattern             =86         # from enum EObjectType
	OT_ElectricalNet              =47         # from enum EObjectType
	OT_Formula                    =139        # from enum EObjectType
	OT_FromTo                     =50         # from enum EObjectType
	OT_GeneralClearance           =28         # from enum EObjectType
	OT_Layer                      =23         # from enum EObjectType
	OT_MatchGroup                 =136        # from enum EObjectType
	OT_Net                        =49         # from enum EObjectType
	OT_NetClass                   =24         # from enum EObjectType
	OT_NoiseRule                  =36         # from enum EObjectType
	OT_PackageClearance           =32         # from enum EObjectType
	OT_PackageType                =142        # from enum EObjectType
	OT_ParallelismRule            =34         # from enum EObjectType
	OT_ParallelismRuleSegment     =35         # from enum EObjectType
	OT_Part                       =53         # from enum EObjectType
	OT_PartPin                    =54         # from enum EObjectType
	OT_PartPinPair                =71         # from enum EObjectType
	OT_Pin                        =52         # from enum EObjectType
	OT_PinPair                    =48         # from enum EObjectType
	OT_PinSet                     =138        # from enum EObjectType
	OT_Scheme                     =37         # from enum EObjectType
	OT_Stackup                    =141        # from enum EObjectType
	OT_Topology                   =137        # from enum EObjectType
	OT_Variable                   =140        # from enum EObjectType
	PCD_All                       =4          # from enum EPackageClearanceDirection
	PCD_EndToEnd                  =1          # from enum EPackageClearanceDirection
	PCD_EndToSide                 =3          # from enum EPackageClearanceDirection
	PCD_SideToEnd                 =2          # from enum EPackageClearanceDirection
	PCD_SideToSide                =0          # from enum EPackageClearanceDirection
	PCS_Both                      =2          # from enum EPackageClearanceSide
	PCS_Bottom                    =1          # from enum EPackageClearanceSide
	PCS_Top                       =0          # from enum EPackageClearanceSide
	PRSM_AdjacentLayers           =2          # from enum EParallelismRuleSegmentMask
	PRSM_AllSegments              =3          # from enum EParallelismRuleSegmentMask
	PRSM_SameLayers               =1          # from enum EParallelismRuleSegmentMask
	PRST_AdjacentLayers           =1          # from enum EParallelismRuleSegmentType
	PRST_SameLayers               =0          # from enum EParallelismRuleSegmentType
	PST_Balanced                  =3          # from enum EPinSetType
	PST_Chained                   =1          # from enum EPinSetType
	PST_MST                       =0          # from enum EPinSetType
	PST_TShape                    =2          # from enum EPinSetType
	PST_Unbalanced                =4          # from enum EPinSetType
	PT_Component                  =0          # from enum EPinType
	PT_Guide                      =2          # from enum EPinType
	PT_Virtual                    =1          # from enum EPinType
	RM_Cannonball                 =0          # from enum ERoughnessModel
	RM_Hammerstad                 =1          # from enum ERoughnessModel
	RM_ModifiedHammerstad         =2          # from enum ERoughnessModel
	RP_Ra                         =1          # from enum ERoughnessParameter
	RP_Rrms                       =0          # from enum ERoughnessParameter
	RP_Rz                         =2          # from enum ERoughnessParameter
	TP_L                          =1          # from enum ETopologyPinType
	TP_S                          =0          # from enum ETopologyPinType
	TP_T                          =2          # from enum ETopologyPinType
	TT_Chained                    =1          # from enum ETopologyType
	TT_Complex                    =6          # from enum ETopologyType
	TT_Custom                     =5          # from enum ETopologyType
	TT_HTree                      =3          # from enum ETopologyType
	TT_MST                        =0          # from enum ETopologyType
	TT_Mixed                      =7          # from enum ETopologyType
	TT_Star                       =4          # from enum ETopologyType
	TT_TShape                     =2          # from enum ETopologyType
	U_Capacitance_F               =0          # from enum EUnitCapacitance
	U_Capacitance_Last            =5          # from enum EUnitCapacitance
	U_Capacitance_mF              =1          # from enum EUnitCapacitance
	U_Capacitance_nF              =3          # from enum EUnitCapacitance
	U_Capacitance_pF              =4          # from enum EUnitCapacitance
	U_Capacitance_uF              =2          # from enum EUnitCapacitance
	U_Current_A                   =0          # from enum EUnitCurrent
	U_Current_Last                =5          # from enum EUnitCurrent
	U_Current_mA                  =1          # from enum EUnitCurrent
	U_Current_nA                  =3          # from enum EUnitCurrent
	U_Current_pA                  =4          # from enum EUnitCurrent
	U_Current_uA                  =2          # from enum EUnitCurrent
	U_CurrentDensity_Last         =1          # from enum EUnitCurrentDensity
	U_CurrentDensity_mA_per_th2   =0          # from enum EUnitCurrentDensity
	U_Inductance_H                =0          # from enum EUnitInductance
	U_Inductance_Last             =4          # from enum EUnitInductance
	U_Inductance_mH               =1          # from enum EUnitInductance
	U_Inductance_nH               =3          # from enum EUnitInductance
	U_Inductance_uH               =2          # from enum EUnitInductance
	U_Linear_Last                 =5          # from enum EUnitLinear
	U_Linear_in                   =0          # from enum EUnitLinear
	U_Linear_mm                   =2          # from enum EUnitLinear
	U_Linear_nm                   =4          # from enum EUnitLinear
	U_Linear_th                   =1          # from enum EUnitLinear
	U_Linear_um                   =3          # from enum EUnitLinear
	U_Power_Last                  =5          # from enum EUnitPower
	U_Power_W                     =1          # from enum EUnitPower
	U_Power_kW                    =0          # from enum EUnitPower
	U_Power_mW                    =2          # from enum EUnitPower
	U_Power_nW                    =4          # from enum EUnitPower
	U_Power_uW                    =3          # from enum EUnitPower
	U_Resistance_Last             =5          # from enum EUnitResistance
	U_Resistance_MegOhm           =0          # from enum EUnitResistance
	U_Resistance_Ohm              =2          # from enum EUnitResistance
	U_Resistance_kOhm             =1          # from enum EUnitResistance
	U_Resistance_mOhm             =3          # from enum EUnitResistance
	U_Resistance_uOhm             =4          # from enum EUnitResistance
	U_Temperature_Last            =1          # from enum EUnitTemperature
	U_Temperature_degC            =0          # from enum EUnitTemperature
	U_Theta_Last                  =1          # from enum EUnitTheta
	U_Theta_degC_per_W            =0          # from enum EUnitTheta
	U_Time_Last                   =5          # from enum EUnitTime
	U_Time_ms                     =1          # from enum EUnitTime
	U_Time_ns                     =3          # from enum EUnitTime
	U_Time_ps                     =4          # from enum EUnitTime
	U_Time_s                      =0          # from enum EUnitTime
	U_Time_us                     =2          # from enum EUnitTime
	U_Voltage_Last                =5          # from enum EUnitVoltage
	U_Voltage_V                   =1          # from enum EUnitVoltage
	U_Voltage_kV                  =0          # from enum EUnitVoltage
	U_Voltage_mV                  =2          # from enum EUnitVoltage
	U_Voltage_nV                  =4          # from enum EUnitVoltage
	U_Voltage_uV                  =3          # from enum EUnitVoltage

from win32com.client import DispatchBaseClass
class IBase(DispatchBaseClass):
	CLSID = IID('{5147D582-BD1E-4F71-82E9-D7ECD5956AE6}')
	coclass_clsid = IID('{FDD01A44-69ED-4E7F-88C7-7947E8C7BD69}')

	def IsDefault(self):
		'Returns true if the object is default and cannot be deleted.'
		return self._oleobj_.InvokeTypes(1610743811, LCID, 1, (11, 0), (),)

	def IsValid(self):
		'Returns true if the object is still valid.'
		return self._oleobj_.InvokeTypes(1610743810, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"Name": (0, 2, (8, 0), (), "Name", None),
		# Method 'Parent' returns object of type 'IObject'
		"Parent": (1610743809, 2, (9, 0), (), "Parent", '{7A5D1A08-B723-4929-BB46-A801DC642EB6}'),
	}
	_prop_map_put_ = {
	}

	Name: str # read_only
	Parent: str # IObject; read_only

	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
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

class IClass(DispatchBaseClass):
	CLSID = IID('{AC287CEE-0F24-4AA5-AB3F-7FCAB43B13A6}')
	coclass_clsid = IID('{3FA6B387-5FB9-4380-B4FF-BD1D0CC40F08}')

	def AssignNet(self, p_pNet=defaultNamedNotOptArg):
		'Assigns the given net to the class.'
		return self._oleobj_.InvokeTypes(1610874883, LCID, 1, (24, 0), ((9, 1),),p_pNet
			)

	# Result is of type IConstraintsMutable
	# The method GetConstraints is actually a property, but must be used as a method to correctly pass the arguments
	def GetConstraints(self, p_nConstraintMask=7):
		'Returns the collection of constraints, filtered by EConstraintMask constant.'
		ret = self._oleobj_.InvokeTypes(1610809345, LCID, 2, (9, 0), ((3, 49),),p_nConstraintMask
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetConstraints', '{1DDEC891-7D43-4EE9-9BD4-63772C577150}')
		return ret

	# Result is of type INets
	# The method GetNets is actually a property, but must be used as a method to correctly pass the arguments
	def GetNets(self, p_nNetMask=1):
		'Returns the collection of nets assigned to the class, filtered by ENetMask constant.'
		ret = self._oleobj_.InvokeTypes(1610874881, LCID, 2, (9, 0), ((3, 49),),p_nNetMask
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetNets', '{EAF633E9-E21E-47FF-A361-60A4B480301F}')
		return ret

	# Result is of type IObjects
	# The method GetObjects is actually a property, but must be used as a method to correctly pass the arguments
	def GetObjects(self, p_eObjectType=0):
		'Returns the collection of child objects, filtered by EObjectType constant.'
		ret = self._oleobj_.InvokeTypes(1610809347, LCID, 2, (9, 0), ((3, 49),),p_eObjectType
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjects', '{44747797-9642-483B-AB9C-6AE0A1899549}')
		return ret

	def IsDefault(self):
		'Returns true if the object is default and cannot be deleted.'
		return self._oleobj_.InvokeTypes(1610743811, LCID, 1, (11, 0), (),)

	def IsValid(self):
		'Returns true if the object is still valid.'
		return self._oleobj_.InvokeTypes(1610743810, LCID, 1, (11, 0), (),)

	def Rename(self, p_strName=defaultNamedNotOptArg):
		'Changes the name of the object.'
		return self._oleobj_.InvokeTypes(1610874882, LCID, 1, (24, 0), ((8, 1),),p_strName
			)

	_prop_map_get_ = {
		# Method 'Comments' returns object of type 'ICommentsMutable'
		"Comments": (1610809346, 2, (9, 0), (), "Comments", '{23FAC1D8-2578-42BC-9F65-F04930FB6489}'),
		# Method 'Constraints' returns object of type 'IConstraintsMutable'
		"Constraints": (1610809345, 2, (9, 0), ((3, 49),), "Constraints", '{1DDEC891-7D43-4EE9-9BD4-63772C577150}'),
		# Method 'DisplayPattern' returns object of type 'IDisplayPattern'
		"DisplayPattern": (1610874884, 2, (9, 0), (), "DisplayPattern", '{E6F44CAC-B61D-4437-971F-60F01875D6BB}'),
		"FullName": (1610874880, 2, (8, 0), (), "FullName", None),
		"Name": (0, 2, (8, 0), (), "Name", None),
		# Method 'Nets' returns object of type 'INets'
		"Nets": (1610874881, 2, (9, 0), ((3, 49),), "Nets", '{EAF633E9-E21E-47FF-A361-60A4B480301F}'),
		"ObjectType": (1610809344, 2, (3, 0), (), "ObjectType", None),
		# Method 'Objects' returns object of type 'IObjects'
		"Objects": (1610809347, 2, (9, 0), ((3, 49),), "Objects", '{44747797-9642-483B-AB9C-6AE0A1899549}'),
		# Method 'Parent' returns object of type 'IObject'
		"Parent": (1610743809, 2, (9, 0), (), "Parent", '{7A5D1A08-B723-4929-BB46-A801DC642EB6}'),
	}
	_prop_map_put_ = {
	}

	Comments: str # ICommentsMutable; read_only
	Constraints: str # IConstraintsMutable; read_only
	DisplayPattern: str # IDisplayPattern; read_only
	FullName: str # read_only
	Name: str # read_only
	Nets: str # INets; read_only
	ObjectType: str # read_only
	Objects: str # IObjects; read_only
	Parent: str # IObject; read_only

	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
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

class IClassClearance(DispatchBaseClass):
	CLSID = IID('{77040253-C4BE-4037-B759-739678531FE8}')
	coclass_clsid = IID('{6E8C0221-D322-40BA-80E0-0271F8DFD70C}')

	# Result is of type IConstraintsMutable
	# The method GetConstraints is actually a property, but must be used as a method to correctly pass the arguments
	def GetConstraints(self, p_nConstraintMask=7):
		'Returns the collection of constraints, filtered by EConstraintMask constant.'
		ret = self._oleobj_.InvokeTypes(1610809345, LCID, 2, (9, 0), ((3, 49),),p_nConstraintMask
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetConstraints', '{1DDEC891-7D43-4EE9-9BD4-63772C577150}')
		return ret

	# Result is of type IObjects
	# The method GetObjects is actually a property, but must be used as a method to correctly pass the arguments
	def GetObjects(self, p_eObjectType=0):
		'Returns the collection of child objects, filtered by EObjectType constant.'
		ret = self._oleobj_.InvokeTypes(1610809347, LCID, 2, (9, 0), ((3, 49),),p_eObjectType
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjects', '{44747797-9642-483B-AB9C-6AE0A1899549}')
		return ret

	def IsDefault(self):
		'Returns true if the object is default and cannot be deleted.'
		return self._oleobj_.InvokeTypes(1610743811, LCID, 1, (11, 0), (),)

	def IsValid(self):
		'Returns true if the object is still valid.'
		return self._oleobj_.InvokeTypes(1610743810, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"ClassClearanceType": (1610874880, 2, (3, 0), (), "ClassClearanceType", None),
		# Method 'ClearanceRule' returns object of type 'IClearanceRule'
		"ClearanceRule": (1610874884, 2, (9, 0), (), "ClearanceRule", '{A0F38DDB-184D-4D4E-9E99-FFF4E73A4235}'),
		# Method 'Comments' returns object of type 'ICommentsMutable'
		"Comments": (1610809346, 2, (9, 0), (), "Comments", '{23FAC1D8-2578-42BC-9F65-F04930FB6489}'),
		# Method 'Constraints' returns object of type 'IConstraintsMutable'
		"Constraints": (1610809345, 2, (9, 0), ((3, 49),), "Constraints", '{1DDEC891-7D43-4EE9-9BD4-63772C577150}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
		"ObjectType": (1610809344, 2, (3, 0), (), "ObjectType", None),
		# Method 'Objects' returns object of type 'IObjects'
		"Objects": (1610809347, 2, (9, 0), ((3, 49),), "Objects", '{44747797-9642-483B-AB9C-6AE0A1899549}'),
		# Method 'Parent' returns object of type 'IObject'
		"Parent": (1610743809, 2, (9, 0), (), "Parent", '{7A5D1A08-B723-4929-BB46-A801DC642EB6}'),
		# Method 'Scheme' returns object of type 'IScheme'
		"Scheme": (1610874881, 2, (9, 0), (), "Scheme", '{6F39247C-17C2-4C9F-B14C-469620C80FC4}'),
		# Method 'SourceNetClass' returns object of type 'INetClass'
		"SourceNetClass": (1610874882, 2, (9, 0), (), "SourceNetClass", '{791A98C5-512E-45E0-8F4F-715A45F5707A}'),
		# Method 'TargetNetClass' returns object of type 'INetClass'
		"TargetNetClass": (1610874883, 2, (9, 0), (), "TargetNetClass", '{791A98C5-512E-45E0-8F4F-715A45F5707A}'),
	}
	_prop_map_put_ = {
		"ClearanceRule": ((1610874884, LCID, 4, 0),()),
	}

	ClassClearanceType: str # read_only
	ClearanceRule: str # read/write
	Comments: str # ICommentsMutable; read_only
	Constraints: str # IConstraintsMutable; read_only
	Name: str # read_only
	ObjectType: str # read_only
	Objects: str # IObjects; read_only
	Parent: str # IObject; read_only
	Scheme: str # IScheme; read_only
	SourceNetClass: str # INetClass; read_only
	TargetNetClass: str # INetClass; read_only

	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
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

class IClassClearances(DispatchBaseClass):
	CLSID = IID('{96FD6C42-8C02-4A00-A1B6-C47FB0D47913}')
	coclass_clsid = IID('{5FF6AAE0-F6A3-40A0-8B3E-36E1C22D7808}')

	# Result is of type IClassClearance
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the class clearance of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{77040253-C4BE-4037-B759-739678531FE8}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the class clearance of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{77040253-C4BE-4037-B759-739678531FE8}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{77040253-C4BE-4037-B759-739678531FE8}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IClassClearancesMutable(DispatchBaseClass):
	CLSID = IID('{FA648CF5-E9A3-4841-AD76-BD4BCD55DF45}')
	coclass_clsid = IID('{3D99E63D-958F-4443-9BA7-4C07BBB99068}')

	# Result is of type IClassClearance
	def Add(self, p_eClassClearanceType=defaultNamedNotOptArg, p_strName=defaultNamedNotOptArg, p_pScheme=defaultNamedNotOptArg, p_pSourceNetClass=defaultNamedNotOptArg
			, p_pTargetNetClass=defaultNamedNotOptArg, p_pClearanceRule=defaultNamedNotOptArg):
		'Creates the class clearance of the given parameters and adds it to the collection.'
		ret = self._oleobj_.InvokeTypes(1610874880, LCID, 1, (9, 0), ((3, 1), (8, 1), (9, 1), (9, 1), (9, 1), (9, 1)),p_eClassClearanceType
			, p_strName, p_pScheme, p_pSourceNetClass, p_pTargetNetClass, p_pClearanceRule
			)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{77040253-C4BE-4037-B759-739678531FE8}')
		return ret

	def Delete(self, p_vIndex=defaultNamedNotOptArg):
		'Deletes the class clearance of the given index or name and removes it from the collection.'
		return self._oleobj_.InvokeTypes(1610874881, LCID, 1, (24, 0), ((12, 1),),p_vIndex
			)

	# Result is of type IClassClearance
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the class clearance of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{77040253-C4BE-4037-B759-739678531FE8}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the class clearance of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{77040253-C4BE-4037-B759-739678531FE8}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{77040253-C4BE-4037-B759-739678531FE8}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IClearanceRule(DispatchBaseClass):
	CLSID = IID('{A0F38DDB-184D-4D4E-9E99-FFF4E73A4235}')
	coclass_clsid = IID('{02D9EB90-8303-47C0-8C9B-27D02DE97D52}')

	# Result is of type IConstraintsMutable
	# The method GetConstraints is actually a property, but must be used as a method to correctly pass the arguments
	def GetConstraints(self, p_nConstraintMask=7):
		'Returns the collection of constraints, filtered by EConstraintMask constant.'
		ret = self._oleobj_.InvokeTypes(1610809345, LCID, 2, (9, 0), ((3, 49),),p_nConstraintMask
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetConstraints', '{1DDEC891-7D43-4EE9-9BD4-63772C577150}')
		return ret

	# Result is of type IObjects
	# The method GetObjects is actually a property, but must be used as a method to correctly pass the arguments
	def GetObjects(self, p_eObjectType=0):
		'Returns the collection of child objects, filtered by EObjectType constant.'
		ret = self._oleobj_.InvokeTypes(1610809347, LCID, 2, (9, 0), ((3, 49),),p_eObjectType
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjects', '{44747797-9642-483B-AB9C-6AE0A1899549}')
		return ret

	def IsDefault(self):
		'Returns true if the object is default and cannot be deleted.'
		return self._oleobj_.InvokeTypes(1610743811, LCID, 1, (11, 0), (),)

	def IsValid(self):
		'Returns true if the object is still valid.'
		return self._oleobj_.InvokeTypes(1610743810, LCID, 1, (11, 0), (),)

	def Rename(self, p_strName=defaultNamedNotOptArg):
		'Changes the name of the object.'
		return self._oleobj_.InvokeTypes(1610874883, LCID, 1, (24, 0), ((8, 1),),p_strName
			)

	_prop_map_get_ = {
		# Method 'ClassClearances' returns object of type 'IClassClearances'
		"ClassClearances": (1610874881, 2, (9, 0), (), "ClassClearances", '{96FD6C42-8C02-4A00-A1B6-C47FB0D47913}'),
		"ClearanceRuleType": (1610874880, 2, (3, 0), (), "ClearanceRuleType", None),
		# Method 'Comments' returns object of type 'ICommentsMutable'
		"Comments": (1610809346, 2, (9, 0), (), "Comments", '{23FAC1D8-2578-42BC-9F65-F04930FB6489}'),
		# Method 'Constraints' returns object of type 'IConstraintsMutable'
		"Constraints": (1610809345, 2, (9, 0), ((3, 49),), "Constraints", '{1DDEC891-7D43-4EE9-9BD4-63772C577150}'),
		# Method 'Layers' returns object of type 'IRuleLayers'
		"Layers": (1610874882, 2, (9, 0), (), "Layers", '{6710F183-E176-48F4-B3CA-DBD22E0CF5FF}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
		"ObjectType": (1610809344, 2, (3, 0), (), "ObjectType", None),
		# Method 'Objects' returns object of type 'IObjects'
		"Objects": (1610809347, 2, (9, 0), ((3, 49),), "Objects", '{44747797-9642-483B-AB9C-6AE0A1899549}'),
		# Method 'Parent' returns object of type 'IObject'
		"Parent": (1610743809, 2, (9, 0), (), "Parent", '{7A5D1A08-B723-4929-BB46-A801DC642EB6}'),
	}
	_prop_map_put_ = {
	}

	ClassClearances: str # IClassClearances; read_only
	ClearanceRuleType: str # read_only
	Comments: str # ICommentsMutable; read_only
	Constraints: str # IConstraintsMutable; read_only
	Layers: str # IRuleLayers; read_only
	Name: str # read_only
	ObjectType: str # read_only
	Objects: str # IObjects; read_only
	Parent: str # IObject; read_only

	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
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

class IClearanceRules(DispatchBaseClass):
	CLSID = IID('{349CEE9A-3FFB-4FA8-AB31-F98DC12E4E74}')
	coclass_clsid = IID('{CC09F366-B8E9-4E10-84DC-8C92197B0207}')

	# Result is of type IClearanceRule
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the clearance rule of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{A0F38DDB-184D-4D4E-9E99-FFF4E73A4235}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the clearance rule of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{A0F38DDB-184D-4D4E-9E99-FFF4E73A4235}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{A0F38DDB-184D-4D4E-9E99-FFF4E73A4235}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IClearanceRulesMutable(DispatchBaseClass):
	CLSID = IID('{088425F1-88A0-4675-B9B9-D6FBC0454CF3}')
	coclass_clsid = IID('{15582A4E-85ED-45F4-BA66-696181360E83}')

	# Result is of type IClearanceRule
	def Add(self, p_strName=defaultNamedNotOptArg):
		'Creates the clearance rule of the given name and adds it to the collection.'
		ret = self._oleobj_.InvokeTypes(1610874880, LCID, 1, (9, 0), ((8, 1),),p_strName
			)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{A0F38DDB-184D-4D4E-9E99-FFF4E73A4235}')
		return ret

	def Delete(self, p_vIndex=defaultNamedNotOptArg):
		'Deletes the clearance rule of the given index or name and removes it from the collection.'
		return self._oleobj_.InvokeTypes(1610874881, LCID, 1, (24, 0), ((12, 1),),p_vIndex
			)

	# Result is of type IClearanceRule
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the clearance rule of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{A0F38DDB-184D-4D4E-9E99-FFF4E73A4235}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the clearance rule of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{A0F38DDB-184D-4D4E-9E99-FFF4E73A4235}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{A0F38DDB-184D-4D4E-9E99-FFF4E73A4235}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ICollection(DispatchBaseClass):
	CLSID = IID('{32B4374A-B64C-4E76-AEDB-5C944EF0D68A}')
	coclass_clsid = IID('{E2E4868A-9FD4-478F-A504-0AB8B2DEB117}')

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IComment(DispatchBaseClass):
	CLSID = IID('{8A5D0FF3-3D6C-4AD0-9F2C-150132A98B73}')
	coclass_clsid = IID('{C5CB9071-36B8-4E69-95FC-41839093973B}')

	_prop_map_get_ = {
		"ConstraintType": (1610743810, 2, (3, 0), (), "ConstraintType", None),
		# Method 'Parent' returns object of type 'IObject'
		"Parent": (1610743811, 2, (9, 0), (), "Parent", '{7A5D1A08-B723-4929-BB46-A801DC642EB6}'),
		"Value": (0, 2, (8, 0), (), "Value", None),
	}
	_prop_map_put_ = {
		"Value": ((0, LCID, 4, 0),()),
	}

	ConstraintType: str # read_only
	Parent: str # IObject; read_only
	Value: str # read/write

	# Default property for this class is 'Value'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Value", None))
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

class IComments(DispatchBaseClass):
	CLSID = IID('{32285CE8-91FA-40D4-844F-9D468F111061}')
	coclass_clsid = IID('{F7269414-6A1B-4F30-9FA0-619B80717D2A}')

	# Result is of type IComment
	def FindItem(self, p_eType=defaultNamedNotOptArg):
		'Finds the comment of the given constraint type.'
		ret = self._oleobj_.InvokeTypes(1610809345, LCID, 1, (9, 0), ((3, 1),),p_eType
			)
		if ret is not None:
			ret = Dispatch(ret, 'FindItem', '{8A5D0FF3-3D6C-4AD0-9F2C-150132A98B73}')
		return ret

	# Result is of type IComment
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the comment of the given index or constraint name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{8A5D0FF3-3D6C-4AD0-9F2C-150132A98B73}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the comment of the given index or constraint name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{8A5D0FF3-3D6C-4AD0-9F2C-150132A98B73}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{8A5D0FF3-3D6C-4AD0-9F2C-150132A98B73}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ICommentsMutable(DispatchBaseClass):
	CLSID = IID('{23FAC1D8-2578-42BC-9F65-F04930FB6489}')
	coclass_clsid = IID('{65183681-9F46-4373-B909-A345126B459B}')

	# Result is of type IComment
	def Add(self, p_strName=defaultNamedNotOptArg, p_strValue=defaultNamedNotOptArg):
		'Creates the comment of the given constraint name and value, and adds it to the collection. Empty constraint name creates comment on object.'
		ret = self._oleobj_.InvokeTypes(1610874880, LCID, 1, (9, 0), ((8, 1), (8, 1)),p_strName
			, p_strValue)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{8A5D0FF3-3D6C-4AD0-9F2C-150132A98B73}')
		return ret

	# Result is of type IComment
	def AddByType(self, p_eType=defaultNamedNotOptArg, p_strValue=defaultNamedNotOptArg):
		'Creates the comment of the given constraint type and value, and adds it to the collection.'
		ret = self._oleobj_.InvokeTypes(1610874881, LCID, 1, (9, 0), ((3, 1), (8, 1)),p_eType
			, p_strValue)
		if ret is not None:
			ret = Dispatch(ret, 'AddByType', '{8A5D0FF3-3D6C-4AD0-9F2C-150132A98B73}')
		return ret

	def Delete(self, p_vIndex=defaultNamedNotOptArg):
		'Deletes the comment of the given index or constraint name and removes it from the collection.'
		return self._oleobj_.InvokeTypes(1610874882, LCID, 1, (24, 0), ((12, 1),),p_vIndex
			)

	def DeleteByType(self, p_eType=defaultNamedNotOptArg):
		'Deletes the comment of the given constraint type and removes it from the collection.'
		return self._oleobj_.InvokeTypes(1610874883, LCID, 1, (24, 0), ((3, 1),),p_eType
			)

	# Result is of type IComment
	def FindItem(self, p_eType=defaultNamedNotOptArg):
		'Finds the comment of the given constraint type.'
		ret = self._oleobj_.InvokeTypes(1610809345, LCID, 1, (9, 0), ((3, 1),),p_eType
			)
		if ret is not None:
			ret = Dispatch(ret, 'FindItem', '{8A5D0FF3-3D6C-4AD0-9F2C-150132A98B73}')
		return ret

	# Result is of type IComment
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the comment of the given index or constraint name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{8A5D0FF3-3D6C-4AD0-9F2C-150132A98B73}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the comment of the given index or constraint name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{8A5D0FF3-3D6C-4AD0-9F2C-150132A98B73}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{8A5D0FF3-3D6C-4AD0-9F2C-150132A98B73}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IComponent(DispatchBaseClass):
	CLSID = IID('{60516EC5-86D9-4E16-86E7-9B66302D3A83}')
	coclass_clsid = IID('{E8CEF3AC-4D63-4E45-B553-CCC01DFC4202}')

	# Result is of type IConstraintsMutable
	# The method GetConstraints is actually a property, but must be used as a method to correctly pass the arguments
	def GetConstraints(self, p_nConstraintMask=7):
		'Returns the collection of constraints, filtered by EConstraintMask constant.'
		ret = self._oleobj_.InvokeTypes(1610809345, LCID, 2, (9, 0), ((3, 49),),p_nConstraintMask
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetConstraints', '{1DDEC891-7D43-4EE9-9BD4-63772C577150}')
		return ret

	# Result is of type IObjects
	# The method GetObjects is actually a property, but must be used as a method to correctly pass the arguments
	def GetObjects(self, p_eObjectType=0):
		'Returns the collection of child objects, filtered by EObjectType constant.'
		ret = self._oleobj_.InvokeTypes(1610809347, LCID, 2, (9, 0), ((3, 49),),p_eObjectType
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjects', '{44747797-9642-483B-AB9C-6AE0A1899549}')
		return ret

	def IsDefault(self):
		'Returns true if the object is default and cannot be deleted.'
		return self._oleobj_.InvokeTypes(1610743811, LCID, 1, (11, 0), (),)

	def IsValid(self):
		'Returns true if the object is still valid.'
		return self._oleobj_.InvokeTypes(1610743810, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		# Method 'Comments' returns object of type 'ICommentsMutable'
		"Comments": (1610809346, 2, (9, 0), (), "Comments", '{23FAC1D8-2578-42BC-9F65-F04930FB6489}'),
		# Method 'Constraints' returns object of type 'IConstraintsMutable'
		"Constraints": (1610809345, 2, (9, 0), ((3, 49),), "Constraints", '{1DDEC891-7D43-4EE9-9BD4-63772C577150}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
		"ObjectType": (1610809344, 2, (3, 0), (), "ObjectType", None),
		# Method 'Objects' returns object of type 'IObjects'
		"Objects": (1610809347, 2, (9, 0), ((3, 49),), "Objects", '{44747797-9642-483B-AB9C-6AE0A1899549}'),
		# Method 'Parent' returns object of type 'IObject'
		"Parent": (1610743809, 2, (9, 0), (), "Parent", '{7A5D1A08-B723-4929-BB46-A801DC642EB6}'),
		# Method 'Pins' returns object of type 'IPinsMutable'
		"Pins": (1610874880, 2, (9, 0), (), "Pins", '{B034C5D7-24E1-4F6A-836A-7906257DABAA}'),
	}
	_prop_map_put_ = {
	}

	Comments: str # ICommentsMutable; read_only
	Constraints: str # IConstraintsMutable; read_only
	Name: str # read_only
	ObjectType: str # read_only
	Objects: str # IObjects; read_only
	Parent: str # IObject; read_only
	Pins: str # IPinsMutable; read_only

	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
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

class IComponents(DispatchBaseClass):
	CLSID = IID('{AC3ABD04-B1DD-47C7-8A94-404DFD764E56}')
	coclass_clsid = IID('{B7DC1FFB-DDF7-4710-96DF-9CE53C3399A1}')

	# Result is of type IComponent
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the component of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{60516EC5-86D9-4E16-86E7-9B66302D3A83}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the component of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{60516EC5-86D9-4E16-86E7-9B66302D3A83}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{60516EC5-86D9-4E16-86E7-9B66302D3A83}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IComponentsMutable(DispatchBaseClass):
	CLSID = IID('{E010B178-C036-4BDE-815F-9B48CE213D1E}')
	coclass_clsid = IID('{153D5723-3036-4796-9184-BA5AA4999BF7}')

	# Result is of type IComponent
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the component of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{60516EC5-86D9-4E16-86E7-9B66302D3A83}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the component of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{60516EC5-86D9-4E16-86E7-9B66302D3A83}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{60516EC5-86D9-4E16-86E7-9B66302D3A83}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IConstant(DispatchBaseClass):
	CLSID = IID('{E43EED65-B104-4518-A7C0-21C3FA01B4F5}')
	coclass_clsid = IID('{104F0D8D-82A5-44BA-A563-92EBF5BAEEB7}')

	# Result is of type IConstraintsMutable
	# The method GetConstraints is actually a property, but must be used as a method to correctly pass the arguments
	def GetConstraints(self, p_nConstraintMask=7):
		'Returns the collection of constraints, filtered by EConstraintMask constant.'
		ret = self._oleobj_.InvokeTypes(1610809345, LCID, 2, (9, 0), ((3, 49),),p_nConstraintMask
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetConstraints', '{1DDEC891-7D43-4EE9-9BD4-63772C577150}')
		return ret

	# Result is of type IObjects
	# The method GetObjects is actually a property, but must be used as a method to correctly pass the arguments
	def GetObjects(self, p_eObjectType=0):
		'Returns the collection of child objects, filtered by EObjectType constant.'
		ret = self._oleobj_.InvokeTypes(1610809347, LCID, 2, (9, 0), ((3, 49),),p_eObjectType
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjects', '{44747797-9642-483B-AB9C-6AE0A1899549}')
		return ret

	def IsDefault(self):
		'Returns true if the object is default and cannot be deleted.'
		return self._oleobj_.InvokeTypes(1610743811, LCID, 1, (11, 0), (),)

	def IsValid(self):
		'Returns true if the object is still valid.'
		return self._oleobj_.InvokeTypes(1610743810, LCID, 1, (11, 0), (),)

	def Rename(self, p_strName=defaultNamedNotOptArg):
		'Changes the name of the object.'
		return self._oleobj_.InvokeTypes(1610874882, LCID, 1, (24, 0), ((8, 1),),p_strName
			)

	_prop_map_get_ = {
		# Method 'Comments' returns object of type 'ICommentsMutable'
		"Comments": (1610809346, 2, (9, 0), (), "Comments", '{23FAC1D8-2578-42BC-9F65-F04930FB6489}'),
		# Method 'Constraints' returns object of type 'IConstraintsMutable'
		"Constraints": (1610809345, 2, (9, 0), ((3, 49),), "Constraints", '{1DDEC891-7D43-4EE9-9BD4-63772C577150}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
		"ObjectType": (1610809344, 2, (3, 0), (), "ObjectType", None),
		# Method 'Objects' returns object of type 'IObjects'
		"Objects": (1610809347, 2, (9, 0), ((3, 49),), "Objects", '{44747797-9642-483B-AB9C-6AE0A1899549}'),
		# Method 'Parent' returns object of type 'IObject'
		"Parent": (1610743809, 2, (9, 0), (), "Parent", '{7A5D1A08-B723-4929-BB46-A801DC642EB6}'),
		"Value": (1610874880, 2, (8, 0), (), "Value", None),
	}
	_prop_map_put_ = {
		"Value": ((1610874880, LCID, 4, 0),()),
	}

	Comments: str # ICommentsMutable; read_only
	Constraints: str # IConstraintsMutable; read_only
	Name: str # read_only
	ObjectType: str # read_only
	Objects: str # IObjects; read_only
	Parent: str # IObject; read_only
	Value: str # read/write

	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
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

class IConstants(DispatchBaseClass):
	CLSID = IID('{F5D6BDC5-5DB8-4F47-AC16-CABDF8BE0437}')
	coclass_clsid = IID('{52504AB6-DF45-424B-A06A-B4F29C000667}')

	# Result is of type IConstant
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the constant of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{E43EED65-B104-4518-A7C0-21C3FA01B4F5}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the constant of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{E43EED65-B104-4518-A7C0-21C3FA01B4F5}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{E43EED65-B104-4518-A7C0-21C3FA01B4F5}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IConstantsMutable(DispatchBaseClass):
	CLSID = IID('{3C22162A-1920-4AF1-B2BA-805CC3A2500C}')
	coclass_clsid = IID('{2FC31295-E0FE-453B-AE2D-1BD5726CE291}')

	# Result is of type IConstant
	def Add(self, p_strName=defaultNamedNotOptArg, p_strValue=defaultNamedNotOptArg):
		'Creates the constant of the given name and value, and adds it to the collection.'
		ret = self._oleobj_.InvokeTypes(1610874880, LCID, 1, (9, 0), ((8, 1), (8, 1)),p_strName
			, p_strValue)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{E43EED65-B104-4518-A7C0-21C3FA01B4F5}')
		return ret

	def Delete(self, p_vIndex=defaultNamedNotOptArg):
		'Deletes the constant of the given index or name and removes it from the collection.'
		return self._oleobj_.InvokeTypes(1610874881, LCID, 1, (24, 0), ((12, 1),),p_vIndex
			)

	# Result is of type IConstant
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the constant of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{E43EED65-B104-4518-A7C0-21C3FA01B4F5}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the constant of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{E43EED65-B104-4518-A7C0-21C3FA01B4F5}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{E43EED65-B104-4518-A7C0-21C3FA01B4F5}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IConstraint(DispatchBaseClass):
	CLSID = IID('{7C5585B1-767E-47E1-8BC9-F4564CA62236}')
	coclass_clsid = IID('{D3A2A3F8-D4FC-453F-9A69-CF8425497168}')

	def IsDefault(self):
		'Returns true if the object is default and cannot be deleted.'
		return self._oleobj_.InvokeTypes(1610743811, LCID, 1, (11, 0), (),)

	def IsReadOnly(self):
		'Returns true if the constraint cannot be modified.'
		return self._oleobj_.InvokeTypes(1610809348, LCID, 1, (11, 0), (),)

	def IsValid(self):
		'Returns true if the object is still valid.'
		return self._oleobj_.InvokeTypes(1610743810, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"ConstraintType": (1610809344, 2, (3, 0), (), "ConstraintType", None),
		"Name": (0, 2, (8, 0), (), "Name", None),
		# Method 'Parent' returns object of type 'IObject'
		"Parent": (1610743809, 2, (9, 0), (), "Parent", '{7A5D1A08-B723-4929-BB46-A801DC642EB6}'),
		"Value": (1610809345, 2, (12, 0), (), "Value", None),
		"ValueString": (1610809347, 2, (8, 0), (), "ValueString", None),
	}
	_prop_map_put_ = {
		"Value": ((1610809345, LCID, 4, 0),()),
	}

	ConstraintType: str # read_only
	Name: str # read_only
	Parent: str # IObject; read_only
	Value: str # read/write
	ValueString: str # read_only

	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
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

class IConstraintClass(DispatchBaseClass):
	CLSID = IID('{CB59FE57-0379-43C2-86FF-E6E0D31CBAB9}')
	coclass_clsid = IID('{032414B7-8F46-402E-B8B1-D834CF6FB083}')

	def AssignNet(self, p_pNet=defaultNamedNotOptArg):
		'Assigns the given net to the class.'
		return self._oleobj_.InvokeTypes(1610874883, LCID, 1, (24, 0), ((9, 1),),p_pNet
			)

	# Result is of type IConstraintClassesMutable
	# The method GetConstraintClasses is actually a property, but must be used as a method to correctly pass the arguments
	def GetConstraintClasses(self, p_nConstraintClassMask=2):
		'Returns the collection of child constraint classes, filtered by EObjectMask constant.'
		ret = self._oleobj_.InvokeTypes(1610940420, LCID, 2, (9, 0), ((3, 49),),p_nConstraintClassMask
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetConstraintClasses', '{E4076B8B-3F93-407C-8E18-9DD473F3C4B6}')
		return ret

	# Result is of type IConstraintsMutable
	# The method GetConstraints is actually a property, but must be used as a method to correctly pass the arguments
	def GetConstraints(self, p_nConstraintMask=7):
		'Returns the collection of constraints, filtered by EConstraintMask constant.'
		ret = self._oleobj_.InvokeTypes(1610809345, LCID, 2, (9, 0), ((3, 49),),p_nConstraintMask
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetConstraints', '{1DDEC891-7D43-4EE9-9BD4-63772C577150}')
		return ret

	# Result is of type INets
	# The method GetNets is actually a property, but must be used as a method to correctly pass the arguments
	def GetNets(self, p_nNetMask=1):
		'Returns the collection of nets assigned to the class, filtered by ENetMask constant.'
		ret = self._oleobj_.InvokeTypes(1610874881, LCID, 2, (9, 0), ((3, 49),),p_nNetMask
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetNets', '{EAF633E9-E21E-47FF-A361-60A4B480301F}')
		return ret

	# Result is of type IObjects
	# The method GetObjects is actually a property, but must be used as a method to correctly pass the arguments
	def GetObjects(self, p_eObjectType=0):
		'Returns the collection of child objects, filtered by EObjectType constant.'
		ret = self._oleobj_.InvokeTypes(1610809347, LCID, 2, (9, 0), ((3, 49),),p_eObjectType
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjects', '{44747797-9642-483B-AB9C-6AE0A1899549}')
		return ret

	def IsDefault(self):
		'Returns true if the object is default and cannot be deleted.'
		return self._oleobj_.InvokeTypes(1610743811, LCID, 1, (11, 0), (),)

	def IsValid(self):
		'Returns true if the object is still valid.'
		return self._oleobj_.InvokeTypes(1610743810, LCID, 1, (11, 0), (),)

	def MoveTo(self, p_pParentConstraintClass=defaultNamedNotOptArg):
		'Changes the parent of the constraint class. Set to Null for the root constraint class.'
		return self._oleobj_.InvokeTypes(1610940422, LCID, 1, (24, 0), ((9, 1),),p_pParentConstraintClass
			)

	def Rename(self, p_strName=defaultNamedNotOptArg):
		'Changes the name of the object.'
		return self._oleobj_.InvokeTypes(1610874882, LCID, 1, (24, 0), ((8, 1),),p_strName
			)

	_prop_map_get_ = {
		# Method 'Comments' returns object of type 'ICommentsMutable'
		"Comments": (1610809346, 2, (9, 0), (), "Comments", '{23FAC1D8-2578-42BC-9F65-F04930FB6489}'),
		# Method 'ConstraintClasses' returns object of type 'IConstraintClassesMutable'
		"ConstraintClasses": (1610940420, 2, (9, 0), ((3, 49),), "ConstraintClasses", '{E4076B8B-3F93-407C-8E18-9DD473F3C4B6}'),
		# Method 'Constraints' returns object of type 'IConstraintsMutable'
		"Constraints": (1610809345, 2, (9, 0), ((3, 49),), "Constraints", '{1DDEC891-7D43-4EE9-9BD4-63772C577150}'),
		"DelayType": (1610940416, 2, (3, 0), (), "DelayType", None),
		# Method 'DisplayPattern' returns object of type 'IDisplayPattern'
		"DisplayPattern": (1610874884, 2, (9, 0), (), "DisplayPattern", '{E6F44CAC-B61D-4437-971F-60F01875D6BB}'),
		"FullName": (1610874880, 2, (8, 0), (), "FullName", None),
		"Name": (0, 2, (8, 0), (), "Name", None),
		# Method 'NetClass' returns object of type 'INetClass'
		"NetClass": (1610940421, 2, (9, 0), (), "NetClass", '{791A98C5-512E-45E0-8F4F-715A45F5707A}'),
		# Method 'Nets' returns object of type 'INets'
		"Nets": (1610874881, 2, (9, 0), ((3, 49),), "Nets", '{EAF633E9-E21E-47FF-A361-60A4B480301F}'),
		# Method 'NoiseRules' returns object of type 'INoiseRules'
		"NoiseRules": (1610940423, 2, (9, 0), (), "NoiseRules", '{ED063FFC-209C-48D7-8D59-6677873C9A7A}'),
		"ObjectType": (1610809344, 2, (3, 0), (), "ObjectType", None),
		# Method 'Objects' returns object of type 'IObjects'
		"Objects": (1610809347, 2, (9, 0), ((3, 49),), "Objects", '{44747797-9642-483B-AB9C-6AE0A1899549}'),
		# Method 'Parent' returns object of type 'IObject'
		"Parent": (1610743809, 2, (9, 0), (), "Parent", '{7A5D1A08-B723-4929-BB46-A801DC642EB6}'),
		"TopologyType": (1610940418, 2, (3, 0), (), "TopologyType", None),
	}
	_prop_map_put_ = {
		"DelayType": ((1610940416, LCID, 4, 0),()),
		"TopologyType": ((1610940418, LCID, 4, 0),()),
	}

	Comments: str # ICommentsMutable; read_only
	ConstraintClasses: str # IConstraintClassesMutable; read_only
	Constraints: str # IConstraintsMutable; read_only
	DelayType: str # read/write
	DisplayPattern: str # IDisplayPattern; read_only
	FullName: str # read_only
	Name: str # read_only
	NetClass: str # INetClass; read_only
	Nets: str # INets; read_only
	NoiseRules: str # INoiseRules; read_only
	ObjectType: str # read_only
	Objects: str # IObjects; read_only
	Parent: str # IObject; read_only
	TopologyType: str # read/write

	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
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

class IConstraintClasses(DispatchBaseClass):
	CLSID = IID('{7D9A71CB-B02F-4A1B-9995-2ADF58C69494}')
	coclass_clsid = IID('{3BC701EA-8962-401F-8213-9782C2A5471F}')

	# Result is of type IConstraintClass
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the constraint class of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{CB59FE57-0379-43C2-86FF-E6E0D31CBAB9}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the constraint class of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{CB59FE57-0379-43C2-86FF-E6E0D31CBAB9}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{CB59FE57-0379-43C2-86FF-E6E0D31CBAB9}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IConstraintClassesMutable(DispatchBaseClass):
	CLSID = IID('{E4076B8B-3F93-407C-8E18-9DD473F3C4B6}')
	coclass_clsid = IID('{06CEF5AA-5BDB-4B33-8BBA-7E6A0E108A1B}')

	# Result is of type IConstraintClass
	def Add(self, p_strName=defaultNamedNotOptArg):
		'Creates the constraint class of the given name and adds it to the collection.'
		ret = self._oleobj_.InvokeTypes(1610874880, LCID, 1, (9, 0), ((8, 1),),p_strName
			)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{CB59FE57-0379-43C2-86FF-E6E0D31CBAB9}')
		return ret

	def Delete(self, p_vIndex=defaultNamedNotOptArg):
		'Deletes the constraint class of the given index or name and removes it from the collection.'
		return self._oleobj_.InvokeTypes(1610874883, LCID, 1, (24, 0), ((12, 1),),p_vIndex
			)

	def Insert(self, p_pConstraintClass=defaultNamedNotOptArg):
		'Inserts the constraint class to the collection.'
		return self._oleobj_.InvokeTypes(1610874881, LCID, 1, (24, 0), ((9, 1),),p_pConstraintClass
			)

	# Result is of type IConstraintClass
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the constraint class of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{CB59FE57-0379-43C2-86FF-E6E0D31CBAB9}')
		return ret

	def Remove(self, p_vIndex=defaultNamedNotOptArg):
		'Removes the constraint class of the given index or name from the collection.'
		return self._oleobj_.InvokeTypes(1610874882, LCID, 1, (24, 0), ((12, 1),),p_vIndex
			)

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the constraint class of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{CB59FE57-0379-43C2-86FF-E6E0D31CBAB9}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{CB59FE57-0379-43C2-86FF-E6E0D31CBAB9}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IConstraints(DispatchBaseClass):
	CLSID = IID('{75C541D3-DD34-4A0C-9BAA-91155454CAD5}')
	coclass_clsid = IID('{25937434-EBF2-42A3-B4C8-2EC32F4DEE6E}')

	# Result is of type IConstraint
	def FindItem(self, p_eType=defaultNamedNotOptArg):
		'Finds the constraint of the given constraint type.'
		ret = self._oleobj_.InvokeTypes(1610809345, LCID, 1, (9, 0), ((3, 1),),p_eType
			)
		if ret is not None:
			ret = Dispatch(ret, 'FindItem', '{7C5585B1-767E-47E1-8BC9-F4564CA62236}')
		return ret

	# Result is of type IConstraint
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the constraint of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{7C5585B1-767E-47E1-8BC9-F4564CA62236}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the constraint of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{7C5585B1-767E-47E1-8BC9-F4564CA62236}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{7C5585B1-767E-47E1-8BC9-F4564CA62236}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IConstraintsAuto(DispatchBaseClass):
	CLSID = IID('{8B0AE548-6CF5-1014-9B55-8BB0EECCF0AC}')
	coclass_clsid = IID('{8B0AE687-6CF5-1014-9B55-8BB0EECCF0AC}')

	def Validate(self, p_dSeed=defaultNamedNotOptArg):
		'Validates the license for the automation. Specify 0 for the license seed to get a key.'
		return self._oleobj_.InvokeTypes(1610743810, LCID, 1, (3, 0), ((3, 1),),p_dSeed
			)

	_prop_map_get_ = {
		# Method 'Design' returns object of type 'IDesign'
		"Design": (1610743808, 2, (9, 0), (), "Design", '{416A557D-9764-45C2-B656-BC53A72B6DDC}'),
		# Method 'Settings' returns object of type 'ISettings'
		"Settings": (1610743809, 2, (9, 0), (), "Settings", '{8D9E96B8-678C-4EC9-93EE-F7E4CEC025FB}'),
	}
	_prop_map_put_ = {
	}

	Design: str # IDesign; read_only
	Settings: str # ISettings; read_only

	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IConstraintsMutable(DispatchBaseClass):
	CLSID = IID('{1DDEC891-7D43-4EE9-9BD4-63772C577150}')
	coclass_clsid = IID('{211695E1-560F-41E3-8125-5C41B4A1131B}')

	# Result is of type IConstraint
	def Add(self, p_strName=defaultNamedNotOptArg, p_vValue=defaultNamedNotOptArg):
		'Creates the constraint of the given name and value, and adds it to the collection.'
		ret = self._oleobj_.InvokeTypes(1610874880, LCID, 1, (9, 0), ((8, 1), (12, 1)),p_strName
			, p_vValue)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{7C5585B1-767E-47E1-8BC9-F4564CA62236}')
		return ret

	# Result is of type IConstraint
	def AddByType(self, p_eType=defaultNamedNotOptArg, p_vValue=defaultNamedNotOptArg):
		'Creates the constraint of the given constraint type and value, and adds it to the collection.'
		ret = self._oleobj_.InvokeTypes(1610874881, LCID, 1, (9, 0), ((3, 1), (12, 1)),p_eType
			, p_vValue)
		if ret is not None:
			ret = Dispatch(ret, 'AddByType', '{7C5585B1-767E-47E1-8BC9-F4564CA62236}')
		return ret

	def Delete(self, p_vIndex=defaultNamedNotOptArg):
		'Deletes the constraint of the given index or name and removes it from the collection.'
		return self._oleobj_.InvokeTypes(1610874882, LCID, 1, (24, 0), ((12, 1),),p_vIndex
			)

	def DeleteByType(self, p_eType=defaultNamedNotOptArg):
		'Deletes the constraint of the given constraint type and removes it from the collection.'
		return self._oleobj_.InvokeTypes(1610874883, LCID, 1, (24, 0), ((3, 1),),p_eType
			)

	# Result is of type IConstraint
	def FindItem(self, p_eType=defaultNamedNotOptArg):
		'Finds the constraint of the given constraint type.'
		ret = self._oleobj_.InvokeTypes(1610809345, LCID, 1, (9, 0), ((3, 1),),p_eType
			)
		if ret is not None:
			ret = Dispatch(ret, 'FindItem', '{7C5585B1-767E-47E1-8BC9-F4564CA62236}')
		return ret

	# Result is of type IConstraint
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the constraint of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{7C5585B1-767E-47E1-8BC9-F4564CA62236}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the constraint of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{7C5585B1-767E-47E1-8BC9-F4564CA62236}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{7C5585B1-767E-47E1-8BC9-F4564CA62236}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IDRC(DispatchBaseClass):
	CLSID = IID('{D9FEE0D7-B9FE-41C9-9FCF-6597EDC8E2AF}')
	coclass_clsid = IID('{644E0684-E131-45ED-A4B3-A76EC1D5B33E}')

	_prop_map_get_ = {
		"Description": (1610743809, 2, (8, 0), (), "Description", None),
		"Status": (0, 2, (3, 0), (), "Status", None),
	}
	_prop_map_put_ = {
	}

	Description: str # read_only
	Status: str # read_only

	# Default property for this class is 'Status'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (3, 0), (), "Status", None))
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

class IDesign(DispatchBaseClass):
	CLSID = IID('{416A557D-9764-45C2-B656-BC53A72B6DDC}')
	coclass_clsid = IID('{BD801DC8-79E4-45DE-ADB7-45E7918DF499}')

	# Result is of type IDesignParams
	def CreateDesignParams(self):
		'Creates and returns the design parameters object. This object is used for specifying design parameters like path or context.'
		ret = self._oleobj_.InvokeTypes(1610743808, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'CreateDesignParams', '{3CD8028B-F3A2-4077-8F4F-83A89F4DD990}')
		return ret

	# Result is of type IConstraintClassesMutable
	# The method GetConstraintClasses is actually a property, but must be used as a method to correctly pass the arguments
	def GetConstraintClasses(self, p_nConstraintClassMask=2):
		'Returns the collection of constraint classes, filtered by EObjectMask constant.'
		ret = self._oleobj_.InvokeTypes(1610743815, LCID, 2, (9, 0), ((3, 49),),p_nConstraintClassMask
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetConstraintClasses', '{E4076B8B-3F93-407C-8E18-9DD473F3C4B6}')
		return ret

	# Result is of type IMatchGroupsMutable
	# The method GetMatchGroups is actually a property, but must be used as a method to correctly pass the arguments
	def GetMatchGroups(self, p_nMatchGroupMask=3):
		'Returns the collection of match groups, filtered by EMatchGroupMask constant.'
		ret = self._oleobj_.InvokeTypes(1610743818, LCID, 2, (9, 0), ((3, 49),),p_nMatchGroupMask
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetMatchGroups', '{F36348AB-8180-41C3-951F-0B079E3FF03F}')
		return ret

	# Result is of type INetClassesMutable
	# The method GetNetClasses is actually a property, but must be used as a method to correctly pass the arguments
	def GetNetClasses(self, p_nNetClassMask=2):
		'Returns the collection of net classes, filtered by EObjectMask constant.'
		ret = self._oleobj_.InvokeTypes(1610743816, LCID, 2, (9, 0), ((3, 49),),p_nNetClassMask
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetNetClasses', '{DAA15140-C478-41AE-90D4-8782BA3A8707}')
		return ret

	# Result is of type INetsMutable
	# The method GetNets is actually a property, but must be used as a method to correctly pass the arguments
	def GetNets(self, p_nNetMask=1):
		'Returns the collection of nets, filtered by ENetMask constant.'
		ret = self._oleobj_.InvokeTypes(1610743811, LCID, 2, (9, 0), ((3, 49),),p_nNetMask
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetNets', '{17F8541C-BB01-40FC-AAFD-179AA166F42D}')
		return ret

	# Result is of type INoiseRulesMutable
	# The method GetNoiseRules is actually a property, but must be used as a method to correctly pass the arguments
	def GetNoiseRules(self, p_nNoiseRuleMask=3):
		'Returns the collection of noise rules, filtered by ENoiseRuleMask constant.'
		ret = self._oleobj_.InvokeTypes(1610743820, LCID, 2, (9, 0), ((3, 49),),p_nNoiseRuleMask
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetNoiseRules', '{D07554EB-FCFF-48EC-AD04-C79988D20C9D}')
		return ret

	def Load(self, p_pDesignParams=defaultNamedNotOptArg):
		'Loads the design specified by the DesignParams object.'
		return self._oleobj_.InvokeTypes(1610743809, LCID, 1, (24, 0), ((9, 1),),p_pDesignParams
			)

	def UnLoad(self):
		'Unloads the current design. Call this method before loading a different design.'
		return self._oleobj_.InvokeTypes(1610743810, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'ClearanceRules' returns object of type 'IClearanceRulesMutable'
		"ClearanceRules": (1610743817, 2, (9, 0), (), "ClearanceRules", '{088425F1-88A0-4675-B9B9-D6FBC0454CF3}'),
		# Method 'Components' returns object of type 'IComponentsMutable'
		"Components": (1610743822, 2, (9, 0), (), "Components", '{E010B178-C036-4BDE-815F-9B48CE213D1E}'),
		# Method 'Constants' returns object of type 'IConstantsMutable'
		"Constants": (1610743824, 2, (9, 0), (), "Constants", '{3C22162A-1920-4AF1-B2BA-805CC3A2500C}'),
		# Method 'ConstraintClasses' returns object of type 'IConstraintClassesMutable'
		"ConstraintClasses": (1610743815, 2, (9, 0), ((3, 49),), "ConstraintClasses", '{E4076B8B-3F93-407C-8E18-9DD473F3C4B6}'),
		# Method 'DifferentialPairs' returns object of type 'IDifferentialPairsMutable'
		"DifferentialPairs": (1610743814, 2, (9, 0), (), "DifferentialPairs", '{7E649A6C-5038-4FD1-94D9-44A56CAC894E}'),
		# Method 'DisplayPatterns' returns object of type 'IDisplayPatternsMutable'
		"DisplayPatterns": (1610743828, 2, (9, 0), (), "DisplayPatterns", '{209DB434-B7A4-4CF7-A1DC-87CFD2B21543}'),
		# Method 'ElectricalNets' returns object of type 'IElectricalNetsMutable'
		"ElectricalNets": (1610743812, 2, (9, 0), (), "ElectricalNets", '{6F698C72-5BBF-4DEE-A09C-065A7AB68829}'),
		# Method 'Formulas' returns object of type 'IFormulasMutable'
		"Formulas": (1610743819, 2, (9, 0), (), "Formulas", '{AF4369BD-BEF9-48A7-849A-F39065467C85}'),
		# Method 'MatchGroups' returns object of type 'IMatchGroupsMutable'
		"MatchGroups": (1610743818, 2, (9, 0), ((3, 49),), "MatchGroups", '{F36348AB-8180-41C3-951F-0B079E3FF03F}'),
		# Method 'NetClasses' returns object of type 'INetClassesMutable'
		"NetClasses": (1610743816, 2, (9, 0), ((3, 49),), "NetClasses", '{DAA15140-C478-41AE-90D4-8782BA3A8707}'),
		# Method 'Nets' returns object of type 'INetsMutable'
		"Nets": (1610743811, 2, (9, 0), ((3, 49),), "Nets", '{17F8541C-BB01-40FC-AAFD-179AA166F42D}'),
		# Method 'NoiseRules' returns object of type 'INoiseRulesMutable'
		"NoiseRules": (1610743820, 2, (9, 0), ((3, 49),), "NoiseRules", '{D07554EB-FCFF-48EC-AD04-C79988D20C9D}'),
		# Method 'PackageTypes' returns object of type 'IPackageTypesMutable'
		"PackageTypes": (1610743829, 2, (9, 0), (), "PackageTypes", '{EA65AC00-04E5-42F6-AC61-7FA81534926F}'),
		# Method 'ParallelismRules' returns object of type 'IParallelismRulesMutable'
		"ParallelismRules": (1610743821, 2, (9, 0), (), "ParallelismRules", '{E37D92BA-6E24-45E0-859C-43A40855C3AD}'),
		# Method 'Parts' returns object of type 'IPartsMutable'
		"Parts": (1610743823, 2, (9, 0), (), "Parts", '{965F3ED3-C357-4CD4-8778-9B61B12D5D24}'),
		# Method 'PhysicalRules' returns object of type 'IPhysicalRules'
		"PhysicalRules": (1610743827, 2, (9, 0), (), "PhysicalRules", '{F1F96334-F630-42BA-A3F4-2D314D51D535}'),
		# Method 'PowerNets' returns object of type 'IPowerNetsMutable'
		"PowerNets": (1610743813, 2, (9, 0), (), "PowerNets", '{B224A038-B04A-47E1-8F9F-C7938C61FD68}'),
		# Method 'Stackup' returns object of type 'IStackup'
		"Stackup": (1610743826, 2, (9, 0), (), "Stackup", '{FBFDBD21-1B6F-4263-A285-6FB6E9C7747F}'),
		# Method 'Variables' returns object of type 'IVariablesMutable'
		"Variables": (1610743825, 2, (9, 0), (), "Variables", '{9B803C91-3B87-4F74-810E-C038E63376B7}'),
	}
	_prop_map_put_ = {
	}

	ClearanceRules: str # IClearanceRulesMutable; read_only
	Components: str # IComponentsMutable; read_only
	Constants: str # IConstantsMutable; read_only
	ConstraintClasses: str # IConstraintClassesMutable; read_only
	DifferentialPairs: str # IDifferentialPairsMutable; read_only
	DisplayPatterns: str # IDisplayPatternsMutable; read_only
	ElectricalNets: str # IElectricalNetsMutable; read_only
	Formulas: str # IFormulasMutable; read_only
	MatchGroups: str # IMatchGroupsMutable; read_only
	NetClasses: str # INetClassesMutable; read_only
	Nets: str # INetsMutable; read_only
	NoiseRules: str # INoiseRulesMutable; read_only
	PackageTypes: str # IPackageTypesMutable; read_only
	ParallelismRules: str # IParallelismRulesMutable; read_only
	Parts: str # IPartsMutable; read_only
	PhysicalRules: str # IPhysicalRules; read_only
	PowerNets: str # IPowerNetsMutable; read_only
	Stackup: str # IStackup; read_only
	Variables: str # IVariablesMutable; read_only

	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IDesignParams(DispatchBaseClass):
	CLSID = IID('{3CD8028B-F3A2-4077-8F4F-83A89F4DD990}')
	coclass_clsid = IID('{E835C9C8-FC4E-417D-BD00-A948B4F66D20}')

	_prop_map_get_ = {
		"Board": (1610743812, 2, (8, 0), (), "Board", None),
		"DesignContext": (1610743810, 2, (3, 0), (), "DesignContext", None),
		"ProjectFile": (1610743808, 2, (8, 0), (), "ProjectFile", None),
	}
	_prop_map_put_ = {
		"Board": ((1610743812, LCID, 4, 0),()),
		"DesignContext": ((1610743810, LCID, 4, 0),()),
		"ProjectFile": ((1610743808, LCID, 4, 0),()),
	}

	Board: str # read/write
	DesignContext: str # read/write
	ProjectFile: str # read/write

	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IDifferentialPair(DispatchBaseClass):
	CLSID = IID('{90FF1694-9C25-4F12-A08B-999F24686B57}')
	coclass_clsid = IID('{04DE4486-51F4-4FB5-A1D2-DCB6CD97EF6C}')

	# Result is of type IConstraintsMutable
	# The method GetConstraints is actually a property, but must be used as a method to correctly pass the arguments
	def GetConstraints(self, p_nConstraintMask=7):
		'Returns the collection of constraints, filtered by EConstraintMask constant.'
		ret = self._oleobj_.InvokeTypes(1610809345, LCID, 2, (9, 0), ((3, 49),),p_nConstraintMask
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetConstraints', '{1DDEC891-7D43-4EE9-9BD4-63772C577150}')
		return ret

	# Result is of type IMatchGroups
	# The method GetMatchGroups is actually a property, but must be used as a method to correctly pass the arguments
	def GetMatchGroups(self, p_nMatchGroupMask=3):
		'Returns all match groups related to the net.'
		ret = self._oleobj_.InvokeTypes(1610874887, LCID, 2, (9, 0), ((3, 49),),p_nMatchGroupMask
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetMatchGroups', '{1F460B56-507F-4CA6-B8D7-676CBB2427BD}')
		return ret

	# Result is of type IObjects
	# The method GetObjects is actually a property, but must be used as a method to correctly pass the arguments
	def GetObjects(self, p_eObjectType=0):
		'Returns the collection of child objects, filtered by EObjectType constant.'
		ret = self._oleobj_.InvokeTypes(1610809347, LCID, 2, (9, 0), ((3, 49),),p_eObjectType
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjects', '{44747797-9642-483B-AB9C-6AE0A1899549}')
		return ret

	def IsDefault(self):
		'Returns true if the object is default and cannot be deleted.'
		return self._oleobj_.InvokeTypes(1610743811, LCID, 1, (11, 0), (),)

	def IsValid(self):
		'Returns true if the object is still valid.'
		return self._oleobj_.InvokeTypes(1610743810, LCID, 1, (11, 0), (),)

	def Rename(self, p_strName=defaultNamedNotOptArg):
		'Changes the name of the object.'
		return self._oleobj_.InvokeTypes(1610940419, LCID, 1, (24, 0), ((8, 1),),p_strName
			)

	_prop_map_get_ = {
		# Method 'Comments' returns object of type 'ICommentsMutable'
		"Comments": (1610809346, 2, (9, 0), (), "Comments", '{23FAC1D8-2578-42BC-9F65-F04930FB6489}'),
		# Method 'ConstraintClass' returns object of type 'IConstraintClass'
		"ConstraintClass": (1610874885, 2, (9, 0), (), "ConstraintClass", '{CB59FE57-0379-43C2-86FF-E6E0D31CBAB9}'),
		# Method 'Constraints' returns object of type 'IConstraintsMutable'
		"Constraints": (1610809345, 2, (9, 0), ((3, 49),), "Constraints", '{1DDEC891-7D43-4EE9-9BD4-63772C577150}'),
		"DelayType": (1610874882, 2, (3, 0), (), "DelayType", None),
		# Method 'DisplayPattern' returns object of type 'IDisplayPattern'
		"DisplayPattern": (1610874890, 2, (9, 0), (), "DisplayPattern", '{E6F44CAC-B61D-4437-971F-60F01875D6BB}'),
		# Method 'FirstNet' returns object of type 'INet'
		"FirstNet": (1610940416, 2, (9, 0), (), "FirstNet", '{48420240-E6BB-423E-9FD3-F3E4687E1452}'),
		# Method 'Formula' returns object of type 'IFormula'
		"Formula": (1610874888, 2, (9, 0), (), "Formula", '{A59586BA-4C99-4643-B6F8-E42BBF2E00D2}'),
		# Method 'MatchGroups' returns object of type 'IMatchGroups'
		"MatchGroups": (1610874887, 2, (9, 0), ((3, 49),), "MatchGroups", '{1F460B56-507F-4CA6-B8D7-676CBB2427BD}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
		# Method 'NetClass' returns object of type 'INetClass'
		"NetClass": (1610874886, 2, (9, 0), (), "NetClass", '{791A98C5-512E-45E0-8F4F-715A45F5707A}'),
		"NetType": (1610874880, 2, (3, 0), (), "NetType", None),
		# Method 'Nets' returns object of type 'INets'
		"Nets": (1610940418, 2, (9, 0), (), "Nets", '{EAF633E9-E21E-47FF-A361-60A4B480301F}'),
		# Method 'NoiseRules' returns object of type 'INoiseRules'
		"NoiseRules": (1610874889, 2, (9, 0), (), "NoiseRules", '{ED063FFC-209C-48D7-8D59-6677873C9A7A}'),
		"ObjectType": (1610809344, 2, (3, 0), (), "ObjectType", None),
		# Method 'Objects' returns object of type 'IObjects'
		"Objects": (1610809347, 2, (9, 0), ((3, 49),), "Objects", '{44747797-9642-483B-AB9C-6AE0A1899549}'),
		# Method 'Parent' returns object of type 'IObject'
		"Parent": (1610743809, 2, (9, 0), (), "Parent", '{7A5D1A08-B723-4929-BB46-A801DC642EB6}'),
		# Method 'SecondNet' returns object of type 'INet'
		"SecondNet": (1610940417, 2, (9, 0), (), "SecondNet", '{48420240-E6BB-423E-9FD3-F3E4687E1452}'),
		# Method 'Topology' returns object of type 'ITopology'
		"Topology": (1610874884, 2, (9, 0), (), "Topology", '{E827A25D-2BEB-4013-9E2B-035133E06025}'),
	}
	_prop_map_put_ = {
		"DelayType": ((1610874882, LCID, 4, 0),()),
		"NetType": ((1610874880, LCID, 4, 0),()),
	}

	Comments: str # ICommentsMutable; read_only
	ConstraintClass: str # IConstraintClass; read_only
	Constraints: str # IConstraintsMutable; read_only
	DelayType: str # read/write
	DisplayPattern: str # IDisplayPattern; read_only
	FirstNet: str # INet; read_only
	Formula: str # IFormula; read_only
	MatchGroups: str # IMatchGroups; read_only
	Name: str # read_only
	NetClass: str # INetClass; read_only
	NetType: str # read/write
	Nets: str # INets; read_only
	NoiseRules: str # INoiseRules; read_only
	ObjectType: str # read_only
	Objects: str # IObjects; read_only
	Parent: str # IObject; read_only
	SecondNet: str # INet; read_only
	Topology: str # ITopology; read_only

	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
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

class IDifferentialPairs(DispatchBaseClass):
	CLSID = IID('{3F1097CF-2AFC-4D0B-8477-FEA016F94987}')
	coclass_clsid = IID('{0E5A6F70-EA58-4E16-B16D-8B24785E5617}')

	# Result is of type IDifferentialPair
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the differential pair of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{90FF1694-9C25-4F12-A08B-999F24686B57}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the differential pair of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{90FF1694-9C25-4F12-A08B-999F24686B57}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{90FF1694-9C25-4F12-A08B-999F24686B57}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IDifferentialPairsMutable(DispatchBaseClass):
	CLSID = IID('{7E649A6C-5038-4FD1-94D9-44A56CAC894E}')
	coclass_clsid = IID('{B42E232E-C7ED-444C-81BC-4E88A3540DF3}')

	# Result is of type IDifferentialPair
	def Add(self, p_pNet1=defaultNamedNotOptArg, p_pNet2=defaultNamedNotOptArg):
		'Creates the differential pair of the two given nets and adds it to the collection.'
		ret = self._oleobj_.InvokeTypes(1610874880, LCID, 1, (9, 0), ((9, 1), (9, 1)),p_pNet1
			, p_pNet2)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{90FF1694-9C25-4F12-A08B-999F24686B57}')
		return ret

	def Delete(self, p_vIndex=defaultNamedNotOptArg):
		'Deletes the differential pair of the given index or name and removes it from the collection.'
		return self._oleobj_.InvokeTypes(1610874881, LCID, 1, (24, 0), ((12, 1),),p_vIndex
			)

	# Result is of type IDifferentialPair
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the differential pair of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{90FF1694-9C25-4F12-A08B-999F24686B57}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the differential pair of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{90FF1694-9C25-4F12-A08B-999F24686B57}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{90FF1694-9C25-4F12-A08B-999F24686B57}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IDisplayPattern(DispatchBaseClass):
	CLSID = IID('{E6F44CAC-B61D-4437-971F-60F01875D6BB}')
	coclass_clsid = IID('{8914D1F0-18EC-4E84-8CDA-F1598F99A228}')

	# Result is of type IConstraintsMutable
	# The method GetConstraints is actually a property, but must be used as a method to correctly pass the arguments
	def GetConstraints(self, p_nConstraintMask=7):
		'Returns the collection of constraints, filtered by EConstraintMask constant.'
		ret = self._oleobj_.InvokeTypes(1610809345, LCID, 2, (9, 0), ((3, 49),),p_nConstraintMask
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetConstraints', '{1DDEC891-7D43-4EE9-9BD4-63772C577150}')
		return ret

	# Result is of type INetsMutable
	# The method GetNets is actually a property, but must be used as a method to correctly pass the arguments
	def GetNets(self, p_nNetMask=1):
		'Returns the collection of nets associated with the display pattern, filtered by ENetMask constant.'
		ret = self._oleobj_.InvokeTypes(1610874880, LCID, 2, (9, 0), ((3, 49),),p_nNetMask
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetNets', '{17F8541C-BB01-40FC-AAFD-179AA166F42D}')
		return ret

	# Result is of type IObjects
	# The method GetObjects is actually a property, but must be used as a method to correctly pass the arguments
	def GetObjects(self, p_eObjectType=0):
		'Returns the collection of child objects, filtered by EObjectType constant.'
		ret = self._oleobj_.InvokeTypes(1610809347, LCID, 2, (9, 0), ((3, 49),),p_eObjectType
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjects', '{44747797-9642-483B-AB9C-6AE0A1899549}')
		return ret

	def IsDefault(self):
		'Returns true if the object is default and cannot be deleted.'
		return self._oleobj_.InvokeTypes(1610743811, LCID, 1, (11, 0), (),)

	def IsValid(self):
		'Returns true if the object is still valid.'
		return self._oleobj_.InvokeTypes(1610743810, LCID, 1, (11, 0), (),)

	def Rename(self, p_strName=defaultNamedNotOptArg):
		'Changes the name of the object.'
		return self._oleobj_.InvokeTypes(1610874883, LCID, 1, (24, 0), ((8, 1),),p_strName
			)

	_prop_map_get_ = {
		# Method 'Comments' returns object of type 'ICommentsMutable'
		"Comments": (1610809346, 2, (9, 0), (), "Comments", '{23FAC1D8-2578-42BC-9F65-F04930FB6489}'),
		# Method 'ConstraintClasses' returns object of type 'IConstraintClassesMutable'
		"ConstraintClasses": (1610874882, 2, (9, 0), (), "ConstraintClasses", '{E4076B8B-3F93-407C-8E18-9DD473F3C4B6}'),
		# Method 'Constraints' returns object of type 'IConstraintsMutable'
		"Constraints": (1610809345, 2, (9, 0), ((3, 49),), "Constraints", '{1DDEC891-7D43-4EE9-9BD4-63772C577150}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
		# Method 'NetClasses' returns object of type 'INetClassesMutable'
		"NetClasses": (1610874881, 2, (9, 0), (), "NetClasses", '{DAA15140-C478-41AE-90D4-8782BA3A8707}'),
		# Method 'Nets' returns object of type 'INetsMutable'
		"Nets": (1610874880, 2, (9, 0), ((3, 49),), "Nets", '{17F8541C-BB01-40FC-AAFD-179AA166F42D}'),
		"ObjectType": (1610809344, 2, (3, 0), (), "ObjectType", None),
		# Method 'Objects' returns object of type 'IObjects'
		"Objects": (1610809347, 2, (9, 0), ((3, 49),), "Objects", '{44747797-9642-483B-AB9C-6AE0A1899549}'),
		# Method 'Parent' returns object of type 'IObject'
		"Parent": (1610743809, 2, (9, 0), (), "Parent", '{7A5D1A08-B723-4929-BB46-A801DC642EB6}'),
	}
	_prop_map_put_ = {
	}

	Comments: str # ICommentsMutable; read_only
	ConstraintClasses: str # IConstraintClassesMutable; read_only
	Constraints: str # IConstraintsMutable; read_only
	Name: str # read_only
	NetClasses: str # INetClassesMutable; read_only
	Nets: str # INetsMutable; read_only
	ObjectType: str # read_only
	Objects: str # IObjects; read_only
	Parent: str # IObject; read_only

	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
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

class IDisplayPatterns(DispatchBaseClass):
	CLSID = IID('{D47DF953-026D-440D-819D-2DE548AD17C4}')
	coclass_clsid = IID('{078B323D-5BB7-4C07-92CF-9F3C48ED98B5}')

	# Result is of type IDisplayPattern
	def FindItem(self, p_vColor=defaultNamedNotOptArg, p_vPatternIndex=1, p_bPatternOutline=True, p_vPatternTransparency=100
			, p_bPatternTransparent=False):
		'Returns the display pattern of the given parameters.'
		ret = self._oleobj_.InvokeTypes(1610809345, LCID, 1, (9, 0), ((12, 1), (12, 49), (11, 49), (12, 49), (11, 49)),p_vColor
			, p_vPatternIndex, p_bPatternOutline, p_vPatternTransparency, p_bPatternTransparent)
		if ret is not None:
			ret = Dispatch(ret, 'FindItem', '{E6F44CAC-B61D-4437-971F-60F01875D6BB}')
		return ret

	# Result is of type IDisplayPattern
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the display pattern of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{E6F44CAC-B61D-4437-971F-60F01875D6BB}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the display pattern of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{E6F44CAC-B61D-4437-971F-60F01875D6BB}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{E6F44CAC-B61D-4437-971F-60F01875D6BB}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IDisplayPatternsMutable(DispatchBaseClass):
	CLSID = IID('{209DB434-B7A4-4CF7-A1DC-87CFD2B21543}')
	coclass_clsid = IID('{4415B5A1-315A-4D3E-91C9-898489133B66}')

	# Result is of type IDisplayPattern
	def Add(self, p_strName=defaultNamedNotOptArg, p_vColor=defaultNamedNotOptArg, p_vPatternIndex=1, p_bPatternOutline=True
			, p_vPatternTransparency=100, p_bPatternTransparent=False):
		'Creates the display pattern and adds it to the collection.'
		ret = self._oleobj_.InvokeTypes(1610874880, LCID, 1, (9, 0), ((8, 1), (12, 1), (12, 49), (11, 49), (12, 49), (11, 49)),p_strName
			, p_vColor, p_vPatternIndex, p_bPatternOutline, p_vPatternTransparency, p_bPatternTransparent
			)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{E6F44CAC-B61D-4437-971F-60F01875D6BB}')
		return ret

	def Delete(self, p_vIndex=defaultNamedNotOptArg):
		'Deletes the display pattern of the given index or name and removes it from the collection.'
		return self._oleobj_.InvokeTypes(1610874881, LCID, 1, (24, 0), ((12, 1),),p_vIndex
			)

	# Result is of type IDisplayPattern
	def FindItem(self, p_vColor=defaultNamedNotOptArg, p_vPatternIndex=1, p_bPatternOutline=True, p_vPatternTransparency=100
			, p_bPatternTransparent=False):
		'Returns the display pattern of the given parameters.'
		ret = self._oleobj_.InvokeTypes(1610809345, LCID, 1, (9, 0), ((12, 1), (12, 49), (11, 49), (12, 49), (11, 49)),p_vColor
			, p_vPatternIndex, p_bPatternOutline, p_vPatternTransparency, p_bPatternTransparent)
		if ret is not None:
			ret = Dispatch(ret, 'FindItem', '{E6F44CAC-B61D-4437-971F-60F01875D6BB}')
		return ret

	# Result is of type IDisplayPattern
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the display pattern of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{E6F44CAC-B61D-4437-971F-60F01875D6BB}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the display pattern of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{E6F44CAC-B61D-4437-971F-60F01875D6BB}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{E6F44CAC-B61D-4437-971F-60F01875D6BB}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IElectricalNet(DispatchBaseClass):
	CLSID = IID('{7DB3D012-77AB-47DF-9C24-9A297A370AD0}')
	coclass_clsid = IID('{34AD93FA-589D-4CA9-B092-E60A1B16F627}')

	# Result is of type IConstraintsMutable
	# The method GetConstraints is actually a property, but must be used as a method to correctly pass the arguments
	def GetConstraints(self, p_nConstraintMask=7):
		'Returns the collection of constraints, filtered by EConstraintMask constant.'
		ret = self._oleobj_.InvokeTypes(1610809345, LCID, 2, (9, 0), ((3, 49),),p_nConstraintMask
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetConstraints', '{1DDEC891-7D43-4EE9-9BD4-63772C577150}')
		return ret

	# Result is of type IMatchGroups
	# The method GetMatchGroups is actually a property, but must be used as a method to correctly pass the arguments
	def GetMatchGroups(self, p_nMatchGroupMask=3):
		'Returns all match groups related to the net.'
		ret = self._oleobj_.InvokeTypes(1610874887, LCID, 2, (9, 0), ((3, 49),),p_nMatchGroupMask
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetMatchGroups', '{1F460B56-507F-4CA6-B8D7-676CBB2427BD}')
		return ret

	# Result is of type IObjects
	# The method GetObjects is actually a property, but must be used as a method to correctly pass the arguments
	def GetObjects(self, p_eObjectType=0):
		'Returns the collection of child objects, filtered by EObjectType constant.'
		ret = self._oleobj_.InvokeTypes(1610809347, LCID, 2, (9, 0), ((3, 49),),p_eObjectType
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjects', '{44747797-9642-483B-AB9C-6AE0A1899549}')
		return ret

	def IsDefault(self):
		'Returns true if the object is default and cannot be deleted.'
		return self._oleobj_.InvokeTypes(1610743811, LCID, 1, (11, 0), (),)

	def IsValid(self):
		'Returns true if the object is still valid.'
		return self._oleobj_.InvokeTypes(1610743810, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		# Method 'Comments' returns object of type 'ICommentsMutable'
		"Comments": (1610809346, 2, (9, 0), (), "Comments", '{23FAC1D8-2578-42BC-9F65-F04930FB6489}'),
		# Method 'ConstraintClass' returns object of type 'IConstraintClass'
		"ConstraintClass": (1610874885, 2, (9, 0), (), "ConstraintClass", '{CB59FE57-0379-43C2-86FF-E6E0D31CBAB9}'),
		# Method 'Constraints' returns object of type 'IConstraintsMutable'
		"Constraints": (1610809345, 2, (9, 0), ((3, 49),), "Constraints", '{1DDEC891-7D43-4EE9-9BD4-63772C577150}'),
		"DelayType": (1610874882, 2, (3, 0), (), "DelayType", None),
		# Method 'DisplayPattern' returns object of type 'IDisplayPattern'
		"DisplayPattern": (1610874890, 2, (9, 0), (), "DisplayPattern", '{E6F44CAC-B61D-4437-971F-60F01875D6BB}'),
		# Method 'Formula' returns object of type 'IFormula'
		"Formula": (1610874888, 2, (9, 0), (), "Formula", '{A59586BA-4C99-4643-B6F8-E42BBF2E00D2}'),
		# Method 'MatchGroups' returns object of type 'IMatchGroups'
		"MatchGroups": (1610874887, 2, (9, 0), ((3, 49),), "MatchGroups", '{1F460B56-507F-4CA6-B8D7-676CBB2427BD}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
		# Method 'NetClass' returns object of type 'INetClass'
		"NetClass": (1610874886, 2, (9, 0), (), "NetClass", '{791A98C5-512E-45E0-8F4F-715A45F5707A}'),
		"NetType": (1610874880, 2, (3, 0), (), "NetType", None),
		# Method 'Nets' returns object of type 'INets'
		"Nets": (1610940416, 2, (9, 0), (), "Nets", '{EAF633E9-E21E-47FF-A361-60A4B480301F}'),
		# Method 'NoiseRules' returns object of type 'INoiseRules'
		"NoiseRules": (1610874889, 2, (9, 0), (), "NoiseRules", '{ED063FFC-209C-48D7-8D59-6677873C9A7A}'),
		"ObjectType": (1610809344, 2, (3, 0), (), "ObjectType", None),
		# Method 'Objects' returns object of type 'IObjects'
		"Objects": (1610809347, 2, (9, 0), ((3, 49),), "Objects", '{44747797-9642-483B-AB9C-6AE0A1899549}'),
		# Method 'Parent' returns object of type 'IObject'
		"Parent": (1610743809, 2, (9, 0), (), "Parent", '{7A5D1A08-B723-4929-BB46-A801DC642EB6}'),
		# Method 'Topology' returns object of type 'ITopology'
		"Topology": (1610874884, 2, (9, 0), (), "Topology", '{E827A25D-2BEB-4013-9E2B-035133E06025}'),
	}
	_prop_map_put_ = {
		"DelayType": ((1610874882, LCID, 4, 0),()),
		"NetType": ((1610874880, LCID, 4, 0),()),
	}

	Comments: str # ICommentsMutable; read_only
	ConstraintClass: str # IConstraintClass; read_only
	Constraints: str # IConstraintsMutable; read_only
	DelayType: str # read/write
	DisplayPattern: str # IDisplayPattern; read_only
	Formula: str # IFormula; read_only
	MatchGroups: str # IMatchGroups; read_only
	Name: str # read_only
	NetClass: str # INetClass; read_only
	NetType: str # read/write
	Nets: str # INets; read_only
	NoiseRules: str # INoiseRules; read_only
	ObjectType: str # read_only
	Objects: str # IObjects; read_only
	Parent: str # IObject; read_only
	Topology: str # ITopology; read_only

	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
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

class IElectricalNets(DispatchBaseClass):
	CLSID = IID('{26EBA780-1293-4DF0-87B3-2F4113E178CB}')
	coclass_clsid = IID('{D29538F3-CD23-4FB3-ACDB-6489A2B9F6E9}')

	# Result is of type IElectricalNet
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the electrical net of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{7DB3D012-77AB-47DF-9C24-9A297A370AD0}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the electrical net of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{7DB3D012-77AB-47DF-9C24-9A297A370AD0}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{7DB3D012-77AB-47DF-9C24-9A297A370AD0}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IElectricalNetsMutable(DispatchBaseClass):
	CLSID = IID('{6F698C72-5BBF-4DEE-A09C-065A7AB68829}')
	coclass_clsid = IID('{511DF122-52DC-494E-B932-BC4DB9932B41}')

	# Result is of type IElectricalNet
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the electrical net of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{7DB3D012-77AB-47DF-9C24-9A297A370AD0}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the electrical net of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{7DB3D012-77AB-47DF-9C24-9A297A370AD0}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{7DB3D012-77AB-47DF-9C24-9A297A370AD0}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IFormula(DispatchBaseClass):
	CLSID = IID('{A59586BA-4C99-4643-B6F8-E42BBF2E00D2}')
	coclass_clsid = IID('{50FBC794-9C15-4AF8-82C3-DE231368AAFE}')

	def AddObject(self, p_pObject=defaultNamedNotOptArg):
		'Adds an object (i.e. net, pin pair, constant or variable) to the formula.'
		return self._oleobj_.InvokeTypes(1610874885, LCID, 1, (24, 0), ((9, 1),),p_pObject
			)

	def AddOperator(self, p_eOperator=defaultNamedNotOptArg):
		'Adds an operator to the formula.'
		return self._oleobj_.InvokeTypes(1610874887, LCID, 1, (24, 0), ((3, 1),),p_eOperator
			)

	def AddText(self, p_strText=defaultNamedNotOptArg):
		'Adds a text to the formula.'
		return self._oleobj_.InvokeTypes(1610874886, LCID, 1, (24, 0), ((8, 1),),p_strText
			)

	def Begin(self):
		'Begins the formula creation.'
		return self._oleobj_.InvokeTypes(1610874882, LCID, 1, (24, 0), (),)

	def Clear(self):
		'Clears the formula value.'
		return self._oleobj_.InvokeTypes(1610874888, LCID, 1, (24, 0), (),)

	def Commit(self):
		'Commits the changes in the formula.'
		return self._oleobj_.InvokeTypes(1610874883, LCID, 1, (24, 0), (),)

	# Result is of type IConstraintsMutable
	# The method GetConstraints is actually a property, but must be used as a method to correctly pass the arguments
	def GetConstraints(self, p_nConstraintMask=7):
		'Returns the collection of constraints, filtered by EConstraintMask constant.'
		ret = self._oleobj_.InvokeTypes(1610809345, LCID, 2, (9, 0), ((3, 49),),p_nConstraintMask
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetConstraints', '{1DDEC891-7D43-4EE9-9BD4-63772C577150}')
		return ret

	# Result is of type IObjects
	# The method GetObjects is actually a property, but must be used as a method to correctly pass the arguments
	def GetObjects(self, p_eObjectType=0):
		'Returns the collection of child objects, filtered by EObjectType constant.'
		ret = self._oleobj_.InvokeTypes(1610809347, LCID, 2, (9, 0), ((3, 49),),p_eObjectType
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjects', '{44747797-9642-483B-AB9C-6AE0A1899549}')
		return ret

	def IsDefault(self):
		'Returns true if the object is default and cannot be deleted.'
		return self._oleobj_.InvokeTypes(1610743811, LCID, 1, (11, 0), (),)

	def IsValid(self):
		'Returns true if the object is still valid.'
		return self._oleobj_.InvokeTypes(1610743810, LCID, 1, (11, 0), (),)

	def Rollback(self):
		'Discards the changes in the formula.'
		return self._oleobj_.InvokeTypes(1610874884, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Comments' returns object of type 'ICommentsMutable'
		"Comments": (1610809346, 2, (9, 0), (), "Comments", '{23FAC1D8-2578-42BC-9F65-F04930FB6489}'),
		# Method 'Constraints' returns object of type 'IConstraintsMutable'
		"Constraints": (1610809345, 2, (9, 0), ((3, 49),), "Constraints", '{1DDEC891-7D43-4EE9-9BD4-63772C577150}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
		"ObjectType": (1610809344, 2, (3, 0), (), "ObjectType", None),
		# Method 'Objects' returns object of type 'IObjects'
		"Objects": (1610809347, 2, (9, 0), ((3, 49),), "Objects", '{44747797-9642-483B-AB9C-6AE0A1899549}'),
		# Method 'Parent' returns object of type 'IObject'
		"Parent": (1610743809, 2, (9, 0), (), "Parent", '{7A5D1A08-B723-4929-BB46-A801DC642EB6}'),
		"Value": (1610874880, 2, (8, 0), (), "Value", None),
	}
	_prop_map_put_ = {
		"Value": ((1610874880, LCID, 4, 0),()),
	}

	Comments: str # ICommentsMutable; read_only
	Constraints: str # IConstraintsMutable; read_only
	Name: str # read_only
	ObjectType: str # read_only
	Objects: str # IObjects; read_only
	Parent: str # IObject; read_only
	Value: str # read/write

	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
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

class IFormulas(DispatchBaseClass):
	CLSID = IID('{7232F46D-2CFB-423B-927D-E8B1AA3B959A}')
	coclass_clsid = IID('{FC12916D-BCA2-44C7-8BA2-0469F29C2F99}')

	# Result is of type IFormula
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the formula of the given index.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{A59586BA-4C99-4643-B6F8-E42BBF2E00D2}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the formula of the given index.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{A59586BA-4C99-4643-B6F8-E42BBF2E00D2}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{A59586BA-4C99-4643-B6F8-E42BBF2E00D2}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IFormulasMutable(DispatchBaseClass):
	CLSID = IID('{AF4369BD-BEF9-48A7-849A-F39065467C85}')
	coclass_clsid = IID('{02C5D3D1-CD4B-49B9-A5A1-6D517184C8A3}')

	# Result is of type IFormula
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the formula of the given index.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{A59586BA-4C99-4643-B6F8-E42BBF2E00D2}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the formula of the given index.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{A59586BA-4C99-4643-B6F8-E42BBF2E00D2}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{A59586BA-4C99-4643-B6F8-E42BBF2E00D2}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IFromTo(DispatchBaseClass):
	CLSID = IID('{0DEB5A91-FF99-4B23-BAD2-4B5C2C84D5BF}')
	coclass_clsid = IID('{FDBE490D-01ED-4EF4-96DF-C4D1034AC95F}')

	# Result is of type IConstraintsMutable
	# The method GetConstraints is actually a property, but must be used as a method to correctly pass the arguments
	def GetConstraints(self, p_nConstraintMask=7):
		'Returns the collection of constraints, filtered by EConstraintMask constant.'
		ret = self._oleobj_.InvokeTypes(1610809345, LCID, 2, (9, 0), ((3, 49),),p_nConstraintMask
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetConstraints', '{1DDEC891-7D43-4EE9-9BD4-63772C577150}')
		return ret

	# Result is of type IObjects
	# The method GetObjects is actually a property, but must be used as a method to correctly pass the arguments
	def GetObjects(self, p_eObjectType=0):
		'Returns the collection of child objects, filtered by EObjectType constant.'
		ret = self._oleobj_.InvokeTypes(1610809347, LCID, 2, (9, 0), ((3, 49),),p_eObjectType
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjects', '{44747797-9642-483B-AB9C-6AE0A1899549}')
		return ret

	def IsDefault(self):
		'Returns true if the object is default and cannot be deleted.'
		return self._oleobj_.InvokeTypes(1610743811, LCID, 1, (11, 0), (),)

	def IsValid(self):
		'Returns true if the object is still valid.'
		return self._oleobj_.InvokeTypes(1610743810, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		# Method 'Comments' returns object of type 'ICommentsMutable'
		"Comments": (1610809346, 2, (9, 0), (), "Comments", '{23FAC1D8-2578-42BC-9F65-F04930FB6489}'),
		# Method 'Constraints' returns object of type 'IConstraintsMutable'
		"Constraints": (1610809345, 2, (9, 0), ((3, 49),), "Constraints", '{1DDEC891-7D43-4EE9-9BD4-63772C577150}'),
		# Method 'FirstPin' returns object of type 'IPin'
		"FirstPin": (1610874880, 2, (9, 0), (), "FirstPin", '{1B2620CF-90B0-4E6B-9CDF-A1799A578FDC}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
		"ObjectType": (1610809344, 2, (3, 0), (), "ObjectType", None),
		# Method 'Objects' returns object of type 'IObjects'
		"Objects": (1610809347, 2, (9, 0), ((3, 49),), "Objects", '{44747797-9642-483B-AB9C-6AE0A1899549}'),
		# Method 'Parent' returns object of type 'IObject'
		"Parent": (1610743809, 2, (9, 0), (), "Parent", '{7A5D1A08-B723-4929-BB46-A801DC642EB6}'),
		# Method 'Pins' returns object of type 'IPins'
		"Pins": (1610874882, 2, (9, 0), (), "Pins", '{3F1B4618-0423-42B9-A741-72E65CE0E573}'),
		# Method 'SecondPin' returns object of type 'IPin'
		"SecondPin": (1610874881, 2, (9, 0), (), "SecondPin", '{1B2620CF-90B0-4E6B-9CDF-A1799A578FDC}'),
	}
	_prop_map_put_ = {
	}

	Comments: str # ICommentsMutable; read_only
	Constraints: str # IConstraintsMutable; read_only
	FirstPin: str # IPin; read_only
	Name: str # read_only
	ObjectType: str # read_only
	Objects: str # IObjects; read_only
	Parent: str # IObject; read_only
	Pins: str # IPins; read_only
	SecondPin: str # IPin; read_only

	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
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

class IFromTos(DispatchBaseClass):
	CLSID = IID('{9C2F6146-F58D-43EC-B1B4-F0FF99B33E31}')
	coclass_clsid = IID('{661A1886-47C6-4BE7-B902-7D741CC216C5}')

	# Result is of type IFromTo
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the from-to of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{0DEB5A91-FF99-4B23-BAD2-4B5C2C84D5BF}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the from-to of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{0DEB5A91-FF99-4B23-BAD2-4B5C2C84D5BF}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{0DEB5A91-FF99-4B23-BAD2-4B5C2C84D5BF}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IFromTosMutable(DispatchBaseClass):
	CLSID = IID('{EE1AE409-4E07-44DC-8E8A-13B34E7FF81E}')
	coclass_clsid = IID('{3925DBCB-CE2E-4FA2-8BD8-D60CC27BF192}')

	# Result is of type IFromTo
	def Add(self, p_pPin1=defaultNamedNotOptArg, p_pPin2=defaultNamedNotOptArg):
		'Creates the from-to and adds it to the collection.'
		ret = self._oleobj_.InvokeTypes(1610874880, LCID, 1, (9, 0), ((9, 1), (9, 1)),p_pPin1
			, p_pPin2)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{0DEB5A91-FF99-4B23-BAD2-4B5C2C84D5BF}')
		return ret

	def Delete(self, p_vIndex=defaultNamedNotOptArg):
		'Deletes the from-to of the given index or name and removes it from the collection.'
		return self._oleobj_.InvokeTypes(1610874881, LCID, 1, (24, 0), ((12, 1),),p_vIndex
			)

	# Result is of type IFromTo
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the from-to of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{0DEB5A91-FF99-4B23-BAD2-4B5C2C84D5BF}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the from-to of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{0DEB5A91-FF99-4B23-BAD2-4B5C2C84D5BF}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{0DEB5A91-FF99-4B23-BAD2-4B5C2C84D5BF}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IGeneralClearance(DispatchBaseClass):
	CLSID = IID('{D7ABE808-2624-4912-B413-96F9E0B5BA5B}')
	coclass_clsid = IID('{AFF28CA8-1527-4C24-BD65-632849524714}')

	# Result is of type IConstraintsMutable
	# The method GetConstraints is actually a property, but must be used as a method to correctly pass the arguments
	def GetConstraints(self, p_nConstraintMask=7):
		'Returns the collection of constraints, filtered by EConstraintMask constant.'
		ret = self._oleobj_.InvokeTypes(1610809345, LCID, 2, (9, 0), ((3, 49),),p_nConstraintMask
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetConstraints', '{1DDEC891-7D43-4EE9-9BD4-63772C577150}')
		return ret

	# Result is of type IObjects
	# The method GetObjects is actually a property, but must be used as a method to correctly pass the arguments
	def GetObjects(self, p_eObjectType=0):
		'Returns the collection of child objects, filtered by EObjectType constant.'
		ret = self._oleobj_.InvokeTypes(1610809347, LCID, 2, (9, 0), ((3, 49),),p_eObjectType
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjects', '{44747797-9642-483B-AB9C-6AE0A1899549}')
		return ret

	def IsDefault(self):
		'Returns true if the object is default and cannot be deleted.'
		return self._oleobj_.InvokeTypes(1610743811, LCID, 1, (11, 0), (),)

	def IsValid(self):
		'Returns true if the object is still valid.'
		return self._oleobj_.InvokeTypes(1610743810, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"ClearanceType": (1610874881, 2, (3, 0), (), "ClearanceType", None),
		# Method 'Comments' returns object of type 'ICommentsMutable'
		"Comments": (1610809346, 2, (9, 0), (), "Comments", '{23FAC1D8-2578-42BC-9F65-F04930FB6489}'),
		# Method 'Constraints' returns object of type 'IConstraintsMutable'
		"Constraints": (1610809345, 2, (9, 0), ((3, 49),), "Constraints", '{1DDEC891-7D43-4EE9-9BD4-63772C577150}'),
		"GeneralClearanceType": (1610874880, 2, (3, 0), (), "GeneralClearanceType", None),
		"Name": (0, 2, (8, 0), (), "Name", None),
		"ObjectType": (1610809344, 2, (3, 0), (), "ObjectType", None),
		# Method 'Objects' returns object of type 'IObjects'
		"Objects": (1610809347, 2, (9, 0), ((3, 49),), "Objects", '{44747797-9642-483B-AB9C-6AE0A1899549}'),
		# Method 'Parent' returns object of type 'IObject'
		"Parent": (1610743809, 2, (9, 0), (), "Parent", '{7A5D1A08-B723-4929-BB46-A801DC642EB6}'),
	}
	_prop_map_put_ = {
	}

	ClearanceType: str # read_only
	Comments: str # ICommentsMutable; read_only
	Constraints: str # IConstraintsMutable; read_only
	GeneralClearanceType: str # read_only
	Name: str # read_only
	ObjectType: str # read_only
	Objects: str # IObjects; read_only
	Parent: str # IObject; read_only

	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
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

class IGeneralClearances(DispatchBaseClass):
	CLSID = IID('{A96A5A2C-6E39-4FB7-A86C-C6992501261A}')
	coclass_clsid = IID('{E82C72F8-E994-46BB-8E9A-1A2815C34A4F}')

	# Result is of type IGeneralClearance
	def FindItem(self, p_eType=defaultNamedNotOptArg):
		'Finds the general clearance of the given type.'
		ret = self._oleobj_.InvokeTypes(1610809345, LCID, 1, (9, 0), ((3, 1),),p_eType
			)
		if ret is not None:
			ret = Dispatch(ret, 'FindItem', '{D7ABE808-2624-4912-B413-96F9E0B5BA5B}')
		return ret

	# Result is of type IGeneralClearance
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the general clearance of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{D7ABE808-2624-4912-B413-96F9E0B5BA5B}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the general clearance of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{D7ABE808-2624-4912-B413-96F9E0B5BA5B}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{D7ABE808-2624-4912-B413-96F9E0B5BA5B}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IGeneralClearancesMutable(DispatchBaseClass):
	CLSID = IID('{BC62A287-210A-4466-A894-5ACB1F4E0E25}')
	coclass_clsid = IID('{7B50268E-5CD1-480D-B35F-E20A8430DD24}')

	# Result is of type IGeneralClearance
	def Add(self, p_strName=defaultNamedNotOptArg):
		'Creates the general clearance of the given name and adds it to the collection.'
		ret = self._oleobj_.InvokeTypes(1610874880, LCID, 1, (9, 0), ((8, 1),),p_strName
			)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{D7ABE808-2624-4912-B413-96F9E0B5BA5B}')
		return ret

	# Result is of type IGeneralClearance
	def AddByType(self, p_eType=defaultNamedNotOptArg):
		'Creates the general clearance of the given type and adds it to the collection.'
		ret = self._oleobj_.InvokeTypes(1610874881, LCID, 1, (9, 0), ((3, 1),),p_eType
			)
		if ret is not None:
			ret = Dispatch(ret, 'AddByType', '{D7ABE808-2624-4912-B413-96F9E0B5BA5B}')
		return ret

	def Delete(self, p_vIndex=defaultNamedNotOptArg):
		'Deletes the general clearance of the given index or name and removes it from the collection.'
		return self._oleobj_.InvokeTypes(1610874882, LCID, 1, (24, 0), ((12, 1),),p_vIndex
			)

	def DeleteByType(self, p_eType=defaultNamedNotOptArg):
		'Deletes the general clearance of the given type and removes it from the collection.'
		return self._oleobj_.InvokeTypes(1610874883, LCID, 1, (24, 0), ((3, 1),),p_eType
			)

	# Result is of type IGeneralClearance
	def FindItem(self, p_eType=defaultNamedNotOptArg):
		'Finds the general clearance of the given type.'
		ret = self._oleobj_.InvokeTypes(1610809345, LCID, 1, (9, 0), ((3, 1),),p_eType
			)
		if ret is not None:
			ret = Dispatch(ret, 'FindItem', '{D7ABE808-2624-4912-B413-96F9E0B5BA5B}')
		return ret

	# Result is of type IGeneralClearance
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the general clearance of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{D7ABE808-2624-4912-B413-96F9E0B5BA5B}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the general clearance of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{D7ABE808-2624-4912-B413-96F9E0B5BA5B}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{D7ABE808-2624-4912-B413-96F9E0B5BA5B}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ILayer(DispatchBaseClass):
	CLSID = IID('{052E8B90-0E4C-44C1-8F39-89E344392B5C}')
	coclass_clsid = IID('{A1BB2710-763F-4DC1-AE6D-0F079CAC9AFA}')

	# Result is of type IConstraintsMutable
	# The method GetConstraints is actually a property, but must be used as a method to correctly pass the arguments
	def GetConstraints(self, p_nConstraintMask=7):
		'Returns the collection of constraints, filtered by EConstraintMask constant.'
		ret = self._oleobj_.InvokeTypes(1610809345, LCID, 2, (9, 0), ((3, 49),),p_nConstraintMask
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetConstraints', '{1DDEC891-7D43-4EE9-9BD4-63772C577150}')
		return ret

	# Result is of type IObjects
	# The method GetObjects is actually a property, but must be used as a method to correctly pass the arguments
	def GetObjects(self, p_eObjectType=0):
		'Returns the collection of child objects, filtered by EObjectType constant.'
		ret = self._oleobj_.InvokeTypes(1610809347, LCID, 2, (9, 0), ((3, 49),),p_eObjectType
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjects', '{44747797-9642-483B-AB9C-6AE0A1899549}')
		return ret

	def IsDefault(self):
		'Returns true if the object is default and cannot be deleted.'
		return self._oleobj_.InvokeTypes(1610743811, LCID, 1, (11, 0), (),)

	def IsValid(self):
		'Returns true if the object is still valid.'
		return self._oleobj_.InvokeTypes(1610743810, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		# Method 'Comments' returns object of type 'ICommentsMutable'
		"Comments": (1610809346, 2, (9, 0), (), "Comments", '{23FAC1D8-2578-42BC-9F65-F04930FB6489}'),
		# Method 'Constraints' returns object of type 'IConstraintsMutable'
		"Constraints": (1610809345, 2, (9, 0), ((3, 49),), "Constraints", '{1DDEC891-7D43-4EE9-9BD4-63772C577150}'),
		"Index": (1610874880, 2, (3, 0), (), "Index", None),
		"LayerType": (1610874882, 2, (3, 0), (), "LayerType", None),
		"LayerUsage": (1610874883, 2, (3, 0), (), "LayerUsage", None),
		"MetallicIndex": (1610874881, 2, (3, 0), (), "MetallicIndex", None),
		"Name": (0, 2, (8, 0), (), "Name", None),
		"ObjectType": (1610809344, 2, (3, 0), (), "ObjectType", None),
		# Method 'Objects' returns object of type 'IObjects'
		"Objects": (1610809347, 2, (9, 0), ((3, 49),), "Objects", '{44747797-9642-483B-AB9C-6AE0A1899549}'),
		# Method 'Parent' returns object of type 'IObject'
		"Parent": (1610743809, 2, (9, 0), (), "Parent", '{7A5D1A08-B723-4929-BB46-A801DC642EB6}'),
	}
	_prop_map_put_ = {
	}

	Comments: str # ICommentsMutable; read_only
	Constraints: str # IConstraintsMutable; read_only
	Index: str # read_only
	LayerType: str # read_only
	LayerUsage: str # read_only
	MetallicIndex: str # read_only
	Name: str # read_only
	ObjectType: str # read_only
	Objects: str # IObjects; read_only
	Parent: str # IObject; read_only

	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
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

class ILayers(DispatchBaseClass):
	CLSID = IID('{A8C2D4D7-EF76-436C-BDC8-0813B8248EBF}')
	coclass_clsid = IID('{96977B18-D144-4DB5-AF5F-266B353B61E6}')

	# Result is of type ILayer
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the layer of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{052E8B90-0E4C-44C1-8F39-89E344392B5C}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
		"MetallicCount": (1610809344, 2, (3, 0), (), "MetallicCount", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only
	MetallicCount: str # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the layer of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{052E8B90-0E4C-44C1-8F39-89E344392B5C}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{052E8B90-0E4C-44C1-8F39-89E344392B5C}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ILayersMutable(DispatchBaseClass):
	CLSID = IID('{39981775-2776-4221-AB3C-1C27040DB64E}')
	coclass_clsid = IID('{CD47D215-A820-47E2-AE07-453CC2ED6D7C}')

	# Result is of type ILayer
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the layer of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{052E8B90-0E4C-44C1-8F39-89E344392B5C}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
		"MetallicCount": (1610809344, 2, (3, 0), (), "MetallicCount", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only
	MetallicCount: str # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the layer of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{052E8B90-0E4C-44C1-8F39-89E344392B5C}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{052E8B90-0E4C-44C1-8F39-89E344392B5C}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IMatchGroup(DispatchBaseClass):
	CLSID = IID('{141C68A8-5519-4BD9-887B-C02B3E31E9F0}')
	coclass_clsid = IID('{BE604238-860C-429A-86DD-282A1D52ADFF}')

	# Result is of type IConstraintsMutable
	# The method GetConstraints is actually a property, but must be used as a method to correctly pass the arguments
	def GetConstraints(self, p_nConstraintMask=7):
		'Returns the collection of constraints, filtered by EConstraintMask constant.'
		ret = self._oleobj_.InvokeTypes(1610809345, LCID, 2, (9, 0), ((3, 49),),p_nConstraintMask
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetConstraints', '{1DDEC891-7D43-4EE9-9BD4-63772C577150}')
		return ret

	# Result is of type INetsMutable
	# The method GetNets is actually a property, but must be used as a method to correctly pass the arguments
	def GetNets(self, p_nNetMask=15):
		'Returns the collection of nets assigned to the match group, filtered by ENetMask constant.'
		ret = self._oleobj_.InvokeTypes(1610874883, LCID, 2, (9, 0), ((3, 49),),p_nNetMask
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetNets', '{17F8541C-BB01-40FC-AAFD-179AA166F42D}')
		return ret

	# Result is of type IObjects
	# The method GetObjects is actually a property, but must be used as a method to correctly pass the arguments
	def GetObjects(self, p_eObjectType=0):
		'Returns the collection of child objects, filtered by EObjectType constant.'
		ret = self._oleobj_.InvokeTypes(1610809347, LCID, 2, (9, 0), ((3, 49),),p_eObjectType
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjects', '{44747797-9642-483B-AB9C-6AE0A1899549}')
		return ret

	def IsDefault(self):
		'Returns true if the object is default and cannot be deleted.'
		return self._oleobj_.InvokeTypes(1610743811, LCID, 1, (11, 0), (),)

	def IsValid(self):
		'Returns true if the object is still valid.'
		return self._oleobj_.InvokeTypes(1610743810, LCID, 1, (11, 0), (),)

	def Rename(self, p_strName=defaultNamedNotOptArg):
		'Changes the name of the object.'
		return self._oleobj_.InvokeTypes(1610874885, LCID, 1, (24, 0), ((8, 1),),p_strName
			)

	_prop_map_get_ = {
		# Method 'Comments' returns object of type 'ICommentsMutable'
		"Comments": (1610809346, 2, (9, 0), (), "Comments", '{23FAC1D8-2578-42BC-9F65-F04930FB6489}'),
		# Method 'Constraints' returns object of type 'IConstraintsMutable'
		"Constraints": (1610809345, 2, (9, 0), ((3, 49),), "Constraints", '{1DDEC891-7D43-4EE9-9BD4-63772C577150}'),
		"DelayType": (1610874881, 2, (3, 0), (), "DelayType", None),
		"MatchGroupType": (1610874880, 2, (3, 0), (), "MatchGroupType", None),
		"Name": (0, 2, (8, 0), (), "Name", None),
		# Method 'Nets' returns object of type 'INetsMutable'
		"Nets": (1610874883, 2, (9, 0), ((3, 49),), "Nets", '{17F8541C-BB01-40FC-AAFD-179AA166F42D}'),
		"ObjectType": (1610809344, 2, (3, 0), (), "ObjectType", None),
		# Method 'Objects' returns object of type 'IObjects'
		"Objects": (1610809347, 2, (9, 0), ((3, 49),), "Objects", '{44747797-9642-483B-AB9C-6AE0A1899549}'),
		# Method 'Parent' returns object of type 'IObject'
		"Parent": (1610743809, 2, (9, 0), (), "Parent", '{7A5D1A08-B723-4929-BB46-A801DC642EB6}'),
		# Method 'PinPairs' returns object of type 'IPinPairsMutable'
		"PinPairs": (1610874884, 2, (9, 0), (), "PinPairs", '{0D52DE96-799A-4660-ACFE-109F34DEE67B}'),
	}
	_prop_map_put_ = {
		"DelayType": ((1610874881, LCID, 4, 0),()),
	}

	Comments: str # ICommentsMutable; read_only
	Constraints: str # IConstraintsMutable; read_only
	DelayType: str # read/write
	MatchGroupType: str # read_only
	Name: str # read_only
	Nets: str # INetsMutable; read_only
	ObjectType: str # read_only
	Objects: str # IObjects; read_only
	Parent: str # IObject; read_only
	PinPairs: str # IPinPairsMutable; read_only

	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
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

class IMatchGroups(DispatchBaseClass):
	CLSID = IID('{1F460B56-507F-4CA6-B8D7-676CBB2427BD}')
	coclass_clsid = IID('{95AF9055-4360-4AD1-837E-8A4AEF81AF34}')

	# Result is of type IMatchGroup
	def FindItem(self, p_eType=defaultNamedNotOptArg, p_strName=defaultNamedNotOptArg):
		'Finds the match group of the given type and name.'
		ret = self._oleobj_.InvokeTypes(1610809345, LCID, 1, (9, 0), ((3, 1), (8, 1)),p_eType
			, p_strName)
		if ret is not None:
			ret = Dispatch(ret, 'FindItem', '{141C68A8-5519-4BD9-887B-C02B3E31E9F0}')
		return ret

	# Result is of type IMatchGroup
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the match group of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{141C68A8-5519-4BD9-887B-C02B3E31E9F0}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the match group of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{141C68A8-5519-4BD9-887B-C02B3E31E9F0}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{141C68A8-5519-4BD9-887B-C02B3E31E9F0}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IMatchGroupsMutable(DispatchBaseClass):
	CLSID = IID('{F36348AB-8180-41C3-951F-0B079E3FF03F}')
	coclass_clsid = IID('{E4717647-28C9-420B-8624-6A0298314D93}')

	# Result is of type IMatchGroup
	def Add(self, p_eType=defaultNamedNotOptArg, p_strName=defaultNamedNotOptArg, p_vTolerance=defaultNamedOptArg):
		'Creates the match group of the given type and name and adds it to the collection.'
		ret = self._oleobj_.InvokeTypes(1610874880, LCID, 1, (9, 0), ((3, 1), (8, 1), (12, 17)),p_eType
			, p_strName, p_vTolerance)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{141C68A8-5519-4BD9-887B-C02B3E31E9F0}')
		return ret

	def Delete(self, p_vIndex=defaultNamedNotOptArg):
		'Deletes the match group of the given index or name and removes it from the collection.'
		return self._oleobj_.InvokeTypes(1610874881, LCID, 1, (24, 0), ((12, 1),),p_vIndex
			)

	def DeleteByType(self, p_eType=defaultNamedNotOptArg, p_strName=defaultNamedNotOptArg):
		'Deletes the match group of the given type and name and removes it from the collection.'
		return self._oleobj_.InvokeTypes(1610874882, LCID, 1, (24, 0), ((3, 1), (8, 1)),p_eType
			, p_strName)

	# Result is of type IMatchGroup
	def FindItem(self, p_eType=defaultNamedNotOptArg, p_strName=defaultNamedNotOptArg):
		'Finds the match group of the given type and name.'
		ret = self._oleobj_.InvokeTypes(1610809345, LCID, 1, (9, 0), ((3, 1), (8, 1)),p_eType
			, p_strName)
		if ret is not None:
			ret = Dispatch(ret, 'FindItem', '{141C68A8-5519-4BD9-887B-C02B3E31E9F0}')
		return ret

	# Result is of type IMatchGroup
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the match group of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{141C68A8-5519-4BD9-887B-C02B3E31E9F0}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the match group of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{141C68A8-5519-4BD9-887B-C02B3E31E9F0}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{141C68A8-5519-4BD9-887B-C02B3E31E9F0}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class INet(DispatchBaseClass):
	CLSID = IID('{48420240-E6BB-423E-9FD3-F3E4687E1452}')
	coclass_clsid = IID('{E111A365-1082-4B6E-A64B-FAE25BFEFB1B}')

	# Result is of type IConstraintsMutable
	# The method GetConstraints is actually a property, but must be used as a method to correctly pass the arguments
	def GetConstraints(self, p_nConstraintMask=7):
		'Returns the collection of constraints, filtered by EConstraintMask constant.'
		ret = self._oleobj_.InvokeTypes(1610809345, LCID, 2, (9, 0), ((3, 49),),p_nConstraintMask
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetConstraints', '{1DDEC891-7D43-4EE9-9BD4-63772C577150}')
		return ret

	# Result is of type IMatchGroups
	# The method GetMatchGroups is actually a property, but must be used as a method to correctly pass the arguments
	def GetMatchGroups(self, p_nMatchGroupMask=3):
		'Returns all match groups related to the net.'
		ret = self._oleobj_.InvokeTypes(1610874887, LCID, 2, (9, 0), ((3, 49),),p_nMatchGroupMask
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetMatchGroups', '{1F460B56-507F-4CA6-B8D7-676CBB2427BD}')
		return ret

	# Result is of type IObjects
	# The method GetObjects is actually a property, but must be used as a method to correctly pass the arguments
	def GetObjects(self, p_eObjectType=0):
		'Returns the collection of child objects, filtered by EObjectType constant.'
		ret = self._oleobj_.InvokeTypes(1610809347, LCID, 2, (9, 0), ((3, 49),),p_eObjectType
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjects', '{44747797-9642-483B-AB9C-6AE0A1899549}')
		return ret

	def IsDefault(self):
		'Returns true if the object is default and cannot be deleted.'
		return self._oleobj_.InvokeTypes(1610743811, LCID, 1, (11, 0), (),)

	def IsValid(self):
		'Returns true if the object is still valid.'
		return self._oleobj_.InvokeTypes(1610743810, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		# Method 'Comments' returns object of type 'ICommentsMutable'
		"Comments": (1610809346, 2, (9, 0), (), "Comments", '{23FAC1D8-2578-42BC-9F65-F04930FB6489}'),
		# Method 'ConstraintClass' returns object of type 'IConstraintClass'
		"ConstraintClass": (1610874885, 2, (9, 0), (), "ConstraintClass", '{CB59FE57-0379-43C2-86FF-E6E0D31CBAB9}'),
		# Method 'Constraints' returns object of type 'IConstraintsMutable'
		"Constraints": (1610809345, 2, (9, 0), ((3, 49),), "Constraints", '{1DDEC891-7D43-4EE9-9BD4-63772C577150}'),
		"DelayType": (1610874882, 2, (3, 0), (), "DelayType", None),
		# Method 'DisplayPattern' returns object of type 'IDisplayPattern'
		"DisplayPattern": (1610874890, 2, (9, 0), (), "DisplayPattern", '{E6F44CAC-B61D-4437-971F-60F01875D6BB}'),
		# Method 'Formula' returns object of type 'IFormula'
		"Formula": (1610874888, 2, (9, 0), (), "Formula", '{A59586BA-4C99-4643-B6F8-E42BBF2E00D2}'),
		# Method 'MatchGroups' returns object of type 'IMatchGroups'
		"MatchGroups": (1610874887, 2, (9, 0), ((3, 49),), "MatchGroups", '{1F460B56-507F-4CA6-B8D7-676CBB2427BD}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
		# Method 'NetClass' returns object of type 'INetClass'
		"NetClass": (1610874886, 2, (9, 0), (), "NetClass", '{791A98C5-512E-45E0-8F4F-715A45F5707A}'),
		"NetType": (1610874880, 2, (3, 0), (), "NetType", None),
		# Method 'NoiseRules' returns object of type 'INoiseRules'
		"NoiseRules": (1610874889, 2, (9, 0), (), "NoiseRules", '{ED063FFC-209C-48D7-8D59-6677873C9A7A}'),
		"ObjectType": (1610809344, 2, (3, 0), (), "ObjectType", None),
		# Method 'Objects' returns object of type 'IObjects'
		"Objects": (1610809347, 2, (9, 0), ((3, 49),), "Objects", '{44747797-9642-483B-AB9C-6AE0A1899549}'),
		# Method 'Parent' returns object of type 'IObject'
		"Parent": (1610743809, 2, (9, 0), (), "Parent", '{7A5D1A08-B723-4929-BB46-A801DC642EB6}'),
		# Method 'Topology' returns object of type 'ITopology'
		"Topology": (1610874884, 2, (9, 0), (), "Topology", '{E827A25D-2BEB-4013-9E2B-035133E06025}'),
	}
	_prop_map_put_ = {
		"DelayType": ((1610874882, LCID, 4, 0),()),
		"NetType": ((1610874880, LCID, 4, 0),()),
	}

	Comments: str # ICommentsMutable; read_only
	ConstraintClass: str # IConstraintClass; read_only
	Constraints: str # IConstraintsMutable; read_only
	DelayType: str # read/write
	DisplayPattern: str # IDisplayPattern; read_only
	Formula: str # IFormula; read_only
	MatchGroups: str # IMatchGroups; read_only
	Name: str # read_only
	NetClass: str # INetClass; read_only
	NetType: str # read/write
	NoiseRules: str # INoiseRules; read_only
	ObjectType: str # read_only
	Objects: str # IObjects; read_only
	Parent: str # IObject; read_only
	Topology: str # ITopology; read_only

	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
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

class INetClass(DispatchBaseClass):
	CLSID = IID('{791A98C5-512E-45E0-8F4F-715A45F5707A}')
	coclass_clsid = IID('{34DA88B0-930D-469A-8CE0-0738CBCD4870}')

	def AssignConstraintClass(self, p_pConstraintClass=defaultNamedNotOptArg):
		'Assigns the given constraint class to the net class.'
		return self._oleobj_.InvokeTypes(1610940419, LCID, 1, (24, 0), ((9, 1),),p_pConstraintClass
			)

	def AssignNet(self, p_pNet=defaultNamedNotOptArg):
		'Assigns the given net to the class.'
		return self._oleobj_.InvokeTypes(1610874883, LCID, 1, (24, 0), ((9, 1),),p_pNet
			)

	# Result is of type IClassClearances
	# The method GetClassClearances is actually a property, but must be used as a method to correctly pass the arguments
	def GetClassClearances(self, p_nClassClearancesMask=3):
		'Returns the collection of all class clearances associated with the net class, filtered by EClassClearancesMask constant.'
		ret = self._oleobj_.InvokeTypes(1610940420, LCID, 2, (9, 0), ((3, 49),),p_nClassClearancesMask
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetClassClearances', '{96FD6C42-8C02-4A00-A1B6-C47FB0D47913}')
		return ret

	# Result is of type IConstraintsMutable
	# The method GetConstraints is actually a property, but must be used as a method to correctly pass the arguments
	def GetConstraints(self, p_nConstraintMask=7):
		'Returns the collection of constraints, filtered by EConstraintMask constant.'
		ret = self._oleobj_.InvokeTypes(1610809345, LCID, 2, (9, 0), ((3, 49),),p_nConstraintMask
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetConstraints', '{1DDEC891-7D43-4EE9-9BD4-63772C577150}')
		return ret

	# Result is of type INetClassesMutable
	# The method GetNetClasses is actually a property, but must be used as a method to correctly pass the arguments
	def GetNetClasses(self, p_nNetClassMask=2):
		'Returns the collection of child net classes, filtered by EObjectMask constant.'
		ret = self._oleobj_.InvokeTypes(1610940416, LCID, 2, (9, 0), ((3, 49),),p_nNetClassMask
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetNetClasses', '{DAA15140-C478-41AE-90D4-8782BA3A8707}')
		return ret

	# Result is of type INets
	# The method GetNets is actually a property, but must be used as a method to correctly pass the arguments
	def GetNets(self, p_nNetMask=1):
		'Returns the collection of nets assigned to the class, filtered by ENetMask constant.'
		ret = self._oleobj_.InvokeTypes(1610874881, LCID, 2, (9, 0), ((3, 49),),p_nNetMask
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetNets', '{EAF633E9-E21E-47FF-A361-60A4B480301F}')
		return ret

	# Result is of type IObjects
	# The method GetObjects is actually a property, but must be used as a method to correctly pass the arguments
	def GetObjects(self, p_eObjectType=0):
		'Returns the collection of child objects, filtered by EObjectType constant.'
		ret = self._oleobj_.InvokeTypes(1610809347, LCID, 2, (9, 0), ((3, 49),),p_eObjectType
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjects', '{44747797-9642-483B-AB9C-6AE0A1899549}')
		return ret

	def IsDefault(self):
		'Returns true if the object is default and cannot be deleted.'
		return self._oleobj_.InvokeTypes(1610743811, LCID, 1, (11, 0), (),)

	def IsValid(self):
		'Returns true if the object is still valid.'
		return self._oleobj_.InvokeTypes(1610743810, LCID, 1, (11, 0), (),)

	def MoveTo(self, p_pParentNetClass=defaultNamedNotOptArg):
		'Changes the parent of the net class. Set to Null for the root net class.'
		return self._oleobj_.InvokeTypes(1610940418, LCID, 1, (24, 0), ((9, 1),),p_pParentNetClass
			)

	def Rename(self, p_strName=defaultNamedNotOptArg):
		'Changes the name of the object.'
		return self._oleobj_.InvokeTypes(1610874882, LCID, 1, (24, 0), ((8, 1),),p_strName
			)

	_prop_map_get_ = {
		# Method 'ClassClearances' returns object of type 'IClassClearances'
		"ClassClearances": (1610940420, 2, (9, 0), ((3, 49),), "ClassClearances", '{96FD6C42-8C02-4A00-A1B6-C47FB0D47913}'),
		# Method 'Comments' returns object of type 'ICommentsMutable'
		"Comments": (1610809346, 2, (9, 0), (), "Comments", '{23FAC1D8-2578-42BC-9F65-F04930FB6489}'),
		# Method 'ConstraintClasses' returns object of type 'IConstraintClasses'
		"ConstraintClasses": (1610940417, 2, (9, 0), (), "ConstraintClasses", '{7D9A71CB-B02F-4A1B-9995-2ADF58C69494}'),
		# Method 'Constraints' returns object of type 'IConstraintsMutable'
		"Constraints": (1610809345, 2, (9, 0), ((3, 49),), "Constraints", '{1DDEC891-7D43-4EE9-9BD4-63772C577150}'),
		# Method 'DisplayPattern' returns object of type 'IDisplayPattern'
		"DisplayPattern": (1610874884, 2, (9, 0), (), "DisplayPattern", '{E6F44CAC-B61D-4437-971F-60F01875D6BB}'),
		"FullName": (1610874880, 2, (8, 0), (), "FullName", None),
		"Name": (0, 2, (8, 0), (), "Name", None),
		# Method 'NetClasses' returns object of type 'INetClassesMutable'
		"NetClasses": (1610940416, 2, (9, 0), ((3, 49),), "NetClasses", '{DAA15140-C478-41AE-90D4-8782BA3A8707}'),
		# Method 'Nets' returns object of type 'INets'
		"Nets": (1610874881, 2, (9, 0), ((3, 49),), "Nets", '{EAF633E9-E21E-47FF-A361-60A4B480301F}'),
		"ObjectType": (1610809344, 2, (3, 0), (), "ObjectType", None),
		# Method 'Objects' returns object of type 'IObjects'
		"Objects": (1610809347, 2, (9, 0), ((3, 49),), "Objects", '{44747797-9642-483B-AB9C-6AE0A1899549}'),
		# Method 'Parent' returns object of type 'IObject'
		"Parent": (1610743809, 2, (9, 0), (), "Parent", '{7A5D1A08-B723-4929-BB46-A801DC642EB6}'),
	}
	_prop_map_put_ = {
	}

	ClassClearances: str # IClassClearances; read_only
	Comments: str # ICommentsMutable; read_only
	ConstraintClasses: str # IConstraintClasses; read_only
	Constraints: str # IConstraintsMutable; read_only
	DisplayPattern: str # IDisplayPattern; read_only
	FullName: str # read_only
	Name: str # read_only
	NetClasses: str # INetClassesMutable; read_only
	Nets: str # INets; read_only
	ObjectType: str # read_only
	Objects: str # IObjects; read_only
	Parent: str # IObject; read_only

	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
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

class INetClasses(DispatchBaseClass):
	CLSID = IID('{53A3ED0F-BBD8-41BF-9460-F17C61BCD389}')
	coclass_clsid = IID('{E6945AC7-71DE-4FBD-B914-513A60E82520}')

	# Result is of type INetClass
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the net class of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{791A98C5-512E-45E0-8F4F-715A45F5707A}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the net class of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{791A98C5-512E-45E0-8F4F-715A45F5707A}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{791A98C5-512E-45E0-8F4F-715A45F5707A}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class INetClassesMutable(DispatchBaseClass):
	CLSID = IID('{DAA15140-C478-41AE-90D4-8782BA3A8707}')
	coclass_clsid = IID('{38ABD376-70EE-45BF-B017-90DC59A9EB2F}')

	# Result is of type INetClass
	def Add(self, p_strName=defaultNamedNotOptArg):
		'Creates the net class of the given name and adds it to the collection.'
		ret = self._oleobj_.InvokeTypes(1610874880, LCID, 1, (9, 0), ((8, 1),),p_strName
			)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{791A98C5-512E-45E0-8F4F-715A45F5707A}')
		return ret

	def Delete(self, p_vIndex=defaultNamedNotOptArg):
		'Deletes the net class of the given index or name and removes it from the collection.'
		return self._oleobj_.InvokeTypes(1610874883, LCID, 1, (24, 0), ((12, 1),),p_vIndex
			)

	def Insert(self, p_pNetClass=defaultNamedNotOptArg):
		'Inserts the net class to the collection.'
		return self._oleobj_.InvokeTypes(1610874881, LCID, 1, (24, 0), ((9, 1),),p_pNetClass
			)

	# Result is of type INetClass
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the net class of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{791A98C5-512E-45E0-8F4F-715A45F5707A}')
		return ret

	def Remove(self, p_vIndex=defaultNamedNotOptArg):
		'Removes the net class of the given index or name from the collection.'
		return self._oleobj_.InvokeTypes(1610874882, LCID, 1, (24, 0), ((12, 1),),p_vIndex
			)

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the net class of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{791A98C5-512E-45E0-8F4F-715A45F5707A}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{791A98C5-512E-45E0-8F4F-715A45F5707A}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class INets(DispatchBaseClass):
	CLSID = IID('{EAF633E9-E21E-47FF-A361-60A4B480301F}')
	coclass_clsid = IID('{6AAAB236-9207-4D72-91AB-37FAD56B1505}')

	# Result is of type INet
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the net of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{48420240-E6BB-423E-9FD3-F3E4687E1452}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the net of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{48420240-E6BB-423E-9FD3-F3E4687E1452}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{48420240-E6BB-423E-9FD3-F3E4687E1452}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class INetsMutable(DispatchBaseClass):
	CLSID = IID('{17F8541C-BB01-40FC-AAFD-179AA166F42D}')
	coclass_clsid = IID('{C03A89DF-4DDB-4892-BF2A-3C92018D9F7E}')

	def Insert(self, p_pNet=defaultNamedNotOptArg):
		'Inserts the net to the collection.'
		return self._oleobj_.InvokeTypes(1610874880, LCID, 1, (24, 0), ((9, 1),),p_pNet
			)

	# Result is of type INet
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the net of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{48420240-E6BB-423E-9FD3-F3E4687E1452}')
		return ret

	def Remove(self, p_vIndex=defaultNamedNotOptArg):
		'Removes the net of the given index or name from the collection.'
		return self._oleobj_.InvokeTypes(1610874881, LCID, 1, (24, 0), ((12, 1),),p_vIndex
			)

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the net of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{48420240-E6BB-423E-9FD3-F3E4687E1452}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{48420240-E6BB-423E-9FD3-F3E4687E1452}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class INoiseRule(DispatchBaseClass):
	CLSID = IID('{D06D3CAD-4D4E-40B8-9A9A-16D446917F77}')
	coclass_clsid = IID('{62CDF1A0-E6E8-4C62-8C4E-05015FA9FD54}')

	# Result is of type IConstraintsMutable
	# The method GetConstraints is actually a property, but must be used as a method to correctly pass the arguments
	def GetConstraints(self, p_nConstraintMask=7):
		'Returns the collection of constraints, filtered by EConstraintMask constant.'
		ret = self._oleobj_.InvokeTypes(1610809345, LCID, 2, (9, 0), ((3, 49),),p_nConstraintMask
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetConstraints', '{1DDEC891-7D43-4EE9-9BD4-63772C577150}')
		return ret

	# Result is of type IObjects
	# The method GetObjects is actually a property, but must be used as a method to correctly pass the arguments
	def GetObjects(self, p_eObjectType=0):
		'Returns the collection of child objects, filtered by EObjectType constant.'
		ret = self._oleobj_.InvokeTypes(1610809347, LCID, 2, (9, 0), ((3, 49),),p_eObjectType
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjects', '{44747797-9642-483B-AB9C-6AE0A1899549}')
		return ret

	def IsDefault(self):
		'Returns true if the object is default and cannot be deleted.'
		return self._oleobj_.InvokeTypes(1610743811, LCID, 1, (11, 0), (),)

	def IsValid(self):
		'Returns true if the object is still valid.'
		return self._oleobj_.InvokeTypes(1610743810, LCID, 1, (11, 0), (),)

	def Rename(self, p_strName=defaultNamedNotOptArg):
		'Changes the name of the object.'
		return self._oleobj_.InvokeTypes(1610874880, LCID, 1, (24, 0), ((8, 1),),p_strName
			)

	_prop_map_get_ = {
		"Aggressor": (1610874884, 2, (12, 0), (), "Aggressor", None),
		# Method 'Comments' returns object of type 'ICommentsMutable'
		"Comments": (1610809346, 2, (9, 0), (), "Comments", '{23FAC1D8-2578-42BC-9F65-F04930FB6489}'),
		# Method 'Constraints' returns object of type 'IConstraintsMutable'
		"Constraints": (1610809345, 2, (9, 0), ((3, 49),), "Constraints", '{1DDEC891-7D43-4EE9-9BD4-63772C577150}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
		"NoiseRuleType": (1610874881, 2, (3, 0), (), "NoiseRuleType", None),
		"ObjectType": (1610809344, 2, (3, 0), (), "ObjectType", None),
		# Method 'Objects' returns object of type 'IObjects'
		"Objects": (1610809347, 2, (9, 0), ((3, 49),), "Objects", '{44747797-9642-483B-AB9C-6AE0A1899549}'),
		# Method 'ParallelismRule' returns object of type 'IParallelismRule'
		"ParallelismRule": (1610874886, 2, (9, 0), (), "ParallelismRule", '{A11D8E06-CE97-402B-AFD5-D75BACE22E1A}'),
		# Method 'Parent' returns object of type 'IObject'
		"Parent": (1610743809, 2, (9, 0), (), "Parent", '{7A5D1A08-B723-4929-BB46-A801DC642EB6}'),
		"Victim": (1610874882, 2, (12, 0), (), "Victim", None),
	}
	_prop_map_put_ = {
		"Aggressor": ((1610874884, LCID, 4, 0),()),
		"ParallelismRule": ((1610874886, LCID, 4, 0),()),
		"Victim": ((1610874882, LCID, 4, 0),()),
	}

	Aggressor: str # read/write
	Comments: str # ICommentsMutable; read_only
	Constraints: str # IConstraintsMutable; read_only
	Name: str # read_only
	NoiseRuleType: str # read_only
	ObjectType: str # read_only
	Objects: str # IObjects; read_only
	ParallelismRule: str # read/write
	Parent: str # IObject; read_only
	Victim: str # read/write

	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
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

class INoiseRules(DispatchBaseClass):
	CLSID = IID('{ED063FFC-209C-48D7-8D59-6677873C9A7A}')
	coclass_clsid = IID('{B954C85D-6103-4A81-A73D-4334ACE4FB4C}')

	# Result is of type INoiseRule
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the noise rule of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{D06D3CAD-4D4E-40B8-9A9A-16D446917F77}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the noise rule of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{D06D3CAD-4D4E-40B8-9A9A-16D446917F77}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{D06D3CAD-4D4E-40B8-9A9A-16D446917F77}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class INoiseRulesMutable(DispatchBaseClass):
	CLSID = IID('{D07554EB-FCFF-48EC-AD04-C79988D20C9D}')
	coclass_clsid = IID('{1C7ACB33-918C-4071-BB73-471C94FDFA75}')

	# Result is of type INoiseRule
	def Add(self, p_eNoiseRuleType=defaultNamedNotOptArg, p_strName=defaultNamedNotOptArg, p_vVictim=defaultNamedNotOptArg, p_vAggressor=defaultNamedNotOptArg):
		'Creates the noise rule and adds it to the collection.'
		ret = self._oleobj_.InvokeTypes(1610874880, LCID, 1, (9, 0), ((3, 1), (8, 1), (12, 1), (12, 1)),p_eNoiseRuleType
			, p_strName, p_vVictim, p_vAggressor)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{D06D3CAD-4D4E-40B8-9A9A-16D446917F77}')
		return ret

	def Delete(self, p_vIndex=defaultNamedNotOptArg):
		'Deletes the noise rule of the given index or name and removes it from the collection.'
		return self._oleobj_.InvokeTypes(1610874881, LCID, 1, (24, 0), ((12, 1),),p_vIndex
			)

	# Result is of type INoiseRule
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the noise rule of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{D06D3CAD-4D4E-40B8-9A9A-16D446917F77}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the noise rule of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{D06D3CAD-4D4E-40B8-9A9A-16D446917F77}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{D06D3CAD-4D4E-40B8-9A9A-16D446917F77}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class INotation(DispatchBaseClass):
	CLSID = IID('{177B82E6-3AFF-4E52-8141-7911C63B1879}')
	coclass_clsid = IID('{866B8DDA-424F-4C1D-ACC7-74D2FD26A5E6}')

	_prop_map_get_ = {
		"ColorFormat": (1610743820, 2, (3, 0), (), "ColorFormat", None),
		"DecimalSymbol": (1610743808, 2, (8, 0), (), "DecimalSymbol", None),
		"DisplayLeadingZeros": (1610743816, 2, (11, 0), (), "DisplayLeadingZeros", None),
		"DisplayTrailingZeros": (1610743814, 2, (11, 0), (), "DisplayTrailingZeros", None),
		"GroupDigitsCount": (1610743812, 2, (3, 0), (), "GroupDigitsCount", None),
		"GroupSymbol": (1610743810, 2, (8, 0), (), "GroupSymbol", None),
		"Precision": (1610743818, 2, (3, 0), (), "Precision", None),
	}
	_prop_map_put_ = {
		"ColorFormat": ((1610743820, LCID, 4, 0),()),
		"DecimalSymbol": ((1610743808, LCID, 4, 0),()),
		"DisplayLeadingZeros": ((1610743816, LCID, 4, 0),()),
		"DisplayTrailingZeros": ((1610743814, LCID, 4, 0),()),
		"GroupDigitsCount": ((1610743812, LCID, 4, 0),()),
		"GroupSymbol": ((1610743810, LCID, 4, 0),()),
		"Precision": ((1610743818, LCID, 4, 0),()),
	}

	ColorFormat: str # read/write
	DecimalSymbol: str # read/write
	DisplayLeadingZeros: str # read/write
	DisplayTrailingZeros: str # read/write
	GroupDigitsCount: str # read/write
	GroupSymbol: str # read/write
	Precision: str # read/write

	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IObject(DispatchBaseClass):
	CLSID = IID('{7A5D1A08-B723-4929-BB46-A801DC642EB6}')
	coclass_clsid = IID('{B29B6B0B-4390-4DE0-AB0E-652FBD8D5845}')

	# Result is of type IConstraintsMutable
	# The method GetConstraints is actually a property, but must be used as a method to correctly pass the arguments
	def GetConstraints(self, p_nConstraintMask=7):
		'Returns the collection of constraints, filtered by EConstraintMask constant.'
		ret = self._oleobj_.InvokeTypes(1610809345, LCID, 2, (9, 0), ((3, 49),),p_nConstraintMask
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetConstraints', '{1DDEC891-7D43-4EE9-9BD4-63772C577150}')
		return ret

	# Result is of type IObjects
	# The method GetObjects is actually a property, but must be used as a method to correctly pass the arguments
	def GetObjects(self, p_eObjectType=0):
		'Returns the collection of child objects, filtered by EObjectType constant.'
		ret = self._oleobj_.InvokeTypes(1610809347, LCID, 2, (9, 0), ((3, 49),),p_eObjectType
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjects', '{44747797-9642-483B-AB9C-6AE0A1899549}')
		return ret

	def IsDefault(self):
		'Returns true if the object is default and cannot be deleted.'
		return self._oleobj_.InvokeTypes(1610743811, LCID, 1, (11, 0), (),)

	def IsValid(self):
		'Returns true if the object is still valid.'
		return self._oleobj_.InvokeTypes(1610743810, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		# Method 'Comments' returns object of type 'ICommentsMutable'
		"Comments": (1610809346, 2, (9, 0), (), "Comments", '{23FAC1D8-2578-42BC-9F65-F04930FB6489}'),
		# Method 'Constraints' returns object of type 'IConstraintsMutable'
		"Constraints": (1610809345, 2, (9, 0), ((3, 49),), "Constraints", '{1DDEC891-7D43-4EE9-9BD4-63772C577150}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
		"ObjectType": (1610809344, 2, (3, 0), (), "ObjectType", None),
		# Method 'Objects' returns object of type 'IObjects'
		"Objects": (1610809347, 2, (9, 0), ((3, 49),), "Objects", '{44747797-9642-483B-AB9C-6AE0A1899549}'),
		# Method 'Parent' returns object of type 'IObject'
		"Parent": (1610743809, 2, (9, 0), (), "Parent", '{7A5D1A08-B723-4929-BB46-A801DC642EB6}'),
	}
	_prop_map_put_ = {
	}

	Comments: str # ICommentsMutable; read_only
	Constraints: str # IConstraintsMutable; read_only
	Name: str # read_only
	ObjectType: str # read_only
	Objects: str # IObjects; read_only
	Parent: str # IObject; read_only

	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
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

class IObjects(DispatchBaseClass):
	CLSID = IID('{44747797-9642-483B-AB9C-6AE0A1899549}')
	coclass_clsid = IID('{26F1B6BC-D3D7-4A17-9387-53063A8F3E19}')

	# Result is of type IObject
	def FindItem(self, p_eType=defaultNamedNotOptArg, p_strName=defaultNamedNotOptArg):
		'Finds the object of the given object type and name.'
		ret = self._oleobj_.InvokeTypes(1610809345, LCID, 1, (9, 0), ((3, 1), (8, 1)),p_eType
			, p_strName)
		if ret is not None:
			ret = Dispatch(ret, 'FindItem', '{7A5D1A08-B723-4929-BB46-A801DC642EB6}')
		return ret

	# Result is of type IObject
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_nIndex=defaultNamedNotOptArg):
		'Returns the object of the given index.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),p_nIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{7A5D1A08-B723-4929-BB46-A801DC642EB6}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_nIndex=defaultNamedNotOptArg):
		'Returns the object of the given index.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),p_nIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{7A5D1A08-B723-4929-BB46-A801DC642EB6}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{7A5D1A08-B723-4929-BB46-A801DC642EB6}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IPackageClearance(DispatchBaseClass):
	CLSID = IID('{240DA68C-6822-4B65-A4B3-8E7AB10B66AE}')
	coclass_clsid = IID('{8C1CE62E-16DF-4CF0-8939-4DC718FED03A}')

	# Result is of type IConstraintsMutable
	# The method GetConstraints is actually a property, but must be used as a method to correctly pass the arguments
	def GetConstraints(self, p_nConstraintMask=7):
		'Returns the collection of constraints, filtered by EConstraintMask constant.'
		ret = self._oleobj_.InvokeTypes(1610809345, LCID, 2, (9, 0), ((3, 49),),p_nConstraintMask
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetConstraints', '{1DDEC891-7D43-4EE9-9BD4-63772C577150}')
		return ret

	# Result is of type IObjects
	# The method GetObjects is actually a property, but must be used as a method to correctly pass the arguments
	def GetObjects(self, p_eObjectType=0):
		'Returns the collection of child objects, filtered by EObjectType constant.'
		ret = self._oleobj_.InvokeTypes(1610809347, LCID, 2, (9, 0), ((3, 49),),p_eObjectType
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjects', '{44747797-9642-483B-AB9C-6AE0A1899549}')
		return ret

	def IsDefault(self):
		'Returns true if the object is default and cannot be deleted.'
		return self._oleobj_.InvokeTypes(1610743811, LCID, 1, (11, 0), (),)

	def IsValid(self):
		'Returns true if the object is still valid.'
		return self._oleobj_.InvokeTypes(1610743810, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"ClearanceType": (1610874880, 2, (3, 0), (), "ClearanceType", None),
		# Method 'Comments' returns object of type 'ICommentsMutable'
		"Comments": (1610809346, 2, (9, 0), (), "Comments", '{23FAC1D8-2578-42BC-9F65-F04930FB6489}'),
		# Method 'Constraints' returns object of type 'IConstraintsMutable'
		"Constraints": (1610809345, 2, (9, 0), ((3, 49),), "Constraints", '{1DDEC891-7D43-4EE9-9BD4-63772C577150}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
		"ObjectType": (1610809344, 2, (3, 0), (), "ObjectType", None),
		# Method 'Objects' returns object of type 'IObjects'
		"Objects": (1610809347, 2, (9, 0), ((3, 49),), "Objects", '{44747797-9642-483B-AB9C-6AE0A1899549}'),
		# Method 'Parent' returns object of type 'IObject'
		"Parent": (1610743809, 2, (9, 0), (), "Parent", '{7A5D1A08-B723-4929-BB46-A801DC642EB6}'),
		# Method 'SourcePackage' returns object of type 'IPackageType'
		"SourcePackage": (1610874881, 2, (9, 0), (), "SourcePackage", '{9253A04D-448B-459A-AF00-BC956F499198}'),
		# Method 'TargetPackage' returns object of type 'IPackageType'
		"TargetPackage": (1610874882, 2, (9, 0), (), "TargetPackage", '{9253A04D-448B-459A-AF00-BC956F499198}'),
	}
	_prop_map_put_ = {
	}

	ClearanceType: str # read_only
	Comments: str # ICommentsMutable; read_only
	Constraints: str # IConstraintsMutable; read_only
	Name: str # read_only
	ObjectType: str # read_only
	Objects: str # IObjects; read_only
	Parent: str # IObject; read_only
	SourcePackage: str # IPackageType; read_only
	TargetPackage: str # IPackageType; read_only

	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
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

class IPackageClearances(DispatchBaseClass):
	CLSID = IID('{B5A4D7C8-1D7D-42CB-8E1D-508B0BD67DCC}')
	coclass_clsid = IID('{8E8E5C86-7002-4197-9495-56C1B7BC5603}')

	# Result is of type IPackageClearance
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the package clearance of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{240DA68C-6822-4B65-A4B3-8E7AB10B66AE}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the package clearance of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{240DA68C-6822-4B65-A4B3-8E7AB10B66AE}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{240DA68C-6822-4B65-A4B3-8E7AB10B66AE}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IPackageClearancesMutable(DispatchBaseClass):
	CLSID = IID('{D2CFD11E-A067-4F0F-BE2F-17A9F507040E}')
	coclass_clsid = IID('{258F61A2-1815-4AF5-BC54-FBA8FA6ECF60}')

	# Result is of type IPackageClearance
	def Add(self, p_eType=defaultNamedNotOptArg, p_strName=defaultNamedNotOptArg, p_pSourcePackage=defaultNamedNotOptArg, p_pTargetPackage=defaultNamedNotOptArg
			, p_vSide='Both', p_vDirection='All'):
		'Creates the package clearance of the given parameters and adds it to the collection.'
		return self._ApplyTypes_(1610874880, 1, (9, 32), ((3, 1), (8, 1), (9, 1), (9, 1), (12, 49), (12, 49)), 'Add', '{240DA68C-6822-4B65-A4B3-8E7AB10B66AE}',p_eType
			, p_strName, p_pSourcePackage, p_pTargetPackage, p_vSide, p_vDirection
			)

	def Delete(self, p_vIndex=defaultNamedNotOptArg):
		'Deletes the package clearance of the given index or name and removes it from the collection.'
		return self._oleobj_.InvokeTypes(1610874881, LCID, 1, (24, 0), ((12, 1),),p_vIndex
			)

	# Result is of type IPackageClearance
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the package clearance of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{240DA68C-6822-4B65-A4B3-8E7AB10B66AE}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the package clearance of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{240DA68C-6822-4B65-A4B3-8E7AB10B66AE}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{240DA68C-6822-4B65-A4B3-8E7AB10B66AE}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IPackageType(DispatchBaseClass):
	CLSID = IID('{9253A04D-448B-459A-AF00-BC956F499198}')
	coclass_clsid = IID('{CB10CB0C-DAB8-41C9-AAAB-500CC8C5A398}')

	# Result is of type IConstraintsMutable
	# The method GetConstraints is actually a property, but must be used as a method to correctly pass the arguments
	def GetConstraints(self, p_nConstraintMask=7):
		'Returns the collection of constraints, filtered by EConstraintMask constant.'
		ret = self._oleobj_.InvokeTypes(1610809345, LCID, 2, (9, 0), ((3, 49),),p_nConstraintMask
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetConstraints', '{1DDEC891-7D43-4EE9-9BD4-63772C577150}')
		return ret

	# Result is of type IObjects
	# The method GetObjects is actually a property, but must be used as a method to correctly pass the arguments
	def GetObjects(self, p_eObjectType=0):
		'Returns the collection of child objects, filtered by EObjectType constant.'
		ret = self._oleobj_.InvokeTypes(1610809347, LCID, 2, (9, 0), ((3, 49),),p_eObjectType
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjects', '{44747797-9642-483B-AB9C-6AE0A1899549}')
		return ret

	# Result is of type IPackageClearances
	# The method GetPackageClearances is actually a property, but must be used as a method to correctly pass the arguments
	def GetPackageClearances(self, p_nClearanceMask=3):
		'Returns the collection of all package clearances which the package type is assigned to, filtered by EClearanceMask constant.'
		ret = self._oleobj_.InvokeTypes(1610874880, LCID, 2, (9, 0), ((3, 49),),p_nClearanceMask
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetPackageClearances', '{B5A4D7C8-1D7D-42CB-8E1D-508B0BD67DCC}')
		return ret

	def IsDefault(self):
		'Returns true if the object is default and cannot be deleted.'
		return self._oleobj_.InvokeTypes(1610743811, LCID, 1, (11, 0), (),)

	def IsValid(self):
		'Returns true if the object is still valid.'
		return self._oleobj_.InvokeTypes(1610743810, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		# Method 'Comments' returns object of type 'ICommentsMutable'
		"Comments": (1610809346, 2, (9, 0), (), "Comments", '{23FAC1D8-2578-42BC-9F65-F04930FB6489}'),
		# Method 'Constraints' returns object of type 'IConstraintsMutable'
		"Constraints": (1610809345, 2, (9, 0), ((3, 49),), "Constraints", '{1DDEC891-7D43-4EE9-9BD4-63772C577150}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
		"ObjectType": (1610809344, 2, (3, 0), (), "ObjectType", None),
		# Method 'Objects' returns object of type 'IObjects'
		"Objects": (1610809347, 2, (9, 0), ((3, 49),), "Objects", '{44747797-9642-483B-AB9C-6AE0A1899549}'),
		# Method 'PackageClearances' returns object of type 'IPackageClearances'
		"PackageClearances": (1610874880, 2, (9, 0), ((3, 49),), "PackageClearances", '{B5A4D7C8-1D7D-42CB-8E1D-508B0BD67DCC}'),
		# Method 'Parent' returns object of type 'IObject'
		"Parent": (1610743809, 2, (9, 0), (), "Parent", '{7A5D1A08-B723-4929-BB46-A801DC642EB6}'),
	}
	_prop_map_put_ = {
	}

	Comments: str # ICommentsMutable; read_only
	Constraints: str # IConstraintsMutable; read_only
	Name: str # read_only
	ObjectType: str # read_only
	Objects: str # IObjects; read_only
	PackageClearances: str # IPackageClearances; read_only
	Parent: str # IObject; read_only

	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
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

class IPackageTypes(DispatchBaseClass):
	CLSID = IID('{4536460C-7AFD-40EE-ADED-BBE2D068ECC8}')
	coclass_clsid = IID('{16AC6FAA-65B2-4B25-A3A3-EA0203A483FF}')

	# Result is of type IPackageType
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the package type of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{9253A04D-448B-459A-AF00-BC956F499198}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the package type of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{9253A04D-448B-459A-AF00-BC956F499198}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{9253A04D-448B-459A-AF00-BC956F499198}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IPackageTypesMutable(DispatchBaseClass):
	CLSID = IID('{EA65AC00-04E5-42F6-AC61-7FA81534926F}')
	coclass_clsid = IID('{5515A13F-6AFA-45BA-BA6F-C291928DE332}')

	# Result is of type IPackageType
	def Add(self, p_strName=defaultNamedNotOptArg):
		'Creates the package type of the given name and adds it to the collection.'
		ret = self._oleobj_.InvokeTypes(1610874880, LCID, 1, (9, 0), ((8, 1),),p_strName
			)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{9253A04D-448B-459A-AF00-BC956F499198}')
		return ret

	def Delete(self, p_vIndex=defaultNamedNotOptArg):
		'Deletes the package type of the given index or name and removes it from the collection.'
		return self._oleobj_.InvokeTypes(1610874881, LCID, 1, (24, 0), ((12, 1),),p_vIndex
			)

	# Result is of type IPackageType
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the package type of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{9253A04D-448B-459A-AF00-BC956F499198}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the package type of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{9253A04D-448B-459A-AF00-BC956F499198}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{9253A04D-448B-459A-AF00-BC956F499198}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IParallelismRule(DispatchBaseClass):
	CLSID = IID('{A11D8E06-CE97-402B-AFD5-D75BACE22E1A}')
	coclass_clsid = IID('{A73969C5-E0DA-45BA-BAB3-DDFCF3BE6FE8}')

	# Result is of type IConstraintsMutable
	# The method GetConstraints is actually a property, but must be used as a method to correctly pass the arguments
	def GetConstraints(self, p_nConstraintMask=7):
		'Returns the collection of constraints, filtered by EConstraintMask constant.'
		ret = self._oleobj_.InvokeTypes(1610809345, LCID, 2, (9, 0), ((3, 49),),p_nConstraintMask
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetConstraints', '{1DDEC891-7D43-4EE9-9BD4-63772C577150}')
		return ret

	# Result is of type INoiseRules
	# The method GetNoiseRules is actually a property, but must be used as a method to correctly pass the arguments
	def GetNoiseRules(self, p_nNoiseRuleMask=3):
		'Returns the collection of noise rules, filtered by ENoiseRuleMask constant.'
		ret = self._oleobj_.InvokeTypes(1610874881, LCID, 2, (9, 0), ((3, 49),),p_nNoiseRuleMask
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetNoiseRules', '{ED063FFC-209C-48D7-8D59-6677873C9A7A}')
		return ret

	# Result is of type IObjects
	# The method GetObjects is actually a property, but must be used as a method to correctly pass the arguments
	def GetObjects(self, p_eObjectType=0):
		'Returns the collection of child objects, filtered by EObjectType constant.'
		ret = self._oleobj_.InvokeTypes(1610809347, LCID, 2, (9, 0), ((3, 49),),p_eObjectType
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjects', '{44747797-9642-483B-AB9C-6AE0A1899549}')
		return ret

	# Result is of type IParallelismRuleSegmentsMutable
	# The method GetSegments is actually a property, but must be used as a method to correctly pass the arguments
	def GetSegments(self, p_nParallelismRuleSegmentMask=3):
		'Returns the collection of parallelism rule segments, filtered by EParallelismRuleSegmentMask constant.'
		ret = self._oleobj_.InvokeTypes(1610874882, LCID, 2, (9, 0), ((3, 49),),p_nParallelismRuleSegmentMask
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetSegments', '{DEB98723-9BE8-482E-A482-E511BA818C2C}')
		return ret

	def IsDefault(self):
		'Returns true if the object is default and cannot be deleted.'
		return self._oleobj_.InvokeTypes(1610743811, LCID, 1, (11, 0), (),)

	def IsValid(self):
		'Returns true if the object is still valid.'
		return self._oleobj_.InvokeTypes(1610743810, LCID, 1, (11, 0), (),)

	def Rename(self, p_strName=defaultNamedNotOptArg):
		'Changes the name of the object.'
		return self._oleobj_.InvokeTypes(1610874880, LCID, 1, (24, 0), ((8, 1),),p_strName
			)

	_prop_map_get_ = {
		# Method 'Comments' returns object of type 'ICommentsMutable'
		"Comments": (1610809346, 2, (9, 0), (), "Comments", '{23FAC1D8-2578-42BC-9F65-F04930FB6489}'),
		# Method 'Constraints' returns object of type 'IConstraintsMutable'
		"Constraints": (1610809345, 2, (9, 0), ((3, 49),), "Constraints", '{1DDEC891-7D43-4EE9-9BD4-63772C577150}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
		# Method 'NoiseRules' returns object of type 'INoiseRules'
		"NoiseRules": (1610874881, 2, (9, 0), ((3, 49),), "NoiseRules", '{ED063FFC-209C-48D7-8D59-6677873C9A7A}'),
		"ObjectType": (1610809344, 2, (3, 0), (), "ObjectType", None),
		# Method 'Objects' returns object of type 'IObjects'
		"Objects": (1610809347, 2, (9, 0), ((3, 49),), "Objects", '{44747797-9642-483B-AB9C-6AE0A1899549}'),
		# Method 'Parent' returns object of type 'IObject'
		"Parent": (1610743809, 2, (9, 0), (), "Parent", '{7A5D1A08-B723-4929-BB46-A801DC642EB6}'),
		# Method 'Segments' returns object of type 'IParallelismRuleSegmentsMutable'
		"Segments": (1610874882, 2, (9, 0), ((3, 49),), "Segments", '{DEB98723-9BE8-482E-A482-E511BA818C2C}'),
	}
	_prop_map_put_ = {
	}

	Comments: str # ICommentsMutable; read_only
	Constraints: str # IConstraintsMutable; read_only
	Name: str # read_only
	NoiseRules: str # INoiseRules; read_only
	ObjectType: str # read_only
	Objects: str # IObjects; read_only
	Parent: str # IObject; read_only
	Segments: str # IParallelismRuleSegmentsMutable; read_only

	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
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

class IParallelismRuleSegment(DispatchBaseClass):
	CLSID = IID('{C391FA67-1209-4DD6-BD23-9D3DD7332651}')
	coclass_clsid = IID('{A5CBB258-CAC7-4150-A5FE-61B8027641DF}')

	# Result is of type IConstraintsMutable
	# The method GetConstraints is actually a property, but must be used as a method to correctly pass the arguments
	def GetConstraints(self, p_nConstraintMask=7):
		'Returns the collection of constraints, filtered by EConstraintMask constant.'
		ret = self._oleobj_.InvokeTypes(1610809345, LCID, 2, (9, 0), ((3, 49),),p_nConstraintMask
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetConstraints', '{1DDEC891-7D43-4EE9-9BD4-63772C577150}')
		return ret

	# Result is of type IObjects
	# The method GetObjects is actually a property, but must be used as a method to correctly pass the arguments
	def GetObjects(self, p_eObjectType=0):
		'Returns the collection of child objects, filtered by EObjectType constant.'
		ret = self._oleobj_.InvokeTypes(1610809347, LCID, 2, (9, 0), ((3, 49),),p_eObjectType
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjects', '{44747797-9642-483B-AB9C-6AE0A1899549}')
		return ret

	def IsDefault(self):
		'Returns true if the object is default and cannot be deleted.'
		return self._oleobj_.InvokeTypes(1610743811, LCID, 1, (11, 0), (),)

	def IsValid(self):
		'Returns true if the object is still valid.'
		return self._oleobj_.InvokeTypes(1610743810, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		# Method 'Comments' returns object of type 'ICommentsMutable'
		"Comments": (1610809346, 2, (9, 0), (), "Comments", '{23FAC1D8-2578-42BC-9F65-F04930FB6489}'),
		# Method 'Constraints' returns object of type 'IConstraintsMutable'
		"Constraints": (1610809345, 2, (9, 0), ((3, 49),), "Constraints", '{1DDEC891-7D43-4EE9-9BD4-63772C577150}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
		"ObjectType": (1610809344, 2, (3, 0), (), "ObjectType", None),
		# Method 'Objects' returns object of type 'IObjects'
		"Objects": (1610809347, 2, (9, 0), ((3, 49),), "Objects", '{44747797-9642-483B-AB9C-6AE0A1899549}'),
		# Method 'Parent' returns object of type 'IObject'
		"Parent": (1610743809, 2, (9, 0), (), "Parent", '{7A5D1A08-B723-4929-BB46-A801DC642EB6}'),
		"SegmentType": (1610874880, 2, (3, 0), (), "SegmentType", None),
	}
	_prop_map_put_ = {
	}

	Comments: str # ICommentsMutable; read_only
	Constraints: str # IConstraintsMutable; read_only
	Name: str # read_only
	ObjectType: str # read_only
	Objects: str # IObjects; read_only
	Parent: str # IObject; read_only
	SegmentType: str # read_only

	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
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

class IParallelismRuleSegments(DispatchBaseClass):
	CLSID = IID('{201C826A-8C6C-4172-931F-92F9208F3717}')
	coclass_clsid = IID('{7689BAC5-FCD4-4523-B7F7-693B529238D9}')

	# Result is of type IParallelismRuleSegment
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the parallelism rule segment of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{C391FA67-1209-4DD6-BD23-9D3DD7332651}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the parallelism rule segment of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{C391FA67-1209-4DD6-BD23-9D3DD7332651}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{C391FA67-1209-4DD6-BD23-9D3DD7332651}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IParallelismRuleSegmentsMutable(DispatchBaseClass):
	CLSID = IID('{DEB98723-9BE8-482E-A482-E511BA818C2C}')
	coclass_clsid = IID('{6E18E1F9-1BCF-4EB3-B700-6A4D68349F92}')

	# Result is of type IParallelismRuleSegment
	def Add(self, p_eParallelismRuleSegmentType=defaultNamedNotOptArg, p_vEdge=defaultNamedNotOptArg, p_vMaxParallelLength=defaultNamedNotOptArg):
		'Creates the parallelism rule segment and adds it to the collection.'
		ret = self._oleobj_.InvokeTypes(1610874880, LCID, 1, (9, 0), ((3, 1), (12, 1), (12, 1)),p_eParallelismRuleSegmentType
			, p_vEdge, p_vMaxParallelLength)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{C391FA67-1209-4DD6-BD23-9D3DD7332651}')
		return ret

	def Delete(self, p_vIndex=defaultNamedNotOptArg):
		'Deletes the parallelism rule segment of the given index or name and removes it from the collection.'
		return self._oleobj_.InvokeTypes(1610874881, LCID, 1, (24, 0), ((12, 1),),p_vIndex
			)

	# Result is of type IParallelismRuleSegment
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the parallelism rule segment of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{C391FA67-1209-4DD6-BD23-9D3DD7332651}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the parallelism rule segment of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{C391FA67-1209-4DD6-BD23-9D3DD7332651}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{C391FA67-1209-4DD6-BD23-9D3DD7332651}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IParallelismRules(DispatchBaseClass):
	CLSID = IID('{595C88AE-5AAA-431C-97BD-5B3C181097EF}')
	coclass_clsid = IID('{2ABDB9DD-E0F6-4344-B4C8-EF2E68B91DDC}')

	# Result is of type IParallelismRule
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the parallelism rule of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{A11D8E06-CE97-402B-AFD5-D75BACE22E1A}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the parallelism rule of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{A11D8E06-CE97-402B-AFD5-D75BACE22E1A}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{A11D8E06-CE97-402B-AFD5-D75BACE22E1A}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IParallelismRulesMutable(DispatchBaseClass):
	CLSID = IID('{E37D92BA-6E24-45E0-859C-43A40855C3AD}')
	coclass_clsid = IID('{DD6F53A1-D9F2-4E92-AD84-81C15D262F16}')

	# Result is of type IParallelismRule
	def Add(self, p_pName=defaultNamedNotOptArg):
		'Creates the parallelism rule and adds it to the collection.'
		ret = self._oleobj_.InvokeTypes(1610874880, LCID, 1, (9, 0), ((8, 1),),p_pName
			)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{A11D8E06-CE97-402B-AFD5-D75BACE22E1A}')
		return ret

	def Delete(self, p_vIndex=defaultNamedNotOptArg):
		'Deletes the parallelism rule of the given index or name and removes it from the collection.'
		return self._oleobj_.InvokeTypes(1610874881, LCID, 1, (24, 0), ((12, 1),),p_vIndex
			)

	# Result is of type IParallelismRule
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the parallelism rule of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{A11D8E06-CE97-402B-AFD5-D75BACE22E1A}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the parallelism rule of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{A11D8E06-CE97-402B-AFD5-D75BACE22E1A}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{A11D8E06-CE97-402B-AFD5-D75BACE22E1A}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IPart(DispatchBaseClass):
	CLSID = IID('{2D3374B6-ED6A-4024-AC29-ACF03A09B7C5}')
	coclass_clsid = IID('{17DCD0D5-D0AD-41C1-924E-F6237BF78120}')

	# Result is of type IConstraintsMutable
	# The method GetConstraints is actually a property, but must be used as a method to correctly pass the arguments
	def GetConstraints(self, p_nConstraintMask=7):
		'Returns the collection of constraints, filtered by EConstraintMask constant.'
		ret = self._oleobj_.InvokeTypes(1610809345, LCID, 2, (9, 0), ((3, 49),),p_nConstraintMask
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetConstraints', '{1DDEC891-7D43-4EE9-9BD4-63772C577150}')
		return ret

	# Result is of type IObjects
	# The method GetObjects is actually a property, but must be used as a method to correctly pass the arguments
	def GetObjects(self, p_eObjectType=0):
		'Returns the collection of child objects, filtered by EObjectType constant.'
		ret = self._oleobj_.InvokeTypes(1610809347, LCID, 2, (9, 0), ((3, 49),),p_eObjectType
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjects', '{44747797-9642-483B-AB9C-6AE0A1899549}')
		return ret

	def IsDefault(self):
		'Returns true if the object is default and cannot be deleted.'
		return self._oleobj_.InvokeTypes(1610743811, LCID, 1, (11, 0), (),)

	def IsValid(self):
		'Returns true if the object is still valid.'
		return self._oleobj_.InvokeTypes(1610743810, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		# Method 'Comments' returns object of type 'ICommentsMutable'
		"Comments": (1610809346, 2, (9, 0), (), "Comments", '{23FAC1D8-2578-42BC-9F65-F04930FB6489}'),
		# Method 'Components' returns object of type 'IComponentsMutable'
		"Components": (1610874882, 2, (9, 0), (), "Components", '{E010B178-C036-4BDE-815F-9B48CE213D1E}'),
		# Method 'Constraints' returns object of type 'IConstraintsMutable'
		"Constraints": (1610809345, 2, (9, 0), ((3, 49),), "Constraints", '{1DDEC891-7D43-4EE9-9BD4-63772C577150}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
		"ObjectType": (1610809344, 2, (3, 0), (), "ObjectType", None),
		# Method 'Objects' returns object of type 'IObjects'
		"Objects": (1610809347, 2, (9, 0), ((3, 49),), "Objects", '{44747797-9642-483B-AB9C-6AE0A1899549}'),
		# Method 'Parent' returns object of type 'IObject'
		"Parent": (1610743809, 2, (9, 0), (), "Parent", '{7A5D1A08-B723-4929-BB46-A801DC642EB6}'),
		# Method 'PartPinPairs' returns object of type 'IPartPinPairsMutable'
		"PartPinPairs": (1610874881, 2, (9, 0), (), "PartPinPairs", '{7DA3F078-E3B2-4436-A267-6FC09F25AB19}'),
		# Method 'PartPins' returns object of type 'IPartPinsMutable'
		"PartPins": (1610874880, 2, (9, 0), (), "PartPins", '{8596DD5E-2C99-4DED-9A1F-D9067D3D34DB}'),
	}
	_prop_map_put_ = {
	}

	Comments: str # ICommentsMutable; read_only
	Components: str # IComponentsMutable; read_only
	Constraints: str # IConstraintsMutable; read_only
	Name: str # read_only
	ObjectType: str # read_only
	Objects: str # IObjects; read_only
	Parent: str # IObject; read_only
	PartPinPairs: str # IPartPinPairsMutable; read_only
	PartPins: str # IPartPinsMutable; read_only

	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
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

class IPartPin(DispatchBaseClass):
	CLSID = IID('{A6EC1810-AC7F-4B10-AA00-BBC2FCB7C929}')
	coclass_clsid = IID('{2FAE361D-F475-44EC-B87C-F58184D8DFA1}')

	# Result is of type IConstraintsMutable
	# The method GetConstraints is actually a property, but must be used as a method to correctly pass the arguments
	def GetConstraints(self, p_nConstraintMask=7):
		'Returns the collection of constraints, filtered by EConstraintMask constant.'
		ret = self._oleobj_.InvokeTypes(1610809345, LCID, 2, (9, 0), ((3, 49),),p_nConstraintMask
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetConstraints', '{1DDEC891-7D43-4EE9-9BD4-63772C577150}')
		return ret

	# Result is of type IObjects
	# The method GetObjects is actually a property, but must be used as a method to correctly pass the arguments
	def GetObjects(self, p_eObjectType=0):
		'Returns the collection of child objects, filtered by EObjectType constant.'
		ret = self._oleobj_.InvokeTypes(1610809347, LCID, 2, (9, 0), ((3, 49),),p_eObjectType
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjects', '{44747797-9642-483B-AB9C-6AE0A1899549}')
		return ret

	def IsDefault(self):
		'Returns true if the object is default and cannot be deleted.'
		return self._oleobj_.InvokeTypes(1610743811, LCID, 1, (11, 0), (),)

	def IsValid(self):
		'Returns true if the object is still valid.'
		return self._oleobj_.InvokeTypes(1610743810, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		# Method 'Comments' returns object of type 'ICommentsMutable'
		"Comments": (1610809346, 2, (9, 0), (), "Comments", '{23FAC1D8-2578-42BC-9F65-F04930FB6489}'),
		# Method 'Constraints' returns object of type 'IConstraintsMutable'
		"Constraints": (1610809345, 2, (9, 0), ((3, 49),), "Constraints", '{1DDEC891-7D43-4EE9-9BD4-63772C577150}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
		"ObjectType": (1610809344, 2, (3, 0), (), "ObjectType", None),
		# Method 'Objects' returns object of type 'IObjects'
		"Objects": (1610809347, 2, (9, 0), ((3, 49),), "Objects", '{44747797-9642-483B-AB9C-6AE0A1899549}'),
		# Method 'Parent' returns object of type 'IObject'
		"Parent": (1610743809, 2, (9, 0), (), "Parent", '{7A5D1A08-B723-4929-BB46-A801DC642EB6}'),
		# Method 'PartPinPairs' returns object of type 'IPartPinPairs'
		"PartPinPairs": (1610874880, 2, (9, 0), (), "PartPinPairs", '{44495392-B0D3-496F-8925-A5F0710C3A67}'),
		# Method 'Pins' returns object of type 'IPins'
		"Pins": (1610874881, 2, (9, 0), (), "Pins", '{3F1B4618-0423-42B9-A741-72E65CE0E573}'),
	}
	_prop_map_put_ = {
	}

	Comments: str # ICommentsMutable; read_only
	Constraints: str # IConstraintsMutable; read_only
	Name: str # read_only
	ObjectType: str # read_only
	Objects: str # IObjects; read_only
	Parent: str # IObject; read_only
	PartPinPairs: str # IPartPinPairs; read_only
	Pins: str # IPins; read_only

	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
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

class IPartPinPair(DispatchBaseClass):
	CLSID = IID('{FE3B36FE-C912-41F3-88EA-542F43253414}')
	coclass_clsid = IID('{2C8C8556-C2B6-449B-88A2-9030268296AC}')

	# Result is of type IConstraintsMutable
	# The method GetConstraints is actually a property, but must be used as a method to correctly pass the arguments
	def GetConstraints(self, p_nConstraintMask=7):
		'Returns the collection of constraints, filtered by EConstraintMask constant.'
		ret = self._oleobj_.InvokeTypes(1610809345, LCID, 2, (9, 0), ((3, 49),),p_nConstraintMask
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetConstraints', '{1DDEC891-7D43-4EE9-9BD4-63772C577150}')
		return ret

	# Result is of type IObjects
	# The method GetObjects is actually a property, but must be used as a method to correctly pass the arguments
	def GetObjects(self, p_eObjectType=0):
		'Returns the collection of child objects, filtered by EObjectType constant.'
		ret = self._oleobj_.InvokeTypes(1610809347, LCID, 2, (9, 0), ((3, 49),),p_eObjectType
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjects', '{44747797-9642-483B-AB9C-6AE0A1899549}')
		return ret

	def IsDefault(self):
		'Returns true if the object is default and cannot be deleted.'
		return self._oleobj_.InvokeTypes(1610743811, LCID, 1, (11, 0), (),)

	def IsValid(self):
		'Returns true if the object is still valid.'
		return self._oleobj_.InvokeTypes(1610743810, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		# Method 'Comments' returns object of type 'ICommentsMutable'
		"Comments": (1610809346, 2, (9, 0), (), "Comments", '{23FAC1D8-2578-42BC-9F65-F04930FB6489}'),
		# Method 'Constraints' returns object of type 'IConstraintsMutable'
		"Constraints": (1610809345, 2, (9, 0), ((3, 49),), "Constraints", '{1DDEC891-7D43-4EE9-9BD4-63772C577150}'),
		# Method 'FirstPartPin' returns object of type 'IPartPin'
		"FirstPartPin": (1610874880, 2, (9, 0), (), "FirstPartPin", '{A6EC1810-AC7F-4B10-AA00-BBC2FCB7C929}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
		"ObjectType": (1610809344, 2, (3, 0), (), "ObjectType", None),
		# Method 'Objects' returns object of type 'IObjects'
		"Objects": (1610809347, 2, (9, 0), ((3, 49),), "Objects", '{44747797-9642-483B-AB9C-6AE0A1899549}'),
		# Method 'Parent' returns object of type 'IObject'
		"Parent": (1610743809, 2, (9, 0), (), "Parent", '{7A5D1A08-B723-4929-BB46-A801DC642EB6}'),
		# Method 'PartPins' returns object of type 'IPartPins'
		"PartPins": (1610874882, 2, (9, 0), (), "PartPins", '{1C51DCE2-A09B-4680-BF6F-9EDAF0C822B8}'),
		# Method 'SecondPartPin' returns object of type 'IPartPin'
		"SecondPartPin": (1610874881, 2, (9, 0), (), "SecondPartPin", '{A6EC1810-AC7F-4B10-AA00-BBC2FCB7C929}'),
	}
	_prop_map_put_ = {
	}

	Comments: str # ICommentsMutable; read_only
	Constraints: str # IConstraintsMutable; read_only
	FirstPartPin: str # IPartPin; read_only
	Name: str # read_only
	ObjectType: str # read_only
	Objects: str # IObjects; read_only
	Parent: str # IObject; read_only
	PartPins: str # IPartPins; read_only
	SecondPartPin: str # IPartPin; read_only

	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
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

class IPartPinPairs(DispatchBaseClass):
	CLSID = IID('{44495392-B0D3-496F-8925-A5F0710C3A67}')
	coclass_clsid = IID('{8FA9F4DB-8EE1-45BB-9B2C-FBD758CCD1A0}')

	# Result is of type IPartPinPair
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the part pin pair of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{FE3B36FE-C912-41F3-88EA-542F43253414}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the part pin pair of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{FE3B36FE-C912-41F3-88EA-542F43253414}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{FE3B36FE-C912-41F3-88EA-542F43253414}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IPartPinPairsMutable(DispatchBaseClass):
	CLSID = IID('{7DA3F078-E3B2-4436-A267-6FC09F25AB19}')
	coclass_clsid = IID('{F86FDE27-D779-458D-A51D-56FC1186F818}')

	# Result is of type IPartPinPair
	def Add(self, p_pPartPin1=defaultNamedNotOptArg, p_pPartPin2=defaultNamedNotOptArg):
		'Creates the part pin pair and adds it to the collection.'
		ret = self._oleobj_.InvokeTypes(1610874880, LCID, 1, (9, 0), ((9, 1), (9, 1)),p_pPartPin1
			, p_pPartPin2)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{FE3B36FE-C912-41F3-88EA-542F43253414}')
		return ret

	def Delete(self, p_vIndex=defaultNamedNotOptArg):
		'Deletes the part pin pair of the given index or name and removes it from the collection.'
		return self._oleobj_.InvokeTypes(1610874881, LCID, 1, (24, 0), ((12, 1),),p_vIndex
			)

	# Result is of type IPartPinPair
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the part pin pair of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{FE3B36FE-C912-41F3-88EA-542F43253414}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the part pin pair of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{FE3B36FE-C912-41F3-88EA-542F43253414}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{FE3B36FE-C912-41F3-88EA-542F43253414}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IPartPins(DispatchBaseClass):
	CLSID = IID('{1C51DCE2-A09B-4680-BF6F-9EDAF0C822B8}')
	coclass_clsid = IID('{57320C9B-E888-40E1-B937-7090B95682E3}')

	# Result is of type IPartPin
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the part pin of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{A6EC1810-AC7F-4B10-AA00-BBC2FCB7C929}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the part pin of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{A6EC1810-AC7F-4B10-AA00-BBC2FCB7C929}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{A6EC1810-AC7F-4B10-AA00-BBC2FCB7C929}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IPartPinsMutable(DispatchBaseClass):
	CLSID = IID('{8596DD5E-2C99-4DED-9A1F-D9067D3D34DB}')
	coclass_clsid = IID('{6BD38466-57D0-4836-A566-60674280EBC8}')

	# Result is of type IPartPin
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the part pin of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{A6EC1810-AC7F-4B10-AA00-BBC2FCB7C929}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the part pin of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{A6EC1810-AC7F-4B10-AA00-BBC2FCB7C929}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{A6EC1810-AC7F-4B10-AA00-BBC2FCB7C929}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IParts(DispatchBaseClass):
	CLSID = IID('{CD4E27CD-B11C-4EDD-B1BE-6D1996D3A4F1}')
	coclass_clsid = IID('{902446D5-4B16-4320-91AE-682169A4B7A3}')

	# Result is of type IPart
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the part of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{2D3374B6-ED6A-4024-AC29-ACF03A09B7C5}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the part of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{2D3374B6-ED6A-4024-AC29-ACF03A09B7C5}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{2D3374B6-ED6A-4024-AC29-ACF03A09B7C5}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IPartsMutable(DispatchBaseClass):
	CLSID = IID('{965F3ED3-C357-4CD4-8778-9B61B12D5D24}')
	coclass_clsid = IID('{1C06D4C9-421F-47C1-B4F0-86179BDE6A44}')

	# Result is of type IPart
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the part of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{2D3374B6-ED6A-4024-AC29-ACF03A09B7C5}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the part of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{2D3374B6-ED6A-4024-AC29-ACF03A09B7C5}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{2D3374B6-ED6A-4024-AC29-ACF03A09B7C5}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IPhysicalRules(DispatchBaseClass):
	CLSID = IID('{F1F96334-F630-42BA-A3F4-2D314D51D535}')
	coclass_clsid = IID('{D902C696-50D9-4383-BC8C-595FDA5434F1}')

	# Result is of type IClassClearancesMutable
	# The method GetClassClearances is actually a property, but must be used as a method to correctly pass the arguments
	def GetClassClearances(self, p_nClassClearancesMask=3):
		'Returns the collection of all class clearances, filtered by EClassClearancesMask constant.'
		ret = self._oleobj_.InvokeTypes(1610743810, LCID, 2, (9, 0), ((3, 49),),p_nClassClearancesMask
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetClassClearances', '{FA648CF5-E9A3-4841-AD76-BD4BCD55DF45}')
		return ret

	# Result is of type IGeneralClearancesMutable
	# The method GetGeneralClearances is actually a property, but must be used as a method to correctly pass the arguments
	def GetGeneralClearances(self, p_nClearanceMask=3):
		'Returns the collection of all general clearances, filtered by EClearanceMask constant.'
		ret = self._oleobj_.InvokeTypes(1610743811, LCID, 2, (9, 0), ((3, 49),),p_nClearanceMask
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetGeneralClearances', '{BC62A287-210A-4466-A894-5ACB1F4E0E25}')
		return ret

	# Result is of type IPackageClearancesMutable
	# The method GetPackageClearances is actually a property, but must be used as a method to correctly pass the arguments
	def GetPackageClearances(self, p_nClearancesMask=3):
		'Returns the collection of all package clearances, filtered by EClearanceMask constant.'
		ret = self._oleobj_.InvokeTypes(1610743812, LCID, 2, (9, 0), ((3, 49),),p_nClearancesMask
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetPackageClearances', '{D2CFD11E-A067-4F0F-BE2F-17A9F507040E}')
		return ret

	_prop_map_get_ = {
		# Method 'ClassClearances' returns object of type 'IClassClearancesMutable'
		"ClassClearances": (1610743810, 2, (9, 0), ((3, 49),), "ClassClearances", '{FA648CF5-E9A3-4841-AD76-BD4BCD55DF45}'),
		# Method 'GeneralClearances' returns object of type 'IGeneralClearancesMutable'
		"GeneralClearances": (1610743811, 2, (9, 0), ((3, 49),), "GeneralClearances", '{BC62A287-210A-4466-A894-5ACB1F4E0E25}'),
		# Method 'PackageClearances' returns object of type 'IPackageClearancesMutable'
		"PackageClearances": (1610743812, 2, (9, 0), ((3, 49),), "PackageClearances", '{D2CFD11E-A067-4F0F-BE2F-17A9F507040E}'),
		# Method 'Schemes' returns object of type 'ISchemesMutable'
		"Schemes": (1610743808, 2, (9, 0), (), "Schemes", '{C868C166-9607-4506-AEF9-5AE4FB428F95}'),
		# Method 'ZAxisClearanceRules' returns object of type 'IClearanceRulesMutable'
		"ZAxisClearanceRules": (1610743809, 2, (9, 0), (), "ZAxisClearanceRules", '{088425F1-88A0-4675-B9B9-D6FBC0454CF3}'),
	}
	_prop_map_put_ = {
	}

	ClassClearances: str # IClassClearancesMutable; read_only
	GeneralClearances: str # IGeneralClearancesMutable; read_only
	PackageClearances: str # IPackageClearancesMutable; read_only
	Schemes: str # ISchemesMutable; read_only
	ZAxisClearanceRules: str # IClearanceRulesMutable; read_only

	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IPin(DispatchBaseClass):
	CLSID = IID('{1B2620CF-90B0-4E6B-9CDF-A1799A578FDC}')
	coclass_clsid = IID('{BFB658F1-2CC5-4D15-B3F8-077FC1497BC4}')

	# Result is of type IConstraintsMutable
	# The method GetConstraints is actually a property, but must be used as a method to correctly pass the arguments
	def GetConstraints(self, p_nConstraintMask=7):
		'Returns the collection of constraints, filtered by EConstraintMask constant.'
		ret = self._oleobj_.InvokeTypes(1610809345, LCID, 2, (9, 0), ((3, 49),),p_nConstraintMask
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetConstraints', '{1DDEC891-7D43-4EE9-9BD4-63772C577150}')
		return ret

	# Result is of type IObjects
	# The method GetObjects is actually a property, but must be used as a method to correctly pass the arguments
	def GetObjects(self, p_eObjectType=0):
		'Returns the collection of child objects, filtered by EObjectType constant.'
		ret = self._oleobj_.InvokeTypes(1610809347, LCID, 2, (9, 0), ((3, 49),),p_eObjectType
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjects', '{44747797-9642-483B-AB9C-6AE0A1899549}')
		return ret

	def IsDefault(self):
		'Returns true if the object is default and cannot be deleted.'
		return self._oleobj_.InvokeTypes(1610743811, LCID, 1, (11, 0), (),)

	def IsValid(self):
		'Returns true if the object is still valid.'
		return self._oleobj_.InvokeTypes(1610743810, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		# Method 'Comments' returns object of type 'ICommentsMutable'
		"Comments": (1610809346, 2, (9, 0), (), "Comments", '{23FAC1D8-2578-42BC-9F65-F04930FB6489}'),
		# Method 'Constraints' returns object of type 'IConstraintsMutable'
		"Constraints": (1610809345, 2, (9, 0), ((3, 49),), "Constraints", '{1DDEC891-7D43-4EE9-9BD4-63772C577150}'),
		# Method 'FromTos' returns object of type 'IFromTos'
		"FromTos": (1610874882, 2, (9, 0), (), "FromTos", '{9C2F6146-F58D-43EC-B1B4-F0FF99B33E31}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
		# Method 'Net' returns object of type 'INet'
		"Net": (1610874881, 2, (9, 0), (), "Net", '{48420240-E6BB-423E-9FD3-F3E4687E1452}'),
		"ObjectType": (1610809344, 2, (3, 0), (), "ObjectType", None),
		# Method 'Objects' returns object of type 'IObjects'
		"Objects": (1610809347, 2, (9, 0), ((3, 49),), "Objects", '{44747797-9642-483B-AB9C-6AE0A1899549}'),
		# Method 'Parent' returns object of type 'IObject'
		"Parent": (1610743809, 2, (9, 0), (), "Parent", '{7A5D1A08-B723-4929-BB46-A801DC642EB6}'),
		# Method 'PartPin' returns object of type 'IPartPin'
		"PartPin": (1610874885, 2, (9, 0), (), "PartPin", '{A6EC1810-AC7F-4B10-AA00-BBC2FCB7C929}'),
		# Method 'PinPairs' returns object of type 'IPinPairs'
		"PinPairs": (1610874883, 2, (9, 0), (), "PinPairs", '{AE314BDB-B6CC-4DD0-B514-1A525DA682D6}'),
		# Method 'PinSets' returns object of type 'IPinSets'
		"PinSets": (1610874884, 2, (9, 0), (), "PinSets", '{B80F7CDC-6D14-471E-9983-979FF0059B5A}'),
		"PinType": (1610874880, 2, (3, 0), (), "PinType", None),
	}
	_prop_map_put_ = {
	}

	Comments: str # ICommentsMutable; read_only
	Constraints: str # IConstraintsMutable; read_only
	FromTos: str # IFromTos; read_only
	Name: str # read_only
	Net: str # INet; read_only
	ObjectType: str # read_only
	Objects: str # IObjects; read_only
	Parent: str # IObject; read_only
	PartPin: str # IPartPin; read_only
	PinPairs: str # IPinPairs; read_only
	PinSets: str # IPinSets; read_only
	PinType: str # read_only

	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
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

class IPinPair(DispatchBaseClass):
	CLSID = IID('{DAE2F804-60E5-4B5F-96F0-FB5585334EAB}')
	coclass_clsid = IID('{F2284F80-6E4A-4945-BB5F-69FED15C9C5A}')

	# Result is of type IConstraintsMutable
	# The method GetConstraints is actually a property, but must be used as a method to correctly pass the arguments
	def GetConstraints(self, p_nConstraintMask=7):
		'Returns the collection of constraints, filtered by EConstraintMask constant.'
		ret = self._oleobj_.InvokeTypes(1610809345, LCID, 2, (9, 0), ((3, 49),),p_nConstraintMask
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetConstraints', '{1DDEC891-7D43-4EE9-9BD4-63772C577150}')
		return ret

	# Result is of type IMatchGroups
	# The method GetMatchGroups is actually a property, but must be used as a method to correctly pass the arguments
	def GetMatchGroups(self, p_nMatchGroupMask=3):
		'Returns all match groups related to the pin pair.'
		ret = self._oleobj_.InvokeTypes(1610874885, LCID, 2, (9, 0), ((3, 49),),p_nMatchGroupMask
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetMatchGroups', '{1F460B56-507F-4CA6-B8D7-676CBB2427BD}')
		return ret

	# Result is of type IObjects
	# The method GetObjects is actually a property, but must be used as a method to correctly pass the arguments
	def GetObjects(self, p_eObjectType=0):
		'Returns the collection of child objects, filtered by EObjectType constant.'
		ret = self._oleobj_.InvokeTypes(1610809347, LCID, 2, (9, 0), ((3, 49),),p_eObjectType
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjects', '{44747797-9642-483B-AB9C-6AE0A1899549}')
		return ret

	def IsDefault(self):
		'Returns true if the object is default and cannot be deleted.'
		return self._oleobj_.InvokeTypes(1610743811, LCID, 1, (11, 0), (),)

	def IsValid(self):
		'Returns true if the object is still valid.'
		return self._oleobj_.InvokeTypes(1610743810, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		# Method 'Comments' returns object of type 'ICommentsMutable'
		"Comments": (1610809346, 2, (9, 0), (), "Comments", '{23FAC1D8-2578-42BC-9F65-F04930FB6489}'),
		# Method 'Constraints' returns object of type 'IConstraintsMutable'
		"Constraints": (1610809345, 2, (9, 0), ((3, 49),), "Constraints", '{1DDEC891-7D43-4EE9-9BD4-63772C577150}'),
		"DelayType": (1610874883, 2, (3, 0), (), "DelayType", None),
		# Method 'FirstPin' returns object of type 'IPin'
		"FirstPin": (1610874880, 2, (9, 0), (), "FirstPin", '{1B2620CF-90B0-4E6B-9CDF-A1799A578FDC}'),
		# Method 'Formula' returns object of type 'IFormula'
		"Formula": (1610874886, 2, (9, 0), (), "Formula", '{A59586BA-4C99-4643-B6F8-E42BBF2E00D2}'),
		# Method 'MatchGroups' returns object of type 'IMatchGroups'
		"MatchGroups": (1610874885, 2, (9, 0), ((3, 49),), "MatchGroups", '{1F460B56-507F-4CA6-B8D7-676CBB2427BD}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
		"ObjectType": (1610809344, 2, (3, 0), (), "ObjectType", None),
		# Method 'Objects' returns object of type 'IObjects'
		"Objects": (1610809347, 2, (9, 0), ((3, 49),), "Objects", '{44747797-9642-483B-AB9C-6AE0A1899549}'),
		# Method 'Parent' returns object of type 'IObject'
		"Parent": (1610743809, 2, (9, 0), (), "Parent", '{7A5D1A08-B723-4929-BB46-A801DC642EB6}'),
		# Method 'Pins' returns object of type 'IPins'
		"Pins": (1610874882, 2, (9, 0), (), "Pins", '{3F1B4618-0423-42B9-A741-72E65CE0E573}'),
		# Method 'SecondPin' returns object of type 'IPin'
		"SecondPin": (1610874881, 2, (9, 0), (), "SecondPin", '{1B2620CF-90B0-4E6B-9CDF-A1799A578FDC}'),
	}
	_prop_map_put_ = {
		"DelayType": ((1610874883, LCID, 4, 0),()),
	}

	Comments: str # ICommentsMutable; read_only
	Constraints: str # IConstraintsMutable; read_only
	DelayType: str # read/write
	FirstPin: str # IPin; read_only
	Formula: str # IFormula; read_only
	MatchGroups: str # IMatchGroups; read_only
	Name: str # read_only
	ObjectType: str # read_only
	Objects: str # IObjects; read_only
	Parent: str # IObject; read_only
	Pins: str # IPins; read_only
	SecondPin: str # IPin; read_only

	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
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

class IPinPairs(DispatchBaseClass):
	CLSID = IID('{AE314BDB-B6CC-4DD0-B514-1A525DA682D6}')
	coclass_clsid = IID('{FB7CB482-1529-451F-911B-7BC33EC256BF}')

	# Result is of type IPinPair
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the pin pair of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{DAE2F804-60E5-4B5F-96F0-FB5585334EAB}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the pin pair of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{DAE2F804-60E5-4B5F-96F0-FB5585334EAB}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{DAE2F804-60E5-4B5F-96F0-FB5585334EAB}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IPinPairsMutable(DispatchBaseClass):
	CLSID = IID('{0D52DE96-799A-4660-ACFE-109F34DEE67B}')
	coclass_clsid = IID('{31380624-17C9-4E40-8A0D-826E88AC4589}')

	# Result is of type IPinPair
	def Add(self, p_pPin1=defaultNamedNotOptArg, p_pPin2=defaultNamedNotOptArg):
		'Creates the pin pair and adds it to the collection.'
		ret = self._oleobj_.InvokeTypes(1610874880, LCID, 1, (9, 0), ((9, 1), (9, 1)),p_pPin1
			, p_pPin2)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{DAE2F804-60E5-4B5F-96F0-FB5585334EAB}')
		return ret

	def Delete(self, p_vIndex=defaultNamedNotOptArg):
		'Deletes the pin pair of the given index or name and removes it from the collection.'
		return self._oleobj_.InvokeTypes(1610874883, LCID, 1, (24, 0), ((12, 1),),p_vIndex
			)

	def Insert(self, p_pPinPair=defaultNamedNotOptArg):
		'Inserts the pin pair to the collection.'
		return self._oleobj_.InvokeTypes(1610874881, LCID, 1, (24, 0), ((9, 1),),p_pPinPair
			)

	# Result is of type IPinPair
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the pin pair of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{DAE2F804-60E5-4B5F-96F0-FB5585334EAB}')
		return ret

	def Remove(self, p_vIndex=defaultNamedNotOptArg):
		'Removes the pin pair of the given index or name from the collection.'
		return self._oleobj_.InvokeTypes(1610874882, LCID, 1, (24, 0), ((12, 1),),p_vIndex
			)

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the pin pair of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{DAE2F804-60E5-4B5F-96F0-FB5585334EAB}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{DAE2F804-60E5-4B5F-96F0-FB5585334EAB}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IPinSet(DispatchBaseClass):
	CLSID = IID('{5B8C932F-F283-4D9C-AD70-4B4213109BC3}')
	coclass_clsid = IID('{58AF7426-636E-4771-8BA8-06179F6D3A0B}')

	# Result is of type IConstraintsMutable
	# The method GetConstraints is actually a property, but must be used as a method to correctly pass the arguments
	def GetConstraints(self, p_nConstraintMask=7):
		'Returns the collection of constraints, filtered by EConstraintMask constant.'
		ret = self._oleobj_.InvokeTypes(1610809345, LCID, 2, (9, 0), ((3, 49),),p_nConstraintMask
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetConstraints', '{1DDEC891-7D43-4EE9-9BD4-63772C577150}')
		return ret

	# Result is of type IObjects
	# The method GetObjects is actually a property, but must be used as a method to correctly pass the arguments
	def GetObjects(self, p_eObjectType=0):
		'Returns the collection of child objects, filtered by EObjectType constant.'
		ret = self._oleobj_.InvokeTypes(1610809347, LCID, 2, (9, 0), ((3, 49),),p_eObjectType
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjects', '{44747797-9642-483B-AB9C-6AE0A1899549}')
		return ret

	def IsDefault(self):
		'Returns true if the object is default and cannot be deleted.'
		return self._oleobj_.InvokeTypes(1610743811, LCID, 1, (11, 0), (),)

	def IsValid(self):
		'Returns true if the object is still valid.'
		return self._oleobj_.InvokeTypes(1610743810, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		# Method 'Comments' returns object of type 'ICommentsMutable'
		"Comments": (1610809346, 2, (9, 0), (), "Comments", '{23FAC1D8-2578-42BC-9F65-F04930FB6489}'),
		# Method 'ConnectionPin' returns object of type 'IPin'
		"ConnectionPin": (1610874882, 2, (9, 0), (), "ConnectionPin", '{1B2620CF-90B0-4E6B-9CDF-A1799A578FDC}'),
		# Method 'Constraints' returns object of type 'IConstraintsMutable'
		"Constraints": (1610809345, 2, (9, 0), ((3, 49),), "Constraints", '{1DDEC891-7D43-4EE9-9BD4-63772C577150}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
		"ObjectType": (1610809344, 2, (3, 0), (), "ObjectType", None),
		# Method 'Objects' returns object of type 'IObjects'
		"Objects": (1610809347, 2, (9, 0), ((3, 49),), "Objects", '{44747797-9642-483B-AB9C-6AE0A1899549}'),
		# Method 'Parent' returns object of type 'IObject'
		"Parent": (1610743809, 2, (9, 0), (), "Parent", '{7A5D1A08-B723-4929-BB46-A801DC642EB6}'),
		"PinSetType": (1610874880, 2, (3, 0), (), "PinSetType", None),
		# Method 'Pins' returns object of type 'IPinsMutable'
		"Pins": (1610874881, 2, (9, 0), (), "Pins", '{B034C5D7-24E1-4F6A-836A-7906257DABAA}'),
		# Method 'VirtualPin' returns object of type 'IPin'
		"VirtualPin": (1610874883, 2, (9, 0), (), "VirtualPin", '{1B2620CF-90B0-4E6B-9CDF-A1799A578FDC}'),
	}
	_prop_map_put_ = {
	}

	Comments: str # ICommentsMutable; read_only
	ConnectionPin: str # IPin; read_only
	Constraints: str # IConstraintsMutable; read_only
	Name: str # read_only
	ObjectType: str # read_only
	Objects: str # IObjects; read_only
	Parent: str # IObject; read_only
	PinSetType: str # read_only
	Pins: str # IPinsMutable; read_only
	VirtualPin: str # IPin; read_only

	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
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

class IPinSets(DispatchBaseClass):
	CLSID = IID('{B80F7CDC-6D14-471E-9983-979FF0059B5A}')
	coclass_clsid = IID('{9670C07E-EF9C-4FF8-9DE7-EDEA3B5868A3}')

	# Result is of type IPinSet
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the pin set of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{5B8C932F-F283-4D9C-AD70-4B4213109BC3}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the pin set of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{5B8C932F-F283-4D9C-AD70-4B4213109BC3}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{5B8C932F-F283-4D9C-AD70-4B4213109BC3}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IPinSetsMutable(DispatchBaseClass):
	CLSID = IID('{27E83E75-0024-45DF-92D3-516B20F446C8}')
	coclass_clsid = IID('{EDCACA3C-AF91-401F-970F-CF31FC29E3AE}')

	# Result is of type IPinSet
	def Add(self, p_ePinSetType=defaultNamedNotOptArg, p_pPinsArray=defaultNamedNotOptArg):
		'Creates the pin set and adds it to the collection.'
		ret = self._oleobj_.InvokeTypes(1610874880, LCID, 1, (9, 0), ((3, 1), (16396, 1)),p_ePinSetType
			, p_pPinsArray)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{5B8C932F-F283-4D9C-AD70-4B4213109BC3}')
		return ret

	def Delete(self, p_vIndex=defaultNamedNotOptArg):
		'Deletes the pin set of the given index or name and removes it from the collection.'
		return self._oleobj_.InvokeTypes(1610874881, LCID, 1, (24, 0), ((12, 1),),p_vIndex
			)

	# Result is of type IPinSet
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the pin set of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{5B8C932F-F283-4D9C-AD70-4B4213109BC3}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the pin set of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{5B8C932F-F283-4D9C-AD70-4B4213109BC3}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{5B8C932F-F283-4D9C-AD70-4B4213109BC3}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IPins(DispatchBaseClass):
	CLSID = IID('{3F1B4618-0423-42B9-A741-72E65CE0E573}')
	coclass_clsid = IID('{BEBB09AC-7396-4C74-9423-9BFA9D766B1F}')

	# Result is of type IPin
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the pin of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{1B2620CF-90B0-4E6B-9CDF-A1799A578FDC}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the pin of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{1B2620CF-90B0-4E6B-9CDF-A1799A578FDC}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{1B2620CF-90B0-4E6B-9CDF-A1799A578FDC}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IPinsMutable(DispatchBaseClass):
	CLSID = IID('{B034C5D7-24E1-4F6A-836A-7906257DABAA}')
	coclass_clsid = IID('{F6D6CDD0-C76D-4243-A552-2A37424621A0}')

	def Insert(self, p_pPin=defaultNamedNotOptArg):
		'Inserts the pin to the collection.'
		return self._oleobj_.InvokeTypes(1610874880, LCID, 1, (24, 0), ((9, 1),),p_pPin
			)

	# Result is of type IPin
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the pin of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{1B2620CF-90B0-4E6B-9CDF-A1799A578FDC}')
		return ret

	def Remove(self, p_vIndex=defaultNamedNotOptArg):
		'Removes the pin of the given index or name from the collection.'
		return self._oleobj_.InvokeTypes(1610874881, LCID, 1, (24, 0), ((12, 1),),p_vIndex
			)

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the pin of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{1B2620CF-90B0-4E6B-9CDF-A1799A578FDC}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{1B2620CF-90B0-4E6B-9CDF-A1799A578FDC}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IPowerNets(DispatchBaseClass):
	CLSID = IID('{88AFDE06-B464-4045-8FC0-321DAAB9EDDE}')
	coclass_clsid = IID('{0798D9AB-9C3F-4E6D-8C31-382798093C5B}')

	# Result is of type INet
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the power net of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{48420240-E6BB-423E-9FD3-F3E4687E1452}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the power net of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{48420240-E6BB-423E-9FD3-F3E4687E1452}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{48420240-E6BB-423E-9FD3-F3E4687E1452}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IPowerNetsMutable(DispatchBaseClass):
	CLSID = IID('{B224A038-B04A-47E1-8F9F-C7938C61FD68}')
	coclass_clsid = IID('{AFF3111C-9B72-46E6-9E5F-0A241014C7C1}')

	# Result is of type INet
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the power net of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{48420240-E6BB-423E-9FD3-F3E4687E1452}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the power net of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{48420240-E6BB-423E-9FD3-F3E4687E1452}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{48420240-E6BB-423E-9FD3-F3E4687E1452}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IRuleLayer(DispatchBaseClass):
	CLSID = IID('{F25192FE-8196-46B9-BF8A-CBA1AFA316A3}')
	coclass_clsid = IID('{A4733E8D-B970-4077-AC69-E6578DC3FB93}')

	# Result is of type IConstraintsMutable
	# The method GetConstraints is actually a property, but must be used as a method to correctly pass the arguments
	def GetConstraints(self, p_nConstraintMask=7):
		'Returns the collection of constraints, filtered by EConstraintMask constant.'
		ret = self._oleobj_.InvokeTypes(1610809345, LCID, 2, (9, 0), ((3, 49),),p_nConstraintMask
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetConstraints', '{1DDEC891-7D43-4EE9-9BD4-63772C577150}')
		return ret

	# Result is of type IObjects
	# The method GetObjects is actually a property, but must be used as a method to correctly pass the arguments
	def GetObjects(self, p_eObjectType=0):
		'Returns the collection of child objects, filtered by EObjectType constant.'
		ret = self._oleobj_.InvokeTypes(1610809347, LCID, 2, (9, 0), ((3, 49),),p_eObjectType
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjects', '{44747797-9642-483B-AB9C-6AE0A1899549}')
		return ret

	def IsDefault(self):
		'Returns true if the object is default and cannot be deleted.'
		return self._oleobj_.InvokeTypes(1610743811, LCID, 1, (11, 0), (),)

	def IsValid(self):
		'Returns true if the object is still valid.'
		return self._oleobj_.InvokeTypes(1610743810, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		# Method 'Comments' returns object of type 'ICommentsMutable'
		"Comments": (1610809346, 2, (9, 0), (), "Comments", '{23FAC1D8-2578-42BC-9F65-F04930FB6489}'),
		# Method 'Constraints' returns object of type 'IConstraintsMutable'
		"Constraints": (1610809345, 2, (9, 0), ((3, 49),), "Constraints", '{1DDEC891-7D43-4EE9-9BD4-63772C577150}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
		"ObjectType": (1610809344, 2, (3, 0), (), "ObjectType", None),
		# Method 'Objects' returns object of type 'IObjects'
		"Objects": (1610809347, 2, (9, 0), ((3, 49),), "Objects", '{44747797-9642-483B-AB9C-6AE0A1899549}'),
		# Method 'Parent' returns object of type 'IObject'
		"Parent": (1610743809, 2, (9, 0), (), "Parent", '{7A5D1A08-B723-4929-BB46-A801DC642EB6}'),
	}
	_prop_map_put_ = {
	}

	Comments: str # ICommentsMutable; read_only
	Constraints: str # IConstraintsMutable; read_only
	Name: str # read_only
	ObjectType: str # read_only
	Objects: str # IObjects; read_only
	Parent: str # IObject; read_only

	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
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

class IRuleLayers(DispatchBaseClass):
	CLSID = IID('{6710F183-E176-48F4-B3CA-DBD22E0CF5FF}')
	coclass_clsid = IID('{756E21CB-A264-4D2A-B086-0B12F97D0FB5}')

	# Result is of type IRuleLayer
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the rule layer of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{F25192FE-8196-46B9-BF8A-CBA1AFA316A3}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the rule layer of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{F25192FE-8196-46B9-BF8A-CBA1AFA316A3}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{F25192FE-8196-46B9-BF8A-CBA1AFA316A3}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IScheme(DispatchBaseClass):
	CLSID = IID('{6F39247C-17C2-4C9F-B14C-469620C80FC4}')
	coclass_clsid = IID('{0A5EE769-4E45-41A0-98EE-9BFE90EDB47D}')

	# Result is of type IConstraintsMutable
	# The method GetConstraints is actually a property, but must be used as a method to correctly pass the arguments
	def GetConstraints(self, p_nConstraintMask=7):
		'Returns the collection of constraints, filtered by EConstraintMask constant.'
		ret = self._oleobj_.InvokeTypes(1610809345, LCID, 2, (9, 0), ((3, 49),),p_nConstraintMask
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetConstraints', '{1DDEC891-7D43-4EE9-9BD4-63772C577150}')
		return ret

	# Result is of type ISchemeNetClasses
	# The method GetNetClasses is actually a property, but must be used as a method to correctly pass the arguments
	def GetNetClasses(self, p_nNetClassMask=2):
		'Returns the collection of all net classes.'
		ret = self._oleobj_.InvokeTypes(1610874880, LCID, 2, (9, 0), ((3, 49),),p_nNetClassMask
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetNetClasses', '{FA885B75-B122-4B9E-BAA2-87C657CB5659}')
		return ret

	# Result is of type IObjects
	# The method GetObjects is actually a property, but must be used as a method to correctly pass the arguments
	def GetObjects(self, p_eObjectType=0):
		'Returns the collection of child objects, filtered by EObjectType constant.'
		ret = self._oleobj_.InvokeTypes(1610809347, LCID, 2, (9, 0), ((3, 49),),p_eObjectType
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjects', '{44747797-9642-483B-AB9C-6AE0A1899549}')
		return ret

	def IsDefault(self):
		'Returns true if the object is default and cannot be deleted.'
		return self._oleobj_.InvokeTypes(1610743811, LCID, 1, (11, 0), (),)

	def IsValid(self):
		'Returns true if the object is still valid.'
		return self._oleobj_.InvokeTypes(1610743810, LCID, 1, (11, 0), (),)

	def Rename(self, p_strName=defaultNamedNotOptArg):
		'Changes the name of the object.'
		return self._oleobj_.InvokeTypes(1610874883, LCID, 1, (24, 0), ((8, 1),),p_strName
			)

	_prop_map_get_ = {
		# Method 'ClassClearances' returns object of type 'IClassClearances'
		"ClassClearances": (1610874882, 2, (9, 0), (), "ClassClearances", '{96FD6C42-8C02-4A00-A1B6-C47FB0D47913}'),
		# Method 'ClearanceRules' returns object of type 'ISchemeClearanceRules'
		"ClearanceRules": (1610874881, 2, (9, 0), (), "ClearanceRules", '{8F934507-D505-4A25-A96A-1654C17B5C81}'),
		# Method 'Comments' returns object of type 'ICommentsMutable'
		"Comments": (1610809346, 2, (9, 0), (), "Comments", '{23FAC1D8-2578-42BC-9F65-F04930FB6489}'),
		# Method 'Constraints' returns object of type 'IConstraintsMutable'
		"Constraints": (1610809345, 2, (9, 0), ((3, 49),), "Constraints", '{1DDEC891-7D43-4EE9-9BD4-63772C577150}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
		# Method 'NetClasses' returns object of type 'ISchemeNetClasses'
		"NetClasses": (1610874880, 2, (9, 0), ((3, 49),), "NetClasses", '{FA885B75-B122-4B9E-BAA2-87C657CB5659}'),
		"ObjectType": (1610809344, 2, (3, 0), (), "ObjectType", None),
		# Method 'Objects' returns object of type 'IObjects'
		"Objects": (1610809347, 2, (9, 0), ((3, 49),), "Objects", '{44747797-9642-483B-AB9C-6AE0A1899549}'),
		# Method 'Parent' returns object of type 'IObject'
		"Parent": (1610743809, 2, (9, 0), (), "Parent", '{7A5D1A08-B723-4929-BB46-A801DC642EB6}'),
	}
	_prop_map_put_ = {
	}

	ClassClearances: str # IClassClearances; read_only
	ClearanceRules: str # ISchemeClearanceRules; read_only
	Comments: str # ICommentsMutable; read_only
	Constraints: str # IConstraintsMutable; read_only
	Name: str # read_only
	NetClasses: str # ISchemeNetClasses; read_only
	ObjectType: str # read_only
	Objects: str # IObjects; read_only
	Parent: str # IObject; read_only

	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
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

class ISchemeClearanceRule(DispatchBaseClass):
	CLSID = IID('{DD8B4252-8E56-4A1A-B5CC-2A3A1284B1C5}')
	coclass_clsid = IID('{150A1D3E-3113-420A-9322-80966E1D7B42}')

	# Result is of type IConstraintsMutable
	# The method GetConstraints is actually a property, but must be used as a method to correctly pass the arguments
	def GetConstraints(self, p_nConstraintMask=7):
		'Returns the collection of constraints, filtered by EConstraintMask constant.'
		ret = self._oleobj_.InvokeTypes(1610809345, LCID, 2, (9, 0), ((3, 49),),p_nConstraintMask
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetConstraints', '{1DDEC891-7D43-4EE9-9BD4-63772C577150}')
		return ret

	# Result is of type IObjects
	# The method GetObjects is actually a property, but must be used as a method to correctly pass the arguments
	def GetObjects(self, p_eObjectType=0):
		'Returns the collection of child objects, filtered by EObjectType constant.'
		ret = self._oleobj_.InvokeTypes(1610809347, LCID, 2, (9, 0), ((3, 49),),p_eObjectType
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjects', '{44747797-9642-483B-AB9C-6AE0A1899549}')
		return ret

	def IsDefault(self):
		'Returns true if the object is default and cannot be deleted.'
		return self._oleobj_.InvokeTypes(1610743811, LCID, 1, (11, 0), (),)

	def IsValid(self):
		'Returns true if the object is still valid.'
		return self._oleobj_.InvokeTypes(1610743810, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		# Method 'Comments' returns object of type 'ICommentsMutable'
		"Comments": (1610809346, 2, (9, 0), (), "Comments", '{23FAC1D8-2578-42BC-9F65-F04930FB6489}'),
		# Method 'Constraints' returns object of type 'IConstraintsMutable'
		"Constraints": (1610809345, 2, (9, 0), ((3, 49),), "Constraints", '{1DDEC891-7D43-4EE9-9BD4-63772C577150}'),
		# Method 'Layers' returns object of type 'IRuleLayers'
		"Layers": (1610874880, 2, (9, 0), (), "Layers", '{6710F183-E176-48F4-B3CA-DBD22E0CF5FF}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
		"ObjectType": (1610809344, 2, (3, 0), (), "ObjectType", None),
		# Method 'Objects' returns object of type 'IObjects'
		"Objects": (1610809347, 2, (9, 0), ((3, 49),), "Objects", '{44747797-9642-483B-AB9C-6AE0A1899549}'),
		# Method 'Parent' returns object of type 'IObject'
		"Parent": (1610743809, 2, (9, 0), (), "Parent", '{7A5D1A08-B723-4929-BB46-A801DC642EB6}'),
	}
	_prop_map_put_ = {
	}

	Comments: str # ICommentsMutable; read_only
	Constraints: str # IConstraintsMutable; read_only
	Layers: str # IRuleLayers; read_only
	Name: str # read_only
	ObjectType: str # read_only
	Objects: str # IObjects; read_only
	Parent: str # IObject; read_only

	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
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

class ISchemeClearanceRules(DispatchBaseClass):
	CLSID = IID('{8F934507-D505-4A25-A96A-1654C17B5C81}')
	coclass_clsid = IID('{9CA49EA5-F767-4CD7-827C-9566CC755DDB}')

	# Result is of type ISchemeClearanceRule
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the scheme clearance rule of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{DD8B4252-8E56-4A1A-B5CC-2A3A1284B1C5}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the scheme clearance rule of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{DD8B4252-8E56-4A1A-B5CC-2A3A1284B1C5}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{DD8B4252-8E56-4A1A-B5CC-2A3A1284B1C5}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISchemeNetClass(DispatchBaseClass):
	CLSID = IID('{06818093-77D0-48D0-847E-77DFFAB80667}')
	coclass_clsid = IID('{4262249B-F52C-4618-9643-BD9C1D625E87}')

	# Result is of type IConstraintsMutable
	# The method GetConstraints is actually a property, but must be used as a method to correctly pass the arguments
	def GetConstraints(self, p_nConstraintMask=7):
		'Returns the collection of constraints, filtered by EConstraintMask constant.'
		ret = self._oleobj_.InvokeTypes(1610809345, LCID, 2, (9, 0), ((3, 49),),p_nConstraintMask
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetConstraints', '{1DDEC891-7D43-4EE9-9BD4-63772C577150}')
		return ret

	# Result is of type ISchemeNetClasses
	# The method GetNetClasses is actually a property, but must be used as a method to correctly pass the arguments
	def GetNetClasses(self, p_nNetClassMask=2):
		'Returns the collection of child net classes, filtered by EObjectMask constant.'
		ret = self._oleobj_.InvokeTypes(1610874881, LCID, 2, (9, 0), ((3, 49),),p_nNetClassMask
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetNetClasses', '{FA885B75-B122-4B9E-BAA2-87C657CB5659}')
		return ret

	# Result is of type IObjects
	# The method GetObjects is actually a property, but must be used as a method to correctly pass the arguments
	def GetObjects(self, p_eObjectType=0):
		'Returns the collection of child objects, filtered by EObjectType constant.'
		ret = self._oleobj_.InvokeTypes(1610809347, LCID, 2, (9, 0), ((3, 49),),p_eObjectType
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjects', '{44747797-9642-483B-AB9C-6AE0A1899549}')
		return ret

	def IsDefault(self):
		'Returns true if the object is default and cannot be deleted.'
		return self._oleobj_.InvokeTypes(1610743811, LCID, 1, (11, 0), (),)

	def IsValid(self):
		'Returns true if the object is still valid.'
		return self._oleobj_.InvokeTypes(1610743810, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		# Method 'Comments' returns object of type 'ICommentsMutable'
		"Comments": (1610809346, 2, (9, 0), (), "Comments", '{23FAC1D8-2578-42BC-9F65-F04930FB6489}'),
		# Method 'Constraints' returns object of type 'IConstraintsMutable'
		"Constraints": (1610809345, 2, (9, 0), ((3, 49),), "Constraints", '{1DDEC891-7D43-4EE9-9BD4-63772C577150}'),
		"FullName": (1610874880, 2, (8, 0), (), "FullName", None),
		# Method 'Layers' returns object of type 'IRuleLayers'
		"Layers": (1610874882, 2, (9, 0), (), "Layers", '{6710F183-E176-48F4-B3CA-DBD22E0CF5FF}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
		# Method 'NetClasses' returns object of type 'ISchemeNetClasses'
		"NetClasses": (1610874881, 2, (9, 0), ((3, 49),), "NetClasses", '{FA885B75-B122-4B9E-BAA2-87C657CB5659}'),
		"ObjectType": (1610809344, 2, (3, 0), (), "ObjectType", None),
		# Method 'Objects' returns object of type 'IObjects'
		"Objects": (1610809347, 2, (9, 0), ((3, 49),), "Objects", '{44747797-9642-483B-AB9C-6AE0A1899549}'),
		# Method 'Parent' returns object of type 'IObject'
		"Parent": (1610743809, 2, (9, 0), (), "Parent", '{7A5D1A08-B723-4929-BB46-A801DC642EB6}'),
	}
	_prop_map_put_ = {
	}

	Comments: str # ICommentsMutable; read_only
	Constraints: str # IConstraintsMutable; read_only
	FullName: str # read_only
	Layers: str # IRuleLayers; read_only
	Name: str # read_only
	NetClasses: str # ISchemeNetClasses; read_only
	ObjectType: str # read_only
	Objects: str # IObjects; read_only
	Parent: str # IObject; read_only

	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
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

class ISchemeNetClasses(DispatchBaseClass):
	CLSID = IID('{FA885B75-B122-4B9E-BAA2-87C657CB5659}')
	coclass_clsid = IID('{42D9D034-924A-4439-9747-D6441A45571A}')

	# Result is of type ISchemeNetClass
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the scheme net class of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{06818093-77D0-48D0-847E-77DFFAB80667}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the scheme net class of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{06818093-77D0-48D0-847E-77DFFAB80667}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{06818093-77D0-48D0-847E-77DFFAB80667}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISchemes(DispatchBaseClass):
	CLSID = IID('{08A1E04B-6987-41C4-90E5-CA467E65937B}')
	coclass_clsid = IID('{47D1E5C7-D510-4D3D-9EE3-8A19493FAC71}')

	# Result is of type IScheme
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the scheme of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{6F39247C-17C2-4C9F-B14C-469620C80FC4}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the scheme of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{6F39247C-17C2-4C9F-B14C-469620C80FC4}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{6F39247C-17C2-4C9F-B14C-469620C80FC4}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISchemesMutable(DispatchBaseClass):
	CLSID = IID('{C868C166-9607-4506-AEF9-5AE4FB428F95}')
	coclass_clsid = IID('{1855D335-FBB0-475E-B448-9F6C0D035807}')

	# Result is of type IScheme
	def Add(self, p_strName=defaultNamedNotOptArg):
		'Creates the scheme of the given name and adds it to the collection.'
		ret = self._oleobj_.InvokeTypes(1610874880, LCID, 1, (9, 0), ((8, 1),),p_strName
			)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{6F39247C-17C2-4C9F-B14C-469620C80FC4}')
		return ret

	def Delete(self, p_vIndex=defaultNamedNotOptArg):
		'Deletes the scheme of the given index or name and removes it from the collection.'
		return self._oleobj_.InvokeTypes(1610874881, LCID, 1, (24, 0), ((12, 1),),p_vIndex
			)

	# Result is of type IScheme
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the scheme of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{6F39247C-17C2-4C9F-B14C-469620C80FC4}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the scheme of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{6F39247C-17C2-4C9F-B14C-469620C80FC4}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{6F39247C-17C2-4C9F-B14C-469620C80FC4}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISettings(DispatchBaseClass):
	CLSID = IID('{8D9E96B8-678C-4EC9-93EE-F7E4CEC025FB}')
	coclass_clsid = IID('{5B3D4D1E-F433-41E5-A6CF-1166E1812E45}')

	_prop_map_get_ = {
		# Method 'Notation' returns object of type 'INotation'
		"Notation": (1610743809, 2, (9, 0), (), "Notation", '{177B82E6-3AFF-4E52-8141-7911C63B1879}'),
		# Method 'Units' returns object of type 'IUnits'
		"Units": (1610743808, 2, (9, 0), (), "Units", '{19C74DFD-6D72-4514-BAEB-D6FF7C4A1182}'),
	}
	_prop_map_put_ = {
	}

	Notation: str # INotation; read_only
	Units: str # IUnits; read_only

	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IStackup(DispatchBaseClass):
	CLSID = IID('{FBFDBD21-1B6F-4263-A285-6FB6E9C7747F}')
	coclass_clsid = IID('{A9F41CFA-8BA3-4D5A-A002-D4E2C9F54CD2}')

	# Result is of type IConstraintsMutable
	# The method GetConstraints is actually a property, but must be used as a method to correctly pass the arguments
	def GetConstraints(self, p_nConstraintMask=7):
		'Returns the collection of constraints, filtered by EConstraintMask constant.'
		ret = self._oleobj_.InvokeTypes(1610809345, LCID, 2, (9, 0), ((3, 49),),p_nConstraintMask
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetConstraints', '{1DDEC891-7D43-4EE9-9BD4-63772C577150}')
		return ret

	# Result is of type IObjects
	# The method GetObjects is actually a property, but must be used as a method to correctly pass the arguments
	def GetObjects(self, p_eObjectType=0):
		'Returns the collection of child objects, filtered by EObjectType constant.'
		ret = self._oleobj_.InvokeTypes(1610809347, LCID, 2, (9, 0), ((3, 49),),p_eObjectType
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjects', '{44747797-9642-483B-AB9C-6AE0A1899549}')
		return ret

	def IsDefault(self):
		'Returns true if the object is default and cannot be deleted.'
		return self._oleobj_.InvokeTypes(1610743811, LCID, 1, (11, 0), (),)

	def IsValid(self):
		'Returns true if the object is still valid.'
		return self._oleobj_.InvokeTypes(1610743810, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		# Method 'Comments' returns object of type 'ICommentsMutable'
		"Comments": (1610809346, 2, (9, 0), (), "Comments", '{23FAC1D8-2578-42BC-9F65-F04930FB6489}'),
		# Method 'Constraints' returns object of type 'IConstraintsMutable'
		"Constraints": (1610809345, 2, (9, 0), ((3, 49),), "Constraints", '{1DDEC891-7D43-4EE9-9BD4-63772C577150}'),
		# Method 'Layers' returns object of type 'ILayersMutable'
		"Layers": (1610874880, 2, (9, 0), (), "Layers", '{39981775-2776-4221-AB3C-1C27040DB64E}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
		"ObjectType": (1610809344, 2, (3, 0), (), "ObjectType", None),
		# Method 'Objects' returns object of type 'IObjects'
		"Objects": (1610809347, 2, (9, 0), ((3, 49),), "Objects", '{44747797-9642-483B-AB9C-6AE0A1899549}'),
		# Method 'Parent' returns object of type 'IObject'
		"Parent": (1610743809, 2, (9, 0), (), "Parent", '{7A5D1A08-B723-4929-BB46-A801DC642EB6}'),
	}
	_prop_map_put_ = {
	}

	Comments: str # ICommentsMutable; read_only
	Constraints: str # IConstraintsMutable; read_only
	Layers: str # ILayersMutable; read_only
	Name: str # read_only
	ObjectType: str # read_only
	Objects: str # IObjects; read_only
	Parent: str # IObject; read_only

	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
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

class ITopology(DispatchBaseClass):
	CLSID = IID('{E827A25D-2BEB-4013-9E2B-035133E06025}')
	coclass_clsid = IID('{31529548-2AD2-4506-854D-E81C61784146}')

	def Begin(self, p_eTopologyType=defaultNamedNotOptArg):
		'Begins the topology creation.'
		return self._oleobj_.InvokeTypes(1610874887, LCID, 1, (24, 0), ((3, 1),),p_eTopologyType
			)

	def Commit(self):
		'Commits the changes in the topology.'
		return self._oleobj_.InvokeTypes(1610874888, LCID, 1, (24, 0), (),)

	# Result is of type IConstraintsMutable
	# The method GetConstraints is actually a property, but must be used as a method to correctly pass the arguments
	def GetConstraints(self, p_nConstraintMask=7):
		'Returns the collection of constraints, filtered by EConstraintMask constant.'
		ret = self._oleobj_.InvokeTypes(1610809345, LCID, 2, (9, 0), ((3, 49),),p_nConstraintMask
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetConstraints', '{1DDEC891-7D43-4EE9-9BD4-63772C577150}')
		return ret

	# Result is of type IObjects
	# The method GetObjects is actually a property, but must be used as a method to correctly pass the arguments
	def GetObjects(self, p_eObjectType=0):
		'Returns the collection of child objects, filtered by EObjectType constant.'
		ret = self._oleobj_.InvokeTypes(1610809347, LCID, 2, (9, 0), ((3, 49),),p_eObjectType
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjects', '{44747797-9642-483B-AB9C-6AE0A1899549}')
		return ret

	def IsDefault(self):
		'Returns true if the object is default and cannot be deleted.'
		return self._oleobj_.InvokeTypes(1610743811, LCID, 1, (11, 0), (),)

	def IsOrdered(self):
		'Returns true if the topology is fully defined.'
		return self._oleobj_.InvokeTypes(1610874882, LCID, 1, (11, 0), (),)

	def IsValid(self):
		'Returns true if the object is still valid.'
		return self._oleobj_.InvokeTypes(1610743810, LCID, 1, (11, 0), (),)

	def Rollback(self):
		'Discards the changes in the topology.'
		return self._oleobj_.InvokeTypes(1610874889, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Comments' returns object of type 'ICommentsMutable'
		"Comments": (1610809346, 2, (9, 0), (), "Comments", '{23FAC1D8-2578-42BC-9F65-F04930FB6489}'),
		# Method 'Constraints' returns object of type 'IConstraintsMutable'
		"Constraints": (1610809345, 2, (9, 0), ((3, 49),), "Constraints", '{1DDEC891-7D43-4EE9-9BD4-63772C577150}'),
		# Method 'FromTos' returns object of type 'IFromTosMutable'
		"FromTos": (1610874884, 2, (9, 0), (), "FromTos", '{EE1AE409-4E07-44DC-8E8A-13B34E7FF81E}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
		"ObjectType": (1610809344, 2, (3, 0), (), "ObjectType", None),
		# Method 'Objects' returns object of type 'IObjects'
		"Objects": (1610809347, 2, (9, 0), ((3, 49),), "Objects", '{44747797-9642-483B-AB9C-6AE0A1899549}'),
		# Method 'Parent' returns object of type 'IObject'
		"Parent": (1610743809, 2, (9, 0), (), "Parent", '{7A5D1A08-B723-4929-BB46-A801DC642EB6}'),
		# Method 'PinPairs' returns object of type 'IPinPairsMutable'
		"PinPairs": (1610874885, 2, (9, 0), (), "PinPairs", '{0D52DE96-799A-4660-ACFE-109F34DEE67B}'),
		# Method 'PinSets' returns object of type 'IPinSetsMutable'
		"PinSets": (1610874886, 2, (9, 0), (), "PinSets", '{27E83E75-0024-45DF-92D3-516B20F446C8}'),
		# Method 'Pins' returns object of type 'IPins'
		"Pins": (1610874883, 2, (9, 0), (), "Pins", '{3F1B4618-0423-42B9-A741-72E65CE0E573}'),
		"TopologyType": (1610874880, 2, (3, 0), (), "TopologyType", None),
	}
	_prop_map_put_ = {
		"TopologyType": ((1610874880, LCID, 4, 0),()),
	}

	Comments: str # ICommentsMutable; read_only
	Constraints: str # IConstraintsMutable; read_only
	FromTos: str # IFromTosMutable; read_only
	Name: str # read_only
	ObjectType: str # read_only
	Objects: str # IObjects; read_only
	Parent: str # IObject; read_only
	PinPairs: str # IPinPairsMutable; read_only
	PinSets: str # IPinSetsMutable; read_only
	Pins: str # IPins; read_only
	TopologyType: str # read/write

	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
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

class IUnits(DispatchBaseClass):
	CLSID = IID('{19C74DFD-6D72-4514-BAEB-D6FF7C4A1182}')
	coclass_clsid = IID('{58F0FCDE-99F8-49B8-B105-EB6B93C25616}')

	_prop_map_get_ = {
		"Capacitance": (1610743808, 2, (3, 0), (), "Capacitance", None),
		"Current": (1610743810, 2, (3, 0), (), "Current", None),
		"CurrentDensity": (1610743812, 2, (3, 0), (), "CurrentDensity", None),
		"Inductance": (1610743816, 2, (3, 0), (), "Inductance", None),
		"Linear": (1610743818, 2, (3, 0), (), "Linear", None),
		"Power": (1610743820, 2, (3, 0), (), "Power", None),
		"Resistance": (1610743822, 2, (3, 0), (), "Resistance", None),
		"Temperature": (1610743824, 2, (3, 0), (), "Temperature", None),
		"Theta": (1610743826, 2, (3, 0), (), "Theta", None),
		"Time": (1610743828, 2, (3, 0), (), "Time", None),
		"Voltage": (1610743814, 2, (3, 0), (), "Voltage", None),
	}
	_prop_map_put_ = {
		"Capacitance": ((1610743808, LCID, 4, 0),()),
		"Current": ((1610743810, LCID, 4, 0),()),
		"CurrentDensity": ((1610743812, LCID, 4, 0),()),
		"Inductance": ((1610743816, LCID, 4, 0),()),
		"Linear": ((1610743818, LCID, 4, 0),()),
		"Power": ((1610743820, LCID, 4, 0),()),
		"Resistance": ((1610743822, LCID, 4, 0),()),
		"Temperature": ((1610743824, LCID, 4, 0),()),
		"Theta": ((1610743826, LCID, 4, 0),()),
		"Time": ((1610743828, LCID, 4, 0),()),
		"Voltage": ((1610743814, LCID, 4, 0),()),
	}

	Capacitance: str # read/write
	Current: str # read/write
	CurrentDensity: str # read/write
	Inductance: str # read/write
	Linear: str # read/write
	Power: str # read/write
	Resistance: str # read/write
	Temperature: str # read/write
	Theta: str # read/write
	Time: str # read/write
	Voltage: str # read/write

	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IVariable(DispatchBaseClass):
	CLSID = IID('{FB9D7374-6228-4B92-8403-03F3927706DE}')
	coclass_clsid = IID('{401B8E73-606E-42F1-A576-EEFB1EADDD08}')

	# Result is of type IConstraintsMutable
	# The method GetConstraints is actually a property, but must be used as a method to correctly pass the arguments
	def GetConstraints(self, p_nConstraintMask=7):
		'Returns the collection of constraints, filtered by EConstraintMask constant.'
		ret = self._oleobj_.InvokeTypes(1610809345, LCID, 2, (9, 0), ((3, 49),),p_nConstraintMask
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetConstraints', '{1DDEC891-7D43-4EE9-9BD4-63772C577150}')
		return ret

	# Result is of type IObjects
	# The method GetObjects is actually a property, but must be used as a method to correctly pass the arguments
	def GetObjects(self, p_eObjectType=0):
		'Returns the collection of child objects, filtered by EObjectType constant.'
		ret = self._oleobj_.InvokeTypes(1610809347, LCID, 2, (9, 0), ((3, 49),),p_eObjectType
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjects', '{44747797-9642-483B-AB9C-6AE0A1899549}')
		return ret

	def IsDefault(self):
		'Returns true if the object is default and cannot be deleted.'
		return self._oleobj_.InvokeTypes(1610743811, LCID, 1, (11, 0), (),)

	def IsValid(self):
		'Returns true if the object is still valid.'
		return self._oleobj_.InvokeTypes(1610743810, LCID, 1, (11, 0), (),)

	def Rename(self, p_strName=defaultNamedNotOptArg):
		'Changes the name of the object.'
		return self._oleobj_.InvokeTypes(1610874880, LCID, 1, (24, 0), ((8, 1),),p_strName
			)

	_prop_map_get_ = {
		# Method 'Comments' returns object of type 'ICommentsMutable'
		"Comments": (1610809346, 2, (9, 0), (), "Comments", '{23FAC1D8-2578-42BC-9F65-F04930FB6489}'),
		# Method 'Constraints' returns object of type 'IConstraintsMutable'
		"Constraints": (1610809345, 2, (9, 0), ((3, 49),), "Constraints", '{1DDEC891-7D43-4EE9-9BD4-63772C577150}'),
		"Name": (0, 2, (8, 0), (), "Name", None),
		"ObjectType": (1610809344, 2, (3, 0), (), "ObjectType", None),
		# Method 'Objects' returns object of type 'IObjects'
		"Objects": (1610809347, 2, (9, 0), ((3, 49),), "Objects", '{44747797-9642-483B-AB9C-6AE0A1899549}'),
		# Method 'Parent' returns object of type 'IObject'
		"Parent": (1610743809, 2, (9, 0), (), "Parent", '{7A5D1A08-B723-4929-BB46-A801DC642EB6}'),
	}
	_prop_map_put_ = {
	}

	Comments: str # ICommentsMutable; read_only
	Constraints: str # IConstraintsMutable; read_only
	Name: str # read_only
	ObjectType: str # read_only
	Objects: str # IObjects; read_only
	Parent: str # IObject; read_only

	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
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

class IVariables(DispatchBaseClass):
	CLSID = IID('{CB2822E1-C294-4DD7-8DAC-A30B11174649}')
	coclass_clsid = IID('{D99D85C4-7960-4462-B02F-193CCD7DA13B}')

	# Result is of type IVariable
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the variable of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{FB9D7374-6228-4B92-8403-03F3927706DE}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the variable of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{FB9D7374-6228-4B92-8403-03F3927706DE}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{FB9D7374-6228-4B92-8403-03F3927706DE}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IVariablesMutable(DispatchBaseClass):
	CLSID = IID('{9B803C91-3B87-4F74-810E-C038E63376B7}')
	coclass_clsid = IID('{43B955FB-3E8A-4B7F-92FC-821418613BF8}')

	# Result is of type IVariable
	def Add(self, p_strName=defaultNamedNotOptArg):
		'Creates the variable of the given name and adds it to the collection.'
		ret = self._oleobj_.InvokeTypes(1610874880, LCID, 1, (9, 0), ((8, 1),),p_strName
			)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{FB9D7374-6228-4B92-8403-03F3927706DE}')
		return ret

	def Delete(self, p_vIndex=defaultNamedNotOptArg):
		'Deletes the variable of the given index or name and removes it from the collection.'
		return self._oleobj_.InvokeTypes(1610874881, LCID, 1, (24, 0), ((12, 1),),p_vIndex
			)

	# Result is of type IVariable
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the variable of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{FB9D7374-6228-4B92-8403-03F3927706DE}')
		return ret

	_prop_map_get_ = {
		"Count": (1610743809, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}

	Count: int # read_only

	# Default method for this class is 'Item'
	def __call__(self, p_vIndex=defaultNamedNotOptArg):
		'Returns the variable of the given index or name.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),p_vIndex
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{FB9D7374-6228-4B92-8403-03F3927706DE}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{FB9D7374-6228-4B92-8403-03F3927706DE}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1610743809, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

from win32com.client import CoClassBaseClass
class Base(CoClassBaseClass): # A CoClass
	# The generic base object.
	CLSID = IID('{FDD01A44-69ED-4E7F-88C7-7947E8C7BD69}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IBase,
	]
	default_interface = IBase

class Class(CoClassBaseClass): # A CoClass
	# The generic class object.
	CLSID = IID('{3FA6B387-5FB9-4380-B4FF-BD1D0CC40F08}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IClass,
	]
	default_interface = IClass

class ClassClearance(CoClassBaseClass): # A CoClass
	# The class clearance object.
	CLSID = IID('{6E8C0221-D322-40BA-80E0-0271F8DFD70C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IClassClearance,
	]
	default_interface = IClassClearance

class ClassClearances(CoClassBaseClass): # A CoClass
	# The class clearances base collection that allows accessing class clearance items only.
	CLSID = IID('{5FF6AAE0-F6A3-40A0-8B3E-36E1C22D7808}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IClassClearances,
	]
	default_interface = IClassClearances

class ClassClearancesMutable(CoClassBaseClass): # A CoClass
	# The class clearances mutable collection that allows adding or removing class clearance items.
	CLSID = IID('{3D99E63D-958F-4443-9BA7-4C07BBB99068}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IClassClearancesMutable,
	]
	default_interface = IClassClearancesMutable

class ClearanceRule(CoClassBaseClass): # A CoClass
	# The clearance rule object.
	CLSID = IID('{02D9EB90-8303-47C0-8C9B-27D02DE97D52}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IClearanceRule,
	]
	default_interface = IClearanceRule

class ClearanceRules(CoClassBaseClass): # A CoClass
	# The clearance rules base collection that allows accessing clearance rule items only.
	CLSID = IID('{CC09F366-B8E9-4E10-84DC-8C92197B0207}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IClearanceRules,
	]
	default_interface = IClearanceRules

class ClearanceRulesMutable(CoClassBaseClass): # A CoClass
	# The clearance rules mutable collection that allows adding or removing clearance rule items.
	CLSID = IID('{15582A4E-85ED-45F4-BA66-696181360E83}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IClearanceRulesMutable,
	]
	default_interface = IClearanceRulesMutable

class Collection(CoClassBaseClass): # A CoClass
	# The generic collection.
	CLSID = IID('{E2E4868A-9FD4-478F-A504-0AB8B2DEB117}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ICollection,
	]
	default_interface = ICollection

class Comment(CoClassBaseClass): # A CoClass
	# The comment object.
	CLSID = IID('{C5CB9071-36B8-4E69-95FC-41839093973B}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IComment,
	]
	default_interface = IComment

class Comments(CoClassBaseClass): # A CoClass
	# The comments base collection that allows accessing comment items only.
	CLSID = IID('{F7269414-6A1B-4F30-9FA0-619B80717D2A}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IComments,
	]
	default_interface = IComments

class CommentsMutable(CoClassBaseClass): # A CoClass
	# The comments mutable collection that allows adding or removing comments items.
	CLSID = IID('{65183681-9F46-4373-B909-A345126B459B}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ICommentsMutable,
	]
	default_interface = ICommentsMutable

class Component(CoClassBaseClass): # A CoClass
	# The component object.
	CLSID = IID('{E8CEF3AC-4D63-4E45-B553-CCC01DFC4202}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IComponent,
	]
	default_interface = IComponent

class Components(CoClassBaseClass): # A CoClass
	# The components base collection that allows accessing component items only.
	CLSID = IID('{B7DC1FFB-DDF7-4710-96DF-9CE53C3399A1}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IComponents,
	]
	default_interface = IComponents

class ComponentsMutable(CoClassBaseClass): # A CoClass
	# The components mutable collection is provided for future usage.
	CLSID = IID('{153D5723-3036-4796-9184-BA5AA4999BF7}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IComponentsMutable,
	]
	default_interface = IComponentsMutable

class Constant(CoClassBaseClass): # A CoClass
	# The constant object.
	CLSID = IID('{104F0D8D-82A5-44BA-A563-92EBF5BAEEB7}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IConstant,
	]
	default_interface = IConstant

class Constants(CoClassBaseClass): # A CoClass
	# The constants base collection that allows accessing constant items only.
	CLSID = IID('{52504AB6-DF45-424B-A06A-B4F29C000667}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IConstants,
	]
	default_interface = IConstants

class ConstantsMutable(CoClassBaseClass): # A CoClass
	# The constants mutable collection that allows adding or removing constant items.
	CLSID = IID('{2FC31295-E0FE-453B-AE2D-1BD5726CE291}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IConstantsMutable,
	]
	default_interface = IConstantsMutable

class Constraint(CoClassBaseClass): # A CoClass
	# The constraint object.
	CLSID = IID('{D3A2A3F8-D4FC-453F-9A69-CF8425497168}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IConstraint,
	]
	default_interface = IConstraint

class ConstraintClass(CoClassBaseClass): # A CoClass
	# The constraint class object.
	CLSID = IID('{032414B7-8F46-402E-B8B1-D834CF6FB083}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IConstraintClass,
	]
	default_interface = IConstraintClass

class ConstraintClasses(CoClassBaseClass): # A CoClass
	# The constraint classes base collection that allows accessing constraint class items only.
	CLSID = IID('{3BC701EA-8962-401F-8213-9782C2A5471F}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IConstraintClasses,
	]
	default_interface = IConstraintClasses

class ConstraintClassesMutable(CoClassBaseClass): # A CoClass
	# The constraint classes mutable collection that allows adding or removing constraint class items.
	CLSID = IID('{06CEF5AA-5BDB-4B33-8BBA-7E6A0E108A1B}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IConstraintClassesMutable,
	]
	default_interface = IConstraintClassesMutable

class Constraints(CoClassBaseClass): # A CoClass
	# The constraints base collection that allows accessing constraint items only.
	CLSID = IID('{25937434-EBF2-42A3-B4C8-2EC32F4DEE6E}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IConstraints,
	]
	default_interface = IConstraints

# This CoClass is known by the name 'ConstraintsAuto.119'
class ConstraintsAuto(CoClassBaseClass): # A CoClass
	# The Constraints Auto object.
	CLSID = IID('{8B0AE687-6CF5-1014-9B55-8BB0EECCF0AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IConstraintsAuto,
	]
	default_interface = IConstraintsAuto

class ConstraintsMutable(CoClassBaseClass): # A CoClass
	# The constraints mutable collection that allows adding or removing constraint items.
	CLSID = IID('{211695E1-560F-41E3-8125-5C41B4A1131B}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IConstraintsMutable,
	]
	default_interface = IConstraintsMutable

class DRC(CoClassBaseClass): # A CoClass
	# The DRC object.
	CLSID = IID('{644E0684-E131-45ED-A4B3-A76EC1D5B33E}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IDRC,
	]
	default_interface = IDRC

class Design(CoClassBaseClass): # A CoClass
	# The design object.
	CLSID = IID('{BD801DC8-79E4-45DE-ADB7-45E7918DF499}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IDesign,
	]
	default_interface = IDesign

class DesignParams(CoClassBaseClass): # A CoClass
	# The design parameters object.
	CLSID = IID('{E835C9C8-FC4E-417D-BD00-A948B4F66D20}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IDesignParams,
	]
	default_interface = IDesignParams

class DifferentialPair(CoClassBaseClass): # A CoClass
	# The differential pair object.
	CLSID = IID('{04DE4486-51F4-4FB5-A1D2-DCB6CD97EF6C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IDifferentialPair,
	]
	default_interface = IDifferentialPair

class DifferentialPairs(CoClassBaseClass): # A CoClass
	# The differential pairs base collection that allows accessing differential pair items only.
	CLSID = IID('{0E5A6F70-EA58-4E16-B16D-8B24785E5617}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IDifferentialPairs,
	]
	default_interface = IDifferentialPairs

class DifferentialPairsMutable(CoClassBaseClass): # A CoClass
	# The differential pairs mutable collection that allows adding or removing differential pair items.
	CLSID = IID('{B42E232E-C7ED-444C-81BC-4E88A3540DF3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IDifferentialPairsMutable,
	]
	default_interface = IDifferentialPairsMutable

class DisplayPattern(CoClassBaseClass): # A CoClass
	# The display pattern object.
	CLSID = IID('{8914D1F0-18EC-4E84-8CDA-F1598F99A228}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IDisplayPattern,
	]
	default_interface = IDisplayPattern

class DisplayPatterns(CoClassBaseClass): # A CoClass
	# The display patterns base collection that allows accessing display pattern items only.
	CLSID = IID('{078B323D-5BB7-4C07-92CF-9F3C48ED98B5}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IDisplayPatterns,
	]
	default_interface = IDisplayPatterns

class DisplayPatternsMutable(CoClassBaseClass): # A CoClass
	# The display patterns mutable collection that allows adding or removing display pattern items.
	CLSID = IID('{4415B5A1-315A-4D3E-91C9-898489133B66}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IDisplayPatternsMutable,
	]
	default_interface = IDisplayPatternsMutable

class ElectricalNet(CoClassBaseClass): # A CoClass
	# The electrical net object.
	CLSID = IID('{34AD93FA-589D-4CA9-B092-E60A1B16F627}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IElectricalNet,
	]
	default_interface = IElectricalNet

class ElectricalNets(CoClassBaseClass): # A CoClass
	# The electrical nets base collection that allows accessing electrical net items only.
	CLSID = IID('{D29538F3-CD23-4FB3-ACDB-6489A2B9F6E9}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IElectricalNets,
	]
	default_interface = IElectricalNets

class ElectricalNetsMutable(CoClassBaseClass): # A CoClass
	# The electrical nets mutable collection is provided for future usage.
	CLSID = IID('{511DF122-52DC-494E-B932-BC4DB9932B41}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IElectricalNetsMutable,
	]
	default_interface = IElectricalNetsMutable

class Formula(CoClassBaseClass): # A CoClass
	# The formula object.
	CLSID = IID('{50FBC794-9C15-4AF8-82C3-DE231368AAFE}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IFormula,
	]
	default_interface = IFormula

class Formulas(CoClassBaseClass): # A CoClass
	# The formulas base collection that allows accessing formula items only.
	CLSID = IID('{FC12916D-BCA2-44C7-8BA2-0469F29C2F99}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IFormulas,
	]
	default_interface = IFormulas

class FormulasMutable(CoClassBaseClass): # A CoClass
	# The formulas mutable collection is provided for future usage.
	CLSID = IID('{02C5D3D1-CD4B-49B9-A5A1-6D517184C8A3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IFormulasMutable,
	]
	default_interface = IFormulasMutable

class FromTo(CoClassBaseClass): # A CoClass
	# The from-to object.
	CLSID = IID('{FDBE490D-01ED-4EF4-96DF-C4D1034AC95F}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IFromTo,
	]
	default_interface = IFromTo

class FromTos(CoClassBaseClass): # A CoClass
	# The from-tos base collection that allows accessing from-to items only.
	CLSID = IID('{661A1886-47C6-4BE7-B902-7D741CC216C5}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IFromTos,
	]
	default_interface = IFromTos

class FromTosMutable(CoClassBaseClass): # A CoClass
	# The from-tos mutable collection that allows adding or removing from-to items.
	CLSID = IID('{3925DBCB-CE2E-4FA2-8BD8-D60CC27BF192}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IFromTosMutable,
	]
	default_interface = IFromTosMutable

class GeneralClearance(CoClassBaseClass): # A CoClass
	# The general clearance object.
	CLSID = IID('{AFF28CA8-1527-4C24-BD65-632849524714}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IGeneralClearance,
	]
	default_interface = IGeneralClearance

class GeneralClearances(CoClassBaseClass): # A CoClass
	# The general clearances base collection that allows accessing general clearance items only.
	CLSID = IID('{E82C72F8-E994-46BB-8E9A-1A2815C34A4F}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IGeneralClearances,
	]
	default_interface = IGeneralClearances

class GeneralClearancesMutable(CoClassBaseClass): # A CoClass
	# The general clearances mutable collection that allows adding or removing general clearance items.
	CLSID = IID('{7B50268E-5CD1-480D-B35F-E20A8430DD24}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IGeneralClearancesMutable,
	]
	default_interface = IGeneralClearancesMutable

class Layer(CoClassBaseClass): # A CoClass
	# The layer object.
	CLSID = IID('{A1BB2710-763F-4DC1-AE6D-0F079CAC9AFA}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ILayer,
	]
	default_interface = ILayer

class Layers(CoClassBaseClass): # A CoClass
	# The layers base collection that allows accessing layer items only.
	CLSID = IID('{96977B18-D144-4DB5-AF5F-266B353B61E6}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ILayers,
	]
	default_interface = ILayers

class LayersMutable(CoClassBaseClass): # A CoClass
	# The layers mutable collection that allows adding or removing layer items.
	CLSID = IID('{CD47D215-A820-47E2-AE07-453CC2ED6D7C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ILayersMutable,
	]
	default_interface = ILayersMutable

class MatchGroup(CoClassBaseClass): # A CoClass
	# The match group object.
	CLSID = IID('{BE604238-860C-429A-86DD-282A1D52ADFF}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMatchGroup,
	]
	default_interface = IMatchGroup

class MatchGroups(CoClassBaseClass): # A CoClass
	# The match group base collection that allows accessing match group items only.
	CLSID = IID('{95AF9055-4360-4AD1-837E-8A4AEF81AF34}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMatchGroups,
	]
	default_interface = IMatchGroups

class MatchGroupsMutable(CoClassBaseClass): # A CoClass
	# The match group mutable collection that allows adding or removing match group items.
	CLSID = IID('{E4717647-28C9-420B-8624-6A0298314D93}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMatchGroupsMutable,
	]
	default_interface = IMatchGroupsMutable

class Net(CoClassBaseClass): # A CoClass
	# The net object.
	CLSID = IID('{E111A365-1082-4B6E-A64B-FAE25BFEFB1B}')
	coclass_sources = [
	]
	coclass_interfaces = [
		INet,
	]
	default_interface = INet

class NetClass(CoClassBaseClass): # A CoClass
	# The net class object.
	CLSID = IID('{34DA88B0-930D-469A-8CE0-0738CBCD4870}')
	coclass_sources = [
	]
	coclass_interfaces = [
		INetClass,
	]
	default_interface = INetClass

class NetClasses(CoClassBaseClass): # A CoClass
	# The net classes base collection that allows accessing net class items only.
	CLSID = IID('{E6945AC7-71DE-4FBD-B914-513A60E82520}')
	coclass_sources = [
	]
	coclass_interfaces = [
		INetClasses,
	]
	default_interface = INetClasses

class NetClassesMutable(CoClassBaseClass): # A CoClass
	# The net classes mutable collection that allows adding or removing net class items.
	CLSID = IID('{38ABD376-70EE-45BF-B017-90DC59A9EB2F}')
	coclass_sources = [
	]
	coclass_interfaces = [
		INetClassesMutable,
	]
	default_interface = INetClassesMutable

class Nets(CoClassBaseClass): # A CoClass
	# The nets base collection that allows accessing net items only.
	CLSID = IID('{6AAAB236-9207-4D72-91AB-37FAD56B1505}')
	coclass_sources = [
	]
	coclass_interfaces = [
		INets,
	]
	default_interface = INets

class NetsMutable(CoClassBaseClass): # A CoClass
	# The nets mutable collection is provided for future usage.
	CLSID = IID('{C03A89DF-4DDB-4892-BF2A-3C92018D9F7E}')
	coclass_sources = [
	]
	coclass_interfaces = [
		INetsMutable,
	]
	default_interface = INetsMutable

class NoiseRule(CoClassBaseClass): # A CoClass
	# The noise rule object.
	CLSID = IID('{62CDF1A0-E6E8-4C62-8C4E-05015FA9FD54}')
	coclass_sources = [
	]
	coclass_interfaces = [
		INoiseRule,
	]
	default_interface = INoiseRule

class NoiseRules(CoClassBaseClass): # A CoClass
	# The noise rules base collection that allows accessing noise rule items only.
	CLSID = IID('{B954C85D-6103-4A81-A73D-4334ACE4FB4C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		INoiseRules,
	]
	default_interface = INoiseRules

class NoiseRulesMutable(CoClassBaseClass): # A CoClass
	# The parallelism rules mutable collection that allows adding or removing parallelism rule items.
	CLSID = IID('{1C7ACB33-918C-4071-BB73-471C94FDFA75}')
	coclass_sources = [
	]
	coclass_interfaces = [
		INoiseRulesMutable,
	]
	default_interface = INoiseRulesMutable

class Notation(CoClassBaseClass): # A CoClass
	# The design notation object.
	CLSID = IID('{866B8DDA-424F-4C1D-ACC7-74D2FD26A5E6}')
	coclass_sources = [
	]
	coclass_interfaces = [
		INotation,
	]
	default_interface = INotation

class Object(CoClassBaseClass): # A CoClass
	# The generic object.
	CLSID = IID('{B29B6B0B-4390-4DE0-AB0E-652FBD8D5845}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IObject,
	]
	default_interface = IObject

class Objects(CoClassBaseClass): # A CoClass
	# The generic objects collection.
	CLSID = IID('{26F1B6BC-D3D7-4A17-9387-53063A8F3E19}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IObjects,
	]
	default_interface = IObjects

class PackageClearance(CoClassBaseClass): # A CoClass
	# The package clearance object.
	CLSID = IID('{8C1CE62E-16DF-4CF0-8939-4DC718FED03A}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IPackageClearance,
	]
	default_interface = IPackageClearance

class PackageClearances(CoClassBaseClass): # A CoClass
	# The package clearances base collection that allows accessing package clearance items only.
	CLSID = IID('{8E8E5C86-7002-4197-9495-56C1B7BC5603}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IPackageClearances,
	]
	default_interface = IPackageClearances

class PackageClearancesMutable(CoClassBaseClass): # A CoClass
	# The package clearances mutable collection that allows adding or removing package clearance items.
	CLSID = IID('{258F61A2-1815-4AF5-BC54-FBA8FA6ECF60}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IPackageClearancesMutable,
	]
	default_interface = IPackageClearancesMutable

class PackageType(CoClassBaseClass): # A CoClass
	# The package type object.
	CLSID = IID('{CB10CB0C-DAB8-41C9-AAAB-500CC8C5A398}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IPackageType,
	]
	default_interface = IPackageType

class PackageTypes(CoClassBaseClass): # A CoClass
	# The package types base collection that allows accessing package type items only.
	CLSID = IID('{16AC6FAA-65B2-4B25-A3A3-EA0203A483FF}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IPackageTypes,
	]
	default_interface = IPackageTypes

class PackageTypesMutable(CoClassBaseClass): # A CoClass
	# The package types mutable collection that allows adding or removing package type items.
	CLSID = IID('{5515A13F-6AFA-45BA-BA6F-C291928DE332}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IPackageTypesMutable,
	]
	default_interface = IPackageTypesMutable

class ParallelismRule(CoClassBaseClass): # A CoClass
	# The parallelism rule object.
	CLSID = IID('{A73969C5-E0DA-45BA-BAB3-DDFCF3BE6FE8}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IParallelismRule,
	]
	default_interface = IParallelismRule

class ParallelismRuleSegment(CoClassBaseClass): # A CoClass
	# The parallelism rule segment object.
	CLSID = IID('{A5CBB258-CAC7-4150-A5FE-61B8027641DF}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IParallelismRuleSegment,
	]
	default_interface = IParallelismRuleSegment

class ParallelismRuleSegments(CoClassBaseClass): # A CoClass
	# The parallelism rules segment base collection that allows accessing parallelism rule segment items only.
	CLSID = IID('{7689BAC5-FCD4-4523-B7F7-693B529238D9}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IParallelismRuleSegments,
	]
	default_interface = IParallelismRuleSegments

class ParallelismRuleSegmentsMutable(CoClassBaseClass): # A CoClass
	# The parallelism rules mutable collection that allows adding or removing parallelism rule segment items.
	CLSID = IID('{6E18E1F9-1BCF-4EB3-B700-6A4D68349F92}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IParallelismRuleSegmentsMutable,
	]
	default_interface = IParallelismRuleSegmentsMutable

class ParallelismRules(CoClassBaseClass): # A CoClass
	# The parallelism rules base collection that allows accessing parallelism rule items only.
	CLSID = IID('{2ABDB9DD-E0F6-4344-B4C8-EF2E68B91DDC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IParallelismRules,
	]
	default_interface = IParallelismRules

class ParallelismRulesMutable(CoClassBaseClass): # A CoClass
	# The parallelism rules mutable collection that allows adding or removing parallelism rule items.
	CLSID = IID('{DD6F53A1-D9F2-4E92-AD84-81C15D262F16}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IParallelismRulesMutable,
	]
	default_interface = IParallelismRulesMutable

class Part(CoClassBaseClass): # A CoClass
	# The part object.
	CLSID = IID('{17DCD0D5-D0AD-41C1-924E-F6237BF78120}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IPart,
	]
	default_interface = IPart

class PartPin(CoClassBaseClass): # A CoClass
	# The part pin object.
	CLSID = IID('{2FAE361D-F475-44EC-B87C-F58184D8DFA1}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IPartPin,
	]
	default_interface = IPartPin

class PartPinPair(CoClassBaseClass): # A CoClass
	# The part pin pair object.
	CLSID = IID('{2C8C8556-C2B6-449B-88A2-9030268296AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IPartPinPair,
	]
	default_interface = IPartPinPair

class PartPinPairs(CoClassBaseClass): # A CoClass
	# The part pin pair base collection that allows accessing part pin pair items only.
	CLSID = IID('{8FA9F4DB-8EE1-45BB-9B2C-FBD758CCD1A0}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IPartPinPairs,
	]
	default_interface = IPartPinPairs

class PartPinPairsMutable(CoClassBaseClass): # A CoClass
	# The part pin pairs mutable collection that allows adding or removing part pin pair items.
	CLSID = IID('{F86FDE27-D779-458D-A51D-56FC1186F818}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IPartPinPairsMutable,
	]
	default_interface = IPartPinPairsMutable

class PartPins(CoClassBaseClass): # A CoClass
	# The part pin base collection that allows accessing part pin items only.
	CLSID = IID('{57320C9B-E888-40E1-B937-7090B95682E3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IPartPins,
	]
	default_interface = IPartPins

class PartPinsMutable(CoClassBaseClass): # A CoClass
	# The part pins mutable collection is provided for future usage.
	CLSID = IID('{6BD38466-57D0-4836-A566-60674280EBC8}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IPartPinsMutable,
	]
	default_interface = IPartPinsMutable

class Parts(CoClassBaseClass): # A CoClass
	# The parts base collection that allows accessing part items only.
	CLSID = IID('{902446D5-4B16-4320-91AE-682169A4B7A3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IParts,
	]
	default_interface = IParts

class PartsMutable(CoClassBaseClass): # A CoClass
	# The parts mutable collection is provided for future usage.
	CLSID = IID('{1C06D4C9-421F-47C1-B4F0-86179BDE6A44}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IPartsMutable,
	]
	default_interface = IPartsMutable

class PhysicalRules(CoClassBaseClass): # A CoClass
	# The physical rules object.
	CLSID = IID('{D902C696-50D9-4383-BC8C-595FDA5434F1}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IPhysicalRules,
	]
	default_interface = IPhysicalRules

class Pin(CoClassBaseClass): # A CoClass
	# The pin object.
	CLSID = IID('{BFB658F1-2CC5-4D15-B3F8-077FC1497BC4}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IPin,
	]
	default_interface = IPin

class PinPair(CoClassBaseClass): # A CoClass
	# The pin pair object.
	CLSID = IID('{F2284F80-6E4A-4945-BB5F-69FED15C9C5A}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IPinPair,
	]
	default_interface = IPinPair

class PinPairs(CoClassBaseClass): # A CoClass
	# The pin pair base collection that allows accessing pin pair items only.
	CLSID = IID('{FB7CB482-1529-451F-911B-7BC33EC256BF}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IPinPairs,
	]
	default_interface = IPinPairs

class PinPairsMutable(CoClassBaseClass): # A CoClass
	# The pin pairs mutable collection that allows adding or removing pin pair items.
	CLSID = IID('{31380624-17C9-4E40-8A0D-826E88AC4589}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IPinPairsMutable,
	]
	default_interface = IPinPairsMutable

class PinSet(CoClassBaseClass): # A CoClass
	# The pin set object.
	CLSID = IID('{58AF7426-636E-4771-8BA8-06179F6D3A0B}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IPinSet,
	]
	default_interface = IPinSet

class PinSets(CoClassBaseClass): # A CoClass
	# The pin set base collection that allows accessing pin set items only.
	CLSID = IID('{9670C07E-EF9C-4FF8-9DE7-EDEA3B5868A3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IPinSets,
	]
	default_interface = IPinSets

class PinSetsMutable(CoClassBaseClass): # A CoClass
	# The pin sets mutable collection that allows adding or removing pin set items.
	CLSID = IID('{EDCACA3C-AF91-401F-970F-CF31FC29E3AE}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IPinSetsMutable,
	]
	default_interface = IPinSetsMutable

class Pins(CoClassBaseClass): # A CoClass
	# The pin base collection that allows accessing pin items only.
	CLSID = IID('{BEBB09AC-7396-4C74-9423-9BFA9D766B1F}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IPins,
	]
	default_interface = IPins

class PinsMutable(CoClassBaseClass): # A CoClass
	# The pins mutable collection that allows inserting or removing pin items.
	CLSID = IID('{F6D6CDD0-C76D-4243-A552-2A37424621A0}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IPinsMutable,
	]
	default_interface = IPinsMutable

class PowerNets(CoClassBaseClass): # A CoClass
	# The power nets base collection that allows accessing power net items only.
	CLSID = IID('{0798D9AB-9C3F-4E6D-8C31-382798093C5B}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IPowerNets,
	]
	default_interface = IPowerNets

class PowerNetsMutable(CoClassBaseClass): # A CoClass
	# The power nets mutable collection is provided for future usage.
	CLSID = IID('{AFF3111C-9B72-46E6-9E5F-0A241014C7C1}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IPowerNetsMutable,
	]
	default_interface = IPowerNetsMutable

class RuleLayer(CoClassBaseClass): # A CoClass
	# The rule layer object.
	CLSID = IID('{A4733E8D-B970-4077-AC69-E6578DC3FB93}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IRuleLayer,
	]
	default_interface = IRuleLayer

class RuleLayers(CoClassBaseClass): # A CoClass
	# The rule layers base collection that allows accessing rule layer items only.
	CLSID = IID('{756E21CB-A264-4D2A-B086-0B12F97D0FB5}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IRuleLayers,
	]
	default_interface = IRuleLayers

class Scheme(CoClassBaseClass): # A CoClass
	# The scheme object.
	CLSID = IID('{0A5EE769-4E45-41A0-98EE-9BFE90EDB47D}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IScheme,
	]
	default_interface = IScheme

class SchemeClearanceRule(CoClassBaseClass): # A CoClass
	# The scheme clearance rule object.
	CLSID = IID('{150A1D3E-3113-420A-9322-80966E1D7B42}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISchemeClearanceRule,
	]
	default_interface = ISchemeClearanceRule

class SchemeClearanceRules(CoClassBaseClass): # A CoClass
	# The scheme clearance rules base collection that allows accessing scheme clearance rule items only.
	CLSID = IID('{9CA49EA5-F767-4CD7-827C-9566CC755DDB}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISchemeClearanceRules,
	]
	default_interface = ISchemeClearanceRules

class SchemeNetClass(CoClassBaseClass): # A CoClass
	# The scheme net class object.
	CLSID = IID('{4262249B-F52C-4618-9643-BD9C1D625E87}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISchemeNetClass,
	]
	default_interface = ISchemeNetClass

class SchemeNetClasses(CoClassBaseClass): # A CoClass
	# The scheme net classes base collection that allows accessing scheme net class items only.
	CLSID = IID('{42D9D034-924A-4439-9747-D6441A45571A}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISchemeNetClasses,
	]
	default_interface = ISchemeNetClasses

class Schemes(CoClassBaseClass): # A CoClass
	# The schemes base collection that allows accessing scheme items only.
	CLSID = IID('{47D1E5C7-D510-4D3D-9EE3-8A19493FAC71}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISchemes,
	]
	default_interface = ISchemes

class SchemesMutable(CoClassBaseClass): # A CoClass
	# The schemes mutable collection that allows adding or removing scheme items.
	CLSID = IID('{1855D335-FBB0-475E-B448-9F6C0D035807}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISchemesMutable,
	]
	default_interface = ISchemesMutable

class Settings(CoClassBaseClass): # A CoClass
	# The design settings object.
	CLSID = IID('{5B3D4D1E-F433-41E5-A6CF-1166E1812E45}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISettings,
	]
	default_interface = ISettings

class Stackup(CoClassBaseClass): # A CoClass
	# The design stackup object.
	CLSID = IID('{A9F41CFA-8BA3-4D5A-A002-D4E2C9F54CD2}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IStackup,
	]
	default_interface = IStackup

class Topology(CoClassBaseClass): # A CoClass
	# The topology object.
	CLSID = IID('{31529548-2AD2-4506-854D-E81C61784146}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ITopology,
	]
	default_interface = ITopology

class Units(CoClassBaseClass): # A CoClass
	# The design units object.
	CLSID = IID('{58F0FCDE-99F8-49B8-B105-EB6B93C25616}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IUnits,
	]
	default_interface = IUnits

class Variable(CoClassBaseClass): # A CoClass
	# The variable object.
	CLSID = IID('{401B8E73-606E-42F1-A576-EEFB1EADDD08}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVariable,
	]
	default_interface = IVariable

class Variables(CoClassBaseClass): # A CoClass
	# The variables base collection that allows accessing variable items only.
	CLSID = IID('{D99D85C4-7960-4462-B02F-193CCD7DA13B}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVariables,
	]
	default_interface = IVariables

class VariablesMutable(CoClassBaseClass): # A CoClass
	# The variables mutable collection that allows adding or removing variable items.
	CLSID = IID('{43B955FB-3E8A-4B7F-92FC-821418613BF8}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVariablesMutable,
	]
	default_interface = IVariablesMutable

IBase_vtables_dispatch_ = 1
IBase_vtables_ = [
	(( 'Name' , 'p_pName' , ), 0, (0, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'p_ppObject' , ), 1610743809, (1610743809, (), [ (16393, 10, None, "IID('{7A5D1A08-B723-4929-BB46-A801DC642EB6}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'IsValid' , 'p_pIsValid' , ), 1610743810, (1610743810, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'IsDefault' , 'p_pIsDefault' , ), 1610743811, (1610743811, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

IClass_vtables_dispatch_ = 1
IClass_vtables_ = [
	(( 'FullName' , 'p_pFullName' , ), 1610874880, (1610874880, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Nets' , 'p_nNetMask' , 'p_ppNets' , ), 1610874881, (1610874881, (), [ (3, 49, '1', None) , 
			 (16393, 10, None, "IID('{EAF633E9-E21E-47FF-A361-60A4B480301F}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Nets' , 'p_nNetMask' , 'p_ppNets' , ), 1610874881, (1610874881, (), [ (3, 49, '1', None) , 
			 (16393, 10, None, "IID('{EAF633E9-E21E-47FF-A361-60A4B480301F}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Rename' , 'p_strName' , ), 1610874882, (1610874882, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'AssignNet' , 'p_pNet' , ), 1610874883, (1610874883, (), [ (9, 1, None, "IID('{48420240-E6BB-423E-9FD3-F3E4687E1452}')") , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'DisplayPattern' , 'p_ppDisplayPattern' , ), 1610874884, (1610874884, (), [ (16393, 10, None, "IID('{E6F44CAC-B61D-4437-971F-60F01875D6BB}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
]

IClassClearance_vtables_dispatch_ = 1
IClassClearance_vtables_ = [
	(( 'ClassClearanceType' , 'p_pClassClearanceType' , ), 1610874880, (1610874880, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Scheme' , 'p_ppScheme' , ), 1610874881, (1610874881, (), [ (16393, 10, None, "IID('{6F39247C-17C2-4C9F-B14C-469620C80FC4}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'SourceNetClass' , 'p_ppSourceNetClass' , ), 1610874882, (1610874882, (), [ (16393, 10, None, "IID('{791A98C5-512E-45E0-8F4F-715A45F5707A}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'TargetNetClass' , 'p_ppTargetNetClass' , ), 1610874883, (1610874883, (), [ (16393, 10, None, "IID('{791A98C5-512E-45E0-8F4F-715A45F5707A}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'ClearanceRule' , 'p_ppClearanceRule' , ), 1610874884, (1610874884, (), [ (9, 1, None, "IID('{A0F38DDB-184D-4D4E-9E99-FFF4E73A4235}')") , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'ClearanceRule' , 'p_ppClearanceRule' , ), 1610874884, (1610874884, (), [ (16393, 10, None, "IID('{A0F38DDB-184D-4D4E-9E99-FFF4E73A4235}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
]

IClassClearances_vtables_dispatch_ = 1
IClassClearances_vtables_ = [
	(( 'Item' , 'p_vIndex' , 'p_ppClassClearance' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{77040253-C4BE-4037-B759-739678531FE8}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IClassClearancesMutable_vtables_dispatch_ = 1
IClassClearancesMutable_vtables_ = [
	(( 'Add' , 'p_eClassClearanceType' , 'p_strName' , 'p_pScheme' , 'p_pSourceNetClass' , 
			 'p_pTargetNetClass' , 'p_pClearanceRule' , 'p_ppClassClearance' , ), 1610874880, (1610874880, (), [ (3, 1, None, None) , 
			 (8, 1, None, None) , (9, 1, None, "IID('{6F39247C-17C2-4C9F-B14C-469620C80FC4}')") , (9, 1, None, "IID('{791A98C5-512E-45E0-8F4F-715A45F5707A}')") , (9, 1, None, "IID('{791A98C5-512E-45E0-8F4F-715A45F5707A}')") , (9, 1, None, "IID('{A0F38DDB-184D-4D4E-9E99-FFF4E73A4235}')") , 
			 (16393, 10, None, "IID('{77040253-C4BE-4037-B759-739678531FE8}')") , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Delete' , 'p_vIndex' , ), 1610874881, (1610874881, (), [ (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IClearanceRule_vtables_dispatch_ = 1
IClearanceRule_vtables_ = [
	(( 'ClearanceRuleType' , 'p_pClearanceRuleType' , ), 1610874880, (1610874880, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'ClassClearances' , 'p_ppClassClearances' , ), 1610874881, (1610874881, (), [ (16393, 10, None, "IID('{96FD6C42-8C02-4A00-A1B6-C47FB0D47913}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Layers' , 'p_ppLayers' , ), 1610874882, (1610874882, (), [ (16393, 10, None, "IID('{6710F183-E176-48F4-B3CA-DBD22E0CF5FF}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Rename' , 'p_strName' , ), 1610874883, (1610874883, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
]

IClearanceRules_vtables_dispatch_ = 1
IClearanceRules_vtables_ = [
	(( 'Item' , 'p_vIndex' , 'p_ppClearanceRule' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{A0F38DDB-184D-4D4E-9E99-FFF4E73A4235}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IClearanceRulesMutable_vtables_dispatch_ = 1
IClearanceRulesMutable_vtables_ = [
	(( 'Add' , 'p_strName' , 'p_ppClearanceRule' , ), 1610874880, (1610874880, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{A0F38DDB-184D-4D4E-9E99-FFF4E73A4235}')") , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Delete' , 'p_vIndex' , ), 1610874881, (1610874881, (), [ (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

ICollection_vtables_dispatch_ = 1
ICollection_vtables_ = [
	(( '_NewEnum' , 'p_ppRetVal' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 65 , )),
	(( 'Count' , 'p_pCount' , ), 1610743809, (1610743809, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

IComment_vtables_dispatch_ = 1
IComment_vtables_ = [
	(( 'Value' , 'p_pValue' , ), 0, (0, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Value' , 'p_pValue' , ), 0, (0, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'ConstraintType' , 'p_pConstraintType' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'p_ppObject' , ), 1610743811, (1610743811, (), [ (16393, 10, None, "IID('{7A5D1A08-B723-4929-BB46-A801DC642EB6}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

IComments_vtables_dispatch_ = 1
IComments_vtables_ = [
	(( 'Item' , 'p_vIndex' , 'p_ppComment' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{8A5D0FF3-3D6C-4AD0-9F2C-150132A98B73}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'FindItem' , 'p_eType' , 'p_ppComment' , ), 1610809345, (1610809345, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{8A5D0FF3-3D6C-4AD0-9F2C-150132A98B73}')") , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

ICommentsMutable_vtables_dispatch_ = 1
ICommentsMutable_vtables_ = [
	(( 'Add' , 'p_strName' , 'p_strValue' , 'p_ppComment' , ), 1610874880, (1610874880, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (16393, 10, None, "IID('{8A5D0FF3-3D6C-4AD0-9F2C-150132A98B73}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'AddByType' , 'p_eType' , 'p_strValue' , 'p_ppComment' , ), 1610874881, (1610874881, (), [ 
			 (3, 1, None, None) , (8, 1, None, None) , (16393, 10, None, "IID('{8A5D0FF3-3D6C-4AD0-9F2C-150132A98B73}')") , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Delete' , 'p_vIndex' , ), 1610874882, (1610874882, (), [ (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'DeleteByType' , 'p_eType' , ), 1610874883, (1610874883, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
]

IComponent_vtables_dispatch_ = 1
IComponent_vtables_ = [
	(( 'Pins' , 'p_ppPins' , ), 1610874880, (1610874880, (), [ (16393, 10, None, "IID('{B034C5D7-24E1-4F6A-836A-7906257DABAA}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
]

IComponents_vtables_dispatch_ = 1
IComponents_vtables_ = [
	(( 'Item' , 'p_vIndex' , 'p_ppComponent' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{60516EC5-86D9-4E16-86E7-9B66302D3A83}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IComponentsMutable_vtables_dispatch_ = 1
IComponentsMutable_vtables_ = [
]

IConstant_vtables_dispatch_ = 1
IConstant_vtables_ = [
	(( 'Value' , 'p_pValue' , ), 1610874880, (1610874880, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Value' , 'p_pValue' , ), 1610874880, (1610874880, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Rename' , 'p_strName' , ), 1610874882, (1610874882, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
]

IConstants_vtables_dispatch_ = 1
IConstants_vtables_ = [
	(( 'Item' , 'p_vIndex' , 'p_ppConstant' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{E43EED65-B104-4518-A7C0-21C3FA01B4F5}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IConstantsMutable_vtables_dispatch_ = 1
IConstantsMutable_vtables_ = [
	(( 'Add' , 'p_strName' , 'p_strValue' , 'p_ppConstant' , ), 1610874880, (1610874880, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (16393, 10, None, "IID('{E43EED65-B104-4518-A7C0-21C3FA01B4F5}')") , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Delete' , 'p_vIndex' , ), 1610874881, (1610874881, (), [ (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IConstraint_vtables_dispatch_ = 1
IConstraint_vtables_ = [
	(( 'ConstraintType' , 'p_pConstraintType' , ), 1610809344, (1610809344, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Value' , 'p_pValue' , ), 1610809345, (1610809345, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Value' , 'p_pValue' , ), 1610809345, (1610809345, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'ValueString' , 'p_pValue' , ), 1610809347, (1610809347, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'IsReadOnly' , 'p_pIsReadOnly' , ), 1610809348, (1610809348, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
]

IConstraintClass_vtables_dispatch_ = 1
IConstraintClass_vtables_ = [
	(( 'DelayType' , 'p_pDelayType' , ), 1610940416, (1610940416, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'DelayType' , 'p_pDelayType' , ), 1610940416, (1610940416, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'TopologyType' , 'p_pTopologyType' , ), 1610940418, (1610940418, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'TopologyType' , 'p_pTopologyType' , ), 1610940418, (1610940418, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'ConstraintClasses' , 'p_nConstraintClassMask' , 'p_ppConstraintClasses' , ), 1610940420, (1610940420, (), [ (3, 49, '2', None) , 
			 (16393, 10, None, "IID('{E4076B8B-3F93-407C-8E18-9DD473F3C4B6}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'ConstraintClasses' , 'p_nConstraintClassMask' , 'p_ppConstraintClasses' , ), 1610940420, (1610940420, (), [ (3, 49, '2', None) , 
			 (16393, 10, None, "IID('{E4076B8B-3F93-407C-8E18-9DD473F3C4B6}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'NetClass' , 'p_ppNetClass' , ), 1610940421, (1610940421, (), [ (16393, 10, None, "IID('{791A98C5-512E-45E0-8F4F-715A45F5707A}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'MoveTo' , 'p_pParentConstraintClass' , ), 1610940422, (1610940422, (), [ (9, 1, None, "IID('{CB59FE57-0379-43C2-86FF-E6E0D31CBAB9}')") , ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'NoiseRules' , 'p_ppNoiseRules' , ), 1610940423, (1610940423, (), [ (16393, 10, None, "IID('{ED063FFC-209C-48D7-8D59-6677873C9A7A}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
]

IConstraintClasses_vtables_dispatch_ = 1
IConstraintClasses_vtables_ = [
	(( 'Item' , 'p_vIndex' , 'p_ppConstraintClass' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{CB59FE57-0379-43C2-86FF-E6E0D31CBAB9}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IConstraintClassesMutable_vtables_dispatch_ = 1
IConstraintClassesMutable_vtables_ = [
	(( 'Add' , 'p_strName' , 'p_ppConstraintClass' , ), 1610874880, (1610874880, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{CB59FE57-0379-43C2-86FF-E6E0D31CBAB9}')") , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Insert' , 'p_pConstraintClass' , ), 1610874881, (1610874881, (), [ (9, 1, None, "IID('{CB59FE57-0379-43C2-86FF-E6E0D31CBAB9}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Remove' , 'p_vIndex' , ), 1610874882, (1610874882, (), [ (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Delete' , 'p_vIndex' , ), 1610874883, (1610874883, (), [ (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
]

IConstraints_vtables_dispatch_ = 1
IConstraints_vtables_ = [
	(( 'Item' , 'p_vIndex' , 'p_ppConstraint' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{7C5585B1-767E-47E1-8BC9-F4564CA62236}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'FindItem' , 'p_eType' , 'p_ppConstraint' , ), 1610809345, (1610809345, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{7C5585B1-767E-47E1-8BC9-F4564CA62236}')") , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

IConstraintsAuto_vtables_dispatch_ = 1
IConstraintsAuto_vtables_ = [
	(( 'Design' , 'p_ppDesign' , ), 1610743808, (1610743808, (), [ (16393, 10, None, "IID('{416A557D-9764-45C2-B656-BC53A72B6DDC}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Settings' , 'p_ppSettings' , ), 1610743809, (1610743809, (), [ (16393, 10, None, "IID('{8D9E96B8-678C-4EC9-93EE-F7E4CEC025FB}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Validate' , 'p_dSeed' , 'p_pKey' , ), 1610743810, (1610743810, (), [ (3, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IConstraintsMutable_vtables_dispatch_ = 1
IConstraintsMutable_vtables_ = [
	(( 'Add' , 'p_strName' , 'p_vValue' , 'p_ppConstraint' , ), 1610874880, (1610874880, (), [ 
			 (8, 1, None, None) , (12, 1, None, None) , (16393, 10, None, "IID('{7C5585B1-767E-47E1-8BC9-F4564CA62236}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'AddByType' , 'p_eType' , 'p_vValue' , 'p_ppConstraint' , ), 1610874881, (1610874881, (), [ 
			 (3, 1, None, None) , (12, 1, None, None) , (16393, 10, None, "IID('{7C5585B1-767E-47E1-8BC9-F4564CA62236}')") , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Delete' , 'p_vIndex' , ), 1610874882, (1610874882, (), [ (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'DeleteByType' , 'p_eType' , ), 1610874883, (1610874883, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
]

IDRC_vtables_dispatch_ = 1
IDRC_vtables_ = [
	(( 'Status' , 'p_pStatus' , ), 0, (0, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Description' , 'p_pDescription' , ), 1610743809, (1610743809, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

IDesign_vtables_dispatch_ = 1
IDesign_vtables_ = [
	(( 'CreateDesignParams' , 'p_ppDesignParams' , ), 1610743808, (1610743808, (), [ (16393, 10, None, "IID('{3CD8028B-F3A2-4077-8F4F-83A89F4DD990}')") , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Load' , 'p_pDesignParams' , ), 1610743809, (1610743809, (), [ (9, 1, None, "IID('{3CD8028B-F3A2-4077-8F4F-83A89F4DD990}')") , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'UnLoad' , ), 1610743810, (1610743810, (), [ ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Nets' , 'p_nNetMask' , 'p_ppNets' , ), 1610743811, (1610743811, (), [ (3, 49, '1', None) , 
			 (16393, 10, None, "IID('{17F8541C-BB01-40FC-AAFD-179AA166F42D}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Nets' , 'p_nNetMask' , 'p_ppNets' , ), 1610743811, (1610743811, (), [ (3, 49, '1', None) , 
			 (16393, 10, None, "IID('{17F8541C-BB01-40FC-AAFD-179AA166F42D}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'ElectricalNets' , 'p_ppElectricalNets' , ), 1610743812, (1610743812, (), [ (16393, 10, None, "IID('{6F698C72-5BBF-4DEE-A09C-065A7AB68829}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'PowerNets' , 'p_ppPowerNets' , ), 1610743813, (1610743813, (), [ (16393, 10, None, "IID('{B224A038-B04A-47E1-8F9F-C7938C61FD68}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'DifferentialPairs' , 'p_ppDifferentialPairs' , ), 1610743814, (1610743814, (), [ (16393, 10, None, "IID('{7E649A6C-5038-4FD1-94D9-44A56CAC894E}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'ConstraintClasses' , 'p_nConstraintClassMask' , 'p_ppConstraintClasses' , ), 1610743815, (1610743815, (), [ (3, 49, '2', None) , 
			 (16393, 10, None, "IID('{E4076B8B-3F93-407C-8E18-9DD473F3C4B6}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'ConstraintClasses' , 'p_nConstraintClassMask' , 'p_ppConstraintClasses' , ), 1610743815, (1610743815, (), [ (3, 49, '2', None) , 
			 (16393, 10, None, "IID('{E4076B8B-3F93-407C-8E18-9DD473F3C4B6}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'NetClasses' , 'p_nNetClassMask' , 'p_ppNetClasses' , ), 1610743816, (1610743816, (), [ (3, 49, '2', None) , 
			 (16393, 10, None, "IID('{DAA15140-C478-41AE-90D4-8782BA3A8707}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'NetClasses' , 'p_nNetClassMask' , 'p_ppNetClasses' , ), 1610743816, (1610743816, (), [ (3, 49, '2', None) , 
			 (16393, 10, None, "IID('{DAA15140-C478-41AE-90D4-8782BA3A8707}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'ClearanceRules' , 'p_ppClearanceRules' , ), 1610743817, (1610743817, (), [ (16393, 10, None, "IID('{088425F1-88A0-4675-B9B9-D6FBC0454CF3}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'MatchGroups' , 'p_nMatchGroupMask' , 'p_ppMatchGroups' , ), 1610743818, (1610743818, (), [ (3, 49, '3', None) , 
			 (16393, 10, None, "IID('{F36348AB-8180-41C3-951F-0B079E3FF03F}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'MatchGroups' , 'p_nMatchGroupMask' , 'p_ppMatchGroups' , ), 1610743818, (1610743818, (), [ (3, 49, '3', None) , 
			 (16393, 10, None, "IID('{F36348AB-8180-41C3-951F-0B079E3FF03F}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Formulas' , 'p_ppFormulas' , ), 1610743819, (1610743819, (), [ (16393, 10, None, "IID('{AF4369BD-BEF9-48A7-849A-F39065467C85}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'NoiseRules' , 'p_nNoiseRuleMask' , 'p_ppNoiseRules' , ), 1610743820, (1610743820, (), [ (3, 49, '3', None) , 
			 (16393, 10, None, "IID('{D07554EB-FCFF-48EC-AD04-C79988D20C9D}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'NoiseRules' , 'p_nNoiseRuleMask' , 'p_ppNoiseRules' , ), 1610743820, (1610743820, (), [ (3, 49, '3', None) , 
			 (16393, 10, None, "IID('{D07554EB-FCFF-48EC-AD04-C79988D20C9D}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'ParallelismRules' , 'p_ppParallelismRule' , ), 1610743821, (1610743821, (), [ (16393, 10, None, "IID('{E37D92BA-6E24-45E0-859C-43A40855C3AD}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Components' , 'p_ppComponents' , ), 1610743822, (1610743822, (), [ (16393, 10, None, "IID('{E010B178-C036-4BDE-815F-9B48CE213D1E}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Parts' , 'p_ppParts' , ), 1610743823, (1610743823, (), [ (16393, 10, None, "IID('{965F3ED3-C357-4CD4-8778-9B61B12D5D24}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Constants' , 'p_ppConstants' , ), 1610743824, (1610743824, (), [ (16393, 10, None, "IID('{3C22162A-1920-4AF1-B2BA-805CC3A2500C}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Variables' , 'p_ppVariables' , ), 1610743825, (1610743825, (), [ (16393, 10, None, "IID('{9B803C91-3B87-4F74-810E-C038E63376B7}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Stackup' , 'p_ppStackup' , ), 1610743826, (1610743826, (), [ (16393, 10, None, "IID('{FBFDBD21-1B6F-4263-A285-6FB6E9C7747F}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'PhysicalRules' , 'p_ppPhysicalRules' , ), 1610743827, (1610743827, (), [ (16393, 10, None, "IID('{F1F96334-F630-42BA-A3F4-2D314D51D535}')") , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'DisplayPatterns' , 'p_ppDisplayPatterns' , ), 1610743828, (1610743828, (), [ (16393, 10, None, "IID('{209DB434-B7A4-4CF7-A1DC-87CFD2B21543}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'PackageTypes' , 'p_ppPackageTypes' , ), 1610743829, (1610743829, (), [ (16393, 10, None, "IID('{EA65AC00-04E5-42F6-AC61-7FA81534926F}')") , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
]

IDesignParams_vtables_dispatch_ = 1
IDesignParams_vtables_ = [
	(( 'ProjectFile' , 'p_pProjectFile' , ), 1610743808, (1610743808, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'ProjectFile' , 'p_pProjectFile' , ), 1610743808, (1610743808, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'DesignContext' , 'p_pDesignContext' , ), 1610743810, (1610743810, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'DesignContext' , 'p_pDesignContext' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Board' , 'p_pBoard' , ), 1610743812, (1610743812, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Board' , 'p_pBoard' , ), 1610743812, (1610743812, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IDifferentialPair_vtables_dispatch_ = 1
IDifferentialPair_vtables_ = [
	(( 'FirstNet' , 'p_ppNet' , ), 1610940416, (1610940416, (), [ (16393, 10, None, "IID('{48420240-E6BB-423E-9FD3-F3E4687E1452}')") , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'SecondNet' , 'p_ppNet' , ), 1610940417, (1610940417, (), [ (16393, 10, None, "IID('{48420240-E6BB-423E-9FD3-F3E4687E1452}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Nets' , 'p_ppNets' , ), 1610940418, (1610940418, (), [ (16393, 10, None, "IID('{EAF633E9-E21E-47FF-A361-60A4B480301F}')") , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Rename' , 'p_strName' , ), 1610940419, (1610940419, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
]

IDifferentialPairs_vtables_dispatch_ = 1
IDifferentialPairs_vtables_ = [
	(( 'Item' , 'p_vIndex' , 'p_ppDifferentialPair' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{90FF1694-9C25-4F12-A08B-999F24686B57}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IDifferentialPairsMutable_vtables_dispatch_ = 1
IDifferentialPairsMutable_vtables_ = [
	(( 'Add' , 'p_pNet1' , 'p_pNet2' , 'p_ppDifferentialPair' , ), 1610874880, (1610874880, (), [ 
			 (9, 1, None, "IID('{48420240-E6BB-423E-9FD3-F3E4687E1452}')") , (9, 1, None, "IID('{48420240-E6BB-423E-9FD3-F3E4687E1452}')") , (16393, 10, None, "IID('{90FF1694-9C25-4F12-A08B-999F24686B57}')") , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Delete' , 'p_vIndex' , ), 1610874881, (1610874881, (), [ (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IDisplayPattern_vtables_dispatch_ = 1
IDisplayPattern_vtables_ = [
	(( 'Nets' , 'p_nNetMask' , 'p_ppNets' , ), 1610874880, (1610874880, (), [ (3, 49, '1', None) , 
			 (16393, 10, None, "IID('{17F8541C-BB01-40FC-AAFD-179AA166F42D}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Nets' , 'p_nNetMask' , 'p_ppNets' , ), 1610874880, (1610874880, (), [ (3, 49, '1', None) , 
			 (16393, 10, None, "IID('{17F8541C-BB01-40FC-AAFD-179AA166F42D}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'NetClasses' , 'p_ppNets' , ), 1610874881, (1610874881, (), [ (16393, 10, None, "IID('{DAA15140-C478-41AE-90D4-8782BA3A8707}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'ConstraintClasses' , 'p_ppNets' , ), 1610874882, (1610874882, (), [ (16393, 10, None, "IID('{E4076B8B-3F93-407C-8E18-9DD473F3C4B6}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Rename' , 'p_strName' , ), 1610874883, (1610874883, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
]

IDisplayPatterns_vtables_dispatch_ = 1
IDisplayPatterns_vtables_ = [
	(( 'Item' , 'p_vIndex' , 'p_ppDisplayPattern' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{E6F44CAC-B61D-4437-971F-60F01875D6BB}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'FindItem' , 'p_vColor' , 'p_vPatternIndex' , 'p_bPatternOutline' , 'p_vPatternTransparency' , 
			 'p_bPatternTransparent' , 'p_ppDisplayPattern' , ), 1610809345, (1610809345, (), [ (12, 1, None, None) , (12, 49, '1', None) , 
			 (11, 49, 'True', None) , (12, 49, '100', None) , (11, 49, 'False', None) , (16393, 10, None, "IID('{E6F44CAC-B61D-4437-971F-60F01875D6BB}')") , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

IDisplayPatternsMutable_vtables_dispatch_ = 1
IDisplayPatternsMutable_vtables_ = [
	(( 'Add' , 'p_strName' , 'p_vColor' , 'p_vPatternIndex' , 'p_bPatternOutline' , 
			 'p_vPatternTransparency' , 'p_bPatternTransparent' , 'p_ppDisplayPattern' , ), 1610874880, (1610874880, (), [ (8, 1, None, None) , 
			 (12, 1, None, None) , (12, 49, '1', None) , (11, 49, 'True', None) , (12, 49, '100', None) , (11, 49, 'False', None) , 
			 (16393, 10, None, "IID('{E6F44CAC-B61D-4437-971F-60F01875D6BB}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Delete' , 'p_vIndex' , ), 1610874881, (1610874881, (), [ (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IElectricalNet_vtables_dispatch_ = 1
IElectricalNet_vtables_ = [
	(( 'Nets' , 'p_ppNets' , ), 1610940416, (1610940416, (), [ (16393, 10, None, "IID('{EAF633E9-E21E-47FF-A361-60A4B480301F}')") , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
]

IElectricalNets_vtables_dispatch_ = 1
IElectricalNets_vtables_ = [
	(( 'Item' , 'p_vIndex' , 'p_ppElectricalNet' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{7DB3D012-77AB-47DF-9C24-9A297A370AD0}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IElectricalNetsMutable_vtables_dispatch_ = 1
IElectricalNetsMutable_vtables_ = [
]

IFormula_vtables_dispatch_ = 1
IFormula_vtables_ = [
	(( 'Value' , 'p_pValue' , ), 1610874880, (1610874880, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Value' , 'p_pValue' , ), 1610874880, (1610874880, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Begin' , ), 1610874882, (1610874882, (), [ ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Commit' , ), 1610874883, (1610874883, (), [ ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Rollback' , ), 1610874884, (1610874884, (), [ ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'AddObject' , 'p_pObject' , ), 1610874885, (1610874885, (), [ (9, 1, None, "IID('{7A5D1A08-B723-4929-BB46-A801DC642EB6}')") , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'AddText' , 'p_strText' , ), 1610874886, (1610874886, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'AddOperator' , 'p_eOperator' , ), 1610874887, (1610874887, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Clear' , ), 1610874888, (1610874888, (), [ ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
]

IFormulas_vtables_dispatch_ = 1
IFormulas_vtables_ = [
	(( 'Item' , 'p_vIndex' , 'p_ppFormula' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{A59586BA-4C99-4643-B6F8-E42BBF2E00D2}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IFormulasMutable_vtables_dispatch_ = 1
IFormulasMutable_vtables_ = [
]

IFromTo_vtables_dispatch_ = 1
IFromTo_vtables_ = [
	(( 'FirstPin' , 'p_ppPin' , ), 1610874880, (1610874880, (), [ (16393, 10, None, "IID('{1B2620CF-90B0-4E6B-9CDF-A1799A578FDC}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'SecondPin' , 'p_ppPin' , ), 1610874881, (1610874881, (), [ (16393, 10, None, "IID('{1B2620CF-90B0-4E6B-9CDF-A1799A578FDC}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Pins' , 'p_ppPins' , ), 1610874882, (1610874882, (), [ (16393, 10, None, "IID('{3F1B4618-0423-42B9-A741-72E65CE0E573}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
]

IFromTos_vtables_dispatch_ = 1
IFromTos_vtables_ = [
	(( 'Item' , 'p_vIndex' , 'p_ppFromTo' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{0DEB5A91-FF99-4B23-BAD2-4B5C2C84D5BF}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IFromTosMutable_vtables_dispatch_ = 1
IFromTosMutable_vtables_ = [
	(( 'Add' , 'p_pPin1' , 'p_pPin2' , 'p_ppFromTo' , ), 1610874880, (1610874880, (), [ 
			 (9, 1, None, "IID('{1B2620CF-90B0-4E6B-9CDF-A1799A578FDC}')") , (9, 1, None, "IID('{1B2620CF-90B0-4E6B-9CDF-A1799A578FDC}')") , (16393, 10, None, "IID('{0DEB5A91-FF99-4B23-BAD2-4B5C2C84D5BF}')") , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Delete' , 'p_vIndex' , ), 1610874881, (1610874881, (), [ (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IGeneralClearance_vtables_dispatch_ = 1
IGeneralClearance_vtables_ = [
	(( 'GeneralClearanceType' , 'p_pType' , ), 1610874880, (1610874880, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'ClearanceType' , 'p_pType' , ), 1610874881, (1610874881, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
]

IGeneralClearances_vtables_dispatch_ = 1
IGeneralClearances_vtables_ = [
	(( 'Item' , 'p_vIndex' , 'p_ppGeneralClearance' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{D7ABE808-2624-4912-B413-96F9E0B5BA5B}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'FindItem' , 'p_eType' , 'p_ppGeneralClearance' , ), 1610809345, (1610809345, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{D7ABE808-2624-4912-B413-96F9E0B5BA5B}')") , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

IGeneralClearancesMutable_vtables_dispatch_ = 1
IGeneralClearancesMutable_vtables_ = [
	(( 'Add' , 'p_strName' , 'p_ppGeneralClearance' , ), 1610874880, (1610874880, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{D7ABE808-2624-4912-B413-96F9E0B5BA5B}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'AddByType' , 'p_eType' , 'p_ppGeneralClearance' , ), 1610874881, (1610874881, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{D7ABE808-2624-4912-B413-96F9E0B5BA5B}')") , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Delete' , 'p_vIndex' , ), 1610874882, (1610874882, (), [ (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'DeleteByType' , 'p_eType' , ), 1610874883, (1610874883, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
]

ILayer_vtables_dispatch_ = 1
ILayer_vtables_ = [
	(( 'Index' , 'p_pIndex' , ), 1610874880, (1610874880, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'MetallicIndex' , 'p_pMetallicIndex' , ), 1610874881, (1610874881, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'LayerType' , 'p_pLayerType' , ), 1610874882, (1610874882, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'LayerUsage' , 'p_pLayerUsage' , ), 1610874883, (1610874883, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
]

ILayers_vtables_dispatch_ = 1
ILayers_vtables_ = [
	(( 'MetallicCount' , 'p_pMetallicCount' , ), 1610809344, (1610809344, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'p_vIndex' , 'p_ppLayer' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{052E8B90-0E4C-44C1-8F39-89E344392B5C}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

ILayersMutable_vtables_dispatch_ = 1
ILayersMutable_vtables_ = [
]

IMatchGroup_vtables_dispatch_ = 1
IMatchGroup_vtables_ = [
	(( 'MatchGroupType' , 'p_pMatchGroupType' , ), 1610874880, (1610874880, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'DelayType' , 'p_pDelayType' , ), 1610874881, (1610874881, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'DelayType' , 'p_pDelayType' , ), 1610874881, (1610874881, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Nets' , 'p_nNetMask' , 'p_ppNets' , ), 1610874883, (1610874883, (), [ (3, 49, '15', None) , 
			 (16393, 10, None, "IID('{17F8541C-BB01-40FC-AAFD-179AA166F42D}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Nets' , 'p_nNetMask' , 'p_ppNets' , ), 1610874883, (1610874883, (), [ (3, 49, '15', None) , 
			 (16393, 10, None, "IID('{17F8541C-BB01-40FC-AAFD-179AA166F42D}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'PinPairs' , 'p_ppPinPairs' , ), 1610874884, (1610874884, (), [ (16393, 10, None, "IID('{0D52DE96-799A-4660-ACFE-109F34DEE67B}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Rename' , 'p_strName' , ), 1610874885, (1610874885, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
]

IMatchGroups_vtables_dispatch_ = 1
IMatchGroups_vtables_ = [
	(( 'Item' , 'p_vIndex' , 'p_ppMatchGroup' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{141C68A8-5519-4BD9-887B-C02B3E31E9F0}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'FindItem' , 'p_eType' , 'p_strName' , 'p_ppMatchGroup' , ), 1610809345, (1610809345, (), [ 
			 (3, 1, None, None) , (8, 1, None, None) , (16393, 10, None, "IID('{141C68A8-5519-4BD9-887B-C02B3E31E9F0}')") , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

IMatchGroupsMutable_vtables_dispatch_ = 1
IMatchGroupsMutable_vtables_ = [
	(( 'Add' , 'p_eType' , 'p_strName' , 'p_vTolerance' , 'p_ppMatchGroup' , 
			 ), 1610874880, (1610874880, (), [ (3, 1, None, None) , (8, 1, None, None) , (12, 17, None, None) , (16393, 10, None, "IID('{141C68A8-5519-4BD9-887B-C02B3E31E9F0}')") , ], 1 , 1 , 4 , 1 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Delete' , 'p_vIndex' , ), 1610874881, (1610874881, (), [ (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'DeleteByType' , 'p_eType' , 'p_strName' , ), 1610874882, (1610874882, (), [ (3, 1, None, None) , 
			 (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
]

INet_vtables_dispatch_ = 1
INet_vtables_ = [
	(( 'NetType' , 'p_pNetType' , ), 1610874880, (1610874880, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'NetType' , 'p_pNetType' , ), 1610874880, (1610874880, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'DelayType' , 'p_pDelayType' , ), 1610874882, (1610874882, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'DelayType' , 'p_pDelayType' , ), 1610874882, (1610874882, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Topology' , 'p_ppTopology' , ), 1610874884, (1610874884, (), [ (16393, 10, None, "IID('{E827A25D-2BEB-4013-9E2B-035133E06025}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'ConstraintClass' , 'p_ppConstraintClass' , ), 1610874885, (1610874885, (), [ (16393, 10, None, "IID('{CB59FE57-0379-43C2-86FF-E6E0D31CBAB9}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'NetClass' , 'p_ppNetClass' , ), 1610874886, (1610874886, (), [ (16393, 10, None, "IID('{791A98C5-512E-45E0-8F4F-715A45F5707A}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'MatchGroups' , 'p_nMatchGroupMask' , 'p_ppMatchGroups' , ), 1610874887, (1610874887, (), [ (3, 49, '3', None) , 
			 (16393, 10, None, "IID('{1F460B56-507F-4CA6-B8D7-676CBB2427BD}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'MatchGroups' , 'p_nMatchGroupMask' , 'p_ppMatchGroups' , ), 1610874887, (1610874887, (), [ (3, 49, '3', None) , 
			 (16393, 10, None, "IID('{1F460B56-507F-4CA6-B8D7-676CBB2427BD}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Formula' , 'p_ppFormula' , ), 1610874888, (1610874888, (), [ (16393, 10, None, "IID('{A59586BA-4C99-4643-B6F8-E42BBF2E00D2}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'NoiseRules' , 'p_ppNoiseRules' , ), 1610874889, (1610874889, (), [ (16393, 10, None, "IID('{ED063FFC-209C-48D7-8D59-6677873C9A7A}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'DisplayPattern' , 'p_ppDisplayPattern' , ), 1610874890, (1610874890, (), [ (16393, 10, None, "IID('{E6F44CAC-B61D-4437-971F-60F01875D6BB}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
]

INetClass_vtables_dispatch_ = 1
INetClass_vtables_ = [
	(( 'NetClasses' , 'p_nNetClassMask' , 'p_ppNetClasses' , ), 1610940416, (1610940416, (), [ (3, 49, '2', None) , 
			 (16393, 10, None, "IID('{DAA15140-C478-41AE-90D4-8782BA3A8707}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'NetClasses' , 'p_nNetClassMask' , 'p_ppNetClasses' , ), 1610940416, (1610940416, (), [ (3, 49, '2', None) , 
			 (16393, 10, None, "IID('{DAA15140-C478-41AE-90D4-8782BA3A8707}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'ConstraintClasses' , 'p_ppConstraintClasses' , ), 1610940417, (1610940417, (), [ (16393, 10, None, "IID('{7D9A71CB-B02F-4A1B-9995-2ADF58C69494}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'MoveTo' , 'p_pParentNetClass' , ), 1610940418, (1610940418, (), [ (9, 1, None, "IID('{791A98C5-512E-45E0-8F4F-715A45F5707A}')") , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'AssignConstraintClass' , 'p_pConstraintClass' , ), 1610940419, (1610940419, (), [ (9, 1, None, "IID('{CB59FE57-0379-43C2-86FF-E6E0D31CBAB9}')") , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'ClassClearances' , 'p_nClassClearancesMask' , 'p_ppClassClearances' , ), 1610940420, (1610940420, (), [ (3, 49, '3', None) , 
			 (16393, 10, None, "IID('{96FD6C42-8C02-4A00-A1B6-C47FB0D47913}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'ClassClearances' , 'p_nClassClearancesMask' , 'p_ppClassClearances' , ), 1610940420, (1610940420, (), [ (3, 49, '3', None) , 
			 (16393, 10, None, "IID('{96FD6C42-8C02-4A00-A1B6-C47FB0D47913}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
]

INetClasses_vtables_dispatch_ = 1
INetClasses_vtables_ = [
	(( 'Item' , 'p_vIndex' , 'p_ppNetClass' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{791A98C5-512E-45E0-8F4F-715A45F5707A}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

INetClassesMutable_vtables_dispatch_ = 1
INetClassesMutable_vtables_ = [
	(( 'Add' , 'p_strName' , 'p_ppNetClass' , ), 1610874880, (1610874880, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{791A98C5-512E-45E0-8F4F-715A45F5707A}')") , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Insert' , 'p_pNetClass' , ), 1610874881, (1610874881, (), [ (9, 1, None, "IID('{791A98C5-512E-45E0-8F4F-715A45F5707A}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Remove' , 'p_vIndex' , ), 1610874882, (1610874882, (), [ (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Delete' , 'p_vIndex' , ), 1610874883, (1610874883, (), [ (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
]

INets_vtables_dispatch_ = 1
INets_vtables_ = [
	(( 'Item' , 'p_vIndex' , 'p_ppNet' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{48420240-E6BB-423E-9FD3-F3E4687E1452}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

INetsMutable_vtables_dispatch_ = 1
INetsMutable_vtables_ = [
	(( 'Insert' , 'p_pNet' , ), 1610874880, (1610874880, (), [ (9, 1, None, "IID('{48420240-E6BB-423E-9FD3-F3E4687E1452}')") , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Remove' , 'p_vIndex' , ), 1610874881, (1610874881, (), [ (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

INoiseRule_vtables_dispatch_ = 1
INoiseRule_vtables_ = [
	(( 'Rename' , 'p_strName' , ), 1610874880, (1610874880, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'NoiseRuleType' , 'p_eNoiseRuleType' , ), 1610874881, (1610874881, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Victim' , 'p_pVictim' , ), 1610874882, (1610874882, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Victim' , 'p_pVictim' , ), 1610874882, (1610874882, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Aggressor' , 'p_pAggressor' , ), 1610874884, (1610874884, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Aggressor' , 'p_pAggressor' , ), 1610874884, (1610874884, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'ParallelismRule' , 'p_ppParallelismRule' , ), 1610874886, (1610874886, (), [ (9, 1, None, "IID('{A11D8E06-CE97-402B-AFD5-D75BACE22E1A}')") , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'ParallelismRule' , 'p_ppParallelismRule' , ), 1610874886, (1610874886, (), [ (16393, 10, None, "IID('{A11D8E06-CE97-402B-AFD5-D75BACE22E1A}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
]

INoiseRules_vtables_dispatch_ = 1
INoiseRules_vtables_ = [
	(( 'Item' , 'p_vIndex' , 'p_ppNoiseRule' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{D06D3CAD-4D4E-40B8-9A9A-16D446917F77}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

INoiseRulesMutable_vtables_dispatch_ = 1
INoiseRulesMutable_vtables_ = [
	(( 'Add' , 'p_eNoiseRuleType' , 'p_strName' , 'p_vVictim' , 'p_vAggressor' , 
			 'p_ppNoiseRule' , ), 1610874880, (1610874880, (), [ (3, 1, None, None) , (8, 1, None, None) , (12, 1, None, None) , 
			 (12, 1, None, None) , (16393, 10, None, "IID('{D06D3CAD-4D4E-40B8-9A9A-16D446917F77}')") , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Delete' , 'p_vIndex' , ), 1610874881, (1610874881, (), [ (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

INotation_vtables_dispatch_ = 1
INotation_vtables_ = [
	(( 'DecimalSymbol' , 'p_pDecimalSymbol' , ), 1610743808, (1610743808, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'DecimalSymbol' , 'p_pDecimalSymbol' , ), 1610743808, (1610743808, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'GroupSymbol' , 'p_pGroupSymbol' , ), 1610743810, (1610743810, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'GroupSymbol' , 'p_pGroupSymbol' , ), 1610743810, (1610743810, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'GroupDigitsCount' , 'p_pGroupDigitsCount' , ), 1610743812, (1610743812, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'GroupDigitsCount' , 'p_pGroupDigitsCount' , ), 1610743812, (1610743812, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'DisplayTrailingZeros' , 'p_pDisplayTrailingZeros' , ), 1610743814, (1610743814, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'DisplayTrailingZeros' , 'p_pDisplayTrailingZeros' , ), 1610743814, (1610743814, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'DisplayLeadingZeros' , 'p_pDisplayLeadingZeros' , ), 1610743816, (1610743816, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'DisplayLeadingZeros' , 'p_pDisplayLeadingZeros' , ), 1610743816, (1610743816, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Precision' , 'p_pPrecision' , ), 1610743818, (1610743818, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Precision' , 'p_pPrecision' , ), 1610743818, (1610743818, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'ColorFormat' , 'p_pColorFormat' , ), 1610743820, (1610743820, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'ColorFormat' , 'p_pColorFormat' , ), 1610743820, (1610743820, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
]

IObject_vtables_dispatch_ = 1
IObject_vtables_ = [
	(( 'ObjectType' , 'p_pObjectType' , ), 1610809344, (1610809344, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Constraints' , 'p_nConstraintMask' , 'p_ppConstraints' , ), 1610809345, (1610809345, (), [ (3, 49, '7', None) , 
			 (16393, 10, None, "IID('{1DDEC891-7D43-4EE9-9BD4-63772C577150}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Constraints' , 'p_nConstraintMask' , 'p_ppConstraints' , ), 1610809345, (1610809345, (), [ (3, 49, '7', None) , 
			 (16393, 10, None, "IID('{1DDEC891-7D43-4EE9-9BD4-63772C577150}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Comments' , 'p_ppComments' , ), 1610809346, (1610809346, (), [ (16393, 10, None, "IID('{23FAC1D8-2578-42BC-9F65-F04930FB6489}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Objects' , 'p_eObjectType' , 'p_ppObjects' , ), 1610809347, (1610809347, (), [ (3, 49, '0', None) , 
			 (16393, 10, None, "IID('{44747797-9642-483B-AB9C-6AE0A1899549}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Objects' , 'p_eObjectType' , 'p_ppObjects' , ), 1610809347, (1610809347, (), [ (3, 49, '0', None) , 
			 (16393, 10, None, "IID('{44747797-9642-483B-AB9C-6AE0A1899549}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
]

IObjects_vtables_dispatch_ = 1
IObjects_vtables_ = [
	(( 'Item' , 'p_nIndex' , 'p_ppObject' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{7A5D1A08-B723-4929-BB46-A801DC642EB6}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'FindItem' , 'p_eType' , 'p_strName' , 'p_ppObject' , ), 1610809345, (1610809345, (), [ 
			 (3, 1, None, None) , (8, 1, None, None) , (16393, 10, None, "IID('{7A5D1A08-B723-4929-BB46-A801DC642EB6}')") , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

IPackageClearance_vtables_dispatch_ = 1
IPackageClearance_vtables_ = [
	(( 'ClearanceType' , 'p_pType' , ), 1610874880, (1610874880, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'SourcePackage' , 'p_ppSourcePackage' , ), 1610874881, (1610874881, (), [ (16393, 10, None, "IID('{9253A04D-448B-459A-AF00-BC956F499198}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'TargetPackage' , 'p_ppTargetPackage' , ), 1610874882, (1610874882, (), [ (16393, 10, None, "IID('{9253A04D-448B-459A-AF00-BC956F499198}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
]

IPackageClearances_vtables_dispatch_ = 1
IPackageClearances_vtables_ = [
	(( 'Item' , 'p_vIndex' , 'p_ppPackageClearance' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{240DA68C-6822-4B65-A4B3-8E7AB10B66AE}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IPackageClearancesMutable_vtables_dispatch_ = 1
IPackageClearancesMutable_vtables_ = [
	(( 'Add' , 'p_eType' , 'p_strName' , 'p_pSourcePackage' , 'p_pTargetPackage' , 
			 'p_vSide' , 'p_vDirection' , 'p_ppPackageClearance' , ), 1610874880, (1610874880, (), [ (3, 1, None, None) , 
			 (8, 1, None, None) , (9, 1, None, "IID('{9253A04D-448B-459A-AF00-BC956F499198}')") , (9, 1, None, "IID('{9253A04D-448B-459A-AF00-BC956F499198}')") , (12, 49, "'Both'", None) , (12, 49, "'All'", None) , 
			 (16393, 10, None, "IID('{240DA68C-6822-4B65-A4B3-8E7AB10B66AE}')") , ], 1 , 1 , 4 , 0 , 80 , (3, 32, None, None) , 0 , )),
	(( 'Delete' , 'p_vIndex' , ), 1610874881, (1610874881, (), [ (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IPackageType_vtables_dispatch_ = 1
IPackageType_vtables_ = [
	(( 'PackageClearances' , 'p_nClearanceMask' , 'p_ppPackageClearances' , ), 1610874880, (1610874880, (), [ (3, 49, '3', None) , 
			 (16393, 10, None, "IID('{B5A4D7C8-1D7D-42CB-8E1D-508B0BD67DCC}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'PackageClearances' , 'p_nClearanceMask' , 'p_ppPackageClearances' , ), 1610874880, (1610874880, (), [ (3, 49, '3', None) , 
			 (16393, 10, None, "IID('{B5A4D7C8-1D7D-42CB-8E1D-508B0BD67DCC}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
]

IPackageTypes_vtables_dispatch_ = 1
IPackageTypes_vtables_ = [
	(( 'Item' , 'p_vIndex' , 'p_ppPackageType' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{9253A04D-448B-459A-AF00-BC956F499198}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IPackageTypesMutable_vtables_dispatch_ = 1
IPackageTypesMutable_vtables_ = [
	(( 'Add' , 'p_strName' , 'p_ppPackageType' , ), 1610874880, (1610874880, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{9253A04D-448B-459A-AF00-BC956F499198}')") , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Delete' , 'p_vIndex' , ), 1610874881, (1610874881, (), [ (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IParallelismRule_vtables_dispatch_ = 1
IParallelismRule_vtables_ = [
	(( 'Rename' , 'p_strName' , ), 1610874880, (1610874880, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'NoiseRules' , 'p_nNoiseRuleMask' , 'p_ppNoiseRules' , ), 1610874881, (1610874881, (), [ (3, 49, '3', None) , 
			 (16393, 10, None, "IID('{ED063FFC-209C-48D7-8D59-6677873C9A7A}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'NoiseRules' , 'p_nNoiseRuleMask' , 'p_ppNoiseRules' , ), 1610874881, (1610874881, (), [ (3, 49, '3', None) , 
			 (16393, 10, None, "IID('{ED063FFC-209C-48D7-8D59-6677873C9A7A}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Segments' , 'p_nParallelismRuleSegmentMask' , 'p_ppParallelismRuleSegments' , ), 1610874882, (1610874882, (), [ (3, 49, '3', None) , 
			 (16393, 10, None, "IID('{DEB98723-9BE8-482E-A482-E511BA818C2C}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Segments' , 'p_nParallelismRuleSegmentMask' , 'p_ppParallelismRuleSegments' , ), 1610874882, (1610874882, (), [ (3, 49, '3', None) , 
			 (16393, 10, None, "IID('{DEB98723-9BE8-482E-A482-E511BA818C2C}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
]

IParallelismRuleSegment_vtables_dispatch_ = 1
IParallelismRuleSegment_vtables_ = [
	(( 'SegmentType' , 'p_eParallelismRuleSegmentType' , ), 1610874880, (1610874880, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
]

IParallelismRuleSegments_vtables_dispatch_ = 1
IParallelismRuleSegments_vtables_ = [
	(( 'Item' , 'p_vIndex' , 'p_ppParallelismRuleSegment' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{C391FA67-1209-4DD6-BD23-9D3DD7332651}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IParallelismRuleSegmentsMutable_vtables_dispatch_ = 1
IParallelismRuleSegmentsMutable_vtables_ = [
	(( 'Add' , 'p_eParallelismRuleSegmentType' , 'p_vEdge' , 'p_vMaxParallelLength' , 'p_ppParallelismRuleSegment' , 
			 ), 1610874880, (1610874880, (), [ (3, 1, None, None) , (12, 1, None, None) , (12, 1, None, None) , (16393, 10, None, "IID('{C391FA67-1209-4DD6-BD23-9D3DD7332651}')") , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Delete' , 'p_vIndex' , ), 1610874881, (1610874881, (), [ (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IParallelismRules_vtables_dispatch_ = 1
IParallelismRules_vtables_ = [
	(( 'Item' , 'p_vIndex' , 'p_ppParallelismRule' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{A11D8E06-CE97-402B-AFD5-D75BACE22E1A}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IParallelismRulesMutable_vtables_dispatch_ = 1
IParallelismRulesMutable_vtables_ = [
	(( 'Add' , 'p_pName' , 'p_ppParallelismRule' , ), 1610874880, (1610874880, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{A11D8E06-CE97-402B-AFD5-D75BACE22E1A}')") , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Delete' , 'p_vIndex' , ), 1610874881, (1610874881, (), [ (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IPart_vtables_dispatch_ = 1
IPart_vtables_ = [
	(( 'PartPins' , 'p_ppPartPins' , ), 1610874880, (1610874880, (), [ (16393, 10, None, "IID('{8596DD5E-2C99-4DED-9A1F-D9067D3D34DB}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'PartPinPairs' , 'p_ppPartPinPairs' , ), 1610874881, (1610874881, (), [ (16393, 10, None, "IID('{7DA3F078-E3B2-4436-A267-6FC09F25AB19}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Components' , 'p_ppComponents' , ), 1610874882, (1610874882, (), [ (16393, 10, None, "IID('{E010B178-C036-4BDE-815F-9B48CE213D1E}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
]

IPartPin_vtables_dispatch_ = 1
IPartPin_vtables_ = [
	(( 'PartPinPairs' , 'p_ppPartPinPairs' , ), 1610874880, (1610874880, (), [ (16393, 10, None, "IID('{44495392-B0D3-496F-8925-A5F0710C3A67}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Pins' , 'p_ppPins' , ), 1610874881, (1610874881, (), [ (16393, 10, None, "IID('{3F1B4618-0423-42B9-A741-72E65CE0E573}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
]

IPartPinPair_vtables_dispatch_ = 1
IPartPinPair_vtables_ = [
	(( 'FirstPartPin' , 'p_ppPartPin' , ), 1610874880, (1610874880, (), [ (16393, 10, None, "IID('{A6EC1810-AC7F-4B10-AA00-BBC2FCB7C929}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'SecondPartPin' , 'p_ppPartPin' , ), 1610874881, (1610874881, (), [ (16393, 10, None, "IID('{A6EC1810-AC7F-4B10-AA00-BBC2FCB7C929}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'PartPins' , 'p_ppPartPins' , ), 1610874882, (1610874882, (), [ (16393, 10, None, "IID('{1C51DCE2-A09B-4680-BF6F-9EDAF0C822B8}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
]

IPartPinPairs_vtables_dispatch_ = 1
IPartPinPairs_vtables_ = [
	(( 'Item' , 'p_vIndex' , 'p_ppPartPinPair' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{FE3B36FE-C912-41F3-88EA-542F43253414}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IPartPinPairsMutable_vtables_dispatch_ = 1
IPartPinPairsMutable_vtables_ = [
	(( 'Add' , 'p_pPartPin1' , 'p_pPartPin2' , 'p_ppPartPinPair' , ), 1610874880, (1610874880, (), [ 
			 (9, 1, None, "IID('{A6EC1810-AC7F-4B10-AA00-BBC2FCB7C929}')") , (9, 1, None, "IID('{A6EC1810-AC7F-4B10-AA00-BBC2FCB7C929}')") , (16393, 10, None, "IID('{FE3B36FE-C912-41F3-88EA-542F43253414}')") , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Delete' , 'p_vIndex' , ), 1610874881, (1610874881, (), [ (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IPartPins_vtables_dispatch_ = 1
IPartPins_vtables_ = [
	(( 'Item' , 'p_vIndex' , 'p_ppPartPin' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{A6EC1810-AC7F-4B10-AA00-BBC2FCB7C929}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IPartPinsMutable_vtables_dispatch_ = 1
IPartPinsMutable_vtables_ = [
]

IParts_vtables_dispatch_ = 1
IParts_vtables_ = [
	(( 'Item' , 'p_vIndex' , 'p_ppPart' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{2D3374B6-ED6A-4024-AC29-ACF03A09B7C5}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IPartsMutable_vtables_dispatch_ = 1
IPartsMutable_vtables_ = [
]

IPhysicalRules_vtables_dispatch_ = 1
IPhysicalRules_vtables_ = [
	(( 'Schemes' , 'p_ppSchemes' , ), 1610743808, (1610743808, (), [ (16393, 10, None, "IID('{C868C166-9607-4506-AEF9-5AE4FB428F95}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'ZAxisClearanceRules' , 'p_ppZAxisClearances' , ), 1610743809, (1610743809, (), [ (16393, 10, None, "IID('{088425F1-88A0-4675-B9B9-D6FBC0454CF3}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'ClassClearances' , 'p_nClassClearancesMask' , 'p_ppClassClearances' , ), 1610743810, (1610743810, (), [ (3, 49, '3', None) , 
			 (16393, 10, None, "IID('{FA648CF5-E9A3-4841-AD76-BD4BCD55DF45}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'ClassClearances' , 'p_nClassClearancesMask' , 'p_ppClassClearances' , ), 1610743810, (1610743810, (), [ (3, 49, '3', None) , 
			 (16393, 10, None, "IID('{FA648CF5-E9A3-4841-AD76-BD4BCD55DF45}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'GeneralClearances' , 'p_nClearanceMask' , 'p_ppGeneralClearances' , ), 1610743811, (1610743811, (), [ (3, 49, '3', None) , 
			 (16393, 10, None, "IID('{BC62A287-210A-4466-A894-5ACB1F4E0E25}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'GeneralClearances' , 'p_nClearanceMask' , 'p_ppGeneralClearances' , ), 1610743811, (1610743811, (), [ (3, 49, '3', None) , 
			 (16393, 10, None, "IID('{BC62A287-210A-4466-A894-5ACB1F4E0E25}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'PackageClearances' , 'p_nClearancesMask' , 'p_ppPackageClearances' , ), 1610743812, (1610743812, (), [ (3, 49, '3', None) , 
			 (16393, 10, None, "IID('{D2CFD11E-A067-4F0F-BE2F-17A9F507040E}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'PackageClearances' , 'p_nClearancesMask' , 'p_ppPackageClearances' , ), 1610743812, (1610743812, (), [ (3, 49, '3', None) , 
			 (16393, 10, None, "IID('{D2CFD11E-A067-4F0F-BE2F-17A9F507040E}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IPin_vtables_dispatch_ = 1
IPin_vtables_ = [
	(( 'PinType' , 'p_pPinType' , ), 1610874880, (1610874880, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Net' , 'p_ppNet' , ), 1610874881, (1610874881, (), [ (16393, 10, None, "IID('{48420240-E6BB-423E-9FD3-F3E4687E1452}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'FromTos' , 'p_ppFromTos' , ), 1610874882, (1610874882, (), [ (16393, 10, None, "IID('{9C2F6146-F58D-43EC-B1B4-F0FF99B33E31}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'PinPairs' , 'p_ppPinPairs' , ), 1610874883, (1610874883, (), [ (16393, 10, None, "IID('{AE314BDB-B6CC-4DD0-B514-1A525DA682D6}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'PinSets' , 'p_ppPinSets' , ), 1610874884, (1610874884, (), [ (16393, 10, None, "IID('{B80F7CDC-6D14-471E-9983-979FF0059B5A}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'PartPin' , 'p_ppPartPin' , ), 1610874885, (1610874885, (), [ (16393, 10, None, "IID('{A6EC1810-AC7F-4B10-AA00-BBC2FCB7C929}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
]

IPinPair_vtables_dispatch_ = 1
IPinPair_vtables_ = [
	(( 'FirstPin' , 'p_ppPin' , ), 1610874880, (1610874880, (), [ (16393, 10, None, "IID('{1B2620CF-90B0-4E6B-9CDF-A1799A578FDC}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'SecondPin' , 'p_ppPin' , ), 1610874881, (1610874881, (), [ (16393, 10, None, "IID('{1B2620CF-90B0-4E6B-9CDF-A1799A578FDC}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Pins' , 'p_ppPins' , ), 1610874882, (1610874882, (), [ (16393, 10, None, "IID('{3F1B4618-0423-42B9-A741-72E65CE0E573}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'DelayType' , 'p_pDelayType' , ), 1610874883, (1610874883, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'DelayType' , 'p_pDelayType' , ), 1610874883, (1610874883, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'MatchGroups' , 'p_nMatchGroupMask' , 'p_ppMatchGroups' , ), 1610874885, (1610874885, (), [ (3, 49, '3', None) , 
			 (16393, 10, None, "IID('{1F460B56-507F-4CA6-B8D7-676CBB2427BD}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'MatchGroups' , 'p_nMatchGroupMask' , 'p_ppMatchGroups' , ), 1610874885, (1610874885, (), [ (3, 49, '3', None) , 
			 (16393, 10, None, "IID('{1F460B56-507F-4CA6-B8D7-676CBB2427BD}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Formula' , 'p_ppFormula' , ), 1610874886, (1610874886, (), [ (16393, 10, None, "IID('{A59586BA-4C99-4643-B6F8-E42BBF2E00D2}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
]

IPinPairs_vtables_dispatch_ = 1
IPinPairs_vtables_ = [
	(( 'Item' , 'p_vIndex' , 'p_ppPinPair' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{DAE2F804-60E5-4B5F-96F0-FB5585334EAB}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IPinPairsMutable_vtables_dispatch_ = 1
IPinPairsMutable_vtables_ = [
	(( 'Add' , 'p_pPin1' , 'p_pPin2' , 'p_ppPinPair' , ), 1610874880, (1610874880, (), [ 
			 (9, 1, None, "IID('{1B2620CF-90B0-4E6B-9CDF-A1799A578FDC}')") , (9, 1, None, "IID('{1B2620CF-90B0-4E6B-9CDF-A1799A578FDC}')") , (16393, 10, None, "IID('{DAE2F804-60E5-4B5F-96F0-FB5585334EAB}')") , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Insert' , 'p_pPinPair' , ), 1610874881, (1610874881, (), [ (9, 1, None, "IID('{DAE2F804-60E5-4B5F-96F0-FB5585334EAB}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Remove' , 'p_vIndex' , ), 1610874882, (1610874882, (), [ (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Delete' , 'p_vIndex' , ), 1610874883, (1610874883, (), [ (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
]

IPinSet_vtables_dispatch_ = 1
IPinSet_vtables_ = [
	(( 'PinSetType' , 'p_pPinSetType' , ), 1610874880, (1610874880, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Pins' , 'p_ppPins' , ), 1610874881, (1610874881, (), [ (16393, 10, None, "IID('{B034C5D7-24E1-4F6A-836A-7906257DABAA}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'ConnectionPin' , 'p_ppPin' , ), 1610874882, (1610874882, (), [ (16393, 10, None, "IID('{1B2620CF-90B0-4E6B-9CDF-A1799A578FDC}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'VirtualPin' , 'p_ppPin' , ), 1610874883, (1610874883, (), [ (16393, 10, None, "IID('{1B2620CF-90B0-4E6B-9CDF-A1799A578FDC}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
]

IPinSets_vtables_dispatch_ = 1
IPinSets_vtables_ = [
	(( 'Item' , 'p_vIndex' , 'p_ppPinSet' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{5B8C932F-F283-4D9C-AD70-4B4213109BC3}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IPinSetsMutable_vtables_dispatch_ = 1
IPinSetsMutable_vtables_ = [
	(( 'Add' , 'p_ePinSetType' , 'p_pPinsArray' , 'p_ppPinSet' , ), 1610874880, (1610874880, (), [ 
			 (3, 1, None, None) , (16396, 1, None, None) , (16393, 10, None, "IID('{5B8C932F-F283-4D9C-AD70-4B4213109BC3}')") , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Delete' , 'p_vIndex' , ), 1610874881, (1610874881, (), [ (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IPins_vtables_dispatch_ = 1
IPins_vtables_ = [
	(( 'Item' , 'p_vIndex' , 'p_ppPin' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{1B2620CF-90B0-4E6B-9CDF-A1799A578FDC}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IPinsMutable_vtables_dispatch_ = 1
IPinsMutable_vtables_ = [
	(( 'Insert' , 'p_pPin' , ), 1610874880, (1610874880, (), [ (9, 1, None, "IID('{1B2620CF-90B0-4E6B-9CDF-A1799A578FDC}')") , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Remove' , 'p_vIndex' , ), 1610874881, (1610874881, (), [ (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IPowerNets_vtables_dispatch_ = 1
IPowerNets_vtables_ = [
	(( 'Item' , 'p_vIndex' , 'p_ppNet' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{48420240-E6BB-423E-9FD3-F3E4687E1452}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IPowerNetsMutable_vtables_dispatch_ = 1
IPowerNetsMutable_vtables_ = [
]

IRuleLayer_vtables_dispatch_ = 1
IRuleLayer_vtables_ = [
]

IRuleLayers_vtables_dispatch_ = 1
IRuleLayers_vtables_ = [
	(( 'Item' , 'p_vIndex' , 'p_ppRuleLayer' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{F25192FE-8196-46B9-BF8A-CBA1AFA316A3}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IScheme_vtables_dispatch_ = 1
IScheme_vtables_ = [
	(( 'NetClasses' , 'p_nNetClassMask' , 'p_ppNetClasses' , ), 1610874880, (1610874880, (), [ (3, 49, '2', None) , 
			 (16393, 10, None, "IID('{FA885B75-B122-4B9E-BAA2-87C657CB5659}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'NetClasses' , 'p_nNetClassMask' , 'p_ppNetClasses' , ), 1610874880, (1610874880, (), [ (3, 49, '2', None) , 
			 (16393, 10, None, "IID('{FA885B75-B122-4B9E-BAA2-87C657CB5659}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'ClearanceRules' , 'p_ppClearanceRules' , ), 1610874881, (1610874881, (), [ (16393, 10, None, "IID('{8F934507-D505-4A25-A96A-1654C17B5C81}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'ClassClearances' , 'p_ppClassClearances' , ), 1610874882, (1610874882, (), [ (16393, 10, None, "IID('{96FD6C42-8C02-4A00-A1B6-C47FB0D47913}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Rename' , 'p_strName' , ), 1610874883, (1610874883, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
]

ISchemeClearanceRule_vtables_dispatch_ = 1
ISchemeClearanceRule_vtables_ = [
	(( 'Layers' , 'p_ppLayers' , ), 1610874880, (1610874880, (), [ (16393, 10, None, "IID('{6710F183-E176-48F4-B3CA-DBD22E0CF5FF}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
]

ISchemeClearanceRules_vtables_dispatch_ = 1
ISchemeClearanceRules_vtables_ = [
	(( 'Item' , 'p_vIndex' , 'p_ppSchemeClearanceRule' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{DD8B4252-8E56-4A1A-B5CC-2A3A1284B1C5}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

ISchemeNetClass_vtables_dispatch_ = 1
ISchemeNetClass_vtables_ = [
	(( 'FullName' , 'p_pFullName' , ), 1610874880, (1610874880, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'NetClasses' , 'p_nNetClassMask' , 'p_ppNetClasses' , ), 1610874881, (1610874881, (), [ (3, 49, '2', None) , 
			 (16393, 10, None, "IID('{FA885B75-B122-4B9E-BAA2-87C657CB5659}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'NetClasses' , 'p_nNetClassMask' , 'p_ppNetClasses' , ), 1610874881, (1610874881, (), [ (3, 49, '2', None) , 
			 (16393, 10, None, "IID('{FA885B75-B122-4B9E-BAA2-87C657CB5659}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Layers' , 'p_ppLayers' , ), 1610874882, (1610874882, (), [ (16393, 10, None, "IID('{6710F183-E176-48F4-B3CA-DBD22E0CF5FF}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
]

ISchemeNetClasses_vtables_dispatch_ = 1
ISchemeNetClasses_vtables_ = [
	(( 'Item' , 'p_vIndex' , 'p_ppSchemeNetClass' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{06818093-77D0-48D0-847E-77DFFAB80667}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

ISchemes_vtables_dispatch_ = 1
ISchemes_vtables_ = [
	(( 'Item' , 'p_vIndex' , 'p_ppScheme' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{6F39247C-17C2-4C9F-B14C-469620C80FC4}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

ISchemesMutable_vtables_dispatch_ = 1
ISchemesMutable_vtables_ = [
	(( 'Add' , 'p_strName' , 'p_ppScheme' , ), 1610874880, (1610874880, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{6F39247C-17C2-4C9F-B14C-469620C80FC4}')") , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Delete' , 'p_vIndex' , ), 1610874881, (1610874881, (), [ (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

ISettings_vtables_dispatch_ = 1
ISettings_vtables_ = [
	(( 'Units' , 'p_ppUnits' , ), 1610743808, (1610743808, (), [ (16393, 10, None, "IID('{19C74DFD-6D72-4514-BAEB-D6FF7C4A1182}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Notation' , 'p_ppNotation' , ), 1610743809, (1610743809, (), [ (16393, 10, None, "IID('{177B82E6-3AFF-4E52-8141-7911C63B1879}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

IStackup_vtables_dispatch_ = 1
IStackup_vtables_ = [
	(( 'Layers' , 'p_ppLayers' , ), 1610874880, (1610874880, (), [ (16393, 10, None, "IID('{39981775-2776-4221-AB3C-1C27040DB64E}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
]

ITopology_vtables_dispatch_ = 1
ITopology_vtables_ = [
	(( 'TopologyType' , 'p_pTopologyType' , ), 1610874880, (1610874880, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'TopologyType' , 'p_pTopologyType' , ), 1610874880, (1610874880, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'IsOrdered' , 'p_pIsOrdered' , ), 1610874882, (1610874882, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Pins' , 'p_ppPins' , ), 1610874883, (1610874883, (), [ (16393, 10, None, "IID('{3F1B4618-0423-42B9-A741-72E65CE0E573}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'FromTos' , 'p_ppFromTos' , ), 1610874884, (1610874884, (), [ (16393, 10, None, "IID('{EE1AE409-4E07-44DC-8E8A-13B34E7FF81E}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'PinPairs' , 'p_ppPinPairs' , ), 1610874885, (1610874885, (), [ (16393, 10, None, "IID('{0D52DE96-799A-4660-ACFE-109F34DEE67B}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'PinSets' , 'p_ppPinSets' , ), 1610874886, (1610874886, (), [ (16393, 10, None, "IID('{27E83E75-0024-45DF-92D3-516B20F446C8}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Begin' , 'p_eTopologyType' , ), 1610874887, (1610874887, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Commit' , ), 1610874888, (1610874888, (), [ ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Rollback' , ), 1610874889, (1610874889, (), [ ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
]

IUnits_vtables_dispatch_ = 1
IUnits_vtables_ = [
	(( 'Capacitance' , 'p_pUnit' , ), 1610743808, (1610743808, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Capacitance' , 'p_pUnit' , ), 1610743808, (1610743808, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Current' , 'p_pUnit' , ), 1610743810, (1610743810, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Current' , 'p_pUnit' , ), 1610743810, (1610743810, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'CurrentDensity' , 'p_pUnit' , ), 1610743812, (1610743812, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'CurrentDensity' , 'p_pUnit' , ), 1610743812, (1610743812, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Voltage' , 'p_pUnit' , ), 1610743814, (1610743814, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Voltage' , 'p_pUnit' , ), 1610743814, (1610743814, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Inductance' , 'p_pUnit' , ), 1610743816, (1610743816, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Inductance' , 'p_pUnit' , ), 1610743816, (1610743816, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Linear' , 'p_pUnit' , ), 1610743818, (1610743818, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Linear' , 'p_pUnit' , ), 1610743818, (1610743818, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Power' , 'p_pUnit' , ), 1610743820, (1610743820, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Power' , 'p_pUnit' , ), 1610743820, (1610743820, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Resistance' , 'p_pUnit' , ), 1610743822, (1610743822, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Resistance' , 'p_pUnit' , ), 1610743822, (1610743822, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Temperature' , 'p_pUnit' , ), 1610743824, (1610743824, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Temperature' , 'p_pUnit' , ), 1610743824, (1610743824, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Theta' , 'p_pUnit' , ), 1610743826, (1610743826, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Theta' , 'p_pUnit' , ), 1610743826, (1610743826, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Time' , 'p_pUnit' , ), 1610743828, (1610743828, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Time' , 'p_pUnit' , ), 1610743828, (1610743828, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
]

IVariable_vtables_dispatch_ = 1
IVariable_vtables_ = [
	(( 'Rename' , 'p_strName' , ), 1610874880, (1610874880, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
]

IVariables_vtables_dispatch_ = 1
IVariables_vtables_ = [
	(( 'Item' , 'p_vIndex' , 'p_ppVariable' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{FB9D7374-6228-4B92-8403-03F3927706DE}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IVariablesMutable_vtables_dispatch_ = 1
IVariablesMutable_vtables_ = [
	(( 'Add' , 'p_strName' , 'p_ppVariable' , ), 1610874880, (1610874880, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{FB9D7374-6228-4B92-8403-03F3927706DE}')") , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Delete' , 'p_vIndex' , ), 1610874881, (1610874881, (), [ (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

RecordMap = {
}

CLSIDToClassMap = {
	'{3CD8028B-F3A2-4077-8F4F-83A89F4DD990}' : IDesignParams,
	'{8B0AE548-6CF5-1014-9B55-8BB0EECCF0AC}' : IConstraintsAuto,
	'{416A557D-9764-45C2-B656-BC53A72B6DDC}' : IDesign,
	'{17F8541C-BB01-40FC-AAFD-179AA166F42D}' : INetsMutable,
	'{EAF633E9-E21E-47FF-A361-60A4B480301F}' : INets,
	'{32B4374A-B64C-4E76-AEDB-5C944EF0D68A}' : ICollection,
	'{48420240-E6BB-423E-9FD3-F3E4687E1452}' : INet,
	'{7A5D1A08-B723-4929-BB46-A801DC642EB6}' : IObject,
	'{5147D582-BD1E-4F71-82E9-D7ECD5956AE6}' : IBase,
	'{1DDEC891-7D43-4EE9-9BD4-63772C577150}' : IConstraintsMutable,
	'{75C541D3-DD34-4A0C-9BAA-91155454CAD5}' : IConstraints,
	'{7C5585B1-767E-47E1-8BC9-F4564CA62236}' : IConstraint,
	'{23FAC1D8-2578-42BC-9F65-F04930FB6489}' : ICommentsMutable,
	'{32285CE8-91FA-40D4-844F-9D468F111061}' : IComments,
	'{8A5D0FF3-3D6C-4AD0-9F2C-150132A98B73}' : IComment,
	'{44747797-9642-483B-AB9C-6AE0A1899549}' : IObjects,
	'{E827A25D-2BEB-4013-9E2B-035133E06025}' : ITopology,
	'{3F1B4618-0423-42B9-A741-72E65CE0E573}' : IPins,
	'{1B2620CF-90B0-4E6B-9CDF-A1799A578FDC}' : IPin,
	'{9C2F6146-F58D-43EC-B1B4-F0FF99B33E31}' : IFromTos,
	'{0DEB5A91-FF99-4B23-BAD2-4B5C2C84D5BF}' : IFromTo,
	'{AE314BDB-B6CC-4DD0-B514-1A525DA682D6}' : IPinPairs,
	'{DAE2F804-60E5-4B5F-96F0-FB5585334EAB}' : IPinPair,
	'{1F460B56-507F-4CA6-B8D7-676CBB2427BD}' : IMatchGroups,
	'{141C68A8-5519-4BD9-887B-C02B3E31E9F0}' : IMatchGroup,
	'{0D52DE96-799A-4660-ACFE-109F34DEE67B}' : IPinPairsMutable,
	'{A59586BA-4C99-4643-B6F8-E42BBF2E00D2}' : IFormula,
	'{B80F7CDC-6D14-471E-9983-979FF0059B5A}' : IPinSets,
	'{5B8C932F-F283-4D9C-AD70-4B4213109BC3}' : IPinSet,
	'{B034C5D7-24E1-4F6A-836A-7906257DABAA}' : IPinsMutable,
	'{A6EC1810-AC7F-4B10-AA00-BBC2FCB7C929}' : IPartPin,
	'{44495392-B0D3-496F-8925-A5F0710C3A67}' : IPartPinPairs,
	'{FE3B36FE-C912-41F3-88EA-542F43253414}' : IPartPinPair,
	'{1C51DCE2-A09B-4680-BF6F-9EDAF0C822B8}' : IPartPins,
	'{EE1AE409-4E07-44DC-8E8A-13B34E7FF81E}' : IFromTosMutable,
	'{27E83E75-0024-45DF-92D3-516B20F446C8}' : IPinSetsMutable,
	'{CB59FE57-0379-43C2-86FF-E6E0D31CBAB9}' : IConstraintClass,
	'{AC287CEE-0F24-4AA5-AB3F-7FCAB43B13A6}' : IClass,
	'{E6F44CAC-B61D-4437-971F-60F01875D6BB}' : IDisplayPattern,
	'{DAA15140-C478-41AE-90D4-8782BA3A8707}' : INetClassesMutable,
	'{53A3ED0F-BBD8-41BF-9460-F17C61BCD389}' : INetClasses,
	'{791A98C5-512E-45E0-8F4F-715A45F5707A}' : INetClass,
	'{7D9A71CB-B02F-4A1B-9995-2ADF58C69494}' : IConstraintClasses,
	'{96FD6C42-8C02-4A00-A1B6-C47FB0D47913}' : IClassClearances,
	'{77040253-C4BE-4037-B759-739678531FE8}' : IClassClearance,
	'{6F39247C-17C2-4C9F-B14C-469620C80FC4}' : IScheme,
	'{FA885B75-B122-4B9E-BAA2-87C657CB5659}' : ISchemeNetClasses,
	'{06818093-77D0-48D0-847E-77DFFAB80667}' : ISchemeNetClass,
	'{6710F183-E176-48F4-B3CA-DBD22E0CF5FF}' : IRuleLayers,
	'{F25192FE-8196-46B9-BF8A-CBA1AFA316A3}' : IRuleLayer,
	'{8F934507-D505-4A25-A96A-1654C17B5C81}' : ISchemeClearanceRules,
	'{DD8B4252-8E56-4A1A-B5CC-2A3A1284B1C5}' : ISchemeClearanceRule,
	'{A0F38DDB-184D-4D4E-9E99-FFF4E73A4235}' : IClearanceRule,
	'{E4076B8B-3F93-407C-8E18-9DD473F3C4B6}' : IConstraintClassesMutable,
	'{ED063FFC-209C-48D7-8D59-6677873C9A7A}' : INoiseRules,
	'{D06D3CAD-4D4E-40B8-9A9A-16D446917F77}' : INoiseRule,
	'{A11D8E06-CE97-402B-AFD5-D75BACE22E1A}' : IParallelismRule,
	'{DEB98723-9BE8-482E-A482-E511BA818C2C}' : IParallelismRuleSegmentsMutable,
	'{201C826A-8C6C-4172-931F-92F9208F3717}' : IParallelismRuleSegments,
	'{C391FA67-1209-4DD6-BD23-9D3DD7332651}' : IParallelismRuleSegment,
	'{6F698C72-5BBF-4DEE-A09C-065A7AB68829}' : IElectricalNetsMutable,
	'{26EBA780-1293-4DF0-87B3-2F4113E178CB}' : IElectricalNets,
	'{7DB3D012-77AB-47DF-9C24-9A297A370AD0}' : IElectricalNet,
	'{B224A038-B04A-47E1-8F9F-C7938C61FD68}' : IPowerNetsMutable,
	'{88AFDE06-B464-4045-8FC0-321DAAB9EDDE}' : IPowerNets,
	'{7E649A6C-5038-4FD1-94D9-44A56CAC894E}' : IDifferentialPairsMutable,
	'{3F1097CF-2AFC-4D0B-8477-FEA016F94987}' : IDifferentialPairs,
	'{90FF1694-9C25-4F12-A08B-999F24686B57}' : IDifferentialPair,
	'{088425F1-88A0-4675-B9B9-D6FBC0454CF3}' : IClearanceRulesMutable,
	'{349CEE9A-3FFB-4FA8-AB31-F98DC12E4E74}' : IClearanceRules,
	'{F36348AB-8180-41C3-951F-0B079E3FF03F}' : IMatchGroupsMutable,
	'{AF4369BD-BEF9-48A7-849A-F39065467C85}' : IFormulasMutable,
	'{7232F46D-2CFB-423B-927D-E8B1AA3B959A}' : IFormulas,
	'{D07554EB-FCFF-48EC-AD04-C79988D20C9D}' : INoiseRulesMutable,
	'{E37D92BA-6E24-45E0-859C-43A40855C3AD}' : IParallelismRulesMutable,
	'{595C88AE-5AAA-431C-97BD-5B3C181097EF}' : IParallelismRules,
	'{E010B178-C036-4BDE-815F-9B48CE213D1E}' : IComponentsMutable,
	'{AC3ABD04-B1DD-47C7-8A94-404DFD764E56}' : IComponents,
	'{60516EC5-86D9-4E16-86E7-9B66302D3A83}' : IComponent,
	'{965F3ED3-C357-4CD4-8778-9B61B12D5D24}' : IPartsMutable,
	'{CD4E27CD-B11C-4EDD-B1BE-6D1996D3A4F1}' : IParts,
	'{2D3374B6-ED6A-4024-AC29-ACF03A09B7C5}' : IPart,
	'{8596DD5E-2C99-4DED-9A1F-D9067D3D34DB}' : IPartPinsMutable,
	'{7DA3F078-E3B2-4436-A267-6FC09F25AB19}' : IPartPinPairsMutable,
	'{3C22162A-1920-4AF1-B2BA-805CC3A2500C}' : IConstantsMutable,
	'{F5D6BDC5-5DB8-4F47-AC16-CABDF8BE0437}' : IConstants,
	'{E43EED65-B104-4518-A7C0-21C3FA01B4F5}' : IConstant,
	'{9B803C91-3B87-4F74-810E-C038E63376B7}' : IVariablesMutable,
	'{CB2822E1-C294-4DD7-8DAC-A30B11174649}' : IVariables,
	'{FB9D7374-6228-4B92-8403-03F3927706DE}' : IVariable,
	'{FBFDBD21-1B6F-4263-A285-6FB6E9C7747F}' : IStackup,
	'{39981775-2776-4221-AB3C-1C27040DB64E}' : ILayersMutable,
	'{A8C2D4D7-EF76-436C-BDC8-0813B8248EBF}' : ILayers,
	'{052E8B90-0E4C-44C1-8F39-89E344392B5C}' : ILayer,
	'{F1F96334-F630-42BA-A3F4-2D314D51D535}' : IPhysicalRules,
	'{C868C166-9607-4506-AEF9-5AE4FB428F95}' : ISchemesMutable,
	'{08A1E04B-6987-41C4-90E5-CA467E65937B}' : ISchemes,
	'{FA648CF5-E9A3-4841-AD76-BD4BCD55DF45}' : IClassClearancesMutable,
	'{BC62A287-210A-4466-A894-5ACB1F4E0E25}' : IGeneralClearancesMutable,
	'{A96A5A2C-6E39-4FB7-A86C-C6992501261A}' : IGeneralClearances,
	'{D7ABE808-2624-4912-B413-96F9E0B5BA5B}' : IGeneralClearance,
	'{D2CFD11E-A067-4F0F-BE2F-17A9F507040E}' : IPackageClearancesMutable,
	'{B5A4D7C8-1D7D-42CB-8E1D-508B0BD67DCC}' : IPackageClearances,
	'{240DA68C-6822-4B65-A4B3-8E7AB10B66AE}' : IPackageClearance,
	'{9253A04D-448B-459A-AF00-BC956F499198}' : IPackageType,
	'{209DB434-B7A4-4CF7-A1DC-87CFD2B21543}' : IDisplayPatternsMutable,
	'{D47DF953-026D-440D-819D-2DE548AD17C4}' : IDisplayPatterns,
	'{EA65AC00-04E5-42F6-AC61-7FA81534926F}' : IPackageTypesMutable,
	'{4536460C-7AFD-40EE-ADED-BBE2D068ECC8}' : IPackageTypes,
	'{8D9E96B8-678C-4EC9-93EE-F7E4CEC025FB}' : ISettings,
	'{19C74DFD-6D72-4514-BAEB-D6FF7C4A1182}' : IUnits,
	'{177B82E6-3AFF-4E52-8141-7911C63B1879}' : INotation,
	'{D9FEE0D7-B9FE-41C9-9FCF-6597EDC8E2AF}' : IDRC,
	'{E835C9C8-FC4E-417D-BD00-A948B4F66D20}' : DesignParams,
	'{8B0AE687-6CF5-1014-9B55-8BB0EECCF0AC}' : ConstraintsAuto,
	'{BD801DC8-79E4-45DE-ADB7-45E7918DF499}' : Design,
	'{5B3D4D1E-F433-41E5-A6CF-1166E1812E45}' : Settings,
	'{58F0FCDE-99F8-49B8-B105-EB6B93C25616}' : Units,
	'{866B8DDA-424F-4C1D-ACC7-74D2FD26A5E6}' : Notation,
	'{E2E4868A-9FD4-478F-A504-0AB8B2DEB117}' : Collection,
	'{26F1B6BC-D3D7-4A17-9387-53063A8F3E19}' : Objects,
	'{25937434-EBF2-42A3-B4C8-2EC32F4DEE6E}' : Constraints,
	'{211695E1-560F-41E3-8125-5C41B4A1131B}' : ConstraintsMutable,
	'{F7269414-6A1B-4F30-9FA0-619B80717D2A}' : Comments,
	'{65183681-9F46-4373-B909-A345126B459B}' : CommentsMutable,
	'{3BC701EA-8962-401F-8213-9782C2A5471F}' : ConstraintClasses,
	'{06CEF5AA-5BDB-4B33-8BBA-7E6A0E108A1B}' : ConstraintClassesMutable,
	'{E6945AC7-71DE-4FBD-B914-513A60E82520}' : NetClasses,
	'{38ABD376-70EE-45BF-B017-90DC59A9EB2F}' : NetClassesMutable,
	'{CC09F366-B8E9-4E10-84DC-8C92197B0207}' : ClearanceRules,
	'{15582A4E-85ED-45F4-BA66-696181360E83}' : ClearanceRulesMutable,
	'{6AAAB236-9207-4D72-91AB-37FAD56B1505}' : Nets,
	'{C03A89DF-4DDB-4892-BF2A-3C92018D9F7E}' : NetsMutable,
	'{D29538F3-CD23-4FB3-ACDB-6489A2B9F6E9}' : ElectricalNets,
	'{511DF122-52DC-494E-B932-BC4DB9932B41}' : ElectricalNetsMutable,
	'{0798D9AB-9C3F-4E6D-8C31-382798093C5B}' : PowerNets,
	'{AFF3111C-9B72-46E6-9E5F-0A241014C7C1}' : PowerNetsMutable,
	'{0E5A6F70-EA58-4E16-B16D-8B24785E5617}' : DifferentialPairs,
	'{B42E232E-C7ED-444C-81BC-4E88A3540DF3}' : DifferentialPairsMutable,
	'{BEBB09AC-7396-4C74-9423-9BFA9D766B1F}' : Pins,
	'{F6D6CDD0-C76D-4243-A552-2A37424621A0}' : PinsMutable,
	'{FB7CB482-1529-451F-911B-7BC33EC256BF}' : PinPairs,
	'{31380624-17C9-4E40-8A0D-826E88AC4589}' : PinPairsMutable,
	'{9670C07E-EF9C-4FF8-9DE7-EDEA3B5868A3}' : PinSets,
	'{EDCACA3C-AF91-401F-970F-CF31FC29E3AE}' : PinSetsMutable,
	'{661A1886-47C6-4BE7-B902-7D741CC216C5}' : FromTos,
	'{3925DBCB-CE2E-4FA2-8BD8-D60CC27BF192}' : FromTosMutable,
	'{95AF9055-4360-4AD1-837E-8A4AEF81AF34}' : MatchGroups,
	'{E4717647-28C9-420B-8624-6A0298314D93}' : MatchGroupsMutable,
	'{FC12916D-BCA2-44C7-8BA2-0469F29C2F99}' : Formulas,
	'{02C5D3D1-CD4B-49B9-A5A1-6D517184C8A3}' : FormulasMutable,
	'{57320C9B-E888-40E1-B937-7090B95682E3}' : PartPins,
	'{6BD38466-57D0-4836-A566-60674280EBC8}' : PartPinsMutable,
	'{8FA9F4DB-8EE1-45BB-9B2C-FBD758CCD1A0}' : PartPinPairs,
	'{F86FDE27-D779-458D-A51D-56FC1186F818}' : PartPinPairsMutable,
	'{B7DC1FFB-DDF7-4710-96DF-9CE53C3399A1}' : Components,
	'{153D5723-3036-4796-9184-BA5AA4999BF7}' : ComponentsMutable,
	'{902446D5-4B16-4320-91AE-682169A4B7A3}' : Parts,
	'{1C06D4C9-421F-47C1-B4F0-86179BDE6A44}' : PartsMutable,
	'{52504AB6-DF45-424B-A06A-B4F29C000667}' : Constants,
	'{2FC31295-E0FE-453B-AE2D-1BD5726CE291}' : ConstantsMutable,
	'{D99D85C4-7960-4462-B02F-193CCD7DA13B}' : Variables,
	'{43B955FB-3E8A-4B7F-92FC-821418613BF8}' : VariablesMutable,
	'{96977B18-D144-4DB5-AF5F-266B353B61E6}' : Layers,
	'{CD47D215-A820-47E2-AE07-453CC2ED6D7C}' : LayersMutable,
	'{47D1E5C7-D510-4D3D-9EE3-8A19493FAC71}' : Schemes,
	'{1855D335-FBB0-475E-B448-9F6C0D035807}' : SchemesMutable,
	'{42D9D034-924A-4439-9747-D6441A45571A}' : SchemeNetClasses,
	'{9CA49EA5-F767-4CD7-827C-9566CC755DDB}' : SchemeClearanceRules,
	'{756E21CB-A264-4D2A-B086-0B12F97D0FB5}' : RuleLayers,
	'{D902C696-50D9-4383-BC8C-595FDA5434F1}' : PhysicalRules,
	'{5FF6AAE0-F6A3-40A0-8B3E-36E1C22D7808}' : ClassClearances,
	'{3D99E63D-958F-4443-9BA7-4C07BBB99068}' : ClassClearancesMutable,
	'{078B323D-5BB7-4C07-92CF-9F3C48ED98B5}' : DisplayPatterns,
	'{4415B5A1-315A-4D3E-91C9-898489133B66}' : DisplayPatternsMutable,
	'{FDD01A44-69ED-4E7F-88C7-7947E8C7BD69}' : Base,
	'{B29B6B0B-4390-4DE0-AB0E-652FBD8D5845}' : Object,
	'{D3A2A3F8-D4FC-453F-9A69-CF8425497168}' : Constraint,
	'{C5CB9071-36B8-4E69-95FC-41839093973B}' : Comment,
	'{E111A365-1082-4B6E-A64B-FAE25BFEFB1B}' : Net,
	'{34AD93FA-589D-4CA9-B092-E60A1B16F627}' : ElectricalNet,
	'{04DE4486-51F4-4FB5-A1D2-DCB6CD97EF6C}' : DifferentialPair,
	'{31529548-2AD2-4506-854D-E81C61784146}' : Topology,
	'{BFB658F1-2CC5-4D15-B3F8-077FC1497BC4}' : Pin,
	'{F2284F80-6E4A-4945-BB5F-69FED15C9C5A}' : PinPair,
	'{58AF7426-636E-4771-8BA8-06179F6D3A0B}' : PinSet,
	'{FDBE490D-01ED-4EF4-96DF-C4D1034AC95F}' : FromTo,
	'{BE604238-860C-429A-86DD-282A1D52ADFF}' : MatchGroup,
	'{3FA6B387-5FB9-4380-B4FF-BD1D0CC40F08}' : Class,
	'{34DA88B0-930D-469A-8CE0-0738CBCD4870}' : NetClass,
	'{032414B7-8F46-402E-B8B1-D834CF6FB083}' : ConstraintClass,
	'{02D9EB90-8303-47C0-8C9B-27D02DE97D52}' : ClearanceRule,
	'{6E8C0221-D322-40BA-80E0-0271F8DFD70C}' : ClassClearance,
	'{50FBC794-9C15-4AF8-82C3-DE231368AAFE}' : Formula,
	'{A73969C5-E0DA-45BA-BAB3-DDFCF3BE6FE8}' : ParallelismRule,
	'{2ABDB9DD-E0F6-4344-B4C8-EF2E68B91DDC}' : ParallelismRules,
	'{DD6F53A1-D9F2-4E92-AD84-81C15D262F16}' : ParallelismRulesMutable,
	'{A5CBB258-CAC7-4150-A5FE-61B8027641DF}' : ParallelismRuleSegment,
	'{7689BAC5-FCD4-4523-B7F7-693B529238D9}' : ParallelismRuleSegments,
	'{6E18E1F9-1BCF-4EB3-B700-6A4D68349F92}' : ParallelismRuleSegmentsMutable,
	'{62CDF1A0-E6E8-4C62-8C4E-05015FA9FD54}' : NoiseRule,
	'{B954C85D-6103-4A81-A73D-4334ACE4FB4C}' : NoiseRules,
	'{1C7ACB33-918C-4071-BB73-471C94FDFA75}' : NoiseRulesMutable,
	'{2FAE361D-F475-44EC-B87C-F58184D8DFA1}' : PartPin,
	'{2C8C8556-C2B6-449B-88A2-9030268296AC}' : PartPinPair,
	'{E8CEF3AC-4D63-4E45-B553-CCC01DFC4202}' : Component,
	'{17DCD0D5-D0AD-41C1-924E-F6237BF78120}' : Part,
	'{104F0D8D-82A5-44BA-A563-92EBF5BAEEB7}' : Constant,
	'{401B8E73-606E-42F1-A576-EEFB1EADDD08}' : Variable,
	'{A1BB2710-763F-4DC1-AE6D-0F079CAC9AFA}' : Layer,
	'{A9F41CFA-8BA3-4D5A-A002-D4E2C9F54CD2}' : Stackup,
	'{0A5EE769-4E45-41A0-98EE-9BFE90EDB47D}' : Scheme,
	'{4262249B-F52C-4618-9643-BD9C1D625E87}' : SchemeNetClass,
	'{150A1D3E-3113-420A-9322-80966E1D7B42}' : SchemeClearanceRule,
	'{A4733E8D-B970-4077-AC69-E6578DC3FB93}' : RuleLayer,
	'{644E0684-E131-45ED-A4B3-A76EC1D5B33E}' : DRC,
	'{8914D1F0-18EC-4E84-8CDA-F1598F99A228}' : DisplayPattern,
	'{E82C72F8-E994-46BB-8E9A-1A2815C34A4F}' : GeneralClearances,
	'{7B50268E-5CD1-480D-B35F-E20A8430DD24}' : GeneralClearancesMutable,
	'{AFF28CA8-1527-4C24-BD65-632849524714}' : GeneralClearance,
	'{16AC6FAA-65B2-4B25-A3A3-EA0203A483FF}' : PackageTypes,
	'{5515A13F-6AFA-45BA-BA6F-C291928DE332}' : PackageTypesMutable,
	'{CB10CB0C-DAB8-41C9-AAAB-500CC8C5A398}' : PackageType,
	'{8E8E5C86-7002-4197-9495-56C1B7BC5603}' : PackageClearances,
	'{258F61A2-1815-4AF5-BC54-FBA8FA6ECF60}' : PackageClearancesMutable,
	'{8C1CE62E-16DF-4CF0-8939-4DC718FED03A}' : PackageClearance,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
	'{3CD8028B-F3A2-4077-8F4F-83A89F4DD990}' : 'IDesignParams',
	'{8B0AE548-6CF5-1014-9B55-8BB0EECCF0AC}' : 'IConstraintsAuto',
	'{416A557D-9764-45C2-B656-BC53A72B6DDC}' : 'IDesign',
	'{17F8541C-BB01-40FC-AAFD-179AA166F42D}' : 'INetsMutable',
	'{EAF633E9-E21E-47FF-A361-60A4B480301F}' : 'INets',
	'{32B4374A-B64C-4E76-AEDB-5C944EF0D68A}' : 'ICollection',
	'{48420240-E6BB-423E-9FD3-F3E4687E1452}' : 'INet',
	'{7A5D1A08-B723-4929-BB46-A801DC642EB6}' : 'IObject',
	'{5147D582-BD1E-4F71-82E9-D7ECD5956AE6}' : 'IBase',
	'{1DDEC891-7D43-4EE9-9BD4-63772C577150}' : 'IConstraintsMutable',
	'{75C541D3-DD34-4A0C-9BAA-91155454CAD5}' : 'IConstraints',
	'{7C5585B1-767E-47E1-8BC9-F4564CA62236}' : 'IConstraint',
	'{23FAC1D8-2578-42BC-9F65-F04930FB6489}' : 'ICommentsMutable',
	'{32285CE8-91FA-40D4-844F-9D468F111061}' : 'IComments',
	'{8A5D0FF3-3D6C-4AD0-9F2C-150132A98B73}' : 'IComment',
	'{44747797-9642-483B-AB9C-6AE0A1899549}' : 'IObjects',
	'{E827A25D-2BEB-4013-9E2B-035133E06025}' : 'ITopology',
	'{3F1B4618-0423-42B9-A741-72E65CE0E573}' : 'IPins',
	'{1B2620CF-90B0-4E6B-9CDF-A1799A578FDC}' : 'IPin',
	'{9C2F6146-F58D-43EC-B1B4-F0FF99B33E31}' : 'IFromTos',
	'{0DEB5A91-FF99-4B23-BAD2-4B5C2C84D5BF}' : 'IFromTo',
	'{AE314BDB-B6CC-4DD0-B514-1A525DA682D6}' : 'IPinPairs',
	'{DAE2F804-60E5-4B5F-96F0-FB5585334EAB}' : 'IPinPair',
	'{1F460B56-507F-4CA6-B8D7-676CBB2427BD}' : 'IMatchGroups',
	'{141C68A8-5519-4BD9-887B-C02B3E31E9F0}' : 'IMatchGroup',
	'{0D52DE96-799A-4660-ACFE-109F34DEE67B}' : 'IPinPairsMutable',
	'{A59586BA-4C99-4643-B6F8-E42BBF2E00D2}' : 'IFormula',
	'{B80F7CDC-6D14-471E-9983-979FF0059B5A}' : 'IPinSets',
	'{5B8C932F-F283-4D9C-AD70-4B4213109BC3}' : 'IPinSet',
	'{B034C5D7-24E1-4F6A-836A-7906257DABAA}' : 'IPinsMutable',
	'{A6EC1810-AC7F-4B10-AA00-BBC2FCB7C929}' : 'IPartPin',
	'{44495392-B0D3-496F-8925-A5F0710C3A67}' : 'IPartPinPairs',
	'{FE3B36FE-C912-41F3-88EA-542F43253414}' : 'IPartPinPair',
	'{1C51DCE2-A09B-4680-BF6F-9EDAF0C822B8}' : 'IPartPins',
	'{EE1AE409-4E07-44DC-8E8A-13B34E7FF81E}' : 'IFromTosMutable',
	'{27E83E75-0024-45DF-92D3-516B20F446C8}' : 'IPinSetsMutable',
	'{CB59FE57-0379-43C2-86FF-E6E0D31CBAB9}' : 'IConstraintClass',
	'{AC287CEE-0F24-4AA5-AB3F-7FCAB43B13A6}' : 'IClass',
	'{E6F44CAC-B61D-4437-971F-60F01875D6BB}' : 'IDisplayPattern',
	'{DAA15140-C478-41AE-90D4-8782BA3A8707}' : 'INetClassesMutable',
	'{53A3ED0F-BBD8-41BF-9460-F17C61BCD389}' : 'INetClasses',
	'{791A98C5-512E-45E0-8F4F-715A45F5707A}' : 'INetClass',
	'{7D9A71CB-B02F-4A1B-9995-2ADF58C69494}' : 'IConstraintClasses',
	'{96FD6C42-8C02-4A00-A1B6-C47FB0D47913}' : 'IClassClearances',
	'{77040253-C4BE-4037-B759-739678531FE8}' : 'IClassClearance',
	'{6F39247C-17C2-4C9F-B14C-469620C80FC4}' : 'IScheme',
	'{FA885B75-B122-4B9E-BAA2-87C657CB5659}' : 'ISchemeNetClasses',
	'{06818093-77D0-48D0-847E-77DFFAB80667}' : 'ISchemeNetClass',
	'{6710F183-E176-48F4-B3CA-DBD22E0CF5FF}' : 'IRuleLayers',
	'{F25192FE-8196-46B9-BF8A-CBA1AFA316A3}' : 'IRuleLayer',
	'{8F934507-D505-4A25-A96A-1654C17B5C81}' : 'ISchemeClearanceRules',
	'{DD8B4252-8E56-4A1A-B5CC-2A3A1284B1C5}' : 'ISchemeClearanceRule',
	'{A0F38DDB-184D-4D4E-9E99-FFF4E73A4235}' : 'IClearanceRule',
	'{E4076B8B-3F93-407C-8E18-9DD473F3C4B6}' : 'IConstraintClassesMutable',
	'{ED063FFC-209C-48D7-8D59-6677873C9A7A}' : 'INoiseRules',
	'{D06D3CAD-4D4E-40B8-9A9A-16D446917F77}' : 'INoiseRule',
	'{A11D8E06-CE97-402B-AFD5-D75BACE22E1A}' : 'IParallelismRule',
	'{DEB98723-9BE8-482E-A482-E511BA818C2C}' : 'IParallelismRuleSegmentsMutable',
	'{201C826A-8C6C-4172-931F-92F9208F3717}' : 'IParallelismRuleSegments',
	'{C391FA67-1209-4DD6-BD23-9D3DD7332651}' : 'IParallelismRuleSegment',
	'{6F698C72-5BBF-4DEE-A09C-065A7AB68829}' : 'IElectricalNetsMutable',
	'{26EBA780-1293-4DF0-87B3-2F4113E178CB}' : 'IElectricalNets',
	'{7DB3D012-77AB-47DF-9C24-9A297A370AD0}' : 'IElectricalNet',
	'{B224A038-B04A-47E1-8F9F-C7938C61FD68}' : 'IPowerNetsMutable',
	'{88AFDE06-B464-4045-8FC0-321DAAB9EDDE}' : 'IPowerNets',
	'{7E649A6C-5038-4FD1-94D9-44A56CAC894E}' : 'IDifferentialPairsMutable',
	'{3F1097CF-2AFC-4D0B-8477-FEA016F94987}' : 'IDifferentialPairs',
	'{90FF1694-9C25-4F12-A08B-999F24686B57}' : 'IDifferentialPair',
	'{088425F1-88A0-4675-B9B9-D6FBC0454CF3}' : 'IClearanceRulesMutable',
	'{349CEE9A-3FFB-4FA8-AB31-F98DC12E4E74}' : 'IClearanceRules',
	'{F36348AB-8180-41C3-951F-0B079E3FF03F}' : 'IMatchGroupsMutable',
	'{AF4369BD-BEF9-48A7-849A-F39065467C85}' : 'IFormulasMutable',
	'{7232F46D-2CFB-423B-927D-E8B1AA3B959A}' : 'IFormulas',
	'{D07554EB-FCFF-48EC-AD04-C79988D20C9D}' : 'INoiseRulesMutable',
	'{E37D92BA-6E24-45E0-859C-43A40855C3AD}' : 'IParallelismRulesMutable',
	'{595C88AE-5AAA-431C-97BD-5B3C181097EF}' : 'IParallelismRules',
	'{E010B178-C036-4BDE-815F-9B48CE213D1E}' : 'IComponentsMutable',
	'{AC3ABD04-B1DD-47C7-8A94-404DFD764E56}' : 'IComponents',
	'{60516EC5-86D9-4E16-86E7-9B66302D3A83}' : 'IComponent',
	'{965F3ED3-C357-4CD4-8778-9B61B12D5D24}' : 'IPartsMutable',
	'{CD4E27CD-B11C-4EDD-B1BE-6D1996D3A4F1}' : 'IParts',
	'{2D3374B6-ED6A-4024-AC29-ACF03A09B7C5}' : 'IPart',
	'{8596DD5E-2C99-4DED-9A1F-D9067D3D34DB}' : 'IPartPinsMutable',
	'{7DA3F078-E3B2-4436-A267-6FC09F25AB19}' : 'IPartPinPairsMutable',
	'{3C22162A-1920-4AF1-B2BA-805CC3A2500C}' : 'IConstantsMutable',
	'{F5D6BDC5-5DB8-4F47-AC16-CABDF8BE0437}' : 'IConstants',
	'{E43EED65-B104-4518-A7C0-21C3FA01B4F5}' : 'IConstant',
	'{9B803C91-3B87-4F74-810E-C038E63376B7}' : 'IVariablesMutable',
	'{CB2822E1-C294-4DD7-8DAC-A30B11174649}' : 'IVariables',
	'{FB9D7374-6228-4B92-8403-03F3927706DE}' : 'IVariable',
	'{FBFDBD21-1B6F-4263-A285-6FB6E9C7747F}' : 'IStackup',
	'{39981775-2776-4221-AB3C-1C27040DB64E}' : 'ILayersMutable',
	'{A8C2D4D7-EF76-436C-BDC8-0813B8248EBF}' : 'ILayers',
	'{052E8B90-0E4C-44C1-8F39-89E344392B5C}' : 'ILayer',
	'{F1F96334-F630-42BA-A3F4-2D314D51D535}' : 'IPhysicalRules',
	'{C868C166-9607-4506-AEF9-5AE4FB428F95}' : 'ISchemesMutable',
	'{08A1E04B-6987-41C4-90E5-CA467E65937B}' : 'ISchemes',
	'{FA648CF5-E9A3-4841-AD76-BD4BCD55DF45}' : 'IClassClearancesMutable',
	'{BC62A287-210A-4466-A894-5ACB1F4E0E25}' : 'IGeneralClearancesMutable',
	'{A96A5A2C-6E39-4FB7-A86C-C6992501261A}' : 'IGeneralClearances',
	'{D7ABE808-2624-4912-B413-96F9E0B5BA5B}' : 'IGeneralClearance',
	'{D2CFD11E-A067-4F0F-BE2F-17A9F507040E}' : 'IPackageClearancesMutable',
	'{B5A4D7C8-1D7D-42CB-8E1D-508B0BD67DCC}' : 'IPackageClearances',
	'{240DA68C-6822-4B65-A4B3-8E7AB10B66AE}' : 'IPackageClearance',
	'{9253A04D-448B-459A-AF00-BC956F499198}' : 'IPackageType',
	'{209DB434-B7A4-4CF7-A1DC-87CFD2B21543}' : 'IDisplayPatternsMutable',
	'{D47DF953-026D-440D-819D-2DE548AD17C4}' : 'IDisplayPatterns',
	'{EA65AC00-04E5-42F6-AC61-7FA81534926F}' : 'IPackageTypesMutable',
	'{4536460C-7AFD-40EE-ADED-BBE2D068ECC8}' : 'IPackageTypes',
	'{8D9E96B8-678C-4EC9-93EE-F7E4CEC025FB}' : 'ISettings',
	'{19C74DFD-6D72-4514-BAEB-D6FF7C4A1182}' : 'IUnits',
	'{177B82E6-3AFF-4E52-8141-7911C63B1879}' : 'INotation',
	'{D9FEE0D7-B9FE-41C9-9FCF-6597EDC8E2AF}' : 'IDRC',
}


NamesToIIDMap = {
	'IDesignParams' : '{3CD8028B-F3A2-4077-8F4F-83A89F4DD990}',
	'IConstraintsAuto' : '{8B0AE548-6CF5-1014-9B55-8BB0EECCF0AC}',
	'IDesign' : '{416A557D-9764-45C2-B656-BC53A72B6DDC}',
	'INetsMutable' : '{17F8541C-BB01-40FC-AAFD-179AA166F42D}',
	'INets' : '{EAF633E9-E21E-47FF-A361-60A4B480301F}',
	'ICollection' : '{32B4374A-B64C-4E76-AEDB-5C944EF0D68A}',
	'INet' : '{48420240-E6BB-423E-9FD3-F3E4687E1452}',
	'IObject' : '{7A5D1A08-B723-4929-BB46-A801DC642EB6}',
	'IBase' : '{5147D582-BD1E-4F71-82E9-D7ECD5956AE6}',
	'IConstraintsMutable' : '{1DDEC891-7D43-4EE9-9BD4-63772C577150}',
	'IConstraints' : '{75C541D3-DD34-4A0C-9BAA-91155454CAD5}',
	'IConstraint' : '{7C5585B1-767E-47E1-8BC9-F4564CA62236}',
	'ICommentsMutable' : '{23FAC1D8-2578-42BC-9F65-F04930FB6489}',
	'IComments' : '{32285CE8-91FA-40D4-844F-9D468F111061}',
	'IComment' : '{8A5D0FF3-3D6C-4AD0-9F2C-150132A98B73}',
	'IObjects' : '{44747797-9642-483B-AB9C-6AE0A1899549}',
	'ITopology' : '{E827A25D-2BEB-4013-9E2B-035133E06025}',
	'IPins' : '{3F1B4618-0423-42B9-A741-72E65CE0E573}',
	'IPin' : '{1B2620CF-90B0-4E6B-9CDF-A1799A578FDC}',
	'IFromTos' : '{9C2F6146-F58D-43EC-B1B4-F0FF99B33E31}',
	'IFromTo' : '{0DEB5A91-FF99-4B23-BAD2-4B5C2C84D5BF}',
	'IPinPairs' : '{AE314BDB-B6CC-4DD0-B514-1A525DA682D6}',
	'IPinPair' : '{DAE2F804-60E5-4B5F-96F0-FB5585334EAB}',
	'IMatchGroups' : '{1F460B56-507F-4CA6-B8D7-676CBB2427BD}',
	'IMatchGroup' : '{141C68A8-5519-4BD9-887B-C02B3E31E9F0}',
	'IPinPairsMutable' : '{0D52DE96-799A-4660-ACFE-109F34DEE67B}',
	'IFormula' : '{A59586BA-4C99-4643-B6F8-E42BBF2E00D2}',
	'IPinSets' : '{B80F7CDC-6D14-471E-9983-979FF0059B5A}',
	'IPinSet' : '{5B8C932F-F283-4D9C-AD70-4B4213109BC3}',
	'IPinsMutable' : '{B034C5D7-24E1-4F6A-836A-7906257DABAA}',
	'IPartPin' : '{A6EC1810-AC7F-4B10-AA00-BBC2FCB7C929}',
	'IPartPinPairs' : '{44495392-B0D3-496F-8925-A5F0710C3A67}',
	'IPartPinPair' : '{FE3B36FE-C912-41F3-88EA-542F43253414}',
	'IPartPins' : '{1C51DCE2-A09B-4680-BF6F-9EDAF0C822B8}',
	'IFromTosMutable' : '{EE1AE409-4E07-44DC-8E8A-13B34E7FF81E}',
	'IPinSetsMutable' : '{27E83E75-0024-45DF-92D3-516B20F446C8}',
	'IConstraintClass' : '{CB59FE57-0379-43C2-86FF-E6E0D31CBAB9}',
	'IClass' : '{AC287CEE-0F24-4AA5-AB3F-7FCAB43B13A6}',
	'IDisplayPattern' : '{E6F44CAC-B61D-4437-971F-60F01875D6BB}',
	'INetClassesMutable' : '{DAA15140-C478-41AE-90D4-8782BA3A8707}',
	'INetClasses' : '{53A3ED0F-BBD8-41BF-9460-F17C61BCD389}',
	'INetClass' : '{791A98C5-512E-45E0-8F4F-715A45F5707A}',
	'IConstraintClasses' : '{7D9A71CB-B02F-4A1B-9995-2ADF58C69494}',
	'IClassClearances' : '{96FD6C42-8C02-4A00-A1B6-C47FB0D47913}',
	'IClassClearance' : '{77040253-C4BE-4037-B759-739678531FE8}',
	'IScheme' : '{6F39247C-17C2-4C9F-B14C-469620C80FC4}',
	'ISchemeNetClasses' : '{FA885B75-B122-4B9E-BAA2-87C657CB5659}',
	'ISchemeNetClass' : '{06818093-77D0-48D0-847E-77DFFAB80667}',
	'IRuleLayers' : '{6710F183-E176-48F4-B3CA-DBD22E0CF5FF}',
	'IRuleLayer' : '{F25192FE-8196-46B9-BF8A-CBA1AFA316A3}',
	'ISchemeClearanceRules' : '{8F934507-D505-4A25-A96A-1654C17B5C81}',
	'ISchemeClearanceRule' : '{DD8B4252-8E56-4A1A-B5CC-2A3A1284B1C5}',
	'IClearanceRule' : '{A0F38DDB-184D-4D4E-9E99-FFF4E73A4235}',
	'IConstraintClassesMutable' : '{E4076B8B-3F93-407C-8E18-9DD473F3C4B6}',
	'INoiseRules' : '{ED063FFC-209C-48D7-8D59-6677873C9A7A}',
	'INoiseRule' : '{D06D3CAD-4D4E-40B8-9A9A-16D446917F77}',
	'IParallelismRule' : '{A11D8E06-CE97-402B-AFD5-D75BACE22E1A}',
	'IParallelismRuleSegmentsMutable' : '{DEB98723-9BE8-482E-A482-E511BA818C2C}',
	'IParallelismRuleSegments' : '{201C826A-8C6C-4172-931F-92F9208F3717}',
	'IParallelismRuleSegment' : '{C391FA67-1209-4DD6-BD23-9D3DD7332651}',
	'IElectricalNetsMutable' : '{6F698C72-5BBF-4DEE-A09C-065A7AB68829}',
	'IElectricalNets' : '{26EBA780-1293-4DF0-87B3-2F4113E178CB}',
	'IElectricalNet' : '{7DB3D012-77AB-47DF-9C24-9A297A370AD0}',
	'IPowerNetsMutable' : '{B224A038-B04A-47E1-8F9F-C7938C61FD68}',
	'IPowerNets' : '{88AFDE06-B464-4045-8FC0-321DAAB9EDDE}',
	'IDifferentialPairsMutable' : '{7E649A6C-5038-4FD1-94D9-44A56CAC894E}',
	'IDifferentialPairs' : '{3F1097CF-2AFC-4D0B-8477-FEA016F94987}',
	'IDifferentialPair' : '{90FF1694-9C25-4F12-A08B-999F24686B57}',
	'IClearanceRulesMutable' : '{088425F1-88A0-4675-B9B9-D6FBC0454CF3}',
	'IClearanceRules' : '{349CEE9A-3FFB-4FA8-AB31-F98DC12E4E74}',
	'IMatchGroupsMutable' : '{F36348AB-8180-41C3-951F-0B079E3FF03F}',
	'IFormulasMutable' : '{AF4369BD-BEF9-48A7-849A-F39065467C85}',
	'IFormulas' : '{7232F46D-2CFB-423B-927D-E8B1AA3B959A}',
	'INoiseRulesMutable' : '{D07554EB-FCFF-48EC-AD04-C79988D20C9D}',
	'IParallelismRulesMutable' : '{E37D92BA-6E24-45E0-859C-43A40855C3AD}',
	'IParallelismRules' : '{595C88AE-5AAA-431C-97BD-5B3C181097EF}',
	'IComponentsMutable' : '{E010B178-C036-4BDE-815F-9B48CE213D1E}',
	'IComponents' : '{AC3ABD04-B1DD-47C7-8A94-404DFD764E56}',
	'IComponent' : '{60516EC5-86D9-4E16-86E7-9B66302D3A83}',
	'IPartsMutable' : '{965F3ED3-C357-4CD4-8778-9B61B12D5D24}',
	'IParts' : '{CD4E27CD-B11C-4EDD-B1BE-6D1996D3A4F1}',
	'IPart' : '{2D3374B6-ED6A-4024-AC29-ACF03A09B7C5}',
	'IPartPinsMutable' : '{8596DD5E-2C99-4DED-9A1F-D9067D3D34DB}',
	'IPartPinPairsMutable' : '{7DA3F078-E3B2-4436-A267-6FC09F25AB19}',
	'IConstantsMutable' : '{3C22162A-1920-4AF1-B2BA-805CC3A2500C}',
	'IConstants' : '{F5D6BDC5-5DB8-4F47-AC16-CABDF8BE0437}',
	'IConstant' : '{E43EED65-B104-4518-A7C0-21C3FA01B4F5}',
	'IVariablesMutable' : '{9B803C91-3B87-4F74-810E-C038E63376B7}',
	'IVariables' : '{CB2822E1-C294-4DD7-8DAC-A30B11174649}',
	'IVariable' : '{FB9D7374-6228-4B92-8403-03F3927706DE}',
	'IStackup' : '{FBFDBD21-1B6F-4263-A285-6FB6E9C7747F}',
	'ILayersMutable' : '{39981775-2776-4221-AB3C-1C27040DB64E}',
	'ILayers' : '{A8C2D4D7-EF76-436C-BDC8-0813B8248EBF}',
	'ILayer' : '{052E8B90-0E4C-44C1-8F39-89E344392B5C}',
	'IPhysicalRules' : '{F1F96334-F630-42BA-A3F4-2D314D51D535}',
	'ISchemesMutable' : '{C868C166-9607-4506-AEF9-5AE4FB428F95}',
	'ISchemes' : '{08A1E04B-6987-41C4-90E5-CA467E65937B}',
	'IClassClearancesMutable' : '{FA648CF5-E9A3-4841-AD76-BD4BCD55DF45}',
	'IGeneralClearancesMutable' : '{BC62A287-210A-4466-A894-5ACB1F4E0E25}',
	'IGeneralClearances' : '{A96A5A2C-6E39-4FB7-A86C-C6992501261A}',
	'IGeneralClearance' : '{D7ABE808-2624-4912-B413-96F9E0B5BA5B}',
	'IPackageClearancesMutable' : '{D2CFD11E-A067-4F0F-BE2F-17A9F507040E}',
	'IPackageClearances' : '{B5A4D7C8-1D7D-42CB-8E1D-508B0BD67DCC}',
	'IPackageClearance' : '{240DA68C-6822-4B65-A4B3-8E7AB10B66AE}',
	'IPackageType' : '{9253A04D-448B-459A-AF00-BC956F499198}',
	'IDisplayPatternsMutable' : '{209DB434-B7A4-4CF7-A1DC-87CFD2B21543}',
	'IDisplayPatterns' : '{D47DF953-026D-440D-819D-2DE548AD17C4}',
	'IPackageTypesMutable' : '{EA65AC00-04E5-42F6-AC61-7FA81534926F}',
	'IPackageTypes' : '{4536460C-7AFD-40EE-ADED-BBE2D068ECC8}',
	'ISettings' : '{8D9E96B8-678C-4EC9-93EE-F7E4CEC025FB}',
	'IUnits' : '{19C74DFD-6D72-4514-BAEB-D6FF7C4A1182}',
	'INotation' : '{177B82E6-3AFF-4E52-8141-7911C63B1879}',
	'IDRC' : '{D9FEE0D7-B9FE-41C9-9FCF-6597EDC8E2AF}',
}

win32com.client.constants.__dicts__.append(constants.__dict__)

__all__ = ['IBase','IClass','IClassClearance','IClassClearances','IClassClearancesMutable','IClearanceRule','IClearanceRules','IClearanceRulesMutable','ICollection','IComment','IComments','ICommentsMutable','IComponent','IComponents','IComponentsMutable','IConstant','IConstants','IConstantsMutable','IConstraint','IConstraintClass','IConstraintClasses','IConstraintClassesMutable','IConstraints','IConstraintsAuto','IConstraintsMutable','IDRC','IDesign','IDesignParams','IDifferentialPair','IDifferentialPairs','IDifferentialPairsMutable','IDisplayPattern','IDisplayPatterns','IDisplayPatternsMutable','IElectricalNet','IElectricalNets','IElectricalNetsMutable','IFormula','IFormulas','IFormulasMutable','IFromTo','IFromTos','IFromTosMutable','IGeneralClearance','IGeneralClearances','IGeneralClearancesMutable','ILayer','ILayers','ILayersMutable','IMatchGroup','IMatchGroups','IMatchGroupsMutable','INet','INetClass','INetClasses','INetClassesMutable','INets','INetsMutable','INoiseRule','INoiseRules','INoiseRulesMutable','INotation','IObject','IObjects','IPackageClearance','IPackageClearances','IPackageClearancesMutable','IPackageType','IPackageTypes','IPackageTypesMutable','IParallelismRule','IParallelismRuleSegment','IParallelismRuleSegments','IParallelismRuleSegmentsMutable','IParallelismRules','IParallelismRulesMutable','IPart','IPartPin','IPartPinPair','IPartPinPairs','IPartPinPairsMutable','IPartPins','IPartPinsMutable','IParts','IPartsMutable','IPhysicalRules','IPin','IPinPair','IPinPairs','IPinPairsMutable','IPinSet','IPinSets','IPinSetsMutable','IPins','IPinsMutable','IPowerNets','IPowerNetsMutable','IRuleLayer','IRuleLayers','IScheme','ISchemeClearanceRule','ISchemeClearanceRules','ISchemeNetClass','ISchemeNetClasses','ISchemes','ISchemesMutable','ISettings','IStackup','ITopology','IUnits','IVariable','IVariables','IVariablesMutable']
