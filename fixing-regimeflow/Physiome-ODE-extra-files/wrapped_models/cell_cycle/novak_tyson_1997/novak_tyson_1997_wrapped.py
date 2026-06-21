# Size of variable arrays:
sizeAlgebraic = 9
sizeStates = 13
sizeConstants = 43
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (minute)"
    legend_constants[0] = "k1 in component rate_constants (first_order_rate_constant)"
    legend_algebraic[1] = "k2 in component rate_constants (first_order_rate_constant)"
    legend_constants[1] = "k2_ in component rate_constants (first_order_rate_constant)"
    legend_constants[2] = "k3 in component rate_constants (first_order_rate_constant)"
    legend_constants[3] = "k4 in component rate_constants (first_order_rate_constant)"
    legend_constants[4] = "k5 in component rate_constants (first_order_rate_constant)"
    legend_algebraic[0] = "k6 in component rate_constants (first_order_rate_constant)"
    legend_constants[5] = "k6_ in component rate_constants (first_order_rate_constant)"
    legend_constants[6] = "k7 in component rate_constants (first_order_rate_constant)"
    legend_constants[7] = "k7r in component rate_constants (first_order_rate_constant)"
    legend_constants[8] = "k8 in component rate_constants (first_order_rate_constant)"
    legend_constants[9] = "k8r in component rate_constants (first_order_rate_constant)"
    legend_algebraic[5] = "kwee in component rate_constants (first_order_rate_constant)"
    legend_algebraic[7] = "k25 in component rate_constants (first_order_rate_constant)"
    legend_constants[10] = "ku in component rate_constants (first_order_rate_constant)"
    legend_constants[11] = "kp in component rate_constants (first_order_rate_constant)"
    legend_constants[12] = "kur in component rate_constants (first_order_rate_constant)"
    legend_constants[13] = "ku2 in component rate_constants (first_order_rate_constant)"
    legend_constants[14] = "kur2 in component rate_constants (first_order_rate_constant)"
    legend_constants[15] = "kc in component rate_constants (first_order_rate_constant)"
    legend_constants[16] = "kcr in component rate_constants (first_order_rate_constant)"
    legend_constants[17] = "kw in component rate_constants (first_order_rate_constant)"
    legend_constants[18] = "kwr in component rate_constants (first_order_rate_constant)"
    legend_constants[19] = "ki in component rate_constants (first_order_rate_constant)"
    legend_constants[20] = "kir in component rate_constants (first_order_rate_constant)"
    legend_constants[21] = "mu in component rate_constants (first_order_rate_constant)"
    legend_constants[22] = "Kmu2 in component rate_constants (dimensionless)"
    legend_constants[23] = "Kmur2 in component rate_constants (dimensionless)"
    legend_constants[24] = "Kmi in component rate_constants (dimensionless)"
    legend_constants[25] = "Kmir in component rate_constants (dimensionless)"
    legend_constants[26] = "Kmw in component rate_constants (dimensionless)"
    legend_constants[27] = "Kmwr in component rate_constants (dimensionless)"
    legend_constants[28] = "Kmu in component rate_constants (dimensionless)"
    legend_constants[29] = "Kmur in component rate_constants (dimensionless)"
    legend_constants[30] = "Kmc in component rate_constants (dimensionless)"
    legend_constants[31] = "Kmcr in component rate_constants (dimensionless)"
    legend_constants[32] = "Kmp in component rate_constants (dimensionless)"
    legend_constants[33] = "V2 in component rate_constants (first_order_rate_constant)"
    legend_constants[34] = "V2_ in component rate_constants (first_order_rate_constant)"
    legend_constants[35] = "V6 in component rate_constants (first_order_rate_constant)"
    legend_constants[36] = "V6_ in component rate_constants (first_order_rate_constant)"
    legend_constants[37] = "V25 in component rate_constants (first_order_rate_constant)"
    legend_constants[38] = "V25_ in component rate_constants (first_order_rate_constant)"
    legend_constants[39] = "Vw in component rate_constants (first_order_rate_constant)"
    legend_constants[40] = "Vw_ in component rate_constants (first_order_rate_constant)"
    legend_states[0] = "Cdc25 in component Cdc25 (dimensionless)"
    legend_states[1] = "UbE in component UbE (dimensionless)"
    legend_states[2] = "UbE2 in component UbE2 (dimensionless)"
    legend_states[3] = "Wee1 in component Wee1 (dimensionless)"
    legend_algebraic[8] = "SPF in component concentration_variables (dimensionless)"
    legend_algebraic[6] = "MPF in component concentration_variables (dimensionless)"
    legend_constants[41] = "alpha in component concentration_variables (dimensionless)"
    legend_constants[42] = "beta in component concentration_variables (dimensionless)"
    legend_states[4] = "G1K in component G1K (dimensionless)"
    legend_states[5] = "G2K in component G2K (dimensionless)"
    legend_states[6] = "PG2 in component PG2 (dimensionless)"
    legend_states[7] = "G2R in component G2R (dimensionless)"
    legend_states[8] = "R in component R (dimensionless)"
    legend_states[9] = "G1R in component G1R (dimensionless)"
    legend_states[10] = "PG2R in component PG2R (dimensionless)"
    legend_states[11] = "mass in component mass (dimensionless)"
    legend_states[12] = "IE in component IE (dimensionless)"
    legend_algebraic[2] = "Cig2_total in component Cig2_total (dimensionless)"
    legend_algebraic[3] = "Rum1_total in component Rum1_total (dimensionless)"
    legend_algebraic[4] = "Cdc13_total in component Cdc13_total (dimensionless)"
    legend_rates[5] = "d/dt G2K in component G2K (dimensionless)"
    legend_rates[8] = "d/dt R in component R (dimensionless)"
    legend_rates[4] = "d/dt G1K in component G1K (dimensionless)"
    legend_rates[7] = "d/dt G2R in component G2R (dimensionless)"
    legend_rates[12] = "d/dt IE in component IE (dimensionless)"
    legend_rates[2] = "d/dt UbE2 in component UbE2 (dimensionless)"
    legend_rates[3] = "d/dt Wee1 in component Wee1 (dimensionless)"
    legend_rates[6] = "d/dt PG2 in component PG2 (dimensionless)"
    legend_rates[9] = "d/dt G1R in component G1R (dimensionless)"
    legend_rates[10] = "d/dt PG2R in component PG2R (dimensionless)"
    legend_rates[1] = "d/dt UbE in component UbE (dimensionless)"
    legend_rates[11] = "d/dt mass in component mass (dimensionless)"
    legend_rates[0] = "d/dt Cdc25 in component Cdc25 (dimensionless)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    constants[0] = 0.015
    constants[1] = 0.05
    constants[2] = 0.09375
    constants[3] = 0.1875
    constants[4] = 0.00175
    constants[5] = 0
    constants[6] = 100
    constants[7] = 0.1
    constants[8] = 10
    constants[9] = 0.1
    constants[10] = 0.2
    constants[11] = 3.25
    constants[12] = 0.1
    constants[13] = 1
    constants[14] = 0.3
    constants[15] = 1
    constants[16] = 0.25
    constants[17] = 1
    constants[18] = 0.25
    constants[19] = 0.4
    constants[20] = 0.1
    constants[21] = 0.00495
    constants[22] = 0.05
    constants[23] = 0.05
    constants[24] = 0.01
    constants[25] = 0.01
    constants[26] = 0.1
    constants[27] = 0.1
    constants[28] = 0.01
    constants[29] = 0.01
    constants[30] = 0.1
    constants[31] = 0.1
    constants[32] = 0.001
    constants[33] = 0.25
    constants[34] = 0.0075
    constants[35] = 7.5
    constants[36] = 0.0375
    constants[37] = 0.5
    constants[38] = 0.025
    constants[39] = 0.35
    constants[40] = 0.035
    states[0] = 0
    states[1] = 1
    states[2] = 0
    states[3] = 0
    constants[41] = 0.25
    constants[42] = 0.05
    states[4] = 0
    states[5] = 0
    states[6] = 0
    states[7] = 0
    states[8] = 0.4
    states[9] = 0
    states[10] = 0
    states[11] = 0.5
    states[12] = 0
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[9] = constants[8]*states[8]*states[4]-(constants[9]+constants[3]+constants[5])*states[9]
    rates[1] = (constants[10]*states[12]*(1.00000-states[1]))/((constants[28]+1.00000)-states[1])-(constants[12]*states[1])/(constants[29]+states[1])
    rates[11] = constants[21]*states[11]
    algebraic[0] = constants[36]*(1.00000-states[2])+constants[35]*states[2]
    rates[4] = (constants[4]+(constants[9]+constants[3])*states[9])-(algebraic[0]+constants[8]*states[8])*states[4]
    algebraic[1] = constants[34]*(1.00000-states[1])+constants[33]*states[1]
    rates[7] = constants[6]*states[8]*states[5]-(constants[7]+constants[3]+algebraic[1]+constants[1])*states[7]
    rates[10] = constants[6]*states[8]*states[6]-(constants[7]+constants[3]+algebraic[1]+constants[1])*states[10]
    algebraic[6] = states[5]+constants[42]*states[6]
    rates[12] = (constants[19]*algebraic[6]*(1.00000-states[12]))/((constants[24]+1.00000)-states[12])-(constants[20]*states[12])/(constants[25]+states[12])
    rates[2] = (constants[13]*algebraic[6]*(1.00000-states[2]))/((constants[22]+1.00000)-states[2])-(constants[14]*states[2])/(constants[23]+states[2])
    rates[3] = (constants[18]*(1.00000-states[3]))/((constants[27]+1.00000)-states[3])-(constants[17]*algebraic[6]*states[3])/(constants[26]+states[3])
    rates[0] = (constants[15]*algebraic[6]*(1.00000-states[0]))/((constants[30]+1.00000)-states[0])-(constants[16]*states[0])/(constants[31]+states[0])
    algebraic[5] = constants[40]*(1.00000-states[3])+constants[39]*states[3]
    algebraic[7] = constants[38]*(1.00000-states[0])+constants[37]*states[0]
    rates[5] = (constants[0]+algebraic[7]*states[6]+(constants[7]+constants[3])*states[7])-(algebraic[1]+algebraic[5]+constants[6]*states[8])*states[5]
    algebraic[8] = algebraic[6]+constants[41]*states[4]
    rates[8] = (constants[2]+(constants[7]+algebraic[1]+constants[1])*(states[7]+states[10])+(constants[9]+constants[5])*states[9])-(constants[3]*states[8]+constants[6]*states[8]*(states[5]+states[6])+constants[8]*states[8]*states[4]+(constants[11]*states[8]*algebraic[8]*states[11])/(constants[32]+states[8]))
    rates[6] = (algebraic[5]*states[5]+(constants[7]+constants[3])*states[10])-(algebraic[7]+algebraic[1]+constants[6]*states[8])*states[6]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = constants[36]*(1.00000-states[2])+constants[35]*states[2]
    algebraic[1] = constants[34]*(1.00000-states[1])+constants[33]*states[1]
    algebraic[6] = states[5]+constants[42]*states[6]
    algebraic[5] = constants[40]*(1.00000-states[3])+constants[39]*states[3]
    algebraic[7] = constants[38]*(1.00000-states[0])+constants[37]*states[0]
    algebraic[8] = algebraic[6]+constants[41]*states[4]
    algebraic[2] = states[4]+states[9]
    algebraic[3] = states[8]+states[9]+states[7]+states[10]
    algebraic[4] = states[5]+states[7]+states[6]+states[10]
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
        self.k1 = 0.015
        self.k2_ = 0.05
        self.k3 = 0.09375
        self.k4 = 0.1875
        self.k5 = 0.00175
        self.k6_ = 0
        self.k7 = 100
        self.k7r = 0.1
        self.k8 = 10
        self.k8r = 0.1
        self.ku = 0.2
        self.kp = 3.25
        self.kur = 0.1
        self.ku2 = 1
        self.kur2 = 0.3
        self.kc = 1
        self.kcr = 0.25
        self.kw = 1
        self.kwr = 0.25
        self.ki = 0.4
        self.kir = 0.1
        self.mu = 0.00495
        self.Kmu2 = 0.05
        self.Kmur2 = 0.05
        self.Kmi = 0.01
        self.Kmir = 0.01
        self.Kmw = 0.1
        self.Kmwr = 0.1
        self.Kmu = 0.01
        self.Kmur = 0.01
        self.Kmc = 0.1
        self.Kmcr = 0.1
        self.Kmp = 0.001
        self.V2 = 0.25
        self.V2_ = 0.0075
        self.V6 = 7.5
        self.V6_ = 0.0375
        self.V25 = 0.5
        self.V25_ = 0.025
        self.Vw = 0.35
        self.Vw_ = 0.035
        self.alpha = 0.25
        self.beta = 0.05

    def to_dict(self):
        return {
            "k1": self.k1,
            "k2_": self.k2_,
            "k3": self.k3,
            "k4": self.k4,
            "k5": self.k5,
            "k6_": self.k6_,
            "k7": self.k7,
            "k7r": self.k7r,
            "k8": self.k8,
            "k8r": self.k8r,
            "ku": self.ku,
            "kp": self.kp,
            "kur": self.kur,
            "ku2": self.ku2,
            "kur2": self.kur2,
            "kc": self.kc,
            "kcr": self.kcr,
            "kw": self.kw,
            "kwr": self.kwr,
            "ki": self.ki,
            "kir": self.kir,
            "mu": self.mu,
            "Kmu2": self.Kmu2,
            "Kmur2": self.Kmur2,
            "Kmi": self.Kmi,
            "Kmir": self.Kmir,
            "Kmw": self.Kmw,
            "Kmwr": self.Kmwr,
            "Kmu": self.Kmu,
            "Kmur": self.Kmur,
            "Kmc": self.Kmc,
            "Kmcr": self.Kmcr,
            "Kmp": self.Kmp,
            "V2": self.V2,
            "V2_": self.V2_,
            "V6": self.V6,
            "V6_": self.V6_,
            "V25": self.V25,
            "V25_": self.V25_,
            "Vw": self.Vw,
            "Vw_": self.Vw_,
            "alpha": self.alpha,
            "beta": self.beta,
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
        y0=[0, 1, 0, 0, 0, 0, 0, 0, 0.4, 0, 0, 0.5, 0],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "novak_tyson_1997"
        self.curve_names = [
            "Cdc25",
            "UbE",
            "UbE2",
            "Wee1",
            "G1K",
            "G2K",
            "PG2",
            "G2R",
            "R",
            "G1R",
            "PG2R",
            "mass",
            "IE",
        ]
        self.state_names = ['Cdc25', 'UbE', 'UbE2', 'Wee1', 'G1K', 'G2K', 'PG2', 'G2R', 'R', 'G1R', 'PG2R', 'mass', 'IE']
        self.algebraic_names = ['k6', 'k2', 'Cig2_total', 'Rum1_total', 'Cdc13_total', 'kwee', 'MPF', 'k25', 'SPF']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 43
        p = self.params

        # direct mapping
        c[0] = p.k1
        c[1] = p.k2_
        c[2] = p.k3
        c[3] = p.k4
        c[4] = p.k5
        c[5] = p.k6_
        c[6] = p.k7
        c[7] = p.k7r
        c[8] = p.k8
        c[9] = p.k8r
        c[10] = p.ku
        c[11] = p.kp
        c[12] = p.kur
        c[13] = p.ku2
        c[14] = p.kur2
        c[15] = p.kc
        c[16] = p.kcr
        c[17] = p.kw
        c[18] = p.kwr
        c[19] = p.ki
        c[20] = p.kir
        c[21] = p.mu
        c[22] = p.Kmu2
        c[23] = p.Kmur2
        c[24] = p.Kmi
        c[25] = p.Kmir
        c[26] = p.Kmw
        c[27] = p.Kmwr
        c[28] = p.Kmu
        c[29] = p.Kmur
        c[30] = p.Kmc
        c[31] = p.Kmcr
        c[32] = p.Kmp
        c[33] = p.V2
        c[34] = p.V2_
        c[35] = p.V6
        c[36] = p.V6_
        c[37] = p.V25
        c[38] = p.V25_
        c[39] = p.Vw
        c[40] = p.Vw_
        c[41] = p.alpha
        c[42] = p.beta

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
