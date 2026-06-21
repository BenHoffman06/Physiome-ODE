# Size of variable arrays:
sizeAlgebraic = 4
sizeStates = 5
sizeConstants = 16
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (second)"
    legend_states[0] = "P in component P (picomolar)"
    legend_constants[0] = "k1 in component model_parameters (second_order_rate_constant)"
    legend_constants[1] = "k1_ in component model_parameters (first_order_rate_constant)"
    legend_constants[2] = "k2 in component model_parameters (second_order_rate_constant)"
    legend_constants[3] = "k2_ in component model_parameters (first_order_rate_constant)"
    legend_constants[4] = "kcl in component model_parameters (first_order_rate_constant)"
    legend_algebraic[3] = "D in component model_parameters (flux)"
    legend_states[1] = "Ca in component Ca (picomolar)"
    legend_states[2] = "Ci in component Ci (picomolar)"
    legend_states[3] = "Ra in component Ra (picomolar)"
    legend_states[4] = "Ri in component Ri (picomolar)"
    legend_constants[5] = "k3 in component model_parameters (first_order_rate_constant)"
    legend_constants[6] = "k3_ in component model_parameters (first_order_rate_constant)"
    legend_constants[7] = "k4 in component model_parameters (first_order_rate_constant)"
    legend_constants[8] = "k4_ in component model_parameters (first_order_rate_constant)"
    legend_algebraic[1] = "rho in component rho (dimensionless)"
    legend_constants[9] = "De in component model_parameters (flux)"
    legend_algebraic[2] = "Dd in component model_parameters (flux)"
    legend_constants[10] = "dmax in component model_parameters (flux)"
    legend_constants[11] = "dmin in component model_parameters (flux)"
    legend_constants[12] = "tau_on in component model_parameters (hour)"
    legend_constants[13] = "tau_off in component model_parameters (hour)"
    legend_constants[15] = "cycle_length in component model_parameters (hour)"
    legend_constants[14] = "j in component model_parameters (dimensionless)"
    legend_algebraic[0] = "time_hour in component model_parameters (hour)"
    legend_rates[0] = "d/dt P in component P (picomolar)"
    legend_rates[3] = "d/dt Ra in component Ra (picomolar)"
    legend_rates[4] = "d/dt Ri in component Ri (picomolar)"
    legend_rates[1] = "d/dt Ca in component Ca (picomolar)"
    legend_rates[2] = "d/dt Ci in component Ci (picomolar)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 3
    constants[0] = 1e-6
    constants[1] = 1e-3
    constants[2] = 1e-7
    constants[3] = 1e-3
    constants[4] = 5e-3
    states[1] = 4e-4
    states[2] = 0.05
    states[3] = 16.9
    states[4] = 1.7
    constants[5] = 1e-3
    constants[6] = 1e-4
    constants[7] = 2e-3
    constants[8] = 0.4
    constants[9] = 0
    constants[10] = 7.5
    constants[11] = 0
    constants[12] = 0.5
    constants[13] = 0.5
    constants[14] = 9
    constants[15] = constants[12]+constants[13]
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[3] = (constants[1]*states[1]+constants[5]*states[4])-(constants[0]*states[3]*states[0]+constants[6]*states[3])
    rates[4] = (constants[3]*states[2]+constants[6]*states[3])-(constants[2]*states[4]*states[0]+constants[5]*states[4])
    rates[1] = (constants[0]*states[3]*states[0]+constants[7]*states[2])-(constants[1]*states[1]+constants[8]*states[1])
    rates[2] = (constants[2]*states[4]*states[0]+constants[8]*states[1])-(constants[3]*states[2]+constants[7]*states[2])
    algebraic[0] = (voi*1.00000)/3600.00
    algebraic[2] = custom_piecewise([greater_equal(algebraic[0]/constants[15] , constants[14]), constants[11] , greater_equal(algebraic[0]-floor(algebraic[0]/constants[15])*constants[15] , 0.00000) & less(algebraic[0]-floor(algebraic[0]/constants[15])*constants[15] , constants[12]), constants[10] , greater_equal(algebraic[0]-floor(algebraic[0]/constants[15])*constants[15] , constants[12]) & less(algebraic[0]-floor(algebraic[0]/constants[15])*constants[15] , constants[15]), constants[11] , True, float('nan')])
    algebraic[3] = constants[9]+algebraic[2]
    rates[0] = (constants[1]*states[1]+constants[3]*states[2]+algebraic[3])-(constants[0]*states[3]*states[0]+constants[2]*states[4]*states[0]+constants[4]*states[0])
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = (voi*1.00000)/3600.00
    algebraic[2] = custom_piecewise([greater_equal(algebraic[0]/constants[15] , constants[14]), constants[11] , greater_equal(algebraic[0]-floor(algebraic[0]/constants[15])*constants[15] , 0.00000) & less(algebraic[0]-floor(algebraic[0]/constants[15])*constants[15] , constants[12]), constants[10] , greater_equal(algebraic[0]-floor(algebraic[0]/constants[15])*constants[15] , constants[12]) & less(algebraic[0]-floor(algebraic[0]/constants[15])*constants[15] , constants[15]), constants[11] , True, float('nan')])
    algebraic[3] = constants[9]+algebraic[2]
    algebraic[1] = (states[3]+states[1])/(states[3]+states[1]+states[4]+states[2])
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
        self.k1 = 1e-6
        self.k1_ = 1e-3
        self.k2 = 1e-7
        self.k2_ = 1e-3
        self.kcl = 5e-3
        self.k3 = 1e-3
        self.k3_ = 1e-4
        self.k4 = 2e-3
        self.k4_ = 0.4
        self.De = 0
        self.dmax = 7.5
        self.dmin = 0
        self.tau_on = 0.5
        self.tau_off = 0.5
        self.j = 9

    def to_dict(self):
        return {
            "k1": self.k1,
            "k1_": self.k1_,
            "k2": self.k2,
            "k2_": self.k2_,
            "kcl": self.kcl,
            "k3": self.k3,
            "k3_": self.k3_,
            "k4": self.k4,
            "k4_": self.k4_,
            "De": self.De,
            "dmax": self.dmax,
            "dmin": self.dmin,
            "tau_on": self.tau_on,
            "tau_off": self.tau_off,
            "j": self.j,
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
        y0=[3, 4e-4, 0.05, 16.9, 1.7],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "potter_greller_cho_nuttall_stroup_suva_tobin_2005_b"
        self.curve_names = [
            "P",
            "Ca",
            "Ci",
            "Ra",
            "Ri",
        ]
        self.state_names = ['P', 'Ca', 'Ci', 'Ra', 'Ri']
        self.algebraic_names = ['time_hour', 'rho', 'Dd', 'D']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 16
        p = self.params

        # direct mapping
        c[0] = p.k1
        c[1] = p.k1_
        c[2] = p.k2
        c[3] = p.k2_
        c[4] = p.kcl
        c[5] = p.k3
        c[6] = p.k3_
        c[7] = p.k4
        c[8] = p.k4_
        c[9] = p.De
        c[10] = p.dmax
        c[11] = p.dmin
        c[12] = p.tau_on
        c[13] = p.tau_off
        c[14] = p.j

        # derived constants
        c[15] = c[12]+c[13]

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
