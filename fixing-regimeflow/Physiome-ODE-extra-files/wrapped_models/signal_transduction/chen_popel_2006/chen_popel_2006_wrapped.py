# Size of variable arrays:
sizeAlgebraic = 2
sizeStates = 15
sizeConstants = 21
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (second)"
    legend_states[0] = "Arg in component Arg (micromolar)"
    legend_algebraic[0] = "S in component Arg (flux)"
    legend_states[1] = "Fe3 in component Fe3 (micromolar)"
    legend_states[2] = "Fe3_Arg in component Fe3_Arg (micromolar)"
    legend_states[3] = "Fe2_Arg in component Fe2_Arg (micromolar)"
    legend_states[4] = "Fe2 in component Fe2 (micromolar)"
    legend_constants[0] = "k1 in component model_constants (second_order_rate_constant)"
    legend_constants[1] = "k_1 in component model_constants (first_order_rate_constant)"
    legend_constants[2] = "k4 in component model_constants (second_order_rate_constant)"
    legend_constants[3] = "k_4 in component model_constants (first_order_rate_constant)"
    legend_states[5] = "Fe3_NO in component Fe3_NO (micromolar)"
    legend_states[6] = "Fe2_NO in component Fe2_NO (micromolar)"
    legend_constants[4] = "O2 in component model_constants (micromolar)"
    legend_states[7] = "Fe3_NOHA in component Fe3_NOHA (micromolar)"
    legend_states[8] = "NOHA in component NOHA (micromolar)"
    legend_constants[5] = "k2 in component model_constants (first_order_rate_constant)"
    legend_constants[6] = "k13 in component model_constants (second_order_rate_constant)"
    legend_constants[7] = "k14 in component model_constants (first_order_rate_constant)"
    legend_constants[8] = "k8 in component model_constants (first_order_rate_constant)"
    legend_constants[9] = "k_8 in component model_constants (second_order_rate_constant)"
    legend_constants[10] = "k3 in component model_constants (first_order_rate_constant)"
    legend_states[9] = "Fe2_NOHA in component Fe2_NOHA (micromolar)"
    legend_constants[11] = "k9 in component model_constants (first_order_rate_constant)"
    legend_constants[12] = "k_9 in component model_constants (second_order_rate_constant)"
    legend_states[10] = "Fe3_O2_Arg in component Fe3_O2_Arg (micromolar)"
    legend_constants[13] = "k5 in component model_constants (second_order_rate_constant)"
    legend_constants[14] = "k_5 in component model_constants (first_order_rate_constant)"
    legend_constants[15] = "k6 in component model_constants (first_order_rate_constant)"
    legend_constants[16] = "k7 in component model_constants (first_order_rate_constant)"
    legend_states[11] = "Fe3_O2_NOHA in component Fe3_O2_NOHA (micromolar)"
    legend_constants[17] = "k_10 in component model_constants (first_order_rate_constant)"
    legend_constants[18] = "k10 in component model_constants (second_order_rate_constant)"
    legend_constants[19] = "k11 in component model_constants (first_order_rate_constant)"
    legend_constants[20] = "k12 in component model_constants (first_order_rate_constant)"
    legend_states[12] = "NO in component NO (micromolar)"
    legend_algebraic[1] = "dNOdt in component NO (flux)"
    legend_states[13] = "citrulline in component citrulline (micromolar)"
    legend_states[14] = "NO3 in component NO3 (micromolar)"
    legend_rates[0] = "d/dt Arg in component Arg (micromolar)"
    legend_rates[1] = "d/dt Fe3 in component Fe3 (micromolar)"
    legend_rates[2] = "d/dt Fe3_Arg in component Fe3_Arg (micromolar)"
    legend_rates[4] = "d/dt Fe2 in component Fe2 (micromolar)"
    legend_rates[3] = "d/dt Fe2_Arg in component Fe2_Arg (micromolar)"
    legend_rates[10] = "d/dt Fe3_O2_Arg in component Fe3_O2_Arg (micromolar)"
    legend_rates[7] = "d/dt Fe3_NOHA in component Fe3_NOHA (micromolar)"
    legend_rates[9] = "d/dt Fe2_NOHA in component Fe2_NOHA (micromolar)"
    legend_rates[11] = "d/dt Fe3_O2_NOHA in component Fe3_O2_NOHA (micromolar)"
    legend_rates[5] = "d/dt Fe3_NO in component Fe3_NO (micromolar)"
    legend_rates[6] = "d/dt Fe2_NO in component Fe2_NO (micromolar)"
    legend_rates[12] = "d/dt NO in component NO (micromolar)"
    legend_rates[13] = "d/dt citrulline in component citrulline (micromolar)"
    legend_rates[14] = "d/dt NO3 in component NO3 (micromolar)"
    legend_rates[8] = "d/dt NOHA in component NOHA (micromolar)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 100.0
    states[1] = 0.045
    states[2] = 0.0
    states[3] = 0.0
    states[4] = 0.0
    constants[0] = 0.1
    constants[1] = 0.1
    constants[2] = 1.89
    constants[3] = 11.4
    states[5] = 0.0
    states[6] = 0.0
    constants[4] = 172.0
    states[7] = 0.0
    states[8] = 0.0
    constants[5] = 0.91
    constants[6] = 0.033
    constants[7] = 53.9
    constants[8] = 0.1
    constants[9] = 0.1
    constants[10] = 0.91
    states[9] = 0.0
    constants[11] = 11.4
    constants[12] = 1.89
    states[10] = 0.0
    constants[13] = 2.58
    constants[14] = 98.0
    constants[15] = 12.6
    constants[16] = 0.91
    states[11] = 0.0
    constants[17] = 89.9
    constants[18] = 3.33
    constants[19] = 29.4
    constants[20] = 0.91
    states[12] = 0.0
    states[13] = 0.0
    states[14] = 0.0
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[1] = (constants[1]*states[2]+constants[7]*states[5]+constants[6]*states[6]*constants[4]+constants[8]*states[7])-(constants[0]*states[0]*states[1]+constants[5]*states[1]+constants[9]*states[8]*states[1])
    rates[2] = constants[0]*states[1]*states[0]-(constants[1]*states[2]+constants[10]*states[2])
    rates[4] = (constants[5]*states[1]+constants[3]*states[3]+constants[11]*states[9])-(constants[2]*states[4]*states[0]+constants[12]*states[4]*states[8])
    rates[3] = (constants[10]*states[2]+constants[14]*states[10]+constants[2]*states[4]*states[0])-(constants[13]*states[3]*constants[4]+constants[3]*states[3])
    rates[10] = constants[13]*states[3]*constants[4]-(constants[15]*states[10]+constants[14]*states[10])
    rates[7] = (constants[15]*states[10]+constants[9]*states[1]*states[8])-(constants[16]*states[7]+constants[8]*states[7])
    rates[9] = (constants[16]*states[7]+constants[17]*states[11]+constants[12]*states[4]*states[8])-(constants[11]*states[9]+constants[18]*states[9]*constants[4])
    rates[11] = constants[18]*states[9]*constants[4]-(constants[19]*states[11]+constants[17]*states[11])
    rates[5] = constants[19]*states[11]-(constants[7]*states[5]+constants[20]*states[5])
    rates[6] = constants[20]*states[5]-constants[6]*states[6]*constants[4]
    rates[12] = constants[7]*states[5]
    rates[13] = constants[19]*states[11]
    rates[14] = constants[6]*states[6]*constants[4]
    rates[8] = (constants[8]*states[7]+constants[11]*states[9])-(constants[9]*states[1]*states[8]+constants[12]*states[4]*states[8])
    algebraic[0] = (constants[0]*states[0]*states[1]+constants[2]*states[0]*states[4])-(constants[1]*states[2]+constants[3]*states[3])
    rates[0] = (constants[1]*states[2]+constants[3]*states[3]+algebraic[0])-(constants[0]*states[0]*states[1]+constants[2]*states[0]*states[4])
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = (constants[0]*states[0]*states[1]+constants[2]*states[0]*states[4])-(constants[1]*states[2]+constants[3]*states[3])
    algebraic[1] = constants[7]*states[5]
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
        self.k1 = 0.1
        self.k_1 = 0.1
        self.k4 = 1.89
        self.k_4 = 11.4
        self.O2 = 172.0
        self.k2 = 0.91
        self.k13 = 0.033
        self.k14 = 53.9
        self.k8 = 0.1
        self.k_8 = 0.1
        self.k3 = 0.91
        self.k9 = 11.4
        self.k_9 = 1.89
        self.k5 = 2.58
        self.k_5 = 98.0
        self.k6 = 12.6
        self.k7 = 0.91
        self.k_10 = 89.9
        self.k10 = 3.33
        self.k11 = 29.4
        self.k12 = 0.91

    def to_dict(self):
        return {
            "k1": self.k1,
            "k_1": self.k_1,
            "k4": self.k4,
            "k_4": self.k_4,
            "O2": self.O2,
            "k2": self.k2,
            "k13": self.k13,
            "k14": self.k14,
            "k8": self.k8,
            "k_8": self.k_8,
            "k3": self.k3,
            "k9": self.k9,
            "k_9": self.k_9,
            "k5": self.k5,
            "k_5": self.k_5,
            "k6": self.k6,
            "k7": self.k7,
            "k_10": self.k_10,
            "k10": self.k10,
            "k11": self.k11,
            "k12": self.k12,
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
        y0=[100.0, 0.045, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "chen_popel_2006"
        self.curve_names = [
            "Arg",
            "Fe3",
            "Fe3_Arg",
            "Fe2_Arg",
            "Fe2",
            "Fe3_NO",
            "Fe2_NO",
            "Fe3_NOHA",
            "NOHA",
            "Fe2_NOHA",
            "Fe3_O2_Arg",
            "Fe3_O2_NOHA",
            "NO",
            "citrulline",
            "NO3",
        ]
        self.state_names = ['Arg', 'Fe3', 'Fe3_Arg', 'Fe2_Arg', 'Fe2', 'Fe3_NO', 'Fe2_NO', 'Fe3_NOHA', 'NOHA', 'Fe2_NOHA', 'Fe3_O2_Arg', 'Fe3_O2_NOHA', 'NO', 'citrulline', 'NO3']
        self.algebraic_names = ['S', 'dNOdt']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 21
        p = self.params

        # direct mapping
        c[0] = p.k1
        c[1] = p.k_1
        c[2] = p.k4
        c[3] = p.k_4
        c[4] = p.O2
        c[5] = p.k2
        c[6] = p.k13
        c[7] = p.k14
        c[8] = p.k8
        c[9] = p.k_8
        c[10] = p.k3
        c[11] = p.k9
        c[12] = p.k_9
        c[13] = p.k5
        c[14] = p.k_5
        c[15] = p.k6
        c[16] = p.k7
        c[17] = p.k_10
        c[18] = p.k10
        c[19] = p.k11
        c[20] = p.k12

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
