# Size of variable arrays:
sizeAlgebraic = 0
sizeStates = 5
sizeConstants = 11
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (hour)"
    legend_states[0] = "x in component x (dimensionless)"
    legend_constants[0] = "d in component model_parameters (first_order_rate_constant)"
    legend_constants[1] = "gamma in component model_parameters (first_order_rate_constant)"
    legend_constants[2] = "lambda in component model_parameters (first_order_rate_constant)"
    legend_constants[3] = "beta in component model_parameters (first_order_rate_constant)"
    legend_states[1] = "v in component v (dimensionless)"
    legend_states[2] = "y0 in component y0 (dimensionless)"
    legend_constants[4] = "a0 in component model_parameters (first_order_rate_constant)"
    legend_constants[5] = "eta in component model_parameters (first_order_rate_constant)"
    legend_constants[6] = "phi in component model_parameters (first_order_rate_constant)"
    legend_states[3] = "L in component L (dimensionless)"
    legend_states[4] = "y1 in component y1 (dimensionless)"
    legend_constants[7] = "a1 in component model_parameters (first_order_rate_constant)"
    legend_constants[8] = "k in component model_parameters (first_order_rate_constant)"
    legend_constants[9] = "u in component model_parameters (first_order_rate_constant)"
    legend_constants[10] = "R0 in component R0 (dimensionless)"
    legend_rates[0] = "d/dt x in component x (dimensionless)"
    legend_rates[2] = "d/dt y0 in component y0 (dimensionless)"
    legend_rates[4] = "d/dt y1 in component y1 (dimensionless)"
    legend_rates[3] = "d/dt L in component L (dimensionless)"
    legend_rates[1] = "d/dt v in component v (dimensionless)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 1
    constants[0] = 0.1
    constants[1] = 0.5
    constants[2] = 10
    constants[3] = 0.1
    states[1] = 1
    states[2] = 0
    constants[4] = 0.1
    constants[5] = 0.01
    constants[6] = 0.1
    states[3] = 0
    states[4] = 0
    constants[7] = 0.2
    constants[8] = 1
    constants[9] = 1
    constants[10] = ((constants[2]*constants[5])/(constants[0]*constants[7]*(constants[4]+constants[5])))*(constants[3]+(constants[1]*constants[6])/(constants[6]+constants[0]))
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[0] = constants[2]-(constants[0]*states[0]+constants[3]*states[0]*states[1]+constants[1]*states[0]*states[1])
    rates[2] = (constants[3]*states[0]*states[1]-(constants[4]*states[2]+constants[5]*states[2]))+constants[6]*states[3]
    rates[4] = constants[5]*states[2]-constants[7]*states[4]
    rates[3] = constants[1]*states[0]*states[1]-(constants[6]*states[3]+constants[0]*states[3])
    rates[1] = constants[8]*states[4]-constants[9]*states[1]
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
        self.d = 0.1
        self.gamma = 0.5
        self.lambda = 10
        self.beta = 0.1
        self.a0 = 0.1
        self.eta = 0.01
        self.phi = 0.1
        self.a1 = 0.2
        self.k = 1
        self.u = 1

    def to_dict(self):
        return {
            "d": self.d,
            "gamma": self.gamma,
            "lambda": self.lambda,
            "beta": self.beta,
            "a0": self.a0,
            "eta": self.eta,
            "phi": self.phi,
            "a1": self.a1,
            "k": self.k,
            "u": self.u,
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
        y0=[1, 1, 0, 0, 0],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "wodarz_sierro_klenerman_2007_a"
        self.curve_names = [
            "x",
            "v",
            "y0",
            "L",
            "y1",
        ]
        self.state_names = ['x', 'v', 'y0', 'L', 'y1']
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
        c = [0.0] * 11
        p = self.params

        # direct mapping
        c[0] = p.d
        c[1] = p.gamma
        c[2] = p.lambda
        c[3] = p.beta
        c[4] = p.a0
        c[5] = p.eta
        c[6] = p.phi
        c[7] = p.a1
        c[8] = p.k
        c[9] = p.u

        # derived constants
        c[10] = ((c[2]*c[5])/(c[0]*c[7]*(c[4]+c[5])))*(c[3]+(c[1]*c[6])/(c[6]+c[0]))

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
