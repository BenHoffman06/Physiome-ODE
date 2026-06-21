# Size of variable arrays:
sizeAlgebraic = 21
sizeStates = 8
sizeConstants = 55
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
    legend_algebraic[8] = "I_iCa in component membrane (picoampere)"
    legend_algebraic[11] = "I_iNa in component membrane (picoampere)"
    legend_constants[0] = "Cm in component membrane (picofarad)"
    legend_algebraic[2] = "I_Ca in component I_Ca (picoampere)"
    legend_algebraic[9] = "I_Na in component I_Na (picoampere)"
    legend_algebraic[4] = "I_NSCC_Ca in component I_NSCC_Ca (picoampere)"
    legend_algebraic[7] = "I_PM in component I_PM (picoampere)"
    legend_algebraic[6] = "I_NSCC_Na in component I_NSCC_Na (picoampere)"
    legend_constants[1] = "gCa in component I_Ca (picosiemens)"
    legend_algebraic[0] = "ECa in component I_Ca (millivolt)"
    legend_constants[2] = "T in component model_parameters (kelvin)"
    legend_constants[3] = "R in component model_parameters (attojoule_per_zeptomole_kelvin)"
    legend_constants[4] = "F in component model_parameters (femtocoulomb_per_zeptomole)"
    legend_constants[5] = "CO in component model_parameters (micromolar)"
    legend_states[1] = "CS1 in component CS1 (micromolar)"
    legend_constants[6] = "gNSCC_Ca_ in component I_NSCC_Ca (picosiemens)"
    legend_algebraic[3] = "gNSCC_Ca in component I_NSCC_Ca (picosiemens)"
    legend_constants[7] = "hNSCC in component model_parameters (dimensionless)"
    legend_constants[8] = "ENSCC in component model_parameters (millivolt)"
    legend_constants[9] = "KNSCC in component model_parameters (micromolar)"
    legend_constants[10] = "gNSCC_Na_ in component I_NSCC_Na (picosiemens)"
    legend_algebraic[5] = "gNSCC_Na in component I_NSCC_Na (picosiemens)"
    legend_constants[11] = "gPM in component I_PM (femtoampere)"
    legend_constants[12] = "KPM in component I_PM (micromolar)"
    legend_constants[13] = "gNa in component I_Na (femtoampere)"
    legend_constants[14] = "KNa in component I_Na (micromolar)"
    legend_constants[15] = "hNa in component I_Na (dimensionless)"
    legend_states[2] = "NS1 in component NS1 (micromolar)"
    legend_algebraic[10] = "JSERCA in component JSERCA (flux)"
    legend_constants[16] = "VSERCA in component JSERCA (first_order_rate_constant)"
    legend_constants[17] = "A2 in component JSERCA (dimensionless)"
    legend_constants[18] = "A4 in component JSERCA (per_micromolar)"
    legend_constants[19] = "A5 in component JSERCA (per_micromolar)"
    legend_constants[20] = "A6 in component JSERCA (per_micromolar2)"
    legend_states[3] = "CER in component CER (micromolar)"
    legend_algebraic[13] = "JMCU in component JMCU (flux)"
    legend_constants[21] = "VMCU in component JMCU (flux)"
    legend_constants[22] = "KMCU in component JMCU (micromolar)"
    legend_algebraic[12] = "epsilon_INH in component JMCU (dimensionless)"
    legend_constants[23] = "KINH in component JMCU (micromolar)"
    legend_constants[24] = "hINH in component JMCU (dimensionless)"
    legend_states[4] = "CS2 in component CS2 (micromolar)"
    legend_states[5] = "CMT in component CMT (micromolar)"
    legend_algebraic[14] = "JNCX in component JNCX (flux)"
    legend_constants[25] = "VNCX in component JNCX (flux)"
    legend_constants[26] = "KNCX in component JNCX (micromolar)"
    legend_algebraic[15] = "JS1S2 in component JS1S2 (flux)"
    legend_constants[27] = "mu_S1S2 in component JS1S2 (first_order_rate_constant)"
    legend_algebraic[19] = "JIPR in component JIPR (flux)"
    legend_constants[28] = "kIPR in component JIPR (first_order_rate_constant)"
    legend_constants[29] = "k_1 in component JIPR (flux)"
    legend_constants[30] = "k1 in component JIPR (first_order_rate_constant)"
    legend_constants[31] = "k2 in component JIPR (first_order_rate_constant)"
    legend_constants[32] = "r2 in component JIPR (first_order_rate_constant)"
    legend_constants[33] = "r_2 in component JIPR (flux)"
    legend_constants[34] = "r4 in component JIPR (first_order_rate_constant)"
    legend_constants[35] = "R1 in component JIPR (micromolar)"
    legend_constants[36] = "R3 in component JIPR (micromolar)"
    legend_algebraic[17] = "phi1 in component JIPR (first_order_rate_constant)"
    legend_algebraic[18] = "phi_1 in component JIPR (flux)"
    legend_algebraic[20] = "phi2 in component JIPR (first_order_rate_constant)"
    legend_states[6] = "phi3 in component JIPR (first_order_rate_constant)"
    legend_states[7] = "H in component JIPR (dimensionless)"
    legend_constants[37] = "g_beta in component JIPR (first_order_rate_constant)"
    legend_constants[38] = "h_beta in component JIPR (dimensionless)"
    legend_constants[39] = "g_alpha in component JIPR (per_second_squared)"
    legend_constants[40] = "K_beta in component JIPR (micromolar)"
    legend_constants[50] = "alpha_phi3 in component JIPR (per_second_squared)"
    legend_algebraic[1] = "beta_phi3 in component JIPR (first_order_rate_constant)"
    legend_constants[41] = "P in component model_parameters (micromolar)"
    legend_constants[49] = "lambda_MT_S1 in component CS1 (dimensionless)"
    legend_constants[51] = "lambda_ER_S1 in component CS1 (dimensionless)"
    legend_constants[42] = "delta_s in component model_parameters (micromolar_coulomb)"
    legend_constants[43] = "gamma_S1 in component model_parameters (dimensionless)"
    legend_constants[44] = "gamma_MT in component model_parameters (dimensionless)"
    legend_constants[45] = "gamma_ER in component model_parameters (dimensionless)"
    legend_constants[52] = "lambda_MT_S2 in component CS2 (dimensionless)"
    legend_constants[53] = "lambda_ER_S2 in component CS2 (dimensionless)"
    legend_constants[54] = "lambda_S1_S2 in component CS2 (dimensionless)"
    legend_constants[46] = "gamma_S2 in component model_parameters (dimensionless)"
    legend_algebraic[16] = "fm in component CMT (dimensionless)"
    legend_constants[47] = "Km in component CMT (micromolar)"
    legend_constants[48] = "Bm in component CMT (micromolar)"
    legend_rates[0] = "d/dt Vm in component membrane (millivolt)"
    legend_rates[7] = "d/dt H in component JIPR (dimensionless)"
    legend_rates[6] = "d/dt phi3 in component JIPR (first_order_rate_constant)"
    legend_rates[1] = "d/dt CS1 in component CS1 (micromolar)"
    legend_rates[4] = "d/dt CS2 in component CS2 (micromolar)"
    legend_rates[3] = "d/dt CER in component CER (micromolar)"
    legend_rates[5] = "d/dt CMT in component CMT (micromolar)"
    legend_rates[2] = "d/dt NS1 in component NS1 (micromolar)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = -70.1
    constants[0] = 20.0
    constants[1] = 0.01
    constants[2] = 310.16
    constants[3] = 8.314E-3
    constants[4] = 0.09649
    constants[5] = 1.8E3
    states[1] = 0.120
    constants[6] = 0.12
    constants[7] = 3.0
    constants[8] = 0.0
    constants[9] = 0.12
    constants[10] = 220.0
    constants[11] = 420.0
    constants[12] = 1.0
    constants[13] = 1.5E4
    constants[14] = 1.0E4
    constants[15] = 4.0
    states[2] = 1.01E4
    constants[16] = 1.0E5
    constants[17] = 6E-4
    constants[18] = 3.57
    constants[19] = 2.7E-5
    constants[20] = 2.31E-5
    states[3] = 203.0
    constants[21] = 800.0
    constants[22] = 10.0
    constants[23] = 10.0
    constants[24] = 4.0
    states[4] = 0.023
    states[5] = 0.220
    constants[25] = 0.5
    constants[26] = 0.3
    constants[27] = 0.04
    constants[28] = 2000.0
    constants[29] = 6.4
    constants[30] = 0.0
    constants[31] = 4.0
    constants[32] = 200.0
    constants[33] = 0.0
    constants[34] = 750.0
    constants[35] = 36.0
    constants[36] = 300.0
    states[6] = 0.306
    states[7] = 0.787
    constants[37] = 300.0
    constants[38] = 2.0
    constants[39] = 0.02
    constants[40] = 2.0
    constants[41] = 1.0
    constants[42] = 26.0
    constants[43] = 100.0
    constants[44] = 200.0
    constants[45] = 20.0
    constants[46] = 1.0
    constants[47] = 0.01
    constants[48] = 100.0
    constants[49] = constants[44]/constants[43]
    constants[50] = constants[39]
    constants[51] = constants[45]/constants[43]
    constants[52] = constants[44]/constants[46]
    constants[53] = constants[45]/constants[46]
    constants[54] = constants[43]/constants[46]
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[1] = constants[37]*((power(states[4], constants[38]))/(power(constants[40], constants[38])+power(states[4], constants[38])))
    rates[6] = constants[50]-algebraic[1]*states[6]
    algebraic[0] = ((constants[3]*constants[2])/(2.00000*constants[4]))*log(constants[5]/states[1])
    algebraic[2] = constants[1]*(states[0]-algebraic[0])
    algebraic[3] = constants[6]*((power(constants[9], constants[7]))/(power(constants[9], constants[7])+power(states[1], constants[7])))
    algebraic[4] = algebraic[3]*(states[0]-constants[8])
    algebraic[7] = constants[11]*((power(states[1], 2.00000))/(power(constants[12], 2.00000)+power(states[1], 2.00000)))
    algebraic[8] = algebraic[2]+algebraic[4]+algebraic[7]
    algebraic[9] = constants[13]*((power(states[2], constants[15]))/(power(constants[14], constants[15])+power(states[2], constants[15])))
    algebraic[5] = constants[10]*((power(constants[9], constants[7]))/(power(constants[9], constants[7])+power(states[1], constants[7])))
    algebraic[6] = algebraic[5]*(states[0]-constants[8])
    algebraic[11] = algebraic[6]+algebraic[9]
    rates[0] = -((algebraic[8]+algebraic[11])/constants[0])
    rates[2] = -(constants[42]/1.00000)*algebraic[11]
    algebraic[10] = (constants[16]*(states[1]-constants[17]*states[3]))/(1.00000+constants[18]*states[1]+constants[19]*states[3]+constants[20]*states[1]*states[3])
    algebraic[14] = constants[25]*(states[5]/(states[5]+constants[26]))
    algebraic[15] = constants[27]*(states[4]-states[1])
    rates[1] = (algebraic[15]+constants[49]*algebraic[14])-((constants[42]/2.00000)*algebraic[8]+constants[51]*algebraic[10])
    algebraic[12] = (power(constants[23], constants[24]))/(power(constants[23], constants[24])+power(states[5], constants[24]))
    algebraic[13] = constants[21]*((power(states[4], 2.00000))/(power(constants[22], 2.00000)+power(states[4], 2.00000)))*algebraic[12]
    algebraic[16] = 1.00000/(1.00000+(constants[47]*constants[48])/(power(constants[47]+states[5], 2.00000)))
    rates[5] = algebraic[16]*(algebraic[13]-algebraic[14])
    algebraic[17] = (constants[30]*constants[35]+constants[32]*states[4])/(constants[35]+states[4])
    algebraic[18] = ((constants[29]+constants[33])*constants[36])/(constants[36]+states[4])
    algebraic[20] = (constants[31]*constants[36]+constants[34]*states[4])/(constants[36]+states[4])
    rates[7] = states[6]*(1.00000-states[7])-((constants[41]*algebraic[17]*algebraic[20])/(constants[41]*algebraic[17]+algebraic[18]))*states[7]
    algebraic[19] = constants[28]*(power((constants[41]*algebraic[17]*states[7])/(constants[41]*algebraic[17]+algebraic[18]), 4.00000))*(states[3]-states[4])
    rates[4] = constants[53]*algebraic[19]-(constants[54]*algebraic[15]+constants[52]*algebraic[13])
    rates[3] = algebraic[10]-algebraic[19]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[1] = constants[37]*((power(states[4], constants[38]))/(power(constants[40], constants[38])+power(states[4], constants[38])))
    algebraic[0] = ((constants[3]*constants[2])/(2.00000*constants[4]))*log(constants[5]/states[1])
    algebraic[2] = constants[1]*(states[0]-algebraic[0])
    algebraic[3] = constants[6]*((power(constants[9], constants[7]))/(power(constants[9], constants[7])+power(states[1], constants[7])))
    algebraic[4] = algebraic[3]*(states[0]-constants[8])
    algebraic[7] = constants[11]*((power(states[1], 2.00000))/(power(constants[12], 2.00000)+power(states[1], 2.00000)))
    algebraic[8] = algebraic[2]+algebraic[4]+algebraic[7]
    algebraic[9] = constants[13]*((power(states[2], constants[15]))/(power(constants[14], constants[15])+power(states[2], constants[15])))
    algebraic[5] = constants[10]*((power(constants[9], constants[7]))/(power(constants[9], constants[7])+power(states[1], constants[7])))
    algebraic[6] = algebraic[5]*(states[0]-constants[8])
    algebraic[11] = algebraic[6]+algebraic[9]
    algebraic[10] = (constants[16]*(states[1]-constants[17]*states[3]))/(1.00000+constants[18]*states[1]+constants[19]*states[3]+constants[20]*states[1]*states[3])
    algebraic[14] = constants[25]*(states[5]/(states[5]+constants[26]))
    algebraic[15] = constants[27]*(states[4]-states[1])
    algebraic[12] = (power(constants[23], constants[24]))/(power(constants[23], constants[24])+power(states[5], constants[24]))
    algebraic[13] = constants[21]*((power(states[4], 2.00000))/(power(constants[22], 2.00000)+power(states[4], 2.00000)))*algebraic[12]
    algebraic[16] = 1.00000/(1.00000+(constants[47]*constants[48])/(power(constants[47]+states[5], 2.00000)))
    algebraic[17] = (constants[30]*constants[35]+constants[32]*states[4])/(constants[35]+states[4])
    algebraic[18] = ((constants[29]+constants[33])*constants[36])/(constants[36]+states[4])
    algebraic[20] = (constants[31]*constants[36]+constants[34]*states[4])/(constants[36]+states[4])
    algebraic[19] = constants[28]*(power((constants[41]*algebraic[17]*states[7])/(constants[41]*algebraic[17]+algebraic[18]), 4.00000))*(states[3]-states[4])
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
        self.Cm = 20.0
        self.gCa = 0.01
        self.T = 310.16
        self.R = 8.314E-3
        self.F = 0.09649
        self.CO = 1.8E3
        self.gNSCC_Ca_ = 0.12
        self.hNSCC = 3.0
        self.ENSCC = 0.0
        self.KNSCC = 0.12
        self.gNSCC_Na_ = 220.0
        self.gPM = 420.0
        self.KPM = 1.0
        self.gNa = 1.5E4
        self.KNa = 1.0E4
        self.hNa = 4.0
        self.VSERCA = 1.0E5
        self.A2 = 6E-4
        self.A4 = 3.57
        self.A5 = 2.7E-5
        self.A6 = 2.31E-5
        self.VMCU = 800.0
        self.KMCU = 10.0
        self.KINH = 10.0
        self.hINH = 4.0
        self.VNCX = 0.5
        self.KNCX = 0.3
        self.mu_S1S2 = 0.04
        self.kIPR = 2000.0
        self.k_1 = 6.4
        self.k1 = 0.0
        self.k2 = 4.0
        self.r2 = 200.0
        self.r_2 = 0.0
        self.r4 = 750.0
        self.R1 = 36.0
        self.R3 = 300.0
        self.g_beta = 300.0
        self.h_beta = 2.0
        self.g_alpha = 0.02
        self.K_beta = 2.0
        self.P = 1.0
        self.delta_s = 26.0
        self.gamma_S1 = 100.0
        self.gamma_MT = 200.0
        self.gamma_ER = 20.0
        self.gamma_S2 = 1.0
        self.Km = 0.01
        self.Bm = 100.0

    def to_dict(self):
        return {
            "Cm": self.Cm,
            "gCa": self.gCa,
            "T": self.T,
            "R": self.R,
            "F": self.F,
            "CO": self.CO,
            "gNSCC_Ca_": self.gNSCC_Ca_,
            "hNSCC": self.hNSCC,
            "ENSCC": self.ENSCC,
            "KNSCC": self.KNSCC,
            "gNSCC_Na_": self.gNSCC_Na_,
            "gPM": self.gPM,
            "KPM": self.KPM,
            "gNa": self.gNa,
            "KNa": self.KNa,
            "hNa": self.hNa,
            "VSERCA": self.VSERCA,
            "A2": self.A2,
            "A4": self.A4,
            "A5": self.A5,
            "A6": self.A6,
            "VMCU": self.VMCU,
            "KMCU": self.KMCU,
            "KINH": self.KINH,
            "hINH": self.hINH,
            "VNCX": self.VNCX,
            "KNCX": self.KNCX,
            "mu_S1S2": self.mu_S1S2,
            "kIPR": self.kIPR,
            "k_1": self.k_1,
            "k1": self.k1,
            "k2": self.k2,
            "r2": self.r2,
            "r_2": self.r_2,
            "r4": self.r4,
            "R1": self.R1,
            "R3": self.R3,
            "g_beta": self.g_beta,
            "h_beta": self.h_beta,
            "g_alpha": self.g_alpha,
            "K_beta": self.K_beta,
            "P": self.P,
            "delta_s": self.delta_s,
            "gamma_S1": self.gamma_S1,
            "gamma_MT": self.gamma_MT,
            "gamma_ER": self.gamma_ER,
            "gamma_S2": self.gamma_S2,
            "Km": self.Km,
            "Bm": self.Bm,
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
        y0=[-70.1, 0.120, 1.01E4, 203.0, 0.023, 0.220, 0.306, 0.787],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "faville_pullan_sanders_smith_2008"
        self.curve_names = [
            "Vm",
            "CS1",
            "NS1",
            "CER",
            "CS2",
            "CMT",
            "phi3",
            "H",
        ]
        self.state_names = ['Vm', 'CS1', 'NS1', 'CER', 'CS2', 'CMT', 'phi3', 'H']
        self.algebraic_names = ['ECa', 'beta_phi3', 'I_Ca', 'gNSCC_Ca', 'I_NSCC_Ca', 'gNSCC_Na', 'I_NSCC_Na', 'I_PM', 'I_iCa', 'I_Na', 'JSERCA', 'I_iNa', 'epsilon_INH', 'JMCU', 'JNCX', 'JS1S2', 'fm', 'phi1', 'phi_1', 'JIPR', 'phi2']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 55
        p = self.params

        # direct mapping
        c[0] = p.Cm
        c[1] = p.gCa
        c[2] = p.T
        c[3] = p.R
        c[4] = p.F
        c[5] = p.CO
        c[6] = p.gNSCC_Ca_
        c[7] = p.hNSCC
        c[8] = p.ENSCC
        c[9] = p.KNSCC
        c[10] = p.gNSCC_Na_
        c[11] = p.gPM
        c[12] = p.KPM
        c[13] = p.gNa
        c[14] = p.KNa
        c[15] = p.hNa
        c[16] = p.VSERCA
        c[17] = p.A2
        c[18] = p.A4
        c[19] = p.A5
        c[20] = p.A6
        c[21] = p.VMCU
        c[22] = p.KMCU
        c[23] = p.KINH
        c[24] = p.hINH
        c[25] = p.VNCX
        c[26] = p.KNCX
        c[27] = p.mu_S1S2
        c[28] = p.kIPR
        c[29] = p.k_1
        c[30] = p.k1
        c[31] = p.k2
        c[32] = p.r2
        c[33] = p.r_2
        c[34] = p.r4
        c[35] = p.R1
        c[36] = p.R3
        c[37] = p.g_beta
        c[38] = p.h_beta
        c[39] = p.g_alpha
        c[40] = p.K_beta
        c[41] = p.P
        c[42] = p.delta_s
        c[43] = p.gamma_S1
        c[44] = p.gamma_MT
        c[45] = p.gamma_ER
        c[46] = p.gamma_S2
        c[47] = p.Km
        c[48] = p.Bm

        # derived constants
        c[49] = c[44]/c[43]
        c[50] = c[39]
        c[51] = c[45]/c[43]
        c[52] = c[44]/c[46]
        c[53] = c[45]/c[46]
        c[54] = c[43]/c[46]

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
