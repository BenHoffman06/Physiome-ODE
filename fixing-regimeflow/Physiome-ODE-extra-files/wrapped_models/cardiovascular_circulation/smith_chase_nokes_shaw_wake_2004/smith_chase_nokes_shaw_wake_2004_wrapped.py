# Size of variable arrays:
sizeAlgebraic = 22
sizeStates = 10
sizeConstants = 43
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (second)"
    legend_constants[0] = "R_mt in component heart_parameters (kPa_second_per_mL)"
    legend_constants[1] = "R_av in component heart_parameters (kPa_second_per_mL)"
    legend_constants[2] = "R_tc in component heart_parameters (kPa_second_per_mL)"
    legend_constants[3] = "R_pv in component heart_parameters (kPa_second_per_mL)"
    legend_constants[4] = "R_pul in component heart_parameters (kPa_second_per_mL)"
    legend_constants[5] = "R_sys in component heart_parameters (kPa_second_per_mL)"
    legend_constants[6] = "L_tc in component heart_parameters (kPa_second2_per_mL)"
    legend_constants[7] = "L_pv in component heart_parameters (kPa_second2_per_mL)"
    legend_constants[8] = "L_mt in component heart_parameters (kPa_second2_per_mL)"
    legend_constants[9] = "L_av in component heart_parameters (kPa_second2_per_mL)"
    legend_constants[10] = "V_tot in component heart_parameters (mL)"
    legend_constants[11] = "P_th in component heart_parameters (kPa)"
    legend_algebraic[1] = "e_t in component driver_function (dimensionless)"
    legend_constants[12] = "A in component driver_function (dimensionless)"
    legend_constants[13] = "B in component driver_function (per_second2)"
    legend_constants[14] = "C in component driver_function (second)"
    legend_algebraic[0] = "tau in component driver_function (second)"
    legend_constants[15] = "period in component driver_function (second)"
    legend_algebraic[2] = "V_pcd in component pericardium (mL)"
    legend_algebraic[3] = "P_pcd in component pericardium (kPa)"
    legend_algebraic[4] = "P_peri in component pericardium (kPa)"
    legend_states[0] = "V_lv in component left_ventricle (mL)"
    legend_states[1] = "V_rv in component right_ventricle (mL)"
    legend_constants[16] = "P_0_pcd in component pericardium (kPa)"
    legend_constants[17] = "V_0_pcd in component pericardium (mL)"
    legend_constants[18] = "lambda_pcd in component pericardium (per_mL)"
    legend_algebraic[6] = "V_lvf in component left_ventricle (mL)"
    legend_algebraic[9] = "P_lvf in component left_ventricle (kPa)"
    legend_algebraic[10] = "P_lv in component left_ventricle (kPa)"
    legend_algebraic[5] = "V_spt in component septum (mL)"
    legend_algebraic[7] = "P_es_lvf in component lvf_calculator (kPa)"
    legend_algebraic[8] = "P_ed_lvf in component lvf_calculator (kPa)"
    legend_algebraic[18] = "P_pu in component pulmonary_vein (kPa)"
    legend_algebraic[17] = "P_ao in component aorta (kPa)"
    legend_constants[19] = "E_es_lvf in component lvf_calculator (kPa_per_mL)"
    legend_constants[20] = "lambda_lvf in component lvf_calculator (per_mL)"
    legend_constants[21] = "P_0_lvf in component lvf_calculator (kPa)"
    legend_states[2] = "Q_mt in component flow (mL_per_second)"
    legend_states[3] = "Q_av in component flow (mL_per_second)"
    legend_constants[22] = "V_d_lvf in component lvf_calculator (mL)"
    legend_constants[23] = "V_0_lvf in component lvf_calculator (mL)"
    legend_algebraic[11] = "V_rvf in component right_ventricle (mL)"
    legend_algebraic[14] = "P_rvf in component right_ventricle (kPa)"
    legend_algebraic[15] = "P_rv in component right_ventricle (kPa)"
    legend_algebraic[12] = "P_es_rvf in component rvf_calculator (kPa)"
    legend_algebraic[13] = "P_ed_rvf in component rvf_calculator (kPa)"
    legend_algebraic[16] = "P_pa in component pulmonary_artery (kPa)"
    legend_algebraic[19] = "P_vc in component vena_cava (kPa)"
    legend_constants[24] = "E_es_rvf in component rvf_calculator (kPa_per_mL)"
    legend_constants[25] = "lambda_rvf in component rvf_calculator (per_mL)"
    legend_constants[26] = "P_0_rvf in component rvf_calculator (kPa)"
    legend_states[4] = "Q_tc in component flow (mL_per_second)"
    legend_states[5] = "Q_pv in component flow (mL_per_second)"
    legend_constants[27] = "V_d_rvf in component rvf_calculator (mL)"
    legend_constants[28] = "V_0_rvf in component rvf_calculator (mL)"
    legend_constants[29] = "E_es_spt in component septum (kPa_per_mL)"
    legend_constants[30] = "V_d_spt in component septum (mL)"
    legend_constants[31] = "P_0_spt in component septum (kPa)"
    legend_constants[32] = "lambda_spt in component septum (per_mL)"
    legend_constants[33] = "V_0_spt in component septum (mL)"
    legend_constants[34] = "one in component septum (dimensionless)"
    legend_constants[35] = "E_es_pa in component pulmonary_artery (kPa_per_mL)"
    legend_states[6] = "V_pa in component pulmonary_artery (mL)"
    legend_constants[36] = "V_d_pa in component pulmonary_artery (mL)"
    legend_algebraic[20] = "Q_pul in component flow (mL_per_second)"
    legend_constants[37] = "E_es_pu in component pulmonary_vein (kPa_per_mL)"
    legend_states[7] = "V_pu in component pulmonary_vein (mL)"
    legend_constants[38] = "V_d_pu in component pulmonary_vein (mL)"
    legend_constants[39] = "E_es_ao in component aorta (kPa_per_mL)"
    legend_states[8] = "V_ao in component aorta (mL)"
    legend_constants[40] = "V_d_ao in component aorta (mL)"
    legend_algebraic[21] = "Q_sys in component flow (mL_per_second)"
    legend_constants[41] = "E_es_vc in component vena_cava (kPa_per_mL)"
    legend_states[9] = "V_vc in component vena_cava (mL)"
    legend_constants[42] = "V_d_vc in component vena_cava (mL)"
    legend_rates[0] = "d/dt V_lv in component left_ventricle (mL)"
    legend_rates[1] = "d/dt V_rv in component right_ventricle (mL)"
    legend_rates[6] = "d/dt V_pa in component pulmonary_artery (mL)"
    legend_rates[7] = "d/dt V_pu in component pulmonary_vein (mL)"
    legend_rates[8] = "d/dt V_ao in component aorta (mL)"
    legend_rates[9] = "d/dt V_vc in component vena_cava (mL)"
    legend_rates[2] = "d/dt Q_mt in component flow (mL_per_second)"
    legend_rates[3] = "d/dt Q_av in component flow (mL_per_second)"
    legend_rates[4] = "d/dt Q_tc in component flow (mL_per_second)"
    legend_rates[5] = "d/dt Q_pv in component flow (mL_per_second)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    constants[0] = 0.0158
    constants[1] = 0.0180
    constants[2] = 0.0237
    constants[3] = 0.0055
    constants[4] = 0.1552
    constants[5] = 1.0889
    constants[6] = 8.0093e-5
    constants[7] = 1.4868e-4
    constants[8] = 7.6968e-5
    constants[9] = 1.2189e-4
    constants[10] = 5.5
    constants[11] = -4
    constants[12] = 1
    constants[13] = 80
    constants[14] = 0.375
    constants[15] = 0.75
    states[0] = 94.6812
    states[1] = 90.7302
    constants[16] = 0.5003
    constants[17] = 200
    constants[18] = 0.03
    constants[19] = 2.8798
    constants[20] = 0.033
    constants[21] = 0.1203
    states[2] = 245.5813
    states[3] = 0
    constants[22] = 0
    constants[23] = 0
    constants[24] = 0.585
    constants[25] = 0.023
    constants[26] = 0.2157
    states[4] = 190.0661
    states[5] = 0
    constants[27] = 0
    constants[28] = 0
    constants[29] = 48.754
    constants[30] = 2
    constants[31] = 1.1101
    constants[32] = 0.435
    constants[33] = 2
    constants[34] = 1
    constants[35] = 0.369
    states[6] = 43.0123
    constants[36] = 0
    constants[37] = 0.0073
    states[7] = 808.4579
    constants[38] = 0
    constants[39] = 0.6913
    states[8] = 133.3381
    constants[40] = 0
    constants[41] = 0.0059
    states[9] = 329.7803
    constants[42] = 0
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[0] = custom_piecewise([less(states[2] , 0.00000) & less(states[3] , 0.00000), 0.00000 , less(states[2] , 0.00000), -states[3] , less(states[3] , 0.00000), states[2] , True, states[2]-states[3]])
    rates[1] = custom_piecewise([less(states[4] , 0.00000) & less(states[5] , 0.00000), 0.00000 , less(states[4] , 0.00000), -states[5] , less(states[5] , 0.00000), states[4] , True, states[4]-states[5]])
    algebraic[2] = states[0]+states[1]
    algebraic[3] = constants[16]*(exp(constants[18]*(algebraic[2]-constants[17]))-1.00000)
    algebraic[4] = algebraic[3]+constants[11]
    algebraic[0] = custom_piecewise([less_equal(voi , constants[15]), voi , less_equal(voi , constants[15]*2.00000), voi-constants[15] , less_equal(voi , constants[15]*3.00000), voi-constants[15]*2.00000 , less_equal(voi , constants[15]*4.00000), voi-constants[15]*3.00000 , less_equal(voi , constants[15]*5.00000), voi-constants[15]*4.00000 , less_equal(voi , constants[15]*6.00000), voi-constants[15]*5.00000 , less_equal(voi , constants[15]*7.00000), voi-constants[15]*6.00000 , less_equal(voi , constants[15]*8.00000), voi-constants[15]*7.00000 , less_equal(voi , constants[15]*9.00000), voi-constants[15]*8.00000 , less_equal(voi , constants[15]*10.0000), voi-constants[15]*9.00000 , less_equal(voi , constants[15]*11.0000), voi-constants[15]*10.0000 , less_equal(voi , constants[15]*12.0000), voi-constants[15]*11.0000 , less_equal(voi , constants[15]*13.0000), voi-constants[15]*12.0000 , True, float('nan')])
    algebraic[1] = constants[12]*exp(-constants[13]*(power(algebraic[0]-constants[14], 2.00000)))
    rootfind_0(voi, constants, rates, states, algebraic)
    algebraic[6] = states[0]-algebraic[5]
    algebraic[7] = constants[19]*(algebraic[6]-constants[22])
    algebraic[8] = constants[21]*(exp(constants[20]*(algebraic[6]-constants[23]))-1.00000)
    algebraic[9] = algebraic[1]*algebraic[7]+(1.00000-algebraic[1])*algebraic[8]
    algebraic[10] = algebraic[9]+algebraic[4]
    algebraic[17] = constants[39]*(states[8]-constants[40])
    rates[3] = custom_piecewise([less(algebraic[10]-algebraic[17] , 0.00000) & less(states[3] , 0.00000), 0.00000 , True, ((algebraic[10]-algebraic[17])-states[3]*constants[1])/constants[9]])
    algebraic[11] = states[1]+algebraic[5]
    algebraic[12] = constants[24]*(algebraic[11]-constants[27])
    algebraic[13] = constants[26]*(exp(constants[25]*(algebraic[11]-constants[28]))-1.00000)
    algebraic[14] = algebraic[1]*algebraic[12]+(1.00000-algebraic[1])*algebraic[13]
    algebraic[15] = algebraic[14]+algebraic[4]
    algebraic[16] = constants[35]*(states[6]-constants[36])+constants[11]
    rates[5] = custom_piecewise([less(algebraic[15]-algebraic[16] , 0.00000) & less(states[5] , 0.00000), 0.00000 , True, ((algebraic[15]-algebraic[16])-states[5]*constants[3])/constants[7]])
    algebraic[18] = constants[37]*(states[7]-constants[38])+constants[11]
    rates[2] = custom_piecewise([less(algebraic[18]-algebraic[10] , 0.00000) & less(states[2] , 0.00000), 0.00000 , True, ((algebraic[18]-algebraic[10])-states[2]*constants[0])/constants[8]])
    algebraic[19] = constants[41]*(states[9]-constants[42])
    rates[4] = custom_piecewise([less(algebraic[19]-algebraic[15] , 0.00000) & less(states[4] , 0.00000), 0.00000 , True, ((algebraic[19]-algebraic[15])-states[4]*constants[2])/constants[6]])
    algebraic[20] = (algebraic[16]-algebraic[18])/constants[4]
    rates[6] = custom_piecewise([less(states[5] , 0.00000), -algebraic[20] , True, states[5]-algebraic[20]])
    rates[7] = custom_piecewise([less(states[2] , 0.00000), algebraic[20] , True, algebraic[20]-states[2]])
    algebraic[21] = (algebraic[17]-algebraic[19])/constants[5]
    rates[8] = custom_piecewise([less(states[3] , 0.00000), -algebraic[21] , True, states[3]-algebraic[21]])
    rates[9] = custom_piecewise([less(states[4] , 0.00000), algebraic[21] , True, algebraic[21]-states[4]])
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[2] = states[0]+states[1]
    algebraic[3] = constants[16]*(exp(constants[18]*(algebraic[2]-constants[17]))-1.00000)
    algebraic[4] = algebraic[3]+constants[11]
    algebraic[0] = custom_piecewise([less_equal(voi , constants[15]), voi , less_equal(voi , constants[15]*2.00000), voi-constants[15] , less_equal(voi , constants[15]*3.00000), voi-constants[15]*2.00000 , less_equal(voi , constants[15]*4.00000), voi-constants[15]*3.00000 , less_equal(voi , constants[15]*5.00000), voi-constants[15]*4.00000 , less_equal(voi , constants[15]*6.00000), voi-constants[15]*5.00000 , less_equal(voi , constants[15]*7.00000), voi-constants[15]*6.00000 , less_equal(voi , constants[15]*8.00000), voi-constants[15]*7.00000 , less_equal(voi , constants[15]*9.00000), voi-constants[15]*8.00000 , less_equal(voi , constants[15]*10.0000), voi-constants[15]*9.00000 , less_equal(voi , constants[15]*11.0000), voi-constants[15]*10.0000 , less_equal(voi , constants[15]*12.0000), voi-constants[15]*11.0000 , less_equal(voi , constants[15]*13.0000), voi-constants[15]*12.0000 , True, float('nan')])
    algebraic[1] = constants[12]*exp(-constants[13]*(power(algebraic[0]-constants[14], 2.00000)))
    algebraic[6] = states[0]-algebraic[5]
    algebraic[7] = constants[19]*(algebraic[6]-constants[22])
    algebraic[8] = constants[21]*(exp(constants[20]*(algebraic[6]-constants[23]))-1.00000)
    algebraic[9] = algebraic[1]*algebraic[7]+(1.00000-algebraic[1])*algebraic[8]
    algebraic[10] = algebraic[9]+algebraic[4]
    algebraic[17] = constants[39]*(states[8]-constants[40])
    algebraic[11] = states[1]+algebraic[5]
    algebraic[12] = constants[24]*(algebraic[11]-constants[27])
    algebraic[13] = constants[26]*(exp(constants[25]*(algebraic[11]-constants[28]))-1.00000)
    algebraic[14] = algebraic[1]*algebraic[12]+(1.00000-algebraic[1])*algebraic[13]
    algebraic[15] = algebraic[14]+algebraic[4]
    algebraic[16] = constants[35]*(states[6]-constants[36])+constants[11]
    algebraic[18] = constants[37]*(states[7]-constants[38])+constants[11]
    algebraic[19] = constants[41]*(states[9]-constants[42])
    algebraic[20] = (algebraic[16]-algebraic[18])/constants[4]
    algebraic[21] = (algebraic[17]-algebraic[19])/constants[5]
    return algebraic

initialGuess0 = None
def rootfind_0(voi, constants, states, algebraic):
    """Calculate value of algebraic variable for DAE"""
    from scipy.optimize import fsolve
    global initialGuess0
    if initialGuess0 is None: initialGuess0 = 0.1
    if not iterable(voi):
        algebraic[5] = fsolve(residualSN_0, initialGuess0, args=(algebraic, voi, constants, rates, states), xtol=1E-6)
        initialGuess0 = algebraic[5]
    else:
        for (i,t) in enumerate(voi):
            algebraic[5][i] = fsolve(residualSN_0, initialGuess0, args=(algebraic[:,i], voi[i], constants, rates, states[:,i]), xtol=1E-6)
            initialGuess0 = algebraic[5][i]

def residualSN_0(algebraicCandidate, algebraic, voi, constants, rates, states):
    algebraic[5] = algebraicCandidate
    return (0.00000) - ((((algebraic[1]*constants[29]*(algebraic[5]-constants[30])+(constants[34]-algebraic[1])*constants[31]*(exp(constants[32]*(algebraic[5]-constants[33]))-constants[34]))-algebraic[1]*constants[19]*(states[0]-algebraic[5]))-(1.00000-algebraic[1])*constants[21]*(exp(constants[20]*(states[0]-algebraic[5]))-1.00000))+algebraic[1]*constants[24]*(states[1]+algebraic[5])+(1.00000-algebraic[1])*constants[26]*(exp(constants[25]*(states[1]+algebraic[5]))-1.00000))

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
        self.R_mt = 0.0158
        self.R_av = 0.0180
        self.R_tc = 0.0237
        self.R_pv = 0.0055
        self.R_pul = 0.1552
        self.R_sys = 1.0889
        self.L_tc = 8.0093e-5
        self.L_pv = 1.4868e-4
        self.L_mt = 7.6968e-5
        self.L_av = 1.2189e-4
        self.V_tot = 5.5
        self.P_th = -4
        self.A = 1
        self.B = 80
        self.C = 0.375
        self.period = 0.75
        self.P_0_pcd = 0.5003
        self.V_0_pcd = 200
        self.lambda_pcd = 0.03
        self.E_es_lvf = 2.8798
        self.lambda_lvf = 0.033
        self.P_0_lvf = 0.1203
        self.V_d_lvf = 0
        self.V_0_lvf = 0
        self.E_es_rvf = 0.585
        self.lambda_rvf = 0.023
        self.P_0_rvf = 0.2157
        self.V_d_rvf = 0
        self.V_0_rvf = 0
        self.E_es_spt = 48.754
        self.V_d_spt = 2
        self.P_0_spt = 1.1101
        self.lambda_spt = 0.435
        self.V_0_spt = 2
        self.one = 1
        self.E_es_pa = 0.369
        self.V_d_pa = 0
        self.E_es_pu = 0.0073
        self.V_d_pu = 0
        self.E_es_ao = 0.6913
        self.V_d_ao = 0
        self.E_es_vc = 0.0059
        self.V_d_vc = 0

    def to_dict(self):
        return {
            "R_mt": self.R_mt,
            "R_av": self.R_av,
            "R_tc": self.R_tc,
            "R_pv": self.R_pv,
            "R_pul": self.R_pul,
            "R_sys": self.R_sys,
            "L_tc": self.L_tc,
            "L_pv": self.L_pv,
            "L_mt": self.L_mt,
            "L_av": self.L_av,
            "V_tot": self.V_tot,
            "P_th": self.P_th,
            "A": self.A,
            "B": self.B,
            "C": self.C,
            "period": self.period,
            "P_0_pcd": self.P_0_pcd,
            "V_0_pcd": self.V_0_pcd,
            "lambda_pcd": self.lambda_pcd,
            "E_es_lvf": self.E_es_lvf,
            "lambda_lvf": self.lambda_lvf,
            "P_0_lvf": self.P_0_lvf,
            "V_d_lvf": self.V_d_lvf,
            "V_0_lvf": self.V_0_lvf,
            "E_es_rvf": self.E_es_rvf,
            "lambda_rvf": self.lambda_rvf,
            "P_0_rvf": self.P_0_rvf,
            "V_d_rvf": self.V_d_rvf,
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
        y0=[94.6812, 90.7302, 245.5813, 0, 190.0661, 0, 43.0123, 808.4579, 133.3381, 329.7803],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "smith_chase_nokes_shaw_wake_2004"
        self.curve_names = [
            "V_lv",
            "V_rv",
            "Q_mt",
            "Q_av",
            "Q_tc",
            "Q_pv",
            "V_pa",
            "V_pu",
            "V_ao",
            "V_vc",
        ]
        self.state_names = ['V_lv', 'V_rv', 'Q_mt', 'Q_av', 'Q_tc', 'Q_pv', 'V_pa', 'V_pu', 'V_ao', 'V_vc']
        self.algebraic_names = ['tau', 'e_t', 'V_pcd', 'P_pcd', 'P_peri', 'V_spt', 'V_lvf', 'P_es_lvf', 'P_ed_lvf', 'P_lvf', 'P_lv', 'V_rvf', 'P_es_rvf', 'P_ed_rvf', 'P_rvf', 'P_rv', 'P_pa', 'P_ao', 'P_pu', 'P_vc', 'Q_pul', 'Q_sys']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 43
        p = self.params

        # direct mapping
        c[0] = p.R_mt
        c[1] = p.R_av
        c[2] = p.R_tc
        c[3] = p.R_pv
        c[4] = p.R_pul
        c[5] = p.R_sys
        c[6] = p.L_tc
        c[7] = p.L_pv
        c[8] = p.L_mt
        c[9] = p.L_av
        c[10] = p.V_tot
        c[11] = p.P_th
        c[12] = p.A
        c[13] = p.B
        c[14] = p.C
        c[15] = p.period
        c[16] = p.P_0_pcd
        c[17] = p.V_0_pcd
        c[18] = p.lambda_pcd
        c[19] = p.E_es_lvf
        c[20] = p.lambda_lvf
        c[21] = p.P_0_lvf
        c[22] = p.V_d_lvf
        c[23] = p.V_0_lvf
        c[24] = p.E_es_rvf
        c[25] = p.lambda_rvf
        c[26] = p.P_0_rvf
        c[27] = p.V_d_rvf
        c[28] = p.V_0_rvf
        c[29] = p.E_es_spt
        c[30] = p.V_d_spt
        c[31] = p.P_0_spt
        c[32] = p.lambda_spt
        c[33] = p.V_0_spt
        c[34] = p.one
        c[35] = p.E_es_pa
        c[36] = p.V_d_pa
        c[37] = p.E_es_pu
        c[38] = p.V_d_pu
        c[39] = p.E_es_ao
        c[40] = p.V_d_ao
        c[41] = p.E_es_vc
        c[42] = p.V_d_vc

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
