# Size of variable arrays:
sizeAlgebraic = 17
sizeStates = 7
sizeConstants = 40
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (millisecond)"
    legend_constants[0] = "V_cell in component environment (picoL)"
    legend_constants[1] = "Ca_e in component environment (millimolar)"
    legend_constants[2] = "K_e in component environment (millimolar)"
    legend_constants[3] = "K_i in component environment (millimolar)"
    legend_constants[4] = "V_tau in component environment (millivolt)"
    legend_constants[5] = "k_tau in component environment (millivolt)"
    legend_states[0] = "V in component membrane (millivolt)"
    legend_constants[6] = "R in component membrane (joule_per_kilomole_kelvin)"
    legend_constants[7] = "T in component membrane (kelvin)"
    legend_constants[8] = "F in component membrane (coulomb_per_mole)"
    legend_constants[9] = "Cm in component membrane (picoF)"
    legend_algebraic[5] = "i_Ca_L in component L_type_calcium_current (picoA)"
    legend_algebraic[8] = "i_Ca_T in component T_type_calcium_current (picoA)"
    legend_algebraic[11] = "i_K_DR in component voltage_sensitive_K_current (picoA)"
    legend_algebraic[13] = "i_K_Ca in component Ca_activated_K_current (picoA)"
    legend_algebraic[15] = "i_leak in component leak_current (picoA)"
    legend_algebraic[0] = "phi_Ca in component L_type_calcium_current (millivolt_millimolar)"
    legend_constants[10] = "g_Ca_L in component L_type_calcium_current (nanoS_per_millimolar)"
    legend_states[1] = "Ca_i in component cytosolic_calcium (millimolar)"
    legend_states[2] = "m_L in component L_type_calcium_current_m_gate (dimensionless)"
    legend_algebraic[1] = "m_L_infinity in component L_type_calcium_current_m_gate (dimensionless)"
    legend_algebraic[6] = "tau_m_L in component L_type_calcium_current_m_gate (millisecond)"
    legend_constants[11] = "tau_m_L_max in component L_type_calcium_current_m_gate (millisecond)"
    legend_constants[12] = "V_m_L in component L_type_calcium_current_m_gate (millivolt)"
    legend_constants[13] = "k_m_L in component L_type_calcium_current_m_gate (millivolt)"
    legend_constants[14] = "g_Ca_T in component T_type_calcium_current (nanoS_per_millimolar)"
    legend_states[3] = "m_T in component T_type_calcium_current_m_gate (dimensionless)"
    legend_states[4] = "h_T in component T_type_calcium_current_h_gate (dimensionless)"
    legend_algebraic[2] = "m_T_infinity in component T_type_calcium_current_m_gate (dimensionless)"
    legend_algebraic[7] = "tau_m_T in component T_type_calcium_current_m_gate (millisecond)"
    legend_constants[15] = "tau_m_T_max in component T_type_calcium_current_m_gate (millisecond)"
    legend_constants[16] = "V_m_T in component T_type_calcium_current_m_gate (millivolt)"
    legend_constants[17] = "k_m_T in component T_type_calcium_current_m_gate (millivolt)"
    legend_algebraic[3] = "h_T_infinity in component T_type_calcium_current_h_gate (dimensionless)"
    legend_constants[18] = "tau_h_T in component T_type_calcium_current_h_gate (millisecond)"
    legend_constants[19] = "V_h_T in component T_type_calcium_current_h_gate (millivolt)"
    legend_constants[20] = "k_h_T in component T_type_calcium_current_h_gate (millivolt)"
    legend_algebraic[9] = "phi_K in component voltage_sensitive_K_current (millivolt_millimolar)"
    legend_constants[21] = "g_K_DR in component voltage_sensitive_K_current (nanoS_per_millimolar)"
    legend_states[5] = "n in component voltage_sensitive_K_current_n_gate (dimensionless)"
    legend_algebraic[4] = "n_infinity in component voltage_sensitive_K_current_n_gate (dimensionless)"
    legend_constants[22] = "tau_n in component voltage_sensitive_K_current_n_gate (millisecond)"
    legend_constants[23] = "V_n in component voltage_sensitive_K_current_n_gate (millivolt)"
    legend_constants[24] = "k_n in component voltage_sensitive_K_current_n_gate (millivolt)"
    legend_constants[25] = "g_K_Ca in component Ca_activated_K_current (nanoS_per_millimolar)"
    legend_constants[26] = "Kc in component Ca_activated_K_current (millimolar)"
    legend_constants[27] = "g_L in component leak_current (nanoS)"
    legend_constants[28] = "V_L in component leak_current (millivolt)"
    legend_states[6] = "Ca_er in component ER_calcium (millimolar)"
    legend_algebraic[10] = "J_rel in component ER_calcium (millimolar_picoL_per_millisecond)"
    legend_algebraic[12] = "J_up in component ER_calcium (millimolar_picoL_per_millisecond)"
    legend_constants[38] = "V_er in component ER_calcium (picoL)"
    legend_constants[29] = "K_er in component ER_calcium (millimolar)"
    legend_constants[30] = "f_er in component ER_calcium (dimensionless)"
    legend_constants[31] = "P in component ER_calcium (picoL_per_millisecond)"
    legend_constants[32] = "v_er in component ER_calcium (millimolar_picoL_per_millisecond)"
    legend_constants[39] = "V_c in component cytosolic_calcium (picoL)"
    legend_constants[33] = "K_p in component cytosolic_calcium (millimolar)"
    legend_constants[34] = "f_cyt in component cytosolic_calcium (dimensionless)"
    legend_constants[35] = "v_p in component cytosolic_calcium (millimolar_micrometre_per_millisecond)"
    legend_algebraic[14] = "J_in in component cytosolic_calcium (millimolar_micrometre_per_millisecond)"
    legend_algebraic[16] = "J_eff in component cytosolic_calcium (millimolar_micrometre_per_millisecond)"
    legend_constants[36] = "alpha in component cytosolic_calcium (millimolar_micrometre_per_millisecond_per_picoA)"
    legend_constants[37] = "beta in component cytosolic_calcium (per_micrometre)"
    legend_rates[0] = "d/dt V in component membrane (millivolt)"
    legend_rates[2] = "d/dt m_L in component L_type_calcium_current_m_gate (dimensionless)"
    legend_rates[3] = "d/dt m_T in component T_type_calcium_current_m_gate (dimensionless)"
    legend_rates[4] = "d/dt h_T in component T_type_calcium_current_h_gate (dimensionless)"
    legend_rates[5] = "d/dt n in component voltage_sensitive_K_current_n_gate (dimensionless)"
    legend_rates[6] = "d/dt Ca_er in component ER_calcium (millimolar)"
    legend_rates[1] = "d/dt Ca_i in component cytosolic_calcium (millimolar)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    constants[0] = 1.77
    constants[1] = 20
    constants[2] = 5.6
    constants[3] = 140
    constants[4] = -60
    constants[5] = 22
    states[0] = -70
    constants[6] = 8314
    constants[7] = 310
    constants[8] = 96845
    constants[9] = 7
    constants[10] = 9
    states[1] = 0.00026
    states[2] = 0
    constants[11] = 27
    constants[12] = -18
    constants[13] = 12
    constants[14] = 10
    states[3] = 0
    states[4] = 0
    constants[15] = 10
    constants[16] = -30
    constants[17] = 10.5
    constants[18] = 15
    constants[19] = -57
    constants[20] = 5
    constants[21] = 0.1
    states[5] = 0
    constants[22] = 20
    constants[23] = -20
    constants[24] = 4.5
    constants[25] = 0.09
    constants[26] = 0.0004
    constants[27] = 0.3
    constants[28] = -67
    states[6] = 0.0172
    constants[29] = 0.0002
    constants[30] = 0.0025
    constants[31] = 0.0012
    constants[32] = 0.00005
    constants[33] = 0.00008
    constants[34] = 0.01
    constants[35] = 0.000045
    constants[36] = 0.0000074
    constants[37] = 0.47
    constants[38] = constants[0]*0.150000
    constants[39] = constants[0]*0.850000
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[3] = 1.00000/(1.00000+exp((states[0]-constants[19])/constants[20]))
    rates[4] = (algebraic[3]-states[4])/constants[18]
    algebraic[4] = 1.00000/(1.00000+exp((constants[23]-states[0])/constants[24]))
    rates[5] = (algebraic[4]-states[5])/constants[22]
    algebraic[1] = 1.00000/(1.00000+exp((constants[12]-states[0])/constants[13]))
    algebraic[6] = constants[11]/(exp((states[0]-constants[4])/constants[5])+2.00000*exp((2.00000*(constants[4]-states[0]))/constants[5]))
    rates[2] = (algebraic[1]-states[2])/algebraic[6]
    algebraic[2] = 1.00000/(1.00000+exp((constants[16]-states[0])/constants[17]))
    algebraic[7] = constants[15]/(exp((states[0]-constants[4])/constants[5])+2.00000*exp((2.00000*(constants[4]-states[0]))/constants[5]))
    rates[3] = (algebraic[2]-states[3])/algebraic[7]
    algebraic[10] = constants[31]*(states[6]-states[1])
    algebraic[12] = (constants[32]*(power(states[1], 2.00000)))/(power(states[1], 2.00000)+power(constants[29], 2.00000))
    rates[6] = (-constants[30]/constants[38])*(algebraic[10]-algebraic[12])
    algebraic[0] = (states[0]*(states[1]-constants[1])*exp((-2.00000*constants[8]*states[0])/(constants[6]*constants[7])))/(1.00000-exp((-2.00000*constants[8]*states[0])/(constants[6]*constants[7])))
    algebraic[5] = constants[10]*(power(states[2], 2.00000))*algebraic[0]
    algebraic[8] = constants[14]*(power(states[3], 2.00000))*states[4]*algebraic[0]
    algebraic[9] = (states[0]*(constants[3]-constants[2])*exp((-1.00000*constants[8]*states[0])/(constants[6]*constants[7])))/(1.00000-exp((-1.00000*constants[8]*states[0])/(constants[6]*constants[7])))
    algebraic[11] = constants[21]*states[5]*algebraic[9]
    algebraic[13] = ((constants[25]*(power(states[1], 4.00000)))/(power(states[1], 4.00000)+power(constants[26], 4.00000)))*algebraic[9]
    algebraic[15] = constants[27]*(states[0]-constants[28])
    rates[0] = -(algebraic[5]+algebraic[8]+algebraic[11]+algebraic[13]+algebraic[15])/constants[9]
    algebraic[14] = -constants[36]*(algebraic[5]+algebraic[8])
    algebraic[16] = (constants[35]*(power(states[1], 2.00000)))/(power(states[1], 2.00000)+power(constants[33], 2.00000))
    rates[1] = (constants[34]/constants[39])*(algebraic[10]-algebraic[12])+constants[34]*constants[37]*(algebraic[14]-algebraic[16])
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[3] = 1.00000/(1.00000+exp((states[0]-constants[19])/constants[20]))
    algebraic[4] = 1.00000/(1.00000+exp((constants[23]-states[0])/constants[24]))
    algebraic[1] = 1.00000/(1.00000+exp((constants[12]-states[0])/constants[13]))
    algebraic[6] = constants[11]/(exp((states[0]-constants[4])/constants[5])+2.00000*exp((2.00000*(constants[4]-states[0]))/constants[5]))
    algebraic[2] = 1.00000/(1.00000+exp((constants[16]-states[0])/constants[17]))
    algebraic[7] = constants[15]/(exp((states[0]-constants[4])/constants[5])+2.00000*exp((2.00000*(constants[4]-states[0]))/constants[5]))
    algebraic[10] = constants[31]*(states[6]-states[1])
    algebraic[12] = (constants[32]*(power(states[1], 2.00000)))/(power(states[1], 2.00000)+power(constants[29], 2.00000))
    algebraic[0] = (states[0]*(states[1]-constants[1])*exp((-2.00000*constants[8]*states[0])/(constants[6]*constants[7])))/(1.00000-exp((-2.00000*constants[8]*states[0])/(constants[6]*constants[7])))
    algebraic[5] = constants[10]*(power(states[2], 2.00000))*algebraic[0]
    algebraic[8] = constants[14]*(power(states[3], 2.00000))*states[4]*algebraic[0]
    algebraic[9] = (states[0]*(constants[3]-constants[2])*exp((-1.00000*constants[8]*states[0])/(constants[6]*constants[7])))/(1.00000-exp((-1.00000*constants[8]*states[0])/(constants[6]*constants[7])))
    algebraic[11] = constants[21]*states[5]*algebraic[9]
    algebraic[13] = ((constants[25]*(power(states[1], 4.00000)))/(power(states[1], 4.00000)+power(constants[26], 4.00000)))*algebraic[9]
    algebraic[15] = constants[27]*(states[0]-constants[28])
    algebraic[14] = -constants[36]*(algebraic[5]+algebraic[8])
    algebraic[16] = (constants[35]*(power(states[1], 2.00000)))/(power(states[1], 2.00000)+power(constants[33], 2.00000))
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
        self.V_cell = 1.77
        self.Ca_e = 20
        self.K_e = 5.6
        self.K_i = 140
        self.V_tau = -60
        self.k_tau = 22
        self.R = 8314
        self.T = 310
        self.F = 96845
        self.Cm = 7
        self.g_Ca_L = 9
        self.tau_m_L_max = 27
        self.V_m_L = -18
        self.k_m_L = 12
        self.g_Ca_T = 10
        self.tau_m_T_max = 10
        self.V_m_T = -30
        self.k_m_T = 10.5
        self.tau_h_T = 15
        self.V_h_T = -57
        self.k_h_T = 5
        self.g_K_DR = 0.1
        self.tau_n = 20
        self.V_n = -20
        self.k_n = 4.5
        self.g_K_Ca = 0.09
        self.Kc = 0.0004
        self.g_L = 0.3
        self.V_L = -67
        self.K_er = 0.0002
        self.f_er = 0.0025
        self.P = 0.0012
        self.v_er = 0.00005
        self.K_p = 0.00008
        self.f_cyt = 0.01
        self.v_p = 0.000045
        self.alpha = 0.0000074
        self.beta = 0.47

    def to_dict(self):
        return {
            "V_cell": self.V_cell,
            "Ca_e": self.Ca_e,
            "K_e": self.K_e,
            "K_i": self.K_i,
            "V_tau": self.V_tau,
            "k_tau": self.k_tau,
            "R": self.R,
            "T": self.T,
            "F": self.F,
            "Cm": self.Cm,
            "g_Ca_L": self.g_Ca_L,
            "tau_m_L_max": self.tau_m_L_max,
            "V_m_L": self.V_m_L,
            "k_m_L": self.k_m_L,
            "g_Ca_T": self.g_Ca_T,
            "tau_m_T_max": self.tau_m_T_max,
            "V_m_T": self.V_m_T,
            "k_m_T": self.k_m_T,
            "tau_h_T": self.tau_h_T,
            "V_h_T": self.V_h_T,
            "k_h_T": self.k_h_T,
            "g_K_DR": self.g_K_DR,
            "tau_n": self.tau_n,
            "V_n": self.V_n,
            "k_n": self.k_n,
            "g_K_Ca": self.g_K_Ca,
            "Kc": self.Kc,
            "g_L": self.g_L,
            "V_L": self.V_L,
            "K_er": self.K_er,
            "f_er": self.f_er,
            "P": self.P,
            "v_er": self.v_er,
            "K_p": self.K_p,
            "f_cyt": self.f_cyt,
            "v_p": self.v_p,
            "alpha": self.alpha,
            "beta": self.beta,
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
        y0=[-70, 0.00026, 0, 0, 0, 0, 0.0172],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "shorten_wall_2000"
        self.curve_names = [
            "V",
            "Ca_i",
            "m_L",
            "m_T",
            "h_T",
            "n",
            "Ca_er",
        ]
        self.state_names = ['V', 'Ca_i', 'm_L', 'm_T', 'h_T', 'n', 'Ca_er']
        self.algebraic_names = ['phi_Ca', 'm_L_infinity', 'm_T_infinity', 'h_T_infinity', 'n_infinity', 'i_Ca_L', 'tau_m_L', 'tau_m_T', 'i_Ca_T', 'phi_K', 'J_rel', 'i_K_DR', 'J_up', 'i_K_Ca', 'J_in', 'i_leak', 'J_eff']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 40
        p = self.params

        # direct mapping
        c[0] = p.V_cell
        c[1] = p.Ca_e
        c[2] = p.K_e
        c[3] = p.K_i
        c[4] = p.V_tau
        c[5] = p.k_tau
        c[6] = p.R
        c[7] = p.T
        c[8] = p.F
        c[9] = p.Cm
        c[10] = p.g_Ca_L
        c[11] = p.tau_m_L_max
        c[12] = p.V_m_L
        c[13] = p.k_m_L
        c[14] = p.g_Ca_T
        c[15] = p.tau_m_T_max
        c[16] = p.V_m_T
        c[17] = p.k_m_T
        c[18] = p.tau_h_T
        c[19] = p.V_h_T
        c[20] = p.k_h_T
        c[21] = p.g_K_DR
        c[22] = p.tau_n
        c[23] = p.V_n
        c[24] = p.k_n
        c[25] = p.g_K_Ca
        c[26] = p.Kc
        c[27] = p.g_L
        c[28] = p.V_L
        c[29] = p.K_er
        c[30] = p.f_er
        c[31] = p.P
        c[32] = p.v_er
        c[33] = p.K_p
        c[34] = p.f_cyt
        c[35] = p.v_p
        c[36] = p.alpha
        c[37] = p.beta

        # derived constants
        c[38] = c[0]*0.150000
        c[39] = c[0]*0.850000

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
