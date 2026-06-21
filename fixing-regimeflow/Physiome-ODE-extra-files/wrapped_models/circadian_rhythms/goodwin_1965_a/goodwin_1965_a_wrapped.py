# Size of variable arrays:
sizeAlgebraic = 0
sizeStates = 2
sizeConstants = 6
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (second)"
    legend_states[0] = "Xi in component Xi (nanomolar)"
    legend_constants[0] = "ai in component Xi (flux)"
    legend_constants[1] = "bi in component Xi (flux)"
    legend_constants[2] = "Ai in component Xi (dimensionless)"
    legend_constants[3] = "ki in component Xi (per_nanomolar)"
    legend_states[1] = "Yi in component Yi (nanomolar)"
    legend_constants[4] = "beta_i in component Yi (flux)"
    legend_constants[5] = "alpha_i in component Yi (first_order_rate_constant)"
    legend_rates[0] = "d/dt Xi in component Xi (nanomolar)"
    legend_rates[1] = "d/dt Yi in component Yi (nanomolar)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 7
    constants[0] = 72
    constants[1] = 2
    constants[2] = 36
    constants[3] = 1
    states[1] = -10
    constants[4] = 0
    constants[5] = 1
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[0] = constants[0]/(constants[2]+constants[3]*states[1])-constants[1]
    rates[1] = constants[5]*states[0]-constants[4]
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
        self.ai = 72
        self.bi = 2
        self.Ai = 36
        self.ki = 1
        self.beta_i = 0
        self.alpha_i = 1

    def to_dict(self):
        return {
            "ai": self.ai,
            "bi": self.bi,
            "Ai": self.Ai,
            "ki": self.ki,
            "beta_i": self.beta_i,
            "alpha_i": self.alpha_i,
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
        y0=[7, -10],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "goodwin_1965_a"
        self.curve_names = [
            "Xi",
            "Yi",
        ]
        self.state_names = ['Xi', 'Yi']
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
        c = [0.0] * 6
        p = self.params

        # direct mapping
        c[0] = p.ai
        c[1] = p.bi
        c[2] = p.Ai
        c[3] = p.ki
        c[4] = p.beta_i
        c[5] = p.alpha_i

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
