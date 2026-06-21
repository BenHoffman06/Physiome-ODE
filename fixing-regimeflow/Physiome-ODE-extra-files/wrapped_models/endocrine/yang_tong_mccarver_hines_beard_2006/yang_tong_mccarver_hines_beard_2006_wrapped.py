# Size of variable arrays:
sizeAlgebraic = 4
sizeStates = 2
sizeConstants = 13
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (minute)"
    legend_algebraic[0] = "B in component B (micromolar)"
    legend_constants[0] = "F in component B (micromolar)"
    legend_constants[1] = "n2 in component B (dimensionless)"
    legend_constants[2] = "K2 in component B (per_micromolar)"
    legend_states[0] = "Ca in component Ca (micromolar)"
    legend_algebraic[3] = "R in component R (flux)"
    legend_constants[3] = "Vmax in component R (flux)"
    legend_constants[4] = "Km in component R (micromolar)"
    legend_algebraic[2] = "fu in component R (dimensionless)"
    legend_constants[12] = "ISF in component R (dimensionless)"
    legend_constants[5] = "age in component R (dimensionless)"
    legend_states[1] = "C in component C (micromolar)"
    legend_constants[6] = "Va in component Ca (ml)"
    legend_constants[7] = "Vv in component Ca (ml)"
    legend_constants[8] = "Qc in component model_constants (flow)"
    legend_algebraic[1] = "Cv in component Cv (micromolar)"
    legend_constants[9] = "Q in component model_constants (flow)"
    legend_constants[10] = "P in component model_constants (dimensionless)"
    legend_constants[11] = "V in component C (ml)"
    legend_rates[0] = "d/dt Ca in component Ca (micromolar)"
    legend_rates[1] = "d/dt C in component C (micromolar)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    constants[0] = 0.48
    constants[1] = 1
    constants[2] = 0.8532
    states[0] = 6.6685
    constants[3] = 9.433e-3
    constants[4] = 198
    constants[5] = 5
    states[1] = 0
    constants[6] = 2148
    constants[7] = 3431
    constants[8] = 6445.65
    constants[9] = 1221.34
    constants[10] = 15.61
    constants[11] = 1454
    constants[12] = -8.32120+2.04010*constants[5]+4.19620*log(constants[5]*365.000, 10)
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[1] = ((constants[9]*states[1])/constants[10])/constants[8]
    rates[0] = (constants[8]*(algebraic[1]-states[0]))/(constants[6]+constants[7])
    algebraic[0] = (constants[0]*constants[1]*constants[2]*states[0])/(1.00000+constants[2]*constants[0])
    algebraic[2] = constants[0]/(constants[0]+algebraic[0])
    algebraic[3] = (constants[12]*constants[3]*algebraic[2]*states[1])/(constants[4]+algebraic[2]*states[1])
    rates[1] = (constants[9]*(states[0]-states[1]/constants[10])-algebraic[3]*1.00000)/constants[11]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[1] = ((constants[9]*states[1])/constants[10])/constants[8]
    algebraic[0] = (constants[0]*constants[1]*constants[2]*states[0])/(1.00000+constants[2]*constants[0])
    algebraic[2] = constants[0]/(constants[0]+algebraic[0])
    algebraic[3] = (constants[12]*constants[3]*algebraic[2]*states[1])/(constants[4]+algebraic[2]*states[1])
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
        self.F = 0.48
        self.n2 = 1
        self.K2 = 0.8532
        self.Vmax = 9.433e-3
        self.Km = 198
        self.age = 5
        self.Va = 2148
        self.Vv = 3431
        self.Qc = 6445.65
        self.Q = 1221.34
        self.P = 15.61
        self.V = 1454

    def to_dict(self):
        return {
            "F": self.F,
            "n2": self.n2,
            "K2": self.K2,
            "Vmax": self.Vmax,
            "Km": self.Km,
            "age": self.age,
            "Va": self.Va,
            "Vv": self.Vv,
            "Qc": self.Qc,
            "Q": self.Q,
            "P": self.P,
            "V": self.V,
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
        y0=[6.6685, 0],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "yang_tong_mccarver_hines_beard_2006"
        self.curve_names = [
            "Ca",
            "C",
        ]
        self.state_names = ['Ca', 'C']
        self.algebraic_names = ['B', 'Cv', 'fu', 'R']
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
        c[0] = p.F
        c[1] = p.n2
        c[2] = p.K2
        c[3] = p.Vmax
        c[4] = p.Km
        c[5] = p.age
        c[6] = p.Va
        c[7] = p.Vv
        c[8] = p.Qc
        c[9] = p.Q
        c[10] = p.P
        c[11] = p.V

        # derived constants
        c[12] = -8.32120+2.04010*c[5]+4.19620*log(c[5]*365.000, 10)

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
