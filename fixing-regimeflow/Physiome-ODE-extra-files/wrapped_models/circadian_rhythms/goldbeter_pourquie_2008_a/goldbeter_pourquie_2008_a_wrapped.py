# Size of variable arrays:
sizeAlgebraic = 18
sizeStates = 16
sizeConstants = 76
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (minute)"
    legend_states[0] = "N in component N (nanomolar)"
    legend_constants[0] = "KdN in component N (nanomolar)"
    legend_constants[1] = "vsN in component N (flux)"
    legend_constants[2] = "vdN in component N (flux)"
    legend_constants[3] = "kc in component model_parameters (first_order_rate_constant)"
    legend_constants[4] = "KIF in component model_parameters (nanomolar)"
    legend_states[1] = "F in component F (nanomolar)"
    legend_constants[5] = "epsilon in component model_parameters (dimensionless)"
    legend_constants[6] = "j in component model_parameters (dimensionless)"
    legend_states[2] = "Na in component Na (nanomolar)"
    legend_algebraic[0] = "Vtr in component Na (flux)"
    legend_constants[7] = "KdNa in component Na (nanomolar)"
    legend_constants[8] = "VdNa in component Na (flux)"
    legend_constants[9] = "kt1 in component Na (first_order_rate_constant)"
    legend_constants[10] = "kt2 in component Na (first_order_rate_constant)"
    legend_states[3] = "Nan in component Nan (nanomolar)"
    legend_constants[11] = "KdNan in component Nan (nanomolar)"
    legend_constants[12] = "VdNan in component Nan (flux)"
    legend_states[4] = "MF in component MF (nanomolar)"
    legend_constants[13] = "KdMF in component MF (nanomolar)"
    legend_constants[14] = "KIG1 in component MF (nanomolar)"
    legend_algebraic[1] = "vsFK in component MF (flux)"
    legend_constants[15] = "vsF in component MF (flux)"
    legend_constants[16] = "vmF in component MF (flux)"
    legend_constants[17] = "KA in component MF (nanomolar)"
    legend_states[5] = "K in component K (nanomolar)"
    legend_constants[18] = "p in component model_parameters (dimensionless)"
    legend_constants[19] = "KdF in component F (nanomolar)"
    legend_constants[20] = "vdF in component F (flux)"
    legend_constants[21] = "ksF in component F (first_order_rate_constant)"
    legend_algebraic[7] = "V1 in component Wnt_parameters (flux)"
    legend_constants[22] = "theta in component model_parameters (dimensionless)"
    legend_states[6] = "B in component B (nanomolar)"
    legend_constants[23] = "kd1 in component B (first_order_rate_constant)"
    legend_constants[24] = "vsB in component B (flux)"
    legend_algebraic[13] = "VK in component Wnt_parameters (flux)"
    legend_algebraic[17] = "VP in component Wnt_parameters (flux)"
    legend_algebraic[8] = "V2 in component Wnt_parameters (flux)"
    legend_constants[25] = "Kt in component Wnt_parameters (nanomolar)"
    legend_algebraic[2] = "AK in component Wnt_parameters (nanomolar)"
    legend_states[7] = "Bp in component Bp (nanomolar)"
    legend_constants[26] = "kd2 in component Bp (first_order_rate_constant)"
    legend_states[8] = "BN in component BN (nanomolar)"
    legend_states[9] = "MAx in component MAx (nanomolar)"
    legend_constants[27] = "v0 in component MAx (flux)"
    legend_constants[28] = "vMB in component MAx (flux)"
    legend_constants[29] = "vmd in component MAx (flux)"
    legend_constants[30] = "KaB in component MAx (nanomolar)"
    legend_constants[31] = "KaXa in component MAx (nanomolar)"
    legend_constants[32] = "Kmd in component MAx (nanomolar)"
    legend_constants[33] = "n in component MAx (dimensionless)"
    legend_constants[34] = "m in component MAx (dimensionless)"
    legend_constants[35] = "vMXa in component MAx (flux)"
    legend_states[10] = "Xa in component Xa (nanomolar)"
    legend_states[11] = "A in component A (nanomolar)"
    legend_constants[36] = "ksAx in component A (first_order_rate_constant)"
    legend_constants[37] = "vdAx in component A (flux)"
    legend_constants[38] = "KdAx in component A (nanomolar)"
    legend_constants[39] = "d1 in component Wnt_parameters (first_order_rate_constant)"
    legend_constants[40] = "a1 in component Wnt_parameters (second_order_rate_constant)"
    legend_constants[41] = "K1 in component Wnt_parameters (nanomolar)"
    legend_constants[42] = "K2 in component Wnt_parameters (nanomolar)"
    legend_constants[43] = "D in component Wnt_parameters (nanomolar)"
    legend_constants[44] = "KID in component Wnt_parameters (nanomolar)"
    legend_constants[45] = "kt3 in component Wnt_parameters (first_order_rate_constant)"
    legend_constants[46] = "kt4 in component Wnt_parameters (first_order_rate_constant)"
    legend_constants[47] = "VMK in component Wnt_parameters (flux)"
    legend_constants[48] = "VMP in component Wnt_parameters (flux)"
    legend_states[12] = "Rasa in component Rasa (nanomolar)"
    legend_algebraic[9] = "VaRas in component FGF_parameters (flux)"
    legend_algebraic[14] = "VdRas in component FGF_parameters (flux)"
    legend_constants[49] = "eta in component model_parameters (dimensionless)"
    legend_states[13] = "ERKa in component ERKa (nanomolar)"
    legend_algebraic[10] = "VaErk in component FGF_parameters (flux)"
    legend_algebraic[15] = "VdErk in component FGF_parameters (flux)"
    legend_algebraic[11] = "VaX in component FGF_parameters (flux)"
    legend_algebraic[16] = "VdX in component FGF_parameters (flux)"
    legend_states[14] = "MDusp in component MDusp (nanomolar)"
    legend_algebraic[6] = "VsMDusp in component FGF_parameters (flux)"
    legend_algebraic[12] = "VdMDusp in component FGF_parameters (flux)"
    legend_states[15] = "Dusp in component Dusp (nanomolar)"
    legend_constants[50] = "ksDusp in component Dusp (first_order_rate_constant)"
    legend_constants[51] = "vdDusp in component Dusp (flux)"
    legend_constants[52] = "KdDusp in component Dusp (nanomolar)"
    legend_algebraic[3] = "Rasi in component FGF_parameters (nanomolar)"
    legend_algebraic[4] = "ERKi in component FGF_parameters (nanomolar)"
    legend_algebraic[5] = "Xi in component FGF_parameters (nanomolar)"
    legend_constants[53] = "Rast in component FGF_parameters (nanomolar)"
    legend_constants[54] = "ERKt in component FGF_parameters (nanomolar)"
    legend_constants[55] = "Xt in component FGF_parameters (nanomolar)"
    legend_constants[56] = "kcDusp in component FGF_parameters (first_order_rate_constant)"
    legend_constants[57] = "VMaRas in component FGF_parameters (flux)"
    legend_constants[58] = "VMdRas in component FGF_parameters (flux)"
    legend_constants[59] = "VMaErk in component FGF_parameters (flux)"
    legend_constants[60] = "VMaX in component FGF_parameters (flux)"
    legend_constants[61] = "VMdX in component FGF_parameters (flux)"
    legend_constants[62] = "VMsMDusp in component FGF_parameters (flux)"
    legend_constants[63] = "VMdMDusp in component FGF_parameters (flux)"
    legend_constants[64] = "Fgf in component FGF_parameters (nanomolar)"
    legend_constants[65] = "KaFgf in component FGF_parameters (nanomolar)"
    legend_constants[66] = "KaRas in component FGF_parameters (nanomolar)"
    legend_constants[67] = "KdRas in component FGF_parameters (nanomolar)"
    legend_constants[68] = "KdErk in component FGF_parameters (nanomolar)"
    legend_constants[69] = "KaErk in component FGF_parameters (nanomolar)"
    legend_constants[70] = "KaX in component FGF_parameters (nanomolar)"
    legend_constants[71] = "KdX in component FGF_parameters (nanomolar)"
    legend_constants[72] = "KaMDusp in component FGF_parameters (nanomolar)"
    legend_constants[73] = "KdMDusp in component FGF_parameters (nanomolar)"
    legend_constants[74] = "q in component FGF_parameters (dimensionless)"
    legend_constants[75] = "r in component FGF_parameters (dimensionless)"
    legend_rates[0] = "d/dt N in component N (nanomolar)"
    legend_rates[2] = "d/dt Na in component Na (nanomolar)"
    legend_rates[3] = "d/dt Nan in component Nan (nanomolar)"
    legend_rates[4] = "d/dt MF in component MF (nanomolar)"
    legend_rates[1] = "d/dt F in component F (nanomolar)"
    legend_rates[5] = "d/dt K in component K (nanomolar)"
    legend_rates[6] = "d/dt B in component B (nanomolar)"
    legend_rates[7] = "d/dt Bp in component Bp (nanomolar)"
    legend_rates[8] = "d/dt BN in component BN (nanomolar)"
    legend_rates[9] = "d/dt MAx in component MAx (nanomolar)"
    legend_rates[11] = "d/dt A in component A (nanomolar)"
    legend_rates[12] = "d/dt Rasa in component Rasa (nanomolar)"
    legend_rates[13] = "d/dt ERKa in component ERKa (nanomolar)"
    legend_rates[10] = "d/dt Xa in component Xa (nanomolar)"
    legend_rates[14] = "d/dt MDusp in component MDusp (nanomolar)"
    legend_rates[15] = "d/dt Dusp in component Dusp (nanomolar)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 0.5
    constants[0] = 1.4
    constants[1] = 0.23
    constants[2] = 2.82
    constants[3] = 3.45
    constants[4] = 0.5
    states[1] = 0.001
    constants[5] = 0.3
    constants[6] = 2.0
    states[2] = 0.2
    constants[7] = 0.001
    constants[8] = 0.01
    constants[9] = 0.1
    constants[10] = 0.1
    states[3] = 0.0
    constants[11] = 0.001
    constants[12] = 0.1
    states[4] = 0.1
    constants[13] = 0.768
    constants[14] = 2.5
    constants[15] = 3.0
    constants[16] = 1.92
    constants[17] = 0.05
    states[5] = 3.0
    constants[18] = 2.0
    constants[19] = 0.37
    constants[20] = 0.39
    constants[21] = 0.3
    constants[22] = 1.5
    states[6] = 0.1
    constants[23] = 0.0
    constants[24] = 0.087
    constants[25] = 3.0
    states[7] = 0.1
    constants[26] = 7.062
    states[8] = 0.001
    states[9] = 0.1
    constants[27] = 0.06
    constants[28] = 1.64
    constants[29] = 0.8
    constants[30] = 0.7
    constants[31] = 0.05
    constants[32] = 0.48
    constants[33] = 2.0
    constants[34] = 2.0
    constants[35] = 0.5
    states[10] = 0.1
    states[11] = 0.1
    constants[36] = 0.02
    constants[37] = 0.6
    constants[38] = 0.63
    constants[39] = 0.1
    constants[40] = 1.8
    constants[41] = 0.28
    constants[42] = 0.03
    constants[43] = 2.0
    constants[44] = 0.5
    constants[45] = 0.7
    constants[46] = 1.5
    constants[47] = 5.08
    constants[48] = 1.0
    states[12] = 0.5
    constants[49] = 0.3
    states[13] = 0.2
    states[14] = 0.1
    states[15] = 0.1
    constants[50] = 0.5
    constants[51] = 2.0
    constants[52] = 0.5
    constants[53] = 2.0
    constants[54] = 2.0
    constants[55] = 2.0
    constants[56] = 1.35
    constants[57] = 4.968
    constants[58] = 0.41
    constants[59] = 3.30
    constants[60] = 1.6
    constants[61] = 0.5
    constants[62] = 0.9
    constants[63] = 0.5
    constants[64] = 1.0
    constants[65] = 0.5
    constants[66] = 0.103
    constants[67] = 0.1
    constants[68] = 0.05
    constants[69] = 0.05
    constants[70] = 0.05
    constants[71] = 0.05
    constants[72] = 0.5
    constants[73] = 0.5
    constants[74] = 2.0
    constants[75] = 2.0
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[0] = constants[5]*(constants[1]-(constants[2]*(states[0]/(constants[0]+states[0]))+constants[3]*states[0]*((power(constants[4], constants[6]))/(power(constants[4], constants[6])+power(states[1], constants[6])))))
    rates[1] = constants[5]*(constants[21]*states[4]-constants[20]*(states[1]/(constants[19]+states[1])))
    rates[9] = constants[22]*((constants[27]+constants[28]*((power(states[8], constants[33]))/(power(constants[30], constants[33])+power(states[8], constants[33])))+constants[35]*((power(states[10], constants[34]))/(power(constants[31], constants[34])+power(states[10], constants[34]))))-constants[29]*(states[9]/(constants[32]+states[9])))
    rates[15] = constants[49]*(constants[50]*states[14]-constants[51]*(states[15]/(constants[52]+states[15])))
    algebraic[0] = constants[9]*states[2]-constants[10]*states[3]
    rates[2] = constants[5]*(constants[3]*states[0]*((power(constants[4], constants[6]))/(power(constants[4], constants[6])+power(states[1], constants[6])))-(constants[8]*(states[2]/(constants[7]+states[2]))+algebraic[0]))
    rates[3] = constants[5]*(algebraic[0]-constants[12]*(states[3]/(constants[11]+states[3])))
    algebraic[1] = constants[15]*(constants[14]/(constants[14]+states[5]))
    rates[4] = constants[5]*(algebraic[1]*((power(states[3], constants[18]))/(power(constants[17], constants[18])+power(states[3], constants[18])))-constants[16]*(states[4]/(constants[13]+states[4])))
    algebraic[2] = constants[25]-states[5]
    algebraic[7] = constants[39]*algebraic[2]-constants[40]*states[11]*states[5]
    rates[5] = constants[22]*algebraic[7]
    algebraic[8] = constants[46]*states[8]-constants[45]*states[6]
    rates[8] = -(constants[22]*algebraic[8])
    rates[11] = constants[22]*((constants[36]*states[9]+algebraic[7])-constants[37]*(states[11]/(constants[38]+states[11])))
    algebraic[6] = constants[62]*((power(states[10], constants[74]))/(power(constants[72], constants[74])+power(states[10], constants[74])))
    algebraic[12] = constants[63]*(states[14]/(constants[73]+states[14]))
    rates[14] = constants[49]*(algebraic[6]-algebraic[12])
    algebraic[3] = constants[53]-states[12]
    algebraic[9] = constants[57]*((power(constants[64], constants[75]))/(power(constants[65], constants[75])+power(constants[64], constants[75])))*(algebraic[3]/(constants[66]+algebraic[3]))
    algebraic[14] = constants[58]*(states[12]/(constants[67]+states[12]))
    rates[12] = constants[49]*(algebraic[9]-algebraic[14])
    algebraic[4] = constants[54]-states[13]
    algebraic[10] = constants[59]*(states[12]/constants[53])*(algebraic[4]/(constants[69]+algebraic[4]))
    algebraic[15] = constants[56]*states[15]*(states[13]/(constants[68]+states[13]))
    rates[13] = constants[49]*(algebraic[10]-algebraic[15])
    algebraic[5] = constants[55]-states[10]
    algebraic[11] = constants[60]*(states[13]/constants[54])*(algebraic[5]/(constants[70]+algebraic[5]))
    algebraic[16] = constants[61]*(states[10]/(constants[71]+states[10]))
    rates[10] = constants[49]*(algebraic[11]-algebraic[16])
    algebraic[13] = constants[47]*(constants[44]/(constants[44]+constants[43]))*(states[6]/(constants[41]+states[6]))
    algebraic[17] = constants[48]*(states[7]/(constants[42]+states[7]))
    rates[6] = constants[22]*((constants[24]+algebraic[17]+algebraic[8])-(algebraic[13]*(algebraic[2]/constants[25])+constants[23]*states[6]))
    rates[7] = constants[22]*(algebraic[13]*(algebraic[2]/constants[25])-(algebraic[17]+constants[26]*states[7]))
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = constants[9]*states[2]-constants[10]*states[3]
    algebraic[1] = constants[15]*(constants[14]/(constants[14]+states[5]))
    algebraic[2] = constants[25]-states[5]
    algebraic[7] = constants[39]*algebraic[2]-constants[40]*states[11]*states[5]
    algebraic[8] = constants[46]*states[8]-constants[45]*states[6]
    algebraic[6] = constants[62]*((power(states[10], constants[74]))/(power(constants[72], constants[74])+power(states[10], constants[74])))
    algebraic[12] = constants[63]*(states[14]/(constants[73]+states[14]))
    algebraic[3] = constants[53]-states[12]
    algebraic[9] = constants[57]*((power(constants[64], constants[75]))/(power(constants[65], constants[75])+power(constants[64], constants[75])))*(algebraic[3]/(constants[66]+algebraic[3]))
    algebraic[14] = constants[58]*(states[12]/(constants[67]+states[12]))
    algebraic[4] = constants[54]-states[13]
    algebraic[10] = constants[59]*(states[12]/constants[53])*(algebraic[4]/(constants[69]+algebraic[4]))
    algebraic[15] = constants[56]*states[15]*(states[13]/(constants[68]+states[13]))
    algebraic[5] = constants[55]-states[10]
    algebraic[11] = constants[60]*(states[13]/constants[54])*(algebraic[5]/(constants[70]+algebraic[5]))
    algebraic[16] = constants[61]*(states[10]/(constants[71]+states[10]))
    algebraic[13] = constants[47]*(constants[44]/(constants[44]+constants[43]))*(states[6]/(constants[41]+states[6]))
    algebraic[17] = constants[48]*(states[7]/(constants[42]+states[7]))
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
        self.KdN = 1.4
        self.vsN = 0.23
        self.vdN = 2.82
        self.kc = 3.45
        self.KIF = 0.5
        self.epsilon = 0.3
        self.j = 2.0
        self.KdNa = 0.001
        self.VdNa = 0.01
        self.kt1 = 0.1
        self.kt2 = 0.1
        self.KdNan = 0.001
        self.VdNan = 0.1
        self.KdMF = 0.768
        self.KIG1 = 2.5
        self.vsF = 3.0
        self.vmF = 1.92
        self.KA = 0.05
        self.p = 2.0
        self.KdF = 0.37
        self.vdF = 0.39
        self.ksF = 0.3
        self.theta = 1.5
        self.kd1 = 0.0
        self.vsB = 0.087
        self.Kt = 3.0
        self.kd2 = 7.062
        self.v0 = 0.06
        self.vMB = 1.64
        self.vmd = 0.8
        self.KaB = 0.7
        self.KaXa = 0.05
        self.Kmd = 0.48
        self.n = 2.0
        self.m = 2.0
        self.vMXa = 0.5
        self.ksAx = 0.02
        self.vdAx = 0.6
        self.KdAx = 0.63
        self.d1 = 0.1
        self.a1 = 1.8
        self.K1 = 0.28
        self.K2 = 0.03
        self.D = 2.0
        self.KID = 0.5
        self.kt3 = 0.7
        self.kt4 = 1.5
        self.VMK = 5.08
        self.VMP = 1.0
        self.eta = 0.3
        self.ksDusp = 0.5
        self.vdDusp = 2.0
        self.KdDusp = 0.5
        self.Rast = 2.0
        self.ERKt = 2.0
        self.Xt = 2.0
        self.kcDusp = 1.35
        self.VMaRas = 4.968
        self.VMdRas = 0.41
        self.VMaErk = 3.30
        self.VMaX = 1.6
        self.VMdX = 0.5
        self.VMsMDusp = 0.9
        self.VMdMDusp = 0.5
        self.Fgf = 1.0
        self.KaFgf = 0.5
        self.KaRas = 0.103
        self.KdRas = 0.1
        self.KdErk = 0.05
        self.KaErk = 0.05
        self.KaX = 0.05
        self.KdX = 0.05
        self.KaMDusp = 0.5
        self.KdMDusp = 0.5
        self.q = 2.0
        self.r = 2.0

    def to_dict(self):
        return {
            "KdN": self.KdN,
            "vsN": self.vsN,
            "vdN": self.vdN,
            "kc": self.kc,
            "KIF": self.KIF,
            "epsilon": self.epsilon,
            "j": self.j,
            "KdNa": self.KdNa,
            "VdNa": self.VdNa,
            "kt1": self.kt1,
            "kt2": self.kt2,
            "KdNan": self.KdNan,
            "VdNan": self.VdNan,
            "KdMF": self.KdMF,
            "KIG1": self.KIG1,
            "vsF": self.vsF,
            "vmF": self.vmF,
            "KA": self.KA,
            "p": self.p,
            "KdF": self.KdF,
            "vdF": self.vdF,
            "ksF": self.ksF,
            "theta": self.theta,
            "kd1": self.kd1,
            "vsB": self.vsB,
            "Kt": self.Kt,
            "kd2": self.kd2,
            "v0": self.v0,
            "vMB": self.vMB,
            "vmd": self.vmd,
            "KaB": self.KaB,
            "KaXa": self.KaXa,
            "Kmd": self.Kmd,
            "n": self.n,
            "m": self.m,
            "vMXa": self.vMXa,
            "ksAx": self.ksAx,
            "vdAx": self.vdAx,
            "KdAx": self.KdAx,
            "d1": self.d1,
            "a1": self.a1,
            "K1": self.K1,
            "K2": self.K2,
            "D": self.D,
            "KID": self.KID,
            "kt3": self.kt3,
            "kt4": self.kt4,
            "VMK": self.VMK,
            "VMP": self.VMP,
            "eta": self.eta,
            "ksDusp": self.ksDusp,
            "vdDusp": self.vdDusp,
            "KdDusp": self.KdDusp,
            "Rast": self.Rast,
            "ERKt": self.ERKt,
            "Xt": self.Xt,
            "kcDusp": self.kcDusp,
            "VMaRas": self.VMaRas,
            "VMdRas": self.VMdRas,
            "VMaErk": self.VMaErk,
            "VMaX": self.VMaX,
            "VMdX": self.VMdX,
            "VMsMDusp": self.VMsMDusp,
            "VMdMDusp": self.VMdMDusp,
            "Fgf": self.Fgf,
            "KaFgf": self.KaFgf,
            "KaRas": self.KaRas,
            "KdRas": self.KdRas,
            "KdErk": self.KdErk,
            "KaErk": self.KaErk,
            "KaX": self.KaX,
            "KdX": self.KdX,
            "KaMDusp": self.KaMDusp,
            "KdMDusp": self.KdMDusp,
            "q": self.q,
            "r": self.r,
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
        y0=[0.5, 0.001, 0.2, 0.0, 0.1, 3.0, 0.1, 0.1, 0.001, 0.1, 0.1, 0.1, 0.5, 0.2, 0.1, 0.1],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "goldbeter_pourquie_2008_a"
        self.curve_names = [
            "N",
            "F",
            "Na",
            "Nan",
            "MF",
            "K",
            "B",
            "Bp",
            "BN",
            "MAx",
            "Xa",
            "A",
            "Rasa",
            "ERKa",
            "MDusp",
            "Dusp",
        ]
        self.state_names = ['N', 'F', 'Na', 'Nan', 'MF', 'K', 'B', 'Bp', 'BN', 'MAx', 'Xa', 'A', 'Rasa', 'ERKa', 'MDusp', 'Dusp']
        self.algebraic_names = ['Vtr', 'vsFK', 'AK', 'Rasi', 'ERKi', 'Xi', 'VsMDusp', 'V1', 'V2', 'VaRas', 'VaErk', 'VaX', 'VdMDusp', 'VK', 'VdRas', 'VdErk', 'VdX', 'VP']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 76
        p = self.params

        # direct mapping
        c[0] = p.KdN
        c[1] = p.vsN
        c[2] = p.vdN
        c[3] = p.kc
        c[4] = p.KIF
        c[5] = p.epsilon
        c[6] = p.j
        c[7] = p.KdNa
        c[8] = p.VdNa
        c[9] = p.kt1
        c[10] = p.kt2
        c[11] = p.KdNan
        c[12] = p.VdNan
        c[13] = p.KdMF
        c[14] = p.KIG1
        c[15] = p.vsF
        c[16] = p.vmF
        c[17] = p.KA
        c[18] = p.p
        c[19] = p.KdF
        c[20] = p.vdF
        c[21] = p.ksF
        c[22] = p.theta
        c[23] = p.kd1
        c[24] = p.vsB
        c[25] = p.Kt
        c[26] = p.kd2
        c[27] = p.v0
        c[28] = p.vMB
        c[29] = p.vmd
        c[30] = p.KaB
        c[31] = p.KaXa
        c[32] = p.Kmd
        c[33] = p.n
        c[34] = p.m
        c[35] = p.vMXa
        c[36] = p.ksAx
        c[37] = p.vdAx
        c[38] = p.KdAx
        c[39] = p.d1
        c[40] = p.a1
        c[41] = p.K1
        c[42] = p.K2
        c[43] = p.D
        c[44] = p.KID
        c[45] = p.kt3
        c[46] = p.kt4
        c[47] = p.VMK
        c[48] = p.VMP
        c[49] = p.eta
        c[50] = p.ksDusp
        c[51] = p.vdDusp
        c[52] = p.KdDusp
        c[53] = p.Rast
        c[54] = p.ERKt
        c[55] = p.Xt
        c[56] = p.kcDusp
        c[57] = p.VMaRas
        c[58] = p.VMdRas
        c[59] = p.VMaErk
        c[60] = p.VMaX
        c[61] = p.VMdX
        c[62] = p.VMsMDusp
        c[63] = p.VMdMDusp
        c[64] = p.Fgf
        c[65] = p.KaFgf
        c[66] = p.KaRas
        c[67] = p.KdRas
        c[68] = p.KdErk
        c[69] = p.KaErk
        c[70] = p.KaX
        c[71] = p.KdX
        c[72] = p.KaMDusp
        c[73] = p.KdMDusp
        c[74] = p.q
        c[75] = p.r

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
