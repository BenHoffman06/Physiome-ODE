# Size of variable arrays:
sizeAlgebraic = 0
sizeStates = 3
sizeConstants = 12
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (second)"
    legend_states[0] = "x in component x (dimensionless)"
    legend_constants[0] = "r_1 in component x (rate)"
    legend_constants[1] = "r_2 in component x (rate)"
    legend_constants[2] = "c_1 in component x (rate)"
    legend_states[1] = "z in component z (dimensionless)"
    legend_states[2] = "y in component y (dimensionless)"
    legend_constants[3] = "r_3 in component y (rate)"
    legend_constants[4] = "r_4 in component y (rate)"
    legend_constants[5] = "c_2 in component y (rate)"
    legend_constants[6] = "epsilon in component model_constants (dimensionless)"
    legend_constants[7] = "r_5 in component z (rate)"
    legend_constants[8] = "r_6 in component z (rate)"
    legend_constants[9] = "r_7 in component z (rate)"
    legend_constants[10] = "z_hat in component z (dimensionless)"
    legend_constants[11] = "y_hat in component z (dimensionless)"
    legend_rates[0] = "d/dt x in component x (dimensionless)"
    legend_rates[2] = "d/dt y in component y (dimensionless)"
    legend_rates[1] = "d/dt z in component z (dimensionless)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 4.0
    constants[0] = 0.2
    constants[1] = 0.1
    constants[2] = 0.1
    states[1] = 1.0
    states[2] = 0.0
    constants[3] = 0.1
    constants[4] = 0.1
    constants[5] = 0.1
    constants[6] = 0.1
    constants[7] = 0.1
    constants[8] = 0.1
    constants[9] = 0.05
    constants[10] = 2.0
    constants[11] = 1.24
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[0] = states[1]*(constants[0]*states[2]+-constants[1]*states[0]+constants[2])
    rates[2] = constants[6]*((constants[3]/states[1]-constants[4]*states[0])+constants[5])
    rates[1] = (constants[7]*(states[2]-constants[11])*(constants[10]-states[1])+constants[8]*states[1]*(constants[10]-states[1]))-constants[9]*states[1]
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
        self.r_1 = 0.2
        self.r_2 = 0.1
        self.c_1 = 0.1
        self.r_3 = 0.1
        self.r_4 = 0.1
        self.c_2 = 0.1
        self.epsilon = 0.1
        self.r_5 = 0.1
        self.r_6 = 0.1
        self.r_7 = 0.05
        self.z_hat = 2.0
        self.y_hat = 1.24

    def to_dict(self):
        return {
            "r_1": self.r_1,
            "r_2": self.r_2,
            "c_1": self.c_1,
            "r_3": self.r_3,
            "r_4": self.r_4,
            "c_2": self.c_2,
            "epsilon": self.epsilon,
            "r_5": self.r_5,
            "r_6": self.r_6,
            "r_7": self.r_7,
            "z_hat": self.z_hat,
            "y_hat": self.y_hat,
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
        y0=[4.0, 1.0, 0.0],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "lenbury_ruktamatakul_amornsamarnkul_2001_a"
        self.curve_names = [
            "x",
            "z",
            "y",
        ]
        self.state_names = ['x', 'z', 'y']
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
        c = [0.0] * 12
        p = self.params

        # direct mapping
        c[0] = p.r_1
        c[1] = p.r_2
        c[2] = p.c_1
        c[3] = p.r_3
        c[4] = p.r_4
        c[5] = p.c_2
        c[6] = p.epsilon
        c[7] = p.r_5
        c[8] = p.r_6
        c[9] = p.r_7
        c[10] = p.z_hat
        c[11] = p.y_hat

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
