# Size of variable arrays:
sizeAlgebraic = 70
sizeStates = 30
sizeConstants = 51
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (second)"
    legend_states[0] = "V in component membrane (millivolt)"
    legend_constants[0] = "R in component membrane (millijoule_per_mole_kelvin)"
    legend_constants[1] = "T in component membrane (kelvin)"
    legend_constants[2] = "F in component membrane (coulomb_per_mole)"
    legend_constants[3] = "Cm in component membrane (nanoF)"
    legend_algebraic[0] = "Q_tot in component membrane (millivolt)"
    legend_algebraic[37] = "i_Na in component sodium_current (picoA)"
    legend_algebraic[41] = "i_Ca_L in component L_type_Ca_channel (picoA)"
    legend_algebraic[44] = "i_t in component Ca_independent_transient_outward_K_current (picoA)"
    legend_algebraic[45] = "i_Kur in component ultra_rapid_K_current (picoA)"
    legend_algebraic[46] = "i_K1 in component inward_rectifier (picoA)"
    legend_algebraic[49] = "i_Kr in component delayed_rectifier_K_currents (picoA)"
    legend_algebraic[47] = "i_Ks in component delayed_rectifier_K_currents (picoA)"
    legend_algebraic[50] = "i_B_Na in component background_currents (picoA)"
    legend_algebraic[52] = "i_B_Ca in component background_currents (picoA)"
    legend_algebraic[54] = "i_NaK in component sodium_potassium_pump (picoA)"
    legend_algebraic[55] = "i_CaP in component sarcolemmal_calcium_pump_current (picoA)"
    legend_algebraic[56] = "i_NaCa in component Na_Ca_ion_exchanger_current (picoA)"
    legend_algebraic[57] = "i_KACh in component ACh_dependent_K_current (picoA)"
    legend_algebraic[59] = "I in component membrane (pA_per_nF)"
    legend_algebraic[24] = "i_Stim in component membrane (pA_per_nF)"
    legend_constants[4] = "stim_offset in component membrane (second)"
    legend_constants[5] = "stim_period in component membrane (second)"
    legend_constants[6] = "stim_duration in component membrane (second)"
    legend_constants[7] = "stim_amplitude in component membrane (pA_per_nF)"
    legend_algebraic[1] = "past in component membrane (second)"
    legend_algebraic[35] = "E_Na in component sodium_current (millivolt)"
    legend_constants[8] = "P_Na in component sodium_current (nanolitre_per_second)"
    legend_states[1] = "Na_c in component cleft_space_ion_concentrations (millimolar)"
    legend_states[2] = "Na_i in component intracellular_ion_concentrations (millimolar)"
    legend_states[3] = "m in component sodium_current_m_gate (dimensionless)"
    legend_states[4] = "h1 in component sodium_current_h1_gate (dimensionless)"
    legend_states[5] = "h2 in component sodium_current_h2_gate (dimensionless)"
    legend_algebraic[14] = "m_infinity in component sodium_current_m_gate (dimensionless)"
    legend_algebraic[2] = "m_factor in component sodium_current_m_gate (dimensionless)"
    legend_algebraic[26] = "tau_m in component sodium_current_m_gate (second)"
    legend_algebraic[3] = "h_infinity in component sodium_current_h1_gate (dimensionless)"
    legend_algebraic[15] = "h_factor in component sodium_current_h1_gate (dimensionless)"
    legend_algebraic[27] = "tau_h1 in component sodium_current_h1_gate (second)"
    legend_algebraic[28] = "tau_h2 in component sodium_current_h2_gate (second)"
    legend_constants[9] = "g_Ca_L in component L_type_Ca_channel (nanoS)"
    legend_constants[10] = "E_Ca_app in component L_type_Ca_channel (millivolt)"
    legend_algebraic[39] = "f_Ca in component L_type_Ca_channel (dimensionless)"
    legend_constants[11] = "k_Ca in component L_type_Ca_channel (millimolar)"
    legend_states[6] = "Ca_d in component intracellular_ion_concentrations (millimolar)"
    legend_states[7] = "d_L in component L_type_Ca_channel_d_L_gate (dimensionless)"
    legend_states[8] = "f_L1 in component L_type_Ca_channel_f_L1_gate (dimensionless)"
    legend_states[9] = "f_L2 in component L_type_Ca_channel_f_L2_gate (dimensionless)"
    legend_algebraic[4] = "d_L_infinity in component L_type_Ca_channel_d_L_gate (dimensionless)"
    legend_algebraic[16] = "d_L_factor in component L_type_Ca_channel_d_L_gate (dimensionless)"
    legend_algebraic[29] = "tau_d_L in component L_type_Ca_channel_d_L_gate (second)"
    legend_algebraic[5] = "f_L_infinity in component L_type_Ca_channel_f_L1_gate (dimensionless)"
    legend_algebraic[17] = "f_L_factor in component L_type_Ca_channel_f_L1_gate (millivolt)"
    legend_algebraic[30] = "tau_f_L1 in component L_type_Ca_channel_f_L1_gate (second)"
    legend_algebraic[31] = "tau_f_L2 in component L_type_Ca_channel_f_L2_gate (second)"
    legend_algebraic[43] = "E_K in component Ca_independent_transient_outward_K_current (millivolt)"
    legend_constants[12] = "g_t in component Ca_independent_transient_outward_K_current (nanoS)"
    legend_states[10] = "K_c in component cleft_space_ion_concentrations (millimolar)"
    legend_states[11] = "K_i in component intracellular_ion_concentrations (millimolar)"
    legend_states[12] = "r in component Ca_independent_transient_outward_K_current_r_gate (dimensionless)"
    legend_states[13] = "s in component Ca_independent_transient_outward_K_current_s_gate (dimensionless)"
    legend_algebraic[18] = "tau_r in component Ca_independent_transient_outward_K_current_r_gate (second)"
    legend_algebraic[6] = "r_infinity in component Ca_independent_transient_outward_K_current_r_gate (dimensionless)"
    legend_algebraic[32] = "tau_s in component Ca_independent_transient_outward_K_current_s_gate (second)"
    legend_algebraic[7] = "s_infinity in component Ca_independent_transient_outward_K_current_s_gate (dimensionless)"
    legend_algebraic[19] = "s_factor in component Ca_independent_transient_outward_K_current_s_gate (dimensionless)"
    legend_constants[13] = "g_kur in component ultra_rapid_K_current (nanoS)"
    legend_states[14] = "a_ur in component ultra_rapid_K_current_aur_gate (dimensionless)"
    legend_states[15] = "i_ur in component ultra_rapid_K_current_iur_gate (dimensionless)"
    legend_algebraic[8] = "a_ur_infinity in component ultra_rapid_K_current_aur_gate (dimensionless)"
    legend_algebraic[20] = "tau_a_ur in component ultra_rapid_K_current_aur_gate (second)"
    legend_algebraic[9] = "i_ur_infinity in component ultra_rapid_K_current_iur_gate (dimensionless)"
    legend_algebraic[21] = "tau_i_ur in component ultra_rapid_K_current_iur_gate (second)"
    legend_constants[14] = "g_K1 in component inward_rectifier (nanoS)"
    legend_constants[15] = "g_Ks in component delayed_rectifier_K_currents (nanoS)"
    legend_constants[16] = "g_Kr in component delayed_rectifier_K_currents (nanoS)"
    legend_states[16] = "n in component delayed_rectifier_K_currents_n_gate (dimensionless)"
    legend_states[17] = "pa in component delayed_rectifier_K_currents_pa_gate (dimensionless)"
    legend_algebraic[48] = "pip in component delayed_rectifier_K_currents_pi_gate (dimensionless)"
    legend_algebraic[33] = "tau_n in component delayed_rectifier_K_currents_n_gate (second)"
    legend_algebraic[10] = "n_infinity in component delayed_rectifier_K_currents_n_gate (dimensionless)"
    legend_algebraic[22] = "n_factor in component delayed_rectifier_K_currents_n_gate (dimensionless)"
    legend_algebraic[34] = "tau_pa in component delayed_rectifier_K_currents_pa_gate (second)"
    legend_algebraic[23] = "pa_factor in component delayed_rectifier_K_currents_pa_gate (dimensionless)"
    legend_algebraic[11] = "p_a_infinity in component delayed_rectifier_K_currents_pa_gate (dimensionless)"
    legend_constants[17] = "g_B_Na in component background_currents (nanoS)"
    legend_constants[18] = "g_B_Ca in component background_currents (nanoS)"
    legend_algebraic[51] = "E_Ca in component background_currents (millivolt)"
    legend_states[18] = "Ca_c in component cleft_space_ion_concentrations (millimolar)"
    legend_states[19] = "Ca_i in component intracellular_ion_concentrations (millimolar)"
    legend_constants[19] = "K_NaK_K in component sodium_potassium_pump (millimolar)"
    legend_constants[20] = "i_NaK_max in component sodium_potassium_pump (picoA)"
    legend_constants[21] = "pow_K_NaK_Na_15 in component sodium_potassium_pump (millimolar15)"
    legend_algebraic[53] = "pow_Na_i_15 in component sodium_potassium_pump (millimolar15)"
    legend_constants[22] = "i_CaP_max in component sarcolemmal_calcium_pump_current (picoA)"
    legend_constants[23] = "k_CaP in component sarcolemmal_calcium_pump_current (millimolar)"
    legend_constants[24] = "K_NaCa in component Na_Ca_ion_exchanger_current (picoA_per_millimolar_4)"
    legend_constants[25] = "d_NaCa in component Na_Ca_ion_exchanger_current (per_millimolar_4)"
    legend_constants[26] = "gamma_Na in component Na_Ca_ion_exchanger_current (dimensionless)"
    legend_constants[27] = "ACh in component ACh_dependent_K_current (millimolar)"
    legend_constants[28] = "phi_Na_en in component intracellular_ion_concentrations (picoA)"
    legend_constants[29] = "Vol_i in component intracellular_ion_concentrations (nanolitre)"
    legend_constants[30] = "Vol_d in component intracellular_ion_concentrations (nanolitre)"
    legend_algebraic[58] = "i_di in component intracellular_ion_concentrations (picoA)"
    legend_constants[31] = "tau_di in component intracellular_ion_concentrations (second)"
    legend_algebraic[67] = "i_up in component Ca_handling_by_the_SR (picoA)"
    legend_algebraic[66] = "i_rel in component Ca_handling_by_the_SR (picoA)"
    legend_algebraic[63] = "J_O in component intracellular_Ca_buffering (per_second)"
    legend_states[20] = "O_C in component intracellular_Ca_buffering (dimensionless)"
    legend_states[21] = "O_TC in component intracellular_Ca_buffering (dimensionless)"
    legend_states[22] = "O_TMgC in component intracellular_Ca_buffering (dimensionless)"
    legend_states[23] = "O_TMgMg in component intracellular_Ca_buffering (dimensionless)"
    legend_states[24] = "O in component intracellular_Ca_buffering (dimensionless)"
    legend_algebraic[60] = "J_O_C in component intracellular_Ca_buffering (per_second)"
    legend_algebraic[61] = "J_O_TC in component intracellular_Ca_buffering (per_second)"
    legend_algebraic[62] = "J_O_TMgC in component intracellular_Ca_buffering (per_second)"
    legend_algebraic[12] = "J_O_TMgMg in component intracellular_Ca_buffering (per_second)"
    legend_constants[32] = "Mg_i in component intracellular_Ca_buffering (millimolar)"
    legend_constants[33] = "Vol_c in component cleft_space_ion_concentrations (nanolitre)"
    legend_constants[34] = "tau_Na in component cleft_space_ion_concentrations (second)"
    legend_constants[35] = "tau_K in component cleft_space_ion_concentrations (second)"
    legend_constants[36] = "tau_Ca in component cleft_space_ion_concentrations (second)"
    legend_constants[37] = "Na_b in component cleft_space_ion_concentrations (millimolar)"
    legend_constants[38] = "Ca_b in component cleft_space_ion_concentrations (millimolar)"
    legend_constants[39] = "K_b in component cleft_space_ion_concentrations (millimolar)"
    legend_algebraic[68] = "i_tr in component Ca_handling_by_the_SR (picoA)"
    legend_constants[40] = "I_up_max in component Ca_handling_by_the_SR (picoA)"
    legend_constants[41] = "k_cyca in component Ca_handling_by_the_SR (millimolar)"
    legend_constants[42] = "k_srca in component Ca_handling_by_the_SR (millimolar)"
    legend_constants[43] = "k_xcs in component Ca_handling_by_the_SR (dimensionless)"
    legend_constants[44] = "alpha_rel in component Ca_handling_by_the_SR (picoA_per_millimolar)"
    legend_states[25] = "Ca_rel in component Ca_handling_by_the_SR (millimolar)"
    legend_states[26] = "Ca_up in component Ca_handling_by_the_SR (millimolar)"
    legend_constants[45] = "Vol_up in component Ca_handling_by_the_SR (nanolitre)"
    legend_constants[46] = "Vol_rel in component Ca_handling_by_the_SR (nanolitre)"
    legend_algebraic[40] = "r_act in component Ca_handling_by_the_SR (per_second)"
    legend_algebraic[42] = "r_inact in component Ca_handling_by_the_SR (per_second)"
    legend_constants[47] = "r_recov in component Ca_handling_by_the_SR (per_second)"
    legend_algebraic[13] = "r_Ca_d_term in component Ca_handling_by_the_SR (dimensionless)"
    legend_algebraic[25] = "r_Ca_i_term in component Ca_handling_by_the_SR (dimensionless)"
    legend_algebraic[36] = "r_Ca_d_factor in component Ca_handling_by_the_SR (dimensionless)"
    legend_algebraic[38] = "r_Ca_i_factor in component Ca_handling_by_the_SR (dimensionless)"
    legend_algebraic[64] = "i_rel_f2 in component Ca_handling_by_the_SR (dimensionless)"
    legend_algebraic[65] = "i_rel_factor in component Ca_handling_by_the_SR (dimensionless)"
    legend_states[27] = "O_Calse in component Ca_handling_by_the_SR (dimensionless)"
    legend_algebraic[69] = "J_O_Calse in component Ca_handling_by_the_SR (per_second)"
    legend_states[28] = "F1 in component Ca_handling_by_the_SR (dimensionless)"
    legend_states[29] = "F2 in component Ca_handling_by_the_SR (dimensionless)"
    legend_constants[48] = "tau_tr in component Ca_handling_by_the_SR (second)"
    legend_constants[49] = "k_rel_i in component Ca_handling_by_the_SR (millimolar)"
    legend_constants[50] = "k_rel_d in component Ca_handling_by_the_SR (millimolar)"
    legend_rates[0] = "d/dt V in component membrane (millivolt)"
    legend_rates[3] = "d/dt m in component sodium_current_m_gate (dimensionless)"
    legend_rates[4] = "d/dt h1 in component sodium_current_h1_gate (dimensionless)"
    legend_rates[5] = "d/dt h2 in component sodium_current_h2_gate (dimensionless)"
    legend_rates[7] = "d/dt d_L in component L_type_Ca_channel_d_L_gate (dimensionless)"
    legend_rates[8] = "d/dt f_L1 in component L_type_Ca_channel_f_L1_gate (dimensionless)"
    legend_rates[9] = "d/dt f_L2 in component L_type_Ca_channel_f_L2_gate (dimensionless)"
    legend_rates[12] = "d/dt r in component Ca_independent_transient_outward_K_current_r_gate (dimensionless)"
    legend_rates[13] = "d/dt s in component Ca_independent_transient_outward_K_current_s_gate (dimensionless)"
    legend_rates[14] = "d/dt a_ur in component ultra_rapid_K_current_aur_gate (dimensionless)"
    legend_rates[15] = "d/dt i_ur in component ultra_rapid_K_current_iur_gate (dimensionless)"
    legend_rates[16] = "d/dt n in component delayed_rectifier_K_currents_n_gate (dimensionless)"
    legend_rates[17] = "d/dt pa in component delayed_rectifier_K_currents_pa_gate (dimensionless)"
    legend_rates[11] = "d/dt K_i in component intracellular_ion_concentrations (millimolar)"
    legend_rates[2] = "d/dt Na_i in component intracellular_ion_concentrations (millimolar)"
    legend_rates[19] = "d/dt Ca_i in component intracellular_ion_concentrations (millimolar)"
    legend_rates[6] = "d/dt Ca_d in component intracellular_ion_concentrations (millimolar)"
    legend_rates[20] = "d/dt O_C in component intracellular_Ca_buffering (dimensionless)"
    legend_rates[21] = "d/dt O_TC in component intracellular_Ca_buffering (dimensionless)"
    legend_rates[22] = "d/dt O_TMgC in component intracellular_Ca_buffering (dimensionless)"
    legend_rates[23] = "d/dt O_TMgMg in component intracellular_Ca_buffering (dimensionless)"
    legend_rates[24] = "d/dt O in component intracellular_Ca_buffering (dimensionless)"
    legend_rates[18] = "d/dt Ca_c in component cleft_space_ion_concentrations (millimolar)"
    legend_rates[10] = "d/dt K_c in component cleft_space_ion_concentrations (millimolar)"
    legend_rates[1] = "d/dt Na_c in component cleft_space_ion_concentrations (millimolar)"
    legend_rates[28] = "d/dt F1 in component Ca_handling_by_the_SR (dimensionless)"
    legend_rates[29] = "d/dt F2 in component Ca_handling_by_the_SR (dimensionless)"
    legend_rates[27] = "d/dt O_Calse in component Ca_handling_by_the_SR (dimensionless)"
    legend_rates[26] = "d/dt Ca_up in component Ca_handling_by_the_SR (millimolar)"
    legend_rates[25] = "d/dt Ca_rel in component Ca_handling_by_the_SR (millimolar)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = -74.031982
    constants[0] = 8314
    constants[1] = 306.15
    constants[2] = 96487
    constants[3] = 50
    constants[4] = 0
    constants[5] = 1
    constants[6] = 0.006
    constants[7] = -15
    constants[8] = 0.0018
    states[1] = 130.022096
    states[2] = 8.516766
    states[3] = 0.003289
    states[4] = 0.877202
    states[5] = 0.873881
    constants[9] = 6.75
    constants[10] = 60
    constants[11] = 0.025
    states[6] = 7.1e-5
    states[7] = 0.000014
    states[8] = 0.998597
    states[9] = 0.998586
    constants[12] = 8.25
    states[10] = 5.560224
    states[11] = 129.485991
    states[12] = 0.001089
    states[13] = 0.948597
    constants[13] = 2.25
    states[14] = 0.000367
    states[15] = 0.96729
    constants[14] = 3.1
    constants[15] = 1
    constants[16] = 0.5
    states[16] = 0.004374
    states[17] = 0.000053
    constants[17] = 0.060599
    constants[18] = 0.078681
    states[18] = 1.815768
    states[19] = 6.5e-5
    constants[19] = 1
    constants[20] = 68.55
    constants[21] = 36.4829
    constants[22] = 4
    constants[23] = 0.0002
    constants[24] = 0.0374842
    constants[25] = 0.0003
    constants[26] = 0.45
    constants[27] = 1e-24
    constants[28] = 0
    constants[29] = 0.005884
    constants[30] = 0.00011768
    constants[31] = 0.01
    states[20] = 0.026766
    states[21] = 0.012922
    states[22] = 0.190369
    states[23] = 0.714463
    states[24] = 1.38222
    constants[32] = 2.5
    constants[33] = 0.000800224
    constants[34] = 14.3
    constants[35] = 10
    constants[36] = 24.7
    constants[37] = 130
    constants[38] = 1.8
    constants[39] = 5.4
    constants[40] = 2800
    constants[41] = 0.0003
    constants[42] = 0.5
    constants[43] = 0.4
    constants[44] = 200000
    states[25] = 0.632613
    states[26] = 0.649195
    constants[45] = 0.0003969
    constants[46] = 0.0000441
    constants[47] = 0.815
    states[27] = 0.431547
    states[28] = 0.470055
    states[29] = 0.002814
    constants[48] = 0.01
    constants[49] = 0.0003
    constants[50] = 0.003
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[12] = 2000.00*constants[32]*((1.00000-states[22])-states[23])-666.000*states[23]
    rates[23] = algebraic[12]
    algebraic[18] = 0.00350000*exp(((-states[0]*states[0])/30.0000)/30.0000)+0.00150000
    algebraic[6] = 1.00000/(1.00000+exp((states[0]-1.00000)/-11.0000))
    rates[12] = (algebraic[6]-states[12])/algebraic[18]
    algebraic[8] = 1.00000/(1.00000+exp(-(states[0]+6.00000)/8.60000))
    algebraic[20] = 0.00900000/(1.00000+exp((states[0]+5.00000)/12.0000))+0.000500000
    rates[14] = (algebraic[8]-states[14])/algebraic[20]
    algebraic[9] = 1.00000/(1.00000+exp((states[0]+7.50000)/10.0000))
    algebraic[21] = 0.590000/(1.00000+exp((states[0]+60.0000)/10.0000))+3.05000
    rates[15] = (algebraic[9]-states[15])/algebraic[21]
    algebraic[14] = 1.00000/(1.00000+exp((states[0]+27.1200)/-8.21000))
    algebraic[2] = (states[0]+25.5700)/28.8000
    algebraic[26] = 4.20000e-05*exp(-algebraic[2]*algebraic[2])+2.40000e-05
    rates[3] = (algebraic[14]-states[3])/algebraic[26]
    algebraic[3] = 1.00000/(1.00000+exp((states[0]+63.6000)/5.30000))
    algebraic[15] = 1.00000/(1.00000+exp((states[0]+35.1000)/3.20000))
    algebraic[27] = 0.0300000*algebraic[15]+0.000300000
    rates[4] = (algebraic[3]-states[4])/algebraic[27]
    algebraic[28] = 0.120000*algebraic[15]+0.00300000
    rates[5] = (algebraic[3]-states[5])/algebraic[28]
    algebraic[4] = 1.00000/(1.00000+exp((states[0]+9.00000)/-5.80000))
    algebraic[16] = (states[0]+35.0000)/30.0000
    algebraic[29] = 0.00270000*exp(-algebraic[16]*algebraic[16])+0.00200000
    rates[7] = (algebraic[4]-states[7])/algebraic[29]
    algebraic[5] = 1.00000/(1.00000+exp((states[0]+27.4000)/7.10000))
    algebraic[17] = states[0]+40.0000
    algebraic[30] = 0.161000*exp(((-algebraic[17]*algebraic[17])/14.4000)/14.4000)+0.0100000
    rates[8] = (algebraic[5]-states[8])/algebraic[30]
    algebraic[31] = 1.33230*exp(((-algebraic[17]*algebraic[17])/14.2000)/14.2000)+0.0626000
    rates[9] = (algebraic[5]-states[9])/algebraic[31]
    algebraic[19] = (states[0]+52.4500)/15.8827
    algebraic[32] = 0.0256350*exp(-algebraic[19]*algebraic[19])+0.0141400
    algebraic[7] = 1.00000/(1.00000+exp((states[0]+40.5000)/11.5000))
    rates[13] = (algebraic[7]-states[13])/algebraic[32]
    algebraic[22] = (states[0]-20.0000)/20.0000
    algebraic[33] = 0.700000+0.400000*exp(-algebraic[22]*algebraic[22])
    algebraic[10] = 1.00000/(1.00000+exp((states[0]-19.9000)/-12.7000))
    rates[16] = (algebraic[10]-states[16])/algebraic[33]
    algebraic[23] = (states[0]+20.1376)/22.1996
    algebraic[34] = 0.0311800+0.217180*exp(-algebraic[23]*algebraic[23])
    algebraic[11] = 1.00000/(1.00000+exp((states[0]+15.0000)/-6.00000))
    rates[17] = (algebraic[11]-states[17])/algebraic[34]
    algebraic[13] = states[6]/(states[6]+constants[50])
    algebraic[36] = algebraic[13]*algebraic[13]*algebraic[13]*algebraic[13]
    algebraic[25] = states[19]/(states[19]+constants[49])
    algebraic[38] = algebraic[25]*algebraic[25]*algebraic[25]*algebraic[25]
    algebraic[40] = 203.800*(algebraic[38]+algebraic[36])
    rates[28] = constants[47]*((1.00000-states[28])-states[29])-algebraic[40]*states[28]
    algebraic[42] = 33.9600+339.600*algebraic[38]
    rates[29] = algebraic[40]*states[28]-algebraic[42]*states[29]
    algebraic[43] = ((constants[0]*constants[1])/constants[2])*log(states[10]/states[11])
    algebraic[44] = constants[12]*states[12]*states[13]*(states[0]-algebraic[43])
    algebraic[45] = constants[13]*states[14]*states[15]*(states[0]-algebraic[43])
    algebraic[46] = (constants[14]*(power(states[10]/1.00000, 0.445700))*(states[0]-algebraic[43]))/(1.00000+exp((1.50000*((states[0]-algebraic[43])+3.60000)*constants[2])/(constants[0]*constants[1])))
    algebraic[48] = 1.00000/(1.00000+exp((states[0]+55.0000)/24.0000))
    algebraic[49] = constants[16]*states[17]*algebraic[48]*(states[0]-algebraic[43])
    algebraic[47] = constants[15]*states[16]*(states[0]-algebraic[43])
    algebraic[53] = power(states[2], 1.50000)
    algebraic[54] = (((((constants[20]*states[10])/(states[10]+constants[19]))*algebraic[53])/(algebraic[53]+constants[21]))*(states[0]+150.000))/(states[0]+200.000)
    algebraic[1] = floor(voi/constants[5])*constants[5]
    algebraic[24] = custom_piecewise([greater_equal(voi-algebraic[1] , constants[4]) & less_equal(voi-algebraic[1] , constants[4]+constants[6]), constants[7] , True, 0.00000])
    rates[11] = -(((algebraic[44]+algebraic[45]+algebraic[46]+algebraic[47]+algebraic[49])-2.00000*algebraic[54])+algebraic[24]*constants[3])/(constants[29]*constants[2])
    rates[10] = (constants[39]-states[10])/constants[35]+((algebraic[44]+algebraic[45]+algebraic[46]+algebraic[47]+algebraic[49])-2.00000*algebraic[54])/(constants[33]*constants[2])
    algebraic[35] = ((constants[0]*constants[1])/constants[2])*log(states[1]/states[2])
    algebraic[37] = (((constants[8]*states[3]*states[3]*states[3]*(0.900000*states[4]+0.100000*states[5])*states[1]*states[0]*constants[2]*constants[2])/(constants[0]*constants[1]))*(exp(((states[0]-algebraic[35])*constants[2])/(constants[0]*constants[1]))-1.00000))/(exp((states[0]*constants[2])/(constants[0]*constants[1]))-1.00000)
    algebraic[50] = constants[17]*(states[0]-algebraic[35])
    algebraic[56] = (constants[24]*(states[2]*states[2]*states[2]*states[18]*exp((constants[2]*states[0]*constants[26])/(constants[0]*constants[1]))-states[1]*states[1]*states[1]*states[19]*exp(((constants[26]-1.00000)*states[0]*constants[2])/(constants[0]*constants[1]))))/(1.00000+constants[25]*(states[1]*states[1]*states[1]*states[19]+states[2]*states[2]*states[2]*states[18]))
    rates[2] = -(algebraic[37]+algebraic[50]+3.00000*algebraic[56]+3.00000*algebraic[54]+constants[28])/(constants[29]*constants[2])
    algebraic[39] = states[6]/(states[6]+constants[11])
    algebraic[41] = constants[9]*states[7]*(algebraic[39]*states[8]+(1.00000-algebraic[39])*states[9])*(states[0]-constants[10])
    algebraic[51] = ((constants[0]*constants[1])/(2.00000*constants[2]))*log(states[18]/states[19])
    algebraic[52] = constants[18]*(states[0]-algebraic[51])
    algebraic[55] = (constants[22]*states[19])/(states[19]+constants[23])
    rates[18] = (constants[38]-states[18])/constants[36]+((algebraic[41]+algebraic[52]+algebraic[55])-2.00000*algebraic[56])/(2.00000*constants[33]*constants[2])
    rates[1] = (constants[37]-states[1])/constants[34]+(algebraic[37]+algebraic[50]+3.00000*algebraic[56]+3.00000*algebraic[54]+constants[28])/(constants[33]*constants[2])
    algebraic[58] = ((states[6]-states[19])*2.00000*constants[30]*constants[2])/constants[31]
    rates[6] = -(algebraic[41]+algebraic[58])/(2.00000*constants[30]*constants[2])
    algebraic[57] = (10.0000/(1.00000+(9.13652*(power(1.00000, 0.477811)))/(power(constants[27], 0.477811))))*(0.0517000+0.451600/(1.00000+exp((states[0]+59.5300)/17.1800)))*(states[0]-algebraic[43])*constants[3]
    algebraic[59] = (algebraic[37]+algebraic[41]+algebraic[44]+algebraic[45]+algebraic[46]+algebraic[49]+algebraic[47]+algebraic[50]+algebraic[52]+algebraic[54]+algebraic[55]+algebraic[56]+algebraic[57])/constants[3]+algebraic[24]
    rates[0] = -algebraic[59]*1000.00
    algebraic[60] = 200000.*states[19]*(1.00000-states[20])-476.000*states[20]
    rates[20] = algebraic[60]
    algebraic[61] = 78400.0*states[19]*(1.00000-states[21])-392.000*states[21]
    rates[21] = algebraic[61]
    algebraic[62] = 200000.*states[19]*((1.00000-states[22])-states[23])-6.60000*states[22]
    rates[22] = algebraic[62]
    algebraic[63] = 0.0800000*algebraic[61]+0.160000*algebraic[62]+0.0450000*algebraic[60]
    rates[24] = algebraic[63]
    algebraic[67] = (constants[40]*(states[19]/constants[41]-(constants[43]*constants[43]*states[26])/constants[42]))/((states[19]+constants[41])/constants[41]+(constants[43]*(states[26]+constants[42]))/constants[42])
    algebraic[64] = states[29]/(states[29]+0.250000)
    algebraic[65] = algebraic[64]*algebraic[64]
    algebraic[66] = constants[44]*algebraic[65]*(states[25]-states[19])
    rates[19] = -((algebraic[52]+algebraic[55]+algebraic[67])-(algebraic[58]+algebraic[66]+2.00000*algebraic[56]))/(2.00000*constants[29]*constants[2])-1.00000*algebraic[63]
    algebraic[68] = ((states[26]-states[25])*2.00000*constants[46]*constants[2])/constants[48]
    rates[26] = (algebraic[67]-algebraic[68])/(2.00000*constants[45]*constants[2])
    algebraic[69] = 480.000*states[25]*(1.00000-states[27])-400.000*states[27]
    rates[27] = algebraic[69]
    rates[25] = (algebraic[68]-algebraic[66])/(2.00000*constants[46]*constants[2])-31.0000*algebraic[69]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[12] = 2000.00*constants[32]*((1.00000-states[22])-states[23])-666.000*states[23]
    algebraic[18] = 0.00350000*exp(((-states[0]*states[0])/30.0000)/30.0000)+0.00150000
    algebraic[6] = 1.00000/(1.00000+exp((states[0]-1.00000)/-11.0000))
    algebraic[8] = 1.00000/(1.00000+exp(-(states[0]+6.00000)/8.60000))
    algebraic[20] = 0.00900000/(1.00000+exp((states[0]+5.00000)/12.0000))+0.000500000
    algebraic[9] = 1.00000/(1.00000+exp((states[0]+7.50000)/10.0000))
    algebraic[21] = 0.590000/(1.00000+exp((states[0]+60.0000)/10.0000))+3.05000
    algebraic[14] = 1.00000/(1.00000+exp((states[0]+27.1200)/-8.21000))
    algebraic[2] = (states[0]+25.5700)/28.8000
    algebraic[26] = 4.20000e-05*exp(-algebraic[2]*algebraic[2])+2.40000e-05
    algebraic[3] = 1.00000/(1.00000+exp((states[0]+63.6000)/5.30000))
    algebraic[15] = 1.00000/(1.00000+exp((states[0]+35.1000)/3.20000))
    algebraic[27] = 0.0300000*algebraic[15]+0.000300000
    algebraic[28] = 0.120000*algebraic[15]+0.00300000
    algebraic[4] = 1.00000/(1.00000+exp((states[0]+9.00000)/-5.80000))
    algebraic[16] = (states[0]+35.0000)/30.0000
    algebraic[29] = 0.00270000*exp(-algebraic[16]*algebraic[16])+0.00200000
    algebraic[5] = 1.00000/(1.00000+exp((states[0]+27.4000)/7.10000))
    algebraic[17] = states[0]+40.0000
    algebraic[30] = 0.161000*exp(((-algebraic[17]*algebraic[17])/14.4000)/14.4000)+0.0100000
    algebraic[31] = 1.33230*exp(((-algebraic[17]*algebraic[17])/14.2000)/14.2000)+0.0626000
    algebraic[19] = (states[0]+52.4500)/15.8827
    algebraic[32] = 0.0256350*exp(-algebraic[19]*algebraic[19])+0.0141400
    algebraic[7] = 1.00000/(1.00000+exp((states[0]+40.5000)/11.5000))
    algebraic[22] = (states[0]-20.0000)/20.0000
    algebraic[33] = 0.700000+0.400000*exp(-algebraic[22]*algebraic[22])
    algebraic[10] = 1.00000/(1.00000+exp((states[0]-19.9000)/-12.7000))
    algebraic[23] = (states[0]+20.1376)/22.1996
    algebraic[34] = 0.0311800+0.217180*exp(-algebraic[23]*algebraic[23])
    algebraic[11] = 1.00000/(1.00000+exp((states[0]+15.0000)/-6.00000))
    algebraic[13] = states[6]/(states[6]+constants[50])
    algebraic[36] = algebraic[13]*algebraic[13]*algebraic[13]*algebraic[13]
    algebraic[25] = states[19]/(states[19]+constants[49])
    algebraic[38] = algebraic[25]*algebraic[25]*algebraic[25]*algebraic[25]
    algebraic[40] = 203.800*(algebraic[38]+algebraic[36])
    algebraic[42] = 33.9600+339.600*algebraic[38]
    algebraic[43] = ((constants[0]*constants[1])/constants[2])*log(states[10]/states[11])
    algebraic[44] = constants[12]*states[12]*states[13]*(states[0]-algebraic[43])
    algebraic[45] = constants[13]*states[14]*states[15]*(states[0]-algebraic[43])
    algebraic[46] = (constants[14]*(power(states[10]/1.00000, 0.445700))*(states[0]-algebraic[43]))/(1.00000+exp((1.50000*((states[0]-algebraic[43])+3.60000)*constants[2])/(constants[0]*constants[1])))
    algebraic[48] = 1.00000/(1.00000+exp((states[0]+55.0000)/24.0000))
    algebraic[49] = constants[16]*states[17]*algebraic[48]*(states[0]-algebraic[43])
    algebraic[47] = constants[15]*states[16]*(states[0]-algebraic[43])
    algebraic[53] = power(states[2], 1.50000)
    algebraic[54] = (((((constants[20]*states[10])/(states[10]+constants[19]))*algebraic[53])/(algebraic[53]+constants[21]))*(states[0]+150.000))/(states[0]+200.000)
    algebraic[1] = floor(voi/constants[5])*constants[5]
    algebraic[24] = custom_piecewise([greater_equal(voi-algebraic[1] , constants[4]) & less_equal(voi-algebraic[1] , constants[4]+constants[6]), constants[7] , True, 0.00000])
    algebraic[35] = ((constants[0]*constants[1])/constants[2])*log(states[1]/states[2])
    algebraic[37] = (((constants[8]*states[3]*states[3]*states[3]*(0.900000*states[4]+0.100000*states[5])*states[1]*states[0]*constants[2]*constants[2])/(constants[0]*constants[1]))*(exp(((states[0]-algebraic[35])*constants[2])/(constants[0]*constants[1]))-1.00000))/(exp((states[0]*constants[2])/(constants[0]*constants[1]))-1.00000)
    algebraic[50] = constants[17]*(states[0]-algebraic[35])
    algebraic[56] = (constants[24]*(states[2]*states[2]*states[2]*states[18]*exp((constants[2]*states[0]*constants[26])/(constants[0]*constants[1]))-states[1]*states[1]*states[1]*states[19]*exp(((constants[26]-1.00000)*states[0]*constants[2])/(constants[0]*constants[1]))))/(1.00000+constants[25]*(states[1]*states[1]*states[1]*states[19]+states[2]*states[2]*states[2]*states[18]))
    algebraic[39] = states[6]/(states[6]+constants[11])
    algebraic[41] = constants[9]*states[7]*(algebraic[39]*states[8]+(1.00000-algebraic[39])*states[9])*(states[0]-constants[10])
    algebraic[51] = ((constants[0]*constants[1])/(2.00000*constants[2]))*log(states[18]/states[19])
    algebraic[52] = constants[18]*(states[0]-algebraic[51])
    algebraic[55] = (constants[22]*states[19])/(states[19]+constants[23])
    algebraic[58] = ((states[6]-states[19])*2.00000*constants[30]*constants[2])/constants[31]
    algebraic[57] = (10.0000/(1.00000+(9.13652*(power(1.00000, 0.477811)))/(power(constants[27], 0.477811))))*(0.0517000+0.451600/(1.00000+exp((states[0]+59.5300)/17.1800)))*(states[0]-algebraic[43])*constants[3]
    algebraic[59] = (algebraic[37]+algebraic[41]+algebraic[44]+algebraic[45]+algebraic[46]+algebraic[49]+algebraic[47]+algebraic[50]+algebraic[52]+algebraic[54]+algebraic[55]+algebraic[56]+algebraic[57])/constants[3]+algebraic[24]
    algebraic[60] = 200000.*states[19]*(1.00000-states[20])-476.000*states[20]
    algebraic[61] = 78400.0*states[19]*(1.00000-states[21])-392.000*states[21]
    algebraic[62] = 200000.*states[19]*((1.00000-states[22])-states[23])-6.60000*states[22]
    algebraic[63] = 0.0800000*algebraic[61]+0.160000*algebraic[62]+0.0450000*algebraic[60]
    algebraic[67] = (constants[40]*(states[19]/constants[41]-(constants[43]*constants[43]*states[26])/constants[42]))/((states[19]+constants[41])/constants[41]+(constants[43]*(states[26]+constants[42]))/constants[42])
    algebraic[64] = states[29]/(states[29]+0.250000)
    algebraic[65] = algebraic[64]*algebraic[64]
    algebraic[66] = constants[44]*algebraic[65]*(states[25]-states[19])
    algebraic[68] = ((states[26]-states[25])*2.00000*constants[46]*constants[2])/constants[48]
    algebraic[69] = 480.000*states[25]*(1.00000-states[27])-400.000*states[27]
    algebraic[0] = 0.0500000*states[0]
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
        self.R = 8314
        self.T = 306.15
        self.F = 96487
        self.Cm = 50
        self.stim_offset = 0
        self.stim_period = 1
        self.stim_duration = 0.006
        self.stim_amplitude = -15
        self.P_Na = 0.0018
        self.g_Ca_L = 6.75
        self.E_Ca_app = 60
        self.k_Ca = 0.025
        self.g_t = 8.25
        self.g_kur = 2.25
        self.g_K1 = 3.1
        self.g_Ks = 1
        self.g_Kr = 0.5
        self.g_B_Na = 0.060599
        self.g_B_Ca = 0.078681
        self.K_NaK_K = 1
        self.i_NaK_max = 68.55
        self.pow_K_NaK_Na_15 = 36.4829
        self.i_CaP_max = 4
        self.k_CaP = 0.0002
        self.K_NaCa = 0.0374842
        self.d_NaCa = 0.0003
        self.gamma_Na = 0.45
        self.ACh = 1e-24
        self.phi_Na_en = 0
        self.Vol_i = 0.005884
        self.Vol_d = 0.00011768
        self.tau_di = 0.01
        self.Mg_i = 2.5
        self.Vol_c = 0.000800224
        self.tau_Na = 14.3
        self.tau_K = 10
        self.tau_Ca = 24.7
        self.Na_b = 130
        self.Ca_b = 1.8
        self.K_b = 5.4
        self.I_up_max = 2800
        self.k_cyca = 0.0003
        self.k_srca = 0.5
        self.k_xcs = 0.4
        self.alpha_rel = 200000
        self.Vol_up = 0.0003969
        self.Vol_rel = 0.0000441
        self.r_recov = 0.815
        self.tau_tr = 0.01
        self.k_rel_i = 0.0003
        self.k_rel_d = 0.003

    def to_dict(self):
        return {
            "R": self.R,
            "T": self.T,
            "F": self.F,
            "Cm": self.Cm,
            "stim_offset": self.stim_offset,
            "stim_period": self.stim_period,
            "stim_duration": self.stim_duration,
            "stim_amplitude": self.stim_amplitude,
            "P_Na": self.P_Na,
            "g_Ca_L": self.g_Ca_L,
            "E_Ca_app": self.E_Ca_app,
            "k_Ca": self.k_Ca,
            "g_t": self.g_t,
            "g_kur": self.g_kur,
            "g_K1": self.g_K1,
            "g_Ks": self.g_Ks,
            "g_Kr": self.g_Kr,
            "g_B_Na": self.g_B_Na,
            "g_B_Ca": self.g_B_Ca,
            "K_NaK_K": self.K_NaK_K,
            "i_NaK_max": self.i_NaK_max,
            "pow_K_NaK_Na_15": self.pow_K_NaK_Na_15,
            "i_CaP_max": self.i_CaP_max,
            "k_CaP": self.k_CaP,
            "K_NaCa": self.K_NaCa,
            "d_NaCa": self.d_NaCa,
            "gamma_Na": self.gamma_Na,
            "ACh": self.ACh,
            "phi_Na_en": self.phi_Na_en,
            "Vol_i": self.Vol_i,
            "Vol_d": self.Vol_d,
            "tau_di": self.tau_di,
            "Mg_i": self.Mg_i,
            "Vol_c": self.Vol_c,
            "tau_Na": self.tau_Na,
            "tau_K": self.tau_K,
            "tau_Ca": self.tau_Ca,
            "Na_b": self.Na_b,
            "Ca_b": self.Ca_b,
            "K_b": self.K_b,
            "I_up_max": self.I_up_max,
            "k_cyca": self.k_cyca,
            "k_srca": self.k_srca,
            "k_xcs": self.k_xcs,
            "alpha_rel": self.alpha_rel,
            "Vol_up": self.Vol_up,
            "Vol_rel": self.Vol_rel,
            "r_recov": self.r_recov,
            "tau_tr": self.tau_tr,
            "k_rel_i": self.k_rel_i,
            "k_rel_d": self.k_rel_d,
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
        y0=[-74.031982, 130.022096, 8.516766, 0.003289, 0.877202, 0.873881, 7.1e-5, 0.000014, 0.998597, 0.998586, 5.560224, 129.485991, 0.001089, 0.948597, 0.000367, 0.96729, 0.004374, 0.000053, 1.815768, 6.5e-5, 0.026766, 0.012922, 0.190369, 0.714463, 1.38222, 0.632613, 0.649195, 0.431547, 0.470055, 0.002814],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "maleckar_greenstein_trayanova_giles_2009"
        self.curve_names = [
            "V",
            "Na_c",
            "Na_i",
            "m",
            "h1",
            "h2",
            "Ca_d",
            "d_L",
            "f_L1",
            "f_L2",
            "K_c",
            "K_i",
            "r",
            "s",
            "a_ur",
            "i_ur",
            "n",
            "pa",
            "Ca_c",
            "Ca_i",
            "O_C",
            "O_TC",
            "O_TMgC",
            "O_TMgMg",
            "O",
            "Ca_rel",
            "Ca_up",
            "O_Calse",
            "F1",
            "F2",
        ]
        self.state_names = ['V', 'Na_c', 'Na_i', 'm', 'h1', 'h2', 'Ca_d', 'd_L', 'f_L1', 'f_L2', 'K_c', 'K_i', 'r', 's', 'a_ur', 'i_ur', 'n', 'pa', 'Ca_c', 'Ca_i', 'O_C', 'O_TC', 'O_TMgC', 'O_TMgMg', 'O', 'Ca_rel', 'Ca_up', 'O_Calse', 'F1', 'F2']
        self.algebraic_names = ['Q_tot', 'past', 'm_factor', 'h_infinity', 'd_L_infinity', 'f_L_infinity', 'r_infinity', 's_infinity', 'a_ur_infinity', 'i_ur_infinity', 'n_infinity', 'p_a_infinity', 'J_O_TMgMg', 'r_Ca_d_term', 'm_infinity', 'h_factor', 'd_L_factor', 'f_L_factor', 'tau_r', 's_factor', 'tau_a_ur', 'tau_i_ur', 'n_factor', 'pa_factor', 'i_Stim', 'r_Ca_i_term', 'tau_m', 'tau_h1', 'tau_h2', 'tau_d_L', 'tau_f_L1', 'tau_f_L2', 'tau_s', 'tau_n', 'tau_pa', 'E_Na', 'r_Ca_d_factor', 'i_Na', 'r_Ca_i_factor', 'f_Ca', 'r_act', 'i_Ca_L', 'r_inact', 'E_K', 'i_t', 'i_Kur', 'i_K1', 'i_Ks', 'pip', 'i_Kr', 'i_B_Na', 'E_Ca', 'i_B_Ca', 'pow_Na_i_15', 'i_NaK', 'i_CaP', 'i_NaCa', 'i_KACh', 'i_di', 'I', 'J_O_C', 'J_O_TC', 'J_O_TMgC', 'J_O', 'i_rel_f2', 'i_rel_factor', 'i_rel', 'i_up', 'i_tr', 'J_O_Calse']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 51
        p = self.params

        # direct mapping
        c[0] = p.R
        c[1] = p.T
        c[2] = p.F
        c[3] = p.Cm
        c[4] = p.stim_offset
        c[5] = p.stim_period
        c[6] = p.stim_duration
        c[7] = p.stim_amplitude
        c[8] = p.P_Na
        c[9] = p.g_Ca_L
        c[10] = p.E_Ca_app
        c[11] = p.k_Ca
        c[12] = p.g_t
        c[13] = p.g_kur
        c[14] = p.g_K1
        c[15] = p.g_Ks
        c[16] = p.g_Kr
        c[17] = p.g_B_Na
        c[18] = p.g_B_Ca
        c[19] = p.K_NaK_K
        c[20] = p.i_NaK_max
        c[21] = p.pow_K_NaK_Na_15
        c[22] = p.i_CaP_max
        c[23] = p.k_CaP
        c[24] = p.K_NaCa
        c[25] = p.d_NaCa
        c[26] = p.gamma_Na
        c[27] = p.ACh
        c[28] = p.phi_Na_en
        c[29] = p.Vol_i
        c[30] = p.Vol_d
        c[31] = p.tau_di
        c[32] = p.Mg_i
        c[33] = p.Vol_c
        c[34] = p.tau_Na
        c[35] = p.tau_K
        c[36] = p.tau_Ca
        c[37] = p.Na_b
        c[38] = p.Ca_b
        c[39] = p.K_b
        c[40] = p.I_up_max
        c[41] = p.k_cyca
        c[42] = p.k_srca
        c[43] = p.k_xcs
        c[44] = p.alpha_rel
        c[45] = p.Vol_up
        c[46] = p.Vol_rel
        c[47] = p.r_recov
        c[48] = p.tau_tr
        c[49] = p.k_rel_i
        c[50] = p.k_rel_d

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
