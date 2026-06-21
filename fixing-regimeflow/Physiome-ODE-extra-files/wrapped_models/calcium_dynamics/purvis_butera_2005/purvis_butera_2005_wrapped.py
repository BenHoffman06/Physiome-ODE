# Size of variable arrays:
sizeAlgebraic = 31
sizeStates = 16
sizeConstants = 72
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
    legend_constants[0] = "C in component membrane (uF)"
    legend_algebraic[0] = "i_Na in component sodium_current (nanoA)"
    legend_algebraic[15] = "i_NaP in component persistent_sodium_current (nanoA)"
    legend_algebraic[22] = "i_K in component delayed_rectifier_current (nanoA)"
    legend_algebraic[23] = "i_leak in component leak_current (nanoA)"
    legend_algebraic[24] = "i_T in component LVA_calcium_current (nanoA)"
    legend_algebraic[25] = "i_N in component N_HVA_calcium_current (nanoA)"
    legend_algebraic[26] = "i_P in component P_HVA_calcium_current (nanoA)"
    legend_algebraic[27] = "i_SK in component calcium_dependent_potassium_current (nanoA)"
    legend_algebraic[28] = "i_A in component fast_transient_potassium_current (nanoA)"
    legend_algebraic[29] = "i_H in component hyperpolarization_activated_current (nanoA)"
    legend_algebraic[30] = "i_app in component stimulus_protocol (nanoA)"
    legend_constants[1] = "g_Na in component sodium_current (uS)"
    legend_constants[2] = "E_Na in component sodium_current (millivolt)"
    legend_states[1] = "m in component sodium_current_m_gate (dimensionless)"
    legend_states[2] = "h in component sodium_current_h_gate (dimensionless)"
    legend_constants[3] = "theta_h in component sodium_current_h_gate (millivolt)"
    legend_constants[4] = "sigma_h in component sodium_current_h_gate (millivolt)"
    legend_constants[5] = "theta_1 in component sodium_current_h_gate (millivolt)"
    legend_constants[6] = "sigma_1 in component sodium_current_h_gate (millivolt)"
    legend_constants[7] = "sigma_2 in component sodium_current_h_gate (millivolt)"
    legend_algebraic[1] = "tau_h in component sodium_current_h_gate (millisecond)"
    legend_algebraic[16] = "h_infinity in component sodium_current_h_gate (dimensionless)"
    legend_constants[8] = "theta_m in component sodium_current_m_gate (millivolt)"
    legend_constants[9] = "sigma_m in component sodium_current_m_gate (millivolt)"
    legend_constants[10] = "tau_m in component sodium_current_m_gate (millisecond)"
    legend_algebraic[2] = "m_infinity in component sodium_current_m_gate (dimensionless)"
    legend_constants[11] = "g_NaP in component persistent_sodium_current (uS)"
    legend_states[3] = "m in component persistent_sodium_current_m_gate (dimensionless)"
    legend_states[4] = "h in component persistent_sodium_current_h_gate (dimensionless)"
    legend_constants[12] = "theta_h in component persistent_sodium_current_h_gate (millivolt)"
    legend_constants[13] = "sigma_h in component persistent_sodium_current_h_gate (millivolt)"
    legend_constants[14] = "tau_h in component persistent_sodium_current_h_gate (millisecond)"
    legend_algebraic[3] = "h_infinity in component persistent_sodium_current_h_gate (dimensionless)"
    legend_constants[15] = "theta_m in component persistent_sodium_current_m_gate (millivolt)"
    legend_constants[16] = "sigma_m in component persistent_sodium_current_m_gate (millivolt)"
    legend_constants[17] = "tau_m in component persistent_sodium_current_m_gate (millisecond)"
    legend_algebraic[4] = "m_infinity in component persistent_sodium_current_m_gate (dimensionless)"
    legend_constants[18] = "g_K in component delayed_rectifier_current (uS)"
    legend_constants[19] = "E_K in component delayed_rectifier_current (millivolt)"
    legend_states[5] = "n in component delayed_rectifier_current_n_gate (dimensionless)"
    legend_constants[20] = "theta_n in component delayed_rectifier_current_n_gate (millivolt)"
    legend_constants[21] = "sigma_n in component delayed_rectifier_current_n_gate (millivolt)"
    legend_constants[22] = "theta_1 in component delayed_rectifier_current_n_gate (millivolt)"
    legend_constants[23] = "sigma_1 in component delayed_rectifier_current_n_gate (millivolt)"
    legend_constants[24] = "sigma_2 in component delayed_rectifier_current_n_gate (millivolt)"
    legend_algebraic[5] = "tau_n in component delayed_rectifier_current_n_gate (millisecond)"
    legend_algebraic[17] = "n_infinity in component delayed_rectifier_current_n_gate (dimensionless)"
    legend_constants[25] = "g_leak in component leak_current (uS)"
    legend_constants[26] = "E_leak in component leak_current (millivolt)"
    legend_constants[27] = "g_T in component LVA_calcium_current (uS)"
    legend_constants[28] = "E_Ca in component LVA_calcium_current (millivolt)"
    legend_states[6] = "m in component LVA_calcium_current_m_gate (dimensionless)"
    legend_states[7] = "h in component LVA_calcium_current_h_gate (dimensionless)"
    legend_constants[29] = "theta_m in component LVA_calcium_current_m_gate (millivolt)"
    legend_constants[30] = "sigma_m in component LVA_calcium_current_m_gate (millivolt)"
    legend_constants[31] = "theta_1 in component LVA_calcium_current_m_gate (millivolt)"
    legend_constants[32] = "sigma_1 in component LVA_calcium_current_m_gate (millivolt)"
    legend_constants[33] = "sigma_2 in component LVA_calcium_current_m_gate (millivolt)"
    legend_algebraic[6] = "tau_m in component LVA_calcium_current_m_gate (millisecond)"
    legend_algebraic[18] = "m_infinity in component LVA_calcium_current_m_gate (dimensionless)"
    legend_constants[34] = "theta_h in component LVA_calcium_current_h_gate (millivolt)"
    legend_constants[35] = "sigma_h in component LVA_calcium_current_h_gate (millivolt)"
    legend_constants[36] = "theta_1 in component LVA_calcium_current_h_gate (millivolt)"
    legend_constants[37] = "sigma_1 in component LVA_calcium_current_h_gate (millivolt)"
    legend_algebraic[7] = "tau_h in component LVA_calcium_current_h_gate (millisecond)"
    legend_algebraic[19] = "h_infinity in component LVA_calcium_current_h_gate (dimensionless)"
    legend_constants[38] = "g_N in component N_HVA_calcium_current (uS)"
    legend_states[8] = "m in component N_HVA_calcium_current_m_gate (dimensionless)"
    legend_states[9] = "h in component N_HVA_calcium_current_h_gate (dimensionless)"
    legend_constants[39] = "theta_m in component N_HVA_calcium_current_m_gate (millivolt)"
    legend_constants[40] = "sigma_m in component N_HVA_calcium_current_m_gate (millivolt)"
    legend_constants[41] = "tau_m in component N_HVA_calcium_current_m_gate (millisecond)"
    legend_algebraic[8] = "m_infinity in component N_HVA_calcium_current_m_gate (dimensionless)"
    legend_constants[42] = "theta_h in component N_HVA_calcium_current_h_gate (millivolt)"
    legend_constants[43] = "sigma_h in component N_HVA_calcium_current_h_gate (millivolt)"
    legend_constants[44] = "tau_h in component N_HVA_calcium_current_h_gate (millisecond)"
    legend_algebraic[9] = "h_infinity in component N_HVA_calcium_current_h_gate (dimensionless)"
    legend_constants[45] = "g_P in component P_HVA_calcium_current (uS)"
    legend_states[10] = "m in component P_HVA_calcium_current_m_gate (dimensionless)"
    legend_constants[46] = "theta_m in component P_HVA_calcium_current_m_gate (millivolt)"
    legend_constants[47] = "sigma_m in component P_HVA_calcium_current_m_gate (millivolt)"
    legend_constants[48] = "tau_m in component P_HVA_calcium_current_m_gate (millisecond)"
    legend_algebraic[10] = "m_infinity in component P_HVA_calcium_current_m_gate (dimensionless)"
    legend_constants[49] = "g_SK in component calcium_dependent_potassium_current (uS)"
    legend_states[11] = "z in component calcium_dependent_potassium_current_z_gate (dimensionless)"
    legend_constants[50] = "K1 in component calcium_dependent_potassium_current_z_gate (uM_per_nanocoulomb)"
    legend_constants[51] = "K2 in component calcium_dependent_potassium_current_z_gate (per_ms)"
    legend_states[12] = "Ca_conc in component calcium_dependent_potassium_current_z_gate (uM)"
    legend_constants[52] = "tau_z in component calcium_dependent_potassium_current_z_gate (millisecond)"
    legend_algebraic[11] = "z_infinity in component calcium_dependent_potassium_current_z_gate (dimensionless)"
    legend_constants[53] = "g_A in component fast_transient_potassium_current (uS)"
    legend_states[13] = "m in component fast_transient_potassium_current_m_gate (dimensionless)"
    legend_states[14] = "h in component fast_transient_potassium_current_h_gate (dimensionless)"
    legend_constants[54] = "theta_m in component fast_transient_potassium_current_m_gate (millivolt)"
    legend_constants[55] = "sigma_m in component fast_transient_potassium_current_m_gate (millivolt)"
    legend_constants[56] = "theta_1 in component fast_transient_potassium_current_m_gate (millivolt)"
    legend_constants[57] = "theta_2 in component fast_transient_potassium_current_m_gate (millivolt)"
    legend_constants[58] = "sigma_1 in component fast_transient_potassium_current_m_gate (millivolt)"
    legend_constants[59] = "sigma_2 in component fast_transient_potassium_current_m_gate (millivolt)"
    legend_algebraic[12] = "tau_m in component fast_transient_potassium_current_m_gate (millisecond)"
    legend_algebraic[20] = "m_infinity in component fast_transient_potassium_current_m_gate (dimensionless)"
    legend_constants[60] = "theta_h in component fast_transient_potassium_current_h_gate (millivolt)"
    legend_constants[61] = "sigma_h in component fast_transient_potassium_current_h_gate (millivolt)"
    legend_constants[62] = "tau_h in component fast_transient_potassium_current_h_gate (millisecond)"
    legend_algebraic[13] = "h_infinity in component fast_transient_potassium_current_h_gate (dimensionless)"
    legend_constants[63] = "g_H in component hyperpolarization_activated_current (uS)"
    legend_constants[64] = "E_H in component hyperpolarization_activated_current (millivolt)"
    legend_states[15] = "m in component hyperpolarization_activated_current_m_gate (dimensionless)"
    legend_constants[65] = "theta_m in component hyperpolarization_activated_current_m_gate (millivolt)"
    legend_constants[66] = "sigma_m in component hyperpolarization_activated_current_m_gate (millivolt)"
    legend_constants[67] = "theta_1 in component hyperpolarization_activated_current_m_gate (millivolt)"
    legend_constants[68] = "sigma_1 in component hyperpolarization_activated_current_m_gate (millivolt)"
    legend_algebraic[14] = "tau_m in component hyperpolarization_activated_current_m_gate (millisecond)"
    legend_algebraic[21] = "m_infinity in component hyperpolarization_activated_current_m_gate (dimensionless)"
    legend_constants[69] = "i_stimStart in component stimulus_protocol (millisecond)"
    legend_constants[70] = "i_stimEnd in component stimulus_protocol (millisecond)"
    legend_constants[71] = "i_stimAmplitude in component stimulus_protocol (nanoA)"
    legend_rates[0] = "d/dt V in component membrane (millivolt)"
    legend_rates[2] = "d/dt h in component sodium_current_h_gate (dimensionless)"
    legend_rates[1] = "d/dt m in component sodium_current_m_gate (dimensionless)"
    legend_rates[4] = "d/dt h in component persistent_sodium_current_h_gate (dimensionless)"
    legend_rates[3] = "d/dt m in component persistent_sodium_current_m_gate (dimensionless)"
    legend_rates[5] = "d/dt n in component delayed_rectifier_current_n_gate (dimensionless)"
    legend_rates[6] = "d/dt m in component LVA_calcium_current_m_gate (dimensionless)"
    legend_rates[7] = "d/dt h in component LVA_calcium_current_h_gate (dimensionless)"
    legend_rates[8] = "d/dt m in component N_HVA_calcium_current_m_gate (dimensionless)"
    legend_rates[9] = "d/dt h in component N_HVA_calcium_current_h_gate (dimensionless)"
    legend_rates[10] = "d/dt m in component P_HVA_calcium_current_m_gate (dimensionless)"
    legend_rates[12] = "d/dt Ca_conc in component calcium_dependent_potassium_current_z_gate (uM)"
    legend_rates[11] = "d/dt z in component calcium_dependent_potassium_current_z_gate (dimensionless)"
    legend_rates[13] = "d/dt m in component fast_transient_potassium_current_m_gate (dimensionless)"
    legend_rates[14] = "d/dt h in component fast_transient_potassium_current_h_gate (dimensionless)"
    legend_rates[15] = "d/dt m in component hyperpolarization_activated_current_m_gate (dimensionless)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = -71.847
    constants[0] = 0.04
    constants[1] = 0.7
    constants[2] = 60
    states[1] = 0.015
    states[2] = 0.981
    constants[3] = 44.1
    constants[4] = 7
    constants[5] = 35
    constants[6] = 4
    constants[7] = 25
    constants[8] = 36
    constants[9] = 8.5
    constants[10] = 0.1
    constants[11] = 0.05
    states[3] = 0.002
    states[4] = 0.797
    constants[12] = 65
    constants[13] = 5
    constants[14] = 150
    constants[15] = 47.1
    constants[16] = 4.1
    constants[17] = 0.1
    constants[18] = 1.3
    constants[19] = -80
    states[5] = 0.158
    constants[20] = 30
    constants[21] = 25
    constants[22] = 30
    constants[23] = 40
    constants[24] = 50
    constants[25] = 0.005
    constants[26] = -50
    constants[27] = 0.1
    constants[28] = 40
    states[6] = 0.001
    states[7] = 0.562
    constants[29] = 38
    constants[30] = 5
    constants[31] = 28
    constants[32] = 25
    constants[33] = 70
    constants[34] = 70.1
    constants[35] = 7
    constants[36] = 70
    constants[37] = 65
    constants[38] = 0.05
    states[8] = 0.001
    states[9] = 0.649
    constants[39] = 30
    constants[40] = 6
    constants[41] = 5
    constants[42] = 70
    constants[43] = 3
    constants[44] = 25
    constants[45] = 0.05
    states[10] = 0
    constants[46] = 17
    constants[47] = 3
    constants[48] = 10
    constants[49] = 0.3
    states[11] = 0
    constants[50] = -500
    constants[51] = 0.04
    states[12] = 0.0604
    constants[52] = 1
    constants[53] = 1
    states[13] = 0.057
    states[14] = 0.287
    constants[54] = 27
    constants[55] = 16
    constants[56] = 40
    constants[57] = 74
    constants[58] = 5
    constants[59] = 7.5
    constants[60] = 80
    constants[61] = 11
    constants[62] = 20
    constants[63] = 0.005
    constants[64] = -38.8
    states[15] = 0.182
    constants[65] = 79.8
    constants[66] = 5.3
    constants[67] = 70
    constants[68] = 11
    constants[69] = 10
    constants[70] = 11
    constants[71] = 10
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[2] = 1.00000/(1.00000+exp((states[0]+constants[8])/-constants[9]))
    rates[1] = (algebraic[2]-states[1])/constants[10]
    algebraic[3] = 1.00000/(1.00000+exp((states[0]+constants[12])/constants[13]))
    rates[4] = (algebraic[3]-states[4])/constants[14]
    algebraic[4] = 1.00000/(1.00000+exp(-(states[0]+constants[15])/constants[16]))
    rates[3] = (algebraic[4]-states[3])/constants[17]
    algebraic[8] = 1.00000/(1.00000+exp(-(states[0]+constants[39])/constants[40]))
    rates[8] = (algebraic[8]-states[8])/constants[41]
    algebraic[9] = 1.00000/(1.00000+exp((states[0]+constants[42])/constants[43]))
    rates[9] = (algebraic[9]-states[9])/constants[44]
    algebraic[10] = 1.00000/(1.00000+exp(-(states[0]+constants[46])/constants[47]))
    rates[10] = (algebraic[10]-states[10])/constants[48]
    algebraic[11] = 1.00000/(1.00000+power(0.00300000/states[12], 2.00000))
    rates[11] = (algebraic[11]-states[11])/constants[52]
    algebraic[13] = 1.00000/(1.00000+exp((states[0]+constants[60])/constants[61]))
    rates[14] = (algebraic[13]-states[14])/constants[62]
    algebraic[1] = 3.50000/(exp((states[0]+constants[5])/constants[6])+exp(-(states[0]+constants[5])/constants[7]))+1.00000
    algebraic[16] = 1.00000/(1.00000+exp((states[0]+constants[3])/constants[4]))
    rates[2] = (algebraic[16]-states[2])/algebraic[1]
    algebraic[5] = 2.50000/(exp((states[0]+constants[22])/constants[23])+exp(-(states[0]+constants[22])/constants[24]))+0.0100000
    algebraic[17] = 1.00000/(1.00000+exp(-(states[0]+constants[20])/constants[21]))
    rates[5] = (algebraic[17]-states[5])/algebraic[5]
    algebraic[6] = 5.00000/(exp((states[0]+constants[31])/constants[32])+exp(-(states[0]+constants[31])/constants[33]))+2.00000
    algebraic[18] = 1.00000/(1.00000+exp(-(states[0]+constants[29])/constants[30]))
    rates[6] = (algebraic[18]-states[6])/algebraic[6]
    algebraic[7] = 20.0000/(exp((states[0]+constants[36])/constants[37])+exp(-(states[0]+constants[36])/constants[37]))+1.00000
    algebraic[19] = 1.00000/(1.00000+exp((states[0]+constants[34])/constants[35]))
    rates[7] = (algebraic[19]-states[7])/algebraic[7]
    algebraic[12] = 1.00000/(exp((states[0]+constants[56])/constants[58])+exp(-(states[0]+constants[57])/constants[59]))+0.370000
    algebraic[20] = 1.00000/(1.00000+exp(-(states[0]+constants[54])/constants[55]))
    rates[13] = (algebraic[20]-states[13])/algebraic[12]
    algebraic[14] = 1.00000/(exp((states[0]+constants[67])/constants[68])+exp(-(states[0]+constants[67])/constants[68]))+50.0000
    algebraic[21] = 1.00000/(1.00000+exp((states[0]+constants[65])/constants[66]))
    rates[15] = (algebraic[21]-states[15])/algebraic[14]
    algebraic[24] = constants[27]*states[6]*states[7]*(states[0]-constants[28])
    algebraic[25] = constants[38]*states[8]*states[9]*(states[0]-constants[28])
    algebraic[26] = constants[45]*states[10]*(states[0]-constants[28])
    rates[12] = (1.00000/1000.00)*constants[50]*(algebraic[24]+algebraic[25]+algebraic[26])-constants[51]*states[12]
    algebraic[0] = constants[1]*(power(states[1], 3.00000))*states[2]*(states[0]-constants[2])
    algebraic[15] = constants[11]*states[3]*states[4]*(states[0]-constants[2])
    algebraic[22] = constants[18]*(power(states[5], 4.00000))*(states[0]-constants[19])
    algebraic[23] = constants[25]*(states[0]-constants[26])
    algebraic[27] = constants[49]*(power(states[11], 2.00000))*(states[0]-constants[19])
    algebraic[28] = constants[53]*states[13]*states[14]*(states[0]-constants[19])
    algebraic[29] = constants[63]*states[15]*(states[0]-constants[64])
    algebraic[30] = custom_piecewise([greater_equal(voi , constants[69]) & less_equal(voi , constants[70]), constants[71] , True, 0.00000])
    rates[0] = (-(algebraic[0]+algebraic[15]+algebraic[22]+algebraic[23]+algebraic[24]+algebraic[25]+algebraic[26]+algebraic[27]+algebraic[28]+algebraic[29])+algebraic[30])/constants[0]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[2] = 1.00000/(1.00000+exp((states[0]+constants[8])/-constants[9]))
    algebraic[3] = 1.00000/(1.00000+exp((states[0]+constants[12])/constants[13]))
    algebraic[4] = 1.00000/(1.00000+exp(-(states[0]+constants[15])/constants[16]))
    algebraic[8] = 1.00000/(1.00000+exp(-(states[0]+constants[39])/constants[40]))
    algebraic[9] = 1.00000/(1.00000+exp((states[0]+constants[42])/constants[43]))
    algebraic[10] = 1.00000/(1.00000+exp(-(states[0]+constants[46])/constants[47]))
    algebraic[11] = 1.00000/(1.00000+power(0.00300000/states[12], 2.00000))
    algebraic[13] = 1.00000/(1.00000+exp((states[0]+constants[60])/constants[61]))
    algebraic[1] = 3.50000/(exp((states[0]+constants[5])/constants[6])+exp(-(states[0]+constants[5])/constants[7]))+1.00000
    algebraic[16] = 1.00000/(1.00000+exp((states[0]+constants[3])/constants[4]))
    algebraic[5] = 2.50000/(exp((states[0]+constants[22])/constants[23])+exp(-(states[0]+constants[22])/constants[24]))+0.0100000
    algebraic[17] = 1.00000/(1.00000+exp(-(states[0]+constants[20])/constants[21]))
    algebraic[6] = 5.00000/(exp((states[0]+constants[31])/constants[32])+exp(-(states[0]+constants[31])/constants[33]))+2.00000
    algebraic[18] = 1.00000/(1.00000+exp(-(states[0]+constants[29])/constants[30]))
    algebraic[7] = 20.0000/(exp((states[0]+constants[36])/constants[37])+exp(-(states[0]+constants[36])/constants[37]))+1.00000
    algebraic[19] = 1.00000/(1.00000+exp((states[0]+constants[34])/constants[35]))
    algebraic[12] = 1.00000/(exp((states[0]+constants[56])/constants[58])+exp(-(states[0]+constants[57])/constants[59]))+0.370000
    algebraic[20] = 1.00000/(1.00000+exp(-(states[0]+constants[54])/constants[55]))
    algebraic[14] = 1.00000/(exp((states[0]+constants[67])/constants[68])+exp(-(states[0]+constants[67])/constants[68]))+50.0000
    algebraic[21] = 1.00000/(1.00000+exp((states[0]+constants[65])/constants[66]))
    algebraic[24] = constants[27]*states[6]*states[7]*(states[0]-constants[28])
    algebraic[25] = constants[38]*states[8]*states[9]*(states[0]-constants[28])
    algebraic[26] = constants[45]*states[10]*(states[0]-constants[28])
    algebraic[0] = constants[1]*(power(states[1], 3.00000))*states[2]*(states[0]-constants[2])
    algebraic[15] = constants[11]*states[3]*states[4]*(states[0]-constants[2])
    algebraic[22] = constants[18]*(power(states[5], 4.00000))*(states[0]-constants[19])
    algebraic[23] = constants[25]*(states[0]-constants[26])
    algebraic[27] = constants[49]*(power(states[11], 2.00000))*(states[0]-constants[19])
    algebraic[28] = constants[53]*states[13]*states[14]*(states[0]-constants[19])
    algebraic[29] = constants[63]*states[15]*(states[0]-constants[64])
    algebraic[30] = custom_piecewise([greater_equal(voi , constants[69]) & less_equal(voi , constants[70]), constants[71] , True, 0.00000])
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
        self.C = 0.04
        self.g_Na = 0.7
        self.E_Na = 60
        self.theta_h = 44.1
        self.sigma_h = 7
        self.theta_1 = 35
        self.sigma_1 = 4
        self.sigma_2 = 25
        self.theta_m = 36
        self.sigma_m = 8.5
        self.tau_m = 0.1
        self.g_NaP = 0.05
        self.theta_h_1 = 65
        self.sigma_h_1 = 5
        self.tau_h = 150
        self.theta_m_1 = 47.1
        self.sigma_m_1 = 4.1
        self.tau_m_1 = 0.1
        self.g_K = 1.3
        self.E_K = -80
        self.theta_n = 30
        self.sigma_n = 25
        self.theta_1_1 = 30
        self.sigma_1_1 = 40
        self.sigma_2_1 = 50
        self.g_leak = 0.005
        self.E_leak = -50
        self.g_T = 0.1
        self.E_Ca = 40
        self.theta_m_2 = 38
        self.sigma_m_2 = 5
        self.theta_1_2 = 28
        self.sigma_1_2 = 25
        self.sigma_2_2 = 70
        self.theta_h_2 = 70.1
        self.sigma_h_2 = 7
        self.theta_1_3 = 70
        self.sigma_1_3 = 65
        self.g_N = 0.05
        self.theta_m_3 = 30
        self.sigma_m_3 = 6
        self.tau_m_2 = 5
        self.theta_h_3 = 70
        self.sigma_h_3 = 3
        self.tau_h_1 = 25
        self.g_P = 0.05
        self.theta_m_4 = 17
        self.sigma_m_4 = 3
        self.tau_m_3 = 10
        self.g_SK = 0.3
        self.K1 = -500
        self.K2 = 0.04
        self.tau_z = 1
        self.g_A = 1
        self.theta_m_5 = 27
        self.sigma_m_5 = 16
        self.theta_1_4 = 40
        self.theta_2 = 74
        self.sigma_1_4 = 5
        self.sigma_2_3 = 7.5
        self.theta_h_4 = 80
        self.sigma_h_4 = 11
        self.tau_h_2 = 20
        self.g_H = 0.005
        self.E_H = -38.8
        self.theta_m_6 = 79.8
        self.sigma_m_6 = 5.3
        self.theta_1_5 = 70
        self.sigma_1_5 = 11
        self.i_stimStart = 10
        self.i_stimEnd = 11
        self.i_stimAmplitude = 10

    def to_dict(self):
        return {
            "C": self.C,
            "g_Na": self.g_Na,
            "E_Na": self.E_Na,
            "theta_h": self.theta_h,
            "sigma_h": self.sigma_h,
            "theta_1": self.theta_1,
            "sigma_1": self.sigma_1,
            "sigma_2": self.sigma_2,
            "theta_m": self.theta_m,
            "sigma_m": self.sigma_m,
            "tau_m": self.tau_m,
            "g_NaP": self.g_NaP,
            "theta_h_1": self.theta_h_1,
            "sigma_h_1": self.sigma_h_1,
            "tau_h": self.tau_h,
            "theta_m_1": self.theta_m_1,
            "sigma_m_1": self.sigma_m_1,
            "tau_m_1": self.tau_m_1,
            "g_K": self.g_K,
            "E_K": self.E_K,
            "theta_n": self.theta_n,
            "sigma_n": self.sigma_n,
            "theta_1_1": self.theta_1_1,
            "sigma_1_1": self.sigma_1_1,
            "sigma_2_1": self.sigma_2_1,
            "g_leak": self.g_leak,
            "E_leak": self.E_leak,
            "g_T": self.g_T,
            "E_Ca": self.E_Ca,
            "theta_m_2": self.theta_m_2,
            "sigma_m_2": self.sigma_m_2,
            "theta_1_2": self.theta_1_2,
            "sigma_1_2": self.sigma_1_2,
            "sigma_2_2": self.sigma_2_2,
            "theta_h_2": self.theta_h_2,
            "sigma_h_2": self.sigma_h_2,
            "theta_1_3": self.theta_1_3,
            "sigma_1_3": self.sigma_1_3,
            "g_N": self.g_N,
            "theta_m_3": self.theta_m_3,
            "sigma_m_3": self.sigma_m_3,
            "tau_m_2": self.tau_m_2,
            "theta_h_3": self.theta_h_3,
            "sigma_h_3": self.sigma_h_3,
            "tau_h_1": self.tau_h_1,
            "g_P": self.g_P,
            "theta_m_4": self.theta_m_4,
            "sigma_m_4": self.sigma_m_4,
            "tau_m_3": self.tau_m_3,
            "g_SK": self.g_SK,
            "K1": self.K1,
            "K2": self.K2,
            "tau_z": self.tau_z,
            "g_A": self.g_A,
            "theta_m_5": self.theta_m_5,
            "sigma_m_5": self.sigma_m_5,
            "theta_1_4": self.theta_1_4,
            "theta_2": self.theta_2,
            "sigma_1_4": self.sigma_1_4,
            "sigma_2_3": self.sigma_2_3,
            "theta_h_4": self.theta_h_4,
            "sigma_h_4": self.sigma_h_4,
            "tau_h_2": self.tau_h_2,
            "g_H": self.g_H,
            "E_H": self.E_H,
            "theta_m_6": self.theta_m_6,
            "sigma_m_6": self.sigma_m_6,
            "theta_1_5": self.theta_1_5,
            "sigma_1_5": self.sigma_1_5,
            "i_stimStart": self.i_stimStart,
            "i_stimEnd": self.i_stimEnd,
            "i_stimAmplitude": self.i_stimAmplitude,
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
        y0=[-71.847, 0.015, 0.981, 0.002, 0.797, 0.158, 0.001, 0.562, 0.001, 0.649, 0, 0, 0.0604, 0.057, 0.287, 0.182],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "purvis_butera_2005"
        self.curve_names = [
            "V",
            "m",
            "h",
            "m_1",
            "h_1",
            "n",
            "m_2",
            "h_2",
            "m_3",
            "h_3",
            "m_4",
            "z",
            "Ca_conc",
            "m_5",
            "h_4",
            "m_6",
        ]
        self.state_names = ['V', 'm', 'h', 'm_1', 'h_1', 'n', 'm_2', 'h_2', 'm_3', 'h_3', 'm_4', 'z', 'Ca_conc', 'm_5', 'h_4', 'm_6']
        self.algebraic_names = ['i_Na', 'tau_h', 'm_infinity', 'h_infinity', 'm_infinity_1', 'tau_n', 'tau_m', 'tau_h_1', 'm_infinity_2', 'h_infinity_1', 'm_infinity_3', 'z_infinity', 'tau_m_1', 'h_infinity_2', 'tau_m_2', 'i_NaP', 'h_infinity_3', 'n_infinity', 'm_infinity_4', 'h_infinity_4', 'm_infinity_5', 'm_infinity_6', 'i_K', 'i_leak', 'i_T', 'i_N', 'i_P', 'i_SK', 'i_A', 'i_H', 'i_app']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 72
        p = self.params

        # direct mapping
        c[0] = p.C
        c[1] = p.g_Na
        c[2] = p.E_Na
        c[3] = p.theta_h
        c[4] = p.sigma_h
        c[5] = p.theta_1
        c[6] = p.sigma_1
        c[7] = p.sigma_2
        c[8] = p.theta_m
        c[9] = p.sigma_m
        c[10] = p.tau_m
        c[11] = p.g_NaP
        c[12] = p.theta_h_1
        c[13] = p.sigma_h_1
        c[14] = p.tau_h
        c[15] = p.theta_m_1
        c[16] = p.sigma_m_1
        c[17] = p.tau_m_1
        c[18] = p.g_K
        c[19] = p.E_K
        c[20] = p.theta_n
        c[21] = p.sigma_n
        c[22] = p.theta_1_1
        c[23] = p.sigma_1_1
        c[24] = p.sigma_2_1
        c[25] = p.g_leak
        c[26] = p.E_leak
        c[27] = p.g_T
        c[28] = p.E_Ca
        c[29] = p.theta_m_2
        c[30] = p.sigma_m_2
        c[31] = p.theta_1_2
        c[32] = p.sigma_1_2
        c[33] = p.sigma_2_2
        c[34] = p.theta_h_2
        c[35] = p.sigma_h_2
        c[36] = p.theta_1_3
        c[37] = p.sigma_1_3
        c[38] = p.g_N
        c[39] = p.theta_m_3
        c[40] = p.sigma_m_3
        c[41] = p.tau_m_2
        c[42] = p.theta_h_3
        c[43] = p.sigma_h_3
        c[44] = p.tau_h_1
        c[45] = p.g_P
        c[46] = p.theta_m_4
        c[47] = p.sigma_m_4
        c[48] = p.tau_m_3
        c[49] = p.g_SK
        c[50] = p.K1
        c[51] = p.K2
        c[52] = p.tau_z
        c[53] = p.g_A
        c[54] = p.theta_m_5
        c[55] = p.sigma_m_5
        c[56] = p.theta_1_4
        c[57] = p.theta_2
        c[58] = p.sigma_1_4
        c[59] = p.sigma_2_3
        c[60] = p.theta_h_4
        c[61] = p.sigma_h_4
        c[62] = p.tau_h_2
        c[63] = p.g_H
        c[64] = p.E_H
        c[65] = p.theta_m_6
        c[66] = p.sigma_m_6
        c[67] = p.theta_1_5
        c[68] = p.sigma_1_5
        c[69] = p.i_stimStart
        c[70] = p.i_stimEnd
        c[71] = p.i_stimAmplitude

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
