# Size of variable arrays:
sizeAlgebraic = 141
sizeStates = 37
sizeConstants = 101
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (millisecond)"
    legend_states[0] = "Vm in component membrane (millivolt)"
    legend_constants[0] = "R in component membrane (coulomb_millivolt_per_kelvin_millimole)"
    legend_constants[1] = "T in component membrane (kelvin)"
    legend_constants[2] = "F in component membrane (coulomb_per_millimole)"
    legend_constants[3] = "Cm in component membrane (picoF)"
    legend_algebraic[0] = "i_ext in component membrane (picoA)"
    legend_algebraic[105] = "i_tot in component membrane (picoA)"
    legend_algebraic[89] = "i_I in component membrane (picoA)"
    legend_algebraic[45] = "i_Na in component sodium_current (picoA)"
    legend_algebraic[50] = "i_Ca_L in component L_type_Ca_channel (picoA)"
    legend_algebraic[54] = "i_Ca_T in component T_type_Ca_channel (picoA)"
    legend_algebraic[70] = "i_K1 in component time_independent_potassium_current (picoA)"
    legend_algebraic[71] = "i_Kr in component rapid_time_dependent_potassium_current (picoA)"
    legend_algebraic[74] = "i_Ks in component slow_time_dependent_potassium_current (picoA)"
    legend_algebraic[77] = "i_to in component transient_outward_current (picoA)"
    legend_algebraic[103] = "i_NaK in component sodium_potassium_pump (picoA)"
    legend_algebraic[94] = "i_NaCa in component sodium_calcium_exchanger (picoA)"
    legend_algebraic[80] = "i_bNSC in component background_NSC_current (picoA)"
    legend_algebraic[88] = "i_Cab in component background_Cab_current (picoA)"
    legend_algebraic[81] = "i_Kpl in component background_Kpl_current (picoA)"
    legend_algebraic[85] = "i_lCa in component background_lCa_current (picoA)"
    legend_algebraic[87] = "i_KATP in component background_KATP_current (picoA)"
    legend_constants[4] = "stim_start in component membrane (millisecond)"
    legend_constants[5] = "stim_end in component membrane (millisecond)"
    legend_constants[6] = "stim_period in component membrane (millisecond)"
    legend_constants[7] = "stim_duration in component membrane (millisecond)"
    legend_constants[8] = "stim_amplitude in component membrane (picoA)"
    legend_constants[9] = "Nao in component external_ion_concentrations (millimolar)"
    legend_constants[10] = "Cao in component external_ion_concentrations (millimolar)"
    legend_constants[11] = "Ko in component external_ion_concentrations (millimolar)"
    legend_states[1] = "Nai in component internal_ion_concentrations (millimolar)"
    legend_algebraic[29] = "Cai in component internal_ion_concentrations (millimolar)"
    legend_states[2] = "Ki in component internal_ion_concentrations (millimolar)"
    legend_constants[12] = "Vi in component internal_ion_concentrations (micrometre3)"
    legend_algebraic[106] = "i_net_Na in component internal_ion_concentrations (picoA)"
    legend_algebraic[107] = "i_net_K in component internal_ion_concentrations (picoA)"
    legend_algebraic[96] = "i_net_Ca in component internal_ion_concentrations (picoA)"
    legend_algebraic[42] = "i_Na_Na in component sodium_current (picoA)"
    legend_algebraic[48] = "i_CaL_Na in component L_type_Ca_channel (picoA)"
    legend_algebraic[79] = "i_bNSC_Na in component background_NSC_current (picoA)"
    legend_algebraic[84] = "i_lCa_Na in component background_lCa_current (picoA)"
    legend_algebraic[75] = "i_to_K in component transient_outward_current (picoA)"
    legend_algebraic[76] = "i_to_Na in component transient_outward_current (picoA)"
    legend_algebraic[72] = "i_Ks_K in component slow_time_dependent_potassium_current (picoA)"
    legend_algebraic[73] = "i_Ks_Na in component slow_time_dependent_potassium_current (picoA)"
    legend_algebraic[44] = "i_Na_K in component sodium_current (picoA)"
    legend_algebraic[49] = "i_CaL_K in component L_type_Ca_channel (picoA)"
    legend_algebraic[78] = "i_bNSC_K in component background_NSC_current (picoA)"
    legend_algebraic[83] = "i_lCa_K in component background_lCa_current (picoA)"
    legend_algebraic[47] = "i_CaL_Ca in component L_type_Ca_channel (picoA)"
    legend_algebraic[126] = "i_RyR in component RyR_channel (picoA)"
    legend_algebraic[115] = "i_SR_U in component SR_calcium_pump (picoA)"
    legend_algebraic[120] = "i_SR_L in component SR_L_current (picoA)"
    legend_algebraic[140] = "dCaidt in component NL_model (millimolar_per_millisecond)"
    legend_constants[13] = "CMDN_max in component internal_ion_concentrations (millimolar)"
    legend_constants[14] = "K_mCMDN in component internal_ion_concentrations (millimolar)"
    legend_states[3] = "Ca_Total in component internal_ion_concentrations (millimolar)"
    legend_algebraic[13] = "b1 in component internal_ion_concentrations (millimolar)"
    legend_algebraic[26] = "c1 in component internal_ion_concentrations (millimolar2)"
    legend_algebraic[32] = "CF_Na in component constant_field_equations (millimolar)"
    legend_algebraic[36] = "CF_Ca in component constant_field_equations (millimolar)"
    legend_algebraic[39] = "CF_K in component constant_field_equations (millimolar)"
    legend_states[4] = "ATPi in component ATP_production (millimolar)"
    legend_algebraic[117] = "dATPdt in component NL_model (millimolar_per_millisecond)"
    legend_constants[15] = "ProducingRate_Max in component ATP_production (per_millisecond)"
    legend_constants[16] = "Adenosine_Total in component ATP_production (millimolar)"
    legend_constants[17] = "P_Na in component sodium_current (picoA_per_millimolar)"
    legend_states[5] = "p_AP_Na in component sodium_current_voltage_dependent_gate (dimensionless)"
    legend_states[6] = "y in component sodium_current_ultra_slow_gate (dimensionless)"
    legend_algebraic[1] = "p_RI_Na in component sodium_current_voltage_dependent_gate (dimensionless)"
    legend_states[7] = "p_RP_Na in component sodium_current_voltage_dependent_gate (dimensionless)"
    legend_states[8] = "p_AI_Na in component sodium_current_voltage_dependent_gate (dimensionless)"
    legend_algebraic[14] = "k_RP_AP in component sodium_current_voltage_dependent_gate (per_millisecond)"
    legend_algebraic[27] = "k_AP_RP in component sodium_current_voltage_dependent_gate (per_millisecond)"
    legend_algebraic[37] = "k_RI_AI in component sodium_current_voltage_dependent_gate (per_millisecond)"
    legend_algebraic[33] = "k_AI_RI in component sodium_current_voltage_dependent_gate (per_millisecond)"
    legend_algebraic[30] = "k_AP_AI in component sodium_current_voltage_dependent_gate (per_millisecond)"
    legend_constants[18] = "k_AI_AP in component sodium_current_voltage_dependent_gate (per_millisecond)"
    legend_algebraic[40] = "k_RP_RI in component sodium_current_voltage_dependent_gate (per_millisecond)"
    legend_algebraic[43] = "k_RI_RP in component sodium_current_voltage_dependent_gate (per_millisecond)"
    legend_algebraic[2] = "alpha_y in component sodium_current_ultra_slow_gate (per_millisecond)"
    legend_algebraic[15] = "beta_y in component sodium_current_ultra_slow_gate (per_millisecond)"
    legend_algebraic[46] = "p_open_CaL in component L_type_Ca_channel (dimensionless)"
    legend_algebraic[52] = "CaDiadic in component L_type_Ca_channel_Ca_dependent_gate (picoA)"
    legend_constants[19] = "P_CaL in component L_type_Ca_channel (picoA_per_millimolar)"
    legend_states[9] = "p_AP_CaL in component L_type_Ca_channel_voltage_dependent_gate (dimensionless)"
    legend_states[10] = "p_U in component L_type_Ca_channel_Ca_dependent_gate (dimensionless)"
    legend_states[11] = "p_UCa in component L_type_Ca_channel_Ca_dependent_gate (dimensionless)"
    legend_states[12] = "y in component L_type_Ca_channel_ultra_slow_gate (dimensionless)"
    legend_algebraic[3] = "p_RI_CaL in component L_type_Ca_channel_voltage_dependent_gate (dimensionless)"
    legend_states[13] = "p_RP_CaL in component L_type_Ca_channel_voltage_dependent_gate (dimensionless)"
    legend_states[14] = "p_AI_CaL in component L_type_Ca_channel_voltage_dependent_gate (dimensionless)"
    legend_algebraic[16] = "k_RP_AP in component L_type_Ca_channel_voltage_dependent_gate (per_millisecond)"
    legend_algebraic[28] = "k_AP_RP in component L_type_Ca_channel_voltage_dependent_gate (per_millisecond)"
    legend_algebraic[31] = "k_RI_AI in component L_type_Ca_channel_voltage_dependent_gate (per_millisecond)"
    legend_algebraic[34] = "k_AI_RI in component L_type_Ca_channel_voltage_dependent_gate (per_millisecond)"
    legend_constants[20] = "k_AP_AI in component L_type_Ca_channel_voltage_dependent_gate (per_millisecond)"
    legend_constants[21] = "k_AI_AP in component L_type_Ca_channel_voltage_dependent_gate (per_millisecond)"
    legend_algebraic[38] = "k_RP_RI in component L_type_Ca_channel_voltage_dependent_gate (per_millisecond)"
    legend_algebraic[41] = "k_RI_RP in component L_type_Ca_channel_voltage_dependent_gate (per_millisecond)"
    legend_algebraic[51] = "iCaL in component L_type_Ca_channel_Ca_dependent_gate (picoA)"
    legend_algebraic[53] = "Cacm in component L_type_Ca_channel_Ca_dependent_gate (millimolar)"
    legend_algebraic[62] = "p_CCa in component L_type_Ca_channel_Ca_dependent_gate (dimensionless)"
    legend_states[15] = "p_C in component L_type_Ca_channel_Ca_dependent_gate (dimensionless)"
    legend_constants[22] = "k_CCa_UCa in component L_type_Ca_channel_Ca_dependent_gate (per_millisecond)"
    legend_constants[23] = "k_UCa_CCa in component L_type_Ca_channel_Ca_dependent_gate (per_millisecond)"
    legend_constants[24] = "k_C_U in component L_type_Ca_channel_Ca_dependent_gate (per_millisecond)"
    legend_constants[25] = "k_U_C in component L_type_Ca_channel_Ca_dependent_gate (per_millisecond)"
    legend_constants[92] = "k_UCa_U in component L_type_Ca_channel_Ca_dependent_gate (per_millisecond)"
    legend_constants[26] = "k_U_UCa in component L_type_Ca_channel_Ca_dependent_gate (per_millimolar_millisecond)"
    legend_constants[27] = "k_CCa_C in component L_type_Ca_channel_Ca_dependent_gate (per_millisecond)"
    legend_constants[28] = "k_C_CCa in component L_type_Ca_channel_Ca_dependent_gate (per_millimolar_millisecond)"
    legend_algebraic[55] = "CaEffC in component L_type_Ca_channel_Ca_dependent_gate (millimolar)"
    legend_algebraic[57] = "CaEffU in component L_type_Ca_channel_Ca_dependent_gate (millimolar)"
    legend_algebraic[60] = "k_UUCa_Ca in component L_type_Ca_channel_Ca_dependent_gate (per_millisecond)"
    legend_algebraic[58] = "k_CCCa_Ca in component L_type_Ca_channel_Ca_dependent_gate (per_millisecond)"
    legend_algebraic[4] = "alpha_y in component L_type_Ca_channel_ultra_slow_gate (per_millisecond)"
    legend_algebraic[17] = "beta_y in component L_type_Ca_channel_ultra_slow_gate (per_millisecond)"
    legend_constants[29] = "P_CaT in component T_type_Ca_channel (picoA_per_millimolar)"
    legend_states[16] = "y1 in component T_type_Ca_channel_y1_gate (dimensionless)"
    legend_states[17] = "y2 in component T_type_Ca_channel_y2_gate (dimensionless)"
    legend_algebraic[5] = "alpha_y1 in component T_type_Ca_channel_y1_gate (per_millisecond)"
    legend_algebraic[18] = "beta_y1 in component T_type_Ca_channel_y1_gate (per_millisecond)"
    legend_algebraic[6] = "alpha_y2 in component T_type_Ca_channel_y2_gate (per_millisecond)"
    legend_algebraic[19] = "beta_y2 in component T_type_Ca_channel_y2_gate (per_millisecond)"
    legend_algebraic[56] = "E_K in component time_independent_potassium_current (millivolt)"
    legend_constants[93] = "g_K1 in component time_independent_potassium_current (nanoS)"
    legend_constants[30] = "P_K1_0 in component time_independent_potassium_current (nanoS_per_picoF)"
    legend_algebraic[64] = "fO in component time_independent_potassium_current (dimensionless)"
    legend_algebraic[65] = "fO2 in component time_independent_potassium_current (dimensionless)"
    legend_algebraic[67] = "fO3 in component time_independent_potassium_current (dimensionless)"
    legend_algebraic[69] = "fO4 in component time_independent_potassium_current (dimensionless)"
    legend_algebraic[63] = "fB in component time_independent_potassium_current (dimensionless)"
    legend_algebraic[59] = "mu in component time_independent_potassium_current (per_millisecond)"
    legend_algebraic[61] = "lambda in component time_independent_potassium_current (per_millisecond)"
    legend_states[18] = "y in component time_independent_potassium_current_y_gate (dimensionless)"
    legend_algebraic[66] = "alpha_y in component time_independent_potassium_current_y_gate (per_millisecond)"
    legend_algebraic[68] = "beta_y in component time_independent_potassium_current_y_gate (per_millisecond)"
    legend_constants[94] = "g_Kr in component rapid_time_dependent_potassium_current (nanoS)"
    legend_constants[31] = "P_Kr in component rapid_time_dependent_potassium_current (nanoS_per_picoF)"
    legend_states[19] = "y1 in component rapid_time_dependent_potassium_current_y1_gate (dimensionless)"
    legend_states[20] = "y2 in component rapid_time_dependent_potassium_current_y2_gate (dimensionless)"
    legend_states[21] = "y3 in component rapid_time_dependent_potassium_current_y3_gate (dimensionless)"
    legend_algebraic[7] = "alpha_y1 in component rapid_time_dependent_potassium_current_y1_gate (per_millisecond)"
    legend_algebraic[20] = "beta_y1 in component rapid_time_dependent_potassium_current_y1_gate (per_millisecond)"
    legend_algebraic[8] = "alpha_y2 in component rapid_time_dependent_potassium_current_y2_gate (per_millisecond)"
    legend_algebraic[21] = "beta_y2 in component rapid_time_dependent_potassium_current_y2_gate (per_millisecond)"
    legend_algebraic[9] = "alpha_y3 in component rapid_time_dependent_potassium_current_y3_gate (per_millisecond)"
    legend_algebraic[22] = "beta_y3 in component rapid_time_dependent_potassium_current_y3_gate (per_millisecond)"
    legend_states[22] = "y1 in component slow_time_dependent_potassium_current_y1_gate (dimensionless)"
    legend_states[23] = "y2 in component slow_time_dependent_potassium_current_y2_gate (dimensionless)"
    legend_constants[32] = "P_Ks_K in component slow_time_dependent_potassium_current (picoA_per_millimolar)"
    legend_constants[33] = "P_Ks_Na in component slow_time_dependent_potassium_current (picoA_per_millimolar)"
    legend_algebraic[10] = "alpha_y1 in component slow_time_dependent_potassium_current_y1_gate (per_millisecond)"
    legend_algebraic[23] = "beta_y1 in component slow_time_dependent_potassium_current_y1_gate (per_millisecond)"
    legend_algebraic[35] = "alpha_y2 in component slow_time_dependent_potassium_current_y2_gate (per_millisecond)"
    legend_constants[34] = "beta_y2 in component slow_time_dependent_potassium_current_y2_gate (per_millisecond)"
    legend_states[24] = "y1 in component transient_outward_current_y1_gate (dimensionless)"
    legend_states[25] = "y2 in component transient_outward_current_y2_gate (dimensionless)"
    legend_constants[35] = "P_to_K in component transient_outward_current (picoA_per_millimolar)"
    legend_constants[36] = "P_to_Na in component transient_outward_current (picoA_per_millimolar)"
    legend_algebraic[11] = "alpha_y1 in component transient_outward_current_y1_gate (per_millisecond)"
    legend_algebraic[24] = "beta_y1 in component transient_outward_current_y1_gate (per_millisecond)"
    legend_algebraic[12] = "alpha_y2 in component transient_outward_current_y2_gate (per_millisecond)"
    legend_algebraic[25] = "beta_y2 in component transient_outward_current_y2_gate (per_millisecond)"
    legend_constants[37] = "P_bNSC in component background_NSC_current (picoA_per_millimolar)"
    legend_constants[95] = "P_Kpl in component background_Kpl_current (nanoS_per_millimolar)"
    legend_constants[38] = "P_lCa in component background_lCa_current (picoA_per_millimolar)"
    legend_algebraic[82] = "p_open in component background_lCa_current (dimensionless)"
    legend_algebraic[86] = "p_open in component background_KATP_current (dimensionless)"
    legend_constants[96] = "gamma in component background_KATP_current (nanoS)"
    legend_constants[39] = "P_KATP in component background_KATP_current (nanoS_per_picoF)"
    legend_constants[40] = "N in component background_KATP_current (picoF)"
    legend_constants[41] = "P_Cab in component background_Cab_current (picoA_per_millimolar)"
    legend_constants[97] = "p_E2Na in component sodium_calcium_exchanger (dimensionless)"
    legend_algebraic[90] = "p_E1Na in component sodium_calcium_exchanger (dimensionless)"
    legend_algebraic[91] = "p_E1Ca in component sodium_calcium_exchanger (dimensionless)"
    legend_constants[100] = "p_E2Ca in component sodium_calcium_exchanger (dimensionless)"
    legend_algebraic[92] = "k1 in component sodium_calcium_exchanger (per_millisecond)"
    legend_algebraic[93] = "k2 in component sodium_calcium_exchanger (per_millisecond)"
    legend_constants[42] = "k3 in component sodium_calcium_exchanger (per_millisecond)"
    legend_constants[43] = "k4 in component sodium_calcium_exchanger (per_millisecond)"
    legend_constants[44] = "Km_Nai in component sodium_calcium_exchanger (millimolar)"
    legend_constants[45] = "Km_Nao in component sodium_calcium_exchanger (millimolar)"
    legend_constants[46] = "Km_Cai in component sodium_calcium_exchanger (millimolar)"
    legend_constants[47] = "Km_Cao in component sodium_calcium_exchanger (millimolar)"
    legend_states[26] = "y in component sodium_calcium_exchanger_y_gate (dimensionless)"
    legend_constants[48] = "P_NaCa in component sodium_calcium_exchanger (picoA_per_picoF)"
    legend_constants[49] = "Partition in component sodium_calcium_exchanger (dimensionless)"
    legend_algebraic[95] = "alpha_y in component sodium_calcium_exchanger_y_gate (per_millisecond)"
    legend_algebraic[97] = "beta_y in component sodium_calcium_exchanger_y_gate (per_millisecond)"
    legend_algebraic[102] = "p_E2Na in component sodium_potassium_pump (dimensionless)"
    legend_algebraic[98] = "p_E1Na in component sodium_potassium_pump (dimensionless)"
    legend_algebraic[99] = "p_E1K in component sodium_potassium_pump (dimensionless)"
    legend_algebraic[104] = "p_E2K in component sodium_potassium_pump (dimensionless)"
    legend_algebraic[100] = "k1 in component sodium_potassium_pump (per_millisecond)"
    legend_constants[50] = "k2 in component sodium_potassium_pump (per_millisecond)"
    legend_constants[51] = "k3 in component sodium_potassium_pump (per_millisecond)"
    legend_constants[52] = "k4 in component sodium_potassium_pump (per_millisecond)"
    legend_constants[53] = "Km_Nai in component sodium_potassium_pump (millimolar)"
    legend_constants[54] = "Km_Nao in component sodium_potassium_pump (millimolar)"
    legend_constants[55] = "Km_Ki in component sodium_potassium_pump (millimolar)"
    legend_constants[56] = "Km_Ko in component sodium_potassium_pump (millimolar)"
    legend_constants[57] = "Km_ATP in component sodium_potassium_pump (millimolar)"
    legend_algebraic[101] = "Nao_Eff in component sodium_potassium_pump (millimolar)"
    legend_states[27] = "y in component sodium_potassium_pump_y_gate (dimensionless)"
    legend_constants[58] = "P_NaK in component sodium_potassium_pump (picoA_per_picoF)"
    legend_algebraic[109] = "alpha_y in component sodium_potassium_pump_y_gate (per_millisecond)"
    legend_algebraic[111] = "beta_y in component sodium_potassium_pump_y_gate (per_millisecond)"
    legend_algebraic[110] = "p_E2Ca in component SR_calcium_pump (dimensionless)"
    legend_algebraic[108] = "p_E1Ca in component SR_calcium_pump (dimensionless)"
    legend_algebraic[112] = "p_E1 in component SR_calcium_pump (dimensionless)"
    legend_algebraic[113] = "p_E2 in component SR_calcium_pump (dimensionless)"
    legend_constants[59] = "k1 in component SR_calcium_pump (per_millisecond)"
    legend_algebraic[114] = "k2 in component SR_calcium_pump (per_millisecond)"
    legend_constants[60] = "k3 in component SR_calcium_pump (per_millisecond)"
    legend_constants[61] = "k4 in component SR_calcium_pump (per_millisecond)"
    legend_constants[62] = "Km_CaSR in component SR_calcium_pump (millimolar)"
    legend_constants[63] = "Km_CaCyto in component SR_calcium_pump (millimolar)"
    legend_constants[64] = "Km_ATP in component SR_calcium_pump (millimolar)"
    legend_constants[65] = "i_max in component SR_calcium_pump (picoA)"
    legend_states[28] = "Caup in component Ca_concentrations_in_SR (millimolar)"
    legend_states[29] = "y in component SR_calcium_pump_y_gate (dimensionless)"
    legend_algebraic[116] = "alpha_y in component SR_calcium_pump_y_gate (per_millisecond)"
    legend_algebraic[118] = "beta_y in component SR_calcium_pump_y_gate (per_millisecond)"
    legend_constants[66] = "P_RyR in component RyR_channel (picoA_per_millimolar)"
    legend_algebraic[119] = "k1 in component RyR_channel (per_millisecond)"
    legend_algebraic[124] = "k2 in component RyR_channel (per_millisecond)"
    legend_algebraic[125] = "k3 in component RyR_channel (per_millisecond)"
    legend_constants[67] = "k4 in component RyR_channel (per_millisecond)"
    legend_states[30] = "p_open_RyR in component RyR_channel (dimensionless)"
    legend_states[31] = "p_close_RyR in component RyR_channel (dimensionless)"
    legend_algebraic[123] = "Carel in component Ca_concentrations_in_SR (millimolar)"
    legend_constants[68] = "Diadid_Factor in component RyR_channel (per_picoA_millisecond)"
    legend_algebraic[127] = "i_SR_T in component SR_T_current (picoA)"
    legend_constants[69] = "P_SR_T in component SR_T_current (picoA_per_millimolar)"
    legend_constants[70] = "P_SR_L in component SR_L_current (picoA_per_millimolar)"
    legend_states[32] = "Ca_Total in component Ca_concentrations_in_SR (millimolar)"
    legend_constants[71] = "V_rel in component Ca_concentrations_in_SR (micrometre3)"
    legend_constants[72] = "V_up in component Ca_concentrations_in_SR (micrometre3)"
    legend_constants[73] = "CSQN_max in component Ca_concentrations_in_SR (millimolar)"
    legend_constants[74] = "K_mCSQN in component Ca_concentrations_in_SR (millimolar)"
    legend_algebraic[121] = "b1 in component Ca_concentrations_in_SR (millimolar)"
    legend_algebraic[122] = "c1 in component Ca_concentrations_in_SR (millimolar2)"
    legend_constants[98] = "EffFraction in component NL_model (dimensionless)"
    legend_states[33] = "pCa in component NL_model (dimensionless)"
    legend_states[34] = "pCaCB in component NL_model (dimensionless)"
    legend_states[35] = "pCB in component NL_model (dimensionless)"
    legend_algebraic[130] = "p in component NL_model (dimensionless)"
    legend_constants[75] = "T_t in component NL_model (millimolar)"
    legend_algebraic[134] = "Q_a in component NL_model (per_millisecond)"
    legend_algebraic[132] = "Q_b in component NL_model (per_millisecond)"
    legend_algebraic[136] = "Q_r in component NL_model (per_millisecond)"
    legend_algebraic[137] = "Q_d in component NL_model (per_millisecond)"
    legend_algebraic[138] = "Q_d1 in component NL_model (per_millisecond)"
    legend_algebraic[139] = "Q_d2 in component NL_model (per_millisecond)"
    legend_constants[76] = "Y_1 in component NL_model (per_millimolar_millisecond)"
    legend_constants[77] = "Y_2 in component NL_model (per_millisecond)"
    legend_constants[78] = "Y_3 in component NL_model (per_millisecond)"
    legend_constants[79] = "Y_4 in component NL_model (per_millisecond)"
    legend_constants[80] = "Y_d in component NL_model (millisecond_per_micrometre2)"
    legend_constants[81] = "Z_1 in component NL_model (per_millisecond)"
    legend_constants[82] = "Z_2 in component NL_model (per_millisecond)"
    legend_constants[83] = "Z_3 in component NL_model (per_millimolar_millisecond)"
    legend_algebraic[128] = "h in component NL_model (micrometre)"
    legend_constants[84] = "L_a in component NL_model (micrometre)"
    legend_constants[85] = "L in component NL_model (micrometre)"
    legend_algebraic[133] = "ForceCB in component NL_model (mN_per_mm2)"
    legend_states[36] = "X in component NL_model (micrometre)"
    legend_algebraic[131] = "NewCBF in component NL_model (mN_per_mm2_micrometre)"
    legend_algebraic[129] = "CBBound in component NL_model (millimolar)"
    legend_constants[86] = "KForceEC in component NL_model (mN_per_mm2_micrometre5)"
    legend_constants[87] = "ZeroForceEL in component NL_model (micrometre)"
    legend_constants[88] = "KForceLinearEc in component NL_model (mN_per_mm2_micrometre)"
    legend_constants[89] = "ForceFactor in component NL_model (mN_per_mm2_micrometre_millimolar)"
    legend_constants[99] = "ForceEcomp in component NL_model (mN_per_mm2)"
    legend_constants[90] = "B in component NL_model (per_millisecond)"
    legend_constants[91] = "h_c in component NL_model (micrometre)"
    legend_algebraic[135] = "ForceExt in component NL_model (mN_per_mm2)"
    legend_rates[0] = "d/dt Vm in component membrane (millivolt)"
    legend_rates[1] = "d/dt Nai in component internal_ion_concentrations (millimolar)"
    legend_rates[2] = "d/dt Ki in component internal_ion_concentrations (millimolar)"
    legend_rates[3] = "d/dt Ca_Total in component internal_ion_concentrations (millimolar)"
    legend_rates[4] = "d/dt ATPi in component ATP_production (millimolar)"
    legend_rates[7] = "d/dt p_RP_Na in component sodium_current_voltage_dependent_gate (dimensionless)"
    legend_rates[5] = "d/dt p_AP_Na in component sodium_current_voltage_dependent_gate (dimensionless)"
    legend_rates[8] = "d/dt p_AI_Na in component sodium_current_voltage_dependent_gate (dimensionless)"
    legend_rates[6] = "d/dt y in component sodium_current_ultra_slow_gate (dimensionless)"
    legend_rates[13] = "d/dt p_RP_CaL in component L_type_Ca_channel_voltage_dependent_gate (dimensionless)"
    legend_rates[9] = "d/dt p_AP_CaL in component L_type_Ca_channel_voltage_dependent_gate (dimensionless)"
    legend_rates[14] = "d/dt p_AI_CaL in component L_type_Ca_channel_voltage_dependent_gate (dimensionless)"
    legend_rates[10] = "d/dt p_U in component L_type_Ca_channel_Ca_dependent_gate (dimensionless)"
    legend_rates[11] = "d/dt p_UCa in component L_type_Ca_channel_Ca_dependent_gate (dimensionless)"
    legend_rates[15] = "d/dt p_C in component L_type_Ca_channel_Ca_dependent_gate (dimensionless)"
    legend_rates[12] = "d/dt y in component L_type_Ca_channel_ultra_slow_gate (dimensionless)"
    legend_rates[16] = "d/dt y1 in component T_type_Ca_channel_y1_gate (dimensionless)"
    legend_rates[17] = "d/dt y2 in component T_type_Ca_channel_y2_gate (dimensionless)"
    legend_rates[18] = "d/dt y in component time_independent_potassium_current_y_gate (dimensionless)"
    legend_rates[19] = "d/dt y1 in component rapid_time_dependent_potassium_current_y1_gate (dimensionless)"
    legend_rates[20] = "d/dt y2 in component rapid_time_dependent_potassium_current_y2_gate (dimensionless)"
    legend_rates[21] = "d/dt y3 in component rapid_time_dependent_potassium_current_y3_gate (dimensionless)"
    legend_rates[22] = "d/dt y1 in component slow_time_dependent_potassium_current_y1_gate (dimensionless)"
    legend_rates[23] = "d/dt y2 in component slow_time_dependent_potassium_current_y2_gate (dimensionless)"
    legend_rates[24] = "d/dt y1 in component transient_outward_current_y1_gate (dimensionless)"
    legend_rates[25] = "d/dt y2 in component transient_outward_current_y2_gate (dimensionless)"
    legend_rates[26] = "d/dt y in component sodium_calcium_exchanger_y_gate (dimensionless)"
    legend_rates[27] = "d/dt y in component sodium_potassium_pump_y_gate (dimensionless)"
    legend_rates[29] = "d/dt y in component SR_calcium_pump_y_gate (dimensionless)"
    legend_rates[30] = "d/dt p_open_RyR in component RyR_channel (dimensionless)"
    legend_rates[31] = "d/dt p_close_RyR in component RyR_channel (dimensionless)"
    legend_rates[32] = "d/dt Ca_Total in component Ca_concentrations_in_SR (millimolar)"
    legend_rates[28] = "d/dt Caup in component Ca_concentrations_in_SR (millimolar)"
    legend_rates[36] = "d/dt X in component NL_model (micrometre)"
    legend_rates[33] = "d/dt pCa in component NL_model (dimensionless)"
    legend_rates[34] = "d/dt pCaCB in component NL_model (dimensionless)"
    legend_rates[35] = "d/dt pCB in component NL_model (dimensionless)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = -85.95752434460744
    constants[0] = 8.3143
    constants[1] = 310
    constants[2] = 96.4867
    constants[3] = 132
    constants[4] = 50
    constants[5] = 1000000
    constants[6] = 400
    constants[7] = 2
    constants[8] = -4000
    constants[9] = 140
    constants[10] = 1.8
    constants[11] = 5.4
    states[1] = 4.925761439682025
    states[2] = 143.1837333000449
    constants[12] = 8000
    constants[13] = 0.05
    constants[14] = 0.00238
    states[3] = 4.0180173572968586e-4
    states[4] = 4.657102729020499
    constants[15] = 0.003
    constants[16] = 5
    constants[17] = 2860
    states[5] = 1.779648367445368e-5
    states[6] = 0.5861887862983165
    states[7] = 0.3556412697995689
    states[8] = 0.40285968661346977
    constants[18] = 0.0000875
    constants[19] = 8712
    states[9] = 1.5445004166497696e-6
    states[10] = 0.17246483915629204
    states[11] = 6.098246017787626e-5
    states[12] = 0.9985266538252986
    states[13] = 0.9968480629364956
    states[14] = 8.77325391245903e-4
    constants[20] = 0.004
    constants[21] = 0.001
    states[15] = 0.4250747299372254
    constants[22] = 0.0003
    constants[23] = 0.35
    constants[24] = 0.143
    constants[25] = 0.35
    constants[26] = 6.954
    constants[27] = 0.0042
    constants[28] = 6.954
    constants[29] = 612
    states[16] = 1.6882718240109127e-5
    states[17] = 0.8585352091865849
    constants[30] = 1.146
    states[18] = 0.6080573900752752
    constants[31] = 0.00864
    states[19] = 0.0018339931180983765
    states[20] = 0.20443083454225305
    states[21] = 0.967887666264921
    states[22] = 0.09738789658609195
    states[23] = 0.09745345578743213
    constants[32] = 5.04
    constants[33] = 0.2016
    constants[34] = 0.004444
    states[24] = 7.956883250874798e-4
    states[25] = 0.9999125083105881
    constants[35] = 0.033
    constants[36] = 0.00297
    constants[37] = 0.385
    constants[38] = 0.11
    constants[39] = 0.0236
    constants[40] = 2333
    constants[41] = 0.04
    constants[42] = 1
    constants[43] = 1
    constants[44] = 8.75
    constants[45] = 87.5
    constants[46] = 0.00138
    constants[47] = 1.38
    states[26] = 0.9891789193465331
    constants[48] = 6.81
    constants[49] = 0.32
    constants[50] = 0.04
    constants[51] = 0.01
    constants[52] = 0.165
    constants[53] = 4.05
    constants[54] = 69.8
    constants[55] = 32.88
    constants[56] = 0.258
    constants[57] = 0.094
    states[27] = 0.5910747147428818
    constants[58] = 21
    constants[59] = 0.01
    constants[60] = 1
    constants[61] = 0.01
    constants[62] = 0.08
    constants[63] = 0.0008
    constants[64] = 0.1
    constants[65] = 162500
    states[28] = 2.611712901567567
    states[29] = 0.46108441538480216
    constants[66] = 62000
    constants[67] = 0.000849
    states[30] = 3.4314360001543243e-4
    states[31] = 0.19135178123107768
    constants[68] = -150
    constants[69] = 386
    constants[70] = 459
    states[32] = 9.455741736977666
    constants[71] = 160
    constants[72] = 400
    constants[73] = 10
    constants[74] = 0.8
    states[33] = 0.02490898775497523
    states[34] = 0.001990153835322864
    states[35] = 4.2941813853474524e-4
    constants[75] = 0.07
    constants[76] = 39
    constants[77] = 0.0039
    constants[78] = 0.03
    constants[79] = 0.12
    constants[80] = 0.027
    constants[81] = 0.03
    constants[82] = 0.0039
    constants[83] = 1560
    constants[84] = 1.17
    constants[85] = 0.9623799975411884
    states[36] = 0.9573749975411884
    constants[86] = 140000
    constants[87] = 0.97
    constants[88] = 200
    constants[89] = 1800000
    constants[90] = 1.2
    constants[91] = 0.005
    constants[92] = (constants[27]*constants[24]*constants[26]*constants[23])/(constants[25]*constants[28]*constants[22])
    constants[93] = constants[30]*constants[3]*(power(constants[11]/5.40000, 0.400000))
    constants[94] = constants[31]*constants[3]*(power(constants[11]/5.40000, 0.200000))
    constants[95] = 0.000110000*(power(constants[11]/5.40000, 0.160000))
    constants[96] = constants[39]*constants[40]*(power(constants[11]/1.00000, 0.240000))
    constants[97] = 1.00000/(1.00000+(power(constants[45]/constants[9], 3.00000))*(1.00000+constants[10]/constants[47]))
    constants[98] = exp(-20.0000*(power(constants[85]-constants[84], 2.00000)))
    constants[99] = constants[86]*(power(constants[87]-constants[85], 5.00000))+constants[88]*(constants[87]-constants[85])
    constants[100] = 1.00000/(1.00000+(constants[47]/constants[10])*(1.00000+power(constants[9]/constants[45], 3.00000)))
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[2] = 1.00000/(9.00000e+09*exp(states[0]/5.00000)+8000.00*exp(states[0]/100.000))
    algebraic[15] = 1.00000/(0.0140000*exp(-states[0]/5.00000)+4000.00*exp(-states[0]/100.000))
    rates[6] = algebraic[2]*(1.00000-states[6])-algebraic[15]*states[6]
    algebraic[4] = 1.00000/(250000.*exp(states[0]/9.00000)+58.0000*exp(states[0]/65.0000))
    algebraic[17] = 1.00000/(1800.00*exp(-states[0]/14.0000)+66.0000*exp(-states[0]/65.0000))
    rates[12] = algebraic[4]*(1.00000-states[12])-algebraic[17]*states[12]
    algebraic[5] = 1.00000/(0.0190000*exp(-states[0]/5.60000)+0.820000*exp(-states[0]/250.000))
    algebraic[18] = 1.00000/(40.0000*exp(states[0]/6.30000)+1.50000*exp(states[0]/10000.0))
    rates[16] = algebraic[5]*(1.00000-states[16])-algebraic[18]*states[16]
    algebraic[6] = 1.00000/(62000.0*exp(states[0]/10.1000)+30.0000*exp(states[0]/3000.00))
    algebraic[19] = 1.00000/(0.000600000*exp(-states[0]/6.70000)+1.20000*exp(-states[0]/25.0000))
    rates[17] = algebraic[6]*(1.00000-states[17])-algebraic[19]*states[17]
    algebraic[7] = 1.00000/(20.0000*exp(-states[0]/11.5000)+5.00000*exp(-states[0]/300.000))
    algebraic[20] = 1.00000/(160.000*exp(states[0]/28.0000)+200.000*exp(states[0]/1000.00))+1.00000/(2500.00*exp(states[0]/20.0000))
    rates[19] = algebraic[7]*(1.00000-states[19])-algebraic[20]*states[19]
    algebraic[8] = 1.00000/(200.000*exp(-states[0]/13.0000)+20.0000*exp(-states[0]/300.000))
    algebraic[21] = 1.00000/(1600.00*exp(states[0]/28.0000)+2000.00*exp(states[0]/1000.00))+1.00000/(10000.0*exp(states[0]/20.0000))
    rates[20] = algebraic[8]*(1.00000-states[20])-algebraic[21]*states[20]
    algebraic[9] = 1.00000/(10.0000*exp(states[0]/17.0000)+2.50000*exp(states[0]/300.000))
    algebraic[22] = 1.00000/(0.350000*exp(-states[0]/17.0000)+2.00000*exp(-states[0]/150.000))
    rates[21] = algebraic[9]*(1.00000-states[21])-algebraic[22]*states[21]
    algebraic[10] = 1.00000/(85.0000*exp(-states[0]/10.5000)+370.000*exp(-states[0]/62.0000))
    algebraic[23] = 1.00000/(1450.00*exp(states[0]/20.0000)+260.000*exp(states[0]/100.000))
    rates[22] = algebraic[10]*(1.00000-states[22])-algebraic[23]*states[22]
    algebraic[11] = 1.00000/(11.0000*exp(-states[0]/28.0000)+0.200000*exp(-states[0]/400.000))
    algebraic[24] = 1.00000/(4.40000*exp(states[0]/16.0000)+0.200000*exp(states[0]/500.000))
    rates[24] = algebraic[11]*(1.00000-states[24])-algebraic[24]*states[24]
    algebraic[12] = (0.00380000*exp(-(states[0]+13.5000)/11.3000))/(1.00000+0.0513350*exp(-(states[0]+13.5000)/11.3000))
    algebraic[25] = (0.00380000*exp((states[0]+13.5000)/11.3000))/(1.00000+0.0670830*exp((states[0]+13.5000)/11.3000))
    rates[25] = algebraic[12]*(1.00000-states[25])-algebraic[25]*states[25]
    algebraic[16] = 1.00000/(0.270000*exp(-states[0]/5.90000)+1.50000*exp(-states[0]/65.0000))
    algebraic[28] = 1.00000/(480.000*exp(states[0]/7.00000)+2.20000*exp(states[0]/65.0000))
    rates[9] = (states[13]*algebraic[16]+states[14]*constants[21])-states[9]*(algebraic[28]+constants[20])
    algebraic[14] = 1.00000/(0.102700*exp(-states[0]/8.00000)+0.250000*exp(-states[0]/50.0000))
    algebraic[27] = 1.00000/(26.0000*exp(states[0]/17.0000)+0.0200000*exp(states[0]/800.000))
    algebraic[30] = 1.00000/(0.800000*exp(-states[0]/400.000))
    rates[5] = (states[7]*algebraic[14]+states[8]*constants[18])-states[5]*(algebraic[27]+algebraic[30])
    algebraic[3] = ((1.00000-states[9])-states[13])-states[14]
    algebraic[31] = 1.00000/(0.00180000*exp(-states[0]/7.40000)+2.00000*exp(-states[0]/100.000))
    algebraic[34] = 1.00000/(2.20000e+06*exp(states[0]/7.40000)+11.0000*exp(states[0]/100.000))
    rates[14] = (algebraic[3]*algebraic[31]+states[9]*constants[20])-states[14]*(algebraic[34]+constants[21])
    algebraic[13] = (constants[13]-states[3])+constants[14]
    algebraic[26] = constants[14]*states[3]
    algebraic[29] = (power(power(algebraic[13], 2.00000)+4.00000*algebraic[26], 1.0/2)-algebraic[13])/2.00000
    algebraic[35] = 3.70000*algebraic[29]
    rates[23] = algebraic[35]*(1.00000-states[23])-constants[34]*states[23]
    algebraic[1] = ((1.00000-states[7])-states[5])-states[8]
    algebraic[37] = 1.00000/(0.000102700*exp(-states[0]/8.00000)+5.00000*exp(-states[0]/400.000))
    algebraic[33] = 1.00000/(1300.00*exp(states[0]/20.0000)+0.0400000*exp(states[0]/800.000))
    rates[8] = (algebraic[1]*algebraic[37]+states[5]*algebraic[30])-states[8]*(algebraic[33]+constants[18])
    algebraic[38] = 0.0400000/(1.00000+(constants[21]*algebraic[28]*algebraic[31])/(constants[20]*algebraic[16]*algebraic[34]))
    algebraic[41] = 0.0400000-algebraic[38]
    rates[13] = (states[9]*algebraic[28]+algebraic[3]*algebraic[41])-states[13]*(algebraic[38]+algebraic[16])
    algebraic[40] = 0.0100000/(1.00000+(constants[18]*algebraic[27]*algebraic[37])/(algebraic[30]*algebraic[14]*algebraic[33]))
    algebraic[43] = 0.0100000-algebraic[40]
    rates[7] = (states[5]*algebraic[27]+algebraic[1]*algebraic[43])-states[7]*(algebraic[40]+algebraic[14])
    algebraic[36] = custom_piecewise([equal(states[0] , 0.00000), -constants[10] , True, (((2.00000*constants[2]*states[0])/(constants[0]*constants[1]))*(algebraic[29]-constants[10]*exp((-2.00000*constants[2]*states[0])/(constants[0]*constants[1]))))/(1.00000-exp((-2.00000*constants[2]*states[0])/(constants[0]*constants[1])))])
    algebraic[51] = 0.0676000*algebraic[36]
    algebraic[53] = algebraic[29]-0.300000*algebraic[51]
    algebraic[55] = algebraic[53]*states[9]
    algebraic[57] = algebraic[55]+algebraic[29]*(1.00000-states[9])
    algebraic[60] = constants[26]*algebraic[57]
    rates[10] = (states[15]*constants[24]+states[11]*constants[92])-states[10]*(algebraic[60]+constants[25])
    algebraic[62] = ((1.00000-states[15])-states[10])-states[11]
    rates[11] = (states[10]*algebraic[60]+algebraic[62]*constants[22])-states[11]*(constants[23]+constants[92])
    rates[15] = (algebraic[62]*constants[27]+states[10]*constants[25])-states[15]*(constants[24]+constants[28]*algebraic[53]*states[9])
    algebraic[56] = ((constants[0]*constants[1])/constants[2])*log(constants[11]/states[2])
    algebraic[66] = 1.00000/(8000.00*exp(((states[0]-algebraic[56])-97.0000)/8.50000)+7.00000*exp(((states[0]-algebraic[56])-97.0000)/300.000))
    algebraic[59] = (0.750000*exp(0.0350000*((states[0]-algebraic[56])-10.0000)))/(1.00000+exp(0.0150000*((states[0]-algebraic[56])-140.000)))
    algebraic[61] = (3.00000*exp(-0.0480000*((states[0]-algebraic[56])-10.0000))*(1.00000+exp(0.0640000*((states[0]-algebraic[56])-38.0000))))/(1.00000+exp(0.0300000*((states[0]-algebraic[56])-70.0000)))
    algebraic[64] = algebraic[61]/(algebraic[59]+algebraic[61])
    algebraic[68] = ((power(algebraic[64], 4.00000))*1.00000)/(0.000140000*exp(-((states[0]-algebraic[56])-97.0000)/9.10000)+0.200000*exp(-((states[0]-algebraic[56])-97.0000)/500.000))
    rates[18] = algebraic[66]*(1.00000-states[18])-algebraic[68]*states[18]
    algebraic[93] = 1.00000*exp(((constants[49]-1.00000)*constants[2]*states[0])/(constants[0]*constants[1]))
    algebraic[95] = algebraic[93]*constants[97]+constants[43]*constants[100]
    algebraic[90] = 1.00000/(1.00000+(power(constants[44]/states[1], 3.00000))*(1.00000+algebraic[29]/constants[46]))
    algebraic[91] = 1.00000/(1.00000+(constants[46]/algebraic[29])*(1.00000+power(states[1]/constants[44], 3.00000)))
    algebraic[92] = 1.00000*exp((constants[49]*constants[2]*states[0])/(constants[0]*constants[1]))
    algebraic[97] = algebraic[92]*algebraic[90]+constants[42]*algebraic[91]
    rates[26] = algebraic[95]*(1.00000-states[26])-algebraic[97]*states[26]
    algebraic[0] = custom_piecewise([greater_equal(voi , constants[4]) & less_equal(voi , constants[5]) & less_equal((voi-constants[4])-floor((voi-constants[4])/constants[6])*constants[6] , constants[7]), constants[8] , True, 0.00000])
    algebraic[32] = custom_piecewise([equal(states[0] , 0.00000), -constants[9] , True, (((constants[2]*states[0])/(constants[0]*constants[1]))*(states[1]-constants[9]*exp((-constants[2]*states[0])/(constants[0]*constants[1]))))/(1.00000-exp((-constants[2]*states[0])/(constants[0]*constants[1])))])
    algebraic[79] = constants[37]*algebraic[32]
    algebraic[39] = custom_piecewise([equal(states[0] , 0.00000), states[2] , True, (((constants[2]*states[0])/(constants[0]*constants[1]))*(states[2]-constants[11]*exp((-constants[2]*states[0])/(constants[0]*constants[1]))))/(1.00000-exp((-constants[2]*states[0])/(constants[0]*constants[1])))])
    algebraic[78] = 0.400000*constants[37]*algebraic[39]
    algebraic[80] = algebraic[78]+algebraic[79]
    algebraic[88] = constants[41]*algebraic[36]
    algebraic[81] = custom_piecewise([equal(states[0] , -3.00000), constants[95]*algebraic[39]*13.0077 , True, (constants[95]*algebraic[39]*(states[0]+3.00000))/(1.00000-exp(-(states[0]+3.00000)/13.0000))])
    algebraic[82] = 1.00000/(1.00000+power(0.00120000/algebraic[29], 3.00000))
    algebraic[84] = constants[38]*algebraic[32]*algebraic[82]
    algebraic[83] = constants[38]*algebraic[39]*algebraic[82]
    algebraic[85] = algebraic[83]+algebraic[84]
    algebraic[86] = 0.800000/(1.00000+power(states[4]/0.100000, 2.00000))
    algebraic[87] = constants[96]*(states[0]-algebraic[56])*algebraic[86]
    algebraic[89] = algebraic[80]+algebraic[88]+algebraic[81]+algebraic[85]+algebraic[87]
    algebraic[42] = constants[17]*algebraic[32]*states[5]*states[6]
    algebraic[44] = 0.100000*constants[17]*algebraic[39]*states[5]*states[6]
    algebraic[45] = algebraic[42]+algebraic[44]
    algebraic[46] = (states[9]*(states[10]+states[11])*states[12])/(1.00000+power(1.40000/states[4], 3.00000))
    algebraic[48] = 1.85000e-05*constants[19]*algebraic[32]*algebraic[46]
    algebraic[49] = 0.000365000*constants[19]*algebraic[39]*algebraic[46]
    algebraic[47] = constants[19]*algebraic[36]*algebraic[46]
    algebraic[50] = algebraic[48]+algebraic[47]+algebraic[49]
    algebraic[54] = constants[29]*algebraic[36]*states[16]*states[17]
    algebraic[63] = algebraic[59]/(algebraic[59]+algebraic[61])
    algebraic[65] = 2.00000*(power(algebraic[64], 2.00000))*(power(algebraic[63], 2.00000))
    algebraic[67] = (8.00000/3.00000)*(power(algebraic[64], 3.00000))*algebraic[63]
    algebraic[69] = power(algebraic[64], 4.00000)
    algebraic[70] = constants[93]*(states[0]-algebraic[56])*(algebraic[69]+algebraic[67]+algebraic[65])*states[18]
    algebraic[71] = constants[94]*(states[0]-algebraic[56])*(0.600000*states[19]+0.400000*states[20])*states[21]
    algebraic[72] = constants[32]*algebraic[39]*(power(states[22], 2.00000))*(0.900000*states[23]+0.100000)
    algebraic[73] = constants[33]*algebraic[32]*(power(states[22], 2.00000))*(0.900000*states[23]+0.100000)
    algebraic[74] = algebraic[73]+algebraic[72]
    algebraic[75] = constants[35]*algebraic[39]*(power(states[24], 3.00000))*states[25]
    algebraic[76] = constants[36]*algebraic[32]*(power(states[24], 3.00000))*states[25]
    algebraic[77] = algebraic[76]+algebraic[75]
    algebraic[101] = constants[9]*exp((-0.820000*constants[2]*states[0])/(constants[0]*constants[1]))
    algebraic[102] = 1.00000/(1.00000+(power(constants[54]/algebraic[101], 1.06000))*(1.00000+power(constants[11]/constants[56], 1.12000)))
    algebraic[98] = 1.00000/(1.00000+(power(constants[53]/states[1], 1.06000))*(1.00000+power(states[2]/constants[55], 1.12000)))
    algebraic[100] = 0.370000/(1.00000+constants[57]/states[4])
    algebraic[103] = constants[58]*constants[3]*1.00000*(algebraic[100]*algebraic[98]*states[27]-constants[50]*algebraic[102]*(1.00000-states[27]))
    algebraic[94] = constants[48]*constants[3]*1.00000*(algebraic[92]*algebraic[90]*states[26]-algebraic[93]*constants[97]*(1.00000-states[26]))
    algebraic[105] = algebraic[45]+algebraic[50]+algebraic[54]+algebraic[70]+algebraic[71]+algebraic[74]+algebraic[77]+algebraic[89]+algebraic[103]+algebraic[94]
    rates[0] = -(algebraic[105]+algebraic[0])/constants[3]
    algebraic[106] = algebraic[42]+algebraic[73]+algebraic[76]+algebraic[48]+algebraic[79]+algebraic[84]+3.00000*algebraic[103]+3.00000*algebraic[94]
    rates[1] = -algebraic[106]/(constants[2]*constants[12])
    algebraic[107] = (algebraic[70]+algebraic[71]+algebraic[75]+algebraic[87]+algebraic[72]+algebraic[44]+algebraic[49]+algebraic[78]+algebraic[83]+algebraic[81])-2.00000*algebraic[103]
    rates[2] = -(algebraic[107]+algebraic[0])/(constants[2]*constants[12])
    algebraic[104] = 1.00000/(1.00000+(power(constants[56]/constants[11], 1.12000))*(1.00000+power(algebraic[101]/constants[54], 1.06000)))
    algebraic[109] = constants[50]*algebraic[102]+constants[52]*algebraic[104]
    algebraic[99] = 1.00000/(1.00000+(power(constants[55]/states[2], 1.12000))*(1.00000+power(states[1]/constants[53], 1.06000)))
    algebraic[111] = algebraic[100]*algebraic[98]+constants[51]*algebraic[99]
    rates[27] = algebraic[109]*(1.00000-states[27])-algebraic[111]*states[27]
    algebraic[110] = 1.00000/(1.00000+constants[63]/algebraic[29])
    algebraic[108] = 1.00000/(1.00000+constants[62]/states[28])
    algebraic[114] = 1.00000/(1.00000+constants[64]/states[4])
    algebraic[115] = constants[65]*1.00000*(constants[59]*algebraic[108]*states[29]-algebraic[114]*algebraic[110]*(1.00000-states[29]))
    algebraic[117] = -0.400000*states[34]*constants[75]
    rates[4] = ((constants[15]*(constants[16]-states[4])+algebraic[117])-algebraic[103]/(constants[2]*constants[12]))+algebraic[115]/(4.00000*constants[2]*constants[12])
    algebraic[113] = 1.00000-algebraic[110]
    algebraic[116] = algebraic[114]*algebraic[110]+constants[61]*algebraic[113]
    algebraic[112] = 1.00000-algebraic[108]
    algebraic[118] = constants[59]*algebraic[108]+constants[60]*algebraic[112]
    rates[29] = algebraic[116]*(1.00000-states[29])-algebraic[118]*states[29]
    algebraic[52] = algebraic[51]*algebraic[46]
    algebraic[119] = 280000.*(power(algebraic[29]/1.00000, 2.00000))+constants[68]*algebraic[52]
    algebraic[121] = (constants[73]-states[32])+constants[74]
    algebraic[122] = constants[74]*states[32]
    algebraic[123] = (power(power(algebraic[121], 2.00000)+4.00000*algebraic[122], 1.0/2)-algebraic[121])/2.00000
    algebraic[124] = 0.0800000/(1.00000+0.360000/algebraic[123])
    rates[30] = states[31]*algebraic[119]-states[30]*algebraic[124]
    algebraic[125] = 0.000377000*(power(algebraic[123]/1.00000, 2.00000))
    rates[31] = algebraic[125]*(1.00000-(states[30]+states[31]))-(algebraic[119]+constants[67])*states[31]
    algebraic[126] = constants[66]*(algebraic[123]-algebraic[29])*states[30]
    algebraic[127] = constants[69]*(states[28]-algebraic[123])
    rates[32] = (algebraic[127]-algebraic[126])/(2.00000*constants[2]*constants[71])
    algebraic[120] = constants[70]*(states[28]-algebraic[29])
    rates[28] = ((-algebraic[115]-algebraic[127])-algebraic[120])/(2.00000*constants[2]*constants[72])
    algebraic[134] = constants[77]*states[33]*constants[98]-constants[82]*states[34]
    algebraic[130] = ((1.00000-states[33])-states[34])-states[35]
    algebraic[132] = constants[76]*algebraic[29]*algebraic[130]-constants[81]*states[33]
    rates[33] = algebraic[132]-algebraic[134]
    algebraic[128] = constants[85]-states[36]
    rates[36] = constants[90]*(algebraic[128]-constants[91])
    algebraic[136] = constants[78]*states[34]-constants[83]*states[35]*algebraic[29]
    algebraic[139] = constants[80]*(power(rates[36], 2.00000))*states[34]
    rates[34] = (algebraic[134]-algebraic[136])-algebraic[139]
    algebraic[137] = constants[79]*states[35]
    algebraic[138] = constants[80]*(power(rates[36], 2.00000))*states[35]
    rates[35] = (algebraic[136]-algebraic[137])-algebraic[138]
    algebraic[96] = (algebraic[47]+algebraic[54]+algebraic[88])-2.00000*algebraic[94]
    algebraic[140] = constants[75]*((algebraic[139]+algebraic[136])-algebraic[132])
    rates[3] = -(((algebraic[96]-algebraic[115])-algebraic[126])-algebraic[120])/(2.00000*constants[2]*constants[12])+algebraic[140]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[2] = 1.00000/(9.00000e+09*exp(states[0]/5.00000)+8000.00*exp(states[0]/100.000))
    algebraic[15] = 1.00000/(0.0140000*exp(-states[0]/5.00000)+4000.00*exp(-states[0]/100.000))
    algebraic[4] = 1.00000/(250000.*exp(states[0]/9.00000)+58.0000*exp(states[0]/65.0000))
    algebraic[17] = 1.00000/(1800.00*exp(-states[0]/14.0000)+66.0000*exp(-states[0]/65.0000))
    algebraic[5] = 1.00000/(0.0190000*exp(-states[0]/5.60000)+0.820000*exp(-states[0]/250.000))
    algebraic[18] = 1.00000/(40.0000*exp(states[0]/6.30000)+1.50000*exp(states[0]/10000.0))
    algebraic[6] = 1.00000/(62000.0*exp(states[0]/10.1000)+30.0000*exp(states[0]/3000.00))
    algebraic[19] = 1.00000/(0.000600000*exp(-states[0]/6.70000)+1.20000*exp(-states[0]/25.0000))
    algebraic[7] = 1.00000/(20.0000*exp(-states[0]/11.5000)+5.00000*exp(-states[0]/300.000))
    algebraic[20] = 1.00000/(160.000*exp(states[0]/28.0000)+200.000*exp(states[0]/1000.00))+1.00000/(2500.00*exp(states[0]/20.0000))
    algebraic[8] = 1.00000/(200.000*exp(-states[0]/13.0000)+20.0000*exp(-states[0]/300.000))
    algebraic[21] = 1.00000/(1600.00*exp(states[0]/28.0000)+2000.00*exp(states[0]/1000.00))+1.00000/(10000.0*exp(states[0]/20.0000))
    algebraic[9] = 1.00000/(10.0000*exp(states[0]/17.0000)+2.50000*exp(states[0]/300.000))
    algebraic[22] = 1.00000/(0.350000*exp(-states[0]/17.0000)+2.00000*exp(-states[0]/150.000))
    algebraic[10] = 1.00000/(85.0000*exp(-states[0]/10.5000)+370.000*exp(-states[0]/62.0000))
    algebraic[23] = 1.00000/(1450.00*exp(states[0]/20.0000)+260.000*exp(states[0]/100.000))
    algebraic[11] = 1.00000/(11.0000*exp(-states[0]/28.0000)+0.200000*exp(-states[0]/400.000))
    algebraic[24] = 1.00000/(4.40000*exp(states[0]/16.0000)+0.200000*exp(states[0]/500.000))
    algebraic[12] = (0.00380000*exp(-(states[0]+13.5000)/11.3000))/(1.00000+0.0513350*exp(-(states[0]+13.5000)/11.3000))
    algebraic[25] = (0.00380000*exp((states[0]+13.5000)/11.3000))/(1.00000+0.0670830*exp((states[0]+13.5000)/11.3000))
    algebraic[16] = 1.00000/(0.270000*exp(-states[0]/5.90000)+1.50000*exp(-states[0]/65.0000))
    algebraic[28] = 1.00000/(480.000*exp(states[0]/7.00000)+2.20000*exp(states[0]/65.0000))
    algebraic[14] = 1.00000/(0.102700*exp(-states[0]/8.00000)+0.250000*exp(-states[0]/50.0000))
    algebraic[27] = 1.00000/(26.0000*exp(states[0]/17.0000)+0.0200000*exp(states[0]/800.000))
    algebraic[30] = 1.00000/(0.800000*exp(-states[0]/400.000))
    algebraic[3] = ((1.00000-states[9])-states[13])-states[14]
    algebraic[31] = 1.00000/(0.00180000*exp(-states[0]/7.40000)+2.00000*exp(-states[0]/100.000))
    algebraic[34] = 1.00000/(2.20000e+06*exp(states[0]/7.40000)+11.0000*exp(states[0]/100.000))
    algebraic[13] = (constants[13]-states[3])+constants[14]
    algebraic[26] = constants[14]*states[3]
    algebraic[29] = (power(power(algebraic[13], 2.00000)+4.00000*algebraic[26], 1.0/2)-algebraic[13])/2.00000
    algebraic[35] = 3.70000*algebraic[29]
    algebraic[1] = ((1.00000-states[7])-states[5])-states[8]
    algebraic[37] = 1.00000/(0.000102700*exp(-states[0]/8.00000)+5.00000*exp(-states[0]/400.000))
    algebraic[33] = 1.00000/(1300.00*exp(states[0]/20.0000)+0.0400000*exp(states[0]/800.000))
    algebraic[38] = 0.0400000/(1.00000+(constants[21]*algebraic[28]*algebraic[31])/(constants[20]*algebraic[16]*algebraic[34]))
    algebraic[41] = 0.0400000-algebraic[38]
    algebraic[40] = 0.0100000/(1.00000+(constants[18]*algebraic[27]*algebraic[37])/(algebraic[30]*algebraic[14]*algebraic[33]))
    algebraic[43] = 0.0100000-algebraic[40]
    algebraic[36] = custom_piecewise([equal(states[0] , 0.00000), -constants[10] , True, (((2.00000*constants[2]*states[0])/(constants[0]*constants[1]))*(algebraic[29]-constants[10]*exp((-2.00000*constants[2]*states[0])/(constants[0]*constants[1]))))/(1.00000-exp((-2.00000*constants[2]*states[0])/(constants[0]*constants[1])))])
    algebraic[51] = 0.0676000*algebraic[36]
    algebraic[53] = algebraic[29]-0.300000*algebraic[51]
    algebraic[55] = algebraic[53]*states[9]
    algebraic[57] = algebraic[55]+algebraic[29]*(1.00000-states[9])
    algebraic[60] = constants[26]*algebraic[57]
    algebraic[62] = ((1.00000-states[15])-states[10])-states[11]
    algebraic[56] = ((constants[0]*constants[1])/constants[2])*log(constants[11]/states[2])
    algebraic[66] = 1.00000/(8000.00*exp(((states[0]-algebraic[56])-97.0000)/8.50000)+7.00000*exp(((states[0]-algebraic[56])-97.0000)/300.000))
    algebraic[59] = (0.750000*exp(0.0350000*((states[0]-algebraic[56])-10.0000)))/(1.00000+exp(0.0150000*((states[0]-algebraic[56])-140.000)))
    algebraic[61] = (3.00000*exp(-0.0480000*((states[0]-algebraic[56])-10.0000))*(1.00000+exp(0.0640000*((states[0]-algebraic[56])-38.0000))))/(1.00000+exp(0.0300000*((states[0]-algebraic[56])-70.0000)))
    algebraic[64] = algebraic[61]/(algebraic[59]+algebraic[61])
    algebraic[68] = ((power(algebraic[64], 4.00000))*1.00000)/(0.000140000*exp(-((states[0]-algebraic[56])-97.0000)/9.10000)+0.200000*exp(-((states[0]-algebraic[56])-97.0000)/500.000))
    algebraic[93] = 1.00000*exp(((constants[49]-1.00000)*constants[2]*states[0])/(constants[0]*constants[1]))
    algebraic[95] = algebraic[93]*constants[97]+constants[43]*constants[100]
    algebraic[90] = 1.00000/(1.00000+(power(constants[44]/states[1], 3.00000))*(1.00000+algebraic[29]/constants[46]))
    algebraic[91] = 1.00000/(1.00000+(constants[46]/algebraic[29])*(1.00000+power(states[1]/constants[44], 3.00000)))
    algebraic[92] = 1.00000*exp((constants[49]*constants[2]*states[0])/(constants[0]*constants[1]))
    algebraic[97] = algebraic[92]*algebraic[90]+constants[42]*algebraic[91]
    algebraic[0] = custom_piecewise([greater_equal(voi , constants[4]) & less_equal(voi , constants[5]) & less_equal((voi-constants[4])-floor((voi-constants[4])/constants[6])*constants[6] , constants[7]), constants[8] , True, 0.00000])
    algebraic[32] = custom_piecewise([equal(states[0] , 0.00000), -constants[9] , True, (((constants[2]*states[0])/(constants[0]*constants[1]))*(states[1]-constants[9]*exp((-constants[2]*states[0])/(constants[0]*constants[1]))))/(1.00000-exp((-constants[2]*states[0])/(constants[0]*constants[1])))])
    algebraic[79] = constants[37]*algebraic[32]
    algebraic[39] = custom_piecewise([equal(states[0] , 0.00000), states[2] , True, (((constants[2]*states[0])/(constants[0]*constants[1]))*(states[2]-constants[11]*exp((-constants[2]*states[0])/(constants[0]*constants[1]))))/(1.00000-exp((-constants[2]*states[0])/(constants[0]*constants[1])))])
    algebraic[78] = 0.400000*constants[37]*algebraic[39]
    algebraic[80] = algebraic[78]+algebraic[79]
    algebraic[88] = constants[41]*algebraic[36]
    algebraic[81] = custom_piecewise([equal(states[0] , -3.00000), constants[95]*algebraic[39]*13.0077 , True, (constants[95]*algebraic[39]*(states[0]+3.00000))/(1.00000-exp(-(states[0]+3.00000)/13.0000))])
    algebraic[82] = 1.00000/(1.00000+power(0.00120000/algebraic[29], 3.00000))
    algebraic[84] = constants[38]*algebraic[32]*algebraic[82]
    algebraic[83] = constants[38]*algebraic[39]*algebraic[82]
    algebraic[85] = algebraic[83]+algebraic[84]
    algebraic[86] = 0.800000/(1.00000+power(states[4]/0.100000, 2.00000))
    algebraic[87] = constants[96]*(states[0]-algebraic[56])*algebraic[86]
    algebraic[89] = algebraic[80]+algebraic[88]+algebraic[81]+algebraic[85]+algebraic[87]
    algebraic[42] = constants[17]*algebraic[32]*states[5]*states[6]
    algebraic[44] = 0.100000*constants[17]*algebraic[39]*states[5]*states[6]
    algebraic[45] = algebraic[42]+algebraic[44]
    algebraic[46] = (states[9]*(states[10]+states[11])*states[12])/(1.00000+power(1.40000/states[4], 3.00000))
    algebraic[48] = 1.85000e-05*constants[19]*algebraic[32]*algebraic[46]
    algebraic[49] = 0.000365000*constants[19]*algebraic[39]*algebraic[46]
    algebraic[47] = constants[19]*algebraic[36]*algebraic[46]
    algebraic[50] = algebraic[48]+algebraic[47]+algebraic[49]
    algebraic[54] = constants[29]*algebraic[36]*states[16]*states[17]
    algebraic[63] = algebraic[59]/(algebraic[59]+algebraic[61])
    algebraic[65] = 2.00000*(power(algebraic[64], 2.00000))*(power(algebraic[63], 2.00000))
    algebraic[67] = (8.00000/3.00000)*(power(algebraic[64], 3.00000))*algebraic[63]
    algebraic[69] = power(algebraic[64], 4.00000)
    algebraic[70] = constants[93]*(states[0]-algebraic[56])*(algebraic[69]+algebraic[67]+algebraic[65])*states[18]
    algebraic[71] = constants[94]*(states[0]-algebraic[56])*(0.600000*states[19]+0.400000*states[20])*states[21]
    algebraic[72] = constants[32]*algebraic[39]*(power(states[22], 2.00000))*(0.900000*states[23]+0.100000)
    algebraic[73] = constants[33]*algebraic[32]*(power(states[22], 2.00000))*(0.900000*states[23]+0.100000)
    algebraic[74] = algebraic[73]+algebraic[72]
    algebraic[75] = constants[35]*algebraic[39]*(power(states[24], 3.00000))*states[25]
    algebraic[76] = constants[36]*algebraic[32]*(power(states[24], 3.00000))*states[25]
    algebraic[77] = algebraic[76]+algebraic[75]
    algebraic[101] = constants[9]*exp((-0.820000*constants[2]*states[0])/(constants[0]*constants[1]))
    algebraic[102] = 1.00000/(1.00000+(power(constants[54]/algebraic[101], 1.06000))*(1.00000+power(constants[11]/constants[56], 1.12000)))
    algebraic[98] = 1.00000/(1.00000+(power(constants[53]/states[1], 1.06000))*(1.00000+power(states[2]/constants[55], 1.12000)))
    algebraic[100] = 0.370000/(1.00000+constants[57]/states[4])
    algebraic[103] = constants[58]*constants[3]*1.00000*(algebraic[100]*algebraic[98]*states[27]-constants[50]*algebraic[102]*(1.00000-states[27]))
    algebraic[94] = constants[48]*constants[3]*1.00000*(algebraic[92]*algebraic[90]*states[26]-algebraic[93]*constants[97]*(1.00000-states[26]))
    algebraic[105] = algebraic[45]+algebraic[50]+algebraic[54]+algebraic[70]+algebraic[71]+algebraic[74]+algebraic[77]+algebraic[89]+algebraic[103]+algebraic[94]
    algebraic[106] = algebraic[42]+algebraic[73]+algebraic[76]+algebraic[48]+algebraic[79]+algebraic[84]+3.00000*algebraic[103]+3.00000*algebraic[94]
    algebraic[107] = (algebraic[70]+algebraic[71]+algebraic[75]+algebraic[87]+algebraic[72]+algebraic[44]+algebraic[49]+algebraic[78]+algebraic[83]+algebraic[81])-2.00000*algebraic[103]
    algebraic[104] = 1.00000/(1.00000+(power(constants[56]/constants[11], 1.12000))*(1.00000+power(algebraic[101]/constants[54], 1.06000)))
    algebraic[109] = constants[50]*algebraic[102]+constants[52]*algebraic[104]
    algebraic[99] = 1.00000/(1.00000+(power(constants[55]/states[2], 1.12000))*(1.00000+power(states[1]/constants[53], 1.06000)))
    algebraic[111] = algebraic[100]*algebraic[98]+constants[51]*algebraic[99]
    algebraic[110] = 1.00000/(1.00000+constants[63]/algebraic[29])
    algebraic[108] = 1.00000/(1.00000+constants[62]/states[28])
    algebraic[114] = 1.00000/(1.00000+constants[64]/states[4])
    algebraic[115] = constants[65]*1.00000*(constants[59]*algebraic[108]*states[29]-algebraic[114]*algebraic[110]*(1.00000-states[29]))
    algebraic[117] = -0.400000*states[34]*constants[75]
    algebraic[113] = 1.00000-algebraic[110]
    algebraic[116] = algebraic[114]*algebraic[110]+constants[61]*algebraic[113]
    algebraic[112] = 1.00000-algebraic[108]
    algebraic[118] = constants[59]*algebraic[108]+constants[60]*algebraic[112]
    algebraic[52] = algebraic[51]*algebraic[46]
    algebraic[119] = 280000.*(power(algebraic[29]/1.00000, 2.00000))+constants[68]*algebraic[52]
    algebraic[121] = (constants[73]-states[32])+constants[74]
    algebraic[122] = constants[74]*states[32]
    algebraic[123] = (power(power(algebraic[121], 2.00000)+4.00000*algebraic[122], 1.0/2)-algebraic[121])/2.00000
    algebraic[124] = 0.0800000/(1.00000+0.360000/algebraic[123])
    algebraic[125] = 0.000377000*(power(algebraic[123]/1.00000, 2.00000))
    algebraic[126] = constants[66]*(algebraic[123]-algebraic[29])*states[30]
    algebraic[127] = constants[69]*(states[28]-algebraic[123])
    algebraic[120] = constants[70]*(states[28]-algebraic[29])
    algebraic[134] = constants[77]*states[33]*constants[98]-constants[82]*states[34]
    algebraic[130] = ((1.00000-states[33])-states[34])-states[35]
    algebraic[132] = constants[76]*algebraic[29]*algebraic[130]-constants[81]*states[33]
    algebraic[128] = constants[85]-states[36]
    algebraic[136] = constants[78]*states[34]-constants[83]*states[35]*algebraic[29]
    algebraic[139] = constants[80]*(power(rates[36], 2.00000))*states[34]
    algebraic[137] = constants[79]*states[35]
    algebraic[138] = constants[80]*(power(rates[36], 2.00000))*states[35]
    algebraic[96] = (algebraic[47]+algebraic[54]+algebraic[88])-2.00000*algebraic[94]
    algebraic[140] = constants[75]*((algebraic[139]+algebraic[136])-algebraic[132])
    algebraic[58] = constants[28]*algebraic[55]
    algebraic[129] = constants[75]*(states[34]+states[35])
    algebraic[131] = constants[89]*algebraic[129]
    algebraic[133] = algebraic[131]*algebraic[128]
    algebraic[135] = -constants[99]+algebraic[133]
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
        self.R = 8.3143
        self.T = 310
        self.F = 96.4867
        self.Cm = 132
        self.stim_start = 50
        self.stim_end = 1000000
        self.stim_period = 400
        self.stim_duration = 2
        self.stim_amplitude = -4000
        self.Nao = 140
        self.Cao = 1.8
        self.Ko = 5.4
        self.Vi = 8000
        self.CMDN_max = 0.05
        self.K_mCMDN = 0.00238
        self.ProducingRate_Max = 0.003
        self.Adenosine_Total = 5
        self.P_Na = 2860
        self.k_AI_AP = 0.0000875
        self.P_CaL = 8712
        self.k_AP_AI = 0.004
        self.k_AI_AP_1 = 0.001
        self.k_CCa_UCa = 0.0003
        self.k_UCa_CCa = 0.35
        self.k_C_U = 0.143
        self.k_U_C = 0.35
        self.k_U_UCa = 6.954
        self.k_CCa_C = 0.0042
        self.k_C_CCa = 6.954
        self.P_CaT = 612
        self.P_K1_0 = 1.146
        self.P_Kr = 0.00864
        self.P_Ks_K = 5.04
        self.P_Ks_Na = 0.2016
        self.beta_y2 = 0.004444
        self.P_to_K = 0.033
        self.P_to_Na = 0.00297
        self.P_bNSC = 0.385
        self.P_lCa = 0.11
        self.P_KATP = 0.0236
        self.N = 2333
        self.P_Cab = 0.04
        self.k3 = 1
        self.k4 = 1
        self.Km_Nai = 8.75
        self.Km_Nao = 87.5
        self.Km_Cai = 0.00138
        self.Km_Cao = 1.38
        self.P_NaCa = 6.81
        self.Partition = 0.32
        self.k2 = 0.04
        self.k3_1 = 0.01
        self.k4_1 = 0.165
        self.Km_Nai_1 = 4.05
        self.Km_Nao_1 = 69.8
        self.Km_Ki = 32.88
        self.Km_Ko = 0.258
        self.Km_ATP = 0.094
        self.P_NaK = 21
        self.k1 = 0.01
        self.k3_2 = 1
        self.k4_2 = 0.01
        self.Km_CaSR = 0.08
        self.Km_CaCyto = 0.0008
        self.Km_ATP_1 = 0.1
        self.i_max = 162500
        self.P_RyR = 62000
        self.k4_3 = 0.000849
        self.Diadid_Factor = -150
        self.P_SR_T = 386
        self.P_SR_L = 459
        self.V_rel = 160
        self.V_up = 400
        self.CSQN_max = 10
        self.K_mCSQN = 0.8
        self.T_t = 0.07
        self.Y_1 = 39
        self.Y_2 = 0.0039
        self.Y_3 = 0.03
        self.Y_4 = 0.12
        self.Y_d = 0.027
        self.Z_1 = 0.03
        self.Z_2 = 0.0039
        self.Z_3 = 1560
        self.L_a = 1.17
        self.L = 0.9623799975411884
        self.KForceEC = 140000
        self.ZeroForceEL = 0.97
        self.KForceLinearEc = 200
        self.ForceFactor = 1800000
        self.B = 1.2
        self.h_c = 0.005

    def to_dict(self):
        return {
            "R": self.R,
            "T": self.T,
            "F": self.F,
            "Cm": self.Cm,
            "stim_start": self.stim_start,
            "stim_end": self.stim_end,
            "stim_period": self.stim_period,
            "stim_duration": self.stim_duration,
            "stim_amplitude": self.stim_amplitude,
            "Nao": self.Nao,
            "Cao": self.Cao,
            "Ko": self.Ko,
            "Vi": self.Vi,
            "CMDN_max": self.CMDN_max,
            "K_mCMDN": self.K_mCMDN,
            "ProducingRate_Max": self.ProducingRate_Max,
            "Adenosine_Total": self.Adenosine_Total,
            "P_Na": self.P_Na,
            "k_AI_AP": self.k_AI_AP,
            "P_CaL": self.P_CaL,
            "k_AP_AI": self.k_AP_AI,
            "k_AI_AP_1": self.k_AI_AP_1,
            "k_CCa_UCa": self.k_CCa_UCa,
            "k_UCa_CCa": self.k_UCa_CCa,
            "k_C_U": self.k_C_U,
            "k_U_C": self.k_U_C,
            "k_U_UCa": self.k_U_UCa,
            "k_CCa_C": self.k_CCa_C,
            "k_C_CCa": self.k_C_CCa,
            "P_CaT": self.P_CaT,
            "P_K1_0": self.P_K1_0,
            "P_Kr": self.P_Kr,
            "P_Ks_K": self.P_Ks_K,
            "P_Ks_Na": self.P_Ks_Na,
            "beta_y2": self.beta_y2,
            "P_to_K": self.P_to_K,
            "P_to_Na": self.P_to_Na,
            "P_bNSC": self.P_bNSC,
            "P_lCa": self.P_lCa,
            "P_KATP": self.P_KATP,
            "N": self.N,
            "P_Cab": self.P_Cab,
            "k3": self.k3,
            "k4": self.k4,
            "Km_Nai": self.Km_Nai,
            "Km_Nao": self.Km_Nao,
            "Km_Cai": self.Km_Cai,
            "Km_Cao": self.Km_Cao,
            "P_NaCa": self.P_NaCa,
            "Partition": self.Partition,
            "k2": self.k2,
            "k3_1": self.k3_1,
            "k4_1": self.k4_1,
            "Km_Nai_1": self.Km_Nai_1,
            "Km_Nao_1": self.Km_Nao_1,
            "Km_Ki": self.Km_Ki,
            "Km_Ko": self.Km_Ko,
            "Km_ATP": self.Km_ATP,
            "P_NaK": self.P_NaK,
            "k1": self.k1,
            "k3_2": self.k3_2,
            "k4_2": self.k4_2,
            "Km_CaSR": self.Km_CaSR,
            "Km_CaCyto": self.Km_CaCyto,
            "Km_ATP_1": self.Km_ATP_1,
            "i_max": self.i_max,
            "P_RyR": self.P_RyR,
            "k4_3": self.k4_3,
            "Diadid_Factor": self.Diadid_Factor,
            "P_SR_T": self.P_SR_T,
            "P_SR_L": self.P_SR_L,
            "V_rel": self.V_rel,
            "V_up": self.V_up,
            "CSQN_max": self.CSQN_max,
            "K_mCSQN": self.K_mCSQN,
            "T_t": self.T_t,
            "Y_1": self.Y_1,
            "Y_2": self.Y_2,
            "Y_3": self.Y_3,
            "Y_4": self.Y_4,
            "Y_d": self.Y_d,
            "Z_1": self.Z_1,
            "Z_2": self.Z_2,
            "Z_3": self.Z_3,
            "L_a": self.L_a,
            "L": self.L,
            "KForceEC": self.KForceEC,
            "ZeroForceEL": self.ZeroForceEL,
            "KForceLinearEc": self.KForceLinearEc,
            "ForceFactor": self.ForceFactor,
            "B": self.B,
            "h_c": self.h_c,
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
        y0=[-85.95752434460744, 4.925761439682025, 143.1837333000449, 4.0180173572968586e-4, 4.657102729020499, 1.779648367445368e-5, 0.5861887862983165, 0.3556412697995689, 0.40285968661346977, 1.5445004166497696e-6, 0.17246483915629204, 6.098246017787626e-5, 0.9985266538252986, 0.9968480629364956, 8.77325391245903e-4, 0.4250747299372254, 1.6882718240109127e-5, 0.8585352091865849, 0.6080573900752752, 0.0018339931180983765, 0.20443083454225305, 0.967887666264921, 0.09738789658609195, 0.09745345578743213, 7.956883250874798e-4, 0.9999125083105881, 0.9891789193465331, 0.5910747147428818, 2.611712901567567, 0.46108441538480216, 3.4314360001543243e-4, 0.19135178123107768, 9.455741736977666, 0.02490898775497523, 0.001990153835322864, 4.2941813853474524e-4, 0.9573749975411884],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "matsuoka_sarai_kuratomi_ono_noma_2003"
        self.curve_names = [
            "Vm",
            "Nai",
            "Ki",
            "Ca_Total",
            "ATPi",
            "p_AP_Na",
            "y",
            "p_RP_Na",
            "p_AI_Na",
            "p_AP_CaL",
            "p_U",
            "p_UCa",
            "y_1",
            "p_RP_CaL",
            "p_AI_CaL",
            "p_C",
            "y1",
            "y2",
            "y_2",
            "y1_1",
            "y2_1",
            "y3",
            "y1_2",
            "y2_2",
            "y1_3",
            "y2_3",
            "y_3",
            "y_4",
            "Caup",
            "y_5",
            "p_open_RyR",
            "p_close_RyR",
            "Ca_Total_1",
            "pCa",
            "pCaCB",
            "pCB",
            "X",
        ]
        self.state_names = ['Vm', 'Nai', 'Ki', 'Ca_Total', 'ATPi', 'p_AP_Na', 'y', 'p_RP_Na', 'p_AI_Na', 'p_AP_CaL', 'p_U', 'p_UCa', 'y_1', 'p_RP_CaL', 'p_AI_CaL', 'p_C', 'y1', 'y2', 'y_2', 'y1_1', 'y2_1', 'y3', 'y1_2', 'y2_2', 'y1_3', 'y2_3', 'y_3', 'y_4', 'Caup', 'y_5', 'p_open_RyR', 'p_close_RyR', 'Ca_Total_1', 'pCa', 'pCaCB', 'pCB', 'X']
        self.algebraic_names = ['i_ext', 'p_RI_Na', 'alpha_y', 'p_RI_CaL', 'alpha_y_1', 'alpha_y1', 'alpha_y2', 'alpha_y1_1', 'alpha_y2_1', 'alpha_y3', 'alpha_y1_2', 'alpha_y1_3', 'alpha_y2_2', 'b1', 'k_RP_AP', 'beta_y', 'k_RP_AP_1', 'beta_y_1', 'beta_y1', 'beta_y2', 'beta_y1_1', 'beta_y2_1', 'beta_y3', 'beta_y1_2', 'beta_y1_3', 'beta_y2_2', 'c1', 'k_AP_RP', 'k_AP_RP_1', 'Cai', 'k_AP_AI', 'k_RI_AI', 'CF_Na', 'k_AI_RI', 'k_AI_RI_1', 'alpha_y2_3', 'CF_Ca', 'k_RI_AI_1', 'k_RP_RI', 'CF_K', 'k_RP_RI_1', 'k_RI_RP', 'i_Na_Na', 'k_RI_RP_1', 'i_Na_K', 'i_Na', 'p_open_CaL', 'i_CaL_Ca', 'i_CaL_Na', 'i_CaL_K', 'i_Ca_L', 'iCaL', 'CaDiadic', 'Cacm', 'i_Ca_T', 'CaEffC', 'E_K', 'CaEffU', 'k_CCCa_Ca', 'mu', 'k_UUCa_Ca', 'lambda', 'p_CCa', 'fB', 'fO', 'fO2', 'alpha_y_2', 'fO3', 'beta_y_2', 'fO4', 'i_K1', 'i_Kr', 'i_Ks_K', 'i_Ks_Na', 'i_Ks', 'i_to_K', 'i_to_Na', 'i_to', 'i_bNSC_K', 'i_bNSC_Na', 'i_bNSC', 'i_Kpl', 'p_open', 'i_lCa_K', 'i_lCa_Na', 'i_lCa', 'p_open_1', 'i_KATP', 'i_Cab', 'i_I', 'p_E1Na', 'p_E1Ca', 'k1', 'k2', 'i_NaCa', 'alpha_y_3', 'i_net_Ca', 'beta_y_3', 'p_E1Na_1', 'p_E1K', 'k1_1', 'Nao_Eff', 'p_E2Na', 'i_NaK', 'p_E2K', 'i_tot', 'i_net_Na', 'i_net_K', 'p_E1Ca_1', 'alpha_y_4', 'p_E2Ca', 'beta_y_4', 'p_E1', 'p_E2', 'k2_1', 'i_SR_U', 'alpha_y_5', 'dATPdt', 'beta_y_5', 'k1_2', 'i_SR_L', 'b1_1', 'c1_1', 'Carel', 'k2_2', 'k3', 'i_RyR', 'i_SR_T', 'h', 'CBBound', 'p', 'NewCBF', 'Q_b', 'ForceCB', 'Q_a', 'ForceExt', 'Q_r', 'Q_d', 'Q_d1', 'Q_d2', 'dCaidt']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 101
        p = self.params

        # direct mapping
        c[0] = p.R
        c[1] = p.T
        c[2] = p.F
        c[3] = p.Cm
        c[4] = p.stim_start
        c[5] = p.stim_end
        c[6] = p.stim_period
        c[7] = p.stim_duration
        c[8] = p.stim_amplitude
        c[9] = p.Nao
        c[10] = p.Cao
        c[11] = p.Ko
        c[12] = p.Vi
        c[13] = p.CMDN_max
        c[14] = p.K_mCMDN
        c[15] = p.ProducingRate_Max
        c[16] = p.Adenosine_Total
        c[17] = p.P_Na
        c[18] = p.k_AI_AP
        c[19] = p.P_CaL
        c[20] = p.k_AP_AI
        c[21] = p.k_AI_AP_1
        c[22] = p.k_CCa_UCa
        c[23] = p.k_UCa_CCa
        c[24] = p.k_C_U
        c[25] = p.k_U_C
        c[26] = p.k_U_UCa
        c[27] = p.k_CCa_C
        c[28] = p.k_C_CCa
        c[29] = p.P_CaT
        c[30] = p.P_K1_0
        c[31] = p.P_Kr
        c[32] = p.P_Ks_K
        c[33] = p.P_Ks_Na
        c[34] = p.beta_y2
        c[35] = p.P_to_K
        c[36] = p.P_to_Na
        c[37] = p.P_bNSC
        c[38] = p.P_lCa
        c[39] = p.P_KATP
        c[40] = p.N
        c[41] = p.P_Cab
        c[42] = p.k3
        c[43] = p.k4
        c[44] = p.Km_Nai
        c[45] = p.Km_Nao
        c[46] = p.Km_Cai
        c[47] = p.Km_Cao
        c[48] = p.P_NaCa
        c[49] = p.Partition
        c[50] = p.k2
        c[51] = p.k3_1
        c[52] = p.k4_1
        c[53] = p.Km_Nai_1
        c[54] = p.Km_Nao_1
        c[55] = p.Km_Ki
        c[56] = p.Km_Ko
        c[57] = p.Km_ATP
        c[58] = p.P_NaK
        c[59] = p.k1
        c[60] = p.k3_2
        c[61] = p.k4_2
        c[62] = p.Km_CaSR
        c[63] = p.Km_CaCyto
        c[64] = p.Km_ATP_1
        c[65] = p.i_max
        c[66] = p.P_RyR
        c[67] = p.k4_3
        c[68] = p.Diadid_Factor
        c[69] = p.P_SR_T
        c[70] = p.P_SR_L
        c[71] = p.V_rel
        c[72] = p.V_up
        c[73] = p.CSQN_max
        c[74] = p.K_mCSQN
        c[75] = p.T_t
        c[76] = p.Y_1
        c[77] = p.Y_2
        c[78] = p.Y_3
        c[79] = p.Y_4
        c[80] = p.Y_d
        c[81] = p.Z_1
        c[82] = p.Z_2
        c[83] = p.Z_3
        c[84] = p.L_a
        c[85] = p.L
        c[86] = p.KForceEC
        c[87] = p.ZeroForceEL
        c[88] = p.KForceLinearEc
        c[89] = p.ForceFactor
        c[90] = p.B
        c[91] = p.h_c

        # derived constants
        c[92] = (c[27]*c[24]*c[26]*c[23])/(c[25]*c[28]*c[22])
        c[93] = c[30]*c[3]*(power(c[11]/5.40000, 0.400000))
        c[94] = c[31]*c[3]*(power(c[11]/5.40000, 0.200000))
        c[95] = 0.000110000*(power(c[11]/5.40000, 0.160000))
        c[96] = c[39]*c[40]*(power(c[11]/1.00000, 0.240000))
        c[97] = 1.00000/(1.00000+(power(c[45]/c[9], 3.00000))*(1.00000+c[10]/c[47]))
        c[98] = exp(-20.0000*(power(c[85]-c[84], 2.00000)))
        c[99] = c[86]*(power(c[87]-c[85], 5.00000))+c[88]*(c[87]-c[85])
        c[100] = 1.00000/(1.00000+(c[47]/c[10])*(1.00000+power(c[9]/c[45], 3.00000)))

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
