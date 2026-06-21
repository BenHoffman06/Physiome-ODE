# Size of variable arrays:
sizeAlgebraic = 13
sizeStates = 7
sizeConstants = 41
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (millisecond)"
    legend_constants[40] = "F_SE in component F_SE (newton)"
    legend_constants[0] = "cT in component F_SE (dimensionless)"
    legend_constants[1] = "kT in component F_SE (dimensionless)"
    legend_constants[2] = "LT_r in component F_SE (dimensionless)"
    legend_constants[3] = "LT in component user_defined_constants (dimensionless)"
    legend_constants[4] = "F_max in component user_defined_constants (newton)"
    legend_algebraic[1] = "F_PE1 in component F_PE1 (dimensionless)"
    legend_constants[5] = "c1 in component F_PE1 (dimensionless)"
    legend_constants[6] = "k1 in component F_PE1 (dimensionless)"
    legend_constants[7] = "L_r1 in component F_PE1 (dimensionless)"
    legend_constants[8] = "eta in component F_PE1 (millisecond)"
    legend_states[0] = "L in component L (dimensionless)"
    legend_constants[9] = "L_max in component user_defined_constants (dimensionless)"
    legend_states[1] = "V in component V (first_order_rate_constant)"
    legend_algebraic[4] = "F_PE2 in component F_PE2 (dimensionless)"
    legend_constants[10] = "c2 in component F_PE2 (dimensionless)"
    legend_constants[11] = "k2 in component F_PE2 (dimensionless)"
    legend_constants[12] = "L_r2 in component F_PE2 (dimensionless)"
    legend_algebraic[5] = "FL in component FL (dimensionless)"
    legend_constants[13] = "beta in component FL (dimensionless)"
    legend_constants[14] = "omega in component FL (dimensionless)"
    legend_constants[15] = "rho in component FL (dimensionless)"
    legend_algebraic[6] = "FV in component FV (dimensionless)"
    legend_constants[16] = "av0 in component FV (dimensionless)"
    legend_constants[17] = "av1 in component FV (dimensionless)"
    legend_constants[18] = "av2 in component FV (dimensionless)"
    legend_constants[19] = "cv0 in component FV (dimensionless)"
    legend_constants[20] = "cv1 in component FV (dimensionless)"
    legend_constants[21] = "bv in component FV (first_order_rate_constant)"
    legend_constants[22] = "V_max in component FV (first_order_rate_constant)"
    legend_algebraic[7] = "Af in component Af (dimensionless)"
    legend_constants[23] = "af in component Af (dimensionless)"
    legend_constants[24] = "nf0 in component Af (dimensionless)"
    legend_constants[25] = "nf1 in component Af (dimensionless)"
    legend_constants[26] = "nf in component Af (dimensionless)"
    legend_states[2] = "Y in component Y (dimensionless)"
    legend_states[3] = "S in component S (dimensionless)"
    legend_states[4] = "f_eff in component rise_and_fall_time (dimensionless)"
    legend_states[5] = "L_eff in component L_eff (dimensionless)"
    legend_algebraic[8] = "F0 in component F0 (dimensionless)"
    legend_algebraic[11] = "F_CE in component F_CE (newton)"
    legend_algebraic[12] = "F_total in component F_total (newton)"
    legend_constants[27] = "T_L in component L_eff (millisecond)"
    legend_constants[28] = "T_s in component S (millisecond)"
    legend_constants[29] = "as1 in component S (dimensionless)"
    legend_constants[30] = "as2 in component S (dimensionless)"
    legend_algebraic[0] = "as_ in component S (dimensionless)"
    legend_constants[31] = "c_Y in component Y (dimensionless)"
    legend_constants[32] = "V_Y in component Y (first_order_rate_constant)"
    legend_constants[33] = "T_Y in component Y (millisecond)"
    legend_states[6] = "f_int in component rise_and_fall_time (dimensionless)"
    legend_algebraic[9] = "df_eff_dt in component rise_and_fall_time (first_order_rate_constant)"
    legend_algebraic[10] = "T_f in component rise_and_fall_time (millisecond)"
    legend_constants[34] = "T_f1 in component rise_and_fall_time (millisecond)"
    legend_constants[35] = "T_f2 in component rise_and_fall_time (millisecond)"
    legend_constants[36] = "T_f3 in component rise_and_fall_time (millisecond)"
    legend_constants[37] = "T_f4 in component rise_and_fall_time (millisecond)"
    legend_constants[38] = "f_env in component user_defined_constants (dimensionless)"
    legend_constants[39] = "mass in component V (kilogram)"
    legend_algebraic[2] = "V0 in component V0 (first_order_rate_constant)"
    legend_algebraic[3] = "L0 in component L0 (dimensionless)"
    legend_rates[5] = "d/dt L_eff in component L_eff (dimensionless)"
    legend_rates[3] = "d/dt S in component S (dimensionless)"
    legend_rates[2] = "d/dt Y in component Y (dimensionless)"
    legend_rates[6] = "d/dt f_int in component rise_and_fall_time (dimensionless)"
    legend_rates[4] = "d/dt f_eff in component rise_and_fall_time (dimensionless)"
    legend_rates[1] = "d/dt V in component V (first_order_rate_constant)"
    legend_rates[0] = "d/dt L in component L (dimensionless)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    constants[0] = 27.8
    constants[1] = 0.0047
    constants[2] = 0.964
    constants[3] = 0.02
    constants[4] = 23
    constants[5] = 23
    constants[6] = 0.046
    constants[7] = 1.17
    constants[8] = 0.001
    states[0] = 0.15
    constants[9] = 0.13
    states[1] = 0.09314
    constants[10] = 23
    constants[11] = 0.046
    constants[12] = 1.17
    constants[13] = 1.55
    constants[14] = 0.75
    constants[15] = 2.12
    constants[16] = -1.53
    constants[17] = 0
    constants[18] = 0
    constants[19] = -5.7
    constants[20] = 9.18
    constants[21] = 0.69
    constants[22] = -9.15
    constants[23] = 0.56
    constants[24] = 2.1
    constants[25] = 3.3
    constants[26] = 1
    states[2] = 1
    states[3] = 1
    states[4] = 0
    states[5] = 0.1497
    constants[27] = 0.088
    constants[28] = 43
    constants[29] = 1.76
    constants[30] = 0.96
    constants[31] = 0.35
    constants[32] = 0.1
    constants[33] = 200
    states[6] = 0
    constants[34] = 0.35
    constants[35] = 0.1
    constants[36] = 200
    constants[37] = 200
    constants[38] = 1
    constants[39] = 0.005
    constants[40] = constants[0]*constants[4]*constants[1]*log(exp((constants[3]-constants[2])/constants[1])+1.00000)
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[2] = (1.00000-(constants[31]*(1.00000-exp(-fabs(states[1])/constants[32]))+states[2]))/constants[33]
    rates[0] = states[1]
    algebraic[0] = custom_piecewise([less(states[4] , 0.100000), constants[29] , True, constants[30]])
    rates[3] = (algebraic[0]-states[3])/constants[28]
    algebraic[7] = 1.00000-exp(-(power((states[2]*states[3]*states[4])/(constants[23]*constants[26]), constants[26])))
    rates[5] = (power(states[0]-states[5], 3.00000))/(constants[27]*(1.00000-algebraic[7]))
    rootfind_0(voi, constants, rates, states, algebraic)
    rates[6] = (constants[38]-states[6])/algebraic[10]
    rates[4] = algebraic[9]
    algebraic[1] = constants[5]*constants[6]*log(exp((states[0]/constants[9]-constants[7])/constants[6])+1.00000)+constants[8]*states[1]
    algebraic[4] = constants[10]*(exp(constants[11]*(states[0]-constants[12]))-1.00000)
    algebraic[5] = exp(-(power(fabs((power(states[0], constants[13])-1.00000)/constants[14]), constants[15])))
    algebraic[6] = custom_piecewise([less_equal(states[1] , 0.00000), (constants[22]-states[1])/(constants[22]+(constants[19]+constants[20]*states[0])*states[1]) , True, (constants[21]-(constants[16]+constants[17]*states[0]+constants[18]*(power(states[0], 2.00000)))*states[1])/(constants[21]+states[1])])
    algebraic[8] = algebraic[7]*(algebraic[5]+algebraic[6]+algebraic[4])+algebraic[1]
    algebraic[11] = algebraic[8]*constants[4]
    algebraic[12] = constants[40]-algebraic[11]
    rates[1] = algebraic[12]/(1.00000*constants[39])
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = custom_piecewise([less(states[4] , 0.100000), constants[29] , True, constants[30]])
    algebraic[7] = 1.00000-exp(-(power((states[2]*states[3]*states[4])/(constants[23]*constants[26]), constants[26])))
    algebraic[1] = constants[5]*constants[6]*log(exp((states[0]/constants[9]-constants[7])/constants[6])+1.00000)+constants[8]*states[1]
    algebraic[4] = constants[10]*(exp(constants[11]*(states[0]-constants[12]))-1.00000)
    algebraic[5] = exp(-(power(fabs((power(states[0], constants[13])-1.00000)/constants[14]), constants[15])))
    algebraic[6] = custom_piecewise([less_equal(states[1] , 0.00000), (constants[22]-states[1])/(constants[22]+(constants[19]+constants[20]*states[0])*states[1]) , True, (constants[21]-(constants[16]+constants[17]*states[0]+constants[18]*(power(states[0], 2.00000)))*states[1])/(constants[21]+states[1])])
    algebraic[8] = algebraic[7]*(algebraic[5]+algebraic[6]+algebraic[4])+algebraic[1]
    algebraic[11] = algebraic[8]*constants[4]
    algebraic[12] = constants[40]-algebraic[11]
    algebraic[2] = states[1]/constants[9]
    algebraic[3] = states[0]/constants[9]
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
        algebraic[9] = soln[0]
        algebraic[10] = soln[1]
    else:
        for (i,t) in enumerate(voi):
            soln = fsolve(residualSN_0, initialGuess0, args=(algebraic[:,i], voi[i], constants, rates[:i], states[:,i]), xtol=1E-6)
            initialGuess0 = soln
            algebraic[9][i] = soln[0]
            algebraic[10][i] = soln[1]

def residualSN_0(algebraicCandidate, algebraic, voi, constants, rates, states):
    resid = array([0.0] * 2)
    algebraic[9] = algebraicCandidate[0]
    algebraic[10] = algebraicCandidate[1]
    resid[0] = (algebraic[9]-(states[6]-states[4])/algebraic[10])
    resid[1] = (algebraic[10]-(custom_piecewise([greater_equal(algebraic[9] , 0.00000), constants[34]*(power(states[0], 2.00000))+constants[35]*constants[38] , True, (constants[36]+constants[37]*algebraic[7])/states[0]])))
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
        self.cT = 27.8
        self.kT = 0.0047
        self.LT_r = 0.964
        self.LT = 0.02
        self.F_max = 23
        self.c1 = 23
        self.k1 = 0.046
        self.L_r1 = 1.17
        self.eta = 0.001
        self.L_max = 0.13
        self.c2 = 23
        self.k2 = 0.046
        self.L_r2 = 1.17
        self.beta = 1.55
        self.omega = 0.75
        self.rho = 2.12
        self.av0 = -1.53
        self.av1 = 0
        self.av2 = 0
        self.cv0 = -5.7
        self.cv1 = 9.18
        self.bv = 0.69
        self.V_max = -9.15
        self.af = 0.56
        self.nf0 = 2.1
        self.nf1 = 3.3
        self.nf = 1
        self.T_L = 0.088
        self.T_s = 43
        self.as1 = 1.76
        self.as2 = 0.96
        self.c_Y = 0.35
        self.V_Y = 0.1
        self.T_Y = 200
        self.T_f1 = 0.35
        self.T_f2 = 0.1
        self.T_f3 = 200
        self.T_f4 = 200
        self.f_env = 1
        self.mass = 0.005

    def to_dict(self):
        return {
            "cT": self.cT,
            "kT": self.kT,
            "LT_r": self.LT_r,
            "LT": self.LT,
            "F_max": self.F_max,
            "c1": self.c1,
            "k1": self.k1,
            "L_r1": self.L_r1,
            "eta": self.eta,
            "L_max": self.L_max,
            "c2": self.c2,
            "k2": self.k2,
            "L_r2": self.L_r2,
            "beta": self.beta,
            "omega": self.omega,
            "rho": self.rho,
            "av0": self.av0,
            "av1": self.av1,
            "av2": self.av2,
            "cv0": self.cv0,
            "cv1": self.cv1,
            "bv": self.bv,
            "V_max": self.V_max,
            "af": self.af,
            "nf0": self.nf0,
            "nf1": self.nf1,
            "nf": self.nf,
            "T_L": self.T_L,
            "T_s": self.T_s,
            "as1": self.as1,
            "as2": self.as2,
            "c_Y": self.c_Y,
            "V_Y": self.V_Y,
            "T_Y": self.T_Y,
            "T_f1": self.T_f1,
            "T_f2": self.T_f2,
            "T_f3": self.T_f3,
            "T_f4": self.T_f4,
            "f_env": self.f_env,
            "mass": self.mass,
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
        y0=[0.15, 0.09314, 1, 1, 0, 0.1497, 0],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "cheng_brown_loeb_2000"
        self.curve_names = [
            "L",
            "V",
            "Y",
            "S",
            "f_eff",
            "L_eff",
            "f_int",
        ]
        self.state_names = ['L', 'V', 'Y', 'S', 'f_eff', 'L_eff', 'f_int']
        self.algebraic_names = ['as_', 'F_PE1', 'V0', 'L0', 'F_PE2', 'FL', 'FV', 'Af', 'F0', 'df_eff_dt', 'T_f', 'F_CE', 'F_total']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 41
        p = self.params

        # direct mapping
        c[0] = p.cT
        c[1] = p.kT
        c[2] = p.LT_r
        c[3] = p.LT
        c[4] = p.F_max
        c[5] = p.c1
        c[6] = p.k1
        c[7] = p.L_r1
        c[8] = p.eta
        c[9] = p.L_max
        c[10] = p.c2
        c[11] = p.k2
        c[12] = p.L_r2
        c[13] = p.beta
        c[14] = p.omega
        c[15] = p.rho
        c[16] = p.av0
        c[17] = p.av1
        c[18] = p.av2
        c[19] = p.cv0
        c[20] = p.cv1
        c[21] = p.bv
        c[22] = p.V_max
        c[23] = p.af
        c[24] = p.nf0
        c[25] = p.nf1
        c[26] = p.nf
        c[27] = p.T_L
        c[28] = p.T_s
        c[29] = p.as1
        c[30] = p.as2
        c[31] = p.c_Y
        c[32] = p.V_Y
        c[33] = p.T_Y
        c[34] = p.T_f1
        c[35] = p.T_f2
        c[36] = p.T_f3
        c[37] = p.T_f4
        c[38] = p.f_env
        c[39] = p.mass

        # derived constants
        c[40] = c[0]*c[4]*c[1]*log(exp((c[3]-c[2])/c[1])+1.00000)

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
