# Size of variable arrays:
sizeAlgebraic = 2
sizeStates = 3
sizeConstants = 18
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
    legend_constants[17] = "V_in in component V_in (uM_per_min)"
    legend_algebraic[0] = "V_2 in component V_2 (uM_per_min)"
    legend_algebraic[1] = "V_3 in component V_3 (uM_per_min)"
    legend_constants[0] = "K_f in component Ca (per_min)"
    legend_constants[1] = "K in component Ca (per_min)"
    legend_constants[2] = "beta in component Ca_flux (dimensionless)"
    legend_constants[3] = "v_0 in component V_in (uM_per_min)"
    legend_constants[4] = "v_1 in component V_in (uM_per_min)"
    legend_constants[5] = "V_M2 in component V_2 (uM_per_min)"
    legend_constants[6] = "K_2 in component V_2 (uM)"
    legend_states[2] = "A in component A (uM)"
    legend_constants[7] = "K_y in component V_3 (uM)"
    legend_constants[8] = "K_z in component V_3 (uM)"
    legend_constants[9] = "K_a in component V_3 (uM)"
    legend_constants[10] = "V_M3 in component V_3 (uM_per_min)"
    legend_constants[11] = "upsilon_p in component A (uM_per_min)"
    legend_constants[12] = "upsilon_d in component A (uM_per_min)"
    legend_constants[13] = "K_p in component A (uM)"
    legend_constants[14] = "K_d in component A (uM)"
    legend_constants[15] = "n in component A (dimensionless)"
    legend_constants[16] = "epsilon in component A (per_min)"
    legend_rates[0] = "d/dt Z in component Ca (uM)"
    legend_rates[1] = "d/dt Y in component Ca (uM)"
    legend_rates[2] = "d/dt A in component A (uM)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 0.1
    states[1] = 1.0
    constants[0] = 1
    constants[1] = 10
    constants[2] = 0.5
    constants[3] = 2
    constants[4] = 1
    constants[5] = 6.5
    constants[6] = 0.1
    states[2] = 0.5
    constants[7] = 0.2
    constants[8] = 0.3
    constants[9] = 0.2
    constants[10] = 19.5
    constants[11] = 2.5
    constants[12] = 80
    constants[13] = 1
    constants[14] = 0.4
    constants[15] = 4
    constants[16] = 0.1
    constants[17] = constants[3]+constants[4]*constants[2]
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[2] = (constants[2]*constants[11]-constants[12]*((power(states[2], 2.00000))/(power(constants[13], 2.00000)+power(states[2], 2.00000)))*((power(states[0], constants[15]))/(power(constants[14], constants[15])+power(states[0], constants[15]))))-constants[16]*states[2]
    algebraic[0] = constants[5]*((power(states[0], 2.00000))/(power(constants[6], 2.00000)+power(states[0], 2.00000)))
    algebraic[1] = constants[10]*((power(states[2], 4.00000))/(power(constants[9], 4.00000)+power(states[2], 4.00000)))*((power(states[1], 2.00000))/(power(constants[7], 2.00000)+power(states[1], 2.00000)))*((power(states[0], 4.00000))/(power(constants[8], 4.00000)+power(states[0], 4.00000)))
    rates[0] = (constants[17]-algebraic[0])+algebraic[1]+(constants[0]*states[1]-constants[1]*states[0])
    rates[1] = (algebraic[0]-algebraic[1])-constants[0]*states[1]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = constants[5]*((power(states[0], 2.00000))/(power(constants[6], 2.00000)+power(states[0], 2.00000)))
    algebraic[1] = constants[10]*((power(states[2], 4.00000))/(power(constants[9], 4.00000)+power(states[2], 4.00000)))*((power(states[1], 2.00000))/(power(constants[7], 2.00000)+power(states[1], 2.00000)))*((power(states[0], 4.00000))/(power(constants[8], 4.00000)+power(states[0], 4.00000)))
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
        self.K_f = 1
        self.K = 10
        self.beta = 0.5
        self.v_0 = 2
        self.v_1 = 1
        self.V_M2 = 6.5
        self.K_2 = 0.1
        self.K_y = 0.2
        self.K_z = 0.3
        self.K_a = 0.2
        self.V_M3 = 19.5
        self.upsilon_p = 2.5
        self.upsilon_d = 80
        self.K_p = 1
        self.K_d = 0.4
        self.n = 4
        self.epsilon = 0.1

    def to_dict(self):
        return {
            "K_f": self.K_f,
            "K": self.K,
            "beta": self.beta,
            "v_0": self.v_0,
            "v_1": self.v_1,
            "V_M2": self.V_M2,
            "K_2": self.K_2,
            "K_y": self.K_y,
            "K_z": self.K_z,
            "K_a": self.K_a,
            "V_M3": self.V_M3,
            "upsilon_p": self.upsilon_p,
            "upsilon_d": self.upsilon_d,
            "K_p": self.K_p,
            "K_d": self.K_d,
            "n": self.n,
            "epsilon": self.epsilon,
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
        y0=[0.1, 1.0, 0.5],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "borghans_dupont_goldbeter_1997b"
        self.curve_names = [
            "Z",
            "Y",
            "A",
        ]
        self.state_names = ['Z', 'Y', 'A']
        self.algebraic_names = ['V_2', 'V_3']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 18
        p = self.params

        # direct mapping
        c[0] = p.K_f
        c[1] = p.K
        c[2] = p.beta
        c[3] = p.v_0
        c[4] = p.v_1
        c[5] = p.V_M2
        c[6] = p.K_2
        c[7] = p.K_y
        c[8] = p.K_z
        c[9] = p.K_a
        c[10] = p.V_M3
        c[11] = p.upsilon_p
        c[12] = p.upsilon_d
        c[13] = p.K_p
        c[14] = p.K_d
        c[15] = p.n
        c[16] = p.epsilon

        # derived constants
        c[17] = c[3]+c[4]*c[2]

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
