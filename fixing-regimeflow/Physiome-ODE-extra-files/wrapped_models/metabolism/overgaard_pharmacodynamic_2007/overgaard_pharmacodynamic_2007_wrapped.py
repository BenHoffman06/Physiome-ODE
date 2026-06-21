# Size of variable arrays:
sizeAlgebraic = 16
sizeStates = 3
sizeConstants = 37
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (hour)"
    legend_constants[0] = "T_a in component model_parameters (celsius)"
    legend_constants[1] = "T_b in component model_parameters (celsius)"
    legend_constants[2] = "delta_T in component model_parameters (celsius)"
    legend_constants[3] = "kinc in component model_parameters (W_per_kg_C2)"
    legend_constants[4] = "tdose1 in component model_parameters (hour)"
    legend_constants[5] = "tdose2 in component model_parameters (hour)"
    legend_constants[6] = "tdose3 in component model_parameters (hour)"
    legend_algebraic[5] = "M_c in component M_c (W_per_kg)"
    legend_constants[7] = "t_day in component M_c (hour)"
    legend_constants[8] = "t_night in component M_c (hour)"
    legend_algebraic[1] = "tprime in component M_c (second)"
    legend_constants[9] = "day_length in component M_c (second)"
    legend_constants[35] = "M_day in component M_day (W_per_kg)"
    legend_algebraic[3] = "M_night in component M_night (W_per_kg)"
    legend_states[0] = "M in component M (W_per_kg)"
    legend_constants[10] = "km in component M (per_hour)"
    legend_states[1] = "T in component T (celsius)"
    legend_constants[11] = "c in component T (kJ_per_kg_C)"
    legend_algebraic[0] = "k in component k (W_per_kg_C)"
    legend_states[2] = "BR in component k (dimensionless)"
    legend_constants[12] = "pEtot in component k (dimensionless)"
    legend_constants[13] = "kR in component k (per_day)"
    legend_constants[14] = "AMT_dose in component k (mg_per_kg)"
    legend_constants[15] = "pEf1 in component k (per_day)"
    legend_constants[16] = "pEs1 in component k (kg_per_day_mg)"
    legend_constants[17] = "pEf2 in component k (per_day)"
    legend_constants[18] = "pEs2 in component k (kg_per_day_mg)"
    legend_constants[19] = "pEf3 in component k (per_day)"
    legend_constants[20] = "pEs3 in component k (kg_per_day_mg)"
    legend_algebraic[13] = "E_slow in component k (per_day)"
    legend_algebraic[15] = "E_fast in component k (per_day)"
    legend_constants[30] = "f2_drug in component k (W_per_kg_C)"
    legend_constants[34] = "kb in component kb (W_per_kg_C)"
    legend_algebraic[2] = "f_prime in component M_night (dimensionless)"
    legend_algebraic[6] = "gNsTs1 in component gNT (dimensionless)"
    legend_algebraic[9] = "gNsTs2 in component gNT (dimensionless)"
    legend_algebraic[12] = "gNsTs3 in component gNT (dimensionless)"
    legend_algebraic[7] = "gNfTf1 in component gNT (dimensionless)"
    legend_algebraic[10] = "gNfTf2 in component gNT (dimensionless)"
    legend_algebraic[14] = "gNfTf3 in component gNT (dimensionless)"
    legend_constants[29] = "T_day in component T_day (celsius)"
    legend_constants[32] = "T_night in component T_night (celsius)"
    legend_constants[21] = "M_b in component kb (W_per_kg)"
    legend_constants[22] = "t_prime in component M_night (hour)"
    legend_constants[23] = "alpha in component M_night (per_hour)"
    legend_constants[24] = "delta_high_dose in component M_night (dimensionless)"
    legend_constants[36] = "M_night_baseline in component M_night (W_per_kg)"
    legend_constants[25] = "Ns in component gNT (dimensionless)"
    legend_constants[26] = "Nf in component gNT (dimensionless)"
    legend_constants[27] = "Ts in component gNT (day)"
    legend_constants[28] = "Tf in component gNT (day)"
    legend_algebraic[4] = "X1 in component gNT (day)"
    legend_algebraic[8] = "X2 in component gNT (day)"
    legend_algebraic[11] = "X3 in component gNT (day)"
    legend_constants[31] = "Kf in component gNT (per_day)"
    legend_constants[33] = "Ks in component gNT (per_day)"
    legend_rates[0] = "d/dt M in component M (W_per_kg)"
    legend_rates[1] = "d/dt T in component T (celsius)"
    legend_rates[2] = "d/dt BR in component k (dimensionless)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    constants[0] = 21.0
    constants[1] = 38.0
    constants[2] = 1.57
    constants[3] = 0.0258
    constants[4] = 24.0
    constants[5] = 72.0
    constants[6] = 120.0
    constants[7] = 17.5
    constants[8] = 6.73
    constants[9] = 86400
    states[0] = 3.5
    constants[10] = 1.1375
    states[1] = 38.785
    constants[11] = 3.47
    states[2] = 0.0
    constants[12] = 0.144
    constants[13] = 5.35
    constants[14] = 3.0
    constants[15] = 1.0
    constants[16] = 0.2
    constants[17] = 3.57
    constants[18] = 2.43
    constants[19] = 8.0
    constants[20] = 50.0
    constants[21] = 3.0
    constants[22] = 45.12
    constants[23] = 0.2229166
    constants[24] = 1.0
    constants[25] = 4.0
    constants[26] = 4.0
    constants[27] = 2.45
    constants[28] = 0.368
    constants[29] = constants[1]+constants[2]/2.00000
    constants[30] = 0.00000
    constants[31] = constants[26]/constants[28]
    constants[32] = constants[1]-constants[2]/2.00000
    constants[33] = constants[25]/constants[27]
    constants[34] = constants[21]/(constants[1]-constants[0])
    constants[35] = (constants[34]+constants[3]*(constants[29]-constants[1]))*(constants[29]-constants[0])
    constants[36] = (constants[34]+constants[3]*(constants[32]-constants[1]))*(constants[32]-constants[0])
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[0] = constants[34]+constants[3]*(states[1]-constants[1]*(1.00000+constants[12]*states[2]))+constants[30]
    rates[1] = (power(constants[11], -1.00000))*(states[0]-algebraic[0]*(states[1]-constants[0]))
    algebraic[1] =  voi*3600.00*1.00000 % constants[9]
    algebraic[2] = constants[24]*(power(1.00000+exp(-constants[23]*(voi-(constants[4]+constants[22]))), -1.00000))
    algebraic[3] = (1.00000-algebraic[2])*constants[36]+algebraic[2]*constants[35]
    algebraic[5] = custom_piecewise([greater_equal(algebraic[1]/3600.00 , constants[8]) & less(algebraic[1]/3600.00 , constants[7]), algebraic[3] , True, constants[35]])
    rates[0] = -constants[10]*(states[0]-algebraic[5])
    algebraic[4] = (voi-constants[4])/24.0000
    algebraic[6] = custom_piecewise([greater(algebraic[4] , 0.00000), ((power(constants[33], constants[25]))/6.00000)*exp(-constants[33]*algebraic[4])*(power(algebraic[4], constants[25]-1.00000)) , True, 0.00000])
    algebraic[8] = (voi-constants[5])/24.0000
    algebraic[9] = custom_piecewise([greater(algebraic[8] , 0.00000), ((power(constants[33], constants[25]))/6.00000)*exp(-constants[33]*algebraic[8])*(power(algebraic[8], constants[25]-1.00000)) , True, 0.00000])
    algebraic[11] = (voi-constants[6])/24.0000
    algebraic[12] = custom_piecewise([greater(algebraic[11] , 0.00000), ((power(constants[33], constants[25]))/6.00000)*exp(-constants[33]*algebraic[11])*(power(algebraic[11], constants[25]-1.00000)) , True, 0.00000])
    algebraic[13] = constants[14]*constants[18]*(algebraic[6]+algebraic[9]+algebraic[12])
    algebraic[7] = custom_piecewise([greater(algebraic[4] , 0.00000), ((power(constants[31], constants[26]))/6.00000)*exp(-constants[31]*algebraic[4])*(power(algebraic[4], constants[26]-1.00000)) , True, 0.00000])
    algebraic[10] = custom_piecewise([greater(algebraic[8] , 0.00000), ((power(constants[31], constants[26]))/6.00000)*exp(-constants[31]*algebraic[8])*(power(algebraic[8], constants[26]-1.00000)) , True, 0.00000])
    algebraic[14] = custom_piecewise([greater(algebraic[11] , 0.00000), ((power(constants[31], constants[26]))/6.00000)*exp(-constants[31]*algebraic[11])*(power(algebraic[11], constants[26]-1.00000)) , True, 0.00000])
    algebraic[15] = constants[17]*(algebraic[7]+algebraic[10]+algebraic[14])
    rates[2] = (algebraic[2]*(algebraic[13]+algebraic[15]))*(1.00000-states[2])-constants[13]*states[2]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = constants[34]+constants[3]*(states[1]-constants[1]*(1.00000+constants[12]*states[2]))+constants[30]
    algebraic[1] =  voi*3600.00*1.00000 % constants[9]
    algebraic[2] = constants[24]*(power(1.00000+exp(-constants[23]*(voi-(constants[4]+constants[22]))), -1.00000))
    algebraic[3] = (1.00000-algebraic[2])*constants[36]+algebraic[2]*constants[35]
    algebraic[5] = custom_piecewise([greater_equal(algebraic[1]/3600.00 , constants[8]) & less(algebraic[1]/3600.00 , constants[7]), algebraic[3] , True, constants[35]])
    algebraic[4] = (voi-constants[4])/24.0000
    algebraic[6] = custom_piecewise([greater(algebraic[4] , 0.00000), ((power(constants[33], constants[25]))/6.00000)*exp(-constants[33]*algebraic[4])*(power(algebraic[4], constants[25]-1.00000)) , True, 0.00000])
    algebraic[8] = (voi-constants[5])/24.0000
    algebraic[9] = custom_piecewise([greater(algebraic[8] , 0.00000), ((power(constants[33], constants[25]))/6.00000)*exp(-constants[33]*algebraic[8])*(power(algebraic[8], constants[25]-1.00000)) , True, 0.00000])
    algebraic[11] = (voi-constants[6])/24.0000
    algebraic[12] = custom_piecewise([greater(algebraic[11] , 0.00000), ((power(constants[33], constants[25]))/6.00000)*exp(-constants[33]*algebraic[11])*(power(algebraic[11], constants[25]-1.00000)) , True, 0.00000])
    algebraic[13] = constants[14]*constants[18]*(algebraic[6]+algebraic[9]+algebraic[12])
    algebraic[7] = custom_piecewise([greater(algebraic[4] , 0.00000), ((power(constants[31], constants[26]))/6.00000)*exp(-constants[31]*algebraic[4])*(power(algebraic[4], constants[26]-1.00000)) , True, 0.00000])
    algebraic[10] = custom_piecewise([greater(algebraic[8] , 0.00000), ((power(constants[31], constants[26]))/6.00000)*exp(-constants[31]*algebraic[8])*(power(algebraic[8], constants[26]-1.00000)) , True, 0.00000])
    algebraic[14] = custom_piecewise([greater(algebraic[11] , 0.00000), ((power(constants[31], constants[26]))/6.00000)*exp(-constants[31]*algebraic[11])*(power(algebraic[11], constants[26]-1.00000)) , True, 0.00000])
    algebraic[15] = constants[17]*(algebraic[7]+algebraic[10]+algebraic[14])
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
        self.T_a = 21.0
        self.T_b = 38.0
        self.delta_T = 1.57
        self.kinc = 0.0258
        self.tdose1 = 24.0
        self.tdose2 = 72.0
        self.tdose3 = 120.0
        self.t_day = 17.5
        self.t_night = 6.73
        self.day_length = 86400
        self.km = 1.1375
        self.c = 3.47
        self.pEtot = 0.144
        self.kR = 5.35
        self.AMT_dose = 3.0
        self.pEf1 = 1.0
        self.pEs1 = 0.2
        self.pEf2 = 3.57
        self.pEs2 = 2.43
        self.pEf3 = 8.0
        self.pEs3 = 50.0
        self.M_b = 3.0
        self.t_prime = 45.12
        self.alpha = 0.2229166
        self.delta_high_dose = 1.0
        self.Ns = 4.0
        self.Nf = 4.0
        self.Ts = 2.45
        self.Tf = 0.368
        self.f2_drug = 0.00000

    def to_dict(self):
        return {
            "T_a": self.T_a,
            "T_b": self.T_b,
            "delta_T": self.delta_T,
            "kinc": self.kinc,
            "tdose1": self.tdose1,
            "tdose2": self.tdose2,
            "tdose3": self.tdose3,
            "t_day": self.t_day,
            "t_night": self.t_night,
            "day_length": self.day_length,
            "km": self.km,
            "c": self.c,
            "pEtot": self.pEtot,
            "kR": self.kR,
            "AMT_dose": self.AMT_dose,
            "pEf1": self.pEf1,
            "pEs1": self.pEs1,
            "pEf2": self.pEf2,
            "pEs2": self.pEs2,
            "pEf3": self.pEf3,
            "pEs3": self.pEs3,
            "M_b": self.M_b,
            "t_prime": self.t_prime,
            "alpha": self.alpha,
            "delta_high_dose": self.delta_high_dose,
            "Ns": self.Ns,
            "Nf": self.Nf,
            "Ts": self.Ts,
            "Tf": self.Tf,
            "f2_drug": self.f2_drug,
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
        y0=[3.5, 38.785, 0.0],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "overgaard_pharmacodynamic_2007"
        self.curve_names = [
            "M",
            "T",
            "BR",
        ]
        self.state_names = ['M', 'T', 'BR']
        self.algebraic_names = ['k', 'tprime', 'f_prime', 'M_night', 'X1', 'M_c', 'gNsTs1', 'gNfTf1', 'X2', 'gNsTs2', 'gNfTf2', 'X3', 'gNsTs3', 'E_slow', 'gNfTf3', 'E_fast']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 37
        p = self.params

        # direct mapping
        c[0] = p.T_a
        c[1] = p.T_b
        c[2] = p.delta_T
        c[3] = p.kinc
        c[4] = p.tdose1
        c[5] = p.tdose2
        c[6] = p.tdose3
        c[7] = p.t_day
        c[8] = p.t_night
        c[9] = p.day_length
        c[10] = p.km
        c[11] = p.c
        c[12] = p.pEtot
        c[13] = p.kR
        c[14] = p.AMT_dose
        c[15] = p.pEf1
        c[16] = p.pEs1
        c[17] = p.pEf2
        c[18] = p.pEs2
        c[19] = p.pEf3
        c[20] = p.pEs3
        c[21] = p.M_b
        c[22] = p.t_prime
        c[23] = p.alpha
        c[24] = p.delta_high_dose
        c[25] = p.Ns
        c[26] = p.Nf
        c[27] = p.Ts
        c[28] = p.Tf
        c[30] = p.f2_drug

        # derived constants
        c[29] = c[1]+c[2]/2.00000
        c[31] = c[26]/c[28]
        c[32] = c[1]-c[2]/2.00000
        c[33] = c[25]/c[27]
        c[34] = c[21]/(c[1]-c[0])
        c[35] = (c[34]+c[3]*(c[29]-c[1]))*(c[29]-c[0])
        c[36] = (c[34]+c[3]*(c[32]-c[1]))*(c[32]-c[0])

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
