# Size of variable arrays:
sizeAlgebraic = 5
sizeStates = 2
sizeConstants = 17
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (minute)"
    legend_states[0] = "x1 in component x1 (picomole)"
    legend_constants[14] = "k in component k (flux)"
    legend_algebraic[4] = "lambda_Ca in component lambda_Ca (per_minute)"
    legend_constants[0] = "lambda1 in component model_parameters (per_minute)"
    legend_constants[15] = "A in component A (per_minute)"
    legend_constants[16] = "B in component B (per_minute)"
    legend_algebraic[0] = "Ca in component Ca (millimolar)"
    legend_algebraic[3] = "S in component S (millimolar)"
    legend_algebraic[2] = "m_Ca in component m_Ca (dimensionless)"
    legend_constants[1] = "m1 in component model_parameters (dimensionless)"
    legend_constants[2] = "m2 in component model_parameters (dimensionless)"
    legend_constants[3] = "beta in component model_parameters (litre_per_millimole)"
    legend_constants[4] = "R in component model_parameters (millimolar)"
    legend_states[1] = "x2 in component x2 (picomole)"
    legend_algebraic[1] = "PTH in component x2 (picomole)"
    legend_constants[5] = "lambda2 in component model_parameters (per_minute)"
    legend_constants[6] = "Ca_0 in component model_parameters (millimolar)"
    legend_constants[7] = "Ca_1 in component model_parameters (millimolar)"
    legend_constants[8] = "alpha in component model_parameters (per_minute)"
    legend_constants[9] = "t0 in component model_parameters (minute)"
    legend_constants[10] = "x1_n in component model_parameters (picomole)"
    legend_constants[11] = "x2_n in component model_parameters (picomole)"
    legend_constants[12] = "x2_max in component model_parameters (picomole)"
    legend_constants[13] = "x2_min in component model_parameters (picomole)"
    legend_rates[0] = "d/dt x1 in component x1 (picomole)"
    legend_rates[1] = "d/dt x2 in component x2 (picomole)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 0.00
    constants[0] = 0.0125
    constants[1] = 112.5200
    constants[2] = 15.00
    constants[3] = 1e6
    constants[4] = 1.2162
    states[1] = 0.00
    constants[5] = 0.5595
    constants[6] = 1.255
    constants[7] = 0.1817
    constants[8] = 0.0442
    constants[9] = 575.0
    constants[10] = 490.7800
    constants[11] = 6.6290
    constants[12] = 14.0430
    constants[13] = 0.6697
    constants[14] = constants[5]*constants[11]+constants[0]*constants[10]
    constants[15] = (constants[0]*constants[5]*constants[12])/(constants[14]-constants[5]*constants[12])
    constants[16] = (constants[0]*constants[5]*constants[13])/(constants[14]-constants[5]*constants[13])
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[0] = custom_piecewise([less(voi , constants[9]), constants[6] , True, constants[6]-constants[7]*(1.00000-exp(-constants[8]*(voi-constants[9])))])
    algebraic[2] = constants[1]/(1.00000+exp(-constants[3]*(constants[4]-algebraic[0])))+constants[2]
    algebraic[3] = constants[6]*(power(-((constants[10]*constants[16]-constants[5]*constants[11])/(constants[10]*constants[15]-constants[5]*constants[11])), 1.00000/algebraic[2]))
    algebraic[4] = (constants[15]-constants[16])/(1.00000+power(algebraic[0]/algebraic[3], algebraic[2]))+constants[16]
    rates[0] = constants[14]-(algebraic[4]*states[0]+constants[0]*states[0])
    rates[1] = algebraic[4]*states[0]-constants[5]*states[1]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = custom_piecewise([less(voi , constants[9]), constants[6] , True, constants[6]-constants[7]*(1.00000-exp(-constants[8]*(voi-constants[9])))])
    algebraic[2] = constants[1]/(1.00000+exp(-constants[3]*(constants[4]-algebraic[0])))+constants[2]
    algebraic[3] = constants[6]*(power(-((constants[10]*constants[16]-constants[5]*constants[11])/(constants[10]*constants[15]-constants[5]*constants[11])), 1.00000/algebraic[2]))
    algebraic[4] = (constants[15]-constants[16])/(1.00000+power(algebraic[0]/algebraic[3], algebraic[2]))+constants[16]
    algebraic[1] = states[1]/2.75000
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
        self.lambda1 = 0.0125
        self.m1 = 112.5200
        self.m2 = 15.00
        self.beta = 1e6
        self.R = 1.2162
        self.lambda2 = 0.5595
        self.Ca_0 = 1.255
        self.Ca_1 = 0.1817
        self.alpha = 0.0442
        self.t0 = 575.0
        self.x1_n = 490.7800
        self.x2_n = 6.6290
        self.x2_max = 14.0430
        self.x2_min = 0.6697

    def to_dict(self):
        return {
            "lambda1": self.lambda1,
            "m1": self.m1,
            "m2": self.m2,
            "beta": self.beta,
            "R": self.R,
            "lambda2": self.lambda2,
            "Ca_0": self.Ca_0,
            "Ca_1": self.Ca_1,
            "alpha": self.alpha,
            "t0": self.t0,
            "x1_n": self.x1_n,
            "x2_n": self.x2_n,
            "x2_max": self.x2_max,
            "x2_min": self.x2_min,
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
        y0=[0.00, 0.00],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "shrestha_2010"
        self.curve_names = [
            "x1",
            "x2",
        ]
        self.state_names = ['x1', 'x2']
        self.algebraic_names = ['Ca', 'PTH', 'm_Ca', 'S', 'lambda_Ca']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 17
        p = self.params

        # direct mapping
        c[0] = p.lambda1
        c[1] = p.m1
        c[2] = p.m2
        c[3] = p.beta
        c[4] = p.R
        c[5] = p.lambda2
        c[6] = p.Ca_0
        c[7] = p.Ca_1
        c[8] = p.alpha
        c[9] = p.t0
        c[10] = p.x1_n
        c[11] = p.x2_n
        c[12] = p.x2_max
        c[13] = p.x2_min

        # derived constants
        c[14] = c[5]*c[11]+c[0]*c[10]
        c[15] = (c[0]*c[5]*c[12])/(c[14]-c[5]*c[12])
        c[16] = (c[0]*c[5]*c[13])/(c[14]-c[5]*c[13])

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
