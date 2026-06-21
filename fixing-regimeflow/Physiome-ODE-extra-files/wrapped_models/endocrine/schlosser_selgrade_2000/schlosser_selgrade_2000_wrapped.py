# Size of variable arrays:
sizeAlgebraic = 12
sizeStates = 4
sizeConstants = 20
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (day)"
    legend_algebraic[6] = "rel_LH_E2_P4_RP_LH in component RP_LH (microg_day)"
    legend_states[0] = "RP_LH in component RP_LH (microg)"
    legend_algebraic[10] = "syn_LH_E2_P4 in component RP_LH (microg_day)"
    legend_constants[0] = "V0_LH in component RP_LH (microg_day)"
    legend_constants[1] = "V1_LH in component RP_LH (microg_day)"
    legend_constants[2] = "h in component RP_LH (dimensionless)"
    legend_constants[3] = "Km_LH in component RP_LH (ng_L)"
    legend_constants[4] = "Ki_LHP in component RP_LH (nmol_L)"
    legend_constants[5] = "kLH_rel in component RP_LH (first_order_rate_constant)"
    legend_constants[6] = "CLH_P in component RP_LH (L_nmol)"
    legend_constants[7] = "CLH_E in component RP_LH (L_ng)"
    legend_algebraic[3] = "E2 in component E2 (ng_L)"
    legend_algebraic[4] = "E2_dE in component E2_dE (ng_L)"
    legend_algebraic[5] = "P4 in component P4 (nmol_L)"
    legend_algebraic[8] = "P4_dP in component P4_dP (nmol_L)"
    legend_states[1] = "LH in component LH (microg_l)"
    legend_constants[8] = "v_dis in component LH (litre)"
    legend_algebraic[0] = "clear_LH in component LH (microg_l_day)"
    legend_constants[9] = "kLH_cl in component LH (first_order_rate_constant)"
    legend_algebraic[7] = "rel_FSH_E2_P4_RP_FSH in component RP_FSH (microg_day)"
    legend_states[2] = "RP_FSH in component RP_FSH (microg)"
    legend_algebraic[11] = "syn_FSH_Ih in component RP_FSH (microg_day)"
    legend_constants[10] = "V_FSH in component RP_FSH (microg_day)"
    legend_constants[11] = "Ki_FSH_Ih in component RP_FSH (U_L)"
    legend_constants[12] = "kFSH_rel in component RP_FSH (first_order_rate_constant)"
    legend_constants[13] = "CFSH_P in component RP_FSH (L_nmol)"
    legend_constants[14] = "CFSH_E in component RP_FSH (L_ng2)"
    legend_algebraic[9] = "Ih_dIh in component Ih_dIh (U_L)"
    legend_states[3] = "FSH in component FSH (microg_l)"
    legend_constants[15] = "v_dis in component FSH (litre)"
    legend_algebraic[2] = "clear_FSH in component FSH (microg_l_day)"
    legend_constants[16] = "kFSH_cl in component FSH (first_order_rate_constant)"
    legend_constants[17] = "dE in component E2_dE (day)"
    legend_constants[18] = "dP in component P4_dP (day)"
    legend_algebraic[1] = "Ih in component Ih (U_L)"
    legend_constants[19] = "dIh in component Ih_dIh (day)"
    legend_rates[0] = "d/dt RP_LH in component RP_LH (microg)"
    legend_rates[1] = "d/dt LH in component LH (microg_l)"
    legend_rates[2] = "d/dt RP_FSH in component RP_FSH (microg)"
    legend_rates[3] = "d/dt FSH in component FSH (microg_l)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 467.0
    constants[0] = 1400.0
    constants[1] = 95900.0
    constants[2] = 8.0
    constants[3] = 360.0
    constants[4] = 26.0
    constants[5] = 3.0
    constants[6] = 0.024
    constants[7] = 0.008
    states[1] = 40.0
    constants[8] = 2.5
    constants[9] = 14.0
    states[2] = 0.0
    constants[10] = 4400.0
    constants[11] = 1176.5
    constants[12] = 45.0
    constants[13] = 3.0
    constants[14] = 0.005
    states[3] = 150.0
    constants[15] = 2.5
    constants[16] = 8.21
    constants[17] = 0.42
    constants[18] = 2.9
    constants[19] = 2.0
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[3] = (300.000-(240.000*(power(voi+1.00000, 2.00000)))/(3.00000+power(voi+1.00000, 2.00000)))+90.0000*exp(-((power(voi-8.00000, 2.00000))/10.0000))
    algebraic[5] = 52.0000*exp(-((power(voi-7.00000, 2.00000))/18.0000))
    algebraic[6] = (constants[5]*(1.00000+constants[6]*algebraic[5])*states[0])/(1.00000+constants[7]*algebraic[3])
    algebraic[0] = constants[9]*states[1]
    rates[1] = algebraic[6]/constants[8]-algebraic[0]
    algebraic[7] = (constants[12]*(1.00000+constants[13]*algebraic[5])*states[2])/(1.00000+constants[14]*(power(algebraic[3], 2.00000)))
    algebraic[2] = constants[16]*states[3]
    rates[3] = algebraic[7]/constants[15]-algebraic[2]
    algebraic[4] = (300.000-(240.000*(power((voi+1.00000)-constants[17], 2.00000)))/(3.00000+power((voi+1.00000)-constants[17], 2.00000)))+90.0000*exp(-((power(voi-(constants[17]+8.00000), 2.00000))/10.0000))
    algebraic[8] = 52.0000*exp(-((power(voi-(constants[18]+7.00000), 2.00000))/18.0000))
    algebraic[10] = (constants[0]+(constants[1]*(power(algebraic[4], constants[2])))/(power(constants[3], constants[2])+power(algebraic[4], constants[2])))/(1.00000+algebraic[8]/constants[4])
    rates[0] = algebraic[10]-algebraic[6]
    algebraic[9] = 300.000+1330.00*exp(-((power(voi-(7.00000+constants[19]), 2.00000))/19.0000))
    algebraic[11] = constants[10]/(1.00000+algebraic[9]/constants[11])
    rates[2] = algebraic[11]-algebraic[7]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[3] = (300.000-(240.000*(power(voi+1.00000, 2.00000)))/(3.00000+power(voi+1.00000, 2.00000)))+90.0000*exp(-((power(voi-8.00000, 2.00000))/10.0000))
    algebraic[5] = 52.0000*exp(-((power(voi-7.00000, 2.00000))/18.0000))
    algebraic[6] = (constants[5]*(1.00000+constants[6]*algebraic[5])*states[0])/(1.00000+constants[7]*algebraic[3])
    algebraic[0] = constants[9]*states[1]
    algebraic[7] = (constants[12]*(1.00000+constants[13]*algebraic[5])*states[2])/(1.00000+constants[14]*(power(algebraic[3], 2.00000)))
    algebraic[2] = constants[16]*states[3]
    algebraic[4] = (300.000-(240.000*(power((voi+1.00000)-constants[17], 2.00000)))/(3.00000+power((voi+1.00000)-constants[17], 2.00000)))+90.0000*exp(-((power(voi-(constants[17]+8.00000), 2.00000))/10.0000))
    algebraic[8] = 52.0000*exp(-((power(voi-(constants[18]+7.00000), 2.00000))/18.0000))
    algebraic[10] = (constants[0]+(constants[1]*(power(algebraic[4], constants[2])))/(power(constants[3], constants[2])+power(algebraic[4], constants[2])))/(1.00000+algebraic[8]/constants[4])
    algebraic[9] = 300.000+1330.00*exp(-((power(voi-(7.00000+constants[19]), 2.00000))/19.0000))
    algebraic[11] = constants[10]/(1.00000+algebraic[9]/constants[11])
    algebraic[1] = 300.000+1330.00*exp(-((power(voi-7.00000, 2.00000))/19.0000))
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
        self.V0_LH = 1400.0
        self.V1_LH = 95900.0
        self.h = 8.0
        self.Km_LH = 360.0
        self.Ki_LHP = 26.0
        self.kLH_rel = 3.0
        self.CLH_P = 0.024
        self.CLH_E = 0.008
        self.v_dis = 2.5
        self.kLH_cl = 14.0
        self.V_FSH = 4400.0
        self.Ki_FSH_Ih = 1176.5
        self.kFSH_rel = 45.0
        self.CFSH_P = 3.0
        self.CFSH_E = 0.005
        self.v_dis_1 = 2.5
        self.kFSH_cl = 8.21
        self.dE = 0.42
        self.dP = 2.9
        self.dIh = 2.0

    def to_dict(self):
        return {
            "V0_LH": self.V0_LH,
            "V1_LH": self.V1_LH,
            "h": self.h,
            "Km_LH": self.Km_LH,
            "Ki_LHP": self.Ki_LHP,
            "kLH_rel": self.kLH_rel,
            "CLH_P": self.CLH_P,
            "CLH_E": self.CLH_E,
            "v_dis": self.v_dis,
            "kLH_cl": self.kLH_cl,
            "V_FSH": self.V_FSH,
            "Ki_FSH_Ih": self.Ki_FSH_Ih,
            "kFSH_rel": self.kFSH_rel,
            "CFSH_P": self.CFSH_P,
            "CFSH_E": self.CFSH_E,
            "v_dis_1": self.v_dis_1,
            "kFSH_cl": self.kFSH_cl,
            "dE": self.dE,
            "dP": self.dP,
            "dIh": self.dIh,
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
        y0=[467.0, 40.0, 0.0, 150.0],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "schlosser_selgrade_2000"
        self.curve_names = [
            "RP_LH",
            "LH",
            "RP_FSH",
            "FSH",
        ]
        self.state_names = ['RP_LH', 'LH', 'RP_FSH', 'FSH']
        self.algebraic_names = ['clear_LH', 'Ih', 'clear_FSH', 'E2', 'E2_dE', 'P4', 'rel_LH_E2_P4_RP_LH', 'rel_FSH_E2_P4_RP_FSH', 'P4_dP', 'Ih_dIh', 'syn_LH_E2_P4', 'syn_FSH_Ih']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 20
        p = self.params

        # direct mapping
        c[0] = p.V0_LH
        c[1] = p.V1_LH
        c[2] = p.h
        c[3] = p.Km_LH
        c[4] = p.Ki_LHP
        c[5] = p.kLH_rel
        c[6] = p.CLH_P
        c[7] = p.CLH_E
        c[8] = p.v_dis
        c[9] = p.kLH_cl
        c[10] = p.V_FSH
        c[11] = p.Ki_FSH_Ih
        c[12] = p.kFSH_rel
        c[13] = p.CFSH_P
        c[14] = p.CFSH_E
        c[15] = p.v_dis_1
        c[16] = p.kFSH_cl
        c[17] = p.dE
        c[18] = p.dP
        c[19] = p.dIh

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
