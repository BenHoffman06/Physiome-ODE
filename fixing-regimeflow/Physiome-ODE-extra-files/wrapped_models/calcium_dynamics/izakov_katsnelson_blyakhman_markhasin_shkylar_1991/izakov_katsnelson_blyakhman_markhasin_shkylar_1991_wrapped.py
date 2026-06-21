# Size of variable arrays:
sizeAlgebraic = 13
sizeStates = 2
sizeConstants = 30
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (millisecond)"
    legend_algebraic[10] = "P_CE in component equations (dimensionless)"
    legend_algebraic[5] = "P_PE in component equations (dimensionless)"
    legend_algebraic[6] = "P_SE in component equations (dimensionless)"
    legend_algebraic[0] = "Ca in component equations (dimensionless)"
    legend_algebraic[12] = "C_2 in component equations (per_millisec)"
    legend_algebraic[1] = "phi_A_1 in component equations (dimensionless)"
    legend_algebraic[11] = "pi_n in component equations (dimensionless)"
    legend_algebraic[8] = "A in component equations (dimensionless)"
    legend_states[0] = "A_1 in component equations (dimensionless)"
    legend_algebraic[3] = "S in component equations (um)"
    legend_algebraic[9] = "n in component equations (dimensionless)"
    legend_algebraic[7] = "n_1 in component equations (dimensionless)"
    legend_states[1] = "n_2 in component equations (dimensionless)"
    legend_constants[27] = "G_V in component equations (dimensionless)"
    legend_constants[26] = "q_V in component equations (per_millisec)"
    legend_constants[25] = "V in component equations (um_per_millisec)"
    legend_constants[28] = "F_V in component equations (dimensionless)"
    legend_constants[29] = "p_V in component equations (dimensionless)"
    legend_constants[0] = "alpha_1 in component equations (per_um)"
    legend_constants[1] = "alpha_2 in component equations (per_um)"
    legend_constants[2] = "beta_1 in component equations (dimensionless)"
    legend_constants[3] = "beta_2 in component equations (dimensionless)"
    legend_constants[4] = "lambda in component equations (per_um)"
    legend_constants[5] = "V_max in component equations (um_per_millisec)"
    legend_constants[6] = "Ca_m in component equations (dimensionless)"
    legend_constants[7] = "t_d in component equations (millisecond)"
    legend_constants[8] = "a_c in component equations (per_millisec2)"
    legend_constants[9] = "b_c in component equations (per_millisec2)"
    legend_constants[10] = "C_1 in component equations (per_millisec)"
    legend_constants[11] = "C_20 in component equations (per_millisec)"
    legend_constants[12] = "q_k in component equations (dimensionless)"
    legend_constants[24] = "V_1 in component equations (um_per_millisec)"
    legend_constants[13] = "a in component equations (dimensionless)"
    legend_constants[14] = "m_0 in component equations (dimensionless)"
    legend_constants[15] = "g_1 in component equations (per_um)"
    legend_constants[16] = "g_2 in component equations (dimensionless)"
    legend_constants[17] = "pi_min in component equations (dimensionless)"
    legend_constants[18] = "S_0 in component equations (um)"
    legend_constants[19] = "q_1 in component equations (per_millisec)"
    legend_constants[20] = "q_2 in component equations (per_millisec)"
    legend_constants[21] = "q_3 in component equations (per_millisec)"
    legend_constants[22] = "TnC in component equations (dimensionless)"
    legend_algebraic[2] = "l_1 in component user_defined (um)"
    legend_algebraic[4] = "l_2 in component user_defined (um)"
    legend_constants[23] = "dl_1_dt in component user_defined (um_per_millisec)"
    legend_rates[0] = "d/dt A_1 in component equations (dimensionless)"
    legend_rates[1] = "d/dt n_2 in component equations (dimensionless)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 0
    states[1] = 0
    constants[0] = 14.6
    constants[1] = 14.6
    constants[2] = 1
    constants[3] = 0.0012
    constants[4] = 30
    constants[5] = 0.0043
    constants[6] = 45e-3
    constants[7] = 170
    constants[8] = 2.4e-4
    constants[9] = 5e-4
    constants[10] = 2.9e-2
    constants[11] = 0.2
    constants[12] = 4
    constants[13] = 0.25
    constants[14] = 0.87
    constants[15] = 0.4
    constants[16] = 0.6
    constants[17] = 5e-2
    constants[18] = 0.77
    constants[19] = 0.017
    constants[20] = 0.26
    constants[21] = 0.03
    constants[22] = 1
    constants[23] = 0.00000
    constants[24] = 0.100000*constants[5]
    constants[25] = -constants[23]
    constants[26] = custom_piecewise([less_equal(constants[25] , 0.00000), constants[19]-(constants[20]*constants[25])/constants[5] , True, constants[21]])
    constants[27] = 1.00000+(0.600000*constants[25])/constants[5]
    constants[28] = (constants[13]*(1.00000+constants[25]/constants[5]))/(constants[13]-constants[25]/constants[5])
    constants[29] = constants[28]/constants[27]
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[1] = constants[26]*(constants[14]*constants[27]-states[1])
    algebraic[0] = custom_piecewise([less_equal(voi , constants[7]), constants[6]*(power(1.00000-exp(-constants[8]*(power(voi, 2.00000))), 2.00000)) , True, constants[6]*(power((1.00000-exp(-constants[8]*(power(voi, 2.00000))))*exp(-constants[9]*(power(voi-constants[7], 2.00000))), 2.00000))])
    algebraic[1] = exp(-constants[12]*states[0])
    algebraic[2] = custom_piecewise([less_equal(200.000 , voi) & less_equal(voi , 201.000), 0.00000 , True, 0.00000])
    algebraic[7] = custom_piecewise([less(constants[15]*algebraic[2]+constants[16] , 0.00000), 0.00000 , less_equal(0.00000 , constants[15]*algebraic[2]+constants[16]) & less_equal(constants[15]*algebraic[2]+constants[16] , 1.00000), constants[15]*algebraic[2]+constants[16] , True, 1.00000])
    algebraic[9] = algebraic[7]*states[1]
    algebraic[11] = custom_piecewise([less_equal(0.750000 , algebraic[9]) & less_equal(algebraic[9] , 1.00000), constants[17] , less_equal(0.250000 , algebraic[9]) & less(algebraic[9] , 0.750000), power(constants[17], 2.00000*algebraic[9]-0.500000) , True, 1.00000])
    rates[0] = constants[10]*algebraic[0]*(constants[22]-states[0])-constants[11]*algebraic[11]*algebraic[1]*states[0]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = custom_piecewise([less_equal(voi , constants[7]), constants[6]*(power(1.00000-exp(-constants[8]*(power(voi, 2.00000))), 2.00000)) , True, constants[6]*(power((1.00000-exp(-constants[8]*(power(voi, 2.00000))))*exp(-constants[9]*(power(voi-constants[7], 2.00000))), 2.00000))])
    algebraic[1] = exp(-constants[12]*states[0])
    algebraic[2] = custom_piecewise([less_equal(200.000 , voi) & less_equal(voi , 201.000), 0.00000 , True, 0.00000])
    algebraic[7] = custom_piecewise([less(constants[15]*algebraic[2]+constants[16] , 0.00000), 0.00000 , less_equal(0.00000 , constants[15]*algebraic[2]+constants[16]) & less_equal(constants[15]*algebraic[2]+constants[16] , 1.00000), constants[15]*algebraic[2]+constants[16] , True, 1.00000])
    algebraic[9] = algebraic[7]*states[1]
    algebraic[11] = custom_piecewise([less_equal(0.750000 , algebraic[9]) & less_equal(algebraic[9] , 1.00000), constants[17] , less_equal(0.250000 , algebraic[9]) & less(algebraic[9] , 0.750000), power(constants[17], 2.00000*algebraic[9]-0.500000) , True, 1.00000])
    algebraic[3] = 0.500000*algebraic[2]+constants[18]
    algebraic[4] = algebraic[2]+1.87000
    algebraic[5] = constants[3]*(exp(constants[1]*algebraic[4])-1.00000)
    algebraic[6] = constants[2]*(exp(constants[0]*(algebraic[4]-algebraic[2]))-1.00000)
    algebraic[8] = (states[0]*algebraic[3])/1.00000
    algebraic[10] = constants[4]*algebraic[3]*states[0]*algebraic[9]*constants[29]
    algebraic[12] = constants[11]*algebraic[11]*algebraic[1]
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
        self.alpha_1 = 14.6
        self.alpha_2 = 14.6
        self.beta_1 = 1
        self.beta_2 = 0.0012
        self.lambda = 30
        self.V_max = 0.0043
        self.Ca_m = 45e-3
        self.t_d = 170
        self.a_c = 2.4e-4
        self.b_c = 5e-4
        self.C_1 = 2.9e-2
        self.C_20 = 0.2
        self.q_k = 4
        self.a = 0.25
        self.m_0 = 0.87
        self.g_1 = 0.4
        self.g_2 = 0.6
        self.pi_min = 5e-2
        self.S_0 = 0.77
        self.q_1 = 0.017
        self.q_2 = 0.26
        self.q_3 = 0.03
        self.TnC = 1
        self.dl_1_dt = 0.00000

    def to_dict(self):
        return {
            "alpha_1": self.alpha_1,
            "alpha_2": self.alpha_2,
            "beta_1": self.beta_1,
            "beta_2": self.beta_2,
            "lambda": self.lambda,
            "V_max": self.V_max,
            "Ca_m": self.Ca_m,
            "t_d": self.t_d,
            "a_c": self.a_c,
            "b_c": self.b_c,
            "C_1": self.C_1,
            "C_20": self.C_20,
            "q_k": self.q_k,
            "a": self.a,
            "m_0": self.m_0,
            "g_1": self.g_1,
            "g_2": self.g_2,
            "pi_min": self.pi_min,
            "S_0": self.S_0,
            "q_1": self.q_1,
            "q_2": self.q_2,
            "q_3": self.q_3,
            "TnC": self.TnC,
            "dl_1_dt": self.dl_1_dt,
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
        y0=[0, 0],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "izakov_katsnelson_blyakhman_markhasin_shkylar_1991"
        self.curve_names = [
            "A_1",
            "n_2",
        ]
        self.state_names = ['A_1', 'n_2']
        self.algebraic_names = ['Ca', 'phi_A_1', 'l_1', 'S', 'l_2', 'P_PE', 'P_SE', 'n_1', 'A', 'n', 'P_CE', 'pi_n', 'C_2']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 30
        p = self.params

        # direct mapping
        c[0] = p.alpha_1
        c[1] = p.alpha_2
        c[2] = p.beta_1
        c[3] = p.beta_2
        c[4] = p.lambda
        c[5] = p.V_max
        c[6] = p.Ca_m
        c[7] = p.t_d
        c[8] = p.a_c
        c[9] = p.b_c
        c[10] = p.C_1
        c[11] = p.C_20
        c[12] = p.q_k
        c[13] = p.a
        c[14] = p.m_0
        c[15] = p.g_1
        c[16] = p.g_2
        c[17] = p.pi_min
        c[18] = p.S_0
        c[19] = p.q_1
        c[20] = p.q_2
        c[21] = p.q_3
        c[22] = p.TnC
        c[23] = p.dl_1_dt

        # derived constants
        c[24] = 0.100000*c[5]
        c[25] = -c[23]
        c[26] = (c[19]-(c[20]*c[25])/c[5] if less_equal(c[25] , 0.00000) else c[21])
        c[27] = 1.00000+(0.600000*c[25])/c[5]
        c[28] = (c[13]*(1.00000+c[25]/c[5]))/(c[13]-c[25]/c[5])
        c[29] = c[28]/c[27]

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
