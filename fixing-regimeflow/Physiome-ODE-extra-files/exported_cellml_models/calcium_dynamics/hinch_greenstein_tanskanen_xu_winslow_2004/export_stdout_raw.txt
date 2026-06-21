# Size of variable arrays:
sizeAlgebraic = 56
sizeStates = 6
sizeConstants = 46
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (ms)"
    legend_constants[0] = "V_myo in component cell_geometry (um3)"
    legend_constants[1] = "V_SR in component cell_geometry (um3)"
    legend_constants[2] = "A_cap in component cell_geometry (um2)"
    legend_algebraic[0] = "V in component membrane (mV)"
    legend_constants[3] = "R in component membrane (mJ_per_mole_K)"
    legend_constants[4] = "T in component membrane (kelvin)"
    legend_constants[5] = "F in component membrane (C_per_mole)"
    legend_algebraic[3] = "FVRT in component membrane (dimensionless)"
    legend_algebraic[4] = "FVRT_Ca in component membrane (dimensionless)"
    legend_constants[6] = "g_D in component CaRU (um3_per_ms)"
    legend_constants[7] = "J_R in component CaRU (um3_per_ms)"
    legend_constants[8] = "J_L in component CaRU (um3_per_ms)"
    legend_constants[9] = "N in component CaRU (dimensionless)"
    legend_states[0] = "Ca_i in component intracellular_ion_concentrations (mM)"
    legend_constants[10] = "Ca_o in component extracellular_ion_concentrations (mM)"
    legend_states[1] = "Ca_SR in component intracellular_ion_concentrations (mM)"
    legend_algebraic[34] = "I_RyR in component RyR_current (mM_per_ms)"
    legend_algebraic[43] = "I_LCC in component LCC_current (mM_per_ms)"
    legend_algebraic[15] = "C_oc in component DS_Calcium_Concentrations (mM)"
    legend_algebraic[13] = "C_co in component DS_Calcium_Concentrations (mM)"
    legend_constants[11] = "V_L in component CaRU_Transitions (mV)"
    legend_constants[12] = "del_VL in component CaRU_Transitions (mV)"
    legend_constants[13] = "phi_L in component CaRU_Transitions (dimensionless)"
    legend_constants[14] = "t_L in component CaRU_Transitions (ms)"
    legend_constants[15] = "tau_L in component CaRU_Transitions (ms)"
    legend_constants[43] = "t_R in component CaRU_Transitions (ms)"
    legend_constants[16] = "tau_R in component CaRU_Transitions (ms)"
    legend_constants[17] = "phi_R in component CaRU_Transitions (dimensionless)"
    legend_constants[18] = "theta_R in component CaRU_Transitions (dimensionless)"
    legend_constants[19] = "K_RyR in component CaRU_Transitions (mM)"
    legend_constants[20] = "K_L in component CaRU_Transitions (mM)"
    legend_constants[21] = "a in component CaRU_Transitions (dimensionless)"
    legend_constants[22] = "b in component CaRU_Transitions (dimensionless)"
    legend_constants[23] = "c in component CaRU_Transitions (dimensionless)"
    legend_constants[24] = "d in component CaRU_Transitions (dimensionless)"
    legend_algebraic[5] = "expVL in component CaRU_Transitions (dimensionless)"
    legend_algebraic[7] = "alpha_p in component CaRU_Transitions (per_ms)"
    legend_constants[44] = "alpha_m in component CaRU_Transitions (per_ms)"
    legend_algebraic[16] = "beta_poc in component CaRU_Transitions (per_ms)"
    legend_algebraic[8] = "beta_pcc in component CaRU_Transitions (per_ms)"
    legend_constants[45] = "beta_m in component CaRU_Transitions (per_ms)"
    legend_algebraic[14] = "epsilon_pco in component CaRU_Transitions (per_ms)"
    legend_algebraic[9] = "epsilon_pcc in component CaRU_Transitions (per_ms)"
    legend_algebraic[10] = "epsilon_m in component CaRU_Transitions (per_ms)"
    legend_algebraic[17] = "mu_poc in component CaRU_Transitions (per_ms)"
    legend_algebraic[11] = "mu_pcc in component CaRU_Transitions (per_ms)"
    legend_algebraic[18] = "mu_moc in component CaRU_Transitions (per_ms)"
    legend_algebraic[12] = "mu_mcc in component CaRU_Transitions (per_ms)"
    legend_algebraic[1] = "C_cc in component DS_Calcium_Concentrations (mM)"
    legend_algebraic[6] = "C_oo in component DS_Calcium_Concentrations (mM)"
    legend_algebraic[22] = "J_Loo in component LCC_and_RyR_fluxes (um3_mM_per_ms)"
    legend_algebraic[21] = "J_Loc in component LCC_and_RyR_fluxes (um3_mM_per_ms)"
    legend_algebraic[19] = "J_Rco in component LCC_and_RyR_fluxes (um3_mM_per_ms)"
    legend_algebraic[20] = "J_Roo in component LCC_and_RyR_fluxes (um3_mM_per_ms)"
    legend_algebraic[23] = "denom in component CaRU_states (per_ms3)"
    legend_algebraic[24] = "y_oc in component CaRU_states (dimensionless)"
    legend_algebraic[25] = "y_co in component CaRU_states (dimensionless)"
    legend_algebraic[26] = "y_oo in component CaRU_states (dimensionless)"
    legend_algebraic[27] = "y_cc in component CaRU_states (dimensionless)"
    legend_algebraic[29] = "y_ci in component CaRU_states (dimensionless)"
    legend_algebraic[32] = "y_oi in component CaRU_states (dimensionless)"
    legend_algebraic[35] = "y_ic in component CaRU_states (dimensionless)"
    legend_algebraic[38] = "y_io in component CaRU_states (dimensionless)"
    legend_algebraic[41] = "y_ii in component CaRU_states (dimensionless)"
    legend_algebraic[30] = "r_1 in component CaRU_reduced_states (per_ms)"
    legend_algebraic[33] = "r_2 in component CaRU_reduced_states (per_ms)"
    legend_algebraic[36] = "r_3 in component CaRU_reduced_states (per_ms)"
    legend_algebraic[39] = "r_4 in component CaRU_reduced_states (per_ms)"
    legend_algebraic[42] = "r_5 in component CaRU_reduced_states (per_ms)"
    legend_algebraic[44] = "r_6 in component CaRU_reduced_states (per_ms)"
    legend_algebraic[46] = "r_7 in component CaRU_reduced_states (per_ms)"
    legend_algebraic[48] = "r_8 in component CaRU_reduced_states (per_ms)"
    legend_states[2] = "z_1 in component CaRU_reduced_states (dimensionless)"
    legend_states[3] = "z_2 in component CaRU_reduced_states (dimensionless)"
    legend_states[4] = "z_3 in component CaRU_reduced_states (dimensionless)"
    legend_algebraic[50] = "z_4 in component CaRU_reduced_states (dimensionless)"
    legend_algebraic[28] = "J_R1 in component RyR_current (um3_mM_per_ms)"
    legend_algebraic[31] = "J_R3 in component RyR_current (um3_mM_per_ms)"
    legend_algebraic[37] = "J_L1 in component LCC_current (um3_mM_per_ms)"
    legend_algebraic[40] = "J_L2 in component LCC_current (um3_mM_per_ms)"
    legend_constants[25] = "K_mNa in component Na_Ca_Exchanger (mM)"
    legend_constants[26] = "K_mCa in component Na_Ca_Exchanger (mM)"
    legend_constants[27] = "eta in component Na_Ca_Exchanger (dimensionless)"
    legend_constants[28] = "k_sat in component Na_Ca_Exchanger (dimensionless)"
    legend_constants[29] = "g_NCX in component Na_Ca_Exchanger (mM_per_ms)"
    legend_constants[30] = "Na_i in component intracellular_ion_concentrations (mM)"
    legend_constants[31] = "Na_o in component extracellular_ion_concentrations (mM)"
    legend_algebraic[45] = "I_NaCa in component Na_Ca_Exchanger (mM_per_ms)"
    legend_constants[32] = "g_SERCA in component SERCA (mM_per_ms)"
    legend_constants[33] = "K_SERCA in component SERCA (mM)"
    legend_algebraic[47] = "I_SERCA in component SERCA (mM_per_ms)"
    legend_constants[34] = "g_pCa in component Sarcolemmal_Ca_pump (mM_per_ms)"
    legend_constants[35] = "K_mpCa in component Sarcolemmal_Ca_pump (mM)"
    legend_algebraic[49] = "I_pCa in component Sarcolemmal_Ca_pump (mM_per_ms)"
    legend_algebraic[51] = "E_Ca in component Background_Ca_current (mV)"
    legend_constants[36] = "g_CaB in component Background_Ca_current (mM_per_mV_ms)"
    legend_algebraic[52] = "I_CaB in component Background_Ca_current (mM_per_ms)"
    legend_constants[37] = "g_SRl in component SR_Ca_leak_current (per_ms)"
    legend_algebraic[53] = "I_SR in component SR_Ca_leak_current (mM_per_ms)"
    legend_constants[38] = "k_m_TRPN in component troponin_Ca_buffer (per_ms)"
    legend_constants[39] = "k_p_TRPN in component troponin_Ca_buffer (per_mM_ms)"
    legend_constants[40] = "B_TRPN in component troponin_Ca_buffer (mM)"
    legend_states[5] = "TRPN in component intracellular_ion_concentrations (mM)"
    legend_algebraic[54] = "I_TRPN in component troponin_Ca_buffer (mM_per_ms)"
    legend_constants[41] = "k_CMDN in component calmodulin_Ca_buffer (mM)"
    legend_constants[42] = "B_CMDN in component calmodulin_Ca_buffer (mM)"
    legend_algebraic[55] = "beta_CMDN in component calmodulin_Ca_buffer (dimensionless)"
    legend_algebraic[2] = "CaSR_plot in component intracellular_ion_concentrations (mM)"
    legend_rates[2] = "d/dt z_1 in component CaRU_reduced_states (dimensionless)"
    legend_rates[3] = "d/dt z_2 in component CaRU_reduced_states (dimensionless)"
    legend_rates[4] = "d/dt z_3 in component CaRU_reduced_states (dimensionless)"
    legend_rates[5] = "d/dt TRPN in component intracellular_ion_concentrations (mM)"
    legend_rates[0] = "d/dt Ca_i in component intracellular_ion_concentrations (mM)"
    legend_rates[1] = "d/dt Ca_SR in component intracellular_ion_concentrations (mM)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    constants[0] = 25.84e3
    constants[1] = 2.098e3
    constants[2] = 1.534e4
    constants[3] = 8314.5
    constants[4] = 295
    constants[5] = 96487
    constants[6] = 0.065
    constants[7] = 0.02
    constants[8] = 9.13e-4
    constants[9] = 50000
    states[0] = 0.0001
    constants[10] = 1
    states[1] = 700e-3
    constants[11] = -2
    constants[12] = 7
    constants[13] = 2.35
    constants[14] = 1
    constants[15] = 650
    constants[16] = 2.43
    constants[17] = 0.05
    constants[18] = 0.012
    constants[19] = 41e-3
    constants[20] = 0.22e-3
    constants[21] = 0.0625
    constants[22] = 14
    constants[23] = 0.01
    constants[24] = 100
    states[2] = 0.98859
    states[3] = 0.0087302
    states[4] = 0.0026566
    constants[25] = 87.5
    constants[26] = 1.38
    constants[27] = 0.35
    constants[28] = 0.1
    constants[29] = 38.5e-3
    constants[30] = 10
    constants[31] = 140
    constants[32] = 0.45e-3
    constants[33] = 0.5e-3
    constants[34] = 0.0035e-3
    constants[35] = 0.5e-3
    constants[36] = 2.6875e-8
    constants[37] = 1.8951e-5
    constants[38] = 0.04
    constants[39] = 0.04e3
    constants[40] = 70e-3
    states[5] = 0.0636364
    constants[41] = 2.382e-3
    constants[42] = 50e-3
    constants[43] = 1.17000*constants[14]
    constants[44] = constants[13]/constants[14]
    constants[45] = constants[17]/constants[43]
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[0] = custom_piecewise([greater_equal(voi , 0.00000) & less_equal(voi , 200.000), 0.00000 , True, -80.0000])
    algebraic[3] = (constants[5]*algebraic[0])/(constants[3]*constants[4])
    algebraic[4] = 2.00000*algebraic[3]
    algebraic[15] = custom_piecewise([greater(fabs(algebraic[4]) , 1.00000e-09), (states[0]+((constants[8]/constants[6])*constants[10]*algebraic[4]*exp(-algebraic[4]))/(1.00000-exp(-algebraic[4])))/(1.00000+((constants[8]/constants[6])*algebraic[4])/(1.00000-exp(-algebraic[4]))) , True, (states[0]+(constants[8]/constants[6])*constants[10])/(1.00000+constants[8]/constants[6])])
    algebraic[17] = (power(algebraic[15], 2.00000)+constants[23]*(power(constants[19], 2.00000)))/(constants[16]*(power(algebraic[15], 2.00000)+power(constants[19], 2.00000)))
    algebraic[11] = (power(states[0], 2.00000)+constants[23]*(power(constants[19], 2.00000)))/(constants[16]*(power(states[0], 2.00000)+power(constants[19], 2.00000)))
    algebraic[5] = exp((algebraic[0]-constants[11])/constants[12])
    algebraic[7] = algebraic[5]/(constants[14]*(algebraic[5]+1.00000))
    algebraic[8] = (power(states[0], 2.00000))/(constants[43]*(power(states[0], 2.00000)+power(constants[19], 2.00000)))
    algebraic[16] = (power(algebraic[15], 2.00000))/(constants[43]*(power(algebraic[15], 2.00000)+power(constants[19], 2.00000)))
    algebraic[23] = (algebraic[7]+constants[44])*((constants[44]+constants[45]+algebraic[16])*(constants[45]+algebraic[8])+algebraic[7]*(constants[45]+algebraic[16]))
    algebraic[24] = (algebraic[7]*constants[45]*(algebraic[7]+constants[44]+constants[45]+algebraic[8]))/algebraic[23]
    algebraic[27] = (constants[44]*constants[45]*(constants[44]+algebraic[7]+constants[45]+algebraic[16]))/algebraic[23]
    algebraic[30] = algebraic[24]*algebraic[17]+algebraic[27]*algebraic[11]
    algebraic[18] = (constants[18]*constants[24]*(power(algebraic[15], 2.00000)+constants[23]*(power(constants[19], 2.00000))))/(constants[16]*(constants[24]*(power(algebraic[15], 2.00000))+constants[23]*(power(constants[19], 2.00000))))
    algebraic[12] = (constants[18]*constants[24]*(power(states[0], 2.00000)+constants[23]*(power(constants[19], 2.00000))))/(constants[16]*(constants[24]*(power(states[0], 2.00000))+constants[23]*(power(constants[19], 2.00000))))
    algebraic[33] = (algebraic[7]*algebraic[18]+constants[44]*algebraic[12])/(algebraic[7]+constants[44])
    algebraic[13] = (states[0]+(constants[7]/constants[6])*states[1])/(1.00000+constants[7]/constants[6])
    algebraic[14] = (algebraic[13]*(algebraic[5]+constants[21]))/(constants[15]*constants[20]*(algebraic[5]+1.00000))
    algebraic[9] = (states[0]*(algebraic[5]+constants[21]))/(constants[15]*constants[20]*(algebraic[5]+1.00000))
    algebraic[25] = (constants[44]*(algebraic[8]*(constants[44]+constants[45]+algebraic[16])+algebraic[16]*algebraic[7]))/algebraic[23]
    algebraic[42] = algebraic[25]*algebraic[14]+algebraic[27]*algebraic[9]
    algebraic[10] = (constants[22]*(algebraic[5]+constants[21]))/(constants[15]*(constants[22]*algebraic[5]+constants[21]))
    algebraic[44] = algebraic[10]
    rates[2] = -(algebraic[30]+algebraic[42])*states[2]+algebraic[33]*states[3]+algebraic[44]*states[4]
    algebraic[46] = (constants[44]*algebraic[9])/(algebraic[7]+constants[44])
    algebraic[48] = algebraic[10]
    algebraic[50] = ((1.00000-states[2])-states[3])-states[4]
    rates[3] = (algebraic[30]*states[2]-(algebraic[33]+algebraic[46])*states[3])+algebraic[48]*algebraic[50]
    algebraic[36] = (constants[45]*algebraic[11])/(constants[45]+algebraic[8])
    algebraic[39] = algebraic[12]
    rates[4] = (algebraic[42]*states[2]-(algebraic[44]+algebraic[36])*states[4])+algebraic[39]*algebraic[50]
    algebraic[19] = (constants[7]*(states[1]-states[0]))/(1.00000+constants[7]/constants[6])
    algebraic[20] = custom_piecewise([greater(fabs(algebraic[4]) , 1.00000e-05), (constants[7]*((states[1]-states[0])+(((constants[8]/constants[6])*algebraic[4])/(1.00000-exp(-algebraic[4])))*(states[1]-constants[10]*exp(-algebraic[4]))))/(1.00000+constants[7]/constants[6]+((constants[8]/constants[6])*algebraic[4])/(1.00000-exp(-algebraic[4]))) , True, (constants[7]*((states[1]-states[0])+(((constants[8]/constants[6])*1.00000e-05)/(1.00000-exp(-1.00000e-05)))*(states[1]-constants[10]*exp(-1.00000e-05))))/(1.00000+constants[7]/constants[6]+((constants[8]/constants[6])*1.00000e-05)/(1.00000-exp(-1.00000e-05)))])
    algebraic[26] = (algebraic[7]*(algebraic[16]*(algebraic[7]+constants[45]+algebraic[8])+algebraic[8]*constants[44]))/algebraic[23]
    algebraic[28] = algebraic[26]*algebraic[20]+algebraic[19]*algebraic[25]
    algebraic[31] = (algebraic[19]*algebraic[8])/(constants[45]+algebraic[8])
    algebraic[34] = ((states[2]*algebraic[28]+states[4]*algebraic[31])*constants[9])/constants[0]
    algebraic[47] = (constants[32]*(power(states[0], 2.00000)))/(power(constants[33], 2.00000)+power(states[0], 2.00000))
    algebraic[53] = constants[37]*(states[1]-states[0])
    rates[1] = (constants[0]/constants[1])*((-algebraic[34]+algebraic[47])-algebraic[53])
    algebraic[54] = constants[38]*(constants[40]-states[5])-constants[39]*states[5]*states[0]
    rates[5] = algebraic[54]
    algebraic[22] = custom_piecewise([greater(fabs(algebraic[4]) , 1.00000e-05), (((constants[8]*algebraic[4])/(1.00000-exp(-algebraic[4])))*((constants[10]*exp(-algebraic[4])-states[0])+(constants[7]/constants[6])*(constants[10]*exp(-algebraic[4])-states[1])))/(1.00000+constants[7]/constants[6]+((constants[8]/constants[6])*algebraic[4])/(1.00000-exp(algebraic[4]))) , True, (((constants[8]*1.00000e-05)/(1.00000-exp(-1.00000e-05)))*((constants[10]*exp(-1.00000e-05)-states[0])+(constants[7]/constants[6])*(constants[10]*exp(-1.00000e-05)-states[1])))/(1.00000+constants[7]/constants[6]+((constants[8]/constants[6])*1.00000e-05)/(1.00000-exp(-1.00000e-05)))])
    algebraic[21] = custom_piecewise([greater(fabs(algebraic[4]) , 1.00000e-05), (((constants[8]*algebraic[4])/(1.00000-exp(-algebraic[4])))*(constants[10]*exp(-algebraic[4])-states[0]))/(1.00000+((constants[8]/constants[6])*algebraic[4])/(1.00000-exp(-algebraic[4]))) , True, (((constants[8]*1.00000e-05)/(1.00000-exp(-1.00000e-05)))*(constants[10]*exp(-1.00000e-05)-states[0]))/(1.00000+((constants[8]/constants[6])*1.00000e-05)/(1.00000-exp(-1.00000e-05)))])
    algebraic[37] = algebraic[22]*algebraic[26]+algebraic[21]*algebraic[24]
    algebraic[40] = (algebraic[21]*algebraic[7])/(algebraic[7]+constants[44])
    algebraic[43] = ((states[2]*algebraic[37]+states[3]*algebraic[40])*constants[9])/constants[0]
    algebraic[45] = (constants[29]*(exp(constants[27]*algebraic[3])*(power(constants[30], 3.00000))*constants[10]-exp((constants[27]-1.00000)*algebraic[3])*(power(constants[31], 3.00000))*states[0]))/((power(constants[31], 3.00000)+power(constants[25], 3.00000))*(constants[10]+constants[26])*(1.00000+constants[28]*exp((constants[27]-1.00000)*algebraic[3])))
    algebraic[49] = (constants[34]*states[0])/(constants[35]+states[0])
    algebraic[51] = ((constants[3]*constants[4])/(2.00000*constants[5]))*log(constants[10]/states[0])
    algebraic[52] = constants[36]*(algebraic[51]-algebraic[0])
    algebraic[55] = power(1.00000+(constants[41]*constants[42])/(power(constants[41]+states[0], 2.00000)), -1.00000)
    rates[0] = algebraic[55]*(((((algebraic[43]+algebraic[34])-algebraic[47])+algebraic[53]+algebraic[45])-algebraic[49])+algebraic[52]+algebraic[54])
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = custom_piecewise([greater_equal(voi , 0.00000) & less_equal(voi , 200.000), 0.00000 , True, -80.0000])
    algebraic[3] = (constants[5]*algebraic[0])/(constants[3]*constants[4])
    algebraic[4] = 2.00000*algebraic[3]
    algebraic[15] = custom_piecewise([greater(fabs(algebraic[4]) , 1.00000e-09), (states[0]+((constants[8]/constants[6])*constants[10]*algebraic[4]*exp(-algebraic[4]))/(1.00000-exp(-algebraic[4])))/(1.00000+((constants[8]/constants[6])*algebraic[4])/(1.00000-exp(-algebraic[4]))) , True, (states[0]+(constants[8]/constants[6])*constants[10])/(1.00000+constants[8]/constants[6])])
    algebraic[17] = (power(algebraic[15], 2.00000)+constants[23]*(power(constants[19], 2.00000)))/(constants[16]*(power(algebraic[15], 2.00000)+power(constants[19], 2.00000)))
    algebraic[11] = (power(states[0], 2.00000)+constants[23]*(power(constants[19], 2.00000)))/(constants[16]*(power(states[0], 2.00000)+power(constants[19], 2.00000)))
    algebraic[5] = exp((algebraic[0]-constants[11])/constants[12])
    algebraic[7] = algebraic[5]/(constants[14]*(algebraic[5]+1.00000))
    algebraic[8] = (power(states[0], 2.00000))/(constants[43]*(power(states[0], 2.00000)+power(constants[19], 2.00000)))
    algebraic[16] = (power(algebraic[15], 2.00000))/(constants[43]*(power(algebraic[15], 2.00000)+power(constants[19], 2.00000)))
    algebraic[23] = (algebraic[7]+constants[44])*((constants[44]+constants[45]+algebraic[16])*(constants[45]+algebraic[8])+algebraic[7]*(constants[45]+algebraic[16]))
    algebraic[24] = (algebraic[7]*constants[45]*(algebraic[7]+constants[44]+constants[45]+algebraic[8]))/algebraic[23]
    algebraic[27] = (constants[44]*constants[45]*(constants[44]+algebraic[7]+constants[45]+algebraic[16]))/algebraic[23]
    algebraic[30] = algebraic[24]*algebraic[17]+algebraic[27]*algebraic[11]
    algebraic[18] = (constants[18]*constants[24]*(power(algebraic[15], 2.00000)+constants[23]*(power(constants[19], 2.00000))))/(constants[16]*(constants[24]*(power(algebraic[15], 2.00000))+constants[23]*(power(constants[19], 2.00000))))
    algebraic[12] = (constants[18]*constants[24]*(power(states[0], 2.00000)+constants[23]*(power(constants[19], 2.00000))))/(constants[16]*(constants[24]*(power(states[0], 2.00000))+constants[23]*(power(constants[19], 2.00000))))
    algebraic[33] = (algebraic[7]*algebraic[18]+constants[44]*algebraic[12])/(algebraic[7]+constants[44])
    algebraic[13] = (states[0]+(constants[7]/constants[6])*states[1])/(1.00000+constants[7]/constants[6])
    algebraic[14] = (algebraic[13]*(algebraic[5]+constants[21]))/(constants[15]*constants[20]*(algebraic[5]+1.00000))
    algebraic[9] = (states[0]*(algebraic[5]+constants[21]))/(constants[15]*constants[20]*(algebraic[5]+1.00000))
    algebraic[25] = (constants[44]*(algebraic[8]*(constants[44]+constants[45]+algebraic[16])+algebraic[16]*algebraic[7]))/algebraic[23]
    algebraic[42] = algebraic[25]*algebraic[14]+algebraic[27]*algebraic[9]
    algebraic[10] = (constants[22]*(algebraic[5]+constants[21]))/(constants[15]*(constants[22]*algebraic[5]+constants[21]))
    algebraic[44] = algebraic[10]
    algebraic[46] = (constants[44]*algebraic[9])/(algebraic[7]+constants[44])
    algebraic[48] = algebraic[10]
    algebraic[50] = ((1.00000-states[2])-states[3])-states[4]
    algebraic[36] = (constants[45]*algebraic[11])/(constants[45]+algebraic[8])
    algebraic[39] = algebraic[12]
    algebraic[19] = (constants[7]*(states[1]-states[0]))/(1.00000+constants[7]/constants[6])
    algebraic[20] = custom_piecewise([greater(fabs(algebraic[4]) , 1.00000e-05), (constants[7]*((states[1]-states[0])+(((constants[8]/constants[6])*algebraic[4])/(1.00000-exp(-algebraic[4])))*(states[1]-constants[10]*exp(-algebraic[4]))))/(1.00000+constants[7]/constants[6]+((constants[8]/constants[6])*algebraic[4])/(1.00000-exp(-algebraic[4]))) , True, (constants[7]*((states[1]-states[0])+(((constants[8]/constants[6])*1.00000e-05)/(1.00000-exp(-1.00000e-05)))*(states[1]-constants[10]*exp(-1.00000e-05))))/(1.00000+constants[7]/constants[6]+((constants[8]/constants[6])*1.00000e-05)/(1.00000-exp(-1.00000e-05)))])
    algebraic[26] = (algebraic[7]*(algebraic[16]*(algebraic[7]+constants[45]+algebraic[8])+algebraic[8]*constants[44]))/algebraic[23]
    algebraic[28] = algebraic[26]*algebraic[20]+algebraic[19]*algebraic[25]
    algebraic[31] = (algebraic[19]*algebraic[8])/(constants[45]+algebraic[8])
    algebraic[34] = ((states[2]*algebraic[28]+states[4]*algebraic[31])*constants[9])/constants[0]
    algebraic[47] = (constants[32]*(power(states[0], 2.00000)))/(power(constants[33], 2.00000)+power(states[0], 2.00000))
    algebraic[53] = constants[37]*(states[1]-states[0])
    algebraic[54] = constants[38]*(constants[40]-states[5])-constants[39]*states[5]*states[0]
    algebraic[22] = custom_piecewise([greater(fabs(algebraic[4]) , 1.00000e-05), (((constants[8]*algebraic[4])/(1.00000-exp(-algebraic[4])))*((constants[10]*exp(-algebraic[4])-states[0])+(constants[7]/constants[6])*(constants[10]*exp(-algebraic[4])-states[1])))/(1.00000+constants[7]/constants[6]+((constants[8]/constants[6])*algebraic[4])/(1.00000-exp(algebraic[4]))) , True, (((constants[8]*1.00000e-05)/(1.00000-exp(-1.00000e-05)))*((constants[10]*exp(-1.00000e-05)-states[0])+(constants[7]/constants[6])*(constants[10]*exp(-1.00000e-05)-states[1])))/(1.00000+constants[7]/constants[6]+((constants[8]/constants[6])*1.00000e-05)/(1.00000-exp(-1.00000e-05)))])
    algebraic[21] = custom_piecewise([greater(fabs(algebraic[4]) , 1.00000e-05), (((constants[8]*algebraic[4])/(1.00000-exp(-algebraic[4])))*(constants[10]*exp(-algebraic[4])-states[0]))/(1.00000+((constants[8]/constants[6])*algebraic[4])/(1.00000-exp(-algebraic[4]))) , True, (((constants[8]*1.00000e-05)/(1.00000-exp(-1.00000e-05)))*(constants[10]*exp(-1.00000e-05)-states[0]))/(1.00000+((constants[8]/constants[6])*1.00000e-05)/(1.00000-exp(-1.00000e-05)))])
    algebraic[37] = algebraic[22]*algebraic[26]+algebraic[21]*algebraic[24]
    algebraic[40] = (algebraic[21]*algebraic[7])/(algebraic[7]+constants[44])
    algebraic[43] = ((states[2]*algebraic[37]+states[3]*algebraic[40])*constants[9])/constants[0]
    algebraic[45] = (constants[29]*(exp(constants[27]*algebraic[3])*(power(constants[30], 3.00000))*constants[10]-exp((constants[27]-1.00000)*algebraic[3])*(power(constants[31], 3.00000))*states[0]))/((power(constants[31], 3.00000)+power(constants[25], 3.00000))*(constants[10]+constants[26])*(1.00000+constants[28]*exp((constants[27]-1.00000)*algebraic[3])))
    algebraic[49] = (constants[34]*states[0])/(constants[35]+states[0])
    algebraic[51] = ((constants[3]*constants[4])/(2.00000*constants[5]))*log(constants[10]/states[0])
    algebraic[52] = constants[36]*(algebraic[51]-algebraic[0])
    algebraic[55] = power(1.00000+(constants[41]*constants[42])/(power(constants[41]+states[0], 2.00000)), -1.00000)
    algebraic[1] = states[0]
    algebraic[2] = (states[1]*constants[1])/constants[0]
    algebraic[6] = custom_piecewise([greater(fabs(algebraic[4]) , 1.00000e-09), (states[0]+(constants[7]/constants[6])*states[1]+((constants[8]/constants[6])*constants[10]*algebraic[4]*exp(-algebraic[4]))/(1.00000-exp(-algebraic[4])))/(1.00000+constants[7]/constants[6]+((constants[8]/constants[6])*algebraic[4])/(1.00000-exp(-algebraic[4]))) , True, (states[0]+(constants[7]/constants[6])*states[1]+(constants[8]/constants[6])*constants[10])/(1.00000+constants[7]/constants[6]+constants[8]/constants[6])])
    algebraic[29] = constants[44]/(algebraic[7]+constants[44])
    algebraic[32] = algebraic[7]/(algebraic[7]+constants[44])
    algebraic[35] = constants[45]/(algebraic[8]+constants[45])
    algebraic[38] = algebraic[8]/(algebraic[8]+constants[45])
    algebraic[41] = (((((((1.00000-algebraic[24])-algebraic[25])-algebraic[26])-algebraic[27])-algebraic[29])-algebraic[35])-algebraic[32])-algebraic[38]
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
