# Size of variable arrays:
sizeAlgebraic = 19
sizeStates = 11
sizeConstants = 72
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (minute)"
    legend_constants[0] = "G_o in component G_o (millimolar)"
    legend_states[0] = "G in component G (millimolar)"
    legend_algebraic[3] = "V_IN in component V_IN (flux)"
    legend_algebraic[4] = "V_HK in component V_HK (flux)"
    legend_states[1] = "G6P in component G6P (millimolar)"
    legend_algebraic[5] = "V_PFK in component V_PFK (flux)"
    legend_algebraic[8] = "V_G6PDH in component V_G6PDH (flux)"
    legend_states[2] = "FDP in component FDP (millimolar)"
    legend_algebraic[7] = "V_ALD in component V_ALD (flux)"
    legend_states[3] = "G3P in component G3P (millimolar)"
    legend_algebraic[9] = "V_GAPDH in component V_GAPDH (flux)"
    legend_states[4] = "DPG in component DPG (millimolar)"
    legend_algebraic[10] = "V_PGK in component V_PGK (flux)"
    legend_states[5] = "PEP in component PEP (millimolar)"
    legend_algebraic[15] = "V_PK in component V_PK (flux)"
    legend_states[6] = "Py in component Py (millimolar)"
    legend_algebraic[16] = "V_TCA in component V_TCA (flux)"
    legend_algebraic[17] = "V_ADH in component V_ADH (flux)"
    legend_states[7] = "ATP in component ATP (millimolar)"
    legend_constants[1] = "PO in component ATP (dimensionless)"
    legend_algebraic[18] = "V_ATPase in component V_ATPase (flux)"
    legend_algebraic[0] = "ADP in component ADP (millimolar)"
    legend_constants[2] = "Cn in component ADP (millimolar)"
    legend_constants[3] = "AMP in component AMP (millimolar)"
    legend_constants[4] = "GTP in component GTP (millimolar)"
    legend_constants[5] = "GDP in component GDP (millimolar)"
    legend_constants[6] = "H in component H (millimolar)"
    legend_constants[7] = "NADP in component NADP (millimolar)"
    legend_constants[8] = "NADH in component NADH (millimolar)"
    legend_constants[9] = "NAD in component NAD (millimolar)"
    legend_algebraic[2] = "CD in component CD (millimolar)"
    legend_constants[10] = "CMTP in component CD (millimolar)"
    legend_states[8] = "CT in component CT (millimolar)"
    legend_states[9] = "CP in component CP (millimolar)"
    legend_constants[11] = "kpol in component CT (third_order_rate_constant)"
    legend_constants[12] = "kf in component CT (first_order_rate_constant)"
    legend_constants[13] = "kb in component CT (second_order_rate_constant)"
    legend_constants[14] = "kdp in component CP (first_order_rate_constant)"
    legend_states[10] = "PKp in component PKp (millimolar)"
    legend_constants[15] = "kp2 in component PKp (second_order_rate_constant)"
    legend_constants[16] = "kp3 in component PKp (first_order_rate_constant)"
    legend_constants[17] = "k4 in component PKp (second_order_rate_constant)"
    legend_algebraic[1] = "PKt in component PKt (millimolar)"
    legend_constants[18] = "C_PK in component PKt (millimolar)"
    legend_constants[19] = "Ke_in in component V_IN (millimolar)"
    legend_constants[20] = "KG_in in component V_IN (millimolar)"
    legend_constants[21] = "V_IN_max in component V_IN (flux)"
    legend_constants[22] = "KG_m in component V_HK (millimolar)"
    legend_constants[23] = "KG_s in component V_HK (millimolar)"
    legend_constants[24] = "KATP_m in component V_HK (millimolar)"
    legend_constants[25] = "V_HK_max in component V_HK (flux)"
    legend_constants[26] = "KG6P_r in component V_PFK (millimolar)"
    legend_constants[27] = "KATP_r in component V_PFK (millimolar)"
    legend_constants[28] = "KAMP_r in component V_PFK (millimolar)"
    legend_constants[29] = "cATP in component V_PFK (dimensionless)"
    legend_constants[30] = "cAMP in component V_PFK (dimensionless)"
    legend_constants[31] = "cG6P in component V_PFK (dimensionless)"
    legend_constants[32] = "Lo in component V_PFK (dimensionless)"
    legend_constants[33] = "gr in component V_PFK (dimensionless)"
    legend_constants[34] = "n1 in component V_PFK (dimensionless)"
    legend_constants[35] = "V_PFK_max in component V_PFK (flux)"
    legend_algebraic[6] = "TUB in component V_G6PDH (millimolar)"
    legend_constants[36] = "KG6P in component V_G6PDH (millimolar)"
    legend_constants[37] = "KNADP in component V_G6PDH (millimolar)"
    legend_constants[38] = "KNADP_ in component V_G6PDH (millimolar)"
    legend_constants[39] = "KTUB in component V_G6PDH (millimolar)"
    legend_constants[40] = "V_G6PDH_max in component V_G6PDH (flux)"
    legend_constants[41] = "V_G6PDH_max_II in component V_G6PDH (flux)"
    legend_constants[42] = "KG3P_m in component V_ALD (millimolar)"
    legend_constants[43] = "KFDP_m in component V_ALD (millimolar)"
    legend_constants[44] = "V_ALD_max in component V_ALD (flux)"
    legend_constants[45] = "V_ALD_max_r in component V_ALD (flux)"
    legend_constants[46] = "K1 in component V_GAPDH (millimolar)"
    legend_constants[47] = "K2 in component V_GAPDH (millimolar)"
    legend_constants[48] = "K3 in component V_GAPDH (millimolar)"
    legend_constants[49] = "KG3P in component V_GAPDH (millimolar)"
    legend_constants[50] = "KNAD in component V_GAPDH (millimolar)"
    legend_constants[51] = "KNADH_i in component V_GAPDH (millimolar)"
    legend_constants[52] = "V_GAPDH_max in component V_GAPDH (flux)"
    legend_constants[53] = "KDPG_m in component V_PGK (millimolar)"
    legend_constants[54] = "V_PGK_max in component V_PGK (flux)"
    legend_algebraic[11] = "R in component V_PK (dimensionless)"
    legend_algebraic[12] = "T in component V_PK (dimensionless)"
    legend_constants[55] = "KpH in component V_PK (millimolar)"
    legend_constants[56] = "KPEP_r in component V_PK (millimolar)"
    legend_constants[57] = "KADP_r in component V_PK (millimolar)"
    legend_constants[58] = "KFDP_r in component V_PK (millimolar)"
    legend_constants[59] = "cADP in component V_PK (dimensionless)"
    legend_constants[60] = "cFDP in component V_PK (dimensionless)"
    legend_constants[61] = "cPEP in component V_PK (dimensionless)"
    legend_constants[62] = "Lo_PK in component V_PK (dimensionless)"
    legend_constants[63] = "gr_PK in component V_PK (dimensionless)"
    legend_constants[64] = "gt_PK in component V_PK (dimensionless)"
    legend_algebraic[14] = "n in component V_PK (dimensionless)"
    legend_algebraic[13] = "V_PK_max in component V_PK (flux)"
    legend_constants[65] = "V_PKt_max in component V_PK (flux)"
    legend_constants[66] = "V_PKp_max in component V_PK (flux)"
    legend_constants[67] = "KPy_m in component V_TCA (millimolar)"
    legend_constants[68] = "V_TCA_max in component V_TCA (flux)"
    legend_constants[69] = "KPy__m in component V_ADH (millimolar)"
    legend_constants[70] = "V_ADH_max in component V_ADH (flux)"
    legend_constants[71] = "KATP in component V_ATPase (first_order_rate_constant)"
    legend_rates[0] = "d/dt G in component G (millimolar)"
    legend_rates[1] = "d/dt G6P in component G6P (millimolar)"
    legend_rates[2] = "d/dt FDP in component FDP (millimolar)"
    legend_rates[3] = "d/dt G3P in component G3P (millimolar)"
    legend_rates[4] = "d/dt DPG in component DPG (millimolar)"
    legend_rates[5] = "d/dt PEP in component PEP (millimolar)"
    legend_rates[6] = "d/dt Py in component Py (millimolar)"
    legend_rates[7] = "d/dt ATP in component ATP (millimolar)"
    legend_rates[8] = "d/dt CT in component CT (millimolar)"
    legend_rates[9] = "d/dt CP in component CP (millimolar)"
    legend_rates[10] = "d/dt PKp in component PKp (millimolar)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    constants[0] = 1
    states[0] = 0.01
    states[1] = 0.01
    states[2] = 0.01
    states[3] = 0.01
    states[4] = 0.01
    states[5] = 0.01
    states[6] = 0.01
    states[7] = 1.4
    constants[1] = 4
    constants[2] = 9
    constants[3] = 0.5
    constants[4] = 0.95
    constants[5] = 0.05
    constants[6] = 3.2e-8
    constants[7] = 1
    constants[8] = 0.01
    constants[9] = 1
    constants[10] = 0.9
    states[8] = 0.2
    states[9] = 1.2
    constants[11] = 10
    constants[12] = 3
    constants[13] = 2.5
    constants[14] = 0.0025
    states[10] = 0.005
    constants[15] = 10
    constants[16] = 0.05
    constants[17] = 0.02
    constants[18] = 0.01
    constants[19] = 12
    constants[20] = 0.001
    constants[21] = 10
    constants[22] = 0.11
    constants[23] = 0.0062
    constants[24] = 0.1
    constants[25] = 13
    constants[26] = 1
    constants[27] = 0.06
    constants[28] = 0.025
    constants[29] = 1
    constants[30] = 0.019
    constants[31] = 0.0005
    constants[32] = 25000
    constants[33] = 10
    constants[34] = 2
    constants[35] = 30
    constants[36] = 0.05
    constants[37] = 0.05
    constants[38] = 0.05
    constants[39] = 0.4
    constants[40] = 1.6
    constants[41] = 1
    constants[42] = 20
    constants[43] = 0.5
    constants[44] = 2.5
    constants[45] = 1
    constants[46] = 1.1
    constants[47] = 1.5
    constants[48] = 2.5
    constants[49] = 0.0025
    constants[50] = 0.18
    constants[51] = 0.0003
    constants[52] = 10
    constants[53] = 0.002
    constants[54] = 3
    constants[55] = 9.5e-9
    constants[56] = 1
    constants[57] = 0.06
    constants[58] = 0.025
    constants[59] = 1
    constants[60] = 0.01
    constants[61] = 0.02
    constants[62] = 1000
    constants[63] = 0.1
    constants[64] = 1
    constants[65] = 25
    constants[66] = 50
    constants[67] = 0.329
    constants[68] = 10
    constants[69] = 0.169
    constants[70] = 0.5
    constants[71] = 5
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[9] = constants[11]*states[8]*(power(states[9], 2.00000))-constants[14]*states[9]
    algebraic[1] = constants[18]-states[10]
    rates[10] = 0.100000*constants[15]*algebraic[1]*states[9]-(constants[16]*states[10]+constants[17]*states[10]*constants[4])
    algebraic[2] = constants[10]-(states[8]+states[9])
    rates[8] = -(constants[11]*states[8]*(power(states[9], 2.00000))+constants[12]*algebraic[2]+constants[13]*states[8]*constants[5])
    algebraic[3] = constants[21]*(constants[0]/((constants[20]+constants[0])*(1.00000+states[1]/constants[19]))-states[0]/((constants[20]+states[0])*(1.00000+states[1]/constants[19])))
    algebraic[4] = (constants[25]*1.00000)/(1.00000+(constants[23]*constants[24])/(states[0]*states[7])+constants[22]/states[0]+constants[24]/states[7])
    rates[0] = algebraic[3]-algebraic[4]
    algebraic[5] = (((((constants[35]*constants[33]*states[1])/constants[26])*states[7])/constants[27])*(power(1.00000+states[1]/constants[26]+states[7]/constants[27]+(((constants[33]*states[1])/constants[26])*states[7])/constants[27], constants[34]-1.00000)))/(power(1.00000+states[1]/constants[26]+states[7]/constants[27]+(((constants[33]*states[1])/constants[26])*states[7])/constants[27], constants[34])+constants[32]*(power((1.00000+(constants[30]*constants[3])/constants[28])/(1.00000+constants[3]/constants[28]), constants[34]))*(power(1.00000+(constants[31]*states[1])/constants[26]+(constants[29]*states[7])/constants[27]+(((constants[33]*constants[31]*states[1])/constants[26])*constants[29]*states[7])/constants[27], constants[34])))
    algebraic[7] = ((constants[44]*states[2])/constants[43]-(constants[45]*states[3])/constants[42])/(1.00000+states[2]/constants[43]+states[3]/constants[42])
    rates[2] = algebraic[5]-algebraic[7]
    algebraic[6] = states[8]+algebraic[2]
    algebraic[8] = constants[40]/((constants[36]*constants[37])/(states[1]*constants[7])+constants[36]/states[1]+constants[37]/constants[7]+1.00000)+constants[41]/((constants[36]*constants[38]*constants[39])/(states[1]*constants[7]*algebraic[6])+(constants[36]*constants[38])/(states[1]*constants[7])+(constants[38]*constants[39])/(constants[7]*algebraic[6])+(constants[36]*constants[39])/(states[1]*algebraic[6])+constants[39]/algebraic[6]+constants[36]/states[1]+constants[38]/constants[7]+1.00000)
    rates[1] = algebraic[4]-(algebraic[5]+algebraic[8])
    algebraic[0] = constants[2]-(states[7]+constants[3])
    algebraic[9] = constants[52]/(1.00000+constants[49]/states[3]+(constants[50]/constants[9])*(1.00000+constants[3]/constants[46]+algebraic[0]/constants[47]+states[7]/constants[48])+((constants[49]*constants[50])/(states[3]*constants[9]))*(1.00000+constants[8]/constants[51])+1.00000+constants[3]/constants[46]+algebraic[0]/constants[47]+states[7]/constants[48])
    rates[3] = 2.00000*algebraic[7]-algebraic[9]
    algebraic[10] = (constants[54]*states[4])/(constants[53]+states[4])
    rates[4] = algebraic[9]-algebraic[10]
    algebraic[11] = 1.00000+states[5]/constants[56]+algebraic[0]/constants[57]+(((constants[63]*states[5])/constants[56])*algebraic[0])/constants[57]
    algebraic[12] = 1.00000+(constants[61]*states[5])/constants[56]+(constants[59]*algebraic[0])/constants[57]+(((constants[64]*constants[61]*states[5])/constants[56])*constants[59]*algebraic[0])/constants[57]
    algebraic[14] = 4.00000+states[10]/constants[18]
    algebraic[13] = constants[65]+((constants[66]-constants[65])*states[10])/constants[18]
    algebraic[15] = ((algebraic[13]/(1.00000+constants[55]/constants[6]))*(constants[63]*(states[5]/constants[56])*(algebraic[0]/constants[57])*(power(algebraic[11], algebraic[14]-1.00000))+constants[62]*(power((1.00000+(constants[60]*states[2])/constants[58])/(1.00000+states[2]/constants[58]), algebraic[14]))*(states[2]/constants[58])*constants[64]*((constants[61]*states[5])/constants[56])*((constants[59]*algebraic[0])/constants[57])*(power(algebraic[12], algebraic[14]-1.00000))))/(power(algebraic[11], algebraic[14])+constants[62]*(power((1.00000+(constants[60]*states[2])/constants[58])/(1.00000+states[2]/constants[58]), algebraic[14]))*(power(algebraic[12], algebraic[14])))
    rates[5] = algebraic[10]-algebraic[15]
    algebraic[16] = (constants[68]*(power(states[6], 2.00000)))/(power(constants[67], 2.00000)+power(states[6], 2.00000))
    algebraic[17] = (constants[70]*states[6])/(constants[69]+states[6])
    rates[6] = algebraic[15]-(algebraic[16]+algebraic[17])
    algebraic[18] = constants[71]*states[7]
    rates[7] = (algebraic[10]+algebraic[15]+constants[1]*algebraic[16])-(algebraic[4]+algebraic[5]+algebraic[18])
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[1] = constants[18]-states[10]
    algebraic[2] = constants[10]-(states[8]+states[9])
    algebraic[3] = constants[21]*(constants[0]/((constants[20]+constants[0])*(1.00000+states[1]/constants[19]))-states[0]/((constants[20]+states[0])*(1.00000+states[1]/constants[19])))
    algebraic[4] = (constants[25]*1.00000)/(1.00000+(constants[23]*constants[24])/(states[0]*states[7])+constants[22]/states[0]+constants[24]/states[7])
    algebraic[5] = (((((constants[35]*constants[33]*states[1])/constants[26])*states[7])/constants[27])*(power(1.00000+states[1]/constants[26]+states[7]/constants[27]+(((constants[33]*states[1])/constants[26])*states[7])/constants[27], constants[34]-1.00000)))/(power(1.00000+states[1]/constants[26]+states[7]/constants[27]+(((constants[33]*states[1])/constants[26])*states[7])/constants[27], constants[34])+constants[32]*(power((1.00000+(constants[30]*constants[3])/constants[28])/(1.00000+constants[3]/constants[28]), constants[34]))*(power(1.00000+(constants[31]*states[1])/constants[26]+(constants[29]*states[7])/constants[27]+(((constants[33]*constants[31]*states[1])/constants[26])*constants[29]*states[7])/constants[27], constants[34])))
    algebraic[7] = ((constants[44]*states[2])/constants[43]-(constants[45]*states[3])/constants[42])/(1.00000+states[2]/constants[43]+states[3]/constants[42])
    algebraic[6] = states[8]+algebraic[2]
    algebraic[8] = constants[40]/((constants[36]*constants[37])/(states[1]*constants[7])+constants[36]/states[1]+constants[37]/constants[7]+1.00000)+constants[41]/((constants[36]*constants[38]*constants[39])/(states[1]*constants[7]*algebraic[6])+(constants[36]*constants[38])/(states[1]*constants[7])+(constants[38]*constants[39])/(constants[7]*algebraic[6])+(constants[36]*constants[39])/(states[1]*algebraic[6])+constants[39]/algebraic[6]+constants[36]/states[1]+constants[38]/constants[7]+1.00000)
    algebraic[0] = constants[2]-(states[7]+constants[3])
    algebraic[9] = constants[52]/(1.00000+constants[49]/states[3]+(constants[50]/constants[9])*(1.00000+constants[3]/constants[46]+algebraic[0]/constants[47]+states[7]/constants[48])+((constants[49]*constants[50])/(states[3]*constants[9]))*(1.00000+constants[8]/constants[51])+1.00000+constants[3]/constants[46]+algebraic[0]/constants[47]+states[7]/constants[48])
    algebraic[10] = (constants[54]*states[4])/(constants[53]+states[4])
    algebraic[11] = 1.00000+states[5]/constants[56]+algebraic[0]/constants[57]+(((constants[63]*states[5])/constants[56])*algebraic[0])/constants[57]
    algebraic[12] = 1.00000+(constants[61]*states[5])/constants[56]+(constants[59]*algebraic[0])/constants[57]+(((constants[64]*constants[61]*states[5])/constants[56])*constants[59]*algebraic[0])/constants[57]
    algebraic[14] = 4.00000+states[10]/constants[18]
    algebraic[13] = constants[65]+((constants[66]-constants[65])*states[10])/constants[18]
    algebraic[15] = ((algebraic[13]/(1.00000+constants[55]/constants[6]))*(constants[63]*(states[5]/constants[56])*(algebraic[0]/constants[57])*(power(algebraic[11], algebraic[14]-1.00000))+constants[62]*(power((1.00000+(constants[60]*states[2])/constants[58])/(1.00000+states[2]/constants[58]), algebraic[14]))*(states[2]/constants[58])*constants[64]*((constants[61]*states[5])/constants[56])*((constants[59]*algebraic[0])/constants[57])*(power(algebraic[12], algebraic[14]-1.00000))))/(power(algebraic[11], algebraic[14])+constants[62]*(power((1.00000+(constants[60]*states[2])/constants[58])/(1.00000+states[2]/constants[58]), algebraic[14]))*(power(algebraic[12], algebraic[14])))
    algebraic[16] = (constants[68]*(power(states[6], 2.00000)))/(power(constants[67], 2.00000)+power(states[6], 2.00000))
    algebraic[17] = (constants[70]*states[6])/(constants[69]+states[6])
    algebraic[18] = constants[71]*states[7]
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
        self.G_o = 1
        self.PO = 4
        self.Cn = 9
        self.AMP = 0.5
        self.GTP = 0.95
        self.GDP = 0.05
        self.H = 3.2e-8
        self.NADP = 1
        self.NADH = 0.01
        self.NAD = 1
        self.CMTP = 0.9
        self.kpol = 10
        self.kf = 3
        self.kb = 2.5
        self.kdp = 0.0025
        self.kp2 = 10
        self.kp3 = 0.05
        self.k4 = 0.02
        self.C_PK = 0.01
        self.Ke_in = 12
        self.KG_in = 0.001
        self.V_IN_max = 10
        self.KG_m = 0.11
        self.KG_s = 0.0062
        self.KATP_m = 0.1
        self.V_HK_max = 13
        self.KG6P_r = 1
        self.KATP_r = 0.06
        self.KAMP_r = 0.025
        self.cATP = 1
        self.cAMP = 0.019
        self.cG6P = 0.0005
        self.Lo = 25000
        self.gr = 10
        self.n1 = 2
        self.V_PFK_max = 30
        self.KG6P = 0.05
        self.KNADP = 0.05
        self.KNADP_ = 0.05
        self.KTUB = 0.4
        self.V_G6PDH_max = 1.6
        self.V_G6PDH_max_II = 1
        self.KG3P_m = 20
        self.KFDP_m = 0.5
        self.V_ALD_max = 2.5
        self.V_ALD_max_r = 1
        self.K1 = 1.1
        self.K2 = 1.5
        self.K3 = 2.5
        self.KG3P = 0.0025
        self.KNAD = 0.18
        self.KNADH_i = 0.0003
        self.V_GAPDH_max = 10
        self.KDPG_m = 0.002
        self.V_PGK_max = 3
        self.KpH = 9.5e-9
        self.KPEP_r = 1
        self.KADP_r = 0.06
        self.KFDP_r = 0.025
        self.cADP = 1
        self.cFDP = 0.01
        self.cPEP = 0.02
        self.Lo_PK = 1000
        self.gr_PK = 0.1
        self.gt_PK = 1
        self.V_PKt_max = 25
        self.V_PKp_max = 50
        self.KPy_m = 0.329
        self.V_TCA_max = 10
        self.KPy_m_1 = 0.169
        self.V_ADH_max = 0.5
        self.KATP = 5

    def to_dict(self):
        return {
            "G_o": self.G_o,
            "PO": self.PO,
            "Cn": self.Cn,
            "AMP": self.AMP,
            "GTP": self.GTP,
            "GDP": self.GDP,
            "H": self.H,
            "NADP": self.NADP,
            "NADH": self.NADH,
            "NAD": self.NAD,
            "CMTP": self.CMTP,
            "kpol": self.kpol,
            "kf": self.kf,
            "kb": self.kb,
            "kdp": self.kdp,
            "kp2": self.kp2,
            "kp3": self.kp3,
            "k4": self.k4,
            "C_PK": self.C_PK,
            "Ke_in": self.Ke_in,
            "KG_in": self.KG_in,
            "V_IN_max": self.V_IN_max,
            "KG_m": self.KG_m,
            "KG_s": self.KG_s,
            "KATP_m": self.KATP_m,
            "V_HK_max": self.V_HK_max,
            "KG6P_r": self.KG6P_r,
            "KATP_r": self.KATP_r,
            "KAMP_r": self.KAMP_r,
            "cATP": self.cATP,
            "cAMP": self.cAMP,
            "cG6P": self.cG6P,
            "Lo": self.Lo,
            "gr": self.gr,
            "n1": self.n1,
            "V_PFK_max": self.V_PFK_max,
            "KG6P": self.KG6P,
            "KNADP": self.KNADP,
            "KNADP_": self.KNADP_,
            "KTUB": self.KTUB,
            "V_G6PDH_max": self.V_G6PDH_max,
            "V_G6PDH_max_II": self.V_G6PDH_max_II,
            "KG3P_m": self.KG3P_m,
            "KFDP_m": self.KFDP_m,
            "V_ALD_max": self.V_ALD_max,
            "V_ALD_max_r": self.V_ALD_max_r,
            "K1": self.K1,
            "K2": self.K2,
            "K3": self.K3,
            "KG3P": self.KG3P,
            "KNAD": self.KNAD,
            "KNADH_i": self.KNADH_i,
            "V_GAPDH_max": self.V_GAPDH_max,
            "KDPG_m": self.KDPG_m,
            "V_PGK_max": self.V_PGK_max,
            "KpH": self.KpH,
            "KPEP_r": self.KPEP_r,
            "KADP_r": self.KADP_r,
            "KFDP_r": self.KFDP_r,
            "cADP": self.cADP,
            "cFDP": self.cFDP,
            "cPEP": self.cPEP,
            "Lo_PK": self.Lo_PK,
            "gr_PK": self.gr_PK,
            "gt_PK": self.gt_PK,
            "V_PKt_max": self.V_PKt_max,
            "V_PKp_max": self.V_PKp_max,
            "KPy_m": self.KPy_m,
            "V_TCA_max": self.V_TCA_max,
            "KPy_m_1": self.KPy_m_1,
            "V_ADH_max": self.V_ADH_max,
            "KATP": self.KATP,
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
        y0=[0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 1.4, 0.2, 1.2, 0.005],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "aon_cortassa_2002"
        self.curve_names = [
            "G",
            "G6P",
            "FDP",
            "G3P",
            "DPG",
            "PEP",
            "Py",
            "ATP",
            "CT",
            "CP",
            "PKp",
        ]
        self.state_names = ['G', 'G6P', 'FDP', 'G3P', 'DPG', 'PEP', 'Py', 'ATP', 'CT', 'CP', 'PKp']
        self.algebraic_names = ['ADP', 'PKt', 'CD', 'V_IN', 'V_HK', 'V_PFK', 'TUB', 'V_ALD', 'V_G6PDH', 'V_GAPDH', 'V_PGK', 'R', 'T', 'V_PK_max', 'n', 'V_PK', 'V_TCA', 'V_ADH', 'V_ATPase']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 72
        p = self.params

        # direct mapping
        c[0] = p.G_o
        c[1] = p.PO
        c[2] = p.Cn
        c[3] = p.AMP
        c[4] = p.GTP
        c[5] = p.GDP
        c[6] = p.H
        c[7] = p.NADP
        c[8] = p.NADH
        c[9] = p.NAD
        c[10] = p.CMTP
        c[11] = p.kpol
        c[12] = p.kf
        c[13] = p.kb
        c[14] = p.kdp
        c[15] = p.kp2
        c[16] = p.kp3
        c[17] = p.k4
        c[18] = p.C_PK
        c[19] = p.Ke_in
        c[20] = p.KG_in
        c[21] = p.V_IN_max
        c[22] = p.KG_m
        c[23] = p.KG_s
        c[24] = p.KATP_m
        c[25] = p.V_HK_max
        c[26] = p.KG6P_r
        c[27] = p.KATP_r
        c[28] = p.KAMP_r
        c[29] = p.cATP
        c[30] = p.cAMP
        c[31] = p.cG6P
        c[32] = p.Lo
        c[33] = p.gr
        c[34] = p.n1
        c[35] = p.V_PFK_max
        c[36] = p.KG6P
        c[37] = p.KNADP
        c[38] = p.KNADP_
        c[39] = p.KTUB
        c[40] = p.V_G6PDH_max
        c[41] = p.V_G6PDH_max_II
        c[42] = p.KG3P_m
        c[43] = p.KFDP_m
        c[44] = p.V_ALD_max
        c[45] = p.V_ALD_max_r
        c[46] = p.K1
        c[47] = p.K2
        c[48] = p.K3
        c[49] = p.KG3P
        c[50] = p.KNAD
        c[51] = p.KNADH_i
        c[52] = p.V_GAPDH_max
        c[53] = p.KDPG_m
        c[54] = p.V_PGK_max
        c[55] = p.KpH
        c[56] = p.KPEP_r
        c[57] = p.KADP_r
        c[58] = p.KFDP_r
        c[59] = p.cADP
        c[60] = p.cFDP
        c[61] = p.cPEP
        c[62] = p.Lo_PK
        c[63] = p.gr_PK
        c[64] = p.gt_PK
        c[65] = p.V_PKt_max
        c[66] = p.V_PKp_max
        c[67] = p.KPy_m
        c[68] = p.V_TCA_max
        c[69] = p.KPy_m_1
        c[70] = p.V_ADH_max
        c[71] = p.KATP

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
