# Size of variable arrays:
sizeAlgebraic = 2
sizeStates = 13
sizeConstants = 30
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (minute)"
    legend_states[0] = "cAMP in component cAMP (micromolar)"
    legend_constants[0] = "Ko in component cAMP (dimensionless)"
    legend_constants[1] = "Ka in component cAMP (per_micromolar)"
    legend_constants[2] = "Kb in component cAMP (per_micromolar)"
    legend_constants[3] = "Kdsm in component cAMP (micromolar)"
    legend_constants[4] = "Vmsm in component cAMP (flux)"
    legend_constants[5] = "Vdsm in component cAMP (flux)"
    legend_algebraic[0] = "ACTH in component cAMP (micromolar)"
    legend_algebraic[1] = "IS in component IS (dimensionless)"
    legend_constants[6] = "Crpt in component IS (dimensionless)"
    legend_constants[7] = "K in component IS (dimensionless)"
    legend_constants[8] = "Kd in component IS (micromolar)"
    legend_constants[9] = "n in component IS (dimensionless)"
    legend_states[1] = "V in component V (flux)"
    legend_constants[10] = "P in component V (micromolar_per_minute2)"
    legend_constants[11] = "Q in component V (first_order_rate_constant)"
    legend_states[2] = "W in component W (flux)"
    legend_constants[12] = "T in component W (micromolar2_per_minute2)"
    legend_constants[13] = "U in component W (first_order_rate_constant)"
    legend_states[3] = "CHOC in component CHOC (micromolar)"
    legend_constants[14] = "Lmtr in component model_parameters (first_order_rate_constant)"
    legend_states[4] = "Kmtr in component Kmtr (first_order_rate_constant)"
    legend_states[5] = "CHOM in component CHOM (micromolar)"
    legend_constants[15] = "Kbac in component model_parameters (first_order_rate_constant)"
    legend_states[6] = "Kfor in component Kfor (first_order_rate_constant)"
    legend_constants[16] = "Kcb in component model_parameters (first_order_rate_constant)"
    legend_constants[17] = "Kcf in component model_parameters (first_order_rate_constant)"
    legend_states[7] = "CHON in component CHON (micromolar)"
    legend_states[8] = "CHOL in component CHOL (micromolar)"
    legend_constants[18] = "C in component Kmtr (per_minute2)"
    legend_constants[19] = "D in component Kmtr (first_order_rate_constant)"
    legend_constants[20] = "R in component Kfor (per_minute2)"
    legend_constants[21] = "S in component Kfor (first_order_rate_constant)"
    legend_constants[22] = "Vm in component model_parameters (flux)"
    legend_constants[23] = "Km in component model_parameters (micromolar)"
    legend_states[9] = "PREG in component PREG (micromolar)"
    legend_constants[24] = "Vmptr in component model_parameters (flux)"
    legend_constants[25] = "Kmptr in component model_parameters (micromolar)"
    legend_states[10] = "PRO in component PRO (micromolar)"
    legend_constants[26] = "HA in component PRO (dimensionless)"
    legend_constants[27] = "AH in component model_parameters (first_order_rate_constant)"
    legend_states[11] = "HYPR in component HYPR (micromolar)"
    legend_constants[28] = "HY in component model_parameters (first_order_rate_constant)"
    legend_states[12] = "CORT in component CORT (micromolar)"
    legend_constants[29] = "LH in component CORT (first_order_rate_constant)"
    legend_rates[0] = "d/dt cAMP in component cAMP (micromolar)"
    legend_rates[1] = "d/dt V in component V (flux)"
    legend_rates[2] = "d/dt W in component W (flux)"
    legend_rates[3] = "d/dt CHOC in component CHOC (micromolar)"
    legend_rates[5] = "d/dt CHOM in component CHOM (micromolar)"
    legend_rates[8] = "d/dt CHOL in component CHOL (micromolar)"
    legend_rates[4] = "d/dt Kmtr in component Kmtr (first_order_rate_constant)"
    legend_rates[6] = "d/dt Kfor in component Kfor (first_order_rate_constant)"
    legend_rates[7] = "d/dt CHON in component CHON (micromolar)"
    legend_rates[9] = "d/dt PREG in component PREG (micromolar)"
    legend_rates[10] = "d/dt PRO in component PRO (micromolar)"
    legend_rates[11] = "d/dt HYPR in component HYPR (micromolar)"
    legend_rates[12] = "d/dt CORT in component CORT (micromolar)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 0.95
    constants[0] = 0.013
    constants[1] = 10
    constants[2] = 1000000.0
    constants[3] = 10.0
    constants[4] = 6.0
    constants[5] = 10.0
    constants[6] = 3.0
    constants[7] = 80.0
    constants[8] = 2.11
    constants[9] = 4.0
    states[1] = 11.3
    constants[10] = 0.052
    constants[11] = 0.042
    states[2] = 10.0
    constants[12] = 8.0
    constants[13] = 0.0015
    states[3] = 532.0
    constants[14] = 1.65
    states[4] = 0.446
    states[5] = 139.0
    constants[15] = 10.0
    states[6] = 0.370
    constants[16] = 0.01
    constants[17] = 0.00033
    states[7] = 3.03
    states[8] = 3000.0
    constants[18] = 6.25
    constants[19] = 125.0
    constants[20] = 3.0
    constants[21] = 76.0
    constants[22] = 1890.0
    constants[23] = 270.0
    states[9] = 6.56
    constants[24] = 500.0
    constants[25] = 150.0
    states[10] = 0.64
    constants[26] = 0.5
    constants[27] = 16.4
    states[11] = 0.64
    constants[28] = 16.4
    states[12] = 5.2
    constants[29] = 0.724
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[2] = constants[12]*(power(states[3], -1.00000))-constants[13]*states[2]
    rates[3] = (states[1]+states[2]+constants[14]*states[5])-states[4]*states[3]
    rates[5] = (states[4]*states[3]+constants[15]*states[7]+constants[17]*states[8])-(constants[14]*states[5]+constants[16]*states[5]+states[6]*states[5])
    rates[8] = constants[16]*states[5]-constants[17]*states[8]
    rates[7] = states[6]*states[5]-(constants[15]*states[7]+(constants[22]*states[7])/(constants[23]+states[7]))
    rates[9] = (constants[22]*states[7])/(constants[23]+states[7])-(constants[24]*states[9])/(constants[25]+states[9])
    rates[10] = constants[26]*((constants[24]*states[9])/(constants[25]+states[9]))-constants[27]*states[10]
    rates[11] = constants[27]*states[10]-constants[28]*states[11]
    rates[12] = constants[28]*states[11]-constants[29]*states[12]
    algebraic[0] = custom_piecewise([greater_equal(voi , 0.00000) & less(voi , 10.0000), 1.20000e-05 , greater_equal(voi , 10.0000) & less(voi , 20.0000), 1.60000e-05 , greater_equal(voi , 20.0000) & less(voi , 35.0000), 1.20000e-05 , greater_equal(voi , 35.0000) & less(voi , 45.0000), 1.60000e-05 , True, 1.20000e-05])
    rates[0] = (constants[4]*constants[0]*(1.00000+constants[2]*algebraic[0]))/((1.00000+constants[1]*algebraic[0])+constants[0]*(1.00000+constants[2]*algebraic[0]))-(constants[5]*states[0])/(constants[3]+states[0])
    algebraic[1] = (constants[7]*constants[6]*(power(states[0], constants[9])))/(power(constants[8], constants[9])+power(states[0], constants[9]))
    rates[1] = constants[10]*algebraic[1]-constants[11]*states[1]
    rates[4] = constants[18]*algebraic[1]-constants[19]*states[4]
    rates[6] = constants[20]*algebraic[1]-constants[21]*states[6]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = custom_piecewise([greater_equal(voi , 0.00000) & less(voi , 10.0000), 1.20000e-05 , greater_equal(voi , 10.0000) & less(voi , 20.0000), 1.60000e-05 , greater_equal(voi , 20.0000) & less(voi , 35.0000), 1.20000e-05 , greater_equal(voi , 35.0000) & less(voi , 45.0000), 1.60000e-05 , True, 1.20000e-05])
    algebraic[1] = (constants[7]*constants[6]*(power(states[0], constants[9])))/(power(constants[8], constants[9])+power(states[0], constants[9]))
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
        self.Ko = 0.013
        self.Ka = 10
        self.Kb = 1000000.0
        self.Kdsm = 10.0
        self.Vmsm = 6.0
        self.Vdsm = 10.0
        self.Crpt = 3.0
        self.K = 80.0
        self.Kd = 2.11
        self.n = 4.0
        self.P = 0.052
        self.Q = 0.042
        self.T = 8.0
        self.U = 0.0015
        self.Lmtr = 1.65
        self.Kbac = 10.0
        self.Kcb = 0.01
        self.Kcf = 0.00033
        self.C = 6.25
        self.D = 125.0
        self.R = 3.0
        self.S = 76.0
        self.Vm = 1890.0
        self.Km = 270.0
        self.Vmptr = 500.0
        self.Kmptr = 150.0
        self.HA = 0.5
        self.AH = 16.4
        self.HY = 16.4
        self.LH = 0.724

    def to_dict(self):
        return {
            "Ko": self.Ko,
            "Ka": self.Ka,
            "Kb": self.Kb,
            "Kdsm": self.Kdsm,
            "Vmsm": self.Vmsm,
            "Vdsm": self.Vdsm,
            "Crpt": self.Crpt,
            "K": self.K,
            "Kd": self.Kd,
            "n": self.n,
            "P": self.P,
            "Q": self.Q,
            "T": self.T,
            "U": self.U,
            "Lmtr": self.Lmtr,
            "Kbac": self.Kbac,
            "Kcb": self.Kcb,
            "Kcf": self.Kcf,
            "C": self.C,
            "D": self.D,
            "R": self.R,
            "S": self.S,
            "Vm": self.Vm,
            "Km": self.Km,
            "Vmptr": self.Vmptr,
            "Kmptr": self.Kmptr,
            "HA": self.HA,
            "AH": self.AH,
            "HY": self.HY,
            "LH": self.LH,
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
        y0=[0.95, 11.3, 10.0, 532.0, 0.446, 139.0, 0.370, 3.03, 3000.0, 6.56, 0.64, 0.64, 5.2],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "dempsher_gann_phair_1984"
        self.curve_names = [
            "cAMP",
            "V",
            "W",
            "CHOC",
            "Kmtr",
            "CHOM",
            "Kfor",
            "CHON",
            "CHOL",
            "PREG",
            "PRO",
            "HYPR",
            "CORT",
        ]
        self.state_names = ['cAMP', 'V', 'W', 'CHOC', 'Kmtr', 'CHOM', 'Kfor', 'CHON', 'CHOL', 'PREG', 'PRO', 'HYPR', 'CORT']
        self.algebraic_names = ['ACTH', 'IS']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 30
        p = self.params

        # direct mapping
        c[0] = p.Ko
        c[1] = p.Ka
        c[2] = p.Kb
        c[3] = p.Kdsm
        c[4] = p.Vmsm
        c[5] = p.Vdsm
        c[6] = p.Crpt
        c[7] = p.K
        c[8] = p.Kd
        c[9] = p.n
        c[10] = p.P
        c[11] = p.Q
        c[12] = p.T
        c[13] = p.U
        c[14] = p.Lmtr
        c[15] = p.Kbac
        c[16] = p.Kcb
        c[17] = p.Kcf
        c[18] = p.C
        c[19] = p.D
        c[20] = p.R
        c[21] = p.S
        c[22] = p.Vm
        c[23] = p.Km
        c[24] = p.Vmptr
        c[25] = p.Kmptr
        c[26] = p.HA
        c[27] = p.AH
        c[28] = p.HY
        c[29] = p.LH

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
