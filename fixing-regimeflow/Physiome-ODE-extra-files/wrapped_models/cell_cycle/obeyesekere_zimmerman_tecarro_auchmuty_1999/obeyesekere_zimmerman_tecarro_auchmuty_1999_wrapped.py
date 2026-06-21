# Size of variable arrays:
sizeAlgebraic = 2
sizeStates = 5
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
    legend_constants[0] = "a_D in component parameters (first_order_rate_constant)"
    legend_constants[1] = "a_E in component parameters (first_order_rate_constant)"
    legend_constants[2] = "a_X in component parameters (first_order_rate_constant)"
    legend_constants[3] = "k in component parameters (dimensionless)"
    legend_constants[4] = "q_D in component parameters (dimensionless)"
    legend_constants[5] = "q_E in component parameters (dimensionless)"
    legend_constants[6] = "q_X in component parameters (dimensionless)"
    legend_constants[7] = "f in component parameters (first_order_rate_constant)"
    legend_constants[8] = "g in component parameters (first_order_rate_constant)"
    legend_constants[9] = "p_S in component parameters (first_order_rate_constant)"
    legend_constants[10] = "p_D in component parameters (first_order_rate_constant)"
    legend_constants[11] = "p_E in component parameters (first_order_rate_constant)"
    legend_constants[12] = "p_X in component parameters (first_order_rate_constant)"
    legend_constants[13] = "d_D in component parameters (first_order_rate_constant)"
    legend_constants[14] = "d_E in component parameters (first_order_rate_constant)"
    legend_constants[15] = "d_X in component parameters (first_order_rate_constant)"
    legend_constants[16] = "a_f in component parameters (first_order_rate_constant)"
    legend_constants[17] = "R_T in component parameters (dimensionless)"
    legend_constants[18] = "theta in component parameters (dimensionless)"
    legend_constants[19] = "GF in component parameters (dimensionless)"
    legend_states[0] = "D in component D (dimensionless)"
    legend_states[1] = "E in component E (dimensionless)"
    legend_states[2] = "R_S in component R_S (dimensionless)"
    legend_states[3] = "X in component X (dimensionless)"
    legend_states[4] = "R in component R (dimensionless)"
    legend_algebraic[0] = "unpho_RB in component unpho_RB (dimensionless)"
    legend_algebraic[1] = "free_E2F in component free_E2F (dimensionless)"
    legend_rates[0] = "d/dt D in component D (dimensionless)"
    legend_rates[1] = "d/dt E in component E (dimensionless)"
    legend_rates[4] = "d/dt R in component R (dimensionless)"
    legend_rates[2] = "d/dt R_S in component R_S (dimensionless)"
    legend_rates[3] = "d/dt X in component X (dimensionless)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    constants[0] = 0.4
    constants[1] = 0.16
    constants[2] = 0.08
    constants[3] = 0.05
    constants[4] = 0.6
    constants[5] = 0.6
    constants[6] = 0.8
    constants[7] = 0.2
    constants[8] = 0.528
    constants[9] = 0.6
    constants[10] = 0.48
    constants[11] = 0.096
    constants[12] = 0.48
    constants[13] = 0.4
    constants[14] = 0.2
    constants[15] = 1.04
    constants[16] = 0.9
    constants[17] = 2.5
    constants[18] = 1.5
    constants[19] = 6.3
    states[0] = 0.1
    states[1] = 0.6
    states[2] = 1
    states[3] = 0.7
    states[4] = 0.5
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[0] = (constants[0]*constants[3]*constants[19])/(1.00000+constants[3]*constants[19])-constants[13]*states[1]*states[0]
    rates[1] = constants[1]*(1.00000+constants[16]*(constants[18]-states[2]))*1.00000-constants[14]*states[3]*states[1]
    rates[4] = (constants[12]*states[3]*((constants[17]-states[2])-states[4]))/(constants[6]+((constants[17]-states[2])-states[4])+states[3])-constants[9]*(constants[18]-states[2])*states[4]
    rates[2] = (constants[9]*(constants[18]-states[2])*states[4]-(constants[10]*states[2]*states[0])/(constants[4]+states[2]+states[0]))-(constants[11]*states[2]*states[1])/(constants[5]+states[2]+states[1])
    rates[3] = (constants[2]*states[1]+constants[7]*(constants[18]-states[2])+constants[8]*(power(states[3], 2.00000))*states[1])-constants[15]*states[3]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = states[4]+states[2]
    algebraic[1] = constants[18]-states[2]
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
        self.a_D = 0.4
        self.a_E = 0.16
        self.a_X = 0.08
        self.k = 0.05
        self.q_D = 0.6
        self.q_E = 0.6
        self.q_X = 0.8
        self.f = 0.2
        self.g = 0.528
        self.p_S = 0.6
        self.p_D = 0.48
        self.p_E = 0.096
        self.p_X = 0.48
        self.d_D = 0.4
        self.d_E = 0.2
        self.d_X = 1.04
        self.a_f = 0.9
        self.R_T = 2.5
        self.theta = 1.5
        self.GF = 6.3

    def to_dict(self):
        return {
            "a_D": self.a_D,
            "a_E": self.a_E,
            "a_X": self.a_X,
            "k": self.k,
            "q_D": self.q_D,
            "q_E": self.q_E,
            "q_X": self.q_X,
            "f": self.f,
            "g": self.g,
            "p_S": self.p_S,
            "p_D": self.p_D,
            "p_E": self.p_E,
            "p_X": self.p_X,
            "d_D": self.d_D,
            "d_E": self.d_E,
            "d_X": self.d_X,
            "a_f": self.a_f,
            "R_T": self.R_T,
            "theta": self.theta,
            "GF": self.GF,
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
        y0=[0.1, 0.6, 1, 0.7, 0.5],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "obeyesekere_zimmerman_tecarro_auchmuty_1999"
        self.curve_names = [
            "D",
            "E",
            "R_S",
            "X",
            "R",
        ]
        self.state_names = ['D', 'E', 'R_S', 'X', 'R']
        self.algebraic_names = ['unpho_RB', 'free_E2F']
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
        c[0] = p.a_D
        c[1] = p.a_E
        c[2] = p.a_X
        c[3] = p.k
        c[4] = p.q_D
        c[5] = p.q_E
        c[6] = p.q_X
        c[7] = p.f
        c[8] = p.g
        c[9] = p.p_S
        c[10] = p.p_D
        c[11] = p.p_E
        c[12] = p.p_X
        c[13] = p.d_D
        c[14] = p.d_E
        c[15] = p.d_X
        c[16] = p.a_f
        c[17] = p.R_T
        c[18] = p.theta
        c[19] = p.GF

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
