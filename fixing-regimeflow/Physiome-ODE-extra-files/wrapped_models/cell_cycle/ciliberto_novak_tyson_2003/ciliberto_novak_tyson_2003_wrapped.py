# Size of variable arrays:
sizeAlgebraic = 9
sizeStates = 19
sizeConstants = 69
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (minute)"
    legend_states[0] = "Clb2 in component Clb2 (dimensionless)"
    legend_constants[0] = "epsilon in component Clb2 (dimensionless)"
    legend_constants[1] = "Jm in component Clb2 (dimensionless)"
    legend_constants[2] = "ks_clb in component Clb2 (first_order_rate_constant)"
    legend_constants[3] = "kd_clb_1 in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[4] = "kd_clb_2 in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[5] = "kd_clb_3 in component kinetic_parameters (first_order_rate_constant)"
    legend_algebraic[8] = "kswe in component kinetic_parameters (first_order_rate_constant)"
    legend_algebraic[7] = "kmih in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[6] = "kass in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[7] = "kdiss in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[8] = "kd_sic in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[9] = "kd_sic_1 in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[10] = "kd_sic_2 in component kinetic_parameters (first_order_rate_constant)"
    legend_states[1] = "M in component M (dimensionless)"
    legend_states[2] = "Mcm_a in component Mcm_a (dimensionless)"
    legend_states[3] = "Cdh1_a in component Cdh1_a (dimensionless)"
    legend_states[4] = "Cdc20_a in component Cdc20_a (dimensionless)"
    legend_states[5] = "Sic1 in component Sic1 (dimensionless)"
    legend_states[6] = "PClb2 in component PClb2 (dimensionless)"
    legend_states[7] = "Trim in component Trim (dimensionless)"
    legend_states[8] = "Cln in component Cln (dimensionless)"
    legend_states[9] = "PTrim in component PTrim (dimensionless)"
    legend_constants[11] = "Ji_mcm in component Mcm_a (dimensionless)"
    legend_constants[12] = "Ja_mcm in component Mcm_a (dimensionless)"
    legend_constants[13] = "ki_mcm in component Mcm_a (first_order_rate_constant)"
    legend_constants[14] = "ka_mcm in component Mcm_a (first_order_rate_constant)"
    legend_algebraic[0] = "Mcm in component Mcm (dimensionless)"
    legend_constants[15] = "ks_sic in component Sic1 (first_order_rate_constant)"
    legend_states[10] = "Mih1_a in component Mih1_a (dimensionless)"
    legend_constants[16] = "Ji_mih in component Mih1_a (dimensionless)"
    legend_constants[17] = "Ja_mih in component Mih1_a (dimensionless)"
    legend_constants[18] = "Vi_mih in component Mih1_a (first_order_rate_constant)"
    legend_constants[19] = "Va_mih in component Mih1_a (first_order_rate_constant)"
    legend_algebraic[1] = "Mih1 in component Mih1 (dimensionless)"
    legend_states[11] = "IE_a in component IE_a (dimensionless)"
    legend_constants[20] = "Ji_ie in component IE_a (dimensionless)"
    legend_constants[21] = "Ja_ie in component IE_a (dimensionless)"
    legend_constants[22] = "ki_ie in component IE_a (first_order_rate_constant)"
    legend_constants[23] = "ka_ie in component IE_a (first_order_rate_constant)"
    legend_algebraic[2] = "IE in component IE (dimensionless)"
    legend_constants[24] = "Ji_cdc20 in component kinetic_parameters (dimensionless)"
    legend_constants[25] = "Ja_cdc20 in component kinetic_parameters (dimensionless)"
    legend_constants[26] = "ki_cdc20 in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[27] = "kd_cdc20 in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[28] = "ka_cdc20 in component kinetic_parameters (first_order_rate_constant)"
    legend_states[12] = "Cdc20 in component Cdc20 (dimensionless)"
    legend_constants[29] = "ks_cdc20_1 in component Cdc20 (first_order_rate_constant)"
    legend_constants[30] = "ks_cdc20_2 in component Cdc20 (first_order_rate_constant)"
    legend_constants[31] = "Js_cdc20 in component Cdc20 (dimensionless)"
    legend_constants[32] = "Ji_cdh in component Cdh1_a (dimensionless)"
    legend_constants[33] = "Ja_cdh in component Cdh1_a (dimensionless)"
    legend_constants[34] = "ki_cdh in component Cdh1_a (first_order_rate_constant)"
    legend_constants[35] = "ka_cdh_1 in component Cdh1_a (first_order_rate_constant)"
    legend_constants[36] = "ki_cdh_1 in component Cdh1_a (first_order_rate_constant)"
    legend_constants[37] = "ka_cdh_2 in component Cdh1_a (first_order_rate_constant)"
    legend_algebraic[3] = "Cdh1 in component Cdh1 (dimensionless)"
    legend_constants[38] = "ks_cln in component Cln (first_order_rate_constant)"
    legend_constants[39] = "kd_cln in component Cln (first_order_rate_constant)"
    legend_states[13] = "SBF_a in component SBF_a (dimensionless)"
    legend_constants[40] = "Ji_sbf in component SBF_a (dimensionless)"
    legend_constants[41] = "Ja_sbf in component SBF_a (dimensionless)"
    legend_constants[42] = "ki_sbf_1 in component SBF_a (first_order_rate_constant)"
    legend_constants[43] = "ka_sbf_1 in component SBF_a (first_order_rate_constant)"
    legend_constants[44] = "ki_sbf_2 in component SBF_a (first_order_rate_constant)"
    legend_constants[45] = "ka_sbf_2 in component SBF_a (first_order_rate_constant)"
    legend_algebraic[4] = "SBF in component SBF (dimensionless)"
    legend_states[14] = "Swe1 in component Swe1 (dimensionless)"
    legend_constants[46] = "ks_swe in component Swe1 (first_order_rate_constant)"
    legend_constants[47] = "ks_sweC in component Swe1 (first_order_rate_constant)"
    legend_constants[48] = "khsl1 in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[49] = "khsl1r in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[50] = "kd_swe_1 in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[51] = "Ji_wee in component kinetic_parameters (dimensionless)"
    legend_constants[52] = "Ja_wee in component kinetic_parameters (dimensionless)"
    legend_constants[53] = "Vi_wee in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[54] = "Va_wee in component kinetic_parameters (first_order_rate_constant)"
    legend_algebraic[5] = "BUD in component BUD (dimensionless)"
    legend_states[15] = "PSwe1 in component PSwe1 (dimensionless)"
    legend_states[16] = "Swe1M in component Swe1M (dimensionless)"
    legend_states[17] = "PSwe1M in component PSwe1M (dimensionless)"
    legend_constants[55] = "kd_swe_2 in component PSwe1M (first_order_rate_constant)"
    legend_states[18] = "BE in component BE (dimensionless)"
    legend_constants[56] = "ks_bud in component BE (first_order_rate_constant)"
    legend_constants[57] = "kd_bud in component BE (first_order_rate_constant)"
    legend_constants[58] = "mu in component M (first_order_rate_constant)"
    legend_constants[59] = "IE_total in component IE (dimensionless)"
    legend_constants[60] = "Cdh1_total in component Cdh1 (dimensionless)"
    legend_constants[61] = "Mih1_total in component Mih1 (dimensionless)"
    legend_constants[62] = "Mcm_total in component Mcm (dimensionless)"
    legend_constants[63] = "SBF_total in component SBF (dimensionless)"
    legend_algebraic[6] = "Swe1_total in component Swe1_total (dimensionless)"
    legend_constants[64] = "kswe_1 in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[65] = "kswe_2 in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[66] = "kswe_3 in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[67] = "kmih_1 in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[68] = "kmih_2 in component kinetic_parameters (first_order_rate_constant)"
    legend_rates[0] = "d/dt Clb2 in component Clb2 (dimensionless)"
    legend_rates[6] = "d/dt PClb2 in component PClb2 (dimensionless)"
    legend_rates[7] = "d/dt Trim in component Trim (dimensionless)"
    legend_rates[9] = "d/dt PTrim in component PTrim (dimensionless)"
    legend_rates[2] = "d/dt Mcm_a in component Mcm_a (dimensionless)"
    legend_rates[5] = "d/dt Sic1 in component Sic1 (dimensionless)"
    legend_rates[10] = "d/dt Mih1_a in component Mih1_a (dimensionless)"
    legend_rates[11] = "d/dt IE_a in component IE_a (dimensionless)"
    legend_rates[4] = "d/dt Cdc20_a in component Cdc20_a (dimensionless)"
    legend_rates[12] = "d/dt Cdc20 in component Cdc20 (dimensionless)"
    legend_rates[3] = "d/dt Cdh1_a in component Cdh1_a (dimensionless)"
    legend_rates[8] = "d/dt Cln in component Cln (dimensionless)"
    legend_rates[13] = "d/dt SBF_a in component SBF_a (dimensionless)"
    legend_rates[14] = "d/dt Swe1 in component Swe1 (dimensionless)"
    legend_rates[15] = "d/dt PSwe1 in component PSwe1 (dimensionless)"
    legend_rates[16] = "d/dt Swe1M in component Swe1M (dimensionless)"
    legend_rates[17] = "d/dt PSwe1M in component PSwe1M (dimensionless)"
    legend_rates[18] = "d/dt BE in component BE (dimensionless)"
    legend_rates[1] = "d/dt M in component M (dimensionless)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 0.184
    constants[0] = 0.5
    constants[1] = 10
    constants[2] = 0.015
    constants[3] = 0.015
    constants[4] = 1
    constants[5] = 0.1
    constants[6] = 300
    constants[7] = 0.1
    constants[8] = 0.01
    constants[9] = 1
    constants[10] = 3
    states[1] = 0.802
    states[2] = 0.933
    states[3] = 0.993
    states[4] = 1.438
    states[5] = 0.003
    states[6] = 0
    states[7] = 0.084
    states[8] = 0.054
    states[9] = 0
    constants[11] = 0.1
    constants[12] = 0.1
    constants[13] = 0.15
    constants[14] = 1
    constants[15] = 0.1
    states[10] = 0.808
    constants[16] = 0.1
    constants[17] = 0.1
    constants[18] = 0.3
    constants[19] = 1
    states[11] = 0.522
    constants[20] = 0.01
    constants[21] = 0.01
    constants[22] = 0.04
    constants[23] = 0.1
    constants[24] = 0.001
    constants[25] = 0.001
    constants[26] = 0.25
    constants[27] = 0.1
    constants[28] = 1
    states[12] = 1.172
    constants[29] = 0.005
    constants[30] = 0.3
    constants[31] = 0.3
    constants[32] = 0.01
    constants[33] = 0.01
    constants[34] = 35
    constants[35] = 1
    constants[36] = 2
    constants[37] = 10
    constants[38] = 0.1
    constants[39] = 0.1
    states[13] = 0.124
    constants[40] = 0.01
    constants[41] = 0.01
    constants[42] = 1
    constants[43] = 1
    constants[44] = 2
    constants[45] = 0
    states[14] = 0
    constants[46] = 0.0025
    constants[47] = 0
    constants[48] = 1
    constants[49] = 0.01
    constants[50] = 0.007
    constants[51] = 0.05
    constants[52] = 0.05
    constants[53] = 1
    constants[54] = 0.3
    states[15] = 0
    states[16] = 0.018
    states[17] = 0.013
    constants[55] = 0.05
    states[18] = 0
    constants[56] = 0.1
    constants[57] = 0.1
    constants[58] = 0.005
    constants[59] = 1
    constants[60] = 1
    constants[61] = 1
    constants[62] = 1
    constants[63] = 1
    constants[64] = 2
    constants[65] = 0.01
    constants[66] = 0.2
    constants[67] = 5
    constants[68] = 0.5
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[5] = (constants[15]+constants[7]*(states[9]+states[7])+(constants[3]+constants[4]*states[3]+constants[5]*states[4])*(states[9]+states[7]))-((constants[8]+constants[9]*states[8]+constants[10]*states[0])*states[5]+constants[6]*states[5]*(states[0]+states[6]))
    rates[4] = (constants[28]*states[11]*states[12])/(constants[25]+states[12])-((constants[26]*states[4])/(constants[24]+states[4])+constants[27]*states[4])
    rates[12] = (constants[29]+(constants[30]*(power(states[0], 4.00000)))/(power(constants[31], 4.00000)+power(states[0], 4.00000))+(constants[26]*states[4])/(constants[24]+states[4]))-((constants[28]*states[11]*states[12])/(constants[25]+states[12])+constants[27]*states[12])
    rates[8] = constants[38]*states[13]-constants[39]*states[8]
    rates[18] = constants[56]*states[8]-constants[57]*states[18]
    rates[1] = constants[58]*states[1]
    algebraic[0] = constants[62]-states[2]
    rates[2] = (-constants[13]*states[2])/(constants[11]+states[2])+(constants[14]*algebraic[0]*states[0])/(constants[12]+algebraic[0])
    algebraic[1] = constants[61]-states[10]
    rates[10] = (-constants[18]*states[10])/(constants[16]+states[10])+(constants[19]*states[0]*algebraic[1])/(constants[17]+algebraic[1])
    algebraic[2] = constants[59]-states[11]
    rates[11] = (-constants[22]*states[11])/(constants[20]+states[11])+(constants[23]*states[0]*algebraic[2])/(constants[21]+algebraic[2])
    algebraic[3] = constants[60]-states[3]
    rates[3] = (-(constants[34]*states[0]+constants[36]*states[8])*states[3])/(constants[32]+states[3])+((constants[35]+constants[37]*states[4])*algebraic[3])/(constants[33]+algebraic[3])
    algebraic[4] = constants[63]-states[13]
    rates[13] = (-(constants[42]+constants[44]*states[0])*states[13])/(constants[40]+states[13])+((constants[43]*states[1]+constants[45]*states[8])*algebraic[4])/(constants[41]+algebraic[4])
    algebraic[5] = custom_piecewise([less_equal(states[18] , 0.600000) & less(states[0] , 0.200000), 0.00000 , True, 1.00000])
    rates[14] = (constants[46]*states[13]+constants[47]+constants[49]*states[16]+(constants[54]*states[15])/(constants[52]+states[15]))-(constants[48]*algebraic[5]*states[14]+(constants[53]*states[0]*states[14])/(constants[51]+states[14])+constants[50]*states[14])
    rates[15] = (constants[49]*states[17]+(constants[53]*states[14]*states[0])/(constants[51]+states[14]))-(constants[48]*algebraic[5]*states[15]+(constants[54]*states[15])/(constants[52]+states[15])+constants[50]*states[15])
    rates[16] = (constants[48]*algebraic[5]*states[14]+(constants[54]*states[17])/(constants[52]+states[17]))-(constants[49]*states[16]+(constants[53]*states[0]*states[16])/(constants[51]+states[16])+constants[50]*states[16])
    rates[17] = (constants[48]*algebraic[5]*states[15]+(constants[53]*states[0]*states[16])/(constants[51]+states[16]))-(constants[49]*states[17]+(constants[54]*states[17])/(constants[52]+states[17])+constants[55]*states[17])
    algebraic[8] = constants[64]*states[14]+constants[65]*states[16]+constants[66]*states[15]
    algebraic[7] = constants[67]*states[10]+constants[68]*algebraic[1]
    rates[0] = ((constants[2]*(constants[0]+states[2])*states[1])/(1.00000+states[1]/constants[1])+algebraic[7]*states[6]+constants[7]*states[7]+(constants[8]+constants[9]*states[8]+constants[10]*states[0])*states[7])-((constants[3]+constants[4]*states[3]+constants[5]*states[4])*states[0]+algebraic[8]*states[0]+constants[6]*states[5]*states[0])
    rates[6] = (algebraic[8]*states[0]+constants[7]*states[9]+(constants[8]+constants[9]*states[8]+constants[10]*states[0])*states[9])-((constants[3]+constants[4]*states[3]+constants[5]*states[4])*states[6]+algebraic[7]*states[6]+constants[6]*states[5]*states[6])
    rates[7] = (constants[6]*states[5]*states[0]+algebraic[7]*states[9])-(constants[7]*states[7]+(constants[8]+constants[9]*states[8]+constants[10]*states[0])*states[7]+(constants[3]+constants[4]*states[3]+constants[5]*states[4])*states[7]+algebraic[8]*states[7])
    rates[9] = (algebraic[8]*states[7]+constants[6]*states[5]*states[6])-(constants[7]*states[9]+(constants[8]+constants[9]*states[8]+constants[10]*states[0])*states[9]+(constants[3]+constants[4]*states[3]+constants[5]*states[4])*states[9]+algebraic[7]*states[9])
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = constants[62]-states[2]
    algebraic[1] = constants[61]-states[10]
    algebraic[2] = constants[59]-states[11]
    algebraic[3] = constants[60]-states[3]
    algebraic[4] = constants[63]-states[13]
    algebraic[5] = custom_piecewise([less_equal(states[18] , 0.600000) & less(states[0] , 0.200000), 0.00000 , True, 1.00000])
    algebraic[8] = constants[64]*states[14]+constants[65]*states[16]+constants[66]*states[15]
    algebraic[7] = constants[67]*states[10]+constants[68]*algebraic[1]
    algebraic[6] = states[14]+states[15]+states[16]+states[17]
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
        self.epsilon = 0.5
        self.Jm = 10
        self.ks_clb = 0.015
        self.kd_clb_1 = 0.015
        self.kd_clb_2 = 1
        self.kd_clb_3 = 0.1
        self.kass = 300
        self.kdiss = 0.1
        self.kd_sic = 0.01
        self.kd_sic_1 = 1
        self.kd_sic_2 = 3
        self.Ji_mcm = 0.1
        self.Ja_mcm = 0.1
        self.ki_mcm = 0.15
        self.ka_mcm = 1
        self.ks_sic = 0.1
        self.Ji_mih = 0.1
        self.Ja_mih = 0.1
        self.Vi_mih = 0.3
        self.Va_mih = 1
        self.Ji_ie = 0.01
        self.Ja_ie = 0.01
        self.ki_ie = 0.04
        self.ka_ie = 0.1
        self.Ji_cdc20 = 0.001
        self.Ja_cdc20 = 0.001
        self.ki_cdc20 = 0.25
        self.kd_cdc20 = 0.1
        self.ka_cdc20 = 1
        self.ks_cdc20_1 = 0.005
        self.ks_cdc20_2 = 0.3
        self.Js_cdc20 = 0.3
        self.Ji_cdh = 0.01
        self.Ja_cdh = 0.01
        self.ki_cdh = 35
        self.ka_cdh_1 = 1
        self.ki_cdh_1 = 2
        self.ka_cdh_2 = 10
        self.ks_cln = 0.1
        self.kd_cln = 0.1
        self.Ji_sbf = 0.01
        self.Ja_sbf = 0.01
        self.ki_sbf_1 = 1
        self.ka_sbf_1 = 1
        self.ki_sbf_2 = 2
        self.ka_sbf_2 = 0
        self.ks_swe = 0.0025
        self.ks_sweC = 0
        self.khsl1 = 1
        self.khsl1r = 0.01
        self.kd_swe_1 = 0.007
        self.Ji_wee = 0.05
        self.Ja_wee = 0.05
        self.Vi_wee = 1
        self.Va_wee = 0.3
        self.kd_swe_2 = 0.05
        self.ks_bud = 0.1
        self.kd_bud = 0.1
        self.mu = 0.005
        self.IE_total = 1
        self.Cdh1_total = 1
        self.Mih1_total = 1
        self.Mcm_total = 1
        self.SBF_total = 1
        self.kswe_1 = 2
        self.kswe_2 = 0.01
        self.kswe_3 = 0.2
        self.kmih_1 = 5
        self.kmih_2 = 0.5

    def to_dict(self):
        return {
            "epsilon": self.epsilon,
            "Jm": self.Jm,
            "ks_clb": self.ks_clb,
            "kd_clb_1": self.kd_clb_1,
            "kd_clb_2": self.kd_clb_2,
            "kd_clb_3": self.kd_clb_3,
            "kass": self.kass,
            "kdiss": self.kdiss,
            "kd_sic": self.kd_sic,
            "kd_sic_1": self.kd_sic_1,
            "kd_sic_2": self.kd_sic_2,
            "Ji_mcm": self.Ji_mcm,
            "Ja_mcm": self.Ja_mcm,
            "ki_mcm": self.ki_mcm,
            "ka_mcm": self.ka_mcm,
            "ks_sic": self.ks_sic,
            "Ji_mih": self.Ji_mih,
            "Ja_mih": self.Ja_mih,
            "Vi_mih": self.Vi_mih,
            "Va_mih": self.Va_mih,
            "Ji_ie": self.Ji_ie,
            "Ja_ie": self.Ja_ie,
            "ki_ie": self.ki_ie,
            "ka_ie": self.ka_ie,
            "Ji_cdc20": self.Ji_cdc20,
            "Ja_cdc20": self.Ja_cdc20,
            "ki_cdc20": self.ki_cdc20,
            "kd_cdc20": self.kd_cdc20,
            "ka_cdc20": self.ka_cdc20,
            "ks_cdc20_1": self.ks_cdc20_1,
            "ks_cdc20_2": self.ks_cdc20_2,
            "Js_cdc20": self.Js_cdc20,
            "Ji_cdh": self.Ji_cdh,
            "Ja_cdh": self.Ja_cdh,
            "ki_cdh": self.ki_cdh,
            "ka_cdh_1": self.ka_cdh_1,
            "ki_cdh_1": self.ki_cdh_1,
            "ka_cdh_2": self.ka_cdh_2,
            "ks_cln": self.ks_cln,
            "kd_cln": self.kd_cln,
            "Ji_sbf": self.Ji_sbf,
            "Ja_sbf": self.Ja_sbf,
            "ki_sbf_1": self.ki_sbf_1,
            "ka_sbf_1": self.ka_sbf_1,
            "ki_sbf_2": self.ki_sbf_2,
            "ka_sbf_2": self.ka_sbf_2,
            "ks_swe": self.ks_swe,
            "ks_sweC": self.ks_sweC,
            "khsl1": self.khsl1,
            "khsl1r": self.khsl1r,
            "kd_swe_1": self.kd_swe_1,
            "Ji_wee": self.Ji_wee,
            "Ja_wee": self.Ja_wee,
            "Vi_wee": self.Vi_wee,
            "Va_wee": self.Va_wee,
            "kd_swe_2": self.kd_swe_2,
            "ks_bud": self.ks_bud,
            "kd_bud": self.kd_bud,
            "mu": self.mu,
            "IE_total": self.IE_total,
            "Cdh1_total": self.Cdh1_total,
            "Mih1_total": self.Mih1_total,
            "Mcm_total": self.Mcm_total,
            "SBF_total": self.SBF_total,
            "kswe_1": self.kswe_1,
            "kswe_2": self.kswe_2,
            "kswe_3": self.kswe_3,
            "kmih_1": self.kmih_1,
            "kmih_2": self.kmih_2,
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
        y0=[0.184, 0.802, 0.933, 0.993, 1.438, 0.003, 0, 0.084, 0.054, 0, 0.808, 0.522, 1.172, 0.124, 0, 0, 0.018, 0.013, 0],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "ciliberto_novak_tyson_2003"
        self.curve_names = [
            "Clb2",
            "M",
            "Mcm_a",
            "Cdh1_a",
            "Cdc20_a",
            "Sic1",
            "PClb2",
            "Trim",
            "Cln",
            "PTrim",
            "Mih1_a",
            "IE_a",
            "Cdc20",
            "SBF_a",
            "Swe1",
            "PSwe1",
            "Swe1M",
            "PSwe1M",
            "BE",
        ]
        self.state_names = ['Clb2', 'M', 'Mcm_a', 'Cdh1_a', 'Cdc20_a', 'Sic1', 'PClb2', 'Trim', 'Cln', 'PTrim', 'Mih1_a', 'IE_a', 'Cdc20', 'SBF_a', 'Swe1', 'PSwe1', 'Swe1M', 'PSwe1M', 'BE']
        self.algebraic_names = ['Mcm', 'Mih1', 'IE', 'Cdh1', 'SBF', 'BUD', 'Swe1_total', 'kmih', 'kswe']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 69
        p = self.params

        # direct mapping
        c[0] = p.epsilon
        c[1] = p.Jm
        c[2] = p.ks_clb
        c[3] = p.kd_clb_1
        c[4] = p.kd_clb_2
        c[5] = p.kd_clb_3
        c[6] = p.kass
        c[7] = p.kdiss
        c[8] = p.kd_sic
        c[9] = p.kd_sic_1
        c[10] = p.kd_sic_2
        c[11] = p.Ji_mcm
        c[12] = p.Ja_mcm
        c[13] = p.ki_mcm
        c[14] = p.ka_mcm
        c[15] = p.ks_sic
        c[16] = p.Ji_mih
        c[17] = p.Ja_mih
        c[18] = p.Vi_mih
        c[19] = p.Va_mih
        c[20] = p.Ji_ie
        c[21] = p.Ja_ie
        c[22] = p.ki_ie
        c[23] = p.ka_ie
        c[24] = p.Ji_cdc20
        c[25] = p.Ja_cdc20
        c[26] = p.ki_cdc20
        c[27] = p.kd_cdc20
        c[28] = p.ka_cdc20
        c[29] = p.ks_cdc20_1
        c[30] = p.ks_cdc20_2
        c[31] = p.Js_cdc20
        c[32] = p.Ji_cdh
        c[33] = p.Ja_cdh
        c[34] = p.ki_cdh
        c[35] = p.ka_cdh_1
        c[36] = p.ki_cdh_1
        c[37] = p.ka_cdh_2
        c[38] = p.ks_cln
        c[39] = p.kd_cln
        c[40] = p.Ji_sbf
        c[41] = p.Ja_sbf
        c[42] = p.ki_sbf_1
        c[43] = p.ka_sbf_1
        c[44] = p.ki_sbf_2
        c[45] = p.ka_sbf_2
        c[46] = p.ks_swe
        c[47] = p.ks_sweC
        c[48] = p.khsl1
        c[49] = p.khsl1r
        c[50] = p.kd_swe_1
        c[51] = p.Ji_wee
        c[52] = p.Ja_wee
        c[53] = p.Vi_wee
        c[54] = p.Va_wee
        c[55] = p.kd_swe_2
        c[56] = p.ks_bud
        c[57] = p.kd_bud
        c[58] = p.mu
        c[59] = p.IE_total
        c[60] = p.Cdh1_total
        c[61] = p.Mih1_total
        c[62] = p.Mcm_total
        c[63] = p.SBF_total
        c[64] = p.kswe_1
        c[65] = p.kswe_2
        c[66] = p.kswe_3
        c[67] = p.kmih_1
        c[68] = p.kmih_2

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
