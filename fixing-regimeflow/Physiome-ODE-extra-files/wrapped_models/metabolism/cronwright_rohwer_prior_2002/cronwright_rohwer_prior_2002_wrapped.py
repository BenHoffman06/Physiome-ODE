# Size of variable arrays:
sizeAlgebraic = 2
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
    legend_voi = "time in component environment (minute)"
    legend_constants[12] = "F16BP in component F16BP (millimolar)"
    legend_states[0] = "G3P in component G3P (millimolar)"
    legend_algebraic[0] = "V_Gpd_p in component V_Gpd_p (flux)"
    legend_algebraic[1] = "V_Gpp_p in component V_Gpp_p (flux)"
    legend_constants[13] = "DHAP in component DHAP (millimolar)"
    legend_constants[14] = "ATP in component ATP (millimolar)"
    legend_constants[15] = "ADP in component ADP (millimolar)"
    legend_constants[16] = "NADH in component NADH (millimolar)"
    legend_constants[17] = "NAD in component NAD (millimolar)"
    legend_constants[18] = "Pi_ in component Pi (millimolar)"
    legend_constants[0] = "K_F16BP in component V_Gpd_p (millimolar)"
    legend_constants[1] = "K_ATP in component V_Gpd_p (millimolar)"
    legend_constants[2] = "K_ADP in component V_Gpd_p (millimolar)"
    legend_constants[3] = "K_NAD in component V_Gpd_p (millimolar)"
    legend_constants[4] = "K_NADH in component V_Gpd_p (millimolar)"
    legend_constants[5] = "K_G3P in component V_Gpd_p (millimolar)"
    legend_constants[6] = "K_DHAP in component V_Gpd_p (millimolar)"
    legend_constants[7] = "K_eq in component V_Gpd_p (dimensionless)"
    legend_constants[8] = "Vf in component V_Gpd_p (flux)"
    legend_constants[9] = "K_G3P in component V_Gpp_p (millimolar)"
    legend_constants[10] = "K_Pi in component V_Gpp_p (millimolar)"
    legend_constants[11] = "V in component V_Gpp_p (flux)"
    legend_rates[0] = "d/dt G3P in component G3P (millimolar)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 24
    constants[0] = 4.8
    constants[1] = 0.73
    constants[2] = 2
    constants[3] = 0.93
    constants[4] = 0.023
    constants[5] = 1.2
    constants[6] = 0.54
    constants[7] = 1e4
    constants[8] = 36
    constants[9] = 3.5
    constants[10] = 1
    constants[11] = 18
    constants[12] = 0.00000
    constants[13] = 0.590000
    constants[14] = 2.37000
    constants[15] = 2.17000
    constants[16] = 1.87000
    constants[17] = 1.45000
    constants[18] = 2.17000
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[0] = ((constants[8]/(constants[4]*constants[6]))*(constants[16]*constants[13]-(constants[17]*states[0])/constants[7]))/((1.00000+constants[12]/constants[0]+constants[14]/constants[1]+constants[15]/constants[2])*(1.00000+constants[16]/constants[4]+constants[17]/constants[3])*(1.00000+constants[13]/constants[6]+states[0]/constants[5]))
    algebraic[1] = ((constants[11]*states[0])/constants[9])/((1.00000+states[0]/constants[9])*(1.00000+constants[18]/constants[10]))
    rates[0] = -algebraic[1]+algebraic[0]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = ((constants[8]/(constants[4]*constants[6]))*(constants[16]*constants[13]-(constants[17]*states[0])/constants[7]))/((1.00000+constants[12]/constants[0]+constants[14]/constants[1]+constants[15]/constants[2])*(1.00000+constants[16]/constants[4]+constants[17]/constants[3])*(1.00000+constants[13]/constants[6]+states[0]/constants[5]))
    algebraic[1] = ((constants[11]*states[0])/constants[9])/((1.00000+states[0]/constants[9])*(1.00000+constants[18]/constants[10]))
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
        self.K_F16BP = 4.8
        self.K_ATP = 0.73
        self.K_ADP = 2
        self.K_NAD = 0.93
        self.K_NADH = 0.023
        self.K_G3P = 1.2
        self.K_DHAP = 0.54
        self.K_eq = 1e4
        self.Vf = 36
        self.K_G3P_1 = 3.5
        self.K_Pi = 1
        self.V = 18
        self.F16BP = 0.00000
        self.DHAP = 0.590000
        self.ATP = 2.37000
        self.ADP = 2.17000
        self.NADH = 1.87000
        self.NAD = 1.45000
        self.Pi_ = 2.17000

    def to_dict(self):
        return {
            "K_F16BP": self.K_F16BP,
            "K_ATP": self.K_ATP,
            "K_ADP": self.K_ADP,
            "K_NAD": self.K_NAD,
            "K_NADH": self.K_NADH,
            "K_G3P": self.K_G3P,
            "K_DHAP": self.K_DHAP,
            "K_eq": self.K_eq,
            "Vf": self.Vf,
            "K_G3P_1": self.K_G3P_1,
            "K_Pi": self.K_Pi,
            "V": self.V,
            "F16BP": self.F16BP,
            "DHAP": self.DHAP,
            "ATP": self.ATP,
            "ADP": self.ADP,
            "NADH": self.NADH,
            "NAD": self.NAD,
            "Pi_": self.Pi_,
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
        y0=[24],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "cronwright_rohwer_prior_2002"
        self.curve_names = [
            "G3P",
        ]
        self.state_names = ['G3P']
        self.algebraic_names = ['V_Gpd_p', 'V_Gpp_p']
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
        c[0] = p.K_F16BP
        c[1] = p.K_ATP
        c[2] = p.K_ADP
        c[3] = p.K_NAD
        c[4] = p.K_NADH
        c[5] = p.K_G3P
        c[6] = p.K_DHAP
        c[7] = p.K_eq
        c[8] = p.Vf
        c[9] = p.K_G3P_1
        c[10] = p.K_Pi
        c[11] = p.V
        c[12] = p.F16BP
        c[13] = p.DHAP
        c[14] = p.ATP
        c[15] = p.ADP
        c[16] = p.NADH
        c[17] = p.NAD
        c[18] = p.Pi_

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
