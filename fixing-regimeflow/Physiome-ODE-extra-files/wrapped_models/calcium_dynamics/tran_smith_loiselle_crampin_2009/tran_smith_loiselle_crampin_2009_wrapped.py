# Size of variable arrays:
sizeAlgebraic = 6
sizeStates = 1
sizeConstants = 29
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (second)"
    legend_constants[0] = "k_p1 in component SERCA (second_order_rate_constant)"
    legend_constants[1] = "k_p2 in component SERCA (first_order_rate_constant)"
    legend_constants[2] = "k_p3 in component SERCA (first_order_rate_constant)"
    legend_constants[3] = "k_m1 in component SERCA (first_order_rate_constant)"
    legend_constants[4] = "k_m2 in component SERCA (second_order_rate_constant)"
    legend_constants[5] = "k_m3 in component SERCA (second_order_rate_constant)"
    legend_constants[6] = "kdcai in component SERCA (millimolar)"
    legend_constants[7] = "kdcasr in component SERCA (millimolar)"
    legend_constants[8] = "kdh1 in component SERCA (millimolar)"
    legend_constants[9] = "kdhi in component SERCA (millimolar_squared)"
    legend_constants[10] = "kdhsr in component SERCA (millimolar_squared)"
    legend_constants[11] = "kdh in component SERCA (millimolar)"
    legend_constants[12] = "n in component SERCA (dimensionless)"
    legend_constants[13] = "Ca_i in component SERCA (millimolar)"
    legend_states[0] = "Ca_sr in component SERCA (millimolar)"
    legend_constants[14] = "H_i in component SERCA (millimolar)"
    legend_constants[15] = "ATP in component SERCA (millimolar)"
    legend_constants[16] = "ADP in component SERCA (millimolar)"
    legend_constants[17] = "P_i in component SERCA (millimolar)"
    legend_constants[18] = "T_Cai in component SERCA (dimensionless)"
    legend_algebraic[0] = "T_Casr in component SERCA (dimensionless)"
    legend_constants[19] = "T_H1 in component SERCA (dimensionless)"
    legend_constants[20] = "T_Hi in component SERCA (dimensionless)"
    legend_constants[21] = "T_Hsr in component SERCA (dimensionless)"
    legend_constants[22] = "T_H in component SERCA (dimensionless)"
    legend_constants[23] = "a_p1 in component SERCA (first_order_rate_constant)"
    legend_constants[24] = "a_p2 in component SERCA (first_order_rate_constant)"
    legend_algebraic[1] = "a_p3 in component SERCA (first_order_rate_constant)"
    legend_constants[25] = "a_m1 in component SERCA (first_order_rate_constant)"
    legend_algebraic[2] = "a_m2 in component SERCA (first_order_rate_constant)"
    legend_constants[26] = "a_m3 in component SERCA (first_order_rate_constant)"
    legend_algebraic[3] = "s1 in component SERCA (per_second_squared)"
    legend_algebraic[4] = "s2 in component SERCA (per_second_squared)"
    legend_constants[27] = "s3 in component SERCA (per_second_squared)"
    legend_algebraic[5] = "v_cycle in component SERCA (first_order_rate_constant)"
    legend_rates[0] = "d/dt Ca_sr in component SERCA (millimolar)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    constants[0] = 25900
    constants[1] = 2540
    constants[2] = 20.5
    constants[3] = 16
    constants[4] = 67200
    constants[5] = 149
    constants[6] = 0.9
    constants[7] = 2.24
    constants[8] = 1.09e-5
    constants[9] = 3.54e-3
    constants[10] = 1.05e-8
    constants[11] = 7.24e-5
    constants[12] = 2
    constants[13] = 150e-6
    states[0] = 0
    constants[14] = 1e-4
    constants[15] = 5
    constants[16] = 36.3e-3
    constants[17] = 1
    constants[18] = constants[13]/constants[6]
    constants[28] = 1.00000
    constants[19] = constants[14]/constants[8]
    constants[20] = (power(constants[14], constants[12]))/constants[9]
    constants[21] = (power(constants[14], constants[12]))/constants[10]
    constants[22] = constants[14]/constants[11]
    constants[23] = constants[0]*constants[15]
    constants[24] = (constants[1]*(power(constants[18], 2.00000)))/(power(constants[18], 2.00000)+(power(constants[18], 2.00000))*constants[20]+constants[20]*(1.00000+constants[19]))
    constants[25] = (constants[3]*constants[20])/(power(constants[18], 2.00000)+(power(constants[18], 2.00000))*constants[20]+constants[20]*(1.00000+constants[19]))
    constants[26] = constants[5]*constants[17]
    constants[27] = constants[23]*constants[24]+constants[26]*constants[25]+constants[26]*constants[24]
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[0] = constants[28]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = states[0]/constants[7]
    algebraic[1] = (constants[2]*constants[21])/((power(algebraic[0], 2.00000))*constants[22]+constants[22]+constants[21]*(1.00000+constants[22]))
    algebraic[2] = (constants[4]*constants[16]*(power(algebraic[0], 2.00000))*constants[22])/((power(algebraic[0], 2.00000))*constants[22]+constants[22]+constants[21]*(1.00000+constants[22]))
    algebraic[3] = constants[24]*algebraic[1]+constants[25]*algebraic[1]+constants[25]*algebraic[2]
    algebraic[4] = constants[23]*algebraic[1]+algebraic[2]*constants[23]+algebraic[2]*constants[26]
    algebraic[5] = (constants[23]*constants[24]*algebraic[1]-constants[25]*algebraic[2]*constants[26])/(algebraic[3]+algebraic[4]+constants[27])
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
        self.k_p1 = 25900
        self.k_p2 = 2540
        self.k_p3 = 20.5
        self.k_m1 = 16
        self.k_m2 = 67200
        self.k_m3 = 149
        self.kdcai = 0.9
        self.kdcasr = 2.24
        self.kdh1 = 1.09e-5
        self.kdhi = 3.54e-3
        self.kdhsr = 1.05e-8
        self.kdh = 7.24e-5
        self.n = 2
        self.Ca_i = 150e-6
        self.H_i = 1e-4
        self.ATP = 5
        self.ADP = 36.3e-3
        self.P_i = 1
        self.legend_constants_28 = 1.00000

    def to_dict(self):
        return {
            "k_p1": self.k_p1,
            "k_p2": self.k_p2,
            "k_p3": self.k_p3,
            "k_m1": self.k_m1,
            "k_m2": self.k_m2,
            "k_m3": self.k_m3,
            "kdcai": self.kdcai,
            "kdcasr": self.kdcasr,
            "kdh1": self.kdh1,
            "kdhi": self.kdhi,
            "kdhsr": self.kdhsr,
            "kdh": self.kdh,
            "n": self.n,
            "Ca_i": self.Ca_i,
            "H_i": self.H_i,
            "ATP": self.ATP,
            "ADP": self.ADP,
            "P_i": self.P_i,
            "legend_constants_28": self.legend_constants_28,
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
        y0=[0],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "tran_smith_loiselle_crampin_2009"
        self.curve_names = [
            "Ca_sr",
        ]
        self.state_names = ['Ca_sr']
        self.algebraic_names = ['T_Casr', 'a_p3', 'a_m2', 's1', 's2', 'v_cycle']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 29
        p = self.params

        # direct mapping
        c[0] = p.k_p1
        c[1] = p.k_p2
        c[2] = p.k_p3
        c[3] = p.k_m1
        c[4] = p.k_m2
        c[5] = p.k_m3
        c[6] = p.kdcai
        c[7] = p.kdcasr
        c[8] = p.kdh1
        c[9] = p.kdhi
        c[10] = p.kdhsr
        c[11] = p.kdh
        c[12] = p.n
        c[13] = p.Ca_i
        c[14] = p.H_i
        c[15] = p.ATP
        c[16] = p.ADP
        c[17] = p.P_i
        c[28] = p.legend_constants_28

        # derived constants
        c[18] = c[13]/c[6]
        c[19] = c[14]/c[8]
        c[20] = (power(c[14], c[12]))/c[9]
        c[21] = (power(c[14], c[12]))/c[10]
        c[22] = c[14]/c[11]
        c[23] = c[0]*c[15]
        c[24] = (c[1]*(power(c[18], 2.00000)))/(power(c[18], 2.00000)+(power(c[18], 2.00000))*c[20]+c[20]*(1.00000+c[19]))
        c[25] = (c[3]*c[20])/(power(c[18], 2.00000)+(power(c[18], 2.00000))*c[20]+c[20]*(1.00000+c[19]))
        c[26] = c[5]*c[17]
        c[27] = c[23]*c[24]+c[26]*c[25]+c[26]*c[24]

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
