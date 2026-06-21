# Size of variable arrays:
sizeAlgebraic = 108
sizeStates = 26
sizeConstants = 80
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component Environment (ms)"
    legend_constants[0] = "R in component Environment (J_per_moleK)"
    legend_constants[1] = "T in component Environment (kelvin)"
    legend_constants[2] = "F in component Environment (coulomb_per_mmole)"
    legend_constants[3] = "K_o in component Environment (mM)"
    legend_constants[4] = "Ca_o in component Environment (mM)"
    legend_constants[5] = "Na_o in component Environment (mM)"
    legend_constants[75] = "FonRT in component Environment (per_mV)"
    legend_states[0] = "V in component cell (mV)"
    legend_algebraic[49] = "xik1 in component IK1 (nA_per_nF)"
    legend_algebraic[60] = "xito in component Ito (nA_per_nF)"
    legend_algebraic[65] = "xiNaK in component INaK (nA_per_nF)"
    legend_constants[6] = "wca in component cell (mV_per_uM)"
    legend_algebraic[102] = "xiNaCa in component INaCa (nA_per_nF)"
    legend_algebraic[93] = "xica in component ICaL (nA_per_nF)"
    legend_algebraic[107] = "Itotal in component cell (nA_per_nF)"
    legend_algebraic[106] = "xina in component INa (nA_per_nF)"
    legend_algebraic[51] = "xikr in component IKr (nA_per_nF)"
    legend_algebraic[104] = "xiks in component IKs (nA_per_nF)"
    legend_algebraic[10] = "i_Stim in component cell (nA_per_nF)"
    legend_constants[7] = "stim_offset in component cell (ms)"
    legend_constants[8] = "stim_period in component cell (ms)"
    legend_constants[9] = "stim_duration in component cell (ms)"
    legend_constants[10] = "stim_amplitude in component cell (nA_per_nF)"
    legend_algebraic[3] = "past in component cell (ms)"
    legend_algebraic[105] = "ena in component reversal_potentials (mV)"
    legend_states[1] = "xm in component INa (dimensionless)"
    legend_states[2] = "xh in component INa (dimensionless)"
    legend_states[3] = "xj in component INa (dimensionless)"
    legend_constants[11] = "gna in component INa (uS_per_nF)"
    legend_algebraic[0] = "am in component INa (per_ms)"
    legend_algebraic[7] = "bm in component INa (per_ms)"
    legend_algebraic[1] = "ah in component INa (per_ms)"
    legend_algebraic[8] = "bh in component INa (per_ms)"
    legend_algebraic[2] = "aj in component INa (per_ms)"
    legend_algebraic[9] = "bj in component INa (per_ms)"
    legend_states[4] = "Ca_dyad in component Ca (uM)"
    legend_algebraic[88] = "csm in component Ca (mM)"
    legend_states[5] = "c1 in component ICaL (dimensionless)"
    legend_states[6] = "c2 in component ICaL (dimensionless)"
    legend_states[7] = "xi1ca in component ICaL (dimensionless)"
    legend_states[8] = "xi1ba in component ICaL (dimensionless)"
    legend_states[9] = "xi2ca in component ICaL (dimensionless)"
    legend_states[10] = "xi2ba in component ICaL (dimensionless)"
    legend_constants[12] = "gca in component ICaL (mmole_per_coulomb_cm)"
    legend_constants[13] = "pca in component ICaL (cm_per_s)"
    legend_algebraic[14] = "za in component ICaL (dimensionless)"
    legend_algebraic[18] = "poinf in component ICaL (dimensionless)"
    legend_algebraic[26] = "fca in component ICaL (dimensionless)"
    legend_constants[14] = "vth in component ICaL (mV)"
    legend_constants[15] = "s6 in component ICaL (mV)"
    legend_constants[16] = "vx in component ICaL (mV)"
    legend_constants[17] = "sx in component ICaL (mV)"
    legend_constants[18] = "vy in component ICaL (mV)"
    legend_constants[19] = "sy in component ICaL (mV)"
    legend_constants[20] = "vyr in component ICaL (mV)"
    legend_constants[21] = "syr in component ICaL (mV)"
    legend_constants[22] = "cat in component ICaL (uM)"
    legend_constants[23] = "cpt in component ICaL (uM)"
    legend_algebraic[23] = "alpha in component ICaL (per_ms)"
    legend_algebraic[25] = "beta in component ICaL (per_ms)"
    legend_algebraic[28] = "k1 in component ICaL (per_ms)"
    legend_constants[24] = "k2 in component ICaL (per_ms)"
    legend_constants[25] = "k1t in component ICaL (per_ms)"
    legend_constants[26] = "k2t in component ICaL (per_ms)"
    legend_algebraic[31] = "k3 in component ICaL (per_ms)"
    legend_algebraic[32] = "k3t in component ICaL (per_ms)"
    legend_algebraic[39] = "k6 in component ICaL (per_ms)"
    legend_algebraic[40] = "k5 in component ICaL (per_ms)"
    legend_algebraic[41] = "k6t in component ICaL (per_ms)"
    legend_algebraic[42] = "k5t in component ICaL (per_ms)"
    legend_algebraic[43] = "k4 in component ICaL (per_ms)"
    legend_algebraic[44] = "k4t in component ICaL (per_ms)"
    legend_constants[27] = "r1 in component ICaL (per_ms)"
    legend_constants[28] = "r2 in component ICaL (per_ms)"
    legend_algebraic[27] = "s1 in component ICaL (per_ms)"
    legend_constants[29] = "s1t in component ICaL (per_ms)"
    legend_algebraic[29] = "s2 in component ICaL (per_ms)"
    legend_constants[76] = "s2t in component ICaL (per_ms)"
    legend_algebraic[34] = "recov in component ICaL (ms)"
    legend_constants[30] = "tca in component ICaL (ms)"
    legend_algebraic[35] = "tau_ca in component ICaL (ms)"
    legend_algebraic[36] = "tauca in component ICaL (ms)"
    legend_algebraic[37] = "tauba in component ICaL (ms)"
    legend_constants[31] = "taupo in component ICaL (ms)"
    legend_constants[32] = "tau3 in component ICaL (ms)"
    legend_algebraic[33] = "Pr in component ICaL (dimensionless)"
    legend_algebraic[38] = "Ps in component ICaL (dimensionless)"
    legend_algebraic[30] = "poi in component ICaL (dimensionless)"
    legend_algebraic[45] = "po in component ICaL (dimensionless)"
    legend_algebraic[89] = "rxa in component ICaL (mA_per_cm2)"
    legend_algebraic[90] = "jca in component ICaL (uM_per_ms)"
    legend_constants[79] = "ek in component reversal_potentials (mV)"
    legend_constants[33] = "gkix in component IK1 (uS_per_nF)"
    legend_algebraic[46] = "aki in component IK1 (per_ms)"
    legend_algebraic[47] = "bki in component IK1 (per_ms)"
    legend_algebraic[48] = "xkin in component IK1 (dimensionless)"
    legend_states[11] = "xr in component IKr (dimensionless)"
    legend_constants[34] = "gkr in component IKr (uS_per_nF)"
    legend_algebraic[4] = "xkrv1 in component IKr (per_ms)"
    legend_algebraic[11] = "xkrv2 in component IKr (per_ms)"
    legend_algebraic[15] = "taukr in component IKr (ms)"
    legend_algebraic[19] = "xkrinf in component IKr (dimensionless)"
    legend_algebraic[50] = "rg in component IKr (dimensionless)"
    legend_states[12] = "Ca_i in component Ca (uM)"
    legend_constants[35] = "gks in component IKs (uS_per_nF)"
    legend_states[13] = "xs1 in component IKs (dimensionless)"
    legend_states[14] = "xs2 in component IKs (dimensionless)"
    legend_algebraic[103] = "eks in component reversal_potentials (mV)"
    legend_algebraic[5] = "xs1ss in component IKs (dimensionless)"
    legend_algebraic[12] = "xs2ss in component IKs (dimensionless)"
    legend_algebraic[16] = "tauxs1 in component IKs (ms)"
    legend_algebraic[20] = "tauxs2 in component IKs (ms)"
    legend_algebraic[52] = "gksx in component IKs (dimensionless)"
    legend_algebraic[56] = "xitos in component Ito (nA_per_nF)"
    legend_algebraic[58] = "xitof in component Ito (nA_per_nF)"
    legend_states[15] = "xtos in component Ito (dimensionless)"
    legend_states[16] = "ytos in component Ito (dimensionless)"
    legend_states[17] = "xtof in component Ito (dimensionless)"
    legend_states[18] = "ytof in component Ito (dimensionless)"
    legend_constants[36] = "gtos in component Ito (uS_per_nF)"
    legend_constants[37] = "gtof in component Ito (uS_per_nF)"
    legend_algebraic[6] = "rt1 in component Ito (dimensionless)"
    legend_algebraic[53] = "rt2 in component Ito (dimensionless)"
    legend_algebraic[55] = "rt3 in component Ito (dimensionless)"
    legend_algebraic[13] = "rt4 in component Ito (dimensionless)"
    legend_algebraic[57] = "rt5 in component Ito (dimensionless)"
    legend_algebraic[17] = "xtos_inf in component Ito (dimensionless)"
    legend_algebraic[59] = "ytos_inf in component Ito (dimensionless)"
    legend_algebraic[21] = "xtof_inf in component Ito (dimensionless)"
    legend_algebraic[61] = "ytof_inf in component Ito (dimensionless)"
    legend_algebraic[54] = "rs_inf in component Ito (dimensionless)"
    legend_algebraic[22] = "txs in component Ito (ms)"
    legend_algebraic[62] = "tys in component Ito (ms)"
    legend_algebraic[24] = "txf in component Ito (ms)"
    legend_algebraic[64] = "tyf in component Ito (ms)"
    legend_states[19] = "Na_i in component Na (mM)"
    legend_constants[38] = "gNaK in component INaK (nA_per_nF)"
    legend_constants[39] = "xkmko in component INaK (mM)"
    legend_constants[40] = "xkmnai in component INaK (mM)"
    legend_constants[77] = "sigma in component INaK (dimensionless)"
    legend_algebraic[63] = "fNaK in component INaK (dimensionless)"
    legend_states[20] = "Ca_submem in component Ca (uM)"
    legend_constants[41] = "gNaCa in component INaCa (uM_per_ms)"
    legend_algebraic[67] = "aloss in component INaCa (dimensionless)"
    legend_algebraic[97] = "yz1 in component INaCa (mM4)"
    legend_algebraic[98] = "yz2 in component INaCa (mM4)"
    legend_algebraic[68] = "yz3 in component INaCa (mM4)"
    legend_algebraic[99] = "yz4 in component INaCa (mM4)"
    legend_algebraic[95] = "zw3 in component INaCa (mM4)"
    legend_algebraic[66] = "zw4 in component INaCa (dimensionless)"
    legend_algebraic[100] = "zw8 in component INaCa (mM4)"
    legend_algebraic[101] = "jNaCa in component INaCa (uM_per_ms)"
    legend_constants[42] = "xkdna in component INaCa (uM)"
    legend_constants[43] = "xmcao in component INaCa (mM)"
    legend_constants[44] = "xmnao in component INaCa (mM)"
    legend_constants[45] = "xmnai in component INaCa (mM)"
    legend_constants[46] = "xmcai in component INaCa (mM)"
    legend_states[21] = "Ca_NSR in component Ca (uM)"
    legend_algebraic[87] = "dCa_JSR in component Ca (uM_per_ms)"
    legend_constants[47] = "cstar in component Irel (uM)"
    legend_states[22] = "Ca_JSR in component Irel (uM)"
    legend_constants[48] = "gryr in component Irel (per_ms)"
    legend_constants[49] = "gbarsr in component Irel (dimensionless)"
    legend_constants[50] = "gdyad in component Irel (mmole_per_coulomb_cm)"
    legend_constants[51] = "ax in component Irel (per_mV)"
    legend_constants[52] = "ay in component Irel (per_mV)"
    legend_constants[53] = "av in component Irel (per_ms)"
    legend_constants[78] = "bv in component Irel (uM_per_ms)"
    legend_algebraic[69] = "Qr0 in component Irel (uM_per_ms)"
    legend_algebraic[70] = "Qr in component Irel (uM_per_ms)"
    legend_algebraic[71] = "sparkV in component Irel (dimensionless)"
    legend_algebraic[91] = "spark_rate in component Irel (per_ms)"
    legend_constants[54] = "taua in component Irel (ms)"
    legend_constants[55] = "taur in component Irel (ms)"
    legend_algebraic[92] = "xirp in component Irel (uM_per_ms)"
    legend_algebraic[94] = "xicap in component Irel (uM_per_ms)"
    legend_algebraic[96] = "xiryr in component Irel (uM_per_ms)"
    legend_states[23] = "xir in component Irel (uM_per_ms)"
    legend_algebraic[72] = "jup in component Ileak_Iup_Ixfer (uM_per_ms)"
    legend_algebraic[73] = "jleak in component Ileak_Iup_Ixfer (uM_per_ms)"
    legend_constants[56] = "cup in component Ileak_Iup_Ixfer (uM)"
    legend_constants[57] = "kj in component Ileak_Iup_Ixfer (uM)"
    legend_constants[58] = "vup in component Ileak_Iup_Ixfer (uM_per_ms)"
    legend_constants[59] = "gleak in component Ileak_Iup_Ixfer (per_ms)"
    legend_constants[60] = "bcal in component Ca (uM)"
    legend_constants[61] = "xkcal in component Ca (uM)"
    legend_constants[62] = "srmax in component Ca (uM)"
    legend_constants[63] = "srkd in component Ca (uM)"
    legend_constants[64] = "bmem in component Ca (uM)"
    legend_constants[65] = "kmem in component Ca (uM)"
    legend_constants[66] = "bsar in component Ca (uM)"
    legend_constants[67] = "ksar in component Ca (uM)"
    legend_algebraic[74] = "bpxs in component Ca (dimensionless)"
    legend_algebraic[75] = "spxs in component Ca (dimensionless)"
    legend_algebraic[76] = "mempxs in component Ca (dimensionless)"
    legend_algebraic[77] = "sarpxs in component Ca (dimensionless)"
    legend_algebraic[78] = "dcsib in component Ca (dimensionless)"
    legend_algebraic[79] = "bpxi in component Ca (dimensionless)"
    legend_algebraic[80] = "spxi in component Ca (dimensionless)"
    legend_algebraic[81] = "mempxi in component Ca (dimensionless)"
    legend_algebraic[82] = "sarpxi in component Ca (dimensionless)"
    legend_algebraic[83] = "dciib in component Ca (dimensionless)"
    legend_constants[68] = "xkon in component Ca (per_uM_per_ms)"
    legend_constants[69] = "xkoff in component Ca (per_ms)"
    legend_constants[70] = "btrop in component Ca (uM)"
    legend_algebraic[86] = "xbi in component Ca (uM_per_ms)"
    legend_algebraic[85] = "xbs in component Ca (uM_per_ms)"
    legend_states[24] = "tropi in component Ca (uM)"
    legend_states[25] = "trops in component Ca (uM)"
    legend_constants[71] = "taud in component Ca (ms)"
    legend_constants[72] = "taups in component Ca (ms)"
    legend_algebraic[84] = "jd in component Ca (uM_per_ms)"
    legend_constants[73] = "K_i in component reversal_potentials (mM)"
    legend_constants[74] = "prNaK in component reversal_potentials (dimensionless)"
    legend_rates[0] = "d/dt V in component cell (mV)"
    legend_rates[2] = "d/dt xh in component INa (dimensionless)"
    legend_rates[3] = "d/dt xj in component INa (dimensionless)"
    legend_rates[1] = "d/dt xm in component INa (dimensionless)"
    legend_rates[5] = "d/dt c1 in component ICaL (dimensionless)"
    legend_rates[6] = "d/dt c2 in component ICaL (dimensionless)"
    legend_rates[7] = "d/dt xi1ca in component ICaL (dimensionless)"
    legend_rates[8] = "d/dt xi1ba in component ICaL (dimensionless)"
    legend_rates[9] = "d/dt xi2ca in component ICaL (dimensionless)"
    legend_rates[10] = "d/dt xi2ba in component ICaL (dimensionless)"
    legend_rates[11] = "d/dt xr in component IKr (dimensionless)"
    legend_rates[13] = "d/dt xs1 in component IKs (dimensionless)"
    legend_rates[14] = "d/dt xs2 in component IKs (dimensionless)"
    legend_rates[15] = "d/dt xtos in component Ito (dimensionless)"
    legend_rates[16] = "d/dt ytos in component Ito (dimensionless)"
    legend_rates[17] = "d/dt xtof in component Ito (dimensionless)"
    legend_rates[18] = "d/dt ytof in component Ito (dimensionless)"
    legend_rates[22] = "d/dt Ca_JSR in component Irel (uM)"
    legend_rates[23] = "d/dt xir in component Irel (uM_per_ms)"
    legend_rates[19] = "d/dt Na_i in component Na (mM)"
    legend_rates[4] = "d/dt Ca_dyad in component Ca (uM)"
    legend_rates[20] = "d/dt Ca_submem in component Ca (uM)"
    legend_rates[12] = "d/dt Ca_i in component Ca (uM)"
    legend_rates[21] = "d/dt Ca_NSR in component Ca (uM)"
    legend_rates[24] = "d/dt tropi in component Ca (uM)"
    legend_rates[25] = "d/dt trops in component Ca (uM)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    constants[0] = 8.314472
    constants[1] = 308
    constants[2] = 96.4853415
    constants[3] = 5.4
    constants[4] = 1.8
    constants[5] = 136
    states[0] = -87.169816169406
    constants[6] = 8
    constants[7] = 0
    constants[8] = 400
    constants[9] = 3
    constants[10] = -15
    states[1] = 0.001075453357
    states[2] = 0.990691306716
    states[3] = 0.993888937283
    constants[11] = 12
    states[4] = 1.716573130685
    states[5] = 0.000018211252
    states[6] = 0.979322592773
    states[7] = 0.001208153482
    states[8] = 0.000033616596
    states[9] = 0.004173008466
    states[10] = 0.015242594688
    constants[12] = 182
    constants[13] = 0.00054
    constants[14] = 0
    constants[15] = 8
    constants[16] = -40
    constants[17] = 3
    constants[18] = -40
    constants[19] = 4
    constants[20] = -40
    constants[21] = 11.32
    constants[22] = 3
    constants[23] = 6.09365
    constants[24] = 1.03615e-4
    constants[25] = 0.00413
    constants[26] = 0.00224
    constants[27] = 0.3
    constants[28] = 3
    constants[29] = 0.00195
    constants[30] = 78.0329
    constants[31] = 1
    constants[32] = 3
    constants[33] = 0.3
    states[11] = 0.007074239331
    constants[34] = 0.0125
    states[12] = 0.256752008084
    constants[35] = 0.1386
    states[13] = 0.048267587131
    states[14] = 0.105468807033
    states[15] = 0.00364776906
    states[16] = 0.174403618112
    states[17] = 0.003643592594
    states[18] = 0.993331326442
    constants[36] = 0.04
    constants[37] = 0.11
    states[19] = 11.441712311614
    constants[38] = 1.5
    constants[39] = 1.5
    constants[40] = 12
    states[20] = 0.226941113355
    constants[41] = 0.84
    constants[42] = 0.3
    constants[43] = 1.3
    constants[44] = 87.5
    constants[45] = 12.3
    constants[46] = 0.0036
    states[21] = 104.450004990523
    constants[47] = 90
    states[22] = 97.505463697266
    constants[48] = 2.58079
    constants[49] = 26841.8
    constants[50] = 9000
    constants[51] = 0.3576
    constants[52] = 0.05
    constants[53] = 11.3
    constants[54] = 100
    constants[55] = 30
    states[23] = 0.006679257264
    constants[56] = 0.5
    constants[57] = 50
    constants[58] = 0.4
    constants[59] = 0.00002069
    constants[60] = 24
    constants[61] = 7
    constants[62] = 47
    constants[63] = 0.6
    constants[64] = 15
    constants[65] = 0.3
    constants[66] = 42
    constants[67] = 13
    constants[68] = 0.0327
    constants[69] = 0.0196
    constants[70] = 70
    states[24] = 22.171689894953
    states[25] = 19.864701949854
    constants[71] = 4
    constants[72] = 0.5
    constants[73] = 140
    constants[74] = 0.01833
    constants[75] = constants[2]/(constants[0]*constants[1])
    constants[76] = (((constants[29]*constants[27])/constants[28])*constants[26])/constants[25]
    constants[77] = (exp(constants[5]/67.3000)-1.00000)/7.00000
    constants[78] = (1.00000-constants[53])*constants[47]-50.0000
    constants[79] = (1.00000/constants[75])*log(constants[3]/constants[73])
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[22] = (states[21]-states[22])/constants[54]
    algebraic[1] = custom_piecewise([less(states[0] , -40.0000), 0.135000*exp((80.0000+states[0])/-6.80000) , True, 0.00000])
    algebraic[8] = custom_piecewise([less(states[0] , -40.0000), 3.56000*exp(0.0790000*states[0])+310000.*exp(0.350000*states[0]) , True, 1.00000/(0.130000*(1.00000+exp((states[0]+10.6600)/-11.1000)))])
    rates[2] = algebraic[1]*(1.00000-states[2])-algebraic[8]*states[2]
    algebraic[2] = custom_piecewise([less(states[0] , -40.0000), ((-127140.*exp(0.244400*states[0])-3.47400e-05*exp(-0.0439100*states[0]))*1.00000*(states[0]+37.7800))/(1.00000+exp(0.311000*(states[0]+79.2300))) , True, 0.00000])
    algebraic[9] = custom_piecewise([less(states[0] , -40.0000), (0.121200*exp(-0.0105200*states[0]))/(1.00000+exp(-0.137800*(states[0]+40.1400))) , True, (0.300000*exp(-2.53500e-07*states[0]))/(1.00000+exp(-0.100000*(states[0]+32.0000)))])
    rates[3] = algebraic[2]*(1.00000-states[3])-algebraic[9]*states[3]
    algebraic[0] = custom_piecewise([greater(fabs(states[0]+47.1300) , 0.00100000), (0.320000*1.00000*(states[0]+47.1300))/(1.00000-exp(-0.100000*(states[0]+47.1300))) , True, 3.20000])
    algebraic[7] = 0.0800000*exp(-states[0]/11.0000)
    rates[1] = algebraic[0]*(1.00000-states[1])-algebraic[7]*states[1]
    algebraic[5] = 1.00000/(1.00000+exp(-(states[0]-1.50000)/16.7000))
    algebraic[16] = custom_piecewise([less(fabs(states[0]+30.0000) , 0.00100000/0.0687000), 1.00000/(7.19000e-05/0.148000+0.000131000/0.0687000) , True, 1.00000/((7.19000e-05*(states[0]+30.0000))/(1.00000-exp(-0.148000*(states[0]+30.0000)))+(0.000131000*(states[0]+30.0000))/(exp(0.0687000*(states[0]+30.0000))-1.00000))])
    rates[13] = (algebraic[5]-states[13])/algebraic[16]
    algebraic[4] = custom_piecewise([greater(fabs(states[0]+7.00000) , 0.00100000), (0.00138000*1.00000*(states[0]+7.00000))/(1.00000-exp(-0.123000*(states[0]+7.00000))) , True, 0.00138000/0.123000])
    algebraic[11] = custom_piecewise([greater(fabs(states[0]+10.0000) , 0.00100000), (0.000610000*1.00000*(states[0]+10.0000))/(exp(0.145000*(states[0]+10.0000))-1.00000) , True, 0.000610000/0.145000])
    algebraic[15] = 1.00000/(algebraic[4]+algebraic[11])
    algebraic[19] = 1.00000/(1.00000+exp(-(states[0]+50.0000)/7.50000))
    rates[11] = (algebraic[19]-states[11])/algebraic[15]
    algebraic[12] = algebraic[5]
    algebraic[20] = 4.00000*algebraic[16]
    rates[14] = (algebraic[12]-states[14])/algebraic[20]
    algebraic[6] = -(states[0]+3.00000)/15.0000
    algebraic[17] = 1.00000/(1.00000+exp(algebraic[6]))
    algebraic[22] = 9.00000/(1.00000+exp(-algebraic[6]))+0.500000
    rates[15] = (algebraic[17]-states[15])/algebraic[22]
    algebraic[21] = algebraic[17]
    algebraic[13] = ((-states[0]/30.0000)*states[0])/30.0000
    algebraic[24] = 3.50000*exp(algebraic[13])+1.50000
    rates[17] = (algebraic[21]-states[17])/algebraic[24]
    algebraic[18] = 1.00000/(1.00000+exp(-(states[0]-constants[14])/constants[15]))
    algebraic[23] = algebraic[18]/constants[31]
    algebraic[25] = (1.00000-algebraic[18])/constants[31]
    algebraic[26] = 1.00000/(1.00000+power(constants[22]/states[4], 3.00000))
    algebraic[34] = 10.0000+4954.00*exp(states[0]/15.6000)
    algebraic[35] = constants[30]/(1.00000+power(states[4]/constants[23], 4.00000))+0.100000
    algebraic[33] = 1.00000-1.00000/(1.00000+exp(-(states[0]-constants[18])/constants[19]))
    algebraic[36] = (algebraic[34]-algebraic[35])*algebraic[33]+algebraic[35]
    algebraic[38] = 1.00000/(1.00000+exp(-(states[0]-constants[20])/constants[21]))
    algebraic[39] = (algebraic[26]*algebraic[38])/algebraic[36]
    algebraic[40] = (1.00000-algebraic[38])/algebraic[36]
    algebraic[37] = (algebraic[34]-450.000)*algebraic[33]+450.000
    algebraic[41] = algebraic[38]/algebraic[37]
    algebraic[42] = (1.00000-algebraic[38])/algebraic[37]
    rates[6] = (algebraic[25]*states[5]+algebraic[40]*states[9]+algebraic[42]*states[10])-(algebraic[39]+algebraic[41]+algebraic[23])*states[6]
    algebraic[30] = 1.00000/(1.00000+exp(-(states[0]-constants[16])/constants[17]))
    algebraic[31] = (1.00000-algebraic[30])/constants[32]
    algebraic[28] = 0.0241680*algebraic[26]
    algebraic[43] = (((((algebraic[31]*algebraic[23])/algebraic[25])*algebraic[28])/constants[24])*algebraic[40])/algebraic[39]
    rates[9] = (algebraic[31]*states[7]+algebraic[39]*states[6])-(algebraic[40]+algebraic[43])*states[9]
    algebraic[32] = algebraic[31]
    algebraic[44] = (((((algebraic[32]*algebraic[23])/algebraic[25])*constants[25])/constants[26])*algebraic[42])/algebraic[41]
    rates[10] = (algebraic[32]*states[8]+algebraic[41]*states[6])-(algebraic[42]+algebraic[44])*states[10]
    algebraic[45] = (((((1.00000-states[7])-states[9])-states[8])-states[10])-states[5])-states[6]
    rates[5] = (algebraic[23]*states[6]+constants[24]*states[7]+constants[26]*states[8]+constants[28]*algebraic[45])-(algebraic[25]+constants[27]+constants[25]+algebraic[28])*states[5]
    algebraic[27] = 0.0182688*algebraic[26]
    algebraic[29] = (((algebraic[27]*constants[27])/constants[28])*constants[24])/algebraic[28]
    rates[7] = (algebraic[28]*states[5]+algebraic[43]*states[9]+algebraic[27]*algebraic[45])-(algebraic[31]+constants[24]+algebraic[29])*states[7]
    rates[8] = (constants[25]*states[5]+algebraic[44]*states[10]+constants[29]*algebraic[45])-(algebraic[32]+constants[26]+constants[76])*states[8]
    algebraic[53] = (states[0]+33.5000)/10.0000
    algebraic[59] = 1.00000/(1.00000+exp(algebraic[53]))
    algebraic[55] = (states[0]+60.0000)/10.0000
    algebraic[62] = 3000.00/(1.00000+exp(algebraic[55]))+30.0000
    rates[16] = (algebraic[59]-states[16])/algebraic[62]
    algebraic[61] = algebraic[59]
    algebraic[57] = (states[0]+33.5000)/10.0000
    algebraic[64] = 20.0000/(1.00000+exp(algebraic[57]))+20.0000
    rates[18] = (algebraic[61]-states[18])/algebraic[64]
    algebraic[72] = (constants[58]*states[12]*states[12])/(states[12]*states[12]+constants[56]*constants[56])
    algebraic[73] = ((constants[59]*states[21]*states[21])/(states[21]*states[21]+constants[57]*constants[57]))*(states[21]*16.6670-states[12])
    algebraic[79] = (constants[60]*constants[61])/((constants[61]+states[12])*(constants[61]+states[12]))
    algebraic[80] = (constants[62]*constants[63])/((constants[63]+states[12])*(constants[63]+states[12]))
    algebraic[81] = (constants[64]*constants[65])/((constants[65]+states[12])*(constants[65]+states[12]))
    algebraic[82] = (constants[66]*constants[67])/((constants[67]+states[12])*(constants[67]+states[12]))
    algebraic[83] = 1.00000/(1.00000+algebraic[79]+algebraic[80]+algebraic[81]+algebraic[82])
    algebraic[86] = constants[68]*states[12]*(constants[70]-states[24])-constants[69]*states[24]
    algebraic[84] = (states[20]-states[12])/constants[71]
    rates[12] = algebraic[83]*(((algebraic[84]-algebraic[72])+algebraic[73])-algebraic[86])
    rates[24] = algebraic[86]
    algebraic[85] = constants[68]*states[20]*(constants[70]-states[25])-constants[69]*states[25]
    rates[25] = algebraic[85]
    algebraic[87] = (-states[23]+algebraic[72])-algebraic[73]
    rates[21] = algebraic[87]
    algebraic[69] = custom_piecewise([greater(states[22] , 50.0000) & less(states[22] , constants[47]), (states[22]-50.0000)/1.00000 , greater_equal(states[22] , constants[47]), constants[53]*states[22]+constants[78] , True, 0.00000])
    algebraic[70] = (states[21]*algebraic[69])/constants[47]
    algebraic[88] = states[20]/1000.00
    algebraic[14] = states[0]*2.00000*constants[75]
    algebraic[89] = custom_piecewise([less(fabs(algebraic[14]) , 0.00100000), (4.00000*constants[13]*constants[2]*constants[75]*(algebraic[88]*exp(algebraic[14])-0.341000*constants[4]))/(2.00000*constants[75]) , True, (4.00000*constants[13]*states[0]*constants[2]*constants[75]*(algebraic[88]*exp(algebraic[14])-0.341000*constants[4]))/(exp(algebraic[14])-1.00000)])
    algebraic[71] = exp(-constants[52]*(states[0]+30.0000))/(1.00000+exp(-constants[52]*(states[0]+30.0000)))
    algebraic[91] = (constants[48]/1.00000)*algebraic[45]*fabs(algebraic[89])*algebraic[71]
    rates[23] = algebraic[91]*algebraic[70]-(states[23]*(1.00000-(constants[55]*algebraic[87])/states[21]))/constants[55]
    algebraic[92] = (((algebraic[45]*algebraic[70]*fabs(algebraic[89])*constants[49])/1.00000)*exp(-constants[51]*(states[0]+30.0000)))/(1.00000+exp(-constants[51]*(states[0]+30.0000)))
    algebraic[94] = algebraic[45]*constants[50]*fabs(algebraic[89])
    algebraic[96] = algebraic[92]+algebraic[94]
    rates[4] = algebraic[96]-(states[4]-states[20])/constants[72]
    algebraic[90] = constants[12]*algebraic[45]*algebraic[89]
    algebraic[67] = 1.00000/(1.00000+power(constants[42]/states[20], 3.00000))
    algebraic[95] = (power(states[19], 3.00000))*constants[4]*exp(states[0]*0.350000*constants[75])-(power(constants[5], 3.00000))*algebraic[88]*exp(states[0]*(0.350000-1.00000)*constants[75])
    algebraic[66] = 1.00000+0.200000*exp(states[0]*(0.350000-1.00000)*constants[75])
    algebraic[97] = constants[43]*(power(states[19], 3.00000))+(power(constants[44], 3.00000))*algebraic[88]
    algebraic[98] = (power(constants[45], 3.00000))*constants[4]*(1.00000+algebraic[88]/constants[46])
    algebraic[68] = constants[46]*(power(constants[5], 3.00000))*(1.00000+power(states[19]/constants[45], 3.00000))
    algebraic[99] = (power(states[19], 3.00000))*constants[4]+(power(constants[5], 3.00000))*algebraic[88]
    algebraic[100] = algebraic[97]+algebraic[98]+algebraic[68]+algebraic[99]
    algebraic[101] = (constants[41]*algebraic[67]*algebraic[95])/(algebraic[66]*algebraic[100])
    algebraic[74] = (constants[60]*constants[61])/((constants[61]+states[20])*(constants[61]+states[20]))
    algebraic[75] = (constants[62]*constants[63])/((constants[63]+states[20])*(constants[63]+states[20]))
    algebraic[76] = (constants[64]*constants[65])/((constants[65]+states[20])*(constants[65]+states[20]))
    algebraic[77] = (constants[66]*constants[67])/((constants[67]+states[20])*(constants[67]+states[20]))
    algebraic[78] = 1.00000/(1.00000+algebraic[74]+algebraic[75]+algebraic[76]+algebraic[77])
    rates[20] = algebraic[78]*(50.0000*(((states[23]-algebraic[84])-algebraic[90])+algebraic[101])-algebraic[85])
    algebraic[63] = 1.00000/(1.00000+0.124500*exp(-0.100000*states[0]*constants[75])+0.0365000*constants[77]*exp(-states[0]*constants[75]))
    algebraic[65] = (((constants[38]*algebraic[63]*states[19])/(states[19]+constants[40]))*constants[3])/(constants[3]+constants[39])
    algebraic[102] = constants[6]*algebraic[101]
    algebraic[105] = (1.00000/constants[75])*log(constants[5]/states[19])
    algebraic[106] = constants[11]*states[2]*states[3]*states[1]*states[1]*states[1]*(states[0]-algebraic[105])
    rates[19] = -(algebraic[106]+3.00000*algebraic[65]+3.00000*algebraic[102])/(constants[6]*1000.00)
    algebraic[46] = 1.02000/(1.00000+exp(0.238500*((states[0]-constants[79])-59.2150)))
    algebraic[47] = (0.491240*exp(0.0803200*((states[0]-constants[79])+5.47600))+1.00000*exp(0.0617500*((states[0]-constants[79])-594.310)))/(1.00000+exp(-0.514300*((states[0]-constants[79])+4.75300)))
    algebraic[48] = algebraic[46]/(algebraic[46]+algebraic[47])
    algebraic[49] = constants[33]*(power(constants[3]/5.40000, 1.0/2))*algebraic[48]*(states[0]-constants[79])
    algebraic[54] = 1.00000/(1.00000+exp(algebraic[53]))
    algebraic[56] = constants[36]*states[15]*(states[16]+0.500000*algebraic[54])*(states[0]-constants[79])
    algebraic[58] = constants[37]*states[17]*states[18]*(states[0]-constants[79])
    algebraic[60] = algebraic[56]+algebraic[58]
    algebraic[93] = 2.00000*constants[6]*algebraic[90]
    algebraic[50] = 1.00000/(1.00000+exp((states[0]+33.0000)/22.4000))
    algebraic[51] = constants[34]*(power(constants[3]/5.40000, 1.0/2))*states[11]*algebraic[50]*(states[0]-constants[79])
    algebraic[103] = (1.00000/constants[75])*log((constants[3]+constants[74]*constants[5])/(constants[73]+constants[74]*states[19]))
    algebraic[52] = 1.00000+0.800000/(1.00000+power(0.500000/states[12], 3.00000))
    algebraic[104] = constants[35]*algebraic[52]*states[13]*states[14]*(states[0]-algebraic[103])
    algebraic[3] = floor(voi/constants[8])*constants[8]
    algebraic[10] = custom_piecewise([greater_equal(voi-algebraic[3] , constants[7]) & less_equal(voi-algebraic[3] , constants[7]+constants[9]), constants[10] , True, 0.00000])
    algebraic[107] = -(algebraic[106]+algebraic[49]+algebraic[51]+algebraic[104]+algebraic[60]+algebraic[102]+algebraic[93]+algebraic[65]+algebraic[10])
    rates[0] = algebraic[107]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[1] = custom_piecewise([less(states[0] , -40.0000), 0.135000*exp((80.0000+states[0])/-6.80000) , True, 0.00000])
    algebraic[8] = custom_piecewise([less(states[0] , -40.0000), 3.56000*exp(0.0790000*states[0])+310000.*exp(0.350000*states[0]) , True, 1.00000/(0.130000*(1.00000+exp((states[0]+10.6600)/-11.1000)))])
    algebraic[2] = custom_piecewise([less(states[0] , -40.0000), ((-127140.*exp(0.244400*states[0])-3.47400e-05*exp(-0.0439100*states[0]))*1.00000*(states[0]+37.7800))/(1.00000+exp(0.311000*(states[0]+79.2300))) , True, 0.00000])
    algebraic[9] = custom_piecewise([less(states[0] , -40.0000), (0.121200*exp(-0.0105200*states[0]))/(1.00000+exp(-0.137800*(states[0]+40.1400))) , True, (0.300000*exp(-2.53500e-07*states[0]))/(1.00000+exp(-0.100000*(states[0]+32.0000)))])
    algebraic[0] = custom_piecewise([greater(fabs(states[0]+47.1300) , 0.00100000), (0.320000*1.00000*(states[0]+47.1300))/(1.00000-exp(-0.100000*(states[0]+47.1300))) , True, 3.20000])
    algebraic[7] = 0.0800000*exp(-states[0]/11.0000)
    algebraic[5] = 1.00000/(1.00000+exp(-(states[0]-1.50000)/16.7000))
    algebraic[16] = custom_piecewise([less(fabs(states[0]+30.0000) , 0.00100000/0.0687000), 1.00000/(7.19000e-05/0.148000+0.000131000/0.0687000) , True, 1.00000/((7.19000e-05*(states[0]+30.0000))/(1.00000-exp(-0.148000*(states[0]+30.0000)))+(0.000131000*(states[0]+30.0000))/(exp(0.0687000*(states[0]+30.0000))-1.00000))])
    algebraic[4] = custom_piecewise([greater(fabs(states[0]+7.00000) , 0.00100000), (0.00138000*1.00000*(states[0]+7.00000))/(1.00000-exp(-0.123000*(states[0]+7.00000))) , True, 0.00138000/0.123000])
    algebraic[11] = custom_piecewise([greater(fabs(states[0]+10.0000) , 0.00100000), (0.000610000*1.00000*(states[0]+10.0000))/(exp(0.145000*(states[0]+10.0000))-1.00000) , True, 0.000610000/0.145000])
    algebraic[15] = 1.00000/(algebraic[4]+algebraic[11])
    algebraic[19] = 1.00000/(1.00000+exp(-(states[0]+50.0000)/7.50000))
    algebraic[12] = algebraic[5]
    algebraic[20] = 4.00000*algebraic[16]
    algebraic[6] = -(states[0]+3.00000)/15.0000
    algebraic[17] = 1.00000/(1.00000+exp(algebraic[6]))
    algebraic[22] = 9.00000/(1.00000+exp(-algebraic[6]))+0.500000
    algebraic[21] = algebraic[17]
    algebraic[13] = ((-states[0]/30.0000)*states[0])/30.0000
    algebraic[24] = 3.50000*exp(algebraic[13])+1.50000
    algebraic[18] = 1.00000/(1.00000+exp(-(states[0]-constants[14])/constants[15]))
    algebraic[23] = algebraic[18]/constants[31]
    algebraic[25] = (1.00000-algebraic[18])/constants[31]
    algebraic[26] = 1.00000/(1.00000+power(constants[22]/states[4], 3.00000))
    algebraic[34] = 10.0000+4954.00*exp(states[0]/15.6000)
    algebraic[35] = constants[30]/(1.00000+power(states[4]/constants[23], 4.00000))+0.100000
    algebraic[33] = 1.00000-1.00000/(1.00000+exp(-(states[0]-constants[18])/constants[19]))
    algebraic[36] = (algebraic[34]-algebraic[35])*algebraic[33]+algebraic[35]
    algebraic[38] = 1.00000/(1.00000+exp(-(states[0]-constants[20])/constants[21]))
    algebraic[39] = (algebraic[26]*algebraic[38])/algebraic[36]
    algebraic[40] = (1.00000-algebraic[38])/algebraic[36]
    algebraic[37] = (algebraic[34]-450.000)*algebraic[33]+450.000
    algebraic[41] = algebraic[38]/algebraic[37]
    algebraic[42] = (1.00000-algebraic[38])/algebraic[37]
    algebraic[30] = 1.00000/(1.00000+exp(-(states[0]-constants[16])/constants[17]))
    algebraic[31] = (1.00000-algebraic[30])/constants[32]
    algebraic[28] = 0.0241680*algebraic[26]
    algebraic[43] = (((((algebraic[31]*algebraic[23])/algebraic[25])*algebraic[28])/constants[24])*algebraic[40])/algebraic[39]
    algebraic[32] = algebraic[31]
    algebraic[44] = (((((algebraic[32]*algebraic[23])/algebraic[25])*constants[25])/constants[26])*algebraic[42])/algebraic[41]
    algebraic[45] = (((((1.00000-states[7])-states[9])-states[8])-states[10])-states[5])-states[6]
    algebraic[27] = 0.0182688*algebraic[26]
    algebraic[29] = (((algebraic[27]*constants[27])/constants[28])*constants[24])/algebraic[28]
    algebraic[53] = (states[0]+33.5000)/10.0000
    algebraic[59] = 1.00000/(1.00000+exp(algebraic[53]))
    algebraic[55] = (states[0]+60.0000)/10.0000
    algebraic[62] = 3000.00/(1.00000+exp(algebraic[55]))+30.0000
    algebraic[61] = algebraic[59]
    algebraic[57] = (states[0]+33.5000)/10.0000
    algebraic[64] = 20.0000/(1.00000+exp(algebraic[57]))+20.0000
    algebraic[72] = (constants[58]*states[12]*states[12])/(states[12]*states[12]+constants[56]*constants[56])
    algebraic[73] = ((constants[59]*states[21]*states[21])/(states[21]*states[21]+constants[57]*constants[57]))*(states[21]*16.6670-states[12])
    algebraic[79] = (constants[60]*constants[61])/((constants[61]+states[12])*(constants[61]+states[12]))
    algebraic[80] = (constants[62]*constants[63])/((constants[63]+states[12])*(constants[63]+states[12]))
    algebraic[81] = (constants[64]*constants[65])/((constants[65]+states[12])*(constants[65]+states[12]))
    algebraic[82] = (constants[66]*constants[67])/((constants[67]+states[12])*(constants[67]+states[12]))
    algebraic[83] = 1.00000/(1.00000+algebraic[79]+algebraic[80]+algebraic[81]+algebraic[82])
    algebraic[86] = constants[68]*states[12]*(constants[70]-states[24])-constants[69]*states[24]
    algebraic[84] = (states[20]-states[12])/constants[71]
    algebraic[85] = constants[68]*states[20]*(constants[70]-states[25])-constants[69]*states[25]
    algebraic[87] = (-states[23]+algebraic[72])-algebraic[73]
    algebraic[69] = custom_piecewise([greater(states[22] , 50.0000) & less(states[22] , constants[47]), (states[22]-50.0000)/1.00000 , greater_equal(states[22] , constants[47]), constants[53]*states[22]+constants[78] , True, 0.00000])
    algebraic[70] = (states[21]*algebraic[69])/constants[47]
    algebraic[88] = states[20]/1000.00
    algebraic[14] = states[0]*2.00000*constants[75]
    algebraic[89] = custom_piecewise([less(fabs(algebraic[14]) , 0.00100000), (4.00000*constants[13]*constants[2]*constants[75]*(algebraic[88]*exp(algebraic[14])-0.341000*constants[4]))/(2.00000*constants[75]) , True, (4.00000*constants[13]*states[0]*constants[2]*constants[75]*(algebraic[88]*exp(algebraic[14])-0.341000*constants[4]))/(exp(algebraic[14])-1.00000)])
    algebraic[71] = exp(-constants[52]*(states[0]+30.0000))/(1.00000+exp(-constants[52]*(states[0]+30.0000)))
    algebraic[91] = (constants[48]/1.00000)*algebraic[45]*fabs(algebraic[89])*algebraic[71]
    algebraic[92] = (((algebraic[45]*algebraic[70]*fabs(algebraic[89])*constants[49])/1.00000)*exp(-constants[51]*(states[0]+30.0000)))/(1.00000+exp(-constants[51]*(states[0]+30.0000)))
    algebraic[94] = algebraic[45]*constants[50]*fabs(algebraic[89])
    algebraic[96] = algebraic[92]+algebraic[94]
    algebraic[90] = constants[12]*algebraic[45]*algebraic[89]
    algebraic[67] = 1.00000/(1.00000+power(constants[42]/states[20], 3.00000))
    algebraic[95] = (power(states[19], 3.00000))*constants[4]*exp(states[0]*0.350000*constants[75])-(power(constants[5], 3.00000))*algebraic[88]*exp(states[0]*(0.350000-1.00000)*constants[75])
    algebraic[66] = 1.00000+0.200000*exp(states[0]*(0.350000-1.00000)*constants[75])
    algebraic[97] = constants[43]*(power(states[19], 3.00000))+(power(constants[44], 3.00000))*algebraic[88]
    algebraic[98] = (power(constants[45], 3.00000))*constants[4]*(1.00000+algebraic[88]/constants[46])
    algebraic[68] = constants[46]*(power(constants[5], 3.00000))*(1.00000+power(states[19]/constants[45], 3.00000))
    algebraic[99] = (power(states[19], 3.00000))*constants[4]+(power(constants[5], 3.00000))*algebraic[88]
    algebraic[100] = algebraic[97]+algebraic[98]+algebraic[68]+algebraic[99]
    algebraic[101] = (constants[41]*algebraic[67]*algebraic[95])/(algebraic[66]*algebraic[100])
    algebraic[74] = (constants[60]*constants[61])/((constants[61]+states[20])*(constants[61]+states[20]))
    algebraic[75] = (constants[62]*constants[63])/((constants[63]+states[20])*(constants[63]+states[20]))
    algebraic[76] = (constants[64]*constants[65])/((constants[65]+states[20])*(constants[65]+states[20]))
    algebraic[77] = (constants[66]*constants[67])/((constants[67]+states[20])*(constants[67]+states[20]))
    algebraic[78] = 1.00000/(1.00000+algebraic[74]+algebraic[75]+algebraic[76]+algebraic[77])
    algebraic[63] = 1.00000/(1.00000+0.124500*exp(-0.100000*states[0]*constants[75])+0.0365000*constants[77]*exp(-states[0]*constants[75]))
    algebraic[65] = (((constants[38]*algebraic[63]*states[19])/(states[19]+constants[40]))*constants[3])/(constants[3]+constants[39])
    algebraic[102] = constants[6]*algebraic[101]
    algebraic[105] = (1.00000/constants[75])*log(constants[5]/states[19])
    algebraic[106] = constants[11]*states[2]*states[3]*states[1]*states[1]*states[1]*(states[0]-algebraic[105])
    algebraic[46] = 1.02000/(1.00000+exp(0.238500*((states[0]-constants[79])-59.2150)))
    algebraic[47] = (0.491240*exp(0.0803200*((states[0]-constants[79])+5.47600))+1.00000*exp(0.0617500*((states[0]-constants[79])-594.310)))/(1.00000+exp(-0.514300*((states[0]-constants[79])+4.75300)))
    algebraic[48] = algebraic[46]/(algebraic[46]+algebraic[47])
    algebraic[49] = constants[33]*(power(constants[3]/5.40000, 1.0/2))*algebraic[48]*(states[0]-constants[79])
    algebraic[54] = 1.00000/(1.00000+exp(algebraic[53]))
    algebraic[56] = constants[36]*states[15]*(states[16]+0.500000*algebraic[54])*(states[0]-constants[79])
    algebraic[58] = constants[37]*states[17]*states[18]*(states[0]-constants[79])
    algebraic[60] = algebraic[56]+algebraic[58]
    algebraic[93] = 2.00000*constants[6]*algebraic[90]
    algebraic[50] = 1.00000/(1.00000+exp((states[0]+33.0000)/22.4000))
    algebraic[51] = constants[34]*(power(constants[3]/5.40000, 1.0/2))*states[11]*algebraic[50]*(states[0]-constants[79])
    algebraic[103] = (1.00000/constants[75])*log((constants[3]+constants[74]*constants[5])/(constants[73]+constants[74]*states[19]))
    algebraic[52] = 1.00000+0.800000/(1.00000+power(0.500000/states[12], 3.00000))
    algebraic[104] = constants[35]*algebraic[52]*states[13]*states[14]*(states[0]-algebraic[103])
    algebraic[3] = floor(voi/constants[8])*constants[8]
    algebraic[10] = custom_piecewise([greater_equal(voi-algebraic[3] , constants[7]) & less_equal(voi-algebraic[3] , constants[7]+constants[9]), constants[10] , True, 0.00000])
    algebraic[107] = -(algebraic[106]+algebraic[49]+algebraic[51]+algebraic[104]+algebraic[60]+algebraic[102]+algebraic[93]+algebraic[65]+algebraic[10])
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
        self.R = 8.314472
        self.T = 308
        self.F = 96.4853415
        self.K_o = 5.4
        self.Ca_o = 1.8
        self.Na_o = 136
        self.wca = 8
        self.stim_offset = 0
        self.stim_period = 400
        self.stim_duration = 3
        self.stim_amplitude = -15
        self.gna = 12
        self.gca = 182
        self.pca = 0.00054
        self.vth = 0
        self.s6 = 8
        self.vx = -40
        self.sx = 3
        self.vy = -40
        self.sy = 4
        self.vyr = -40
        self.syr = 11.32
        self.cat = 3
        self.cpt = 6.09365
        self.k2 = 1.03615e-4
        self.k1t = 0.00413
        self.k2t = 0.00224
        self.r1 = 0.3
        self.r2 = 3
        self.s1t = 0.00195
        self.tca = 78.0329
        self.taupo = 1
        self.tau3 = 3
        self.gkix = 0.3
        self.gkr = 0.0125
        self.gks = 0.1386
        self.gtos = 0.04
        self.gtof = 0.11
        self.gNaK = 1.5
        self.xkmko = 1.5
        self.xkmnai = 12
        self.gNaCa = 0.84
        self.xkdna = 0.3
        self.xmcao = 1.3
        self.xmnao = 87.5
        self.xmnai = 12.3
        self.xmcai = 0.0036
        self.cstar = 90
        self.gryr = 2.58079
        self.gbarsr = 26841.8
        self.gdyad = 9000
        self.ax = 0.3576
        self.ay = 0.05
        self.av = 11.3
        self.taua = 100
        self.taur = 30
        self.cup = 0.5
        self.kj = 50
        self.vup = 0.4
        self.gleak = 0.00002069
        self.bcal = 24
        self.xkcal = 7
        self.srmax = 47
        self.srkd = 0.6
        self.bmem = 15
        self.kmem = 0.3
        self.bsar = 42
        self.ksar = 13
        self.xkon = 0.0327
        self.xkoff = 0.0196
        self.btrop = 70
        self.taud = 4
        self.taups = 0.5
        self.K_i = 140
        self.prNaK = 0.01833

    def to_dict(self):
        return {
            "R": self.R,
            "T": self.T,
            "F": self.F,
            "K_o": self.K_o,
            "Ca_o": self.Ca_o,
            "Na_o": self.Na_o,
            "wca": self.wca,
            "stim_offset": self.stim_offset,
            "stim_period": self.stim_period,
            "stim_duration": self.stim_duration,
            "stim_amplitude": self.stim_amplitude,
            "gna": self.gna,
            "gca": self.gca,
            "pca": self.pca,
            "vth": self.vth,
            "s6": self.s6,
            "vx": self.vx,
            "sx": self.sx,
            "vy": self.vy,
            "sy": self.sy,
            "vyr": self.vyr,
            "syr": self.syr,
            "cat": self.cat,
            "cpt": self.cpt,
            "k2": self.k2,
            "k1t": self.k1t,
            "k2t": self.k2t,
            "r1": self.r1,
            "r2": self.r2,
            "s1t": self.s1t,
            "tca": self.tca,
            "taupo": self.taupo,
            "tau3": self.tau3,
            "gkix": self.gkix,
            "gkr": self.gkr,
            "gks": self.gks,
            "gtos": self.gtos,
            "gtof": self.gtof,
            "gNaK": self.gNaK,
            "xkmko": self.xkmko,
            "xkmnai": self.xkmnai,
            "gNaCa": self.gNaCa,
            "xkdna": self.xkdna,
            "xmcao": self.xmcao,
            "xmnao": self.xmnao,
            "xmnai": self.xmnai,
            "xmcai": self.xmcai,
            "cstar": self.cstar,
            "gryr": self.gryr,
            "gbarsr": self.gbarsr,
            "gdyad": self.gdyad,
            "ax": self.ax,
            "ay": self.ay,
            "av": self.av,
            "taua": self.taua,
            "taur": self.taur,
            "cup": self.cup,
            "kj": self.kj,
            "vup": self.vup,
            "gleak": self.gleak,
            "bcal": self.bcal,
            "xkcal": self.xkcal,
            "srmax": self.srmax,
            "srkd": self.srkd,
            "bmem": self.bmem,
            "kmem": self.kmem,
            "bsar": self.bsar,
            "ksar": self.ksar,
            "xkon": self.xkon,
            "xkoff": self.xkoff,
            "btrop": self.btrop,
            "taud": self.taud,
            "taups": self.taups,
            "K_i": self.K_i,
            "prNaK": self.prNaK,
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
        y0=[-87.169816169406, 0.001075453357, 0.990691306716, 0.993888937283, 1.716573130685, 0.000018211252, 0.979322592773, 0.001208153482, 0.000033616596, 0.004173008466, 0.015242594688, 0.007074239331, 0.256752008084, 0.048267587131, 0.105468807033, 0.00364776906, 0.174403618112, 0.003643592594, 0.993331326442, 11.441712311614, 0.226941113355, 104.450004990523, 97.505463697266, 0.006679257264, 22.171689894953, 19.864701949854],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "mahajan_shiferaw_sato_baher_olcese_xie_yang_chen_restrepo_karma_garfinkel_qu_weiss_2008"
        self.curve_names = [
            "V",
            "xm",
            "xh",
            "xj",
            "Ca_dyad",
            "c1",
            "c2",
            "xi1ca",
            "xi1ba",
            "xi2ca",
            "xi2ba",
            "xr",
            "Ca_i",
            "xs1",
            "xs2",
            "xtos",
            "ytos",
            "xtof",
            "ytof",
            "Na_i",
            "Ca_submem",
            "Ca_NSR",
            "Ca_JSR",
            "xir",
            "tropi",
            "trops",
        ]
        self.state_names = ['V', 'xm', 'xh', 'xj', 'Ca_dyad', 'c1', 'c2', 'xi1ca', 'xi1ba', 'xi2ca', 'xi2ba', 'xr', 'Ca_i', 'xs1', 'xs2', 'xtos', 'ytos', 'xtof', 'ytof', 'Na_i', 'Ca_submem', 'Ca_NSR', 'Ca_JSR', 'xir', 'tropi', 'trops']
        self.algebraic_names = ['am', 'ah', 'aj', 'past', 'xkrv1', 'xs1ss', 'rt1', 'bm', 'bh', 'bj', 'i_Stim', 'xkrv2', 'xs2ss', 'rt4', 'za', 'taukr', 'tauxs1', 'xtos_inf', 'poinf', 'xkrinf', 'tauxs2', 'xtof_inf', 'txs', 'alpha', 'txf', 'beta', 'fca', 's1', 'k1', 's2', 'poi', 'k3', 'k3t', 'Pr', 'recov', 'tau_ca', 'tauca', 'tauba', 'Ps', 'k6', 'k5', 'k6t', 'k5t', 'k4', 'k4t', 'po', 'aki', 'bki', 'xkin', 'xik1', 'rg', 'xikr', 'gksx', 'rt2', 'rs_inf', 'rt3', 'xitos', 'rt5', 'xitof', 'ytos_inf', 'xito', 'ytof_inf', 'tys', 'fNaK', 'tyf', 'xiNaK', 'zw4', 'aloss', 'yz3', 'Qr0', 'Qr', 'sparkV', 'jup', 'jleak', 'bpxs', 'spxs', 'mempxs', 'sarpxs', 'dcsib', 'bpxi', 'spxi', 'mempxi', 'sarpxi', 'dciib', 'jd', 'xbs', 'xbi', 'dCa_JSR', 'csm', 'rxa', 'jca', 'spark_rate', 'xirp', 'xica', 'xicap', 'zw3', 'xiryr', 'yz1', 'yz2', 'yz4', 'zw8', 'jNaCa', 'xiNaCa', 'eks', 'xiks', 'ena', 'xina', 'Itotal']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 80
        p = self.params

        # direct mapping
        c[0] = p.R
        c[1] = p.T
        c[2] = p.F
        c[3] = p.K_o
        c[4] = p.Ca_o
        c[5] = p.Na_o
        c[6] = p.wca
        c[7] = p.stim_offset
        c[8] = p.stim_period
        c[9] = p.stim_duration
        c[10] = p.stim_amplitude
        c[11] = p.gna
        c[12] = p.gca
        c[13] = p.pca
        c[14] = p.vth
        c[15] = p.s6
        c[16] = p.vx
        c[17] = p.sx
        c[18] = p.vy
        c[19] = p.sy
        c[20] = p.vyr
        c[21] = p.syr
        c[22] = p.cat
        c[23] = p.cpt
        c[24] = p.k2
        c[25] = p.k1t
        c[26] = p.k2t
        c[27] = p.r1
        c[28] = p.r2
        c[29] = p.s1t
        c[30] = p.tca
        c[31] = p.taupo
        c[32] = p.tau3
        c[33] = p.gkix
        c[34] = p.gkr
        c[35] = p.gks
        c[36] = p.gtos
        c[37] = p.gtof
        c[38] = p.gNaK
        c[39] = p.xkmko
        c[40] = p.xkmnai
        c[41] = p.gNaCa
        c[42] = p.xkdna
        c[43] = p.xmcao
        c[44] = p.xmnao
        c[45] = p.xmnai
        c[46] = p.xmcai
        c[47] = p.cstar
        c[48] = p.gryr
        c[49] = p.gbarsr
        c[50] = p.gdyad
        c[51] = p.ax
        c[52] = p.ay
        c[53] = p.av
        c[54] = p.taua
        c[55] = p.taur
        c[56] = p.cup
        c[57] = p.kj
        c[58] = p.vup
        c[59] = p.gleak
        c[60] = p.bcal
        c[61] = p.xkcal
        c[62] = p.srmax
        c[63] = p.srkd
        c[64] = p.bmem
        c[65] = p.kmem
        c[66] = p.bsar
        c[67] = p.ksar
        c[68] = p.xkon
        c[69] = p.xkoff
        c[70] = p.btrop
        c[71] = p.taud
        c[72] = p.taups
        c[73] = p.K_i
        c[74] = p.prNaK

        # derived constants
        c[75] = c[2]/(c[0]*c[1])
        c[76] = (((c[29]*c[27])/c[28])*c[26])/c[25]
        c[77] = (exp(c[5]/67.3000)-1.00000)/7.00000
        c[78] = (1.00000-c[53])*c[47]-50.0000
        c[79] = (1.00000/c[75])*log(c[3]/c[73])

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
