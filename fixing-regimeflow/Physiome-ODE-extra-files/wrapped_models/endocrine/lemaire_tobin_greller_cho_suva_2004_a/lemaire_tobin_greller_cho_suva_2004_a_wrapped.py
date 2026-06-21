# Size of variable arrays:
sizeAlgebraic = 3
sizeStates = 3
sizeConstants = 28
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (day)"
    legend_states[0] = "R in component R (picomolar)"
    legend_algebraic[0] = "f in component R (flux)"
    legend_constants[0] = "DR in component model_parameters (flux)"
    legend_algebraic[2] = "pi_C in component model_parameters (dimensionless)"
    legend_constants[23] = "DB in component model_parameters (first_order_rate_constant)"
    legend_states[1] = "B in component B (picomolar)"
    legend_constants[1] = "kB in component model_parameters (first_order_rate_constant)"
    legend_states[2] = "C in component C (picomolar)"
    legend_constants[2] = "DC in component model_parameters (flux)"
    legend_algebraic[1] = "pi_L in component pi_L (dimensionless)"
    legend_constants[3] = "DA in component model_parameters (first_order_rate_constant)"
    legend_constants[4] = "k1 in component pi_L (second_order_rate_constant)"
    legend_constants[5] = "k2 in component pi_L (first_order_rate_constant)"
    legend_constants[6] = "k3 in component pi_L (second_order_rate_constant)"
    legend_constants[7] = "k4 in component pi_L (first_order_rate_constant)"
    legend_constants[8] = "K in component pi_L (picomolar)"
    legend_constants[9] = "ko in component pi_L (first_order_rate_constant)"
    legend_constants[10] = "Io in component pi_L (flux)"
    legend_constants[11] = "IL in component pi_L (flux)"
    legend_constants[12] = "rL in component pi_L (flux)"
    legend_constants[13] = "KOP in component pi_L (picomole_per_day_per_picomole_cells)"
    legend_constants[14] = "KLP in component pi_L (picomole_per_picomole_cells)"
    legend_constants[27] = "pi_P in component model_parameters (dimensionless)"
    legend_constants[15] = "f0 in component model_parameters (dimensionless)"
    legend_constants[16] = "dB in component model_parameters (first_order_rate_constant)"
    legend_constants[17] = "IP in component model_parameters (flux)"
    legend_constants[18] = "kP in component model_parameters (first_order_rate_constant)"
    legend_constants[24] = "P in component model_parameters (picomolar)"
    legend_constants[25] = "P_0 in component model_parameters (picomolar)"
    legend_constants[26] = "P_s in component model_parameters (picomolar)"
    legend_constants[19] = "C_s in component model_parameters (picomolar)"
    legend_constants[20] = "SP in component model_parameters (flux)"
    legend_constants[21] = "k5 in component model_parameters (second_order_rate_constant)"
    legend_constants[22] = "k6 in component model_parameters (first_order_rate_constant)"
    legend_rates[0] = "d/dt R in component R (picomolar)"
    legend_rates[1] = "d/dt B in component B (picomolar)"
    legend_rates[2] = "d/dt C in component C (picomolar)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 0.00077
    constants[0] = 7e-4
    states[1] = 0.00073
    constants[1] = 0.189
    states[2] = 0.00091
    constants[2] = 2.1e-3
    constants[3] = 0.7
    constants[4] = 1e-2
    constants[5] = 10
    constants[6] = 5.8e-4
    constants[7] = 1.7e-2
    constants[8] = 10
    constants[9] = 0.35
    constants[10] = 0
    constants[11] = 0
    constants[12] = 1e3
    constants[13] = 2e5
    constants[14] = 3e6
    constants[15] = 0.05
    constants[16] = 0.7
    constants[17] = 0
    constants[18] = 86
    constants[19] = 5e-3
    constants[20] = 250
    constants[21] = 0.02
    constants[22] = 3
    constants[23] = constants[15]*constants[16]
    constants[24] = constants[17]/constants[18]
    constants[25] = constants[20]/constants[18]
    constants[26] = constants[22]/constants[21]
    constants[27] = (constants[24]+constants[25])/(constants[24]+constants[26])
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[0] = custom_piecewise([greater(voi , 20.0000) & less_equal(voi , 80.0000), 0.000100000 , True, 0.00000])
    algebraic[2] = (states[2]+constants[15]*constants[19])/(states[2]+constants[19])
    rates[0] = (constants[0]*algebraic[2]-(constants[23]/algebraic[2])*states[0])+algebraic[0]
    rates[1] = (constants[23]/algebraic[2])*states[0]-constants[1]*states[1]
    algebraic[1] = (((constants[6]/constants[7])*(constants[14]/1.00000)*constants[27]*states[1])/(1.00000+(constants[6]*constants[8])/constants[7]+(constants[4]/(constants[5]*constants[9]))*((constants[13]/(1.00000*constants[27]))*states[0]+constants[10])))*(1.00000+constants[11]/constants[12])
    rates[2] = constants[2]*algebraic[1]-constants[3]*algebraic[2]*states[2]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = custom_piecewise([greater(voi , 20.0000) & less_equal(voi , 80.0000), 0.000100000 , True, 0.00000])
    algebraic[2] = (states[2]+constants[15]*constants[19])/(states[2]+constants[19])
    algebraic[1] = (((constants[6]/constants[7])*(constants[14]/1.00000)*constants[27]*states[1])/(1.00000+(constants[6]*constants[8])/constants[7]+(constants[4]/(constants[5]*constants[9]))*((constants[13]/(1.00000*constants[27]))*states[0]+constants[10])))*(1.00000+constants[11]/constants[12])
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
        self.DR = 7e-4
        self.kB = 0.189
        self.DC = 2.1e-3
        self.DA = 0.7
        self.k1 = 1e-2
        self.k2 = 10
        self.k3 = 5.8e-4
        self.k4 = 1.7e-2
        self.K = 10
        self.ko = 0.35
        self.Io = 0
        self.IL = 0
        self.rL = 1e3
        self.KOP = 2e5
        self.KLP = 3e6
        self.f0 = 0.05
        self.dB = 0.7
        self.IP = 0
        self.kP = 86
        self.C_s = 5e-3
        self.SP = 250
        self.k5 = 0.02
        self.k6 = 3

    def to_dict(self):
        return {
            "DR": self.DR,
            "kB": self.kB,
            "DC": self.DC,
            "DA": self.DA,
            "k1": self.k1,
            "k2": self.k2,
            "k3": self.k3,
            "k4": self.k4,
            "K": self.K,
            "ko": self.ko,
            "Io": self.Io,
            "IL": self.IL,
            "rL": self.rL,
            "KOP": self.KOP,
            "KLP": self.KLP,
            "f0": self.f0,
            "dB": self.dB,
            "IP": self.IP,
            "kP": self.kP,
            "C_s": self.C_s,
            "SP": self.SP,
            "k5": self.k5,
            "k6": self.k6,
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
        y0=[0.00077, 0.00073, 0.00091],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "lemaire_tobin_greller_cho_suva_2004_a"
        self.curve_names = [
            "R",
            "B",
            "C",
        ]
        self.state_names = ['R', 'B', 'C']
        self.algebraic_names = ['f', 'pi_L', 'pi_C']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 28
        p = self.params

        # direct mapping
        c[0] = p.DR
        c[1] = p.kB
        c[2] = p.DC
        c[3] = p.DA
        c[4] = p.k1
        c[5] = p.k2
        c[6] = p.k3
        c[7] = p.k4
        c[8] = p.K
        c[9] = p.ko
        c[10] = p.Io
        c[11] = p.IL
        c[12] = p.rL
        c[13] = p.KOP
        c[14] = p.KLP
        c[15] = p.f0
        c[16] = p.dB
        c[17] = p.IP
        c[18] = p.kP
        c[19] = p.C_s
        c[20] = p.SP
        c[21] = p.k5
        c[22] = p.k6

        # derived constants
        c[23] = c[15]*c[16]
        c[24] = c[17]/c[18]
        c[25] = c[20]/c[18]
        c[26] = c[22]/c[21]
        c[27] = (c[24]+c[25])/(c[24]+c[26])

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
