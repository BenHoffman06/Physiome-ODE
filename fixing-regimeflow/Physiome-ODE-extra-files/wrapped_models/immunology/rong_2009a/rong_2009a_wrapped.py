# Size of variable arrays:
sizeAlgebraic = 0
sizeStates = 4
sizeConstants = 10
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (day)"
    legend_constants[0] = "lambda in component uninfected (per_ml_day)"
    legend_constants[1] = "d_T in component uninfected (per_day)"
    legend_constants[2] = "efficacy in component drug_efficacy (dimensionless)"
    legend_constants[3] = "k in component uninfected (ml_per_day)"
    legend_states[0] = "V in component viral_load (per_ml)"
    legend_states[1] = "T in component uninfected (per_ml)"
    legend_constants[4] = "d_0 in component latently_infected (per_day)"
    legend_constants[5] = "a_L in component latently_infected (per_day)"
    legend_constants[6] = "eta in component latently_infected (dimensionless)"
    legend_states[2] = "L in component latently_infected (per_ml)"
    legend_constants[7] = "delta in component productively_infected (per_day)"
    legend_states[3] = "T_star in component productively_infected (per_ml)"
    legend_constants[8] = "N in component viral_load (dimensionless)"
    legend_constants[9] = "c in component viral_load (per_day)"
    legend_rates[1] = "d/dt T in component uninfected (per_ml)"
    legend_rates[2] = "d/dt L in component latently_infected (per_ml)"
    legend_rates[3] = "d/dt T_star in component productively_infected (per_ml)"
    legend_rates[0] = "d/dt V in component viral_load (per_ml)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    constants[0] = 1E4
    constants[1] = 0.01
    constants[2] = 0.4
    constants[3] = 2.4E-8
    states[0] = 50
    states[1] = 600000
    constants[4] = 0.001
    constants[5] = 0.1
    constants[6] = 0.001
    states[2] = 2
    constants[7] = 1
    states[3] = 0.3
    constants[8] = 2000
    constants[9] = 23
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[1] = (constants[0]-constants[1]*states[1])-(1.00000-constants[2])*constants[3]*states[0]*states[1]
    rates[2] = (constants[6]*(1.00000-constants[2])*constants[3]*states[0]*states[1]-constants[4]*states[2])-constants[5]*states[2]
    rates[3] = ((1.00000-constants[6])*(1.00000-constants[2])*constants[3]*states[0]*states[1]-constants[7]*states[3])+constants[5]*states[2]
    rates[0] = constants[8]*constants[7]*states[3]-constants[9]*states[0]
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
        self.lambda = 1E4
        self.d_T = 0.01
        self.efficacy = 0.4
        self.k = 2.4E-8
        self.d_0 = 0.001
        self.a_L = 0.1
        self.eta = 0.001
        self.delta = 1
        self.N = 2000
        self.c = 23

    def to_dict(self):
        return {
            "lambda": self.lambda,
            "d_T": self.d_T,
            "efficacy": self.efficacy,
            "k": self.k,
            "d_0": self.d_0,
            "a_L": self.a_L,
            "eta": self.eta,
            "delta": self.delta,
            "N": self.N,
            "c": self.c,
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
        y0=[50, 600000, 2, 0.3],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "rong_2009a"
        self.curve_names = [
            "V",
            "T",
            "L",
            "T_star",
        ]
        self.state_names = ['V', 'T', 'L', 'T_star']
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
        c = [0.0] * 10
        p = self.params

        # direct mapping
        c[0] = p.lambda
        c[1] = p.d_T
        c[2] = p.efficacy
        c[3] = p.k
        c[4] = p.d_0
        c[5] = p.a_L
        c[6] = p.eta
        c[7] = p.delta
        c[8] = p.N
        c[9] = p.c

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
