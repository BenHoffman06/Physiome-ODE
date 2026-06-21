# Size of variable arrays:
sizeAlgebraic = 8
sizeStates = 6
sizeConstants = 21
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (min)"
    legend_constants[0] = "Vp in component environment (l)"
    legend_constants[1] = "Vi in component environment (l)"
    legend_constants[2] = "Vg in component environment (l)"
    legend_constants[3] = "E in component environment (l_per_min)"
    legend_states[0] = "Ip in component plasma_insulin (mU)"
    legend_algebraic[0] = "Ip_conc in component plasma_insulin (mU_per_l)"
    legend_constants[4] = "tp in component plasma_insulin (min)"
    legend_algebraic[1] = "f1_G in component plasma_insulin (mU_per_min)"
    legend_constants[5] = "Rm in component plasma_insulin (mU_per_min)"
    legend_constants[6] = "C1 in component plasma_insulin (mg_per_l)"
    legend_constants[7] = "a1 in component plasma_insulin (mg_per_l)"
    legend_states[1] = "Ii in component intercellular_insulin (mU)"
    legend_states[2] = "G in component glucose (mg)"
    legend_algebraic[2] = "Ii_conc in component intercellular_insulin (mU_per_l)"
    legend_constants[8] = "ti in component intercellular_insulin (min)"
    legend_algebraic[3] = "G_conc in component glucose (mg_per_dl)"
    legend_constants[9] = "Gin in component glucose (mg_per_min)"
    legend_algebraic[4] = "f2_G in component glucose (mg_per_min)"
    legend_algebraic[5] = "f3_G in component glucose (dimensionless)"
    legend_algebraic[6] = "f4_Ii in component glucose (mg_per_min)"
    legend_algebraic[7] = "f5_x3 in component glucose (mg_per_min)"
    legend_constants[10] = "C2 in component glucose (mg_per_l)"
    legend_constants[11] = "C3 in component glucose (mg_per_l)"
    legend_constants[12] = "C4 in component glucose (mU_per_l)"
    legend_constants[13] = "C5 in component glucose (mU_per_l)"
    legend_constants[14] = "U0 in component glucose (mg_per_min)"
    legend_constants[15] = "Um in component glucose (mg_per_min)"
    legend_constants[16] = "Ub in component glucose (mg_per_min)"
    legend_constants[17] = "beta in component glucose (dimensionless)"
    legend_constants[18] = "Rg in component glucose (mg_per_min)"
    legend_constants[19] = "alpha in component glucose (l_per_mU)"
    legend_states[3] = "x3 in component delay (min)"
    legend_constants[20] = "td in component delay (min)"
    legend_states[4] = "x1 in component delay (min)"
    legend_states[5] = "x2 in component delay (min)"
    legend_rates[0] = "d/dt Ip in component plasma_insulin (mU)"
    legend_rates[1] = "d/dt Ii in component intercellular_insulin (mU)"
    legend_rates[2] = "d/dt G in component glucose (mg)"
    legend_rates[4] = "d/dt x1 in component delay (min)"
    legend_rates[5] = "d/dt x2 in component delay (min)"
    legend_rates[3] = "d/dt x3 in component delay (min)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    constants[0] = 3
    constants[1] = 11
    constants[2] = 10
    constants[3] = 0.2
    states[0] = 93.36441699
    constants[4] = 6
    constants[5] = 210
    constants[6] = 2000
    constants[7] = 300
    states[1] = 243.2865183
    states[2] = 12342.61665
    constants[8] = 100
    constants[9] = 216
    constants[10] = 144
    constants[11] = 1000
    constants[12] = 80
    constants[13] = 26
    constants[14] = 40
    constants[15] = 940
    constants[16] = 72
    constants[17] = 1.77
    constants[18] = 180
    constants[19] = 0.29
    states[3] = 104.5878705
    constants[20] = 36
    states[4] = 110.420253
    states[5] = 112.7601171
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[1] = constants[3]*(states[0]/constants[0]-states[1]/constants[1])-states[1]/constants[8]
    rates[4] = (3.00000/constants[20])*(states[0]/1.00000-states[4])
    rates[5] = (3.00000/constants[20])*(states[4]-states[5])
    rates[3] = (3.00000/constants[20])*(states[5]-states[3])
    algebraic[1] = constants[5]/(1.00000+exp((constants[6]-states[2]/constants[2])/constants[7]))
    rates[0] = algebraic[1]-(constants[3]*(states[0]/constants[0]-states[1]/constants[1])+states[0]/constants[4])
    algebraic[4] = constants[16]*(1.00000-exp(-states[2]/(constants[10]*constants[2])))
    algebraic[5] = states[2]/(constants[11]*constants[2])
    algebraic[6] = constants[14]+(constants[15]-constants[14])/(1.00000+exp(-constants[17]*log((states[1]/constants[12])*(1.00000/constants[1]+1.00000/(constants[3]*constants[8])))))
    algebraic[7] = constants[18]/(1.00000+exp(constants[19]*((states[3]*1.00000)/constants[0]-constants[13])))
    rates[2] = constants[9]+algebraic[7]+-(algebraic[4]+algebraic[5]*algebraic[6])
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[1] = constants[5]/(1.00000+exp((constants[6]-states[2]/constants[2])/constants[7]))
    algebraic[4] = constants[16]*(1.00000-exp(-states[2]/(constants[10]*constants[2])))
    algebraic[5] = states[2]/(constants[11]*constants[2])
    algebraic[6] = constants[14]+(constants[15]-constants[14])/(1.00000+exp(-constants[17]*log((states[1]/constants[12])*(1.00000/constants[1]+1.00000/(constants[3]*constants[8])))))
    algebraic[7] = constants[18]/(1.00000+exp(constants[19]*((states[3]*1.00000)/constants[0]-constants[13])))
    algebraic[0] = states[0]/constants[0]
    algebraic[2] = states[1]/constants[1]
    algebraic[3] = states[2]/(constants[2]*10.0000)
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
        self.Vp = 3
        self.Vi = 11
        self.Vg = 10
        self.E = 0.2
        self.tp = 6
        self.Rm = 210
        self.C1 = 2000
        self.a1 = 300
        self.ti = 100
        self.Gin = 216
        self.C2 = 144
        self.C3 = 1000
        self.C4 = 80
        self.C5 = 26
        self.U0 = 40
        self.Um = 940
        self.Ub = 72
        self.beta = 1.77
        self.Rg = 180
        self.alpha = 0.29
        self.td = 36

    def to_dict(self):
        return {
            "Vp": self.Vp,
            "Vi": self.Vi,
            "Vg": self.Vg,
            "E": self.E,
            "tp": self.tp,
            "Rm": self.Rm,
            "C1": self.C1,
            "a1": self.a1,
            "ti": self.ti,
            "Gin": self.Gin,
            "C2": self.C2,
            "C3": self.C3,
            "C4": self.C4,
            "C5": self.C5,
            "U0": self.U0,
            "Um": self.Um,
            "Ub": self.Ub,
            "beta": self.beta,
            "Rg": self.Rg,
            "alpha": self.alpha,
            "td": self.td,
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
        y0=[93.36441699, 243.2865183, 12342.61665, 104.5878705, 110.420253, 112.7601171],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "tolic_mosekilde_sturis_2000"
        self.curve_names = [
            "Ip",
            "Ii",
            "G",
            "x3",
            "x1",
            "x2",
        ]
        self.state_names = ['Ip', 'Ii', 'G', 'x3', 'x1', 'x2']
        self.algebraic_names = ['Ip_conc', 'f1_G', 'Ii_conc', 'G_conc', 'f2_G', 'f3_G', 'f4_Ii', 'f5_x3']
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
        c[0] = p.Vp
        c[1] = p.Vi
        c[2] = p.Vg
        c[3] = p.E
        c[4] = p.tp
        c[5] = p.Rm
        c[6] = p.C1
        c[7] = p.a1
        c[8] = p.ti
        c[9] = p.Gin
        c[10] = p.C2
        c[11] = p.C3
        c[12] = p.C4
        c[13] = p.C5
        c[14] = p.U0
        c[15] = p.Um
        c[16] = p.Ub
        c[17] = p.beta
        c[18] = p.Rg
        c[19] = p.alpha
        c[20] = p.td

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
