# Size of variable arrays:
sizeAlgebraic = 2
sizeStates = 7
sizeConstants = 13
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (day)"
    legend_constants[9] = "T in component T (per_ml)"
    legend_constants[0] = "k in component kinetic_parameters (ml_per_day)"
    legend_constants[1] = "p in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[2] = "c in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[3] = "delta in component kinetic_parameters (first_order_rate_constant)"
    legend_states[0] = "I in component I (per_ml)"
    legend_constants[10] = "I_0 in component I (per_ml)"
    legend_constants[11] = "k_ in component kinetic_parameters (ml_per_day)"
    legend_states[1] = "E4 in component E4 (per_ml)"
    legend_constants[4] = "VI_0 in component VI (per_ml)"
    legend_states[2] = "VI in component VI (per_ml)"
    legend_algebraic[0] = "h in component Heavyside_function (dimensionless)"
    legend_states[3] = "VNI in component VNI (per_ml)"
    legend_algebraic[1] = "V in component virus_total (per_ml)"
    legend_states[4] = "E1 in component E1 (per_ml)"
    legend_constants[12] = "b_ in component kinetic_parameters (day)"
    legend_states[5] = "E2 in component E2 (per_ml)"
    legend_states[6] = "E3 in component E3 (per_ml)"
    legend_constants[5] = "tau_p in component Heavyside_function (day)"
    legend_constants[6] = "b in component kinetic_parameters (day)"
    legend_constants[7] = "m in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[8] = "n in component kinetic_parameters (dimensionless)"
    legend_rates[0] = "d/dt I in component I (per_ml)"
    legend_rates[2] = "d/dt VI in component VI (per_ml)"
    legend_rates[3] = "d/dt VNI in component VNI (per_ml)"
    legend_rates[4] = "d/dt E1 in component E1 (per_ml)"
    legend_rates[5] = "d/dt E2 in component E2 (per_ml)"
    legend_rates[6] = "d/dt E3 in component E3 (per_ml)"
    legend_rates[1] = "d/dt E4 in component E4 (per_ml)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    constants[0] = 2.4e-5
    constants[1] = 774
    constants[2] = 3
    constants[3] = 0.5
    states[0] = 0.1
    states[1] = 0
    constants[4] = 200000
    states[2] = 200000
    states[3] = 0
    states[4] = 0
    states[5] = 0
    states[6] = 0
    constants[5] = 0
    constants[6] = 0.25
    constants[7] = 0.01
    constants[8] = 4
    constants[9] = (constants[2]*constants[3])/(constants[0]*constants[1])
    constants[10] = (constants[2]/constants[1])*constants[4]
    constants[11] = constants[0]/(power(1.00000+constants[7]*constants[6], constants[8]))
    constants[12] = constants[6]/(1.00000+constants[7]*constants[6])
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[0] = constants[11]*constants[9]*states[1]-constants[3]*states[0]
    rates[4] = (states[2]-states[4])/constants[12]
    rates[5] = (states[4]-states[5])/constants[12]
    rates[6] = (states[5]-states[6])/constants[12]
    rates[1] = (states[6]-states[1])/constants[12]
    algebraic[0] = custom_piecewise([less(voi , constants[5]), 0.00000 , True, 1.00000])
    rates[2] = (1.00000-algebraic[0])*constants[1]*states[0]-constants[2]*states[2]
    rates[3] = algebraic[0]*constants[1]*states[0]-constants[2]*states[3]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = custom_piecewise([less(voi , constants[5]), 0.00000 , True, 1.00000])
    algebraic[1] = states[2]+states[3]
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
        self.k = 2.4e-5
        self.p = 774
        self.c = 3
        self.delta = 0.5
        self.VI_0 = 200000
        self.tau_p = 0
        self.b = 0.25
        self.m = 0.01
        self.n = 4

    def to_dict(self):
        return {
            "k": self.k,
            "p": self.p,
            "c": self.c,
            "delta": self.delta,
            "VI_0": self.VI_0,
            "tau_p": self.tau_p,
            "b": self.b,
            "m": self.m,
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
        y0=[0.1, 0, 200000, 0, 0, 0, 0],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "mittler_sulzer_neumann_perelson_1998"
        self.curve_names = [
            "I",
            "E4",
            "VI",
            "VNI",
            "E1",
            "E2",
            "E3",
        ]
        self.state_names = ['I', 'E4', 'VI', 'VNI', 'E1', 'E2', 'E3']
        self.algebraic_names = ['h', 'V']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 13
        p = self.params

        # direct mapping
        c[0] = p.k
        c[1] = p.p
        c[2] = p.c
        c[3] = p.delta
        c[4] = p.VI_0
        c[5] = p.tau_p
        c[6] = p.b
        c[7] = p.m
        c[8] = p.n

        # derived constants
        c[9] = (c[2]*c[3])/(c[0]*c[1])
        c[10] = (c[2]/c[1])*c[4]
        c[11] = c[0]/(power(1.00000+c[7]*c[6], c[8]))
        c[12] = c[6]/(1.00000+c[7]*c[6])

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
