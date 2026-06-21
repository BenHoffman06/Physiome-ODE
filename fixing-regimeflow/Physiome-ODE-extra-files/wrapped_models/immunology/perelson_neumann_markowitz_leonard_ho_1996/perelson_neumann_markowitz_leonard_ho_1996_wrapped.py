# Size of variable arrays:
sizeAlgebraic = 1
sizeStates = 3
sizeConstants = 5
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (day)"
    legend_constants[0] = "T in component T (per_ml)"
    legend_states[0] = "T_star in component T_star (per_ml)"
    legend_constants[1] = "k in component T_star (second_order_rate_constant)"
    legend_states[1] = "VI in component VI (per_ml)"
    legend_constants[2] = "delta in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[3] = "c in component kinetic_parameters (first_order_rate_constant)"
    legend_states[2] = "VNI in component VNI (per_ml)"
    legend_constants[4] = "N in component VNI (dimensionless)"
    legend_algebraic[0] = "V in component V (per_ml)"
    legend_rates[0] = "d/dt T_star in component T_star (per_ml)"
    legend_rates[1] = "d/dt VI in component VI (per_ml)"
    legend_rates[2] = "d/dt VNI in component VNI (per_ml)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    constants[0] = 170000
    states[0] = 0
    constants[1] = 2.4e-5
    states[1] = 216000.0
    constants[2] = 0.49
    constants[3] = 3.07
    states[2] = 0
    constants[4] = 774
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[0] = constants[1]*states[1]*constants[0]-constants[2]*states[0]
    rates[1] = -(constants[3]*states[1])
    rates[2] = constants[4]*constants[2]*states[0]-constants[3]*states[2]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = states[1]+states[2]
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
        self.T = 170000
        self.k = 2.4e-5
        self.delta = 0.49
        self.c = 3.07
        self.N = 774

    def to_dict(self):
        return {
            "T": self.T,
            "k": self.k,
            "delta": self.delta,
            "c": self.c,
            "N": self.N,
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
        y0=[0, 216000.0, 0],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "perelson_neumann_markowitz_leonard_ho_1996"
        self.curve_names = [
            "T_star",
            "VI",
            "VNI",
        ]
        self.state_names = ['T_star', 'VI', 'VNI']
        self.algebraic_names = ['V']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 5
        p = self.params

        # direct mapping
        c[0] = p.T
        c[1] = p.k
        c[2] = p.delta
        c[3] = p.c
        c[4] = p.N

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
