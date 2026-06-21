# Size of variable arrays:
sizeAlgebraic = 50
sizeStates = 11
sizeConstants = 71
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (millisecond)"
    legend_algebraic[3] = "SOVFThick in component sarcomere_geometry (dimensionless)"
    legend_algebraic[4] = "SOVFThin in component sarcomere_geometry (dimensionless)"
    legend_algebraic[0] = "sovr_ze in component sarcomere_geometry (micrometre)"
    legend_algebraic[1] = "sovr_cle in component sarcomere_geometry (micrometre)"
    legend_algebraic[2] = "len_sovr in component sarcomere_geometry (micrometre)"
    legend_constants[0] = "len_thin in component model_parameters (micrometre)"
    legend_constants[1] = "len_thick in component model_parameters (micrometre)"
    legend_constants[2] = "len_hbare in component model_parameters (micrometre)"
    legend_states[0] = "SL in component normalised_active_and_passive_force (micrometre)"
    legend_states[1] = "TRPNCaL in component Ca_binding_to_troponin_to_thin_filament_regulation (dimensionless)"
    legend_states[2] = "TRPNCaH in component Ca_binding_to_troponin_to_thin_filament_regulation (dimensionless)"
    legend_algebraic[7] = "dTRPNCaL in component Ca_binding_to_troponin_to_thin_filament_regulation (first_order_rate_constant)"
    legend_algebraic[10] = "dTRPNCaH in component Ca_binding_to_troponin_to_thin_filament_regulation (first_order_rate_constant)"
    legend_algebraic[12] = "kn_pT in component Ca_binding_to_troponin_to_thin_filament_regulation (first_order_rate_constant)"
    legend_algebraic[18] = "kp_nT in component Ca_binding_to_troponin_to_thin_filament_regulation (first_order_rate_constant)"
    legend_constants[60] = "H in component Ca_binding_to_troponin_to_thin_filament_regulation (micromolar)"
    legend_constants[62] = "H_cons in component Ca_binding_to_troponin_to_thin_filament_regulation (micromolar)"
    legend_constants[63] = "konT in component Ca_binding_to_troponin_to_thin_filament_regulation (second_order_rate_constant)"
    legend_constants[58] = "koffLT in component Ca_binding_to_troponin_to_thin_filament_regulation (first_order_rate_constant)"
    legend_constants[59] = "koffHT in component Ca_binding_to_troponin_to_thin_filament_regulation (first_order_rate_constant)"
    legend_constants[3] = "Qkon in component Ca_binding_to_troponin_to_thin_filament_regulation (dimensionless)"
    legend_constants[4] = "Qkoff in component Ca_binding_to_troponin_to_thin_filament_regulation (dimensionless)"
    legend_constants[5] = "Qkn_p in component Ca_binding_to_troponin_to_thin_filament_regulation (dimensionless)"
    legend_constants[6] = "Qkp_n in component Ca_binding_to_troponin_to_thin_filament_regulation (dimensionless)"
    legend_constants[7] = "kon in component Ca_binding_to_troponin_to_thin_filament_regulation (second_order_rate_constant)"
    legend_constants[8] = "koffL in component Ca_binding_to_troponin_to_thin_filament_regulation (first_order_rate_constant)"
    legend_constants[9] = "koffH in component Ca_binding_to_troponin_to_thin_filament_regulation (first_order_rate_constant)"
    legend_constants[10] = "perm50 in component Ca_binding_to_troponin_to_thin_filament_regulation (dimensionless)"
    legend_constants[11] = "nperm in component Ca_binding_to_troponin_to_thin_filament_regulation (dimensionless)"
    legend_constants[12] = "kn_p in component Ca_binding_to_troponin_to_thin_filament_regulation (first_order_rate_constant)"
    legend_constants[13] = "kp_n in component Ca_binding_to_troponin_to_thin_filament_regulation (first_order_rate_constant)"
    legend_constants[14] = "koffmod in component Ca_binding_to_troponin_to_thin_filament_regulation (dimensionless)"
    legend_algebraic[6] = "Tropreg in component Ca_binding_to_troponin_to_thin_filament_regulation (dimensionless)"
    legend_algebraic[9] = "permtot in component Ca_binding_to_troponin_to_thin_filament_regulation (dimensionless)"
    legend_algebraic[15] = "inprmt in component Ca_binding_to_troponin_to_thin_filament_regulation (dimensionless)"
    legend_constants[15] = "pH in component Ca_binding_to_troponin_to_thin_filament_regulation (dimensionless)"
    legend_constants[16] = "m in component Ca_binding_to_troponin_to_thin_filament_regulation (dimensionless)"
    legend_constants[17] = "kdHCa in component Ca_binding_to_troponin_to_thin_filament_regulation (micromolar)"
    legend_constants[18] = "TmpC in component model_parameters (celsius)"
    legend_constants[19] = "Cai in component model_parameters (micromolar)"
    legend_constants[64] = "fappT in component thin_filament_regulation_and_crossbridge_cycling_rates (first_order_rate_constant)"
    legend_algebraic[16] = "gappT in component thin_filament_regulation_and_crossbridge_cycling_rates (first_order_rate_constant)"
    legend_algebraic[23] = "hfT in component thin_filament_regulation_and_crossbridge_cycling_rates (first_order_rate_constant)"
    legend_algebraic[24] = "hbT in component thin_filament_regulation_and_crossbridge_cycling_rates (first_order_rate_constant)"
    legend_algebraic[26] = "gxbT in component thin_filament_regulation_and_crossbridge_cycling_rates (first_order_rate_constant)"
    legend_constants[20] = "fapp in component thin_filament_regulation_and_crossbridge_cycling_rates (first_order_rate_constant)"
    legend_constants[21] = "gapp in component thin_filament_regulation_and_crossbridge_cycling_rates (first_order_rate_constant)"
    legend_constants[22] = "hf in component thin_filament_regulation_and_crossbridge_cycling_rates (first_order_rate_constant)"
    legend_constants[23] = "hb in component thin_filament_regulation_and_crossbridge_cycling_rates (first_order_rate_constant)"
    legend_constants[24] = "gxb in component thin_filament_regulation_and_crossbridge_cycling_rates (first_order_rate_constant)"
    legend_constants[25] = "gslmod in component thin_filament_regulation_and_crossbridge_cycling_rates (dimensionless)"
    legend_algebraic[19] = "hfmd in component thin_filament_regulation_and_crossbridge_cycling_rates (dimensionless)"
    legend_algebraic[21] = "hbmd in component thin_filament_regulation_and_crossbridge_cycling_rates (dimensionless)"
    legend_constants[26] = "hfmdc in component thin_filament_regulation_and_crossbridge_cycling_rates (dimensionless)"
    legend_constants[27] = "hbmdc in component thin_filament_regulation_and_crossbridge_cycling_rates (dimensionless)"
    legend_constants[28] = "sigmap in component thin_filament_regulation_and_crossbridge_cycling_rates (dimensionless)"
    legend_constants[29] = "sigman in component thin_filament_regulation_and_crossbridge_cycling_rates (dimensionless)"
    legend_constants[30] = "xbmodsp in component thin_filament_regulation_and_crossbridge_cycling_rates (dimensionless)"
    legend_constants[31] = "Qfapp in component thin_filament_regulation_and_crossbridge_cycling_rates (dimensionless)"
    legend_constants[32] = "Qgapp in component thin_filament_regulation_and_crossbridge_cycling_rates (dimensionless)"
    legend_constants[33] = "Qhf in component thin_filament_regulation_and_crossbridge_cycling_rates (dimensionless)"
    legend_constants[34] = "Qhb in component thin_filament_regulation_and_crossbridge_cycling_rates (dimensionless)"
    legend_constants[35] = "Qgxb in component thin_filament_regulation_and_crossbridge_cycling_rates (dimensionless)"
    legend_algebraic[25] = "gxbmd in component thin_filament_regulation_and_crossbridge_cycling_rates (dimensionless)"
    legend_algebraic[13] = "gapslmd in component thin_filament_regulation_and_crossbridge_cycling_rates (dimensionless)"
    legend_constants[36] = "x_0 in component model_parameters (micrometre)"
    legend_states[3] = "xXBpostr in component mean_strain_of_strongly_bound_states (micrometre)"
    legend_states[4] = "xXBprer in component mean_strain_of_strongly_bound_states (micrometre)"
    legend_states[5] = "XBpostr in component regulation_and_crossbridge_cycling_state_equations (dimensionless)"
    legend_states[6] = "XBprer in component regulation_and_crossbridge_cycling_state_equations (dimensionless)"
    legend_algebraic[34] = "dXBpostr in component regulation_and_crossbridge_cycling_state_equations (first_order_rate_constant)"
    legend_algebraic[31] = "dXBprer in component regulation_and_crossbridge_cycling_state_equations (first_order_rate_constant)"
    legend_constants[65] = "alpha1_plus in component regulation_and_crossbridge_cycling_state_equations (first_order_rate_constant)"
    legend_algebraic[27] = "alpha2_plus in component regulation_and_crossbridge_cycling_state_equations (first_order_rate_constant)"
    legend_algebraic[28] = "alpha3_plus in component regulation_and_crossbridge_cycling_state_equations (first_order_rate_constant)"
    legend_algebraic[29] = "alpha1_minus in component regulation_and_crossbridge_cycling_state_equations (first_order_rate_constant)"
    legend_algebraic[30] = "alpha2_minus in component regulation_and_crossbridge_cycling_state_equations (first_order_rate_constant)"
    legend_algebraic[33] = "alpha3_minus in component regulation_and_crossbridge_cycling_state_equations (first_order_rate_constant)"
    legend_constants[37] = "kMgATP in component regulation_and_crossbridge_cycling_state_equations (micromolar2)"
    legend_constants[38] = "kdADP in component regulation_and_crossbridge_cycling_state_equations (micromolar)"
    legend_constants[39] = "xPi_cons in component regulation_and_crossbridge_cycling_state_equations (micromolar)"
    legend_constants[40] = "MgATP_cons in component regulation_and_crossbridge_cycling_state_equations (micromolar)"
    legend_algebraic[32] = "fxbT in component regulation_and_crossbridge_cycling_state_equations (first_order_rate_constant)"
    legend_states[7] = "N_NoXB in component regulation_and_crossbridge_cycling_state_equations (dimensionless)"
    legend_states[8] = "P_NoXB in component regulation_and_crossbridge_cycling_state_equations (dimensionless)"
    legend_states[9] = "P in component regulation_and_crossbridge_cycling_state_equations (dimensionless)"
    legend_algebraic[22] = "N in component regulation_and_crossbridge_cycling_state_equations (dimensionless)"
    legend_constants[41] = "MgADP_cons in component regulation_and_crossbridge_cycling_state_equations (micromolar)"
    legend_constants[42] = "xPi in component regulation_and_crossbridge_cycling_state_equations (micromolar)"
    legend_constants[43] = "MgATP in component regulation_and_crossbridge_cycling_state_equations (micromolar)"
    legend_constants[44] = "MgADP in component regulation_and_crossbridge_cycling_state_equations (micromolar)"
    legend_algebraic[38] = "dxXBpostr in component mean_strain_of_strongly_bound_states (micrometre_per_millisecond)"
    legend_algebraic[36] = "dxXBprer in component mean_strain_of_strongly_bound_states (micrometre_per_millisecond)"
    legend_constants[45] = "xPsi in component mean_strain_of_strongly_bound_states (dimensionless)"
    legend_algebraic[35] = "dutyprer in component mean_strain_of_strongly_bound_states (dimensionless)"
    legend_algebraic[37] = "dutypostr in component mean_strain_of_strongly_bound_states (dimensionless)"
    legend_constants[61] = "dSL in component normalised_active_and_passive_force (micrometre_per_millisecond)"
    legend_constants[67] = "SSXBpostr in component normalised_active_and_passive_force (dimensionless)"
    legend_algebraic[39] = "SSXBprer in component normalised_active_and_passive_force (dimensionless)"
    legend_constants[46] = "kxb in component normalised_active_and_passive_force (millinewton_per_millimetre2)"
    legend_constants[68] = "Fnordv in component normalised_active_and_passive_force (millinewton_micrometre_per_millimetre2)"
    legend_algebraic[5] = "force in component normalised_active_and_passive_force (millinewton_micrometre_per_millimetre2)"
    legend_algebraic[8] = "active in component normalised_active_and_passive_force (unit_normalised_force)"
    legend_algebraic[17] = "ppforce in component normalised_active_and_passive_force (unit_normalised_force)"
    legend_algebraic[11] = "ppforce_t in component normalised_active_and_passive_force (unit_normalised_force)"
    legend_algebraic[14] = "ppforce_c in component normalised_active_and_passive_force (unit_normalised_force)"
    legend_constants[69] = "preload in component normalised_active_and_passive_force (unit_normalised_force)"
    legend_algebraic[20] = "afterload in component normalised_active_and_passive_force (unit_normalised_force)"
    legend_states[10] = "intf in component normalised_active_and_passive_force (unit_normalised_force_millisecond)"
    legend_constants[47] = "SL_c in component normalised_active_and_passive_force (micrometre)"
    legend_constants[48] = "SLrest in component normalised_active_and_passive_force (micrometre)"
    legend_constants[49] = "SLset in component normalised_active_and_passive_force (micrometre)"
    legend_constants[50] = "PCon_t in component normalised_active_and_passive_force (unit_normalised_force)"
    legend_constants[51] = "PExp_t in component normalised_active_and_passive_force (per_micrometre)"
    legend_constants[52] = "PCon_c in component normalised_active_and_passive_force (unit_normalised_force)"
    legend_constants[53] = "PExp_c in component normalised_active_and_passive_force (per_micrometre)"
    legend_constants[54] = "KSE in component normalised_active_and_passive_force (unit_normalised_force_per_micrometre)"
    legend_constants[66] = "fxb in component normalised_active_and_passive_force (first_order_rate_constant)"
    legend_constants[55] = "SEon in component normalised_active_and_passive_force (dimensionless)"
    legend_algebraic[40] = "FrSBXB in component calculation_of_micromolar_per_millisecondes_of_Ca_for_apparent_Ca_binding (dimensionless)"
    legend_algebraic[41] = "dFrSBXB in component calculation_of_micromolar_per_millisecondes_of_Ca_for_apparent_Ca_binding (first_order_rate_constant)"
    legend_algebraic[43] = "dsovr_ze in component calculation_of_micromolar_per_millisecondes_of_Ca_for_apparent_Ca_binding (micrometre_per_millisecond)"
    legend_algebraic[44] = "dsovr_cle in component calculation_of_micromolar_per_millisecondes_of_Ca_for_apparent_Ca_binding (micrometre_per_millisecond)"
    legend_algebraic[45] = "dlen_sovr in component calculation_of_micromolar_per_millisecondes_of_Ca_for_apparent_Ca_binding (micrometre_per_millisecond)"
    legend_algebraic[46] = "dSOVFThick in component calculation_of_micromolar_per_millisecondes_of_Ca_for_apparent_Ca_binding (first_order_rate_constant)"
    legend_algebraic[47] = "dSOVFThin in component calculation_of_micromolar_per_millisecondes_of_Ca_for_apparent_Ca_binding (first_order_rate_constant)"
    legend_constants[56] = "kxb in component calculation_of_micromolar_per_millisecondes_of_Ca_for_apparent_Ca_binding (millinewton_per_millimetre2)"
    legend_algebraic[48] = "dforce in component calculation_of_micromolar_per_millisecondes_of_Ca_for_apparent_Ca_binding (millinewton_micrometre_per_millimetre2_per_millisecond)"
    legend_constants[57] = "Trop_conc in component calculation_of_micromolar_per_millisecondes_of_Ca_for_apparent_Ca_binding (micromolar)"
    legend_algebraic[42] = "TropTot in component calculation_of_micromolar_per_millisecondes_of_Ca_for_apparent_Ca_binding (micromolar)"
    legend_algebraic[49] = "dTropTot in component calculation_of_micromolar_per_millisecondes_of_Ca_for_apparent_Ca_binding (micromolar_per_millisecond)"
    legend_rates[1] = "d/dt TRPNCaL in component Ca_binding_to_troponin_to_thin_filament_regulation (dimensionless)"
    legend_rates[2] = "d/dt TRPNCaH in component Ca_binding_to_troponin_to_thin_filament_regulation (dimensionless)"
    legend_rates[7] = "d/dt N_NoXB in component regulation_and_crossbridge_cycling_state_equations (dimensionless)"
    legend_rates[8] = "d/dt P_NoXB in component regulation_and_crossbridge_cycling_state_equations (dimensionless)"
    legend_rates[9] = "d/dt P in component regulation_and_crossbridge_cycling_state_equations (dimensionless)"
    legend_rates[6] = "d/dt XBprer in component regulation_and_crossbridge_cycling_state_equations (dimensionless)"
    legend_rates[5] = "d/dt XBpostr in component regulation_and_crossbridge_cycling_state_equations (dimensionless)"
    legend_rates[4] = "d/dt xXBprer in component mean_strain_of_strongly_bound_states (micrometre)"
    legend_rates[3] = "d/dt xXBpostr in component mean_strain_of_strongly_bound_states (micrometre)"
    legend_rates[0] = "d/dt SL in component normalised_active_and_passive_force (micrometre)"
    legend_rates[10] = "d/dt intf in component normalised_active_and_passive_force (unit_normalised_force_millisecond)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    constants[0] = 1.2
    constants[1] = 1.65
    constants[2] = 0.1
    states[0] = 2.2
    states[1] = 0.0147730085063734
    states[2] = 0.13066096561522
    constants[3] = 1.5
    constants[4] = 1.3
    constants[5] = 1.6
    constants[6] = 1.6
    constants[7] = 0.05
    constants[8] = 0.25
    constants[9] = 0.025
    constants[10] = 0.5
    constants[11] = 15
    constants[12] = 0.5
    constants[13] = 0.05
    constants[14] = 1
    constants[15] = 7.15
    constants[16] = 1
    constants[17] = 2e-2
    constants[18] = 22
    constants[19] = 200.0
    constants[20] = 0.5
    constants[21] = 0.07
    constants[22] = 2
    constants[23] = 0.4
    constants[24] = 0.07
    constants[25] = 6
    constants[26] = 5
    constants[27] = 0
    constants[28] = 8
    constants[29] = 1
    constants[30] = 0.2
    constants[31] = 6.25
    constants[32] = 2.5
    constants[33] = 6.25
    constants[34] = 6.25
    constants[35] = 6.25
    constants[36] = 0.007
    states[3] = 0.00700005394873882
    states[4] = 3.41212828972468e-8
    states[5] = 1.81017564383744e-6
    states[6] = 3.0494964880038e-7
    constants[37] = 15400e6
    constants[38] = 4
    constants[39] = 2e3
    constants[40] = 5e3
    states[7] = 0.999999959256274
    states[8] = 4.07437173988636e-8
    states[9] = 0.999997834540066
    constants[41] = 36
    constants[42] = 2e3
    constants[43] = 5e3
    constants[44] = 36.3
    constants[45] = 2
    constants[46] = 120
    states[10] = -4.5113452510363e-6
    constants[47] = 2.25
    constants[48] = 1.85
    constants[49] = 1.9
    constants[50] = 0.002
    constants[51] = 10
    constants[52] = 0.02
    constants[53] = 70
    constants[54] = 1
    constants[55] = 1
    constants[56] = 120
    constants[57] = 70
    constants[58] = constants[8]*constants[14]*(power(constants[4], (constants[18]-37.0000)/10.0000))
    constants[59] = constants[9]*constants[14]*(power(constants[4], (constants[18]-37.0000)/10.0000))
    constants[60] = 1.00000e+07*(power(10.0000, -constants[15]))
    constants[61] = 0.00000
    constants[62] = 1.00000e+07*(power(10.0000, -7.15000))
    constants[70] = constants[61]
    constants[63] = ((power(constants[17], constants[16])+power(constants[62], constants[16]))/(power(constants[17], constants[16])+power(constants[60], constants[16])))*(constants[7]*(power(constants[3], (constants[18]-37.0000)/10.0000)))
    constants[64] = constants[20]*constants[30]*(power(constants[31], (constants[18]-37.0000)/10.0000))
    constants[65] = constants[64]
    constants[66] = (constants[38]*constants[20]*constants[22]*(constants[24]/constants[40]))/((constants[21]/constants[39])*(constants[23]/constants[62])*constants[37])
    constants[67] = (constants[20]*constants[22]+constants[66]*constants[21]+constants[66]*constants[23])/(constants[22]*constants[24]+constants[23]*constants[21]+constants[24]*constants[21]+constants[66]*constants[23]+constants[24]*constants[20]+constants[23]*constants[20]+constants[66]*constants[21]+constants[20]*constants[22]+constants[66]*constants[23])
    constants[68] = constants[46]*constants[36]*constants[67]
    constants[69] = (fabs(constants[49]-constants[48])/(constants[49]-constants[48]))*constants[50]*(exp(constants[51]*fabs(constants[49]-constants[48]))-1.00000)
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[0] = constants[70]
    algebraic[7] = constants[63]*constants[19]*(1.00000-states[1])-constants[58]*states[1]
    rates[1] = algebraic[7]
    algebraic[10] = constants[63]*constants[19]*(1.00000-states[2])-constants[59]*states[2]
    rates[2] = algebraic[10]
    algebraic[0] = custom_piecewise([less(constants[1]/2.00000 , states[0]/2.00000), constants[1]/2.00000 , True, states[0]/2.00000])
    algebraic[1] = custom_piecewise([greater(states[0]/2.00000-(states[0]-constants[0]) , constants[2]/2.00000), states[0]/2.00000-(states[0]-constants[0]) , True, constants[2]/2.00000])
    algebraic[2] = algebraic[0]-algebraic[1]
    algebraic[4] = algebraic[2]/constants[0]
    algebraic[6] = (1.00000-algebraic[4])*states[1]+algebraic[4]*states[2]
    algebraic[9] = power(fabs(1.00000/(1.00000+power(constants[10]/algebraic[6], constants[11]))), 1.0/2)
    algebraic[12] = constants[12]*algebraic[9]*(power(constants[5], (constants[18]-37.0000)/10.0000))
    algebraic[15] = custom_piecewise([less(1.00000/algebraic[9] , 100.000), 1.00000/algebraic[9] , True, 100.000])
    algebraic[18] = constants[13]*algebraic[15]*(power(constants[6], (constants[18]-37.0000)/10.0000))
    rates[7] = algebraic[18]*states[8]-algebraic[12]*states[7]
    rates[8] = algebraic[12]*states[7]-algebraic[18]*states[8]
    algebraic[3] = (algebraic[2]*2.00000)/(constants[1]-constants[2])
    algebraic[5] = constants[46]*algebraic[3]*(states[3]*states[5]+states[4]*states[6])
    algebraic[8] = (1.00000*algebraic[5])/constants[68]
    algebraic[11] = ((states[0]-constants[48])/fabs(states[0]-constants[48]))*constants[50]*(exp(constants[51]*fabs(states[0]-constants[48]))-1.00000)
    algebraic[14] = custom_piecewise([greater(states[0] , constants[47]), constants[52]*(exp(constants[53]*fabs(states[0]-constants[47]))-1.00000) , True, 0.00000])
    algebraic[17] = algebraic[11]+algebraic[14]
    algebraic[20] = custom_piecewise([equal(constants[55] , 1.00000), constants[54]*(constants[49]-states[0]) , True, 0.00000])
    rates[10] = (constants[69]+algebraic[20])-(algebraic[17]+algebraic[8])
    algebraic[22] = 1.00000-(states[9]+states[6]+states[5])
    rates[9] = algebraic[12]*algebraic[22]-(algebraic[18]+constants[65])*states[9]
    algebraic[19] = exp((-states[4]/fabs(states[4]))*constants[26]*(power(states[4]/constants[36], 2.00000)))
    algebraic[23] = constants[22]*algebraic[19]*constants[30]*(power(constants[33], (constants[18]-37.0000)/10.0000))
    algebraic[27] = algebraic[23]
    algebraic[13] = 1.00000+(1.00000-algebraic[3])*constants[25]
    algebraic[16] = constants[21]*algebraic[13]*constants[30]*(power(constants[32], (constants[18]-37.0000)/10.0000))
    algebraic[29] = constants[42]*(algebraic[16]/constants[39])
    algebraic[21] = exp(((states[3]-constants[36])/fabs(states[3]-constants[36]))*constants[27]*(power((states[3]-constants[36])/constants[36], 2.00000)))
    algebraic[24] = constants[23]*algebraic[21]*constants[30]*(power(constants[34], (constants[18]-37.0000)/10.0000))
    algebraic[30] = constants[60]*(algebraic[24]/constants[62])*((constants[38]+constants[41])/constants[41])*(constants[44]/(constants[38]+constants[44]))
    algebraic[31] = (constants[65]*states[9]+algebraic[30]*states[5])-(algebraic[29]+algebraic[27])*states[6]
    rates[6] = algebraic[31]
    algebraic[25] = custom_piecewise([less(states[3] , constants[36]), exp(constants[28]*(power((constants[36]-states[3])/constants[36], 2.00000))) , True, exp(constants[29]*(power((states[3]-constants[36])/constants[36], 2.00000)))])
    algebraic[26] = constants[24]*algebraic[25]*constants[30]*(power(constants[35], (constants[18]-37.0000)/10.0000))
    algebraic[28] = constants[43]*(algebraic[26]/constants[40])*((constants[38]+constants[41])/(constants[38]+constants[44]))
    algebraic[32] = (constants[38]*constants[64]*algebraic[23]*(algebraic[26]/constants[40]))/((algebraic[16]/constants[39])*(algebraic[24]/constants[62])*constants[37])
    algebraic[33] = algebraic[32]
    algebraic[34] = (algebraic[33]*states[9]+algebraic[27]*states[6])-(algebraic[30]+algebraic[28])*states[5]
    rates[5] = algebraic[34]
    algebraic[35] = (algebraic[33]*algebraic[30]+algebraic[28]*constants[65]+algebraic[30]*constants[65])/(constants[65]*algebraic[27]+algebraic[33]*algebraic[29]+algebraic[33]*algebraic[27]+algebraic[33]*algebraic[30]+algebraic[28]*constants[65]+algebraic[30]*constants[65]+algebraic[27]*algebraic[28]+algebraic[33]*algebraic[29]+algebraic[28]*algebraic[29])
    algebraic[36] = constants[61]/2.00000+(constants[45]/algebraic[35])*(-(constants[65]*states[4])+algebraic[30]*(states[3]-(constants[36]+states[4])))
    rates[4] = algebraic[36]
    algebraic[37] = (constants[65]*algebraic[27]+algebraic[33]*algebraic[29]+algebraic[33]*algebraic[27])/(constants[65]*algebraic[27]+algebraic[33]*algebraic[29]+algebraic[33]*algebraic[27]+algebraic[33]*algebraic[30]+algebraic[28]*constants[65]+algebraic[30]*constants[65]+algebraic[27]*algebraic[28]+algebraic[33]*algebraic[29]+algebraic[28]*algebraic[29])
    algebraic[38] = constants[61]/2.00000+(constants[45]/algebraic[37])*(algebraic[27]*((states[4]+constants[36])-states[3]))
    rates[3] = algebraic[38]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[7] = constants[63]*constants[19]*(1.00000-states[1])-constants[58]*states[1]
    algebraic[10] = constants[63]*constants[19]*(1.00000-states[2])-constants[59]*states[2]
    algebraic[0] = custom_piecewise([less(constants[1]/2.00000 , states[0]/2.00000), constants[1]/2.00000 , True, states[0]/2.00000])
    algebraic[1] = custom_piecewise([greater(states[0]/2.00000-(states[0]-constants[0]) , constants[2]/2.00000), states[0]/2.00000-(states[0]-constants[0]) , True, constants[2]/2.00000])
    algebraic[2] = algebraic[0]-algebraic[1]
    algebraic[4] = algebraic[2]/constants[0]
    algebraic[6] = (1.00000-algebraic[4])*states[1]+algebraic[4]*states[2]
    algebraic[9] = power(fabs(1.00000/(1.00000+power(constants[10]/algebraic[6], constants[11]))), 1.0/2)
    algebraic[12] = constants[12]*algebraic[9]*(power(constants[5], (constants[18]-37.0000)/10.0000))
    algebraic[15] = custom_piecewise([less(1.00000/algebraic[9] , 100.000), 1.00000/algebraic[9] , True, 100.000])
    algebraic[18] = constants[13]*algebraic[15]*(power(constants[6], (constants[18]-37.0000)/10.0000))
    algebraic[3] = (algebraic[2]*2.00000)/(constants[1]-constants[2])
    algebraic[5] = constants[46]*algebraic[3]*(states[3]*states[5]+states[4]*states[6])
    algebraic[8] = (1.00000*algebraic[5])/constants[68]
    algebraic[11] = ((states[0]-constants[48])/fabs(states[0]-constants[48]))*constants[50]*(exp(constants[51]*fabs(states[0]-constants[48]))-1.00000)
    algebraic[14] = custom_piecewise([greater(states[0] , constants[47]), constants[52]*(exp(constants[53]*fabs(states[0]-constants[47]))-1.00000) , True, 0.00000])
    algebraic[17] = algebraic[11]+algebraic[14]
    algebraic[20] = custom_piecewise([equal(constants[55] , 1.00000), constants[54]*(constants[49]-states[0]) , True, 0.00000])
    algebraic[22] = 1.00000-(states[9]+states[6]+states[5])
    algebraic[19] = exp((-states[4]/fabs(states[4]))*constants[26]*(power(states[4]/constants[36], 2.00000)))
    algebraic[23] = constants[22]*algebraic[19]*constants[30]*(power(constants[33], (constants[18]-37.0000)/10.0000))
    algebraic[27] = algebraic[23]
    algebraic[13] = 1.00000+(1.00000-algebraic[3])*constants[25]
    algebraic[16] = constants[21]*algebraic[13]*constants[30]*(power(constants[32], (constants[18]-37.0000)/10.0000))
    algebraic[29] = constants[42]*(algebraic[16]/constants[39])
    algebraic[21] = exp(((states[3]-constants[36])/fabs(states[3]-constants[36]))*constants[27]*(power((states[3]-constants[36])/constants[36], 2.00000)))
    algebraic[24] = constants[23]*algebraic[21]*constants[30]*(power(constants[34], (constants[18]-37.0000)/10.0000))
    algebraic[30] = constants[60]*(algebraic[24]/constants[62])*((constants[38]+constants[41])/constants[41])*(constants[44]/(constants[38]+constants[44]))
    algebraic[31] = (constants[65]*states[9]+algebraic[30]*states[5])-(algebraic[29]+algebraic[27])*states[6]
    algebraic[25] = custom_piecewise([less(states[3] , constants[36]), exp(constants[28]*(power((constants[36]-states[3])/constants[36], 2.00000))) , True, exp(constants[29]*(power((states[3]-constants[36])/constants[36], 2.00000)))])
    algebraic[26] = constants[24]*algebraic[25]*constants[30]*(power(constants[35], (constants[18]-37.0000)/10.0000))
    algebraic[28] = constants[43]*(algebraic[26]/constants[40])*((constants[38]+constants[41])/(constants[38]+constants[44]))
    algebraic[32] = (constants[38]*constants[64]*algebraic[23]*(algebraic[26]/constants[40]))/((algebraic[16]/constants[39])*(algebraic[24]/constants[62])*constants[37])
    algebraic[33] = algebraic[32]
    algebraic[34] = (algebraic[33]*states[9]+algebraic[27]*states[6])-(algebraic[30]+algebraic[28])*states[5]
    algebraic[35] = (algebraic[33]*algebraic[30]+algebraic[28]*constants[65]+algebraic[30]*constants[65])/(constants[65]*algebraic[27]+algebraic[33]*algebraic[29]+algebraic[33]*algebraic[27]+algebraic[33]*algebraic[30]+algebraic[28]*constants[65]+algebraic[30]*constants[65]+algebraic[27]*algebraic[28]+algebraic[33]*algebraic[29]+algebraic[28]*algebraic[29])
    algebraic[36] = constants[61]/2.00000+(constants[45]/algebraic[35])*(-(constants[65]*states[4])+algebraic[30]*(states[3]-(constants[36]+states[4])))
    algebraic[37] = (constants[65]*algebraic[27]+algebraic[33]*algebraic[29]+algebraic[33]*algebraic[27])/(constants[65]*algebraic[27]+algebraic[33]*algebraic[29]+algebraic[33]*algebraic[27]+algebraic[33]*algebraic[30]+algebraic[28]*constants[65]+algebraic[30]*constants[65]+algebraic[27]*algebraic[28]+algebraic[33]*algebraic[29]+algebraic[28]*algebraic[29])
    algebraic[38] = constants[61]/2.00000+(constants[45]/algebraic[37])*(algebraic[27]*((states[4]+constants[36])-states[3]))
    algebraic[39] = (constants[66]*constants[23]+constants[24]*constants[20]+algebraic[24]*constants[20])/(constants[22]*constants[24]+constants[23]*constants[21]+constants[24]*constants[21]+constants[66]*constants[23]+constants[24]*constants[20]+constants[23]*constants[20]+constants[66]*constants[21]+constants[20]*constants[22]+constants[66]*constants[23])
    algebraic[40] = (states[5]+states[6])/(constants[67]+algebraic[39])
    algebraic[41] = (algebraic[34]+algebraic[31])/(constants[67]+algebraic[39])
    algebraic[42] = constants[57]*((1.00000-algebraic[4])*states[1]+algebraic[4]*(algebraic[40]*states[2]+(1.00000-algebraic[40])*states[1]))
    algebraic[43] = custom_piecewise([less(states[0] , constants[1]), -0.500000*constants[61] , True, 0.00000])
    algebraic[44] = custom_piecewise([greater(2.00000*constants[0]-states[0] , constants[2]), -0.500000*constants[61] , True, 0.00000])
    algebraic[45] = algebraic[43]-algebraic[44]
    algebraic[46] = (2.00000*algebraic[45])/(constants[1]-constants[2])
    algebraic[47] = algebraic[45]/constants[0]
    algebraic[48] = constants[56]*algebraic[46]*(states[3]*states[5]+states[4]*states[6])+constants[56]*algebraic[3]*(algebraic[38]*states[5]+states[3]*algebraic[34]+algebraic[36]*states[6]+states[4]*algebraic[31])
    algebraic[49] = constants[57]*(-algebraic[47]*states[1]+(1.00000-algebraic[4])*algebraic[7]+algebraic[47]*(algebraic[40]*states[2]+(1.00000-algebraic[40])*states[1])+algebraic[4]*((algebraic[41]*states[2]+algebraic[40]*algebraic[10]+(1.00000-algebraic[40])*algebraic[7])-algebraic[41]*states[1]))
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
        self.len_thin = 1.2
        self.len_thick = 1.65
        self.len_hbare = 0.1
        self.Qkon = 1.5
        self.Qkoff = 1.3
        self.Qkn_p = 1.6
        self.Qkp_n = 1.6
        self.kon = 0.05
        self.koffL = 0.25
        self.koffH = 0.025
        self.perm50 = 0.5
        self.nperm = 15
        self.kn_p = 0.5
        self.kp_n = 0.05
        self.koffmod = 1
        self.pH = 7.15
        self.m = 1
        self.kdHCa = 2e-2
        self.TmpC = 22
        self.Cai = 200.0
        self.fapp = 0.5
        self.gapp = 0.07
        self.hf = 2
        self.hb = 0.4
        self.gxb = 0.07
        self.gslmod = 6
        self.hfmdc = 5
        self.hbmdc = 0
        self.sigmap = 8
        self.sigman = 1
        self.xbmodsp = 0.2
        self.Qfapp = 6.25
        self.Qgapp = 2.5
        self.Qhf = 6.25
        self.Qhb = 6.25
        self.Qgxb = 6.25
        self.x_0 = 0.007
        self.kMgATP = 15400e6
        self.kdADP = 4
        self.xPi_cons = 2e3
        self.MgATP_cons = 5e3
        self.MgADP_cons = 36
        self.xPi = 2e3
        self.MgATP = 5e3
        self.MgADP = 36.3
        self.xPsi = 2
        self.kxb = 120
        self.SL_c = 2.25
        self.SLrest = 1.85
        self.SLset = 1.9
        self.PCon_t = 0.002
        self.PExp_t = 10
        self.PCon_c = 0.02
        self.PExp_c = 70
        self.KSE = 1
        self.SEon = 1
        self.kxb_1 = 120
        self.Trop_conc = 70
        self.dSL = 0.00000
        self.H_cons = 1.00000e+07*(power(10.0000, -7.15000))

    def to_dict(self):
        return {
            "len_thin": self.len_thin,
            "len_thick": self.len_thick,
            "len_hbare": self.len_hbare,
            "Qkon": self.Qkon,
            "Qkoff": self.Qkoff,
            "Qkn_p": self.Qkn_p,
            "Qkp_n": self.Qkp_n,
            "kon": self.kon,
            "koffL": self.koffL,
            "koffH": self.koffH,
            "perm50": self.perm50,
            "nperm": self.nperm,
            "kn_p": self.kn_p,
            "kp_n": self.kp_n,
            "koffmod": self.koffmod,
            "pH": self.pH,
            "m": self.m,
            "kdHCa": self.kdHCa,
            "TmpC": self.TmpC,
            "Cai": self.Cai,
            "fapp": self.fapp,
            "gapp": self.gapp,
            "hf": self.hf,
            "hb": self.hb,
            "gxb": self.gxb,
            "gslmod": self.gslmod,
            "hfmdc": self.hfmdc,
            "hbmdc": self.hbmdc,
            "sigmap": self.sigmap,
            "sigman": self.sigman,
            "xbmodsp": self.xbmodsp,
            "Qfapp": self.Qfapp,
            "Qgapp": self.Qgapp,
            "Qhf": self.Qhf,
            "Qhb": self.Qhb,
            "Qgxb": self.Qgxb,
            "x_0": self.x_0,
            "kMgATP": self.kMgATP,
            "kdADP": self.kdADP,
            "xPi_cons": self.xPi_cons,
            "MgATP_cons": self.MgATP_cons,
            "MgADP_cons": self.MgADP_cons,
            "xPi": self.xPi,
            "MgATP": self.MgATP,
            "MgADP": self.MgADP,
            "xPsi": self.xPsi,
            "kxb": self.kxb,
            "SL_c": self.SL_c,
            "SLrest": self.SLrest,
            "SLset": self.SLset,
            "PCon_t": self.PCon_t,
            "PExp_t": self.PExp_t,
            "PCon_c": self.PCon_c,
            "PExp_c": self.PExp_c,
            "KSE": self.KSE,
            "SEon": self.SEon,
            "kxb_1": self.kxb_1,
            "Trop_conc": self.Trop_conc,
            "dSL": self.dSL,
            "H_cons": self.H_cons,
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
        y0=[2.2, 0.0147730085063734, 0.13066096561522, 0.00700005394873882, 3.41212828972468e-8, 1.81017564383744e-6, 3.0494964880038e-7, 0.999999959256274, 4.07437173988636e-8, 0.999997834540066, -4.5113452510363e-6],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "tran_2009"
        self.curve_names = [
            "SL",
            "TRPNCaL",
            "TRPNCaH",
            "xXBpostr",
            "xXBprer",
            "XBpostr",
            "XBprer",
            "N_NoXB",
            "P_NoXB",
            "P",
            "intf",
        ]
        self.state_names = ['SL', 'TRPNCaL', 'TRPNCaH', 'xXBpostr', 'xXBprer', 'XBpostr', 'XBprer', 'N_NoXB', 'P_NoXB', 'P', 'intf']
        self.algebraic_names = ['sovr_ze', 'sovr_cle', 'len_sovr', 'SOVFThick', 'SOVFThin', 'force', 'Tropreg', 'dTRPNCaL', 'active', 'permtot', 'dTRPNCaH', 'ppforce_t', 'kn_pT', 'gapslmd', 'ppforce_c', 'inprmt', 'gappT', 'ppforce', 'kp_nT', 'hfmd', 'afterload', 'hbmd', 'N', 'hfT', 'hbT', 'gxbmd', 'gxbT', 'alpha2_plus', 'alpha3_plus', 'alpha1_minus', 'alpha2_minus', 'dXBprer', 'fxbT', 'alpha3_minus', 'dXBpostr', 'dutyprer', 'dxXBprer', 'dutypostr', 'dxXBpostr', 'SSXBprer', 'FrSBXB', 'dFrSBXB', 'TropTot', 'dsovr_ze', 'dsovr_cle', 'dlen_sovr', 'dSOVFThick', 'dSOVFThin', 'dforce', 'dTropTot']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 71
        p = self.params

        # direct mapping
        c[0] = p.len_thin
        c[1] = p.len_thick
        c[2] = p.len_hbare
        c[3] = p.Qkon
        c[4] = p.Qkoff
        c[5] = p.Qkn_p
        c[6] = p.Qkp_n
        c[7] = p.kon
        c[8] = p.koffL
        c[9] = p.koffH
        c[10] = p.perm50
        c[11] = p.nperm
        c[12] = p.kn_p
        c[13] = p.kp_n
        c[14] = p.koffmod
        c[15] = p.pH
        c[16] = p.m
        c[17] = p.kdHCa
        c[18] = p.TmpC
        c[19] = p.Cai
        c[20] = p.fapp
        c[21] = p.gapp
        c[22] = p.hf
        c[23] = p.hb
        c[24] = p.gxb
        c[25] = p.gslmod
        c[26] = p.hfmdc
        c[27] = p.hbmdc
        c[28] = p.sigmap
        c[29] = p.sigman
        c[30] = p.xbmodsp
        c[31] = p.Qfapp
        c[32] = p.Qgapp
        c[33] = p.Qhf
        c[34] = p.Qhb
        c[35] = p.Qgxb
        c[36] = p.x_0
        c[37] = p.kMgATP
        c[38] = p.kdADP
        c[39] = p.xPi_cons
        c[40] = p.MgATP_cons
        c[41] = p.MgADP_cons
        c[42] = p.xPi
        c[43] = p.MgATP
        c[44] = p.MgADP
        c[45] = p.xPsi
        c[46] = p.kxb
        c[47] = p.SL_c
        c[48] = p.SLrest
        c[49] = p.SLset
        c[50] = p.PCon_t
        c[51] = p.PExp_t
        c[52] = p.PCon_c
        c[53] = p.PExp_c
        c[54] = p.KSE
        c[55] = p.SEon
        c[56] = p.kxb_1
        c[57] = p.Trop_conc
        c[61] = p.dSL
        c[62] = p.H_cons

        # derived constants
        c[58] = c[8]*c[14]*(power(c[4], (c[18]-37.0000)/10.0000))
        c[59] = c[9]*c[14]*(power(c[4], (c[18]-37.0000)/10.0000))
        c[60] = 1.00000e+07*(power(10.0000, -c[15]))
        c[63] = ((power(c[17], c[16])+power(c[62], c[16]))/(power(c[17], c[16])+power(c[60], c[16])))*(c[7]*(power(c[3], (c[18]-37.0000)/10.0000)))
        c[64] = c[20]*c[30]*(power(c[31], (c[18]-37.0000)/10.0000))
        c[65] = c[64]
        c[66] = (c[38]*c[20]*c[22]*(c[24]/c[40]))/((c[21]/c[39])*(c[23]/c[62])*c[37])
        c[67] = (c[20]*c[22]+c[66]*c[21]+c[66]*c[23])/(c[22]*c[24]+c[23]*c[21]+c[24]*c[21]+c[66]*c[23]+c[24]*c[20]+c[23]*c[20]+c[66]*c[21]+c[20]*c[22]+c[66]*c[23])
        c[68] = c[46]*c[36]*c[67]
        c[69] = (fabs(c[49]-c[48])/(c[49]-c[48]))*c[50]*(exp(c[51]*fabs(c[49]-c[48]))-1.00000)
        c[70] = c[61]

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
