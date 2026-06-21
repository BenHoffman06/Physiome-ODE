# Size of variable arrays:
sizeAlgebraic = 9
sizeStates = 13
sizeConstants = 15
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (second)"
    legend_algebraic[0] = "v1 in component main (flux)"
    legend_algebraic[1] = "v2 in component main (flux)"
    legend_algebraic[2] = "v3 in component main (flux)"
    legend_algebraic[3] = "v4 in component main (flux)"
    legend_algebraic[4] = "v5 in component main (flux)"
    legend_algebraic[5] = "v6 in component main (flux)"
    legend_algebraic[6] = "v7 in component main (flux)"
    legend_algebraic[7] = "v8 in component main (flux)"
    legend_algebraic[8] = "v9 in component main (flux)"
    legend_states[0] = "MT1 in component main (molar)"
    legend_states[1] = "MT1cat in component main (molar)"
    legend_states[2] = "MT1T2 in component main (molar)"
    legend_states[3] = "MT1T2M2P in component main (molar)"
    legend_states[4] = "M2P in component main (molar)"
    legend_states[5] = "M2 in component main (molar)"
    legend_states[6] = "M2T2 in component main (molar)"
    legend_states[7] = "M2T2star in component main (molar)"
    legend_states[8] = "M2C1 in component main (molar)"
    legend_states[9] = "C1 in component main (molar)"
    legend_states[10] = "C1dmt1 in component main (molar)"
    legend_states[11] = "C1dm2 in component main (molar)"
    legend_states[12] = "T2 in component main (molar)"
    legend_constants[0] = "kshed_eff in component model_parameters (second_order_rate_constant)"
    legend_constants[1] = "kon_MT1T2 in component model_parameters (second_order_rate_constant)"
    legend_constants[2] = "ki_MT1T2 in component model_parameters (molar)"
    legend_constants[3] = "kon_MT1T2M2P in component model_parameters (second_order_rate_constant)"
    legend_constants[4] = "koff_MT1T2M2P in component model_parameters (first_order_rate_constant)"
    legend_constants[5] = "kact_eff_m2 in component model_parameters (second_order_rate_constant)"
    legend_constants[6] = "kon_M2T2 in component model_parameters (second_order_rate_constant)"
    legend_constants[7] = "ki_M2T2 in component model_parameters (molar)"
    legend_constants[8] = "kiso_M2T2 in component model_parameters (first_order_rate_constant)"
    legend_constants[9] = "k_iso_M2T2 in component model_parameters (first_order_rate_constant)"
    legend_constants[10] = "kon_M2C1 in component model_parameters (second_order_rate_constant)"
    legend_constants[11] = "koff_M2C1 in component model_parameters (first_order_rate_constant)"
    legend_constants[12] = "kcat_M2C1 in component model_parameters (first_order_rate_constant)"
    legend_constants[13] = "kcat_MT1C1 in component model_parameters (first_order_rate_constant)"
    legend_constants[14] = "km_MT1C1 in component model_parameters (molar)"
    legend_rates[0] = "d/dt MT1 in component main (molar)"
    legend_rates[1] = "d/dt MT1cat in component main (molar)"
    legend_rates[2] = "d/dt MT1T2 in component main (molar)"
    legend_rates[3] = "d/dt MT1T2M2P in component main (molar)"
    legend_rates[4] = "d/dt M2P in component main (molar)"
    legend_rates[5] = "d/dt M2 in component main (molar)"
    legend_rates[6] = "d/dt M2T2 in component main (molar)"
    legend_rates[7] = "d/dt M2T2star in component main (molar)"
    legend_rates[8] = "d/dt M2C1 in component main (molar)"
    legend_rates[9] = "d/dt C1 in component main (molar)"
    legend_rates[10] = "d/dt C1dmt1 in component main (molar)"
    legend_rates[11] = "d/dt C1dm2 in component main (molar)"
    legend_rates[12] = "d/dt T2 in component main (molar)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 100e-9
    states[1] = 0
    states[2] = 0
    states[3] = 0
    states[4] = 50e-9
    states[5] = 0
    states[6] = 0
    states[7] = 0
    states[8] = 0
    states[9] = 1e-6
    states[10] = 0
    states[11] = 0
    states[12] = 50e-9
    constants[0] = 2.8e3
    constants[1] = 3.54e6
    constants[2] = 4.9e-9
    constants[3] = 0.14e6
    constants[4] = 4.7e-3
    constants[5] = 2.8e3
    constants[6] = 5.9e6
    constants[7] = 1.07e-6
    constants[8] = 33
    constants[9] = 2e-8
    constants[10] = 2.6e3
    constants[11] = 2.1e-3
    constants[12] = 4.5e-3
    constants[13] = 1.97e-3
    constants[14] = 2.9e-6
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[0] = constants[0]*states[0]*states[0]
    rates[1] = algebraic[0]
    algebraic[1] = constants[1]*states[0]*states[12]-constants[2]*constants[1]*states[2]
    rates[0] = -algebraic[0]-algebraic[1]
    algebraic[2] = constants[3]*states[2]*states[4]-constants[4]*states[3]
    rates[2] = algebraic[1]-algebraic[2]
    rates[4] = -algebraic[2]
    algebraic[3] = constants[5]*states[0]*states[3]
    rates[3] = algebraic[2]-algebraic[3]
    algebraic[4] = constants[6]*states[5]*states[12]-constants[6]*constants[7]*states[6]
    rates[12] = -algebraic[1]-algebraic[4]
    algebraic[6] = constants[10]*states[5]*states[9]-constants[11]*states[8]
    rates[5] = (algebraic[3]-algebraic[4])-algebraic[6]
    algebraic[5] = constants[8]*states[6]-constants[9]*states[7]
    rates[6] = algebraic[4]-algebraic[5]
    rates[7] = algebraic[5]
    algebraic[7] = constants[12]*states[8]
    rates[8] = algebraic[6]-algebraic[7]
    algebraic[8] = (constants[13]/constants[14])*states[0]*states[9]
    rates[9] = -algebraic[6]-algebraic[8]
    rates[10] = algebraic[8]
    rates[11] = algebraic[7]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = constants[0]*states[0]*states[0]
    algebraic[1] = constants[1]*states[0]*states[12]-constants[2]*constants[1]*states[2]
    algebraic[2] = constants[3]*states[2]*states[4]-constants[4]*states[3]
    algebraic[3] = constants[5]*states[0]*states[3]
    algebraic[4] = constants[6]*states[5]*states[12]-constants[6]*constants[7]*states[6]
    algebraic[6] = constants[10]*states[5]*states[9]-constants[11]*states[8]
    algebraic[5] = constants[8]*states[6]-constants[9]*states[7]
    algebraic[7] = constants[12]*states[8]
    algebraic[8] = (constants[13]/constants[14])*states[0]*states[9]
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
        self.kshed_eff = 2.8e3
        self.kon_MT1T2 = 3.54e6
        self.ki_MT1T2 = 4.9e-9
        self.kon_MT1T2M2P = 0.14e6
        self.koff_MT1T2M2P = 4.7e-3
        self.kact_eff_m2 = 2.8e3
        self.kon_M2T2 = 5.9e6
        self.ki_M2T2 = 1.07e-6
        self.kiso_M2T2 = 33
        self.k_iso_M2T2 = 2e-8
        self.kon_M2C1 = 2.6e3
        self.koff_M2C1 = 2.1e-3
        self.kcat_M2C1 = 4.5e-3
        self.kcat_MT1C1 = 1.97e-3
        self.km_MT1C1 = 2.9e-6

    def to_dict(self):
        return {
            "kshed_eff": self.kshed_eff,
            "kon_MT1T2": self.kon_MT1T2,
            "ki_MT1T2": self.ki_MT1T2,
            "kon_MT1T2M2P": self.kon_MT1T2M2P,
            "koff_MT1T2M2P": self.koff_MT1T2M2P,
            "kact_eff_m2": self.kact_eff_m2,
            "kon_M2T2": self.kon_M2T2,
            "ki_M2T2": self.ki_M2T2,
            "kiso_M2T2": self.kiso_M2T2,
            "k_iso_M2T2": self.k_iso_M2T2,
            "kon_M2C1": self.kon_M2C1,
            "koff_M2C1": self.koff_M2C1,
            "kcat_M2C1": self.kcat_M2C1,
            "kcat_MT1C1": self.kcat_MT1C1,
            "km_MT1C1": self.km_MT1C1,
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
        y0=[100e-9, 0, 0, 0, 50e-9, 0, 0, 0, 0, 1e-6, 0, 0, 50e-9],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "karagiannis_popel_2004"
        self.curve_names = [
            "MT1",
            "MT1cat",
            "MT1T2",
            "MT1T2M2P",
            "M2P",
            "M2",
            "M2T2",
            "M2T2star",
            "M2C1",
            "C1",
            "C1dmt1",
            "C1dm2",
            "T2",
        ]
        self.state_names = ['MT1', 'MT1cat', 'MT1T2', 'MT1T2M2P', 'M2P', 'M2', 'M2T2', 'M2T2star', 'M2C1', 'C1', 'C1dmt1', 'C1dm2', 'T2']
        self.algebraic_names = ['v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8', 'v9']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 15
        p = self.params

        # direct mapping
        c[0] = p.kshed_eff
        c[1] = p.kon_MT1T2
        c[2] = p.ki_MT1T2
        c[3] = p.kon_MT1T2M2P
        c[4] = p.koff_MT1T2M2P
        c[5] = p.kact_eff_m2
        c[6] = p.kon_M2T2
        c[7] = p.ki_M2T2
        c[8] = p.kiso_M2T2
        c[9] = p.k_iso_M2T2
        c[10] = p.kon_M2C1
        c[11] = p.koff_M2C1
        c[12] = p.kcat_M2C1
        c[13] = p.kcat_MT1C1
        c[14] = p.km_MT1C1

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
