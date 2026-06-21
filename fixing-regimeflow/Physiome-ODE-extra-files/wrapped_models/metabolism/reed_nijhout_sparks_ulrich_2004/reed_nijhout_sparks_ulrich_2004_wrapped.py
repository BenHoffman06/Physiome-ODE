# Size of variable arrays:
sizeAlgebraic = 11
sizeStates = 4
sizeConstants = 21
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (hour)"
    legend_algebraic[0] = "Metin in component environment (flux)"
    legend_states[0] = "Met in component Met (micromolar)"
    legend_algebraic[7] = "V_MS in component V_MS (flux)"
    legend_algebraic[10] = "V_BHMT in component V_BHMT (flux)"
    legend_algebraic[1] = "V_MATI in component V_MATI (flux)"
    legend_algebraic[3] = "V_MATIII in component V_MATIII (flux)"
    legend_states[1] = "AdoMet in component AdoMet (micromolar)"
    legend_algebraic[6] = "V_METH in component V_METH (flux)"
    legend_algebraic[4] = "V_GNMT in component V_GNMT (flux)"
    legend_states[2] = "AdoHcy in component AdoHcy (micromolar)"
    legend_algebraic[8] = "V_AH in component V_AH (flux)"
    legend_states[3] = "Hcy in component Hcy (micromolar)"
    legend_algebraic[9] = "V_CBS in component V_CBS (flux)"
    legend_constants[0] = "V_MATImax in component V_MATI (flux)"
    legend_constants[1] = "Km_MATI in component V_MATI (micromolar)"
    legend_constants[2] = "Ki_MATI in component V_MATI (micromolar)"
    legend_constants[3] = "V_MATIIImax in component V_MATIII (flux)"
    legend_algebraic[2] = "Km1_MATIII in component V_MATIII (micromolar)"
    legend_constants[4] = "Km2_MATIII in component V_MATIII (micromolar)"
    legend_constants[5] = "V_GNMTmax in component V_GNMT (flux)"
    legend_constants[6] = "Km_GNMT in component V_GNMT (micromolar)"
    legend_constants[7] = "Ki_GNMT in component V_GNMT (micromolar)"
    legend_constants[8] = "V_METHmax in component V_METH (flux)"
    legend_algebraic[5] = "Km1_METH in component V_METH (micromolar)"
    legend_constants[9] = "Km2_METH_A in component V_METH (dimensionless)"
    legend_constants[10] = "five_mTHF in component V_MS (micromolar)"
    legend_constants[11] = "V_MSmax in component V_MS (flux)"
    legend_constants[12] = "Kd_MS in component V_MS (micromolar)"
    legend_constants[13] = "Km_Hcy_MS in component V_MS (micromolar)"
    legend_constants[14] = "Km_five_mTHF_MS in component V_MS (micromolar)"
    legend_constants[15] = "alpha1 in component V_AH (first_order_rate_constant)"
    legend_constants[16] = "alpha2 in component V_AH (dimensionless)"
    legend_constants[17] = "beta1 in component V_CBS (second_order_rate_constant)"
    legend_constants[18] = "beta2 in component V_CBS (first_order_rate_constant)"
    legend_constants[19] = "V_BHMTmax in component V_BHMT (flux)"
    legend_constants[20] = "Km_BHMT in component V_BHMT (micromolar)"
    legend_rates[0] = "d/dt Met in component Met (micromolar)"
    legend_rates[1] = "d/dt AdoMet in component AdoMet (micromolar)"
    legend_rates[2] = "d/dt AdoHcy in component AdoHcy (micromolar)"
    legend_rates[3] = "d/dt Hcy in component Hcy (micromolar)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 53.5
    states[1] = 137.6
    states[2] = 13.2
    states[3] = 0.88
    constants[0] = 561
    constants[1] = 41
    constants[2] = 50
    constants[3] = 22870
    constants[4] = 21.1
    constants[5] = 10600
    constants[6] = 4500
    constants[7] = 20
    constants[8] = 4521
    constants[9] = 10
    constants[10] = 5.2
    constants[11] = 500
    constants[12] = 1
    constants[13] = 0.1
    constants[14] = 25
    constants[15] = 100
    constants[16] = 10
    constants[17] = 1.7
    constants[18] = 30
    constants[19] = 2500
    constants[20] = 12
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[1] = constants[0]/(1.00000+(constants[1]/states[0])*(1.00000+states[1]/constants[2]))
    algebraic[2] = 20000.0/(1.00000+5.70000*(power(states[1]/(states[1]+600.000), 2.00000)))
    algebraic[3] = constants[3]/(1.00000+(algebraic[2]*constants[4])/(power(states[0], 2.00000)+states[0]*constants[4]))
    algebraic[5] = 1.00000*(1.00000+states[2]/4.00000)
    algebraic[6] = constants[8]/(1.00000+algebraic[5]/states[1]+constants[9]+(constants[9]*algebraic[5])/states[1])
    algebraic[4] = ((constants[5]/(1.00000+power(constants[6]/states[1], 2.30000)))*1.00000)/(1.00000+states[2]/constants[7])
    rates[1] = (algebraic[1]+algebraic[3])-(algebraic[6]+algebraic[4])
    algebraic[8] = constants[15]*(states[2]-constants[16]*states[3])
    rates[2] = (algebraic[6]+algebraic[4])-algebraic[8]
    algebraic[0] = custom_piecewise([less(voi , 2.00000) | greater_equal(voi , 8.00000), 200.000 , greater_equal(voi , 2.00000) & less(voi , 5.00000), 300.000 , greater_equal(voi , 5.00000) & less(voi , 8.00000), 100.000 , True, 200.000])
    algebraic[7] = (constants[11]*constants[10]*states[3])/(constants[12]*constants[13]+constants[13]*constants[10]+constants[14]*states[3]+constants[10]*states[3])
    algebraic[10] = ((0.700000-0.0250000*((states[1]+states[2])-150.000))*constants[19]*states[3])/(constants[20]+states[3])
    rates[0] = (algebraic[7]+algebraic[10]+algebraic[0])-(algebraic[1]+algebraic[3])
    algebraic[9] = (constants[17]*(states[1]+states[2])-constants[18])*states[3]
    rates[3] = algebraic[8]-(algebraic[9]+algebraic[7]+algebraic[10])
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[1] = constants[0]/(1.00000+(constants[1]/states[0])*(1.00000+states[1]/constants[2]))
    algebraic[2] = 20000.0/(1.00000+5.70000*(power(states[1]/(states[1]+600.000), 2.00000)))
    algebraic[3] = constants[3]/(1.00000+(algebraic[2]*constants[4])/(power(states[0], 2.00000)+states[0]*constants[4]))
    algebraic[5] = 1.00000*(1.00000+states[2]/4.00000)
    algebraic[6] = constants[8]/(1.00000+algebraic[5]/states[1]+constants[9]+(constants[9]*algebraic[5])/states[1])
    algebraic[4] = ((constants[5]/(1.00000+power(constants[6]/states[1], 2.30000)))*1.00000)/(1.00000+states[2]/constants[7])
    algebraic[8] = constants[15]*(states[2]-constants[16]*states[3])
    algebraic[0] = custom_piecewise([less(voi , 2.00000) | greater_equal(voi , 8.00000), 200.000 , greater_equal(voi , 2.00000) & less(voi , 5.00000), 300.000 , greater_equal(voi , 5.00000) & less(voi , 8.00000), 100.000 , True, 200.000])
    algebraic[7] = (constants[11]*constants[10]*states[3])/(constants[12]*constants[13]+constants[13]*constants[10]+constants[14]*states[3]+constants[10]*states[3])
    algebraic[10] = ((0.700000-0.0250000*((states[1]+states[2])-150.000))*constants[19]*states[3])/(constants[20]+states[3])
    algebraic[9] = (constants[17]*(states[1]+states[2])-constants[18])*states[3]
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
        self.V_MATImax = 561
        self.Km_MATI = 41
        self.Ki_MATI = 50
        self.V_MATIIImax = 22870
        self.Km2_MATIII = 21.1
        self.V_GNMTmax = 10600
        self.Km_GNMT = 4500
        self.Ki_GNMT = 20
        self.V_METHmax = 4521
        self.Km2_METH_A = 10
        self.five_mTHF = 5.2
        self.V_MSmax = 500
        self.Kd_MS = 1
        self.Km_Hcy_MS = 0.1
        self.Km_five_mTHF_MS = 25
        self.alpha1 = 100
        self.alpha2 = 10
        self.beta1 = 1.7
        self.beta2 = 30
        self.V_BHMTmax = 2500
        self.Km_BHMT = 12

    def to_dict(self):
        return {
            "V_MATImax": self.V_MATImax,
            "Km_MATI": self.Km_MATI,
            "Ki_MATI": self.Ki_MATI,
            "V_MATIIImax": self.V_MATIIImax,
            "Km2_MATIII": self.Km2_MATIII,
            "V_GNMTmax": self.V_GNMTmax,
            "Km_GNMT": self.Km_GNMT,
            "Ki_GNMT": self.Ki_GNMT,
            "V_METHmax": self.V_METHmax,
            "Km2_METH_A": self.Km2_METH_A,
            "five_mTHF": self.five_mTHF,
            "V_MSmax": self.V_MSmax,
            "Kd_MS": self.Kd_MS,
            "Km_Hcy_MS": self.Km_Hcy_MS,
            "Km_five_mTHF_MS": self.Km_five_mTHF_MS,
            "alpha1": self.alpha1,
            "alpha2": self.alpha2,
            "beta1": self.beta1,
            "beta2": self.beta2,
            "V_BHMTmax": self.V_BHMTmax,
            "Km_BHMT": self.Km_BHMT,
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
        y0=[53.5, 137.6, 13.2, 0.88],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "reed_nijhout_sparks_ulrich_2004"
        self.curve_names = [
            "Met",
            "AdoMet",
            "AdoHcy",
            "Hcy",
        ]
        self.state_names = ['Met', 'AdoMet', 'AdoHcy', 'Hcy']
        self.algebraic_names = ['Metin', 'V_MATI', 'Km1_MATIII', 'V_MATIII', 'V_GNMT', 'Km1_METH', 'V_METH', 'V_MS', 'V_AH', 'V_CBS', 'V_BHMT']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 21
        p = self.params

        # direct mapping
        c[0] = p.V_MATImax
        c[1] = p.Km_MATI
        c[2] = p.Ki_MATI
        c[3] = p.V_MATIIImax
        c[4] = p.Km2_MATIII
        c[5] = p.V_GNMTmax
        c[6] = p.Km_GNMT
        c[7] = p.Ki_GNMT
        c[8] = p.V_METHmax
        c[9] = p.Km2_METH_A
        c[10] = p.five_mTHF
        c[11] = p.V_MSmax
        c[12] = p.Kd_MS
        c[13] = p.Km_Hcy_MS
        c[14] = p.Km_five_mTHF_MS
        c[15] = p.alpha1
        c[16] = p.alpha2
        c[17] = p.beta1
        c[18] = p.beta2
        c[19] = p.V_BHMTmax
        c[20] = p.Km_BHMT

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
