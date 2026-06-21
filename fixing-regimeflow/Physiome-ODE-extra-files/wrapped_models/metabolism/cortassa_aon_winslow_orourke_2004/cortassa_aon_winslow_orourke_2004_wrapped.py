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


# =========================
# Auto-generated wrapper
# =========================
import numpy as np
from scipy.integrate import odeint


class Parameters:
    def __init__(self):
        self.f = 0.0003
        self.stim_start = 0
        self.stim_end = 10000
        self.stim_duration = 0.4
        self.pulse_value = 1
        self.Na_i = 10.0
        self.ATP_i = 6.5
        self.Cm = 15.0
        self.pulse_value_1 = 0.15
        self.GLU = 20
        self.Mg = 0.4
        self.H = 2.5E-5
        self.Pi = 20.0
        self.CoA = 0.02
        self.AcCoA = 0.0002
        self.FAD = 0.01
        self.FADH2 = 1.24
        self.C_PN = 10.0
        self.NADPH = 1.0
        self.shunt = 0.05
        self.GT = 1.0
        self.C_Kint = 1.0
        self.R = 8.315
        self.T = 310.16
        self.F = 96480
        self.C_mito = 1.812
        self.Km_AcCoA = 1.26E-2
        self.Km_OAA = 6.4E-4
        self.Kcat_CS = 3.2
        self.ET_CS = 0.4
        self.Kf_ACO = 12.5
        self.KE_ACO = 2.22
        self.Kh_1 = 8.1E-5
        self.Kh_2 = 5.98E-5
        self.Km_ISOC = 1.52
        self.Ka_ADP = 6.2E-2
        self.Ka_Ca = 1.41
        self.Km_NAD = 0.923
        self.Ki_NADH = 0.19
        self.Kcat_IDH = 1.94
        self.ET_IDH = 0.109
        self.ni = 1
        self.Km_alpha_KG = 1.94
        self.Kcat_KGDH = 0.15
        self.ET_KGDH = 0.5
        self.Kd_Mg = 0.0308
        self.Kd_Ca = 1.27
        self.n_alpha_KG = 1.2
        self.Km_NAD_1 = 38.7
        self.kf_SL = 0.127
        self.Ke_SL = 3.115
        self.Kisdh_OAA = 0.15
        self.Kcat_SDH = 1.0
        self.ET_SDH = 0.5
        self.Km_Suc = 3.0E-2
        self.Ki_FUM = 1.3
        self.Km_MAL = 1.493
        self.Kcat_MDH = 2.775E1
        self.ET_MDH = 0.154
        self.Ki_OAA = 3.1E-3
        self.Km_NAD_2 = 0.2244
        self.kh1 = 1.13E-5
        self.kh2 = 26.7
        self.kh3 = 6.68E-9
        self.kh4 = 5.62E-6
        self.k_offset = 3.99E-2
        self.Ke_FH = 1.0
        self.kf_FH = 0.83
        self.Ke_AAT = 6.6
        self.kf_AAT = 0.644
        self.k_C_ASP = 0.01
        self.k1_SOD = 2.4E6
        self.k3_SOD = 4.8E4
        self.k5_SOD = 5.0E-1
        self.ET_SOD = 0.4E-3
        self.Ki_H2O2 = 0.5
        self.k1_CAT = 1.7E4
        self.ET_CAT = 0.001
        self.fr = 50.0
        self.phi1_GPX = 0.15
        self.phi2_GPX = 0.5
        self.ET_GPX = 0.00141
        self.k1_GR = 0.0308
        self.KM_GSSG = 1.94
        self.KM_NADPH = 38.7
        self.ET_GR = 1.27E-3
        self.Gmax = 7.82
        self.GL = 0.0782
        self.a = 1.0E-3
        self.b = 1.0E4
        self.kappa = 70.0
        self.delta_psi_bm = 0.004
        self.Kcc = 0.01
        self.j = 0.12
        self.rho_res = 0.0006
        self.rho_res_F = 0.0045
        self.ra = 6.394E-10
        self.rc1 = 2.656E-19
        self.r1 = 2.077E-18
        self.r2 = 1.728E-9
        self.r3 = 1.059E-26
        self.rb = 1.762E-13
        self.rc2 = 8.632E-27
        self.Kres = 1.35E18
        self.Kres_F = 5.765E13
        self.gH = 0.01
        self.delta_psi_B = 0.05
        self.g = 0.85
        self.delta_pH = -0.6
        self.rho_F1 = 0.06
        self.pa = 1.656E-5
        self.pc1 = 9.651E-14
        self.p1 = 1.346E-8
        self.p2 = 7.739E-7
        self.p3 = 6.65E-15
        self.pb = 3.373E-7
        self.pc2 = 4.585E-14
        self.KF1 = 1.71E6
        self.h = 0.5
        self.delta_psi_0 = 0.091
        self.Vmax_ANT = 0.05
        self.L = 110.0
        self.na = 2.8
        self.Vmax_uni = 0.000625
        self.K_act = 0.38
        self.K_trans = 19.0
        self.n = 3.0
        self.Vmax_NaCa = 0.005
        self.KNa = 9.4
        self.KCa = 3.75E-1
        self.b_1 = 0.5

    def to_dict(self):
        return {
            "f": self.f,
            "stim_start": self.stim_start,
            "stim_end": self.stim_end,
            "stim_duration": self.stim_duration,
            "pulse_value": self.pulse_value,
            "Na_i": self.Na_i,
            "ATP_i": self.ATP_i,
            "Cm": self.Cm,
            "pulse_value_1": self.pulse_value_1,
            "GLU": self.GLU,
            "Mg": self.Mg,
            "H": self.H,
            "Pi": self.Pi,
            "CoA": self.CoA,
            "AcCoA": self.AcCoA,
            "FAD": self.FAD,
            "FADH2": self.FADH2,
            "C_PN": self.C_PN,
            "NADPH": self.NADPH,
            "shunt": self.shunt,
            "GT": self.GT,
            "C_Kint": self.C_Kint,
            "R": self.R,
            "T": self.T,
            "F": self.F,
            "C_mito": self.C_mito,
            "Km_AcCoA": self.Km_AcCoA,
            "Km_OAA": self.Km_OAA,
            "Kcat_CS": self.Kcat_CS,
            "ET_CS": self.ET_CS,
            "Kf_ACO": self.Kf_ACO,
            "KE_ACO": self.KE_ACO,
            "Kh_1": self.Kh_1,
            "Kh_2": self.Kh_2,
            "Km_ISOC": self.Km_ISOC,
            "Ka_ADP": self.Ka_ADP,
            "Ka_Ca": self.Ka_Ca,
            "Km_NAD": self.Km_NAD,
            "Ki_NADH": self.Ki_NADH,
            "Kcat_IDH": self.Kcat_IDH,
            "ET_IDH": self.ET_IDH,
            "ni": self.ni,
            "Km_alpha_KG": self.Km_alpha_KG,
            "Kcat_KGDH": self.Kcat_KGDH,
            "ET_KGDH": self.ET_KGDH,
            "Kd_Mg": self.Kd_Mg,
            "Kd_Ca": self.Kd_Ca,
            "n_alpha_KG": self.n_alpha_KG,
            "Km_NAD_1": self.Km_NAD_1,
            "kf_SL": self.kf_SL,
            "Ke_SL": self.Ke_SL,
            "Kisdh_OAA": self.Kisdh_OAA,
            "Kcat_SDH": self.Kcat_SDH,
            "ET_SDH": self.ET_SDH,
            "Km_Suc": self.Km_Suc,
            "Ki_FUM": self.Ki_FUM,
            "Km_MAL": self.Km_MAL,
            "Kcat_MDH": self.Kcat_MDH,
            "ET_MDH": self.ET_MDH,
            "Ki_OAA": self.Ki_OAA,
            "Km_NAD_2": self.Km_NAD_2,
            "kh1": self.kh1,
            "kh2": self.kh2,
            "kh3": self.kh3,
            "kh4": self.kh4,
            "k_offset": self.k_offset,
            "Ke_FH": self.Ke_FH,
            "kf_FH": self.kf_FH,
            "Ke_AAT": self.Ke_AAT,
            "kf_AAT": self.kf_AAT,
            "k_C_ASP": self.k_C_ASP,
            "k1_SOD": self.k1_SOD,
            "k3_SOD": self.k3_SOD,
            "k5_SOD": self.k5_SOD,
            "ET_SOD": self.ET_SOD,
            "Ki_H2O2": self.Ki_H2O2,
            "k1_CAT": self.k1_CAT,
            "ET_CAT": self.ET_CAT,
            "fr": self.fr,
            "phi1_GPX": self.phi1_GPX,
            "phi2_GPX": self.phi2_GPX,
            "ET_GPX": self.ET_GPX,
            "k1_GR": self.k1_GR,
            "KM_GSSG": self.KM_GSSG,
            "KM_NADPH": self.KM_NADPH,
            "ET_GR": self.ET_GR,
            "Gmax": self.Gmax,
            "GL": self.GL,
            "a": self.a,
            "b": self.b,
            "kappa": self.kappa,
            "delta_psi_bm": self.delta_psi_bm,
            "Kcc": self.Kcc,
            "j": self.j,
            "rho_res": self.rho_res,
            "rho_res_F": self.rho_res_F,
            "ra": self.ra,
            "rc1": self.rc1,
            "r1": self.r1,
            "r2": self.r2,
            "r3": self.r3,
            "rb": self.rb,
            "rc2": self.rc2,
            "Kres": self.Kres,
            "Kres_F": self.Kres_F,
            "gH": self.gH,
            "delta_psi_B": self.delta_psi_B,
            "g": self.g,
            "delta_pH": self.delta_pH,
            "rho_F1": self.rho_F1,
            "pa": self.pa,
            "pc1": self.pc1,
            "p1": self.p1,
            "p2": self.p2,
            "p3": self.p3,
            "pb": self.pb,
            "pc2": self.pc2,
            "KF1": self.KF1,
            "h": self.h,
            "delta_psi_0": self.delta_psi_0,
            "Vmax_ANT": self.Vmax_ANT,
            "L": self.L,
            "na": self.na,
            "Vmax_uni": self.Vmax_uni,
            "K_act": self.K_act,
            "K_trans": self.K_trans,
            "n": self.n,
            "Vmax_NaCa": self.Vmax_NaCa,
            "KNa": self.KNa,
            "KCa": self.KCa,
            "b_1": self.b_1,
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
        y0=[0.1, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "cortassa_aon_winslow_orourke_2004"
        self.curve_names = [
            "ADP_m",
            "NADH",
            "ISOC",
            "alpha_KG",
            "SCoA",
            "Suc",
            "FUM",
            "MAL",
            "OAA",
            "ASP",
            "Ca_m",
            "O2_m",
            "O2_i",
            "H2O2",
            "GSH",
            "delta_psi_m",
        ]
        self.state_names = ['ADP_m', 'NADH', 'ISOC', 'alpha_KG', 'SCoA', 'Suc', 'FUM', 'MAL', 'OAA', 'ASP', 'Ca_m', 'O2_m', 'O2_i', 'H2O2', 'GSH', 'delta_psi_m']
        self.algebraic_names = ['stim_period', 'Ca_i', 'ATP_m', 'ADP_i', 'NAD', 'GSSG', 'CIT', 'V_CS', 'V_ACO', 'V_IDH', 'V_KGDH', 'V_SL', 'V_SDH', 'V_MDH', 'V_SOD', 'V_AAT', 'V_FH', 'V_IMAC', 'V_C_ASP', 'V_CAT', 'VTr_ROS', 'V_GPX', 'Ares', 'V_GR', 'delta_mu_H', 'V_He', 'V_O2', 'V_He_F', 'V_Hleak', 'AF1', 'V_ATPase', 'V_Hu', 'V_ANT', 'V_uni', 'V_NaCa']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 134
        p = self.params

        # direct mapping
        c[0] = p.f
        c[1] = p.stim_start
        c[2] = p.stim_end
        c[3] = p.stim_duration
        c[4] = p.pulse_value
        c[5] = p.Na_i
        c[6] = p.ATP_i
        c[7] = p.Cm
        c[8] = p.pulse_value_1
        c[9] = p.GLU
        c[10] = p.Mg
        c[11] = p.H
        c[12] = p.Pi
        c[13] = p.CoA
        c[14] = p.AcCoA
        c[15] = p.FAD
        c[16] = p.FADH2
        c[17] = p.C_PN
        c[18] = p.NADPH
        c[19] = p.shunt
        c[20] = p.GT
        c[21] = p.C_Kint
        c[22] = p.R
        c[23] = p.T
        c[24] = p.F
        c[25] = p.C_mito
        c[26] = p.Km_AcCoA
        c[27] = p.Km_OAA
        c[28] = p.Kcat_CS
        c[29] = p.ET_CS
        c[30] = p.Kf_ACO
        c[31] = p.KE_ACO
        c[32] = p.Kh_1
        c[33] = p.Kh_2
        c[34] = p.Km_ISOC
        c[35] = p.Ka_ADP
        c[36] = p.Ka_Ca
        c[37] = p.Km_NAD
        c[38] = p.Ki_NADH
        c[39] = p.Kcat_IDH
        c[40] = p.ET_IDH
        c[41] = p.ni
        c[42] = p.Km_alpha_KG
        c[43] = p.Kcat_KGDH
        c[44] = p.ET_KGDH
        c[45] = p.Kd_Mg
        c[46] = p.Kd_Ca
        c[47] = p.n_alpha_KG
        c[48] = p.Km_NAD_1
        c[49] = p.kf_SL
        c[50] = p.Ke_SL
        c[51] = p.Kisdh_OAA
        c[52] = p.Kcat_SDH
        c[53] = p.ET_SDH
        c[54] = p.Km_Suc
        c[55] = p.Ki_FUM
        c[56] = p.Km_MAL
        c[57] = p.Kcat_MDH
        c[58] = p.ET_MDH
        c[59] = p.Ki_OAA
        c[60] = p.Km_NAD_2
        c[61] = p.kh1
        c[62] = p.kh2
        c[63] = p.kh3
        c[64] = p.kh4
        c[65] = p.k_offset
        c[66] = p.Ke_FH
        c[67] = p.kf_FH
        c[68] = p.Ke_AAT
        c[69] = p.kf_AAT
        c[70] = p.k_C_ASP
        c[71] = p.k1_SOD
        c[72] = p.k3_SOD
        c[73] = p.k5_SOD
        c[74] = p.ET_SOD
        c[75] = p.Ki_H2O2
        c[76] = p.k1_CAT
        c[77] = p.ET_CAT
        c[78] = p.fr
        c[79] = p.phi1_GPX
        c[80] = p.phi2_GPX
        c[81] = p.ET_GPX
        c[82] = p.k1_GR
        c[83] = p.KM_GSSG
        c[84] = p.KM_NADPH
        c[85] = p.ET_GR
        c[86] = p.Gmax
        c[87] = p.GL
        c[88] = p.a
        c[89] = p.b
        c[90] = p.kappa
        c[91] = p.delta_psi_bm
        c[92] = p.Kcc
        c[93] = p.j
        c[94] = p.rho_res
        c[95] = p.rho_res_F
        c[96] = p.ra
        c[97] = p.rc1
        c[98] = p.r1
        c[99] = p.r2
        c[100] = p.r3
        c[101] = p.rb
        c[102] = p.rc2
        c[103] = p.Kres
        c[104] = p.Kres_F
        c[105] = p.gH
        c[106] = p.delta_psi_B
        c[107] = p.g
        c[108] = p.delta_pH
        c[109] = p.rho_F1
        c[110] = p.pa
        c[111] = p.pc1
        c[112] = p.p1
        c[113] = p.p2
        c[114] = p.p3
        c[115] = p.pb
        c[116] = p.pc2
        c[117] = p.KF1
        c[118] = p.h
        c[119] = p.delta_psi_0
        c[120] = p.Vmax_ANT
        c[121] = p.L
        c[122] = p.na
        c[123] = p.Vmax_uni
        c[124] = p.K_act
        c[125] = p.K_trans
        c[126] = p.n
        c[127] = p.Vmax_NaCa
        c[128] = p.KNa
        c[129] = p.KCa
        c[130] = p.b_1

        # derived constants
        c[131] = ((c[22]*c[23])/c[24])*log(c[104]*(power(c[16]/c[15], 0.500000)))
        c[132] = 1.00000/(1.00000+c[11]/c[61]+(power(c[11], 2.00000))/(c[61]*c[62]))+c[65]
        c[133] = power(1.00000/(1.00000+c[63]/c[11]+(c[63]*c[64])/(power(c[11], 2.00000))), 2.00000)

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
