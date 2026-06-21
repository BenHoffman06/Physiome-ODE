# Size of variable arrays:
sizeAlgebraic = 15
sizeStates = 5
sizeConstants = 24
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (minute)"
    legend_states[0] = "y0 in component y0 (dimensionless)"
    legend_algebraic[10] = "g0 in component y0 (dimensionless)"
    legend_algebraic[5] = "r0 in component y0 (dimensionless)"
    legend_algebraic[0] = "h0 in component y0 (dimensionless)"
    legend_constants[0] = "S0 in component y0 (dimensionless)"
    legend_states[1] = "y2 in component y2 (dimensionless)"
    legend_constants[1] = "a00 in component model_parameters (dimensionless)"
    legend_constants[2] = "a02 in component model_parameters (dimensionless)"
    legend_constants[3] = "c0 in component model_parameters (first_order_rate_constant)"
    legend_constants[4] = "e0 in component model_parameters (first_order_rate_constant)"
    legend_constants[5] = "epsilon in component model_parameters (dimensionless)"
    legend_states[2] = "y1 in component y1 (dimensionless)"
    legend_algebraic[11] = "g1 in component y1 (dimensionless)"
    legend_algebraic[6] = "r1 in component y1 (dimensionless)"
    legend_algebraic[1] = "h1 in component y1 (dimensionless)"
    legend_constants[6] = "S1 in component y1 (dimensionless)"
    legend_constants[7] = "a10 in component model_parameters (dimensionless)"
    legend_constants[8] = "a12 in component model_parameters (dimensionless)"
    legend_constants[9] = "a11 in component model_parameters (dimensionless)"
    legend_constants[10] = "e1 in component model_parameters (first_order_rate_constant)"
    legend_algebraic[12] = "g2 in component y2 (dimensionless)"
    legend_algebraic[7] = "r2 in component y2 (dimensionless)"
    legend_algebraic[2] = "h2 in component y2 (dimensionless)"
    legend_constants[11] = "S2 in component y2 (dimensionless)"
    legend_states[3] = "y3 in component y3 (dimensionless)"
    legend_states[4] = "y4 in component y4 (dimensionless)"
    legend_constants[12] = "a23 in component model_parameters (dimensionless)"
    legend_constants[13] = "a24 in component model_parameters (dimensionless)"
    legend_constants[14] = "a20 in component model_parameters (dimensionless)"
    legend_constants[15] = "a21 in component model_parameters (dimensionless)"
    legend_constants[16] = "a22 in component model_parameters (dimensionless)"
    legend_constants[17] = "e2 in component model_parameters (first_order_rate_constant)"
    legend_algebraic[13] = "g3 in component y3 (dimensionless)"
    legend_algebraic[8] = "r3 in component y3 (dimensionless)"
    legend_algebraic[3] = "h3 in component y3 (dimensionless)"
    legend_constants[18] = "S3 in component y3 (dimensionless)"
    legend_constants[19] = "a32 in component model_parameters (dimensionless)"
    legend_constants[20] = "a33 in component model_parameters (dimensionless)"
    legend_algebraic[14] = "g4 in component y4 (dimensionless)"
    legend_algebraic[9] = "r4 in component y4 (dimensionless)"
    legend_algebraic[4] = "h4 in component y4 (dimensionless)"
    legend_constants[21] = "S4 in component y4 (dimensionless)"
    legend_constants[22] = "a42 in component model_parameters (dimensionless)"
    legend_constants[23] = "a44 in component model_parameters (dimensionless)"
    legend_rates[0] = "d/dt y0 in component y0 (dimensionless)"
    legend_rates[2] = "d/dt y1 in component y1 (dimensionless)"
    legend_rates[1] = "d/dt y2 in component y2 (dimensionless)"
    legend_rates[3] = "d/dt y3 in component y3 (dimensionless)"
    legend_rates[4] = "d/dt y4 in component y4 (dimensionless)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 0.4
    constants[0] = 0.010
    states[1] = 1.17
    constants[1] = -0.00843
    constants[2] = -0.440
    constants[3] = 0.443
    constants[4] = 0.0
    constants[5] = 0.50
    states[2] = 1.4
    constants[6] = 0.010
    constants[7] = 0.082
    constants[8] = -0.0668
    constants[9] = -0.0040
    constants[10] = 0.0
    constants[11] = 0.010
    states[3] = 0.95
    states[4] = 0.65
    constants[12] = 0.0576
    constants[13] = 3.25E-4
    constants[14] = 0.0
    constants[15] = 0.0310
    constants[16] = -0.0957
    constants[17] = 0.0
    constants[18] = 0.010
    constants[19] = 0.00869
    constants[20] = -0.00857
    constants[21] = 0.010
    constants[22] = 1.39E-4
    constants[23] = -1.43E-4
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[5] = custom_piecewise([less(states[0] , constants[5]) & less(constants[1]*states[0]+constants[2]*states[1] , 0.00000), 1.00000-exp((constants[0]*(power(states[0], 2.00000)))/((constants[1]*states[0]+constants[2]*states[1])*(power(constants[5]-states[0], 2.00000)))) , True, 1.00000])
    algebraic[0] = custom_piecewise([greater(constants[1]*states[0]+constants[2]*states[1] , 0.00000), (constants[1]*states[0]+constants[2]*states[1])/(1.00000+((constants[1]*states[0]+constants[2]*states[1])/constants[0])*(1.00000-exp(-((constants[1]*states[0]+constants[2]*states[1])/constants[0])))) , less_equal(constants[1]*states[0]+constants[2]*states[1] , 0.00000), constants[1]*states[0]+constants[2]*states[1] , True, float('nan')])
    algebraic[10] = algebraic[0]*algebraic[5]
    rates[0] = 1.00000*algebraic[10]+constants[3]+constants[4]
    algebraic[6] = custom_piecewise([less(states[2] , constants[5]) & less(constants[7]*states[0]+constants[9]*states[2]+constants[8]*states[1] , 0.00000), 1.00000-exp((constants[6]*(power(states[2], 2.00000)))/((constants[7]*states[0]+constants[9]*states[2]+constants[8]*states[1])*(power(constants[5]-states[2], 2.00000)))) , True, 1.00000])
    algebraic[1] = custom_piecewise([greater(constants[7]*states[0]+constants[9]*states[2]+constants[8]*states[1] , 0.00000), (constants[7]*states[0]+constants[9]*states[2]+constants[8]*states[1])/(1.00000+((constants[7]*states[0]+constants[9]*states[2]+constants[8]*states[1])/constants[6])*(1.00000-exp(-((constants[7]*states[0]+constants[9]*states[2]+constants[8]*states[1])/constants[6])))) , less_equal(constants[7]*states[0]+constants[9]*states[2]+constants[8]*states[1] , 0.00000), constants[7]*states[0]+constants[9]*states[2]+constants[8]*states[1] , True, float('nan')])
    algebraic[11] = algebraic[1]*algebraic[6]
    rates[2] = 1.00000*algebraic[11]+constants[10]
    algebraic[7] = custom_piecewise([less(states[1] , constants[5]) & less(constants[14]*states[0]+constants[15]*states[2]+constants[16]*states[1]+constants[12]*states[3]+constants[13]*states[4] , 0.00000), 1.00000-exp((constants[11]*(power(states[1], 2.00000)))/((constants[14]*states[0]+constants[15]*states[2]+constants[16]*states[1]+constants[12]*states[3]+constants[13]*states[4])*(power(constants[5]-states[1], 2.00000)))) , True, 1.00000])
    algebraic[2] = custom_piecewise([greater(constants[14]*states[0]+constants[15]*states[2]+constants[16]*states[1]+constants[12]*states[3]+constants[13]*states[4] , 0.00000), (constants[14]*states[0]+constants[15]*states[2]+constants[16]*states[1]+constants[12]*states[3]+constants[13]*states[4])/(1.00000+((constants[14]*states[0]+constants[15]*states[2]+constants[16]*states[1]+constants[12]*states[3]+constants[13]*states[4])/constants[11])*(1.00000-exp(-((constants[14]*states[0]+constants[15]*states[2]+constants[16]*states[1]+constants[12]*states[3]+constants[13]*states[4])/constants[11])))) , less_equal(constants[14]*states[0]+constants[15]*states[2]+constants[16]*states[1]+constants[12]*states[3]+constants[13]*states[4] , 0.00000), constants[14]*states[0]+constants[15]*states[2]+constants[16]*states[1]+constants[12]*states[3]+constants[13]*states[4] , True, float('nan')])
    algebraic[12] = algebraic[2]*algebraic[7]
    rates[1] = 1.00000*algebraic[12]+constants[17]
    algebraic[8] = custom_piecewise([less(states[3] , constants[5]) & less(constants[19]*states[1]+constants[20]*states[3] , 0.00000), 1.00000-exp((constants[18]*(power(states[3], 2.00000)))/((constants[19]*states[1]+constants[20]*states[3])*(power(constants[5]-states[3], 2.00000)))) , True, 1.00000])
    algebraic[3] = custom_piecewise([greater(constants[19]*states[1]+constants[20]*states[3] , 0.00000), (constants[19]*states[1]+constants[20]*states[3])/(1.00000+((constants[19]*states[1]+constants[20]*states[3])/constants[18])*(1.00000-exp(-((constants[19]*states[1]+constants[20]*states[3])/constants[18])))) , less_equal(constants[19]*states[1]+constants[20]*states[3] , 0.00000), constants[19]*states[1]+constants[20]*states[3] , True, float('nan')])
    algebraic[13] = algebraic[3]*algebraic[8]
    rates[3] = 1.00000*algebraic[13]
    algebraic[9] = custom_piecewise([less(states[4] , constants[5]) & less(constants[22]*states[1]+constants[23]*states[4] , 0.00000), 1.00000-exp((constants[21]*(power(states[4], 2.00000)))/((constants[22]*states[1]+constants[23]*states[4])*(power(constants[5]-states[4], 2.00000)))) , True, 1.00000])
    algebraic[4] = custom_piecewise([greater(constants[22]*states[1]+constants[23]*states[4] , 0.00000), (constants[22]*states[1]+constants[23]*states[4])/(1.00000+((constants[22]*states[1]+constants[23]*states[4])/constants[21])*(1.00000-exp(-((constants[22]*states[1]+constants[23]*states[4])/constants[21])))) , less_equal(constants[22]*states[1]+constants[23]*states[4] , 0.00000), constants[22]*states[1]+constants[23]*states[4] , True, float('nan')])
    algebraic[14] = algebraic[4]*algebraic[9]
    rates[4] = 1.00000*algebraic[14]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[5] = custom_piecewise([less(states[0] , constants[5]) & less(constants[1]*states[0]+constants[2]*states[1] , 0.00000), 1.00000-exp((constants[0]*(power(states[0], 2.00000)))/((constants[1]*states[0]+constants[2]*states[1])*(power(constants[5]-states[0], 2.00000)))) , True, 1.00000])
    algebraic[0] = custom_piecewise([greater(constants[1]*states[0]+constants[2]*states[1] , 0.00000), (constants[1]*states[0]+constants[2]*states[1])/(1.00000+((constants[1]*states[0]+constants[2]*states[1])/constants[0])*(1.00000-exp(-((constants[1]*states[0]+constants[2]*states[1])/constants[0])))) , less_equal(constants[1]*states[0]+constants[2]*states[1] , 0.00000), constants[1]*states[0]+constants[2]*states[1] , True, float('nan')])
    algebraic[10] = algebraic[0]*algebraic[5]
    algebraic[6] = custom_piecewise([less(states[2] , constants[5]) & less(constants[7]*states[0]+constants[9]*states[2]+constants[8]*states[1] , 0.00000), 1.00000-exp((constants[6]*(power(states[2], 2.00000)))/((constants[7]*states[0]+constants[9]*states[2]+constants[8]*states[1])*(power(constants[5]-states[2], 2.00000)))) , True, 1.00000])
    algebraic[1] = custom_piecewise([greater(constants[7]*states[0]+constants[9]*states[2]+constants[8]*states[1] , 0.00000), (constants[7]*states[0]+constants[9]*states[2]+constants[8]*states[1])/(1.00000+((constants[7]*states[0]+constants[9]*states[2]+constants[8]*states[1])/constants[6])*(1.00000-exp(-((constants[7]*states[0]+constants[9]*states[2]+constants[8]*states[1])/constants[6])))) , less_equal(constants[7]*states[0]+constants[9]*states[2]+constants[8]*states[1] , 0.00000), constants[7]*states[0]+constants[9]*states[2]+constants[8]*states[1] , True, float('nan')])
    algebraic[11] = algebraic[1]*algebraic[6]
    algebraic[7] = custom_piecewise([less(states[1] , constants[5]) & less(constants[14]*states[0]+constants[15]*states[2]+constants[16]*states[1]+constants[12]*states[3]+constants[13]*states[4] , 0.00000), 1.00000-exp((constants[11]*(power(states[1], 2.00000)))/((constants[14]*states[0]+constants[15]*states[2]+constants[16]*states[1]+constants[12]*states[3]+constants[13]*states[4])*(power(constants[5]-states[1], 2.00000)))) , True, 1.00000])
    algebraic[2] = custom_piecewise([greater(constants[14]*states[0]+constants[15]*states[2]+constants[16]*states[1]+constants[12]*states[3]+constants[13]*states[4] , 0.00000), (constants[14]*states[0]+constants[15]*states[2]+constants[16]*states[1]+constants[12]*states[3]+constants[13]*states[4])/(1.00000+((constants[14]*states[0]+constants[15]*states[2]+constants[16]*states[1]+constants[12]*states[3]+constants[13]*states[4])/constants[11])*(1.00000-exp(-((constants[14]*states[0]+constants[15]*states[2]+constants[16]*states[1]+constants[12]*states[3]+constants[13]*states[4])/constants[11])))) , less_equal(constants[14]*states[0]+constants[15]*states[2]+constants[16]*states[1]+constants[12]*states[3]+constants[13]*states[4] , 0.00000), constants[14]*states[0]+constants[15]*states[2]+constants[16]*states[1]+constants[12]*states[3]+constants[13]*states[4] , True, float('nan')])
    algebraic[12] = algebraic[2]*algebraic[7]
    algebraic[8] = custom_piecewise([less(states[3] , constants[5]) & less(constants[19]*states[1]+constants[20]*states[3] , 0.00000), 1.00000-exp((constants[18]*(power(states[3], 2.00000)))/((constants[19]*states[1]+constants[20]*states[3])*(power(constants[5]-states[3], 2.00000)))) , True, 1.00000])
    algebraic[3] = custom_piecewise([greater(constants[19]*states[1]+constants[20]*states[3] , 0.00000), (constants[19]*states[1]+constants[20]*states[3])/(1.00000+((constants[19]*states[1]+constants[20]*states[3])/constants[18])*(1.00000-exp(-((constants[19]*states[1]+constants[20]*states[3])/constants[18])))) , less_equal(constants[19]*states[1]+constants[20]*states[3] , 0.00000), constants[19]*states[1]+constants[20]*states[3] , True, float('nan')])
    algebraic[13] = algebraic[3]*algebraic[8]
    algebraic[9] = custom_piecewise([less(states[4] , constants[5]) & less(constants[22]*states[1]+constants[23]*states[4] , 0.00000), 1.00000-exp((constants[21]*(power(states[4], 2.00000)))/((constants[22]*states[1]+constants[23]*states[4])*(power(constants[5]-states[4], 2.00000)))) , True, 1.00000])
    algebraic[4] = custom_piecewise([greater(constants[22]*states[1]+constants[23]*states[4] , 0.00000), (constants[22]*states[1]+constants[23]*states[4])/(1.00000+((constants[22]*states[1]+constants[23]*states[4])/constants[21])*(1.00000-exp(-((constants[22]*states[1]+constants[23]*states[4])/constants[21])))) , less_equal(constants[22]*states[1]+constants[23]*states[4] , 0.00000), constants[22]*states[1]+constants[23]*states[4] , True, float('nan')])
    algebraic[14] = algebraic[4]*algebraic[9]
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
        self.S0 = 0.010
        self.a00 = -0.00843
        self.a02 = -0.440
        self.c0 = 0.443
        self.e0 = 0.0
        self.epsilon = 0.50
        self.S1 = 0.010
        self.a10 = 0.082
        self.a12 = -0.0668
        self.a11 = -0.0040
        self.e1 = 0.0
        self.S2 = 0.010
        self.a23 = 0.0576
        self.a24 = 3.25E-4
        self.a20 = 0.0
        self.a21 = 0.0310
        self.a22 = -0.0957
        self.e2 = 0.0
        self.S3 = 0.010
        self.a32 = 0.00869
        self.a33 = -0.00857
        self.S4 = 0.010
        self.a42 = 1.39E-4
        self.a44 = -1.43E-4

    def to_dict(self):
        return {
            "S0": self.S0,
            "a00": self.a00,
            "a02": self.a02,
            "c0": self.c0,
            "e0": self.e0,
            "epsilon": self.epsilon,
            "S1": self.S1,
            "a10": self.a10,
            "a12": self.a12,
            "a11": self.a11,
            "e1": self.e1,
            "S2": self.S2,
            "a23": self.a23,
            "a24": self.a24,
            "a20": self.a20,
            "a21": self.a21,
            "a22": self.a22,
            "e2": self.e2,
            "S3": self.S3,
            "a32": self.a32,
            "a33": self.a33,
            "S4": self.S4,
            "a42": self.a42,
            "a44": self.a44,
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
        y0=[0.4, 1.17, 1.4, 0.95, 0.65],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "kyrylov_severyanova_vieira_2005"
        self.curve_names = [
            "y0",
            "y2",
            "y1",
            "y3",
            "y4",
        ]
        self.state_names = ['y0', 'y2', 'y1', 'y3', 'y4']
        self.algebraic_names = ['h0', 'h1', 'h2', 'h3', 'h4', 'r0', 'r1', 'r2', 'r3', 'r4', 'g0', 'g1', 'g2', 'g3', 'g4']
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
        c[0] = p.S0
        c[1] = p.a00
        c[2] = p.a02
        c[3] = p.c0
        c[4] = p.e0
        c[5] = p.epsilon
        c[6] = p.S1
        c[7] = p.a10
        c[8] = p.a12
        c[9] = p.a11
        c[10] = p.e1
        c[11] = p.S2
        c[12] = p.a23
        c[13] = p.a24
        c[14] = p.a20
        c[15] = p.a21
        c[16] = p.a22
        c[17] = p.e2
        c[18] = p.S3
        c[19] = p.a32
        c[20] = p.a33
        c[21] = p.S4
        c[22] = p.a42
        c[23] = p.a44

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
