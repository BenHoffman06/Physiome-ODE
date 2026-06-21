# Size of variable arrays:
sizeAlgebraic = 7
sizeStates = 11
sizeConstants = 57
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (hour)"
    legend_states[0] = "Q_Ca_p in component Q_Ca_p (millimole)"
    legend_constants[0] = "J_bp_Ca in component model_fluxes (millimole_per_hour)"
    legend_algebraic[0] = "J_pb_Ca in component model_fluxes (millimole_per_hour)"
    legend_constants[1] = "J_pu_Ca in component model_fluxes (millimole_per_hour)"
    legend_algebraic[3] = "J_ip_Ca in component model_fluxes (millimole_per_hour)"
    legend_states[1] = "Q_P_p in component Q_P_p (millimole)"
    legend_constants[38] = "J_bp_P in component model_fluxes (millimole_per_hour)"
    legend_algebraic[4] = "J_pb_P in component model_fluxes (millimole_per_hour)"
    legend_constants[2] = "J_pu_P in component model_fluxes (millimole_per_hour)"
    legend_constants[48] = "J_ip_P in component model_fluxes (millimole_per_hour)"
    legend_constants[55] = "J_pc_P in component model_fluxes (millimole_per_hour)"
    legend_algebraic[6] = "J_cp_P in component model_fluxes (millimole_per_hour)"
    legend_states[2] = "Q_P_c in component Q_P_c (millimole)"
    legend_states[3] = "Q_PTH_p in component Q_PTH_p (millimole)"
    legend_algebraic[1] = "S_PTH in component model_fluxes (millimole_per_hour)"
    legend_constants[3] = "C_PTH_p in component model_parameters (millimolar)"
    legend_constants[4] = "k_PTH in component model_parameters (first_order_rate_constant)"
    legend_states[4] = "Q_Ca_b in component Q_Ca_b (millimole)"
    legend_states[5] = "Q_P_b in component Q_P_b (millimole)"
    legend_states[6] = "Q_E_k in component Q_E_k (millimole)"
    legend_constants[5] = "S_E in component model_parameters (millimole_per_hour)"
    legend_constants[6] = "k_E in component model_parameters (first_order_rate_constant)"
    legend_states[7] = "Q_D_p in component Q_D_p (millimole)"
    legend_constants[7] = "k_D in component model_parameters (first_order_rate_constant)"
    legend_states[8] = "Q_TCa_i in component Q_TCa_i (millimole)"
    legend_constants[49] = "k1_D in component model_parameters (first_order_rate_constant)"
    legend_constants[50] = "k2_D in component model_parameters (first_order_rate_constant)"
    legend_states[9] = "Q_C_PT in component Q_C_PT (millimole)"
    legend_constants[51] = "k3_D in component model_parameters (first_order_rate_constant)"
    legend_constants[52] = "k4_D in component model_parameters (first_order_rate_constant)"
    legend_states[10] = "Q_TP_k in component Q_TP_k (millimole)"
    legend_constants[53] = "k1_P in component model_parameters (first_order_rate_constant)"
    legend_constants[8] = "k2_P in component model_parameters (first_order_rate_constant)"
    legend_constants[9] = "J_P_ing in component model_fluxes (millimole_per_hour)"
    legend_constants[10] = "Stoic_Ca_P in component model_fluxes (dimensionless)"
    legend_constants[11] = "k_Ca_i in component model_fluxes (first_order_rate_constant)"
    legend_constants[12] = "C_Ca_i in component model_parameters (millimolar)"
    legend_constants[13] = "C_Ca_p in component model_parameters (millimolar)"
    legend_constants[14] = "C_P_p in component model_parameters (millimolar)"
    legend_constants[15] = "k_Ca_b in component model_parameters (first_order_rate_constant)"
    legend_constants[16] = "k3_P in component model_parameters (first_order_rate_constant)"
    legend_constants[17] = "k4_P in component model_parameters (first_order_rate_constant)"
    legend_constants[39] = "Y_Ca_i_2plus in component model_parameters (first_order_rate_constant)"
    legend_constants[40] = "Y_Ca_p_1minus in component model_parameters (first_order_rate_constant)"
    legend_constants[18] = "C_D_p in component model_parameters (picomolar)"
    legend_constants[54] = "Ca_thr in component model_parameters (first_order_rate_constant)"
    legend_constants[56] = "Ca_T in component model_parameters (second_order_rate_constant)"
    legend_algebraic[2] = "P_thr in component model_parameters (millimole_per_hour)"
    legend_algebraic[5] = "P_T in component model_parameters (litre_per_hour)"
    legend_constants[41] = "Y_i_D_p_1plus in component model_parameters (first_order_rate_constant)"
    legend_constants[42] = "Y_PT_D_p_1plus in component model_parameters (first_order_rate_constant)"
    legend_constants[43] = "Y_k_Jext_1plus in component model_parameters (first_order_rate_constant)"
    legend_constants[44] = "Y_PTH_p_2plus in component model_parameters (first_order_rate_constant)"
    legend_constants[45] = "Y_PTH_p_2minus in component model_parameters (first_order_rate_constant)"
    legend_constants[46] = "Y_i_D_p_1minus in component model_parameters (first_order_rate_constant)"
    legend_constants[47] = "Y_PT_D_p_1minus in component model_parameters (first_order_rate_constant)"
    legend_constants[19] = "Y_Ca_i_2plus_Max in component model_parameters (first_order_rate_constant)"
    legend_constants[20] = "Y_PTH_p_2plus_Max in component model_parameters (first_order_rate_constant)"
    legend_constants[21] = "Y_PTH_p_2minus_Max in component model_parameters (first_order_rate_constant)"
    legend_constants[22] = "Y_Ca_p_1plus_minus_Max in component model_parameters (first_order_rate_constant)"
    legend_constants[23] = "Y_i_D_p_1plus_minus_Max in component model_parameters (first_order_rate_constant)"
    legend_constants[24] = "Y_PT_D_p_1plus_minus_Max in component model_parameters (first_order_rate_constant)"
    legend_constants[25] = "Y_k_Jext_1plus_minus_Max in component model_parameters (first_order_rate_constant)"
    legend_constants[26] = "X_R_PTH_Ca in component model_parameters (millimolar)"
    legend_constants[27] = "X_R_i_Ca in component model_parameters (millimolar)"
    legend_constants[28] = "X_R_PTH_D in component model_parameters (picomolar)"
    legend_constants[29] = "X_R_E_PTH in component model_parameters (picomolar)"
    legend_constants[30] = "X_R_i_D in component model_parameters (picomolar)"
    legend_constants[31] = "X_R_P_k_PTH in component model_parameters (picomolar)"
    legend_constants[32] = "b_PTH_Ca in component model_parameters (litre_per_millimole)"
    legend_constants[33] = "b_PTH_D in component model_parameters (litre_per_picomole)"
    legend_constants[34] = "b_E_PTH in component model_parameters (litre_per_picomole)"
    legend_constants[35] = "b_i_D in component model_parameters (litre_per_picomole)"
    legend_constants[36] = "a in component model_parameters (dimensionless)"
    legend_constants[37] = "d in component model_parameters (dimensionless)"
    legend_rates[0] = "d/dt Q_Ca_p in component Q_Ca_p (millimole)"
    legend_rates[1] = "d/dt Q_P_p in component Q_P_p (millimole)"
    legend_rates[2] = "d/dt Q_P_c in component Q_P_c (millimole)"
    legend_rates[3] = "d/dt Q_PTH_p in component Q_PTH_p (millimole)"
    legend_rates[4] = "d/dt Q_Ca_b in component Q_Ca_b (millimole)"
    legend_rates[5] = "d/dt Q_P_b in component Q_P_b (millimole)"
    legend_rates[6] = "d/dt Q_E_k in component Q_E_k (millimole)"
    legend_rates[7] = "d/dt Q_D_p in component Q_D_p (millimole)"
    legend_rates[8] = "d/dt Q_TCa_i in component Q_TCa_i (millimole)"
    legend_rates[9] = "d/dt Q_C_PT in component Q_C_PT (millimole)"
    legend_rates[10] = "d/dt Q_TP_k in component Q_TP_k (millimole)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 1.000
    constants[0] = 3.3
    constants[1] = 0.21
    states[1] = 1.000
    constants[2] = 1.27
    states[2] = 3226.0
    states[3] = 1.000
    constants[3] = 3.85
    constants[4] = 100.0
    states[4] = 100.0
    states[5] = 1.000
    states[6] = 1.000
    constants[5] = 1.000
    constants[6] = 0.05
    states[7] = 1.000
    constants[7] = 0.1
    states[8] = 1.000
    states[9] = 1.000
    states[10] = 1.000
    constants[8] = 1.000
    constants[9] = 1.000
    constants[10] = 0.464
    constants[11] = 1.000
    constants[12] = 1.000
    constants[13] = 2.4
    constants[14] = 1.2
    constants[15] = 1.000
    constants[16] = 1.000
    constants[17] = 51.8
    constants[18] = 90.0
    constants[19] = 1.000
    constants[20] = 1.000
    constants[21] = 1.000
    constants[22] = 0.02
    constants[23] = 0.02
    constants[24] = 0.01
    constants[25] = 0.01
    constants[26] = 1.0
    constants[27] = 1.0
    constants[28] = 90.0
    constants[29] = 3.85
    constants[30] = 90.0
    constants[31] = 90.0
    constants[32] = 0.05
    constants[33] = 0.03
    constants[34] = 0.55
    constants[35] = 0.03
    constants[36] = 0.85
    constants[37] = 0.15
    constants[38] = constants[10]*constants[0]
    constants[39] = constants[19]*(constants[12]/(constants[12]+constants[27]))
    constants[40] = constants[22]*(constants[36]*(1.00000-tanh(constants[32]*(constants[13]-constants[26])))+constants[37])
    constants[41] = constants[23]*(constants[36]*(1.00000+tanh(constants[35]*(constants[18]-constants[30])))+constants[37])
    constants[42] = constants[24]*(constants[36]*(1.00000+tanh(constants[33]*(constants[18]-constants[28])))+constants[37])
    constants[43] = constants[25]*(constants[36]*(1.00000+tanh(constants[34]*(1.00000*constants[14]-constants[29])))+constants[37])
    constants[44] = constants[20]*(constants[3]/(constants[3]+1.00000*constants[31]))
    constants[45] = constants[21]*(constants[31]/(1.00000*constants[3]+constants[31]))
    constants[46] = constants[23]*(constants[36]*(1.00000-tanh(constants[35]*(constants[18]-constants[30])))+constants[37])
    constants[47] = constants[24]*(constants[36]*(1.00000-tanh(constants[33]*(constants[18]-constants[28])))+constants[37])
    constants[48] = constants[9]
    constants[49] = constants[41]
    constants[50] = constants[46]
    constants[51] = constants[42]
    constants[52] = constants[47]
    constants[53] = constants[43]
    constants[54] = 1.95000+constants[44]
    constants[55] = constants[17]*1.00000*constants[14]
    constants[56] = constants[54]/constants[13]
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[6] = constants[5]-constants[6]*states[6]
    rates[7] = 1.00000*states[6]-constants[7]*states[7]
    rates[8] = (1.00000-states[8])*constants[49]-states[8]*constants[50]
    rates[9] = (1.00000-states[9])*constants[51]-states[9]*constants[52]
    rates[10] = (1.00000-states[10])*constants[53]-states[10]*constants[8]
    algebraic[1] = 1.00000*constants[40]*(constants[51]*(1.00000-states[9])-constants[52]*states[9])
    rates[3] = algebraic[1]-constants[4]*1.00000*constants[3]
    algebraic[0] = constants[15]*states[4]
    rates[4] = algebraic[0]-constants[0]
    algebraic[3] = (constants[39]*(1.00000-states[8])*1.00000*constants[49]+constants[11]*1.00000*(constants[12]-constants[13]))-states[8]*constants[50]
    rates[0] = (constants[0]+algebraic[3])-(algebraic[0]+constants[1])
    algebraic[4] = constants[10]*algebraic[0]
    rates[5] = algebraic[4]-constants[38]
    algebraic[6] = constants[16]*states[2]
    rates[1] = (constants[38]+constants[48]+algebraic[6])-(algebraic[4]+constants[2]+constants[55])
    rates[2] = constants[55]-algebraic[6]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[1] = 1.00000*constants[40]*(constants[51]*(1.00000-states[9])-constants[52]*states[9])
    algebraic[0] = constants[15]*states[4]
    algebraic[3] = (constants[39]*(1.00000-states[8])*1.00000*constants[49]+constants[11]*1.00000*(constants[12]-constants[13]))-states[8]*constants[50]
    algebraic[4] = constants[10]*algebraic[0]
    algebraic[6] = constants[16]*states[2]
    algebraic[2] = constants[45]*states[10]
    algebraic[5] = algebraic[2]/constants[14]
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
        self.J_bp_Ca = 3.3
        self.J_pu_Ca = 0.21
        self.J_pu_P = 1.27
        self.C_PTH_p = 3.85
        self.k_PTH = 100.0
        self.S_E = 1.000
        self.k_E = 0.05
        self.k_D = 0.1
        self.k2_P = 1.000
        self.J_P_ing = 1.000
        self.Stoic_Ca_P = 0.464
        self.k_Ca_i = 1.000
        self.C_Ca_i = 1.000
        self.C_Ca_p = 2.4
        self.C_P_p = 1.2
        self.k_Ca_b = 1.000
        self.k3_P = 1.000
        self.k4_P = 51.8
        self.C_D_p = 90.0
        self.Y_Ca_i_2plus_Max = 1.000
        self.Y_PTH_p_2plus_Max = 1.000
        self.Y_PTH_p_2minus_Max = 1.000
        self.Y_Ca_p_1plus_minus_Max = 0.02
        self.Y_i_D_p_1plus_minus_Max = 0.02
        self.Y_PT_D_p_1plus_minus_Max = 0.01
        self.Y_k_Jext_1plus_minus_Max = 0.01
        self.X_R_PTH_Ca = 1.0
        self.X_R_i_Ca = 1.0
        self.X_R_PTH_D = 90.0
        self.X_R_E_PTH = 3.85
        self.X_R_i_D = 90.0
        self.X_R_P_k_PTH = 90.0
        self.b_PTH_Ca = 0.05
        self.b_PTH_D = 0.03
        self.b_E_PTH = 0.55
        self.b_i_D = 0.03
        self.a = 0.85
        self.d = 0.15

    def to_dict(self):
        return {
            "J_bp_Ca": self.J_bp_Ca,
            "J_pu_Ca": self.J_pu_Ca,
            "J_pu_P": self.J_pu_P,
            "C_PTH_p": self.C_PTH_p,
            "k_PTH": self.k_PTH,
            "S_E": self.S_E,
            "k_E": self.k_E,
            "k_D": self.k_D,
            "k2_P": self.k2_P,
            "J_P_ing": self.J_P_ing,
            "Stoic_Ca_P": self.Stoic_Ca_P,
            "k_Ca_i": self.k_Ca_i,
            "C_Ca_i": self.C_Ca_i,
            "C_Ca_p": self.C_Ca_p,
            "C_P_p": self.C_P_p,
            "k_Ca_b": self.k_Ca_b,
            "k3_P": self.k3_P,
            "k4_P": self.k4_P,
            "C_D_p": self.C_D_p,
            "Y_Ca_i_2plus_Max": self.Y_Ca_i_2plus_Max,
            "Y_PTH_p_2plus_Max": self.Y_PTH_p_2plus_Max,
            "Y_PTH_p_2minus_Max": self.Y_PTH_p_2minus_Max,
            "Y_Ca_p_1plus_minus_Max": self.Y_Ca_p_1plus_minus_Max,
            "Y_i_D_p_1plus_minus_Max": self.Y_i_D_p_1plus_minus_Max,
            "Y_PT_D_p_1plus_minus_Max": self.Y_PT_D_p_1plus_minus_Max,
            "Y_k_Jext_1plus_minus_Max": self.Y_k_Jext_1plus_minus_Max,
            "X_R_PTH_Ca": self.X_R_PTH_Ca,
            "X_R_i_Ca": self.X_R_i_Ca,
            "X_R_PTH_D": self.X_R_PTH_D,
            "X_R_E_PTH": self.X_R_E_PTH,
            "X_R_i_D": self.X_R_i_D,
            "X_R_P_k_PTH": self.X_R_P_k_PTH,
            "b_PTH_Ca": self.b_PTH_Ca,
            "b_PTH_D": self.b_PTH_D,
            "b_E_PTH": self.b_E_PTH,
            "b_i_D": self.b_i_D,
            "a": self.a,
            "d": self.d,
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
        y0=[1.000, 1.000, 3226.0, 1.000, 100.0, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "raposo_2002"
        self.curve_names = [
            "Q_Ca_p",
            "Q_P_p",
            "Q_P_c",
            "Q_PTH_p",
            "Q_Ca_b",
            "Q_P_b",
            "Q_E_k",
            "Q_D_p",
            "Q_TCa_i",
            "Q_C_PT",
            "Q_TP_k",
        ]
        self.state_names = ['Q_Ca_p', 'Q_P_p', 'Q_P_c', 'Q_PTH_p', 'Q_Ca_b', 'Q_P_b', 'Q_E_k', 'Q_D_p', 'Q_TCa_i', 'Q_C_PT', 'Q_TP_k']
        self.algebraic_names = ['J_pb_Ca', 'S_PTH', 'P_thr', 'J_ip_Ca', 'J_pb_P', 'P_T', 'J_cp_P']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 57
        p = self.params

        # direct mapping
        c[0] = p.J_bp_Ca
        c[1] = p.J_pu_Ca
        c[2] = p.J_pu_P
        c[3] = p.C_PTH_p
        c[4] = p.k_PTH
        c[5] = p.S_E
        c[6] = p.k_E
        c[7] = p.k_D
        c[8] = p.k2_P
        c[9] = p.J_P_ing
        c[10] = p.Stoic_Ca_P
        c[11] = p.k_Ca_i
        c[12] = p.C_Ca_i
        c[13] = p.C_Ca_p
        c[14] = p.C_P_p
        c[15] = p.k_Ca_b
        c[16] = p.k3_P
        c[17] = p.k4_P
        c[18] = p.C_D_p
        c[19] = p.Y_Ca_i_2plus_Max
        c[20] = p.Y_PTH_p_2plus_Max
        c[21] = p.Y_PTH_p_2minus_Max
        c[22] = p.Y_Ca_p_1plus_minus_Max
        c[23] = p.Y_i_D_p_1plus_minus_Max
        c[24] = p.Y_PT_D_p_1plus_minus_Max
        c[25] = p.Y_k_Jext_1plus_minus_Max
        c[26] = p.X_R_PTH_Ca
        c[27] = p.X_R_i_Ca
        c[28] = p.X_R_PTH_D
        c[29] = p.X_R_E_PTH
        c[30] = p.X_R_i_D
        c[31] = p.X_R_P_k_PTH
        c[32] = p.b_PTH_Ca
        c[33] = p.b_PTH_D
        c[34] = p.b_E_PTH
        c[35] = p.b_i_D
        c[36] = p.a
        c[37] = p.d

        # derived constants
        c[38] = c[10]*c[0]
        c[39] = c[19]*(c[12]/(c[12]+c[27]))
        c[40] = c[22]*(c[36]*(1.00000-tanh(c[32]*(c[13]-c[26])))+c[37])
        c[41] = c[23]*(c[36]*(1.00000+tanh(c[35]*(c[18]-c[30])))+c[37])
        c[42] = c[24]*(c[36]*(1.00000+tanh(c[33]*(c[18]-c[28])))+c[37])
        c[43] = c[25]*(c[36]*(1.00000+tanh(c[34]*(1.00000*c[14]-c[29])))+c[37])
        c[44] = c[20]*(c[3]/(c[3]+1.00000*c[31]))
        c[45] = c[21]*(c[31]/(1.00000*c[3]+c[31]))
        c[46] = c[23]*(c[36]*(1.00000-tanh(c[35]*(c[18]-c[30])))+c[37])
        c[47] = c[24]*(c[36]*(1.00000-tanh(c[33]*(c[18]-c[28])))+c[37])
        c[48] = c[9]
        c[49] = c[41]
        c[50] = c[46]
        c[51] = c[42]
        c[52] = c[47]
        c[53] = c[43]
        c[54] = 1.95000+c[44]
        c[55] = c[17]*1.00000*c[14]
        c[56] = c[54]/c[13]

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
