# Size of variable arrays:
sizeAlgebraic = 2
sizeStates = 2
sizeConstants = 9
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (minute)"
    legend_constants[0] = "PMO in component muscle_autoregulatory_local_blood_flow_control (mmHg)"
    legend_constants[6] = "PDO in component M_autoregulatory_driving_force (mmHg)"
    legend_constants[7] = "POE in component M_ST_sensitivity_control (mmHg)"
    legend_constants[1] = "POM in component parameter_values (dimensionless)"
    legend_algebraic[0] = "AMM1 in component M_ST_time_delay_and_limit (dimensionless)"
    legend_constants[2] = "A4K in component parameter_values (minute)"
    legend_constants[3] = "AMM4 in component parameter_values (dimensionless)"
    legend_states[0] = "AMM1T in component M_ST_time_delay_and_limit (dimensionless)"
    legend_constants[8] = "POF in component M_LT_sensitivity_control (mmHg)"
    legend_constants[4] = "POM2 in component parameter_values (dimensionless)"
    legend_states[1] = "AMM2 in component M_LT_time_delay (dimensionless)"
    legend_constants[5] = "A4K2 in component parameter_values (minute)"
    legend_algebraic[1] = "AMM in component global_M_blood_flow_autoregulation_output (dimensionless)"
    legend_rates[0] = "d/dt AMM1T in component M_ST_time_delay_and_limit (dimensionless)"
    legend_rates[1] = "d/dt AMM2 in component M_LT_time_delay (dimensionless)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    constants[0] = 38.0666
    constants[1] = 0.04
    constants[2] = 0.1
    constants[3] = 0.005
    states[0] = 1.00269
    constants[4] = 2
    states[1] = 1.09071
    constants[5] = 40000
    constants[6] = constants[0]-38.0000
    constants[7] = constants[6]*constants[1]+1.00000
    constants[8] = constants[4]*constants[6]+1.00000
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[0] = (constants[7]*1.00000-states[0])/constants[2]
    rates[1] = (constants[8]*1.00000-states[1])/constants[5]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = custom_piecewise([less(states[0] , constants[3]), constants[3] , True, states[0]])
    algebraic[1] = algebraic[0]*states[1]
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
        self.PMO = 38.0666
        self.POM = 0.04
        self.A4K = 0.1
        self.AMM4 = 0.005
        self.POM2 = 2
        self.A4K2 = 40000

    def to_dict(self):
        return {
            "PMO": self.PMO,
            "POM": self.POM,
            "A4K": self.A4K,
            "AMM4": self.AMM4,
            "POM2": self.POM2,
            "A4K2": self.A4K2,
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
        y0=[1.00269, 1.09071],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "guyton_muscle_blood_flow_control_2008"
        self.curve_names = [
            "AMM1T",
            "AMM2",
        ]
        self.state_names = ['AMM1T', 'AMM2']
        self.algebraic_names = ['AMM1', 'AMM']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 9
        p = self.params

        # direct mapping
        c[0] = p.PMO
        c[1] = p.POM
        c[2] = p.A4K
        c[3] = p.AMM4
        c[4] = p.POM2
        c[5] = p.A4K2

        # derived constants
        c[6] = c[0]-38.0000
        c[7] = c[6]*c[1]+1.00000
        c[8] = c[4]*c[6]+1.00000

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
