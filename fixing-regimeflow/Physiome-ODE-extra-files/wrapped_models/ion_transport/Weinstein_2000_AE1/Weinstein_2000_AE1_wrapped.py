# Size of variable arrays:
sizeAlgebraic = 15
sizeStates = 1
sizeConstants = 17
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (second)"
    legend_states[0] = "HCO3_i in component Concentrations (mM)"
    legend_constants[0] = "HCO3_e in component Concentrations (mM)"
    legend_constants[1] = "Cl_i in component Concentrations (mM)"
    legend_constants[2] = "Cl_e in component Concentrations (mM)"
    legend_constants[3] = "x_Tmax in component Concentrations (nmol_per_cm2)"
    legend_algebraic[0] = "x_T in component Concentrations (nmol_per_cm2)"
    legend_constants[4] = "K_I in component AE1_rate_constants (mM)"
    legend_constants[5] = "Kc_p in component AE1_rate_constants (mM)"
    legend_constants[6] = "Kc_pp in component AE1_rate_constants (mM)"
    legend_constants[7] = "Kb_p in component AE1_rate_constants (mM)"
    legend_constants[8] = "Kb_pp in component AE1_rate_constants (mM)"
    legend_constants[9] = "Pc_p in component AE1_rate_constants (per_s)"
    legend_constants[10] = "Pc_pp in component AE1_rate_constants (per_s)"
    legend_constants[11] = "Pb_p in component AE1_rate_constants (per_s)"
    legend_constants[12] = "Pb_pp in component AE1_rate_constants (per_s)"
    legend_constants[13] = "beta_p in component AE1 (dimensionless)"
    legend_algebraic[1] = "beta_pp in component AE1 (dimensionless)"
    legend_constants[14] = "gamma_p in component AE1 (dimensionless)"
    legend_constants[15] = "gamma_pp in component AE1 (dimensionless)"
    legend_algebraic[8] = "sigma in component AE1 (per_s)"
    legend_algebraic[9] = "x_p in component AE1 (nmol_per_cm2)"
    legend_algebraic[10] = "x_pp in component AE1 (nmol_per_cm2)"
    legend_algebraic[11] = "J_HCO3 in component AE1 (nmol_per_s_per_cm2)"
    legend_algebraic[14] = "J_Cl in component AE1 (nmol_per_s_per_cm2)"
    legend_algebraic[12] = "Jb_influx in component AE1 (nmol_per_s_per_cm2)"
    legend_algebraic[13] = "Jc_influx in component AE1 (nmol_per_s_per_cm2)"
    legend_algebraic[2] = "Jo_bm in component AE1 (nmol_per_s_per_cm2)"
    legend_algebraic[3] = "Ji_bm in component AE1 (nmol_per_s_per_cm2)"
    legend_algebraic[4] = "Js_bm in component AE1 (nmol_per_s_per_cm2)"
    legend_algebraic[5] = "Jo_cm in component AE1 (nmol_per_s_per_cm2)"
    legend_algebraic[6] = "Ji_cm in component AE1 (nmol_per_s_per_cm2)"
    legend_algebraic[7] = "Js_cm in component AE1 (nmol_per_s_per_cm2)"
    legend_rates[0] = "d/dt HCO3_i in component Concentrations (mM)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 0
    constants[0] = 26
    constants[1] = 29
    constants[2] = 114
    constants[3] = 1
    constants[4] = 172
    constants[5] = 50
    constants[6] = 50
    constants[7] = 198
    constants[8] = 198
    constants[9] = 562
    constants[10] = 61
    constants[11] = 1247
    constants[12] = 135
    constants[13] = constants[0]/constants[7]
    constants[16] = 60.0000
    constants[14] = constants[2]/constants[5]
    constants[15] = constants[1]/constants[6]
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[0] = constants[16]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = constants[3]/(1.00000+states[0]/constants[4])
    algebraic[1] = states[0]/constants[8]
    algebraic[2] = power((1.00000/algebraic[0])*(1.00000/constants[11]+1.00000/constants[12]+constants[8]/(constants[12]*states[0])), -1.00000)
    algebraic[3] = power((1.00000/algebraic[0])*(1.00000/constants[11]+1.00000/constants[12]+constants[7]/(constants[11]*constants[0])), -1.00000)
    algebraic[4] = power((1.00000/algebraic[0])*(1.00000/constants[11]+1.00000/constants[12]), -1.00000)
    algebraic[5] = power((1.00000/algebraic[0])*(1.00000/constants[9]+1.00000/constants[10]+constants[6]/(constants[10]*constants[1])), -1.00000)
    algebraic[6] = power((1.00000/algebraic[0])*(1.00000/constants[9]+1.00000/constants[10]+constants[5]/(constants[9]*constants[2])), -1.00000)
    algebraic[7] = power((1.00000/algebraic[0])*(1.00000/constants[9]+1.00000/constants[10]), -1.00000)
    algebraic[8] = (1.00000+constants[13]+constants[14])*(constants[12]*algebraic[1]+constants[10]*constants[15])+(1.00000+algebraic[1]+constants[15])*(constants[11]*constants[13]+constants[9]*constants[14])
    algebraic[9] = (algebraic[0]*(constants[12]*algebraic[1]+constants[10]*constants[15]))/algebraic[8]
    algebraic[10] = (algebraic[0]*(constants[11]*constants[13]+constants[9]*constants[14]))/algebraic[8]
    algebraic[11] = (algebraic[0]/algebraic[8])*(constants[12]*algebraic[1]*constants[9]*constants[14]-constants[11]*constants[13]*constants[10]*constants[15])
    algebraic[12] = (algebraic[0]/algebraic[8])*constants[11]*constants[13]*(constants[12]*algebraic[1]+constants[10]*constants[15])
    algebraic[13] = (algebraic[0]/algebraic[8])*constants[9]*constants[14]*(constants[12]*algebraic[1]+constants[10]*constants[15])
    algebraic[14] = -algebraic[11]
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
        self.HCO3_e = 26
        self.Cl_i = 29
        self.Cl_e = 114
        self.x_Tmax = 1
        self.K_I = 172
        self.Kc_p = 50
        self.Kc_pp = 50
        self.Kb_p = 198
        self.Kb_pp = 198
        self.Pc_p = 562
        self.Pc_pp = 61
        self.Pb_p = 1247
        self.Pb_pp = 135
        self.legend_constants_16 = 60.0000

    def to_dict(self):
        return {
            "HCO3_e": self.HCO3_e,
            "Cl_i": self.Cl_i,
            "Cl_e": self.Cl_e,
            "x_Tmax": self.x_Tmax,
            "K_I": self.K_I,
            "Kc_p": self.Kc_p,
            "Kc_pp": self.Kc_pp,
            "Kb_p": self.Kb_p,
            "Kb_pp": self.Kb_pp,
            "Pc_p": self.Pc_p,
            "Pc_pp": self.Pc_pp,
            "Pb_p": self.Pb_p,
            "Pb_pp": self.Pb_pp,
            "legend_constants_16": self.legend_constants_16,
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
        y0=[0],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "Weinstein_2000_AE1"
        self.curve_names = [
            "HCO3_i",
        ]
        self.state_names = ['HCO3_i']
        self.algebraic_names = ['x_T', 'beta_pp', 'Jo_bm', 'Ji_bm', 'Js_bm', 'Jo_cm', 'Ji_cm', 'Js_cm', 'sigma', 'x_p', 'x_pp', 'J_HCO3', 'Jb_influx', 'Jc_influx', 'J_Cl']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 17
        p = self.params

        # direct mapping
        c[0] = p.HCO3_e
        c[1] = p.Cl_i
        c[2] = p.Cl_e
        c[3] = p.x_Tmax
        c[4] = p.K_I
        c[5] = p.Kc_p
        c[6] = p.Kc_pp
        c[7] = p.Kb_p
        c[8] = p.Kb_pp
        c[9] = p.Pc_p
        c[10] = p.Pc_pp
        c[11] = p.Pb_p
        c[12] = p.Pb_pp
        c[16] = p.legend_constants_16

        # derived constants
        c[13] = c[0]/c[7]
        c[14] = c[2]/c[5]
        c[15] = c[1]/c[6]

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
