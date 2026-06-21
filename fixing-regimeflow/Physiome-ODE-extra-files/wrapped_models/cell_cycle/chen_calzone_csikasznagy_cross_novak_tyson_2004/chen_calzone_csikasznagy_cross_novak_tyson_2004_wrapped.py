# Size of variable arrays:
sizeAlgebraic = 30
sizeStates = 36
sizeConstants = 136
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (minute)"
    legend_states[0] = "mass in component mass (dimensionless)"
    legend_constants[0] = "kg in component model_parameters (first_order_rate_constant)"
    legend_states[1] = "Cln2 in component Cln2 (dimensionless)"
    legend_constants[1] = "ks_n2_ in component model_parameters (first_order_rate_constant)"
    legend_constants[2] = "ks_n2__ in component model_parameters (first_order_rate_constant)"
    legend_constants[3] = "kd_n2 in component model_parameters (first_order_rate_constant)"
    legend_algebraic[27] = "SBF in component SBF_MBF (dimensionless)"
    legend_states[2] = "Clb5 in component Clb5 (dimensionless)"
    legend_constants[4] = "ks_b5_ in component model_parameters (first_order_rate_constant)"
    legend_constants[5] = "ks_b5__ in component model_parameters (first_order_rate_constant)"
    legend_constants[6] = "kdi_f5 in component model_parameters (first_order_rate_constant)"
    legend_constants[7] = "kdi_b5 in component model_parameters (first_order_rate_constant)"
    legend_constants[8] = "kas_b5 in component model_parameters (first_order_rate_constant)"
    legend_constants[9] = "kas_f5 in component model_parameters (first_order_rate_constant)"
    legend_constants[10] = "kd3_f6 in component model_parameters (first_order_rate_constant)"
    legend_constants[11] = "kd3_c1 in component model_parameters (first_order_rate_constant)"
    legend_algebraic[20] = "Vd_b5 in component Vd_b5 (first_order_rate_constant)"
    legend_algebraic[26] = "MBF in component SBF_MBF (dimensionless)"
    legend_states[3] = "C5P in component C5P (dimensionless)"
    legend_states[4] = "C5 in component C5 (dimensionless)"
    legend_states[5] = "F5P in component F5P (dimensionless)"
    legend_states[6] = "F5 in component F5 (dimensionless)"
    legend_states[7] = "Sic1 in component Sic1 (dimensionless)"
    legend_states[8] = "Cdc6 in component Cdc6 (dimensionless)"
    legend_states[9] = "Clb2 in component Clb2 (dimensionless)"
    legend_constants[12] = "ks_b2_ in component model_parameters (first_order_rate_constant)"
    legend_constants[13] = "ks_b2__ in component model_parameters (first_order_rate_constant)"
    legend_constants[14] = "kdi_b2 in component model_parameters (first_order_rate_constant)"
    legend_constants[15] = "kdi_f2 in component model_parameters (first_order_rate_constant)"
    legend_constants[16] = "kas_b2 in component model_parameters (first_order_rate_constant)"
    legend_constants[17] = "kas_f2 in component model_parameters (first_order_rate_constant)"
    legend_algebraic[21] = "Vd_b2 in component Vd_b2 (first_order_rate_constant)"
    legend_algebraic[7] = "Mcm1 in component Mcm1 (dimensionless)"
    legend_states[10] = "C2P in component C2P (dimensionless)"
    legend_states[11] = "C2 in component C2 (dimensionless)"
    legend_states[12] = "F2P in component F2P (dimensionless)"
    legend_states[13] = "F2 in component F2 (dimensionless)"
    legend_constants[18] = "ks_c1_ in component model_parameters (first_order_rate_constant)"
    legend_constants[19] = "ks_c1__ in component model_parameters (first_order_rate_constant)"
    legend_constants[20] = "kpp_c1 in component model_parameters (first_order_rate_constant)"
    legend_algebraic[23] = "Vkp_c1 in component Vkp_c1 (first_order_rate_constant)"
    legend_states[14] = "Swi5 in component Swi5 (dimensionless)"
    legend_states[15] = "Cdc14 in component Cdc14 (dimensionless)"
    legend_states[16] = "Sic1P in component Sic1P (dimensionless)"
    legend_constants[21] = "ks_f6_ in component model_parameters (first_order_rate_constant)"
    legend_constants[22] = "ks_f6__ in component model_parameters (first_order_rate_constant)"
    legend_constants[23] = "ks_f6___ in component model_parameters (first_order_rate_constant)"
    legend_constants[24] = "kpp_f6 in component model_parameters (first_order_rate_constant)"
    legend_algebraic[28] = "Vkp_f6 in component Vkp_f6 (first_order_rate_constant)"
    legend_states[17] = "Cdc6P in component Cdc6P (dimensionless)"
    legend_states[18] = "Pds1 in component Pds1 (dimensionless)"
    legend_constants[25] = "ks_pds_ in component model_parameters (first_order_rate_constant)"
    legend_constants[26] = "ks1_pds__ in component model_parameters (first_order_rate_constant)"
    legend_constants[27] = "ks2_pds__ in component model_parameters (first_order_rate_constant)"
    legend_constants[28] = "kdi_esp in component model_parameters (first_order_rate_constant)"
    legend_algebraic[29] = "Vd_pds in component Vd_pds (first_order_rate_constant)"
    legend_constants[29] = "kas_esp in component model_parameters (first_order_rate_constant)"
    legend_algebraic[18] = "PE in component PE (dimensionless)"
    legend_states[19] = "Esp1 in component Esp1 (dimensionless)"
    legend_states[20] = "ORI in component ORI (dimensionless)"
    legend_constants[30] = "ks_ori in component model_parameters (first_order_rate_constant)"
    legend_constants[31] = "kd_ori in component model_parameters (first_order_rate_constant)"
    legend_constants[32] = "epsilon_ori_b5 in component model_parameters (dimensionless)"
    legend_constants[33] = "epsilon_ori_b2 in component model_parameters (dimensionless)"
    legend_states[21] = "BUD in component BUD (dimensionless)"
    legend_constants[34] = "ks_bud in component model_parameters (first_order_rate_constant)"
    legend_constants[35] = "kd_bud in component model_parameters (first_order_rate_constant)"
    legend_constants[36] = "epsilon_bud_n2 in component model_parameters (dimensionless)"
    legend_constants[37] = "epsilon_bud_n3 in component model_parameters (dimensionless)"
    legend_constants[38] = "epsilon_bud_b5 in component model_parameters (dimensionless)"
    legend_algebraic[10] = "Cln3 in component Cln3 (dimensionless)"
    legend_states[22] = "SPN in component SPN (dimensionless)"
    legend_constants[39] = "ks_spn in component model_parameters (first_order_rate_constant)"
    legend_constants[40] = "kd_spn in component model_parameters (first_order_rate_constant)"
    legend_constants[41] = "Jspn in component model_parameters (dimensionless)"
    legend_algebraic[25] = "G_sbf in component G_sbf (dimensionless)"
    legend_constants[42] = "Ji_sbf in component model_parameters (dimensionless)"
    legend_constants[43] = "Ja_sbf in component model_parameters (dimensionless)"
    legend_algebraic[24] = "Vi_sbf in component Vi_sbf (first_order_rate_constant)"
    legend_algebraic[22] = "Va_sbf in component Va_sbf (first_order_rate_constant)"
    legend_algebraic[0] = "G_mcm in component G_mcm (dimensionless)"
    legend_constants[44] = "Ji_mcm in component model_parameters (dimensionless)"
    legend_constants[45] = "Ja_mcm in component model_parameters (dimensionless)"
    legend_constants[46] = "ki_mcm in component model_parameters (first_order_rate_constant)"
    legend_constants[47] = "ka_mcm in component model_parameters (first_order_rate_constant)"
    legend_constants[48] = "C0 in component model_parameters (dimensionless)"
    legend_constants[49] = "Dn3 in component model_parameters (dimensionless)"
    legend_constants[50] = "Jn3 in component model_parameters (dimensionless)"
    legend_algebraic[12] = "Bck2 in component Bck2 (dimensionless)"
    legend_constants[51] = "B0 in component model_parameters (dimensionless)"
    legend_algebraic[1] = "Clb5_T in component Clb5_T (dimensionless)"
    legend_algebraic[2] = "Clb2_T in component Clb2_T (dimensionless)"
    legend_algebraic[15] = "Sic1_T in component Sic1_T (dimensionless)"
    legend_states[23] = "Swi5_T in component Swi5_T (dimensionless)"
    legend_constants[52] = "ks_swi_ in component model_parameters (first_order_rate_constant)"
    legend_constants[53] = "ks_swi__ in component model_parameters (first_order_rate_constant)"
    legend_constants[54] = "kd_swi in component model_parameters (first_order_rate_constant)"
    legend_constants[55] = "ka_swi in component model_parameters (first_order_rate_constant)"
    legend_constants[56] = "ki_swi in component model_parameters (first_order_rate_constant)"
    legend_states[24] = "APC_P in component APC_P (dimensionless)"
    legend_constants[57] = "ka_apc in component model_parameters (first_order_rate_constant)"
    legend_constants[58] = "ki_apc in component model_parameters (first_order_rate_constant)"
    legend_constants[59] = "Ja_apc in component model_parameters (dimensionless)"
    legend_constants[60] = "Ji_apc in component model_parameters (dimensionless)"
    legend_states[25] = "Cdc20_T in component Cdc20_T (dimensionless)"
    legend_constants[61] = "ks_20_ in component model_parameters (first_order_rate_constant)"
    legend_constants[62] = "ks_20__ in component model_parameters (first_order_rate_constant)"
    legend_constants[63] = "kd_20 in component model_parameters (first_order_rate_constant)"
    legend_states[26] = "Cdc20_A in component Cdc20_A (dimensionless)"
    legend_constants[64] = "ka_20_ in component model_parameters (first_order_rate_constant)"
    legend_constants[65] = "ka_20__ in component model_parameters (first_order_rate_constant)"
    legend_algebraic[3] = "kmad2 in component model_parameters (first_order_rate_constant)"
    legend_states[27] = "Cdh1_T in component Cdh1_T (dimensionless)"
    legend_constants[66] = "ks_cdh in component model_parameters (first_order_rate_constant)"
    legend_constants[67] = "kd_cdh in component model_parameters (first_order_rate_constant)"
    legend_states[28] = "Cdh1 in component Cdh1 (dimensionless)"
    legend_constants[68] = "Ja_cdh in component model_parameters (dimensionless)"
    legend_constants[69] = "Ji_cdh in component model_parameters (dimensionless)"
    legend_algebraic[13] = "Va_cdh in component Va_cdh (first_order_rate_constant)"
    legend_algebraic[16] = "Vi_cdh in component Vi_cdh (first_order_rate_constant)"
    legend_states[29] = "Tem1 in component Tem1 (dimensionless)"
    legend_algebraic[4] = "kbub2 in component model_parameters (first_order_rate_constant)"
    legend_algebraic[8] = "klte1 in component model_parameters (first_order_rate_constant)"
    legend_constants[70] = "Ja_tem in component model_parameters (dimensionless)"
    legend_constants[71] = "Ji_tem in component model_parameters (dimensionless)"
    legend_constants[72] = "Tem1_T in component model_parameters (dimensionless)"
    legend_states[30] = "Cdc15 in component Cdc15 (dimensionless)"
    legend_constants[73] = "ka_15_ in component model_parameters (first_order_rate_constant)"
    legend_constants[74] = "ka_15__ in component model_parameters (first_order_rate_constant)"
    legend_constants[75] = "ka_15___ in component model_parameters (first_order_rate_constant)"
    legend_constants[76] = "ki_15 in component model_parameters (first_order_rate_constant)"
    legend_constants[77] = "Cdc15_T in component model_parameters (dimensionless)"
    legend_states[31] = "Cdc14_T in component Cdc14_T (dimensionless)"
    legend_constants[78] = "ks_14 in component model_parameters (first_order_rate_constant)"
    legend_constants[79] = "kd_14 in component model_parameters (first_order_rate_constant)"
    legend_constants[80] = "kd_net in component model_parameters (first_order_rate_constant)"
    legend_constants[81] = "kdi_rent in component model_parameters (first_order_rate_constant)"
    legend_constants[82] = "kdi_rentp in component model_parameters (first_order_rate_constant)"
    legend_constants[83] = "kas_rent in component model_parameters (first_order_rate_constant)"
    legend_constants[84] = "kas_rentp in component model_parameters (first_order_rate_constant)"
    legend_states[32] = "RENT in component RENT (dimensionless)"
    legend_algebraic[5] = "RENTP in component RENTP (dimensionless)"
    legend_states[33] = "Net1 in component Net1 (dimensionless)"
    legend_algebraic[9] = "Net1P in component Net1P (dimensionless)"
    legend_states[34] = "Net1_T in component Net1_T (dimensionless)"
    legend_constants[85] = "ks_net in component model_parameters (first_order_rate_constant)"
    legend_algebraic[17] = "Cdc6_T in component Cdc6_T (dimensionless)"
    legend_algebraic[19] = "CKI_T in component CKI_T (dimensionless)"
    legend_constants[86] = "Esp1_T in component model_parameters (dimensionless)"
    legend_constants[87] = "kd_b5_ in component model_parameters (first_order_rate_constant)"
    legend_constants[88] = "kd_b5__ in component model_parameters (first_order_rate_constant)"
    legend_constants[89] = "kd_b2_ in component model_parameters (first_order_rate_constant)"
    legend_constants[90] = "kd_b2__ in component model_parameters (first_order_rate_constant)"
    legend_constants[91] = "kd_b2p in component model_parameters (first_order_rate_constant)"
    legend_constants[92] = "ka_sbf in component model_parameters (first_order_rate_constant)"
    legend_constants[93] = "epsilon_sbf_n2 in component model_parameters (dimensionless)"
    legend_constants[94] = "epsilon_sbf_n3 in component model_parameters (dimensionless)"
    legend_constants[95] = "epsilon_sbf_b5 in component model_parameters (dimensionless)"
    legend_constants[96] = "ki_sbf_ in component model_parameters (first_order_rate_constant)"
    legend_constants[97] = "ki_sbf__ in component model_parameters (first_order_rate_constant)"
    legend_constants[98] = "kd1_c1 in component model_parameters (first_order_rate_constant)"
    legend_constants[99] = "kd2_c1 in component model_parameters (first_order_rate_constant)"
    legend_constants[100] = "Jd2_c1 in component model_parameters (dimensionless)"
    legend_constants[101] = "epsilon_c1_n2 in component model_parameters (dimensionless)"
    legend_constants[102] = "epsilon_c1_n3 in component model_parameters (dimensionless)"
    legend_constants[103] = "epsilon_c1_k2 in component model_parameters (dimensionless)"
    legend_constants[104] = "epsilon_c1_b5 in component model_parameters (dimensionless)"
    legend_constants[105] = "epsilon_c1_b2 in component model_parameters (dimensionless)"
    legend_constants[106] = "Jd2_f6 in component model_parameters (dimensionless)"
    legend_constants[107] = "kd1_f6 in component model_parameters (first_order_rate_constant)"
    legend_constants[108] = "kd2_f6 in component model_parameters (first_order_rate_constant)"
    legend_constants[109] = "epsilon_f6_n2 in component model_parameters (dimensionless)"
    legend_constants[110] = "epsilon_f6_n3 in component model_parameters (dimensionless)"
    legend_constants[111] = "epsilon_f6_k2 in component model_parameters (dimensionless)"
    legend_constants[112] = "epsilon_f6_b5 in component model_parameters (dimensionless)"
    legend_constants[113] = "epsilon_f6_b2 in component model_parameters (dimensionless)"
    legend_constants[114] = "ka_cdh_ in component model_parameters (first_order_rate_constant)"
    legend_constants[115] = "ka_cdh__ in component model_parameters (first_order_rate_constant)"
    legend_constants[116] = "ki_cdh_ in component model_parameters (first_order_rate_constant)"
    legend_constants[117] = "ki_cdh__ in component model_parameters (first_order_rate_constant)"
    legend_constants[118] = "epsilon_cdh_n2 in component model_parameters (dimensionless)"
    legend_constants[119] = "epsilon_cdh_n3 in component model_parameters (dimensionless)"
    legend_constants[120] = "epsilon_cdh_b5 in component model_parameters (dimensionless)"
    legend_constants[121] = "epsilon_cdh_b2 in component model_parameters (dimensionless)"
    legend_algebraic[11] = "Vpp_net in component Vpp_net (first_order_rate_constant)"
    legend_constants[122] = "kpp_net_ in component model_parameters (first_order_rate_constant)"
    legend_constants[123] = "kpp_net__ in component model_parameters (first_order_rate_constant)"
    legend_states[35] = "PPX in component PPX (dimensionless)"
    legend_algebraic[14] = "Vkp_net in component Vkp_net (first_order_rate_constant)"
    legend_constants[124] = "kkp_net_ in component model_parameters (first_order_rate_constant)"
    legend_constants[125] = "kkp_net__ in component model_parameters (first_order_rate_constant)"
    legend_constants[126] = "ks_ppx in component model_parameters (first_order_rate_constant)"
    legend_algebraic[6] = "Vd_ppx in component Vd_ppx (first_order_rate_constant)"
    legend_constants[127] = "kd_ppx_ in component model_parameters (first_order_rate_constant)"
    legend_constants[128] = "kd_ppx__ in component model_parameters (first_order_rate_constant)"
    legend_constants[129] = "Jpds in component model_parameters (dimensionless)"
    legend_constants[130] = "J20_ppx in component model_parameters (dimensionless)"
    legend_constants[131] = "kd1_pds_ in component model_parameters (first_order_rate_constant)"
    legend_constants[132] = "kd2_pds__ in component model_parameters (first_order_rate_constant)"
    legend_constants[133] = "kd3_pds__ in component model_parameters (first_order_rate_constant)"
    legend_constants[134] = "Kez in component model_parameters (dimensionless)"
    legend_constants[135] = "Kez2 in component model_parameters (dimensionless)"
    legend_rates[0] = "d/dt mass in component mass (dimensionless)"
    legend_rates[1] = "d/dt Cln2 in component Cln2 (dimensionless)"
    legend_rates[2] = "d/dt Clb5 in component Clb5 (dimensionless)"
    legend_rates[9] = "d/dt Clb2 in component Clb2 (dimensionless)"
    legend_rates[7] = "d/dt Sic1 in component Sic1 (dimensionless)"
    legend_rates[16] = "d/dt Sic1P in component Sic1P (dimensionless)"
    legend_rates[11] = "d/dt C2 in component C2 (dimensionless)"
    legend_rates[4] = "d/dt C5 in component C5 (dimensionless)"
    legend_rates[10] = "d/dt C2P in component C2P (dimensionless)"
    legend_rates[3] = "d/dt C5P in component C5P (dimensionless)"
    legend_rates[8] = "d/dt Cdc6 in component Cdc6 (dimensionless)"
    legend_rates[17] = "d/dt Cdc6P in component Cdc6P (dimensionless)"
    legend_rates[13] = "d/dt F2 in component F2 (dimensionless)"
    legend_rates[18] = "d/dt Pds1 in component Pds1 (dimensionless)"
    legend_rates[19] = "d/dt Esp1 in component Esp1 (dimensionless)"
    legend_rates[20] = "d/dt ORI in component ORI (dimensionless)"
    legend_rates[21] = "d/dt BUD in component BUD (dimensionless)"
    legend_rates[22] = "d/dt SPN in component SPN (dimensionless)"
    legend_rates[6] = "d/dt F5 in component F5 (dimensionless)"
    legend_rates[12] = "d/dt F2P in component F2P (dimensionless)"
    legend_rates[5] = "d/dt F5P in component F5P (dimensionless)"
    legend_rates[23] = "d/dt Swi5_T in component Swi5_T (dimensionless)"
    legend_rates[14] = "d/dt Swi5 in component Swi5 (dimensionless)"
    legend_rates[24] = "d/dt APC_P in component APC_P (dimensionless)"
    legend_rates[25] = "d/dt Cdc20_T in component Cdc20_T (dimensionless)"
    legend_rates[26] = "d/dt Cdc20_A in component Cdc20_A (dimensionless)"
    legend_rates[27] = "d/dt Cdh1_T in component Cdh1_T (dimensionless)"
    legend_rates[28] = "d/dt Cdh1 in component Cdh1 (dimensionless)"
    legend_rates[29] = "d/dt Tem1 in component Tem1 (dimensionless)"
    legend_rates[30] = "d/dt Cdc15 in component Cdc15 (dimensionless)"
    legend_rates[31] = "d/dt Cdc14_T in component Cdc14_T (dimensionless)"
    legend_rates[15] = "d/dt Cdc14 in component Cdc14 (dimensionless)"
    legend_rates[34] = "d/dt Net1_T in component Net1_T (dimensionless)"
    legend_rates[33] = "d/dt Net1 in component Net1 (dimensionless)"
    legend_rates[32] = "d/dt RENT in component RENT (dimensionless)"
    legend_rates[35] = "d/dt PPX in component PPX (dimensionless)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 1.206
    constants[0] = 0.007702
    states[1] = 0.0652
    constants[1] = 0
    constants[2] = 0.15
    constants[3] = 0.12
    states[2] = 0.0518
    constants[4] = 0.0008
    constants[5] = 0.005
    constants[6] = 0.01
    constants[7] = 0.06
    constants[8] = 50
    constants[9] = 0.01
    constants[10] = 1
    constants[11] = 1
    states[3] = 0.0069
    states[4] = 0.0701
    states[5] = 7.9e-6
    states[6] = 7.2e-5
    states[7] = 0.0229
    states[8] = 0.1076
    states[9] = 0.1469
    constants[12] = 0.001
    constants[13] = 0.04
    constants[14] = 0.05
    constants[15] = 0.5
    constants[16] = 50
    constants[17] = 15
    states[10] = 0.024
    states[11] = 0.2384
    states[12] = 0.0274
    states[13] = 0.2361
    constants[18] = 0.012
    constants[19] = 0.12
    constants[20] = 4
    states[14] = 0.9562
    states[15] = 0.4683
    states[16] = 0.0064
    constants[21] = 0.024
    constants[22] = 0.12
    constants[23] = 0.004
    constants[24] = 4
    states[17] = 0.0155
    states[18] = 0.0256
    constants[25] = 0
    constants[26] = 0.03
    constants[27] = 0.055
    constants[28] = 0.5
    constants[29] = 50
    states[19] = 0.3013
    states[20] = 0.0009
    constants[30] = 2
    constants[31] = 0.06
    constants[32] = 0.9
    constants[33] = 0.45
    states[21] = 0.0085
    constants[34] = 0.2
    constants[35] = 0.06
    constants[36] = 0.25
    constants[37] = 0.05
    constants[38] = 1
    states[22] = 0.0305
    constants[39] = 0.1
    constants[40] = 0.06
    constants[41] = 0.14
    constants[42] = 0.01
    constants[43] = 0.01
    constants[44] = 0.1
    constants[45] = 0.1
    constants[46] = 0.15
    constants[47] = 1
    constants[48] = 0.4
    constants[49] = 1
    constants[50] = 6
    constants[51] = 0.054
    states[23] = 0.9765
    constants[52] = 0.005
    constants[53] = 0.08
    constants[54] = 0.08
    constants[55] = 2
    constants[56] = 0.05
    states[24] = 0.1015
    constants[57] = 0.1
    constants[58] = 0.15
    constants[59] = 0.1
    constants[60] = 0.1
    states[25] = 1.9163
    constants[61] = 0.006
    constants[62] = 0.6
    constants[63] = 0.3
    states[26] = 0.4443
    constants[64] = 0.05
    constants[65] = 0.2
    states[27] = 1
    constants[66] = 0.01
    constants[67] = 0.01
    states[28] = 0.9305
    constants[68] = 0.03
    constants[69] = 0.03
    states[29] = 0.9039
    constants[70] = 0.1
    constants[71] = 0.1
    constants[72] = 1
    states[30] = 0.6565
    constants[73] = 0.002
    constants[74] = 1
    constants[75] = 0.001
    constants[76] = 0.5
    constants[77] = 1
    states[31] = 2
    constants[78] = 0.2
    constants[79] = 0.1
    constants[80] = 0.03
    constants[81] = 1
    constants[82] = 2
    constants[83] = 200
    constants[84] = 1
    states[32] = 1.0495
    states[33] = 0.0186
    states[34] = 2.8
    constants[85] = 0.084
    constants[86] = 1
    constants[87] = 0.01
    constants[88] = 0.16
    constants[89] = 0.003
    constants[90] = 0.4
    constants[91] = 0.15
    constants[92] = 0.38
    constants[93] = 2
    constants[94] = 10
    constants[95] = 2
    constants[96] = 0.6
    constants[97] = 8
    constants[98] = 0.01
    constants[99] = 1
    constants[100] = 0.05
    constants[101] = 0.06
    constants[102] = 0.3
    constants[103] = 0.03
    constants[104] = 0.1
    constants[105] = 0.45
    constants[106] = 0.05
    constants[107] = 0.01
    constants[108] = 1
    constants[109] = 0.06
    constants[110] = 0.3
    constants[111] = 0.03
    constants[112] = 0.1
    constants[113] = 0.55
    constants[114] = 0.01
    constants[115] = 0.8
    constants[116] = 0.001
    constants[117] = 0.08
    constants[118] = 0.4
    constants[119] = 0.25
    constants[120] = 8
    constants[121] = 1.2
    constants[122] = 0.05
    constants[123] = 3
    states[35] = 0.1232
    constants[124] = 0.01
    constants[125] = 0.6
    constants[126] = 0.1
    constants[127] = 0.17
    constants[128] = 2
    constants[129] = 0.04
    constants[130] = 0.15
    constants[131] = 0.01
    constants[132] = 0.2
    constants[133] = 0.04
    constants[134] = 0.3
    constants[135] = 0.2
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[0] = states[0]*constants[0]
    rates[20] = constants[30]*(constants[32]*states[2]+constants[33]*states[9])-constants[31]*states[20]
    rates[22] = (constants[39]*states[9])/(constants[41]+states[9])-constants[40]*states[22]
    rates[24] = (constants[57]*states[9]*(1.00000-states[24]))/((constants[59]+1.00000)-states[24])-(constants[58]*states[24])/(constants[60]+states[24])
    rates[27] = constants[66]-constants[67]*states[27]
    rates[30] = (constants[73]*(constants[72]-states[29])+constants[74]*states[29]+constants[75]*states[15])*(constants[77]-states[30])-constants[76]*states[30]
    rates[31] = constants[78]-constants[79]*states[31]
    rates[34] = constants[85]-constants[80]*states[34]
    algebraic[3] = custom_piecewise([greater(states[20] , 1.00000) & less(states[22] , 1.00000), 8.00000 , True, 0.0100000])
    rates[26] = (constants[64]+constants[65]*states[24])*(states[25]-states[26])-(algebraic[3]+constants[63])*states[26]
    algebraic[6] = constants[127]+(constants[128]*(constants[130]+states[26])*constants[129])/(constants[129]+states[18])
    rates[35] = constants[126]-algebraic[6]*states[35]
    algebraic[0] = (2.00000*constants[44]*constants[47]*states[9])/((constants[46]+constants[45]*constants[46]+constants[44]*constants[47]*states[9]+power(power((constants[46]+constants[45]*constants[46]+constants[44]*constants[47]*states[9])-constants[47]*states[9], 2.00000)-4.00000*(constants[46]-constants[47]*states[9])*constants[44]*constants[47]*states[9], 1.0/2))-constants[47]*states[9])
    algebraic[7] = algebraic[0]
    rates[23] = (constants[52]+constants[53]*algebraic[7])-constants[54]*states[23]
    rates[14] = (constants[52]+constants[53]*algebraic[7]+constants[55]*states[15]*(states[23]-states[14]))-(constants[54]+constants[56]*states[9])*states[14]
    rates[25] = (constants[61]+constants[62]*algebraic[7])-constants[63]*states[25]
    algebraic[4] = custom_piecewise([greater(states[20] , 1.00000) & less(states[22] , 1.00000), 1.00000 , True, 0.200000])
    algebraic[8] = custom_piecewise([greater(states[22] , 1.00000) & greater(states[9] , constants[134]), 1.00000 , True, 0.100000])
    rates[29] = (algebraic[8]*(constants[72]-states[29]))/((constants[70]+constants[72])-states[29])-(algebraic[4]*states[29])/(constants[71]+states[29])
    algebraic[5] = states[31]-(states[32]+states[15])
    algebraic[9] = (states[34]+states[15])-(states[33]+states[31])
    rates[15] = (constants[78]+constants[80]*(states[32]+algebraic[5])+constants[81]*states[32]+constants[82]*algebraic[5])-(constants[79]*states[15]+(constants[83]*states[33]+constants[84]*algebraic[9])*states[15])
    algebraic[10] = (constants[48]*constants[49]*states[0])/(constants[50]+constants[49]*states[0])
    rates[21] = constants[34]*(constants[36]*states[1]+constants[37]*algebraic[10]+constants[38]*states[2])-constants[35]*states[21]
    algebraic[11] = constants[122]+constants[123]*states[35]
    algebraic[14] = (constants[124]+constants[125]*states[30])*states[0]
    rates[33] = (constants[85]+constants[79]*states[32]+constants[81]*states[32]+algebraic[11]*algebraic[9])-(constants[80]*states[33]+constants[83]*states[15]*states[33]+algebraic[14]*states[33])
    rates[32] = (constants[83]*states[15]*states[33]+algebraic[11]*algebraic[5])-((constants[79]+constants[80])*states[32]+constants[81]*states[32]+algebraic[14]*states[32])
    algebraic[13] = constants[114]+constants[115]*states[15]
    algebraic[16] = constants[116]+constants[117]*(constants[119]*algebraic[10]+constants[118]*states[1]+constants[120]*states[2]+constants[121]*states[9])
    rates[28] = (constants[66]+(algebraic[13]*(states[27]-states[28]))/((constants[68]+states[27])-states[28]))-(constants[67]*states[28]+(algebraic[16]*states[28])/(constants[69]+states[28]))
    algebraic[21] = constants[89]+constants[90]*states[28]+constants[91]*states[26]
    rates[9] = ((constants[12]+constants[13]*algebraic[7])*states[0]+constants[11]*states[10]+constants[14]*states[11]+constants[10]*states[12]+constants[15]*states[13])-(algebraic[21]+constants[16]*states[7]+constants[17]*states[8])*states[9]
    algebraic[20] = constants[87]+constants[88]*states[26]
    algebraic[12] = constants[51]*states[0]
    algebraic[15] = states[7]+states[16]+states[11]+states[10]+states[4]+states[3]
    algebraic[23] = constants[98]+(constants[99]*(constants[102]*algebraic[10]+constants[103]*algebraic[12]+constants[101]*states[1]+constants[104]*states[2]+constants[105]*states[9]))/(constants[100]+algebraic[15])
    rates[7] = (constants[18]+constants[19]*states[14]+(algebraic[21]+constants[14])*states[11]+(algebraic[20]+constants[7])*states[4]+constants[20]*states[15]*states[16])-(constants[16]*states[9]+constants[8]*states[2]+algebraic[23])*states[7]
    rates[16] = (algebraic[23]*states[7]-(constants[20]*states[15]+constants[11])*states[16])+algebraic[21]*states[10]+algebraic[20]*states[3]
    rates[11] = (constants[16]*states[9]*states[7]+constants[20]*states[15]*states[10])-(constants[14]+algebraic[21]+algebraic[23])*states[11]
    rates[4] = (constants[8]*states[2]*states[7]+constants[20]*states[15]*states[3])-(constants[7]+algebraic[20]+algebraic[23])*states[4]
    rates[10] = algebraic[23]*states[11]-(constants[20]*states[15]+constants[11]+algebraic[21])*states[10]
    rates[3] = algebraic[23]*states[4]-(constants[20]*states[15]+constants[11]+algebraic[20])*states[3]
    algebraic[24] = constants[96]+constants[97]*states[9]
    algebraic[22] = constants[92]*(constants[93]*states[1]+constants[94]*(algebraic[10]+algebraic[12])+constants[95]*states[2])
    algebraic[25] = (2.00000*constants[42]*algebraic[22])/((algebraic[24]+constants[43]*algebraic[24]+constants[42]*algebraic[22]+power(power((algebraic[24]+constants[43]*algebraic[24]+constants[42]*algebraic[22])-algebraic[22], 2.00000)-4.00000*(algebraic[24]-algebraic[22])*constants[42]*algebraic[22], 1.0/2))-algebraic[22])
    algebraic[26] = algebraic[25]
    rates[2] = ((constants[4]+constants[5]*algebraic[26])*states[0]+constants[11]*states[3]+constants[7]*states[4]+constants[10]*states[5]+constants[6]*states[6])-(algebraic[20]+constants[8]*states[7]+constants[9]*states[8])*states[2]
    algebraic[27] = algebraic[26]
    rates[1] = (constants[1]+constants[2]*algebraic[27])*states[0]-constants[3]*states[1]
    algebraic[17] = states[8]+states[17]+states[13]+states[12]+states[6]+states[5]
    algebraic[28] = constants[107]+(constants[108]*(constants[110]*algebraic[10]+constants[111]*algebraic[12]+constants[109]*states[1]+constants[112]*states[2]+constants[113]*states[9]))/(constants[106]+algebraic[17])
    rates[8] = (constants[21]+constants[22]*states[14]+constants[23]*algebraic[27]+(algebraic[21]+constants[15])*states[13]+(algebraic[20]+constants[6])*states[6]+constants[24]*states[15]*states[17])-(constants[17]*states[9]+constants[9]*states[2]+algebraic[28])*states[8]
    rates[17] = (algebraic[28]*states[8]-(constants[24]*states[15]+constants[10])*states[17])+algebraic[21]*states[12]+algebraic[20]*states[5]
    rates[13] = (constants[17]*states[9]*states[8]+constants[24]*states[15]*states[12])-(constants[15]+algebraic[21]+algebraic[28])*states[13]
    algebraic[29] = constants[131]+constants[132]*states[26]+constants[133]*states[28]
    algebraic[18] = constants[86]-states[19]
    rates[18] = (constants[25]+constants[26]*algebraic[27]+constants[27]*algebraic[7]+constants[28]*algebraic[18])-(algebraic[29]+constants[29]*states[19])*states[18]
    rates[19] = -constants[29]*states[18]*states[19]+(constants[28]+algebraic[29])*algebraic[18]
    rates[6] = (constants[9]*states[2]*states[8]+constants[24]*states[15]*states[5])-(constants[6]+algebraic[20]+algebraic[28])*states[6]
    rates[12] = algebraic[28]*states[13]-(constants[24]*states[15]+constants[10]+algebraic[21])*states[12]
    rates[5] = algebraic[28]*states[6]-(constants[24]*states[15]+constants[10]+algebraic[20])*states[5]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[3] = custom_piecewise([greater(states[20] , 1.00000) & less(states[22] , 1.00000), 8.00000 , True, 0.0100000])
    algebraic[6] = constants[127]+(constants[128]*(constants[130]+states[26])*constants[129])/(constants[129]+states[18])
    algebraic[0] = (2.00000*constants[44]*constants[47]*states[9])/((constants[46]+constants[45]*constants[46]+constants[44]*constants[47]*states[9]+power(power((constants[46]+constants[45]*constants[46]+constants[44]*constants[47]*states[9])-constants[47]*states[9], 2.00000)-4.00000*(constants[46]-constants[47]*states[9])*constants[44]*constants[47]*states[9], 1.0/2))-constants[47]*states[9])
    algebraic[7] = algebraic[0]
    algebraic[4] = custom_piecewise([greater(states[20] , 1.00000) & less(states[22] , 1.00000), 1.00000 , True, 0.200000])
    algebraic[8] = custom_piecewise([greater(states[22] , 1.00000) & greater(states[9] , constants[134]), 1.00000 , True, 0.100000])
    algebraic[5] = states[31]-(states[32]+states[15])
    algebraic[9] = (states[34]+states[15])-(states[33]+states[31])
    algebraic[10] = (constants[48]*constants[49]*states[0])/(constants[50]+constants[49]*states[0])
    algebraic[11] = constants[122]+constants[123]*states[35]
    algebraic[14] = (constants[124]+constants[125]*states[30])*states[0]
    algebraic[13] = constants[114]+constants[115]*states[15]
    algebraic[16] = constants[116]+constants[117]*(constants[119]*algebraic[10]+constants[118]*states[1]+constants[120]*states[2]+constants[121]*states[9])
    algebraic[21] = constants[89]+constants[90]*states[28]+constants[91]*states[26]
    algebraic[20] = constants[87]+constants[88]*states[26]
    algebraic[12] = constants[51]*states[0]
    algebraic[15] = states[7]+states[16]+states[11]+states[10]+states[4]+states[3]
    algebraic[23] = constants[98]+(constants[99]*(constants[102]*algebraic[10]+constants[103]*algebraic[12]+constants[101]*states[1]+constants[104]*states[2]+constants[105]*states[9]))/(constants[100]+algebraic[15])
    algebraic[24] = constants[96]+constants[97]*states[9]
    algebraic[22] = constants[92]*(constants[93]*states[1]+constants[94]*(algebraic[10]+algebraic[12])+constants[95]*states[2])
    algebraic[25] = (2.00000*constants[42]*algebraic[22])/((algebraic[24]+constants[43]*algebraic[24]+constants[42]*algebraic[22]+power(power((algebraic[24]+constants[43]*algebraic[24]+constants[42]*algebraic[22])-algebraic[22], 2.00000)-4.00000*(algebraic[24]-algebraic[22])*constants[42]*algebraic[22], 1.0/2))-algebraic[22])
    algebraic[26] = algebraic[25]
    algebraic[27] = algebraic[26]
    algebraic[17] = states[8]+states[17]+states[13]+states[12]+states[6]+states[5]
    algebraic[28] = constants[107]+(constants[108]*(constants[110]*algebraic[10]+constants[111]*algebraic[12]+constants[109]*states[1]+constants[112]*states[2]+constants[113]*states[9]))/(constants[106]+algebraic[17])
    algebraic[29] = constants[131]+constants[132]*states[26]+constants[133]*states[28]
    algebraic[18] = constants[86]-states[19]
    algebraic[1] = states[2]+states[4]+states[3]+states[6]+states[5]
    algebraic[2] = states[9]+states[11]+states[10]+states[13]+states[12]
    algebraic[19] = algebraic[15]+algebraic[17]
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
        self.kg = 0.007702
        self.ks_n2_ = 0
        self.ks_n2__1 = 0.15
        self.kd_n2 = 0.12
        self.ks_b5_ = 0.0008
        self.ks_b5__1 = 0.005
        self.kdi_f5 = 0.01
        self.kdi_b5 = 0.06
        self.kas_b5 = 50
        self.kas_f5 = 0.01
        self.kd3_f6 = 1
        self.kd3_c1 = 1
        self.ks_b2_ = 0.001
        self.ks_b2__1 = 0.04
        self.kdi_b2 = 0.05
        self.kdi_f2 = 0.5
        self.kas_b2 = 50
        self.kas_f2 = 15
        self.ks_c1_ = 0.012
        self.ks_c1__1 = 0.12
        self.kpp_c1 = 4
        self.ks_f6_ = 0.024
        self.ks_f6__1 = 0.12
        self.ks_f6__2 = 0.004
        self.kpp_f6 = 4
        self.ks_pds_ = 0
        self.ks1_pds_ = 0.03
        self.ks2_pds_ = 0.055
        self.kdi_esp = 0.5
        self.kas_esp = 50
        self.ks_ori = 2
        self.kd_ori = 0.06
        self.epsilon_ori_b5 = 0.9
        self.epsilon_ori_b2 = 0.45
        self.ks_bud = 0.2
        self.kd_bud = 0.06
        self.epsilon_bud_n2 = 0.25
        self.epsilon_bud_n3 = 0.05
        self.epsilon_bud_b5 = 1
        self.ks_spn = 0.1
        self.kd_spn = 0.06
        self.Jspn = 0.14
        self.Ji_sbf = 0.01
        self.Ja_sbf = 0.01
        self.Ji_mcm = 0.1
        self.Ja_mcm = 0.1
        self.ki_mcm = 0.15
        self.ka_mcm = 1
        self.C0 = 0.4
        self.Dn3 = 1
        self.Jn3 = 6
        self.B0 = 0.054
        self.ks_swi_ = 0.005
        self.ks_swi__1 = 0.08
        self.kd_swi = 0.08
        self.ka_swi = 2
        self.ki_swi = 0.05
        self.ka_apc = 0.1
        self.ki_apc = 0.15
        self.Ja_apc = 0.1
        self.Ji_apc = 0.1
        self.ks_20_ = 0.006
        self.ks_20__1 = 0.6
        self.kd_20 = 0.3
        self.ka_20_ = 0.05
        self.ka_20__1 = 0.2
        self.ks_cdh = 0.01
        self.kd_cdh = 0.01
        self.Ja_cdh = 0.03
        self.Ji_cdh = 0.03
        self.Ja_tem = 0.1
        self.Ji_tem = 0.1
        self.Tem1_T = 1
        self.ka_15_ = 0.002
        self.ka_15__1 = 1
        self.ka_15__2 = 0.001
        self.ki_15 = 0.5
        self.Cdc15_T = 1
        self.ks_14 = 0.2
        self.kd_14 = 0.1
        self.kd_net = 0.03
        self.kdi_rent = 1
        self.kdi_rentp = 2
        self.kas_rent = 200
        self.kas_rentp = 1
        self.ks_net = 0.084
        self.Esp1_T = 1
        self.kd_b5_ = 0.01
        self.kd_b5__1 = 0.16
        self.kd_b2_ = 0.003
        self.kd_b2__1 = 0.4
        self.kd_b2p = 0.15
        self.ka_sbf = 0.38
        self.epsilon_sbf_n2 = 2
        self.epsilon_sbf_n3 = 10
        self.epsilon_sbf_b5 = 2
        self.ki_sbf_ = 0.6
        self.ki_sbf__1 = 8
        self.kd1_c1 = 0.01
        self.kd2_c1 = 1
        self.Jd2_c1 = 0.05
        self.epsilon_c1_n2 = 0.06
        self.epsilon_c1_n3 = 0.3
        self.epsilon_c1_k2 = 0.03
        self.epsilon_c1_b5 = 0.1
        self.epsilon_c1_b2 = 0.45
        self.Jd2_f6 = 0.05
        self.kd1_f6 = 0.01
        self.kd2_f6 = 1
        self.epsilon_f6_n2 = 0.06
        self.epsilon_f6_n3 = 0.3
        self.epsilon_f6_k2 = 0.03
        self.epsilon_f6_b5 = 0.1
        self.epsilon_f6_b2 = 0.55
        self.ka_cdh_ = 0.01
        self.ka_cdh__1 = 0.8
        self.ki_cdh_ = 0.001
        self.ki_cdh__1 = 0.08
        self.epsilon_cdh_n2 = 0.4
        self.epsilon_cdh_n3 = 0.25
        self.epsilon_cdh_b5 = 8
        self.epsilon_cdh_b2 = 1.2
        self.kpp_net_ = 0.05
        self.kpp_net__1 = 3
        self.kkp_net_ = 0.01
        self.kkp_net__1 = 0.6
        self.ks_ppx = 0.1
        self.kd_ppx_ = 0.17
        self.kd_ppx__1 = 2
        self.Jpds = 0.04
        self.J20_ppx = 0.15
        self.kd1_pds_ = 0.01
        self.kd2_pds_ = 0.2
        self.kd3_pds_ = 0.04
        self.Kez = 0.3
        self.Kez2 = 0.2

    def to_dict(self):
        return {
            "kg": self.kg,
            "ks_n2_": self.ks_n2_,
            "ks_n2__1": self.ks_n2__1,
            "kd_n2": self.kd_n2,
            "ks_b5_": self.ks_b5_,
            "ks_b5__1": self.ks_b5__1,
            "kdi_f5": self.kdi_f5,
            "kdi_b5": self.kdi_b5,
            "kas_b5": self.kas_b5,
            "kas_f5": self.kas_f5,
            "kd3_f6": self.kd3_f6,
            "kd3_c1": self.kd3_c1,
            "ks_b2_": self.ks_b2_,
            "ks_b2__1": self.ks_b2__1,
            "kdi_b2": self.kdi_b2,
            "kdi_f2": self.kdi_f2,
            "kas_b2": self.kas_b2,
            "kas_f2": self.kas_f2,
            "ks_c1_": self.ks_c1_,
            "ks_c1__1": self.ks_c1__1,
            "kpp_c1": self.kpp_c1,
            "ks_f6_": self.ks_f6_,
            "ks_f6__1": self.ks_f6__1,
            "ks_f6__2": self.ks_f6__2,
            "kpp_f6": self.kpp_f6,
            "ks_pds_": self.ks_pds_,
            "ks1_pds_": self.ks1_pds_,
            "ks2_pds_": self.ks2_pds_,
            "kdi_esp": self.kdi_esp,
            "kas_esp": self.kas_esp,
            "ks_ori": self.ks_ori,
            "kd_ori": self.kd_ori,
            "epsilon_ori_b5": self.epsilon_ori_b5,
            "epsilon_ori_b2": self.epsilon_ori_b2,
            "ks_bud": self.ks_bud,
            "kd_bud": self.kd_bud,
            "epsilon_bud_n2": self.epsilon_bud_n2,
            "epsilon_bud_n3": self.epsilon_bud_n3,
            "epsilon_bud_b5": self.epsilon_bud_b5,
            "ks_spn": self.ks_spn,
            "kd_spn": self.kd_spn,
            "Jspn": self.Jspn,
            "Ji_sbf": self.Ji_sbf,
            "Ja_sbf": self.Ja_sbf,
            "Ji_mcm": self.Ji_mcm,
            "Ja_mcm": self.Ja_mcm,
            "ki_mcm": self.ki_mcm,
            "ka_mcm": self.ka_mcm,
            "C0": self.C0,
            "Dn3": self.Dn3,
            "Jn3": self.Jn3,
            "B0": self.B0,
            "ks_swi_": self.ks_swi_,
            "ks_swi__1": self.ks_swi__1,
            "kd_swi": self.kd_swi,
            "ka_swi": self.ka_swi,
            "ki_swi": self.ki_swi,
            "ka_apc": self.ka_apc,
            "ki_apc": self.ki_apc,
            "Ja_apc": self.Ja_apc,
            "Ji_apc": self.Ji_apc,
            "ks_20_": self.ks_20_,
            "ks_20__1": self.ks_20__1,
            "kd_20": self.kd_20,
            "ka_20_": self.ka_20_,
            "ka_20__1": self.ka_20__1,
            "ks_cdh": self.ks_cdh,
            "kd_cdh": self.kd_cdh,
            "Ja_cdh": self.Ja_cdh,
            "Ji_cdh": self.Ji_cdh,
            "Ja_tem": self.Ja_tem,
            "Ji_tem": self.Ji_tem,
            "Tem1_T": self.Tem1_T,
            "ka_15_": self.ka_15_,
            "ka_15__1": self.ka_15__1,
            "ka_15__2": self.ka_15__2,
            "ki_15": self.ki_15,
            "Cdc15_T": self.Cdc15_T,
            "ks_14": self.ks_14,
            "kd_14": self.kd_14,
            "kd_net": self.kd_net,
            "kdi_rent": self.kdi_rent,
            "kdi_rentp": self.kdi_rentp,
            "kas_rent": self.kas_rent,
            "kas_rentp": self.kas_rentp,
            "ks_net": self.ks_net,
            "Esp1_T": self.Esp1_T,
            "kd_b5_": self.kd_b5_,
            "kd_b5__1": self.kd_b5__1,
            "kd_b2_": self.kd_b2_,
            "kd_b2__1": self.kd_b2__1,
            "kd_b2p": self.kd_b2p,
            "ka_sbf": self.ka_sbf,
            "epsilon_sbf_n2": self.epsilon_sbf_n2,
            "epsilon_sbf_n3": self.epsilon_sbf_n3,
            "epsilon_sbf_b5": self.epsilon_sbf_b5,
            "ki_sbf_": self.ki_sbf_,
            "ki_sbf__1": self.ki_sbf__1,
            "kd1_c1": self.kd1_c1,
            "kd2_c1": self.kd2_c1,
            "Jd2_c1": self.Jd2_c1,
            "epsilon_c1_n2": self.epsilon_c1_n2,
            "epsilon_c1_n3": self.epsilon_c1_n3,
            "epsilon_c1_k2": self.epsilon_c1_k2,
            "epsilon_c1_b5": self.epsilon_c1_b5,
            "epsilon_c1_b2": self.epsilon_c1_b2,
            "Jd2_f6": self.Jd2_f6,
            "kd1_f6": self.kd1_f6,
            "kd2_f6": self.kd2_f6,
            "epsilon_f6_n2": self.epsilon_f6_n2,
            "epsilon_f6_n3": self.epsilon_f6_n3,
            "epsilon_f6_k2": self.epsilon_f6_k2,
            "epsilon_f6_b5": self.epsilon_f6_b5,
            "epsilon_f6_b2": self.epsilon_f6_b2,
            "ka_cdh_": self.ka_cdh_,
            "ka_cdh__1": self.ka_cdh__1,
            "ki_cdh_": self.ki_cdh_,
            "ki_cdh__1": self.ki_cdh__1,
            "epsilon_cdh_n2": self.epsilon_cdh_n2,
            "epsilon_cdh_n3": self.epsilon_cdh_n3,
            "epsilon_cdh_b5": self.epsilon_cdh_b5,
            "epsilon_cdh_b2": self.epsilon_cdh_b2,
            "kpp_net_": self.kpp_net_,
            "kpp_net__1": self.kpp_net__1,
            "kkp_net_": self.kkp_net_,
            "kkp_net__1": self.kkp_net__1,
            "ks_ppx": self.ks_ppx,
            "kd_ppx_": self.kd_ppx_,
            "kd_ppx__1": self.kd_ppx__1,
            "Jpds": self.Jpds,
            "J20_ppx": self.J20_ppx,
            "kd1_pds_": self.kd1_pds_,
            "kd2_pds_": self.kd2_pds_,
            "kd3_pds_": self.kd3_pds_,
            "Kez": self.Kez,
            "Kez2": self.Kez2,
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
        y0=[1.206, 0.0652, 0.0518, 0.0069, 0.0701, 7.9e-6, 7.2e-5, 0.0229, 0.1076, 0.1469, 0.024, 0.2384, 0.0274, 0.2361, 0.9562, 0.4683, 0.0064, 0.0155, 0.0256, 0.3013, 0.0009, 0.0085, 0.0305, 0.9765, 0.1015, 1.9163, 0.4443, 1, 0.9305, 0.9039, 0.6565, 2, 1.0495, 0.0186, 2.8, 0.1232],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "chen_calzone_csikasznagy_cross_novak_tyson_2004"
        self.curve_names = [
            "mass",
            "Cln2",
            "Clb5",
            "C5P",
            "C5",
            "F5P",
            "F5",
            "Sic1",
            "Cdc6",
            "Clb2",
            "C2P",
            "C2",
            "F2P",
            "F2",
            "Swi5",
            "Cdc14",
            "Sic1P",
            "Cdc6P",
            "Pds1",
            "Esp1",
            "ORI",
            "BUD",
            "SPN",
            "Swi5_T",
            "APC_P",
            "Cdc20_T",
            "Cdc20_A",
            "Cdh1_T",
            "Cdh1",
            "Tem1",
            "Cdc15",
            "Cdc14_T",
            "RENT",
            "Net1",
            "Net1_T",
            "PPX",
        ]
        self.state_names = ['mass', 'Cln2', 'Clb5', 'C5P', 'C5', 'F5P', 'F5', 'Sic1', 'Cdc6', 'Clb2', 'C2P', 'C2', 'F2P', 'F2', 'Swi5', 'Cdc14', 'Sic1P', 'Cdc6P', 'Pds1', 'Esp1', 'ORI', 'BUD', 'SPN', 'Swi5_T', 'APC_P', 'Cdc20_T', 'Cdc20_A', 'Cdh1_T', 'Cdh1', 'Tem1', 'Cdc15', 'Cdc14_T', 'RENT', 'Net1', 'Net1_T', 'PPX']
        self.algebraic_names = ['G_mcm', 'Clb5_T', 'Clb2_T', 'kmad2', 'kbub2', 'RENTP', 'Vd_ppx', 'Mcm1', 'klte1', 'Net1P', 'Cln3', 'Vpp_net', 'Bck2', 'Va_cdh', 'Vkp_net', 'Sic1_T', 'Vi_cdh', 'Cdc6_T', 'PE', 'CKI_T', 'Vd_b5', 'Vd_b2', 'Va_sbf', 'Vkp_c1', 'Vi_sbf', 'G_sbf', 'MBF', 'SBF', 'Vkp_f6', 'Vd_pds']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 136
        p = self.params

        # direct mapping
        c[0] = p.kg
        c[1] = p.ks_n2_
        c[2] = p.ks_n2__1
        c[3] = p.kd_n2
        c[4] = p.ks_b5_
        c[5] = p.ks_b5__1
        c[6] = p.kdi_f5
        c[7] = p.kdi_b5
        c[8] = p.kas_b5
        c[9] = p.kas_f5
        c[10] = p.kd3_f6
        c[11] = p.kd3_c1
        c[12] = p.ks_b2_
        c[13] = p.ks_b2__1
        c[14] = p.kdi_b2
        c[15] = p.kdi_f2
        c[16] = p.kas_b2
        c[17] = p.kas_f2
        c[18] = p.ks_c1_
        c[19] = p.ks_c1__1
        c[20] = p.kpp_c1
        c[21] = p.ks_f6_
        c[22] = p.ks_f6__1
        c[23] = p.ks_f6__2
        c[24] = p.kpp_f6
        c[25] = p.ks_pds_
        c[26] = p.ks1_pds_
        c[27] = p.ks2_pds_
        c[28] = p.kdi_esp
        c[29] = p.kas_esp
        c[30] = p.ks_ori
        c[31] = p.kd_ori
        c[32] = p.epsilon_ori_b5
        c[33] = p.epsilon_ori_b2
        c[34] = p.ks_bud
        c[35] = p.kd_bud
        c[36] = p.epsilon_bud_n2
        c[37] = p.epsilon_bud_n3
        c[38] = p.epsilon_bud_b5
        c[39] = p.ks_spn
        c[40] = p.kd_spn
        c[41] = p.Jspn
        c[42] = p.Ji_sbf
        c[43] = p.Ja_sbf
        c[44] = p.Ji_mcm
        c[45] = p.Ja_mcm
        c[46] = p.ki_mcm
        c[47] = p.ka_mcm
        c[48] = p.C0
        c[49] = p.Dn3
        c[50] = p.Jn3
        c[51] = p.B0
        c[52] = p.ks_swi_
        c[53] = p.ks_swi__1
        c[54] = p.kd_swi
        c[55] = p.ka_swi
        c[56] = p.ki_swi
        c[57] = p.ka_apc
        c[58] = p.ki_apc
        c[59] = p.Ja_apc
        c[60] = p.Ji_apc
        c[61] = p.ks_20_
        c[62] = p.ks_20__1
        c[63] = p.kd_20
        c[64] = p.ka_20_
        c[65] = p.ka_20__1
        c[66] = p.ks_cdh
        c[67] = p.kd_cdh
        c[68] = p.Ja_cdh
        c[69] = p.Ji_cdh
        c[70] = p.Ja_tem
        c[71] = p.Ji_tem
        c[72] = p.Tem1_T
        c[73] = p.ka_15_
        c[74] = p.ka_15__1
        c[75] = p.ka_15__2
        c[76] = p.ki_15
        c[77] = p.Cdc15_T
        c[78] = p.ks_14
        c[79] = p.kd_14
        c[80] = p.kd_net
        c[81] = p.kdi_rent
        c[82] = p.kdi_rentp
        c[83] = p.kas_rent
        c[84] = p.kas_rentp
        c[85] = p.ks_net
        c[86] = p.Esp1_T
        c[87] = p.kd_b5_
        c[88] = p.kd_b5__1
        c[89] = p.kd_b2_
        c[90] = p.kd_b2__1
        c[91] = p.kd_b2p
        c[92] = p.ka_sbf
        c[93] = p.epsilon_sbf_n2
        c[94] = p.epsilon_sbf_n3
        c[95] = p.epsilon_sbf_b5
        c[96] = p.ki_sbf_
        c[97] = p.ki_sbf__1
        c[98] = p.kd1_c1
        c[99] = p.kd2_c1
        c[100] = p.Jd2_c1
        c[101] = p.epsilon_c1_n2
        c[102] = p.epsilon_c1_n3
        c[103] = p.epsilon_c1_k2
        c[104] = p.epsilon_c1_b5
        c[105] = p.epsilon_c1_b2
        c[106] = p.Jd2_f6
        c[107] = p.kd1_f6
        c[108] = p.kd2_f6
        c[109] = p.epsilon_f6_n2
        c[110] = p.epsilon_f6_n3
        c[111] = p.epsilon_f6_k2
        c[112] = p.epsilon_f6_b5
        c[113] = p.epsilon_f6_b2
        c[114] = p.ka_cdh_
        c[115] = p.ka_cdh__1
        c[116] = p.ki_cdh_
        c[117] = p.ki_cdh__1
        c[118] = p.epsilon_cdh_n2
        c[119] = p.epsilon_cdh_n3
        c[120] = p.epsilon_cdh_b5
        c[121] = p.epsilon_cdh_b2
        c[122] = p.kpp_net_
        c[123] = p.kpp_net__1
        c[124] = p.kkp_net_
        c[125] = p.kkp_net__1
        c[126] = p.ks_ppx
        c[127] = p.kd_ppx_
        c[128] = p.kd_ppx__1
        c[129] = p.Jpds
        c[130] = p.J20_ppx
        c[131] = p.kd1_pds_
        c[132] = p.kd2_pds_
        c[133] = p.kd3_pds_
        c[134] = p.Kez
        c[135] = p.Kez2

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
