# Size of variable arrays:
sizeAlgebraic = 0
sizeStates = 12
sizeConstants = 38
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (second)"
    legend_states[0] = "E in component E (millimolar)"
    legend_constants[0] = "k23 in component reaction_constants (second_order_rate_constant)"
    legend_constants[1] = "k24 in component reaction_constants (first_order_rate_constant)"
    legend_constants[2] = "k17 in component reaction_constants (first_order_rate_constant)"
    legend_constants[3] = "k18 in component reaction_constants (first_order_rate_constant)"
    legend_constants[4] = "k1 in component reaction_constants (second_order_rate_constant)"
    legend_constants[5] = "k2 in component reaction_constants (first_order_rate_constant)"
    legend_constants[6] = "k3 in component reaction_constants (second_order_rate_constant)"
    legend_constants[7] = "k4 in component reaction_constants (first_order_rate_constant)"
    legend_states[1] = "ED in component ED (millimolar)"
    legend_states[2] = "E_ in component E_ (millimolar)"
    legend_states[3] = "ENa in component ENa (millimolar)"
    legend_states[4] = "ECl in component ECl (millimolar)"
    legend_constants[8] = "D in component reaction_constants (millimolar)"
    legend_constants[9] = "Na in component reaction_constants (millimolar)"
    legend_constants[10] = "Cl in component reaction_constants (millimolar)"
    legend_constants[11] = "k29 in component reaction_constants (second_order_rate_constant)"
    legend_constants[12] = "k30 in component reaction_constants (first_order_rate_constant)"
    legend_constants[13] = "k11 in component reaction_constants (second_order_rate_constant)"
    legend_constants[14] = "k12 in component reaction_constants (first_order_rate_constant)"
    legend_constants[15] = "k9 in component reaction_constants (second_order_rate_constant)"
    legend_constants[16] = "k10 in component reaction_constants (first_order_rate_constant)"
    legend_states[5] = "ED_ in component ED_ (millimolar)"
    legend_states[6] = "ENa_ in component ENa_ (millimolar)"
    legend_states[7] = "ECl_ in component ECl_ (millimolar)"
    legend_constants[17] = "D_ in component reaction_constants (millimolar)"
    legend_constants[18] = "Na_ in component reaction_constants (millimolar)"
    legend_constants[19] = "Cl_ in component reaction_constants (millimolar)"
    legend_constants[20] = "k21 in component reaction_constants (second_order_rate_constant)"
    legend_constants[21] = "k22 in component reaction_constants (first_order_rate_constant)"
    legend_states[8] = "ENaD in component ENaD (millimolar)"
    legend_constants[22] = "k27 in component reaction_constants (second_order_rate_constant)"
    legend_constants[23] = "k28 in component reaction_constants (first_order_rate_constant)"
    legend_states[9] = "ENaD_ in component ENaD_ (millimolar)"
    legend_constants[24] = "k25 in component reaction_constants (second_order_rate_constant)"
    legend_constants[25] = "k26 in component reaction_constants (first_order_rate_constant)"
    legend_constants[26] = "k31 in component reaction_constants (second_order_rate_constant)"
    legend_constants[27] = "k32 in component reaction_constants (first_order_rate_constant)"
    legend_constants[28] = "k5 in component reaction_constants (second_order_rate_constant)"
    legend_constants[29] = "k6 in component reaction_constants (first_order_rate_constant)"
    legend_states[10] = "ENaCl in component ENaCl (millimolar)"
    legend_constants[30] = "k13 in component reaction_constants (second_order_rate_constant)"
    legend_constants[31] = "k14 in component reaction_constants (first_order_rate_constant)"
    legend_states[11] = "ENaCl_ in component ENaCl_ (millimolar)"
    legend_constants[32] = "k7 in component reaction_constants (second_order_rate_constant)"
    legend_constants[33] = "k8 in component reaction_constants (first_order_rate_constant)"
    legend_constants[34] = "k15 in component reaction_constants (second_order_rate_constant)"
    legend_constants[35] = "k16 in component reaction_constants (first_order_rate_constant)"
    legend_constants[36] = "k19 in component reaction_constants (first_order_rate_constant)"
    legend_constants[37] = "k20 in component reaction_constants (first_order_rate_constant)"
    legend_rates[0] = "d/dt E in component E (millimolar)"
    legend_rates[2] = "d/dt E_ in component E_ (millimolar)"
    legend_rates[1] = "d/dt ED in component ED (millimolar)"
    legend_rates[5] = "d/dt ED_ in component ED_ (millimolar)"
    legend_rates[8] = "d/dt ENaD in component ENaD (millimolar)"
    legend_rates[9] = "d/dt ENaD_ in component ENaD_ (millimolar)"
    legend_rates[3] = "d/dt ENa in component ENa (millimolar)"
    legend_rates[6] = "d/dt ENa_ in component ENa_ (millimolar)"
    legend_rates[4] = "d/dt ECl in component ECl (millimolar)"
    legend_rates[7] = "d/dt ECl_ in component ECl_ (millimolar)"
    legend_rates[10] = "d/dt ENaCl in component ENaCl (millimolar)"
    legend_rates[11] = "d/dt ENaCl_ in component ENaCl_ (millimolar)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 0.08333
    constants[0] = 1.0E5
    constants[1] = 3.192E1
    constants[2] = 4.587E5
    constants[3] = 1.0E5
    constants[4] = 1.0E5
    constants[5] = 4.183E5
    constants[6] = 1.0E5
    constants[7] = 4.928E6
    states[1] = 0.08333
    states[2] = 0.08333
    states[3] = 0.08333
    states[4] = 0.08333
    constants[8] = 1.0E-6
    constants[9] = 50.0
    constants[10] = 96.0
    constants[11] = 1.0E5
    constants[12] = 3.514E-1
    constants[13] = 1.0E5
    constants[14] = 4.982E6
    constants[15] = 1.0E5
    constants[16] = 4.183E5
    states[5] = 0.08333
    states[6] = 0.08333
    states[7] = 0.08333
    constants[17] = 1.0E-6
    constants[18] = 10.0
    constants[19] = 40.0
    constants[20] = 1.0E5
    constants[21] = 4.183E5
    states[8] = 0.08333
    constants[22] = 1.0E5
    constants[23] = 1.389E5
    states[9] = 0.08333
    constants[24] = 1.0E5
    constants[25] = 3.192E1
    constants[26] = 1.0E5
    constants[27] = 1.166E-1
    constants[28] = 1.0E5
    constants[29] = 1.065E6
    states[10] = 0.08333
    constants[30] = 1.0E5
    constants[31] = 1.065E6
    states[11] = 0.08333
    constants[32] = 1.0E5
    constants[33] = 8.940E4
    constants[34] = 1.0E5
    constants[35] = 8.940E4
    constants[36] = 1.0E3
    constants[37] = 2.180E2
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[0] = (constants[1]*states[1]+constants[3]*states[2]+constants[5]*states[3]+constants[7]*states[4])-(constants[0]*constants[8]*states[0]+constants[2]*states[0]+constants[4]*constants[9]*states[0]+constants[6]*constants[10]*states[0])
    rates[2] = (constants[12]*states[5]+constants[2]*states[0]+constants[16]*states[6]+constants[14]*states[7])-(constants[11]*constants[17]*states[2]+constants[3]*states[2]+constants[15]*constants[18]*states[2]+constants[13]*constants[19]*states[2])
    rates[1] = (constants[0]*states[0]*constants[8]+constants[21]*states[8])-(constants[1]*states[1]+constants[20]*constants[9]*states[1])
    rates[5] = (constants[11]*states[2]*constants[17]+constants[23]*states[9])-(constants[12]*states[5]+constants[22]*constants[18]*states[5])
    rates[8] = (constants[20]*constants[9]*states[1]+constants[24]*constants[8]*states[3])-(constants[21]*states[8]+constants[25]*states[8])
    rates[9] = (constants[22]*constants[18]*states[5]+constants[26]*constants[17]*states[6])-(constants[23]*states[9]+constants[27]*states[9])
    rates[3] = (constants[4]*constants[9]*states[0]+constants[25]*states[8]+constants[29]*states[10])-(constants[5]*states[3]+constants[28]*constants[10]*states[3]+constants[24]*constants[8]*states[3])
    rates[6] = (constants[15]*constants[18]*states[2]+constants[27]*states[9]+constants[31]*states[11])-(constants[16]*states[6]+constants[30]*constants[19]*states[6]+constants[26]*constants[17]*states[6])
    rates[4] = (constants[6]*constants[10]*states[0]+constants[33]*states[10])-(constants[32]*constants[9]*states[4]+constants[7]*states[4])
    rates[7] = (constants[13]*constants[19]*states[2]+constants[35]*states[11])-(constants[34]*constants[18]*states[7]+constants[14]*states[7])
    rates[10] = (constants[28]*constants[10]*states[3]+constants[32]*constants[9]*states[4]+constants[37]*states[11])-(constants[29]*states[10]+constants[33]*states[10]+constants[36]*states[10])
    rates[11] = (constants[30]*constants[19]*states[6]+constants[34]*constants[18]*states[7]+constants[36]*states[10])-(constants[31]*states[11]+constants[35]*states[11]+constants[37]*states[11])
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
        self.k23 = 1.0E5
        self.k24 = 3.192E1
        self.k17 = 4.587E5
        self.k18 = 1.0E5
        self.k1 = 1.0E5
        self.k2 = 4.183E5
        self.k3 = 1.0E5
        self.k4 = 4.928E6
        self.D = 1.0E-6
        self.Na = 50.0
        self.Cl = 96.0
        self.k29 = 1.0E5
        self.k30 = 3.514E-1
        self.k11 = 1.0E5
        self.k12 = 4.982E6
        self.k9 = 1.0E5
        self.k10 = 4.183E5
        self.D_ = 1.0E-6
        self.Na_ = 10.0
        self.Cl_ = 40.0
        self.k21 = 1.0E5
        self.k22 = 4.183E5
        self.k27 = 1.0E5
        self.k28 = 1.389E5
        self.k25 = 1.0E5
        self.k26 = 3.192E1
        self.k31 = 1.0E5
        self.k32 = 1.166E-1
        self.k5 = 1.0E5
        self.k6 = 1.065E6
        self.k13 = 1.0E5
        self.k14 = 1.065E6
        self.k7 = 1.0E5
        self.k8 = 8.940E4
        self.k15 = 1.0E5
        self.k16 = 8.940E4
        self.k19 = 1.0E3
        self.k20 = 2.180E2

    def to_dict(self):
        return {
            "k23": self.k23,
            "k24": self.k24,
            "k17": self.k17,
            "k18": self.k18,
            "k1": self.k1,
            "k2": self.k2,
            "k3": self.k3,
            "k4": self.k4,
            "D": self.D,
            "Na": self.Na,
            "Cl": self.Cl,
            "k29": self.k29,
            "k30": self.k30,
            "k11": self.k11,
            "k12": self.k12,
            "k9": self.k9,
            "k10": self.k10,
            "D_": self.D_,
            "Na_": self.Na_,
            "Cl_": self.Cl_,
            "k21": self.k21,
            "k22": self.k22,
            "k27": self.k27,
            "k28": self.k28,
            "k25": self.k25,
            "k26": self.k26,
            "k31": self.k31,
            "k32": self.k32,
            "k5": self.k5,
            "k6": self.k6,
            "k13": self.k13,
            "k14": self.k14,
            "k7": self.k7,
            "k8": self.k8,
            "k15": self.k15,
            "k16": self.k16,
            "k19": self.k19,
            "k20": self.k20,
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
        y0=[0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333, 0.08333],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "chang_fujita_1999"
        self.curve_names = [
            "E",
            "ED",
            "E_",
            "ENa",
            "ECl",
            "ED_",
            "ENa_",
            "ECl_",
            "ENaD",
            "ENaD_",
            "ENaCl",
            "ENaCl_",
        ]
        self.state_names = ['E', 'ED', 'E_', 'ENa', 'ECl', 'ED_', 'ENa_', 'ECl_', 'ENaD', 'ENaD_', 'ENaCl', 'ENaCl_']
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
        c = [0.0] * 38
        p = self.params

        # direct mapping
        c[0] = p.k23
        c[1] = p.k24
        c[2] = p.k17
        c[3] = p.k18
        c[4] = p.k1
        c[5] = p.k2
        c[6] = p.k3
        c[7] = p.k4
        c[8] = p.D
        c[9] = p.Na
        c[10] = p.Cl
        c[11] = p.k29
        c[12] = p.k30
        c[13] = p.k11
        c[14] = p.k12
        c[15] = p.k9
        c[16] = p.k10
        c[17] = p.D_
        c[18] = p.Na_
        c[19] = p.Cl_
        c[20] = p.k21
        c[21] = p.k22
        c[22] = p.k27
        c[23] = p.k28
        c[24] = p.k25
        c[25] = p.k26
        c[26] = p.k31
        c[27] = p.k32
        c[28] = p.k5
        c[29] = p.k6
        c[30] = p.k13
        c[31] = p.k14
        c[32] = p.k7
        c[33] = p.k8
        c[34] = p.k15
        c[35] = p.k16
        c[36] = p.k19
        c[37] = p.k20

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
