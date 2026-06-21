# Size of variable arrays:
sizeAlgebraic = 75
sizeStates = 27
sizeConstants = 66
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
    legend_constants[0] = "R in component membrane (attojoule_per_millimole_kelvin)"
    legend_constants[1] = "T in component membrane (kelvin)"
    legend_constants[2] = "F in component membrane (femtocoulomb_per_millimole)"
    legend_constants[3] = "Cm in component membrane (picoF)"
    legend_algebraic[39] = "i_CaT in component T_type_calcium_channel_current (picoA)"
    legend_algebraic[34] = "i_CaL in component L_type_calcium_channel_current (picoA)"
    legend_algebraic[40] = "i_Kr in component rapidly_activating_delayed_rectifier_potassium_current (picoA)"
    legend_algebraic[42] = "i_Ks in component slowly_activating_delayed_rectifier_potassium_current (picoA)"
    legend_algebraic[43] = "i_to in component AP_sensitive_currents (picoA)"
    legend_algebraic[44] = "i_sus in component AP_sensitive_currents (picoA)"
    legend_algebraic[47] = "i_h in component hyperpolarisation_activated_current (picoA)"
    legend_algebraic[48] = "i_st in component sustained_inward_current (picoA)"
    legend_algebraic[49] = "i_b_Na in component sodium_dependent_background_current (picoA)"
    legend_algebraic[65] = "i_NaCa in component sodium_calcium_exchange_current (picoA)"
    legend_algebraic[51] = "i_NaK in component sodium_potassium_pump_current (picoA)"
    legend_algebraic[50] = "i_K_ACh in component background_muscarinic_potassium_channel_current (picoA)"
    legend_algebraic[0] = "E_Na in component reversal_potentials (millivolt)"
    legend_algebraic[29] = "E_K in component reversal_potentials (millivolt)"
    legend_states[1] = "Nai in component intracellular_ion_concentrations (millimolar)"
    legend_constants[4] = "Nao in component intracellular_ion_concentrations (millimolar)"
    legend_states[2] = "Ki in component intracellular_ion_concentrations (millimolar)"
    legend_constants[5] = "Ko in component intracellular_ion_concentrations (millimolar)"
    legend_constants[6] = "g_CaL in component L_type_calcium_channel_current (nanoS)"
    legend_constants[7] = "E_CaL in component L_type_calcium_channel_current (millivolt)"
    legend_states[3] = "Ca_sub in component intracellular_ion_concentrations (millimolar)"
    legend_states[4] = "d in component L_type_calcium_channel_current_d_gate (dimensionless)"
    legend_states[5] = "f in component L_type_calcium_channel_current_f_gate (dimensionless)"
    legend_states[6] = "fCa in component L_type_calcium_channel_current_fCa_gate (dimensionless)"
    legend_algebraic[1] = "d_infinity in component L_type_calcium_channel_current_d_gate (dimensionless)"
    legend_algebraic[35] = "tau_d in component L_type_calcium_channel_current_d_gate (millisecond)"
    legend_algebraic[15] = "alpha_d in component L_type_calcium_channel_current_d_gate (per_millisecond)"
    legend_algebraic[30] = "beta_d in component L_type_calcium_channel_current_d_gate (per_millisecond)"
    legend_algebraic[2] = "f_infinity in component L_type_calcium_channel_current_f_gate (dimensionless)"
    legend_algebraic[16] = "tau_f in component L_type_calcium_channel_current_f_gate (millisecond)"
    legend_constants[62] = "alpha_fCa in component L_type_calcium_channel_current_fCa_gate (per_millisecond)"
    legend_constants[8] = "beta_fCa in component L_type_calcium_channel_current_fCa_gate (per_millimolar_millisecond)"
    legend_algebraic[3] = "fCa_infinity in component L_type_calcium_channel_current_fCa_gate (dimensionless)"
    legend_algebraic[17] = "tau_fCa in component L_type_calcium_channel_current_fCa_gate (millisecond)"
    legend_constants[9] = "Km_fCa in component L_type_calcium_channel_current_fCa_gate (millimolar)"
    legend_constants[10] = "g_CaT in component T_type_calcium_channel_current (nanoS)"
    legend_constants[11] = "E_CaT in component T_type_calcium_channel_current (millivolt)"
    legend_states[7] = "d in component T_type_calcium_channel_current_d_gate (dimensionless)"
    legend_states[8] = "f in component T_type_calcium_channel_current_f_gate (dimensionless)"
    legend_algebraic[4] = "d_infinity in component T_type_calcium_channel_current_d_gate (dimensionless)"
    legend_algebraic[18] = "tau_d in component T_type_calcium_channel_current_d_gate (millisecond)"
    legend_algebraic[5] = "f_infinity in component T_type_calcium_channel_current_f_gate (dimensionless)"
    legend_algebraic[19] = "tau_f in component T_type_calcium_channel_current_f_gate (millisecond)"
    legend_constants[63] = "g_Kr in component rapidly_activating_delayed_rectifier_potassium_current (nanoS)"
    legend_states[9] = "paS in component rapidly_activating_delayed_rectifier_potassium_current_pa_gate (dimensionless)"
    legend_states[10] = "paF in component rapidly_activating_delayed_rectifier_potassium_current_pa_gate (dimensionless)"
    legend_states[11] = "piy in component rapidly_activating_delayed_rectifier_potassium_current_pi_gate (dimensionless)"
    legend_algebraic[6] = "pa_infinity in component rapidly_activating_delayed_rectifier_potassium_current_pa_gate (dimensionless)"
    legend_algebraic[20] = "tau_paS in component rapidly_activating_delayed_rectifier_potassium_current_pa_gate (millisecond)"
    legend_algebraic[21] = "tau_paF in component rapidly_activating_delayed_rectifier_potassium_current_pa_gate (millisecond)"
    legend_algebraic[7] = "pi_infinity in component rapidly_activating_delayed_rectifier_potassium_current_pi_gate (dimensionless)"
    legend_algebraic[22] = "tau_pi in component rapidly_activating_delayed_rectifier_potassium_current_pi_gate (millisecond)"
    legend_constants[12] = "g_Ks in component slowly_activating_delayed_rectifier_potassium_current (nanoS)"
    legend_algebraic[41] = "E_Ks in component slowly_activating_delayed_rectifier_potassium_current (millivolt)"
    legend_states[12] = "n in component slowly_activating_delayed_rectifier_potassium_current_n_gate (dimensionless)"
    legend_algebraic[31] = "n_infinity in component slowly_activating_delayed_rectifier_potassium_current_n_gate (dimensionless)"
    legend_algebraic[36] = "tau_n in component slowly_activating_delayed_rectifier_potassium_current_n_gate (millisecond)"
    legend_algebraic[8] = "alpha_n in component slowly_activating_delayed_rectifier_potassium_current_n_gate (per_millisecond)"
    legend_algebraic[23] = "beta_n in component slowly_activating_delayed_rectifier_potassium_current_n_gate (per_millisecond)"
    legend_constants[13] = "g_to in component AP_sensitive_currents (nanoS)"
    legend_constants[14] = "g_sus in component AP_sensitive_currents (nanoS)"
    legend_states[13] = "q in component AP_sensitive_currents_q_gate (dimensionless)"
    legend_states[14] = "r in component AP_sensitive_currents_r_gate (dimensionless)"
    legend_algebraic[9] = "q_infinity in component AP_sensitive_currents_q_gate (dimensionless)"
    legend_algebraic[24] = "tau_q in component AP_sensitive_currents_q_gate (millisecond)"
    legend_algebraic[10] = "r_infinity in component AP_sensitive_currents_r_gate (dimensionless)"
    legend_algebraic[25] = "tau_r in component AP_sensitive_currents_r_gate (millisecond)"
    legend_algebraic[45] = "i_h_Na in component hyperpolarisation_activated_current (picoA)"
    legend_algebraic[46] = "i_h_K in component hyperpolarisation_activated_current (picoA)"
    legend_constants[15] = "g_h_Na in component hyperpolarisation_activated_current (nanoS)"
    legend_constants[16] = "g_h_K in component hyperpolarisation_activated_current (nanoS)"
    legend_states[15] = "y in component hyperpolarisation_activated_current_y_gate (dimensionless)"
    legend_algebraic[11] = "y_infinity in component hyperpolarisation_activated_current_y_gate (dimensionless)"
    legend_algebraic[26] = "tau_y in component hyperpolarisation_activated_current_y_gate (millisecond)"
    legend_constants[17] = "g_st in component sustained_inward_current (nanoS)"
    legend_constants[18] = "E_st in component sustained_inward_current (millivolt)"
    legend_states[16] = "qa in component sustained_inward_current_qa_gate (dimensionless)"
    legend_states[17] = "qi in component sustained_inward_current_qi_gate (dimensionless)"
    legend_algebraic[12] = "qa_infinity in component sustained_inward_current_qa_gate (dimensionless)"
    legend_algebraic[37] = "tau_qa in component sustained_inward_current_qa_gate (millisecond)"
    legend_algebraic[27] = "alpha_qa in component sustained_inward_current_qa_gate (per_millisecond)"
    legend_algebraic[32] = "beta_qa in component sustained_inward_current_qa_gate (per_millisecond)"
    legend_algebraic[33] = "qi_infinity in component sustained_inward_current_qi_gate (dimensionless)"
    legend_algebraic[38] = "tau_qi in component sustained_inward_current_qi_gate (millisecond)"
    legend_algebraic[13] = "alpha_qi in component sustained_inward_current_qi_gate (per_millisecond)"
    legend_algebraic[28] = "beta_qi in component sustained_inward_current_qi_gate (per_millisecond)"
    legend_constants[19] = "g_b_Na in component sodium_dependent_background_current (nanoS)"
    legend_constants[64] = "g_K_ACh in component background_muscarinic_potassium_channel_current (picoA)"
    legend_constants[20] = "Km_Kp in component sodium_potassium_pump_current (millimolar)"
    legend_constants[21] = "Km_Nap in component sodium_potassium_pump_current (millimolar)"
    legend_constants[22] = "i_NaK_max in component sodium_potassium_pump_current (picoA)"
    legend_constants[23] = "kNaCa in component sodium_calcium_exchange_current (picoA)"
    legend_algebraic[62] = "x1 in component sodium_calcium_exchange_current (dimensionless)"
    legend_algebraic[58] = "x2 in component sodium_calcium_exchange_current (dimensionless)"
    legend_algebraic[63] = "x3 in component sodium_calcium_exchange_current (dimensionless)"
    legend_algebraic[64] = "x4 in component sodium_calcium_exchange_current (dimensionless)"
    legend_algebraic[53] = "k41 in component sodium_calcium_exchange_current (dimensionless)"
    legend_constants[65] = "k34 in component sodium_calcium_exchange_current (dimensionless)"
    legend_algebraic[61] = "k23 in component sodium_calcium_exchange_current (dimensionless)"
    legend_algebraic[60] = "k21 in component sodium_calcium_exchange_current (dimensionless)"
    legend_algebraic[57] = "k32 in component sodium_calcium_exchange_current (dimensionless)"
    legend_algebraic[52] = "k43 in component sodium_calcium_exchange_current (dimensionless)"
    legend_algebraic[55] = "k12 in component sodium_calcium_exchange_current (dimensionless)"
    legend_algebraic[56] = "k14 in component sodium_calcium_exchange_current (dimensionless)"
    legend_constants[24] = "Qci in component sodium_calcium_exchange_current (dimensionless)"
    legend_constants[25] = "Qn in component sodium_calcium_exchange_current (dimensionless)"
    legend_constants[26] = "Qco in component sodium_calcium_exchange_current (dimensionless)"
    legend_constants[27] = "K3ni in component sodium_calcium_exchange_current (millimolar)"
    legend_constants[28] = "Kci in component sodium_calcium_exchange_current (millimolar)"
    legend_constants[29] = "K1ni in component sodium_calcium_exchange_current (millimolar)"
    legend_constants[30] = "K2ni in component sodium_calcium_exchange_current (millimolar)"
    legend_constants[31] = "Kcni in component sodium_calcium_exchange_current (millimolar)"
    legend_constants[32] = "K3no in component sodium_calcium_exchange_current (millimolar)"
    legend_constants[33] = "K1no in component sodium_calcium_exchange_current (millimolar)"
    legend_constants[34] = "K2no in component sodium_calcium_exchange_current (millimolar)"
    legend_constants[35] = "Kco in component sodium_calcium_exchange_current (millimolar)"
    legend_algebraic[59] = "do in component sodium_calcium_exchange_current (dimensionless)"
    legend_algebraic[54] = "di in component sodium_calcium_exchange_current (dimensionless)"
    legend_constants[36] = "Cao in component intracellular_ion_concentrations (millimolar)"
    legend_algebraic[66] = "j_Ca_dif in component intracellular_calcium_dynamics (millimolar_per_millisecond)"
    legend_algebraic[67] = "j_rel in component intracellular_calcium_dynamics (millimolar_per_millisecond)"
    legend_algebraic[68] = "j_up in component intracellular_calcium_dynamics (millimolar_per_millisecond)"
    legend_algebraic[70] = "j_tr in component intracellular_calcium_dynamics (millimolar_per_millisecond)"
    legend_constants[37] = "tau_dif_Ca in component intracellular_calcium_dynamics (millisecond)"
    legend_constants[38] = "tau_tr in component intracellular_calcium_dynamics (millisecond)"
    legend_constants[39] = "K_rel in component intracellular_calcium_dynamics (millimolar)"
    legend_constants[40] = "P_up in component intracellular_calcium_dynamics (millimolar_per_millisecond)"
    legend_constants[41] = "P_rel in component intracellular_calcium_dynamics (per_millisecond)"
    legend_constants[42] = "K_up in component intracellular_calcium_dynamics (millimolar)"
    legend_states[18] = "Ca_up in component intracellular_ion_concentrations (millimolar)"
    legend_states[19] = "Cai in component intracellular_ion_concentrations (millimolar)"
    legend_states[20] = "Ca_rel in component intracellular_ion_concentrations (millimolar)"
    legend_constants[43] = "Mgi in component intracellular_ion_concentrations (millimolar)"
    legend_constants[44] = "V_i in component intracellular_ion_concentrations (litre)"
    legend_constants[45] = "V_rel in component intracellular_ion_concentrations (litre)"
    legend_constants[46] = "V_up in component intracellular_ion_concentrations (litre)"
    legend_constants[47] = "V_sub in component intracellular_ion_concentrations (litre)"
    legend_constants[48] = "TMC_tot in component calcium_buffering (dimensionless)"
    legend_constants[49] = "CM_tot in component calcium_buffering (dimensionless)"
    legend_constants[50] = "TC_tot in component calcium_buffering (dimensionless)"
    legend_constants[51] = "CQ_tot in component calcium_buffering (dimensionless)"
    legend_algebraic[72] = "delta_fTMC in component calcium_buffering (millimolar_per_millisecond)"
    legend_algebraic[74] = "delta_fCMi in component calcium_buffering (millimolar_per_millisecond)"
    legend_algebraic[69] = "delta_fCMs in component calcium_buffering (millimolar_per_millisecond)"
    legend_algebraic[71] = "delta_fTC in component calcium_buffering (millimolar_per_millisecond)"
    legend_algebraic[73] = "delta_fCQ in component calcium_buffering (millimolar_per_millisecond)"
    legend_algebraic[14] = "delta_fTMM in component calcium_buffering (millimolar_per_millisecond)"
    legend_states[21] = "fTMM in component calcium_buffering (millimolar)"
    legend_states[22] = "fCMi in component calcium_buffering (millimolar)"
    legend_states[23] = "fCMs in component calcium_buffering (millimolar)"
    legend_states[24] = "fTC in component calcium_buffering (millimolar)"
    legend_states[25] = "fTMC in component calcium_buffering (millimolar)"
    legend_states[26] = "fCQ in component calcium_buffering (millimolar)"
    legend_constants[52] = "kf_TC in component calcium_buffering (per_millimolar_millisecond)"
    legend_constants[53] = "kf_TMM in component calcium_buffering (per_millimolar_millisecond)"
    legend_constants[54] = "kf_TMC in component calcium_buffering (per_millimolar_millisecond)"
    legend_constants[55] = "kf_CM in component calcium_buffering (per_millimolar_millisecond)"
    legend_constants[56] = "kf_CQ in component calcium_buffering (per_millimolar_millisecond)"
    legend_constants[57] = "kb_TC in component calcium_buffering (per_millisecond)"
    legend_constants[58] = "kb_TMC in component calcium_buffering (per_millisecond)"
    legend_constants[59] = "kb_TMM in component calcium_buffering (per_millisecond)"
    legend_constants[60] = "kb_CM in component calcium_buffering (per_millisecond)"
    legend_constants[61] = "kb_CQ in component calcium_buffering (per_millisecond)"
    legend_rates[0] = "d/dt V in component membrane (millivolt)"
    legend_rates[4] = "d/dt d in component L_type_calcium_channel_current_d_gate (dimensionless)"
    legend_rates[5] = "d/dt f in component L_type_calcium_channel_current_f_gate (dimensionless)"
    legend_rates[6] = "d/dt fCa in component L_type_calcium_channel_current_fCa_gate (dimensionless)"
    legend_rates[7] = "d/dt d in component T_type_calcium_channel_current_d_gate (dimensionless)"
    legend_rates[8] = "d/dt f in component T_type_calcium_channel_current_f_gate (dimensionless)"
    legend_rates[9] = "d/dt paS in component rapidly_activating_delayed_rectifier_potassium_current_pa_gate (dimensionless)"
    legend_rates[10] = "d/dt paF in component rapidly_activating_delayed_rectifier_potassium_current_pa_gate (dimensionless)"
    legend_rates[11] = "d/dt piy in component rapidly_activating_delayed_rectifier_potassium_current_pi_gate (dimensionless)"
    legend_rates[12] = "d/dt n in component slowly_activating_delayed_rectifier_potassium_current_n_gate (dimensionless)"
    legend_rates[13] = "d/dt q in component AP_sensitive_currents_q_gate (dimensionless)"
    legend_rates[14] = "d/dt r in component AP_sensitive_currents_r_gate (dimensionless)"
    legend_rates[15] = "d/dt y in component hyperpolarisation_activated_current_y_gate (dimensionless)"
    legend_rates[16] = "d/dt qa in component sustained_inward_current_qa_gate (dimensionless)"
    legend_rates[17] = "d/dt qi in component sustained_inward_current_qi_gate (dimensionless)"
    legend_rates[1] = "d/dt Nai in component intracellular_ion_concentrations (millimolar)"
    legend_rates[2] = "d/dt Ki in component intracellular_ion_concentrations (millimolar)"
    legend_rates[19] = "d/dt Cai in component intracellular_ion_concentrations (millimolar)"
    legend_rates[3] = "d/dt Ca_sub in component intracellular_ion_concentrations (millimolar)"
    legend_rates[18] = "d/dt Ca_up in component intracellular_ion_concentrations (millimolar)"
    legend_rates[20] = "d/dt Ca_rel in component intracellular_ion_concentrations (millimolar)"
    legend_rates[24] = "d/dt fTC in component calcium_buffering (millimolar)"
    legend_rates[25] = "d/dt fTMC in component calcium_buffering (millimolar)"
    legend_rates[21] = "d/dt fTMM in component calcium_buffering (millimolar)"
    legend_rates[22] = "d/dt fCMi in component calcium_buffering (millimolar)"
    legend_rates[23] = "d/dt fCMs in component calcium_buffering (millimolar)"
    legend_rates[26] = "d/dt fCQ in component calcium_buffering (millimolar)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = -58.600291137693
    constants[0] = 8314400000000000
    constants[1] = 310.15
    constants[2] = 96485000000000000
    constants[3] = 32
    states[1] = 9.438646305915
    constants[4] = 140
    states[2] = 139.984146485614
    constants[5] = 5.4
    constants[6] = 0.58
    constants[7] = 45
    states[3] = 0.00019074741
    states[4] = 0.000602055134
    states[5] = 0.626999773853
    states[6] = 0.589580408056
    constants[8] = 60
    constants[9] = 0.00035
    constants[10] = 0.458
    constants[11] = 45
    states[7] = 0.004571884917
    states[8] = 0.249637570396
    states[9] = 0.629323128348
    states[10] = 0.3493633709533
    states[11] = 0.852396631172
    constants[12] = 0.0259
    states[12] = 0.054409723782
    constants[13] = 0.18
    constants[14] = 0.02
    states[13] = 0.531446952485
    states[14] = 0.005550489445
    constants[15] = 0.1437375
    constants[16] = 0.2312625
    states[15] = 0.067156687129
    constants[17] = 0.015
    constants[18] = 37.4
    states[16] = 0.426018100136
    states[17] = 0.333330378068
    constants[19] = 0.0054
    constants[20] = 1.4
    constants[21] = 14
    constants[22] = 3.6
    constants[23] = 125
    constants[24] = 0.1369
    constants[25] = 0.4315
    constants[26] = 0
    constants[27] = 26.44
    constants[28] = 0.0207
    constants[29] = 395.3
    constants[30] = 2.289
    constants[31] = 26.44
    constants[32] = 4.663
    constants[33] = 1628
    constants[34] = 561.4
    constants[35] = 3.663
    constants[36] = 2
    constants[37] = 0.04
    constants[38] = 60
    constants[39] = 0.0012
    constants[40] = 0.005
    constants[41] = 0.5
    constants[42] = 0.0006
    states[18] = 1.462338380106
    states[19] = 0.000312494921
    states[20] = 0.296742023718
    constants[43] = 2.5
    constants[44] = 0.0000000000015835
    constants[45] = 0.0000000000000042223
    constants[46] = 0.000000000000040816
    constants[47] = 0.000000000000035098
    constants[48] = 0.062
    constants[49] = 0.045
    constants[50] = 0.031
    constants[51] = 10
    states[21] = 0.350600895635
    states[22] = 0.116947220413
    states[23] = 0.074631965653
    states[24] = 0.059206293446
    states[25] = 0.602955114871
    states[26] = 0.260317260703
    constants[52] = 88.8
    constants[53] = 2.277
    constants[54] = 227.7
    constants[55] = 227.7
    constants[56] = 0.534
    constants[57] = 0.446
    constants[58] = 0.00751
    constants[59] = 0.751
    constants[60] = 0.542
    constants[61] = 0.445
    constants[62] = constants[9]*constants[8]
    constants[63] = 0.0250000*(power(constants[5]/1.00000, 0.590000))
    constants[64] = 0.00110000*(power(constants[5]/1.00000, 0.410000))
    constants[65] = constants[4]/(constants[32]+constants[4])
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[14] = constants[53]*constants[43]*(1.00000-(states[25]+states[21]))-constants[59]*states[21]
    rates[21] = algebraic[14]
    algebraic[2] = 1.00000/(1.00000+exp((states[0]+30.0000)/5.00000))
    algebraic[16] = 44.3000+257.100*exp(-(power((states[0]+32.5000)/13.9000, 2.00000)))
    rates[5] = (algebraic[2]-states[5])/algebraic[16]
    algebraic[3] = constants[9]/(constants[9]+states[3])
    algebraic[17] = algebraic[3]/constants[62]
    rates[6] = (algebraic[3]-states[6])/algebraic[17]
    algebraic[4] = 1.00000/(1.00000+exp(-(states[0]+26.3000)/6.00000))
    algebraic[18] = 1.00000/(1.06800*exp((states[0]+26.3000)/30.0000)+1.06800*exp(-(states[0]+26.3000)/30.0000))
    rates[7] = (algebraic[4]-states[7])/algebraic[18]
    algebraic[5] = 1.00000/(1.00000+exp((states[0]+61.7000)/5.60000))
    algebraic[19] = 1.00000/(0.0153000*exp(-(states[0]+61.7000)/83.3000)+0.0150000*exp((states[0]+61.7000)/15.3800))
    rates[8] = (algebraic[5]-states[8])/algebraic[19]
    algebraic[6] = 1.00000/(1.00000+exp(-(states[0]+23.2000)/10.6000))
    algebraic[20] = 0.846554/(0.00420000*exp(states[0]/17.0000)+0.000150000*exp(-states[0]/21.6000))
    rates[9] = (algebraic[6]-states[9])/algebraic[20]
    algebraic[21] = 0.846554/(0.0372000*exp(states[0]/15.9000)+0.000960000*exp(-states[0]/22.5000))
    rates[10] = (algebraic[6]-states[10])/algebraic[21]
    algebraic[7] = 1.00000/(1.00000+exp((states[0]+28.6000)/17.1000))
    algebraic[22] = 1.00000/(0.100000*exp(-states[0]/54.6450)+0.656000*exp(states[0]/106.157))
    rates[11] = (algebraic[7]-states[11])/algebraic[22]
    algebraic[9] = 1.00000/(1.00000+exp((states[0]+49.0000)/13.0000))
    algebraic[24] = 0.600000*(65.1700/(0.570000*exp(-0.0800000*(states[0]+44.0000))+0.0650000*exp(0.100000*(states[0]+45.9300)))+10.1000)
    rates[13] = (algebraic[9]-states[13])/algebraic[24]
    algebraic[10] = 1.00000/(1.00000+exp(-(states[0]-19.3000)/15.0000))
    algebraic[25] = 0.660000*1.40000*(15.5900/(1.03700*exp(0.0900000*(states[0]+30.6100))+0.369000*exp(-0.120000*(states[0]+23.8400)))+2.98000)
    rates[14] = (algebraic[10]-states[14])/algebraic[25]
    algebraic[11] = 1.00000/(1.00000+exp((states[0]+64.0000)/13.5000))
    algebraic[26] = 0.716653/(exp(-(states[0]+386.900)/45.3020)+exp((states[0]-73.0800)/19.2310))
    rates[15] = (algebraic[11]-states[15])/algebraic[26]
    algebraic[1] = 1.00000/(1.00000+exp(-(states[0]+14.1000)/6.00000))
    algebraic[15] = (-0.0283900*(states[0]+35.0000))/(exp(-(states[0]+35.0000)/2.50000)-1.00000)-(0.0849000*states[0])/(exp(-states[0]/4.80800)-1.00000)
    algebraic[30] = (0.0114300*(states[0]-5.00000))/(exp((states[0]-5.00000)/2.50000)-1.00000)
    algebraic[35] = 1.00000/(algebraic[15]+algebraic[30])
    rates[4] = (algebraic[1]-states[4])/algebraic[35]
    algebraic[8] = 0.0140000/(1.00000+exp(-(states[0]-40.0000)/9.00000))
    algebraic[23] = 0.00100000*exp(-states[0]/45.0000)
    algebraic[31] = algebraic[8]/(algebraic[8]+algebraic[23])
    algebraic[36] = 1.00000/(algebraic[8]+algebraic[23])
    rates[12] = (algebraic[31]-states[12])/algebraic[36]
    algebraic[12] = 1.00000/(1.00000+exp(-(states[0]+57.0000)/5.00000))
    algebraic[27] = 1.00000/(0.150000*exp(-states[0]/11.0000)+0.200000*exp(-states[0]/700.000))
    algebraic[32] = 1.00000/(16.0000*exp(states[0]/8.00000)+15.0000*exp(states[0]/50.0000))
    algebraic[37] = 1.00000/(algebraic[27]+algebraic[32])
    rates[16] = (algebraic[12]-states[16])/algebraic[37]
    algebraic[13] = 1.00000/(3100.00*exp(states[0]/13.0000)+700.000*exp(states[0]/70.0000))
    algebraic[28] = 1.00000/(95.0000*exp(-states[0]/10.0000)+50.0000*exp(-states[0]/700.000))+0.000229000/(1.00000+exp(-states[0]/5.00000))
    algebraic[33] = algebraic[13]/(algebraic[13]+algebraic[28])
    algebraic[38] = 6.65000/(algebraic[13]+algebraic[28])
    rates[17] = (algebraic[33]-states[17])/algebraic[38]
    algebraic[29] = ((constants[0]*constants[1])/constants[2])*log(constants[5]/states[2])
    algebraic[40] = constants[63]*(states[0]-algebraic[29])*(0.600000*states[10]+0.400000*states[9])*states[11]
    algebraic[41] = ((constants[0]*constants[1])/constants[2])*log((constants[5]+0.120000*constants[4])/(states[2]+0.120000*states[1]))
    algebraic[42] = constants[12]*(states[0]-algebraic[41])*(power(states[12], 2.00000))
    algebraic[43] = constants[13]*(states[0]-algebraic[29])*states[13]*states[14]
    algebraic[44] = constants[14]*(states[0]-algebraic[29])*states[14]
    algebraic[0] = ((constants[0]*constants[1])/constants[2])*log(constants[4]/states[1])
    algebraic[51] = constants[22]*(power(1.00000+power(constants[20]/constants[5], 1.20000), -1.00000))*(power(1.00000+power(constants[21]/states[1], 1.30000), -1.00000))*(power(1.00000+exp(-((states[0]-algebraic[0])+120.000)/30.0000), -1.00000))
    algebraic[50] = (constants[64]*(states[2]-constants[5]*exp((-states[0]*constants[2])/(constants[0]*constants[1]))))/1.00000
    algebraic[46] = constants[16]*(states[0]-algebraic[29])*(power(states[15], 2.00000))
    rates[2] = (-(algebraic[40]+algebraic[42]+algebraic[43]+algebraic[44]+algebraic[46]+algebraic[50]+-2.00000*algebraic[51])*constants[3])/(1.00000*constants[2]*(constants[44]+constants[47]))
    algebraic[39] = constants[10]*(states[0]-constants[11])*states[7]*states[8]
    algebraic[34] = constants[6]*(states[0]-constants[7])*states[4]*states[5]*states[6]
    algebraic[45] = constants[15]*(states[0]-algebraic[0])*(power(states[15], 2.00000))
    algebraic[47] = algebraic[45]+algebraic[46]
    algebraic[48] = constants[17]*(states[0]-constants[18])*states[16]*states[17]
    algebraic[49] = constants[19]*(states[0]-algebraic[0])
    algebraic[53] = exp((-constants[25]*states[0]*constants[2])/(2.00000*constants[0]*constants[1]))
    algebraic[59] = 1.00000+(constants[36]/constants[35])*(1.00000+exp((constants[26]*states[0]*constants[2])/(constants[0]*constants[1])))+(constants[4]/constants[33])*(1.00000+constants[4]/constants[34])*(1.00000+constants[4]/constants[32])
    algebraic[61] = ((((constants[4]/constants[33])*constants[4])/constants[34])*(1.00000+constants[4]/constants[32])*exp((-constants[25]*states[0]*constants[2])/(2.00000*constants[0]*constants[1])))/algebraic[59]
    algebraic[60] = ((constants[36]/constants[35])*exp((constants[26]*states[0]*constants[2])/(constants[0]*constants[1])))/algebraic[59]
    algebraic[57] = exp((constants[25]*states[0]*constants[2])/(2.00000*constants[0]*constants[1]))
    algebraic[52] = states[1]/(constants[27]+states[1])
    algebraic[62] = algebraic[53]*constants[65]*(algebraic[61]+algebraic[60])+algebraic[60]*algebraic[57]*(algebraic[52]+algebraic[53])
    algebraic[54] = 1.00000+(states[3]/constants[28])*(1.00000+exp((-constants[24]*states[0]*constants[2])/(constants[0]*constants[1]))+states[1]/constants[31])+(states[1]/constants[29])*(1.00000+(states[1]/constants[30])*(1.00000+states[1]/constants[27]))
    algebraic[55] = ((states[3]/constants[28])*exp((-constants[24]*states[0]*constants[2])/(constants[0]*constants[1])))/algebraic[54]
    algebraic[56] = ((((states[1]/constants[29])*states[1])/constants[30])*(1.00000+states[1]/constants[27])*exp((constants[25]*states[0]*constants[2])/(2.00000*constants[0]*constants[1])))/algebraic[54]
    algebraic[58] = algebraic[57]*algebraic[52]*(algebraic[56]+algebraic[55])+algebraic[53]*algebraic[55]*(constants[65]+algebraic[57])
    algebraic[63] = algebraic[56]*algebraic[52]*(algebraic[61]+algebraic[60])+algebraic[55]*algebraic[61]*(algebraic[52]+algebraic[53])
    algebraic[64] = algebraic[61]*constants[65]*(algebraic[56]+algebraic[55])+algebraic[56]*algebraic[60]*(constants[65]+algebraic[57])
    algebraic[65] = (constants[23]*(algebraic[58]*algebraic[60]-algebraic[62]*algebraic[55]))/(algebraic[62]+algebraic[58]+algebraic[63]+algebraic[64])
    rates[0] = -(algebraic[34]+algebraic[39]+algebraic[40]+algebraic[42]+algebraic[43]+algebraic[44]+algebraic[47]+algebraic[48]+algebraic[49]+algebraic[50]+algebraic[51]+algebraic[65])/1.00000
    rates[1] = (-(algebraic[45]+algebraic[48]+algebraic[49]+3.00000*algebraic[51]+3.00000*algebraic[65])*constants[3])/(1.00000*constants[2]*(constants[44]+constants[47]))
    algebraic[66] = (states[3]-states[19])/constants[37]
    algebraic[67] = (constants[41]*(states[20]-states[3]))/(1.00000+power(constants[39]/states[3], 2.00000))
    algebraic[69] = constants[55]*states[3]*(1.00000-states[23])-constants[60]*states[23]
    rates[3] = ((-((algebraic[34]+algebraic[39])-2.00000*algebraic[65])*constants[3])/(1.00000*2.00000*constants[2])+algebraic[67]*constants[45])/constants[47]-(algebraic[66]+constants[49]*algebraic[69])
    rates[23] = algebraic[69]
    algebraic[68] = constants[40]/(1.00000+constants[42]/states[19])
    algebraic[70] = (states[18]-states[20])/constants[38]
    rates[18] = algebraic[68]-(algebraic[70]*constants[45])/constants[46]
    algebraic[71] = constants[52]*states[19]*(1.00000-states[24])-constants[57]*states[24]
    rates[24] = algebraic[71]
    algebraic[73] = constants[56]*states[20]*(1.00000-states[26])-constants[61]*states[26]
    rates[20] = algebraic[70]-(algebraic[67]+constants[51]*algebraic[73])
    algebraic[72] = constants[54]*states[19]*(1.00000-(states[25]+states[21]))-constants[58]*states[25]
    rates[25] = algebraic[72]
    rates[26] = algebraic[73]
    algebraic[74] = constants[55]*states[19]*(1.00000-states[22])-constants[60]*states[22]
    rates[19] = (algebraic[66]*constants[47]-algebraic[68]*constants[46])/constants[44]-(constants[49]*algebraic[74]+constants[50]*algebraic[71]+constants[48]*algebraic[72])
    rates[22] = algebraic[74]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[14] = constants[53]*constants[43]*(1.00000-(states[25]+states[21]))-constants[59]*states[21]
    algebraic[2] = 1.00000/(1.00000+exp((states[0]+30.0000)/5.00000))
    algebraic[16] = 44.3000+257.100*exp(-(power((states[0]+32.5000)/13.9000, 2.00000)))
    algebraic[3] = constants[9]/(constants[9]+states[3])
    algebraic[17] = algebraic[3]/constants[62]
    algebraic[4] = 1.00000/(1.00000+exp(-(states[0]+26.3000)/6.00000))
    algebraic[18] = 1.00000/(1.06800*exp((states[0]+26.3000)/30.0000)+1.06800*exp(-(states[0]+26.3000)/30.0000))
    algebraic[5] = 1.00000/(1.00000+exp((states[0]+61.7000)/5.60000))
    algebraic[19] = 1.00000/(0.0153000*exp(-(states[0]+61.7000)/83.3000)+0.0150000*exp((states[0]+61.7000)/15.3800))
    algebraic[6] = 1.00000/(1.00000+exp(-(states[0]+23.2000)/10.6000))
    algebraic[20] = 0.846554/(0.00420000*exp(states[0]/17.0000)+0.000150000*exp(-states[0]/21.6000))
    algebraic[21] = 0.846554/(0.0372000*exp(states[0]/15.9000)+0.000960000*exp(-states[0]/22.5000))
    algebraic[7] = 1.00000/(1.00000+exp((states[0]+28.6000)/17.1000))
    algebraic[22] = 1.00000/(0.100000*exp(-states[0]/54.6450)+0.656000*exp(states[0]/106.157))
    algebraic[9] = 1.00000/(1.00000+exp((states[0]+49.0000)/13.0000))
    algebraic[24] = 0.600000*(65.1700/(0.570000*exp(-0.0800000*(states[0]+44.0000))+0.0650000*exp(0.100000*(states[0]+45.9300)))+10.1000)
    algebraic[10] = 1.00000/(1.00000+exp(-(states[0]-19.3000)/15.0000))
    algebraic[25] = 0.660000*1.40000*(15.5900/(1.03700*exp(0.0900000*(states[0]+30.6100))+0.369000*exp(-0.120000*(states[0]+23.8400)))+2.98000)
    algebraic[11] = 1.00000/(1.00000+exp((states[0]+64.0000)/13.5000))
    algebraic[26] = 0.716653/(exp(-(states[0]+386.900)/45.3020)+exp((states[0]-73.0800)/19.2310))
    algebraic[1] = 1.00000/(1.00000+exp(-(states[0]+14.1000)/6.00000))
    algebraic[15] = (-0.0283900*(states[0]+35.0000))/(exp(-(states[0]+35.0000)/2.50000)-1.00000)-(0.0849000*states[0])/(exp(-states[0]/4.80800)-1.00000)
    algebraic[30] = (0.0114300*(states[0]-5.00000))/(exp((states[0]-5.00000)/2.50000)-1.00000)
    algebraic[35] = 1.00000/(algebraic[15]+algebraic[30])
    algebraic[8] = 0.0140000/(1.00000+exp(-(states[0]-40.0000)/9.00000))
    algebraic[23] = 0.00100000*exp(-states[0]/45.0000)
    algebraic[31] = algebraic[8]/(algebraic[8]+algebraic[23])
    algebraic[36] = 1.00000/(algebraic[8]+algebraic[23])
    algebraic[12] = 1.00000/(1.00000+exp(-(states[0]+57.0000)/5.00000))
    algebraic[27] = 1.00000/(0.150000*exp(-states[0]/11.0000)+0.200000*exp(-states[0]/700.000))
    algebraic[32] = 1.00000/(16.0000*exp(states[0]/8.00000)+15.0000*exp(states[0]/50.0000))
    algebraic[37] = 1.00000/(algebraic[27]+algebraic[32])
    algebraic[13] = 1.00000/(3100.00*exp(states[0]/13.0000)+700.000*exp(states[0]/70.0000))
    algebraic[28] = 1.00000/(95.0000*exp(-states[0]/10.0000)+50.0000*exp(-states[0]/700.000))+0.000229000/(1.00000+exp(-states[0]/5.00000))
    algebraic[33] = algebraic[13]/(algebraic[13]+algebraic[28])
    algebraic[38] = 6.65000/(algebraic[13]+algebraic[28])
    algebraic[29] = ((constants[0]*constants[1])/constants[2])*log(constants[5]/states[2])
    algebraic[40] = constants[63]*(states[0]-algebraic[29])*(0.600000*states[10]+0.400000*states[9])*states[11]
    algebraic[41] = ((constants[0]*constants[1])/constants[2])*log((constants[5]+0.120000*constants[4])/(states[2]+0.120000*states[1]))
    algebraic[42] = constants[12]*(states[0]-algebraic[41])*(power(states[12], 2.00000))
    algebraic[43] = constants[13]*(states[0]-algebraic[29])*states[13]*states[14]
    algebraic[44] = constants[14]*(states[0]-algebraic[29])*states[14]
    algebraic[0] = ((constants[0]*constants[1])/constants[2])*log(constants[4]/states[1])
    algebraic[51] = constants[22]*(power(1.00000+power(constants[20]/constants[5], 1.20000), -1.00000))*(power(1.00000+power(constants[21]/states[1], 1.30000), -1.00000))*(power(1.00000+exp(-((states[0]-algebraic[0])+120.000)/30.0000), -1.00000))
    algebraic[50] = (constants[64]*(states[2]-constants[5]*exp((-states[0]*constants[2])/(constants[0]*constants[1]))))/1.00000
    algebraic[46] = constants[16]*(states[0]-algebraic[29])*(power(states[15], 2.00000))
    algebraic[39] = constants[10]*(states[0]-constants[11])*states[7]*states[8]
    algebraic[34] = constants[6]*(states[0]-constants[7])*states[4]*states[5]*states[6]
    algebraic[45] = constants[15]*(states[0]-algebraic[0])*(power(states[15], 2.00000))
    algebraic[47] = algebraic[45]+algebraic[46]
    algebraic[48] = constants[17]*(states[0]-constants[18])*states[16]*states[17]
    algebraic[49] = constants[19]*(states[0]-algebraic[0])
    algebraic[53] = exp((-constants[25]*states[0]*constants[2])/(2.00000*constants[0]*constants[1]))
    algebraic[59] = 1.00000+(constants[36]/constants[35])*(1.00000+exp((constants[26]*states[0]*constants[2])/(constants[0]*constants[1])))+(constants[4]/constants[33])*(1.00000+constants[4]/constants[34])*(1.00000+constants[4]/constants[32])
    algebraic[61] = ((((constants[4]/constants[33])*constants[4])/constants[34])*(1.00000+constants[4]/constants[32])*exp((-constants[25]*states[0]*constants[2])/(2.00000*constants[0]*constants[1])))/algebraic[59]
    algebraic[60] = ((constants[36]/constants[35])*exp((constants[26]*states[0]*constants[2])/(constants[0]*constants[1])))/algebraic[59]
    algebraic[57] = exp((constants[25]*states[0]*constants[2])/(2.00000*constants[0]*constants[1]))
    algebraic[52] = states[1]/(constants[27]+states[1])
    algebraic[62] = algebraic[53]*constants[65]*(algebraic[61]+algebraic[60])+algebraic[60]*algebraic[57]*(algebraic[52]+algebraic[53])
    algebraic[54] = 1.00000+(states[3]/constants[28])*(1.00000+exp((-constants[24]*states[0]*constants[2])/(constants[0]*constants[1]))+states[1]/constants[31])+(states[1]/constants[29])*(1.00000+(states[1]/constants[30])*(1.00000+states[1]/constants[27]))
    algebraic[55] = ((states[3]/constants[28])*exp((-constants[24]*states[0]*constants[2])/(constants[0]*constants[1])))/algebraic[54]
    algebraic[56] = ((((states[1]/constants[29])*states[1])/constants[30])*(1.00000+states[1]/constants[27])*exp((constants[25]*states[0]*constants[2])/(2.00000*constants[0]*constants[1])))/algebraic[54]
    algebraic[58] = algebraic[57]*algebraic[52]*(algebraic[56]+algebraic[55])+algebraic[53]*algebraic[55]*(constants[65]+algebraic[57])
    algebraic[63] = algebraic[56]*algebraic[52]*(algebraic[61]+algebraic[60])+algebraic[55]*algebraic[61]*(algebraic[52]+algebraic[53])
    algebraic[64] = algebraic[61]*constants[65]*(algebraic[56]+algebraic[55])+algebraic[56]*algebraic[60]*(constants[65]+algebraic[57])
    algebraic[65] = (constants[23]*(algebraic[58]*algebraic[60]-algebraic[62]*algebraic[55]))/(algebraic[62]+algebraic[58]+algebraic[63]+algebraic[64])
    algebraic[66] = (states[3]-states[19])/constants[37]
    algebraic[67] = (constants[41]*(states[20]-states[3]))/(1.00000+power(constants[39]/states[3], 2.00000))
    algebraic[69] = constants[55]*states[3]*(1.00000-states[23])-constants[60]*states[23]
    algebraic[68] = constants[40]/(1.00000+constants[42]/states[19])
    algebraic[70] = (states[18]-states[20])/constants[38]
    algebraic[71] = constants[52]*states[19]*(1.00000-states[24])-constants[57]*states[24]
    algebraic[73] = constants[56]*states[20]*(1.00000-states[26])-constants[61]*states[26]
    algebraic[72] = constants[54]*states[19]*(1.00000-(states[25]+states[21]))-constants[58]*states[25]
    algebraic[74] = constants[55]*states[19]*(1.00000-states[22])-constants[60]*states[22]
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
        self.R = 8314400000000000
        self.T = 310.15
        self.F = 96485000000000000
        self.Cm = 32
        self.Nao = 140
        self.Ko = 5.4
        self.g_CaL = 0.58
        self.E_CaL = 45
        self.beta_fCa = 60
        self.Km_fCa = 0.00035
        self.g_CaT = 0.458
        self.E_CaT = 45
        self.g_Ks = 0.0259
        self.g_to = 0.18
        self.g_sus = 0.02
        self.g_h_Na = 0.1437375
        self.g_h_K = 0.2312625
        self.g_st = 0.015
        self.E_st = 37.4
        self.g_b_Na = 0.0054
        self.Km_Kp = 1.4
        self.Km_Nap = 14
        self.i_NaK_max = 3.6
        self.kNaCa = 125
        self.Qci = 0.1369
        self.Qn = 0.4315
        self.Qco = 0
        self.K3ni = 26.44
        self.Kci = 0.0207
        self.K1ni = 395.3
        self.K2ni = 2.289
        self.Kcni = 26.44
        self.K3no = 4.663
        self.K1no = 1628
        self.K2no = 561.4
        self.Kco = 3.663
        self.Cao = 2
        self.tau_dif_Ca = 0.04
        self.tau_tr = 60
        self.K_rel = 0.0012
        self.P_up = 0.005
        self.P_rel = 0.5
        self.K_up = 0.0006
        self.Mgi = 2.5
        self.V_i = 0.0000000000015835
        self.V_rel = 0.0000000000000042223
        self.V_up = 0.000000000000040816
        self.V_sub = 0.000000000000035098
        self.TMC_tot = 0.062
        self.CM_tot = 0.045
        self.TC_tot = 0.031
        self.CQ_tot = 10
        self.kf_TC = 88.8
        self.kf_TMM = 2.277
        self.kf_TMC = 227.7
        self.kf_CM = 227.7
        self.kf_CQ = 0.534
        self.kb_TC = 0.446
        self.kb_TMC = 0.00751
        self.kb_TMM = 0.751
        self.kb_CM = 0.542
        self.kb_CQ = 0.445

    def to_dict(self):
        return {
            "R": self.R,
            "T": self.T,
            "F": self.F,
            "Cm": self.Cm,
            "Nao": self.Nao,
            "Ko": self.Ko,
            "g_CaL": self.g_CaL,
            "E_CaL": self.E_CaL,
            "beta_fCa": self.beta_fCa,
            "Km_fCa": self.Km_fCa,
            "g_CaT": self.g_CaT,
            "E_CaT": self.E_CaT,
            "g_Ks": self.g_Ks,
            "g_to": self.g_to,
            "g_sus": self.g_sus,
            "g_h_Na": self.g_h_Na,
            "g_h_K": self.g_h_K,
            "g_st": self.g_st,
            "E_st": self.E_st,
            "g_b_Na": self.g_b_Na,
            "Km_Kp": self.Km_Kp,
            "Km_Nap": self.Km_Nap,
            "i_NaK_max": self.i_NaK_max,
            "kNaCa": self.kNaCa,
            "Qci": self.Qci,
            "Qn": self.Qn,
            "Qco": self.Qco,
            "K3ni": self.K3ni,
            "Kci": self.Kci,
            "K1ni": self.K1ni,
            "K2ni": self.K2ni,
            "Kcni": self.Kcni,
            "K3no": self.K3no,
            "K1no": self.K1no,
            "K2no": self.K2no,
            "Kco": self.Kco,
            "Cao": self.Cao,
            "tau_dif_Ca": self.tau_dif_Ca,
            "tau_tr": self.tau_tr,
            "K_rel": self.K_rel,
            "P_up": self.P_up,
            "P_rel": self.P_rel,
            "K_up": self.K_up,
            "Mgi": self.Mgi,
            "V_i": self.V_i,
            "V_rel": self.V_rel,
            "V_up": self.V_up,
            "V_sub": self.V_sub,
            "TMC_tot": self.TMC_tot,
            "CM_tot": self.CM_tot,
            "TC_tot": self.TC_tot,
            "CQ_tot": self.CQ_tot,
            "kf_TC": self.kf_TC,
            "kf_TMM": self.kf_TMM,
            "kf_TMC": self.kf_TMC,
            "kf_CM": self.kf_CM,
            "kf_CQ": self.kf_CQ,
            "kb_TC": self.kb_TC,
            "kb_TMC": self.kb_TMC,
            "kb_TMM": self.kb_TMM,
            "kb_CM": self.kb_CM,
            "kb_CQ": self.kb_CQ,
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
        y0=[-58.600291137693, 9.438646305915, 139.984146485614, 0.00019074741, 0.000602055134, 0.626999773853, 0.589580408056, 0.004571884917, 0.249637570396, 0.629323128348, 0.3493633709533, 0.852396631172, 0.054409723782, 0.531446952485, 0.005550489445, 0.067156687129, 0.426018100136, 0.333330378068, 1.462338380106, 0.000312494921, 0.296742023718, 0.350600895635, 0.116947220413, 0.074631965653, 0.059206293446, 0.602955114871, 0.260317260703],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "kurata_hisatome_imanishi_shibamoto_2002"
        self.curve_names = [
            "V",
            "Nai",
            "Ki",
            "Ca_sub",
            "d",
            "f",
            "fCa",
            "d_1",
            "f_1",
            "paS",
            "paF",
            "piy",
            "n",
            "q",
            "r",
            "y",
            "qa",
            "qi",
            "Ca_up",
            "Cai",
            "Ca_rel",
            "fTMM",
            "fCMi",
            "fCMs",
            "fTC",
            "fTMC",
            "fCQ",
        ]
        self.state_names = ['V', 'Nai', 'Ki', 'Ca_sub', 'd', 'f', 'fCa', 'd_1', 'f_1', 'paS', 'paF', 'piy', 'n', 'q', 'r', 'y', 'qa', 'qi', 'Ca_up', 'Cai', 'Ca_rel', 'fTMM', 'fCMi', 'fCMs', 'fTC', 'fTMC', 'fCQ']
        self.algebraic_names = ['E_Na', 'd_infinity', 'f_infinity', 'fCa_infinity', 'd_infinity_1', 'f_infinity_1', 'pa_infinity', 'pi_infinity', 'alpha_n', 'q_infinity', 'r_infinity', 'y_infinity', 'qa_infinity', 'alpha_qi', 'delta_fTMM', 'alpha_d', 'tau_f', 'tau_fCa', 'tau_d', 'tau_f_1', 'tau_paS', 'tau_paF', 'tau_pi', 'beta_n', 'tau_q', 'tau_r', 'tau_y', 'alpha_qa', 'beta_qi', 'E_K', 'beta_d', 'n_infinity', 'beta_qa', 'qi_infinity', 'i_CaL', 'tau_d_1', 'tau_n', 'tau_qa', 'tau_qi', 'i_CaT', 'i_Kr', 'E_Ks', 'i_Ks', 'i_to', 'i_sus', 'i_h_Na', 'i_h_K', 'i_h', 'i_st', 'i_b_Na', 'i_K_ACh', 'i_NaK', 'k43', 'k41', 'di', 'k12', 'k14', 'k32', 'x2', 'do', 'k21', 'k23', 'x1', 'x3', 'x4', 'i_NaCa', 'j_Ca_dif', 'j_rel', 'j_up', 'delta_fCMs', 'j_tr', 'delta_fTC', 'delta_fTMC', 'delta_fCQ', 'delta_fCMi']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 66
        p = self.params

        # direct mapping
        c[0] = p.R
        c[1] = p.T
        c[2] = p.F
        c[3] = p.Cm
        c[4] = p.Nao
        c[5] = p.Ko
        c[6] = p.g_CaL
        c[7] = p.E_CaL
        c[8] = p.beta_fCa
        c[9] = p.Km_fCa
        c[10] = p.g_CaT
        c[11] = p.E_CaT
        c[12] = p.g_Ks
        c[13] = p.g_to
        c[14] = p.g_sus
        c[15] = p.g_h_Na
        c[16] = p.g_h_K
        c[17] = p.g_st
        c[18] = p.E_st
        c[19] = p.g_b_Na
        c[20] = p.Km_Kp
        c[21] = p.Km_Nap
        c[22] = p.i_NaK_max
        c[23] = p.kNaCa
        c[24] = p.Qci
        c[25] = p.Qn
        c[26] = p.Qco
        c[27] = p.K3ni
        c[28] = p.Kci
        c[29] = p.K1ni
        c[30] = p.K2ni
        c[31] = p.Kcni
        c[32] = p.K3no
        c[33] = p.K1no
        c[34] = p.K2no
        c[35] = p.Kco
        c[36] = p.Cao
        c[37] = p.tau_dif_Ca
        c[38] = p.tau_tr
        c[39] = p.K_rel
        c[40] = p.P_up
        c[41] = p.P_rel
        c[42] = p.K_up
        c[43] = p.Mgi
        c[44] = p.V_i
        c[45] = p.V_rel
        c[46] = p.V_up
        c[47] = p.V_sub
        c[48] = p.TMC_tot
        c[49] = p.CM_tot
        c[50] = p.TC_tot
        c[51] = p.CQ_tot
        c[52] = p.kf_TC
        c[53] = p.kf_TMM
        c[54] = p.kf_TMC
        c[55] = p.kf_CM
        c[56] = p.kf_CQ
        c[57] = p.kb_TC
        c[58] = p.kb_TMC
        c[59] = p.kb_TMM
        c[60] = p.kb_CM
        c[61] = p.kb_CQ

        # derived constants
        c[62] = c[9]*c[8]
        c[63] = 0.0250000*(power(c[5]/1.00000, 0.590000))
        c[64] = 0.00110000*(power(c[5]/1.00000, 0.410000))
        c[65] = c[4]/(c[32]+c[4])

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
