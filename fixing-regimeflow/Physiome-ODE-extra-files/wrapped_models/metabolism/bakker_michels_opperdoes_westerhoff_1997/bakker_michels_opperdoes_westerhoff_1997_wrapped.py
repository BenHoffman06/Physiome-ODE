# Size of variable arrays:
sizeAlgebraic = 33
sizeStates = 10
sizeConstants = 61
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (second)"
    legend_constants[0] = "Vc_Vg in component volume_ratio (dimensionless)"
    legend_constants[1] = "Glc_o in component Glc_o (millimolar)"
    legend_states[0] = "Glc_i in component Glc_i (millimolar)"
    legend_algebraic[22] = "V_HK in component V_HK (flux)"
    legend_algebraic[19] = "V_glucose_transport in component V_glucose_transport (flux)"
    legend_algebraic[0] = "Glc_6_P_g in component Glc_6_P_g (millimolar)"
    legend_constants[2] = "Keq_PGI in component Glc_6_P_g (dimensionless)"
    legend_algebraic[1] = "Fru_6_P_g in component Fru_6_P_g (millimolar)"
    legend_states[1] = "hexose_P_g in component hexose_P_g (millimolar)"
    legend_algebraic[29] = "V_PFK in component V_PFK (flux)"
    legend_states[2] = "Fru_1_6_BP_g in component Fru_1_6_BP_g (millimolar)"
    legend_algebraic[32] = "V_ALD in component V_ALD (flux)"
    legend_algebraic[8] = "GA_3_P_g in component GA_3_P_g (millimolar)"
    legend_constants[3] = "Keq_TIM in component DHAP (dimensionless)"
    legend_algebraic[6] = "DHAP_g in component DHAP_g (millimolar)"
    legend_states[3] = "triose_P in component triose_P (millimolar)"
    legend_algebraic[23] = "V_GAPDH in component V_GAPDH (flux)"
    legend_algebraic[27] = "V_GDH in component V_GDH (flux)"
    legend_algebraic[21] = "V_GPO in component V_GPO (flux)"
    legend_states[4] = "one_three_BPGA_g in component one_three_BPGA_g (millimolar)"
    legend_algebraic[24] = "V_PGK in component V_PGK (flux)"
    legend_algebraic[2] = "three_PGA in component three_PGA (millimolar)"
    legend_states[5] = "N in component N (millimolar)"
    legend_constants[4] = "Keq_PGM in component three_PGA (dimensionless)"
    legend_constants[5] = "Keq_ENO in component three_PGA (dimensionless)"
    legend_algebraic[3] = "two_PGA_c in component two_PGA_c (millimolar)"
    legend_algebraic[28] = "V_PYK in component V_PYK (flux)"
    legend_algebraic[4] = "PEP_c in component PEP_c (millimolar)"
    legend_states[6] = "PYR_c in component PYR_c (millimolar)"
    legend_algebraic[20] = "V_pyruvate_transport in component V_pyruvate_transport (flux)"
    legend_constants[6] = "glycerol_g in component glycerol_g (millimolar)"
    legend_algebraic[5] = "DHAP in component DHAP (millimolar)"
    legend_algebraic[7] = "DHAP_c in component DHAP_c (millimolar)"
    legend_algebraic[13] = "Gly_3_P in component Gly_3_P (millimolar)"
    legend_algebraic[10] = "ATP_g in component ATP_g (millimolar)"
    legend_algebraic[12] = "ADP_g in component ADP_g (millimolar)"
    legend_constants[7] = "C4 in component C4 (millimolar)"
    legend_algebraic[14] = "Gly_3_P_c in component Gly_3_P_c (millimolar)"
    legend_algebraic[15] = "Gly_3_P_g in component Gly_3_P_g (millimolar)"
    legend_algebraic[9] = "NAD_g in component NAD_g (millimolar)"
    legend_states[7] = "NADH_g in component NADH_g (millimolar)"
    legend_constants[8] = "C3 in component C3 (millimolar)"
    legend_states[8] = "P_g in component P_g (millimolar)"
    legend_algebraic[25] = "V_GK in component V_GK (flux)"
    legend_states[9] = "P_c in component P_c (millimolar)"
    legend_algebraic[30] = "V_ATP_utilisation in component V_ATP_utilisation (flux)"
    legend_constants[9] = "Keq_AK in component ATP_g (dimensionless)"
    legend_constants[10] = "C1 in component C1 (millimolar)"
    legend_algebraic[11] = "ATP_c in component ATP_c (millimolar)"
    legend_constants[11] = "Keq_AK in component ATP_c (dimensionless)"
    legend_constants[12] = "C2 in component C2 (millimolar)"
    legend_algebraic[16] = "ADP_c in component ADP_c (millimolar)"
    legend_algebraic[17] = "AMP_g in component AMP_g (millimolar)"
    legend_algebraic[18] = "AMP_c in component AMP_c (millimolar)"
    legend_constants[13] = "K_Glc in component V_glucose_transport (millimolar)"
    legend_constants[14] = "alpha in component V_glucose_transport (dimensionless)"
    legend_constants[15] = "V_glucose_transport_max in component V_glucose_transport (flux)"
    legend_constants[16] = "K_pyruvate in component V_pyruvate_transport (millimolar)"
    legend_constants[17] = "V_pyruvate_transport_max in component V_pyruvate_transport (flux)"
    legend_constants[18] = "K_Gly_3_P in component V_GPO (millimolar)"
    legend_constants[19] = "V_GPO_max in component V_GPO (flux)"
    legend_constants[20] = "K_Glc_i in component V_HK (millimolar)"
    legend_constants[21] = "K_ATP in component V_HK (millimolar)"
    legend_constants[22] = "K_ADP in component V_HK (millimolar)"
    legend_constants[23] = "V_HK_max in component V_HK (flux)"
    legend_constants[24] = "K_NAD in component V_GAPDH (millimolar)"
    legend_constants[25] = "K_GA_3_P in component V_GAPDH (millimolar)"
    legend_constants[26] = "K_1_3_BPGA in component V_GAPDH (millimolar)"
    legend_constants[27] = "K_NADH in component V_GAPDH (millimolar)"
    legend_constants[28] = "V_GAPDH_max_plus in component V_GAPDH (flux)"
    legend_constants[29] = "V_GAPDH_max_ratio in component V_GAPDH (dimensionless)"
    legend_constants[30] = "K_ADP in component V_PGK (millimolar)"
    legend_constants[31] = "K_1_3_BPGA in component V_PGK (millimolar)"
    legend_constants[32] = "K_3_PGA in component V_PGK (millimolar)"
    legend_constants[33] = "K_ATP in component V_PGK (millimolar)"
    legend_constants[34] = "V_PGK_max_plus in component V_PGK (flux)"
    legend_constants[35] = "V_PGK_max_ratio in component V_PGK (dimensionless)"
    legend_constants[36] = "K_ADP in component V_GK (millimolar)"
    legend_constants[37] = "K_Gly_3_P in component V_GK (millimolar)"
    legend_constants[38] = "K_glycerol in component V_GK (millimolar)"
    legend_constants[39] = "K_ATP in component V_GK (millimolar)"
    legend_constants[40] = "V_GK_max_plus in component V_GK (flux)"
    legend_constants[41] = "V_GK_max_ratio in component V_GK (dimensionless)"
    legend_constants[42] = "K_NADH in component V_GDH (millimolar)"
    legend_constants[43] = "K_Gly_3_P in component V_GDH (millimolar)"
    legend_constants[44] = "K_DHAP in component V_GDH (millimolar)"
    legend_constants[45] = "K_NAD in component V_GDH (millimolar)"
    legend_constants[46] = "V_GDH_max_plus in component V_GDH (flux)"
    legend_constants[47] = "V_GDH_max_ratio in component V_GDH (dimensionless)"
    legend_constants[48] = "n in component V_PFK (dimensionless)"
    legend_constants[49] = "Km_Fru_6_P in component V_PFK (millimolar)"
    legend_constants[50] = "Km_ATP in component V_PFK (millimolar)"
    legend_constants[51] = "V_PFK_max in component V_PFK (flux)"
    legend_algebraic[26] = "Km_PEP in component V_PYK (millimolar)"
    legend_constants[52] = "Km_ADP in component V_PYK (millimolar)"
    legend_constants[53] = "n in component V_PYK (dimensionless)"
    legend_constants[54] = "V_PYK_max in component V_PYK (flux)"
    legend_algebraic[31] = "Km_Fru_1_6_BP in component V_ALD (millimolar)"
    legend_constants[55] = "Km_GA_3_P in component V_ALD (millimolar)"
    legend_constants[56] = "Ki_GA_3_P in component V_ALD (millimolar)"
    legend_constants[57] = "Km_DHAP in component V_ALD (millimolar)"
    legend_constants[58] = "V_ALD_max_plus in component V_ALD (flux)"
    legend_constants[59] = "V_ALD_max_ratio in component V_ALD (dimensionless)"
    legend_constants[60] = "k in component V_ATP_utilisation (flux)"
    legend_rates[0] = "d/dt Glc_i in component Glc_i (millimolar)"
    legend_rates[1] = "d/dt hexose_P_g in component hexose_P_g (millimolar)"
    legend_rates[2] = "d/dt Fru_1_6_BP_g in component Fru_1_6_BP_g (millimolar)"
    legend_rates[3] = "d/dt triose_P in component triose_P (millimolar)"
    legend_rates[4] = "d/dt one_three_BPGA_g in component one_three_BPGA_g (millimolar)"
    legend_rates[5] = "d/dt N in component N (millimolar)"
    legend_rates[6] = "d/dt PYR_c in component PYR_c (millimolar)"
    legend_rates[7] = "d/dt NADH_g in component NADH_g (millimolar)"
    legend_rates[8] = "d/dt P_g in component P_g (millimolar)"
    legend_rates[9] = "d/dt P_c in component P_c (millimolar)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    constants[0] = 22.3
    constants[1] = 5.0
    states[0] = 0.01
    constants[2] = 0.29
    states[1] = 0.01
    states[2] = 0.01
    constants[3] = 0.045
    states[3] = 0.01
    states[4] = 0.01
    states[5] = 0.01
    constants[4] = 0.187
    constants[5] = 6.7
    states[6] = 0.01
    constants[6] = 0.00
    constants[7] = 120.0
    states[7] = 0.01
    constants[8] = 4.0
    states[8] = 0.01
    states[9] = 0.01
    constants[9] = 0.442
    constants[10] = 3.9
    constants[11] = 0.442
    constants[12] = 3.9
    constants[13] = 2.0
    constants[14] = 0.75
    constants[15] = 106.2
    constants[16] = 1.96
    constants[17] = 160.0
    constants[18] = 1.7
    constants[19] = 200.0
    constants[20] = 0.1
    constants[21] = 0.116
    constants[22] = 0.126
    constants[23] = 625.0
    constants[24] = 0.45
    constants[25] = 0.15
    constants[26] = 0.1
    constants[27] = 0.02
    constants[28] = 1470.0
    constants[29] = 0.67
    constants[30] = 0.1
    constants[31] = 0.05
    constants[32] = 1.62
    constants[33] = 0.29
    constants[34] = 640.0
    constants[35] = 0.029
    constants[36] = 0.12
    constants[37] = 5.1
    constants[38] = 0.12
    constants[39] = 0.19
    constants[40] = 0.0
    constants[41] = 167.0
    constants[42] = 0.01
    constants[43] = 2.0
    constants[44] = 0.1
    constants[45] = 0.4
    constants[46] = 533.0
    constants[47] = 0.28
    constants[48] = 1.2
    constants[49] = 0.82
    constants[50] = 2.6E-2
    constants[51] = 780.0
    constants[52] = 0.114
    constants[53] = 2.5
    constants[54] = 2.6E3
    constants[55] = 6.7E-2
    constants[56] = 9.8E-2
    constants[57] = 1.5E-2
    constants[58] = 780.0
    constants[59] = 1.19
    constants[60] = 50
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[10] = ((constants[10]--(states[8]*(1.00000-4.00000*constants[9])))+power(power(constants[10]--(states[8]*(1.00000-4.00000*constants[9])), 2.00000)-4.00000*(1.00000-4.00000*constants[9])*(-constants[9]*(power(states[8], 2.00000))), 0.500000))/(2.00000*(1.00000-4.00000*constants[9]))
    algebraic[12] = states[8]-2.00000*algebraic[10]
    algebraic[22] = constants[23]*(((algebraic[10]/constants[21])*(states[0]/constants[20]))/((1.00000+algebraic[10]/constants[21]+algebraic[12]/constants[22])*(1.00000+states[0]/constants[20])))
    algebraic[19] = constants[15]*((constants[1]-states[0])/(constants[13]+constants[1]+states[0]+constants[14]*constants[1]*(states[0]/constants[13])))
    rates[0] = algebraic[19]-algebraic[22]
    algebraic[5] = (states[3]*(1.00000+constants[0]))/(1.00000+constants[0]+constants[3])
    algebraic[6] = algebraic[5]
    algebraic[8] = constants[3]*algebraic[6]
    algebraic[9] = constants[8]-states[7]
    algebraic[23] = constants[28]*(((algebraic[8]/constants[25])*(algebraic[9]/constants[24]-constants[29])*(states[4]/constants[26])*(states[7]/constants[27]))/((1.00000+algebraic[8]/constants[25]+states[4]/constants[26])*(1.00000+algebraic[9]/constants[24]+states[7]/constants[27])))
    algebraic[2] = (states[5]*(1.00000+constants[0]))/(1.00000+(1.00000+constants[4]+constants[4]*constants[5])*constants[0])
    algebraic[24] = constants[34]*(((states[4]/constants[31])*(algebraic[12]/constants[30]-constants[35])*(algebraic[2]/constants[32])*(algebraic[10]/constants[33]))/((1.00000+states[4]/constants[31]+algebraic[2]/constants[32])*(1.00000+algebraic[12]/constants[30]+algebraic[10]/constants[33])))
    rates[4] = algebraic[23]-algebraic[24]
    algebraic[3] = constants[4]*algebraic[2]
    algebraic[4] = constants[5]*algebraic[3]
    algebraic[11] = ((constants[12]--(states[9]*(1.00000-4.00000*constants[11])))+power(power(constants[12]--(states[9]*(1.00000-4.00000*constants[11])), 2.00000)-4.00000*(1.00000-4.00000*constants[11])*(-constants[11]*(power(states[9], 2.00000))), 0.500000))/(2.00000*(1.00000-4.00000*constants[11]))
    algebraic[16] = states[9]-2.00000*algebraic[11]
    algebraic[26] = 0.340000*(1.00000+algebraic[11]/0.570000+algebraic[16]/0.640000)
    algebraic[28] = constants[54]*(((power(algebraic[4]/algebraic[26], constants[53]))*(algebraic[16]/constants[52]))/((1.00000+power(algebraic[4]/algebraic[26], constants[53]))*(1.00000+algebraic[16]/constants[52])))
    rates[5] = algebraic[24]-algebraic[28]
    algebraic[20] = constants[17]*(states[6]/constants[16])*(1.00000+states[6]/constants[16])
    rates[6] = algebraic[28]-algebraic[20]
    algebraic[0] = states[1]/constants[2]
    algebraic[1] = states[1]-algebraic[0]
    algebraic[13] = (constants[7]-(algebraic[0]+algebraic[1]+2.00000*states[2]+algebraic[8]+states[4]+2.00000*algebraic[10]+algebraic[12]))/(1.00000+constants[0])-algebraic[5]
    algebraic[15] = algebraic[13]
    algebraic[27] = constants[46]*(((algebraic[6]/constants[44])*(states[7]/constants[42]-constants[47])*(algebraic[15]/constants[43])*(algebraic[9]/constants[45]))/((1.00000+algebraic[6]/constants[44]+algebraic[15]/constants[43])*(1.00000+states[7]/constants[42]+algebraic[9]/constants[45])))
    rates[7] = algebraic[23]-algebraic[27]
    algebraic[29] = constants[51]*(((power(algebraic[1]/constants[49], constants[48]))*(algebraic[10]/constants[50]))/((1.00000+power(algebraic[1]/constants[49], constants[48]))*(1.00000+algebraic[10]/constants[50])))
    rates[1] = algebraic[22]-algebraic[29]
    algebraic[25] = constants[40]*(((algebraic[15]/constants[37])*(algebraic[12]/constants[36]-constants[41])*(constants[6]/constants[38])*(algebraic[10]/constants[39]))/((1.00000+algebraic[15]/constants[37]+constants[6]/constants[38])*(1.00000+algebraic[12]/constants[36]+algebraic[10]/constants[39])))
    rates[8] = (algebraic[24]+algebraic[25])-(algebraic[22]+algebraic[29])
    algebraic[30] = constants[60]*(algebraic[11]/algebraic[16])
    rates[9] = algebraic[28]-algebraic[30]
    algebraic[17] = constants[10]-(algebraic[10]+algebraic[12])
    algebraic[31] = 0.00900000*(1.00000+algebraic[10]/0.680000+algebraic[12]/1.51000+algebraic[17]/3.65000)
    algebraic[32] = constants[58]*((states[2]/algebraic[31]-constants[59]*((algebraic[8]*algebraic[6])/(constants[55]*constants[57])))/(1.00000+states[2]/algebraic[31]+algebraic[8]/constants[55]+algebraic[6]/constants[57]+(states[2]*algebraic[8])/(algebraic[31]*constants[56])+(algebraic[6]*algebraic[8])/(constants[57]*constants[55])))
    rates[2] = algebraic[29]-algebraic[32]
    algebraic[14] = algebraic[13]
    algebraic[21] = constants[19]*(algebraic[14]/constants[18])*(1.00000+algebraic[14]/constants[18])
    rates[3] = (2.00000*algebraic[32]+algebraic[21])-(algebraic[23]+algebraic[27])
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[10] = ((constants[10]--(states[8]*(1.00000-4.00000*constants[9])))+power(power(constants[10]--(states[8]*(1.00000-4.00000*constants[9])), 2.00000)-4.00000*(1.00000-4.00000*constants[9])*(-constants[9]*(power(states[8], 2.00000))), 0.500000))/(2.00000*(1.00000-4.00000*constants[9]))
    algebraic[12] = states[8]-2.00000*algebraic[10]
    algebraic[22] = constants[23]*(((algebraic[10]/constants[21])*(states[0]/constants[20]))/((1.00000+algebraic[10]/constants[21]+algebraic[12]/constants[22])*(1.00000+states[0]/constants[20])))
    algebraic[19] = constants[15]*((constants[1]-states[0])/(constants[13]+constants[1]+states[0]+constants[14]*constants[1]*(states[0]/constants[13])))
    algebraic[5] = (states[3]*(1.00000+constants[0]))/(1.00000+constants[0]+constants[3])
    algebraic[6] = algebraic[5]
    algebraic[8] = constants[3]*algebraic[6]
    algebraic[9] = constants[8]-states[7]
    algebraic[23] = constants[28]*(((algebraic[8]/constants[25])*(algebraic[9]/constants[24]-constants[29])*(states[4]/constants[26])*(states[7]/constants[27]))/((1.00000+algebraic[8]/constants[25]+states[4]/constants[26])*(1.00000+algebraic[9]/constants[24]+states[7]/constants[27])))
    algebraic[2] = (states[5]*(1.00000+constants[0]))/(1.00000+(1.00000+constants[4]+constants[4]*constants[5])*constants[0])
    algebraic[24] = constants[34]*(((states[4]/constants[31])*(algebraic[12]/constants[30]-constants[35])*(algebraic[2]/constants[32])*(algebraic[10]/constants[33]))/((1.00000+states[4]/constants[31]+algebraic[2]/constants[32])*(1.00000+algebraic[12]/constants[30]+algebraic[10]/constants[33])))
    algebraic[3] = constants[4]*algebraic[2]
    algebraic[4] = constants[5]*algebraic[3]
    algebraic[11] = ((constants[12]--(states[9]*(1.00000-4.00000*constants[11])))+power(power(constants[12]--(states[9]*(1.00000-4.00000*constants[11])), 2.00000)-4.00000*(1.00000-4.00000*constants[11])*(-constants[11]*(power(states[9], 2.00000))), 0.500000))/(2.00000*(1.00000-4.00000*constants[11]))
    algebraic[16] = states[9]-2.00000*algebraic[11]
    algebraic[26] = 0.340000*(1.00000+algebraic[11]/0.570000+algebraic[16]/0.640000)
    algebraic[28] = constants[54]*(((power(algebraic[4]/algebraic[26], constants[53]))*(algebraic[16]/constants[52]))/((1.00000+power(algebraic[4]/algebraic[26], constants[53]))*(1.00000+algebraic[16]/constants[52])))
    algebraic[20] = constants[17]*(states[6]/constants[16])*(1.00000+states[6]/constants[16])
    algebraic[0] = states[1]/constants[2]
    algebraic[1] = states[1]-algebraic[0]
    algebraic[13] = (constants[7]-(algebraic[0]+algebraic[1]+2.00000*states[2]+algebraic[8]+states[4]+2.00000*algebraic[10]+algebraic[12]))/(1.00000+constants[0])-algebraic[5]
    algebraic[15] = algebraic[13]
    algebraic[27] = constants[46]*(((algebraic[6]/constants[44])*(states[7]/constants[42]-constants[47])*(algebraic[15]/constants[43])*(algebraic[9]/constants[45]))/((1.00000+algebraic[6]/constants[44]+algebraic[15]/constants[43])*(1.00000+states[7]/constants[42]+algebraic[9]/constants[45])))
    algebraic[29] = constants[51]*(((power(algebraic[1]/constants[49], constants[48]))*(algebraic[10]/constants[50]))/((1.00000+power(algebraic[1]/constants[49], constants[48]))*(1.00000+algebraic[10]/constants[50])))
    algebraic[25] = constants[40]*(((algebraic[15]/constants[37])*(algebraic[12]/constants[36]-constants[41])*(constants[6]/constants[38])*(algebraic[10]/constants[39]))/((1.00000+algebraic[15]/constants[37]+constants[6]/constants[38])*(1.00000+algebraic[12]/constants[36]+algebraic[10]/constants[39])))
    algebraic[30] = constants[60]*(algebraic[11]/algebraic[16])
    algebraic[17] = constants[10]-(algebraic[10]+algebraic[12])
    algebraic[31] = 0.00900000*(1.00000+algebraic[10]/0.680000+algebraic[12]/1.51000+algebraic[17]/3.65000)
    algebraic[32] = constants[58]*((states[2]/algebraic[31]-constants[59]*((algebraic[8]*algebraic[6])/(constants[55]*constants[57])))/(1.00000+states[2]/algebraic[31]+algebraic[8]/constants[55]+algebraic[6]/constants[57]+(states[2]*algebraic[8])/(algebraic[31]*constants[56])+(algebraic[6]*algebraic[8])/(constants[57]*constants[55])))
    algebraic[14] = algebraic[13]
    algebraic[21] = constants[19]*(algebraic[14]/constants[18])*(1.00000+algebraic[14]/constants[18])
    algebraic[7] = algebraic[5]
    algebraic[18] = constants[12]-(algebraic[11]+algebraic[16])
    return algebraic

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
        self.Vc_Vg = 22.3
        self.Glc_o = 5.0
        self.Keq_PGI = 0.29
        self.Keq_TIM = 0.045
        self.Keq_PGM = 0.187
        self.Keq_ENO = 6.7
        self.glycerol_g = 0.00
        self.C4 = 120.0
        self.C3 = 4.0
        self.Keq_AK = 0.442
        self.C1 = 3.9
        self.Keq_AK_1 = 0.442
        self.C2 = 3.9
        self.K_Glc = 2.0
        self.alpha = 0.75
        self.V_glucose_transport_max = 106.2
        self.K_pyruvate = 1.96
        self.V_pyruvate_transport_max = 160.0
        self.K_Gly_3_P = 1.7
        self.V_GPO_max = 200.0
        self.K_Glc_i = 0.1
        self.K_ATP = 0.116
        self.K_ADP = 0.126
        self.V_HK_max = 625.0
        self.K_NAD = 0.45
        self.K_GA_3_P = 0.15
        self.K_1_3_BPGA = 0.1
        self.K_NADH = 0.02
        self.V_GAPDH_max_plus = 1470.0
        self.V_GAPDH_max_ratio = 0.67
        self.K_ADP_1 = 0.1
        self.K_1_3_BPGA_1 = 0.05
        self.K_3_PGA = 1.62
        self.K_ATP_1 = 0.29
        self.V_PGK_max_plus = 640.0
        self.V_PGK_max_ratio = 0.029
        self.K_ADP_2 = 0.12
        self.K_Gly_3_P_1 = 5.1
        self.K_glycerol = 0.12
        self.K_ATP_2 = 0.19
        self.V_GK_max_plus = 0.0
        self.V_GK_max_ratio = 167.0
        self.K_NADH_1 = 0.01
        self.K_Gly_3_P_2 = 2.0
        self.K_DHAP = 0.1
        self.K_NAD_1 = 0.4
        self.V_GDH_max_plus = 533.0
        self.V_GDH_max_ratio = 0.28
        self.n = 1.2
        self.Km_Fru_6_P = 0.82
        self.Km_ATP = 2.6E-2
        self.V_PFK_max = 780.0
        self.Km_ADP = 0.114
        self.n_1 = 2.5
        self.V_PYK_max = 2.6E3
        self.Km_GA_3_P = 6.7E-2
        self.Ki_GA_3_P = 9.8E-2
        self.Km_DHAP = 1.5E-2
        self.V_ALD_max_plus = 780.0
        self.V_ALD_max_ratio = 1.19
        self.k = 50

    def to_dict(self):
        return {
            "Vc_Vg": self.Vc_Vg,
            "Glc_o": self.Glc_o,
            "Keq_PGI": self.Keq_PGI,
            "Keq_TIM": self.Keq_TIM,
            "Keq_PGM": self.Keq_PGM,
            "Keq_ENO": self.Keq_ENO,
            "glycerol_g": self.glycerol_g,
            "C4": self.C4,
            "C3": self.C3,
            "Keq_AK": self.Keq_AK,
            "C1": self.C1,
            "Keq_AK_1": self.Keq_AK_1,
            "C2": self.C2,
            "K_Glc": self.K_Glc,
            "alpha": self.alpha,
            "V_glucose_transport_max": self.V_glucose_transport_max,
            "K_pyruvate": self.K_pyruvate,
            "V_pyruvate_transport_max": self.V_pyruvate_transport_max,
            "K_Gly_3_P": self.K_Gly_3_P,
            "V_GPO_max": self.V_GPO_max,
            "K_Glc_i": self.K_Glc_i,
            "K_ATP": self.K_ATP,
            "K_ADP": self.K_ADP,
            "V_HK_max": self.V_HK_max,
            "K_NAD": self.K_NAD,
            "K_GA_3_P": self.K_GA_3_P,
            "K_1_3_BPGA": self.K_1_3_BPGA,
            "K_NADH": self.K_NADH,
            "V_GAPDH_max_plus": self.V_GAPDH_max_plus,
            "V_GAPDH_max_ratio": self.V_GAPDH_max_ratio,
            "K_ADP_1": self.K_ADP_1,
            "K_1_3_BPGA_1": self.K_1_3_BPGA_1,
            "K_3_PGA": self.K_3_PGA,
            "K_ATP_1": self.K_ATP_1,
            "V_PGK_max_plus": self.V_PGK_max_plus,
            "V_PGK_max_ratio": self.V_PGK_max_ratio,
            "K_ADP_2": self.K_ADP_2,
            "K_Gly_3_P_1": self.K_Gly_3_P_1,
            "K_glycerol": self.K_glycerol,
            "K_ATP_2": self.K_ATP_2,
            "V_GK_max_plus": self.V_GK_max_plus,
            "V_GK_max_ratio": self.V_GK_max_ratio,
            "K_NADH_1": self.K_NADH_1,
            "K_Gly_3_P_2": self.K_Gly_3_P_2,
            "K_DHAP": self.K_DHAP,
            "K_NAD_1": self.K_NAD_1,
            "V_GDH_max_plus": self.V_GDH_max_plus,
            "V_GDH_max_ratio": self.V_GDH_max_ratio,
            "n": self.n,
            "Km_Fru_6_P": self.Km_Fru_6_P,
            "Km_ATP": self.Km_ATP,
            "V_PFK_max": self.V_PFK_max,
            "Km_ADP": self.Km_ADP,
            "n_1": self.n_1,
            "V_PYK_max": self.V_PYK_max,
            "Km_GA_3_P": self.Km_GA_3_P,
            "Ki_GA_3_P": self.Ki_GA_3_P,
            "Km_DHAP": self.Km_DHAP,
            "V_ALD_max_plus": self.V_ALD_max_plus,
            "V_ALD_max_ratio": self.V_ALD_max_ratio,
            "k": self.k,
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
        y0=[0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "bakker_michels_opperdoes_westerhoff_1997"
        self.curve_names = [
            "Glc_i",
            "hexose_P_g",
            "Fru_1_6_BP_g",
            "triose_P",
            "one_three_BPGA_g",
            "N",
            "PYR_c",
            "NADH_g",
            "P_g",
            "P_c",
        ]
        self.state_names = ['Glc_i', 'hexose_P_g', 'Fru_1_6_BP_g', 'triose_P', 'one_three_BPGA_g', 'N', 'PYR_c', 'NADH_g', 'P_g', 'P_c']
        self.algebraic_names = ['Glc_6_P_g', 'Fru_6_P_g', 'three_PGA', 'two_PGA_c', 'PEP_c', 'DHAP', 'DHAP_g', 'DHAP_c', 'GA_3_P_g', 'NAD_g', 'ATP_g', 'ATP_c', 'ADP_g', 'Gly_3_P', 'Gly_3_P_c', 'Gly_3_P_g', 'ADP_c', 'AMP_g', 'AMP_c', 'V_glucose_transport', 'V_pyruvate_transport', 'V_GPO', 'V_HK', 'V_GAPDH', 'V_PGK', 'V_GK', 'Km_PEP', 'V_GDH', 'V_PYK', 'V_PFK', 'V_ATP_utilisation', 'Km_Fru_1_6_BP', 'V_ALD']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 61
        p = self.params

        # direct mapping
        c[0] = p.Vc_Vg
        c[1] = p.Glc_o
        c[2] = p.Keq_PGI
        c[3] = p.Keq_TIM
        c[4] = p.Keq_PGM
        c[5] = p.Keq_ENO
        c[6] = p.glycerol_g
        c[7] = p.C4
        c[8] = p.C3
        c[9] = p.Keq_AK
        c[10] = p.C1
        c[11] = p.Keq_AK_1
        c[12] = p.C2
        c[13] = p.K_Glc
        c[14] = p.alpha
        c[15] = p.V_glucose_transport_max
        c[16] = p.K_pyruvate
        c[17] = p.V_pyruvate_transport_max
        c[18] = p.K_Gly_3_P
        c[19] = p.V_GPO_max
        c[20] = p.K_Glc_i
        c[21] = p.K_ATP
        c[22] = p.K_ADP
        c[23] = p.V_HK_max
        c[24] = p.K_NAD
        c[25] = p.K_GA_3_P
        c[26] = p.K_1_3_BPGA
        c[27] = p.K_NADH
        c[28] = p.V_GAPDH_max_plus
        c[29] = p.V_GAPDH_max_ratio
        c[30] = p.K_ADP_1
        c[31] = p.K_1_3_BPGA_1
        c[32] = p.K_3_PGA
        c[33] = p.K_ATP_1
        c[34] = p.V_PGK_max_plus
        c[35] = p.V_PGK_max_ratio
        c[36] = p.K_ADP_2
        c[37] = p.K_Gly_3_P_1
        c[38] = p.K_glycerol
        c[39] = p.K_ATP_2
        c[40] = p.V_GK_max_plus
        c[41] = p.V_GK_max_ratio
        c[42] = p.K_NADH_1
        c[43] = p.K_Gly_3_P_2
        c[44] = p.K_DHAP
        c[45] = p.K_NAD_1
        c[46] = p.V_GDH_max_plus
        c[47] = p.V_GDH_max_ratio
        c[48] = p.n
        c[49] = p.Km_Fru_6_P
        c[50] = p.Km_ATP
        c[51] = p.V_PFK_max
        c[52] = p.Km_ADP
        c[53] = p.n_1
        c[54] = p.V_PYK_max
        c[55] = p.Km_GA_3_P
        c[56] = p.Ki_GA_3_P
        c[57] = p.Km_DHAP
        c[58] = p.V_ALD_max_plus
        c[59] = p.V_ALD_max_ratio
        c[60] = p.k

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
