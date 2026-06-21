# Size of variable arrays:
sizeAlgebraic = 3
sizeStates = 4
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
    legend_states[0] = "x in component x (per_mm3)"
    legend_constants[0] = "lamda in component x (per_mm3_per_day)"
    legend_constants[1] = "d in component x (per_day)"
    legend_constants[2] = "beta in component kinetic_parameters (mm3_per_day)"
    legend_algebraic[0] = "s in component kinetic_parameters (dimensionless)"
    legend_states[1] = "y in component y (per_mm3)"
    legend_constants[3] = "a in component y (per_day)"
    legend_constants[4] = "p in component kinetic_parameters (mm3_per_day)"
    legend_states[2] = "z in component z (per_mm3)"
    legend_algebraic[1] = "log_y in component y (dimensionless)"
    legend_states[3] = "w in component w (per_mm3)"
    legend_constants[5] = "b in component w (per_day)"
    legend_constants[6] = "c in component kinetic_parameters (mm3_mm3_per_day)"
    legend_constants[7] = "q in component kinetic_parameters (per_mm3)"
    legend_algebraic[2] = "log_w in component w (dimensionless)"
    legend_constants[8] = "h in component z (per_day)"
    legend_rates[0] = "d/dt x in component x (per_mm3)"
    legend_rates[1] = "d/dt y in component y (per_mm3)"
    legend_rates[3] = "d/dt w in component w (per_mm3)"
    legend_rates[2] = "d/dt z in component z (per_mm3)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 10
    constants[0] = 1
    constants[1] = 0.1
    constants[2] = 0.5
    states[1] = 0.1
    constants[3] = 0.2
    constants[4] = 1
    states[2] = 0
    states[3] = 0.001
    constants[5] = 0.01
    constants[6] = 0.1
    constants[7] = 0.5
    constants[8] = 0.1
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[3] = constants[6]*states[0]*states[1]*states[3]-(constants[6]*constants[7]*states[1]*states[3]+constants[5]*states[3])
    rates[2] = constants[6]*constants[7]*states[1]*states[3]-constants[8]*states[2]
    algebraic[0] = custom_piecewise([less_equal(voi , 15.0000), 1.00000 , greater_equal(voi , 40.0000), 1.00000 , True, 0.00420000])
    rates[0] = constants[0]-(constants[1]*states[0]+algebraic[0]*constants[2]*states[0]*states[1])
    rates[1] = algebraic[0]*constants[2]*states[0]*states[1]-(constants[3]*states[1]+constants[4]*states[1]*states[2])
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = custom_piecewise([less_equal(voi , 15.0000), 1.00000 , greater_equal(voi , 40.0000), 1.00000 , True, 0.00420000])
    algebraic[1] = log(states[1]*1.00000, 10)
    algebraic[2] = log(states[3]*1.00000, 10)
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
        self.lamda = 1
        self.d = 0.1
        self.beta = 0.5
        self.a = 0.2
        self.p = 1
        self.b = 0.01
        self.c = 0.1
        self.q = 0.5
        self.h = 0.1

    def to_dict(self):
        return {
            "lamda": self.lamda,
            "d": self.d,
            "beta": self.beta,
            "a": self.a,
            "p": self.p,
            "b": self.b,
            "c": self.c,
            "q": self.q,
            "h": self.h,
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
        y0=[10, 0.1, 0, 0.001],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "wodarz_nowak_1999"
        self.curve_names = [
            "x",
            "y",
            "z",
            "w",
        ]
        self.state_names = ['x', 'y', 'z', 'w']
        self.algebraic_names = ['s', 'log_y', 'log_w']
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
        c[0] = p.lamda
        c[1] = p.d
        c[2] = p.beta
        c[3] = p.a
        c[4] = p.p
        c[5] = p.b
        c[6] = p.c
        c[7] = p.q
        c[8] = p.h

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
