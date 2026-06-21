# Size of variable arrays:
sizeAlgebraic = 0
sizeStates = 11
sizeConstants = 18
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (second)"
    legend_constants[0] = "k11 in component kinetic_constants (second_order_rate_constant)"
    legend_constants[1] = "k11_ in component kinetic_constants (first_order_rate_constant)"
    legend_constants[2] = "k71 in component kinetic_constants (first_order_rate_constant)"
    legend_constants[3] = "k72 in component kinetic_constants (first_order_rate_constant)"
    legend_constants[4] = "k12 in component kinetic_constants (second_order_rate_constant)"
    legend_constants[5] = "k12_ in component kinetic_constants (first_order_rate_constant)"
    legend_constants[6] = "k51 in component kinetic_constants (first_order_rate_constant)"
    legend_constants[7] = "k52 in component kinetic_constants (first_order_rate_constant)"
    legend_constants[8] = "k41 in component kinetic_constants (first_order_rate_constant)"
    legend_constants[9] = "k31 in component kinetic_constants (first_order_rate_constant)"
    legend_constants[10] = "k32 in component kinetic_constants (first_order_rate_constant)"
    legend_constants[11] = "k42 in component kinetic_constants (first_order_rate_constant)"
    legend_constants[12] = "k22 in component kinetic_constants (first_order_rate_constant)"
    legend_constants[13] = "k22_ in component kinetic_constants (first_order_rate_constant)"
    legend_constants[14] = "k21 in component kinetic_constants (first_order_rate_constant)"
    legend_constants[15] = "k21_ in component kinetic_constants (first_order_rate_constant)"
    legend_states[0] = "PB in component PB (micromolar)"
    legend_constants[16] = "kreset1 in component kreset1 (first_order_rate_constant)"
    legend_states[1] = "A1 in component A1 (micromolar)"
    legend_states[2] = "A2 in component A2 (micromolar)"
    legend_states[3] = "PC1 in component PC1 (micromolar)"
    legend_states[4] = "PF1 in component PF1 (micromolar)"
    legend_states[5] = "PG1 in component PG1 (micromolar)"
    legend_states[6] = "PC2 in component PC2 (micromolar)"
    legend_states[7] = "PF2 in component PF2 (micromolar)"
    legend_states[8] = "PD1 in component PD1 (micromolar)"
    legend_states[9] = "PE1 in component PE1 (micromolar)"
    legend_states[10] = "PD2 in component PD2 (micromolar)"
    legend_constants[17] = "PE2 in component PE2 (micromolar)"
    legend_rates[0] = "d/dt PB in component PB (micromolar)"
    legend_rates[1] = "d/dt A1 in component A1 (micromolar)"
    legend_rates[2] = "d/dt A2 in component A2 (micromolar)"
    legend_rates[3] = "d/dt PC1 in component PC1 (micromolar)"
    legend_rates[8] = "d/dt PD1 in component PD1 (micromolar)"
    legend_rates[9] = "d/dt PE1 in component PE1 (micromolar)"
    legend_rates[4] = "d/dt PF1 in component PF1 (micromolar)"
    legend_rates[5] = "d/dt PG1 in component PG1 (micromolar)"
    legend_rates[6] = "d/dt PC2 in component PC2 (micromolar)"
    legend_rates[10] = "d/dt PD2 in component PD2 (micromolar)"
    legend_rates[7] = "d/dt PF2 in component PF2 (micromolar)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    constants[0] = 110.0
    constants[1] = 25.0
    constants[2] = 0.1
    constants[3] = 60.0
    constants[4] = 110.0
    constants[5] = 0.2
    constants[6] = 7.0
    constants[7] = 0.0
    constants[8] = 60.0
    constants[9] = 500.0
    constants[10] = 50.0
    constants[11] = 70.0
    constants[12] = 100.0
    constants[13] = 17.0
    constants[14] = 100.0
    constants[15] = 0.2
    states[0] = 0.1
    constants[16] = 35.0
    states[1] = 0.1
    states[2] = 0.1
    states[3] = 0.1
    states[4] = 0.1
    states[5] = 0.1
    states[6] = 0.1
    states[7] = 0.1
    states[8] = 0.1
    states[9] = 0.1
    states[10] = 0.1
    constants[17] = 0.1
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[0] = (constants[1]*states[3]+constants[2]*states[4]+constants[16]*states[5]+constants[5]*states[6]+constants[3]*states[7])-(constants[0]*states[1]*states[0]+constants[4]*states[2]*states[0])
    rates[1] = constants[1]*states[3]-constants[0]*states[1]*states[0]
    rates[2] = constants[5]*states[6]-constants[4]*states[2]*states[0]
    rates[3] = (constants[0]*states[1]*states[0]-(constants[1]+constants[14])*states[3])+constants[15]*states[8]
    rates[8] = constants[14]*states[3]-(constants[15]+constants[9])*states[8]
    rates[9] = constants[9]*states[8]-constants[8]*states[9]
    rates[4] = constants[8]*states[9]-(constants[6]+constants[2])*states[4]
    rates[5] = constants[6]*states[4]-constants[16]*states[5]
    rates[6] = (constants[4]*states[2]*states[0]-(constants[5]+constants[12])*states[6])+constants[13]*states[10]
    rates[10] = constants[12]*states[6]-(constants[13]+constants[10])*states[10]
    rates[7] = constants[11]*constants[17]-(constants[7]+constants[3])*states[7]
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
        self.k11 = 110.0
        self.k11_ = 25.0
        self.k71 = 0.1
        self.k72 = 60.0
        self.k12 = 110.0
        self.k12_ = 0.2
        self.k51 = 7.0
        self.k52 = 0.0
        self.k41 = 60.0
        self.k31 = 500.0
        self.k32 = 50.0
        self.k42 = 70.0
        self.k22 = 100.0
        self.k22_ = 17.0
        self.k21 = 100.0
        self.k21_ = 0.2
        self.kreset1 = 35.0
        self.PE2 = 0.1

    def to_dict(self):
        return {
            "k11": self.k11,
            "k11_": self.k11_,
            "k71": self.k71,
            "k72": self.k72,
            "k12": self.k12,
            "k12_": self.k12_,
            "k51": self.k51,
            "k52": self.k52,
            "k41": self.k41,
            "k31": self.k31,
            "k32": self.k32,
            "k42": self.k42,
            "k22": self.k22,
            "k22_": self.k22_,
            "k21": self.k21,
            "k21_": self.k21_,
            "kreset1": self.kreset1,
            "PE2": self.PE2,
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
        y0=[0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "heyd_drew_2003"
        self.curve_names = [
            "PB",
            "A1",
            "A2",
            "PC1",
            "PF1",
            "PG1",
            "PC2",
            "PF2",
            "PD1",
            "PE1",
            "PD2",
        ]
        self.state_names = ['PB', 'A1', 'A2', 'PC1', 'PF1', 'PG1', 'PC2', 'PF2', 'PD1', 'PE1', 'PD2']
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
        c = [0.0] * 18
        p = self.params

        # direct mapping
        c[0] = p.k11
        c[1] = p.k11_
        c[2] = p.k71
        c[3] = p.k72
        c[4] = p.k12
        c[5] = p.k12_
        c[6] = p.k51
        c[7] = p.k52
        c[8] = p.k41
        c[9] = p.k31
        c[10] = p.k32
        c[11] = p.k42
        c[12] = p.k22
        c[13] = p.k22_
        c[14] = p.k21
        c[15] = p.k21_
        c[16] = p.kreset1
        c[17] = p.PE2

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
