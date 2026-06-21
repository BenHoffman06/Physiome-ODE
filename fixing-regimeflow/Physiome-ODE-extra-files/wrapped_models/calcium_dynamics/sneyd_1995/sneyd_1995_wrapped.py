# Size of variable arrays:
sizeAlgebraic = 3
sizeStates = 3
sizeConstants = 13
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component enviroment (second)"
    legend_states[0] = "P in component P (micromolar)"
    legend_constants[0] = "V_p in component P (per_second)"
    legend_constants[1] = "k_p in component P (micromolar)"
    legend_constants[2] = "IPR_3_flux in component P (flux)"
    legend_states[1] = "c in component c (micromolar)"
    legend_algebraic[2] = "J_flux in component J_flux (flux)"
    legend_algebraic[0] = "J_pump in component J_pump (flux)"
    legend_constants[12] = "J_leak in component J_leak (flux)"
    legend_constants[3] = "k_flux in component J_flux (micromolar_per_second)"
    legend_algebraic[1] = "mu in component mu (dimensionless)"
    legend_states[2] = "h in component h (dimensionless)"
    legend_constants[4] = "b in component J_flux (dimensionless)"
    legend_constants[5] = "k_1 in component J_flux (micromolar)"
    legend_constants[6] = "gamma in component J_pump (micromolar_per_second)"
    legend_constants[7] = "k_gamma in component J_pump (micromolar)"
    legend_constants[8] = "beta in component J_leak (flux)"
    legend_constants[9] = "k_mu in component mu (micromolar)"
    legend_constants[10] = "k_2 in component h (micromolar)"
    legend_constants[11] = "tau_h in component h (second)"
    legend_rates[0] = "d/dt P in component P (micromolar)"
    legend_rates[1] = "d/dt c in component c (micromolar)"
    legend_rates[2] = "d/dt h in component h (dimensionless)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 0
    constants[0] = 0.08
    constants[1] = 1
    constants[2] = 0.72
    states[1] = 0.3
    constants[3] = 3
    states[2] = 1
    constants[4] = 0.11
    constants[5] = 0.7
    constants[6] = 1
    constants[7] = 0.27
    constants[8] = 0.15
    constants[9] = 0.01
    constants[10] = 0.7
    constants[11] = 0.2
    constants[12] = constants[8]
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[0] = custom_piecewise([less_equal(voi , 15.0000), constants[2]-(constants[0]*states[0]*constants[1])/(constants[1]+states[0]) , True, (-constants[0]*states[0]*constants[1])/(constants[1]+states[0])])
    rates[2] = ((power(constants[10], 2.00000))/(power(constants[10], 2.00000)+power(states[1], 2.00000))-states[2])/constants[11]
    algebraic[1] = (power(states[0], 3.00000))/(power(constants[9], 3.00000)+power(states[0], 3.00000))
    algebraic[2] = constants[3]*algebraic[1]*states[2]*(constants[4]+((1.00000-constants[4])*states[1])/(constants[5]+states[1]))
    algebraic[0] = (constants[6]*(power(states[1], 2.00000)))/(power(constants[7], 2.00000)+power(states[1], 2.00000))
    rates[1] = (algebraic[2]-algebraic[0])+constants[12]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[1] = (power(states[0], 3.00000))/(power(constants[9], 3.00000)+power(states[0], 3.00000))
    algebraic[2] = constants[3]*algebraic[1]*states[2]*(constants[4]+((1.00000-constants[4])*states[1])/(constants[5]+states[1]))
    algebraic[0] = (constants[6]*(power(states[1], 2.00000)))/(power(constants[7], 2.00000)+power(states[1], 2.00000))
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
        self.V_p = 0.08
        self.k_p = 1
        self.IPR_3_flux = 0.72
        self.k_flux = 3
        self.b = 0.11
        self.k_1 = 0.7
        self.gamma = 1
        self.k_gamma = 0.27
        self.beta = 0.15
        self.k_mu = 0.01
        self.k_2 = 0.7
        self.tau_h = 0.2

    def to_dict(self):
        return {
            "V_p": self.V_p,
            "k_p": self.k_p,
            "IPR_3_flux": self.IPR_3_flux,
            "k_flux": self.k_flux,
            "b": self.b,
            "k_1": self.k_1,
            "gamma": self.gamma,
            "k_gamma": self.k_gamma,
            "beta": self.beta,
            "k_mu": self.k_mu,
            "k_2": self.k_2,
            "tau_h": self.tau_h,
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
        y0=[0, 0.3, 1],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "sneyd_1995"
        self.curve_names = [
            "P",
            "c",
            "h",
        ]
        self.state_names = ['P', 'c', 'h']
        self.algebraic_names = ['J_pump', 'mu', 'J_flux']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 13
        p = self.params

        # direct mapping
        c[0] = p.V_p
        c[1] = p.k_p
        c[2] = p.IPR_3_flux
        c[3] = p.k_flux
        c[4] = p.b
        c[5] = p.k_1
        c[6] = p.gamma
        c[7] = p.k_gamma
        c[8] = p.beta
        c[9] = p.k_mu
        c[10] = p.k_2
        c[11] = p.tau_h

        # derived constants
        c[12] = c[8]

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
