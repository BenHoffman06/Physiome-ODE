# Size of variable arrays:
sizeAlgebraic = 30
sizeStates = 8
sizeConstants = 81
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (minute)"
    legend_states[0] = "PYR in component PYR (millimolar)"
    legend_algebraic[4] = "V_GLYC in component V_GLYC (flux)"
    legend_algebraic[6] = "V_LDH in component V_LDH (flux)"
    legend_algebraic[8] = "V_PDH in component V_PDH (flux)"
    legend_algebraic[20] = "V_ALS in component V_ALS (flux)"
    legend_states[1] = "ACP in component ACP (millimolar)"
    legend_algebraic[10] = "V_PTA in component V_PTA (flux)"
    legend_algebraic[14] = "V_ACK in component V_ACK (flux)"
    legend_states[2] = "ACAL in component ACAL (millimolar)"
    legend_algebraic[13] = "V_ACALDH in component V_ACALDH (flux)"
    legend_algebraic[17] = "V_ADH in component V_ADH (flux)"
    legend_states[3] = "ACLAC in component ACLAC (millimolar)"
    legend_algebraic[22] = "V_ALDC in component V_ALDC (flux)"
    legend_algebraic[27] = "V_NEALC in component V_NEALC (flux)"
    legend_states[4] = "ACET in component ACET (millimolar)"
    legend_algebraic[26] = "V_ACETDH in component V_ACETDH (flux)"
    legend_algebraic[24] = "V_ACETEFF in component V_ACETEFF (flux)"
    legend_states[5] = "ATP in component ATP (millimolar)"
    legend_algebraic[18] = "V_ATPase in component V_ATPase (flux)"
    legend_algebraic[0] = "ADP in component ADP (millimolar)"
    legend_constants[0] = "A_tot in component ADP (millimolar)"
    legend_states[6] = "NADH in component NADH (millimolar)"
    legend_algebraic[29] = "V_NOX in component V_NOX (flux)"
    legend_algebraic[1] = "NAD in component NAD (millimolar)"
    legend_constants[1] = "NAD_tot in component NAD (millimolar)"
    legend_states[7] = "ACCOA in component ACCOA (millimolar)"
    legend_algebraic[2] = "COA in component COA (millimolar)"
    legend_constants[2] = "C_tot in component COA (millimolar)"
    legend_constants[3] = "AC in component AC (millimolar)"
    legend_constants[4] = "BUT in component BUT (millimolar)"
    legend_constants[5] = "ETOH in component ETOH (millimolar)"
    legend_constants[6] = "GLC in component GLC (millimolar)"
    legend_constants[7] = "LAC in component LAC (millimolar)"
    legend_constants[8] = "O in component O (millimolar)"
    legend_constants[9] = "P in component P (millimolar)"
    legend_algebraic[3] = "V_GLYC_temp in component V_GLYC (flux)"
    legend_constants[10] = "Km_GLC in component V_GLYC (millimolar)"
    legend_constants[11] = "Km_NAD in component V_GLYC (millimolar)"
    legend_constants[12] = "Km_ADP in component V_GLYC (millimolar)"
    legend_constants[13] = "Km_PYR in component V_GLYC (millimolar)"
    legend_constants[14] = "Km_NADH in component V_GLYC (millimolar)"
    legend_constants[15] = "Km_ATP in component V_GLYC (millimolar)"
    legend_constants[16] = "V_GLYC_max in component V_GLYC (flux)"
    legend_algebraic[5] = "V_LDH_temp in component V_LDH (flux)"
    legend_constants[17] = "Keq in component V_LDH (dimensionless)"
    legend_constants[18] = "Km_LAC in component V_LDH (millimolar)"
    legend_constants[19] = "Km_NAD in component V_LDH (millimolar)"
    legend_constants[20] = "Km_PYR in component V_LDH (millimolar)"
    legend_constants[21] = "Km_NADH in component V_LDH (millimolar)"
    legend_constants[22] = "V_LDH_max in component V_LDH (flux)"
    legend_algebraic[7] = "V_PDH_temp in component V_PDH (flux)"
    legend_constants[23] = "Ki in component V_PDH (dimensionless)"
    legend_constants[24] = "Km_NAD in component V_PDH (millimolar)"
    legend_constants[25] = "Km_COA in component V_PDH (millimolar)"
    legend_constants[26] = "Km_PYR in component V_PDH (millimolar)"
    legend_constants[27] = "Km_NADH in component V_PDH (millimolar)"
    legend_constants[28] = "Km_ACCOA in component V_PDH (millimolar)"
    legend_constants[29] = "V_PDH_max in component V_PDH (flux)"
    legend_algebraic[9] = "V_PTA_temp in component V_PTA (flux)"
    legend_constants[30] = "Keq in component V_PTA (dimensionless)"
    legend_constants[31] = "Km_P in component V_PTA (millimolar)"
    legend_constants[32] = "Ki_P in component V_PTA (millimolar)"
    legend_constants[33] = "Ki_COA in component V_PTA (millimolar)"
    legend_constants[34] = "Km_ACP in component V_PTA (millimolar)"
    legend_constants[35] = "Ki_ACP in component V_PTA (millimolar)"
    legend_constants[36] = "Ki_ACCOA in component V_PTA (millimolar)"
    legend_constants[37] = "V_PTA_max in component V_PTA (flux)"
    legend_algebraic[12] = "V_ACK_temp in component V_ACK (flux)"
    legend_constants[38] = "Keq in component V_ACK (dimensionless)"
    legend_constants[39] = "Km_AC in component V_ACK (millimolar)"
    legend_constants[40] = "Km_ATP in component V_ACK (millimolar)"
    legend_constants[41] = "Km_ADP in component V_ACK (millimolar)"
    legend_constants[42] = "Km_ACP in component V_ACK (millimolar)"
    legend_constants[43] = "V_ACK_max in component V_ACK (flux)"
    legend_algebraic[11] = "V_ACALDH_temp in component V_ACALDH (flux)"
    legend_constants[44] = "Keq in component V_ACALDH (millimolar)"
    legend_constants[45] = "Km_NAD in component V_ACALDH (millimolar)"
    legend_constants[46] = "Km_NADH in component V_ACALDH (millimolar)"
    legend_constants[47] = "Km_COA in component V_ACALDH (millimolar)"
    legend_constants[48] = "Km_ACCOA in component V_ACALDH (millimolar)"
    legend_constants[49] = "Km_ACAL in component V_ACALDH (millimolar)"
    legend_constants[50] = "V_ACALDH_max in component V_ACALDH (flux)"
    legend_algebraic[15] = "V_ADH_temp in component V_ADH (flux)"
    legend_constants[51] = "Keq in component V_ADH (dimensionless)"
    legend_constants[52] = "Km_NAD in component V_ADH (millimolar)"
    legend_constants[53] = "Km_NADH in component V_ADH (millimolar)"
    legend_constants[54] = "Km_ETOH in component V_ADH (millimolar)"
    legend_constants[55] = "Km_ACAL in component V_ADH (millimolar)"
    legend_constants[56] = "V_ADH_max in component V_ADH (flux)"
    legend_algebraic[19] = "V_ALS_temp in component V_ALS (flux)"
    legend_constants[57] = "N in component V_ALS (dimensionless)"
    legend_constants[58] = "Keq in component V_ALS (dimensionless)"
    legend_constants[59] = "Km_ACLAC in component V_ALS (millimolar)"
    legend_constants[60] = "Km_PYR in component V_ALS (millimolar)"
    legend_constants[61] = "V_ALS_max in component V_ALS (flux)"
    legend_algebraic[21] = "V_ALDC_temp in component V_ALDC (flux)"
    legend_constants[62] = "Km_ACLAC in component V_ALDC (millimolar)"
    legend_constants[63] = "Km_ACET in component V_ALDC (millimolar)"
    legend_constants[64] = "V_ALDC_max in component V_ALDC (flux)"
    legend_algebraic[23] = "V_ACETEFF_temp in component V_ACETEFF (flux)"
    legend_constants[65] = "Km_ACET in component V_ACETEFF (millimolar)"
    legend_constants[66] = "V_ACETEFF_max in component V_ACETEFF (flux)"
    legend_algebraic[25] = "V_ACETDH_temp in component V_ACETDH (flux)"
    legend_constants[67] = "Keq in component V_ACETDH (dimensionless)"
    legend_constants[68] = "Km_NAD in component V_ACETDH (millimolar)"
    legend_constants[69] = "Km_NADH in component V_ACETDH (millimolar)"
    legend_constants[70] = "Km_BUT in component V_ACETDH (millimolar)"
    legend_constants[71] = "Km_ACET in component V_ACETDH (millimolar)"
    legend_constants[72] = "V_ACETDH_max in component V_ACETDH (flux)"
    legend_algebraic[16] = "V_ATPase_temp in component V_ATPase (flux)"
    legend_constants[73] = "N in component V_ATPase (dimensionless)"
    legend_constants[74] = "Km_ATP in component V_ATPase (dimensionless)"
    legend_constants[75] = "V_ATPase_max in component V_ATPase (flux)"
    legend_algebraic[28] = "V_NOX_temp in component V_NOX (flux)"
    legend_constants[76] = "Km_NAD in component V_NOX (millimolar)"
    legend_constants[77] = "Km_NADH in component V_NOX (millimolar)"
    legend_constants[78] = "Km_O in component V_NOX (millimolar)"
    legend_constants[79] = "V_NOX_max in component V_NOX (flux)"
    legend_constants[80] = "k in component V_NEALC (first_order_rate_constant)"
    legend_rates[0] = "d/dt PYR in component PYR (millimolar)"
    legend_rates[1] = "d/dt ACP in component ACP (millimolar)"
    legend_rates[2] = "d/dt ACAL in component ACAL (millimolar)"
    legend_rates[3] = "d/dt ACLAC in component ACLAC (millimolar)"
    legend_rates[4] = "d/dt ACET in component ACET (millimolar)"
    legend_rates[5] = "d/dt ATP in component ATP (millimolar)"
    legend_rates[6] = "d/dt NADH in component NADH (millimolar)"
    legend_rates[7] = "d/dt ACCOA in component ACCOA (millimolar)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 1
    states[1] = 0.03145
    states[2] = 0.11
    states[3] = 1e-5
    states[4] = 1e-5
    states[5] = 0.1
    constants[0] = 5
    states[6] = 3.67
    constants[1] = 10
    states[7] = 0.11
    constants[2] = 1
    constants[3] = 0.01
    constants[4] = 0.01
    constants[5] = 0.1
    constants[6] = 15
    constants[7] = 0.1
    constants[8] = 0.2
    constants[9] = 10
    constants[10] = 0.1
    constants[11] = 0.1412
    constants[12] = 0.04699
    constants[13] = 2.5
    constants[14] = 0.08999
    constants[15] = 0.01867
    constants[16] = 2397
    constants[17] = 21120.69
    constants[18] = 100
    constants[19] = 2.4
    constants[20] = 1.5
    constants[21] = 0.08
    constants[22] = 5118
    constants[23] = 46.4159
    constants[24] = 0.4
    constants[25] = 0.014
    constants[26] = 1
    constants[27] = 0.1
    constants[28] = 0.008
    constants[29] = 259
    constants[30] = 0.0065
    constants[31] = 2.6
    constants[32] = 2.6
    constants[33] = 0.029
    constants[34] = 0.7
    constants[35] = 0.2
    constants[36] = 0.2
    constants[37] = 42
    constants[38] = 174.217
    constants[39] = 7
    constants[40] = 0.07
    constants[41] = 0.5
    constants[42] = 0.16
    constants[43] = 2700
    constants[44] = 1
    constants[45] = 0.08
    constants[46] = 0.025
    constants[47] = 0.008
    constants[48] = 0.007
    constants[49] = 10
    constants[50] = 97
    constants[51] = 12354.9
    constants[52] = 0.08
    constants[53] = 0.05
    constants[54] = 1
    constants[55] = 0.03
    constants[56] = 162
    constants[57] = 2.4
    constants[58] = 9e12
    constants[59] = 100
    constants[60] = 50
    constants[61] = 600
    constants[62] = 10
    constants[63] = 100
    constants[64] = 106
    constants[65] = 5
    constants[66] = 200
    constants[67] = 1400
    constants[68] = 0.16
    constants[69] = 0.02
    constants[70] = 2.6
    constants[71] = 0.06
    constants[72] = 105
    constants[73] = 2.58
    constants[74] = 6.196
    constants[75] = 900
    constants[76] = 1
    constants[77] = 0.041
    constants[78] = 0.2
    constants[79] = 118
    constants[80] = 0.0003
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[2] = constants[2]-states[7]
    algebraic[9] = ((constants[37]/(constants[36]*constants[31]))*(states[7]*constants[9]-(states[1]*algebraic[2])/constants[30]))/(1.00000+states[7]/constants[36]+constants[9]/constants[32]+states[1]/constants[35]+algebraic[2]/constants[33]+(states[7]*constants[9])/(constants[36]*constants[31])+(states[1]*algebraic[2])/(constants[34]*constants[33]))
    algebraic[10] = custom_piecewise([greater_equal(algebraic[9] , 0.00000), algebraic[9] , True, algebraic[9]])
    algebraic[0] = constants[0]-states[5]
    algebraic[12] = ((constants[43]/(constants[41]*constants[42]))*(states[1]*algebraic[0]-(constants[3]*states[5])/constants[38]))/((1.00000+states[1]/constants[42]+constants[3]/constants[39])*(1.00000+algebraic[0]/constants[41]+states[5]/constants[40]))
    algebraic[14] = custom_piecewise([greater_equal(algebraic[12] , 0.00000), algebraic[12] , True, algebraic[12]])
    rates[1] = algebraic[10]-algebraic[14]
    algebraic[1] = constants[1]-states[6]
    algebraic[7] = (((((((constants[29]/(1.00000+(constants[23]*states[6])/algebraic[1]))*states[0])/constants[26])*algebraic[1])/constants[24])*algebraic[2])/constants[25])/((1.00000+states[0]/constants[26])*(1.00000+algebraic[1]/constants[24]+states[6]/constants[27])*(1.00000+algebraic[2]/constants[25]+states[7]/constants[28]))
    algebraic[8] = custom_piecewise([greater_equal(algebraic[7] , 0.00000), algebraic[7] , True, algebraic[7]])
    algebraic[11] = ((constants[50]/(constants[48]*constants[46]))*(states[7]*states[6]-(algebraic[1]*algebraic[2]*states[2])/constants[44]))/((1.00000+algebraic[1]/constants[45]+states[6]/constants[46])*(1.00000+states[7]/constants[48]+algebraic[2]/constants[47])*(1.00000+states[2]/constants[49]))
    algebraic[13] = custom_piecewise([greater_equal(algebraic[11] , 0.00000), algebraic[11] , True, algebraic[11]])
    rates[7] = algebraic[8]-(algebraic[13]+algebraic[10])
    algebraic[15] = ((constants[56]/(constants[55]*constants[53]))*(states[2]*states[6]-(constants[5]*algebraic[1])/constants[51]))/((1.00000+algebraic[1]/constants[52]+states[6]/constants[53])*(1.00000+states[2]/constants[55]+constants[5]/constants[54]))
    algebraic[17] = custom_piecewise([greater_equal(algebraic[15] , 0.00000), algebraic[15] , True, algebraic[15]])
    rates[2] = algebraic[13]-algebraic[17]
    algebraic[3] = ((((((constants[16]*constants[6])/constants[10])*algebraic[1])/constants[11])*algebraic[0])/constants[12])/((1.00000+constants[6]/constants[10]+states[0]/constants[13])*(1.00000+algebraic[1]/constants[11]+states[6]/constants[14])*(1.00000+algebraic[0]/constants[12]+states[5]/constants[15]))
    algebraic[4] = custom_piecewise([greater_equal(algebraic[3] , 0.00000), algebraic[3] , True, algebraic[3]])
    algebraic[16] = (constants[75]*(power(states[5]/algebraic[0], constants[73])))/(power(constants[74], constants[73])+power(states[5]/algebraic[0], constants[73]))
    algebraic[18] = custom_piecewise([greater_equal(algebraic[16] , 0.00000), algebraic[16] , True, algebraic[16]])
    rates[5] = (algebraic[4]+algebraic[14])-algebraic[18]
    algebraic[5] = ((constants[22]/(constants[20]*constants[21]))*(states[0]*states[6]-(constants[7]*algebraic[1])/constants[17]))/((1.00000+states[0]/constants[20]+constants[7]/constants[18])*(1.00000+states[6]/constants[21]+algebraic[1]/constants[19]))
    algebraic[6] = custom_piecewise([greater_equal(algebraic[5] , 0.00000), algebraic[5] , True, algebraic[5]])
    algebraic[19] = (((constants[61]*states[0])/constants[60])*(1.00000-states[3]/(states[0]*constants[58]))*(power(states[0]/constants[60]+states[3]/constants[59], constants[57]-1.00000)))/(1.00000+power(states[0]/constants[60]+states[3]/constants[59], constants[57]))
    algebraic[20] = custom_piecewise([greater_equal(algebraic[19] , 0.00000), algebraic[19] , True, algebraic[19]])
    rates[0] = algebraic[4]-(algebraic[6]+algebraic[8]+algebraic[20])
    algebraic[21] = ((constants[64]*states[3])/constants[62])/(1.00000+states[3]/constants[62]+states[4]/constants[63])
    algebraic[22] = custom_piecewise([greater_equal(algebraic[21] , 0.00000), algebraic[21] , True, algebraic[21]])
    algebraic[27] = constants[80]*states[3]
    rates[3] = 0.500000*algebraic[20]-(algebraic[22]+algebraic[27])
    algebraic[25] = ((constants[72]/(constants[71]*constants[69]))*(states[4]*states[6]-(constants[4]*algebraic[1])/constants[67]))/((1.00000+states[4]/constants[71]+constants[4]/constants[70])*(1.00000+states[6]/constants[69]+algebraic[1]/constants[68]))
    algebraic[26] = custom_piecewise([greater_equal(algebraic[25] , 0.00000), algebraic[25] , True, algebraic[25]])
    algebraic[23] = ((constants[66]*states[4])/constants[65])/(1.00000+states[4]/constants[65])
    algebraic[24] = custom_piecewise([greater_equal(algebraic[23] , 0.00000), algebraic[23] , True, algebraic[23]])
    rates[4] = (algebraic[22]+algebraic[27])-(algebraic[26]+algebraic[24])
    algebraic[28] = ((constants[79]*states[6]*constants[8])/(constants[77]*constants[78]))/((1.00000+states[6]/constants[77]+algebraic[1]/constants[76])*(1.00000+constants[8]/constants[78]))
    algebraic[29] = custom_piecewise([greater_equal(algebraic[28] , 0.00000), algebraic[28] , True, algebraic[28]])
    rates[6] = (algebraic[4]+algebraic[8])-(algebraic[6]+algebraic[13]+algebraic[17]+algebraic[26]+algebraic[29])
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[2] = constants[2]-states[7]
    algebraic[9] = ((constants[37]/(constants[36]*constants[31]))*(states[7]*constants[9]-(states[1]*algebraic[2])/constants[30]))/(1.00000+states[7]/constants[36]+constants[9]/constants[32]+states[1]/constants[35]+algebraic[2]/constants[33]+(states[7]*constants[9])/(constants[36]*constants[31])+(states[1]*algebraic[2])/(constants[34]*constants[33]))
    algebraic[10] = custom_piecewise([greater_equal(algebraic[9] , 0.00000), algebraic[9] , True, algebraic[9]])
    algebraic[0] = constants[0]-states[5]
    algebraic[12] = ((constants[43]/(constants[41]*constants[42]))*(states[1]*algebraic[0]-(constants[3]*states[5])/constants[38]))/((1.00000+states[1]/constants[42]+constants[3]/constants[39])*(1.00000+algebraic[0]/constants[41]+states[5]/constants[40]))
    algebraic[14] = custom_piecewise([greater_equal(algebraic[12] , 0.00000), algebraic[12] , True, algebraic[12]])
    algebraic[1] = constants[1]-states[6]
    algebraic[7] = (((((((constants[29]/(1.00000+(constants[23]*states[6])/algebraic[1]))*states[0])/constants[26])*algebraic[1])/constants[24])*algebraic[2])/constants[25])/((1.00000+states[0]/constants[26])*(1.00000+algebraic[1]/constants[24]+states[6]/constants[27])*(1.00000+algebraic[2]/constants[25]+states[7]/constants[28]))
    algebraic[8] = custom_piecewise([greater_equal(algebraic[7] , 0.00000), algebraic[7] , True, algebraic[7]])
    algebraic[11] = ((constants[50]/(constants[48]*constants[46]))*(states[7]*states[6]-(algebraic[1]*algebraic[2]*states[2])/constants[44]))/((1.00000+algebraic[1]/constants[45]+states[6]/constants[46])*(1.00000+states[7]/constants[48]+algebraic[2]/constants[47])*(1.00000+states[2]/constants[49]))
    algebraic[13] = custom_piecewise([greater_equal(algebraic[11] , 0.00000), algebraic[11] , True, algebraic[11]])
    algebraic[15] = ((constants[56]/(constants[55]*constants[53]))*(states[2]*states[6]-(constants[5]*algebraic[1])/constants[51]))/((1.00000+algebraic[1]/constants[52]+states[6]/constants[53])*(1.00000+states[2]/constants[55]+constants[5]/constants[54]))
    algebraic[17] = custom_piecewise([greater_equal(algebraic[15] , 0.00000), algebraic[15] , True, algebraic[15]])
    algebraic[3] = ((((((constants[16]*constants[6])/constants[10])*algebraic[1])/constants[11])*algebraic[0])/constants[12])/((1.00000+constants[6]/constants[10]+states[0]/constants[13])*(1.00000+algebraic[1]/constants[11]+states[6]/constants[14])*(1.00000+algebraic[0]/constants[12]+states[5]/constants[15]))
    algebraic[4] = custom_piecewise([greater_equal(algebraic[3] , 0.00000), algebraic[3] , True, algebraic[3]])
    algebraic[16] = (constants[75]*(power(states[5]/algebraic[0], constants[73])))/(power(constants[74], constants[73])+power(states[5]/algebraic[0], constants[73]))
    algebraic[18] = custom_piecewise([greater_equal(algebraic[16] , 0.00000), algebraic[16] , True, algebraic[16]])
    algebraic[5] = ((constants[22]/(constants[20]*constants[21]))*(states[0]*states[6]-(constants[7]*algebraic[1])/constants[17]))/((1.00000+states[0]/constants[20]+constants[7]/constants[18])*(1.00000+states[6]/constants[21]+algebraic[1]/constants[19]))
    algebraic[6] = custom_piecewise([greater_equal(algebraic[5] , 0.00000), algebraic[5] , True, algebraic[5]])
    algebraic[19] = (((constants[61]*states[0])/constants[60])*(1.00000-states[3]/(states[0]*constants[58]))*(power(states[0]/constants[60]+states[3]/constants[59], constants[57]-1.00000)))/(1.00000+power(states[0]/constants[60]+states[3]/constants[59], constants[57]))
    algebraic[20] = custom_piecewise([greater_equal(algebraic[19] , 0.00000), algebraic[19] , True, algebraic[19]])
    algebraic[21] = ((constants[64]*states[3])/constants[62])/(1.00000+states[3]/constants[62]+states[4]/constants[63])
    algebraic[22] = custom_piecewise([greater_equal(algebraic[21] , 0.00000), algebraic[21] , True, algebraic[21]])
    algebraic[27] = constants[80]*states[3]
    algebraic[25] = ((constants[72]/(constants[71]*constants[69]))*(states[4]*states[6]-(constants[4]*algebraic[1])/constants[67]))/((1.00000+states[4]/constants[71]+constants[4]/constants[70])*(1.00000+states[6]/constants[69]+algebraic[1]/constants[68]))
    algebraic[26] = custom_piecewise([greater_equal(algebraic[25] , 0.00000), algebraic[25] , True, algebraic[25]])
    algebraic[23] = ((constants[66]*states[4])/constants[65])/(1.00000+states[4]/constants[65])
    algebraic[24] = custom_piecewise([greater_equal(algebraic[23] , 0.00000), algebraic[23] , True, algebraic[23]])
    algebraic[28] = ((constants[79]*states[6]*constants[8])/(constants[77]*constants[78]))/((1.00000+states[6]/constants[77]+algebraic[1]/constants[76])*(1.00000+constants[8]/constants[78]))
    algebraic[29] = custom_piecewise([greater_equal(algebraic[28] , 0.00000), algebraic[28] , True, algebraic[28]])
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
        self.A_tot = 5
        self.NAD_tot = 10
        self.C_tot = 1
        self.AC = 0.01
        self.BUT = 0.01
        self.ETOH = 0.1
        self.GLC = 15
        self.LAC = 0.1
        self.O = 0.2
        self.P = 10
        self.Km_GLC = 0.1
        self.Km_NAD = 0.1412
        self.Km_ADP = 0.04699
        self.Km_PYR = 2.5
        self.Km_NADH = 0.08999
        self.Km_ATP = 0.01867
        self.V_GLYC_max = 2397
        self.Keq = 21120.69
        self.Km_LAC = 100
        self.Km_NAD_1 = 2.4
        self.Km_PYR_1 = 1.5
        self.Km_NADH_1 = 0.08
        self.V_LDH_max = 5118
        self.Ki = 46.4159
        self.Km_NAD_2 = 0.4
        self.Km_COA = 0.014
        self.Km_PYR_2 = 1
        self.Km_NADH_2 = 0.1
        self.Km_ACCOA = 0.008
        self.V_PDH_max = 259
        self.Keq_1 = 0.0065
        self.Km_P = 2.6
        self.Ki_P = 2.6
        self.Ki_COA = 0.029
        self.Km_ACP = 0.7
        self.Ki_ACP = 0.2
        self.Ki_ACCOA = 0.2
        self.V_PTA_max = 42
        self.Keq_2 = 174.217
        self.Km_AC = 7
        self.Km_ATP_1 = 0.07
        self.Km_ADP_1 = 0.5
        self.Km_ACP_1 = 0.16
        self.V_ACK_max = 2700
        self.Keq_3 = 1
        self.Km_NAD_3 = 0.08
        self.Km_NADH_3 = 0.025
        self.Km_COA_1 = 0.008
        self.Km_ACCOA_1 = 0.007
        self.Km_ACAL = 10
        self.V_ACALDH_max = 97
        self.Keq_4 = 12354.9
        self.Km_NAD_4 = 0.08
        self.Km_NADH_4 = 0.05
        self.Km_ETOH = 1
        self.Km_ACAL_1 = 0.03
        self.V_ADH_max = 162
        self.N = 2.4
        self.Keq_5 = 9e12
        self.Km_ACLAC = 100
        self.Km_PYR_3 = 50
        self.V_ALS_max = 600
        self.Km_ACLAC_1 = 10
        self.Km_ACET = 100
        self.V_ALDC_max = 106
        self.Km_ACET_1 = 5
        self.V_ACETEFF_max = 200
        self.Keq_6 = 1400
        self.Km_NAD_5 = 0.16
        self.Km_NADH_5 = 0.02
        self.Km_BUT = 2.6
        self.Km_ACET_2 = 0.06
        self.V_ACETDH_max = 105
        self.N_1 = 2.58
        self.Km_ATP_2 = 6.196
        self.V_ATPase_max = 900
        self.Km_NAD_6 = 1
        self.Km_NADH_6 = 0.041
        self.Km_O = 0.2
        self.V_NOX_max = 118
        self.k = 0.0003

    def to_dict(self):
        return {
            "A_tot": self.A_tot,
            "NAD_tot": self.NAD_tot,
            "C_tot": self.C_tot,
            "AC": self.AC,
            "BUT": self.BUT,
            "ETOH": self.ETOH,
            "GLC": self.GLC,
            "LAC": self.LAC,
            "O": self.O,
            "P": self.P,
            "Km_GLC": self.Km_GLC,
            "Km_NAD": self.Km_NAD,
            "Km_ADP": self.Km_ADP,
            "Km_PYR": self.Km_PYR,
            "Km_NADH": self.Km_NADH,
            "Km_ATP": self.Km_ATP,
            "V_GLYC_max": self.V_GLYC_max,
            "Keq": self.Keq,
            "Km_LAC": self.Km_LAC,
            "Km_NAD_1": self.Km_NAD_1,
            "Km_PYR_1": self.Km_PYR_1,
            "Km_NADH_1": self.Km_NADH_1,
            "V_LDH_max": self.V_LDH_max,
            "Ki": self.Ki,
            "Km_NAD_2": self.Km_NAD_2,
            "Km_COA": self.Km_COA,
            "Km_PYR_2": self.Km_PYR_2,
            "Km_NADH_2": self.Km_NADH_2,
            "Km_ACCOA": self.Km_ACCOA,
            "V_PDH_max": self.V_PDH_max,
            "Keq_1": self.Keq_1,
            "Km_P": self.Km_P,
            "Ki_P": self.Ki_P,
            "Ki_COA": self.Ki_COA,
            "Km_ACP": self.Km_ACP,
            "Ki_ACP": self.Ki_ACP,
            "Ki_ACCOA": self.Ki_ACCOA,
            "V_PTA_max": self.V_PTA_max,
            "Keq_2": self.Keq_2,
            "Km_AC": self.Km_AC,
            "Km_ATP_1": self.Km_ATP_1,
            "Km_ADP_1": self.Km_ADP_1,
            "Km_ACP_1": self.Km_ACP_1,
            "V_ACK_max": self.V_ACK_max,
            "Keq_3": self.Keq_3,
            "Km_NAD_3": self.Km_NAD_3,
            "Km_NADH_3": self.Km_NADH_3,
            "Km_COA_1": self.Km_COA_1,
            "Km_ACCOA_1": self.Km_ACCOA_1,
            "Km_ACAL": self.Km_ACAL,
            "V_ACALDH_max": self.V_ACALDH_max,
            "Keq_4": self.Keq_4,
            "Km_NAD_4": self.Km_NAD_4,
            "Km_NADH_4": self.Km_NADH_4,
            "Km_ETOH": self.Km_ETOH,
            "Km_ACAL_1": self.Km_ACAL_1,
            "V_ADH_max": self.V_ADH_max,
            "N": self.N,
            "Keq_5": self.Keq_5,
            "Km_ACLAC": self.Km_ACLAC,
            "Km_PYR_3": self.Km_PYR_3,
            "V_ALS_max": self.V_ALS_max,
            "Km_ACLAC_1": self.Km_ACLAC_1,
            "Km_ACET": self.Km_ACET,
            "V_ALDC_max": self.V_ALDC_max,
            "Km_ACET_1": self.Km_ACET_1,
            "V_ACETEFF_max": self.V_ACETEFF_max,
            "Keq_6": self.Keq_6,
            "Km_NAD_5": self.Km_NAD_5,
            "Km_NADH_5": self.Km_NADH_5,
            "Km_BUT": self.Km_BUT,
            "Km_ACET_2": self.Km_ACET_2,
            "V_ACETDH_max": self.V_ACETDH_max,
            "N_1": self.N_1,
            "Km_ATP_2": self.Km_ATP_2,
            "V_ATPase_max": self.V_ATPase_max,
            "Km_NAD_6": self.Km_NAD_6,
            "Km_NADH_6": self.Km_NADH_6,
            "Km_O": self.Km_O,
            "V_NOX_max": self.V_NOX_max,
            "k": self.k,
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
        y0=[1, 0.03145, 0.11, 1e-5, 1e-5, 0.1, 3.67, 0.11],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "hoefnagel_starrenburg_martens_hugenholtz_kleerebezem_vanswam_bongers_westerhoff_snoep_2002"
        self.curve_names = [
            "PYR",
            "ACP",
            "ACAL",
            "ACLAC",
            "ACET",
            "ATP",
            "NADH",
            "ACCOA",
        ]
        self.state_names = ['PYR', 'ACP', 'ACAL', 'ACLAC', 'ACET', 'ATP', 'NADH', 'ACCOA']
        self.algebraic_names = ['ADP', 'NAD', 'COA', 'V_GLYC_temp', 'V_GLYC', 'V_LDH_temp', 'V_LDH', 'V_PDH_temp', 'V_PDH', 'V_PTA_temp', 'V_PTA', 'V_ACALDH_temp', 'V_ACK_temp', 'V_ACALDH', 'V_ACK', 'V_ADH_temp', 'V_ATPase_temp', 'V_ADH', 'V_ATPase', 'V_ALS_temp', 'V_ALS', 'V_ALDC_temp', 'V_ALDC', 'V_ACETEFF_temp', 'V_ACETEFF', 'V_ACETDH_temp', 'V_ACETDH', 'V_NEALC', 'V_NOX_temp', 'V_NOX']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 81
        p = self.params

        # direct mapping
        c[0] = p.A_tot
        c[1] = p.NAD_tot
        c[2] = p.C_tot
        c[3] = p.AC
        c[4] = p.BUT
        c[5] = p.ETOH
        c[6] = p.GLC
        c[7] = p.LAC
        c[8] = p.O
        c[9] = p.P
        c[10] = p.Km_GLC
        c[11] = p.Km_NAD
        c[12] = p.Km_ADP
        c[13] = p.Km_PYR
        c[14] = p.Km_NADH
        c[15] = p.Km_ATP
        c[16] = p.V_GLYC_max
        c[17] = p.Keq
        c[18] = p.Km_LAC
        c[19] = p.Km_NAD_1
        c[20] = p.Km_PYR_1
        c[21] = p.Km_NADH_1
        c[22] = p.V_LDH_max
        c[23] = p.Ki
        c[24] = p.Km_NAD_2
        c[25] = p.Km_COA
        c[26] = p.Km_PYR_2
        c[27] = p.Km_NADH_2
        c[28] = p.Km_ACCOA
        c[29] = p.V_PDH_max
        c[30] = p.Keq_1
        c[31] = p.Km_P
        c[32] = p.Ki_P
        c[33] = p.Ki_COA
        c[34] = p.Km_ACP
        c[35] = p.Ki_ACP
        c[36] = p.Ki_ACCOA
        c[37] = p.V_PTA_max
        c[38] = p.Keq_2
        c[39] = p.Km_AC
        c[40] = p.Km_ATP_1
        c[41] = p.Km_ADP_1
        c[42] = p.Km_ACP_1
        c[43] = p.V_ACK_max
        c[44] = p.Keq_3
        c[45] = p.Km_NAD_3
        c[46] = p.Km_NADH_3
        c[47] = p.Km_COA_1
        c[48] = p.Km_ACCOA_1
        c[49] = p.Km_ACAL
        c[50] = p.V_ACALDH_max
        c[51] = p.Keq_4
        c[52] = p.Km_NAD_4
        c[53] = p.Km_NADH_4
        c[54] = p.Km_ETOH
        c[55] = p.Km_ACAL_1
        c[56] = p.V_ADH_max
        c[57] = p.N
        c[58] = p.Keq_5
        c[59] = p.Km_ACLAC
        c[60] = p.Km_PYR_3
        c[61] = p.V_ALS_max
        c[62] = p.Km_ACLAC_1
        c[63] = p.Km_ACET
        c[64] = p.V_ALDC_max
        c[65] = p.Km_ACET_1
        c[66] = p.V_ACETEFF_max
        c[67] = p.Keq_6
        c[68] = p.Km_NAD_5
        c[69] = p.Km_NADH_5
        c[70] = p.Km_BUT
        c[71] = p.Km_ACET_2
        c[72] = p.V_ACETDH_max
        c[73] = p.N_1
        c[74] = p.Km_ATP_2
        c[75] = p.V_ATPase_max
        c[76] = p.Km_NAD_6
        c[77] = p.Km_NADH_6
        c[78] = p.Km_O
        c[79] = p.V_NOX_max
        c[80] = p.k

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
