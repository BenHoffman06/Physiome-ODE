# Size of variable arrays:
sizeAlgebraic = 0
sizeStates = 2
sizeConstants = 11
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (minute)"
    legend_states[0] = "GSH in component GSH (millimolar)"
    legend_constants[0] = "V in component GSH (flux)"
    legend_constants[1] = "Kms in component GSH (millimolar)"
    legend_constants[2] = "Kmp in component GSH (millimolar)"
    legend_constants[3] = "Kmq in component GSH (millimolar)"
    legend_constants[4] = "Keq in component GSH (millimolar)"
    legend_states[1] = "SDLGSH in component SDLGSH (millimolar)"
    legend_constants[5] = "D_lactate in component D_lactate (millimolar)"
    legend_constants[6] = "HTA in component HTA (millimolar)"
    legend_constants[7] = "V in component SDLGSH (flux)"
    legend_constants[8] = "Kms in component SDLGSH (millimolar)"
    legend_constants[9] = "Kmp in component SDLGSH (millimolar)"
    legend_constants[10] = "Keq in component SDLGSH (dimensionless)"
    legend_rates[0] = "d/dt GSH in component GSH (millimolar)"
    legend_rates[1] = "d/dt SDLGSH in component SDLGSH (millimolar)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 1.0
    constants[0] = 3.44E-3
    constants[1] = 0.49
    constants[2] = 0.49
    constants[3] = 0.49
    constants[4] = 0.49
    states[1] = 1.0
    constants[5] = 0.0
    constants[6] = 1.0
    constants[7] = 8.12E-2
    constants[8] = 0.61
    constants[9] = 0.61
    constants[10] = 0.61
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[0] = ((constants[0]/constants[1])*(states[1]-(states[0]*constants[5])/constants[4]))/(1.00000+states[1]/constants[1]+states[0]/constants[2]+constants[5]/constants[3])
    rates[1] = ((constants[7]/constants[8])*(constants[6]-states[1]/constants[10]))/(1.00000+constants[6]/constants[8]+states[1]/constants[9])
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
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
        self.V = 3.44E-3
        self.Kms = 0.49
        self.Kmp = 0.49
        self.Kmq = 0.49
        self.Keq = 0.49
        self.D_lactate = 0.0
        self.HTA = 1.0
        self.V_1 = 8.12E-2
        self.Kms_1 = 0.61
        self.Kmp_1 = 0.61
        self.Keq_1 = 0.61

    def to_dict(self):
        return {
            "V": self.V,
            "Kms": self.Kms,
            "Kmp": self.Kmp,
            "Kmq": self.Kmq,
            "Keq": self.Keq,
            "D_lactate": self.D_lactate,
            "HTA": self.HTA,
            "V_1": self.V_1,
            "Kms_1": self.Kms_1,
            "Kmp_1": self.Kmp_1,
            "Keq_1": self.Keq_1,
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
        y0=[1.0, 1.0],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "martins_mendes_coreiro_freire_2001"
        self.curve_names = [
            "GSH",
            "SDLGSH",
        ]
        self.state_names = ['GSH', 'SDLGSH']
        self.algebraic_names = []
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 11
        p = self.params

        # direct mapping
        c[0] = p.V
        c[1] = p.Kms
        c[2] = p.Kmp
        c[3] = p.Kmq
        c[4] = p.Keq
        c[5] = p.D_lactate
        c[6] = p.HTA
        c[7] = p.V_1
        c[8] = p.Kms_1
        c[9] = p.Kmp_1
        c[10] = p.Keq_1

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
