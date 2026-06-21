# Size of variable arrays:
sizeAlgebraic = 9
sizeStates = 5
sizeConstants = 28
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (millisecond)"
    legend_states[0] = "V in component membrane (millivolt)"
    legend_constants[0] = "Cm in component membrane (femtoF)"
    legend_algebraic[5] = "i_Ca in component calcium_current (picoA)"
    legend_algebraic[0] = "i_K in component rapidly_activating_K_current (picoA)"
    legend_algebraic[6] = "i_slow in component slow_K_current (picoA)"
    legend_algebraic[8] = "i_Na_Ca in component Na_Ca_exchanger_current (picoA)"
    legend_constants[1] = "V_K in component rapidly_activating_K_current (millivolt)"
    legend_constants[2] = "g_K in component rapidly_activating_K_current (picoS)"
    legend_states[1] = "n in component rapidly_activating_K_current_n_gate (dimensionless)"
    legend_algebraic[1] = "n_infinity in component rapidly_activating_K_current_n_gate (dimensionless)"
    legend_constants[3] = "lamda in component rapidly_activating_K_current_n_gate (dimensionless)"
    legend_constants[4] = "tau_n in component rapidly_activating_K_current_n_gate (millisecond)"
    legend_constants[5] = "V_n in component rapidly_activating_K_current_n_gate (millivolt)"
    legend_constants[6] = "S_n in component rapidly_activating_K_current_n_gate (millivolt)"
    legend_constants[7] = "V_Ca in component calcium_current (millivolt)"
    legend_constants[8] = "g_Ca in component calcium_current (picoS)"
    legend_algebraic[3] = "m_infinity in component calcium_current_m_gate (dimensionless)"
    legend_constants[9] = "V_m in component calcium_current_m_gate (millivolt)"
    legend_constants[10] = "S_m in component calcium_current_m_gate (millivolt)"
    legend_constants[11] = "g_s in component slow_K_current (picoS)"
    legend_states[2] = "s in component slow_K_current_s_gate (dimensionless)"
    legend_algebraic[2] = "s_infinity in component slow_K_current_s_gate (dimensionless)"
    legend_constants[12] = "tau_s in component slow_K_current_s_gate (millisecond)"
    legend_constants[13] = "V_s in component slow_K_current_s_gate (millivolt)"
    legend_constants[14] = "S_s in component slow_K_current_s_gate (millivolt)"
    legend_constants[15] = "R_s in component slow_K_current_s_gate (dimensionless)"
    legend_algebraic[4] = "S_V_R_s in component slow_K_current_s_gate (dimensionless)"
    legend_constants[16] = "g_Na_Ca in component Na_Ca_exchanger_current (picoS)"
    legend_constants[17] = "K_1_2 in component Na_Ca_exchanger_current (micromolar)"
    legend_algebraic[7] = "V_Na_Ca in component Na_Ca_exchanger_current (millivolt)"
    legend_constants[18] = "RT_F in component Na_Ca_exchanger_current (millivolt)"
    legend_constants[19] = "nH in component Na_Ca_exchanger_current (dimensionless)"
    legend_states[3] = "Ca_i in component ionic_concentrations (micromolar)"
    legend_constants[20] = "Ca_o in component ionic_concentrations (micromolar)"
    legend_constants[21] = "Na_i in component ionic_concentrations (millimolar)"
    legend_constants[22] = "Na_o in component ionic_concentrations (millimolar)"
    legend_states[4] = "Ca_ret in component ionic_concentrations (micromolar)"
    legend_constants[23] = "f in component ionic_concentrations (dimensionless)"
    legend_constants[24] = "k_Ca in component ionic_concentrations (per_millisecond)"
    legend_constants[25] = "k_rel in component ionic_concentrations (per_millisecond)"
    legend_constants[26] = "k_pump in component ionic_concentrations (per_millisecond)"
    legend_constants[27] = "alpha in component ionic_concentrations (mole_per_microlitre_coulomb)"
    legend_rates[0] = "d/dt V in component membrane (millivolt)"
    legend_rates[1] = "d/dt n in component rapidly_activating_K_current_n_gate (dimensionless)"
    legend_rates[2] = "d/dt s in component slow_K_current_s_gate (dimensionless)"
    legend_rates[3] = "d/dt Ca_i in component ionic_concentrations (micromolar)"
    legend_rates[4] = "d/dt Ca_ret in component ionic_concentrations (micromolar)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = -76.0
    constants[0] = 5310.0
    constants[1] = -75.0
    constants[2] = 2700.0
    states[1] = 0.1
    constants[3] = 1.0
    constants[4] = 20.0
    constants[5] = -16.0
    constants[6] = 5.6
    constants[7] = 25.0
    constants[8] = 1000.0
    constants[9] = -20.0
    constants[10] = 12.0
    constants[11] = 200.0
    states[2] = 0.1
    constants[12] = 12000.0
    constants[13] = -52.0
    constants[14] = 10.0
    constants[15] = 0.58
    constants[16] = 350.0
    constants[17] = 1.5
    constants[18] = 26.54
    constants[19] = 5.0
    states[3] = 0.52
    constants[20] = 2600.0
    constants[21] = 10.0
    constants[22] = 140.0
    states[4] = 0.7
    constants[23] = 0.02
    constants[24] = 0.64
    constants[25] = 0.0006
    constants[26] = 0.2
    constants[27] = 0.00006
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[4] = -constants[25]*(states[4]-states[3])+constants[26]*states[3]
    algebraic[1] = 1.00000/(1.00000+exp((constants[5]-states[0])/constants[6]))
    rates[1] = constants[3]*((algebraic[1]-states[1])/constants[4])
    algebraic[2] = 1.00000/(1.00000+exp((constants[13]-states[0])/constants[14]))
    algebraic[4] = algebraic[2]+constants[15]
    rates[2] = (algebraic[4]-states[2])/constants[12]
    algebraic[3] = 1.00000/(1.00000+exp((constants[9]-states[0])/constants[10]))
    algebraic[5] = constants[8]*algebraic[3]*(states[0]-constants[7])
    algebraic[0] = constants[2]*states[1]*(states[0]-constants[1])
    algebraic[6] = constants[11]*states[2]*(states[0]-constants[1])
    algebraic[7] = constants[18]*(3.00000*log(constants[22]/constants[21]-log(constants[20]/states[3])))
    algebraic[8] = constants[16]*((power(states[3], constants[19]))/(power(constants[17], constants[19])+power(states[3], constants[19])))*(states[0]-algebraic[7])
    rates[0] = -(algebraic[0]+algebraic[5]+algebraic[6]+algebraic[8])/constants[0]
    rates[3] = (constants[23]*(-constants[27]*(algebraic[5]-2.00000*algebraic[8])-constants[24]*states[3])+constants[25]*(states[4]-states[3]))-constants[26]*states[3]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[1] = 1.00000/(1.00000+exp((constants[5]-states[0])/constants[6]))
    algebraic[2] = 1.00000/(1.00000+exp((constants[13]-states[0])/constants[14]))
    algebraic[4] = algebraic[2]+constants[15]
    algebraic[3] = 1.00000/(1.00000+exp((constants[9]-states[0])/constants[10]))
    algebraic[5] = constants[8]*algebraic[3]*(states[0]-constants[7])
    algebraic[0] = constants[2]*states[1]*(states[0]-constants[1])
    algebraic[6] = constants[11]*states[2]*(states[0]-constants[1])
    algebraic[7] = constants[18]*(3.00000*log(constants[22]/constants[21]-log(constants[20]/states[3])))
    algebraic[8] = constants[16]*((power(states[3], constants[19]))/(power(constants[17], constants[19])+power(states[3], constants[19])))*(states[0]-algebraic[7])
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
        self.Cm = 5310.0
        self.V_K = -75.0
        self.g_K = 2700.0
        self.lamda = 1.0
        self.tau_n = 20.0
        self.V_n = -16.0
        self.S_n = 5.6
        self.V_Ca = 25.0
        self.g_Ca = 1000.0
        self.V_m = -20.0
        self.S_m = 12.0
        self.g_s = 200.0
        self.tau_s = 12000.0
        self.V_s = -52.0
        self.S_s = 10.0
        self.R_s = 0.58
        self.g_Na_Ca = 350.0
        self.K_1_2 = 1.5
        self.RT_F = 26.54
        self.nH = 5.0
        self.Ca_o = 2600.0
        self.Na_i = 10.0
        self.Na_o = 140.0
        self.f = 0.02
        self.k_Ca = 0.64
        self.k_rel = 0.0006
        self.k_pump = 0.2
        self.alpha = 0.00006

    def to_dict(self):
        return {
            "Cm": self.Cm,
            "V_K": self.V_K,
            "g_K": self.g_K,
            "lamda": self.lamda,
            "tau_n": self.tau_n,
            "V_n": self.V_n,
            "S_n": self.S_n,
            "V_Ca": self.V_Ca,
            "g_Ca": self.g_Ca,
            "V_m": self.V_m,
            "S_m": self.S_m,
            "g_s": self.g_s,
            "tau_s": self.tau_s,
            "V_s": self.V_s,
            "S_s": self.S_s,
            "R_s": self.R_s,
            "g_Na_Ca": self.g_Na_Ca,
            "K_1_2": self.K_1_2,
            "RT_F": self.RT_F,
            "nH": self.nH,
            "Ca_o": self.Ca_o,
            "Na_i": self.Na_i,
            "Na_o": self.Na_o,
            "f": self.f,
            "k_Ca": self.k_Ca,
            "k_rel": self.k_rel,
            "k_pump": self.k_pump,
            "alpha": self.alpha,
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
        y0=[-76.0, 0.1, 0.1, 0.52, 0.7],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "gall_susa_1999_b"
        self.curve_names = [
            "V",
            "n",
            "s",
            "Ca_i",
            "Ca_ret",
        ]
        self.state_names = ['V', 'n', 's', 'Ca_i', 'Ca_ret']
        self.algebraic_names = ['i_K', 'n_infinity', 's_infinity', 'm_infinity', 'S_V_R_s', 'i_Ca', 'i_slow', 'V_Na_Ca', 'i_Na_Ca']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 28
        p = self.params

        # direct mapping
        c[0] = p.Cm
        c[1] = p.V_K
        c[2] = p.g_K
        c[3] = p.lamda
        c[4] = p.tau_n
        c[5] = p.V_n
        c[6] = p.S_n
        c[7] = p.V_Ca
        c[8] = p.g_Ca
        c[9] = p.V_m
        c[10] = p.S_m
        c[11] = p.g_s
        c[12] = p.tau_s
        c[13] = p.V_s
        c[14] = p.S_s
        c[15] = p.R_s
        c[16] = p.g_Na_Ca
        c[17] = p.K_1_2
        c[18] = p.RT_F
        c[19] = p.nH
        c[20] = p.Ca_o
        c[21] = p.Na_i
        c[22] = p.Na_o
        c[23] = p.f
        c[24] = p.k_Ca
        c[25] = p.k_rel
        c[26] = p.k_pump
        c[27] = p.alpha

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
