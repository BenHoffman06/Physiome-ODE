# Size of variable arrays:
sizeAlgebraic = 0
sizeStates = 1
sizeConstants = 19
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (minute)"
    legend_constants[0] = "ADHC in component thirst_drinking_and_salt_appetite (dimensionless)"
    legend_constants[1] = "ANM in component thirst_drinking_and_salt_appetite (dimensionless)"
    legend_constants[2] = "POT in component thirst_drinking_and_salt_appetite (mmHg)"
    legend_constants[12] = "STH in component effect_of_salt_appetite_stimulation_on_thirst (dimensionless)"
    legend_constants[3] = "ANMSLT in component parameter_values (dimensionless)"
    legend_constants[4] = "Z10 in component parameter_values (mmHg)"
    legend_constants[5] = "Z11 in component parameter_values (per_mmHg2)"
    legend_constants[10] = "ANMSML in component effect_of_salt_appetite_stimulation_on_thirst (dimensionless)"
    legend_constants[11] = "STH1 in component effect_of_salt_appetite_stimulation_on_thirst (dimensionless)"
    legend_constants[13] = "AHCM in component effect_of_antidiuretic_hormone_on_thirst (dimensionless)"
    legend_constants[6] = "AHTHM in component parameter_values (dimensionless)"
    legend_constants[14] = "ANMTH in component effect_of_angiotensin_on_thirst (dimensionless)"
    legend_constants[7] = "ANMTM in component parameter_values (dimensionless)"
    legend_states[0] = "TVD in component rate_of_fluid_intake (L_per_minute)"
    legend_constants[8] = "DR in component parameter_values (L_per_minute)"
    legend_constants[9] = "TVDDL in component parameter_values (minute)"
    legend_constants[16] = "AHTH in component rate_of_fluid_intake (dimensionless)"
    legend_constants[15] = "AHTH1 in component rate_of_fluid_intake (dimensionless)"
    legend_constants[18] = "TVZ in component rate_of_fluid_intake (L_per_minute)"
    legend_constants[17] = "TVZ1 in component rate_of_fluid_intake (L_per_minute)"
    legend_rates[0] = "d/dt TVD in component rate_of_fluid_intake (L_per_minute)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    constants[0] = 1.0
    constants[1] = 0.987545
    constants[2] = 35.1148
    constants[3] = 2
    constants[4] = 45
    constants[5] = 0.01
    constants[6] = 2
    constants[7] = 1.5
    states[0] = 0.000980838
    constants[8] = 0
    constants[9] = 30
    constants[10] = (constants[1]-1.00000)*constants[3]+1.00000
    constants[11] = (power(constants[4]-constants[2], 2.00000))*constants[5]*constants[10]
    constants[12] = custom_piecewise([less(constants[11] , 0.800000), 0.800000 , greater(constants[11] , 8.00000), 8.00000 , True, constants[11]])
    constants[13] = (constants[0]-1.00000)*constants[6]+1.00000
    constants[14] = (constants[1]-1.00000)*constants[7]*0.00100000
    constants[15] = constants[13]*constants[12]*0.00100000
    constants[16] = custom_piecewise([less(constants[15] , 0.00000), 0.00000 , True, constants[15]])
    constants[17] = (constants[14]+constants[16])*1.00000
    constants[18] = custom_piecewise([less(constants[17] , 0.00000), 0.00000 , True, constants[17]])
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[0] = ((constants[18]+constants[8])-states[0])/constants[9]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
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
        self.ADHC = 1.0
        self.ANM = 0.987545
        self.POT = 35.1148
        self.ANMSLT = 2
        self.Z10 = 45
        self.Z11 = 0.01
        self.AHTHM = 2
        self.ANMTM = 1.5
        self.DR = 0
        self.TVDDL = 30

    def to_dict(self):
        return {
            "ADHC": self.ADHC,
            "ANM": self.ANM,
            "POT": self.POT,
            "ANMSLT": self.ANMSLT,
            "Z10": self.Z10,
            "Z11": self.Z11,
            "AHTHM": self.AHTHM,
            "ANMTM": self.ANMTM,
            "DR": self.DR,
            "TVDDL": self.TVDDL,
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
        y0=[0.000980838],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "guyton_thirst_drinking_and_salt_appetite_2008"
        self.curve_names = [
            "TVD",
        ]
        self.state_names = ['TVD']
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
        c = [0.0] * 19
        p = self.params

        # direct mapping
        c[0] = p.ADHC
        c[1] = p.ANM
        c[2] = p.POT
        c[3] = p.ANMSLT
        c[4] = p.Z10
        c[5] = p.Z11
        c[6] = p.AHTHM
        c[7] = p.ANMTM
        c[8] = p.DR
        c[9] = p.TVDDL

        # derived constants
        c[10] = (c[1]-1.00000)*c[3]+1.00000
        c[11] = (power(c[4]-c[2], 2.00000))*c[5]*c[10]
        c[12] = custom_piecewise([less(c[11] , 0.800000), 0.800000 , greater(c[11] , 8.00000), 8.00000 , True, c[11]])
        c[13] = (c[0]-1.00000)*c[6]+1.00000
        c[14] = (c[1]-1.00000)*c[7]*0.00100000
        c[15] = c[13]*c[12]*0.00100000
        c[16] = (0.00000 if (c[15] < 0.00000) else c[15])
        c[17] = (c[14]+c[16])*1.00000
        c[18] = (0.00000 if (c[17] < 0.00000) else c[17])

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
