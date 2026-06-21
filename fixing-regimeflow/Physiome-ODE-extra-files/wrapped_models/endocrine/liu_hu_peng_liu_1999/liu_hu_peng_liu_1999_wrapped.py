# Size of variable arrays:
sizeAlgebraic = 0
sizeStates = 5
sizeConstants = 36
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (minute)"
    legend_states[0] = "x1 in component x1 (microg_l)"
    legend_constants[0] = "lambda_1 in component model_parameters (first_order_rate_constant)"
    legend_states[1] = "x3 in component x3 (microg_l)"
    legend_constants[1] = "a1 in component model_parameters (flux)"
    legend_constants[2] = "a2 in component model_parameters (flux)"
    legend_constants[3] = "a3 in component model_parameters (first_order_rate_constant)"
    legend_constants[4] = "a4 in component model_parameters (second_order_rate_constant)"
    legend_constants[5] = "a5 in component model_parameters (per_microg_l)"
    legend_constants[6] = "a6 in component model_parameters (per_microg_l2)"
    legend_constants[7] = "a7 in component model_parameters (per_microg_l)"
    legend_constants[8] = "a8 in component model_parameters (per_microg_l2)"
    legend_states[2] = "x2 in component x2 (microg_l)"
    legend_constants[9] = "lambda_2 in component model_parameters (first_order_rate_constant)"
    legend_constants[10] = "a9 in component model_parameters (flux)"
    legend_constants[11] = "a10 in component model_parameters (first_order_rate_constant)"
    legend_constants[12] = "a11 in component model_parameters (second_order_rate_constant)"
    legend_constants[13] = "a12 in component model_parameters (per_microg_l)"
    legend_constants[14] = "a13 in component model_parameters (per_microg_l2)"
    legend_constants[15] = "a14 in component model_parameters (per_microg_l)"
    legend_constants[16] = "a15 in component model_parameters (per_microg_l2)"
    legend_constants[33] = "lambda_3_ in component model_parameters (first_order_rate_constant)"
    legend_states[3] = "x4 in component x4 (microg_l)"
    legend_states[4] = "x5 in component x5 (microg_l)"
    legend_constants[17] = "a16 in component model_parameters (flux)"
    legend_constants[18] = "a17 in component model_parameters (first_order_rate_constant)"
    legend_constants[19] = "a18 in component model_parameters (second_order_rate_constant)"
    legend_constants[20] = "a19 in component model_parameters (first_order_rate_constant)"
    legend_constants[21] = "a20 in component model_parameters (second_order_rate_constant)"
    legend_constants[22] = "a21 in component model_parameters (per_microg_l)"
    legend_constants[23] = "a22 in component model_parameters (per_microg_l2)"
    legend_constants[24] = "a23 in component model_parameters (per_microg_l)"
    legend_constants[25] = "a24 in component model_parameters (per_microg_l2)"
    legend_constants[26] = "a25 in component model_parameters (first_order_rate_constant)"
    legend_constants[27] = "a26 in component model_parameters (first_order_rate_constant)"
    legend_constants[34] = "lambda_4_ in component model_parameters (first_order_rate_constant)"
    legend_constants[28] = "a27 in component model_parameters (first_order_rate_constant)"
    legend_constants[35] = "lambda_5_ in component model_parameters (first_order_rate_constant)"
    legend_constants[29] = "a28 in component model_parameters (first_order_rate_constant)"
    legend_constants[30] = "lambda_3 in component model_parameters (first_order_rate_constant)"
    legend_constants[31] = "lambda_4 in component model_parameters (first_order_rate_constant)"
    legend_constants[32] = "lambda_5 in component model_parameters (first_order_rate_constant)"
    legend_rates[0] = "d/dt x1 in component x1 (microg_l)"
    legend_rates[2] = "d/dt x2 in component x2 (microg_l)"
    legend_rates[1] = "d/dt x3 in component x3 (microg_l)"
    legend_rates[3] = "d/dt x4 in component x4 (microg_l)"
    legend_rates[4] = "d/dt x5 in component x5 (microg_l)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 0.01067
    constants[0] = 0.059
    states[1] = 6.51
    constants[1] = 0.000017
    constants[2] = 0.0023
    constants[3] = 0.6
    constants[4] = 45
    constants[5] = 36
    constants[6] = 216
    constants[7] = 0.28
    constants[8] = 0.36
    states[2] = 0.04665
    constants[9] = 0.028
    constants[10] = 0.0003
    constants[11] = 0.18
    constants[12] = 150
    constants[13] = 18
    constants[14] = 460
    constants[15] = 0.46
    constants[16] = 0.1
    states[3] = 60.61
    states[4] = 12.61
    constants[17] = 0.04
    constants[18] = 150
    constants[19] = 3800
    constants[20] = 57
    constants[21] = 2600
    constants[22] = 200
    constants[23] = 9400
    constants[24] = 10
    constants[25] = 320
    constants[26] = 0.04
    constants[27] = 0.00097
    constants[28] = 0.57
    constants[29] = 0.0017
    constants[30] = 0.0986
    constants[31] = 0.024
    constants[32] = 3e-5
    constants[33] = constants[30]+constants[28]+constants[29]
    constants[34] = constants[31]+constants[26]
    constants[35] = constants[32]+constants[27]
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[0] = (constants[1]+(constants[2]+constants[3]*states[0]+constants[4]*(power(states[0], 2.00000)))/(1.00000+constants[5]*states[0]+constants[6]*(power(states[0], 2.00000))+constants[7]*states[1]+constants[8]*(power(states[1], 2.00000))))-constants[0]*states[0]
    rates[2] = (constants[10]+constants[11]*states[0]+constants[12]*(power(states[0], 2.00000)))/(1.00000+constants[13]*states[0]+constants[14]*(power(states[0], 2.00000))+constants[15]*states[1]+constants[16]*(power(states[1], 2.00000)))-constants[9]*states[2]
    rates[1] = (constants[17]+(constants[18]*states[0]+constants[19]*(power(states[0], 2.00000))+constants[20]*states[2]+constants[21]*(power(states[2], 2.00000)))/(1.00000+constants[22]*states[0]+constants[23]*(power(states[0], 2.00000))+constants[24]*states[2]+constants[25]*(power(states[2], 2.00000)))+constants[26]*states[3]+constants[27]*states[4])-constants[33]*states[1]
    rates[3] = constants[28]*states[1]-constants[34]*states[3]
    rates[4] = constants[29]*states[1]-constants[35]*states[4]
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
        self.lambda_1 = 0.059
        self.a1 = 0.000017
        self.a2 = 0.0023
        self.a3 = 0.6
        self.a4 = 45
        self.a5 = 36
        self.a6 = 216
        self.a7 = 0.28
        self.a8 = 0.36
        self.lambda_2 = 0.028
        self.a9 = 0.0003
        self.a10 = 0.18
        self.a11 = 150
        self.a12 = 18
        self.a13 = 460
        self.a14 = 0.46
        self.a15 = 0.1
        self.a16 = 0.04
        self.a17 = 150
        self.a18 = 3800
        self.a19 = 57
        self.a20 = 2600
        self.a21 = 200
        self.a22 = 9400
        self.a23 = 10
        self.a24 = 320
        self.a25 = 0.04
        self.a26 = 0.00097
        self.a27 = 0.57
        self.a28 = 0.0017
        self.lambda_3 = 0.0986
        self.lambda_4 = 0.024
        self.lambda_5 = 3e-5

    def to_dict(self):
        return {
            "lambda_1": self.lambda_1,
            "a1": self.a1,
            "a2": self.a2,
            "a3": self.a3,
            "a4": self.a4,
            "a5": self.a5,
            "a6": self.a6,
            "a7": self.a7,
            "a8": self.a8,
            "lambda_2": self.lambda_2,
            "a9": self.a9,
            "a10": self.a10,
            "a11": self.a11,
            "a12": self.a12,
            "a13": self.a13,
            "a14": self.a14,
            "a15": self.a15,
            "a16": self.a16,
            "a17": self.a17,
            "a18": self.a18,
            "a19": self.a19,
            "a20": self.a20,
            "a21": self.a21,
            "a22": self.a22,
            "a23": self.a23,
            "a24": self.a24,
            "a25": self.a25,
            "a26": self.a26,
            "a27": self.a27,
            "a28": self.a28,
            "lambda_3": self.lambda_3,
            "lambda_4": self.lambda_4,
            "lambda_5": self.lambda_5,
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
        y0=[0.01067, 6.51, 0.04665, 60.61, 12.61],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "liu_hu_peng_liu_1999"
        self.curve_names = [
            "x1",
            "x3",
            "x2",
            "x4",
            "x5",
        ]
        self.state_names = ['x1', 'x3', 'x2', 'x4', 'x5']
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
        c = [0.0] * 36
        p = self.params

        # direct mapping
        c[0] = p.lambda_1
        c[1] = p.a1
        c[2] = p.a2
        c[3] = p.a3
        c[4] = p.a4
        c[5] = p.a5
        c[6] = p.a6
        c[7] = p.a7
        c[8] = p.a8
        c[9] = p.lambda_2
        c[10] = p.a9
        c[11] = p.a10
        c[12] = p.a11
        c[13] = p.a12
        c[14] = p.a13
        c[15] = p.a14
        c[16] = p.a15
        c[17] = p.a16
        c[18] = p.a17
        c[19] = p.a18
        c[20] = p.a19
        c[21] = p.a20
        c[22] = p.a21
        c[23] = p.a22
        c[24] = p.a23
        c[25] = p.a24
        c[26] = p.a25
        c[27] = p.a26
        c[28] = p.a27
        c[29] = p.a28
        c[30] = p.lambda_3
        c[31] = p.lambda_4
        c[32] = p.lambda_5

        # derived constants
        c[33] = c[30]+c[28]+c[29]
        c[34] = c[31]+c[26]
        c[35] = c[32]+c[27]

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
