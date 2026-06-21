import numpy as np
from scipy.integrate import odeint


class Parameters:
    g11 = 1.0
    p186 = 0.5
    p110 = 1.0
    p19 = 1.0
    p18 = 1.0
    k1 = 0.03
    g22 = 1.0
    p286 = 0.25
    p210 = 0.5
    p29 = 0.5
    p28 = 0.5
    i26 = -1.0
    k2 = 0.01
    g326 = 1.0
    g23 = 1.0
    k3 = 0.007
    k4 = 0.9
    i41 = -0.01
    i42 = -0.01
    i43 = -0.01
    g412 = 1.0
    g415 = 1.0
    g427 = 1.0
    g430 = 1.0
    k6 = 0.5
    g613 = 1.0
    g614 = 1.0
    g615 = 1.0
    k7 = 0.03
    g715 = 1.0
    g716 = 1.0
    g717 = 1.0
    k8 = 0.001
    g819 = 1.0
    g821 = 1.0
    k9 = 0.001
    g919 = 1.0
    g920 = 1.0
    k10 = 0.05
    g1025 = 1.0
    g1072 = 1.0
    k11 = 0.05
    g1124 = 1.0
    g1170 = 1.0
    k13 = 0.1
    i131 = -0.01
    i1310 = -0.01
    g1335 = 1.0
    g1336 = 1.0
    g1351 = 1.0
    k14 = 3.0
    g1437 = 1.0
    g1467 = 1.0
    k15 = 0.2
    i152 = -0.1
    g156 = 1.0
    g1544 = 1.0
    g1545 = 1.0
    k16 = 1e-4
    g1643 = 1.0
    g1644 = 1.0
    k17 = 1e-4
    g1742 = 1.0
    g1744 = 1.0
    k18 = 0.02
    g186 = 1.0
    g1851 = 1.0
    k19 = 0.01
    g196 = 1.0
    g1951 = 1.0
    g1953 = 1.0
    g1960 = 1.0
    k20 = 0.1
    g209 = 1.0
    g2065 = 1.0
    k21 = 0.1
    g2166 = 1.0
    k22 = 0.5
    g229 = 1.0
    g2259 = 1.0
    k23 = 0.5
    g239 = 1.0
    g2361 = 1.0
    g2362 = 1.0
    k24 = 1.0
    g2463 = 1.0
    g2464 = 1.0
    k25 = 0.05
    g2552 = 1.0
    g2555 = 0.3
    g2556 = 0.25
    k26f = 0.05
    g26f15 = 1.0
    g26f16 = 1.0
    g26f18 = 1.0
    k26r = 0.005
    g26r30 = 1.0
    g26r68 = 1.0
    k27f = 0.05
    g27f15 = 1.0
    g27f16 = 1.0
    g27f68 = 1.0
    k27r = 0.005
    g27r30 = 1.0
    g27r69 = 1.0
    k28f = 0.05
    g28f15 = 1.0
    g28f16 = 1.0
    g28f69 = 1.0
    k28r = 0.005
    g28r30 = 1.0
    g28r70 = 1.0
    k29 = 0.05
    g2915 = 1.0
    g2916 = 1.0
    g2971 = 1.0
    k30 = 0.001
    g301 = 1.0
    g3030 = 1.0
    k31 = 0.05
    g3172 = 1.0
    g3173 = 1.0
    k32 = 0.001
    g321 = 1.0
    p328 = 0.1
    p329 = 0.1
    p3210 = 0.1
    p3286 = 0.05
    g3274 = 1.0
    k33 = 0.001
    g332 = 1.0
    g3330 = 1.0
    k34 = 0.05
    g3472 = 1.0
    g3475 = 1.0
    k35 = 0.001
    g352 = 1.0
    p358 = 0.1
    p359 = 0.1
    p3510 = 0.1
    p3586 = 0.05
    g3576 = 1.0
    k36 = 0.05
    i368 = -0.1
    i369 = -0.1
    i3610 = -0.1
    i3686 = -0.05
    g3677 = 1.0
    g3679 = 1.0
    k37 = 0.05
    g3770 = 1.0
    g3773 = 1.0
    k38 = 0.7
    i381 = -0.01
    i382 = -0.01
    i383 = -0.01
    g3812 = 1.0
    g3815 = 1.0
    g3830 = 1.0
    g3878 = 1.0
    k43 = 0.05
    g431 = 1.0
    g4384 = 1.0
    k44 = 0.045
    g442 = 1.0
    g4484 = 1.0
    k45 = 0.04
    g453 = 1.0
    g4584 = 1.0
    k46 = 0.03
    i468 = -0.1
    i469 = -0.1
    i4610 = -0.1
    i4686 = -0.05
    g4677 = 1.0
    g4681 = 1.0
    k47 = 0.03
    i478 = -0.1
    i479 = -0.1
    i4710 = -0.1
    i4786 = -0.05
    g4777 = 1.0
    g4782 = 1.0
    k48 = 0.03
    i488 = -0.1
    i489 = -0.1
    i4810 = -0.1
    i4886 = -0.05
    g4877 = 1.0
    g4883 = 1.0
    k50 = 0.05
    g501 = 1.0
    g5080 = 1.0
    k51 = 0.05
    g512 = 1.0
    g5180 = 1.0
    k52 = 0.05
    g523 = 1.0
    g5280 = 1.0
    k53 = 0.05
    g534 = 1.0
    g5380 = 1.0
    k54 = 0.005
    g5410 = 1.0
    g5419 = 1.0
    k55 = 0.05
    g556 = 1.0
    g5586 = 1.0
    k56 = 0.05
    g5686 = 1.0
    g5687 = 1.0
    k57 = 0.005
    g5710 = 1.0
    g5762 = 1.0
    k100 = 0.005
    g10037 = 1.0
    g10051 = 1.0
    g100115 = 1.0
    k101 = 0.005
    g10136 = 1.0
    g10151 = 1.0
    g101115 = 1.0
    k102 = 0.005
    g10210 = 1.0
    g10251 = 1.0
    g102115 = 1.0
    k115 = 0.5
    g11565 = 1.0
    g11566 = 1.0
    g115118 = 1.0
    k116 = 0.5
    g11642 = 1.0
    g116118 = 1.0
    k1_0 = 0.0
    k2_0 = 0.0
    k4_0 = 0.0
    k13_0 = 0.0
    k15_0 = 0.0
    k32_0 = 0.0
    k35_0 = 0.0
    k36_0 = 0.0
    k38_0 = 0.0
    k46_0 = 0.0
    k47_0 = 0.0
    k48_0 = 0.0


class Config:
    def __init__(
        self,
        param: Parameters = None,
        calculate: bool = False,
        T: int = 100,
        T_unit: float = 0.01,
    ):
        self.model_name = "Sass2009 - Approach to an α-synuclein-based BST model of Parkinson's disease"
        self.curve_names = [
            "Alpha_synuclein",
            "Protofibril",
            "Fibril",
            "Lewy_body",
            "Dopamine",
            "OH",
            "OH_radical",
            "H2O2",
            "DA_quinone",
            "Ubiquitin",
            "E1",
            "Ub_E1",
            "UbcH8",
            "UbcH8_Ub",
            "Parkin",
            "Parkin_sub",
            "Parkin_synphilin_1",
            "Parkin_synphilin_1_ub",
            "Parkin_sub_ub4",
            "Fragments",
            "UCH_L1",
            "L_Dopa",
            "DOPAL",
            "DOPAC",
            "GSH",
            "GSSG",
            "Fe2",
            "Fe3",
            "UbcH8ub2",
            "UbcH8ub3",
            "UbcH8ub4",
            "UbcH13_Uev1a",
            "UbcH13_Uev1a_ub",
            "asyn_UCH_L1",
            "asyn_ub",
            "Protofibril_UCH_L1",
            "Protofibril_Ub",
            "UCH_L1_asyn_ub4",
            "Hsc70_asyn",
            "Hsc70_Protofibril",
            "Hsc70_fibril",
            "Hsc70",
            "DA_S_parkin",
            "O2",
            "DA_GSH",
            "Neuromelanin",
            "Neuromelanin_ntox_Fe3",
            "V_DA",
            "V_ntox_ba",
            "Autophagosome_0",
            "Fe2",
        ]
        self.params = param

        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)

        self.prob_dim = 50
        self.y0 = np.zeros(self.prob_dim)
        self.y0[49] = 0.5
        self.y0[0] = 0.05
        self.y0[1] = 0.025
        self.y0[2] = 0.01
        self.y0[3] = 2.0
        self.y0[4] = 0.5
        self.y0[5] = 0.02
        self.y0[6] = 0.1
        self.y0[7] = 0.05
        self.y0[8] = 1.0
        self.y0[9] = 0.2
        self.y0[10] = 0.35
        self.y0[11] = 0.2
        self.y0[12] = 0.35
        self.y0[13] = 0.2
        self.y0[14] = 0.1
        self.y0[15] = 1.3
        self.y0[16] = 2.5
        self.y0[17] = 0.2
        self.y0[18] = 0.1
        self.y0[19] = 0.5
        self.y0[20] = 1.0
        self.y0[21] = 0.05
        self.y0[22] = 0.3
        self.y0[23] = 1.5
        self.y0[24] = 1.5
        self.y0[25] = 0.5
        self.y0[26] = 0.5
        self.y0[27] = 0.35
        self.y0[28] = 0.35
        self.y0[29] = 0.35
        self.y0[30] = 0.2
        self.y0[31] = 0.35
        self.y0[32] = 0.1
        self.y0[33] = 0.05
        self.y0[34] = 0.025
        self.y0[35] = 0.013
        self.y0[36] = 0.1
        self.y0[37] = 0.1
        self.y0[38] = 0.025
        self.y0[39] = 0.013
        self.y0[40] = 0.5
        self.y0[41] = 0.2
        self.y0[42] = 0.02
        self.y0[43] = 0.2
        self.y0[44] = 1.0
        self.y0[45] = 0.5
        self.y0[46] = 10.0
        self.y0[47] = 0.3
        self.y0[48] = 0.5
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def pend(self, y, t):
        compartment_Neuronal_cytosol = 1.0
        compartment_Vesicle = 1.0
        compartment_Autophagosome = 1.0
        compartment_Proteasome = 1.0
        compartment_Lysosome = 1.0
        const_species_Alpha_synuclein = 0.2
        const_species_ATP = 2.0
        const_species_Synphilin_1 = 0.05
        const_species_Substrate = 0.4
        const_species_TH = 0.6
        const_species_L_Tyr = 5.0
        const_species_CO2 = 0.5
        const_species_Neurotoxins = 0.01
        const_species_Bioamines = 0.1
        const_species_VMAT2 = 2.0
        const_species_O2_0 = 2.0
        const_species_MAO = 1.5
        const_species_NH3 = 0.5
        const_species_ALDH = 1.5
        const_species_NAD = 1.5
        const_species_NADH = 1.5
        const_species_Catalase = 1.0
        const_species_H2O = 3.0
        const_species_Gluta_per = 0.8
        const_species_Gluta_red = 0.8
        const_species_DDC = 1.5
        const_species_Preautophagosome_membrane = 1.0
        const_species_SOD = 0.6
        const_species_Cysteine = 0.5
        const_species_Vesicle_0 = 1.0
        const_species_Proteasome_0 = 1.5
        const_species_Lysosome_0 = 2.5

        self.params.k1_0 = 0.0003 * (
            self.params.p18 * y[5]
            + self.params.p19 * y[6]
            + self.params.p110 * y[7]
            + self.params.p186 * y[42]
        )
        self.params.k2_0 = 0.0001 * (
            self.params.i26 * y[3]
            + self.params.p28 * y[5]
            + self.params.p29 * y[6]
            + self.params.p210 * y[7]
            + self.params.p286 * y[42]
        )
        self.params.k4_0 = 0.009 * (
            self.params.i41 * const_species_Alpha_synuclein
            + self.params.i42 * y[0]
            + self.params.i43 * y[1]
        )
        self.params.k13_0 = 0.001 * (
            self.params.i131 * const_species_Alpha_synuclein + self.params.i1310 * y[7]
        )
        self.params.k15_0 = 0.002 * self.params.i152 * y[0]
        self.params.k32_0 = 1e-5 * (
            self.params.p328 * y[5]
            + self.params.p329 * y[6]
            + self.params.p3210 * y[7]
            + self.params.p3286 * y[42]
        )
        self.params.k35_0 = 1e-5 * (
            self.params.p358 * y[5]
            + self.params.p359 * y[6]
            + self.params.p3510 * y[7]
            + self.params.p3586 * y[42]
        )
        self.params.k36_0 = 0.0005 * (
            self.params.i368 * y[5]
            + self.params.i369 * y[6]
            + self.params.i3610 * y[7]
            + self.params.i3686 * y[42]
        )
        self.params.k38_0 = 0.007 * (
            self.params.i381 * const_species_Alpha_synuclein
            + self.params.i382 * y[0]
            + self.params.i383 * y[1]
        )
        self.params.k46_0 = 0.0003 * (
            self.params.i468 * y[5]
            + self.params.i469 * y[6]
            + self.params.i4610 * y[7]
            + self.params.i4686 * y[42]
        )
        self.params.k47_0 = 0.0003 * (
            self.params.i478 * y[5]
            + self.params.i479 * y[6]
            + self.params.i4710 * y[7]
            + self.params.i4786 * y[42]
        )
        self.params.k48_0 = 0.0003 * (
            self.params.i488 * y[5]
            + self.params.i489 * y[6]
            + self.params.i4810 * y[7]
            + self.params.i4886 * y[42]
        )

        y[25] = y[49]

        reaction_J1 = compartment_Neuronal_cytosol * self.J1Sub(
            self.params.k1, const_species_Alpha_synuclein, self.params.g11
        )
        reaction_J2 = compartment_Neuronal_cytosol * self.J1Sub(
            self.params.k2, y[0], self.params.g22
        )
        reaction_J3 = compartment_Neuronal_cytosol * self.J2Sub(
            self.params.k3, y[1], self.params.g23, y[16], self.params.g326
        )
        reaction_J4 = compartment_Neuronal_cytosol * self.J1Sub3Mod(
            self.params.k4,
            y[17],
            self.params.g427,
            const_species_Proteasome_0,
            self.params.g412,
            const_species_ATP,
            self.params.g415,
            y[19],
            self.params.g430,
        )
        reaction_J6 = compartment_Neuronal_cytosol * self.J2Sub1Mod(
            self.params.k6,
            y[8],
            self.params.g613,
            y[9],
            self.params.g614,
            const_species_ATP,
            self.params.g615,
        )
        reaction_J7 = compartment_Neuronal_cytosol * self.J2Sub1Mod(
            self.params.k7,
            y[10],
            self.params.g716,
            y[11],
            self.params.g717,
            const_species_ATP,
            self.params.g715,
        )
        reaction_J8 = compartment_Neuronal_cytosol * self.J2Sub(
            self.params.k8,
            y[13],
            self.params.g819,
            const_species_Substrate,
            self.params.g821,
        )
        reaction_J9 = compartment_Neuronal_cytosol * self.J2Sub(
            self.params.k9,
            y[13],
            self.params.g919,
            const_species_Synphilin_1,
            self.params.g920,
        )
        reaction_J10 = compartment_Neuronal_cytosol * self.J2Sub(
            self.params.k10, y[15], self.params.g1025, y[31], self.params.g1072
        )
        reaction_J11 = compartment_Neuronal_cytosol * self.J2Sub(
            self.params.k11, y[14], self.params.g1124, y[29], self.params.g1170
        )
        reaction_J13 = compartment_Neuronal_cytosol * self.J2Sub1Mod(
            self.params.k13,
            const_species_L_Tyr,
            self.params.g1336,
            const_species_O2_0,
            self.params.g1351,
            const_species_TH,
            self.params.g1335,
        )
        reaction_J14 = compartment_Neuronal_cytosol * self.J1Sub1Mod(
            self.params.k14,
            y[20],
            self.params.g1437,
            const_species_DDC,
            self.params.g1467,
        )
        reaction_J15 = self.J2Sub1Mod(
            self.params.k15,
            y[3],
            self.params.g156,
            const_species_Vesicle_0,
            self.params.g1544,
            const_species_VMAT2,
            self.params.g1545,
        )
        reaction_J16 = self.J2Sub(
            self.params.k16,
            const_species_Bioamines,
            self.params.g1643,
            const_species_Vesicle_0,
            self.params.g1644,
        )
        reaction_J17 = self.J2Sub(
            self.params.k17,
            const_species_Neurotoxins,
            self.params.g1742,
            const_species_Vesicle_0,
            self.params.g1744,
        )
        reaction_J18 = compartment_Neuronal_cytosol * self.J2Sub(
            self.params.k18,
            y[3],
            self.params.g186,
            const_species_O2_0,
            self.params.g1851,
        )
        reaction_J19 = compartment_Neuronal_cytosol * self.J3Sub1Mod(
            self.params.k19,
            y[3],
            self.params.g196,
            const_species_O2_0,
            self.params.g1951,
            const_species_H2O,
            self.params.g1960,
            const_species_MAO,
            self.params.g1953,
        )
        reaction_J20 = compartment_Neuronal_cytosol * self.J2Sub(
            self.params.k20, y[6], self.params.g209, y[25], self.params.g2065
        )
        reaction_J21 = compartment_Neuronal_cytosol * self.J1Sub(
            self.params.k21, y[26], self.params.g2166
        )
        reaction_J22 = compartment_Neuronal_cytosol * self.J1Sub1Mod(
            self.params.k22,
            y[6],
            self.params.g229,
            const_species_Catalase,
            self.params.g2259,
        )
        reaction_J23 = compartment_Neuronal_cytosol * self.J2Sub1Mod(
            self.params.k23,
            y[6],
            self.params.g239,
            y[23],
            self.params.g2362,
            const_species_Gluta_per,
            self.params.g2361,
        )
        reaction_J24 = compartment_Neuronal_cytosol * self.J1Sub1Mod(
            self.params.k24,
            y[24],
            self.params.g2463,
            const_species_Gluta_red,
            self.params.g2464,
        )
        reaction_J25 = compartment_Neuronal_cytosol * self.J2Sub1Mod(
            self.params.k25,
            y[21],
            self.params.g2552,
            const_species_NAD,
            self.params.g2556,
            const_species_ALDH,
            self.params.g2555,
        )
        reaction_J26f = compartment_Neuronal_cytosol * self.J2Sub1Mod(
            self.params.k26f,
            y[10],
            self.params.g26f16,
            y[12],
            self.params.g26f18,
            const_species_ATP,
            self.params.g26f15,
        )
        reaction_J26r = compartment_Neuronal_cytosol * self.J1Sub1Mod(
            self.params.k26r, y[27], self.params.g26r68, y[19], self.params.g26r30
        )
        reaction_J27f = compartment_Neuronal_cytosol * self.J2Sub1Mod(
            self.params.k27f,
            y[10],
            self.params.g27f16,
            y[27],
            self.params.g27f68,
            const_species_ATP,
            self.params.g27f15,
        )
        reaction_J27r = compartment_Neuronal_cytosol * self.J1Sub1Mod(
            self.params.k27r, y[28], self.params.g27r69, y[19], self.params.g27r30
        )
        reaction_J28f = compartment_Neuronal_cytosol * self.J2Sub1Mod(
            self.params.k28f,
            y[10],
            self.params.g28f16,
            y[28],
            self.params.g28f69,
            const_species_ATP,
            self.params.g28f15,
        )
        reaction_J28r = compartment_Neuronal_cytosol * self.J1Sub1Mod(
            self.params.k28r, y[29], self.params.g28r70, y[19], self.params.g28r30
        )
        reaction_J29 = compartment_Neuronal_cytosol * self.J2Sub1Mod(
            self.params.k29,
            y[10],
            self.params.g2916,
            y[30],
            self.params.g2971,
            const_species_ATP,
            self.params.g2915,
        )
        reaction_J30 = compartment_Neuronal_cytosol * self.J2Sub(
            self.params.k30,
            const_species_Alpha_synuclein,
            self.params.g301,
            y[19],
            self.params.g3030,
        )
        reaction_J31 = compartment_Neuronal_cytosol * self.J2Sub(
            self.params.k31, y[31], self.params.g3172, y[32], self.params.g3173
        )
        reaction_J32 = compartment_Neuronal_cytosol * self.J2Sub(
            self.params.k32,
            const_species_Alpha_synuclein,
            self.params.g321,
            y[33],
            self.params.g3274,
        )
        reaction_J33 = compartment_Neuronal_cytosol * self.J2Sub(
            self.params.k33, y[0], self.params.g332, y[19], self.params.g3330
        )
        reaction_J34 = compartment_Neuronal_cytosol * self.J2Sub(
            self.params.k34, y[31], self.params.g3472, y[34], self.params.g3475
        )
        reaction_J35 = compartment_Neuronal_cytosol * self.J2Sub(
            self.params.k35, y[0], self.params.g352, y[35], self.params.g3576
        )
        reaction_J36 = self.J1Sub1Mod(
            self.params.k36,
            y[48],
            self.params.g3679,
            const_species_Lysosome_0,
            self.params.g3677,
        )
        reaction_J37 = compartment_Neuronal_cytosol * self.J2Sub(
            self.params.k37, y[29], self.params.g3770, y[32], self.params.g3773
        )
        reaction_J38 = compartment_Neuronal_cytosol * self.J1Sub3Mod(
            self.params.k38,
            y[36],
            self.params.g3878,
            const_species_Proteasome_0,
            self.params.g3812,
            const_species_ATP,
            self.params.g3815,
            y[19],
            self.params.g3830,
        )
        reaction_J43 = compartment_Neuronal_cytosol * self.J2Sub(
            self.params.k43,
            const_species_Alpha_synuclein,
            self.params.g431,
            y[40],
            self.params.g4384,
        )
        reaction_J44 = compartment_Neuronal_cytosol * self.J2Sub(
            self.params.k44, y[0], self.params.g442, y[40], self.params.g4484
        )
        reaction_J45 = compartment_Neuronal_cytosol * self.J2Sub(
            self.params.k45, y[1], self.params.g453, y[40], self.params.g4584
        )
        reaction_J46 = compartment_Neuronal_cytosol * self.J1Sub1Mod(
            self.params.k46,
            y[37],
            self.params.g4681,
            const_species_Lysosome_0,
            self.params.g4677,
        )
        reaction_J47 = compartment_Neuronal_cytosol * self.J1Sub1Mod(
            self.params.k47,
            y[38],
            self.params.g4782,
            const_species_Lysosome_0,
            self.params.g4777,
        )
        reaction_J48 = compartment_Neuronal_cytosol * self.J1Sub1Mod(
            self.params.k48,
            y[39],
            self.params.g4883,
            const_species_Lysosome_0,
            self.params.g4877,
        )
        reaction_J50 = self.J2Sub(
            self.params.k50,
            const_species_Alpha_synuclein,
            self.params.g501,
            const_species_Preautophagosome_membrane,
            self.params.g5080,
        )
        reaction_J51 = self.J2Sub(
            self.params.k51,
            y[0],
            self.params.g512,
            const_species_Preautophagosome_membrane,
            self.params.g5180,
        )
        reaction_J52 = self.J2Sub(
            self.params.k52,
            y[1],
            self.params.g523,
            const_species_Preautophagosome_membrane,
            self.params.g5280,
        )
        reaction_J53 = self.J2Sub(
            self.params.k53,
            y[2],
            self.params.g534,
            const_species_Preautophagosome_membrane,
            self.params.g5380,
        )
        reaction_J54 = compartment_Neuronal_cytosol * self.J2Sub(
            self.params.k54, y[7], self.params.g5410, y[13], self.params.g5419
        )
        reaction_J55 = compartment_Neuronal_cytosol * self.J2Sub(
            self.params.k55, y[3], self.params.g556, y[42], self.params.g5586
        )
        reaction_J56 = compartment_Neuronal_cytosol * self.J1Sub1Mod(
            self.params.k56,
            y[42],
            self.params.g5686,
            const_species_SOD,
            self.params.g5687,
        )
        reaction_J57 = compartment_Neuronal_cytosol * self.J2Sub(
            self.params.k57, y[7], self.params.g5710, y[23], self.params.g5762
        )
        reaction_J100 = compartment_Neuronal_cytosol * self.J3Sub(
            self.params.k100,
            y[20],
            self.params.g10037,
            const_species_O2_0,
            self.params.g10051,
            const_species_Cysteine,
            self.params.g100115,
        )
        reaction_J101 = compartment_Neuronal_cytosol * self.J3Sub(
            self.params.k101,
            const_species_L_Tyr,
            self.params.g10136,
            const_species_O2_0,
            self.params.g10151,
            const_species_Cysteine,
            self.params.g101115,
        )
        reaction_J102 = compartment_Neuronal_cytosol * self.J3Sub(
            self.params.k102,
            y[7],
            self.params.g10210,
            const_species_O2_0,
            self.params.g10251,
            const_species_Cysteine,
            self.params.g102115,
        )
        reaction_J115 = compartment_Neuronal_cytosol * self.J2Sub(
            self.params.k115, y[26], self.params.g11565, y[44], self.params.g115118
        )
        reaction_J116 = compartment_Neuronal_cytosol * self.J2Sub(
            self.params.k116,
            y[44],
            self.params.g116118,
            const_species_Neurotoxins,
            self.params.g11642,
        )

        dydt = np.zeros(self.prob_dim)
        dydt[49] = reaction_J21 - reaction_J20 + 0.01
        dydt[0] = (1 / compartment_Neuronal_cytosol) * (
            (1.0 * reaction_J1)
            + (-1.0 * reaction_J2)
            + (1.0 * reaction_J32)
            + (-1.0 * reaction_J33)
            + (-1.0 * reaction_J35)
            + (-1.0 * reaction_J44)
            + (-1.0 * reaction_J51)
        )
        dydt[1] = (1 / compartment_Neuronal_cytosol) * (
            (1.0 * reaction_J2)
            + (-1.0 * reaction_J3)
            + (1.0 * reaction_J35)
            + (-1.0 * reaction_J45)
            + (-1.0 * reaction_J52)
        )
        dydt[2] = (1 / compartment_Neuronal_cytosol) * (
            (1.0 * reaction_J3) + (-1.0 * reaction_J53)
        )
        dydt[3] = (1 / compartment_Neuronal_cytosol) * (
            (1.0 * reaction_J14)
            + (-1.0 * reaction_J15)
            + (-1.0 * reaction_J18)
            + (-1.0 * reaction_J19)
            + (-1.0 * reaction_J55)
        )
        dydt[4] = (1 / compartment_Neuronal_cytosol) * ((1.0 * reaction_J20))
        dydt[5] = (1 / compartment_Neuronal_cytosol) * ((1.0 * reaction_J20))
        dydt[6] = (1 / compartment_Neuronal_cytosol) * (
            (1.0 * reaction_J19)
            + (-1.0 * reaction_J20)
            + (-1.0 * reaction_J22)
            + (-1.0 * reaction_J23)
            + (1.0 * reaction_J55)
            + (1.0 * reaction_J56)
            + (1.0 * reaction_J100)
            + (1.0 * reaction_J101)
        )
        dydt[7] = (1 / compartment_Neuronal_cytosol) * (
            (1.0 * reaction_J18)
            + (-1.0 * reaction_J54)
            + (1.0 * reaction_J55)
            + (-1.0 * reaction_J57)
            + (-1.0 * reaction_J102)
        )
        dydt[8] = (1 / compartment_Neuronal_cytosol) * (
            (4.0 * reaction_J4)
            + (-1.0 * reaction_J6)
            + (2.0 * reaction_J26r)
            + (3.0 * reaction_J27r)
            + (4.0 * reaction_J28r)
            + (4.0 * reaction_J38)
        )
        dydt[9] = (1 / compartment_Neuronal_cytosol) * (
            (-1.0 * reaction_J6)
            + (1.0 * reaction_J7)
            + (1.0 * reaction_J26f)
            + (1.0 * reaction_J27f)
            + (1.0 * reaction_J28f)
            + (1.0 * reaction_J29)
        )
        dydt[10] = (1 / compartment_Neuronal_cytosol) * (
            (1.0 * reaction_J6)
            + (-1.0 * reaction_J7)
            + (-1.0 * reaction_J26f)
            + (-1.0 * reaction_J27f)
            + (-1.0 * reaction_J28f)
            + (-1.0 * reaction_J29)
        )
        dydt[11] = (1 / compartment_Neuronal_cytosol) * (
            (-1.0 * reaction_J7)
            + (1.0 * reaction_J11)
            + (1.0 * reaction_J26r)
            + (1.0 * reaction_J27r)
            + (1.0 * reaction_J28r)
            + (1.0 * reaction_J37)
        )
        dydt[12] = (1 / compartment_Neuronal_cytosol) * (
            (1.0 * reaction_J7) + (-1.0 * reaction_J26f)
        )
        dydt[13] = (1 / compartment_Neuronal_cytosol) * (
            (1.0 * reaction_J4)
            + (-1.0 * reaction_J8)
            + (-1.0 * reaction_J9)
            + (-1.0 * reaction_J54)
        )
        dydt[14] = (1 / compartment_Neuronal_cytosol) * (
            (1.0 * reaction_J8) + (-1.0 * reaction_J11)
        )
        dydt[15] = (1 / compartment_Neuronal_cytosol) * (
            (1.0 * reaction_J9) + (-1.0 * reaction_J10)
        )
        dydt[16] = (1 / compartment_Neuronal_cytosol) * (
            (-1.0 * reaction_J3) + (1.0 * reaction_J10)
        )
        dydt[17] = (1 / compartment_Neuronal_cytosol) * (
            (-1.0 * reaction_J4) + (1.0 * reaction_J11)
        )
        dydt[18] = (1 / compartment_Neuronal_cytosol) * (
            (1.0 * reaction_J4)
            + (1.0 * reaction_J36)
            + (1.0 * reaction_J38)
            + (1.0 * reaction_J46)
            + (1.0 * reaction_J47)
            + (1.0 * reaction_J48)
        )
        dydt[19] = (1 / compartment_Neuronal_cytosol) * (
            (-1.0 * reaction_J30)
            + (1.0 * reaction_J31)
            + (-1.0 * reaction_J33)
            + (1.0 * reaction_J34)
            + (1.0 * reaction_J38)
        )
        dydt[20] = (1 / compartment_Neuronal_cytosol) * (
            (1.0 * reaction_J13) + (-1.0 * reaction_J14) + (-1.0 * reaction_J100)
        )
        dydt[21] = (1 / compartment_Neuronal_cytosol) * (
            (1.0 * reaction_J19) + (-1.0 * reaction_J25)
        )
        dydt[22] = (1 / compartment_Neuronal_cytosol) * ((1.0 * reaction_J25))
        dydt[23] = (1 / compartment_Neuronal_cytosol) * (
            (-1.0 * reaction_J23) + (1.0 * reaction_J24) + (-1.0 * reaction_J57)
        )
        dydt[24] = (1 / compartment_Neuronal_cytosol) * (
            (1.0 * reaction_J23) + (-1.0 * reaction_J24)
        )
        dydt[25] = y[25]
        dydt[26] = (1 / compartment_Neuronal_cytosol) * (
            (1.0 * reaction_J20) + (-1.0 * reaction_J21) + (-1.0 * reaction_J115)
        )
        dydt[27] = (1 / compartment_Neuronal_cytosol) * (
            (1.0 * reaction_J26f) + (-1.0 * reaction_J26r) + (-1.0 * reaction_J27f)
        )
        dydt[28] = (1 / compartment_Neuronal_cytosol) * (
            (1.0 * reaction_J27f) + (-1.0 * reaction_J27r) + (-1.0 * reaction_J28f)
        )
        dydt[29] = (1 / compartment_Neuronal_cytosol) * (
            (-1.0 * reaction_J11)
            + (1.0 * reaction_J28f)
            + (-1.0 * reaction_J28r)
            + (-1.0 * reaction_J37)
        )
        dydt[30] = (1 / compartment_Neuronal_cytosol) * (
            (1.0 * reaction_J10)
            + (-1.0 * reaction_J29)
            + (1.0 * reaction_J31)
            + (1.0 * reaction_J34)
        )
        dydt[31] = (1 / compartment_Neuronal_cytosol) * (
            (-1.0 * reaction_J10)
            + (1.0 * reaction_J29)
            + (-1.0 * reaction_J31)
            + (-1.0 * reaction_J34)
        )
        dydt[32] = (1 / compartment_Neuronal_cytosol) * (
            (1.0 * reaction_J30) + (-1.0 * reaction_J31) + (-1.0 * reaction_J37)
        )
        dydt[33] = (1 / compartment_Neuronal_cytosol) * (
            (1.0 * reaction_J31) + (-1.0 * reaction_J32)
        )
        dydt[34] = (1 / compartment_Neuronal_cytosol) * (
            (1.0 * reaction_J33) + (-1.0 * reaction_J34)
        )
        dydt[35] = (1 / compartment_Neuronal_cytosol) * (
            (1.0 * reaction_J34) + (-1.0 * reaction_J35)
        )
        dydt[36] = (1 / compartment_Neuronal_cytosol) * (
            (1.0 * reaction_J37) + (-1.0 * reaction_J38)
        )
        dydt[37] = (1 / compartment_Neuronal_cytosol) * (
            (1.0 * reaction_J43) + (-1.0 * reaction_J46)
        )
        dydt[38] = (1 / compartment_Neuronal_cytosol) * (
            (1.0 * reaction_J44) + (-1.0 * reaction_J47)
        )
        dydt[39] = (1 / compartment_Neuronal_cytosol) * (
            (1.0 * reaction_J45) + (-1.0 * reaction_J48)
        )
        dydt[40] = (1 / compartment_Neuronal_cytosol) * (
            (-1.0 * reaction_J43)
            + (-1.0 * reaction_J44)
            + (-1.0 * reaction_J45)
            + (1.0 * reaction_J46)
            + (1.0 * reaction_J47)
            + (1.0 * reaction_J48)
        )
        dydt[41] = (1 / compartment_Neuronal_cytosol) * ((1.0 * reaction_J54))
        dydt[42] = (1 / compartment_Neuronal_cytosol) * (
            (1.0 * reaction_J18) + (-1.0 * reaction_J55) + (-1.0 * reaction_J56)
        )
        dydt[43] = (1 / compartment_Neuronal_cytosol) * ((1.0 * reaction_J57))
        dydt[44] = (1 / compartment_Neuronal_cytosol) * (
            (1.0 * reaction_J100)
            + (1.0 * reaction_J101)
            + (1.0 * reaction_J102)
            + (-1.0 * reaction_J115)
            + (-1.0 * reaction_J116)
        )
        dydt[45] = (1 / compartment_Neuronal_cytosol) * (
            (1.0 * reaction_J115) + (1.0 * reaction_J116)
        )
        dydt[46] = (1 / compartment_Vesicle) * ((1.0 * reaction_J15))
        dydt[47] = (1 / compartment_Vesicle) * (
            (1.0 * reaction_J16) + (1.0 * reaction_J17)
        )
        dydt[48] = (1 / compartment_Autophagosome) * (
            (-1.0 * reaction_J36)
            + (1.0 * reaction_J50)
            + (1.0 * reaction_J51)
            + (1.0 * reaction_J52)
            + (1.0 * reaction_J53)
        )

        return dydt

    def J3Sub(self, K, X1, G1, X2, G2, X3, G3):
        return K * X1**G1 * X2**G2 * X3**G3

    def J1Sub(self, K, X, G):
        return K * X**G

    def J2Sub(self, K, X1, G1, X2, G2):
        return K * X1**G1 * X2**G2

    def J1Sub3Mod(self, K, X1, G1, X2, G2, X3, G3, X4, G4):
        return K * X1**G1 * X2**G2 * X3**G3 * X4**G4

    def J2Sub1Mod(self, K, X1, G1, X2, G2, X3, G3):
        return K * X1**G1 * X2**G2 * X3**G3

    def J1Sub1Mod(self, K, X1, G1, X2, G2):
        return K * X1**G1 * X2**G2

    def J3Sub1Mod(self, K, X1, G1, X2, G2, X3, G3, X4, G4):
        return K * X1**G1 * X2**G2 * X3**G3 * X4**G4
