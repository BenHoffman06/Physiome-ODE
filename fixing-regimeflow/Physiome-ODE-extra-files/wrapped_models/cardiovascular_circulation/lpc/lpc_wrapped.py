# Size of variable arrays:
sizeAlgebraic = 98
sizeStates = 30
sizeConstants = 108
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "t in component lpc (s)"
    legend_constants[0] = "Vlvrd in component lpc (mL)"
    legend_constants[1] = "Vlvrs in component lpc (mL)"
    legend_constants[2] = "Vrvrd in component lpc (mL)"
    legend_constants[3] = "Vrvrs in component lpc (mL)"
    legend_constants[4] = "Vlard in component lpc (mL)"
    legend_constants[5] = "Vlars in component lpc (mL)"
    legend_constants[6] = "Vrard in component lpc (mL)"
    legend_constants[7] = "Vrars in component lpc (mL)"
    legend_constants[8] = "Rra in component lpc (resistance)"
    legend_constants[9] = "Rla in component lpc (resistance)"
    legend_constants[10] = "PRint in component lpc (s)"
    legend_constants[11] = "Emaxlv in component lpc (elastance)"
    legend_constants[12] = "Eminlv in component lpc (elastance)"
    legend_constants[13] = "Emaxrv in component lpc (elastance)"
    legend_constants[14] = "Eminrv in component lpc (elastance)"
    legend_constants[15] = "Emaxra in component lpc (elastance)"
    legend_constants[16] = "Eminra in component lpc (elastance)"
    legend_constants[17] = "Emaxla in component lpc (elastance)"
    legend_constants[18] = "Eminla in component lpc (elastance)"
    legend_constants[19] = "Pbs in component lpc (mmHg)"
    legend_constants[20] = "Vmyo in component lpc (mL)"
    legend_constants[21] = "TsvK in component lpc (s)"
    legend_constants[22] = "TsaK in component lpc (s)"
    legend_constants[23] = "HR in component lpc (ratepm)"
    legend_algebraic[17] = "Elv in component lpc (elastance)"
    legend_algebraic[15] = "Erv in component lpc (elastance)"
    legend_algebraic[14] = "Era in component lpc (elastance)"
    legend_algebraic[16] = "Ela in component lpc (elastance)"
    legend_algebraic[58] = "Vlvr in component lpc (mL)"
    legend_algebraic[81] = "Vrvr in component lpc (mL)"
    legend_algebraic[55] = "Vlar in component lpc (mL)"
    legend_algebraic[70] = "Vrar in component lpc (mL)"
    legend_algebraic[88] = "Fra in component lpc (flow)"
    legend_algebraic[94] = "Frv in component lpc (flow)"
    legend_algebraic[80] = "Fla in component lpc (flow)"
    legend_algebraic[83] = "Flv in component lpc (flow)"
    legend_algebraic[72] = "Pra in component lpc (mmHg)"
    legend_algebraic[74] = "Prac in component lpc (mmHg)"
    legend_algebraic[84] = "Prv in component lpc (mmHg)"
    legend_algebraic[86] = "Prvc in component lpc (mmHg)"
    legend_algebraic[57] = "Pla in component lpc (mmHg)"
    legend_algebraic[75] = "Plac in component lpc (mmHg)"
    legend_algebraic[59] = "Plv in component lpc (mmHg)"
    legend_algebraic[79] = "Plvc in component lpc (mmHg)"
    legend_states[0] = "Vra in component lpc (mL)"
    legend_states[1] = "Vrv in component lpc (mL)"
    legend_states[2] = "Vla in component lpc (mL)"
    legend_states[3] = "Vlv in component lpc (mL)"
    legend_constants[24] = "COutput in component lpc (flow)"
    legend_constants[103] = "SV in component lpc (mL)"
    legend_algebraic[6] = "P_QRSwave in component lpc (mV)"
    legend_constants[105] = "Tsv in component lpc (s)"
    legend_constants[107] = "Tsa in component lpc (s)"
    legend_algebraic[9] = "trela in component lpc (s)"
    legend_algebraic[7] = "trelv in component lpc (s)"
    legend_constants[25] = "Rav in component lpc (resistance)"
    legend_constants[26] = "Raop in component lpc (resistance)"
    legend_constants[27] = "Rcrb in component lpc (resistance)"
    legend_constants[28] = "Raod in component lpc (resistance)"
    legend_constants[29] = "Rtaop in component lpc (resistance)"
    legend_constants[30] = "Rtaod in component lpc (resistance)"
    legend_constants[31] = "Rsap in component lpc (resistance)"
    legend_constants[32] = "Rsc in component lpc (resistance)"
    legend_constants[33] = "Rsv in component lpc (resistance)"
    legend_constants[34] = "Rsao in component lpc (resistance)"
    legend_constants[35] = "Caop in component lpc (capacitance)"
    legend_constants[36] = "Caod in component lpc (capacitance)"
    legend_constants[37] = "Csap in component lpc (capacitance)"
    legend_constants[38] = "Csc in component lpc (capacitance)"
    legend_constants[39] = "Laop in component lpc (inductance)"
    legend_constants[40] = "Laod in component lpc (inductance)"
    legend_constants[41] = "Kc in component lpc (mmHg)"
    legend_constants[42] = "Do in component lpc (mL)"
    legend_constants[43] = "Vsa_o in component lpc (mL)"
    legend_constants[44] = "Vsa_max in component lpc (mL)"
    legend_constants[45] = "Kp1 in component lpc (mmHg)"
    legend_constants[46] = "Kp2 in component lpc (mmHgmlm2)"
    legend_constants[47] = "Kr in component lpc (resistance)"
    legend_constants[48] = "tau_p in component lpc (perml)"
    legend_constants[49] = "Kv in component lpc (mmHg)"
    legend_constants[50] = "Vmax_sv in component lpc (mL)"
    legend_constants[51] = "D2 in component lpc (mmHg)"
    legend_constants[52] = "K1 in component lpc (dimensionless)"
    legend_constants[53] = "K2 in component lpc (mmHg)"
    legend_constants[54] = "KR in component lpc (resistance)"
    legend_constants[55] = "Ro in component lpc (resistance)"
    legend_constants[56] = "Vo in component lpc (mL)"
    legend_constants[57] = "Vmax_vc in component lpc (mL)"
    legend_constants[58] = "Vmin_vc in component lpc (mL)"
    legend_constants[59] = "COtau in component lpc (s)"
    legend_constants[60] = "Pplc in component lpc (mmHg)"
    legend_constants[61] = "Px2 in component lpc (mmHg)"
    legend_constants[62] = "Vx8 in component lpc (mL)"
    legend_constants[63] = "Vx75 in component lpc (mL)"
    legend_constants[64] = "Vx1 in component lpc (mL)"
    legend_constants[65] = "Px1 in component lpc (mmHg)"
    legend_constants[66] = "F_vaso in component lpc (dimensionless)"
    legend_algebraic[52] = "Rvc in component lpc (resistance)"
    legend_algebraic[44] = "Rsa in component lpc (resistance)"
    legend_algebraic[0] = "Paop in component lpc (mmHg)"
    legend_states[4] = "Paopc in component lpc (mmHg)"
    legend_algebraic[50] = "Paod in component lpc (mmHg)"
    legend_algebraic[49] = "Paodc in component lpc (mmHg)"
    legend_algebraic[36] = "Psa_a in component lpc (mmHg)"
    legend_algebraic[37] = "Psa_p in component lpc (mmHg)"
    legend_algebraic[38] = "Psa in component lpc (mmHg)"
    legend_algebraic[39] = "Psap in component lpc (mmHg)"
    legend_algebraic[41] = "Psc in component lpc (mmHg)"
    legend_algebraic[42] = "Psv in component lpc (mmHg)"
    legend_algebraic[45] = "Pvc in component lpc (mmHg)"
    legend_algebraic[47] = "Pvcc in component lpc (mmHg)"
    legend_states[5] = "MAP in component lpc (mmHg)"
    legend_states[6] = "Faop in component lpc (flowLm)"
    legend_states[7] = "Faod in component lpc (flow)"
    legend_algebraic[40] = "Fsap in component lpc (flow)"
    legend_algebraic[46] = "Fsa in component lpc (flow)"
    legend_algebraic[43] = "Fsc in component lpc (flow)"
    legend_algebraic[48] = "Fsv in component lpc (flow)"
    legend_algebraic[78] = "Fvc in component lpc (flow)"
    legend_algebraic[51] = "Fcrb in component lpc (flow)"
    legend_states[8] = "Vaop in component lpc (mL)"
    legend_states[9] = "Vaod in component lpc (mL)"
    legend_states[10] = "Vsa in component lpc (mL)"
    legend_states[11] = "Vsap in component lpc (mL)"
    legend_states[12] = "Vsc in component lpc (mL)"
    legend_states[13] = "Vsv in component lpc (mL)"
    legend_states[14] = "Vvc in component lpc (mL)"
    legend_algebraic[54] = "Vtot in component lpc (mL)"
    legend_algebraic[1] = "SysArtVol in component lpc (mL)"
    legend_algebraic[2] = "SysVenVol in component lpc (mL)"
    legend_algebraic[3] = "PulArtVol in component lpc (mL)"
    legend_algebraic[4] = "PulVenVol in component lpc (mL)"
    legend_algebraic[56] = "VBcirc in component lpc (mL)"
    legend_constants[104] = "Ppl in component lpc (mmHg)"
    legend_constants[67] = "Rpuv in component lpc (resistance)"
    legend_constants[68] = "Rtpap in component lpc (resistance)"
    legend_constants[69] = "Rtpad in component lpc (resistance)"
    legend_constants[70] = "Rpap in component lpc (resistance)"
    legend_constants[71] = "Rpad in component lpc (resistance)"
    legend_constants[72] = "Rps in component lpc (resistance)"
    legend_constants[73] = "Rpa in component lpc (resistance)"
    legend_constants[74] = "Rpc in component lpc (resistance)"
    legend_constants[75] = "Rpv in component lpc (resistance)"
    legend_constants[76] = "Ctpap in component lpc (capacitance)"
    legend_constants[77] = "Ctpad in component lpc (capacitance)"
    legend_constants[78] = "Cpa in component lpc (capacitance)"
    legend_constants[79] = "Cpc in component lpc (capacitance)"
    legend_constants[80] = "Cpv in component lpc (capacitance)"
    legend_constants[81] = "Lpa in component lpc (inductance)"
    legend_constants[82] = "Lpad in component lpc (inductance)"
    legend_algebraic[92] = "Ppapc in component lpc (mmHg)"
    legend_algebraic[90] = "Ppapc1 in component lpc (mmHg)"
    legend_algebraic[28] = "Ppapc2 in component lpc (mmHg)"
    legend_algebraic[95] = "Ppap in component lpc (mmHg)"
    legend_algebraic[61] = "Ppad in component lpc (mmHg)"
    legend_algebraic[60] = "Ppadc in component lpc (mmHg)"
    legend_algebraic[26] = "Ppa in component lpc (mmHg)"
    legend_algebraic[27] = "Ppac in component lpc (mmHg)"
    legend_algebraic[29] = "Ppc in component lpc (mmHg)"
    legend_algebraic[30] = "Ppcc in component lpc (mmHg)"
    legend_algebraic[32] = "Ppv in component lpc (mmHg)"
    legend_algebraic[33] = "Ppvc in component lpc (mmHg)"
    legend_states[15] = "Vpap in component lpc (mL)"
    legend_states[16] = "Vpad in component lpc (mL)"
    legend_states[17] = "Vpa in component lpc (mL)"
    legend_states[18] = "Vpc in component lpc (mL)"
    legend_states[19] = "Vpv in component lpc (mL)"
    legend_states[20] = "Fpap in component lpc (flowLm)"
    legend_states[21] = "Fpad in component lpc (flow)"
    legend_algebraic[35] = "Fps in component lpc (flow)"
    legend_algebraic[31] = "Fpa in component lpc (flow)"
    legend_algebraic[34] = "Fpc in component lpc (flow)"
    legend_algebraic[77] = "Fpv in component lpc (flow)"
    legend_constants[83] = "K_pcd in component lpc (mmHg)"
    legend_constants[84] = "phi_pcd in component lpc (mL)"
    legend_constants[85] = "Vpcd_o in component lpc (mL)"
    legend_constants[86] = "perifl in component lpc (mL)"
    legend_algebraic[63] = "Ppcd in component lpc (mmHg)"
    legend_algebraic[64] = "Ppcdc in component lpc (mmHg)"
    legend_algebraic[62] = "Vpcd in component lpc (mL)"
    legend_constants[87] = "Rcorao in component lpc (resistance)"
    legend_constants[88] = "Rcorea in component lpc (resistance)"
    legend_constants[89] = "Rcorla in component lpc (resistance)"
    legend_constants[90] = "Rcorsa in component lpc (resistance)"
    legend_constants[91] = "Rcorcap in component lpc (resistance)"
    legend_constants[92] = "Rcorsv in component lpc (resistance)"
    legend_constants[93] = "Rcorlv in component lpc (resistance)"
    legend_constants[94] = "Rcorev in component lpc (resistance)"
    legend_constants[95] = "Ccorao in component lpc (capacitance)"
    legend_constants[96] = "Ccorea in component lpc (capacitance)"
    legend_constants[97] = "Ccorla in component lpc (capacitance)"
    legend_constants[98] = "Ccorsa in component lpc (capacitance)"
    legend_constants[99] = "Ccorcap in component lpc (capacitance)"
    legend_constants[100] = "Ccorsv in component lpc (capacitance)"
    legend_constants[101] = "Ccorlv in component lpc (capacitance)"
    legend_constants[102] = "Ccorev in component lpc (capacitance)"
    legend_algebraic[82] = "Pcorisfc in component lpc (mmHg)"
    legend_algebraic[18] = "Pcoraoc in component lpc (mmHg)"
    legend_algebraic[65] = "Pcoreac in component lpc (mmHg)"
    legend_algebraic[89] = "Pcorlac in component lpc (mmHg)"
    legend_algebraic[93] = "Pcorsac in component lpc (mmHg)"
    legend_algebraic[85] = "Pcorcapc in component lpc (mmHg)"
    legend_algebraic[71] = "Pcorsvc in component lpc (mmHg)"
    legend_algebraic[68] = "Pcorlvc in component lpc (mmHg)"
    legend_algebraic[67] = "Pcorevc in component lpc (mmHg)"
    legend_algebraic[8] = "Pcorao in component lpc (mmHg)"
    legend_algebraic[20] = "Pcorea in component lpc (mmHg)"
    legend_algebraic[22] = "Pcorla in component lpc (mmHg)"
    legend_algebraic[24] = "Pcorsa in component lpc (mmHg)"
    legend_algebraic[19] = "Pcorcap in component lpc (mmHg)"
    legend_algebraic[25] = "Pcorsv in component lpc (mmHg)"
    legend_algebraic[23] = "Pcorlv in component lpc (mmHg)"
    legend_algebraic[21] = "Pcorev in component lpc (mmHg)"
    legend_states[22] = "Vcorao in component lpc (mL)"
    legend_states[23] = "Vcorea in component lpc (mL)"
    legend_states[24] = "Vcorla in component lpc (mL)"
    legend_states[25] = "Vcorsa in component lpc (mL)"
    legend_states[26] = "Vcorcap in component lpc (mL)"
    legend_states[27] = "Vcorsv in component lpc (mL)"
    legend_states[28] = "Vcorlv in component lpc (mL)"
    legend_states[29] = "Vcorev in component lpc (mL)"
    legend_algebraic[53] = "Vcorcirc in component lpc (mL)"
    legend_algebraic[66] = "Fcorao in component lpc (flow)"
    legend_algebraic[91] = "Fcorea in component lpc (flow)"
    legend_algebraic[96] = "Fcorla in component lpc (flow)"
    legend_algebraic[97] = "Fcorsa in component lpc (flow)"
    legend_algebraic[87] = "Fcorcap in component lpc (flow)"
    legend_algebraic[73] = "Fcorsv in component lpc (flow)"
    legend_algebraic[69] = "Fcorlv in component lpc (flow)"
    legend_algebraic[76] = "Fcorev in component lpc (flow)"
    legend_algebraic[5] = "beattime in component lpc (s)"
    legend_algebraic[10] = "yla in component lpc (dimensionless)"
    legend_algebraic[11] = "yra in component lpc (dimensionless)"
    legend_algebraic[12] = "ylv in component lpc (dimensionless)"
    legend_algebraic[13] = "yrv in component lpc (dimensionless)"
    legend_constants[106] = "hrf in component lpc (Hz)"
    legend_rates[7] = "d/dt Faod in component lpc (flow)"
    legend_rates[6] = "d/dt Faop in component lpc (flowLm)"
    legend_rates[21] = "d/dt Fpad in component lpc (flow)"
    legend_rates[20] = "d/dt Fpap in component lpc (flowLm)"
    legend_rates[5] = "d/dt MAP in component lpc (mmHg)"
    legend_rates[4] = "d/dt Paopc in component lpc (mmHg)"
    legend_rates[8] = "d/dt Vaop in component lpc (mL)"
    legend_rates[16] = "d/dt Vpad in component lpc (mL)"
    legend_rates[9] = "d/dt Vaod in component lpc (mL)"
    legend_rates[22] = "d/dt Vcorao in component lpc (mL)"
    legend_rates[26] = "d/dt Vcorcap in component lpc (mL)"
    legend_rates[23] = "d/dt Vcorea in component lpc (mL)"
    legend_rates[29] = "d/dt Vcorev in component lpc (mL)"
    legend_rates[24] = "d/dt Vcorla in component lpc (mL)"
    legend_rates[28] = "d/dt Vcorlv in component lpc (mL)"
    legend_rates[25] = "d/dt Vcorsa in component lpc (mL)"
    legend_rates[27] = "d/dt Vcorsv in component lpc (mL)"
    legend_rates[2] = "d/dt Vla in component lpc (mL)"
    legend_rates[3] = "d/dt Vlv in component lpc (mL)"
    legend_rates[17] = "d/dt Vpa in component lpc (mL)"
    legend_rates[15] = "d/dt Vpap in component lpc (mL)"
    legend_rates[18] = "d/dt Vpc in component lpc (mL)"
    legend_rates[19] = "d/dt Vpv in component lpc (mL)"
    legend_rates[0] = "d/dt Vra in component lpc (mL)"
    legend_rates[1] = "d/dt Vrv in component lpc (mL)"
    legend_rates[10] = "d/dt Vsa in component lpc (mL)"
    legend_rates[11] = "d/dt Vsap in component lpc (mL)"
    legend_rates[12] = "d/dt Vsc in component lpc (mL)"
    legend_rates[13] = "d/dt Vsv in component lpc (mL)"
    legend_rates[14] = "d/dt Vvc in component lpc (mL)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    constants[0] = 72
    constants[1] = 23
    constants[2] = 103
    constants[3] = 53
    constants[4] = 10
    constants[5] = 8
    constants[6] = 10
    constants[7] = 8
    constants[8] = 0.001
    constants[9] = 0.001
    constants[10] = 0.12
    constants[11] = 5.6
    constants[12] = 0.186874659
    constants[13] = 0.67
    constants[14] = 0.1041640922
    constants[15] = 0.1091675077
    constants[16] = 0.0992431888
    constants[17] = 0.1446191772
    constants[18] = 0.1314719793
    constants[19] = 0
    constants[20] = 238
    constants[21] = 0.35
    constants[22] = 0.2
    constants[23] = 77
    states[0] = 78.2537
    states[1] = 167.4806
    states[2] = 85.9126
    states[3] = 125.360568
    constants[24] = 108.56912706
    constants[25] = 1e-4
    constants[26] = 1e-4
    constants[27] = 6.8284472205
    constants[28] = 0.025
    constants[29] = 0.2
    constants[30] = 0.3
    constants[31] = 0.025
    constants[32] = 0.1545054945
    constants[33] = 0.1381298227
    constants[34] = 0.5508058134
    constants[35] = 0.3445734208
    constants[36] = 1.4544677036
    constants[37] = 1.4843409851
    constants[38] = 7.9822364317
    constants[39] = 3.5e-4
    constants[40] = 3.5e-4
    constants[41] = 497.7852450367
    constants[42] = 50
    constants[43] = 485.7624931891
    constants[44] = 577.7106000108
    constants[45] = 0.03
    constants[46] = 0.05
    constants[47] = 0.01
    constants[48] = 0.1
    constants[49] = 21.83
    constants[50] = 3379.545
    constants[51] = -5
    constants[52] = 0.0968305478
    constants[53] = 0.4
    constants[54] = 0.001
    constants[55] = 0.025
    constants[56] = 129.6486
    constants[57] = 350.5314
    constants[58] = 50.010747
    constants[59] = 15
    constants[60] = -5.6
    constants[61] = 2
    constants[62] = 8
    constants[63] = 75
    constants[64] = 1
    constants[65] = 1
    constants[66] = 0.5
    states[4] = 87.93968
    states[5] = 90.6179
    states[6] = 0.698577
    states[7] = 23.5957
    states[8] = 31.1705
    states[9] = 138.4476
    states[10] = 519.7915
    states[11] = 129.6439
    states[12] = 256.8555
    states[13] = 2961.6507
    states[14] = 232.46638962
    constants[67] = 1e-4
    constants[68] = 0.05
    constants[69] = 0.05
    constants[70] = 1e-4
    constants[71] = 0.03
    constants[72] = 4.2958026137
    constants[73] = 0.0565149137
    constants[74] = 0.0309026688
    constants[75] = 1e-4
    constants[76] = 1.5365929068
    constants[77] = 2.6893667388
    constants[78] = 3.1321449506
    constants[79] = 7.7147
    constants[80] = 27.87028922
    constants[81] = 1.801907e-4
    constants[82] = 1.932239e-4
    states[15] = 33.1398
    states[16] = 60.11203897
    states[17] = 58.926
    states[18] = 107.57022
    states[19] = 293.0398
    states[20] = 1.2282
    states[21] = 57.1876
    constants[83] = 1
    constants[84] = 40
    constants[85] = 785
    constants[86] = 15
    constants[87] = 2.642367
    constants[88] = 2.642367
    constants[89] = 5.073345
    constants[90] = 5.073345
    constants[91] = 4.227788
    constants[92] = 0.4932479
    constants[93] = 0.4932479
    constants[94] = 0.4932479
    constants[95] = 0.13
    constants[96] = 0.05507
    constants[97] = 0.09129
    constants[98] = 0.15602
    constants[99] = 1.8
    constants[100] = 0.58155
    constants[101] = 0.68372
    constants[102] = 0.832299
    states[22] = 2.76087
    states[23] = 4.41135
    states[24] = 4.992799
    states[25] = 4.22047
    states[26] = 8.55228
    states[27] = 7.8362
    states[28] = 8.213955
    states[29] = 8.76758
    constants[103] = (constants[24]/constants[23])*60.0000
    constants[104] = constants[60]-constants[19]
    constants[105] = constants[21]*(power((1.00000*1.00000)/constants[23], 1.0/2))*7.74597
    constants[106] = 60.0000/constants[23]
    constants[107] = constants[22]*(power(1.00000/constants[23], 1.0/2))*7.74597
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[26] = states[17]/constants[78]-(constants[61]*1.00000)/(exp(states[17]/constants[62])-1.00000)
    algebraic[27] = algebraic[26]+constants[60]
    algebraic[29] = states[18]/constants[79]-(constants[61]*1.00000)/(exp(states[18]/constants[62])-1.00000)
    algebraic[30] = algebraic[29]+constants[60]
    algebraic[31] = (algebraic[27]-algebraic[30])/constants[73]
    algebraic[32] = states[19]/constants[80]-(constants[61]*1.00000)/(exp(states[19]/constants[62])-1.00000)
    algebraic[33] = algebraic[32]+constants[60]
    algebraic[34] = (algebraic[30]-algebraic[33])/constants[74]
    rates[18] = algebraic[31]-algebraic[34]
    algebraic[35] = (algebraic[27]-algebraic[33])/constants[72]
    rates[17] = (states[21]-algebraic[35])-algebraic[31]
    algebraic[36] = constants[41]*log((states[10]-constants[43])/constants[42]+1.00000, 10)
    algebraic[37] = constants[45]*exp(constants[48]*(states[10]-constants[43]))+constants[46]*(power(states[10]-constants[43], 2.00000))
    algebraic[38] = constants[66]*algebraic[36]+(1.00000-constants[66])*algebraic[37]
    rates[5] = (algebraic[38]-states[5])/constants[59]
    algebraic[39] = states[11]/constants[37]-(constants[61]*1.00000)/(exp(states[11]/constants[62])-1.00000)
    algebraic[40] = (algebraic[39]-algebraic[38])/constants[31]
    rates[11] = states[7]-algebraic[40]
    algebraic[44] = constants[34]+constants[47]*exp(4.00000*constants[66])+constants[47]*(power(constants[44]/states[10], 2.00000))
    algebraic[41] = states[12]/constants[38]-(constants[61]*1.00000)/(exp(states[12]/constants[62])-1.00000)
    algebraic[46] = (algebraic[38]-algebraic[41])/algebraic[44]
    rates[10] = algebraic[40]-algebraic[46]
    algebraic[42] = constants[49]*log(constants[50]/states[13]-0.990000, 10)*-1.00000
    algebraic[43] = (algebraic[41]-algebraic[42])/constants[32]
    rates[12] = algebraic[46]-algebraic[43]
    algebraic[45] = custom_piecewise([greater(states[14] , constants[56]), (constants[51]+constants[53]*exp(constants[56]/constants[58])+(constants[52]*(states[14]-constants[56]))/1.00000)-constants[61]/(exp(states[14]/constants[62])-1.00000) , True, (constants[51]+constants[53]*exp(states[14]/constants[58]))-constants[61]/(exp(states[14]/constants[62])-1.00000)])
    algebraic[47] = algebraic[45]+constants[60]
    algebraic[48] = (algebraic[42]-algebraic[47])/constants[33]
    rates[13] = algebraic[43]-algebraic[48]
    algebraic[49] = (((((constants[30]*constants[27]*states[6]-constants[30]*constants[27]*states[7]*0.0600000)+((states[9]*constants[27])/constants[36])*0.0600000)-((constants[27]*constants[61])/(exp(states[9]/constants[62])-1.00000))*0.0600000)+algebraic[47]*constants[30]*0.0600000)/(constants[27]+constants[30]))*16.6667
    rates[7] = ((algebraic[49]-states[7]*constants[28])-algebraic[39])/constants[40]
    rates[6] = (((states[4]-states[6]*constants[26]*16.6667)-algebraic[49])/constants[39])*0.0600000
    algebraic[51] = (algebraic[49]-algebraic[47])/constants[27]
    rates[9] = ((states[6]-states[7]*0.0600000)-algebraic[51]*0.0600000)*16.6667
    rates[8] = ((states[4]-states[8]/constants[35])+(constants[61]*1.00000)/(exp(states[8]/constants[62])-1.00000))/constants[29]
    rates[16] = (states[20]-states[21]*0.0600000)*16.6667
    algebraic[60] = (rates[16]*constants[69]+constants[60]+states[16]/constants[77])-(constants[61]*1.00000)/(exp(states[16]/constants[62])-1.00000)
    rates[21] = ((algebraic[60]-algebraic[27])-states[21]*constants[71])/constants[82]
    algebraic[53] = states[22]+states[23]+states[24]+states[25]+states[26]+states[27]+states[28]+states[29]
    algebraic[62] = states[1]+states[0]+states[3]+states[2]+constants[86]+constants[20]+algebraic[53]
    algebraic[63] = constants[83]*exp((algebraic[62]-constants[85])/constants[84])-(constants[61]*1.00000)/(exp(algebraic[62]/constants[63])-1.00000)
    algebraic[64] = algebraic[63]+constants[60]
    algebraic[25] = states[27]/constants[100]-(constants[65]*1.00000)/(exp(states[27]/constants[64])-1.00000)
    algebraic[71] = algebraic[25]+algebraic[64]
    algebraic[23] = states[28]/constants[101]-(constants[65]*1.00000)/(exp(states[28]/constants[64])-1.00000)
    algebraic[68] = algebraic[23]+algebraic[64]
    algebraic[73] = (algebraic[71]-algebraic[68])/constants[92]
    algebraic[21] = states[29]/constants[102]-(constants[61]*1.00000)/(exp(states[29]/constants[62])-1.00000)
    algebraic[67] = algebraic[21]+algebraic[64]
    algebraic[69] = (algebraic[68]-algebraic[67])/constants[93]
    rates[28] = algebraic[73]-algebraic[69]
    algebraic[5] = voi-floor(voi/constants[106])*constants[106]
    algebraic[9] = algebraic[5]
    algebraic[10] = custom_piecewise([greater_equal(algebraic[9] , 0.00000) & less_equal(algebraic[9] , constants[107]), (1.00000-cos(( pi*algebraic[9])/constants[107]))/2.00000 , less(algebraic[9] , 1.50000*constants[107]) & greater_equal(algebraic[9] , constants[107]), (1.00000+cos((2.00000* pi*(algebraic[9]-constants[107]))/constants[107]))/2.00000 , True, 0.00000])
    algebraic[11] = algebraic[10]
    algebraic[14] = (constants[15]-constants[16])*algebraic[11]+constants[16]
    algebraic[70] = (1.00000-algebraic[11])*(constants[6]-constants[7])+constants[7]
    algebraic[72] = (states[0]-algebraic[70])*algebraic[14]-(constants[61]*1.00000)/(exp(states[0]/constants[62])-1.00000)
    algebraic[74] = algebraic[72]+algebraic[64]
    algebraic[76] = (algebraic[67]-algebraic[74])/constants[94]
    rates[29] = algebraic[69]-algebraic[76]
    algebraic[16] = (constants[17]-constants[18])*algebraic[10]+constants[18]
    algebraic[55] = (1.00000-algebraic[10])*(constants[4]-constants[5])+constants[5]
    algebraic[57] = (states[2]-algebraic[55])*algebraic[16]-(constants[61]*1.00000)/(exp(states[2]/constants[62])-1.00000)
    algebraic[75] = algebraic[57]+algebraic[64]
    algebraic[77] = (algebraic[33]-algebraic[75])/constants[75]
    rates[19] = (algebraic[34]+algebraic[35])-algebraic[77]
    algebraic[52] = constants[54]*(power(constants[57]/states[14], 2.00000))+constants[55]
    algebraic[78] = (algebraic[47]-algebraic[74])/algebraic[52]
    rates[14] = (algebraic[48]+algebraic[51])-algebraic[78]
    algebraic[7] = algebraic[5]-constants[10]
    algebraic[12] = custom_piecewise([greater_equal(algebraic[7] , 0.00000) & less_equal(algebraic[7] , constants[105]), (1.00000-cos(( pi*algebraic[7])/constants[105]))/2.00000 , less(algebraic[7] , 1.50000*constants[105]) & greater_equal(algebraic[7] , constants[105]), (1.00000+cos((2.00000* pi*(algebraic[7]-constants[105]))/constants[105]))/2.00000 , True, 0.00000])
    algebraic[17] = (constants[11]-constants[12])*algebraic[12]+constants[12]
    algebraic[58] = (1.00000-algebraic[12])*(constants[0]-constants[1])+constants[1]
    algebraic[59] = (states[3]-algebraic[58])*algebraic[17]-(constants[61]*1.00000)/(exp(states[3]/constants[62])-1.00000)
    algebraic[79] = algebraic[59]+algebraic[64]
    algebraic[80] = custom_piecewise([greater(algebraic[75] , algebraic[79]), (algebraic[75]-algebraic[79])/constants[9] , True, 0.00000])
    rates[2] = algebraic[77]-algebraic[80]
    algebraic[83] = custom_piecewise([greater(algebraic[79] , states[4]), (algebraic[79]-states[4])/constants[25] , True, 0.00000])
    algebraic[18] = states[4]
    algebraic[20] = states[23]/constants[96]-(constants[65]*1.00000)/(exp(states[23]/constants[64])-1.00000)
    algebraic[65] = algebraic[20]+algebraic[64]
    algebraic[66] = (algebraic[18]-algebraic[65])/constants[87]
    rates[4] = (((algebraic[83]-rates[8])-states[6]*16.6667)-algebraic[66])*(1.00000/constants[95]+((constants[61]/1.00000)*exp(states[22]/constants[64]))/(power(exp(states[22]/constants[64])-1.00000, 2.00000)))
    rates[22] = ((algebraic[83]-rates[8])-states[6]*16.6667)-algebraic[66]
    rates[3] = algebraic[80]-algebraic[83]
    algebraic[82] = fabs((algebraic[79]-algebraic[64])/2.00000)
    algebraic[19] = states[26]/constants[99]-(constants[65]*1.00000)/(exp(states[26]/constants[64])-1.00000)
    algebraic[85] = algebraic[19]+algebraic[82]
    algebraic[87] = (algebraic[85]-algebraic[71])/constants[91]
    rates[27] = algebraic[87]-algebraic[73]
    algebraic[13] = algebraic[12]
    algebraic[15] = (constants[13]-constants[14])*algebraic[13]+constants[14]
    algebraic[81] = (1.00000-algebraic[13])*(constants[2]-constants[3])+constants[3]
    algebraic[84] = (states[1]-algebraic[81])*algebraic[15]-(constants[61]*1.00000)/(exp(states[1]/constants[62])-1.00000)
    algebraic[86] = algebraic[84]+algebraic[64]
    algebraic[88] = custom_piecewise([greater(algebraic[74] , algebraic[86]), (algebraic[74]-algebraic[86])/constants[8] , True, 0.00000])
    rates[0] = (algebraic[78]-algebraic[88])+algebraic[76]
    algebraic[22] = states[24]/constants[97]-(constants[65]*1.00000)/(exp(states[24]/constants[64])-1.00000)
    algebraic[89] = algebraic[22]+algebraic[82]
    algebraic[91] = (algebraic[65]-algebraic[89])/constants[88]
    rates[23] = algebraic[66]-algebraic[91]
    algebraic[90] = (((((constants[67]*states[15])/constants[76]-(constants[67]*constants[61]*1.00000)/(exp(states[15]/constants[62])-1.00000))+algebraic[86]*constants[68])-constants[67]*constants[68]*states[20]*16.6667)+constants[60]*constants[67])/(constants[68]+constants[67])
    algebraic[28] = ((states[15]/constants[76]+constants[60])-constants[68]*states[20]*16.6667)-(constants[61]*1.00000)/(exp(states[15]/constants[62])-1.00000)
    algebraic[92] = custom_piecewise([greater(algebraic[86] , algebraic[90]), algebraic[90] , True, algebraic[28]])
    rates[20] = (((algebraic[92]-algebraic[60])-states[20]*constants[70]*16.6667)/constants[81])*0.0600000
    algebraic[24] = states[25]/constants[98]-(constants[65]*1.00000)/(exp(states[25]/constants[64])-1.00000)
    algebraic[93] = algebraic[24]+algebraic[82]
    algebraic[96] = (algebraic[89]-algebraic[93])/constants[89]
    rates[24] = algebraic[91]-algebraic[96]
    algebraic[94] = custom_piecewise([greater(algebraic[86] , algebraic[92]), (algebraic[86]-algebraic[92])/constants[67] , True, 0.00000])
    rates[15] = algebraic[94]-states[20]*16.6667
    rates[1] = algebraic[88]-algebraic[94]
    algebraic[97] = (algebraic[93]-algebraic[85])/constants[90]
    rates[26] = algebraic[97]-algebraic[87]
    rates[25] = algebraic[96]-algebraic[97]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[26] = states[17]/constants[78]-(constants[61]*1.00000)/(exp(states[17]/constants[62])-1.00000)
    algebraic[27] = algebraic[26]+constants[60]
    algebraic[29] = states[18]/constants[79]-(constants[61]*1.00000)/(exp(states[18]/constants[62])-1.00000)
    algebraic[30] = algebraic[29]+constants[60]
    algebraic[31] = (algebraic[27]-algebraic[30])/constants[73]
    algebraic[32] = states[19]/constants[80]-(constants[61]*1.00000)/(exp(states[19]/constants[62])-1.00000)
    algebraic[33] = algebraic[32]+constants[60]
    algebraic[34] = (algebraic[30]-algebraic[33])/constants[74]
    algebraic[35] = (algebraic[27]-algebraic[33])/constants[72]
    algebraic[36] = constants[41]*log((states[10]-constants[43])/constants[42]+1.00000, 10)
    algebraic[37] = constants[45]*exp(constants[48]*(states[10]-constants[43]))+constants[46]*(power(states[10]-constants[43], 2.00000))
    algebraic[38] = constants[66]*algebraic[36]+(1.00000-constants[66])*algebraic[37]
    algebraic[39] = states[11]/constants[37]-(constants[61]*1.00000)/(exp(states[11]/constants[62])-1.00000)
    algebraic[40] = (algebraic[39]-algebraic[38])/constants[31]
    algebraic[44] = constants[34]+constants[47]*exp(4.00000*constants[66])+constants[47]*(power(constants[44]/states[10], 2.00000))
    algebraic[41] = states[12]/constants[38]-(constants[61]*1.00000)/(exp(states[12]/constants[62])-1.00000)
    algebraic[46] = (algebraic[38]-algebraic[41])/algebraic[44]
    algebraic[42] = constants[49]*log(constants[50]/states[13]-0.990000, 10)*-1.00000
    algebraic[43] = (algebraic[41]-algebraic[42])/constants[32]
    algebraic[45] = custom_piecewise([greater(states[14] , constants[56]), (constants[51]+constants[53]*exp(constants[56]/constants[58])+(constants[52]*(states[14]-constants[56]))/1.00000)-constants[61]/(exp(states[14]/constants[62])-1.00000) , True, (constants[51]+constants[53]*exp(states[14]/constants[58]))-constants[61]/(exp(states[14]/constants[62])-1.00000)])
    algebraic[47] = algebraic[45]+constants[60]
    algebraic[48] = (algebraic[42]-algebraic[47])/constants[33]
    algebraic[49] = (((((constants[30]*constants[27]*states[6]-constants[30]*constants[27]*states[7]*0.0600000)+((states[9]*constants[27])/constants[36])*0.0600000)-((constants[27]*constants[61])/(exp(states[9]/constants[62])-1.00000))*0.0600000)+algebraic[47]*constants[30]*0.0600000)/(constants[27]+constants[30]))*16.6667
    algebraic[51] = (algebraic[49]-algebraic[47])/constants[27]
    algebraic[60] = (rates[16]*constants[69]+constants[60]+states[16]/constants[77])-(constants[61]*1.00000)/(exp(states[16]/constants[62])-1.00000)
    algebraic[53] = states[22]+states[23]+states[24]+states[25]+states[26]+states[27]+states[28]+states[29]
    algebraic[62] = states[1]+states[0]+states[3]+states[2]+constants[86]+constants[20]+algebraic[53]
    algebraic[63] = constants[83]*exp((algebraic[62]-constants[85])/constants[84])-(constants[61]*1.00000)/(exp(algebraic[62]/constants[63])-1.00000)
    algebraic[64] = algebraic[63]+constants[60]
    algebraic[25] = states[27]/constants[100]-(constants[65]*1.00000)/(exp(states[27]/constants[64])-1.00000)
    algebraic[71] = algebraic[25]+algebraic[64]
    algebraic[23] = states[28]/constants[101]-(constants[65]*1.00000)/(exp(states[28]/constants[64])-1.00000)
    algebraic[68] = algebraic[23]+algebraic[64]
    algebraic[73] = (algebraic[71]-algebraic[68])/constants[92]
    algebraic[21] = states[29]/constants[102]-(constants[61]*1.00000)/(exp(states[29]/constants[62])-1.00000)
    algebraic[67] = algebraic[21]+algebraic[64]
    algebraic[69] = (algebraic[68]-algebraic[67])/constants[93]
    algebraic[5] = voi-floor(voi/constants[106])*constants[106]
    algebraic[9] = algebraic[5]
    algebraic[10] = custom_piecewise([greater_equal(algebraic[9] , 0.00000) & less_equal(algebraic[9] , constants[107]), (1.00000-cos(( pi*algebraic[9])/constants[107]))/2.00000 , less(algebraic[9] , 1.50000*constants[107]) & greater_equal(algebraic[9] , constants[107]), (1.00000+cos((2.00000* pi*(algebraic[9]-constants[107]))/constants[107]))/2.00000 , True, 0.00000])
    algebraic[11] = algebraic[10]
    algebraic[14] = (constants[15]-constants[16])*algebraic[11]+constants[16]
    algebraic[70] = (1.00000-algebraic[11])*(constants[6]-constants[7])+constants[7]
    algebraic[72] = (states[0]-algebraic[70])*algebraic[14]-(constants[61]*1.00000)/(exp(states[0]/constants[62])-1.00000)
    algebraic[74] = algebraic[72]+algebraic[64]
    algebraic[76] = (algebraic[67]-algebraic[74])/constants[94]
    algebraic[16] = (constants[17]-constants[18])*algebraic[10]+constants[18]
    algebraic[55] = (1.00000-algebraic[10])*(constants[4]-constants[5])+constants[5]
    algebraic[57] = (states[2]-algebraic[55])*algebraic[16]-(constants[61]*1.00000)/(exp(states[2]/constants[62])-1.00000)
    algebraic[75] = algebraic[57]+algebraic[64]
    algebraic[77] = (algebraic[33]-algebraic[75])/constants[75]
    algebraic[52] = constants[54]*(power(constants[57]/states[14], 2.00000))+constants[55]
    algebraic[78] = (algebraic[47]-algebraic[74])/algebraic[52]
    algebraic[7] = algebraic[5]-constants[10]
    algebraic[12] = custom_piecewise([greater_equal(algebraic[7] , 0.00000) & less_equal(algebraic[7] , constants[105]), (1.00000-cos(( pi*algebraic[7])/constants[105]))/2.00000 , less(algebraic[7] , 1.50000*constants[105]) & greater_equal(algebraic[7] , constants[105]), (1.00000+cos((2.00000* pi*(algebraic[7]-constants[105]))/constants[105]))/2.00000 , True, 0.00000])
    algebraic[17] = (constants[11]-constants[12])*algebraic[12]+constants[12]
    algebraic[58] = (1.00000-algebraic[12])*(constants[0]-constants[1])+constants[1]
    algebraic[59] = (states[3]-algebraic[58])*algebraic[17]-(constants[61]*1.00000)/(exp(states[3]/constants[62])-1.00000)
    algebraic[79] = algebraic[59]+algebraic[64]
    algebraic[80] = custom_piecewise([greater(algebraic[75] , algebraic[79]), (algebraic[75]-algebraic[79])/constants[9] , True, 0.00000])
    algebraic[83] = custom_piecewise([greater(algebraic[79] , states[4]), (algebraic[79]-states[4])/constants[25] , True, 0.00000])
    algebraic[18] = states[4]
    algebraic[20] = states[23]/constants[96]-(constants[65]*1.00000)/(exp(states[23]/constants[64])-1.00000)
    algebraic[65] = algebraic[20]+algebraic[64]
    algebraic[66] = (algebraic[18]-algebraic[65])/constants[87]
    algebraic[82] = fabs((algebraic[79]-algebraic[64])/2.00000)
    algebraic[19] = states[26]/constants[99]-(constants[65]*1.00000)/(exp(states[26]/constants[64])-1.00000)
    algebraic[85] = algebraic[19]+algebraic[82]
    algebraic[87] = (algebraic[85]-algebraic[71])/constants[91]
    algebraic[13] = algebraic[12]
    algebraic[15] = (constants[13]-constants[14])*algebraic[13]+constants[14]
    algebraic[81] = (1.00000-algebraic[13])*(constants[2]-constants[3])+constants[3]
    algebraic[84] = (states[1]-algebraic[81])*algebraic[15]-(constants[61]*1.00000)/(exp(states[1]/constants[62])-1.00000)
    algebraic[86] = algebraic[84]+algebraic[64]
    algebraic[88] = custom_piecewise([greater(algebraic[74] , algebraic[86]), (algebraic[74]-algebraic[86])/constants[8] , True, 0.00000])
    algebraic[22] = states[24]/constants[97]-(constants[65]*1.00000)/(exp(states[24]/constants[64])-1.00000)
    algebraic[89] = algebraic[22]+algebraic[82]
    algebraic[91] = (algebraic[65]-algebraic[89])/constants[88]
    algebraic[90] = (((((constants[67]*states[15])/constants[76]-(constants[67]*constants[61]*1.00000)/(exp(states[15]/constants[62])-1.00000))+algebraic[86]*constants[68])-constants[67]*constants[68]*states[20]*16.6667)+constants[60]*constants[67])/(constants[68]+constants[67])
    algebraic[28] = ((states[15]/constants[76]+constants[60])-constants[68]*states[20]*16.6667)-(constants[61]*1.00000)/(exp(states[15]/constants[62])-1.00000)
    algebraic[92] = custom_piecewise([greater(algebraic[86] , algebraic[90]), algebraic[90] , True, algebraic[28]])
    algebraic[24] = states[25]/constants[98]-(constants[65]*1.00000)/(exp(states[25]/constants[64])-1.00000)
    algebraic[93] = algebraic[24]+algebraic[82]
    algebraic[96] = (algebraic[89]-algebraic[93])/constants[89]
    algebraic[94] = custom_piecewise([greater(algebraic[86] , algebraic[92]), (algebraic[86]-algebraic[92])/constants[67] , True, 0.00000])
    algebraic[97] = (algebraic[93]-algebraic[85])/constants[90]
    algebraic[0] = states[4]-constants[60]
    algebraic[1] = states[8]+states[9]+states[10]+states[11]
    algebraic[2] = states[13]+states[14]
    algebraic[3] = states[15]+states[16]+states[17]
    algebraic[4] = states[19]
    algebraic[6] = custom_piecewise([greater(voi , algebraic[5]) & less(voi , algebraic[5]+0.0200000), 5.00000 , greater(voi , algebraic[5]+constants[10]) & less(voi , algebraic[5]+constants[10]+0.0200000), 10.0000 , True, 0.00000])
    algebraic[8] = algebraic[0]
    algebraic[50] = algebraic[49]-constants[19]
    algebraic[54] = states[0]+states[1]+states[15]+states[16]+states[17]+states[18]+states[19]+states[2]+states[3]+states[8]+states[9]+states[10]+states[11]+states[12]+states[13]+states[14]+constants[86]+algebraic[53]
    algebraic[56] = algebraic[54]-constants[86]
    algebraic[61] = algebraic[60]-constants[60]
    algebraic[95] = algebraic[92]-constants[60]
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
        self.Vlvrd = 72
        self.Vlvrs = 23
        self.Vrvrd = 103
        self.Vrvrs = 53
        self.Vlard = 10
        self.Vlars = 8
        self.Vrard = 10
        self.Vrars = 8
        self.Rra = 0.001
        self.Rla = 0.001
        self.PRint = 0.12
        self.Emaxlv = 5.6
        self.Eminlv = 0.186874659
        self.Emaxrv = 0.67
        self.Eminrv = 0.1041640922
        self.Emaxra = 0.1091675077
        self.Eminra = 0.0992431888
        self.Emaxla = 0.1446191772
        self.Eminla = 0.1314719793
        self.Pbs = 0
        self.Vmyo = 238
        self.TsvK = 0.35
        self.TsaK = 0.2
        self.HR = 77
        self.COutput = 108.56912706
        self.Rav = 1e-4
        self.Raop = 1e-4
        self.Rcrb = 6.8284472205
        self.Raod = 0.025
        self.Rtaop = 0.2
        self.Rtaod = 0.3
        self.Rsap = 0.025
        self.Rsc = 0.1545054945
        self.Rsv = 0.1381298227
        self.Rsao = 0.5508058134
        self.Caop = 0.3445734208
        self.Caod = 1.4544677036
        self.Csap = 1.4843409851
        self.Csc = 7.9822364317
        self.Laop = 3.5e-4
        self.Laod = 3.5e-4
        self.Kc = 497.7852450367
        self.Do = 50
        self.Vsa_o = 485.7624931891
        self.Vsa_max = 577.7106000108
        self.Kp1 = 0.03
        self.Kp2 = 0.05
        self.Kr = 0.01
        self.tau_p = 0.1
        self.Kv = 21.83
        self.Vmax_sv = 3379.545
        self.D2 = -5
        self.K1 = 0.0968305478
        self.K2 = 0.4
        self.KR = 0.001
        self.Ro = 0.025
        self.Vo = 129.6486
        self.Vmax_vc = 350.5314
        self.Vmin_vc = 50.010747
        self.COtau = 15
        self.Pplc = -5.6
        self.Px2 = 2
        self.Vx8 = 8
        self.Vx75 = 75
        self.Vx1 = 1
        self.Px1 = 1
        self.F_vaso = 0.5
        self.Rpuv = 1e-4
        self.Rtpap = 0.05
        self.Rtpad = 0.05
        self.Rpap = 1e-4
        self.Rpad = 0.03
        self.Rps = 4.2958026137
        self.Rpa = 0.0565149137
        self.Rpc = 0.0309026688
        self.Rpv = 1e-4
        self.Ctpap = 1.5365929068
        self.Ctpad = 2.6893667388
        self.Cpa = 3.1321449506
        self.Cpc = 7.7147
        self.Cpv = 27.87028922
        self.Lpa = 1.801907e-4
        self.Lpad = 1.932239e-4
        self.K_pcd = 1
        self.phi_pcd = 40
        self.Vpcd_o = 785
        self.perifl = 15
        self.Rcorao = 2.642367
        self.Rcorea = 2.642367
        self.Rcorla = 5.073345
        self.Rcorsa = 5.073345
        self.Rcorcap = 4.227788
        self.Rcorsv = 0.4932479
        self.Rcorlv = 0.4932479
        self.Rcorev = 0.4932479
        self.Ccorao = 0.13
        self.Ccorea = 0.05507
        self.Ccorla = 0.09129
        self.Ccorsa = 0.15602
        self.Ccorcap = 1.8
        self.Ccorsv = 0.58155
        self.Ccorlv = 0.68372
        self.Ccorev = 0.832299

    def to_dict(self):
        return {
            "Vlvrd": self.Vlvrd,
            "Vlvrs": self.Vlvrs,
            "Vrvrd": self.Vrvrd,
            "Vrvrs": self.Vrvrs,
            "Vlard": self.Vlard,
            "Vlars": self.Vlars,
            "Vrard": self.Vrard,
            "Vrars": self.Vrars,
            "Rra": self.Rra,
            "Rla": self.Rla,
            "PRint": self.PRint,
            "Emaxlv": self.Emaxlv,
            "Eminlv": self.Eminlv,
            "Emaxrv": self.Emaxrv,
            "Eminrv": self.Eminrv,
            "Emaxra": self.Emaxra,
            "Eminra": self.Eminra,
            "Emaxla": self.Emaxla,
            "Eminla": self.Eminla,
            "Pbs": self.Pbs,
            "Vmyo": self.Vmyo,
            "TsvK": self.TsvK,
            "TsaK": self.TsaK,
            "HR": self.HR,
            "COutput": self.COutput,
            "Rav": self.Rav,
            "Raop": self.Raop,
            "Rcrb": self.Rcrb,
            "Raod": self.Raod,
            "Rtaop": self.Rtaop,
            "Rtaod": self.Rtaod,
            "Rsap": self.Rsap,
            "Rsc": self.Rsc,
            "Rsv": self.Rsv,
            "Rsao": self.Rsao,
            "Caop": self.Caop,
            "Caod": self.Caod,
            "Csap": self.Csap,
            "Csc": self.Csc,
            "Laop": self.Laop,
            "Laod": self.Laod,
            "Kc": self.Kc,
            "Do": self.Do,
            "Vsa_o": self.Vsa_o,
            "Vsa_max": self.Vsa_max,
            "Kp1": self.Kp1,
            "Kp2": self.Kp2,
            "Kr": self.Kr,
            "tau_p": self.tau_p,
            "Kv": self.Kv,
            "Vmax_sv": self.Vmax_sv,
            "D2": self.D2,
            "K1": self.K1,
            "K2": self.K2,
            "KR": self.KR,
            "Ro": self.Ro,
            "Vo": self.Vo,
            "Vmax_vc": self.Vmax_vc,
            "Vmin_vc": self.Vmin_vc,
            "COtau": self.COtau,
            "Pplc": self.Pplc,
            "Px2": self.Px2,
            "Vx8": self.Vx8,
            "Vx75": self.Vx75,
            "Vx1": self.Vx1,
            "Px1": self.Px1,
            "F_vaso": self.F_vaso,
            "Rpuv": self.Rpuv,
            "Rtpap": self.Rtpap,
            "Rtpad": self.Rtpad,
            "Rpap": self.Rpap,
            "Rpad": self.Rpad,
            "Rps": self.Rps,
            "Rpa": self.Rpa,
            "Rpc": self.Rpc,
            "Rpv": self.Rpv,
            "Ctpap": self.Ctpap,
            "Ctpad": self.Ctpad,
            "Cpa": self.Cpa,
            "Cpc": self.Cpc,
            "Cpv": self.Cpv,
            "Lpa": self.Lpa,
            "Lpad": self.Lpad,
            "K_pcd": self.K_pcd,
            "phi_pcd": self.phi_pcd,
            "Vpcd_o": self.Vpcd_o,
            "perifl": self.perifl,
            "Rcorao": self.Rcorao,
            "Rcorea": self.Rcorea,
            "Rcorla": self.Rcorla,
            "Rcorsa": self.Rcorsa,
            "Rcorcap": self.Rcorcap,
            "Rcorsv": self.Rcorsv,
            "Rcorlv": self.Rcorlv,
            "Rcorev": self.Rcorev,
            "Ccorao": self.Ccorao,
            "Ccorea": self.Ccorea,
            "Ccorla": self.Ccorla,
            "Ccorsa": self.Ccorsa,
            "Ccorcap": self.Ccorcap,
            "Ccorsv": self.Ccorsv,
            "Ccorlv": self.Ccorlv,
            "Ccorev": self.Ccorev,
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
        y0=[78.2537, 167.4806, 85.9126, 125.360568, 87.93968, 90.6179, 0.698577, 23.5957, 31.1705, 138.4476, 519.7915, 129.6439, 256.8555, 2961.6507, 232.46638962, 33.1398, 60.11203897, 58.926, 107.57022, 293.0398, 1.2282, 57.1876, 2.76087, 4.41135, 4.992799, 4.22047, 8.55228, 7.8362, 8.213955, 8.76758],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "lpc"
        self.curve_names = [
            "Vra",
            "Vrv",
            "Vla",
            "Vlv",
            "Paopc",
            "MAP",
            "Faop",
            "Faod",
            "Vaop",
            "Vaod",
            "Vsa",
            "Vsap",
            "Vsc",
            "Vsv",
            "Vvc",
            "Vpap",
            "Vpad",
            "Vpa",
            "Vpc",
            "Vpv",
            "Fpap",
            "Fpad",
            "Vcorao",
            "Vcorea",
            "Vcorla",
            "Vcorsa",
            "Vcorcap",
            "Vcorsv",
            "Vcorlv",
            "Vcorev",
        ]
        self.state_names = ['Vra', 'Vrv', 'Vla', 'Vlv', 'Paopc', 'MAP', 'Faop', 'Faod', 'Vaop', 'Vaod', 'Vsa', 'Vsap', 'Vsc', 'Vsv', 'Vvc', 'Vpap', 'Vpad', 'Vpa', 'Vpc', 'Vpv', 'Fpap', 'Fpad', 'Vcorao', 'Vcorea', 'Vcorla', 'Vcorsa', 'Vcorcap', 'Vcorsv', 'Vcorlv', 'Vcorev']
        self.algebraic_names = ['Paop', 'SysArtVol', 'SysVenVol', 'PulArtVol', 'PulVenVol', 'beattime', 'P_QRSwave', 'trelv', 'Pcorao', 'trela', 'yla', 'yra', 'ylv', 'yrv', 'Era', 'Erv', 'Ela', 'Elv', 'Pcoraoc', 'Pcorcap', 'Pcorea', 'Pcorev', 'Pcorla', 'Pcorlv', 'Pcorsa', 'Pcorsv', 'Ppa', 'Ppac', 'Ppapc2', 'Ppc', 'Ppcc', 'Fpa', 'Ppv', 'Ppvc', 'Fpc', 'Fps', 'Psa_a', 'Psa_p', 'Psa', 'Psap', 'Fsap', 'Psc', 'Psv', 'Fsc', 'Rsa', 'Pvc', 'Fsa', 'Pvcc', 'Fsv', 'Paodc', 'Paod', 'Fcrb', 'Rvc', 'Vcorcirc', 'Vtot', 'Vlar', 'VBcirc', 'Pla', 'Vlvr', 'Plv', 'Ppadc', 'Ppad', 'Vpcd', 'Ppcd', 'Ppcdc', 'Pcoreac', 'Fcorao', 'Pcorevc', 'Pcorlvc', 'Fcorlv', 'Vrar', 'Pcorsvc', 'Pra', 'Fcorsv', 'Prac', 'Plac', 'Fcorev', 'Fpv', 'Fvc', 'Plvc', 'Fla', 'Vrvr', 'Pcorisfc', 'Flv', 'Prv', 'Pcorcapc', 'Prvc', 'Fcorcap', 'Fra', 'Pcorlac', 'Ppapc1', 'Fcorea', 'Ppapc', 'Pcorsac', 'Frv', 'Ppap', 'Fcorla', 'Fcorsa']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 108
        p = self.params

        # direct mapping
        c[0] = p.Vlvrd
        c[1] = p.Vlvrs
        c[2] = p.Vrvrd
        c[3] = p.Vrvrs
        c[4] = p.Vlard
        c[5] = p.Vlars
        c[6] = p.Vrard
        c[7] = p.Vrars
        c[8] = p.Rra
        c[9] = p.Rla
        c[10] = p.PRint
        c[11] = p.Emaxlv
        c[12] = p.Eminlv
        c[13] = p.Emaxrv
        c[14] = p.Eminrv
        c[15] = p.Emaxra
        c[16] = p.Eminra
        c[17] = p.Emaxla
        c[18] = p.Eminla
        c[19] = p.Pbs
        c[20] = p.Vmyo
        c[21] = p.TsvK
        c[22] = p.TsaK
        c[23] = p.HR
        c[24] = p.COutput
        c[25] = p.Rav
        c[26] = p.Raop
        c[27] = p.Rcrb
        c[28] = p.Raod
        c[29] = p.Rtaop
        c[30] = p.Rtaod
        c[31] = p.Rsap
        c[32] = p.Rsc
        c[33] = p.Rsv
        c[34] = p.Rsao
        c[35] = p.Caop
        c[36] = p.Caod
        c[37] = p.Csap
        c[38] = p.Csc
        c[39] = p.Laop
        c[40] = p.Laod
        c[41] = p.Kc
        c[42] = p.Do
        c[43] = p.Vsa_o
        c[44] = p.Vsa_max
        c[45] = p.Kp1
        c[46] = p.Kp2
        c[47] = p.Kr
        c[48] = p.tau_p
        c[49] = p.Kv
        c[50] = p.Vmax_sv
        c[51] = p.D2
        c[52] = p.K1
        c[53] = p.K2
        c[54] = p.KR
        c[55] = p.Ro
        c[56] = p.Vo
        c[57] = p.Vmax_vc
        c[58] = p.Vmin_vc
        c[59] = p.COtau
        c[60] = p.Pplc
        c[61] = p.Px2
        c[62] = p.Vx8
        c[63] = p.Vx75
        c[64] = p.Vx1
        c[65] = p.Px1
        c[66] = p.F_vaso
        c[67] = p.Rpuv
        c[68] = p.Rtpap
        c[69] = p.Rtpad
        c[70] = p.Rpap
        c[71] = p.Rpad
        c[72] = p.Rps
        c[73] = p.Rpa
        c[74] = p.Rpc
        c[75] = p.Rpv
        c[76] = p.Ctpap
        c[77] = p.Ctpad
        c[78] = p.Cpa
        c[79] = p.Cpc
        c[80] = p.Cpv
        c[81] = p.Lpa
        c[82] = p.Lpad
        c[83] = p.K_pcd
        c[84] = p.phi_pcd
        c[85] = p.Vpcd_o
        c[86] = p.perifl
        c[87] = p.Rcorao
        c[88] = p.Rcorea
        c[89] = p.Rcorla
        c[90] = p.Rcorsa
        c[91] = p.Rcorcap
        c[92] = p.Rcorsv
        c[93] = p.Rcorlv
        c[94] = p.Rcorev
        c[95] = p.Ccorao
        c[96] = p.Ccorea
        c[97] = p.Ccorla
        c[98] = p.Ccorsa
        c[99] = p.Ccorcap
        c[100] = p.Ccorsv
        c[101] = p.Ccorlv
        c[102] = p.Ccorev

        # derived constants
        c[103] = (c[24]/c[23])*60.0000
        c[104] = c[60]-c[19]
        c[105] = c[21]*(power((1.00000*1.00000)/c[23], 1.0/2))*7.74597
        c[106] = 60.0000/c[23]
        c[107] = c[22]*(power(1.00000/c[23], 1.0/2))*7.74597

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
