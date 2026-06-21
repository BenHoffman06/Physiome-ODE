# Size of variable arrays:
sizeAlgebraic = 15
sizeStates = 7
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
    legend_constants[0] = "cap in component parameters (nanofarad)"
    legend_constants[1] = "cc1lin in component parameters (per_second)"
    legend_constants[2] = "cc_2 in component parameters (per_second)"
    legend_constants[3] = "ck1lin in component parameters (per_second)"
    legend_constants[4] = "ck_2 in component parameters (per_second)"
    legend_constants[5] = "clmax in component parameters (nanosiemens)"
    legend_constants[6] = "cnmax in component parameters (nanosiemens)"
    legend_constants[7] = "cx1lin in component parameters (per_second)"
    legend_constants[8] = "cx2 in component parameters (per_second)"
    legend_constants[9] = "ef in component parameters (per_second)"
    legend_constants[10] = "gl in component parameters (nanosiemens)"
    legend_constants[11] = "hmc_1 in component parameters (uM)"
    legend_constants[12] = "hmc_2 in component parameters (uM)"
    legend_constants[13] = "inf in component parameters (uM_per_picocoulomb)"
    legend_constants[14] = "inhmax in component parameters (dimensionless)"
    legend_constants[15] = "k_1 in component parameters (per_uM_per_second)"
    legend_constants[16] = "k_2 in component parameters (per_second)"
    legend_constants[17] = "kI in component parameters (uM)"
    legend_constants[18] = "kinh in component parameters (uM)"
    legend_constants[19] = "kinhcng in component parameters (uM)"
    legend_constants[20] = "n_1 in component parameters (dimensionless)"
    legend_constants[21] = "n_2 in component parameters (dimensionless)"
    legend_constants[22] = "nI in component parameters (dimensionless)"
    legend_constants[23] = "ninh in component parameters (dimensionless)"
    legend_constants[24] = "ninhcng in component parameters (dimensionless)"
    legend_constants[25] = "pd in component parameters (per_second)"
    legend_constants[26] = "r_1 in component parameters (per_second)"
    legend_constants[27] = "r_2 in component parameters (per_second)"
    legend_constants[28] = "smax in component parameters (uM_per_second)"
    legend_constants[29] = "V_Cl in component parameters (millivolt)"
    legend_constants[30] = "V_cng in component parameters (millivolt)"
    legend_constants[31] = "V_l in component parameters (millivolt)"
    legend_constants[39] = "F_vol in component parameters (picocoulomb_per_uM)"
    legend_constants[32] = "F in component parameters (coulombs_per_mole)"
    legend_constants[33] = "C_vol in component parameters (liter)"
    legend_algebraic[9] = "O_stim in component O_stim (uM)"
    legend_constants[34] = "od in component O_stim (uM)"
    legend_constants[35] = "t_0 in component O_stim (second)"
    legend_constants[36] = "t_1 in component O_stim (second)"
    legend_algebraic[0] = "H_0 in component O_stim (dimensionless)"
    legend_algebraic[5] = "H_1 in component O_stim (dimensionless)"
    legend_states[0] = "bLR in component bLR (dimensionless)"
    legend_constants[37] = "R_tot in component bLR (dimensionless)"
    legend_states[1] = "aG in component aG (dimensionless)"
    legend_constants[38] = "G_tot in component aG (dimensionless)"
    legend_algebraic[1] = "k_G in component k_G (per_second)"
    legend_algebraic[6] = "r_G in component r_G (per_second)"
    legend_states[2] = "cAMP in component cAMP (uM)"
    legend_algebraic[2] = "synth in component synth (uM_per_second)"
    legend_algebraic[7] = "degrad in component degrad (uM_per_second)"
    legend_states[3] = "aCaMK in component aCaMK (uM)"
    legend_states[4] = "Ca in component Ca (uM)"
    legend_algebraic[10] = "I_CNG in component I_CNG (nanoampere)"
    legend_algebraic[12] = "J_NCX in component J_NCX (uM_per_second)"
    legend_algebraic[3] = "cc_1 in component cc_1 (uM_per_second)"
    legend_states[5] = "CaCaM in component CaCaM (uM)"
    legend_algebraic[4] = "ck_1 in component ck_1 (uM_per_second)"
    legend_states[6] = "V in component V (millivolt)"
    legend_algebraic[11] = "I_ClCa in component I_ClCa (nanoampere)"
    legend_algebraic[13] = "I_NCX in component I_NCX (nanoampere)"
    legend_algebraic[14] = "I_other in component I_other (nanoampere)"
    legend_algebraic[8] = "inhcng in component inhcng (dimensionless)"
    legend_rates[0] = "d/dt bLR in component bLR (dimensionless)"
    legend_rates[1] = "d/dt aG in component aG (dimensionless)"
    legend_rates[2] = "d/dt cAMP in component cAMP (uM)"
    legend_rates[4] = "d/dt Ca in component Ca (uM)"
    legend_rates[5] = "d/dt CaCaM in component CaCaM (uM)"
    legend_rates[3] = "d/dt aCaMK in component aCaMK (uM)"
    legend_rates[6] = "d/dt V in component V (millivolt)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    constants[0] = 0.004
    constants[1] = 0.88
    constants[2] = 26
    constants[3] = 13
    constants[4] = 0.9
    constants[5] = 1
    constants[6] = 1
    constants[7] = 1
    constants[8] = 13
    constants[9] = 2
    constants[10] = 6
    constants[11] = 2
    constants[12] = 3
    constants[13] = 1.9
    constants[14] = 5
    constants[15] = 0.06
    constants[16] = 20
    constants[17] = 0.7
    constants[18] = 2
    constants[19] = 1
    constants[20] = 2
    constants[21] = 2
    constants[22] = 2
    constants[23] = 1.5
    constants[24] = 1.3
    constants[25] = 20
    constants[26] = 10
    constants[27] = 5
    constants[28] = 71
    constants[29] = -50
    constants[30] = 0
    constants[31] = -70
    constants[32] = 9.649e4
    constants[33] = 1e-13
    constants[34] = 20
    constants[35] = 0.5
    constants[36] = 1.5
    states[0] = 0
    constants[37] = 1
    states[1] = 0
    constants[38] = 1
    states[2] = 1.35648992164649e-88
    states[3] = 6.60756525051462e-8
    states[4] = 5.09073088043779e-12
    states[5] = 1.86113118246926e-13
    states[6] = -70
    constants[39] = (1.00000e+12/1.00000)*(1.00000/1000.00)*constants[32]*constants[33]
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[3] = constants[1]*states[4]
    rates[5] = algebraic[3]-constants[2]*states[5]
    algebraic[4] = constants[3]*states[5]
    rates[3] = algebraic[4]-constants[4]*states[3]
    algebraic[1] = constants[16]*states[0]
    algebraic[6] = constants[27]*states[1]
    rates[1] = algebraic[1]*(constants[38]-states[1])-algebraic[6]
    algebraic[2] = (states[1]*constants[28])/(1.00000+power(states[3]/constants[18], constants[23]))
    algebraic[7] = constants[25]*states[2]
    rates[2] = algebraic[2]-algebraic[7]
    algebraic[0] = custom_piecewise([less(voi , constants[35]), 0.00000 , True, 1.00000])
    algebraic[5] = custom_piecewise([less(voi , constants[36]), 0.00000 , True, 1.00000])
    algebraic[9] = constants[34]*(algebraic[0]-algebraic[5])
    rates[0] = constants[15]*algebraic[9]*(constants[37]-states[0])-constants[26]*states[0]
    algebraic[8] = 1.00000+((constants[14]-1.00000)*(power(states[5], constants[24])))/(power(states[5], constants[24])+power(constants[19], constants[24]))
    algebraic[10] = ((constants[6]*(power(states[2], constants[20])))/(power(states[2], constants[20])+power(algebraic[8]*constants[11], constants[20])))*(1.00000/1000.00)*(constants[30]-states[6])
    algebraic[12] = constants[9]*states[4]
    rates[4] = ((1000.00/1.00000)*constants[13]*algebraic[10]-algebraic[12])-(algebraic[3]-constants[2]*states[5])
    algebraic[11] = ((constants[5]*(power(states[4], constants[21])))/(power(states[4], constants[21])+power(constants[12], constants[21])))*(1.00000/1000.00)*(constants[29]-states[6])
    algebraic[13] = (1.00000/1000.00)*constants[39]*algebraic[12]
    algebraic[14] = constants[10]*(1.00000/1000.00)*(constants[31]-states[6])
    rates[6] = (1000.00/1.00000)*(1.00000/constants[0])*(algebraic[10]+algebraic[11]+algebraic[13]+algebraic[14])
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[3] = constants[1]*states[4]
    algebraic[4] = constants[3]*states[5]
    algebraic[1] = constants[16]*states[0]
    algebraic[6] = constants[27]*states[1]
    algebraic[2] = (states[1]*constants[28])/(1.00000+power(states[3]/constants[18], constants[23]))
    algebraic[7] = constants[25]*states[2]
    algebraic[0] = custom_piecewise([less(voi , constants[35]), 0.00000 , True, 1.00000])
    algebraic[5] = custom_piecewise([less(voi , constants[36]), 0.00000 , True, 1.00000])
    algebraic[9] = constants[34]*(algebraic[0]-algebraic[5])
    algebraic[8] = 1.00000+((constants[14]-1.00000)*(power(states[5], constants[24])))/(power(states[5], constants[24])+power(constants[19], constants[24]))
    algebraic[10] = ((constants[6]*(power(states[2], constants[20])))/(power(states[2], constants[20])+power(algebraic[8]*constants[11], constants[20])))*(1.00000/1000.00)*(constants[30]-states[6])
    algebraic[12] = constants[9]*states[4]
    algebraic[11] = ((constants[5]*(power(states[4], constants[21])))/(power(states[4], constants[21])+power(constants[12], constants[21])))*(1.00000/1000.00)*(constants[29]-states[6])
    algebraic[13] = (1.00000/1000.00)*constants[39]*algebraic[12]
    algebraic[14] = constants[10]*(1.00000/1000.00)*(constants[31]-states[6])
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
        self.cap = 0.004
        self.cc1lin = 0.88
        self.cc_2 = 26
        self.ck1lin = 13
        self.ck_2 = 0.9
        self.clmax = 1
        self.cnmax = 1
        self.cx1lin = 1
        self.cx2 = 13
        self.ef = 2
        self.gl = 6
        self.hmc_1 = 2
        self.hmc_2 = 3
        self.inf = 1.9
        self.inhmax = 5
        self.k_1 = 0.06
        self.k_2 = 20
        self.kI = 0.7
        self.kinh = 2
        self.kinhcng = 1
        self.n_1 = 2
        self.n_2 = 2
        self.nI = 2
        self.ninh = 1.5
        self.ninhcng = 1.3
        self.pd = 20
        self.r_1 = 10
        self.r_2 = 5
        self.smax = 71
        self.V_Cl = -50
        self.V_cng = 0
        self.V_l = -70
        self.F = 9.649e4
        self.C_vol = 1e-13
        self.od = 20
        self.t_0 = 0.5
        self.t_1 = 1.5
        self.R_tot = 1
        self.G_tot = 1

    def to_dict(self):
        return {
            "cap": self.cap,
            "cc1lin": self.cc1lin,
            "cc_2": self.cc_2,
            "ck1lin": self.ck1lin,
            "ck_2": self.ck_2,
            "clmax": self.clmax,
            "cnmax": self.cnmax,
            "cx1lin": self.cx1lin,
            "cx2": self.cx2,
            "ef": self.ef,
            "gl": self.gl,
            "hmc_1": self.hmc_1,
            "hmc_2": self.hmc_2,
            "inf": self.inf,
            "inhmax": self.inhmax,
            "k_1": self.k_1,
            "k_2": self.k_2,
            "kI": self.kI,
            "kinh": self.kinh,
            "kinhcng": self.kinhcng,
            "n_1": self.n_1,
            "n_2": self.n_2,
            "nI": self.nI,
            "ninh": self.ninh,
            "ninhcng": self.ninhcng,
            "pd": self.pd,
            "r_1": self.r_1,
            "r_2": self.r_2,
            "smax": self.smax,
            "V_Cl": self.V_Cl,
            "V_cng": self.V_cng,
            "V_l": self.V_l,
            "F": self.F,
            "C_vol": self.C_vol,
            "od": self.od,
            "t_0": self.t_0,
            "t_1": self.t_1,
            "R_tot": self.R_tot,
            "G_tot": self.G_tot,
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
        y0=[0, 0, 1.35648992164649e-88, 6.60756525051462e-8, 5.09073088043779e-12, 1.86113118246926e-13, -70],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "dougherty_wright_yew_2005"
        self.curve_names = [
            "bLR",
            "aG",
            "cAMP",
            "aCaMK",
            "Ca",
            "CaCaM",
            "V",
        ]
        self.state_names = ['bLR', 'aG', 'cAMP', 'aCaMK', 'Ca', 'CaCaM', 'V']
        self.algebraic_names = ['H_0', 'k_G', 'synth', 'cc_1', 'ck_1', 'H_1', 'r_G', 'degrad', 'inhcng', 'O_stim', 'I_CNG', 'I_ClCa', 'J_NCX', 'I_NCX', 'I_other']
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
        c[0] = p.cap
        c[1] = p.cc1lin
        c[2] = p.cc_2
        c[3] = p.ck1lin
        c[4] = p.ck_2
        c[5] = p.clmax
        c[6] = p.cnmax
        c[7] = p.cx1lin
        c[8] = p.cx2
        c[9] = p.ef
        c[10] = p.gl
        c[11] = p.hmc_1
        c[12] = p.hmc_2
        c[13] = p.inf
        c[14] = p.inhmax
        c[15] = p.k_1
        c[16] = p.k_2
        c[17] = p.kI
        c[18] = p.kinh
        c[19] = p.kinhcng
        c[20] = p.n_1
        c[21] = p.n_2
        c[22] = p.nI
        c[23] = p.ninh
        c[24] = p.ninhcng
        c[25] = p.pd
        c[26] = p.r_1
        c[27] = p.r_2
        c[28] = p.smax
        c[29] = p.V_Cl
        c[30] = p.V_cng
        c[31] = p.V_l
        c[32] = p.F
        c[33] = p.C_vol
        c[34] = p.od
        c[35] = p.t_0
        c[36] = p.t_1
        c[37] = p.R_tot
        c[38] = p.G_tot

        # derived constants
        c[39] = (1.00000e+12/1.00000)*(1.00000/1000.00)*c[32]*c[33]

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
