# Size of variable arrays:
sizeAlgebraic = 0
sizeStates = 3
sizeConstants = 13
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "tau in component environment (dimensionless)"
    legend_constants[0] = "mu2 in component x (dimensionless)"
    legend_constants[1] = "c in component x (dimensionless)"
    legend_constants[2] = "p1 in component x (dimensionless)"
    legend_constants[3] = "g1 in component x (dimensionless)"
    legend_constants[4] = "s1 in component x (dimensionless)"
    legend_states[0] = "y in component y (dimensionless)"
    legend_states[1] = "x in component x (dimensionless)"
    legend_states[2] = "z in component z (dimensionless)"
    legend_constants[5] = "r2 in component y (dimensionless)"
    legend_constants[6] = "a in component y (dimensionless)"
    legend_constants[7] = "b in component y (dimensionless)"
    legend_constants[8] = "g2 in component y (dimensionless)"
    legend_constants[9] = "mu3 in component z (dimensionless)"
    legend_constants[10] = "p2 in component z (dimensionless)"
    legend_constants[11] = "g3 in component z (dimensionless)"
    legend_constants[12] = "s2 in component z (dimensionless)"
    legend_rates[1] = "d/dt x in component x (dimensionless)"
    legend_rates[0] = "d/dt y in component y (dimensionless)"
    legend_rates[2] = "d/dt z in component z (dimensionless)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    constants[0] = 0.03
    constants[1] = 0.02
    constants[2] = 0.1245
    constants[3] = 2.0E-7
    constants[4] = 0
    states[0] = 1.0
    states[1] = 1.0
    states[2] = 1.0
    constants[5] = 0.18
    constants[6] = 1.0
    constants[7] = 1.0E-9
    constants[8] = 1.0E5
    constants[9] = 10.0
    constants[10] = 5.0
    constants[11] = 1.0E3
    constants[12] = 0
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[1] = (constants[1]*states[0]-constants[0]*states[1])+(constants[2]*states[1]*states[2])/(constants[3]+states[2])+constants[4]
    rates[0] = constants[5]*states[0]*(1.00000-constants[7]*states[0])-(constants[6]*states[1]*states[0])/(constants[8]+states[0])
    rates[2] = ((constants[10]*states[1]*states[0])/(constants[11]+states[0])-constants[9]*states[2])+constants[12]
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
        self.mu2 = 0.03
        self.c = 0.02
        self.p1 = 0.1245
        self.g1 = 2.0E-7
        self.s1 = 0
        self.r2 = 0.18
        self.a = 1.0
        self.b = 1.0E-9
        self.g2 = 1.0E5
        self.mu3 = 10.0
        self.p2 = 5.0
        self.g3 = 1.0E3
        self.s2 = 0

    def to_dict(self):
        return {
            "mu2": self.mu2,
            "c": self.c,
            "p1": self.p1,
            "g1": self.g1,
            "s1": self.s1,
            "r2": self.r2,
            "a": self.a,
            "b": self.b,
            "g2": self.g2,
            "mu3": self.mu3,
            "p2": self.p2,
            "g3": self.g3,
            "s2": self.s2,
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
        y0=[1.0, 1.0, 1.0],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "kirschner_panetta_1998"
        self.curve_names = [
            "y",
            "x",
            "z",
        ]
        self.state_names = ['y', 'x', 'z']
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
        c = [0.0] * 13
        p = self.params

        # direct mapping
        c[0] = p.mu2
        c[1] = p.c
        c[2] = p.p1
        c[3] = p.g1
        c[4] = p.s1
        c[5] = p.r2
        c[6] = p.a
        c[7] = p.b
        c[8] = p.g2
        c[9] = p.mu3
        c[10] = p.p2
        c[11] = p.g3
        c[12] = p.s2

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
