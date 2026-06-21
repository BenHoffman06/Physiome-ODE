# Size of variable arrays:
sizeAlgebraic = 1
sizeStates = 2
sizeConstants = 34
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "t in component environment (second)"
    legend_constants[0] = "x in component environment (nanometer)"
    legend_states[0] = "n in component Crossbridges_attached (dimensionless)"
    legend_states[1] = "A_c in component Actin_free (dimensionless)"
    legend_constants[23] = "f in component f (per_second)"
    legend_constants[24] = "g in component g (per_second)"
    legend_constants[1] = "h in component Crossbridges_attached (nanometer)"
    legend_constants[2] = "f_1 in component f (per_second)"
    legend_constants[3] = "g_1 in component g (per_second)"
    legend_constants[4] = "g_2 in component g (per_second)"
    legend_algebraic[0] = "Ca_f in component Ca_sarcoplasm (molar)"
    legend_constants[5] = "t_d in component Ca_sarcoplasm (second)"
    legend_constants[6] = "a_1 in component Ca_sarcoplasm (per_second_squared)"
    legend_constants[7] = "b_1 in component Ca_sarcoplasm (per_second_squared)"
    legend_constants[8] = "Ca_0 in component Ca_sarcoplasm (molar)"
    legend_constants[9] = "c_1 in component Actin_free (per_second)"
    legend_constants[26] = "c_2 in component Actin_free (per_second)"
    legend_constants[10] = "c_2_0 in component Actin_free (per_second)"
    legend_constants[11] = "k_i in component Actin_free (dimensionless)"
    legend_constants[25] = "s_h in component s_h (muscle_length)"
    legend_constants[12] = "q in component Actin_free (dimensionless)"
    legend_constants[13] = "AT_0 in component Actin_free (dimensionless)"
    legend_constants[32] = "F_SE in component Series_Elastic_Element (force)"
    legend_constants[14] = "alpha_s in component Series_Elastic_Element (force)"
    legend_constants[15] = "beta_s in component Series_Elastic_Element (muscle_length)"
    legend_constants[31] = "x_s in component SE_constants (muscle_length)"
    legend_constants[16] = "x_so in component Series_Elastic_Element (muscle_length)"
    legend_constants[30] = "X_M_0 in component X_0 (muscle_length)"
    legend_constants[17] = "L_max in component Series_Elastic_Element (muscle_length)"
    legend_constants[28] = "F_PE in component Parallel_Elastic_Element (force)"
    legend_constants[18] = "alpha_p in component Parallel_Elastic_Element (force)"
    legend_constants[19] = "beta_p in component Parallel_Elastic_Element (muscle_length)"
    legend_constants[27] = "x_p in component PE_constants (muscle_length)"
    legend_constants[20] = "x_po in component Parallel_Elastic_Element (muscle_length)"
    legend_constants[33] = "F_CE in component Contractile_Element (force)"
    legend_constants[21] = "F_PL in component s_h (force)"
    legend_constants[29] = "X_S_0 in component X_0 (muscle_length)"
    legend_constants[22] = "F_PL in component X_0 (force)"
    legend_rates[0] = "d/dt n in component Crossbridges_attached (dimensionless)"
    legend_rates[1] = "d/dt A_c in component Actin_free (dimensionless)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    constants[0] = 10
    states[0] = 0
    states[1] = 1
    constants[1] = 12
    constants[2] = 70
    constants[3] = 40
    constants[4] = 240
    constants[5] = 0.3
    constants[6] = 200
    constants[7] = 5
    constants[8] = 0.45e-6
    constants[9] = 200e12
    constants[10] = 20
    constants[11] = 30.9
    constants[12] = 1.45
    constants[13] = 2
    constants[14] = 0.1027
    constants[15] = 20
    constants[16] = 0.0387
    constants[17] = 1
    constants[18] = 0.00224
    constants[19] = 20
    constants[20] = 0.221
    constants[21] = 3
    constants[22] = 3
    constants[23] = custom_piecewise([less(constants[0] , 0.00000), 0.00000 , greater_equal(constants[0] , 0.00000) & less(constants[0] , constants[1]), (constants[2]*constants[0])/constants[1] , True, 0.00000])
    constants[24] = custom_piecewise([less(constants[0] , 0.00000), constants[4] , greater_equal(constants[0] , 0.00000) & less(constants[0] , constants[1]), (constants[3]*constants[0])/constants[1] , True, (constants[3]*constants[0])/constants[1]])
    constants[25] = constants[20]-(1.00000*1.00000*log(1.00000+constants[21]/constants[18], 10))/constants[19]
    constants[26] = constants[10]*exp(constants[11]*(power(constants[25]/1.00000, constants[12])))
    constants[27] = constants[20]-constants[25]
    constants[28] = constants[18]*(exp((constants[19]*constants[27])/(1.00000*1.00000))-1.00000)
    constants[29] = (1.00000*1.00000*log(1.00000+constants[22]/constants[14], 10))/constants[15]
    constants[30] = ((constants[29]+constants[17])-constants[25])-constants[16]
    constants[31] = (constants[16]+constants[25]+constants[30])-constants[17]
    constants[32] = constants[14]*(exp((constants[15]*constants[31])/(1.00000*1.00000))-1.00000)
    constants[33] = constants[32]-constants[28]
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[0] = constants[23]*(states[1]-states[0])-constants[24]*states[0]
    algebraic[0] = constants[8]*fabs(1.00000-exp(-constants[6]*(power(voi, 2.00000))))*exp(-constants[7]*(power(voi-constants[5], 2.00000)))
    rates[1] = constants[9]*(power(algebraic[0]/1.00000, 2.00000))*(constants[13]-states[1])-constants[26]*states[1]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = constants[8]*fabs(1.00000-exp(-constants[6]*(power(voi, 2.00000))))*exp(-constants[7]*(power(voi-constants[5], 2.00000)))
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
        self.x = 10
        self.h = 12
        self.f_1 = 70
        self.g_1 = 40
        self.g_2 = 240
        self.t_d = 0.3
        self.a_1 = 200
        self.b_1 = 5
        self.Ca_0 = 0.45e-6
        self.c_1 = 200e12
        self.c_2_0 = 20
        self.k_i = 30.9
        self.q = 1.45
        self.AT_0 = 2
        self.alpha_s = 0.1027
        self.beta_s = 20
        self.x_so = 0.0387
        self.L_max = 1
        self.alpha_p = 0.00224
        self.beta_p = 20
        self.x_po = 0.221
        self.F_PL = 3
        self.F_PL_1 = 3

    def to_dict(self):
        return {
            "x": self.x,
            "h": self.h,
            "f_1": self.f_1,
            "g_1": self.g_1,
            "g_2": self.g_2,
            "t_d": self.t_d,
            "a_1": self.a_1,
            "b_1": self.b_1,
            "Ca_0": self.Ca_0,
            "c_1": self.c_1,
            "c_2_0": self.c_2_0,
            "k_i": self.k_i,
            "q": self.q,
            "AT_0": self.AT_0,
            "alpha_s": self.alpha_s,
            "beta_s": self.beta_s,
            "x_so": self.x_so,
            "L_max": self.L_max,
            "alpha_p": self.alpha_p,
            "beta_p": self.beta_p,
            "x_po": self.x_po,
            "F_PL": self.F_PL,
            "F_PL_1": self.F_PL_1,
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
        y0=[0, 1],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "panerai_1980"
        self.curve_names = [
            "n",
            "A_c",
        ]
        self.state_names = ['n', 'A_c']
        self.algebraic_names = ['Ca_f']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 34
        p = self.params

        # direct mapping
        c[0] = p.x
        c[1] = p.h
        c[2] = p.f_1
        c[3] = p.g_1
        c[4] = p.g_2
        c[5] = p.t_d
        c[6] = p.a_1
        c[7] = p.b_1
        c[8] = p.Ca_0
        c[9] = p.c_1
        c[10] = p.c_2_0
        c[11] = p.k_i
        c[12] = p.q
        c[13] = p.AT_0
        c[14] = p.alpha_s
        c[15] = p.beta_s
        c[16] = p.x_so
        c[17] = p.L_max
        c[18] = p.alpha_p
        c[19] = p.beta_p
        c[20] = p.x_po
        c[21] = p.F_PL
        c[22] = p.F_PL_1

        # derived constants
        c[23] = custom_piecewise([less(c[0] , 0.00000), 0.00000 , greater_equal(c[0] , 0.00000) & less(c[0] , c[1]), (c[2]*c[0])/c[1] , True, 0.00000])
        c[24] = custom_piecewise([less(c[0] , 0.00000), c[4] , greater_equal(c[0] , 0.00000) & less(c[0] , c[1]), (c[3]*c[0])/c[1] , True, (c[3]*c[0])/c[1]])
        c[25] = c[20]-(1.00000*1.00000*log(1.00000+c[21]/c[18], 10))/c[19]
        c[26] = c[10]*exp(c[11]*(power(c[25]/1.00000, c[12])))
        c[27] = c[20]-c[25]
        c[28] = c[18]*(exp((c[19]*c[27])/(1.00000*1.00000))-1.00000)
        c[29] = (1.00000*1.00000*log(1.00000+c[22]/c[14], 10))/c[15]
        c[30] = ((c[29]+c[17])-c[25])-c[16]
        c[31] = (c[16]+c[25]+c[30])-c[17]
        c[32] = c[14]*(exp((c[15]*c[31])/(1.00000*1.00000))-1.00000)
        c[33] = c[32]-c[28]

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
