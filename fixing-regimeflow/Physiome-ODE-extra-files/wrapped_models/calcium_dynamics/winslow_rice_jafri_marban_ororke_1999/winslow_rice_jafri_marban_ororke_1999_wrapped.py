# Size of variable arrays:
sizeAlgebraic = 60
sizeStates = 33
sizeConstants = 79
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
    legend_constants[0] = "R in component membrane (joule_per_mole_kelvin)"
    legend_constants[1] = "T in component membrane (kelvin)"
    legend_constants[2] = "F in component membrane (coulomb_per_millimole)"
    legend_constants[3] = "C_sc in component membrane (microF_per_cm2)"
    legend_algebraic[23] = "i_Na in component fast_sodium_current (microA_per_microF)"
    legend_algebraic[45] = "i_Ca in component L_type_Ca_current (microA_per_microF)"
    legend_algebraic[48] = "i_Ca_K in component L_type_Ca_current (microA_per_microF)"
    legend_algebraic[29] = "i_Kr in component rapid_activating_delayed_rectifiyer_K_current (microA_per_microF)"
    legend_algebraic[31] = "i_Ks in component slow_activating_delayed_rectifiyer_K_current (microA_per_microF)"
    legend_algebraic[32] = "i_to1 in component transient_outward_potassium_current (microA_per_microF)"
    legend_algebraic[34] = "i_K1 in component time_independent_potassium_current (microA_per_microF)"
    legend_algebraic[36] = "i_Kp in component plateau_potassium_current (microA_per_microF)"
    legend_algebraic[37] = "i_NaCa in component Na_Ca_exchanger (microA_per_microF)"
    legend_algebraic[39] = "i_NaK in component sodium_potassium_pump (microA_per_microF)"
    legend_algebraic[40] = "i_p_Ca in component sarcolemmal_calcium_pump (microA_per_microF)"
    legend_algebraic[42] = "i_Ca_b in component calcium_background_current (microA_per_microF)"
    legend_algebraic[43] = "i_Na_b in component sodium_background_current (microA_per_microF)"
    legend_algebraic[9] = "i_Stim in component membrane (microA_per_microF)"
    legend_constants[4] = "stim_start in component membrane (second)"
    legend_constants[5] = "stim_end in component membrane (second)"
    legend_constants[6] = "stim_period in component membrane (second)"
    legend_constants[7] = "stim_duration in component membrane (second)"
    legend_constants[8] = "stim_amplitude in component membrane (microA_per_microF)"
    legend_algebraic[19] = "E_Na in component fast_sodium_current (millivolt)"
    legend_constants[9] = "g_Na in component fast_sodium_current (milliS_per_microF)"
    legend_constants[10] = "Nao in component standard_ionic_concentrations (millimolar)"
    legend_states[1] = "Nai in component intracellular_ion_concentrations (millimolar)"
    legend_states[2] = "m in component fast_sodium_current_m_gate (dimensionless)"
    legend_states[3] = "h in component fast_sodium_current_h_gate (dimensionless)"
    legend_states[4] = "j in component fast_sodium_current_j_gate (dimensionless)"
    legend_algebraic[10] = "alpha_m in component fast_sodium_current_m_gate (per_second)"
    legend_algebraic[20] = "beta_m in component fast_sodium_current_m_gate (per_second)"
    legend_algebraic[0] = "E0_m in component fast_sodium_current_m_gate (millivolt)"
    legend_algebraic[1] = "alpha_h in component fast_sodium_current_h_gate (per_second)"
    legend_algebraic[11] = "beta_h in component fast_sodium_current_h_gate (per_second)"
    legend_algebraic[2] = "alpha_j in component fast_sodium_current_j_gate (per_second)"
    legend_algebraic[12] = "beta_j in component fast_sodium_current_j_gate (per_second)"
    legend_algebraic[26] = "E_K in component rapid_activating_delayed_rectifiyer_K_current (millivolt)"
    legend_constants[11] = "g_Kr in component rapid_activating_delayed_rectifiyer_K_current (milliS_per_microF)"
    legend_constants[77] = "f_Ko in component rapid_activating_delayed_rectifiyer_K_current (dimensionless)"
    legend_algebraic[28] = "R_V in component rapid_activating_delayed_rectifiyer_K_current (dimensionless)"
    legend_constants[12] = "Ko in component standard_ionic_concentrations (millimolar)"
    legend_states[5] = "Ki in component intracellular_ion_concentrations (millimolar)"
    legend_states[6] = "X_kr in component rapid_activating_delayed_rectifiyer_K_current_X_kr_gate (dimensionless)"
    legend_algebraic[3] = "K12 in component rapid_activating_delayed_rectifiyer_K_current_X_kr_gate (dimensionless)"
    legend_algebraic[13] = "K21 in component rapid_activating_delayed_rectifiyer_K_current_X_kr_gate (dimensionless)"
    legend_algebraic[21] = "X_kr_inf in component rapid_activating_delayed_rectifiyer_K_current_X_kr_gate (dimensionless)"
    legend_algebraic[24] = "tau_X_kr in component rapid_activating_delayed_rectifiyer_K_current_X_kr_gate (second)"
    legend_constants[13] = "tau_factor in component rapid_activating_delayed_rectifiyer_K_current_X_kr_gate (dimensionless)"
    legend_constants[14] = "g_Ks in component slow_activating_delayed_rectifiyer_K_current (milliS_per_microF)"
    legend_algebraic[30] = "E_Ks in component slow_activating_delayed_rectifiyer_K_current (millivolt)"
    legend_states[7] = "X_ks in component slow_activating_delayed_rectifiyer_K_current_X_ks_gate (dimensionless)"
    legend_algebraic[14] = "tau_X_ks in component slow_activating_delayed_rectifiyer_K_current_X_ks_gate (second)"
    legend_algebraic[4] = "X_ks_infinity in component slow_activating_delayed_rectifiyer_K_current_X_ks_gate (dimensionless)"
    legend_constants[15] = "g_to1 in component transient_outward_potassium_current (milliS_per_microF)"
    legend_states[8] = "X_to1 in component transient_outward_potassium_current_X_to1_gate (dimensionless)"
    legend_states[9] = "Y_to1 in component transient_outward_potassium_current_Y_to1_gate (dimensionless)"
    legend_algebraic[5] = "alpha_X_to1 in component transient_outward_potassium_current_X_to1_gate (per_second)"
    legend_algebraic[15] = "beta_X_to1 in component transient_outward_potassium_current_X_to1_gate (per_second)"
    legend_algebraic[6] = "alpha_Y_to1 in component transient_outward_potassium_current_Y_to1_gate (per_second)"
    legend_algebraic[16] = "beta_Y_to1 in component transient_outward_potassium_current_Y_to1_gate (per_second)"
    legend_constants[16] = "g_K1 in component time_independent_potassium_current (milliS_per_microF)"
    legend_constants[17] = "K_mK1 in component time_independent_potassium_current (millimolar)"
    legend_algebraic[33] = "K1_infinity_V in component time_independent_potassium_current_K1_gate (dimensionless)"
    legend_constants[18] = "g_Kp in component plateau_potassium_current (milliS_per_microF)"
    legend_algebraic[35] = "Kp_V in component plateau_potassium_current_Kp_gate (dimensionless)"
    legend_constants[19] = "K_mCa in component Na_Ca_exchanger (millimolar)"
    legend_constants[20] = "K_mNa in component Na_Ca_exchanger (millimolar)"
    legend_constants[21] = "K_NaCa in component Na_Ca_exchanger (microA_per_microF)"
    legend_constants[22] = "K_sat in component Na_Ca_exchanger (dimensionless)"
    legend_constants[23] = "eta in component Na_Ca_exchanger (dimensionless)"
    legend_states[10] = "Cai in component intracellular_ion_concentrations (millimolar)"
    legend_constants[24] = "Cao in component standard_ionic_concentrations (millimolar)"
    legend_constants[25] = "I_NaK in component sodium_potassium_pump (microA_per_microF)"
    legend_algebraic[38] = "f_NaK in component sodium_potassium_pump (dimensionless)"
    legend_constants[26] = "K_mNai in component sodium_potassium_pump (millimolar)"
    legend_constants[27] = "K_mKo in component sodium_potassium_pump (millimolar)"
    legend_constants[78] = "sigma in component sodium_potassium_pump (dimensionless)"
    legend_constants[28] = "K_mpCa in component sarcolemmal_calcium_pump (millimolar)"
    legend_constants[29] = "I_pCa in component sarcolemmal_calcium_pump (microA_per_microF)"
    legend_constants[30] = "g_Cab in component calcium_background_current (milliS_per_microF)"
    legend_algebraic[41] = "E_Ca in component calcium_background_current (millivolt)"
    legend_constants[31] = "g_Nab in component sodium_background_current (milliS_per_microF)"
    legend_constants[32] = "P_Ca in component L_type_Ca_current (cm_per_second)"
    legend_constants[33] = "P_K in component L_type_Ca_current (cm_per_second)"
    legend_algebraic[46] = "p_prime_k in component L_type_Ca_current (cm_per_second)"
    legend_constants[34] = "i_Ca_half in component L_type_Ca_current (microA_per_microF)"
    legend_algebraic[44] = "i_Ca_max in component L_type_Ca_current (microA_per_microF)"
    legend_states[11] = "O in component L_type_Ca_current (dimensionless)"
    legend_states[12] = "O_Ca in component L_type_Ca_current (dimensionless)"
    legend_algebraic[7] = "alpha in component L_type_Ca_current (per_second)"
    legend_algebraic[17] = "beta in component L_type_Ca_current (per_second)"
    legend_algebraic[27] = "gamma in component L_type_Ca_current (per_second)"
    legend_algebraic[22] = "alpha_a in component L_type_Ca_current (per_second)"
    legend_algebraic[25] = "beta_b in component L_type_Ca_current (per_second)"
    legend_constants[35] = "a in component L_type_Ca_current (dimensionless)"
    legend_constants[36] = "b in component L_type_Ca_current (dimensionless)"
    legend_constants[37] = "g in component L_type_Ca_current (per_second)"
    legend_constants[38] = "f in component L_type_Ca_current (per_second)"
    legend_constants[39] = "gprime in component L_type_Ca_current (per_second)"
    legend_constants[40] = "fprime in component L_type_Ca_current (per_second)"
    legend_constants[41] = "omega in component L_type_Ca_current (per_second)"
    legend_states[13] = "C0 in component L_type_Ca_current (dimensionless)"
    legend_states[14] = "C1 in component L_type_Ca_current (dimensionless)"
    legend_states[15] = "C2 in component L_type_Ca_current (dimensionless)"
    legend_states[16] = "C3 in component L_type_Ca_current (dimensionless)"
    legend_states[17] = "C4 in component L_type_Ca_current (dimensionless)"
    legend_states[18] = "C_Ca0 in component L_type_Ca_current (dimensionless)"
    legend_states[19] = "C_Ca1 in component L_type_Ca_current (dimensionless)"
    legend_states[20] = "C_Ca2 in component L_type_Ca_current (dimensionless)"
    legend_states[21] = "C_Ca3 in component L_type_Ca_current (dimensionless)"
    legend_states[22] = "C_Ca4 in component L_type_Ca_current (dimensionless)"
    legend_states[23] = "Ca_ss in component intracellular_ion_concentrations (millimolar)"
    legend_states[24] = "y in component L_type_Ca_current_y_gate (dimensionless)"
    legend_algebraic[8] = "y_infinity in component L_type_Ca_current_y_gate (dimensionless)"
    legend_algebraic[18] = "tau_y in component L_type_Ca_current_y_gate (second)"
    legend_algebraic[47] = "J_rel in component RyR_channel (millimolar_per_second)"
    legend_constants[42] = "v1 in component RyR_channel (per_second)"
    legend_constants[43] = "k_a_plus in component RyR_channel (millimolar4_per_second)"
    legend_constants[44] = "k_a_minus in component RyR_channel (per_second)"
    legend_constants[45] = "k_b_plus in component RyR_channel (millimolar3_per_second)"
    legend_constants[46] = "k_b_minus in component RyR_channel (per_second)"
    legend_constants[47] = "k_c_plus in component RyR_channel (per_second)"
    legend_constants[48] = "k_c_minus in component RyR_channel (per_second)"
    legend_states[25] = "P_O1 in component RyR_channel (dimensionless)"
    legend_states[26] = "P_O2 in component RyR_channel (dimensionless)"
    legend_states[27] = "P_C1 in component RyR_channel (dimensionless)"
    legend_states[28] = "P_C2 in component RyR_channel (dimensionless)"
    legend_constants[49] = "n in component RyR_channel (dimensionless)"
    legend_constants[50] = "m in component RyR_channel (dimensionless)"
    legend_states[29] = "Ca_JSR in component intracellular_ion_concentrations (millimolar)"
    legend_algebraic[51] = "J_up in component SERCA2a_pump (millimolar_per_second)"
    legend_constants[51] = "K_fb in component SERCA2a_pump (millimolar)"
    legend_constants[52] = "K_rb in component SERCA2a_pump (millimolar)"
    legend_algebraic[49] = "fb in component SERCA2a_pump (dimensionless)"
    legend_algebraic[50] = "rb in component SERCA2a_pump (dimensionless)"
    legend_constants[53] = "Vmaxf in component SERCA2a_pump (millimolar_per_second)"
    legend_constants[54] = "Vmaxr in component SERCA2a_pump (millimolar_per_second)"
    legend_constants[55] = "K_SR in component SERCA2a_pump (dimensionless)"
    legend_constants[56] = "N_fb in component SERCA2a_pump (dimensionless)"
    legend_constants[57] = "N_rb in component SERCA2a_pump (dimensionless)"
    legend_states[30] = "Ca_NSR in component intracellular_ion_concentrations (millimolar)"
    legend_algebraic[53] = "J_tr in component intracellular_Ca_fluxes (millimolar_per_second)"
    legend_algebraic[52] = "J_xfer in component intracellular_Ca_fluxes (millimolar_per_second)"
    legend_algebraic[58] = "J_trpn in component intracellular_Ca_fluxes (millimolar_per_second)"
    legend_constants[58] = "tau_tr in component intracellular_Ca_fluxes (second)"
    legend_constants[59] = "tau_xfer in component intracellular_Ca_fluxes (second)"
    legend_states[31] = "HTRPNCa in component intracellular_Ca_fluxes (millimolar)"
    legend_states[32] = "LTRPNCa in component intracellular_Ca_fluxes (millimolar)"
    legend_algebraic[56] = "J_HTRPNCa in component intracellular_Ca_fluxes (millimolar_per_second)"
    legend_algebraic[57] = "J_LTRPNCa in component intracellular_Ca_fluxes (millimolar_per_second)"
    legend_constants[60] = "HTRPN_tot in component intracellular_Ca_fluxes (dimensionless)"
    legend_constants[61] = "LTRPN_tot in component intracellular_Ca_fluxes (dimensionless)"
    legend_constants[62] = "k_htrpn_plus in component intracellular_Ca_fluxes (per_millimolar_second)"
    legend_constants[63] = "k_htrpn_minus in component intracellular_Ca_fluxes (per_second)"
    legend_constants[64] = "k_ltrpn_plus in component intracellular_Ca_fluxes (per_millimolar_second)"
    legend_constants[65] = "k_ltrpn_minus in component intracellular_Ca_fluxes (per_second)"
    legend_constants[66] = "A_cap in component intracellular_ion_concentrations (cm2)"
    legend_constants[67] = "V_myo in component intracellular_ion_concentrations (micro_litre)"
    legend_constants[68] = "V_JSR in component intracellular_ion_concentrations (micro_litre)"
    legend_constants[69] = "V_NSR in component intracellular_ion_concentrations (micro_litre)"
    legend_constants[70] = "V_SS in component intracellular_ion_concentrations (micro_litre)"
    legend_constants[71] = "K_mCMDN in component intracellular_ion_concentrations (millimolar)"
    legend_constants[72] = "K_mEGTA in component intracellular_ion_concentrations (millimolar)"
    legend_constants[73] = "K_mCSQN in component intracellular_ion_concentrations (millimolar)"
    legend_constants[74] = "CMDN_tot in component intracellular_ion_concentrations (millimolar)"
    legend_constants[75] = "EGTA_tot in component intracellular_ion_concentrations (millimolar)"
    legend_constants[76] = "CSQN_tot in component intracellular_ion_concentrations (millimolar)"
    legend_algebraic[59] = "beta_i in component intracellular_ion_concentrations (dimensionless)"
    legend_algebraic[54] = "beta_SS in component intracellular_ion_concentrations (dimensionless)"
    legend_algebraic[55] = "beta_JSR in component intracellular_ion_concentrations (dimensionless)"
    legend_rates[0] = "d/dt V in component membrane (millivolt)"
    legend_rates[2] = "d/dt m in component fast_sodium_current_m_gate (dimensionless)"
    legend_rates[3] = "d/dt h in component fast_sodium_current_h_gate (dimensionless)"
    legend_rates[4] = "d/dt j in component fast_sodium_current_j_gate (dimensionless)"
    legend_rates[6] = "d/dt X_kr in component rapid_activating_delayed_rectifiyer_K_current_X_kr_gate (dimensionless)"
    legend_rates[7] = "d/dt X_ks in component slow_activating_delayed_rectifiyer_K_current_X_ks_gate (dimensionless)"
    legend_rates[8] = "d/dt X_to1 in component transient_outward_potassium_current_X_to1_gate (dimensionless)"
    legend_rates[9] = "d/dt Y_to1 in component transient_outward_potassium_current_Y_to1_gate (dimensionless)"
    legend_rates[13] = "d/dt C0 in component L_type_Ca_current (dimensionless)"
    legend_rates[14] = "d/dt C1 in component L_type_Ca_current (dimensionless)"
    legend_rates[15] = "d/dt C2 in component L_type_Ca_current (dimensionless)"
    legend_rates[16] = "d/dt C3 in component L_type_Ca_current (dimensionless)"
    legend_rates[17] = "d/dt C4 in component L_type_Ca_current (dimensionless)"
    legend_rates[11] = "d/dt O in component L_type_Ca_current (dimensionless)"
    legend_rates[18] = "d/dt C_Ca0 in component L_type_Ca_current (dimensionless)"
    legend_rates[19] = "d/dt C_Ca1 in component L_type_Ca_current (dimensionless)"
    legend_rates[20] = "d/dt C_Ca2 in component L_type_Ca_current (dimensionless)"
    legend_rates[21] = "d/dt C_Ca3 in component L_type_Ca_current (dimensionless)"
    legend_rates[22] = "d/dt C_Ca4 in component L_type_Ca_current (dimensionless)"
    legend_rates[12] = "d/dt O_Ca in component L_type_Ca_current (dimensionless)"
    legend_rates[24] = "d/dt y in component L_type_Ca_current_y_gate (dimensionless)"
    legend_rates[27] = "d/dt P_C1 in component RyR_channel (dimensionless)"
    legend_rates[25] = "d/dt P_O1 in component RyR_channel (dimensionless)"
    legend_rates[26] = "d/dt P_O2 in component RyR_channel (dimensionless)"
    legend_rates[28] = "d/dt P_C2 in component RyR_channel (dimensionless)"
    legend_rates[31] = "d/dt HTRPNCa in component intracellular_Ca_fluxes (millimolar)"
    legend_rates[32] = "d/dt LTRPNCa in component intracellular_Ca_fluxes (millimolar)"
    legend_rates[10] = "d/dt Cai in component intracellular_ion_concentrations (millimolar)"
    legend_rates[1] = "d/dt Nai in component intracellular_ion_concentrations (millimolar)"
    legend_rates[5] = "d/dt Ki in component intracellular_ion_concentrations (millimolar)"
    legend_rates[23] = "d/dt Ca_ss in component intracellular_ion_concentrations (millimolar)"
    legend_rates[29] = "d/dt Ca_JSR in component intracellular_ion_concentrations (millimolar)"
    legend_rates[30] = "d/dt Ca_NSR in component intracellular_ion_concentrations (millimolar)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = -96.1638
    constants[0] = 8.314472
    constants[1] = 310
    constants[2] = 96.4853415
    constants[3] = 0.001
    constants[4] = 0.1
    constants[5] = 100000000
    constants[6] = 1
    constants[7] = 0.002
    constants[8] = -21.1268
    constants[9] = 12.8
    constants[10] = 138
    states[1] = 10
    states[2] = 0.0328302
    states[3] = 0.988354
    states[4] = 0.99254
    constants[11] = 0.0034
    constants[12] = 4
    states[5] = 157.8
    states[6] = 0.51
    constants[13] = 1
    constants[14] = 0.0027134
    states[7] = 0.264
    constants[15] = 0.23815
    states[8] = 2.63
    states[9] = 0.99
    constants[16] = 2.8
    constants[17] = 13
    constants[18] = 0.002216
    constants[19] = 1.38
    constants[20] = 87.5
    constants[21] = 0.3
    constants[22] = 0.2
    constants[23] = 0.35
    states[10] = 0.00008
    constants[24] = 2
    constants[25] = 0.693
    constants[26] = 10
    constants[27] = 1.5
    constants[28] = 0.00005
    constants[29] = 0.05
    constants[30] = 0.0003842
    constants[31] = 0.0031
    constants[32] = 3.125e-4
    constants[33] = 5.79e-7
    constants[34] = -0.265
    states[11] = 9.84546e-21
    states[12] = 0
    constants[35] = 2
    constants[36] = 2
    constants[37] = 2000
    constants[38] = 300
    constants[39] = 7000
    constants[40] = 7
    constants[41] = 10
    states[13] = 0.997208
    states[14] = 6.38897e-5
    states[15] = 1.535e-9
    states[16] = 1.63909e-14
    states[17] = 6.56337e-20
    states[18] = 0.00272826
    states[19] = 6.99215e-7
    states[20] = 6.71989e-11
    states[21] = 2.87031e-15
    states[22] = 4.59752e-20
    states[23] = 0.00011
    states[24] = 0.798
    constants[42] = 1800
    constants[43] = 1.215e13
    constants[44] = 576
    constants[45] = 4.05e9
    constants[46] = 1930
    constants[47] = 100
    constants[48] = 0.8
    states[25] = 0
    states[26] = 0
    states[27] = 0.47
    states[28] = 0.53
    constants[49] = 4
    constants[50] = 3
    states[29] = 0.257
    constants[51] = 0.000168
    constants[52] = 3.29
    constants[53] = 0.0813
    constants[54] = 0.318
    constants[55] = 1
    constants[56] = 1.2
    constants[57] = 1
    states[30] = 0.257
    constants[58] = 0.0005747
    constants[59] = 0.0267
    states[31] = 0.98
    states[32] = 0.078
    constants[60] = 0.14
    constants[61] = 0.07
    constants[62] = 20000
    constants[63] = 0.066
    constants[64] = 40000
    constants[65] = 40
    constants[66] = 0.0001534
    constants[67] = 0.00002584
    constants[68] = 0.00000016
    constants[69] = 0.0000021
    constants[70] = 0.0000000012
    constants[71] = 0.00238
    constants[72] = 0.00015
    constants[73] = 0.8
    constants[74] = 0.05
    constants[75] = 0
    constants[76] = 15
    constants[77] = power(constants[12]/4.00000, 1.0/2)
    constants[78] = (1.00000/7.00000)*(exp(constants[10]/67.3000)-1.00000)
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[11] = constants[38]*states[17]-constants[37]*states[11]
    rates[12] = constants[40]*states[22]-constants[39]*states[12]
    rates[27] = -constants[43]*(power(states[23], constants[49]))*states[27]+constants[44]*states[25]
    rates[25] = (constants[43]*(power(states[23], constants[49]))*states[27]-(constants[44]*states[25]+constants[45]*(power(states[23], constants[50]))*states[25]+constants[47]*states[25]))+constants[46]*states[26]+constants[48]*states[28]
    rates[26] = constants[45]*(power(states[23], constants[50]))*states[25]-constants[46]*states[26]
    rates[28] = constants[47]*states[25]-constants[48]*states[28]
    algebraic[1] = custom_piecewise([less(states[0] , -40.0000), 135.000*exp((80.0000+states[0])/-6.80000) , True, 0.00000])
    algebraic[11] = custom_piecewise([less(states[0] , -40.0000), 3560.00*exp(0.0790000*states[0])+310000.*exp(0.350000*states[0]) , True, 1000.00/(0.130000*(1.00000+exp((states[0]+10.6600)/-11.1000)))])
    rates[3] = algebraic[1]*(1.00000-states[3])-algebraic[11]*states[3]
    algebraic[2] = custom_piecewise([less(states[0] , -40.0000), (1000.00*-(127140.*exp(0.244400*states[0])+3.47400e-05*exp(-0.0439100*states[0]))*(states[0]+37.7800))/(1.00000+exp(0.311000*(states[0]+79.2300))) , True, 0.00000])
    algebraic[12] = custom_piecewise([less(states[0] , -40.0000), (121.200*exp(-0.0105200*states[0]))/(1.00000+exp(-0.137800*(states[0]+40.1400))) , True, (300.000*exp(-2.53500e-07*states[0]))/(1.00000+exp(-0.100000*(states[0]+32.0000)))])
    rates[4] = algebraic[2]*(1.00000-states[4])-algebraic[12]*states[4]
    algebraic[14] = 0.00100000/((7.19000e-05*(states[0]-10.0000))/(1.00000-exp(-0.148000*(states[0]-10.0000)))+(0.000131000*(states[0]-10.0000))/(exp(0.0687000*(states[0]-10.0000))-1.00000))
    algebraic[4] = 1.00000/(1.00000+exp(-(states[0]-24.7000)/13.6000))
    rates[7] = (algebraic[4]-states[7])/algebraic[14]
    algebraic[5] = 45.1600*exp(0.0357700*states[0])
    algebraic[15] = 98.9000*exp(-0.0623700*states[0])
    rates[8] = algebraic[5]*(1.00000-states[8])-algebraic[15]*states[8]
    algebraic[6] = (5.41500*exp(-(states[0]+33.5000)/5.00000))/(1.00000+0.0513350*exp(-(states[0]+33.5000)/5.00000))
    algebraic[16] = (5.41500*exp((states[0]+33.5000)/5.00000))/(1.00000+0.0513350*exp((states[0]+33.5000)/5.00000))
    rates[9] = algebraic[6]*(1.00000-states[9])-algebraic[16]*states[9]
    algebraic[8] = 0.800000/(1.00000+exp((states[0]+12.5000)/5.00000))+0.200000
    algebraic[18] = (20.0000+600.000/(1.00000+exp((states[0]+20.0000)/9.50000)))/1000.00
    rates[24] = (algebraic[8]-states[24])/algebraic[18]
    algebraic[0] = states[0]+47.1300
    algebraic[10] = custom_piecewise([less(fabs(algebraic[0]) , 1.00000e-05), 1000.00/(0.100000-0.00500000*algebraic[0]) , True, (320.000*algebraic[0])/(1.00000-exp(-0.100000*algebraic[0]))])
    algebraic[20] = 80.0000*exp(-states[0]/11.0000)
    rates[2] = custom_piecewise([greater_equal(states[0] , -90.0000), algebraic[10]*(1.00000-states[2])-algebraic[20]*states[2] , True, 0.00000])
    algebraic[3] = exp(-5.49500+0.169100*states[0])
    algebraic[13] = exp(-7.67700-0.0128000*states[0])
    algebraic[21] = algebraic[3]/(algebraic[3]+algebraic[13])
    algebraic[24] = 0.00100000/(algebraic[3]+algebraic[13])+constants[13]*0.0270000
    rates[6] = (algebraic[21]-states[6])/algebraic[24]
    algebraic[7] = 400.000*exp((states[0]+2.00000)/10.0000)
    algebraic[17] = 50.0000*exp(-(states[0]+2.00000)/13.0000)
    algebraic[27] = (103.750*states[23])/1.00000
    rates[13] = (algebraic[17]*states[14]+constants[41]*states[18])-(4.00000*algebraic[7]+algebraic[27])*states[13]
    rates[14] = (4.00000*algebraic[7]*states[13]+2.00000*algebraic[17]*states[15]+(constants[41]/constants[36])*states[19])-(algebraic[17]+3.00000*algebraic[7]+algebraic[27]*constants[35])*states[14]
    rates[15] = (3.00000*algebraic[7]*states[14]+3.00000*algebraic[17]*states[16]+(constants[41]/(power(constants[36], 2.00000)))*states[20])-(algebraic[17]*2.00000+2.00000*algebraic[7]+algebraic[27]*(power(constants[35], 2.00000)))*states[15]
    rates[16] = (2.00000*algebraic[7]*states[15]+4.00000*algebraic[17]*states[17]+(constants[41]/(power(constants[36], 3.00000)))*states[21])-(algebraic[17]*3.00000+algebraic[7]+algebraic[27]*(power(constants[35], 3.00000)))*states[16]
    rates[17] = (algebraic[7]*states[16]+constants[37]*states[11]+(constants[41]/(power(constants[36], 4.00000)))*states[22])-(algebraic[17]*4.00000+constants[38]+algebraic[27]*(power(constants[35], 4.00000)))*states[17]
    algebraic[22] = algebraic[7]*constants[35]
    algebraic[25] = algebraic[17]/constants[36]
    rates[18] = (algebraic[25]*states[19]+algebraic[27]*states[13])-(4.00000*algebraic[22]+constants[41])*states[18]
    rates[19] = (4.00000*algebraic[22]*states[18]+2.00000*algebraic[25]*states[20]+algebraic[27]*constants[35]*states[14])-(algebraic[25]+3.00000*algebraic[22]+constants[41]/constants[36])*states[19]
    rates[20] = (3.00000*algebraic[22]*states[19]+3.00000*algebraic[25]*states[21]+algebraic[27]*(power(constants[35], 2.00000))*states[15])-(algebraic[25]*2.00000+2.00000*algebraic[22]+constants[41]/(power(constants[36], 2.00000)))*states[20]
    rates[21] = (2.00000*algebraic[22]*states[20]+4.00000*algebraic[25]*states[22]+algebraic[27]*(power(constants[35], 3.00000))*states[16])-(algebraic[25]*3.00000+algebraic[22]+constants[41]/(power(constants[36], 3.00000)))*states[21]
    rates[22] = (algebraic[22]*states[21]+constants[39]*states[12]+algebraic[27]*(power(constants[35], 4.00000))*states[17])-(algebraic[25]*4.00000+constants[40]+constants[41]/(power(constants[36], 4.00000)))*states[22]
    algebraic[19] = ((constants[0]*constants[1])/constants[2])*log(constants[10]/states[1])
    algebraic[23] = constants[9]*(power(states[2], 3.00000))*states[3]*states[4]*(states[0]-algebraic[19])
    algebraic[37] = ((constants[21]*5000.00)/((power(constants[20], 3.00000)+power(constants[10], 3.00000))*(constants[19]+constants[24])*(1.00000+constants[22]*exp(((constants[23]-1.00000)*states[0]*constants[2])/(constants[0]*constants[1])))))*(exp((constants[23]*states[0]*constants[2])/(constants[0]*constants[1]))*(power(states[1], 3.00000))*constants[24]-exp(((constants[23]-1.00000)*states[0]*constants[2])/(constants[0]*constants[1]))*(power(constants[10], 3.00000))*states[10])
    algebraic[38] = 1.00000/(1.00000+0.124500*exp((-0.100000*states[0]*constants[2])/(constants[0]*constants[1]))+0.0365000*constants[78]*exp((-states[0]*constants[2])/(constants[0]*constants[1])))
    algebraic[39] = (((constants[25]*algebraic[38])/(1.00000+power(constants[26]/states[1], 1.50000)))*constants[12])/(constants[12]+constants[27])
    algebraic[43] = constants[31]*(states[0]-algebraic[19])
    rates[1] = (-0.00000*(algebraic[23]+algebraic[43]+algebraic[37]*3.00000+algebraic[39]*3.00000)*constants[66]*1.00000)/(constants[67]*constants[2])
    algebraic[44] = ((((constants[32]/(1.00000*1.00000))*4.00000*states[0]*(power(constants[2], 2.00000))*1000.00)/(constants[0]*constants[1]))*(0.00100000*exp((2.00000*states[0]*constants[2])/(constants[0]*constants[1]))-0.341000*constants[24]))/(exp((2.00000*states[0]*constants[2])/(constants[0]*constants[1]))-1.00000)
    algebraic[45] = algebraic[44]*states[24]*(states[11]+states[12])
    algebraic[46] = constants[33]/(1.00000+algebraic[44]/constants[34])
    algebraic[48] = ((((algebraic[46]/(1.00000*1.00000))*states[24]*(states[11]+states[12])*states[0]*(power(constants[2], 2.00000)))/(constants[0]*constants[1]))*(states[5]*exp((states[0]*constants[2])/(constants[0]*constants[1]))-constants[12]))/(exp((states[0]*constants[2])/(constants[0]*constants[1]))-1.00000)
    algebraic[26] = ((constants[0]*constants[1])/constants[2])*log(constants[12]/states[5])
    algebraic[28] = 1.00000/(1.00000+1.49450*exp(0.0446000*states[0]))
    algebraic[29] = constants[11]*constants[77]*algebraic[28]*states[6]*(states[0]-algebraic[26])
    algebraic[30] = ((constants[0]*constants[1])/constants[2])*log((constants[12]+0.0183300*constants[10])/(states[5]+0.0183300*states[1]))
    algebraic[31] = constants[14]*(power(states[7], 2.00000))*(states[0]-algebraic[30])
    algebraic[32] = constants[15]*states[8]*states[9]*(states[0]-algebraic[26])
    algebraic[33] = 1.00000/(2.00000+exp(((1.50000*constants[2])/(constants[0]*constants[1]))*(states[0]-algebraic[26])))
    algebraic[34] = ((constants[16]*algebraic[33]*constants[12])/(constants[12]+constants[17]))*(states[0]-algebraic[26])
    algebraic[35] = 1.00000/(1.00000+exp((7.48800-states[0])/5.98000))
    algebraic[36] = constants[18]*algebraic[35]*(states[0]-algebraic[26])
    algebraic[40] = (constants[29]*states[10])/(constants[28]+states[10])
    algebraic[41] = ((constants[0]*constants[1])/(2.00000*constants[2]))*log(constants[24]/states[10])
    algebraic[42] = constants[30]*(states[0]-algebraic[41])
    algebraic[9] = custom_piecewise([greater_equal(voi , constants[4]) & less_equal(voi , constants[5]) & less_equal((voi-constants[4])-floor((voi-constants[4])/constants[6])*constants[6] , constants[7]), constants[8] , True, 0.00000])
    rates[0] = (-1.00000*1.00000*(algebraic[23]+algebraic[45]+algebraic[48]+algebraic[29]+algebraic[31]+algebraic[32]+algebraic[34]+algebraic[36]+algebraic[37]+algebraic[39]+algebraic[40]+algebraic[43]+algebraic[42]+algebraic[9]))/constants[3]
    rates[5] = (-0.00000*(algebraic[48]+algebraic[29]+algebraic[31]+algebraic[34]+algebraic[36]+algebraic[32]+algebraic[39]*-2.00000)*constants[66]*1.00000)/(constants[67]*constants[2])
    rates[31] = constants[62]*states[10]*(1.00000-states[31])-constants[63]*states[31]
    algebraic[49] = power(states[10]/constants[51], constants[56])
    algebraic[50] = power(states[30]/constants[52], constants[57])
    algebraic[51] = (constants[55]*(constants[53]*algebraic[49]-constants[54]*algebraic[50]))/(1.00000+algebraic[49]+algebraic[50])
    algebraic[53] = (states[30]-states[29])/constants[58]
    rates[30] = (algebraic[51]*constants[67])/constants[69]-(algebraic[53]*constants[68])/constants[69]
    algebraic[47] = constants[42]*(states[25]+states[26])*(states[29]-states[23])
    algebraic[52] = (states[23]-states[10])/constants[59]
    algebraic[54] = 1.00000/(1.00000+(constants[74]*constants[71])/(power(constants[71]+states[23], 2.00000))+(constants[75]*constants[72])/(power(constants[72]+states[23], 2.00000)))
    rates[23] = algebraic[54]*(((algebraic[47]*constants[68])/constants[70]-(algebraic[52]*constants[67])/constants[70])-(algebraic[45]*constants[66]*1.00000)/(2.00000*constants[70]*constants[2]))
    algebraic[55] = 1.00000/(1.00000+(constants[76]*constants[73])/(power(constants[73]+states[29], 2.00000)))
    rates[29] = algebraic[55]*(algebraic[53]-algebraic[47])
    rates[32] = constants[64]*states[10]*(1.00000-states[32])-constants[65]*states[32]
    algebraic[56] = rates[31]
    algebraic[57] = rates[32]
    algebraic[58] = constants[60]*algebraic[56]+constants[61]*algebraic[57]
    algebraic[59] = 1.00000/(1.00000+(constants[74]*constants[71])/(power(constants[71]+states[10], 2.00000))+(constants[75]*constants[72])/(power(constants[72]+states[10], 2.00000)))
    rates[10] = algebraic[59]*((algebraic[52]-(algebraic[51]+algebraic[58]))+((2.00000*algebraic[37]-(algebraic[40]+algebraic[42]))*constants[66]*1.00000)/(2.00000*constants[67]*constants[2]))
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[1] = custom_piecewise([less(states[0] , -40.0000), 135.000*exp((80.0000+states[0])/-6.80000) , True, 0.00000])
    algebraic[11] = custom_piecewise([less(states[0] , -40.0000), 3560.00*exp(0.0790000*states[0])+310000.*exp(0.350000*states[0]) , True, 1000.00/(0.130000*(1.00000+exp((states[0]+10.6600)/-11.1000)))])
    algebraic[2] = custom_piecewise([less(states[0] , -40.0000), (1000.00*-(127140.*exp(0.244400*states[0])+3.47400e-05*exp(-0.0439100*states[0]))*(states[0]+37.7800))/(1.00000+exp(0.311000*(states[0]+79.2300))) , True, 0.00000])
    algebraic[12] = custom_piecewise([less(states[0] , -40.0000), (121.200*exp(-0.0105200*states[0]))/(1.00000+exp(-0.137800*(states[0]+40.1400))) , True, (300.000*exp(-2.53500e-07*states[0]))/(1.00000+exp(-0.100000*(states[0]+32.0000)))])
    algebraic[14] = 0.00100000/((7.19000e-05*(states[0]-10.0000))/(1.00000-exp(-0.148000*(states[0]-10.0000)))+(0.000131000*(states[0]-10.0000))/(exp(0.0687000*(states[0]-10.0000))-1.00000))
    algebraic[4] = 1.00000/(1.00000+exp(-(states[0]-24.7000)/13.6000))
    algebraic[5] = 45.1600*exp(0.0357700*states[0])
    algebraic[15] = 98.9000*exp(-0.0623700*states[0])
    algebraic[6] = (5.41500*exp(-(states[0]+33.5000)/5.00000))/(1.00000+0.0513350*exp(-(states[0]+33.5000)/5.00000))
    algebraic[16] = (5.41500*exp((states[0]+33.5000)/5.00000))/(1.00000+0.0513350*exp((states[0]+33.5000)/5.00000))
    algebraic[8] = 0.800000/(1.00000+exp((states[0]+12.5000)/5.00000))+0.200000
    algebraic[18] = (20.0000+600.000/(1.00000+exp((states[0]+20.0000)/9.50000)))/1000.00
    algebraic[0] = states[0]+47.1300
    algebraic[10] = custom_piecewise([less(fabs(algebraic[0]) , 1.00000e-05), 1000.00/(0.100000-0.00500000*algebraic[0]) , True, (320.000*algebraic[0])/(1.00000-exp(-0.100000*algebraic[0]))])
    algebraic[20] = 80.0000*exp(-states[0]/11.0000)
    algebraic[3] = exp(-5.49500+0.169100*states[0])
    algebraic[13] = exp(-7.67700-0.0128000*states[0])
    algebraic[21] = algebraic[3]/(algebraic[3]+algebraic[13])
    algebraic[24] = 0.00100000/(algebraic[3]+algebraic[13])+constants[13]*0.0270000
    algebraic[7] = 400.000*exp((states[0]+2.00000)/10.0000)
    algebraic[17] = 50.0000*exp(-(states[0]+2.00000)/13.0000)
    algebraic[27] = (103.750*states[23])/1.00000
    algebraic[22] = algebraic[7]*constants[35]
    algebraic[25] = algebraic[17]/constants[36]
    algebraic[19] = ((constants[0]*constants[1])/constants[2])*log(constants[10]/states[1])
    algebraic[23] = constants[9]*(power(states[2], 3.00000))*states[3]*states[4]*(states[0]-algebraic[19])
    algebraic[37] = ((constants[21]*5000.00)/((power(constants[20], 3.00000)+power(constants[10], 3.00000))*(constants[19]+constants[24])*(1.00000+constants[22]*exp(((constants[23]-1.00000)*states[0]*constants[2])/(constants[0]*constants[1])))))*(exp((constants[23]*states[0]*constants[2])/(constants[0]*constants[1]))*(power(states[1], 3.00000))*constants[24]-exp(((constants[23]-1.00000)*states[0]*constants[2])/(constants[0]*constants[1]))*(power(constants[10], 3.00000))*states[10])
    algebraic[38] = 1.00000/(1.00000+0.124500*exp((-0.100000*states[0]*constants[2])/(constants[0]*constants[1]))+0.0365000*constants[78]*exp((-states[0]*constants[2])/(constants[0]*constants[1])))
    algebraic[39] = (((constants[25]*algebraic[38])/(1.00000+power(constants[26]/states[1], 1.50000)))*constants[12])/(constants[12]+constants[27])
    algebraic[43] = constants[31]*(states[0]-algebraic[19])
    algebraic[44] = ((((constants[32]/(1.00000*1.00000))*4.00000*states[0]*(power(constants[2], 2.00000))*1000.00)/(constants[0]*constants[1]))*(0.00100000*exp((2.00000*states[0]*constants[2])/(constants[0]*constants[1]))-0.341000*constants[24]))/(exp((2.00000*states[0]*constants[2])/(constants[0]*constants[1]))-1.00000)
    algebraic[45] = algebraic[44]*states[24]*(states[11]+states[12])
    algebraic[46] = constants[33]/(1.00000+algebraic[44]/constants[34])
    algebraic[48] = ((((algebraic[46]/(1.00000*1.00000))*states[24]*(states[11]+states[12])*states[0]*(power(constants[2], 2.00000)))/(constants[0]*constants[1]))*(states[5]*exp((states[0]*constants[2])/(constants[0]*constants[1]))-constants[12]))/(exp((states[0]*constants[2])/(constants[0]*constants[1]))-1.00000)
    algebraic[26] = ((constants[0]*constants[1])/constants[2])*log(constants[12]/states[5])
    algebraic[28] = 1.00000/(1.00000+1.49450*exp(0.0446000*states[0]))
    algebraic[29] = constants[11]*constants[77]*algebraic[28]*states[6]*(states[0]-algebraic[26])
    algebraic[30] = ((constants[0]*constants[1])/constants[2])*log((constants[12]+0.0183300*constants[10])/(states[5]+0.0183300*states[1]))
    algebraic[31] = constants[14]*(power(states[7], 2.00000))*(states[0]-algebraic[30])
    algebraic[32] = constants[15]*states[8]*states[9]*(states[0]-algebraic[26])
    algebraic[33] = 1.00000/(2.00000+exp(((1.50000*constants[2])/(constants[0]*constants[1]))*(states[0]-algebraic[26])))
    algebraic[34] = ((constants[16]*algebraic[33]*constants[12])/(constants[12]+constants[17]))*(states[0]-algebraic[26])
    algebraic[35] = 1.00000/(1.00000+exp((7.48800-states[0])/5.98000))
    algebraic[36] = constants[18]*algebraic[35]*(states[0]-algebraic[26])
    algebraic[40] = (constants[29]*states[10])/(constants[28]+states[10])
    algebraic[41] = ((constants[0]*constants[1])/(2.00000*constants[2]))*log(constants[24]/states[10])
    algebraic[42] = constants[30]*(states[0]-algebraic[41])
    algebraic[9] = custom_piecewise([greater_equal(voi , constants[4]) & less_equal(voi , constants[5]) & less_equal((voi-constants[4])-floor((voi-constants[4])/constants[6])*constants[6] , constants[7]), constants[8] , True, 0.00000])
    algebraic[49] = power(states[10]/constants[51], constants[56])
    algebraic[50] = power(states[30]/constants[52], constants[57])
    algebraic[51] = (constants[55]*(constants[53]*algebraic[49]-constants[54]*algebraic[50]))/(1.00000+algebraic[49]+algebraic[50])
    algebraic[53] = (states[30]-states[29])/constants[58]
    algebraic[47] = constants[42]*(states[25]+states[26])*(states[29]-states[23])
    algebraic[52] = (states[23]-states[10])/constants[59]
    algebraic[54] = 1.00000/(1.00000+(constants[74]*constants[71])/(power(constants[71]+states[23], 2.00000))+(constants[75]*constants[72])/(power(constants[72]+states[23], 2.00000)))
    algebraic[55] = 1.00000/(1.00000+(constants[76]*constants[73])/(power(constants[73]+states[29], 2.00000)))
    algebraic[56] = rates[31]
    algebraic[57] = rates[32]
    algebraic[58] = constants[60]*algebraic[56]+constants[61]*algebraic[57]
    algebraic[59] = 1.00000/(1.00000+(constants[74]*constants[71])/(power(constants[71]+states[10], 2.00000))+(constants[75]*constants[72])/(power(constants[72]+states[10], 2.00000)))
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
        self.R = 8.314472
        self.T = 310
        self.F = 96.4853415
        self.C_sc = 0.001
        self.stim_start = 0.1
        self.stim_end = 100000000
        self.stim_period = 1
        self.stim_duration = 0.002
        self.stim_amplitude = -21.1268
        self.g_Na = 12.8
        self.Nao = 138
        self.g_Kr = 0.0034
        self.Ko = 4
        self.tau_factor = 1
        self.g_Ks = 0.0027134
        self.g_to1 = 0.23815
        self.g_K1 = 2.8
        self.K_mK1 = 13
        self.g_Kp = 0.002216
        self.K_mCa = 1.38
        self.K_mNa = 87.5
        self.K_NaCa = 0.3
        self.K_sat = 0.2
        self.eta = 0.35
        self.Cao = 2
        self.I_NaK = 0.693
        self.K_mNai = 10
        self.K_mKo = 1.5
        self.K_mpCa = 0.00005
        self.I_pCa = 0.05
        self.g_Cab = 0.0003842
        self.g_Nab = 0.0031
        self.P_Ca = 3.125e-4
        self.P_K = 5.79e-7
        self.i_Ca_half = -0.265
        self.a = 2
        self.b = 2
        self.g = 2000
        self.f = 300
        self.gprime = 7000
        self.fprime = 7
        self.omega = 10
        self.v1 = 1800
        self.k_a_plus = 1.215e13
        self.k_a_minus = 576
        self.k_b_plus = 4.05e9
        self.k_b_minus = 1930
        self.k_c_plus = 100
        self.k_c_minus = 0.8
        self.n = 4
        self.m = 3
        self.K_fb = 0.000168
        self.K_rb = 3.29
        self.Vmaxf = 0.0813
        self.Vmaxr = 0.318
        self.K_SR = 1
        self.N_fb = 1.2
        self.N_rb = 1
        self.tau_tr = 0.0005747
        self.tau_xfer = 0.0267
        self.HTRPN_tot = 0.14
        self.LTRPN_tot = 0.07
        self.k_htrpn_plus = 20000
        self.k_htrpn_minus = 0.066
        self.k_ltrpn_plus = 40000
        self.k_ltrpn_minus = 40
        self.A_cap = 0.0001534
        self.V_myo = 0.00002584
        self.V_JSR = 0.00000016
        self.V_NSR = 0.0000021
        self.V_SS = 0.0000000012
        self.K_mCMDN = 0.00238
        self.K_mEGTA = 0.00015
        self.K_mCSQN = 0.8
        self.CMDN_tot = 0.05
        self.EGTA_tot = 0
        self.CSQN_tot = 15

    def to_dict(self):
        return {
            "R": self.R,
            "T": self.T,
            "F": self.F,
            "C_sc": self.C_sc,
            "stim_start": self.stim_start,
            "stim_end": self.stim_end,
            "stim_period": self.stim_period,
            "stim_duration": self.stim_duration,
            "stim_amplitude": self.stim_amplitude,
            "g_Na": self.g_Na,
            "Nao": self.Nao,
            "g_Kr": self.g_Kr,
            "Ko": self.Ko,
            "tau_factor": self.tau_factor,
            "g_Ks": self.g_Ks,
            "g_to1": self.g_to1,
            "g_K1": self.g_K1,
            "K_mK1": self.K_mK1,
            "g_Kp": self.g_Kp,
            "K_mCa": self.K_mCa,
            "K_mNa": self.K_mNa,
            "K_NaCa": self.K_NaCa,
            "K_sat": self.K_sat,
            "eta": self.eta,
            "Cao": self.Cao,
            "I_NaK": self.I_NaK,
            "K_mNai": self.K_mNai,
            "K_mKo": self.K_mKo,
            "K_mpCa": self.K_mpCa,
            "I_pCa": self.I_pCa,
            "g_Cab": self.g_Cab,
            "g_Nab": self.g_Nab,
            "P_Ca": self.P_Ca,
            "P_K": self.P_K,
            "i_Ca_half": self.i_Ca_half,
            "a": self.a,
            "b": self.b,
            "g": self.g,
            "f": self.f,
            "gprime": self.gprime,
            "fprime": self.fprime,
            "omega": self.omega,
            "v1": self.v1,
            "k_a_plus": self.k_a_plus,
            "k_a_minus": self.k_a_minus,
            "k_b_plus": self.k_b_plus,
            "k_b_minus": self.k_b_minus,
            "k_c_plus": self.k_c_plus,
            "k_c_minus": self.k_c_minus,
            "n": self.n,
            "m": self.m,
            "K_fb": self.K_fb,
            "K_rb": self.K_rb,
            "Vmaxf": self.Vmaxf,
            "Vmaxr": self.Vmaxr,
            "K_SR": self.K_SR,
            "N_fb": self.N_fb,
            "N_rb": self.N_rb,
            "tau_tr": self.tau_tr,
            "tau_xfer": self.tau_xfer,
            "HTRPN_tot": self.HTRPN_tot,
            "LTRPN_tot": self.LTRPN_tot,
            "k_htrpn_plus": self.k_htrpn_plus,
            "k_htrpn_minus": self.k_htrpn_minus,
            "k_ltrpn_plus": self.k_ltrpn_plus,
            "k_ltrpn_minus": self.k_ltrpn_minus,
            "A_cap": self.A_cap,
            "V_myo": self.V_myo,
            "V_JSR": self.V_JSR,
            "V_NSR": self.V_NSR,
            "V_SS": self.V_SS,
            "K_mCMDN": self.K_mCMDN,
            "K_mEGTA": self.K_mEGTA,
            "K_mCSQN": self.K_mCSQN,
            "CMDN_tot": self.CMDN_tot,
            "EGTA_tot": self.EGTA_tot,
            "CSQN_tot": self.CSQN_tot,
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
        y0=[-96.1638, 10, 0.0328302, 0.988354, 0.99254, 157.8, 0.51, 0.264, 2.63, 0.99, 0.00008, 9.84546e-21, 0, 0.997208, 6.38897e-5, 1.535e-9, 1.63909e-14, 6.56337e-20, 0.00272826, 6.99215e-7, 6.71989e-11, 2.87031e-15, 4.59752e-20, 0.00011, 0.798, 0, 0, 0.47, 0.53, 0.257, 0.257, 0.98, 0.078],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "winslow_rice_jafri_marban_ororke_1999"
        self.curve_names = [
            "V",
            "Nai",
            "m",
            "h",
            "j",
            "Ki",
            "X_kr",
            "X_ks",
            "X_to1",
            "Y_to1",
            "Cai",
            "O",
            "O_Ca",
            "C0",
            "C1",
            "C2",
            "C3",
            "C4",
            "C_Ca0",
            "C_Ca1",
            "C_Ca2",
            "C_Ca3",
            "C_Ca4",
            "Ca_ss",
            "y",
            "P_O1",
            "P_O2",
            "P_C1",
            "P_C2",
            "Ca_JSR",
            "Ca_NSR",
            "HTRPNCa",
            "LTRPNCa",
        ]
        self.state_names = ['V', 'Nai', 'm', 'h', 'j', 'Ki', 'X_kr', 'X_ks', 'X_to1', 'Y_to1', 'Cai', 'O', 'O_Ca', 'C0', 'C1', 'C2', 'C3', 'C4', 'C_Ca0', 'C_Ca1', 'C_Ca2', 'C_Ca3', 'C_Ca4', 'Ca_ss', 'y', 'P_O1', 'P_O2', 'P_C1', 'P_C2', 'Ca_JSR', 'Ca_NSR', 'HTRPNCa', 'LTRPNCa']
        self.algebraic_names = ['E0_m', 'alpha_h', 'alpha_j', 'K12', 'X_ks_infinity', 'alpha_X_to1', 'alpha_Y_to1', 'alpha', 'y_infinity', 'i_Stim', 'alpha_m', 'beta_h', 'beta_j', 'K21', 'tau_X_ks', 'beta_X_to1', 'beta_Y_to1', 'beta', 'tau_y', 'E_Na', 'beta_m', 'X_kr_inf', 'alpha_a', 'i_Na', 'tau_X_kr', 'beta_b', 'E_K', 'gamma', 'R_V', 'i_Kr', 'E_Ks', 'i_Ks', 'i_to1', 'K1_infinity_V', 'i_K1', 'Kp_V', 'i_Kp', 'i_NaCa', 'f_NaK', 'i_NaK', 'i_p_Ca', 'E_Ca', 'i_Ca_b', 'i_Na_b', 'i_Ca_max', 'i_Ca', 'p_prime_k', 'J_rel', 'i_Ca_K', 'fb', 'rb', 'J_up', 'J_xfer', 'J_tr', 'beta_SS', 'beta_JSR', 'J_HTRPNCa', 'J_LTRPNCa', 'J_trpn', 'beta_i']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 79
        p = self.params

        # direct mapping
        c[0] = p.R
        c[1] = p.T
        c[2] = p.F
        c[3] = p.C_sc
        c[4] = p.stim_start
        c[5] = p.stim_end
        c[6] = p.stim_period
        c[7] = p.stim_duration
        c[8] = p.stim_amplitude
        c[9] = p.g_Na
        c[10] = p.Nao
        c[11] = p.g_Kr
        c[12] = p.Ko
        c[13] = p.tau_factor
        c[14] = p.g_Ks
        c[15] = p.g_to1
        c[16] = p.g_K1
        c[17] = p.K_mK1
        c[18] = p.g_Kp
        c[19] = p.K_mCa
        c[20] = p.K_mNa
        c[21] = p.K_NaCa
        c[22] = p.K_sat
        c[23] = p.eta
        c[24] = p.Cao
        c[25] = p.I_NaK
        c[26] = p.K_mNai
        c[27] = p.K_mKo
        c[28] = p.K_mpCa
        c[29] = p.I_pCa
        c[30] = p.g_Cab
        c[31] = p.g_Nab
        c[32] = p.P_Ca
        c[33] = p.P_K
        c[34] = p.i_Ca_half
        c[35] = p.a
        c[36] = p.b
        c[37] = p.g
        c[38] = p.f
        c[39] = p.gprime
        c[40] = p.fprime
        c[41] = p.omega
        c[42] = p.v1
        c[43] = p.k_a_plus
        c[44] = p.k_a_minus
        c[45] = p.k_b_plus
        c[46] = p.k_b_minus
        c[47] = p.k_c_plus
        c[48] = p.k_c_minus
        c[49] = p.n
        c[50] = p.m
        c[51] = p.K_fb
        c[52] = p.K_rb
        c[53] = p.Vmaxf
        c[54] = p.Vmaxr
        c[55] = p.K_SR
        c[56] = p.N_fb
        c[57] = p.N_rb
        c[58] = p.tau_tr
        c[59] = p.tau_xfer
        c[60] = p.HTRPN_tot
        c[61] = p.LTRPN_tot
        c[62] = p.k_htrpn_plus
        c[63] = p.k_htrpn_minus
        c[64] = p.k_ltrpn_plus
        c[65] = p.k_ltrpn_minus
        c[66] = p.A_cap
        c[67] = p.V_myo
        c[68] = p.V_JSR
        c[69] = p.V_NSR
        c[70] = p.V_SS
        c[71] = p.K_mCMDN
        c[72] = p.K_mEGTA
        c[73] = p.K_mCSQN
        c[74] = p.CMDN_tot
        c[75] = p.EGTA_tot
        c[76] = p.CSQN_tot

        # derived constants
        c[77] = power(c[12]/4.00000, 1.0/2)
        c[78] = (1.00000/7.00000)*(exp(c[10]/67.3000)-1.00000)

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
