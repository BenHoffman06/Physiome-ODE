# Size of variable arrays:
sizeAlgebraic = 9
sizeStates = 16
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
    legend_states[0] = "B0 in component B0 (cells_per_GC)"
    legend_constants[0] = "pr in component kinetic_parameters (dimensionless)"
    legend_constants[1] = "mu in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[2] = "rho in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[3] = "delta_B in component kinetic_parameters (first_order_rate_constant)"
    legend_algebraic[0] = "CT_star in component CT_star (cells_per_GC)"
    legend_states[1] = "B1 in component B1 (cells_per_GC)"
    legend_algebraic[4] = "alpha_B in component alpha_B (dimensionless)"
    legend_states[2] = "B2 in component B2 (cells_per_GC)"
    legend_states[3] = "B3 in component B3 (cells_per_GC)"
    legend_states[4] = "B4 in component B4 (cells_per_GC)"
    legend_states[5] = "B5 in component B5 (cells_per_GC)"
    legend_states[6] = "B6 in component B6 (cells_per_GC)"
    legend_states[7] = "B7 in component B7 (cells_per_GC)"
    legend_states[8] = "B8 in component B8 (cells_per_GC)"
    legend_states[9] = "B9 in component B9 (cells_per_GC)"
    legend_states[10] = "B10 in component B10 (cells_per_GC)"
    legend_algebraic[1] = "B_sum in component centroblasts_sum (cells_per_GC)"
    legend_states[11] = "C in component C (cells_per_GC)"
    legend_constants[4] = "d in component C (first_order_rate_constant)"
    legend_states[12] = "C_star in component C_star (cells_per_GC)"
    legend_algebraic[2] = "CA in component CA (cells_per_GC)"
    legend_algebraic[5] = "C_starsum in component centrocytes_sum (cells_per_GC)"
    legend_states[13] = "M in component M (cells_per_GC)"
    legend_states[14] = "A in component A (cells_per_GC)"
    legend_constants[5] = "z in component A (first_order_rate_constant)"
    legend_constants[6] = "u in component A (dimensionless)"
    legend_algebraic[3] = "log_A in component A (dimensionless)"
    legend_states[15] = "T in component T (cells_per_GC)"
    legend_constants[7] = "p in component T (first_order_rate_constant)"
    legend_constants[8] = "sigma in component T (first_order_rate_constant)"
    legend_constants[9] = "delta_T in component T (first_order_rate_constant)"
    legend_algebraic[6] = "alpha_T in component alpha_T (dimensionless)"
    legend_constants[10] = "SA in component CA (dimensionless)"
    legend_constants[11] = "ST in component CT_star (dimensionless)"
    legend_constants[12] = "KB in component alpha_B (dimensionless)"
    legend_constants[13] = "KT in component alpha_T (dimensionless)"
    legend_algebraic[7] = "total in component total (cells_per_GC)"
    legend_algebraic[8] = "log_total in component total (dimensionless)"
    legend_rates[0] = "d/dt B0 in component B0 (cells_per_GC)"
    legend_rates[1] = "d/dt B1 in component B1 (cells_per_GC)"
    legend_rates[2] = "d/dt B2 in component B2 (cells_per_GC)"
    legend_rates[3] = "d/dt B3 in component B3 (cells_per_GC)"
    legend_rates[4] = "d/dt B4 in component B4 (cells_per_GC)"
    legend_rates[5] = "d/dt B5 in component B5 (cells_per_GC)"
    legend_rates[6] = "d/dt B6 in component B6 (cells_per_GC)"
    legend_rates[7] = "d/dt B7 in component B7 (cells_per_GC)"
    legend_rates[8] = "d/dt B8 in component B8 (cells_per_GC)"
    legend_rates[9] = "d/dt B9 in component B9 (cells_per_GC)"
    legend_rates[10] = "d/dt B10 in component B10 (cells_per_GC)"
    legend_rates[11] = "d/dt C in component C (cells_per_GC)"
    legend_rates[12] = "d/dt C_star in component C_star (cells_per_GC)"
    legend_rates[13] = "d/dt M in component M (cells_per_GC)"
    legend_rates[14] = "d/dt A in component A (cells_per_GC)"
    legend_rates[15] = "d/dt T in component T (cells_per_GC)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 3
    constants[0] = 0.15
    constants[1] = 3
    constants[2] = 4
    constants[3] = 0.8
    states[1] = 0
    states[2] = 0
    states[3] = 0
    states[4] = 0
    states[5] = 0
    states[6] = 0
    states[7] = 0
    states[8] = 0
    states[9] = 0
    states[10] = 0
    states[11] = 0
    constants[4] = 2
    states[12] = 0
    states[13] = 0
    states[14] = 500
    constants[5] = 0.02
    constants[6] = 0.15
    states[15] = 0
    constants[7] = 2
    constants[8] = 5
    constants[9] = 0.8
    constants[10] = 500
    constants[11] = 50
    constants[12] = 1e4
    constants[13] = 100
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[11] = constants[4]*constants[2]*states[10]*1.00000-constants[1]*states[11]
    algebraic[0] = (states[12]*states[15])/(constants[11]*1.00000+states[12])
    rates[0] = constants[0]*constants[1]*algebraic[0]-(constants[2]*states[0]+constants[3]*states[0])
    algebraic[2] = (states[11]*states[14])/(constants[10]*1.00000+states[14])
    rates[12] = constants[1]*algebraic[2]-constants[1]*states[12]
    rates[13] = (1.00000-constants[0])*constants[1]*algebraic[0]
    rates[14] = -constants[5]*states[14]-constants[6]*algebraic[2]*1.00000
    algebraic[1] = states[1]+states[1]+states[3]+states[4]+states[5]+states[6]+states[6]+states[7]+states[8]+states[9]+states[10]
    algebraic[4] = constants[12]/(constants[12]+algebraic[1]/1.00000)
    rates[1] = constants[2]*(1.00000+algebraic[4])*states[0]-(constants[2]*states[1]+constants[3]*states[1])
    rates[2] = constants[2]*(1.00000+algebraic[4])*states[1]-(constants[2]*states[2]+constants[3]*states[2])
    rates[3] = constants[2]*(1.00000+algebraic[4])*states[2]-(constants[2]*states[3]+constants[3]*states[3])
    rates[4] = constants[2]*(1.00000+algebraic[4])*states[3]-(constants[2]*states[4]+constants[3]*states[4])
    rates[5] = constants[2]*(1.00000+algebraic[4])*states[4]-(constants[2]*states[5]+constants[3]*states[5])
    rates[6] = constants[2]*(1.00000+algebraic[4])*states[5]-(constants[2]*states[6]+constants[3]*states[6])
    rates[7] = constants[2]*(1.00000+algebraic[4])*states[6]-(constants[2]*states[7]+constants[3]*states[7])
    rates[8] = constants[2]*(1.00000+algebraic[4])*states[7]-(constants[2]*states[8]+constants[3]*states[8])
    rates[9] = constants[2]*(1.00000+algebraic[4])*states[8]-(constants[2]*states[9]+constants[3]*states[9])
    rates[10] = constants[2]*(1.00000+algebraic[4])*states[9]-(constants[2]*states[10]+constants[3]*states[10])
    algebraic[6] = constants[13]/(constants[13]+states[15]/1.00000)
    rates[15] = (constants[8]*1.00000+constants[7]*algebraic[6]*algebraic[0])-constants[9]*states[15]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = (states[12]*states[15])/(constants[11]*1.00000+states[12])
    algebraic[2] = (states[11]*states[14])/(constants[10]*1.00000+states[14])
    algebraic[1] = states[1]+states[1]+states[3]+states[4]+states[5]+states[6]+states[6]+states[7]+states[8]+states[9]+states[10]
    algebraic[4] = constants[12]/(constants[12]+algebraic[1]/1.00000)
    algebraic[6] = constants[13]/(constants[13]+states[15]/1.00000)
    algebraic[3] = log(states[14]/1.00000, 10)
    algebraic[5] = states[11]+states[12]
    algebraic[7] = algebraic[1]+algebraic[5]
    algebraic[8] = log(algebraic[7]/1.00000+1.00000e-12, 10)
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
        self.pr = 0.15
        self.mu = 3
        self.rho = 4
        self.delta_B = 0.8
        self.d = 2
        self.z = 0.02
        self.u = 0.15
        self.p = 2
        self.sigma = 5
        self.delta_T = 0.8
        self.SA = 500
        self.ST = 50
        self.KB = 1e4
        self.KT = 100

    def to_dict(self):
        return {
            "pr": self.pr,
            "mu": self.mu,
            "rho": self.rho,
            "delta_B": self.delta_B,
            "d": self.d,
            "z": self.z,
            "u": self.u,
            "p": self.p,
            "sigma": self.sigma,
            "delta_T": self.delta_T,
            "SA": self.SA,
            "ST": self.ST,
            "KB": self.KB,
            "KT": self.KT,
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
        y0=[3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 500, 0],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "kesmir_deboer_1999"
        self.curve_names = [
            "B0",
            "B1",
            "B2",
            "B3",
            "B4",
            "B5",
            "B6",
            "B7",
            "B8",
            "B9",
            "B10",
            "C",
            "C_star",
            "M",
            "A",
            "T",
        ]
        self.state_names = ['B0', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'C', 'C_star', 'M', 'A', 'T']
        self.algebraic_names = ['CT_star', 'B_sum', 'CA', 'log_A', 'alpha_B', 'C_starsum', 'alpha_T', 'total', 'log_total']
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
        c[0] = p.pr
        c[1] = p.mu
        c[2] = p.rho
        c[3] = p.delta_B
        c[4] = p.d
        c[5] = p.z
        c[6] = p.u
        c[7] = p.p
        c[8] = p.sigma
        c[9] = p.delta_T
        c[10] = p.SA
        c[11] = p.ST
        c[12] = p.KB
        c[13] = p.KT

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
