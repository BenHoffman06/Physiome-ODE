# Size of variable arrays:
sizeAlgebraic = 6
sizeStates = 3
sizeConstants = 28
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (second)"
    legend_constants[27] = "v_GK in component v_GK (flux)"
    legend_constants[0] = "V_GK_min in component v_GK (enzyme_activity)"
    legend_constants[24] = "V_GK in component v_GK (enzyme_activity)"
    legend_constants[1] = "Sgk in component v_GK (millimolar)"
    legend_constants[2] = "h_GK in component v_GK (dimensionless)"
    legend_constants[26] = "Glc in component Glc (millimolar)"
    legend_constants[3] = "min_to_sec in component model_parameters (dimensionless)"
    legend_constants[4] = "dw_per_ml in component model_parameters (dimensionless)"
    legend_algebraic[1] = "v_PFK in component v_PFK (flux)"
    legend_constants[5] = "V_PFK_min in component v_PFK (enzyme_activity)"
    legend_constants[22] = "V_PFK in component v_PFK (enzyme_activity)"
    legend_constants[6] = "Spfk in component v_PFK (millimolar)"
    legend_constants[7] = "Sfba in component v_PFK (millimolar)"
    legend_constants[8] = "Xpfk in component v_PFK (millimolar)"
    legend_constants[9] = "hx in component v_PFK (dimensionless)"
    legend_constants[10] = "alpha in component v_PFK (dimensionless)"
    legend_constants[11] = "h_PFK in component v_PFK (dimensionless)"
    legend_constants[12] = "h_act in component v_PFK (dimensionless)"
    legend_states[0] = "FBP in component FBP (millimolar)"
    legend_algebraic[0] = "F6P in component F6P (millimolar)"
    legend_algebraic[5] = "v_FBA in component v_FBA (flux)"
    legend_constants[13] = "V_FBA_min in component v_FBA (enzyme_activity)"
    legend_constants[23] = "V_FBA in component v_FBA (enzyme_activity)"
    legend_constants[14] = "Qfba in component v_FBA (millimolar)"
    legend_constants[15] = "Sfba in component v_FBA (millimolar)"
    legend_constants[16] = "Pfba in component v_FBA (millimolar)"
    legend_constants[17] = "Keq_FBA in component v_FBA (millimolar)"
    legend_algebraic[2] = "G3P in component G3P (millimolar)"
    legend_algebraic[4] = "DHAP in component DHAP (millimolar)"
    legend_algebraic[3] = "v_GAPDH in component v_GAPDH (flux)"
    legend_constants[18] = "V_GAPDH_min in component v_GAPDH (enzyme_activity)"
    legend_constants[25] = "V_GAPDH in component v_GAPDH (enzyme_activity)"
    legend_constants[19] = "Sgapdh in component v_GAPDH (millimolar)"
    legend_states[1] = "G6P_F6P in component G6P_F6P (millimolar)"
    legend_constants[20] = "Keq_GPI in component F6P (dimensionless)"
    legend_states[2] = "DHAP_G3P in component DHAP_G3P (millimolar)"
    legend_constants[21] = "Keq_TPI in component G3P (dimensionless)"
    legend_rates[1] = "d/dt G6P_F6P in component G6P_F6P (millimolar)"
    legend_rates[0] = "d/dt FBP in component FBP (millimolar)"
    legend_rates[2] = "d/dt DHAP_G3P in component DHAP_G3P (millimolar)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    constants[0] = 10.0
    constants[1] = 8.0
    constants[2] = 1.7
    constants[3] = 60.0
    constants[4] = 0.3333
    constants[5] = 100.0
    constants[6] = 4.0
    constants[7] = 0.005
    constants[8] = 0.01
    constants[9] = 2.5
    constants[10] = 5.0
    constants[11] = 2.5
    constants[12] = 1.0
    states[0] = 0.00063612
    constants[13] = 25.0
    constants[14] = 0.275
    constants[15] = 0.005
    constants[16] = 0.5
    constants[17] = 0.1
    constants[18] = 250.0
    constants[19] = 0.005
    states[1] = 3.71728
    constants[20] = 0.3
    states[2] = 0.00262966
    constants[21] = 0.045455
    constants[22] = (constants[5]*constants[4])/constants[3]
    constants[23] = (constants[13]*constants[4])/constants[3]
    constants[24] = (constants[0]*constants[4])/constants[3]
    constants[25] = (constants[18]*constants[4])/constants[3]
    constants[26] = 10.0000
    constants[27] = (constants[24]*(power(constants[26]/constants[1], constants[2])))/(1.00000+power(constants[26]/constants[1], constants[2]))
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[0] = (states[1]*constants[20])/(1.00000+constants[20])
    algebraic[1] = (constants[22]*(power(algebraic[0]/constants[6], constants[11]-(constants[11]-constants[12])*((states[0]/constants[7])/(1.00000+states[0]/constants[7])))))/(power(algebraic[0]/constants[6], constants[11]-(constants[11]-constants[12])*((states[0]/constants[7])/(1.00000+states[0]/constants[7])))+(1.00000+power(states[0]/constants[8], constants[9]))/(1.00000+(power(constants[10], constants[11]-(constants[11]-constants[12])*((states[0]/constants[7])/(1.00000+states[0]/constants[7]))))*(power(states[0]/constants[8], constants[9]))))
    rates[1] = constants[27]-algebraic[1]
    algebraic[2] = (states[2]*constants[21])/(1.00000+constants[21])
    algebraic[4] = states[2]-algebraic[2]
    algebraic[5] = (constants[23]*(states[0]/constants[15]-(algebraic[2]*algebraic[4])/(constants[16]*constants[14]*constants[17])))/(1.00000+states[0]/constants[15]+algebraic[4]/constants[14]+(algebraic[2]*algebraic[4])/(constants[16]*constants[14]))
    rates[0] = algebraic[1]-algebraic[5]
    algebraic[3] = (constants[25]*algebraic[2])/(constants[19]+algebraic[2])
    rates[2] = 2.00000*algebraic[5]-algebraic[3]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = (states[1]*constants[20])/(1.00000+constants[20])
    algebraic[1] = (constants[22]*(power(algebraic[0]/constants[6], constants[11]-(constants[11]-constants[12])*((states[0]/constants[7])/(1.00000+states[0]/constants[7])))))/(power(algebraic[0]/constants[6], constants[11]-(constants[11]-constants[12])*((states[0]/constants[7])/(1.00000+states[0]/constants[7])))+(1.00000+power(states[0]/constants[8], constants[9]))/(1.00000+(power(constants[10], constants[11]-(constants[11]-constants[12])*((states[0]/constants[7])/(1.00000+states[0]/constants[7]))))*(power(states[0]/constants[8], constants[9]))))
    algebraic[2] = (states[2]*constants[21])/(1.00000+constants[21])
    algebraic[4] = states[2]-algebraic[2]
    algebraic[5] = (constants[23]*(states[0]/constants[15]-(algebraic[2]*algebraic[4])/(constants[16]*constants[14]*constants[17])))/(1.00000+states[0]/constants[15]+algebraic[4]/constants[14]+(algebraic[2]*algebraic[4])/(constants[16]*constants[14]))
    algebraic[3] = (constants[25]*algebraic[2])/(constants[19]+algebraic[2])
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
        self.V_GK_min = 10.0
        self.Sgk = 8.0
        self.h_GK = 1.7
        self.min_to_sec = 60.0
        self.dw_per_ml = 0.3333
        self.V_PFK_min = 100.0
        self.Spfk = 4.0
        self.Sfba = 0.005
        self.Xpfk = 0.01
        self.hx = 2.5
        self.alpha = 5.0
        self.h_PFK = 2.5
        self.h_act = 1.0
        self.V_FBA_min = 25.0
        self.Qfba = 0.275
        self.Sfba_1 = 0.005
        self.Pfba = 0.5
        self.Keq_FBA = 0.1
        self.V_GAPDH_min = 250.0
        self.Sgapdh = 0.005
        self.Keq_GPI = 0.3
        self.Keq_TPI = 0.045455
        self.Glc = 10.0000

    def to_dict(self):
        return {
            "V_GK_min": self.V_GK_min,
            "Sgk": self.Sgk,
            "h_GK": self.h_GK,
            "min_to_sec": self.min_to_sec,
            "dw_per_ml": self.dw_per_ml,
            "V_PFK_min": self.V_PFK_min,
            "Spfk": self.Spfk,
            "Sfba": self.Sfba,
            "Xpfk": self.Xpfk,
            "hx": self.hx,
            "alpha": self.alpha,
            "h_PFK": self.h_PFK,
            "h_act": self.h_act,
            "V_FBA_min": self.V_FBA_min,
            "Qfba": self.Qfba,
            "Sfba_1": self.Sfba_1,
            "Pfba": self.Pfba,
            "Keq_FBA": self.Keq_FBA,
            "V_GAPDH_min": self.V_GAPDH_min,
            "Sgapdh": self.Sgapdh,
            "Keq_GPI": self.Keq_GPI,
            "Keq_TPI": self.Keq_TPI,
            "Glc": self.Glc,
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
        y0=[0.00063612, 3.71728, 0.00262966],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "westermark_lansner_2003"
        self.curve_names = [
            "FBP",
            "G6P_F6P",
            "DHAP_G3P",
        ]
        self.state_names = ['FBP', 'G6P_F6P', 'DHAP_G3P']
        self.algebraic_names = ['F6P', 'v_PFK', 'G3P', 'v_GAPDH', 'DHAP', 'v_FBA']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 28
        p = self.params

        # direct mapping
        c[0] = p.V_GK_min
        c[1] = p.Sgk
        c[2] = p.h_GK
        c[3] = p.min_to_sec
        c[4] = p.dw_per_ml
        c[5] = p.V_PFK_min
        c[6] = p.Spfk
        c[7] = p.Sfba
        c[8] = p.Xpfk
        c[9] = p.hx
        c[10] = p.alpha
        c[11] = p.h_PFK
        c[12] = p.h_act
        c[13] = p.V_FBA_min
        c[14] = p.Qfba
        c[15] = p.Sfba_1
        c[16] = p.Pfba
        c[17] = p.Keq_FBA
        c[18] = p.V_GAPDH_min
        c[19] = p.Sgapdh
        c[20] = p.Keq_GPI
        c[21] = p.Keq_TPI
        c[26] = p.Glc

        # derived constants
        c[22] = (c[5]*c[4])/c[3]
        c[23] = (c[13]*c[4])/c[3]
        c[24] = (c[0]*c[4])/c[3]
        c[25] = (c[18]*c[4])/c[3]
        c[27] = (c[24]*(power(c[26]/c[1], c[2])))/(1.00000+power(c[26]/c[1], c[2]))

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
