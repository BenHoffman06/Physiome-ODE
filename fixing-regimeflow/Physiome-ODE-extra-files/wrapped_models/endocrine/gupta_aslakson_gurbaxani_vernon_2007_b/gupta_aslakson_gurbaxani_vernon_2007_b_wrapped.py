# Size of variable arrays:
sizeAlgebraic = 1
sizeStates = 4
sizeConstants = 7
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (hour)"
    legend_states[0] = "c in component c (dimensionless)"
    legend_algebraic[0] = "f in component c (dimensionless)"
    legend_constants[0] = "kcd in component reaction_constants (first_order_rate_constant)"
    legend_constants[1] = "ki1 in component reaction_constants (dimensionless)"
    legend_states[1] = "o in component o (dimensionless)"
    legend_states[2] = "a in component a (dimensionless)"
    legend_constants[2] = "kad in component reaction_constants (first_order_rate_constant)"
    legend_constants[3] = "ki2 in component reaction_constants (first_order_rate_constant)"
    legend_states[3] = "r in component r (dimensionless)"
    legend_constants[4] = "kcr in component reaction_constants (first_order_rate_constant)"
    legend_constants[5] = "krd in component reaction_constants (first_order_rate_constant)"
    legend_constants[6] = "k in component reaction_constants (dimensionless)"
    legend_rates[0] = "d/dt c in component c (dimensionless)"
    legend_rates[2] = "d/dt a in component a (dimensionless)"
    legend_rates[3] = "d/dt r in component r (dimensionless)"
    legend_rates[1] = "d/dt o in component o (dimensionless)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 0.6
    constants[0] = 1.0
    constants[1] = 0.1
    states[1] = 0.055
    states[2] = 0.055
    constants[2] = 10.0
    constants[3] = 0.1
    states[3] = 0.01
    constants[4] = 0.05
    constants[5] = 0.9
    constants[6] = 0.001
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[2] = states[0]/(1.00000+(states[1]*states[3])/constants[3])-constants[2]*states[2]
    rates[3] = ((power(states[1]*states[3], 2.00000))/(1.00000*(constants[6]+power(states[1]*states[3], 2.00000)))+constants[4])-constants[5]*states[3]
    rates[1] = 1.00000*(states[2]-states[1])
    algebraic[0] = custom_piecewise([greater(voi , 0.00000) & less(voi , 1.00000) | greater(voi , 4.00000) & less(voi , 5.00000) | greater(voi , 8.00000) & less(voi , 9.00000) | greater(voi , 12.0000) & less(voi , 13.0000) | greater(voi , 16.0000) & less(voi , 17.0000), 1.00000 , True, 0.00000])
    rates[0] = 1.00000*((1.00000+algebraic[0])/(1.00000+states[1]/constants[1]))-constants[0]*states[0]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = custom_piecewise([greater(voi , 0.00000) & less(voi , 1.00000) | greater(voi , 4.00000) & less(voi , 5.00000) | greater(voi , 8.00000) & less(voi , 9.00000) | greater(voi , 12.0000) & less(voi , 13.0000) | greater(voi , 16.0000) & less(voi , 17.0000), 1.00000 , True, 0.00000])
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
        self.kcd = 1.0
        self.ki1 = 0.1
        self.kad = 10.0
        self.ki2 = 0.1
        self.kcr = 0.05
        self.krd = 0.9
        self.k = 0.001

    def to_dict(self):
        return {
            "kcd": self.kcd,
            "ki1": self.ki1,
            "kad": self.kad,
            "ki2": self.ki2,
            "kcr": self.kcr,
            "krd": self.krd,
            "k": self.k,
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
        y0=[0.6, 0.055, 0.055, 0.01],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "gupta_aslakson_gurbaxani_vernon_2007_b"
        self.curve_names = [
            "c",
            "o",
            "a",
            "r",
        ]
        self.state_names = ['c', 'o', 'a', 'r']
        self.algebraic_names = ['f']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 7
        p = self.params

        # direct mapping
        c[0] = p.kcd
        c[1] = p.ki1
        c[2] = p.kad
        c[3] = p.ki2
        c[4] = p.kcr
        c[5] = p.krd
        c[6] = p.k

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
