# Size of variable arrays:
sizeAlgebraic = 13
sizeStates = 5
sizeConstants = 15
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
    legend_algebraic[0] = "Vs in component membrane (millivolt)"
    legend_constants[0] = "V_I in component membrane (millivolt)"
    legend_constants[1] = "V_K in component membrane (millivolt)"
    legend_constants[2] = "V_L in component membrane (millivolt)"
    legend_constants[3] = "V_H_Na in component membrane (millivolt)"
    legend_constants[4] = "V_H_K in component membrane (millivolt)"
    legend_constants[13] = "g_I in component membrane (milliS_per_microF)"
    legend_constants[5] = "g_K in component membrane (milliS_per_microF)"
    legend_constants[6] = "g_L in component membrane (milliS_per_microF)"
    legend_constants[14] = "g_T in component membrane (milliS_per_microF)"
    legend_constants[7] = "g_P in component membrane (milliS_per_microF)"
    legend_constants[8] = "Kp in component membrane (millimolar)"
    legend_states[1] = "c in component calcium_concentration (millimolar)"
    legend_algebraic[8] = "sI in component sI_gate (dimensionless)"
    legend_states[2] = "yI in component yI_gate (dimensionless)"
    legend_states[3] = "xT in component xT_gate (dimensionless)"
    legend_states[4] = "xK in component xK_gate (dimensionless)"
    legend_algebraic[1] = "alpha_m in component sI_gate (per_millisecond)"
    legend_algebraic[5] = "beta_m in component sI_gate (per_millisecond)"
    legend_algebraic[9] = "ZI in component yI_gate (dimensionless)"
    legend_algebraic[2] = "alpha_h in component yI_gate (per_millisecond)"
    legend_algebraic[6] = "beta_h in component yI_gate (per_millisecond)"
    legend_algebraic[11] = "tau_yI in component yI_gate (millisecond)"
    legend_algebraic[3] = "sT in component xT_gate (dimensionless)"
    legend_constants[9] = "tau_xT in component xT_gate (millisecond)"
    legend_constants[10] = "V_Ca in component calcium_concentration (millivolt)"
    legend_constants[11] = "rho in component calcium_concentration (per_millisecond)"
    legend_constants[12] = "K_c in component calcium_concentration (millimolar_per_millivolt)"
    legend_algebraic[4] = "alpha_n in component xK_gate (per_millisecond)"
    legend_algebraic[7] = "beta_n in component xK_gate (per_millisecond)"
    legend_algebraic[12] = "tau_xK in component xK_gate (millisecond)"
    legend_algebraic[10] = "sK in component xK_gate (dimensionless)"
    legend_rates[0] = "d/dt V in component membrane (millivolt)"
    legend_rates[2] = "d/dt yI in component yI_gate (dimensionless)"
    legend_rates[3] = "d/dt xT in component xT_gate (dimensionless)"
    legend_rates[1] = "d/dt c in component calcium_concentration (millimolar)"
    legend_rates[4] = "d/dt xK in component xK_gate (dimensionless)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = -54
    constants[0] = 30.0
    constants[1] = -75.0
    constants[2] = -40.0
    constants[3] = 115.0
    constants[4] = -12.0
    constants[5] = 0.3
    constants[6] = 0.003
    constants[7] = 0.03
    constants[8] = 0.5
    states[1] = 0.1
    states[2] = 0.1
    states[3] = 0.1
    states[4] = 0.1
    constants[9] = 235.0
    constants[10] = 140.0
    constants[11] = 0.0003
    constants[12] = 0.0085
    constants[13] = 1.00000*((constants[3]-constants[4])/(constants[0]-constants[1]))
    constants[14] = 1.00000*((constants[3]*constants[1]-constants[0]*constants[4])/(constants[0]-constants[1]))
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[1] = constants[11]*(constants[12]*states[3]*(constants[10]-states[0])-states[1])
    algebraic[0] = 1.00000*constants[13]*states[0]+1.00000*constants[14]
    algebraic[3] = 1.00000/(exp(0.150000*(-50.0000-algebraic[0]))+1.00000)
    rates[3] = (algebraic[3]-states[3])/constants[9]
    algebraic[1] = (0.100000*(50.0000-algebraic[0]))/-exp((50.0000-algebraic[0])/10.0000)
    algebraic[5] = 4.00000*exp((25.0000-algebraic[0])/18.0000)
    algebraic[8] = algebraic[1]/(algebraic[1]+algebraic[5])
    rates[0] = (constants[13]*(power(algebraic[8], 3.00000))*states[2]+constants[14]*states[3])*(constants[0]-states[0])+(constants[5]*(power(states[4], 4.00000))+constants[7]*states[1]*(power(constants[8]+states[1], -1.00000)))*(constants[1]-states[0])+constants[6]*(constants[2]-states[0])
    algebraic[2] = 0.0700000*exp((25.0000-algebraic[0])/20.0000)
    algebraic[6] = 1.00000/(exp((55.0000-algebraic[0])/10.0000)+1.00000)
    algebraic[9] = algebraic[2]/(algebraic[2]+algebraic[6])
    algebraic[11] = 12.5000/(algebraic[2]+algebraic[6])
    rates[2] = (algebraic[9]-states[2])/algebraic[11]
    algebraic[4] = (0.0100000*(55.0000-algebraic[0]))/(exp((55.0000-algebraic[0])/10.0000)-1.00000)
    algebraic[7] = 0.125000*exp((45.0000-algebraic[0])/80.0000)
    algebraic[12] = 12.5000/(algebraic[4]+algebraic[7])
    algebraic[10] = algebraic[4]/(algebraic[4]+algebraic[7])
    rates[4] = (algebraic[10]-states[4])/algebraic[12]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = 1.00000*constants[13]*states[0]+1.00000*constants[14]
    algebraic[3] = 1.00000/(exp(0.150000*(-50.0000-algebraic[0]))+1.00000)
    algebraic[1] = (0.100000*(50.0000-algebraic[0]))/-exp((50.0000-algebraic[0])/10.0000)
    algebraic[5] = 4.00000*exp((25.0000-algebraic[0])/18.0000)
    algebraic[8] = algebraic[1]/(algebraic[1]+algebraic[5])
    algebraic[2] = 0.0700000*exp((25.0000-algebraic[0])/20.0000)
    algebraic[6] = 1.00000/(exp((55.0000-algebraic[0])/10.0000)+1.00000)
    algebraic[9] = algebraic[2]/(algebraic[2]+algebraic[6])
    algebraic[11] = 12.5000/(algebraic[2]+algebraic[6])
    algebraic[4] = (0.0100000*(55.0000-algebraic[0]))/(exp((55.0000-algebraic[0])/10.0000)-1.00000)
    algebraic[7] = 0.125000*exp((45.0000-algebraic[0])/80.0000)
    algebraic[12] = 12.5000/(algebraic[4]+algebraic[7])
    algebraic[10] = algebraic[4]/(algebraic[4]+algebraic[7])
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
        self.V_I = 30.0
        self.V_K = -75.0
        self.V_L = -40.0
        self.V_H_Na = 115.0
        self.V_H_K = -12.0
        self.g_K = 0.3
        self.g_L = 0.003
        self.g_P = 0.03
        self.Kp = 0.5
        self.tau_xT = 235.0
        self.V_Ca = 140.0
        self.rho = 0.0003
        self.K_c = 0.0085

    def to_dict(self):
        return {
            "V_I": self.V_I,
            "V_K": self.V_K,
            "V_L": self.V_L,
            "V_H_Na": self.V_H_Na,
            "V_H_K": self.V_H_K,
            "g_K": self.g_K,
            "g_L": self.g_L,
            "g_P": self.g_P,
            "Kp": self.Kp,
            "tau_xT": self.tau_xT,
            "V_Ca": self.V_Ca,
            "rho": self.rho,
            "K_c": self.K_c,
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
        y0=[-54, 0.1, 0.1, 0.1, 0.1],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "plant_1981"
        self.curve_names = [
            "V",
            "c",
            "yI",
            "xT",
            "xK",
        ]
        self.state_names = ['V', 'c', 'yI', 'xT', 'xK']
        self.algebraic_names = ['Vs', 'alpha_m', 'alpha_h', 'sT', 'alpha_n', 'beta_m', 'beta_h', 'beta_n', 'sI', 'ZI', 'sK', 'tau_yI', 'tau_xK']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 15
        p = self.params

        # direct mapping
        c[0] = p.V_I
        c[1] = p.V_K
        c[2] = p.V_L
        c[3] = p.V_H_Na
        c[4] = p.V_H_K
        c[5] = p.g_K
        c[6] = p.g_L
        c[7] = p.g_P
        c[8] = p.Kp
        c[9] = p.tau_xT
        c[10] = p.V_Ca
        c[11] = p.rho
        c[12] = p.K_c

        # derived constants
        c[13] = 1.00000*((c[3]-c[4])/(c[0]-c[1]))
        c[14] = 1.00000*((c[3]*c[1]-c[0]*c[4])/(c[0]-c[1]))

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
