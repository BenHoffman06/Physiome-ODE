# Size of variable arrays:
sizeAlgebraic = 28
sizeStates = 12
sizeConstants = 108
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (second)"
    legend_states[0] = "ADP_m in component ADP_m (millimolar)"
    legend_algebraic[25] = "V_ANT in component calcium_dynamics (flux)"
    legend_algebraic[23] = "V_ATPase in component oxidative_phosphorylation (flux)"
    legend_algebraic[10] = "V_SL in component V_SL (flux)"
    legend_states[1] = "NADH in component NADH (millimolar)"
    legend_algebraic[19] = "V_O2 in component oxidative_phosphorylation (flux)"
    legend_algebraic[8] = "V_IDH in component V_IDH (flux)"
    legend_algebraic[9] = "V_KGDH in component V_KGDH (flux)"
    legend_algebraic[12] = "V_MDH in component V_MDH (flux)"
    legend_states[2] = "ISOC in component ISOC (millimolar)"
    legend_algebraic[7] = "V_ACO in component V_ACO (flux)"
    legend_states[3] = "alpha_KG in component alpha_KG (millimolar)"
    legend_algebraic[14] = "V_AAT in component V_AAT (flux)"
    legend_states[4] = "SCoA in component SCoA (millimolar)"
    legend_states[5] = "Suc in component Suc (millimolar)"
    legend_algebraic[11] = "V_SDH in component V_SDH (flux)"
    legend_states[6] = "FUM in component FUM (millimolar)"
    legend_algebraic[15] = "V_FH in component V_FH (flux)"
    legend_states[7] = "MAL in component MAL (millimolar)"
    legend_states[8] = "OAA in component OAA (millimolar)"
    legend_algebraic[6] = "V_CS in component V_CS (flux)"
    legend_states[9] = "ASP in component ASP (millimolar)"
    legend_algebraic[17] = "V_C_ASP in component V_C_ASP (flux)"
    legend_states[10] = "Ca_m in component Ca_m (micromolar)"
    legend_constants[0] = "f in component Ca_m (dimensionless)"
    legend_algebraic[26] = "V_uni in component calcium_dynamics (flux)"
    legend_algebraic[27] = "V_NaCa in component calcium_dynamics (flux)"
    legend_algebraic[1] = "Ca_i in component Ca_i (micromolar)"
    legend_constants[1] = "stim_start in component Ca_i (second)"
    legend_constants[2] = "stim_end in component Ca_i (second)"
    legend_algebraic[0] = "stim_period in component Ca_i (second)"
    legend_constants[3] = "stim_duration in component Ca_i (second)"
    legend_constants[4] = "pulse_value in component Ca_i (micromolar)"
    legend_constants[5] = "Na_i in component Na_i (millimolar)"
    legend_constants[6] = "ATP_i in component ATP_i (millimolar)"
    legend_algebraic[2] = "ATP_m in component ATP_m (millimolar)"
    legend_constants[7] = "Cm in component ATP_m (millimolar)"
    legend_algebraic[3] = "ADP_i in component ADP_i (millimolar)"
    legend_constants[8] = "pulse_value in component ADP_i (millimolar)"
    legend_constants[9] = "GLU in component GLU (millimolar)"
    legend_constants[10] = "Mg in component Mg (millimolar)"
    legend_constants[11] = "H in component H (millimolar)"
    legend_constants[12] = "Pi in component Pi (millimolar)"
    legend_constants[13] = "CoA in component CoA (millimolar)"
    legend_constants[14] = "AcCoA in component AcCoA (millimolar)"
    legend_constants[15] = "FAD in component FAD (millimolar)"
    legend_constants[16] = "FADH2 in component FADH2 (millimolar)"
    legend_algebraic[4] = "NAD in component NAD (millimolar)"
    legend_constants[17] = "C_PN in component NAD (millimolar)"
    legend_algebraic[5] = "CIT in component CIT (millimolar)"
    legend_constants[18] = "C_Kint in component CIT (millimolar)"
    legend_states[11] = "delta_psi_m in component mitochondrial_membrane (volt)"
    legend_constants[19] = "R in component mitochondrial_membrane (volt_coulomb_per_mole_kelvin)"
    legend_constants[20] = "T in component mitochondrial_membrane (kelvin)"
    legend_constants[21] = "F in component mitochondrial_membrane (coulomb_per_mole)"
    legend_constants[22] = "C_mito in component mitochondrial_membrane (millimolar_per_volt)"
    legend_algebraic[18] = "V_He in component oxidative_phosphorylation (flux)"
    legend_algebraic[20] = "V_He_F in component oxidative_phosphorylation (flux)"
    legend_algebraic[24] = "V_Hu in component oxidative_phosphorylation (flux)"
    legend_algebraic[21] = "V_Hleak in component oxidative_phosphorylation (flux)"
    legend_constants[23] = "Km_AcCoA in component V_CS (millimolar)"
    legend_constants[24] = "Km_OAA in component V_CS (millimolar)"
    legend_constants[25] = "Kcat_CS in component V_CS (first_order_rate_constant)"
    legend_constants[26] = "ET_CS in component V_CS (millimolar)"
    legend_constants[27] = "Kf_ACO in component V_ACO (first_order_rate_constant)"
    legend_constants[28] = "KE_ACO in component V_ACO (dimensionless)"
    legend_constants[29] = "Kh_1 in component V_IDH (millimolar)"
    legend_constants[30] = "Kh_2 in component V_IDH (millimolar)"
    legend_constants[31] = "Km_ISOC in component V_IDH (millimolar)"
    legend_constants[32] = "Ka_ADP in component V_IDH (millimolar)"
    legend_constants[33] = "Ka_Ca in component V_IDH (micromolar)"
    legend_constants[34] = "Km_NAD in component V_IDH (millimolar)"
    legend_constants[35] = "Ki_NADH in component V_IDH (millimolar)"
    legend_constants[36] = "Kcat_IDH in component V_IDH (first_order_rate_constant)"
    legend_constants[37] = "ET_IDH in component V_IDH (millimolar)"
    legend_constants[38] = "ni in component V_IDH (dimensionless)"
    legend_constants[39] = "Km_alpha_KG in component V_KGDH (millimolar)"
    legend_constants[40] = "Kcat_KGDH in component V_KGDH (first_order_rate_constant)"
    legend_constants[41] = "ET_KGDH in component V_KGDH (millimolar)"
    legend_constants[42] = "Kd_Mg in component V_KGDH (millimolar)"
    legend_constants[43] = "Kd_Ca in component V_KGDH (micromolar)"
    legend_constants[44] = "n_alpha_KG in component V_KGDH (dimensionless)"
    legend_constants[45] = "Km_NAD in component V_KGDH (millimolar)"
    legend_constants[46] = "kf_SL in component V_SL (second_order_rate_constant)"
    legend_constants[47] = "Ke_SL in component V_SL (millimolar)"
    legend_constants[48] = "Kisdh_OAA in component V_SDH (millimolar)"
    legend_constants[49] = "Kcat_SDH in component V_SDH (first_order_rate_constant)"
    legend_constants[50] = "ET_SDH in component V_SDH (millimolar)"
    legend_constants[51] = "Km_Suc in component V_SDH (millimolar)"
    legend_constants[52] = "Ki_FUM in component V_SDH (millimolar)"
    legend_constants[53] = "Km_MAL in component V_MDH (millimolar)"
    legend_constants[54] = "Kcat_MDH in component V_MDH (first_order_rate_constant)"
    legend_constants[55] = "ET_MDH in component V_MDH (millimolar)"
    legend_constants[56] = "Ki_OAA in component V_MDH (millimolar)"
    legend_constants[106] = "fh_a in component V_MDH (dimensionless)"
    legend_constants[107] = "fh_i in component V_MDH (dimensionless)"
    legend_constants[57] = "Km_NAD in component V_MDH (millimolar)"
    legend_constants[58] = "kh1 in component V_MDH (millimolar)"
    legend_constants[59] = "kh2 in component V_MDH (millimolar)"
    legend_constants[60] = "kh3 in component V_MDH (millimolar)"
    legend_constants[61] = "kh4 in component V_MDH (millimolar)"
    legend_constants[62] = "k_offset in component V_MDH (dimensionless)"
    legend_constants[63] = "Ke_FH in component V_FH (dimensionless)"
    legend_constants[64] = "kf_FH in component V_FH (first_order_rate_constant)"
    legend_constants[65] = "Ke_AAT in component V_AAT (dimensionless)"
    legend_constants[66] = "kf_AAT in component V_AAT (second_order_rate_constant)"
    legend_constants[67] = "k_C_ASP in component V_C_ASP (first_order_rate_constant)"
    legend_constants[68] = "rho_res in component oxidative_phosphorylation (millimolar)"
    legend_constants[69] = "rho_res_F in component oxidative_phosphorylation (millimolar)"
    legend_constants[70] = "ra in component oxidative_phosphorylation (first_order_rate_constant)"
    legend_constants[71] = "rc1 in component oxidative_phosphorylation (first_order_rate_constant)"
    legend_algebraic[13] = "Ares in component oxidative_phosphorylation (volt)"
    legend_constants[105] = "Ares_F in component oxidative_phosphorylation (volt)"
    legend_constants[72] = "r1 in component oxidative_phosphorylation (dimensionless)"
    legend_constants[73] = "r2 in component oxidative_phosphorylation (dimensionless)"
    legend_constants[74] = "r3 in component oxidative_phosphorylation (dimensionless)"
    legend_constants[75] = "rb in component oxidative_phosphorylation (first_order_rate_constant)"
    legend_constants[76] = "rc2 in component oxidative_phosphorylation (first_order_rate_constant)"
    legend_constants[77] = "Kres in component oxidative_phosphorylation (dimensionless)"
    legend_constants[78] = "Kres_F in component oxidative_phosphorylation (dimensionless)"
    legend_constants[79] = "gH in component oxidative_phosphorylation (millimolar_per_second_volt)"
    legend_constants[80] = "delta_psi_B in component oxidative_phosphorylation (volt)"
    legend_constants[81] = "g in component oxidative_phosphorylation (dimensionless)"
    legend_algebraic[16] = "delta_mu_H in component oxidative_phosphorylation (volt)"
    legend_constants[82] = "delta_pH in component oxidative_phosphorylation (dimensionless)"
    legend_constants[83] = "rho_F1 in component oxidative_phosphorylation (millimolar)"
    legend_constants[84] = "pa in component oxidative_phosphorylation (first_order_rate_constant)"
    legend_constants[85] = "pc1 in component oxidative_phosphorylation (first_order_rate_constant)"
    legend_algebraic[22] = "AF1 in component oxidative_phosphorylation (volt)"
    legend_constants[86] = "p1 in component oxidative_phosphorylation (dimensionless)"
    legend_constants[87] = "p2 in component oxidative_phosphorylation (dimensionless)"
    legend_constants[88] = "p3 in component oxidative_phosphorylation (dimensionless)"
    legend_constants[89] = "pb in component oxidative_phosphorylation (first_order_rate_constant)"
    legend_constants[90] = "pc2 in component oxidative_phosphorylation (first_order_rate_constant)"
    legend_constants[91] = "KF1 in component oxidative_phosphorylation (millimolar)"
    legend_constants[92] = "h in component calcium_dynamics (dimensionless)"
    legend_constants[93] = "delta_psi_0 in component calcium_dynamics (volt)"
    legend_constants[94] = "Vmax_ANT in component calcium_dynamics (flux)"
    legend_constants[95] = "L in component calcium_dynamics (dimensionless)"
    legend_constants[96] = "na in component calcium_dynamics (dimensionless)"
    legend_constants[97] = "Vmax_uni in component calcium_dynamics (flux)"
    legend_constants[98] = "K_act in component calcium_dynamics (micromolar)"
    legend_constants[99] = "K_trans in component calcium_dynamics (micromolar)"
    legend_constants[100] = "n in component calcium_dynamics (dimensionless)"
    legend_constants[101] = "Vmax_NaCa in component calcium_dynamics (flux)"
    legend_constants[102] = "KNa in component calcium_dynamics (millimolar)"
    legend_constants[103] = "KCa in component calcium_dynamics (micromolar)"
    legend_constants[104] = "b in component calcium_dynamics (dimensionless)"
    legend_rates[0] = "d/dt ADP_m in component ADP_m (millimolar)"
    legend_rates[1] = "d/dt NADH in component NADH (millimolar)"
    legend_rates[2] = "d/dt ISOC in component ISOC (millimolar)"
    legend_rates[3] = "d/dt alpha_KG in component alpha_KG (millimolar)"
    legend_rates[4] = "d/dt SCoA in component SCoA (millimolar)"
    legend_rates[5] = "d/dt Suc in component Suc (millimolar)"
    legend_rates[6] = "d/dt FUM in component FUM (millimolar)"
    legend_rates[7] = "d/dt MAL in component MAL (millimolar)"
    legend_rates[8] = "d/dt OAA in component OAA (millimolar)"
    legend_rates[9] = "d/dt ASP in component ASP (millimolar)"
    legend_rates[10] = "d/dt Ca_m in component Ca_m (micromolar)"
    legend_rates[11] = "d/dt delta_psi_m in component mitochondrial_membrane (volt)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 0.1
    states[1] = 0.01
    states[2] = 0.01
    states[3] = 0.01
    states[4] = 0.01
    states[5] = 0.01
    states[6] = 0.01
    states[7] = 0.01
    states[8] = 0.01
    states[9] = 0.01
    states[10] = 0.01
    constants[0] = 0.0003
    constants[1] = 0
    constants[2] = 10000
    constants[3] = 0.4
    constants[4] = 1
    constants[5] = 10.0
    constants[6] = 6.5
    constants[7] = 15.0
    constants[8] = 0.15
    constants[9] = 20
    constants[10] = 0.4
    constants[11] = 2.5E-5
    constants[12] = 20.0
    constants[13] = 0.02
    constants[14] = 0.0002
    constants[15] = 0.01
    constants[16] = 1.24
    constants[17] = 10.0
    constants[18] = 1.0
    states[11] = 0.01
    constants[19] = 8.315
    constants[20] = 310.16
    constants[21] = 96480
    constants[22] = 1.812
    constants[23] = 1.26E-2
    constants[24] = 6.4E-4
    constants[25] = 3.2
    constants[26] = 0.4
    constants[27] = 12.5
    constants[28] = 2.22
    constants[29] = 8.1E-5
    constants[30] = 5.98E-5
    constants[31] = 1.52
    constants[32] = 6.2E-2
    constants[33] = 1.41
    constants[34] = 0.923
    constants[35] = 0.19
    constants[36] = 1.94
    constants[37] = 0.109
    constants[38] = 1
    constants[39] = 1.94
    constants[40] = 0.15
    constants[41] = 0.5
    constants[42] = 0.0308
    constants[43] = 1.27
    constants[44] = 1.2
    constants[45] = 38.7
    constants[46] = 0.127
    constants[47] = 3.115
    constants[48] = 0.15
    constants[49] = 1.0
    constants[50] = 0.5
    constants[51] = 3.0E-2
    constants[52] = 1.3
    constants[53] = 1.493
    constants[54] = 2.775E1
    constants[55] = 0.154
    constants[56] = 3.1E-3
    constants[57] = 0.2244
    constants[58] = 1.13E-5
    constants[59] = 26.7
    constants[60] = 6.68E-9
    constants[61] = 5.62E-6
    constants[62] = 3.99E-2
    constants[63] = 1.0
    constants[64] = 0.83
    constants[65] = 6.6
    constants[66] = 0.644
    constants[67] = 0.01
    constants[68] = 0.0006
    constants[69] = 0.0045
    constants[70] = 6.394E-10
    constants[71] = 2.656E-19
    constants[72] = 2.077E-18
    constants[73] = 1.728E-9
    constants[74] = 1.059E-26
    constants[75] = 1.762E-13
    constants[76] = 8.632E-27
    constants[77] = 1.35E18
    constants[78] = 5.765E13
    constants[79] = 0.01
    constants[80] = 0.05
    constants[81] = 0.85
    constants[82] = -0.6
    constants[83] = 0.06
    constants[84] = 1.656E-5
    constants[85] = 9.651E-14
    constants[86] = 1.346E-8
    constants[87] = 7.739E-7
    constants[88] = 6.65E-15
    constants[89] = 3.373E-7
    constants[90] = 4.585E-14
    constants[91] = 1.71E6
    constants[92] = 0.5
    constants[93] = 0.091
    constants[94] = 0.05
    constants[95] = 110.0
    constants[96] = 2.8
    constants[97] = 0.000625
    constants[98] = 0.38
    constants[99] = 19.0
    constants[100] = 3.0
    constants[101] = 0.005
    constants[102] = 9.4
    constants[103] = 3.75E-1
    constants[104] = 0.5
    constants[105] = ((constants[19]*constants[20])/constants[21])*log(constants[78]*(power(constants[16]/constants[15], 0.500000)))
    constants[106] = 1.00000/(1.00000+constants[11]/constants[58]+(power(constants[11], 2.00000))/(constants[58]*constants[59]))+constants[62]
    constants[107] = power(1.00000/(1.00000+constants[60]/constants[11]+(constants[60]*constants[61])/(power(constants[11], 2.00000))), 2.00000)
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[4] = constants[17]-states[1]
    algebraic[8] = (constants[36]*constants[37])/(1.00000+constants[11]/constants[29]+constants[30]/constants[11]+(power(constants[31]/states[2], constants[38]))/((1.00000+states[0]/constants[32])*(1.00000+states[10]/constants[33]))+(constants[34]/algebraic[4])*(1.00000+states[1]/constants[35])+((power(constants[31]/states[2], constants[38]))*(constants[34]/algebraic[4])*(1.00000+states[1]/constants[35]))/((1.00000+states[0]/constants[32])*(1.00000+states[10]/constants[33])))
    algebraic[5] = constants[18]-(states[2]+states[3]+states[4]+states[5]+states[6]+states[7]+states[8])
    algebraic[7] = constants[27]*(algebraic[5]-states[2]/constants[28])
    rates[2] = algebraic[7]-algebraic[8]
    algebraic[2] = constants[7]-states[0]
    algebraic[10] = constants[46]*(states[4]*states[0]-(states[5]*algebraic[2]*constants[13])/constants[47])
    algebraic[9] = (constants[40]*constants[41])/(1.00000+(power(constants[39]/states[3], constants[44]))/((1.00000+constants[10]/constants[42])*(1.00000+states[10]/constants[43]))+(constants[45]/algebraic[4])/((1.00000+constants[10]/constants[42])*(1.00000+states[10]/constants[43])))
    rates[4] = algebraic[9]-algebraic[10]
    algebraic[11] = (constants[49]*constants[50])/(1.00000+(constants[51]/states[5])*(1.00000+states[8]/constants[48])*(1.00000+states[6]/constants[52]))
    rates[5] = algebraic[10]-algebraic[11]
    algebraic[14] = constants[66]*(states[8]*constants[9]-(states[3]*states[9])/constants[65])
    rates[3] = algebraic[14]+algebraic[8]+-algebraic[9]
    algebraic[15] = constants[64]*(states[6]-states[7]/constants[63])
    rates[6] = algebraic[11]-algebraic[15]
    algebraic[12] = (constants[54]*constants[55]*constants[106]*constants[107])/(1.00000+(constants[53]/states[7])*(1.00000+states[8]/constants[56])+constants[57]/algebraic[4]+(constants[53]/states[7])*(1.00000+states[8]/constants[56])*(constants[57]/algebraic[4]))
    rates[7] = algebraic[15]-algebraic[12]
    algebraic[6] = (constants[25]*constants[26])/(1.00000+constants[23]/constants[14]+constants[24]/states[8]+(constants[23]/constants[14])*(constants[24]/states[8]))
    rates[8] = algebraic[12]-(algebraic[6]+algebraic[14])
    algebraic[17] = constants[67]*states[9]
    rates[9] = algebraic[14]-algebraic[17]
    algebraic[13] = ((constants[19]*constants[20])/constants[21])*log(constants[77]*(power(states[1]/algebraic[4], 0.500000)))
    algebraic[16] = ((constants[19]*constants[20])/constants[21])*constants[82]+states[11]
    algebraic[19] = 0.500000*constants[68]*((((constants[70]+constants[71]*exp((6.00000*constants[21]*constants[80])/(constants[19]*constants[20])))*exp((algebraic[13]*constants[21])/(constants[19]*constants[20]))-constants[70]*exp((constants[81]*6.00000*constants[21]*algebraic[16])/(constants[19]*constants[20])))+constants[76]*exp((algebraic[13]*constants[21])/(constants[19]*constants[20]))*exp((constants[81]*6.00000*constants[21]*algebraic[16])/(constants[19]*constants[20])))/((1.00000+constants[72]*exp((constants[21]*algebraic[13])/(constants[19]*constants[20])))*exp((6.00000*constants[21]*constants[80])/(constants[19]*constants[20]))+(constants[73]+constants[74]*exp((constants[21]*algebraic[13])/(constants[19]*constants[20])))*exp((constants[81]*6.00000*constants[21]*algebraic[16])/(constants[19]*constants[20]))))
    rates[1] = -algebraic[19]+algebraic[8]+algebraic[9]+algebraic[12]
    algebraic[3] = custom_piecewise([greater_equal(voi , 100.000) & less(voi , 300.000), constants[8] , True, 0.0500000])
    algebraic[25] = constants[94]*((1.00000-(0.0500000*constants[6]*0.450000*0.800000*states[0])/(0.450000*algebraic[3]*0.0500000*algebraic[2]))/((1.00000+((0.0500000*constants[6])/(0.450000*algebraic[3]))*exp((-constants[92]*constants[21]*constants[93])/(constants[19]*constants[20])))*(1.00000+(0.450000*0.800000*states[0])/(0.0500000*algebraic[2]))))
    algebraic[22] = ((constants[19]*constants[20])/constants[21])*log(constants[91]*(algebraic[2]/(states[0]*constants[12])))
    algebraic[23] = -constants[83]*(((100.000*constants[84]+constants[85]*exp((3.00000*constants[21]*constants[80])/(constants[19]*constants[20])))*exp((algebraic[22]*constants[21])/(constants[19]*constants[20]))-(constants[84]*exp((3.00000*constants[21]*algebraic[16])/(constants[19]*constants[20]))+constants[90]*exp((algebraic[22]*constants[21])/(constants[19]*constants[20]))*exp((3.00000*constants[21]*algebraic[16])/(constants[19]*constants[20]))))/((1.00000+constants[86]*exp((constants[21]*algebraic[22])/(constants[19]*constants[20])))*exp((3.00000*constants[21]*constants[80])/(constants[19]*constants[20]))+(constants[87]+constants[88]*exp((constants[21]*algebraic[22])/(constants[19]*constants[20])))*exp((3.00000*constants[21]*algebraic[16])/(constants[19]*constants[20]))))
    rates[0] = algebraic[25]-(algebraic[23]+algebraic[10])
    algebraic[0] = custom_piecewise([greater_equal(voi , 100.000) & less(voi , 300.000), 0.500000 , True, 4.00000])
    algebraic[1] = custom_piecewise([greater_equal(voi , constants[1]) & less_equal(voi , constants[2]) & less_equal((voi-constants[1])-floor((voi-constants[1])/algebraic[0])*algebraic[0] , constants[3]), constants[4] , True, 0.100000])
    algebraic[26] = constants[97]*(((algebraic[1]/constants[99])*(power(1.00000+algebraic[1]/constants[99], 3.00000))*((2.00000*constants[21]*(states[11]-constants[93]))/(constants[19]*constants[20])))/(power(1.00000+algebraic[1]/constants[99], 4.00000)+(constants[95]/(power(1.00000+algebraic[1]/constants[98], constants[96])))*(1.00000-exp((-2.00000*constants[21]*(states[11]-constants[93]))/(constants[19]*constants[20])))))
    algebraic[27] = constants[101]*((exp((constants[104]*constants[21]*(states[11]-constants[93]))/(constants[19]*constants[20]))*exp(log(algebraic[1]/states[10])))/((power(1.00000+constants[102]/constants[5], constants[100]))*(1.00000+constants[103]/states[10])))
    rates[10] = constants[0]*1.00000*(algebraic[26]-algebraic[27])
    algebraic[18] = 6.00000*constants[68]*((constants[70]*exp((constants[21]*algebraic[13])/(constants[19]*constants[20]))-(constants[70]+constants[75])*exp((constants[81]*6.00000*constants[21]*algebraic[16])/(constants[19]*constants[20])))/((1.00000+constants[72]*exp((constants[21]*algebraic[13])/(constants[19]*constants[20])))*exp((6.00000*constants[21]*constants[80])/(constants[19]*constants[20]))+(constants[73]+constants[74]*exp((constants[21]*algebraic[13])/(constants[19]*constants[20])))*exp((constants[81]*6.00000*constants[21]*algebraic[16])/(constants[19]*constants[20]))))
    algebraic[20] = 6.00000*constants[69]*((constants[70]*exp((constants[21]*constants[105])/(constants[19]*constants[20]))-(constants[70]+constants[75])*exp((constants[81]*6.00000*constants[21]*algebraic[16])/(constants[19]*constants[20])))/((1.00000+constants[72]*exp((constants[21]*constants[105])/(constants[19]*constants[20])))*exp((6.00000*constants[21]*constants[80])/(constants[19]*constants[20]))+(constants[73]+constants[74]*exp((constants[21]*constants[105])/(constants[19]*constants[20])))*exp((constants[81]*6.00000*constants[21]*algebraic[16])/(constants[19]*constants[20]))))
    algebraic[24] = -3.00000*constants[83]*((100.000*constants[84]*(1.00000+exp((constants[21]*algebraic[22])/(constants[19]*constants[20])))-(constants[84]+constants[89])*exp((3.00000*constants[21]*algebraic[16])/(constants[19]*constants[20])))/((1.00000+constants[86]*exp((constants[21]*algebraic[22])/(constants[19]*constants[20])))*exp((3.00000*constants[21]*constants[80])/(constants[19]*constants[20]))+(constants[87]+constants[88]*exp((constants[21]*algebraic[22])/(constants[19]*constants[20])))*exp((3.00000*constants[21]*algebraic[16])/(constants[19]*constants[20]))))
    algebraic[21] = constants[79]*algebraic[16]
    rates[11] = (algebraic[18]+algebraic[20]+-(algebraic[24]+algebraic[25]+algebraic[21]+algebraic[27]+2.00000*algebraic[26]))/constants[22]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[4] = constants[17]-states[1]
    algebraic[8] = (constants[36]*constants[37])/(1.00000+constants[11]/constants[29]+constants[30]/constants[11]+(power(constants[31]/states[2], constants[38]))/((1.00000+states[0]/constants[32])*(1.00000+states[10]/constants[33]))+(constants[34]/algebraic[4])*(1.00000+states[1]/constants[35])+((power(constants[31]/states[2], constants[38]))*(constants[34]/algebraic[4])*(1.00000+states[1]/constants[35]))/((1.00000+states[0]/constants[32])*(1.00000+states[10]/constants[33])))
    algebraic[5] = constants[18]-(states[2]+states[3]+states[4]+states[5]+states[6]+states[7]+states[8])
    algebraic[7] = constants[27]*(algebraic[5]-states[2]/constants[28])
    algebraic[2] = constants[7]-states[0]
    algebraic[10] = constants[46]*(states[4]*states[0]-(states[5]*algebraic[2]*constants[13])/constants[47])
    algebraic[9] = (constants[40]*constants[41])/(1.00000+(power(constants[39]/states[3], constants[44]))/((1.00000+constants[10]/constants[42])*(1.00000+states[10]/constants[43]))+(constants[45]/algebraic[4])/((1.00000+constants[10]/constants[42])*(1.00000+states[10]/constants[43])))
    algebraic[11] = (constants[49]*constants[50])/(1.00000+(constants[51]/states[5])*(1.00000+states[8]/constants[48])*(1.00000+states[6]/constants[52]))
    algebraic[14] = constants[66]*(states[8]*constants[9]-(states[3]*states[9])/constants[65])
    algebraic[15] = constants[64]*(states[6]-states[7]/constants[63])
    algebraic[12] = (constants[54]*constants[55]*constants[106]*constants[107])/(1.00000+(constants[53]/states[7])*(1.00000+states[8]/constants[56])+constants[57]/algebraic[4]+(constants[53]/states[7])*(1.00000+states[8]/constants[56])*(constants[57]/algebraic[4]))
    algebraic[6] = (constants[25]*constants[26])/(1.00000+constants[23]/constants[14]+constants[24]/states[8]+(constants[23]/constants[14])*(constants[24]/states[8]))
    algebraic[17] = constants[67]*states[9]
    algebraic[13] = ((constants[19]*constants[20])/constants[21])*log(constants[77]*(power(states[1]/algebraic[4], 0.500000)))
    algebraic[16] = ((constants[19]*constants[20])/constants[21])*constants[82]+states[11]
    algebraic[19] = 0.500000*constants[68]*((((constants[70]+constants[71]*exp((6.00000*constants[21]*constants[80])/(constants[19]*constants[20])))*exp((algebraic[13]*constants[21])/(constants[19]*constants[20]))-constants[70]*exp((constants[81]*6.00000*constants[21]*algebraic[16])/(constants[19]*constants[20])))+constants[76]*exp((algebraic[13]*constants[21])/(constants[19]*constants[20]))*exp((constants[81]*6.00000*constants[21]*algebraic[16])/(constants[19]*constants[20])))/((1.00000+constants[72]*exp((constants[21]*algebraic[13])/(constants[19]*constants[20])))*exp((6.00000*constants[21]*constants[80])/(constants[19]*constants[20]))+(constants[73]+constants[74]*exp((constants[21]*algebraic[13])/(constants[19]*constants[20])))*exp((constants[81]*6.00000*constants[21]*algebraic[16])/(constants[19]*constants[20]))))
    algebraic[3] = custom_piecewise([greater_equal(voi , 100.000) & less(voi , 300.000), constants[8] , True, 0.0500000])
    algebraic[25] = constants[94]*((1.00000-(0.0500000*constants[6]*0.450000*0.800000*states[0])/(0.450000*algebraic[3]*0.0500000*algebraic[2]))/((1.00000+((0.0500000*constants[6])/(0.450000*algebraic[3]))*exp((-constants[92]*constants[21]*constants[93])/(constants[19]*constants[20])))*(1.00000+(0.450000*0.800000*states[0])/(0.0500000*algebraic[2]))))
    algebraic[22] = ((constants[19]*constants[20])/constants[21])*log(constants[91]*(algebraic[2]/(states[0]*constants[12])))
    algebraic[23] = -constants[83]*(((100.000*constants[84]+constants[85]*exp((3.00000*constants[21]*constants[80])/(constants[19]*constants[20])))*exp((algebraic[22]*constants[21])/(constants[19]*constants[20]))-(constants[84]*exp((3.00000*constants[21]*algebraic[16])/(constants[19]*constants[20]))+constants[90]*exp((algebraic[22]*constants[21])/(constants[19]*constants[20]))*exp((3.00000*constants[21]*algebraic[16])/(constants[19]*constants[20]))))/((1.00000+constants[86]*exp((constants[21]*algebraic[22])/(constants[19]*constants[20])))*exp((3.00000*constants[21]*constants[80])/(constants[19]*constants[20]))+(constants[87]+constants[88]*exp((constants[21]*algebraic[22])/(constants[19]*constants[20])))*exp((3.00000*constants[21]*algebraic[16])/(constants[19]*constants[20]))))
    algebraic[0] = custom_piecewise([greater_equal(voi , 100.000) & less(voi , 300.000), 0.500000 , True, 4.00000])
    algebraic[1] = custom_piecewise([greater_equal(voi , constants[1]) & less_equal(voi , constants[2]) & less_equal((voi-constants[1])-floor((voi-constants[1])/algebraic[0])*algebraic[0] , constants[3]), constants[4] , True, 0.100000])
    algebraic[26] = constants[97]*(((algebraic[1]/constants[99])*(power(1.00000+algebraic[1]/constants[99], 3.00000))*((2.00000*constants[21]*(states[11]-constants[93]))/(constants[19]*constants[20])))/(power(1.00000+algebraic[1]/constants[99], 4.00000)+(constants[95]/(power(1.00000+algebraic[1]/constants[98], constants[96])))*(1.00000-exp((-2.00000*constants[21]*(states[11]-constants[93]))/(constants[19]*constants[20])))))
    algebraic[27] = constants[101]*((exp((constants[104]*constants[21]*(states[11]-constants[93]))/(constants[19]*constants[20]))*exp(log(algebraic[1]/states[10])))/((power(1.00000+constants[102]/constants[5], constants[100]))*(1.00000+constants[103]/states[10])))
    algebraic[18] = 6.00000*constants[68]*((constants[70]*exp((constants[21]*algebraic[13])/(constants[19]*constants[20]))-(constants[70]+constants[75])*exp((constants[81]*6.00000*constants[21]*algebraic[16])/(constants[19]*constants[20])))/((1.00000+constants[72]*exp((constants[21]*algebraic[13])/(constants[19]*constants[20])))*exp((6.00000*constants[21]*constants[80])/(constants[19]*constants[20]))+(constants[73]+constants[74]*exp((constants[21]*algebraic[13])/(constants[19]*constants[20])))*exp((constants[81]*6.00000*constants[21]*algebraic[16])/(constants[19]*constants[20]))))
    algebraic[20] = 6.00000*constants[69]*((constants[70]*exp((constants[21]*constants[105])/(constants[19]*constants[20]))-(constants[70]+constants[75])*exp((constants[81]*6.00000*constants[21]*algebraic[16])/(constants[19]*constants[20])))/((1.00000+constants[72]*exp((constants[21]*constants[105])/(constants[19]*constants[20])))*exp((6.00000*constants[21]*constants[80])/(constants[19]*constants[20]))+(constants[73]+constants[74]*exp((constants[21]*constants[105])/(constants[19]*constants[20])))*exp((constants[81]*6.00000*constants[21]*algebraic[16])/(constants[19]*constants[20]))))
    algebraic[24] = -3.00000*constants[83]*((100.000*constants[84]*(1.00000+exp((constants[21]*algebraic[22])/(constants[19]*constants[20])))-(constants[84]+constants[89])*exp((3.00000*constants[21]*algebraic[16])/(constants[19]*constants[20])))/((1.00000+constants[86]*exp((constants[21]*algebraic[22])/(constants[19]*constants[20])))*exp((3.00000*constants[21]*constants[80])/(constants[19]*constants[20]))+(constants[87]+constants[88]*exp((constants[21]*algebraic[22])/(constants[19]*constants[20])))*exp((3.00000*constants[21]*algebraic[16])/(constants[19]*constants[20]))))
    algebraic[21] = constants[79]*algebraic[16]
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
