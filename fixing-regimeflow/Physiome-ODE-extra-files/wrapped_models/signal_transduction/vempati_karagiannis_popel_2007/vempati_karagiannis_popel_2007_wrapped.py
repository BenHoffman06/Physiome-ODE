# Size of variable arrays:
sizeAlgebraic = 20
sizeStates = 17
sizeConstants = 33
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (second)"
    legend_algebraic[0] = "v1 in component v1 (flux)"
    legend_states[0] = "pM9 in component pM9 (molar)"
    legend_states[1] = "M3 in component M3 (molar)"
    legend_states[2] = "M3_pM9 in component M3_pM9 (molar)"
    legend_constants[0] = "kon_M3pM9 in component kinetic_parameters (second_order_rate_constant)"
    legend_constants[1] = "koff_M3pM9 in component kinetic_parameters (first_order_rate_constant)"
    legend_algebraic[1] = "v2 in component v2 (flux)"
    legend_constants[2] = "kact_M3pM9 in component kinetic_parameters (first_order_rate_constant)"
    legend_algebraic[2] = "v3 in component v3 (flux)"
    legend_states[3] = "M3_T1 in component M3_T1 (molar)"
    legend_states[4] = "T1 in component T1 (molar)"
    legend_constants[3] = "kon_M3T1 in component kinetic_parameters (second_order_rate_constant)"
    legend_constants[4] = "koff_M3T1 in component kinetic_parameters (first_order_rate_constant)"
    legend_algebraic[3] = "v4 in component v4 (flux)"
    legend_states[5] = "pM9_T1 in component pM9_T1 (molar)"
    legend_constants[5] = "kon_pM9T1 in component kinetic_parameters (second_order_rate_constant)"
    legend_constants[6] = "koff_pM9T1 in component kinetic_parameters (first_order_rate_constant)"
    legend_algebraic[4] = "v5 in component v5 (flux)"
    legend_states[6] = "M3_pM9_T1 in component M3_pM9_T1 (molar)"
    legend_constants[7] = "kon_M3pM9T1 in component kinetic_parameters (second_order_rate_constant)"
    legend_constants[8] = "koff_M3pM9T1 in component kinetic_parameters (first_order_rate_constant)"
    legend_algebraic[5] = "v6 in component v6 (flux)"
    legend_constants[9] = "kact_M3pM9T1 in component kinetic_parameters (first_order_rate_constant)"
    legend_algebraic[6] = "v7 in component v7 (flux)"
    legend_states[7] = "M9_T1_star in component M9_T1_star (molar)"
    legend_states[8] = "M9 in component M9 (molar)"
    legend_constants[10] = "kon_M9T1_star in component kinetic_parameters (second_order_rate_constant)"
    legend_constants[11] = "koff_M9T1_star in component kinetic_parameters (first_order_rate_constant)"
    legend_algebraic[7] = "v8 in component v8 (flux)"
    legend_states[9] = "M9_T1 in component M9_T1 (molar)"
    legend_constants[12] = "kon_M9T1 in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[13] = "koff_M9T1 in component kinetic_parameters (first_order_rate_constant)"
    legend_algebraic[8] = "v9 in component v9 (flux)"
    legend_states[10] = "M9_T1_M3 in component M9_T1_M3 (molar)"
    legend_constants[14] = "kon_M9_M3T1 in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[15] = "koff_M9_M3T1 in component kinetic_parameters (second_order_rate_constant)"
    legend_algebraic[9] = "v10 in component v10 (flux)"
    legend_states[11] = "pM9_T1_M3 in component pM9_T1_M3 (molar)"
    legend_constants[16] = "kon_M3_pM9T1 in component kinetic_parameters (second_order_rate_constant)"
    legend_constants[17] = "koff_M3_pM9T1 in component kinetic_parameters (first_order_rate_constant)"
    legend_algebraic[10] = "v11 in component v11 (flux)"
    legend_constants[18] = "kon_pM9T1M3 in component kinetic_parameters (second_order_rate_constant)"
    legend_constants[19] = "koff_pM9T1M3 in component kinetic_parameters (first_order_rate_constant)"
    legend_algebraic[11] = "v12 in component v12 (flux)"
    legend_states[12] = "M3_pM9_T1_M3 in component M3_pM9_T1_M3 (molar)"
    legend_constants[20] = "kon_M3pM9T1M3 in component kinetic_parameters (second_order_rate_constant)"
    legend_constants[21] = "koff_M3pM9T1M3 in component kinetic_parameters (first_order_rate_constant)"
    legend_algebraic[12] = "v13 in component v13 (flux)"
    legend_constants[22] = "kact_M3pM9T1M3 in component kinetic_parameters (first_order_rate_constant)"
    legend_algebraic[13] = "v14 in component v14 (flux)"
    legend_constants[23] = "kact_M9T1M3 in component kinetic_parameters (first_order_rate_constant)"
    legend_algebraic[14] = "v15 in component v15 (flux)"
    legend_states[13] = "Tr in component Tr (molar)"
    legend_states[14] = "Tr_pM9 in component Tr_pM9 (molar)"
    legend_constants[24] = "kon_TrpM9 in component kinetic_parameters (second_order_rate_constant)"
    legend_constants[25] = "koff_TrpM9 in component kinetic_parameters (first_order_rate_constant)"
    legend_algebraic[15] = "v16 in component v16 (flux)"
    legend_constants[26] = "kact_TrpM9 in component kinetic_parameters (first_order_rate_constant)"
    legend_algebraic[16] = "v17 in component v17 (flux)"
    legend_states[15] = "Tr_pM9_T1 in component Tr_pM9_T1 (molar)"
    legend_constants[27] = "kon_TrpM9T1 in component kinetic_parameters (second_order_rate_constant)"
    legend_constants[28] = "koff_TrpM9T1 in component kinetic_parameters (first_order_rate_constant)"
    legend_algebraic[17] = "v18 in component v18 (flux)"
    legend_constants[29] = "kact_TrpM9T1 in component kinetic_parameters (first_order_rate_constant)"
    legend_algebraic[18] = "v19 in component v19 (flux)"
    legend_states[16] = "Tr_pM9_T1_M3 in component Tr_pM9_T1_M3 (molar)"
    legend_constants[30] = "kon_TrpM9T1M3 in component kinetic_parameters (second_order_rate_constant)"
    legend_constants[31] = "koff_TrpM9T1M3 in component kinetic_parameters (first_order_rate_constant)"
    legend_algebraic[19] = "v20 in component v20 (flux)"
    legend_constants[32] = "kact_TrpM9T1M3 in component kinetic_parameters (first_order_rate_constant)"
    legend_rates[0] = "d/dt pM9 in component pM9 (molar)"
    legend_rates[1] = "d/dt M3 in component M3 (molar)"
    legend_rates[2] = "d/dt M3_pM9 in component M3_pM9 (molar)"
    legend_rates[4] = "d/dt T1 in component T1 (molar)"
    legend_rates[3] = "d/dt M3_T1 in component M3_T1 (molar)"
    legend_rates[5] = "d/dt pM9_T1 in component pM9_T1 (molar)"
    legend_rates[6] = "d/dt M3_pM9_T1 in component M3_pM9_T1 (molar)"
    legend_rates[7] = "d/dt M9_T1_star in component M9_T1_star (molar)"
    legend_rates[8] = "d/dt M9 in component M9 (molar)"
    legend_rates[9] = "d/dt M9_T1 in component M9_T1 (molar)"
    legend_rates[11] = "d/dt pM9_T1_M3 in component pM9_T1_M3 (molar)"
    legend_rates[12] = "d/dt M3_pM9_T1_M3 in component M3_pM9_T1_M3 (molar)"
    legend_rates[10] = "d/dt M9_T1_M3 in component M9_T1_M3 (molar)"
    legend_rates[13] = "d/dt Tr in component Tr (molar)"
    legend_rates[14] = "d/dt Tr_pM9 in component Tr_pM9 (molar)"
    legend_rates[15] = "d/dt Tr_pM9_T1 in component Tr_pM9_T1 (molar)"
    legend_rates[16] = "d/dt Tr_pM9_T1_M3 in component Tr_pM9_T1_M3 (molar)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 3e-7
    states[1] = 5e-8
    states[2] = 0
    constants[0] = 1e4
    constants[1] = 0.001
    constants[2] = 0.0019
    states[3] = 0
    states[4] = 3e-7
    constants[3] = 1.9e6
    constants[4] = 1.26e-4
    states[5] = 0
    constants[5] = 3.4e4
    constants[6] = 7.48e-5
    states[6] = 0
    constants[7] = 1e4
    constants[8] = 0.001
    constants[9] = 0.00057
    states[7] = 0
    states[8] = 0
    constants[10] = 5.6e6
    constants[11] = 1.6e-5
    states[9] = 0
    constants[12] = 6.3e-4
    constants[13] = 2.5e-4
    states[10] = 0
    constants[14] = 7.48e-5
    constants[15] = 3.4e4
    states[11] = 0
    constants[16] = 1.9e6
    constants[17] = 1.26e-4
    constants[18] = 3.4e4
    constants[19] = 7.48e-5
    states[12] = 0
    constants[20] = 1e4
    constants[21] = 0.001
    constants[22] = 0.00057
    constants[23] = 1.26e-4
    states[13] = 1e-7
    states[14] = 0
    constants[24] = 1e4
    constants[25] = 0.007
    constants[26] = 0.002
    states[15] = 0
    constants[27] = 1e4
    constants[28] = 0.007
    constants[29] = 0.0006
    states[16] = 0
    constants[30] = 1e4
    constants[31] = 0.007
    constants[32] = 0.0006
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[0] = constants[0]*states[1]*states[0]-constants[1]*states[2]
    algebraic[1] = constants[2]*states[2]
    rates[2] = algebraic[0]-algebraic[1]
    algebraic[4] = constants[7]*states[5]*states[1]-constants[8]*states[6]
    algebraic[5] = constants[9]*states[6]
    rates[6] = algebraic[4]-algebraic[5]
    algebraic[2] = constants[3]*states[1]*states[4]-constants[4]*states[3]
    algebraic[3] = constants[5]*states[0]*states[4]-constants[6]*states[5]
    algebraic[6] = constants[10]*states[4]*states[8]-constants[11]*states[7]
    rates[4] = -(algebraic[2]+algebraic[3]+algebraic[6])
    algebraic[8] = constants[14]*states[10]-constants[15]*states[8]*states[3]
    algebraic[10] = constants[18]*states[0]*states[3]-constants[19]*states[11]
    rates[3] = (algebraic[2]+algebraic[8])-algebraic[10]
    algebraic[11] = constants[20]*states[1]*states[11]-constants[21]*states[12]
    algebraic[12] = constants[22]*states[12]
    rates[12] = algebraic[11]-algebraic[12]
    algebraic[9] = constants[16]*states[5]*states[1]-constants[17]*states[11]
    algebraic[13] = constants[23]*states[10]
    rates[1] = (algebraic[1]+algebraic[5]+algebraic[12]+algebraic[13])-(algebraic[0]+algebraic[2]+algebraic[4]+algebraic[9]+algebraic[11])
    algebraic[7] = constants[12]*states[7]-constants[13]*states[9]
    rates[7] = (algebraic[6]+algebraic[13])-algebraic[7]
    algebraic[14] = constants[24]*states[13]*states[0]-constants[25]*states[14]
    rates[0] = -(algebraic[0]+algebraic[3]+algebraic[14]+algebraic[10])
    algebraic[15] = constants[26]*states[14]
    rates[8] = (algebraic[1]+algebraic[8]+algebraic[15])-algebraic[6]
    rates[14] = algebraic[14]-algebraic[15]
    algebraic[16] = constants[27]*states[5]*states[13]-constants[28]*states[15]
    rates[5] = algebraic[3]-(algebraic[4]+algebraic[9]+algebraic[16])
    algebraic[17] = constants[29]*states[15]
    rates[9] = algebraic[7]+algebraic[17]
    rates[15] = algebraic[16]-algebraic[17]
    algebraic[18] = constants[30]*states[13]*states[11]-constants[31]*states[16]
    rates[11] = (algebraic[9]+algebraic[10])-(algebraic[11]+algebraic[18])
    algebraic[19] = constants[32]*states[16]
    rates[10] = (algebraic[12]+algebraic[19])-(algebraic[13]+algebraic[8])
    rates[13] = (algebraic[15]+algebraic[17]+algebraic[19])-(algebraic[14]+algebraic[16]+algebraic[18])
    rates[16] = algebraic[18]-algebraic[19]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = constants[0]*states[1]*states[0]-constants[1]*states[2]
    algebraic[1] = constants[2]*states[2]
    algebraic[4] = constants[7]*states[5]*states[1]-constants[8]*states[6]
    algebraic[5] = constants[9]*states[6]
    algebraic[2] = constants[3]*states[1]*states[4]-constants[4]*states[3]
    algebraic[3] = constants[5]*states[0]*states[4]-constants[6]*states[5]
    algebraic[6] = constants[10]*states[4]*states[8]-constants[11]*states[7]
    algebraic[8] = constants[14]*states[10]-constants[15]*states[8]*states[3]
    algebraic[10] = constants[18]*states[0]*states[3]-constants[19]*states[11]
    algebraic[11] = constants[20]*states[1]*states[11]-constants[21]*states[12]
    algebraic[12] = constants[22]*states[12]
    algebraic[9] = constants[16]*states[5]*states[1]-constants[17]*states[11]
    algebraic[13] = constants[23]*states[10]
    algebraic[7] = constants[12]*states[7]-constants[13]*states[9]
    algebraic[14] = constants[24]*states[13]*states[0]-constants[25]*states[14]
    algebraic[15] = constants[26]*states[14]
    algebraic[16] = constants[27]*states[5]*states[13]-constants[28]*states[15]
    algebraic[17] = constants[29]*states[15]
    algebraic[18] = constants[30]*states[13]*states[11]-constants[31]*states[16]
    algebraic[19] = constants[32]*states[16]
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
        self.kon_M3pM9 = 1e4
        self.koff_M3pM9 = 0.001
        self.kact_M3pM9 = 0.0019
        self.kon_M3T1 = 1.9e6
        self.koff_M3T1 = 1.26e-4
        self.kon_pM9T1 = 3.4e4
        self.koff_pM9T1 = 7.48e-5
        self.kon_M3pM9T1 = 1e4
        self.koff_M3pM9T1 = 0.001
        self.kact_M3pM9T1 = 0.00057
        self.kon_M9T1_star = 5.6e6
        self.koff_M9T1_star = 1.6e-5
        self.kon_M9T1 = 6.3e-4
        self.koff_M9T1 = 2.5e-4
        self.kon_M9_M3T1 = 7.48e-5
        self.koff_M9_M3T1 = 3.4e4
        self.kon_M3_pM9T1 = 1.9e6
        self.koff_M3_pM9T1 = 1.26e-4
        self.kon_pM9T1M3 = 3.4e4
        self.koff_pM9T1M3 = 7.48e-5
        self.kon_M3pM9T1M3 = 1e4
        self.koff_M3pM9T1M3 = 0.001
        self.kact_M3pM9T1M3 = 0.00057
        self.kact_M9T1M3 = 1.26e-4
        self.kon_TrpM9 = 1e4
        self.koff_TrpM9 = 0.007
        self.kact_TrpM9 = 0.002
        self.kon_TrpM9T1 = 1e4
        self.koff_TrpM9T1 = 0.007
        self.kact_TrpM9T1 = 0.0006
        self.kon_TrpM9T1M3 = 1e4
        self.koff_TrpM9T1M3 = 0.007
        self.kact_TrpM9T1M3 = 0.0006

    def to_dict(self):
        return {
            "kon_M3pM9": self.kon_M3pM9,
            "koff_M3pM9": self.koff_M3pM9,
            "kact_M3pM9": self.kact_M3pM9,
            "kon_M3T1": self.kon_M3T1,
            "koff_M3T1": self.koff_M3T1,
            "kon_pM9T1": self.kon_pM9T1,
            "koff_pM9T1": self.koff_pM9T1,
            "kon_M3pM9T1": self.kon_M3pM9T1,
            "koff_M3pM9T1": self.koff_M3pM9T1,
            "kact_M3pM9T1": self.kact_M3pM9T1,
            "kon_M9T1_star": self.kon_M9T1_star,
            "koff_M9T1_star": self.koff_M9T1_star,
            "kon_M9T1": self.kon_M9T1,
            "koff_M9T1": self.koff_M9T1,
            "kon_M9_M3T1": self.kon_M9_M3T1,
            "koff_M9_M3T1": self.koff_M9_M3T1,
            "kon_M3_pM9T1": self.kon_M3_pM9T1,
            "koff_M3_pM9T1": self.koff_M3_pM9T1,
            "kon_pM9T1M3": self.kon_pM9T1M3,
            "koff_pM9T1M3": self.koff_pM9T1M3,
            "kon_M3pM9T1M3": self.kon_M3pM9T1M3,
            "koff_M3pM9T1M3": self.koff_M3pM9T1M3,
            "kact_M3pM9T1M3": self.kact_M3pM9T1M3,
            "kact_M9T1M3": self.kact_M9T1M3,
            "kon_TrpM9": self.kon_TrpM9,
            "koff_TrpM9": self.koff_TrpM9,
            "kact_TrpM9": self.kact_TrpM9,
            "kon_TrpM9T1": self.kon_TrpM9T1,
            "koff_TrpM9T1": self.koff_TrpM9T1,
            "kact_TrpM9T1": self.kact_TrpM9T1,
            "kon_TrpM9T1M3": self.kon_TrpM9T1M3,
            "koff_TrpM9T1M3": self.koff_TrpM9T1M3,
            "kact_TrpM9T1M3": self.kact_TrpM9T1M3,
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
        y0=[3e-7, 5e-8, 0, 0, 3e-7, 0, 0, 0, 0, 0, 0, 0, 0, 1e-7, 0, 0, 0],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "vempati_karagiannis_popel_2007"
        self.curve_names = [
            "pM9",
            "M3",
            "M3_pM9",
            "M3_T1",
            "T1",
            "pM9_T1",
            "M3_pM9_T1",
            "M9_T1_star",
            "M9",
            "M9_T1",
            "M9_T1_M3",
            "pM9_T1_M3",
            "M3_pM9_T1_M3",
            "Tr",
            "Tr_pM9",
            "Tr_pM9_T1",
            "Tr_pM9_T1_M3",
        ]
        self.state_names = ['pM9', 'M3', 'M3_pM9', 'M3_T1', 'T1', 'pM9_T1', 'M3_pM9_T1', 'M9_T1_star', 'M9', 'M9_T1', 'M9_T1_M3', 'pM9_T1_M3', 'M3_pM9_T1_M3', 'Tr', 'Tr_pM9', 'Tr_pM9_T1', 'Tr_pM9_T1_M3']
        self.algebraic_names = ['v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8', 'v9', 'v10', 'v11', 'v12', 'v13', 'v14', 'v15', 'v16', 'v17', 'v18', 'v19', 'v20']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 33
        p = self.params

        # direct mapping
        c[0] = p.kon_M3pM9
        c[1] = p.koff_M3pM9
        c[2] = p.kact_M3pM9
        c[3] = p.kon_M3T1
        c[4] = p.koff_M3T1
        c[5] = p.kon_pM9T1
        c[6] = p.koff_pM9T1
        c[7] = p.kon_M3pM9T1
        c[8] = p.koff_M3pM9T1
        c[9] = p.kact_M3pM9T1
        c[10] = p.kon_M9T1_star
        c[11] = p.koff_M9T1_star
        c[12] = p.kon_M9T1
        c[13] = p.koff_M9T1
        c[14] = p.kon_M9_M3T1
        c[15] = p.koff_M9_M3T1
        c[16] = p.kon_M3_pM9T1
        c[17] = p.koff_M3_pM9T1
        c[18] = p.kon_pM9T1M3
        c[19] = p.koff_pM9T1M3
        c[20] = p.kon_M3pM9T1M3
        c[21] = p.koff_M3pM9T1M3
        c[22] = p.kact_M3pM9T1M3
        c[23] = p.kact_M9T1M3
        c[24] = p.kon_TrpM9
        c[25] = p.koff_TrpM9
        c[26] = p.kact_TrpM9
        c[27] = p.kon_TrpM9T1
        c[28] = p.koff_TrpM9T1
        c[29] = p.kact_TrpM9T1
        c[30] = p.kon_TrpM9T1M3
        c[31] = p.koff_TrpM9T1M3
        c[32] = p.kact_TrpM9T1M3

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
