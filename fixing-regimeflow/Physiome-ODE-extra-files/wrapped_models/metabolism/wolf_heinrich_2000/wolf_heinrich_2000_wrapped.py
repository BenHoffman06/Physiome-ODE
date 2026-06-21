# Size of variable arrays:
sizeAlgebraic = 11
sizeStates = 7
sizeConstants = 14
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (minute)"
    legend_states[0] = "S1 in component S1 (millimolar)"
    legend_constants[0] = "Jo in component glucose_influx_rate (flux)"
    legend_algebraic[3] = "v1 in component v1 (flux)"
    legend_states[1] = "S2 in component S2 (millimolar)"
    legend_algebraic[4] = "v2 in component v2 (flux)"
    legend_algebraic[8] = "v6 in component v6 (flux)"
    legend_states[2] = "S3 in component S3 (millimolar)"
    legend_algebraic[5] = "v3 in component v3 (flux)"
    legend_states[3] = "S4 in component S4 (millimolar)"
    legend_algebraic[6] = "v4 in component v4 (flux)"
    legend_algebraic[10] = "J in component S4_flux_rate_across_the_plasma_membrane (flux)"
    legend_states[4] = "S4_ex in component S4_ex (millimolar)"
    legend_constants[1] = "phi in component S4_ex (dimensionless)"
    legend_algebraic[9] = "v7 in component v7 (flux)"
    legend_states[5] = "A3 in component A3 (millimolar)"
    legend_algebraic[7] = "v5 in component v5 (flux)"
    legend_constants[2] = "A in component A2 (millimolar)"
    legend_algebraic[0] = "A2 in component A2 (millimolar)"
    legend_states[6] = "N2 in component N2 (millimolar)"
    legend_constants[3] = "N in component N1 (millimolar)"
    legend_algebraic[1] = "N1 in component N1 (millimolar)"
    legend_constants[4] = "K_I in component v1 (millimolar)"
    legend_constants[5] = "k_1 in component v1 (second_order_rate_constant)"
    legend_constants[6] = "q in component v1 (dimensionless)"
    legend_algebraic[2] = "f_A3 in component v1 (dimensionless)"
    legend_constants[7] = "k_2 in component v2 (second_order_rate_constant)"
    legend_constants[8] = "k_3 in component v3 (second_order_rate_constant)"
    legend_constants[9] = "k_4 in component v4 (second_order_rate_constant)"
    legend_constants[10] = "k_5 in component v5 (first_order_rate_constant)"
    legend_constants[11] = "k_6 in component v6 (second_order_rate_constant)"
    legend_constants[12] = "k in component v7 (first_order_rate_constant)"
    legend_constants[13] = "kappa in component S4_flux_rate_across_the_plasma_membrane (first_order_rate_constant)"
    legend_rates[0] = "d/dt S1 in component S1 (millimolar)"
    legend_rates[1] = "d/dt S2 in component S2 (millimolar)"
    legend_rates[2] = "d/dt S3 in component S3 (millimolar)"
    legend_rates[3] = "d/dt S4 in component S4 (millimolar)"
    legend_rates[4] = "d/dt S4_ex in component S4_ex (millimolar)"
    legend_rates[5] = "d/dt A3 in component A3 (millimolar)"
    legend_rates[6] = "d/dt N2 in component N2 (millimolar)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 5.8
    constants[0] = 3.0
    states[1] = 0.9
    states[2] = 0.2
    states[3] = 0.2
    states[4] = 0.1
    constants[1] = 0.1
    states[5] = 2.4
    constants[2] = 4.0
    states[6] = 0.1
    constants[3] = 1.0
    constants[4] = 0.52
    constants[5] = 100.0
    constants[6] = 4.0
    constants[7] = 6.0
    constants[8] = 16.0
    constants[9] = 100.0
    constants[10] = 1.28
    constants[11] = 12.0
    constants[12] = 1.3
    constants[13] = 13.0
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[2] = power(1.00000+power(states[5]/constants[4], constants[6]), -1.00000)
    algebraic[3] = constants[5]*states[0]*states[5]*algebraic[2]
    rates[0] = constants[0]-algebraic[3]
    algebraic[1] = constants[3]-states[6]
    algebraic[4] = constants[7]*states[1]*algebraic[1]
    algebraic[0] = constants[2]-states[5]
    algebraic[5] = constants[8]*states[2]*algebraic[0]
    rates[2] = algebraic[4]-algebraic[5]
    algebraic[7] = constants[10]*states[5]
    rates[5] = 2.00000*algebraic[5]-(2.00000*algebraic[3]+algebraic[7])
    algebraic[8] = constants[11]*states[1]*states[6]
    rates[1] = 2.00000*algebraic[3]-(algebraic[4]+algebraic[8])
    algebraic[6] = constants[9]*states[3]*states[6]
    rates[6] = algebraic[4]-(algebraic[6]+algebraic[8])
    algebraic[10] = constants[13]*(states[3]-states[4])
    rates[3] = algebraic[5]-(algebraic[6]+algebraic[10])
    algebraic[9] = constants[12]*states[4]
    rates[4] = constants[1]*algebraic[10]-algebraic[9]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[2] = power(1.00000+power(states[5]/constants[4], constants[6]), -1.00000)
    algebraic[3] = constants[5]*states[0]*states[5]*algebraic[2]
    algebraic[1] = constants[3]-states[6]
    algebraic[4] = constants[7]*states[1]*algebraic[1]
    algebraic[0] = constants[2]-states[5]
    algebraic[5] = constants[8]*states[2]*algebraic[0]
    algebraic[7] = constants[10]*states[5]
    algebraic[8] = constants[11]*states[1]*states[6]
    algebraic[6] = constants[9]*states[3]*states[6]
    algebraic[10] = constants[13]*(states[3]-states[4])
    algebraic[9] = constants[12]*states[4]
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
        self.Jo = 3.0
        self.phi = 0.1
        self.A = 4.0
        self.N = 1.0
        self.K_I = 0.52
        self.k_1 = 100.0
        self.q = 4.0
        self.k_2 = 6.0
        self.k_3 = 16.0
        self.k_4 = 100.0
        self.k_5 = 1.28
        self.k_6 = 12.0
        self.k = 1.3
        self.kappa = 13.0

    def to_dict(self):
        return {
            "Jo": self.Jo,
            "phi": self.phi,
            "A": self.A,
            "N": self.N,
            "K_I": self.K_I,
            "k_1": self.k_1,
            "q": self.q,
            "k_2": self.k_2,
            "k_3": self.k_3,
            "k_4": self.k_4,
            "k_5": self.k_5,
            "k_6": self.k_6,
            "k": self.k,
            "kappa": self.kappa,
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
        y0=[5.8, 0.9, 0.2, 0.2, 0.1, 2.4, 0.1],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "wolf_heinrich_2000"
        self.curve_names = [
            "S1",
            "S2",
            "S3",
            "S4",
            "S4_ex",
            "A3",
            "N2",
        ]
        self.state_names = ['S1', 'S2', 'S3', 'S4', 'S4_ex', 'A3', 'N2']
        self.algebraic_names = ['A2', 'N1', 'f_A3', 'v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'J']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 14
        p = self.params

        # direct mapping
        c[0] = p.Jo
        c[1] = p.phi
        c[2] = p.A
        c[3] = p.N
        c[4] = p.K_I
        c[5] = p.k_1
        c[6] = p.q
        c[7] = p.k_2
        c[8] = p.k_3
        c[9] = p.k_4
        c[10] = p.k_5
        c[11] = p.k_6
        c[12] = p.k
        c[13] = p.kappa

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
