# Size of variable arrays:
sizeAlgebraic = 35
sizeStates = 16
sizeConstants = 134
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
    legend_algebraic[32] = "V_ANT in component calcium_dynamics (flux)"
    legend_algebraic[30] = "V_ATPase in component oxidative_phosphorylation (flux)"
    legend_algebraic[11] = "V_SL in component V_SL (flux)"
    legend_states[1] = "NADH in component NADH (millimolar)"
    legend_algebraic[26] = "V_O2 in component oxidative_phosphorylation (flux)"
    legend_algebraic[9] = "V_IDH in component V_IDH (flux)"
    legend_algebraic[10] = "V_KGDH in component V_KGDH (flux)"
    legend_algebraic[13] = "V_MDH in component V_MDH (flux)"
    legend_states[2] = "ISOC in component ISOC (millimolar)"
    legend_algebraic[8] = "V_ACO in component V_ACO (flux)"
    legend_states[3] = "alpha_KG in component alpha_KG (millimolar)"
    legend_algebraic[15] = "V_AAT in component V_AAT (flux)"
    legend_states[4] = "SCoA in component SCoA (millimolar)"
    legend_states[5] = "Suc in component Suc (millimolar)"
    legend_algebraic[12] = "V_SDH in component V_SDH (flux)"
    legend_states[6] = "FUM in component FUM (millimolar)"
    legend_algebraic[16] = "V_FH in component V_FH (flux)"
    legend_states[7] = "MAL in component MAL (millimolar)"
    legend_states[8] = "OAA in component OAA (millimolar)"
    legend_algebraic[7] = "V_CS in component V_CS (flux)"
    legend_states[9] = "ASP in component ASP (millimolar)"
    legend_algebraic[18] = "V_C_ASP in component V_C_ASP (flux)"
    legend_states[10] = "Ca_m in component Ca_m (micromolar)"
    legend_constants[0] = "f in component Ca_m (dimensionless)"
    legend_algebraic[33] = "V_uni in component calcium_dynamics (flux)"
    legend_algebraic[34] = "V_NaCa in component calcium_dynamics (flux)"
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
    legend_constants[18] = "NADPH in component NADPH (millimolar)"
    legend_states[11] = "O2_m in component O2_m (millimolar)"
    legend_constants[19] = "shunt in component O2_m (dimensionless)"
    legend_algebraic[20] = "VTr_ROS in component VTr_ROS (flux)"
    legend_states[12] = "O2_i in component O2_i (millimolar)"
    legend_algebraic[14] = "V_SOD in component V_SOD (flux)"
    legend_states[13] = "H2O2 in component H2O2 (millimolar)"
    legend_algebraic[19] = "V_CAT in component V_CAT (flux)"
    legend_algebraic[21] = "V_GPX in component V_GPX (flux)"
    legend_states[14] = "GSH in component GSH (millimolar)"
    legend_algebraic[23] = "V_GR in component V_GR (flux)"
    legend_algebraic[5] = "GSSG in component GSSG (millimolar)"
    legend_constants[20] = "GT in component GSSG (millimolar)"
    legend_algebraic[6] = "CIT in component CIT (millimolar)"
    legend_constants[21] = "C_Kint in component CIT (millimolar)"
    legend_states[15] = "delta_psi_m in component mitochondrial_membrane (volt)"
    legend_constants[22] = "R in component mitochondrial_membrane (volt_coulomb_per_mole_kelvin)"
    legend_constants[23] = "T in component mitochondrial_membrane (kelvin)"
    legend_constants[24] = "F in component mitochondrial_membrane (coulomb_per_mole)"
    legend_constants[25] = "C_mito in component mitochondrial_membrane (millimolar_per_volt)"
    legend_algebraic[25] = "V_He in component oxidative_phosphorylation (flux)"
    legend_algebraic[27] = "V_He_F in component oxidative_phosphorylation (flux)"
    legend_algebraic[31] = "V_Hu in component oxidative_phosphorylation (flux)"
    legend_algebraic[28] = "V_Hleak in component oxidative_phosphorylation (flux)"
    legend_constants[26] = "Km_AcCoA in component V_CS (millimolar)"
    legend_constants[27] = "Km_OAA in component V_CS (millimolar)"
    legend_constants[28] = "Kcat_CS in component V_CS (first_order_rate_constant)"
    legend_constants[29] = "ET_CS in component V_CS (millimolar)"
    legend_constants[30] = "Kf_ACO in component V_ACO (first_order_rate_constant)"
    legend_constants[31] = "KE_ACO in component V_ACO (dimensionless)"
    legend_constants[32] = "Kh_1 in component V_IDH (millimolar)"
    legend_constants[33] = "Kh_2 in component V_IDH (millimolar)"
    legend_constants[34] = "Km_ISOC in component V_IDH (millimolar)"
    legend_constants[35] = "Ka_ADP in component V_IDH (millimolar)"
    legend_constants[36] = "Ka_Ca in component V_IDH (micromolar)"
    legend_constants[37] = "Km_NAD in component V_IDH (millimolar)"
    legend_constants[38] = "Ki_NADH in component V_IDH (millimolar)"
    legend_constants[39] = "Kcat_IDH in component V_IDH (first_order_rate_constant)"
    legend_constants[40] = "ET_IDH in component V_IDH (millimolar)"
    legend_constants[41] = "ni in component V_IDH (dimensionless)"
    legend_constants[42] = "Km_alpha_KG in component V_KGDH (millimolar)"
    legend_constants[43] = "Kcat_KGDH in component V_KGDH (first_order_rate_constant)"
    legend_constants[44] = "ET_KGDH in component V_KGDH (millimolar)"
    legend_constants[45] = "Kd_Mg in component V_KGDH (millimolar)"
    legend_constants[46] = "Kd_Ca in component V_KGDH (micromolar)"
    legend_constants[47] = "n_alpha_KG in component V_KGDH (dimensionless)"
    legend_constants[48] = "Km_NAD in component V_KGDH (millimolar)"
    legend_constants[49] = "kf_SL in component V_SL (second_order_rate_constant)"
    legend_constants[50] = "Ke_SL in component V_SL (millimolar)"
    legend_constants[51] = "Kisdh_OAA in component V_SDH (millimolar)"
    legend_constants[52] = "Kcat_SDH in component V_SDH (first_order_rate_constant)"
    legend_constants[53] = "ET_SDH in component V_SDH (millimolar)"
    legend_constants[54] = "Km_Suc in component V_SDH (millimolar)"
    legend_constants[55] = "Ki_FUM in component V_SDH (millimolar)"
    legend_constants[56] = "Km_MAL in component V_MDH (millimolar)"
    legend_constants[57] = "Kcat_MDH in component V_MDH (first_order_rate_constant)"
    legend_constants[58] = "ET_MDH in component V_MDH (millimolar)"
    legend_constants[59] = "Ki_OAA in component V_MDH (millimolar)"
    legend_constants[132] = "fh_a in component V_MDH (dimensionless)"
    legend_constants[133] = "fh_i in component V_MDH (dimensionless)"
    legend_constants[60] = "Km_NAD in component V_MDH (millimolar)"
    legend_constants[61] = "kh1 in component V_MDH (millimolar)"
    legend_constants[62] = "kh2 in component V_MDH (millimolar)"
    legend_constants[63] = "kh3 in component V_MDH (millimolar)"
    legend_constants[64] = "kh4 in component V_MDH (millimolar)"
    legend_constants[65] = "k_offset in component V_MDH (dimensionless)"
    legend_constants[66] = "Ke_FH in component V_FH (dimensionless)"
    legend_constants[67] = "kf_FH in component V_FH (first_order_rate_constant)"
    legend_constants[68] = "Ke_AAT in component V_AAT (dimensionless)"
    legend_constants[69] = "kf_AAT in component V_AAT (second_order_rate_constant)"
    legend_constants[70] = "k_C_ASP in component V_C_ASP (first_order_rate_constant)"
    legend_constants[71] = "k1_SOD in component V_SOD (second_order_rate_constant)"
    legend_constants[72] = "k3_SOD in component V_SOD (second_order_rate_constant)"
    legend_constants[73] = "k5_SOD in component V_SOD (first_order_rate_constant)"
    legend_constants[74] = "ET_SOD in component V_SOD (millimolar)"
    legend_constants[75] = "Ki_H2O2 in component V_SOD (millimolar)"
    legend_constants[76] = "k1_CAT in component V_CAT (second_order_rate_constant)"
    legend_constants[77] = "ET_CAT in component V_CAT (millimolar)"
    legend_constants[78] = "fr in component V_CAT (per_millimolar)"
    legend_constants[79] = "phi1_GPX in component V_GPX (millimolar_second)"
    legend_constants[80] = "phi2_GPX in component V_GPX (millimolar_second)"
    legend_constants[81] = "ET_GPX in component V_GPX (millimolar)"
    legend_constants[82] = "k1_GR in component V_GR (first_order_rate_constant)"
    legend_constants[83] = "KM_GSSG in component V_GR (millimolar)"
    legend_constants[84] = "KM_NADPH in component V_GR (millimolar)"
    legend_constants[85] = "ET_GR in component V_GR (millimolar)"
    legend_algebraic[17] = "V_IMAC in component V_IMAC (flux)"
    legend_constants[86] = "Gmax in component V_IMAC (millimolar_per_second_volt)"
    legend_constants[87] = "GL in component V_IMAC (millimolar_per_second_volt)"
    legend_constants[88] = "a in component V_IMAC (dimensionless)"
    legend_constants[89] = "b in component V_IMAC (dimensionless)"
    legend_constants[90] = "kappa in component V_IMAC (per_volt)"
    legend_constants[91] = "delta_psi_bm in component V_IMAC (volt)"
    legend_constants[92] = "Kcc in component V_IMAC (millimolar)"
    legend_constants[93] = "j in component VTr_ROS (dimensionless)"
    legend_constants[94] = "rho_res in component oxidative_phosphorylation (millimolar)"
    legend_constants[95] = "rho_res_F in component oxidative_phosphorylation (millimolar)"
    legend_constants[96] = "ra in component oxidative_phosphorylation (first_order_rate_constant)"
    legend_constants[97] = "rc1 in component oxidative_phosphorylation (first_order_rate_constant)"
    legend_algebraic[22] = "Ares in component oxidative_phosphorylation (volt)"
    legend_constants[131] = "Ares_F in component oxidative_phosphorylation (volt)"
    legend_constants[98] = "r1 in component oxidative_phosphorylation (dimensionless)"
    legend_constants[99] = "r2 in component oxidative_phosphorylation (dimensionless)"
    legend_constants[100] = "r3 in component oxidative_phosphorylation (dimensionless)"
    legend_constants[101] = "rb in component oxidative_phosphorylation (first_order_rate_constant)"
    legend_constants[102] = "rc2 in component oxidative_phosphorylation (first_order_rate_constant)"
    legend_constants[103] = "Kres in component oxidative_phosphorylation (dimensionless)"
    legend_constants[104] = "Kres_F in component oxidative_phosphorylation (dimensionless)"
    legend_constants[105] = "gH in component oxidative_phosphorylation (millimolar_per_second_volt)"
    legend_constants[106] = "delta_psi_B in component oxidative_phosphorylation (volt)"
    legend_constants[107] = "g in component oxidative_phosphorylation (dimensionless)"
    legend_algebraic[24] = "delta_mu_H in component oxidative_phosphorylation (volt)"
    legend_constants[108] = "delta_pH in component oxidative_phosphorylation (dimensionless)"
    legend_constants[109] = "rho_F1 in component oxidative_phosphorylation (millimolar)"
    legend_constants[110] = "pa in component oxidative_phosphorylation (first_order_rate_constant)"
    legend_constants[111] = "pc1 in component oxidative_phosphorylation (first_order_rate_constant)"
    legend_algebraic[29] = "AF1 in component oxidative_phosphorylation (volt)"
    legend_constants[112] = "p1 in component oxidative_phosphorylation (dimensionless)"
    legend_constants[113] = "p2 in component oxidative_phosphorylation (dimensionless)"
    legend_constants[114] = "p3 in component oxidative_phosphorylation (dimensionless)"
    legend_constants[115] = "pb in component oxidative_phosphorylation (first_order_rate_constant)"
    legend_constants[116] = "pc2 in component oxidative_phosphorylation (first_order_rate_constant)"
    legend_constants[117] = "KF1 in component oxidative_phosphorylation (millimolar)"
    legend_constants[118] = "h in component calcium_dynamics (dimensionless)"
    legend_constants[119] = "delta_psi_0 in component calcium_dynamics (volt)"
    legend_constants[120] = "Vmax_ANT in component calcium_dynamics (flux)"
    legend_constants[121] = "L in component calcium_dynamics (dimensionless)"
    legend_constants[122] = "na in component calcium_dynamics (dimensionless)"
    legend_constants[123] = "Vmax_uni in component calcium_dynamics (flux)"
    legend_constants[124] = "K_act in component calcium_dynamics (micromolar)"
    legend_constants[125] = "K_trans in component calcium_dynamics (micromolar)"
    legend_constants[126] = "n in component calcium_dynamics (dimensionless)"
    legend_constants[127] = "Vmax_NaCa in component calcium_dynamics (flux)"
    legend_constants[128] = "KNa in component calcium_dynamics (millimolar)"
    legend_constants[129] = "KCa in component calcium_dynamics (micromolar)"
    legend_constants[130] = "b in component calcium_dynamics (dimensionless)"
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
    legend_rates[11] = "d/dt O2_m in component O2_m (millimolar)"
    legend_rates[12] = "d/dt O2_i in component O2_i (millimolar)"
    legend_rates[13] = "d/dt H2O2 in component H2O2 (millimolar)"
    legend_rates[14] = "d/dt GSH in component GSH (millimolar)"
    legend_rates[15] = "d/dt delta_psi_m in component mitochondrial_membrane (volt)"
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
    constants[19] = 0.05
    states[12] = 0.01
    states[13] = 0.01
    states[14] = 0.01
    constants[20] = 1.0
    constants[21] = 1.0
    states[15] = 0.01
    constants[22] = 8.315
    constants[23] = 310.16
    constants[24] = 96480
    constants[25] = 1.812
    constants[26] = 1.26E-2
    constants[27] = 6.4E-4
    constants[28] = 3.2
    constants[29] = 0.4
    constants[30] = 12.5
    constants[31] = 2.22
    constants[32] = 8.1E-5
    constants[33] = 5.98E-5
    constants[34] = 1.52
    constants[35] = 6.2E-2
    constants[36] = 1.41
    constants[37] = 0.923
    constants[38] = 0.19
    constants[39] = 1.94
    constants[40] = 0.109
    constants[41] = 1
    constants[42] = 1.94
    constants[43] = 0.15
    constants[44] = 0.5
    constants[45] = 0.0308
    constants[46] = 1.27
    constants[47] = 1.2
    constants[48] = 38.7
    constants[49] = 0.127
    constants[50] = 3.115
    constants[51] = 0.15
    constants[52] = 1.0
    constants[53] = 0.5
    constants[54] = 3.0E-2
    constants[55] = 1.3
    constants[56] = 1.493
    constants[57] = 2.775E1
    constants[58] = 0.154
    constants[59] = 3.1E-3
    constants[60] = 0.2244
    constants[61] = 1.13E-5
    constants[62] = 26.7
    constants[63] = 6.68E-9
    constants[64] = 5.62E-6
    constants[65] = 3.99E-2
    constants[66] = 1.0
    constants[67] = 0.83
    constants[68] = 6.6
    constants[69] = 0.644
    constants[70] = 0.01
    constants[71] = 2.4E6
    constants[72] = 4.8E4
    constants[73] = 5.0E-1
    constants[74] = 0.4E-3
    constants[75] = 0.5
    constants[76] = 1.7E4
    constants[77] = 0.001
    constants[78] = 50.0
    constants[79] = 0.15
    constants[80] = 0.5
    constants[81] = 0.00141
    constants[82] = 0.0308
    constants[83] = 1.94
    constants[84] = 38.7
    constants[85] = 1.27E-3
    constants[86] = 7.82
    constants[87] = 0.0782
    constants[88] = 1.0E-3
    constants[89] = 1.0E4
    constants[90] = 70.0
    constants[91] = 0.004
    constants[92] = 0.01
    constants[93] = 0.12
    constants[94] = 0.0006
    constants[95] = 0.0045
    constants[96] = 6.394E-10
    constants[97] = 2.656E-19
    constants[98] = 2.077E-18
    constants[99] = 1.728E-9
    constants[100] = 1.059E-26
    constants[101] = 1.762E-13
    constants[102] = 8.632E-27
    constants[103] = 1.35E18
    constants[104] = 5.765E13
    constants[105] = 0.01
    constants[106] = 0.05
    constants[107] = 0.85
    constants[108] = -0.6
    constants[109] = 0.06
    constants[110] = 1.656E-5
    constants[111] = 9.651E-14
    constants[112] = 1.346E-8
    constants[113] = 7.739E-7
    constants[114] = 6.65E-15
    constants[115] = 3.373E-7
    constants[116] = 4.585E-14
    constants[117] = 1.71E6
    constants[118] = 0.5
    constants[119] = 0.091
    constants[120] = 0.05
    constants[121] = 110.0
    constants[122] = 2.8
    constants[123] = 0.000625
    constants[124] = 0.38
    constants[125] = 19.0
    constants[126] = 3.0
    constants[127] = 0.005
    constants[128] = 9.4
    constants[129] = 3.75E-1
    constants[130] = 0.5
    constants[131] = ((constants[22]*constants[23])/constants[24])*log(constants[104]*(power(constants[16]/constants[15], 0.500000)))
    constants[132] = 1.00000/(1.00000+constants[11]/constants[61]+(power(constants[11], 2.00000))/(constants[61]*constants[62]))+constants[65]
    constants[133] = power(1.00000/(1.00000+constants[63]/constants[11]+(constants[63]*constants[64])/(power(constants[11], 2.00000))), 2.00000)
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[4] = constants[17]-states[1]
    algebraic[9] = (constants[39]*constants[40])/(1.00000+constants[11]/constants[32]+constants[33]/constants[11]+(power(constants[34]/states[2], constants[41]))/((1.00000+states[0]/constants[35])*(1.00000+states[10]/constants[36]))+(constants[37]/algebraic[4])*(1.00000+states[1]/constants[38])+((power(constants[34]/states[2], constants[41]))*(constants[37]/algebraic[4])*(1.00000+states[1]/constants[38]))/((1.00000+states[0]/constants[35])*(1.00000+states[10]/constants[36])))
    algebraic[6] = constants[21]-(states[2]+states[3]+states[4]+states[5]+states[6]+states[7]+states[8])
    algebraic[8] = constants[30]*(algebraic[6]-states[2]/constants[31])
    rates[2] = algebraic[8]-algebraic[9]
    algebraic[2] = constants[7]-states[0]
    algebraic[11] = constants[49]*(states[4]*states[0]-(states[5]*algebraic[2]*constants[13])/constants[50])
    algebraic[10] = (constants[43]*constants[44])/(1.00000+(power(constants[42]/states[3], constants[47]))/((1.00000+constants[10]/constants[45])*(1.00000+states[10]/constants[46]))+(constants[48]/algebraic[4])/((1.00000+constants[10]/constants[45])*(1.00000+states[10]/constants[46])))
    rates[4] = algebraic[10]-algebraic[11]
    algebraic[12] = (constants[52]*constants[53])/(1.00000+(constants[54]/states[5])*(1.00000+states[8]/constants[51])*(1.00000+states[6]/constants[55]))
    rates[5] = algebraic[11]-algebraic[12]
    algebraic[15] = constants[69]*(states[8]*constants[9]-(states[3]*states[9])/constants[68])
    rates[3] = algebraic[15]+algebraic[9]+-algebraic[10]
    algebraic[16] = constants[67]*(states[6]-states[7]/constants[66])
    rates[6] = algebraic[12]-algebraic[16]
    algebraic[13] = (constants[57]*constants[58]*constants[132]*constants[133])/(1.00000+(constants[56]/states[7])*(1.00000+states[8]/constants[59])+constants[60]/algebraic[4]+(constants[56]/states[7])*(1.00000+states[8]/constants[59])*(constants[60]/algebraic[4]))
    rates[7] = algebraic[16]-algebraic[13]
    algebraic[7] = (constants[28]*constants[29])/(1.00000+constants[26]/constants[14]+constants[27]/states[8]+(constants[26]/constants[14])*(constants[27]/states[8]))
    rates[8] = algebraic[13]-(algebraic[7]+algebraic[15])
    algebraic[18] = constants[70]*states[9]
    rates[9] = algebraic[15]-algebraic[18]
    algebraic[17] = (constants[88]+constants[89]/(1.00000+constants[92]/states[12]))*(constants[87]+constants[86]/(1.00000+exp(constants[90]*(constants[91]-states[15]))))*states[15]
    algebraic[20] = constants[93]*(algebraic[17]/states[15])*(states[15]-((constants[22]*constants[23])/constants[24])*log(states[11]/states[12], 10))
    algebraic[14] = (2.00000*constants[71]*constants[73]*(constants[71]+constants[72]*(1.00000+states[13]/constants[75]))*constants[74]*states[12])/(constants[73]*(2.00000*constants[71]+constants[72]*(1.00000+states[13]/constants[75]))+states[12]*constants[71]*constants[72]*(1.00000+states[13]/constants[75]))
    rates[12] = algebraic[20]-algebraic[14]
    algebraic[19] = 2.00000*constants[76]*constants[77]*states[13]*exp(-constants[78]*states[13])
    algebraic[21] = (constants[81]*states[13]*states[14])/(constants[79]*states[14]+constants[80]*states[13])
    rates[13] = algebraic[14]-(algebraic[19]+algebraic[21])
    algebraic[5] = 2.00000*(constants[20]-states[14])
    algebraic[23] = (constants[82]*constants[85])/(1.00000+constants[83]/algebraic[5]+constants[84]/constants[18]+(constants[83]/algebraic[5])*(constants[84]/constants[18]))
    rates[14] = algebraic[23]-algebraic[21]
    algebraic[22] = ((constants[22]*constants[23])/constants[24])*log(constants[103]*(power(states[1]/algebraic[4], 0.500000)))
    algebraic[24] = ((constants[22]*constants[23])/constants[24])*constants[108]+states[15]
    algebraic[26] = 0.500000*constants[94]*((((constants[96]+constants[97]*exp((6.00000*constants[24]*constants[106])/(constants[22]*constants[23])))*exp((algebraic[22]*constants[24])/(constants[22]*constants[23]))-constants[96]*exp((constants[107]*6.00000*constants[24]*algebraic[24])/(constants[22]*constants[23])))+constants[102]*exp((algebraic[22]*constants[24])/(constants[22]*constants[23]))*exp((constants[107]*6.00000*constants[24]*algebraic[24])/(constants[22]*constants[23])))/((1.00000+constants[98]*exp((constants[24]*algebraic[22])/(constants[22]*constants[23])))*exp((6.00000*constants[24]*constants[106])/(constants[22]*constants[23]))+(constants[99]+constants[100]*exp((constants[24]*algebraic[22])/(constants[22]*constants[23])))*exp((constants[107]*6.00000*constants[24]*algebraic[24])/(constants[22]*constants[23]))))
    rates[1] = -algebraic[26]+algebraic[9]+algebraic[10]+algebraic[13]
    rates[11] = constants[19]*algebraic[26]-algebraic[20]
    algebraic[3] = custom_piecewise([greater_equal(voi , 100.000) & less(voi , 300.000), constants[8] , True, 0.0500000])
    algebraic[32] = constants[120]*((1.00000-(0.0500000*constants[6]*0.450000*0.800000*states[0])/(0.450000*algebraic[3]*0.0500000*algebraic[2]))/((1.00000+((0.0500000*constants[6])/(0.450000*algebraic[3]))*exp((-constants[118]*constants[24]*constants[119])/(constants[22]*constants[23])))*(1.00000+(0.450000*0.800000*states[0])/(0.0500000*algebraic[2]))))
    algebraic[29] = ((constants[22]*constants[23])/constants[24])*log(constants[117]*(algebraic[2]/(states[0]*constants[12])))
    algebraic[30] = -constants[109]*(((100.000*constants[110]+constants[111]*exp((3.00000*constants[24]*constants[106])/(constants[22]*constants[23])))*exp((algebraic[29]*constants[24])/(constants[22]*constants[23]))-(constants[110]*exp((3.00000*constants[24]*algebraic[24])/(constants[22]*constants[23]))+constants[116]*exp((algebraic[29]*constants[24])/(constants[22]*constants[23]))*exp((3.00000*constants[24]*algebraic[24])/(constants[22]*constants[23]))))/((1.00000+constants[112]*exp((constants[24]*algebraic[29])/(constants[22]*constants[23])))*exp((3.00000*constants[24]*constants[106])/(constants[22]*constants[23]))+(constants[113]+constants[114]*exp((constants[24]*algebraic[29])/(constants[22]*constants[23])))*exp((3.00000*constants[24]*algebraic[24])/(constants[22]*constants[23]))))
    rates[0] = algebraic[32]-(algebraic[30]+algebraic[11])
    algebraic[0] = custom_piecewise([greater_equal(voi , 100.000) & less(voi , 300.000), 0.500000 , True, 4.00000])
    algebraic[1] = custom_piecewise([greater_equal(voi , constants[1]) & less_equal(voi , constants[2]) & less_equal((voi-constants[1])-floor((voi-constants[1])/algebraic[0])*algebraic[0] , constants[3]), constants[4] , True, 0.100000])
    algebraic[33] = constants[123]*(((algebraic[1]/constants[125])*(power(1.00000+algebraic[1]/constants[125], 3.00000))*((2.00000*constants[24]*(states[15]-constants[119]))/(constants[22]*constants[23])))/(power(1.00000+algebraic[1]/constants[125], 4.00000)+(constants[121]/(power(1.00000+algebraic[1]/constants[124], constants[122])))*(1.00000-exp((-2.00000*constants[24]*(states[15]-constants[119]))/(constants[22]*constants[23])))))
    algebraic[34] = constants[127]*((exp((constants[130]*constants[24]*(states[15]-constants[119]))/(constants[22]*constants[23]))*exp(log(algebraic[1]/states[10])))/((power(1.00000+constants[128]/constants[5], constants[126]))*(1.00000+constants[129]/states[10])))
    rates[10] = constants[0]*1.00000*(algebraic[33]-algebraic[34])
    algebraic[25] = 6.00000*constants[94]*((constants[96]*exp((constants[24]*algebraic[22])/(constants[22]*constants[23]))-(constants[96]+constants[101])*exp((constants[107]*6.00000*constants[24]*algebraic[24])/(constants[22]*constants[23])))/((1.00000+constants[98]*exp((constants[24]*algebraic[22])/(constants[22]*constants[23])))*exp((6.00000*constants[24]*constants[106])/(constants[22]*constants[23]))+(constants[99]+constants[100]*exp((constants[24]*algebraic[22])/(constants[22]*constants[23])))*exp((constants[107]*6.00000*constants[24]*algebraic[24])/(constants[22]*constants[23]))))
    algebraic[27] = 6.00000*constants[95]*((constants[96]*exp((constants[24]*constants[131])/(constants[22]*constants[23]))-(constants[96]+constants[101])*exp((constants[107]*6.00000*constants[24]*algebraic[24])/(constants[22]*constants[23])))/((1.00000+constants[98]*exp((constants[24]*constants[131])/(constants[22]*constants[23])))*exp((6.00000*constants[24]*constants[106])/(constants[22]*constants[23]))+(constants[99]+constants[100]*exp((constants[24]*constants[131])/(constants[22]*constants[23])))*exp((constants[107]*6.00000*constants[24]*algebraic[24])/(constants[22]*constants[23]))))
    algebraic[31] = -3.00000*constants[109]*((100.000*constants[110]*(1.00000+exp((constants[24]*algebraic[29])/(constants[22]*constants[23])))-(constants[110]+constants[115])*exp((3.00000*constants[24]*algebraic[24])/(constants[22]*constants[23])))/((1.00000+constants[112]*exp((constants[24]*algebraic[29])/(constants[22]*constants[23])))*exp((3.00000*constants[24]*constants[106])/(constants[22]*constants[23]))+(constants[113]+constants[114]*exp((constants[24]*algebraic[29])/(constants[22]*constants[23])))*exp((3.00000*constants[24]*algebraic[24])/(constants[22]*constants[23]))))
    algebraic[28] = constants[105]*algebraic[24]
    rates[15] = (algebraic[25]+algebraic[27]+-(algebraic[31]+algebraic[32]+algebraic[28]+algebraic[34]+2.00000*algebraic[33]))/constants[25]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[4] = constants[17]-states[1]
    algebraic[9] = (constants[39]*constants[40])/(1.00000+constants[11]/constants[32]+constants[33]/constants[11]+(power(constants[34]/states[2], constants[41]))/((1.00000+states[0]/constants[35])*(1.00000+states[10]/constants[36]))+(constants[37]/algebraic[4])*(1.00000+states[1]/constants[38])+((power(constants[34]/states[2], constants[41]))*(constants[37]/algebraic[4])*(1.00000+states[1]/constants[38]))/((1.00000+states[0]/constants[35])*(1.00000+states[10]/constants[36])))
    algebraic[6] = constants[21]-(states[2]+states[3]+states[4]+states[5]+states[6]+states[7]+states[8])
    algebraic[8] = constants[30]*(algebraic[6]-states[2]/constants[31])
    algebraic[2] = constants[7]-states[0]
    algebraic[11] = constants[49]*(states[4]*states[0]-(states[5]*algebraic[2]*constants[13])/constants[50])
    algebraic[10] = (constants[43]*constants[44])/(1.00000+(power(constants[42]/states[3], constants[47]))/((1.00000+constants[10]/constants[45])*(1.00000+states[10]/constants[46]))+(constants[48]/algebraic[4])/((1.00000+constants[10]/constants[45])*(1.00000+states[10]/constants[46])))
    algebraic[12] = (constants[52]*constants[53])/(1.00000+(constants[54]/states[5])*(1.00000+states[8]/constants[51])*(1.00000+states[6]/constants[55]))
    algebraic[15] = constants[69]*(states[8]*constants[9]-(states[3]*states[9])/constants[68])
    algebraic[16] = constants[67]*(states[6]-states[7]/constants[66])
    algebraic[13] = (constants[57]*constants[58]*constants[132]*constants[133])/(1.00000+(constants[56]/states[7])*(1.00000+states[8]/constants[59])+constants[60]/algebraic[4]+(constants[56]/states[7])*(1.00000+states[8]/constants[59])*(constants[60]/algebraic[4]))
    algebraic[7] = (constants[28]*constants[29])/(1.00000+constants[26]/constants[14]+constants[27]/states[8]+(constants[26]/constants[14])*(constants[27]/states[8]))
    algebraic[18] = constants[70]*states[9]
    algebraic[17] = (constants[88]+constants[89]/(1.00000+constants[92]/states[12]))*(constants[87]+constants[86]/(1.00000+exp(constants[90]*(constants[91]-states[15]))))*states[15]
    algebraic[20] = constants[93]*(algebraic[17]/states[15])*(states[15]-((constants[22]*constants[23])/constants[24])*log(states[11]/states[12], 10))
    algebraic[14] = (2.00000*constants[71]*constants[73]*(constants[71]+constants[72]*(1.00000+states[13]/constants[75]))*constants[74]*states[12])/(constants[73]*(2.00000*constants[71]+constants[72]*(1.00000+states[13]/constants[75]))+states[12]*constants[71]*constants[72]*(1.00000+states[13]/constants[75]))
    algebraic[19] = 2.00000*constants[76]*constants[77]*states[13]*exp(-constants[78]*states[13])
    algebraic[21] = (constants[81]*states[13]*states[14])/(constants[79]*states[14]+constants[80]*states[13])
    algebraic[5] = 2.00000*(constants[20]-states[14])
    algebraic[23] = (constants[82]*constants[85])/(1.00000+constants[83]/algebraic[5]+constants[84]/constants[18]+(constants[83]/algebraic[5])*(constants[84]/constants[18]))
    algebraic[22] = ((constants[22]*constants[23])/constants[24])*log(constants[103]*(power(states[1]/algebraic[4], 0.500000)))
    algebraic[24] = ((constants[22]*constants[23])/constants[24])*constants[108]+states[15]
    algebraic[26] = 0.500000*constants[94]*((((constants[96]+constants[97]*exp((6.00000*constants[24]*constants[106])/(constants[22]*constants[23])))*exp((algebraic[22]*constants[24])/(constants[22]*constants[23]))-constants[96]*exp((constants[107]*6.00000*constants[24]*algebraic[24])/(constants[22]*constants[23])))+constants[102]*exp((algebraic[22]*constants[24])/(constants[22]*constants[23]))*exp((constants[107]*6.00000*constants[24]*algebraic[24])/(constants[22]*constants[23])))/((1.00000+constants[98]*exp((constants[24]*algebraic[22])/(constants[22]*constants[23])))*exp((6.00000*constants[24]*constants[106])/(constants[22]*constants[23]))+(constants[99]+constants[100]*exp((constants[24]*algebraic[22])/(constants[22]*constants[23])))*exp((constants[107]*6.00000*constants[24]*algebraic[24])/(constants[22]*constants[23]))))
    algebraic[3] = custom_piecewise([greater_equal(voi , 100.000) & less(voi , 300.000), constants[8] , True, 0.0500000])
    algebraic[32] = constants[120]*((1.00000-(0.0500000*constants[6]*0.450000*0.800000*states[0])/(0.450000*algebraic[3]*0.0500000*algebraic[2]))/((1.00000+((0.0500000*constants[6])/(0.450000*algebraic[3]))*exp((-constants[118]*constants[24]*constants[119])/(constants[22]*constants[23])))*(1.00000+(0.450000*0.800000*states[0])/(0.0500000*algebraic[2]))))
    algebraic[29] = ((constants[22]*constants[23])/constants[24])*log(constants[117]*(algebraic[2]/(states[0]*constants[12])))
    algebraic[30] = -constants[109]*(((100.000*constants[110]+constants[111]*exp((3.00000*constants[24]*constants[106])/(constants[22]*constants[23])))*exp((algebraic[29]*constants[24])/(constants[22]*constants[23]))-(constants[110]*exp((3.00000*constants[24]*algebraic[24])/(constants[22]*constants[23]))+constants[116]*exp((algebraic[29]*constants[24])/(constants[22]*constants[23]))*exp((3.00000*constants[24]*algebraic[24])/(constants[22]*constants[23]))))/((1.00000+constants[112]*exp((constants[24]*algebraic[29])/(constants[22]*constants[23])))*exp((3.00000*constants[24]*constants[106])/(constants[22]*constants[23]))+(constants[113]+constants[114]*exp((constants[24]*algebraic[29])/(constants[22]*constants[23])))*exp((3.00000*constants[24]*algebraic[24])/(constants[22]*constants[23]))))
    algebraic[0] = custom_piecewise([greater_equal(voi , 100.000) & less(voi , 300.000), 0.500000 , True, 4.00000])
    algebraic[1] = custom_piecewise([greater_equal(voi , constants[1]) & less_equal(voi , constants[2]) & less_equal((voi-constants[1])-floor((voi-constants[1])/algebraic[0])*algebraic[0] , constants[3]), constants[4] , True, 0.100000])
    algebraic[33] = constants[123]*(((algebraic[1]/constants[125])*(power(1.00000+algebraic[1]/constants[125], 3.00000))*((2.00000*constants[24]*(states[15]-constants[119]))/(constants[22]*constants[23])))/(power(1.00000+algebraic[1]/constants[125], 4.00000)+(constants[121]/(power(1.00000+algebraic[1]/constants[124], constants[122])))*(1.00000-exp((-2.00000*constants[24]*(states[15]-constants[119]))/(constants[22]*constants[23])))))
    algebraic[34] = constants[127]*((exp((constants[130]*constants[24]*(states[15]-constants[119]))/(constants[22]*constants[23]))*exp(log(algebraic[1]/states[10])))/((power(1.00000+constants[128]/constants[5], constants[126]))*(1.00000+constants[129]/states[10])))
    algebraic[25] = 6.00000*constants[94]*((constants[96]*exp((constants[24]*algebraic[22])/(constants[22]*constants[23]))-(constants[96]+constants[101])*exp((constants[107]*6.00000*constants[24]*algebraic[24])/(constants[22]*constants[23])))/((1.00000+constants[98]*exp((constants[24]*algebraic[22])/(constants[22]*constants[23])))*exp((6.00000*constants[24]*constants[106])/(constants[22]*constants[23]))+(constants[99]+constants[100]*exp((constants[24]*algebraic[22])/(constants[22]*constants[23])))*exp((constants[107]*6.00000*constants[24]*algebraic[24])/(constants[22]*constants[23]))))
    algebraic[27] = 6.00000*constants[95]*((constants[96]*exp((constants[24]*constants[131])/(constants[22]*constants[23]))-(constants[96]+constants[101])*exp((constants[107]*6.00000*constants[24]*algebraic[24])/(constants[22]*constants[23])))/((1.00000+constants[98]*exp((constants[24]*constants[131])/(constants[22]*constants[23])))*exp((6.00000*constants[24]*constants[106])/(constants[22]*constants[23]))+(constants[99]+constants[100]*exp((constants[24]*constants[131])/(constants[22]*constants[23])))*exp((constants[107]*6.00000*constants[24]*algebraic[24])/(constants[22]*constants[23]))))
    algebraic[31] = -3.00000*constants[109]*((100.000*constants[110]*(1.00000+exp((constants[24]*algebraic[29])/(constants[22]*constants[23])))-(constants[110]+constants[115])*exp((3.00000*constants[24]*algebraic[24])/(constants[22]*constants[23])))/((1.00000+constants[112]*exp((constants[24]*algebraic[29])/(constants[22]*constants[23])))*exp((3.00000*constants[24]*constants[106])/(constants[22]*constants[23]))+(constants[113]+constants[114]*exp((constants[24]*algebraic[29])/(constants[22]*constants[23])))*exp((3.00000*constants[24]*algebraic[24])/(constants[22]*constants[23]))))
    algebraic[28] = constants[105]*algebraic[24]
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
