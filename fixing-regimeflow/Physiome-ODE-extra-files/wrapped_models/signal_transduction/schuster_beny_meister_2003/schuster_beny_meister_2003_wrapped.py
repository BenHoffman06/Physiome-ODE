# Size of variable arrays:
sizeAlgebraic = 4
sizeStates = 3
sizeConstants = 25
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (second)"
    legend_states[0] = "Vm in component membrane (millivolt)"
    legend_constants[0] = "C in component membrane (picoF)"
    legend_algebraic[2] = "i_K in component potassium_current (picoA)"
    legend_algebraic[3] = "i_R in component repolarising_current (picoA)"
    legend_states[1] = "IP3 in component IP3 (nanomolar)"
    legend_constants[1] = "m3IP3 in component IP3 (dimensionless)"
    legend_constants[2] = "m4IP3 in component IP3 (dimensionless)"
    legend_constants[3] = "kIP3 in component IP3 (first_order_rate_constant)"
    legend_constants[4] = "A in component IP3 (dimensionless)"
    legend_states[2] = "Ca in component Ca (nanomolar)"
    legend_constants[5] = "m3SR in component Ca (dimensionless)"
    legend_constants[6] = "m4SR in component Ca (dimensionless)"
    legend_constants[7] = "m3PMCA in component Ca (dimensionless)"
    legend_constants[8] = "m4PMCA in component Ca (dimensionless)"
    legend_constants[9] = "kSR_rel in component Ca (flux)"
    legend_constants[10] = "kPMCA in component Ca (flux)"
    legend_algebraic[1] = "Jcat in component Jcat (flux)"
    legend_constants[11] = "ECa in component Jcat (millivolt)"
    legend_constants[12] = "Gcat in component Jcat (nanomolar_per_millivolt_second)"
    legend_constants[13] = "m3cat in component Jcat (dimensionless)"
    legend_constants[14] = "m4cat in component Jcat (dimensionless)"
    legend_constants[15] = "Gtot in component potassium_current (picoS)"
    legend_algebraic[0] = "PoBKCa in component potassium_current (dimensionless)"
    legend_constants[16] = "PoSKCa in component potassium_current (dimensionless)"
    legend_constants[17] = "E_K in component potassium_current (millivolt)"
    legend_constants[18] = "a in component potassium_current (dimensionless)"
    legend_constants[19] = "b in component potassium_current (dimensionless)"
    legend_constants[20] = "c in component potassium_current (dimensionless)"
    legend_constants[21] = "m3 in component potassium_current (dimensionless)"
    legend_constants[22] = "m4 in component potassium_current (dimensionless)"
    legend_constants[23] = "GR in component repolarising_current (picoS)"
    legend_constants[24] = "Vrest in component repolarising_current (millivolt)"
    legend_rates[0] = "d/dt Vm in component membrane (millivolt)"
    legend_rates[1] = "d/dt IP3 in component IP3 (nanomolar)"
    legend_rates[2] = "d/dt Ca in component Ca (nanomolar)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = -31.1
    constants[0] = 1.0
    states[1] = 1.0
    constants[1] = 4.0
    constants[2] = 55.0
    constants[3] = 0.1733
    constants[4] = 0.211
    states[2] = 50.0
    constants[5] = 1.1
    constants[6] = 0.3
    constants[7] = -6.19
    constants[8] = 0.39
    constants[9] = 180.0
    constants[10] = 0.679
    constants[11] = 50.0
    constants[12] = 0.66
    constants[13] = -6.18
    constants[14] = 0.37
    constants[15] = 6927
    constants[16] = 0.5
    constants[17] = -80.0
    constants[18] = 53.3
    constants[19] = -80.8
    constants[20] = -6.4
    constants[21] = 1.32E-3
    constants[22] = 0.30
    constants[23] = 955.0
    constants[24] = -31.1
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[1] = constants[4]*(1.00000+tanh((constants[1]-voi)/constants[2]))-constants[3]*states[1]
    rates[2] = (constants[9]/2.00000)*(1.00000+tanh((states[1]-constants[5])/constants[6]))-(constants[10]/2.00000)*(1.00000+tanh((log(states[2], 10)-constants[7])/constants[8]))
    algebraic[0] = 0.500000*(1.00000+tanh(((log(states[2], 10)-constants[20])*(states[0]-constants[19])-constants[18])/(constants[21]*(power((states[0]+constants[18]*(log(states[2], 10)-constants[20]))-constants[19], 2.00000))+constants[22])))
    algebraic[2] = constants[15]*(states[0]-constants[17])*(0.400000*algebraic[0]+0.600000*constants[16])
    algebraic[3] = constants[23]*(states[0]-constants[24])
    rates[0] = -(1.00000/constants[0])*(algebraic[2]+algebraic[3])
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = 0.500000*(1.00000+tanh(((log(states[2], 10)-constants[20])*(states[0]-constants[19])-constants[18])/(constants[21]*(power((states[0]+constants[18]*(log(states[2], 10)-constants[20]))-constants[19], 2.00000))+constants[22])))
    algebraic[2] = constants[15]*(states[0]-constants[17])*(0.400000*algebraic[0]+0.600000*constants[16])
    algebraic[3] = constants[23]*(states[0]-constants[24])
    algebraic[1] = (constants[12]*(constants[11]-states[0]))*(0.500000*(1.00000+tanh((log(states[2], 10)-constants[13])/constants[14])))
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
        self.C = 1.0
        self.m3IP3 = 4.0
        self.m4IP3 = 55.0
        self.kIP3 = 0.1733
        self.A = 0.211
        self.m3SR = 1.1
        self.m4SR = 0.3
        self.m3PMCA = -6.19
        self.m4PMCA = 0.39
        self.kSR_rel = 180.0
        self.kPMCA = 0.679
        self.ECa = 50.0
        self.Gcat = 0.66
        self.m3cat = -6.18
        self.m4cat = 0.37
        self.Gtot = 6927
        self.PoSKCa = 0.5
        self.E_K = -80.0
        self.a = 53.3
        self.b = -80.8
        self.c = -6.4
        self.m3 = 1.32E-3
        self.m4 = 0.30
        self.GR = 955.0
        self.Vrest = -31.1

    def to_dict(self):
        return {
            "C": self.C,
            "m3IP3": self.m3IP3,
            "m4IP3": self.m4IP3,
            "kIP3": self.kIP3,
            "A": self.A,
            "m3SR": self.m3SR,
            "m4SR": self.m4SR,
            "m3PMCA": self.m3PMCA,
            "m4PMCA": self.m4PMCA,
            "kSR_rel": self.kSR_rel,
            "kPMCA": self.kPMCA,
            "ECa": self.ECa,
            "Gcat": self.Gcat,
            "m3cat": self.m3cat,
            "m4cat": self.m4cat,
            "Gtot": self.Gtot,
            "PoSKCa": self.PoSKCa,
            "E_K": self.E_K,
            "a": self.a,
            "b": self.b,
            "c": self.c,
            "m3": self.m3,
            "m4": self.m4,
            "GR": self.GR,
            "Vrest": self.Vrest,
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
        y0=[-31.1, 1.0, 50.0],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "schuster_beny_meister_2003"
        self.curve_names = [
            "Vm",
            "IP3",
            "Ca",
        ]
        self.state_names = ['Vm', 'IP3', 'Ca']
        self.algebraic_names = ['PoBKCa', 'Jcat', 'i_K', 'i_R']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 25
        p = self.params

        # direct mapping
        c[0] = p.C
        c[1] = p.m3IP3
        c[2] = p.m4IP3
        c[3] = p.kIP3
        c[4] = p.A
        c[5] = p.m3SR
        c[6] = p.m4SR
        c[7] = p.m3PMCA
        c[8] = p.m4PMCA
        c[9] = p.kSR_rel
        c[10] = p.kPMCA
        c[11] = p.ECa
        c[12] = p.Gcat
        c[13] = p.m3cat
        c[14] = p.m4cat
        c[15] = p.Gtot
        c[16] = p.PoSKCa
        c[17] = p.E_K
        c[18] = p.a
        c[19] = p.b
        c[20] = p.c
        c[21] = p.m3
        c[22] = p.m4
        c[23] = p.GR
        c[24] = p.Vrest

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
