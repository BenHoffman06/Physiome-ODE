# Size of variable arrays:
sizeAlgebraic = 9
sizeStates = 2
sizeConstants = 13
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (hour)"
    legend_constants[0] = "Ado in component Ado (micromolar)"
    legend_algebraic[0] = "Met in component Met (micromolar)"
    legend_algebraic[1] = "Hcy in component Hcy (micromolar)"
    legend_states[0] = "AdoHcy in component AdoHcy (micromolar)"
    legend_constants[1] = "K_AHC in component K_AHC (micromolar)"
    legend_states[1] = "AdoMet in component AdoMet (micromolar)"
    legend_algebraic[6] = "V_MET in component V_MET (flux)"
    legend_algebraic[7] = "V_GNMT in component V_GNMT (flux)"
    legend_algebraic[2] = "V_MATI in component V_MATI (flux)"
    legend_algebraic[4] = "V_MATIII in component V_MATIII (flux)"
    legend_algebraic[8] = "V_D in component V_D (flux)"
    legend_constants[2] = "V_MATImax in component V_MATI (flux)"
    legend_constants[3] = "Km_MATI in component V_MATI (micromolar)"
    legend_constants[4] = "Ki_MATI in component V_MATI (micromolar)"
    legend_constants[5] = "V_MATIIImax in component V_MATIII (flux)"
    legend_algebraic[3] = "Km1_MATIII in component V_MATIII (micromolar)"
    legend_constants[6] = "Km2_MATIII in component V_MATIII (micromolar)"
    legend_constants[7] = "V_METmax in component V_MET (flux)"
    legend_algebraic[5] = "Km1_MET in component V_MET (micromolar)"
    legend_constants[8] = "Km2_MET_A in component V_MET (dimensionless)"
    legend_constants[9] = "V_GNMTmax in component V_GNMT (flux)"
    legend_constants[10] = "Km_GNMT in component V_GNMT (micromolar)"
    legend_constants[11] = "Ki_GNMT in component V_GNMT (micromolar)"
    legend_constants[12] = "alpha_d in component V_D (first_order_rate_constant)"
    legend_rates[1] = "d/dt AdoMet in component AdoMet (micromolar)"
    legend_rates[0] = "d/dt AdoHcy in component AdoHcy (micromolar)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    constants[0] = 1
    states[0] = 3
    constants[1] = 0.1
    states[1] = 60
    constants[2] = 561
    constants[3] = 41
    constants[4] = 50
    constants[5] = 22870
    constants[6] = 21.1
    constants[7] = 4544
    constants[8] = 10
    constants[9] = 10600
    constants[10] = 4500
    constants[11] = 20
    constants[12] = 1333
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[5] = 10.0000*(1.00000+states[0]/4.00000)
    algebraic[6] = constants[7]/(1.00000+algebraic[5]/states[1]+constants[8]+(constants[8]*algebraic[5])/states[1])
    algebraic[7] = ((constants[9]/(1.00000+power(constants[10]/states[1], 2.30000)))*1.00000)/(1.00000+states[0]/constants[11])
    algebraic[0] = custom_piecewise([greater_equal(voi , 0.00000) & less(voi , 5.00000), 45.0000 , greater_equal(voi , 5.00000) & less(voi , 15.0000), 52.0000 , greater_equal(voi , 15.0000) & less(voi , 60.0000), 55.0000 , greater_equal(voi , 60.0000) & less(voi , 75.0000), 52.0000 , greater_equal(voi , 75.0000), 45.0000 , True, float('nan')])
    algebraic[2] = constants[2]/(1.00000+(constants[3]/algebraic[0])*(1.00000+states[1]/constants[4]))
    algebraic[3] = 20000.0/(1.00000+5.70000*(power(states[1]/(states[1]+600.000), 2.00000)))
    algebraic[4] = constants[5]/(1.00000+(algebraic[3]*constants[6])/(power(algebraic[0], 2.00000)+algebraic[0]*constants[6]))
    rates[1] = (algebraic[2]+algebraic[4])-(algebraic[6]+algebraic[7])
    algebraic[1] = (states[0]*constants[1])/constants[0]
    algebraic[8] = constants[12]*algebraic[1]
    rates[0] = ((algebraic[6]+algebraic[7])-algebraic[8])/(1.00000+constants[1]/constants[0])
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[5] = 10.0000*(1.00000+states[0]/4.00000)
    algebraic[6] = constants[7]/(1.00000+algebraic[5]/states[1]+constants[8]+(constants[8]*algebraic[5])/states[1])
    algebraic[7] = ((constants[9]/(1.00000+power(constants[10]/states[1], 2.30000)))*1.00000)/(1.00000+states[0]/constants[11])
    algebraic[0] = custom_piecewise([greater_equal(voi , 0.00000) & less(voi , 5.00000), 45.0000 , greater_equal(voi , 5.00000) & less(voi , 15.0000), 52.0000 , greater_equal(voi , 15.0000) & less(voi , 60.0000), 55.0000 , greater_equal(voi , 60.0000) & less(voi , 75.0000), 52.0000 , greater_equal(voi , 75.0000), 45.0000 , True, float('nan')])
    algebraic[2] = constants[2]/(1.00000+(constants[3]/algebraic[0])*(1.00000+states[1]/constants[4]))
    algebraic[3] = 20000.0/(1.00000+5.70000*(power(states[1]/(states[1]+600.000), 2.00000)))
    algebraic[4] = constants[5]/(1.00000+(algebraic[3]*constants[6])/(power(algebraic[0], 2.00000)+algebraic[0]*constants[6]))
    algebraic[1] = (states[0]*constants[1])/constants[0]
    algebraic[8] = constants[12]*algebraic[1]
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
        self.Ado = 1
        self.K_AHC = 0.1
        self.V_MATImax = 561
        self.Km_MATI = 41
        self.Ki_MATI = 50
        self.V_MATIIImax = 22870
        self.Km2_MATIII = 21.1
        self.V_METmax = 4544
        self.Km2_MET_A = 10
        self.V_GNMTmax = 10600
        self.Km_GNMT = 4500
        self.Ki_GNMT = 20
        self.alpha_d = 1333

    def to_dict(self):
        return {
            "Ado": self.Ado,
            "K_AHC": self.K_AHC,
            "V_MATImax": self.V_MATImax,
            "Km_MATI": self.Km_MATI,
            "Ki_MATI": self.Ki_MATI,
            "V_MATIIImax": self.V_MATIIImax,
            "Km2_MATIII": self.Km2_MATIII,
            "V_METmax": self.V_METmax,
            "Km2_MET_A": self.Km2_MET_A,
            "V_GNMTmax": self.V_GNMTmax,
            "Km_GNMT": self.Km_GNMT,
            "Ki_GNMT": self.Ki_GNMT,
            "alpha_d": self.alpha_d,
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
        y0=[3, 60],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "martinov_vitvitsky_mosharov_banerjee_ataullakhanov_2000"
        self.curve_names = [
            "AdoHcy",
            "AdoMet",
        ]
        self.state_names = ['AdoHcy', 'AdoMet']
        self.algebraic_names = ['Met', 'Hcy', 'V_MATI', 'Km1_MATIII', 'V_MATIII', 'Km1_MET', 'V_MET', 'V_GNMT', 'V_D']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 13
        p = self.params

        # direct mapping
        c[0] = p.Ado
        c[1] = p.K_AHC
        c[2] = p.V_MATImax
        c[3] = p.Km_MATI
        c[4] = p.Ki_MATI
        c[5] = p.V_MATIIImax
        c[6] = p.Km2_MATIII
        c[7] = p.V_METmax
        c[8] = p.Km2_MET_A
        c[9] = p.V_GNMTmax
        c[10] = p.Km_GNMT
        c[11] = p.Ki_GNMT
        c[12] = p.alpha_d

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
