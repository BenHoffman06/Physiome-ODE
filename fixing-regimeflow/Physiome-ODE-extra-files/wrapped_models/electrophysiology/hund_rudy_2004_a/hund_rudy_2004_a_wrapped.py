# Size of variable arrays:
sizeAlgebraic = 92
sizeStates = 29
sizeConstants = 70
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component Environment (ms)"
    legend_constants[0] = "F in component Environment (C_per_mole)"
    legend_constants[1] = "K_o in component Environment (mM)"
    legend_constants[2] = "Ca_o in component Environment (mM)"
    legend_constants[3] = "Na_o in component Environment (mM)"
    legend_constants[4] = "Cl_o in component Environment (mM)"
    legend_constants[5] = "FonRT in component Environment (per_mV)"
    legend_constants[6] = "tissue in component Environment (dimensionless)"
    legend_states[0] = "V in component cell (mV)"
    legend_algebraic[62] = "INa in component INa (uA_per_uF)"
    legend_algebraic[31] = "ICaL in component ICaL (uA_per_uF)"
    legend_algebraic[77] = "IK1 in component IK1 (uA_per_uF)"
    legend_algebraic[83] = "IKp in component IKp (uA_per_uF)"
    legend_algebraic[85] = "IKs in component IKs (uA_per_uF)"
    legend_algebraic[81] = "IKr in component IKr (uA_per_uF)"
    legend_algebraic[49] = "IpCa in component IpCa (uA_per_uF)"
    legend_algebraic[50] = "ICab in component ICab (uA_per_uF)"
    legend_algebraic[48] = "INaCa in component INaCa (uA_per_uF)"
    legend_algebraic[41] = "INaK in component INaK (uA_per_uF)"
    legend_algebraic[82] = "Ito in component Ito (uA_per_uF)"
    legend_algebraic[55] = "Ito2 in component Ito2 (uA_per_uF)"
    legend_algebraic[88] = "IClb in component IClb (uA_per_uF)"
    legend_algebraic[65] = "INal in component INal (uA_per_uF)"
    legend_algebraic[51] = "caiont in component cell (uA_per_uF)"
    legend_algebraic[68] = "naiont in component cell (uA_per_uF)"
    legend_algebraic[86] = "kiont in component cell (uA_per_uF)"
    legend_algebraic[89] = "clont in component cell (uA_per_uF)"
    legend_constants[7] = "l in component cell (cm)"
    legend_constants[8] = "a in component cell (cm)"
    legend_constants[57] = "vcell in component cell (uL)"
    legend_constants[61] = "ageo in component cell (cm2)"
    legend_constants[64] = "Acap in component cell (uF)"
    legend_constants[65] = "vmyo in component cell (uL)"
    legend_constants[62] = "vmito in component cell (uL)"
    legend_constants[63] = "vsr in component cell (uL)"
    legend_constants[66] = "vnsr in component cell (uL)"
    legend_constants[67] = "vjsr in component cell (uL)"
    legend_constants[68] = "vss in component cell (uL)"
    legend_constants[69] = "AF in component cell (uF_mole_per_C)"
    legend_constants[9] = "stim_offset in component cell (ms)"
    legend_constants[10] = "stim_period in component cell (ms)"
    legend_constants[11] = "stim_duration in component cell (ms)"
    legend_constants[12] = "stim_amplitude in component cell (uA_per_uF)"
    legend_algebraic[16] = "i_Stim in component cell (uA_per_uF)"
    legend_algebraic[0] = "past in component cell (ms)"
    legend_algebraic[59] = "ENa in component reversal_potentials (mV)"
    legend_constants[58] = "GNa in component INa (mS_per_uF)"
    legend_algebraic[29] = "gNa in component INa (mS_per_uF)"
    legend_states[1] = "H in component INa (dimensionless)"
    legend_states[2] = "m in component INa (dimensionless)"
    legend_states[3] = "J in component INa (dimensionless)"
    legend_algebraic[1] = "am in component INa (per_ms)"
    legend_algebraic[17] = "bm in component INa (per_ms)"
    legend_algebraic[2] = "ah in component INa (per_ms)"
    legend_algebraic[18] = "bh in component INa (per_ms)"
    legend_algebraic[3] = "aj in component INa (per_ms)"
    legend_algebraic[19] = "bj in component INa (per_ms)"
    legend_states[4] = "Ca_ss in component Ca (mM)"
    legend_states[5] = "d in component ICaL (dimensionless)"
    legend_states[6] = "dp in component ICaL (dimensionless)"
    legend_states[7] = "f in component ICaL (dimensionless)"
    legend_states[8] = "fca in component ICaL (dimensionless)"
    legend_states[9] = "fca2 in component ICaL (dimensionless)"
    legend_states[10] = "f2 in component ICaL (dimensionless)"
    legend_constants[13] = "pca in component ICaL (L_per_F_ms)"
    legend_constants[14] = "gacai in component ICaL (dimensionless)"
    legend_constants[15] = "gacao in component ICaL (dimensionless)"
    legend_algebraic[54] = "CaMKactive in component Irel (dimensionless)"
    legend_algebraic[30] = "ibarca in component ICaL (uA_per_uF)"
    legend_algebraic[4] = "dss in component ICaL (dimensionless)"
    legend_algebraic[20] = "taud in component ICaL (ms)"
    legend_algebraic[5] = "fss in component ICaL (dimensionless)"
    legend_algebraic[6] = "f2ss in component ICaL (dimensionless)"
    legend_algebraic[21] = "tauf in component ICaL (ms)"
    legend_algebraic[22] = "tauf2 in component ICaL (ms)"
    legend_algebraic[7] = "dpss in component ICaL (dimensionless)"
    legend_algebraic[32] = "fcass in component ICaL (dimensionless)"
    legend_algebraic[33] = "fca2ss in component ICaL (dimensionless)"
    legend_algebraic[56] = "taufca in component ICaL (ms)"
    legend_algebraic[35] = "taufca2 in component ICaL (ms)"
    legend_algebraic[70] = "EK in component reversal_potentials (mV)"
    legend_algebraic[72] = "ak1 in component IK1 (per_ms)"
    legend_algebraic[74] = "bk1 in component IK1 (per_ms)"
    legend_constants[59] = "gkr in component IKr (mS_per_uF)"
    legend_constants[16] = "gkr_const in component IKr (mS_per_uF)"
    legend_algebraic[37] = "r in component IKr (dimensionless)"
    legend_states[11] = "xr in component IKr (dimensionless)"
    legend_algebraic[8] = "xrss in component IKr (dimensionless)"
    legend_algebraic[23] = "tauxr in component IKr (ms)"
    legend_states[12] = "Ca_i in component Ca (mM)"
    legend_algebraic[38] = "gks in component IKs (mS_per_uF)"
    legend_algebraic[84] = "EKs in component reversal_potentials (mV)"
    legend_algebraic[9] = "xss in component IKs (dimensionless)"
    legend_algebraic[24] = "tauxs in component IKs (ms)"
    legend_states[13] = "xs1 in component IKs (dimensionless)"
    legend_states[14] = "xs2 in component IKs (dimensionless)"
    legend_constants[17] = "gitodv in component Ito (mS_per_uF)"
    legend_algebraic[39] = "rv in component Ito (dimensionless)"
    legend_algebraic[10] = "ay in component Ito (per_ms)"
    legend_algebraic[25] = "by in component Ito (per_ms)"
    legend_algebraic[11] = "ay2 in component Ito (per_ms)"
    legend_algebraic[26] = "by2 in component Ito (per_ms)"
    legend_algebraic[12] = "ay3 in component Ito (per_ms)"
    legend_algebraic[27] = "by3 in component Ito (per_ms)"
    legend_states[15] = "ydv in component Ito (dimensionless)"
    legend_states[16] = "ydv2 in component Ito (dimensionless)"
    legend_states[17] = "zdv in component Ito (dimensionless)"
    legend_states[18] = "Na_i in component Na (mM)"
    legend_constants[18] = "kmnai in component INaK (mM)"
    legend_constants[19] = "kmko in component INaK (mM)"
    legend_constants[20] = "ibarnak in component INaK (uA_per_uF)"
    legend_constants[60] = "sigma in component INaK (dimensionless)"
    legend_algebraic[40] = "fnak in component INaK (dimensionless)"
    legend_algebraic[42] = "ca_i_NaCa in component INaCa (mM)"
    legend_constants[21] = "KmCa in component INaCa (mM)"
    legend_algebraic[43] = "allo in component INaCa (dimensionless)"
    legend_constants[22] = "NCXmax in component INaCa (uA_per_uF)"
    legend_constants[23] = "ksat in component INaCa (dimensionless)"
    legend_constants[24] = "eta in component INaCa (dimensionless)"
    legend_constants[25] = "KmNai in component INaCa (mM)"
    legend_constants[26] = "KmNao in component INaCa (mM)"
    legend_constants[27] = "KmCai in component INaCa (mM)"
    legend_constants[28] = "KmCao in component INaCa (mM)"
    legend_algebraic[44] = "num in component INaCa (mM4)"
    legend_algebraic[45] = "denom1 in component INaCa (dimensionless)"
    legend_algebraic[46] = "denom2 in component INaCa (mM4)"
    legend_algebraic[47] = "denom3 in component INaCa (mM4)"
    legend_constants[29] = "ibarpca in component IpCa (uA_per_uF)"
    legend_constants[30] = "kmpca in component IpCa (mM)"
    legend_states[19] = "Cl_i in component Cl (mM)"
    legend_constants[31] = "PCl in component Ito2 (L_per_F_ms)"
    legend_states[20] = "AA in component Ito2 (dimensionless)"
    legend_algebraic[53] = "Ito2_max in component Ito2 (uA_per_uF)"
    legend_algebraic[13] = "AAss in component Ito2 (dimensionless)"
    legend_constants[32] = "Kmto2 in component Ito2 (mM)"
    legend_algebraic[87] = "ECl in component reversal_potentials (mV)"
    legend_constants[33] = "GClb in component IClb (mS_per_uF)"
    legend_constants[34] = "GNaL in component INal (mS_per_uF)"
    legend_states[21] = "mL in component INal (dimensionless)"
    legend_states[22] = "hL in component INal (dimensionless)"
    legend_algebraic[14] = "amL in component INal (per_ms)"
    legend_algebraic[28] = "bmL in component INal (per_ms)"
    legend_algebraic[15] = "hLss in component INal (dimensionless)"
    legend_states[23] = "K_i in component K (mM)"
    legend_constants[35] = "prnak in component reversal_potentials (dimensionless)"
    legend_states[24] = "Ca_jsr in component Ca (mM)"
    legend_algebraic[61] = "Grel in component Irel (per_ms)"
    legend_algebraic[34] = "dro_inf in component Irel (dimensionless)"
    legend_constants[36] = "dtau_rel_max in component Irel (ms)"
    legend_algebraic[60] = "dtau_rel in component Irel (ms)"
    legend_algebraic[36] = "ross in component Irel (dimensionless)"
    legend_algebraic[63] = "riss in component Irel (dimensionless)"
    legend_algebraic[66] = "tauri in component Irel (ms)"
    legend_algebraic[64] = "irelcicr in component Irel (mM_per_ms)"
    legend_constants[37] = "CaMK0 in component Irel (dimensionless)"
    legend_constants[38] = "Km in component Irel (mM)"
    legend_constants[39] = "KmCaMK in component Irel (dimensionless)"
    legend_algebraic[52] = "CaMKbound in component Irel (dimensionless)"
    legend_states[25] = "CaMKtrap in component Irel (dimensionless)"
    legend_states[26] = "ro in component Irel (dimensionless)"
    legend_states[27] = "ri in component Irel (dimensionless)"
    legend_algebraic[58] = "vg in component Irel (dimensionless)"
    legend_algebraic[57] = "cafac in component Irel (dimensionless)"
    legend_constants[40] = "dKmPLBmax in component Iup_Ileak (mM)"
    legend_constants[41] = "dJupmax in component Iup_Ileak (dimensionless)"
    legend_algebraic[67] = "dKmPLB in component Iup_Ileak (mM)"
    legend_algebraic[69] = "dJup in component Iup_Ileak (dimensionless)"
    legend_constants[42] = "iupmax in component Iup_Ileak (mM_per_ms)"
    legend_constants[43] = "Kmup in component Iup_Ileak (mM)"
    legend_constants[44] = "nsrmax in component Iup_Ileak (mM)"
    legend_algebraic[71] = "iup in component Iup_Ileak (mM_per_ms)"
    legend_algebraic[73] = "ileak in component Iup_Ileak (mM_per_ms)"
    legend_states[28] = "Ca_nsr in component Ca (mM)"
    legend_algebraic[76] = "idiff in component Idiff_Itr (mM_per_ms)"
    legend_algebraic[75] = "itr in component Idiff_Itr (mM_per_ms)"
    legend_algebraic[90] = "CTNaCl in component Na (mM_per_ms)"
    legend_constants[45] = "CTNaClmax in component Na (mM_per_ms)"
    legend_algebraic[91] = "CTKCl in component K (mM_per_ms)"
    legend_constants[46] = "CTKClmax in component K (mM_per_ms)"
    legend_constants[47] = "kmt in component Ca (mM)"
    legend_constants[48] = "kmc in component Ca (mM)"
    legend_constants[49] = "tbar in component Ca (mM)"
    legend_constants[50] = "cbar in component Ca (mM)"
    legend_constants[51] = "kmcsqn in component Ca (mM)"
    legend_constants[52] = "csqnbar in component Ca (mM)"
    legend_algebraic[78] = "bcsqn in component Ca (dimensionless)"
    legend_algebraic[79] = "bmyo in component Ca (dimensionless)"
    legend_constants[53] = "BSRmax in component Ca (mM)"
    legend_constants[54] = "KmBSR in component Ca (mM)"
    legend_constants[55] = "BSLmax in component Ca (mM)"
    legend_constants[56] = "KmBSL in component Ca (mM)"
    legend_algebraic[80] = "bss in component Ca (dimensionless)"
    legend_rates[0] = "d/dt V in component cell (mV)"
    legend_rates[1] = "d/dt H in component INa (dimensionless)"
    legend_rates[2] = "d/dt m in component INa (dimensionless)"
    legend_rates[3] = "d/dt J in component INa (dimensionless)"
    legend_rates[5] = "d/dt d in component ICaL (dimensionless)"
    legend_rates[6] = "d/dt dp in component ICaL (dimensionless)"
    legend_rates[7] = "d/dt f in component ICaL (dimensionless)"
    legend_rates[10] = "d/dt f2 in component ICaL (dimensionless)"
    legend_rates[8] = "d/dt fca in component ICaL (dimensionless)"
    legend_rates[9] = "d/dt fca2 in component ICaL (dimensionless)"
    legend_rates[11] = "d/dt xr in component IKr (dimensionless)"
    legend_rates[13] = "d/dt xs1 in component IKs (dimensionless)"
    legend_rates[14] = "d/dt xs2 in component IKs (dimensionless)"
    legend_rates[15] = "d/dt ydv in component Ito (dimensionless)"
    legend_rates[16] = "d/dt ydv2 in component Ito (dimensionless)"
    legend_rates[17] = "d/dt zdv in component Ito (dimensionless)"
    legend_rates[20] = "d/dt AA in component Ito2 (dimensionless)"
    legend_rates[21] = "d/dt mL in component INal (dimensionless)"
    legend_rates[22] = "d/dt hL in component INal (dimensionless)"
    legend_rates[26] = "d/dt ro in component Irel (dimensionless)"
    legend_rates[27] = "d/dt ri in component Irel (dimensionless)"
    legend_rates[25] = "d/dt CaMKtrap in component Irel (dimensionless)"
    legend_rates[18] = "d/dt Na_i in component Na (mM)"
    legend_rates[23] = "d/dt K_i in component K (mM)"
    legend_rates[19] = "d/dt Cl_i in component Cl (mM)"
    legend_rates[12] = "d/dt Ca_i in component Ca (mM)"
    legend_rates[4] = "d/dt Ca_ss in component Ca (mM)"
    legend_rates[28] = "d/dt Ca_nsr in component Ca (mM)"
    legend_rates[24] = "d/dt Ca_jsr in component Ca (mM)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    constants[0] = 96485
    constants[1] = 5.4
    constants[2] = 1.8
    constants[3] = 140
    constants[4] = 100
    constants[5] = 0.0374358835078
    constants[6] = 1
    states[0] = -85.781844107117
    constants[7] = 0.01
    constants[8] = 0.0011
    constants[9] = 0
    constants[10] = 1e3
    constants[11] = 3
    constants[12] = -15
    states[1] = 0.987317750543
    states[2] = 0.001356538159
    states[3] = 0.991924983076
    states[4] = 0.00012271265
    states[5] = 0.00000164013
    states[6] = 8.98230672628
    states[7] = 0.999961508634
    states[8] = 0.97836624923
    states[9] = 0.893052931249
    states[10] = 0.992234519148
    constants[13] = 2.43e-4
    constants[14] = 1
    constants[15] = 0.341
    constants[16] = 0.0138542
    states[11] = 0.00000724074
    states[12] = 0.00012131666
    states[13] = 0.019883138161
    states[14] = 0.019890650554
    constants[17] = 0.19
    states[15] = 0.013970786703
    states[16] = 0.99996472752
    states[17] = 0.829206149767
    states[18] = 12.972433387269
    constants[18] = 10
    constants[19] = 1.5
    constants[20] = 0.61875
    constants[21] = 1.25e-4
    constants[22] = 4.5
    constants[23] = 0.27
    constants[24] = 0.35
    constants[25] = 12.3
    constants[26] = 87.5
    constants[27] = 0.0036
    constants[28] = 1.3
    constants[29] = 0.0575
    constants[30] = 0.5e-3
    states[19] = 15.59207157178
    constants[31] = 4e-7
    states[20] = 0.000816605172
    constants[32] = 0.1502
    constants[33] = 2.25e-4
    constants[34] = 65e-4
    states[21] = 0.001356538159
    states[22] = 0.26130711759
    states[23] = 135.469546216758
    constants[35] = 0.01833
    states[24] = 1.737580994071
    constants[36] = 10
    constants[37] = 0.05
    constants[38] = 0.0015
    constants[39] = 0.15
    states[25] = 0.021123704774
    states[26] = 0
    states[27] = 0.862666650318
    constants[40] = 0.00017
    constants[41] = 0.75
    constants[42] = 0.004375
    constants[43] = 0.00092
    constants[44] = 15
    states[28] = 1.832822335168
    constants[45] = 9.8443e-6
    constants[46] = 7.0756e-6
    constants[47] = 0.5e-3
    constants[48] = 2.38e-3
    constants[49] = 70e-3
    constants[50] = 50e-3
    constants[51] = 0.8
    constants[52] = 10
    constants[53] = 0.047
    constants[54] = 0.00087
    constants[55] = 1.124
    constants[56] = 0.0087
    constants[57] = 1000.00* pi*constants[8]*constants[8]*constants[7]
    constants[58] = custom_piecewise([equal(constants[6] , 0.00000), 8.25000 , True, 4.00000*8.25000])
    constants[59] = constants[16]*(power(constants[1]/5.40000, 1.0/2))
    constants[60] = (exp(constants[3]/67.3000)-1.00000)/7.00000
    constants[61] = 2.00000* pi*constants[8]*constants[8]+2.00000* pi*constants[8]*constants[7]
    constants[62] = constants[57]*0.260000
    constants[63] = constants[57]*0.0600000
    constants[64] = constants[61]*2.00000
    constants[65] = constants[57]*0.680000
    constants[66] = constants[57]*0.0552000
    constants[67] = constants[57]*0.00480000
    constants[68] = constants[57]*0.0200000
    constants[69] = constants[64]/constants[0]
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[7] = 9.00000-8.00000/(1.00000+exp(-(states[0]+65.0000)/3.40000))
    rates[6] = (algebraic[7]-states[6])/10.0000
    algebraic[13] = 1.00000/(1.00000+constants[32]/states[4])
    rates[20] = (algebraic[13]-states[20])/1.00000
    algebraic[15] = 1.00000/(1.00000+exp((states[0]+91.0000)/6.10000))
    rates[22] = (algebraic[15]-states[22])/600.000
    algebraic[2] = custom_piecewise([greater_equal(states[0] , -40.0000), 0.00000 , True, 0.135000*exp((80.0000+states[0])/-6.80000)])
    algebraic[18] = custom_piecewise([greater_equal(states[0] , -40.0000), 1.00000/(0.130000*(1.00000+exp((states[0]+10.6600)/-11.1000))) , True, 3.56000*exp(0.0790000*states[0])+310000.*exp(0.350000*states[0])])
    rates[1] = algebraic[2]*(1.00000-states[1])-algebraic[18]*states[1]
    algebraic[1] = (0.320000*1.00000*(states[0]+47.1300))/(1.00000-exp(-0.100000*(states[0]+47.1300)))
    algebraic[17] = 0.0800000*exp(-states[0]/11.0000)
    rates[2] = algebraic[1]*(1.00000-states[2])-algebraic[17]*states[2]
    algebraic[3] = custom_piecewise([greater_equal(states[0] , -40.0000), 0.00000 , True, ((-127140.*exp(0.244400*states[0])-3.47400e-05*exp(-0.0439100*states[0]))*1.00000*(states[0]+37.7800))/(1.00000+exp(0.311000*(states[0]+79.2300)))])
    algebraic[19] = custom_piecewise([greater_equal(states[0] , -40.0000), (0.300000*exp(-2.53500e-07*states[0]))/(1.00000+exp(-0.100000*(states[0]+32.0000))) , True, (0.121200*exp(-0.0105200*states[0]))/(1.00000+exp(-0.137800*(states[0]+40.1400)))])
    rates[3] = algebraic[3]*(1.00000-states[3])-algebraic[19]*states[3]
    algebraic[4] = 1.00000/(1.00000+exp(-(states[0]-4.00000)/6.74000))
    algebraic[20] = 0.590000+(0.800000*exp(0.0520000*(states[0]+13.0000)))/(1.00000+exp(0.132000*(states[0]+13.0000)))
    rates[5] = (algebraic[4]-states[5])/algebraic[20]
    algebraic[5] = 0.700000/(1.00000+exp((states[0]+17.1200)/7.00000))+0.300000
    algebraic[21] = 1.00000/(0.241100*exp(-(power(0.0450000*(states[0]-9.69140), 2.00000)))+0.0529000)
    rates[7] = (algebraic[5]-states[7])/algebraic[21]
    algebraic[6] = 0.770000/(1.00000+exp((states[0]+17.1200)/7.00000))+0.230000
    algebraic[22] = 1.00000/(0.0423000*exp(-(power(0.0590000*(states[0]-18.5726), 2.00000)))+0.00540000)
    rates[10] = (algebraic[6]-states[10])/algebraic[22]
    algebraic[8] = 1.00000/(1.00000+exp(-(states[0]+10.0850)/4.25000))
    algebraic[23] = 1.00000/((0.000600000*(states[0]-1.73840))/(1.00000-exp(-0.136000*(states[0]-1.73840)))+(0.000300000*(states[0]+38.3608))/(exp(0.152200*(states[0]+38.3608))-1.00000))
    rates[11] = (algebraic[8]-states[11])/algebraic[23]
    algebraic[9] = 1.00000/(1.00000+exp(-(states[0]-10.5000)/24.7000))
    algebraic[24] = 1.00000/((7.61000e-05*(states[0]+44.6000))/(1.00000-exp(-9.97000*(states[0]+44.6000)))+(0.000360000*(states[0]-0.550000))/(exp(0.128000*(states[0]-0.550000))-1.00000))
    rates[13] = (algebraic[9]-states[13])/algebraic[24]
    rates[14] = ((algebraic[9]-states[14])/algebraic[24])/2.00000
    algebraic[10] = (25.0000*exp((states[0]-40.0000)/25.0000))/(1.00000+exp((states[0]-40.0000)/25.0000))
    algebraic[25] = (25.0000*exp(-(states[0]+90.0000)/25.0000))/(1.00000+exp(-(states[0]+90.0000)/25.0000))
    rates[15] = algebraic[10]*(1.00000-states[15])-algebraic[25]*states[15]
    algebraic[11] = 0.0300000/(1.00000+exp((states[0]+60.0000)/5.00000))
    algebraic[26] = (0.200000*exp((states[0]+25.0000)/5.00000))/(1.00000+exp((states[0]+25.0000)/5.00000))
    rates[16] = algebraic[11]*(1.00000-states[16])-algebraic[26]*states[16]
    algebraic[12] = 0.00225000/(1.00000+exp((states[0]+60.0000)/5.00000))
    algebraic[27] = (0.100000*exp((states[0]+25.0000)/5.00000))/(1.00000+exp((states[0]+25.0000)/5.00000))
    rates[17] = algebraic[12]*(1.00000-states[17])-algebraic[27]*states[17]
    algebraic[14] = (0.320000*1.00000*(states[0]+47.1300))/(1.00000-exp(-0.100000*(states[0]+47.1300)))
    algebraic[28] = 0.0800000*exp(-states[0]/11.0000)
    rates[21] = algebraic[14]*(1.00000-states[21])-algebraic[28]*states[21]
    algebraic[30] = (constants[13]*4.00000*(states[0]-15.0000)*constants[0]*constants[5]*(constants[14]*states[4]*exp(2.00000*(states[0]-15.0000)*constants[5])-constants[15]*constants[2]))/(exp(2.00000*(states[0]-15.0000)*constants[5])-1.00000)
    algebraic[31] = custom_piecewise([equal(constants[6] , 0.00000), (power(states[5], states[6]))*states[7]*states[10]*states[8]*states[9]*algebraic[30] , True, states[5]*states[7]*states[10]*states[8]*states[9]*algebraic[30]])
    algebraic[33] = 1.00000/(1.00000-algebraic[31]/0.0100000)
    algebraic[35] = 300.000/(1.00000+exp((-algebraic[31]-0.175000)/0.0400000))+125.000
    rates[9] = (algebraic[33]-states[9])/algebraic[35]
    algebraic[34] = (power(states[24], 1.90000))/(power(states[24], 1.90000)+power((49.2800*states[4])/(states[4]+0.00280000), 1.90000))
    algebraic[36] = algebraic[34]/(power(1.00000/algebraic[31], 2.00000)+1.00000)
    rates[26] = (algebraic[36]-states[26])/3.00000
    algebraic[52] = (constants[37]*(1.00000-states[25]))/(1.00000+constants[38]/states[4])
    algebraic[54] = algebraic[52]+states[25]
    rates[25] = 0.0500000*algebraic[54]*(algebraic[54]-states[25])-0.000680000*states[25]
    algebraic[32] = 0.300000/(1.00000-algebraic[31]/0.0500000)+0.550000/(1.00000+states[4]/0.00300000)+0.150000
    algebraic[56] = (10.0000*algebraic[54])/(0.150000+algebraic[54])+1.00000/(1.00000+states[4]/0.00300000)+0.500000
    rates[8] = (algebraic[32]-states[8])/algebraic[56]
    algebraic[57] = 1.00000/(1.00000+exp((algebraic[31]+0.0500000)/0.0150000))
    algebraic[63] = 1.00000/(1.00000+exp(((states[4]-0.000400000)+0.00200000*algebraic[57])/2.50000e-05))
    algebraic[60] = (constants[36]*algebraic[54])/(constants[39]+algebraic[54])
    algebraic[66] = 3.00000+algebraic[60]+(350.000-algebraic[60])/(1.00000+exp(((states[4]-0.00300000)+0.00300000*algebraic[57])/0.000200000))
    rates[27] = (algebraic[63]-states[27])/algebraic[66]
    algebraic[67] = (constants[40]*algebraic[54])/(constants[39]+algebraic[54])
    algebraic[69] = (constants[41]*algebraic[54])/(constants[39]+algebraic[54])
    algebraic[71] = ((algebraic[69]+1.00000)*constants[42]*states[12])/((states[12]+constants[43])-algebraic[67])
    algebraic[73] = (constants[42]*states[28])/constants[44]
    algebraic[75] = (states[28]-states[24])/120.000
    rates[28] = (algebraic[71]-(algebraic[75]*constants[67])/constants[66])-algebraic[73]
    algebraic[49] = (constants[29]*states[12])/(constants[30]+states[12])
    algebraic[50] = (1.99508e-07*4.00000*states[0]*constants[0]*constants[5]*(states[12]*exp(2.00000*states[0]*constants[5])-0.341000*constants[2]))/(exp(2.00000*states[0]*constants[5])-1.00000)
    algebraic[42] = 1.50000*states[12]
    algebraic[43] = 1.00000/(1.00000+power(constants[21]/algebraic[42], 2.00000))
    algebraic[44] = (power(states[18], 3.00000))*constants[2]*exp(constants[24]*states[0]*constants[5])-(power(constants[3], 3.00000))*algebraic[42]*exp((constants[24]-1.00000)*states[0]*constants[5])
    algebraic[45] = 1.00000+constants[23]*exp((constants[24]-1.00000)*states[0]*constants[5])
    algebraic[46] = constants[28]*(power(states[18], 3.00000))+(power(constants[26], 3.00000))*algebraic[42]+(power(constants[25], 3.00000))*constants[2]*(1.00000+algebraic[42]/constants[27])
    algebraic[47] = constants[27]*(power(constants[3], 3.00000))*(1.00000+power(states[18]/constants[25], 3.00000))+(power(states[18], 3.00000))*constants[2]+(power(constants[3], 3.00000))*algebraic[42]
    algebraic[48] = (constants[22]*algebraic[43]*algebraic[44])/(algebraic[45]*(algebraic[46]+algebraic[47]))
    algebraic[76] = (states[4]-states[12])/0.200000
    algebraic[79] = 1.00000/(1.00000+(constants[50]*constants[48])/(power(states[12]+constants[48], 2.00000))+(constants[47]*constants[49])/(power(states[12]+constants[47], 2.00000)))
    rates[12] = algebraic[79]*((-((algebraic[50]+algebraic[49])-2.00000*algebraic[48])*constants[69])/(constants[65]*2.00000)+((algebraic[73]-algebraic[71])*constants[66])/constants[65]+(algebraic[76]*constants[68])/constants[65])
    algebraic[58] = custom_piecewise([equal(constants[6] , 0.00000), 1.00000/(1.00000+exp((algebraic[30]+13.0000)/5.00000)) , True, 1.00000])
    algebraic[61] = 3000.00*algebraic[58]
    algebraic[64] = algebraic[61]*states[26]*states[27]*(states[24]-states[4])
    algebraic[80] = 1.00000/(1.00000+(constants[53]*constants[54])/(power(constants[54]+states[4], 2.00000))+(constants[55]*constants[56])/(power(constants[56]+states[4], 2.00000)))
    rates[4] = algebraic[80]*(((-algebraic[31]*constants[69])/(constants[68]*2.00000)+(algebraic[64]*constants[67])/constants[68])-algebraic[76])
    algebraic[78] = 1.00000/(1.00000+(constants[51]*constants[52])/(power(states[24]+constants[51], 2.00000)))
    rates[24] = algebraic[78]*(algebraic[75]-algebraic[64])
    algebraic[51] = (algebraic[31]+algebraic[50]+algebraic[49])-2.00000*algebraic[48]
    algebraic[59] = log(constants[3]/states[18])/constants[5]
    algebraic[29] = constants[58]*states[2]*states[2]*states[2]*states[1]*states[3]
    algebraic[62] = algebraic[29]*(states[0]-algebraic[59])
    algebraic[40] = 1.00000/(1.00000+0.124500*exp(-0.100000*states[0]*constants[5])+0.0365000*constants[60]*exp(-states[0]*constants[5]))
    algebraic[41] = (((constants[20]*algebraic[40]*1.00000)/(1.00000+power(constants[18]/states[18], 2.00000)))*constants[1])/(constants[1]+constants[19])
    algebraic[65] = constants[34]*(power(states[21], 3.00000))*states[22]*(states[0]-algebraic[59])
    algebraic[68] = algebraic[62]+3.00000*algebraic[48]+3.00000*algebraic[41]+algebraic[65]
    algebraic[70] = log(constants[1]/states[23])/constants[5]
    algebraic[72] = 1.02000/(1.00000+exp(0.238500*((states[0]-algebraic[70])-59.2150)))
    algebraic[74] = (0.491240*exp(0.0803200*((states[0]-algebraic[70])+5.47600))+1.00000*exp(0.0617500*((states[0]-algebraic[70])-594.310)))/(1.00000+exp(-0.514300*((states[0]-algebraic[70])+4.75300)))
    algebraic[77] = ((0.500000*(power(constants[1]/5.40000, 1.0/2))*algebraic[72])/(algebraic[72]+algebraic[74]))*(states[0]-algebraic[70])
    algebraic[83] = (0.00276000*(states[0]-algebraic[70]))/(1.00000+exp((7.48800-states[0])/5.98000))
    algebraic[38] = 0.0248975*(1.00000+0.600000/(1.00000+power(3.80000e-05/states[12], 1.40000)))
    algebraic[84] = log((constants[1]+constants[35]*constants[3])/(states[23]+constants[35]*states[18]))/constants[5]
    algebraic[85] = algebraic[38]*states[13]*states[14]*(states[0]-algebraic[84])
    algebraic[37] = 1.00000/(1.00000+exp((states[0]+10.0000)/15.4000))
    algebraic[81] = constants[59]*states[11]*algebraic[37]*(states[0]-algebraic[70])
    algebraic[39] = exp(states[0]/300.000)
    algebraic[82] = constants[17]*(power(states[15], 3.00000))*states[16]*states[17]*algebraic[39]*(states[0]-algebraic[70])
    algebraic[0] = floor(voi/constants[10])*constants[10]
    algebraic[16] = custom_piecewise([greater_equal(voi-algebraic[0] , constants[9]) & less_equal(voi-algebraic[0] , constants[9]+constants[11]), constants[12] , True, 0.00000])
    algebraic[86] = ((algebraic[81]+algebraic[85]+algebraic[77]+algebraic[83])-2.00000*algebraic[41])+algebraic[82]+0.500000*algebraic[16]
    algebraic[53] = (constants[31]*states[0]*constants[0]*constants[5]*(states[19]-constants[4]*exp(states[0]*constants[5])))/(1.00000-exp(states[0]*constants[5]))
    algebraic[55] = algebraic[53]*states[20]
    algebraic[87] = -log(constants[4]/states[19])/constants[5]
    algebraic[88] = constants[33]*(states[0]-algebraic[87])
    algebraic[89] = algebraic[88]+algebraic[55]+0.500000*algebraic[16]
    rates[0] = -(algebraic[68]+algebraic[86]+algebraic[51]+algebraic[89])
    algebraic[90] = (constants[45]*(power(algebraic[59]-algebraic[87], 4.00000)))/(power(algebraic[59]-algebraic[87], 4.00000)+power(87.8251, 4.00000))
    rates[18] = (-algebraic[68]*constants[69])/constants[65]+algebraic[90]
    algebraic[91] = (constants[46]*(algebraic[70]-algebraic[87]))/((algebraic[70]-algebraic[87])+87.8251)
    rates[23] = (-algebraic[86]*constants[69])/constants[65]+algebraic[91]
    rates[19] = (algebraic[89]*constants[69])/constants[65]+algebraic[90]+algebraic[91]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[7] = 9.00000-8.00000/(1.00000+exp(-(states[0]+65.0000)/3.40000))
    algebraic[13] = 1.00000/(1.00000+constants[32]/states[4])
    algebraic[15] = 1.00000/(1.00000+exp((states[0]+91.0000)/6.10000))
    algebraic[2] = custom_piecewise([greater_equal(states[0] , -40.0000), 0.00000 , True, 0.135000*exp((80.0000+states[0])/-6.80000)])
    algebraic[18] = custom_piecewise([greater_equal(states[0] , -40.0000), 1.00000/(0.130000*(1.00000+exp((states[0]+10.6600)/-11.1000))) , True, 3.56000*exp(0.0790000*states[0])+310000.*exp(0.350000*states[0])])
    algebraic[1] = (0.320000*1.00000*(states[0]+47.1300))/(1.00000-exp(-0.100000*(states[0]+47.1300)))
    algebraic[17] = 0.0800000*exp(-states[0]/11.0000)
    algebraic[3] = custom_piecewise([greater_equal(states[0] , -40.0000), 0.00000 , True, ((-127140.*exp(0.244400*states[0])-3.47400e-05*exp(-0.0439100*states[0]))*1.00000*(states[0]+37.7800))/(1.00000+exp(0.311000*(states[0]+79.2300)))])
    algebraic[19] = custom_piecewise([greater_equal(states[0] , -40.0000), (0.300000*exp(-2.53500e-07*states[0]))/(1.00000+exp(-0.100000*(states[0]+32.0000))) , True, (0.121200*exp(-0.0105200*states[0]))/(1.00000+exp(-0.137800*(states[0]+40.1400)))])
    algebraic[4] = 1.00000/(1.00000+exp(-(states[0]-4.00000)/6.74000))
    algebraic[20] = 0.590000+(0.800000*exp(0.0520000*(states[0]+13.0000)))/(1.00000+exp(0.132000*(states[0]+13.0000)))
    algebraic[5] = 0.700000/(1.00000+exp((states[0]+17.1200)/7.00000))+0.300000
    algebraic[21] = 1.00000/(0.241100*exp(-(power(0.0450000*(states[0]-9.69140), 2.00000)))+0.0529000)
    algebraic[6] = 0.770000/(1.00000+exp((states[0]+17.1200)/7.00000))+0.230000
    algebraic[22] = 1.00000/(0.0423000*exp(-(power(0.0590000*(states[0]-18.5726), 2.00000)))+0.00540000)
    algebraic[8] = 1.00000/(1.00000+exp(-(states[0]+10.0850)/4.25000))
    algebraic[23] = 1.00000/((0.000600000*(states[0]-1.73840))/(1.00000-exp(-0.136000*(states[0]-1.73840)))+(0.000300000*(states[0]+38.3608))/(exp(0.152200*(states[0]+38.3608))-1.00000))
    algebraic[9] = 1.00000/(1.00000+exp(-(states[0]-10.5000)/24.7000))
    algebraic[24] = 1.00000/((7.61000e-05*(states[0]+44.6000))/(1.00000-exp(-9.97000*(states[0]+44.6000)))+(0.000360000*(states[0]-0.550000))/(exp(0.128000*(states[0]-0.550000))-1.00000))
    algebraic[10] = (25.0000*exp((states[0]-40.0000)/25.0000))/(1.00000+exp((states[0]-40.0000)/25.0000))
    algebraic[25] = (25.0000*exp(-(states[0]+90.0000)/25.0000))/(1.00000+exp(-(states[0]+90.0000)/25.0000))
    algebraic[11] = 0.0300000/(1.00000+exp((states[0]+60.0000)/5.00000))
    algebraic[26] = (0.200000*exp((states[0]+25.0000)/5.00000))/(1.00000+exp((states[0]+25.0000)/5.00000))
    algebraic[12] = 0.00225000/(1.00000+exp((states[0]+60.0000)/5.00000))
    algebraic[27] = (0.100000*exp((states[0]+25.0000)/5.00000))/(1.00000+exp((states[0]+25.0000)/5.00000))
    algebraic[14] = (0.320000*1.00000*(states[0]+47.1300))/(1.00000-exp(-0.100000*(states[0]+47.1300)))
    algebraic[28] = 0.0800000*exp(-states[0]/11.0000)
    algebraic[30] = (constants[13]*4.00000*(states[0]-15.0000)*constants[0]*constants[5]*(constants[14]*states[4]*exp(2.00000*(states[0]-15.0000)*constants[5])-constants[15]*constants[2]))/(exp(2.00000*(states[0]-15.0000)*constants[5])-1.00000)
    algebraic[31] = custom_piecewise([equal(constants[6] , 0.00000), (power(states[5], states[6]))*states[7]*states[10]*states[8]*states[9]*algebraic[30] , True, states[5]*states[7]*states[10]*states[8]*states[9]*algebraic[30]])
    algebraic[33] = 1.00000/(1.00000-algebraic[31]/0.0100000)
    algebraic[35] = 300.000/(1.00000+exp((-algebraic[31]-0.175000)/0.0400000))+125.000
    algebraic[34] = (power(states[24], 1.90000))/(power(states[24], 1.90000)+power((49.2800*states[4])/(states[4]+0.00280000), 1.90000))
    algebraic[36] = algebraic[34]/(power(1.00000/algebraic[31], 2.00000)+1.00000)
    algebraic[52] = (constants[37]*(1.00000-states[25]))/(1.00000+constants[38]/states[4])
    algebraic[54] = algebraic[52]+states[25]
    algebraic[32] = 0.300000/(1.00000-algebraic[31]/0.0500000)+0.550000/(1.00000+states[4]/0.00300000)+0.150000
    algebraic[56] = (10.0000*algebraic[54])/(0.150000+algebraic[54])+1.00000/(1.00000+states[4]/0.00300000)+0.500000
    algebraic[57] = 1.00000/(1.00000+exp((algebraic[31]+0.0500000)/0.0150000))
    algebraic[63] = 1.00000/(1.00000+exp(((states[4]-0.000400000)+0.00200000*algebraic[57])/2.50000e-05))
    algebraic[60] = (constants[36]*algebraic[54])/(constants[39]+algebraic[54])
    algebraic[66] = 3.00000+algebraic[60]+(350.000-algebraic[60])/(1.00000+exp(((states[4]-0.00300000)+0.00300000*algebraic[57])/0.000200000))
    algebraic[67] = (constants[40]*algebraic[54])/(constants[39]+algebraic[54])
    algebraic[69] = (constants[41]*algebraic[54])/(constants[39]+algebraic[54])
    algebraic[71] = ((algebraic[69]+1.00000)*constants[42]*states[12])/((states[12]+constants[43])-algebraic[67])
    algebraic[73] = (constants[42]*states[28])/constants[44]
    algebraic[75] = (states[28]-states[24])/120.000
    algebraic[49] = (constants[29]*states[12])/(constants[30]+states[12])
    algebraic[50] = (1.99508e-07*4.00000*states[0]*constants[0]*constants[5]*(states[12]*exp(2.00000*states[0]*constants[5])-0.341000*constants[2]))/(exp(2.00000*states[0]*constants[5])-1.00000)
    algebraic[42] = 1.50000*states[12]
    algebraic[43] = 1.00000/(1.00000+power(constants[21]/algebraic[42], 2.00000))
    algebraic[44] = (power(states[18], 3.00000))*constants[2]*exp(constants[24]*states[0]*constants[5])-(power(constants[3], 3.00000))*algebraic[42]*exp((constants[24]-1.00000)*states[0]*constants[5])
    algebraic[45] = 1.00000+constants[23]*exp((constants[24]-1.00000)*states[0]*constants[5])
    algebraic[46] = constants[28]*(power(states[18], 3.00000))+(power(constants[26], 3.00000))*algebraic[42]+(power(constants[25], 3.00000))*constants[2]*(1.00000+algebraic[42]/constants[27])
    algebraic[47] = constants[27]*(power(constants[3], 3.00000))*(1.00000+power(states[18]/constants[25], 3.00000))+(power(states[18], 3.00000))*constants[2]+(power(constants[3], 3.00000))*algebraic[42]
    algebraic[48] = (constants[22]*algebraic[43]*algebraic[44])/(algebraic[45]*(algebraic[46]+algebraic[47]))
    algebraic[76] = (states[4]-states[12])/0.200000
    algebraic[79] = 1.00000/(1.00000+(constants[50]*constants[48])/(power(states[12]+constants[48], 2.00000))+(constants[47]*constants[49])/(power(states[12]+constants[47], 2.00000)))
    algebraic[58] = custom_piecewise([equal(constants[6] , 0.00000), 1.00000/(1.00000+exp((algebraic[30]+13.0000)/5.00000)) , True, 1.00000])
    algebraic[61] = 3000.00*algebraic[58]
    algebraic[64] = algebraic[61]*states[26]*states[27]*(states[24]-states[4])
    algebraic[80] = 1.00000/(1.00000+(constants[53]*constants[54])/(power(constants[54]+states[4], 2.00000))+(constants[55]*constants[56])/(power(constants[56]+states[4], 2.00000)))
    algebraic[78] = 1.00000/(1.00000+(constants[51]*constants[52])/(power(states[24]+constants[51], 2.00000)))
    algebraic[51] = (algebraic[31]+algebraic[50]+algebraic[49])-2.00000*algebraic[48]
    algebraic[59] = log(constants[3]/states[18])/constants[5]
    algebraic[29] = constants[58]*states[2]*states[2]*states[2]*states[1]*states[3]
    algebraic[62] = algebraic[29]*(states[0]-algebraic[59])
    algebraic[40] = 1.00000/(1.00000+0.124500*exp(-0.100000*states[0]*constants[5])+0.0365000*constants[60]*exp(-states[0]*constants[5]))
    algebraic[41] = (((constants[20]*algebraic[40]*1.00000)/(1.00000+power(constants[18]/states[18], 2.00000)))*constants[1])/(constants[1]+constants[19])
    algebraic[65] = constants[34]*(power(states[21], 3.00000))*states[22]*(states[0]-algebraic[59])
    algebraic[68] = algebraic[62]+3.00000*algebraic[48]+3.00000*algebraic[41]+algebraic[65]
    algebraic[70] = log(constants[1]/states[23])/constants[5]
    algebraic[72] = 1.02000/(1.00000+exp(0.238500*((states[0]-algebraic[70])-59.2150)))
    algebraic[74] = (0.491240*exp(0.0803200*((states[0]-algebraic[70])+5.47600))+1.00000*exp(0.0617500*((states[0]-algebraic[70])-594.310)))/(1.00000+exp(-0.514300*((states[0]-algebraic[70])+4.75300)))
    algebraic[77] = ((0.500000*(power(constants[1]/5.40000, 1.0/2))*algebraic[72])/(algebraic[72]+algebraic[74]))*(states[0]-algebraic[70])
    algebraic[83] = (0.00276000*(states[0]-algebraic[70]))/(1.00000+exp((7.48800-states[0])/5.98000))
    algebraic[38] = 0.0248975*(1.00000+0.600000/(1.00000+power(3.80000e-05/states[12], 1.40000)))
    algebraic[84] = log((constants[1]+constants[35]*constants[3])/(states[23]+constants[35]*states[18]))/constants[5]
    algebraic[85] = algebraic[38]*states[13]*states[14]*(states[0]-algebraic[84])
    algebraic[37] = 1.00000/(1.00000+exp((states[0]+10.0000)/15.4000))
    algebraic[81] = constants[59]*states[11]*algebraic[37]*(states[0]-algebraic[70])
    algebraic[39] = exp(states[0]/300.000)
    algebraic[82] = constants[17]*(power(states[15], 3.00000))*states[16]*states[17]*algebraic[39]*(states[0]-algebraic[70])
    algebraic[0] = floor(voi/constants[10])*constants[10]
    algebraic[16] = custom_piecewise([greater_equal(voi-algebraic[0] , constants[9]) & less_equal(voi-algebraic[0] , constants[9]+constants[11]), constants[12] , True, 0.00000])
    algebraic[86] = ((algebraic[81]+algebraic[85]+algebraic[77]+algebraic[83])-2.00000*algebraic[41])+algebraic[82]+0.500000*algebraic[16]
    algebraic[53] = (constants[31]*states[0]*constants[0]*constants[5]*(states[19]-constants[4]*exp(states[0]*constants[5])))/(1.00000-exp(states[0]*constants[5]))
    algebraic[55] = algebraic[53]*states[20]
    algebraic[87] = -log(constants[4]/states[19])/constants[5]
    algebraic[88] = constants[33]*(states[0]-algebraic[87])
    algebraic[89] = algebraic[88]+algebraic[55]+0.500000*algebraic[16]
    algebraic[90] = (constants[45]*(power(algebraic[59]-algebraic[87], 4.00000)))/(power(algebraic[59]-algebraic[87], 4.00000)+power(87.8251, 4.00000))
    algebraic[91] = (constants[46]*(algebraic[70]-algebraic[87]))/((algebraic[70]-algebraic[87])+87.8251)
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
        self.F = 96485
        self.K_o = 5.4
        self.Ca_o = 1.8
        self.Na_o = 140
        self.Cl_o = 100
        self.FonRT = 0.0374358835078
        self.tissue = 1
        self.l = 0.01
        self.a = 0.0011
        self.stim_offset = 0
        self.stim_period = 1e3
        self.stim_duration = 3
        self.stim_amplitude = -15
        self.pca = 2.43e-4
        self.gacai = 1
        self.gacao = 0.341
        self.gkr_const = 0.0138542
        self.gitodv = 0.19
        self.kmnai = 10
        self.kmko = 1.5
        self.ibarnak = 0.61875
        self.KmCa = 1.25e-4
        self.NCXmax = 4.5
        self.ksat = 0.27
        self.eta = 0.35
        self.KmNai = 12.3
        self.KmNao = 87.5
        self.KmCai = 0.0036
        self.KmCao = 1.3
        self.ibarpca = 0.0575
        self.kmpca = 0.5e-3
        self.PCl = 4e-7
        self.Kmto2 = 0.1502
        self.GClb = 2.25e-4
        self.GNaL = 65e-4
        self.prnak = 0.01833
        self.dtau_rel_max = 10
        self.CaMK0 = 0.05
        self.Km = 0.0015
        self.KmCaMK = 0.15
        self.dKmPLBmax = 0.00017
        self.dJupmax = 0.75
        self.iupmax = 0.004375
        self.Kmup = 0.00092
        self.nsrmax = 15
        self.CTNaClmax = 9.8443e-6
        self.CTKClmax = 7.0756e-6
        self.kmt = 0.5e-3
        self.kmc = 2.38e-3
        self.tbar = 70e-3
        self.cbar = 50e-3
        self.kmcsqn = 0.8
        self.csqnbar = 10
        self.BSRmax = 0.047
        self.KmBSR = 0.00087
        self.BSLmax = 1.124
        self.KmBSL = 0.0087

    def to_dict(self):
        return {
            "F": self.F,
            "K_o": self.K_o,
            "Ca_o": self.Ca_o,
            "Na_o": self.Na_o,
            "Cl_o": self.Cl_o,
            "FonRT": self.FonRT,
            "tissue": self.tissue,
            "l": self.l,
            "a": self.a,
            "stim_offset": self.stim_offset,
            "stim_period": self.stim_period,
            "stim_duration": self.stim_duration,
            "stim_amplitude": self.stim_amplitude,
            "pca": self.pca,
            "gacai": self.gacai,
            "gacao": self.gacao,
            "gkr_const": self.gkr_const,
            "gitodv": self.gitodv,
            "kmnai": self.kmnai,
            "kmko": self.kmko,
            "ibarnak": self.ibarnak,
            "KmCa": self.KmCa,
            "NCXmax": self.NCXmax,
            "ksat": self.ksat,
            "eta": self.eta,
            "KmNai": self.KmNai,
            "KmNao": self.KmNao,
            "KmCai": self.KmCai,
            "KmCao": self.KmCao,
            "ibarpca": self.ibarpca,
            "kmpca": self.kmpca,
            "PCl": self.PCl,
            "Kmto2": self.Kmto2,
            "GClb": self.GClb,
            "GNaL": self.GNaL,
            "prnak": self.prnak,
            "dtau_rel_max": self.dtau_rel_max,
            "CaMK0": self.CaMK0,
            "Km": self.Km,
            "KmCaMK": self.KmCaMK,
            "dKmPLBmax": self.dKmPLBmax,
            "dJupmax": self.dJupmax,
            "iupmax": self.iupmax,
            "Kmup": self.Kmup,
            "nsrmax": self.nsrmax,
            "CTNaClmax": self.CTNaClmax,
            "CTKClmax": self.CTKClmax,
            "kmt": self.kmt,
            "kmc": self.kmc,
            "tbar": self.tbar,
            "cbar": self.cbar,
            "kmcsqn": self.kmcsqn,
            "csqnbar": self.csqnbar,
            "BSRmax": self.BSRmax,
            "KmBSR": self.KmBSR,
            "BSLmax": self.BSLmax,
            "KmBSL": self.KmBSL,
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
        y0=[-85.781844107117, 0.987317750543, 0.001356538159, 0.991924983076, 0.00012271265, 0.00000164013, 8.98230672628, 0.999961508634, 0.97836624923, 0.893052931249, 0.992234519148, 0.00000724074, 0.00012131666, 0.019883138161, 0.019890650554, 0.013970786703, 0.99996472752, 0.829206149767, 12.972433387269, 15.59207157178, 0.000816605172, 0.001356538159, 0.26130711759, 135.469546216758, 1.737580994071, 0.021123704774, 0, 0.862666650318, 1.832822335168],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "hund_rudy_2004_a"
        self.curve_names = [
            "V",
            "H",
            "m",
            "J",
            "Ca_ss",
            "d",
            "dp",
            "f",
            "fca",
            "fca2",
            "f2",
            "xr",
            "Ca_i",
            "xs1",
            "xs2",
            "ydv",
            "ydv2",
            "zdv",
            "Na_i",
            "Cl_i",
            "AA",
            "mL",
            "hL",
            "K_i",
            "Ca_jsr",
            "CaMKtrap",
            "ro",
            "ri",
            "Ca_nsr",
        ]
        self.state_names = ['V', 'H', 'm', 'J', 'Ca_ss', 'd', 'dp', 'f', 'fca', 'fca2', 'f2', 'xr', 'Ca_i', 'xs1', 'xs2', 'ydv', 'ydv2', 'zdv', 'Na_i', 'Cl_i', 'AA', 'mL', 'hL', 'K_i', 'Ca_jsr', 'CaMKtrap', 'ro', 'ri', 'Ca_nsr']
        self.algebraic_names = ['past', 'am', 'ah', 'aj', 'dss', 'fss', 'f2ss', 'dpss', 'xrss', 'xss', 'ay', 'ay2', 'ay3', 'AAss', 'amL', 'hLss', 'i_Stim', 'bm', 'bh', 'bj', 'taud', 'tauf', 'tauf2', 'tauxr', 'tauxs', 'by', 'by2', 'by3', 'bmL', 'gNa', 'ibarca', 'ICaL', 'fcass', 'fca2ss', 'dro_inf', 'taufca2', 'ross', 'r', 'gks', 'rv', 'fnak', 'INaK', 'ca_i_NaCa', 'allo', 'num', 'denom1', 'denom2', 'denom3', 'INaCa', 'IpCa', 'ICab', 'caiont', 'CaMKbound', 'Ito2_max', 'CaMKactive', 'Ito2', 'taufca', 'cafac', 'vg', 'ENa', 'dtau_rel', 'Grel', 'INa', 'riss', 'irelcicr', 'INal', 'tauri', 'dKmPLB', 'naiont', 'dJup', 'EK', 'iup', 'ak1', 'ileak', 'bk1', 'itr', 'idiff', 'IK1', 'bcsqn', 'bmyo', 'bss', 'IKr', 'Ito', 'IKp', 'EKs', 'IKs', 'kiont', 'ECl', 'IClb', 'clont', 'CTNaCl', 'CTKCl']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 70
        p = self.params

        # direct mapping
        c[0] = p.F
        c[1] = p.K_o
        c[2] = p.Ca_o
        c[3] = p.Na_o
        c[4] = p.Cl_o
        c[5] = p.FonRT
        c[6] = p.tissue
        c[7] = p.l
        c[8] = p.a
        c[9] = p.stim_offset
        c[10] = p.stim_period
        c[11] = p.stim_duration
        c[12] = p.stim_amplitude
        c[13] = p.pca
        c[14] = p.gacai
        c[15] = p.gacao
        c[16] = p.gkr_const
        c[17] = p.gitodv
        c[18] = p.kmnai
        c[19] = p.kmko
        c[20] = p.ibarnak
        c[21] = p.KmCa
        c[22] = p.NCXmax
        c[23] = p.ksat
        c[24] = p.eta
        c[25] = p.KmNai
        c[26] = p.KmNao
        c[27] = p.KmCai
        c[28] = p.KmCao
        c[29] = p.ibarpca
        c[30] = p.kmpca
        c[31] = p.PCl
        c[32] = p.Kmto2
        c[33] = p.GClb
        c[34] = p.GNaL
        c[35] = p.prnak
        c[36] = p.dtau_rel_max
        c[37] = p.CaMK0
        c[38] = p.Km
        c[39] = p.KmCaMK
        c[40] = p.dKmPLBmax
        c[41] = p.dJupmax
        c[42] = p.iupmax
        c[43] = p.Kmup
        c[44] = p.nsrmax
        c[45] = p.CTNaClmax
        c[46] = p.CTKClmax
        c[47] = p.kmt
        c[48] = p.kmc
        c[49] = p.tbar
        c[50] = p.cbar
        c[51] = p.kmcsqn
        c[52] = p.csqnbar
        c[53] = p.BSRmax
        c[54] = p.KmBSR
        c[55] = p.BSLmax
        c[56] = p.KmBSL

        # derived constants
        c[57] = 1000.00* pi*c[8]*c[8]*c[7]
        c[58] = (8.25000 if equal(c[6] , 0.00000) else 4.00000*8.25000)
        c[59] = c[16]*(power(c[1]/5.40000, 1.0/2))
        c[60] = (exp(c[3]/67.3000)-1.00000)/7.00000
        c[61] = 2.00000* pi*c[8]*c[8]+2.00000* pi*c[8]*c[7]
        c[62] = c[57]*0.260000
        c[63] = c[57]*0.0600000
        c[64] = c[61]*2.00000
        c[65] = c[57]*0.680000
        c[66] = c[57]*0.0552000
        c[67] = c[57]*0.00480000
        c[68] = c[57]*0.0200000
        c[69] = c[64]/c[0]

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
