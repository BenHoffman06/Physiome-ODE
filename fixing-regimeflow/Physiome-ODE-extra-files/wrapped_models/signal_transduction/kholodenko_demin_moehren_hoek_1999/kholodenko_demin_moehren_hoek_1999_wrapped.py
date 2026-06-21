# Size of variable arrays:
sizeAlgebraic = 32
sizeStates = 23
sizeConstants = 50
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (second)"
    legend_states[0] = "EGF in component EGF (nanomolar)"
    legend_algebraic[0] = "v1 in component v1 (flux)"
    legend_states[1] = "R in component R (nanomolar)"
    legend_states[2] = "Ra in component Ra (nanomolar)"
    legend_algebraic[8] = "v2 in component v2 (flux)"
    legend_states[3] = "R2 in component R2 (nanomolar)"
    legend_algebraic[9] = "v3 in component v3 (flux)"
    legend_algebraic[10] = "v4 in component v4 (flux)"
    legend_states[4] = "RP in component RP (nanomolar)"
    legend_algebraic[13] = "v7 in component v7 (flux)"
    legend_algebraic[18] = "v11 in component v11 (flux)"
    legend_algebraic[22] = "v15 in component v15 (flux)"
    legend_algebraic[25] = "v18 in component v18 (flux)"
    legend_algebraic[27] = "v20 in component v20 (flux)"
    legend_algebraic[11] = "v5 in component v5 (flux)"
    legend_algebraic[14] = "v9 in component v9 (flux)"
    legend_algebraic[20] = "v13 in component v13 (flux)"
    legend_states[5] = "R_PL in component R_PL (nanomolar)"
    legend_algebraic[12] = "v6 in component v6 (flux)"
    legend_states[6] = "R_PLP in component R_PLP (nanomolar)"
    legend_states[7] = "R_G in component R_G (nanomolar)"
    legend_algebraic[16] = "v10 in component v10 (flux)"
    legend_states[8] = "R_G_S in component R_G_S (nanomolar)"
    legend_states[9] = "R_Sh in component R_Sh (nanomolar)"
    legend_algebraic[21] = "v14 in component v14 (flux)"
    legend_states[10] = "R_ShP in component R_ShP (nanomolar)"
    legend_algebraic[31] = "v24 in component v24 (flux)"
    legend_algebraic[24] = "v17 in component v17 (flux)"
    legend_states[11] = "R_Sh_G in component R_Sh_G (nanomolar)"
    legend_algebraic[26] = "v19 in component v19 (flux)"
    legend_states[12] = "R_Sh_G_S in component R_Sh_G_S (nanomolar)"
    legend_states[13] = "G_S in component G_S (nanomolar)"
    legend_algebraic[30] = "v23 in component v23 (flux)"
    legend_algebraic[19] = "v12 in component v12 (flux)"
    legend_states[14] = "ShP in component ShP (nanomolar)"
    legend_algebraic[28] = "v21 in component v21 (flux)"
    legend_algebraic[23] = "v16 in component v16 (flux)"
    legend_states[15] = "Sh_G in component Sh_G (nanomolar)"
    legend_algebraic[29] = "v22 in component v22 (flux)"
    legend_states[16] = "Sh_G_S in component Sh_G_S (nanomolar)"
    legend_states[17] = "PLC_gamma in component PLC_gamma (nanomolar)"
    legend_algebraic[15] = "v8 in component v8 (flux)"
    legend_states[18] = "PLC_gamma_P in component PLC_gamma_P (nanomolar)"
    legend_algebraic[17] = "v25 in component v25 (flux)"
    legend_states[19] = "PLC_gamma_P_I in component PLC_gamma_P_I (nanomolar)"
    legend_states[20] = "Grb in component Grb (nanomolar)"
    legend_states[21] = "Shc in component Shc (nanomolar)"
    legend_states[22] = "SOS in component SOS (nanomolar)"
    legend_constants[0] = "k1 in component v1 (second_order_rate_constant)"
    legend_constants[1] = "k1_ in component v1 (first_order_rate_constant)"
    legend_constants[2] = "k2 in component v2 (second_order_rate_constant)"
    legend_constants[3] = "k2_ in component v2 (first_order_rate_constant)"
    legend_constants[4] = "k3 in component v3 (first_order_rate_constant)"
    legend_constants[5] = "k3_ in component v3 (first_order_rate_constant)"
    legend_constants[6] = "K4 in component v4 (nanomolar)"
    legend_constants[7] = "V4 in component v4 (flux)"
    legend_constants[8] = "k5 in component v5 (second_order_rate_constant)"
    legend_constants[9] = "k5_ in component v5 (first_order_rate_constant)"
    legend_constants[10] = "k6 in component v6 (first_order_rate_constant)"
    legend_constants[11] = "k6_ in component v6 (first_order_rate_constant)"
    legend_constants[12] = "k7 in component v7 (first_order_rate_constant)"
    legend_constants[13] = "k7_ in component v7 (second_order_rate_constant)"
    legend_constants[14] = "K8 in component v8 (nanomolar)"
    legend_constants[15] = "V8 in component v8 (flux)"
    legend_constants[16] = "k9 in component v9 (second_order_rate_constant)"
    legend_constants[17] = "k9_ in component v9 (first_order_rate_constant)"
    legend_constants[18] = "k10 in component v10 (second_order_rate_constant)"
    legend_constants[19] = "k10_ in component v10 (first_order_rate_constant)"
    legend_constants[20] = "k11 in component v11 (first_order_rate_constant)"
    legend_constants[21] = "k11_ in component v11 (second_order_rate_constant)"
    legend_constants[22] = "k12 in component v12 (first_order_rate_constant)"
    legend_constants[23] = "k12_ in component v12 (second_order_rate_constant)"
    legend_constants[24] = "k13 in component v13 (second_order_rate_constant)"
    legend_constants[25] = "k13_ in component v13 (first_order_rate_constant)"
    legend_constants[26] = "k14 in component v14 (first_order_rate_constant)"
    legend_constants[27] = "k14_ in component v14 (first_order_rate_constant)"
    legend_constants[28] = "k15 in component v15 (first_order_rate_constant)"
    legend_constants[29] = "k15_ in component v15 (second_order_rate_constant)"
    legend_constants[30] = "K16 in component v16 (nanomolar)"
    legend_constants[31] = "V16 in component v16 (flux)"
    legend_constants[32] = "k17 in component v17 (second_order_rate_constant)"
    legend_constants[33] = "k17_ in component v17 (first_order_rate_constant)"
    legend_constants[34] = "k18 in component v18 (first_order_rate_constant)"
    legend_constants[35] = "k18_ in component v18 (second_order_rate_constant)"
    legend_constants[36] = "k19 in component v19 (second_order_rate_constant)"
    legend_constants[37] = "k19_ in component v19 (first_order_rate_constant)"
    legend_constants[38] = "k20 in component v20 (first_order_rate_constant)"
    legend_constants[39] = "k20_ in component v20 (second_order_rate_constant)"
    legend_constants[40] = "k21 in component v21 (second_order_rate_constant)"
    legend_constants[41] = "k21_ in component v21 (first_order_rate_constant)"
    legend_constants[42] = "k22 in component v22 (second_order_rate_constant)"
    legend_constants[43] = "k22_ in component v22 (first_order_rate_constant)"
    legend_constants[44] = "k23 in component v23 (first_order_rate_constant)"
    legend_constants[45] = "k23_ in component v23 (second_order_rate_constant)"
    legend_constants[46] = "k24 in component v24 (second_order_rate_constant)"
    legend_constants[47] = "k24_ in component v24 (first_order_rate_constant)"
    legend_constants[48] = "k25 in component v25 (first_order_rate_constant)"
    legend_constants[49] = "k25_ in component v25 (first_order_rate_constant)"
    legend_algebraic[1] = "totEGFRphos in component combined_concs (nanomolar)"
    legend_algebraic[2] = "totPLCgammaphos in component combined_concs (nanomolar)"
    legend_algebraic[3] = "totGrb_EGFR in component combined_concs (nanomolar)"
    legend_algebraic[4] = "totGrb_Shc in component combined_concs (nanomolar)"
    legend_algebraic[5] = "totShcphos in component combined_concs (nanomolar)"
    legend_algebraic[6] = "totShc_EGFR in component combined_concs (nanomolar)"
    legend_algebraic[7] = "totSOS_EGFR in component combined_concs (nanomolar)"
    legend_rates[0] = "d/dt EGF in component EGF (nanomolar)"
    legend_rates[1] = "d/dt R in component R (nanomolar)"
    legend_rates[2] = "d/dt Ra in component Ra (nanomolar)"
    legend_rates[3] = "d/dt R2 in component R2 (nanomolar)"
    legend_rates[4] = "d/dt RP in component RP (nanomolar)"
    legend_rates[5] = "d/dt R_PL in component R_PL (nanomolar)"
    legend_rates[6] = "d/dt R_PLP in component R_PLP (nanomolar)"
    legend_rates[7] = "d/dt R_G in component R_G (nanomolar)"
    legend_rates[8] = "d/dt R_G_S in component R_G_S (nanomolar)"
    legend_rates[9] = "d/dt R_Sh in component R_Sh (nanomolar)"
    legend_rates[10] = "d/dt R_ShP in component R_ShP (nanomolar)"
    legend_rates[11] = "d/dt R_Sh_G in component R_Sh_G (nanomolar)"
    legend_rates[12] = "d/dt R_Sh_G_S in component R_Sh_G_S (nanomolar)"
    legend_rates[13] = "d/dt G_S in component G_S (nanomolar)"
    legend_rates[14] = "d/dt ShP in component ShP (nanomolar)"
    legend_rates[15] = "d/dt Sh_G in component Sh_G (nanomolar)"
    legend_rates[16] = "d/dt Sh_G_S in component Sh_G_S (nanomolar)"
    legend_rates[17] = "d/dt PLC_gamma in component PLC_gamma (nanomolar)"
    legend_rates[18] = "d/dt PLC_gamma_P in component PLC_gamma_P (nanomolar)"
    legend_rates[19] = "d/dt PLC_gamma_P_I in component PLC_gamma_P_I (nanomolar)"
    legend_rates[20] = "d/dt Grb in component Grb (nanomolar)"
    legend_rates[21] = "d/dt Shc in component Shc (nanomolar)"
    legend_rates[22] = "d/dt SOS in component SOS (nanomolar)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 680
    states[1] = 100
    states[2] = 0
    states[3] = 0
    states[4] = 0
    states[5] = 0
    states[6] = 0
    states[7] = 0
    states[8] = 0
    states[9] = 0
    states[10] = 0
    states[11] = 0
    states[12] = 0
    states[13] = 0
    states[14] = 0
    states[15] = 0
    states[16] = 0
    states[17] = 105
    states[18] = 0
    states[19] = 0
    states[20] = 85
    states[21] = 150
    states[22] = 34
    constants[0] = 0.003
    constants[1] = 0.06
    constants[2] = 0.01
    constants[3] = 0.1
    constants[4] = 1
    constants[5] = 0.01
    constants[6] = 50
    constants[7] = 450
    constants[8] = 0.06
    constants[9] = 0.2
    constants[10] = 1
    constants[11] = 0.05
    constants[12] = 0.3
    constants[13] = 0.006
    constants[14] = 100
    constants[15] = 1
    constants[16] = 0.003
    constants[17] = 0.05
    constants[18] = 0.01
    constants[19] = 0.06
    constants[20] = 0.03
    constants[21] = 4.5e-3
    constants[22] = 1.5e-3
    constants[23] = 1e-4
    constants[24] = 0.09
    constants[25] = 0.6
    constants[26] = 6
    constants[27] = 0.06
    constants[28] = 0.3
    constants[29] = 9e-4
    constants[30] = 340
    constants[31] = 1.7
    constants[32] = 0.003
    constants[33] = 0.1
    constants[34] = 0.3
    constants[35] = 9e-4
    constants[36] = 0.01
    constants[37] = 2.14e-2
    constants[38] = 0.12
    constants[39] = 2.4e-4
    constants[40] = 0.003
    constants[41] = 0.1
    constants[42] = 0.03
    constants[43] = 0.064
    constants[44] = 0.1
    constants[45] = 0.021
    constants[46] = 0.009
    constants[47] = 4.29e-2
    constants[48] = 1
    constants[49] = 0.03
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[0] = constants[0]*states[1]*states[0]-constants[1]*states[2]
    rates[0] = -algebraic[0]
    rates[1] = -algebraic[0]
    algebraic[8] = constants[2]*states[2]*states[2]-constants[3]*states[3]
    rates[2] = algebraic[0]-2.00000*algebraic[8]
    algebraic[9] = constants[4]*states[3]-constants[5]*states[4]
    algebraic[10] = (constants[7]*states[4])/(constants[6]+states[4])
    rates[3] = (algebraic[8]+algebraic[10])-algebraic[9]
    algebraic[11] = constants[8]*states[4]*states[17]-constants[9]*states[5]
    algebraic[12] = constants[10]*states[5]-constants[11]*states[6]
    rates[5] = algebraic[11]-algebraic[12]
    algebraic[13] = constants[12]*states[6]-constants[13]*states[4]*states[18]
    rates[6] = algebraic[12]-algebraic[13]
    algebraic[15] = (constants[15]*states[18])/(constants[14]+states[18])
    rates[17] = algebraic[15]-algebraic[11]
    algebraic[14] = constants[16]*states[4]*states[20]-constants[17]*states[7]
    algebraic[16] = constants[18]*states[7]*states[22]-constants[19]*states[8]
    rates[7] = algebraic[14]-algebraic[16]
    algebraic[17] = constants[48]*states[18]-constants[49]*states[19]
    rates[18] = algebraic[13]-(algebraic[15]+algebraic[17])
    rates[19] = algebraic[17]
    algebraic[18] = constants[20]*states[8]-constants[21]*states[4]*states[13]
    rates[8] = algebraic[16]-algebraic[18]
    algebraic[20] = constants[24]*states[4]*states[21]-constants[25]*states[9]
    algebraic[21] = constants[26]*states[9]-constants[27]*states[10]
    rates[9] = algebraic[20]-algebraic[21]
    algebraic[23] = (constants[31]*states[14])/(constants[30]+states[14])
    rates[21] = algebraic[23]-algebraic[20]
    algebraic[25] = constants[34]*states[11]-constants[35]*states[4]*states[15]
    algebraic[24] = constants[32]*states[10]*states[20]-constants[33]*states[11]
    algebraic[26] = constants[36]*states[11]*states[22]-constants[37]*states[12]
    rates[11] = algebraic[24]-(algebraic[25]+algebraic[26])
    algebraic[22] = constants[28]*states[10]-constants[29]*states[14]*states[4]
    algebraic[27] = constants[38]*states[12]-constants[39]*states[16]*states[4]
    rates[4] = (algebraic[9]+algebraic[13]+algebraic[18]+algebraic[22]+algebraic[25]+algebraic[27])-(algebraic[10]+algebraic[11]+algebraic[14]+algebraic[20])
    algebraic[19] = constants[22]*states[13]-constants[23]*states[20]*states[22]
    algebraic[28] = constants[40]*states[14]*states[20]-constants[41]*states[15]
    rates[20] = algebraic[19]-(algebraic[14]+algebraic[24]+algebraic[28])
    algebraic[29] = constants[42]*states[15]*states[22]-constants[43]*states[16]
    rates[15] = (algebraic[25]+algebraic[28])-algebraic[29]
    rates[22] = algebraic[19]-(algebraic[16]+algebraic[26]+algebraic[29])
    algebraic[30] = constants[44]*states[16]-constants[45]*states[14]*states[13]
    rates[14] = (algebraic[22]+algebraic[30])-(algebraic[28]+algebraic[23])
    rates[16] = (algebraic[27]+algebraic[29])-algebraic[30]
    algebraic[31] = constants[46]*states[10]*states[13]-constants[47]*states[12]
    rates[10] = algebraic[21]-(algebraic[31]+algebraic[22]+algebraic[24])
    rates[12] = (algebraic[26]+algebraic[31])-algebraic[27]
    rates[13] = (algebraic[18]+algebraic[30])-(algebraic[19]+algebraic[31])
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = constants[0]*states[1]*states[0]-constants[1]*states[2]
    algebraic[8] = constants[2]*states[2]*states[2]-constants[3]*states[3]
    algebraic[9] = constants[4]*states[3]-constants[5]*states[4]
    algebraic[10] = (constants[7]*states[4])/(constants[6]+states[4])
    algebraic[11] = constants[8]*states[4]*states[17]-constants[9]*states[5]
    algebraic[12] = constants[10]*states[5]-constants[11]*states[6]
    algebraic[13] = constants[12]*states[6]-constants[13]*states[4]*states[18]
    algebraic[15] = (constants[15]*states[18])/(constants[14]+states[18])
    algebraic[14] = constants[16]*states[4]*states[20]-constants[17]*states[7]
    algebraic[16] = constants[18]*states[7]*states[22]-constants[19]*states[8]
    algebraic[17] = constants[48]*states[18]-constants[49]*states[19]
    algebraic[18] = constants[20]*states[8]-constants[21]*states[4]*states[13]
    algebraic[20] = constants[24]*states[4]*states[21]-constants[25]*states[9]
    algebraic[21] = constants[26]*states[9]-constants[27]*states[10]
    algebraic[23] = (constants[31]*states[14])/(constants[30]+states[14])
    algebraic[25] = constants[34]*states[11]-constants[35]*states[4]*states[15]
    algebraic[24] = constants[32]*states[10]*states[20]-constants[33]*states[11]
    algebraic[26] = constants[36]*states[11]*states[22]-constants[37]*states[12]
    algebraic[22] = constants[28]*states[10]-constants[29]*states[14]*states[4]
    algebraic[27] = constants[38]*states[12]-constants[39]*states[16]*states[4]
    algebraic[19] = constants[22]*states[13]-constants[23]*states[20]*states[22]
    algebraic[28] = constants[40]*states[14]*states[20]-constants[41]*states[15]
    algebraic[29] = constants[42]*states[15]*states[22]-constants[43]*states[16]
    algebraic[30] = constants[44]*states[16]-constants[45]*states[14]*states[13]
    algebraic[31] = constants[46]*states[10]*states[13]-constants[47]*states[12]
    algebraic[1] = 2.00000*(states[4]+states[5]+states[6]+states[7]+states[8]+states[9]+states[10]+states[11]+states[12])
    algebraic[2] = states[6]+states[18]
    algebraic[3] = states[7]+states[8]+states[11]+states[12]
    algebraic[4] = states[11]+states[15]+states[12]+states[16]
    algebraic[5] = states[10]+states[11]+states[12]+states[14]+states[15]+states[16]
    algebraic[6] = states[10]+states[11]+states[12]
    algebraic[7] = states[8]+states[12]
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
        self.k1 = 0.003
        self.k1_ = 0.06
        self.k2 = 0.01
        self.k2_ = 0.1
        self.k3 = 1
        self.k3_ = 0.01
        self.K4 = 50
        self.V4 = 450
        self.k5 = 0.06
        self.k5_ = 0.2
        self.k6 = 1
        self.k6_ = 0.05
        self.k7 = 0.3
        self.k7_ = 0.006
        self.K8 = 100
        self.V8 = 1
        self.k9 = 0.003
        self.k9_ = 0.05
        self.k10 = 0.01
        self.k10_ = 0.06
        self.k11 = 0.03
        self.k11_ = 4.5e-3
        self.k12 = 1.5e-3
        self.k12_ = 1e-4
        self.k13 = 0.09
        self.k13_ = 0.6
        self.k14 = 6
        self.k14_ = 0.06
        self.k15 = 0.3
        self.k15_ = 9e-4
        self.K16 = 340
        self.V16 = 1.7
        self.k17 = 0.003
        self.k17_ = 0.1
        self.k18 = 0.3
        self.k18_ = 9e-4
        self.k19 = 0.01
        self.k19_ = 2.14e-2
        self.k20 = 0.12
        self.k20_ = 2.4e-4
        self.k21 = 0.003
        self.k21_ = 0.1
        self.k22 = 0.03
        self.k22_ = 0.064
        self.k23 = 0.1
        self.k23_ = 0.021
        self.k24 = 0.009
        self.k24_ = 4.29e-2
        self.k25 = 1
        self.k25_ = 0.03

    def to_dict(self):
        return {
            "k1": self.k1,
            "k1_": self.k1_,
            "k2": self.k2,
            "k2_": self.k2_,
            "k3": self.k3,
            "k3_": self.k3_,
            "K4": self.K4,
            "V4": self.V4,
            "k5": self.k5,
            "k5_": self.k5_,
            "k6": self.k6,
            "k6_": self.k6_,
            "k7": self.k7,
            "k7_": self.k7_,
            "K8": self.K8,
            "V8": self.V8,
            "k9": self.k9,
            "k9_": self.k9_,
            "k10": self.k10,
            "k10_": self.k10_,
            "k11": self.k11,
            "k11_": self.k11_,
            "k12": self.k12,
            "k12_": self.k12_,
            "k13": self.k13,
            "k13_": self.k13_,
            "k14": self.k14,
            "k14_": self.k14_,
            "k15": self.k15,
            "k15_": self.k15_,
            "K16": self.K16,
            "V16": self.V16,
            "k17": self.k17,
            "k17_": self.k17_,
            "k18": self.k18,
            "k18_": self.k18_,
            "k19": self.k19,
            "k19_": self.k19_,
            "k20": self.k20,
            "k20_": self.k20_,
            "k21": self.k21,
            "k21_": self.k21_,
            "k22": self.k22,
            "k22_": self.k22_,
            "k23": self.k23,
            "k23_": self.k23_,
            "k24": self.k24,
            "k24_": self.k24_,
            "k25": self.k25,
            "k25_": self.k25_,
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
        y0=[680, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 105, 0, 0, 85, 150, 34],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "kholodenko_demin_moehren_hoek_1999"
        self.curve_names = [
            "EGF",
            "R",
            "Ra",
            "R2",
            "RP",
            "R_PL",
            "R_PLP",
            "R_G",
            "R_G_S",
            "R_Sh",
            "R_ShP",
            "R_Sh_G",
            "R_Sh_G_S",
            "G_S",
            "ShP",
            "Sh_G",
            "Sh_G_S",
            "PLC_gamma",
            "PLC_gamma_P",
            "PLC_gamma_P_I",
            "Grb",
            "Shc",
            "SOS",
        ]
        self.state_names = ['EGF', 'R', 'Ra', 'R2', 'RP', 'R_PL', 'R_PLP', 'R_G', 'R_G_S', 'R_Sh', 'R_ShP', 'R_Sh_G', 'R_Sh_G_S', 'G_S', 'ShP', 'Sh_G', 'Sh_G_S', 'PLC_gamma', 'PLC_gamma_P', 'PLC_gamma_P_I', 'Grb', 'Shc', 'SOS']
        self.algebraic_names = ['v1', 'totEGFRphos', 'totPLCgammaphos', 'totGrb_EGFR', 'totGrb_Shc', 'totShcphos', 'totShc_EGFR', 'totSOS_EGFR', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v9', 'v8', 'v10', 'v25', 'v11', 'v12', 'v13', 'v14', 'v15', 'v16', 'v17', 'v18', 'v19', 'v20', 'v21', 'v22', 'v23', 'v24']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 50
        p = self.params

        # direct mapping
        c[0] = p.k1
        c[1] = p.k1_
        c[2] = p.k2
        c[3] = p.k2_
        c[4] = p.k3
        c[5] = p.k3_
        c[6] = p.K4
        c[7] = p.V4
        c[8] = p.k5
        c[9] = p.k5_
        c[10] = p.k6
        c[11] = p.k6_
        c[12] = p.k7
        c[13] = p.k7_
        c[14] = p.K8
        c[15] = p.V8
        c[16] = p.k9
        c[17] = p.k9_
        c[18] = p.k10
        c[19] = p.k10_
        c[20] = p.k11
        c[21] = p.k11_
        c[22] = p.k12
        c[23] = p.k12_
        c[24] = p.k13
        c[25] = p.k13_
        c[26] = p.k14
        c[27] = p.k14_
        c[28] = p.k15
        c[29] = p.k15_
        c[30] = p.K16
        c[31] = p.V16
        c[32] = p.k17
        c[33] = p.k17_
        c[34] = p.k18
        c[35] = p.k18_
        c[36] = p.k19
        c[37] = p.k19_
        c[38] = p.k20
        c[39] = p.k20_
        c[40] = p.k21
        c[41] = p.k21_
        c[42] = p.k22
        c[43] = p.k22_
        c[44] = p.k23
        c[45] = p.k23_
        c[46] = p.k24
        c[47] = p.k24_
        c[48] = p.k25
        c[49] = p.k25_

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
