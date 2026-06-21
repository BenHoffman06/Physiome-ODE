# Size of variable arrays:
sizeAlgebraic = 42
sizeStates = 14
sizeConstants = 44
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
    legend_constants[3] = "C in component membrane (microF)"
    legend_constants[39] = "RTONF in component membrane (millivolt)"
    legend_algebraic[23] = "i_f in component hyperpolarising_activated_current (nanoA)"
    legend_algebraic[25] = "i_K in component time_dependent_potassium_current (nanoA)"
    legend_algebraic[26] = "i_K1 in component time_independent_potassium_current (nanoA)"
    legend_algebraic[27] = "i_Na_b in component sodium_background_current (nanoA)"
    legend_algebraic[29] = "i_Ca_b in component calcium_background_current (nanoA)"
    legend_algebraic[30] = "i_p in component sodium_potassium_pump (nanoA)"
    legend_algebraic[31] = "i_NaCa in component Na_Ca_exchanger (nanoA)"
    legend_algebraic[33] = "i_Na in component fast_sodium_current (nanoA)"
    legend_algebraic[40] = "i_si in component second_inward_current (nanoA)"
    legend_algebraic[20] = "i_fNa in component hyperpolarising_activated_current (nanoA)"
    legend_algebraic[0] = "E_Na in component hyperpolarising_activated_current (millivolt)"
    legend_algebraic[9] = "E_K in component hyperpolarising_activated_current (millivolt)"
    legend_algebraic[22] = "i_fK in component hyperpolarising_activated_current (nanoA)"
    legend_constants[4] = "g_f_Na in component hyperpolarising_activated_current (microS)"
    legend_constants[5] = "g_f_K in component hyperpolarising_activated_current (microS)"
    legend_constants[6] = "Km_f in component hyperpolarising_activated_current (millimolar)"
    legend_constants[7] = "Kc in component extracellular_potassium_concentration (millimolar)"
    legend_states[1] = "Ki in component intracellular_potassium_concentration (millimolar)"
    legend_states[2] = "Nai in component intracellular_sodium_concentration (millimolar)"
    legend_constants[8] = "Nao in component extracellular_sodium_concentration (millimolar)"
    legend_states[3] = "y in component hyperpolarising_activated_current_y_gate (dimensionless)"
    legend_algebraic[1] = "alpha_y in component hyperpolarising_activated_current_y_gate (per_second)"
    legend_algebraic[10] = "beta_y in component hyperpolarising_activated_current_y_gate (per_second)"
    legend_constants[9] = "speed_y in component hyperpolarising_activated_current_y_gate (dimensionless)"
    legend_algebraic[24] = "I_K in component time_dependent_potassium_current (nanoA)"
    legend_constants[10] = "i_K_max in component time_dependent_potassium_current (nanoA)"
    legend_states[4] = "x in component time_dependent_potassium_current_x_gate (dimensionless)"
    legend_algebraic[2] = "alpha_x in component time_dependent_potassium_current_x_gate (per_second)"
    legend_algebraic[11] = "beta_x in component time_dependent_potassium_current_x_gate (per_second)"
    legend_constants[11] = "g_K1 in component time_independent_potassium_current (microS)"
    legend_constants[12] = "Km_K1 in component time_independent_potassium_current (millimolar)"
    legend_constants[13] = "g_Nab in component sodium_background_current (microS)"
    legend_algebraic[28] = "E_Ca in component calcium_background_current (millivolt)"
    legend_constants[14] = "g_Cab in component calcium_background_current (microS)"
    legend_states[5] = "Cai in component intracellular_calcium_concentration (millimolar)"
    legend_constants[15] = "Cao in component extracellular_calcium_concentration (millimolar)"
    legend_constants[16] = "I_p in component sodium_potassium_pump (nanoA)"
    legend_constants[17] = "K_mK in component sodium_potassium_pump (millimolar)"
    legend_constants[18] = "K_mNa in component sodium_potassium_pump (millimolar)"
    legend_constants[19] = "n_NaCa in component Na_Ca_exchanger (dimensionless)"
    legend_constants[20] = "K_NaCa in component Na_Ca_exchanger (nanoA)"
    legend_constants[21] = "d_NaCa in component Na_Ca_exchanger (dimensionless)"
    legend_constants[22] = "gamma in component Na_Ca_exchanger (dimensionless)"
    legend_constants[23] = "g_Na in component fast_sodium_current (microS)"
    legend_algebraic[32] = "E_mh in component fast_sodium_current (millivolt)"
    legend_states[6] = "m in component fast_sodium_current_m_gate (dimensionless)"
    legend_states[7] = "h in component fast_sodium_current_h_gate (dimensionless)"
    legend_algebraic[12] = "alpha_m in component fast_sodium_current_m_gate (per_second)"
    legend_algebraic[17] = "beta_m in component fast_sodium_current_m_gate (per_second)"
    legend_constants[24] = "delta_m in component fast_sodium_current_m_gate (millivolt)"
    legend_algebraic[3] = "E0_m in component fast_sodium_current_m_gate (millivolt)"
    legend_algebraic[4] = "alpha_h in component fast_sodium_current_h_gate (per_second)"
    legend_algebraic[13] = "beta_h in component fast_sodium_current_h_gate (per_second)"
    legend_algebraic[34] = "i_siCa in component second_inward_current (nanoA)"
    legend_algebraic[35] = "i_siK in component second_inward_current (nanoA)"
    legend_algebraic[37] = "i_siNa in component second_inward_current (nanoA)"
    legend_constants[25] = "P_si in component second_inward_current (nanoA_per_millimolar)"
    legend_states[8] = "d in component second_inward_current_d_gate (dimensionless)"
    legend_states[9] = "f in component second_inward_current_f_gate (dimensionless)"
    legend_states[10] = "f2 in component second_inward_current_f2_gate (dimensionless)"
    legend_algebraic[14] = "alpha_d in component second_inward_current_d_gate (per_second)"
    legend_algebraic[18] = "beta_d in component second_inward_current_d_gate (per_second)"
    legend_constants[26] = "delta_d in component second_inward_current_d_gate (millivolt)"
    legend_algebraic[5] = "E0_d in component second_inward_current_d_gate (millivolt)"
    legend_algebraic[15] = "alpha_f in component second_inward_current_f_gate (per_second)"
    legend_algebraic[19] = "beta_f in component second_inward_current_f_gate (per_second)"
    legend_constants[27] = "delta_f in component second_inward_current_f_gate (millivolt)"
    legend_algebraic[6] = "E0_f in component second_inward_current_f_gate (millivolt)"
    legend_constants[28] = "alpha_f2 in component second_inward_current_f2_gate (per_second)"
    legend_algebraic[7] = "beta_f2 in component second_inward_current_f2_gate (per_second)"
    legend_constants[29] = "K_mf2 in component second_inward_current_f2_gate (millimolar)"
    legend_constants[30] = "radius in component intracellular_sodium_concentration (millimetre)"
    legend_constants[31] = "length in component intracellular_sodium_concentration (millimetre)"
    legend_constants[32] = "V_e_ratio in component intracellular_sodium_concentration (dimensionless)"
    legend_constants[40] = "V_Cell in component intracellular_sodium_concentration (millimetre3)"
    legend_constants[41] = "Vi in component intracellular_sodium_concentration (millimetre3)"
    legend_constants[42] = "V_up in component intracellular_calcium_concentration (millimetre3)"
    legend_constants[43] = "V_rel in component intracellular_calcium_concentration (millimetre3)"
    legend_algebraic[36] = "i_up in component intracellular_calcium_concentration (nanoA)"
    legend_algebraic[38] = "i_tr in component intracellular_calcium_concentration (nanoA)"
    legend_algebraic[41] = "i_rel in component intracellular_calcium_concentration (nanoA)"
    legend_states[11] = "Ca_up in component intracellular_calcium_concentration (millimolar)"
    legend_states[12] = "Ca_rel in component intracellular_calcium_concentration (millimolar)"
    legend_constants[33] = "Ca_up_max in component intracellular_calcium_concentration (millimolar)"
    legend_constants[34] = "K_mCa in component intracellular_calcium_concentration (millimolar)"
    legend_states[13] = "p in component intracellular_calcium_concentration (dimensionless)"
    legend_algebraic[16] = "alpha_p in component intracellular_calcium_concentration (per_second)"
    legend_algebraic[21] = "beta_p in component intracellular_calcium_concentration (per_second)"
    legend_algebraic[8] = "E0_p in component intracellular_calcium_concentration (millivolt)"
    legend_constants[35] = "tau_up in component intracellular_calcium_concentration (second)"
    legend_constants[36] = "tau_rep in component intracellular_calcium_concentration (second)"
    legend_constants[37] = "tau_rel in component intracellular_calcium_concentration (second)"
    legend_constants[38] = "rCa in component intracellular_calcium_concentration (dimensionless)"
    legend_algebraic[39] = "i_mK in component intracellular_potassium_concentration (nanoA)"
    legend_rates[0] = "d/dt V in component membrane (millivolt)"
    legend_rates[3] = "d/dt y in component hyperpolarising_activated_current_y_gate (dimensionless)"
    legend_rates[4] = "d/dt x in component time_dependent_potassium_current_x_gate (dimensionless)"
    legend_rates[6] = "d/dt m in component fast_sodium_current_m_gate (dimensionless)"
    legend_rates[7] = "d/dt h in component fast_sodium_current_h_gate (dimensionless)"
    legend_rates[8] = "d/dt d in component second_inward_current_d_gate (dimensionless)"
    legend_rates[9] = "d/dt f in component second_inward_current_f_gate (dimensionless)"
    legend_rates[10] = "d/dt f2 in component second_inward_current_f2_gate (dimensionless)"
    legend_rates[2] = "d/dt Nai in component intracellular_sodium_concentration (millimolar)"
    legend_rates[13] = "d/dt p in component intracellular_calcium_concentration (dimensionless)"
    legend_rates[11] = "d/dt Ca_up in component intracellular_calcium_concentration (millimolar)"
    legend_rates[12] = "d/dt Ca_rel in component intracellular_calcium_concentration (millimolar)"
    legend_rates[5] = "d/dt Cai in component intracellular_calcium_concentration (millimolar)"
    legend_rates[1] = "d/dt Ki in component intracellular_potassium_concentration (millimolar)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = -67.797059970601
    constants[0] = 8314.472
    constants[1] = 310
    constants[2] = 96485.3415
    constants[3] = 6e-5
    constants[4] = 0.06
    constants[5] = 0.06
    constants[6] = 45
    constants[7] = 3
    states[1] = 139.859968229045
    states[2] = 7.51007221193712
    constants[8] = 140
    states[3] = 0.0743464067197738
    constants[9] = 2
    constants[10] = 0.8
    states[4] = 0.129303443591363
    constants[11] = 0.0075
    constants[12] = 10
    constants[13] = 0.0007
    constants[14] = 0.0001
    states[5] = 5.84191784887783e-5
    constants[15] = 2
    constants[16] = 0.45
    constants[17] = 1
    constants[18] = 40
    constants[19] = 3
    constants[20] = 2e-5
    constants[21] = 0.0001
    constants[22] = 0.5
    constants[23] = 0.0125
    states[6] = 0.042697621819783
    states[7] = 0.138105285882671
    constants[24] = 1e-5
    constants[25] = 0.12
    states[8] = 1.26333192869164e-5
    states[9] = 0.999507224159629
    states[10] = 0.485471180273736
    constants[26] = 0.0001
    constants[27] = 0.0001
    constants[28] = 10
    constants[29] = 0.0005
    constants[30] = 0.008
    constants[31] = 0.11
    constants[32] = 0.1
    states[11] = 3.70806465918854
    states[12] = 0.177741556496929
    constants[33] = 5
    constants[34] = 0.002
    states[13] = 0.176207580044253
    constants[35] = 0.005
    constants[36] = 0.2
    constants[37] = 0.01
    constants[38] = 2
    constants[39] = (constants[0]*constants[1])/constants[2]
    constants[40] = 3.14159*(power(constants[30], 2.00000))*constants[31]
    constants[41] = constants[40]*(1.00000-constants[32])
    constants[42] = constants[41]*0.0500000
    constants[43] = constants[41]*0.0200000
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[7] = (states[5]*constants[28])/constants[29]
    rates[10] = constants[28]-states[10]*(constants[28]+algebraic[7])
    algebraic[1] = 0.0140000*exp(-states[0]/16.0000)
    algebraic[10] = 9.75000*exp(states[0]/19.0000)
    rates[3] = constants[9]*(algebraic[1]*(1.00000-states[3])-algebraic[10]*states[3])
    algebraic[2] = 2.10000*exp(states[0]/28.0000)
    algebraic[11] = 0.960000*exp(-states[0]/24.0000)
    rates[4] = algebraic[2]*(1.00000-states[4])-algebraic[11]*states[4]
    algebraic[4] = 20.0000*exp(-0.125000*(states[0]+75.0000))
    algebraic[13] = 2000.00/(320.000*exp(-0.100000*(states[0]+75.0000))+1.00000)
    rates[7] = algebraic[4]*(1.00000-states[7])-algebraic[13]*states[7]
    algebraic[3] = states[0]+41.0000
    algebraic[12] = custom_piecewise([less(fabs(algebraic[3]) , constants[24]), 2000.00 , True, (200.000*algebraic[3])/(1.00000-exp(-0.100000*algebraic[3]))])
    algebraic[17] = 8000.00*exp(-0.0560000*(states[0]+66.0000))
    rates[6] = algebraic[12]*(1.00000-states[6])-algebraic[17]*states[6]
    algebraic[5] = (states[0]+24.0000)-5.00000
    algebraic[14] = custom_piecewise([less(fabs(algebraic[5]) , constants[26]), 120.000 , True, (30.0000*algebraic[5])/(1.00000-exp((-1.00000*algebraic[5])/4.00000))])
    algebraic[18] = custom_piecewise([less(fabs(algebraic[5]) , constants[26]), 120.000 , True, (12.0000*algebraic[5])/(exp(algebraic[5]/10.0000)-1.00000)])
    rates[8] = algebraic[14]*(1.00000-states[8])-algebraic[18]*states[8]
    algebraic[6] = states[0]+34.0000
    algebraic[15] = custom_piecewise([less(fabs(algebraic[6]) , constants[27]), 25.0000 , True, (6.25000*algebraic[6])/(exp(algebraic[6]/4.00000)-1.00000)])
    algebraic[19] = 50.0000/(1.00000+exp((-1.00000*(states[0]+34.0000))/4.00000))
    rates[9] = algebraic[15]*(1.00000-states[9])-algebraic[19]*states[9]
    algebraic[8] = (states[0]+34.0000)--30.0000
    algebraic[16] = (0.625000*algebraic[8])/(exp(algebraic[8]/4.00000)-1.00000)
    algebraic[21] = 5.00000/(1.00000+exp((-1.00000*algebraic[8])/4.00000))
    rates[13] = algebraic[16]*(1.00000-states[13])-algebraic[21]*states[13]
    algebraic[0] = constants[39]*log(constants[8]/states[2])
    algebraic[27] = constants[13]*(states[0]-algebraic[0])
    algebraic[30] = (((constants[16]*constants[7])/(constants[17]+constants[7]))*states[2])/(constants[18]+states[2])
    algebraic[31] = (constants[20]*(exp((constants[22]*(constants[19]-2.00000)*states[0])/constants[39])*(power(states[2], constants[19]))*constants[15]-exp(((constants[22]-1.00000)*(constants[19]-2.00000)*states[0])/constants[39])*(power(constants[8], constants[19]))*states[5]))/((1.00000+constants[21]*(states[5]*(power(constants[8], constants[19]))+constants[15]*(power(states[2], constants[19]))))*(1.00000+states[5]/0.00690000))
    algebraic[32] = constants[39]*log((constants[8]+0.120000*constants[7])/(states[2]+0.120000*states[1]))
    algebraic[33] = constants[23]*(power(states[6], 3.00000))*states[7]*(states[0]-algebraic[32])
    algebraic[20] = (((power(states[3], 2.00000))*constants[7])/(constants[7]+constants[6]))*constants[4]*(states[0]-algebraic[0])
    algebraic[37] = ((0.0100000*constants[25]*(states[0]-50.0000))/(constants[39]*(1.00000-exp((-1.00000*(states[0]-50.0000))/constants[39]))))*(states[2]*exp(50.0000/constants[39])-constants[8]*exp((-1.00000*(states[0]-50.0000))/constants[39]))*states[8]*states[9]*states[10]
    rates[2] = (-1.00000*(algebraic[33]+algebraic[27]+algebraic[20]+algebraic[37]+algebraic[30]*3.00000+(algebraic[31]*constants[19])/(constants[19]-2.00000)))/(1.00000*constants[41]*constants[2])
    algebraic[36] = ((2.00000*1.00000*constants[41]*constants[2])/(1.00000*constants[35]*constants[33]))*states[5]*(constants[33]-states[11])
    algebraic[38] = ((2.00000*1.00000*constants[43]*constants[2])/(1.00000*constants[36]))*states[13]*(states[11]-states[12])
    rates[11] = (1.00000*(algebraic[36]-algebraic[38]))/(2.00000*1.00000*constants[42]*constants[2])
    algebraic[24] = (constants[10]*(states[1]-constants[7]*exp(-states[0]/constants[39])))/140.000
    algebraic[25] = states[4]*algebraic[24]
    algebraic[9] = constants[39]*log(constants[7]/states[1])
    algebraic[26] = (((constants[11]*constants[7])/(constants[7]+constants[12]))*(states[0]-algebraic[9]))/(1.00000+exp((((states[0]+10.0000)-algebraic[9])*2.00000)/constants[39]))
    algebraic[22] = (((power(states[3], 2.00000))*constants[7])/(constants[7]+constants[6]))*constants[5]*(states[0]-algebraic[9])
    algebraic[35] = ((0.0100000*constants[25]*(states[0]-50.0000))/(constants[39]*(1.00000-exp((-1.00000*(states[0]-50.0000))/constants[39]))))*(states[1]*exp(50.0000/constants[39])-constants[7]*exp((-1.00000*(states[0]-50.0000))/constants[39]))*states[8]*states[9]*states[10]
    algebraic[39] = (algebraic[26]+algebraic[25]+algebraic[22]+algebraic[35])-2.00000*algebraic[30]
    rates[1] = (-1.00000*algebraic[39])/(1.00000*constants[41]*constants[2])
    algebraic[23] = algebraic[20]+algebraic[22]
    algebraic[28] = 0.500000*constants[39]*log(constants[15]/states[5])
    algebraic[29] = constants[14]*(states[0]-algebraic[28])
    algebraic[34] = ((4.00000*constants[25]*(states[0]-50.0000))/(constants[39]*(1.00000-exp((-1.00000*(states[0]-50.0000)*2.00000)/constants[39]))))*(states[5]*exp(100.000/constants[39])-constants[15]*exp((-2.00000*(states[0]-50.0000))/constants[39]))*states[8]*states[9]*states[10]
    algebraic[40] = algebraic[34]+algebraic[35]+algebraic[37]
    rates[0] = -(algebraic[23]+algebraic[25]+algebraic[26]+algebraic[27]+algebraic[29]+algebraic[30]+algebraic[31]+algebraic[33]+algebraic[40])/constants[3]
    algebraic[41] = (((2.00000*1.00000*constants[43]*constants[2])/(1.00000*constants[37]))*states[12]*(power(states[5], constants[38])))/(power(states[5], constants[38])+power(constants[34], constants[38]))
    rates[12] = (1.00000*(algebraic[38]-algebraic[41]))/(2.00000*1.00000*constants[43]*constants[2])
    rates[5] = (-1.00000*((((algebraic[34]+algebraic[29])-(2.00000*algebraic[31])/(constants[19]-2.00000))-algebraic[41])+algebraic[36]))/(2.00000*1.00000*constants[41]*constants[2])
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[7] = (states[5]*constants[28])/constants[29]
    algebraic[1] = 0.0140000*exp(-states[0]/16.0000)
    algebraic[10] = 9.75000*exp(states[0]/19.0000)
    algebraic[2] = 2.10000*exp(states[0]/28.0000)
    algebraic[11] = 0.960000*exp(-states[0]/24.0000)
    algebraic[4] = 20.0000*exp(-0.125000*(states[0]+75.0000))
    algebraic[13] = 2000.00/(320.000*exp(-0.100000*(states[0]+75.0000))+1.00000)
    algebraic[3] = states[0]+41.0000
    algebraic[12] = custom_piecewise([less(fabs(algebraic[3]) , constants[24]), 2000.00 , True, (200.000*algebraic[3])/(1.00000-exp(-0.100000*algebraic[3]))])
    algebraic[17] = 8000.00*exp(-0.0560000*(states[0]+66.0000))
    algebraic[5] = (states[0]+24.0000)-5.00000
    algebraic[14] = custom_piecewise([less(fabs(algebraic[5]) , constants[26]), 120.000 , True, (30.0000*algebraic[5])/(1.00000-exp((-1.00000*algebraic[5])/4.00000))])
    algebraic[18] = custom_piecewise([less(fabs(algebraic[5]) , constants[26]), 120.000 , True, (12.0000*algebraic[5])/(exp(algebraic[5]/10.0000)-1.00000)])
    algebraic[6] = states[0]+34.0000
    algebraic[15] = custom_piecewise([less(fabs(algebraic[6]) , constants[27]), 25.0000 , True, (6.25000*algebraic[6])/(exp(algebraic[6]/4.00000)-1.00000)])
    algebraic[19] = 50.0000/(1.00000+exp((-1.00000*(states[0]+34.0000))/4.00000))
    algebraic[8] = (states[0]+34.0000)--30.0000
    algebraic[16] = (0.625000*algebraic[8])/(exp(algebraic[8]/4.00000)-1.00000)
    algebraic[21] = 5.00000/(1.00000+exp((-1.00000*algebraic[8])/4.00000))
    algebraic[0] = constants[39]*log(constants[8]/states[2])
    algebraic[27] = constants[13]*(states[0]-algebraic[0])
    algebraic[30] = (((constants[16]*constants[7])/(constants[17]+constants[7]))*states[2])/(constants[18]+states[2])
    algebraic[31] = (constants[20]*(exp((constants[22]*(constants[19]-2.00000)*states[0])/constants[39])*(power(states[2], constants[19]))*constants[15]-exp(((constants[22]-1.00000)*(constants[19]-2.00000)*states[0])/constants[39])*(power(constants[8], constants[19]))*states[5]))/((1.00000+constants[21]*(states[5]*(power(constants[8], constants[19]))+constants[15]*(power(states[2], constants[19]))))*(1.00000+states[5]/0.00690000))
    algebraic[32] = constants[39]*log((constants[8]+0.120000*constants[7])/(states[2]+0.120000*states[1]))
    algebraic[33] = constants[23]*(power(states[6], 3.00000))*states[7]*(states[0]-algebraic[32])
    algebraic[20] = (((power(states[3], 2.00000))*constants[7])/(constants[7]+constants[6]))*constants[4]*(states[0]-algebraic[0])
    algebraic[37] = ((0.0100000*constants[25]*(states[0]-50.0000))/(constants[39]*(1.00000-exp((-1.00000*(states[0]-50.0000))/constants[39]))))*(states[2]*exp(50.0000/constants[39])-constants[8]*exp((-1.00000*(states[0]-50.0000))/constants[39]))*states[8]*states[9]*states[10]
    algebraic[36] = ((2.00000*1.00000*constants[41]*constants[2])/(1.00000*constants[35]*constants[33]))*states[5]*(constants[33]-states[11])
    algebraic[38] = ((2.00000*1.00000*constants[43]*constants[2])/(1.00000*constants[36]))*states[13]*(states[11]-states[12])
    algebraic[24] = (constants[10]*(states[1]-constants[7]*exp(-states[0]/constants[39])))/140.000
    algebraic[25] = states[4]*algebraic[24]
    algebraic[9] = constants[39]*log(constants[7]/states[1])
    algebraic[26] = (((constants[11]*constants[7])/(constants[7]+constants[12]))*(states[0]-algebraic[9]))/(1.00000+exp((((states[0]+10.0000)-algebraic[9])*2.00000)/constants[39]))
    algebraic[22] = (((power(states[3], 2.00000))*constants[7])/(constants[7]+constants[6]))*constants[5]*(states[0]-algebraic[9])
    algebraic[35] = ((0.0100000*constants[25]*(states[0]-50.0000))/(constants[39]*(1.00000-exp((-1.00000*(states[0]-50.0000))/constants[39]))))*(states[1]*exp(50.0000/constants[39])-constants[7]*exp((-1.00000*(states[0]-50.0000))/constants[39]))*states[8]*states[9]*states[10]
    algebraic[39] = (algebraic[26]+algebraic[25]+algebraic[22]+algebraic[35])-2.00000*algebraic[30]
    algebraic[23] = algebraic[20]+algebraic[22]
    algebraic[28] = 0.500000*constants[39]*log(constants[15]/states[5])
    algebraic[29] = constants[14]*(states[0]-algebraic[28])
    algebraic[34] = ((4.00000*constants[25]*(states[0]-50.0000))/(constants[39]*(1.00000-exp((-1.00000*(states[0]-50.0000)*2.00000)/constants[39]))))*(states[5]*exp(100.000/constants[39])-constants[15]*exp((-2.00000*(states[0]-50.0000))/constants[39]))*states[8]*states[9]*states[10]
    algebraic[40] = algebraic[34]+algebraic[35]+algebraic[37]
    algebraic[41] = (((2.00000*1.00000*constants[43]*constants[2])/(1.00000*constants[37]))*states[12]*(power(states[5], constants[38])))/(power(states[5], constants[38])+power(constants[34], constants[38]))
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
        self.C = 6e-5
        self.g_f_Na = 0.06
        self.g_f_K = 0.06
        self.Km_f = 45
        self.Kc = 3
        self.Nao = 140
        self.speed_y = 2
        self.i_K_max = 0.8
        self.g_K1 = 0.0075
        self.Km_K1 = 10
        self.g_Nab = 0.0007
        self.g_Cab = 0.0001
        self.Cao = 2
        self.I_p = 0.45
        self.K_mK = 1
        self.K_mNa = 40
        self.n_NaCa = 3
        self.K_NaCa = 2e-5
        self.d_NaCa = 0.0001
        self.gamma = 0.5
        self.g_Na = 0.0125
        self.delta_m = 1e-5
        self.P_si = 0.12
        self.delta_d = 0.0001
        self.delta_f = 0.0001
        self.alpha_f2 = 10
        self.K_mf2 = 0.0005
        self.radius = 0.008
        self.length = 0.11
        self.V_e_ratio = 0.1
        self.Ca_up_max = 5
        self.K_mCa = 0.002
        self.tau_up = 0.005
        self.tau_rep = 0.2
        self.tau_rel = 0.01
        self.rCa = 2

    def to_dict(self):
        return {
            "R": self.R,
            "T": self.T,
            "F": self.F,
            "C": self.C,
            "g_f_Na": self.g_f_Na,
            "g_f_K": self.g_f_K,
            "Km_f": self.Km_f,
            "Kc": self.Kc,
            "Nao": self.Nao,
            "speed_y": self.speed_y,
            "i_K_max": self.i_K_max,
            "g_K1": self.g_K1,
            "Km_K1": self.Km_K1,
            "g_Nab": self.g_Nab,
            "g_Cab": self.g_Cab,
            "Cao": self.Cao,
            "I_p": self.I_p,
            "K_mK": self.K_mK,
            "K_mNa": self.K_mNa,
            "n_NaCa": self.n_NaCa,
            "K_NaCa": self.K_NaCa,
            "d_NaCa": self.d_NaCa,
            "gamma": self.gamma,
            "g_Na": self.g_Na,
            "delta_m": self.delta_m,
            "P_si": self.P_si,
            "delta_d": self.delta_d,
            "delta_f": self.delta_f,
            "alpha_f2": self.alpha_f2,
            "K_mf2": self.K_mf2,
            "radius": self.radius,
            "length": self.length,
            "V_e_ratio": self.V_e_ratio,
            "Ca_up_max": self.Ca_up_max,
            "K_mCa": self.K_mCa,
            "tau_up": self.tau_up,
            "tau_rep": self.tau_rep,
            "tau_rel": self.tau_rel,
            "rCa": self.rCa,
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
        y0=[-67.797059970601, 139.859968229045, 7.51007221193712, 0.0743464067197738, 0.129303443591363, 5.84191784887783e-5, 0.042697621819783, 0.138105285882671, 1.26333192869164e-5, 0.999507224159629, 0.485471180273736, 3.70806465918854, 0.177741556496929, 0.176207580044253],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "noble_difrancesco_denyer_1989"
        self.curve_names = [
            "V",
            "Ki",
            "Nai",
            "y",
            "x",
            "Cai",
            "m",
            "h",
            "d",
            "f",
            "f2",
            "Ca_up",
            "Ca_rel",
            "p",
        ]
        self.state_names = ['V', 'Ki', 'Nai', 'y', 'x', 'Cai', 'm', 'h', 'd', 'f', 'f2', 'Ca_up', 'Ca_rel', 'p']
        self.algebraic_names = ['E_Na', 'alpha_y', 'alpha_x', 'E0_m', 'alpha_h', 'E0_d', 'E0_f', 'beta_f2', 'E0_p', 'E_K', 'beta_y', 'beta_x', 'alpha_m', 'beta_h', 'alpha_d', 'alpha_f', 'alpha_p', 'beta_m', 'beta_d', 'beta_f', 'i_fNa', 'beta_p', 'i_fK', 'i_f', 'I_K', 'i_K', 'i_K1', 'i_Na_b', 'E_Ca', 'i_Ca_b', 'i_p', 'i_NaCa', 'E_mh', 'i_Na', 'i_siCa', 'i_siK', 'i_up', 'i_siNa', 'i_tr', 'i_mK', 'i_si', 'i_rel']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 44
        p = self.params

        # direct mapping
        c[0] = p.R
        c[1] = p.T
        c[2] = p.F
        c[3] = p.C
        c[4] = p.g_f_Na
        c[5] = p.g_f_K
        c[6] = p.Km_f
        c[7] = p.Kc
        c[8] = p.Nao
        c[9] = p.speed_y
        c[10] = p.i_K_max
        c[11] = p.g_K1
        c[12] = p.Km_K1
        c[13] = p.g_Nab
        c[14] = p.g_Cab
        c[15] = p.Cao
        c[16] = p.I_p
        c[17] = p.K_mK
        c[18] = p.K_mNa
        c[19] = p.n_NaCa
        c[20] = p.K_NaCa
        c[21] = p.d_NaCa
        c[22] = p.gamma
        c[23] = p.g_Na
        c[24] = p.delta_m
        c[25] = p.P_si
        c[26] = p.delta_d
        c[27] = p.delta_f
        c[28] = p.alpha_f2
        c[29] = p.K_mf2
        c[30] = p.radius
        c[31] = p.length
        c[32] = p.V_e_ratio
        c[33] = p.Ca_up_max
        c[34] = p.K_mCa
        c[35] = p.tau_up
        c[36] = p.tau_rep
        c[37] = p.tau_rel
        c[38] = p.rCa

        # derived constants
        c[39] = (c[0]*c[1])/c[2]
        c[40] = 3.14159*(power(c[30], 2.00000))*c[31]
        c[41] = c[40]*(1.00000-c[32])
        c[42] = c[41]*0.0500000
        c[43] = c[41]*0.0200000

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
