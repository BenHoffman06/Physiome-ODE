# Size of variable arrays:
sizeAlgebraic = 8
sizeStates = 1
sizeConstants = 12
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (second)"
    legend_algebraic[0] = "F_isom in component contraction (newton)"
    legend_constants[11] = "c in component contraction (newton)"
    legend_states[0] = "L_ce in component contraction (metre)"
    legend_constants[0] = "L_ce_opt in component contraction (metre)"
    legend_algebraic[1] = "L in component contraction (metre)"
    legend_constants[1] = "width in component contraction (metre)"
    legend_constants[2] = "Factor in component contraction (per_second)"
    legend_constants[3] = "A_REL in component contraction (newton)"
    legend_constants[4] = "B_REL in component contraction (dimensionless)"
    legend_algebraic[7] = "v_ce in component contraction (metre_per_second)"
    legend_algebraic[5] = "F in component contraction (newton)"
    legend_constants[5] = "F_max in component contraction (newton)"
    legend_constants[6] = "q in component contraction (dimensionless)"
    legend_algebraic[4] = "c1 in component contraction (per_second)"
    legend_algebraic[2] = "c2 in component contraction (newton)"
    legend_algebraic[6] = "c3 in component contraction (per_newton_second)"
    legend_constants[7] = "slope in component contraction (newton)"
    legend_constants[8] = "F_asympt in component contraction (dimensionless)"
    legend_algebraic[3] = "L_see in component contraction (metre)"
    legend_constants[9] = "L_slack in component contraction (metre)"
    legend_constants[10] = "alpha in component contraction (newton_per_metre)"
    legend_rates[0] = "d/dt L_ce in component contraction (metre)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 0.05
    constants[0] = 0.055
    constants[1] = 0.888
    constants[2] = 1
    constants[3] = 0.41
    constants[4] = 5.2
    constants[5] = 3277.4
    constants[6] = 1
    constants[7] = 2
    constants[8] = 1.5
    constants[9] = 0.42
    constants[10] = 1449.027
    constants[11] = -1.00000/(power(constants[1], 2.00000))
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[0] = (constants[11]*(power(states[0]/constants[0], 2.00000))-(2.00000*constants[11]*states[0])/constants[0])+constants[11]+1.00000
    algebraic[1] = custom_piecewise([less_equal(voi , 1.00000), 1.00000 , greater(voi , 1.00000) & less(voi , 5.00000), 0.920000 , True, 0.900000])
    algebraic[3] = algebraic[1]-states[0]
    algebraic[5] = constants[10]*(algebraic[3]-constants[9])
    algebraic[7] = -constants[2]*states[0]*(((algebraic[0]+constants[3])*constants[4])/(1.00000*(algebraic[5]/(constants[5]*constants[6]))+constants[3])-constants[4])
    rates[0] = algebraic[7]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = (constants[11]*(power(states[0]/constants[0], 2.00000))-(2.00000*constants[11]*states[0])/constants[0])+constants[11]+1.00000
    algebraic[1] = custom_piecewise([less_equal(voi , 1.00000), 1.00000 , greater(voi , 1.00000) & less(voi , 5.00000), 0.920000 , True, 0.900000])
    algebraic[3] = algebraic[1]-states[0]
    algebraic[5] = constants[10]*(algebraic[3]-constants[9])
    algebraic[7] = -constants[2]*states[0]*(((algebraic[0]+constants[3])*constants[4])/(1.00000*(algebraic[5]/(constants[5]*constants[6]))+constants[3])-constants[4])
    algebraic[2] = algebraic[0]*constants[8]
    algebraic[4] = (constants[2]*constants[4]*(power(algebraic[0]+algebraic[2], 2.00000)))/((algebraic[0]+constants[3])*constants[7])
    algebraic[6] = algebraic[4]/(algebraic[0]+algebraic[2])
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
        self.L_ce_opt = 0.055
        self.width = 0.888
        self.Factor = 1
        self.A_REL = 0.41
        self.B_REL = 5.2
        self.F_max = 3277.4
        self.q = 1
        self.slope = 2
        self.F_asympt = 1.5
        self.L_slack = 0.42
        self.alpha = 1449.027

    def to_dict(self):
        return {
            "L_ce_opt": self.L_ce_opt,
            "width": self.width,
            "Factor": self.Factor,
            "A_REL": self.A_REL,
            "B_REL": self.B_REL,
            "F_max": self.F_max,
            "q": self.q,
            "slope": self.slope,
            "F_asympt": self.F_asympt,
            "L_slack": self.L_slack,
            "alpha": self.alpha,
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
        y0=[0.05],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "nagano_2001"
        self.curve_names = [
            "L_ce",
        ]
        self.state_names = ['L_ce']
        self.algebraic_names = ['F_isom', 'L', 'c2', 'L_see', 'c1', 'F', 'c3', 'v_ce']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 12
        p = self.params

        # direct mapping
        c[0] = p.L_ce_opt
        c[1] = p.width
        c[2] = p.Factor
        c[3] = p.A_REL
        c[4] = p.B_REL
        c[5] = p.F_max
        c[6] = p.q
        c[7] = p.slope
        c[8] = p.F_asympt
        c[9] = p.L_slack
        c[10] = p.alpha

        # derived constants
        c[11] = -1.00000/(power(c[1], 2.00000))

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
