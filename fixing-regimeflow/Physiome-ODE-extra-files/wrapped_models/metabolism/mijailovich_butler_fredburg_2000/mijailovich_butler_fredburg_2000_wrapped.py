# Size of variable arrays:
sizeAlgebraic = 2
sizeStates = 4
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
    legend_states[0] = "M in component M (dimensionless)"
    legend_states[1] = "AM in component AM (dimensionless)"
    legend_states[2] = "Mp in component Mp (dimensionless)"
    legend_algebraic[0] = "k1 in component model_parameters (first_order_rate_constant)"
    legend_constants[0] = "k2 in component model_parameters (first_order_rate_constant)"
    legend_constants[1] = "gx in component model_parameters (first_order_rate_constant)"
    legend_states[3] = "AMp in component AMp (dimensionless)"
    legend_constants[2] = "fp in component model_parameters (first_order_rate_constant)"
    legend_constants[3] = "gp in component model_parameters (first_order_rate_constant)"
    legend_constants[4] = "k5 in component model_parameters (first_order_rate_constant)"
    legend_algebraic[1] = "k6 in component model_parameters (first_order_rate_constant)"
    legend_constants[5] = "fp1 in component model_parameters (first_order_rate_constant)"
    legend_constants[6] = "gp1 in component model_parameters (first_order_rate_constant)"
    legend_constants[7] = "g1 in component model_parameters (first_order_rate_constant)"
    legend_constants[8] = "gp3 in component model_parameters (first_order_rate_constant)"
    legend_constants[9] = "g3 in component model_parameters (first_order_rate_constant)"
    legend_constants[10] = "g2 in component model_parameters (first_order_rate_constant)"
    legend_constants[11] = "gp2 in component model_parameters (first_order_rate_constant)"
    legend_rates[0] = "d/dt M in component M (dimensionless)"
    legend_rates[2] = "d/dt Mp in component Mp (dimensionless)"
    legend_rates[3] = "d/dt AMp in component AMp (dimensionless)"
    legend_rates[1] = "d/dt AM in component AM (dimensionless)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 1.0
    states[1] = 0.0
    states[2] = 0.0
    constants[0] = 0.1
    constants[1] = 0.11
    states[3] = 0.0
    constants[2] = 0.44
    constants[3] = 0.11
    constants[4] = 0.1
    constants[5] = 0.88
    constants[6] = 0.22
    constants[7] = 0.01
    constants[8] = 3.00000*constants[6]
    constants[9] = 3.00000*constants[7]
    constants[10] = 20.0000*constants[7]
    constants[11] = 4.00000*(constants[5]+constants[6])
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[0] = custom_piecewise([greater(voi , 0.00000) & less(voi , 5.00000), 0.350000 , True, 0.0600000])
    rates[0] = -(algebraic[0]*states[0])+constants[0]*states[2]+constants[1]*states[1]
    rates[2] = (constants[3]*states[3]+algebraic[0]*states[0])-(constants[0]+constants[2])*states[2]
    algebraic[1] = algebraic[0]
    rates[3] = (constants[2]*states[2]+algebraic[1]*states[1])-(constants[4]+constants[3])*states[3]
    rates[1] = constants[4]*states[3]-(algebraic[1]+constants[1])*states[1]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = custom_piecewise([greater(voi , 0.00000) & less(voi , 5.00000), 0.350000 , True, 0.0600000])
    algebraic[1] = algebraic[0]
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
        self.k2 = 0.1
        self.gx = 0.11
        self.fp = 0.44
        self.gp = 0.11
        self.k5 = 0.1
        self.fp1 = 0.88
        self.gp1 = 0.22
        self.g1 = 0.01

    def to_dict(self):
        return {
            "k2": self.k2,
            "gx": self.gx,
            "fp": self.fp,
            "gp": self.gp,
            "k5": self.k5,
            "fp1": self.fp1,
            "gp1": self.gp1,
            "g1": self.g1,
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
        y0=[1.0, 0.0, 0.0, 0.0],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "mijailovich_butler_fredburg_2000"
        self.curve_names = [
            "M",
            "AM",
            "Mp",
            "AMp",
        ]
        self.state_names = ['M', 'AM', 'Mp', 'AMp']
        self.algebraic_names = ['k1', 'k6']
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
        c[0] = p.k2
        c[1] = p.gx
        c[2] = p.fp
        c[3] = p.gp
        c[4] = p.k5
        c[5] = p.fp1
        c[6] = p.gp1
        c[7] = p.g1

        # derived constants
        c[8] = 3.00000*c[6]
        c[9] = 3.00000*c[7]
        c[10] = 20.0000*c[7]
        c[11] = 4.00000*(c[5]+c[6])

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
