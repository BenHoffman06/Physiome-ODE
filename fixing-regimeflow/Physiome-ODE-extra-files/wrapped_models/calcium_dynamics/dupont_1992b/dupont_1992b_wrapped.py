# Size of variable arrays:
sizeAlgebraic = 3
sizeStates = 3
sizeConstants = 19
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (minute)"
    legend_constants[0] = "VM2 in component parameters (micromolar_min)"
    legend_constants[1] = "VM3 in component parameters (micromolar_min)"
    legend_constants[2] = "KR in component parameters (micromolar)"
    legend_constants[3] = "KA in component parameters (micromolar)"
    legend_constants[4] = "KP in component parameters (micromolar)"
    legend_constants[5] = "n in component parameters (dimensionless)"
    legend_constants[6] = "m in component parameters (dimensionless)"
    legend_constants[7] = "p in component parameters (dimensionless)"
    legend_constants[8] = "kf in component parameters (per_minute)"
    legend_constants[9] = "k in component parameters (per_minute)"
    legend_states[0] = "Y in component insensitive_pool (micromolar)"
    legend_states[1] = "Z in component cytosol (micromolar)"
    legend_algebraic[0] = "v2 in component parameters (micromolar_min)"
    legend_algebraic[2] = "v3 in component parameters (micromolar_min)"
    legend_constants[10] = "v0 in component cytosol (micromolar_min)"
    legend_constants[11] = "v1beta in component cytosol (micromolar_min)"
    legend_constants[12] = "K1 in component phosphorylation (dimensionless)"
    legend_constants[13] = "K2 in component phosphorylation (dimensionless)"
    legend_constants[14] = "WT in component phosphorylation (micromolar)"
    legend_constants[18] = "vP in component phosphorylation (micromolar_min)"
    legend_algebraic[1] = "vK in component kinase_reaction (micromolar_min)"
    legend_constants[15] = "vMK in component kinase_reaction (micromolar_min)"
    legend_states[2] = "Wstar in component phosphorylation (dimensionless)"
    legend_constants[16] = "Ka in component kinase_reaction (micromolar)"
    legend_constants[17] = "q in component kinase_reaction (dimensionless)"
    legend_rates[1] = "d/dt Z in component cytosol (micromolar)"
    legend_rates[0] = "d/dt Y in component insensitive_pool (micromolar)"
    legend_rates[2] = "d/dt Wstar in component phosphorylation (dimensionless)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    constants[0] = 65
    constants[1] = 500
    constants[2] = 2
    constants[3] = 0.9
    constants[4] = 1
    constants[5] = 2
    constants[6] = 2
    constants[7] = 4
    constants[8] = 1
    constants[9] = 10
    states[0] = 1.454
    states[1] = 0.2281
    constants[10] = 1
    constants[11] = 2.4
    constants[12] = 0.01
    constants[13] = 0.01
    constants[14] = 10
    constants[15] = 100
    states[2] = 0.8916
    constants[16] = 1
    constants[17] = 4
    constants[18] = constants[15]*(0.890000/20.0000)
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[1] = constants[15]*((power(states[1], constants[17]))/(power(constants[16], constants[17])+power(states[1], constants[17])))
    rates[2] = (constants[18]/constants[14])*(((algebraic[1]/constants[18])*(1.00000-states[2]))/((constants[12]+1.00000)-states[2])-states[2]/(constants[13]+states[2]))
    algebraic[0] = (constants[0]*(power(states[1], constants[5])))/(power(constants[4], constants[5])+power(states[1], constants[5]))
    algebraic[2] = constants[1]*((power(states[0], constants[6]))/(power(constants[2], constants[6])+power(states[0], constants[6])))*((power(states[1], constants[7]))/(power(constants[3], constants[7])+power(states[1], constants[7])))
    rates[1] = (((constants[10]+constants[11])-algebraic[0])+algebraic[2]+constants[8]*states[0])-constants[9]*states[1]
    rates[0] = (algebraic[0]-algebraic[2])-constants[8]*states[0]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[1] = constants[15]*((power(states[1], constants[17]))/(power(constants[16], constants[17])+power(states[1], constants[17])))
    algebraic[0] = (constants[0]*(power(states[1], constants[5])))/(power(constants[4], constants[5])+power(states[1], constants[5]))
    algebraic[2] = constants[1]*((power(states[0], constants[6]))/(power(constants[2], constants[6])+power(states[0], constants[6])))*((power(states[1], constants[7]))/(power(constants[3], constants[7])+power(states[1], constants[7])))
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
        self.VM2 = 65
        self.VM3 = 500
        self.KR = 2
        self.KA = 0.9
        self.KP = 1
        self.n = 2
        self.m = 2
        self.p = 4
        self.kf = 1
        self.k = 10
        self.v0 = 1
        self.v1beta = 2.4
        self.K1 = 0.01
        self.K2 = 0.01
        self.WT = 10
        self.vMK = 100
        self.Ka = 1
        self.q = 4

    def to_dict(self):
        return {
            "VM2": self.VM2,
            "VM3": self.VM3,
            "KR": self.KR,
            "KA": self.KA,
            "KP": self.KP,
            "n": self.n,
            "m": self.m,
            "p": self.p,
            "kf": self.kf,
            "k": self.k,
            "v0": self.v0,
            "v1beta": self.v1beta,
            "K1": self.K1,
            "K2": self.K2,
            "WT": self.WT,
            "vMK": self.vMK,
            "Ka": self.Ka,
            "q": self.q,
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
        y0=[1.454, 0.2281, 0.8916],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "dupont_1992b"
        self.curve_names = [
            "Y",
            "Z",
            "Wstar",
        ]
        self.state_names = ['Y', 'Z', 'Wstar']
        self.algebraic_names = ['v2', 'vK', 'v3']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 19
        p = self.params

        # direct mapping
        c[0] = p.VM2
        c[1] = p.VM3
        c[2] = p.KR
        c[3] = p.KA
        c[4] = p.KP
        c[5] = p.n
        c[6] = p.m
        c[7] = p.p
        c[8] = p.kf
        c[9] = p.k
        c[10] = p.v0
        c[11] = p.v1beta
        c[12] = p.K1
        c[13] = p.K2
        c[14] = p.WT
        c[15] = p.vMK
        c[16] = p.Ka
        c[17] = p.q

        # derived constants
        c[18] = c[15]*(0.890000/20.0000)

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
