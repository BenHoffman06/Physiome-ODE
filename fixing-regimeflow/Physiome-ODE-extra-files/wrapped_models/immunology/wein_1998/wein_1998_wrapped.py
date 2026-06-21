# Size of variable arrays:
sizeAlgebraic = 0
sizeStates = 10
sizeConstants = 28
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (day)"
    legend_states[0] = "T in component uninfected_CD4 (cells_per_mm3)"
    legend_constants[0] = "s in component uninfected_CD4 (cells_per_mm3_day)"
    legend_constants[1] = "lambda in component uninfected_CD4 (per_day)"
    legend_states[1] = "T1_star in component productively_infected_CD4 (cells_per_mm3)"
    legend_states[2] = "T2_star in component productively_infected_CD4 (cells_per_mm3)"
    legend_constants[2] = "Tmax in component uninfected_CD4 (cells_per_mm3)"
    legend_constants[3] = "mu in component uninfected_CD4 (per_day)"
    legend_constants[4] = "k1 in component productively_infected_CD4 (ml_per_virons_day)"
    legend_constants[5] = "r1 in component drug_parameters (dimensionless)"
    legend_states[3] = "V1_I in component virus_strain1 (virons_per_ml)"
    legend_constants[6] = "k2 in component productively_infected_CD4 (ml_per_virons_day)"
    legend_constants[7] = "r2 in component drug_parameters (dimensionless)"
    legend_states[4] = "V2_I in component virus_strain2 (virons_per_ml)"
    legend_states[5] = "M in component uninfected_long_lived_cells (cells_per_mm3)"
    legend_constants[8] = "lambda_M in component uninfected_long_lived_cells (cells_per_mm3_day)"
    legend_constants[9] = "mu_M in component uninfected_long_lived_cells (per_day)"
    legend_constants[10] = "k1_M in component productively_infected_long_lived_cells (ml_per_virons_day)"
    legend_constants[11] = "k2_M in component productively_infected_long_lived_cells (ml_per_virons_day)"
    legend_constants[12] = "m11 in component productively_infected_CD4 (dimensionless)"
    legend_constants[13] = "m21 in component productively_infected_CD4 (dimensionless)"
    legend_constants[14] = "delta1 in component productively_infected_CD4 (per_day)"
    legend_constants[15] = "m22 in component productively_infected_CD4 (dimensionless)"
    legend_constants[16] = "m12 in component productively_infected_CD4 (dimensionless)"
    legend_constants[17] = "delta2 in component productively_infected_CD4 (per_day)"
    legend_states[6] = "M1_star in component productively_infected_long_lived_cells (cells_per_mm3)"
    legend_constants[18] = "delta1_M in component productively_infected_long_lived_cells (per_day)"
    legend_states[7] = "M2_star in component productively_infected_long_lived_cells (cells_per_mm3)"
    legend_constants[19] = "delta2_M in component productively_infected_long_lived_cells (per_day)"
    legend_constants[20] = "p1 in component drug_parameters (dimensionless)"
    legend_constants[21] = "N1 in component virus_strain1 (virons_per_cell)"
    legend_constants[22] = "N1_M in component virus_strain1 (virons_per_cell)"
    legend_states[8] = "V1 in component virus_strain1 (virons_per_ml)"
    legend_constants[23] = "c1 in component virus_strain1 (per_day)"
    legend_constants[24] = "p2 in component drug_parameters (dimensionless)"
    legend_constants[25] = "N2 in component virus_strain2 (virons_per_cell)"
    legend_constants[26] = "N2_M in component virus_strain2 (virons_per_cell)"
    legend_constants[27] = "c2 in component virus_strain2 (per_day)"
    legend_states[9] = "V2 in component virus_strain2 (virons_per_ml)"
    legend_rates[0] = "d/dt T in component uninfected_CD4 (cells_per_mm3)"
    legend_rates[5] = "d/dt M in component uninfected_long_lived_cells (cells_per_mm3)"
    legend_rates[1] = "d/dt T1_star in component productively_infected_CD4 (cells_per_mm3)"
    legend_rates[2] = "d/dt T2_star in component productively_infected_CD4 (cells_per_mm3)"
    legend_rates[6] = "d/dt M1_star in component productively_infected_long_lived_cells (cells_per_mm3)"
    legend_rates[7] = "d/dt M2_star in component productively_infected_long_lived_cells (cells_per_mm3)"
    legend_rates[3] = "d/dt V1_I in component virus_strain1 (virons_per_ml)"
    legend_rates[8] = "d/dt V1 in component virus_strain1 (virons_per_ml)"
    legend_rates[4] = "d/dt V2_I in component virus_strain2 (virons_per_ml)"
    legend_rates[9] = "d/dt V2 in component virus_strain2 (virons_per_ml)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 178.81
    constants[0] = 0
    constants[1] = 0.01
    states[1] = 1.19
    states[2] = 0.004
    constants[2] = 450
    constants[3] = 0.0014
    constants[4] = 3.43E-8
    constants[5] = 0.9
    states[3] = 133500
    constants[6] = 3.43E-8
    constants[7] = 0.25
    states[4] = 450
    states[5] = 49.2
    constants[8] = 2.0
    constants[9] = 0.04
    constants[10] = 4.67E-9
    constants[11] = 4.67E-9
    constants[12] = 1
    constants[13] = 3.4E-5
    constants[14] = 0.69
    constants[15] = 1
    constants[16] = 3.4E-5
    constants[17] = 0.69
    states[6] = 0.49
    constants[18] = 0.062
    states[7] = 1.7E-3
    constants[19] = 0.062
    constants[20] = 0.99
    constants[21] = 480.1
    constants[22] = 534.4
    states[8] = 133500
    constants[23] = 3.07
    constants[24] = 0.25
    constants[25] = 475.3
    constants[26] = 529.0
    constants[27] = 3.07
    states[9] = 450
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[0] = (((constants[0]+constants[1]*states[0]*(1.00000-(states[0]+states[1]+states[2])/constants[2]))-constants[3]*states[0])-constants[4]*(1.00000-constants[5])*states[0]*states[3])-constants[6]*(1.00000-constants[7])*states[0]*states[4]
    rates[5] = ((constants[8]-constants[9]*states[5])-constants[10]*(1.00000-constants[5])*states[5]*states[3])-constants[11]*(1.00000-constants[7])*states[5]*states[4]
    rates[1] = (constants[12]*constants[4]*(1.00000-constants[5])*states[0]*states[3]+constants[13]*constants[6]*(1.00000-constants[7])*states[0]*states[4])-constants[14]*states[1]
    rates[2] = (constants[15]*constants[6]*(1.00000-constants[7])*states[0]*states[4]+constants[16]*constants[4]*(1.00000-constants[5])*states[0]*states[3])-constants[17]*states[2]
    rates[6] = (constants[12]*constants[10]*(1.00000-constants[5])*states[5]*states[3]+constants[13]*constants[11]*(1.00000-constants[7])*states[5]*states[4])-constants[18]*states[6]
    rates[7] = (constants[15]*constants[11]*(1.00000-constants[7])*states[5]*states[4]+constants[16]*constants[10]*(1.00000-constants[5])*states[5]*states[3])-constants[19]*states[7]
    rates[3] = ((1.00000-constants[20])*constants[21]*constants[14]*states[1]+(1.00000-constants[20])*constants[22]*constants[18]*states[6])-constants[23]*states[3]
    rates[8] = (constants[21]*constants[14]*states[1]+constants[22]*constants[18]*states[6])-constants[23]*states[8]
    rates[4] = ((1.00000-constants[24])*constants[25]*constants[17]*states[2]+(1.00000-constants[24])*constants[26]*constants[19]*states[7])-constants[27]*states[4]
    rates[9] = (constants[25]*constants[17]*states[2]+constants[26]*constants[19]*states[7])-constants[27]*states[9]
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
        self.s = 0
        self.lambda = 0.01
        self.Tmax = 450
        self.mu = 0.0014
        self.k1 = 3.43E-8
        self.r1 = 0.9
        self.k2 = 3.43E-8
        self.r2 = 0.25
        self.lambda_M = 2.0
        self.mu_M = 0.04
        self.k1_M = 4.67E-9
        self.k2_M = 4.67E-9
        self.m11 = 1
        self.m21 = 3.4E-5
        self.delta1 = 0.69
        self.m22 = 1
        self.m12 = 3.4E-5
        self.delta2 = 0.69
        self.delta1_M = 0.062
        self.delta2_M = 0.062
        self.p1 = 0.99
        self.N1 = 480.1
        self.N1_M = 534.4
        self.c1 = 3.07
        self.p2 = 0.25
        self.N2 = 475.3
        self.N2_M = 529.0
        self.c2 = 3.07

    def to_dict(self):
        return {
            "s": self.s,
            "lambda": self.lambda,
            "Tmax": self.Tmax,
            "mu": self.mu,
            "k1": self.k1,
            "r1": self.r1,
            "k2": self.k2,
            "r2": self.r2,
            "lambda_M": self.lambda_M,
            "mu_M": self.mu_M,
            "k1_M": self.k1_M,
            "k2_M": self.k2_M,
            "m11": self.m11,
            "m21": self.m21,
            "delta1": self.delta1,
            "m22": self.m22,
            "m12": self.m12,
            "delta2": self.delta2,
            "delta1_M": self.delta1_M,
            "delta2_M": self.delta2_M,
            "p1": self.p1,
            "N1": self.N1,
            "N1_M": self.N1_M,
            "c1": self.c1,
            "p2": self.p2,
            "N2": self.N2,
            "N2_M": self.N2_M,
            "c2": self.c2,
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
        y0=[178.81, 1.19, 0.004, 133500, 450, 49.2, 0.49, 1.7E-3, 133500, 450],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "wein_1998"
        self.curve_names = [
            "T",
            "T1_star",
            "T2_star",
            "V1_I",
            "V2_I",
            "M",
            "M1_star",
            "M2_star",
            "V1",
            "V2",
        ]
        self.state_names = ['T', 'T1_star', 'T2_star', 'V1_I', 'V2_I', 'M', 'M1_star', 'M2_star', 'V1', 'V2']
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
        c = [0.0] * 28
        p = self.params

        # direct mapping
        c[0] = p.s
        c[1] = p.lambda
        c[2] = p.Tmax
        c[3] = p.mu
        c[4] = p.k1
        c[5] = p.r1
        c[6] = p.k2
        c[7] = p.r2
        c[8] = p.lambda_M
        c[9] = p.mu_M
        c[10] = p.k1_M
        c[11] = p.k2_M
        c[12] = p.m11
        c[13] = p.m21
        c[14] = p.delta1
        c[15] = p.m22
        c[16] = p.m12
        c[17] = p.delta2
        c[18] = p.delta1_M
        c[19] = p.delta2_M
        c[20] = p.p1
        c[21] = p.N1
        c[22] = p.N1_M
        c[23] = p.c1
        c[24] = p.p2
        c[25] = p.N2
        c[26] = p.N2_M
        c[27] = p.c2

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
