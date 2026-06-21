# Size of variable arrays:
sizeAlgebraic = 11
sizeStates = 2
sizeConstants = 11
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (minute)"
    legend_constants[0] = "VPF in component pulmonary_O2_uptake (litre)"
    legend_constants[1] = "DOB in component pulmonary_O2_uptake (mL_per_minute)"
    legend_constants[2] = "QRO in component pulmonary_O2_uptake (L_per_minute)"
    legend_constants[3] = "RMO in component pulmonary_O2_uptake (mL_per_minute)"
    legend_constants[4] = "HM in component pulmonary_O2_uptake (dimensionless)"
    legend_constants[9] = "O2UTIL in component total_O2_utilization (mL_per_minute)"
    legend_algebraic[5] = "O2VAD2 in component progressive_chemoreceptor_adaptation_of_alveolar_ventilation (dimensionless)"
    legend_algebraic[4] = "O2VTS2 in component acute_chemoreceptor_adaptation_of_alveolar_ventilation (dimensionless)"
    legend_algebraic[7] = "ALVENT in component alveolar_ventilation (L_per_minute)"
    legend_constants[5] = "VNTSTM in component parameter_values (dimensionless)"
    legend_algebraic[8] = "PO2ALV in component alveolar_PO2 (mmHg)"
    legend_constants[6] = "PO2AMB in component parameter_values (mmHg)"
    legend_algebraic[1] = "PO2ART in component arterial_PO2 (mmHg)"
    legend_algebraic[9] = "O2DFS in component respiratory_O2_diffusion_into_capillaries (mL_per_minute)"
    legend_constants[7] = "PL2 in component parameter_values (L_mL_per_minute_per_mmHg)"
    legend_constants[8] = "VPTISS in component parameter_values (litre)"
    legend_constants[10] = "RSPDFC in component respiratory_O2_diffusion_into_capillaries (mL_per_minute_per_mmHg)"
    legend_states[0] = "OVA in component O2_volume_of_arterial_blood (mL_per_L)"
    legend_algebraic[10] = "DOVA in component O2_volume_of_arterial_blood (mL_per_L_per_minute)"
    legend_algebraic[0] = "OSA in component arterial_PO2 (dimensionless)"
    legend_algebraic[3] = "O2VTST in component acute_chemoreceptor_adaptation_of_alveolar_ventilation (dimensionless)"
    legend_algebraic[2] = "O2VTST1 in component acute_chemoreceptor_adaptation_of_alveolar_ventilation (dimensionless)"
    legend_algebraic[6] = "DO2VAD in component progressive_chemoreceptor_adaptation_of_alveolar_ventilation (per_minute)"
    legend_states[1] = "O2VAD1 in component progressive_chemoreceptor_adaptation_of_alveolar_ventilation (dimensionless)"
    legend_rates[0] = "d/dt OVA in component O2_volume_of_arterial_blood (mL_per_L)"
    legend_rates[1] = "d/dt O2VAD1 in component progressive_chemoreceptor_adaptation_of_alveolar_ventilation (dimensionless)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    constants[0] = 0.0123238
    constants[1] = 163.508
    constants[2] = 4.97838
    constants[3] = 56.8057
    constants[4] = 40.0381
    constants[5] = 1
    constants[6] = 150
    constants[7] = 1.8
    constants[8] = 0.0175
    states[0] = 204.497
    states[1] = 2.368e-07
    constants[9] = constants[1]+constants[3]
    constants[10] = constants[7]/(constants[8]+constants[0])
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[0] = (states[0]/constants[4])/5.25000
    algebraic[1] = custom_piecewise([greater(algebraic[0] , 1.00000), 114.000+(algebraic[0]-1.00000)*6667.00 , greater(algebraic[0] , 0.936000) & less_equal(algebraic[0] , 1.00000), 74.0000+(algebraic[0]-0.936000)*625.000 , greater(algebraic[0] , 0.800000) & less_equal(algebraic[0] , 0.936000), 46.0000+(algebraic[0]-0.800000)*205.882 , True, algebraic[0]*57.5000])
    algebraic[2] = (algebraic[1]-67.0000)/30.0000
    algebraic[3] = custom_piecewise([greater(algebraic[2] , 1.00000), 1.00000 , less(algebraic[2] , 0.600000), 0.600000 , True, algebraic[2]])
    algebraic[4] = 1.00000/algebraic[3]
    algebraic[6] = ((algebraic[4]-1.00000)*3.00000-states[1])*0.000500000
    rates[1] = algebraic[6]
    algebraic[5] = states[1]+1.00000
    algebraic[7] = constants[9]*constants[5]*0.0266670*algebraic[4]*algebraic[5]
    algebraic[8] = constants[6]-(constants[9]/algebraic[7])/0.761000
    algebraic[9] = (algebraic[8]-algebraic[1])*constants[10]
    algebraic[10] = (algebraic[9]-constants[9])/(constants[2]*1.00000)
    rates[0] = algebraic[10]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = (states[0]/constants[4])/5.25000
    algebraic[1] = custom_piecewise([greater(algebraic[0] , 1.00000), 114.000+(algebraic[0]-1.00000)*6667.00 , greater(algebraic[0] , 0.936000) & less_equal(algebraic[0] , 1.00000), 74.0000+(algebraic[0]-0.936000)*625.000 , greater(algebraic[0] , 0.800000) & less_equal(algebraic[0] , 0.936000), 46.0000+(algebraic[0]-0.800000)*205.882 , True, algebraic[0]*57.5000])
    algebraic[2] = (algebraic[1]-67.0000)/30.0000
    algebraic[3] = custom_piecewise([greater(algebraic[2] , 1.00000), 1.00000 , less(algebraic[2] , 0.600000), 0.600000 , True, algebraic[2]])
    algebraic[4] = 1.00000/algebraic[3]
    algebraic[6] = ((algebraic[4]-1.00000)*3.00000-states[1])*0.000500000
    algebraic[5] = states[1]+1.00000
    algebraic[7] = constants[9]*constants[5]*0.0266670*algebraic[4]*algebraic[5]
    algebraic[8] = constants[6]-(constants[9]/algebraic[7])/0.761000
    algebraic[9] = (algebraic[8]-algebraic[1])*constants[10]
    algebraic[10] = (algebraic[9]-constants[9])/(constants[2]*1.00000)
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
        self.VPF = 0.0123238
        self.DOB = 163.508
        self.QRO = 4.97838
        self.RMO = 56.8057
        self.HM = 40.0381
        self.VNTSTM = 1
        self.PO2AMB = 150
        self.PL2 = 1.8
        self.VPTISS = 0.0175

    def to_dict(self):
        return {
            "VPF": self.VPF,
            "DOB": self.DOB,
            "QRO": self.QRO,
            "RMO": self.RMO,
            "HM": self.HM,
            "VNTSTM": self.VNTSTM,
            "PO2AMB": self.PO2AMB,
            "PL2": self.PL2,
            "VPTISS": self.VPTISS,
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
        y0=[204.497, 2.368e-07],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "guyton_pulmonary_oxygen_uptake_2008"
        self.curve_names = [
            "OVA",
            "O2VAD1",
        ]
        self.state_names = ['OVA', 'O2VAD1']
        self.algebraic_names = ['OSA', 'PO2ART', 'O2VTST1', 'O2VTST', 'O2VTS2', 'O2VAD2', 'DO2VAD', 'ALVENT', 'PO2ALV', 'O2DFS', 'DOVA']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 11
        p = self.params

        # direct mapping
        c[0] = p.VPF
        c[1] = p.DOB
        c[2] = p.QRO
        c[3] = p.RMO
        c[4] = p.HM
        c[5] = p.VNTSTM
        c[6] = p.PO2AMB
        c[7] = p.PL2
        c[8] = p.VPTISS

        # derived constants
        c[9] = c[1]+c[3]
        c[10] = c[7]/(c[8]+c[0])

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
