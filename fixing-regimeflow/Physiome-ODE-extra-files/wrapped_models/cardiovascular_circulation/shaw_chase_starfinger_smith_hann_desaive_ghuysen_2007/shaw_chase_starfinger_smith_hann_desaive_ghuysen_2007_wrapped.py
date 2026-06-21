# Size of variable arrays:
sizeAlgebraic = 21
sizeStates = 6
sizeConstants = 40
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (second)"
    legend_constants[0] = "R_mt in component heart_parameters (kPa_second_per_liter)"
    legend_constants[1] = "R_av in component heart_parameters (kPa_second_per_liter)"
    legend_constants[2] = "R_tc in component heart_parameters (kPa_second_per_liter)"
    legend_constants[3] = "R_pv in component heart_parameters (kPa_second_per_liter)"
    legend_constants[4] = "R_pul in component heart_parameters (kPa_second_per_liter)"
    legend_constants[5] = "R_sys in component heart_parameters (kPa_second_per_liter)"
    legend_constants[6] = "HR in component heart_parameters (dimensionless)"
    legend_constants[7] = "V_tot in component heart_parameters (liter)"
    legend_constants[8] = "P_pl in component heart_parameters (kPa)"
    legend_algebraic[1] = "e_t in component driver_function (dimensionless)"
    legend_constants[9] = "A in component driver_function (dimensionless)"
    legend_constants[10] = "B in component driver_function (dimensionless)"
    legend_constants[11] = "C in component driver_function (dimensionless)"
    legend_algebraic[0] = "tau in component driver_function (second)"
    legend_constants[12] = "period in component driver_function (dimensionless)"
    legend_algebraic[2] = "V_pcd in component pericardium (liter)"
    legend_algebraic[3] = "P_pcd in component pericardium (kPa)"
    legend_algebraic[4] = "P_peri in component pericardium (kPa)"
    legend_states[0] = "V_lv in component left_ventricle (liter)"
    legend_states[1] = "V_rv in component right_ventricle (liter)"
    legend_constants[13] = "P_0_pcd in component pericardium (kPa)"
    legend_constants[14] = "V_0_pcd in component pericardium (liter)"
    legend_constants[15] = "lambda_pcd in component pericardium (per_liter)"
    legend_algebraic[9] = "V_lvf in component left_ventricle (liter)"
    legend_algebraic[10] = "P_lvf in component left_ventricle (kPa)"
    legend_algebraic[18] = "P_lv in component left_ventricle (kPa)"
    legend_algebraic[11] = "V_spt in component septum (liter)"
    legend_algebraic[12] = "P_es_lvf in component lvf_calculator (kPa)"
    legend_algebraic[13] = "P_ed_lvf in component lvf_calculator (kPa)"
    legend_algebraic[6] = "P_pu in component pulmonary_vein (kPa)"
    legend_algebraic[7] = "P_ao in component aorta (kPa)"
    legend_constants[16] = "E_es_lvf in component lvf_calculator (kPa_per_liter)"
    legend_constants[17] = "V_d_lvf in component lvf_calculator (liter)"
    legend_constants[18] = "P_0_lvf in component lvf_calculator (kPa)"
    legend_constants[19] = "lambda_lvf in component lvf_calculator (per_liter)"
    legend_constants[20] = "V_0_lvf in component lvf_calculator (liter)"
    legend_algebraic[14] = "V_rvf in component right_ventricle (liter)"
    legend_algebraic[15] = "P_rvf in component right_ventricle (kPa)"
    legend_algebraic[19] = "P_rv in component right_ventricle (kPa)"
    legend_algebraic[16] = "P_es_rvf in component rvf_calculator (kPa)"
    legend_algebraic[17] = "P_ed_rvf in component rvf_calculator (kPa)"
    legend_algebraic[5] = "P_pa in component pulmonary_artery (kPa)"
    legend_algebraic[8] = "P_vc in component vena_cava (kPa)"
    legend_constants[21] = "E_es_rvf in component rvf_calculator (kPa_per_liter)"
    legend_constants[22] = "V_d_rvf in component rvf_calculator (liter)"
    legend_constants[23] = "P_0_rvf in component rvf_calculator (kPa)"
    legend_constants[24] = "lambda_rvf in component rvf_calculator (per_liter)"
    legend_constants[25] = "V_0_rvf in component rvf_calculator (liter)"
    legend_algebraic[20] = "P_sept in component septum (kPa)"
    legend_constants[26] = "E_es_spt in component septum (kPa_per_liter)"
    legend_constants[27] = "V_d_spt in component septum (liter)"
    legend_constants[28] = "P_0_spt in component septum (kPa)"
    legend_constants[29] = "lambda_spt in component septum (per_liter)"
    legend_constants[30] = "V_0_spt in component septum (liter)"
    legend_constants[31] = "one in component septum (dimensionless)"
    legend_constants[32] = "E_es_pa in component pulmonary_artery (kPa_per_liter)"
    legend_states[2] = "V_pa in component pulmonary_artery (liter)"
    legend_constants[33] = "V_d_pa in component pulmonary_artery (liter)"
    legend_constants[34] = "E_es_pu in component pulmonary_vein (kPa_per_liter)"
    legend_states[3] = "V_pu in component pulmonary_vein (liter)"
    legend_constants[35] = "V_d_pu in component pulmonary_vein (liter)"
    legend_constants[36] = "E_es_ao in component aorta (kPa_per_liter)"
    legend_states[4] = "V_ao in component aorta (liter)"
    legend_constants[37] = "V_d_ao in component aorta (liter)"
    legend_constants[38] = "E_es_vc in component vena_cava (kPa_per_liter)"
    legend_states[5] = "V_vc in component vena_cava (liter)"
    legend_constants[39] = "V_d_vc in component vena_cava (liter)"
    legend_rates[0] = "d/dt V_lv in component left_ventricle (liter)"
    legend_rates[1] = "d/dt V_rv in component right_ventricle (liter)"
    legend_rates[2] = "d/dt V_pa in component pulmonary_artery (liter)"
    legend_rates[3] = "d/dt V_pu in component pulmonary_vein (liter)"
    legend_rates[4] = "d/dt V_ao in component aorta (liter)"
    legend_rates[5] = "d/dt V_vc in component vena_cava (liter)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    constants[0] = 0.06
    constants[1] = 1.4
    constants[2] = 0.18
    constants[3] = 0.48
    constants[4] = 19
    constants[5] = 140
    constants[6] = 80
    constants[7] = 5.5
    constants[8] = -0.533289474
    constants[9] = 1
    constants[10] = 80
    constants[11] = 0.27
    constants[12] = 0.405
    states[0] = 0.005
    states[1] = 0.005
    constants[13] = 0.067
    constants[14] = 0.2
    constants[15] = 30
    constants[16] = 454
    constants[17] = 0.005
    constants[18] = 0.17
    constants[19] = 15
    constants[20] = 0.005
    constants[21] = 87
    constants[22] = 0.005
    constants[23] = 0.16
    constants[24] = 15
    constants[25] = 0.005
    constants[26] = 6500
    constants[27] = 0.002
    constants[28] = 0.148
    constants[29] = 435
    constants[30] = 0.002
    constants[31] = 1
    constants[32] = 45
    states[2] = 0.16
    constants[33] = 0.16
    constants[34] = 0.8
    states[3] = 0.2
    constants[35] = 0.2
    constants[36] = 94
    states[4] = 0.8
    constants[37] = 0.8
    constants[38] = 1.5
    states[5] = 2.83
    constants[39] = 2.83
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[2] = states[0]+states[1]
    algebraic[3] = constants[13]*(exp(constants[15]*(algebraic[2]-constants[14]))-1.00000)
    algebraic[4] = algebraic[3]+constants[8]
    algebraic[0] =  voi % constants[12]
    algebraic[1] = constants[9]*exp(-constants[10]*(power((algebraic[0]*constants[6])/60.0000-constants[11], 2.00000)))
    rootfind_0(voi, constants, rates, states, algebraic)
    algebraic[18] = algebraic[10]+algebraic[4]
    algebraic[6] = constants[34]*(states[3]-constants[35])
    algebraic[7] = constants[36]*(states[4]-constants[37])
    rates[0] = custom_piecewise([less(algebraic[6]-algebraic[18] , 0.00000) & less(algebraic[18]-algebraic[7] , 0.00000), 0.00000 , less(algebraic[6]-algebraic[18] , 0.00000), -(algebraic[18]-algebraic[7])/constants[1] , less(algebraic[18]-algebraic[7] , 0.00000), (algebraic[6]-algebraic[18])/constants[0] , True, (algebraic[6]-algebraic[18])/constants[0]-(algebraic[18]-algebraic[7])/constants[1]])
    algebraic[5] = constants[32]*(states[2]-constants[33])
    rates[3] = custom_piecewise([less(algebraic[5]-algebraic[6] , 0.00000) & less(algebraic[6]-algebraic[18] , 0.00000), 0.00000 , less(algebraic[5]-algebraic[6] , 0.00000), -(algebraic[6]-algebraic[18])/constants[0] , less(algebraic[6]-algebraic[18] , 0.00000), (algebraic[5]-algebraic[6])/constants[4] , True, (algebraic[5]-algebraic[6])/constants[4]-(algebraic[6]-algebraic[18])/constants[0]])
    algebraic[8] = constants[38]*(states[5]-constants[39])
    rates[4] = custom_piecewise([less(algebraic[18]-algebraic[7] , 0.00000) & less(algebraic[7]-algebraic[8] , 0.00000), 0.00000 , less(algebraic[18]-algebraic[7] , 0.00000), -(algebraic[7]-algebraic[8])/constants[5] , less(algebraic[7]-algebraic[8] , 0.00000), (algebraic[18]-algebraic[7])/constants[1] , True, (algebraic[18]-algebraic[7])/constants[1]-(algebraic[7]-algebraic[8])/constants[5]])
    algebraic[19] = algebraic[15]+algebraic[4]
    rates[1] = custom_piecewise([less(algebraic[8]-algebraic[19] , 0.00000) & less(algebraic[19]-algebraic[5] , 0.00000), 0.00000 , less(algebraic[8]-algebraic[19] , 0.00000), -(algebraic[19]-algebraic[5])/constants[3] , less(algebraic[19]-algebraic[5] , 0.00000), (algebraic[8]-algebraic[19])/constants[2] , True, (algebraic[8]-algebraic[19])/constants[2]-(algebraic[19]-algebraic[5])/constants[3]])
    rates[2] = custom_piecewise([less(algebraic[19]-algebraic[5] , 0.00000) & less(algebraic[5]-algebraic[6] , 0.00000), 0.00000 , less(algebraic[19]-algebraic[5] , 0.00000), -(algebraic[5]-algebraic[6])/constants[4] , less(algebraic[5]-algebraic[6] , 0.00000), (algebraic[19]-algebraic[5])/constants[3] , True, (algebraic[19]-algebraic[5])/constants[3]-(algebraic[5]-algebraic[6])/constants[4]])
    rates[5] = custom_piecewise([less(algebraic[7]-algebraic[8] , 0.00000) & less(algebraic[8]-algebraic[19] , 0.00000), 0.00000 , less(algebraic[7]-algebraic[8] , 0.00000), -(algebraic[8]-algebraic[19])/constants[2] , less(algebraic[8]-algebraic[19] , 0.00000), (algebraic[7]-algebraic[8])/constants[5] , True, (algebraic[7]-algebraic[8])/constants[5]-(algebraic[8]-algebraic[19])/constants[2]])
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[2] = states[0]+states[1]
    algebraic[3] = constants[13]*(exp(constants[15]*(algebraic[2]-constants[14]))-1.00000)
    algebraic[4] = algebraic[3]+constants[8]
    algebraic[0] =  voi % constants[12]
    algebraic[1] = constants[9]*exp(-constants[10]*(power((algebraic[0]*constants[6])/60.0000-constants[11], 2.00000)))
    algebraic[18] = algebraic[10]+algebraic[4]
    algebraic[6] = constants[34]*(states[3]-constants[35])
    algebraic[7] = constants[36]*(states[4]-constants[37])
    algebraic[5] = constants[32]*(states[2]-constants[33])
    algebraic[8] = constants[38]*(states[5]-constants[39])
    algebraic[19] = algebraic[15]+algebraic[4]
    algebraic[20] = algebraic[18]-algebraic[19]
    return algebraic

initialGuess0 = None
def rootfind_0(voi, constants, rates, states, algebraic):
    """Calculate values of algebraic variables for DAE"""
    from scipy.optimize import fsolve
    global initialGuess0
    if initialGuess0 is None: initialGuess0 = ones(9)*0.1
    if not iterable(voi):
        soln = fsolve(residualSN_0, initialGuess0, args=(algebraic, voi, constants, rates, states), xtol=1E-6)
        initialGuess0 = soln
        algebraic[9] = soln[0]
        algebraic[10] = soln[1]
        algebraic[11] = soln[2]
        algebraic[12] = soln[3]
        algebraic[13] = soln[4]
        algebraic[14] = soln[5]
        algebraic[15] = soln[6]
        algebraic[16] = soln[7]
        algebraic[17] = soln[8]
    else:
        for (i,t) in enumerate(voi):
            soln = fsolve(residualSN_0, initialGuess0, args=(algebraic[:,i], voi[i], constants, rates[:i], states[:,i]), xtol=1E-6)
            initialGuess0 = soln
            algebraic[9][i] = soln[0]
            algebraic[10][i] = soln[1]
            algebraic[11][i] = soln[2]
            algebraic[12][i] = soln[3]
            algebraic[13][i] = soln[4]
            algebraic[14][i] = soln[5]
            algebraic[15][i] = soln[6]
            algebraic[16][i] = soln[7]
            algebraic[17][i] = soln[8]

def residualSN_0(algebraicCandidate, algebraic, voi, constants, rates, states):
    resid = array([0.0] * 9)
    algebraic[9] = algebraicCandidate[0]
    algebraic[10] = algebraicCandidate[1]
    algebraic[11] = algebraicCandidate[2]
    algebraic[12] = algebraicCandidate[3]
    algebraic[13] = algebraicCandidate[4]
    algebraic[14] = algebraicCandidate[5]
    algebraic[15] = algebraicCandidate[6]
    algebraic[16] = algebraicCandidate[7]
    algebraic[17] = algebraicCandidate[8]
    resid[0] = (algebraic[9]-(states[0]-algebraic[11]))
    resid[1] = (algebraic[10]-(algebraic[1]*algebraic[12]+(1.00000-algebraic[1])*algebraic[13]))
    resid[2] = (algebraic[12]-constants[16]*(algebraic[9]-constants[17]))
    resid[3] = (algebraic[13]-constants[18]*(exp(constants[19]*(algebraic[9]-constants[20]))-1.00000))
    resid[4] = (algebraic[14]-(states[1]+algebraic[11]))
    resid[5] = (algebraic[15]-(algebraic[1]*algebraic[16]+(1.00000-algebraic[1])*algebraic[17]))
    resid[6] = (algebraic[16]-constants[21]*(algebraic[14]-constants[22]))
    resid[7] = (algebraic[17]-constants[23]*(exp(constants[24]*(algebraic[14]-constants[25]))-1.00000))
    resid[8] = (algebraic[10]-((algebraic[1]*constants[26]*(algebraic[11]-constants[27])+(constants[31]-algebraic[1])*constants[28]*(exp(constants[29]*(algebraic[11]-constants[30]))-constants[31]))-algebraic[15]))
    return resid

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
        self.R_mt = 0.06
        self.R_av = 1.4
        self.R_tc = 0.18
        self.R_pv = 0.48
        self.R_pul = 19
        self.R_sys = 140
        self.HR = 80
        self.V_tot = 5.5
        self.P_pl = -0.533289474
        self.A = 1
        self.B = 80
        self.C = 0.27
        self.period = 0.405
        self.P_0_pcd = 0.067
        self.V_0_pcd = 0.2
        self.lambda_pcd = 30
        self.E_es_lvf = 454
        self.V_d_lvf = 0.005
        self.P_0_lvf = 0.17
        self.lambda_lvf = 15
        self.V_0_lvf = 0.005
        self.E_es_rvf = 87
        self.V_d_rvf = 0.005
        self.P_0_rvf = 0.16
        self.lambda_rvf = 15
        self.V_0_rvf = 0.005
        self.E_es_spt = 6500
        self.V_d_spt = 0.002
        self.P_0_spt = 0.148
        self.lambda_spt = 435
        self.V_0_spt = 0.002
        self.one = 1
        self.E_es_pa = 45
        self.V_d_pa = 0.16
        self.E_es_pu = 0.8
        self.V_d_pu = 0.2
        self.E_es_ao = 94
        self.V_d_ao = 0.8
        self.E_es_vc = 1.5
        self.V_d_vc = 2.83

    def to_dict(self):
        return {
            "R_mt": self.R_mt,
            "R_av": self.R_av,
            "R_tc": self.R_tc,
            "R_pv": self.R_pv,
            "R_pul": self.R_pul,
            "R_sys": self.R_sys,
            "HR": self.HR,
            "V_tot": self.V_tot,
            "P_pl": self.P_pl,
            "A": self.A,
            "B": self.B,
            "C": self.C,
            "period": self.period,
            "P_0_pcd": self.P_0_pcd,
            "V_0_pcd": self.V_0_pcd,
            "lambda_pcd": self.lambda_pcd,
            "E_es_lvf": self.E_es_lvf,
            "V_d_lvf": self.V_d_lvf,
            "P_0_lvf": self.P_0_lvf,
            "lambda_lvf": self.lambda_lvf,
            "V_0_lvf": self.V_0_lvf,
            "E_es_rvf": self.E_es_rvf,
            "V_d_rvf": self.V_d_rvf,
            "P_0_rvf": self.P_0_rvf,
            "lambda_rvf": self.lambda_rvf,
            "V_0_rvf": self.V_0_rvf,
            "E_es_spt": self.E_es_spt,
            "V_d_spt": self.V_d_spt,
            "P_0_spt": self.P_0_spt,
            "lambda_spt": self.lambda_spt,
            "V_0_spt": self.V_0_spt,
            "one": self.one,
            "E_es_pa": self.E_es_pa,
            "V_d_pa": self.V_d_pa,
            "E_es_pu": self.E_es_pu,
            "V_d_pu": self.V_d_pu,
            "E_es_ao": self.E_es_ao,
            "V_d_ao": self.V_d_ao,
            "E_es_vc": self.E_es_vc,
            "V_d_vc": self.V_d_vc,
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
        y0=[0.005, 0.005, 0.16, 0.2, 0.8, 2.83],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "shaw_chase_starfinger_smith_hann_desaive_ghuysen_2007"
        self.curve_names = [
            "V_lv",
            "V_rv",
            "V_pa",
            "V_pu",
            "V_ao",
            "V_vc",
        ]
        self.state_names = ['V_lv', 'V_rv', 'V_pa', 'V_pu', 'V_ao', 'V_vc']
        self.algebraic_names = ['tau', 'e_t', 'V_pcd', 'P_pcd', 'P_peri', 'P_pa', 'P_pu', 'P_ao', 'P_vc', 'V_lvf', 'P_lvf', 'V_spt', 'P_es_lvf', 'P_ed_lvf', 'V_rvf', 'P_rvf', 'P_es_rvf', 'P_ed_rvf', 'P_lv', 'P_rv', 'P_sept']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 40
        p = self.params

        # direct mapping
        c[0] = p.R_mt
        c[1] = p.R_av
        c[2] = p.R_tc
        c[3] = p.R_pv
        c[4] = p.R_pul
        c[5] = p.R_sys
        c[6] = p.HR
        c[7] = p.V_tot
        c[8] = p.P_pl
        c[9] = p.A
        c[10] = p.B
        c[11] = p.C
        c[12] = p.period
        c[13] = p.P_0_pcd
        c[14] = p.V_0_pcd
        c[15] = p.lambda_pcd
        c[16] = p.E_es_lvf
        c[17] = p.V_d_lvf
        c[18] = p.P_0_lvf
        c[19] = p.lambda_lvf
        c[20] = p.V_0_lvf
        c[21] = p.E_es_rvf
        c[22] = p.V_d_rvf
        c[23] = p.P_0_rvf
        c[24] = p.lambda_rvf
        c[25] = p.V_0_rvf
        c[26] = p.E_es_spt
        c[27] = p.V_d_spt
        c[28] = p.P_0_spt
        c[29] = p.lambda_spt
        c[30] = p.V_0_spt
        c[31] = p.one
        c[32] = p.E_es_pa
        c[33] = p.V_d_pa
        c[34] = p.E_es_pu
        c[35] = p.V_d_pu
        c[36] = p.E_es_ao
        c[37] = p.V_d_ao
        c[38] = p.E_es_vc
        c[39] = p.V_d_vc

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
