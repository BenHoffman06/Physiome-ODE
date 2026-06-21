# Size of variable arrays:
sizeAlgebraic = 34
sizeStates = 19
sizeConstants = 60
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "t in component Environment (second)"
    legend_constants[0] = "Mg_tot in component Environment (molar)"
    legend_constants[1] = "Pi_e in component Environment (molar)"
    legend_constants[2] = "ADP_e in component Environment (molar)"
    legend_constants[3] = "RT in component Fixed_parameters (kilojoule_per_mole)"
    legend_constants[4] = "F in component Fixed_parameters (kilojoule_per_mole_per_millivolt)"
    legend_constants[5] = "n_A in component Fixed_parameters (dimensionless)"
    legend_constants[6] = "dG_C1o in component Fixed_parameters (kilojoule_per_mole)"
    legend_constants[7] = "dG_C3o in component Fixed_parameters (kilojoule_per_mole)"
    legend_constants[8] = "dG_C4o in component Fixed_parameters (kilojoule_per_mole)"
    legend_constants[9] = "dG_F1o in component Fixed_parameters (kilojoule_per_mole)"
    legend_constants[10] = "pH_e in component Fixed_parameters (dimensionless)"
    legend_constants[47] = "H_e in component Fixed_parameters (molar)"
    legend_constants[11] = "K_e in component Fixed_parameters (molar)"
    legend_constants[12] = "ATP_e in component Fixed_parameters (molar)"
    legend_constants[13] = "AMP_e in component Fixed_parameters (molar)"
    legend_constants[48] = "k_dHPi in component Fixed_parameters (molar)"
    legend_constants[49] = "k_dHatp in component Fixed_parameters (molar)"
    legend_constants[50] = "k_dHadp in component Fixed_parameters (molar)"
    legend_constants[14] = "K_DT in component Fixed_parameters (molar)"
    legend_constants[15] = "K_DD in component Fixed_parameters (molar)"
    legend_constants[16] = "K_AK in component Fixed_parameters (dimensionless)"
    legend_constants[17] = "W_m in component Fixed_parameters (l_water_per_l_mito)"
    legend_constants[52] = "W_x in component Fixed_parameters (l_water_per_l_mito)"
    legend_constants[55] = "W_i in component Fixed_parameters (l_water_per_l_mito)"
    legend_constants[18] = "gamma in component Fixed_parameters (per_micron)"
    legend_constants[19] = "Ctot in component Fixed_parameters (molar)"
    legend_constants[20] = "Qtot in component Fixed_parameters (molar)"
    legend_constants[21] = "NADtot in component Fixed_parameters (molar)"
    legend_constants[54] = "H_i in component Fixed_parameters (molar)"
    legend_constants[51] = "K_i in component Fixed_parameters (molar)"
    legend_constants[22] = "k_Pi1 in component Adjustable_parameters (molar)"
    legend_constants[23] = "k_Pi2 in component Adjustable_parameters (molar)"
    legend_constants[24] = "k_Pi3 in component Adjustable_parameters (molar)"
    legend_constants[25] = "k_Pi4 in component Adjustable_parameters (molar)"
    legend_constants[26] = "k_PiH in component Adjustable_parameters (molar)"
    legend_constants[27] = "r in component Adjustable_parameters (dimensionless)"
    legend_constants[28] = "x_DH in component Adjustable_parameters (mole_per_second_per_l_mito_per_molar)"
    legend_constants[29] = "x_C1 in component Adjustable_parameters (mole_per_second_per_l_mito_per_molar)"
    legend_constants[30] = "x_C3 in component Adjustable_parameters (mole_per_second_per_l_mito_per_molar)"
    legend_constants[31] = "x_C4 in component Adjustable_parameters (mole_per_second_per_l_mito_per_molar)"
    legend_constants[32] = "x_F1 in component Adjustable_parameters (mole_per_second_per_l_mito_per_molar_per_molar)"
    legend_constants[33] = "x_ANT in component Adjustable_parameters (mole_per_second_per_l_mito)"
    legend_constants[34] = "x_Pi1 in component Adjustable_parameters (mole_per_second_per_l_mito_per_molar)"
    legend_constants[35] = "x_KH in component Adjustable_parameters (mole_per_second_per_l_mito_per_molar_per_molar)"
    legend_constants[36] = "x_Hle in component Adjustable_parameters (mole_per_second_per_l_mito_per_molar_per_millivolt)"
    legend_constants[37] = "x_K in component Adjustable_parameters (mole_per_second_per_l_mito_per_molar_per_millivolt)"
    legend_constants[38] = "k_mADP in component Adjustable_parameters (molar)"
    legend_constants[39] = "x_AK in component Adjustable_parameters (mole_per_second_per_l_mito_per_molar_per_molar)"
    legend_constants[40] = "p_A in component Adjustable_parameters (micron_per_second)"
    legend_constants[41] = "k_O2 in component Adjustable_parameters (molar)"
    legend_constants[42] = "x_buff in component Adjustable_parameters (per_molar)"
    legend_constants[43] = "x_MgA in component Adjustable_parameters (mole_per_second_per_l_mito_per_molar_per_molar)"
    legend_constants[44] = "x_Pi2 in component Adjustable_parameters (micron_per_second)"
    legend_algebraic[0] = "dG_H in component Proton_motive_force (kilojoule_per_mole)"
    legend_states[0] = "dPsi in component dPsi_dt (millivolt)"
    legend_states[1] = "H_x in component dH_x_dt (molar)"
    legend_algebraic[26] = "J_DH in component Dehydrogenase_flux (mole_per_second_per_l_mito)"
    legend_algebraic[25] = "NAD_x in component NAD_x_concentration (molar)"
    legend_states[2] = "NADH_x in component dNADH_x_dt (molar)"
    legend_states[3] = "Pi_x in component dPi_x_dt (molar)"
    legend_algebraic[29] = "J_C1 in component Electron_flux_complex_I (mole_per_second_per_l_mito)"
    legend_algebraic[28] = "dG_C1op in component Electron_flux_complex_I (kilojoule_per_mole)"
    legend_algebraic[27] = "Q in component Q_concentration (molar)"
    legend_states[4] = "QH2 in component dQH2_dt (molar)"
    legend_algebraic[32] = "J_C3 in component Electron_flux_complex_III (mole_per_second_per_l_mito)"
    legend_algebraic[30] = "dG_C3op in component Electron_flux_complex_III (kilojoule_per_mole)"
    legend_algebraic[31] = "Cox in component Cox_concentration (molar)"
    legend_states[5] = "Cred in component dCred_dt (molar)"
    legend_algebraic[33] = "J_C4 in component Electron_flux_complex_IV (mole_per_second_per_l_mito)"
    legend_algebraic[1] = "dG_C4op in component Electron_flux_complex_IV (kilojoule_per_mole)"
    legend_states[6] = "O2 in component dO2_dt (molar)"
    legend_algebraic[2] = "J_F1 in component ATP_synthesis_flux (mole_per_second_per_l_mito)"
    legend_states[7] = "ADP_mx in component dADP_mx_dt (molar)"
    legend_states[8] = "ATP_mx in component dATP_mx_dt (molar)"
    legend_algebraic[12] = "J_ANT in component ANT_flux (mole_per_second_per_l_mito)"
    legend_algebraic[3] = "Psi_x in component ANT_flux (millivolt)"
    legend_algebraic[4] = "Psi_i in component ANT_flux (millivolt)"
    legend_algebraic[10] = "ADP_fi in component MgADPi_binding_flux (molar)"
    legend_algebraic[8] = "ATP_fi in component MgATPi_binding_flux (molar)"
    legend_algebraic[7] = "ADP_fx in component MgADPx_binding_flux (molar)"
    legend_algebraic[5] = "ATP_fx in component MgATPx_binding_flux (molar)"
    legend_constants[45] = "mincond in component ANT_flux (molar)"
    legend_algebraic[6] = "J_MgATPx in component MgATPx_binding_flux (mole_per_second_per_l_mito)"
    legend_states[9] = "ATP_x in component dATP_x_dt (molar)"
    legend_states[10] = "Mg_x in component dMg_x_dt (molar)"
    legend_algebraic[9] = "J_MgADPx in component MgADPx_binding_flux (mole_per_second_per_l_mito)"
    legend_states[11] = "ADP_x in component dADP_x_dt (molar)"
    legend_algebraic[11] = "J_MgATPi in component MgATPi_binding_flux (mole_per_second_per_l_mito)"
    legend_states[12] = "ATP_i in component dATP_i_dt (molar)"
    legend_states[13] = "ATP_mi in component dATP_mi_dt (molar)"
    legend_constants[58] = "Mg_i in component Mg_binding (molar)"
    legend_algebraic[13] = "J_MgADPi in component MgADPi_binding_flux (mole_per_second_per_l_mito)"
    legend_states[14] = "ADP_i in component dADP_i_dt (molar)"
    legend_states[15] = "ADP_mi in component dADP_mi_dt (molar)"
    legend_algebraic[15] = "J_ATP in component ATP_substrate_flux (mole_per_second_per_l_mito)"
    legend_algebraic[17] = "J_ADP in component ADP_substrate_flux (mole_per_second_per_l_mito)"
    legend_algebraic[19] = "J_AMP in component AMP_substrate_flux (mole_per_second_per_l_mito)"
    legend_states[16] = "AMP_i in component dAMP_i_dt (molar)"
    legend_algebraic[14] = "J_Pi2 in component Pi_substrate_flux (mole_per_second_per_l_mito)"
    legend_states[17] = "Pi_i in component dPi_i_dt (molar)"
    legend_algebraic[20] = "J_Pi1 in component Phosphate_hydrogen_cotransporter_flux (mole_per_second_per_l_mito)"
    legend_algebraic[16] = "H2PIi in component Phosphate_hydrogen_cotransporter_flux (molar)"
    legend_algebraic[18] = "H2PIx in component Phosphate_hydrogen_cotransporter_flux (molar)"
    legend_algebraic[21] = "J_AKi in component Adenylate_kinase_flux (mole_per_second_per_l_mito)"
    legend_algebraic[22] = "J_Hle in component Hydrogen_leak_flux (mole_per_second_per_l_mito)"
    legend_algebraic[23] = "J_K in component Passive_potassium_flux (mole_per_second_per_l_mito)"
    legend_states[18] = "K_x in component dK_x_dt (molar)"
    legend_algebraic[24] = "J_KH in component Potassium_hydrogen_flux (mole_per_second_per_l_mito)"
    legend_constants[53] = "ADP_me in component ADP_binding (molar)"
    legend_constants[56] = "ADP_fe in component ADP_binding (molar)"
    legend_constants[57] = "Mg_e in component Mg_binding (molar)"
    legend_constants[46] = "C_im in component dPsi_dt (mole_per_l_mito_per_millivolt)"
    legend_rates[1] = "d/dt H_x in component dH_x_dt (molar)"
    legend_rates[18] = "d/dt K_x in component dK_x_dt (molar)"
    legend_rates[10] = "d/dt Mg_x in component dMg_x_dt (molar)"
    legend_rates[2] = "d/dt NADH_x in component dNADH_x_dt (molar)"
    legend_rates[4] = "d/dt QH2 in component dQH2_dt (molar)"
    legend_rates[5] = "d/dt Cred in component dCred_dt (molar)"
    legend_rates[9] = "d/dt ATP_x in component dATP_x_dt (molar)"
    legend_rates[11] = "d/dt ADP_x in component dADP_x_dt (molar)"
    legend_rates[8] = "d/dt ATP_mx in component dATP_mx_dt (molar)"
    legend_rates[7] = "d/dt ADP_mx in component dADP_mx_dt (molar)"
    legend_rates[3] = "d/dt Pi_x in component dPi_x_dt (molar)"
    legend_rates[12] = "d/dt ATP_i in component dATP_i_dt (molar)"
    legend_rates[14] = "d/dt ADP_i in component dADP_i_dt (molar)"
    legend_rates[16] = "d/dt AMP_i in component dAMP_i_dt (molar)"
    legend_rates[13] = "d/dt ATP_mi in component dATP_mi_dt (molar)"
    legend_rates[15] = "d/dt ADP_mi in component dADP_mi_dt (molar)"
    legend_rates[17] = "d/dt Pi_i in component dPi_i_dt (molar)"
    legend_rates[0] = "d/dt dPsi in component dPsi_dt (millivolt)"
    legend_rates[6] = "d/dt O2 in component dO2_dt (molar)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    constants[0] = 0.005
    constants[1] = 0.000125
    constants[2] = 0
    constants[3] = 2.4734
    constants[4] = 0.096484
    constants[5] = 3
    constants[6] = -69.37
    constants[7] = -32.53
    constants[8] = -122.94
    constants[9] = 36.03
    constants[10] = 7.1
    constants[11] = 0.15
    constants[12] = 0
    constants[13] = 0
    constants[14] = 2.4e-5
    constants[15] = 3.47e-4
    constants[16] = 0.4331
    constants[17] = 0.72376
    constants[18] = 5.99
    constants[19] = 0.0027
    constants[20] = 0.00135
    constants[21] = 0.00297
    constants[22] = 1.3413e-4
    constants[23] = 6.7668e-4
    constants[24] = 1.9172e-4
    constants[25] = 0.02531
    constants[26] = 4.5082e-4
    constants[27] = 4.5807
    constants[28] = 0.09183
    constants[29] = 0.36923
    constants[30] = 0.091737
    constants[31] = 3.2562e-5
    constants[32] = 150.93
    constants[33] = 0.0079204
    constants[34] = 339430
    constants[35] = 2.9802e7
    constants[36] = 250
    constants[37] = 0
    constants[38] = 3.5e-6
    constants[39] = 0
    constants[40] = 85
    constants[41] = 1.2e-4
    constants[42] = 100
    constants[43] = 1000000
    constants[44] = 327
    states[0] = 160
    states[1] = 6.30957344480193e-8
    states[2] = 0.0015
    states[3] = 0.001
    states[4] = 8e-4
    states[5] = 0.001
    states[6] = 2.6e-5
    states[7] = 0
    states[8] = 0
    constants[45] = 1e-12
    states[9] = 0
    states[10] = 0.005
    states[11] = 0.01
    states[12] = 0
    states[13] = 0
    states[14] = 0
    states[15] = 0
    states[16] = 0
    states[17] = 0.001
    states[18] = 0.14
    constants[46] = 6.756756756756757e-6
    constants[47] = 1.00000*(power(10.0000, -constants[10]))
    constants[48] = 1.00000*(power(10.0000, -6.75000))
    constants[49] = 1.00000*(power(10.0000, -6.48000))
    constants[50] = 1.00000*(power(10.0000, -6.29000))
    constants[51] = constants[11]
    constants[52] = 0.900000*constants[17]
    constants[53] = ((constants[15]+constants[2]+constants[0])-power(power(constants[15]+constants[2]+constants[0], 2.00000)-4.00000*constants[0]*constants[2], 1.0/2))/2.00000
    constants[59] = 0.00000
    constants[54] = constants[47]
    constants[55] = 0.100000*constants[17]
    constants[56] = constants[2]-constants[53]
    constants[57] = constants[0]-constants[53]
    constants[58] = constants[57]
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[6] = constants[59]
    algebraic[5] = states[9]-states[8]
    algebraic[6] = constants[43]*(algebraic[5]*states[10]-constants[14]*states[8])
    rates[8] = algebraic[6]/constants[52]
    algebraic[7] = states[11]-states[7]
    algebraic[9] = constants[43]*(algebraic[7]*states[10]-constants[15]*states[7])
    rates[10] = (-algebraic[6]-algebraic[9])/constants[52]
    rates[7] = algebraic[9]/constants[52]
    algebraic[8] = states[12]-states[13]
    algebraic[11] = constants[43]*(algebraic[8]*constants[58]-constants[14]*states[13])
    rates[13] = algebraic[11]/constants[55]
    algebraic[0] = constants[4]*states[0]+constants[3]*log(constants[54]/states[1])
    algebraic[2] = constants[32]*(((exp(-(constants[9]-constants[5]*algebraic[0])/constants[3])*constants[15])/constants[14])*states[7]*states[3]-states[8]*1.00000)
    algebraic[3] = -0.650000*states[0]
    algebraic[4] = 0.350000*states[0]
    algebraic[10] = states[14]-states[15]
    algebraic[12] = custom_piecewise([greater(algebraic[10] , constants[45]) | greater(algebraic[8] , constants[45]), (constants[33]*(algebraic[10]/(algebraic[10]+algebraic[8]*exp((-constants[4]*algebraic[4])/constants[3]))-algebraic[7]/(algebraic[7]+algebraic[5]*exp((-constants[4]*algebraic[3])/constants[3])))*algebraic[10])/(constants[38]+algebraic[10]) , True, 0.00000])
    rates[9] = (algebraic[2]-algebraic[12])/constants[52]
    rates[11] = (-algebraic[2]+algebraic[12])/constants[52]
    algebraic[13] = constants[43]*(algebraic[10]*constants[58]-constants[15]*states[15])
    rates[15] = algebraic[13]/constants[55]
    algebraic[16] = (states[17]*constants[54])/(constants[54]+constants[48])
    algebraic[18] = (states[3]*states[1])/(states[1]+constants[48])
    algebraic[20] = (constants[34]*(states[1]*algebraic[16]-constants[54]*algebraic[18]))/(algebraic[16]+constants[26])
    rates[3] = (-algebraic[2]+algebraic[20])/constants[52]
    algebraic[15] = constants[18]*constants[40]*(constants[12]-states[12])
    algebraic[21] = constants[39]*(constants[16]*states[14]*states[14]-states[16]*states[12])
    rates[12] = (algebraic[15]+algebraic[12]+algebraic[21])/constants[55]
    algebraic[17] = constants[18]*constants[40]*(constants[2]-states[14])
    rates[14] = ((algebraic[17]-algebraic[12])-2.00000*algebraic[21])/constants[55]
    algebraic[19] = constants[18]*constants[40]*(constants[13]-states[16])
    rates[16] = (algebraic[19]+algebraic[21])/constants[55]
    algebraic[14] = constants[18]*constants[44]*(constants[1]-states[17])
    rates[17] = (-algebraic[20]+algebraic[14])/constants[55]
    algebraic[23] = (constants[37]*states[0]*(constants[51]*exp((constants[4]*states[0])/constants[3])-states[18]))/(exp((constants[4]*states[0])/constants[3])-1.00000)
    algebraic[24] = constants[35]*(constants[51]*states[1]-states[18]*constants[54])
    rates[18] = (algebraic[24]+algebraic[23])/constants[52]
    algebraic[25] = constants[21]-states[2]
    algebraic[26] = (constants[28]*(constants[27]*algebraic[25]-states[2])*(1.00000+states[3]/constants[22]))/(1.00000+states[3]/constants[23])
    algebraic[27] = constants[20]-states[4]
    algebraic[28] = (constants[6]-constants[3]*log(states[1]/1.00000e-07))-constants[3]*log(algebraic[27]/states[4])
    algebraic[29] = constants[29]*(exp(-(algebraic[28]+4.00000*algebraic[0])/constants[3])*states[2]-algebraic[25])
    rates[2] = (algebraic[26]-algebraic[29])/constants[52]
    algebraic[30] = (constants[7]+2.00000*constants[3]*log(states[1]/1.00000e-07))-constants[3]*log(states[4]/algebraic[27])
    algebraic[31] = constants[19]-states[5]
    algebraic[32] = ((constants[30]*(1.00000+states[3]/constants[24]))/(1.00000+states[3]/constants[25]))*(exp(-((algebraic[30]+4.00000*algebraic[0])-2.00000*constants[4]*states[0])/(2.00000*constants[3]))*algebraic[31]-states[5])
    rates[4] = (algebraic[29]-algebraic[32])/constants[52]
    algebraic[1] = (constants[8]-2.00000*constants[3]*log(states[1]/1.00000e-07))-(constants[3]/2.00000)*log(states[6]/1.00000)
    algebraic[33] = ((((constants[31]*1.00000)/(1.00000+constants[41]/states[6]))*states[5])/constants[19])*(exp(-(algebraic[1]+2.00000*algebraic[0])/(2.00000*constants[3]))*states[5]-algebraic[31]*exp((constants[4]*states[0])/constants[3]))
    algebraic[22] = (constants[36]*states[0]*(constants[54]*exp((constants[4]*states[0])/constants[3])-states[1]))/(exp((constants[4]*states[0])/constants[3])-1.00000)
    rates[1] = (constants[42]*states[1]*(((((algebraic[26]-5.00000*algebraic[29])-2.00000*algebraic[32])-4.00000*algebraic[33])+(constants[5]-1.00000)*algebraic[2]+2.00000*algebraic[20]+algebraic[22])-algebraic[24]))/constants[52]
    rates[5] = (2.00000*algebraic[32]-2.00000*algebraic[33])/constants[55]
    rates[0] = (((((4.00000*algebraic[29]+2.00000*algebraic[32]+4.00000*algebraic[33])-constants[5]*algebraic[2])-algebraic[12])-algebraic[22])-algebraic[23])/constants[46]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[5] = states[9]-states[8]
    algebraic[6] = constants[43]*(algebraic[5]*states[10]-constants[14]*states[8])
    algebraic[7] = states[11]-states[7]
    algebraic[9] = constants[43]*(algebraic[7]*states[10]-constants[15]*states[7])
    algebraic[8] = states[12]-states[13]
    algebraic[11] = constants[43]*(algebraic[8]*constants[58]-constants[14]*states[13])
    algebraic[0] = constants[4]*states[0]+constants[3]*log(constants[54]/states[1])
    algebraic[2] = constants[32]*(((exp(-(constants[9]-constants[5]*algebraic[0])/constants[3])*constants[15])/constants[14])*states[7]*states[3]-states[8]*1.00000)
    algebraic[3] = -0.650000*states[0]
    algebraic[4] = 0.350000*states[0]
    algebraic[10] = states[14]-states[15]
    algebraic[12] = custom_piecewise([greater(algebraic[10] , constants[45]) | greater(algebraic[8] , constants[45]), (constants[33]*(algebraic[10]/(algebraic[10]+algebraic[8]*exp((-constants[4]*algebraic[4])/constants[3]))-algebraic[7]/(algebraic[7]+algebraic[5]*exp((-constants[4]*algebraic[3])/constants[3])))*algebraic[10])/(constants[38]+algebraic[10]) , True, 0.00000])
    algebraic[13] = constants[43]*(algebraic[10]*constants[58]-constants[15]*states[15])
    algebraic[16] = (states[17]*constants[54])/(constants[54]+constants[48])
    algebraic[18] = (states[3]*states[1])/(states[1]+constants[48])
    algebraic[20] = (constants[34]*(states[1]*algebraic[16]-constants[54]*algebraic[18]))/(algebraic[16]+constants[26])
    algebraic[15] = constants[18]*constants[40]*(constants[12]-states[12])
    algebraic[21] = constants[39]*(constants[16]*states[14]*states[14]-states[16]*states[12])
    algebraic[17] = constants[18]*constants[40]*(constants[2]-states[14])
    algebraic[19] = constants[18]*constants[40]*(constants[13]-states[16])
    algebraic[14] = constants[18]*constants[44]*(constants[1]-states[17])
    algebraic[23] = (constants[37]*states[0]*(constants[51]*exp((constants[4]*states[0])/constants[3])-states[18]))/(exp((constants[4]*states[0])/constants[3])-1.00000)
    algebraic[24] = constants[35]*(constants[51]*states[1]-states[18]*constants[54])
    algebraic[25] = constants[21]-states[2]
    algebraic[26] = (constants[28]*(constants[27]*algebraic[25]-states[2])*(1.00000+states[3]/constants[22]))/(1.00000+states[3]/constants[23])
    algebraic[27] = constants[20]-states[4]
    algebraic[28] = (constants[6]-constants[3]*log(states[1]/1.00000e-07))-constants[3]*log(algebraic[27]/states[4])
    algebraic[29] = constants[29]*(exp(-(algebraic[28]+4.00000*algebraic[0])/constants[3])*states[2]-algebraic[25])
    algebraic[30] = (constants[7]+2.00000*constants[3]*log(states[1]/1.00000e-07))-constants[3]*log(states[4]/algebraic[27])
    algebraic[31] = constants[19]-states[5]
    algebraic[32] = ((constants[30]*(1.00000+states[3]/constants[24]))/(1.00000+states[3]/constants[25]))*(exp(-((algebraic[30]+4.00000*algebraic[0])-2.00000*constants[4]*states[0])/(2.00000*constants[3]))*algebraic[31]-states[5])
    algebraic[1] = (constants[8]-2.00000*constants[3]*log(states[1]/1.00000e-07))-(constants[3]/2.00000)*log(states[6]/1.00000)
    algebraic[33] = ((((constants[31]*1.00000)/(1.00000+constants[41]/states[6]))*states[5])/constants[19])*(exp(-(algebraic[1]+2.00000*algebraic[0])/(2.00000*constants[3]))*states[5]-algebraic[31]*exp((constants[4]*states[0])/constants[3]))
    algebraic[22] = (constants[36]*states[0]*(constants[54]*exp((constants[4]*states[0])/constants[3])-states[1]))/(exp((constants[4]*states[0])/constants[3])-1.00000)
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
        self.Mg_tot = 0.005
        self.Pi_e = 0.000125
        self.ADP_e = 0
        self.RT = 2.4734
        self.F = 0.096484
        self.n_A = 3
        self.dG_C1o = -69.37
        self.dG_C3o = -32.53
        self.dG_C4o = -122.94
        self.dG_F1o = 36.03
        self.pH_e = 7.1
        self.K_e = 0.15
        self.ATP_e = 0
        self.AMP_e = 0
        self.K_DT = 2.4e-5
        self.K_DD = 3.47e-4
        self.K_AK = 0.4331
        self.W_m = 0.72376
        self.gamma = 5.99
        self.Ctot = 0.0027
        self.Qtot = 0.00135
        self.NADtot = 0.00297
        self.k_Pi1 = 1.3413e-4
        self.k_Pi2 = 6.7668e-4
        self.k_Pi3 = 1.9172e-4
        self.k_Pi4 = 0.02531
        self.k_PiH = 4.5082e-4
        self.r = 4.5807
        self.x_DH = 0.09183
        self.x_C1 = 0.36923
        self.x_C3 = 0.091737
        self.x_C4 = 3.2562e-5
        self.x_F1 = 150.93
        self.x_ANT = 0.0079204
        self.x_Pi1 = 339430
        self.x_KH = 2.9802e7
        self.x_Hle = 250
        self.x_K = 0
        self.k_mADP = 3.5e-6
        self.x_AK = 0
        self.p_A = 85
        self.k_O2 = 1.2e-4
        self.x_buff = 100
        self.x_MgA = 1000000
        self.x_Pi2 = 327
        self.mincond = 1e-12
        self.C_im = 6.756756756756757e-6
        self.k_dHPi = 1.00000*(power(10.0000, -6.75000))
        self.k_dHatp = 1.00000*(power(10.0000, -6.48000))
        self.k_dHadp = 1.00000*(power(10.0000, -6.29000))
        self.legend_constants_59 = 0.00000

    def to_dict(self):
        return {
            "Mg_tot": self.Mg_tot,
            "Pi_e": self.Pi_e,
            "ADP_e": self.ADP_e,
            "RT": self.RT,
            "F": self.F,
            "n_A": self.n_A,
            "dG_C1o": self.dG_C1o,
            "dG_C3o": self.dG_C3o,
            "dG_C4o": self.dG_C4o,
            "dG_F1o": self.dG_F1o,
            "pH_e": self.pH_e,
            "K_e": self.K_e,
            "ATP_e": self.ATP_e,
            "AMP_e": self.AMP_e,
            "K_DT": self.K_DT,
            "K_DD": self.K_DD,
            "K_AK": self.K_AK,
            "W_m": self.W_m,
            "gamma": self.gamma,
            "Ctot": self.Ctot,
            "Qtot": self.Qtot,
            "NADtot": self.NADtot,
            "k_Pi1": self.k_Pi1,
            "k_Pi2": self.k_Pi2,
            "k_Pi3": self.k_Pi3,
            "k_Pi4": self.k_Pi4,
            "k_PiH": self.k_PiH,
            "r": self.r,
            "x_DH": self.x_DH,
            "x_C1": self.x_C1,
            "x_C3": self.x_C3,
            "x_C4": self.x_C4,
            "x_F1": self.x_F1,
            "x_ANT": self.x_ANT,
            "x_Pi1": self.x_Pi1,
            "x_KH": self.x_KH,
            "x_Hle": self.x_Hle,
            "x_K": self.x_K,
            "k_mADP": self.k_mADP,
            "x_AK": self.x_AK,
            "p_A": self.p_A,
            "k_O2": self.k_O2,
            "x_buff": self.x_buff,
            "x_MgA": self.x_MgA,
            "x_Pi2": self.x_Pi2,
            "mincond": self.mincond,
            "C_im": self.C_im,
            "k_dHPi": self.k_dHPi,
            "k_dHatp": self.k_dHatp,
            "k_dHadp": self.k_dHadp,
            "legend_constants_59": self.legend_constants_59,
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
        y0=[160, 6.30957344480193e-8, 0.0015, 0.001, 8e-4, 0.001, 2.6e-5, 0, 0, 0, 0.005, 0.01, 0, 0, 0, 0, 0, 0.001, 0.14],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "beard_2005"
        self.curve_names = [
            "dPsi",
            "H_x",
            "NADH_x",
            "Pi_x",
            "QH2",
            "Cred",
            "O2",
            "ADP_mx",
            "ATP_mx",
            "ATP_x",
            "Mg_x",
            "ADP_x",
            "ATP_i",
            "ATP_mi",
            "ADP_i",
            "ADP_mi",
            "AMP_i",
            "Pi_i",
            "K_x",
        ]
        self.state_names = ['dPsi', 'H_x', 'NADH_x', 'Pi_x', 'QH2', 'Cred', 'O2', 'ADP_mx', 'ATP_mx', 'ATP_x', 'Mg_x', 'ADP_x', 'ATP_i', 'ATP_mi', 'ADP_i', 'ADP_mi', 'AMP_i', 'Pi_i', 'K_x']
        self.algebraic_names = ['dG_H', 'dG_C4op', 'J_F1', 'Psi_x', 'Psi_i', 'ATP_fx', 'J_MgATPx', 'ADP_fx', 'ATP_fi', 'J_MgADPx', 'ADP_fi', 'J_MgATPi', 'J_ANT', 'J_MgADPi', 'J_Pi2', 'J_ATP', 'H2PIi', 'J_ADP', 'H2PIx', 'J_AMP', 'J_Pi1', 'J_AKi', 'J_Hle', 'J_K', 'J_KH', 'NAD_x', 'J_DH', 'Q', 'dG_C1op', 'J_C1', 'dG_C3op', 'Cox', 'J_C3', 'J_C4']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 60
        p = self.params

        # direct mapping
        c[0] = p.Mg_tot
        c[1] = p.Pi_e
        c[2] = p.ADP_e
        c[3] = p.RT
        c[4] = p.F
        c[5] = p.n_A
        c[6] = p.dG_C1o
        c[7] = p.dG_C3o
        c[8] = p.dG_C4o
        c[9] = p.dG_F1o
        c[10] = p.pH_e
        c[11] = p.K_e
        c[12] = p.ATP_e
        c[13] = p.AMP_e
        c[14] = p.K_DT
        c[15] = p.K_DD
        c[16] = p.K_AK
        c[17] = p.W_m
        c[18] = p.gamma
        c[19] = p.Ctot
        c[20] = p.Qtot
        c[21] = p.NADtot
        c[22] = p.k_Pi1
        c[23] = p.k_Pi2
        c[24] = p.k_Pi3
        c[25] = p.k_Pi4
        c[26] = p.k_PiH
        c[27] = p.r
        c[28] = p.x_DH
        c[29] = p.x_C1
        c[30] = p.x_C3
        c[31] = p.x_C4
        c[32] = p.x_F1
        c[33] = p.x_ANT
        c[34] = p.x_Pi1
        c[35] = p.x_KH
        c[36] = p.x_Hle
        c[37] = p.x_K
        c[38] = p.k_mADP
        c[39] = p.x_AK
        c[40] = p.p_A
        c[41] = p.k_O2
        c[42] = p.x_buff
        c[43] = p.x_MgA
        c[44] = p.x_Pi2
        c[45] = p.mincond
        c[46] = p.C_im
        c[48] = p.k_dHPi
        c[49] = p.k_dHatp
        c[50] = p.k_dHadp
        c[59] = p.legend_constants_59

        # derived constants
        c[47] = 1.00000*(power(10.0000, -c[10]))
        c[51] = c[11]
        c[52] = 0.900000*c[17]
        c[53] = ((c[15]+c[2]+c[0])-power(power(c[15]+c[2]+c[0], 2.00000)-4.00000*c[0]*c[2], 1.0/2))/2.00000
        c[54] = c[47]
        c[55] = 0.100000*c[17]
        c[56] = c[2]-c[53]
        c[57] = c[0]-c[53]
        c[58] = c[57]

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
