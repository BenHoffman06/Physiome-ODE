# Size of variable arrays:
sizeAlgebraic = 50
sizeStates = 13
sizeConstants = 53
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (second)"
    legend_constants[0] = "R_cm in component cell (dimensionless)"
    legend_constants[1] = "R in component cell (kilojoule_per_mole_kelvin)"
    legend_constants[2] = "T in component cell (kelvin)"
    legend_constants[3] = "F in component cell (kilojoule_per_mole_millivolt)"
    legend_constants[50] = "S in component cell (kilojoule_per_mole)"
    legend_constants[51] = "Z in component cell (millivolt)"
    legend_algebraic[8] = "electric_potential in component cell (millivolt)"
    legend_constants[4] = "protonmotive_force in component cell (millivolt)"
    legend_algebraic[9] = "ex_membrane_potential in component cell (millivolt)"
    legend_algebraic[10] = "in_membrane_potential in component cell (millivolt)"
    legend_constants[5] = "c_buffi in component cell (molar_proton_per_pH_unit)"
    legend_constants[6] = "c_buffe in component cell (molar_proton_per_pH_unit)"
    legend_algebraic[0] = "pH_e in component cell (dimensionless)"
    legend_algebraic[4] = "pH_i in component cell (dimensionless)"
    legend_constants[7] = "pKa in component cell (dimensionless)"
    legend_states[0] = "He in component He (micromolar)"
    legend_states[1] = "Hi in component Hi (micromolar)"
    legend_algebraic[7] = "delta_pH in component cell (dimensionless)"
    legend_constants[8] = "dpH in component cell (dimensionless)"
    legend_algebraic[5] = "C0_i in component cell (molar_proton_per_pH_unit)"
    legend_algebraic[2] = "C0_e in component cell (molar_proton_per_pH_unit)"
    legend_algebraic[6] = "r_buffi in component cell (dimensionless)"
    legend_algebraic[3] = "r_buffe in component cell (dimensionless)"
    legend_constants[9] = "BN in component cell (dimensionless)"
    legend_algebraic[11] = "u in component cell (dimensionless)"
    legend_algebraic[13] = "EmN in component redox_potentials (millivolt)"
    legend_algebraic[32] = "EmU in component redox_potentials (millivolt)"
    legend_algebraic[29] = "Emc in component redox_potentials (millivolt)"
    legend_algebraic[31] = "Ema in component redox_potentials (millivolt)"
    legend_constants[10] = "EmN0 in component redox_potentials (millivolt)"
    legend_constants[11] = "EmU0 in component redox_potentials (millivolt)"
    legend_constants[12] = "Emc0 in component redox_potentials (millivolt)"
    legend_algebraic[12] = "NAD in component NAD (micromolar)"
    legend_states[2] = "NADH in component NADH (micromolar)"
    legend_algebraic[30] = "UQ in component UQ (micromolar)"
    legend_states[3] = "UQH2 in component UQH2 (micromolar)"
    legend_states[4] = "c_2 in component c_2 (micromolar)"
    legend_algebraic[28] = "c_3 in component c_3 (micromolar)"
    legend_constants[13] = "Nt in component NAD (micromolar)"
    legend_algebraic[34] = "vDH in component vDH (flux)"
    legend_algebraic[36] = "vC1 in component vC1 (flux)"
    legend_states[5] = "O2 in component O2 (micromolar)"
    legend_algebraic[39] = "vC4 in component vC4 (flux)"
    legend_constants[14] = "nA in component vSN (dimensionless)"
    legend_algebraic[38] = "vC3 in component vC3 (flux)"
    legend_algebraic[43] = "vSN in component vSN (flux)"
    legend_algebraic[44] = "vEX in component vEX (flux)"
    legend_algebraic[47] = "vPI in component vPI (flux)"
    legend_constants[52] = "vLK in component vLK (flux)"
    legend_algebraic[48] = "vCK in component vCK (flux)"
    legend_algebraic[49] = "vEFF in component vEFF (flux)"
    legend_algebraic[17] = "ADP_mi in component ADP_mi (micromolar)"
    legend_algebraic[14] = "ADP_ti in component ADP_ti (micromolar)"
    legend_algebraic[15] = "ADP_fi in component ADP_fi (micromolar)"
    legend_constants[15] = "kDDi in component ADP_fi (micromolar)"
    legend_constants[16] = "Mg_fi in component Mg_fi (micromolar)"
    legend_constants[17] = "Ai_SUM in component ADP_ti (micromolar)"
    legend_states[6] = "ATP_ti in component ATP_ti (micromolar)"
    legend_algebraic[19] = "ATP_mi in component ATP_mi (micromolar)"
    legend_algebraic[16] = "ATP_fi in component ATP_fi (micromolar)"
    legend_constants[18] = "kDTi in component ATP_fi (micromolar)"
    legend_algebraic[20] = "ADP_me in component ADP_me (micromolar)"
    legend_states[7] = "ADP_te in component ADP_te (micromolar)"
    legend_algebraic[18] = "ADP_fe in component ADP_fe (micromolar)"
    legend_constants[19] = "kDDe in component ADP_fe (micromolar)"
    legend_constants[20] = "Mg_fe in component Mg_fe (micromolar)"
    legend_algebraic[45] = "vUT in component vUT (flux)"
    legend_algebraic[46] = "vAK in component vAK (flux)"
    legend_algebraic[22] = "ATP_me in component ATP_me (micromolar)"
    legend_states[8] = "ATP_te in component ATP_te (micromolar)"
    legend_algebraic[21] = "ATP_fe in component ATP_fe (micromolar)"
    legend_constants[21] = "kDTe in component ATP_fe (micromolar)"
    legend_algebraic[23] = "AMP_e in component AMP_e (micromolar)"
    legend_constants[22] = "Ae_SUM in component AMP_e (micromolar)"
    legend_algebraic[24] = "Cr in component Cr (micromolar)"
    legend_constants[23] = "C_SUM in component Cr (micromolar)"
    legend_states[9] = "PCr in component PCr (micromolar)"
    legend_algebraic[26] = "Pi_ji in component Pi_ji (micromolar)"
    legend_states[10] = "Pi_ti in component Pi_ti (micromolar)"
    legend_algebraic[27] = "Pi_je in component Pi_je (micromolar)"
    legend_states[11] = "Pi_te in component Pi_te (micromolar)"
    legend_algebraic[25] = "P_SUM in component P_SUM (micromolar)"
    legend_constants[24] = "ct in component c_3 (micromolar)"
    legend_constants[25] = "Ut in component UQ (micromolar)"
    legend_states[12] = "a_2 in component a_2 (micromolar)"
    legend_algebraic[33] = "A3_2 in component a_2 (dimensionless)"
    legend_constants[26] = "Ema0 in component a_2 (millivolt)"
    legend_constants[27] = "at in component a_2 (micromolar)"
    legend_algebraic[1] = "a_3 in component a_3 (micromolar)"
    legend_constants[28] = "kDH in component vDH (flux)"
    legend_constants[29] = "KmN in component vDH (micromolar)"
    legend_constants[30] = "pD in component vDH (dimensionless)"
    legend_constants[31] = "kC1 in component vC1 (flux)"
    legend_algebraic[35] = "delta_GC1 in component vC1 (millivolt)"
    legend_constants[32] = "kC3 in component vC3 (flux)"
    legend_algebraic[37] = "delta_GC3 in component vC3 (millivolt)"
    legend_constants[33] = "kC4 in component vC4 (flux)"
    legend_constants[34] = "KmO in component vC4 (micromolar)"
    legend_constants[35] = "kSN in component vSN (flux)"
    legend_algebraic[41] = "delta_GSN in component vSN (millivolt)"
    legend_algebraic[40] = "delta_Gp in component vSN (kilojoule_per_mole)"
    legend_constants[36] = "delta_Gp0 in component vSN (kilojoule_per_mole)"
    legend_algebraic[42] = "gamma in component vSN (dimensionless)"
    legend_constants[37] = "kEX in component vEX (flux)"
    legend_constants[38] = "km_ADP in component vEX (micromolar)"
    legend_constants[39] = "km_A in component vUT (micromolar)"
    legend_constants[40] = "kUT in component vUT (flux)"
    legend_constants[41] = "kf_AK in component vAK (second_order_rate_constant)"
    legend_constants[42] = "kb_AK in component vAK (second_order_rate_constant)"
    legend_constants[43] = "kL1 in component vLK (flux)"
    legend_constants[44] = "kL2 in component vLK (per_millivolt)"
    legend_constants[45] = "kPI in component vPI (second_order_rate_constant)"
    legend_constants[46] = "kf_CK in component vCK (third_order_rate_constant)"
    legend_constants[47] = "kb_CK in component vCK (second_order_rate_constant)"
    legend_constants[48] = "pH_o in component vEFF (dimensionless)"
    legend_constants[49] = "k_EFF in component vEFF (flux)"
    legend_rates[2] = "d/dt NADH in component NADH (micromolar)"
    legend_rates[5] = "d/dt O2 in component O2 (micromolar)"
    legend_rates[1] = "d/dt Hi in component Hi (micromolar)"
    legend_rates[0] = "d/dt He in component He (micromolar)"
    legend_rates[6] = "d/dt ATP_ti in component ATP_ti (micromolar)"
    legend_rates[7] = "d/dt ADP_te in component ADP_te (micromolar)"
    legend_rates[8] = "d/dt ATP_te in component ATP_te (micromolar)"
    legend_rates[9] = "d/dt PCr in component PCr (micromolar)"
    legend_rates[10] = "d/dt Pi_ti in component Pi_ti (micromolar)"
    legend_rates[11] = "d/dt Pi_te in component Pi_te (micromolar)"
    legend_rates[4] = "d/dt c_2 in component c_2 (micromolar)"
    legend_rates[3] = "d/dt UQH2 in component UQH2 (micromolar)"
    legend_rates[12] = "d/dt a_2 in component a_2 (micromolar)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    constants[0] = 15.0
    constants[1] = 0.0083
    constants[2] = 289.0
    constants[3] = 0.0965
    constants[4] = 190.0
    constants[5] = 0.022
    constants[6] = 0.025
    constants[7] = 6.8
    states[0] = 1.00
    states[1] = 1.00
    constants[8] = 0.001
    constants[9] = 5.0
    constants[10] = -320.0
    constants[11] = 85.0
    constants[12] = 250.0
    states[2] = 500.0
    states[3] = 1.00
    states[4] = 1.00
    constants[13] = 2970.0
    states[5] = 1.00
    constants[14] = 2.5
    constants[15] = 282
    constants[16] = 380.0
    constants[17] = 16260.0
    states[6] = 1.00
    constants[18] = 17
    states[7] = 1.00
    constants[19] = 347
    constants[20] = 4000.0
    states[8] = 1.00
    constants[21] = 24
    constants[22] = 1600.2
    constants[23] = 35000.0
    states[9] = 1.00
    states[10] = 1.00
    states[11] = 1.00
    constants[24] = 270.0
    constants[25] = 1350.0
    states[12] = 1.00
    constants[26] = 540.0
    constants[27] = 135.0
    constants[28] = 28074
    constants[29] = 100.0
    constants[30] = 0.8
    constants[31] = 238.95
    constants[32] = 136.41
    constants[33] = 136.41
    constants[34] = 120.0
    constants[35] = 34316.0
    constants[36] = 31.9
    constants[37] = 54572
    constants[38] = 3.5
    constants[39] = 150.0
    constants[40] = 686.5
    constants[41] = 862.10
    constants[42] = 22.747
    constants[43] = 2.5
    constants[44] = 0.038
    constants[45] = 69.421
    constants[46] = 1.9258
    constants[47] = 0.00087538
    constants[48] = 7.0
    constants[49] = 1.9258
    constants[50] = 2.30300*constants[1]*constants[2]
    constants[51] = 2.30300*constants[1]*(constants[2]/constants[3])
    constants[52] = constants[43]*(exp(constants[44]*constants[4])-1.00000)
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[0] = -log(states[0]/1.00000e+06, 10)
    algebraic[4] = -log(states[1]/1.00000e+06, 10)
    algebraic[7] = constants[51]*(algebraic[4]-algebraic[0])
    algebraic[8] = -(constants[4]-algebraic[7])
    algebraic[11] = algebraic[8]/constants[4]
    algebraic[28] = constants[24]-states[4]
    algebraic[29] = constants[12]+constants[51]*log(algebraic[28]/states[4], 10)
    algebraic[31] = algebraic[29]+constants[4]*((2.00000+2.00000*algebraic[11])/2.00000)
    algebraic[33] = power(10.0000, (algebraic[31]-constants[26])/constants[51])
    rates[12] = constants[27]/(1.00000+algebraic[33])
    algebraic[12] = constants[13]-states[2]
    algebraic[34] = constants[28]*(1.00000/(power(1.00000+constants[29]/(algebraic[12]/states[2]), constants[30])))
    algebraic[13] = constants[10]+(constants[51]/2.00000)*log(algebraic[12]/states[2], 10)
    algebraic[30] = constants[25]-states[3]
    algebraic[32] = constants[11]+(constants[51]/2.00000)*log(algebraic[30]/states[3], 10)
    algebraic[35] = algebraic[32]-(algebraic[13]+constants[4]*(4.00000/2.00000))
    algebraic[36] = constants[31]*algebraic[35]
    rates[2] = (algebraic[34]-algebraic[36])*(constants[0]/constants[9])
    algebraic[37] = algebraic[29]-(algebraic[32]+constants[4]*((4.00000-2.00000*algebraic[11])/2.00000))
    algebraic[38] = constants[32]*algebraic[37]
    rates[3] = constants[0]*(algebraic[36]-algebraic[38])
    algebraic[39] = constants[33]*states[12]*states[4]*(1.00000/(1.00000+constants[34]/states[5]))
    rates[5] = -algebraic[39]
    rates[4] = (algebraic[38]+algebraic[39]*2.00000)*constants[0]*2.00000
    algebraic[14] = constants[17]-states[6]
    algebraic[40] = constants[36]/(constants[3]+constants[51]*log(1.00000e+06*(states[6]/(algebraic[14]*states[10])), 10))
    algebraic[41] = constants[14]*constants[4]-algebraic[40]
    algebraic[42] = power(10.0000, algebraic[41]/constants[51])
    algebraic[43] = constants[35]*((algebraic[42]-1.00000)/(algebraic[42]+1.00000))
    algebraic[10] = 0.650000*algebraic[8]
    algebraic[15] = algebraic[14]/(1.00000+constants[16]/constants[15])
    algebraic[16] = states[6]/(1.00000+constants[16]/constants[18])
    algebraic[18] = states[7]/(1.00000+constants[20]/constants[19])
    algebraic[21] = states[8]/(1.00000+constants[20]/constants[21])
    algebraic[44] = constants[37]*(algebraic[18]/(algebraic[18]+algebraic[21]*(power(10.0000, -algebraic[10]/constants[51])))-algebraic[15]/(algebraic[15]+algebraic[16]*(power(10.0000, -algebraic[10]/constants[51]))))*(1.00000/(1.00000+constants[38]/algebraic[18]))
    rates[6] = (algebraic[43]-algebraic[44])*constants[0]
    algebraic[5] = (power(10.0000, -algebraic[4])-power(10.0000, -algebraic[4]-constants[8]))/constants[8]
    algebraic[6] = constants[5]/algebraic[5]
    algebraic[26] = states[10]/(1.00000+power(10.0000, algebraic[4]-constants[7]))
    algebraic[27] = states[11]/(1.00000+power(10.0000, algebraic[0]-constants[7]))
    algebraic[47] = constants[45]*(states[0]*algebraic[27]-states[1]*algebraic[26])
    rates[1] = ((((4.00000-2.00000*algebraic[11])*algebraic[38]+4.00000*algebraic[36])-(2.00000*(2.00000+2.00000*algebraic[11])*algebraic[39]+constants[14]*algebraic[43]+algebraic[11]*algebraic[44]+(1.00000-algebraic[11])*algebraic[47]+constants[52]))*constants[0])/algebraic[6]
    rates[10] = (algebraic[47]-algebraic[43])*constants[0]
    algebraic[45] = constants[40]*(1.00000/(1.00000+constants[39]/states[8]))
    rates[11] = algebraic[45]-algebraic[47]
    algebraic[24] = constants[23]-states[9]
    algebraic[48] = constants[46]*states[7]*states[9]*states[0]-constants[47]*states[8]*algebraic[24]
    algebraic[20] = states[7]-algebraic[18]
    algebraic[22] = states[8]-algebraic[21]
    algebraic[23] = constants[22]-(states[8]+states[7])
    algebraic[46] = constants[41]*algebraic[20]*algebraic[18]-constants[42]*algebraic[22]*algebraic[23]
    rates[7] = algebraic[45]-(algebraic[44]+2.00000*algebraic[46]+algebraic[48])
    rates[8] = (algebraic[44]+algebraic[46]+algebraic[48])-algebraic[45]
    rates[9] = -algebraic[48]
    algebraic[2] = (power(10.0000, -algebraic[0])-power(10.0000, -algebraic[0]-constants[8]))/constants[8]
    algebraic[3] = constants[6]/algebraic[2]
    algebraic[49] = constants[49]*(constants[48]-algebraic[0])
    rates[0] = ((2.00000*(2.00000+2.00000*algebraic[11])*algebraic[39]+(4.00000-2.00000*algebraic[11])*algebraic[38]+4.00000*algebraic[36])-(constants[14]*algebraic[43]+algebraic[11]*algebraic[44]+(1.00000-algebraic[11])*algebraic[47]+constants[52]+algebraic[48]+algebraic[49]))/algebraic[3]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = -log(states[0]/1.00000e+06, 10)
    algebraic[4] = -log(states[1]/1.00000e+06, 10)
    algebraic[7] = constants[51]*(algebraic[4]-algebraic[0])
    algebraic[8] = -(constants[4]-algebraic[7])
    algebraic[11] = algebraic[8]/constants[4]
    algebraic[28] = constants[24]-states[4]
    algebraic[29] = constants[12]+constants[51]*log(algebraic[28]/states[4], 10)
    algebraic[31] = algebraic[29]+constants[4]*((2.00000+2.00000*algebraic[11])/2.00000)
    algebraic[33] = power(10.0000, (algebraic[31]-constants[26])/constants[51])
    algebraic[12] = constants[13]-states[2]
    algebraic[34] = constants[28]*(1.00000/(power(1.00000+constants[29]/(algebraic[12]/states[2]), constants[30])))
    algebraic[13] = constants[10]+(constants[51]/2.00000)*log(algebraic[12]/states[2], 10)
    algebraic[30] = constants[25]-states[3]
    algebraic[32] = constants[11]+(constants[51]/2.00000)*log(algebraic[30]/states[3], 10)
    algebraic[35] = algebraic[32]-(algebraic[13]+constants[4]*(4.00000/2.00000))
    algebraic[36] = constants[31]*algebraic[35]
    algebraic[37] = algebraic[29]-(algebraic[32]+constants[4]*((4.00000-2.00000*algebraic[11])/2.00000))
    algebraic[38] = constants[32]*algebraic[37]
    algebraic[39] = constants[33]*states[12]*states[4]*(1.00000/(1.00000+constants[34]/states[5]))
    algebraic[14] = constants[17]-states[6]
    algebraic[40] = constants[36]/(constants[3]+constants[51]*log(1.00000e+06*(states[6]/(algebraic[14]*states[10])), 10))
    algebraic[41] = constants[14]*constants[4]-algebraic[40]
    algebraic[42] = power(10.0000, algebraic[41]/constants[51])
    algebraic[43] = constants[35]*((algebraic[42]-1.00000)/(algebraic[42]+1.00000))
    algebraic[10] = 0.650000*algebraic[8]
    algebraic[15] = algebraic[14]/(1.00000+constants[16]/constants[15])
    algebraic[16] = states[6]/(1.00000+constants[16]/constants[18])
    algebraic[18] = states[7]/(1.00000+constants[20]/constants[19])
    algebraic[21] = states[8]/(1.00000+constants[20]/constants[21])
    algebraic[44] = constants[37]*(algebraic[18]/(algebraic[18]+algebraic[21]*(power(10.0000, -algebraic[10]/constants[51])))-algebraic[15]/(algebraic[15]+algebraic[16]*(power(10.0000, -algebraic[10]/constants[51]))))*(1.00000/(1.00000+constants[38]/algebraic[18]))
    algebraic[5] = (power(10.0000, -algebraic[4])-power(10.0000, -algebraic[4]-constants[8]))/constants[8]
    algebraic[6] = constants[5]/algebraic[5]
    algebraic[26] = states[10]/(1.00000+power(10.0000, algebraic[4]-constants[7]))
    algebraic[27] = states[11]/(1.00000+power(10.0000, algebraic[0]-constants[7]))
    algebraic[47] = constants[45]*(states[0]*algebraic[27]-states[1]*algebraic[26])
    algebraic[45] = constants[40]*(1.00000/(1.00000+constants[39]/states[8]))
    algebraic[24] = constants[23]-states[9]
    algebraic[48] = constants[46]*states[7]*states[9]*states[0]-constants[47]*states[8]*algebraic[24]
    algebraic[20] = states[7]-algebraic[18]
    algebraic[22] = states[8]-algebraic[21]
    algebraic[23] = constants[22]-(states[8]+states[7])
    algebraic[46] = constants[41]*algebraic[20]*algebraic[18]-constants[42]*algebraic[22]*algebraic[23]
    algebraic[2] = (power(10.0000, -algebraic[0])-power(10.0000, -algebraic[0]-constants[8]))/constants[8]
    algebraic[3] = constants[6]/algebraic[2]
    algebraic[49] = constants[49]*(constants[48]-algebraic[0])
    algebraic[1] = constants[27]-states[12]
    algebraic[9] = -0.350000*algebraic[8]
    algebraic[17] = algebraic[14]-algebraic[15]
    algebraic[19] = states[6]-algebraic[16]
    algebraic[25] = states[9]+states[8]*3.00000+states[7]*2.00000+algebraic[23]+states[11]+(states[6]*3.00000+algebraic[14]*2.00000+states[10])/constants[0]
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
        self.R_cm = 15.0
        self.R = 0.0083
        self.T = 289.0
        self.F = 0.0965
        self.protonmotive_force = 190.0
        self.c_buffi = 0.022
        self.c_buffe = 0.025
        self.pKa = 6.8
        self.dpH = 0.001
        self.BN = 5.0
        self.EmN0 = -320.0
        self.EmU0 = 85.0
        self.Emc0 = 250.0
        self.Nt = 2970.0
        self.nA = 2.5
        self.kDDi = 282
        self.Mg_fi = 380.0
        self.Ai_SUM = 16260.0
        self.kDTi = 17
        self.kDDe = 347
        self.Mg_fe = 4000.0
        self.kDTe = 24
        self.Ae_SUM = 1600.2
        self.C_SUM = 35000.0
        self.ct = 270.0
        self.Ut = 1350.0
        self.Ema0 = 540.0
        self.at = 135.0
        self.kDH = 28074
        self.KmN = 100.0
        self.pD = 0.8
        self.kC1 = 238.95
        self.kC3 = 136.41
        self.kC4 = 136.41
        self.KmO = 120.0
        self.kSN = 34316.0
        self.delta_Gp0 = 31.9
        self.kEX = 54572
        self.km_ADP = 3.5
        self.km_A = 150.0
        self.kUT = 686.5
        self.kf_AK = 862.10
        self.kb_AK = 22.747
        self.kL1 = 2.5
        self.kL2 = 0.038
        self.kPI = 69.421
        self.kf_CK = 1.9258
        self.kb_CK = 0.00087538
        self.pH_o = 7.0
        self.k_EFF = 1.9258

    def to_dict(self):
        return {
            "R_cm": self.R_cm,
            "R": self.R,
            "T": self.T,
            "F": self.F,
            "protonmotive_force": self.protonmotive_force,
            "c_buffi": self.c_buffi,
            "c_buffe": self.c_buffe,
            "pKa": self.pKa,
            "dpH": self.dpH,
            "BN": self.BN,
            "EmN0": self.EmN0,
            "EmU0": self.EmU0,
            "Emc0": self.Emc0,
            "Nt": self.Nt,
            "nA": self.nA,
            "kDDi": self.kDDi,
            "Mg_fi": self.Mg_fi,
            "Ai_SUM": self.Ai_SUM,
            "kDTi": self.kDTi,
            "kDDe": self.kDDe,
            "Mg_fe": self.Mg_fe,
            "kDTe": self.kDTe,
            "Ae_SUM": self.Ae_SUM,
            "C_SUM": self.C_SUM,
            "ct": self.ct,
            "Ut": self.Ut,
            "Ema0": self.Ema0,
            "at": self.at,
            "kDH": self.kDH,
            "KmN": self.KmN,
            "pD": self.pD,
            "kC1": self.kC1,
            "kC3": self.kC3,
            "kC4": self.kC4,
            "KmO": self.KmO,
            "kSN": self.kSN,
            "delta_Gp0": self.delta_Gp0,
            "kEX": self.kEX,
            "km_ADP": self.km_ADP,
            "km_A": self.km_A,
            "kUT": self.kUT,
            "kf_AK": self.kf_AK,
            "kb_AK": self.kb_AK,
            "kL1": self.kL1,
            "kL2": self.kL2,
            "kPI": self.kPI,
            "kf_CK": self.kf_CK,
            "kb_CK": self.kb_CK,
            "pH_o": self.pH_o,
            "k_EFF": self.k_EFF,
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
        y0=[1.00, 1.00, 500.0, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "korzeniewski_zoladz_2001"
        self.curve_names = [
            "He",
            "Hi",
            "NADH",
            "UQH2",
            "c_2",
            "O2",
            "ATP_ti",
            "ADP_te",
            "ATP_te",
            "PCr",
            "Pi_ti",
            "Pi_te",
            "a_2",
        ]
        self.state_names = ['He', 'Hi', 'NADH', 'UQH2', 'c_2', 'O2', 'ATP_ti', 'ADP_te', 'ATP_te', 'PCr', 'Pi_ti', 'Pi_te', 'a_2']
        self.algebraic_names = ['pH_e', 'a_3', 'C0_e', 'r_buffe', 'pH_i', 'C0_i', 'r_buffi', 'delta_pH', 'electric_potential', 'ex_membrane_potential', 'in_membrane_potential', 'u', 'NAD', 'EmN', 'ADP_ti', 'ADP_fi', 'ATP_fi', 'ADP_mi', 'ADP_fe', 'ATP_mi', 'ADP_me', 'ATP_fe', 'ATP_me', 'AMP_e', 'Cr', 'P_SUM', 'Pi_ji', 'Pi_je', 'c_3', 'Emc', 'UQ', 'Ema', 'EmU', 'A3_2', 'vDH', 'delta_GC1', 'vC1', 'delta_GC3', 'vC3', 'vC4', 'delta_Gp', 'delta_GSN', 'gamma', 'vSN', 'vEX', 'vUT', 'vAK', 'vPI', 'vCK', 'vEFF']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 53
        p = self.params

        # direct mapping
        c[0] = p.R_cm
        c[1] = p.R
        c[2] = p.T
        c[3] = p.F
        c[4] = p.protonmotive_force
        c[5] = p.c_buffi
        c[6] = p.c_buffe
        c[7] = p.pKa
        c[8] = p.dpH
        c[9] = p.BN
        c[10] = p.EmN0
        c[11] = p.EmU0
        c[12] = p.Emc0
        c[13] = p.Nt
        c[14] = p.nA
        c[15] = p.kDDi
        c[16] = p.Mg_fi
        c[17] = p.Ai_SUM
        c[18] = p.kDTi
        c[19] = p.kDDe
        c[20] = p.Mg_fe
        c[21] = p.kDTe
        c[22] = p.Ae_SUM
        c[23] = p.C_SUM
        c[24] = p.ct
        c[25] = p.Ut
        c[26] = p.Ema0
        c[27] = p.at
        c[28] = p.kDH
        c[29] = p.KmN
        c[30] = p.pD
        c[31] = p.kC1
        c[32] = p.kC3
        c[33] = p.kC4
        c[34] = p.KmO
        c[35] = p.kSN
        c[36] = p.delta_Gp0
        c[37] = p.kEX
        c[38] = p.km_ADP
        c[39] = p.km_A
        c[40] = p.kUT
        c[41] = p.kf_AK
        c[42] = p.kb_AK
        c[43] = p.kL1
        c[44] = p.kL2
        c[45] = p.kPI
        c[46] = p.kf_CK
        c[47] = p.kb_CK
        c[48] = p.pH_o
        c[49] = p.k_EFF

        # derived constants
        c[50] = 2.30300*c[1]*c[2]
        c[51] = 2.30300*c[1]*(c[2]/c[3])
        c[52] = c[43]*(exp(c[44]*c[4])-1.00000)

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
