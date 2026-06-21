# Size of variable arrays:
sizeAlgebraic = 1
sizeStates = 2
sizeConstants = 9
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (hour)"
    legend_states[0] = "M in component M (nanomolar)"
    legend_algebraic[0] = "q in component M (dimensionless)"
    legend_constants[0] = "vm in component M (flux)"
    legend_constants[1] = "km in component M (first_order_rate_constant)"
    legend_constants[2] = "Pcrit in component M (nanomolar)"
    legend_constants[3] = "Keq in component M (per_nanomolar)"
    legend_states[1] = "Pt in component Pt (nanomolar)"
    legend_constants[4] = "vp in component Pt (first_order_rate_constant)"
    legend_constants[5] = "kp1 in component Pt (flux)"
    legend_constants[6] = "kp3 in component Pt (first_order_rate_constant)"
    legend_constants[7] = "kp2 in component Pt (flux)"
    legend_constants[8] = "Jp in component Pt (nanomolar)"
    legend_rates[0] = "d/dt M in component M (nanomolar)"
    legend_rates[1] = "d/dt Pt in component Pt (nanomolar)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 0.0
    constants[0] = 1.0
    constants[1] = 0.1
    constants[2] = 0.1
    constants[3] = 200.0
    states[1] = 0.0
    constants[4] = 0.5
    constants[5] = 10.0
    constants[6] = 0.1
    constants[7] = 0.03
    constants[8] = 0.05
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[0] = 2.00000/(1.00000+power(1.00000+8.00000*constants[3]*states[1], 1.0/2))
    rates[0] = constants[0]/(1.00000+power((states[1]*(1.00000-algebraic[0]))/(2.00000*constants[2]), 2.00000))-constants[1]*states[0]
    rates[1] = constants[4]*states[0]-((constants[5]*states[1]*algebraic[0]+constants[7]*states[1])/(constants[8]+states[1])+constants[6]*states[1])
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = 2.00000/(1.00000+power(1.00000+8.00000*constants[3]*states[1], 1.0/2))
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
        self.vm = 1.0
        self.km = 0.1
        self.Pcrit = 0.1
        self.Keq = 200.0
        self.vp = 0.5
        self.kp1 = 10.0
        self.kp3 = 0.1
        self.kp2 = 0.03
        self.Jp = 0.05

    def to_dict(self):
        return {
            "vm": self.vm,
            "km": self.km,
            "Pcrit": self.Pcrit,
            "Keq": self.Keq,
            "vp": self.vp,
            "kp1": self.kp1,
            "kp3": self.kp3,
            "kp2": self.kp2,
            "Jp": self.Jp,
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
        y0=[0.0, 0.0],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "tyson_hong_thron_novak_1999"
        self.curve_names = [
            "M",
            "Pt",
        ]
        self.state_names = ['M', 'Pt']
        self.algebraic_names = ['q']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 9
        p = self.params

        # direct mapping
        c[0] = p.vm
        c[1] = p.km
        c[2] = p.Pcrit
        c[3] = p.Keq
        c[4] = p.vp
        c[5] = p.kp1
        c[6] = p.kp3
        c[7] = p.kp2
        c[8] = p.Jp

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
