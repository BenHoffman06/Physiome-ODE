# Size of variable arrays:
sizeAlgebraic = 34
sizeStates = 16
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
    legend_algebraic[0] = "v1 in component v1 (flux)"
    legend_constants[0] = "Vmax in component v1 (flux)"
    legend_constants[1] = "Km in component v1 (umol_per_g)"
    legend_states[0] = "GL in component GL (umol_per_g)"
    legend_algebraic[1] = "v2 in component v2 (flux)"
    legend_constants[2] = "Vmax in component v2 (flux)"
    legend_constants[3] = "Km in component v2 (umol_per_g)"
    legend_states[1] = "O2 in component O2 (umol_per_g)"
    legend_algebraic[15] = "v3 in component v3 (flux)"
    legend_constants[4] = "Vmax in component v3 (first_order_rate_constant)"
    legend_algebraic[14] = "k3 in component v3 (first_order_rate_constant)"
    legend_states[2] = "FA in component FA (umol_per_g)"
    legend_algebraic[13] = "PS in component PS (dimensionless)"
    legend_constants[5] = "PS0 in component PS0 (dimensionless)"
    legend_algebraic[30] = "v4 in component v4 (flux)"
    legend_constants[6] = "Vmax in component v4 (first_order_rate_constant)"
    legend_algebraic[29] = "k4 in component v4 (first_order_rate_constant)"
    legend_constants[7] = "epsilon in component v4 (dimensionless)"
    legend_algebraic[4] = "RS in component RS (dimensionless)"
    legend_constants[8] = "RS0 in component RS0 (dimensionless)"
    legend_algebraic[28] = "AF in component AF (dimensionless)"
    legend_constants[9] = "AF0 in component AF0 (dimensionless)"
    legend_algebraic[17] = "v5 in component v5 (flux)"
    legend_constants[10] = "Vmax in component v5 (first_order_rate_constant)"
    legend_algebraic[16] = "k5 in component v5 (first_order_rate_constant)"
    legend_constants[11] = "epsilon in component v5 (dimensionless)"
    legend_states[3] = "GP in component GP (umol_per_g)"
    legend_algebraic[19] = "v6 in component v6 (flux)"
    legend_constants[12] = "Vmax in component v6 (first_order_rate_constant)"
    legend_algebraic[18] = "k6 in component v6 (first_order_rate_constant)"
    legend_constants[13] = "epsilon in component v6 (dimensionless)"
    legend_algebraic[3] = "CS in component CS (dimensionless)"
    legend_constants[14] = "CS0 in component CS0 (dimensionless)"
    legend_algebraic[23] = "v7 in component v7 (flux)"
    legend_constants[15] = "Vmax in component v7 (first_order_rate_constant)"
    legend_algebraic[21] = "k7 in component v7 (first_order_rate_constant)"
    legend_constants[16] = "epsilon in component v7 (dimensionless)"
    legend_states[4] = "GY in component GY (umol_per_g)"
    legend_algebraic[2] = "v8 in component v8 (flux)"
    legend_constants[17] = "Vmax in component v8 (first_order_rate_constant)"
    legend_constants[45] = "k8 in component v8 (first_order_rate_constant)"
    legend_states[5] = "TG in component TG (umol_per_g)"
    legend_algebraic[6] = "v9 in component v9 (flux)"
    legend_constants[18] = "Vmax in component v9 (first_order_rate_constant)"
    legend_algebraic[5] = "k9 in component v9 (first_order_rate_constant)"
    legend_states[6] = "PY in component PY (umol_per_g)"
    legend_algebraic[32] = "v10 in component v10 (flux)"
    legend_constants[19] = "Vmax in component v10 (first_order_rate_constant)"
    legend_algebraic[31] = "k10 in component v10 (first_order_rate_constant)"
    legend_constants[20] = "epsilon in component v10 (dimensionless)"
    legend_algebraic[8] = "v11 in component v11 (flux)"
    legend_constants[21] = "Vmax in component v11 (first_order_rate_constant)"
    legend_algebraic[7] = "k11 in component v11 (first_order_rate_constant)"
    legend_states[7] = "LA in component LA (umol_per_g)"
    legend_algebraic[22] = "v12 in component v12 (flux)"
    legend_constants[22] = "Vmax in component v12 (first_order_rate_constant)"
    legend_algebraic[20] = "k12 in component v12 (first_order_rate_constant)"
    legend_constants[23] = "epsilon in component v12 (dimensionless)"
    legend_states[8] = "AC in component AC (umol_per_g)"
    legend_algebraic[25] = "v13 in component v13 (flux)"
    legend_constants[24] = "Vmax in component v13 (first_order_rate_constant)"
    legend_algebraic[24] = "k13 in component v13 (first_order_rate_constant)"
    legend_states[9] = "CR in component CR (umol_per_g)"
    legend_algebraic[27] = "v14 in component v14 (flux)"
    legend_constants[25] = "Vmax in component v14 (first_order_rate_constant)"
    legend_algebraic[26] = "k14 in component v14 (first_order_rate_constant)"
    legend_states[10] = "PC in component PC (umol_per_g)"
    legend_algebraic[10] = "v15 in component v15 (flux)"
    legend_constants[26] = "Vmax in component v15 (first_order_rate_constant)"
    legend_algebraic[9] = "k15 in component v15 (first_order_rate_constant)"
    legend_constants[27] = "epsilon in component v15 (dimensionless)"
    legend_states[11] = "CoA_pool in component CoA_pool (umol_per_g)"
    legend_states[12] = "FC in component FC (umol_per_g)"
    legend_constants[28] = "FC0 in component FC0 (umol_per_g)"
    legend_algebraic[12] = "v16 in component v16 (flux)"
    legend_constants[29] = "Vmax in component v16 (first_order_rate_constant)"
    legend_algebraic[11] = "k16 in component v16 (first_order_rate_constant)"
    legend_constants[30] = "epsilon in component v16 (dimensionless)"
    legend_constants[46] = "v17 in component v17 (flux)"
    legend_constants[31] = "Vmax in component v17 (first_order_rate_constant)"
    legend_constants[44] = "k17 in component v17 (first_order_rate_constant)"
    legend_constants[32] = "ATP in component ATP (umol_per_g)"
    legend_constants[33] = "aGL in component GL (umol_per_ml)"
    legend_constants[34] = "sigmaGL in component GL (g_per_ml)"
    legend_algebraic[33] = "F in component model_parameters (ml_per_g_min)"
    legend_constants[35] = "aFA in component FA (umol_per_ml)"
    legend_constants[36] = "sigmaFA in component FA (g_per_ml)"
    legend_constants[37] = "aLA in component LA (umol_per_ml)"
    legend_constants[38] = "sigmaLA in component LA (g_per_ml)"
    legend_constants[39] = "aO2 in component O2 (umol_per_ml)"
    legend_constants[40] = "sigmaO2 in component O2 (g_per_ml)"
    legend_states[13] = "CO2 in component CO2 (umol_per_g)"
    legend_constants[41] = "aCO2 in component CO2 (umol_per_ml)"
    legend_constants[42] = "sigmaCO2 in component CO2 (g_per_ml)"
    legend_states[14] = "NAD in component NAD (umol_per_g)"
    legend_states[15] = "ADP in component ADP (umol_per_g)"
    legend_constants[43] = "NADH in component NADH (umol_per_g)"
    legend_rates[0] = "d/dt GL in component GL (umol_per_g)"
    legend_rates[2] = "d/dt FA in component FA (umol_per_g)"
    legend_rates[3] = "d/dt GP in component GP (umol_per_g)"
    legend_rates[4] = "d/dt GY in component GY (umol_per_g)"
    legend_rates[5] = "d/dt TG in component TG (umol_per_g)"
    legend_rates[6] = "d/dt PY in component PY (umol_per_g)"
    legend_rates[7] = "d/dt LA in component LA (umol_per_g)"
    legend_rates[8] = "d/dt AC in component AC (umol_per_g)"
    legend_rates[12] = "d/dt FC in component FC (umol_per_g)"
    legend_rates[11] = "d/dt CoA_pool in component CoA_pool (umol_per_g)"
    legend_rates[1] = "d/dt O2 in component O2 (umol_per_g)"
    legend_rates[13] = "d/dt CO2 in component CO2 (umol_per_g)"
    legend_rates[14] = "d/dt NAD in component NAD (umol_per_g)"
    legend_rates[15] = "d/dt ADP in component ADP (umol_per_g)"
    legend_rates[10] = "d/dt PC in component PC (umol_per_g)"
    legend_rates[9] = "d/dt CR in component CR (umol_per_g)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    constants[0] = 5.90
    constants[1] = 0.05
    states[0] = 0.998
    constants[2] = 67.6
    constants[3] = 0.01
    states[1] = 0.963
    constants[4] = 4.90
    states[2] = 0.021
    constants[5] = 0.2
    constants[6] = 21.3
    constants[7] = 0.6
    constants[8] = 0.111
    constants[9] = 0.523
    constants[10] = 2.82
    constants[11] = 0.254
    states[3] = 0.171
    constants[12] = 3.14
    constants[13] = 0.5
    constants[14] = 1.0
    constants[15] = 0.0162
    constants[16] = 0.5
    states[4] = 33.0
    constants[17] = 0.005
    states[5] = 3.96
    constants[18] = 1.8
    states[6] = 0.20
    constants[19] = 12.6
    constants[20] = 0.98
    constants[21] = 0.96
    states[7] = 1.98
    constants[22] = 695.7
    constants[23] = 0.75
    states[8] = 0.0046
    constants[24] = 0.455
    states[9] = 3.5
    constants[25] = 0.455
    states[10] = 8.80
    constants[26] = 626.1
    constants[27] = 0.669
    states[11] = 0.043
    states[12] = 0.0088
    constants[28] = 0.0088
    constants[29] = 67.0
    constants[30] = 0.775
    constants[31] = 7.76
    constants[32] = 4.5
    constants[33] = 4.0
    constants[34] = 3.76
    constants[35] = 0.5
    constants[36] = 13.2
    constants[37] = 1.8
    constants[38] = 0.51
    constants[39] = 6.53
    constants[40] = 1.0
    states[13] = 20.0
    constants[41] = 15.5
    constants[42] = 1.0
    states[14] = 1.81
    states[15] = 0.90
    constants[43] = 0.19
    constants[44] = constants[31]
    constants[45] = constants[17]
    constants[46] = constants[44]*constants[32]
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[4] = constants[43]/states[14]
    algebraic[9] = constants[26]*(constants[27]*((power(algebraic[4], -1.00000))/(power(constants[8], -1.00000)+power(algebraic[4], -1.00000)))+(1.00000-constants[27])*((power(states[12], -1.00000))/(power(constants[28], -1.00000)+power(states[12], -1.00000))))
    algebraic[10] = algebraic[9]*states[11]
    algebraic[11] = constants[29]*(constants[30]*((power(algebraic[4], -1.00000))/(power(constants[8], -1.00000)+power(algebraic[4], -1.00000)))+(1.00000-constants[30])*((power(states[12], -1.00000))/(power(constants[28], -1.00000)+power(states[12], -1.00000))))
    algebraic[12] = algebraic[11]*states[8]
    rates[11] = algebraic[12]-algebraic[10]
    algebraic[13] = states[15]/constants[32]
    algebraic[14] = constants[4]*((power(algebraic[13], -1.00000))/(power(constants[5], -1.00000)+power(algebraic[13], -1.00000)))
    algebraic[15] = algebraic[14]*states[2]
    algebraic[2] = constants[45]*states[5]
    rates[5] = (1.00000/3.00000)*algebraic[15]-algebraic[2]
    algebraic[0] = constants[0]*(states[0]/(constants[1]+states[0]))
    algebraic[16] = constants[10]*(constants[11]*(algebraic[13]/(constants[5]+algebraic[13]))+(1.00000-constants[11])*((power(algebraic[4], -1.00000))/(power(constants[8], -1.00000)+power(algebraic[4], -1.00000))))
    algebraic[17] = algebraic[16]*states[3]
    algebraic[3] = states[9]/states[10]
    algebraic[18] = constants[12]*(constants[13]*((power(algebraic[13], -1.00000))/(power(constants[5], -1.00000)+power(algebraic[13], -1.00000)))+(1.00000-constants[13])*(power((power(algebraic[3], -1.00000))/(power(constants[14], -1.00000)+power(algebraic[3], -1.00000)), 2.00000)))
    algebraic[19] = algebraic[18]*states[3]
    algebraic[21] = constants[15]*(constants[16]*(algebraic[13]/(constants[5]+algebraic[13]))+(1.00000-constants[16])*(power(algebraic[3]/(constants[14]+algebraic[3]), 2.00000)))
    algebraic[23] = algebraic[21]*states[4]
    rates[3] = (algebraic[0]+algebraic[23])-(algebraic[17]+algebraic[19])
    rates[4] = algebraic[19]-algebraic[23]
    algebraic[24] = constants[24]*((power(algebraic[13], -1.00000))/(power(constants[5], -1.00000)+power(algebraic[13], -1.00000)))
    algebraic[25] = algebraic[24]*states[9]
    algebraic[26] = constants[25]*(algebraic[13]/(constants[5]+algebraic[13]))
    algebraic[27] = algebraic[26]*states[10]
    rates[10] = algebraic[25]-algebraic[27]
    rates[9] = algebraic[27]-algebraic[25]
    algebraic[1] = constants[2]*(states[1]/(constants[3]+states[1]))
    algebraic[28] = states[8]/states[12]
    algebraic[29] = constants[6]*(constants[7]*((power(algebraic[28], -1.00000))/(power(constants[9], -1.00000)+power(algebraic[28], -1.00000)))+(1.00000-constants[7])*((power(algebraic[4], -1.00000))/(power(constants[8], -1.00000)+power(algebraic[4], -1.00000))))
    algebraic[30] = algebraic[29]*states[2]
    algebraic[20] = constants[22]*(constants[23]*((power(algebraic[4], -1.00000))/(power(constants[8], -1.00000)+power(algebraic[4], -1.00000)))+(1.00000-constants[23])*(algebraic[13]/(constants[5]+algebraic[13])))
    algebraic[22] = algebraic[20]*states[8]
    rates[15] = (algebraic[0]+algebraic[19]+2.00000*algebraic[30]+2.00000*algebraic[15]+algebraic[25]+constants[46])-(3.00000*algebraic[17]+algebraic[22]+6.00000*algebraic[1]+algebraic[27])
    algebraic[5] = constants[18]*(algebraic[4]/(constants[8]+algebraic[4]))
    algebraic[6] = algebraic[5]*states[6]
    algebraic[31] = constants[19]*(constants[20]*((power(algebraic[4], -1.00000))/(power(constants[8], -1.00000)+power(algebraic[4], -1.00000)))+(1.00000-constants[20])*((power(algebraic[28], -1.00000))/(power(constants[9], -1.00000)+power(algebraic[28], -1.00000))))
    algebraic[32] = algebraic[31]*states[6]
    algebraic[7] = constants[21]*((power(algebraic[4], -1.00000))/(power(constants[8], -1.00000)+power(algebraic[4], -1.00000)))
    algebraic[8] = algebraic[7]*states[7]
    rates[6] = (2.00000*algebraic[17]+algebraic[8])-(algebraic[6]+algebraic[32])
    rates[8] = (algebraic[32]+algebraic[30])-(algebraic[22]+algebraic[12])
    rates[12] = (algebraic[22]+algebraic[10]+algebraic[12])-(algebraic[32]+algebraic[30])
    rates[14] = (algebraic[6]+2.00000*algebraic[1])-(2.00000*algebraic[17]+algebraic[32]+algebraic[8]+(11.0000/3.00000)*algebraic[22]+(35.0000/3.00000)*algebraic[30])
    algebraic[33] = custom_piecewise([greater(voi , 0.00000) & less(voi , 5.00000), 1.00000 , True, 0.400000])
    rates[0] = algebraic[33]*(constants[33]-constants[34]*states[0])-algebraic[0]
    rates[2] = (3.00000*algebraic[2]+algebraic[33]*(constants[35]-constants[36]*states[2]))-(algebraic[15]+algebraic[30])
    rates[7] = (algebraic[6]+algebraic[33]*(constants[37]-constants[38]*states[7]))-algebraic[8]
    rates[1] = algebraic[33]*(constants[39]-constants[40]*states[1])-algebraic[1]
    rates[13] = algebraic[32]+2.00000*algebraic[22]+algebraic[33]*(constants[41]-constants[42]*states[13])
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[4] = constants[43]/states[14]
    algebraic[9] = constants[26]*(constants[27]*((power(algebraic[4], -1.00000))/(power(constants[8], -1.00000)+power(algebraic[4], -1.00000)))+(1.00000-constants[27])*((power(states[12], -1.00000))/(power(constants[28], -1.00000)+power(states[12], -1.00000))))
    algebraic[10] = algebraic[9]*states[11]
    algebraic[11] = constants[29]*(constants[30]*((power(algebraic[4], -1.00000))/(power(constants[8], -1.00000)+power(algebraic[4], -1.00000)))+(1.00000-constants[30])*((power(states[12], -1.00000))/(power(constants[28], -1.00000)+power(states[12], -1.00000))))
    algebraic[12] = algebraic[11]*states[8]
    algebraic[13] = states[15]/constants[32]
    algebraic[14] = constants[4]*((power(algebraic[13], -1.00000))/(power(constants[5], -1.00000)+power(algebraic[13], -1.00000)))
    algebraic[15] = algebraic[14]*states[2]
    algebraic[2] = constants[45]*states[5]
    algebraic[0] = constants[0]*(states[0]/(constants[1]+states[0]))
    algebraic[16] = constants[10]*(constants[11]*(algebraic[13]/(constants[5]+algebraic[13]))+(1.00000-constants[11])*((power(algebraic[4], -1.00000))/(power(constants[8], -1.00000)+power(algebraic[4], -1.00000))))
    algebraic[17] = algebraic[16]*states[3]
    algebraic[3] = states[9]/states[10]
    algebraic[18] = constants[12]*(constants[13]*((power(algebraic[13], -1.00000))/(power(constants[5], -1.00000)+power(algebraic[13], -1.00000)))+(1.00000-constants[13])*(power((power(algebraic[3], -1.00000))/(power(constants[14], -1.00000)+power(algebraic[3], -1.00000)), 2.00000)))
    algebraic[19] = algebraic[18]*states[3]
    algebraic[21] = constants[15]*(constants[16]*(algebraic[13]/(constants[5]+algebraic[13]))+(1.00000-constants[16])*(power(algebraic[3]/(constants[14]+algebraic[3]), 2.00000)))
    algebraic[23] = algebraic[21]*states[4]
    algebraic[24] = constants[24]*((power(algebraic[13], -1.00000))/(power(constants[5], -1.00000)+power(algebraic[13], -1.00000)))
    algebraic[25] = algebraic[24]*states[9]
    algebraic[26] = constants[25]*(algebraic[13]/(constants[5]+algebraic[13]))
    algebraic[27] = algebraic[26]*states[10]
    algebraic[1] = constants[2]*(states[1]/(constants[3]+states[1]))
    algebraic[28] = states[8]/states[12]
    algebraic[29] = constants[6]*(constants[7]*((power(algebraic[28], -1.00000))/(power(constants[9], -1.00000)+power(algebraic[28], -1.00000)))+(1.00000-constants[7])*((power(algebraic[4], -1.00000))/(power(constants[8], -1.00000)+power(algebraic[4], -1.00000))))
    algebraic[30] = algebraic[29]*states[2]
    algebraic[20] = constants[22]*(constants[23]*((power(algebraic[4], -1.00000))/(power(constants[8], -1.00000)+power(algebraic[4], -1.00000)))+(1.00000-constants[23])*(algebraic[13]/(constants[5]+algebraic[13])))
    algebraic[22] = algebraic[20]*states[8]
    algebraic[5] = constants[18]*(algebraic[4]/(constants[8]+algebraic[4]))
    algebraic[6] = algebraic[5]*states[6]
    algebraic[31] = constants[19]*(constants[20]*((power(algebraic[4], -1.00000))/(power(constants[8], -1.00000)+power(algebraic[4], -1.00000)))+(1.00000-constants[20])*((power(algebraic[28], -1.00000))/(power(constants[9], -1.00000)+power(algebraic[28], -1.00000))))
    algebraic[32] = algebraic[31]*states[6]
    algebraic[7] = constants[21]*((power(algebraic[4], -1.00000))/(power(constants[8], -1.00000)+power(algebraic[4], -1.00000)))
    algebraic[8] = algebraic[7]*states[7]
    algebraic[33] = custom_piecewise([greater(voi , 0.00000) & less(voi , 5.00000), 1.00000 , True, 0.400000])
    return algebraic

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
        self.Vmax = 5.90
        self.Km = 0.05
        self.Vmax_1 = 67.6
        self.Km_1 = 0.01
        self.Vmax_2 = 4.90
        self.PS0 = 0.2
        self.Vmax_3 = 21.3
        self.epsilon = 0.6
        self.RS0 = 0.111
        self.AF0 = 0.523
        self.Vmax_4 = 2.82
        self.epsilon_1 = 0.254
        self.Vmax_5 = 3.14
        self.epsilon_2 = 0.5
        self.CS0 = 1.0
        self.Vmax_6 = 0.0162
        self.epsilon_3 = 0.5
        self.Vmax_7 = 0.005
        self.Vmax_8 = 1.8
        self.Vmax_9 = 12.6
        self.epsilon_4 = 0.98
        self.Vmax_10 = 0.96
        self.Vmax_11 = 695.7
        self.epsilon_5 = 0.75
        self.Vmax_12 = 0.455
        self.Vmax_13 = 0.455
        self.Vmax_14 = 626.1
        self.epsilon_6 = 0.669
        self.FC0 = 0.0088
        self.Vmax_15 = 67.0
        self.epsilon_7 = 0.775
        self.Vmax_16 = 7.76
        self.ATP = 4.5
        self.aGL = 4.0
        self.sigmaGL = 3.76
        self.aFA = 0.5
        self.sigmaFA = 13.2
        self.aLA = 1.8
        self.sigmaLA = 0.51
        self.aO2 = 6.53
        self.sigmaO2 = 1.0
        self.aCO2 = 15.5
        self.sigmaCO2 = 1.0
        self.NADH = 0.19

    def to_dict(self):
        return {
            "Vmax": self.Vmax,
            "Km": self.Km,
            "Vmax_1": self.Vmax_1,
            "Km_1": self.Km_1,
            "Vmax_2": self.Vmax_2,
            "PS0": self.PS0,
            "Vmax_3": self.Vmax_3,
            "epsilon": self.epsilon,
            "RS0": self.RS0,
            "AF0": self.AF0,
            "Vmax_4": self.Vmax_4,
            "epsilon_1": self.epsilon_1,
            "Vmax_5": self.Vmax_5,
            "epsilon_2": self.epsilon_2,
            "CS0": self.CS0,
            "Vmax_6": self.Vmax_6,
            "epsilon_3": self.epsilon_3,
            "Vmax_7": self.Vmax_7,
            "Vmax_8": self.Vmax_8,
            "Vmax_9": self.Vmax_9,
            "epsilon_4": self.epsilon_4,
            "Vmax_10": self.Vmax_10,
            "Vmax_11": self.Vmax_11,
            "epsilon_5": self.epsilon_5,
            "Vmax_12": self.Vmax_12,
            "Vmax_13": self.Vmax_13,
            "Vmax_14": self.Vmax_14,
            "epsilon_6": self.epsilon_6,
            "FC0": self.FC0,
            "Vmax_15": self.Vmax_15,
            "epsilon_7": self.epsilon_7,
            "Vmax_16": self.Vmax_16,
            "ATP": self.ATP,
            "aGL": self.aGL,
            "sigmaGL": self.sigmaGL,
            "aFA": self.aFA,
            "sigmaFA": self.sigmaFA,
            "aLA": self.aLA,
            "sigmaLA": self.sigmaLA,
            "aO2": self.aO2,
            "sigmaO2": self.sigmaO2,
            "aCO2": self.aCO2,
            "sigmaCO2": self.sigmaCO2,
            "NADH": self.NADH,
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
        y0=[0.998, 0.963, 0.021, 0.171, 33.0, 3.96, 0.20, 1.98, 0.0046, 3.5, 8.80, 0.043, 0.0088, 20.0, 1.81, 0.90],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "salem_saidel_stanley_cabrera_2002"
        self.curve_names = [
            "GL",
            "O2",
            "FA",
            "GP",
            "GY",
            "TG",
            "PY",
            "LA",
            "AC",
            "CR",
            "PC",
            "CoA_pool",
            "FC",
            "CO2",
            "NAD",
            "ADP",
        ]
        self.state_names = ['GL', 'O2', 'FA', 'GP', 'GY', 'TG', 'PY', 'LA', 'AC', 'CR', 'PC', 'CoA_pool', 'FC', 'CO2', 'NAD', 'ADP']
        self.algebraic_names = ['v1', 'v2', 'v8', 'CS', 'RS', 'k9', 'v9', 'k11', 'v11', 'k15', 'v15', 'k16', 'v16', 'PS', 'k3', 'v3', 'k5', 'v5', 'k6', 'v6', 'k12', 'k7', 'v12', 'v7', 'k13', 'v13', 'k14', 'v14', 'AF', 'k4', 'v4', 'k10', 'v10', 'F']
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
        c[0] = p.Vmax
        c[1] = p.Km
        c[2] = p.Vmax_1
        c[3] = p.Km_1
        c[4] = p.Vmax_2
        c[5] = p.PS0
        c[6] = p.Vmax_3
        c[7] = p.epsilon
        c[8] = p.RS0
        c[9] = p.AF0
        c[10] = p.Vmax_4
        c[11] = p.epsilon_1
        c[12] = p.Vmax_5
        c[13] = p.epsilon_2
        c[14] = p.CS0
        c[15] = p.Vmax_6
        c[16] = p.epsilon_3
        c[17] = p.Vmax_7
        c[18] = p.Vmax_8
        c[19] = p.Vmax_9
        c[20] = p.epsilon_4
        c[21] = p.Vmax_10
        c[22] = p.Vmax_11
        c[23] = p.epsilon_5
        c[24] = p.Vmax_12
        c[25] = p.Vmax_13
        c[26] = p.Vmax_14
        c[27] = p.epsilon_6
        c[28] = p.FC0
        c[29] = p.Vmax_15
        c[30] = p.epsilon_7
        c[31] = p.Vmax_16
        c[32] = p.ATP
        c[33] = p.aGL
        c[34] = p.sigmaGL
        c[35] = p.aFA
        c[36] = p.sigmaFA
        c[37] = p.aLA
        c[38] = p.sigmaLA
        c[39] = p.aO2
        c[40] = p.sigmaO2
        c[41] = p.aCO2
        c[42] = p.sigmaCO2
        c[43] = p.NADH

        # derived constants
        c[44] = c[31]
        c[45] = c[17]
        c[46] = c[44]*c[32]

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
