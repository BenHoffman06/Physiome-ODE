# Size of variable arrays:
sizeAlgebraic = 0
sizeStates = 8
sizeConstants = 17
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (second)"
    legend_states[0] = "C1 in component C1 (dimensionless)"
    legend_constants[0] = "C1C2 in component reaction_constants (second_order_rate_constant)"
    legend_constants[1] = "C2C1 in component reaction_constants (first_order_rate_constant)"
    legend_states[1] = "C2 in component C2 (dimensionless)"
    legend_constants[2] = "Ca in component reaction_constants (micromolar)"
    legend_constants[3] = "C2C3 in component reaction_constants (second_order_rate_constant)"
    legend_constants[4] = "C3C2 in component reaction_constants (first_order_rate_constant)"
    legend_constants[5] = "C2C5 in component reaction_constants (first_order_rate_constant)"
    legend_constants[6] = "C5C2 in component reaction_constants (first_order_rate_constant)"
    legend_states[2] = "C3 in component C3 (dimensionless)"
    legend_states[3] = "C5 in component C5 (dimensionless)"
    legend_constants[7] = "O1C3 in component reaction_constants (first_order_rate_constant)"
    legend_constants[8] = "C3O1 in component reaction_constants (first_order_rate_constant)"
    legend_constants[9] = "O2C3 in component reaction_constants (first_order_rate_constant)"
    legend_constants[10] = "C3O2 in component reaction_constants (first_order_rate_constant)"
    legend_constants[11] = "O3C3 in component reaction_constants (first_order_rate_constant)"
    legend_constants[12] = "C3O3 in component reaction_constants (first_order_rate_constant)"
    legend_states[4] = "O1 in component O1 (dimensionless)"
    legend_states[5] = "O2 in component O2 (dimensionless)"
    legend_states[6] = "O3 in component O3 (dimensionless)"
    legend_states[7] = "C4 in component C4 (dimensionless)"
    legend_constants[13] = "O2C4 in component reaction_constants (first_order_rate_constant)"
    legend_constants[14] = "C4O2 in component reaction_constants (first_order_rate_constant)"
    legend_constants[15] = "O3C4 in component reaction_constants (first_order_rate_constant)"
    legend_constants[16] = "C4O3 in component reaction_constants (first_order_rate_constant)"
    legend_rates[0] = "d/dt C1 in component C1 (dimensionless)"
    legend_rates[1] = "d/dt C2 in component C2 (dimensionless)"
    legend_rates[2] = "d/dt C3 in component C3 (dimensionless)"
    legend_rates[7] = "d/dt C4 in component C4 (dimensionless)"
    legend_rates[3] = "d/dt C5 in component C5 (dimensionless)"
    legend_rates[4] = "d/dt O1 in component O1 (dimensionless)"
    legend_rates[5] = "d/dt O2 in component O2 (dimensionless)"
    legend_rates[6] = "d/dt O3 in component O3 (dimensionless)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 0.125
    constants[0] = 2.5
    constants[1] = 13.3
    states[1] = 0.125
    constants[2] = 20.0
    constants[3] = 68.0
    constants[4] = 8000.0
    constants[5] = 0.13
    constants[6] = 3.6
    states[2] = 0.125
    states[3] = 0.125
    constants[7] = 3400.0
    constants[8] = 1100.0
    constants[9] = 92.0
    constants[10] = 17.0
    constants[11] = 138.0
    constants[12] = 14.0
    states[4] = 0.125
    states[5] = 0.125
    states[6] = 0.125
    states[7] = 0.125
    constants[13] = 1900.0
    constants[14] = 520.0
    constants[15] = 300.0
    constants[16] = 46.0
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[0] = constants[1]*states[1]-constants[0]*constants[2]*states[1]
    rates[1] = (constants[0]*constants[2]*states[0]+constants[4]*states[2]+constants[6]*states[3])-(constants[1]*states[1]+constants[3]*constants[2]*states[1]+constants[5]*states[1])
    rates[2] = (constants[3]*constants[2]*states[1]+constants[7]*states[4]+constants[11]*states[6]+constants[9]*states[5])-(constants[4]*states[2]+constants[8]*states[2]+constants[10]*states[2]+constants[12]*states[2])
    rates[7] = (constants[13]*states[5]+constants[15]*states[6])-(constants[14]*states[7]+constants[16]*states[7])
    rates[3] = constants[5]*states[1]-constants[6]*states[3]
    rates[4] = constants[8]*states[2]-constants[7]*states[4]
    rates[5] = (constants[10]*states[2]+constants[14]*states[7])-(constants[9]*states[5]+constants[13]*states[5])
    rates[6] = (constants[12]*states[2]+constants[16]*states[7])-(constants[11]*states[6]+constants[15]*states[6])
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
        self.C1C2 = 2.5
        self.C2C1 = 13.3
        self.Ca = 20.0
        self.C2C3 = 68.0
        self.C3C2 = 8000.0
        self.C2C5 = 0.13
        self.C5C2 = 3.6
        self.O1C3 = 3400.0
        self.C3O1 = 1100.0
        self.O2C3 = 92.0
        self.C3O2 = 17.0
        self.O3C3 = 138.0
        self.C3O3 = 14.0
        self.O2C4 = 1900.0
        self.C4O2 = 520.0
        self.O3C4 = 300.0
        self.C4O3 = 46.0

    def to_dict(self):
        return {
            "C1C2": self.C1C2,
            "C2C1": self.C2C1,
            "Ca": self.Ca,
            "C2C3": self.C2C3,
            "C3C2": self.C3C2,
            "C2C5": self.C2C5,
            "C5C2": self.C5C2,
            "O1C3": self.O1C3,
            "C3O1": self.C3O1,
            "O2C3": self.O2C3,
            "C3O2": self.C3O2,
            "O3C3": self.O3C3,
            "C3O3": self.C3O3,
            "O2C4": self.O2C4,
            "C4O2": self.C4O2,
            "O3C4": self.O3C4,
            "C4O3": self.C4O3,
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
        y0=[0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "saftenku_williams_sitsapesan_2001_low_model"
        self.curve_names = [
            "C1",
            "C2",
            "C3",
            "C5",
            "O1",
            "O2",
            "O3",
            "C4",
        ]
        self.state_names = ['C1', 'C2', 'C3', 'C5', 'O1', 'O2', 'O3', 'C4']
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
        c = [0.0] * 17
        p = self.params

        # direct mapping
        c[0] = p.C1C2
        c[1] = p.C2C1
        c[2] = p.Ca
        c[3] = p.C2C3
        c[4] = p.C3C2
        c[5] = p.C2C5
        c[6] = p.C5C2
        c[7] = p.O1C3
        c[8] = p.C3O1
        c[9] = p.O2C3
        c[10] = p.C3O2
        c[11] = p.O3C3
        c[12] = p.C3O3
        c[13] = p.O2C4
        c[14] = p.C4O2
        c[15] = p.O3C4
        c[16] = p.C4O3

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
