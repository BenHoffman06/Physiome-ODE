# Size of variable arrays:
sizeAlgebraic = 0
sizeStates = 5
sizeConstants = 15
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
    legend_constants[0] = "r1 in component x (rate)"
    legend_constants[1] = "r2 in component x (rate)"
    legend_constants[2] = "c1 in component x (rate)"
    legend_states[1] = "z in component z (dimensionless)"
    legend_states[2] = "y in component y (dimensionless)"
    legend_constants[3] = "r3 in component y (rate)"
    legend_constants[4] = "r4 in component y (rate)"
    legend_constants[5] = "c2 in component y (rate)"
    legend_constants[6] = "c3 in component y (rate)"
    legend_constants[7] = "epsilon in component model_constants (dimensionless)"
    legend_states[3] = "u in component u (dimensionless)"
    legend_constants[8] = "r5 in component z (rate)"
    legend_constants[9] = "r6 in component z (rate)"
    legend_constants[10] = "r7 in component z (rate)"
    legend_constants[11] = "z_ in component z (dimensionless)"
    legend_constants[12] = "y_ in component z (dimensionless)"
    legend_constants[13] = "delta in component z (dimensionless)"
    legend_constants[14] = "omega in component u (rate)"
    legend_states[4] = "v in component u (dimensionless)"
    legend_rates[0] = "d/dt x in component x (dimensionless)"
    legend_rates[2] = "d/dt y in component y (dimensionless)"
    legend_rates[1] = "d/dt z in component z (dimensionless)"
    legend_rates[3] = "d/dt u in component u (dimensionless)"
    legend_rates[4] = "d/dt v in component u (dimensionless)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 5
    constants[0] = 0.15
    constants[1] = 0.12
    constants[2] = 0.1
    states[1] = 1
    states[2] = 0
    constants[3] = 0.05
    constants[4] = 0.03
    constants[5] = 0.1
    constants[6] = 0.005
    constants[7] = 0.1
    states[3] = 1
    constants[8] = 0.09
    constants[9] = 0.1
    constants[10] = 0.05
    constants[11] = 1.01
    constants[12] = 1.08
    constants[13] = 0.01
    constants[14] = 0.05
    states[4] = 0
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[0] = states[1]*(constants[0]*states[2]+-constants[1]*states[0]+constants[2])
    rates[2] = constants[7]*(constants[3]/states[1]+-constants[4]*states[0]+constants[5]+constants[6]*states[3])
    rates[1] = constants[7]*constants[13]*((constants[8]*(states[2]-constants[12])*(constants[11]-states[1])+constants[9]*states[1]*(constants[11]-states[1]))-constants[10]*states[1])
    rates[3] = -constants[14]*states[4]
    rates[4] = constants[14]*states[3]
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
        self.r1 = 0.15
        self.r2 = 0.12
        self.c1 = 0.1
        self.r3 = 0.05
        self.r4 = 0.03
        self.c2 = 0.1
        self.c3 = 0.005
        self.epsilon = 0.1
        self.r5 = 0.09
        self.r6 = 0.1
        self.r7 = 0.05
        self.z_ = 1.01
        self.y_ = 1.08
        self.delta = 0.01
        self.omega = 0.05

    def to_dict(self):
        return {
            "r1": self.r1,
            "r2": self.r2,
            "c1": self.c1,
            "r3": self.r3,
            "r4": self.r4,
            "c2": self.c2,
            "c3": self.c3,
            "epsilon": self.epsilon,
            "r5": self.r5,
            "r6": self.r6,
            "r7": self.r7,
            "z_": self.z_,
            "y_": self.y_,
            "delta": self.delta,
            "omega": self.omega,
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
        y0=[5, 1, 0, 1, 0],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "lenbury_ruktamatakul_amornsamarnkul_2001_b"
        self.curve_names = [
            "x",
            "z",
            "y",
            "u",
            "v",
        ]
        self.state_names = ['x', 'z', 'y', 'u', 'v']
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
        c = [0.0] * 15
        p = self.params

        # direct mapping
        c[0] = p.r1
        c[1] = p.r2
        c[2] = p.c1
        c[3] = p.r3
        c[4] = p.r4
        c[5] = p.c2
        c[6] = p.c3
        c[7] = p.epsilon
        c[8] = p.r5
        c[9] = p.r6
        c[10] = p.r7
        c[11] = p.z_
        c[12] = p.y_
        c[13] = p.delta
        c[14] = p.omega

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
