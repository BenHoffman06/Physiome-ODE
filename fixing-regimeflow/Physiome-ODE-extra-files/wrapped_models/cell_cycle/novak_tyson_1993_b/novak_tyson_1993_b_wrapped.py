# Size of variable arrays:
sizeAlgebraic = 5
sizeStates = 9
sizeConstants = 31
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (minute)"
    legend_constants[0] = "k1AA in component rate_constants (first_order_rate_constant)"
    legend_constants[1] = "k3 in component rate_constants (first_order_rate_constant)"
    legend_constants[2] = "kinh in component rate_constants (first_order_rate_constant)"
    legend_constants[3] = "kcak in component rate_constants (first_order_rate_constant)"
    legend_constants[4] = "kbPPase in component rate_constants (first_order_rate_constant)"
    legend_constants[5] = "kfPPase in component rate_constants (first_order_rate_constant)"
    legend_constants[6] = "khPPase in component rate_constants (first_order_rate_constant)"
    legend_constants[7] = "kd_antiIE in component rate_constants (first_order_rate_constant)"
    legend_constants[8] = "ka in component rate_constants (first_order_rate_constant)"
    legend_constants[9] = "kc in component rate_constants (first_order_rate_constant)"
    legend_constants[10] = "ke in component rate_constants (first_order_rate_constant)"
    legend_constants[11] = "kg in component rate_constants (first_order_rate_constant)"
    legend_constants[12] = "V2_ in component rate_constants (first_order_rate_constant)"
    legend_constants[13] = "V2__ in component rate_constants (first_order_rate_constant)"
    legend_constants[14] = "V25_ in component rate_constants (first_order_rate_constant)"
    legend_constants[15] = "V25__ in component rate_constants (first_order_rate_constant)"
    legend_constants[16] = "Vwee_ in component rate_constants (first_order_rate_constant)"
    legend_constants[17] = "Vwee__ in component rate_constants (first_order_rate_constant)"
    legend_constants[18] = "K_a in component rate_constants (dimensionless)"
    legend_constants[19] = "K_b in component rate_constants (dimensionless)"
    legend_constants[20] = "K_c in component rate_constants (dimensionless)"
    legend_constants[21] = "K_d in component rate_constants (dimensionless)"
    legend_constants[22] = "K_e in component rate_constants (dimensionless)"
    legend_constants[23] = "K_f in component rate_constants (dimensionless)"
    legend_constants[24] = "K_g in component rate_constants (dimensionless)"
    legend_constants[25] = "K_h in component rate_constants (dimensionless)"
    legend_constants[26] = "Cdc25_T in component concentration_variables (dimensionless)"
    legend_states[0] = "Cdc25_P in component Cdc25_P (dimensionless)"
    legend_states[1] = "Wee1_P in component Wee1_P (dimensionless)"
    legend_constants[27] = "Wee1_T in component concentration_variables (dimensionless)"
    legend_constants[28] = "UbE_T in component concentration_variables (dimensionless)"
    legend_states[2] = "UbE in component UbE (dimensionless)"
    legend_algebraic[0] = "k25 in component rate_constants (first_order_rate_constant)"
    legend_algebraic[2] = "kwee in component rate_constants (first_order_rate_constant)"
    legend_algebraic[3] = "k2 in component rate_constants (first_order_rate_constant)"
    legend_constants[29] = "Cdc2_T in component concentration_variables (dimensionless)"
    legend_constants[30] = "IE_T in component concentration_variables (dimensionless)"
    legend_states[3] = "cyclin in component cyclin (dimensionless)"
    legend_algebraic[4] = "Cdc2 in component Cdc2 (dimensionless)"
    legend_states[4] = "cyclin_Cdc2 in component cyclin_Cdc2 (dimensionless)"
    legend_states[5] = "MPF_active in component MPF_active (dimensionless)"
    legend_states[6] = "Tyr15P_dimer in component Tyr15P_dimer (dimensionless)"
    legend_states[7] = "MPF_pre in component MPF_pre (dimensionless)"
    legend_algebraic[1] = "cyclin_T in component cyclin_T (dimensionless)"
    legend_states[8] = "IE_P in component IE_P (dimensionless)"
    legend_rates[3] = "d/dt cyclin in component cyclin (dimensionless)"
    legend_rates[4] = "d/dt cyclin_Cdc2 in component cyclin_Cdc2 (dimensionless)"
    legend_rates[6] = "d/dt Tyr15P_dimer in component Tyr15P_dimer (dimensionless)"
    legend_rates[7] = "d/dt MPF_pre in component MPF_pre (dimensionless)"
    legend_rates[5] = "d/dt MPF_active in component MPF_active (dimensionless)"
    legend_rates[0] = "d/dt Cdc25_P in component Cdc25_P (dimensionless)"
    legend_rates[1] = "d/dt Wee1_P in component Wee1_P (dimensionless)"
    legend_rates[8] = "d/dt IE_P in component IE_P (dimensionless)"
    legend_rates[2] = "d/dt UbE in component UbE (dimensionless)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    constants[0] = 1
    constants[1] = 0.01
    constants[2] = 0.025
    constants[3] = 0.25
    constants[4] = 0.125
    constants[5] = 0.1
    constants[6] = 0.087
    constants[7] = 0.095
    constants[8] = 0.01
    constants[9] = 0.1
    constants[10] = 0.0133
    constants[11] = 0.0065
    constants[12] = 0.015
    constants[13] = 1
    constants[14] = 0.1
    constants[15] = 2
    constants[16] = 0.1
    constants[17] = 1
    constants[18] = 0.1
    constants[19] = 0.1
    constants[20] = 0.01
    constants[21] = 0.01
    constants[22] = 0.3
    constants[23] = 0.3
    constants[24] = 0.01
    constants[25] = 0.01
    constants[26] = 1
    states[0] = 0
    states[1] = 0
    constants[27] = 1
    constants[28] = 1
    states[2] = 0
    constants[29] = 100
    constants[30] = 1
    states[3] = 1
    states[4] = 0
    states[5] = 0
    states[6] = 0
    states[7] = 0
    states[8] = 0
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[0] = (constants[8]*states[5]*(constants[26]-states[0]))/((constants[18]+constants[26])-states[0])-(constants[4]*states[0])/(constants[19]+states[0])
    rates[1] = (constants[10]*states[5]*(constants[27]-states[1]))/((constants[22]+constants[27])-states[1])-(constants[5]*states[1])/(constants[23]+states[1])
    rates[8] = (constants[11]*states[5]*(constants[30]-states[8]))/((constants[24]+constants[30])-states[8])-(constants[6]*states[8])/(constants[25]+states[8])
    rates[2] = (constants[9]*states[8]*(constants[28]-states[2]))/((constants[20]+constants[28])-states[2])-(constants[7]*states[2])/(constants[21]+states[2])
    algebraic[0] = constants[14]*(constants[26]-states[0])+constants[15]*states[0]
    algebraic[2] = constants[16]*states[1]+constants[17]*(constants[27]-states[1])
    algebraic[3] = constants[12]*(constants[28]-states[2])+constants[13]*states[2]
    rates[6] = (algebraic[2]*states[4]-(algebraic[0]+constants[3]+algebraic[3])*states[6])+constants[2]*states[7]
    rates[7] = (algebraic[2]*states[5]-(constants[2]+algebraic[0]+algebraic[3])*states[7])+constants[3]*states[6]
    rates[5] = (constants[3]*states[4]-(constants[2]+algebraic[2]+algebraic[3])*states[5])+algebraic[0]*states[7]
    algebraic[4] = constants[29]-(states[4]+states[5]+states[7]+states[6])
    rates[3] = (constants[0]-algebraic[3]*states[3])-constants[1]*states[3]*algebraic[4]
    rates[4] = (constants[2]*states[5]-(algebraic[2]+constants[3]+algebraic[3])*states[4])+algebraic[0]*states[6]+constants[1]*states[3]*algebraic[4]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = constants[14]*(constants[26]-states[0])+constants[15]*states[0]
    algebraic[2] = constants[16]*states[1]+constants[17]*(constants[27]-states[1])
    algebraic[3] = constants[12]*(constants[28]-states[2])+constants[13]*states[2]
    algebraic[4] = constants[29]-(states[4]+states[5]+states[7]+states[6])
    algebraic[1] = states[3]+states[4]+states[5]+states[7]+states[6]
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
        self.k1AA = 1
        self.k3 = 0.01
        self.kinh = 0.025
        self.kcak = 0.25
        self.kbPPase = 0.125
        self.kfPPase = 0.1
        self.khPPase = 0.087
        self.kd_antiIE = 0.095
        self.ka = 0.01
        self.kc = 0.1
        self.ke = 0.0133
        self.kg = 0.0065
        self.V2_ = 0.015
        self.V2__1 = 1
        self.V25_ = 0.1
        self.V25__1 = 2
        self.Vwee_ = 0.1
        self.Vwee__1 = 1
        self.K_a = 0.1
        self.K_b = 0.1
        self.K_c = 0.01
        self.K_d = 0.01
        self.K_e = 0.3
        self.K_f = 0.3
        self.K_g = 0.01
        self.K_h = 0.01
        self.Cdc25_T = 1
        self.Wee1_T = 1
        self.UbE_T = 1
        self.Cdc2_T = 100
        self.IE_T = 1

    def to_dict(self):
        return {
            "k1AA": self.k1AA,
            "k3": self.k3,
            "kinh": self.kinh,
            "kcak": self.kcak,
            "kbPPase": self.kbPPase,
            "kfPPase": self.kfPPase,
            "khPPase": self.khPPase,
            "kd_antiIE": self.kd_antiIE,
            "ka": self.ka,
            "kc": self.kc,
            "ke": self.ke,
            "kg": self.kg,
            "V2_": self.V2_,
            "V2__1": self.V2__1,
            "V25_": self.V25_,
            "V25__1": self.V25__1,
            "Vwee_": self.Vwee_,
            "Vwee__1": self.Vwee__1,
            "K_a": self.K_a,
            "K_b": self.K_b,
            "K_c": self.K_c,
            "K_d": self.K_d,
            "K_e": self.K_e,
            "K_f": self.K_f,
            "K_g": self.K_g,
            "K_h": self.K_h,
            "Cdc25_T": self.Cdc25_T,
            "Wee1_T": self.Wee1_T,
            "UbE_T": self.UbE_T,
            "Cdc2_T": self.Cdc2_T,
            "IE_T": self.IE_T,
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
        y0=[0, 0, 0, 1, 0, 0, 0, 0, 0],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "novak_tyson_1993_b"
        self.curve_names = [
            "Cdc25_P",
            "Wee1_P",
            "UbE",
            "cyclin",
            "cyclin_Cdc2",
            "MPF_active",
            "Tyr15P_dimer",
            "MPF_pre",
            "IE_P",
        ]
        self.state_names = ['Cdc25_P', 'Wee1_P', 'UbE', 'cyclin', 'cyclin_Cdc2', 'MPF_active', 'Tyr15P_dimer', 'MPF_pre', 'IE_P']
        self.algebraic_names = ['k25', 'cyclin_T', 'kwee', 'k2', 'Cdc2']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 31
        p = self.params

        # direct mapping
        c[0] = p.k1AA
        c[1] = p.k3
        c[2] = p.kinh
        c[3] = p.kcak
        c[4] = p.kbPPase
        c[5] = p.kfPPase
        c[6] = p.khPPase
        c[7] = p.kd_antiIE
        c[8] = p.ka
        c[9] = p.kc
        c[10] = p.ke
        c[11] = p.kg
        c[12] = p.V2_
        c[13] = p.V2__1
        c[14] = p.V25_
        c[15] = p.V25__1
        c[16] = p.Vwee_
        c[17] = p.Vwee__1
        c[18] = p.K_a
        c[19] = p.K_b
        c[20] = p.K_c
        c[21] = p.K_d
        c[22] = p.K_e
        c[23] = p.K_f
        c[24] = p.K_g
        c[25] = p.K_h
        c[26] = p.Cdc25_T
        c[27] = p.Wee1_T
        c[28] = p.UbE_T
        c[29] = p.Cdc2_T
        c[30] = p.IE_T

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
