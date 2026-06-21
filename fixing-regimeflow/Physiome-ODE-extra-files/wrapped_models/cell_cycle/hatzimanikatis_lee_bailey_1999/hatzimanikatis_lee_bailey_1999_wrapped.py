# Size of variable arrays:
sizeAlgebraic = 12
sizeStates = 3
sizeConstants = 19
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (dimensionless)"
    legend_states[0] = "C in component C (dimensionless)"
    legend_constants[0] = "gamma in component C (dimensionless)"
    legend_algebraic[5] = "Vs in component Vs (dimensionless)"
    legend_algebraic[0] = "V1 in component V1 (dimensionless)"
    legend_algebraic[10] = "V2 in component V2 (dimensionless)"
    legend_algebraic[6] = "Vd in component Vd (dimensionless)"
    legend_states[1] = "K in component K (dimensionless)"
    legend_states[2] = "RP in component RP (dimensionless)"
    legend_algebraic[11] = "V3 in component V3 (dimensionless)"
    legend_algebraic[1] = "V4 in component V4 (dimensionless)"
    legend_algebraic[2] = "E in component E (dimensionless)"
    legend_constants[1] = "sigma in component E (dimensionless)"
    legend_algebraic[3] = "RE in component RE (dimensionless)"
    legend_algebraic[7] = "KP in component KP (dimensionless)"
    legend_algebraic[8] = "KPI in component KPI (dimensionless)"
    legend_constants[2] = "thetaI in component KPI (dimensionless)"
    legend_algebraic[9] = "I in component I (dimensionless)"
    legend_constants[3] = "lambda in component I (dimensionless)"
    legend_constants[4] = "thetaE in component RE (dimensionless)"
    legend_algebraic[4] = "R in component R (dimensionless)"
    legend_constants[5] = "VCs in component Vs (dimensionless)"
    legend_constants[6] = "Vsm in component Vs (dimensionless)"
    legend_constants[7] = "KsE in component Vs (dimensionless)"
    legend_constants[8] = "V1m in component V1 (dimensionless)"
    legend_constants[9] = "K1C in component V1 (dimensionless)"
    legend_constants[10] = "K1 in component V1 (dimensionless)"
    legend_constants[11] = "V2m in component V2 (dimensionless)"
    legend_constants[12] = "K2 in component V2 (dimensionless)"
    legend_constants[13] = "V3m in component V3 (dimensionless)"
    legend_constants[14] = "K3 in component V3 (dimensionless)"
    legend_constants[15] = "V4m in component V4 (dimensionless)"
    legend_constants[16] = "K4 in component V4 (dimensionless)"
    legend_constants[17] = "VdEm in component Vd (dimensionless)"
    legend_constants[18] = "KdC in component Vd (dimensionless)"
    legend_rates[0] = "d/dt C in component C (dimensionless)"
    legend_rates[1] = "d/dt K in component K (dimensionless)"
    legend_rates[2] = "d/dt RP in component RP (dimensionless)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 0.38
    constants[0] = 1.0
    states[1] = 0.1
    states[2] = 1.0
    constants[1] = 10
    constants[2] = 1.0
    constants[3] = 1.0
    constants[4] = 0.01
    constants[5] = 1.0
    constants[6] = 1.0
    constants[7] = 0.1
    constants[8] = 50.0
    constants[9] = 0.1
    constants[10] = 0.0001
    constants[11] = 40
    constants[12] = 0.0001
    constants[13] = 3000
    constants[14] = 0.0001
    constants[15] = 3.0
    constants[16] = 0.0001
    constants[17] = 1000.0
    constants[18] = 0.005
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rootfind_0(voi, constants, rates, states, algebraic)
    algebraic[5] = constants[5]+constants[6]*(algebraic[2]/(constants[7]+algebraic[2]))
    algebraic[0] = constants[8]*(states[0]/(constants[9]+states[0]))*(states[1]/(constants[10]+states[1]))
    rootfind_1(voi, constants, rates, states, algebraic)
    algebraic[10] = constants[11]*(algebraic[7]/(constants[12]+algebraic[7]))
    algebraic[6] = states[0]+constants[17]*algebraic[2]*(states[0]/(constants[18]+states[0]))
    rates[0] = (algebraic[5]+constants[0]*algebraic[10])-(constants[0]*algebraic[0]+algebraic[6])
    rates[1] = algebraic[10]-algebraic[0]
    algebraic[11] = constants[13]*algebraic[7]*(algebraic[3]/(constants[14]+algebraic[3]))
    algebraic[1] = constants[15]*(states[2]/(constants[16]+states[2]))
    rates[2] = algebraic[11]-algebraic[1]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[5] = constants[5]+constants[6]*(algebraic[2]/(constants[7]+algebraic[2]))
    algebraic[0] = constants[8]*(states[0]/(constants[9]+states[0]))*(states[1]/(constants[10]+states[1]))
    algebraic[10] = constants[11]*(algebraic[7]/(constants[12]+algebraic[7]))
    algebraic[6] = states[0]+constants[17]*algebraic[2]*(states[0]/(constants[18]+states[0]))
    algebraic[11] = constants[13]*algebraic[7]*(algebraic[3]/(constants[14]+algebraic[3]))
    algebraic[1] = constants[15]*(states[2]/(constants[16]+states[2]))
    return algebraic

initialGuess0 = None
def rootfind_0(voi, constants, rates, states, algebraic):
    """Calculate values of algebraic variables for DAE"""
    from scipy.optimize import fsolve
    global initialGuess0
    if initialGuess0 is None: initialGuess0 = ones(3)*0.1
    if not iterable(voi):
        soln = fsolve(residualSN_0, initialGuess0, args=(algebraic, voi, constants, rates, states), xtol=1E-6)
        initialGuess0 = soln
        algebraic[2] = soln[0]
        algebraic[3] = soln[1]
        algebraic[4] = soln[2]
    else:
        for (i,t) in enumerate(voi):
            soln = fsolve(residualSN_0, initialGuess0, args=(algebraic[:,i], voi[i], constants, rates[:i], states[:,i]), xtol=1E-6)
            initialGuess0 = soln
            algebraic[2][i] = soln[0]
            algebraic[3][i] = soln[1]
            algebraic[4][i] = soln[2]

def residualSN_0(algebraicCandidate, algebraic, voi, constants, rates, states):
    resid = array([0.0] * 3)
    algebraic[2] = algebraicCandidate[0]
    algebraic[3] = algebraicCandidate[1]
    algebraic[4] = algebraicCandidate[2]
    resid[0] = (algebraic[2]-(1.00000-constants[1]*algebraic[3]))
    resid[1] = (algebraic[3]-constants[4]*algebraic[4]*algebraic[2])
    resid[2] = (algebraic[4]-(1.00000-(states[2]+algebraic[3])))
    return resid

initialGuess1 = None
def rootfind_1(voi, constants, rates, states, algebraic):
    """Calculate values of algebraic variables for DAE"""
    from scipy.optimize import fsolve
    global initialGuess1
    if initialGuess1 is None: initialGuess1 = ones(3)*0.1
    if not iterable(voi):
        soln = fsolve(residualSN_1, initialGuess1, args=(algebraic, voi, constants, rates, states), xtol=1E-6)
        initialGuess1 = soln
        algebraic[7] = soln[0]
        algebraic[8] = soln[1]
        algebraic[9] = soln[2]
    else:
        for (i,t) in enumerate(voi):
            soln = fsolve(residualSN_1, initialGuess1, args=(algebraic[:,i], voi[i], constants, rates[:i], states[:,i]), xtol=1E-6)
            initialGuess1 = soln
            algebraic[7][i] = soln[0]
            algebraic[8][i] = soln[1]
            algebraic[9][i] = soln[2]

def residualSN_1(algebraicCandidate, algebraic, voi, constants, rates, states):
    resid = array([0.0] * 3)
    algebraic[7] = algebraicCandidate[0]
    algebraic[8] = algebraicCandidate[1]
    algebraic[9] = algebraicCandidate[2]
    resid[0] = (algebraic[7]-(1.00000-(algebraic[8]+states[1])))
    resid[1] = (algebraic[8]-constants[2]*algebraic[7]*algebraic[9])
    resid[2] = (algebraic[9]-(1.00000-constants[3]*algebraic[8]))
    return resid

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
        self.gamma = 1.0
        self.sigma = 10
        self.thetaI = 1.0
        self.lambda = 1.0
        self.thetaE = 0.01
        self.VCs = 1.0
        self.Vsm = 1.0
        self.KsE = 0.1
        self.V1m = 50.0
        self.K1C = 0.1
        self.K1 = 0.0001
        self.V2m = 40
        self.K2 = 0.0001
        self.V3m = 3000
        self.K3 = 0.0001
        self.V4m = 3.0
        self.K4 = 0.0001
        self.VdEm = 1000.0
        self.KdC = 0.005

    def to_dict(self):
        return {
            "gamma": self.gamma,
            "sigma": self.sigma,
            "thetaI": self.thetaI,
            "lambda": self.lambda,
            "thetaE": self.thetaE,
            "VCs": self.VCs,
            "Vsm": self.Vsm,
            "KsE": self.KsE,
            "V1m": self.V1m,
            "K1C": self.K1C,
            "K1": self.K1,
            "V2m": self.V2m,
            "K2": self.K2,
            "V3m": self.V3m,
            "K3": self.K3,
            "V4m": self.V4m,
            "K4": self.K4,
            "VdEm": self.VdEm,
            "KdC": self.KdC,
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
        y0=[0.38, 0.1, 1.0],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "hatzimanikatis_lee_bailey_1999"
        self.curve_names = [
            "C",
            "K",
            "RP",
        ]
        self.state_names = ['C', 'K', 'RP']
        self.algebraic_names = ['V1', 'V4', 'E', 'RE', 'R', 'Vs', 'Vd', 'KP', 'KPI', 'I', 'V2', 'V3']
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
        c[0] = p.gamma
        c[1] = p.sigma
        c[2] = p.thetaI
        c[3] = p.lambda
        c[4] = p.thetaE
        c[5] = p.VCs
        c[6] = p.Vsm
        c[7] = p.KsE
        c[8] = p.V1m
        c[9] = p.K1C
        c[10] = p.K1
        c[11] = p.V2m
        c[12] = p.K2
        c[13] = p.V3m
        c[14] = p.K3
        c[15] = p.V4m
        c[16] = p.K4
        c[17] = p.VdEm
        c[18] = p.KdC

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
