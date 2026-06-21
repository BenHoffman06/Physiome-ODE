# Size of variable arrays:
sizeAlgebraic = 0
sizeStates = 3
sizeConstants = 8
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (second)"
    legend_states[0] = "X1 in component X1 (nanomolar)"
    legend_constants[0] = "a1 in component X1 (flux)"
    legend_constants[1] = "b1 in component X1 (first_order_rate_constant)"
    legend_constants[2] = "A1 in component X1 (dimensionless)"
    legend_constants[3] = "k1 in component X1 (per_nanomolar)"
    legend_states[1] = "Z1 in component Z1 (nanomolar)"
    legend_states[2] = "Y1 in component Y1 (nanomolar)"
    legend_constants[4] = "beta_1 in component Y1 (first_order_rate_constant)"
    legend_constants[5] = "alpha_1 in component Y1 (first_order_rate_constant)"
    legend_constants[6] = "gamma_1 in component Z1 (first_order_rate_constant)"
    legend_constants[7] = "delta_1 in component Z1 (first_order_rate_constant)"
    legend_rates[0] = "d/dt X1 in component X1 (nanomolar)"
    legend_rates[2] = "d/dt Y1 in component Y1 (nanomolar)"
    legend_rates[1] = "d/dt Z1 in component Z1 (nanomolar)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 7
    constants[0] = 360
    constants[1] = 1
    constants[2] = 43
    constants[3] = 1
    states[1] = 0
    states[2] = 0
    constants[4] = 0.6
    constants[5] = 1
    constants[6] = 1
    constants[7] = 0.8
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[0] = constants[0]/(constants[2]+constants[3]*states[1])-constants[1]*states[0]
    rates[2] = constants[5]*states[0]-constants[4]*states[2]
    rates[1] = constants[6]*states[2]-constants[7]*states[1]
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
        self.a1 = 360
        self.b1 = 1
        self.A1 = 43
        self.k1 = 1
        self.beta_1 = 0.6
        self.alpha_1 = 1
        self.gamma_1 = 1
        self.delta_1 = 0.8

    def to_dict(self):
        return {
            "a1": self.a1,
            "b1": self.b1,
            "A1": self.A1,
            "k1": self.k1,
            "beta_1": self.beta_1,
            "alpha_1": self.alpha_1,
            "gamma_1": self.gamma_1,
            "delta_1": self.delta_1,
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
        y0=[7, 0, 0],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "goodwin_1965_c"
        self.curve_names = [
            "X1",
            "Z1",
            "Y1",
        ]
        self.state_names = ['X1', 'Z1', 'Y1']
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
        c = [0.0] * 8
        p = self.params

        # direct mapping
        c[0] = p.a1
        c[1] = p.b1
        c[2] = p.A1
        c[3] = p.k1
        c[4] = p.beta_1
        c[5] = p.alpha_1
        c[6] = p.gamma_1
        c[7] = p.delta_1

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
