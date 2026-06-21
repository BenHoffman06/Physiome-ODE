# Size of variable arrays:
sizeAlgebraic = 0
sizeStates = 5
sizeConstants = 13
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (hour)"
    legend_states[0] = "Y in component Y (dimensionless)"
    legend_constants[0] = "C1 in component model_parameters (dimensionless)"
    legend_constants[1] = "k1 in component model_parameters (first_order_rate_constant)"
    legend_states[1] = "P in component P (dimensionless)"
    legend_constants[2] = "K in component model_parameters (dimensionless)"
    legend_constants[3] = "C in component model_parameters (dimensionless)"
    legend_constants[4] = "C2 in component model_parameters (dimensionless)"
    legend_constants[5] = "k2 in component model_parameters (first_order_rate_constant)"
    legend_constants[6] = "ky in component model_parameters (first_order_rate_constant)"
    legend_states[2] = "X in component X (dimensionless)"
    legend_constants[7] = "k3 in component model_parameters (first_order_rate_constant)"
    legend_constants[8] = "k4 in component model_parameters (first_order_rate_constant)"
    legend_states[3] = "Z in component Z (dimensionless)"
    legend_constants[9] = "C3 in component model_parameters (dimensionless)"
    legend_constants[10] = "k5 in component model_parameters (first_order_rate_constant)"
    legend_constants[11] = "K2 in component model_parameters (dimensionless)"
    legend_states[4] = "IL6 in component IL6 (dimensionless)"
    legend_constants[12] = "k6 in component model_parameters (first_order_rate_constant)"
    legend_rates[0] = "d/dt Y in component Y (dimensionless)"
    legend_rates[2] = "d/dt X in component X (dimensionless)"
    legend_rates[1] = "d/dt P in component P (dimensionless)"
    legend_rates[3] = "d/dt Z in component Z (dimensionless)"
    legend_rates[4] = "d/dt IL6 in component IL6 (dimensionless)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 10.0
    constants[0] = 1.0
    constants[1] = 1.0
    states[1] = 10.0
    constants[2] = 5.0
    constants[3] = 50.0
    constants[4] = 1.0
    constants[5] = 1.3
    constants[6] = 0.01
    states[2] = 500.0
    constants[7] = 0.05
    constants[8] = 0.9
    states[3] = 200.0
    constants[9] = 1.0
    constants[10] = 5.0
    constants[11] = 2.0
    states[4] = 1.9
    constants[12] = 0.02
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[0] = constants[1]*constants[0]*(states[1]/(constants[2]+states[1]))*constants[3]-(constants[5]*constants[4]*(1.00000-states[1]/(constants[2]+states[1]))*states[0]+constants[6]*states[0])
    rates[2] = constants[5]*constants[4]*(1.00000-states[1]/(constants[2]+states[1]))*states[0]-constants[7]*states[2]
    rates[1] = custom_piecewise([greater_equal(voi , 0.00000) & less(voi , 6.00000), 10.0000-constants[8]*states[1] , greater_equal(voi , 6.00000) & less(voi , 12.0000), -(constants[8]*states[1]) , greater_equal(voi , 12.0000) & less(voi , 18.0000), 10.0000-constants[8]*states[1] , greater_equal(voi , 18.0000) & less(voi , 24.0000), -(constants[8]*states[1]) , greater_equal(voi , 24.0000) & less(voi , 30.0000), 10.0000-constants[8]*states[1] , greater_equal(voi , 30.0000) & less(voi , 36.0000), -(constants[8]*states[1]) , greater_equal(voi , 36.0000) & less(voi , 42.0000), 10.0000-constants[8]*states[1] , greater_equal(voi , 42.0000) & less(voi , 48.0000), -(constants[8]*states[1]) , greater_equal(voi , 48.0000) & less(voi , 54.0000), 10.0000-constants[8]*states[1] , greater_equal(voi , 54.0000) & less(voi , 60.0000), -(constants[8]*states[1]) , greater_equal(voi , 60.0000) & less(voi , 66.0000), 10.0000-constants[8]*states[1] , greater_equal(voi , 66.0000) & less(voi , 72.0000), -(constants[8]*states[1]) , greater_equal(voi , 72.0000) & less(voi , 78.0000), 10.0000-constants[8]*states[1] , greater_equal(voi , 78.0000) & less(voi , 84.0000), -(constants[8]*states[1]) , greater_equal(voi , 84.0000) & less(voi , 90.0000), 10.0000-constants[8]*states[1] , greater_equal(voi , 90.0000) & less(voi , 96.0000), -(constants[8]*states[1]) , True, float('nan')])
    rates[3] = constants[10]*constants[9]*(states[4]/(constants[11]+states[4]))-constants[12]*states[3]
    rates[4] = 0.100000*states[2]-10.0000*states[4]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
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
        self.C1 = 1.0
        self.k1 = 1.0
        self.K = 5.0
        self.C = 50.0
        self.C2 = 1.0
        self.k2 = 1.3
        self.ky = 0.01
        self.k3 = 0.05
        self.k4 = 0.9
        self.C3 = 1.0
        self.k5 = 5.0
        self.K2 = 2.0
        self.k6 = 0.02

    def to_dict(self):
        return {
            "C1": self.C1,
            "k1": self.k1,
            "K": self.K,
            "C": self.C,
            "C2": self.C2,
            "k2": self.k2,
            "ky": self.ky,
            "k3": self.k3,
            "k4": self.k4,
            "C3": self.C3,
            "k5": self.k5,
            "K2": self.K2,
            "k6": self.k6,
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
        y0=[10.0, 10.0, 500.0, 200.0, 1.9],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "kroll_2000"
        self.curve_names = [
            "Y",
            "P",
            "X",
            "Z",
            "IL6",
        ]
        self.state_names = ['Y', 'P', 'X', 'Z', 'IL6']
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
        c[0] = p.C1
        c[1] = p.k1
        c[2] = p.K
        c[3] = p.C
        c[4] = p.C2
        c[5] = p.k2
        c[6] = p.ky
        c[7] = p.k3
        c[8] = p.k4
        c[9] = p.C3
        c[10] = p.k5
        c[11] = p.K2
        c[12] = p.k6

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
