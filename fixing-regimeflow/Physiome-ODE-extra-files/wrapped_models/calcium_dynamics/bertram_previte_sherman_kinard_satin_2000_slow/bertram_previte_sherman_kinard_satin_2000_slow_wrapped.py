# Size of variable arrays:
sizeAlgebraic = 10
sizeStates = 4
sizeConstants = 21
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (millisecond)"
    legend_constants[0] = "Cm in component membrane (femtoF)"
    legend_states[0] = "V in component membrane (millivolt)"
    legend_algebraic[4] = "ICa in component Ca_current (femtoA)"
    legend_algebraic[6] = "IK in component rapid_K_current (femtoA)"
    legend_algebraic[9] = "Il in component leak_current (femtoA)"
    legend_algebraic[7] = "Is1 in component slow_K_current (femtoA)"
    legend_algebraic[8] = "Is2 in component very_slow_K_current (femtoA)"
    legend_constants[1] = "Vm in component Ca_current (millivolt)"
    legend_constants[2] = "VCa in component Ca_current (millivolt)"
    legend_constants[3] = "gCa in component Ca_current (picoS)"
    legend_algebraic[0] = "minf in component Ca_current (dimensionless)"
    legend_constants[4] = "sm in component Ca_current (millivolt)"
    legend_constants[5] = "VK in component rapid_K_current (millivolt)"
    legend_constants[6] = "gK in component rapid_K_current (picoS)"
    legend_states[1] = "n in component rapid_K_current (dimensionless)"
    legend_constants[7] = "lambda in component rapid_K_current (dimensionless)"
    legend_constants[8] = "tnbar in component rapid_K_current (dimensionless)"
    legend_constants[9] = "Vn in component rapid_K_current (millivolt)"
    legend_constants[10] = "sn in component rapid_K_current (millivolt)"
    legend_algebraic[5] = "taun in component rapid_K_current (dimensionless)"
    legend_algebraic[1] = "ninf in component rapid_K_current (dimensionless)"
    legend_constants[11] = "gs1 in component slow_K_current (picoS)"
    legend_states[2] = "s1 in component slow_K_current (dimensionless)"
    legend_algebraic[2] = "s1inf in component slow_K_current (dimensionless)"
    legend_constants[12] = "Vs1 in component slow_K_current (millivolt)"
    legend_constants[13] = "ss1 in component slow_K_current (millivolt)"
    legend_constants[14] = "taus1 in component slow_K_current (dimensionless)"
    legend_constants[15] = "Vs2 in component very_slow_K_current (millivolt)"
    legend_states[3] = "s2 in component very_slow_K_current (dimensionless)"
    legend_algebraic[3] = "s2inf in component very_slow_K_current (dimensionless)"
    legend_constants[16] = "ss2 in component very_slow_K_current (millivolt)"
    legend_constants[17] = "gs2 in component very_slow_K_current (picoS)"
    legend_constants[18] = "taus2 in component very_slow_K_current (dimensionless)"
    legend_constants[19] = "gl in component leak_current (picoS)"
    legend_constants[20] = "Vl in component leak_current (millivolt)"
    legend_rates[0] = "d/dt V in component membrane (millivolt)"
    legend_rates[1] = "d/dt n in component rapid_K_current (dimensionless)"
    legend_rates[2] = "d/dt s1 in component slow_K_current (dimensionless)"
    legend_rates[3] = "d/dt s2 in component very_slow_K_current (dimensionless)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    constants[0] = 4524
    states[0] = -43
    constants[1] = -22
    constants[2] = 100
    constants[3] = 280
    constants[4] = 7.5
    constants[5] = -80
    constants[6] = 1300
    states[1] = 0.03
    constants[7] = 1.1
    constants[8] = 9.09
    constants[9] = -9
    constants[10] = 10
    constants[11] = 3
    states[2] = 0.1
    constants[12] = -40
    constants[13] = 0.5
    constants[14] = 1000
    constants[15] = -42
    states[3] = 0.434
    constants[16] = 0.4
    constants[17] = 32
    constants[18] = 120000
    constants[19] = 25
    constants[20] = -40
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[2] = 1.00000/(1.00000+exp((constants[12]-states[0])/constants[13]))
    rates[2] = (algebraic[2]-states[2])/(constants[14]*1.00000)
    algebraic[3] = 1.00000/(1.00000+exp((constants[15]-states[0])/constants[16]))
    rates[3] = (algebraic[3]-states[3])/(constants[18]*1.00000)
    algebraic[5] = constants[8]/(1.00000+exp((states[0]-constants[9])/constants[10]))
    algebraic[1] = 1.00000/(1.00000+exp((constants[9]-states[0])/constants[10]))
    rates[1] = (constants[7]*(algebraic[1]-states[1]))/(algebraic[5]*1.00000)
    algebraic[0] = 1.00000/(1.00000+exp((constants[1]-states[0])/constants[4]))
    algebraic[4] = constants[3]*algebraic[0]*(states[0]-constants[2])
    algebraic[6] = constants[6]*states[1]*(states[0]-constants[5])
    algebraic[9] = constants[19]*(states[0]-constants[20])
    algebraic[7] = constants[11]*states[2]*(states[0]-constants[5])
    algebraic[8] = constants[17]*states[3]*(states[0]-constants[5])
    rates[0] = -(algebraic[4]+algebraic[6]+algebraic[9]+algebraic[7]+algebraic[8])/constants[0]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[2] = 1.00000/(1.00000+exp((constants[12]-states[0])/constants[13]))
    algebraic[3] = 1.00000/(1.00000+exp((constants[15]-states[0])/constants[16]))
    algebraic[5] = constants[8]/(1.00000+exp((states[0]-constants[9])/constants[10]))
    algebraic[1] = 1.00000/(1.00000+exp((constants[9]-states[0])/constants[10]))
    algebraic[0] = 1.00000/(1.00000+exp((constants[1]-states[0])/constants[4]))
    algebraic[4] = constants[3]*algebraic[0]*(states[0]-constants[2])
    algebraic[6] = constants[6]*states[1]*(states[0]-constants[5])
    algebraic[9] = constants[19]*(states[0]-constants[20])
    algebraic[7] = constants[11]*states[2]*(states[0]-constants[5])
    algebraic[8] = constants[17]*states[3]*(states[0]-constants[5])
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
        self.Cm = 4524
        self.Vm = -22
        self.VCa = 100
        self.gCa = 280
        self.sm = 7.5
        self.VK = -80
        self.gK = 1300
        self.lambda = 1.1
        self.tnbar = 9.09
        self.Vn = -9
        self.sn = 10
        self.gs1 = 3
        self.Vs1 = -40
        self.ss1 = 0.5
        self.taus1 = 1000
        self.Vs2 = -42
        self.ss2 = 0.4
        self.gs2 = 32
        self.taus2 = 120000
        self.gl = 25
        self.Vl = -40

    def to_dict(self):
        return {
            "Cm": self.Cm,
            "Vm": self.Vm,
            "VCa": self.VCa,
            "gCa": self.gCa,
            "sm": self.sm,
            "VK": self.VK,
            "gK": self.gK,
            "lambda": self.lambda,
            "tnbar": self.tnbar,
            "Vn": self.Vn,
            "sn": self.sn,
            "gs1": self.gs1,
            "Vs1": self.Vs1,
            "ss1": self.ss1,
            "taus1": self.taus1,
            "Vs2": self.Vs2,
            "ss2": self.ss2,
            "gs2": self.gs2,
            "taus2": self.taus2,
            "gl": self.gl,
            "Vl": self.Vl,
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
        y0=[-43, 0.03, 0.1, 0.434],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "bertram_previte_sherman_kinard_satin_2000_slow"
        self.curve_names = [
            "V",
            "n",
            "s1",
            "s2",
        ]
        self.state_names = ['V', 'n', 's1', 's2']
        self.algebraic_names = ['minf', 'ninf', 's1inf', 's2inf', 'ICa', 'taun', 'IK', 'Is1', 'Is2', 'Il']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 21
        p = self.params

        # direct mapping
        c[0] = p.Cm
        c[1] = p.Vm
        c[2] = p.VCa
        c[3] = p.gCa
        c[4] = p.sm
        c[5] = p.VK
        c[6] = p.gK
        c[7] = p.lambda
        c[8] = p.tnbar
        c[9] = p.Vn
        c[10] = p.sn
        c[11] = p.gs1
        c[12] = p.Vs1
        c[13] = p.ss1
        c[14] = p.taus1
        c[15] = p.Vs2
        c[16] = p.ss2
        c[17] = p.gs2
        c[18] = p.taus2
        c[19] = p.gl
        c[20] = p.Vl

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
