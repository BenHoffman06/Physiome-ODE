# Size of variable arrays:
sizeAlgebraic = 5
sizeStates = 3
sizeConstants = 13
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (minute)"
    legend_constants[0] = "POT in component non_muscle_autoregulatory_local_blood_flow_control (mmHg)"
    legend_constants[9] = "POD in component NM_autoregulatory_driving_force (mmHg)"
    legend_constants[1] = "POR in component parameter_values (mmHg)"
    legend_constants[10] = "POB in component NM_ST_sensitivity_control (mmHg)"
    legend_constants[2] = "POK in component parameter_values (dimensionless)"
    legend_algebraic[0] = "AR1 in component NM_ST_time_delay_and_damping (dimensionless)"
    legend_constants[3] = "A1K in component parameter_values (minute)"
    legend_states[0] = "AR1T in component NM_ST_time_delay_and_damping (dimensionless)"
    legend_constants[11] = "POA in component NM_I_sensitivity_control (mmHg)"
    legend_constants[4] = "PON in component parameter_values (dimensionless)"
    legend_algebraic[1] = "AR2 in component NM_I_time_delay_and_limit (dimensionless)"
    legend_constants[5] = "A2K in component parameter_values (minute)"
    legend_states[1] = "AR2T in component NM_I_time_delay_and_limit (dimensionless)"
    legend_constants[12] = "POC in component NM_LT_sensitivity_control (mmHg)"
    legend_constants[6] = "POZ in component parameter_values (dimensionless)"
    legend_algebraic[2] = "AR3 in component NM_LT_time_delay_and_limit (dimensionless)"
    legend_constants[7] = "A3K in component parameter_values (minute)"
    legend_states[2] = "AR3T in component NM_LT_time_delay_and_limit (dimensionless)"
    legend_algebraic[3] = "ARM1 in component total_NM_autoregulation (dimensionless)"
    legend_algebraic[4] = "ARM in component global_NM_blood_flow_autoregulation_output (dimensionless)"
    legend_constants[8] = "AUTOSN in component parameter_values (dimensionless)"
    legend_rates[0] = "d/dt AR1T in component NM_ST_time_delay_and_damping (dimensionless)"
    legend_rates[1] = "d/dt AR2T in component NM_I_time_delay_and_limit (dimensionless)"
    legend_rates[2] = "d/dt AR3T in component NM_LT_time_delay_and_limit (dimensionless)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    constants[0] = 35.1148
    constants[1] = 35
    constants[2] = 0.1
    constants[3] = 0.5
    states[0] = 1.02127
    constants[4] = 0.1
    constants[5] = 60
    states[1] = 1.01179
    constants[6] = 2
    constants[7] = 40000
    states[2] = 1.1448
    constants[8] = 0.9
    constants[9] = constants[0]-constants[1]
    constants[10] = constants[9]*constants[2]+1.00000
    constants[11] = constants[4]*constants[9]+1.00000
    constants[12] = constants[6]*constants[9]+1.00000
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[0] = (constants[10]*1.00000-states[0])/constants[3]
    rates[1] = (constants[11]*1.00000-states[1])/constants[5]
    rates[2] = (constants[12]*1.00000-states[2])/constants[7]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = custom_piecewise([less(states[0] , 0.500000), 0.500000 , True, states[0]])
    algebraic[1] = custom_piecewise([less(states[1] , 0.500000), 0.500000 , True, states[1]])
    algebraic[2] = custom_piecewise([less(states[2] , 0.300000), 0.300000 , True, states[2]])
    algebraic[3] = algebraic[0]*algebraic[1]*algebraic[2]
    algebraic[4] = (algebraic[3]-1.00000)*constants[8]+1.00000
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
        self.POT = 35.1148
        self.POR = 35
        self.POK = 0.1
        self.A1K = 0.5
        self.PON = 0.1
        self.A2K = 60
        self.POZ = 2
        self.A3K = 40000
        self.AUTOSN = 0.9

    def to_dict(self):
        return {
            "POT": self.POT,
            "POR": self.POR,
            "POK": self.POK,
            "A1K": self.A1K,
            "PON": self.PON,
            "A2K": self.A2K,
            "POZ": self.POZ,
            "A3K": self.A3K,
            "AUTOSN": self.AUTOSN,
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
        y0=[1.02127, 1.01179, 1.1448],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "guyton_non_muscle_blood_flow_control_2008"
        self.curve_names = [
            "AR1T",
            "AR2T",
            "AR3T",
        ]
        self.state_names = ['AR1T', 'AR2T', 'AR3T']
        self.algebraic_names = ['AR1', 'AR2', 'AR3', 'ARM1', 'ARM']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 13
        p = self.params

        # direct mapping
        c[0] = p.POT
        c[1] = p.POR
        c[2] = p.POK
        c[3] = p.A1K
        c[4] = p.PON
        c[5] = p.A2K
        c[6] = p.POZ
        c[7] = p.A3K
        c[8] = p.AUTOSN

        # derived constants
        c[9] = c[0]-c[1]
        c[10] = c[9]*c[2]+1.00000
        c[11] = c[4]*c[9]+1.00000
        c[12] = c[6]*c[9]+1.00000

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
