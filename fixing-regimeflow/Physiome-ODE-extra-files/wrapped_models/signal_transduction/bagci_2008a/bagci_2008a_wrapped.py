# Size of variable arrays:
sizeAlgebraic = 19
sizeStates = 9
sizeConstants = 30
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (second)"
    legend_states[0] = "NO in component NO (micromolar)"
    legend_states[1] = "O_2m in component O_2m (micromolar)"
    legend_constants[0] = "O_2 in component NO (micromolar)"
    legend_states[2] = "NO_2 in component NO (micromolar)"
    legend_states[3] = "N2O3 in component N2O3 (micromolar)"
    legend_states[4] = "GSNO in component GSNO (micromolar)"
    legend_states[5] = "CcOX in component NO (micromolar)"
    legend_states[6] = "FeLn in component FeLn (micromolar)"
    legend_constants[28] = "r_1NO in component NO (flux)"
    legend_algebraic[0] = "r_4NO in component NO (flux)"
    legend_algebraic[1] = "r_12aNO in component NO (flux)"
    legend_algebraic[2] = "r_12bNOp in component NO (flux)"
    legend_algebraic[3] = "r_12bNOm in component NO (flux)"
    legend_algebraic[4] = "r_14NO in component NO (flux)"
    legend_algebraic[5] = "r_15NO in component NO (flux)"
    legend_algebraic[6] = "r_16NO in component NO (flux)"
    legend_constants[1] = "k_1NO in component model_constant (flux)"
    legend_constants[2] = "k_4NO in component model_constant (second_order_rate_constant)"
    legend_constants[3] = "k_12aNO in component model_constant (rate2)"
    legend_constants[4] = "k_12bNOp in component model_constant (second_order_rate_constant)"
    legend_constants[5] = "k_12bNOm in component model_constant (first_order_rate_constant)"
    legend_constants[6] = "k_14NO in component model_constant (first_order_rate_constant)"
    legend_constants[7] = "k_15NO in component model_constant (second_order_rate_constant)"
    legend_constants[8] = "k_16NO in component model_constant (second_order_rate_constant)"
    legend_constants[9] = "SOD in component O_2m (micromolar)"
    legend_constants[29] = "r_2NO in component O_2m (flux)"
    legend_algebraic[7] = "r_5NO in component O_2m (flux)"
    legend_algebraic[8] = "r_10NO in component O_2m (flux)"
    legend_constants[10] = "k_2NO in component model_constant (flux)"
    legend_constants[11] = "k_5NO in component model_constant (second_order_rate_constant)"
    legend_constants[12] = "k_10NO in component model_constant (rate2)"
    legend_states[7] = "ONOO_m in component ONOO_m (micromolar)"
    legend_states[8] = "GSH in component GSH (micromolar)"
    legend_constants[13] = "GPX in component ONOO_m (micromolar)"
    legend_constants[14] = "CO_2 in component ONOO_m (micromolar)"
    legend_constants[15] = "Cyt_c in component ONOO_m (micromolar)"
    legend_algebraic[9] = "r_6NO in component ONOO_m (flux)"
    legend_algebraic[10] = "r_7NO in component ONOO_m (flux)"
    legend_algebraic[12] = "r_8NO in component ONOO_m (flux)"
    legend_algebraic[14] = "r_9NO in component ONOO_m (flux)"
    legend_constants[16] = "k_6NO in component model_constant (second_order_rate_constant)"
    legend_constants[17] = "k_7NO in component model_constant (second_order_rate_constant)"
    legend_constants[18] = "k_8NO in component model_constant (second_order_rate_constant)"
    legend_constants[19] = "k_9NO in component model_constant (second_order_rate_constant)"
    legend_algebraic[13] = "GSSG in component GSH (micromolar)"
    legend_algebraic[11] = "FeLnNO in component GSH (micromolar)"
    legend_constants[20] = "FeLn_0 in component model_constant (micromolar)"
    legend_constants[21] = "GSH_0 in component model_constant (micromolar)"
    legend_algebraic[15] = "r_11NO in component GSH (flux)"
    legend_algebraic[16] = "r_m in component GSH (flux)"
    legend_algebraic[18] = "r_17NO in component GSH (flux)"
    legend_constants[22] = "k_11NO in component model_constant (second_order_rate_constant)"
    legend_constants[23] = "v_m in component model_constant (flux)"
    legend_constants[24] = "k_m in component model_constant (micromolar)"
    legend_constants[25] = "k_17NO in component model_constant (second_order_rate_constant)"
    legend_algebraic[17] = "r_13NO in component N2O3 (flux)"
    legend_constants[26] = "k_13NO in component model_constant (first_order_rate_constant)"
    legend_constants[27] = "k_17bNO in component model_constant (second_order_rate_constant)"
    legend_rates[0] = "d/dt NO in component NO (micromolar)"
    legend_rates[5] = "d/dt CcOX in component NO (micromolar)"
    legend_rates[2] = "d/dt NO_2 in component NO (micromolar)"
    legend_rates[1] = "d/dt O_2m in component O_2m (micromolar)"
    legend_rates[7] = "d/dt ONOO_m in component ONOO_m (micromolar)"
    legend_rates[8] = "d/dt GSH in component GSH (micromolar)"
    legend_rates[4] = "d/dt GSNO in component GSNO (micromolar)"
    legend_rates[3] = "d/dt N2O3 in component N2O3 (micromolar)"
    legend_rates[6] = "d/dt FeLn in component FeLn (micromolar)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 0
    states[1] = 0
    constants[0] = 35
    states[2] = 0
    states[3] = 0
    states[4] = 0
    states[5] = 0.1
    states[6] = 0.05
    constants[1] = 1
    constants[2] = 6700
    constants[3] = 0.000006
    constants[4] = 1100
    constants[5] = 81000
    constants[6] = 0.0002
    constants[7] = 100
    constants[8] = 1.21
    constants[9] = 10
    constants[10] = 0.1
    constants[11] = 2400
    constants[12] = 0.0006
    states[7] = 0
    states[8] = 10000
    constants[13] = 5.8
    constants[14] = 1000
    constants[15] = 400
    constants[16] = 0.00135
    constants[17] = 2
    constants[18] = 0.058
    constants[19] = 0.025
    constants[20] = 0.05
    constants[21] = 10000
    constants[22] = 66
    constants[23] = 320
    constants[24] = 50
    constants[25] = 66
    constants[26] = 1600
    constants[27] = 0.0002
    constants[28] = constants[1]
    constants[29] = constants[10]
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[1] = constants[3]*(power(states[0], 2.00000))*constants[0]
    algebraic[2] = constants[4]*states[2]*states[0]
    algebraic[3] = constants[5]*states[3]
    rates[2] = (2.00000*algebraic[1]-algebraic[2])+algebraic[3]
    algebraic[5] = constants[7]*states[5]*states[0]
    rates[5] = -algebraic[5]
    algebraic[0] = constants[2]*states[0]*states[1]
    algebraic[4] = constants[6]*states[4]
    algebraic[6] = constants[8]*states[6]*states[0]
    rates[0] = (((((constants[28]-algebraic[0])-2.00000*algebraic[1])-algebraic[2])+algebraic[3]+algebraic[4])-algebraic[5])-algebraic[6]
    algebraic[7] = constants[11]*constants[9]*states[1]
    algebraic[8] = constants[12]*(power(states[4], 2.00000))*states[1]
    rates[1] = ((constants[29]-algebraic[0])-algebraic[7])-algebraic[8]
    algebraic[9] = constants[16]*states[7]*states[8]
    algebraic[10] = constants[17]*states[7]*constants[13]
    algebraic[12] = constants[18]*states[7]*constants[14]
    algebraic[14] = constants[19]*states[7]*constants[15]
    rates[7] = (((algebraic[0]-algebraic[9])-algebraic[10])-algebraic[12])-algebraic[14]
    algebraic[15] = constants[22]*states[3]*states[8]
    algebraic[17] = constants[26]*states[3]
    rates[3] = ((-algebraic[15]+algebraic[2])-algebraic[3])-algebraic[17]
    algebraic[13] = ((constants[21]-states[8])-states[4])/2.00000
    algebraic[16] = (constants[23]*algebraic[13])/(constants[24]+algebraic[13])
    algebraic[11] = constants[20]-states[6]
    algebraic[18] = constants[25]*algebraic[11]*states[8]
    rates[8] = ((-algebraic[9]-algebraic[15])+2.00000*algebraic[16])-algebraic[18]
    rates[4] = (((algebraic[9]-2.00000*algebraic[8])+algebraic[15])-algebraic[4])+algebraic[18]
    rates[6] = -algebraic[6]+algebraic[18]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[1] = constants[3]*(power(states[0], 2.00000))*constants[0]
    algebraic[2] = constants[4]*states[2]*states[0]
    algebraic[3] = constants[5]*states[3]
    algebraic[5] = constants[7]*states[5]*states[0]
    algebraic[0] = constants[2]*states[0]*states[1]
    algebraic[4] = constants[6]*states[4]
    algebraic[6] = constants[8]*states[6]*states[0]
    algebraic[7] = constants[11]*constants[9]*states[1]
    algebraic[8] = constants[12]*(power(states[4], 2.00000))*states[1]
    algebraic[9] = constants[16]*states[7]*states[8]
    algebraic[10] = constants[17]*states[7]*constants[13]
    algebraic[12] = constants[18]*states[7]*constants[14]
    algebraic[14] = constants[19]*states[7]*constants[15]
    algebraic[15] = constants[22]*states[3]*states[8]
    algebraic[17] = constants[26]*states[3]
    algebraic[13] = ((constants[21]-states[8])-states[4])/2.00000
    algebraic[16] = (constants[23]*algebraic[13])/(constants[24]+algebraic[13])
    algebraic[11] = constants[20]-states[6]
    algebraic[18] = constants[25]*algebraic[11]*states[8]
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
        self.O_2 = 35
        self.k_1NO = 1
        self.k_4NO = 6700
        self.k_12aNO = 0.000006
        self.k_12bNOp = 1100
        self.k_12bNOm = 81000
        self.k_14NO = 0.0002
        self.k_15NO = 100
        self.k_16NO = 1.21
        self.SOD = 10
        self.k_2NO = 0.1
        self.k_5NO = 2400
        self.k_10NO = 0.0006
        self.GPX = 5.8
        self.CO_2 = 1000
        self.Cyt_c = 400
        self.k_6NO = 0.00135
        self.k_7NO = 2
        self.k_8NO = 0.058
        self.k_9NO = 0.025
        self.FeLn_0 = 0.05
        self.GSH_0 = 10000
        self.k_11NO = 66
        self.v_m = 320
        self.k_m = 50
        self.k_17NO = 66
        self.k_13NO = 1600
        self.k_17bNO = 0.0002

    def to_dict(self):
        return {
            "O_2": self.O_2,
            "k_1NO": self.k_1NO,
            "k_4NO": self.k_4NO,
            "k_12aNO": self.k_12aNO,
            "k_12bNOp": self.k_12bNOp,
            "k_12bNOm": self.k_12bNOm,
            "k_14NO": self.k_14NO,
            "k_15NO": self.k_15NO,
            "k_16NO": self.k_16NO,
            "SOD": self.SOD,
            "k_2NO": self.k_2NO,
            "k_5NO": self.k_5NO,
            "k_10NO": self.k_10NO,
            "GPX": self.GPX,
            "CO_2": self.CO_2,
            "Cyt_c": self.Cyt_c,
            "k_6NO": self.k_6NO,
            "k_7NO": self.k_7NO,
            "k_8NO": self.k_8NO,
            "k_9NO": self.k_9NO,
            "FeLn_0": self.FeLn_0,
            "GSH_0": self.GSH_0,
            "k_11NO": self.k_11NO,
            "v_m": self.v_m,
            "k_m": self.k_m,
            "k_17NO": self.k_17NO,
            "k_13NO": self.k_13NO,
            "k_17bNO": self.k_17bNO,
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
        y0=[0, 0, 0, 0, 0, 0.1, 0.05, 0, 10000],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "bagci_2008a"
        self.curve_names = [
            "NO",
            "O_2m",
            "NO_2",
            "N2O3",
            "GSNO",
            "CcOX",
            "FeLn",
            "ONOO_m",
            "GSH",
        ]
        self.state_names = ['NO', 'O_2m', 'NO_2', 'N2O3', 'GSNO', 'CcOX', 'FeLn', 'ONOO_m', 'GSH']
        self.algebraic_names = ['r_4NO', 'r_12aNO', 'r_12bNOp', 'r_12bNOm', 'r_14NO', 'r_15NO', 'r_16NO', 'r_5NO', 'r_10NO', 'r_6NO', 'r_7NO', 'FeLnNO', 'r_8NO', 'GSSG', 'r_9NO', 'r_11NO', 'r_m', 'r_13NO', 'r_17NO']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 30
        p = self.params

        # direct mapping
        c[0] = p.O_2
        c[1] = p.k_1NO
        c[2] = p.k_4NO
        c[3] = p.k_12aNO
        c[4] = p.k_12bNOp
        c[5] = p.k_12bNOm
        c[6] = p.k_14NO
        c[7] = p.k_15NO
        c[8] = p.k_16NO
        c[9] = p.SOD
        c[10] = p.k_2NO
        c[11] = p.k_5NO
        c[12] = p.k_10NO
        c[13] = p.GPX
        c[14] = p.CO_2
        c[15] = p.Cyt_c
        c[16] = p.k_6NO
        c[17] = p.k_7NO
        c[18] = p.k_8NO
        c[19] = p.k_9NO
        c[20] = p.FeLn_0
        c[21] = p.GSH_0
        c[22] = p.k_11NO
        c[23] = p.v_m
        c[24] = p.k_m
        c[25] = p.k_17NO
        c[26] = p.k_13NO
        c[27] = p.k_17bNO

        # derived constants
        c[28] = c[1]
        c[29] = c[10]

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
