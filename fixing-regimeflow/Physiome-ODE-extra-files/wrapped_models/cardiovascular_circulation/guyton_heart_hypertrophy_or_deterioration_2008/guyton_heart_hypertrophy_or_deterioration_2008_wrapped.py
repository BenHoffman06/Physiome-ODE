# Size of variable arrays:
sizeAlgebraic = 1
sizeStates = 3
sizeConstants = 10
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (minute)"
    legend_constants[0] = "QAO in component heart_hypertrophy_or_deterioration (L_per_minute)"
    legend_constants[1] = "PA in component heart_hypertrophy_or_deterioration (mmHg)"
    legend_constants[2] = "POT in component heart_hypertrophy_or_deterioration (mmHg)"
    legend_constants[3] = "PPA in component heart_hypertrophy_or_deterioration (mmHg)"
    legend_states[0] = "HPL in component left_ventricular_hypertrophy (dimensionless)"
    legend_constants[4] = "HSL in component parameter_values (dimensionless)"
    legend_constants[5] = "Z13 in component parameter_values (dimensionless)"
    legend_states[1] = "HPR in component right_ventricular_hypertrophy (dimensionless)"
    legend_constants[6] = "HSR in component parameter_values (dimensionless)"
    legend_algebraic[0] = "HMD in component heart_deterioration (dimensionless)"
    legend_constants[7] = "DHDTR in component parameter_values (per_mmHg_per_minute)"
    legend_states[2] = "HMD1 in component heart_deterioration (dimensionless)"
    legend_constants[8] = "DHM in component heart_deterioration (per_minute)"
    legend_rates[0] = "d/dt HPL in component left_ventricular_hypertrophy (dimensionless)"
    legend_rates[1] = "d/dt HPR in component right_ventricular_hypertrophy (dimensionless)"
    legend_rates[2] = "d/dt HMD1 in component heart_deterioration (dimensionless)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    constants[0] = 5.00707
    constants[1] = 103.525
    constants[2] = 35.1148
    constants[3] = 15.6376
    states[0] = 1.00163
    constants[4] = 1
    constants[5] = 0.625
    states[1] = 1.00237
    constants[6] = 1
    constants[7] = 0.05
    states[2] = 1.0
    constants[8] = (constants[2]-10.0000)*constants[7]
    constants[9] = constants[8]
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[2] = constants[9]
    rates[0] = (power((constants[1]*constants[0])/(500.000*constants[4]), constants[5])-states[0])/57600.0
    rates[1] = (power((constants[3]*constants[0])/(75.0000*constants[6]), constants[5])-states[1])/57600.0
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = custom_piecewise([greater(states[2] , 1.00000), 1.00000 , True, states[2]])
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
        self.QAO = 5.00707
        self.PA = 103.525
        self.POT = 35.1148
        self.PPA = 15.6376
        self.HSL = 1
        self.Z13 = 0.625
        self.HSR = 1
        self.DHDTR = 0.05

    def to_dict(self):
        return {
            "QAO": self.QAO,
            "PA": self.PA,
            "POT": self.POT,
            "PPA": self.PPA,
            "HSL": self.HSL,
            "Z13": self.Z13,
            "HSR": self.HSR,
            "DHDTR": self.DHDTR,
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
        y0=[1.00163, 1.00237, 1.0],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "guyton_heart_hypertrophy_or_deterioration_2008"
        self.curve_names = [
            "HPL",
            "HPR",
            "HMD1",
        ]
        self.state_names = ['HPL', 'HPR', 'HMD1']
        self.algebraic_names = ['HMD']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 10
        p = self.params

        # direct mapping
        c[0] = p.QAO
        c[1] = p.PA
        c[2] = p.POT
        c[3] = p.PPA
        c[4] = p.HSL
        c[5] = p.Z13
        c[6] = p.HSR
        c[7] = p.DHDTR

        # derived constants
        c[8] = (c[2]-10.0000)*c[7]
        c[9] = c[8]

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
