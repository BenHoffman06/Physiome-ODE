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
    legend_voi = "time in component environment (second)"
    legend_states[0] = "C1 in component C1 (dimensionless)"
    legend_constants[0] = "O2C1 in component reaction_constants (second_order_rate_constant)"
    legend_constants[1] = "C1O2 in component reaction_constants (first_order_rate_constant)"
    legend_constants[2] = "C1C2 in component reaction_constants (first_order_rate_constant)"
    legend_constants[3] = "C2C1 in component reaction_constants (first_order_rate_constant)"
    legend_states[1] = "C2 in component C2 (dimensionless)"
    legend_states[2] = "O2 in component O2 (dimensionless)"
    legend_constants[4] = "Ca in component reaction_constants (micromolar)"
    legend_states[3] = "O1 in component O1 (dimensionless)"
    legend_constants[5] = "O1O2 in component reaction_constants (second_order_rate_constant)"
    legend_constants[6] = "O2O1 in component reaction_constants (first_order_rate_constant)"
    legend_rates[0] = "d/dt C1 in component C1 (dimensionless)"
    legend_rates[1] = "d/dt C2 in component C2 (dimensionless)"
    legend_rates[3] = "d/dt O1 in component O1 (dimensionless)"
    legend_rates[2] = "d/dt O2 in component O2 (dimensionless)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 0.25
    constants[0] = 2.62
    constants[1] = 2277.0
    constants[2] = 60.8
    constants[3] = 198.0
    states[1] = 0.25
    states[2] = 0.25
    constants[4] = 50.0
    states[3] = 0.25
    constants[5] = 2.41
    constants[6] = 85.1
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[0] = (constants[0]*constants[4]*states[2]+constants[3]*states[1])-(constants[1]*states[0]+constants[2]*states[0])
    rates[1] = constants[2]*states[0]-constants[3]*states[1]
    rates[3] = constants[6]*states[2]-constants[5]*constants[4]*states[3]
    rates[2] = (constants[5]*constants[4]*states[3]+constants[1]*states[0])-(constants[6]*states[2]+constants[0]*constants[4]*states[2])
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
        self.O2C1 = 2.62
        self.C1O2 = 2277.0
        self.C1C2 = 60.8
        self.C2C1 = 198.0
        self.Ca = 50.0
        self.O1O2 = 2.41
        self.O2O1 = 85.1

    def to_dict(self):
        return {
            "O2C1": self.O2C1,
            "C1O2": self.C1O2,
            "C1C2": self.C1C2,
            "C2C1": self.C2C1,
            "Ca": self.Ca,
            "O1O2": self.O1O2,
            "O2O1": self.O2O1,
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
        y0=[0.25, 0.25, 0.25, 0.25],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "saftenku_williams_sitsapesan_2001_H2_model"
        self.curve_names = [
            "C1",
            "C2",
            "O2",
            "O1",
        ]
        self.state_names = ['C1', 'C2', 'O2', 'O1']
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
        c[0] = p.O2C1
        c[1] = p.C1O2
        c[2] = p.C1C2
        c[3] = p.C2C1
        c[4] = p.Ca
        c[5] = p.O1O2
        c[6] = p.O2O1

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
