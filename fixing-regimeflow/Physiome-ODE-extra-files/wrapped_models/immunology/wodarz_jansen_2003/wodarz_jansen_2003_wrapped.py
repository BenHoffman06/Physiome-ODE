# Size of variable arrays:
sizeAlgebraic = 1
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
    legend_voi = "time in component environment (day)"
    legend_states[0] = "T in component T (dimensionless)"
    legend_constants[0] = "k in component T (first_order_rate_constant)"
    legend_constants[1] = "r in component T (first_order_rate_constant)"
    legend_constants[2] = "d in component T (first_order_rate_constant)"
    legend_constants[3] = "gamma in component T (first_order_rate_constant)"
    legend_states[1] = "C in component C (dimensionless)"
    legend_states[2] = "A in component A (dimensionless)"
    legend_constants[4] = "lambda in component A (first_order_rate_constant)"
    legend_constants[5] = "delta_1 in component A (first_order_rate_constant)"
    legend_constants[6] = "alpha in component kinetic_parameters (first_order_rate_constant)"
    legend_states[3] = "A_star in component A_star (dimensionless)"
    legend_constants[7] = "delta_2 in component A_star (first_order_rate_constant)"
    legend_constants[8] = "eta in component C (first_order_rate_constant)"
    legend_constants[9] = "epsilon in component C (dimensionless)"
    legend_constants[10] = "q in component C (first_order_rate_constant)"
    legend_constants[11] = "mu in component C (first_order_rate_constant)"
    legend_algebraic[0] = "R in component ratio (dimensionless)"
    legend_rates[0] = "d/dt T in component T (dimensionless)"
    legend_rates[2] = "d/dt A in component A (dimensionless)"
    legend_rates[3] = "d/dt A_star in component A_star (dimensionless)"
    legend_rates[1] = "d/dt C in component C (dimensionless)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 0.1
    constants[0] = 10
    constants[1] = 0.5
    constants[2] = 0.1
    constants[3] = 1
    states[1] = 0.015
    states[2] = 1
    constants[4] = 1
    constants[5] = 0.1
    constants[6] = 0.05
    states[3] = 2
    constants[7] = 1.5
    constants[8] = 2
    constants[9] = 1
    constants[10] = 0.5
    constants[11] = 0.1
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[0] = (constants[1]*states[0]*(1.00000-(states[0]*1.00000)/constants[0])-constants[2]*states[0])-constants[3]*states[0]*states[1]
    rates[2] = (constants[4]-constants[5]*states[2])-constants[6]*states[2]*states[0]
    rates[3] = constants[6]*states[2]*states[0]-constants[7]*states[3]
    rates[1] = ((constants[8]*states[3]*states[1])/(constants[9]*states[1]+1.00000)-constants[10]*states[0]*states[1])-constants[11]*states[1]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = (states[1]*states[3])/(constants[10]*1.00000*states[0])
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
        self.k = 10
        self.r = 0.5
        self.d = 0.1
        self.gamma = 1
        self.lambda = 1
        self.delta_1 = 0.1
        self.alpha = 0.05
        self.delta_2 = 1.5
        self.eta = 2
        self.epsilon = 1
        self.q = 0.5
        self.mu = 0.1

    def to_dict(self):
        return {
            "k": self.k,
            "r": self.r,
            "d": self.d,
            "gamma": self.gamma,
            "lambda": self.lambda,
            "delta_1": self.delta_1,
            "alpha": self.alpha,
            "delta_2": self.delta_2,
            "eta": self.eta,
            "epsilon": self.epsilon,
            "q": self.q,
            "mu": self.mu,
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
        y0=[0.1, 0.015, 1, 2],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "wodarz_jansen_2003"
        self.curve_names = [
            "T",
            "C",
            "A",
            "A_star",
        ]
        self.state_names = ['T', 'C', 'A', 'A_star']
        self.algebraic_names = ['R']
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
        c[0] = p.k
        c[1] = p.r
        c[2] = p.d
        c[3] = p.gamma
        c[4] = p.lambda
        c[5] = p.delta_1
        c[6] = p.alpha
        c[7] = p.delta_2
        c[8] = p.eta
        c[9] = p.epsilon
        c[10] = p.q
        c[11] = p.mu

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
