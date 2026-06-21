# Size of variable arrays:
sizeAlgebraic = 6
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
    legend_voi = "time in component environment (day)"
    legend_states[0] = "x1 in component x1 (cell)"
    legend_constants[0] = "alpha1 in component model_parameters (flux)"
    legend_constants[1] = "beta1 in component model_parameters (first_order_rate_constant)"
    legend_constants[2] = "g11 in component model_parameters (dimensionless)"
    legend_algebraic[0] = "g21 in component model_parameters (dimensionless)"
    legend_states[1] = "x2 in component x2 (cell)"
    legend_constants[3] = "alpha2 in component model_parameters (first_order_rate_constant)"
    legend_constants[4] = "beta2 in component model_parameters (first_order_rate_constant)"
    legend_constants[5] = "g12 in component model_parameters (dimensionless)"
    legend_constants[6] = "g22 in component model_parameters (dimensionless)"
    legend_states[2] = "z in component z (percent)"
    legend_constants[7] = "k1 in component model_parameters (percent_per_cell_per_day)"
    legend_constants[8] = "k2 in component model_parameters (percent_per_cell_per_day)"
    legend_algebraic[3] = "y1 in component y1 (cell)"
    legend_algebraic[5] = "y2 in component y2 (cell)"
    legend_algebraic[2] = "x1_bar in component x1_bar (cell)"
    legend_algebraic[4] = "x2_bar in component x2_bar (cell)"
    legend_algebraic[1] = "gamma in component model_parameters (dimensionless)"
    legend_rates[0] = "d/dt x1 in component x1 (cell)"
    legend_rates[1] = "d/dt x2 in component x2 (cell)"
    legend_rates[2] = "d/dt z in component z (percent)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 10.06066
    constants[0] = 3
    constants[1] = 0.2
    constants[2] = 0.5
    states[1] = 212.132
    constants[3] = 4
    constants[4] = 0.02
    constants[5] = 1
    constants[6] = 0
    states[2] = 100.0
    constants[7] = 0.24
    constants[8] = 0.0017
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[1] = constants[3]*(power(states[0], constants[5]))*(power(states[1], constants[6]))-constants[4]*states[1]
    algebraic[0] = custom_piecewise([greater_equal(voi , 1.00000) & less(voi , 2.00000), 0.150000 , True, -0.500000])
    rates[0] = constants[0]*(power(states[0], constants[2]))*(power(states[1], algebraic[0]))-constants[1]*states[0]
    algebraic[1] = constants[5]*algebraic[0]-(1.00000-constants[2])*(1.00000-constants[6])
    algebraic[2] = (power(constants[1]/constants[0], (1.00000-constants[6])/algebraic[1]))*(power(constants[4]/constants[3], algebraic[0]/algebraic[1]))
    algebraic[3] = custom_piecewise([greater(states[0] , algebraic[2]), states[0]-algebraic[2] , True, 0.00000])
    algebraic[4] = (power(constants[1]/constants[0], constants[5]/algebraic[1]))*(power(constants[4]/constants[3], (1.00000-constants[2])/algebraic[1]))
    algebraic[5] = custom_piecewise([greater(states[1] , algebraic[4]), states[1]-algebraic[4] , True, 0.00000])
    rates[2] = constants[8]*algebraic[5]-constants[7]*algebraic[3]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = custom_piecewise([greater_equal(voi , 1.00000) & less(voi , 2.00000), 0.150000 , True, -0.500000])
    algebraic[1] = constants[5]*algebraic[0]-(1.00000-constants[2])*(1.00000-constants[6])
    algebraic[2] = (power(constants[1]/constants[0], (1.00000-constants[6])/algebraic[1]))*(power(constants[4]/constants[3], algebraic[0]/algebraic[1]))
    algebraic[3] = custom_piecewise([greater(states[0] , algebraic[2]), states[0]-algebraic[2] , True, 0.00000])
    algebraic[4] = (power(constants[1]/constants[0], constants[5]/algebraic[1]))*(power(constants[4]/constants[3], (1.00000-constants[2])/algebraic[1]))
    algebraic[5] = custom_piecewise([greater(states[1] , algebraic[4]), states[1]-algebraic[4] , True, 0.00000])
    return algebraic

def custom_piecewise(cases):
    """Compute result of a piecewise function"""
    return select(cases[0::2],cases[1::2])

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
        self.alpha1 = 3
        self.beta1 = 0.2
        self.g11 = 0.5
        self.alpha2 = 4
        self.beta2 = 0.02
        self.g12 = 1
        self.g22 = 0
        self.k1 = 0.24
        self.k2 = 0.0017

    def to_dict(self):
        return {
            "alpha1": self.alpha1,
            "beta1": self.beta1,
            "g11": self.g11,
            "alpha2": self.alpha2,
            "beta2": self.beta2,
            "g12": self.g12,
            "g22": self.g22,
            "k1": self.k1,
            "k2": self.k2,
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
        y0=[10.06066, 212.132, 100.0],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "komarova_2005"
        self.curve_names = [
            "x1",
            "x2",
            "z",
        ]
        self.state_names = ['x1', 'x2', 'z']
        self.algebraic_names = ['g21', 'gamma', 'x1_bar', 'y1', 'x2_bar', 'y2']
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
        c[0] = p.alpha1
        c[1] = p.beta1
        c[2] = p.g11
        c[3] = p.alpha2
        c[4] = p.beta2
        c[5] = p.g12
        c[6] = p.g22
        c[7] = p.k1
        c[8] = p.k2

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
