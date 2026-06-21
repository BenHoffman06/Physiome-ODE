# Size of variable arrays:
sizeAlgebraic = 24
sizeStates = 33
sizeConstants = 97
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (hour)"
    legend_states[0] = "ATbl in component ATbl (nanomole)"
    legend_constants[0] = "k2T in component ATbl (nmol_hr)"
    legend_algebraic[17] = "Qb in component model_parameters (l_hr)"
    legend_algebraic[15] = "Qp in component Qp (l_hr)"
    legend_constants[1] = "Ql in component model_parameters (l_hr)"
    legend_constants[2] = "Qt in component model_parameters (l_hr)"
    legend_constants[94] = "CTbf in component model_parameters (nM)"
    legend_algebraic[0] = "CTblf in component CTblf (nM)"
    legend_algebraic[10] = "CTpf in component CTpf (nM)"
    legend_constants[3] = "CTbl in component model_parameters (nM)"
    legend_constants[90] = "CTlf in component CTlf (nM)"
    legend_constants[93] = "CTtv in component CTtv (nM)"
    legend_constants[4] = "ts in component model_parameters (dimensionless)"
    legend_states[1] = "ADbl in component ADbl (nanomole)"
    legend_algebraic[18] = "Qbt in component model_parameters (l_hr)"
    legend_constants[95] = "CDbf in component model_parameters (nM)"
    legend_algebraic[4] = "CDblf in component CDblf (nM)"
    legend_algebraic[12] = "CDpf in component CDpf (nM)"
    legend_constants[92] = "CDlf in component CDlf (nM)"
    legend_constants[5] = "CDbl in component model_parameters (nM)"
    legend_states[2] = "CT_A in component CT_A (nM)"
    legend_constants[6] = "kTA_on in component CT_A (second_order_rate_constant)"
    legend_constants[7] = "kTA_off in component CT_A (first_order_rate_constant)"
    legend_algebraic[8] = "CAf in component CAf (nM)"
    legend_states[3] = "CD_A in component CD_A (nM)"
    legend_constants[8] = "kDA_on in component CD_A (second_order_rate_constant)"
    legend_constants[9] = "kDA_off in component CD_A (first_order_rate_constant)"
    legend_constants[10] = "CA in component model_parameters (nM)"
    legend_states[4] = "ATl in component ATl (nanomole)"
    legend_constants[11] = "k1T in component model_parameters (first_order_rate_constant)"
    legend_constants[12] = "km5alpha in component model_parameters (nM)"
    legend_constants[13] = "Vmax1 in component model_parameters (nmol_hr)"
    legend_constants[14] = "PTl in component model_parameters (dimensionless)"
    legend_states[5] = "ADl in component ADl (nanomole)"
    legend_constants[15] = "k1D in component model_parameters (first_order_rate_constant)"
    legend_constants[16] = "PDl in component model_parameters (dimensionless)"
    legend_constants[17] = "CTl in component model_parameters (nM)"
    legend_constants[18] = "CDl in component model_parameters (nM)"
    legend_states[6] = "ATif in component ATif (nanomole)"
    legend_constants[19] = "mu in component model_parameters (l_hr)"
    legend_constants[20] = "PTif in component model_parameters (dimensionless)"
    legend_constants[21] = "CTif in component model_parameters (nM)"
    legend_constants[22] = "CTst in component model_parameters (nM)"
    legend_constants[23] = "CLH in component model_parameters (nanomole)"
    legend_constants[24] = "PTst in component model_parameters (dimensionless)"
    legend_states[7] = "ATst in component ATst (nanomole)"
    legend_states[8] = "ATp in component ATp (nanomole)"
    legend_constants[25] = "Vmax0 in component model_parameters (nmol_hr)"
    legend_states[9] = "ADp in component ADp (nanomole)"
    legend_states[10] = "CT_R in component CT_R (nM)"
    legend_constants[26] = "kTR_on in component CT_R (second_order_rate_constant)"
    legend_constants[27] = "kTR_off in component CT_R (first_order_rate_constant)"
    legend_algebraic[23] = "CRf in component CRf (nM)"
    legend_states[11] = "CD_R in component CD_R (nM)"
    legend_constants[28] = "kDR_on in component CD_R (second_order_rate_constant)"
    legend_constants[29] = "kDR_off in component CD_R (first_order_rate_constant)"
    legend_states[12] = "CDT in component CDT (nM)"
    legend_constants[30] = "kDT_on in component CDT (second_order_rate_constant)"
    legend_constants[31] = "kDT_off in component CDT (first_order_rate_constant)"
    legend_states[13] = "CDD in component CDD (nM)"
    legend_constants[32] = "kDD_on in component CDD (second_order_rate_constant)"
    legend_constants[33] = "kDD_off in component CDD (first_order_rate_constant)"
    legend_states[14] = "CTT in component CTT (nM)"
    legend_constants[34] = "kTT_on in component CTT (second_order_rate_constant)"
    legend_constants[35] = "kTT_off in component CTT (first_order_rate_constant)"
    legend_states[15] = "CDD5a in component CDD5a (nM)"
    legend_constants[36] = "kDNA_onDD5a in component CDD5a (second_order_rate_constant)"
    legend_constants[37] = "kDNA_offDD5a in component CDD5a (first_order_rate_constant)"
    legend_algebraic[19] = "CDNA5af in component CDNA5af (nM)"
    legend_states[16] = "CDDcd in component CDDcd (nM)"
    legend_constants[38] = "kDNA_onDDcd in component CDDcd (second_order_rate_constant)"
    legend_constants[39] = "kDNA_offDDcd in component CDDcd (first_order_rate_constant)"
    legend_algebraic[14] = "CDNAcdf in component CDNAcdf (nM)"
    legend_states[17] = "CDDsec in component CDDsec (nM)"
    legend_constants[40] = "kDNA_onDDsec in component CDDsec (second_order_rate_constant)"
    legend_constants[41] = "kDNA_offDDsec in component CDDsec (first_order_rate_constant)"
    legend_algebraic[16] = "CDNAsecf in component CDNAsecf (nM)"
    legend_states[18] = "CDDcp in component CDDcp (nM)"
    legend_constants[42] = "kDNA_onDDcp in component CDDcp (second_order_rate_constant)"
    legend_constants[43] = "kDNA_offDDcp in component CDDcp (first_order_rate_constant)"
    legend_algebraic[20] = "CDNAcpf in component CDNAcpf (nM)"
    legend_states[19] = "CDT5a in component CDT5a (nM)"
    legend_constants[44] = "kDNA_onDT5a in component CDT5a (second_order_rate_constant)"
    legend_constants[45] = "kDNA_offDT5a in component CDT5a (first_order_rate_constant)"
    legend_states[20] = "CDTcd in component CDTcd (nM)"
    legend_constants[46] = "kDNA_onDTcd in component CDTcd (second_order_rate_constant)"
    legend_constants[47] = "kDNA_offDTcd in component CDTcd (first_order_rate_constant)"
    legend_states[21] = "CDTsec in component CDTsec (nM)"
    legend_constants[48] = "kDNA_onDTsec in component CDTsec (second_order_rate_constant)"
    legend_constants[49] = "kDNA_offDTsec in component CDTsec (first_order_rate_constant)"
    legend_states[22] = "CDTcp in component CDTcp (nM)"
    legend_constants[50] = "kDNA_onDTcp in component CDTcp (second_order_rate_constant)"
    legend_constants[51] = "kDNA_offDTcp in component CDTcp (first_order_rate_constant)"
    legend_states[23] = "CTT5a in component CTT5a (nM)"
    legend_constants[52] = "kDNA_onTT5a in component CTT5a (second_order_rate_constant)"
    legend_constants[53] = "kDNA_offTT5a in component CTT5a (first_order_rate_constant)"
    legend_states[24] = "CTTcd in component CTTcd (nM)"
    legend_constants[54] = "kDNA_onTTcd in component CTTcd (second_order_rate_constant)"
    legend_constants[55] = "kDNA_offTTcd in component CTTcd (first_order_rate_constant)"
    legend_states[25] = "CTTsec in component CTTsec (nM)"
    legend_constants[56] = "kDNA_onTTsec in component CTTsec (second_order_rate_constant)"
    legend_constants[57] = "kDNA_offTTsec in component CTTsec (first_order_rate_constant)"
    legend_states[26] = "CTTcp in component CTTcp (nM)"
    legend_constants[58] = "kDNA_onTTcp in component CTTcp (second_order_rate_constant)"
    legend_constants[59] = "kDNA_offTTcp in component CTTcp (first_order_rate_constant)"
    legend_algebraic[7] = "T in component CTpf (nM)"
    legend_constants[60] = "NTp in component CTpf (dimensionless)"
    legend_constants[61] = "CTp in component model_parameters (nM)"
    legend_algebraic[11] = "D in component CDpf (nM)"
    legend_constants[62] = "NDp in component CDpf (dimensionless)"
    legend_constants[63] = "CDp in component model_parameters (nM)"
    legend_algebraic[22] = "CR in component CR (nM)"
    legend_constants[64] = "CDNAcd in component model_parameters (nM)"
    legend_constants[65] = "CDNAsec in component model_parameters (nM)"
    legend_constants[66] = "CDNA5a in component model_parameters (nM)"
    legend_constants[67] = "CDNAcp in component model_parameters (nM)"
    legend_algebraic[1] = "DNAocp in component DNAocp (dimensionless)"
    legend_algebraic[2] = "DNAosec in component DNAosec (dimensionless)"
    legend_algebraic[5] = "DNAocd in component DNAocd (dimensionless)"
    legend_algebraic[3] = "DNAo5a in component DNAo5a (dimensionless)"
    legend_states[27] = "ATb in component ATb (nanomole)"
    legend_constants[68] = "CTb in component model_parameters (nM)"
    legend_constants[69] = "PTb in component model_parameters (dimensionless)"
    legend_states[28] = "ADb in component ADb (nanomole)"
    legend_constants[70] = "CDb in component model_parameters (nM)"
    legend_constants[71] = "PDb in component model_parameters (dimensionless)"
    legend_states[29] = "ALH in component ALH (nanomole)"
    legend_constants[72] = "kLH1 in component ALH (l_hr)"
    legend_constants[73] = "kLH2 in component ALH (nmol_hr)"
    legend_constants[74] = "kLH3 in component ALH (nmol_hr)"
    legend_constants[75] = "kLH4 in component ALH (first_order_rate_constant)"
    legend_constants[76] = "alpha_T in component ALH (dimensionless)"
    legend_constants[77] = "alpha_D in component ALH (dimensionless)"
    legend_algebraic[9] = "A in component ALH (nmol_hr)"
    legend_constants[91] = "B in component ALH (nmol_hr)"
    legend_states[30] = "AR in component AR (nanomole)"
    legend_constants[78] = "k1R in component AR (nmol_hr)"
    legend_constants[79] = "keR in component AR (l_hr)"
    legend_algebraic[21] = "Vp in component Vp (litre)"
    legend_constants[80] = "kQp in component Qp (first_order_rate_constant)"
    legend_algebraic[13] = "Vpc in component Qp (litre)"
    legend_states[31] = "VPC1 in component VPC1 (litre)"
    legend_constants[81] = "VPC2 in component model_parameters (litre)"
    legend_algebraic[6] = "Vmax in component Vmax (nmol_hr)"
    legend_constants[82] = "k5a in component Vmax (nmol_hr)"
    legend_constants[83] = "kcpl in component VPC1 (kg_hr)"
    legend_constants[84] = "kcd1 in component VPC1 (first_order_rate_constant)"
    legend_constants[85] = "VPC1b in component model_parameters (kg)"
    legend_states[32] = "VPL1 in component VPL1 (litre)"
    legend_constants[86] = "ksec in component VPL1 (kg_hr)"
    legend_constants[87] = "kflo in component VPL1 (first_order_rate_constant)"
    legend_constants[88] = "VPL2 in component model_parameters (litre)"
    legend_constants[89] = "Qc in component model_parameters (l_hr)"
    legend_rates[0] = "d/dt ATbl in component ATbl (nanomole)"
    legend_rates[1] = "d/dt ADbl in component ADbl (nanomole)"
    legend_rates[2] = "d/dt CT_A in component CT_A (nM)"
    legend_rates[3] = "d/dt CD_A in component CD_A (nM)"
    legend_rates[4] = "d/dt ATl in component ATl (nanomole)"
    legend_rates[5] = "d/dt ADl in component ADl (nanomole)"
    legend_rates[6] = "d/dt ATif in component ATif (nanomole)"
    legend_rates[7] = "d/dt ATst in component ATst (nanomole)"
    legend_rates[8] = "d/dt ATp in component ATp (nanomole)"
    legend_rates[9] = "d/dt ADp in component ADp (nanomole)"
    legend_rates[10] = "d/dt CT_R in component CT_R (nM)"
    legend_rates[11] = "d/dt CD_R in component CD_R (nM)"
    legend_rates[12] = "d/dt CDT in component CDT (nM)"
    legend_rates[13] = "d/dt CDD in component CDD (nM)"
    legend_rates[14] = "d/dt CTT in component CTT (nM)"
    legend_rates[15] = "d/dt CDD5a in component CDD5a (nM)"
    legend_rates[16] = "d/dt CDDcd in component CDDcd (nM)"
    legend_rates[17] = "d/dt CDDsec in component CDDsec (nM)"
    legend_rates[18] = "d/dt CDDcp in component CDDcp (nM)"
    legend_rates[19] = "d/dt CDT5a in component CDT5a (nM)"
    legend_rates[20] = "d/dt CDTcd in component CDTcd (nM)"
    legend_rates[21] = "d/dt CDTsec in component CDTsec (nM)"
    legend_rates[22] = "d/dt CDTcp in component CDTcp (nM)"
    legend_rates[23] = "d/dt CTT5a in component CTT5a (nM)"
    legend_rates[24] = "d/dt CTTcd in component CTTcd (nM)"
    legend_rates[25] = "d/dt CTTsec in component CTTsec (nM)"
    legend_rates[26] = "d/dt CTTcp in component CTTcp (nM)"
    legend_rates[27] = "d/dt ATb in component ATb (nanomole)"
    legend_rates[28] = "d/dt ADb in component ADb (nanomole)"
    legend_rates[29] = "d/dt ALH in component ALH (nanomole)"
    legend_rates[30] = "d/dt AR in component AR (nanomole)"
    legend_rates[31] = "d/dt VPC1 in component VPC1 (litre)"
    legend_rates[32] = "d/dt VPL1 in component VPL1 (litre)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 0.0
    constants[0] = 0.17
    constants[1] = 1.06
    constants[2] = 0.061
    constants[3] = 7.60
    constants[4] = 0.56
    states[1] = 0.0
    constants[5] = 0.59
    states[2] = 0.0
    constants[6] = 0.18
    constants[7] = 8131.0
    states[3] = 0.0
    constants[8] = 0.15
    constants[9] = 5407.0
    constants[10] = 5.00E5
    states[4] = 0.0
    constants[11] = 87.93
    constants[12] = 40.00
    constants[13] = 3.65
    constants[14] = 2.75
    states[5] = 0.0
    constants[15] = 77.20
    constants[16] = 2.00
    constants[17] = 9.92
    constants[18] = 0.92
    states[6] = 0.0
    constants[19] = 1000.0
    constants[20] = 1.96
    constants[21] = 307.29
    constants[22] = 307.29
    constants[23] = 0.104
    constants[24] = 1.00
    states[7] = 0.0
    states[8] = 0.0
    constants[25] = 2.89
    states[9] = 0.0
    states[10] = 0.0
    constants[26] = 0.14
    constants[27] = 0.069
    states[11] = 0.0
    constants[28] = 0.053
    constants[29] = 0.018
    states[12] = 0.0
    constants[30] = 0.14
    constants[31] = 3.13
    states[13] = 0.0
    constants[32] = 0.14
    constants[33] = 3.13
    states[14] = 0.0
    constants[34] = 0.14
    constants[35] = 3.13
    states[15] = 0.0
    constants[36] = 0.14
    constants[37] = 0.07
    states[16] = 0.0
    constants[38] = 0.14
    constants[39] = 0.1
    states[17] = 0.0
    constants[40] = 0.14
    constants[41] = 0.2
    states[18] = 0.0
    constants[42] = 0.14
    constants[43] = 0.7
    states[19] = 0.0
    constants[44] = 0.14
    constants[45] = 0.56
    states[20] = 0.0
    constants[46] = 0.14
    constants[47] = 0.8
    states[21] = 0.0
    constants[48] = 0.14
    constants[49] = 1.6
    states[22] = 0.0
    constants[50] = 0.14
    constants[51] = 5.6
    states[23] = 0.0
    constants[52] = 0.14
    constants[53] = 0.84
    states[24] = 0.0
    constants[54] = 0.14
    constants[55] = 1.2
    states[25] = 0.0
    constants[56] = 0.14
    constants[57] = 2.4
    states[26] = 0.0
    constants[58] = 0.14
    constants[59] = 8.4
    constants[60] = 0.79
    constants[61] = 11.38
    constants[62] = 1.00
    constants[63] = 52.46
    constants[64] = 0.075
    constants[65] = 0.075
    constants[66] = 0.075
    constants[67] = 0.075
    states[27] = 0.0
    constants[68] = 0.6275
    constants[69] = 1.00
    states[28] = 0.0
    constants[70] = 0.019884
    constants[71] = 0.62
    states[29] = 0.0
    constants[72] = 0.13
    constants[73] = 0.026
    constants[74] = 1.68E-4
    constants[75] = 0.80
    constants[76] = 0.25
    constants[77] = 0.75
    states[30] = 0.0
    constants[78] = 68.15
    constants[79] = 71.90
    constants[80] = 73.84
    states[31] = 0.0
    constants[81] = 5.08E-5
    constants[82] = 3.02
    constants[83] = 1.17E-7
    constants[84] = 0.014
    constants[85] = 1E-4
    states[32] = 0.0
    constants[86] = 8.44E-6
    constants[87] = 0.043
    constants[88] = 3.08E-6
    constants[89] = 6.08
    constants[90] = constants[17]/constants[14]
    constants[91] = constants[74]
    constants[96] = constants[19]*(constants[21]-constants[22]/constants[24])
    constants[92] = constants[18]/constants[16]
    constants[93] = constants[21]/constants[20]
    constants[94] = constants[68]/constants[69]
    constants[95] = constants[70]/constants[71]
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[7] = constants[96]
    rates[4] = constants[1]*(constants[3]-constants[90])-((constants[13]*constants[90])/(constants[12]+constants[90])+constants[11]*(states[4]/constants[14]))
    rates[5] = constants[1]*(constants[5]-constants[92])-((constants[13]*constants[90])/(constants[12]+constants[90])+constants[15]*(states[5]/constants[16]))
    rates[12] = constants[30]*states[11]*states[10]-constants[31]*states[12]
    rates[13] = constants[32]*(power(states[11], 2.00000))-constants[33]*states[13]
    rates[14] = constants[34]*(power(states[10], 2.00000))-constants[35]*states[14]
    algebraic[0] = constants[3]-states[2]
    rates[6] = constants[2]*(1.00000-constants[4])*(algebraic[0]-constants[21]/constants[20])+constants[19]*(constants[22]/constants[24]-constants[21])+constants[11]*constants[23]
    algebraic[2] = (states[25]+states[17]+states[21])/constants[65]
    rates[32] = (states[31]/constants[85])*constants[86]*algebraic[2]-constants[87]*states[32]
    algebraic[1] = (states[26]+states[18]+states[22])/constants[67]
    algebraic[5] = (states[24]+states[16]+states[20])/constants[64]
    rates[31] = (states[31]/constants[85])*constants[83]*algebraic[1]-constants[84]*(1.00000-algebraic[5])*states[31]
    algebraic[8] = constants[10]-(states[2]+states[3])
    rates[2] = constants[6]*algebraic[0]*algebraic[8]-constants[7]*states[2]
    algebraic[4] = constants[5]-states[3]
    rates[3] = constants[8]*algebraic[4]*algebraic[8]-constants[9]*states[3]
    algebraic[9] = -constants[72]*(constants[76]*algebraic[0]+constants[77]*algebraic[4])+constants[73]
    rates[29] = custom_piecewise([greater(algebraic[9] , constants[91]), algebraic[9]-constants[75]*states[29] , True, constants[91]-constants[75]*states[29]])
    algebraic[14] = constants[64]-(states[24]+states[16]+states[20])
    rates[16] = constants[38]*states[13]*algebraic[14]-constants[39]*states[16]
    rates[20] = constants[46]*states[12]*algebraic[14]-constants[47]*states[20]
    rates[24] = constants[54]*states[14]*algebraic[14]-constants[55]*states[24]
    algebraic[13] = states[31]+constants[81]
    algebraic[15] = constants[80]*algebraic[13]
    algebraic[7] = states[25]+states[21]+states[23]+states[19]+states[24]+states[20]+states[26]+states[22]
    algebraic[10] = (constants[61]-(states[10]+2.00000*states[14]+states[12]+algebraic[7]))/(1.00000+constants[60])
    rates[8] = algebraic[15]*(constants[3]-algebraic[10])-(constants[25]*algebraic[10])/(constants[12]+algebraic[10])
    algebraic[11] = states[17]+states[21]+states[15]+states[19]+states[16]+states[20]+states[18]+states[22]
    algebraic[12] = (constants[63]-(states[11]+2.00000*states[13]+states[12]+algebraic[11]))/(1.00000+constants[62])
    rates[9] = algebraic[15]*(constants[5]-algebraic[12])-(constants[25]*algebraic[10])/(constants[12]+algebraic[10])
    algebraic[16] = constants[65]-(states[25]+states[17]+states[21])
    rates[17] = constants[40]*states[13]*algebraic[16]-constants[41]*states[17]
    rates[21] = constants[48]*states[12]*algebraic[16]-constants[49]*states[21]
    rates[25] = constants[56]*states[14]*algebraic[16]-constants[57]*states[25]
    algebraic[17] = constants[89]-(algebraic[15]+constants[2]+constants[1])
    rates[0] = algebraic[17]*(constants[94]-algebraic[0])+algebraic[15]*(algebraic[10]-constants[3])+constants[1]*(constants[90]-constants[3])+constants[2]*(1.00000-constants[4])*(constants[93]-algebraic[0])+constants[0]
    algebraic[18] = constants[89]-(algebraic[15]+constants[1])
    rates[1] = algebraic[18]*(constants[95]-algebraic[4])+algebraic[15]*(algebraic[12]-algebraic[4])+constants[1]*(constants[92]-constants[5])
    algebraic[19] = constants[66]-(states[23]+states[15]+states[19])
    rates[15] = constants[36]*states[13]*algebraic[19]-constants[37]*states[15]
    rates[19] = constants[44]*states[12]*algebraic[19]-constants[45]*states[19]
    rates[23] = constants[52]*states[14]*algebraic[19]-constants[53]*states[23]
    rates[27] = algebraic[17]*(algebraic[0]-constants[68]/constants[69])
    rates[28] = algebraic[18]*(algebraic[4]-constants[70]/constants[71])
    algebraic[20] = constants[67]-(states[26]+states[18]+states[22])
    rates[18] = constants[42]*states[13]*algebraic[20]-constants[43]*states[18]
    rates[22] = constants[50]*states[12]*algebraic[20]-constants[51]*states[22]
    rates[26] = constants[58]*states[14]*algebraic[20]-constants[59]*states[26]
    algebraic[21] = states[31]+constants[81]+states[32]+constants[88]
    algebraic[22] = states[30]/algebraic[21]
    algebraic[23] = algebraic[22]-(states[10]+states[11]+2.00000*(states[14]+states[13]+states[12])+2.00000*(algebraic[14]+algebraic[16]+algebraic[20]+algebraic[19]))
    rates[10] = constants[26]*algebraic[10]*algebraic[23]-constants[27]*states[10]
    rates[11] = constants[28]*algebraic[12]*algebraic[23]-constants[29]*states[11]
    rates[30] = constants[78]-constants[79]*algebraic[23]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = constants[3]-states[2]
    algebraic[2] = (states[25]+states[17]+states[21])/constants[65]
    algebraic[1] = (states[26]+states[18]+states[22])/constants[67]
    algebraic[5] = (states[24]+states[16]+states[20])/constants[64]
    algebraic[8] = constants[10]-(states[2]+states[3])
    algebraic[4] = constants[5]-states[3]
    algebraic[9] = -constants[72]*(constants[76]*algebraic[0]+constants[77]*algebraic[4])+constants[73]
    algebraic[14] = constants[64]-(states[24]+states[16]+states[20])
    algebraic[13] = states[31]+constants[81]
    algebraic[15] = constants[80]*algebraic[13]
    algebraic[7] = states[25]+states[21]+states[23]+states[19]+states[24]+states[20]+states[26]+states[22]
    algebraic[10] = (constants[61]-(states[10]+2.00000*states[14]+states[12]+algebraic[7]))/(1.00000+constants[60])
    algebraic[11] = states[17]+states[21]+states[15]+states[19]+states[16]+states[20]+states[18]+states[22]
    algebraic[12] = (constants[63]-(states[11]+2.00000*states[13]+states[12]+algebraic[11]))/(1.00000+constants[62])
    algebraic[16] = constants[65]-(states[25]+states[17]+states[21])
    algebraic[17] = constants[89]-(algebraic[15]+constants[2]+constants[1])
    algebraic[18] = constants[89]-(algebraic[15]+constants[1])
    algebraic[19] = constants[66]-(states[23]+states[15]+states[19])
    algebraic[20] = constants[67]-(states[26]+states[18]+states[22])
    algebraic[21] = states[31]+constants[81]+states[32]+constants[88]
    algebraic[22] = states[30]/algebraic[21]
    algebraic[23] = algebraic[22]-(states[10]+states[11]+2.00000*(states[14]+states[13]+states[12])+2.00000*(algebraic[14]+algebraic[16]+algebraic[20]+algebraic[19]))
    algebraic[3] = (states[23]+states[15]+states[19])/constants[66]
    algebraic[6] = constants[82]*algebraic[3]
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
        self.k2T = 0.17
        self.Ql = 1.06
        self.Qt = 0.061
        self.CTbl = 7.60
        self.ts = 0.56
        self.CDbl = 0.59
        self.kTA_on = 0.18
        self.kTA_off = 8131.0
        self.kDA_on = 0.15
        self.kDA_off = 5407.0
        self.CA = 5.00E5
        self.k1T = 87.93
        self.km5alpha = 40.00
        self.Vmax1 = 3.65
        self.PTl = 2.75
        self.k1D = 77.20
        self.PDl = 2.00
        self.CTl = 9.92
        self.CDl = 0.92
        self.mu = 1000.0
        self.PTif = 1.96
        self.CTif = 307.29
        self.CTst = 307.29
        self.CLH = 0.104
        self.PTst = 1.00
        self.Vmax0 = 2.89
        self.kTR_on = 0.14
        self.kTR_off = 0.069
        self.kDR_on = 0.053
        self.kDR_off = 0.018
        self.kDT_on = 0.14
        self.kDT_off = 3.13
        self.kDD_on = 0.14
        self.kDD_off = 3.13
        self.kTT_on = 0.14
        self.kTT_off = 3.13
        self.kDNA_onDD5a = 0.14
        self.kDNA_offDD5a = 0.07
        self.kDNA_onDDcd = 0.14
        self.kDNA_offDDcd = 0.1
        self.kDNA_onDDsec = 0.14
        self.kDNA_offDDsec = 0.2
        self.kDNA_onDDcp = 0.14
        self.kDNA_offDDcp = 0.7
        self.kDNA_onDT5a = 0.14
        self.kDNA_offDT5a = 0.56
        self.kDNA_onDTcd = 0.14
        self.kDNA_offDTcd = 0.8
        self.kDNA_onDTsec = 0.14
        self.kDNA_offDTsec = 1.6
        self.kDNA_onDTcp = 0.14
        self.kDNA_offDTcp = 5.6
        self.kDNA_onTT5a = 0.14
        self.kDNA_offTT5a = 0.84
        self.kDNA_onTTcd = 0.14
        self.kDNA_offTTcd = 1.2
        self.kDNA_onTTsec = 0.14
        self.kDNA_offTTsec = 2.4
        self.kDNA_onTTcp = 0.14
        self.kDNA_offTTcp = 8.4
        self.NTp = 0.79
        self.CTp = 11.38
        self.NDp = 1.00
        self.CDp = 52.46
        self.CDNAcd = 0.075
        self.CDNAsec = 0.075
        self.CDNA5a = 0.075
        self.CDNAcp = 0.075
        self.CTb = 0.6275
        self.PTb = 1.00
        self.CDb = 0.019884
        self.PDb = 0.62
        self.kLH1 = 0.13
        self.kLH2 = 0.026
        self.kLH3 = 1.68E-4
        self.kLH4 = 0.80
        self.alpha_T = 0.25
        self.alpha_D = 0.75
        self.k1R = 68.15
        self.keR = 71.90
        self.kQp = 73.84
        self.VPC2 = 5.08E-5
        self.k5a = 3.02
        self.kcpl = 1.17E-7
        self.kcd1 = 0.014
        self.VPC1b = 1E-4
        self.ksec = 8.44E-6
        self.kflo = 0.043
        self.VPL2 = 3.08E-6
        self.Qc = 6.08

    def to_dict(self):
        return {
            "k2T": self.k2T,
            "Ql": self.Ql,
            "Qt": self.Qt,
            "CTbl": self.CTbl,
            "ts": self.ts,
            "CDbl": self.CDbl,
            "kTA_on": self.kTA_on,
            "kTA_off": self.kTA_off,
            "kDA_on": self.kDA_on,
            "kDA_off": self.kDA_off,
            "CA": self.CA,
            "k1T": self.k1T,
            "km5alpha": self.km5alpha,
            "Vmax1": self.Vmax1,
            "PTl": self.PTl,
            "k1D": self.k1D,
            "PDl": self.PDl,
            "CTl": self.CTl,
            "CDl": self.CDl,
            "mu": self.mu,
            "PTif": self.PTif,
            "CTif": self.CTif,
            "CTst": self.CTst,
            "CLH": self.CLH,
            "PTst": self.PTst,
            "Vmax0": self.Vmax0,
            "kTR_on": self.kTR_on,
            "kTR_off": self.kTR_off,
            "kDR_on": self.kDR_on,
            "kDR_off": self.kDR_off,
            "kDT_on": self.kDT_on,
            "kDT_off": self.kDT_off,
            "kDD_on": self.kDD_on,
            "kDD_off": self.kDD_off,
            "kTT_on": self.kTT_on,
            "kTT_off": self.kTT_off,
            "kDNA_onDD5a": self.kDNA_onDD5a,
            "kDNA_offDD5a": self.kDNA_offDD5a,
            "kDNA_onDDcd": self.kDNA_onDDcd,
            "kDNA_offDDcd": self.kDNA_offDDcd,
            "kDNA_onDDsec": self.kDNA_onDDsec,
            "kDNA_offDDsec": self.kDNA_offDDsec,
            "kDNA_onDDcp": self.kDNA_onDDcp,
            "kDNA_offDDcp": self.kDNA_offDDcp,
            "kDNA_onDT5a": self.kDNA_onDT5a,
            "kDNA_offDT5a": self.kDNA_offDT5a,
            "kDNA_onDTcd": self.kDNA_onDTcd,
            "kDNA_offDTcd": self.kDNA_offDTcd,
            "kDNA_onDTsec": self.kDNA_onDTsec,
            "kDNA_offDTsec": self.kDNA_offDTsec,
            "kDNA_onDTcp": self.kDNA_onDTcp,
            "kDNA_offDTcp": self.kDNA_offDTcp,
            "kDNA_onTT5a": self.kDNA_onTT5a,
            "kDNA_offTT5a": self.kDNA_offTT5a,
            "kDNA_onTTcd": self.kDNA_onTTcd,
            "kDNA_offTTcd": self.kDNA_offTTcd,
            "kDNA_onTTsec": self.kDNA_onTTsec,
            "kDNA_offTTsec": self.kDNA_offTTsec,
            "kDNA_onTTcp": self.kDNA_onTTcp,
            "kDNA_offTTcp": self.kDNA_offTTcp,
            "NTp": self.NTp,
            "CTp": self.CTp,
            "NDp": self.NDp,
            "CDp": self.CDp,
            "CDNAcd": self.CDNAcd,
            "CDNAsec": self.CDNAsec,
            "CDNA5a": self.CDNA5a,
            "CDNAcp": self.CDNAcp,
            "CTb": self.CTb,
            "PTb": self.PTb,
            "CDb": self.CDb,
            "PDb": self.PDb,
            "kLH1": self.kLH1,
            "kLH2": self.kLH2,
            "kLH3": self.kLH3,
            "kLH4": self.kLH4,
            "alpha_T": self.alpha_T,
            "alpha_D": self.alpha_D,
            "k1R": self.k1R,
            "keR": self.keR,
            "kQp": self.kQp,
            "VPC2": self.VPC2,
            "k5a": self.k5a,
            "kcpl": self.kcpl,
            "kcd1": self.kcd1,
            "VPC1b": self.VPC1b,
            "ksec": self.ksec,
            "kflo": self.kflo,
            "VPL2": self.VPL2,
            "Qc": self.Qc,
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
        y0=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "potter_zager_barton_2006"
        self.curve_names = [
            "ATbl",
            "ADbl",
            "CT_A",
            "CD_A",
            "ATl",
            "ADl",
            "ATif",
            "ATst",
            "ATp",
            "ADp",
            "CT_R",
            "CD_R",
            "CDT",
            "CDD",
            "CTT",
            "CDD5a",
            "CDDcd",
            "CDDsec",
            "CDDcp",
            "CDT5a",
            "CDTcd",
            "CDTsec",
            "CDTcp",
            "CTT5a",
            "CTTcd",
            "CTTsec",
            "CTTcp",
            "ATb",
            "ADb",
            "ALH",
            "AR",
            "VPC1",
            "VPL1",
        ]
        self.state_names = ['ATbl', 'ADbl', 'CT_A', 'CD_A', 'ATl', 'ADl', 'ATif', 'ATst', 'ATp', 'ADp', 'CT_R', 'CD_R', 'CDT', 'CDD', 'CTT', 'CDD5a', 'CDDcd', 'CDDsec', 'CDDcp', 'CDT5a', 'CDTcd', 'CDTsec', 'CDTcp', 'CTT5a', 'CTTcd', 'CTTsec', 'CTTcp', 'ATb', 'ADb', 'ALH', 'AR', 'VPC1', 'VPL1']
        self.algebraic_names = ['CTblf', 'DNAocp', 'DNAosec', 'DNAo5a', 'CDblf', 'DNAocd', 'Vmax', 'T', 'CAf', 'A', 'CTpf', 'D', 'CDpf', 'Vpc', 'CDNAcdf', 'Qp', 'CDNAsecf', 'Qb', 'Qbt', 'CDNA5af', 'CDNAcpf', 'Vp', 'CR', 'CRf']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 97
        p = self.params

        # direct mapping
        c[0] = p.k2T
        c[1] = p.Ql
        c[2] = p.Qt
        c[3] = p.CTbl
        c[4] = p.ts
        c[5] = p.CDbl
        c[6] = p.kTA_on
        c[7] = p.kTA_off
        c[8] = p.kDA_on
        c[9] = p.kDA_off
        c[10] = p.CA
        c[11] = p.k1T
        c[12] = p.km5alpha
        c[13] = p.Vmax1
        c[14] = p.PTl
        c[15] = p.k1D
        c[16] = p.PDl
        c[17] = p.CTl
        c[18] = p.CDl
        c[19] = p.mu
        c[20] = p.PTif
        c[21] = p.CTif
        c[22] = p.CTst
        c[23] = p.CLH
        c[24] = p.PTst
        c[25] = p.Vmax0
        c[26] = p.kTR_on
        c[27] = p.kTR_off
        c[28] = p.kDR_on
        c[29] = p.kDR_off
        c[30] = p.kDT_on
        c[31] = p.kDT_off
        c[32] = p.kDD_on
        c[33] = p.kDD_off
        c[34] = p.kTT_on
        c[35] = p.kTT_off
        c[36] = p.kDNA_onDD5a
        c[37] = p.kDNA_offDD5a
        c[38] = p.kDNA_onDDcd
        c[39] = p.kDNA_offDDcd
        c[40] = p.kDNA_onDDsec
        c[41] = p.kDNA_offDDsec
        c[42] = p.kDNA_onDDcp
        c[43] = p.kDNA_offDDcp
        c[44] = p.kDNA_onDT5a
        c[45] = p.kDNA_offDT5a
        c[46] = p.kDNA_onDTcd
        c[47] = p.kDNA_offDTcd
        c[48] = p.kDNA_onDTsec
        c[49] = p.kDNA_offDTsec
        c[50] = p.kDNA_onDTcp
        c[51] = p.kDNA_offDTcp
        c[52] = p.kDNA_onTT5a
        c[53] = p.kDNA_offTT5a
        c[54] = p.kDNA_onTTcd
        c[55] = p.kDNA_offTTcd
        c[56] = p.kDNA_onTTsec
        c[57] = p.kDNA_offTTsec
        c[58] = p.kDNA_onTTcp
        c[59] = p.kDNA_offTTcp
        c[60] = p.NTp
        c[61] = p.CTp
        c[62] = p.NDp
        c[63] = p.CDp
        c[64] = p.CDNAcd
        c[65] = p.CDNAsec
        c[66] = p.CDNA5a
        c[67] = p.CDNAcp
        c[68] = p.CTb
        c[69] = p.PTb
        c[70] = p.CDb
        c[71] = p.PDb
        c[72] = p.kLH1
        c[73] = p.kLH2
        c[74] = p.kLH3
        c[75] = p.kLH4
        c[76] = p.alpha_T
        c[77] = p.alpha_D
        c[78] = p.k1R
        c[79] = p.keR
        c[80] = p.kQp
        c[81] = p.VPC2
        c[82] = p.k5a
        c[83] = p.kcpl
        c[84] = p.kcd1
        c[85] = p.VPC1b
        c[86] = p.ksec
        c[87] = p.kflo
        c[88] = p.VPL2
        c[89] = p.Qc

        # derived constants
        c[90] = c[17]/c[14]
        c[91] = c[74]
        c[92] = c[18]/c[16]
        c[93] = c[21]/c[20]
        c[94] = c[68]/c[69]
        c[95] = c[70]/c[71]
        c[96] = c[19]*(c[21]-c[22]/c[24])

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
