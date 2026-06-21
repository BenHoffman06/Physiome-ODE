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
    legend_voi = "time in component environment (hour)"
    legend_constants[0] = "T_a in component model_parameters (celsius)"
    legend_constants[1] = "T_b in component model_parameters (celsius)"
    legend_constants[2] = "delta_T in component model_parameters (celsius)"
    legend_constants[3] = "kinc in component model_parameters (W_per_kg_C2)"
    legend_algebraic[2] = "M_c in component M_c (W_per_kg)"
    legend_constants[4] = "t_day in component M_c (hour)"
    legend_constants[5] = "t_night in component M_c (hour)"
    legend_algebraic[0] = "tprime in component M_c (second)"
    legend_constants[6] = "day_length in component M_c (second)"
    legend_constants[13] = "M_day in component M_day (W_per_kg)"
    legend_constants[14] = "M_night in component M_night (W_per_kg)"
    legend_states[0] = "M in component M (W_per_kg)"
    legend_constants[7] = "km in component M (per_hour)"
    legend_states[1] = "T in component T (celsius)"
    legend_constants[8] = "c in component T (kJ_per_kg_C)"
    legend_algebraic[1] = "k in component k (W_per_kg_C)"
    legend_constants[12] = "kb in component kb (W_per_kg_C)"
    legend_constants[10] = "T_day in component T_day (celsius)"
    legend_constants[11] = "T_night in component T_night (celsius)"
    legend_constants[9] = "M_b in component kb (W_per_kg)"
    legend_rates[0] = "d/dt M in component M (W_per_kg)"
    legend_rates[1] = "d/dt T in component T (celsius)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    constants[0] = 21.0
    constants[1] = 38.0
    constants[2] = 1.57
    constants[3] = 0.0258
    constants[4] = 17.5
    constants[5] = 6.73
    constants[6] = 86400
    states[0] = 3.5
    constants[7] = 1.1375
    states[1] = 38.785
    constants[8] = 3.47
    constants[9] = 3.0
    constants[10] = constants[1]+constants[2]/2.00000
    constants[11] = constants[1]-constants[2]/2.00000
    constants[12] = constants[9]/(constants[1]-constants[0])
    constants[13] = (constants[12]+constants[3]*(constants[10]-constants[1]))*(constants[10]-constants[0])
    constants[14] = (constants[12]+constants[3]*(constants[11]-constants[1]))*(constants[11]-constants[0])
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[1] = constants[12]+constants[3]*(states[1]-constants[1])
    rates[1] = (power(constants[8], -1.00000))*(states[0]-algebraic[1]*(states[1]-constants[0]))
    algebraic[0] =  voi*3600.00*1.00000 % constants[6]
    algebraic[2] = custom_piecewise([greater_equal(algebraic[0]/3600.00 , constants[5]) & less(algebraic[0]/3600.00 , constants[4]), constants[14] , True, constants[13]])
    rates[0] = -constants[7]*(states[0]-algebraic[2])
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[1] = constants[12]+constants[3]*(states[1]-constants[1])
    algebraic[0] =  voi*3600.00*1.00000 % constants[6]
    algebraic[2] = custom_piecewise([greater_equal(algebraic[0]/3600.00 , constants[5]) & less(algebraic[0]/3600.00 , constants[4]), constants[14] , True, constants[13]])
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
        self.T_a = 21.0
        self.T_b = 38.0
        self.delta_T = 1.57
        self.kinc = 0.0258
        self.t_day = 17.5
        self.t_night = 6.73
        self.day_length = 86400
        self.km = 1.1375
        self.c = 3.47
        self.M_b = 3.0

    def to_dict(self):
        return {
            "T_a": self.T_a,
            "T_b": self.T_b,
            "delta_T": self.delta_T,
            "kinc": self.kinc,
            "t_day": self.t_day,
            "t_night": self.t_night,
            "day_length": self.day_length,
            "km": self.km,
            "c": self.c,
            "M_b": self.M_b,
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
        y0=[3.5, 38.785],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "overgaard_baseline_2007"
        self.curve_names = [
            "M",
            "T",
        ]
        self.state_names = ['M', 'T']
        self.algebraic_names = ['tprime', 'k', 'M_c']
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
        c[0] = p.T_a
        c[1] = p.T_b
        c[2] = p.delta_T
        c[3] = p.kinc
        c[4] = p.t_day
        c[5] = p.t_night
        c[6] = p.day_length
        c[7] = p.km
        c[8] = p.c
        c[9] = p.M_b

        # derived constants
        c[10] = c[1]+c[2]/2.00000
        c[11] = c[1]-c[2]/2.00000
        c[12] = c[9]/(c[1]-c[0])
        c[13] = (c[12]+c[3]*(c[10]-c[1]))*(c[10]-c[0])
        c[14] = (c[12]+c[3]*(c[11]-c[1]))*(c[11]-c[0])

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
