# Size of variable arrays:
sizeAlgebraic = 2
sizeStates = 6
sizeConstants = 19
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (minute)"
    legend_states[0] = "y1 in component y1 (micromolar)"
    legend_constants[0] = "a1 in component y1 (flux)"
    legend_algebraic[0] = "g1 in component y1 (micromolar)"
    legend_constants[1] = "b1 in component y1 (micromolar)"
    legend_constants[2] = "d1 in component y1 (first_order_rate_constant)"
    legend_states[1] = "y2 in component y2 (micromolar)"
    legend_constants[3] = "a2 in component y2 (flux)"
    legend_algebraic[1] = "g2 in component y2 (micromolar)"
    legend_constants[4] = "b2 in component y2 (micromolar)"
    legend_constants[5] = "d2 in component y2 (first_order_rate_constant)"
    legend_states[2] = "y3 in component y3 (micromolar)"
    legend_constants[6] = "f53 in component y3 (second_order_rate_constant)"
    legend_constants[7] = "f13 in component y3 (second_order_rate_constant)"
    legend_constants[8] = "h36 in component y3 (second_order_rate_constant)"
    legend_constants[9] = "d3 in component y3 (first_order_rate_constant)"
    legend_constants[10] = "E in component y3 (micromolar)"
    legend_states[3] = "y5 in component y5 (micromolar)"
    legend_states[4] = "y6 in component y6 (micromolar)"
    legend_states[5] = "y4 in component y4 (micromolar)"
    legend_constants[11] = "f14 in component y4 (first_order_rate_constant)"
    legend_constants[12] = "f24 in component y4 (first_order_rate_constant)"
    legend_constants[13] = "d4 in component y4 (first_order_rate_constant)"
    legend_constants[14] = "f35 in component y5 (first_order_rate_constant)"
    legend_constants[15] = "f45 in component y5 (first_order_rate_constant)"
    legend_constants[16] = "d5 in component y5 (first_order_rate_constant)"
    legend_constants[17] = "h36 in component y6 (second_order_rate_constant)"
    legend_constants[18] = "d6 in component y6 (first_order_rate_constant)"
    legend_rates[0] = "d/dt y1 in component y1 (micromolar)"
    legend_rates[1] = "d/dt y2 in component y2 (micromolar)"
    legend_rates[2] = "d/dt y3 in component y3 (micromolar)"
    legend_rates[5] = "d/dt y4 in component y4 (micromolar)"
    legend_rates[3] = "d/dt y5 in component y5 (micromolar)"
    legend_rates[4] = "d/dt y6 in component y6 (micromolar)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 0.0
    constants[0] = 10.0
    constants[1] = 10.0
    constants[2] = 0.2
    states[1] = 0.0
    constants[3] = 10.0
    constants[4] = 10.0
    constants[5] = 0.1
    states[2] = 0.0
    constants[6] = 1.5
    constants[7] = 0.6
    constants[8] = 0.1
    constants[9] = 1.0
    constants[10] = 10.0
    states[3] = 0.0
    states[4] = 0.0
    states[5] = 0.0
    constants[11] = 0.1
    constants[12] = 0.8
    constants[13] = 1.1
    constants[14] = 0.3
    constants[15] = 0.1
    constants[16] = 1.0
    constants[17] = 0.1
    constants[18] = 0.001
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[2] = (constants[7]*(constants[10]-(states[2]+states[4]))*states[0]+constants[6]*(constants[10]-(states[2]+states[4]))*states[3])-(constants[8]*states[1]*states[2]+constants[9]*states[2])
    rates[5] = (constants[11]*states[0]+constants[12]*states[1])-constants[13]*states[5]
    rates[3] = (constants[14]*states[2]+constants[15]*states[5])-constants[16]*states[3]
    rates[4] = constants[17]*states[1]*states[2]-constants[18]*states[4]
    algebraic[0] = custom_piecewise([greater_equal(voi , 0.00000) & less(voi , 5.00000), 0.00000 , greater_equal(voi , 5.00000) & less_equal(voi , 10.0000), 1.00000 , True, 0.00000])
    rates[0] = constants[0]*(algebraic[0]/(constants[1]+algebraic[0]))-constants[2]*states[0]
    algebraic[1] = custom_piecewise([greater_equal(voi , 0.00000) & less_equal(voi , 5.00000), 1.00000 , True, 0.00000])
    rates[1] = constants[3]*(algebraic[1]/(constants[4]+algebraic[1]))-constants[5]*states[1]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = custom_piecewise([greater_equal(voi , 0.00000) & less(voi , 5.00000), 0.00000 , greater_equal(voi , 5.00000) & less_equal(voi , 10.0000), 1.00000 , True, 0.00000])
    algebraic[1] = custom_piecewise([greater_equal(voi , 0.00000) & less_equal(voi , 5.00000), 1.00000 , True, 0.00000])
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
        self.a1 = 10.0
        self.b1 = 10.0
        self.d1 = 0.2
        self.a2 = 10.0
        self.b2 = 10.0
        self.d2 = 0.1
        self.f53 = 1.5
        self.f13 = 0.6
        self.h36 = 0.1
        self.d3 = 1.0
        self.E = 10.0
        self.f14 = 0.1
        self.f24 = 0.8
        self.d4 = 1.1
        self.f35 = 0.3
        self.f45 = 0.1
        self.d5 = 1.0
        self.h36_1 = 0.1
        self.d6 = 0.001

    def to_dict(self):
        return {
            "a1": self.a1,
            "b1": self.b1,
            "d1": self.d1,
            "a2": self.a2,
            "b2": self.b2,
            "d2": self.d2,
            "f53": self.f53,
            "f13": self.f13,
            "h36": self.h36,
            "d3": self.d3,
            "E": self.E,
            "f14": self.f14,
            "f24": self.f24,
            "d4": self.d4,
            "f35": self.f35,
            "f45": self.f45,
            "d5": self.d5,
            "h36_1": self.h36_1,
            "d6": self.d6,
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
        y0=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "muller_obeyesekere_mills_ram_2008"
        self.curve_names = [
            "y1",
            "y2",
            "y3",
            "y5",
            "y6",
            "y4",
        ]
        self.state_names = ['y1', 'y2', 'y3', 'y5', 'y6', 'y4']
        self.algebraic_names = ['g1', 'g2']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 19
        p = self.params

        # direct mapping
        c[0] = p.a1
        c[1] = p.b1
        c[2] = p.d1
        c[3] = p.a2
        c[4] = p.b2
        c[5] = p.d2
        c[6] = p.f53
        c[7] = p.f13
        c[8] = p.h36
        c[9] = p.d3
        c[10] = p.E
        c[11] = p.f14
        c[12] = p.f24
        c[13] = p.d4
        c[14] = p.f35
        c[15] = p.f45
        c[16] = p.d5
        c[17] = p.h36_1
        c[18] = p.d6

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
