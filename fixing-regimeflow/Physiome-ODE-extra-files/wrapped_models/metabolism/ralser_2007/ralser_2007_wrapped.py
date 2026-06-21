# Size of variable arrays:
sizeAlgebraic = 32
sizeStates = 24
sizeConstants = 142
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (minute)"
    legend_constants[0] = "k_rel_TPI in component parameters (dimensionless)"
    legend_constants[1] = "k_rel_GAPDH in component parameters (dimensionless)"
    legend_constants[2] = "SUMAXP in component parameters (mM)"
    legend_constants[3] = "CO2 in component extracellular (mM)"
    legend_constants[4] = "ETOH in component extracellular (mM)"
    legend_constants[5] = "SUCC in component extracellular (mM)"
    legend_constants[6] = "GLY in component extracellular (mM)"
    legend_constants[7] = "GLCo in component extracellular (mM)"
    legend_constants[8] = "cytoplasm in component cytoplasm (liter)"
    legend_states[0] = "P in component cytoplasm (mM)"
    legend_states[1] = "G6P in component cytoplasm (mM)"
    legend_states[2] = "F6P in component cytoplasm (mM)"
    legend_states[3] = "F16P in component cytoplasm (mM)"
    legend_states[4] = "NADH in component cytoplasm (mM)"
    legend_states[5] = "NAD in component cytoplasm (mM)"
    legend_states[6] = "BPG in component cytoplasm (mM)"
    legend_states[7] = "P3G in component cytoplasm (mM)"
    legend_states[8] = "P2G in component cytoplasm (mM)"
    legend_states[9] = "PEP in component cytoplasm (mM)"
    legend_states[10] = "PYR in component cytoplasm (mM)"
    legend_states[11] = "ACE in component cytoplasm (mM)"
    legend_constants[9] = "X in component cytoplasm (mM)"
    legend_states[12] = "GA3P in component cytoplasm (mM)"
    legend_states[13] = "DHAP in component cytoplasm (mM)"
    legend_states[14] = "D6PGluconoLactone in component cytoplasm (mM)"
    legend_states[15] = "D6PGluconate in component cytoplasm (mM)"
    legend_states[16] = "NADP in component cytoplasm (mM)"
    legend_states[17] = "NADPH in component cytoplasm (mM)"
    legend_states[18] = "Ribulose5P in component cytoplasm (mM)"
    legend_states[19] = "Ribose5P in component cytoplasm (mM)"
    legend_states[20] = "Xyl5P in component cytoplasm (mM)"
    legend_states[21] = "Seduhept7P in component cytoplasm (mM)"
    legend_states[22] = "Erythrose4P in component cytoplasm (mM)"
    legend_states[23] = "GLCi in component cytoplasm (mM)"
    legend_constants[10] = "F26BP in component cytoplasm (mM)"
    legend_algebraic[0] = "vGLK in component vGLK (mmol_per_min)"
    legend_algebraic[2] = "vPGI in component vPGI (mmol_per_min)"
    legend_algebraic[10] = "vPFK in component vPFK (mmol_per_min)"
    legend_algebraic[11] = "vALD in component vALD (mmol_per_min)"
    legend_algebraic[12] = "vG3PDH in component vG3PDH (mmol_per_min)"
    legend_algebraic[13] = "vGAPDH in component vGAPDH (mmol_per_min)"
    legend_algebraic[14] = "vPGK in component vPGK (mmol_per_min)"
    legend_algebraic[16] = "vPGM in component vPGM (mmol_per_min)"
    legend_algebraic[18] = "vENO in component vENO (mmol_per_min)"
    legend_algebraic[20] = "vPYK in component vPYK (mmol_per_min)"
    legend_algebraic[22] = "vPDC in component vPDC (mmol_per_min)"
    legend_algebraic[26] = "vSUC in component vSUC (mmol_per_min)"
    legend_algebraic[28] = "vADH in component vADH (mmol_per_min)"
    legend_algebraic[23] = "vATP in component vATP (mmol_per_min)"
    legend_algebraic[15] = "vTPI in component vTPI (mmol_per_min)"
    legend_algebraic[17] = "vG6PDH in component vG6PDH (mmol_per_min)"
    legend_algebraic[19] = "v6PGL in component v6PGL (mmol_per_min)"
    legend_algebraic[21] = "vGluDH in component vGluDH (mmol_per_min)"
    legend_algebraic[24] = "vPPI in component vPPI (mmol_per_min)"
    legend_algebraic[27] = "vTransk1 in component vTransk1 (mmol_per_min)"
    legend_algebraic[29] = "vR5PI in component vR5PI (mmol_per_min)"
    legend_algebraic[30] = "vTransald in component vTransald (mmol_per_min)"
    legend_algebraic[31] = "vTransk2 in component vTransk2 (mmol_per_min)"
    legend_algebraic[25] = "vNADPH in component vNADPH (mmol_per_min)"
    legend_algebraic[3] = "vGLT in component vGLT (mmol_per_min)"
    legend_algebraic[1] = "ratio_NADPH_NADP in component rules (dimensionless)"
    legend_constants[11] = "VmGLK in component vGLK (mM_per_min)"
    legend_constants[12] = "KeqAK in component vGLK (dimensionless)"
    legend_constants[13] = "KeqGLK in component vGLK (dimensionless)"
    legend_constants[14] = "KmGLKATP in component vGLK (mM)"
    legend_constants[15] = "KmGLKGLCi in component vGLK (mM)"
    legend_constants[16] = "KmGLKG6P in component vGLK (mM)"
    legend_constants[17] = "KmGLKADP in component vGLK (mM)"
    legend_constants[18] = "VmPGI in component vPGI (mM_per_min)"
    legend_constants[19] = "KmPGIG6P in component vPGI (mM)"
    legend_constants[20] = "KeqPGI in component vPGI (dimensionless)"
    legend_constants[21] = "KmPGIF6P in component vPGI (mM)"
    legend_algebraic[4] = "numerator1 in component vPFK (mmol_mM2_per_minute)"
    legend_algebraic[5] = "numerator2 in component vPFK (dimensionless)"
    legend_algebraic[9] = "denominator in component vPFK (mM2)"
    legend_algebraic[6] = "denom1 in component vPFK (dimensionless)"
    legend_algebraic[7] = "denom2 in component vPFK (dimensionless)"
    legend_algebraic[8] = "denom3 in component vPFK (dimensionless)"
    legend_constants[22] = "gR in component vPFK (dimensionless)"
    legend_constants[23] = "VmPFK in component vPFK (mM_per_min)"
    legend_constants[24] = "KeqAK in component vPFK (dimensionless)"
    legend_constants[25] = "KmPFKF6P in component vPFK (mM)"
    legend_constants[26] = "KmPFKATP in component vPFK (mM)"
    legend_constants[27] = "L0 in component vPFK (dimensionless)"
    legend_constants[28] = "CPFKF26BP in component vPFK (dimensionless)"
    legend_constants[29] = "KPFKF26BP in component vPFK (mM)"
    legend_constants[30] = "CPFKF16BP in component vPFK (dimensionless)"
    legend_constants[31] = "KPFKF16BP in component vPFK (mM)"
    legend_constants[32] = "CPFKAMP in component vPFK (dimensionless)"
    legend_constants[33] = "KPFKAMP in component vPFK (mM)"
    legend_constants[34] = "CiPFKATP in component vPFK (dimensionless)"
    legend_constants[35] = "KiPFKATP in component vPFK (mM)"
    legend_constants[36] = "CPFKATP in component vPFK (dimensionless)"
    legend_constants[37] = "VmALD in component vALD (mM_per_min)"
    legend_constants[38] = "KeqTPI in component vALD (dimensionless)"
    legend_constants[39] = "KeqALD in component vALD (mM)"
    legend_constants[40] = "KmALDF16P in component vALD (mM)"
    legend_constants[41] = "KmALDDHAP in component vALD (mM)"
    legend_constants[42] = "KmALDGAP in component vALD (mM)"
    legend_constants[43] = "KmALDGAPi in component vALD (mM)"
    legend_constants[44] = "VmG3PDH in component vG3PDH (mM_per_min)"
    legend_constants[45] = "KeqG3PDH in component vG3PDH (dimensionless)"
    legend_constants[46] = "KeqTPI in component vG3PDH (dimensionless)"
    legend_constants[47] = "KmG3PDHDHAP in component vG3PDH (mM)"
    legend_constants[48] = "KmG3PDHNADH in component vG3PDH (mM)"
    legend_constants[49] = "KmG3PDHNAD in component vG3PDH (mM)"
    legend_constants[50] = "KmG3PDHGLY in component vG3PDH (mM)"
    legend_constants[51] = "VmGAPDHr in component vGAPDH (mM_per_min)"
    legend_constants[52] = "KmGAPDHBPG in component vGAPDH (mM)"
    legend_constants[53] = "KmGAPDHNADH in component vGAPDH (mM)"
    legend_constants[54] = "KeqTPI in component vGAPDH (dimensionless)"
    legend_constants[55] = "VmGAPDHf in component vGAPDH (mM_per_min)"
    legend_constants[56] = "KmGAPDHGAP in component vGAPDH (mM)"
    legend_constants[57] = "KmGAPDHNAD in component vGAPDH (mM)"
    legend_constants[58] = "KeqGAPDH in component vGAPDH (dimensionless)"
    legend_constants[59] = "VmPGK in component vPGK (mM_per_min)"
    legend_constants[60] = "KeqPGK in component vPGK (dimensionless)"
    legend_constants[61] = "KeqAK in component vPGK (dimensionless)"
    legend_constants[62] = "KmPGKATP in component vPGK (mM)"
    legend_constants[63] = "KmPGKP3G in component vPGK (mM)"
    legend_constants[64] = "KmPGKADP in component vPGK (mM)"
    legend_constants[65] = "KmPGKBPG in component vPGK (mM)"
    legend_constants[66] = "VmPGM in component vPGM (mM_per_min)"
    legend_constants[67] = "KmPGMP3G in component vPGM (mM)"
    legend_constants[68] = "KeqPGM in component vPGM (dimensionless)"
    legend_constants[69] = "KmPGMP2G in component vPGM (mM)"
    legend_constants[70] = "VmENO in component vENO (mM_per_min)"
    legend_constants[71] = "KmENOP2G in component vENO (mM)"
    legend_constants[72] = "KeqENO in component vENO (dimensionless)"
    legend_constants[73] = "KmENOPEP in component vENO (mM)"
    legend_constants[74] = "VmPYK in component vPYK (mM_per_min)"
    legend_constants[75] = "KmPYKPEP in component vPYK (mM)"
    legend_constants[76] = "KmPYKADP in component vPYK (mM)"
    legend_constants[77] = "KeqAK in component vPYK (dimensionless)"
    legend_constants[78] = "KeqPYK in component vPYK (dimensionless)"
    legend_constants[79] = "KmPYKPYR in component vPYK (mM)"
    legend_constants[80] = "KmPYKATP in component vPYK (mM)"
    legend_constants[81] = "VmPDC in component vPDC (mM_per_min)"
    legend_constants[82] = "nPDC in component vPDC (dimensionless)"
    legend_constants[83] = "KmPDCPYR in component vPDC (mM)"
    legend_constants[84] = "KSUCC in component vSUC (per_min)"
    legend_constants[85] = "VmADH in component vADH (mM_per_min)"
    legend_constants[86] = "KiADHNAD in component vADH (mM)"
    legend_constants[87] = "KmADHETOH in component vADH (mM)"
    legend_constants[88] = "KeqADH in component vADH (dimensionless)"
    legend_constants[89] = "KmADHNAD in component vADH (mM)"
    legend_constants[90] = "KmADHNADH in component vADH (mM)"
    legend_constants[91] = "KiADHNADH in component vADH (mM)"
    legend_constants[92] = "KmADHACE in component vADH (mM)"
    legend_constants[93] = "KiADHACE in component vADH (mM)"
    legend_constants[94] = "KiADHETOH in component vADH (mM)"
    legend_constants[95] = "KATPASE in component vATP (per_min)"
    legend_constants[96] = "KeqAK in component vATP (dimensionless)"
    legend_constants[97] = "KmGA3P in component vTPI (mM)"
    legend_constants[98] = "KmDHAP in component vTPI (mM)"
    legend_constants[99] = "VmDHAP in component vTPI (mM_per_min)"
    legend_constants[100] = "VmGA3P in component vTPI (mM_per_min)"
    legend_constants[101] = "VmG6PDH in component vG6PDH (mM_per_min)"
    legend_constants[102] = "KmG6P in component vG6PDH (mM)"
    legend_constants[103] = "KmNADP in component vG6PDH (mM)"
    legend_constants[104] = "KiNADPH in component vG6PDH (mM)"
    legend_constants[105] = "Vm6PGL in component v6PGL (mM_per_min)"
    legend_constants[106] = "Km6PGL in component v6PGL (mM)"
    legend_constants[107] = "VmGluDH in component vGluDH (mM_per_min)"
    legend_constants[108] = "KmGluconate in component vGluDH (mM)"
    legend_constants[109] = "KmNADP in component vGluDH (mM)"
    legend_constants[110] = "KiNADPH in component vGluDH (mM)"
    legend_constants[111] = "VmPPIf in component vPPI (mM_per_min)"
    legend_constants[112] = "VmPPIr in component vPPI (mM_per_min)"
    legend_constants[113] = "KmRibu5P in component vPPI (mM)"
    legend_constants[114] = "KmRibo5P in component vPPI (mM)"
    legend_constants[115] = "VmTransk1f in component vTransk1 (mM_per_min)"
    legend_constants[116] = "VmTransk1r in component vTransk1 (mM_per_min)"
    legend_constants[117] = "KmRibose5P in component vTransk1 (mM)"
    legend_constants[118] = "KmXyl5P in component vTransk1 (mM)"
    legend_constants[119] = "KmGA3P in component vTransk1 (mM)"
    legend_constants[120] = "KmSeduhept in component vTransk1 (mM)"
    legend_constants[121] = "VmR5PIf in component vR5PI (mM_per_min)"
    legend_constants[122] = "VmR5PIr in component vR5PI (mM_per_min)"
    legend_constants[123] = "KmRibu5P in component vR5PI (mM)"
    legend_constants[124] = "KmXyl in component vR5PI (mM)"
    legend_constants[125] = "VmTransaldf in component vTransald (mM_per_min)"
    legend_constants[126] = "VmTransaldr in component vTransald (mM_per_min)"
    legend_constants[127] = "KmGA3P in component vTransald (mM)"
    legend_constants[128] = "KmSeduhept in component vTransald (mM)"
    legend_constants[129] = "KmF6P in component vTransald (mM)"
    legend_constants[130] = "KmEry4P in component vTransald (mM)"
    legend_constants[131] = "VmTransk2f in component vTransk2 (mM_per_min)"
    legend_constants[132] = "VmTransk2r in component vTransk2 (mM_per_min)"
    legend_constants[133] = "KmXyl5P in component vTransk2 (mM)"
    legend_constants[134] = "KmEry4P in component vTransk2 (mM)"
    legend_constants[135] = "KmF6P in component vTransk2 (mM)"
    legend_constants[136] = "KmGA3P in component vTransk2 (mM)"
    legend_constants[137] = "kNADPH in component vNADPH (per_min)"
    legend_constants[138] = "VmGLT in component vGLT (mM_per_min)"
    legend_constants[139] = "KeqGLT in component vGLT (dimensionless)"
    legend_constants[140] = "KmGLTGLCo in component vGLT (mM)"
    legend_constants[141] = "KmGLTGLCi in component vGLT (mM)"
    legend_rates[0] = "d/dt P in component cytoplasm (mM)"
    legend_rates[1] = "d/dt G6P in component cytoplasm (mM)"
    legend_rates[2] = "d/dt F6P in component cytoplasm (mM)"
    legend_rates[3] = "d/dt F16P in component cytoplasm (mM)"
    legend_rates[4] = "d/dt NADH in component cytoplasm (mM)"
    legend_rates[5] = "d/dt NAD in component cytoplasm (mM)"
    legend_rates[6] = "d/dt BPG in component cytoplasm (mM)"
    legend_rates[7] = "d/dt P3G in component cytoplasm (mM)"
    legend_rates[8] = "d/dt P2G in component cytoplasm (mM)"
    legend_rates[9] = "d/dt PEP in component cytoplasm (mM)"
    legend_rates[10] = "d/dt PYR in component cytoplasm (mM)"
    legend_rates[11] = "d/dt ACE in component cytoplasm (mM)"
    legend_rates[12] = "d/dt GA3P in component cytoplasm (mM)"
    legend_rates[13] = "d/dt DHAP in component cytoplasm (mM)"
    legend_rates[14] = "d/dt D6PGluconoLactone in component cytoplasm (mM)"
    legend_rates[15] = "d/dt D6PGluconate in component cytoplasm (mM)"
    legend_rates[16] = "d/dt NADP in component cytoplasm (mM)"
    legend_rates[17] = "d/dt NADPH in component cytoplasm (mM)"
    legend_rates[18] = "d/dt Ribulose5P in component cytoplasm (mM)"
    legend_rates[19] = "d/dt Ribose5P in component cytoplasm (mM)"
    legend_rates[20] = "d/dt Xyl5P in component cytoplasm (mM)"
    legend_rates[21] = "d/dt Seduhept7P in component cytoplasm (mM)"
    legend_rates[22] = "d/dt Erythrose4P in component cytoplasm (mM)"
    legend_rates[23] = "d/dt GLCi in component cytoplasm (mM)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    constants[0] = 1
    constants[1] = 1
    constants[2] = 4.1
    constants[3] = 1
    constants[4] = 50
    constants[5] = 0.1
    constants[6] = 0.15
    constants[7] = 50
    constants[8] = 1
    states[0] = 5
    states[1] = 1.39
    states[2] = 0.28
    states[3] = 0.1
    states[4] = 0.39
    states[5] = 1.2
    states[6] = 0.1
    states[7] = 0.1
    states[8] = 0.1
    states[9] = 0.1
    states[10] = 3.36
    states[11] = 0.04
    constants[9] = 0.1
    states[12] = 0.05
    states[13] = 1
    states[14] = 0.1
    states[15] = 0.1
    states[16] = 0.4
    states[17] = 1.6
    states[18] = 0.1
    states[19] = 0.1
    states[20] = 0.1
    states[21] = 0.1
    states[22] = 0
    states[23] = 0.087
    constants[10] = 0.02
    constants[11] = 226.452
    constants[12] = 0.45
    constants[13] = 3800
    constants[14] = 0.15
    constants[15] = 0.08
    constants[16] = 30
    constants[17] = 0.23
    constants[18] = 339.677
    constants[19] = 1.4
    constants[20] = 0.314
    constants[21] = 0.3
    constants[22] = 5.12
    constants[23] = 182.903
    constants[24] = 0.45
    constants[25] = 0.1
    constants[26] = 0.71
    constants[27] = 0.66
    constants[28] = 0.0174
    constants[29] = 0.000682
    constants[30] = 0.397
    constants[31] = 0.111
    constants[32] = 0.0845
    constants[33] = 0.0995
    constants[34] = 100
    constants[35] = 0.65
    constants[36] = 3
    constants[37] = 322.258
    constants[38] = 0.045
    constants[39] = 0.069
    constants[40] = 0.3
    constants[41] = 2.4
    constants[42] = 2
    constants[43] = 10
    constants[44] = 70.15
    constants[45] = 4300
    constants[46] = 0.045
    constants[47] = 0.4
    constants[48] = 0.023
    constants[49] = 0.93
    constants[50] = 1
    constants[51] = 6549.68
    constants[52] = 0.0098
    constants[53] = 0.06
    constants[54] = 0.045
    constants[55] = 1184.52
    constants[56] = 0.21
    constants[57] = 0.09
    constants[58] = 0.005
    constants[59] = 1306.45
    constants[60] = 3200
    constants[61] = 0.45
    constants[62] = 0.3
    constants[63] = 0.53
    constants[64] = 0.2
    constants[65] = 0.003
    constants[66] = 2525.81
    constants[67] = 1.2
    constants[68] = 0.19
    constants[69] = 0.08
    constants[70] = 365.806
    constants[71] = 0.04
    constants[72] = 6.7
    constants[73] = 0.5
    constants[74] = 1088.71
    constants[75] = 0.14
    constants[76] = 0.53
    constants[77] = 0.45
    constants[78] = 6500
    constants[79] = 21
    constants[80] = 1.5
    constants[81] = 174.194
    constants[82] = 1.9
    constants[83] = 4.33
    constants[84] = 21.4
    constants[85] = 810
    constants[86] = 0.92
    constants[87] = 17
    constants[88] = 6.9e-5
    constants[89] = 0.17
    constants[90] = 0.11
    constants[91] = 0.031
    constants[92] = 1.11
    constants[93] = 1.1
    constants[94] = 90
    constants[95] = 39.5
    constants[96] = 0.45
    constants[97] = 1.27
    constants[98] = 1.23
    constants[99] = 10900
    constants[100] = 555
    constants[101] = 4
    constants[102] = 0.04
    constants[103] = 0.02
    constants[104] = 0.017
    constants[105] = 4
    constants[106] = 0.8
    constants[107] = 4
    constants[108] = 0.02
    constants[109] = 0.03
    constants[110] = 0.03
    constants[111] = 3458
    constants[112] = 3458
    constants[113] = 1.6
    constants[114] = 1.6
    constants[115] = 4
    constants[116] = 2
    constants[117] = 0.1
    constants[118] = 0.15
    constants[119] = 0.1
    constants[120] = 0.15
    constants[121] = 1039
    constants[122] = 1039
    constants[123] = 1.5
    constants[124] = 1.5
    constants[125] = 55
    constants[126] = 10
    constants[127] = 0.22
    constants[128] = 0.18
    constants[129] = 0.32
    constants[130] = 0.018
    constants[131] = 3.2
    constants[132] = 43
    constants[133] = 0.16
    constants[134] = 0.09
    constants[135] = 1.1
    constants[136] = 2.1
    constants[137] = 2
    constants[138] = 97.264
    constants[139] = 1
    constants[140] = 1.1918
    constants[141] = 1.1918
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[0] = (constants[8]*constants[11]*((-states[1]*(constants[2]-power(((power(constants[2], 2.00000)-2.00000*constants[2]*states[0])+8.00000*constants[12]*constants[2]*states[0]+power(states[0], 2.00000))-4.00000*constants[12]*(power(states[0], 2.00000)), 1.0/2)))/((1.00000-4.00000*constants[12])*constants[13])+(states[23]*(((-constants[2]+states[0])-4.00000*constants[12]*states[0])+power(((power(constants[2], 2.00000)-2.00000*constants[2]*states[0])+8.00000*constants[12]*constants[2]*states[0]+power(states[0], 2.00000))-4.00000*constants[12]*(power(states[0], 2.00000)), 1.0/2)))/(2.00000-8.00000*constants[12])))/(constants[14]*constants[15]*(1.00000+states[1]/constants[16]+states[23]/constants[15])*(1.00000+(constants[2]-power(((power(constants[2], 2.00000)-2.00000*constants[2]*states[0])+8.00000*constants[12]*constants[2]*states[0]+power(states[0], 2.00000))-4.00000*constants[12]*(power(states[0], 2.00000)), 1.0/2))/((1.00000-4.00000*constants[12])*constants[17])+(((-constants[2]+states[0])-4.00000*constants[12]*states[0])+power(((power(constants[2], 2.00000)-2.00000*constants[2]*states[0])+8.00000*constants[12]*constants[2]*states[0]+power(states[0], 2.00000))-4.00000*constants[12]*(power(states[0], 2.00000)), 1.0/2))/((2.00000-8.00000*constants[12])*constants[14])))
    algebraic[3] = (constants[8]*constants[138]*(constants[7]-states[23]/constants[139]))/(constants[140]*(1.00000+constants[7]/constants[140]+states[23]/constants[141]+(0.910000*constants[7]*states[23])/(constants[141]*constants[140])))
    rates[23] = (algebraic[3]-algebraic[0])/constants[8]
    algebraic[4] = constants[8]*constants[22]*constants[23]*states[2]*(((-constants[2]+states[0])-4.00000*constants[24]*states[0])+power(((power(constants[2], 2.00000)-2.00000*constants[2]*states[0])+8.00000*constants[24]*constants[2]*states[0]+power(states[0], 2.00000))-4.00000*constants[24]*(power(states[0], 2.00000)), 1.0/2))
    algebraic[5] = 1.00000+states[2]/constants[25]+(((-constants[2]+states[0])-4.00000*constants[24]*states[0])+power(((power(constants[2], 2.00000)-2.00000*constants[2]*states[0])+8.00000*constants[24]*constants[2]*states[0]+power(states[0], 2.00000))-4.00000*constants[24]*(power(states[0], 2.00000)), 1.0/2))/((2.00000-8.00000*constants[24])*constants[26])+(constants[22]*states[2]*(((-constants[2]+states[0])-4.00000*constants[24]*states[0])+power(((power(constants[2], 2.00000)-2.00000*constants[2]*states[0])+8.00000*constants[24]*constants[2]*states[0]+power(states[0], 2.00000))-4.00000*constants[24]*(power(states[0], 2.00000)), 1.0/2)))/((2.00000-8.00000*constants[24])*constants[26]*constants[25])
    algebraic[6] = (power(1.00000+(constants[28]*constants[10])/constants[29]+(constants[30]*states[3])/constants[31], 2.00000))*(power(1.00000+(2.00000*constants[32]*constants[24]*(power(constants[2]-power(((power(constants[2], 2.00000)-2.00000*constants[2]*states[0])+8.00000*constants[24]*constants[2]*states[0]+power(states[0], 2.00000))-4.00000*constants[24]*(power(states[0], 2.00000)), 1.0/2), 2.00000)))/((-1.00000+4.00000*constants[24])*constants[33]*(((constants[2]-states[0])+4.00000*constants[24]*states[0])-power(((power(constants[2], 2.00000)-2.00000*constants[2]*states[0])+8.00000*constants[24]*constants[2]*states[0]+power(states[0], 2.00000))-4.00000*constants[24]*(power(states[0], 2.00000)), 1.0/2))), 2.00000))
    algebraic[7] = (power(1.00000+(constants[34]*(((-constants[2]+states[0])-4.00000*constants[24]*states[0])+power(((power(constants[2], 2.00000)-2.00000*constants[2]*states[0])+8.00000*constants[24]*constants[2]*states[0]+power(states[0], 2.00000))-4.00000*constants[24]*(power(states[0], 2.00000)), 1.0/2)))/((2.00000-8.00000*constants[24])*constants[35]), 2.00000))*(power(1.00000+(constants[36]*(((-constants[2]+states[0])-4.00000*constants[24]*states[0])+power(((power(constants[2], 2.00000)-2.00000*constants[2]*states[0])+8.00000*constants[24]*constants[2]*states[0]+power(states[0], 2.00000))-4.00000*constants[24]*(power(states[0], 2.00000)), 1.0/2)))/((2.00000-8.00000*constants[24])*constants[26]), 2.00000))
    algebraic[8] = (power(1.00000+constants[10]/constants[29]+states[3]/constants[31], 2.00000))*(power(1.00000+(2.00000*constants[24]*(power(constants[2]-power(((power(constants[2], 2.00000)-2.00000*constants[2]*states[0])+8.00000*constants[24]*constants[2]*states[0]+power(states[0], 2.00000))-4.00000*constants[24]*(power(states[0], 2.00000)), 1.0/2), 2.00000)))/((-1.00000+4.00000*constants[24])*constants[33]*(((constants[2]-states[0])+4.00000*constants[24]*states[0])-power(((power(constants[2], 2.00000)-2.00000*constants[2]*states[0])+8.00000*constants[24]*constants[2]*states[0]+power(states[0], 2.00000))-4.00000*constants[24]*(power(states[0], 2.00000)), 1.0/2))), 2.00000))*(power(1.00000+(((-constants[2]+states[0])-4.00000*constants[24]*states[0])+power(((power(constants[2], 2.00000)-2.00000*constants[2]*states[0])+8.00000*constants[24]*constants[2]*states[0]+power(states[0], 2.00000))-4.00000*constants[24]*(power(states[0], 2.00000)), 1.0/2))/((2.00000-8.00000*constants[24])*constants[35]), 2.00000))
    algebraic[9] = (2.00000-8.00000*constants[24])*constants[26]*constants[25]*((constants[27]*algebraic[6]*algebraic[7])/algebraic[8]+power(1.00000+states[2]/constants[25]+(((-constants[2]+states[0])-4.00000*constants[24]*states[0])+power(((power(constants[2], 2.00000)-2.00000*constants[2]*states[0])+8.00000*constants[24]*constants[2]*states[0]+power(states[0], 2.00000))-4.00000*constants[24]*(power(states[0], 2.00000)), 1.0/2))/((2.00000-8.00000*constants[24])*constants[26])+(constants[22]*states[2]*(((-constants[2]+states[0])-4.00000*constants[24]*states[0])+power(((power(constants[2], 2.00000)-2.00000*constants[2]*states[0])+8.00000*constants[24]*constants[2]*states[0]+power(states[0], 2.00000))-4.00000*constants[24]*(power(states[0], 2.00000)), 1.0/2)))/((2.00000-8.00000*constants[24])*constants[26]*constants[25]), 2.00000))
    algebraic[10] = (algebraic[4]*algebraic[5])/algebraic[9]
    algebraic[11] = (((constants[8]*constants[37]*states[3])/constants[40])*(1.00000-(states[13]*states[12])/(states[3]*constants[39])))/(1.00000+states[3]/constants[40]+states[13]/constants[41]+states[12]/constants[42]+(states[3]*states[12])/(constants[40]*constants[43])+(states[13]*states[12])/(constants[41]*constants[42]))
    rates[3] = (algebraic[10]-algebraic[11])/constants[8]
    algebraic[13] = (((constants[8]*constants[1]*constants[55]*states[12]*states[5])/(constants[56]*constants[57]))*(1.00000-(states[6]*states[4])/(states[12]*states[5]*constants[58])))/((1.00000+states[12]/constants[56]+states[6]/constants[52])*(1.00000+states[5]/constants[57]+states[4]/constants[53]))
    algebraic[14] = (1.00000*constants[8]*constants[59]*((constants[60]*states[6]*(constants[2]-power(((power(constants[2], 2.00000)-2.00000*constants[2]*states[0])+8.00000*constants[61]*constants[2]*states[0]+power(states[0], 2.00000))-4.00000*constants[61]*(power(states[0], 2.00000)), 1.0/2)))/(1.00000-4.00000*constants[61])-((((-constants[2]+states[0])-4.00000*constants[61]*states[0])+power(((power(constants[2], 2.00000)-2.00000*constants[2]*states[0])+8.00000*constants[61]*constants[2]*states[0]+power(states[0], 2.00000))-4.00000*constants[61]*(power(states[0], 2.00000)), 1.0/2))*states[7])/(2.00000-8.00000*constants[61])))/(constants[62]*constants[63]*(1.00000+(constants[2]-power(((power(constants[2], 2.00000)-2.00000*constants[2]*states[0])+8.00000*constants[61]*constants[2]*states[0]+power(states[0], 2.00000))-4.00000*constants[61]*(power(states[0], 2.00000)), 1.0/2))/((1.00000-4.00000*constants[61])*constants[64])+(((-constants[2]+states[0])-4.00000*constants[61]*states[0])+power(((power(constants[2], 2.00000)-2.00000*constants[2]*states[0])+8.00000*constants[61]*constants[2]*states[0]+power(states[0], 2.00000))-4.00000*constants[61]*(power(states[0], 2.00000)), 1.0/2))/((2.00000-8.00000*constants[61])*constants[62]))*(1.00000+states[6]/constants[65]+states[7]/constants[63]))
    rates[6] = (algebraic[13]-algebraic[14])/constants[8]
    algebraic[12] = (constants[8]*constants[44]*((-constants[6]*states[5])/constants[45]+(states[4]*states[13])/(1.00000+constants[46])))/(constants[47]*constants[48]*(1.00000+states[5]/constants[49]+states[4]/constants[48])*(1.00000+constants[6]/constants[50]+states[13]/((1.00000+constants[46])*constants[47])))
    algebraic[15] = (constants[8]*constants[0]*((constants[99]*states[12])/constants[97]-(constants[100]*states[13])/constants[98]))/(1.00000+states[12]/constants[97]+states[13]/constants[98])
    rates[13] = ((algebraic[11]-algebraic[12])+algebraic[15])/constants[8]
    algebraic[2] = (((constants[8]*constants[18])/constants[19])*(states[1]-states[2]/constants[20]))/(1.00000+states[1]/constants[19]+states[2]/constants[21])
    algebraic[17] = ((constants[8]*constants[101]*states[1]*states[16])/(constants[102]*constants[103]))/((1.00000+states[1]/constants[102]+states[17]/constants[104])*(1.00000+states[16]/constants[103]))
    rates[1] = ((algebraic[0]-algebraic[2])-algebraic[17])/constants[8]
    algebraic[16] = (((constants[8]*constants[66])/constants[67])*(states[7]-states[8]/constants[68]))/(1.00000+states[7]/constants[67]+states[8]/constants[69])
    rates[7] = (algebraic[14]-algebraic[16])/constants[8]
    algebraic[18] = (((constants[8]*constants[70])/constants[71])*(states[8]-states[9]/constants[72]))/(1.00000+states[8]/constants[71]+states[9]/constants[73])
    rates[8] = (algebraic[16]-algebraic[18])/constants[8]
    algebraic[19] = (constants[8]*constants[105]*states[14])/(constants[106]+states[14])
    rates[14] = (algebraic[17]-algebraic[19])/constants[8]
    algebraic[20] = (((constants[8]*constants[74])/(constants[75]*constants[76]))*((states[9]*(constants[2]-power(((power(states[0], 2.00000)-4.00000*constants[77]*(power(states[0], 2.00000)))-2.00000*states[0]*constants[2])+8.00000*constants[77]*states[0]*constants[2]+power(constants[2], 2.00000), 1.0/2)))/(1.00000-4.00000*constants[77])-((states[10]*(((states[0]-4.00000*constants[77]*states[0])-constants[2])+power(((power(states[0], 2.00000)-4.00000*constants[77]*(power(states[0], 2.00000)))-2.00000*states[0]*constants[2])+8.00000*constants[77]*states[0]*constants[2]+power(constants[2], 2.00000), 1.0/2)))/(2.00000-8.00000*constants[77]))/constants[78]))/((1.00000+states[9]/constants[75]+states[10]/constants[79])*(1.00000+((((states[0]-4.00000*constants[77]*states[0])-constants[2])+power(((power(states[0], 2.00000)-4.00000*constants[77]*(power(states[0], 2.00000)))-2.00000*states[0]*constants[2])+8.00000*constants[77]*states[0]*constants[2]+power(constants[2], 2.00000), 1.0/2))/(2.00000-8.00000*constants[77]))/constants[80]+((constants[2]-power(((power(states[0], 2.00000)-4.00000*constants[77]*(power(states[0], 2.00000)))-2.00000*states[0]*constants[2])+8.00000*constants[77]*states[0]*constants[2]+power(constants[2], 2.00000), 1.0/2))/(1.00000-4.00000*constants[77]))/constants[76]))
    rates[9] = (algebraic[18]-algebraic[20])/constants[8]
    algebraic[21] = ((constants[8]*constants[107]*states[15]*states[16])/(constants[108]*constants[109]))/((1.00000+states[15]/constants[108]+states[17]/constants[110])*(1.00000+states[16]/constants[109]))
    rates[15] = (algebraic[19]-algebraic[21])/constants[8]
    algebraic[23] = (constants[8]*constants[95]*(((states[0]-4.00000*constants[96]*states[0])-constants[2])+power(((power(states[0], 2.00000)-4.00000*constants[96]*(power(states[0], 2.00000)))-2.00000*states[0]*constants[2])+8.00000*constants[96]*states[0]*constants[2]+power(constants[2], 2.00000), 1.0/2)))/(2.00000-8.00000*constants[96])
    rates[0] = (((algebraic[14]-(algebraic[0]+algebraic[10]))+algebraic[20])-algebraic[23])/constants[8]
    algebraic[22] = ((constants[8]*constants[81]*(power(states[10], constants[82])))/(power(constants[83], constants[82])))/(1.00000+(power(states[10], constants[82]))/(power(constants[83], constants[82])))
    rates[10] = (algebraic[20]-algebraic[22])/constants[8]
    algebraic[25] = constants[8]*constants[137]*states[17]
    rates[16] = (algebraic[25]-(algebraic[17]+algebraic[21]))/constants[8]
    rates[17] = ((algebraic[17]+algebraic[21])-algebraic[25])/constants[8]
    algebraic[24] = (constants[8]*((constants[111]*states[18])/constants[113]-(constants[112]*states[19])/constants[114]))/(1.00000+states[18]/constants[113]+states[19]/constants[114])
    algebraic[27] = (constants[8]*((constants[115]*states[19]*states[20])/(constants[117]*constants[118])-(constants[116]*states[12]*states[21])/(constants[119]*constants[120])))/((1.00000+states[19]/constants[117]+states[12]/constants[119])*(1.00000+states[20]/constants[118]+states[21]/constants[120]))
    rates[19] = (algebraic[24]-algebraic[27])/constants[8]
    algebraic[26] = constants[8]*constants[84]*states[11]
    algebraic[28] = (((constants[8]*-constants[85])/(constants[86]*constants[87]))*(states[5]*constants[4]-(states[4]*states[11])/constants[88]))/(1.00000+states[5]/constants[86]+(constants[89]*constants[4])/(constants[86]*constants[87])+(constants[90]*states[11])/(constants[91]*constants[92])+states[4]/constants[91]+(states[5]*constants[4])/(constants[86]*constants[87])+(constants[90]*states[5]*states[11])/(constants[86]*constants[91]*constants[92])+(constants[89]*constants[4]*states[4])/(constants[86]*constants[87]*constants[91])+(states[4]*states[11])/(constants[91]*constants[92])+(states[5]*constants[4]*states[11])/(constants[86]*constants[87]*constants[93])+(constants[4]*states[4]*states[11])/(constants[94]*constants[91]*constants[92]))
    rates[4] = (((algebraic[13]-algebraic[12])+3.00000*algebraic[26])-algebraic[28])/constants[8]
    rates[5] = (((algebraic[12]-algebraic[13])-3.00000*algebraic[26])+algebraic[28])/constants[8]
    rates[11] = ((algebraic[22]-2.00000*algebraic[26])-algebraic[28])/constants[8]
    algebraic[29] = (constants[8]*((constants[121]*states[18])/constants[123]-(constants[122]*states[20])/constants[124]))/(1.00000+states[18]/constants[123]+states[20]/constants[124])
    rates[18] = ((algebraic[21]-algebraic[24])-algebraic[29])/constants[8]
    algebraic[30] = (constants[8]*((constants[125]*states[12]*states[21])/(constants[127]*constants[128])-(constants[126]*states[2]*states[22])/(constants[129]*constants[130])))/((1.00000+states[12]/constants[127]+states[2]/constants[129])*(1.00000+states[21]/constants[128]+states[22]/constants[130]))
    rates[21] = (algebraic[27]-algebraic[30])/constants[8]
    algebraic[31] = (constants[8]*((constants[131]*states[22]*states[20])/(constants[134]*constants[133])-(constants[132]*states[2]*states[12])/(constants[135]*constants[136])))/((1.00000+states[20]/constants[133]+states[12]/constants[136])*(1.00000+states[22]/constants[134]+states[2]/constants[135]))
    rates[2] = ((algebraic[2]-algebraic[10])+algebraic[30]+algebraic[31])/constants[8]
    rates[12] = (((((algebraic[11]-algebraic[13])-algebraic[15])+algebraic[27])-algebraic[30])+algebraic[31])/constants[8]
    rates[20] = ((algebraic[29]-algebraic[27])-algebraic[31])/constants[8]
    rates[22] = (algebraic[30]-algebraic[31])/constants[8]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = (constants[8]*constants[11]*((-states[1]*(constants[2]-power(((power(constants[2], 2.00000)-2.00000*constants[2]*states[0])+8.00000*constants[12]*constants[2]*states[0]+power(states[0], 2.00000))-4.00000*constants[12]*(power(states[0], 2.00000)), 1.0/2)))/((1.00000-4.00000*constants[12])*constants[13])+(states[23]*(((-constants[2]+states[0])-4.00000*constants[12]*states[0])+power(((power(constants[2], 2.00000)-2.00000*constants[2]*states[0])+8.00000*constants[12]*constants[2]*states[0]+power(states[0], 2.00000))-4.00000*constants[12]*(power(states[0], 2.00000)), 1.0/2)))/(2.00000-8.00000*constants[12])))/(constants[14]*constants[15]*(1.00000+states[1]/constants[16]+states[23]/constants[15])*(1.00000+(constants[2]-power(((power(constants[2], 2.00000)-2.00000*constants[2]*states[0])+8.00000*constants[12]*constants[2]*states[0]+power(states[0], 2.00000))-4.00000*constants[12]*(power(states[0], 2.00000)), 1.0/2))/((1.00000-4.00000*constants[12])*constants[17])+(((-constants[2]+states[0])-4.00000*constants[12]*states[0])+power(((power(constants[2], 2.00000)-2.00000*constants[2]*states[0])+8.00000*constants[12]*constants[2]*states[0]+power(states[0], 2.00000))-4.00000*constants[12]*(power(states[0], 2.00000)), 1.0/2))/((2.00000-8.00000*constants[12])*constants[14])))
    algebraic[3] = (constants[8]*constants[138]*(constants[7]-states[23]/constants[139]))/(constants[140]*(1.00000+constants[7]/constants[140]+states[23]/constants[141]+(0.910000*constants[7]*states[23])/(constants[141]*constants[140])))
    algebraic[4] = constants[8]*constants[22]*constants[23]*states[2]*(((-constants[2]+states[0])-4.00000*constants[24]*states[0])+power(((power(constants[2], 2.00000)-2.00000*constants[2]*states[0])+8.00000*constants[24]*constants[2]*states[0]+power(states[0], 2.00000))-4.00000*constants[24]*(power(states[0], 2.00000)), 1.0/2))
    algebraic[5] = 1.00000+states[2]/constants[25]+(((-constants[2]+states[0])-4.00000*constants[24]*states[0])+power(((power(constants[2], 2.00000)-2.00000*constants[2]*states[0])+8.00000*constants[24]*constants[2]*states[0]+power(states[0], 2.00000))-4.00000*constants[24]*(power(states[0], 2.00000)), 1.0/2))/((2.00000-8.00000*constants[24])*constants[26])+(constants[22]*states[2]*(((-constants[2]+states[0])-4.00000*constants[24]*states[0])+power(((power(constants[2], 2.00000)-2.00000*constants[2]*states[0])+8.00000*constants[24]*constants[2]*states[0]+power(states[0], 2.00000))-4.00000*constants[24]*(power(states[0], 2.00000)), 1.0/2)))/((2.00000-8.00000*constants[24])*constants[26]*constants[25])
    algebraic[6] = (power(1.00000+(constants[28]*constants[10])/constants[29]+(constants[30]*states[3])/constants[31], 2.00000))*(power(1.00000+(2.00000*constants[32]*constants[24]*(power(constants[2]-power(((power(constants[2], 2.00000)-2.00000*constants[2]*states[0])+8.00000*constants[24]*constants[2]*states[0]+power(states[0], 2.00000))-4.00000*constants[24]*(power(states[0], 2.00000)), 1.0/2), 2.00000)))/((-1.00000+4.00000*constants[24])*constants[33]*(((constants[2]-states[0])+4.00000*constants[24]*states[0])-power(((power(constants[2], 2.00000)-2.00000*constants[2]*states[0])+8.00000*constants[24]*constants[2]*states[0]+power(states[0], 2.00000))-4.00000*constants[24]*(power(states[0], 2.00000)), 1.0/2))), 2.00000))
    algebraic[7] = (power(1.00000+(constants[34]*(((-constants[2]+states[0])-4.00000*constants[24]*states[0])+power(((power(constants[2], 2.00000)-2.00000*constants[2]*states[0])+8.00000*constants[24]*constants[2]*states[0]+power(states[0], 2.00000))-4.00000*constants[24]*(power(states[0], 2.00000)), 1.0/2)))/((2.00000-8.00000*constants[24])*constants[35]), 2.00000))*(power(1.00000+(constants[36]*(((-constants[2]+states[0])-4.00000*constants[24]*states[0])+power(((power(constants[2], 2.00000)-2.00000*constants[2]*states[0])+8.00000*constants[24]*constants[2]*states[0]+power(states[0], 2.00000))-4.00000*constants[24]*(power(states[0], 2.00000)), 1.0/2)))/((2.00000-8.00000*constants[24])*constants[26]), 2.00000))
    algebraic[8] = (power(1.00000+constants[10]/constants[29]+states[3]/constants[31], 2.00000))*(power(1.00000+(2.00000*constants[24]*(power(constants[2]-power(((power(constants[2], 2.00000)-2.00000*constants[2]*states[0])+8.00000*constants[24]*constants[2]*states[0]+power(states[0], 2.00000))-4.00000*constants[24]*(power(states[0], 2.00000)), 1.0/2), 2.00000)))/((-1.00000+4.00000*constants[24])*constants[33]*(((constants[2]-states[0])+4.00000*constants[24]*states[0])-power(((power(constants[2], 2.00000)-2.00000*constants[2]*states[0])+8.00000*constants[24]*constants[2]*states[0]+power(states[0], 2.00000))-4.00000*constants[24]*(power(states[0], 2.00000)), 1.0/2))), 2.00000))*(power(1.00000+(((-constants[2]+states[0])-4.00000*constants[24]*states[0])+power(((power(constants[2], 2.00000)-2.00000*constants[2]*states[0])+8.00000*constants[24]*constants[2]*states[0]+power(states[0], 2.00000))-4.00000*constants[24]*(power(states[0], 2.00000)), 1.0/2))/((2.00000-8.00000*constants[24])*constants[35]), 2.00000))
    algebraic[9] = (2.00000-8.00000*constants[24])*constants[26]*constants[25]*((constants[27]*algebraic[6]*algebraic[7])/algebraic[8]+power(1.00000+states[2]/constants[25]+(((-constants[2]+states[0])-4.00000*constants[24]*states[0])+power(((power(constants[2], 2.00000)-2.00000*constants[2]*states[0])+8.00000*constants[24]*constants[2]*states[0]+power(states[0], 2.00000))-4.00000*constants[24]*(power(states[0], 2.00000)), 1.0/2))/((2.00000-8.00000*constants[24])*constants[26])+(constants[22]*states[2]*(((-constants[2]+states[0])-4.00000*constants[24]*states[0])+power(((power(constants[2], 2.00000)-2.00000*constants[2]*states[0])+8.00000*constants[24]*constants[2]*states[0]+power(states[0], 2.00000))-4.00000*constants[24]*(power(states[0], 2.00000)), 1.0/2)))/((2.00000-8.00000*constants[24])*constants[26]*constants[25]), 2.00000))
    algebraic[10] = (algebraic[4]*algebraic[5])/algebraic[9]
    algebraic[11] = (((constants[8]*constants[37]*states[3])/constants[40])*(1.00000-(states[13]*states[12])/(states[3]*constants[39])))/(1.00000+states[3]/constants[40]+states[13]/constants[41]+states[12]/constants[42]+(states[3]*states[12])/(constants[40]*constants[43])+(states[13]*states[12])/(constants[41]*constants[42]))
    algebraic[13] = (((constants[8]*constants[1]*constants[55]*states[12]*states[5])/(constants[56]*constants[57]))*(1.00000-(states[6]*states[4])/(states[12]*states[5]*constants[58])))/((1.00000+states[12]/constants[56]+states[6]/constants[52])*(1.00000+states[5]/constants[57]+states[4]/constants[53]))
    algebraic[14] = (1.00000*constants[8]*constants[59]*((constants[60]*states[6]*(constants[2]-power(((power(constants[2], 2.00000)-2.00000*constants[2]*states[0])+8.00000*constants[61]*constants[2]*states[0]+power(states[0], 2.00000))-4.00000*constants[61]*(power(states[0], 2.00000)), 1.0/2)))/(1.00000-4.00000*constants[61])-((((-constants[2]+states[0])-4.00000*constants[61]*states[0])+power(((power(constants[2], 2.00000)-2.00000*constants[2]*states[0])+8.00000*constants[61]*constants[2]*states[0]+power(states[0], 2.00000))-4.00000*constants[61]*(power(states[0], 2.00000)), 1.0/2))*states[7])/(2.00000-8.00000*constants[61])))/(constants[62]*constants[63]*(1.00000+(constants[2]-power(((power(constants[2], 2.00000)-2.00000*constants[2]*states[0])+8.00000*constants[61]*constants[2]*states[0]+power(states[0], 2.00000))-4.00000*constants[61]*(power(states[0], 2.00000)), 1.0/2))/((1.00000-4.00000*constants[61])*constants[64])+(((-constants[2]+states[0])-4.00000*constants[61]*states[0])+power(((power(constants[2], 2.00000)-2.00000*constants[2]*states[0])+8.00000*constants[61]*constants[2]*states[0]+power(states[0], 2.00000))-4.00000*constants[61]*(power(states[0], 2.00000)), 1.0/2))/((2.00000-8.00000*constants[61])*constants[62]))*(1.00000+states[6]/constants[65]+states[7]/constants[63]))
    algebraic[12] = (constants[8]*constants[44]*((-constants[6]*states[5])/constants[45]+(states[4]*states[13])/(1.00000+constants[46])))/(constants[47]*constants[48]*(1.00000+states[5]/constants[49]+states[4]/constants[48])*(1.00000+constants[6]/constants[50]+states[13]/((1.00000+constants[46])*constants[47])))
    algebraic[15] = (constants[8]*constants[0]*((constants[99]*states[12])/constants[97]-(constants[100]*states[13])/constants[98]))/(1.00000+states[12]/constants[97]+states[13]/constants[98])
    algebraic[2] = (((constants[8]*constants[18])/constants[19])*(states[1]-states[2]/constants[20]))/(1.00000+states[1]/constants[19]+states[2]/constants[21])
    algebraic[17] = ((constants[8]*constants[101]*states[1]*states[16])/(constants[102]*constants[103]))/((1.00000+states[1]/constants[102]+states[17]/constants[104])*(1.00000+states[16]/constants[103]))
    algebraic[16] = (((constants[8]*constants[66])/constants[67])*(states[7]-states[8]/constants[68]))/(1.00000+states[7]/constants[67]+states[8]/constants[69])
    algebraic[18] = (((constants[8]*constants[70])/constants[71])*(states[8]-states[9]/constants[72]))/(1.00000+states[8]/constants[71]+states[9]/constants[73])
    algebraic[19] = (constants[8]*constants[105]*states[14])/(constants[106]+states[14])
    algebraic[20] = (((constants[8]*constants[74])/(constants[75]*constants[76]))*((states[9]*(constants[2]-power(((power(states[0], 2.00000)-4.00000*constants[77]*(power(states[0], 2.00000)))-2.00000*states[0]*constants[2])+8.00000*constants[77]*states[0]*constants[2]+power(constants[2], 2.00000), 1.0/2)))/(1.00000-4.00000*constants[77])-((states[10]*(((states[0]-4.00000*constants[77]*states[0])-constants[2])+power(((power(states[0], 2.00000)-4.00000*constants[77]*(power(states[0], 2.00000)))-2.00000*states[0]*constants[2])+8.00000*constants[77]*states[0]*constants[2]+power(constants[2], 2.00000), 1.0/2)))/(2.00000-8.00000*constants[77]))/constants[78]))/((1.00000+states[9]/constants[75]+states[10]/constants[79])*(1.00000+((((states[0]-4.00000*constants[77]*states[0])-constants[2])+power(((power(states[0], 2.00000)-4.00000*constants[77]*(power(states[0], 2.00000)))-2.00000*states[0]*constants[2])+8.00000*constants[77]*states[0]*constants[2]+power(constants[2], 2.00000), 1.0/2))/(2.00000-8.00000*constants[77]))/constants[80]+((constants[2]-power(((power(states[0], 2.00000)-4.00000*constants[77]*(power(states[0], 2.00000)))-2.00000*states[0]*constants[2])+8.00000*constants[77]*states[0]*constants[2]+power(constants[2], 2.00000), 1.0/2))/(1.00000-4.00000*constants[77]))/constants[76]))
    algebraic[21] = ((constants[8]*constants[107]*states[15]*states[16])/(constants[108]*constants[109]))/((1.00000+states[15]/constants[108]+states[17]/constants[110])*(1.00000+states[16]/constants[109]))
    algebraic[23] = (constants[8]*constants[95]*(((states[0]-4.00000*constants[96]*states[0])-constants[2])+power(((power(states[0], 2.00000)-4.00000*constants[96]*(power(states[0], 2.00000)))-2.00000*states[0]*constants[2])+8.00000*constants[96]*states[0]*constants[2]+power(constants[2], 2.00000), 1.0/2)))/(2.00000-8.00000*constants[96])
    algebraic[22] = ((constants[8]*constants[81]*(power(states[10], constants[82])))/(power(constants[83], constants[82])))/(1.00000+(power(states[10], constants[82]))/(power(constants[83], constants[82])))
    algebraic[25] = constants[8]*constants[137]*states[17]
    algebraic[24] = (constants[8]*((constants[111]*states[18])/constants[113]-(constants[112]*states[19])/constants[114]))/(1.00000+states[18]/constants[113]+states[19]/constants[114])
    algebraic[27] = (constants[8]*((constants[115]*states[19]*states[20])/(constants[117]*constants[118])-(constants[116]*states[12]*states[21])/(constants[119]*constants[120])))/((1.00000+states[19]/constants[117]+states[12]/constants[119])*(1.00000+states[20]/constants[118]+states[21]/constants[120]))
    algebraic[26] = constants[8]*constants[84]*states[11]
    algebraic[28] = (((constants[8]*-constants[85])/(constants[86]*constants[87]))*(states[5]*constants[4]-(states[4]*states[11])/constants[88]))/(1.00000+states[5]/constants[86]+(constants[89]*constants[4])/(constants[86]*constants[87])+(constants[90]*states[11])/(constants[91]*constants[92])+states[4]/constants[91]+(states[5]*constants[4])/(constants[86]*constants[87])+(constants[90]*states[5]*states[11])/(constants[86]*constants[91]*constants[92])+(constants[89]*constants[4]*states[4])/(constants[86]*constants[87]*constants[91])+(states[4]*states[11])/(constants[91]*constants[92])+(states[5]*constants[4]*states[11])/(constants[86]*constants[87]*constants[93])+(constants[4]*states[4]*states[11])/(constants[94]*constants[91]*constants[92]))
    algebraic[29] = (constants[8]*((constants[121]*states[18])/constants[123]-(constants[122]*states[20])/constants[124]))/(1.00000+states[18]/constants[123]+states[20]/constants[124])
    algebraic[30] = (constants[8]*((constants[125]*states[12]*states[21])/(constants[127]*constants[128])-(constants[126]*states[2]*states[22])/(constants[129]*constants[130])))/((1.00000+states[12]/constants[127]+states[2]/constants[129])*(1.00000+states[21]/constants[128]+states[22]/constants[130]))
    algebraic[31] = (constants[8]*((constants[131]*states[22]*states[20])/(constants[134]*constants[133])-(constants[132]*states[2]*states[12])/(constants[135]*constants[136])))/((1.00000+states[20]/constants[133]+states[12]/constants[136])*(1.00000+states[22]/constants[134]+states[2]/constants[135]))
    algebraic[1] = states[17]/states[16]
    return algebraic

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
        self.k_rel_TPI = 1
        self.k_rel_GAPDH = 1
        self.SUMAXP = 4.1
        self.CO2 = 1
        self.ETOH = 50
        self.SUCC = 0.1
        self.GLY = 0.15
        self.GLCo = 50
        self.cytoplasm = 1
        self.X = 0.1
        self.F26BP = 0.02
        self.VmGLK = 226.452
        self.KeqAK = 0.45
        self.KeqGLK = 3800
        self.KmGLKATP = 0.15
        self.KmGLKGLCi = 0.08
        self.KmGLKG6P = 30
        self.KmGLKADP = 0.23
        self.VmPGI = 339.677
        self.KmPGIG6P = 1.4
        self.KeqPGI = 0.314
        self.KmPGIF6P = 0.3
        self.gR = 5.12
        self.VmPFK = 182.903
        self.KeqAK_1 = 0.45
        self.KmPFKF6P = 0.1
        self.KmPFKATP = 0.71
        self.L0 = 0.66
        self.CPFKF26BP = 0.0174
        self.KPFKF26BP = 0.000682
        self.CPFKF16BP = 0.397
        self.KPFKF16BP = 0.111
        self.CPFKAMP = 0.0845
        self.KPFKAMP = 0.0995
        self.CiPFKATP = 100
        self.KiPFKATP = 0.65
        self.CPFKATP = 3
        self.VmALD = 322.258
        self.KeqTPI = 0.045
        self.KeqALD = 0.069
        self.KmALDF16P = 0.3
        self.KmALDDHAP = 2.4
        self.KmALDGAP = 2
        self.KmALDGAPi = 10
        self.VmG3PDH = 70.15
        self.KeqG3PDH = 4300
        self.KeqTPI_1 = 0.045
        self.KmG3PDHDHAP = 0.4
        self.KmG3PDHNADH = 0.023
        self.KmG3PDHNAD = 0.93
        self.KmG3PDHGLY = 1
        self.VmGAPDHr = 6549.68
        self.KmGAPDHBPG = 0.0098
        self.KmGAPDHNADH = 0.06
        self.KeqTPI_2 = 0.045
        self.VmGAPDHf = 1184.52
        self.KmGAPDHGAP = 0.21
        self.KmGAPDHNAD = 0.09
        self.KeqGAPDH = 0.005
        self.VmPGK = 1306.45
        self.KeqPGK = 3200
        self.KeqAK_2 = 0.45
        self.KmPGKATP = 0.3
        self.KmPGKP3G = 0.53
        self.KmPGKADP = 0.2
        self.KmPGKBPG = 0.003
        self.VmPGM = 2525.81
        self.KmPGMP3G = 1.2
        self.KeqPGM = 0.19
        self.KmPGMP2G = 0.08
        self.VmENO = 365.806
        self.KmENOP2G = 0.04
        self.KeqENO = 6.7
        self.KmENOPEP = 0.5
        self.VmPYK = 1088.71
        self.KmPYKPEP = 0.14
        self.KmPYKADP = 0.53
        self.KeqAK_3 = 0.45
        self.KeqPYK = 6500
        self.KmPYKPYR = 21
        self.KmPYKATP = 1.5
        self.VmPDC = 174.194
        self.nPDC = 1.9
        self.KmPDCPYR = 4.33
        self.KSUCC = 21.4
        self.VmADH = 810
        self.KiADHNAD = 0.92
        self.KmADHETOH = 17
        self.KeqADH = 6.9e-5
        self.KmADHNAD = 0.17
        self.KmADHNADH = 0.11
        self.KiADHNADH = 0.031
        self.KmADHACE = 1.11
        self.KiADHACE = 1.1
        self.KiADHETOH = 90
        self.KATPASE = 39.5
        self.KeqAK_4 = 0.45
        self.KmGA3P = 1.27
        self.KmDHAP = 1.23
        self.VmDHAP = 10900
        self.VmGA3P = 555
        self.VmG6PDH = 4
        self.KmG6P = 0.04
        self.KmNADP = 0.02
        self.KiNADPH = 0.017
        self.Vm6PGL = 4
        self.Km6PGL = 0.8
        self.VmGluDH = 4
        self.KmGluconate = 0.02
        self.KmNADP_1 = 0.03
        self.KiNADPH_1 = 0.03
        self.VmPPIf = 3458
        self.VmPPIr = 3458
        self.KmRibu5P = 1.6
        self.KmRibo5P = 1.6
        self.VmTransk1f = 4
        self.VmTransk1r = 2
        self.KmRibose5P = 0.1
        self.KmXyl5P = 0.15
        self.KmGA3P_1 = 0.1
        self.KmSeduhept = 0.15
        self.VmR5PIf = 1039
        self.VmR5PIr = 1039
        self.KmRibu5P_1 = 1.5
        self.KmXyl = 1.5
        self.VmTransaldf = 55
        self.VmTransaldr = 10
        self.KmGA3P_2 = 0.22
        self.KmSeduhept_1 = 0.18
        self.KmF6P = 0.32
        self.KmEry4P = 0.018
        self.VmTransk2f = 3.2
        self.VmTransk2r = 43
        self.KmXyl5P_1 = 0.16
        self.KmEry4P_1 = 0.09
        self.KmF6P_1 = 1.1
        self.KmGA3P_3 = 2.1
        self.kNADPH = 2
        self.VmGLT = 97.264
        self.KeqGLT = 1
        self.KmGLTGLCo = 1.1918
        self.KmGLTGLCi = 1.1918

    def to_dict(self):
        return {
            "k_rel_TPI": self.k_rel_TPI,
            "k_rel_GAPDH": self.k_rel_GAPDH,
            "SUMAXP": self.SUMAXP,
            "CO2": self.CO2,
            "ETOH": self.ETOH,
            "SUCC": self.SUCC,
            "GLY": self.GLY,
            "GLCo": self.GLCo,
            "cytoplasm": self.cytoplasm,
            "X": self.X,
            "F26BP": self.F26BP,
            "VmGLK": self.VmGLK,
            "KeqAK": self.KeqAK,
            "KeqGLK": self.KeqGLK,
            "KmGLKATP": self.KmGLKATP,
            "KmGLKGLCi": self.KmGLKGLCi,
            "KmGLKG6P": self.KmGLKG6P,
            "KmGLKADP": self.KmGLKADP,
            "VmPGI": self.VmPGI,
            "KmPGIG6P": self.KmPGIG6P,
            "KeqPGI": self.KeqPGI,
            "KmPGIF6P": self.KmPGIF6P,
            "gR": self.gR,
            "VmPFK": self.VmPFK,
            "KeqAK_1": self.KeqAK_1,
            "KmPFKF6P": self.KmPFKF6P,
            "KmPFKATP": self.KmPFKATP,
            "L0": self.L0,
            "CPFKF26BP": self.CPFKF26BP,
            "KPFKF26BP": self.KPFKF26BP,
            "CPFKF16BP": self.CPFKF16BP,
            "KPFKF16BP": self.KPFKF16BP,
            "CPFKAMP": self.CPFKAMP,
            "KPFKAMP": self.KPFKAMP,
            "CiPFKATP": self.CiPFKATP,
            "KiPFKATP": self.KiPFKATP,
            "CPFKATP": self.CPFKATP,
            "VmALD": self.VmALD,
            "KeqTPI": self.KeqTPI,
            "KeqALD": self.KeqALD,
            "KmALDF16P": self.KmALDF16P,
            "KmALDDHAP": self.KmALDDHAP,
            "KmALDGAP": self.KmALDGAP,
            "KmALDGAPi": self.KmALDGAPi,
            "VmG3PDH": self.VmG3PDH,
            "KeqG3PDH": self.KeqG3PDH,
            "KeqTPI_1": self.KeqTPI_1,
            "KmG3PDHDHAP": self.KmG3PDHDHAP,
            "KmG3PDHNADH": self.KmG3PDHNADH,
            "KmG3PDHNAD": self.KmG3PDHNAD,
            "KmG3PDHGLY": self.KmG3PDHGLY,
            "VmGAPDHr": self.VmGAPDHr,
            "KmGAPDHBPG": self.KmGAPDHBPG,
            "KmGAPDHNADH": self.KmGAPDHNADH,
            "KeqTPI_2": self.KeqTPI_2,
            "VmGAPDHf": self.VmGAPDHf,
            "KmGAPDHGAP": self.KmGAPDHGAP,
            "KmGAPDHNAD": self.KmGAPDHNAD,
            "KeqGAPDH": self.KeqGAPDH,
            "VmPGK": self.VmPGK,
            "KeqPGK": self.KeqPGK,
            "KeqAK_2": self.KeqAK_2,
            "KmPGKATP": self.KmPGKATP,
            "KmPGKP3G": self.KmPGKP3G,
            "KmPGKADP": self.KmPGKADP,
            "KmPGKBPG": self.KmPGKBPG,
            "VmPGM": self.VmPGM,
            "KmPGMP3G": self.KmPGMP3G,
            "KeqPGM": self.KeqPGM,
            "KmPGMP2G": self.KmPGMP2G,
            "VmENO": self.VmENO,
            "KmENOP2G": self.KmENOP2G,
            "KeqENO": self.KeqENO,
            "KmENOPEP": self.KmENOPEP,
            "VmPYK": self.VmPYK,
            "KmPYKPEP": self.KmPYKPEP,
            "KmPYKADP": self.KmPYKADP,
            "KeqAK_3": self.KeqAK_3,
            "KeqPYK": self.KeqPYK,
            "KmPYKPYR": self.KmPYKPYR,
            "KmPYKATP": self.KmPYKATP,
            "VmPDC": self.VmPDC,
            "nPDC": self.nPDC,
            "KmPDCPYR": self.KmPDCPYR,
            "KSUCC": self.KSUCC,
            "VmADH": self.VmADH,
            "KiADHNAD": self.KiADHNAD,
            "KmADHETOH": self.KmADHETOH,
            "KeqADH": self.KeqADH,
            "KmADHNAD": self.KmADHNAD,
            "KmADHNADH": self.KmADHNADH,
            "KiADHNADH": self.KiADHNADH,
            "KmADHACE": self.KmADHACE,
            "KiADHACE": self.KiADHACE,
            "KiADHETOH": self.KiADHETOH,
            "KATPASE": self.KATPASE,
            "KeqAK_4": self.KeqAK_4,
            "KmGA3P": self.KmGA3P,
            "KmDHAP": self.KmDHAP,
            "VmDHAP": self.VmDHAP,
            "VmGA3P": self.VmGA3P,
            "VmG6PDH": self.VmG6PDH,
            "KmG6P": self.KmG6P,
            "KmNADP": self.KmNADP,
            "KiNADPH": self.KiNADPH,
            "Vm6PGL": self.Vm6PGL,
            "Km6PGL": self.Km6PGL,
            "VmGluDH": self.VmGluDH,
            "KmGluconate": self.KmGluconate,
            "KmNADP_1": self.KmNADP_1,
            "KiNADPH_1": self.KiNADPH_1,
            "VmPPIf": self.VmPPIf,
            "VmPPIr": self.VmPPIr,
            "KmRibu5P": self.KmRibu5P,
            "KmRibo5P": self.KmRibo5P,
            "VmTransk1f": self.VmTransk1f,
            "VmTransk1r": self.VmTransk1r,
            "KmRibose5P": self.KmRibose5P,
            "KmXyl5P": self.KmXyl5P,
            "KmGA3P_1": self.KmGA3P_1,
            "KmSeduhept": self.KmSeduhept,
            "VmR5PIf": self.VmR5PIf,
            "VmR5PIr": self.VmR5PIr,
            "KmRibu5P_1": self.KmRibu5P_1,
            "KmXyl": self.KmXyl,
            "VmTransaldf": self.VmTransaldf,
            "VmTransaldr": self.VmTransaldr,
            "KmGA3P_2": self.KmGA3P_2,
            "KmSeduhept_1": self.KmSeduhept_1,
            "KmF6P": self.KmF6P,
            "KmEry4P": self.KmEry4P,
            "VmTransk2f": self.VmTransk2f,
            "VmTransk2r": self.VmTransk2r,
            "KmXyl5P_1": self.KmXyl5P_1,
            "KmEry4P_1": self.KmEry4P_1,
            "KmF6P_1": self.KmF6P_1,
            "KmGA3P_3": self.KmGA3P_3,
            "kNADPH": self.kNADPH,
            "VmGLT": self.VmGLT,
            "KeqGLT": self.KeqGLT,
            "KmGLTGLCo": self.KmGLTGLCo,
            "KmGLTGLCi": self.KmGLTGLCi,
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
        y0=[5, 1.39, 0.28, 0.1, 0.39, 1.2, 0.1, 0.1, 0.1, 0.1, 3.36, 0.04, 0.05, 1, 0.1, 0.1, 0.4, 1.6, 0.1, 0.1, 0.1, 0.1, 0, 0.087],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "ralser_2007"
        self.curve_names = [
            "P",
            "G6P",
            "F6P",
            "F16P",
            "NADH",
            "NAD",
            "BPG",
            "P3G",
            "P2G",
            "PEP",
            "PYR",
            "ACE",
            "GA3P",
            "DHAP",
            "D6PGluconoLactone",
            "D6PGluconate",
            "NADP",
            "NADPH",
            "Ribulose5P",
            "Ribose5P",
            "Xyl5P",
            "Seduhept7P",
            "Erythrose4P",
            "GLCi",
        ]
        self.state_names = ['P', 'G6P', 'F6P', 'F16P', 'NADH', 'NAD', 'BPG', 'P3G', 'P2G', 'PEP', 'PYR', 'ACE', 'GA3P', 'DHAP', 'D6PGluconoLactone', 'D6PGluconate', 'NADP', 'NADPH', 'Ribulose5P', 'Ribose5P', 'Xyl5P', 'Seduhept7P', 'Erythrose4P', 'GLCi']
        self.algebraic_names = ['vGLK', 'ratio_NADPH_NADP', 'vPGI', 'vGLT', 'numerator1', 'numerator2', 'denom1', 'denom2', 'denom3', 'denominator', 'vPFK', 'vALD', 'vG3PDH', 'vGAPDH', 'vPGK', 'vTPI', 'vPGM', 'vG6PDH', 'vENO', 'v6PGL', 'vPYK', 'vGluDH', 'vPDC', 'vATP', 'vPPI', 'vNADPH', 'vSUC', 'vTransk1', 'vADH', 'vR5PI', 'vTransald', 'vTransk2']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 142
        p = self.params

        # direct mapping
        c[0] = p.k_rel_TPI
        c[1] = p.k_rel_GAPDH
        c[2] = p.SUMAXP
        c[3] = p.CO2
        c[4] = p.ETOH
        c[5] = p.SUCC
        c[6] = p.GLY
        c[7] = p.GLCo
        c[8] = p.cytoplasm
        c[9] = p.X
        c[10] = p.F26BP
        c[11] = p.VmGLK
        c[12] = p.KeqAK
        c[13] = p.KeqGLK
        c[14] = p.KmGLKATP
        c[15] = p.KmGLKGLCi
        c[16] = p.KmGLKG6P
        c[17] = p.KmGLKADP
        c[18] = p.VmPGI
        c[19] = p.KmPGIG6P
        c[20] = p.KeqPGI
        c[21] = p.KmPGIF6P
        c[22] = p.gR
        c[23] = p.VmPFK
        c[24] = p.KeqAK_1
        c[25] = p.KmPFKF6P
        c[26] = p.KmPFKATP
        c[27] = p.L0
        c[28] = p.CPFKF26BP
        c[29] = p.KPFKF26BP
        c[30] = p.CPFKF16BP
        c[31] = p.KPFKF16BP
        c[32] = p.CPFKAMP
        c[33] = p.KPFKAMP
        c[34] = p.CiPFKATP
        c[35] = p.KiPFKATP
        c[36] = p.CPFKATP
        c[37] = p.VmALD
        c[38] = p.KeqTPI
        c[39] = p.KeqALD
        c[40] = p.KmALDF16P
        c[41] = p.KmALDDHAP
        c[42] = p.KmALDGAP
        c[43] = p.KmALDGAPi
        c[44] = p.VmG3PDH
        c[45] = p.KeqG3PDH
        c[46] = p.KeqTPI_1
        c[47] = p.KmG3PDHDHAP
        c[48] = p.KmG3PDHNADH
        c[49] = p.KmG3PDHNAD
        c[50] = p.KmG3PDHGLY
        c[51] = p.VmGAPDHr
        c[52] = p.KmGAPDHBPG
        c[53] = p.KmGAPDHNADH
        c[54] = p.KeqTPI_2
        c[55] = p.VmGAPDHf
        c[56] = p.KmGAPDHGAP
        c[57] = p.KmGAPDHNAD
        c[58] = p.KeqGAPDH
        c[59] = p.VmPGK
        c[60] = p.KeqPGK
        c[61] = p.KeqAK_2
        c[62] = p.KmPGKATP
        c[63] = p.KmPGKP3G
        c[64] = p.KmPGKADP
        c[65] = p.KmPGKBPG
        c[66] = p.VmPGM
        c[67] = p.KmPGMP3G
        c[68] = p.KeqPGM
        c[69] = p.KmPGMP2G
        c[70] = p.VmENO
        c[71] = p.KmENOP2G
        c[72] = p.KeqENO
        c[73] = p.KmENOPEP
        c[74] = p.VmPYK
        c[75] = p.KmPYKPEP
        c[76] = p.KmPYKADP
        c[77] = p.KeqAK_3
        c[78] = p.KeqPYK
        c[79] = p.KmPYKPYR
        c[80] = p.KmPYKATP
        c[81] = p.VmPDC
        c[82] = p.nPDC
        c[83] = p.KmPDCPYR
        c[84] = p.KSUCC
        c[85] = p.VmADH
        c[86] = p.KiADHNAD
        c[87] = p.KmADHETOH
        c[88] = p.KeqADH
        c[89] = p.KmADHNAD
        c[90] = p.KmADHNADH
        c[91] = p.KiADHNADH
        c[92] = p.KmADHACE
        c[93] = p.KiADHACE
        c[94] = p.KiADHETOH
        c[95] = p.KATPASE
        c[96] = p.KeqAK_4
        c[97] = p.KmGA3P
        c[98] = p.KmDHAP
        c[99] = p.VmDHAP
        c[100] = p.VmGA3P
        c[101] = p.VmG6PDH
        c[102] = p.KmG6P
        c[103] = p.KmNADP
        c[104] = p.KiNADPH
        c[105] = p.Vm6PGL
        c[106] = p.Km6PGL
        c[107] = p.VmGluDH
        c[108] = p.KmGluconate
        c[109] = p.KmNADP_1
        c[110] = p.KiNADPH_1
        c[111] = p.VmPPIf
        c[112] = p.VmPPIr
        c[113] = p.KmRibu5P
        c[114] = p.KmRibo5P
        c[115] = p.VmTransk1f
        c[116] = p.VmTransk1r
        c[117] = p.KmRibose5P
        c[118] = p.KmXyl5P
        c[119] = p.KmGA3P_1
        c[120] = p.KmSeduhept
        c[121] = p.VmR5PIf
        c[122] = p.VmR5PIr
        c[123] = p.KmRibu5P_1
        c[124] = p.KmXyl
        c[125] = p.VmTransaldf
        c[126] = p.VmTransaldr
        c[127] = p.KmGA3P_2
        c[128] = p.KmSeduhept_1
        c[129] = p.KmF6P
        c[130] = p.KmEry4P
        c[131] = p.VmTransk2f
        c[132] = p.VmTransk2r
        c[133] = p.KmXyl5P_1
        c[134] = p.KmEry4P_1
        c[135] = p.KmF6P_1
        c[136] = p.KmGA3P_3
        c[137] = p.kNADPH
        c[138] = p.VmGLT
        c[139] = p.KeqGLT
        c[140] = p.KmGLTGLCo
        c[141] = p.KmGLTGLCi

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
