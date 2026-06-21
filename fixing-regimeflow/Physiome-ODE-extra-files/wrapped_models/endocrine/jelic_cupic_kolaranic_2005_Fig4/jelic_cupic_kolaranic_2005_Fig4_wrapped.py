# Size of variable arrays:
sizeAlgebraic = 3
sizeStates = 2
sizeConstants = 15
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_algebraic[0] = "time in component environment (second)"
    legend_voi = "tau in component environment (dimensionless)"
    legend_constants[12] = "C_0 in component reaction_constants (per_second)"
    legend_algebraic[1] = "A in component a (molar)"
    legend_states[0] = "a in component a (dimensionless)"
    legend_constants[0] = "alpha in component reaction_constants (dimensionless)"
    legend_constants[1] = "beta in component reaction_constants (dimensionless)"
    legend_constants[2] = "K in component reaction_constants (dimensionless)"
    legend_constants[13] = "C_1 in component reaction_constants (molar)"
    legend_states[1] = "g in component g (dimensionless)"
    legend_algebraic[2] = "G in component g (molar)"
    legend_constants[3] = "gamma in component reaction_constants (dimensionless)"
    legend_constants[4] = "L in component reaction_constants (dimensionless)"
    legend_constants[14] = "C_2 in component reaction_constants (molar)"
    legend_constants[5] = "k2 in component reaction_constants (per_second)"
    legend_constants[6] = "k3 in component reaction_constants (per_second)"
    legend_constants[7] = "k6 in component reaction_constants (per_second)"
    legend_constants[8] = "k7 in component reaction_constants (per_second)"
    legend_constants[9] = "k0 in component reaction_constants (molar_per_second)"
    legend_constants[10] = "k4 in component reaction_constants (per_molar2_per_second)"
    legend_constants[11] = "km in component reaction_constants (molar_per_second)"
    legend_rates[0] = "d/dt a in component a (dimensionless)"
    legend_rates[1] = "d/dt g in component g (dimensionless)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 4.39927
    constants[0] = 0.008
    constants[1] = 1.485
    constants[2] = 30
    states[1] = 1.96477
    constants[3] = 11.385
    constants[4] = 0.1
    constants[5] = 6e-4
    constants[6] = 0.0000048
    constants[7] = 0.000891
    constants[8] = 0.006831
    constants[9] = 8.7831e-11
    constants[10] = 2.1e12
    constants[11] = 6.9001e-14
    constants[12] = constants[5]
    constants[13] = power(constants[5]/constants[10], 1.0/2)
    constants[14] = power(constants[5]/constants[10], 1.0/2)
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[0] = constants[2]-((1.00000+constants[0]+constants[1])*states[0]+states[0]*(power(states[1], 2.00000)))
    rates[1] = ((1.00000-constants[0])*states[0]+states[0]*(power(states[1], 2.00000)))-(constants[4]+constants[3]*states[1])
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = voi/constants[12]
    algebraic[1] = constants[13]*states[0]
    algebraic[2] = constants[14]*states[1]
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
        self.alpha = 0.008
        self.beta = 1.485
        self.K = 30
        self.gamma = 11.385
        self.L = 0.1
        self.k2 = 6e-4
        self.k3 = 0.0000048
        self.k6 = 0.000891
        self.k7 = 0.006831
        self.k0 = 8.7831e-11
        self.k4 = 2.1e12
        self.km = 6.9001e-14

    def to_dict(self):
        return {
            "alpha": self.alpha,
            "beta": self.beta,
            "K": self.K,
            "gamma": self.gamma,
            "L": self.L,
            "k2": self.k2,
            "k3": self.k3,
            "k6": self.k6,
            "k7": self.k7,
            "k0": self.k0,
            "k4": self.k4,
            "km": self.km,
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
        y0=[4.39927, 1.96477],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "jelic_cupic_kolaranic_2005_Fig4"
        self.curve_names = [
            "a",
            "g",
        ]
        self.state_names = ['a', 'g']
        self.algebraic_names = ['time', 'A', 'G']
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
        c[0] = p.alpha
        c[1] = p.beta
        c[2] = p.K
        c[3] = p.gamma
        c[4] = p.L
        c[5] = p.k2
        c[6] = p.k3
        c[7] = p.k6
        c[8] = p.k7
        c[9] = p.k0
        c[10] = p.k4
        c[11] = p.km

        # derived constants
        c[12] = c[5]
        c[13] = power(c[5]/c[10], 1.0/2)
        c[14] = power(c[5]/c[10], 1.0/2)

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
