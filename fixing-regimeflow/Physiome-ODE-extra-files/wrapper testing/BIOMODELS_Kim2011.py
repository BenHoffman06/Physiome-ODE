import numpy as np
from scipy.integrate import odeint


class Parameters:
    global_par_parameter_1 = 1.0
    global_par_parameter_2 = 0.3
    global_par_parameter_3 = 5.0


class Config:
    def __init__(
        self,
        param: Parameters = None,
        calculate: bool = False,
        T: int = 100,
        T_unit: float = 0.01,
        y0=[0.0, 0.0, 0.33],
    ):
        self.model_name = "Kim2011_Oscillator_SimpleIII"
        self.curve_names = ["x1", "x2", "x3"]
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def pend(self, y, t):
        compartment_compartment_1 = 1.0
        reaction_reaction_1_Shalve = 1.0
        reaction_reaction_2_Shalve = 1.0
        reaction_reaction_3_Shalve = 1.0

        def function_1(V, Shalve, h, substrate):
            return V / (Shalve**h + substrate**h)

        def function_3(x, beta):
            return x / beta / (1 + x / beta)

        reaction_reaction_1 = compartment_compartment_1 * function_1(
            self.params.global_par_parameter_1,
            reaction_reaction_1_Shalve,
            self.params.global_par_parameter_3,
            y[0],
        )
        reaction_reaction_2 = compartment_compartment_1 * function_1(
            self.params.global_par_parameter_1,
            reaction_reaction_2_Shalve,
            self.params.global_par_parameter_3,
            y[1],
        )
        reaction_reaction_3 = compartment_compartment_1 * function_1(
            self.params.global_par_parameter_1,
            reaction_reaction_3_Shalve,
            self.params.global_par_parameter_3,
            y[2],
        )
        reaction_reaction_4 = compartment_compartment_1 * function_3(
            y[0], self.params.global_par_parameter_2
        )
        reaction_reaction_5 = compartment_compartment_1 * function_3(
            y[1], self.params.global_par_parameter_2
        )
        reaction_reaction_6 = compartment_compartment_1 * function_3(
            y[2], self.params.global_par_parameter_2
        )

        xdot = np.zeros(3)
        xdot[0] = (1 / compartment_compartment_1) * (
            (-1.0 * reaction_reaction_1)
            + (1.0 * reaction_reaction_1)
            + (1.0 * reaction_reaction_2)
            + (-1.0 * reaction_reaction_4)
        )
        xdot[1] = (1 / compartment_compartment_1) * (
            (-1.0 * reaction_reaction_2)
            + (1.0 * reaction_reaction_2)
            + (1.0 * reaction_reaction_3)
            + (-1.0 * reaction_reaction_5)
        )
        xdot[2] = (1 / compartment_compartment_1) * (
            (1.0 * reaction_reaction_1)
            + (-1.0 * reaction_reaction_3)
            + (1.0 * reaction_reaction_3)
            + (-1.0 * reaction_reaction_6)
        )
        return xdot
