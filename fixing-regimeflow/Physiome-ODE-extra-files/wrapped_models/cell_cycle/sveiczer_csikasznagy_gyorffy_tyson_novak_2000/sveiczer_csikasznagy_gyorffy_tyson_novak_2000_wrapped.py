# Size of variable arrays:
sizeAlgebraic = 8
sizeStates = 16
sizeConstants = 58
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (minute)"
    legend_states[0] = "MPF in component MPF (dimensionless)"
    legend_constants[0] = "k1 in component rate_constants (first_order_rate_constant)"
    legend_algebraic[0] = "k2 in component rate_constants (first_order_rate_constant)"
    legend_algebraic[2] = "kwee in component rate_constants (first_order_rate_constant)"
    legend_algebraic[4] = "kc25 in component rate_constants (first_order_rate_constant)"
    legend_constants[1] = "kj in component rate_constants (first_order_rate_constant)"
    legend_constants[2] = "kjr in component rate_constants (first_order_rate_constant)"
    legend_constants[3] = "k6_ in component rate_constants (first_order_rate_constant)"
    legend_constants[4] = "k6 in component rate_constants (first_order_rate_constant)"
    legend_states[1] = "mass in component mass (dimensionless)"
    legend_states[2] = "preMPF in component preMPF (dimensionless)"
    legend_states[3] = "Rum1 in component Rum1 (dimensionless)"
    legend_states[4] = "Rum1P in component Rum1P (dimensionless)"
    legend_states[5] = "CR in component CR (dimensionless)"
    legend_states[6] = "CRP in component CRP (dimensionless)"
    legend_states[7] = "Ste9 in component Ste9 (dimensionless)"
    legend_constants[5] = "kste9r_ in component rate_constants (first_order_rate_constant)"
    legend_constants[6] = "kste9r in component rate_constants (first_order_rate_constant)"
    legend_constants[7] = "kste9 in component rate_constants (first_order_rate_constant)"
    legend_constants[8] = "Jste9r in component Ste9 (dimensionless)"
    legend_constants[9] = "Jste9 in component Ste9 (dimensionless)"
    legend_algebraic[1] = "MPF_a in component MPF_a (dimensionless)"
    legend_algebraic[3] = "PP in component PP (dimensionless)"
    legend_constants[10] = "SK in component dimensionless_constants (dimensionless)"
    legend_states[8] = "Mik1 in component Mik1 (dimensionless)"
    legend_constants[11] = "ks in component rate_constants (first_order_rate_constant)"
    legend_constants[12] = "kmr_ in component rate_constants (first_order_rate_constant)"
    legend_constants[13] = "kmr in component rate_constants (first_order_rate_constant)"
    legend_constants[14] = "km in component rate_constants (first_order_rate_constant)"
    legend_constants[15] = "Jmikr in component Mik1 (dimensionless)"
    legend_constants[16] = "Jmik in component Mik1 (dimensionless)"
    legend_states[9] = "Wee1 in component Wee1 (dimensionless)"
    legend_constants[17] = "kwr_ in component rate_constants (first_order_rate_constant)"
    legend_constants[18] = "kwr in component rate_constants (first_order_rate_constant)"
    legend_constants[19] = "kw in component rate_constants (first_order_rate_constant)"
    legend_constants[20] = "Jweer in component Wee1 (dimensionless)"
    legend_constants[21] = "Jwee in component Wee1 (dimensionless)"
    legend_states[10] = "Cdc25 in component Cdc25 (dimensionless)"
    legend_constants[22] = "k25 in component rate_constants (first_order_rate_constant)"
    legend_constants[23] = "k5 in component rate_constants (first_order_rate_constant)"
    legend_constants[24] = "k25r_ in component rate_constants (first_order_rate_constant)"
    legend_constants[25] = "k25r in component rate_constants (first_order_rate_constant)"
    legend_constants[26] = "J25 in component Cdc25 (dimensionless)"
    legend_constants[27] = "J25r in component Cdc25 (dimensionless)"
    legend_states[11] = "Slp1 in component Slp1 (dimensionless)"
    legend_constants[28] = "kas in component rate_constants (first_order_rate_constant)"
    legend_constants[29] = "kad in component rate_constants (first_order_rate_constant)"
    legend_states[12] = "Slp1_a in component Slp1_a (dimensionless)"
    legend_constants[30] = "kaa_ in component rate_constants (first_order_rate_constant)"
    legend_constants[31] = "kaa in component rate_constants (first_order_rate_constant)"
    legend_constants[32] = "kai in component rate_constants (first_order_rate_constant)"
    legend_states[13] = "Inh in component Inh (dimensionless)"
    legend_constants[33] = "k3 in component rate_constants (first_order_rate_constant)"
    legend_constants[34] = "ki in component rate_constants (first_order_rate_constant)"
    legend_constants[35] = "kir in component rate_constants (first_order_rate_constant)"
    legend_algebraic[5] = "k4 in component rate_constants (first_order_rate_constant)"
    legend_states[14] = "PI in component PI (dimensionless)"
    legend_constants[36] = "kp in component rate_constants (first_order_rate_constant)"
    legend_constants[37] = "kpp_ in component rate_constants (first_order_rate_constant)"
    legend_constants[38] = "kpp in component rate_constants (first_order_rate_constant)"
    legend_algebraic[6] = "k2c in component rate_constants (first_order_rate_constant)"
    legend_constants[39] = "epsilon_p in component dimensionless_constants (dimensionless)"
    legend_constants[40] = "mu in component mass (first_order_rate_constant)"
    legend_states[15] = "R_dna in component R_dna (dimensionless)"
    legend_constants[41] = "K in component R_dna (dimensionless)"
    legend_constants[42] = "Y in component R_dna (dimensionless)"
    legend_constants[43] = "epsilon in component dimensionless_constants (dimensionless)"
    legend_algebraic[7] = "ratio in component ratio (dimensionless)"
    legend_constants[44] = "V2_ in component rate_constants (first_order_rate_constant)"
    legend_constants[45] = "V2 in component rate_constants (first_order_rate_constant)"
    legend_constants[46] = "V2c in component rate_constants (first_order_rate_constant)"
    legend_constants[47] = "V2c_ in component rate_constants (first_order_rate_constant)"
    legend_constants[48] = "Vwee in component rate_constants (first_order_rate_constant)"
    legend_constants[49] = "Vwee_ in component rate_constants (first_order_rate_constant)"
    legend_constants[50] = "Vmik in component rate_constants (first_order_rate_constant)"
    legend_constants[51] = "Vmik_ in component rate_constants (first_order_rate_constant)"
    legend_constants[52] = "V25 in component rate_constants (first_order_rate_constant)"
    legend_constants[53] = "V25_ in component rate_constants (first_order_rate_constant)"
    legend_constants[54] = "Vpyp in component rate_constants (first_order_rate_constant)"
    legend_constants[55] = "V4 in component rate_constants (first_order_rate_constant)"
    legend_constants[56] = "V4_ in component rate_constants (first_order_rate_constant)"
    legend_constants[57] = "Pyp3 in component rate_constants (dimensionless)"
    legend_rates[0] = "d/dt MPF in component MPF (dimensionless)"
    legend_rates[2] = "d/dt preMPF in component preMPF (dimensionless)"
    legend_rates[7] = "d/dt Ste9 in component Ste9 (dimensionless)"
    legend_rates[8] = "d/dt Mik1 in component Mik1 (dimensionless)"
    legend_rates[9] = "d/dt Wee1 in component Wee1 (dimensionless)"
    legend_rates[10] = "d/dt Cdc25 in component Cdc25 (dimensionless)"
    legend_rates[11] = "d/dt Slp1 in component Slp1 (dimensionless)"
    legend_rates[12] = "d/dt Slp1_a in component Slp1_a (dimensionless)"
    legend_rates[13] = "d/dt Inh in component Inh (dimensionless)"
    legend_rates[14] = "d/dt PI in component PI (dimensionless)"
    legend_rates[6] = "d/dt CRP in component CRP (dimensionless)"
    legend_rates[5] = "d/dt CR in component CR (dimensionless)"
    legend_rates[3] = "d/dt Rum1 in component Rum1 (dimensionless)"
    legend_rates[4] = "d/dt Rum1P in component Rum1P (dimensionless)"
    legend_rates[1] = "d/dt mass in component mass (dimensionless)"
    legend_rates[15] = "d/dt R_dna in component R_dna (dimensionless)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 0
    constants[0] = 0.02
    constants[1] = 400
    constants[2] = 1
    constants[3] = 0.1
    constants[4] = 5
    states[1] = 1
    states[2] = 1
    states[3] = 0
    states[4] = 0
    states[5] = 0
    states[6] = 0
    states[7] = 0
    constants[5] = 0.03
    constants[6] = 8
    constants[7] = 5
    constants[8] = 0.01
    constants[9] = 0.01
    constants[10] = 0.018
    states[8] = 0
    constants[11] = 0.1
    constants[12] = 0.01
    constants[13] = 5
    constants[14] = 1
    constants[15] = 0.15
    constants[16] = 0.15
    states[9] = 0
    constants[17] = 0.4
    constants[18] = 1
    constants[19] = 2
    constants[20] = 0.2
    constants[21] = 0.2
    states[10] = 0
    constants[22] = 1
    constants[23] = 0.1
    constants[24] = 0.4
    constants[25] = 2
    constants[26] = 0.05
    constants[27] = 0.05
    states[11] = 0
    constants[28] = 0.1
    constants[29] = 0.1
    states[12] = 0
    constants[30] = 0.01
    constants[31] = 0.1
    constants[32] = 0.1
    states[13] = 0
    constants[33] = 0.1
    constants[34] = 50
    constants[35] = 0.5
    states[14] = 0.2
    constants[36] = 100
    constants[37] = 1
    constants[38] = 100
    constants[39] = 0.025
    constants[40] = 0.00462
    states[15] = 1
    constants[41] = 0.06
    constants[42] = 0
    constants[43] = 0.05
    constants[44] = 0.02
    constants[45] = 1
    constants[46] = 0.5
    constants[47] = 0.02
    constants[48] = 10
    constants[49] = 0.08
    constants[50] = 2
    constants[51] = 0.04
    constants[52] = 10
    constants[53] = 0.05
    constants[54] = 0.07
    constants[55] = 1
    constants[56] = 0.01
    constants[57] = 1
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[1] = constants[40]*states[1]
    algebraic[1] = states[0]+constants[43]*states[2]
    rates[11] = constants[28]*algebraic[1]-constants[29]*states[11]
    rates[12] = (constants[30]+constants[31]*algebraic[1])*(states[11]-states[12])-(constants[32]+constants[29])*states[12]
    rates[15] = (constants[41]*1.00000)/(1.00000+constants[42]*algebraic[1])
    algebraic[3] = 1.00000-states[14]
    rates[7] = ((constants[5]+constants[6]*algebraic[3])*(1.00000-states[7]))/((constants[8]+1.00000)-states[7])-(constants[7]*(algebraic[1]+constants[10]*states[1])*states[7])/(constants[9]+states[7])
    rates[8] = ((constants[11]+constants[12]+constants[13]*algebraic[3])*(1.00000-states[8]))/((constants[15]+1.00000)-states[8])-(constants[14]*algebraic[1]*states[8])/(constants[16]+states[8])
    rates[9] = ((constants[17]+constants[18]*algebraic[3])*(1.00000-states[9]))/((constants[20]+1.00000)-states[9])-(constants[19]*algebraic[1]*states[9])/(constants[21]+states[9])
    rates[10] = (constants[22]*algebraic[1]*(1.00000-states[10]))/((constants[26]+1.00000)-states[10])-((constants[23]+constants[24]+constants[25]*algebraic[3])*states[10])/(constants[27]+states[10])
    algebraic[0] = constants[44]+constants[45]*states[7]
    algebraic[2] = constants[48]*states[9]+constants[49]*(1.00000-states[9])+constants[50]*states[8]+constants[51]*(1.00000-states[8])
    algebraic[4] = constants[52]*states[10]+constants[53]*(1.00000-states[10])+constants[54]*constants[57]
    rates[0] = ((((constants[0]*states[1]-algebraic[0]*states[0])-algebraic[2]*states[0])+algebraic[4]*states[2])-constants[1]*states[0]*(states[3]+states[4]))+constants[2]*(states[5]+states[6])+constants[3]*states[5]+(constants[3]+constants[4])*states[6]
    rates[2] = (algebraic[2]*states[0]-algebraic[4]*states[2])-algebraic[0]*states[2]
    algebraic[5] = constants[56]+constants[55]*states[12]
    rates[13] = ((constants[33]-constants[34]*states[13]*algebraic[3])+constants[35]*states[14])-algebraic[5]*states[13]
    rates[14] = (constants[34]*states[13]*algebraic[3]-constants[35]*states[14])-algebraic[5]*states[14]
    algebraic[6] = constants[47]+constants[46]*states[7]
    rates[6] = ((((constants[36]*(algebraic[1]+constants[39]*constants[10]*states[1])*states[5]-(constants[37]+constants[38]*algebraic[3])*states[6])+constants[1]*states[0]*states[4])-constants[2]*states[6])-algebraic[6]*states[6])-(constants[3]+constants[4])*states[6]
    rates[5] = ((((constants[1]*states[0]*states[3]-constants[2]*states[5])-algebraic[6]*states[5])-constants[3]*states[5])-constants[36]*(algebraic[1]+constants[39]*constants[10]*states[1])*states[5])+(constants[37]+constants[38]*algebraic[3])*states[6]
    rates[3] = ((((constants[23]-constants[3]*states[3])-constants[36]*(algebraic[1]+constants[39]*constants[10]*states[1])*states[3])+(constants[37]+constants[38]*algebraic[3])*states[4])-constants[1]*states[0]*states[3])+constants[2]*states[5]+algebraic[6]*states[5]
    rates[4] = (((constants[36]*(algebraic[1]+constants[39]*constants[10]*states[1])*states[3]-(constants[37]+constants[38]*algebraic[3])*states[4])-(constants[3]+constants[4])*states[4])-constants[1]*states[0]*states[4])+constants[2]*states[6]+algebraic[6]*states[6]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[1] = states[0]+constants[43]*states[2]
    algebraic[3] = 1.00000-states[14]
    algebraic[0] = constants[44]+constants[45]*states[7]
    algebraic[2] = constants[48]*states[9]+constants[49]*(1.00000-states[9])+constants[50]*states[8]+constants[51]*(1.00000-states[8])
    algebraic[4] = constants[52]*states[10]+constants[53]*(1.00000-states[10])+constants[54]*constants[57]
    algebraic[5] = constants[56]+constants[55]*states[12]
    algebraic[6] = constants[47]+constants[46]*states[7]
    algebraic[7] = algebraic[1]/algebraic[3]
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
        self.k1 = 0.02
        self.kj = 400
        self.kjr = 1
        self.k6_ = 0.1
        self.k6 = 5
        self.kste9r_ = 0.03
        self.kste9r = 8
        self.kste9 = 5
        self.Jste9r = 0.01
        self.Jste9 = 0.01
        self.SK = 0.018
        self.ks = 0.1
        self.kmr_ = 0.01
        self.kmr = 5
        self.km = 1
        self.Jmikr = 0.15
        self.Jmik = 0.15
        self.kwr_ = 0.4
        self.kwr = 1
        self.kw = 2
        self.Jweer = 0.2
        self.Jwee = 0.2
        self.k25 = 1
        self.k5 = 0.1
        self.k25r_ = 0.4
        self.k25r = 2
        self.J25 = 0.05
        self.J25r = 0.05
        self.kas = 0.1
        self.kad = 0.1
        self.kaa_ = 0.01
        self.kaa = 0.1
        self.kai = 0.1
        self.k3 = 0.1
        self.ki = 50
        self.kir = 0.5
        self.kp = 100
        self.kpp_ = 1
        self.kpp = 100
        self.epsilon_p = 0.025
        self.mu = 0.00462
        self.K = 0.06
        self.Y = 0
        self.epsilon = 0.05
        self.V2_ = 0.02
        self.V2 = 1
        self.V2c = 0.5
        self.V2c_ = 0.02
        self.Vwee = 10
        self.Vwee_ = 0.08
        self.Vmik = 2
        self.Vmik_ = 0.04
        self.V25 = 10
        self.V25_ = 0.05
        self.Vpyp = 0.07
        self.V4 = 1
        self.V4_ = 0.01
        self.Pyp3 = 1

    def to_dict(self):
        return {
            "k1": self.k1,
            "kj": self.kj,
            "kjr": self.kjr,
            "k6_": self.k6_,
            "k6": self.k6,
            "kste9r_": self.kste9r_,
            "kste9r": self.kste9r,
            "kste9": self.kste9,
            "Jste9r": self.Jste9r,
            "Jste9": self.Jste9,
            "SK": self.SK,
            "ks": self.ks,
            "kmr_": self.kmr_,
            "kmr": self.kmr,
            "km": self.km,
            "Jmikr": self.Jmikr,
            "Jmik": self.Jmik,
            "kwr_": self.kwr_,
            "kwr": self.kwr,
            "kw": self.kw,
            "Jweer": self.Jweer,
            "Jwee": self.Jwee,
            "k25": self.k25,
            "k5": self.k5,
            "k25r_": self.k25r_,
            "k25r": self.k25r,
            "J25": self.J25,
            "J25r": self.J25r,
            "kas": self.kas,
            "kad": self.kad,
            "kaa_": self.kaa_,
            "kaa": self.kaa,
            "kai": self.kai,
            "k3": self.k3,
            "ki": self.ki,
            "kir": self.kir,
            "kp": self.kp,
            "kpp_": self.kpp_,
            "kpp": self.kpp,
            "epsilon_p": self.epsilon_p,
            "mu": self.mu,
            "K": self.K,
            "Y": self.Y,
            "epsilon": self.epsilon,
            "V2_": self.V2_,
            "V2": self.V2,
            "V2c": self.V2c,
            "V2c_": self.V2c_,
            "Vwee": self.Vwee,
            "Vwee_": self.Vwee_,
            "Vmik": self.Vmik,
            "Vmik_": self.Vmik_,
            "V25": self.V25,
            "V25_": self.V25_,
            "Vpyp": self.Vpyp,
            "V4": self.V4,
            "V4_": self.V4_,
            "Pyp3": self.Pyp3,
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
        y0=[0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.2, 1],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "sveiczer_csikasznagy_gyorffy_tyson_novak_2000"
        self.curve_names = [
            "MPF",
            "mass",
            "preMPF",
            "Rum1",
            "Rum1P",
            "CR",
            "CRP",
            "Ste9",
            "Mik1",
            "Wee1",
            "Cdc25",
            "Slp1",
            "Slp1_a",
            "Inh",
            "PI",
            "R_dna",
        ]
        self.state_names = ['MPF', 'mass', 'preMPF', 'Rum1', 'Rum1P', 'CR', 'CRP', 'Ste9', 'Mik1', 'Wee1', 'Cdc25', 'Slp1', 'Slp1_a', 'Inh', 'PI', 'R_dna']
        self.algebraic_names = ['k2', 'MPF_a', 'kwee', 'PP', 'kc25', 'k4', 'k2c', 'ratio']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 58
        p = self.params

        # direct mapping
        c[0] = p.k1
        c[1] = p.kj
        c[2] = p.kjr
        c[3] = p.k6_
        c[4] = p.k6
        c[5] = p.kste9r_
        c[6] = p.kste9r
        c[7] = p.kste9
        c[8] = p.Jste9r
        c[9] = p.Jste9
        c[10] = p.SK
        c[11] = p.ks
        c[12] = p.kmr_
        c[13] = p.kmr
        c[14] = p.km
        c[15] = p.Jmikr
        c[16] = p.Jmik
        c[17] = p.kwr_
        c[18] = p.kwr
        c[19] = p.kw
        c[20] = p.Jweer
        c[21] = p.Jwee
        c[22] = p.k25
        c[23] = p.k5
        c[24] = p.k25r_
        c[25] = p.k25r
        c[26] = p.J25
        c[27] = p.J25r
        c[28] = p.kas
        c[29] = p.kad
        c[30] = p.kaa_
        c[31] = p.kaa
        c[32] = p.kai
        c[33] = p.k3
        c[34] = p.ki
        c[35] = p.kir
        c[36] = p.kp
        c[37] = p.kpp_
        c[38] = p.kpp
        c[39] = p.epsilon_p
        c[40] = p.mu
        c[41] = p.K
        c[42] = p.Y
        c[43] = p.epsilon
        c[44] = p.V2_
        c[45] = p.V2
        c[46] = p.V2c
        c[47] = p.V2c_
        c[48] = p.Vwee
        c[49] = p.Vwee_
        c[50] = p.Vmik
        c[51] = p.Vmik_
        c[52] = p.V25
        c[53] = p.V25_
        c[54] = p.Vpyp
        c[55] = p.V4
        c[56] = p.V4_
        c[57] = p.Pyp3

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
