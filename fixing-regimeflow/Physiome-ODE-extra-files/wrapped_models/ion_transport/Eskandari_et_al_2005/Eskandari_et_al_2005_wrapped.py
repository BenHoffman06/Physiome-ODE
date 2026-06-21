# Size of variable arrays:
sizeAlgebraic = 43
sizeStates = 7
sizeConstants = 41
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (second)"
    legend_constants[0] = "k0_12 in component parameters (per_M2_per_second)"
    legend_constants[1] = "k0_21 in component parameters (per_second)"
    legend_constants[2] = "k0_23 in component parameters (per_M_per_second)"
    legend_constants[3] = "k0_32 in component parameters (per_second)"
    legend_constants[4] = "k0_34 in component parameters (per_second)"
    legend_constants[5] = "k0_43 in component parameters (per_second)"
    legend_constants[6] = "k0_45 in component parameters (per_second)"
    legend_constants[7] = "k0_54 in component parameters (per_M_per_second)"
    legend_constants[8] = "k0_25 in component parameters (per_second)"
    legend_constants[9] = "k0_52 in component parameters (per_second)"
    legend_constants[10] = "k0_56 in component parameters (per_second)"
    legend_constants[11] = "k0_65_f in component parameters (per_M2_per_second)"
    legend_constants[12] = "k0_61_f in component parameters (per_second)"
    legend_constants[13] = "k0_16_f in component parameters (per_second)"
    legend_constants[14] = "k0_65_r in component parameters (per_M2_per_second)"
    legend_constants[15] = "k0_61_r in component parameters (per_second)"
    legend_constants[16] = "k0_16_r in component parameters (per_second)"
    legend_constants[32] = "k0_65 in component parameters (per_M2_per_second)"
    legend_constants[33] = "k0_61 in component parameters (per_second)"
    legend_constants[34] = "k0_16 in component parameters (per_second)"
    legend_constants[17] = "delta in component parameters (dimensionless)"
    legend_constants[35] = "alpha_p in component parameters (dimensionless)"
    legend_constants[18] = "alpha_pp in component parameters (dimensionless)"
    legend_constants[19] = "N_C in component parameters (dimensionless)"
    legend_constants[20] = "N_Avo in component parameters (per_mol)"
    legend_constants[21] = "area in component parameters (um2)"
    legend_constants[36] = "C_T in component parameters (umol)"
    legend_constants[22] = "n in component parameters (dimensionless)"
    legend_constants[23] = "z_c in component parameters (dimensionless)"
    legend_constants[24] = "z_Na in component parameters (dimensionless)"
    legend_constants[25] = "F in component parameters (C_per_mol)"
    legend_constants[26] = "R in component parameters (J_per_K_per_mol)"
    legend_constants[27] = "T in component parameters (kelvin)"
    legend_states[0] = "V in component ion_concentrations (volt)"
    legend_algebraic[0] = "mu in component parameters (dimensionless)"
    legend_constants[28] = "Na_o in component ion_concentrations (M)"
    legend_constants[29] = "Na_i in component ion_concentrations (M)"
    legend_constants[30] = "glucose_i in component ion_concentrations (M)"
    legend_constants[31] = "glucose_o in component ion_concentrations (M)"
    legend_algebraic[3] = "k_12 in component rate_constants (per_second)"
    legend_algebraic[4] = "k_21 in component rate_constants (per_second)"
    legend_constants[37] = "k_23 in component rate_constants (per_second)"
    legend_constants[38] = "k_32 in component rate_constants (per_second)"
    legend_algebraic[5] = "k_34 in component rate_constants (per_second)"
    legend_algebraic[6] = "k_43 in component rate_constants (per_second)"
    legend_constants[39] = "k_45 in component rate_constants (per_second)"
    legend_algebraic[14] = "k_54 in component rate_constants (per_second)"
    legend_algebraic[7] = "k_25 in component rate_constants (per_second)"
    legend_algebraic[12] = "k_52 in component rate_constants (per_second)"
    legend_algebraic[8] = "k_56 in component rate_constants (per_second)"
    legend_algebraic[9] = "k_65 in component rate_constants (per_second)"
    legend_algebraic[10] = "k_61 in component rate_constants (per_second)"
    legend_algebraic[11] = "k_16 in component rate_constants (per_second)"
    legend_algebraic[1] = "ks_12 in component rate_constants (per_M2_per_second)"
    legend_algebraic[13] = "k0_54_temp in component rate_constants (per_M_per_second)"
    legend_algebraic[2] = "k_52_temp in component rate_constants (per_second)"
    legend_states[1] = "C_1 in component kinetic_equations (umol)"
    legend_states[2] = "C_2 in component kinetic_equations (umol)"
    legend_states[3] = "C_3 in component kinetic_equations (umol)"
    legend_states[4] = "C_4 in component kinetic_equations (umol)"
    legend_states[5] = "C_5 in component kinetic_equations (umol)"
    legend_algebraic[15] = "C_6 in component kinetic_equations (umol)"
    legend_states[6] = "C_6_temp in component kinetic_equations (umol)"
    legend_algebraic[16] = "C1_sum in component king_altman_states (per_second5)"
    legend_algebraic[18] = "C2_sum in component king_altman_states (per_second5)"
    legend_algebraic[22] = "C3_sum in component king_altman_states (per_second5)"
    legend_algebraic[24] = "C4_sum in component king_altman_states (per_second5)"
    legend_algebraic[27] = "C5_sum in component king_altman_states (per_second5)"
    legend_algebraic[31] = "C6_sum in component king_altman_states (per_second5)"
    legend_algebraic[35] = "C_sum in component king_altman_states (per_second5)"
    legend_algebraic[36] = "C1 in component king_altman_states (umol)"
    legend_algebraic[37] = "C2 in component king_altman_states (umol)"
    legend_algebraic[38] = "C3 in component king_altman_states (umol)"
    legend_algebraic[39] = "C4 in component king_altman_states (umol)"
    legend_algebraic[40] = "C5 in component king_altman_states (umol)"
    legend_algebraic[41] = "C6 in component king_altman_states (umol)"
    legend_algebraic[19] = "I_NaGl_pSS in component NBC_current (uA)"
    legend_algebraic[42] = "I_NaGl_SS in component NBC_current (uA)"
    legend_algebraic[28] = "epsilon in component phenomonological_constants (per_second)"
    legend_algebraic[17] = "lambda in component phenomonological_constants (per_M3_per_second5)"
    legend_algebraic[20] = "chi in component phenomonological_constants (M)"
    legend_algebraic[26] = "alpha in component phenomonological_constants (M3)"
    legend_algebraic[23] = "beta in component phenomonological_constants (M2)"
    legend_algebraic[21] = "gamma in component phenomonological_constants (M3_per_second)"
    legend_algebraic[25] = "phi in component phenomonological_constants (M_per_second)"
    legend_algebraic[32] = "Imax_Na in component phenomonological_constants (uA)"
    legend_algebraic[33] = "Imax_gluc in component phenomonological_constants (uA)"
    legend_algebraic[29] = "Khalf_Na_sq in component phenomonological_constants (M2)"
    legend_algebraic[34] = "Khalf_Na in component phenomonological_constants (M)"
    legend_algebraic[30] = "Khalf_gluc in component phenomonological_constants (M)"
    legend_rates[0] = "d/dt V in component ion_concentrations (volt)"
    legend_rates[1] = "d/dt C_1 in component kinetic_equations (umol)"
    legend_rates[2] = "d/dt C_2 in component kinetic_equations (umol)"
    legend_rates[3] = "d/dt C_3 in component kinetic_equations (umol)"
    legend_rates[4] = "d/dt C_4 in component kinetic_equations (umol)"
    legend_rates[5] = "d/dt C_5 in component kinetic_equations (umol)"
    legend_rates[6] = "d/dt C_6_temp in component kinetic_equations (umol)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    constants[0] = 80000
    constants[1] = 500
    constants[2] = 1e5
    constants[3] = 20
    constants[4] = 50
    constants[5] = 50
    constants[6] = 800
    constants[7] = 1.219e4
    constants[8] = 0.3
    constants[9] = 9.1e-4
    constants[10] = 10
    constants[11] = 50
    constants[12] = 5
    constants[13] = 35
    constants[14] = 4500
    constants[15] = 3
    constants[16] = 350
    constants[17] = 0.7
    constants[18] = 0
    constants[19] = 3e6
    constants[20] = 6.022e23
    constants[21] = 1e6
    constants[22] = 2
    constants[23] = -2
    constants[24] = 1
    constants[25] = 96485.34
    constants[26] = 8.314
    constants[27] = 310
    states[0] = -150e-3
    constants[28] = 10e-3
    constants[29] = 500e-3
    constants[30] = 100e-3
    constants[31] = 0e-3
    states[1] = 0
    states[2] = 0
    states[3] = 0
    states[4] = 0
    states[5] = 0
    states[6] = 0
    constants[32] = custom_piecewise([less(constants[28] , 0.100000), constants[14] , True, constants[11]])
    constants[40] = 0.200000
    constants[33] = custom_piecewise([less(constants[28] , 0.100000), constants[15] , True, constants[12]])
    constants[34] = custom_piecewise([less(constants[28] , 0.100000), constants[16] , True, constants[13]])
    constants[35] = (1.00000-constants[17])-constants[18]
    constants[36] = (1.00000e+06*constants[19])/constants[20]
    constants[37] = constants[2]*constants[31]
    constants[38] = constants[3]
    constants[39] = constants[6]
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[0] = constants[40]
    algebraic[0] = (constants[25]*states[0])/(constants[26]*constants[27])
    algebraic[5] = constants[4]*exp((-(constants[23]+constants[22])*constants[17]*algebraic[0])/2.00000)
    algebraic[6] = constants[5]*exp(((constants[23]+constants[22])*constants[17]*algebraic[0])/2.00000)
    rates[3] = (constants[37]*states[2]+algebraic[6]*states[4])-(constants[38]+algebraic[5])*states[3]
    algebraic[8] = constants[10]*exp((-constants[22]*constants[24]*constants[18]*algebraic[0])/2.00000)
    algebraic[9] = constants[32]*(power(constants[29], constants[22]))*exp((constants[22]*constants[24]*constants[18]*algebraic[0])/2.00000)
    algebraic[10] = constants[33]*exp((constants[23]*constants[17]*algebraic[0])/2.00000)
    algebraic[11] = constants[34]*exp((-constants[23]*constants[17]*algebraic[0])/2.00000)
    rates[6] = (algebraic[11]*states[1]+algebraic[8]*states[5])-(algebraic[10]+algebraic[9])*states[6]
    algebraic[1] = constants[0]*exp((-constants[22]*constants[35]*algebraic[0])/2.00000)
    algebraic[3] = algebraic[1]*(power(constants[28], constants[22]))
    algebraic[4] = constants[1]*exp((constants[22]*constants[24]*constants[35]*algebraic[0])/2.00000)
    algebraic[7] = constants[8]*exp((-(constants[23]+constants[22])*constants[17]*algebraic[0])/2.00000)
    algebraic[12] = (constants[0]*algebraic[7]*constants[10]*constants[33])/(constants[1]*constants[34]*constants[32])
    rates[2] = (algebraic[3]*states[1]+constants[38]*states[3]+algebraic[12]*states[5])-(algebraic[4]+constants[37]+algebraic[7])*states[2]
    algebraic[13] = (constants[2]*algebraic[5]*constants[39]*algebraic[12])/(algebraic[6]*constants[38]*algebraic[7])
    algebraic[14] = algebraic[13]*constants[30]
    rates[4] = (algebraic[5]*states[3]+algebraic[14]*states[5])-(constants[39]+algebraic[6])*states[4]
    algebraic[15] = constants[36]-(states[1]+states[2]+states[3]+states[4]+states[5])
    rates[1] = (algebraic[4]*states[2]+algebraic[10]*algebraic[15])-(algebraic[3]+algebraic[11])*states[1]
    rates[5] = (constants[39]*states[4]+algebraic[9]*algebraic[15]+algebraic[7]*states[2])-(algebraic[14]+algebraic[12]+algebraic[8])*states[5]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = (constants[25]*states[0])/(constants[26]*constants[27])
    algebraic[5] = constants[4]*exp((-(constants[23]+constants[22])*constants[17]*algebraic[0])/2.00000)
    algebraic[6] = constants[5]*exp(((constants[23]+constants[22])*constants[17]*algebraic[0])/2.00000)
    algebraic[8] = constants[10]*exp((-constants[22]*constants[24]*constants[18]*algebraic[0])/2.00000)
    algebraic[9] = constants[32]*(power(constants[29], constants[22]))*exp((constants[22]*constants[24]*constants[18]*algebraic[0])/2.00000)
    algebraic[10] = constants[33]*exp((constants[23]*constants[17]*algebraic[0])/2.00000)
    algebraic[11] = constants[34]*exp((-constants[23]*constants[17]*algebraic[0])/2.00000)
    algebraic[1] = constants[0]*exp((-constants[22]*constants[35]*algebraic[0])/2.00000)
    algebraic[3] = algebraic[1]*(power(constants[28], constants[22]))
    algebraic[4] = constants[1]*exp((constants[22]*constants[24]*constants[35]*algebraic[0])/2.00000)
    algebraic[7] = constants[8]*exp((-(constants[23]+constants[22])*constants[17]*algebraic[0])/2.00000)
    algebraic[12] = (constants[0]*algebraic[7]*constants[10]*constants[33])/(constants[1]*constants[34]*constants[32])
    algebraic[13] = (constants[2]*algebraic[5]*constants[39]*algebraic[12])/(algebraic[6]*constants[38]*algebraic[7])
    algebraic[14] = algebraic[13]*constants[30]
    algebraic[15] = constants[36]-(states[1]+states[2]+states[3]+states[4]+states[5])
    algebraic[2] = constants[9]*exp(((constants[23]+constants[22])*constants[17]*algebraic[0])/2.00000)
    algebraic[16] = algebraic[4]*constants[38]*algebraic[6]*algebraic[14]*algebraic[9]+algebraic[4]*algebraic[5]*constants[39]*algebraic[12]*algebraic[9]+algebraic[4]*constants[38]*constants[39]*algebraic[12]*algebraic[9]+algebraic[4]*constants[38]*algebraic[6]*algebraic[12]*algebraic[9]+algebraic[7]*algebraic[5]*constants[39]*algebraic[8]*algebraic[10]+constants[37]*algebraic[5]*constants[39]*algebraic[8]*algebraic[10]+algebraic[4]*algebraic[5]*constants[39]*algebraic[8]*algebraic[10]+algebraic[7]*constants[38]*constants[39]*algebraic[8]*algebraic[10]+algebraic[4]*constants[38]*constants[39]*algebraic[8]*algebraic[10]+algebraic[7]*constants[38]*algebraic[6]*algebraic[8]*algebraic[10]+algebraic[4]*constants[38]*algebraic[6]*algebraic[8]*algebraic[10]+algebraic[4]*constants[38]*algebraic[6]*algebraic[14]*algebraic[10]+algebraic[4]*algebraic[5]*constants[39]*algebraic[12]*algebraic[10]+algebraic[4]*constants[38]*constants[39]*algebraic[12]*algebraic[10]+algebraic[4]*constants[38]*algebraic[6]*algebraic[12]*algebraic[10]
    algebraic[17] = algebraic[1]*constants[2]*algebraic[6]*algebraic[14]*algebraic[9]+algebraic[1]*constants[2]*algebraic[5]*algebraic[14]*algebraic[9]+algebraic[1]*constants[2]*constants[39]*algebraic[12]*algebraic[9]+algebraic[1]*constants[2]*algebraic[6]*algebraic[12]*algebraic[9]+algebraic[1]*constants[2]*algebraic[5]*algebraic[12]*algebraic[9]+algebraic[1]*constants[2]*algebraic[5]*constants[39]*algebraic[9]+algebraic[1]*constants[2]*constants[39]*algebraic[8]*algebraic[10]+algebraic[1]*constants[2]*algebraic[6]*algebraic[8]*algebraic[10]+algebraic[1]*constants[2]*algebraic[5]*algebraic[8]*algebraic[10]+algebraic[1]*constants[2]*algebraic[6]*algebraic[14]*algebraic[10]+algebraic[1]*constants[2]*algebraic[5]*algebraic[14]*algebraic[10]+algebraic[1]*constants[2]*constants[39]*algebraic[12]*algebraic[10]+algebraic[1]*constants[2]*algebraic[6]*algebraic[12]*algebraic[10]+algebraic[1]*constants[2]*algebraic[5]*algebraic[12]*algebraic[10]+algebraic[1]*constants[2]*algebraic[5]*constants[39]*algebraic[10]+algebraic[1]*constants[2]*algebraic[5]*constants[39]*algebraic[8]
    algebraic[18] = algebraic[11]*constants[38]*algebraic[6]*algebraic[14]*algebraic[9]+algebraic[3]*constants[38]*algebraic[6]*algebraic[14]*algebraic[9]+algebraic[11]*algebraic[5]*constants[39]*algebraic[12]*algebraic[9]+algebraic[3]*algebraic[5]*constants[39]*algebraic[12]*algebraic[9]+algebraic[11]*constants[38]*constants[39]*algebraic[12]*algebraic[9]+algebraic[3]*constants[38]*constants[39]*algebraic[12]*algebraic[9]+algebraic[11]*constants[38]*algebraic[6]*algebraic[12]*algebraic[9]+algebraic[3]*constants[38]*algebraic[6]*algebraic[12]*algebraic[9]+algebraic[3]*algebraic[5]*constants[39]*algebraic[8]*algebraic[10]+algebraic[3]*constants[38]*constants[39]*algebraic[8]*algebraic[10]+algebraic[3]*constants[38]*algebraic[6]*algebraic[8]*algebraic[10]+algebraic[3]*constants[38]*algebraic[6]*algebraic[14]*algebraic[10]+algebraic[3]*algebraic[5]*constants[39]*algebraic[12]*algebraic[10]+algebraic[3]*constants[38]*constants[39]*algebraic[12]*algebraic[10]+algebraic[3]*constants[38]*algebraic[6]*algebraic[12]*algebraic[10]
    algebraic[19] = -constants[25]*(constants[22]*constants[24]*constants[35]*(algebraic[3]*states[1]-algebraic[4]*states[2])+constants[23]*constants[17]*(algebraic[11]*states[1]-algebraic[10]*algebraic[15])+constants[22]*constants[24]*constants[18]*(algebraic[8]*states[5]-algebraic[9]*algebraic[15]))
    algebraic[20] = (1.00000/algebraic[17])*(algebraic[1]*constants[38]*algebraic[6]*algebraic[14]*algebraic[9]+algebraic[1]*algebraic[7]*algebraic[6]*algebraic[14]*algebraic[9]+algebraic[1]*algebraic[7]*algebraic[5]*algebraic[14]*algebraic[9]+algebraic[1]*algebraic[7]*constants[38]*algebraic[14]*algebraic[9]+algebraic[1]*algebraic[5]*constants[39]*algebraic[12]*algebraic[9]+algebraic[1]*constants[38]*constants[39]*algebraic[12]*algebraic[9]+algebraic[1]*constants[38]*algebraic[6]*algebraic[12]*algebraic[9]+algebraic[1]*algebraic[7]*algebraic[5]*constants[39]*algebraic[9]+algebraic[1]*algebraic[7]*constants[38]*constants[39]*algebraic[9]+algebraic[1]*algebraic[7]*constants[38]*algebraic[6]*algebraic[9]+algebraic[1]*algebraic[5]*constants[39]*algebraic[8]*algebraic[10]+algebraic[1]*constants[38]*constants[39]*algebraic[8]*algebraic[10]+algebraic[1]*constants[38]*algebraic[6]*algebraic[8]*algebraic[10]+algebraic[1]*constants[38]*algebraic[6]*algebraic[14]*algebraic[10]+algebraic[1]*algebraic[7]*algebraic[6]*algebraic[14]*algebraic[10]+algebraic[1]*algebraic[7]*algebraic[5]*algebraic[14]*algebraic[10]+algebraic[1]*algebraic[7]*constants[38]*algebraic[14]*algebraic[10]+algebraic[1]*algebraic[5]*constants[39]*algebraic[12]*algebraic[10]+algebraic[1]*constants[38]*constants[39]*algebraic[12]*algebraic[10]+algebraic[1]*constants[38]*algebraic[6]*algebraic[12]*algebraic[10]+algebraic[1]*algebraic[7]*algebraic[5]*constants[39]*algebraic[10]+algebraic[1]*algebraic[7]*constants[38]*constants[39]*algebraic[10]+algebraic[1]*algebraic[7]*constants[38]*algebraic[6]*algebraic[10]+algebraic[1]*algebraic[7]*algebraic[5]*constants[39]*algebraic[8]+algebraic[1]*algebraic[7]*constants[38]*constants[39]*algebraic[8]+algebraic[1]*algebraic[7]*constants[38]*algebraic[6]*algebraic[8])
    algebraic[21] = (1.00000/algebraic[17])*(algebraic[11]*algebraic[4]*constants[38]*algebraic[6]*algebraic[14]*algebraic[9]+algebraic[11]*algebraic[4]*algebraic[5]*constants[39]*algebraic[12]*algebraic[9]+algebraic[11]*algebraic[4]*constants[38]*constants[39]*algebraic[12]*algebraic[9]+algebraic[11]*algebraic[4]*constants[38]*algebraic[6]*algebraic[12]*algebraic[9])
    algebraic[22] = algebraic[11]*algebraic[7]*algebraic[6]*algebraic[14]*algebraic[9]+algebraic[3]*algebraic[7]*algebraic[6]*algebraic[14]*algebraic[9]+algebraic[11]*constants[37]*algebraic[6]*algebraic[14]*algebraic[9]+algebraic[3]*constants[37]*algebraic[6]*algebraic[14]*algebraic[9]+algebraic[11]*algebraic[4]*algebraic[6]*algebraic[14]*algebraic[9]+algebraic[11]*constants[37]*constants[39]*algebraic[12]*algebraic[9]+algebraic[3]*constants[37]*constants[39]*algebraic[12]*algebraic[9]+algebraic[11]*constants[37]*algebraic[6]*algebraic[12]*algebraic[9]+algebraic[3]*constants[37]*algebraic[6]*algebraic[12]*algebraic[9]+algebraic[3]*constants[37]*constants[39]*algebraic[8]*algebraic[10]+algebraic[3]*constants[37]*algebraic[6]*algebraic[8]*algebraic[10]+algebraic[3]*algebraic[7]*algebraic[6]*algebraic[14]*algebraic[10]+algebraic[3]*constants[37]*algebraic[6]*algebraic[14]*algebraic[10]+algebraic[3]*constants[37]*constants[39]*algebraic[12]*algebraic[10]+algebraic[3]*constants[37]*algebraic[6]*algebraic[12]*algebraic[10]
    algebraic[23] = (1.00000/algebraic[17])*(constants[2]*algebraic[11]*algebraic[6]*algebraic[14]*algebraic[9]+constants[2]*algebraic[11]*algebraic[5]*algebraic[14]*algebraic[9]+constants[2]*algebraic[11]*constants[39]*algebraic[12]*algebraic[9]+constants[2]*algebraic[11]*algebraic[6]*algebraic[12]*algebraic[9]+constants[2]*algebraic[11]*algebraic[5]*algebraic[12]*algebraic[9]+constants[2]*algebraic[11]*algebraic[5]*constants[39]*algebraic[9]+constants[2]*algebraic[5]*constants[39]*algebraic[8]*algebraic[10]+constants[2]*algebraic[11]*algebraic[5]*constants[39]*algebraic[8])
    algebraic[24] = algebraic[11]*algebraic[7]*algebraic[5]*algebraic[14]*algebraic[9]+algebraic[3]*algebraic[7]*algebraic[5]*algebraic[14]*algebraic[9]+algebraic[11]*constants[37]*algebraic[5]*algebraic[14]*algebraic[9]+algebraic[3]*constants[37]*algebraic[5]*algebraic[14]*algebraic[9]+algebraic[11]*algebraic[4]*algebraic[5]*algebraic[14]*algebraic[9]+algebraic[11]*algebraic[7]*constants[38]*algebraic[14]*algebraic[9]+algebraic[3]*algebraic[7]*constants[38]*algebraic[14]*algebraic[9]+algebraic[11]*algebraic[4]*constants[38]*algebraic[14]*algebraic[9]+algebraic[11]*constants[37]*algebraic[5]*algebraic[12]*algebraic[9]+algebraic[3]*constants[37]*algebraic[5]*algebraic[12]*algebraic[9]+algebraic[3]*constants[37]*algebraic[5]*algebraic[8]*algebraic[10]+algebraic[3]*algebraic[7]*algebraic[5]*algebraic[14]*algebraic[10]+algebraic[3]*constants[37]*algebraic[5]*algebraic[14]*algebraic[10]+algebraic[3]*algebraic[7]*constants[38]*algebraic[14]*algebraic[10]+algebraic[3]*constants[37]*algebraic[5]*algebraic[12]*algebraic[10]
    algebraic[25] = (1.00000/algebraic[17])*((-algebraic[1]*algebraic[7]*algebraic[5]*constants[39]*algebraic[8]*algebraic[10]-algebraic[1]*algebraic[7]*constants[38]*constants[39]*algebraic[8]*algebraic[10])-algebraic[1]*algebraic[7]*constants[38]*algebraic[6]*algebraic[8]*algebraic[10])
    algebraic[26] = (1.00000/algebraic[17])*(algebraic[4]*constants[38]*algebraic[6]*algebraic[14]*algebraic[9]+algebraic[11]*constants[38]*algebraic[6]*algebraic[14]*algebraic[9]+algebraic[11]*algebraic[7]*algebraic[6]*algebraic[14]*algebraic[9]+algebraic[11]*algebraic[4]*algebraic[6]*algebraic[14]*algebraic[9]+algebraic[11]*algebraic[7]*algebraic[5]*algebraic[14]*algebraic[9]+algebraic[11]*algebraic[4]*algebraic[5]*algebraic[14]*algebraic[9]+algebraic[11]*algebraic[7]*constants[38]*algebraic[14]*algebraic[9]+algebraic[11]*algebraic[4]*constants[38]*algebraic[14]*algebraic[9]+algebraic[4]*algebraic[5]*constants[39]*algebraic[12]*algebraic[9]+algebraic[11]*algebraic[5]*constants[39]*algebraic[12]*algebraic[9]+algebraic[4]*constants[38]*constants[39]*algebraic[12]*algebraic[9]+algebraic[11]*constants[38]*constants[39]*algebraic[12]*algebraic[9]+algebraic[4]*constants[38]*algebraic[6]*algebraic[12]*algebraic[9]+algebraic[11]*constants[38]*algebraic[6]*algebraic[12]*algebraic[9]+algebraic[11]*algebraic[7]*algebraic[5]*constants[39]*algebraic[9]+algebraic[11]*algebraic[4]*algebraic[5]*constants[39]*algebraic[9]+algebraic[11]*algebraic[7]*constants[38]*constants[39]*algebraic[9]+algebraic[11]*algebraic[4]*constants[38]*constants[39]*algebraic[9]+algebraic[11]*algebraic[7]*constants[38]*algebraic[6]*algebraic[9]+algebraic[11]*algebraic[4]*constants[38]*algebraic[6]*algebraic[9]+algebraic[7]*algebraic[5]*constants[39]*algebraic[8]*algebraic[10]+algebraic[4]*algebraic[5]*constants[39]*algebraic[8]*algebraic[10]+algebraic[7]*constants[38]*constants[39]*algebraic[8]*algebraic[10]+algebraic[4]*constants[38]*constants[39]*algebraic[8]*algebraic[10]+algebraic[7]*constants[38]*algebraic[6]*algebraic[8]*algebraic[10]+algebraic[4]*constants[38]*algebraic[6]*algebraic[8]*algebraic[10]+algebraic[4]*constants[38]*algebraic[6]*algebraic[14]*algebraic[10]+algebraic[4]*algebraic[5]*constants[39]*algebraic[12]*algebraic[10]+algebraic[4]*constants[38]*constants[39]*algebraic[12]*algebraic[10]+algebraic[4]*constants[38]*algebraic[6]*algebraic[12]*algebraic[10]+algebraic[11]*algebraic[7]*algebraic[5]*constants[39]*algebraic[8]+algebraic[11]*algebraic[4]*algebraic[5]*constants[39]*algebraic[8]+algebraic[11]*algebraic[7]*constants[38]*constants[39]*algebraic[8]+algebraic[11]*algebraic[4]*constants[38]*constants[39]*algebraic[8]+algebraic[11]*algebraic[7]*constants[38]*algebraic[6]*algebraic[8]+algebraic[11]*algebraic[4]*constants[38]*algebraic[6]*algebraic[8]+algebraic[11]*algebraic[4]*constants[38]*algebraic[6]*algebraic[14]+algebraic[11]*algebraic[4]*algebraic[5]*constants[39]*algebraic[12]+algebraic[11]*algebraic[4]*constants[38]*constants[39]*algebraic[12]+algebraic[11]*algebraic[4]*constants[38]*algebraic[6]*algebraic[12])
    algebraic[27] = algebraic[11]*algebraic[7]*algebraic[5]*constants[39]*algebraic[9]+algebraic[3]*algebraic[7]*algebraic[5]*constants[39]*algebraic[9]+algebraic[11]*constants[37]*algebraic[5]*constants[39]*algebraic[9]+algebraic[3]*constants[37]*algebraic[5]*constants[39]*algebraic[9]+algebraic[11]*algebraic[4]*algebraic[5]*constants[39]*algebraic[9]+algebraic[11]*algebraic[7]*constants[38]*constants[39]*algebraic[9]+algebraic[3]*algebraic[7]*constants[38]*constants[39]*algebraic[9]+algebraic[11]*algebraic[4]*constants[38]*constants[39]*algebraic[9]+algebraic[11]*algebraic[7]*constants[38]*algebraic[6]*algebraic[9]+algebraic[3]*algebraic[7]*constants[38]*algebraic[6]*algebraic[9]+algebraic[11]*algebraic[4]*constants[38]*algebraic[6]*algebraic[9]+algebraic[3]*algebraic[7]*algebraic[5]*constants[39]*algebraic[10]+algebraic[3]*constants[37]*algebraic[5]*constants[39]*algebraic[10]+algebraic[3]*algebraic[7]*constants[38]*constants[39]*algebraic[10]+algebraic[3]*algebraic[7]*constants[38]*algebraic[6]*algebraic[10]
    algebraic[28] = (1.00000/algebraic[17])*-algebraic[1]*constants[2]*algebraic[5]*constants[39]*algebraic[8]*algebraic[10]
    algebraic[29] = (algebraic[26]+algebraic[23]*constants[31])/(algebraic[20]+constants[31])
    algebraic[30] = (algebraic[26]+algebraic[20]*(power(constants[28], 2.00000)))/(algebraic[23]+power(constants[28], 2.00000))
    algebraic[31] = algebraic[11]*algebraic[7]*algebraic[5]*constants[39]*algebraic[8]+algebraic[3]*algebraic[7]*algebraic[5]*constants[39]*algebraic[8]+algebraic[11]*constants[37]*algebraic[5]*constants[39]*algebraic[8]+algebraic[3]*constants[37]*algebraic[5]*constants[39]*algebraic[8]+algebraic[11]*algebraic[4]*algebraic[5]*constants[39]*algebraic[8]+algebraic[11]*algebraic[7]*constants[38]*constants[39]*algebraic[8]+algebraic[3]*algebraic[7]*constants[38]*constants[39]*algebraic[8]+algebraic[11]*algebraic[4]*constants[38]*constants[39]*algebraic[8]+algebraic[11]*algebraic[7]*constants[38]*algebraic[6]*algebraic[8]+algebraic[3]*algebraic[7]*constants[38]*algebraic[6]*algebraic[8]+algebraic[11]*algebraic[4]*constants[38]*algebraic[6]*algebraic[8]+algebraic[11]*algebraic[4]*constants[38]*algebraic[6]*algebraic[14]+algebraic[11]*algebraic[4]*algebraic[5]*constants[39]*algebraic[12]+algebraic[11]*algebraic[4]*constants[38]*constants[39]*algebraic[12]+algebraic[11]*algebraic[4]*constants[38]*algebraic[6]*algebraic[12]
    algebraic[32] = (2.00000*constants[25]*constants[36]*(algebraic[25]+algebraic[28]*constants[31]))/(algebraic[20]+constants[31])
    algebraic[33] = (2.00000*constants[25]*constants[36]*algebraic[28]*(power(constants[28], 2.00000)))/(algebraic[23]+power(constants[28], 2.00000))
    algebraic[34] = power(algebraic[29], 1.0/2)
    algebraic[35] = algebraic[16]+algebraic[18]+algebraic[22]+algebraic[24]+algebraic[27]+algebraic[31]
    algebraic[36] = (constants[36]*algebraic[16])/algebraic[35]
    algebraic[37] = (constants[36]*algebraic[18])/algebraic[35]
    algebraic[38] = (constants[36]*algebraic[22])/algebraic[35]
    algebraic[39] = (constants[36]*algebraic[24])/algebraic[35]
    algebraic[40] = (constants[36]*algebraic[27])/algebraic[35]
    algebraic[41] = (constants[36]*algebraic[31])/algebraic[35]
    algebraic[42] = -constants[25]*(constants[23]*(algebraic[11]*algebraic[36]-algebraic[10]*algebraic[41])+(constants[23]+constants[24]*constants[22])*(algebraic[7]*algebraic[37]-algebraic[12]*algebraic[40])+(constants[23]+constants[24]*constants[22])*(algebraic[5]*algebraic[38]-algebraic[6]*algebraic[39]))
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
        self.k0_12 = 80000
        self.k0_21 = 500
        self.k0_23 = 1e5
        self.k0_32 = 20
        self.k0_34 = 50
        self.k0_43 = 50
        self.k0_45 = 800
        self.k0_54 = 1.219e4
        self.k0_25 = 0.3
        self.k0_52 = 9.1e-4
        self.k0_56 = 10
        self.k0_65_f = 50
        self.k0_61_f = 5
        self.k0_16_f = 35
        self.k0_65_r = 4500
        self.k0_61_r = 3
        self.k0_16_r = 350
        self.delta = 0.7
        self.alpha_pp = 0
        self.N_C = 3e6
        self.N_Avo = 6.022e23
        self.area = 1e6
        self.n = 2
        self.z_c = -2
        self.z_Na = 1
        self.F = 96485.34
        self.R = 8.314
        self.T = 310
        self.Na_o = 10e-3
        self.Na_i = 500e-3
        self.glucose_i = 100e-3
        self.glucose_o = 0e-3
        self.legend_constants_40 = 0.200000

    def to_dict(self):
        return {
            "k0_12": self.k0_12,
            "k0_21": self.k0_21,
            "k0_23": self.k0_23,
            "k0_32": self.k0_32,
            "k0_34": self.k0_34,
            "k0_43": self.k0_43,
            "k0_45": self.k0_45,
            "k0_54": self.k0_54,
            "k0_25": self.k0_25,
            "k0_52": self.k0_52,
            "k0_56": self.k0_56,
            "k0_65_f": self.k0_65_f,
            "k0_61_f": self.k0_61_f,
            "k0_16_f": self.k0_16_f,
            "k0_65_r": self.k0_65_r,
            "k0_61_r": self.k0_61_r,
            "k0_16_r": self.k0_16_r,
            "delta": self.delta,
            "alpha_pp": self.alpha_pp,
            "N_C": self.N_C,
            "N_Avo": self.N_Avo,
            "area": self.area,
            "n": self.n,
            "z_c": self.z_c,
            "z_Na": self.z_Na,
            "F": self.F,
            "R": self.R,
            "T": self.T,
            "Na_o": self.Na_o,
            "Na_i": self.Na_i,
            "glucose_i": self.glucose_i,
            "glucose_o": self.glucose_o,
            "legend_constants_40": self.legend_constants_40,
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
        y0=[-150e-3, 0, 0, 0, 0, 0, 0],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "Eskandari_et_al_2005"
        self.curve_names = [
            "V",
            "C_1",
            "C_2",
            "C_3",
            "C_4",
            "C_5",
            "C_6_temp",
        ]
        self.state_names = ['V', 'C_1', 'C_2', 'C_3', 'C_4', 'C_5', 'C_6_temp']
        self.algebraic_names = ['mu', 'ks_12', 'k_52_temp', 'k_12', 'k_21', 'k_34', 'k_43', 'k_25', 'k_56', 'k_65', 'k_61', 'k_16', 'k_52', 'k0_54_temp', 'k_54', 'C_6', 'C1_sum', 'lambda', 'C2_sum', 'I_NaGl_pSS', 'chi', 'gamma', 'C3_sum', 'beta', 'C4_sum', 'phi', 'alpha', 'C5_sum', 'epsilon', 'Khalf_Na_sq', 'Khalf_gluc', 'C6_sum', 'Imax_Na', 'Imax_gluc', 'Khalf_Na', 'C_sum', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'I_NaGl_SS']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 41
        p = self.params

        # direct mapping
        c[0] = p.k0_12
        c[1] = p.k0_21
        c[2] = p.k0_23
        c[3] = p.k0_32
        c[4] = p.k0_34
        c[5] = p.k0_43
        c[6] = p.k0_45
        c[7] = p.k0_54
        c[8] = p.k0_25
        c[9] = p.k0_52
        c[10] = p.k0_56
        c[11] = p.k0_65_f
        c[12] = p.k0_61_f
        c[13] = p.k0_16_f
        c[14] = p.k0_65_r
        c[15] = p.k0_61_r
        c[16] = p.k0_16_r
        c[17] = p.delta
        c[18] = p.alpha_pp
        c[19] = p.N_C
        c[20] = p.N_Avo
        c[21] = p.area
        c[22] = p.n
        c[23] = p.z_c
        c[24] = p.z_Na
        c[25] = p.F
        c[26] = p.R
        c[27] = p.T
        c[28] = p.Na_o
        c[29] = p.Na_i
        c[30] = p.glucose_i
        c[31] = p.glucose_o
        c[40] = p.legend_constants_40

        # derived constants
        c[32] = (c[14] if (c[28] < 0.100000) else c[11])
        c[33] = (c[15] if (c[28] < 0.100000) else c[12])
        c[34] = (c[16] if (c[28] < 0.100000) else c[13])
        c[35] = (1.00000-c[17])-c[18]
        c[36] = (1.00000e+06*c[19])/c[20]
        c[37] = c[2]*c[31]
        c[38] = c[3]
        c[39] = c[6]

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
