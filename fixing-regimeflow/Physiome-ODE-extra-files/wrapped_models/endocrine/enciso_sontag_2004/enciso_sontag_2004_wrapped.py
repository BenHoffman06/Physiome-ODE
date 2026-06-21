# Size of variable arrays:
sizeAlgebraic = 1
sizeStates = 3
sizeConstants = 9
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (hour)"
    legend_states[0] = "R in component R (ng_ml)"
    legend_constants[0] = "b1 in component R (first_order_rate_constant)"
    legend_constants[1] = "b2 in component R (dimensionless)"
    legend_constants[2] = "b3 in component R (dimensionless)"
    legend_constants[3] = "g1 in component R (dimensionless)"
    legend_constants[4] = "g2 in component R (dimensionless)"
    legend_algebraic[0] = "f_T in component R (ng_ml_hr)"
    legend_states[1] = "T in component T (ng_ml)"
    legend_states[2] = "L in component L (ng_ml)"
    legend_constants[5] = "b2 in component L (first_order_rate_constant)"
    legend_constants[6] = "g1 in component L (first_order_rate_constant)"
    legend_constants[7] = "b3 in component T (first_order_rate_constant)"
    legend_constants[8] = "g2 in component T (first_order_rate_constant)"
    legend_rates[0] = "d/dt R in component R (ng_ml)"
    legend_rates[2] = "d/dt L in component L (ng_ml)"
    legend_rates[1] = "d/dt T in component T (ng_ml)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 0.1
    constants[0] = 1.0
    constants[1] = 1.0
    constants[2] = 1.0
    constants[3] = 10.0
    constants[4] = 10.0
    states[1] = 0.0
    states[2] = 0.0
    constants[5] = 1.0
    constants[6] = 10.0
    constants[7] = 1.0
    constants[8] = 10.0
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[2] = constants[6]*states[0]-constants[5]*states[2]
    rates[1] = constants[8]*states[2]-constants[7]*states[1]
    algebraic[0] = (constants[0]*constants[1]*constants[2]*states[1])/(constants[3]*constants[4])
    rates[0] = algebraic[0]-constants[0]*states[0]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = (constants[0]*constants[1]*constants[2]*states[1])/(constants[3]*constants[4])
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
        self.b1 = 1.0
        self.b2 = 1.0
        self.b3 = 1.0
        self.g1 = 10.0
        self.g2 = 10.0
        self.b2_1 = 1.0
        self.g1_1 = 10.0
        self.b3_1 = 1.0
        self.g2_1 = 10.0

    def to_dict(self):
        return {
            "b1": self.b1,
            "b2": self.b2,
            "b3": self.b3,
            "g1": self.g1,
            "g2": self.g2,
            "b2_1": self.b2_1,
            "g1_1": self.g1_1,
            "b3_1": self.b3_1,
            "g2_1": self.g2_1,
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
        y0=[0.1, 0.0, 0.0],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "enciso_sontag_2004"
        self.curve_names = [
            "R",
            "T",
            "L",
        ]
        self.state_names = ['R', 'T', 'L']
        self.algebraic_names = ['f_T']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 9
        p = self.params

        # direct mapping
        c[0] = p.b1
        c[1] = p.b2
        c[2] = p.b3
        c[3] = p.g1
        c[4] = p.g2
        c[5] = p.b2_1
        c[6] = p.g1_1
        c[7] = p.b3_1
        c[8] = p.g2_1

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
