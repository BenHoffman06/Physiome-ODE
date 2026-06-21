# Size of variable arrays:
sizeAlgebraic = 115
sizeStates = 30
sizeConstants = 83
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (millisecond)"
    legend_states[0] = "V in component membrane (millivolt)"
    legend_algebraic[0] = "i_stim in component membrane (microA_per_microF)"
    legend_algebraic[92] = "i_tot in component membrane (microA_per_microF)"
    legend_algebraic[57] = "i_Na in component i_Na (microA_per_microF)"
    legend_algebraic[58] = "i_Na_L in component i_Na_L (microA_per_microF)"
    legend_algebraic[60] = "i_Ca_L in component i_Ca_L (microA_per_microF)"
    legend_algebraic[64] = "i_Ca_T in component i_Ca_T (microA_per_microF)"
    legend_algebraic[67] = "i_to_1 in component i_to_1 (microA_per_microF)"
    legend_algebraic[79] = "i_to_2 in component i_to_2 (microA_per_microF)"
    legend_algebraic[69] = "i_Kr in component i_Kr (microA_per_microF)"
    legend_algebraic[71] = "i_Ks in component i_Ks (microA_per_microF)"
    legend_algebraic[75] = "i_K1 in component i_K1 (microA_per_microF)"
    legend_algebraic[82] = "i_NaCa in component i_NaCa (microA_per_microF)"
    legend_algebraic[84] = "i_NaK in component i_NaK (microA_per_microF)"
    legend_algebraic[88] = "i_Na_b in component background_currents (microA_per_microF)"
    legend_algebraic[91] = "i_Ca_b in component background_currents (microA_per_microF)"
    legend_algebraic[89] = "i_K_b in component background_currents (microA_per_microF)"
    legend_algebraic[90] = "i_Cl_b in component background_currents (microA_per_microF)"
    legend_algebraic[85] = "i_Ca_p in component i_Ca_p (microA_per_microF)"
    legend_algebraic[77] = "i_K_p in component i_K_p (microA_per_microF)"
    legend_constants[0] = "stim_start in component membrane (millisecond)"
    legend_constants[1] = "stim_end in component membrane (millisecond)"
    legend_constants[2] = "stim_amplitude in component membrane (microA_per_microF)"
    legend_algebraic[19] = "E_Na in component equilibrium_potentials (millivolt)"
    legend_algebraic[36] = "E_K in component equilibrium_potentials (millivolt)"
    legend_algebraic[1] = "E_Ca in component equilibrium_potentials (millivolt)"
    legend_algebraic[46] = "E_Cl in component equilibrium_potentials (millivolt)"
    legend_algebraic[56] = "E_Ks in component equilibrium_potentials (millivolt)"
    legend_constants[3] = "r_NaK in component equilibrium_potentials (dimensionless)"
    legend_states[1] = "Na_i in component intracellular_ion_concentrations (millimolar)"
    legend_constants[4] = "Na_o in component model_parameters (millimolar)"
    legend_states[2] = "Ca_i in component Ca_i (millimolar)"
    legend_constants[5] = "Ca_o in component model_parameters (millimolar)"
    legend_states[3] = "K_i in component intracellular_ion_concentrations (millimolar)"
    legend_constants[6] = "K_o in component model_parameters (millimolar)"
    legend_states[4] = "Cl_i in component intracellular_ion_concentrations (millimolar)"
    legend_constants[7] = "Cl_o in component model_parameters (millimolar)"
    legend_constants[8] = "R in component model_parameters (joule_per_kilomole_kelvin)"
    legend_constants[9] = "F in component model_parameters (coulomb_per_mole)"
    legend_constants[10] = "T in component model_parameters (kelvin)"
    legend_constants[11] = "g_Na in component i_Na (milliS_per_microF)"
    legend_states[5] = "m in component i_Na_m_gate (dimensionless)"
    legend_states[6] = "h in component i_Na_h_gate (dimensionless)"
    legend_states[7] = "j in component i_Na_j_gate (dimensionless)"
    legend_algebraic[47] = "tau_m in component i_Na_m_gate (millisecond)"
    legend_algebraic[37] = "m_infinity in component i_Na_m_gate (dimensionless)"
    legend_algebraic[2] = "alpha_m in component i_Na_m_gate (per_millisecond)"
    legend_algebraic[20] = "beta_m in component i_Na_m_gate (per_millisecond)"
    legend_algebraic[48] = "tau_h in component i_Na_h_gate (millisecond)"
    legend_algebraic[38] = "h_infinity in component i_Na_h_gate (dimensionless)"
    legend_algebraic[3] = "alpha_h in component i_Na_h_gate (per_millisecond)"
    legend_algebraic[21] = "beta_h in component i_Na_h_gate (per_millisecond)"
    legend_algebraic[49] = "tau_j in component i_Na_j_gate (millisecond)"
    legend_algebraic[39] = "j_infinity in component i_Na_j_gate (dimensionless)"
    legend_algebraic[4] = "alpha_j in component i_Na_j_gate (per_millisecond)"
    legend_algebraic[22] = "beta_j in component i_Na_j_gate (per_millisecond)"
    legend_constants[12] = "g_Na_L in component i_Na_L (milliS_per_microF)"
    legend_states[8] = "m_L in component i_Na_L_m_L_gate (dimensionless)"
    legend_states[9] = "h_L in component i_Na_L_h_L_gate (dimensionless)"
    legend_algebraic[50] = "tau_m_L in component i_Na_L_m_L_gate (millisecond)"
    legend_algebraic[40] = "m_L_infinity in component i_Na_L_m_L_gate (dimensionless)"
    legend_algebraic[5] = "alpha_m_L in component i_Na_L_m_L_gate (per_millisecond)"
    legend_algebraic[23] = "beta_m_L in component i_Na_L_m_L_gate (per_millisecond)"
    legend_algebraic[24] = "tau_h_L in component i_Na_L_h_L_gate (millisecond)"
    legend_algebraic[6] = "h_L_infinity in component i_Na_L_h_L_gate (dimensionless)"
    legend_constants[13] = "g_Ca_L in component i_Ca_L (dimensionless)"
    legend_algebraic[59] = "i_Ca_L_max in component i_Ca_L (microA_per_microF)"
    legend_constants[14] = "p_Ca in component i_Ca_L (cm_per_second)"
    legend_constants[15] = "z_Ca in component model_parameters (dimensionless)"
    legend_constants[16] = "gamma_Cai in component model_parameters (dimensionless)"
    legend_constants[17] = "gamma_Cao in component model_parameters (dimensionless)"
    legend_states[10] = "Ca_r in component Ca_r (millimolar)"
    legend_algebraic[97] = "Ca_MK_act in component Ca_MK_act (dimensionless)"
    legend_constants[18] = "km_Ca_MK in component Ca_MK_act (millimolar)"
    legend_states[11] = "d in component i_Ca_L_d_gate (dimensionless)"
    legend_states[12] = "f in component i_Ca_L_f_gate (dimensionless)"
    legend_states[13] = "f2 in component i_Ca_L_f2_gate (dimensionless)"
    legend_states[14] = "f_Ca in component i_Ca_L_f_Ca_gate (dimensionless)"
    legend_states[15] = "f_Ca2 in component i_Ca_L_f_Ca2_gate (dimensionless)"
    legend_constants[19] = "Cm in component model_parameters (microF_per_cm2)"
    legend_algebraic[7] = "d_infinity in component i_Ca_L_d_gate (dimensionless)"
    legend_algebraic[25] = "tau_d in component i_Ca_L_d_gate (millisecond)"
    legend_algebraic[8] = "f_infinity in component i_Ca_L_f_gate (dimensionless)"
    legend_algebraic[26] = "tau_f in component i_Ca_L_f_gate (millisecond)"
    legend_algebraic[9] = "f2_infinity in component i_Ca_L_f2_gate (dimensionless)"
    legend_algebraic[27] = "tau_f2 in component i_Ca_L_f2_gate (millisecond)"
    legend_algebraic[61] = "f_Ca_infinity in component i_Ca_L_f_Ca_gate (dimensionless)"
    legend_algebraic[98] = "tau_f_Ca in component i_Ca_L_f_Ca_gate (millisecond)"
    legend_algebraic[62] = "f_Ca2_infinity in component i_Ca_L_f_Ca2_gate (dimensionless)"
    legend_algebraic[65] = "tau_f_Ca2 in component i_Ca_L_f_Ca2_gate (millisecond)"
    legend_constants[20] = "g_Ca_T in component i_Ca_T (milliS_per_microF)"
    legend_states[16] = "b in component i_Ca_T_b_gate (dimensionless)"
    legend_states[17] = "g in component i_Ca_T_g_gate (dimensionless)"
    legend_algebraic[51] = "tau_b in component i_Ca_T_b_gate (millisecond)"
    legend_algebraic[41] = "b_infinity in component i_Ca_T_b_gate (dimensionless)"
    legend_algebraic[10] = "alpha_b in component i_Ca_T_b_gate (per_millisecond)"
    legend_algebraic[28] = "beta_b in component i_Ca_T_b_gate (per_millisecond)"
    legend_algebraic[52] = "tau_g in component i_Ca_T_g_gate (millisecond)"
    legend_algebraic[42] = "g_infinity in component i_Ca_T_g_gate (dimensionless)"
    legend_algebraic[11] = "alpha_g in component i_Ca_T_g_gate (per_millisecond)"
    legend_algebraic[29] = "beta_g in component i_Ca_T_g_gate (per_millisecond)"
    legend_constants[21] = "g_to_1 in component i_to_1 (milliS_per_microF)"
    legend_states[18] = "a in component i_to_1_a_gate (dimensionless)"
    legend_states[19] = "i in component i_to_1_i_gate (dimensionless)"
    legend_states[20] = "i2 in component i_to_1_i2_gate (dimensionless)"
    legend_algebraic[12] = "alpha_a in component i_to_1_a_gate (per_millisecond)"
    legend_algebraic[30] = "beta_a in component i_to_1_a_gate (per_millisecond)"
    legend_algebraic[43] = "tau_a in component i_to_1_a_gate (millisecond)"
    legend_algebraic[53] = "a_infinity in component i_to_1_a_gate (dimensionless)"
    legend_algebraic[13] = "alpha_i in component i_to_1_i_gate (per_millisecond)"
    legend_algebraic[31] = "beta_i in component i_to_1_i_gate (per_millisecond)"
    legend_algebraic[44] = "tau_i in component i_to_1_i_gate (millisecond)"
    legend_algebraic[54] = "i_infinity in component i_to_1_i_gate (dimensionless)"
    legend_algebraic[14] = "alpha_i2 in component i_to_1_i2_gate (per_millisecond)"
    legend_algebraic[32] = "beta_i2 in component i_to_1_i2_gate (per_millisecond)"
    legend_algebraic[45] = "tau_i2 in component i_to_1_i2_gate (millisecond)"
    legend_algebraic[55] = "i2_infinity in component i_to_1_i2_gate (dimensionless)"
    legend_constants[74] = "g_Kr in component i_Kr (milliS_per_microF)"
    legend_algebraic[68] = "rr_infinity in component i_Kr (dimensionless)"
    legend_states[21] = "xr in component i_Kr_xr_gate (dimensionless)"
    legend_algebraic[15] = "tau_xr in component i_Kr_xr_gate (millisecond)"
    legend_algebraic[33] = "xr_infinity in component i_Kr_xr_gate (dimensionless)"
    legend_algebraic[70] = "g_Ks in component i_Ks (milliS_per_microF)"
    legend_states[22] = "xs1 in component i_Ks_xs1_gate (dimensionless)"
    legend_states[23] = "xs2 in component i_Ks_xs2_gate (dimensionless)"
    legend_algebraic[16] = "tau_xs1 in component i_Ks_xs1_gate (millisecond)"
    legend_algebraic[34] = "xs1_infinity in component i_Ks_xs1_gate (dimensionless)"
    legend_algebraic[17] = "tau_xs2 in component i_Ks_xs2_gate (millisecond)"
    legend_algebraic[35] = "xs2_infinity in component i_Ks_xs2_gate (dimensionless)"
    legend_constants[75] = "g_K1 in component i_K1 (milliS_per_microF)"
    legend_algebraic[74] = "xK1 in component i_K1_xK1_gate (dimensionless)"
    legend_algebraic[73] = "alpha_xK1 in component i_K1_xK1_gate (dimensionless)"
    legend_algebraic[72] = "beta_xK1 in component i_K1_xK1_gate (dimensionless)"
    legend_constants[22] = "g_K_p in component i_K_p (milliS_per_microF)"
    legend_algebraic[76] = "kp in component i_K_p (dimensionless)"
    legend_constants[23] = "p_Cl in component i_to_2 (cm_per_second)"
    legend_constants[24] = "z_Cl in component i_to_2 (dimensionless)"
    legend_algebraic[78] = "i_to_2_max in component i_to_2 (microA_per_microF)"
    legend_states[24] = "a in component i_to_2_a_gate (dimensionless)"
    legend_algebraic[18] = "a_infinity in component i_to_2_a_gate (dimensionless)"
    legend_constants[76] = "tau_a in component i_to_2_a_gate (millisecond)"
    legend_constants[25] = "km_to_2 in component i_to_2_a_gate (millimolar)"
    legend_constants[26] = "X_NaCa in component i_NaCa (dimensionless)"
    legend_constants[27] = "i_NaCa_max in component i_NaCa (microA_per_microF)"
    legend_constants[28] = "km_Na_i_1 in component i_NaCa (millimolar)"
    legend_constants[29] = "km_Na_o in component i_NaCa (millimolar)"
    legend_constants[30] = "km_Ca_i in component i_NaCa (millimolar)"
    legend_constants[31] = "km_Ca_o in component i_NaCa (millimolar)"
    legend_constants[32] = "km_Ca_act in component i_NaCa (millimolar)"
    legend_constants[33] = "k_sat in component i_NaCa (dimensionless)"
    legend_algebraic[80] = "dNaCa_1 in component i_NaCa (millimolar4)"
    legend_algebraic[81] = "dNaCa_2 in component i_NaCa (millimolar4)"
    legend_constants[34] = "g_NaK in component i_NaK (microA_per_microF)"
    legend_constants[35] = "km_Na_i_2 in component i_NaK (millimolar)"
    legend_constants[36] = "km_K_o in component i_NaK (millimolar)"
    legend_algebraic[83] = "f_NaK in component i_NaK (dimensionless)"
    legend_constants[77] = "sigma in component i_NaK (dimensionless)"
    legend_constants[37] = "i_Ca_p_max in component i_Ca_p (microA_per_microF)"
    legend_constants[38] = "km_Ca_p in component i_Ca_p (millimolar)"
    legend_algebraic[86] = "CT_K_Cl in component CT_K_Cl (millimolar_per_millisecond)"
    legend_constants[39] = "CT_K_Cl_max in component CT_K_Cl (millimolar_per_millisecond)"
    legend_algebraic[87] = "CT_Na_Cl in component CT_Na_Cl (millimolar_per_millisecond)"
    legend_constants[40] = "CT_Na_Cl_max in component CT_Na_Cl (millimolar_per_millisecond)"
    legend_constants[41] = "g_Na_b in component background_currents (milliS_per_microF)"
    legend_constants[42] = "g_K_b in component background_currents (milliS_per_microF)"
    legend_constants[43] = "p_Ca_b in component background_currents (cm_per_second)"
    legend_constants[44] = "g_Cl_b in component background_currents (milliS_per_microF)"
    legend_constants[79] = "Vol_myo in component model_parameters (microlitre)"
    legend_constants[78] = "a_cap in component model_parameters (cm2)"
    legend_constants[45] = "km_TRPN in component Ca_i (millimolar)"
    legend_constants[46] = "km_CMDN in component Ca_i (millimolar)"
    legend_constants[47] = "TRPN_max in component Ca_i (millimolar)"
    legend_constants[48] = "CMDN_max in component Ca_i (millimolar)"
    legend_algebraic[94] = "TRPN in component Ca_i (dimensionless)"
    legend_algebraic[93] = "CMDN in component Ca_i (dimensionless)"
    legend_algebraic[95] = "b_myo in component Ca_i (dimensionless)"
    legend_constants[80] = "Vol_nsr in component model_parameters (microlitre)"
    legend_constants[82] = "Vol_ss in component model_parameters (microlitre)"
    legend_algebraic[113] = "q_up in component q_up (millimolar_per_millisecond)"
    legend_algebraic[110] = "q_leak in component q_leak (millimolar_per_millisecond)"
    legend_algebraic[99] = "q_diff in component Ca_r (millimolar_per_millisecond)"
    legend_states[25] = "Ca_MK_trap in component Ca_MK_act (dimensionless)"
    legend_algebraic[96] = "Ca_MK_bound in component Ca_MK_act (dimensionless)"
    legend_constants[49] = "alpha_Ca_MK in component Ca_MK_act (per_millisecond)"
    legend_constants[50] = "beta_Ca_MK in component Ca_MK_act (per_millisecond)"
    legend_constants[51] = "Ca_MK_0 in component Ca_MK_act (dimensionless)"
    legend_states[26] = "Ca_NSR in component Ca_NSR (millimolar)"
    legend_constants[81] = "Vol_jsr in component model_parameters (microlitre)"
    legend_algebraic[114] = "q_tr in component q_tr (millimolar_per_millisecond)"
    legend_states[27] = "Ca_JSR in component Ca_JSR (millimolar)"
    legend_constants[52] = "CSQN_max in component Ca_JSR (millimolar)"
    legend_constants[53] = "km_CSQN in component Ca_JSR (millimolar)"
    legend_algebraic[109] = "q_rel in component q_rel (millimolar_per_millisecond)"
    legend_constants[54] = "km_b_SR in component Ca_r (millimolar)"
    legend_constants[55] = "km_b_SL in component Ca_r (millimolar)"
    legend_constants[56] = "b_SR_max in component Ca_r (millimolar)"
    legend_constants[57] = "b_SL_max in component Ca_r (millimolar)"
    legend_constants[58] = "tau_ss in component Ca_r (millisecond)"
    legend_algebraic[103] = "b_SR in component Ca_r (dimensionless)"
    legend_algebraic[101] = "b_SL in component Ca_r (dimensionless)"
    legend_algebraic[105] = "Ca_r_tot in component Ca_r (dimensionless)"
    legend_algebraic[108] = "g_rel in component q_rel (per_millisecond)"
    legend_algebraic[107] = "vg in component q_rel (dimensionless)"
    legend_states[28] = "ri in component q_rel_ri_gate (dimensionless)"
    legend_states[29] = "ro in component q_rel_ro_gate (dimensionless)"
    legend_algebraic[106] = "tau_ri in component q_rel_ri_gate (millisecond)"
    legend_algebraic[104] = "tau_Ca_MK in component q_rel_ri_gate (millisecond)"
    legend_constants[59] = "tau_Ca_MK_max in component q_rel_ri_gate (millisecond)"
    legend_algebraic[100] = "Ca_fac in component q_rel_ri_gate (millimolar)"
    legend_algebraic[102] = "ri_infinity in component q_rel_ri_gate (dimensionless)"
    legend_constants[60] = "tau_ro in component q_rel_ro_gate (millisecond)"
    legend_algebraic[66] = "ro_infinity in component q_rel_ro_gate (dimensionless)"
    legend_algebraic[63] = "ro_infinity_JSR in component q_rel_ro_gate (dimensionless)"
    legend_constants[61] = "q_leak_max in component q_leak (millimolar_per_millisecond)"
    legend_constants[62] = "NSR_max in component q_leak (millimolar)"
    legend_constants[63] = "X_q_up in component q_up (dimensionless)"
    legend_constants[64] = "q_up_max in component q_up (millimolar_per_millisecond)"
    legend_algebraic[111] = "dq_up_Ca_MK in component q_up (dimensionless)"
    legend_constants[65] = "dq_up_Ca_MK_max in component q_up (dimensionless)"
    legend_algebraic[112] = "dkm_plb in component q_up (millimolar)"
    legend_constants[66] = "dkm_plb_max in component q_up (millimolar)"
    legend_constants[67] = "km_up in component q_up (millimolar)"
    legend_constants[68] = "tau_tr in component q_tr (millisecond)"
    legend_constants[69] = "Vol_cell in component model_parameters (microlitre)"
    legend_constants[73] = "a_geo in component model_parameters (cm2)"
    legend_constants[70] = "radius in component model_parameters (cm)"
    legend_constants[71] = "length in component model_parameters (cm)"
    legend_constants[72] = "rcg in component model_parameters (dimensionless)"
    legend_rates[0] = "d/dt V in component membrane (millivolt)"
    legend_rates[5] = "d/dt m in component i_Na_m_gate (dimensionless)"
    legend_rates[6] = "d/dt h in component i_Na_h_gate (dimensionless)"
    legend_rates[7] = "d/dt j in component i_Na_j_gate (dimensionless)"
    legend_rates[8] = "d/dt m_L in component i_Na_L_m_L_gate (dimensionless)"
    legend_rates[9] = "d/dt h_L in component i_Na_L_h_L_gate (dimensionless)"
    legend_rates[11] = "d/dt d in component i_Ca_L_d_gate (dimensionless)"
    legend_rates[12] = "d/dt f in component i_Ca_L_f_gate (dimensionless)"
    legend_rates[13] = "d/dt f2 in component i_Ca_L_f2_gate (dimensionless)"
    legend_rates[14] = "d/dt f_Ca in component i_Ca_L_f_Ca_gate (dimensionless)"
    legend_rates[15] = "d/dt f_Ca2 in component i_Ca_L_f_Ca2_gate (dimensionless)"
    legend_rates[16] = "d/dt b in component i_Ca_T_b_gate (dimensionless)"
    legend_rates[17] = "d/dt g in component i_Ca_T_g_gate (dimensionless)"
    legend_rates[18] = "d/dt a in component i_to_1_a_gate (dimensionless)"
    legend_rates[19] = "d/dt i in component i_to_1_i_gate (dimensionless)"
    legend_rates[20] = "d/dt i2 in component i_to_1_i2_gate (dimensionless)"
    legend_rates[21] = "d/dt xr in component i_Kr_xr_gate (dimensionless)"
    legend_rates[22] = "d/dt xs1 in component i_Ks_xs1_gate (dimensionless)"
    legend_rates[23] = "d/dt xs2 in component i_Ks_xs2_gate (dimensionless)"
    legend_rates[24] = "d/dt a in component i_to_2_a_gate (dimensionless)"
    legend_rates[1] = "d/dt Na_i in component intracellular_ion_concentrations (millimolar)"
    legend_rates[3] = "d/dt K_i in component intracellular_ion_concentrations (millimolar)"
    legend_rates[4] = "d/dt Cl_i in component intracellular_ion_concentrations (millimolar)"
    legend_rates[2] = "d/dt Ca_i in component Ca_i (millimolar)"
    legend_rates[25] = "d/dt Ca_MK_trap in component Ca_MK_act (dimensionless)"
    legend_rates[26] = "d/dt Ca_NSR in component Ca_NSR (millimolar)"
    legend_rates[27] = "d/dt Ca_JSR in component Ca_JSR (millimolar)"
    legend_rates[10] = "d/dt Ca_r in component Ca_r (millimolar)"
    legend_rates[28] = "d/dt ri in component q_rel_ri_gate (dimensionless)"
    legend_rates[29] = "d/dt ro in component q_rel_ro_gate (dimensionless)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = -83.43812846286808
    constants[0] = 0
    constants[1] = 1
    constants[2] = -80
    constants[3] = 0.01833
    states[1] = 9.927155552932733
    constants[4] = 140
    states[2] = 0.00022355433459434943
    constants[5] = 1.8
    states[3] = 141.9670801746057
    constants[6] = 5.4
    states[4] = 18.904682470140408
    constants[7] = 100
    constants[8] = 8314
    constants[9] = 96485
    constants[10] = 310
    constants[11] = 8
    states[5] = 0.002003390432234504
    states[6] = 0.9786390933308567
    states[7] = 0.09866447258167589
    constants[12] = 0.037375
    states[8] = 0.002003390432234504
    states[9] = 0.8946968372659203
    constants[13] = 0.3392328
    constants[14] = 0.000243
    constants[15] = 2
    constants[16] = 1
    constants[17] = 0.341
    states[10] = 0.00022418117117903934
    constants[18] = 0.15
    states[11] = 0.000002322223865147363
    states[12] = 0.9985607329462358
    states[13] = 0.8173435436674658
    states[14] = 0.9610551285529658
    states[15] = 0.868690796671854
    constants[19] = 1
    constants[20] = 0.13
    states[16] = 0.0002563937630984438
    states[17] = 0.9720432601848331
    constants[21] = 0.14135944
    states[18] = 0.0004238729429342389
    states[19] = 0.9990935802459496
    states[20] = 0.9777368439681764
    states[21] = 0.07084939408222911
    states[22] = 0.0011737654433043125
    states[23] = 0.001179442867470093
    constants[22] = 0.00276
    constants[23] = 0.0000004
    constants[24] = -1
    states[24] = 0.0014909437525000811
    constants[25] = 0.1502
    constants[26] = 0.4
    constants[27] = 4.5
    constants[28] = 12.3
    constants[29] = 87.5
    constants[30] = 0.0036
    constants[31] = 1.3
    constants[32] = 0.000125
    constants[33] = 0.27
    constants[34] = 0.61875
    constants[35] = 10
    constants[36] = 1.5
    constants[37] = 0.0575
    constants[38] = 0.0005
    constants[39] = 7.0756e-6
    constants[40] = 9.8443e-6
    constants[41] = 0.0025
    constants[42] = 0.005
    constants[43] = 1.995084e-7
    constants[44] = 0.000225
    constants[45] = 0.0005
    constants[46] = 0.00238
    constants[47] = 0.07
    constants[48] = 0.05
    states[25] = 0.000008789168284782809
    constants[49] = 0.05
    constants[50] = 0.00068
    constants[51] = 0.05
    states[26] = 1.2132524695849454
    states[27] = 1.1433050636518596
    constants[52] = 10
    constants[53] = 0.8
    constants[54] = 0.00087
    constants[55] = 0.0087
    constants[56] = 0.047
    constants[57] = 1.124
    constants[58] = 0.2
    states[28] = 0.7802870066567904
    states[29] = 1.2785734760674763e-9
    constants[59] = 10
    constants[60] = 3
    constants[61] = 0.004375
    constants[62] = 15
    constants[63] = 0.5
    constants[64] = 0.004375
    constants[65] = 0.75
    constants[66] = 0.00017
    constants[67] = 0.00092
    constants[68] = 120
    constants[69] = 0.3454
    constants[70] = 0.0011
    constants[71] = 0.01
    constants[72] = 2
    constants[73] = 2.00000*3.14000*(power(constants[70], 2.00000))+2.00000*3.14000*constants[70]*constants[71]
    constants[74] = 0.0400085*(power(constants[6]/5.40000, 1.0/2))
    constants[75] = 0.250000*(power(constants[6]/5.40000, 1.0/2))
    constants[76] = 1.00000
    constants[77] = (1.00000/7.00000)*(exp(constants[4]/67.3000)-1.00000)
    constants[78] = constants[72]*constants[73]
    constants[79] = constants[69]*0.680000
    constants[80] = constants[69]*0.0552000
    constants[81] = constants[69]*0.00480000
    constants[82] = constants[69]*0.0200000
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[18] = 1.00000/(1.00000+constants[25]/states[10])
    rates[24] = (algebraic[18]-states[24])/constants[76]
    algebraic[24] = 175.000+125.000/(1.00000+exp(-(states[0]+25.0000)/6.00000))
    algebraic[6] = 1.00000/(1.00000+exp((states[0]+69.0000)/6.10000))
    rates[9] = (algebraic[6]-states[9])/algebraic[24]
    algebraic[7] = 1.00000/(1.00000+exp(-(states[0]-4.00000)/6.74000))
    algebraic[25] = 0.590000+(0.800000*exp(0.0520000*(states[0]+13.0000)))/(1.00000+exp(0.132000*(states[0]+13.0000)))
    rates[11] = (algebraic[7]-states[11])/algebraic[25]
    algebraic[8] = 1.00000/(1.00000+exp((states[0]+18.0000)/10.0000))
    algebraic[26] = 4.00000+0.00500000*(power(states[0]-2.50000, 2.00000))
    rates[12] = (algebraic[8]-states[12])/algebraic[26]
    algebraic[9] = 1.00000/(1.00000+exp((states[0]+18.0000)/10.0000))
    algebraic[27] = 38.0000+0.0700000*(power(states[0]-18.6000, 2.00000))
    rates[13] = (algebraic[9]-states[13])/algebraic[27]
    algebraic[15] = 900.000/(1.00000+exp(states[0]/5.00000))+100.000
    algebraic[33] = 1.00000/(1.00000+exp(-(states[0]+0.0850000)/12.2500))
    rates[21] = (algebraic[33]-states[21])/algebraic[15]
    algebraic[16] = 1.00000/((7.61000e-05*(states[0]+44.6000))/(1.00000-exp(-9.97000*(states[0]+44.6000)))+(0.000360000*(states[0]-0.550000))/(exp(0.128000*(states[0]-0.550000))-1.00000))
    algebraic[34] = 1.00000/(1.00000+exp(-(states[0]-9.00000)/13.7000))
    rates[22] = (algebraic[34]-states[22])/algebraic[16]
    algebraic[17] = (2.00000*1.00000)/((7.61000e-05*(states[0]+44.6000))/(1.00000-exp(-9.97000*(states[0]+44.6000)))+(0.000360000*(states[0]-0.550000))/(exp(0.128000*(states[0]-0.550000))-1.00000))
    algebraic[35] = 1.00000/(1.00000+exp(-(states[0]-9.00000)/13.7000))
    rates[23] = (algebraic[35]-states[23])/algebraic[17]
    algebraic[2] = (0.320000*(states[0]+47.1300))/(1.00000-exp(-0.100000*(states[0]+47.1300)))
    algebraic[20] = 0.0800000*exp(-states[0]/11.0000)
    algebraic[47] = 1.00000/(algebraic[2]+algebraic[20])
    algebraic[37] = algebraic[2]/(algebraic[2]+algebraic[20])
    rates[5] = (algebraic[37]-states[5])/algebraic[47]
    algebraic[3] = custom_piecewise([less(states[0] , -40.0000), 0.135000*exp((states[0]+80.0000)/-6.80000) , True, 0.00000])
    algebraic[21] = custom_piecewise([less(states[0] , -40.0000), 3.56000*exp(0.0790000*states[0])+310000.*exp(0.350000*states[0]) , True, 1.00000/(0.130000*(1.00000+exp((states[0]+10.6600)/-11.1000)))])
    algebraic[48] = 1.00000/(algebraic[3]+algebraic[21])
    algebraic[38] = algebraic[3]/(algebraic[3]+algebraic[21])
    rates[6] = (algebraic[38]-states[6])/algebraic[48]
    algebraic[4] = custom_piecewise([less(states[0] , -40.0000), ((-127140.*exp(0.244400*states[0])-3.47400e-05*exp(-0.0439100*states[0]))*(states[0]+37.7800))/(1.00000+exp(0.311000*(states[0]+79.2300))) , True, 0.00000])
    algebraic[22] = custom_piecewise([less(states[0] , -40.0000), (0.121200*exp(-0.0105200*states[0]))/(1.00000+exp(-0.137800*(states[0]+40.1400))) , True, (0.300000*exp(-2.53500e-07*states[0]))/(1.00000+exp(-0.100000*(states[0]+32.0000)))])
    algebraic[49] = 0.100000/(algebraic[4]+algebraic[22])
    algebraic[39] = (0.100000*algebraic[4])/(algebraic[4]+algebraic[22])
    rates[7] = (algebraic[39]-states[7])/algebraic[49]
    algebraic[5] = (0.320000*(states[0]+47.1300))/(1.00000-exp(-0.100000*(states[0]+47.1300)))
    algebraic[23] = 0.0800000*exp(-states[0]/11.0000)
    algebraic[50] = 1.00000/(algebraic[5]+algebraic[23])
    algebraic[40] = algebraic[5]/(algebraic[5]+algebraic[23])
    rates[8] = (algebraic[40]-states[8])/algebraic[50]
    algebraic[10] = 1.06800*exp((states[0]+16.3000)/30.0000)
    algebraic[28] = 1.06800*exp(-(states[0]+16.3000)/30.0000)
    algebraic[51] = 1.00000/(algebraic[10]+algebraic[28])
    algebraic[41] = 1.00000/(1.00000+exp(-(states[0]+33.0000)/6.10000))
    rates[16] = (algebraic[41]-states[16])/algebraic[51]
    algebraic[11] = 0.0150000*exp(-(states[0]+71.7000)/83.3000)
    algebraic[29] = 0.0150000*exp((states[0]+71.7000)/15.4000)
    algebraic[52] = 1.00000/(algebraic[11]+algebraic[29])
    algebraic[42] = 1.00000/(1.00000+exp((states[0]+60.0000)/6.60000))
    rates[17] = (algebraic[42]-states[17])/algebraic[52]
    algebraic[12] = (25.0000*exp((states[0]-76.0000)/20.0000))/(1.00000+exp((states[0]-76.0000)/20.0000))
    algebraic[30] = (25.0000*exp(-(states[0]+54.0000)/20.0000))/(1.00000+exp(-(states[0]+54.0000)/20.0000))
    algebraic[43] = 1.00000/(algebraic[12]+algebraic[30])
    algebraic[53] = algebraic[12]/(algebraic[12]+algebraic[30])
    rates[18] = (algebraic[53]-states[18])/algebraic[43]
    algebraic[44] = 6.00000+5.00000/(1.00000+exp((states[0]-16.5000)/10.0000))
    algebraic[13] = 0.0300000/(1.00000+exp((states[0]+25.0000)/15.0000))
    algebraic[31] = (0.100000*exp((states[0]-40.0000)/15.0000))/(1.00000+exp((states[0]-40.0000)/15.0000))
    algebraic[54] = algebraic[13]/(algebraic[13]+algebraic[31])
    rates[19] = (algebraic[54]-states[19])/algebraic[44]
    algebraic[45] = 21.5000+30.0000/(1.00000+exp((states[0]-25.0000)/10.0000))
    algebraic[14] = 0.00442000/(1.00000+exp((states[0]+26.0000)/15.0000))
    algebraic[32] = (0.0500000*exp((states[0]-10.0000)/15.0000))/(1.00000+exp((states[0]-10.0000)/15.0000))
    algebraic[55] = algebraic[14]/(algebraic[14]+algebraic[32])
    rates[20] = (algebraic[55]-states[20])/algebraic[45]
    algebraic[59] = (((((1.00000*constants[14])/constants[19])*(power(constants[15], 2.00000))*(states[0]-15.0000)*(power(constants[9], 2.00000)))/(constants[8]*constants[10]))*(constants[16]*states[10]*exp((constants[15]*constants[9]*(states[0]-15.0000))/(constants[8]*constants[10]))-constants[17]*constants[5]))/(exp((constants[15]*constants[9]*(states[0]-15.0000))/(constants[8]*constants[10]))-1.00000)
    algebraic[60] = constants[13]*states[11]*states[12]*states[13]*states[14]*states[15]*algebraic[59]
    algebraic[62] = 1.00000/(1.00000-algebraic[60]/0.0100000)
    algebraic[65] = 125.000+300.000/(1.00000+exp((-algebraic[60]-0.175000)/0.0400000))
    rates[15] = (algebraic[62]-states[15])/algebraic[65]
    algebraic[63] = (power(states[27], 1.90000))/(power(states[27], 1.90000)+power((49.2800*states[10])/(states[10]+0.00280000), 1.90000))
    algebraic[66] = (algebraic[63]*(power(algebraic[60], 2.00000)))/(power(algebraic[60], 2.00000)+1.00000)
    rates[29] = (algebraic[66]-states[29])/constants[60]
    algebraic[19] = ((constants[8]*constants[10])/constants[9])*log(constants[4]/states[1])
    algebraic[57] = constants[11]*(power(states[5], 3.00000))*(0.800000*states[6]+0.200000*states[7])*(states[0]-algebraic[19])
    algebraic[58] = constants[12]*(power(states[8], 3.00000))*states[9]*(states[0]-algebraic[19])
    algebraic[80] = constants[31]*(power(states[1], 3.00000))+1.50000*(power(constants[29], 3.00000))*states[2]+(power(constants[28], 3.00000))*constants[5]*(1.00000+(1.50000*states[2])/constants[30])
    algebraic[81] = constants[30]*(power(constants[4], 3.00000))*(1.00000+states[1]/constants[28])+(power(states[1], 3.00000))*constants[5]+1.50000*(power(constants[4], 3.00000))*states[2]
    algebraic[82] = (constants[26]*constants[27]*(power(states[1], 3.00000))*constants[5]*exp((0.350000*constants[9]*states[0])/(constants[8]*constants[10]))-1.50000*(power(constants[4], 3.00000))*states[2]*exp((-0.650000*constants[9]*states[0])/(constants[8]*constants[10])))/((1.00000+power(constants[32]/(1.50000*states[2]), 2.00000))*(1.00000+constants[33]*exp((-0.650000*states[0]*constants[9])/(constants[8]*constants[10])))*(algebraic[80]+algebraic[81]))
    algebraic[83] = 1.00000/(1.00000+0.124500*exp((-0.100000*constants[9]*states[0])/(constants[8]*constants[10]))+0.0365000*constants[77]*exp((-constants[9]*states[0])/(constants[8]*constants[10])))
    algebraic[84] = (((constants[34]*algebraic[83]*1.00000)/(1.00000+power(constants[35]/states[1], 2.00000)))*constants[6])/(constants[6]+constants[36])
    algebraic[88] = constants[41]*(states[0]-algebraic[19])
    algebraic[46] = ((-constants[8]*constants[10])/constants[9])*log(constants[7]/states[4])
    algebraic[87] = (constants[40]*(power(algebraic[19]-algebraic[46], 4.00000)))/(power(algebraic[19]-algebraic[46], 4.00000)+power(87.8251, 4.00000))
    rates[1] = (-constants[19]*(algebraic[57]+algebraic[58]+algebraic[88]+3.00000*algebraic[84]+3.00000*algebraic[82])*constants[78])/(constants[79]*constants[9])+algebraic[87]
    algebraic[36] = ((constants[8]*constants[10])/constants[9])*log(constants[6]/states[3])
    algebraic[67] = constants[21]*states[18]*(0.800000*states[19]+0.200000*states[20])*(states[0]-algebraic[36])
    algebraic[68] = 1.00000/(1.00000+exp((states[0]-5.40000)/20.4000))
    algebraic[69] = constants[74]*states[21]*algebraic[68]*(states[0]-algebraic[36])
    algebraic[56] = ((constants[8]*constants[10])/constants[9])*log((constants[6]+constants[3]*constants[4])/(states[3]+constants[3]*states[1]))
    algebraic[70] = 0.0525813*(1.00000+0.600000/(1.00000+power(3.80000e-05/states[2], 1.40000)))
    algebraic[71] = algebraic[70]*states[22]*states[23]*(states[0]-algebraic[56])
    algebraic[73] = 1.02000/(1.00000+exp(0.238500*(states[0]-(algebraic[36]+59.2150))))
    algebraic[72] = (0.491240*exp(0.0803200*((states[0]+5.47600)-algebraic[36]))+exp(0.0617500*(states[0]-(594.310+algebraic[36]))))/(1.00000+exp(-0.514300*((states[0]+4.75300)-algebraic[36])))
    algebraic[74] = algebraic[73]/(algebraic[73]+algebraic[72])
    algebraic[75] = (constants[75]*algebraic[74]+0.00400000)*(states[0]-algebraic[36])
    algebraic[89] = constants[42]*(states[0]-algebraic[36])
    algebraic[76] = 1.00000/(1.00000+exp((7.48800-states[0])/5.98000))
    algebraic[77] = constants[22]*algebraic[76]*(states[0]-algebraic[36])
    algebraic[86] = (constants[39]*(algebraic[36]-algebraic[46]))/((algebraic[36]+87.8251)-algebraic[46])
    rates[3] = (-constants[19]*((algebraic[67]+algebraic[75]+algebraic[69]+algebraic[71]+algebraic[77]+algebraic[89])-2.00000*algebraic[84])*constants[78])/(constants[79]*constants[9])+algebraic[86]
    algebraic[78] = (((((1.00000*constants[23])/constants[19])*(power(constants[24], 2.00000))*states[0]*(power(constants[9], 2.00000)))/(constants[8]*constants[10]))*(states[4]-constants[7]*exp((-constants[24]*states[0]*constants[9])/(constants[8]*constants[10]))))/(1.00000-exp((-constants[24]*states[0]*constants[9])/(constants[8]*constants[10])))
    algebraic[79] = 20.0000*algebraic[78]*states[24]
    algebraic[90] = constants[44]*(states[0]-algebraic[46])
    rates[4] = (-constants[19]*(algebraic[79]+algebraic[90])*constants[78])/(constants[79]*constants[9])+algebraic[87]+algebraic[86]
    algebraic[0] = custom_piecewise([greater_equal(voi , constants[0]) & less_equal(voi , constants[1]), constants[2] , True, 0.00000])
    algebraic[64] = constants[20]*states[16]*states[17]*(states[0]-50.0000)
    algebraic[91] = (((((1.00000*constants[43])/constants[19])*(power(constants[15], 2.00000))*states[0]*(power(constants[9], 2.00000)))/(constants[8]*constants[10]))*(constants[16]*states[2]*exp((constants[15]*states[0]*constants[9])/(constants[8]*constants[10]))-constants[17]*constants[5]))/(exp((constants[15]*states[0]*constants[9])/(constants[8]*constants[10]))-1.00000)
    algebraic[85] = (constants[37]*states[2])/(constants[38]+states[2])
    algebraic[92] = algebraic[57]+algebraic[58]+algebraic[60]+algebraic[64]+algebraic[67]+algebraic[79]+algebraic[69]+algebraic[71]+algebraic[75]+algebraic[82]+algebraic[84]+algebraic[88]+algebraic[89]+algebraic[91]+algebraic[90]+algebraic[85]+algebraic[77]
    rates[0] = -(algebraic[92]+algebraic[0])
    algebraic[96] = (constants[51]*(1.00000-states[25]))/(1.00000+constants[18]/states[10])
    rates[25] = constants[49]*algebraic[96]*(algebraic[96]+states[25])-constants[50]*states[25]
    algebraic[61] = 0.300000/(1.00000-algebraic[60]/0.0500000)+0.550000/(1.00000+states[10]/0.00300000)+0.150000
    algebraic[97] = algebraic[96]+states[25]
    algebraic[98] = 0.500000+(10.0000*1.00000*algebraic[97])/(1.00000*algebraic[97]+constants[18])+1.00000/(1.00000+states[10]/0.00300000)
    rates[14] = (algebraic[61]-states[14])/algebraic[98]
    algebraic[104] = (constants[59]*1.00000*algebraic[97])/(constants[18]+1.00000*algebraic[97])
    algebraic[100] = 1.00000/(1.00000+exp((algebraic[60]+0.0500000)/0.0150000))
    algebraic[106] = (350.000-algebraic[104])/(1.00000+exp(((states[10]-0.00300000)+0.00300000*algebraic[100])/0.000200000))+3.00000+algebraic[104]
    algebraic[102] = 1.00000/(1.00000+exp(((states[10]-0.000400000)+0.00200000*algebraic[100])/2.50000e-05))
    rates[28] = (algebraic[102]-states[28])/algebraic[106]
    algebraic[99] = (states[10]-states[2])/constants[58]
    algebraic[107] = 1.00000/(1.00000+exp((constants[13]*algebraic[59]+13.0000)/5.00000))
    algebraic[108] = 3000.00*algebraic[107]
    algebraic[109] = algebraic[108]*states[29]*states[28]*(states[27]-states[10])
    algebraic[103] = (2.00000*constants[56]*states[10])/(power(states[10]+constants[54], 2.00000))
    algebraic[101] = (2.00000*constants[57]*states[10])/(power(states[10]+constants[55], 2.00000))
    algebraic[105] = 1.00000/(1.00000+algebraic[103]+algebraic[101])
    rates[10] = algebraic[105]*(((-constants[19]*algebraic[60]*constants[78])/(constants[82]*constants[15]*constants[9])+(algebraic[109]*constants[81])/constants[82])-algebraic[99])
    algebraic[94] = (2.00000*constants[47]*states[2])/(power(states[2]+constants[45], 2.00000))
    algebraic[93] = (2.00000*constants[48]*states[2])/(power(states[2]+constants[46], 2.00000))
    algebraic[95] = 1.00000/(1.00000+algebraic[94]+algebraic[93])
    algebraic[111] = (constants[65]*algebraic[97]*1.00000)/(constants[18]+algebraic[97]*1.00000)
    algebraic[112] = (constants[66]*algebraic[97]*1.00000)/(constants[18]+algebraic[97]*1.00000)
    algebraic[113] = (constants[63]*(algebraic[111]+1.00000)*constants[64]*states[2])/((states[2]+constants[67])-algebraic[112])
    algebraic[110] = (constants[61]*states[26])/constants[62]
    rates[2] = -algebraic[95]*(((constants[19]*((algebraic[91]+algebraic[85])-2.00000*algebraic[82])*constants[78])/(2.00000*constants[79]*constants[9])+((algebraic[113]-algebraic[110])*constants[80])/constants[79])-(algebraic[99]*constants[82])/constants[79])
    algebraic[114] = (states[26]-states[27])/constants[68]
    rates[26] = algebraic[113]-(algebraic[110]+(algebraic[114]*constants[81])/constants[80])
    rates[27] = (algebraic[114]-algebraic[109])/(1.00000+(constants[52]*constants[53])/(power(constants[53]+states[27], 2.00000)))
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[18] = 1.00000/(1.00000+constants[25]/states[10])
    algebraic[24] = 175.000+125.000/(1.00000+exp(-(states[0]+25.0000)/6.00000))
    algebraic[6] = 1.00000/(1.00000+exp((states[0]+69.0000)/6.10000))
    algebraic[7] = 1.00000/(1.00000+exp(-(states[0]-4.00000)/6.74000))
    algebraic[25] = 0.590000+(0.800000*exp(0.0520000*(states[0]+13.0000)))/(1.00000+exp(0.132000*(states[0]+13.0000)))
    algebraic[8] = 1.00000/(1.00000+exp((states[0]+18.0000)/10.0000))
    algebraic[26] = 4.00000+0.00500000*(power(states[0]-2.50000, 2.00000))
    algebraic[9] = 1.00000/(1.00000+exp((states[0]+18.0000)/10.0000))
    algebraic[27] = 38.0000+0.0700000*(power(states[0]-18.6000, 2.00000))
    algebraic[15] = 900.000/(1.00000+exp(states[0]/5.00000))+100.000
    algebraic[33] = 1.00000/(1.00000+exp(-(states[0]+0.0850000)/12.2500))
    algebraic[16] = 1.00000/((7.61000e-05*(states[0]+44.6000))/(1.00000-exp(-9.97000*(states[0]+44.6000)))+(0.000360000*(states[0]-0.550000))/(exp(0.128000*(states[0]-0.550000))-1.00000))
    algebraic[34] = 1.00000/(1.00000+exp(-(states[0]-9.00000)/13.7000))
    algebraic[17] = (2.00000*1.00000)/((7.61000e-05*(states[0]+44.6000))/(1.00000-exp(-9.97000*(states[0]+44.6000)))+(0.000360000*(states[0]-0.550000))/(exp(0.128000*(states[0]-0.550000))-1.00000))
    algebraic[35] = 1.00000/(1.00000+exp(-(states[0]-9.00000)/13.7000))
    algebraic[2] = (0.320000*(states[0]+47.1300))/(1.00000-exp(-0.100000*(states[0]+47.1300)))
    algebraic[20] = 0.0800000*exp(-states[0]/11.0000)
    algebraic[47] = 1.00000/(algebraic[2]+algebraic[20])
    algebraic[37] = algebraic[2]/(algebraic[2]+algebraic[20])
    algebraic[3] = custom_piecewise([less(states[0] , -40.0000), 0.135000*exp((states[0]+80.0000)/-6.80000) , True, 0.00000])
    algebraic[21] = custom_piecewise([less(states[0] , -40.0000), 3.56000*exp(0.0790000*states[0])+310000.*exp(0.350000*states[0]) , True, 1.00000/(0.130000*(1.00000+exp((states[0]+10.6600)/-11.1000)))])
    algebraic[48] = 1.00000/(algebraic[3]+algebraic[21])
    algebraic[38] = algebraic[3]/(algebraic[3]+algebraic[21])
    algebraic[4] = custom_piecewise([less(states[0] , -40.0000), ((-127140.*exp(0.244400*states[0])-3.47400e-05*exp(-0.0439100*states[0]))*(states[0]+37.7800))/(1.00000+exp(0.311000*(states[0]+79.2300))) , True, 0.00000])
    algebraic[22] = custom_piecewise([less(states[0] , -40.0000), (0.121200*exp(-0.0105200*states[0]))/(1.00000+exp(-0.137800*(states[0]+40.1400))) , True, (0.300000*exp(-2.53500e-07*states[0]))/(1.00000+exp(-0.100000*(states[0]+32.0000)))])
    algebraic[49] = 0.100000/(algebraic[4]+algebraic[22])
    algebraic[39] = (0.100000*algebraic[4])/(algebraic[4]+algebraic[22])
    algebraic[5] = (0.320000*(states[0]+47.1300))/(1.00000-exp(-0.100000*(states[0]+47.1300)))
    algebraic[23] = 0.0800000*exp(-states[0]/11.0000)
    algebraic[50] = 1.00000/(algebraic[5]+algebraic[23])
    algebraic[40] = algebraic[5]/(algebraic[5]+algebraic[23])
    algebraic[10] = 1.06800*exp((states[0]+16.3000)/30.0000)
    algebraic[28] = 1.06800*exp(-(states[0]+16.3000)/30.0000)
    algebraic[51] = 1.00000/(algebraic[10]+algebraic[28])
    algebraic[41] = 1.00000/(1.00000+exp(-(states[0]+33.0000)/6.10000))
    algebraic[11] = 0.0150000*exp(-(states[0]+71.7000)/83.3000)
    algebraic[29] = 0.0150000*exp((states[0]+71.7000)/15.4000)
    algebraic[52] = 1.00000/(algebraic[11]+algebraic[29])
    algebraic[42] = 1.00000/(1.00000+exp((states[0]+60.0000)/6.60000))
    algebraic[12] = (25.0000*exp((states[0]-76.0000)/20.0000))/(1.00000+exp((states[0]-76.0000)/20.0000))
    algebraic[30] = (25.0000*exp(-(states[0]+54.0000)/20.0000))/(1.00000+exp(-(states[0]+54.0000)/20.0000))
    algebraic[43] = 1.00000/(algebraic[12]+algebraic[30])
    algebraic[53] = algebraic[12]/(algebraic[12]+algebraic[30])
    algebraic[44] = 6.00000+5.00000/(1.00000+exp((states[0]-16.5000)/10.0000))
    algebraic[13] = 0.0300000/(1.00000+exp((states[0]+25.0000)/15.0000))
    algebraic[31] = (0.100000*exp((states[0]-40.0000)/15.0000))/(1.00000+exp((states[0]-40.0000)/15.0000))
    algebraic[54] = algebraic[13]/(algebraic[13]+algebraic[31])
    algebraic[45] = 21.5000+30.0000/(1.00000+exp((states[0]-25.0000)/10.0000))
    algebraic[14] = 0.00442000/(1.00000+exp((states[0]+26.0000)/15.0000))
    algebraic[32] = (0.0500000*exp((states[0]-10.0000)/15.0000))/(1.00000+exp((states[0]-10.0000)/15.0000))
    algebraic[55] = algebraic[14]/(algebraic[14]+algebraic[32])
    algebraic[59] = (((((1.00000*constants[14])/constants[19])*(power(constants[15], 2.00000))*(states[0]-15.0000)*(power(constants[9], 2.00000)))/(constants[8]*constants[10]))*(constants[16]*states[10]*exp((constants[15]*constants[9]*(states[0]-15.0000))/(constants[8]*constants[10]))-constants[17]*constants[5]))/(exp((constants[15]*constants[9]*(states[0]-15.0000))/(constants[8]*constants[10]))-1.00000)
    algebraic[60] = constants[13]*states[11]*states[12]*states[13]*states[14]*states[15]*algebraic[59]
    algebraic[62] = 1.00000/(1.00000-algebraic[60]/0.0100000)
    algebraic[65] = 125.000+300.000/(1.00000+exp((-algebraic[60]-0.175000)/0.0400000))
    algebraic[63] = (power(states[27], 1.90000))/(power(states[27], 1.90000)+power((49.2800*states[10])/(states[10]+0.00280000), 1.90000))
    algebraic[66] = (algebraic[63]*(power(algebraic[60], 2.00000)))/(power(algebraic[60], 2.00000)+1.00000)
    algebraic[19] = ((constants[8]*constants[10])/constants[9])*log(constants[4]/states[1])
    algebraic[57] = constants[11]*(power(states[5], 3.00000))*(0.800000*states[6]+0.200000*states[7])*(states[0]-algebraic[19])
    algebraic[58] = constants[12]*(power(states[8], 3.00000))*states[9]*(states[0]-algebraic[19])
    algebraic[80] = constants[31]*(power(states[1], 3.00000))+1.50000*(power(constants[29], 3.00000))*states[2]+(power(constants[28], 3.00000))*constants[5]*(1.00000+(1.50000*states[2])/constants[30])
    algebraic[81] = constants[30]*(power(constants[4], 3.00000))*(1.00000+states[1]/constants[28])+(power(states[1], 3.00000))*constants[5]+1.50000*(power(constants[4], 3.00000))*states[2]
    algebraic[82] = (constants[26]*constants[27]*(power(states[1], 3.00000))*constants[5]*exp((0.350000*constants[9]*states[0])/(constants[8]*constants[10]))-1.50000*(power(constants[4], 3.00000))*states[2]*exp((-0.650000*constants[9]*states[0])/(constants[8]*constants[10])))/((1.00000+power(constants[32]/(1.50000*states[2]), 2.00000))*(1.00000+constants[33]*exp((-0.650000*states[0]*constants[9])/(constants[8]*constants[10])))*(algebraic[80]+algebraic[81]))
    algebraic[83] = 1.00000/(1.00000+0.124500*exp((-0.100000*constants[9]*states[0])/(constants[8]*constants[10]))+0.0365000*constants[77]*exp((-constants[9]*states[0])/(constants[8]*constants[10])))
    algebraic[84] = (((constants[34]*algebraic[83]*1.00000)/(1.00000+power(constants[35]/states[1], 2.00000)))*constants[6])/(constants[6]+constants[36])
    algebraic[88] = constants[41]*(states[0]-algebraic[19])
    algebraic[46] = ((-constants[8]*constants[10])/constants[9])*log(constants[7]/states[4])
    algebraic[87] = (constants[40]*(power(algebraic[19]-algebraic[46], 4.00000)))/(power(algebraic[19]-algebraic[46], 4.00000)+power(87.8251, 4.00000))
    algebraic[36] = ((constants[8]*constants[10])/constants[9])*log(constants[6]/states[3])
    algebraic[67] = constants[21]*states[18]*(0.800000*states[19]+0.200000*states[20])*(states[0]-algebraic[36])
    algebraic[68] = 1.00000/(1.00000+exp((states[0]-5.40000)/20.4000))
    algebraic[69] = constants[74]*states[21]*algebraic[68]*(states[0]-algebraic[36])
    algebraic[56] = ((constants[8]*constants[10])/constants[9])*log((constants[6]+constants[3]*constants[4])/(states[3]+constants[3]*states[1]))
    algebraic[70] = 0.0525813*(1.00000+0.600000/(1.00000+power(3.80000e-05/states[2], 1.40000)))
    algebraic[71] = algebraic[70]*states[22]*states[23]*(states[0]-algebraic[56])
    algebraic[73] = 1.02000/(1.00000+exp(0.238500*(states[0]-(algebraic[36]+59.2150))))
    algebraic[72] = (0.491240*exp(0.0803200*((states[0]+5.47600)-algebraic[36]))+exp(0.0617500*(states[0]-(594.310+algebraic[36]))))/(1.00000+exp(-0.514300*((states[0]+4.75300)-algebraic[36])))
    algebraic[74] = algebraic[73]/(algebraic[73]+algebraic[72])
    algebraic[75] = (constants[75]*algebraic[74]+0.00400000)*(states[0]-algebraic[36])
    algebraic[89] = constants[42]*(states[0]-algebraic[36])
    algebraic[76] = 1.00000/(1.00000+exp((7.48800-states[0])/5.98000))
    algebraic[77] = constants[22]*algebraic[76]*(states[0]-algebraic[36])
    algebraic[86] = (constants[39]*(algebraic[36]-algebraic[46]))/((algebraic[36]+87.8251)-algebraic[46])
    algebraic[78] = (((((1.00000*constants[23])/constants[19])*(power(constants[24], 2.00000))*states[0]*(power(constants[9], 2.00000)))/(constants[8]*constants[10]))*(states[4]-constants[7]*exp((-constants[24]*states[0]*constants[9])/(constants[8]*constants[10]))))/(1.00000-exp((-constants[24]*states[0]*constants[9])/(constants[8]*constants[10])))
    algebraic[79] = 20.0000*algebraic[78]*states[24]
    algebraic[90] = constants[44]*(states[0]-algebraic[46])
    algebraic[0] = custom_piecewise([greater_equal(voi , constants[0]) & less_equal(voi , constants[1]), constants[2] , True, 0.00000])
    algebraic[64] = constants[20]*states[16]*states[17]*(states[0]-50.0000)
    algebraic[91] = (((((1.00000*constants[43])/constants[19])*(power(constants[15], 2.00000))*states[0]*(power(constants[9], 2.00000)))/(constants[8]*constants[10]))*(constants[16]*states[2]*exp((constants[15]*states[0]*constants[9])/(constants[8]*constants[10]))-constants[17]*constants[5]))/(exp((constants[15]*states[0]*constants[9])/(constants[8]*constants[10]))-1.00000)
    algebraic[85] = (constants[37]*states[2])/(constants[38]+states[2])
    algebraic[92] = algebraic[57]+algebraic[58]+algebraic[60]+algebraic[64]+algebraic[67]+algebraic[79]+algebraic[69]+algebraic[71]+algebraic[75]+algebraic[82]+algebraic[84]+algebraic[88]+algebraic[89]+algebraic[91]+algebraic[90]+algebraic[85]+algebraic[77]
    algebraic[96] = (constants[51]*(1.00000-states[25]))/(1.00000+constants[18]/states[10])
    algebraic[61] = 0.300000/(1.00000-algebraic[60]/0.0500000)+0.550000/(1.00000+states[10]/0.00300000)+0.150000
    algebraic[97] = algebraic[96]+states[25]
    algebraic[98] = 0.500000+(10.0000*1.00000*algebraic[97])/(1.00000*algebraic[97]+constants[18])+1.00000/(1.00000+states[10]/0.00300000)
    algebraic[104] = (constants[59]*1.00000*algebraic[97])/(constants[18]+1.00000*algebraic[97])
    algebraic[100] = 1.00000/(1.00000+exp((algebraic[60]+0.0500000)/0.0150000))
    algebraic[106] = (350.000-algebraic[104])/(1.00000+exp(((states[10]-0.00300000)+0.00300000*algebraic[100])/0.000200000))+3.00000+algebraic[104]
    algebraic[102] = 1.00000/(1.00000+exp(((states[10]-0.000400000)+0.00200000*algebraic[100])/2.50000e-05))
    algebraic[99] = (states[10]-states[2])/constants[58]
    algebraic[107] = 1.00000/(1.00000+exp((constants[13]*algebraic[59]+13.0000)/5.00000))
    algebraic[108] = 3000.00*algebraic[107]
    algebraic[109] = algebraic[108]*states[29]*states[28]*(states[27]-states[10])
    algebraic[103] = (2.00000*constants[56]*states[10])/(power(states[10]+constants[54], 2.00000))
    algebraic[101] = (2.00000*constants[57]*states[10])/(power(states[10]+constants[55], 2.00000))
    algebraic[105] = 1.00000/(1.00000+algebraic[103]+algebraic[101])
    algebraic[94] = (2.00000*constants[47]*states[2])/(power(states[2]+constants[45], 2.00000))
    algebraic[93] = (2.00000*constants[48]*states[2])/(power(states[2]+constants[46], 2.00000))
    algebraic[95] = 1.00000/(1.00000+algebraic[94]+algebraic[93])
    algebraic[111] = (constants[65]*algebraic[97]*1.00000)/(constants[18]+algebraic[97]*1.00000)
    algebraic[112] = (constants[66]*algebraic[97]*1.00000)/(constants[18]+algebraic[97]*1.00000)
    algebraic[113] = (constants[63]*(algebraic[111]+1.00000)*constants[64]*states[2])/((states[2]+constants[67])-algebraic[112])
    algebraic[110] = (constants[61]*states[26])/constants[62]
    algebraic[114] = (states[26]-states[27])/constants[68]
    algebraic[1] = ((constants[8]*constants[10])/(2.00000*constants[9]))*log(constants[5]/states[2])
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
        self.stim_start = 0
        self.stim_end = 1
        self.stim_amplitude = -80
        self.r_NaK = 0.01833
        self.Na_o = 140
        self.Ca_o = 1.8
        self.K_o = 5.4
        self.Cl_o = 100
        self.R = 8314
        self.F = 96485
        self.T = 310
        self.g_Na = 8
        self.g_Na_L = 0.037375
        self.g_Ca_L = 0.3392328
        self.p_Ca = 0.000243
        self.z_Ca = 2
        self.gamma_Cai = 1
        self.gamma_Cao = 0.341
        self.km_Ca_MK = 0.15
        self.Cm = 1
        self.g_Ca_T = 0.13
        self.g_to_1 = 0.14135944
        self.g_K_p = 0.00276
        self.p_Cl = 0.0000004
        self.z_Cl = -1
        self.km_to_2 = 0.1502
        self.X_NaCa = 0.4
        self.i_NaCa_max = 4.5
        self.km_Na_i_1 = 12.3
        self.km_Na_o = 87.5
        self.km_Ca_i = 0.0036
        self.km_Ca_o = 1.3
        self.km_Ca_act = 0.000125
        self.k_sat = 0.27
        self.g_NaK = 0.61875
        self.km_Na_i_2 = 10
        self.km_K_o = 1.5
        self.i_Ca_p_max = 0.0575
        self.km_Ca_p = 0.0005
        self.CT_K_Cl_max = 7.0756e-6
        self.CT_Na_Cl_max = 9.8443e-6
        self.g_Na_b = 0.0025
        self.g_K_b = 0.005
        self.p_Ca_b = 1.995084e-7
        self.g_Cl_b = 0.000225
        self.km_TRPN = 0.0005
        self.km_CMDN = 0.00238
        self.TRPN_max = 0.07
        self.CMDN_max = 0.05
        self.alpha_Ca_MK = 0.05
        self.beta_Ca_MK = 0.00068
        self.Ca_MK_0 = 0.05
        self.CSQN_max = 10
        self.km_CSQN = 0.8
        self.km_b_SR = 0.00087
        self.km_b_SL = 0.0087
        self.b_SR_max = 0.047
        self.b_SL_max = 1.124
        self.tau_ss = 0.2
        self.tau_Ca_MK_max = 10
        self.tau_ro = 3
        self.q_leak_max = 0.004375
        self.NSR_max = 15
        self.X_q_up = 0.5
        self.q_up_max = 0.004375
        self.dq_up_Ca_MK_max = 0.75
        self.dkm_plb_max = 0.00017
        self.km_up = 0.00092
        self.tau_tr = 120
        self.Vol_cell = 0.3454
        self.radius = 0.0011
        self.length = 0.01
        self.rcg = 2
        self.tau_a = 1.00000

    def to_dict(self):
        return {
            "stim_start": self.stim_start,
            "stim_end": self.stim_end,
            "stim_amplitude": self.stim_amplitude,
            "r_NaK": self.r_NaK,
            "Na_o": self.Na_o,
            "Ca_o": self.Ca_o,
            "K_o": self.K_o,
            "Cl_o": self.Cl_o,
            "R": self.R,
            "F": self.F,
            "T": self.T,
            "g_Na": self.g_Na,
            "g_Na_L": self.g_Na_L,
            "g_Ca_L": self.g_Ca_L,
            "p_Ca": self.p_Ca,
            "z_Ca": self.z_Ca,
            "gamma_Cai": self.gamma_Cai,
            "gamma_Cao": self.gamma_Cao,
            "km_Ca_MK": self.km_Ca_MK,
            "Cm": self.Cm,
            "g_Ca_T": self.g_Ca_T,
            "g_to_1": self.g_to_1,
            "g_K_p": self.g_K_p,
            "p_Cl": self.p_Cl,
            "z_Cl": self.z_Cl,
            "km_to_2": self.km_to_2,
            "X_NaCa": self.X_NaCa,
            "i_NaCa_max": self.i_NaCa_max,
            "km_Na_i_1": self.km_Na_i_1,
            "km_Na_o": self.km_Na_o,
            "km_Ca_i": self.km_Ca_i,
            "km_Ca_o": self.km_Ca_o,
            "km_Ca_act": self.km_Ca_act,
            "k_sat": self.k_sat,
            "g_NaK": self.g_NaK,
            "km_Na_i_2": self.km_Na_i_2,
            "km_K_o": self.km_K_o,
            "i_Ca_p_max": self.i_Ca_p_max,
            "km_Ca_p": self.km_Ca_p,
            "CT_K_Cl_max": self.CT_K_Cl_max,
            "CT_Na_Cl_max": self.CT_Na_Cl_max,
            "g_Na_b": self.g_Na_b,
            "g_K_b": self.g_K_b,
            "p_Ca_b": self.p_Ca_b,
            "g_Cl_b": self.g_Cl_b,
            "km_TRPN": self.km_TRPN,
            "km_CMDN": self.km_CMDN,
            "TRPN_max": self.TRPN_max,
            "CMDN_max": self.CMDN_max,
            "alpha_Ca_MK": self.alpha_Ca_MK,
            "beta_Ca_MK": self.beta_Ca_MK,
            "Ca_MK_0": self.Ca_MK_0,
            "CSQN_max": self.CSQN_max,
            "km_CSQN": self.km_CSQN,
            "km_b_SR": self.km_b_SR,
            "km_b_SL": self.km_b_SL,
            "b_SR_max": self.b_SR_max,
            "b_SL_max": self.b_SL_max,
            "tau_ss": self.tau_ss,
            "tau_Ca_MK_max": self.tau_Ca_MK_max,
            "tau_ro": self.tau_ro,
            "q_leak_max": self.q_leak_max,
            "NSR_max": self.NSR_max,
            "X_q_up": self.X_q_up,
            "q_up_max": self.q_up_max,
            "dq_up_Ca_MK_max": self.dq_up_Ca_MK_max,
            "dkm_plb_max": self.dkm_plb_max,
            "km_up": self.km_up,
            "tau_tr": self.tau_tr,
            "Vol_cell": self.Vol_cell,
            "radius": self.radius,
            "length": self.length,
            "rcg": self.rcg,
            "tau_a": self.tau_a,
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
        y0=[-83.43812846286808, 9.927155552932733, 0.00022355433459434943, 141.9670801746057, 18.904682470140408, 0.002003390432234504, 0.9786390933308567, 0.09866447258167589, 0.002003390432234504, 0.8946968372659203, 0.00022418117117903934, 0.000002322223865147363, 0.9985607329462358, 0.8173435436674658, 0.9610551285529658, 0.868690796671854, 0.0002563937630984438, 0.9720432601848331, 0.0004238729429342389, 0.9990935802459496, 0.9777368439681764, 0.07084939408222911, 0.0011737654433043125, 0.001179442867470093, 0.0014909437525000811, 0.000008789168284782809, 1.2132524695849454, 1.1433050636518596, 0.7802870066567904, 1.2785734760674763e-9],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "aslanidi_2009"
        self.curve_names = [
            "V",
            "Na_i",
            "Ca_i",
            "K_i",
            "Cl_i",
            "m",
            "h",
            "j",
            "m_L",
            "h_L",
            "Ca_r",
            "d",
            "f",
            "f2",
            "f_Ca",
            "f_Ca2",
            "b",
            "g",
            "a",
            "i",
            "i2",
            "xr",
            "xs1",
            "xs2",
            "a_1",
            "Ca_MK_trap",
            "Ca_NSR",
            "Ca_JSR",
            "ri",
            "ro",
        ]
        self.state_names = ['V', 'Na_i', 'Ca_i', 'K_i', 'Cl_i', 'm', 'h', 'j', 'm_L', 'h_L', 'Ca_r', 'd', 'f', 'f2', 'f_Ca', 'f_Ca2', 'b', 'g', 'a', 'i', 'i2', 'xr', 'xs1', 'xs2', 'a_1', 'Ca_MK_trap', 'Ca_NSR', 'Ca_JSR', 'ri', 'ro']
        self.algebraic_names = ['i_stim', 'E_Ca', 'alpha_m', 'alpha_h', 'alpha_j', 'alpha_m_L', 'h_L_infinity', 'd_infinity', 'f_infinity', 'f2_infinity', 'alpha_b', 'alpha_g', 'alpha_a', 'alpha_i', 'alpha_i2', 'tau_xr', 'tau_xs1', 'tau_xs2', 'a_infinity', 'E_Na', 'beta_m', 'beta_h', 'beta_j', 'beta_m_L', 'tau_h_L', 'tau_d', 'tau_f', 'tau_f2', 'beta_b', 'beta_g', 'beta_a', 'beta_i', 'beta_i2', 'xr_infinity', 'xs1_infinity', 'xs2_infinity', 'E_K', 'm_infinity', 'h_infinity', 'j_infinity', 'm_L_infinity', 'b_infinity', 'g_infinity', 'tau_a', 'tau_i', 'tau_i2', 'E_Cl', 'tau_m', 'tau_h', 'tau_j', 'tau_m_L', 'tau_b', 'tau_g', 'a_infinity_1', 'i_infinity', 'i2_infinity', 'E_Ks', 'i_Na', 'i_Na_L', 'i_Ca_L_max', 'i_Ca_L', 'f_Ca_infinity', 'f_Ca2_infinity', 'ro_infinity_JSR', 'i_Ca_T', 'tau_f_Ca2', 'ro_infinity', 'i_to_1', 'rr_infinity', 'i_Kr', 'g_Ks', 'i_Ks', 'beta_xK1', 'alpha_xK1', 'xK1', 'i_K1', 'kp', 'i_K_p', 'i_to_2_max', 'i_to_2', 'dNaCa_1', 'dNaCa_2', 'i_NaCa', 'f_NaK', 'i_NaK', 'i_Ca_p', 'CT_K_Cl', 'CT_Na_Cl', 'i_Na_b', 'i_K_b', 'i_Cl_b', 'i_Ca_b', 'i_tot', 'CMDN', 'TRPN', 'b_myo', 'Ca_MK_bound', 'Ca_MK_act', 'tau_f_Ca', 'q_diff', 'Ca_fac', 'b_SL', 'ri_infinity', 'b_SR', 'tau_Ca_MK', 'Ca_r_tot', 'tau_ri', 'vg', 'g_rel', 'q_rel', 'q_leak', 'dq_up_Ca_MK', 'dkm_plb', 'q_up', 'q_tr']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 83
        p = self.params

        # direct mapping
        c[0] = p.stim_start
        c[1] = p.stim_end
        c[2] = p.stim_amplitude
        c[3] = p.r_NaK
        c[4] = p.Na_o
        c[5] = p.Ca_o
        c[6] = p.K_o
        c[7] = p.Cl_o
        c[8] = p.R
        c[9] = p.F
        c[10] = p.T
        c[11] = p.g_Na
        c[12] = p.g_Na_L
        c[13] = p.g_Ca_L
        c[14] = p.p_Ca
        c[15] = p.z_Ca
        c[16] = p.gamma_Cai
        c[17] = p.gamma_Cao
        c[18] = p.km_Ca_MK
        c[19] = p.Cm
        c[20] = p.g_Ca_T
        c[21] = p.g_to_1
        c[22] = p.g_K_p
        c[23] = p.p_Cl
        c[24] = p.z_Cl
        c[25] = p.km_to_2
        c[26] = p.X_NaCa
        c[27] = p.i_NaCa_max
        c[28] = p.km_Na_i_1
        c[29] = p.km_Na_o
        c[30] = p.km_Ca_i
        c[31] = p.km_Ca_o
        c[32] = p.km_Ca_act
        c[33] = p.k_sat
        c[34] = p.g_NaK
        c[35] = p.km_Na_i_2
        c[36] = p.km_K_o
        c[37] = p.i_Ca_p_max
        c[38] = p.km_Ca_p
        c[39] = p.CT_K_Cl_max
        c[40] = p.CT_Na_Cl_max
        c[41] = p.g_Na_b
        c[42] = p.g_K_b
        c[43] = p.p_Ca_b
        c[44] = p.g_Cl_b
        c[45] = p.km_TRPN
        c[46] = p.km_CMDN
        c[47] = p.TRPN_max
        c[48] = p.CMDN_max
        c[49] = p.alpha_Ca_MK
        c[50] = p.beta_Ca_MK
        c[51] = p.Ca_MK_0
        c[52] = p.CSQN_max
        c[53] = p.km_CSQN
        c[54] = p.km_b_SR
        c[55] = p.km_b_SL
        c[56] = p.b_SR_max
        c[57] = p.b_SL_max
        c[58] = p.tau_ss
        c[59] = p.tau_Ca_MK_max
        c[60] = p.tau_ro
        c[61] = p.q_leak_max
        c[62] = p.NSR_max
        c[63] = p.X_q_up
        c[64] = p.q_up_max
        c[65] = p.dq_up_Ca_MK_max
        c[66] = p.dkm_plb_max
        c[67] = p.km_up
        c[68] = p.tau_tr
        c[69] = p.Vol_cell
        c[70] = p.radius
        c[71] = p.length
        c[72] = p.rcg
        c[76] = p.tau_a

        # derived constants
        c[73] = 2.00000*3.14000*(power(c[70], 2.00000))+2.00000*3.14000*c[70]*c[71]
        c[74] = 0.0400085*(power(c[6]/5.40000, 1.0/2))
        c[75] = 0.250000*(power(c[6]/5.40000, 1.0/2))
        c[77] = (1.00000/7.00000)*(exp(c[4]/67.3000)-1.00000)
        c[78] = c[72]*c[73]
        c[79] = c[69]*0.680000
        c[80] = c[69]*0.0552000
        c[81] = c[69]*0.00480000
        c[82] = c[69]*0.0200000

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
