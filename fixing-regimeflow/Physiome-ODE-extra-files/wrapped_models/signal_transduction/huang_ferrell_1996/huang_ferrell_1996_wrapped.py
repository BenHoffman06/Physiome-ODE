# Size of variable arrays:
sizeAlgebraic = 0
sizeStates = 18
sizeConstants = 37
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (second)"
    legend_constants[0] = "mostot in component total_concs (micromolar)"
    legend_constants[1] = "e1tot in component total_concs (micromolar)"
    legend_constants[2] = "e2tot in component total_concs (micromolar)"
    legend_constants[3] = "mektot in component total_concs (micromolar)"
    legend_constants[4] = "mekpasetot in component total_concs (micromolar)"
    legend_constants[5] = "mapktot in component total_concs (micromolar)"
    legend_constants[6] = "mapkpasetot in component total_concs (micromolar)"
    legend_constants[7] = "a1 in component rate_constants (second_order_rate_constant_units)"
    legend_constants[8] = "a2 in component rate_constants (second_order_rate_constant_units)"
    legend_constants[9] = "a3 in component rate_constants (second_order_rate_constant_units)"
    legend_constants[10] = "a4 in component rate_constants (second_order_rate_constant_units)"
    legend_constants[11] = "a5 in component rate_constants (second_order_rate_constant_units)"
    legend_constants[12] = "a6 in component rate_constants (second_order_rate_constant_units)"
    legend_constants[13] = "a7 in component rate_constants (second_order_rate_constant_units)"
    legend_constants[14] = "a8 in component rate_constants (second_order_rate_constant_units)"
    legend_constants[15] = "a9 in component rate_constants (second_order_rate_constant_units)"
    legend_constants[16] = "a10 in component rate_constants (second_order_rate_constant_units)"
    legend_constants[17] = "d1 in component rate_constants (first_order_rate_constant_units)"
    legend_constants[18] = "d2 in component rate_constants (first_order_rate_constant_units)"
    legend_constants[19] = "d3 in component rate_constants (first_order_rate_constant_units)"
    legend_constants[20] = "d4 in component rate_constants (first_order_rate_constant_units)"
    legend_constants[21] = "d5 in component rate_constants (first_order_rate_constant_units)"
    legend_constants[22] = "d6 in component rate_constants (first_order_rate_constant_units)"
    legend_constants[23] = "d7 in component rate_constants (first_order_rate_constant_units)"
    legend_constants[24] = "d8 in component rate_constants (first_order_rate_constant_units)"
    legend_constants[25] = "d9 in component rate_constants (first_order_rate_constant_units)"
    legend_constants[26] = "d10 in component rate_constants (first_order_rate_constant_units)"
    legend_constants[27] = "k1 in component rate_constants (first_order_rate_constant_units)"
    legend_constants[28] = "k2 in component rate_constants (first_order_rate_constant_units)"
    legend_constants[29] = "k3 in component rate_constants (first_order_rate_constant_units)"
    legend_constants[30] = "k4 in component rate_constants (first_order_rate_constant_units)"
    legend_constants[31] = "k5 in component rate_constants (first_order_rate_constant_units)"
    legend_constants[32] = "k6 in component rate_constants (first_order_rate_constant_units)"
    legend_constants[33] = "k7 in component rate_constants (first_order_rate_constant_units)"
    legend_constants[34] = "k8 in component rate_constants (first_order_rate_constant_units)"
    legend_constants[35] = "k9 in component rate_constants (first_order_rate_constant_units)"
    legend_constants[36] = "k10 in component rate_constants (first_order_rate_constant_units)"
    legend_states[0] = "mos in component mos (micromolar)"
    legend_states[1] = "mosstar in component mosstar (micromolar)"
    legend_states[2] = "mose1 in component mose1 (micromolar)"
    legend_states[3] = "mosstare2 in component mosstare2 (micromolar)"
    legend_states[4] = "mekstarmosstar in component mekstarmosstar (micromolar)"
    legend_states[5] = "mekmosstar in component mekmosstar (micromolar)"
    legend_states[6] = "mekstar in component mekstar (micromolar)"
    legend_states[7] = "mekstarstar in component mekstarstar (micromolar)"
    legend_states[8] = "mekstarmekpase in component mekstarmekpase (micromolar)"
    legend_states[9] = "mekstarstarmekpase in component mekstarstarmekpase (micromolar)"
    legend_states[10] = "mapkmekstarstar in component mapkmekstarstar (micromolar)"
    legend_states[11] = "mapkstarmekstarstar in component mapkstarmekstarstar (micromolar)"
    legend_states[12] = "mek in component mek (micromolar)"
    legend_states[13] = "mapkstar in component mapkstar (micromolar)"
    legend_states[14] = "mapkstarstar in component mapkstarstar (micromolar)"
    legend_states[15] = "mapkstarmapkpase in component mapkstarmapkpase (micromolar)"
    legend_states[16] = "mapkstarstarmapkpase in component mapkstarstarmapkpase (micromolar)"
    legend_states[17] = "mapk in component mapk (micromolar)"
    legend_rates[0] = "d/dt mos in component mos (micromolar)"
    legend_rates[2] = "d/dt mose1 in component mose1 (micromolar)"
    legend_rates[1] = "d/dt mosstar in component mosstar (micromolar)"
    legend_rates[3] = "d/dt mosstare2 in component mosstare2 (micromolar)"
    legend_rates[12] = "d/dt mek in component mek (micromolar)"
    legend_rates[5] = "d/dt mekmosstar in component mekmosstar (micromolar)"
    legend_rates[6] = "d/dt mekstar in component mekstar (micromolar)"
    legend_rates[8] = "d/dt mekstarmekpase in component mekstarmekpase (micromolar)"
    legend_rates[4] = "d/dt mekstarmosstar in component mekstarmosstar (micromolar)"
    legend_rates[7] = "d/dt mekstarstar in component mekstarstar (micromolar)"
    legend_rates[9] = "d/dt mekstarstarmekpase in component mekstarstarmekpase (micromolar)"
    legend_rates[17] = "d/dt mapk in component mapk (micromolar)"
    legend_rates[10] = "d/dt mapkmekstarstar in component mapkmekstarstar (micromolar)"
    legend_rates[13] = "d/dt mapkstar in component mapkstar (micromolar)"
    legend_rates[11] = "d/dt mapkstarmekstarstar in component mapkstarmekstarstar (micromolar)"
    legend_rates[14] = "d/dt mapkstarstar in component mapkstarstar (micromolar)"
    legend_rates[15] = "d/dt mapkstarmapkpase in component mapkstarmapkpase (micromolar)"
    legend_rates[16] = "d/dt mapkstarstarmapkpase in component mapkstarstarmapkpase (micromolar)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    constants[0] = 0.003
    constants[1] = 0.0003
    constants[2] = 0.0003
    constants[3] = 1.2
    constants[4] = 0.0003
    constants[5] = 1.2
    constants[6] = 0.12
    constants[7] = 1000
    constants[8] = 1000
    constants[9] = 1000
    constants[10] = 1000
    constants[11] = 1000
    constants[12] = 1000
    constants[13] = 1000
    constants[14] = 1000
    constants[15] = 1000
    constants[16] = 1000
    constants[17] = 150
    constants[18] = 150
    constants[19] = 150
    constants[20] = 150
    constants[21] = 150
    constants[22] = 150
    constants[23] = 150
    constants[24] = 150
    constants[25] = 150
    constants[26] = 150
    constants[27] = 150
    constants[28] = 150
    constants[29] = 150
    constants[30] = 150
    constants[31] = 150
    constants[32] = 150
    constants[33] = 150
    constants[34] = 150
    constants[35] = 150
    constants[36] = 150
    states[0] = 0.003
    states[1] = 0
    states[2] = 0
    states[3] = 0
    states[4] = 0
    states[5] = 0
    states[6] = 0
    states[7] = 0
    states[8] = 0
    states[9] = 0
    states[10] = 0
    states[11] = 0
    states[12] = 1.2
    states[13] = 0
    states[14] = 0
    states[15] = 0
    states[16] = 0
    states[17] = 1.2
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[0] = -constants[7]*(((((constants[0]-states[1])-states[2])-states[3])-states[5])-states[4])*(constants[1]-states[2])+constants[17]*states[2]+constants[28]*states[3]
    rates[2] = constants[7]*(((((constants[0]-states[1])-states[2])-states[3])-states[5])-states[4])*(constants[1]-states[2])-(constants[17]+constants[27])*states[2]
    rates[1] = (((-constants[8]*states[1]*(constants[2]-states[3])+constants[18]*states[3]+constants[27]*states[2]+(constants[29]+constants[19])*states[5])-constants[9]*states[1]*((((((((constants[3]-states[6])-states[7])-states[8])-states[9])-states[5])-states[4])-states[10])-states[11]))+(constants[31]+constants[21])*states[4])-constants[11]*states[6]*states[1]
    rates[3] = constants[8]*states[1]*(constants[2]-states[3])-(constants[18]+constants[28])*states[3]
    rates[12] = -constants[9]*((((((((constants[3]-states[6])-states[7])-states[8])-states[9])-states[5])-states[4])-states[10])-states[11])*states[1]+constants[19]*states[5]+constants[30]*states[8]
    rates[5] = constants[9]*((((((((constants[3]-states[6])-states[7])-states[8])-states[9])-states[5])-states[4])-states[10])-states[11])*states[1]-(constants[19]+constants[29])*states[5]
    rates[6] = (-constants[10]*states[6]*((constants[4]-states[8])-states[9])+constants[20]*states[8]+constants[29]*states[5]+constants[32]*states[9]+constants[21]*states[4])-constants[11]*states[6]*states[1]
    rates[8] = constants[10]*states[6]*((constants[4]-states[8])-states[9])-(constants[20]+constants[30])*states[8]
    rates[4] = constants[11]*states[6]*states[1]-(constants[21]+constants[31])*states[4]
    rates[7] = ((((constants[31]*states[4]-constants[12]*states[7]*((constants[4]-states[8])-states[9]))+constants[22]*states[9])-constants[13]*states[7]*((((((constants[5]-states[13])-states[14])-states[15])-states[16])-states[10])-states[11]))+(constants[23]+constants[33])*states[10]+(constants[25]+constants[35])*states[11])-constants[15]*states[13]*states[7]
    rates[9] = constants[12]*states[7]*((constants[4]-states[8])-states[9])-(constants[22]+constants[32])*states[9]
    rates[17] = -constants[13]*((((((constants[5]-states[13])-states[14])-states[15])-states[16])-states[10])-states[11])*states[7]+constants[23]*states[10]+constants[34]*states[15]
    rates[10] = constants[13]*((((((constants[5]-states[13])-states[14])-states[15])-states[16])-states[10])-states[11])*states[7]-(constants[23]+constants[33])*states[10]
    rates[13] = (((constants[33]*states[10]-constants[14]*states[13]*((constants[6]-states[15])-states[16]))+constants[24]*states[15])-constants[15]*states[13]*states[7])+constants[25]*states[11]+constants[36]*states[16]
    rates[11] = constants[15]*states[13]*states[7]-(constants[25]+constants[35])*states[11]
    rates[14] = -constants[16]*states[14]*((constants[6]-states[15])-states[16])+constants[26]*states[16]+constants[35]*states[11]
    rates[15] = constants[14]*states[13]*((constants[6]-states[15])-states[16])-(constants[24]+constants[34])*states[15]
    rates[16] = constants[16]*states[14]*((constants[6]-states[15])-states[16])-(constants[26]+constants[36])*states[16]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
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
        self.mostot = 0.003
        self.e1tot = 0.0003
        self.e2tot = 0.0003
        self.mektot = 1.2
        self.mekpasetot = 0.0003
        self.mapktot = 1.2
        self.mapkpasetot = 0.12
        self.a1 = 1000
        self.a2 = 1000
        self.a3 = 1000
        self.a4 = 1000
        self.a5 = 1000
        self.a6 = 1000
        self.a7 = 1000
        self.a8 = 1000
        self.a9 = 1000
        self.a10 = 1000
        self.d1 = 150
        self.d2 = 150
        self.d3 = 150
        self.d4 = 150
        self.d5 = 150
        self.d6 = 150
        self.d7 = 150
        self.d8 = 150
        self.d9 = 150
        self.d10 = 150
        self.k1 = 150
        self.k2 = 150
        self.k3 = 150
        self.k4 = 150
        self.k5 = 150
        self.k6 = 150
        self.k7 = 150
        self.k8 = 150
        self.k9 = 150
        self.k10 = 150

    def to_dict(self):
        return {
            "mostot": self.mostot,
            "e1tot": self.e1tot,
            "e2tot": self.e2tot,
            "mektot": self.mektot,
            "mekpasetot": self.mekpasetot,
            "mapktot": self.mapktot,
            "mapkpasetot": self.mapkpasetot,
            "a1": self.a1,
            "a2": self.a2,
            "a3": self.a3,
            "a4": self.a4,
            "a5": self.a5,
            "a6": self.a6,
            "a7": self.a7,
            "a8": self.a8,
            "a9": self.a9,
            "a10": self.a10,
            "d1": self.d1,
            "d2": self.d2,
            "d3": self.d3,
            "d4": self.d4,
            "d5": self.d5,
            "d6": self.d6,
            "d7": self.d7,
            "d8": self.d8,
            "d9": self.d9,
            "d10": self.d10,
            "k1": self.k1,
            "k2": self.k2,
            "k3": self.k3,
            "k4": self.k4,
            "k5": self.k5,
            "k6": self.k6,
            "k7": self.k7,
            "k8": self.k8,
            "k9": self.k9,
            "k10": self.k10,
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
        y0=[0.003, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1.2, 0, 0, 0, 0, 1.2],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "huang_ferrell_1996"
        self.curve_names = [
            "mos",
            "mosstar",
            "mose1",
            "mosstare2",
            "mekstarmosstar",
            "mekmosstar",
            "mekstar",
            "mekstarstar",
            "mekstarmekpase",
            "mekstarstarmekpase",
            "mapkmekstarstar",
            "mapkstarmekstarstar",
            "mek",
            "mapkstar",
            "mapkstarstar",
            "mapkstarmapkpase",
            "mapkstarstarmapkpase",
            "mapk",
        ]
        self.state_names = ['mos', 'mosstar', 'mose1', 'mosstare2', 'mekstarmosstar', 'mekmosstar', 'mekstar', 'mekstarstar', 'mekstarmekpase', 'mekstarstarmekpase', 'mapkmekstarstar', 'mapkstarmekstarstar', 'mek', 'mapkstar', 'mapkstarstar', 'mapkstarmapkpase', 'mapkstarstarmapkpase', 'mapk']
        self.algebraic_names = []
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 37
        p = self.params

        # direct mapping
        c[0] = p.mostot
        c[1] = p.e1tot
        c[2] = p.e2tot
        c[3] = p.mektot
        c[4] = p.mekpasetot
        c[5] = p.mapktot
        c[6] = p.mapkpasetot
        c[7] = p.a1
        c[8] = p.a2
        c[9] = p.a3
        c[10] = p.a4
        c[11] = p.a5
        c[12] = p.a6
        c[13] = p.a7
        c[14] = p.a8
        c[15] = p.a9
        c[16] = p.a10
        c[17] = p.d1
        c[18] = p.d2
        c[19] = p.d3
        c[20] = p.d4
        c[21] = p.d5
        c[22] = p.d6
        c[23] = p.d7
        c[24] = p.d8
        c[25] = p.d9
        c[26] = p.d10
        c[27] = p.k1
        c[28] = p.k2
        c[29] = p.k3
        c[30] = p.k4
        c[31] = p.k5
        c[32] = p.k6
        c[33] = p.k7
        c[34] = p.k8
        c[35] = p.k9
        c[36] = p.k10

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
