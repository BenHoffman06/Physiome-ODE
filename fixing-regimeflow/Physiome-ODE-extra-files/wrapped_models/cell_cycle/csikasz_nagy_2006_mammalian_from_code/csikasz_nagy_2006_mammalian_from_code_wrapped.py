# Size of variable arrays:
sizeAlgebraic = 30
sizeStates = 14
sizeConstants = 93
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (minute)"
    legend_states[0] = "CycA in component CycA (dimensionless)"
    legend_constants[0] = "k_assa in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[1] = "k_dissa in component kinetic_parameters (first_order_rate_constant)"
    legend_algebraic[20] = "V_di in component V_di (first_order_rate_constant)"
    legend_algebraic[21] = "V_sa in component V_sa (first_order_rate_constant)"
    legend_algebraic[14] = "V_da in component V_da (first_order_rate_constant)"
    legend_states[1] = "Tri_A in component Tri_A (dimensionless)"
    legend_states[2] = "CKI in component CKI (dimensionless)"
    legend_states[3] = "CycB in component CycB (dimensionless)"
    legend_constants[2] = "k_assb in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[3] = "k_dissb in component kinetic_parameters (first_order_rate_constant)"
    legend_algebraic[24] = "V_sb in component V_sb (first_order_rate_constant)"
    legend_algebraic[25] = "V_db in component V_db (first_order_rate_constant)"
    legend_algebraic[29] = "V_25 in component V_25 (first_order_rate_constant)"
    legend_algebraic[27] = "V_wee in component V_wee (first_order_rate_constant)"
    legend_states[4] = "pB in component pB (dimensionless)"
    legend_states[5] = "BCKI in component BCKI (dimensionless)"
    legend_states[6] = "CycE in component CycE (dimensionless)"
    legend_constants[4] = "k_disse in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[5] = "k_asse in component kinetic_parameters (first_order_rate_constant)"
    legend_algebraic[23] = "V_se in component V_se (first_order_rate_constant)"
    legend_algebraic[13] = "V_de in component V_de (first_order_rate_constant)"
    legend_states[7] = "Tri_E in component Tri_E (dimensionless)"
    legend_algebraic[1] = "CycD in component CycD (dimensionless)"
    legend_constants[6] = "CycD_0 in component CycD (dimensionless)"
    legend_states[8] = "mass in component mass (dimensionless)"
    legend_states[9] = "Cdc20_A in component Cdc20_A (dimensionless)"
    legend_constants[7] = "k_a20 in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[8] = "k_i20 in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[9] = "k_d20 in component kinetic_parameters (first_order_rate_constant)"
    legend_states[10] = "APCP in component APCP (dimensionless)"
    legend_states[11] = "Cdc20_i in component Cdc20_i (dimensionless)"
    legend_constants[10] = "J_a20 in component Cdc20_A (dimensionless)"
    legend_constants[11] = "J_i20 in component Cdc20_A (dimensionless)"
    legend_constants[12] = "k_s20p in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[13] = "k_s20pp in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[14] = "n20 in component Cdc20_i (dimensionless)"
    legend_constants[15] = "J_20 in component Cdc20_i (dimensionless)"
    legend_constants[16] = "J_a20 in component Cdc20_i (dimensionless)"
    legend_constants[17] = "J_i20 in component Cdc20_i (dimensionless)"
    legend_algebraic[0] = "APC in component APC (dimensionless)"
    legend_constants[18] = "APC_T in component APC (dimensionless)"
    legend_constants[19] = "k_aie in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[20] = "k_iie in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[21] = "J_aie in component APCP (dimensionless)"
    legend_constants[22] = "J_iie in component APCP (dimensionless)"
    legend_states[12] = "pBCKI in component pBCKI (dimensionless)"
    legend_algebraic[18] = "V_si in component V_si (first_order_rate_constant)"
    legend_algebraic[9] = "Cdh1_i in component Cdh1_i (dimensionless)"
    legend_constants[23] = "Cdh1_T in component Cdh1_i (dimensionless)"
    legend_states[13] = "Cdh1 in component Cdh1 (dimensionless)"
    legend_algebraic[17] = "V_ah1 in component V_ah1 (first_order_rate_constant)"
    legend_algebraic[19] = "V_ih1 in component V_ih1 (first_order_rate_constant)"
    legend_constants[24] = "J_ah1 in component Cdh1 (dimensionless)"
    legend_constants[25] = "J_ih1 in component Cdh1 (dimensionless)"
    legend_constants[26] = "mu in component mass (first_order_rate_constant)"
    legend_constants[27] = "maxmass in component mass (dimensionless)"
    legend_algebraic[10] = "V_atf in component V_atf (first_order_rate_constant)"
    legend_constants[28] = "k_atfp in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[29] = "k_atfapp in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[30] = "k_atfepp in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[31] = "k_atfdpp in component kinetic_parameters (first_order_rate_constant)"
    legend_algebraic[11] = "V_itf in component V_itf (first_order_rate_constant)"
    legend_constants[32] = "k_itfp in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[33] = "k_itfapp in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[34] = "k_itfbpp in component kinetic_parameters (first_order_rate_constant)"
    legend_algebraic[12] = "TF_E in component TF_E (dimensionless)"
    legend_constants[35] = "J_itf in component TF_E (dimensionless)"
    legend_constants[36] = "J_atf in component TF_E (dimensionless)"
    legend_constants[37] = "k_dep in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[38] = "k_deepp in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[39] = "k_deapp in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[40] = "k_debpp in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[41] = "k_dap in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[42] = "k_dapp in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[43] = "k_dappp in component kinetic_parameters (first_order_rate_constant)"
    legend_algebraic[16] = "TF_I in component TF_I (dimensionless)"
    legend_constants[44] = "k_afi in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[45] = "k_ifip in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[46] = "k_ifibpp in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[47] = "J_ifi in component TF_I (dimensionless)"
    legend_constants[48] = "J_afi in component TF_I (dimensionless)"
    legend_algebraic[15] = "Cdc14 in component TF_I (dimensionless)"
    legend_constants[49] = "k_ah1p in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[50] = "k_ah1pp in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[51] = "k_ih1p in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[52] = "k_ih1app in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[53] = "k_ih1bpp in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[54] = "k_ih1epp in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[55] = "k_ih1dpp in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[56] = "k_sip in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[57] = "k_sipp in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[58] = "k_dip in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[59] = "k_diapp in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[60] = "k_diepp in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[61] = "k_didpp in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[62] = "k_dibpp in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[63] = "k_14di in component kinetic_parameters (dimensionless)"
    legend_algebraic[2] = "preMPF in component preMPF (dimensionless)"
    legend_algebraic[3] = "CycBT in component CycBT (dimensionless)"
    legend_algebraic[4] = "CycAT in component CycAT (dimensionless)"
    legend_algebraic[5] = "CycET in component CycET (dimensionless)"
    legend_algebraic[6] = "Tri_B in component Tri_B (dimensionless)"
    legend_algebraic[7] = "CKIT in component CKIT (dimensionless)"
    legend_algebraic[8] = "Cdc20_T in component Cdc20_T (dimensionless)"
    legend_algebraic[22] = "TF_B in component TF_B (dimensionless)"
    legend_constants[64] = "k_afb in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[65] = "k_ifb in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[66] = "J_ifb in component TF_B (dimensionless)"
    legend_constants[67] = "J_afb in component TF_B (dimensionless)"
    legend_constants[68] = "k_sbp in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[69] = "k_sbpp in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[70] = "k_sap in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[71] = "k_sapp in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[72] = "k_sep in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[73] = "k_sepp in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[74] = "k_dbp in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[75] = "k_dbhpp in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[76] = "k_dbcpp in component kinetic_parameters (first_order_rate_constant)"
    legend_algebraic[26] = "Wee1 in component Wee1 (dimensionless)"
    legend_constants[77] = "k_aweep in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[78] = "k_aweepp in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[79] = "k_iweep in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[80] = "k_iweepp in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[81] = "J_iwee in component Wee1 (dimensionless)"
    legend_constants[82] = "J_awee in component Wee1 (dimensionless)"
    legend_constants[83] = "k_weep in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[84] = "k_weepp in component kinetic_parameters (first_order_rate_constant)"
    legend_algebraic[28] = "Cdc25 in component Cdc25 (dimensionless)"
    legend_constants[85] = "k_a25p in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[86] = "k_a25pp in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[87] = "k_i25p in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[88] = "k_i25pp in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[89] = "J_i25 in component Cdc25 (dimensionless)"
    legend_constants[90] = "J_a25 in component Cdc25 (dimensionless)"
    legend_constants[91] = "k_25p in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[92] = "k_25pp in component kinetic_parameters (first_order_rate_constant)"
    legend_rates[0] = "d/dt CycA in component CycA (dimensionless)"
    legend_rates[3] = "d/dt CycB in component CycB (dimensionless)"
    legend_rates[6] = "d/dt CycE in component CycE (dimensionless)"
    legend_rates[9] = "d/dt Cdc20_A in component Cdc20_A (dimensionless)"
    legend_rates[11] = "d/dt Cdc20_i in component Cdc20_i (dimensionless)"
    legend_rates[10] = "d/dt APCP in component APCP (dimensionless)"
    legend_rates[4] = "d/dt pB in component pB (dimensionless)"
    legend_rates[5] = "d/dt BCKI in component BCKI (dimensionless)"
    legend_rates[12] = "d/dt pBCKI in component pBCKI (dimensionless)"
    legend_rates[1] = "d/dt Tri_A in component Tri_A (dimensionless)"
    legend_rates[7] = "d/dt Tri_E in component Tri_E (dimensionless)"
    legend_rates[2] = "d/dt CKI in component CKI (dimensionless)"
    legend_rates[13] = "d/dt Cdh1 in component Cdh1 (dimensionless)"
    legend_rates[8] = "d/dt mass in component mass (dimensionless)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 0.009940445423126221
    constants[0] = 25
    constants[1] = 1
    states[1] = 0.01715379953384399
    states[2] = 0.2954076826572418
    states[3] = 0.1668413728475571
    constants[2] = 0
    constants[3] = 0
    states[4] = 0.009814870543777943
    states[5] = 0
    states[6] = 0.07760512828826904
    constants[4] = 1
    constants[5] = 50
    states[7] = 0.3117263317108154
    constants[6] = 0.05
    states[8] = 1.174216866493225
    states[9] = 0.6605867147445679
    constants[7] = 0.5
    constants[8] = 0.25
    constants[9] = 0.15
    states[10] = 0.6716265678405762
    states[11] = 0.01855352707207203
    constants[10] = 0.005
    constants[11] = 0.005
    constants[12] = 0
    constants[13] = 0.15
    constants[14] = 1
    constants[15] = 1
    constants[16] = 0.005
    constants[17] = 0.005
    constants[18] = 1
    constants[19] = 0.07
    constants[20] = 0.18
    constants[21] = 0.01
    constants[22] = 0.01
    states[12] = 0
    constants[23] = 1
    states[13] = 0.9992357492446899
    constants[24] = 0.01
    constants[25] = 0.01
    constants[26] = 0.004951
    constants[27] = 10000
    constants[28] = 0
    constants[29] = 0.2
    constants[30] = 0.5
    constants[31] = 3
    constants[32] = 0.25
    constants[33] = 0.1
    constants[34] = 0.1
    constants[35] = 0.01
    constants[36] = 0.01
    constants[37] = 0.01
    constants[38] = 0.1
    constants[39] = 0.5
    constants[40] = 0.5
    constants[41] = 0.02
    constants[42] = 2
    constants[43] = 0
    constants[44] = 88
    constants[45] = 88
    constants[46] = 88
    constants[47] = 88
    constants[48] = 88
    constants[49] = 0.18
    constants[50] = 3.5
    constants[51] = 0
    constants[52] = 0.2
    constants[53] = 1
    constants[54] = 0.1
    constants[55] = 0
    constants[56] = 1.8
    constants[57] = 0
    constants[58] = 0.8
    constants[59] = 5
    constants[60] = 5
    constants[61] = 0
    constants[62] = 5
    constants[63] = 0
    constants[64] = 1
    constants[65] = 0.1
    constants[66] = 0.1
    constants[67] = 0.1
    constants[68] = 0.01
    constants[69] = 0.03
    constants[70] = 0
    constants[71] = 0.025
    constants[72] = 0.01
    constants[73] = 0.18
    constants[74] = 0.005
    constants[75] = 2
    constants[76] = 0.1
    constants[77] = 0.3
    constants[78] = 0
    constants[79] = 0
    constants[80] = 1
    constants[81] = 0.05
    constants[82] = 0.05
    constants[83] = 0.02
    constants[84] = 0.2
    constants[85] = 0
    constants[86] = 1
    constants[87] = 0.3
    constants[88] = 0
    constants[89] = 0.1
    constants[90] = 0.1
    constants[91] = 0.01
    constants[92] = 5
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[9] = ((constants[7]*states[10]*states[11])/(constants[10]+states[11])-(states[9]*constants[8])/(constants[11]+states[9]))-states[9]*constants[9]
    rates[11] = (((constants[12]+constants[13]*(power(states[3], constants[14])))/(power(constants[15], constants[14])+power(states[3], constants[14]))+(states[9]*constants[8])/(constants[17]+states[9]))-constants[9]*states[11])-(constants[7]*states[10]*states[11])/(constants[16]+states[11])
    rates[8] = constants[26]*states[8]*(1.00000-states[8]/constants[27])
    algebraic[0] = (constants[18]-states[10])/1.00000
    rates[10] = (constants[19]*states[3]*algebraic[0])/(constants[21]+algebraic[0])-(constants[20]*states[10])/(constants[22]+states[10])
    algebraic[9] = (constants[23]-states[13])/1.00000
    algebraic[15] = states[9]
    algebraic[17] = constants[49]+constants[50]*algebraic[15]
    algebraic[1] = constants[6]*states[8]
    algebraic[19] = constants[51]+constants[52]*states[0]+constants[53]*states[3]+constants[54]*states[6]+constants[55]*algebraic[1]
    rates[13] = (algebraic[9]*algebraic[17])/(constants[24]+algebraic[9])-(states[13]*algebraic[19])/(constants[25]+states[13])
    algebraic[20] = (constants[58]+constants[59]*states[0]+constants[62]*states[3]+constants[60]*states[6]+constants[61]*algebraic[1])/(1.00000+constants[63]*algebraic[15])
    algebraic[14] = constants[41]+(constants[42]+constants[43])*states[9]+constants[43]*states[11]
    rates[1] = ((constants[0]*states[2]*states[0]-constants[1]*states[1])-algebraic[20]*states[1])-algebraic[14]*states[1]
    algebraic[13] = constants[37]+constants[38]*states[6]+constants[39]*states[0]+constants[40]*states[3]
    rates[7] = ((constants[5]*states[2]*states[6]-constants[4]*states[7])-algebraic[20]*states[7])-algebraic[13]*states[7]
    algebraic[10] = constants[28]+constants[29]*states[0]+constants[30]*states[6]+constants[31]*algebraic[1]
    algebraic[11] = constants[32]+constants[33]*states[0]+constants[34]*states[3]
    algebraic[12] = (2.00000*algebraic[10]*constants[35])/((algebraic[11]-algebraic[10])+constants[36]*algebraic[11]+constants[35]*algebraic[10]+power(power((algebraic[11]-algebraic[10])+constants[36]*algebraic[11]+constants[35]*algebraic[10], 2.00000)-4.00000*(algebraic[11]-algebraic[10])*constants[35]*algebraic[10], 1.0/2))
    algebraic[21] = states[8]*(constants[70]+constants[71]*algebraic[12])
    rates[0] = ((constants[1]*states[1]+algebraic[20]*states[1]+algebraic[21])-algebraic[14]*states[0])-constants[0]*states[2]*states[0]
    algebraic[23] = states[8]*(constants[72]+constants[73]*algebraic[12])
    rates[6] = ((constants[4]*states[7]+algebraic[20]*states[7]+algebraic[23])-algebraic[13]*states[6])-constants[5]*states[2]*states[6]
    algebraic[25] = constants[74]+constants[75]*states[13]+constants[76]*states[9]
    algebraic[16] = (2.00000*constants[44]*algebraic[15]*constants[47])/(((constants[45]+constants[46]*states[3])-constants[44]*algebraic[15])+constants[48]*(constants[45]+constants[46]*states[3])+constants[47]*constants[44]*algebraic[15]+power(power(((constants[45]+constants[46]*states[3])-constants[44]*algebraic[15])+constants[48]*(constants[45]+constants[46]*states[3])+constants[47]*constants[44]*algebraic[15], 2.00000)-4.00000*((constants[45]+constants[46]*states[3])-constants[44]*algebraic[15])*constants[47]*constants[44]*algebraic[15], 1.0/2))
    algebraic[18] = constants[56]+constants[57]*algebraic[16]
    rates[2] = (((((((-constants[2]*states[3]*states[2]+constants[3]*states[5])-constants[2]*states[4]*states[2])+constants[3]*states[12]+algebraic[25]*states[5]+algebraic[25]*states[12]+algebraic[18])-algebraic[20]*states[2])-constants[0]*states[2]*states[0])+constants[1]*states[1]+algebraic[14]*states[1])-constants[5]*states[2]*states[6])+constants[4]*states[7]+algebraic[13]*states[7]
    algebraic[22] = (2.00000*constants[64]*states[3]*constants[66])/((constants[65]-constants[64]*states[3])+constants[67]*constants[65]+constants[66]*constants[64]*states[3]+power(power((constants[65]-constants[64]*states[3])+constants[67]*constants[65]+constants[66]*constants[64]*states[3], 2.00000)-4.00000*(constants[65]-constants[64]*states[3])*constants[64]*states[3]*constants[66], 1.0/2))
    algebraic[24] = states[8]*(constants[68]+constants[69]*algebraic[22])
    algebraic[28] = (2.00000*(constants[85]+constants[86]*states[3])*constants[89])/(((constants[87]+constants[88]*algebraic[15])-(constants[85]+constants[86]*states[3]))+constants[90]*(constants[87]+constants[88]*algebraic[15])+(constants[85]+constants[86]*states[3])*constants[89]+power(power(((constants[87]+constants[88]*algebraic[15])-(constants[85]+constants[86]*states[3]))+constants[90]*(constants[87]+constants[88]*algebraic[15])+(constants[85]+constants[86]*states[3])*constants[89], 2.00000)-4.00000*((constants[87]+constants[88]*algebraic[15])-(constants[85]+constants[86]*states[3]))*(constants[85]+constants[86]*states[3])*constants[89], 1.0/2))
    algebraic[29] = constants[91]+constants[92]*algebraic[28]
    algebraic[26] = (2.00000*(constants[77]+constants[78]*algebraic[15])*constants[81])/(((constants[79]+constants[80]*states[3])-(constants[77]+constants[78]*algebraic[15]))+constants[82]*(constants[79]+constants[80]*states[3])+constants[81]*(constants[77]+constants[78]*algebraic[15])+power(power(((constants[79]+constants[80]*states[3])-(constants[77]+constants[78]*algebraic[15]))+constants[82]*(constants[79]+constants[80]*states[3])+constants[81]*(constants[77]+constants[78]*algebraic[15]), 2.00000)-4.00000*((constants[79]+constants[80]*states[3])-(constants[77]+constants[78]*algebraic[15]))*(constants[77]+constants[78]*algebraic[15])*constants[81], 1.0/2))
    algebraic[27] = constants[83]+constants[84]*algebraic[26]
    rates[3] = ((((algebraic[24]-algebraic[25]*states[3])+algebraic[29]*states[4])-algebraic[27]*states[3])-constants[2]*states[3]*states[2])+constants[3]*states[5]+algebraic[20]*states[5]
    rates[4] = (((algebraic[27]*states[3]-algebraic[25]*states[4])-constants[2]*states[4]*states[2])+constants[3]*states[12]+algebraic[20]*states[12])-algebraic[29]*states[4]
    rates[5] = ((((constants[2]*states[3]*states[2]-constants[3]*states[5])+algebraic[29]*states[12])-algebraic[27]*states[5])-algebraic[25]*states[5])-algebraic[20]*states[5]
    rates[12] = ((((constants[2]*states[4]*states[2]-constants[3]*states[12])-algebraic[29]*states[12])+algebraic[27]*states[5])-algebraic[25]*states[12])-algebraic[20]*states[12]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = (constants[18]-states[10])/1.00000
    algebraic[9] = (constants[23]-states[13])/1.00000
    algebraic[15] = states[9]
    algebraic[17] = constants[49]+constants[50]*algebraic[15]
    algebraic[1] = constants[6]*states[8]
    algebraic[19] = constants[51]+constants[52]*states[0]+constants[53]*states[3]+constants[54]*states[6]+constants[55]*algebraic[1]
    algebraic[20] = (constants[58]+constants[59]*states[0]+constants[62]*states[3]+constants[60]*states[6]+constants[61]*algebraic[1])/(1.00000+constants[63]*algebraic[15])
    algebraic[14] = constants[41]+(constants[42]+constants[43])*states[9]+constants[43]*states[11]
    algebraic[13] = constants[37]+constants[38]*states[6]+constants[39]*states[0]+constants[40]*states[3]
    algebraic[10] = constants[28]+constants[29]*states[0]+constants[30]*states[6]+constants[31]*algebraic[1]
    algebraic[11] = constants[32]+constants[33]*states[0]+constants[34]*states[3]
    algebraic[12] = (2.00000*algebraic[10]*constants[35])/((algebraic[11]-algebraic[10])+constants[36]*algebraic[11]+constants[35]*algebraic[10]+power(power((algebraic[11]-algebraic[10])+constants[36]*algebraic[11]+constants[35]*algebraic[10], 2.00000)-4.00000*(algebraic[11]-algebraic[10])*constants[35]*algebraic[10], 1.0/2))
    algebraic[21] = states[8]*(constants[70]+constants[71]*algebraic[12])
    algebraic[23] = states[8]*(constants[72]+constants[73]*algebraic[12])
    algebraic[25] = constants[74]+constants[75]*states[13]+constants[76]*states[9]
    algebraic[16] = (2.00000*constants[44]*algebraic[15]*constants[47])/(((constants[45]+constants[46]*states[3])-constants[44]*algebraic[15])+constants[48]*(constants[45]+constants[46]*states[3])+constants[47]*constants[44]*algebraic[15]+power(power(((constants[45]+constants[46]*states[3])-constants[44]*algebraic[15])+constants[48]*(constants[45]+constants[46]*states[3])+constants[47]*constants[44]*algebraic[15], 2.00000)-4.00000*((constants[45]+constants[46]*states[3])-constants[44]*algebraic[15])*constants[47]*constants[44]*algebraic[15], 1.0/2))
    algebraic[18] = constants[56]+constants[57]*algebraic[16]
    algebraic[22] = (2.00000*constants[64]*states[3]*constants[66])/((constants[65]-constants[64]*states[3])+constants[67]*constants[65]+constants[66]*constants[64]*states[3]+power(power((constants[65]-constants[64]*states[3])+constants[67]*constants[65]+constants[66]*constants[64]*states[3], 2.00000)-4.00000*(constants[65]-constants[64]*states[3])*constants[64]*states[3]*constants[66], 1.0/2))
    algebraic[24] = states[8]*(constants[68]+constants[69]*algebraic[22])
    algebraic[28] = (2.00000*(constants[85]+constants[86]*states[3])*constants[89])/(((constants[87]+constants[88]*algebraic[15])-(constants[85]+constants[86]*states[3]))+constants[90]*(constants[87]+constants[88]*algebraic[15])+(constants[85]+constants[86]*states[3])*constants[89]+power(power(((constants[87]+constants[88]*algebraic[15])-(constants[85]+constants[86]*states[3]))+constants[90]*(constants[87]+constants[88]*algebraic[15])+(constants[85]+constants[86]*states[3])*constants[89], 2.00000)-4.00000*((constants[87]+constants[88]*algebraic[15])-(constants[85]+constants[86]*states[3]))*(constants[85]+constants[86]*states[3])*constants[89], 1.0/2))
    algebraic[29] = constants[91]+constants[92]*algebraic[28]
    algebraic[26] = (2.00000*(constants[77]+constants[78]*algebraic[15])*constants[81])/(((constants[79]+constants[80]*states[3])-(constants[77]+constants[78]*algebraic[15]))+constants[82]*(constants[79]+constants[80]*states[3])+constants[81]*(constants[77]+constants[78]*algebraic[15])+power(power(((constants[79]+constants[80]*states[3])-(constants[77]+constants[78]*algebraic[15]))+constants[82]*(constants[79]+constants[80]*states[3])+constants[81]*(constants[77]+constants[78]*algebraic[15]), 2.00000)-4.00000*((constants[79]+constants[80]*states[3])-(constants[77]+constants[78]*algebraic[15]))*(constants[77]+constants[78]*algebraic[15])*constants[81], 1.0/2))
    algebraic[27] = constants[83]+constants[84]*algebraic[26]
    algebraic[2] = states[4]+states[5]
    algebraic[3] = states[3]+states[4]+states[5]+states[12]
    algebraic[4] = states[0]+states[1]
    algebraic[5] = states[6]+states[7]
    algebraic[6] = states[5]+states[12]
    algebraic[7] = states[2]+states[5]+states[12]+states[1]+states[7]
    algebraic[8] = states[11]+states[9]
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
        self.k_assa = 25
        self.k_dissa = 1
        self.k_assb = 0
        self.k_dissb = 0
        self.k_disse = 1
        self.k_asse = 50
        self.CycD_0 = 0.05
        self.k_a20 = 0.5
        self.k_i20 = 0.25
        self.k_d20 = 0.15
        self.J_a20 = 0.005
        self.J_i20 = 0.005
        self.k_s20p = 0
        self.k_s20pp = 0.15
        self.n20 = 1
        self.J_20 = 1
        self.J_a20_1 = 0.005
        self.J_i20_1 = 0.005
        self.APC_T = 1
        self.k_aie = 0.07
        self.k_iie = 0.18
        self.J_aie = 0.01
        self.J_iie = 0.01
        self.Cdh1_T = 1
        self.J_ah1 = 0.01
        self.J_ih1 = 0.01
        self.mu = 0.004951
        self.maxmass = 10000
        self.k_atfp = 0
        self.k_atfapp = 0.2
        self.k_atfepp = 0.5
        self.k_atfdpp = 3
        self.k_itfp = 0.25
        self.k_itfapp = 0.1
        self.k_itfbpp = 0.1
        self.J_itf = 0.01
        self.J_atf = 0.01
        self.k_dep = 0.01
        self.k_deepp = 0.1
        self.k_deapp = 0.5
        self.k_debpp = 0.5
        self.k_dap = 0.02
        self.k_dapp = 2
        self.k_dappp = 0
        self.k_afi = 88
        self.k_ifip = 88
        self.k_ifibpp = 88
        self.J_ifi = 88
        self.J_afi = 88
        self.k_ah1p = 0.18
        self.k_ah1pp = 3.5
        self.k_ih1p = 0
        self.k_ih1app = 0.2
        self.k_ih1bpp = 1
        self.k_ih1epp = 0.1
        self.k_ih1dpp = 0
        self.k_sip = 1.8
        self.k_sipp = 0
        self.k_dip = 0.8
        self.k_diapp = 5
        self.k_diepp = 5
        self.k_didpp = 0
        self.k_dibpp = 5
        self.k_14di = 0
        self.k_afb = 1
        self.k_ifb = 0.1
        self.J_ifb = 0.1
        self.J_afb = 0.1
        self.k_sbp = 0.01
        self.k_sbpp = 0.03
        self.k_sap = 0
        self.k_sapp = 0.025
        self.k_sep = 0.01
        self.k_sepp = 0.18
        self.k_dbp = 0.005
        self.k_dbhpp = 2
        self.k_dbcpp = 0.1
        self.k_aweep = 0.3
        self.k_aweepp = 0
        self.k_iweep = 0
        self.k_iweepp = 1
        self.J_iwee = 0.05
        self.J_awee = 0.05
        self.k_weep = 0.02
        self.k_weepp = 0.2
        self.k_a25p = 0
        self.k_a25pp = 1
        self.k_i25p = 0.3
        self.k_i25pp = 0
        self.J_i25 = 0.1
        self.J_a25 = 0.1
        self.k_25p = 0.01
        self.k_25pp = 5

    def to_dict(self):
        return {
            "k_assa": self.k_assa,
            "k_dissa": self.k_dissa,
            "k_assb": self.k_assb,
            "k_dissb": self.k_dissb,
            "k_disse": self.k_disse,
            "k_asse": self.k_asse,
            "CycD_0": self.CycD_0,
            "k_a20": self.k_a20,
            "k_i20": self.k_i20,
            "k_d20": self.k_d20,
            "J_a20": self.J_a20,
            "J_i20": self.J_i20,
            "k_s20p": self.k_s20p,
            "k_s20pp": self.k_s20pp,
            "n20": self.n20,
            "J_20": self.J_20,
            "J_a20_1": self.J_a20_1,
            "J_i20_1": self.J_i20_1,
            "APC_T": self.APC_T,
            "k_aie": self.k_aie,
            "k_iie": self.k_iie,
            "J_aie": self.J_aie,
            "J_iie": self.J_iie,
            "Cdh1_T": self.Cdh1_T,
            "J_ah1": self.J_ah1,
            "J_ih1": self.J_ih1,
            "mu": self.mu,
            "maxmass": self.maxmass,
            "k_atfp": self.k_atfp,
            "k_atfapp": self.k_atfapp,
            "k_atfepp": self.k_atfepp,
            "k_atfdpp": self.k_atfdpp,
            "k_itfp": self.k_itfp,
            "k_itfapp": self.k_itfapp,
            "k_itfbpp": self.k_itfbpp,
            "J_itf": self.J_itf,
            "J_atf": self.J_atf,
            "k_dep": self.k_dep,
            "k_deepp": self.k_deepp,
            "k_deapp": self.k_deapp,
            "k_debpp": self.k_debpp,
            "k_dap": self.k_dap,
            "k_dapp": self.k_dapp,
            "k_dappp": self.k_dappp,
            "k_afi": self.k_afi,
            "k_ifip": self.k_ifip,
            "k_ifibpp": self.k_ifibpp,
            "J_ifi": self.J_ifi,
            "J_afi": self.J_afi,
            "k_ah1p": self.k_ah1p,
            "k_ah1pp": self.k_ah1pp,
            "k_ih1p": self.k_ih1p,
            "k_ih1app": self.k_ih1app,
            "k_ih1bpp": self.k_ih1bpp,
            "k_ih1epp": self.k_ih1epp,
            "k_ih1dpp": self.k_ih1dpp,
            "k_sip": self.k_sip,
            "k_sipp": self.k_sipp,
            "k_dip": self.k_dip,
            "k_diapp": self.k_diapp,
            "k_diepp": self.k_diepp,
            "k_didpp": self.k_didpp,
            "k_dibpp": self.k_dibpp,
            "k_14di": self.k_14di,
            "k_afb": self.k_afb,
            "k_ifb": self.k_ifb,
            "J_ifb": self.J_ifb,
            "J_afb": self.J_afb,
            "k_sbp": self.k_sbp,
            "k_sbpp": self.k_sbpp,
            "k_sap": self.k_sap,
            "k_sapp": self.k_sapp,
            "k_sep": self.k_sep,
            "k_sepp": self.k_sepp,
            "k_dbp": self.k_dbp,
            "k_dbhpp": self.k_dbhpp,
            "k_dbcpp": self.k_dbcpp,
            "k_aweep": self.k_aweep,
            "k_aweepp": self.k_aweepp,
            "k_iweep": self.k_iweep,
            "k_iweepp": self.k_iweepp,
            "J_iwee": self.J_iwee,
            "J_awee": self.J_awee,
            "k_weep": self.k_weep,
            "k_weepp": self.k_weepp,
            "k_a25p": self.k_a25p,
            "k_a25pp": self.k_a25pp,
            "k_i25p": self.k_i25p,
            "k_i25pp": self.k_i25pp,
            "J_i25": self.J_i25,
            "J_a25": self.J_a25,
            "k_25p": self.k_25p,
            "k_25pp": self.k_25pp,
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
        y0=[0.009940445423126221, 0.01715379953384399, 0.2954076826572418, 0.1668413728475571, 0.009814870543777943, 0, 0.07760512828826904, 0.3117263317108154, 1.174216866493225, 0.6605867147445679, 0.6716265678405762, 0.01855352707207203, 0, 0.9992357492446899],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "csikasz_nagy_2006_mammalian_from_code"
        self.curve_names = [
            "CycA",
            "Tri_A",
            "CKI",
            "CycB",
            "pB",
            "BCKI",
            "CycE",
            "Tri_E",
            "mass",
            "Cdc20_A",
            "APCP",
            "Cdc20_i",
            "pBCKI",
            "Cdh1",
        ]
        self.state_names = ['CycA', 'Tri_A', 'CKI', 'CycB', 'pB', 'BCKI', 'CycE', 'Tri_E', 'mass', 'Cdc20_A', 'APCP', 'Cdc20_i', 'pBCKI', 'Cdh1']
        self.algebraic_names = ['APC', 'CycD', 'preMPF', 'CycBT', 'CycAT', 'CycET', 'Tri_B', 'CKIT', 'Cdc20_T', 'Cdh1_i', 'V_atf', 'V_itf', 'TF_E', 'V_de', 'V_da', 'Cdc14', 'TF_I', 'V_ah1', 'V_si', 'V_ih1', 'V_di', 'V_sa', 'TF_B', 'V_se', 'V_sb', 'V_db', 'Wee1', 'V_wee', 'Cdc25', 'V_25']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 93
        p = self.params

        # direct mapping
        c[0] = p.k_assa
        c[1] = p.k_dissa
        c[2] = p.k_assb
        c[3] = p.k_dissb
        c[4] = p.k_disse
        c[5] = p.k_asse
        c[6] = p.CycD_0
        c[7] = p.k_a20
        c[8] = p.k_i20
        c[9] = p.k_d20
        c[10] = p.J_a20
        c[11] = p.J_i20
        c[12] = p.k_s20p
        c[13] = p.k_s20pp
        c[14] = p.n20
        c[15] = p.J_20
        c[16] = p.J_a20_1
        c[17] = p.J_i20_1
        c[18] = p.APC_T
        c[19] = p.k_aie
        c[20] = p.k_iie
        c[21] = p.J_aie
        c[22] = p.J_iie
        c[23] = p.Cdh1_T
        c[24] = p.J_ah1
        c[25] = p.J_ih1
        c[26] = p.mu
        c[27] = p.maxmass
        c[28] = p.k_atfp
        c[29] = p.k_atfapp
        c[30] = p.k_atfepp
        c[31] = p.k_atfdpp
        c[32] = p.k_itfp
        c[33] = p.k_itfapp
        c[34] = p.k_itfbpp
        c[35] = p.J_itf
        c[36] = p.J_atf
        c[37] = p.k_dep
        c[38] = p.k_deepp
        c[39] = p.k_deapp
        c[40] = p.k_debpp
        c[41] = p.k_dap
        c[42] = p.k_dapp
        c[43] = p.k_dappp
        c[44] = p.k_afi
        c[45] = p.k_ifip
        c[46] = p.k_ifibpp
        c[47] = p.J_ifi
        c[48] = p.J_afi
        c[49] = p.k_ah1p
        c[50] = p.k_ah1pp
        c[51] = p.k_ih1p
        c[52] = p.k_ih1app
        c[53] = p.k_ih1bpp
        c[54] = p.k_ih1epp
        c[55] = p.k_ih1dpp
        c[56] = p.k_sip
        c[57] = p.k_sipp
        c[58] = p.k_dip
        c[59] = p.k_diapp
        c[60] = p.k_diepp
        c[61] = p.k_didpp
        c[62] = p.k_dibpp
        c[63] = p.k_14di
        c[64] = p.k_afb
        c[65] = p.k_ifb
        c[66] = p.J_ifb
        c[67] = p.J_afb
        c[68] = p.k_sbp
        c[69] = p.k_sbpp
        c[70] = p.k_sap
        c[71] = p.k_sapp
        c[72] = p.k_sep
        c[73] = p.k_sepp
        c[74] = p.k_dbp
        c[75] = p.k_dbhpp
        c[76] = p.k_dbcpp
        c[77] = p.k_aweep
        c[78] = p.k_aweepp
        c[79] = p.k_iweep
        c[80] = p.k_iweepp
        c[81] = p.J_iwee
        c[82] = p.J_awee
        c[83] = p.k_weep
        c[84] = p.k_weepp
        c[85] = p.k_a25p
        c[86] = p.k_a25pp
        c[87] = p.k_i25p
        c[88] = p.k_i25pp
        c[89] = p.J_i25
        c[90] = p.J_a25
        c[91] = p.k_25p
        c[92] = p.k_25pp

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
