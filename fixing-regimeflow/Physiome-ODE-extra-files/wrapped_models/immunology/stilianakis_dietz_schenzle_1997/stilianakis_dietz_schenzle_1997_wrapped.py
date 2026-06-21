# Size of variable arrays:
sizeAlgebraic = 3
sizeStates = 5
sizeConstants = 14
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (day)"
    legend_states[0] = "X in component X (dimensionless)"
    legend_constants[0] = "mu0 in component X (first_order_rate_constant)"
    legend_constants[1] = "lamda in component X (first_order_rate_constant)"
    legend_states[1] = "K in component K (first_order_rate_constant)"
    legend_states[2] = "V in component V (dimensionless)"
    legend_states[3] = "Y in component Y (dimensionless)"
    legend_constants[2] = "mu1 in component Y (first_order_rate_constant)"
    legend_constants[3] = "a in component Y (dimensionless)"
    legend_states[4] = "Z in component Z (dimensionless)"
    legend_algebraic[0] = "CD4 in component CD4 (dimensionless)"
    legend_constants[4] = "mu2 in component V (first_order_rate_constant)"
    legend_constants[5] = "beta in component V (first_order_rate_constant)"
    legend_constants[6] = "b in component V (dimensionless)"
    legend_constants[7] = "theta in component Z (first_order_rate_constant)"
    legend_constants[8] = "rho in component Z (first_order_rate_constant)"
    legend_algebraic[1] = "f_X in component Z (dimensionless)"
    legend_algebraic[2] = "g_V in component Z (dimensionless)"
    legend_constants[9] = "C1 in component Z (dimensionless)"
    legend_constants[10] = "C2 in component Z (dimensionless)"
    legend_constants[11] = "X0 in component Z (dimensionless)"
    legend_constants[12] = "omega in component K (first_order_rate_constant)"
    legend_constants[13] = "Kmax in component K (first_order_rate_constant)"
    legend_rates[0] = "d/dt X in component X (dimensionless)"
    legend_rates[3] = "d/dt Y in component Y (dimensionless)"
    legend_rates[2] = "d/dt V in component V (dimensionless)"
    legend_rates[4] = "d/dt Z in component Z (dimensionless)"
    legend_rates[1] = "d/dt K in component K (first_order_rate_constant)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 1.0E11
    constants[0] = 4.0E-3
    constants[1] = 4.0E8
    states[1] = 1.35E-14
    states[2] = 1.0
    states[3] = 1.0
    constants[2] = 0.30
    constants[3] = 1.0
    states[4] = 0.0
    constants[4] = 1.0
    constants[5] = 1.0E3
    constants[6] = 1.0
    constants[7] = 1.0E-6
    constants[8] = 0.50
    constants[9] = 0.04
    constants[10] = 1.0E3
    constants[11] = 1.0E11
    constants[12] = 1.0E-16
    constants[13] = 20.0
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[0] = constants[1]-(constants[0]*states[0]+states[1]*states[2]*states[0])
    rates[3] = states[1]*states[2]*states[3]-constants[2]*(1.00000+constants[3]*states[4])*states[3]
    rates[2] = constants[5]*states[3]-constants[4]*(1.00000+constants[6]*states[4])*states[2]
    rates[1] = constants[12]*states[2]*(constants[13]-states[1])
    algebraic[1] = ((1.00000+constants[9])*(power(states[0]/constants[11], 2.00000)))/(constants[9]+power(states[0]/constants[11], 2.00000))
    algebraic[2] = states[2]/(constants[10]+states[2])
    rates[4] = constants[7]*algebraic[2]+constants[8]*(algebraic[1]-states[4])*states[4]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[1] = ((1.00000+constants[9])*(power(states[0]/constants[11], 2.00000)))/(constants[9]+power(states[0]/constants[11], 2.00000))
    algebraic[2] = states[2]/(constants[10]+states[2])
    algebraic[0] = (states[0]+states[3])/1.00000e+11
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
        self.mu0 = 4.0E-3
        self.lamda = 4.0E8
        self.mu1 = 0.30
        self.a = 1.0
        self.mu2 = 1.0
        self.beta = 1.0E3
        self.b = 1.0
        self.theta = 1.0E-6
        self.rho = 0.50
        self.C1 = 0.04
        self.C2 = 1.0E3
        self.X0 = 1.0E11
        self.omega = 1.0E-16
        self.Kmax = 20.0

    def to_dict(self):
        return {
            "mu0": self.mu0,
            "lamda": self.lamda,
            "mu1": self.mu1,
            "a": self.a,
            "mu2": self.mu2,
            "beta": self.beta,
            "b": self.b,
            "theta": self.theta,
            "rho": self.rho,
            "C1": self.C1,
            "C2": self.C2,
            "X0": self.X0,
            "omega": self.omega,
            "Kmax": self.Kmax,
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
        y0=[1.0E11, 1.35E-14, 1.0, 1.0, 0.0],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "stilianakis_dietz_schenzle_1997"
        self.curve_names = [
            "X",
            "K",
            "V",
            "Y",
            "Z",
        ]
        self.state_names = ['X', 'K', 'V', 'Y', 'Z']
        self.algebraic_names = ['CD4', 'f_X', 'g_V']
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
        c[0] = p.mu0
        c[1] = p.lamda
        c[2] = p.mu1
        c[3] = p.a
        c[4] = p.mu2
        c[5] = p.beta
        c[6] = p.b
        c[7] = p.theta
        c[8] = p.rho
        c[9] = p.C1
        c[10] = p.C2
        c[11] = p.X0
        c[12] = p.omega
        c[13] = p.Kmax

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
