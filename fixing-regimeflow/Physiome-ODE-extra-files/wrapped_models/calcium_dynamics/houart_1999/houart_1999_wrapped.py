# Size of variable arrays:
sizeAlgebraic = 3
sizeStates = 3
sizeConstants = 20
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (minute)"
    legend_constants[0] = "V_0 in component Vin (micromolar_per_minute)"
    legend_constants[1] = "V_1 in component Vin (micromolar_per_minute)"
    legend_constants[2] = "beta in component Vin (dimensionless)"
    legend_constants[19] = "V_in in component Vin (micromolar_per_minute)"
    legend_constants[3] = "V_M2 in component V2 (micromolar_per_minute)"
    legend_states[0] = "Z in component cytosol (micromolar)"
    legend_constants[4] = "K_2 in component V2 (micromolar)"
    legend_algebraic[0] = "V_2 in component V2 (micromolar_per_minute)"
    legend_constants[5] = "V_M3 in component V3 (micromolar_per_minute)"
    legend_constants[6] = "K_Z in component V3 (micromolar)"
    legend_constants[7] = "K_A in component V3 (micromolar)"
    legend_constants[8] = "K_Y in component V3 (micromolar)"
    legend_constants[9] = "m in component V3 (dimensionless)"
    legend_states[1] = "Y in component internal_pool (micromolar)"
    legend_states[2] = "A in component InsP3_conc (micromolar)"
    legend_algebraic[2] = "V_3 in component V3 (micromolar_per_minute)"
    legend_constants[10] = "V_M5 in component V5 (micromolar_per_minute)"
    legend_constants[11] = "K_5 in component V5 (micromolar)"
    legend_constants[12] = "K_d in component V5 (micromolar)"
    legend_constants[13] = "p in component V5 (dimensionless)"
    legend_constants[14] = "n in component V5 (dimensionless)"
    legend_algebraic[1] = "V_5 in component V5 (micromolar_per_minute)"
    legend_constants[15] = "k in component cytosol (per_minute)"
    legend_constants[16] = "k_f in component cytosol (per_minute)"
    legend_constants[17] = "epsilon in component InsP3_conc (per_minute)"
    legend_constants[18] = "V_4 in component InsP3_conc (micromolar_per_minute)"
    legend_rates[0] = "d/dt Z in component cytosol (micromolar)"
    legend_rates[1] = "d/dt Y in component internal_pool (micromolar)"
    legend_rates[2] = "d/dt A in component InsP3_conc (micromolar)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    constants[0] = 2
    constants[1] = 2
    constants[2] = 0.6
    constants[3] = 6
    states[0] = 0.15
    constants[4] = 0.1
    constants[5] = 20
    constants[6] = 0.5
    constants[7] = 0.2
    constants[8] = 0.2
    constants[9] = 2
    states[1] = 1
    states[2] = 0.42
    constants[10] = 5
    constants[11] = 1
    constants[12] = 0.4
    constants[13] = 2
    constants[14] = 4
    constants[15] = 10
    constants[16] = 1
    constants[17] = 0.1
    constants[18] = 2
    constants[19] = constants[0]+constants[1]*constants[2]
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[1] = (((constants[10]*(power(states[2], constants[13])))/(power(constants[11], constants[13])+power(states[2], constants[13])))*(power(states[0], constants[14])))/(power(constants[12], constants[14])+power(states[0], constants[14]))
    rates[2] = (constants[2]*constants[18]-algebraic[1])-constants[17]*states[2]
    algebraic[0] = (constants[3]*(power(states[0], 2.00000)))/(power(constants[4], 2.00000)+power(states[0], 2.00000))
    algebraic[2] = (((((constants[5]*(power(states[0], constants[9])))/(power(constants[6], constants[9])+power(states[0], constants[9])))*(power(states[1], 2.00000)))/(power(constants[8], 2.00000)+power(states[1], 2.00000)))*(power(states[2], 4.00000)))/(power(constants[7], 4.00000)+power(states[2], 4.00000))
    rates[0] = ((constants[19]-algebraic[0])+algebraic[2]+constants[16]*states[1])-constants[15]*states[0]
    rates[1] = (algebraic[0]-algebraic[2])-constants[16]*states[1]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[1] = (((constants[10]*(power(states[2], constants[13])))/(power(constants[11], constants[13])+power(states[2], constants[13])))*(power(states[0], constants[14])))/(power(constants[12], constants[14])+power(states[0], constants[14]))
    algebraic[0] = (constants[3]*(power(states[0], 2.00000)))/(power(constants[4], 2.00000)+power(states[0], 2.00000))
    algebraic[2] = (((((constants[5]*(power(states[0], constants[9])))/(power(constants[6], constants[9])+power(states[0], constants[9])))*(power(states[1], 2.00000)))/(power(constants[8], 2.00000)+power(states[1], 2.00000)))*(power(states[2], 4.00000)))/(power(constants[7], 4.00000)+power(states[2], 4.00000))
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
        self.V_0 = 2
        self.V_1 = 2
        self.beta = 0.6
        self.V_M2 = 6
        self.K_2 = 0.1
        self.V_M3 = 20
        self.K_Z = 0.5
        self.K_A = 0.2
        self.K_Y = 0.2
        self.m = 2
        self.V_M5 = 5
        self.K_5 = 1
        self.K_d = 0.4
        self.p = 2
        self.n = 4
        self.k = 10
        self.k_f = 1
        self.epsilon = 0.1
        self.V_4 = 2

    def to_dict(self):
        return {
            "V_0": self.V_0,
            "V_1": self.V_1,
            "beta": self.beta,
            "V_M2": self.V_M2,
            "K_2": self.K_2,
            "V_M3": self.V_M3,
            "K_Z": self.K_Z,
            "K_A": self.K_A,
            "K_Y": self.K_Y,
            "m": self.m,
            "V_M5": self.V_M5,
            "K_5": self.K_5,
            "K_d": self.K_d,
            "p": self.p,
            "n": self.n,
            "k": self.k,
            "k_f": self.k_f,
            "epsilon": self.epsilon,
            "V_4": self.V_4,
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
        y0=[0.15, 1, 0.42],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "houart_1999"
        self.curve_names = [
            "Z",
            "Y",
            "A",
        ]
        self.state_names = ['Z', 'Y', 'A']
        self.algebraic_names = ['V_2', 'V_5', 'V_3']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 20
        p = self.params

        # direct mapping
        c[0] = p.V_0
        c[1] = p.V_1
        c[2] = p.beta
        c[3] = p.V_M2
        c[4] = p.K_2
        c[5] = p.V_M3
        c[6] = p.K_Z
        c[7] = p.K_A
        c[8] = p.K_Y
        c[9] = p.m
        c[10] = p.V_M5
        c[11] = p.K_5
        c[12] = p.K_d
        c[13] = p.p
        c[14] = p.n
        c[15] = p.k
        c[16] = p.k_f
        c[17] = p.epsilon
        c[18] = p.V_4

        # derived constants
        c[19] = c[0]+c[1]*c[2]

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
