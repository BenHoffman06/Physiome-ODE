# Size of variable arrays:
sizeAlgebraic = 2
sizeStates = 5
sizeConstants = 35
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (hour)"
    legend_states[0] = "GH in component GH (ng_ml)"
    legend_constants[0] = "GHS in component GH (dimensionless)"
    legend_constants[1] = "k1 in component GH (first_order_rate_constant)"
    legend_constants[2] = "kr1 in component GH (ng_ml_hr)"
    legend_constants[3] = "t1 in component GH (pg_ml)"
    legend_constants[4] = "n1 in component GH (dimensionless)"
    legend_constants[5] = "n2 in component GH (dimensionless)"
    legend_constants[6] = "g0 in component GH (dimensionless)"
    legend_constants[7] = "ng0 in component GH (dimensionless)"
    legend_constants[8] = "tg0 in component GH (dimensionless)"
    legend_constants[9] = "t2 in component GH (pg_ml)"
    legend_states[1] = "SRIF_PeV in component SRIF_PeV (pg_ml)"
    legend_constants[33] = "F1_GHS in component F (dimensionless)"
    legend_states[2] = "GHRH in component GHRH (pg_ml)"
    legend_states[3] = "ghr_GHRH in component ghr_GHRH (pg_ml)"
    legend_constants[10] = "k4 in component SRIF_PeV (first_order_rate_constant)"
    legend_constants[11] = "kr4 in component SRIF_PeV (pg_ml_hr)"
    legend_constants[12] = "t5 in component SRIF_PeV (ng_ml)"
    legend_constants[13] = "n5 in component SRIF_PeV (dimensionless)"
    legend_constants[14] = "S_basal in component SRIF_PeV (pg_ml_hr)"
    legend_states[4] = "SRIF_ArC in component SRIF_ArC (pg_ml)"
    legend_constants[15] = "k2 in component SRIF_ArC (first_order_rate_constant)"
    legend_constants[16] = "kr2 in component SRIF_ArC (pg_ml_hr)"
    legend_constants[17] = "t3 in component SRIF_ArC (pg_ml)"
    legend_constants[18] = "n3 in component SRIF_ArC (dimensionless)"
    legend_constants[19] = "k3 in component GHRH (first_order_rate_constant)"
    legend_constants[20] = "kr3 in component GHRH (pg_ml_hr)"
    legend_constants[21] = "t4 in component GHRH (pg_ml)"
    legend_constants[22] = "n4 in component GHRH (dimensionless)"
    legend_constants[34] = "F2_GHS in component F (dimensionless)"
    legend_constants[23] = "g1 in component F (dimensionless)"
    legend_constants[24] = "g2 in component F (dimensionless)"
    legend_constants[25] = "tg1 in component F (dimensionless)"
    legend_constants[26] = "tg2 in component F (dimensionless)"
    legend_constants[27] = "ng1 in component F (dimensionless)"
    legend_constants[28] = "ng2 in component F (dimensionless)"
    legend_algebraic[1] = "dghr_GHRH_dt in component ghr_GHRH (pg_ml_hr)"
    legend_algebraic[0] = "inject in component ghr_GHRH (pg_ml_hr)"
    legend_constants[29] = "kghr in component ghr_GHRH (first_order_rate_constant)"
    legend_constants[30] = "C in component ghr_GHRH (pg_ml_hr)"
    legend_constants[31] = "onset in component ghr_GHRH (hour)"
    legend_constants[32] = "duration in component ghr_GHRH (hour)"
    legend_rates[0] = "d/dt GH in component GH (ng_ml)"
    legend_rates[1] = "d/dt SRIF_PeV in component SRIF_PeV (pg_ml)"
    legend_rates[4] = "d/dt SRIF_ArC in component SRIF_ArC (pg_ml)"
    legend_rates[2] = "d/dt GHRH in component GHRH (pg_ml)"
    legend_rates[3] = "d/dt ghr_GHRH in component ghr_GHRH (pg_ml)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 0.0
    constants[0] = 20.0
    constants[1] = 3.0
    constants[2] = 600.0
    constants[3] = 400.0
    constants[4] = 5.0
    constants[5] = 2.0
    constants[6] = 1.0
    constants[7] = 2.9
    constants[8] = 200.0
    constants[9] = 10.0
    states[1] = 0.0
    states[2] = 0.0
    states[3] = 0.0
    constants[10] = 25.0
    constants[11] = 20400.0
    constants[12] = 10.0
    constants[13] = 2.0
    constants[14] = 900.0
    states[4] = 0.0
    constants[15] = 25.0
    constants[16] = 2200.0
    constants[17] = 400.0
    constants[18] = 2.0
    constants[19] = 40.0
    constants[20] = 63000.0
    constants[21] = 28.0
    constants[22] = 5.0
    constants[23] = 45000.0
    constants[24] = 100.0
    constants[25] = 390.0
    constants[26] = 10000.0
    constants[27] = 3.0
    constants[28] = 2.0
    constants[29] = 15.0
    constants[30] = 10000.0
    constants[31] = 2.0
    constants[32] = 0.2
    constants[33] = constants[23]*((power(constants[0]/constants[25], constants[27]))/(1.00000+power(constants[0]/constants[25], constants[27])))
    constants[34] = constants[24]*((power(constants[0]/constants[26], constants[28]))/(1.00000+power(constants[0]/constants[26], constants[28])))
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[0] = constants[2]*((power((states[2]+states[3])/constants[3], constants[4]))/(power((states[2]+states[3])/constants[3], constants[4])+1.00000)+constants[6]*((power(constants[0]/constants[8], constants[7]))/(1.00000+power(constants[0]/constants[8], constants[7])))+(1.00000+constants[33])/(1.00000+power(states[1]/constants[9], constants[5])+constants[33]))-constants[1]*states[0]
    rates[1] = -(constants[10]*states[1])+constants[11]*((power(states[0]/constants[12], constants[13]))/(power(states[0]/constants[12], constants[13])+1.00000))+constants[14]
    rates[4] = constants[16]*((power((states[2]+states[3])/constants[17], constants[18]))/(1.00000+power((states[2]+states[3])/constants[17], constants[18])))-constants[15]*states[4]
    rates[2] = (constants[20]*((1.00000+constants[34])/(1.00000+power((states[1]+states[4])/constants[21], constants[22])+constants[34]))+states[3]*1.00000)-constants[19]*states[2]
    algebraic[0] = custom_piecewise([less(voi , constants[31]), 0.00000 , greater_equal(voi , constants[31]) & less_equal(voi , constants[31]+constants[32]), constants[30] , greater(voi , constants[31]+constants[32]), 0.00000 , True, float('nan')])
    rates[3] = algebraic[0]-constants[29]*states[3]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = custom_piecewise([less(voi , constants[31]), 0.00000 , greater_equal(voi , constants[31]) & less_equal(voi , constants[31]+constants[32]), constants[30] , greater(voi , constants[31]+constants[32]), 0.00000 , True, float('nan')])
    algebraic[1] = algebraic[0]-constants[29]*states[3]
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
        self.GHS = 20.0
        self.k1 = 3.0
        self.kr1 = 600.0
        self.t1 = 400.0
        self.n1 = 5.0
        self.n2 = 2.0
        self.g0 = 1.0
        self.ng0 = 2.9
        self.tg0 = 200.0
        self.t2 = 10.0
        self.k4 = 25.0
        self.kr4 = 20400.0
        self.t5 = 10.0
        self.n5 = 2.0
        self.S_basal = 900.0
        self.k2 = 25.0
        self.kr2 = 2200.0
        self.t3 = 400.0
        self.n3 = 2.0
        self.k3 = 40.0
        self.kr3 = 63000.0
        self.t4 = 28.0
        self.n4 = 5.0
        self.g1 = 45000.0
        self.g2 = 100.0
        self.tg1 = 390.0
        self.tg2 = 10000.0
        self.ng1 = 3.0
        self.ng2 = 2.0
        self.kghr = 15.0
        self.C = 10000.0
        self.onset = 2.0
        self.duration = 0.2

    def to_dict(self):
        return {
            "GHS": self.GHS,
            "k1": self.k1,
            "kr1": self.kr1,
            "t1": self.t1,
            "n1": self.n1,
            "n2": self.n2,
            "g0": self.g0,
            "ng0": self.ng0,
            "tg0": self.tg0,
            "t2": self.t2,
            "k4": self.k4,
            "kr4": self.kr4,
            "t5": self.t5,
            "n5": self.n5,
            "S_basal": self.S_basal,
            "k2": self.k2,
            "kr2": self.kr2,
            "t3": self.t3,
            "n3": self.n3,
            "k3": self.k3,
            "kr3": self.kr3,
            "t4": self.t4,
            "n4": self.n4,
            "g1": self.g1,
            "g2": self.g2,
            "tg1": self.tg1,
            "tg2": self.tg2,
            "ng1": self.ng1,
            "ng2": self.ng2,
            "kghr": self.kghr,
            "C": self.C,
            "onset": self.onset,
            "duration": self.duration,
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
        y0=[0.0, 0.0, 0.0, 0.0, 0.0],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "farhy_bowers_veldhuis_2007_b"
        self.curve_names = [
            "GH",
            "SRIF_PeV",
            "GHRH",
            "ghr_GHRH",
            "SRIF_ArC",
        ]
        self.state_names = ['GH', 'SRIF_PeV', 'GHRH', 'ghr_GHRH', 'SRIF_ArC']
        self.algebraic_names = ['inject', 'dghr_GHRH_dt']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 35
        p = self.params

        # direct mapping
        c[0] = p.GHS
        c[1] = p.k1
        c[2] = p.kr1
        c[3] = p.t1
        c[4] = p.n1
        c[5] = p.n2
        c[6] = p.g0
        c[7] = p.ng0
        c[8] = p.tg0
        c[9] = p.t2
        c[10] = p.k4
        c[11] = p.kr4
        c[12] = p.t5
        c[13] = p.n5
        c[14] = p.S_basal
        c[15] = p.k2
        c[16] = p.kr2
        c[17] = p.t3
        c[18] = p.n3
        c[19] = p.k3
        c[20] = p.kr3
        c[21] = p.t4
        c[22] = p.n4
        c[23] = p.g1
        c[24] = p.g2
        c[25] = p.tg1
        c[26] = p.tg2
        c[27] = p.ng1
        c[28] = p.ng2
        c[29] = p.kghr
        c[30] = p.C
        c[31] = p.onset
        c[32] = p.duration

        # derived constants
        c[33] = c[23]*((power(c[0]/c[25], c[27]))/(1.00000+power(c[0]/c[25], c[27])))
        c[34] = c[24]*((power(c[0]/c[26], c[28]))/(1.00000+power(c[0]/c[26], c[28])))

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
