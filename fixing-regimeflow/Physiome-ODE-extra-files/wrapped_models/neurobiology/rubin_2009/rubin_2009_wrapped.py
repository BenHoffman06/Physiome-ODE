# Size of variable arrays:
sizeAlgebraic = 25
sizeStates = 8
sizeConstants = 49
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (millisecond)"
    legend_states[0] = "V1 in component V1 (millivolt)"
    legend_constants[0] = "C in component model_parameters (nanoF)"
    legend_algebraic[3] = "i_NaP in component i_NaP (nanoA)"
    legend_algebraic[5] = "i_K in component i_K (nanoA)"
    legend_algebraic[9] = "i_L1 in component i_L1 (nanoA)"
    legend_algebraic[13] = "i_synE1 in component i_synE1 (nanoA)"
    legend_algebraic[22] = "i_synI1 in component i_synI1 (nanoA)"
    legend_states[1] = "V2 in component V2 (millivolt)"
    legend_algebraic[6] = "i_AD2 in component i_AD2 (nanoA)"
    legend_algebraic[10] = "i_L2 in component i_L2 (nanoA)"
    legend_algebraic[17] = "i_synE2 in component i_synE2 (nanoA)"
    legend_algebraic[23] = "i_synI2 in component i_synI2 (nanoA)"
    legend_states[2] = "V3 in component V3 (millivolt)"
    legend_algebraic[7] = "i_AD3 in component i_AD3 (nanoA)"
    legend_algebraic[11] = "i_L3 in component i_L3 (nanoA)"
    legend_algebraic[14] = "i_synE3 in component i_synE3 (nanoA)"
    legend_algebraic[24] = "i_synI3 in component i_synI3 (nanoA)"
    legend_states[3] = "V4 in component V4 (millivolt)"
    legend_algebraic[8] = "i_AD4 in component i_AD4 (nanoA)"
    legend_algebraic[12] = "i_L4 in component i_L4 (nanoA)"
    legend_algebraic[15] = "i_synE4 in component i_synE4 (nanoA)"
    legend_algebraic[20] = "i_synI4 in component i_synI4 (nanoA)"
    legend_constants[1] = "g_NaP in component model_parameters (nanoS)"
    legend_constants[2] = "E_Na in component model_parameters (millivolt)"
    legend_algebraic[1] = "m in component i_NaP_m_gate (dimensionless)"
    legend_states[4] = "h in component i_NaP_h_gate (dimensionless)"
    legend_algebraic[0] = "h_infinity in component i_NaP_h_gate (dimensionless)"
    legend_algebraic[2] = "tau_h in component i_NaP_h_gate (millisecond)"
    legend_constants[3] = "tau_h_max in component i_NaP_h_gate (millisecond)"
    legend_constants[4] = "g_K in component model_parameters (nanoS)"
    legend_constants[5] = "E_K in component model_parameters (millivolt)"
    legend_algebraic[4] = "m in component i_K_m_gate (dimensionless)"
    legend_constants[6] = "g_AD in component model_parameters (nanoS)"
    legend_algebraic[18] = "f2_V2 in component model_parameters (dimensionless)"
    legend_states[5] = "m in component i_AD2_m_gate (dimensionless)"
    legend_constants[7] = "k_AD2 in component i_AD2_m_gate (dimensionless)"
    legend_constants[8] = "tau_AD2 in component i_AD2_m_gate (millisecond)"
    legend_algebraic[19] = "f3_V3 in component model_parameters (dimensionless)"
    legend_states[6] = "m in component i_AD3_m_gate (dimensionless)"
    legend_constants[9] = "k_AD3 in component i_AD3_m_gate (dimensionless)"
    legend_constants[10] = "tau_AD3 in component i_AD3_m_gate (millisecond)"
    legend_algebraic[21] = "f4_V4 in component model_parameters (dimensionless)"
    legend_states[7] = "m in component i_AD4_m_gate (dimensionless)"
    legend_constants[11] = "k_AD4 in component i_AD4_m_gate (dimensionless)"
    legend_constants[12] = "tau_AD4 in component i_AD4_m_gate (millisecond)"
    legend_constants[13] = "g_L in component model_parameters (nanoS)"
    legend_constants[14] = "E_L in component model_parameters (millivolt)"
    legend_constants[15] = "c11 in component i_synE1 (dimensionless)"
    legend_constants[16] = "c21 in component i_synE1 (dimensionless)"
    legend_constants[17] = "c31 in component i_synE1 (dimensionless)"
    legend_constants[18] = "d1 in component model_parameters (dimensionless)"
    legend_constants[19] = "d2 in component model_parameters (dimensionless)"
    legend_constants[20] = "d3 in component model_parameters (dimensionless)"
    legend_constants[21] = "g_synE in component model_parameters (nanoS)"
    legend_constants[22] = "E_synE in component model_parameters (millivolt)"
    legend_constants[23] = "c12 in component i_synE2 (dimensionless)"
    legend_constants[24] = "c22 in component i_synE2 (dimensionless)"
    legend_constants[25] = "c32 in component i_synE2 (dimensionless)"
    legend_constants[26] = "a12 in component i_synE2 (dimensionless)"
    legend_algebraic[16] = "f1_V1 in component model_parameters (dimensionless)"
    legend_constants[27] = "c13 in component i_synE3 (dimensionless)"
    legend_constants[28] = "c23 in component i_synE3 (dimensionless)"
    legend_constants[29] = "c33 in component i_synE3 (dimensionless)"
    legend_constants[30] = "c14 in component i_synE4 (dimensionless)"
    legend_constants[31] = "c24 in component i_synE4 (dimensionless)"
    legend_constants[32] = "c34 in component i_synE4 (dimensionless)"
    legend_constants[33] = "b21 in component i_synI1 (dimensionless)"
    legend_constants[34] = "b31 in component i_synI1 (dimensionless)"
    legend_constants[35] = "b41 in component i_synI1 (dimensionless)"
    legend_constants[36] = "g_synI in component model_parameters (nanoS)"
    legend_constants[37] = "E_synI in component model_parameters (millivolt)"
    legend_constants[38] = "b32 in component i_synI2 (dimensionless)"
    legend_constants[39] = "b42 in component i_synI2 (dimensionless)"
    legend_constants[40] = "b23 in component i_synI3 (dimensionless)"
    legend_constants[41] = "b43 in component i_synI3 (dimensionless)"
    legend_constants[42] = "b24 in component i_synI4 (dimensionless)"
    legend_constants[43] = "b34 in component i_synI4 (dimensionless)"
    legend_constants[44] = "V_half in component model_parameters (millivolt)"
    legend_constants[45] = "k_V1 in component model_parameters (millivolt)"
    legend_constants[46] = "k_V2 in component model_parameters (millivolt)"
    legend_constants[47] = "k_V3 in component model_parameters (millivolt)"
    legend_constants[48] = "k_V4 in component model_parameters (millivolt)"
    legend_rates[0] = "d/dt V1 in component V1 (millivolt)"
    legend_rates[1] = "d/dt V2 in component V2 (millivolt)"
    legend_rates[2] = "d/dt V3 in component V3 (millivolt)"
    legend_rates[3] = "d/dt V4 in component V4 (millivolt)"
    legend_rates[4] = "d/dt h in component i_NaP_h_gate (dimensionless)"
    legend_rates[5] = "d/dt m in component i_AD2_m_gate (dimensionless)"
    legend_rates[6] = "d/dt m in component i_AD3_m_gate (dimensionless)"
    legend_rates[7] = "d/dt m in component i_AD4_m_gate (dimensionless)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = -50.0
    constants[0] = 0.020
    states[1] = -50.0
    states[2] = -50.0
    states[3] = -50.0
    constants[1] = 5.0
    constants[2] = 50.0
    states[4] = 0.92
    constants[3] = 6000
    constants[4] = 5.0
    constants[5] = -85.0
    constants[6] = 10.0
    states[5] = 0.92
    constants[7] = 0.9
    constants[8] = 2000
    states[6] = 0.92
    constants[9] = 1.3
    constants[10] = 2000
    states[7] = 0.92
    constants[11] = 0.9
    constants[12] = 1000
    constants[13] = 2.8
    constants[14] = -60.0
    constants[15] = 0.115
    constants[16] = 0.07
    constants[17] = 0.025
    constants[18] = 1.0
    constants[19] = 1.0
    constants[20] = 1.0
    constants[21] = 10.0
    constants[22] = 0.0
    constants[23] = 0.3
    constants[24] = 0.3
    constants[25] = 0.0
    constants[26] = 0.4
    constants[27] = 0.63
    constants[28] = 0.00
    constants[29] = 0.00
    constants[30] = 0.33
    constants[31] = 0.40
    constants[32] = 0.00
    constants[33] = 0.00
    constants[34] = 0.30
    constants[35] = 0.20
    constants[36] = 60.0
    constants[37] = -75.0
    constants[38] = 0.05
    constants[39] = 0.35
    constants[40] = 0.25
    constants[41] = 0.10
    constants[42] = 0.35
    constants[43] = 0.35
    constants[44] = 30.0
    constants[45] = 8.0
    constants[46] = 4.0
    constants[47] = 4.0
    constants[48] = 4.0
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[0] = 1.00000/(1.00000+exp((states[0]+48.0000)/6.00000))
    algebraic[2] = constants[3]/cosh((states[0]+48.0000)/12.0000)
    rates[4] = (algebraic[0]-states[4])/algebraic[2]
    algebraic[18] = 1.00000/(1.00000+exp(-(states[1]-constants[44])/constants[46]))
    rates[5] = (constants[7]*algebraic[18]-states[5])/constants[8]
    algebraic[19] = 1.00000/(1.00000+exp(-(states[2]-constants[44])/constants[47]))
    rates[6] = (constants[9]*algebraic[19]-states[6])/constants[10]
    algebraic[8] = constants[6]*states[7]*(1.00000/1000.00)*(states[3]-constants[5])
    algebraic[12] = constants[13]*(1.00000/1000.00)*(states[3]-constants[14])
    algebraic[15] = constants[21]*(1.00000/1000.00)*(states[3]-constants[22])*(constants[30]*constants[18]+constants[31]*constants[19]+constants[32]*constants[20])
    algebraic[20] = constants[36]*(1.00000/1000.00)*(states[3]-constants[37])*(constants[42]*algebraic[18]+constants[43]*algebraic[19])
    rates[3] = -(algebraic[8]+algebraic[12]+algebraic[15]+algebraic[20])/constants[0]
    algebraic[21] = 1.00000/(1.00000+exp(-(states[3]-constants[44])/constants[48]))
    rates[7] = (constants[11]*algebraic[21]-states[7])/constants[12]
    algebraic[1] = 1.00000/(1.00000+exp(-(states[0]+40.0000)/6.00000))
    algebraic[3] = constants[1]*algebraic[1]*states[4]*(1.00000/1000.00)*(states[0]-constants[2])
    algebraic[4] = 1.00000/(1.00000+exp(-(states[0]+29.0000)/4.00000))
    algebraic[5] = constants[4]*(power(algebraic[4], 4.00000))*(1.00000/1000.00)*(states[0]-constants[5])
    algebraic[9] = constants[13]*(1.00000/1000.00)*(states[0]-constants[14])
    algebraic[13] = constants[21]*(1.00000/1000.00)*(states[0]-constants[22])*(constants[15]*constants[18]+constants[16]*constants[19]+constants[17]*constants[20])
    algebraic[22] = constants[36]*(1.00000/1000.00)*(states[0]-constants[37])*(constants[33]*algebraic[18]+constants[34]*algebraic[19]+constants[35]*algebraic[21])
    rates[0] = -(algebraic[3]+algebraic[5]+algebraic[9]+algebraic[13]+algebraic[22])/constants[0]
    algebraic[6] = constants[6]*states[5]*(1.00000/1000.00)*(states[1]-constants[5])
    algebraic[10] = constants[13]*(1.00000/1000.00)*(states[1]-constants[14])
    algebraic[16] = 1.00000/(1.00000+exp(-(states[0]-constants[44])/constants[45]))
    algebraic[17] = constants[21]*(1.00000/1000.00)*(states[1]-constants[22])*(constants[26]*algebraic[16]+constants[23]*constants[18]+constants[24]*constants[19]+constants[25]*constants[20])
    algebraic[23] = constants[36]*(1.00000/1000.00)*(states[1]-constants[37])*(constants[38]*algebraic[19]+constants[39]*algebraic[21])
    rates[1] = -(algebraic[6]+algebraic[10]+algebraic[17]+algebraic[23])/constants[0]
    algebraic[7] = constants[6]*states[6]*(1.00000/1000.00)*(states[2]-constants[5])
    algebraic[11] = constants[13]*(1.00000/1000.00)*(states[2]-constants[14])
    algebraic[14] = constants[21]*(1.00000/1000.00)*(states[2]-constants[22])*(constants[27]*constants[18]+constants[28]*constants[19]+constants[29]*constants[20])
    algebraic[24] = constants[36]*(1.00000/1000.00)*(states[2]-constants[37])*(constants[40]*algebraic[18]+constants[41]*algebraic[21])
    rates[2] = -(algebraic[7]+algebraic[11]+algebraic[14]+algebraic[24])/constants[0]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = 1.00000/(1.00000+exp((states[0]+48.0000)/6.00000))
    algebraic[2] = constants[3]/cosh((states[0]+48.0000)/12.0000)
    algebraic[18] = 1.00000/(1.00000+exp(-(states[1]-constants[44])/constants[46]))
    algebraic[19] = 1.00000/(1.00000+exp(-(states[2]-constants[44])/constants[47]))
    algebraic[8] = constants[6]*states[7]*(1.00000/1000.00)*(states[3]-constants[5])
    algebraic[12] = constants[13]*(1.00000/1000.00)*(states[3]-constants[14])
    algebraic[15] = constants[21]*(1.00000/1000.00)*(states[3]-constants[22])*(constants[30]*constants[18]+constants[31]*constants[19]+constants[32]*constants[20])
    algebraic[20] = constants[36]*(1.00000/1000.00)*(states[3]-constants[37])*(constants[42]*algebraic[18]+constants[43]*algebraic[19])
    algebraic[21] = 1.00000/(1.00000+exp(-(states[3]-constants[44])/constants[48]))
    algebraic[1] = 1.00000/(1.00000+exp(-(states[0]+40.0000)/6.00000))
    algebraic[3] = constants[1]*algebraic[1]*states[4]*(1.00000/1000.00)*(states[0]-constants[2])
    algebraic[4] = 1.00000/(1.00000+exp(-(states[0]+29.0000)/4.00000))
    algebraic[5] = constants[4]*(power(algebraic[4], 4.00000))*(1.00000/1000.00)*(states[0]-constants[5])
    algebraic[9] = constants[13]*(1.00000/1000.00)*(states[0]-constants[14])
    algebraic[13] = constants[21]*(1.00000/1000.00)*(states[0]-constants[22])*(constants[15]*constants[18]+constants[16]*constants[19]+constants[17]*constants[20])
    algebraic[22] = constants[36]*(1.00000/1000.00)*(states[0]-constants[37])*(constants[33]*algebraic[18]+constants[34]*algebraic[19]+constants[35]*algebraic[21])
    algebraic[6] = constants[6]*states[5]*(1.00000/1000.00)*(states[1]-constants[5])
    algebraic[10] = constants[13]*(1.00000/1000.00)*(states[1]-constants[14])
    algebraic[16] = 1.00000/(1.00000+exp(-(states[0]-constants[44])/constants[45]))
    algebraic[17] = constants[21]*(1.00000/1000.00)*(states[1]-constants[22])*(constants[26]*algebraic[16]+constants[23]*constants[18]+constants[24]*constants[19]+constants[25]*constants[20])
    algebraic[23] = constants[36]*(1.00000/1000.00)*(states[1]-constants[37])*(constants[38]*algebraic[19]+constants[39]*algebraic[21])
    algebraic[7] = constants[6]*states[6]*(1.00000/1000.00)*(states[2]-constants[5])
    algebraic[11] = constants[13]*(1.00000/1000.00)*(states[2]-constants[14])
    algebraic[14] = constants[21]*(1.00000/1000.00)*(states[2]-constants[22])*(constants[27]*constants[18]+constants[28]*constants[19]+constants[29]*constants[20])
    algebraic[24] = constants[36]*(1.00000/1000.00)*(states[2]-constants[37])*(constants[40]*algebraic[18]+constants[41]*algebraic[21])
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
        self.C = 0.020
        self.g_NaP = 5.0
        self.E_Na = 50.0
        self.tau_h_max = 6000
        self.g_K = 5.0
        self.E_K = -85.0
        self.g_AD = 10.0
        self.k_AD2 = 0.9
        self.tau_AD2 = 2000
        self.k_AD3 = 1.3
        self.tau_AD3 = 2000
        self.k_AD4 = 0.9
        self.tau_AD4 = 1000
        self.g_L = 2.8
        self.E_L = -60.0
        self.c11 = 0.115
        self.c21 = 0.07
        self.c31 = 0.025
        self.d1 = 1.0
        self.d2 = 1.0
        self.d3 = 1.0
        self.g_synE = 10.0
        self.E_synE = 0.0
        self.c12 = 0.3
        self.c22 = 0.3
        self.c32 = 0.0
        self.a12 = 0.4
        self.c13 = 0.63
        self.c23 = 0.00
        self.c33 = 0.00
        self.c14 = 0.33
        self.c24 = 0.40
        self.c34 = 0.00
        self.b21 = 0.00
        self.b31 = 0.30
        self.b41 = 0.20
        self.g_synI = 60.0
        self.E_synI = -75.0
        self.b32 = 0.05
        self.b42 = 0.35
        self.b23 = 0.25
        self.b43 = 0.10
        self.b24 = 0.35
        self.b34 = 0.35
        self.V_half = 30.0
        self.k_V1 = 8.0
        self.k_V2 = 4.0
        self.k_V3 = 4.0
        self.k_V4 = 4.0

    def to_dict(self):
        return {
            "C": self.C,
            "g_NaP": self.g_NaP,
            "E_Na": self.E_Na,
            "tau_h_max": self.tau_h_max,
            "g_K": self.g_K,
            "E_K": self.E_K,
            "g_AD": self.g_AD,
            "k_AD2": self.k_AD2,
            "tau_AD2": self.tau_AD2,
            "k_AD3": self.k_AD3,
            "tau_AD3": self.tau_AD3,
            "k_AD4": self.k_AD4,
            "tau_AD4": self.tau_AD4,
            "g_L": self.g_L,
            "E_L": self.E_L,
            "c11": self.c11,
            "c21": self.c21,
            "c31": self.c31,
            "d1": self.d1,
            "d2": self.d2,
            "d3": self.d3,
            "g_synE": self.g_synE,
            "E_synE": self.E_synE,
            "c12": self.c12,
            "c22": self.c22,
            "c32": self.c32,
            "a12": self.a12,
            "c13": self.c13,
            "c23": self.c23,
            "c33": self.c33,
            "c14": self.c14,
            "c24": self.c24,
            "c34": self.c34,
            "b21": self.b21,
            "b31": self.b31,
            "b41": self.b41,
            "g_synI": self.g_synI,
            "E_synI": self.E_synI,
            "b32": self.b32,
            "b42": self.b42,
            "b23": self.b23,
            "b43": self.b43,
            "b24": self.b24,
            "b34": self.b34,
            "V_half": self.V_half,
            "k_V1": self.k_V1,
            "k_V2": self.k_V2,
            "k_V3": self.k_V3,
            "k_V4": self.k_V4,
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
        y0=[-50.0, -50.0, -50.0, -50.0, 0.92, 0.92, 0.92, 0.92],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "rubin_2009"
        self.curve_names = [
            "V1",
            "V2",
            "V3",
            "V4",
            "h",
            "m",
            "m_1",
            "m_2",
        ]
        self.state_names = ['V1', 'V2', 'V3', 'V4', 'h', 'm', 'm_1', 'm_2']
        self.algebraic_names = ['h_infinity', 'm', 'tau_h', 'i_NaP', 'm_1', 'i_K', 'i_AD2', 'i_AD3', 'i_AD4', 'i_L1', 'i_L2', 'i_L3', 'i_L4', 'i_synE1', 'i_synE3', 'i_synE4', 'f1_V1', 'i_synE2', 'f2_V2', 'f3_V3', 'i_synI4', 'f4_V4', 'i_synI1', 'i_synI2', 'i_synI3']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 49
        p = self.params

        # direct mapping
        c[0] = p.C
        c[1] = p.g_NaP
        c[2] = p.E_Na
        c[3] = p.tau_h_max
        c[4] = p.g_K
        c[5] = p.E_K
        c[6] = p.g_AD
        c[7] = p.k_AD2
        c[8] = p.tau_AD2
        c[9] = p.k_AD3
        c[10] = p.tau_AD3
        c[11] = p.k_AD4
        c[12] = p.tau_AD4
        c[13] = p.g_L
        c[14] = p.E_L
        c[15] = p.c11
        c[16] = p.c21
        c[17] = p.c31
        c[18] = p.d1
        c[19] = p.d2
        c[20] = p.d3
        c[21] = p.g_synE
        c[22] = p.E_synE
        c[23] = p.c12
        c[24] = p.c22
        c[25] = p.c32
        c[26] = p.a12
        c[27] = p.c13
        c[28] = p.c23
        c[29] = p.c33
        c[30] = p.c14
        c[31] = p.c24
        c[32] = p.c34
        c[33] = p.b21
        c[34] = p.b31
        c[35] = p.b41
        c[36] = p.g_synI
        c[37] = p.E_synI
        c[38] = p.b32
        c[39] = p.b42
        c[40] = p.b23
        c[41] = p.b43
        c[42] = p.b24
        c[43] = p.b34
        c[44] = p.V_half
        c[45] = p.k_V1
        c[46] = p.k_V2
        c[47] = p.k_V3
        c[48] = p.k_V4

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
