# Size of variable arrays:
sizeAlgebraic = 0
sizeStates = 4
sizeConstants = 4
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (second)"
    legend_states[0] = "Ca in component Ca (micromolar)"
    legend_constants[0] = "k1 in component reaction_constants (second_order_rate_constant)"
    legend_constants[1] = "k1_ in component reaction_constants (first_order_rate_constant)"
    legend_constants[2] = "k2 in component reaction_constants (second_order_rate_constant)"
    legend_constants[3] = "k2_ in component reaction_constants (first_order_rate_constant)"
    legend_states[1] = "Trop in component Trop (micromolar)"
    legend_states[2] = "CaTrop in component CaTrop (micromolar)"
    legend_states[3] = "Ca2Trop in component Ca2Trop (micromolar)"
    legend_rates[0] = "d/dt Ca in component Ca (micromolar)"
    legend_rates[1] = "d/dt Trop in component Trop (micromolar)"
    legend_rates[2] = "d/dt CaTrop in component CaTrop (micromolar)"
    legend_rates[3] = "d/dt Ca2Trop in component Ca2Trop (micromolar)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 0.05
    constants[0] = 2.033E14
    constants[1] = 2642.0
    constants[2] = 1.017E14
    constants[3] = 13.21
    states[1] = 360.0
    states[2] = 0.01
    states[3] = 0.01
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[0] = (constants[1]*states[2]+constants[3]*states[3])-(constants[0]*states[0]*states[1]+constants[2]*states[0]*states[2])
    rates[1] = constants[1]*states[2]-constants[0]*states[0]*states[1]
    rates[2] = (constants[0]*states[0]*states[1]+constants[3]*states[3])-(constants[1]*states[2]+constants[2]*states[0]*states[2])
    rates[3] = constants[2]*states[0]*states[2]-constants[3]*states[3]
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
        self.k1 = 2.033E14
        self.k1_ = 2642.0
        self.k2 = 1.017E14
        self.k2_ = 13.21

    def to_dict(self):
        return {
            "k1": self.k1,
            "k1_": self.k1_,
            "k2": self.k2,
            "k2_": self.k2_,
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
        y0=[0.05, 360.0, 0.01, 0.01],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "baylor_hollingworth_chandler_2002_f"
        self.curve_names = [
            "Ca",
            "Trop",
            "CaTrop",
            "Ca2Trop",
        ]
        self.state_names = ['Ca', 'Trop', 'CaTrop', 'Ca2Trop']
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
        c = [0.0] * 4
        p = self.params

        # direct mapping
        c[0] = p.k1
        c[1] = p.k1_
        c[2] = p.k2
        c[3] = p.k2_

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
