# Size of variable arrays:
sizeAlgebraic = 2
sizeStates = 34
sizeConstants = 55
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (minute)"
    legend_states[0] = "v_c in component v_c (nanomolar)"
    legend_algebraic[0] = "dv_c_dt in component dv_c_dt (flux)"
    legend_constants[0] = "k_growth in component rate_constants (first_order_rate_constant)"
    legend_states[1] = "v_n in component v_n (nanomolar)"
    legend_algebraic[1] = "k_volume in component k_volume (dimensionless)"
    legend_states[2] = "mcln2_c in component mcln2_c (nanomolar)"
    legend_constants[1] = "k_50 in component rate_constants (first_order_rate_constant)"
    legend_constants[2] = "k_10 in component rate_constants (first_order_rate_constant)"
    legend_states[3] = "mcln2_n in component mcln2_n (nanomolar)"
    legend_states[4] = "mclb5_c in component mclb5_c (nanomolar)"
    legend_constants[3] = "k_51 in component rate_constants (first_order_rate_constant)"
    legend_constants[4] = "k_11 in component rate_constants (first_order_rate_constant)"
    legend_states[5] = "mclb5_n in component mclb5_n (nanomolar)"
    legend_constants[5] = "k_1 in component rate_constants (first_order_rate_constant)"
    legend_states[6] = "sbf_n in component sbf_n (nanomolar)"
    legend_constants[6] = "k_2 in component rate_constants (first_order_rate_constant)"
    legend_constants[7] = "k_39 in component rate_constants (first_order_rate_constant)"
    legend_constants[8] = "k_34 in component rate_constants (second_order_rate_constant)"
    legend_constants[9] = "k_35 in component rate_constants (first_order_rate_constant)"
    legend_states[7] = "sbfwhi5p_n in component sbfwhi5p_n (nanomolar)"
    legend_states[8] = "whi5_n in component whi5_n (nanomolar)"
    legend_states[9] = "sbfwhi5_n in component sbfwhi5_n (nanomolar)"
    legend_states[10] = "cln3_c in component cln3_c (nanomolar)"
    legend_constants[10] = "k_6 in component rate_constants (flux)"
    legend_constants[11] = "k_43 in component rate_constants (first_order_rate_constant)"
    legend_constants[12] = "k_15 in component rate_constants (first_order_rate_constant)"
    legend_states[11] = "cln2_c in component cln2_c (nanomolar)"
    legend_constants[13] = "k_3 in component rate_constants (first_order_rate_constant)"
    legend_constants[14] = "k_26 in component rate_constants (second_order_rate_constant)"
    legend_constants[15] = "k_27 in component rate_constants (first_order_rate_constant)"
    legend_constants[16] = "k_12 in component rate_constants (first_order_rate_constant)"
    legend_states[12] = "cdk1_c in component cdk1_c (nanomolar)"
    legend_states[13] = "cdk1cln2_c in component cdk1cln2_c (nanomolar)"
    legend_states[14] = "clb5_c in component clb5_c (nanomolar)"
    legend_constants[17] = "k_4 in component rate_constants (first_order_rate_constant)"
    legend_constants[18] = "k_28 in component rate_constants (second_order_rate_constant)"
    legend_constants[19] = "k_29 in component rate_constants (first_order_rate_constant)"
    legend_constants[20] = "k_13 in component rate_constants (first_order_rate_constant)"
    legend_states[15] = "cdk1clb5_c in component cdk1clb5_c (nanomolar)"
    legend_constants[21] = "k_7 in component rate_constants (flux)"
    legend_constants[22] = "k_44 in component rate_constants (first_order_rate_constant)"
    legend_constants[23] = "k_49 in component rate_constants (first_order_rate_constant)"
    legend_constants[24] = "k_16 in component rate_constants (first_order_rate_constant)"
    legend_states[16] = "cdk1_n in component cdk1_n (nanomolar)"
    legend_states[17] = "cln3_n in component cln3_n (nanomolar)"
    legend_constants[25] = "k_24 in component rate_constants (second_order_rate_constant)"
    legend_constants[26] = "k_25 in component rate_constants (first_order_rate_constant)"
    legend_constants[27] = "k_20 in component rate_constants (first_order_rate_constant)"
    legend_states[18] = "cdk1cln3_n in component cdk1cln3_n (nanomolar)"
    legend_constants[28] = "k_21 in component rate_constants (first_order_rate_constant)"
    legend_constants[29] = "k_46 in component rate_constants (first_order_rate_constant)"
    legend_constants[30] = "k_53 in component rate_constants (first_order_rate_constant)"
    legend_states[19] = "cdk1cln2_n in component cdk1cln2_n (nanomolar)"
    legend_constants[31] = "k_33 in component rate_constants (first_order_rate_constant)"
    legend_constants[32] = "k_32 in component rate_constants (second_order_rate_constant)"
    legend_constants[33] = "k_48 in component rate_constants (first_order_rate_constant)"
    legend_states[20] = "cdk1clb5sic1_c in component cdk1clb5sic1_c (nanomolar)"
    legend_states[21] = "sic1_c in component sic1_c (nanomolar)"
    legend_states[22] = "cdk1clb5_n in component cdk1clb5_n (nanomolar)"
    legend_constants[34] = "k_41 in component rate_constants (first_order_rate_constant)"
    legend_states[23] = "cdk1clb5sic1p_n in component cdk1clb5sic1p_n (nanomolar)"
    legend_constants[35] = "k_31 in component rate_constants (first_order_rate_constant)"
    legend_constants[36] = "k_30 in component rate_constants (second_order_rate_constant)"
    legend_constants[37] = "k_40 in component rate_constants (first_order_rate_constant)"
    legend_states[24] = "cdk1cln3far1_n in component cdk1cln3far1_n (nanomolar)"
    legend_states[25] = "far1_n in component far1_n (nanomolar)"
    legend_states[26] = "cdk1cln3far1p_n in component cdk1cln3far1p_n (nanomolar)"
    legend_constants[38] = "k_36 in component rate_constants (second_order_rate_constant)"
    legend_constants[39] = "k_37 in component rate_constants (second_order_rate_constant)"
    legend_states[27] = "cdk1clb5sic1_n in component cdk1clb5sic1_n (nanomolar)"
    legend_constants[40] = "k_47 in component rate_constants (first_order_rate_constant)"
    legend_constants[41] = "k_38 in component rate_constants (second_order_rate_constant)"
    legend_constants[42] = "k_9 in component rate_constants (flux)"
    legend_constants[43] = "k_18 in component rate_constants (first_order_rate_constant)"
    legend_states[28] = "whi5_c in component whi5_c (nanomolar)"
    legend_constants[44] = "k_8 in component rate_constants (flux)"
    legend_constants[45] = "k_45 in component rate_constants (first_order_rate_constant)"
    legend_constants[46] = "k_17 in component rate_constants (first_order_rate_constant)"
    legend_states[29] = "far1_c in component far1_c (nanomolar)"
    legend_constants[47] = "k_5 in component rate_constants (flux)"
    legend_constants[48] = "k_42 in component rate_constants (first_order_rate_constant)"
    legend_constants[49] = "k_14 in component rate_constants (first_order_rate_constant)"
    legend_states[30] = "whi5p_c in component whi5p_c (nanomolar)"
    legend_constants[50] = "k_52 in component rate_constants (first_order_rate_constant)"
    legend_states[31] = "whi5p_n in component whi5p_n (nanomolar)"
    legend_states[32] = "sic1P_n in component sic1P_n (nanomolar)"
    legend_states[33] = "far1P_n in component far1P_n (nanomolar)"
    legend_constants[51] = "k_22 in component rate_constants (first_order_rate_constant)"
    legend_constants[52] = "k_19 in component rate_constants (first_order_rate_constant)"
    legend_constants[53] = "k_23 in component rate_constants (first_order_rate_constant)"
    legend_rates[0] = "d/dt v_c in component v_c (nanomolar)"
    legend_rates[1] = "d/dt v_n in component v_n (nanomolar)"
    legend_rates[2] = "d/dt mcln2_c in component mcln2_c (nanomolar)"
    legend_rates[4] = "d/dt mclb5_c in component mclb5_c (nanomolar)"
    legend_rates[3] = "d/dt mcln2_n in component mcln2_n (nanomolar)"
    legend_rates[5] = "d/dt mclb5_n in component mclb5_n (nanomolar)"
    legend_rates[6] = "d/dt sbf_n in component sbf_n (nanomolar)"
    legend_rates[10] = "d/dt cln3_c in component cln3_c (nanomolar)"
    legend_rates[11] = "d/dt cln2_c in component cln2_c (nanomolar)"
    legend_rates[14] = "d/dt clb5_c in component clb5_c (nanomolar)"
    legend_rates[12] = "d/dt cdk1_c in component cdk1_c (nanomolar)"
    legend_rates[17] = "d/dt cln3_n in component cln3_n (nanomolar)"
    legend_rates[16] = "d/dt cdk1_n in component cdk1_n (nanomolar)"
    legend_rates[13] = "d/dt cdk1cln2_c in component cdk1cln2_c (nanomolar)"
    legend_rates[15] = "d/dt cdk1clb5_c in component cdk1clb5_c (nanomolar)"
    legend_rates[19] = "d/dt cdk1cln2_n in component cdk1cln2_n (nanomolar)"
    legend_rates[22] = "d/dt cdk1clb5_n in component cdk1clb5_n (nanomolar)"
    legend_rates[18] = "d/dt cdk1cln3_n in component cdk1cln3_n (nanomolar)"
    legend_rates[9] = "d/dt sbfwhi5_n in component sbfwhi5_n (nanomolar)"
    legend_rates[7] = "d/dt sbfwhi5p_n in component sbfwhi5p_n (nanomolar)"
    legend_rates[24] = "d/dt cdk1cln3far1_n in component cdk1cln3far1_n (nanomolar)"
    legend_rates[27] = "d/dt cdk1clb5sic1_n in component cdk1clb5sic1_n (nanomolar)"
    legend_rates[23] = "d/dt cdk1clb5sic1p_n in component cdk1clb5sic1p_n (nanomolar)"
    legend_rates[26] = "d/dt cdk1cln3far1p_n in component cdk1cln3far1p_n (nanomolar)"
    legend_rates[20] = "d/dt cdk1clb5sic1_c in component cdk1clb5sic1_c (nanomolar)"
    legend_rates[21] = "d/dt sic1_c in component sic1_c (nanomolar)"
    legend_rates[28] = "d/dt whi5_c in component whi5_c (nanomolar)"
    legend_rates[29] = "d/dt far1_c in component far1_c (nanomolar)"
    legend_rates[30] = "d/dt whi5p_c in component whi5p_c (nanomolar)"
    legend_rates[32] = "d/dt sic1P_n in component sic1P_n (nanomolar)"
    legend_rates[33] = "d/dt far1P_n in component far1P_n (nanomolar)"
    legend_rates[8] = "d/dt whi5_n in component whi5_n (nanomolar)"
    legend_rates[25] = "d/dt far1_n in component far1_n (nanomolar)"
    legend_rates[31] = "d/dt whi5p_n in component whi5p_n (nanomolar)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 0.5
    constants[0] = 0.0051
    states[1] = 0.5
    states[2] = 0
    constants[1] = 0.6
    constants[2] = 0.12
    states[3] = 0
    states[4] = 0
    constants[3] = 0.6
    constants[4] = 0.12
    states[5] = 0
    constants[5] = 0.03523
    states[6] = 0
    constants[6] = 0.03523
    constants[7] = 1
    constants[8] = 8.46
    constants[9] = 0.0005
    states[7] = 0
    states[8] = 0
    states[9] = 0.025544
    states[10] = 0.000485
    constants[10] = 0.00001
    constants[11] = 0.005
    constants[12] = 0.01
    states[11] = 0
    constants[13] = 0.32
    constants[14] = 2.82
    constants[15] = 0.55
    constants[16] = 0.1
    states[12] = 0.333333
    states[13] = 0
    states[14] = 0
    constants[17] = 0.32
    constants[18] = 2.82
    constants[19] = 0.55
    constants[20] = 0.35
    states[15] = 0
    constants[21] = 0.01
    constants[22] = 0.005
    constants[23] = 0.001
    constants[24] = 0.03
    states[16] = 0.0074127
    states[17] = 0
    constants[25] = 2.82
    constants[26] = 0.55
    constants[27] = 0.01
    states[18] = 0
    constants[28] = 0
    constants[29] = 0.1
    constants[30] = 0.001
    states[19] = 0
    constants[31] = 0.55
    constants[32] = 84.6
    constants[33] = 0.012
    states[20] = 0
    states[21] = 0.039234
    states[22] = 0
    constants[34] = 1
    states[23] = 0
    constants[35] = 0.55
    constants[36] = 42300
    constants[37] = 1
    states[24] = 0
    states[25] = 0
    states[26] = 0
    constants[38] = 4363.6
    constants[39] = 4363.6
    states[27] = 0
    constants[40] = 1
    constants[41] = 4363.6
    constants[42] = 0.00005
    constants[43] = 0.0008
    states[28] = 0.073564
    constants[44] = 0.00004
    constants[45] = 0.005
    constants[46] = 0.01
    states[29] = 0.0037926
    constants[47] = 0.000042
    constants[48] = 0.005
    constants[49] = 0.01
    states[30] = 0
    constants[50] = 0.005
    states[31] = 0
    states[32] = 0
    states[33] = 0
    constants[51] = 0.01
    constants[52] = 0.01
    constants[53] = 0.01
    constants[54] = 0.00000
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[1] = constants[54]
    rates[3] = constants[5]*states[6]-constants[1]*states[3]
    rates[5] = constants[6]*states[6]-constants[3]*states[5]
    rates[6] = (constants[7]*states[7]-constants[8]*states[6]*states[8])+constants[9]*states[9]
    rates[18] = (((constants[25]*states[17]*states[16]-constants[26]*states[18])+constants[35]*states[24])-constants[36]*states[25]*states[18])+constants[37]*states[26]
    rates[9] = (constants[8]*states[6]*states[8]-constants[9]*states[9])-constants[38]*states[9]*states[18]
    rates[7] = constants[38]*states[9]*states[18]-constants[7]*states[7]
    rates[24] = (constants[36]*states[25]*states[18]-constants[35]*states[24])-constants[39]*states[24]*states[19]
    rates[23] = constants[41]*states[27]*states[19]-constants[34]*states[23]
    rates[26] = constants[39]*states[24]*states[19]-constants[37]*states[26]
    rates[32] = constants[34]*states[23]
    rates[33] = constants[37]*states[26]
    rates[31] = (constants[7]*states[7]-constants[50]*states[31])-constants[53]*states[31]
    algebraic[0] = constants[0]*states[0]
    rates[0] = algebraic[0]
    rates[10] = ((constants[10]-constants[11]*states[10])-constants[12]*states[10])-(algebraic[0]/states[0])*states[10]
    rates[11] = (((constants[13]*states[2]-constants[14]*states[12]*states[11])+constants[15]*states[13])-constants[16]*states[11])-(algebraic[0]/states[0])*states[11]
    rates[14] = (((constants[17]*states[4]-constants[18]*states[14]*states[12])+constants[19]*states[15])-constants[20]*states[14])-(algebraic[0]/states[0])*states[14]
    rates[12] = ((((((constants[21]-constants[22]*states[12])+constants[23]*states[16]+constants[15]*states[13])-constants[14]*states[12]*states[11])-constants[18]*states[12]*states[14])+constants[19]*states[15])-constants[24]*states[12])-(algebraic[0]/states[0])*states[12]
    rates[15] = ((((constants[18]*states[12]*states[14]-constants[19]*states[15])+constants[31]*states[20])-constants[32]*states[21]*states[15])-constants[33]*states[15])-(algebraic[0]/states[0])*states[15]
    rates[20] = ((constants[32]*states[21]*states[15]-constants[31]*states[20])-constants[40]*states[20])-(algebraic[0]/states[0])*states[20]
    rates[21] = (((constants[42]-constants[32]*states[21]*states[15])+constants[31]*states[20])-constants[43]*states[21])-(algebraic[0]/states[0])*states[21]
    rates[28] = ((constants[44]-constants[45]*states[28])-constants[46]*states[28])-(algebraic[0]/states[0])*states[28]
    rates[29] = ((constants[47]-constants[48]*states[29])-constants[49]*states[29])-(algebraic[0]/states[0])*states[29]
    algebraic[1] = states[1]/states[0]
    rates[2] = (constants[1]*states[3]*algebraic[1]-constants[2]*states[2])-(algebraic[0]/states[0])*states[2]
    rates[4] = (constants[3]*states[5]*algebraic[1]-constants[4]*states[4])-(algebraic[0]/states[0])*states[4]
    rates[17] = (((constants[11]*states[10])/algebraic[1]-constants[25]*states[17]*states[16])+constants[26]*states[18])-constants[27]*states[17]
    rates[16] = ((((constants[22]*states[12])/algebraic[1]-constants[23]*states[16])-constants[25]*states[17]*states[16])+constants[26]*states[18])-constants[28]*states[16]
    rates[13] = (((constants[14]*states[12]*states[11]-constants[15]*states[13])-constants[29]*states[13])+constants[30]*states[19]*algebraic[1])-(algebraic[0]/states[0])*states[13]
    rates[19] = (constants[29]*states[13])/algebraic[1]-constants[30]*states[19]
    rates[22] = constants[34]*states[23]+(constants[33]*states[15])/algebraic[1]
    rates[27] = (constants[40]*states[20])/algebraic[1]-constants[41]*states[27]*states[19]
    rates[30] = constants[50]*states[31]*algebraic[1]
    rates[8] = ((constants[45]*states[28])/algebraic[1]-constants[8]*states[8]*states[6])-constants[51]*states[8]
    rates[25] = (((constants[48]*states[29])/algebraic[1]-constants[36]*states[25]*states[18])+constants[35]*states[24])-constants[52]*states[25]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = constants[0]*states[0]
    algebraic[1] = states[1]/states[0]
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
        self.k_growth = 0.0051
        self.k_50 = 0.6
        self.k_10 = 0.12
        self.k_51 = 0.6
        self.k_11 = 0.12
        self.k_1 = 0.03523
        self.k_2 = 0.03523
        self.k_39 = 1
        self.k_34 = 8.46
        self.k_35 = 0.0005
        self.k_6 = 0.00001
        self.k_43 = 0.005
        self.k_15 = 0.01
        self.k_3 = 0.32
        self.k_26 = 2.82
        self.k_27 = 0.55
        self.k_12 = 0.1
        self.k_4 = 0.32
        self.k_28 = 2.82
        self.k_29 = 0.55
        self.k_13 = 0.35
        self.k_7 = 0.01
        self.k_44 = 0.005
        self.k_49 = 0.001
        self.k_16 = 0.03
        self.k_24 = 2.82
        self.k_25 = 0.55
        self.k_20 = 0.01
        self.k_21 = 0
        self.k_46 = 0.1
        self.k_53 = 0.001
        self.k_33 = 0.55
        self.k_32 = 84.6
        self.k_48 = 0.012
        self.k_41 = 1
        self.k_31 = 0.55
        self.k_30 = 42300
        self.k_40 = 1
        self.k_36 = 4363.6
        self.k_37 = 4363.6
        self.k_47 = 1
        self.k_38 = 4363.6
        self.k_9 = 0.00005
        self.k_18 = 0.0008
        self.k_8 = 0.00004
        self.k_45 = 0.005
        self.k_17 = 0.01
        self.k_5 = 0.000042
        self.k_42 = 0.005
        self.k_14 = 0.01
        self.k_52 = 0.005
        self.k_22 = 0.01
        self.k_19 = 0.01
        self.k_23 = 0.01
        self.legend_constants_54 = 0.00000

    def to_dict(self):
        return {
            "k_growth": self.k_growth,
            "k_50": self.k_50,
            "k_10": self.k_10,
            "k_51": self.k_51,
            "k_11": self.k_11,
            "k_1": self.k_1,
            "k_2": self.k_2,
            "k_39": self.k_39,
            "k_34": self.k_34,
            "k_35": self.k_35,
            "k_6": self.k_6,
            "k_43": self.k_43,
            "k_15": self.k_15,
            "k_3": self.k_3,
            "k_26": self.k_26,
            "k_27": self.k_27,
            "k_12": self.k_12,
            "k_4": self.k_4,
            "k_28": self.k_28,
            "k_29": self.k_29,
            "k_13": self.k_13,
            "k_7": self.k_7,
            "k_44": self.k_44,
            "k_49": self.k_49,
            "k_16": self.k_16,
            "k_24": self.k_24,
            "k_25": self.k_25,
            "k_20": self.k_20,
            "k_21": self.k_21,
            "k_46": self.k_46,
            "k_53": self.k_53,
            "k_33": self.k_33,
            "k_32": self.k_32,
            "k_48": self.k_48,
            "k_41": self.k_41,
            "k_31": self.k_31,
            "k_30": self.k_30,
            "k_40": self.k_40,
            "k_36": self.k_36,
            "k_37": self.k_37,
            "k_47": self.k_47,
            "k_38": self.k_38,
            "k_9": self.k_9,
            "k_18": self.k_18,
            "k_8": self.k_8,
            "k_45": self.k_45,
            "k_17": self.k_17,
            "k_5": self.k_5,
            "k_42": self.k_42,
            "k_14": self.k_14,
            "k_52": self.k_52,
            "k_22": self.k_22,
            "k_19": self.k_19,
            "k_23": self.k_23,
            "legend_constants_54": self.legend_constants_54,
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
        y0=[0.5, 0.5, 0, 0, 0, 0, 0, 0, 0, 0.025544, 0.000485, 0, 0.333333, 0, 0, 0, 0.0074127, 0, 0, 0, 0, 0.039234, 0, 0, 0, 0, 0, 0, 0.073564, 0.0037926, 0, 0, 0, 0],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "barberis_klipp_vanoni_alberghina_2007"
        self.curve_names = [
            "v_c",
            "v_n",
            "mcln2_c",
            "mcln2_n",
            "mclb5_c",
            "mclb5_n",
            "sbf_n",
            "sbfwhi5p_n",
            "whi5_n",
            "sbfwhi5_n",
            "cln3_c",
            "cln2_c",
            "cdk1_c",
            "cdk1cln2_c",
            "clb5_c",
            "cdk1clb5_c",
            "cdk1_n",
            "cln3_n",
            "cdk1cln3_n",
            "cdk1cln2_n",
            "cdk1clb5sic1_c",
            "sic1_c",
            "cdk1clb5_n",
            "cdk1clb5sic1p_n",
            "cdk1cln3far1_n",
            "far1_n",
            "cdk1cln3far1p_n",
            "cdk1clb5sic1_n",
            "whi5_c",
            "far1_c",
            "whi5p_c",
            "whi5p_n",
            "sic1P_n",
            "far1P_n",
        ]
        self.state_names = ['v_c', 'v_n', 'mcln2_c', 'mcln2_n', 'mclb5_c', 'mclb5_n', 'sbf_n', 'sbfwhi5p_n', 'whi5_n', 'sbfwhi5_n', 'cln3_c', 'cln2_c', 'cdk1_c', 'cdk1cln2_c', 'clb5_c', 'cdk1clb5_c', 'cdk1_n', 'cln3_n', 'cdk1cln3_n', 'cdk1cln2_n', 'cdk1clb5sic1_c', 'sic1_c', 'cdk1clb5_n', 'cdk1clb5sic1p_n', 'cdk1cln3far1_n', 'far1_n', 'cdk1cln3far1p_n', 'cdk1clb5sic1_n', 'whi5_c', 'far1_c', 'whi5p_c', 'whi5p_n', 'sic1P_n', 'far1P_n']
        self.algebraic_names = ['dv_c_dt', 'k_volume']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 55
        p = self.params

        # direct mapping
        c[0] = p.k_growth
        c[1] = p.k_50
        c[2] = p.k_10
        c[3] = p.k_51
        c[4] = p.k_11
        c[5] = p.k_1
        c[6] = p.k_2
        c[7] = p.k_39
        c[8] = p.k_34
        c[9] = p.k_35
        c[10] = p.k_6
        c[11] = p.k_43
        c[12] = p.k_15
        c[13] = p.k_3
        c[14] = p.k_26
        c[15] = p.k_27
        c[16] = p.k_12
        c[17] = p.k_4
        c[18] = p.k_28
        c[19] = p.k_29
        c[20] = p.k_13
        c[21] = p.k_7
        c[22] = p.k_44
        c[23] = p.k_49
        c[24] = p.k_16
        c[25] = p.k_24
        c[26] = p.k_25
        c[27] = p.k_20
        c[28] = p.k_21
        c[29] = p.k_46
        c[30] = p.k_53
        c[31] = p.k_33
        c[32] = p.k_32
        c[33] = p.k_48
        c[34] = p.k_41
        c[35] = p.k_31
        c[36] = p.k_30
        c[37] = p.k_40
        c[38] = p.k_36
        c[39] = p.k_37
        c[40] = p.k_47
        c[41] = p.k_38
        c[42] = p.k_9
        c[43] = p.k_18
        c[44] = p.k_8
        c[45] = p.k_45
        c[46] = p.k_17
        c[47] = p.k_5
        c[48] = p.k_42
        c[49] = p.k_14
        c[50] = p.k_52
        c[51] = p.k_22
        c[52] = p.k_19
        c[53] = p.k_23
        c[54] = p.legend_constants_54

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
