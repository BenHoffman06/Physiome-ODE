# Size of variable arrays:
sizeAlgebraic = 0
sizeStates = 17
sizeConstants = 18
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (second)"
    legend_states[0] = "T in component T (dimensionless)"
    legend_constants[0] = "delta in component model_parameters (first_order_rate_constant)"
    legend_constants[1] = "gamma in component model_parameters (first_order_rate_constant)"
    legend_constants[2] = "lambda in component model_parameters (first_order_rate_constant)"
    legend_states[1] = "v in component v (dimensionless)"
    legend_states[2] = "I in component I (dimensionless)"
    legend_constants[3] = "alpha in component model_parameters (first_order_rate_constant)"
    legend_constants[4] = "p in component model_parameters (first_order_rate_constant)"
    legend_states[3] = "z in component z (dimensionless)"
    legend_states[4] = "w in component w (dimensionless)"
    legend_states[5] = "x in component x (dimensionless)"
    legend_constants[5] = "r in component model_parameters (first_order_rate_constant)"
    legend_states[6] = "y in component y (dimensionless)"
    legend_constants[6] = "k in component model_parameters (dimensionless)"
    legend_constants[7] = "d in component model_parameters (first_order_rate_constant)"
    legend_constants[8] = "beta in component model_parameters (first_order_rate_constant)"
    legend_constants[9] = "a in component model_parameters (first_order_rate_constant)"
    legend_constants[10] = "u in component model_parameters (first_order_rate_constant)"
    legend_constants[11] = "eta in component model_parameters (first_order_rate_constant)"
    legend_constants[12] = "xi in component model_parameters (first_order_rate_constant)"
    legend_constants[13] = "rho in component model_parameters (first_order_rate_constant)"
    legend_constants[14] = "phi in component model_parameters (first_order_rate_constant)"
    legend_states[7] = "m_9 in component m_9 (dimensionless)"
    legend_states[8] = "m_8 in component m_8 (dimensionless)"
    legend_states[9] = "m_7 in component m_7 (dimensionless)"
    legend_states[10] = "m_6 in component m_6 (dimensionless)"
    legend_states[11] = "m_5 in component m_5 (dimensionless)"
    legend_states[12] = "m_4 in component m_4 (dimensionless)"
    legend_states[13] = "m_3 in component m_3 (dimensionless)"
    legend_states[14] = "m_2 in component m_2 (dimensionless)"
    legend_states[15] = "m_1 in component m_1 (dimensionless)"
    legend_states[16] = "m_0 in component m_0 (dimensionless)"
    legend_constants[15] = "b in component model_parameters (first_order_rate_constant)"
    legend_constants[16] = "epsilon in component model_parameters (dimensionless)"
    legend_constants[17] = "c in component model_parameters (first_order_rate_constant)"
    legend_rates[0] = "d/dt T in component T (dimensionless)"
    legend_rates[2] = "d/dt I in component I (dimensionless)"
    legend_rates[5] = "d/dt x in component x (dimensionless)"
    legend_rates[6] = "d/dt y in component y (dimensionless)"
    legend_rates[1] = "d/dt v in component v (dimensionless)"
    legend_rates[4] = "d/dt w in component w (dimensionless)"
    legend_rates[7] = "d/dt m_9 in component m_9 (dimensionless)"
    legend_rates[8] = "d/dt m_8 in component m_8 (dimensionless)"
    legend_rates[9] = "d/dt m_7 in component m_7 (dimensionless)"
    legend_rates[10] = "d/dt m_6 in component m_6 (dimensionless)"
    legend_rates[11] = "d/dt m_5 in component m_5 (dimensionless)"
    legend_rates[12] = "d/dt m_4 in component m_4 (dimensionless)"
    legend_rates[13] = "d/dt m_3 in component m_3 (dimensionless)"
    legend_rates[14] = "d/dt m_2 in component m_2 (dimensionless)"
    legend_rates[15] = "d/dt m_1 in component m_1 (dimensionless)"
    legend_rates[16] = "d/dt m_0 in component m_0 (dimensionless)"
    legend_rates[3] = "d/dt z in component z (dimensionless)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 1000.0
    constants[0] = 0.01
    constants[1] = 0.01
    constants[2] = 1.0
    states[1] = 0.0001
    states[2] = 0.0001
    constants[3] = 0.2
    constants[4] = 45.0
    states[3] = 0.0
    states[4] = 0.0
    states[5] = 10.0
    constants[5] = 1.0
    states[6] = 0.0
    constants[6] = 10.0
    constants[7] = 0.001
    constants[8] = 0.3
    constants[9] = 0.2
    constants[10] = 1.0
    constants[11] = 1.0
    constants[12] = 0.01
    constants[13] = 0.3
    constants[14] = 1.5
    states[7] = 0.0
    states[8] = 0.0
    states[9] = 0.0
    states[10] = 0.0
    states[11] = 0.0
    states[12] = 0.0
    states[13] = 0.0
    states[14] = 0.0
    states[15] = 0.0
    states[16] = 0.1
    constants[15] = 0.1
    constants[16] = 1.0
    constants[17] = 1.0
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[0] = constants[2]-(constants[0]*states[0]+constants[1]*states[0]*states[1])
    rates[2] = constants[1]*states[0]*states[1]-(constants[3]*states[2]+constants[4]*states[2]*(states[3]+states[4]))
    rates[5] = constants[5]*states[5]*states[1]*(1.00000-(states[5]+states[6])/constants[6])-(constants[7]*states[5]+constants[8]*states[5]*states[1])
    rates[6] = (constants[8]*states[5]*states[1]+constants[5]*states[6]*states[1]*(1.00000-(states[5]+states[6])/constants[6]))-(constants[9]*states[6]+constants[4]*states[6]*(states[3]+states[4]))
    rates[1] = constants[11]*(states[6]+states[2])-constants[10]*states[1]
    rates[4] = 2.00000*constants[13]*states[7]-(constants[12]*states[4]+constants[14]*states[4])
    rates[7] = 2.00000*constants[13]*states[8]-constants[13]*states[7]
    rates[8] = 2.00000*constants[13]*states[9]-constants[13]*states[8]
    rates[9] = 2.00000*constants[13]*states[10]-constants[13]*states[9]
    rates[10] = 2.00000*constants[13]*states[11]-constants[13]*states[10]
    rates[11] = 2.00000*constants[13]*states[12]-constants[13]*states[11]
    rates[12] = 2.00000*constants[13]*states[13]-constants[13]*states[12]
    rates[13] = 2.00000*constants[13]*states[14]-constants[13]*states[13]
    rates[14] = 2.00000*constants[13]*states[15]-constants[13]*states[14]
    rates[15] = 2.00000*constants[13]*states[16]-constants[13]*states[15]
    rates[16] = -(constants[13]*states[16])
    rates[3] = (constants[12]*states[4]+constants[17]*states[5]*(states[6]+states[2])*(states[3]/(constants[16]*states[5]+1.00000)))-constants[15]*states[3]
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
        self.delta = 0.01
        self.gamma = 0.01
        self.lambda = 1.0
        self.alpha = 0.2
        self.p = 45.0
        self.r = 1.0
        self.k = 10.0
        self.d = 0.001
        self.beta = 0.3
        self.a = 0.2
        self.u = 1.0
        self.eta = 1.0
        self.xi = 0.01
        self.rho = 0.3
        self.phi = 1.5
        self.b = 0.1
        self.epsilon = 1.0
        self.c = 1.0

    def to_dict(self):
        return {
            "delta": self.delta,
            "gamma": self.gamma,
            "lambda": self.lambda,
            "alpha": self.alpha,
            "p": self.p,
            "r": self.r,
            "k": self.k,
            "d": self.d,
            "beta": self.beta,
            "a": self.a,
            "u": self.u,
            "eta": self.eta,
            "xi": self.xi,
            "rho": self.rho,
            "phi": self.phi,
            "b": self.b,
            "epsilon": self.epsilon,
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
        y0=[1000.0, 0.0001, 0.0001, 0.0, 0.0, 10.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "wodarz_hamer_2007_d"
        self.curve_names = [
            "T",
            "v",
            "I",
            "z",
            "w",
            "x",
            "y",
            "m_9",
            "m_8",
            "m_7",
            "m_6",
            "m_5",
            "m_4",
            "m_3",
            "m_2",
            "m_1",
            "m_0",
        ]
        self.state_names = ['T', 'v', 'I', 'z', 'w', 'x', 'y', 'm_9', 'm_8', 'm_7', 'm_6', 'm_5', 'm_4', 'm_3', 'm_2', 'm_1', 'm_0']
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
        c = [0.0] * 18
        p = self.params

        # direct mapping
        c[0] = p.delta
        c[1] = p.gamma
        c[2] = p.lambda
        c[3] = p.alpha
        c[4] = p.p
        c[5] = p.r
        c[6] = p.k
        c[7] = p.d
        c[8] = p.beta
        c[9] = p.a
        c[10] = p.u
        c[11] = p.eta
        c[12] = p.xi
        c[13] = p.rho
        c[14] = p.phi
        c[15] = p.b
        c[16] = p.epsilon
        c[17] = p.c

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
