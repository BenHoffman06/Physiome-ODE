# Size of variable arrays:
sizeAlgebraic = 9
sizeStates = 1
sizeConstants = 6
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (minute)"
    legend_constants[0] = "BFN in component non_muscle_O2_delivery (L_per_minute)"
    legend_constants[1] = "OVA in component non_muscle_O2_delivery (mL_per_L)"
    legend_constants[2] = "HM in component non_muscle_O2_delivery (dimensionless)"
    legend_constants[3] = "AOM in component non_muscle_O2_delivery (dimensionless)"
    legend_constants[5] = "O2ARTN in component NM_O2_blood_supply (mL_per_minute)"
    legend_algebraic[4] = "DOB in component delivery_of_O2_to_NM_tissues (mL_per_minute)"
    legend_algebraic[5] = "POV in component NM_venous_O2_content (mmHg)"
    legend_algebraic[6] = "OSV in component NM_venous_O2_content (dimensionless)"
    legend_algebraic[1] = "POT in component pressure_of_O2_in_NM_tissue_cells (mmHg)"
    legend_algebraic[3] = "MO2 in component O2_consumption_by_NM_tissue (mL_per_minute)"
    legend_constants[4] = "O2M in component parameter_values (mL_per_minute)"
    legend_algebraic[2] = "P1O in component O2_consumption_by_NM_tissue (mmHg)"
    legend_algebraic[0] = "QO2 in component volume_of_O2_in_NM_tissue (mL)"
    legend_algebraic[8] = "DO2N in component volume_of_O2_in_NM_tissue (mL_per_minute)"
    legend_algebraic[7] = "DO2N1 in component volume_of_O2_in_NM_tissue (mL_per_minute)"
    legend_states[0] = "QO2T in component volume_of_O2_in_NM_tissue (mL)"
    legend_rates[0] = "d/dt QO2T in component volume_of_O2_in_NM_tissue (mL)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    constants[0] = 2.79521
    constants[1] = 204.497
    constants[2] = 40.0381
    constants[3] = 1.00002
    constants[4] = 164
    states[0] = 72.2362
    constants[5] = constants[1]*constants[0]
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[0] = custom_piecewise([less(states[0] , 0.00000), 0.00000 , True, states[0]])
    algebraic[1] = algebraic[0]*0.486110
    rootfind_0(voi, constants, rates, states, algebraic)
    algebraic[2] = custom_piecewise([greater(algebraic[1] , 35.0000), 35.0000 , True, algebraic[1]])
    algebraic[3] = constants[3]*constants[4]*(1.00000-(power(35.0001-algebraic[2], 3.00000))/42875.0)
    algebraic[7] = algebraic[4]-algebraic[3]
    algebraic[8] = custom_piecewise([less(algebraic[0] , 6.00000) & less(algebraic[7] , 0.00000), algebraic[7]*0.100000 , True, algebraic[7]])
    rates[0] = algebraic[8]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = custom_piecewise([less(states[0] , 0.00000), 0.00000 , True, states[0]])
    algebraic[1] = algebraic[0]*0.486110
    algebraic[2] = custom_piecewise([greater(algebraic[1] , 35.0000), 35.0000 , True, algebraic[1]])
    algebraic[3] = constants[3]*constants[4]*(1.00000-(power(35.0001-algebraic[2], 3.00000))/42875.0)
    algebraic[7] = algebraic[4]-algebraic[3]
    algebraic[8] = custom_piecewise([less(algebraic[0] , 6.00000) & less(algebraic[7] , 0.00000), algebraic[7]*0.100000 , True, algebraic[7]])
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
        algebraic[4] = soln[0]
        algebraic[5] = soln[1]
        algebraic[6] = soln[2]
    else:
        for (i,t) in enumerate(voi):
            soln = fsolve(residualSN_0, initialGuess0, args=(algebraic[:,i], voi[i], constants, rates[:i], states[:,i]), xtol=1E-6)
            initialGuess0 = soln
            algebraic[4][i] = soln[0]
            algebraic[5][i] = soln[1]
            algebraic[6][i] = soln[2]

def residualSN_0(algebraicCandidate, algebraic, voi, constants, rates, states):
    resid = array([0.0] * 3)
    algebraic[4] = algebraicCandidate[0]
    algebraic[5] = algebraicCandidate[1]
    algebraic[6] = algebraicCandidate[2]
    resid[0] = (algebraic[6]-(constants[5]-algebraic[4])/(constants[2]*5.25000*constants[0]))
    resid[1] = (algebraic[5]-algebraic[6]*57.1400)
    resid[2] = (algebraic[4]-(algebraic[5]-algebraic[1])*12.8570*constants[0])
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
        self.BFN = 2.79521
        self.OVA = 204.497
        self.HM = 40.0381
        self.AOM = 1.00002
        self.O2M = 164

    def to_dict(self):
        return {
            "BFN": self.BFN,
            "OVA": self.OVA,
            "HM": self.HM,
            "AOM": self.AOM,
            "O2M": self.O2M,
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
        y0=[72.2362],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "guyton_non_muscle_oxygen_delivery_2008"
        self.curve_names = [
            "QO2T",
        ]
        self.state_names = ['QO2T']
        self.algebraic_names = ['QO2', 'POT', 'P1O', 'MO2', 'DOB', 'POV', 'OSV', 'DO2N1', 'DO2N']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 6
        p = self.params

        # direct mapping
        c[0] = p.BFN
        c[1] = p.OVA
        c[2] = p.HM
        c[3] = p.AOM
        c[4] = p.O2M

        # derived constants
        c[5] = c[1]*c[0]

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
