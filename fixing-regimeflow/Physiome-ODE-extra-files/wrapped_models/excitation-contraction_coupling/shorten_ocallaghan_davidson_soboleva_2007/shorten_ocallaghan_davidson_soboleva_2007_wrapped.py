# Size of variable arrays:
sizeAlgebraic = 71
sizeStates = 56
sizeConstants = 105
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component cell (millisecond)"
    legend_constants[0] = "C_m in component wal_environment (microF_per_cm2)"
    legend_constants[1] = "gam in component wal_environment (dimensionless)"
    legend_constants[2] = "R_a in component wal_environment (ohm_cm2)"
    legend_constants[3] = "tsi in component wal_environment (centi_metre)"
    legend_constants[4] = "tsi2 in component wal_environment (centi_metre)"
    legend_constants[5] = "tsi3 in component wal_environment (centi_metre)"
    legend_constants[6] = "FF in component wal_environment (C_per_mol)"
    legend_constants[7] = "tau_K in component wal_environment (millisecond)"
    legend_constants[8] = "tau_Na in component wal_environment (millisecond)"
    legend_constants[9] = "f_T in component wal_environment (dimensionless)"
    legend_constants[10] = "tau_K2 in component wal_environment (millisecond)"
    legend_constants[11] = "tau_Na2 in component wal_environment (millisecond)"
    legend_constants[12] = "I_K_rest in component wal_environment (microA_per_cm2)"
    legend_constants[13] = "I_Na_rest in component wal_environment (microA_per_cm2)"
    legend_constants[14] = "alpha_h_bar in component wal_environment (per_millisecond)"
    legend_constants[15] = "alpha_m_bar in component wal_environment (per_millisecond_per_millivolt)"
    legend_constants[16] = "alpha_n_bar in component wal_environment (per_millisecond_per_millivolt)"
    legend_constants[17] = "beta_h_bar in component wal_environment (per_millisecond)"
    legend_constants[18] = "beta_m_bar in component wal_environment (per_millisecond)"
    legend_constants[19] = "beta_n_bar in component wal_environment (per_millisecond)"
    legend_constants[20] = "V_m in component wal_environment (millivolt)"
    legend_constants[21] = "V_n in component wal_environment (millivolt)"
    legend_constants[22] = "V_h in component wal_environment (millivolt)"
    legend_constants[23] = "V_a in component wal_environment (millivolt)"
    legend_constants[24] = "V_S_inf in component wal_environment (millivolt)"
    legend_constants[25] = "V_h_K_inf in component wal_environment (millivolt)"
    legend_constants[26] = "A_a in component wal_environment (millivolt)"
    legend_constants[27] = "A_S_inf in component wal_environment (millivolt)"
    legend_constants[28] = "A_h_K_inf in component wal_environment (millivolt)"
    legend_constants[29] = "K_alpha_h in component wal_environment (millivolt)"
    legend_constants[30] = "K_beta_h in component wal_environment (millivolt)"
    legend_constants[31] = "K_alpha_m in component wal_environment (millivolt)"
    legend_constants[32] = "K_alpha_n in component wal_environment (millivolt)"
    legend_constants[33] = "K_beta_m in component wal_environment (millivolt)"
    legend_constants[34] = "K_beta_n in component wal_environment (millivolt)"
    legend_constants[35] = "RR in component wal_environment (milliJ_per_degreeK_per_mol)"
    legend_constants[36] = "TT in component wal_environment (degreeK)"
    legend_constants[37] = "g_Cl_bar in component wal_environment (milliS_per_cm2)"
    legend_constants[38] = "g_K_bar in component wal_environment (milliS_per_cm2)"
    legend_constants[39] = "g_Na_bar in component wal_environment (milliS_per_cm2)"
    legend_constants[40] = "G_K in component wal_environment (milliS_per_cm2)"
    legend_constants[41] = "del in component wal_environment (dimensionless)"
    legend_constants[42] = "K_K in component wal_environment (milliM2)"
    legend_constants[43] = "K_S in component wal_environment (milliM2)"
    legend_constants[44] = "K_m_K in component wal_environment (milliM)"
    legend_constants[45] = "K_m_Na in component wal_environment (milliM)"
    legend_constants[46] = "S_i in component wal_environment (milliM)"
    legend_constants[47] = "J_NaK_bar in component wal_environment (micro_mol_per_cm2_per_second)"
    legend_constants[48] = "V_tau in component wal_environment (millivolt)"
    legend_algebraic[0] = "I_T in component wal_environment (microA_per_cm2)"
    legend_states[0] = "vS in component wal_environment (millivolt)"
    legend_states[1] = "vT in component wal_environment (millivolt)"
    legend_algebraic[51] = "I_ionic_s in component wal_environment (microA_per_cm2)"
    legend_algebraic[70] = "I_ionic_t in component wal_environment (microA_per_cm2)"
    legend_states[2] = "K_t in component wal_environment (milliM)"
    legend_states[3] = "K_i in component wal_environment (milliM)"
    legend_states[4] = "K_e in component wal_environment (milliM)"
    legend_states[5] = "Na_i in component wal_environment (milliM)"
    legend_states[6] = "Na_t in component wal_environment (milliM)"
    legend_states[7] = "Na_e in component wal_environment (milliM)"
    legend_algebraic[13] = "E_K in component wal_environment (millivolt)"
    legend_algebraic[25] = "E_K_t in component wal_environment (millivolt)"
    legend_algebraic[26] = "Cl_i in component wal_environment (milliM)"
    legend_algebraic[27] = "Cl_o in component wal_environment (milliM)"
    legend_algebraic[28] = "Cl_i_t in component wal_environment (milliM)"
    legend_algebraic[29] = "Cl_o_t in component wal_environment (milliM)"
    legend_algebraic[30] = "J_K in component wal_environment (milliV_milliM)"
    legend_algebraic[31] = "J_K_t in component wal_environment (milliV_milliM)"
    legend_constants[49] = "eta_Cl in component wal_environment (dimensionless)"
    legend_constants[50] = "eta_IR in component wal_environment (dimensionless)"
    legend_constants[51] = "eta_DR in component wal_environment (dimensionless)"
    legend_constants[52] = "eta_Na in component wal_environment (dimensionless)"
    legend_constants[53] = "eta_NaK in component wal_environment (dimensionless)"
    legend_algebraic[36] = "I_Cl in component sarco_Cl_channel (microA_per_cm2)"
    legend_algebraic[41] = "I_IR in component sarco_IR_channel (microA_per_cm2)"
    legend_algebraic[43] = "I_DR in component sarco_DR_channel (microA_per_cm2)"
    legend_algebraic[46] = "I_Na in component sarco_Na_channel (microA_per_cm2)"
    legend_algebraic[50] = "I_NaK in component sarco_NaK_channel (microA_per_cm2)"
    legend_algebraic[55] = "I_Cl_t in component t_Cl_channel (microA_per_cm2)"
    legend_algebraic[60] = "I_IR_t in component t_IR_channel (microA_per_cm2)"
    legend_algebraic[62] = "I_DR_t in component t_DR_channel (microA_per_cm2)"
    legend_algebraic[65] = "I_Na_t in component t_Na_channel (microA_per_cm2)"
    legend_algebraic[69] = "I_NaK_t in component t_NaK_channel (microA_per_cm2)"
    legend_algebraic[32] = "I_HH in component wal_environment (microA_per_cm2)"
    legend_algebraic[33] = "a in component sarco_Cl_channel (dimensionless)"
    legend_algebraic[34] = "J_Cl in component sarco_Cl_channel (milliV_milliM)"
    legend_algebraic[35] = "g_Cl in component sarco_Cl_channel (milliS_per_cm2)"
    legend_algebraic[37] = "K_R in component sarco_IR_channel (milliM)"
    legend_algebraic[38] = "g_IR_bar in component sarco_IR_channel (milliS_per_cm2)"
    legend_algebraic[39] = "y in component sarco_IR_channel (dimensionless)"
    legend_algebraic[40] = "g_IR in component sarco_IR_channel (milliS_per_cm2)"
    legend_algebraic[1] = "alpha_n in component sarco_DR_channel (per_millisecond)"
    legend_algebraic[14] = "beta_n in component sarco_DR_channel (per_millisecond)"
    legend_algebraic[2] = "h_K_inf in component sarco_DR_channel (dimensionless)"
    legend_algebraic[15] = "tau_h_K in component sarco_DR_channel (millisecond)"
    legend_states[8] = "n in component sarco_DR_channel (dimensionless)"
    legend_states[9] = "h_K in component sarco_DR_channel (dimensionless)"
    legend_algebraic[42] = "g_DR in component sarco_DR_channel (milliS_per_cm2)"
    legend_algebraic[3] = "alpha_h in component sarco_Na_channel (per_millisecond)"
    legend_algebraic[16] = "beta_h in component sarco_Na_channel (per_millisecond)"
    legend_algebraic[4] = "alpha_m in component sarco_Na_channel (per_millisecond)"
    legend_algebraic[17] = "beta_m in component sarco_Na_channel (per_millisecond)"
    legend_algebraic[5] = "S_inf in component sarco_Na_channel (dimensionless)"
    legend_algebraic[18] = "tau_S in component sarco_Na_channel (millisecond)"
    legend_states[10] = "m in component sarco_Na_channel (dimensionless)"
    legend_states[11] = "h in component sarco_Na_channel (dimensionless)"
    legend_states[12] = "S in component sarco_Na_channel (dimensionless)"
    legend_algebraic[45] = "g_Na in component sarco_Na_channel (milliS_per_cm2)"
    legend_algebraic[44] = "J_Na in component sarco_Na_channel (milliV_milliM)"
    legend_algebraic[47] = "sig in component sarco_NaK_channel (dimensionless)"
    legend_algebraic[48] = "f1 in component sarco_NaK_channel (dimensionless)"
    legend_algebraic[49] = "I_NaK_bar in component sarco_NaK_channel (microA_per_cm2)"
    legend_algebraic[52] = "a_t in component t_Cl_channel (dimensionless)"
    legend_algebraic[53] = "J_Cl_t in component t_Cl_channel (milliV_milliM)"
    legend_algebraic[54] = "g_Cl_t in component t_Cl_channel (milliS_per_cm2)"
    legend_algebraic[56] = "K_R_t in component t_IR_channel (milliM)"
    legend_algebraic[57] = "g_IR_bar_t in component t_IR_channel (milliS_per_cm2)"
    legend_algebraic[58] = "y_t in component t_IR_channel (dimensionless)"
    legend_algebraic[59] = "g_IR_t in component t_IR_channel (milliS_per_cm2)"
    legend_algebraic[6] = "alpha_n_t in component t_DR_channel (per_millisecond)"
    legend_algebraic[19] = "beta_n_t in component t_DR_channel (per_millisecond)"
    legend_algebraic[7] = "h_K_inf_t in component t_DR_channel (dimensionless)"
    legend_algebraic[20] = "tau_h_K_t in component t_DR_channel (millisecond)"
    legend_states[13] = "n_t in component t_DR_channel (dimensionless)"
    legend_states[14] = "h_K_t in component t_DR_channel (dimensionless)"
    legend_algebraic[61] = "g_DR_t in component t_DR_channel (milliS_per_cm2)"
    legend_algebraic[8] = "alpha_h_t in component t_Na_channel (per_millisecond)"
    legend_algebraic[21] = "beta_h_t in component t_Na_channel (per_millisecond)"
    legend_algebraic[9] = "alpha_m_t in component t_Na_channel (per_millisecond)"
    legend_algebraic[22] = "beta_m_t in component t_Na_channel (per_millisecond)"
    legend_algebraic[10] = "S_inf_t in component t_Na_channel (dimensionless)"
    legend_algebraic[23] = "tau_S_t in component t_Na_channel (millisecond)"
    legend_states[15] = "m_t in component t_Na_channel (dimensionless)"
    legend_states[16] = "h_t in component t_Na_channel (dimensionless)"
    legend_states[17] = "S_t in component t_Na_channel (dimensionless)"
    legend_algebraic[64] = "g_Na_t in component t_Na_channel (milliS_per_cm2)"
    legend_algebraic[63] = "J_Na_t in component t_Na_channel (milliV_milliM)"
    legend_algebraic[66] = "sig_t in component t_NaK_channel (dimensionless)"
    legend_algebraic[67] = "f1_t in component t_NaK_channel (dimensionless)"
    legend_algebraic[68] = "I_NaK_bar_t in component t_NaK_channel (microA_per_cm2)"
    legend_states[18] = "O_0 in component sternrios (dimensionless)"
    legend_states[19] = "O_1 in component sternrios (dimensionless)"
    legend_states[20] = "O_2 in component sternrios (dimensionless)"
    legend_states[21] = "O_3 in component sternrios (dimensionless)"
    legend_states[22] = "O_4 in component sternrios (dimensionless)"
    legend_constants[54] = "k_L in component sternrios (per_millisecond)"
    legend_constants[55] = "k_Lm in component sternrios (per_millisecond)"
    legend_constants[56] = "f in component sternrios (dimensionless)"
    legend_constants[57] = "alpha1 in component sternrios (per_millisecond)"
    legend_constants[58] = "K in component sternrios (millivolt)"
    legend_constants[59] = "Vbar in component sternrios (millivolt)"
    legend_states[23] = "C_0 in component sternrios (dimensionless)"
    legend_states[24] = "C_1 in component sternrios (dimensionless)"
    legend_states[25] = "C_2 in component sternrios (dimensionless)"
    legend_states[26] = "C_3 in component sternrios (dimensionless)"
    legend_states[27] = "C_4 in component sternrios (dimensionless)"
    legend_algebraic[11] = "k_C in component sternrios (per_millisecond)"
    legend_algebraic[24] = "k_Cm in component sternrios (per_millisecond)"
    legend_constants[60] = "nu_SR in component razumova (micromolar_per_millisecond_micrometre3)"
    legend_constants[61] = "K_SR in component razumova (micromolar)"
    legend_constants[62] = "L_e in component razumova (micrometre3_per_millisecond)"
    legend_constants[63] = "tau_R in component razumova (micrometre3_per_millisecond)"
    legend_constants[64] = "tau_SR_R in component razumova (micrometre3_per_millisecond)"
    legend_constants[65] = "L_x in component razumova (micrometre)"
    legend_constants[66] = "R_R in component razumova (micrometre)"
    legend_constants[99] = "V_o in component razumova (micrometre3)"
    legend_constants[101] = "V_1 in component razumova (micrometre3)"
    legend_constants[102] = "V_2 in component razumova (micrometre3)"
    legend_constants[100] = "V_SR in component razumova (micrometre3)"
    legend_constants[103] = "V_SR1 in component razumova (micrometre3)"
    legend_constants[104] = "V_SR2 in component razumova (micrometre3)"
    legend_constants[67] = "k_T_on in component razumova (per_micromolar_per_millisecond)"
    legend_constants[68] = "k_T_off in component razumova (per_millisecond)"
    legend_constants[69] = "T_tot in component razumova (micromolar)"
    legend_constants[70] = "k_P_on in component razumova (per_micromolar_per_millisecond)"
    legend_constants[71] = "k_P_off in component razumova (per_millisecond)"
    legend_constants[72] = "P_tot in component razumova (micromolar)"
    legend_constants[73] = "k_Mg_on in component razumova (per_micromolar_per_millisecond)"
    legend_constants[74] = "k_Mg_off in component razumova (per_millisecond)"
    legend_constants[75] = "k_Cs_on in component razumova (per_micromolar_per_millisecond)"
    legend_constants[76] = "k_Cs_off in component razumova (per_millisecond)"
    legend_constants[77] = "Cs_tot in component razumova (micromolar)"
    legend_constants[78] = "k_CATP_on in component razumova (per_micromolar_per_millisecond)"
    legend_constants[79] = "k_CATP_off in component razumova (per_millisecond)"
    legend_constants[80] = "k_MATP_on in component razumova (per_micromolar_per_millisecond)"
    legend_constants[81] = "k_MATP_off in component razumova (per_millisecond)"
    legend_constants[82] = "tau_ATP in component razumova (micrometre3_per_millisecond)"
    legend_constants[83] = "tau_Mg in component razumova (micrometre3_per_millisecond)"
    legend_constants[84] = "k_0_on in component razumova (per_millisecond)"
    legend_constants[85] = "k_0_off in component razumova (per_millisecond)"
    legend_constants[86] = "k_Ca_on in component razumova (per_millisecond)"
    legend_constants[87] = "k_Ca_off in component razumova (per_millisecond)"
    legend_constants[88] = "f_o in component razumova (per_millisecond)"
    legend_constants[89] = "f_p in component razumova (per_millisecond)"
    legend_constants[90] = "h_o in component razumova (per_millisecond)"
    legend_constants[91] = "h_p in component razumova (per_millisecond)"
    legend_constants[92] = "g_o in component razumova (per_millisecond)"
    legend_constants[93] = "b_p in component razumova (per_millisecond)"
    legend_constants[94] = "k_p in component razumova (micrometre3_per_millisecond)"
    legend_constants[95] = "A_p in component razumova (per_milliM3_per_millisecond)"
    legend_constants[96] = "B_p in component razumova (per_milliM2_per_millisecond)"
    legend_constants[97] = "PP in component razumova (milliM2)"
    legend_algebraic[12] = "T_0 in component razumova (micromolar)"
    legend_states[28] = "Ca_1 in component razumova (micromolar)"
    legend_states[29] = "Ca_SR1 in component razumova (micromolar)"
    legend_states[30] = "Ca_2 in component razumova (micromolar)"
    legend_states[31] = "Ca_SR2 in component razumova (micromolar)"
    legend_states[32] = "Ca_T_2 in component razumova (micromolar)"
    legend_states[33] = "Ca_P1 in component razumova (micromolar)"
    legend_states[34] = "Ca_P2 in component razumova (micromolar)"
    legend_states[35] = "Mg_P1 in component razumova (micromolar)"
    legend_states[36] = "Mg_P2 in component razumova (micromolar)"
    legend_states[37] = "Ca_Cs1 in component razumova (micromolar)"
    legend_states[38] = "Ca_Cs2 in component razumova (micromolar)"
    legend_states[39] = "Ca_ATP1 in component razumova (micromolar)"
    legend_states[40] = "Ca_ATP2 in component razumova (micromolar)"
    legend_states[41] = "Mg_ATP1 in component razumova (micromolar)"
    legend_states[42] = "Mg_ATP2 in component razumova (micromolar)"
    legend_states[43] = "ATP1 in component razumova (micromolar)"
    legend_states[44] = "ATP2 in component razumova (micromolar)"
    legend_states[45] = "Mg1 in component razumova (micromolar)"
    legend_states[46] = "Mg2 in component razumova (micromolar)"
    legend_states[47] = "Ca_CaT2 in component razumova (micromolar)"
    legend_states[48] = "D_0 in component razumova (micromolar)"
    legend_states[49] = "D_1 in component razumova (micromolar)"
    legend_states[50] = "D_2 in component razumova (micromolar)"
    legend_states[51] = "A_1 in component razumova (micromolar)"
    legend_states[52] = "A_2 in component razumova (micromolar)"
    legend_states[53] = "P in component razumova (milliM)"
    legend_states[54] = "P_SR in component razumova (milliM)"
    legend_states[55] = "P_C_SR in component razumova (milliM)"
    legend_constants[98] = "i2 in component razumova (micrometre3_per_millisecond)"
    legend_rates[0] = "d/dt vS in component wal_environment (millivolt)"
    legend_rates[1] = "d/dt vT in component wal_environment (millivolt)"
    legend_rates[3] = "d/dt K_i in component wal_environment (milliM)"
    legend_rates[2] = "d/dt K_t in component wal_environment (milliM)"
    legend_rates[4] = "d/dt K_e in component wal_environment (milliM)"
    legend_rates[5] = "d/dt Na_i in component wal_environment (milliM)"
    legend_rates[6] = "d/dt Na_t in component wal_environment (milliM)"
    legend_rates[7] = "d/dt Na_e in component wal_environment (milliM)"
    legend_rates[8] = "d/dt n in component sarco_DR_channel (dimensionless)"
    legend_rates[9] = "d/dt h_K in component sarco_DR_channel (dimensionless)"
    legend_rates[10] = "d/dt m in component sarco_Na_channel (dimensionless)"
    legend_rates[11] = "d/dt h in component sarco_Na_channel (dimensionless)"
    legend_rates[12] = "d/dt S in component sarco_Na_channel (dimensionless)"
    legend_rates[13] = "d/dt n_t in component t_DR_channel (dimensionless)"
    legend_rates[14] = "d/dt h_K_t in component t_DR_channel (dimensionless)"
    legend_rates[15] = "d/dt m_t in component t_Na_channel (dimensionless)"
    legend_rates[16] = "d/dt h_t in component t_Na_channel (dimensionless)"
    legend_rates[17] = "d/dt S_t in component t_Na_channel (dimensionless)"
    legend_rates[23] = "d/dt C_0 in component sternrios (dimensionless)"
    legend_rates[18] = "d/dt O_0 in component sternrios (dimensionless)"
    legend_rates[24] = "d/dt C_1 in component sternrios (dimensionless)"
    legend_rates[19] = "d/dt O_1 in component sternrios (dimensionless)"
    legend_rates[25] = "d/dt C_2 in component sternrios (dimensionless)"
    legend_rates[20] = "d/dt O_2 in component sternrios (dimensionless)"
    legend_rates[26] = "d/dt C_3 in component sternrios (dimensionless)"
    legend_rates[21] = "d/dt O_3 in component sternrios (dimensionless)"
    legend_rates[27] = "d/dt C_4 in component sternrios (dimensionless)"
    legend_rates[22] = "d/dt O_4 in component sternrios (dimensionless)"
    legend_rates[28] = "d/dt Ca_1 in component razumova (micromolar)"
    legend_rates[29] = "d/dt Ca_SR1 in component razumova (micromolar)"
    legend_rates[30] = "d/dt Ca_2 in component razumova (micromolar)"
    legend_rates[31] = "d/dt Ca_SR2 in component razumova (micromolar)"
    legend_rates[32] = "d/dt Ca_T_2 in component razumova (micromolar)"
    legend_rates[33] = "d/dt Ca_P1 in component razumova (micromolar)"
    legend_rates[34] = "d/dt Ca_P2 in component razumova (micromolar)"
    legend_rates[35] = "d/dt Mg_P1 in component razumova (micromolar)"
    legend_rates[36] = "d/dt Mg_P2 in component razumova (micromolar)"
    legend_rates[37] = "d/dt Ca_Cs1 in component razumova (micromolar)"
    legend_rates[38] = "d/dt Ca_Cs2 in component razumova (micromolar)"
    legend_rates[39] = "d/dt Ca_ATP1 in component razumova (micromolar)"
    legend_rates[40] = "d/dt Ca_ATP2 in component razumova (micromolar)"
    legend_rates[41] = "d/dt Mg_ATP1 in component razumova (micromolar)"
    legend_rates[42] = "d/dt Mg_ATP2 in component razumova (micromolar)"
    legend_rates[43] = "d/dt ATP1 in component razumova (micromolar)"
    legend_rates[44] = "d/dt ATP2 in component razumova (micromolar)"
    legend_rates[45] = "d/dt Mg1 in component razumova (micromolar)"
    legend_rates[46] = "d/dt Mg2 in component razumova (micromolar)"
    legend_rates[47] = "d/dt Ca_CaT2 in component razumova (micromolar)"
    legend_rates[48] = "d/dt D_0 in component razumova (micromolar)"
    legend_rates[49] = "d/dt D_1 in component razumova (micromolar)"
    legend_rates[50] = "d/dt D_2 in component razumova (micromolar)"
    legend_rates[51] = "d/dt A_1 in component razumova (micromolar)"
    legend_rates[52] = "d/dt A_2 in component razumova (micromolar)"
    legend_rates[53] = "d/dt P in component razumova (milliM)"
    legend_rates[54] = "d/dt P_SR in component razumova (milliM)"
    legend_rates[55] = "d/dt P_C_SR in component razumova (milliM)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    constants[0] = 1.0
    constants[1] = 4.8
    constants[2] = 150
    constants[3] = 0.000001
    constants[4] = 0.0025
    constants[5] = 0.0005
    constants[6] = 96485
    constants[7] = 350
    constants[8] = 350
    constants[9] = 0.0032
    constants[10] = 21875
    constants[11] = 21875
    constants[12] = 1.02
    constants[13] = -1.29
    constants[14] = 0.0081
    constants[15] = 0.288
    constants[16] = 0.0131
    constants[17] = 4.38
    constants[18] = 1.38
    constants[19] = 0.067
    constants[20] = -46
    constants[21] = -40
    constants[22] = -45
    constants[23] = 70
    constants[24] = -78
    constants[25] = -40
    constants[26] = 150
    constants[27] = 5.8
    constants[28] = 7.5
    constants[29] = 14.7
    constants[30] = 9
    constants[31] = 10
    constants[32] = 7
    constants[33] = 18
    constants[34] = 40
    constants[35] = 8314.41
    constants[36] = 293
    constants[37] = 19.65
    constants[38] = 64.8
    constants[39] = 804
    constants[40] = 11.1
    constants[41] = 0.4
    constants[42] = 950
    constants[43] = 1
    constants[44] = 1
    constants[45] = 13
    constants[46] = 10
    constants[47] = 0.000621
    constants[48] = 90
    states[0] = -79.974
    states[1] = -80.2
    states[2] = 5.9
    states[3] = 150.9
    states[4] = 5.9
    states[5] = 12.7
    states[6] = 133
    states[7] = 133
    constants[49] = 0.1
    constants[50] = 1.0
    constants[51] = 0.45
    constants[52] = 0.1
    constants[53] = 0.1
    states[8] = 0.009466
    states[9] = 0.9952
    states[10] = 0.0358
    states[11] = 0.4981
    states[12] = 0.581
    states[13] = 0.009466
    states[14] = 0.9952
    states[15] = 0.0358
    states[16] = 0.4981
    states[17] = 0.581
    states[18] = 0
    states[19] = 0
    states[20] = 0
    states[21] = 0
    states[22] = 0
    constants[54] = 0.002
    constants[55] = 1000
    constants[56] = 0.2
    constants[57] = 0.2
    constants[58] = 4.5
    constants[59] = -20
    states[23] = 1
    states[24] = 0
    states[25] = 0
    states[26] = 0
    states[27] = 0
    constants[60] = 4.875
    constants[61] = 1
    constants[62] = 0.00002
    constants[63] = 0.75
    constants[64] = 0.75
    constants[65] = 1.1
    constants[66] = 0.5
    constants[67] = 0.04425
    constants[68] = 0.115
    constants[69] = 140
    constants[70] = 0.0417
    constants[71] = 0.0005
    constants[72] = 1500
    constants[73] = 0.000033
    constants[74] = 0.003
    constants[75] = 0.000004
    constants[76] = 0.005
    constants[77] = 31000
    constants[78] = 0.15
    constants[79] = 30
    constants[80] = 0.0015
    constants[81] = 0.15
    constants[82] = 0.375
    constants[83] = 1.5
    constants[84] = 0
    constants[85] = 0.15
    constants[86] = 0.15
    constants[87] = 0.05
    constants[88] = 1.5
    constants[89] = 15
    constants[90] = 0.24
    constants[91] = 0.18
    constants[92] = 0.12
    constants[93] = 0.00002867
    constants[94] = 0.00000362
    constants[95] = 1
    constants[96] = 0.0001
    constants[97] = 6
    states[28] = 0.1
    states[29] = 1500
    states[30] = 0.1
    states[31] = 1500
    states[32] = 25
    states[33] = 615
    states[34] = 615
    states[35] = 811
    states[36] = 811
    states[37] = 16900
    states[38] = 16900
    states[39] = 0.4
    states[40] = 0.4
    states[41] = 7200
    states[42] = 7200
    states[43] = 799.6
    states[44] = 799.6
    states[45] = 1000
    states[46] = 1000
    states[47] = 3
    states[48] = 0.8
    states[49] = 1.2
    states[50] = 3
    states[51] = 0.3
    states[52] = 0.23
    states[53] = 0.23
    states[54] = 0.23
    states[55] = 0.23
    constants[98] = 300
    constants[99] = 0.950000*constants[65]* pi*(power(constants[66], 2.00000))
    constants[100] = 0.0500000*constants[65]* pi*(power(constants[66], 2.00000))
    constants[101] = 0.0100000*constants[99]
    constants[102] = 0.990000*constants[99]
    constants[103] = 0.0100000*constants[100]
    constants[104] = 0.990000*constants[100]
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[28] = (((((constants[98]*(states[18]+states[19]+states[20]+states[21]+states[22]))*((states[29]-states[28])/constants[101])-constants[60]*((states[28]/(states[28]+constants[61]))/constants[101]))+constants[62]*((states[29]-states[28])/constants[101]))+-constants[63]*((states[28]-states[30])/constants[101]))+-((constants[70]*states[28])*((constants[72]+-states[33])+-states[35])+-constants[71]*states[33]))+-((constants[78]*states[28])*states[43]+-constants[79]*states[39])
    rates[29] = (((-(constants[98]*(states[18]+states[19]+states[20]+states[21]+states[22]))*((states[29]-states[28])/constants[103])+constants[60]*((states[28]/(states[28]+constants[61]))/constants[103]))+-constants[62]*((states[29]-states[28])/constants[103]))+-constants[64]*((states[29]-states[31])/constants[103]))+-((constants[75]*states[29])*(constants[77]-states[37])+-constants[76]*states[37])
    rates[31] = (((constants[60]*((states[30]/(states[30]+constants[61]))/constants[104])+-constants[62]*((states[31]+-states[30])/constants[104]))+constants[64]*((states[29]+-states[31])/constants[104]))+-((constants[75]*states[31])*(constants[77]+-states[38])+-constants[76]*states[38]))-(1000.00/1.00000)*(constants[95]*(states[54]*(0.00100000/1.00000)*states[31]-constants[97])*(custom_piecewise([greater(states[54]*(0.00100000/1.00000)*states[31]-constants[97] , 0.00000), 1.00000 , True, 0.00000]))*(0.00100000/1.00000)*states[54]*states[31]-constants[96]*states[55]*(constants[97]-states[54]*(0.00100000/1.00000)*states[31])*(custom_piecewise([greater(constants[97]-states[54]*(0.00100000/1.00000)*states[31] , 0.00000), 1.00000 , True, 0.00000])))
    rates[33] = (constants[70]*states[28])*((constants[72]+-states[33])+-states[35])+-constants[71]*states[33]
    rates[34] = (constants[70]*states[30])*((constants[72]+-states[34])+-states[36])+-constants[71]*states[34]
    rates[35] = (constants[73]*(constants[72]+-states[33]+-states[35]))*states[45]+-constants[74]*states[35]
    rates[36] = (constants[73]*(constants[72]+-states[34]+-states[36]))*states[46]+-constants[74]*states[36]
    rates[37] = (constants[75]*states[29])*(constants[77]+-states[37])+-constants[76]*states[37]
    rates[38] = (constants[75]*states[31])*(constants[77]+-states[38])+-constants[76]*states[38]
    rates[39] = ((constants[78]*states[28])*states[43]+-constants[79]*states[39])+-constants[82]*((states[39]+-states[40])/constants[101])
    rates[40] = ((constants[78]*states[30])*states[44]+-constants[79]*states[40])+constants[82]*((states[39]+-states[40])/constants[102])
    rates[41] = ((constants[80]*states[45])*states[43]+-constants[81]*states[41])+-constants[82]*((states[41]+-states[42])/constants[101])
    rates[42] = ((constants[80]*states[46])*states[44]+-constants[81]*states[42])+constants[82]*((states[41]+-states[42])/constants[102])
    rates[43] = (-((constants[78]*states[28])*states[43]+-constants[79]*states[39])+-((constants[80]*states[45])*states[43]+-constants[81]*states[41]))+-constants[82]*((states[43]+-states[44])/constants[101])
    rates[44] = (-((constants[78]*states[30])*states[44]+-constants[79]*states[40])+-((constants[80]*states[46])*states[44]+-constants[81]*states[42]))+constants[82]*((states[43]+-states[44])/constants[102])
    rates[45] = (-((constants[73]*(constants[72]+-states[33]+-states[35]))*states[45]+-constants[74]*states[35])+-((constants[80]*states[45])*states[43]+-constants[81]*states[41]))+-constants[83]*((states[45]+-states[46])/constants[101])
    rates[46] = (-((constants[73]*(constants[72]+-states[34]+-states[36]))*states[46]+-constants[74]*states[36])+-((constants[80]*states[46])*states[44]+-constants[81]*states[42]))+constants[83]*((states[45]+-states[46])/constants[102])
    rates[47] = (((constants[67]*states[30])*states[32]+-constants[68]*states[47])+-constants[86]*states[47])+constants[87]*states[50]
    rates[49] = ((((constants[67]*states[30]*states[48]+-constants[68]*states[49])+constants[84]*states[32])+-constants[85]*states[49])+(-constants[67]*states[30])*states[49])+constants[68]*states[50]
    rates[50] = (((((constants[67]*states[30]*states[49]+-constants[68]*states[50])+constants[86]*states[47])+-constants[87]*states[50])+-constants[88]*states[50])+constants[89]*states[51])+constants[92]*states[52]
    rates[51] = ((constants[88]*states[50]+-constants[89]*states[51])+constants[91]*states[52])+-constants[90]*states[51]
    rates[52] = (-constants[91]*states[52]+constants[90]*states[51])+-constants[92]*states[52]
    rates[53] = (0.00100000/1.00000)*(constants[90]*states[51]-constants[91]*states[52])+-1.00000*constants[93]*states[53]+-1.00000*constants[94]*((states[53]-states[54])/constants[102])
    rates[54] = constants[94]*((states[53]-states[54])/constants[104])-1.00000*(constants[95]*(states[54]*(0.00100000/1.00000)*states[31]-constants[97])*(custom_piecewise([greater(states[54]*(0.00100000/1.00000)*states[31]-constants[97] , 0.00000), 1.00000 , True, 0.00000]))*(0.00100000/1.00000)*states[54]*states[31]-constants[96]*states[55]*(constants[97]-states[54]*(0.00100000/1.00000)*states[31])*(custom_piecewise([greater(constants[97]-states[54]*(0.00100000/1.00000)*states[31] , 0.00000), 1.00000 , True, 0.00000])))
    rates[55] = 1.00000*(constants[95]*(states[54]*(0.00100000/1.00000)*states[31]-constants[97])*(custom_piecewise([greater(states[54]*(0.00100000/1.00000)*states[31]-constants[97] , 0.00000), 1.00000 , True, 0.00000]))*(0.00100000/1.00000)*states[54]*states[31]-constants[96]*states[55]*(constants[97]-states[54]*(0.00100000/1.00000)*states[31])*(custom_piecewise([greater(constants[97]-states[54]*(0.00100000/1.00000)*states[31] , 0.00000), 1.00000 , True, 0.00000])))
    algebraic[12] = constants[69]+-states[32]+-states[47]+-states[48]+-states[49]+-states[50]+-states[51]+-states[52]
    rates[30] = ((((-constants[60]*((states[30]/(states[30]+constants[61]))/constants[102])+constants[62]*((states[31]+-states[30])/constants[102]))+constants[63]*((states[28]-states[30])/constants[102]))+-(((((((constants[67]*states[30]*algebraic[12]+-constants[68]*states[32])+constants[67]*states[30]*states[32])+-constants[68]*states[47])+constants[67]*states[30]*states[48])+-constants[68]*states[49])+constants[67]*states[30]*states[49])+-constants[68]*states[50]))+-((constants[70]*states[30])*(constants[72]+-states[34]+-states[36])+-constants[71]*states[34]))+-((constants[78]*states[30])*states[44]+-constants[79]*states[40])
    rates[32] = (((((constants[67]*states[30])*algebraic[12]+-constants[68]*states[32])+(-constants[67]*states[30])*states[32])+constants[68]*states[47])+-constants[84]*states[32])+constants[85]*states[49]
    rates[48] = (((-constants[67]*states[30])*states[48]+constants[68]*states[49])+constants[84]*algebraic[12])+-constants[85]*states[48]
    algebraic[1] = constants[16]*((states[0]-constants[21])/(1.00000-exp(-((states[0]-constants[21])/constants[32]))))
    algebraic[14] = constants[19]*exp(-((states[0]-constants[21])/constants[34]))
    rates[8] = algebraic[1]*(1.00000-states[8])-algebraic[14]*states[8]
    algebraic[2] = 1.00000/(1.00000+exp((states[0]-constants[25])/constants[28]))
    algebraic[15] = 1000.00*exp(-((states[0]+40.0000)/25.7500))
    rates[9] = (algebraic[2]-states[9])/algebraic[15]
    algebraic[4] = constants[15]*((states[0]-constants[20])/(1.00000-exp(-((states[0]-constants[20])/constants[31]))))
    algebraic[17] = constants[18]*exp(-((states[0]-constants[20])/constants[33]))
    rates[10] = algebraic[4]*(1.00000-states[10])-algebraic[17]*states[10]
    algebraic[3] = constants[14]*exp(-((states[0]-constants[22])/constants[29]))
    algebraic[16] = constants[17]/(1.00000+exp(-((states[0]-constants[22])/constants[30])))
    rates[11] = algebraic[3]*(1.00000-states[11])-algebraic[16]*states[11]
    algebraic[5] = 1.00000/(1.00000+exp((states[0]-constants[24])/constants[27]))
    algebraic[18] = 8571.00/(0.200000+5.65000*(power((states[0]+constants[48])/100.000, 2.00000)))
    rates[12] = (algebraic[5]-states[12])/algebraic[18]
    algebraic[6] = constants[16]*((states[1]-constants[21])/(1.00000-exp(-((states[1]-constants[21])/constants[32]))))
    algebraic[19] = constants[19]*exp(-((states[1]-constants[21])/constants[34]))
    rates[13] = algebraic[6]*(1.00000-states[13])-algebraic[19]*states[13]
    algebraic[7] = 1.00000/(1.00000+exp((states[1]-constants[25])/constants[28]))
    algebraic[20] = 1.00000*exp(-((states[1]+40.0000)/25.7500))
    rates[14] = (algebraic[7]-states[14])/algebraic[20]
    algebraic[9] = constants[15]*((states[1]-constants[20])/(1.00000-exp(-((states[1]-constants[20])/constants[31]))))
    algebraic[22] = constants[18]*exp(-((states[1]-constants[20])/constants[33]))
    rates[15] = algebraic[9]*(1.00000-states[15])-algebraic[22]*states[15]
    algebraic[8] = constants[14]*exp(-((states[1]-constants[22])/constants[29]))
    algebraic[21] = constants[17]/(1.00000+exp(-((states[1]-constants[22])/constants[30])))
    rates[16] = algebraic[8]*(1.00000-states[16])-algebraic[21]*states[16]
    algebraic[10] = 1.00000/(1.00000+exp((states[1]-constants[24])/constants[27]))
    algebraic[23] = 8571.00/(0.200000+5.65000*(power((states[1]+constants[48])/100.000, 2.00000)))
    rates[17] = (algebraic[10]-states[17])/algebraic[23]
    algebraic[11] = 0.500000*constants[57]*exp((states[1]-constants[59])/(8.00000*constants[58]))
    algebraic[24] = 0.500000*constants[57]*exp((constants[59]-states[1])/(8.00000*constants[58]))
    rates[23] = -constants[54]*states[23]+constants[55]*states[18]+-4.00000*algebraic[11]*states[23]+algebraic[24]*states[24]
    rates[18] = constants[54]*states[23]+-constants[55]*states[18]+(-4.00000*algebraic[11]*states[18])/constants[56]+constants[56]*algebraic[24]*states[19]
    rates[24] = 4.00000*algebraic[11]*states[23]+-algebraic[24]*states[24]+(-constants[54]*states[24])/constants[56]+constants[56]*constants[55]*states[19]+-3.00000*algebraic[11]*states[24]+2.00000*algebraic[24]*states[25]
    rates[19] = (constants[54]*states[24])/constants[56]+-constants[55]*constants[56]*states[19]+(4.00000*algebraic[11]*states[18])/constants[56]+-constants[56]*algebraic[24]*states[19]+(-3.00000*algebraic[11]*states[19])/constants[56]+2.00000*constants[56]*algebraic[24]*states[20]
    rates[25] = 3.00000*algebraic[11]*states[24]+-2.00000*algebraic[24]*states[25]+(-constants[54]*states[25])/(power(constants[56], 2.00000))+(power(constants[56], 2.00000))*constants[55]*states[20]+-2.00000*algebraic[11]*states[25]+3.00000*algebraic[24]*states[26]
    rates[20] = (3.00000*algebraic[11]*states[19])/constants[56]+-2.00000*constants[56]*algebraic[24]*states[20]+(constants[54]*states[25])/(power(constants[56], 2.00000))+-constants[55]*(power(constants[56], 2.00000))*states[20]+(-2.00000*algebraic[11]*states[20])/constants[56]+3.00000*constants[56]*algebraic[24]*states[21]
    rates[26] = 2.00000*algebraic[11]*states[25]+-3.00000*algebraic[24]*states[26]+(-constants[54]*states[26])/(power(constants[56], 3.00000))+constants[55]*(power(constants[56], 3.00000))*states[21]+-algebraic[11]*states[26]+4.00000*algebraic[24]*states[27]
    rates[21] = (constants[54]*states[26])/(power(constants[56], 3.00000))+-constants[55]*(power(constants[56], 3.00000))*states[21]+(2.00000*algebraic[11]*states[20])/constants[56]+-3.00000*algebraic[24]*constants[56]*states[21]+(-algebraic[11]*states[21])/constants[56]+4.00000*constants[56]*algebraic[24]*states[22]
    rates[27] = algebraic[11]*states[26]+-4.00000*algebraic[24]*states[27]+(-constants[54]*states[27])/(power(constants[56], 4.00000))+constants[55]*(power(constants[56], 4.00000))*states[22]
    rates[22] = (algebraic[11]*states[21])/constants[56]+-4.00000*constants[56]*algebraic[24]*states[22]+(constants[54]*states[27])/(power(constants[56], 4.00000))+-constants[55]*(power(constants[56], 4.00000))*states[22]
    algebraic[30] = states[0]*((states[3]-states[4]*exp((-1.00000*constants[6]*states[0])/(constants[35]*constants[36])))/(1.00000-exp((-1.00000*constants[6]*states[0])/(constants[35]*constants[36]))))
    algebraic[13] = ((constants[35]*constants[36])/constants[6])*log(states[4]/states[3])
    algebraic[37] = states[4]*exp((-constants[41]*algebraic[13])*(constants[6]/(constants[35]*constants[36])))
    algebraic[38] = constants[40]*((power(algebraic[37], 2.00000))/(constants[42]+power(algebraic[37], 2.00000)))
    algebraic[39] = 1.00000-power(1.00000+(constants[43]*(1.00000+(power(algebraic[37], 2.00000))/constants[42]))/((power(constants[46], 2.00000))*exp((2.00000*(1.00000-constants[41])*states[0]*constants[6])/(constants[35]*constants[36]))), -1.00000)
    algebraic[40] = algebraic[38]*algebraic[39]
    algebraic[41] = algebraic[40]*(custom_piecewise([greater(algebraic[30] , 0.00000), 1.00000 , True, 0.00000]))*(algebraic[30]/50.0000)
    algebraic[42] = (constants[38]*(power(states[8], 4.00000)))*states[9]
    algebraic[43] = algebraic[42]*(algebraic[30]/50.0000)
    algebraic[47] = (1.00000/7.00000)*(exp(states[7]/67.3000)-1.00000)
    algebraic[48] = power(1.00000+0.120000*exp(-0.100000*states[0]*(constants[6]/(constants[35]*constants[36])))+0.0400000*algebraic[47]*exp(-(states[0]*(constants[6]/(constants[35]*constants[36])))), -1.00000)
    algebraic[49] = constants[6]*(constants[47]/((power(1.00000+constants[44]/states[4], 2.00000))*(power(1.00000+constants[45]/states[5], 3.00000))))
    algebraic[50] = algebraic[49]*algebraic[48]
    rates[4] = (algebraic[41]+algebraic[43]+constants[12]+-2.00000*algebraic[50])/((1000.00/1.00000)*constants[6]*constants[5])+(states[2]-states[4])/constants[10]
    algebraic[45] = ((constants[39]*(power(states[10], 3.00000)))*states[11])*states[12]
    algebraic[44] = states[0]*((states[5]-states[7]*exp((-1.00000*constants[6]*states[0])/(constants[35]*constants[36])))/(1.00000-exp((-1.00000*constants[6]*states[0])/(constants[35]*constants[36]))))
    algebraic[46] = algebraic[45]*(algebraic[44]/75.0000)
    rates[7] = (algebraic[46]+constants[13]+3.00000*algebraic[50])/((1000.00/1.00000)*constants[6]*constants[5])+(states[6]-states[7])/constants[11]
    algebraic[0] = (1000.00/1.00000)*((states[0]-states[1])/constants[2])
    algebraic[26] = 156.500/(5.00000+exp((-constants[6]*algebraic[13])/(constants[35]*constants[36])))
    algebraic[27] = 156.500-5.00000*algebraic[26]
    algebraic[34] = states[0]*((algebraic[26]-algebraic[27]*exp((constants[6]*states[0])/(constants[35]*constants[36])))/(1.00000-exp((constants[6]*states[0])/(constants[35]*constants[36]))))
    algebraic[33] = 1.00000/(1.00000+exp((states[0]-constants[23])/constants[26]))
    algebraic[35] = constants[37]*(power(algebraic[33], 4.00000))
    algebraic[36] = algebraic[35]*(algebraic[34]/45.0000)
    algebraic[32] = custom_piecewise([greater_equal(voi , 0.00000) & less(voi , 0.500000), 150.000 , greater_equal(voi , 50.0000) & less(voi , 50.5000), 150.000 , greater_equal(voi , 100.000) & less(voi , 100.500), 150.000 , greater_equal(voi , 150.000) & less(voi , 150.500), 150.000 , greater_equal(voi , 200.000) & less(voi , 200.500), 150.000 , greater_equal(voi , 250.000) & less(voi , 250.500), 150.000 , greater_equal(voi , 300.000) & less(voi , 300.500), 150.000 , greater_equal(voi , 350.000) & less(voi , 350.500), 150.000 , greater_equal(voi , 400.000) & less(voi , 400.500), 150.000 , True, 0.00000])
    algebraic[51] = algebraic[36]+algebraic[41]+algebraic[43]+algebraic[46]+algebraic[50]+-algebraic[32]
    rates[0] = -((algebraic[51]+algebraic[0])/constants[0])
    algebraic[31] = states[1]*((states[3]-states[2]*exp((-1.00000*constants[6]*states[1])/(constants[35]*constants[36])))/(1.00000-exp((-1.00000*constants[6]*states[1])/(constants[35]*constants[36]))))
    algebraic[25] = ((constants[35]*constants[36])/constants[6])*log(states[2]/states[3])
    algebraic[56] = states[2]*exp((-constants[41]*algebraic[25])*(constants[6]/(constants[35]*constants[36])))
    algebraic[57] = constants[40]*((power(algebraic[56], 2.00000))/(constants[42]+power(algebraic[56], 2.00000)))
    algebraic[58] = 1.00000-power(1.00000+(constants[43]*(1.00000+(power(algebraic[56], 2.00000))/constants[42]))/((power(constants[46], 2.00000))*exp((2.00000*(1.00000-constants[41])*states[1]*constants[6])/(constants[35]*constants[36]))), -1.00000)
    algebraic[59] = algebraic[57]*algebraic[58]
    algebraic[60] = constants[50]*algebraic[59]*(algebraic[31]/50.0000)
    algebraic[61] = (constants[38]*(power(states[13], 4.00000)))*states[14]
    algebraic[62] = constants[51]*algebraic[61]*(algebraic[31]/50.0000)
    algebraic[66] = (1.00000/7.00000)*(exp(states[6]/67.3000)-1.00000)
    algebraic[67] = power(1.00000+0.120000*exp(-0.100000*states[1]*(constants[6]/(constants[35]*constants[36])))+0.0400000*algebraic[66]*exp(-(states[1]*(constants[6]/(constants[35]*constants[36])))), -1.00000)
    algebraic[68] = constants[6]*(constants[47]/((power(1.00000+constants[44]/states[2], 2.00000))*(power(1.00000+constants[45]/states[5], 3.00000))))
    algebraic[69] = constants[53]*algebraic[68]*algebraic[67]
    rates[3] = -constants[9]*((algebraic[60]+algebraic[62]+constants[12]+-2.00000*algebraic[69])/((1000.00/1.00000)*constants[6]*constants[3]))-(algebraic[41]+algebraic[43]+constants[12]+-2.00000*algebraic[50])/((1000.00/1.00000)*constants[6]*constants[4])
    rates[2] = (algebraic[60]+algebraic[62]+constants[12]+-2.00000*algebraic[69])/((1000.00/1.00000)*constants[6]*constants[3])-(states[2]-states[4])/constants[7]
    algebraic[64] = ((constants[39]*(power(states[15], 3.00000)))*states[16])*states[17]
    algebraic[63] = states[1]*((states[5]-states[6]*exp((-1.00000*constants[6]*states[1])/(constants[35]*constants[36])))/(1.00000-exp((-1.00000*constants[6]*states[1])/(constants[35]*constants[36]))))
    algebraic[65] = constants[52]*algebraic[64]*(algebraic[63]/75.0000)
    rates[5] = -constants[9]*((algebraic[65]+constants[13]+3.00000*algebraic[69])/((1000.00/1.00000)*constants[6]*constants[3]))-(algebraic[46]+constants[13]+3.00000*algebraic[50])/((1000.00/1.00000)*constants[6]*constants[4])
    rates[6] = (algebraic[65]+constants[13]+3.00000*algebraic[69])/((1000.00/1.00000)*constants[6]*constants[3])-(states[6]-states[7])/constants[8]
    algebraic[28] = 156.500/(5.00000+exp((-constants[6]*algebraic[25])/(constants[35]*constants[36])))
    algebraic[29] = 156.500-5.00000*algebraic[28]
    algebraic[53] = states[1]*((algebraic[28]-algebraic[29]*exp((constants[6]*states[1])/(constants[35]*constants[36])))/(1.00000-exp((constants[6]*states[1])/(constants[35]*constants[36]))))
    algebraic[52] = 1.00000/(1.00000+exp((states[1]-constants[23])/constants[26]))
    algebraic[54] = constants[37]*(power(algebraic[52], 4.00000))
    algebraic[55] = constants[49]*algebraic[54]*(algebraic[53]/45.0000)
    algebraic[70] = algebraic[55]+algebraic[60]+algebraic[62]+algebraic[65]+algebraic[69]
    rates[1] = -((algebraic[70]-algebraic[0]/constants[1])/constants[0])
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[12] = constants[69]+-states[32]+-states[47]+-states[48]+-states[49]+-states[50]+-states[51]+-states[52]
    algebraic[1] = constants[16]*((states[0]-constants[21])/(1.00000-exp(-((states[0]-constants[21])/constants[32]))))
    algebraic[14] = constants[19]*exp(-((states[0]-constants[21])/constants[34]))
    algebraic[2] = 1.00000/(1.00000+exp((states[0]-constants[25])/constants[28]))
    algebraic[15] = 1000.00*exp(-((states[0]+40.0000)/25.7500))
    algebraic[4] = constants[15]*((states[0]-constants[20])/(1.00000-exp(-((states[0]-constants[20])/constants[31]))))
    algebraic[17] = constants[18]*exp(-((states[0]-constants[20])/constants[33]))
    algebraic[3] = constants[14]*exp(-((states[0]-constants[22])/constants[29]))
    algebraic[16] = constants[17]/(1.00000+exp(-((states[0]-constants[22])/constants[30])))
    algebraic[5] = 1.00000/(1.00000+exp((states[0]-constants[24])/constants[27]))
    algebraic[18] = 8571.00/(0.200000+5.65000*(power((states[0]+constants[48])/100.000, 2.00000)))
    algebraic[6] = constants[16]*((states[1]-constants[21])/(1.00000-exp(-((states[1]-constants[21])/constants[32]))))
    algebraic[19] = constants[19]*exp(-((states[1]-constants[21])/constants[34]))
    algebraic[7] = 1.00000/(1.00000+exp((states[1]-constants[25])/constants[28]))
    algebraic[20] = 1.00000*exp(-((states[1]+40.0000)/25.7500))
    algebraic[9] = constants[15]*((states[1]-constants[20])/(1.00000-exp(-((states[1]-constants[20])/constants[31]))))
    algebraic[22] = constants[18]*exp(-((states[1]-constants[20])/constants[33]))
    algebraic[8] = constants[14]*exp(-((states[1]-constants[22])/constants[29]))
    algebraic[21] = constants[17]/(1.00000+exp(-((states[1]-constants[22])/constants[30])))
    algebraic[10] = 1.00000/(1.00000+exp((states[1]-constants[24])/constants[27]))
    algebraic[23] = 8571.00/(0.200000+5.65000*(power((states[1]+constants[48])/100.000, 2.00000)))
    algebraic[11] = 0.500000*constants[57]*exp((states[1]-constants[59])/(8.00000*constants[58]))
    algebraic[24] = 0.500000*constants[57]*exp((constants[59]-states[1])/(8.00000*constants[58]))
    algebraic[30] = states[0]*((states[3]-states[4]*exp((-1.00000*constants[6]*states[0])/(constants[35]*constants[36])))/(1.00000-exp((-1.00000*constants[6]*states[0])/(constants[35]*constants[36]))))
    algebraic[13] = ((constants[35]*constants[36])/constants[6])*log(states[4]/states[3])
    algebraic[37] = states[4]*exp((-constants[41]*algebraic[13])*(constants[6]/(constants[35]*constants[36])))
    algebraic[38] = constants[40]*((power(algebraic[37], 2.00000))/(constants[42]+power(algebraic[37], 2.00000)))
    algebraic[39] = 1.00000-power(1.00000+(constants[43]*(1.00000+(power(algebraic[37], 2.00000))/constants[42]))/((power(constants[46], 2.00000))*exp((2.00000*(1.00000-constants[41])*states[0]*constants[6])/(constants[35]*constants[36]))), -1.00000)
    algebraic[40] = algebraic[38]*algebraic[39]
    algebraic[41] = algebraic[40]*(custom_piecewise([greater(algebraic[30] , 0.00000), 1.00000 , True, 0.00000]))*(algebraic[30]/50.0000)
    algebraic[42] = (constants[38]*(power(states[8], 4.00000)))*states[9]
    algebraic[43] = algebraic[42]*(algebraic[30]/50.0000)
    algebraic[47] = (1.00000/7.00000)*(exp(states[7]/67.3000)-1.00000)
    algebraic[48] = power(1.00000+0.120000*exp(-0.100000*states[0]*(constants[6]/(constants[35]*constants[36])))+0.0400000*algebraic[47]*exp(-(states[0]*(constants[6]/(constants[35]*constants[36])))), -1.00000)
    algebraic[49] = constants[6]*(constants[47]/((power(1.00000+constants[44]/states[4], 2.00000))*(power(1.00000+constants[45]/states[5], 3.00000))))
    algebraic[50] = algebraic[49]*algebraic[48]
    algebraic[45] = ((constants[39]*(power(states[10], 3.00000)))*states[11])*states[12]
    algebraic[44] = states[0]*((states[5]-states[7]*exp((-1.00000*constants[6]*states[0])/(constants[35]*constants[36])))/(1.00000-exp((-1.00000*constants[6]*states[0])/(constants[35]*constants[36]))))
    algebraic[46] = algebraic[45]*(algebraic[44]/75.0000)
    algebraic[0] = (1000.00/1.00000)*((states[0]-states[1])/constants[2])
    algebraic[26] = 156.500/(5.00000+exp((-constants[6]*algebraic[13])/(constants[35]*constants[36])))
    algebraic[27] = 156.500-5.00000*algebraic[26]
    algebraic[34] = states[0]*((algebraic[26]-algebraic[27]*exp((constants[6]*states[0])/(constants[35]*constants[36])))/(1.00000-exp((constants[6]*states[0])/(constants[35]*constants[36]))))
    algebraic[33] = 1.00000/(1.00000+exp((states[0]-constants[23])/constants[26]))
    algebraic[35] = constants[37]*(power(algebraic[33], 4.00000))
    algebraic[36] = algebraic[35]*(algebraic[34]/45.0000)
    algebraic[32] = custom_piecewise([greater_equal(voi , 0.00000) & less(voi , 0.500000), 150.000 , greater_equal(voi , 50.0000) & less(voi , 50.5000), 150.000 , greater_equal(voi , 100.000) & less(voi , 100.500), 150.000 , greater_equal(voi , 150.000) & less(voi , 150.500), 150.000 , greater_equal(voi , 200.000) & less(voi , 200.500), 150.000 , greater_equal(voi , 250.000) & less(voi , 250.500), 150.000 , greater_equal(voi , 300.000) & less(voi , 300.500), 150.000 , greater_equal(voi , 350.000) & less(voi , 350.500), 150.000 , greater_equal(voi , 400.000) & less(voi , 400.500), 150.000 , True, 0.00000])
    algebraic[51] = algebraic[36]+algebraic[41]+algebraic[43]+algebraic[46]+algebraic[50]+-algebraic[32]
    algebraic[31] = states[1]*((states[3]-states[2]*exp((-1.00000*constants[6]*states[1])/(constants[35]*constants[36])))/(1.00000-exp((-1.00000*constants[6]*states[1])/(constants[35]*constants[36]))))
    algebraic[25] = ((constants[35]*constants[36])/constants[6])*log(states[2]/states[3])
    algebraic[56] = states[2]*exp((-constants[41]*algebraic[25])*(constants[6]/(constants[35]*constants[36])))
    algebraic[57] = constants[40]*((power(algebraic[56], 2.00000))/(constants[42]+power(algebraic[56], 2.00000)))
    algebraic[58] = 1.00000-power(1.00000+(constants[43]*(1.00000+(power(algebraic[56], 2.00000))/constants[42]))/((power(constants[46], 2.00000))*exp((2.00000*(1.00000-constants[41])*states[1]*constants[6])/(constants[35]*constants[36]))), -1.00000)
    algebraic[59] = algebraic[57]*algebraic[58]
    algebraic[60] = constants[50]*algebraic[59]*(algebraic[31]/50.0000)
    algebraic[61] = (constants[38]*(power(states[13], 4.00000)))*states[14]
    algebraic[62] = constants[51]*algebraic[61]*(algebraic[31]/50.0000)
    algebraic[66] = (1.00000/7.00000)*(exp(states[6]/67.3000)-1.00000)
    algebraic[67] = power(1.00000+0.120000*exp(-0.100000*states[1]*(constants[6]/(constants[35]*constants[36])))+0.0400000*algebraic[66]*exp(-(states[1]*(constants[6]/(constants[35]*constants[36])))), -1.00000)
    algebraic[68] = constants[6]*(constants[47]/((power(1.00000+constants[44]/states[2], 2.00000))*(power(1.00000+constants[45]/states[5], 3.00000))))
    algebraic[69] = constants[53]*algebraic[68]*algebraic[67]
    algebraic[64] = ((constants[39]*(power(states[15], 3.00000)))*states[16])*states[17]
    algebraic[63] = states[1]*((states[5]-states[6]*exp((-1.00000*constants[6]*states[1])/(constants[35]*constants[36])))/(1.00000-exp((-1.00000*constants[6]*states[1])/(constants[35]*constants[36]))))
    algebraic[65] = constants[52]*algebraic[64]*(algebraic[63]/75.0000)
    algebraic[28] = 156.500/(5.00000+exp((-constants[6]*algebraic[25])/(constants[35]*constants[36])))
    algebraic[29] = 156.500-5.00000*algebraic[28]
    algebraic[53] = states[1]*((algebraic[28]-algebraic[29]*exp((constants[6]*states[1])/(constants[35]*constants[36])))/(1.00000-exp((constants[6]*states[1])/(constants[35]*constants[36]))))
    algebraic[52] = 1.00000/(1.00000+exp((states[1]-constants[23])/constants[26]))
    algebraic[54] = constants[37]*(power(algebraic[52], 4.00000))
    algebraic[55] = constants[49]*algebraic[54]*(algebraic[53]/45.0000)
    algebraic[70] = algebraic[55]+algebraic[60]+algebraic[62]+algebraic[65]+algebraic[69]
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
        self.C_m = 1.0
        self.gam = 4.8
        self.R_a = 150
        self.tsi = 0.000001
        self.tsi2 = 0.0025
        self.tsi3 = 0.0005
        self.FF = 96485
        self.tau_K = 350
        self.tau_Na = 350
        self.f_T = 0.0032
        self.tau_K2 = 21875
        self.tau_Na2 = 21875
        self.I_K_rest = 1.02
        self.I_Na_rest = -1.29
        self.alpha_h_bar = 0.0081
        self.alpha_m_bar = 0.288
        self.alpha_n_bar = 0.0131
        self.beta_h_bar = 4.38
        self.beta_m_bar = 1.38
        self.beta_n_bar = 0.067
        self.V_m = -46
        self.V_n = -40
        self.V_h = -45
        self.V_a = 70
        self.V_S_inf = -78
        self.V_h_K_inf = -40
        self.A_a = 150
        self.A_S_inf = 5.8
        self.A_h_K_inf = 7.5
        self.K_alpha_h = 14.7
        self.K_beta_h = 9
        self.K_alpha_m = 10
        self.K_alpha_n = 7
        self.K_beta_m = 18
        self.K_beta_n = 40
        self.RR = 8314.41
        self.TT = 293
        self.g_Cl_bar = 19.65
        self.g_K_bar = 64.8
        self.g_Na_bar = 804
        self.G_K = 11.1
        self.del = 0.4
        self.K_K = 950
        self.K_S = 1
        self.K_m_K = 1
        self.K_m_Na = 13
        self.S_i = 10
        self.J_NaK_bar = 0.000621
        self.V_tau = 90
        self.eta_Cl = 0.1
        self.eta_IR = 1.0
        self.eta_DR = 0.45
        self.eta_Na = 0.1
        self.eta_NaK = 0.1
        self.k_L = 0.002
        self.k_Lm = 1000
        self.f = 0.2
        self.alpha1 = 0.2
        self.K = 4.5
        self.Vbar = -20
        self.nu_SR = 4.875
        self.K_SR = 1
        self.L_e = 0.00002
        self.tau_R = 0.75
        self.tau_SR_R = 0.75
        self.L_x = 1.1
        self.R_R = 0.5
        self.k_T_on = 0.04425
        self.k_T_off = 0.115
        self.T_tot = 140
        self.k_P_on = 0.0417
        self.k_P_off = 0.0005
        self.P_tot = 1500
        self.k_Mg_on = 0.000033
        self.k_Mg_off = 0.003
        self.k_Cs_on = 0.000004
        self.k_Cs_off = 0.005
        self.Cs_tot = 31000
        self.k_CATP_on = 0.15
        self.k_CATP_off = 30
        self.k_MATP_on = 0.0015
        self.k_MATP_off = 0.15
        self.tau_ATP = 0.375
        self.tau_Mg = 1.5
        self.k_0_on = 0
        self.k_0_off = 0.15
        self.k_Ca_on = 0.15
        self.k_Ca_off = 0.05
        self.f_o = 1.5
        self.f_p = 15
        self.h_o = 0.24
        self.h_p = 0.18
        self.g_o = 0.12
        self.b_p = 0.00002867
        self.k_p = 0.00000362
        self.A_p = 1
        self.B_p = 0.0001
        self.PP = 6
        self.i2 = 300

    def to_dict(self):
        return {
            "C_m": self.C_m,
            "gam": self.gam,
            "R_a": self.R_a,
            "tsi": self.tsi,
            "tsi2": self.tsi2,
            "tsi3": self.tsi3,
            "FF": self.FF,
            "tau_K": self.tau_K,
            "tau_Na": self.tau_Na,
            "f_T": self.f_T,
            "tau_K2": self.tau_K2,
            "tau_Na2": self.tau_Na2,
            "I_K_rest": self.I_K_rest,
            "I_Na_rest": self.I_Na_rest,
            "alpha_h_bar": self.alpha_h_bar,
            "alpha_m_bar": self.alpha_m_bar,
            "alpha_n_bar": self.alpha_n_bar,
            "beta_h_bar": self.beta_h_bar,
            "beta_m_bar": self.beta_m_bar,
            "beta_n_bar": self.beta_n_bar,
            "V_m": self.V_m,
            "V_n": self.V_n,
            "V_h": self.V_h,
            "V_a": self.V_a,
            "V_S_inf": self.V_S_inf,
            "V_h_K_inf": self.V_h_K_inf,
            "A_a": self.A_a,
            "A_S_inf": self.A_S_inf,
            "A_h_K_inf": self.A_h_K_inf,
            "K_alpha_h": self.K_alpha_h,
            "K_beta_h": self.K_beta_h,
            "K_alpha_m": self.K_alpha_m,
            "K_alpha_n": self.K_alpha_n,
            "K_beta_m": self.K_beta_m,
            "K_beta_n": self.K_beta_n,
            "RR": self.RR,
            "TT": self.TT,
            "g_Cl_bar": self.g_Cl_bar,
            "g_K_bar": self.g_K_bar,
            "g_Na_bar": self.g_Na_bar,
            "G_K": self.G_K,
            "del": self.del,
            "K_K": self.K_K,
            "K_S": self.K_S,
            "K_m_K": self.K_m_K,
            "K_m_Na": self.K_m_Na,
            "S_i": self.S_i,
            "J_NaK_bar": self.J_NaK_bar,
            "V_tau": self.V_tau,
            "eta_Cl": self.eta_Cl,
            "eta_IR": self.eta_IR,
            "eta_DR": self.eta_DR,
            "eta_Na": self.eta_Na,
            "eta_NaK": self.eta_NaK,
            "k_L": self.k_L,
            "k_Lm": self.k_Lm,
            "f": self.f,
            "alpha1": self.alpha1,
            "K": self.K,
            "Vbar": self.Vbar,
            "nu_SR": self.nu_SR,
            "K_SR": self.K_SR,
            "L_e": self.L_e,
            "tau_R": self.tau_R,
            "tau_SR_R": self.tau_SR_R,
            "L_x": self.L_x,
            "R_R": self.R_R,
            "k_T_on": self.k_T_on,
            "k_T_off": self.k_T_off,
            "T_tot": self.T_tot,
            "k_P_on": self.k_P_on,
            "k_P_off": self.k_P_off,
            "P_tot": self.P_tot,
            "k_Mg_on": self.k_Mg_on,
            "k_Mg_off": self.k_Mg_off,
            "k_Cs_on": self.k_Cs_on,
            "k_Cs_off": self.k_Cs_off,
            "Cs_tot": self.Cs_tot,
            "k_CATP_on": self.k_CATP_on,
            "k_CATP_off": self.k_CATP_off,
            "k_MATP_on": self.k_MATP_on,
            "k_MATP_off": self.k_MATP_off,
            "tau_ATP": self.tau_ATP,
            "tau_Mg": self.tau_Mg,
            "k_0_on": self.k_0_on,
            "k_0_off": self.k_0_off,
            "k_Ca_on": self.k_Ca_on,
            "k_Ca_off": self.k_Ca_off,
            "f_o": self.f_o,
            "f_p": self.f_p,
            "h_o": self.h_o,
            "h_p": self.h_p,
            "g_o": self.g_o,
            "b_p": self.b_p,
            "k_p": self.k_p,
            "A_p": self.A_p,
            "B_p": self.B_p,
            "PP": self.PP,
            "i2": self.i2,
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
        y0=[-79.974, -80.2, 5.9, 150.9, 5.9, 12.7, 133, 133, 0.009466, 0.9952, 0.0358, 0.4981, 0.581, 0.009466, 0.9952, 0.0358, 0.4981, 0.581, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0.1, 1500, 0.1, 1500, 25, 615, 615, 811, 811, 16900, 16900, 0.4, 0.4, 7200, 7200, 799.6, 799.6, 1000, 1000, 3, 0.8, 1.2, 3, 0.3, 0.23, 0.23, 0.23, 0.23],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "shorten_ocallaghan_davidson_soboleva_2007"
        self.curve_names = [
            "vS",
            "vT",
            "K_t",
            "K_i",
            "K_e",
            "Na_i",
            "Na_t",
            "Na_e",
            "n",
            "h_K",
            "m",
            "h",
            "S",
            "n_t",
            "h_K_t",
            "m_t",
            "h_t",
            "S_t",
            "O_0",
            "O_1",
            "O_2",
            "O_3",
            "O_4",
            "C_0",
            "C_1",
            "C_2",
            "C_3",
            "C_4",
            "Ca_1",
            "Ca_SR1",
            "Ca_2",
            "Ca_SR2",
            "Ca_T_2",
            "Ca_P1",
            "Ca_P2",
            "Mg_P1",
            "Mg_P2",
            "Ca_Cs1",
            "Ca_Cs2",
            "Ca_ATP1",
            "Ca_ATP2",
            "Mg_ATP1",
            "Mg_ATP2",
            "ATP1",
            "ATP2",
            "Mg1",
            "Mg2",
            "Ca_CaT2",
            "D_0",
            "D_1",
            "D_2",
            "A_1",
            "A_2",
            "P",
            "P_SR",
            "P_C_SR",
        ]
        self.state_names = ['vS', 'vT', 'K_t', 'K_i', 'K_e', 'Na_i', 'Na_t', 'Na_e', 'n', 'h_K', 'm', 'h', 'S', 'n_t', 'h_K_t', 'm_t', 'h_t', 'S_t', 'O_0', 'O_1', 'O_2', 'O_3', 'O_4', 'C_0', 'C_1', 'C_2', 'C_3', 'C_4', 'Ca_1', 'Ca_SR1', 'Ca_2', 'Ca_SR2', 'Ca_T_2', 'Ca_P1', 'Ca_P2', 'Mg_P1', 'Mg_P2', 'Ca_Cs1', 'Ca_Cs2', 'Ca_ATP1', 'Ca_ATP2', 'Mg_ATP1', 'Mg_ATP2', 'ATP1', 'ATP2', 'Mg1', 'Mg2', 'Ca_CaT2', 'D_0', 'D_1', 'D_2', 'A_1', 'A_2', 'P', 'P_SR', 'P_C_SR']
        self.algebraic_names = ['I_T', 'alpha_n', 'h_K_inf', 'alpha_h', 'alpha_m', 'S_inf', 'alpha_n_t', 'h_K_inf_t', 'alpha_h_t', 'alpha_m_t', 'S_inf_t', 'k_C', 'T_0', 'E_K', 'beta_n', 'tau_h_K', 'beta_h', 'beta_m', 'tau_S', 'beta_n_t', 'tau_h_K_t', 'beta_h_t', 'beta_m_t', 'tau_S_t', 'k_Cm', 'E_K_t', 'Cl_i', 'Cl_o', 'Cl_i_t', 'Cl_o_t', 'J_K', 'J_K_t', 'I_HH', 'a', 'J_Cl', 'g_Cl', 'I_Cl', 'K_R', 'g_IR_bar', 'y', 'g_IR', 'I_IR', 'g_DR', 'I_DR', 'J_Na', 'g_Na', 'I_Na', 'sig', 'f1', 'I_NaK_bar', 'I_NaK', 'I_ionic_s', 'a_t', 'J_Cl_t', 'g_Cl_t', 'I_Cl_t', 'K_R_t', 'g_IR_bar_t', 'y_t', 'g_IR_t', 'I_IR_t', 'g_DR_t', 'I_DR_t', 'J_Na_t', 'g_Na_t', 'I_Na_t', 'sig_t', 'f1_t', 'I_NaK_bar_t', 'I_NaK_t', 'I_ionic_t']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 105
        p = self.params

        # direct mapping
        c[0] = p.C_m
        c[1] = p.gam
        c[2] = p.R_a
        c[3] = p.tsi
        c[4] = p.tsi2
        c[5] = p.tsi3
        c[6] = p.FF
        c[7] = p.tau_K
        c[8] = p.tau_Na
        c[9] = p.f_T
        c[10] = p.tau_K2
        c[11] = p.tau_Na2
        c[12] = p.I_K_rest
        c[13] = p.I_Na_rest
        c[14] = p.alpha_h_bar
        c[15] = p.alpha_m_bar
        c[16] = p.alpha_n_bar
        c[17] = p.beta_h_bar
        c[18] = p.beta_m_bar
        c[19] = p.beta_n_bar
        c[20] = p.V_m
        c[21] = p.V_n
        c[22] = p.V_h
        c[23] = p.V_a
        c[24] = p.V_S_inf
        c[25] = p.V_h_K_inf
        c[26] = p.A_a
        c[27] = p.A_S_inf
        c[28] = p.A_h_K_inf
        c[29] = p.K_alpha_h
        c[30] = p.K_beta_h
        c[31] = p.K_alpha_m
        c[32] = p.K_alpha_n
        c[33] = p.K_beta_m
        c[34] = p.K_beta_n
        c[35] = p.RR
        c[36] = p.TT
        c[37] = p.g_Cl_bar
        c[38] = p.g_K_bar
        c[39] = p.g_Na_bar
        c[40] = p.G_K
        c[41] = p.del
        c[42] = p.K_K
        c[43] = p.K_S
        c[44] = p.K_m_K
        c[45] = p.K_m_Na
        c[46] = p.S_i
        c[47] = p.J_NaK_bar
        c[48] = p.V_tau
        c[49] = p.eta_Cl
        c[50] = p.eta_IR
        c[51] = p.eta_DR
        c[52] = p.eta_Na
        c[53] = p.eta_NaK
        c[54] = p.k_L
        c[55] = p.k_Lm
        c[56] = p.f
        c[57] = p.alpha1
        c[58] = p.K
        c[59] = p.Vbar
        c[60] = p.nu_SR
        c[61] = p.K_SR
        c[62] = p.L_e
        c[63] = p.tau_R
        c[64] = p.tau_SR_R
        c[65] = p.L_x
        c[66] = p.R_R
        c[67] = p.k_T_on
        c[68] = p.k_T_off
        c[69] = p.T_tot
        c[70] = p.k_P_on
        c[71] = p.k_P_off
        c[72] = p.P_tot
        c[73] = p.k_Mg_on
        c[74] = p.k_Mg_off
        c[75] = p.k_Cs_on
        c[76] = p.k_Cs_off
        c[77] = p.Cs_tot
        c[78] = p.k_CATP_on
        c[79] = p.k_CATP_off
        c[80] = p.k_MATP_on
        c[81] = p.k_MATP_off
        c[82] = p.tau_ATP
        c[83] = p.tau_Mg
        c[84] = p.k_0_on
        c[85] = p.k_0_off
        c[86] = p.k_Ca_on
        c[87] = p.k_Ca_off
        c[88] = p.f_o
        c[89] = p.f_p
        c[90] = p.h_o
        c[91] = p.h_p
        c[92] = p.g_o
        c[93] = p.b_p
        c[94] = p.k_p
        c[95] = p.A_p
        c[96] = p.B_p
        c[97] = p.PP
        c[98] = p.i2

        # derived constants
        c[99] = 0.950000*c[65]* pi*(power(c[66], 2.00000))
        c[100] = 0.0500000*c[65]* pi*(power(c[66], 2.00000))
        c[101] = 0.0100000*c[99]
        c[102] = 0.990000*c[99]
        c[103] = 0.0100000*c[100]
        c[104] = 0.990000*c[100]

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
