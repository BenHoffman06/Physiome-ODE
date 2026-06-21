# Size of variable arrays:
sizeAlgebraic = 2
sizeStates = 7
sizeConstants = 8
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (second)"
    legend_states[0] = "Ca_t in component equations (uM_per_kg)"
    legend_states[1] = "TnCa_t in component equations (uM_per_kg)"
    legend_states[2] = "CB_on_t in component equations (uM_per_kg)"
    legend_states[3] = "Ca_released in component equations (uM_per_kg)"
    legend_states[4] = "Ca_sequestered in component equations (uM_per_kg)"
    legend_states[5] = "cumCB_on_t in component equations (uM_per_kg)"
    legend_states[6] = "cumCB_off_t in component equations (uM_per_kg)"
    legend_algebraic[0] = "Ca_release_rate in component equations (uM_per_kg_per_second)"
    legend_algebraic[1] = "dTnCa_t_dt in component equations (uM_per_kg_per_second)"
    legend_constants[0] = "Ca_tot_released in component equations (uM_per_kg)"
    legend_constants[1] = "total_Tn in component equations (uM_per_kg)"
    legend_constants[2] = "total_CB in component equations (uM_per_kg)"
    legend_constants[3] = "k_1 in component equations (kg_per_uM_per_second)"
    legend_constants[4] = "k_2 in component equations (per_second)"
    legend_constants[5] = "k_3 in component equations (per_second)"
    legend_constants[6] = "f in component equations (kg_per_uM_per_second)"
    legend_constants[7] = "g in component equations (per_second)"
    legend_rates[0] = "d/dt Ca_t in component equations (uM_per_kg)"
    legend_rates[1] = "d/dt TnCa_t in component equations (uM_per_kg)"
    legend_rates[2] = "d/dt CB_on_t in component equations (uM_per_kg)"
    legend_rates[3] = "d/dt Ca_released in component equations (uM_per_kg)"
    legend_rates[4] = "d/dt Ca_sequestered in component equations (uM_per_kg)"
    legend_rates[5] = "d/dt cumCB_on_t in component equations (uM_per_kg)"
    legend_rates[6] = "d/dt cumCB_off_t in component equations (uM_per_kg)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 0
    states[1] = 0
    states[2] = 0
    states[3] = 0
    states[4] = 0
    states[5] = 0
    states[6] = 0
    constants[0] = 35
    constants[1] = 70
    constants[2] = 150
    constants[3] = 5e6
    constants[4] = 10
    constants[5] = 1000
    constants[6] = 0.4e6
    constants[7] = 10
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[1] = constants[3]*states[0]*(constants[1]-states[1])-constants[4]*states[1]
    rates[2] = constants[6]*states[1]*(constants[2]-states[2])-constants[7]*states[2]
    rates[4] = constants[5]*states[0]
    rates[5] = constants[6]*states[1]*(constants[2]-states[2])
    rates[6] = constants[7]*states[2]
    algebraic[0] = custom_piecewise([greater(voi , 0.100000), 0.00000 , True, 20.0000*constants[0]*(1.00000-10.0000*voi)])
    rates[3] = algebraic[0]
    algebraic[1] = constants[3]*states[0]*(constants[1]-states[1])-constants[4]*states[1]
    rates[0] = (algebraic[0]-constants[5]*states[0])-algebraic[1]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = custom_piecewise([greater(voi , 0.100000), 0.00000 , True, 20.0000*constants[0]*(1.00000-10.0000*voi)])
    algebraic[1] = constants[3]*states[0]*(constants[1]-states[1])-constants[4]*states[1]
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
        self.Ca_tot_released = 35
        self.total_Tn = 70
        self.total_CB = 150
        self.k_1 = 5e6
        self.k_2 = 10
        self.k_3 = 1000
        self.f = 0.4e6
        self.g = 10

    def to_dict(self):
        return {
            "Ca_tot_released": self.Ca_tot_released,
            "total_Tn": self.total_Tn,
            "total_CB": self.total_CB,
            "k_1": self.k_1,
            "k_2": self.k_2,
            "k_3": self.k_3,
            "f": self.f,
            "g": self.g,
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
        y0=[0, 0, 0, 0, 0, 0, 0],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "mikane_araki_kohno_nakayama_suzuki_shimuzi_matsubara_hirakawa_takaki_suga_1997"
        self.curve_names = [
            "Ca_t",
            "TnCa_t",
            "CB_on_t",
            "Ca_released",
            "Ca_sequestered",
            "cumCB_on_t",
            "cumCB_off_t",
        ]
        self.state_names = ['Ca_t', 'TnCa_t', 'CB_on_t', 'Ca_released', 'Ca_sequestered', 'cumCB_on_t', 'cumCB_off_t']
        self.algebraic_names = ['Ca_release_rate', 'dTnCa_t_dt']
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
        c[0] = p.Ca_tot_released
        c[1] = p.total_Tn
        c[2] = p.total_CB
        c[3] = p.k_1
        c[4] = p.k_2
        c[5] = p.k_3
        c[6] = p.f
        c[7] = p.g

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
