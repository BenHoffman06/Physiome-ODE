# Size of variable arrays:
sizeAlgebraic = 3
sizeStates = 2
sizeConstants = 15
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (week)"
    legend_algebraic[0] = "rem_time in component environment (week)"
    legend_algebraic[2] = "Exposure in component environment (mg)"
    legend_constants[0] = "Dose in component environment (mg)"
    legend_constants[1] = "Dose_Int1 in component environment (week)"
    legend_constants[2] = "Dose_Int2 in component environment (week)"
    legend_constants[3] = "Dose_Length in component environment (week)"
    legend_constants[4] = "Cycle_Int in component environment (week)"
    legend_constants[5] = "N_Cycle in component environment (dimensionless)"
    legend_constants[6] = "conversion_factor in component environment (sec_per_week)"
    legend_algebraic[1] = "Effect in component effect_compartment (dimensionless)"
    legend_states[0] = "Ce in component effect_compartment (mg)"
    legend_constants[7] = "E_max in component effect_compartment (dimensionless)"
    legend_constants[8] = "Amt_50 in component effect_compartment (mg)"
    legend_constants[12] = "k_1 in component effect_compartment (per_week)"
    legend_constants[9] = "t_half_eq in component effect_compartment (week)"
    legend_states[1] = "Size in component response_compartment (cm)"
    legend_constants[10] = "Size_0 in component response_compartment (cm)"
    legend_constants[14] = "RateIn in component response_compartment (per_week)"
    legend_constants[11] = "T_Turnover in component response_compartment (cm_week)"
    legend_constants[13] = "k_2 in component response_compartment (per_cm_per_week)"
    legend_rates[0] = "d/dt Ce in component effect_compartment (mg)"
    legend_rates[1] = "d/dt Size in component response_compartment (cm)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    constants[0] = 5203.84
    constants[1] = 0
    constants[2] = 1
    constants[3] = 0.44359
    constants[4] = 3
    constants[5] = 6
    constants[6] = 604800
    states[0] = 0
    constants[7] = 1
    constants[8] = 10600
    constants[9] = 7.67
    states[1] = 6.66
    constants[10] = 6.66
    constants[11] = 21.8
    constants[12] = log(2.00000)/constants[9]
    constants[13] = log(2.00000)/constants[11]
    constants[14] = constants[10]*constants[13]
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[1] = 1.00000-(constants[7]*states[0])/(constants[8]+states[0])
    rates[1] = (constants[14]*algebraic[1]-constants[13]*states[1])*states[1]
    algebraic[0] = ( voi*constants[6] % constants[4]*constants[6])/constants[6]
    algebraic[2] = custom_piecewise([less(voi , constants[4]*constants[5]) & less(constants[1] , algebraic[0]) & less(algebraic[0] , constants[3]), constants[0] , less(voi , constants[4]*constants[5]) & less(constants[2] , algebraic[0]) & less(algebraic[0] , constants[2]+constants[3]), constants[0] , True, 0.00000])
    rates[0] = algebraic[2]/1.00000-states[0]*constants[12]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[1] = 1.00000-(constants[7]*states[0])/(constants[8]+states[0])
    algebraic[0] = ( voi*constants[6] % constants[4]*constants[6])/constants[6]
    algebraic[2] = custom_piecewise([less(voi , constants[4]*constants[5]) & less(constants[1] , algebraic[0]) & less(algebraic[0] , constants[3]), constants[0] , less(voi , constants[4]*constants[5]) & less(constants[2] , algebraic[0]) & less(algebraic[0] , constants[2]+constants[3]), constants[0] , True, 0.00000])
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
        self.Dose = 5203.84
        self.Dose_Int1 = 0
        self.Dose_Int2 = 1
        self.Dose_Length = 0.44359
        self.Cycle_Int = 3
        self.N_Cycle = 6
        self.conversion_factor = 604800
        self.E_max = 1
        self.Amt_50 = 10600
        self.t_half_eq = 7.67
        self.Size_0 = 6.66
        self.T_Turnover = 21.8

    def to_dict(self):
        return {
            "Dose": self.Dose,
            "Dose_Int1": self.Dose_Int1,
            "Dose_Int2": self.Dose_Int2,
            "Dose_Length": self.Dose_Length,
            "Cycle_Int": self.Cycle_Int,
            "N_Cycle": self.N_Cycle,
            "conversion_factor": self.conversion_factor,
            "E_max": self.E_max,
            "Amt_50": self.Amt_50,
            "t_half_eq": self.t_half_eq,
            "Size_0": self.Size_0,
            "T_Turnover": self.T_Turnover,
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
        y0=[0, 6.66],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "tham_2008"
        self.curve_names = [
            "Ce",
            "Size",
        ]
        self.state_names = ['Ce', 'Size']
        self.algebraic_names = ['rem_time', 'Effect', 'Exposure']
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
        c[0] = p.Dose
        c[1] = p.Dose_Int1
        c[2] = p.Dose_Int2
        c[3] = p.Dose_Length
        c[4] = p.Cycle_Int
        c[5] = p.N_Cycle
        c[6] = p.conversion_factor
        c[7] = p.E_max
        c[8] = p.Amt_50
        c[9] = p.t_half_eq
        c[10] = p.Size_0
        c[11] = p.T_Turnover

        # derived constants
        c[12] = log(2.00000)/c[9]
        c[13] = log(2.00000)/c[11]
        c[14] = c[10]*c[13]

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
