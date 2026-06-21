# Size of variable arrays:
sizeAlgebraic = 5
sizeStates = 3
sizeConstants = 14
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (second)"
    legend_states[0] = "V in component membrane (millivolt)"
    legend_constants[0] = "Cm in component membrane (picoF)"
    legend_algebraic[0] = "i_s in component calcium_channel (femtoA)"
    legend_algebraic[2] = "i_K in component potassium_channel (femtoA)"
    legend_algebraic[3] = "i_K_ACh in component acetyl_choline_activated_potassium_channel (femtoA)"
    legend_algebraic[4] = "i_j in component coupling_current (femtoA)"
    legend_constants[1] = "g_s in component calcium_channel (picoS)"
    legend_constants[2] = "V_s in component calcium_channel (millivolt)"
    legend_constants[3] = "V_1 in component calcium_channel (millivolt)"
    legend_constants[4] = "V_2 in component calcium_channel (millivolt)"
    legend_constants[5] = "g_K in component potassium_channel (picoS)"
    legend_constants[6] = "V_K in component potassium_channel (millivolt)"
    legend_states[1] = "w in component potassium_channel_w_gate (dimensionless)"
    legend_constants[7] = "lambda_w in component potassium_channel_w_gate (per_second)"
    legend_constants[8] = "V_3 in component potassium_channel_w_gate (millivolt)"
    legend_constants[9] = "V_4 in component potassium_channel_w_gate (millivolt)"
    legend_states[2] = "u in component acetyl_choline_activated_potassium_channel_u_gate (dimensionless)"
    legend_constants[13] = "alpha in component acetyl_choline_activated_potassium_channel_u_gate (per_second)"
    legend_algebraic[1] = "beta in component acetyl_choline_activated_potassium_channel_u_gate (per_second)"
    legend_constants[10] = "ACh in component acetyl_choline_activated_potassium_channel_u_gate (molar)"
    legend_constants[11] = "g_j in component coupling_current (picoS)"
    legend_constants[12] = "V_B in component coupling_current (millivolt)"
    legend_rates[0] = "d/dt V in component membrane (millivolt)"
    legend_rates[1] = "d/dt w in component potassium_channel_w_gate (dimensionless)"
    legend_rates[2] = "d/dt u in component acetyl_choline_activated_potassium_channel_u_gate (dimensionless)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = -52.07606
    constants[0] = 60
    constants[1] = 382.9118
    constants[2] = 214.1429
    constants[3] = -35.9358
    constants[4] = 7.8589
    constants[5] = 536.1093
    constants[6] = -259.0783
    states[1] = 0.0008971
    constants[7] = 20.7796
    constants[8] = -27.9375
    constants[9] = 6.321
    states[2] = 0.2344555
    constants[10] = 1e-6
    constants[11] = 0
    constants[12] = -50
    constants[13] = 0.0123320/(1.00000+4.20000e-06/constants[10])
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[1] = constants[7]*cosh((states[0]-constants[8])/(2.00000*constants[9]))*((1.00000/2.00000)*(1.00000+tanh((states[0]-constants[8])/constants[9]))-states[1])
    algebraic[1] = 0.0100000*exp(0.0133000*(states[0]+40.0000))
    rates[2] = constants[13]*(1.00000-states[2])-algebraic[1]*states[2]
    algebraic[0] = (1.00000/2.00000)*constants[1]*(1.00000+tanh((states[0]-constants[3])/constants[4]))*(states[0]-constants[2])
    algebraic[2] = constants[5]*states[1]*(states[0]-constants[6])
    algebraic[3] = 1.00000*0.270000*states[2]*(states[0]+90.0000)
    algebraic[4] = constants[11]*(states[0]-constants[12])
    rates[0] = -(algebraic[0]+algebraic[2]+algebraic[3]+algebraic[4])/constants[0]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[1] = 0.0100000*exp(0.0133000*(states[0]+40.0000))
    algebraic[0] = (1.00000/2.00000)*constants[1]*(1.00000+tanh((states[0]-constants[3])/constants[4]))*(states[0]-constants[2])
    algebraic[2] = constants[5]*states[1]*(states[0]-constants[6])
    algebraic[3] = 1.00000*0.270000*states[2]*(states[0]+90.0000)
    algebraic[4] = constants[11]*(states[0]-constants[12])
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
        self.Cm = 60
        self.g_s = 382.9118
        self.V_s = 214.1429
        self.V_1 = -35.9358
        self.V_2 = 7.8589
        self.g_K = 536.1093
        self.V_K = -259.0783
        self.lambda_w = 20.7796
        self.V_3 = -27.9375
        self.V_4 = 6.321
        self.ACh = 1e-6
        self.g_j = 0
        self.V_B = -50

    def to_dict(self):
        return {
            "Cm": self.Cm,
            "g_s": self.g_s,
            "V_s": self.V_s,
            "V_1": self.V_1,
            "V_2": self.V_2,
            "g_K": self.g_K,
            "V_K": self.V_K,
            "lambda_w": self.lambda_w,
            "V_3": self.V_3,
            "V_4": self.V_4,
            "ACh": self.ACh,
            "g_j": self.g_j,
            "V_B": self.V_B,
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
        y0=[-52.07606, 0.0008971, 0.2344555],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "endresen_1996"
        self.curve_names = [
            "V",
            "w",
            "u",
        ]
        self.state_names = ['V', 'w', 'u']
        self.algebraic_names = ['i_s', 'beta', 'i_K', 'i_K_ACh', 'i_j']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 14
        p = self.params

        # direct mapping
        c[0] = p.Cm
        c[1] = p.g_s
        c[2] = p.V_s
        c[3] = p.V_1
        c[4] = p.V_2
        c[5] = p.g_K
        c[6] = p.V_K
        c[7] = p.lambda_w
        c[8] = p.V_3
        c[9] = p.V_4
        c[10] = p.ACh
        c[11] = p.g_j
        c[12] = p.V_B

        # derived constants
        c[13] = 0.0123320/(1.00000+4.20000e-06/c[10])

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
