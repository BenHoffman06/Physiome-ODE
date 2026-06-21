# Size of variable arrays:
sizeAlgebraic = 17
sizeStates = 5
sizeConstants = 20
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (second)"
    legend_constants[0] = "C_m in component model_parameters (uF_per_cm2)"
    legend_states[0] = "V_s in component soma_compartment (mV)"
    legend_constants[1] = "V_Na in component soma_compartment (mV)"
    legend_constants[2] = "V_K in component soma_compartment (mV)"
    legend_states[1] = "V_D in component dendritic_compartment (mV)"
    legend_algebraic[13] = "I_Na in component soma_compartment (uA_per_cm2)"
    legend_algebraic[15] = "I_soma in component soma_compartment (uA_per_cm2)"
    legend_algebraic[0] = "I_h in component soma_compartment (uA_per_cm2)"
    legend_algebraic[6] = "I_K_DR in component soma_compartment (uA_per_cm2)"
    legend_constants[3] = "g_K_DR in component soma_compartment (mS_per_cm2)"
    legend_constants[4] = "g_Na in component soma_compartment (mS_per_cm2)"
    legend_constants[5] = "g_c in component model_parameters (mS_per_cm2)"
    legend_constants[6] = "g_h in component soma_compartment (mS_per_cm2)"
    legend_constants[7] = "p in component model_parameters (dimensionless)"
    legend_states[2] = "n in component gating_variables (dimensionless)"
    legend_states[3] = "h in component gating_variables (dimensionless)"
    legend_algebraic[10] = "m_infinity in component gating_variables (dimensionless)"
    legend_constants[8] = "V_L in component dendritic_compartment (mV)"
    legend_algebraic[16] = "I_D in component dendritic_compartment (uA_per_cm2)"
    legend_algebraic[11] = "I_L in component dendritic_compartment (uA_per_cm2)"
    legend_algebraic[7] = "I_pump in component dendritic_compartment (uA_per_cm2)"
    legend_constants[19] = "I_pump_ss in component dendritic_compartment (uA_per_cm2)"
    legend_algebraic[14] = "I_NMDA in component dendritic_compartment (uA_per_cm2)"
    legend_algebraic[12] = "I_Na_NMDA in component dendritic_compartment (uA_per_cm2)"
    legend_constants[14] = "R_pump in component dendritic_compartment (uA_per_cm2)"
    legend_algebraic[1] = "f_NMDA in component dendritic_compartment (dimensionless)"
    legend_constants[9] = "alpha in component dendritic_compartment (mMcm2_per_uAs)"
    legend_constants[15] = "g_NMDA in component dendritic_compartment (mS_per_cm2)"
    legend_constants[16] = "g_Na_NMDA in component dendritic_compartment (mS_per_cm2)"
    legend_constants[17] = "g_L in component dendritic_compartment (mS_per_cm2)"
    legend_states[4] = "Na in component dendritic_compartment (mM)"
    legend_constants[10] = "Na_eq in component dendritic_compartment (mM)"
    legend_constants[11] = "K_p in component dendritic_compartment (mM)"
    legend_constants[12] = "K_Na in component dendritic_compartment (mM)"
    legend_constants[13] = "q in component dendritic_compartment (mV)"
    legend_algebraic[2] = "n_infinity in component gating_variables (dimensionless)"
    legend_algebraic[3] = "h_infinity in component gating_variables (dimensionless)"
    legend_algebraic[4] = "r_infinity in component gating_variables (dimensionless)"
    legend_algebraic[8] = "tau_h in component gating_variables (second)"
    legend_algebraic[9] = "tau_n in component gating_variables (second)"
    legend_algebraic[5] = "tau_mL in component gating_variables (second)"
    legend_constants[18] = "tau_r in component gating_variables (second)"
    legend_rates[0] = "d/dt V_s in component soma_compartment (mV)"
    legend_rates[1] = "d/dt V_D in component dendritic_compartment (mV)"
    legend_rates[4] = "d/dt Na in component dendritic_compartment (mM)"
    legend_rates[3] = "d/dt h in component gating_variables (dimensionless)"
    legend_rates[2] = "d/dt n in component gating_variables (dimensionless)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    constants[0] = 1
    states[0] = -64
    constants[1] = 55
    constants[2] = -85
    states[1] = -77
    constants[3] = 3.2
    constants[4] = 3.2
    constants[5] = 0.1
    constants[6] = 0.1
    constants[7] = 0.5
    states[2] = 0.002
    states[3] = 1
    constants[8] = -50
    constants[9] = 0.173
    states[4] = 5.09
    constants[10] = 8
    constants[11] = 15
    constants[12] = 15
    constants[13] = 12.5
    constants[14] = 18.0000*(constants[7]/(1.00000-constants[7]))
    constants[15] = 1.25000*(constants[7]/(1.00000-constants[7]))
    constants[16] = 1.00000*(constants[7]/(1.00000-constants[7]))
    constants[17] = 0.180000*(constants[7]/(1.00000-constants[7]))
    constants[18] = 190.000
    constants[19] = (((constants[14]*constants[7])/(1.00000-constants[7]))*(power(constants[10], 3.00000)))/(power(constants[12], 3.00000)+power(constants[10], 3.00000))
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[3] = 1.00000/(1.00000+exp((states[0]+30.0000)/8.30000))
    algebraic[8] = 0.430000+0.860000/(1.00000+exp((states[0]+25.0000)/5.00000))
    rates[3] = (algebraic[3]-states[3])/algebraic[8]
    algebraic[2] = 1.00000/(1.00000+exp(-(states[0]+31.0000)/5.30000))
    algebraic[9] = (0.800000+1.60000/(1.00000+exp(0.100000*(states[0]+25.0000))))/(1.00000+exp(-0.100000*(states[0]+70.0000)))
    rates[2] = (algebraic[2]-states[2])/algebraic[9]
    algebraic[7] = (((constants[14]*constants[7])/(1.00000-constants[7]))*(power(states[1]*1.00000+states[4], 3.00000)))/(power(constants[11], 3.00000)+power(states[1]*1.00000+states[4], 3.00000))
    algebraic[1] = 1.00000/(1.00000+0.141000*exp(-states[1]/constants[13]))
    algebraic[12] = constants[16]*algebraic[1]*(states[1]-constants[1])
    rates[4] = constants[9]*(-algebraic[12]-3.00000*(algebraic[7]-constants[19]))
    algebraic[10] = 1.00000/(1.00000+exp(-(states[0]+35.0000)/6.20000))
    algebraic[13] = constants[4]*states[3]*(states[0]-constants[1])*(power(algebraic[10], 3.00000))
    algebraic[0] = constants[6]*states[3]*(states[0]+30.0000)
    algebraic[6] = constants[3]*(states[0]-constants[2])*(power(states[2], 2.00000))
    algebraic[15] = algebraic[13]+algebraic[6]+algebraic[0]
    rates[0] = (-algebraic[15]-(constants[5]/constants[7])*(states[1]-states[0]))/constants[0]
    algebraic[11] = constants[17]*(states[1]-constants[8])
    algebraic[14] = constants[15]*algebraic[1]*states[1]
    algebraic[16] = ((algebraic[14]+algebraic[7])-constants[19])+algebraic[11]
    rates[1] = (-algebraic[16]+(constants[5]/(1.00000-constants[7]))*(states[0]-states[1]))/constants[0]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[3] = 1.00000/(1.00000+exp((states[0]+30.0000)/8.30000))
    algebraic[8] = 0.430000+0.860000/(1.00000+exp((states[0]+25.0000)/5.00000))
    algebraic[2] = 1.00000/(1.00000+exp(-(states[0]+31.0000)/5.30000))
    algebraic[9] = (0.800000+1.60000/(1.00000+exp(0.100000*(states[0]+25.0000))))/(1.00000+exp(-0.100000*(states[0]+70.0000)))
    algebraic[7] = (((constants[14]*constants[7])/(1.00000-constants[7]))*(power(states[1]*1.00000+states[4], 3.00000)))/(power(constants[11], 3.00000)+power(states[1]*1.00000+states[4], 3.00000))
    algebraic[1] = 1.00000/(1.00000+0.141000*exp(-states[1]/constants[13]))
    algebraic[12] = constants[16]*algebraic[1]*(states[1]-constants[1])
    algebraic[10] = 1.00000/(1.00000+exp(-(states[0]+35.0000)/6.20000))
    algebraic[13] = constants[4]*states[3]*(states[0]-constants[1])*(power(algebraic[10], 3.00000))
    algebraic[0] = constants[6]*states[3]*(states[0]+30.0000)
    algebraic[6] = constants[3]*(states[0]-constants[2])*(power(states[2], 2.00000))
    algebraic[15] = algebraic[13]+algebraic[6]+algebraic[0]
    algebraic[11] = constants[17]*(states[1]-constants[8])
    algebraic[14] = constants[15]*algebraic[1]*states[1]
    algebraic[16] = ((algebraic[14]+algebraic[7])-constants[19])+algebraic[11]
    algebraic[4] = 1.00000/(1.00000+exp((states[0]+80.0000)/8.00000))
    algebraic[5] = 0.400000/(5.00000*exp(-(states[1]+11.0000)/8.30000)+(-(states[1]+11.0000)/8.30000)/(exp(-(states[1]+11.0000)/8.30000)-1.00000))
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
        self.C_m = 1
        self.V_Na = 55
        self.V_K = -85
        self.g_K_DR = 3.2
        self.g_Na = 3.2
        self.g_c = 0.1
        self.g_h = 0.1
        self.p = 0.5
        self.V_L = -50
        self.alpha = 0.173
        self.Na_eq = 8
        self.K_p = 15
        self.K_Na = 15
        self.q = 12.5
        self.tau_r = 190.000

    def to_dict(self):
        return {
            "C_m": self.C_m,
            "V_Na": self.V_Na,
            "V_K": self.V_K,
            "g_K_DR": self.g_K_DR,
            "g_Na": self.g_Na,
            "g_c": self.g_c,
            "g_h": self.g_h,
            "p": self.p,
            "V_L": self.V_L,
            "alpha": self.alpha,
            "Na_eq": self.Na_eq,
            "K_p": self.K_p,
            "K_Na": self.K_Na,
            "q": self.q,
            "tau_r": self.tau_r,
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
        y0=[-64, -77, 0.002, 1, 5.09],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "li_1996_simple"
        self.curve_names = [
            "V_s",
            "V_D",
            "n",
            "h",
            "Na",
        ]
        self.state_names = ['V_s', 'V_D', 'n', 'h', 'Na']
        self.algebraic_names = ['I_h', 'f_NMDA', 'n_infinity', 'h_infinity', 'r_infinity', 'tau_mL', 'I_K_DR', 'I_pump', 'tau_h', 'tau_n', 'm_infinity', 'I_L', 'I_Na_NMDA', 'I_Na', 'I_NMDA', 'I_soma', 'I_D']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 20
        p = self.params

        # direct mapping
        c[0] = p.C_m
        c[1] = p.V_Na
        c[2] = p.V_K
        c[3] = p.g_K_DR
        c[4] = p.g_Na
        c[5] = p.g_c
        c[6] = p.g_h
        c[7] = p.p
        c[8] = p.V_L
        c[9] = p.alpha
        c[10] = p.Na_eq
        c[11] = p.K_p
        c[12] = p.K_Na
        c[13] = p.q
        c[18] = p.tau_r

        # derived constants
        c[14] = 18.0000*(c[7]/(1.00000-c[7]))
        c[15] = 1.25000*(c[7]/(1.00000-c[7]))
        c[16] = 1.00000*(c[7]/(1.00000-c[7]))
        c[17] = 0.180000*(c[7]/(1.00000-c[7]))
        c[19] = (((c[14]*c[7])/(1.00000-c[7]))*(power(c[10], 3.00000)))/(power(c[12], 3.00000)+power(c[10], 3.00000))

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
