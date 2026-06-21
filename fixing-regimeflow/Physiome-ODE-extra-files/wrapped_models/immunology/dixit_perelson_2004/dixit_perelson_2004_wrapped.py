# Size of variable arrays:
sizeAlgebraic = 3
sizeStates = 5
sizeConstants = 18
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (day)"
    legend_states[0] = "T in component T (per_ml)"
    legend_constants[0] = "lamda in component T (second_order_rate_constant)"
    legend_constants[1] = "d in component T (first_order_rate_constant)"
    legend_constants[2] = "k in component kinetic_parameters (flux)"
    legend_states[1] = "VI in component VI (per_ml)"
    legend_states[2] = "T_ in component T_ (per_ml)"
    legend_constants[3] = "tau in component T_ (first_order_rate_constant)"
    legend_constants[4] = "m in component T_ (first_order_rate_constant)"
    legend_constants[5] = "delta in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[6] = "N in component kinetic_parameters (dimensionless)"
    legend_constants[7] = "c in component kinetic_parameters (first_order_rate_constant)"
    legend_algebraic[0] = "epsilon_PI in component epsilon_PI (dimensionless)"
    legend_states[3] = "VNI in component VNI (per_ml)"
    legend_constants[8] = "IC50 in component epsilon_PI (mg_per_ml)"
    legend_states[4] = "Cc in component Cc (mg_per_ml)"
    legend_algebraic[1] = "Cb in component Cb (mg_per_ml)"
    legend_constants[9] = "Vd in component Cb (ml)"
    legend_constants[10] = "F in component Cb (dimensionless)"
    legend_constants[11] = "D in component Cb (mg)"
    legend_constants[12] = "ka in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[13] = "ke in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[14] = "kacell in component Cc (first_order_rate_constant)"
    legend_constants[15] = "kecell in component Cc (first_order_rate_constant)"
    legend_algebraic[2] = "Cx in component Cx (mg_per_ml)"
    legend_constants[16] = "H in component Cx (dimensionless)"
    legend_constants[17] = "fb in component Cx (dimensionless)"
    legend_rates[0] = "d/dt T in component T (per_ml)"
    legend_rates[2] = "d/dt T_ in component T_ (per_ml)"
    legend_rates[1] = "d/dt VI in component VI (per_ml)"
    legend_rates[3] = "d/dt VNI in component VNI (per_ml)"
    legend_rates[4] = "d/dt Cc in component Cc (mg_per_ml)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 1e6
    constants[0] = 1e4
    constants[1] = 0.01
    constants[2] = 2.4e-8
    states[1] = 1
    states[2] = 1
    constants[3] = 1.5
    constants[4] = 0.01
    constants[5] = 0.01
    constants[6] = 2500
    constants[7] = 23
    states[3] = 2
    constants[8] = 9e-7
    states[4] = 0
    constants[9] = 28000
    constants[10] = 1
    constants[11] = 600
    constants[12] = 14.64
    constants[13] = 6.86
    constants[14] = 24000
    constants[15] = 1.1
    constants[16] = 0.052
    constants[17] = 0.99
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[0] = constants[0]-(constants[1]*states[0]+constants[2]*states[0]*states[1])
    rates[2] = constants[2]*states[0]*(voi-constants[3])*states[1]*(voi-constants[3])*exp(-constants[4]*constants[3])-constants[5]*states[2]
    algebraic[0] = states[4]/(constants[8]+states[4])
    rates[1] = constants[6]*constants[5]*states[2]*(1.00000-algebraic[0])-constants[7]*states[1]
    rates[3] = constants[6]*constants[5]*states[2]*algebraic[0]-constants[7]*states[3]
    algebraic[1] = ((constants[10]*constants[11])/constants[9])*(constants[12]/(constants[13]-constants[12]))*(exp(-constants[12]*voi)-exp(-constants[13]*voi))
    algebraic[2] = custom_piecewise([greater((1.00000-constants[17])*constants[16]*algebraic[1]-states[4] , 0.00000), (1.00000-constants[17])*constants[16]*algebraic[1]-states[4] , True, 0.00000])
    rates[4] = constants[14]*algebraic[2]-constants[15]*states[4]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = states[4]/(constants[8]+states[4])
    algebraic[1] = ((constants[10]*constants[11])/constants[9])*(constants[12]/(constants[13]-constants[12]))*(exp(-constants[12]*voi)-exp(-constants[13]*voi))
    algebraic[2] = custom_piecewise([greater((1.00000-constants[17])*constants[16]*algebraic[1]-states[4] , 0.00000), (1.00000-constants[17])*constants[16]*algebraic[1]-states[4] , True, 0.00000])
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
        self.lamda = 1e4
        self.d = 0.01
        self.k = 2.4e-8
        self.tau = 1.5
        self.m = 0.01
        self.delta = 0.01
        self.N = 2500
        self.c = 23
        self.IC50 = 9e-7
        self.Vd = 28000
        self.F = 1
        self.D = 600
        self.ka = 14.64
        self.ke = 6.86
        self.kacell = 24000
        self.kecell = 1.1
        self.H = 0.052
        self.fb = 0.99

    def to_dict(self):
        return {
            "lamda": self.lamda,
            "d": self.d,
            "k": self.k,
            "tau": self.tau,
            "m": self.m,
            "delta": self.delta,
            "N": self.N,
            "c": self.c,
            "IC50": self.IC50,
            "Vd": self.Vd,
            "F": self.F,
            "D": self.D,
            "ka": self.ka,
            "ke": self.ke,
            "kacell": self.kacell,
            "kecell": self.kecell,
            "H": self.H,
            "fb": self.fb,
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
        y0=[1e6, 1, 1, 2, 0],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "dixit_perelson_2004"
        self.curve_names = [
            "T",
            "VI",
            "T_",
            "VNI",
            "Cc",
        ]
        self.state_names = ['T', 'VI', 'T_', 'VNI', 'Cc']
        self.algebraic_names = ['epsilon_PI', 'Cb', 'Cx']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 18
        p = self.params

        # direct mapping
        c[0] = p.lamda
        c[1] = p.d
        c[2] = p.k
        c[3] = p.tau
        c[4] = p.m
        c[5] = p.delta
        c[6] = p.N
        c[7] = p.c
        c[8] = p.IC50
        c[9] = p.Vd
        c[10] = p.F
        c[11] = p.D
        c[12] = p.ka
        c[13] = p.ke
        c[14] = p.kacell
        c[15] = p.kecell
        c[16] = p.H
        c[17] = p.fb

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
