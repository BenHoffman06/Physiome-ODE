# Size of variable arrays:
sizeAlgebraic = 7
sizeStates = 1
sizeConstants = 19
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (second)"
    legend_constants[0] = "L_1 in component contraction (mm)"
    legend_constants[1] = "L_2 in component contraction (mm)"
    legend_constants[2] = "L_3 in component contraction (mm)"
    legend_constants[3] = "L_4 in component contraction (mm)"
    legend_constants[4] = "f_c in component contraction (newton)"
    legend_constants[5] = "v_max in component contraction (mm_per_second)"
    legend_constants[6] = "curv in component contraction (dimensionless)"
    legend_constants[7] = "k_1 in component contraction (newton)"
    legend_constants[8] = "k_2 in component contraction (per_mm)"
    legend_constants[9] = "F_1 in component contraction (newton)"
    legend_constants[10] = "d_LSEC1 in component contraction (mm)"
    legend_constants[11] = "k_sh in component contraction (dimensionless)"
    legend_constants[12] = "L_m in component contraction (mm)"
    legend_constants[13] = "F_im in component contraction (newton)"
    legend_constants[14] = "tau in component contraction (second)"
    legend_algebraic[5] = "v_cc in component contraction (mm_per_second)"
    legend_algebraic[6] = "f_v in component contraction (dimensionless)"
    legend_algebraic[1] = "f_L in component contraction (newton)"
    legend_algebraic[4] = "f_sec in component contraction (newton)"
    legend_algebraic[0] = "f_pec in component contraction (newton)"
    legend_algebraic[3] = "delta_L_sec in component contraction (mm)"
    legend_constants[15] = "delta_L_sec1 in component contraction (mm)"
    legend_states[0] = "delta_L_pec in component contraction (mm)"
    legend_constants[16] = "k in component contraction (newton_per_mm)"
    legend_algebraic[2] = "L_mtc in component contraction (mm)"
    legend_constants[17] = "A in component contraction (dimensionless)"
    legend_constants[18] = "L_mslack in component contraction (mm)"
    legend_rates[0] = "d/dt delta_L_pec in component contraction (mm)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    constants[0] = -23
    constants[1] = -14
    constants[2] = 2
    constants[3] = 19
    constants[4] = 0.49
    constants[5] = -141
    constants[6] = 5.8
    constants[7] = 0.012
    constants[8] = 0.317
    constants[9] = 4.1
    constants[10] = 4.1
    constants[11] = 3.3
    constants[12] = 0.3
    constants[13] = 18.1
    constants[14] = 0.006
    constants[15] = 4.1
    states[0] = 0.2
    constants[16] = 3.5
    constants[17] = 1
    constants[18] = 0.3
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[1] = custom_piecewise([greater_equal(states[0] , constants[0]) & less_equal(states[0] , constants[1]), (constants[4]/(constants[1]-constants[0]))*(states[0]-constants[0]) , greater(states[0] , constants[1]) & less_equal(states[0] , 0.00000), ((1.00000-constants[4])/-constants[1])*(states[0]-constants[1]) , greater(states[0] , 0.00000) & less_equal(states[0] , constants[2]), 1.00000 , greater(states[0] , constants[2]) & less_equal(states[0] , constants[3]), (-1.00000/(constants[3]-constants[2]))*(states[0]-constants[2]) , True, float('nan')])
    algebraic[2] = custom_piecewise([less_equal(voi , 1.00000), 0.290000 , greater(voi , 1.00000) & less(voi , 5.00000), 0.220000 , True, 0.190000])
    algebraic[3] = (algebraic[2]-states[0])-constants[18]
    algebraic[4] = custom_piecewise([greater(algebraic[3] , 0.00000) & less(algebraic[3] , constants[15]), (constants[9]/(exp(constants[11])-1.00000))*(exp((constants[11]*algebraic[3])/constants[15])-1.00000) , less_equal(algebraic[3] , constants[15]), constants[9]+constants[16]*(algebraic[3]-constants[15]) , True, float('nan')])
    algebraic[0] = custom_piecewise([greater(states[0] , 0.00000), constants[7]*(exp(constants[8]*states[0])-1.00000) , less_equal(states[0] , 0.00000), 0.00000 , True, float('nan')])
    rootfind_0(voi, constants, rates, states, algebraic)
    rates[0] = algebraic[5]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[1] = custom_piecewise([greater_equal(states[0] , constants[0]) & less_equal(states[0] , constants[1]), (constants[4]/(constants[1]-constants[0]))*(states[0]-constants[0]) , greater(states[0] , constants[1]) & less_equal(states[0] , 0.00000), ((1.00000-constants[4])/-constants[1])*(states[0]-constants[1]) , greater(states[0] , 0.00000) & less_equal(states[0] , constants[2]), 1.00000 , greater(states[0] , constants[2]) & less_equal(states[0] , constants[3]), (-1.00000/(constants[3]-constants[2]))*(states[0]-constants[2]) , True, float('nan')])
    algebraic[2] = custom_piecewise([less_equal(voi , 1.00000), 0.290000 , greater(voi , 1.00000) & less(voi , 5.00000), 0.220000 , True, 0.190000])
    algebraic[3] = (algebraic[2]-states[0])-constants[18]
    algebraic[4] = custom_piecewise([greater(algebraic[3] , 0.00000) & less(algebraic[3] , constants[15]), (constants[9]/(exp(constants[11])-1.00000))*(exp((constants[11]*algebraic[3])/constants[15])-1.00000) , less_equal(algebraic[3] , constants[15]), constants[9]+constants[16]*(algebraic[3]-constants[15]) , True, float('nan')])
    algebraic[0] = custom_piecewise([greater(states[0] , 0.00000), constants[7]*(exp(constants[8]*states[0])-1.00000) , less_equal(states[0] , 0.00000), 0.00000 , True, float('nan')])
    return algebraic

initialGuess0 = None
def rootfind_0(voi, constants, rates, states, algebraic):
    """Calculate values of algebraic variables for DAE"""
    from scipy.optimize import fsolve
    global initialGuess0
    if initialGuess0 is None: initialGuess0 = ones(2)*0.1
    if not iterable(voi):
        soln = fsolve(residualSN_0, initialGuess0, args=(algebraic, voi, constants, rates, states), xtol=1E-6)
        initialGuess0 = soln
        algebraic[5] = soln[0]
        algebraic[6] = soln[1]
    else:
        for (i,t) in enumerate(voi):
            soln = fsolve(residualSN_0, initialGuess0, args=(algebraic[:,i], voi[i], constants, rates[:i], states[:,i]), xtol=1E-6)
            initialGuess0 = soln
            algebraic[5][i] = soln[0]
            algebraic[6][i] = soln[1]

def residualSN_0(algebraicCandidate, algebraic, voi, constants, rates, states):
    resid = array([0.0] * 2)
    algebraic[5] = algebraicCandidate[0]
    algebraic[6] = algebraicCandidate[1]
    resid[0] = (algebraic[5]-(1.00000/algebraic[6])*((algebraic[4]-algebraic[0])/(constants[17]*algebraic[1]*constants[13])))
    resid[1] = (algebraic[6]-(constants[5]-algebraic[5])/(constants[5]+algebraic[5]*constants[6]))
    return resid

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
        self.L_1 = -23
        self.L_2 = -14
        self.L_3 = 2
        self.L_4 = 19
        self.f_c = 0.49
        self.v_max = -141
        self.curv = 5.8
        self.k_1 = 0.012
        self.k_2 = 0.317
        self.F_1 = 4.1
        self.d_LSEC1 = 4.1
        self.k_sh = 3.3
        self.L_m = 0.3
        self.F_im = 18.1
        self.tau = 0.006
        self.delta_L_sec1 = 4.1
        self.k = 3.5
        self.A = 1
        self.L_mslack = 0.3

    def to_dict(self):
        return {
            "L_1": self.L_1,
            "L_2": self.L_2,
            "L_3": self.L_3,
            "L_4": self.L_4,
            "f_c": self.f_c,
            "v_max": self.v_max,
            "curv": self.curv,
            "k_1": self.k_1,
            "k_2": self.k_2,
            "F_1": self.F_1,
            "d_LSEC1": self.d_LSEC1,
            "k_sh": self.k_sh,
            "L_m": self.L_m,
            "F_im": self.F_im,
            "tau": self.tau,
            "delta_L_sec1": self.delta_L_sec1,
            "k": self.k,
            "A": self.A,
            "L_mslack": self.L_mslack,
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
        y0=[0.2],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "siebert_CC_SEC_2008"
        self.curve_names = [
            "delta_L_pec",
        ]
        self.state_names = ['delta_L_pec']
        self.algebraic_names = ['f_pec', 'f_L', 'L_mtc', 'delta_L_sec', 'f_sec', 'v_cc', 'f_v']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 19
        p = self.params

        # direct mapping
        c[0] = p.L_1
        c[1] = p.L_2
        c[2] = p.L_3
        c[3] = p.L_4
        c[4] = p.f_c
        c[5] = p.v_max
        c[6] = p.curv
        c[7] = p.k_1
        c[8] = p.k_2
        c[9] = p.F_1
        c[10] = p.d_LSEC1
        c[11] = p.k_sh
        c[12] = p.L_m
        c[13] = p.F_im
        c[14] = p.tau
        c[15] = p.delta_L_sec1
        c[16] = p.k
        c[17] = p.A
        c[18] = p.L_mslack

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
