# Size of variable arrays:
sizeAlgebraic = 0
sizeStates = 3
sizeConstants = 7
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (day)"
    legend_states[0] = "x in component x (dimensionless)"
    legend_constants[0] = "d1 in component model_parameters (first_order_rate_constant)"
    legend_constants[1] = "a in component model_parameters (first_order_rate_constant)"
    legend_constants[2] = "r in component model_parameters (first_order_rate_constant)"
    legend_states[1] = "y in component y (dimensionless)"
    legend_constants[3] = "kappa in component model_parameters (dimensionless)"
    legend_constants[6] = "d2 in component y (first_order_rate_constant)"
    legend_constants[4] = "p in component model_parameters (first_order_rate_constant)"
    legend_states[2] = "z in component z (dimensionless)"
    legend_constants[5] = "v in component z (first_order_rate_constant)"
    legend_rates[0] = "d/dt x in component x (dimensionless)"
    legend_rates[1] = "d/dt y in component y (dimensionless)"
    legend_rates[2] = "d/dt z in component z (dimensionless)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 10E-1
    constants[0] = 0.005
    constants[1] = 0.03333
    constants[2] = 1.0
    states[1] = 0.0
    constants[3] = 1.0
    constants[4] = 200.0
    states[2] = 0.01
    constants[5] = 0.5
    constants[6] = (-(99.0000*constants[1]*constants[0])+constants[1]*constants[2]+constants[0]*constants[2])/(constants[1]-constants[0])
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[0] = 2.00000*constants[2]*states[1]-(constants[1]*states[0]*(1.00000-states[0]/constants[3])+constants[0]*states[0]*(states[0]/constants[3]))
    rates[1] = constants[1]*states[0]*(1.00000-states[0]/constants[3])-((constants[2]+constants[6])*states[1]+constants[4]*states[2]*states[1])
    rates[2] = constants[4]*states[2]*states[1]-constants[5]*states[2]
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
        self.d1 = 0.005
        self.a = 0.03333
        self.r = 1.0
        self.kappa = 1.0
        self.p = 200.0
        self.v = 0.5

    def to_dict(self):
        return {
            "d1": self.d1,
            "a": self.a,
            "r": self.r,
            "kappa": self.kappa,
            "p": self.p,
            "v": self.v,
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
        y0=[10E-1, 0.0, 0.01],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "yates_stark_klein_antia_callard_2007_b"
        self.curve_names = [
            "x",
            "y",
            "z",
        ]
        self.state_names = ['x', 'y', 'z']
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
        c[0] = p.d1
        c[1] = p.a
        c[2] = p.r
        c[3] = p.kappa
        c[4] = p.p
        c[5] = p.v

        # derived constants
        c[6] = (-(99.0000*c[1]*c[0])+c[1]*c[2]+c[0]*c[2])/(c[1]-c[0])

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
