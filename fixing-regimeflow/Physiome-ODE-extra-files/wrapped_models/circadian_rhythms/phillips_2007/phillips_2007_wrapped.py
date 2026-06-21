# Size of variable arrays:
sizeAlgebraic = 4
sizeStates = 3
sizeConstants = 17
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (hour)"
    legend_algebraic[0] = "Qv in component v (per_second)"
    legend_states[0] = "Vv in component v (mV)"
    legend_constants[0] = "tau_v in component v (second)"
    legend_constants[1] = "v_vm in component v (mV_second)"
    legend_algebraic[1] = "Qm in component m (per_second)"
    legend_constants[2] = "Qmax in component model_parameters (per_second)"
    legend_algebraic[3] = "D in component D (mV)"
    legend_constants[3] = "theta in component model_parameters (mV)"
    legend_constants[4] = "sigma in component model_parameters (mV)"
    legend_constants[16] = "Qa in component a (per_second)"
    legend_constants[14] = "Va in component a (mV)"
    legend_constants[5] = "Vao in component a (mV)"
    legend_states[1] = "Vm in component m (mV)"
    legend_constants[6] = "tau_m in component m (second)"
    legend_constants[7] = "v_mv in component m (mV_second)"
    legend_constants[8] = "v_maQao in component m (mV)"
    legend_states[2] = "H in component H (nM)"
    legend_constants[9] = "chi in component H (hour)"
    legend_constants[10] = "mu in component H (nM_second)"
    legend_algebraic[2] = "C in component D (dimensionless)"
    legend_constants[11] = "c0 in component D (dimensionless)"
    legend_constants[15] = "omega in component D (per_hour)"
    legend_constants[12] = "v_vc in component D (mV)"
    legend_constants[13] = "v_vh in component D (mV_per_nM)"
    legend_rates[0] = "d/dt Vv in component v (mV)"
    legend_rates[1] = "d/dt Vm in component m (mV)"
    legend_rates[2] = "d/dt H in component H (nM)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 0.0
    constants[0] = 10.0
    constants[1] = -1.9
    constants[2] = 100.0
    constants[3] = 10.0
    constants[4] = 3.0
    constants[5] = 1.0
    states[1] = 0.0
    constants[6] = 10.0
    constants[7] = -1.9
    constants[8] = 1.0
    states[2] = 15.0
    constants[9] = 10.8
    constants[10] = 3.6
    constants[11] = 1.0
    constants[12] = -6.3
    constants[13] = 0.19
    constants[14] = constants[5]
    constants[15] = (2.00000* pi)/24.0000
    constants[16] = constants[2]/(1.00000+exp(-(constants[14]-constants[3])/constants[4]))
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[0] = constants[2]/(1.00000+exp(-(states[0]-constants[3])/constants[4]))
    rates[1] = ((constants[8]+constants[7]*algebraic[0])-states[1])/(constants[6]/3600.00)
    algebraic[1] = constants[2]/(1.00000+exp(-(states[1]-constants[3])/constants[4]))
    rates[2] = (constants[10]*algebraic[1]-states[2])/constants[9]
    algebraic[2] = constants[11]+cos(constants[15]*voi)
    algebraic[3] = constants[12]*algebraic[2]+constants[13]*states[2]
    rates[0] = ((constants[1]*algebraic[1]+algebraic[3])-states[0])/(constants[0]/3600.00)
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = constants[2]/(1.00000+exp(-(states[0]-constants[3])/constants[4]))
    algebraic[1] = constants[2]/(1.00000+exp(-(states[1]-constants[3])/constants[4]))
    algebraic[2] = constants[11]+cos(constants[15]*voi)
    algebraic[3] = constants[12]*algebraic[2]+constants[13]*states[2]
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
        self.tau_v = 10.0
        self.v_vm = -1.9
        self.Qmax = 100.0
        self.theta = 10.0
        self.sigma = 3.0
        self.Vao = 1.0
        self.tau_m = 10.0
        self.v_mv = -1.9
        self.v_maQao = 1.0
        self.chi = 10.8
        self.mu = 3.6
        self.c0 = 1.0
        self.v_vc = -6.3
        self.v_vh = 0.19
        self.omega = (2.00000* pi)/24.0000

    def to_dict(self):
        return {
            "tau_v": self.tau_v,
            "v_vm": self.v_vm,
            "Qmax": self.Qmax,
            "theta": self.theta,
            "sigma": self.sigma,
            "Vao": self.Vao,
            "tau_m": self.tau_m,
            "v_mv": self.v_mv,
            "v_maQao": self.v_maQao,
            "chi": self.chi,
            "mu": self.mu,
            "c0": self.c0,
            "v_vc": self.v_vc,
            "v_vh": self.v_vh,
            "omega": self.omega,
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
        y0=[0.0, 0.0, 15.0],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "phillips_2007"
        self.curve_names = [
            "Vv",
            "Vm",
            "H",
        ]
        self.state_names = ['Vv', 'Vm', 'H']
        self.algebraic_names = ['Qv', 'Qm', 'C', 'D']
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
        c[0] = p.tau_v
        c[1] = p.v_vm
        c[2] = p.Qmax
        c[3] = p.theta
        c[4] = p.sigma
        c[5] = p.Vao
        c[6] = p.tau_m
        c[7] = p.v_mv
        c[8] = p.v_maQao
        c[9] = p.chi
        c[10] = p.mu
        c[11] = p.c0
        c[12] = p.v_vc
        c[13] = p.v_vh
        c[15] = p.omega

        # derived constants
        c[14] = c[5]
        c[16] = c[2]/(1.00000+exp(-(c[14]-c[3])/c[4]))

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
