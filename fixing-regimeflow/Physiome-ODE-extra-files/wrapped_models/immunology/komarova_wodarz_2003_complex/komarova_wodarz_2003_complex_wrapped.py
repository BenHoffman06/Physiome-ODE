# Size of variable arrays:
sizeAlgebraic = 4
sizeStates = 20
sizeConstants = 26
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (hour)"
    legend_states[0] = "S_0 in component S_0 (dimensionless)"
    legend_constants[15] = "R_0 in component R (first_order_rate_constant)"
    legend_constants[16] = "u_s in component kinetic_parameters (first_order_rate_constant)"
    legend_algebraic[0] = "phi in component phi (first_order_rate_constant)"
    legend_states[1] = "S_1 in component S_1 (dimensionless)"
    legend_constants[17] = "R_1 in component R (first_order_rate_constant)"
    legend_constants[0] = "epsilon_s in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[1] = "alpha in component kinetic_parameters (dimensionless)"
    legend_constants[2] = "u in component kinetic_parameters (first_order_rate_constant)"
    legend_states[2] = "S_2 in component S_2 (dimensionless)"
    legend_constants[18] = "R_2 in component R (first_order_rate_constant)"
    legend_states[3] = "S_3 in component S_3 (dimensionless)"
    legend_constants[19] = "R_3 in component R (first_order_rate_constant)"
    legend_states[4] = "S_4 in component S_4 (dimensionless)"
    legend_constants[20] = "R_4 in component R (first_order_rate_constant)"
    legend_states[5] = "S_5 in component S_5 (dimensionless)"
    legend_constants[21] = "R_5 in component R (first_order_rate_constant)"
    legend_states[6] = "S_6 in component S_6 (dimensionless)"
    legend_constants[22] = "R_6 in component R (first_order_rate_constant)"
    legend_states[7] = "S_7 in component S_7 (dimensionless)"
    legend_constants[23] = "R_7 in component R (first_order_rate_constant)"
    legend_states[8] = "S_8 in component S_8 (dimensionless)"
    legend_constants[24] = "R_8 in component R (first_order_rate_constant)"
    legend_states[9] = "M_0 in component M_0 (dimensionless)"
    legend_constants[3] = "epsilon_m in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[25] = "u_m in component kinetic_parameters (first_order_rate_constant)"
    legend_states[10] = "M_1 in component M_1 (dimensionless)"
    legend_states[11] = "M_1_2 in component M_1 (dimensionless)"
    legend_states[12] = "M_2 in component M_2 (dimensionless)"
    legend_states[13] = "M_3 in component M_3 (dimensionless)"
    legend_states[14] = "M_4 in component M_4 (dimensionless)"
    legend_states[15] = "M_5 in component M_5 (dimensionless)"
    legend_states[16] = "M_6 in component M_6 (dimensionless)"
    legend_states[17] = "M_7 in component M_7 (dimensionless)"
    legend_states[18] = "M_8 in component M_8 (dimensionless)"
    legend_constants[4] = "r_0 in component R (first_order_rate_constant)"
    legend_constants[5] = "r_1 in component R (first_order_rate_constant)"
    legend_constants[6] = "r_2 in component R (first_order_rate_constant)"
    legend_constants[7] = "r_3 in component R (first_order_rate_constant)"
    legend_constants[8] = "r_4 in component R (first_order_rate_constant)"
    legend_constants[9] = "r_5 in component R (first_order_rate_constant)"
    legend_constants[10] = "r_6 in component R (first_order_rate_constant)"
    legend_constants[11] = "r_7 in component R (first_order_rate_constant)"
    legend_constants[12] = "r_8 in component R (first_order_rate_constant)"
    legend_constants[13] = "a in component kinetic_parameters (dimensionless)"
    legend_states[19] = "w in component w (dimensionless)"
    legend_algebraic[1] = "total_cells in component total_cells (dimensionless)"
    legend_algebraic[2] = "stable_total in component total_cells (dimensionless)"
    legend_algebraic[3] = "mutant_total in component total_cells (dimensionless)"
    legend_constants[14] = "beta in component kinetic_parameters (dimensionless)"
    legend_rates[0] = "d/dt S_0 in component S_0 (dimensionless)"
    legend_rates[1] = "d/dt S_1 in component S_1 (dimensionless)"
    legend_rates[2] = "d/dt S_2 in component S_2 (dimensionless)"
    legend_rates[3] = "d/dt S_3 in component S_3 (dimensionless)"
    legend_rates[4] = "d/dt S_4 in component S_4 (dimensionless)"
    legend_rates[5] = "d/dt S_5 in component S_5 (dimensionless)"
    legend_rates[6] = "d/dt S_6 in component S_6 (dimensionless)"
    legend_rates[7] = "d/dt S_7 in component S_7 (dimensionless)"
    legend_rates[8] = "d/dt S_8 in component S_8 (dimensionless)"
    legend_rates[9] = "d/dt M_0 in component M_0 (dimensionless)"
    legend_rates[10] = "d/dt M_1 in component M_1 (dimensionless)"
    legend_rates[11] = "d/dt M_1_2 in component M_1 (dimensionless)"
    legend_rates[12] = "d/dt M_2 in component M_2 (dimensionless)"
    legend_rates[13] = "d/dt M_3 in component M_3 (dimensionless)"
    legend_rates[14] = "d/dt M_4 in component M_4 (dimensionless)"
    legend_rates[15] = "d/dt M_5 in component M_5 (dimensionless)"
    legend_rates[16] = "d/dt M_6 in component M_6 (dimensionless)"
    legend_rates[17] = "d/dt M_7 in component M_7 (dimensionless)"
    legend_rates[18] = "d/dt M_8 in component M_8 (dimensionless)"
    legend_rates[19] = "d/dt w in component w (dimensionless)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 0.5
    states[1] = 0
    constants[0] = 0.99
    constants[1] = 0.6
    constants[2] = 0.07
    states[2] = 0
    states[3] = 0
    states[4] = 0
    states[5] = 0
    states[6] = 0
    states[7] = 0
    states[8] = 0
    states[9] = 0.5
    constants[3] = 0.1
    states[10] = 0
    states[11] = 0
    states[12] = 0
    states[13] = 0
    states[14] = 0
    states[15] = 0
    states[16] = 0
    states[17] = 0
    states[18] = 0
    constants[4] = 0.5
    constants[5] = 0.6
    constants[6] = 0.7
    constants[7] = 0.8
    constants[8] = 0.9
    constants[9] = 1
    constants[10] = 1.1
    constants[11] = 1.2
    constants[12] = 1.3
    constants[13] = 0.5
    states[19] = 0
    constants[14] = 0.2
    constants[15] = constants[4]
    constants[16] = constants[2]*(1.00000-(constants[14]*constants[0])/1.00000)
    constants[17] = constants[5]*(1.00000-constants[13])
    constants[18] = constants[6]*(1.00000-constants[13])
    constants[19] = constants[7]*(1.00000-constants[13])
    constants[20] = constants[8]*(1.00000-constants[13])
    constants[21] = constants[9]*(1.00000-constants[13])
    constants[22] = constants[10]*(1.00000-constants[13])
    constants[23] = constants[11]*(1.00000-constants[13])
    constants[24] = constants[12]*(1.00000-constants[13])
    constants[25] = constants[2]*(1.00000-(constants[14]*constants[3])/1.00000)
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[10] = states[9]*1.00000
    algebraic[0] = ((1.00000-constants[16])/1.00000)*(constants[15]*states[0]+constants[17]*states[1]+constants[18]*states[2]+constants[19]*states[3]+constants[20]*states[4])+((1.00000-constants[25])/1.00000)*(constants[17]*states[10]+constants[18]*states[12]+constants[19]*states[13]+constants[20]*states[14])
    rates[0] = ((constants[15]*states[0])/1.00000)*(1.00000-constants[16])-algebraic[0]*states[0]
    rates[1] = (((constants[1]*constants[2]*constants[15]*states[0])/1.00000)*(1.00000-constants[0])+((constants[17]*states[1])/1.00000)*(1.00000-constants[16]))-algebraic[0]*states[1]
    rates[2] = (((constants[1]*constants[2]*constants[17]*states[1])/1.00000)*(1.00000-constants[0])+((constants[18]*states[2])/1.00000)*(1.00000-constants[16]))-algebraic[0]*states[2]
    rates[3] = (((constants[1]*constants[2]*constants[18]*states[2])/1.00000)*(1.00000-constants[0])+((constants[19]*states[3])/1.00000)*(1.00000-constants[16]))-algebraic[0]*states[3]
    rates[4] = (((constants[1]*constants[2]*constants[19]*states[3])/1.00000)*(1.00000-constants[0])+((constants[20]*states[4])/1.00000)*(1.00000-constants[16]))-algebraic[0]*states[4]
    rates[5] = (((constants[1]*constants[2]*constants[20]*states[4])/1.00000)*(1.00000-constants[0])+((constants[21]*states[5])/1.00000)*(1.00000-constants[16]))-algebraic[0]*states[5]
    rates[6] = (((constants[1]*constants[2]*constants[21]*states[5])/1.00000)*(1.00000-constants[0])+((constants[22]*states[6])/1.00000)*(1.00000-constants[16]))-algebraic[0]*states[6]
    rates[7] = (((constants[1]*constants[2]*constants[22]*states[6])/1.00000)*(1.00000-constants[0])+((constants[23]*states[7])/1.00000)*(1.00000-constants[16]))-algebraic[0]*states[7]
    rates[8] = (((constants[1]*constants[2]*constants[23]*states[7])/1.00000)*(1.00000-constants[0])+((constants[24]*states[8])/1.00000)*(1.00000-constants[16]))-algebraic[0]*states[8]
    rates[9] = ((constants[15]*states[9])/1.00000)*(1.00000-constants[25])-algebraic[0]*states[9]
    rates[11] = (((constants[1]*constants[2]*constants[15]*states[9])/1.00000)*(1.00000-constants[3])+((constants[17]*states[10])/1.00000)*(1.00000-constants[25]))-algebraic[0]*states[10]
    rates[12] = (((constants[1]*constants[2]*constants[17]*states[10])/1.00000)*(1.00000-constants[3])+((constants[18]*states[12])/1.00000)*(1.00000-constants[25]))-algebraic[0]*states[12]
    rates[13] = (((constants[1]*constants[2]*constants[18]*states[12])/1.00000)*(1.00000-constants[3])+((constants[19]*states[13])/1.00000)*(1.00000-constants[25]))-algebraic[0]*states[13]
    rates[14] = (((constants[1]*constants[2]*constants[19]*states[14])/1.00000)*(1.00000-constants[3])+((constants[20]*states[14])/1.00000)*(1.00000-constants[25]))-algebraic[0]*states[14]
    rates[15] = (((constants[1]*constants[2]*constants[20]*states[14])/1.00000)*(1.00000-constants[3])+((constants[21]*states[15])/1.00000)*(1.00000-constants[25]))-algebraic[0]*states[15]
    rates[16] = (((constants[1]*constants[2]*constants[21]*states[15])/1.00000)*(1.00000-constants[3])+((constants[22]*states[16])/1.00000)*(1.00000-constants[25]))-algebraic[0]*states[16]
    rates[17] = (((constants[1]*constants[2]*constants[22]*states[16])/1.00000)*(1.00000-constants[3])+((constants[23]*states[17])/1.00000)*(1.00000-constants[25]))-algebraic[0]*states[17]
    rates[18] = (((constants[1]*constants[2]*constants[23]*states[17])/1.00000)*(1.00000-constants[3])+((constants[24]*states[18])/1.00000)*((1.00000-constants[25])+((constants[1]*constants[2])/1.00000)*(1.00000-constants[3])))-algebraic[0]*states[8]
    rates[19] = (((1.00000-constants[1])*constants[2])/1.00000)*((1.00000-constants[0])*(constants[15]*states[0]+constants[17]*states[1]+constants[18]*states[2]+constants[19]*states[3]+constants[20]*states[4]+constants[21]*states[5]+constants[22]*states[6]+constants[23]*states[7]+constants[24]*states[8])+(1.00000-constants[3])*(constants[15]*states[9]+constants[17]*states[10]+constants[18]*states[12]+constants[19]*states[13]+constants[20]*states[14]+constants[21]*states[15]+constants[22]*states[16]+constants[23]*states[17]+constants[24]*states[18]))-algebraic[0]*states[19]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = ((1.00000-constants[16])/1.00000)*(constants[15]*states[0]+constants[17]*states[1]+constants[18]*states[2]+constants[19]*states[3]+constants[20]*states[4])+((1.00000-constants[25])/1.00000)*(constants[17]*states[10]+constants[18]*states[12]+constants[19]*states[13]+constants[20]*states[14])
    algebraic[1] = states[0]+states[1]+states[2]+states[3]+states[4]+states[5]+states[6]+states[7]+states[8]+states[9]+states[12]+states[13]+states[14]+states[15]+states[16]+states[17]+states[18]
    algebraic[2] = states[0]+states[1]+states[2]+states[3]+states[4]+states[5]+states[6]+states[7]+states[8]
    algebraic[3] = states[9]+states[12]+states[13]+states[14]+states[15]+states[16]+states[17]+states[18]
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
        self.epsilon_s = 0.99
        self.alpha = 0.6
        self.u = 0.07
        self.epsilon_m = 0.1
        self.r_0 = 0.5
        self.r_1 = 0.6
        self.r_2 = 0.7
        self.r_3 = 0.8
        self.r_4 = 0.9
        self.r_5 = 1
        self.r_6 = 1.1
        self.r_7 = 1.2
        self.r_8 = 1.3
        self.a = 0.5
        self.beta = 0.2

    def to_dict(self):
        return {
            "epsilon_s": self.epsilon_s,
            "alpha": self.alpha,
            "u": self.u,
            "epsilon_m": self.epsilon_m,
            "r_0": self.r_0,
            "r_1": self.r_1,
            "r_2": self.r_2,
            "r_3": self.r_3,
            "r_4": self.r_4,
            "r_5": self.r_5,
            "r_6": self.r_6,
            "r_7": self.r_7,
            "r_8": self.r_8,
            "a": self.a,
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
        y0=[0.5, 0, 0, 0, 0, 0, 0, 0, 0, 0.5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "komarova_wodarz_2003_complex"
        self.curve_names = [
            "S_0",
            "S_1",
            "S_2",
            "S_3",
            "S_4",
            "S_5",
            "S_6",
            "S_7",
            "S_8",
            "M_0",
            "M_1",
            "M_1_2",
            "M_2",
            "M_3",
            "M_4",
            "M_5",
            "M_6",
            "M_7",
            "M_8",
            "w",
        ]
        self.state_names = ['S_0', 'S_1', 'S_2', 'S_3', 'S_4', 'S_5', 'S_6', 'S_7', 'S_8', 'M_0', 'M_1', 'M_1_2', 'M_2', 'M_3', 'M_4', 'M_5', 'M_6', 'M_7', 'M_8', 'w']
        self.algebraic_names = ['phi', 'total_cells', 'stable_total', 'mutant_total']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 26
        p = self.params

        # direct mapping
        c[0] = p.epsilon_s
        c[1] = p.alpha
        c[2] = p.u
        c[3] = p.epsilon_m
        c[4] = p.r_0
        c[5] = p.r_1
        c[6] = p.r_2
        c[7] = p.r_3
        c[8] = p.r_4
        c[9] = p.r_5
        c[10] = p.r_6
        c[11] = p.r_7
        c[12] = p.r_8
        c[13] = p.a
        c[14] = p.beta

        # derived constants
        c[15] = c[4]
        c[16] = c[2]*(1.00000-(c[14]*c[0])/1.00000)
        c[17] = c[5]*(1.00000-c[13])
        c[18] = c[6]*(1.00000-c[13])
        c[19] = c[7]*(1.00000-c[13])
        c[20] = c[8]*(1.00000-c[13])
        c[21] = c[9]*(1.00000-c[13])
        c[22] = c[10]*(1.00000-c[13])
        c[23] = c[11]*(1.00000-c[13])
        c[24] = c[12]*(1.00000-c[13])
        c[25] = c[2]*(1.00000-(c[14]*c[3])/1.00000)

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
