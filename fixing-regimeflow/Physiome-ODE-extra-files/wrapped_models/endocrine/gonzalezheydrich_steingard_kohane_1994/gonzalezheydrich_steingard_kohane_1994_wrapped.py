# Size of variable arrays:
sizeAlgebraic = 0
sizeStates = 3
sizeConstants = 11
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (minute)"
    legend_states[0] = "cortisol in component cortisol (mcg_ml)"
    legend_constants[0] = "k1 in component cortisol (first_order_rate_constant)"
    legend_constants[1] = "k2 in component cortisol (flux)"
    legend_constants[2] = "k3 in component cortisol (first_order_rate_constant)"
    legend_states[1] = "ACTH in component ACTH (mcg_ml)"
    legend_constants[3] = "k4 in component ACTH (first_order_rate_constant)"
    legend_constants[4] = "k5 in component ACTH (flux)"
    legend_constants[5] = "k6 in component ACTH (first_order_rate_constant)"
    legend_constants[6] = "Kd in component ACTH (mcg_ml)"
    legend_constants[7] = "Imax in component ACTH (dimensionless)"
    legend_states[2] = "CRH in component CRH (mcg_ml)"
    legend_constants[8] = "k7 in component CRH (flux)"
    legend_constants[9] = "k8 in component CRH (first_order_rate_constant)"
    legend_constants[10] = "pulse in component CRH (flux)"
    legend_rates[0] = "d/dt cortisol in component cortisol (mcg_ml)"
    legend_rates[1] = "d/dt ACTH in component ACTH (mcg_ml)"
    legend_rates[2] = "d/dt CRH in component CRH (mcg_ml)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 0.0
    constants[0] = 5E5
    constants[1] = 0.01
    constants[2] = 0.01
    states[1] = 0.0
    constants[3] = 10.0
    constants[4] = 4E-3
    constants[5] = 0.035
    constants[6] = 0.004
    constants[7] = 0.99
    states[2] = 50.0
    constants[8] = 1E-6
    constants[9] = 0.01
    constants[10] = 50.0
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[0] = (constants[0]*states[1]+constants[1])-constants[2]*states[0]
    rates[1] = (constants[3]*states[2]+constants[4])-(constants[5]*states[1]+(constants[3]*states[2]+constants[4])*((constants[7]*states[0])/(constants[6]+states[0])))
    rates[2] = (constants[10]+constants[8])-constants[9]*states[2]
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
        self.k1 = 5E5
        self.k2 = 0.01
        self.k3 = 0.01
        self.k4 = 10.0
        self.k5 = 4E-3
        self.k6 = 0.035
        self.Kd = 0.004
        self.Imax = 0.99
        self.k7 = 1E-6
        self.k8 = 0.01
        self.pulse = 50.0

    def to_dict(self):
        return {
            "k1": self.k1,
            "k2": self.k2,
            "k3": self.k3,
            "k4": self.k4,
            "k5": self.k5,
            "k6": self.k6,
            "Kd": self.Kd,
            "Imax": self.Imax,
            "k7": self.k7,
            "k8": self.k8,
            "pulse": self.pulse,
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
        y0=[0.0, 0.0, 50.0],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "gonzalezheydrich_steingard_kohane_1994"
        self.curve_names = [
            "cortisol",
            "ACTH",
            "CRH",
        ]
        self.state_names = ['cortisol', 'ACTH', 'CRH']
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
        c = [0.0] * 11
        p = self.params

        # direct mapping
        c[0] = p.k1
        c[1] = p.k2
        c[2] = p.k3
        c[3] = p.k4
        c[4] = p.k5
        c[5] = p.k6
        c[6] = p.Kd
        c[7] = p.Imax
        c[8] = p.k7
        c[9] = p.k8
        c[10] = p.pulse

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
