# Size of variable arrays:
sizeAlgebraic = 34
sizeStates = 9
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
    legend_constants[0] = "isotonic in component parameters (dimensionless)"
    legend_constants[1] = "alpha_1 in component parameters (per_micrometre)"
    legend_constants[2] = "beta_1 in component parameters (millinewton)"
    legend_constants[3] = "alpha_2 in component parameters (per_micrometre)"
    legend_constants[4] = "beta_2 in component parameters (millinewton)"
    legend_constants[5] = "alpha_3 in component parameters (per_micrometre)"
    legend_constants[6] = "beta_3 in component parameters (millinewton)"
    legend_constants[7] = "lambda in component parameters (millinewton)"
    legend_constants[8] = "A_half in component parameters (dimensionless)"
    legend_constants[9] = "mu in component parameters (dimensionless)"
    legend_constants[10] = "chi in component parameters (dimensionless)"
    legend_constants[11] = "chi_0 in component parameters (dimensionless)"
    legend_constants[12] = "m_0 in component parameters (dimensionless)"
    legend_constants[13] = "v_max in component parameters (micrometre_per_second)"
    legend_constants[14] = "a in component parameters (dimensionless)"
    legend_constants[15] = "d_h in component parameters (dimensionless)"
    legend_constants[16] = "alpha_P in component parameters (dimensionless)"
    legend_algebraic[9] = "l in component length (micrometre)"
    legend_algebraic[5] = "F_muscle in component force (millinewton)"
    legend_algebraic[11] = "flag in component isotonic (dimensionless)"
    legend_constants[17] = "F_afterload in component isotonic (millinewton)"
    legend_algebraic[13] = "isotonic_mode in component isotonic (dimensionless)"
    legend_constants[18] = "l_0 in component isotonic (micrometre)"
    legend_constants[19] = "S_0 in component parameters_izakov_et_al_1991 (micrometre)"
    legend_algebraic[0] = "q_v in component parameters_izakov_et_al_1991 (per_second)"
    legend_constants[20] = "q_1 in component parameters_izakov_et_al_1991 (per_second)"
    legend_constants[21] = "q_2 in component parameters_izakov_et_al_1991 (per_second)"
    legend_constants[22] = "q_3 in component parameters_izakov_et_al_1991 (per_second)"
    legend_constants[23] = "q_4 in component parameters_izakov_et_al_1991 (per_second)"
    legend_constants[24] = "v_star in component parameters_izakov_et_al_1991 (micrometre_per_second)"
    legend_constants[50] = "v_1 in component parameters_izakov_et_al_1991 (micrometre_per_second)"
    legend_constants[25] = "alpha_G in component parameters_izakov_et_al_1991 (dimensionless)"
    legend_constants[26] = "a_on in component parameters_izakov_et_al_1991 (per_second)"
    legend_constants[27] = "a_off in component parameters_izakov_et_al_1991 (per_second)"
    legend_constants[28] = "k_A in component parameters_izakov_et_al_1991 (dimensionless)"
    legend_states[0] = "v in component CE_velocity (micrometre_per_second)"
    legend_constants[29] = "alpha_Q in component parameters_izakov_et_al_1991 (dimensionless)"
    legend_constants[30] = "beta_Q in component parameters_izakov_et_al_1991 (dimensionless)"
    legend_algebraic[31] = "F_CE in component force (millinewton)"
    legend_algebraic[4] = "F_XSE in component force (millinewton)"
    legend_algebraic[1] = "F_SE in component force (millinewton)"
    legend_algebraic[2] = "F_PE in component force (millinewton)"
    legend_states[1] = "N in component crossbridge_kinetics (dimensionless)"
    legend_algebraic[17] = "k_P_vis in component CE_velocity (millinewton_second_per_micrometre)"
    legend_algebraic[20] = "k_S_vis in component PE_velocity (millinewton_second_per_micrometre)"
    legend_states[2] = "w in component PE_velocity (micrometre_per_second)"
    legend_states[3] = "l_1 in component length (micrometre)"
    legend_states[4] = "l_2 in component length (micrometre)"
    legend_states[5] = "l_3 in component length (micrometre)"
    legend_algebraic[30] = "p_v in component average_crossbridge_force (dimensionless)"
    legend_algebraic[27] = "K_chi in component crossbridge_kinetics (per_second)"
    legend_algebraic[6] = "M_A in component crossbridge_kinetics (dimensionless)"
    legend_algebraic[7] = "n_1 in component crossbridge_kinetics (dimensionless)"
    legend_algebraic[8] = "L_oz in component crossbridge_kinetics (dimensionless)"
    legend_algebraic[25] = "k_p_v in component crossbridge_kinetics (per_second)"
    legend_algebraic[26] = "k_m_v in component crossbridge_kinetics (per_second)"
    legend_states[6] = "A in component calcium_handling (dimensionless)"
    legend_algebraic[24] = "G_star in component average_crossbridge_force (dimensionless)"
    legend_algebraic[21] = "P_star in component average_crossbridge_force (dimensionless)"
    legend_constants[31] = "v_0 in component crossbridge_kinetics (micrometre_per_second)"
    legend_constants[32] = "q_star in component crossbridge_kinetics (per_second)"
    legend_algebraic[3] = "dl_1_dt in component length (micrometre_per_second)"
    legend_algebraic[22] = "dl_2_dt in component length (micrometre_per_second)"
    legend_algebraic[23] = "dl_3_dt in component length (micrometre_per_second)"
    legend_algebraic[18] = "phi_chi_2 in component CE_velocity (micrometre_per_second)"
    legend_algebraic[33] = "phi_chi in component CE_velocity (micrometre_per_second2)"
    legend_algebraic[32] = "p_prime_v in component average_crossbridge_force (second_per_micrometre)"
    legend_constants[33] = "alpha_P_lengthening in component CE_velocity (per_micrometre)"
    legend_constants[34] = "beta_P_lengthening in component CE_velocity (millinewton_second_per_micrometre)"
    legend_constants[35] = "alpha_P_shortening in component CE_velocity (per_micrometre)"
    legend_constants[36] = "beta_P_shortening in component CE_velocity (millinewton_second_per_micrometre)"
    legend_algebraic[15] = "alp_p in component CE_velocity (per_micrometre)"
    legend_constants[37] = "alpha_S_lengthening in component PE_velocity (per_micrometre)"
    legend_constants[38] = "beta_S_lengthening in component PE_velocity (millinewton_second_per_micrometre)"
    legend_constants[39] = "alpha_S_shortening in component PE_velocity (per_micrometre)"
    legend_constants[40] = "beta_S_shortening in component PE_velocity (millinewton_second_per_micrometre)"
    legend_algebraic[19] = "alp_s in component PE_velocity (per_micrometre)"
    legend_constants[53] = "gamma in component average_crossbridge_force (dimensionless)"
    legend_constants[51] = "case_1 in component average_crossbridge_force (second_per_micrometre)"
    legend_algebraic[28] = "case_2 in component average_crossbridge_force (second_per_micrometre)"
    legend_constants[52] = "case_3 in component average_crossbridge_force (second_per_micrometre)"
    legend_algebraic[29] = "case_4 in component average_crossbridge_force (second_per_micrometre)"
    legend_algebraic[14] = "dA_dt in component calcium_handling (per_second)"
    legend_algebraic[10] = "N_A in component calcium_handling (dimensionless)"
    legend_algebraic[12] = "pi_N_A in component calcium_handling (dimensionless)"
    legend_states[7] = "B in component calcium_handling (dimensionless)"
    legend_algebraic[16] = "dB_dt in component calcium_handling (per_second)"
    legend_states[8] = "Ca_C in component calcium_handling (dimensionless)"
    legend_constants[41] = "A_tot in component calcium_handling (dimensionless)"
    legend_constants[42] = "B_tot in component calcium_handling (dimensionless)"
    legend_constants[43] = "b_on in component calcium_handling (per_second)"
    legend_constants[44] = "b_off in component calcium_handling (per_second)"
    legend_constants[45] = "a_c in component calcium_handling (per_second2)"
    legend_constants[46] = "r_Ca in component calcium_handling (per_second)"
    legend_constants[47] = "q_Ca in component calcium_handling (dimensionless)"
    legend_constants[48] = "t_d in component calcium_handling (second)"
    legend_constants[49] = "Ca_m in component calcium_handling (dimensionless)"
    legend_rates[1] = "d/dt N in component crossbridge_kinetics (dimensionless)"
    legend_rates[3] = "d/dt l_1 in component length (micrometre)"
    legend_rates[4] = "d/dt l_2 in component length (micrometre)"
    legend_rates[5] = "d/dt l_3 in component length (micrometre)"
    legend_rates[0] = "d/dt v in component CE_velocity (micrometre_per_second)"
    legend_rates[2] = "d/dt w in component PE_velocity (micrometre_per_second)"
    legend_rates[6] = "d/dt A in component calcium_handling (dimensionless)"
    legend_rates[7] = "d/dt B in component calcium_handling (dimensionless)"
    legend_rates[8] = "d/dt Ca_C in component calcium_handling (dimensionless)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    constants[0] = 0
    constants[1] = 19
    constants[2] = 0.29
    constants[3] = 14.6
    constants[4] = 0.000924
    constants[5] = 48
    constants[6] = 0.01
    constants[7] = 96
    constants[8] = 0.6
    constants[9] = 3
    constants[10] = 0.705
    constants[11] = 3
    constants[12] = 0.9
    constants[13] = 5.6
    constants[14] = 0.25
    constants[15] = 0.5
    constants[16] = 4
    constants[17] = 2
    constants[18] = 0.527
    constants[19] = 1.14
    constants[20] = 17.3
    constants[21] = 259
    constants[22] = 17.3
    constants[23] = 15
    constants[24] = 5.3035675
    constants[25] = 1
    constants[26] = 2300
    constants[27] = 290
    constants[28] = 2.8
    states[0] = 0
    constants[29] = 10
    constants[30] = 5000
    states[1] = 0.0001
    states[2] = 0
    states[3] = 0.437
    states[4] = 0.439
    states[5] = 0.089
    states[6] = 0.01
    constants[31] = 560
    constants[32] = 1000
    constants[33] = 16
    constants[34] = 0.0015
    constants[35] = 16
    constants[36] = 0.0015
    constants[37] = 39
    constants[38] = 0.008
    constants[39] = 46
    constants[40] = 0.006
    states[7] = 0
    states[8] = 0
    constants[41] = 1
    constants[42] = 0.4
    constants[43] = 2600
    constants[44] = 182
    constants[45] = 5200
    constants[46] = 650
    constants[47] = 50
    constants[48] = 0.033
    constants[49] = 0.03
    constants[50] = constants[13]/10.0000
    constants[51] = (constants[14]*(0.400000+0.400000*constants[14]))/(constants[13]*(power((constants[14]+1.00000)*0.400000, 2.00000)))
    constants[52] = (0.400000*constants[14]+1.00000)/(constants[14]*constants[13])
    constants[53] = (constants[14]*constants[15]*(power(constants[50]/constants[13], 2.00000)))/(3.00000*constants[14]*constants[15]-((constants[14]+1.00000)*constants[50])/constants[13])
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[3] = states[0]
    rates[3] = algebraic[3]
    algebraic[8] = (states[3]+constants[19])/(0.460000+constants[19])
    algebraic[10] = states[1]/(algebraic[8]*states[6])
    algebraic[12] = custom_piecewise([greater_equal(algebraic[10] , 1.00000), 1.00000 , True, power(0.0200000, algebraic[10])])
    algebraic[14] = constants[26]*(constants[41]-states[6])*states[8]-constants[27]*exp(-constants[28]*states[6])*algebraic[12]*states[6]
    rates[6] = algebraic[14]
    algebraic[16] = constants[43]*(constants[42]-states[7])*states[8]-constants[44]*states[7]
    rates[7] = algebraic[16]
    rates[8] = custom_piecewise([less(voi , constants[48]), 4.00000*constants[45]*constants[49]*voi*(1.00000-exp(-constants[45]*(power(voi, 2.00000))))*exp(-constants[45]*(power(voi, 2.00000))) , True, (-algebraic[14]-algebraic[16])-constants[46]*exp(-constants[47]*states[8])*states[8]])
    algebraic[20] = custom_piecewise([less_equal(states[2] , states[0]), constants[38]*exp(constants[37]*(states[4]-states[3])) , True, constants[40]*exp(constants[39]*(states[4]-states[3]))])
    algebraic[9] = states[4]+states[5]
    algebraic[4] = constants[6]*(exp(constants[5]*states[5])-1.00000)
    algebraic[5] = algebraic[4]
    algebraic[11] = custom_piecewise([greater_equal(algebraic[9] , constants[18]) & less(voi , 0.150000), 0.00000 , True, 1.00000])
    algebraic[13] = custom_piecewise([equal(constants[0] , 0.00000), 0.00000 , equal(constants[0] , 1.00000) & greater_equal(algebraic[5] , constants[17]), 1.00000 , equal(constants[0] , 1.00000) & greater_equal(algebraic[9] , constants[18]) & equal(algebraic[11] , 1.00000), 0.00000 , True, float('nan')])
    algebraic[18] = custom_piecewise([equal(algebraic[13] , 1.00000), (constants[1]*constants[2]*exp(constants[1]*(states[4]-states[3]))*states[0])/(constants[1]*constants[2]*exp(constants[1]*(states[4]-states[3]))+constants[3]*constants[4]*exp(constants[3]*states[4])) , True, (constants[1]*constants[2]*exp(constants[1]*(states[4]-states[3]))*states[0])/(constants[1]*constants[2]*exp(constants[1]*(states[4]-states[3]))+constants[3]*constants[4]*exp(constants[3]*states[4])+constants[5]*constants[6]*exp(constants[5]*states[5]))])
    algebraic[22] = custom_piecewise([equal(algebraic[20] , 0.00000), algebraic[18] , True, states[2]])
    rates[4] = algebraic[22]
    algebraic[23] = custom_piecewise([equal(algebraic[13] , 1.00000), 0.00000 , equal(algebraic[13] , 0.00000) & equal(algebraic[20] , 0.00000), -algebraic[18] , True, -states[2]])
    rates[5] = algebraic[23]
    algebraic[6] = (power(states[6], constants[9]))/(power(states[6], constants[9])+power(constants[8], constants[9]))
    algebraic[7] = 0.600000*states[3]+0.500000
    algebraic[0] = custom_piecewise([less_equal(states[0] , 0.00000), constants[20]-(constants[21]*states[0])/constants[13] , less_equal(states[0] , constants[24]) & less(0.00000 , states[0]), ((constants[23]-constants[22])*states[0])/constants[24]+constants[22] , True, constants[23]/(power(1.00000+(constants[30]*(states[0]-constants[24]))/constants[13], constants[29]))])
    algebraic[21] = custom_piecewise([less_equal(states[0] , 0.00000), (constants[14]*(1.00000+states[0]/constants[13]))/(constants[14]-states[0]/constants[13]) , True, (1.00000+constants[15])-((power(constants[15], 2.00000))*constants[14])/(((constants[14]*constants[15])/constants[53])*(power(states[0]/constants[13], 2.00000))+((constants[14]+1.00000)*states[0])/constants[13]+constants[14]*constants[15])])
    algebraic[24] = custom_piecewise([less_equal(-constants[13] , states[0]) & less_equal(states[0] , 0.00000), 1.00000+(0.600000*states[0])/constants[13] , less(0.00000 , states[0]) & less_equal(states[0] , constants[50]), algebraic[21]/(((0.400000*constants[14]+1.00000)*states[0])/(constants[14]*constants[13])+1.00000) , True, (algebraic[21]*exp(-constants[25]*(power((states[0]-constants[50])/constants[13], constants[16]))))/(((0.400000*constants[14]+1.00000)*states[0])/(constants[14]*constants[13])+1.00000)])
    algebraic[25] = constants[10]*constants[11]*algebraic[0]*constants[12]*algebraic[24]
    algebraic[26] = custom_piecewise([less_equal(states[0] , constants[24]), constants[11]*algebraic[0]*(1.00000-constants[10]*constants[12]*algebraic[24]) , True, constants[11]*(constants[23]*(1.00000-constants[10]*constants[12]*algebraic[24])+(constants[32]*(states[0]-constants[24]))/(constants[31]-constants[24]))])
    algebraic[27] = algebraic[25]*algebraic[6]*algebraic[7]*algebraic[8]*(1.00000-states[1])-algebraic[26]*states[1]
    rates[1] = algebraic[27]
    algebraic[17] = custom_piecewise([less_equal(states[0] , 0.00000), constants[34]*exp(constants[33]*states[3]) , True, constants[36]*exp(constants[35]*states[3])])
    algebraic[30] = algebraic[21]/algebraic[24]
    algebraic[28] = (constants[14]*1.00000*(1.00000+0.400000*constants[14]+(1.20000*states[0])/constants[13]+0.600000*(power(states[0]/constants[13], 2.00000))))/(constants[13]*(power((constants[14]-states[0]/constants[13])*(1.00000+(0.600000*states[0])/constants[13]), 2.00000)))
    algebraic[29] = (1.00000/constants[13])*exp(-constants[25]*(power(states[0]/constants[13]-constants[50]/constants[13], constants[16])))*((0.400000*constants[14]+1.00000)/constants[14]+constants[25]*constants[16]*(1.00000+((0.400000*constants[14]+1.00000)*states[0])/(constants[14]*constants[13]))*(power(states[0]/constants[13]-constants[50]/constants[13], constants[16]-1.00000)))
    algebraic[32] = custom_piecewise([less_equal(states[0] , -constants[13]), constants[51] , less(-constants[13] , states[0]) & less_equal(states[0] , 0.00000), algebraic[28] , less(0.00000 , states[0]) & less_equal(states[0] , constants[50]), constants[52] , True, algebraic[29]])
    algebraic[15] = custom_piecewise([less_equal(states[0] , 0.00000), constants[33] , True, constants[35]])
    algebraic[33] = custom_piecewise([equal(algebraic[13] , 1.00000), -(constants[7]*algebraic[27]*algebraic[30]+algebraic[15]*algebraic[17]*(power(states[0], 2.00000))+constants[3]*constants[4]*exp(constants[3]*states[4])*states[2])/(constants[7]*states[1]*algebraic[32]+algebraic[17]) , True, -(constants[7]*algebraic[27]*algebraic[30]+algebraic[15]*algebraic[17]*(power(states[0], 2.00000))+(constants[3]*constants[4]*exp(constants[3]*states[4])+constants[5]*constants[6]*exp(constants[5]*states[5]))*states[2])/(constants[7]*states[1]*algebraic[32]+algebraic[17])])
    rates[0] = custom_piecewise([equal(algebraic[20] , 0.00000), (constants[1]*constants[2]*exp(constants[1]*(states[4]-states[3]))*(algebraic[18]-states[0])-(constants[7]*algebraic[27]*algebraic[30]+algebraic[15]*algebraic[17]*(power(states[0], 2.00000))))/(constants[7]*states[1]*algebraic[32]+algebraic[17]) , True, algebraic[33]])
    algebraic[19] = custom_piecewise([less_equal(states[2] , states[0]), constants[37] , True, constants[39]])
    rates[2] = custom_piecewise([equal(algebraic[13] , 1.00000), ((algebraic[20]*(algebraic[33]-algebraic[19]*(power(states[2]-states[0], 2.00000)))-constants[1]*constants[2]*exp(constants[1]*(states[4]-states[3]))*(states[2]-states[0]))-constants[3]*constants[4]*exp(constants[3]*states[4])*states[2])/algebraic[20] , True, (algebraic[33]-algebraic[19]*(power(states[2]-states[0], 2.00000)))-(constants[1]*constants[2]*exp(constants[1]*(states[4]-states[3]))*(states[2]-states[0])+(constants[3]*constants[4]*exp(constants[3]*states[4])+constants[5]*constants[6]*exp(constants[5]*states[5]))*states[2])/algebraic[20]])
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[3] = states[0]
    algebraic[8] = (states[3]+constants[19])/(0.460000+constants[19])
    algebraic[10] = states[1]/(algebraic[8]*states[6])
    algebraic[12] = custom_piecewise([greater_equal(algebraic[10] , 1.00000), 1.00000 , True, power(0.0200000, algebraic[10])])
    algebraic[14] = constants[26]*(constants[41]-states[6])*states[8]-constants[27]*exp(-constants[28]*states[6])*algebraic[12]*states[6]
    algebraic[16] = constants[43]*(constants[42]-states[7])*states[8]-constants[44]*states[7]
    algebraic[20] = custom_piecewise([less_equal(states[2] , states[0]), constants[38]*exp(constants[37]*(states[4]-states[3])) , True, constants[40]*exp(constants[39]*(states[4]-states[3]))])
    algebraic[9] = states[4]+states[5]
    algebraic[4] = constants[6]*(exp(constants[5]*states[5])-1.00000)
    algebraic[5] = algebraic[4]
    algebraic[11] = custom_piecewise([greater_equal(algebraic[9] , constants[18]) & less(voi , 0.150000), 0.00000 , True, 1.00000])
    algebraic[13] = custom_piecewise([equal(constants[0] , 0.00000), 0.00000 , equal(constants[0] , 1.00000) & greater_equal(algebraic[5] , constants[17]), 1.00000 , equal(constants[0] , 1.00000) & greater_equal(algebraic[9] , constants[18]) & equal(algebraic[11] , 1.00000), 0.00000 , True, float('nan')])
    algebraic[18] = custom_piecewise([equal(algebraic[13] , 1.00000), (constants[1]*constants[2]*exp(constants[1]*(states[4]-states[3]))*states[0])/(constants[1]*constants[2]*exp(constants[1]*(states[4]-states[3]))+constants[3]*constants[4]*exp(constants[3]*states[4])) , True, (constants[1]*constants[2]*exp(constants[1]*(states[4]-states[3]))*states[0])/(constants[1]*constants[2]*exp(constants[1]*(states[4]-states[3]))+constants[3]*constants[4]*exp(constants[3]*states[4])+constants[5]*constants[6]*exp(constants[5]*states[5]))])
    algebraic[22] = custom_piecewise([equal(algebraic[20] , 0.00000), algebraic[18] , True, states[2]])
    algebraic[23] = custom_piecewise([equal(algebraic[13] , 1.00000), 0.00000 , equal(algebraic[13] , 0.00000) & equal(algebraic[20] , 0.00000), -algebraic[18] , True, -states[2]])
    algebraic[6] = (power(states[6], constants[9]))/(power(states[6], constants[9])+power(constants[8], constants[9]))
    algebraic[7] = 0.600000*states[3]+0.500000
    algebraic[0] = custom_piecewise([less_equal(states[0] , 0.00000), constants[20]-(constants[21]*states[0])/constants[13] , less_equal(states[0] , constants[24]) & less(0.00000 , states[0]), ((constants[23]-constants[22])*states[0])/constants[24]+constants[22] , True, constants[23]/(power(1.00000+(constants[30]*(states[0]-constants[24]))/constants[13], constants[29]))])
    algebraic[21] = custom_piecewise([less_equal(states[0] , 0.00000), (constants[14]*(1.00000+states[0]/constants[13]))/(constants[14]-states[0]/constants[13]) , True, (1.00000+constants[15])-((power(constants[15], 2.00000))*constants[14])/(((constants[14]*constants[15])/constants[53])*(power(states[0]/constants[13], 2.00000))+((constants[14]+1.00000)*states[0])/constants[13]+constants[14]*constants[15])])
    algebraic[24] = custom_piecewise([less_equal(-constants[13] , states[0]) & less_equal(states[0] , 0.00000), 1.00000+(0.600000*states[0])/constants[13] , less(0.00000 , states[0]) & less_equal(states[0] , constants[50]), algebraic[21]/(((0.400000*constants[14]+1.00000)*states[0])/(constants[14]*constants[13])+1.00000) , True, (algebraic[21]*exp(-constants[25]*(power((states[0]-constants[50])/constants[13], constants[16]))))/(((0.400000*constants[14]+1.00000)*states[0])/(constants[14]*constants[13])+1.00000)])
    algebraic[25] = constants[10]*constants[11]*algebraic[0]*constants[12]*algebraic[24]
    algebraic[26] = custom_piecewise([less_equal(states[0] , constants[24]), constants[11]*algebraic[0]*(1.00000-constants[10]*constants[12]*algebraic[24]) , True, constants[11]*(constants[23]*(1.00000-constants[10]*constants[12]*algebraic[24])+(constants[32]*(states[0]-constants[24]))/(constants[31]-constants[24]))])
    algebraic[27] = algebraic[25]*algebraic[6]*algebraic[7]*algebraic[8]*(1.00000-states[1])-algebraic[26]*states[1]
    algebraic[17] = custom_piecewise([less_equal(states[0] , 0.00000), constants[34]*exp(constants[33]*states[3]) , True, constants[36]*exp(constants[35]*states[3])])
    algebraic[30] = algebraic[21]/algebraic[24]
    algebraic[28] = (constants[14]*1.00000*(1.00000+0.400000*constants[14]+(1.20000*states[0])/constants[13]+0.600000*(power(states[0]/constants[13], 2.00000))))/(constants[13]*(power((constants[14]-states[0]/constants[13])*(1.00000+(0.600000*states[0])/constants[13]), 2.00000)))
    algebraic[29] = (1.00000/constants[13])*exp(-constants[25]*(power(states[0]/constants[13]-constants[50]/constants[13], constants[16])))*((0.400000*constants[14]+1.00000)/constants[14]+constants[25]*constants[16]*(1.00000+((0.400000*constants[14]+1.00000)*states[0])/(constants[14]*constants[13]))*(power(states[0]/constants[13]-constants[50]/constants[13], constants[16]-1.00000)))
    algebraic[32] = custom_piecewise([less_equal(states[0] , -constants[13]), constants[51] , less(-constants[13] , states[0]) & less_equal(states[0] , 0.00000), algebraic[28] , less(0.00000 , states[0]) & less_equal(states[0] , constants[50]), constants[52] , True, algebraic[29]])
    algebraic[15] = custom_piecewise([less_equal(states[0] , 0.00000), constants[33] , True, constants[35]])
    algebraic[33] = custom_piecewise([equal(algebraic[13] , 1.00000), -(constants[7]*algebraic[27]*algebraic[30]+algebraic[15]*algebraic[17]*(power(states[0], 2.00000))+constants[3]*constants[4]*exp(constants[3]*states[4])*states[2])/(constants[7]*states[1]*algebraic[32]+algebraic[17]) , True, -(constants[7]*algebraic[27]*algebraic[30]+algebraic[15]*algebraic[17]*(power(states[0], 2.00000))+(constants[3]*constants[4]*exp(constants[3]*states[4])+constants[5]*constants[6]*exp(constants[5]*states[5]))*states[2])/(constants[7]*states[1]*algebraic[32]+algebraic[17])])
    algebraic[19] = custom_piecewise([less_equal(states[2] , states[0]), constants[37] , True, constants[39]])
    algebraic[1] = constants[2]*(exp(constants[1]*(states[4]-states[3]))-1.00000)
    algebraic[2] = constants[4]*(exp(constants[3]*states[4])-1.00000)
    algebraic[31] = constants[7]*algebraic[30]*states[1]
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
        self.isotonic = 0
        self.alpha_1 = 19
        self.beta_1 = 0.29
        self.alpha_2 = 14.6
        self.beta_2 = 0.000924
        self.alpha_3 = 48
        self.beta_3 = 0.01
        self.lambda = 96
        self.A_half = 0.6
        self.mu = 3
        self.chi = 0.705
        self.chi_0 = 3
        self.m_0 = 0.9
        self.v_max = 5.6
        self.a = 0.25
        self.d_h = 0.5
        self.alpha_P = 4
        self.F_afterload = 2
        self.l_0 = 0.527
        self.S_0 = 1.14
        self.q_1 = 17.3
        self.q_2 = 259
        self.q_3 = 17.3
        self.q_4 = 15
        self.v_star = 5.3035675
        self.alpha_G = 1
        self.a_on = 2300
        self.a_off = 290
        self.k_A = 2.8
        self.alpha_Q = 10
        self.beta_Q = 5000
        self.v_0 = 560
        self.q_star = 1000
        self.alpha_P_lengthening = 16
        self.beta_P_lengthening = 0.0015
        self.alpha_P_shortening = 16
        self.beta_P_shortening = 0.0015
        self.alpha_S_lengthening = 39
        self.beta_S_lengthening = 0.008
        self.alpha_S_shortening = 46
        self.beta_S_shortening = 0.006
        self.A_tot = 1
        self.B_tot = 0.4
        self.b_on = 2600
        self.b_off = 182
        self.a_c = 5200
        self.r_Ca = 650
        self.q_Ca = 50
        self.t_d = 0.033
        self.Ca_m = 0.03

    def to_dict(self):
        return {
            "isotonic": self.isotonic,
            "alpha_1": self.alpha_1,
            "beta_1": self.beta_1,
            "alpha_2": self.alpha_2,
            "beta_2": self.beta_2,
            "alpha_3": self.alpha_3,
            "beta_3": self.beta_3,
            "lambda": self.lambda,
            "A_half": self.A_half,
            "mu": self.mu,
            "chi": self.chi,
            "chi_0": self.chi_0,
            "m_0": self.m_0,
            "v_max": self.v_max,
            "a": self.a,
            "d_h": self.d_h,
            "alpha_P": self.alpha_P,
            "F_afterload": self.F_afterload,
            "l_0": self.l_0,
            "S_0": self.S_0,
            "q_1": self.q_1,
            "q_2": self.q_2,
            "q_3": self.q_3,
            "q_4": self.q_4,
            "v_star": self.v_star,
            "alpha_G": self.alpha_G,
            "a_on": self.a_on,
            "a_off": self.a_off,
            "k_A": self.k_A,
            "alpha_Q": self.alpha_Q,
            "beta_Q": self.beta_Q,
            "v_0": self.v_0,
            "q_star": self.q_star,
            "alpha_P_lengthening": self.alpha_P_lengthening,
            "beta_P_lengthening": self.beta_P_lengthening,
            "alpha_P_shortening": self.alpha_P_shortening,
            "beta_P_shortening": self.beta_P_shortening,
            "alpha_S_lengthening": self.alpha_S_lengthening,
            "beta_S_lengthening": self.beta_S_lengthening,
            "alpha_S_shortening": self.alpha_S_shortening,
            "beta_S_shortening": self.beta_S_shortening,
            "A_tot": self.A_tot,
            "B_tot": self.B_tot,
            "b_on": self.b_on,
            "b_off": self.b_off,
            "a_c": self.a_c,
            "r_Ca": self.r_Ca,
            "q_Ca": self.q_Ca,
            "t_d": self.t_d,
            "Ca_m": self.Ca_m,
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
        y0=[0, 0.0001, 0, 0.437, 0.439, 0.089, 0.01, 0, 0],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "katsnelson_2004c"
        self.curve_names = [
            "v",
            "N",
            "w",
            "l_1",
            "l_2",
            "l_3",
            "A",
            "B",
            "Ca_C",
        ]
        self.state_names = ['v', 'N', 'w', 'l_1', 'l_2', 'l_3', 'A', 'B', 'Ca_C']
        self.algebraic_names = ['q_v', 'F_SE', 'F_PE', 'dl_1_dt', 'F_XSE', 'F_muscle', 'M_A', 'n_1', 'L_oz', 'l', 'N_A', 'flag', 'pi_N_A', 'isotonic_mode', 'dA_dt', 'alp_p', 'dB_dt', 'k_P_vis', 'phi_chi_2', 'alp_s', 'k_S_vis', 'P_star', 'dl_2_dt', 'dl_3_dt', 'G_star', 'k_p_v', 'k_m_v', 'K_chi', 'case_2', 'case_4', 'p_v', 'F_CE', 'p_prime_v', 'phi_chi']
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
        c[0] = p.isotonic
        c[1] = p.alpha_1
        c[2] = p.beta_1
        c[3] = p.alpha_2
        c[4] = p.beta_2
        c[5] = p.alpha_3
        c[6] = p.beta_3
        c[7] = p.lambda
        c[8] = p.A_half
        c[9] = p.mu
        c[10] = p.chi
        c[11] = p.chi_0
        c[12] = p.m_0
        c[13] = p.v_max
        c[14] = p.a
        c[15] = p.d_h
        c[16] = p.alpha_P
        c[17] = p.F_afterload
        c[18] = p.l_0
        c[19] = p.S_0
        c[20] = p.q_1
        c[21] = p.q_2
        c[22] = p.q_3
        c[23] = p.q_4
        c[24] = p.v_star
        c[25] = p.alpha_G
        c[26] = p.a_on
        c[27] = p.a_off
        c[28] = p.k_A
        c[29] = p.alpha_Q
        c[30] = p.beta_Q
        c[31] = p.v_0
        c[32] = p.q_star
        c[33] = p.alpha_P_lengthening
        c[34] = p.beta_P_lengthening
        c[35] = p.alpha_P_shortening
        c[36] = p.beta_P_shortening
        c[37] = p.alpha_S_lengthening
        c[38] = p.beta_S_lengthening
        c[39] = p.alpha_S_shortening
        c[40] = p.beta_S_shortening
        c[41] = p.A_tot
        c[42] = p.B_tot
        c[43] = p.b_on
        c[44] = p.b_off
        c[45] = p.a_c
        c[46] = p.r_Ca
        c[47] = p.q_Ca
        c[48] = p.t_d
        c[49] = p.Ca_m

        # derived constants
        c[50] = c[13]/10.0000
        c[51] = (c[14]*(0.400000+0.400000*c[14]))/(c[13]*(power((c[14]+1.00000)*0.400000, 2.00000)))
        c[52] = (0.400000*c[14]+1.00000)/(c[14]*c[13])
        c[53] = (c[14]*c[15]*(power(c[50]/c[13], 2.00000)))/(3.00000*c[14]*c[15]-((c[14]+1.00000)*c[50])/c[13])

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
