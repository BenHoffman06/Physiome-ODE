# Size of variable arrays:
sizeAlgebraic = 2
sizeStates = 10
sizeConstants = 38
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (hour)"
    legend_constants[0] = "v_sP in component nucleus (nanomolar_hour)"
    legend_constants[1] = "v_mP in component nucleus (nanomolar_hour)"
    legend_constants[2] = "K_IP in component nucleus (nanomolar)"
    legend_constants[3] = "K_mP in component nucleus (nanomolar)"
    legend_constants[4] = "v_sT in component nucleus (nanomolar_hour)"
    legend_constants[5] = "v_mT in component nucleus (nanomolar_hour)"
    legend_constants[6] = "K_IT in component nucleus (nanomolar)"
    legend_constants[7] = "K_mT in component nucleus (nanomolar)"
    legend_constants[8] = "k_d in component cytosol (per_hour)"
    legend_constants[9] = "n in component nucleus (dimensionless)"
    legend_constants[10] = "k_1 in component cytosol (per_hour)"
    legend_constants[11] = "k_2 in component cytosol (per_hour)"
    legend_constants[12] = "k_dN in component nucleus (per_hour)"
    legend_states[0] = "C in component cytosol (nanomolar)"
    legend_states[1] = "M_P in component nucleus (nanomolar)"
    legend_states[2] = "M_T in component nucleus (nanomolar)"
    legend_states[3] = "C_N in component nucleus (nanomolar)"
    legend_constants[13] = "k_3 in component cytosol (per_nanomolar_hour)"
    legend_constants[14] = "k_4 in component cytosol (per_hour)"
    legend_constants[15] = "k_dC in component cytosol (per_hour)"
    legend_states[4] = "P_0 in component PER (nanomolar)"
    legend_states[5] = "P_1 in component PER (nanomolar)"
    legend_states[6] = "P_2 in component PER (nanomolar)"
    legend_states[7] = "T_0 in component TIM (nanomolar)"
    legend_states[8] = "T_1 in component TIM (nanomolar)"
    legend_states[9] = "T_2 in component TIM (nanomolar)"
    legend_constants[16] = "V_1P in component PER (nanomolar_hour)"
    legend_constants[17] = "V_2P in component PER (nanomolar_hour)"
    legend_constants[18] = "V_3P in component PER (nanomolar_hour)"
    legend_constants[19] = "V_4P in component PER (nanomolar_hour)"
    legend_constants[20] = "K_1P in component PER (nanomolar)"
    legend_constants[21] = "K_2P in component PER (nanomolar)"
    legend_constants[22] = "K_3P in component PER (nanomolar)"
    legend_constants[23] = "K_4P in component PER (nanomolar)"
    legend_constants[24] = "K_dP in component PER (nanomolar)"
    legend_constants[25] = "v_dP in component PER (nanomolar_hour)"
    legend_constants[26] = "k_sP in component PER (per_hour)"
    legend_constants[27] = "V_1T in component TIM (nanomolar_hour)"
    legend_constants[28] = "V_2T in component TIM (nanomolar_hour)"
    legend_constants[29] = "V_3T in component TIM (nanomolar_hour)"
    legend_constants[30] = "V_4T in component TIM (nanomolar_hour)"
    legend_constants[31] = "K_1T in component TIM (nanomolar)"
    legend_constants[32] = "K_2T in component TIM (nanomolar)"
    legend_constants[33] = "K_3T in component TIM (nanomolar)"
    legend_constants[34] = "K_4T in component TIM (nanomolar)"
    legend_constants[35] = "K_dT in component TIM (nanomolar)"
    legend_constants[36] = "v_dT in component TIM (nanomolar_hour)"
    legend_constants[37] = "k_sT in component TIM (per_hour)"
    legend_algebraic[0] = "P_t in component PER_total (nanomolar)"
    legend_algebraic[1] = "T_t in component TIM_total (nanomolar)"
    legend_rates[1] = "d/dt M_P in component nucleus (nanomolar)"
    legend_rates[2] = "d/dt M_T in component nucleus (nanomolar)"
    legend_rates[3] = "d/dt C_N in component nucleus (nanomolar)"
    legend_rates[0] = "d/dt C in component cytosol (nanomolar)"
    legend_rates[4] = "d/dt P_0 in component PER (nanomolar)"
    legend_rates[5] = "d/dt P_1 in component PER (nanomolar)"
    legend_rates[6] = "d/dt P_2 in component PER (nanomolar)"
    legend_rates[7] = "d/dt T_0 in component TIM (nanomolar)"
    legend_rates[8] = "d/dt T_1 in component TIM (nanomolar)"
    legend_rates[9] = "d/dt T_2 in component TIM (nanomolar)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    constants[0] = 1
    constants[1] = 0.7
    constants[2] = 1
    constants[3] = 0.2
    constants[4] = 1
    constants[5] = 0.7
    constants[6] = 1
    constants[7] = 0.2
    constants[8] = 0.01
    constants[9] = 4
    constants[10] = 0.6
    constants[11] = 0.2
    constants[12] = 0.01
    states[0] = 0.344
    states[1] = 0.031
    states[2] = 0.031
    states[3] = 1.77
    constants[13] = 1.2
    constants[14] = 0.6
    constants[15] = 0.01
    states[4] = 0.0114
    states[5] = 0.0178
    states[6] = 0.0322
    states[7] = 0.0114
    states[8] = 0.0178
    states[9] = 0.0324
    constants[16] = 8
    constants[17] = 1
    constants[18] = 8
    constants[19] = 1
    constants[20] = 2
    constants[21] = 2
    constants[22] = 2
    constants[23] = 2
    constants[24] = 0.2
    constants[25] = 2
    constants[26] = 0.9
    constants[27] = 8
    constants[28] = 1
    constants[29] = 8
    constants[30] = 1
    constants[31] = 2
    constants[32] = 2
    constants[33] = 2
    constants[34] = 2
    constants[35] = 0.2
    constants[36] = 2
    constants[37] = 0.9
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[1] = (constants[0]*((power(constants[2], constants[9]))/(power(constants[2], constants[9])+power(states[3], constants[9])))-constants[1]*(states[1]/(constants[3]+states[1])))-constants[8]*states[1]
    rates[2] = (constants[4]*((power(constants[6], constants[9]))/(power(constants[6], constants[9])+power(states[3], constants[9])))-constants[5]*(states[2]/(constants[7]+states[2])))-constants[8]*states[2]
    rates[3] = (constants[10]*states[0]-constants[11]*states[3])-constants[12]*states[3]
    rates[0] = (((constants[13]*states[6]*states[9]-constants[14]*states[0])-constants[10]*states[0])+constants[11]*states[3])-constants[15]*states[0]
    rates[4] = ((constants[26]*states[1]-constants[16]*(states[4]/(constants[20]+states[4])))+constants[17]*(states[5]/(constants[21]+states[5])))-constants[8]*states[4]
    rates[5] = (((constants[16]*(states[4]/(constants[20]+states[4]))-constants[17]*(states[5]/(constants[21]+states[5])))-constants[18]*(states[5]/(constants[22]+states[5])))+constants[19]*(states[6]/(constants[23]+states[6])))-constants[8]*states[5]
    rates[6] = ((((constants[18]*(states[5]/(constants[22]+states[5]))-constants[19]*(states[6]/(constants[23]+states[6])))-constants[13]*states[6]*states[9])+constants[14]*states[0])-constants[25]*(states[6]/(constants[24]+states[6])))-constants[8]*states[6]
    rates[7] = ((constants[37]*states[2]-constants[27]*(states[7]/(constants[31]+states[7])))+constants[28]*(states[8]/(constants[32]+states[8])))-constants[8]*states[7]
    rates[8] = (((constants[27]*(states[7]/(constants[31]+states[7]))-constants[28]*(states[8]/(constants[32]+states[8])))-constants[29]*(states[8]/(constants[33]+states[8])))+constants[30]*(states[9]/(constants[34]+states[9])))-constants[8]*states[8]
    rates[9] = ((((constants[29]*(states[8]/(constants[33]+states[8]))-constants[30]*(states[9]/(constants[34]+states[9])))-constants[13]*states[6]*states[9])+constants[14]*states[0])-constants[36]*(states[9]/(constants[35]+states[9])))-constants[8]*states[9]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = states[4]+states[5]+states[6]+states[0]+states[3]
    algebraic[1] = states[7]+states[8]+states[9]+states[0]+states[3]
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
        self.v_sP = 1
        self.v_mP = 0.7
        self.K_IP = 1
        self.K_mP = 0.2
        self.v_sT = 1
        self.v_mT = 0.7
        self.K_IT = 1
        self.K_mT = 0.2
        self.k_d = 0.01
        self.n = 4
        self.k_1 = 0.6
        self.k_2 = 0.2
        self.k_dN = 0.01
        self.k_3 = 1.2
        self.k_4 = 0.6
        self.k_dC = 0.01
        self.V_1P = 8
        self.V_2P = 1
        self.V_3P = 8
        self.V_4P = 1
        self.K_1P = 2
        self.K_2P = 2
        self.K_3P = 2
        self.K_4P = 2
        self.K_dP = 0.2
        self.v_dP = 2
        self.k_sP = 0.9
        self.V_1T = 8
        self.V_2T = 1
        self.V_3T = 8
        self.V_4T = 1
        self.K_1T = 2
        self.K_2T = 2
        self.K_3T = 2
        self.K_4T = 2
        self.K_dT = 0.2
        self.v_dT = 2
        self.k_sT = 0.9

    def to_dict(self):
        return {
            "v_sP": self.v_sP,
            "v_mP": self.v_mP,
            "K_IP": self.K_IP,
            "K_mP": self.K_mP,
            "v_sT": self.v_sT,
            "v_mT": self.v_mT,
            "K_IT": self.K_IT,
            "K_mT": self.K_mT,
            "k_d": self.k_d,
            "n": self.n,
            "k_1": self.k_1,
            "k_2": self.k_2,
            "k_dN": self.k_dN,
            "k_3": self.k_3,
            "k_4": self.k_4,
            "k_dC": self.k_dC,
            "V_1P": self.V_1P,
            "V_2P": self.V_2P,
            "V_3P": self.V_3P,
            "V_4P": self.V_4P,
            "K_1P": self.K_1P,
            "K_2P": self.K_2P,
            "K_3P": self.K_3P,
            "K_4P": self.K_4P,
            "K_dP": self.K_dP,
            "v_dP": self.v_dP,
            "k_sP": self.k_sP,
            "V_1T": self.V_1T,
            "V_2T": self.V_2T,
            "V_3T": self.V_3T,
            "V_4T": self.V_4T,
            "K_1T": self.K_1T,
            "K_2T": self.K_2T,
            "K_3T": self.K_3T,
            "K_4T": self.K_4T,
            "K_dT": self.K_dT,
            "v_dT": self.v_dT,
            "k_sT": self.k_sT,
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
        y0=[0.344, 0.031, 0.031, 1.77, 0.0114, 0.0178, 0.0322, 0.0114, 0.0178, 0.0324],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "leloup_1998a"
        self.curve_names = [
            "C",
            "M_P",
            "M_T",
            "C_N",
            "P_0",
            "P_1",
            "P_2",
            "T_0",
            "T_1",
            "T_2",
        ]
        self.state_names = ['C', 'M_P', 'M_T', 'C_N', 'P_0', 'P_1', 'P_2', 'T_0', 'T_1', 'T_2']
        self.algebraic_names = ['P_t', 'T_t']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 38
        p = self.params

        # direct mapping
        c[0] = p.v_sP
        c[1] = p.v_mP
        c[2] = p.K_IP
        c[3] = p.K_mP
        c[4] = p.v_sT
        c[5] = p.v_mT
        c[6] = p.K_IT
        c[7] = p.K_mT
        c[8] = p.k_d
        c[9] = p.n
        c[10] = p.k_1
        c[11] = p.k_2
        c[12] = p.k_dN
        c[13] = p.k_3
        c[14] = p.k_4
        c[15] = p.k_dC
        c[16] = p.V_1P
        c[17] = p.V_2P
        c[18] = p.V_3P
        c[19] = p.V_4P
        c[20] = p.K_1P
        c[21] = p.K_2P
        c[22] = p.K_3P
        c[23] = p.K_4P
        c[24] = p.K_dP
        c[25] = p.v_dP
        c[26] = p.k_sP
        c[27] = p.V_1T
        c[28] = p.V_2T
        c[29] = p.V_3T
        c[30] = p.V_4T
        c[31] = p.K_1T
        c[32] = p.K_2T
        c[33] = p.K_3T
        c[34] = p.K_4T
        c[35] = p.K_dT
        c[36] = p.v_dT
        c[37] = p.k_sT

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
