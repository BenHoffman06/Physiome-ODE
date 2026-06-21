# Size of variable arrays:
sizeAlgebraic = 11
sizeStates = 4
sizeConstants = 23
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (millisecond)"
    legend_states[0] = "V in component membrane (millivolt)"
    legend_constants[0] = "C in component membrane (picofarad)"
    legend_algebraic[5] = "I_Ca in component I_Ca (picoampere)"
    legend_algebraic[0] = "I_K in component I_K (picoampere)"
    legend_algebraic[7] = "I_SK in component I_SK (picoampere)"
    legend_algebraic[10] = "I_DA in component I_DA (picoampere)"
    legend_constants[1] = "gK in component I_K (nanosiemens)"
    legend_constants[2] = "VK in component model_parameters (millivolt)"
    legend_states[1] = "n in component n (dimensionless)"
    legend_algebraic[1] = "n_infinity in component n (dimensionless)"
    legend_constants[3] = "lambda in component n (dimensionless)"
    legend_constants[4] = "tau_n in component n (millisecond)"
    legend_constants[5] = "vn in component n (millivolt)"
    legend_constants[6] = "sn in component n (millivolt)"
    legend_constants[7] = "gCa in component I_Ca (nanosiemens)"
    legend_constants[8] = "VCa in component model_parameters (millivolt)"
    legend_algebraic[4] = "m_infinity in component m (dimensionless)"
    legend_constants[9] = "vm in component m (millivolt)"
    legend_constants[10] = "sm in component m (millivolt)"
    legend_constants[11] = "gSK in component I_SK (nanosiemens)"
    legend_algebraic[6] = "s_infinity in component I_SK (dimensionless)"
    legend_constants[12] = "ks in component I_SK (micromolar)"
    legend_states[2] = "Ca in component Ca (micromolar)"
    legend_algebraic[9] = "I_A in component I_DA (picoampere)"
    legend_constants[13] = "gA in component I_DA (nanosiemens)"
    legend_algebraic[8] = "a_infinity in component a (dimensionless)"
    legend_states[3] = "h in component h (dimensionless)"
    legend_constants[14] = "va in component a (millivolt)"
    legend_constants[15] = "sa in component a (millivolt)"
    legend_algebraic[2] = "h_infinity in component h (dimensionless)"
    legend_constants[16] = "tau_h in component h (millisecond)"
    legend_constants[17] = "vh in component h (millivolt)"
    legend_constants[18] = "sh in component h (millivolt)"
    legend_constants[19] = "fc in component Ca (dimensionless)"
    legend_constants[20] = "alpha in component Ca (micromolar_femtocoulomb)"
    legend_constants[21] = "kc in component Ca (first_order_rate_constant)"
    legend_algebraic[3] = "PRL in component PRL (dimensionless)"
    legend_constants[22] = "kPRL in component PRL (micromolar_4)"
    legend_rates[0] = "d/dt V in component membrane (millivolt)"
    legend_rates[1] = "d/dt n in component n (dimensionless)"
    legend_rates[3] = "d/dt h in component h (dimensionless)"
    legend_rates[2] = "d/dt Ca in component Ca (micromolar)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = -60
    constants[0] = 10
    constants[1] = 4
    constants[2] = -75
    states[1] = 0.1
    constants[3] = 0.7
    constants[4] = 30
    constants[5] = -5
    constants[6] = 10
    constants[7] = 2
    constants[8] = 50
    constants[9] = -20
    constants[10] = 12
    constants[11] = 1.7
    constants[12] = 0.5
    states[2] = 0.1
    constants[13] = 25
    states[3] = 0.1
    constants[14] = -20
    constants[15] = 10
    constants[16] = 20
    constants[17] = -60
    constants[18] = 5
    constants[19] = 0.01
    constants[20] = 0.0015
    constants[21] = 0.16
    constants[22] = 1
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[1] = 1.00000/(1.00000+exp((constants[5]-states[0])/constants[6]))
    rates[1] = (constants[3]*(algebraic[1]-states[1]))/constants[4]
    algebraic[2] = 1.00000/(1.00000+exp((states[0]-constants[17])/constants[18]))
    rates[3] = (algebraic[2]-states[3])/constants[16]
    algebraic[4] = 1.00000/(1.00000+exp((constants[9]-states[0])/constants[10]))
    algebraic[5] = constants[7]*algebraic[4]*(states[0]-constants[8])
    rates[2] = -constants[19]*(constants[20]*algebraic[5]+constants[21]*states[2])
    algebraic[0] = constants[1]*states[1]*(states[0]-constants[2])
    algebraic[6] = (power(states[2], 2.00000))/(power(states[2], 2.00000)+power(constants[12], 2.00000))
    algebraic[7] = constants[11]*algebraic[6]*(states[0]-constants[2])
    algebraic[8] = 1.00000/(1.00000+exp((constants[14]-states[0])/constants[15]))
    algebraic[9] = constants[13]*algebraic[8]*states[3]*(states[0]-constants[2])
    algebraic[10] = algebraic[9]
    rates[0] = -(algebraic[5]+algebraic[0]+algebraic[7]+algebraic[10])/constants[0]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[1] = 1.00000/(1.00000+exp((constants[5]-states[0])/constants[6]))
    algebraic[2] = 1.00000/(1.00000+exp((states[0]-constants[17])/constants[18]))
    algebraic[4] = 1.00000/(1.00000+exp((constants[9]-states[0])/constants[10]))
    algebraic[5] = constants[7]*algebraic[4]*(states[0]-constants[8])
    algebraic[0] = constants[1]*states[1]*(states[0]-constants[2])
    algebraic[6] = (power(states[2], 2.00000))/(power(states[2], 2.00000)+power(constants[12], 2.00000))
    algebraic[7] = constants[11]*algebraic[6]*(states[0]-constants[2])
    algebraic[8] = 1.00000/(1.00000+exp((constants[14]-states[0])/constants[15]))
    algebraic[9] = constants[13]*algebraic[8]*states[3]*(states[0]-constants[2])
    algebraic[10] = algebraic[9]
    algebraic[3] = constants[22]*(power(states[2], 4.00000))
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
        self.C = 10
        self.gK = 4
        self.VK = -75
        self.lambda = 0.7
        self.tau_n = 30
        self.vn = -5
        self.sn = 10
        self.gCa = 2
        self.VCa = 50
        self.vm = -20
        self.sm = 12
        self.gSK = 1.7
        self.ks = 0.5
        self.gA = 25
        self.va = -20
        self.sa = 10
        self.tau_h = 20
        self.vh = -60
        self.sh = 5
        self.fc = 0.01
        self.alpha = 0.0015
        self.kc = 0.16
        self.kPRL = 1

    def to_dict(self):
        return {
            "C": self.C,
            "gK": self.gK,
            "VK": self.VK,
            "lambda": self.lambda,
            "tau_n": self.tau_n,
            "vn": self.vn,
            "sn": self.sn,
            "gCa": self.gCa,
            "VCa": self.VCa,
            "vm": self.vm,
            "sm": self.sm,
            "gSK": self.gSK,
            "ks": self.ks,
            "gA": self.gA,
            "va": self.va,
            "sa": self.sa,
            "tau_h": self.tau_h,
            "vh": self.vh,
            "sh": self.sh,
            "fc": self.fc,
            "alpha": self.alpha,
            "kc": self.kc,
            "kPRL": self.kPRL,
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
        y0=[-60, 0.1, 0.1, 0.1],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "tabak_toporikova_freeman_bertram_2007_b"
        self.curve_names = [
            "V",
            "n",
            "Ca",
            "h",
        ]
        self.state_names = ['V', 'n', 'Ca', 'h']
        self.algebraic_names = ['I_K', 'n_infinity', 'h_infinity', 'PRL', 'm_infinity', 'I_Ca', 's_infinity', 'I_SK', 'a_infinity', 'I_A', 'I_DA']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 23
        p = self.params

        # direct mapping
        c[0] = p.C
        c[1] = p.gK
        c[2] = p.VK
        c[3] = p.lambda
        c[4] = p.tau_n
        c[5] = p.vn
        c[6] = p.sn
        c[7] = p.gCa
        c[8] = p.VCa
        c[9] = p.vm
        c[10] = p.sm
        c[11] = p.gSK
        c[12] = p.ks
        c[13] = p.gA
        c[14] = p.va
        c[15] = p.sa
        c[16] = p.tau_h
        c[17] = p.vh
        c[18] = p.sh
        c[19] = p.fc
        c[20] = p.alpha
        c[21] = p.kc
        c[22] = p.kPRL

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
