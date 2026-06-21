# Size of variable arrays:
sizeAlgebraic = 12
sizeStates = 1
sizeConstants = 11
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (minute)"
    legend_constants[0] = "VP in component red_cells_and_viscosity (litre)"
    legend_states[0] = "VRC in component RBC_volume (litre)"
    legend_algebraic[2] = "HM in component hematocrit_fraction (dimensionless)"
    legend_algebraic[1] = "HM1 in component hematocrit_fraction (dimensionless)"
    legend_algebraic[0] = "VB in component hematocrit_fraction (litre)"
    legend_algebraic[3] = "VIE in component viscosity_due_to_RBCs (dimensionless)"
    legend_constants[1] = "HMK in component parameter_values (dimensionless)"
    legend_constants[2] = "HKM in component parameter_values (dimensionless)"
    legend_algebraic[5] = "VIM in component blood_viscosity (dimensionless)"
    legend_algebraic[4] = "VIB in component blood_viscosity (dimensionless)"
    legend_algebraic[8] = "HM7 in component oxygen_stimulation (mmHg)"
    legend_constants[3] = "PO2AMB in component parameter_values (mmHg)"
    legend_constants[4] = "HM6 in component parameter_values (mmHg)"
    legend_constants[9] = "PO2AM1 in component oxygen_stimulation (mmHg)"
    legend_algebraic[6] = "HM3 in component oxygen_stimulation (mmHg)"
    legend_constants[10] = "HM4 in component oxygen_stimulation (mmHg)"
    legend_algebraic[7] = "HM5 in component oxygen_stimulation (mmHg)"
    legend_algebraic[9] = "RC1 in component RBC_production (L_per_minute)"
    legend_constants[5] = "HM8 in component parameter_values (L_per_minute_per_mmHg)"
    legend_constants[6] = "REK in component parameter_values (dimensionless)"
    legend_algebraic[10] = "RC2 in component RBC_destruction (L_per_minute)"
    legend_constants[7] = "RKC in component parameter_values (per_minute)"
    legend_constants[8] = "TRRBC in component parameter_values (L_per_minute)"
    legend_algebraic[11] = "RCD in component RBC_volume (L_per_minute)"
    legend_rates[0] = "d/dt VRC in component RBC_volume (litre)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    constants[0] = 3.00449
    states[0] = 2.00439
    constants[1] = 90
    constants[2] = 0.53333
    constants[3] = 150
    constants[4] = 1850
    constants[5] = 4.714e-08
    constants[6] = 1
    constants[7] = 5.8e-06
    constants[8] = 0
    constants[9] = custom_piecewise([greater(constants[3] , 80.0000), 80.0000 , True, constants[3]])
    constants[10] = constants[3]-40.0000
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[0] = constants[0]+states[0]
    algebraic[1] = states[0]/algebraic[0]
    algebraic[2] = 100.000*algebraic[1]
    algebraic[6] = (constants[9]-40.0000)*algebraic[2]
    algebraic[7] = custom_piecewise([less(algebraic[6]+constants[10] , 0.00000), 0.00000 , True, algebraic[6]+constants[10]])
    algebraic[8] = constants[4]-algebraic[7]
    algebraic[9] = custom_piecewise([less(algebraic[8]*constants[5]*constants[6]+5.00000e-06 , 0.00000), 0.00000 , True, algebraic[8]*constants[5]*constants[6]+5.00000e-06])
    algebraic[3] = algebraic[2]/((constants[1]-algebraic[2])*constants[2])
    algebraic[4] = algebraic[3]+1.50000
    algebraic[5] = 0.333300*algebraic[4]
    algebraic[10] = states[0]*constants[7]*algebraic[5]
    algebraic[11] = (algebraic[9]-algebraic[10])+constants[8]
    rates[0] = algebraic[11]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = constants[0]+states[0]
    algebraic[1] = states[0]/algebraic[0]
    algebraic[2] = 100.000*algebraic[1]
    algebraic[6] = (constants[9]-40.0000)*algebraic[2]
    algebraic[7] = custom_piecewise([less(algebraic[6]+constants[10] , 0.00000), 0.00000 , True, algebraic[6]+constants[10]])
    algebraic[8] = constants[4]-algebraic[7]
    algebraic[9] = custom_piecewise([less(algebraic[8]*constants[5]*constants[6]+5.00000e-06 , 0.00000), 0.00000 , True, algebraic[8]*constants[5]*constants[6]+5.00000e-06])
    algebraic[3] = algebraic[2]/((constants[1]-algebraic[2])*constants[2])
    algebraic[4] = algebraic[3]+1.50000
    algebraic[5] = 0.333300*algebraic[4]
    algebraic[10] = states[0]*constants[7]*algebraic[5]
    algebraic[11] = (algebraic[9]-algebraic[10])+constants[8]
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
        self.VP = 3.00449
        self.HMK = 90
        self.HKM = 0.53333
        self.PO2AMB = 150
        self.HM6 = 1850
        self.HM8 = 4.714e-08
        self.REK = 1
        self.RKC = 5.8e-06
        self.TRRBC = 0

    def to_dict(self):
        return {
            "VP": self.VP,
            "HMK": self.HMK,
            "HKM": self.HKM,
            "PO2AMB": self.PO2AMB,
            "HM6": self.HM6,
            "HM8": self.HM8,
            "REK": self.REK,
            "RKC": self.RKC,
            "TRRBC": self.TRRBC,
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
        y0=[2.00439],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "guyton_red_cells_and_viscosity_2008"
        self.curve_names = [
            "VRC",
        ]
        self.state_names = ['VRC']
        self.algebraic_names = ['VB', 'HM1', 'HM', 'VIE', 'VIB', 'VIM', 'HM3', 'HM5', 'HM7', 'RC1', 'RC2', 'RCD']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 11
        p = self.params

        # direct mapping
        c[0] = p.VP
        c[1] = p.HMK
        c[2] = p.HKM
        c[3] = p.PO2AMB
        c[4] = p.HM6
        c[5] = p.HM8
        c[6] = p.REK
        c[7] = p.RKC
        c[8] = p.TRRBC

        # derived constants
        c[9] = (80.0000 if (c[3] > 80.0000) else c[3])
        c[10] = c[3]-40.0000

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
