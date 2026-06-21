# Size of variable arrays:
sizeAlgebraic = 2
sizeStates = 5
sizeConstants = 20
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "t in component environment (second)"
    legend_constants[0] = "D_Ca in component parameters (second)"
    legend_constants[1] = "k_1 in component parameters (per_second)"
    legend_constants[2] = "k_2 in component parameters (per_second)"
    legend_constants[3] = "f in component parameters (per_second)"
    legend_constants[4] = "g in component parameters (per_second)"
    legend_constants[5] = "Ca_max in component parameters (dimensionless)"
    legend_constants[6] = "Total_Tn in component parameters (dimensionless)"
    legend_constants[7] = "Total_CB in component parameters (dimensionless)"
    legend_algebraic[0] = "Ca_t in component Ca_t (dimensionless)"
    legend_states[0] = "TnCa in component TnCa (dimensionless)"
    legend_states[1] = "CB_on in component CB_on (dimensionless)"
    legend_states[2] = "CumCB_on in component CumCB (dimensionless)"
    legend_states[3] = "CumCB_off in component CumCB (dimensionless)"
    legend_algebraic[1] = "F in component force_development (force)"
    legend_states[4] = "FTI in component force_development (force_second)"
    legend_constants[15] = "FLA in component force_development (energy)"
    legend_constants[8] = "phi in component force_development (force)"
    legend_constants[9] = "s in component force_development (dimensionless)"
    legend_constants[10] = "L in component force_development (meter)"
    legend_constants[11] = "L_0 in component force_development (meter)"
    legend_constants[12] = "F_max in component force_development (force)"
    legend_constants[17] = "ATP in component ATP (dimensionless)"
    legend_constants[18] = "ATP_energy in component ATP (energy)"
    legend_constants[13] = "epsilon in component ATP (energy)"
    legend_constants[14] = "CumCB_on_end in component ATP (dimensionless)"
    legend_constants[19] = "Efficiency in component equations_main (dimensionless)"
    legend_constants[16] = "Economy in component equations_main (second_per_meter)"
    legend_rates[0] = "d/dt TnCa in component TnCa (dimensionless)"
    legend_rates[1] = "d/dt CB_on in component CB_on (dimensionless)"
    legend_rates[2] = "d/dt CumCB_on in component CumCB (dimensionless)"
    legend_rates[3] = "d/dt CumCB_off in component CumCB (dimensionless)"
    legend_rates[4] = "d/dt FTI in component force_development (force_second)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    constants[0] = 0.1
    constants[1] = 40
    constants[2] = 20
    constants[3] = 10
    constants[4] = 10
    constants[5] = 1
    constants[6] = 1
    constants[7] = 1
    states[0] = 0
    states[1] = 0
    states[2] = 0
    states[3] = 0
    states[4] = 0
    constants[8] = 1
    constants[9] = 1
    constants[10] = 1
    constants[11] = 0
    constants[12] = 0.228
    constants[13] = 1
    constants[14] = 1
    constants[15] = constants[12]*constants[9]*(constants[10]-constants[11])
    constants[16] = (constants[8]/constants[13])*(1.00000/constants[4])
    constants[17] = constants[14]
    constants[18] = constants[17]*constants[13]
    constants[19] = constants[15]/constants[18]
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[1] = constants[3]*states[0]*(constants[7]-states[1])-constants[4]*states[1]
    rates[2] = constants[3]*states[0]*(constants[7]-states[1])
    rates[3] = constants[4]*states[1]
    algebraic[0] = custom_piecewise([greater_equal(voi , 0.00000) & less(voi , 0.300000*constants[0]), (constants[5]*(1.00000+sin(( pi*(voi/constants[0]-0.150000))/0.300000)))/2.00000 , greater_equal(voi , 0.300000*constants[0]) & less(voi , constants[0]), (constants[5]*(1.00000-sin(( pi*(voi/constants[0]-0.650000))/0.700000)))/2.00000 , True, 0.00000])
    rates[0] = constants[1]*algebraic[0]*(constants[6]-states[0])-constants[2]*states[0]
    algebraic[1] = states[1]*constants[8]
    rates[4] = algebraic[1]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = custom_piecewise([greater_equal(voi , 0.00000) & less(voi , 0.300000*constants[0]), (constants[5]*(1.00000+sin(( pi*(voi/constants[0]-0.150000))/0.300000)))/2.00000 , greater_equal(voi , 0.300000*constants[0]) & less(voi , constants[0]), (constants[5]*(1.00000-sin(( pi*(voi/constants[0]-0.650000))/0.700000)))/2.00000 , True, 0.00000])
    algebraic[1] = states[1]*constants[8]
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
        self.D_Ca = 0.1
        self.k_1 = 40
        self.k_2 = 20
        self.f = 10
        self.g = 10
        self.Ca_max = 1
        self.Total_Tn = 1
        self.Total_CB = 1
        self.phi = 1
        self.s = 1
        self.L = 1
        self.L_0 = 0
        self.F_max = 0.228
        self.epsilon = 1
        self.CumCB_on_end = 1

    def to_dict(self):
        return {
            "D_Ca": self.D_Ca,
            "k_1": self.k_1,
            "k_2": self.k_2,
            "f": self.f,
            "g": self.g,
            "Ca_max": self.Ca_max,
            "Total_Tn": self.Total_Tn,
            "Total_CB": self.Total_CB,
            "phi": self.phi,
            "s": self.s,
            "L": self.L,
            "L_0": self.L_0,
            "F_max": self.F_max,
            "epsilon": self.epsilon,
            "CumCB_on_end": self.CumCB_on_end,
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
        y0=[0, 0, 0, 0, 0],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "yamaguchi_takaki_matsubara_yasuhara_suga_1996"
        self.curve_names = [
            "TnCa",
            "CB_on",
            "CumCB_on",
            "CumCB_off",
            "FTI",
        ]
        self.state_names = ['TnCa', 'CB_on', 'CumCB_on', 'CumCB_off', 'FTI']
        self.algebraic_names = ['Ca_t', 'F']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 20
        p = self.params

        # direct mapping
        c[0] = p.D_Ca
        c[1] = p.k_1
        c[2] = p.k_2
        c[3] = p.f
        c[4] = p.g
        c[5] = p.Ca_max
        c[6] = p.Total_Tn
        c[7] = p.Total_CB
        c[8] = p.phi
        c[9] = p.s
        c[10] = p.L
        c[11] = p.L_0
        c[12] = p.F_max
        c[13] = p.epsilon
        c[14] = p.CumCB_on_end

        # derived constants
        c[15] = c[12]*c[9]*(c[10]-c[11])
        c[16] = (c[8]/c[13])*(1.00000/c[4])
        c[17] = c[14]
        c[18] = c[17]*c[13]
        c[19] = c[15]/c[18]

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
