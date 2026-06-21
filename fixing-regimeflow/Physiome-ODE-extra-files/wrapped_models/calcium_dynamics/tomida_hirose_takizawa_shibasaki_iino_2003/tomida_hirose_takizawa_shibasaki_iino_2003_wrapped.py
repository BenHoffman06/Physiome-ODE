# Size of variable arrays:
sizeAlgebraic = 9
sizeStates = 3
sizeConstants = 8
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component model (minute)"
    legend_states[0] = "NFATP_cyt in component model (molecule)"
    legend_states[1] = "NFAT_cyt in component model (molecule)"
    legend_states[2] = "NFAT_nuc in component model (molecule)"
    legend_algebraic[0] = "NFAT_tot in component model (molecule)"
    legend_constants[0] = "k1_unstim in component model (per_minute)"
    legend_constants[1] = "k1_stim in component model (per_minute)"
    legend_algebraic[2] = "k1 in component model (per_minute)"
    legend_constants[2] = "k2 in component model (per_minute)"
    legend_constants[3] = "k3 in component model (per_minute)"
    legend_constants[4] = "k4 in component model (per_minute)"
    legend_constants[5] = "stim_wavelength in component model (minute)"
    legend_constants[6] = "stim_duration in component model (minute)"
    legend_algebraic[1] = "stim_on in component model (dimensionless)"
    legend_constants[7] = "time_before_stim in component model (minute)"
    legend_algebraic[6] = "Jdephosphorylation in component model (molecules_per_minute)"
    legend_algebraic[7] = "Jtranslocate in component model (molecules_per_minute)"
    legend_algebraic[8] = "Jexport in component model (molecules_per_minute)"
    legend_algebraic[3] = "percentage_NFAT_cyt in component model (dimensionless)"
    legend_algebraic[4] = "percentage_NFATP_cyt in component model (dimensionless)"
    legend_algebraic[5] = "percentage_NFAT_nuc in component model (dimensionless)"
    legend_rates[0] = "d/dt NFATP_cyt in component model (molecule)"
    legend_rates[1] = "d/dt NFAT_cyt in component model (molecule)"
    legend_rates[2] = "d/dt NFAT_nuc in component model (molecule)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 5000
    states[1] = 0
    states[2] = 0
    constants[0] = 0
    constants[1] = 0.359
    constants[2] = 0.147
    constants[3] = 0.06
    constants[4] = 0.035
    constants[5] = 3
    constants[6] = 0.5
    constants[7] = 1
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[1] = custom_piecewise([greater_equal(voi , constants[7]) & less_equal( voi-constants[7] % constants[5] , constants[6]), 1.00000 , True, 0.00000])
    algebraic[2] = custom_piecewise([equal(algebraic[1] , 1.00000), constants[1] , True, constants[0]])
    algebraic[6] = algebraic[2]*states[0]-constants[2]*states[1]
    algebraic[7] = constants[3]*states[1]
    rates[1] = algebraic[6]-algebraic[7]
    algebraic[8] = constants[4]*states[2]
    rates[0] = algebraic[8]-algebraic[6]
    rates[2] = algebraic[7]-algebraic[8]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[1] = custom_piecewise([greater_equal(voi , constants[7]) & less_equal( voi-constants[7] % constants[5] , constants[6]), 1.00000 , True, 0.00000])
    algebraic[2] = custom_piecewise([equal(algebraic[1] , 1.00000), constants[1] , True, constants[0]])
    algebraic[6] = algebraic[2]*states[0]-constants[2]*states[1]
    algebraic[7] = constants[3]*states[1]
    algebraic[8] = constants[4]*states[2]
    algebraic[0] = states[0]+states[1]+states[2]
    algebraic[3] = (states[1]*100.000)/algebraic[0]
    algebraic[4] = (states[0]*100.000)/algebraic[0]
    algebraic[5] = (states[2]*100.000)/algebraic[0]
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
        self.k1_unstim = 0
        self.k1_stim = 0.359
        self.k2 = 0.147
        self.k3 = 0.06
        self.k4 = 0.035
        self.stim_wavelength = 3
        self.stim_duration = 0.5
        self.time_before_stim = 1

    def to_dict(self):
        return {
            "k1_unstim": self.k1_unstim,
            "k1_stim": self.k1_stim,
            "k2": self.k2,
            "k3": self.k3,
            "k4": self.k4,
            "stim_wavelength": self.stim_wavelength,
            "stim_duration": self.stim_duration,
            "time_before_stim": self.time_before_stim,
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
        y0=[5000, 0, 0],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "tomida_hirose_takizawa_shibasaki_iino_2003"
        self.curve_names = [
            "NFATP_cyt",
            "NFAT_cyt",
            "NFAT_nuc",
        ]
        self.state_names = ['NFATP_cyt', 'NFAT_cyt', 'NFAT_nuc']
        self.algebraic_names = ['NFAT_tot', 'stim_on', 'k1', 'percentage_NFAT_cyt', 'percentage_NFATP_cyt', 'percentage_NFAT_nuc', 'Jdephosphorylation', 'Jtranslocate', 'Jexport']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 8
        p = self.params

        # direct mapping
        c[0] = p.k1_unstim
        c[1] = p.k1_stim
        c[2] = p.k2
        c[3] = p.k3
        c[4] = p.k4
        c[5] = p.stim_wavelength
        c[6] = p.stim_duration
        c[7] = p.time_before_stim

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
