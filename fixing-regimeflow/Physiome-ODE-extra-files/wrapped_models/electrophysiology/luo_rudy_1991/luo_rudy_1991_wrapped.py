# Size of variable arrays:
sizeAlgebraic = 25
sizeStates = 8
sizeConstants = 24
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (millisecond)"
    legend_states[0] = "V in component membrane (millivolt)"
    legend_constants[0] = "R in component membrane (joule_per_kilomole_kelvin)"
    legend_constants[1] = "T in component membrane (kelvin)"
    legend_constants[2] = "F in component membrane (coulomb_per_mole)"
    legend_constants[3] = "C in component membrane (microF_per_cm2)"
    legend_algebraic[0] = "I_stim in component membrane (microA_per_cm2)"
    legend_algebraic[7] = "i_Na in component fast_sodium_current (microA_per_cm2)"
    legend_algebraic[15] = "i_si in component slow_inward_current (microA_per_cm2)"
    legend_algebraic[17] = "i_K in component time_dependent_potassium_current (microA_per_cm2)"
    legend_algebraic[21] = "i_K1 in component time_independent_potassium_current (microA_per_cm2)"
    legend_algebraic[23] = "i_Kp in component plateau_potassium_current (microA_per_cm2)"
    legend_algebraic[24] = "i_b in component background_current (microA_per_cm2)"
    legend_constants[4] = "stim_start in component membrane (millisecond)"
    legend_constants[5] = "stim_end in component membrane (millisecond)"
    legend_constants[6] = "stim_period in component membrane (millisecond)"
    legend_constants[7] = "stim_duration in component membrane (millisecond)"
    legend_constants[8] = "stim_amplitude in component membrane (microA_per_cm2)"
    legend_constants[9] = "g_Na in component fast_sodium_current (milliS_per_cm2)"
    legend_constants[18] = "E_Na in component fast_sodium_current (millivolt)"
    legend_constants[10] = "Nao in component ionic_concentrations (millimolar)"
    legend_constants[11] = "Nai in component ionic_concentrations (millimolar)"
    legend_states[1] = "m in component fast_sodium_current_m_gate (dimensionless)"
    legend_states[2] = "h in component fast_sodium_current_h_gate (dimensionless)"
    legend_states[3] = "j in component fast_sodium_current_j_gate (dimensionless)"
    legend_algebraic[1] = "alpha_m in component fast_sodium_current_m_gate (per_millisecond)"
    legend_algebraic[8] = "beta_m in component fast_sodium_current_m_gate (per_millisecond)"
    legend_algebraic[2] = "alpha_h in component fast_sodium_current_h_gate (per_millisecond)"
    legend_algebraic[9] = "beta_h in component fast_sodium_current_h_gate (per_millisecond)"
    legend_algebraic[3] = "alpha_j in component fast_sodium_current_j_gate (per_millisecond)"
    legend_algebraic[10] = "beta_j in component fast_sodium_current_j_gate (per_millisecond)"
    legend_algebraic[14] = "E_si in component slow_inward_current (millivolt)"
    legend_states[4] = "Cai in component intracellular_calcium_concentration (millimolar)"
    legend_states[5] = "d in component slow_inward_current_d_gate (dimensionless)"
    legend_states[6] = "f in component slow_inward_current_f_gate (dimensionless)"
    legend_algebraic[4] = "alpha_d in component slow_inward_current_d_gate (per_millisecond)"
    legend_algebraic[11] = "beta_d in component slow_inward_current_d_gate (per_millisecond)"
    legend_algebraic[5] = "alpha_f in component slow_inward_current_f_gate (per_millisecond)"
    legend_algebraic[12] = "beta_f in component slow_inward_current_f_gate (per_millisecond)"
    legend_constants[19] = "g_K in component time_dependent_potassium_current (milliS_per_cm2)"
    legend_constants[20] = "E_K in component time_dependent_potassium_current (millivolt)"
    legend_constants[12] = "PR_NaK in component time_dependent_potassium_current (dimensionless)"
    legend_constants[13] = "Ko in component ionic_concentrations (millimolar)"
    legend_constants[14] = "Ki in component ionic_concentrations (millimolar)"
    legend_states[7] = "X in component time_dependent_potassium_current_X_gate (dimensionless)"
    legend_algebraic[16] = "Xi in component time_dependent_potassium_current_Xi_gate (dimensionless)"
    legend_algebraic[6] = "alpha_X in component time_dependent_potassium_current_X_gate (per_millisecond)"
    legend_algebraic[13] = "beta_X in component time_dependent_potassium_current_X_gate (per_millisecond)"
    legend_constants[21] = "E_K1 in component time_independent_potassium_current (millivolt)"
    legend_constants[22] = "g_K1 in component time_independent_potassium_current (milliS_per_cm2)"
    legend_algebraic[20] = "K1_infinity in component time_independent_potassium_current_K1_gate (dimensionless)"
    legend_algebraic[18] = "alpha_K1 in component time_independent_potassium_current_K1_gate (per_millisecond)"
    legend_algebraic[19] = "beta_K1 in component time_independent_potassium_current_K1_gate (per_millisecond)"
    legend_constants[23] = "E_Kp in component plateau_potassium_current (millivolt)"
    legend_constants[15] = "g_Kp in component plateau_potassium_current (milliS_per_cm2)"
    legend_algebraic[22] = "Kp in component plateau_potassium_current (dimensionless)"
    legend_constants[16] = "E_b in component background_current (millivolt)"
    legend_constants[17] = "g_b in component background_current (milliS_per_cm2)"
    legend_rates[0] = "d/dt V in component membrane (millivolt)"
    legend_rates[1] = "d/dt m in component fast_sodium_current_m_gate (dimensionless)"
    legend_rates[2] = "d/dt h in component fast_sodium_current_h_gate (dimensionless)"
    legend_rates[3] = "d/dt j in component fast_sodium_current_j_gate (dimensionless)"
    legend_rates[5] = "d/dt d in component slow_inward_current_d_gate (dimensionless)"
    legend_rates[6] = "d/dt f in component slow_inward_current_f_gate (dimensionless)"
    legend_rates[7] = "d/dt X in component time_dependent_potassium_current_X_gate (dimensionless)"
    legend_rates[4] = "d/dt Cai in component intracellular_calcium_concentration (millimolar)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = -84.3801107371
    constants[0] = 8314
    constants[1] = 310
    constants[2] = 96484.6
    constants[3] = 1
    constants[4] = 100
    constants[5] = 9000
    constants[6] = 1000
    constants[7] = 2
    constants[8] = -25.5
    constants[9] = 23
    constants[10] = 140
    constants[11] = 18
    states[1] = 0.00171338077730188
    states[2] = 0.982660523699656
    states[3] = 0.989108212766685
    states[4] = 0.00017948816388306
    states[5] = 0.00302126301779861
    states[6] = 0.999967936476325
    constants[12] = 0.01833
    constants[13] = 5.4
    constants[14] = 145
    states[7] = 0.0417603108167287
    constants[15] = 0.0183
    constants[16] = -59.87
    constants[17] = 0.03921
    constants[18] = ((constants[0]*constants[1])/constants[2])*log(constants[10]/constants[11])
    constants[19] = 0.282000*(power(constants[13]/5.40000, 1.0/2))
    constants[20] = ((constants[0]*constants[1])/constants[2])*log((constants[13]+constants[12]*constants[10])/(constants[14]+constants[12]*constants[11]))
    constants[21] = ((constants[0]*constants[1])/constants[2])*log(constants[13]/constants[14])
    constants[22] = 0.604700*(power(constants[13]/5.40000, 1.0/2))
    constants[23] = constants[21]
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[1] = (0.320000*(states[0]+47.1300))/(1.00000-exp(-0.100000*(states[0]+47.1300)))
    algebraic[8] = 0.0800000*exp(-states[0]/11.0000)
    rates[1] = algebraic[1]*(1.00000-states[1])-algebraic[8]*states[1]
    algebraic[2] = custom_piecewise([less(states[0] , -40.0000), 0.135000*exp((80.0000+states[0])/-6.80000) , True, 0.00000])
    algebraic[9] = custom_piecewise([less(states[0] , -40.0000), 3.56000*exp(0.0790000*states[0])+310000.*exp(0.350000*states[0]) , True, 1.00000/(0.130000*(1.00000+exp((states[0]+10.6600)/-11.1000)))])
    rates[2] = algebraic[2]*(1.00000-states[2])-algebraic[9]*states[2]
    algebraic[3] = custom_piecewise([less(states[0] , -40.0000), ((-127140.*exp(0.244400*states[0])-3.47400e-05*exp(-0.0439100*states[0]))*(states[0]+37.7800))/(1.00000+exp(0.311000*(states[0]+79.2300))) , True, 0.00000])
    algebraic[10] = custom_piecewise([less(states[0] , -40.0000), (0.121200*exp(-0.0105200*states[0]))/(1.00000+exp(-0.137800*(states[0]+40.1400))) , True, (0.300000*exp(-2.53500e-07*states[0]))/(1.00000+exp(-0.100000*(states[0]+32.0000)))])
    rates[3] = algebraic[3]*(1.00000-states[3])-algebraic[10]*states[3]
    algebraic[4] = (0.0950000*exp(-0.0100000*(states[0]-5.00000)))/(1.00000+exp(-0.0720000*(states[0]-5.00000)))
    algebraic[11] = (0.0700000*exp(-0.0170000*(states[0]+44.0000)))/(1.00000+exp(0.0500000*(states[0]+44.0000)))
    rates[5] = algebraic[4]*(1.00000-states[5])-algebraic[11]*states[5]
    algebraic[5] = (0.0120000*exp(-0.00800000*(states[0]+28.0000)))/(1.00000+exp(0.150000*(states[0]+28.0000)))
    algebraic[12] = (0.00650000*exp(-0.0200000*(states[0]+30.0000)))/(1.00000+exp(-0.200000*(states[0]+30.0000)))
    rates[6] = algebraic[5]*(1.00000-states[6])-algebraic[12]*states[6]
    algebraic[6] = (0.000500000*exp(0.0830000*(states[0]+50.0000)))/(1.00000+exp(0.0570000*(states[0]+50.0000)))
    algebraic[13] = (0.00130000*exp(-0.0600000*(states[0]+20.0000)))/(1.00000+exp(-0.0400000*(states[0]+20.0000)))
    rates[7] = algebraic[6]*(1.00000-states[7])-algebraic[13]*states[7]
    algebraic[14] = 7.70000-13.0287*log(states[4]/1.00000)
    algebraic[15] = 0.0900000*states[5]*states[6]*(states[0]-algebraic[14])
    rates[4] = (-0.000100000/1.00000)*algebraic[15]+0.0700000*(0.000100000-states[4])
    algebraic[0] = custom_piecewise([greater_equal(voi , constants[4]) & less_equal(voi , constants[5]) & less_equal((voi-constants[4])-floor((voi-constants[4])/constants[6])*constants[6] , constants[7]), constants[8] , True, 0.00000])
    algebraic[7] = constants[9]*(power(states[1], 3.00000))*states[2]*states[3]*(states[0]-constants[18])
    algebraic[16] = custom_piecewise([greater(states[0] , -100.000), (2.83700*(exp(0.0400000*(states[0]+77.0000))-1.00000))/((states[0]+77.0000)*exp(0.0400000*(states[0]+35.0000))) , True, 1.00000])
    algebraic[17] = constants[19]*states[7]*algebraic[16]*(states[0]-constants[20])
    algebraic[18] = 1.02000/(1.00000+exp(0.238500*((states[0]-constants[21])-59.2150)))
    algebraic[19] = (0.491240*exp(0.0803200*((states[0]+5.47600)-constants[21]))+1.00000*exp(0.0617500*(states[0]-(constants[21]+594.310))))/(1.00000+exp(-0.514300*((states[0]-constants[21])+4.75300)))
    algebraic[20] = algebraic[18]/(algebraic[18]+algebraic[19])
    algebraic[21] = constants[22]*algebraic[20]*(states[0]-constants[21])
    algebraic[22] = 1.00000/(1.00000+exp((7.48800-states[0])/5.98000))
    algebraic[23] = constants[15]*algebraic[22]*(states[0]-constants[23])
    algebraic[24] = constants[17]*(states[0]-constants[16])
    rates[0] = (-1.00000/constants[3])*(algebraic[0]+algebraic[7]+algebraic[15]+algebraic[17]+algebraic[21]+algebraic[23]+algebraic[24])
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[1] = (0.320000*(states[0]+47.1300))/(1.00000-exp(-0.100000*(states[0]+47.1300)))
    algebraic[8] = 0.0800000*exp(-states[0]/11.0000)
    algebraic[2] = custom_piecewise([less(states[0] , -40.0000), 0.135000*exp((80.0000+states[0])/-6.80000) , True, 0.00000])
    algebraic[9] = custom_piecewise([less(states[0] , -40.0000), 3.56000*exp(0.0790000*states[0])+310000.*exp(0.350000*states[0]) , True, 1.00000/(0.130000*(1.00000+exp((states[0]+10.6600)/-11.1000)))])
    algebraic[3] = custom_piecewise([less(states[0] , -40.0000), ((-127140.*exp(0.244400*states[0])-3.47400e-05*exp(-0.0439100*states[0]))*(states[0]+37.7800))/(1.00000+exp(0.311000*(states[0]+79.2300))) , True, 0.00000])
    algebraic[10] = custom_piecewise([less(states[0] , -40.0000), (0.121200*exp(-0.0105200*states[0]))/(1.00000+exp(-0.137800*(states[0]+40.1400))) , True, (0.300000*exp(-2.53500e-07*states[0]))/(1.00000+exp(-0.100000*(states[0]+32.0000)))])
    algebraic[4] = (0.0950000*exp(-0.0100000*(states[0]-5.00000)))/(1.00000+exp(-0.0720000*(states[0]-5.00000)))
    algebraic[11] = (0.0700000*exp(-0.0170000*(states[0]+44.0000)))/(1.00000+exp(0.0500000*(states[0]+44.0000)))
    algebraic[5] = (0.0120000*exp(-0.00800000*(states[0]+28.0000)))/(1.00000+exp(0.150000*(states[0]+28.0000)))
    algebraic[12] = (0.00650000*exp(-0.0200000*(states[0]+30.0000)))/(1.00000+exp(-0.200000*(states[0]+30.0000)))
    algebraic[6] = (0.000500000*exp(0.0830000*(states[0]+50.0000)))/(1.00000+exp(0.0570000*(states[0]+50.0000)))
    algebraic[13] = (0.00130000*exp(-0.0600000*(states[0]+20.0000)))/(1.00000+exp(-0.0400000*(states[0]+20.0000)))
    algebraic[14] = 7.70000-13.0287*log(states[4]/1.00000)
    algebraic[15] = 0.0900000*states[5]*states[6]*(states[0]-algebraic[14])
    algebraic[0] = custom_piecewise([greater_equal(voi , constants[4]) & less_equal(voi , constants[5]) & less_equal((voi-constants[4])-floor((voi-constants[4])/constants[6])*constants[6] , constants[7]), constants[8] , True, 0.00000])
    algebraic[7] = constants[9]*(power(states[1], 3.00000))*states[2]*states[3]*(states[0]-constants[18])
    algebraic[16] = custom_piecewise([greater(states[0] , -100.000), (2.83700*(exp(0.0400000*(states[0]+77.0000))-1.00000))/((states[0]+77.0000)*exp(0.0400000*(states[0]+35.0000))) , True, 1.00000])
    algebraic[17] = constants[19]*states[7]*algebraic[16]*(states[0]-constants[20])
    algebraic[18] = 1.02000/(1.00000+exp(0.238500*((states[0]-constants[21])-59.2150)))
    algebraic[19] = (0.491240*exp(0.0803200*((states[0]+5.47600)-constants[21]))+1.00000*exp(0.0617500*(states[0]-(constants[21]+594.310))))/(1.00000+exp(-0.514300*((states[0]-constants[21])+4.75300)))
    algebraic[20] = algebraic[18]/(algebraic[18]+algebraic[19])
    algebraic[21] = constants[22]*algebraic[20]*(states[0]-constants[21])
    algebraic[22] = 1.00000/(1.00000+exp((7.48800-states[0])/5.98000))
    algebraic[23] = constants[15]*algebraic[22]*(states[0]-constants[23])
    algebraic[24] = constants[17]*(states[0]-constants[16])
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
        self.R = 8314
        self.T = 310
        self.F = 96484.6
        self.C = 1
        self.stim_start = 100
        self.stim_end = 9000
        self.stim_period = 1000
        self.stim_duration = 2
        self.stim_amplitude = -25.5
        self.g_Na = 23
        self.Nao = 140
        self.Nai = 18
        self.PR_NaK = 0.01833
        self.Ko = 5.4
        self.Ki = 145
        self.g_Kp = 0.0183
        self.E_b = -59.87
        self.g_b = 0.03921

    def to_dict(self):
        return {
            "R": self.R,
            "T": self.T,
            "F": self.F,
            "C": self.C,
            "stim_start": self.stim_start,
            "stim_end": self.stim_end,
            "stim_period": self.stim_period,
            "stim_duration": self.stim_duration,
            "stim_amplitude": self.stim_amplitude,
            "g_Na": self.g_Na,
            "Nao": self.Nao,
            "Nai": self.Nai,
            "PR_NaK": self.PR_NaK,
            "Ko": self.Ko,
            "Ki": self.Ki,
            "g_Kp": self.g_Kp,
            "E_b": self.E_b,
            "g_b": self.g_b,
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
        y0=[-84.3801107371, 0.00171338077730188, 0.982660523699656, 0.989108212766685, 0.00017948816388306, 0.00302126301779861, 0.999967936476325, 0.0417603108167287],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "luo_rudy_1991"
        self.curve_names = [
            "V",
            "m",
            "h",
            "j",
            "Cai",
            "d",
            "f",
            "X",
        ]
        self.state_names = ['V', 'm', 'h', 'j', 'Cai', 'd', 'f', 'X']
        self.algebraic_names = ['I_stim', 'alpha_m', 'alpha_h', 'alpha_j', 'alpha_d', 'alpha_f', 'alpha_X', 'i_Na', 'beta_m', 'beta_h', 'beta_j', 'beta_d', 'beta_f', 'beta_X', 'E_si', 'i_si', 'Xi', 'i_K', 'alpha_K1', 'beta_K1', 'K1_infinity', 'i_K1', 'Kp', 'i_Kp', 'i_b']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 24
        p = self.params

        # direct mapping
        c[0] = p.R
        c[1] = p.T
        c[2] = p.F
        c[3] = p.C
        c[4] = p.stim_start
        c[5] = p.stim_end
        c[6] = p.stim_period
        c[7] = p.stim_duration
        c[8] = p.stim_amplitude
        c[9] = p.g_Na
        c[10] = p.Nao
        c[11] = p.Nai
        c[12] = p.PR_NaK
        c[13] = p.Ko
        c[14] = p.Ki
        c[15] = p.g_Kp
        c[16] = p.E_b
        c[17] = p.g_b

        # derived constants
        c[18] = ((c[0]*c[1])/c[2])*log(c[10]/c[11])
        c[19] = 0.282000*(power(c[13]/5.40000, 1.0/2))
        c[20] = ((c[0]*c[1])/c[2])*log((c[13]+c[12]*c[10])/(c[14]+c[12]*c[11]))
        c[21] = ((c[0]*c[1])/c[2])*log(c[13]/c[14])
        c[22] = 0.604700*(power(c[13]/5.40000, 1.0/2))
        c[23] = c[21]

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
