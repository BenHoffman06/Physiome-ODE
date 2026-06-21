# Size of variable arrays:
sizeAlgebraic = 6
sizeStates = 9
sizeConstants = 47
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (minute)"
    legend_states[0] = "Cdc13T in component Cdc13T (dimensionless)"
    legend_constants[0] = "k1 in component Cdc13T (first_order_rate_constant)"
    legend_constants[1] = "k2_ in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[2] = "k2__ in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[3] = "k2___ in component kinetic_parameters (first_order_rate_constant)"
    legend_states[1] = "M in component M (dimensionless)"
    legend_states[2] = "Ste9 in component Ste9 (dimensionless)"
    legend_states[3] = "Slp1 in component Slp1 (dimensionless)"
    legend_states[4] = "preMPF in component preMPF (dimensionless)"
    legend_algebraic[3] = "kwee in component preMPF (first_order_rate_constant)"
    legend_constants[4] = "kwee_ in component preMPF (first_order_rate_constant)"
    legend_constants[5] = "kwee__ in component preMPF (first_order_rate_constant)"
    legend_constants[6] = "Vawee in component preMPF (first_order_rate_constant)"
    legend_constants[7] = "Viwee in component preMPF (first_order_rate_constant)"
    legend_constants[8] = "Jawee in component preMPF (dimensionless)"
    legend_constants[9] = "Jiwee in component preMPF (dimensionless)"
    legend_algebraic[5] = "k25 in component preMPF (first_order_rate_constant)"
    legend_constants[10] = "k25_ in component preMPF (first_order_rate_constant)"
    legend_constants[11] = "k25__ in component preMPF (first_order_rate_constant)"
    legend_constants[12] = "Va25 in component preMPF (first_order_rate_constant)"
    legend_constants[13] = "Vi25 in component preMPF (first_order_rate_constant)"
    legend_constants[14] = "Ja25 in component preMPF (dimensionless)"
    legend_constants[15] = "Ji25 in component preMPF (dimensionless)"
    legend_algebraic[2] = "MPF in component MPF (dimensionless)"
    legend_constants[16] = "k3_ in component Ste9 (first_order_rate_constant)"
    legend_constants[17] = "k3__ in component Ste9 (first_order_rate_constant)"
    legend_constants[18] = "k4 in component Ste9 (first_order_rate_constant)"
    legend_constants[19] = "k4_ in component Ste9 (first_order_rate_constant)"
    legend_constants[20] = "J3 in component Ste9 (dimensionless)"
    legend_constants[21] = "J4 in component Ste9 (dimensionless)"
    legend_states[5] = "SK in component SK (dimensionless)"
    legend_states[6] = "Slp1T in component Slp1T (dimensionless)"
    legend_constants[22] = "k5_ in component Slp1T (first_order_rate_constant)"
    legend_constants[23] = "k5__ in component Slp1T (first_order_rate_constant)"
    legend_constants[24] = "J5 in component Slp1T (dimensionless)"
    legend_constants[25] = "k6 in component kinetic_parameters (first_order_rate_constant)"
    legend_constants[26] = "k7 in component Slp1 (first_order_rate_constant)"
    legend_constants[27] = "k8 in component Slp1 (first_order_rate_constant)"
    legend_constants[28] = "J7 in component Slp1 (dimensionless)"
    legend_constants[29] = "J8 in component Slp1 (dimensionless)"
    legend_states[7] = "IEP in component IEP (dimensionless)"
    legend_constants[30] = "k9 in component IEP (first_order_rate_constant)"
    legend_constants[31] = "k10 in component IEP (first_order_rate_constant)"
    legend_constants[32] = "J9 in component IEP (dimensionless)"
    legend_constants[33] = "J10 in component IEP (dimensionless)"
    legend_states[8] = "Rum1T in component Rum1T (dimensionless)"
    legend_constants[34] = "k11 in component Rum1T (first_order_rate_constant)"
    legend_constants[35] = "k12 in component Rum1T (first_order_rate_constant)"
    legend_constants[36] = "k12_ in component Rum1T (first_order_rate_constant)"
    legend_constants[37] = "k12__ in component Rum1T (first_order_rate_constant)"
    legend_constants[38] = "k13 in component SK (first_order_rate_constant)"
    legend_constants[39] = "k14 in component SK (first_order_rate_constant)"
    legend_algebraic[4] = "TF in component TF (dimensionless)"
    legend_constants[40] = "mu in component M (first_order_rate_constant)"
    legend_algebraic[1] = "Trimer in component Trimer (dimensionless)"
    legend_algebraic[0] = "sum in component Trimer (dimensionless)"
    legend_constants[41] = "Kdiss in component Trimer (dimensionless)"
    legend_constants[42] = "k15 in component TF (first_order_rate_constant)"
    legend_constants[43] = "k16_ in component TF (first_order_rate_constant)"
    legend_constants[44] = "k16__ in component TF (first_order_rate_constant)"
    legend_constants[45] = "J15 in component TF (dimensionless)"
    legend_constants[46] = "J16 in component TF (dimensionless)"
    legend_rates[0] = "d/dt Cdc13T in component Cdc13T (dimensionless)"
    legend_rates[4] = "d/dt preMPF in component preMPF (dimensionless)"
    legend_rates[2] = "d/dt Ste9 in component Ste9 (dimensionless)"
    legend_rates[6] = "d/dt Slp1T in component Slp1T (dimensionless)"
    legend_rates[3] = "d/dt Slp1 in component Slp1 (dimensionless)"
    legend_rates[7] = "d/dt IEP in component IEP (dimensionless)"
    legend_rates[8] = "d/dt Rum1T in component Rum1T (dimensionless)"
    legend_rates[5] = "d/dt SK in component SK (dimensionless)"
    legend_rates[1] = "d/dt M in component M (dimensionless)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 0.2
    constants[0] = 0.03
    constants[1] = 0.03
    constants[2] = 1
    constants[3] = 0.1
    states[1] = 1
    states[2] = 1
    states[3] = 2.2
    states[4] = 0
    constants[4] = 0.15
    constants[5] = 1.3
    constants[6] = 0.25
    constants[7] = 1
    constants[8] = 0.01
    constants[9] = 0.01
    constants[10] = 0.05
    constants[11] = 5
    constants[12] = 1
    constants[13] = 0.25
    constants[14] = 0.01
    constants[15] = 0.01
    constants[16] = 1
    constants[17] = 10
    constants[18] = 35
    constants[19] = 2
    constants[20] = 0.01
    constants[21] = 0.01
    states[5] = 0
    states[6] = 0
    constants[22] = 0.005
    constants[23] = 0.3
    constants[24] = 0.3
    constants[25] = 0.1
    constants[26] = 1
    constants[27] = 0.25
    constants[28] = 0.001
    constants[29] = 0.001
    states[7] = 0
    constants[30] = 0.1
    constants[31] = 0.04
    constants[32] = 0.01
    constants[33] = 0.01
    states[8] = 0
    constants[34] = 0.1
    constants[35] = 0.01
    constants[36] = 1
    constants[37] = 3
    constants[38] = 0.1
    constants[39] = 0.1
    constants[40] = 0.005
    constants[41] = 0.001
    constants[42] = 1.5
    constants[43] = 1
    constants[44] = 2
    constants[45] = 0.01
    constants[46] = 0.01
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[0] = constants[0]*states[1]-(constants[1]+constants[2]*states[2]+constants[3]*states[3])*states[0]
    rates[3] = (constants[26]*states[7]*(states[6]-states[3]))/((constants[28]+states[6])-states[3])-((constants[27]*states[3])/(constants[29]+states[3])+constants[25]*states[3])
    rates[1] = constants[40]*states[1]
    algebraic[0] = states[0]+states[8]+constants[41]
    algebraic[1] = (2.00000*states[0]*states[8])/(algebraic[0]+power(power(algebraic[0], 2.00000)-4.00000*states[0]*states[8], 1.0/2))
    algebraic[2] = ((states[0]-states[4])*(states[0]-algebraic[1]))/states[0]
    rates[2] = ((constants[16]+constants[17]*states[3])*(1.00000-states[2]))/((constants[20]+1.00000)-states[2])-((constants[19]*states[5]+constants[18]*algebraic[2])*states[2])/(constants[21]+states[2])
    rates[6] = (constants[22]+(constants[23]*(power(algebraic[2], 4.00000)))/(power(constants[24], 4.00000)+power(algebraic[2], 4.00000)))-constants[25]*states[6]
    rates[7] = (constants[30]*algebraic[2]*(1.00000-states[7]))/((constants[32]+1.00000)-states[7])-(constants[31]*states[7])/(constants[33]+states[7])
    rates[8] = constants[34]-(constants[35]+constants[36]*states[5]+constants[37]*algebraic[2])*states[8]
    algebraic[4] = (2.00000*constants[42]*states[1]*constants[46])/(((constants[43]+constants[44]*algebraic[2])-constants[42]*states[1])+(constants[43]+constants[44]*algebraic[2])*constants[45]+constants[42]*states[1]*constants[46]+power(power(((constants[43]+constants[44]*algebraic[2])-constants[42]*states[1])+(constants[43]+constants[44]*algebraic[2])*constants[45]+constants[42]*states[1]*constants[46], 2.00000)-4.00000*constants[42]*states[1]*constants[46]*((constants[43]+constants[44]*algebraic[2])-constants[42]*states[1]), 1.0/2))
    rates[5] = constants[38]*algebraic[4]-constants[39]*states[5]
    algebraic[3] = constants[4]+((constants[5]-constants[4])*2.00000*constants[6]*constants[9])/((constants[7]*algebraic[2]-constants[6])+constants[7]*algebraic[2]*constants[8]+constants[6]*constants[9]+power(power((constants[7]*algebraic[2]-constants[6])+constants[7]*algebraic[2]*constants[8]+constants[6]*constants[9], 2.00000)-4.00000*constants[6]*constants[9]*(constants[7]*algebraic[2]-constants[6]), 1.0/2))
    algebraic[5] = constants[10]+((constants[11]-constants[10])*2.00000*constants[12]*algebraic[2]*constants[15])/((constants[13]-constants[12]*algebraic[2])+constants[13]*constants[14]+constants[12]*algebraic[2]*constants[15]+power(power((constants[13]-constants[12]*algebraic[2])+constants[13]*constants[14]+constants[12]*algebraic[2]*constants[15], 2.00000)-4.00000*constants[12]*algebraic[2]*constants[15]*(constants[13]-constants[12]*algebraic[2]), 1.0/2))
    rates[4] = (algebraic[3]*(states[0]-states[4])-algebraic[5]*states[4])-(constants[1]+constants[2]*states[2]+constants[3]*states[3])*states[4]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = states[0]+states[8]+constants[41]
    algebraic[1] = (2.00000*states[0]*states[8])/(algebraic[0]+power(power(algebraic[0], 2.00000)-4.00000*states[0]*states[8], 1.0/2))
    algebraic[2] = ((states[0]-states[4])*(states[0]-algebraic[1]))/states[0]
    algebraic[4] = (2.00000*constants[42]*states[1]*constants[46])/(((constants[43]+constants[44]*algebraic[2])-constants[42]*states[1])+(constants[43]+constants[44]*algebraic[2])*constants[45]+constants[42]*states[1]*constants[46]+power(power(((constants[43]+constants[44]*algebraic[2])-constants[42]*states[1])+(constants[43]+constants[44]*algebraic[2])*constants[45]+constants[42]*states[1]*constants[46], 2.00000)-4.00000*constants[42]*states[1]*constants[46]*((constants[43]+constants[44]*algebraic[2])-constants[42]*states[1]), 1.0/2))
    algebraic[3] = constants[4]+((constants[5]-constants[4])*2.00000*constants[6]*constants[9])/((constants[7]*algebraic[2]-constants[6])+constants[7]*algebraic[2]*constants[8]+constants[6]*constants[9]+power(power((constants[7]*algebraic[2]-constants[6])+constants[7]*algebraic[2]*constants[8]+constants[6]*constants[9], 2.00000)-4.00000*constants[6]*constants[9]*(constants[7]*algebraic[2]-constants[6]), 1.0/2))
    algebraic[5] = constants[10]+((constants[11]-constants[10])*2.00000*constants[12]*algebraic[2]*constants[15])/((constants[13]-constants[12]*algebraic[2])+constants[13]*constants[14]+constants[12]*algebraic[2]*constants[15]+power(power((constants[13]-constants[12]*algebraic[2])+constants[13]*constants[14]+constants[12]*algebraic[2]*constants[15], 2.00000)-4.00000*constants[12]*algebraic[2]*constants[15]*(constants[13]-constants[12]*algebraic[2]), 1.0/2))
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
        self.k1 = 0.03
        self.k2_ = 0.03
        self.k2__1 = 1
        self.k2__2 = 0.1
        self.kwee_ = 0.15
        self.kwee__1 = 1.3
        self.Vawee = 0.25
        self.Viwee = 1
        self.Jawee = 0.01
        self.Jiwee = 0.01
        self.k25_ = 0.05
        self.k25__1 = 5
        self.Va25 = 1
        self.Vi25 = 0.25
        self.Ja25 = 0.01
        self.Ji25 = 0.01
        self.k3_ = 1
        self.k3__1 = 10
        self.k4 = 35
        self.k4_ = 2
        self.J3 = 0.01
        self.J4 = 0.01
        self.k5_ = 0.005
        self.k5__1 = 0.3
        self.J5 = 0.3
        self.k6 = 0.1
        self.k7 = 1
        self.k8 = 0.25
        self.J7 = 0.001
        self.J8 = 0.001
        self.k9 = 0.1
        self.k10 = 0.04
        self.J9 = 0.01
        self.J10 = 0.01
        self.k11 = 0.1
        self.k12 = 0.01
        self.k12_ = 1
        self.k12__1 = 3
        self.k13 = 0.1
        self.k14 = 0.1
        self.mu = 0.005
        self.Kdiss = 0.001
        self.k15 = 1.5
        self.k16_ = 1
        self.k16__1 = 2
        self.J15 = 0.01
        self.J16 = 0.01

    def to_dict(self):
        return {
            "k1": self.k1,
            "k2_": self.k2_,
            "k2__1": self.k2__1,
            "k2__2": self.k2__2,
            "kwee_": self.kwee_,
            "kwee__1": self.kwee__1,
            "Vawee": self.Vawee,
            "Viwee": self.Viwee,
            "Jawee": self.Jawee,
            "Jiwee": self.Jiwee,
            "k25_": self.k25_,
            "k25__1": self.k25__1,
            "Va25": self.Va25,
            "Vi25": self.Vi25,
            "Ja25": self.Ja25,
            "Ji25": self.Ji25,
            "k3_": self.k3_,
            "k3__1": self.k3__1,
            "k4": self.k4,
            "k4_": self.k4_,
            "J3": self.J3,
            "J4": self.J4,
            "k5_": self.k5_,
            "k5__1": self.k5__1,
            "J5": self.J5,
            "k6": self.k6,
            "k7": self.k7,
            "k8": self.k8,
            "J7": self.J7,
            "J8": self.J8,
            "k9": self.k9,
            "k10": self.k10,
            "J9": self.J9,
            "J10": self.J10,
            "k11": self.k11,
            "k12": self.k12,
            "k12_": self.k12_,
            "k12__1": self.k12__1,
            "k13": self.k13,
            "k14": self.k14,
            "mu": self.mu,
            "Kdiss": self.Kdiss,
            "k15": self.k15,
            "k16_": self.k16_,
            "k16__1": self.k16__1,
            "J15": self.J15,
            "J16": self.J16,
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
        y0=[0.2, 1, 1, 2.2, 0, 0, 0, 0, 0],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "novak_pataki_ciliberto_tyson_2001"
        self.curve_names = [
            "Cdc13T",
            "M",
            "Ste9",
            "Slp1",
            "preMPF",
            "SK",
            "Slp1T",
            "IEP",
            "Rum1T",
        ]
        self.state_names = ['Cdc13T', 'M', 'Ste9', 'Slp1', 'preMPF', 'SK', 'Slp1T', 'IEP', 'Rum1T']
        self.algebraic_names = ['sum', 'Trimer', 'MPF', 'kwee', 'TF', 'k25']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 47
        p = self.params

        # direct mapping
        c[0] = p.k1
        c[1] = p.k2_
        c[2] = p.k2__1
        c[3] = p.k2__2
        c[4] = p.kwee_
        c[5] = p.kwee__1
        c[6] = p.Vawee
        c[7] = p.Viwee
        c[8] = p.Jawee
        c[9] = p.Jiwee
        c[10] = p.k25_
        c[11] = p.k25__1
        c[12] = p.Va25
        c[13] = p.Vi25
        c[14] = p.Ja25
        c[15] = p.Ji25
        c[16] = p.k3_
        c[17] = p.k3__1
        c[18] = p.k4
        c[19] = p.k4_
        c[20] = p.J3
        c[21] = p.J4
        c[22] = p.k5_
        c[23] = p.k5__1
        c[24] = p.J5
        c[25] = p.k6
        c[26] = p.k7
        c[27] = p.k8
        c[28] = p.J7
        c[29] = p.J8
        c[30] = p.k9
        c[31] = p.k10
        c[32] = p.J9
        c[33] = p.J10
        c[34] = p.k11
        c[35] = p.k12
        c[36] = p.k12_
        c[37] = p.k12__1
        c[38] = p.k13
        c[39] = p.k14
        c[40] = p.mu
        c[41] = p.Kdiss
        c[42] = p.k15
        c[43] = p.k16_
        c[44] = p.k16__1
        c[45] = p.J15
        c[46] = p.J16

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
