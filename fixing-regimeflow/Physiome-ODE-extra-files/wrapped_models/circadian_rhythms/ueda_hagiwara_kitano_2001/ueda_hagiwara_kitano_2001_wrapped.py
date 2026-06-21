# Size of variable arrays:
sizeAlgebraic = 0
sizeStates = 10
sizeConstants = 55
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (hour)"
    legend_states[0] = "Per_m in component Per_m (nanomolar)"
    legend_constants[0] = "B1 in component Per_m (dimensionless)"
    legend_constants[1] = "C1 in component Per_m (flux)"
    legend_constants[2] = "S1 in component Per_m (flux)"
    legend_constants[3] = "D1 in component Per_m (flux)"
    legend_constants[4] = "L1 in component Per_m (nanomolar)"
    legend_constants[5] = "R1 in component Per_m (nanomolar)"
    legend_constants[6] = "A1 in component Per_m (nanomolar)"
    legend_states[1] = "PT_n in component PT_n (nanomolar)"
    legend_states[2] = "CC_n in component CC_n (nanomolar)"
    legend_constants[7] = "D0 in component parameters (first_order_rate_constant)"
    legend_constants[8] = "a in component parameters (dimensionless)"
    legend_constants[9] = "r in component parameters (dimensionless)"
    legend_states[3] = "Per_c in component Per_c (nanomolar)"
    legend_constants[10] = "S2 in component Per_c (first_order_rate_constant)"
    legend_constants[11] = "D2 in component Per_c (first_order_rate_constant)"
    legend_constants[12] = "L2 in component Per_c (nanomolar)"
    legend_constants[13] = "Dbt_c in component Per_c (nanomolar)"
    legend_constants[14] = "V1 in component parameters (second_order_rate_constant)"
    legend_constants[15] = "V2 in component parameters (first_order_rate_constant)"
    legend_states[4] = "Tim_c in component Tim_c (nanomolar)"
    legend_states[5] = "PT_c in component PT_c (nanomolar)"
    legend_states[6] = "Tim_m in component Tim_m (nanomolar)"
    legend_constants[16] = "B2 in component Tim_m (dimensionless)"
    legend_constants[17] = "C2 in component Tim_m (flux)"
    legend_constants[18] = "S3 in component Tim_m (flux)"
    legend_constants[19] = "D3 in component Tim_m (flux)"
    legend_constants[20] = "L3 in component Tim_m (nanomolar)"
    legend_constants[21] = "R2 in component Tim_m (nanomolar)"
    legend_constants[22] = "A2 in component Tim_m (nanomolar)"
    legend_constants[23] = "S4 in component Tim_c (first_order_rate_constant)"
    legend_constants[24] = "D4 in component Tim_c (flux)"
    legend_constants[25] = "L4 in component Tim_c (nanomolar)"
    legend_constants[26] = "D5 in component PT_c (flux)"
    legend_constants[27] = "L5 in component PT_c (nanomolar)"
    legend_constants[28] = "K1 in component parameters (nanomolar)"
    legend_constants[29] = "K2 in component parameters (nanomolar)"
    legend_constants[30] = "T1 in component parameters (flux)"
    legend_constants[31] = "T2 in component parameters (flux)"
    legend_constants[32] = "D6 in component PT_n (flux)"
    legend_constants[33] = "L6 in component PT_n (nanomolar)"
    legend_states[7] = "Clk_m in component Clk_m (nanomolar)"
    legend_constants[34] = "B3 in component Clk_m (dimensionless)"
    legend_constants[35] = "C3 in component Clk_m (flux)"
    legend_constants[36] = "S5 in component Clk_m (flux)"
    legend_constants[37] = "D7 in component Clk_m (flux)"
    legend_constants[38] = "L7 in component Clk_m (nanomolar)"
    legend_constants[39] = "R3 in component Clk_m (nanomolar)"
    legend_constants[40] = "A3 in component Clk_m (nanomolar)"
    legend_states[8] = "Clk_c in component Clk_c (nanomolar)"
    legend_constants[41] = "S6 in component Clk_c (first_order_rate_constant)"
    legend_constants[42] = "D8 in component Clk_c (flux)"
    legend_constants[43] = "L8 in component Clk_c (nanomolar)"
    legend_constants[44] = "V3 in component parameters (second_order_rate_constant)"
    legend_constants[45] = "V4 in component parameters (first_order_rate_constant)"
    legend_constants[46] = "Cyc_c in component Cyc_c (nanomolar)"
    legend_states[9] = "CC_c in component CC_c (nanomolar)"
    legend_constants[47] = "D9 in component CC_c (flux)"
    legend_constants[48] = "L9 in component CC_c (nanomolar)"
    legend_constants[49] = "K3 in component parameters (nanomolar)"
    legend_constants[50] = "K4 in component parameters (nanomolar)"
    legend_constants[51] = "T3 in component parameters (flux)"
    legend_constants[52] = "T4 in component parameters (flux)"
    legend_constants[53] = "D10 in component CC_n (flux)"
    legend_constants[54] = "L10 in component CC_n (nanomolar)"
    legend_rates[0] = "d/dt Per_m in component Per_m (nanomolar)"
    legend_rates[3] = "d/dt Per_c in component Per_c (nanomolar)"
    legend_rates[6] = "d/dt Tim_m in component Tim_m (nanomolar)"
    legend_rates[4] = "d/dt Tim_c in component Tim_c (nanomolar)"
    legend_rates[5] = "d/dt PT_c in component PT_c (nanomolar)"
    legend_rates[1] = "d/dt PT_n in component PT_n (nanomolar)"
    legend_rates[7] = "d/dt Clk_m in component Clk_m (nanomolar)"
    legend_rates[8] = "d/dt Clk_c in component Clk_c (nanomolar)"
    legend_rates[9] = "d/dt CC_c in component CC_c (nanomolar)"
    legend_rates[2] = "d/dt CC_n in component CC_n (nanomolar)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 0.5
    constants[0] = 0.0
    constants[1] = 0.0
    constants[2] = 1.45
    constants[3] = 0.94
    constants[4] = 0.3
    constants[5] = 1.02
    constants[6] = 0.45
    states[1] = 1.0
    states[2] = 0.4
    constants[7] = 0.012
    constants[8] = 1.0
    constants[9] = 4.0
    states[3] = 0.6
    constants[10] = 0.48
    constants[11] = 0.44
    constants[12] = 0.2
    constants[13] = 1.0
    constants[14] = 1.45
    constants[15] = 1.45
    states[4] = 0.8
    states[5] = 0.9
    states[6] = 0.7
    constants[16] = 0.0
    constants[17] = 0.0
    constants[18] = 1.45
    constants[19] = 0.94
    constants[20] = 0.3
    constants[21] = 1.02
    constants[22] = 0.45
    constants[23] = 0.48
    constants[24] = 0.44
    constants[25] = 0.2
    constants[26] = 0.44
    constants[27] = 0.2
    constants[28] = 2.0
    constants[29] = 2.0
    constants[30] = 1.73
    constants[31] = 0.72
    constants[32] = 0.29
    constants[33] = 0.2
    states[7] = 0.1
    constants[34] = 0.6
    constants[35] = 0.0
    constants[36] = 1.63
    constants[37] = 0.54
    constants[38] = 0.13
    constants[39] = 0.89
    constants[40] = 0.8
    states[8] = 0.2
    constants[41] = 0.47
    constants[42] = 0.6
    constants[43] = 0.2
    constants[44] = 1.63
    constants[45] = 1.63
    constants[46] = 1.0
    states[9] = 0.3
    constants[47] = 0.6
    constants[48] = 0.2
    constants[49] = 2.0
    constants[50] = 2.0
    constants[51] = 1.63
    constants[52] = 0.52
    constants[53] = 0.3
    constants[54] = 0.2
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[0] = (constants[1]+constants[2]*((power(states[2]/constants[6], constants[8])+constants[0])/(1.00000+power(states[1]/constants[5], constants[9])+power(states[2]/constants[6], constants[8])+constants[0])))-(constants[3]*(states[0]/(constants[4]+states[0]))+constants[7]*states[0])
    rates[3] = (constants[10]*states[0]+constants[15]*states[5])-(constants[14]*states[3]*states[4]+constants[11]*constants[13]*(states[3]/(constants[12]+states[3]))+constants[7]*states[3])
    rates[6] = (constants[17]+constants[18]*((power(states[2]/constants[22], constants[8])+constants[16])/(1.00000+power(states[1]/constants[21], constants[9])+power(states[2]/constants[22], constants[8])+constants[16])))-(constants[19]*(states[6]/(constants[20]+states[6]))+constants[7]*states[6])
    rates[4] = (constants[23]*states[6]+constants[15]*states[5])-(constants[14]*states[3]*states[4]+constants[24]*(states[4]/(constants[25]+states[4]))+constants[7]*states[4])
    rates[5] = (constants[14]*states[3]*states[4]+constants[31]*(states[1]/(constants[29]+states[1])))-(constants[15]*states[5]+constants[30]*(states[5]/(constants[28]+states[5]))+constants[26]*(states[5]/(constants[27]+states[5]))+constants[7]*states[5])
    rates[1] = constants[30]*(states[5]/(constants[28]+states[5]))-(constants[31]*(states[1]/(constants[29]+states[1]))+constants[32]*(states[1]/(constants[33]+states[1]))+constants[7]*states[1])
    rates[7] = (constants[35]+constants[36]*((power(states[1]/constants[40], constants[8])+constants[34])/(1.00000+power(states[2]/constants[39], constants[9])+power(states[1]/constants[40], constants[8])+constants[34])))-(constants[37]*(states[7]/(constants[38]+states[7]))+constants[7]*states[7])
    rates[8] = (constants[41]*states[7]+constants[45]*states[9])-(constants[44]*states[8]*constants[46]+constants[42]*(states[8]/(constants[43]+states[8]))+constants[7]*states[8])
    rates[9] = (constants[44]*states[8]*constants[46]+constants[52]*(states[2]/(constants[50]+states[2])))-(constants[45]*states[9]+constants[51]*(states[9]/(constants[49]+states[9]))+constants[47]*(states[9]/(constants[48]+states[9]))+constants[7]*states[9])
    rates[2] = constants[51]*(states[9]/(constants[49]+states[9]))-(constants[52]*(states[2]/(constants[50]+states[2]))+constants[53]*(states[2]/(constants[54]+states[2]))+constants[7]*states[2])
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
        self.B1 = 0.0
        self.C1 = 0.0
        self.S1 = 1.45
        self.D1 = 0.94
        self.L1 = 0.3
        self.R1 = 1.02
        self.A1 = 0.45
        self.D0 = 0.012
        self.a = 1.0
        self.r = 4.0
        self.S2 = 0.48
        self.D2 = 0.44
        self.L2 = 0.2
        self.Dbt_c = 1.0
        self.V1 = 1.45
        self.V2 = 1.45
        self.B2 = 0.0
        self.C2 = 0.0
        self.S3 = 1.45
        self.D3 = 0.94
        self.L3 = 0.3
        self.R2 = 1.02
        self.A2 = 0.45
        self.S4 = 0.48
        self.D4 = 0.44
        self.L4 = 0.2
        self.D5 = 0.44
        self.L5 = 0.2
        self.K1 = 2.0
        self.K2 = 2.0
        self.T1 = 1.73
        self.T2 = 0.72
        self.D6 = 0.29
        self.L6 = 0.2
        self.B3 = 0.6
        self.C3 = 0.0
        self.S5 = 1.63
        self.D7 = 0.54
        self.L7 = 0.13
        self.R3 = 0.89
        self.A3 = 0.8
        self.S6 = 0.47
        self.D8 = 0.6
        self.L8 = 0.2
        self.V3 = 1.63
        self.V4 = 1.63
        self.Cyc_c = 1.0
        self.D9 = 0.6
        self.L9 = 0.2
        self.K3 = 2.0
        self.K4 = 2.0
        self.T3 = 1.63
        self.T4 = 0.52
        self.D10 = 0.3
        self.L10 = 0.2

    def to_dict(self):
        return {
            "B1": self.B1,
            "C1": self.C1,
            "S1": self.S1,
            "D1": self.D1,
            "L1": self.L1,
            "R1": self.R1,
            "A1": self.A1,
            "D0": self.D0,
            "a": self.a,
            "r": self.r,
            "S2": self.S2,
            "D2": self.D2,
            "L2": self.L2,
            "Dbt_c": self.Dbt_c,
            "V1": self.V1,
            "V2": self.V2,
            "B2": self.B2,
            "C2": self.C2,
            "S3": self.S3,
            "D3": self.D3,
            "L3": self.L3,
            "R2": self.R2,
            "A2": self.A2,
            "S4": self.S4,
            "D4": self.D4,
            "L4": self.L4,
            "D5": self.D5,
            "L5": self.L5,
            "K1": self.K1,
            "K2": self.K2,
            "T1": self.T1,
            "T2": self.T2,
            "D6": self.D6,
            "L6": self.L6,
            "B3": self.B3,
            "C3": self.C3,
            "S5": self.S5,
            "D7": self.D7,
            "L7": self.L7,
            "R3": self.R3,
            "A3": self.A3,
            "S6": self.S6,
            "D8": self.D8,
            "L8": self.L8,
            "V3": self.V3,
            "V4": self.V4,
            "Cyc_c": self.Cyc_c,
            "D9": self.D9,
            "L9": self.L9,
            "K3": self.K3,
            "K4": self.K4,
            "T3": self.T3,
            "T4": self.T4,
            "D10": self.D10,
            "L10": self.L10,
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
        y0=[0.5, 1.0, 0.4, 0.6, 0.8, 0.9, 0.7, 0.1, 0.2, 0.3],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "ueda_hagiwara_kitano_2001"
        self.curve_names = [
            "Per_m",
            "PT_n",
            "CC_n",
            "Per_c",
            "Tim_c",
            "PT_c",
            "Tim_m",
            "Clk_m",
            "Clk_c",
            "CC_c",
        ]
        self.state_names = ['Per_m', 'PT_n', 'CC_n', 'Per_c', 'Tim_c', 'PT_c', 'Tim_m', 'Clk_m', 'Clk_c', 'CC_c']
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
        c = [0.0] * 55
        p = self.params

        # direct mapping
        c[0] = p.B1
        c[1] = p.C1
        c[2] = p.S1
        c[3] = p.D1
        c[4] = p.L1
        c[5] = p.R1
        c[6] = p.A1
        c[7] = p.D0
        c[8] = p.a
        c[9] = p.r
        c[10] = p.S2
        c[11] = p.D2
        c[12] = p.L2
        c[13] = p.Dbt_c
        c[14] = p.V1
        c[15] = p.V2
        c[16] = p.B2
        c[17] = p.C2
        c[18] = p.S3
        c[19] = p.D3
        c[20] = p.L3
        c[21] = p.R2
        c[22] = p.A2
        c[23] = p.S4
        c[24] = p.D4
        c[25] = p.L4
        c[26] = p.D5
        c[27] = p.L5
        c[28] = p.K1
        c[29] = p.K2
        c[30] = p.T1
        c[31] = p.T2
        c[32] = p.D6
        c[33] = p.L6
        c[34] = p.B3
        c[35] = p.C3
        c[36] = p.S5
        c[37] = p.D7
        c[38] = p.L7
        c[39] = p.R3
        c[40] = p.A3
        c[41] = p.S6
        c[42] = p.D8
        c[43] = p.L8
        c[44] = p.V3
        c[45] = p.V4
        c[46] = p.Cyc_c
        c[47] = p.D9
        c[48] = p.L9
        c[49] = p.K3
        c[50] = p.K4
        c[51] = p.T3
        c[52] = p.T4
        c[53] = p.D10
        c[54] = p.L10

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
