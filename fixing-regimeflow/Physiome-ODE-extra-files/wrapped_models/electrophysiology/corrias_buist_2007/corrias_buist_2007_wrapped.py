# Size of variable arrays:
sizeAlgebraic = 34
sizeStates = 14
sizeConstants = 51
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component Time (time_units)"
    legend_constants[0] = "Ach in component Neural_input (millimolar)"
    legend_constants[1] = "Gcouple in component Gap_junction (conductance_units)"
    legend_constants[2] = "T in component Environment (Temperature_units)"
    legend_constants[3] = "T_exp in component Environment (Temperature_units)"
    legend_constants[4] = "F in component Environment (F_units)"
    legend_constants[5] = "R in component Environment (R_units)"
    legend_constants[6] = "Q10Ca in component Environment (dimensionless)"
    legend_constants[7] = "Q10K in component Environment (dimensionless)"
    legend_constants[8] = "Q10Na in component Environment (dimensionless)"
    legend_constants[9] = "Ca_o in component Environment (millimolar)"
    legend_constants[10] = "Na_o in component Environment (millimolar)"
    legend_constants[11] = "K_o in component Environment (millimolar)"
    legend_constants[12] = "Cl_o in component Environment (millimolar)"
    legend_constants[33] = "T_correction_Na in component Environment (dimensionless)"
    legend_constants[34] = "T_correction_K in component Environment (dimensionless)"
    legend_constants[35] = "T_correction_Ca in component Environment (dimensionless)"
    legend_constants[36] = "T_correction_BK in component Environment (conductance_units)"
    legend_constants[37] = "FoRT in component Environment (Inverse_Voltage_units)"
    legend_constants[38] = "RToF in component Environment (voltage_units)"
    legend_constants[13] = "Cm_SM in component SM_Membrane (capacitance_units)"
    legend_constants[14] = "Vol_SM in component SM_Membrane (volume_units)"
    legend_states[0] = "Vm_SM in component SM_Membrane (voltage_units)"
    legend_states[1] = "Ca_i in component SM_Membrane (millimolar)"
    legend_constants[15] = "Na_i in component SM_Membrane (millimolar)"
    legend_constants[16] = "K_i in component SM_Membrane (millimolar)"
    legend_algebraic[30] = "I_Na_SM in component I_Na_SM (current_units)"
    legend_algebraic[22] = "I_Ltype_SM in component I_Ltype_SM (current_units)"
    legend_algebraic[25] = "I_LVA_SM in component I_LVA_SM (current_units)"
    legend_algebraic[29] = "I_kr_SM in component I_kr_SM (current_units)"
    legend_algebraic[31] = "I_ka_SM in component I_ka_SM (current_units)"
    legend_algebraic[27] = "I_BK_SM in component I_BK_SM (current_units)"
    legend_algebraic[33] = "I_NSCC_SM in component I_NSCC_SM (current_units)"
    legend_algebraic[28] = "I_bk_SM in component I_bk_SM (current_units)"
    legend_algebraic[23] = "J_CaSR_SM in component J_CaSR_SM (millimolar_per_millisecond)"
    legend_algebraic[20] = "I_stim in component I_stim (current_units)"
    legend_algebraic[13] = "local_time in component I_stim (time_units)"
    legend_constants[17] = "period in component I_stim (time_units)"
    legend_algebraic[0] = "stim_start in component I_stim (time_units)"
    legend_constants[18] = "delta_VICC in component I_stim (voltage_units)"
    legend_constants[19] = "t_ICCpeak in component I_stim (time_units)"
    legend_constants[20] = "t_ICCplateau in component I_stim (time_units)"
    legend_constants[21] = "t_ICC_stimulus in component I_stim (time_units)"
    legend_constants[22] = "V_decay in component I_stim (voltage_units)"
    legend_algebraic[1] = "d_inf_Ltype_SM in component d_Ltype_SM (dimensionless)"
    legend_constants[40] = "tau_d_Ltype_SM in component d_Ltype_SM (time_units)"
    legend_states[2] = "d_Ltype_SM in component d_Ltype_SM (dimensionless)"
    legend_algebraic[2] = "f_inf_Ltype_SM in component f_Ltype_SM (dimensionless)"
    legend_constants[41] = "tau_f_Ltype_SM in component f_Ltype_SM (time_units)"
    legend_states[3] = "f_Ltype_SM in component f_Ltype_SM (dimensionless)"
    legend_algebraic[3] = "f_ca_inf_Ltype_SM in component f_ca_Ltype_SM (dimensionless)"
    legend_constants[42] = "tau_f_ca_Ltype_SM in component f_ca_Ltype_SM (time_units)"
    legend_states[4] = "f_ca_Ltype_SM in component f_ca_Ltype_SM (dimensionless)"
    legend_algebraic[21] = "E_Ca in component I_Ltype_SM (voltage_units)"
    legend_constants[23] = "G_max_Ltype in component I_Ltype_SM (conductance_units)"
    legend_constants[24] = "J_max_CaSR in component J_CaSR_SM (millimolar_per_millisecond)"
    legend_algebraic[4] = "d_inf_LVA_SM in component d_LVA_SM (dimensionless)"
    legend_constants[43] = "tau_d_LVA_SM in component d_LVA_SM (time_units)"
    legend_states[5] = "d_LVA_SM in component d_LVA_SM (dimensionless)"
    legend_algebraic[5] = "f_inf_LVA_SM in component f_LVA_SM (dimensionless)"
    legend_algebraic[14] = "tau_f_LVA_SM in component f_LVA_SM (time_units)"
    legend_states[6] = "f_LVA_SM in component f_LVA_SM (dimensionless)"
    legend_algebraic[24] = "E_Ca in component I_LVA_SM (voltage_units)"
    legend_constants[25] = "G_max_LVA in component I_LVA_SM (conductance_units)"
    legend_algebraic[26] = "d_BK_SM in component d_BK_SM (dimensionless)"
    legend_constants[44] = "E_K in component I_BK_SM (voltage_units)"
    legend_constants[26] = "G_max_BK in component I_BK_SM (conductance_units)"
    legend_constants[45] = "E_K in component I_bk_SM (voltage_units)"
    legend_constants[27] = "G_max_bk in component I_bk_SM (conductance_units)"
    legend_algebraic[6] = "xr1_inf_SM in component xr1_SM (dimensionless)"
    legend_constants[46] = "tau_xr1_SM in component xr1_SM (time_units)"
    legend_states[7] = "xr1_SM in component xr1_SM (dimensionless)"
    legend_algebraic[7] = "xr2_inf_SM in component xr2_SM (dimensionless)"
    legend_algebraic[15] = "tau_xr2_SM in component xr2_SM (time_units)"
    legend_states[8] = "xr2_SM in component xr2_SM (dimensionless)"
    legend_constants[47] = "E_K in component I_kr_SM (voltage_units)"
    legend_constants[28] = "G_max_kr_SM in component I_kr_SM (conductance_units)"
    legend_algebraic[8] = "m_inf_Na in component m_Na_SM (dimensionless)"
    legend_algebraic[16] = "tau_m_Na in component m_Na_SM (time_units)"
    legend_states[9] = "m_Na_SM in component m_Na_SM (dimensionless)"
    legend_algebraic[9] = "h_inf_Na in component h_Na_SM (dimensionless)"
    legend_algebraic[17] = "tau_h_Na in component h_Na_SM (time_units)"
    legend_states[10] = "h_Na_SM in component h_Na_SM (dimensionless)"
    legend_constants[48] = "E_Na in component I_Na_SM (voltage_units)"
    legend_constants[29] = "G_max_Na_SM in component I_Na_SM (conductance_units)"
    legend_algebraic[10] = "xa1_inf_SM in component xa1_SM (dimensionless)"
    legend_algebraic[18] = "tau_xa1_SM in component xa1_SM (time_units)"
    legend_states[11] = "xa1_SM in component xa1_SM (dimensionless)"
    legend_algebraic[11] = "xa2_inf_SM in component xa2_SM (dimensionless)"
    legend_constants[49] = "tau_xa2_SM in component xa2_SM (time_units)"
    legend_states[12] = "xa2_SM in component xa2_SM (dimensionless)"
    legend_constants[50] = "E_K in component I_ka_SM (voltage_units)"
    legend_constants[30] = "G_max_ka_SM in component I_ka_SM (conductance_units)"
    legend_algebraic[12] = "m_inf_NSCC_SM in component m_NSCC_SM (dimensionless)"
    legend_algebraic[19] = "tau_m_NSCC_SM in component m_NSCC_SM (time_units)"
    legend_states[13] = "m_NSCC_SM in component m_NSCC_SM (dimensionless)"
    legend_constants[31] = "E_NSCC in component I_NSCC_SM (voltage_units)"
    legend_constants[32] = "G_max_NSCC_SM in component I_NSCC_SM (conductance_units)"
    legend_algebraic[32] = "f_ca_NSCC_SM in component I_NSCC_SM (dimensionless)"
    legend_constants[39] = "rach_NSCC_SM in component I_NSCC_SM (dimensionless)"
    legend_rates[0] = "d/dt Vm_SM in component SM_Membrane (voltage_units)"
    legend_rates[1] = "d/dt Ca_i in component SM_Membrane (millimolar)"
    legend_rates[2] = "d/dt d_Ltype_SM in component d_Ltype_SM (dimensionless)"
    legend_rates[3] = "d/dt f_Ltype_SM in component f_Ltype_SM (dimensionless)"
    legend_rates[4] = "d/dt f_ca_Ltype_SM in component f_ca_Ltype_SM (dimensionless)"
    legend_rates[5] = "d/dt d_LVA_SM in component d_LVA_SM (dimensionless)"
    legend_rates[6] = "d/dt f_LVA_SM in component f_LVA_SM (dimensionless)"
    legend_rates[7] = "d/dt xr1_SM in component xr1_SM (dimensionless)"
    legend_rates[8] = "d/dt xr2_SM in component xr2_SM (dimensionless)"
    legend_rates[9] = "d/dt m_Na_SM in component m_Na_SM (dimensionless)"
    legend_rates[10] = "d/dt h_Na_SM in component h_Na_SM (dimensionless)"
    legend_rates[11] = "d/dt xa1_SM in component xa1_SM (dimensionless)"
    legend_rates[12] = "d/dt xa2_SM in component xa2_SM (dimensionless)"
    legend_rates[13] = "d/dt m_NSCC_SM in component m_NSCC_SM (dimensionless)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    constants[0] = 0.00001
    constants[1] = 1.3
    constants[2] = 310
    constants[3] = 297
    constants[4] = 96486
    constants[5] = 8314.4
    constants[6] = 2.1
    constants[7] = 1.365
    constants[8] = 2.45
    constants[9] = 2.5
    constants[10] = 137
    constants[11] = 5.9
    constants[12] = 134
    constants[13] = 77
    constants[14] = 3500
    states[0] = -69.75
    states[1] = 0.00008
    constants[15] = 10
    constants[16] = 164
    constants[17] = 20000
    constants[18] = 59
    constants[19] = 98
    constants[20] = 7582
    constants[21] = 10000
    constants[22] = 37.25
    states[2] = 0.0
    states[3] = 0.95
    states[4] = 1.0
    constants[23] = 65
    constants[24] = 0.31705
    states[5] = 0.02
    states[6] = 0.99
    constants[25] = 0.18
    constants[26] = 45.7
    constants[27] = 0.0144
    states[7] = 0.0
    states[8] = 0.82
    constants[28] = 35
    states[9] = 0.005
    states[10] = 0.05787
    constants[29] = 3
    states[11] = 0.00414
    states[12] = 0.72
    constants[30] = 9
    states[13] = 0.0
    constants[31] = -28
    constants[32] = 50
    constants[33] = power(constants[8], (constants[2]-constants[3])/10.0000)
    constants[34] = power(constants[7], (constants[2]-constants[3])/10.0000)
    constants[35] = power(constants[6], (constants[2]-constants[3])/10.0000)
    constants[36] = 1.10000*(constants[2]-constants[3])
    constants[37] = constants[4]/(constants[5]*constants[2])
    constants[38] = (constants[5]*constants[2])/constants[4]
    constants[39] = 1.00000/(1.00000+0.0100000/constants[0])
    constants[40] = constants[35]*0.470000
    constants[41] = constants[35]*86.0000
    constants[42] = constants[35]*2.00000
    constants[43] = constants[35]*3.00000
    constants[44] = constants[38]*log(constants[11]/constants[16])
    constants[45] = constants[38]*log(constants[11]/constants[16])
    constants[46] = constants[34]*80.0000
    constants[47] = constants[38]*log(constants[11]/constants[16])
    constants[48] = constants[38]*log(constants[10]/constants[15])
    constants[49] = constants[34]*90.0000
    constants[50] = constants[38]*log(constants[11]/constants[16])
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[1] = 1.00000/(1.00000+exp((states[0]+17.0000)/-4.30000))
    rates[2] = (algebraic[1]-states[2])/constants[40]
    algebraic[2] = 1.00000/(1.00000+exp((states[0]+43.0000)/8.90000))
    rates[3] = (algebraic[2]-states[3])/constants[41]
    algebraic[3] = 1.00000-1.00000/(1.00000+exp(((states[1]-8.99900e-05)-0.000214000)/-1.31000e-05))
    rates[4] = (algebraic[3]-states[4])/constants[42]
    algebraic[4] = 1.00000/(1.00000+exp((states[0]+27.5000)/-10.9000))
    rates[5] = (algebraic[4]-states[5])/constants[43]
    algebraic[6] = 1.00000/(1.00000+exp((states[0]+27.0000)/-5.00000))
    rates[7] = (algebraic[6]-states[7])/constants[46]
    algebraic[11] = 0.100000+0.900000/(1.00000+exp((states[0]+65.0000)/6.20000))
    rates[12] = (algebraic[11]-states[12])/constants[49]
    algebraic[5] = 1.00000/(1.00000+exp((states[0]+15.8000)/7.00000))
    algebraic[14] = constants[35]*(7.58000*exp(states[0]*0.00817000))
    rates[6] = (algebraic[5]-states[6])/algebraic[14]
    algebraic[7] = 0.200000+0.800000/(1.00000+exp((states[0]+58.0000)/10.0000))
    algebraic[15] = constants[34]*(-707.000+1481.00*exp((states[0]+36.0000)/95.0000))
    rates[8] = (algebraic[7]-states[8])/algebraic[15]
    algebraic[8] = 1.00000/(1.00000+exp((states[0]+47.0000)/-4.80000))
    algebraic[16] = constants[33]*(states[0]*-0.0170000*1.00000+0.440000)
    rates[9] = (algebraic[8]-states[9])/algebraic[16]
    algebraic[9] = 1.00000/(1.00000+exp((states[0]+78.0000)/3.00000))
    algebraic[17] = constants[33]*(states[0]*-0.250000*1.00000+5.50000)
    rates[10] = (algebraic[9]-states[10])/algebraic[17]
    algebraic[10] = 1.00000/(1.00000+exp((states[0]+26.5000)/-7.90000))
    algebraic[18] = constants[34]*(31.8000+175.000*exp(-0.500000*(power((states[0]+44.4000)/22.3000, 2.00000))))
    rates[11] = (algebraic[10]-states[11])/algebraic[18]
    algebraic[12] = 1.00000/(1.00000+exp((states[0]+25.0000)/-20.0000))
    algebraic[19] = (1.00000/(1.00000+exp((states[0]+66.0000)/-26.0000)))*150.000
    rates[13] = (algebraic[12]-states[13])/algebraic[19]
    algebraic[21] = 0.500000*constants[38]*log(constants[9]/states[1])
    algebraic[22] = constants[23]*(states[3]*states[2]*states[4])*(states[0]-algebraic[21])
    algebraic[24] = 0.500000*constants[38]*log(constants[9]/states[1])
    algebraic[25] = constants[25]*(states[6]*states[5])*(states[0]-algebraic[24])
    algebraic[23] = constants[24]*(power(states[1]*1.00000, 1.34000))
    rates[1] = (-1.00000*algebraic[22]+-1.00000*algebraic[25])/(2.00000*0.00100000*constants[4]*constants[14])+-1.00000*algebraic[23]
    algebraic[30] = constants[29]*(states[10]*states[9])*(states[0]-constants[48])
    algebraic[29] = constants[28]*(states[7]*states[8])*(states[0]-constants[47])
    algebraic[31] = constants[30]*(states[11]*states[12])*(states[0]-constants[50])
    algebraic[26] = 1.00000/(1.00000+exp(states[0]/-17.0000-2.00000*log(states[1]/0.00100000)))
    algebraic[27] = (constants[26]+constants[36])*algebraic[26]*(states[0]-constants[44])
    algebraic[32] = 1.00000/(1.00000+power(states[1]/0.000200000, -4.00000))
    algebraic[33] = constants[32]*states[13]*algebraic[32]*constants[39]*(states[0]-constants[31])
    algebraic[28] = constants[27]*(states[0]-constants[45])
    algebraic[0] = custom_piecewise([greater(voi , constants[17]*1.00000) & less_equal(voi , constants[17]*2.00000), constants[17]*1.00000 , greater(voi , constants[17]*2.00000) & less_equal(voi , constants[17]*3.00000), constants[17]*2.00000 , greater(voi , constants[17]*3.00000) & less_equal(voi , constants[17]*4.00000), constants[17]*3.00000 , greater(voi , constants[17]*4.00000) & less_equal(voi , constants[17]*5.00000), constants[17]*4.00000 , True, 0.00000])
    algebraic[13] = voi-(algebraic[0]+constants[19])
    algebraic[20] = custom_piecewise([less(algebraic[13] , constants[19]), constants[1]*constants[18] , greater_equal(algebraic[13] , constants[19]) & less_equal(algebraic[13] , constants[20]), constants[1]*constants[18]*(1.00000/(1.00000+exp((algebraic[13]-8000.00)/1000.00))) , greater(algebraic[13] , constants[20]) & less(algebraic[13] , constants[21]), constants[1]*constants[22]*(1.00000/(1.00000+exp((algebraic[13]-8000.00)/150.000))) , True, 0.00000])
    rates[0] = -1.00000*(1.00000/constants[13])*(algebraic[30]+algebraic[22]+algebraic[25]+algebraic[29]+algebraic[31]+algebraic[27]+algebraic[33]+algebraic[28]+-1.00000*algebraic[20])
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[1] = 1.00000/(1.00000+exp((states[0]+17.0000)/-4.30000))
    algebraic[2] = 1.00000/(1.00000+exp((states[0]+43.0000)/8.90000))
    algebraic[3] = 1.00000-1.00000/(1.00000+exp(((states[1]-8.99900e-05)-0.000214000)/-1.31000e-05))
    algebraic[4] = 1.00000/(1.00000+exp((states[0]+27.5000)/-10.9000))
    algebraic[6] = 1.00000/(1.00000+exp((states[0]+27.0000)/-5.00000))
    algebraic[11] = 0.100000+0.900000/(1.00000+exp((states[0]+65.0000)/6.20000))
    algebraic[5] = 1.00000/(1.00000+exp((states[0]+15.8000)/7.00000))
    algebraic[14] = constants[35]*(7.58000*exp(states[0]*0.00817000))
    algebraic[7] = 0.200000+0.800000/(1.00000+exp((states[0]+58.0000)/10.0000))
    algebraic[15] = constants[34]*(-707.000+1481.00*exp((states[0]+36.0000)/95.0000))
    algebraic[8] = 1.00000/(1.00000+exp((states[0]+47.0000)/-4.80000))
    algebraic[16] = constants[33]*(states[0]*-0.0170000*1.00000+0.440000)
    algebraic[9] = 1.00000/(1.00000+exp((states[0]+78.0000)/3.00000))
    algebraic[17] = constants[33]*(states[0]*-0.250000*1.00000+5.50000)
    algebraic[10] = 1.00000/(1.00000+exp((states[0]+26.5000)/-7.90000))
    algebraic[18] = constants[34]*(31.8000+175.000*exp(-0.500000*(power((states[0]+44.4000)/22.3000, 2.00000))))
    algebraic[12] = 1.00000/(1.00000+exp((states[0]+25.0000)/-20.0000))
    algebraic[19] = (1.00000/(1.00000+exp((states[0]+66.0000)/-26.0000)))*150.000
    algebraic[21] = 0.500000*constants[38]*log(constants[9]/states[1])
    algebraic[22] = constants[23]*(states[3]*states[2]*states[4])*(states[0]-algebraic[21])
    algebraic[24] = 0.500000*constants[38]*log(constants[9]/states[1])
    algebraic[25] = constants[25]*(states[6]*states[5])*(states[0]-algebraic[24])
    algebraic[23] = constants[24]*(power(states[1]*1.00000, 1.34000))
    algebraic[30] = constants[29]*(states[10]*states[9])*(states[0]-constants[48])
    algebraic[29] = constants[28]*(states[7]*states[8])*(states[0]-constants[47])
    algebraic[31] = constants[30]*(states[11]*states[12])*(states[0]-constants[50])
    algebraic[26] = 1.00000/(1.00000+exp(states[0]/-17.0000-2.00000*log(states[1]/0.00100000)))
    algebraic[27] = (constants[26]+constants[36])*algebraic[26]*(states[0]-constants[44])
    algebraic[32] = 1.00000/(1.00000+power(states[1]/0.000200000, -4.00000))
    algebraic[33] = constants[32]*states[13]*algebraic[32]*constants[39]*(states[0]-constants[31])
    algebraic[28] = constants[27]*(states[0]-constants[45])
    algebraic[0] = custom_piecewise([greater(voi , constants[17]*1.00000) & less_equal(voi , constants[17]*2.00000), constants[17]*1.00000 , greater(voi , constants[17]*2.00000) & less_equal(voi , constants[17]*3.00000), constants[17]*2.00000 , greater(voi , constants[17]*3.00000) & less_equal(voi , constants[17]*4.00000), constants[17]*3.00000 , greater(voi , constants[17]*4.00000) & less_equal(voi , constants[17]*5.00000), constants[17]*4.00000 , True, 0.00000])
    algebraic[13] = voi-(algebraic[0]+constants[19])
    algebraic[20] = custom_piecewise([less(algebraic[13] , constants[19]), constants[1]*constants[18] , greater_equal(algebraic[13] , constants[19]) & less_equal(algebraic[13] , constants[20]), constants[1]*constants[18]*(1.00000/(1.00000+exp((algebraic[13]-8000.00)/1000.00))) , greater(algebraic[13] , constants[20]) & less(algebraic[13] , constants[21]), constants[1]*constants[22]*(1.00000/(1.00000+exp((algebraic[13]-8000.00)/150.000))) , True, 0.00000])
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
        self.Ach = 0.00001
        self.Gcouple = 1.3
        self.T = 310
        self.T_exp = 297
        self.F = 96486
        self.R = 8314.4
        self.Q10Ca = 2.1
        self.Q10K = 1.365
        self.Q10Na = 2.45
        self.Ca_o = 2.5
        self.Na_o = 137
        self.K_o = 5.9
        self.Cl_o = 134
        self.Cm_SM = 77
        self.Vol_SM = 3500
        self.Na_i = 10
        self.K_i = 164
        self.period = 20000
        self.delta_VICC = 59
        self.t_ICCpeak = 98
        self.t_ICCplateau = 7582
        self.t_ICC_stimulus = 10000
        self.V_decay = 37.25
        self.G_max_Ltype = 65
        self.J_max_CaSR = 0.31705
        self.G_max_LVA = 0.18
        self.G_max_BK = 45.7
        self.G_max_bk = 0.0144
        self.G_max_kr_SM = 35
        self.G_max_Na_SM = 3
        self.G_max_ka_SM = 9
        self.E_NSCC = -28
        self.G_max_NSCC_SM = 50

    def to_dict(self):
        return {
            "Ach": self.Ach,
            "Gcouple": self.Gcouple,
            "T": self.T,
            "T_exp": self.T_exp,
            "F": self.F,
            "R": self.R,
            "Q10Ca": self.Q10Ca,
            "Q10K": self.Q10K,
            "Q10Na": self.Q10Na,
            "Ca_o": self.Ca_o,
            "Na_o": self.Na_o,
            "K_o": self.K_o,
            "Cl_o": self.Cl_o,
            "Cm_SM": self.Cm_SM,
            "Vol_SM": self.Vol_SM,
            "Na_i": self.Na_i,
            "K_i": self.K_i,
            "period": self.period,
            "delta_VICC": self.delta_VICC,
            "t_ICCpeak": self.t_ICCpeak,
            "t_ICCplateau": self.t_ICCplateau,
            "t_ICC_stimulus": self.t_ICC_stimulus,
            "V_decay": self.V_decay,
            "G_max_Ltype": self.G_max_Ltype,
            "J_max_CaSR": self.J_max_CaSR,
            "G_max_LVA": self.G_max_LVA,
            "G_max_BK": self.G_max_BK,
            "G_max_bk": self.G_max_bk,
            "G_max_kr_SM": self.G_max_kr_SM,
            "G_max_Na_SM": self.G_max_Na_SM,
            "G_max_ka_SM": self.G_max_ka_SM,
            "E_NSCC": self.E_NSCC,
            "G_max_NSCC_SM": self.G_max_NSCC_SM,
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
        y0=[-69.75, 0.00008, 0.0, 0.95, 1.0, 0.02, 0.99, 0.0, 0.82, 0.005, 0.05787, 0.00414, 0.72, 0.0],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "corrias_buist_2007"
        self.curve_names = [
            "Vm_SM",
            "Ca_i",
            "d_Ltype_SM",
            "f_Ltype_SM",
            "f_ca_Ltype_SM",
            "d_LVA_SM",
            "f_LVA_SM",
            "xr1_SM",
            "xr2_SM",
            "m_Na_SM",
            "h_Na_SM",
            "xa1_SM",
            "xa2_SM",
            "m_NSCC_SM",
        ]
        self.state_names = ['Vm_SM', 'Ca_i', 'd_Ltype_SM', 'f_Ltype_SM', 'f_ca_Ltype_SM', 'd_LVA_SM', 'f_LVA_SM', 'xr1_SM', 'xr2_SM', 'm_Na_SM', 'h_Na_SM', 'xa1_SM', 'xa2_SM', 'm_NSCC_SM']
        self.algebraic_names = ['stim_start', 'd_inf_Ltype_SM', 'f_inf_Ltype_SM', 'f_ca_inf_Ltype_SM', 'd_inf_LVA_SM', 'f_inf_LVA_SM', 'xr1_inf_SM', 'xr2_inf_SM', 'm_inf_Na', 'h_inf_Na', 'xa1_inf_SM', 'xa2_inf_SM', 'm_inf_NSCC_SM', 'local_time', 'tau_f_LVA_SM', 'tau_xr2_SM', 'tau_m_Na', 'tau_h_Na', 'tau_xa1_SM', 'tau_m_NSCC_SM', 'I_stim', 'E_Ca', 'I_Ltype_SM', 'J_CaSR_SM', 'E_Ca_1', 'I_LVA_SM', 'd_BK_SM', 'I_BK_SM', 'I_bk_SM', 'I_kr_SM', 'I_Na_SM', 'I_ka_SM', 'f_ca_NSCC_SM', 'I_NSCC_SM']
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
        c[0] = p.Ach
        c[1] = p.Gcouple
        c[2] = p.T
        c[3] = p.T_exp
        c[4] = p.F
        c[5] = p.R
        c[6] = p.Q10Ca
        c[7] = p.Q10K
        c[8] = p.Q10Na
        c[9] = p.Ca_o
        c[10] = p.Na_o
        c[11] = p.K_o
        c[12] = p.Cl_o
        c[13] = p.Cm_SM
        c[14] = p.Vol_SM
        c[15] = p.Na_i
        c[16] = p.K_i
        c[17] = p.period
        c[18] = p.delta_VICC
        c[19] = p.t_ICCpeak
        c[20] = p.t_ICCplateau
        c[21] = p.t_ICC_stimulus
        c[22] = p.V_decay
        c[23] = p.G_max_Ltype
        c[24] = p.J_max_CaSR
        c[25] = p.G_max_LVA
        c[26] = p.G_max_BK
        c[27] = p.G_max_bk
        c[28] = p.G_max_kr_SM
        c[29] = p.G_max_Na_SM
        c[30] = p.G_max_ka_SM
        c[31] = p.E_NSCC
        c[32] = p.G_max_NSCC_SM

        # derived constants
        c[33] = power(c[8], (c[2]-c[3])/10.0000)
        c[34] = power(c[7], (c[2]-c[3])/10.0000)
        c[35] = power(c[6], (c[2]-c[3])/10.0000)
        c[36] = 1.10000*(c[2]-c[3])
        c[37] = c[4]/(c[5]*c[2])
        c[38] = (c[5]*c[2])/c[4]
        c[39] = 1.00000/(1.00000+0.0100000/c[0])
        c[40] = c[35]*0.470000
        c[41] = c[35]*86.0000
        c[42] = c[35]*2.00000
        c[43] = c[35]*3.00000
        c[44] = c[38]*log(c[11]/c[16])
        c[45] = c[38]*log(c[11]/c[16])
        c[46] = c[34]*80.0000
        c[47] = c[38]*log(c[11]/c[16])
        c[48] = c[38]*log(c[10]/c[15])
        c[49] = c[34]*90.0000
        c[50] = c[38]*log(c[11]/c[16])

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
