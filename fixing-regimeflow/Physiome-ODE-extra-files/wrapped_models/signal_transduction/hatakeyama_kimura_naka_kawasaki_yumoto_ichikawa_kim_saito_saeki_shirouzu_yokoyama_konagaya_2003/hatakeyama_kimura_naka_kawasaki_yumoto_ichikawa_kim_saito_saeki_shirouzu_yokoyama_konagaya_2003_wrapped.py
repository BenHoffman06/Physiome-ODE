# Size of variable arrays:
sizeAlgebraic = 0
sizeStates = 33
sizeConstants = 80
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (s)"
    legend_constants[0] = "kf1 in component PI3K (second_order_rate_constant)"
    legend_constants[1] = "kb1 in component PI3K (first_order_rate_constant)"
    legend_constants[2] = "kf2 in component PI3K (second_order_rate_constant)"
    legend_constants[3] = "kb2 in component PI3K (first_order_rate_constant)"
    legend_constants[4] = "kf3 in component PI3K (first_order_rate_constant)"
    legend_constants[5] = "kb3 in component PI3K (first_order_rate_constant)"
    legend_constants[6] = "kf34 in component PI3K (first_order_rate_constant)"
    legend_constants[7] = "kb34 in component PI3K (first_order_rate_constant)"
    legend_constants[8] = "V4 in component PI3K (flux)"
    legend_constants[9] = "k4 in component PI3K (nm)"
    legend_constants[10] = "kf5 in component PI3K (second_order_rate_constant)"
    legend_constants[11] = "kb5 in component PI3K (first_order_rate_constant)"
    legend_constants[12] = "kf6 in component PI3K (first_order_rate_constant)"
    legend_constants[13] = "kb6 in component PI3K (first_order_rate_constant)"
    legend_constants[14] = "kf7 in component PI3K (first_order_rate_constant)"
    legend_constants[15] = "kb7 in component PI3K (first_order_rate_constant)"
    legend_constants[16] = "kf8 in component PI3K (first_order_rate_constant)"
    legend_constants[17] = "kb8 in component PI3K (second_order_rate_constant)"
    legend_constants[18] = "kf9 in component PI3K (first_order_rate_constant)"
    legend_constants[19] = "kb9 in component PI3K (second_order_rate_constant)"
    legend_constants[20] = "V10 in component PI3K (flux)"
    legend_constants[21] = "k10 in component PI3K (nm)"
    legend_constants[22] = "kf23 in component PI3K (second_order_rate_constant)"
    legend_constants[23] = "kb23 in component PI3K (first_order_rate_constant)"
    legend_constants[24] = "kf24 in component PI3K (first_order_rate_constant)"
    legend_constants[25] = "kb24 in component PI3K (first_order_rate_constant)"
    legend_constants[26] = "kf25 in component PI3K (first_order_rate_constant)"
    legend_constants[27] = "kb25 in component PI3K (second_order_rate_constant)"
    legend_constants[28] = "V26 in component PI3K (flux)"
    legend_constants[29] = "k26 in component PI3K (nm)"
    legend_states[0] = "R in component PI3K (nm)"
    legend_states[1] = "Shc in component PI3K (nm)"
    legend_states[2] = "PI3K in component PI3K (nm)"
    legend_states[3] = "HRG in component PI3K (nm)"
    legend_states[4] = "R_HRG in component PI3K (nm)"
    legend_states[5] = "R_HRG2 in component PI3K (nm)"
    legend_states[6] = "Internalisation in component PI3K (nm)"
    legend_states[7] = "RP in component PI3K (nm)"
    legend_states[8] = "R_Shc in component PI3K (nm)"
    legend_states[9] = "R_ShP in component PI3K (nm)"
    legend_states[10] = "ShP in component PI3K (nm)"
    legend_states[11] = "R_ShGS in component PI3K (nm)"
    legend_states[12] = "ShGS in component PI3K (nm)"
    legend_states[13] = "GS in component PI3K (nm)"
    legend_states[14] = "R_PI3K in component PI3K (nm)"
    legend_states[15] = "R_PI3Kstar in component PI3K (nm)"
    legend_states[16] = "PI3Kstar in component PI3K (nm)"
    legend_constants[30] = "two in component PI3K (dimensionless)"
    legend_states[17] = "RasGTP in component RasGDPtoRasGTP (nm)"
    legend_constants[31] = "kf11 in component RasGDPtoRasGTP (first_order_rate_constant)"
    legend_constants[32] = "k11 in component RasGDPtoRasGTP (nm)"
    legend_constants[33] = "V12 in component RasGDPtoRasGTP (flux)"
    legend_constants[34] = "k12 in component RasGDPtoRasGTP (nm)"
    legend_states[18] = "RasGDP in component RasGDPtoRasGTP (nm)"
    legend_states[19] = "Akt_PIPP in component Akt (nm)"
    legend_states[20] = "RAF_star in component RAF (nm)"
    legend_constants[35] = "kf13 in component RAF (first_order_rate_constant)"
    legend_constants[36] = "k13 in component RAF (nm)"
    legend_constants[37] = "kf14 in component RAF (first_order_rate_constant)"
    legend_constants[38] = "k14 in component RAF (nm)"
    legend_constants[39] = "E in component RAF (nm)"
    legend_states[21] = "RAF in component RAF (nm)"
    legend_states[22] = "MEKP in component MEK (nm)"
    legend_states[23] = "MEKPP in component MEK (nm)"
    legend_constants[40] = "kf27 in component Akt (first_order_rate_constant)"
    legend_constants[41] = "k27 in component Akt (nm)"
    legend_constants[42] = "V28 in component Akt (flux)"
    legend_constants[43] = "k28 in component Akt (nm)"
    legend_constants[44] = "kf29 in component Akt (second_order_rate_constant)"
    legend_constants[45] = "kb29 in component Akt (first_order_rate_constant)"
    legend_constants[46] = "V30 in component Akt (flux)"
    legend_constants[47] = "k30 in component Akt (nm)"
    legend_constants[48] = "kf31 in component Akt (first_order_rate_constant)"
    legend_constants[49] = "k31 in component Akt (nm)"
    legend_constants[50] = "V32 in component Akt (flux)"
    legend_constants[51] = "k32 in component Akt (nm)"
    legend_constants[52] = "kf33 in component Akt (first_order_rate_constant)"
    legend_constants[53] = "k33 in component Akt (nm)"
    legend_constants[54] = "k16 in component Akt (nm)"
    legend_constants[55] = "k18 in component Akt (nm)"
    legend_states[24] = "P in component Akt (nm)"
    legend_states[25] = "PIP3 in component Akt (nm)"
    legend_states[26] = "Akt in component Akt (nm)"
    legend_states[27] = "Akt_PIP3 in component Akt (nm)"
    legend_states[28] = "Akt_PIP in component Akt (nm)"
    legend_constants[56] = "PP2A in component Akt (nm)"
    legend_constants[57] = "one in component Akt (dimensionless)"
    legend_constants[58] = "PP2A in component MEK (nm)"
    legend_states[29] = "MEK in component MEK (nm)"
    legend_constants[59] = "kf15 in component MEK (first_order_rate_constant)"
    legend_constants[60] = "k15 in component MEK (nm)"
    legend_constants[61] = "kf16 in component MEK (first_order_rate_constant)"
    legend_constants[62] = "k16 in component MEK (nm)"
    legend_constants[63] = "kf17 in component MEK (first_order_rate_constant)"
    legend_constants[64] = "k17 in component MEK (nm)"
    legend_constants[65] = "kf18 in component MEK (first_order_rate_constant)"
    legend_constants[66] = "k18 in component MEK (nm)"
    legend_constants[67] = "k31 in component MEK (nm)"
    legend_constants[68] = "k33 in component MEK (nm)"
    legend_constants[69] = "one in component MEK (dimensionless)"
    legend_constants[70] = "MKP3 in component ERK (nm)"
    legend_states[30] = "ERK in component ERK (nm)"
    legend_states[31] = "ERKP in component ERK (nm)"
    legend_states[32] = "ERKPP in component ERK (nm)"
    legend_constants[71] = "kf19 in component ERK (first_order_rate_constant)"
    legend_constants[72] = "k19 in component ERK (nm)"
    legend_constants[73] = "kf20 in component ERK (first_order_rate_constant)"
    legend_constants[74] = "k20 in component ERK (nm)"
    legend_constants[75] = "kf21 in component ERK (first_order_rate_constant)"
    legend_constants[76] = "k21 in component ERK (nm)"
    legend_constants[77] = "kf22 in component ERK (first_order_rate_constant)"
    legend_constants[78] = "k22 in component ERK (nm)"
    legend_constants[79] = "one in component ERK (dimensionless)"
    legend_rates[0] = "d/dt R in component PI3K (nm)"
    legend_rates[3] = "d/dt HRG in component PI3K (nm)"
    legend_rates[4] = "d/dt R_HRG in component PI3K (nm)"
    legend_rates[5] = "d/dt R_HRG2 in component PI3K (nm)"
    legend_rates[7] = "d/dt RP in component PI3K (nm)"
    legend_rates[6] = "d/dt Internalisation in component PI3K (nm)"
    legend_rates[8] = "d/dt R_Shc in component PI3K (nm)"
    legend_rates[1] = "d/dt Shc in component PI3K (nm)"
    legend_rates[9] = "d/dt R_ShP in component PI3K (nm)"
    legend_rates[13] = "d/dt GS in component PI3K (nm)"
    legend_rates[10] = "d/dt ShP in component PI3K (nm)"
    legend_rates[11] = "d/dt R_ShGS in component PI3K (nm)"
    legend_rates[12] = "d/dt ShGS in component PI3K (nm)"
    legend_rates[14] = "d/dt R_PI3K in component PI3K (nm)"
    legend_rates[2] = "d/dt PI3K in component PI3K (nm)"
    legend_rates[15] = "d/dt R_PI3Kstar in component PI3K (nm)"
    legend_rates[16] = "d/dt PI3Kstar in component PI3K (nm)"
    legend_rates[18] = "d/dt RasGDP in component RasGDPtoRasGTP (nm)"
    legend_rates[17] = "d/dt RasGTP in component RasGDPtoRasGTP (nm)"
    legend_rates[21] = "d/dt RAF in component RAF (nm)"
    legend_rates[20] = "d/dt RAF_star in component RAF (nm)"
    legend_rates[24] = "d/dt P in component Akt (nm)"
    legend_rates[25] = "d/dt PIP3 in component Akt (nm)"
    legend_rates[26] = "d/dt Akt in component Akt (nm)"
    legend_rates[27] = "d/dt Akt_PIP3 in component Akt (nm)"
    legend_rates[28] = "d/dt Akt_PIP in component Akt (nm)"
    legend_rates[19] = "d/dt Akt_PIPP in component Akt (nm)"
    legend_rates[29] = "d/dt MEK in component MEK (nm)"
    legend_rates[22] = "d/dt MEKP in component MEK (nm)"
    legend_rates[23] = "d/dt MEKPP in component MEK (nm)"
    legend_rates[30] = "d/dt ERK in component ERK (nm)"
    legend_rates[32] = "d/dt ERKPP in component ERK (nm)"
    legend_rates[31] = "d/dt ERKP in component ERK (nm)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    constants[0] = 0.0012
    constants[1] = 0.00076
    constants[2] = 0.01
    constants[3] = 0.1
    constants[4] = 1
    constants[5] = 0.01
    constants[6] = 0.001
    constants[7] = 0
    constants[8] = 62.5
    constants[9] = 50
    constants[10] = 0.1
    constants[11] = 1
    constants[12] = 20
    constants[13] = 5
    constants[14] = 60
    constants[15] = 546
    constants[16] = 2040
    constants[17] = 15700
    constants[18] = 40.8
    constants[19] = 0
    constants[20] = 0.0154
    constants[21] = 340
    constants[22] = 0.1
    constants[23] = 2
    constants[24] = 9.85
    constants[25] = 0.0985
    constants[26] = 45.8
    constants[27] = 0.047
    constants[28] = 2620
    constants[29] = 3680
    states[0] = 80
    states[1] = 1000
    states[2] = 10
    states[3] = 10
    states[4] = 0
    states[5] = 0
    states[6] = 0
    states[7] = 0
    states[8] = 0
    states[9] = 0
    states[10] = 0
    states[11] = 0
    states[12] = 0
    states[13] = 10
    states[14] = 0
    states[15] = 0
    states[16] = 0
    constants[30] = 2
    states[17] = 0
    constants[31] = 0.222
    constants[32] = 0.181
    constants[33] = 0.289
    constants[34] = 0.0571
    states[18] = 120
    states[19] = 0.0
    states[20] = 100
    constants[35] = 1.53
    constants[36] = 11.7
    constants[37] = 0.00673
    constants[38] = 8.07
    constants[39] = 7
    states[21] = 0
    states[22] = 0
    states[23] = 0
    constants[40] = 16.9
    constants[41] = 39.1
    constants[42] = 17000
    constants[43] = 9.02
    constants[44] = 507
    constants[45] = 234
    constants[46] = 20000
    constants[47] = 80000
    constants[48] = 0.107
    constants[49] = 4.35
    constants[50] = 20000
    constants[51] = 80000
    constants[52] = 0.211
    constants[53] = 12
    constants[54] = 2200
    constants[55] = 60
    states[24] = 800
    states[25] = 0
    states[26] = 10
    states[27] = 0
    states[28] = 0
    constants[56] = 11.4
    constants[57] = 1
    constants[58] = 11.4
    states[29] = 120
    constants[59] = 3.5
    constants[60] = 317
    constants[61] = 0.058
    constants[62] = 2200
    constants[63] = 2.9
    constants[64] = 317
    constants[65] = 0.058
    constants[66] = 60
    constants[67] = 4.35
    constants[68] = 12
    constants[69] = 1
    constants[70] = 2.4
    states[30] = 1000
    states[31] = 0
    states[32] = 0
    constants[71] = 9.5
    constants[72] = 146000
    constants[73] = 0.3
    constants[74] = 160
    constants[75] = 16
    constants[76] = 146000
    constants[77] = 0.27
    constants[78] = 60
    constants[79] = 1
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[0] = -constants[0]*states[0]*states[3]+constants[1]*states[4]
    rates[3] = -constants[0]*states[0]*states[3]+constants[1]*states[4]
    rates[4] = (constants[0]*states[0]*states[3]-constants[1]*states[4])-constants[30]*(constants[2]*states[4]*states[4]-constants[3]*states[5])
    rates[5] = ((constants[2]*states[4]*states[4]-constants[3]*states[5])-(constants[4]*states[5]-constants[5]*states[7]))+(constants[8]*states[7])/(constants[9]+states[7])
    rates[7] = ((((((constants[4]*states[5]-constants[5]*states[7])-(constants[8]*states[7])/(constants[9]+states[7]))-(constants[10]*states[7]*states[1]-constants[11]*states[8]))+(constants[16]*states[9]-constants[17]*states[12]*states[7]))-(constants[22]*states[7]*states[2]-constants[23]*states[14]))+(constants[26]*states[15]-constants[27]*states[7]*states[16]))-(constants[6]*states[7]-constants[7]*states[6])
    rates[6] = constants[6]*states[7]-constants[7]*states[6]
    rates[8] = (constants[10]*states[7]*states[1]-constants[11]*states[8])-(constants[12]*states[8]-constants[13]*states[9])
    rates[1] = -(constants[10]*states[7]*states[1]-constants[11]*states[8])+(constants[20]*states[10])/(constants[21]+states[10])
    rates[9] = (constants[12]*states[8]-constants[13]*states[9])-(constants[14]*states[9]-constants[15]*states[11])
    rates[13] = -(constants[14]*states[9]-constants[15]*states[11])+(constants[18]*states[12]-constants[19]*states[13]*states[10])
    rates[10] = (constants[18]*states[12]-constants[19]*states[13]*states[10])-(constants[20]*states[10])/(constants[21]+states[10])
    rates[11] = (constants[14]*states[9]-constants[15]*states[11])-(constants[16]*states[9]-constants[17]*states[12]*states[7])
    rates[12] = (constants[16]*states[9]-constants[17]*states[12]*states[7])-(constants[18]*states[12]-constants[19]*states[13]*states[10])
    rates[14] = (constants[22]*states[7]*states[2]-constants[23]*states[14])-(constants[24]*states[14]-constants[25]*states[15])
    rates[2] = -(constants[22]*states[7]*states[2]-constants[23]*states[14])+(constants[28]*states[16])/(constants[29]+states[16])
    rates[15] = (constants[24]*states[14]-constants[25]*states[15])-(constants[26]*states[15]-constants[27]*states[7]*states[16])
    rates[16] = (constants[26]*states[15]-constants[27]*states[7]*states[16])-(constants[28]*states[16])/(constants[29]+states[16])
    rates[18] = -((constants[31]*states[12]*states[18])/(constants[32]+states[18]))+(constants[33]*states[17])/(constants[34]+states[17])
    rates[17] = (constants[31]*states[12]*states[18])/(constants[32]+states[18])-(constants[33]*states[17])/(constants[34]+states[17])
    rates[21] = (constants[37]*(states[19]+constants[39])*states[20])/(constants[38]+states[20])-(constants[35]*states[17]*states[21])/(constants[36]+states[21])
    rates[20] = -((constants[37]*(states[19]+constants[39])*states[20])/(constants[38]+states[20]))+(constants[35]*states[17]*states[21])/(constants[36]+states[21])
    rates[24] = (constants[42]*states[25])/(constants[43]+states[25])-(constants[40]*states[16]*states[24])/(constants[41]+states[24])
    rates[25] = (-((constants[42]*states[25])/(constants[43]+states[25]))+(constants[40]*states[16]*states[24])/(constants[41]+states[24]))-(constants[44]*states[25]*states[26]-constants[45]*states[27])
    rates[26] = -(constants[44]*states[25]*states[26]-constants[45]*states[27])
    rates[27] = ((constants[44]*states[25]*states[26]-constants[45]*states[27])-(constants[46]*states[27])/(constants[47]*(constants[57]+states[28]/constants[51])+states[27]))+(constants[48]*constants[56]*states[28])/(constants[49]*(constants[57]+states[22]/constants[54]+states[23]/constants[55]+states[19]/constants[53])+states[28])
    rates[28] = (((constants[46]*states[27])/(constants[47]*(constants[57]+states[28]/constants[51])+states[27])-(constants[48]*constants[56]*states[28])/(constants[49]*(constants[57]+states[22]/constants[54]+states[23]/constants[55]+states[19]/constants[53])+states[28]))-(constants[50]*states[28])/(constants[51]*(constants[57]+states[27]/constants[47])+states[28]))+(constants[52]*constants[56]*states[19])/(constants[53]*(constants[57]+states[22]/constants[54]+states[23]/constants[55]+states[28]/constants[49])+states[19])
    rates[19] = (constants[50]*states[28])/(constants[51]*(constants[57]+states[27]/constants[47])+states[28])-(constants[52]*constants[56]*states[19])/(constants[53]*(constants[57]+states[22]/constants[54]+states[23]/constants[55]+states[28]/constants[49])+states[19])
    rates[29] = -((constants[59]*states[20]*states[29])/(constants[60]*(constants[69]+states[22]/constants[64])+states[29]))+(constants[61]*constants[58]*states[22])/(constants[62]*(constants[69]+states[23]/constants[66]+states[28]/constants[67]+states[19]/constants[68])+states[22])
    rates[22] = (((constants[59]*states[20]*states[29])/(constants[60]*(constants[69]+states[22]/constants[64])+states[29])-(constants[61]*constants[58]*states[22])/(constants[62]*(constants[69]+states[23]/constants[66]+states[28]/constants[67]+states[19]/constants[68])+states[22]))-(constants[63]*states[20]*states[22])/(constants[64]*(constants[69]+states[29]/constants[60])+states[22]))+(constants[65]*constants[58]*states[23])/(constants[66]*(constants[69]+states[22]/constants[62]+states[28]/constants[67]+states[19]/constants[68])+states[23])
    rates[23] = (constants[63]*states[20]*states[22])/(constants[64]*(constants[69]+states[29]/constants[60])+states[22])-(constants[65]*constants[58]*states[23])/(constants[66]*(constants[69]+states[22]/constants[62]+states[28]/constants[67]+states[19]/constants[68])+states[23])
    rates[30] = -((constants[71]*states[23]*states[30])/(constants[72]*(constants[79]+states[31]/constants[76])+states[30]))+(constants[73]*constants[70]*states[31])/(constants[74]*(constants[79]+states[32]/constants[78])+states[31])
    rates[32] = (constants[75]*states[23]*states[31])/(constants[76]*(constants[79]+states[30]/constants[72])+states[31])-(constants[77]*constants[70]*states[32])/(constants[78]*(constants[79]+states[31]/constants[74])+states[32])
    rates[31] = (((constants[71]*states[23]*states[30])/(constants[72]*(constants[79]+states[31]/constants[76])+states[30])-(constants[73]*constants[70]*states[31])/(constants[74]*(constants[79]+states[32]/constants[78])+states[31]))-(constants[75]*states[23]*states[31])/(constants[76]*(constants[79]+states[30]/constants[72])+states[31]))+(constants[77]*constants[70]*states[32])/(constants[78]*(constants[79]+states[31]/constants[74])+states[32])
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
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
        self.kf1 = 0.0012
        self.kb1 = 0.00076
        self.kf2 = 0.01
        self.kb2 = 0.1
        self.kf3 = 1
        self.kb3 = 0.01
        self.kf34 = 0.001
        self.kb34 = 0
        self.V4 = 62.5
        self.k4 = 50
        self.kf5 = 0.1
        self.kb5 = 1
        self.kf6 = 20
        self.kb6 = 5
        self.kf7 = 60
        self.kb7 = 546
        self.kf8 = 2040
        self.kb8 = 15700
        self.kf9 = 40.8
        self.kb9 = 0
        self.V10 = 0.0154
        self.k10 = 340
        self.kf23 = 0.1
        self.kb23 = 2
        self.kf24 = 9.85
        self.kb24 = 0.0985
        self.kf25 = 45.8
        self.kb25 = 0.047
        self.V26 = 2620
        self.k26 = 3680
        self.two = 2
        self.kf11 = 0.222
        self.k11 = 0.181
        self.V12 = 0.289
        self.k12 = 0.0571
        self.kf13 = 1.53
        self.k13 = 11.7
        self.kf14 = 0.00673
        self.k14 = 8.07
        self.E = 7
        self.kf27 = 16.9
        self.k27 = 39.1
        self.V28 = 17000
        self.k28 = 9.02
        self.kf29 = 507
        self.kb29 = 234
        self.V30 = 20000
        self.k30 = 80000
        self.kf31 = 0.107
        self.k31 = 4.35
        self.V32 = 20000
        self.k32 = 80000
        self.kf33 = 0.211
        self.k33 = 12
        self.k16 = 2200
        self.k18 = 60
        self.PP2A = 11.4
        self.one = 1
        self.PP2A_1 = 11.4
        self.kf15 = 3.5
        self.k15 = 317
        self.kf16 = 0.058
        self.k16_1 = 2200
        self.kf17 = 2.9
        self.k17 = 317
        self.kf18 = 0.058
        self.k18_1 = 60
        self.k31_1 = 4.35
        self.k33_1 = 12
        self.one_1 = 1
        self.MKP3 = 2.4
        self.kf19 = 9.5
        self.k19 = 146000
        self.kf20 = 0.3
        self.k20 = 160
        self.kf21 = 16
        self.k21 = 146000
        self.kf22 = 0.27
        self.k22 = 60
        self.one_2 = 1

    def to_dict(self):
        return {
            "kf1": self.kf1,
            "kb1": self.kb1,
            "kf2": self.kf2,
            "kb2": self.kb2,
            "kf3": self.kf3,
            "kb3": self.kb3,
            "kf34": self.kf34,
            "kb34": self.kb34,
            "V4": self.V4,
            "k4": self.k4,
            "kf5": self.kf5,
            "kb5": self.kb5,
            "kf6": self.kf6,
            "kb6": self.kb6,
            "kf7": self.kf7,
            "kb7": self.kb7,
            "kf8": self.kf8,
            "kb8": self.kb8,
            "kf9": self.kf9,
            "kb9": self.kb9,
            "V10": self.V10,
            "k10": self.k10,
            "kf23": self.kf23,
            "kb23": self.kb23,
            "kf24": self.kf24,
            "kb24": self.kb24,
            "kf25": self.kf25,
            "kb25": self.kb25,
            "V26": self.V26,
            "k26": self.k26,
            "two": self.two,
            "kf11": self.kf11,
            "k11": self.k11,
            "V12": self.V12,
            "k12": self.k12,
            "kf13": self.kf13,
            "k13": self.k13,
            "kf14": self.kf14,
            "k14": self.k14,
            "E": self.E,
            "kf27": self.kf27,
            "k27": self.k27,
            "V28": self.V28,
            "k28": self.k28,
            "kf29": self.kf29,
            "kb29": self.kb29,
            "V30": self.V30,
            "k30": self.k30,
            "kf31": self.kf31,
            "k31": self.k31,
            "V32": self.V32,
            "k32": self.k32,
            "kf33": self.kf33,
            "k33": self.k33,
            "k16": self.k16,
            "k18": self.k18,
            "PP2A": self.PP2A,
            "one": self.one,
            "PP2A_1": self.PP2A_1,
            "kf15": self.kf15,
            "k15": self.k15,
            "kf16": self.kf16,
            "k16_1": self.k16_1,
            "kf17": self.kf17,
            "k17": self.k17,
            "kf18": self.kf18,
            "k18_1": self.k18_1,
            "k31_1": self.k31_1,
            "k33_1": self.k33_1,
            "one_1": self.one_1,
            "MKP3": self.MKP3,
            "kf19": self.kf19,
            "k19": self.k19,
            "kf20": self.kf20,
            "k20": self.k20,
            "kf21": self.kf21,
            "k21": self.k21,
            "kf22": self.kf22,
            "k22": self.k22,
            "one_2": self.one_2,
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
        y0=[80, 1000, 10, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 120, 0.0, 100, 0, 0, 0, 800, 0, 10, 0, 0, 120, 1000, 0, 0],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "hatakeyama_kimura_naka_kawasaki_yumoto_ichikawa_kim_saito_saeki_shirouzu_yokoyama_konagaya_2003"
        self.curve_names = [
            "R",
            "Shc",
            "PI3K",
            "HRG",
            "R_HRG",
            "R_HRG2",
            "Internalisation",
            "RP",
            "R_Shc",
            "R_ShP",
            "ShP",
            "R_ShGS",
            "ShGS",
            "GS",
            "R_PI3K",
            "R_PI3Kstar",
            "PI3Kstar",
            "RasGTP",
            "RasGDP",
            "Akt_PIPP",
            "RAF_star",
            "RAF",
            "MEKP",
            "MEKPP",
            "P",
            "PIP3",
            "Akt",
            "Akt_PIP3",
            "Akt_PIP",
            "MEK",
            "ERK",
            "ERKP",
            "ERKPP",
        ]
        self.state_names = ['R', 'Shc', 'PI3K', 'HRG', 'R_HRG', 'R_HRG2', 'Internalisation', 'RP', 'R_Shc', 'R_ShP', 'ShP', 'R_ShGS', 'ShGS', 'GS', 'R_PI3K', 'R_PI3Kstar', 'PI3Kstar', 'RasGTP', 'RasGDP', 'Akt_PIPP', 'RAF_star', 'RAF', 'MEKP', 'MEKPP', 'P', 'PIP3', 'Akt', 'Akt_PIP3', 'Akt_PIP', 'MEK', 'ERK', 'ERKP', 'ERKPP']
        self.algebraic_names = []
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 80
        p = self.params

        # direct mapping
        c[0] = p.kf1
        c[1] = p.kb1
        c[2] = p.kf2
        c[3] = p.kb2
        c[4] = p.kf3
        c[5] = p.kb3
        c[6] = p.kf34
        c[7] = p.kb34
        c[8] = p.V4
        c[9] = p.k4
        c[10] = p.kf5
        c[11] = p.kb5
        c[12] = p.kf6
        c[13] = p.kb6
        c[14] = p.kf7
        c[15] = p.kb7
        c[16] = p.kf8
        c[17] = p.kb8
        c[18] = p.kf9
        c[19] = p.kb9
        c[20] = p.V10
        c[21] = p.k10
        c[22] = p.kf23
        c[23] = p.kb23
        c[24] = p.kf24
        c[25] = p.kb24
        c[26] = p.kf25
        c[27] = p.kb25
        c[28] = p.V26
        c[29] = p.k26
        c[30] = p.two
        c[31] = p.kf11
        c[32] = p.k11
        c[33] = p.V12
        c[34] = p.k12
        c[35] = p.kf13
        c[36] = p.k13
        c[37] = p.kf14
        c[38] = p.k14
        c[39] = p.E
        c[40] = p.kf27
        c[41] = p.k27
        c[42] = p.V28
        c[43] = p.k28
        c[44] = p.kf29
        c[45] = p.kb29
        c[46] = p.V30
        c[47] = p.k30
        c[48] = p.kf31
        c[49] = p.k31
        c[50] = p.V32
        c[51] = p.k32
        c[52] = p.kf33
        c[53] = p.k33
        c[54] = p.k16
        c[55] = p.k18
        c[56] = p.PP2A
        c[57] = p.one
        c[58] = p.PP2A_1
        c[59] = p.kf15
        c[60] = p.k15
        c[61] = p.kf16
        c[62] = p.k16_1
        c[63] = p.kf17
        c[64] = p.k17
        c[65] = p.kf18
        c[66] = p.k18_1
        c[67] = p.k31_1
        c[68] = p.k33_1
        c[69] = p.one_1
        c[70] = p.MKP3
        c[71] = p.kf19
        c[72] = p.k19
        c[73] = p.kf20
        c[74] = p.k20
        c[75] = p.kf21
        c[76] = p.k21
        c[77] = p.kf22
        c[78] = p.k22
        c[79] = p.one_2

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
