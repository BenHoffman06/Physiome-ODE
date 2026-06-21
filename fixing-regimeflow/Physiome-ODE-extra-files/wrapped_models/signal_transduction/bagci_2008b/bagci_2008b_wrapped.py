# Size of variable arrays:
sizeAlgebraic = 66
sizeStates = 42
sizeConstants = 94
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (second)"
    legend_states[0] = "Casp8 in component Casp8 (micromolar)"
    legend_states[1] = "Casp8Bid in component Casp8 (micromolar)"
    legend_states[2] = "FeLnNO in component FeLn (micromolar)"
    legend_states[3] = "Bid in component Bid (micromolar)"
    legend_algebraic[2] = "J_0 in component Casp8 (flux)"
    legend_algebraic[0] = "J_f0 in component Casp8 (flux)"
    legend_algebraic[1] = "J_Casp8 in component Casp8 (flux)"
    legend_algebraic[3] = "r_20NO in component Casp8 (flux)"
    legend_algebraic[61] = "r_19NO in component PTPC (flux)"
    legend_constants[0] = "k_f0 in component model_constant (first_order_rate_constant)"
    legend_constants[1] = "k_10 in component model_constant (second_order_rate_constant)"
    legend_constants[2] = "k_00 in component model_constant (first_order_rate_constant)"
    legend_constants[3] = "u in component model_constant (first_order_rate_constant)"
    legend_constants[4] = "k_20NO in component model_constant (second_order_rate_constant)"
    legend_states[4] = "Apaf_1 in component Apaf_1 (micromolar)"
    legend_states[5] = "CytcApaf_1 in component CytcApaf_1 (micromolar)"
    legend_states[6] = "Cytc in component Cytc (micromolar)"
    legend_algebraic[4] = "J_Apaf_1 in component Apaf_1 (flux)"
    legend_algebraic[5] = "J_1 in component Apaf_1 (flux)"
    legend_constants[5] = "P_Apaf_1 in component model_constant (flux)"
    legend_constants[6] = "k_11 in component model_constant (second_order_rate_constant)"
    legend_constants[7] = "k_01 in component model_constant (first_order_rate_constant)"
    legend_states[7] = "Apop in component Apop (micromolar)"
    legend_algebraic[7] = "J_1b in component CytcApaf_1 (flux)"
    legend_constants[8] = "k_11b in component model_constant (rate)"
    legend_constants[9] = "k_01b in component model_constant (first_order_rate_constant)"
    legend_constants[10] = "p in component model_constant (dimensionless)"
    legend_states[8] = "Cytc_mito in component Cytc_mito (micromolar)"
    legend_states[9] = "PTPC in component PTPC (micromolar)"
    legend_algebraic[8] = "PTPC_act in component Cytc (micromolar)"
    legend_constants[11] = "PTPC_0 in component model_constant (micromolar)"
    legend_algebraic[12] = "J_14 in component Cytc_mito (flux)"
    legend_algebraic[6] = "J_Cytc in component Cytc (flux)"
    legend_constants[12] = "k_1 in component model_constant (second_order_rate_constant)"
    legend_states[10] = "Bax_2 in component Bax_2 (micromolar)"
    legend_algebraic[10] = "J_Cytc_mito in component Cytc_mito (flux)"
    legend_constants[13] = "P_Cytc_mito in component model_constant (flux)"
    legend_constants[14] = "k14 in component model_constant (second_order_rate_constant)"
    legend_algebraic[17] = "J_12b in component tBidBax (flux)"
    legend_algebraic[9] = "J_Bax_2 in component Bax_2 (flux)"
    legend_states[11] = "tBid_mito in component tBid_mito (micromolar)"
    legend_states[12] = "Bax in component Bax (micromolar)"
    legend_algebraic[14] = "J_11 in component tBid (flux)"
    legend_algebraic[13] = "J_12a in component tBid_mito (flux)"
    legend_algebraic[11] = "J_tBid_mito in component tBid_mito (flux)"
    legend_constants[15] = "k12a in component model_constant (second_order_rate_constant)"
    legend_states[13] = "tBid in component tBid (micromolar)"
    legend_algebraic[25] = "J_f8 in component Casp3Bid (flux)"
    legend_algebraic[15] = "J_tBid in component tBid (flux)"
    legend_constants[16] = "k11 in component model_constant (first_order_rate_constant)"
    legend_states[14] = "tBidBax in component tBidBax (micromolar)"
    legend_algebraic[16] = "J_tBidBax in component tBidBax (flux)"
    legend_constants[17] = "k12b in component model_constant (second_order_rate_constant)"
    legend_states[15] = "Bcl_2 in component Bcl_2 (micromolar)"
    legend_algebraic[19] = "J_13 in component Bax (flux)"
    legend_algebraic[18] = "J_Bax in component Bax (flux)"
    legend_constants[91] = "P_Bax in component Bax (flux)"
    legend_constants[18] = "k13 in component model_constant (second_order_rate_constant)"
    legend_constants[19] = "P_oBax in component model_constant (flux)"
    legend_constants[20] = "p53 in component model_constant (micromolar)"
    legend_constants[21] = "p53_thresh in component model_constant (micromolar)"
    legend_constants[22] = "u_Bax in component model_constant (first_order_rate_constant)"
    legend_states[16] = "Casp3 in component Casp3 (micromolar)"
    legend_states[17] = "Casp3Bcl_2 in component Casp3Bcl_2 (micromolar)"
    legend_algebraic[20] = "J_9 in component Bcl_2 (flux)"
    legend_algebraic[22] = "J_Bcl_2 in component Bcl_2 (flux)"
    legend_constants[23] = "k_19 in component model_constant (second_order_rate_constant)"
    legend_constants[24] = "k_09 in component model_constant (first_order_rate_constant)"
    legend_constants[92] = "P_Bcl_2 in component Bcl_2 (flux)"
    legend_constants[25] = "P_oBcl_2 in component model_constant (flux)"
    legend_constants[26] = "u_Bcl_2 in component model_constant (first_order_rate_constant)"
    legend_algebraic[21] = "J_f9 in component Casp3Bcl_2 (flux)"
    legend_constants[27] = "k_f9 in component model_constant (first_order_rate_constant)"
    legend_states[18] = "Casp3Bid in component Casp3Bid (micromolar)"
    legend_algebraic[23] = "J_8 in component Casp3Bid (flux)"
    legend_constants[28] = "k_18 in component model_constant (second_order_rate_constant)"
    legend_constants[29] = "k_08 in component model_constant (first_order_rate_constant)"
    legend_constants[30] = "k_f8 in component model_constant (first_order_rate_constant)"
    legend_algebraic[24] = "J_Bid in component Bid (flux)"
    legend_constants[31] = "P_Bid in component model_constant (flux)"
    legend_states[19] = "IAP in component IAP (micromolar)"
    legend_states[20] = "Casp3IAP in component Casp3 (micromolar)"
    legend_algebraic[34] = "J_f6 in component Casp9Pro3 (flux)"
    legend_algebraic[33] = "J_f6b in component ApopCasp9_2Pro3 (flux)"
    legend_algebraic[27] = "J_7 in component Casp3 (flux)"
    legend_algebraic[26] = "J_Casp3 in component Casp3 (flux)"
    legend_algebraic[65] = "r_22NO in component FeLn (flux)"
    legend_constants[32] = "k_17 in component model_constant (second_order_rate_constant)"
    legend_constants[33] = "k_07 in component model_constant (first_order_rate_constant)"
    legend_algebraic[29] = "J_2 in component Pro9 (flux)"
    legend_algebraic[42] = "J_4b in component ApopCasp9 (flux)"
    legend_states[21] = "Pro9 in component Pro9 (micromolar)"
    legend_states[22] = "ApopPro9 in component Pro9 (micromolar)"
    legend_states[23] = "ApopPro9_2 in component ApopPro9_2 (micromolar)"
    legend_algebraic[30] = "J_3 in component Pro9 (flux)"
    legend_algebraic[28] = "J_Pro9 in component Pro9 (flux)"
    legend_constants[34] = "k_12 in component model_constant (second_order_rate_constant)"
    legend_constants[35] = "k_02 in component model_constant (first_order_rate_constant)"
    legend_constants[36] = "k_13 in component model_constant (second_order_rate_constant)"
    legend_constants[37] = "k_03 in component model_constant (first_order_rate_constant)"
    legend_constants[38] = "P_Pro9 in component model_constant (flux)"
    legend_algebraic[31] = "J_f3 in component ApopPro9_2 (flux)"
    legend_constants[39] = "k_f3 in component model_constant (first_order_rate_constant)"
    legend_states[24] = "ApopCasp9_2Pro3 in component ApopCasp9_2Pro3 (micromolar)"
    legend_states[25] = "ApopCasp9_2 in component ApopCasp9_2 (micromolar)"
    legend_states[26] = "Pro3 in component Pro3 (micromolar)"
    legend_algebraic[32] = "J_6b in component ApopCasp9_2Pro3 (flux)"
    legend_constants[40] = "k_16b in component model_constant (second_order_rate_constant)"
    legend_constants[41] = "k_06b in component model_constant (first_order_rate_constant)"
    legend_constants[42] = "k_f6b in component model_constant (first_order_rate_constant)"
    legend_states[27] = "Casp9Pro3 in component Casp9Pro3 (micromolar)"
    legend_algebraic[35] = "J_6 in component Pro3 (flux)"
    legend_constants[43] = "k_f6 in component model_constant (first_order_rate_constant)"
    legend_states[28] = "Casp9 in component Casp9 (micromolar)"
    legend_algebraic[36] = "J_Pro3 in component Pro3 (flux)"
    legend_constants[44] = "k_16 in component model_constant (second_order_rate_constant)"
    legend_constants[45] = "k_06 in component model_constant (first_order_rate_constant)"
    legend_constants[46] = "P_Pro3 in component model_constant (flux)"
    legend_states[29] = "Casp9IAP in component IAP (micromolar)"
    legend_states[30] = "ApopCasp9IAP in component IAP (micromolar)"
    legend_states[31] = "ApopCasp9_2IAP in component IAP (micromolar)"
    legend_states[32] = "ApopCasp9 in component ApopCasp9 (micromolar)"
    legend_algebraic[37] = "J_5 in component IAP (flux)"
    legend_algebraic[38] = "J_5b in component IAP (flux)"
    legend_algebraic[39] = "J_5c in component IAP (flux)"
    legend_algebraic[41] = "J_IAP in component IAP (flux)"
    legend_constants[47] = "P_IAP in component model_constant (flux)"
    legend_constants[48] = "k_15 in component model_constant (second_order_rate_constant)"
    legend_constants[49] = "k_05 in component model_constant (first_order_rate_constant)"
    legend_constants[50] = "k_15b in component model_constant (second_order_rate_constant)"
    legend_constants[51] = "k_05b in component model_constant (first_order_rate_constant)"
    legend_constants[52] = "k_15c in component model_constant (second_order_rate_constant)"
    legend_constants[53] = "k_05c in component model_constant (first_order_rate_constant)"
    legend_algebraic[40] = "J_4 in component ApopCasp9 (flux)"
    legend_constants[54] = "k_14 in component model_constant (first_order_rate_constant)"
    legend_constants[55] = "k_04 in component model_constant (second_order_rate_constant)"
    legend_constants[56] = "k_14b in component model_constant (first_order_rate_constant)"
    legend_constants[57] = "k_04b in component model_constant (second_order_rate_constant)"
    legend_algebraic[43] = "J_Casp9 in component Casp9 (flux)"
    legend_algebraic[64] = "r_21NO in component FeLn (flux)"
    legend_states[33] = "NO in component NO (micromolar)"
    legend_states[34] = "O_2m in component O_2m (micromolar)"
    legend_constants[58] = "O_2 in component NO (micromolar)"
    legend_states[35] = "NO_2 in component NO (micromolar)"
    legend_states[36] = "N2O3 in component N2O3 (micromolar)"
    legend_states[37] = "GSNO in component GSNO (micromolar)"
    legend_states[38] = "CcOX in component NO (micromolar)"
    legend_states[39] = "FeLn in component FeLn (micromolar)"
    legend_constants[90] = "r_1NO in component NO (flux)"
    legend_algebraic[44] = "r_4NO in component NO (flux)"
    legend_algebraic[45] = "r_12aNO in component NO (flux)"
    legend_algebraic[46] = "r_12bNOp in component NO (flux)"
    legend_algebraic[47] = "r_12bNOm in component NO (flux)"
    legend_algebraic[48] = "r_14NO in component NO (flux)"
    legend_algebraic[49] = "r_15NO in component NO (flux)"
    legend_algebraic[50] = "r_16NO in component NO (flux)"
    legend_constants[59] = "k_1NO in component model_constant (flux)"
    legend_constants[60] = "k_4NO in component model_constant (second_order_rate_constant)"
    legend_constants[61] = "k_12aNO in component model_constant (rate2)"
    legend_constants[62] = "k_12bNOp in component model_constant (second_order_rate_constant)"
    legend_constants[63] = "k_12bNOm in component model_constant (first_order_rate_constant)"
    legend_constants[64] = "k_14NO in component model_constant (first_order_rate_constant)"
    legend_constants[65] = "k_15NO in component model_constant (second_order_rate_constant)"
    legend_constants[66] = "k_16NO in component model_constant (second_order_rate_constant)"
    legend_constants[67] = "SOD in component O_2m (micromolar)"
    legend_constants[93] = "r_2NO in component O_2m (flux)"
    legend_algebraic[51] = "r_5NO in component O_2m (flux)"
    legend_algebraic[52] = "r_10NO in component O_2m (flux)"
    legend_constants[68] = "k_2NO in component model_constant (flux)"
    legend_constants[69] = "k_5NO in component model_constant (second_order_rate_constant)"
    legend_constants[70] = "k_10NO in component model_constant (rate2)"
    legend_states[40] = "ONOO_m in component ONOO_m (micromolar)"
    legend_states[41] = "GSH in component GSH (micromolar)"
    legend_constants[71] = "GPX in component ONOO_m (micromolar)"
    legend_constants[72] = "CO_2 in component ONOO_m (micromolar)"
    legend_constants[73] = "Cyt_c in component ONOO_m (micromolar)"
    legend_algebraic[53] = "r_6NO in component ONOO_m (flux)"
    legend_algebraic[54] = "r_7NO in component ONOO_m (flux)"
    legend_algebraic[57] = "r_8NO in component ONOO_m (flux)"
    legend_algebraic[60] = "r_9NO in component ONOO_m (flux)"
    legend_algebraic[63] = "r_18NO in component ONOO_m (flux)"
    legend_constants[74] = "k_6NO in component model_constant (second_order_rate_constant)"
    legend_constants[75] = "k_7NO in component model_constant (second_order_rate_constant)"
    legend_constants[76] = "k_8NO in component model_constant (second_order_rate_constant)"
    legend_constants[77] = "k_9NO in component model_constant (second_order_rate_constant)"
    legend_constants[78] = "k_18NO in component model_constant (second_order_rate_constant)"
    legend_algebraic[55] = "GSSG in component GSH (micromolar)"
    legend_constants[79] = "FeLn_0 in component model_constant (micromolar)"
    legend_constants[80] = "GSH_0 in component model_constant (micromolar)"
    legend_algebraic[56] = "r_11NO in component GSH (flux)"
    legend_algebraic[59] = "r_m in component GSH (flux)"
    legend_algebraic[62] = "r_17NO in component GSH (flux)"
    legend_constants[81] = "k_11NO in component model_constant (second_order_rate_constant)"
    legend_constants[82] = "v_m in component model_constant (flux)"
    legend_constants[83] = "k_m in component model_constant (micromolar)"
    legend_constants[84] = "k_17NO in component model_constant (second_order_rate_constant)"
    legend_algebraic[58] = "r_13NO in component N2O3 (flux)"
    legend_constants[85] = "k_13NO in component model_constant (first_order_rate_constant)"
    legend_constants[86] = "k_21NO in component model_constant (second_order_rate_constant)"
    legend_constants[87] = "k_22NO in component model_constant (second_order_rate_constant)"
    legend_constants[88] = "k_19NO in component model_constant (second_order_rate_constant)"
    legend_constants[89] = "k_17bNO in component model_constant (second_order_rate_constant)"
    legend_rates[0] = "d/dt Casp8 in component Casp8 (micromolar)"
    legend_rates[1] = "d/dt Casp8Bid in component Casp8 (micromolar)"
    legend_rates[4] = "d/dt Apaf_1 in component Apaf_1 (micromolar)"
    legend_rates[5] = "d/dt CytcApaf_1 in component CytcApaf_1 (micromolar)"
    legend_rates[6] = "d/dt Cytc in component Cytc (micromolar)"
    legend_rates[8] = "d/dt Cytc_mito in component Cytc_mito (micromolar)"
    legend_rates[10] = "d/dt Bax_2 in component Bax_2 (micromolar)"
    legend_rates[11] = "d/dt tBid_mito in component tBid_mito (micromolar)"
    legend_rates[13] = "d/dt tBid in component tBid (micromolar)"
    legend_rates[14] = "d/dt tBidBax in component tBidBax (micromolar)"
    legend_rates[12] = "d/dt Bax in component Bax (micromolar)"
    legend_rates[15] = "d/dt Bcl_2 in component Bcl_2 (micromolar)"
    legend_rates[17] = "d/dt Casp3Bcl_2 in component Casp3Bcl_2 (micromolar)"
    legend_rates[18] = "d/dt Casp3Bid in component Casp3Bid (micromolar)"
    legend_rates[3] = "d/dt Bid in component Bid (micromolar)"
    legend_rates[20] = "d/dt Casp3IAP in component Casp3 (micromolar)"
    legend_rates[16] = "d/dt Casp3 in component Casp3 (micromolar)"
    legend_rates[7] = "d/dt Apop in component Apop (micromolar)"
    legend_rates[21] = "d/dt Pro9 in component Pro9 (micromolar)"
    legend_rates[22] = "d/dt ApopPro9 in component Pro9 (micromolar)"
    legend_rates[23] = "d/dt ApopPro9_2 in component ApopPro9_2 (micromolar)"
    legend_rates[24] = "d/dt ApopCasp9_2Pro3 in component ApopCasp9_2Pro3 (micromolar)"
    legend_rates[27] = "d/dt Casp9Pro3 in component Casp9Pro3 (micromolar)"
    legend_rates[26] = "d/dt Pro3 in component Pro3 (micromolar)"
    legend_rates[29] = "d/dt Casp9IAP in component IAP (micromolar)"
    legend_rates[30] = "d/dt ApopCasp9IAP in component IAP (micromolar)"
    legend_rates[31] = "d/dt ApopCasp9_2IAP in component IAP (micromolar)"
    legend_rates[19] = "d/dt IAP in component IAP (micromolar)"
    legend_rates[32] = "d/dt ApopCasp9 in component ApopCasp9 (micromolar)"
    legend_rates[28] = "d/dt Casp9 in component Casp9 (micromolar)"
    legend_rates[25] = "d/dt ApopCasp9_2 in component ApopCasp9_2 (micromolar)"
    legend_rates[33] = "d/dt NO in component NO (micromolar)"
    legend_rates[38] = "d/dt CcOX in component NO (micromolar)"
    legend_rates[35] = "d/dt NO_2 in component NO (micromolar)"
    legend_rates[34] = "d/dt O_2m in component O_2m (micromolar)"
    legend_rates[40] = "d/dt ONOO_m in component ONOO_m (micromolar)"
    legend_rates[41] = "d/dt GSH in component GSH (micromolar)"
    legend_rates[37] = "d/dt GSNO in component GSNO (micromolar)"
    legend_rates[36] = "d/dt N2O3 in component N2O3 (micromolar)"
    legend_rates[39] = "d/dt FeLn in component FeLn (micromolar)"
    legend_rates[2] = "d/dt FeLnNO in component FeLn (micromolar)"
    legend_rates[9] = "d/dt PTPC in component PTPC (micromolar)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 0
    states[1] = 0
    states[2] = 0
    states[3] = 0.004
    constants[0] = 0.1
    constants[1] = 10
    constants[2] = 0.5
    constants[3] = 0.006
    constants[4] = 66
    states[4] = 0.004
    states[5] = 0
    states[6] = 0
    constants[5] = 0.0003
    constants[6] = 5
    constants[7] = 0.5
    states[7] = 0
    constants[8] = 50000
    constants[9] = 0.5
    constants[10] = 4
    states[8] = 0.004
    states[9] = 0
    constants[11] = 0
    constants[12] = 1
    states[10] = 0
    constants[13] = 0.0003
    constants[14] = 10
    states[11] = 0
    states[12] = 0.004
    constants[15] = 10
    states[13] = 0
    constants[16] = 10
    states[14] = 0
    constants[17] = 10
    states[15] = 0.004
    constants[18] = 10
    constants[19] = 0.00003
    constants[20] = 0.0066
    constants[21] = 0.004
    constants[22] = 0.006
    states[16] = 0
    states[17] = 0
    constants[23] = 10
    constants[24] = 0.5
    constants[25] = 0.00008
    constants[26] = 0.006
    constants[27] = 0.1
    states[18] = 0
    constants[28] = 10
    constants[29] = 0.5
    constants[30] = 0.1
    constants[31] = 0.00003
    states[19] = 0.004
    states[20] = 0
    constants[32] = 5
    constants[33] = 0.0035
    states[21] = 0.004
    states[22] = 0
    states[23] = 0
    constants[34] = 10
    constants[35] = 0.5
    constants[36] = 10
    constants[37] = 0.5
    constants[38] = 0.0003
    constants[39] = 0.1
    states[24] = 0
    states[25] = 0
    states[26] = 0.004
    constants[40] = 10
    constants[41] = 0.5
    constants[42] = 0.1
    states[27] = 0
    constants[43] = 0.001
    states[28] = 0
    constants[44] = 10
    constants[45] = 0.5
    constants[46] = 0.0003
    states[29] = 0
    states[30] = 0
    states[31] = 0
    states[32] = 0
    constants[47] = 0.00003
    constants[48] = 5
    constants[49] = 0.0035
    constants[50] = 5
    constants[51] = 0.0035
    constants[52] = 5
    constants[53] = 0.0035
    constants[54] = 5
    constants[55] = 0.5
    constants[56] = 5
    constants[57] = 0.5
    states[33] = 0
    states[34] = 35
    constants[58] = 35
    states[35] = 0
    states[36] = 0
    states[37] = 0
    states[38] = 0.1
    states[39] = 0.05
    constants[59] = 1
    constants[60] = 6700
    constants[61] = 0.000006
    constants[62] = 1100
    constants[63] = 81000
    constants[64] = 0.0002
    constants[65] = 100
    constants[66] = 1.21
    constants[67] = 10
    constants[68] = 0.1
    constants[69] = 2400
    constants[70] = 0.0006
    states[40] = 0
    states[41] = 10000
    constants[71] = 5.8
    constants[72] = 1000
    constants[73] = 400
    constants[74] = 0.00135
    constants[75] = 2
    constants[76] = 0.058
    constants[77] = 0.025
    constants[78] = 1
    constants[79] = 0.05
    constants[80] = 10000
    constants[81] = 66
    constants[82] = 320
    constants[83] = 50
    constants[84] = 66
    constants[85] = 1600
    constants[86] = 66
    constants[87] = 66
    constants[88] = 10
    constants[89] = 0.0002
    constants[90] = constants[59]
    constants[91] = constants[19]*(1.00000+(power(constants[20], 4.00000))/(power(constants[20], 4.00000)+power(constants[21], 4.00000)))
    constants[92] = (constants[25]*(power(constants[21], 4.00000)))/(power(constants[20], 4.00000)+power(constants[21], 4.00000))
    constants[93] = constants[68]
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[2] = constants[1]*states[0]*states[3]-constants[2]*states[1]
    algebraic[0] = constants[0]*states[1]
    rates[1] = algebraic[2]-algebraic[0]
    algebraic[4] = constants[5]-constants[3]*states[4]
    algebraic[5] = constants[6]*states[6]*states[4]-constants[7]*states[5]
    rates[4] = -algebraic[5]+algebraic[4]
    algebraic[7] = constants[8]*(power(states[5], constants[10]))-constants[9]*states[7]
    rates[5] = algebraic[5]-7.00000*algebraic[7]
    algebraic[8] = constants[11]-states[9]
    algebraic[12] = constants[14]*states[10]*states[8]
    algebraic[6] = -constants[3]*states[6]
    rates[6] = (algebraic[12]-algebraic[5])+algebraic[6]+constants[12]*algebraic[8]*states[8]
    algebraic[10] = constants[13]-constants[3]*states[8]
    rates[8] = -algebraic[12]+algebraic[10]
    algebraic[14] = constants[16]*states[13]
    algebraic[13] = constants[15]*states[11]*states[12]
    algebraic[11] = -constants[3]*states[11]
    rates[11] = (algebraic[14]-algebraic[13])+algebraic[11]
    algebraic[17] = constants[17]*states[14]*states[12]
    algebraic[9] = -constants[3]*states[10]
    rates[10] = algebraic[17]+algebraic[9]
    algebraic[16] = -constants[3]*states[14]
    rates[14] = (algebraic[13]-algebraic[17])+algebraic[16]
    algebraic[19] = constants[18]*states[15]*states[12]
    algebraic[18] = constants[91]-constants[22]*states[12]
    rates[12] = ((-algebraic[13]-algebraic[17])-algebraic[19])+algebraic[18]
    algebraic[20] = constants[23]*states[16]*states[15]-constants[24]*states[17]
    algebraic[22] = constants[92]-constants[26]*states[15]
    rates[15] = (-algebraic[20]-algebraic[19])+algebraic[22]
    algebraic[21] = constants[27]*states[17]
    rates[17] = algebraic[20]-algebraic[21]
    algebraic[25] = constants[30]*states[18]
    algebraic[15] = -constants[3]*states[13]
    rates[13] = ((algebraic[0]+algebraic[25])-algebraic[14])+algebraic[17]+algebraic[15]
    algebraic[23] = constants[28]*states[16]*states[3]-constants[29]*states[18]
    rates[18] = algebraic[23]-algebraic[25]
    algebraic[24] = constants[31]-constants[3]*states[3]
    rates[3] = (-algebraic[2]-algebraic[23])+algebraic[24]
    algebraic[27] = constants[32]*states[16]*states[19]-constants[33]*states[20]
    rates[20] = algebraic[27]
    algebraic[29] = constants[34]*states[7]*states[21]-constants[35]*states[22]
    algebraic[30] = constants[36]*states[22]*states[21]-constants[37]*states[23]
    algebraic[28] = constants[38]-constants[3]*states[21]
    rates[21] = (-algebraic[29]-algebraic[30])+algebraic[28]
    rates[22] = algebraic[29]-algebraic[30]
    algebraic[31] = constants[39]*states[23]
    rates[23] = algebraic[30]-algebraic[31]
    algebraic[33] = constants[42]*states[24]
    algebraic[32] = constants[40]*states[25]*states[26]-constants[41]*states[24]
    rates[24] = algebraic[32]-algebraic[33]
    algebraic[34] = constants[43]*states[27]
    algebraic[35] = constants[44]*states[28]*states[26]-constants[45]*states[27]
    rates[27] = algebraic[35]-algebraic[34]
    algebraic[36] = constants[46]-constants[3]*states[26]
    rates[26] = (-algebraic[35]-algebraic[32])+algebraic[36]
    algebraic[37] = constants[48]*states[28]*states[19]-constants[49]*states[29]
    rates[29] = algebraic[37]
    algebraic[38] = constants[50]*states[32]*states[19]-constants[51]*states[30]
    rates[30] = algebraic[38]
    algebraic[39] = constants[52]*states[25]*states[19]-constants[53]*states[31]
    rates[31] = algebraic[39]
    algebraic[41] = constants[47]-constants[3]*states[19]
    rates[19] = (((-algebraic[37]-algebraic[38])-algebraic[39])-algebraic[27])+algebraic[41]
    algebraic[40] = constants[54]*states[25]-constants[55]*states[32]*states[28]
    rates[25] = (((algebraic[31]-algebraic[40])-algebraic[39])-algebraic[32])+algebraic[33]
    algebraic[42] = constants[56]*states[32]-constants[57]*states[7]*states[28]
    rates[7] = (algebraic[7]-algebraic[29])+algebraic[42]
    rates[32] = (algebraic[40]-algebraic[42])-algebraic[38]
    algebraic[45] = constants[61]*(power(states[33], 2.00000))*constants[58]
    algebraic[46] = constants[62]*states[35]*states[33]
    algebraic[47] = constants[63]*states[36]
    rates[35] = (2.00000*algebraic[45]-algebraic[46])+algebraic[47]
    algebraic[49] = constants[65]*states[38]*states[33]
    rates[38] = -algebraic[49]
    algebraic[44] = constants[60]*states[33]*states[34]
    algebraic[48] = constants[64]*states[37]
    algebraic[50] = constants[66]*states[39]*states[33]
    rates[33] = (((((constants[90]-algebraic[44])-2.00000*algebraic[45])-algebraic[46])+algebraic[47]+algebraic[48])-algebraic[49])-algebraic[50]
    algebraic[51] = constants[69]*constants[67]*states[34]
    algebraic[52] = constants[70]*(power(states[37], 2.00000))*states[34]
    rates[34] = ((constants[93]-algebraic[44])-algebraic[51])-algebraic[52]
    algebraic[1] = -constants[3]*states[0]
    algebraic[3] = constants[4]*states[2]*states[0]
    algebraic[61] = constants[88]*states[36]*states[0]
    rates[0] = ((-algebraic[2]+algebraic[0]+algebraic[1])-algebraic[61])-algebraic[3]
    algebraic[53] = constants[74]*states[40]*states[41]
    algebraic[54] = constants[75]*states[40]*constants[71]
    algebraic[57] = constants[76]*states[40]*constants[72]
    algebraic[60] = constants[77]*states[40]*constants[73]
    algebraic[63] = constants[78]*states[40]*states[9]
    rates[40] = ((((algebraic[44]-algebraic[53])-algebraic[54])-algebraic[57])-algebraic[60])-algebraic[63]
    algebraic[56] = constants[81]*states[36]*states[41]
    algebraic[55] = ((constants[80]-states[41])-states[37])/2.00000
    algebraic[59] = (constants[82]*algebraic[55])/(constants[83]+algebraic[55])
    algebraic[62] = constants[84]*states[2]*states[41]
    rates[41] = ((-algebraic[53]-algebraic[56])+2.00000*algebraic[59])-algebraic[62]
    rates[37] = (((algebraic[53]-2.00000*algebraic[52])+algebraic[56])-algebraic[48])+algebraic[62]
    algebraic[58] = constants[85]*states[36]
    rates[36] = (((-algebraic[56]+algebraic[46])-algebraic[47])-algebraic[58])-algebraic[61]
    rates[9] = -algebraic[61]
    algebraic[43] = -constants[3]*states[28]
    algebraic[64] = constants[86]*states[2]*states[28]
    rates[28] = ((((algebraic[40]+algebraic[42])-algebraic[37])-algebraic[35])+algebraic[34]+algebraic[43])-algebraic[64]
    algebraic[26] = -constants[3]*states[16]
    algebraic[65] = constants[87]*states[2]*states[16]
    rates[16] = ((((((algebraic[34]+algebraic[33])-algebraic[27])-algebraic[23])+algebraic[25])-algebraic[20])+algebraic[21]+algebraic[26])-algebraic[65]
    rates[39] = -algebraic[50]+algebraic[62]+algebraic[3]+algebraic[64]+algebraic[65]
    rates[2] = (((algebraic[50]-algebraic[62])-algebraic[3])-algebraic[64])-algebraic[65]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[2] = constants[1]*states[0]*states[3]-constants[2]*states[1]
    algebraic[0] = constants[0]*states[1]
    algebraic[4] = constants[5]-constants[3]*states[4]
    algebraic[5] = constants[6]*states[6]*states[4]-constants[7]*states[5]
    algebraic[7] = constants[8]*(power(states[5], constants[10]))-constants[9]*states[7]
    algebraic[8] = constants[11]-states[9]
    algebraic[12] = constants[14]*states[10]*states[8]
    algebraic[6] = -constants[3]*states[6]
    algebraic[10] = constants[13]-constants[3]*states[8]
    algebraic[14] = constants[16]*states[13]
    algebraic[13] = constants[15]*states[11]*states[12]
    algebraic[11] = -constants[3]*states[11]
    algebraic[17] = constants[17]*states[14]*states[12]
    algebraic[9] = -constants[3]*states[10]
    algebraic[16] = -constants[3]*states[14]
    algebraic[19] = constants[18]*states[15]*states[12]
    algebraic[18] = constants[91]-constants[22]*states[12]
    algebraic[20] = constants[23]*states[16]*states[15]-constants[24]*states[17]
    algebraic[22] = constants[92]-constants[26]*states[15]
    algebraic[21] = constants[27]*states[17]
    algebraic[25] = constants[30]*states[18]
    algebraic[15] = -constants[3]*states[13]
    algebraic[23] = constants[28]*states[16]*states[3]-constants[29]*states[18]
    algebraic[24] = constants[31]-constants[3]*states[3]
    algebraic[27] = constants[32]*states[16]*states[19]-constants[33]*states[20]
    algebraic[29] = constants[34]*states[7]*states[21]-constants[35]*states[22]
    algebraic[30] = constants[36]*states[22]*states[21]-constants[37]*states[23]
    algebraic[28] = constants[38]-constants[3]*states[21]
    algebraic[31] = constants[39]*states[23]
    algebraic[33] = constants[42]*states[24]
    algebraic[32] = constants[40]*states[25]*states[26]-constants[41]*states[24]
    algebraic[34] = constants[43]*states[27]
    algebraic[35] = constants[44]*states[28]*states[26]-constants[45]*states[27]
    algebraic[36] = constants[46]-constants[3]*states[26]
    algebraic[37] = constants[48]*states[28]*states[19]-constants[49]*states[29]
    algebraic[38] = constants[50]*states[32]*states[19]-constants[51]*states[30]
    algebraic[39] = constants[52]*states[25]*states[19]-constants[53]*states[31]
    algebraic[41] = constants[47]-constants[3]*states[19]
    algebraic[40] = constants[54]*states[25]-constants[55]*states[32]*states[28]
    algebraic[42] = constants[56]*states[32]-constants[57]*states[7]*states[28]
    algebraic[45] = constants[61]*(power(states[33], 2.00000))*constants[58]
    algebraic[46] = constants[62]*states[35]*states[33]
    algebraic[47] = constants[63]*states[36]
    algebraic[49] = constants[65]*states[38]*states[33]
    algebraic[44] = constants[60]*states[33]*states[34]
    algebraic[48] = constants[64]*states[37]
    algebraic[50] = constants[66]*states[39]*states[33]
    algebraic[51] = constants[69]*constants[67]*states[34]
    algebraic[52] = constants[70]*(power(states[37], 2.00000))*states[34]
    algebraic[1] = -constants[3]*states[0]
    algebraic[3] = constants[4]*states[2]*states[0]
    algebraic[61] = constants[88]*states[36]*states[0]
    algebraic[53] = constants[74]*states[40]*states[41]
    algebraic[54] = constants[75]*states[40]*constants[71]
    algebraic[57] = constants[76]*states[40]*constants[72]
    algebraic[60] = constants[77]*states[40]*constants[73]
    algebraic[63] = constants[78]*states[40]*states[9]
    algebraic[56] = constants[81]*states[36]*states[41]
    algebraic[55] = ((constants[80]-states[41])-states[37])/2.00000
    algebraic[59] = (constants[82]*algebraic[55])/(constants[83]+algebraic[55])
    algebraic[62] = constants[84]*states[2]*states[41]
    algebraic[58] = constants[85]*states[36]
    algebraic[43] = -constants[3]*states[28]
    algebraic[64] = constants[86]*states[2]*states[28]
    algebraic[26] = -constants[3]*states[16]
    algebraic[65] = constants[87]*states[2]*states[16]
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
        self.k_f0 = 0.1
        self.k_10 = 10
        self.k_00 = 0.5
        self.u = 0.006
        self.k_20NO = 66
        self.P_Apaf_1 = 0.0003
        self.k_11 = 5
        self.k_01 = 0.5
        self.k_11b = 50000
        self.k_01b = 0.5
        self.p = 4
        self.PTPC_0 = 0
        self.k_1 = 1
        self.P_Cytc_mito = 0.0003
        self.k14 = 10
        self.k12a = 10
        self.k11 = 10
        self.k12b = 10
        self.k13 = 10
        self.P_oBax = 0.00003
        self.p53 = 0.0066
        self.p53_thresh = 0.004
        self.u_Bax = 0.006
        self.k_19 = 10
        self.k_09 = 0.5
        self.P_oBcl_2 = 0.00008
        self.u_Bcl_2 = 0.006
        self.k_f9 = 0.1
        self.k_18 = 10
        self.k_08 = 0.5
        self.k_f8 = 0.1
        self.P_Bid = 0.00003
        self.k_17 = 5
        self.k_07 = 0.0035
        self.k_12 = 10
        self.k_02 = 0.5
        self.k_13 = 10
        self.k_03 = 0.5
        self.P_Pro9 = 0.0003
        self.k_f3 = 0.1
        self.k_16b = 10
        self.k_06b = 0.5
        self.k_f6b = 0.1
        self.k_f6 = 0.001
        self.k_16 = 10
        self.k_06 = 0.5
        self.P_Pro3 = 0.0003
        self.P_IAP = 0.00003
        self.k_15 = 5
        self.k_05 = 0.0035
        self.k_15b = 5
        self.k_05b = 0.0035
        self.k_15c = 5
        self.k_05c = 0.0035
        self.k_14 = 5
        self.k_04 = 0.5
        self.k_14b = 5
        self.k_04b = 0.5
        self.O_2 = 35
        self.k_1NO = 1
        self.k_4NO = 6700
        self.k_12aNO = 0.000006
        self.k_12bNOp = 1100
        self.k_12bNOm = 81000
        self.k_14NO = 0.0002
        self.k_15NO = 100
        self.k_16NO = 1.21
        self.SOD = 10
        self.k_2NO = 0.1
        self.k_5NO = 2400
        self.k_10NO = 0.0006
        self.GPX = 5.8
        self.CO_2 = 1000
        self.Cyt_c = 400
        self.k_6NO = 0.00135
        self.k_7NO = 2
        self.k_8NO = 0.058
        self.k_9NO = 0.025
        self.k_18NO = 1
        self.FeLn_0 = 0.05
        self.GSH_0 = 10000
        self.k_11NO = 66
        self.v_m = 320
        self.k_m = 50
        self.k_17NO = 66
        self.k_13NO = 1600
        self.k_21NO = 66
        self.k_22NO = 66
        self.k_19NO = 10
        self.k_17bNO = 0.0002

    def to_dict(self):
        return {
            "k_f0": self.k_f0,
            "k_10": self.k_10,
            "k_00": self.k_00,
            "u": self.u,
            "k_20NO": self.k_20NO,
            "P_Apaf_1": self.P_Apaf_1,
            "k_11": self.k_11,
            "k_01": self.k_01,
            "k_11b": self.k_11b,
            "k_01b": self.k_01b,
            "p": self.p,
            "PTPC_0": self.PTPC_0,
            "k_1": self.k_1,
            "P_Cytc_mito": self.P_Cytc_mito,
            "k14": self.k14,
            "k12a": self.k12a,
            "k11": self.k11,
            "k12b": self.k12b,
            "k13": self.k13,
            "P_oBax": self.P_oBax,
            "p53": self.p53,
            "p53_thresh": self.p53_thresh,
            "u_Bax": self.u_Bax,
            "k_19": self.k_19,
            "k_09": self.k_09,
            "P_oBcl_2": self.P_oBcl_2,
            "u_Bcl_2": self.u_Bcl_2,
            "k_f9": self.k_f9,
            "k_18": self.k_18,
            "k_08": self.k_08,
            "k_f8": self.k_f8,
            "P_Bid": self.P_Bid,
            "k_17": self.k_17,
            "k_07": self.k_07,
            "k_12": self.k_12,
            "k_02": self.k_02,
            "k_13": self.k_13,
            "k_03": self.k_03,
            "P_Pro9": self.P_Pro9,
            "k_f3": self.k_f3,
            "k_16b": self.k_16b,
            "k_06b": self.k_06b,
            "k_f6b": self.k_f6b,
            "k_f6": self.k_f6,
            "k_16": self.k_16,
            "k_06": self.k_06,
            "P_Pro3": self.P_Pro3,
            "P_IAP": self.P_IAP,
            "k_15": self.k_15,
            "k_05": self.k_05,
            "k_15b": self.k_15b,
            "k_05b": self.k_05b,
            "k_15c": self.k_15c,
            "k_05c": self.k_05c,
            "k_14": self.k_14,
            "k_04": self.k_04,
            "k_14b": self.k_14b,
            "k_04b": self.k_04b,
            "O_2": self.O_2,
            "k_1NO": self.k_1NO,
            "k_4NO": self.k_4NO,
            "k_12aNO": self.k_12aNO,
            "k_12bNOp": self.k_12bNOp,
            "k_12bNOm": self.k_12bNOm,
            "k_14NO": self.k_14NO,
            "k_15NO": self.k_15NO,
            "k_16NO": self.k_16NO,
            "SOD": self.SOD,
            "k_2NO": self.k_2NO,
            "k_5NO": self.k_5NO,
            "k_10NO": self.k_10NO,
            "GPX": self.GPX,
            "CO_2": self.CO_2,
            "Cyt_c": self.Cyt_c,
            "k_6NO": self.k_6NO,
            "k_7NO": self.k_7NO,
            "k_8NO": self.k_8NO,
            "k_9NO": self.k_9NO,
            "k_18NO": self.k_18NO,
            "FeLn_0": self.FeLn_0,
            "GSH_0": self.GSH_0,
            "k_11NO": self.k_11NO,
            "v_m": self.v_m,
            "k_m": self.k_m,
            "k_17NO": self.k_17NO,
            "k_13NO": self.k_13NO,
            "k_21NO": self.k_21NO,
            "k_22NO": self.k_22NO,
            "k_19NO": self.k_19NO,
            "k_17bNO": self.k_17bNO,
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
        y0=[0, 0, 0, 0.004, 0.004, 0, 0, 0, 0.004, 0, 0, 0, 0.004, 0, 0, 0.004, 0, 0, 0, 0.004, 0, 0.004, 0, 0, 0, 0, 0.004, 0, 0, 0, 0, 0, 0, 0, 35, 0, 0, 0, 0.1, 0.05, 0, 10000],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "bagci_2008b"
        self.curve_names = [
            "Casp8",
            "Casp8Bid",
            "FeLnNO",
            "Bid",
            "Apaf_1",
            "CytcApaf_1",
            "Cytc",
            "Apop",
            "Cytc_mito",
            "PTPC",
            "Bax_2",
            "tBid_mito",
            "Bax",
            "tBid",
            "tBidBax",
            "Bcl_2",
            "Casp3",
            "Casp3Bcl_2",
            "Casp3Bid",
            "IAP",
            "Casp3IAP",
            "Pro9",
            "ApopPro9",
            "ApopPro9_2",
            "ApopCasp9_2Pro3",
            "ApopCasp9_2",
            "Pro3",
            "Casp9Pro3",
            "Casp9",
            "Casp9IAP",
            "ApopCasp9IAP",
            "ApopCasp9_2IAP",
            "ApopCasp9",
            "NO",
            "O_2m",
            "NO_2",
            "N2O3",
            "GSNO",
            "CcOX",
            "FeLn",
            "ONOO_m",
            "GSH",
        ]
        self.state_names = ['Casp8', 'Casp8Bid', 'FeLnNO', 'Bid', 'Apaf_1', 'CytcApaf_1', 'Cytc', 'Apop', 'Cytc_mito', 'PTPC', 'Bax_2', 'tBid_mito', 'Bax', 'tBid', 'tBidBax', 'Bcl_2', 'Casp3', 'Casp3Bcl_2', 'Casp3Bid', 'IAP', 'Casp3IAP', 'Pro9', 'ApopPro9', 'ApopPro9_2', 'ApopCasp9_2Pro3', 'ApopCasp9_2', 'Pro3', 'Casp9Pro3', 'Casp9', 'Casp9IAP', 'ApopCasp9IAP', 'ApopCasp9_2IAP', 'ApopCasp9', 'NO', 'O_2m', 'NO_2', 'N2O3', 'GSNO', 'CcOX', 'FeLn', 'ONOO_m', 'GSH']
        self.algebraic_names = ['J_f0', 'J_Casp8', 'J_0', 'r_20NO', 'J_Apaf_1', 'J_1', 'J_Cytc', 'J_1b', 'PTPC_act', 'J_Bax_2', 'J_Cytc_mito', 'J_tBid_mito', 'J_14', 'J_12a', 'J_11', 'J_tBid', 'J_tBidBax', 'J_12b', 'J_Bax', 'J_13', 'J_9', 'J_f9', 'J_Bcl_2', 'J_8', 'J_Bid', 'J_f8', 'J_Casp3', 'J_7', 'J_Pro9', 'J_2', 'J_3', 'J_f3', 'J_6b', 'J_f6b', 'J_f6', 'J_6', 'J_Pro3', 'J_5', 'J_5b', 'J_5c', 'J_4', 'J_IAP', 'J_4b', 'J_Casp9', 'r_4NO', 'r_12aNO', 'r_12bNOp', 'r_12bNOm', 'r_14NO', 'r_15NO', 'r_16NO', 'r_5NO', 'r_10NO', 'r_6NO', 'r_7NO', 'GSSG', 'r_11NO', 'r_8NO', 'r_13NO', 'r_m', 'r_9NO', 'r_19NO', 'r_17NO', 'r_18NO', 'r_21NO', 'r_22NO']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 94
        p = self.params

        # direct mapping
        c[0] = p.k_f0
        c[1] = p.k_10
        c[2] = p.k_00
        c[3] = p.u
        c[4] = p.k_20NO
        c[5] = p.P_Apaf_1
        c[6] = p.k_11
        c[7] = p.k_01
        c[8] = p.k_11b
        c[9] = p.k_01b
        c[10] = p.p
        c[11] = p.PTPC_0
        c[12] = p.k_1
        c[13] = p.P_Cytc_mito
        c[14] = p.k14
        c[15] = p.k12a
        c[16] = p.k11
        c[17] = p.k12b
        c[18] = p.k13
        c[19] = p.P_oBax
        c[20] = p.p53
        c[21] = p.p53_thresh
        c[22] = p.u_Bax
        c[23] = p.k_19
        c[24] = p.k_09
        c[25] = p.P_oBcl_2
        c[26] = p.u_Bcl_2
        c[27] = p.k_f9
        c[28] = p.k_18
        c[29] = p.k_08
        c[30] = p.k_f8
        c[31] = p.P_Bid
        c[32] = p.k_17
        c[33] = p.k_07
        c[34] = p.k_12
        c[35] = p.k_02
        c[36] = p.k_13
        c[37] = p.k_03
        c[38] = p.P_Pro9
        c[39] = p.k_f3
        c[40] = p.k_16b
        c[41] = p.k_06b
        c[42] = p.k_f6b
        c[43] = p.k_f6
        c[44] = p.k_16
        c[45] = p.k_06
        c[46] = p.P_Pro3
        c[47] = p.P_IAP
        c[48] = p.k_15
        c[49] = p.k_05
        c[50] = p.k_15b
        c[51] = p.k_05b
        c[52] = p.k_15c
        c[53] = p.k_05c
        c[54] = p.k_14
        c[55] = p.k_04
        c[56] = p.k_14b
        c[57] = p.k_04b
        c[58] = p.O_2
        c[59] = p.k_1NO
        c[60] = p.k_4NO
        c[61] = p.k_12aNO
        c[62] = p.k_12bNOp
        c[63] = p.k_12bNOm
        c[64] = p.k_14NO
        c[65] = p.k_15NO
        c[66] = p.k_16NO
        c[67] = p.SOD
        c[68] = p.k_2NO
        c[69] = p.k_5NO
        c[70] = p.k_10NO
        c[71] = p.GPX
        c[72] = p.CO_2
        c[73] = p.Cyt_c
        c[74] = p.k_6NO
        c[75] = p.k_7NO
        c[76] = p.k_8NO
        c[77] = p.k_9NO
        c[78] = p.k_18NO
        c[79] = p.FeLn_0
        c[80] = p.GSH_0
        c[81] = p.k_11NO
        c[82] = p.v_m
        c[83] = p.k_m
        c[84] = p.k_17NO
        c[85] = p.k_13NO
        c[86] = p.k_21NO
        c[87] = p.k_22NO
        c[88] = p.k_19NO
        c[89] = p.k_17bNO

        # derived constants
        c[90] = c[59]
        c[91] = c[19]*(1.00000+(power(c[20], 4.00000))/(power(c[20], 4.00000)+power(c[21], 4.00000)))
        c[92] = (c[25]*(power(c[21], 4.00000)))/(power(c[20], 4.00000)+power(c[21], 4.00000))
        c[93] = c[68]

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
