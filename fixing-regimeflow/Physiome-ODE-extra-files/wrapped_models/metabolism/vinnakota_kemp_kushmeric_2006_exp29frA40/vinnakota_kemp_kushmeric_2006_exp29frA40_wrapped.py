# Size of variable arrays:
sizeAlgebraic = 312
sizeStates = 25
sizeConstants = 342
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (minute)"
    legend_algebraic[0] = "pH_cy in component environment (dimensionless)"
    legend_constants[34] = "addbuffer in component environment (dimensionless)"
    legend_constants[35] = "pHstat in component environment (dimensionless)"
    legend_constants[2] = "Par_97 in component parameters (dimensionless)"
    legend_constants[3] = "Par_98 in component parameters (dimensionless)"
    legend_states[0] = "pH_calc in component differential_equations (dimensionless)"
    legend_constants[0] = "R in component global_parameters (kilojoule_per_kelvin_per_mole)"
    legend_constants[1] = "T1 in component global_parameters (kelvin)"
    legend_constants[130] = "T in component global_parameters (kelvin)"
    legend_constants[125] = "I in component global_parameters (molar)"
    legend_constants[124] = "Par_90 in component parameters (molar)"
    legend_constants[129] = "Par_94 in component parameters (kelvin)"
    legend_constants[4] = "Par_1 in component parameters (molar_per_minute)"
    legend_constants[5] = "Par_2 in component parameters (dimensionless)"
    legend_constants[6] = "Par_3 in component parameters (molar)"
    legend_constants[36] = "Par_4 in component parameters (molar)"
    legend_constants[56] = "Par_5 in component parameters (molar)"
    legend_constants[7] = "Par_6 in component parameters (molar)"
    legend_constants[57] = "Par_7 in component parameters (molar)"
    legend_constants[8] = "Par_8 in component parameters (molar)"
    legend_constants[58] = "Par_9 in component parameters (molar)"
    legend_constants[59] = "Par_10 in component parameters (molar)"
    legend_constants[9] = "Par_11 in component parameters (molar)"
    legend_constants[60] = "Par_12 in component parameters (molar)"
    legend_constants[61] = "Par_13 in component parameters (molar)"
    legend_constants[10] = "Par_14 in component parameters (molar)"
    legend_constants[62] = "Par_15 in component parameters (molar)"
    legend_constants[11] = "Par_16 in component parameters (molar)"
    legend_constants[12] = "Par_17 in component parameters (dimensionless)"
    legend_constants[13] = "Par_18 in component parameters (dimensionless)"
    legend_constants[63] = "Par_19 in component parameters (molar_per_minute)"
    legend_constants[64] = "Par_20 in component parameters (molar)"
    legend_constants[65] = "Par_21 in component parameters (molar)"
    legend_constants[66] = "Par_22 in component parameters (molar_per_minute)"
    legend_constants[67] = "Par_23 in component parameters (molar)"
    legend_constants[68] = "Par_24 in component parameters (molar)"
    legend_constants[69] = "Par_25 in component parameters (molar_per_minute)"
    legend_constants[70] = "Par_26 in component parameters (molar)"
    legend_constants[71] = "Par_27 in component parameters (molar)"
    legend_constants[72] = "Par_28 in component parameters (molar)"
    legend_constants[73] = "Par_29 in component parameters (molar)"
    legend_constants[74] = "Par_30 in component parameters (molar)"
    legend_constants[14] = "Par_31 in component parameters (molar)"
    legend_constants[75] = "Par_32 in component parameters (molar)"
    legend_constants[15] = "Par_33 in component parameters (molar)"
    legend_constants[16] = "Par_34 in component parameters (molar)"
    legend_constants[17] = "Par_35 in component parameters (molar)"
    legend_constants[18] = "Par_36 in component parameters (dimensionless)"
    legend_constants[19] = "Par_37 in component parameters (dimensionless)"
    legend_constants[20] = "Par_38 in component parameters (dimensionless)"
    legend_constants[76] = "Par_39 in component parameters (molar_per_minute)"
    legend_constants[77] = "Par_40 in component parameters (molar)"
    legend_constants[78] = "Par_41 in component parameters (molar)"
    legend_constants[79] = "Par_42 in component parameters (molar)"
    legend_constants[80] = "Par_43 in component parameters (molar_per_minute)"
    legend_constants[81] = "Par_44 in component parameters (molar)"
    legend_constants[82] = "Par_45 in component parameters (molar)"
    legend_constants[83] = "Par_46 in component parameters (molar_per_minute)"
    legend_constants[84] = "Par_47 in component parameters (molar)"
    legend_constants[85] = "Par_48 in component parameters (molar)"
    legend_constants[86] = "Par_49 in component parameters (molar)"
    legend_constants[87] = "Par_50 in component parameters (molar)"
    legend_constants[88] = "Par_51 in component parameters (molar_per_minute)"
    legend_constants[89] = "Par_52 in component parameters (molar)"
    legend_constants[90] = "Par_53 in component parameters (molar)"
    legend_constants[91] = "Par_54 in component parameters (molar)"
    legend_constants[92] = "Par_55 in component parameters (molar)"
    legend_constants[93] = "Par_56 in component parameters (molar)"
    legend_constants[94] = "Par_57 in component parameters (molar_per_minute)"
    legend_constants[95] = "Par_58 in component parameters (molar)"
    legend_constants[96] = "Par_59 in component parameters (molar)"
    legend_constants[97] = "Par_60 in component parameters (molar)"
    legend_constants[98] = "Par_61 in component parameters (molar)"
    legend_constants[99] = "Par_62 in component parameters (molar_per_minute)"
    legend_constants[100] = "Par_63 in component parameters (molar)"
    legend_constants[101] = "Par_64 in component parameters (molar)"
    legend_constants[102] = "Par_65 in component parameters (molar_per_minute)"
    legend_constants[103] = "Par_66 in component parameters (molar)"
    legend_constants[104] = "Par_67 in component parameters (molar)"
    legend_constants[105] = "Par_68 in component parameters (molar_per_minute)"
    legend_constants[106] = "Par_69 in component parameters (molar)"
    legend_constants[107] = "Par_70 in component parameters (molar)"
    legend_constants[108] = "Par_71 in component parameters (molar)"
    legend_constants[109] = "Par_72 in component parameters (molar)"
    legend_constants[110] = "Par_73 in component parameters (molar_per_minute)"
    legend_constants[111] = "Par_74 in component parameters (molar)"
    legend_constants[112] = "Par_75 in component parameters (molar)"
    legend_constants[113] = "Par_76 in component parameters (molar)"
    legend_constants[114] = "Par_77 in component parameters (molar)"
    legend_constants[115] = "Par_78 in component parameters (molar_per_minute)"
    legend_constants[116] = "Par_79 in component parameters (molar)"
    legend_constants[117] = "Par_80 in component parameters (molar)"
    legend_constants[118] = "Par_81 in component parameters (molar)"
    legend_constants[21] = "Par_82 in component parameters (molar)"
    legend_constants[119] = "Par_83 in component parameters (molar)"
    legend_constants[120] = "Par_84 in component parameters (molar_per_minute)"
    legend_constants[121] = "Par_85 in component parameters (molar)"
    legend_constants[122] = "Par_86 in component parameters (molar)"
    legend_constants[123] = "Par_87 in component parameters (molar)"
    legend_constants[22] = "Par_88 in component parameters (molar_per_minute)"
    legend_constants[23] = "Par_89 in component parameters (molar)"
    legend_constants[126] = "Par_91 in component parameters (molar)"
    legend_constants[127] = "Par_92 in component parameters (molar)"
    legend_constants[128] = "Par_93 in component parameters (molar)"
    legend_constants[24] = "Par_95 in component parameters (molar)"
    legend_constants[131] = "Par_96 in component parameters (molar)"
    legend_constants[132] = "Par_99 in component parameters (dimensionless)"
    legend_constants[25] = "Par_100 in component parameters (dimensionless)"
    legend_constants[37] = "mgT in component equilibrium_constants (molar)"
    legend_constants[133] = "k in component equilibrium_constants (molar)"
    legend_constants[134] = "c0 in component equilibrium_constants (molar)"
    legend_constants[135] = "RT2dadT in component correction_factors (kilojoule_half_liter_per_3_half_mole)"
    legend_constants[136] = "B in component correction_factors (per_half_molar)"
    legend_constants[137] = "Icorr in component correction_factors (kilojoule_per_mole)"
    legend_constants[138] = "I1 in component correction_factors (molar)"
    legend_constants[139] = "alphadebye in component correction_factors (per_half_molar)"
    legend_constants[140] = "IcorrpKa in component correction_factors (kilojoule_per_mole)"
    legend_constants[141] = "TcorrpKa in component correction_factors (mole_per_kilojoule)"
    legend_constants[142] = "RTalpha in component correction_factors (kilojoule_half_liter_per_3_half_mole)"
    legend_constants[143] = "IcorrdeltaGpof in component correction_factors (kilojoule_per_mole)"
    legend_constants[144] = "pKak_Pi in component correction_factors (dimensionless)"
    legend_constants[145] = "deltaH1o_Pi in component correction_factors (kilojoule_per_mole)"
    legend_constants[146] = "deltaHmgo_Pi in component correction_factors (kilojoule_per_mole)"
    legend_constants[147] = "deltaH1_Pi in component correction_factors (kilojoule_per_mole)"
    legend_constants[148] = "deltaHmg_Pi in component correction_factors (kilojoule_per_mole)"
    legend_constants[149] = "pKa1_Pi in component correction_factors (dimensionless)"
    legend_constants[150] = "pKamg_Pi in component correction_factors (dimensionless)"
    legend_algebraic[1] = "P_Pi in component correction_factors (dimensionless)"
    legend_algebraic[2] = "HPi2 in component correction_factors (dimensionless)"
    legend_algebraic[3] = "H2Pi1 in component correction_factors (dimensionless)"
    legend_algebraic[4] = "kPi in component correction_factors (dimensionless)"
    legend_algebraic[5] = "mgPi in component correction_factors (dimensionless)"
    legend_algebraic[6] = "Navg_Pi in component correction_factors (dimensionless)"
    legend_algebraic[7] = "dNavgPidH in component correction_factors (per_molar)"
    legend_algebraic[8] = "dNavgPidmg in component correction_factors (per_molar)"
    legend_algebraic[9] = "dmgPidmg in component correction_factors (per_molar)"
    legend_algebraic[10] = "dmgPidpH in component correction_factors (dimensionless)"
    legend_constants[151] = "NH_HPi2 in component correction_factors (dimensionless)"
    legend_constants[152] = "deltaGof_HPi2 in component correction_factors (kilojoule_per_mole)"
    legend_algebraic[11] = "deltaGpof_HPi2 in component correction_factors (kilojoule_per_mole)"
    legend_constants[153] = "deltaH1o_ATP in component correction_factors (kilojoule_per_mole)"
    legend_constants[154] = "deltaHmgo_ATP in component correction_factors (kilojoule_per_mole)"
    legend_constants[155] = "deltaHko_ATP in component correction_factors (kilojoule_per_mole)"
    legend_constants[156] = "deltaH1_ATP in component correction_factors (kilojoule_per_mole)"
    legend_constants[157] = "deltaHmg_ATP in component correction_factors (kilojoule_per_mole)"
    legend_constants[158] = "deltaHk_ATP in component correction_factors (kilojoule_per_mole)"
    legend_constants[159] = "pKa1_ATP in component correction_factors (dimensionless)"
    legend_constants[160] = "pKamg_ATP in component correction_factors (dimensionless)"
    legend_constants[161] = "pKak_ATP in component correction_factors (dimensionless)"
    legend_algebraic[12] = "P_ATP in component correction_factors (dimensionless)"
    legend_algebraic[13] = "ATP4 in component correction_factors (dimensionless)"
    legend_algebraic[14] = "HATP3 in component correction_factors (dimensionless)"
    legend_algebraic[15] = "mgATP2 in component correction_factors (dimensionless)"
    legend_algebraic[16] = "kATP in component correction_factors (dimensionless)"
    legend_algebraic[17] = "Navg_ATP in component correction_factors (dimensionless)"
    legend_algebraic[18] = "dNavgATPdH in component correction_factors (per_molar)"
    legend_algebraic[19] = "dNavgATPdmg in component correction_factors (per_molar)"
    legend_algebraic[20] = "dmgATP2dmg in component correction_factors (per_molar)"
    legend_algebraic[21] = "dmgATP2dpH in component correction_factors (dimensionless)"
    legend_constants[162] = "NH_ATP4 in component correction_factors (dimensionless)"
    legend_constants[163] = "deltaGof_ATP4 in component correction_factors (kilojoule_per_mole)"
    legend_algebraic[22] = "deltaGpof_ATP4 in component correction_factors (kilojoule_per_mole)"
    legend_constants[164] = "pKak_ADP in component correction_factors (dimensionless)"
    legend_constants[165] = "deltaH1o_ADP in component correction_factors (kilojoule_per_mole)"
    legend_constants[166] = "deltaHmgo_ADP in component correction_factors (kilojoule_per_mole)"
    legend_constants[167] = "deltaH1_ADP in component correction_factors (kilojoule_per_mole)"
    legend_constants[168] = "deltaHmg_ADP in component correction_factors (kilojoule_per_mole)"
    legend_constants[169] = "pKa1_ADP in component correction_factors (dimensionless)"
    legend_constants[170] = "pKamg_ADP in component correction_factors (dimensionless)"
    legend_algebraic[23] = "P_ADP in component correction_factors (dimensionless)"
    legend_algebraic[24] = "ADP3 in component correction_factors (dimensionless)"
    legend_algebraic[25] = "HADP2 in component correction_factors (dimensionless)"
    legend_algebraic[26] = "mgADP in component correction_factors (dimensionless)"
    legend_algebraic[27] = "kADP in component correction_factors (dimensionless)"
    legend_algebraic[28] = "Navg_ADP in component correction_factors (dimensionless)"
    legend_algebraic[29] = "dNavgADPdH in component correction_factors (per_molar)"
    legend_algebraic[31] = "dNavgADPdmg in component correction_factors (per_molar)"
    legend_algebraic[32] = "dmgADPdmg in component correction_factors (per_molar)"
    legend_algebraic[33] = "dmgADPdpH in component correction_factors (dimensionless)"
    legend_constants[171] = "NH_ADP3 in component correction_factors (dimensionless)"
    legend_constants[172] = "deltaGof_ADP3 in component correction_factors (kilojoule_per_mole)"
    legend_algebraic[34] = "deltaGpof_ADP3 in component correction_factors (kilojoule_per_mole)"
    legend_constants[173] = "deltaH1o_AMP in component correction_factors (kilojoule_per_mole)"
    legend_constants[174] = "deltaHmgo_AMP in component correction_factors (kilojoule_per_mole)"
    legend_constants[175] = "deltaH1_AMP in component correction_factors (kilojoule_per_mole)"
    legend_constants[176] = "deltaHmg_AMP in component correction_factors (kilojoule_per_mole)"
    legend_constants[177] = "pKa1_AMP in component correction_factors (dimensionless)"
    legend_constants[178] = "pKamg_AMP in component correction_factors (dimensionless)"
    legend_algebraic[35] = "P_AMP in component correction_factors (dimensionless)"
    legend_algebraic[36] = "AMP2 in component correction_factors (dimensionless)"
    legend_algebraic[37] = "HAMP1 in component correction_factors (dimensionless)"
    legend_algebraic[38] = "mgAMP in component correction_factors (dimensionless)"
    legend_algebraic[39] = "Navg_AMP in component correction_factors (dimensionless)"
    legend_algebraic[40] = "dNavgAMPdH in component correction_factors (per_molar)"
    legend_algebraic[41] = "dNavgAMPdmg in component correction_factors (per_molar)"
    legend_algebraic[42] = "dmgAMPdmg in component correction_factors (per_molar)"
    legend_algebraic[43] = "dmgAMPdpH in component correction_factors (dimensionless)"
    legend_constants[179] = "NH_AMP2 in component correction_factors (dimensionless)"
    legend_constants[180] = "deltaGof_AMP2 in component correction_factors (kilojoule_per_mole)"
    legend_algebraic[44] = "deltaGpof_AMP2 in component correction_factors (kilojoule_per_mole)"
    legend_constants[181] = "pKak_PCR in component correction_factors (dimensionless)"
    legend_constants[182] = "deltaH1o_PCR in component correction_factors (kilojoule_per_mole)"
    legend_constants[183] = "deltaHmgo_PCR in component correction_factors (kilojoule_per_mole)"
    legend_constants[184] = "deltaH1_PCR in component correction_factors (kilojoule_per_mole)"
    legend_constants[185] = "deltaHmg_PCR in component correction_factors (kilojoule_per_mole)"
    legend_constants[186] = "pKa1_PCR in component correction_factors (dimensionless)"
    legend_constants[187] = "pKamg_PCR in component correction_factors (dimensionless)"
    legend_algebraic[45] = "P_PCR in component correction_factors (dimensionless)"
    legend_algebraic[46] = "HPCR in component correction_factors (dimensionless)"
    legend_algebraic[48] = "H2PCR in component correction_factors (dimensionless)"
    legend_algebraic[47] = "kPCR in component correction_factors (dimensionless)"
    legend_algebraic[49] = "mgPCR in component correction_factors (dimensionless)"
    legend_algebraic[50] = "Navg_PCR in component correction_factors (dimensionless)"
    legend_algebraic[51] = "dNavgPCRdH in component correction_factors (per_molar)"
    legend_algebraic[52] = "dNavgPCRdmg in component correction_factors (per_molar)"
    legend_algebraic[53] = "dmgPCRdmg in component correction_factors (per_molar)"
    legend_algebraic[54] = "dmgPCRdpH in component correction_factors (dimensionless)"
    legend_constants[188] = "NH_HPCR in component correction_factors (dimensionless)"
    legend_constants[189] = "pKa1_CR in component correction_factors (dimensionless)"
    legend_algebraic[55] = "P_CR in component correction_factors (dimensionless)"
    legend_algebraic[56] = "HCR in component correction_factors (dimensionless)"
    legend_algebraic[57] = "H2CR in component correction_factors (dimensionless)"
    legend_algebraic[58] = "Navg_CR in component correction_factors (dimensionless)"
    legend_algebraic[59] = "dNavgCRdH in component correction_factors (per_molar)"
    legend_constants[26] = "dNavgCRdmg in component correction_factors (per_molar)"
    legend_constants[190] = "NH_HCR in component correction_factors (dimensionless)"
    legend_constants[191] = "deltaH1o_G1P in component correction_factors (kilojoule_per_mole)"
    legend_constants[192] = "deltaHmgo_G1P in component correction_factors (kilojoule_per_mole)"
    legend_constants[193] = "deltaH1_G1P in component correction_factors (kilojoule_per_mole)"
    legend_constants[194] = "deltaHmg_G1P in component correction_factors (kilojoule_per_mole)"
    legend_constants[195] = "pKa1_G1P in component correction_factors (dimensionless)"
    legend_constants[196] = "pKamg_G1P in component correction_factors (dimensionless)"
    legend_algebraic[60] = "P_G1P in component correction_factors (dimensionless)"
    legend_algebraic[61] = "UG1P in component correction_factors (dimensionless)"
    legend_algebraic[62] = "HG1P in component correction_factors (dimensionless)"
    legend_algebraic[63] = "mgG1P in component correction_factors (dimensionless)"
    legend_algebraic[64] = "Navg_G1P in component correction_factors (dimensionless)"
    legend_algebraic[65] = "dNavgG1PdH in component correction_factors (per_molar)"
    legend_algebraic[66] = "dNavgG1Pdmg in component correction_factors (per_molar)"
    legend_algebraic[67] = "dmgG1Pdmg in component correction_factors (per_molar)"
    legend_algebraic[68] = "dmgG1PdpH in component correction_factors (dimensionless)"
    legend_constants[197] = "NH_UG1P in component correction_factors (dimensionless)"
    legend_constants[198] = "deltaGof_UG1P in component correction_factors (kilojoule_per_mole)"
    legend_algebraic[69] = "deltaGpof_UG1P in component correction_factors (kilojoule_per_mole)"
    legend_constants[199] = "pKa1_G6P in component correction_factors (dimensionless)"
    legend_algebraic[70] = "P_G6P in component correction_factors (dimensionless)"
    legend_algebraic[71] = "UG6P in component correction_factors (dimensionless)"
    legend_algebraic[72] = "HG6P in component correction_factors (dimensionless)"
    legend_algebraic[73] = "Navg_G6P in component correction_factors (dimensionless)"
    legend_algebraic[74] = "dNavgG6PdH in component correction_factors (per_molar)"
    legend_constants[27] = "dNavgG6Pdmg in component correction_factors (per_molar)"
    legend_constants[200] = "NH_UG6P in component correction_factors (dimensionless)"
    legend_constants[201] = "deltaGof_UG6P in component correction_factors (kilojoule_per_mole)"
    legend_algebraic[75] = "deltaGpof_UG6P in component correction_factors (kilojoule_per_mole)"
    legend_constants[202] = "pKa1_F6P in component correction_factors (dimensionless)"
    legend_algebraic[76] = "P_F6P in component correction_factors (dimensionless)"
    legend_algebraic[77] = "UF6P in component correction_factors (dimensionless)"
    legend_algebraic[78] = "HF6P in component correction_factors (dimensionless)"
    legend_algebraic[79] = "Navg_F6P in component correction_factors (dimensionless)"
    legend_algebraic[80] = "dNavgF6PdH in component correction_factors (per_molar)"
    legend_constants[28] = "dNavgF6Pdmg in component correction_factors (per_molar)"
    legend_constants[203] = "NH_UF6P in component correction_factors (dimensionless)"
    legend_constants[204] = "deltaGof_UF6P in component correction_factors (kilojoule_per_mole)"
    legend_algebraic[81] = "deltaGpof_UF6P in component correction_factors (kilojoule_per_mole)"
    legend_constants[205] = "pKa1_FDP in component correction_factors (dimensionless)"
    legend_constants[206] = "pKa2_FDP in component correction_factors (dimensionless)"
    legend_constants[207] = "pKamg_FDP in component correction_factors (dimensionless)"
    legend_algebraic[82] = "P_FDP in component correction_factors (dimensionless)"
    legend_algebraic[83] = "UFDP in component correction_factors (dimensionless)"
    legend_algebraic[84] = "HFDP in component correction_factors (dimensionless)"
    legend_algebraic[85] = "H2FDP in component correction_factors (dimensionless)"
    legend_algebraic[86] = "mgFDP in component correction_factors (dimensionless)"
    legend_algebraic[87] = "Navg_FDP in component correction_factors (dimensionless)"
    legend_algebraic[88] = "dNavgFDPdH in component correction_factors (per_molar)"
    legend_algebraic[89] = "dNavgFDPdmg in component correction_factors (per_molar)"
    legend_algebraic[90] = "dmgFDPdmg in component correction_factors (per_molar)"
    legend_algebraic[91] = "dmgFDPdpH in component correction_factors (dimensionless)"
    legend_constants[208] = "NH_UFDP in component correction_factors (dimensionless)"
    legend_constants[209] = "deltaGof_UFDP in component correction_factors (kilojoule_per_mole)"
    legend_algebraic[92] = "deltaGpof_UFDP in component correction_factors (kilojoule_per_mole)"
    legend_constants[210] = "pKa1_GAP in component correction_factors (dimensionless)"
    legend_algebraic[93] = "P_GAP in component correction_factors (dimensionless)"
    legend_algebraic[94] = "UGAP in component correction_factors (dimensionless)"
    legend_algebraic[95] = "HGAP in component correction_factors (dimensionless)"
    legend_algebraic[96] = "Navg_GAP in component correction_factors (dimensionless)"
    legend_algebraic[97] = "dNavgGAPdH in component correction_factors (per_molar)"
    legend_constants[29] = "dNavgGAPdmg in component correction_factors (per_molar)"
    legend_constants[211] = "NH_UGAP in component correction_factors (dimensionless)"
    legend_constants[212] = "deltaGof_UGAP in component correction_factors (kilojoule_per_mole)"
    legend_algebraic[98] = "deltaGpof_UGAP in component correction_factors (kilojoule_per_mole)"
    legend_constants[213] = "pKamg_G3P in component correction_factors (dimensionless)"
    legend_constants[214] = "deltaH1o_G3P in component correction_factors (kilojoule_per_mole)"
    legend_constants[215] = "deltaH1_G3P in component correction_factors (kilojoule_per_mole)"
    legend_constants[216] = "pKa1_G3P in component correction_factors (dimensionless)"
    legend_algebraic[99] = "P_G3P in component correction_factors (dimensionless)"
    legend_algebraic[100] = "UG3P in component correction_factors (dimensionless)"
    legend_algebraic[101] = "HG3P in component correction_factors (dimensionless)"
    legend_algebraic[102] = "mgG3P in component correction_factors (dimensionless)"
    legend_algebraic[103] = "Navg_G3P in component correction_factors (dimensionless)"
    legend_algebraic[104] = "dNavgG3PdH in component correction_factors (per_molar)"
    legend_algebraic[105] = "dNavgG3Pdmg in component correction_factors (per_molar)"
    legend_algebraic[106] = "dmgG3Pdmg in component correction_factors (per_molar)"
    legend_algebraic[107] = "dmgG3PdpH in component correction_factors (dimensionless)"
    legend_constants[217] = "NH_UG3P in component correction_factors (dimensionless)"
    legend_constants[218] = "deltaGof_UG3P in component correction_factors (kilojoule_per_mole)"
    legend_algebraic[108] = "deltaGpof_UG3P in component correction_factors (kilojoule_per_mole)"
    legend_constants[219] = "pKa1_DHAP in component correction_factors (dimensionless)"
    legend_constants[220] = "pKamg_DHAP in component correction_factors (dimensionless)"
    legend_algebraic[109] = "P_DHAP in component correction_factors (dimensionless)"
    legend_algebraic[110] = "UDHAP in component correction_factors (dimensionless)"
    legend_algebraic[111] = "HDHAP in component correction_factors (dimensionless)"
    legend_algebraic[112] = "mgDHAP in component correction_factors (dimensionless)"
    legend_algebraic[113] = "Navg_DHAP in component correction_factors (dimensionless)"
    legend_algebraic[114] = "dNavgDHAPdH in component correction_factors (per_molar)"
    legend_algebraic[115] = "dNavgDHAPdmg in component correction_factors (per_molar)"
    legend_algebraic[116] = "dmgDHAPdmg in component correction_factors (per_molar)"
    legend_algebraic[117] = "dmgDHAPdpH in component correction_factors (dimensionless)"
    legend_constants[221] = "NH_UDHAP in component correction_factors (dimensionless)"
    legend_constants[222] = "deltaGof_UDHAP in component correction_factors (kilojoule_per_mole)"
    legend_algebraic[118] = "deltaGpof_UDHAP in component correction_factors (kilojoule_per_mole)"
    legend_constants[223] = "pKa1_13DPG in component correction_factors (dimensionless)"
    legend_algebraic[119] = "P_13DPG in component correction_factors (dimensionless)"
    legend_algebraic[120] = "U13DPG in component correction_factors (dimensionless)"
    legend_algebraic[121] = "H13DPG in component correction_factors (dimensionless)"
    legend_algebraic[122] = "Navg_13DPG in component correction_factors (dimensionless)"
    legend_algebraic[123] = "dNavg13DPGdH in component correction_factors (per_molar)"
    legend_constants[30] = "dNavg13DPGdmg in component correction_factors (per_molar)"
    legend_constants[224] = "NH_U13DPG in component correction_factors (dimensionless)"
    legend_constants[225] = "deltaGof_U13DPG in component correction_factors (kilojoule_per_mole)"
    legend_algebraic[124] = "deltaGpof_U13DPG in component correction_factors (kilojoule_per_mole)"
    legend_constants[226] = "pKa1_3PG in component correction_factors (dimensionless)"
    legend_algebraic[125] = "P_3PG in component correction_factors (dimensionless)"
    legend_algebraic[126] = "U3PG in component correction_factors (dimensionless)"
    legend_algebraic[127] = "H3PG in component correction_factors (dimensionless)"
    legend_algebraic[128] = "Navg_3PG in component correction_factors (dimensionless)"
    legend_algebraic[129] = "dNavg3PGdH in component correction_factors (per_molar)"
    legend_constants[31] = "dNavg3PGdmg in component correction_factors (per_molar)"
    legend_constants[227] = "NH_U3PG in component correction_factors (dimensionless)"
    legend_constants[228] = "deltaGof_U3PG in component correction_factors (kilojoule_per_mole)"
    legend_algebraic[130] = "deltaGpof_U3PG in component correction_factors (kilojoule_per_mole)"
    legend_constants[229] = "pKa1_2PG in component correction_factors (dimensionless)"
    legend_constants[230] = "pKamg_2PG in component correction_factors (dimensionless)"
    legend_constants[231] = "pKak_2PG in component correction_factors (dimensionless)"
    legend_algebraic[131] = "P_2PG in component correction_factors (dimensionless)"
    legend_algebraic[132] = "U2PG in component correction_factors (dimensionless)"
    legend_algebraic[133] = "H2PG in component correction_factors (dimensionless)"
    legend_algebraic[135] = "mg2PG in component correction_factors (dimensionless)"
    legend_algebraic[134] = "k2PG in component correction_factors (dimensionless)"
    legend_algebraic[136] = "Navg_2PG in component correction_factors (dimensionless)"
    legend_algebraic[137] = "dNavg2PGdH in component correction_factors (per_molar)"
    legend_algebraic[138] = "dNavg2PGdmg in component correction_factors (per_molar)"
    legend_algebraic[139] = "dmg2PGdmg in component correction_factors (per_molar)"
    legend_algebraic[140] = "dmg2PGdpH in component correction_factors (dimensionless)"
    legend_constants[232] = "NH_U2PG in component correction_factors (dimensionless)"
    legend_constants[233] = "deltaGof_U2PG in component correction_factors (kilojoule_per_mole)"
    legend_algebraic[141] = "deltaGpof_U2PG in component correction_factors (kilojoule_per_mole)"
    legend_constants[234] = "pKa1_PEP in component correction_factors (dimensionless)"
    legend_constants[235] = "pKamg_PEP in component correction_factors (dimensionless)"
    legend_constants[236] = "pKak_PEP in component correction_factors (dimensionless)"
    legend_algebraic[142] = "P_PEP in component correction_factors (dimensionless)"
    legend_algebraic[143] = "UPEP in component correction_factors (dimensionless)"
    legend_algebraic[144] = "HPEP in component correction_factors (dimensionless)"
    legend_algebraic[145] = "kPEP in component correction_factors (dimensionless)"
    legend_algebraic[146] = "mgPEP in component correction_factors (dimensionless)"
    legend_algebraic[147] = "Navg_PEP in component correction_factors (dimensionless)"
    legend_algebraic[148] = "dNavgPEPdH in component correction_factors (per_molar)"
    legend_algebraic[149] = "dNavgPEPdmg in component correction_factors (per_molar)"
    legend_algebraic[150] = "dmgPEPdmg in component correction_factors (per_molar)"
    legend_algebraic[151] = "dmgPEPdpH in component correction_factors (dimensionless)"
    legend_constants[237] = "NH_UPEP in component correction_factors (dimensionless)"
    legend_constants[238] = "deltaGof_UPEP in component correction_factors (kilojoule_per_mole)"
    legend_algebraic[152] = "deltaGpof_UPEP in component correction_factors (kilojoule_per_mole)"
    legend_constants[239] = "pKa1_PYR in component correction_factors (dimensionless)"
    legend_algebraic[153] = "P_PYR in component correction_factors (dimensionless)"
    legend_algebraic[154] = "UPYR in component correction_factors (dimensionless)"
    legend_algebraic[155] = "HPYR in component correction_factors (dimensionless)"
    legend_algebraic[156] = "Navg_PYR in component correction_factors (dimensionless)"
    legend_algebraic[157] = "dNavgPYRdH in component correction_factors (per_molar)"
    legend_constants[32] = "dNavgPYRdmg in component correction_factors (per_molar)"
    legend_constants[240] = "NH_UPYR in component correction_factors (dimensionless)"
    legend_constants[241] = "deltaGof_UPYR in component correction_factors (kilojoule_per_mole)"
    legend_algebraic[158] = "deltaGpof_UPYR in component correction_factors (kilojoule_per_mole)"
    legend_constants[242] = "pKamg_LAC in component correction_factors (dimensionless)"
    legend_constants[243] = "deltaH1o_LAC in component correction_factors (kilojoule_per_mole)"
    legend_constants[244] = "deltaH1_LAC in component correction_factors (kilojoule_per_mole)"
    legend_constants[245] = "pKa1_LAC in component correction_factors (dimensionless)"
    legend_algebraic[159] = "P_LAC in component correction_factors (dimensionless)"
    legend_algebraic[160] = "ULAC in component correction_factors (dimensionless)"
    legend_algebraic[161] = "HLAC in component correction_factors (dimensionless)"
    legend_algebraic[162] = "mgLAC in component correction_factors (dimensionless)"
    legend_algebraic[163] = "Navg_LAC in component correction_factors (dimensionless)"
    legend_algebraic[164] = "dNavgLACdH in component correction_factors (per_molar)"
    legend_algebraic[165] = "dNavgLACdmg in component correction_factors (per_molar)"
    legend_algebraic[166] = "dmgLACdmg in component correction_factors (per_molar)"
    legend_algebraic[167] = "dmgLACdpH in component correction_factors (dimensionless)"
    legend_constants[246] = "NH_ULAC in component correction_factors (dimensionless)"
    legend_constants[247] = "deltaGof_ULAC in component correction_factors (kilojoule_per_mole)"
    legend_algebraic[168] = "deltaGpof_ULAC in component correction_factors (kilojoule_per_mole)"
    legend_constants[248] = "dNH_GLY in component correction_factors (dimensionless)"
    legend_algebraic[169] = "deltaGpo_GLY in component correction_factors (kilojoule_per_mole)"
    legend_constants[249] = "NH_NAD in component correction_factors (dimensionless)"
    legend_constants[250] = "deltaGof_NAD in component correction_factors (kilojoule_per_mole)"
    legend_algebraic[170] = "deltaGpof_NAD in component correction_factors (kilojoule_per_mole)"
    legend_constants[251] = "NH_NADH in component correction_factors (dimensionless)"
    legend_constants[252] = "deltaGof_NADH in component correction_factors (kilojoule_per_mole)"
    legend_algebraic[171] = "deltaGpof_NADH in component correction_factors (kilojoule_per_mole)"
    legend_constants[253] = "NH_H2O in component correction_factors (dimensionless)"
    legend_constants[254] = "deltaGof_H2O in component correction_factors (kilojoule_per_mole)"
    legend_algebraic[172] = "deltaGpof_H2O in component correction_factors (kilojoule_per_mole)"
    legend_constants[255] = "NH_H in component correction_factors (dimensionless)"
    legend_constants[256] = "deltaGof_H in component correction_factors (kilojoule_per_mole)"
    legend_algebraic[173] = "deltaGpof_H in component correction_factors (kilojoule_per_mole)"
    legend_algebraic[174] = "deltaH_CK in component correction_factors (dimensionless)"
    legend_constants[257] = "Kref_CK in component correction_factors (dimensionless)"
    legend_constants[258] = "deltaHo_CKo in component correction_factors (kilojoule_per_mole)"
    legend_constants[259] = "deltaH1_CK in component correction_factors (kilojoule_per_mole)"
    legend_constants[260] = "Kref_CKI in component correction_factors (dimensionless)"
    legend_constants[261] = "Kref_CKT in component correction_factors (dimensionless)"
    legend_constants[262] = "deltaGpo_CK in component correction_factors (kilojoule_per_mole)"
    legend_algebraic[176] = "Kapp_CK in component correction_factors (dimensionless)"
    legend_algebraic[178] = "deltaH_ADK in component correction_factors (dimensionless)"
    legend_algebraic[179] = "deltaGpo_ADK in component correction_factors (kilojoule_per_mole)"
    legend_algebraic[180] = "Kapp_ADK in component correction_factors (dimensionless)"
    legend_algebraic[181] = "deltaH_GP in component correction_factors (dimensionless)"
    legend_algebraic[182] = "deltaGpo_GP in component correction_factors (kilojoule_per_mole)"
    legend_algebraic[183] = "Kapp_GP in component correction_factors (dimensionless)"
    legend_algebraic[184] = "deltaH_PGLM in component correction_factors (dimensionless)"
    legend_algebraic[185] = "deltaGpo_PGLM in component correction_factors (kilojoule_per_mole)"
    legend_algebraic[186] = "Kapp_PGLM in component correction_factors (dimensionless)"
    legend_algebraic[187] = "deltaH_PGI in component correction_factors (dimensionless)"
    legend_algebraic[188] = "deltaGpo_PGI in component correction_factors (kilojoule_per_mole)"
    legend_algebraic[189] = "Kapp_PGI in component correction_factors (dimensionless)"
    legend_algebraic[190] = "deltaH_PFK in component correction_factors (dimensionless)"
    legend_algebraic[191] = "deltaGpo_PFK in component correction_factors (kilojoule_per_mole)"
    legend_algebraic[192] = "Kapp_PFK in component correction_factors (dimensionless)"
    legend_algebraic[193] = "deltaH_ALD in component correction_factors (dimensionless)"
    legend_algebraic[194] = "deltaGpo_ALD in component correction_factors (kilojoule_per_mole)"
    legend_algebraic[195] = "Kapp_ALD in component correction_factors (molar)"
    legend_algebraic[196] = "deltaH_TPI in component correction_factors (dimensionless)"
    legend_algebraic[197] = "deltaGpo_TPI in component correction_factors (kilojoule_per_mole)"
    legend_algebraic[198] = "Kapp_TPI in component correction_factors (dimensionless)"
    legend_algebraic[199] = "deltaH_GAPDH in component correction_factors (dimensionless)"
    legend_algebraic[200] = "deltaGpo_GAPDH in component correction_factors (kilojoule_per_mole)"
    legend_algebraic[201] = "Kapp_GAPDH in component correction_factors (per_molar)"
    legend_algebraic[202] = "deltaH_G3PDH in component correction_factors (dimensionless)"
    legend_algebraic[203] = "deltaGpo_G3PDH in component correction_factors (kilojoule_per_mole)"
    legend_algebraic[204] = "Kapp_G3PDH in component correction_factors (dimensionless)"
    legend_algebraic[205] = "deltaH_PGK in component correction_factors (dimensionless)"
    legend_algebraic[206] = "deltaGpo_PGK in component correction_factors (kilojoule_per_mole)"
    legend_algebraic[207] = "Kapp_PGK in component correction_factors (dimensionless)"
    legend_algebraic[208] = "deltaH_PGM in component correction_factors (dimensionless)"
    legend_algebraic[209] = "deltaGpo_PGM in component correction_factors (kilojoule_per_mole)"
    legend_algebraic[210] = "Kapp_PGM in component correction_factors (dimensionless)"
    legend_algebraic[211] = "deltaH_ENOL in component correction_factors (dimensionless)"
    legend_algebraic[212] = "deltaGpo_ENOL in component correction_factors (kilojoule_per_mole)"
    legend_algebraic[213] = "Kapp_ENOL in component correction_factors (dimensionless)"
    legend_algebraic[214] = "deltaH_PK in component correction_factors (dimensionless)"
    legend_algebraic[215] = "deltaGpo_PK in component correction_factors (kilojoule_per_mole)"
    legend_algebraic[216] = "Kapp_PK in component correction_factors (dimensionless)"
    legend_algebraic[217] = "deltaH_LDH in component correction_factors (dimensionless)"
    legend_algebraic[218] = "deltaGpo_LDH in component correction_factors (kilojoule_per_mole)"
    legend_algebraic[219] = "Kapp_LDH in component correction_factors (dimensionless)"
    legend_algebraic[30] = "deltaH_ATPase in component correction_factors (dimensionless)"
    legend_algebraic[175] = "deltaGpo_ATPase in component correction_factors (kilojoule_per_mole)"
    legend_algebraic[177] = "Kapp_ATPase in component correction_factors (dimensionless)"
    legend_states[1] = "Mg in component differential_equations (molar)"
    legend_constants[263] = "Vfgly in component glycogen_phosphorylase (molar_per_minute)"
    legend_constants[38] = "expno in component glycogen_phosphorylase (dimensionless)"
    legend_algebraic[220] = "fracA in component glycogen_phosphorylase (dimensionless)"
    legend_constants[39] = "KgpA_glyf in component glycogen_phosphorylase (molar)"
    legend_constants[264] = "KgpA_pi in component glycogen_phosphorylase (molar)"
    legend_constants[265] = "KgpA_igly in component glycogen_phosphorylase (molar)"
    legend_constants[40] = "KgpA_ipi in component glycogen_phosphorylase (molar)"
    legend_constants[266] = "KgpA_glyb in component glycogen_phosphorylase (molar)"
    legend_constants[41] = "KgpA_g1p in component glycogen_phosphorylase (molar)"
    legend_constants[267] = "KgpA_ig1p in component glycogen_phosphorylase (molar)"
    legend_algebraic[221] = "Dglya in component glycogen_phosphorylase (dimensionless)"
    legend_algebraic[222] = "pa in component glycogen_phosphorylase (dimensionless)"
    legend_algebraic[223] = "VbglyA in component glycogen_phosphorylase (molar_per_minute)"
    legend_algebraic[224] = "glyAF in component glycogen_phosphorylase (per_minute)"
    legend_algebraic[225] = "glyAR in component glycogen_phosphorylase (per_minute)"
    legend_algebraic[226] = "flux_GPa in component glycogen_phosphorylase (molar_per_minute)"
    legend_states[2] = "G1P in component differential_equations (molar)"
    legend_states[3] = "Pi in component differential_equations (molar)"
    legend_states[4] = "Gly in component differential_equations (molar)"
    legend_algebraic[227] = "fracB in component glycogen_phosphorylase_B (dimensionless)"
    legend_constants[268] = "KgpB_pi in component glycogen_phosphorylase_B (molar)"
    legend_constants[42] = "KgpB_ipi in component glycogen_phosphorylase_B (molar)"
    legend_constants[269] = "KgpB_iglyf in component glycogen_phosphorylase_B (molar)"
    legend_constants[270] = "KgpB_g1p in component glycogen_phosphorylase_B (molar)"
    legend_constants[43] = "KgpB_ig1p in component glycogen_phosphorylase_B (molar)"
    legend_constants[271] = "KgpB_iglyb in component glycogen_phosphorylase_B (molar)"
    legend_constants[44] = "Kgp_amp in component glycogen_phosphorylase_B (molar)"
    legend_constants[45] = "interactioncoeff in component glycogen_phosphorylase_B (dimensionless)"
    legend_constants[46] = "nH in component glycogen_phosphorylase_B (dimensionless)"
    legend_algebraic[228] = "M in component glycogen_phosphorylase_B (dimensionless)"
    legend_algebraic[229] = "Dglyb in component glycogen_phosphorylase_B (dimensionless)"
    legend_algebraic[230] = "pb in component glycogen_phosphorylase_B (dimensionless)"
    legend_algebraic[231] = "VbglyB in component glycogen_phosphorylase_B (molar_per_minute)"
    legend_algebraic[232] = "glyBF in component glycogen_phosphorylase_B (per_minute)"
    legend_algebraic[233] = "glyBR in component glycogen_phosphorylase_B (per_minute)"
    legend_algebraic[234] = "flux_GPb in component glycogen_phosphorylase_B (molar_per_minute)"
    legend_states[5] = "AMP in component differential_equations (molar)"
    legend_constants[272] = "Vffpglm in component PGLM (molar_per_minute)"
    legend_constants[273] = "Kpglm_g1p in component PGLM (molar)"
    legend_constants[274] = "Kpglm_g6p in component PGLM (molar)"
    legend_algebraic[235] = "Vfpglm in component PGLM (molar_per_minute)"
    legend_algebraic[237] = "Vbpglm in component PGLM (molar_per_minute)"
    legend_algebraic[238] = "v_PGLM in component PGLM (molar_per_minute)"
    legend_states[6] = "G6P in component differential_equations (molar)"
    legend_constants[275] = "Vbbpgi in component PGI (molar_per_minute)"
    legend_constants[276] = "Kpgi_g6p in component PGI (molar)"
    legend_constants[277] = "Kpgi_f6p in component PGI (molar)"
    legend_algebraic[239] = "Vbpgi in component PGI (molar_per_minute)"
    legend_algebraic[240] = "Vfpgi in component PGI (molar_per_minute)"
    legend_algebraic[241] = "v_PGI in component PGI (molar_per_minute)"
    legend_states[7] = "F6P in component differential_equations (molar)"
    legend_constants[278] = "Vffpfk in component PFK (molar_per_minute)"
    legend_constants[279] = "Kpfk_f6p in component PFK (molar)"
    legend_constants[280] = "Kpfk_f6pT in component PFK (molar)"
    legend_constants[281] = "Kpfk_atp in component PFK (molar)"
    legend_constants[283] = "Kpfk_atpT in component PFK (molar)"
    legend_constants[282] = "Kpfk_fbp in component PFK (molar)"
    legend_constants[47] = "Kpfk_fbpT in component PFK (molar)"
    legend_constants[284] = "Kpfk_adp in component PFK (molar)"
    legend_constants[48] = "Kpfk_adpT in component PFK (molar)"
    legend_constants[49] = "Kpfki in component PFK (molar)"
    legend_constants[50] = "Kmpfk in component PFK (molar)"
    legend_constants[51] = "d in component PFK (dimensionless)"
    legend_constants[52] = "e_ in component PFK (dimensionless)"
    legend_constants[53] = "Lo in component PFK (dimensionless)"
    legend_algebraic[242] = "Vfpfk in component PFK (molar_per_minute)"
    legend_algebraic[244] = "Vbpfk in component PFK (molar_per_minute)"
    legend_algebraic[245] = "L in component PFK (dimensionless)"
    legend_constants[285] = "alpha in component PFK (dimensionless)"
    legend_algebraic[246] = "Delta in component PFK (dimensionless)"
    legend_algebraic[247] = "Deltap in component PFK (dimensionless)"
    legend_algebraic[248] = "v_PFK in component PFK (molar_per_minute)"
    legend_states[8] = "FBP in component differential_equations (molar)"
    legend_states[9] = "ADP in component differential_equations (molar)"
    legend_states[10] = "ATP in component differential_equations (molar)"
    legend_constants[286] = "Vffald in component ALD (molar_per_minute)"
    legend_constants[287] = "Kald_fbp in component ALD (molar)"
    legend_constants[288] = "Kald_dhap in component ALD (molar)"
    legend_constants[289] = "Kald_gap in component ALD (molar)"
    legend_algebraic[249] = "Vfald in component ALD (molar_per_minute)"
    legend_algebraic[251] = "Vbald in component ALD (molar_per_minute)"
    legend_algebraic[252] = "v_ALD in component ALD (molar_per_minute)"
    legend_states[11] = "DHAP in component differential_equations (molar)"
    legend_states[12] = "GAP in component differential_equations (molar)"
    legend_constants[290] = "Vfftpi in component TPI (molar_per_minute)"
    legend_constants[291] = "Ktpi_gap in component TPI (molar)"
    legend_constants[292] = "Ktpi_dhap in component TPI (molar)"
    legend_constants[293] = "Vftpi in component TPI (molar_per_minute)"
    legend_algebraic[253] = "Vbtpi in component TPI (molar_per_minute)"
    legend_algebraic[254] = "v_TPI in component TPI (molar_per_minute)"
    legend_constants[294] = "Vbbg3pdh in component G3PDH (molar_per_minute)"
    legend_constants[295] = "Kg3pdh_g3p in component G3PDH (molar)"
    legend_constants[296] = "Kg3pdh_nad in component G3PDH (molar)"
    legend_constants[297] = "Kg3pdh_dhap in component G3PDH (molar)"
    legend_constants[298] = "Kg3pdh_nadh in component G3PDH (molar)"
    legend_algebraic[255] = "Dg3pdh in component G3PDH (dimensionless)"
    legend_constants[299] = "Vbg3pdh in component G3PDH (molar_per_minute)"
    legend_algebraic[256] = "Vfg3pdh in component G3PDH (molar_per_minute)"
    legend_algebraic[257] = "v_G3PDH in component G3PDH (molar_per_minute)"
    legend_states[13] = "G3P in component differential_equations (molar)"
    legend_states[14] = "NAD in component differential_equations (molar)"
    legend_states[15] = "NADH in component differential_equations (molar)"
    legend_constants[300] = "Vffgad in component GAPDH (molar_per_minute)"
    legend_constants[301] = "Kgapdh_gap in component GAPDH (molar)"
    legend_constants[302] = "Kgapdh_nad in component GAPDH (molar)"
    legend_constants[303] = "Kgapdh_pi in component GAPDH (molar)"
    legend_constants[304] = "Kgapdh_bpg in component GAPDH (molar)"
    legend_constants[305] = "Kgapdh_nadh in component GAPDH (molar)"
    legend_algebraic[258] = "Dgap in component GAPDH (dimensionless)"
    legend_algebraic[259] = "Vfgad in component GAPDH (molar_per_minute)"
    legend_algebraic[260] = "Vbgad in component GAPDH (molar_per_minute)"
    legend_algebraic[261] = "v_GAPDH in component GAPDH (molar_per_minute)"
    legend_states[16] = "BPG in component differential_equations (molar)"
    legend_constants[306] = "Vbbpgk in component PGK (molar_per_minute)"
    legend_constants[307] = "Kpgk_bpg in component PGK (molar)"
    legend_constants[308] = "Kpgk_adp in component PGK (molar)"
    legend_constants[309] = "Kpgk_3pg in component PGK (molar)"
    legend_constants[310] = "Kpgk_atp in component PGK (molar)"
    legend_constants[311] = "Vbpgk in component PGK (molar_per_minute)"
    legend_algebraic[262] = "Vfpgk in component PGK (molar_per_minute)"
    legend_algebraic[264] = "D_PGK in component PGK (dimensionless)"
    legend_algebraic[265] = "v_PGK in component PGK (molar_per_minute)"
    legend_states[17] = "P3G in component differential_equations (molar)"
    legend_constants[312] = "Vffpgm in component PGM (molar_per_minute)"
    legend_constants[313] = "Kpgm_3pg in component PGM (molar)"
    legend_constants[314] = "Kpgm_2pg in component PGM (molar)"
    legend_algebraic[266] = "Vfpgm in component PGM (molar_per_minute)"
    legend_algebraic[268] = "Vbpgm in component PGM (molar_per_minute)"
    legend_algebraic[269] = "v_PGM in component PGM (molar_per_minute)"
    legend_states[18] = "P2G in component differential_equations (molar)"
    legend_constants[315] = "Vffen in component ENOL (molar_per_minute)"
    legend_constants[316] = "Ken_2pg in component ENOL (molar)"
    legend_constants[317] = "Ken_pep in component ENOL (molar)"
    legend_constants[318] = "Vfen in component ENOL (molar_per_minute)"
    legend_algebraic[270] = "Vben in component ENOL (molar_per_minute)"
    legend_algebraic[272] = "v_ENOL in component ENOL (molar_per_minute)"
    legend_states[19] = "PEP in component differential_equations (molar)"
    legend_constants[319] = "Vffpk in component PK (molar_per_minute)"
    legend_constants[320] = "Kpk_pep in component PK (molar)"
    legend_constants[321] = "Kpk_adp in component PK (molar)"
    legend_constants[322] = "Kpk_pyr in component PK (molar)"
    legend_constants[323] = "Kpk_atp in component PK (molar)"
    legend_algebraic[273] = "Vfpk in component PK (molar_per_minute)"
    legend_algebraic[274] = "Vbpk in component PK (molar_per_minute)"
    legend_algebraic[275] = "v_PK in component PK (molar_per_minute)"
    legend_states[20] = "PYR in component differential_equations (molar)"
    legend_constants[324] = "Vffldh in component LDH (molar_per_minute)"
    legend_constants[325] = "Kldh_pyr in component LDH (molar)"
    legend_constants[326] = "Kldh_nadh in component LDH (molar)"
    legend_constants[327] = "Kldh_lac in component LDH (molar)"
    legend_constants[328] = "Kldh_nad in component LDH (molar)"
    legend_algebraic[276] = "Vfldh in component LDH (molar_per_minute)"
    legend_algebraic[277] = "Vbldh in component LDH (molar_per_minute)"
    legend_algebraic[278] = "v_LDH in component LDH (molar_per_minute)"
    legend_states[21] = "LAC in component differential_equations (molar)"
    legend_algebraic[279] = "VmaxATPase in component ATPase (molar_per_minute)"
    legend_constants[54] = "Katp_ATPase in component ATPase (molar)"
    legend_algebraic[284] = "ATPase in component ATPase (molar_per_minute)"
    legend_constants[329] = "VforCK in component creatine_kinase (molar_per_minute)"
    legend_constants[330] = "Kck_pcr in component creatine_kinase (molar)"
    legend_constants[331] = "Kck_iatp in component creatine_kinase (molar)"
    legend_constants[332] = "Kck_iadp in component creatine_kinase (molar)"
    legend_constants[55] = "Kck_ipcr in component creatine_kinase (molar)"
    legend_constants[333] = "Kck_cr in component creatine_kinase (molar)"
    legend_algebraic[285] = "VrevCK in component creatine_kinase (molar_per_minute)"
    legend_algebraic[286] = "CK in component creatine_kinase (molar_per_minute)"
    legend_states[22] = "Cr in component differential_equations (molar)"
    legend_states[23] = "PCr in component differential_equations (molar)"
    legend_constants[334] = "Vfadk in component adenylate_kinase (molar_per_minute)"
    legend_constants[335] = "Kadk_amp in component adenylate_kinase (molar)"
    legend_constants[336] = "Kadk_atp in component adenylate_kinase (molar)"
    legend_constants[337] = "Kadk_adp in component adenylate_kinase (molar)"
    legend_algebraic[287] = "Vbadk in component adenylate_kinase (molar_per_minute)"
    legend_algebraic[290] = "ADK in component adenylate_kinase (molar_per_minute)"
    legend_constants[338] = "carnosine in component buffer_capacity (molar)"
    legend_constants[339] = "tris in component buffer_capacity (molar)"
    legend_constants[340] = "acetate in component buffer_capacity (molar)"
    legend_algebraic[291] = "bufcapfixed in component buffer_capacity (molar)"
    legend_algebraic[292] = "bufcapmetab in component buffer_capacity (molar)"
    legend_algebraic[293] = "protons_consumed in component buffer_capacity (molar_per_minute)"
    legend_algebraic[288] = "CKprtflux in component buffer_capacity (molar_per_minute)"
    legend_algebraic[280] = "glycprtflux in component buffer_capacity (molar_per_minute)"
    legend_algebraic[294] = "pHODEterm1 in component buffer_capacity (per_minute)"
    legend_algebraic[295] = "pHODEterm2 in component buffer_capacity (per_molar)"
    legend_algebraic[296] = "denom_mgODE in component buffer_capacity (dimensionless)"
    legend_algebraic[297] = "RHSterm1_mgODE in component buffer_capacity (molar)"
    legend_algebraic[298] = "denomMgpHODE in component buffer_capacity (dimensionless)"
    legend_algebraic[311] = "RHSterm2_mgODE in component differential_equations (molar_per_minute)"
    legend_constants[33] = "fixmg in component differential_equations (dimensionless)"
    legend_constants[341] = "fixpH in component differential_equations (dimensionless)"
    legend_states[24] = "protonload in component differential_equations (molar)"
    legend_algebraic[300] = "dATPdt in component differential_equations (molar_per_minute)"
    legend_algebraic[301] = "dADPdt in component differential_equations (molar_per_minute)"
    legend_algebraic[302] = "dAMPdt in component differential_equations (molar_per_minute)"
    legend_algebraic[306] = "dDHAPdt in component differential_equations (molar_per_minute)"
    legend_algebraic[305] = "dFBPdt in component differential_equations (molar_per_minute)"
    legend_algebraic[304] = "dG1Pdt in component differential_equations (molar_per_minute)"
    legend_algebraic[307] = "dG3Pdt in component differential_equations (molar_per_minute)"
    legend_algebraic[310] = "dLACdt in component differential_equations (molar_per_minute)"
    legend_algebraic[308] = "dP2Gdt in component differential_equations (molar_per_minute)"
    legend_algebraic[299] = "dPCrdt in component differential_equations (molar_per_minute)"
    legend_algebraic[309] = "dPEPdt in component differential_equations (molar_per_minute)"
    legend_algebraic[303] = "dPidt in component differential_equations (molar_per_minute)"
    legend_algebraic[289] = "dCrdt in component differential_equations (molar_per_minute)"
    legend_algebraic[281] = "dNADdt in component differential_equations (molar_per_minute)"
    legend_algebraic[282] = "dNADHdt in component differential_equations (molar_per_minute)"
    legend_algebraic[236] = "dGlydt in component differential_equations (molar_per_minute)"
    legend_algebraic[243] = "dG6Pdt in component differential_equations (molar_per_minute)"
    legend_algebraic[250] = "dF6Pdt in component differential_equations (molar_per_minute)"
    legend_algebraic[263] = "dGAPdt in component differential_equations (molar_per_minute)"
    legend_algebraic[267] = "dBGPdt in component differential_equations (molar_per_minute)"
    legend_algebraic[271] = "dP3Gdt in component differential_equations (molar_per_minute)"
    legend_algebraic[283] = "dPYRdt in component differential_equations (molar_per_minute)"
    legend_rates[23] = "d/dt PCr in component differential_equations (molar)"
    legend_rates[22] = "d/dt Cr in component differential_equations (molar)"
    legend_rates[14] = "d/dt NAD in component differential_equations (molar)"
    legend_rates[15] = "d/dt NADH in component differential_equations (molar)"
    legend_rates[10] = "d/dt ATP in component differential_equations (molar)"
    legend_rates[9] = "d/dt ADP in component differential_equations (molar)"
    legend_rates[5] = "d/dt AMP in component differential_equations (molar)"
    legend_rates[3] = "d/dt Pi in component differential_equations (molar)"
    legend_rates[4] = "d/dt Gly in component differential_equations (molar)"
    legend_rates[2] = "d/dt G1P in component differential_equations (molar)"
    legend_rates[6] = "d/dt G6P in component differential_equations (molar)"
    legend_rates[7] = "d/dt F6P in component differential_equations (molar)"
    legend_rates[8] = "d/dt FBP in component differential_equations (molar)"
    legend_rates[11] = "d/dt DHAP in component differential_equations (molar)"
    legend_rates[13] = "d/dt G3P in component differential_equations (molar)"
    legend_rates[12] = "d/dt GAP in component differential_equations (molar)"
    legend_rates[16] = "d/dt BPG in component differential_equations (molar)"
    legend_rates[17] = "d/dt P3G in component differential_equations (molar)"
    legend_rates[18] = "d/dt P2G in component differential_equations (molar)"
    legend_rates[19] = "d/dt PEP in component differential_equations (molar)"
    legend_rates[20] = "d/dt PYR in component differential_equations (molar)"
    legend_rates[21] = "d/dt LAC in component differential_equations (molar)"
    legend_rates[1] = "d/dt Mg in component differential_equations (molar)"
    legend_rates[0] = "d/dt pH_calc in component differential_equations (dimensionless)"
    legend_rates[24] = "d/dt protonload in component differential_equations (molar)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 7.8
    constants[0] = 8.314e-3
    constants[1] = 298.15
    states[1] = 5.132658807e-4
    states[2] = 1e-9
    states[3] = 0.03
    states[4] = 0.04
    states[5] = 1e-9
    states[6] = 1e-9
    states[7] = 1e-9
    states[8] = 1e-9
    states[9] = 1e-9
    states[10] = 0.005
    states[11] = 1e-9
    states[12] = 1e-9
    states[13] = 1e-9
    states[14] = 0.0005
    states[15] = 1e-9
    states[16] = 1e-9
    states[17] = 1e-9
    states[18] = 1e-9
    states[19] = 1e-9
    states[20] = 1e-9
    states[21] = 1e-9
    states[22] = 0.029999999
    states[23] = 1e-9
    states[24] = 0
    constants[2] = 1.00000
    constants[3] = 7.40000
    constants[4] = 0.0500000
    constants[5] = 0.400000
    constants[6] = 0.00170000
    constants[7] = 0.00470000
    constants[8] = 0.00270000
    constants[9] = 0.00460000
    constants[10] = 0.00740000
    constants[11] = 0.00266055
    constants[12] = 0.0200000
    constants[13] = 1.75052
    constants[14] = 0.00402000
    constants[15] = 0.00270000
    constants[16] = 0.000870000
    constants[17] = 6.00000e-05
    constants[18] = 0.0100000
    constants[19] = 0.0100000
    constants[20] = 13.0000
    constants[21] = 0.00390000
    constants[22] = 0.00000
    constants[23] = 0.000100000
    constants[24] = 0.00500000
    constants[25] = 29.0000
    constants[26] = 0.00000
    constants[27] = 0.00000
    constants[28] = 0.00000
    constants[29] = 0.00000
    constants[30] = 0.00000
    constants[31] = 0.00000
    constants[32] = 0.00000
    constants[33] = 1.00000
    constants[34] = constants[2]
    constants[35] = constants[3]
    constants[36] = 0.00400000
    constants[37] = constants[24]
    constants[38] = constants[25]
    constants[39] = constants[6]
    constants[40] = constants[7]
    constants[41] = constants[8]
    constants[42] = constants[9]
    constants[43] = constants[10]
    constants[44] = constants[11]
    constants[45] = constants[12]
    constants[46] = constants[13]
    constants[47] = constants[14]
    constants[48] = constants[15]
    constants[49] = constants[16]
    constants[50] = constants[17]
    constants[51] = constants[18]
    constants[52] = constants[19]
    constants[53] = constants[20]
    constants[54] = constants[23]
    constants[55] = constants[21]
    constants[56] = 0.00200000/1.50000
    constants[57] = 0.000150000
    constants[58] = 0.0101000
    constants[59] = 0.000200000
    constants[60] = 0.0150000
    constants[61] = 0.00150000
    constants[62] = 0.00440000
    constants[63] = 0.480000
    constants[64] = 6.30000e-05
    constants[65] = 3.00000e-05
    constants[66] = 0.880000
    constants[67] = 0.000480000
    constants[68] = 0.000119000
    constants[69] = 0.0560000
    constants[70] = 0.000180000
    constants[71] = 0.0200000
    constants[72] = 8.00000e-05
    constants[73] = 0.000250000
    constants[74] = 0.00402000
    constants[75] = 0.00270000
    constants[76] = 0.0106591
    constants[77] = 5.00000e-05
    constants[78] = 0.00200000
    constants[79] = 0.00100000
    constants[80] = 12.0000
    constants[81] = 0.000320000
    constants[82] = 0.000610000
    constants[83] = 0.0825000
    constants[84] = 0.000180000
    constants[85] = 1.20000e-05
    constants[86] = 0.000220000
    constants[87] = 8.00000e-06
    constants[88] = 1.26500
    constants[89] = 2.50000e-06
    constants[90] = 9.00000e-05
    constants[91] = 0.000290000
    constants[92] = 8.00000e-07
    constants[93] = 3.30000e-06
    constants[94] = 1.12000
    constants[95] = 0.00200000
    constants[96] = 8.00000e-06
    constants[97] = 0.00120000
    constants[98] = 0.000350000
    constants[99] = 1.12000
    constants[100] = 0.000200000
    constants[101] = 1.40000e-05
    constants[102] = 0.192000
    constants[103] = 0.000100000
    constants[104] = 0.000370000
    constants[105] = 1.44000
    constants[106] = 8.00000e-05
    constants[107] = 0.000300000
    constants[108] = 0.00705000
    constants[109] = 0.00113000
    constants[110] = 1.92000
    constants[111] = 0.000335000
    constants[112] = 2.00000e-06
    constants[113] = 0.0170000
    constants[114] = 0.000849000
    constants[115] = 0.500000
    constants[116] = 0.00111000
    constants[117] = 0.00350000
    constants[118] = 0.000135000
    constants[119] = 0.00380000
    constants[120] = 0.880000
    constants[121] = 0.000320000
    constants[122] = 0.000270000
    constants[123] = 0.000350000
    constants[124] = 0.100000
    constants[125] = constants[124]
    constants[126] = 0.0150000
    constants[127] = 0.0250000
    constants[128] = 0.0100000
    constants[129] = 303.150
    constants[130] = constants[129]
    constants[131] = 0.0800000
    constants[132] = 1.00000
    constants[133] = constants[131]
    constants[134] = 1.00000
    constants[135] = 1.47750
    constants[136] = 1.60000
    constants[137] = (constants[135]*(power(constants[125], 1.0/2)))/(1.00000+constants[136]*(power(constants[125], 1.0/2)))
    constants[138] = 0.100000
    constants[139] = 1.17582
    constants[140] = (1.00000*constants[139]*((power(constants[138], 1.0/2))/(1.00000+constants[136]*(power(constants[138], 1.0/2)))-(power(constants[125], 1.0/2))/(1.00000+constants[136]*(power(constants[125], 1.0/2)))))/log(10.0000)
    constants[141] = (1.00000/constants[130]-1.00000/constants[1])/(log(10.0000)*constants[0])
    constants[142] = 2.91482
    constants[143] = (constants[142]*(power(constants[125], 1.0/2)))/(1.00000+constants[136]*(power(constants[125], 1.0/2)))
    constants[144] = 0.500000
    constants[145] = 3.00000
    constants[146] = -2.90000
    constants[147] = constants[145]+constants[137]*((power(2.00000, 2.00000)+power(1.00000, 2.00000))-power(1.00000, 2.00000))
    constants[148] = constants[146]+constants[137]*((power(2.00000, 2.00000)+power(2.00000, 2.00000))-power(0.00000, 2.00000))
    constants[149] = 6.75000+(constants[140]/1.00000)*((power(2.00000, 2.00000)+power(1.00000, 2.00000))-power(1.00000, 2.00000))+constants[141]*constants[147]
    constants[150] = 1.65000+(constants[140]/1.00000)*((power(2.00000, 2.00000)+power(1.00000, 2.00000))-power(1.00000, 2.00000))+constants[141]*constants[148]
    constants[151] = 1.00000
    constants[152] = -1096.10
    constants[153] = -5.00000
    constants[154] = -18.0000
    constants[155] = -1.00000
    constants[156] = constants[153]+constants[137]*((power(4.00000, 2.00000)+power(1.00000, 2.00000))-power(3.00000, 2.00000))
    constants[157] = constants[154]+constants[137]*((power(4.00000, 2.00000)+power(2.00000, 2.00000))-power(2.00000, 2.00000))
    constants[158] = constants[155]+constants[137]*((power(4.00000, 2.00000)+power(1.00000, 2.00000))-power(3.00000, 2.00000))
    constants[159] = 6.48000+(constants[140]/1.00000)*((power(4.00000, 2.00000)+power(1.00000, 2.00000))-power(3.00000, 2.00000))+constants[141]*constants[156]
    constants[160] = 4.19000+(constants[140]/1.00000)*((power(4.00000, 2.00000)+power(2.00000, 2.00000))-power(2.00000, 2.00000))+constants[141]*constants[157]
    constants[161] = 1.17000+(constants[140]/1.00000)*((power(4.00000, 2.00000)+power(1.00000, 2.00000))-power(3.00000, 2.00000))+constants[141]*constants[158]
    constants[162] = 12.0000
    constants[163] = -2768.10
    constants[164] = 1.00000
    constants[165] = -3.00000
    constants[166] = -15.0000
    constants[167] = constants[165]+constants[137]*((power(3.00000, 2.00000)+power(1.00000, 2.00000))-power(2.00000, 2.00000))
    constants[168] = constants[166]+constants[137]*((power(3.00000, 2.00000)+power(2.00000, 2.00000))-power(1.00000, 2.00000))
    constants[169] = 6.38000+(constants[140]/1.00000)*((power(3.00000, 2.00000)+power(1.00000, 2.00000))-power(2.00000, 2.00000))+constants[141]*constants[167]
    constants[170] = 3.25000+(constants[140]/1.00000)*((power(3.00000, 2.00000)+power(2.00000, 2.00000))-power(1.00000, 2.00000))+constants[141]*constants[168]
    constants[171] = 12.0000
    constants[172] = -1906.13
    constants[173] = -3.00000
    constants[174] = -7.50000
    constants[175] = constants[173]+constants[137]*((power(2.00000, 2.00000)+power(1.00000, 2.00000))-power(1.00000, 2.00000))
    constants[176] = constants[174]+constants[137]*((power(2.00000, 2.00000)+power(2.00000, 2.00000))-power(0.00000, 2.00000))
    constants[177] = 6.29000+(constants[140]/1.00000)*((power(2.00000, 2.00000)+power(1.00000, 2.00000))-power(1.00000, 2.00000))+constants[141]*constants[175]
    constants[178] = 1.92000+(constants[140]/1.00000)*((power(2.00000, 2.00000)+power(2.00000, 2.00000))-power(0.00000, 2.00000))+constants[141]*constants[176]
    constants[179] = 12.0000
    constants[180] = -1040.45
    constants[181] = 0.310000
    constants[182] = 2.66000
    constants[183] = 8.19000
    constants[184] = constants[182]+constants[137]*((power(2.00000, 2.00000)+power(1.00000, 2.00000))-power(1.00000, 2.00000))
    constants[185] = constants[183]+constants[137]*((power(2.00000, 2.00000)+power(2.00000, 2.00000))-power(0.00000, 2.00000))
    constants[186] = 4.50000+(constants[140]/1.00000)*((power(2.00000, 2.00000)+power(1.00000, 2.00000))-power(1.00000, 2.00000))+constants[141]*constants[184]
    constants[187] = 1.60000+(constants[140]/1.00000)*((power(2.00000, 2.00000)+power(2.00000, 2.00000))-power(0.00000, 2.00000))+constants[141]*constants[185]
    constants[188] = 8.00000
    constants[189] = 2.30000
    constants[190] = 9.00000
    constants[191] = -1.70000
    constants[192] = -12.0000
    constants[193] = constants[191]+constants[137]*((power(2.00000, 2.00000)+power(1.00000, 2.00000))-power(1.00000, 2.00000))
    constants[194] = constants[192]+constants[137]*((power(2.00000, 2.00000)+power(2.00000, 2.00000))-power(0.00000, 2.00000))
    constants[195] = 6.09000+(constants[140]/1.00000)*((power(2.00000, 2.00000)+power(1.00000, 2.00000))-power(1.00000, 2.00000))+constants[141]*constants[193]
    constants[196] = 2.48000+(constants[140]/1.00000)*((power(2.00000, 2.00000)+power(2.00000, 2.00000))-power(0.00000, 2.00000))+constants[141]*constants[194]
    constants[197] = 11.0000
    constants[198] = -1756.87
    constants[199] = 6.11000
    constants[200] = 11.0000
    constants[201] = -1763.94
    constants[202] = 5.89000
    constants[203] = 11.0000
    constants[204] = -1760.80
    constants[205] = 6.40000
    constants[206] = 5.92000
    constants[207] = 2.70000
    constants[208] = 10.0000
    constants[209] = -2601.40
    constants[210] = 6.45000
    constants[211] = 5.00000
    constants[212] = -1288.60
    constants[213] = 1.63000
    constants[214] = -3.10000
    constants[215] = constants[214]+constants[137]*((power(2.00000, 2.00000)+power(1.00000, 2.00000))-power(1.00000, 2.00000))
    constants[216] = 6.22000+(constants[140]/1.00000)*((power(2.00000, 2.00000)+power(1.00000, 2.00000))-power(1.00000, 2.00000))+constants[141]*constants[215]
    constants[217] = 7.00000
    constants[218] = -1339.25
    constants[219] = 5.90000
    constants[220] = 1.57000
    constants[221] = 5.00000
    constants[222] = -1296.26
    constants[223] = 7.50000
    constants[224] = 4.00000
    constants[225] = -2356.14
    constants[226] = 6.21000
    constants[227] = 4.00000
    constants[228] = -1502.54
    constants[229] = 7.00000
    constants[230] = 2.45000
    constants[231] = 1.18000
    constants[232] = 4.00000
    constants[233] = -1496.38
    constants[234] = 6.35000
    constants[235] = 2.26000
    constants[236] = 1.08000
    constants[237] = 2.00000
    constants[238] = -1263.65
    constants[239] = 2.49000
    constants[240] = 3.00000
    constants[241] = -472.270
    constants[242] = 0.980000
    constants[243] = -0.330000
    constants[244] = constants[243]+constants[137]*((power(1.00000, 2.00000)+power(1.00000, 2.00000))-power(0.00000, 2.00000))
    constants[245] = 3.67000+(constants[140]/1.00000)*((power(1.00000, 2.00000)+power(1.00000, 2.00000))-power(0.00000, 2.00000))+constants[141]*constants[244]
    constants[246] = 5.00000
    constants[247] = -516.720
    constants[248] = -10.0000
    constants[249] = 26.0000
    constants[250] = 0.00000
    constants[251] = 27.0000
    constants[252] = 22.6500
    constants[253] = 2.00000
    constants[254] = -237.190
    constants[255] = 1.00000
    constants[256] = 0.00000
    constants[257] = 2.58000e+08
    constants[258] = -17.5500
    constants[259] = constants[258]+constants[137]*(((power(2.00000, 2.00000)+power(3.00000, 2.00000)+power(1.00000, 2.00000))-power(4.00000, 2.00000))-power(0.00000, 2.00000))
    constants[260] = exp(log(constants[257])+(constants[139]*(power(constants[125], 1.0/2))*(((power(2.00000, 2.00000)+power(3.00000, 2.00000)+power(1.00000, 2.00000))-power(4.00000, 2.00000))-power(0.00000, 2.00000)))/(1.00000+constants[136]*(power(constants[125], 1.0/2))))
    constants[261] = power(10.0000, log(constants[260], 10)-constants[141]*constants[259])
    constants[262] = -constants[0]*constants[130]*log(constants[261])
    constants[263] = constants[4]
    constants[264] = constants[36]
    constants[265] = constants[56]
    constants[266] = constants[57]
    constants[267] = constants[58]
    constants[268] = constants[59]
    constants[269] = constants[60]
    constants[270] = constants[61]
    constants[271] = constants[62]
    constants[272] = constants[63]
    constants[273] = constants[64]
    constants[274] = constants[65]
    constants[275] = constants[66]
    constants[276] = constants[67]
    constants[277] = constants[68]
    constants[278] = constants[69]
    constants[279] = constants[70]
    constants[280] = constants[71]
    constants[281] = constants[72]
    constants[282] = constants[74]
    constants[283] = constants[73]
    constants[284] = constants[75]
    constants[285] = (constants[279]*constants[281])/(constants[280]*constants[283])
    constants[286] = constants[76]
    constants[287] = constants[77]
    constants[288] = constants[78]
    constants[289] = constants[79]
    constants[290] = constants[80]
    constants[291] = constants[81]
    constants[292] = constants[82]
    constants[293] = constants[290]
    constants[294] = constants[83]
    constants[295] = constants[84]
    constants[296] = constants[85]
    constants[297] = constants[86]
    constants[298] = constants[87]
    constants[299] = constants[294]
    constants[300] = constants[88]
    constants[301] = constants[89]
    constants[302] = constants[90]
    constants[303] = constants[91]
    constants[304] = constants[92]
    constants[305] = constants[93]
    constants[306] = constants[94]
    constants[307] = constants[95]
    constants[308] = constants[96]
    constants[309] = constants[97]
    constants[310] = constants[98]
    constants[311] = constants[306]
    constants[312] = constants[99]
    constants[313] = constants[100]
    constants[314] = constants[101]
    constants[315] = constants[102]
    constants[316] = constants[103]
    constants[317] = constants[104]
    constants[318] = constants[315]
    constants[319] = constants[105]
    constants[320] = constants[106]
    constants[321] = constants[107]
    constants[322] = constants[108]
    constants[323] = constants[109]
    constants[324] = constants[110]
    constants[325] = constants[111]
    constants[326] = constants[112]
    constants[327] = constants[113]
    constants[328] = constants[114]
    constants[329] = constants[115]
    constants[330] = constants[116]
    constants[331] = constants[117]
    constants[332] = constants[118]
    constants[333] = constants[119]
    constants[334] = constants[120]
    constants[335] = constants[121]
    constants[336] = constants[122]
    constants[337] = constants[123]
    constants[338] = constants[127]
    constants[339] = constants[126]
    constants[340] = constants[128]
    constants[341] = constants[132]
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[220] = custom_piecewise([constants[38] != 45.0000, constants[5] , less(voi , 40.0000), 0.00100000 , greater_equal(voi , 40.0000) & less(voi , 80.0000), 0.00400000 , greater_equal(voi , 80.0000) & less(voi , 100.000), 0.0100000 , greater_equal(voi , 100.000), 0.0400000 , True, float('nan')])
    algebraic[221] = 1.00000+states[4]/constants[39]+states[3]/constants[264]+(states[4]*states[3])/(constants[39]*constants[40])+states[4]/constants[266]+states[2]/constants[41]+(states[4]*states[2])/(constants[267]*constants[266])
    algebraic[0] = custom_piecewise([less_equal(voi , 1.00000) | greater(voi , 1.00000) & equal(constants[34] , 0.00000), states[0] , True, constants[35]])
    algebraic[222] = 1.40400/(1.00000+power(10.0000, 5.94000-algebraic[0])+power(10.0000, algebraic[0]-7.29000))
    algebraic[224] = ((algebraic[222]*constants[263]*states[3])/(constants[265]*constants[264]))/algebraic[221]
    algebraic[1] = 1.00000+power(10.0000, -algebraic[0]+constants[149])+(states[1]/constants[134])*(power(10.0000, constants[150]))+(constants[133]/constants[134])*(power(10.0000, constants[144]))
    algebraic[60] = 1.00000+(power(10.0000, -algebraic[0]))*(power(10.0000, constants[195]))+(states[1]/constants[134])*(power(10.0000, constants[196]))
    algebraic[11] = (constants[152]+constants[151]*log(10.0000)*constants[0]*constants[130]*algebraic[0])-constants[143]*(4.00000-constants[151])
    algebraic[69] = (constants[198]+constants[197]*log(10.0000)*constants[0]*constants[130]*algebraic[0])-constants[143]*(4.00000-constants[197])
    algebraic[169] = 655.700+constants[248]*log(10.0000)*constants[0]*constants[130]*algebraic[0]
    algebraic[182] = (algebraic[169]+algebraic[69])-algebraic[11]
    algebraic[183] = (exp(-algebraic[182]/(constants[0]*constants[130]))*algebraic[60])/algebraic[1]
    algebraic[223] = (algebraic[222]*constants[263]*constants[266]*constants[267])/(constants[265]*constants[264]*algebraic[183])
    algebraic[225] = ((algebraic[223]*states[4])/(constants[266]*constants[267]))/algebraic[221]
    algebraic[226] = algebraic[220]*(states[4]*algebraic[224]-states[2]*algebraic[225])
    algebraic[227] = 1.00000-algebraic[220]
    algebraic[228] = ((power(states[5]/constants[44], constants[46]))/constants[45])/(1.00000+(power(states[5]/constants[44], constants[46]))/constants[45])
    algebraic[229] = 1.00000+states[4]/constants[269]+states[3]/constants[42]+states[4]/constants[271]+states[2]/constants[43]+(states[4]*states[3])/(constants[269]*constants[268])+(states[4]*states[2])/(constants[270]*constants[271])
    algebraic[230] = 1.75000/(1.00000+power(10.0000, 6.12000-algebraic[0])+power(10.0000, algebraic[0]-7.03000))
    algebraic[232] = ((algebraic[230]*algebraic[228]*constants[263]*states[3])/(constants[269]*constants[268]))/algebraic[229]
    algebraic[231] = (algebraic[230]*constants[263]*constants[270]*constants[271])/(constants[269]*constants[268]*algebraic[183])
    algebraic[233] = ((algebraic[228]*algebraic[231]*states[4])/(constants[270]*constants[271]))/algebraic[229]
    algebraic[234] = algebraic[227]*(states[4]*algebraic[232]-states[2]*algebraic[233])
    algebraic[236] = -(algebraic[226]+algebraic[234])
    rates[4] = algebraic[236]
    algebraic[235] = (constants[272]*1.32900)/(1.00000+power(10.0000, -algebraic[0]+6.64000)+power(10.0000, algebraic[0]-8.36000))
    algebraic[70] = 1.00000+power(10.0000, -algebraic[0]+constants[199])
    algebraic[75] = (constants[201]+constants[200]*log(10.0000)*constants[0]*constants[130]*algebraic[0])-constants[143]*(4.00000-constants[200])
    algebraic[185] = algebraic[75]-algebraic[69]
    algebraic[186] = (exp(-algebraic[185]/(constants[0]*constants[130]))*algebraic[70])/algebraic[60]
    algebraic[237] = (algebraic[235]*constants[274])/(constants[273]*algebraic[186])
    algebraic[238] = ((algebraic[235]*states[2])/constants[273]-(algebraic[237]*states[6])/constants[274])/(1.00000+states[2]/constants[273]+states[6]/constants[274])
    algebraic[239] = constants[275]/(1.00000+power(10.0000, -algebraic[0]+6.94000)+power(10.0000, algebraic[0]-9.35000))
    algebraic[76] = 1.00000+power(10.0000, -algebraic[0]+constants[202])
    algebraic[81] = (constants[204]+constants[203]*log(10.0000)*constants[0]*constants[130]*algebraic[0])-constants[143]*(4.00000-constants[203])
    algebraic[188] = algebraic[81]-algebraic[75]
    algebraic[189] = (exp(-algebraic[188]/(constants[0]*constants[130]))*algebraic[76])/algebraic[70]
    algebraic[240] = ((algebraic[239]*constants[276])/constants[277])*algebraic[189]
    algebraic[241] = ((algebraic[240]*states[6])/constants[276]-(algebraic[239]*states[7])/constants[277])/(1.00000+states[7]/constants[277]+states[6]/constants[276])
    algebraic[243] = algebraic[238]-algebraic[241]
    rates[6] = algebraic[243]
    algebraic[242] = constants[278]/(1.00000+power(algebraic[0]/6.80000, -30.0000))
    algebraic[12] = 1.00000+power(10.0000, -algebraic[0]+constants[159])+(states[1]/constants[134])*(power(10.0000, constants[160]))+(constants[133]/constants[134])*(power(10.0000, constants[161]))
    algebraic[23] = 1.00000+power(10.0000, -algebraic[0]+constants[169])+(states[1]/constants[134])*(power(10.0000, constants[170]))+(constants[133]/constants[134])*(power(10.0000, constants[164]))
    algebraic[82] = 1.00000+power(10.0000, -algebraic[0]+constants[205])+power(10.0000, -2.00000*algebraic[0]+constants[205]+constants[206])+(states[1]/constants[134])*(power(10.0000, constants[207]))
    algebraic[22] = (constants[163]+constants[162]*constants[0]*constants[130]*log(10.0000)*algebraic[0])-constants[143]*(16.0000-constants[162])
    algebraic[34] = (constants[172]+constants[171]*constants[0]*constants[130]*log(10.0000)*algebraic[0])-constants[143]*(9.00000-constants[171])
    algebraic[92] = (constants[209]+constants[208]*log(10.0000)*constants[0]*constants[130]*algebraic[0])-constants[143]*(16.0000-constants[208])
    algebraic[173] = constants[256]+constants[255]*log(10.0000)*constants[0]*constants[130]*algebraic[0]
    algebraic[191] = ((algebraic[92]+algebraic[34]+algebraic[173])-algebraic[81])-algebraic[22]
    algebraic[192] = (exp(-algebraic[191]/(constants[0]*constants[130]))*algebraic[82]*algebraic[23])/(algebraic[76]*algebraic[12]*(power(10.0000, -algebraic[0])))
    algebraic[244] = (algebraic[242]*constants[282]*constants[284])/(constants[279]*constants[281]*algebraic[192])
    algebraic[245] = constants[53]*(power((((1.00000+states[10]/constants[49])/(1.00000+(constants[51]*states[10])/constants[49]))*(1.00000+(constants[52]*states[5])/constants[50]))/(1.00000+states[5]/constants[50]), 4.00000))
    algebraic[246] = (1.00000+states[7]/constants[279])*(1.00000+states[10]/constants[281])+states[8]/constants[282]+(states[9]/constants[284])*(1.00000+states[8]/constants[282])
    algebraic[247] = (1.00000+states[7]/constants[280])*(1.00000+states[10]/constants[283])+states[8]/constants[47]+(states[9]/constants[48])*(1.00000+states[8]/constants[47])
    algebraic[248] = ((((algebraic[242]*states[7]*states[10])/(constants[279]*constants[281]))/algebraic[246]-((algebraic[244]*states[9]*states[8])/(constants[284]*constants[282]))/algebraic[246])*(1.00000+constants[285]*algebraic[245]*(power(algebraic[247]/algebraic[246], 3.00000))))/(1.00000+algebraic[245]*(power(algebraic[247]/algebraic[246], 4.00000)))
    algebraic[250] = algebraic[241]-algebraic[248]
    rates[7] = algebraic[250]
    algebraic[249] = (constants[286]*1.01300)/(1.00000+power(10.0000, -algebraic[0]+5.32000)+power(10.0000, algebraic[0]-9.15000))
    algebraic[93] = 1.00000+power(10.0000, -algebraic[0]+constants[210])
    algebraic[109] = 1.00000+power(10.0000, -algebraic[0]+constants[219])+(states[1]/constants[134])*(power(10.0000, constants[220]))
    algebraic[98] = (constants[212]+constants[211]*log(10.0000)*constants[0]*constants[130]*algebraic[0])-constants[143]*(4.00000-constants[211])
    algebraic[118] = (constants[222]+constants[221]*log(10.0000)*constants[0]*constants[130]*algebraic[0])-constants[143]*(4.00000-constants[221])
    algebraic[194] = (algebraic[118]+algebraic[98])-algebraic[92]
    algebraic[195] = (1.00000*exp(-algebraic[194]/(constants[0]*constants[130]))*algebraic[93]*algebraic[82])/algebraic[109]
    algebraic[251] = (algebraic[249]*constants[289]*constants[288])/(constants[287]*algebraic[195])
    algebraic[252] = ((algebraic[249]*states[8])/constants[287]-(algebraic[251]*states[12]*states[11])/(constants[289]*constants[288]))/(1.00000+states[8]/constants[287]+states[12]/constants[289]+states[11]/constants[288])
    algebraic[197] = algebraic[118]-algebraic[98]
    algebraic[198] = (exp(-algebraic[197]/(constants[0]*constants[130]))*algebraic[109])/algebraic[93]
    algebraic[253] = (constants[293]*constants[292])/(constants[291]*algebraic[198])
    algebraic[254] = ((constants[293]*states[12])/constants[291]-(algebraic[253]*states[11])/constants[292])/(1.00000+states[12]/constants[291]+states[11]/constants[292])
    algebraic[258] = 1.00000+states[3]/constants[303]+states[12]/constants[301]+states[14]/constants[302]+(states[12]*states[14])/(constants[301]*constants[302])+(states[12]*states[14]*states[3])/(constants[301]*constants[302]*constants[303])+states[16]/constants[304]+states[15]/constants[305]+(states[16]*states[15])/(constants[305]*constants[304])
    algebraic[259] = constants[300]*0.000700000*exp(algebraic[0]*0.897900)
    algebraic[119] = 1.00000+power(10.0000, -algebraic[0]+constants[223])
    algebraic[124] = (constants[225]+constants[224]*log(10.0000)*constants[0]*constants[130]*algebraic[0])-constants[143]*(16.0000-constants[224])
    algebraic[170] = (constants[250]+constants[249]*log(10.0000)*constants[0]*constants[130]*algebraic[0])-constants[143]*(1.00000-constants[249])
    algebraic[171] = (constants[252]+constants[251]*log(10.0000)*constants[0]*constants[130]*algebraic[0])-constants[143]*(4.00000-constants[251])
    algebraic[200] = (((algebraic[124]+algebraic[171]+algebraic[173])-algebraic[11])-algebraic[98])-algebraic[170]
    algebraic[201] = (exp(-algebraic[200]/(constants[0]*constants[130]))*algebraic[119])/(algebraic[1]*algebraic[93]*(power(10.0000, -algebraic[0]))*1.00000)
    algebraic[260] = (algebraic[259]*constants[304]*constants[305])/(constants[301]*constants[303]*constants[302]*algebraic[201])
    algebraic[261] = ((algebraic[259]*states[12]*states[14]*states[3])/(constants[302]*constants[301]*constants[303])-(algebraic[260]*states[16]*states[15])/(constants[304]*constants[305]))/algebraic[258]
    algebraic[263] = (algebraic[252]-algebraic[254])-algebraic[261]
    rates[12] = algebraic[263]
    algebraic[125] = 1.00000+power(10.0000, -algebraic[0]+6.21000)
    algebraic[130] = (constants[228]+constants[227]*log(10.0000)*constants[0]*constants[130]*algebraic[0])-constants[143]*(9.00000-constants[227])
    algebraic[206] = ((algebraic[22]+algebraic[130])-algebraic[124])-algebraic[34]
    algebraic[207] = (exp(-algebraic[206]/(constants[0]*constants[130]))*algebraic[12]*algebraic[125])/(algebraic[119]*algebraic[23])
    algebraic[262] = ((constants[311]*constants[307]*constants[308])/(constants[309]*constants[310]))*algebraic[207]
    algebraic[264] = 1.00000+states[9]/constants[308]+states[16]/constants[307]+(states[16]*states[9])/(constants[307]*constants[308])+states[17]/constants[309]+states[10]/constants[310]+(states[17]*states[10])/(constants[309]*constants[310])
    algebraic[265] = ((algebraic[262]*states[16]*states[9])/(constants[308]*constants[307])-(constants[311]*states[10]*states[17])/(constants[310]*constants[309]))/algebraic[264]
    algebraic[267] = algebraic[261]-algebraic[265]
    rates[16] = algebraic[267]
    algebraic[266] = (constants[312]*0.989000)/(1.00000+power(10.0000, -algebraic[0]+5.62000)+power(10.0000, algebraic[0]-8.74000))
    algebraic[131] = 1.00000+power(10.0000, -algebraic[0]+constants[229])+(states[1]/constants[134])*(power(10.0000, constants[230]))+(constants[133]/constants[134])*(power(10.0000, constants[231]))
    algebraic[141] = (constants[233]+constants[232]*log(10.0000)*constants[0]*constants[130]*algebraic[0])-constants[143]*(9.00000-constants[232])
    algebraic[209] = algebraic[141]-algebraic[130]
    algebraic[210] = (exp(-algebraic[209]/(constants[0]*constants[130]))*algebraic[131])/algebraic[125]
    algebraic[268] = (algebraic[266]*constants[314])/(constants[313]*algebraic[210])
    algebraic[269] = ((algebraic[266]*states[17])/constants[313]-(algebraic[268]*states[18])/constants[314])/(1.00000+states[17]/constants[313]+states[18]/constants[314])
    algebraic[271] = algebraic[265]-algebraic[269]
    rates[17] = algebraic[271]
    algebraic[255] = (1.00000+states[13]/constants[295]+states[15]/constants[298])*(1.00000+states[11]/constants[297]+states[14]/constants[298])
    algebraic[99] = 1.00000+power(10.0000, -algebraic[0]+constants[216])+(states[1]/constants[134])*(power(10.0000, constants[213]))
    algebraic[108] = (constants[218]+constants[217]*log(10.0000)*constants[0]*constants[130]*algebraic[0])-constants[143]*(4.00000-constants[217])
    algebraic[203] = ((algebraic[173]+algebraic[171]+algebraic[118])-algebraic[170])-algebraic[108]
    algebraic[204] = (exp(-algebraic[203]/(constants[0]*constants[130]))*algebraic[109])/(algebraic[99]*(power(10.0000, -algebraic[0])))
    algebraic[256] = (constants[299]*constants[295]*constants[296]*algebraic[204])/(constants[297]*constants[298])
    algebraic[257] = ((algebraic[256]*states[13]*states[14])/(constants[295]*constants[296])-(constants[299]*states[11]*states[15])/(constants[297]*constants[298]))/algebraic[255]
    algebraic[276] = constants[324]*(-0.113400*algebraic[0]+1.60690)
    algebraic[153] = 1.00000+power(10.0000, -algebraic[0]+constants[239])
    algebraic[159] = 1.00000+power(10.0000, -algebraic[0]+constants[245])+(states[1]/constants[134])*(power(10.0000, constants[242]))
    algebraic[158] = (constants[241]+constants[240]*log(10.0000)*constants[0]*constants[130]*algebraic[0])-constants[143]*(1.00000-constants[240])
    algebraic[168] = (constants[247]+constants[246]*log(10.0000)*constants[0]*constants[130]*algebraic[0])-constants[143]*(1.00000-constants[246])
    algebraic[218] = (((algebraic[168]+algebraic[170])-algebraic[158])-algebraic[171])-algebraic[173]
    algebraic[219] = (exp(-algebraic[218]/(constants[0]*constants[130]))*algebraic[159]*(power(10.0000, -algebraic[0])))/algebraic[153]
    algebraic[277] = (algebraic[276]*constants[327]*constants[328])/(constants[325]*constants[326]*algebraic[219])
    algebraic[278] = ((algebraic[276]*states[20]*states[15])/(constants[325]*constants[326])-(algebraic[277]*states[21]*states[14])/(constants[327]*constants[328]))/(1.00000+states[20]/constants[325]+states[15]/constants[326]+(states[20]*states[15])/(constants[325]*constants[326])+states[21]/constants[327]+states[14]/constants[328]+(states[21]*states[14])/(constants[327]*constants[328]))
    algebraic[281] = (-algebraic[261]-algebraic[257])+algebraic[278]
    rates[14] = algebraic[281]
    algebraic[282] = (algebraic[261]+algebraic[257])-algebraic[278]
    rates[15] = algebraic[282]
    algebraic[273] = (constants[319]*1.05000)/(1.00000+power(10.0000, -algebraic[0]+5.58000)+power(10.0000, algebraic[0]-8.79000))
    algebraic[142] = 1.00000+power(10.0000, constants[234]-algebraic[0])+(states[1]/constants[134])*(power(10.0000, constants[235]))+(constants[133]/constants[134])*(power(10.0000, constants[236]))
    algebraic[152] = (constants[238]+constants[237]*log(10.0000)*constants[0]*constants[130]*algebraic[0])-constants[143]*(9.00000-constants[237])
    algebraic[215] = (((algebraic[158]+algebraic[22])-algebraic[173])-algebraic[152])-algebraic[34]
    algebraic[216] = (exp(-algebraic[215]/(constants[0]*constants[130]))*algebraic[153]*algebraic[12]*(power(10.0000, -algebraic[0])))/(algebraic[142]*algebraic[23])
    algebraic[274] = (algebraic[273]*constants[322]*constants[323])/(constants[320]*constants[321]*algebraic[216])
    algebraic[275] = ((algebraic[273]*states[19]*states[9])/(constants[320]*constants[321])-(algebraic[274]*states[20]*states[10])/(constants[322]*constants[323]))/(1.00000+states[19]/constants[320]+states[9]/constants[321]+(states[19]*states[9])/(constants[320]*constants[321])+states[10]/constants[323]+states[20]/constants[322]+(states[20]*states[10])/(constants[322]*constants[323]))
    algebraic[283] = algebraic[275]-algebraic[278]
    rates[20] = algebraic[283]
    algebraic[45] = 1.00000+power(10.0000, -algebraic[0]+constants[186])+(states[1]/constants[134])*(power(10.0000, constants[187]))+(constants[133]/constants[134])*(power(10.0000, constants[181]))
    algebraic[55] = 1.00000+power(10.0000, -algebraic[0]+constants[189])
    algebraic[176] = (exp(-constants[262]/(constants[0]*constants[130]))*(power(10.0000, -algebraic[0]))*algebraic[12]*algebraic[55])/(algebraic[45]*algebraic[23])
    algebraic[285] = ((constants[329]/algebraic[176])*constants[331]*constants[333])/(constants[332]*constants[330])
    algebraic[286] = ((algebraic[285]*states[10]*states[22])/(constants[331]*constants[333])-(constants[329]*states[9]*states[23])/(constants[332]*constants[330]))/(1.00000+states[9]/constants[332]+states[23]/constants[55]+(states[23]*states[9])/(constants[332]*constants[330])+states[10]/constants[331]+(states[22]*states[10])/(constants[333]*constants[331]))
    algebraic[289] = -algebraic[286]
    rates[22] = algebraic[289]
    algebraic[13] = 1.00000/algebraic[12]
    algebraic[14] = (power(10.0000, -algebraic[0]+constants[159]))*algebraic[13]
    algebraic[15] = (states[1]/constants[134])*(power(10.0000, constants[160]))*algebraic[13]
    algebraic[16] = (constants[133]/constants[134])*(power(10.0000, constants[161]))*algebraic[13]
    algebraic[17] = 0.00000*algebraic[13]+1.00000*algebraic[14]+0.00000*algebraic[15]+0.00000*algebraic[16]
    algebraic[24] = 1.00000/algebraic[23]
    algebraic[25] = (power(10.0000, -algebraic[0]+constants[169]))*algebraic[24]
    algebraic[26] = ((algebraic[24]*states[1])/constants[134])*(power(10.0000, constants[170]))
    algebraic[27] = ((algebraic[24]*constants[133])/constants[134])*(power(10.0000, constants[164]))
    algebraic[28] = 0.00000*algebraic[24]+1.00000*algebraic[25]+0.00000*algebraic[26]+0.00000*algebraic[27]
    algebraic[46] = 1.00000/algebraic[45]
    algebraic[48] = (power(10.0000, -algebraic[0]+constants[186]))*algebraic[46]
    algebraic[50] = algebraic[48]
    algebraic[56] = 1.00000/algebraic[55]
    algebraic[57] = algebraic[56]*(power(10.0000, -algebraic[0]+constants[189]))
    algebraic[58] = 0.00000*algebraic[56]+1.00000*algebraic[57]
    algebraic[174] = (((algebraic[17]+algebraic[58])-algebraic[50])-algebraic[28])+(((constants[162]+constants[190])-constants[188])-constants[171])
    algebraic[35] = 1.00000+power(10.0000, constants[177]-algebraic[0])+(states[1]/constants[134])*(power(10.0000, constants[178]))
    algebraic[36] = 1.00000/algebraic[35]
    algebraic[37] = algebraic[36]*(power(10.0000, constants[177]-algebraic[0]))
    algebraic[38] = (states[1]/constants[134])*(power(10.0000, constants[178]))*algebraic[36]
    algebraic[39] = 0.00000*algebraic[36]+algebraic[37]+0.00000*algebraic[38]
    algebraic[178] = ((2.00000*algebraic[28]-algebraic[17])-algebraic[39])+((2.00000*constants[171]-constants[162])-constants[179])
    algebraic[2] = 1.00000/algebraic[1]
    algebraic[3] = (power(10.0000, -algebraic[0]+constants[149]))*algebraic[2]
    algebraic[6] = 1.00000*algebraic[3]
    algebraic[61] = 1.00000/algebraic[60]
    algebraic[62] = algebraic[61]*(power(10.0000, -algebraic[0]+constants[195]))
    algebraic[64] = algebraic[62]
    algebraic[181] = (algebraic[64]-algebraic[6])+(1.00000-constants[151])
    algebraic[71] = 1.00000/algebraic[70]
    algebraic[72] = algebraic[71]*(power(10.0000, -algebraic[0]+constants[199]))
    algebraic[73] = algebraic[72]
    algebraic[184] = (algebraic[73]-algebraic[64])+(constants[200]-constants[197])
    algebraic[77] = 1.00000/algebraic[76]
    algebraic[78] = algebraic[77]*(power(10.0000, -algebraic[0]+constants[202]))
    algebraic[79] = algebraic[78]
    algebraic[187] = (algebraic[79]-algebraic[73])+(constants[203]-constants[200])
    algebraic[83] = 1.00000/algebraic[82]
    algebraic[84] = algebraic[83]*(power(10.0000, -algebraic[0]+constants[205]))
    algebraic[85] = algebraic[83]*(power(10.0000, -2.00000*algebraic[0]+constants[205]+constants[206]))
    algebraic[87] = algebraic[84]+2.00000*algebraic[85]
    algebraic[190] = (((((algebraic[28]+algebraic[87])-algebraic[79])-algebraic[17])+constants[171]+constants[208])-constants[203])-constants[162]
    algebraic[94] = 1.00000/algebraic[93]
    algebraic[95] = algebraic[94]*(power(10.0000, -algebraic[0]+constants[210]))
    algebraic[96] = algebraic[95]
    algebraic[110] = 1.00000/algebraic[109]
    algebraic[111] = algebraic[110]*(power(10.0000, -algebraic[0]+constants[219]))
    algebraic[113] = algebraic[111]
    algebraic[193] = ((algebraic[113]+algebraic[96])-algebraic[87])+((constants[221]+constants[211])-constants[208])
    algebraic[196] = (algebraic[113]-algebraic[96])+(constants[221]-constants[211])
    algebraic[120] = 1.00000/algebraic[119]
    algebraic[121] = algebraic[120]*(power(10.0000, -algebraic[0]+constants[223]))
    algebraic[122] = algebraic[121]
    algebraic[199] = ((algebraic[122]-algebraic[96])-algebraic[6])+((((constants[224]+constants[251])-constants[211])-constants[151])-constants[249])
    algebraic[100] = 1.00000/algebraic[99]
    algebraic[101] = algebraic[100]*(power(10.0000, -algebraic[0]+constants[216]))
    algebraic[103] = algebraic[101]
    algebraic[202] = (algebraic[113]-algebraic[103])+(((constants[221]+constants[251])-constants[249])-constants[217])
    algebraic[126] = 1.00000/algebraic[125]
    algebraic[127] = algebraic[126]*(power(10.0000, -algebraic[0]+6.21000))
    algebraic[128] = algebraic[127]
    algebraic[205] = (((algebraic[128]+algebraic[17])-algebraic[122])-algebraic[28])+(((constants[227]+constants[162])-constants[224])-constants[171])
    algebraic[132] = 1.00000/algebraic[131]
    algebraic[133] = algebraic[132]*(power(10.0000, -algebraic[0]+constants[229]))
    algebraic[136] = algebraic[133]
    algebraic[208] = (algebraic[136]-algebraic[128])+(constants[232]-constants[227])
    algebraic[143] = 1.00000/algebraic[142]
    algebraic[144] = algebraic[143]*(power(10.0000, constants[234]-algebraic[0]))
    algebraic[147] = algebraic[144]
    algebraic[211] = (algebraic[147]-algebraic[136])+((constants[253]+constants[237])-constants[232])
    algebraic[154] = 1.00000/algebraic[153]
    algebraic[155] = algebraic[154]*(power(10.0000, -algebraic[0]+constants[239]))
    algebraic[156] = algebraic[155]
    algebraic[214] = (((algebraic[156]+algebraic[17])-algebraic[147])-algebraic[28])+(((constants[240]+constants[162])-constants[237])-constants[171])
    algebraic[160] = 1.00000/algebraic[159]
    algebraic[161] = algebraic[160]*(power(10.0000, -algebraic[0]+constants[245]))
    algebraic[163] = algebraic[161]
    algebraic[217] = (algebraic[163]-algebraic[156])+(((constants[246]+constants[249])-constants[240])-constants[251])
    algebraic[172] = (constants[254]+constants[253]*log(10.0000)*constants[0]*constants[130]*algebraic[0])-constants[143]*(0.00000-constants[253])
    algebraic[212] = (algebraic[172]+algebraic[152])-algebraic[141]
    algebraic[213] = (exp(-algebraic[212]/(constants[0]*constants[130]))*algebraic[142])/algebraic[131]
    algebraic[270] = (constants[318]*constants[317])/(constants[316]*algebraic[213])
    algebraic[272] = ((constants[318]*states[18])/constants[316]-(algebraic[270]*states[19])/constants[317])/(1.00000+states[19]/constants[317]+states[18]/constants[316])
    algebraic[44] = (constants[180]+constants[179]*log(10.0000)*constants[0]*constants[130]*algebraic[0])-constants[143]*(4.00000-constants[179])
    algebraic[179] = (2.00000*algebraic[34]-algebraic[22])-algebraic[44]
    algebraic[180] = (exp(-algebraic[179]/(constants[0]*constants[130]))*(power(algebraic[23], 2.00000)))/(algebraic[12]*algebraic[35])
    algebraic[287] = (constants[334]*(power(constants[337], 2.00000)))/(constants[335]*constants[336]*algebraic[180])
    algebraic[290] = ((constants[334]*states[10]*states[5])/(constants[336]*constants[335])-algebraic[287]*(power(states[9]/constants[337], 2.00000)))/(1.00000+states[10]/constants[336]+states[5]/constants[335]+(states[10]*states[5])/(constants[336]*constants[335])+(2.00000*states[9])/constants[337]+(power(states[9], 2.00000))/(power(constants[337], 2.00000)))
    algebraic[293] = algebraic[174]*-algebraic[286]+algebraic[178]*algebraic[290]+algebraic[184]*algebraic[238]+algebraic[181]*(algebraic[226]+algebraic[234])+algebraic[187]*algebraic[241]+algebraic[190]*algebraic[248]+algebraic[193]*algebraic[252]+algebraic[196]*algebraic[254]+algebraic[199]*algebraic[261]+algebraic[205]*algebraic[265]+algebraic[208]*algebraic[269]+algebraic[211]*algebraic[272]+algebraic[214]*algebraic[275]+algebraic[217]*algebraic[278]+algebraic[202]*algebraic[257]
    rates[24] = -algebraic[293]
    algebraic[299] = algebraic[286]
    rates[23] = algebraic[299]
    algebraic[279] = custom_piecewise([constants[38] != 5.00000 & constants[38] != 45.0000, constants[22] , constants[38] != 5.00000 & equal(constants[38] , 45.0000) & greater_equal(voi , 110.000), constants[22] , equal(constants[38] , 5.00000) & greater(voi , 30.0000), constants[22] , True, 0.00000])
    algebraic[284] = (algebraic[279]*states[10])/(constants[54]+states[10])
    algebraic[300] = (((-algebraic[286]-algebraic[290])-algebraic[248])+algebraic[265]+algebraic[275])-algebraic[284]
    rates[10] = algebraic[300]
    algebraic[301] = (((algebraic[286]+2.00000*algebraic[290]+algebraic[248])-algebraic[265])-algebraic[275])+algebraic[284]
    rates[9] = algebraic[301]
    algebraic[302] = -algebraic[290]
    rates[5] = algebraic[302]
    algebraic[303] = (-(algebraic[226]+algebraic[234])-algebraic[261])+algebraic[284]
    rates[3] = algebraic[303]
    algebraic[304] = (algebraic[226]+algebraic[234])-algebraic[238]
    rates[2] = algebraic[304]
    algebraic[305] = algebraic[248]-algebraic[252]
    rates[8] = algebraic[305]
    algebraic[306] = algebraic[252]+algebraic[254]+algebraic[257]
    rates[11] = algebraic[306]
    algebraic[307] = -algebraic[257]
    rates[13] = algebraic[307]
    algebraic[308] = algebraic[269]-algebraic[272]
    rates[18] = algebraic[308]
    algebraic[309] = algebraic[272]-algebraic[275]
    rates[19] = algebraic[309]
    algebraic[310] = algebraic[278]
    rates[21] = algebraic[310]
    algebraic[291] = (log(10.0000)*constants[338]*(power(10.0000, -algebraic[0]-6.87000)))/(power(power(10.0000, -algebraic[0])+power(10.0000, -6.87000), 2.00000))+(log(10.0000)*constants[339]*(power(10.0000, -algebraic[0]-8.30000)))/(power(power(10.0000, -algebraic[0])+power(10.0000, -8.30000), 2.00000))+(log(10.0000)*constants[340]*(power(10.0000, -algebraic[0]-4.80000)))/(power(power(10.0000, -algebraic[0])+power(10.0000, -4.80000), 2.00000))
    algebraic[7] = ((power(10.0000, constants[149]))*(algebraic[1]-power(10.0000, -algebraic[0]+constants[149])))/(constants[134]*(power(algebraic[1], 2.00000)))
    algebraic[18] = ((power(10.0000, constants[159]))*(algebraic[12]-power(10.0000, -algebraic[0]+constants[159])))/(constants[134]*(power(algebraic[12], 2.00000)))
    algebraic[29] = ((power(10.0000, constants[169]))*(algebraic[23]-power(10.0000, -algebraic[0]+constants[169])))/(constants[134]*(power(algebraic[23], 2.00000)))
    algebraic[40] = ((power(10.0000, constants[177]))*(algebraic[35]-power(10.0000, -algebraic[0]+constants[177])))/(constants[134]*(power(algebraic[35], 2.00000)))
    algebraic[51] = ((power(10.0000, constants[186]))*(algebraic[45]-power(10.0000, -algebraic[0]+constants[186])))/(constants[134]*(power(algebraic[45], 2.00000)))
    algebraic[59] = ((power(10.0000, constants[189]))*(algebraic[55]-power(10.0000, -algebraic[0]+constants[189])))/(constants[134]*(power(algebraic[55], 2.00000)))
    algebraic[65] = ((power(10.0000, constants[195]))*(algebraic[60]-power(10.0000, -algebraic[0]+constants[195])))/(constants[134]*(power(algebraic[60], 2.00000)))
    algebraic[74] = ((power(10.0000, constants[199]))*(algebraic[70]-power(10.0000, -algebraic[0]+constants[199])))/(constants[134]*(power(algebraic[70], 2.00000)))
    algebraic[80] = ((power(10.0000, constants[202]))*(algebraic[76]-power(10.0000, -algebraic[0]+constants[202])))/(constants[134]*(power(algebraic[76], 2.00000)))
    algebraic[88] = (algebraic[82]*(power(10.0000, constants[205])+2.00000*(power(10.0000, -algebraic[0]+constants[205]+constants[206])))-(power(10.0000, -algebraic[0]+constants[205])+2.00000*(power(10.0000, -2.00000*algebraic[0]+constants[205]+constants[206])))*(power(10.0000, constants[205])+2.00000*(power(10.0000, -algebraic[0]+constants[205]+constants[206]))))/(constants[134]*(power(algebraic[82], 2.00000)))
    algebraic[97] = ((power(10.0000, constants[210]))*(algebraic[93]-power(10.0000, -algebraic[0]+constants[210])))/(constants[134]*(power(algebraic[93], 2.00000)))
    algebraic[104] = ((power(10.0000, constants[216]))*(algebraic[99]-power(10.0000, -algebraic[0]+constants[216])))/(constants[134]*(power(algebraic[99], 2.00000)))
    algebraic[114] = ((power(10.0000, constants[219]))*(algebraic[109]-power(10.0000, -algebraic[0]+constants[219])))/(constants[134]*(power(algebraic[109], 2.00000)))
    algebraic[123] = ((power(10.0000, constants[223]))*(algebraic[119]-power(10.0000, -algebraic[0]+constants[223])))/(constants[134]*(power(algebraic[119], 2.00000)))
    algebraic[129] = ((power(10.0000, constants[226]))*(algebraic[125]-power(10.0000, -algebraic[0]+constants[226])))/(constants[134]*(power(algebraic[125], 2.00000)))
    algebraic[137] = ((power(10.0000, constants[229]))*(algebraic[131]-power(10.0000, -algebraic[0]+constants[229])))/(constants[134]*(power(algebraic[131], 2.00000)))
    algebraic[148] = ((power(10.0000, constants[234]))*(algebraic[142]-power(10.0000, -algebraic[0]+constants[234])))/(constants[134]*(power(algebraic[142], 2.00000)))
    algebraic[157] = ((power(10.0000, constants[239]))*(algebraic[153]-power(10.0000, -algebraic[0]+constants[239])))/(constants[134]*(power(algebraic[153], 2.00000)))
    algebraic[164] = ((power(10.0000, constants[245]))*(algebraic[159]-power(10.0000, -algebraic[0]+constants[245])))/(constants[134]*(power(algebraic[159], 2.00000)))
    algebraic[292] = log(10.0000)*(power(10.0000, -algebraic[0]))*constants[134]*(1.00000+algebraic[7]*states[3]+algebraic[18]*states[10]+algebraic[29]*states[9]+algebraic[40]*states[5]+algebraic[51]*states[23]+algebraic[59]*states[22]+algebraic[65]*states[2]+algebraic[74]*states[6]+algebraic[80]*states[7]+algebraic[88]*states[8]+algebraic[97]*states[12]+algebraic[114]*states[11]+algebraic[104]*states[13]+algebraic[123]*states[16]+algebraic[129]*states[17]+algebraic[137]*states[18]+algebraic[148]*states[19]+algebraic[157]*states[20]+algebraic[164]*states[21])
    algebraic[294] = algebraic[293]/(algebraic[291]+algebraic[292])
    algebraic[8] = ((-(power(10.0000, -algebraic[0]))/constants[134])*(power(10.0000, constants[149]+constants[150])))/(power(algebraic[1], 2.00000))
    algebraic[19] = ((-(power(10.0000, -algebraic[0]))/constants[134])*(power(10.0000, constants[159]+constants[160])))/(power(algebraic[12], 2.00000))
    algebraic[31] = ((-(power(10.0000, -algebraic[0]))/constants[134])*(power(10.0000, constants[169]+constants[170])))/(power(algebraic[23], 2.00000))
    algebraic[41] = ((-(power(10.0000, -algebraic[0]))/constants[134])*(power(10.0000, constants[177]+constants[178])))/(power(algebraic[35], 2.00000))
    algebraic[52] = ((-(power(10.0000, -algebraic[0]))/constants[134])*(power(10.0000, constants[186]+constants[187])))/(power(algebraic[45], 2.00000))
    algebraic[66] = ((-(power(10.0000, -algebraic[0]))/constants[134])*(power(10.0000, constants[195]+constants[196])))/(power(algebraic[60], 2.00000))
    algebraic[89] = (-(power(10.0000, -algebraic[0]+constants[205])+2.00000*(power(10.0000, -2.00000*algebraic[0]+constants[205]+constants[206])))*(power(10.0000, constants[207])))/(constants[134]*(power(algebraic[82], 2.00000)))
    algebraic[105] = ((-(power(10.0000, -algebraic[0]))/constants[134])*(power(10.0000, constants[216]+constants[213])))/(power(algebraic[99], 2.00000))
    algebraic[115] = ((-(power(10.0000, -algebraic[0]))/constants[134])*(power(10.0000, constants[219]+constants[220])))/(power(algebraic[109], 2.00000))
    algebraic[138] = ((-(power(10.0000, -algebraic[0]))/constants[134])*(power(10.0000, constants[229]+constants[230])))/(power(algebraic[131], 2.00000))
    algebraic[149] = ((-(power(10.0000, -algebraic[0]))/constants[134])*(power(10.0000, constants[234]+constants[235])))/(power(algebraic[142], 2.00000))
    algebraic[165] = ((-(power(10.0000, -algebraic[0]))/constants[134])*(power(10.0000, constants[245]+constants[242])))/(power(algebraic[159], 2.00000))
    algebraic[295] = (algebraic[8]*states[3]+algebraic[19]*states[10]+algebraic[31]*states[9]+algebraic[41]*states[5]+algebraic[52]*states[23]+constants[26]*states[22]+algebraic[66]*states[2]+constants[27]*states[6]+constants[28]*states[7]+algebraic[89]*states[8]+constants[29]*states[12]+algebraic[115]*states[11]+algebraic[105]*states[13]+constants[30]*states[16]+constants[31]*states[17]+algebraic[138]*states[18]+algebraic[149]*states[19]+constants[32]*states[20]+algebraic[165]*states[21])/(algebraic[291]+algebraic[292])
    algebraic[10] = ((states[1]/constants[134])*(power(10.0000, -algebraic[0]+constants[149]+constants[150]))*log(10.0000))/(power(algebraic[1], 2.00000))
    algebraic[21] = ((states[1]/constants[134])*(power(10.0000, -algebraic[0]+constants[159]+constants[160]))*log(10.0000))/(power(algebraic[12], 2.00000))
    algebraic[33] = ((states[1]/constants[134])*(power(10.0000, -algebraic[0]+constants[169]+constants[170]))*log(10.0000))/(power(algebraic[23], 2.00000))
    algebraic[43] = ((states[1]/constants[134])*(power(10.0000, -algebraic[0]+constants[177]+constants[178]))*log(10.0000))/(power(algebraic[35], 2.00000))
    algebraic[54] = ((states[1]/constants[134])*(power(10.0000, -algebraic[0]+constants[186]+constants[187]))*log(10.0000))/(power(algebraic[45], 2.00000))
    algebraic[68] = ((states[1]/constants[134])*(power(10.0000, -algebraic[0]+constants[195]+constants[196]))*log(10.0000))/(power(algebraic[60], 2.00000))
    algebraic[91] = ((states[1]/constants[134])*(power(10.0000, constants[207]))*(algebraic[82]*(power(10.0000, -algebraic[0]+constants[205]))*log(10.0000)-(power(10.0000, -2.00000*algebraic[0]+constants[205]+constants[206]))*2.00000*log(10.0000)))/(power(algebraic[82], 2.00000))
    algebraic[107] = ((states[1]/constants[134])*(power(10.0000, -algebraic[0]+constants[216]+constants[213]))*log(10.0000))/(power(algebraic[99], 2.00000))
    algebraic[117] = ((states[1]/constants[134])*(power(10.0000, -algebraic[0]+constants[219]+constants[220]))*log(10.0000))/(power(algebraic[109], 2.00000))
    algebraic[140] = ((states[1]/constants[134])*(power(10.0000, -algebraic[0]+constants[229]+constants[230]))*log(10.0000))/(power(algebraic[131], 2.00000))
    algebraic[151] = ((states[1]/constants[134])*(power(10.0000, -algebraic[0]+constants[234]+constants[235]))*log(10.0000))/(power(algebraic[142], 2.00000))
    algebraic[167] = ((states[1]/constants[134])*(power(10.0000, -algebraic[0]+constants[245]+constants[242]))*log(10.0000))/(power(algebraic[159], 2.00000))
    algebraic[9] = ((algebraic[1]*(power(10.0000, constants[150])))/constants[134]-((states[1]/constants[134])*(power(10.0000, 2.00000*constants[150])))/constants[134])/(power(algebraic[1], 2.00000))
    algebraic[20] = ((algebraic[12]*(power(10.0000, constants[160])))/constants[134]-((states[1]/constants[134])*(power(10.0000, 2.00000*constants[160])))/constants[134])/(power(algebraic[12], 2.00000))
    algebraic[32] = ((algebraic[23]*(power(10.0000, constants[170])))/constants[134]-((states[1]/constants[134])*(power(10.0000, 2.00000*constants[170])))/constants[134])/(power(algebraic[23], 2.00000))
    algebraic[42] = ((algebraic[35]*(power(10.0000, constants[178])))/constants[134]-((states[1]/constants[134])*(power(10.0000, 2.00000*constants[178])))/constants[134])/(power(algebraic[35], 2.00000))
    algebraic[53] = ((algebraic[45]*(power(10.0000, constants[187])))/constants[134]-((states[1]/constants[134])*(power(10.0000, 2.00000*constants[187])))/constants[134])/(power(algebraic[45], 2.00000))
    algebraic[67] = ((algebraic[60]*(power(10.0000, constants[196])))/constants[134]-((states[1]/constants[134])*(power(10.0000, 2.00000*constants[196])))/constants[134])/(power(algebraic[60], 2.00000))
    algebraic[90] = ((algebraic[82]*(power(10.0000, constants[207])))/constants[134]-((states[1]/constants[134])*(power(10.0000, 2.00000*constants[207])))/constants[134])/(power(algebraic[82], 2.00000))
    algebraic[106] = ((algebraic[99]*(power(10.0000, constants[213])))/constants[134]-((states[1]/constants[134])*(power(10.0000, 2.00000*constants[213])))/constants[134])/(power(algebraic[99], 2.00000))
    algebraic[116] = ((algebraic[109]*(power(10.0000, constants[220])))/constants[134]-((states[1]/constants[134])*(power(10.0000, 2.00000*constants[220])))/constants[134])/(power(algebraic[109], 2.00000))
    algebraic[139] = ((algebraic[131]*(power(10.0000, constants[230])))/constants[134]-((states[1]/constants[134])*(power(10.0000, 2.00000*constants[230])))/constants[134])/(power(algebraic[131], 2.00000))
    algebraic[150] = ((algebraic[142]*(power(10.0000, constants[235])))/constants[134]-((states[1]/constants[134])*(power(10.0000, 2.00000*constants[235])))/constants[134])/(power(algebraic[142], 2.00000))
    algebraic[166] = ((algebraic[159]*(power(10.0000, constants[242])))/constants[134]-((states[1]/constants[134])*(power(10.0000, 2.00000*constants[242])))/constants[134])/(power(algebraic[159], 2.00000))
    algebraic[296] = -1.00000-(algebraic[20]*states[10]+algebraic[32]*states[9]+algebraic[42]*states[5]+algebraic[9]*states[3]+algebraic[53]*states[23]+algebraic[67]*states[2]+algebraic[90]*states[8]+algebraic[106]*states[13]+algebraic[116]*states[11]+algebraic[150]*states[19]+algebraic[139]*states[18]+algebraic[166]*states[21])
    algebraic[297] = (algebraic[21]*states[10]+algebraic[33]*states[9]+algebraic[43]*states[5]+algebraic[10]*states[3]+algebraic[54]*states[23]+algebraic[68]*states[2]+algebraic[91]*states[8]+algebraic[107]*states[13]+algebraic[117]*states[11]+algebraic[151]*states[19]+algebraic[140]*states[18]+algebraic[167]*states[21])/algebraic[296]
    algebraic[5] = (states[1]/constants[134])*(power(10.0000, constants[150]))*algebraic[2]
    algebraic[49] = (states[1]/constants[134])*(power(10.0000, constants[187]))*algebraic[46]
    algebraic[63] = ((algebraic[61]*states[1])/constants[134])*(power(10.0000, constants[196]))
    algebraic[86] = ((algebraic[83]*states[1])/constants[134])*(power(10.0000, constants[207]))
    algebraic[102] = ((algebraic[100]*states[1])/constants[134])*(power(10.0000, constants[213]))
    algebraic[112] = ((algebraic[110]*states[1])/constants[134])*(power(10.0000, constants[220]))
    algebraic[135] = ((algebraic[132]*states[1])/constants[134])*(power(10.0000, constants[230]))
    algebraic[146] = ((algebraic[143]*states[1])/constants[134])*(power(10.0000, constants[235]))
    algebraic[162] = (states[1]/constants[134])*(power(10.0000, constants[242]))*algebraic[160]
    algebraic[311] = (algebraic[15]*algebraic[300]+algebraic[26]*algebraic[301]+algebraic[38]*algebraic[302]+algebraic[5]*algebraic[303]+algebraic[49]*algebraic[299]+algebraic[63]*algebraic[304]+algebraic[86]*algebraic[305]+algebraic[102]*algebraic[307]+algebraic[112]*algebraic[306]+algebraic[146]*algebraic[309]+algebraic[135]*algebraic[308]+algebraic[162]*algebraic[310])/algebraic[296]
    rates[1] = custom_piecewise([less_equal(voi , 1.00000), (constants[33]*(algebraic[311]+algebraic[297]*algebraic[294]))/(1.00000-algebraic[297]*algebraic[295]) , True, constants[33]*algebraic[311]])
    rates[0] = (constants[341]*(algebraic[294]+algebraic[311]*algebraic[295]))/(1.00000-algebraic[297]*algebraic[295])
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[220] = custom_piecewise([constants[38] != 45.0000, constants[5] , less(voi , 40.0000), 0.00100000 , greater_equal(voi , 40.0000) & less(voi , 80.0000), 0.00400000 , greater_equal(voi , 80.0000) & less(voi , 100.000), 0.0100000 , greater_equal(voi , 100.000), 0.0400000 , True, float('nan')])
    algebraic[221] = 1.00000+states[4]/constants[39]+states[3]/constants[264]+(states[4]*states[3])/(constants[39]*constants[40])+states[4]/constants[266]+states[2]/constants[41]+(states[4]*states[2])/(constants[267]*constants[266])
    algebraic[0] = custom_piecewise([less_equal(voi , 1.00000) | greater(voi , 1.00000) & equal(constants[34] , 0.00000), states[0] , True, constants[35]])
    algebraic[222] = 1.40400/(1.00000+power(10.0000, 5.94000-algebraic[0])+power(10.0000, algebraic[0]-7.29000))
    algebraic[224] = ((algebraic[222]*constants[263]*states[3])/(constants[265]*constants[264]))/algebraic[221]
    algebraic[1] = 1.00000+power(10.0000, -algebraic[0]+constants[149])+(states[1]/constants[134])*(power(10.0000, constants[150]))+(constants[133]/constants[134])*(power(10.0000, constants[144]))
    algebraic[60] = 1.00000+(power(10.0000, -algebraic[0]))*(power(10.0000, constants[195]))+(states[1]/constants[134])*(power(10.0000, constants[196]))
    algebraic[11] = (constants[152]+constants[151]*log(10.0000)*constants[0]*constants[130]*algebraic[0])-constants[143]*(4.00000-constants[151])
    algebraic[69] = (constants[198]+constants[197]*log(10.0000)*constants[0]*constants[130]*algebraic[0])-constants[143]*(4.00000-constants[197])
    algebraic[169] = 655.700+constants[248]*log(10.0000)*constants[0]*constants[130]*algebraic[0]
    algebraic[182] = (algebraic[169]+algebraic[69])-algebraic[11]
    algebraic[183] = (exp(-algebraic[182]/(constants[0]*constants[130]))*algebraic[60])/algebraic[1]
    algebraic[223] = (algebraic[222]*constants[263]*constants[266]*constants[267])/(constants[265]*constants[264]*algebraic[183])
    algebraic[225] = ((algebraic[223]*states[4])/(constants[266]*constants[267]))/algebraic[221]
    algebraic[226] = algebraic[220]*(states[4]*algebraic[224]-states[2]*algebraic[225])
    algebraic[227] = 1.00000-algebraic[220]
    algebraic[228] = ((power(states[5]/constants[44], constants[46]))/constants[45])/(1.00000+(power(states[5]/constants[44], constants[46]))/constants[45])
    algebraic[229] = 1.00000+states[4]/constants[269]+states[3]/constants[42]+states[4]/constants[271]+states[2]/constants[43]+(states[4]*states[3])/(constants[269]*constants[268])+(states[4]*states[2])/(constants[270]*constants[271])
    algebraic[230] = 1.75000/(1.00000+power(10.0000, 6.12000-algebraic[0])+power(10.0000, algebraic[0]-7.03000))
    algebraic[232] = ((algebraic[230]*algebraic[228]*constants[263]*states[3])/(constants[269]*constants[268]))/algebraic[229]
    algebraic[231] = (algebraic[230]*constants[263]*constants[270]*constants[271])/(constants[269]*constants[268]*algebraic[183])
    algebraic[233] = ((algebraic[228]*algebraic[231]*states[4])/(constants[270]*constants[271]))/algebraic[229]
    algebraic[234] = algebraic[227]*(states[4]*algebraic[232]-states[2]*algebraic[233])
    algebraic[236] = -(algebraic[226]+algebraic[234])
    algebraic[235] = (constants[272]*1.32900)/(1.00000+power(10.0000, -algebraic[0]+6.64000)+power(10.0000, algebraic[0]-8.36000))
    algebraic[70] = 1.00000+power(10.0000, -algebraic[0]+constants[199])
    algebraic[75] = (constants[201]+constants[200]*log(10.0000)*constants[0]*constants[130]*algebraic[0])-constants[143]*(4.00000-constants[200])
    algebraic[185] = algebraic[75]-algebraic[69]
    algebraic[186] = (exp(-algebraic[185]/(constants[0]*constants[130]))*algebraic[70])/algebraic[60]
    algebraic[237] = (algebraic[235]*constants[274])/(constants[273]*algebraic[186])
    algebraic[238] = ((algebraic[235]*states[2])/constants[273]-(algebraic[237]*states[6])/constants[274])/(1.00000+states[2]/constants[273]+states[6]/constants[274])
    algebraic[239] = constants[275]/(1.00000+power(10.0000, -algebraic[0]+6.94000)+power(10.0000, algebraic[0]-9.35000))
    algebraic[76] = 1.00000+power(10.0000, -algebraic[0]+constants[202])
    algebraic[81] = (constants[204]+constants[203]*log(10.0000)*constants[0]*constants[130]*algebraic[0])-constants[143]*(4.00000-constants[203])
    algebraic[188] = algebraic[81]-algebraic[75]
    algebraic[189] = (exp(-algebraic[188]/(constants[0]*constants[130]))*algebraic[76])/algebraic[70]
    algebraic[240] = ((algebraic[239]*constants[276])/constants[277])*algebraic[189]
    algebraic[241] = ((algebraic[240]*states[6])/constants[276]-(algebraic[239]*states[7])/constants[277])/(1.00000+states[7]/constants[277]+states[6]/constants[276])
    algebraic[243] = algebraic[238]-algebraic[241]
    algebraic[242] = constants[278]/(1.00000+power(algebraic[0]/6.80000, -30.0000))
    algebraic[12] = 1.00000+power(10.0000, -algebraic[0]+constants[159])+(states[1]/constants[134])*(power(10.0000, constants[160]))+(constants[133]/constants[134])*(power(10.0000, constants[161]))
    algebraic[23] = 1.00000+power(10.0000, -algebraic[0]+constants[169])+(states[1]/constants[134])*(power(10.0000, constants[170]))+(constants[133]/constants[134])*(power(10.0000, constants[164]))
    algebraic[82] = 1.00000+power(10.0000, -algebraic[0]+constants[205])+power(10.0000, -2.00000*algebraic[0]+constants[205]+constants[206])+(states[1]/constants[134])*(power(10.0000, constants[207]))
    algebraic[22] = (constants[163]+constants[162]*constants[0]*constants[130]*log(10.0000)*algebraic[0])-constants[143]*(16.0000-constants[162])
    algebraic[34] = (constants[172]+constants[171]*constants[0]*constants[130]*log(10.0000)*algebraic[0])-constants[143]*(9.00000-constants[171])
    algebraic[92] = (constants[209]+constants[208]*log(10.0000)*constants[0]*constants[130]*algebraic[0])-constants[143]*(16.0000-constants[208])
    algebraic[173] = constants[256]+constants[255]*log(10.0000)*constants[0]*constants[130]*algebraic[0]
    algebraic[191] = ((algebraic[92]+algebraic[34]+algebraic[173])-algebraic[81])-algebraic[22]
    algebraic[192] = (exp(-algebraic[191]/(constants[0]*constants[130]))*algebraic[82]*algebraic[23])/(algebraic[76]*algebraic[12]*(power(10.0000, -algebraic[0])))
    algebraic[244] = (algebraic[242]*constants[282]*constants[284])/(constants[279]*constants[281]*algebraic[192])
    algebraic[245] = constants[53]*(power((((1.00000+states[10]/constants[49])/(1.00000+(constants[51]*states[10])/constants[49]))*(1.00000+(constants[52]*states[5])/constants[50]))/(1.00000+states[5]/constants[50]), 4.00000))
    algebraic[246] = (1.00000+states[7]/constants[279])*(1.00000+states[10]/constants[281])+states[8]/constants[282]+(states[9]/constants[284])*(1.00000+states[8]/constants[282])
    algebraic[247] = (1.00000+states[7]/constants[280])*(1.00000+states[10]/constants[283])+states[8]/constants[47]+(states[9]/constants[48])*(1.00000+states[8]/constants[47])
    algebraic[248] = ((((algebraic[242]*states[7]*states[10])/(constants[279]*constants[281]))/algebraic[246]-((algebraic[244]*states[9]*states[8])/(constants[284]*constants[282]))/algebraic[246])*(1.00000+constants[285]*algebraic[245]*(power(algebraic[247]/algebraic[246], 3.00000))))/(1.00000+algebraic[245]*(power(algebraic[247]/algebraic[246], 4.00000)))
    algebraic[250] = algebraic[241]-algebraic[248]
    algebraic[249] = (constants[286]*1.01300)/(1.00000+power(10.0000, -algebraic[0]+5.32000)+power(10.0000, algebraic[0]-9.15000))
    algebraic[93] = 1.00000+power(10.0000, -algebraic[0]+constants[210])
    algebraic[109] = 1.00000+power(10.0000, -algebraic[0]+constants[219])+(states[1]/constants[134])*(power(10.0000, constants[220]))
    algebraic[98] = (constants[212]+constants[211]*log(10.0000)*constants[0]*constants[130]*algebraic[0])-constants[143]*(4.00000-constants[211])
    algebraic[118] = (constants[222]+constants[221]*log(10.0000)*constants[0]*constants[130]*algebraic[0])-constants[143]*(4.00000-constants[221])
    algebraic[194] = (algebraic[118]+algebraic[98])-algebraic[92]
    algebraic[195] = (1.00000*exp(-algebraic[194]/(constants[0]*constants[130]))*algebraic[93]*algebraic[82])/algebraic[109]
    algebraic[251] = (algebraic[249]*constants[289]*constants[288])/(constants[287]*algebraic[195])
    algebraic[252] = ((algebraic[249]*states[8])/constants[287]-(algebraic[251]*states[12]*states[11])/(constants[289]*constants[288]))/(1.00000+states[8]/constants[287]+states[12]/constants[289]+states[11]/constants[288])
    algebraic[197] = algebraic[118]-algebraic[98]
    algebraic[198] = (exp(-algebraic[197]/(constants[0]*constants[130]))*algebraic[109])/algebraic[93]
    algebraic[253] = (constants[293]*constants[292])/(constants[291]*algebraic[198])
    algebraic[254] = ((constants[293]*states[12])/constants[291]-(algebraic[253]*states[11])/constants[292])/(1.00000+states[12]/constants[291]+states[11]/constants[292])
    algebraic[258] = 1.00000+states[3]/constants[303]+states[12]/constants[301]+states[14]/constants[302]+(states[12]*states[14])/(constants[301]*constants[302])+(states[12]*states[14]*states[3])/(constants[301]*constants[302]*constants[303])+states[16]/constants[304]+states[15]/constants[305]+(states[16]*states[15])/(constants[305]*constants[304])
    algebraic[259] = constants[300]*0.000700000*exp(algebraic[0]*0.897900)
    algebraic[119] = 1.00000+power(10.0000, -algebraic[0]+constants[223])
    algebraic[124] = (constants[225]+constants[224]*log(10.0000)*constants[0]*constants[130]*algebraic[0])-constants[143]*(16.0000-constants[224])
    algebraic[170] = (constants[250]+constants[249]*log(10.0000)*constants[0]*constants[130]*algebraic[0])-constants[143]*(1.00000-constants[249])
    algebraic[171] = (constants[252]+constants[251]*log(10.0000)*constants[0]*constants[130]*algebraic[0])-constants[143]*(4.00000-constants[251])
    algebraic[200] = (((algebraic[124]+algebraic[171]+algebraic[173])-algebraic[11])-algebraic[98])-algebraic[170]
    algebraic[201] = (exp(-algebraic[200]/(constants[0]*constants[130]))*algebraic[119])/(algebraic[1]*algebraic[93]*(power(10.0000, -algebraic[0]))*1.00000)
    algebraic[260] = (algebraic[259]*constants[304]*constants[305])/(constants[301]*constants[303]*constants[302]*algebraic[201])
    algebraic[261] = ((algebraic[259]*states[12]*states[14]*states[3])/(constants[302]*constants[301]*constants[303])-(algebraic[260]*states[16]*states[15])/(constants[304]*constants[305]))/algebraic[258]
    algebraic[263] = (algebraic[252]-algebraic[254])-algebraic[261]
    algebraic[125] = 1.00000+power(10.0000, -algebraic[0]+6.21000)
    algebraic[130] = (constants[228]+constants[227]*log(10.0000)*constants[0]*constants[130]*algebraic[0])-constants[143]*(9.00000-constants[227])
    algebraic[206] = ((algebraic[22]+algebraic[130])-algebraic[124])-algebraic[34]
    algebraic[207] = (exp(-algebraic[206]/(constants[0]*constants[130]))*algebraic[12]*algebraic[125])/(algebraic[119]*algebraic[23])
    algebraic[262] = ((constants[311]*constants[307]*constants[308])/(constants[309]*constants[310]))*algebraic[207]
    algebraic[264] = 1.00000+states[9]/constants[308]+states[16]/constants[307]+(states[16]*states[9])/(constants[307]*constants[308])+states[17]/constants[309]+states[10]/constants[310]+(states[17]*states[10])/(constants[309]*constants[310])
    algebraic[265] = ((algebraic[262]*states[16]*states[9])/(constants[308]*constants[307])-(constants[311]*states[10]*states[17])/(constants[310]*constants[309]))/algebraic[264]
    algebraic[267] = algebraic[261]-algebraic[265]
    algebraic[266] = (constants[312]*0.989000)/(1.00000+power(10.0000, -algebraic[0]+5.62000)+power(10.0000, algebraic[0]-8.74000))
    algebraic[131] = 1.00000+power(10.0000, -algebraic[0]+constants[229])+(states[1]/constants[134])*(power(10.0000, constants[230]))+(constants[133]/constants[134])*(power(10.0000, constants[231]))
    algebraic[141] = (constants[233]+constants[232]*log(10.0000)*constants[0]*constants[130]*algebraic[0])-constants[143]*(9.00000-constants[232])
    algebraic[209] = algebraic[141]-algebraic[130]
    algebraic[210] = (exp(-algebraic[209]/(constants[0]*constants[130]))*algebraic[131])/algebraic[125]
    algebraic[268] = (algebraic[266]*constants[314])/(constants[313]*algebraic[210])
    algebraic[269] = ((algebraic[266]*states[17])/constants[313]-(algebraic[268]*states[18])/constants[314])/(1.00000+states[17]/constants[313]+states[18]/constants[314])
    algebraic[271] = algebraic[265]-algebraic[269]
    algebraic[255] = (1.00000+states[13]/constants[295]+states[15]/constants[298])*(1.00000+states[11]/constants[297]+states[14]/constants[298])
    algebraic[99] = 1.00000+power(10.0000, -algebraic[0]+constants[216])+(states[1]/constants[134])*(power(10.0000, constants[213]))
    algebraic[108] = (constants[218]+constants[217]*log(10.0000)*constants[0]*constants[130]*algebraic[0])-constants[143]*(4.00000-constants[217])
    algebraic[203] = ((algebraic[173]+algebraic[171]+algebraic[118])-algebraic[170])-algebraic[108]
    algebraic[204] = (exp(-algebraic[203]/(constants[0]*constants[130]))*algebraic[109])/(algebraic[99]*(power(10.0000, -algebraic[0])))
    algebraic[256] = (constants[299]*constants[295]*constants[296]*algebraic[204])/(constants[297]*constants[298])
    algebraic[257] = ((algebraic[256]*states[13]*states[14])/(constants[295]*constants[296])-(constants[299]*states[11]*states[15])/(constants[297]*constants[298]))/algebraic[255]
    algebraic[276] = constants[324]*(-0.113400*algebraic[0]+1.60690)
    algebraic[153] = 1.00000+power(10.0000, -algebraic[0]+constants[239])
    algebraic[159] = 1.00000+power(10.0000, -algebraic[0]+constants[245])+(states[1]/constants[134])*(power(10.0000, constants[242]))
    algebraic[158] = (constants[241]+constants[240]*log(10.0000)*constants[0]*constants[130]*algebraic[0])-constants[143]*(1.00000-constants[240])
    algebraic[168] = (constants[247]+constants[246]*log(10.0000)*constants[0]*constants[130]*algebraic[0])-constants[143]*(1.00000-constants[246])
    algebraic[218] = (((algebraic[168]+algebraic[170])-algebraic[158])-algebraic[171])-algebraic[173]
    algebraic[219] = (exp(-algebraic[218]/(constants[0]*constants[130]))*algebraic[159]*(power(10.0000, -algebraic[0])))/algebraic[153]
    algebraic[277] = (algebraic[276]*constants[327]*constants[328])/(constants[325]*constants[326]*algebraic[219])
    algebraic[278] = ((algebraic[276]*states[20]*states[15])/(constants[325]*constants[326])-(algebraic[277]*states[21]*states[14])/(constants[327]*constants[328]))/(1.00000+states[20]/constants[325]+states[15]/constants[326]+(states[20]*states[15])/(constants[325]*constants[326])+states[21]/constants[327]+states[14]/constants[328]+(states[21]*states[14])/(constants[327]*constants[328]))
    algebraic[281] = (-algebraic[261]-algebraic[257])+algebraic[278]
    algebraic[282] = (algebraic[261]+algebraic[257])-algebraic[278]
    algebraic[273] = (constants[319]*1.05000)/(1.00000+power(10.0000, -algebraic[0]+5.58000)+power(10.0000, algebraic[0]-8.79000))
    algebraic[142] = 1.00000+power(10.0000, constants[234]-algebraic[0])+(states[1]/constants[134])*(power(10.0000, constants[235]))+(constants[133]/constants[134])*(power(10.0000, constants[236]))
    algebraic[152] = (constants[238]+constants[237]*log(10.0000)*constants[0]*constants[130]*algebraic[0])-constants[143]*(9.00000-constants[237])
    algebraic[215] = (((algebraic[158]+algebraic[22])-algebraic[173])-algebraic[152])-algebraic[34]
    algebraic[216] = (exp(-algebraic[215]/(constants[0]*constants[130]))*algebraic[153]*algebraic[12]*(power(10.0000, -algebraic[0])))/(algebraic[142]*algebraic[23])
    algebraic[274] = (algebraic[273]*constants[322]*constants[323])/(constants[320]*constants[321]*algebraic[216])
    algebraic[275] = ((algebraic[273]*states[19]*states[9])/(constants[320]*constants[321])-(algebraic[274]*states[20]*states[10])/(constants[322]*constants[323]))/(1.00000+states[19]/constants[320]+states[9]/constants[321]+(states[19]*states[9])/(constants[320]*constants[321])+states[10]/constants[323]+states[20]/constants[322]+(states[20]*states[10])/(constants[322]*constants[323]))
    algebraic[283] = algebraic[275]-algebraic[278]
    algebraic[45] = 1.00000+power(10.0000, -algebraic[0]+constants[186])+(states[1]/constants[134])*(power(10.0000, constants[187]))+(constants[133]/constants[134])*(power(10.0000, constants[181]))
    algebraic[55] = 1.00000+power(10.0000, -algebraic[0]+constants[189])
    algebraic[176] = (exp(-constants[262]/(constants[0]*constants[130]))*(power(10.0000, -algebraic[0]))*algebraic[12]*algebraic[55])/(algebraic[45]*algebraic[23])
    algebraic[285] = ((constants[329]/algebraic[176])*constants[331]*constants[333])/(constants[332]*constants[330])
    algebraic[286] = ((algebraic[285]*states[10]*states[22])/(constants[331]*constants[333])-(constants[329]*states[9]*states[23])/(constants[332]*constants[330]))/(1.00000+states[9]/constants[332]+states[23]/constants[55]+(states[23]*states[9])/(constants[332]*constants[330])+states[10]/constants[331]+(states[22]*states[10])/(constants[333]*constants[331]))
    algebraic[289] = -algebraic[286]
    algebraic[13] = 1.00000/algebraic[12]
    algebraic[14] = (power(10.0000, -algebraic[0]+constants[159]))*algebraic[13]
    algebraic[15] = (states[1]/constants[134])*(power(10.0000, constants[160]))*algebraic[13]
    algebraic[16] = (constants[133]/constants[134])*(power(10.0000, constants[161]))*algebraic[13]
    algebraic[17] = 0.00000*algebraic[13]+1.00000*algebraic[14]+0.00000*algebraic[15]+0.00000*algebraic[16]
    algebraic[24] = 1.00000/algebraic[23]
    algebraic[25] = (power(10.0000, -algebraic[0]+constants[169]))*algebraic[24]
    algebraic[26] = ((algebraic[24]*states[1])/constants[134])*(power(10.0000, constants[170]))
    algebraic[27] = ((algebraic[24]*constants[133])/constants[134])*(power(10.0000, constants[164]))
    algebraic[28] = 0.00000*algebraic[24]+1.00000*algebraic[25]+0.00000*algebraic[26]+0.00000*algebraic[27]
    algebraic[46] = 1.00000/algebraic[45]
    algebraic[48] = (power(10.0000, -algebraic[0]+constants[186]))*algebraic[46]
    algebraic[50] = algebraic[48]
    algebraic[56] = 1.00000/algebraic[55]
    algebraic[57] = algebraic[56]*(power(10.0000, -algebraic[0]+constants[189]))
    algebraic[58] = 0.00000*algebraic[56]+1.00000*algebraic[57]
    algebraic[174] = (((algebraic[17]+algebraic[58])-algebraic[50])-algebraic[28])+(((constants[162]+constants[190])-constants[188])-constants[171])
    algebraic[35] = 1.00000+power(10.0000, constants[177]-algebraic[0])+(states[1]/constants[134])*(power(10.0000, constants[178]))
    algebraic[36] = 1.00000/algebraic[35]
    algebraic[37] = algebraic[36]*(power(10.0000, constants[177]-algebraic[0]))
    algebraic[38] = (states[1]/constants[134])*(power(10.0000, constants[178]))*algebraic[36]
    algebraic[39] = 0.00000*algebraic[36]+algebraic[37]+0.00000*algebraic[38]
    algebraic[178] = ((2.00000*algebraic[28]-algebraic[17])-algebraic[39])+((2.00000*constants[171]-constants[162])-constants[179])
    algebraic[2] = 1.00000/algebraic[1]
    algebraic[3] = (power(10.0000, -algebraic[0]+constants[149]))*algebraic[2]
    algebraic[6] = 1.00000*algebraic[3]
    algebraic[61] = 1.00000/algebraic[60]
    algebraic[62] = algebraic[61]*(power(10.0000, -algebraic[0]+constants[195]))
    algebraic[64] = algebraic[62]
    algebraic[181] = (algebraic[64]-algebraic[6])+(1.00000-constants[151])
    algebraic[71] = 1.00000/algebraic[70]
    algebraic[72] = algebraic[71]*(power(10.0000, -algebraic[0]+constants[199]))
    algebraic[73] = algebraic[72]
    algebraic[184] = (algebraic[73]-algebraic[64])+(constants[200]-constants[197])
    algebraic[77] = 1.00000/algebraic[76]
    algebraic[78] = algebraic[77]*(power(10.0000, -algebraic[0]+constants[202]))
    algebraic[79] = algebraic[78]
    algebraic[187] = (algebraic[79]-algebraic[73])+(constants[203]-constants[200])
    algebraic[83] = 1.00000/algebraic[82]
    algebraic[84] = algebraic[83]*(power(10.0000, -algebraic[0]+constants[205]))
    algebraic[85] = algebraic[83]*(power(10.0000, -2.00000*algebraic[0]+constants[205]+constants[206]))
    algebraic[87] = algebraic[84]+2.00000*algebraic[85]
    algebraic[190] = (((((algebraic[28]+algebraic[87])-algebraic[79])-algebraic[17])+constants[171]+constants[208])-constants[203])-constants[162]
    algebraic[94] = 1.00000/algebraic[93]
    algebraic[95] = algebraic[94]*(power(10.0000, -algebraic[0]+constants[210]))
    algebraic[96] = algebraic[95]
    algebraic[110] = 1.00000/algebraic[109]
    algebraic[111] = algebraic[110]*(power(10.0000, -algebraic[0]+constants[219]))
    algebraic[113] = algebraic[111]
    algebraic[193] = ((algebraic[113]+algebraic[96])-algebraic[87])+((constants[221]+constants[211])-constants[208])
    algebraic[196] = (algebraic[113]-algebraic[96])+(constants[221]-constants[211])
    algebraic[120] = 1.00000/algebraic[119]
    algebraic[121] = algebraic[120]*(power(10.0000, -algebraic[0]+constants[223]))
    algebraic[122] = algebraic[121]
    algebraic[199] = ((algebraic[122]-algebraic[96])-algebraic[6])+((((constants[224]+constants[251])-constants[211])-constants[151])-constants[249])
    algebraic[100] = 1.00000/algebraic[99]
    algebraic[101] = algebraic[100]*(power(10.0000, -algebraic[0]+constants[216]))
    algebraic[103] = algebraic[101]
    algebraic[202] = (algebraic[113]-algebraic[103])+(((constants[221]+constants[251])-constants[249])-constants[217])
    algebraic[126] = 1.00000/algebraic[125]
    algebraic[127] = algebraic[126]*(power(10.0000, -algebraic[0]+6.21000))
    algebraic[128] = algebraic[127]
    algebraic[205] = (((algebraic[128]+algebraic[17])-algebraic[122])-algebraic[28])+(((constants[227]+constants[162])-constants[224])-constants[171])
    algebraic[132] = 1.00000/algebraic[131]
    algebraic[133] = algebraic[132]*(power(10.0000, -algebraic[0]+constants[229]))
    algebraic[136] = algebraic[133]
    algebraic[208] = (algebraic[136]-algebraic[128])+(constants[232]-constants[227])
    algebraic[143] = 1.00000/algebraic[142]
    algebraic[144] = algebraic[143]*(power(10.0000, constants[234]-algebraic[0]))
    algebraic[147] = algebraic[144]
    algebraic[211] = (algebraic[147]-algebraic[136])+((constants[253]+constants[237])-constants[232])
    algebraic[154] = 1.00000/algebraic[153]
    algebraic[155] = algebraic[154]*(power(10.0000, -algebraic[0]+constants[239]))
    algebraic[156] = algebraic[155]
    algebraic[214] = (((algebraic[156]+algebraic[17])-algebraic[147])-algebraic[28])+(((constants[240]+constants[162])-constants[237])-constants[171])
    algebraic[160] = 1.00000/algebraic[159]
    algebraic[161] = algebraic[160]*(power(10.0000, -algebraic[0]+constants[245]))
    algebraic[163] = algebraic[161]
    algebraic[217] = (algebraic[163]-algebraic[156])+(((constants[246]+constants[249])-constants[240])-constants[251])
    algebraic[172] = (constants[254]+constants[253]*log(10.0000)*constants[0]*constants[130]*algebraic[0])-constants[143]*(0.00000-constants[253])
    algebraic[212] = (algebraic[172]+algebraic[152])-algebraic[141]
    algebraic[213] = (exp(-algebraic[212]/(constants[0]*constants[130]))*algebraic[142])/algebraic[131]
    algebraic[270] = (constants[318]*constants[317])/(constants[316]*algebraic[213])
    algebraic[272] = ((constants[318]*states[18])/constants[316]-(algebraic[270]*states[19])/constants[317])/(1.00000+states[19]/constants[317]+states[18]/constants[316])
    algebraic[44] = (constants[180]+constants[179]*log(10.0000)*constants[0]*constants[130]*algebraic[0])-constants[143]*(4.00000-constants[179])
    algebraic[179] = (2.00000*algebraic[34]-algebraic[22])-algebraic[44]
    algebraic[180] = (exp(-algebraic[179]/(constants[0]*constants[130]))*(power(algebraic[23], 2.00000)))/(algebraic[12]*algebraic[35])
    algebraic[287] = (constants[334]*(power(constants[337], 2.00000)))/(constants[335]*constants[336]*algebraic[180])
    algebraic[290] = ((constants[334]*states[10]*states[5])/(constants[336]*constants[335])-algebraic[287]*(power(states[9]/constants[337], 2.00000)))/(1.00000+states[10]/constants[336]+states[5]/constants[335]+(states[10]*states[5])/(constants[336]*constants[335])+(2.00000*states[9])/constants[337]+(power(states[9], 2.00000))/(power(constants[337], 2.00000)))
    algebraic[293] = algebraic[174]*-algebraic[286]+algebraic[178]*algebraic[290]+algebraic[184]*algebraic[238]+algebraic[181]*(algebraic[226]+algebraic[234])+algebraic[187]*algebraic[241]+algebraic[190]*algebraic[248]+algebraic[193]*algebraic[252]+algebraic[196]*algebraic[254]+algebraic[199]*algebraic[261]+algebraic[205]*algebraic[265]+algebraic[208]*algebraic[269]+algebraic[211]*algebraic[272]+algebraic[214]*algebraic[275]+algebraic[217]*algebraic[278]+algebraic[202]*algebraic[257]
    algebraic[299] = algebraic[286]
    algebraic[279] = custom_piecewise([constants[38] != 5.00000 & constants[38] != 45.0000, constants[22] , constants[38] != 5.00000 & equal(constants[38] , 45.0000) & greater_equal(voi , 110.000), constants[22] , equal(constants[38] , 5.00000) & greater(voi , 30.0000), constants[22] , True, 0.00000])
    algebraic[284] = (algebraic[279]*states[10])/(constants[54]+states[10])
    algebraic[300] = (((-algebraic[286]-algebraic[290])-algebraic[248])+algebraic[265]+algebraic[275])-algebraic[284]
    algebraic[301] = (((algebraic[286]+2.00000*algebraic[290]+algebraic[248])-algebraic[265])-algebraic[275])+algebraic[284]
    algebraic[302] = -algebraic[290]
    algebraic[303] = (-(algebraic[226]+algebraic[234])-algebraic[261])+algebraic[284]
    algebraic[304] = (algebraic[226]+algebraic[234])-algebraic[238]
    algebraic[305] = algebraic[248]-algebraic[252]
    algebraic[306] = algebraic[252]+algebraic[254]+algebraic[257]
    algebraic[307] = -algebraic[257]
    algebraic[308] = algebraic[269]-algebraic[272]
    algebraic[309] = algebraic[272]-algebraic[275]
    algebraic[310] = algebraic[278]
    algebraic[291] = (log(10.0000)*constants[338]*(power(10.0000, -algebraic[0]-6.87000)))/(power(power(10.0000, -algebraic[0])+power(10.0000, -6.87000), 2.00000))+(log(10.0000)*constants[339]*(power(10.0000, -algebraic[0]-8.30000)))/(power(power(10.0000, -algebraic[0])+power(10.0000, -8.30000), 2.00000))+(log(10.0000)*constants[340]*(power(10.0000, -algebraic[0]-4.80000)))/(power(power(10.0000, -algebraic[0])+power(10.0000, -4.80000), 2.00000))
    algebraic[7] = ((power(10.0000, constants[149]))*(algebraic[1]-power(10.0000, -algebraic[0]+constants[149])))/(constants[134]*(power(algebraic[1], 2.00000)))
    algebraic[18] = ((power(10.0000, constants[159]))*(algebraic[12]-power(10.0000, -algebraic[0]+constants[159])))/(constants[134]*(power(algebraic[12], 2.00000)))
    algebraic[29] = ((power(10.0000, constants[169]))*(algebraic[23]-power(10.0000, -algebraic[0]+constants[169])))/(constants[134]*(power(algebraic[23], 2.00000)))
    algebraic[40] = ((power(10.0000, constants[177]))*(algebraic[35]-power(10.0000, -algebraic[0]+constants[177])))/(constants[134]*(power(algebraic[35], 2.00000)))
    algebraic[51] = ((power(10.0000, constants[186]))*(algebraic[45]-power(10.0000, -algebraic[0]+constants[186])))/(constants[134]*(power(algebraic[45], 2.00000)))
    algebraic[59] = ((power(10.0000, constants[189]))*(algebraic[55]-power(10.0000, -algebraic[0]+constants[189])))/(constants[134]*(power(algebraic[55], 2.00000)))
    algebraic[65] = ((power(10.0000, constants[195]))*(algebraic[60]-power(10.0000, -algebraic[0]+constants[195])))/(constants[134]*(power(algebraic[60], 2.00000)))
    algebraic[74] = ((power(10.0000, constants[199]))*(algebraic[70]-power(10.0000, -algebraic[0]+constants[199])))/(constants[134]*(power(algebraic[70], 2.00000)))
    algebraic[80] = ((power(10.0000, constants[202]))*(algebraic[76]-power(10.0000, -algebraic[0]+constants[202])))/(constants[134]*(power(algebraic[76], 2.00000)))
    algebraic[88] = (algebraic[82]*(power(10.0000, constants[205])+2.00000*(power(10.0000, -algebraic[0]+constants[205]+constants[206])))-(power(10.0000, -algebraic[0]+constants[205])+2.00000*(power(10.0000, -2.00000*algebraic[0]+constants[205]+constants[206])))*(power(10.0000, constants[205])+2.00000*(power(10.0000, -algebraic[0]+constants[205]+constants[206]))))/(constants[134]*(power(algebraic[82], 2.00000)))
    algebraic[97] = ((power(10.0000, constants[210]))*(algebraic[93]-power(10.0000, -algebraic[0]+constants[210])))/(constants[134]*(power(algebraic[93], 2.00000)))
    algebraic[104] = ((power(10.0000, constants[216]))*(algebraic[99]-power(10.0000, -algebraic[0]+constants[216])))/(constants[134]*(power(algebraic[99], 2.00000)))
    algebraic[114] = ((power(10.0000, constants[219]))*(algebraic[109]-power(10.0000, -algebraic[0]+constants[219])))/(constants[134]*(power(algebraic[109], 2.00000)))
    algebraic[123] = ((power(10.0000, constants[223]))*(algebraic[119]-power(10.0000, -algebraic[0]+constants[223])))/(constants[134]*(power(algebraic[119], 2.00000)))
    algebraic[129] = ((power(10.0000, constants[226]))*(algebraic[125]-power(10.0000, -algebraic[0]+constants[226])))/(constants[134]*(power(algebraic[125], 2.00000)))
    algebraic[137] = ((power(10.0000, constants[229]))*(algebraic[131]-power(10.0000, -algebraic[0]+constants[229])))/(constants[134]*(power(algebraic[131], 2.00000)))
    algebraic[148] = ((power(10.0000, constants[234]))*(algebraic[142]-power(10.0000, -algebraic[0]+constants[234])))/(constants[134]*(power(algebraic[142], 2.00000)))
    algebraic[157] = ((power(10.0000, constants[239]))*(algebraic[153]-power(10.0000, -algebraic[0]+constants[239])))/(constants[134]*(power(algebraic[153], 2.00000)))
    algebraic[164] = ((power(10.0000, constants[245]))*(algebraic[159]-power(10.0000, -algebraic[0]+constants[245])))/(constants[134]*(power(algebraic[159], 2.00000)))
    algebraic[292] = log(10.0000)*(power(10.0000, -algebraic[0]))*constants[134]*(1.00000+algebraic[7]*states[3]+algebraic[18]*states[10]+algebraic[29]*states[9]+algebraic[40]*states[5]+algebraic[51]*states[23]+algebraic[59]*states[22]+algebraic[65]*states[2]+algebraic[74]*states[6]+algebraic[80]*states[7]+algebraic[88]*states[8]+algebraic[97]*states[12]+algebraic[114]*states[11]+algebraic[104]*states[13]+algebraic[123]*states[16]+algebraic[129]*states[17]+algebraic[137]*states[18]+algebraic[148]*states[19]+algebraic[157]*states[20]+algebraic[164]*states[21])
    algebraic[294] = algebraic[293]/(algebraic[291]+algebraic[292])
    algebraic[8] = ((-(power(10.0000, -algebraic[0]))/constants[134])*(power(10.0000, constants[149]+constants[150])))/(power(algebraic[1], 2.00000))
    algebraic[19] = ((-(power(10.0000, -algebraic[0]))/constants[134])*(power(10.0000, constants[159]+constants[160])))/(power(algebraic[12], 2.00000))
    algebraic[31] = ((-(power(10.0000, -algebraic[0]))/constants[134])*(power(10.0000, constants[169]+constants[170])))/(power(algebraic[23], 2.00000))
    algebraic[41] = ((-(power(10.0000, -algebraic[0]))/constants[134])*(power(10.0000, constants[177]+constants[178])))/(power(algebraic[35], 2.00000))
    algebraic[52] = ((-(power(10.0000, -algebraic[0]))/constants[134])*(power(10.0000, constants[186]+constants[187])))/(power(algebraic[45], 2.00000))
    algebraic[66] = ((-(power(10.0000, -algebraic[0]))/constants[134])*(power(10.0000, constants[195]+constants[196])))/(power(algebraic[60], 2.00000))
    algebraic[89] = (-(power(10.0000, -algebraic[0]+constants[205])+2.00000*(power(10.0000, -2.00000*algebraic[0]+constants[205]+constants[206])))*(power(10.0000, constants[207])))/(constants[134]*(power(algebraic[82], 2.00000)))
    algebraic[105] = ((-(power(10.0000, -algebraic[0]))/constants[134])*(power(10.0000, constants[216]+constants[213])))/(power(algebraic[99], 2.00000))
    algebraic[115] = ((-(power(10.0000, -algebraic[0]))/constants[134])*(power(10.0000, constants[219]+constants[220])))/(power(algebraic[109], 2.00000))
    algebraic[138] = ((-(power(10.0000, -algebraic[0]))/constants[134])*(power(10.0000, constants[229]+constants[230])))/(power(algebraic[131], 2.00000))
    algebraic[149] = ((-(power(10.0000, -algebraic[0]))/constants[134])*(power(10.0000, constants[234]+constants[235])))/(power(algebraic[142], 2.00000))
    algebraic[165] = ((-(power(10.0000, -algebraic[0]))/constants[134])*(power(10.0000, constants[245]+constants[242])))/(power(algebraic[159], 2.00000))
    algebraic[295] = (algebraic[8]*states[3]+algebraic[19]*states[10]+algebraic[31]*states[9]+algebraic[41]*states[5]+algebraic[52]*states[23]+constants[26]*states[22]+algebraic[66]*states[2]+constants[27]*states[6]+constants[28]*states[7]+algebraic[89]*states[8]+constants[29]*states[12]+algebraic[115]*states[11]+algebraic[105]*states[13]+constants[30]*states[16]+constants[31]*states[17]+algebraic[138]*states[18]+algebraic[149]*states[19]+constants[32]*states[20]+algebraic[165]*states[21])/(algebraic[291]+algebraic[292])
    algebraic[10] = ((states[1]/constants[134])*(power(10.0000, -algebraic[0]+constants[149]+constants[150]))*log(10.0000))/(power(algebraic[1], 2.00000))
    algebraic[21] = ((states[1]/constants[134])*(power(10.0000, -algebraic[0]+constants[159]+constants[160]))*log(10.0000))/(power(algebraic[12], 2.00000))
    algebraic[33] = ((states[1]/constants[134])*(power(10.0000, -algebraic[0]+constants[169]+constants[170]))*log(10.0000))/(power(algebraic[23], 2.00000))
    algebraic[43] = ((states[1]/constants[134])*(power(10.0000, -algebraic[0]+constants[177]+constants[178]))*log(10.0000))/(power(algebraic[35], 2.00000))
    algebraic[54] = ((states[1]/constants[134])*(power(10.0000, -algebraic[0]+constants[186]+constants[187]))*log(10.0000))/(power(algebraic[45], 2.00000))
    algebraic[68] = ((states[1]/constants[134])*(power(10.0000, -algebraic[0]+constants[195]+constants[196]))*log(10.0000))/(power(algebraic[60], 2.00000))
    algebraic[91] = ((states[1]/constants[134])*(power(10.0000, constants[207]))*(algebraic[82]*(power(10.0000, -algebraic[0]+constants[205]))*log(10.0000)-(power(10.0000, -2.00000*algebraic[0]+constants[205]+constants[206]))*2.00000*log(10.0000)))/(power(algebraic[82], 2.00000))
    algebraic[107] = ((states[1]/constants[134])*(power(10.0000, -algebraic[0]+constants[216]+constants[213]))*log(10.0000))/(power(algebraic[99], 2.00000))
    algebraic[117] = ((states[1]/constants[134])*(power(10.0000, -algebraic[0]+constants[219]+constants[220]))*log(10.0000))/(power(algebraic[109], 2.00000))
    algebraic[140] = ((states[1]/constants[134])*(power(10.0000, -algebraic[0]+constants[229]+constants[230]))*log(10.0000))/(power(algebraic[131], 2.00000))
    algebraic[151] = ((states[1]/constants[134])*(power(10.0000, -algebraic[0]+constants[234]+constants[235]))*log(10.0000))/(power(algebraic[142], 2.00000))
    algebraic[167] = ((states[1]/constants[134])*(power(10.0000, -algebraic[0]+constants[245]+constants[242]))*log(10.0000))/(power(algebraic[159], 2.00000))
    algebraic[9] = ((algebraic[1]*(power(10.0000, constants[150])))/constants[134]-((states[1]/constants[134])*(power(10.0000, 2.00000*constants[150])))/constants[134])/(power(algebraic[1], 2.00000))
    algebraic[20] = ((algebraic[12]*(power(10.0000, constants[160])))/constants[134]-((states[1]/constants[134])*(power(10.0000, 2.00000*constants[160])))/constants[134])/(power(algebraic[12], 2.00000))
    algebraic[32] = ((algebraic[23]*(power(10.0000, constants[170])))/constants[134]-((states[1]/constants[134])*(power(10.0000, 2.00000*constants[170])))/constants[134])/(power(algebraic[23], 2.00000))
    algebraic[42] = ((algebraic[35]*(power(10.0000, constants[178])))/constants[134]-((states[1]/constants[134])*(power(10.0000, 2.00000*constants[178])))/constants[134])/(power(algebraic[35], 2.00000))
    algebraic[53] = ((algebraic[45]*(power(10.0000, constants[187])))/constants[134]-((states[1]/constants[134])*(power(10.0000, 2.00000*constants[187])))/constants[134])/(power(algebraic[45], 2.00000))
    algebraic[67] = ((algebraic[60]*(power(10.0000, constants[196])))/constants[134]-((states[1]/constants[134])*(power(10.0000, 2.00000*constants[196])))/constants[134])/(power(algebraic[60], 2.00000))
    algebraic[90] = ((algebraic[82]*(power(10.0000, constants[207])))/constants[134]-((states[1]/constants[134])*(power(10.0000, 2.00000*constants[207])))/constants[134])/(power(algebraic[82], 2.00000))
    algebraic[106] = ((algebraic[99]*(power(10.0000, constants[213])))/constants[134]-((states[1]/constants[134])*(power(10.0000, 2.00000*constants[213])))/constants[134])/(power(algebraic[99], 2.00000))
    algebraic[116] = ((algebraic[109]*(power(10.0000, constants[220])))/constants[134]-((states[1]/constants[134])*(power(10.0000, 2.00000*constants[220])))/constants[134])/(power(algebraic[109], 2.00000))
    algebraic[139] = ((algebraic[131]*(power(10.0000, constants[230])))/constants[134]-((states[1]/constants[134])*(power(10.0000, 2.00000*constants[230])))/constants[134])/(power(algebraic[131], 2.00000))
    algebraic[150] = ((algebraic[142]*(power(10.0000, constants[235])))/constants[134]-((states[1]/constants[134])*(power(10.0000, 2.00000*constants[235])))/constants[134])/(power(algebraic[142], 2.00000))
    algebraic[166] = ((algebraic[159]*(power(10.0000, constants[242])))/constants[134]-((states[1]/constants[134])*(power(10.0000, 2.00000*constants[242])))/constants[134])/(power(algebraic[159], 2.00000))
    algebraic[296] = -1.00000-(algebraic[20]*states[10]+algebraic[32]*states[9]+algebraic[42]*states[5]+algebraic[9]*states[3]+algebraic[53]*states[23]+algebraic[67]*states[2]+algebraic[90]*states[8]+algebraic[106]*states[13]+algebraic[116]*states[11]+algebraic[150]*states[19]+algebraic[139]*states[18]+algebraic[166]*states[21])
    algebraic[297] = (algebraic[21]*states[10]+algebraic[33]*states[9]+algebraic[43]*states[5]+algebraic[10]*states[3]+algebraic[54]*states[23]+algebraic[68]*states[2]+algebraic[91]*states[8]+algebraic[107]*states[13]+algebraic[117]*states[11]+algebraic[151]*states[19]+algebraic[140]*states[18]+algebraic[167]*states[21])/algebraic[296]
    algebraic[5] = (states[1]/constants[134])*(power(10.0000, constants[150]))*algebraic[2]
    algebraic[49] = (states[1]/constants[134])*(power(10.0000, constants[187]))*algebraic[46]
    algebraic[63] = ((algebraic[61]*states[1])/constants[134])*(power(10.0000, constants[196]))
    algebraic[86] = ((algebraic[83]*states[1])/constants[134])*(power(10.0000, constants[207]))
    algebraic[102] = ((algebraic[100]*states[1])/constants[134])*(power(10.0000, constants[213]))
    algebraic[112] = ((algebraic[110]*states[1])/constants[134])*(power(10.0000, constants[220]))
    algebraic[135] = ((algebraic[132]*states[1])/constants[134])*(power(10.0000, constants[230]))
    algebraic[146] = ((algebraic[143]*states[1])/constants[134])*(power(10.0000, constants[235]))
    algebraic[162] = (states[1]/constants[134])*(power(10.0000, constants[242]))*algebraic[160]
    algebraic[311] = (algebraic[15]*algebraic[300]+algebraic[26]*algebraic[301]+algebraic[38]*algebraic[302]+algebraic[5]*algebraic[303]+algebraic[49]*algebraic[299]+algebraic[63]*algebraic[304]+algebraic[86]*algebraic[305]+algebraic[102]*algebraic[307]+algebraic[112]*algebraic[306]+algebraic[146]*algebraic[309]+algebraic[135]*algebraic[308]+algebraic[162]*algebraic[310])/algebraic[296]
    algebraic[4] = (constants[133]/constants[134])*(power(10.0000, constants[144]))*algebraic[2]
    algebraic[30] = ((algebraic[28]+algebraic[6])-algebraic[17])+(((constants[171]+constants[151])-constants[162])-constants[253])
    algebraic[47] = (constants[133]/constants[134])*(power(10.0000, constants[181]))*algebraic[46]
    algebraic[134] = ((algebraic[132]*constants[133])/constants[134])*(power(10.0000, constants[231]))
    algebraic[145] = ((algebraic[143]*constants[133])/constants[134])*(power(10.0000, constants[236]))
    algebraic[175] = ((algebraic[34]+algebraic[11]+algebraic[173])-algebraic[172])-algebraic[22]
    algebraic[177] = (exp(-algebraic[175]/(constants[0]*constants[130]))*algebraic[23]*algebraic[1])/(algebraic[12]*(power(10.0000, -algebraic[0])))
    algebraic[280] = algebraic[184]*algebraic[238]+algebraic[181]*(algebraic[226]+algebraic[234])+algebraic[187]*algebraic[241]+algebraic[190]*algebraic[248]+algebraic[193]*algebraic[252]+algebraic[196]*algebraic[254]+algebraic[199]*algebraic[261]+algebraic[205]*algebraic[265]+algebraic[208]*algebraic[269]+algebraic[211]*algebraic[272]+algebraic[214]*algebraic[275]+algebraic[217]*algebraic[278]+algebraic[202]*algebraic[257]
    algebraic[288] = algebraic[174]*-algebraic[286]
    algebraic[298] = 1.00000-algebraic[297]*algebraic[295]
    return algebraic

def custom_piecewise(cases):
    """Compute result of a piecewise function"""
    return select(cases[0::2],cases[1::2])

def solve_model():
    """Solve model with ODE solver"""
    from scipy.integrate import ode
    # Initialise constants and state variables
    (init_states, constants) = initConsts()

    # Set timespan to solve over
    voi = linspace(0, 10, 500)

    # Construct ODE object to solve
    r = ode(computeRates)
    r.set_integrator('vode', method='bdf', atol=1e-06, rtol=1e-06, max_step=1)
    r.set_initial_value(init_states, voi[0])
    r.set_f_params(constants)

    # Solve model
    states = array([[0.0] * len(voi)] * sizeStates)
    states[:,0] = init_states
    for (i,t) in enumerate(voi[1:]):
        if r.successful():
            r.integrate(t)
            states[:,i+1] = r.y
        else:
            break

    # Compute algebraic variables
    algebraic = computeAlgebraic(constants, states, voi)
    return (voi, states, algebraic)

def plot_model(voi, states, algebraic):
    """Plot variables against variable of integration"""
    import pylab
    (legend_states, legend_algebraic, legend_voi, legend_constants) = createLegends()
    pylab.figure(1)
    pylab.plot(voi,vstack((states,algebraic)).T)
    pylab.xlabel(legend_voi)
    pylab.legend(legend_states + legend_algebraic, loc='best')
    pylab.show()

if __name__ == "__main__":
    (voi, states, algebraic) = solve_model()
    plot_model(voi, states, algebraic)


# =========================
# Auto-generated wrapper
# =========================
import numpy as np
from scipy.integrate import odeint


class Parameters:
    def __init__(self):
        self.R = 8.314e-3
        self.T1 = 298.15
        self.Par_97 = 1.00000
        self.Par_98 = 7.40000
        self.Par_1 = 0.0500000
        self.Par_2 = 0.400000
        self.Par_3 = 0.00170000
        self.Par_6 = 0.00470000
        self.Par_8 = 0.00270000
        self.Par_11 = 0.00460000
        self.Par_14 = 0.00740000
        self.Par_16 = 0.00266055
        self.Par_17 = 0.0200000
        self.Par_18 = 1.75052
        self.Par_31 = 0.00402000
        self.Par_33 = 0.00270000
        self.Par_34 = 0.000870000
        self.Par_35 = 6.00000e-05
        self.Par_36 = 0.0100000
        self.Par_37 = 0.0100000
        self.Par_38 = 13.0000
        self.Par_82 = 0.00390000
        self.Par_88 = 0.00000
        self.Par_89 = 0.000100000
        self.Par_95 = 0.00500000
        self.Par_100 = 29.0000
        self.dNavgCRdmg = 0.00000
        self.dNavgG6Pdmg = 0.00000
        self.dNavgF6Pdmg = 0.00000
        self.dNavgGAPdmg = 0.00000
        self.dNavg13DPGdmg = 0.00000
        self.dNavg3PGdmg = 0.00000
        self.dNavgPYRdmg = 0.00000
        self.fixmg = 1.00000
        self.Par_4 = 0.00400000
        self.Par_5 = 0.00200000/1.50000
        self.Par_7 = 0.000150000
        self.Par_9 = 0.0101000
        self.Par_10 = 0.000200000
        self.Par_12 = 0.0150000
        self.Par_13 = 0.00150000
        self.Par_15 = 0.00440000
        self.Par_19 = 0.480000
        self.Par_20 = 6.30000e-05
        self.Par_21 = 3.00000e-05
        self.Par_22 = 0.880000
        self.Par_23 = 0.000480000
        self.Par_24 = 0.000119000
        self.Par_25 = 0.0560000
        self.Par_26 = 0.000180000
        self.Par_27 = 0.0200000
        self.Par_28 = 8.00000e-05
        self.Par_29 = 0.000250000
        self.Par_30 = 0.00402000
        self.Par_32 = 0.00270000
        self.Par_39 = 0.0106591
        self.Par_40 = 5.00000e-05
        self.Par_41 = 0.00200000
        self.Par_42 = 0.00100000
        self.Par_43 = 12.0000
        self.Par_44 = 0.000320000
        self.Par_45 = 0.000610000
        self.Par_46 = 0.0825000
        self.Par_47 = 0.000180000
        self.Par_48 = 1.20000e-05
        self.Par_49 = 0.000220000
        self.Par_50 = 8.00000e-06
        self.Par_51 = 1.26500
        self.Par_52 = 2.50000e-06
        self.Par_53 = 9.00000e-05
        self.Par_54 = 0.000290000
        self.Par_55 = 8.00000e-07
        self.Par_56 = 3.30000e-06
        self.Par_57 = 1.12000
        self.Par_58 = 0.00200000
        self.Par_59 = 8.00000e-06
        self.Par_60 = 0.00120000
        self.Par_61 = 0.000350000
        self.Par_62 = 1.12000
        self.Par_63 = 0.000200000
        self.Par_64 = 1.40000e-05
        self.Par_65 = 0.192000
        self.Par_66 = 0.000100000
        self.Par_67 = 0.000370000
        self.Par_68 = 1.44000
        self.Par_69 = 8.00000e-05
        self.Par_70 = 0.000300000
        self.Par_71 = 0.00705000
        self.Par_72 = 0.00113000
        self.Par_73 = 1.92000
        self.Par_74 = 0.000335000
        self.Par_75 = 2.00000e-06
        self.Par_76 = 0.0170000
        self.Par_77 = 0.000849000
        self.Par_78 = 0.500000
        self.Par_79 = 0.00111000
        self.Par_80 = 0.00350000
        self.Par_81 = 0.000135000
        self.Par_83 = 0.00380000
        self.Par_84 = 0.880000
        self.Par_85 = 0.000320000
        self.Par_86 = 0.000270000
        self.Par_87 = 0.000350000
        self.Par_90 = 0.100000
        self.Par_91 = 0.0150000
        self.Par_92 = 0.0250000
        self.Par_93 = 0.0100000
        self.Par_94 = 303.150
        self.Par_96 = 0.0800000
        self.Par_99 = 1.00000
        self.c0 = 1.00000
        self.RT2dadT = 1.47750
        self.B = 1.60000
        self.I1 = 0.100000
        self.alphadebye = 1.17582
        self.RTalpha = 2.91482
        self.pKak_Pi = 0.500000
        self.deltaH1o_Pi = 3.00000
        self.deltaHmgo_Pi = -2.90000
        self.NH_HPi2 = 1.00000
        self.deltaGof_HPi2 = -1096.10
        self.deltaH1o_ATP = -5.00000
        self.deltaHmgo_ATP = -18.0000
        self.deltaHko_ATP = -1.00000
        self.NH_ATP4 = 12.0000
        self.deltaGof_ATP4 = -2768.10
        self.pKak_ADP = 1.00000
        self.deltaH1o_ADP = -3.00000
        self.deltaHmgo_ADP = -15.0000
        self.NH_ADP3 = 12.0000
        self.deltaGof_ADP3 = -1906.13
        self.deltaH1o_AMP = -3.00000
        self.deltaHmgo_AMP = -7.50000
        self.NH_AMP2 = 12.0000
        self.deltaGof_AMP2 = -1040.45
        self.pKak_PCR = 0.310000
        self.deltaH1o_PCR = 2.66000
        self.deltaHmgo_PCR = 8.19000
        self.NH_HPCR = 8.00000
        self.pKa1_CR = 2.30000
        self.NH_HCR = 9.00000
        self.deltaH1o_G1P = -1.70000
        self.deltaHmgo_G1P = -12.0000
        self.NH_UG1P = 11.0000
        self.deltaGof_UG1P = -1756.87
        self.pKa1_G6P = 6.11000
        self.NH_UG6P = 11.0000
        self.deltaGof_UG6P = -1763.94
        self.pKa1_F6P = 5.89000
        self.NH_UF6P = 11.0000
        self.deltaGof_UF6P = -1760.80
        self.pKa1_FDP = 6.40000
        self.pKa2_FDP = 5.92000
        self.pKamg_FDP = 2.70000
        self.NH_UFDP = 10.0000
        self.deltaGof_UFDP = -2601.40
        self.pKa1_GAP = 6.45000
        self.NH_UGAP = 5.00000
        self.deltaGof_UGAP = -1288.60
        self.pKamg_G3P = 1.63000
        self.deltaH1o_G3P = -3.10000
        self.NH_UG3P = 7.00000
        self.deltaGof_UG3P = -1339.25
        self.pKa1_DHAP = 5.90000
        self.pKamg_DHAP = 1.57000
        self.NH_UDHAP = 5.00000
        self.deltaGof_UDHAP = -1296.26
        self.pKa1_13DPG = 7.50000
        self.NH_U13DPG = 4.00000
        self.deltaGof_U13DPG = -2356.14
        self.pKa1_3PG = 6.21000
        self.NH_U3PG = 4.00000
        self.deltaGof_U3PG = -1502.54
        self.pKa1_2PG = 7.00000
        self.pKamg_2PG = 2.45000
        self.pKak_2PG = 1.18000
        self.NH_U2PG = 4.00000
        self.deltaGof_U2PG = -1496.38
        self.pKa1_PEP = 6.35000
        self.pKamg_PEP = 2.26000
        self.pKak_PEP = 1.08000
        self.NH_UPEP = 2.00000
        self.deltaGof_UPEP = -1263.65
        self.pKa1_PYR = 2.49000
        self.NH_UPYR = 3.00000
        self.deltaGof_UPYR = -472.270
        self.pKamg_LAC = 0.980000
        self.deltaH1o_LAC = -0.330000
        self.NH_ULAC = 5.00000
        self.deltaGof_ULAC = -516.720
        self.dNH_GLY = -10.0000
        self.NH_NAD = 26.0000
        self.deltaGof_NAD = 0.00000
        self.NH_NADH = 27.0000
        self.deltaGof_NADH = 22.6500
        self.NH_H2O = 2.00000
        self.deltaGof_H2O = -237.190
        self.NH_H = 1.00000
        self.deltaGof_H = 0.00000
        self.Kref_CK = 2.58000e+08
        self.deltaHo_CKo = -17.5500

    def to_dict(self):
        return {
            "R": self.R,
            "T1": self.T1,
            "Par_97": self.Par_97,
            "Par_98": self.Par_98,
            "Par_1": self.Par_1,
            "Par_2": self.Par_2,
            "Par_3": self.Par_3,
            "Par_6": self.Par_6,
            "Par_8": self.Par_8,
            "Par_11": self.Par_11,
            "Par_14": self.Par_14,
            "Par_16": self.Par_16,
            "Par_17": self.Par_17,
            "Par_18": self.Par_18,
            "Par_31": self.Par_31,
            "Par_33": self.Par_33,
            "Par_34": self.Par_34,
            "Par_35": self.Par_35,
            "Par_36": self.Par_36,
            "Par_37": self.Par_37,
            "Par_38": self.Par_38,
            "Par_82": self.Par_82,
            "Par_88": self.Par_88,
            "Par_89": self.Par_89,
            "Par_95": self.Par_95,
            "Par_100": self.Par_100,
            "dNavgCRdmg": self.dNavgCRdmg,
            "dNavgG6Pdmg": self.dNavgG6Pdmg,
            "dNavgF6Pdmg": self.dNavgF6Pdmg,
            "dNavgGAPdmg": self.dNavgGAPdmg,
            "dNavg13DPGdmg": self.dNavg13DPGdmg,
            "dNavg3PGdmg": self.dNavg3PGdmg,
            "dNavgPYRdmg": self.dNavgPYRdmg,
            "fixmg": self.fixmg,
            "Par_4": self.Par_4,
            "Par_5": self.Par_5,
            "Par_7": self.Par_7,
            "Par_9": self.Par_9,
            "Par_10": self.Par_10,
            "Par_12": self.Par_12,
            "Par_13": self.Par_13,
            "Par_15": self.Par_15,
            "Par_19": self.Par_19,
            "Par_20": self.Par_20,
            "Par_21": self.Par_21,
            "Par_22": self.Par_22,
            "Par_23": self.Par_23,
            "Par_24": self.Par_24,
            "Par_25": self.Par_25,
            "Par_26": self.Par_26,
            "Par_27": self.Par_27,
            "Par_28": self.Par_28,
            "Par_29": self.Par_29,
            "Par_30": self.Par_30,
            "Par_32": self.Par_32,
            "Par_39": self.Par_39,
            "Par_40": self.Par_40,
            "Par_41": self.Par_41,
            "Par_42": self.Par_42,
            "Par_43": self.Par_43,
            "Par_44": self.Par_44,
            "Par_45": self.Par_45,
            "Par_46": self.Par_46,
            "Par_47": self.Par_47,
            "Par_48": self.Par_48,
            "Par_49": self.Par_49,
            "Par_50": self.Par_50,
            "Par_51": self.Par_51,
            "Par_52": self.Par_52,
            "Par_53": self.Par_53,
            "Par_54": self.Par_54,
            "Par_55": self.Par_55,
            "Par_56": self.Par_56,
            "Par_57": self.Par_57,
            "Par_58": self.Par_58,
            "Par_59": self.Par_59,
            "Par_60": self.Par_60,
            "Par_61": self.Par_61,
            "Par_62": self.Par_62,
            "Par_63": self.Par_63,
            "Par_64": self.Par_64,
            "Par_65": self.Par_65,
            "Par_66": self.Par_66,
            "Par_67": self.Par_67,
            "Par_68": self.Par_68,
            "Par_69": self.Par_69,
            "Par_70": self.Par_70,
            "Par_71": self.Par_71,
            "Par_72": self.Par_72,
            "Par_73": self.Par_73,
            "Par_74": self.Par_74,
            "Par_75": self.Par_75,
            "Par_76": self.Par_76,
            "Par_77": self.Par_77,
            "Par_78": self.Par_78,
            "Par_79": self.Par_79,
            "Par_80": self.Par_80,
            "Par_81": self.Par_81,
            "Par_83": self.Par_83,
            "Par_84": self.Par_84,
            "Par_85": self.Par_85,
            "Par_86": self.Par_86,
            "Par_87": self.Par_87,
            "Par_90": self.Par_90,
            "Par_91": self.Par_91,
            "Par_92": self.Par_92,
            "Par_93": self.Par_93,
            "Par_94": self.Par_94,
            "Par_96": self.Par_96,
            "Par_99": self.Par_99,
            "c0": self.c0,
            "RT2dadT": self.RT2dadT,
            "B": self.B,
            "I1": self.I1,
            "alphadebye": self.alphadebye,
            "RTalpha": self.RTalpha,
            "pKak_Pi": self.pKak_Pi,
            "deltaH1o_Pi": self.deltaH1o_Pi,
            "deltaHmgo_Pi": self.deltaHmgo_Pi,
            "NH_HPi2": self.NH_HPi2,
            "deltaGof_HPi2": self.deltaGof_HPi2,
            "deltaH1o_ATP": self.deltaH1o_ATP,
            "deltaHmgo_ATP": self.deltaHmgo_ATP,
            "deltaHko_ATP": self.deltaHko_ATP,
            "NH_ATP4": self.NH_ATP4,
            "deltaGof_ATP4": self.deltaGof_ATP4,
            "pKak_ADP": self.pKak_ADP,
            "deltaH1o_ADP": self.deltaH1o_ADP,
            "deltaHmgo_ADP": self.deltaHmgo_ADP,
            "NH_ADP3": self.NH_ADP3,
            "deltaGof_ADP3": self.deltaGof_ADP3,
            "deltaH1o_AMP": self.deltaH1o_AMP,
            "deltaHmgo_AMP": self.deltaHmgo_AMP,
            "NH_AMP2": self.NH_AMP2,
            "deltaGof_AMP2": self.deltaGof_AMP2,
            "pKak_PCR": self.pKak_PCR,
            "deltaH1o_PCR": self.deltaH1o_PCR,
            "deltaHmgo_PCR": self.deltaHmgo_PCR,
            "NH_HPCR": self.NH_HPCR,
            "pKa1_CR": self.pKa1_CR,
            "NH_HCR": self.NH_HCR,
            "deltaH1o_G1P": self.deltaH1o_G1P,
            "deltaHmgo_G1P": self.deltaHmgo_G1P,
            "NH_UG1P": self.NH_UG1P,
            "deltaGof_UG1P": self.deltaGof_UG1P,
            "pKa1_G6P": self.pKa1_G6P,
            "NH_UG6P": self.NH_UG6P,
            "deltaGof_UG6P": self.deltaGof_UG6P,
            "pKa1_F6P": self.pKa1_F6P,
            "NH_UF6P": self.NH_UF6P,
            "deltaGof_UF6P": self.deltaGof_UF6P,
            "pKa1_FDP": self.pKa1_FDP,
            "pKa2_FDP": self.pKa2_FDP,
            "pKamg_FDP": self.pKamg_FDP,
            "NH_UFDP": self.NH_UFDP,
            "deltaGof_UFDP": self.deltaGof_UFDP,
            "pKa1_GAP": self.pKa1_GAP,
            "NH_UGAP": self.NH_UGAP,
            "deltaGof_UGAP": self.deltaGof_UGAP,
            "pKamg_G3P": self.pKamg_G3P,
            "deltaH1o_G3P": self.deltaH1o_G3P,
            "NH_UG3P": self.NH_UG3P,
            "deltaGof_UG3P": self.deltaGof_UG3P,
            "pKa1_DHAP": self.pKa1_DHAP,
            "pKamg_DHAP": self.pKamg_DHAP,
            "NH_UDHAP": self.NH_UDHAP,
            "deltaGof_UDHAP": self.deltaGof_UDHAP,
            "pKa1_13DPG": self.pKa1_13DPG,
            "NH_U13DPG": self.NH_U13DPG,
            "deltaGof_U13DPG": self.deltaGof_U13DPG,
            "pKa1_3PG": self.pKa1_3PG,
            "NH_U3PG": self.NH_U3PG,
            "deltaGof_U3PG": self.deltaGof_U3PG,
            "pKa1_2PG": self.pKa1_2PG,
            "pKamg_2PG": self.pKamg_2PG,
            "pKak_2PG": self.pKak_2PG,
            "NH_U2PG": self.NH_U2PG,
            "deltaGof_U2PG": self.deltaGof_U2PG,
            "pKa1_PEP": self.pKa1_PEP,
            "pKamg_PEP": self.pKamg_PEP,
            "pKak_PEP": self.pKak_PEP,
            "NH_UPEP": self.NH_UPEP,
            "deltaGof_UPEP": self.deltaGof_UPEP,
            "pKa1_PYR": self.pKa1_PYR,
            "NH_UPYR": self.NH_UPYR,
            "deltaGof_UPYR": self.deltaGof_UPYR,
            "pKamg_LAC": self.pKamg_LAC,
            "deltaH1o_LAC": self.deltaH1o_LAC,
            "NH_ULAC": self.NH_ULAC,
            "deltaGof_ULAC": self.deltaGof_ULAC,
            "dNH_GLY": self.dNH_GLY,
            "NH_NAD": self.NH_NAD,
            "deltaGof_NAD": self.deltaGof_NAD,
            "NH_NADH": self.NH_NADH,
            "deltaGof_NADH": self.deltaGof_NADH,
            "NH_H2O": self.NH_H2O,
            "deltaGof_H2O": self.deltaGof_H2O,
            "NH_H": self.NH_H,
            "deltaGof_H": self.deltaGof_H,
            "Kref_CK": self.Kref_CK,
            "deltaHo_CKo": self.deltaHo_CKo,
        }

    @classmethod
    def from_dict(cls, data):
        p = cls()
        for key, value in data.items():
            if hasattr(p, key):
                setattr(p, key, value)
        return p


class Config:
    def __init__(
        self,
        param: Parameters = None,
        calculate: bool = False,
        T: int = 100,
        T_unit: float = 0.01,
        y0=[7.8, 5.132658807e-4, 1e-9, 0.03, 0.04, 1e-9, 1e-9, 1e-9, 1e-9, 1e-9, 0.005, 1e-9, 1e-9, 1e-9, 0.0005, 1e-9, 1e-9, 1e-9, 1e-9, 1e-9, 1e-9, 1e-9, 0.029999999, 1e-9, 0],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "vinnakota_kemp_kushmeric_2006_exp29frA40"
        self.curve_names = [
            "pH_calc",
            "Mg",
            "G1P",
            "Pi",
            "Gly",
            "AMP",
            "G6P",
            "F6P",
            "FBP",
            "ADP",
            "ATP",
            "DHAP",
            "GAP",
            "G3P",
            "NAD",
            "NADH",
            "BPG",
            "P3G",
            "P2G",
            "PEP",
            "PYR",
            "LAC",
            "Cr",
            "PCr",
            "protonload",
        ]
        self.state_names = ['pH_calc', 'Mg', 'G1P', 'Pi', 'Gly', 'AMP', 'G6P', 'F6P', 'FBP', 'ADP', 'ATP', 'DHAP', 'GAP', 'G3P', 'NAD', 'NADH', 'BPG', 'P3G', 'P2G', 'PEP', 'PYR', 'LAC', 'Cr', 'PCr', 'protonload']
        self.algebraic_names = ['pH_cy', 'P_Pi', 'HPi2', 'H2Pi1', 'kPi', 'mgPi', 'Navg_Pi', 'dNavgPidH', 'dNavgPidmg', 'dmgPidmg', 'dmgPidpH', 'deltaGpof_HPi2', 'P_ATP', 'ATP4', 'HATP3', 'mgATP2', 'kATP', 'Navg_ATP', 'dNavgATPdH', 'dNavgATPdmg', 'dmgATP2dmg', 'dmgATP2dpH', 'deltaGpof_ATP4', 'P_ADP', 'ADP3', 'HADP2', 'mgADP', 'kADP', 'Navg_ADP', 'dNavgADPdH', 'deltaH_ATPase', 'dNavgADPdmg', 'dmgADPdmg', 'dmgADPdpH', 'deltaGpof_ADP3', 'P_AMP', 'AMP2', 'HAMP1', 'mgAMP', 'Navg_AMP', 'dNavgAMPdH', 'dNavgAMPdmg', 'dmgAMPdmg', 'dmgAMPdpH', 'deltaGpof_AMP2', 'P_PCR', 'HPCR', 'kPCR', 'H2PCR', 'mgPCR', 'Navg_PCR', 'dNavgPCRdH', 'dNavgPCRdmg', 'dmgPCRdmg', 'dmgPCRdpH', 'P_CR', 'HCR', 'H2CR', 'Navg_CR', 'dNavgCRdH', 'P_G1P', 'UG1P', 'HG1P', 'mgG1P', 'Navg_G1P', 'dNavgG1PdH', 'dNavgG1Pdmg', 'dmgG1Pdmg', 'dmgG1PdpH', 'deltaGpof_UG1P', 'P_G6P', 'UG6P', 'HG6P', 'Navg_G6P', 'dNavgG6PdH', 'deltaGpof_UG6P', 'P_F6P', 'UF6P', 'HF6P', 'Navg_F6P', 'dNavgF6PdH', 'deltaGpof_UF6P', 'P_FDP', 'UFDP', 'HFDP', 'H2FDP', 'mgFDP', 'Navg_FDP', 'dNavgFDPdH', 'dNavgFDPdmg', 'dmgFDPdmg', 'dmgFDPdpH', 'deltaGpof_UFDP', 'P_GAP', 'UGAP', 'HGAP', 'Navg_GAP', 'dNavgGAPdH', 'deltaGpof_UGAP', 'P_G3P', 'UG3P', 'HG3P', 'mgG3P', 'Navg_G3P', 'dNavgG3PdH', 'dNavgG3Pdmg', 'dmgG3Pdmg', 'dmgG3PdpH', 'deltaGpof_UG3P', 'P_DHAP', 'UDHAP', 'HDHAP', 'mgDHAP', 'Navg_DHAP', 'dNavgDHAPdH', 'dNavgDHAPdmg', 'dmgDHAPdmg', 'dmgDHAPdpH', 'deltaGpof_UDHAP', 'P_13DPG', 'U13DPG', 'H13DPG', 'Navg_13DPG', 'dNavg13DPGdH', 'deltaGpof_U13DPG', 'P_3PG', 'U3PG', 'H3PG', 'Navg_3PG', 'dNavg3PGdH', 'deltaGpof_U3PG', 'P_2PG', 'U2PG', 'H2PG', 'k2PG', 'mg2PG', 'Navg_2PG', 'dNavg2PGdH', 'dNavg2PGdmg', 'dmg2PGdmg', 'dmg2PGdpH', 'deltaGpof_U2PG', 'P_PEP', 'UPEP', 'HPEP', 'kPEP', 'mgPEP', 'Navg_PEP', 'dNavgPEPdH', 'dNavgPEPdmg', 'dmgPEPdmg', 'dmgPEPdpH', 'deltaGpof_UPEP', 'P_PYR', 'UPYR', 'HPYR', 'Navg_PYR', 'dNavgPYRdH', 'deltaGpof_UPYR', 'P_LAC', 'ULAC', 'HLAC', 'mgLAC', 'Navg_LAC', 'dNavgLACdH', 'dNavgLACdmg', 'dmgLACdmg', 'dmgLACdpH', 'deltaGpof_ULAC', 'deltaGpo_GLY', 'deltaGpof_NAD', 'deltaGpof_NADH', 'deltaGpof_H2O', 'deltaGpof_H', 'deltaH_CK', 'deltaGpo_ATPase', 'Kapp_CK', 'Kapp_ATPase', 'deltaH_ADK', 'deltaGpo_ADK', 'Kapp_ADK', 'deltaH_GP', 'deltaGpo_GP', 'Kapp_GP', 'deltaH_PGLM', 'deltaGpo_PGLM', 'Kapp_PGLM', 'deltaH_PGI', 'deltaGpo_PGI', 'Kapp_PGI', 'deltaH_PFK', 'deltaGpo_PFK', 'Kapp_PFK', 'deltaH_ALD', 'deltaGpo_ALD', 'Kapp_ALD', 'deltaH_TPI', 'deltaGpo_TPI', 'Kapp_TPI', 'deltaH_GAPDH', 'deltaGpo_GAPDH', 'Kapp_GAPDH', 'deltaH_G3PDH', 'deltaGpo_G3PDH', 'Kapp_G3PDH', 'deltaH_PGK', 'deltaGpo_PGK', 'Kapp_PGK', 'deltaH_PGM', 'deltaGpo_PGM', 'Kapp_PGM', 'deltaH_ENOL', 'deltaGpo_ENOL', 'Kapp_ENOL', 'deltaH_PK', 'deltaGpo_PK', 'Kapp_PK', 'deltaH_LDH', 'deltaGpo_LDH', 'Kapp_LDH', 'fracA', 'Dglya', 'pa', 'VbglyA', 'glyAF', 'glyAR', 'flux_GPa', 'fracB', 'M', 'Dglyb', 'pb', 'VbglyB', 'glyBF', 'glyBR', 'flux_GPb', 'Vfpglm', 'dGlydt', 'Vbpglm', 'v_PGLM', 'Vbpgi', 'Vfpgi', 'v_PGI', 'Vfpfk', 'dG6Pdt', 'Vbpfk', 'L', 'Delta', 'Deltap', 'v_PFK', 'Vfald', 'dF6Pdt', 'Vbald', 'v_ALD', 'Vbtpi', 'v_TPI', 'Dg3pdh', 'Vfg3pdh', 'v_G3PDH', 'Dgap', 'Vfgad', 'Vbgad', 'v_GAPDH', 'Vfpgk', 'dGAPdt', 'D_PGK', 'v_PGK', 'Vfpgm', 'dBGPdt', 'Vbpgm', 'v_PGM', 'Vben', 'dP3Gdt', 'v_ENOL', 'Vfpk', 'Vbpk', 'v_PK', 'Vfldh', 'Vbldh', 'v_LDH', 'VmaxATPase', 'glycprtflux', 'dNADdt', 'dNADHdt', 'dPYRdt', 'ATPase', 'VrevCK', 'CK', 'Vbadk', 'CKprtflux', 'dCrdt', 'ADK', 'bufcapfixed', 'bufcapmetab', 'protons_consumed', 'pHODEterm1', 'pHODEterm2', 'denom_mgODE', 'RHSterm1_mgODE', 'denomMgpHODE', 'dPCrdt', 'dATPdt', 'dADPdt', 'dAMPdt', 'dPidt', 'dG1Pdt', 'dFBPdt', 'dDHAPdt', 'dG3Pdt', 'dP2Gdt', 'dPEPdt', 'dLACdt', 'RHSterm2_mgODE']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 342
        p = self.params

        # direct mapping
        c[0] = p.R
        c[1] = p.T1
        c[2] = p.Par_97
        c[3] = p.Par_98
        c[4] = p.Par_1
        c[5] = p.Par_2
        c[6] = p.Par_3
        c[7] = p.Par_6
        c[8] = p.Par_8
        c[9] = p.Par_11
        c[10] = p.Par_14
        c[11] = p.Par_16
        c[12] = p.Par_17
        c[13] = p.Par_18
        c[14] = p.Par_31
        c[15] = p.Par_33
        c[16] = p.Par_34
        c[17] = p.Par_35
        c[18] = p.Par_36
        c[19] = p.Par_37
        c[20] = p.Par_38
        c[21] = p.Par_82
        c[22] = p.Par_88
        c[23] = p.Par_89
        c[24] = p.Par_95
        c[25] = p.Par_100
        c[26] = p.dNavgCRdmg
        c[27] = p.dNavgG6Pdmg
        c[28] = p.dNavgF6Pdmg
        c[29] = p.dNavgGAPdmg
        c[30] = p.dNavg13DPGdmg
        c[31] = p.dNavg3PGdmg
        c[32] = p.dNavgPYRdmg
        c[33] = p.fixmg
        c[36] = p.Par_4
        c[56] = p.Par_5
        c[57] = p.Par_7
        c[58] = p.Par_9
        c[59] = p.Par_10
        c[60] = p.Par_12
        c[61] = p.Par_13
        c[62] = p.Par_15
        c[63] = p.Par_19
        c[64] = p.Par_20
        c[65] = p.Par_21
        c[66] = p.Par_22
        c[67] = p.Par_23
        c[68] = p.Par_24
        c[69] = p.Par_25
        c[70] = p.Par_26
        c[71] = p.Par_27
        c[72] = p.Par_28
        c[73] = p.Par_29
        c[74] = p.Par_30
        c[75] = p.Par_32
        c[76] = p.Par_39
        c[77] = p.Par_40
        c[78] = p.Par_41
        c[79] = p.Par_42
        c[80] = p.Par_43
        c[81] = p.Par_44
        c[82] = p.Par_45
        c[83] = p.Par_46
        c[84] = p.Par_47
        c[85] = p.Par_48
        c[86] = p.Par_49
        c[87] = p.Par_50
        c[88] = p.Par_51
        c[89] = p.Par_52
        c[90] = p.Par_53
        c[91] = p.Par_54
        c[92] = p.Par_55
        c[93] = p.Par_56
        c[94] = p.Par_57
        c[95] = p.Par_58
        c[96] = p.Par_59
        c[97] = p.Par_60
        c[98] = p.Par_61
        c[99] = p.Par_62
        c[100] = p.Par_63
        c[101] = p.Par_64
        c[102] = p.Par_65
        c[103] = p.Par_66
        c[104] = p.Par_67
        c[105] = p.Par_68
        c[106] = p.Par_69
        c[107] = p.Par_70
        c[108] = p.Par_71
        c[109] = p.Par_72
        c[110] = p.Par_73
        c[111] = p.Par_74
        c[112] = p.Par_75
        c[113] = p.Par_76
        c[114] = p.Par_77
        c[115] = p.Par_78
        c[116] = p.Par_79
        c[117] = p.Par_80
        c[118] = p.Par_81
        c[119] = p.Par_83
        c[120] = p.Par_84
        c[121] = p.Par_85
        c[122] = p.Par_86
        c[123] = p.Par_87
        c[124] = p.Par_90
        c[126] = p.Par_91
        c[127] = p.Par_92
        c[128] = p.Par_93
        c[129] = p.Par_94
        c[131] = p.Par_96
        c[132] = p.Par_99
        c[134] = p.c0
        c[135] = p.RT2dadT
        c[136] = p.B
        c[138] = p.I1
        c[139] = p.alphadebye
        c[142] = p.RTalpha
        c[144] = p.pKak_Pi
        c[145] = p.deltaH1o_Pi
        c[146] = p.deltaHmgo_Pi
        c[151] = p.NH_HPi2
        c[152] = p.deltaGof_HPi2
        c[153] = p.deltaH1o_ATP
        c[154] = p.deltaHmgo_ATP
        c[155] = p.deltaHko_ATP
        c[162] = p.NH_ATP4
        c[163] = p.deltaGof_ATP4
        c[164] = p.pKak_ADP
        c[165] = p.deltaH1o_ADP
        c[166] = p.deltaHmgo_ADP
        c[171] = p.NH_ADP3
        c[172] = p.deltaGof_ADP3
        c[173] = p.deltaH1o_AMP
        c[174] = p.deltaHmgo_AMP
        c[179] = p.NH_AMP2
        c[180] = p.deltaGof_AMP2
        c[181] = p.pKak_PCR
        c[182] = p.deltaH1o_PCR
        c[183] = p.deltaHmgo_PCR
        c[188] = p.NH_HPCR
        c[189] = p.pKa1_CR
        c[190] = p.NH_HCR
        c[191] = p.deltaH1o_G1P
        c[192] = p.deltaHmgo_G1P
        c[197] = p.NH_UG1P
        c[198] = p.deltaGof_UG1P
        c[199] = p.pKa1_G6P
        c[200] = p.NH_UG6P
        c[201] = p.deltaGof_UG6P
        c[202] = p.pKa1_F6P
        c[203] = p.NH_UF6P
        c[204] = p.deltaGof_UF6P
        c[205] = p.pKa1_FDP
        c[206] = p.pKa2_FDP
        c[207] = p.pKamg_FDP
        c[208] = p.NH_UFDP
        c[209] = p.deltaGof_UFDP
        c[210] = p.pKa1_GAP
        c[211] = p.NH_UGAP
        c[212] = p.deltaGof_UGAP
        c[213] = p.pKamg_G3P
        c[214] = p.deltaH1o_G3P
        c[217] = p.NH_UG3P
        c[218] = p.deltaGof_UG3P
        c[219] = p.pKa1_DHAP
        c[220] = p.pKamg_DHAP
        c[221] = p.NH_UDHAP
        c[222] = p.deltaGof_UDHAP
        c[223] = p.pKa1_13DPG
        c[224] = p.NH_U13DPG
        c[225] = p.deltaGof_U13DPG
        c[226] = p.pKa1_3PG
        c[227] = p.NH_U3PG
        c[228] = p.deltaGof_U3PG
        c[229] = p.pKa1_2PG
        c[230] = p.pKamg_2PG
        c[231] = p.pKak_2PG
        c[232] = p.NH_U2PG
        c[233] = p.deltaGof_U2PG
        c[234] = p.pKa1_PEP
        c[235] = p.pKamg_PEP
        c[236] = p.pKak_PEP
        c[237] = p.NH_UPEP
        c[238] = p.deltaGof_UPEP
        c[239] = p.pKa1_PYR
        c[240] = p.NH_UPYR
        c[241] = p.deltaGof_UPYR
        c[242] = p.pKamg_LAC
        c[243] = p.deltaH1o_LAC
        c[246] = p.NH_ULAC
        c[247] = p.deltaGof_ULAC
        c[248] = p.dNH_GLY
        c[249] = p.NH_NAD
        c[250] = p.deltaGof_NAD
        c[251] = p.NH_NADH
        c[252] = p.deltaGof_NADH
        c[253] = p.NH_H2O
        c[254] = p.deltaGof_H2O
        c[255] = p.NH_H
        c[256] = p.deltaGof_H
        c[257] = p.Kref_CK
        c[258] = p.deltaHo_CKo

        # derived constants
        c[34] = c[2]
        c[35] = c[3]
        c[37] = c[24]
        c[38] = c[25]
        c[39] = c[6]
        c[40] = c[7]
        c[41] = c[8]
        c[42] = c[9]
        c[43] = c[10]
        c[44] = c[11]
        c[45] = c[12]
        c[46] = c[13]
        c[47] = c[14]
        c[48] = c[15]
        c[49] = c[16]
        c[50] = c[17]
        c[51] = c[18]
        c[52] = c[19]
        c[53] = c[20]
        c[54] = c[23]
        c[55] = c[21]
        c[125] = c[124]
        c[130] = c[129]
        c[133] = c[131]
        c[137] = (c[135]*(power(c[125], 1.0/2)))/(1.00000+c[136]*(power(c[125], 1.0/2)))
        c[140] = (1.00000*c[139]*((power(c[138], 1.0/2))/(1.00000+c[136]*(power(c[138], 1.0/2)))-(power(c[125], 1.0/2))/(1.00000+c[136]*(power(c[125], 1.0/2)))))/log(10.0000)
        c[141] = (1.00000/c[130]-1.00000/c[1])/(log(10.0000)*c[0])
        c[143] = (c[142]*(power(c[125], 1.0/2)))/(1.00000+c[136]*(power(c[125], 1.0/2)))
        c[147] = c[145]+c[137]*((power(2.00000, 2.00000)+power(1.00000, 2.00000))-power(1.00000, 2.00000))
        c[148] = c[146]+c[137]*((power(2.00000, 2.00000)+power(2.00000, 2.00000))-power(0.00000, 2.00000))
        c[149] = 6.75000+(c[140]/1.00000)*((power(2.00000, 2.00000)+power(1.00000, 2.00000))-power(1.00000, 2.00000))+c[141]*c[147]
        c[150] = 1.65000+(c[140]/1.00000)*((power(2.00000, 2.00000)+power(1.00000, 2.00000))-power(1.00000, 2.00000))+c[141]*c[148]
        c[156] = c[153]+c[137]*((power(4.00000, 2.00000)+power(1.00000, 2.00000))-power(3.00000, 2.00000))
        c[157] = c[154]+c[137]*((power(4.00000, 2.00000)+power(2.00000, 2.00000))-power(2.00000, 2.00000))
        c[158] = c[155]+c[137]*((power(4.00000, 2.00000)+power(1.00000, 2.00000))-power(3.00000, 2.00000))
        c[159] = 6.48000+(c[140]/1.00000)*((power(4.00000, 2.00000)+power(1.00000, 2.00000))-power(3.00000, 2.00000))+c[141]*c[156]
        c[160] = 4.19000+(c[140]/1.00000)*((power(4.00000, 2.00000)+power(2.00000, 2.00000))-power(2.00000, 2.00000))+c[141]*c[157]
        c[161] = 1.17000+(c[140]/1.00000)*((power(4.00000, 2.00000)+power(1.00000, 2.00000))-power(3.00000, 2.00000))+c[141]*c[158]
        c[167] = c[165]+c[137]*((power(3.00000, 2.00000)+power(1.00000, 2.00000))-power(2.00000, 2.00000))
        c[168] = c[166]+c[137]*((power(3.00000, 2.00000)+power(2.00000, 2.00000))-power(1.00000, 2.00000))
        c[169] = 6.38000+(c[140]/1.00000)*((power(3.00000, 2.00000)+power(1.00000, 2.00000))-power(2.00000, 2.00000))+c[141]*c[167]
        c[170] = 3.25000+(c[140]/1.00000)*((power(3.00000, 2.00000)+power(2.00000, 2.00000))-power(1.00000, 2.00000))+c[141]*c[168]
        c[175] = c[173]+c[137]*((power(2.00000, 2.00000)+power(1.00000, 2.00000))-power(1.00000, 2.00000))
        c[176] = c[174]+c[137]*((power(2.00000, 2.00000)+power(2.00000, 2.00000))-power(0.00000, 2.00000))
        c[177] = 6.29000+(c[140]/1.00000)*((power(2.00000, 2.00000)+power(1.00000, 2.00000))-power(1.00000, 2.00000))+c[141]*c[175]
        c[178] = 1.92000+(c[140]/1.00000)*((power(2.00000, 2.00000)+power(2.00000, 2.00000))-power(0.00000, 2.00000))+c[141]*c[176]
        c[184] = c[182]+c[137]*((power(2.00000, 2.00000)+power(1.00000, 2.00000))-power(1.00000, 2.00000))
        c[185] = c[183]+c[137]*((power(2.00000, 2.00000)+power(2.00000, 2.00000))-power(0.00000, 2.00000))
        c[186] = 4.50000+(c[140]/1.00000)*((power(2.00000, 2.00000)+power(1.00000, 2.00000))-power(1.00000, 2.00000))+c[141]*c[184]
        c[187] = 1.60000+(c[140]/1.00000)*((power(2.00000, 2.00000)+power(2.00000, 2.00000))-power(0.00000, 2.00000))+c[141]*c[185]
        c[193] = c[191]+c[137]*((power(2.00000, 2.00000)+power(1.00000, 2.00000))-power(1.00000, 2.00000))
        c[194] = c[192]+c[137]*((power(2.00000, 2.00000)+power(2.00000, 2.00000))-power(0.00000, 2.00000))
        c[195] = 6.09000+(c[140]/1.00000)*((power(2.00000, 2.00000)+power(1.00000, 2.00000))-power(1.00000, 2.00000))+c[141]*c[193]
        c[196] = 2.48000+(c[140]/1.00000)*((power(2.00000, 2.00000)+power(2.00000, 2.00000))-power(0.00000, 2.00000))+c[141]*c[194]
        c[215] = c[214]+c[137]*((power(2.00000, 2.00000)+power(1.00000, 2.00000))-power(1.00000, 2.00000))
        c[216] = 6.22000+(c[140]/1.00000)*((power(2.00000, 2.00000)+power(1.00000, 2.00000))-power(1.00000, 2.00000))+c[141]*c[215]
        c[244] = c[243]+c[137]*((power(1.00000, 2.00000)+power(1.00000, 2.00000))-power(0.00000, 2.00000))
        c[245] = 3.67000+(c[140]/1.00000)*((power(1.00000, 2.00000)+power(1.00000, 2.00000))-power(0.00000, 2.00000))+c[141]*c[244]
        c[259] = c[258]+c[137]*(((power(2.00000, 2.00000)+power(3.00000, 2.00000)+power(1.00000, 2.00000))-power(4.00000, 2.00000))-power(0.00000, 2.00000))
        c[260] = exp(log(c[257])+(c[139]*(power(c[125], 1.0/2))*(((power(2.00000, 2.00000)+power(3.00000, 2.00000)+power(1.00000, 2.00000))-power(4.00000, 2.00000))-power(0.00000, 2.00000)))/(1.00000+c[136]*(power(c[125], 1.0/2))))
        c[261] = power(10.0000, log(c[260], 10)-c[141]*c[259])
        c[262] = -c[0]*c[130]*log(c[261])
        c[263] = c[4]
        c[264] = c[36]
        c[265] = c[56]
        c[266] = c[57]
        c[267] = c[58]
        c[268] = c[59]
        c[269] = c[60]
        c[270] = c[61]
        c[271] = c[62]
        c[272] = c[63]
        c[273] = c[64]
        c[274] = c[65]
        c[275] = c[66]
        c[276] = c[67]
        c[277] = c[68]
        c[278] = c[69]
        c[279] = c[70]
        c[280] = c[71]
        c[281] = c[72]
        c[282] = c[74]
        c[283] = c[73]
        c[284] = c[75]
        c[285] = (c[279]*c[281])/(c[280]*c[283])
        c[286] = c[76]
        c[287] = c[77]
        c[288] = c[78]
        c[289] = c[79]
        c[290] = c[80]
        c[291] = c[81]
        c[292] = c[82]
        c[293] = c[290]
        c[294] = c[83]
        c[295] = c[84]
        c[296] = c[85]
        c[297] = c[86]
        c[298] = c[87]
        c[299] = c[294]
        c[300] = c[88]
        c[301] = c[89]
        c[302] = c[90]
        c[303] = c[91]
        c[304] = c[92]
        c[305] = c[93]
        c[306] = c[94]
        c[307] = c[95]
        c[308] = c[96]
        c[309] = c[97]
        c[310] = c[98]
        c[311] = c[306]
        c[312] = c[99]
        c[313] = c[100]
        c[314] = c[101]
        c[315] = c[102]
        c[316] = c[103]
        c[317] = c[104]
        c[318] = c[315]
        c[319] = c[105]
        c[320] = c[106]
        c[321] = c[107]
        c[322] = c[108]
        c[323] = c[109]
        c[324] = c[110]
        c[325] = c[111]
        c[326] = c[112]
        c[327] = c[113]
        c[328] = c[114]
        c[329] = c[115]
        c[330] = c[116]
        c[331] = c[117]
        c[332] = c[118]
        c[333] = c[119]
        c[334] = c[120]
        c[335] = c[121]
        c[336] = c[122]
        c[337] = c[123]
        c[338] = c[127]
        c[339] = c[126]
        c[340] = c[128]
        c[341] = c[132]

        return np.asarray(c, dtype=float)

    def pend(self, y, t):
        constants = self._build_constants()
        return np.asarray(
            computeRates(t, list(np.asarray(y, dtype=float)), constants),
            dtype=float,
        )

    def algebraic(self, y, t=0.0):
        if "computeAlgebraic" not in globals():
            raise AttributeError("computeAlgebraic is not defined in this module")

        alg = computeAlgebraic(
            self._build_constants(),
            np.asarray(y, dtype=float).reshape(-1, 1),
            np.asarray([t], dtype=float),
        )
        return np.asarray(alg, dtype=float)[:, 0]
