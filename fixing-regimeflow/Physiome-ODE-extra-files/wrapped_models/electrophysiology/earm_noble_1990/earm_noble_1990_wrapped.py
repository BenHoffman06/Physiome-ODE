# Size of variable arrays:
sizeAlgebraic = 41
sizeStates = 16
sizeConstants = 54
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
    legend_constants[0] = "R in component membrane (joule_per_kilomole_kelvin)"
    legend_constants[1] = "T in component membrane (kelvin)"
    legend_constants[2] = "F in component membrane (coulomb_per_mole)"
    legend_constants[49] = "RTONF in component membrane (millivolt)"
    legend_constants[3] = "C_m in component membrane (microF)"
    legend_algebraic[26] = "i_b_K in component potassium_background_current (nanoA)"
    legend_algebraic[27] = "i_K1 in component time_independent_potassium_current (nanoA)"
    legend_algebraic[18] = "i_to in component transient_outward_current (nanoA)"
    legend_algebraic[22] = "i_b_Na in component sodium_background_current (nanoA)"
    legend_algebraic[24] = "i_b_Ca in component calcium_background_current (nanoA)"
    legend_algebraic[20] = "i_NaK in component sodium_potassium_pump (nanoA)"
    legend_algebraic[25] = "i_NaCa in component Na_Ca_exchanger (nanoA)"
    legend_algebraic[14] = "i_Na in component fast_sodium_current (nanoA)"
    legend_algebraic[38] = "i_Ca_L in component L_type_calcium_current (nanoA)"
    legend_algebraic[4] = "i_Stim in component membrane (nanoA)"
    legend_constants[4] = "stim_start in component membrane (second)"
    legend_constants[5] = "stim_end in component membrane (second)"
    legend_constants[6] = "stim_period in component membrane (second)"
    legend_constants[7] = "stim_duration in component membrane (second)"
    legend_constants[8] = "stim_amplitude in component membrane (nanoA)"
    legend_constants[9] = "g_Na in component fast_sodium_current (microS)"
    legend_algebraic[10] = "E_mh in component fast_sodium_current (millivolt)"
    legend_constants[10] = "Na_o in component extracellular_sodium_concentration (millimolar)"
    legend_states[1] = "Na_i in component intracellular_sodium_concentration (millimolar)"
    legend_constants[11] = "K_c in component extracellular_potassium_concentration (millimolar)"
    legend_states[2] = "K_i in component intracellular_potassium_concentration (millimolar)"
    legend_states[3] = "m in component fast_sodium_current_m_gate (dimensionless)"
    legend_states[4] = "h in component fast_sodium_current_h_gate (dimensionless)"
    legend_algebraic[6] = "alpha_m in component fast_sodium_current_m_gate (per_second)"
    legend_algebraic[12] = "beta_m in component fast_sodium_current_m_gate (per_second)"
    legend_constants[12] = "delta_m in component fast_sodium_current_m_gate (millivolt)"
    legend_algebraic[0] = "E0_m in component fast_sodium_current_m_gate (millivolt)"
    legend_algebraic[1] = "alpha_h in component fast_sodium_current_h_gate (per_second)"
    legend_algebraic[7] = "beta_h in component fast_sodium_current_h_gate (per_second)"
    legend_constants[13] = "g_to in component transient_outward_current (microS)"
    legend_algebraic[16] = "E_K in component transient_outward_current (millivolt)"
    legend_constants[14] = "g_to_s in component transient_outward_current (dimensionless)"
    legend_states[5] = "r in component transient_outward_current_r_gate (dimensionless)"
    legend_states[6] = "s in component transient_outward_current_s_gate (dimensionless)"
    legend_algebraic[2] = "alpha_s in component transient_outward_current_s_gate (per_second)"
    legend_algebraic[8] = "beta_s in component transient_outward_current_s_gate (per_second)"
    legend_constants[15] = "i_NaK_max in component sodium_potassium_pump (nanoA)"
    legend_constants[16] = "K_mK in component sodium_potassium_pump (millimolar)"
    legend_constants[17] = "K_mNa in component sodium_potassium_pump (millimolar)"
    legend_algebraic[21] = "E_Na in component sodium_background_current (millivolt)"
    legend_constants[18] = "g_b_Na in component sodium_background_current (microS)"
    legend_algebraic[23] = "E_Ca in component calcium_background_current (millivolt)"
    legend_constants[19] = "g_b_Ca in component calcium_background_current (microS)"
    legend_constants[20] = "Ca_o in component extracellular_calcium_concentration (millimolar)"
    legend_states[7] = "Ca_i in component intracellular_calcium_concentration (millimolar)"
    legend_constants[21] = "k_NaCa in component Na_Ca_exchanger (nanoA)"
    legend_constants[22] = "n_NaCa in component Na_Ca_exchanger (dimensionless)"
    legend_constants[23] = "d_NaCa in component Na_Ca_exchanger (dimensionless)"
    legend_constants[24] = "gamma in component Na_Ca_exchanger (dimensionless)"
    legend_constants[25] = "g_b_K in component potassium_background_current (microS)"
    legend_constants[26] = "g_K1 in component time_independent_potassium_current (microS)"
    legend_constants[27] = "K_m_K1 in component time_independent_potassium_current (millimolar)"
    legend_algebraic[33] = "i_Ca_L_Ca in component L_type_calcium_current (nanoA)"
    legend_algebraic[34] = "i_Ca_L_K in component L_type_calcium_current (nanoA)"
    legend_algebraic[36] = "i_Ca_L_Na in component L_type_calcium_current (nanoA)"
    legend_constants[28] = "P_Ca_L in component L_type_calcium_current (nanoA_per_millimolar)"
    legend_states[8] = "d in component L_type_calcium_current_d_gate (dimensionless)"
    legend_states[9] = "f_Ca in component L_type_calcium_current_f_Ca_gate (dimensionless)"
    legend_algebraic[32] = "CaChon in component L_type_calcium_current_f_Ca_gate (dimensionless)"
    legend_algebraic[9] = "alpha_d in component L_type_calcium_current_d_gate (per_second)"
    legend_algebraic[13] = "beta_d in component L_type_calcium_current_d_gate (per_second)"
    legend_algebraic[3] = "E0_d in component L_type_calcium_current_d_gate (millivolt)"
    legend_algebraic[29] = "alpha_f_Ca in component L_type_calcium_current_f_Ca_gate (per_second)"
    legend_algebraic[30] = "beta_f_Ca in component L_type_calcium_current_f_Ca_gate (per_second)"
    legend_algebraic[31] = "CaChoff in component L_type_calcium_current_f_Ca_gate (dimensionless)"
    legend_algebraic[28] = "E0_f in component L_type_calcium_current_f_Ca_gate (millivolt)"
    legend_algebraic[37] = "i_up in component sarcoplasmic_reticulum_calcium_pump (millimolar_per_second)"
    legend_constants[51] = "K_1 in component sarcoplasmic_reticulum_calcium_pump (dimensionless)"
    legend_algebraic[35] = "K_2 in component sarcoplasmic_reticulum_calcium_pump (millimolar)"
    legend_constants[29] = "K_cyca in component sarcoplasmic_reticulum_calcium_pump (millimolar)"
    legend_constants[30] = "K_xcs in component sarcoplasmic_reticulum_calcium_pump (dimensionless)"
    legend_constants[31] = "K_srca in component sarcoplasmic_reticulum_calcium_pump (millimolar)"
    legend_constants[32] = "alpha_up in component sarcoplasmic_reticulum_calcium_pump (millimolar_per_second)"
    legend_constants[33] = "beta_up in component sarcoplasmic_reticulum_calcium_pump (millimolar_per_second)"
    legend_states[10] = "Ca_up in component intracellular_calcium_concentration (millimolar)"
    legend_algebraic[39] = "i_rel in component calcium_release (millimolar_per_second)"
    legend_algebraic[11] = "VoltDep in component calcium_release (dimensionless)"
    legend_algebraic[15] = "RegBindSite in component calcium_release (dimensionless)"
    legend_algebraic[17] = "ActRate in component calcium_release (per_second)"
    legend_algebraic[19] = "InactRate in component calcium_release (per_second)"
    legend_constants[34] = "K_leak_rate in component calcium_release (per_second)"
    legend_constants[35] = "K_m_rel in component calcium_release (per_second)"
    legend_algebraic[5] = "PrecFrac in component calcium_release (dimensionless)"
    legend_states[11] = "ActFrac in component calcium_release (dimensionless)"
    legend_states[12] = "ProdFrac in component calcium_release (dimensionless)"
    legend_constants[36] = "ProdFracRate in component calcium_release (per_second)"
    legend_states[13] = "Ca_rel in component intracellular_calcium_concentration (millimolar)"
    legend_algebraic[40] = "i_trans in component calcium_translocation (millimolar_per_second)"
    legend_constants[37] = "alpha_tr in component calcium_translocation (per_second)"
    legend_constants[53] = "V_i in component intracellular_calcium_concentration (micrometre3)"
    legend_states[14] = "Ca_Calmod in component intracellular_calcium_concentration (millimolar)"
    legend_states[15] = "Ca_Trop in component intracellular_calcium_concentration (millimolar)"
    legend_constants[38] = "Calmod in component intracellular_calcium_concentration (millimolar)"
    legend_constants[39] = "Trop in component intracellular_calcium_concentration (millimolar)"
    legend_constants[40] = "alpha_Calmod in component intracellular_calcium_concentration (per_millimolar_second)"
    legend_constants[41] = "beta_Calmod in component intracellular_calcium_concentration (per_second)"
    legend_constants[42] = "alpha_Trop in component intracellular_calcium_concentration (per_millimolar_second)"
    legend_constants[43] = "beta_Trop in component intracellular_calcium_concentration (per_second)"
    legend_constants[44] = "radius in component intracellular_calcium_concentration (micrometre)"
    legend_constants[45] = "length in component intracellular_calcium_concentration (micrometre)"
    legend_constants[50] = "V_Cell in component intracellular_calcium_concentration (micrometre3)"
    legend_constants[52] = "V_i_ratio in component intracellular_calcium_concentration (dimensionless)"
    legend_constants[46] = "V_rel_ratio in component intracellular_calcium_concentration (dimensionless)"
    legend_constants[47] = "V_e_ratio in component intracellular_calcium_concentration (dimensionless)"
    legend_constants[48] = "V_up_ratio in component intracellular_calcium_concentration (dimensionless)"
    legend_rates[0] = "d/dt V in component membrane (millivolt)"
    legend_rates[3] = "d/dt m in component fast_sodium_current_m_gate (dimensionless)"
    legend_rates[4] = "d/dt h in component fast_sodium_current_h_gate (dimensionless)"
    legend_rates[5] = "d/dt r in component transient_outward_current_r_gate (dimensionless)"
    legend_rates[6] = "d/dt s in component transient_outward_current_s_gate (dimensionless)"
    legend_rates[8] = "d/dt d in component L_type_calcium_current_d_gate (dimensionless)"
    legend_rates[9] = "d/dt f_Ca in component L_type_calcium_current_f_Ca_gate (dimensionless)"
    legend_rates[11] = "d/dt ActFrac in component calcium_release (dimensionless)"
    legend_rates[12] = "d/dt ProdFrac in component calcium_release (dimensionless)"
    legend_rates[1] = "d/dt Na_i in component intracellular_sodium_concentration (millimolar)"
    legend_rates[2] = "d/dt K_i in component intracellular_potassium_concentration (millimolar)"
    legend_rates[7] = "d/dt Ca_i in component intracellular_calcium_concentration (millimolar)"
    legend_rates[14] = "d/dt Ca_Calmod in component intracellular_calcium_concentration (millimolar)"
    legend_rates[15] = "d/dt Ca_Trop in component intracellular_calcium_concentration (millimolar)"
    legend_rates[10] = "d/dt Ca_up in component intracellular_calcium_concentration (millimolar)"
    legend_rates[13] = "d/dt Ca_rel in component intracellular_calcium_concentration (millimolar)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = -91.6
    constants[0] = 8314.472
    constants[1] = 310
    constants[2] = 96485.3415
    constants[3] = 4e-5
    constants[4] = 0.1
    constants[5] = 100000
    constants[6] = 1
    constants[7] = 0.002
    constants[8] = -1.3
    constants[9] = 0.5
    constants[10] = 140
    states[1] = 6.48
    constants[11] = 4
    states[2] = 140
    states[3] = 0.076
    states[4] = 0.015
    constants[12] = 1e-5
    constants[13] = 0.01
    constants[14] = 0
    states[5] = 0
    states[6] = 1
    constants[15] = 0.14
    constants[16] = 1
    constants[17] = 40
    constants[18] = 0.00012
    constants[19] = 5e-5
    constants[20] = 2
    states[7] = 1e-5
    constants[21] = 0.0001
    constants[22] = 3
    constants[23] = 0.0001
    constants[24] = 0.5
    constants[25] = 0.0017
    constants[26] = 0.017
    constants[27] = 10
    constants[28] = 0.05
    states[8] = 0.0011
    states[9] = 0.785
    constants[29] = 0.0003
    constants[30] = 0.4
    constants[31] = 0.5
    constants[32] = 3
    constants[33] = 0.23
    states[10] = 0.3
    constants[34] = 0
    constants[35] = 250
    states[11] = 0
    states[12] = 0
    constants[36] = 1
    states[13] = 0.3
    constants[37] = 50
    states[14] = 0.0005
    states[15] = 0.0015
    constants[38] = 0.02
    constants[39] = 0.15
    constants[40] = 100000
    constants[41] = 50
    constants[42] = 100000
    constants[43] = 200
    constants[44] = 0.01
    constants[45] = 0.08
    constants[46] = 0.1
    constants[47] = 0.4
    constants[48] = 0.01
    constants[49] = (constants[0]*constants[1])/constants[2]
    constants[50] = 3.14159*(power(constants[44], 2.00000))*constants[45]
    constants[51] = (constants[29]*constants[30])/constants[31]
    constants[52] = ((1.00000-constants[47])-constants[48])-constants[46]
    constants[53] = constants[50]*constants[52]
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[5] = 333.000*(1.00000/(1.00000+exp(-(states[0]+4.00000)/5.00000))-states[5])
    algebraic[1] = 20.0000*exp(-0.125000*(states[0]+75.0000))
    algebraic[7] = 2000.00/(1.00000+320.000*exp(-0.100000*(states[0]+75.0000)))
    rates[4] = algebraic[1]*(1.00000-states[4])-algebraic[7]*states[4]
    algebraic[2] = 0.0330000*exp(-states[0]/17.0000)
    algebraic[8] = 33.0000/(1.00000+exp(-0.125000*(states[0]+10.0000)))
    rates[6] = algebraic[2]*(1.00000-states[6])-algebraic[8]*states[6]
    algebraic[0] = states[0]+41.0000
    algebraic[6] = custom_piecewise([less(fabs(algebraic[0]) , constants[12]), 2000.00 , True, (200.000*algebraic[0])/(1.00000-exp(-0.100000*algebraic[0]))])
    algebraic[12] = 8000.00*exp(-0.0560000*(states[0]+66.0000))
    rates[3] = algebraic[6]*(1.00000-states[3])-algebraic[12]*states[3]
    algebraic[3] = states[0]+19.0000
    algebraic[9] = custom_piecewise([less(fabs(algebraic[3]) , 0.000100000), 120.000 , True, (30.0000*algebraic[3])/(1.00000-exp(-algebraic[3]/4.00000))])
    algebraic[13] = custom_piecewise([less(fabs(algebraic[3]) , 0.000100000), 120.000 , True, (12.0000*algebraic[3])/(exp(algebraic[3]/10.0000)-1.00000)])
    rates[8] = algebraic[9]*(1.00000-states[8])-algebraic[13]*states[8]
    algebraic[11] = exp(0.0800000*(states[0]-40.0000))
    algebraic[15] = power(states[7]/(states[7]+0.000500000), 2.00000)
    algebraic[17] = 600.000*algebraic[11]+500.000*algebraic[15]
    algebraic[19] = 60.0000+500.000*algebraic[15]
    algebraic[5] = (1.00000-states[11])-states[12]
    rates[11] = algebraic[5]*algebraic[17]-states[11]*algebraic[19]
    rates[12] = states[11]*algebraic[19]-constants[36]*states[12]
    algebraic[28] = states[0]+34.0000
    algebraic[29] = custom_piecewise([less(fabs(algebraic[28]) , 0.000100000), 25.0000 , True, (6.25000*algebraic[28])/(exp(algebraic[28]/4.00000)-1.00000)])
    algebraic[30] = 12.0000/(1.00000+exp(-algebraic[28]/4.00000))
    algebraic[31] = states[7]/(0.00100000+states[7])
    rates[9] = (120.000*(1.00000-states[9])*algebraic[31]+(1.00000-states[9])*(1.00000-algebraic[31]))*algebraic[30]-algebraic[29]*states[9]
    algebraic[16] = constants[49]*log(constants[11]/states[2])
    algebraic[26] = constants[25]*(states[0]-algebraic[16])
    algebraic[27] = (((constants[26]*constants[11])/(constants[11]+constants[27]))*(states[0]-algebraic[16]))/(1.00000+exp((((states[0]-algebraic[16])-10.0000)*2.00000)/constants[49]))
    algebraic[18] = constants[13]*(constants[14]+states[6]*(1.00000-constants[14]))*states[5]*(states[0]-algebraic[16])
    algebraic[20] = (((constants[15]*constants[11])/(constants[16]+constants[11]))*states[1])/(constants[17]+states[1])
    algebraic[32] = (1.00000-states[9])*(1.00000-algebraic[31])
    algebraic[34] = (((0.00200000*constants[28]*states[8]*algebraic[32]*(states[0]-50.0000))/constants[49])/(1.00000-exp(-(states[0]-50.0000)/constants[49])))*(states[2]*exp(50.0000/constants[49])-constants[11]*exp(-(states[0]-50.0000)/constants[49]))
    rates[2] = (-1.00000/(1.00000*constants[53]*constants[2]))*((algebraic[27]+algebraic[34]+algebraic[18]+algebraic[26])-2.00000*algebraic[20])
    algebraic[21] = constants[49]*log(constants[10]/states[1])
    algebraic[22] = constants[18]*(states[0]-algebraic[21])
    algebraic[25] = (constants[21]*(exp((constants[24]*(constants[22]-2.00000)*states[0])/constants[49])*(power(states[1], constants[22]))*constants[20]-exp(((constants[24]-1.00000)*(constants[22]-2.00000)*states[0])/constants[49])*(power(constants[10], constants[22]))*states[7]))/((1.00000+constants[23]*(states[7]*(power(constants[10], constants[22]))+constants[20]*(power(states[1], constants[22]))))*(1.00000+states[7]/0.00690000))
    algebraic[10] = constants[49]*log((constants[10]+0.120000*constants[11])/(states[1]+0.120000*states[2]))
    algebraic[14] = constants[9]*(power(states[3], 3.00000))*states[4]*(states[0]-algebraic[10])
    algebraic[36] = (((0.0100000*constants[28]*states[8]*algebraic[32]*(states[0]-50.0000))/constants[49])/(1.00000-exp(-(states[0]-50.0000)/constants[49])))*(states[1]*exp(50.0000/constants[49])-constants[10]*exp(-(states[0]-50.0000)/constants[49]))
    rates[1] = (-1.00000/(1.00000*constants[53]*constants[2]))*(algebraic[14]+algebraic[22]+3.00000*algebraic[20]+3.00000*algebraic[25]+algebraic[36])
    algebraic[23] = 0.500000*constants[49]*log(constants[20]/states[7])
    algebraic[24] = constants[19]*(states[0]-algebraic[23])
    algebraic[33] = (((4.00000*constants[28]*states[8]*algebraic[32]*(states[0]-50.0000))/constants[49])/(1.00000-exp((-(states[0]-50.0000)*2.00000)/constants[49])))*(states[7]*exp(100.000/constants[49])-constants[20]*exp((-(states[0]-50.0000)*2.00000)/constants[49]))
    algebraic[38] = algebraic[33]+algebraic[34]+algebraic[36]
    algebraic[4] = custom_piecewise([greater_equal(voi , constants[4]) & less_equal(voi , constants[5]) & less_equal((voi-constants[4])-floor((voi-constants[4])/constants[6])*constants[6] , constants[7]), constants[8] , True, 0.00000])
    rates[0] = (-1.00000/constants[3])*(algebraic[4]+algebraic[26]+algebraic[27]+algebraic[18]+algebraic[22]+algebraic[24]+algebraic[20]+algebraic[25]+algebraic[14]+algebraic[38])
    rates[14] = constants[40]*states[7]*(constants[38]-states[14])-constants[41]*states[14]
    rates[15] = constants[42]*states[7]*(constants[39]-states[15])-constants[43]*states[15]
    algebraic[35] = states[7]+states[10]*constants[51]+constants[29]*constants[30]+constants[29]
    algebraic[37] = (states[7]/algebraic[35])*constants[32]-((states[10]*constants[51])/algebraic[35])*constants[33]
    algebraic[40] = (states[10]-states[13])*constants[37]
    rates[10] = (constants[52]/constants[48])*algebraic[37]-algebraic[40]
    algebraic[39] = ((power(states[11]/(states[11]+0.250000), 2.00000))*constants[35]+constants[34])*states[13]
    rates[13] = (constants[48]/constants[46])*algebraic[40]-algebraic[39]
    rates[7] = ((((-1.00000/(2.00000*1.00000*constants[53]*constants[2]))*((algebraic[33]+algebraic[24])-2.00000*algebraic[25])+(algebraic[39]*constants[46])/constants[52])-rates[14])-rates[15])-algebraic[37]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[1] = 20.0000*exp(-0.125000*(states[0]+75.0000))
    algebraic[7] = 2000.00/(1.00000+320.000*exp(-0.100000*(states[0]+75.0000)))
    algebraic[2] = 0.0330000*exp(-states[0]/17.0000)
    algebraic[8] = 33.0000/(1.00000+exp(-0.125000*(states[0]+10.0000)))
    algebraic[0] = states[0]+41.0000
    algebraic[6] = custom_piecewise([less(fabs(algebraic[0]) , constants[12]), 2000.00 , True, (200.000*algebraic[0])/(1.00000-exp(-0.100000*algebraic[0]))])
    algebraic[12] = 8000.00*exp(-0.0560000*(states[0]+66.0000))
    algebraic[3] = states[0]+19.0000
    algebraic[9] = custom_piecewise([less(fabs(algebraic[3]) , 0.000100000), 120.000 , True, (30.0000*algebraic[3])/(1.00000-exp(-algebraic[3]/4.00000))])
    algebraic[13] = custom_piecewise([less(fabs(algebraic[3]) , 0.000100000), 120.000 , True, (12.0000*algebraic[3])/(exp(algebraic[3]/10.0000)-1.00000)])
    algebraic[11] = exp(0.0800000*(states[0]-40.0000))
    algebraic[15] = power(states[7]/(states[7]+0.000500000), 2.00000)
    algebraic[17] = 600.000*algebraic[11]+500.000*algebraic[15]
    algebraic[19] = 60.0000+500.000*algebraic[15]
    algebraic[5] = (1.00000-states[11])-states[12]
    algebraic[28] = states[0]+34.0000
    algebraic[29] = custom_piecewise([less(fabs(algebraic[28]) , 0.000100000), 25.0000 , True, (6.25000*algebraic[28])/(exp(algebraic[28]/4.00000)-1.00000)])
    algebraic[30] = 12.0000/(1.00000+exp(-algebraic[28]/4.00000))
    algebraic[31] = states[7]/(0.00100000+states[7])
    algebraic[16] = constants[49]*log(constants[11]/states[2])
    algebraic[26] = constants[25]*(states[0]-algebraic[16])
    algebraic[27] = (((constants[26]*constants[11])/(constants[11]+constants[27]))*(states[0]-algebraic[16]))/(1.00000+exp((((states[0]-algebraic[16])-10.0000)*2.00000)/constants[49]))
    algebraic[18] = constants[13]*(constants[14]+states[6]*(1.00000-constants[14]))*states[5]*(states[0]-algebraic[16])
    algebraic[20] = (((constants[15]*constants[11])/(constants[16]+constants[11]))*states[1])/(constants[17]+states[1])
    algebraic[32] = (1.00000-states[9])*(1.00000-algebraic[31])
    algebraic[34] = (((0.00200000*constants[28]*states[8]*algebraic[32]*(states[0]-50.0000))/constants[49])/(1.00000-exp(-(states[0]-50.0000)/constants[49])))*(states[2]*exp(50.0000/constants[49])-constants[11]*exp(-(states[0]-50.0000)/constants[49]))
    algebraic[21] = constants[49]*log(constants[10]/states[1])
    algebraic[22] = constants[18]*(states[0]-algebraic[21])
    algebraic[25] = (constants[21]*(exp((constants[24]*(constants[22]-2.00000)*states[0])/constants[49])*(power(states[1], constants[22]))*constants[20]-exp(((constants[24]-1.00000)*(constants[22]-2.00000)*states[0])/constants[49])*(power(constants[10], constants[22]))*states[7]))/((1.00000+constants[23]*(states[7]*(power(constants[10], constants[22]))+constants[20]*(power(states[1], constants[22]))))*(1.00000+states[7]/0.00690000))
    algebraic[10] = constants[49]*log((constants[10]+0.120000*constants[11])/(states[1]+0.120000*states[2]))
    algebraic[14] = constants[9]*(power(states[3], 3.00000))*states[4]*(states[0]-algebraic[10])
    algebraic[36] = (((0.0100000*constants[28]*states[8]*algebraic[32]*(states[0]-50.0000))/constants[49])/(1.00000-exp(-(states[0]-50.0000)/constants[49])))*(states[1]*exp(50.0000/constants[49])-constants[10]*exp(-(states[0]-50.0000)/constants[49]))
    algebraic[23] = 0.500000*constants[49]*log(constants[20]/states[7])
    algebraic[24] = constants[19]*(states[0]-algebraic[23])
    algebraic[33] = (((4.00000*constants[28]*states[8]*algebraic[32]*(states[0]-50.0000))/constants[49])/(1.00000-exp((-(states[0]-50.0000)*2.00000)/constants[49])))*(states[7]*exp(100.000/constants[49])-constants[20]*exp((-(states[0]-50.0000)*2.00000)/constants[49]))
    algebraic[38] = algebraic[33]+algebraic[34]+algebraic[36]
    algebraic[4] = custom_piecewise([greater_equal(voi , constants[4]) & less_equal(voi , constants[5]) & less_equal((voi-constants[4])-floor((voi-constants[4])/constants[6])*constants[6] , constants[7]), constants[8] , True, 0.00000])
    algebraic[35] = states[7]+states[10]*constants[51]+constants[29]*constants[30]+constants[29]
    algebraic[37] = (states[7]/algebraic[35])*constants[32]-((states[10]*constants[51])/algebraic[35])*constants[33]
    algebraic[40] = (states[10]-states[13])*constants[37]
    algebraic[39] = ((power(states[11]/(states[11]+0.250000), 2.00000))*constants[35]+constants[34])*states[13]
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
        self.R = 8314.472
        self.T = 310
        self.F = 96485.3415
        self.C_m = 4e-5
        self.stim_start = 0.1
        self.stim_end = 100000
        self.stim_period = 1
        self.stim_duration = 0.002
        self.stim_amplitude = -1.3
        self.g_Na = 0.5
        self.Na_o = 140
        self.K_c = 4
        self.delta_m = 1e-5
        self.g_to = 0.01
        self.g_to_s = 0
        self.i_NaK_max = 0.14
        self.K_mK = 1
        self.K_mNa = 40
        self.g_b_Na = 0.00012
        self.g_b_Ca = 5e-5
        self.Ca_o = 2
        self.k_NaCa = 0.0001
        self.n_NaCa = 3
        self.d_NaCa = 0.0001
        self.gamma = 0.5
        self.g_b_K = 0.0017
        self.g_K1 = 0.017
        self.K_m_K1 = 10
        self.P_Ca_L = 0.05
        self.K_cyca = 0.0003
        self.K_xcs = 0.4
        self.K_srca = 0.5
        self.alpha_up = 3
        self.beta_up = 0.23
        self.K_leak_rate = 0
        self.K_m_rel = 250
        self.ProdFracRate = 1
        self.alpha_tr = 50
        self.Calmod = 0.02
        self.Trop = 0.15
        self.alpha_Calmod = 100000
        self.beta_Calmod = 50
        self.alpha_Trop = 100000
        self.beta_Trop = 200
        self.radius = 0.01
        self.length = 0.08
        self.V_rel_ratio = 0.1
        self.V_e_ratio = 0.4
        self.V_up_ratio = 0.01

    def to_dict(self):
        return {
            "R": self.R,
            "T": self.T,
            "F": self.F,
            "C_m": self.C_m,
            "stim_start": self.stim_start,
            "stim_end": self.stim_end,
            "stim_period": self.stim_period,
            "stim_duration": self.stim_duration,
            "stim_amplitude": self.stim_amplitude,
            "g_Na": self.g_Na,
            "Na_o": self.Na_o,
            "K_c": self.K_c,
            "delta_m": self.delta_m,
            "g_to": self.g_to,
            "g_to_s": self.g_to_s,
            "i_NaK_max": self.i_NaK_max,
            "K_mK": self.K_mK,
            "K_mNa": self.K_mNa,
            "g_b_Na": self.g_b_Na,
            "g_b_Ca": self.g_b_Ca,
            "Ca_o": self.Ca_o,
            "k_NaCa": self.k_NaCa,
            "n_NaCa": self.n_NaCa,
            "d_NaCa": self.d_NaCa,
            "gamma": self.gamma,
            "g_b_K": self.g_b_K,
            "g_K1": self.g_K1,
            "K_m_K1": self.K_m_K1,
            "P_Ca_L": self.P_Ca_L,
            "K_cyca": self.K_cyca,
            "K_xcs": self.K_xcs,
            "K_srca": self.K_srca,
            "alpha_up": self.alpha_up,
            "beta_up": self.beta_up,
            "K_leak_rate": self.K_leak_rate,
            "K_m_rel": self.K_m_rel,
            "ProdFracRate": self.ProdFracRate,
            "alpha_tr": self.alpha_tr,
            "Calmod": self.Calmod,
            "Trop": self.Trop,
            "alpha_Calmod": self.alpha_Calmod,
            "beta_Calmod": self.beta_Calmod,
            "alpha_Trop": self.alpha_Trop,
            "beta_Trop": self.beta_Trop,
            "radius": self.radius,
            "length": self.length,
            "V_rel_ratio": self.V_rel_ratio,
            "V_e_ratio": self.V_e_ratio,
            "V_up_ratio": self.V_up_ratio,
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
        y0=[-91.6, 6.48, 140, 0.076, 0.015, 0, 1, 1e-5, 0.0011, 0.785, 0.3, 0, 0, 0.3, 0.0005, 0.0015],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "earm_noble_1990"
        self.curve_names = [
            "V",
            "Na_i",
            "K_i",
            "m",
            "h",
            "r",
            "s",
            "Ca_i",
            "d",
            "f_Ca",
            "Ca_up",
            "ActFrac",
            "ProdFrac",
            "Ca_rel",
            "Ca_Calmod",
            "Ca_Trop",
        ]
        self.state_names = ['V', 'Na_i', 'K_i', 'm', 'h', 'r', 's', 'Ca_i', 'd', 'f_Ca', 'Ca_up', 'ActFrac', 'ProdFrac', 'Ca_rel', 'Ca_Calmod', 'Ca_Trop']
        self.algebraic_names = ['E0_m', 'alpha_h', 'alpha_s', 'E0_d', 'i_Stim', 'PrecFrac', 'alpha_m', 'beta_h', 'beta_s', 'alpha_d', 'E_mh', 'VoltDep', 'beta_m', 'beta_d', 'i_Na', 'RegBindSite', 'E_K', 'ActRate', 'i_to', 'InactRate', 'i_NaK', 'E_Na', 'i_b_Na', 'E_Ca', 'i_b_Ca', 'i_NaCa', 'i_b_K', 'i_K1', 'E0_f', 'alpha_f_Ca', 'beta_f_Ca', 'CaChoff', 'CaChon', 'i_Ca_L_Ca', 'i_Ca_L_K', 'K_2', 'i_Ca_L_Na', 'i_up', 'i_Ca_L', 'i_rel', 'i_trans']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 54
        p = self.params

        # direct mapping
        c[0] = p.R
        c[1] = p.T
        c[2] = p.F
        c[3] = p.C_m
        c[4] = p.stim_start
        c[5] = p.stim_end
        c[6] = p.stim_period
        c[7] = p.stim_duration
        c[8] = p.stim_amplitude
        c[9] = p.g_Na
        c[10] = p.Na_o
        c[11] = p.K_c
        c[12] = p.delta_m
        c[13] = p.g_to
        c[14] = p.g_to_s
        c[15] = p.i_NaK_max
        c[16] = p.K_mK
        c[17] = p.K_mNa
        c[18] = p.g_b_Na
        c[19] = p.g_b_Ca
        c[20] = p.Ca_o
        c[21] = p.k_NaCa
        c[22] = p.n_NaCa
        c[23] = p.d_NaCa
        c[24] = p.gamma
        c[25] = p.g_b_K
        c[26] = p.g_K1
        c[27] = p.K_m_K1
        c[28] = p.P_Ca_L
        c[29] = p.K_cyca
        c[30] = p.K_xcs
        c[31] = p.K_srca
        c[32] = p.alpha_up
        c[33] = p.beta_up
        c[34] = p.K_leak_rate
        c[35] = p.K_m_rel
        c[36] = p.ProdFracRate
        c[37] = p.alpha_tr
        c[38] = p.Calmod
        c[39] = p.Trop
        c[40] = p.alpha_Calmod
        c[41] = p.beta_Calmod
        c[42] = p.alpha_Trop
        c[43] = p.beta_Trop
        c[44] = p.radius
        c[45] = p.length
        c[46] = p.V_rel_ratio
        c[47] = p.V_e_ratio
        c[48] = p.V_up_ratio

        # derived constants
        c[49] = (c[0]*c[1])/c[2]
        c[50] = 3.14159*(power(c[44], 2.00000))*c[45]
        c[51] = (c[29]*c[30])/c[31]
        c[52] = ((1.00000-c[47])-c[48])-c[46]
        c[53] = c[50]*c[52]

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
