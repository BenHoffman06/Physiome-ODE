# Size of variable arrays:
sizeAlgebraic = 0
sizeStates = 16
sizeConstants = 21
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "t in component environment (s)"
    legend_constants[0] = "kM2T2_on in component Model (second_order_rate_constant)"
    legend_constants[1] = "kM2T2_off in component Model (first_order_rate_constant)"
    legend_constants[2] = "kM2T2_iso in component Model (first_order_rate_constant)"
    legend_constants[3] = "kM2T2_negativeiso in component Model (first_order_rate_constant)"
    legend_constants[4] = "kM2C1_on in component Model (second_order_rate_constant)"
    legend_constants[5] = "kM2C1_off in component Model (first_order_rate_constant)"
    legend_constants[6] = "kM2C1_cat in component Model (first_order_rate_constant)"
    legend_constants[7] = "kMT1T2_on in component Model (second_order_rate_constant)"
    legend_constants[8] = "kMT1T2_off in component Model (first_order_rate_constant)"
    legend_constants[9] = "kMT1T2M2pro_on in component Model (second_order_rate_constant)"
    legend_constants[10] = "kMT1T2M2pro_off in component Model (first_order_rate_constant)"
    legend_constants[11] = "kM2_act in component Model (first_order_rate_constant)"
    legend_constants[12] = "kMT1_shedeff in component Model (second_order_rate_constant)"
    legend_constants[13] = "kMT1C1_cat in component Model (first_order_rate_constant)"
    legend_constants[14] = "kMT1C1_on in component Model (second_order_rate_constant)"
    legend_constants[15] = "kMT1C1_off in component Model (first_order_rate_constant)"
    legend_constants[16] = "kMT1T2M2proMT1_on in component Model (second_order_rate_constant)"
    legend_constants[17] = "kMT1T2M2proMT1_off in component Model (first_order_rate_constant)"
    legend_states[0] = "M2T2 in component Model (M)"
    legend_states[1] = "M2C1 in component Model (M)"
    legend_states[2] = "MT1T2 in component Model (M)"
    legend_states[3] = "MT1T2M2proMT1 in component Model (M)"
    legend_states[4] = "MT1C1 in component Model (M)"
    legend_states[5] = "M2 in component Model (M)"
    legend_states[6] = "MT1 in component Model (M)"
    legend_states[7] = "M2_p in component Model (M)"
    legend_states[8] = "T2 in component Model (M)"
    legend_states[9] = "C1_D in component Model (M)"
    legend_states[10] = "C1 in component Model (M)"
    legend_states[11] = "MT1_cat in component Model (M)"
    legend_states[12] = "MT1_t in component Model (M)"
    legend_states[13] = "MT1T2M2pro in component Model (M)"
    legend_constants[18] = "qMT1 in component Model (flux)"
    legend_constants[19] = "qT2 in component Model (flux)"
    legend_constants[20] = "qpro in component Model (flux)"
    legend_states[14] = "MT1T2_star in component Model (um)"
    legend_states[15] = "M2T2_star in component Model (um)"
    legend_rates[5] = "d/dt M2 in component Model (M)"
    legend_rates[6] = "d/dt MT1 in component Model (M)"
    legend_rates[12] = "d/dt MT1_t in component Model (M)"
    legend_rates[4] = "d/dt MT1C1 in component Model (M)"
    legend_rates[2] = "d/dt MT1T2 in component Model (M)"
    legend_rates[13] = "d/dt MT1T2M2pro in component Model (M)"
    legend_rates[3] = "d/dt MT1T2M2proMT1 in component Model (M)"
    legend_rates[10] = "d/dt C1 in component Model (M)"
    legend_rates[9] = "d/dt C1_D in component Model (M)"
    legend_rates[11] = "d/dt MT1_cat in component Model (M)"
    legend_rates[8] = "d/dt T2 in component Model (M)"
    legend_rates[7] = "d/dt M2_p in component Model (M)"
    legend_rates[0] = "d/dt M2T2 in component Model (M)"
    legend_rates[15] = "d/dt M2T2_star in component Model (um)"
    legend_rates[1] = "d/dt M2C1 in component Model (M)"
    legend_rates[14] = "d/dt MT1T2_star in component Model (um)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    constants[0] = 5900000
    constants[1] = 6.3
    constants[2] = 33
    constants[3] = 0.00000002
    constants[4] = 2600
    constants[5] = 0.0021
    constants[6] = 0.0045
    constants[7] = 2980000
    constants[8] = 0.202
    constants[9] = 140000
    constants[10] = 0.0047
    constants[11] = 0.02
    constants[12] = 2800
    constants[13] = 0.00197
    constants[14] = 1000
    constants[15] = 1
    constants[16] = 3000
    constants[17] = 0.0009
    states[0] = 0.0000000072
    states[1] = 0.0000085
    states[2] = 0.00000000139
    states[3] = 0.00000000056
    states[4] = 0.0000029
    states[5] = 0
    states[6] = 0
    states[7] = 0
    states[8] = 0
    states[9] = 0
    states[10] = 0
    states[11] = 0
    states[12] = 0
    states[13] = 0
    constants[18] = 0
    constants[19] = 0
    constants[20] = 0
    states[14] = 0
    states[15] = 0
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[5] = ((-constants[0]*states[5]*states[8]+constants[1]*states[0])-constants[4]*states[5]*states[10])+(constants[5]+constants[6])*states[1]+constants[11]*states[3]
    rates[6] = ((((((constants[18]-constants[12]*states[6]*states[6])-constants[7]*states[6]*states[8])+constants[8]*states[2])-constants[14]*states[6]*states[10])+(constants[15]+constants[13])*states[4])-constants[16]*states[6]*states[13])+constants[17]*states[3]+constants[11]*states[3]
    rates[12] = constants[12]*states[6]*states[6]
    rates[4] = constants[14]*states[6]*states[10]-(constants[15]+constants[13])*states[4]
    rates[2] = ((constants[7]*states[6]*states[8]-constants[8]*states[2])-constants[9]*states[2]*states[7])+constants[10]*states[13]
    rates[13] = ((constants[9]*states[2]*states[7]-constants[10]*states[13])-constants[16]*states[6]*states[13])+constants[17]*states[3]
    rates[3] = (constants[16]*states[6]*states[13]-constants[17]*states[3])-constants[11]*states[3]
    rates[10] = ((-constants[14]*states[6]*states[10]+constants[15]*states[4])-constants[4]*states[5]*states[10])+constants[5]*states[1]
    rates[9] = constants[6]*states[1]+constants[13]*states[4]
    rates[11] = constants[12]*states[6]*states[6]
    rates[8] = ((-constants[0]*states[5]*states[8]+constants[1]*states[0]+constants[19])-constants[7]*states[6]*states[8])+constants[8]*states[2]
    rates[7] = (constants[20]-constants[9]*states[2]*states[7])+constants[10]*states[13]
    rates[0] = ((constants[0]*states[5]*states[8]-constants[1]*states[0])-constants[2]*states[0])+constants[3]*states[15]
    rates[15] = constants[2]*states[0]-constants[3]*states[15]
    rates[1] = constants[4]*states[5]*states[10]-(constants[5]+constants[6])*states[1]
    rates[14] = constants[11]*states[3]
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
        self.kM2T2_on = 5900000
        self.kM2T2_off = 6.3
        self.kM2T2_iso = 33
        self.kM2T2_negativeiso = 0.00000002
        self.kM2C1_on = 2600
        self.kM2C1_off = 0.0021
        self.kM2C1_cat = 0.0045
        self.kMT1T2_on = 2980000
        self.kMT1T2_off = 0.202
        self.kMT1T2M2pro_on = 140000
        self.kMT1T2M2pro_off = 0.0047
        self.kM2_act = 0.02
        self.kMT1_shedeff = 2800
        self.kMT1C1_cat = 0.00197
        self.kMT1C1_on = 1000
        self.kMT1C1_off = 1
        self.kMT1T2M2proMT1_on = 3000
        self.kMT1T2M2proMT1_off = 0.0009
        self.qMT1 = 0
        self.qT2 = 0
        self.qpro = 0

    def to_dict(self):
        return {
            "kM2T2_on": self.kM2T2_on,
            "kM2T2_off": self.kM2T2_off,
            "kM2T2_iso": self.kM2T2_iso,
            "kM2T2_negativeiso": self.kM2T2_negativeiso,
            "kM2C1_on": self.kM2C1_on,
            "kM2C1_off": self.kM2C1_off,
            "kM2C1_cat": self.kM2C1_cat,
            "kMT1T2_on": self.kMT1T2_on,
            "kMT1T2_off": self.kMT1T2_off,
            "kMT1T2M2pro_on": self.kMT1T2M2pro_on,
            "kMT1T2M2pro_off": self.kMT1T2M2pro_off,
            "kM2_act": self.kM2_act,
            "kMT1_shedeff": self.kMT1_shedeff,
            "kMT1C1_cat": self.kMT1C1_cat,
            "kMT1C1_on": self.kMT1C1_on,
            "kMT1C1_off": self.kMT1C1_off,
            "kMT1T2M2proMT1_on": self.kMT1T2M2proMT1_on,
            "kMT1T2M2proMT1_off": self.kMT1T2M2proMT1_off,
            "qMT1": self.qMT1,
            "qT2": self.qT2,
            "qpro": self.qpro,
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
        y0=[0.0000000072, 0.0000085, 0.00000000139, 0.00000000056, 0.0000029, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "karagiannis_popel_2006"
        self.curve_names = [
            "M2T2",
            "M2C1",
            "MT1T2",
            "MT1T2M2proMT1",
            "MT1C1",
            "M2",
            "MT1",
            "M2_p",
            "T2",
            "C1_D",
            "C1",
            "MT1_cat",
            "MT1_t",
            "MT1T2M2pro",
            "MT1T2_star",
            "M2T2_star",
        ]
        self.state_names = ['M2T2', 'M2C1', 'MT1T2', 'MT1T2M2proMT1', 'MT1C1', 'M2', 'MT1', 'M2_p', 'T2', 'C1_D', 'C1', 'MT1_cat', 'MT1_t', 'MT1T2M2pro', 'MT1T2_star', 'M2T2_star']
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
        c = [0.0] * 21
        p = self.params

        # direct mapping
        c[0] = p.kM2T2_on
        c[1] = p.kM2T2_off
        c[2] = p.kM2T2_iso
        c[3] = p.kM2T2_negativeiso
        c[4] = p.kM2C1_on
        c[5] = p.kM2C1_off
        c[6] = p.kM2C1_cat
        c[7] = p.kMT1T2_on
        c[8] = p.kMT1T2_off
        c[9] = p.kMT1T2M2pro_on
        c[10] = p.kMT1T2M2pro_off
        c[11] = p.kM2_act
        c[12] = p.kMT1_shedeff
        c[13] = p.kMT1C1_cat
        c[14] = p.kMT1C1_on
        c[15] = p.kMT1C1_off
        c[16] = p.kMT1T2M2proMT1_on
        c[17] = p.kMT1T2M2proMT1_off
        c[18] = p.qMT1
        c[19] = p.qT2
        c[20] = p.qpro

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
