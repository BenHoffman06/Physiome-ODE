# Size of variable arrays:
sizeAlgebraic = 0
sizeStates = 4
sizeConstants = 7
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (month)"
    legend_states[0] = "L in component L (fraction)"
    legend_constants[0] = "mu_T in component reaction_constants (month)"
    legend_constants[1] = "mu_L in component reaction_constants (month)"
    legend_constants[2] = "mu_A in component reaction_constants (month)"
    legend_constants[3] = "epsilon in component reaction_constants (first_order_rate_constant)"
    legend_states[1] = "M in component M (fraction)"
    legend_states[2] = "T in component T (fraction)"
    legend_constants[4] = "L_0 in component L (dimensionless)"
    legend_states[3] = "A in component A (fraction)"
    legend_constants[5] = "A_0 in component A (dimensionless)"
    legend_constants[6] = "T_0 in component T (dimensionless)"
    legend_rates[0] = "d/dt L in component L (fraction)"
    legend_rates[3] = "d/dt A in component A (fraction)"
    legend_rates[2] = "d/dt T in component T (fraction)"
    legend_rates[1] = "d/dt M in component M (fraction)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 0.33
    constants[0] = 2.4
    constants[1] = 2
    constants[2] = 3.6
    constants[3] = 0
    states[1] = 0
    states[2] = 0.33
    states[3] = 0.34
    constants[4] = constants[1]/(constants[2]+constants[0]+constants[1])
    constants[5] = constants[2]/(constants[2]+constants[0]+constants[1])
    constants[6] = constants[0]/(constants[2]+constants[0]+constants[1])
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[0] = ((1.00000/constants[0])*states[2]-(1.00000/constants[1])*states[0])+constants[3]*states[1]
    rates[3] = (1.00000/constants[1])*states[0]-(1.00000/constants[2])*states[3]
    rates[2] = (1.00000/constants[2])*states[3]-(1.00000/constants[0])*states[2]
    rates[1] = constants[3]*states[2]
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
        self.mu_T = 2.4
        self.mu_L = 2
        self.mu_A = 3.6
        self.epsilon = 0

    def to_dict(self):
        return {
            "mu_T": self.mu_T,
            "mu_L": self.mu_L,
            "mu_A": self.mu_A,
            "epsilon": self.epsilon,
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
        y0=[0.33, 0, 0.33, 0.34],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "halloy_bernard_loussouarn_goldbeter_2002"
        self.curve_names = [
            "L",
            "M",
            "T",
            "A",
        ]
        self.state_names = ['L', 'M', 'T', 'A']
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
        c = [0.0] * 7
        p = self.params

        # direct mapping
        c[0] = p.mu_T
        c[1] = p.mu_L
        c[2] = p.mu_A
        c[3] = p.epsilon

        # derived constants
        c[4] = c[1]/(c[2]+c[0]+c[1])
        c[5] = c[2]/(c[2]+c[0]+c[1])
        c[6] = c[0]/(c[2]+c[0]+c[1])

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
