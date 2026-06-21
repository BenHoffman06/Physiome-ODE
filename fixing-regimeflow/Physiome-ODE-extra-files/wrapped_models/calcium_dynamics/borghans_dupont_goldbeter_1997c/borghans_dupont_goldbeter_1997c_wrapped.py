# Size of variable arrays:
sizeAlgebraic = 4
sizeStates = 3
sizeConstants = 15
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (min)"
    legend_states[0] = "Z in component Ca (uM)"
    legend_states[1] = "Y in component Ca (uM)"
    legend_states[2] = "X in component Ca (uM)"
    legend_constants[14] = "V_in in component V_in (uM_per_min)"
    legend_algebraic[0] = "V_2i in component V_2i (uM_per_min)"
    legend_algebraic[1] = "V_3i in component V_3i (uM_per_min)"
    legend_algebraic[2] = "V_2s in component V_2s (uM_per_min)"
    legend_algebraic[3] = "V_3s in component V_3s (uM_per_min)"
    legend_constants[0] = "K_f in component Ca (per_min)"
    legend_constants[1] = "K in component Ca (per_min)"
    legend_constants[2] = "beta in component Ca_flux (dimensionless)"
    legend_constants[3] = "v_0 in component V_in (uM_per_min)"
    legend_constants[4] = "v_1 in component V_in (uM_per_min)"
    legend_constants[5] = "V_M2i in component V_2i (uM_per_min)"
    legend_constants[6] = "K_2i in component V_2i (uM)"
    legend_constants[7] = "V_M3i in component V_3i (uM_per_min)"
    legend_constants[8] = "K_3z in component V_3i (uM)"
    legend_constants[9] = "K_3y in component V_3i (uM)"
    legend_constants[10] = "V_M2s in component V_2s (uM_per_min)"
    legend_constants[11] = "K_2s in component V_2s (uM)"
    legend_constants[12] = "V_M3s in component V_3s (uM_per_min)"
    legend_constants[13] = "K_3s in component V_3s (uM)"
    legend_rates[0] = "d/dt Z in component Ca (uM)"
    legend_rates[1] = "d/dt Y in component Ca (uM)"
    legend_rates[2] = "d/dt X in component Ca (uM)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 0.0
    states[1] = 0.0
    states[2] = 0.5
    constants[0] = 0.5
    constants[1] = 1
    constants[2] = 1
    constants[3] = 0.015
    constants[4] = 0.012
    constants[5] = 3.1
    constants[6] = 0.005
    constants[7] = 25
    constants[8] = 0.022
    constants[9] = 0.065
    constants[10] = 1.5
    constants[11] = 0.0265
    constants[12] = 0.169
    constants[13] = 0.1
    constants[14] = constants[3]+constants[4]*constants[2]
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[0] = constants[5]*((power(states[0], 2.00000))/(power(constants[6], 2.00000)+power(states[0], 2.00000)))
    algebraic[1] = constants[7]*((power(states[1], 2.00000))/(power(constants[9], 2.00000)+power(states[1], 2.00000)))*((power(states[0], 2.00000))/(power(constants[8], 2.00000)+power(states[0], 2.00000)))
    rates[1] = algebraic[0]+-algebraic[1]+-(constants[0]*states[1])
    algebraic[2] = constants[10]*((power(states[0], 2.00000))/(power(constants[11], 2.00000)+power(states[0], 2.00000)))
    algebraic[3] = constants[2]*constants[12]*((power(states[2], 2.00000))/(power(constants[13], 2.00000)+power(states[2], 2.00000)))
    rates[0] = constants[14]+-algebraic[0]+algebraic[1]+constants[0]*states[1]+-algebraic[2]+algebraic[3]+constants[0]*states[2]+-(constants[1]*states[0])
    rates[2] = algebraic[2]+-algebraic[3]+-(constants[0]*states[2])
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = constants[5]*((power(states[0], 2.00000))/(power(constants[6], 2.00000)+power(states[0], 2.00000)))
    algebraic[1] = constants[7]*((power(states[1], 2.00000))/(power(constants[9], 2.00000)+power(states[1], 2.00000)))*((power(states[0], 2.00000))/(power(constants[8], 2.00000)+power(states[0], 2.00000)))
    algebraic[2] = constants[10]*((power(states[0], 2.00000))/(power(constants[11], 2.00000)+power(states[0], 2.00000)))
    algebraic[3] = constants[2]*constants[12]*((power(states[2], 2.00000))/(power(constants[13], 2.00000)+power(states[2], 2.00000)))
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
        self.K_f = 0.5
        self.K = 1
        self.beta = 1
        self.v_0 = 0.015
        self.v_1 = 0.012
        self.V_M2i = 3.1
        self.K_2i = 0.005
        self.V_M3i = 25
        self.K_3z = 0.022
        self.K_3y = 0.065
        self.V_M2s = 1.5
        self.K_2s = 0.0265
        self.V_M3s = 0.169
        self.K_3s = 0.1

    def to_dict(self):
        return {
            "K_f": self.K_f,
            "K": self.K,
            "beta": self.beta,
            "v_0": self.v_0,
            "v_1": self.v_1,
            "V_M2i": self.V_M2i,
            "K_2i": self.K_2i,
            "V_M3i": self.V_M3i,
            "K_3z": self.K_3z,
            "K_3y": self.K_3y,
            "V_M2s": self.V_M2s,
            "K_2s": self.K_2s,
            "V_M3s": self.V_M3s,
            "K_3s": self.K_3s,
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
        y0=[0.0, 0.0, 0.5],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "borghans_dupont_goldbeter_1997c"
        self.curve_names = [
            "Z",
            "Y",
            "X",
        ]
        self.state_names = ['Z', 'Y', 'X']
        self.algebraic_names = ['V_2i', 'V_3i', 'V_2s', 'V_3s']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 15
        p = self.params

        # direct mapping
        c[0] = p.K_f
        c[1] = p.K
        c[2] = p.beta
        c[3] = p.v_0
        c[4] = p.v_1
        c[5] = p.V_M2i
        c[6] = p.K_2i
        c[7] = p.V_M3i
        c[8] = p.K_3z
        c[9] = p.K_3y
        c[10] = p.V_M2s
        c[11] = p.K_2s
        c[12] = p.V_M3s
        c[13] = p.K_3s

        # derived constants
        c[14] = c[3]+c[4]*c[2]

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
