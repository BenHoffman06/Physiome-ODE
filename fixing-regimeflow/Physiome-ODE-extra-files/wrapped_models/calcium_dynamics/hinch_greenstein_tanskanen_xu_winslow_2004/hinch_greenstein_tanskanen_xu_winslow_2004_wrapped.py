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


# =========================
# Auto-generated wrapper
# =========================
import numpy as np
from scipy.integrate import odeint


class Parameters:
    def __init__(self):
        self.V_myo = 25.84e3
        self.V_SR = 2.098e3
        self.A_cap = 1.534e4
        self.R = 8314.5
        self.T = 295
        self.F = 96487
        self.g_D = 0.065
        self.J_R = 0.02
        self.J_L = 9.13e-4
        self.N = 50000
        self.Ca_o = 1
        self.V_L = -2
        self.del_VL = 7
        self.phi_L = 2.35
        self.t_L = 1
        self.tau_L = 650
        self.tau_R = 2.43
        self.phi_R = 0.05
        self.theta_R = 0.012
        self.K_RyR = 41e-3
        self.K_L = 0.22e-3
        self.a = 0.0625
        self.b = 14
        self.c = 0.01
        self.d = 100
        self.K_mNa = 87.5
        self.K_mCa = 1.38
        self.eta = 0.35
        self.k_sat = 0.1
        self.g_NCX = 38.5e-3
        self.Na_i = 10
        self.Na_o = 140
        self.g_SERCA = 0.45e-3
        self.K_SERCA = 0.5e-3
        self.g_pCa = 0.0035e-3
        self.K_mpCa = 0.5e-3
        self.g_CaB = 2.6875e-8
        self.g_SRl = 1.8951e-5
        self.k_m_TRPN = 0.04
        self.k_p_TRPN = 0.04e3
        self.B_TRPN = 70e-3
        self.k_CMDN = 2.382e-3
        self.B_CMDN = 50e-3

    def to_dict(self):
        return {
            "V_myo": self.V_myo,
            "V_SR": self.V_SR,
            "A_cap": self.A_cap,
            "R": self.R,
            "T": self.T,
            "F": self.F,
            "g_D": self.g_D,
            "J_R": self.J_R,
            "J_L": self.J_L,
            "N": self.N,
            "Ca_o": self.Ca_o,
            "V_L": self.V_L,
            "del_VL": self.del_VL,
            "phi_L": self.phi_L,
            "t_L": self.t_L,
            "tau_L": self.tau_L,
            "tau_R": self.tau_R,
            "phi_R": self.phi_R,
            "theta_R": self.theta_R,
            "K_RyR": self.K_RyR,
            "K_L": self.K_L,
            "a": self.a,
            "b": self.b,
            "c": self.c,
            "d": self.d,
            "K_mNa": self.K_mNa,
            "K_mCa": self.K_mCa,
            "eta": self.eta,
            "k_sat": self.k_sat,
            "g_NCX": self.g_NCX,
            "Na_i": self.Na_i,
            "Na_o": self.Na_o,
            "g_SERCA": self.g_SERCA,
            "K_SERCA": self.K_SERCA,
            "g_pCa": self.g_pCa,
            "K_mpCa": self.K_mpCa,
            "g_CaB": self.g_CaB,
            "g_SRl": self.g_SRl,
            "k_m_TRPN": self.k_m_TRPN,
            "k_p_TRPN": self.k_p_TRPN,
            "B_TRPN": self.B_TRPN,
            "k_CMDN": self.k_CMDN,
            "B_CMDN": self.B_CMDN,
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
        y0=[0.0001, 700e-3, 0.98859, 0.0087302, 0.0026566, 0.0636364],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "hinch_greenstein_tanskanen_xu_winslow_2004"
        self.curve_names = [
            "Ca_i",
            "Ca_SR",
            "z_1",
            "z_2",
            "z_3",
            "TRPN",
        ]
        self.state_names = ['Ca_i', 'Ca_SR', 'z_1', 'z_2', 'z_3', 'TRPN']
        self.algebraic_names = ['V', 'C_cc', 'CaSR_plot', 'FVRT', 'FVRT_Ca', 'expVL', 'C_oo', 'alpha_p', 'beta_pcc', 'epsilon_pcc', 'epsilon_m', 'mu_pcc', 'mu_mcc', 'C_co', 'epsilon_pco', 'C_oc', 'beta_poc', 'mu_poc', 'mu_moc', 'J_Rco', 'J_Roo', 'J_Loc', 'J_Loo', 'denom', 'y_oc', 'y_co', 'y_oo', 'y_cc', 'J_R1', 'y_ci', 'r_1', 'J_R3', 'y_oi', 'r_2', 'I_RyR', 'y_ic', 'r_3', 'J_L1', 'y_io', 'r_4', 'J_L2', 'y_ii', 'r_5', 'I_LCC', 'r_6', 'I_NaCa', 'r_7', 'I_SERCA', 'r_8', 'I_pCa', 'z_4', 'E_Ca', 'I_CaB', 'I_SR', 'I_TRPN', 'beta_CMDN']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 46
        p = self.params

        # direct mapping
        c[0] = p.V_myo
        c[1] = p.V_SR
        c[2] = p.A_cap
        c[3] = p.R
        c[4] = p.T
        c[5] = p.F
        c[6] = p.g_D
        c[7] = p.J_R
        c[8] = p.J_L
        c[9] = p.N
        c[10] = p.Ca_o
        c[11] = p.V_L
        c[12] = p.del_VL
        c[13] = p.phi_L
        c[14] = p.t_L
        c[15] = p.tau_L
        c[16] = p.tau_R
        c[17] = p.phi_R
        c[18] = p.theta_R
        c[19] = p.K_RyR
        c[20] = p.K_L
        c[21] = p.a
        c[22] = p.b
        c[23] = p.c
        c[24] = p.d
        c[25] = p.K_mNa
        c[26] = p.K_mCa
        c[27] = p.eta
        c[28] = p.k_sat
        c[29] = p.g_NCX
        c[30] = p.Na_i
        c[31] = p.Na_o
        c[32] = p.g_SERCA
        c[33] = p.K_SERCA
        c[34] = p.g_pCa
        c[35] = p.K_mpCa
        c[36] = p.g_CaB
        c[37] = p.g_SRl
        c[38] = p.k_m_TRPN
        c[39] = p.k_p_TRPN
        c[40] = p.B_TRPN
        c[41] = p.k_CMDN
        c[42] = p.B_CMDN

        # derived constants
        c[43] = 1.17000*c[14]
        c[44] = c[13]/c[14]
        c[45] = c[17]/c[43]

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
