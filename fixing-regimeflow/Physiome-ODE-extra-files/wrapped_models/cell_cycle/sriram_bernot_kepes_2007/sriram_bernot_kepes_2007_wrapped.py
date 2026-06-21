# Size of variable arrays:
sizeAlgebraic = 0
sizeStates = 6
sizeConstants = 25
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (minute)"
    legend_constants[0] = "j_1 in component parameters (flux)"
    legend_constants[1] = "j_2 in component parameters (flux)"
    legend_constants[2] = "j_3 in component parameters (flux)"
    legend_constants[3] = "v_d1 in component parameters (flux)"
    legend_constants[4] = "v_d2 in component parameters (flux)"
    legend_constants[5] = "v_d3 in component parameters (flux)"
    legend_constants[6] = "k_d1 in component parameters (first_order_rate_constant)"
    legend_constants[7] = "k_d2 in component parameters (first_order_rate_constant)"
    legend_constants[8] = "k_d3 in component parameters (first_order_rate_constant)"
    legend_constants[9] = "k_c1 in component parameters (first_order_rate_constant)"
    legend_constants[10] = "k_c2 in component parameters (first_order_rate_constant)"
    legend_constants[11] = "k_c3 in component parameters (first_order_rate_constant)"
    legend_constants[12] = "k_m1 in component parameters (nanomolar)"
    legend_constants[13] = "k_m2 in component parameters (nanomolar)"
    legend_constants[14] = "k_m3 in component parameters (nanomolar)"
    legend_constants[15] = "v_12 in component parameters (flux)"
    legend_constants[16] = "v_11 in component parameters (flux)"
    legend_constants[17] = "v_10 in component parameters (flux)"
    legend_constants[18] = "k_120 in component parameters (nanomolar)"
    legend_constants[19] = "k_110 in component parameters (nanomolar)"
    legend_constants[20] = "k_100 in component parameters (nanomolar)"
    legend_constants[21] = "k_d4 in component parameters (first_order_rate_constant)"
    legend_constants[22] = "k_d5 in component parameters (first_order_rate_constant)"
    legend_constants[23] = "k_d6 in component parameters (first_order_rate_constant)"
    legend_constants[24] = "n in component parameters (dimensionless)"
    legend_states[0] = "C_1 in component C_1 (nanomolar)"
    legend_states[1] = "C_2 in component C_2 (nanomolar)"
    legend_states[2] = "T_1 in component T_1 (nanomolar)"
    legend_states[3] = "C_3 in component C_3 (nanomolar)"
    legend_states[4] = "T_2 in component T_2 (nanomolar)"
    legend_states[5] = "T_3 in component T_3 (nanomolar)"
    legend_rates[0] = "d/dt C_1 in component C_1 (nanomolar)"
    legend_rates[1] = "d/dt C_2 in component C_2 (nanomolar)"
    legend_rates[3] = "d/dt C_3 in component C_3 (nanomolar)"
    legend_rates[2] = "d/dt T_1 in component T_1 (nanomolar)"
    legend_rates[4] = "d/dt T_2 in component T_2 (nanomolar)"
    legend_rates[5] = "d/dt T_3 in component T_3 (nanomolar)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    constants[0] = 0.9
    constants[1] = 0.5
    constants[2] = 0.6
    constants[3] = 6
    constants[4] = 1.052
    constants[5] = 3
    constants[6] = 0.8
    constants[7] = 0.9
    constants[8] = 0.8
    constants[9] = 0.2
    constants[10] = 0.22
    constants[11] = 0.6
    constants[12] = 5
    constants[13] = 5
    constants[14] = 5
    constants[15] = 15
    constants[16] = 15
    constants[17] = 15
    constants[18] = 10
    constants[19] = 10
    constants[20] = 10
    constants[21] = 0.16
    constants[22] = 0.16
    constants[23] = 0.16
    constants[24] = 2
    states[0] = 0
    states[1] = 0
    states[2] = 6
    states[3] = 0
    states[4] = 5
    states[5] = 1
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[0] = (constants[15]*(power(states[2], constants[24])))/(power(constants[18], constants[24])+power(states[2], constants[24])+power(states[1], constants[24]))-constants[21]*states[0]
    rates[1] = (constants[16]*(power(states[4], constants[24])))/(power(constants[19], constants[24])+power(states[4], constants[24])+power(states[3], constants[24]))-constants[22]*states[1]
    rates[3] = (constants[17]*(power(states[5], constants[24])))/(power(constants[20], constants[24])+power(states[5], constants[24])+power(states[0], constants[24]))-constants[23]*states[3]
    rates[2] = (constants[0]+(constants[3]*(power(states[5], constants[24])))/(power(constants[12], constants[24])+power(states[5], constants[24]))+constants[9]*states[0])-constants[6]*states[2]
    rates[4] = (constants[1]+(constants[4]*(power(states[2], constants[24])))/(power(constants[13], constants[24])+power(states[2], constants[24]))+constants[10]*states[1])-constants[7]*states[4]
    rates[5] = (constants[2]+(constants[5]*(power(states[4], constants[24])))/(power(constants[14], constants[24])+power(states[4], constants[24]))+constants[11]*states[3])-constants[8]*states[5]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
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
        self.j_1 = 0.9
        self.j_2 = 0.5
        self.j_3 = 0.6
        self.v_d1 = 6
        self.v_d2 = 1.052
        self.v_d3 = 3
        self.k_d1 = 0.8
        self.k_d2 = 0.9
        self.k_d3 = 0.8
        self.k_c1 = 0.2
        self.k_c2 = 0.22
        self.k_c3 = 0.6
        self.k_m1 = 5
        self.k_m2 = 5
        self.k_m3 = 5
        self.v_12 = 15
        self.v_11 = 15
        self.v_10 = 15
        self.k_120 = 10
        self.k_110 = 10
        self.k_100 = 10
        self.k_d4 = 0.16
        self.k_d5 = 0.16
        self.k_d6 = 0.16
        self.n = 2

    def to_dict(self):
        return {
            "j_1": self.j_1,
            "j_2": self.j_2,
            "j_3": self.j_3,
            "v_d1": self.v_d1,
            "v_d2": self.v_d2,
            "v_d3": self.v_d3,
            "k_d1": self.k_d1,
            "k_d2": self.k_d2,
            "k_d3": self.k_d3,
            "k_c1": self.k_c1,
            "k_c2": self.k_c2,
            "k_c3": self.k_c3,
            "k_m1": self.k_m1,
            "k_m2": self.k_m2,
            "k_m3": self.k_m3,
            "v_12": self.v_12,
            "v_11": self.v_11,
            "v_10": self.v_10,
            "k_120": self.k_120,
            "k_110": self.k_110,
            "k_100": self.k_100,
            "k_d4": self.k_d4,
            "k_d5": self.k_d5,
            "k_d6": self.k_d6,
            "n": self.n,
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
        y0=[0, 0, 6, 0, 5, 1],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "sriram_bernot_kepes_2007"
        self.curve_names = [
            "C_1",
            "C_2",
            "T_1",
            "C_3",
            "T_2",
            "T_3",
        ]
        self.state_names = ['C_1', 'C_2', 'T_1', 'C_3', 'T_2', 'T_3']
        self.algebraic_names = []
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 25
        p = self.params

        # direct mapping
        c[0] = p.j_1
        c[1] = p.j_2
        c[2] = p.j_3
        c[3] = p.v_d1
        c[4] = p.v_d2
        c[5] = p.v_d3
        c[6] = p.k_d1
        c[7] = p.k_d2
        c[8] = p.k_d3
        c[9] = p.k_c1
        c[10] = p.k_c2
        c[11] = p.k_c3
        c[12] = p.k_m1
        c[13] = p.k_m2
        c[14] = p.k_m3
        c[15] = p.v_12
        c[16] = p.v_11
        c[17] = p.v_10
        c[18] = p.k_120
        c[19] = p.k_110
        c[20] = p.k_100
        c[21] = p.k_d4
        c[22] = p.k_d5
        c[23] = p.k_d6
        c[24] = p.n

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
