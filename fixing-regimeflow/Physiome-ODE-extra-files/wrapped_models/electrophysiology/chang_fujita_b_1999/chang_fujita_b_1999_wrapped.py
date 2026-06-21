# Size of variable arrays:
sizeAlgebraic = 30
sizeStates = 9
sizeConstants = 27
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (second)"
    legend_constants[0] = "C_m_Imp in component imported_variables (mmol_per_cm3)"
    legend_constants[1] = "C_c_Imp in component imported_variables (mmol_per_cm3)"
    legend_constants[2] = "psi_m in component imported_variables (millivolt)"
    legend_constants[3] = "psi_c in component imported_variables (millivolt)"
    legend_states[0] = "C_m_Na in component solute_concentrations (mmol_per_cm3)"
    legend_states[1] = "C_m_K in component solute_concentrations (mmol_per_cm3)"
    legend_states[2] = "C_m_Cl in component solute_concentrations (mmol_per_cm3)"
    legend_states[3] = "C_c_Na in component solute_concentrations (mmol_per_cm3)"
    legend_states[4] = "C_c_K in component solute_concentrations (mmol_per_cm3)"
    legend_states[5] = "C_c_Cl in component solute_concentrations (mmol_per_cm3)"
    legend_states[6] = "C_s_Na in component solute_concentrations (mmol_per_cm3)"
    legend_states[7] = "C_s_K in component solute_concentrations (mmol_per_cm3)"
    legend_states[8] = "C_s_Cl in component solute_concentrations (mmol_per_cm3)"
    legend_algebraic[4] = "J_mc_Na in component mc_sodium_flux (flux)"
    legend_algebraic[22] = "J_ms_Na in component ms_sodium_flux (flux)"
    legend_algebraic[16] = "J_sc_Na in component sc_sodium_flux (flux)"
    legend_algebraic[11] = "J_mc_K in component mc_potassium_flux (flux)"
    legend_algebraic[25] = "J_ms_K in component ms_potassium_flux (flux)"
    legend_algebraic[20] = "J_sc_K in component sc_potassium_flux (flux)"
    legend_algebraic[15] = "J_mc_Cl in component mc_chloride_flux (flux)"
    legend_algebraic[26] = "J_ms_Cl in component ms_chloride_flux (flux)"
    legend_algebraic[21] = "J_sc_Cl in component sc_chloride_flux (flux)"
    legend_constants[4] = "RT in component constants (J_per_mmol)"
    legend_constants[5] = "F in component constants (C_per_mmol)"
    legend_constants[6] = "C_s_Imp in component constants (mmol_per_cm3)"
    legend_constants[7] = "psi_s in component constants (millivolt)"
    legend_algebraic[2] = "J_mc_NaCl in component mc_sodium_flux (flux)"
    legend_algebraic[0] = "G_mc_Na in component mc_sodium_flux (flux)"
    legend_constants[8] = "P_mc_Na in component mc_sodium_flux (cm_per_s)"
    legend_constants[9] = "J_mc_NaCl_max in component mc_sodium_flux (flux)"
    legend_constants[10] = "K_mc_Na_NaCl in component mc_sodium_flux (mmol_per_cm3)"
    legend_constants[11] = "K_mc_Cl_NaCl in component mc_sodium_flux (mmol_per_cm3)"
    legend_algebraic[9] = "J_mc_KCl in component mc_potassium_flux (flux)"
    legend_algebraic[6] = "G_mc_K in component mc_potassium_flux (flux)"
    legend_constants[12] = "J_mc_KCl_max in component mc_potassium_flux (flux)"
    legend_constants[13] = "K_mc_K_KCl in component mc_potassium_flux (mmol_per_cm3)"
    legend_constants[14] = "K_mc_Cl_KCl in component mc_potassium_flux (mmol_per_cm3)"
    legend_constants[15] = "P_mc_K in component mc_potassium_flux (cm_per_s)"
    legend_algebraic[12] = "G_mc_Cl in component mc_chloride_flux (flux)"
    legend_constants[16] = "P_mc_Cl in component mc_chloride_flux (cm_per_s)"
    legend_algebraic[14] = "J_a in component sc_sodium_flux (flux)"
    legend_constants[17] = "J_a_max in component sc_sodium_flux (flux)"
    legend_constants[18] = "K_Na_ATPase in component sc_sodium_flux (mmol_per_cm3)"
    legend_algebraic[17] = "G_sc_K in component sc_potassium_flux (flux)"
    legend_constants[19] = "P_sc_K in component sc_potassium_flux (cm_per_s)"
    legend_algebraic[18] = "G_sc_Cl in component sc_chloride_flux (flux)"
    legend_constants[20] = "P_sc_Cl in component sc_chloride_flux (cm_per_s)"
    legend_algebraic[19] = "G_ms_Na in component ms_sodium_flux (flux)"
    legend_constants[21] = "P_ms_Na in component ms_sodium_flux (cm_per_s)"
    legend_algebraic[23] = "G_ms_K in component ms_potassium_flux (flux)"
    legend_constants[22] = "P_ms_K in component ms_potassium_flux (cm_per_s)"
    legend_algebraic[24] = "G_ms_Cl in component ms_chloride_flux (flux)"
    legend_constants[23] = "P_ms_Cl in component ms_chloride_flux (cm_per_s)"
    legend_algebraic[27] = "J_Na in component total_transepithelial_sodium_flux (flux)"
    legend_algebraic[28] = "J_K in component total_transepithelial_potassium_flux (flux)"
    legend_algebraic[29] = "J_Cl in component total_transepithelial_chloride_flux (flux)"
    legend_algebraic[1] = "Osm_m in component osmolarities (mmol_per_cm3)"
    legend_algebraic[3] = "Osm_c in component osmolarities (mmol_per_cm3)"
    legend_algebraic[5] = "Osm_s in component osmolarities (mmol_per_cm3)"
    legend_algebraic[7] = "J_mc_v in component mc_transepithelial_volume_flux (cm_per_s)"
    legend_constants[24] = "L_mc_v in component mc_transepithelial_volume_flux (cm_per_s_mmHg)"
    legend_algebraic[10] = "J_ms_v in component ms_transepithelial_volume_flux (cm_per_s)"
    legend_constants[25] = "L_ms_v in component ms_transepithelial_volume_flux (cm_per_s_mmHg)"
    legend_algebraic[8] = "J_sc_v in component sc_transepithelial_volume_flux (cm_per_s)"
    legend_constants[26] = "L_sc_v in component sc_transepithelial_volume_flux (cm_per_s_mmHg)"
    legend_algebraic[13] = "J_v in component total_transepithelial_volume_flux (cm_per_s)"
    legend_rates[0] = "d/dt C_m_Na in component solute_concentrations (mmol_per_cm3)"
    legend_rates[6] = "d/dt C_s_Na in component solute_concentrations (mmol_per_cm3)"
    legend_rates[3] = "d/dt C_c_Na in component solute_concentrations (mmol_per_cm3)"
    legend_rates[1] = "d/dt C_m_K in component solute_concentrations (mmol_per_cm3)"
    legend_rates[7] = "d/dt C_s_K in component solute_concentrations (mmol_per_cm3)"
    legend_rates[4] = "d/dt C_c_K in component solute_concentrations (mmol_per_cm3)"
    legend_rates[2] = "d/dt C_m_Cl in component solute_concentrations (mmol_per_cm3)"
    legend_rates[8] = "d/dt C_s_Cl in component solute_concentrations (mmol_per_cm3)"
    legend_rates[5] = "d/dt C_c_Cl in component solute_concentrations (mmol_per_cm3)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    constants[0] = 0.1033
    constants[1] = 0.1124
    constants[2] = -28.0
    constants[3] = -86.4
    states[0] = 0.05
    states[1] = 0.002
    states[2] = 0.03
    states[3] = 0.0164
    states[4] = 0.1637
    states[5] = 0.0203
    states[6] = 1.438E-1
    states[7] = 4.25E-3
    states[8] = 1.12E-1
    constants[4] = 2.579
    constants[5] = 96.48
    constants[6] = 4.525E-2
    constants[7] = 0.0
    constants[8] = 3.27E-6
    constants[9] = 3.21E-5
    constants[10] = 5.11E-2
    constants[11] = 1.92E-2
    constants[12] = 6.31E-8
    constants[13] = 5.30E-2
    constants[14] = 2.13E-2
    constants[15] = 4.90E-7
    constants[16] = 1.43E-6
    constants[17] = 2.69E-6
    constants[18] = 1.20E-2
    constants[19] = 4.74E-4
    constants[20] = 9.16E-5
    constants[21] = 4.80E-6
    constants[22] = 4.80E-6
    constants[23] = 2.40E-6
    constants[24] = 5.22E-9
    constants[25] = 0.0
    constants[26] = 5.22E-7
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[2] = constants[9]*(((states[0]/constants[10])*(states[2]/constants[11])-(states[3]/constants[10])*(states[5]/constants[11]))/((1.00000+(states[0]/constants[10])*(states[2]/constants[11]))*(1.00000+states[3]/constants[10])*(1.00000+states[5]/constants[11])+(1.00000+(states[3]/constants[10])*(states[5]/constants[11]))*(1.00000+states[0]/constants[10])*(1.00000+states[2]/constants[11])))
    algebraic[0] = constants[8]*((constants[5]*(constants[2]-constants[3]))/constants[4])*((states[0]-states[3]*exp(-(constants[5]/constants[4])*(constants[2]-constants[3])))/(1.00000-exp(-(constants[5]/constants[4])*(constants[2]-constants[3]))))
    algebraic[4] = algebraic[2]+algebraic[0]
    algebraic[14] = constants[17]*(1.00000/(1.00000+power(constants[18]/states[3], 3.00000)))
    algebraic[16] = -3.00000*algebraic[14]
    rates[3] = algebraic[4]+algebraic[16]
    algebraic[9] = constants[12]*(((states[1]/constants[13])*(states[2]/constants[14])-(states[4]/constants[13])*(states[5]/constants[14]))/((1.00000+(states[1]/constants[13])*(states[2]/constants[14]))*(1.00000+states[4]/constants[13])*(1.00000+states[5]/constants[14])+(1.00000+(states[4]/constants[13])*(states[5]/constants[14]))*(1.00000+states[1]/constants[13])*(1.00000+states[2]/constants[14])))
    algebraic[6] = constants[15]*((constants[5]*(constants[2]-constants[3]))/constants[4])*((states[1]-states[4]*exp(-(constants[5]/constants[4])*(constants[2]-constants[3])))/(1.00000-exp(-(constants[5]/constants[4])*(constants[2]-constants[3]))))
    algebraic[11] = algebraic[9]+algebraic[6]
    algebraic[17] = constants[19]*((constants[5]*(constants[7]-constants[3]))/constants[4])*((states[7]-states[4]*exp(-(constants[5]/constants[4])*(constants[7]-constants[3])))/(1.00000-exp(-(constants[5]/constants[4])*(constants[7]-constants[3]))))
    algebraic[20] = 2.00000*algebraic[14]+algebraic[17]
    rates[4] = algebraic[11]+algebraic[20]
    algebraic[12] = constants[16]*((-1.00000*constants[5]*(constants[2]-constants[3]))/constants[4])*((states[2]-states[5]*exp(-((-1.00000*constants[5])/constants[4])*(constants[2]-constants[3])))/(1.00000-exp(-((-1.00000*constants[5])/constants[4])*(constants[2]-constants[3]))))
    algebraic[15] = algebraic[2]+algebraic[9]+algebraic[12]
    algebraic[18] = constants[20]*((-1.00000*constants[5]*(constants[7]-constants[3]))/constants[4])*((states[8]-states[5]*exp(-((-1.00000*constants[5])/constants[4])*(constants[7]-constants[3])))/(1.00000-exp(-((-1.00000*constants[5])/constants[4])*(constants[7]-constants[3]))))
    algebraic[21] = algebraic[18]
    rates[5] = algebraic[15]+algebraic[21]
    algebraic[19] = constants[21]*((constants[5]*(constants[2]-constants[7]))/constants[4])*((states[0]-states[6]*exp(-(constants[5]/constants[4])*(constants[2]-constants[7])))/(1.00000-exp(-(constants[5]/constants[4])*(constants[2]-constants[7]))))
    algebraic[22] = algebraic[19]
    rates[0] = -(algebraic[4]+algebraic[22])
    rates[6] = algebraic[22]-algebraic[16]
    algebraic[23] = constants[22]*((constants[5]*(constants[2]-constants[7]))/constants[4])*((states[1]-states[7]*exp(-(constants[5]/constants[4])*(constants[2]-constants[7])))/(1.00000-exp(-(constants[5]/constants[4])*(constants[2]-constants[7]))))
    algebraic[25] = algebraic[23]
    rates[1] = -(algebraic[11]+algebraic[25])
    rates[7] = algebraic[25]-algebraic[20]
    algebraic[24] = constants[23]*((-1.00000*constants[5]*(constants[2]-constants[7]))/constants[4])*((states[2]-states[8]*exp(-((-1.00000*constants[5])/constants[4])*(constants[2]-constants[7])))/(1.00000-exp(-((-1.00000*constants[5])/constants[4])*(constants[2]-constants[7]))))
    algebraic[26] = algebraic[24]
    rates[2] = -(algebraic[15]+algebraic[26])
    rates[8] = algebraic[26]-algebraic[21]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[2] = constants[9]*(((states[0]/constants[10])*(states[2]/constants[11])-(states[3]/constants[10])*(states[5]/constants[11]))/((1.00000+(states[0]/constants[10])*(states[2]/constants[11]))*(1.00000+states[3]/constants[10])*(1.00000+states[5]/constants[11])+(1.00000+(states[3]/constants[10])*(states[5]/constants[11]))*(1.00000+states[0]/constants[10])*(1.00000+states[2]/constants[11])))
    algebraic[0] = constants[8]*((constants[5]*(constants[2]-constants[3]))/constants[4])*((states[0]-states[3]*exp(-(constants[5]/constants[4])*(constants[2]-constants[3])))/(1.00000-exp(-(constants[5]/constants[4])*(constants[2]-constants[3]))))
    algebraic[4] = algebraic[2]+algebraic[0]
    algebraic[14] = constants[17]*(1.00000/(1.00000+power(constants[18]/states[3], 3.00000)))
    algebraic[16] = -3.00000*algebraic[14]
    algebraic[9] = constants[12]*(((states[1]/constants[13])*(states[2]/constants[14])-(states[4]/constants[13])*(states[5]/constants[14]))/((1.00000+(states[1]/constants[13])*(states[2]/constants[14]))*(1.00000+states[4]/constants[13])*(1.00000+states[5]/constants[14])+(1.00000+(states[4]/constants[13])*(states[5]/constants[14]))*(1.00000+states[1]/constants[13])*(1.00000+states[2]/constants[14])))
    algebraic[6] = constants[15]*((constants[5]*(constants[2]-constants[3]))/constants[4])*((states[1]-states[4]*exp(-(constants[5]/constants[4])*(constants[2]-constants[3])))/(1.00000-exp(-(constants[5]/constants[4])*(constants[2]-constants[3]))))
    algebraic[11] = algebraic[9]+algebraic[6]
    algebraic[17] = constants[19]*((constants[5]*(constants[7]-constants[3]))/constants[4])*((states[7]-states[4]*exp(-(constants[5]/constants[4])*(constants[7]-constants[3])))/(1.00000-exp(-(constants[5]/constants[4])*(constants[7]-constants[3]))))
    algebraic[20] = 2.00000*algebraic[14]+algebraic[17]
    algebraic[12] = constants[16]*((-1.00000*constants[5]*(constants[2]-constants[3]))/constants[4])*((states[2]-states[5]*exp(-((-1.00000*constants[5])/constants[4])*(constants[2]-constants[3])))/(1.00000-exp(-((-1.00000*constants[5])/constants[4])*(constants[2]-constants[3]))))
    algebraic[15] = algebraic[2]+algebraic[9]+algebraic[12]
    algebraic[18] = constants[20]*((-1.00000*constants[5]*(constants[7]-constants[3]))/constants[4])*((states[8]-states[5]*exp(-((-1.00000*constants[5])/constants[4])*(constants[7]-constants[3])))/(1.00000-exp(-((-1.00000*constants[5])/constants[4])*(constants[7]-constants[3]))))
    algebraic[21] = algebraic[18]
    algebraic[19] = constants[21]*((constants[5]*(constants[2]-constants[7]))/constants[4])*((states[0]-states[6]*exp(-(constants[5]/constants[4])*(constants[2]-constants[7])))/(1.00000-exp(-(constants[5]/constants[4])*(constants[2]-constants[7]))))
    algebraic[22] = algebraic[19]
    algebraic[23] = constants[22]*((constants[5]*(constants[2]-constants[7]))/constants[4])*((states[1]-states[7]*exp(-(constants[5]/constants[4])*(constants[2]-constants[7])))/(1.00000-exp(-(constants[5]/constants[4])*(constants[2]-constants[7]))))
    algebraic[25] = algebraic[23]
    algebraic[24] = constants[23]*((-1.00000*constants[5]*(constants[2]-constants[7]))/constants[4])*((states[2]-states[8]*exp(-((-1.00000*constants[5])/constants[4])*(constants[2]-constants[7])))/(1.00000-exp(-((-1.00000*constants[5])/constants[4])*(constants[2]-constants[7]))))
    algebraic[26] = algebraic[24]
    algebraic[1] = states[0]+states[1]+states[2]+constants[0]
    algebraic[3] = states[3]+states[4]+states[5]+constants[1]
    algebraic[5] = states[6]+states[7]+states[8]+constants[6]
    algebraic[7] = constants[24]*constants[4]*(algebraic[1]-algebraic[3])
    algebraic[8] = constants[26]*constants[4]*(algebraic[5]-algebraic[3])
    algebraic[10] = constants[25]*constants[4]*(algebraic[1]-algebraic[5])
    algebraic[13] = algebraic[7]+algebraic[10]
    algebraic[27] = algebraic[4]+algebraic[22]
    algebraic[28] = algebraic[11]+algebraic[25]
    algebraic[29] = algebraic[15]+algebraic[26]
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
        self.C_m_Imp = 0.1033
        self.C_c_Imp = 0.1124
        self.psi_m = -28.0
        self.psi_c = -86.4
        self.RT = 2.579
        self.F = 96.48
        self.C_s_Imp = 4.525E-2
        self.psi_s = 0.0
        self.P_mc_Na = 3.27E-6
        self.J_mc_NaCl_max = 3.21E-5
        self.K_mc_Na_NaCl = 5.11E-2
        self.K_mc_Cl_NaCl = 1.92E-2
        self.J_mc_KCl_max = 6.31E-8
        self.K_mc_K_KCl = 5.30E-2
        self.K_mc_Cl_KCl = 2.13E-2
        self.P_mc_K = 4.90E-7
        self.P_mc_Cl = 1.43E-6
        self.J_a_max = 2.69E-6
        self.K_Na_ATPase = 1.20E-2
        self.P_sc_K = 4.74E-4
        self.P_sc_Cl = 9.16E-5
        self.P_ms_Na = 4.80E-6
        self.P_ms_K = 4.80E-6
        self.P_ms_Cl = 2.40E-6
        self.L_mc_v = 5.22E-9
        self.L_ms_v = 0.0
        self.L_sc_v = 5.22E-7

    def to_dict(self):
        return {
            "C_m_Imp": self.C_m_Imp,
            "C_c_Imp": self.C_c_Imp,
            "psi_m": self.psi_m,
            "psi_c": self.psi_c,
            "RT": self.RT,
            "F": self.F,
            "C_s_Imp": self.C_s_Imp,
            "psi_s": self.psi_s,
            "P_mc_Na": self.P_mc_Na,
            "J_mc_NaCl_max": self.J_mc_NaCl_max,
            "K_mc_Na_NaCl": self.K_mc_Na_NaCl,
            "K_mc_Cl_NaCl": self.K_mc_Cl_NaCl,
            "J_mc_KCl_max": self.J_mc_KCl_max,
            "K_mc_K_KCl": self.K_mc_K_KCl,
            "K_mc_Cl_KCl": self.K_mc_Cl_KCl,
            "P_mc_K": self.P_mc_K,
            "P_mc_Cl": self.P_mc_Cl,
            "J_a_max": self.J_a_max,
            "K_Na_ATPase": self.K_Na_ATPase,
            "P_sc_K": self.P_sc_K,
            "P_sc_Cl": self.P_sc_Cl,
            "P_ms_Na": self.P_ms_Na,
            "P_ms_K": self.P_ms_K,
            "P_ms_Cl": self.P_ms_Cl,
            "L_mc_v": self.L_mc_v,
            "L_ms_v": self.L_ms_v,
            "L_sc_v": self.L_sc_v,
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
        y0=[0.05, 0.002, 0.03, 0.0164, 0.1637, 0.0203, 1.438E-1, 4.25E-3, 1.12E-1],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "chang_fujita_b_1999"
        self.curve_names = [
            "C_m_Na",
            "C_m_K",
            "C_m_Cl",
            "C_c_Na",
            "C_c_K",
            "C_c_Cl",
            "C_s_Na",
            "C_s_K",
            "C_s_Cl",
        ]
        self.state_names = ['C_m_Na', 'C_m_K', 'C_m_Cl', 'C_c_Na', 'C_c_K', 'C_c_Cl', 'C_s_Na', 'C_s_K', 'C_s_Cl']
        self.algebraic_names = ['G_mc_Na', 'Osm_m', 'J_mc_NaCl', 'Osm_c', 'J_mc_Na', 'Osm_s', 'G_mc_K', 'J_mc_v', 'J_sc_v', 'J_mc_KCl', 'J_ms_v', 'J_mc_K', 'G_mc_Cl', 'J_v', 'J_a', 'J_mc_Cl', 'J_sc_Na', 'G_sc_K', 'G_sc_Cl', 'G_ms_Na', 'J_sc_K', 'J_sc_Cl', 'J_ms_Na', 'G_ms_K', 'G_ms_Cl', 'J_ms_K', 'J_ms_Cl', 'J_Na', 'J_K', 'J_Cl']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 27
        p = self.params

        # direct mapping
        c[0] = p.C_m_Imp
        c[1] = p.C_c_Imp
        c[2] = p.psi_m
        c[3] = p.psi_c
        c[4] = p.RT
        c[5] = p.F
        c[6] = p.C_s_Imp
        c[7] = p.psi_s
        c[8] = p.P_mc_Na
        c[9] = p.J_mc_NaCl_max
        c[10] = p.K_mc_Na_NaCl
        c[11] = p.K_mc_Cl_NaCl
        c[12] = p.J_mc_KCl_max
        c[13] = p.K_mc_K_KCl
        c[14] = p.K_mc_Cl_KCl
        c[15] = p.P_mc_K
        c[16] = p.P_mc_Cl
        c[17] = p.J_a_max
        c[18] = p.K_Na_ATPase
        c[19] = p.P_sc_K
        c[20] = p.P_sc_Cl
        c[21] = p.P_ms_Na
        c[22] = p.P_ms_K
        c[23] = p.P_ms_Cl
        c[24] = p.L_mc_v
        c[25] = p.L_ms_v
        c[26] = p.L_sc_v

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
