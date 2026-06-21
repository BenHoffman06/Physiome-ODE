# Size of variable arrays:
sizeAlgebraic = 3
sizeStates = 3
sizeConstants = 18
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (day)"
    legend_algebraic[2] = "S in component population_pharmacodynamics_model (units)"
    legend_constants[0] = "S0 in component population_pharmacodynamics_model (units)"
    legend_constants[1] = "alpha in component population_pharmacodynamics_model (units_per_day)"
    legend_constants[2] = "epsilon in component population_pharmacodynamics_model (units)"
    legend_algebraic[0] = "ADAS_Cog_p in component placebo_response_model (units)"
    legend_constants[14] = "PD_CeA in component drug_response_model (units)"
    legend_constants[3] = "beta_P in component placebo_response_model (units)"
    legend_constants[15] = "Keq_p in component placebo_response_model (per_day)"
    legend_constants[16] = "Kel_p in component placebo_response_model (per_day)"
    legend_constants[4] = "t_half_el_p in component placebo_response_model (day)"
    legend_constants[5] = "t_half_eq_p in component placebo_response_model (day)"
    legend_constants[17] = "CL in component pharmacokinetic_model (litre_per_day)"
    legend_constants[6] = "smk in component pharmacokinetic_model (dimensionless)"
    legend_constants[7] = "age in component pharmacokinetic_model (year)"
    legend_algebraic[1] = "Sv in component drop_out_model (dimensionless)"
    legend_constants[8] = "beta_a in component drug_response_model (units_ml_per_ng)"
    legend_constants[9] = "CeA in component drug_response_model (ng_per_ml)"
    legend_states[0] = "CC in component drug_clearance (mg_per_litre)"
    legend_states[1] = "PC in component drug_clearance (mg_per_litre)"
    legend_constants[10] = "Vc in component drug_clearance (litre)"
    legend_constants[11] = "Vp in component drug_clearance (litre)"
    legend_states[2] = "A_in in component drug_clearance (mg)"
    legend_constants[12] = "k_ab in component drug_clearance (per_day)"
    legend_constants[13] = "CL_ic in component drug_clearance (litre_per_day)"
    legend_rates[0] = "d/dt CC in component drug_clearance (mg_per_litre)"
    legend_rates[1] = "d/dt PC in component drug_clearance (mg_per_litre)"
    legend_rates[2] = "d/dt A_in in component drug_clearance (mg)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    constants[0] = 30
    constants[1] = 0.0164
    constants[2] = 0.0
    constants[3] = -3
    constants[4] = 7
    constants[5] = 6
    constants[6] = 1
    constants[7] = 40
    constants[8] = -0.047
    constants[9] = 25
    states[0] = 0
    states[1] = 0
    constants[10] = 172
    constants[11] = 222
    states[2] = 25
    constants[12] = 115.44
    constants[13] = 763.2
    constants[14] = constants[8]*constants[9]
    constants[15] = log(2.00000)/constants[5]
    constants[16] = log(2.00000)/constants[4]
    constants[17] = 2268.00*exp(-0.0135000*(constants[7]-40.0000))*constants[6]
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[0] = (constants[12]*states[2]-(constants[17]*states[0]+constants[13]*(states[0]-states[1])))/constants[10]
    rates[1] = (constants[13]*(states[0]-states[1]))/constants[11]
    rates[2] = -115.440*states[2]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = ((constants[3]*constants[15])/(constants[15]-constants[16]))*(exp(-constants[16]*voi)-exp(-constants[15]*voi))
    algebraic[1] = exp(-0.00145000*voi)
    algebraic[2] = constants[0]+constants[1]*voi+algebraic[0]+constants[14]+constants[2]
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
        self.S0 = 30
        self.alpha = 0.0164
        self.epsilon = 0.0
        self.beta_P = -3
        self.t_half_el_p = 7
        self.t_half_eq_p = 6
        self.smk = 1
        self.age = 40
        self.beta_a = -0.047
        self.CeA = 25
        self.Vc = 172
        self.Vp = 222
        self.k_ab = 115.44
        self.CL_ic = 763.2

    def to_dict(self):
        return {
            "S0": self.S0,
            "alpha": self.alpha,
            "epsilon": self.epsilon,
            "beta_P": self.beta_P,
            "t_half_el_p": self.t_half_el_p,
            "t_half_eq_p": self.t_half_eq_p,
            "smk": self.smk,
            "age": self.age,
            "beta_a": self.beta_a,
            "CeA": self.CeA,
            "Vc": self.Vc,
            "Vp": self.Vp,
            "k_ab": self.k_ab,
            "CL_ic": self.CL_ic,
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
        y0=[0, 0, 25],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "lockwood_ewy_hermann_holford_2006"
        self.curve_names = [
            "CC",
            "PC",
            "A_in",
        ]
        self.state_names = ['CC', 'PC', 'A_in']
        self.algebraic_names = ['ADAS_Cog_p', 'Sv', 'S']
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
        c[0] = p.S0
        c[1] = p.alpha
        c[2] = p.epsilon
        c[3] = p.beta_P
        c[4] = p.t_half_el_p
        c[5] = p.t_half_eq_p
        c[6] = p.smk
        c[7] = p.age
        c[8] = p.beta_a
        c[9] = p.CeA
        c[10] = p.Vc
        c[11] = p.Vp
        c[12] = p.k_ab
        c[13] = p.CL_ic

        # derived constants
        c[14] = c[8]*c[9]
        c[15] = log(2.00000)/c[5]
        c[16] = log(2.00000)/c[4]
        c[17] = 2268.00*exp(-0.0135000*(c[7]-40.0000))*c[6]

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
