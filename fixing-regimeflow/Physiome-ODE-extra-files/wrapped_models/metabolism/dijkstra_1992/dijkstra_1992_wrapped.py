# Size of variable arrays:
sizeAlgebraic = 179
sizeStates = 17
sizeConstants = 230
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (day)"
    legend_algebraic[10] = "U_Pd_PdPs in component Q_Pd (mole_per_day)"
    legend_states[0] = "Q_Pd in component Q_Pd (mole)"
    legend_algebraic[0] = "C_Pd in component Q_Pd (molar)"
    legend_algebraic[8] = "U_Pd_PdEx in component Q_Pd (mole_per_day)"
    legend_constants[155] = "P_Pd_InPd in component Q_Pd (mole_per_day)"
    legend_algebraic[9] = "v_PdPs in component Q_Pd (mole_per_day)"
    legend_constants[0] = "v_PdPs_star in component Q_Pd (mole_per_gram_day)"
    legend_constants[174] = "M_Pd_PdPs in component Q_Pd (molar)"
    legend_constants[1] = "M_Pd_PdPs_star in component Q_Pd (molar)"
    legend_constants[2] = "Y_Pd_InPd in component Q_Pd (molar)"
    legend_constants[3] = "D_Pd in component Q_Pd (litre_per_day)"
    legend_constants[154] = "k_PdEx in component Q_Pd (first_order_rate_constant)"
    legend_constants[4] = "T_Pd in component Q_Pd (day)"
    legend_constants[5] = "T_Pd_star in component Q_Pd (day)"
    legend_states[1] = "Q_Ma in component Q_Ma (gram)"
    legend_states[2] = "Q_Mc in component Q_Mc (gram)"
    legend_constants[6] = "V_Ru in component model_parameters (litre)"
    legend_constants[7] = "k_SoEx in component model_parameters (first_order_rate_constant)"
    legend_algebraic[11] = "C_Ps in component Q_Ps (molar)"
    legend_algebraic[48] = "U_McPs_PsAm in component Q_Ps (mole_per_day)"
    legend_algebraic[36] = "U_Ps_PsMa in component Q_Ps (mole_per_day)"
    legend_algebraic[49] = "U_Ps_PsMc in component Q_Ps (mole_per_day)"
    legend_algebraic[35] = "U_MaPs_PsAm in component Q_Ps (mole_per_day)"
    legend_constants[8] = "M_Ha_McMa in component Q_Ps (molar)"
    legend_states[3] = "Q_Ps in component Q_Ps (mole)"
    legend_constants[176] = "P_Ps_InPs in component Q_Ps (mole_per_day)"
    legend_constants[179] = "P_Ps_SaPs in component Q_Ps (mole_per_day)"
    legend_algebraic[12] = "P_Ps_PdPs in component Q_Ps (mole_per_day)"
    legend_algebraic[62] = "P_Ps_MaMd in component Q_Ps (mole_per_day)"
    legend_algebraic[78] = "P_Ps_McPs in component Q_Ps (mole_per_day)"
    legend_algebraic[13] = "U_Ps_PsEx in component Q_Ps (mole_per_day)"
    legend_algebraic[76] = "U_Mc_McPs in component Q_Ps (mole_per_day)"
    legend_algebraic[14] = "v_Ma_PsAm in component Q_Ps (mole_per_day)"
    legend_algebraic[15] = "v_Mc_PsAm in component Q_Ps (mole_per_day)"
    legend_algebraic[16] = "v_PsMa in component Q_Ps (mole_per_day)"
    legend_algebraic[17] = "v_PsMc in component Q_Ps (mole_per_day)"
    legend_constants[9] = "v_PsAm_star in component Q_Ps (mole_per_gram_day)"
    legend_constants[10] = "v_PsMa_star in component Q_Ps (mole_per_gram_day)"
    legend_constants[11] = "v_PsMc_star in component Q_Ps (mole_per_gram_day)"
    legend_constants[156] = "k_PsEx in component Q_Ps (first_order_rate_constant)"
    legend_constants[12] = "Y_Ps_InPs in component Q_Ps (molar)"
    legend_constants[13] = "Y_Ps_SaPs in component Q_Ps (molar)"
    legend_constants[14] = "Y_Ps_PdPs in component Q_Ps (dimensionless)"
    legend_constants[15] = "Y_Ps_MaMd in component Q_Ps (mole_per_gram)"
    legend_constants[16] = "Y_Ps_McPs in component Q_Ps (dimensionless)"
    legend_constants[17] = "D_Ps in component Q_Ps (litre_per_day)"
    legend_constants[18] = "M_Ps_PsAm in component Q_Ps (molar)"
    legend_constants[19] = "M_Ps_PsMa in component Q_Ps (molar)"
    legend_constants[20] = "M_Ps_PsMc in component Q_Ps (molar)"
    legend_constants[21] = "M_Ha_PsMa in component Q_Ps (molar)"
    legend_constants[22] = "M_Hc_PsMc in component Q_Ps (molar)"
    legend_constants[23] = "J_Ha_PsAm in component Q_Ps (molar)"
    legend_constants[24] = "J_Hc_PsAm in component Q_Ps (molar)"
    legend_algebraic[75] = "U_Mc_McEg in component Q_Mc (gram_per_day)"
    legend_algebraic[61] = "U_Ma_MaMd in component Q_Ma (gram_per_day)"
    legend_algebraic[54] = "U_Hc_PsMc in component Q_Hc (mole_per_day)"
    legend_algebraic[82] = "U_Ha_McMa in component Q_Ha (mole_per_day)"
    legend_algebraic[34] = "C_Ha in component Q_Ha (molar)"
    legend_algebraic[47] = "C_Hc in component Q_Hc (molar)"
    legend_constants[25] = "k_FlEx in component model_parameters (first_order_rate_constant)"
    legend_constants[26] = "J_Ha_McAm in component model_parameters (molar)"
    legend_states[4] = "Q_Pu in component Q_Pu (mole)"
    legend_algebraic[1] = "C_Pu in component Q_Pu (molar)"
    legend_constants[157] = "P_Pu_InPu in component Q_Pu (mole_per_day)"
    legend_algebraic[2] = "U_Pu_PuEx in component Q_Pu (mole_per_day)"
    legend_constants[27] = "Y_Pu_InPu in component Q_Pu (molar)"
    legend_constants[28] = "D_Pu in component Q_Pu (litre_per_day)"
    legend_constants[158] = "k_PuEx in component Q_Pu (first_order_rate_constant)"
    legend_algebraic[18] = "C_Am in component Q_Am (molar)"
    legend_algebraic[51] = "U_Am_AmMc in component Q_Am (mole_per_day)"
    legend_algebraic[38] = "U_Am_AmMa in component Q_Am (mole_per_day)"
    legend_algebraic[77] = "U_Mc_McAm in component Q_Am (mole_per_day)"
    legend_states[5] = "Q_Am in component Q_Am (mole)"
    legend_constants[180] = "P_Am_InAm in component Q_Am (mole_per_day)"
    legend_algebraic[22] = "P_Am_UeAm in component Q_Am (mole_per_day)"
    legend_algebraic[37] = "P_MaAm_PsAm in component Q_Am (mole_per_day)"
    legend_algebraic[50] = "P_McAm_PsAm in component Q_Am (mole_per_day)"
    legend_algebraic[79] = "P_Am_McAm in component Q_Am (mole_per_day)"
    legend_algebraic[19] = "U_Am_AmAb in component Q_Am (mole_per_day)"
    legend_algebraic[20] = "U_Am_AmEx in component Q_Am (mole_per_day)"
    legend_algebraic[21] = "v_UeAm in component Q_Am (mole_per_day)"
    legend_constants[181] = "v_AmAb in component Q_Am (mole_per_day)"
    legend_algebraic[23] = "v_AmMa in component Q_Am (mole_per_day)"
    legend_algebraic[24] = "v_AmMc in component Q_Am (mole_per_day)"
    legend_constants[29] = "v_UeAm_star in component Q_Am (mole_per_litre_day)"
    legend_constants[30] = "v_AmAb_star in component Q_Am (mole_per_litre_day)"
    legend_constants[31] = "v_AmMa_star in component Q_Am (mole_per_gram_day)"
    legend_constants[32] = "v_AmMc_star in component Q_Am (mole_per_gram_day)"
    legend_constants[159] = "k_AmEx in component Q_Am (first_order_rate_constant)"
    legend_constants[33] = "Y_Am_InAm in component Q_Am (molar)"
    legend_constants[34] = "Y_Am_UeAm in component Q_Am (dimensionless)"
    legend_constants[35] = "Y_Am_PsAm in component Q_Am (dimensionless)"
    legend_constants[36] = "Y_Am_McAm in component Q_Am (dimensionless)"
    legend_constants[37] = "M_Am_AmMa in component Q_Am (molar)"
    legend_constants[38] = "M_Am_AmMc in component Q_Am (molar)"
    legend_constants[39] = "M_Am_AmAb in component Q_Am (molar)"
    legend_constants[40] = "M_pH_AmAb in component Q_Am (dimensionless)"
    legend_constants[41] = "phi_pH_AmAb in component Q_Am (dimensionless)"
    legend_constants[42] = "M_Ha_AmMa in component Q_Am (molar)"
    legend_constants[43] = "M_Hc_AmMc in component Q_Am (molar)"
    legend_constants[44] = "J_Am_UeAm in component Q_Am (molar)"
    legend_constants[45] = "D_Am in component Q_Am (litre_per_day)"
    legend_constants[46] = "pH in component model_parameters (dimensionless)"
    legend_constants[47] = "f_Po_Ma in component model_parameters (dimensionless)"
    legend_constants[48] = "f_Ni_Fe in component model_parameters (dimensionless)"
    legend_states[6] = "Q_Li in component Q_Li (mole)"
    legend_algebraic[3] = "C_Li in component Q_Li (molar)"
    legend_constants[182] = "P_Li_InLi in component Q_Li (mole_per_day)"
    legend_algebraic[63] = "P_Li_MaMd in component Q_Li (mole_per_day)"
    legend_algebraic[25] = "U_Li_LiEx in component Q_Li (mole_per_day)"
    legend_constants[49] = "Y_Li_InLi in component Q_Li (molar)"
    legend_constants[50] = "Y_Li_MaMd in component Q_Li (mole_per_gram)"
    legend_constants[51] = "D_Li in component Q_Li (litre_per_day)"
    legend_constants[160] = "k_LiEx in component Q_Li (first_order_rate_constant)"
    legend_algebraic[29] = "U_Sd_SdHa in component Q_Sd (mole_per_day)"
    legend_states[7] = "Q_Sd in component Q_Sd (mole)"
    legend_algebraic[26] = "C_Sd in component Q_Sd (molar)"
    legend_constants[183] = "P_Sd_InSd in component Q_Sd (mole_per_day)"
    legend_algebraic[27] = "U_Sd_SdEx in component Q_Sd (mole_per_day)"
    legend_constants[52] = "Y_Sd_InSd in component Q_Sd (molar)"
    legend_constants[53] = "D_Sd in component Q_Sd (litre_per_day)"
    legend_constants[161] = "k_SdEx in component Q_Sd (first_order_rate_constant)"
    legend_algebraic[28] = "v_SdHa in component Q_Sd (mole_per_day)"
    legend_constants[54] = "v_SdHa_star in component Q_Sd (mole_per_gram_day)"
    legend_constants[184] = "M_Sd_SdHa in component Q_Sd (molar)"
    legend_constants[55] = "M_Sd_SdHa_star in component Q_Sd (molar)"
    legend_constants[56] = "T_Sd in component Q_Sd (day)"
    legend_constants[57] = "T_Sd_star in component Q_Sd (day)"
    legend_algebraic[33] = "U_Fd_FdHc in component Q_Fd (mole_per_day)"
    legend_states[8] = "Q_Fd in component Q_Fd (mole)"
    legend_algebraic[30] = "C_Fd in component Q_Fd (molar)"
    legend_constants[185] = "P_Fd_InFd in component Q_Fd (mole_per_day)"
    legend_algebraic[31] = "U_Fd_FdEx in component Q_Fd (mole_per_day)"
    legend_constants[58] = "Y_Fd_InFd in component Q_Fd (molar)"
    legend_constants[59] = "D_Fd in component Q_Fd (litre_per_day)"
    legend_constants[162] = "k_FdEx in component Q_Fd (first_order_rate_constant)"
    legend_algebraic[32] = "v_FdHc in component Q_Fd (mole_per_day)"
    legend_constants[60] = "v_FdHc_star in component Q_Fd (mole_per_gram_day)"
    legend_constants[186] = "M_Fd_FdHc in component Q_Fd (molar)"
    legend_constants[61] = "M_Fd_FdHc_star in component Q_Fd (molar)"
    legend_constants[62] = "T_Fd in component Q_Fd (day)"
    legend_constants[63] = "T_Fd_star in component Q_Fd (day)"
    legend_constants[64] = "phi_pH_FdHc in component Q_Fd (dimensionless)"
    legend_constants[65] = "M_pH_FdHc in component Q_Fd (dimensionless)"
    legend_constants[66] = "pm in component model_parameters (dimensionless)"
    legend_constants[67] = "f in component model_parameters (dimensionless)"
    legend_states[9] = "Q_Fu in component Q_Fu (mole)"
    legend_algebraic[4] = "C_Fu in component Q_Fu (molar)"
    legend_constants[163] = "P_Fu_InFu in component Q_Fu (mole_per_day)"
    legend_algebraic[5] = "U_Fu_FuEx in component Q_Fu (mole_per_day)"
    legend_constants[68] = "Y_Fu_InFu in component Q_Fu (molar)"
    legend_constants[69] = "D_Fu in component Q_Fu (litre_per_day)"
    legend_constants[164] = "k_FuEx in component Q_Fu (first_order_rate_constant)"
    legend_algebraic[44] = "U_Ha_HaAs in component Q_Ha (mole_per_day)"
    legend_algebraic[40] = "U_Ha_AmMa in component Q_Ha (mole_per_day)"
    legend_algebraic[41] = "U_Ha_PsMa in component Q_Ha (mole_per_day)"
    legend_algebraic[46] = "U_Ha_HaVa in component Q_Ha (mole_per_day)"
    legend_constants[187] = "P_Ha_WrHa in component Q_Ha (mole_per_day)"
    legend_constants[189] = "P_Ha_LaHa in component Q_Ha (mole_per_day)"
    legend_constants[188] = "P_Ha_SrHa in component Q_Ha (mole_per_day)"
    legend_algebraic[39] = "P_Ha_SdHa in component Q_Ha (mole_per_day)"
    legend_algebraic[67] = "P_Ha_MaMd in component Q_Ha (mole_per_day)"
    legend_states[10] = "Q_Ha in component Q_Ha (mole)"
    legend_algebraic[42] = "U_Ha_HaEx in component Q_Ha (mole_per_day)"
    legend_constants[70] = "R_Ha_AmMa in component Q_Ha (dimensionless)"
    legend_constants[71] = "R_Ha_PsMa in component Q_Ha (dimensionless)"
    legend_constants[72] = "R_Ha_McMa in component Q_Ha (mole_per_gram)"
    legend_constants[73] = "M_Ha_HaAs in component Q_Ha (molar)"
    legend_constants[74] = "M_Ha_HaVa in component Q_Ha (molar)"
    legend_algebraic[43] = "v_HaAs in component Q_Ha (mole_per_day)"
    legend_algebraic[45] = "v_HaVa in component Q_Ha (mole_per_day)"
    legend_constants[75] = "v_HaAs_star in component Q_Ha (mole_per_gram_day)"
    legend_constants[76] = "v_HaVa_star in component Q_Ha (mole_per_gram_day)"
    legend_constants[165] = "k_HaEx in component Q_Ha (first_order_rate_constant)"
    legend_constants[77] = "Y_Ha_WrHa in component Q_Ha (molar)"
    legend_constants[78] = "Y_Ha_SrHa in component Q_Ha (molar)"
    legend_constants[79] = "Y_Ha_LaHa in component Q_Ha (molar)"
    legend_constants[80] = "Y_Ha_SdHa in component Q_Ha (dimensionless)"
    legend_constants[81] = "Y_Ha_MaMd in component Q_Ha (mole_per_gram)"
    legend_constants[82] = "D_Wr in component Q_Ha (litre_per_day)"
    legend_constants[83] = "D_Sr in component Q_Ha (litre_per_day)"
    legend_constants[84] = "D_La in component Q_Ha (litre_per_day)"
    legend_constants[85] = "J_Am_HaVa in component Q_Ha (molar)"
    legend_constants[86] = "J_Ps_HaVa in component Q_Ha (molar)"
    legend_algebraic[66] = "U_As_MaMd in component Q_As (gram_per_day)"
    legend_algebraic[80] = "U_Mc_McMa in component Q_Ma (gram_per_day)"
    legend_algebraic[53] = "U_Hc_AmMc in component Q_Hc (mole_per_day)"
    legend_algebraic[57] = "U_Hc_HcVa in component Q_Hc (mole_per_day)"
    legend_states[11] = "Q_Hc in component Q_Hc (mole)"
    legend_algebraic[52] = "P_Hc_FdHc in component Q_Hc (mole_per_day)"
    legend_algebraic[55] = "U_Hc_HcEx in component Q_Hc (mole_per_day)"
    legend_constants[87] = "R_Hc_AmMc in component Q_Hc (dimensionless)"
    legend_constants[88] = "R_Hc_PsMc in component Q_Hc (dimensionless)"
    legend_algebraic[56] = "v_HcVa in component Q_Hc (mole_per_day)"
    legend_constants[89] = "v_HcVa_star in component Q_Hc (mole_per_gram_day)"
    legend_constants[166] = "k_HcEx in component Q_Hc (first_order_rate_constant)"
    legend_constants[90] = "Y_Hc_FdHc in component Q_Hc (dimensionless)"
    legend_constants[91] = "M_Hc_HcVa in component Q_Hc (molar)"
    legend_constants[92] = "J_Am_HcVa in component Q_Hc (molar)"
    legend_constants[93] = "J_Ps_HcVa in component Q_Hc (molar)"
    legend_algebraic[58] = "C_Ma in component Q_Ma (gram_per_litre)"
    legend_algebraic[59] = "P_Ma_AmMa in component Q_Ma (gram_per_day)"
    legend_algebraic[60] = "P_Ma_PsMa in component Q_Ma (gram_per_day)"
    legend_algebraic[81] = "P_Ma_McMa in component Q_Ma (gram_per_day)"
    legend_algebraic[64] = "U_Ma_PoEx in component Q_Ma (gram_per_day)"
    legend_algebraic[6] = "U_Ma_MaEx in component Q_Ma (gram_per_day)"
    legend_constants[177] = "k_MaMd in component Q_Ma (first_order_rate_constant)"
    legend_constants[94] = "Y_Ma_AmMa in component Q_Ma (gram_per_mole)"
    legend_constants[95] = "Y_Ma_PsMa in component Q_Ma (gram_per_mole)"
    legend_constants[96] = "Y_Ma_McMa in component Q_Ma (dimensionless)"
    legend_constants[167] = "k_MaEx in component model_parameters (first_order_rate_constant)"
    legend_constants[175] = "k_PoEx in component model_parameters (first_order_rate_constant)"
    legend_states[12] = "Q_As in component Q_As (gram)"
    legend_algebraic[7] = "C_As in component Q_As (gram_per_litre)"
    legend_algebraic[65] = "P_As_HaAs in component Q_As (gram_per_day)"
    legend_algebraic[70] = "U_As_PoEx in component Q_As (gram_per_day)"
    legend_algebraic[68] = "U_As_AsEx in component Q_As (gram_per_day)"
    legend_constants[168] = "k_AsEx in component Q_As (first_order_rate_constant)"
    legend_constants[178] = "k_AsMd in component Q_As (first_order_rate_constant)"
    legend_constants[97] = "Y_As_HaAs in component Q_As (gram_per_mole)"
    legend_algebraic[69] = "C_Mc in component Q_Mc (gram_per_litre)"
    legend_algebraic[71] = "P_Mc_AmMc in component Q_Mc (gram_per_day)"
    legend_algebraic[72] = "P_Mc_PsMc in component Q_Mc (gram_per_day)"
    legend_algebraic[73] = "U_Mc_McEx in component Q_Mc (gram_per_day)"
    legend_constants[169] = "k_McEx in component Q_Mc (first_order_rate_constant)"
    legend_constants[98] = "Y_Mc_AmMc in component Q_Mc (gram_per_mole)"
    legend_constants[99] = "Y_Mc_PsMc in component Q_Mc (gram_per_mole)"
    legend_algebraic[74] = "v_McEg in component Q_Mc (gram_per_day)"
    legend_constants[100] = "v_McEg_star in component Q_Mc (first_order_rate_constant)"
    legend_constants[101] = "M_Mc_McEg in component Q_Mc (gram_per_litre)"
    legend_states[13] = "Q_Ac in component Q_Ac (mole)"
    legend_algebraic[83] = "C_Ac in component Q_Ac (molar)"
    legend_constants[190] = "P_Ac_InAc in component Q_Ac (mole_per_day)"
    legend_algebraic[159] = "P_Ac_AmMa in component Q_Ac (mole_per_day)"
    legend_algebraic[119] = "P_Ac_AmMc in component Q_Ac (mole_per_day)"
    legend_algebraic[167] = "P_Ac_PsMa in component Q_Ac (mole_per_day)"
    legend_algebraic[131] = "P_Ac_PsMc in component Q_Ac (mole_per_day)"
    legend_algebraic[175] = "P_Ac_HaAs in component Q_Ac (mole_per_day)"
    legend_algebraic[151] = "P_Ac_HaVa in component Q_Ac (mole_per_day)"
    legend_algebraic[87] = "P_Ac_HcVa in component Q_Ac (mole_per_day)"
    legend_algebraic[91] = "P_MaAc_PsAm in component Q_Ac (mole_per_day)"
    legend_algebraic[95] = "P_McAc_PsAm in component Q_Ac (mole_per_day)"
    legend_algebraic[143] = "P_Ac_McMa in component Q_Ac (mole_per_day)"
    legend_algebraic[99] = "P_Ac_McAm in component Q_Ac (mole_per_day)"
    legend_algebraic[103] = "U_Ac_AcAb in component Q_Ac (mole_per_day)"
    legend_algebraic[107] = "U_Ac_AcEx in component Q_Ac (mole_per_day)"
    legend_algebraic[111] = "U_Hf_AmMa in component Q_Ac (mole_per_day)"
    legend_algebraic[115] = "U_Hf_AmMc in component Q_Ac (mole_per_day)"
    legend_algebraic[123] = "U_Hf_PsMa in component Q_Ac (mole_per_day)"
    legend_algebraic[127] = "U_Hf_PsMc in component Q_Ac (mole_per_day)"
    legend_algebraic[135] = "U_Hf_HaAs in component Q_Ac (mole_per_day)"
    legend_algebraic[139] = "U_Hf_McMa in component Q_Ac (mole_per_day)"
    legend_constants[102] = "M_Ac_AcAb in component Q_Ac (molar)"
    legend_constants[199] = "v_AcAb in component Q_Ac (mole_per_day)"
    legend_constants[103] = "v_AcAb_star in component Q_Ac (mole_per_litre_day)"
    legend_constants[191] = "Y_Ac_LaAc in component Q_Ac (dimensionless)"
    legend_algebraic[147] = "Y_Ac_HaVa in component Q_Ac (dimensionless)"
    legend_constants[193] = "Y_Ac_PsVa in component Q_Ac (dimensionless)"
    legend_algebraic[155] = "Y_Ac_AmMa in component Q_Ac (dimensionless)"
    legend_constants[194] = "Y_Ac_AmMc in component Q_Ac (dimensionless)"
    legend_algebraic[163] = "Y_Ac_PsMa in component Q_Ac (dimensionless)"
    legend_constants[195] = "Y_Ac_PsMc in component Q_Ac (dimensionless)"
    legend_algebraic[171] = "Y_Ac_HaAs in component Q_Ac (dimensionless)"
    legend_constants[196] = "Y_Ac_McMa in component Q_Ac (dimensionless)"
    legend_constants[197] = "Y_Ac_PsAm in component Q_Ac (dimensionless)"
    legend_constants[198] = "Y_Ac_McAm in component Q_Ac (dimensionless)"
    legend_constants[104] = "Y_Ac_WrAc in component Q_Ac (dimensionless)"
    legend_constants[105] = "Y_Ac_InAc in component Q_Ac (molar)"
    legend_constants[106] = "Y_Ac_StAc in component Q_Ac (dimensionless)"
    legend_constants[107] = "Y_Ac_CeAc in component Q_Ac (dimensionless)"
    legend_constants[108] = "Y_Ac_HeAc in component Q_Ac (dimensionless)"
    legend_constants[109] = "Y_Ac_PsAc in component Q_Ac (dimensionless)"
    legend_constants[192] = "Y_Ac_HcVa in component Q_Ac (dimensionless)"
    legend_constants[170] = "k_AcEx in component Q_Ac (first_order_rate_constant)"
    legend_constants[110] = "D_Ac in component Q_Ac (litre_per_day)"
    legend_constants[111] = "J_pH_AcAb in component Q_Ac (dimensionless)"
    legend_constants[112] = "phi_pH_AcAb in component Q_Ac (dimensionless)"
    legend_constants[113] = "f_Hf_AmMa in component model_parameters (dimensionless)"
    legend_constants[114] = "f_Hf_AmMc in component model_parameters (dimensionless)"
    legend_constants[115] = "f_Hf_PsMa in component model_parameters (dimensionless)"
    legend_constants[116] = "f_Hf_PsMc in component model_parameters (dimensionless)"
    legend_constants[117] = "f_Hf_HaAs in component model_parameters (dimensionless)"
    legend_constants[118] = "f_Hf_McMa in component model_parameters (dimensionless)"
    legend_constants[119] = "f_Lc_Le in component model_parameters (dimensionless)"
    legend_constants[120] = "f_Ce_Fd in component model_parameters (dimensionless)"
    legend_states[14] = "Q_Pr in component Q_Pr (mole)"
    legend_algebraic[84] = "C_Pr in component Q_Pr (molar)"
    legend_constants[200] = "P_Pr_InPr in component Q_Pr (mole_per_day)"
    legend_algebraic[160] = "P_Pr_AmMa in component Q_Pr (mole_per_day)"
    legend_algebraic[120] = "P_Pr_AmMc in component Q_Pr (mole_per_day)"
    legend_algebraic[168] = "P_Pr_PsMa in component Q_Pr (mole_per_day)"
    legend_algebraic[132] = "P_Pr_PsMc in component Q_Pr (mole_per_day)"
    legend_algebraic[176] = "P_Pr_HaAs in component Q_Pr (mole_per_day)"
    legend_algebraic[152] = "P_Pr_HaVa in component Q_Pr (mole_per_day)"
    legend_algebraic[88] = "P_Pr_HcVa in component Q_Pr (mole_per_day)"
    legend_algebraic[92] = "P_MaPr_PsAm in component Q_Pr (mole_per_day)"
    legend_algebraic[96] = "P_McPr_PsAm in component Q_Pr (mole_per_day)"
    legend_algebraic[144] = "P_Pr_McMa in component Q_Pr (mole_per_day)"
    legend_algebraic[100] = "P_Pr_McAm in component Q_Pr (mole_per_day)"
    legend_algebraic[104] = "U_Pr_PrAb in component Q_Pr (mole_per_day)"
    legend_algebraic[108] = "U_Pr_PrEx in component Q_Pr (mole_per_day)"
    legend_algebraic[112] = "U_Hf_AmMa in component Q_Pr (mole_per_day)"
    legend_algebraic[116] = "U_Hf_AmMc in component Q_Pr (mole_per_day)"
    legend_algebraic[124] = "U_Hf_PsMa in component Q_Pr (mole_per_day)"
    legend_algebraic[128] = "U_Hf_PsMc in component Q_Pr (mole_per_day)"
    legend_algebraic[136] = "U_Hf_HaAs in component Q_Pr (mole_per_day)"
    legend_algebraic[140] = "U_Hf_McMa in component Q_Pr (mole_per_day)"
    legend_constants[121] = "M_Pr_PrAb in component Q_Pr (molar)"
    legend_constants[209] = "v_PrAb in component Q_Pr (mole_per_day)"
    legend_constants[122] = "v_PrAb_star in component Q_Pr (mole_per_litre_day)"
    legend_constants[201] = "Y_Pr_LaPr in component Q_Pr (dimensionless)"
    legend_algebraic[148] = "Y_Pr_HaVa in component Q_Pr (dimensionless)"
    legend_constants[203] = "Y_Pr_PsVa in component Q_Pr (dimensionless)"
    legend_algebraic[156] = "Y_Pr_AmMa in component Q_Pr (dimensionless)"
    legend_constants[204] = "Y_Pr_AmMc in component Q_Pr (dimensionless)"
    legend_algebraic[164] = "Y_Pr_PsMa in component Q_Pr (dimensionless)"
    legend_constants[205] = "Y_Pr_PsMc in component Q_Pr (dimensionless)"
    legend_algebraic[172] = "Y_Pr_HaAs in component Q_Pr (dimensionless)"
    legend_constants[206] = "Y_Pr_McMa in component Q_Pr (dimensionless)"
    legend_constants[207] = "Y_Pr_PsAm in component Q_Pr (dimensionless)"
    legend_constants[208] = "Y_Pr_McAm in component Q_Pr (dimensionless)"
    legend_constants[123] = "Y_Pr_WrPr in component Q_Pr (dimensionless)"
    legend_constants[124] = "Y_Pr_InPr in component Q_Pr (molar)"
    legend_constants[202] = "Y_Pr_HcVa in component Q_Pr (dimensionless)"
    legend_constants[125] = "Y_Pr_StPr in component Q_Pr (dimensionless)"
    legend_constants[126] = "Y_Pr_CePr in component Q_Pr (dimensionless)"
    legend_constants[127] = "Y_Pr_HePr in component Q_Pr (dimensionless)"
    legend_constants[128] = "Y_Pr_PsPr in component Q_Pr (dimensionless)"
    legend_constants[171] = "k_PrEx in component Q_Pr (first_order_rate_constant)"
    legend_constants[129] = "D_Pr in component Q_Pr (litre_per_day)"
    legend_constants[130] = "phi_pH_PrAb in component Q_Pr (dimensionless)"
    legend_constants[131] = "J_pH_PrAb in component Q_Pr (dimensionless)"
    legend_states[15] = "Q_Bu in component Q_Bu (mole)"
    legend_algebraic[85] = "C_Bu in component Q_Bu (molar)"
    legend_constants[210] = "P_Bu_InBu in component Q_Bu (mole_per_day)"
    legend_algebraic[161] = "P_Bu_AmMa in component Q_Bu (mole_per_day)"
    legend_algebraic[121] = "P_Bu_AmMc in component Q_Bu (mole_per_day)"
    legend_algebraic[169] = "P_Bu_PsMa in component Q_Bu (mole_per_day)"
    legend_algebraic[133] = "P_Bu_PsMc in component Q_Bu (mole_per_day)"
    legend_algebraic[177] = "P_Bu_HaAs in component Q_Bu (mole_per_day)"
    legend_algebraic[153] = "P_Bu_HaVa in component Q_Bu (mole_per_day)"
    legend_algebraic[89] = "P_Bu_HcVa in component Q_Bu (mole_per_day)"
    legend_algebraic[93] = "P_MaBu_PsAm in component Q_Bu (mole_per_day)"
    legend_algebraic[97] = "P_McBu_PsAm in component Q_Bu (mole_per_day)"
    legend_algebraic[145] = "P_Bu_McMa in component Q_Bu (mole_per_day)"
    legend_algebraic[101] = "P_Bu_McAm in component Q_Bu (mole_per_day)"
    legend_algebraic[105] = "U_Bu_BuAb in component Q_Bu (mole_per_day)"
    legend_algebraic[109] = "U_Bu_BuEx in component Q_Bu (mole_per_day)"
    legend_algebraic[113] = "U_Hf_AmMa in component Q_Bu (mole_per_day)"
    legend_algebraic[117] = "U_Hf_AmMc in component Q_Bu (mole_per_day)"
    legend_algebraic[125] = "U_Hf_PsMa in component Q_Bu (mole_per_day)"
    legend_algebraic[129] = "U_Hf_PsMc in component Q_Bu (mole_per_day)"
    legend_algebraic[137] = "U_Hf_HaAs in component Q_Bu (mole_per_day)"
    legend_algebraic[141] = "U_Hf_McMa in component Q_Bu (mole_per_day)"
    legend_constants[132] = "M_Bu_BuAb in component Q_Bu (molar)"
    legend_constants[219] = "v_BuAb in component Q_Bu (mole_per_day)"
    legend_constants[133] = "v_BuAb_star in component Q_Bu (mole_per_litre_day)"
    legend_constants[211] = "Y_Bu_LaBu in component Q_Bu (dimensionless)"
    legend_algebraic[149] = "Y_Bu_HaVa in component Q_Bu (dimensionless)"
    legend_constants[213] = "Y_Bu_PsVa in component Q_Bu (dimensionless)"
    legend_algebraic[157] = "Y_Bu_AmMa in component Q_Bu (dimensionless)"
    legend_constants[214] = "Y_Bu_AmMc in component Q_Bu (dimensionless)"
    legend_algebraic[165] = "Y_Bu_PsMa in component Q_Bu (dimensionless)"
    legend_constants[215] = "Y_Bu_PsMc in component Q_Bu (dimensionless)"
    legend_algebraic[173] = "Y_Bu_HaAs in component Q_Bu (dimensionless)"
    legend_constants[216] = "Y_Bu_McMa in component Q_Bu (dimensionless)"
    legend_constants[217] = "Y_Bu_PsAm in component Q_Bu (dimensionless)"
    legend_constants[218] = "Y_Bu_McAm in component Q_Bu (dimensionless)"
    legend_constants[134] = "Y_Bu_WrBu in component Q_Bu (dimensionless)"
    legend_constants[135] = "Y_Bu_InBu in component Q_Bu (molar)"
    legend_constants[212] = "Y_Bu_HcVa in component Q_Bu (dimensionless)"
    legend_constants[136] = "Y_Bu_StBu in component Q_Bu (dimensionless)"
    legend_constants[137] = "Y_Bu_CeBu in component Q_Bu (dimensionless)"
    legend_constants[138] = "Y_Bu_HeBu in component Q_Bu (dimensionless)"
    legend_constants[139] = "Y_Bu_PsBu in component Q_Bu (dimensionless)"
    legend_constants[172] = "k_BuEx in component Q_Bu (first_order_rate_constant)"
    legend_constants[140] = "D_Bu in component Q_Bu (litre_per_day)"
    legend_constants[141] = "phi_pH_BuAb in component Q_Bu (dimensionless)"
    legend_constants[142] = "J_pH_BuAb in component Q_Bu (dimensionless)"
    legend_states[16] = "Q_Vl in component Q_Vl (mole)"
    legend_algebraic[86] = "C_Vl in component Q_Vl (molar)"
    legend_constants[220] = "P_Vl_InVl in component Q_Vl (mole_per_day)"
    legend_algebraic[162] = "P_Vl_AmMa in component Q_Vl (mole_per_day)"
    legend_algebraic[122] = "P_Vl_AmMc in component Q_Vl (mole_per_day)"
    legend_algebraic[170] = "P_Vl_PsMa in component Q_Vl (mole_per_day)"
    legend_algebraic[134] = "P_Vl_PsMc in component Q_Vl (mole_per_day)"
    legend_algebraic[178] = "P_Vl_HaAs in component Q_Vl (mole_per_day)"
    legend_algebraic[154] = "P_Vl_HaVa in component Q_Vl (mole_per_day)"
    legend_algebraic[90] = "P_Vl_HcVa in component Q_Vl (mole_per_day)"
    legend_algebraic[94] = "P_MaVl_PsAm in component Q_Vl (mole_per_day)"
    legend_algebraic[98] = "P_McVl_PsAm in component Q_Vl (mole_per_day)"
    legend_algebraic[146] = "P_Vl_McMa in component Q_Vl (mole_per_day)"
    legend_algebraic[102] = "P_Vl_McAm in component Q_Vl (mole_per_day)"
    legend_algebraic[106] = "U_Vl_VlAb in component Q_Vl (mole_per_day)"
    legend_algebraic[110] = "U_Vl_VlEx in component Q_Vl (mole_per_day)"
    legend_algebraic[114] = "U_Hf_AmMa in component Q_Vl (mole_per_day)"
    legend_algebraic[118] = "U_Hf_AmMc in component Q_Vl (mole_per_day)"
    legend_algebraic[126] = "U_Hf_PsMa in component Q_Vl (mole_per_day)"
    legend_algebraic[130] = "U_Hf_PsMc in component Q_Vl (mole_per_day)"
    legend_algebraic[138] = "U_Hf_HaAs in component Q_Vl (mole_per_day)"
    legend_algebraic[142] = "U_Hf_McMa in component Q_Vl (mole_per_day)"
    legend_constants[143] = "M_Vl_VlAb in component Q_Vl (molar)"
    legend_constants[229] = "v_VlAb in component Q_Vl (mole_per_day)"
    legend_constants[144] = "v_VlAb_star in component Q_Vl (mole_per_litre_day)"
    legend_constants[221] = "Y_Vl_LaVl in component Q_Vl (dimensionless)"
    legend_algebraic[150] = "Y_Vl_HaVa in component Q_Vl (dimensionless)"
    legend_constants[223] = "Y_Vl_PsVa in component Q_Vl (dimensionless)"
    legend_algebraic[158] = "Y_Vl_AmMa in component Q_Vl (dimensionless)"
    legend_constants[224] = "Y_Vl_AmMc in component Q_Vl (dimensionless)"
    legend_algebraic[166] = "Y_Vl_PsMa in component Q_Vl (dimensionless)"
    legend_constants[225] = "Y_Vl_PsMc in component Q_Vl (dimensionless)"
    legend_algebraic[174] = "Y_Vl_HaAs in component Q_Vl (dimensionless)"
    legend_constants[226] = "Y_Vl_McMa in component Q_Vl (dimensionless)"
    legend_constants[227] = "Y_Vl_PsAm in component Q_Vl (dimensionless)"
    legend_constants[228] = "Y_Vl_McAm in component Q_Vl (dimensionless)"
    legend_constants[145] = "Y_Vl_WrVl in component Q_Vl (dimensionless)"
    legend_constants[146] = "Y_Vl_InVl in component Q_Vl (molar)"
    legend_constants[222] = "Y_Vl_HcVa in component Q_Vl (dimensionless)"
    legend_constants[147] = "Y_Vl_StVl in component Q_Vl (dimensionless)"
    legend_constants[148] = "Y_Vl_CeVl in component Q_Vl (dimensionless)"
    legend_constants[149] = "Y_Vl_HeVl in component Q_Vl (dimensionless)"
    legend_constants[150] = "Y_Vl_PsVl in component Q_Vl (dimensionless)"
    legend_constants[173] = "k_VlEx in component Q_Vl (first_order_rate_constant)"
    legend_constants[151] = "D_Vl in component Q_Vl (litre_per_day)"
    legend_constants[152] = "phi_pH_VlAb in component Q_Vl (dimensionless)"
    legend_constants[153] = "J_pH_VlAb in component Q_Vl (dimensionless)"
    legend_rates[0] = "d/dt Q_Pd in component Q_Pd (mole)"
    legend_rates[3] = "d/dt Q_Ps in component Q_Ps (mole)"
    legend_rates[4] = "d/dt Q_Pu in component Q_Pu (mole)"
    legend_rates[5] = "d/dt Q_Am in component Q_Am (mole)"
    legend_rates[6] = "d/dt Q_Li in component Q_Li (mole)"
    legend_rates[7] = "d/dt Q_Sd in component Q_Sd (mole)"
    legend_rates[8] = "d/dt Q_Fd in component Q_Fd (mole)"
    legend_rates[9] = "d/dt Q_Fu in component Q_Fu (mole)"
    legend_rates[10] = "d/dt Q_Ha in component Q_Ha (mole)"
    legend_rates[11] = "d/dt Q_Hc in component Q_Hc (mole)"
    legend_rates[1] = "d/dt Q_Ma in component Q_Ma (gram)"
    legend_rates[12] = "d/dt Q_As in component Q_As (gram)"
    legend_rates[2] = "d/dt Q_Mc in component Q_Mc (gram)"
    legend_rates[13] = "d/dt Q_Ac in component Q_Ac (mole)"
    legend_rates[14] = "d/dt Q_Pr in component Q_Pr (mole)"
    legend_rates[15] = "d/dt Q_Bu in component Q_Bu (mole)"
    legend_rates[16] = "d/dt Q_Vl in component Q_Vl (mole)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 1.000
    constants[0] = 0.0576
    constants[1] = 0.264
    constants[2] = 0.0091
    constants[3] = 1.000
    constants[4] = 1.000
    constants[5] = 0.66
    states[1] = 1.000
    states[2] = 1.000
    constants[6] = 1.000
    constants[7] = 1.000
    constants[8] = 0.0248
    states[3] = 1.000
    constants[9] = 0.0144
    constants[10] = 0.0576
    constants[11] = 0.0576
    constants[12] = 0.0091
    constants[13] = 0.0010
    constants[14] = 1.0
    constants[15] = 0.0067
    constants[16] = 0.0067
    constants[17] = 1.000
    constants[18] = 0.0289
    constants[19] = 0.0224
    constants[20] = 0.0224
    constants[21] = 0.0248
    constants[22] = 0.0248
    constants[23] = 0.0165
    constants[24] = 0.0165
    constants[25] = 1.000
    constants[26] = 0.0165
    states[4] = 1.000
    constants[27] = 0.0091
    constants[28] = 1.000
    states[5] = 1.000
    constants[29] = 0.00165
    constants[30] = 1.10
    constants[31] = 0.0528
    constants[32] = 0.0528
    constants[33] = 0.0588
    constants[34] = 2.0
    constants[35] = 1.257
    constants[36] = 0.0084
    constants[37] = 0.00135
    constants[38] = 0.00135
    constants[39] = 0.0132
    constants[40] = 7.5
    constants[41] = 7.85
    constants[42] = 0.0159
    constants[43] = 0.0159
    constants[44] = 0.00621
    constants[45] = 1.000
    constants[46] = 7.000
    constants[47] = 0.35
    constants[48] = 1.000
    states[6] = 1.000
    constants[49] = 0.0015
    constants[50] = 0.00021
    constants[51] = 1.000
    states[7] = 1.000
    constants[52] = 0.0062
    constants[53] = 1.000
    constants[54] = 0.2179
    constants[55] = 0.416
    constants[56] = 1.000
    constants[57] = 1.04
    states[8] = 1.000
    constants[58] = 0.0062
    constants[59] = 1.000
    constants[60] = 0.1646
    constants[61] = 0.332
    constants[62] = 1.000
    constants[63] = 0.83
    constants[64] = 22.9
    constants[65] = 5.97
    constants[66] = 1.000
    constants[67] = 1.000
    states[9] = 1.000
    constants[68] = 0.0062
    constants[69] = 1.000
    states[10] = 1.000
    constants[70] = 1.793
    constants[71] = 1.291
    constants[72] = 0.0086
    constants[73] = 0.0268
    constants[74] = 0.055
    constants[75] = 0.053
    constants[76] = 0.1646
    constants[77] = 0.0062
    constants[78] = 0.0062
    constants[79] = 0.0025
    constants[80] = 1.0
    constants[81] = 0.0062
    constants[82] = 1.000
    constants[83] = 1.000
    constants[84] = 1.000
    constants[85] = 0.00861
    constants[86] = 0.01465
    states[11] = 1.000
    constants[87] = 1.793
    constants[88] = 1.291
    constants[89] = 0.1646
    constants[90] = 1.0
    constants[91] = 0.055
    constants[92] = 0.00861
    constants[93] = 0.01465
    constants[94] = 118.91
    constants[95] = 149.48
    constants[96] = 149.48
    states[12] = 1.000
    constants[97] = 112.5
    constants[98] = 118.91
    constants[99] = 149.48
    constants[100] = 15.439
    constants[101] = 34.694
    states[13] = 1.000
    constants[102] = 0.338
    constants[103] = 7.86
    constants[104] = 1.000
    constants[105] = 0.0167
    constants[106] = 1.000
    constants[107] = 1.000
    constants[108] = 1.000
    constants[109] = 1.000
    constants[110] = 1.000
    constants[111] = 6.45
    constants[112] = 6.48
    constants[113] = 0.526
    constants[114] = 0.526
    constants[115] = 0.711
    constants[116] = 0.711
    constants[117] = 0.306
    constants[118] = 0.711
    constants[119] = 2.250
    constants[120] = 1.000
    states[14] = 1.000
    constants[121] = 0.338
    constants[122] = 7.86
    constants[123] = 1.000
    constants[124] = 0.0135
    constants[125] = 1.000
    constants[126] = 1.000
    constants[127] = 1.000
    constants[128] = 1.000
    constants[129] = 1.000
    constants[130] = 6.48
    constants[131] = 6.45
    states[15] = 1.000
    constants[132] = 0.338
    constants[133] = 7.86
    constants[134] = 1.000
    constants[135] = 0.0114
    constants[136] = 1.000
    constants[137] = 1.000
    constants[138] = 1.000
    constants[139] = 1.000
    constants[140] = 1.000
    constants[141] = 6.48
    constants[142] = 6.45
    states[16] = 1.000
    constants[143] = 0.338
    constants[144] = 7.86
    constants[145] = 1.000
    constants[146] = 0.0098
    constants[147] = 1.000
    constants[148] = 1.000
    constants[149] = 1.000
    constants[150] = 1.000
    constants[151] = 1.000
    constants[152] = 6.48
    constants[153] = 6.45
    constants[154] = constants[7]
    constants[155] = constants[2]*constants[3]
    constants[156] = constants[25]
    constants[157] = constants[27]*constants[28]
    constants[158] = constants[7]
    constants[159] = constants[25]
    constants[160] = constants[25]
    constants[161] = constants[7]
    constants[162] = constants[7]
    constants[163] = constants[68]*constants[69]
    constants[164] = constants[7]
    constants[165] = constants[25]
    constants[166] = constants[25]
    constants[167] = constants[25]
    constants[168] = constants[25]
    constants[169] = constants[7]
    constants[170] = constants[25]
    constants[171] = constants[25]
    constants[172] = constants[25]
    constants[173] = constants[25]
    constants[174] = constants[1]*(constants[4]/constants[5])
    constants[175] = constants[7]/2.00000
    constants[176] = constants[12]*constants[17]
    constants[177] = constants[167]-constants[175]
    constants[178] = constants[167]-constants[175]
    constants[179] = constants[13]*constants[17]
    constants[180] = constants[33]*constants[45]
    constants[181] = constants[30]*(power(1.00000, 0.250000))*(power(constants[6], 0.750000))*(1.00000+power(constants[40]/constants[46], constants[41]))
    constants[182] = constants[49]*constants[51]
    constants[183] = constants[52]*constants[53]
    constants[184] = constants[55]*(constants[56]/constants[57])
    constants[185] = constants[58]*constants[59]
    constants[186] = constants[61]*(constants[62]/constants[63])
    constants[187] = constants[77]*constants[82]
    constants[188] = constants[78]*constants[83]
    constants[189] = constants[79]*constants[84]
    constants[190] = constants[105]*constants[110]
    constants[191] = constants[119]*constants[104]
    constants[192] = constants[120]*constants[107]+(1.00000-constants[120])*constants[108]
    constants[193] = constants[109]
    constants[194] = constants[192]
    constants[195] = constants[192]
    constants[196] = constants[192]
    constants[197] = constants[193]
    constants[198] = constants[193]
    constants[199] = constants[103]*(power(1.00000, 0.250000))*((power(constants[6], 0.750000))/(1.00000+power(constants[46]/constants[111], constants[112])))
    constants[200] = constants[124]*constants[129]
    constants[201] = constants[119]*constants[123]
    constants[202] = constants[120]*constants[126]+(1.00000-constants[120])*constants[127]
    constants[203] = constants[128]
    constants[204] = constants[202]
    constants[205] = constants[202]
    constants[206] = constants[202]
    constants[207] = constants[203]
    constants[208] = constants[203]
    constants[209] = constants[122]*(power(1.00000, 0.250000))*((power(constants[6], 0.750000))/(1.00000+power(constants[46]/constants[131], constants[130])))
    constants[210] = constants[135]*constants[140]
    constants[211] = constants[119]*constants[134]
    constants[212] = constants[120]*constants[137]+(1.00000-constants[120])*constants[138]
    constants[213] = constants[139]
    constants[214] = constants[212]
    constants[215] = constants[212]
    constants[216] = constants[212]
    constants[217] = constants[213]
    constants[218] = constants[213]
    constants[219] = constants[133]*(power(1.00000, 0.250000))*((power(constants[6], 0.750000))/(1.00000+power(constants[46]/constants[142], constants[141])))
    constants[220] = constants[146]*constants[151]
    constants[221] = constants[119]*constants[145]
    constants[222] = constants[120]*constants[148]+(1.00000-constants[120])*constants[149]
    constants[223] = constants[150]
    constants[224] = constants[222]
    constants[225] = constants[222]
    constants[226] = constants[222]
    constants[227] = constants[223]
    constants[228] = constants[223]
    constants[229] = constants[144]*(power(1.00000, 0.250000))*((power(constants[6], 0.750000))/(1.00000+power(constants[46]/constants[153], constants[152])))
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[2] = constants[158]*states[4]
    rates[4] = constants[157]-algebraic[2]
    algebraic[5] = constants[164]*states[9]
    rates[9] = constants[163]-algebraic[5]
    algebraic[0] = states[0]/constants[6]
    algebraic[9] = constants[0]*(states[1]+states[2])
    algebraic[10] = algebraic[9]/(1.00000+constants[174]/algebraic[0])
    algebraic[8] = constants[154]*states[0]
    rates[0] = constants[155]-(algebraic[10]+algebraic[8])
    algebraic[26] = states[7]/constants[6]
    algebraic[28] = constants[54]*states[1]
    algebraic[29] = algebraic[28]/(1.00000+constants[184]/algebraic[26])
    algebraic[27] = constants[161]*states[7]
    rates[7] = constants[183]-(algebraic[29]+algebraic[27])
    algebraic[30] = states[8]/constants[6]
    algebraic[32] = constants[60]*states[2]*((1.00000-(voi*constants[67])/1.00000)+((voi*constants[67])/1.00000)/(1.00000+power(constants[65]/constants[66], constants[64])))
    algebraic[33] = algebraic[32]/(1.00000+constants[186]/algebraic[30])
    algebraic[31] = constants[162]*states[8]
    rates[8] = constants[185]-(algebraic[33]+algebraic[31])
    algebraic[11] = states[3]/constants[6]
    algebraic[17] = constants[11]*states[2]
    algebraic[47] = states[11]/constants[6]
    algebraic[49] = algebraic[17]/(1.00000+constants[20]/algebraic[11]+constants[22]/algebraic[47])
    algebraic[54] = constants[88]*algebraic[49]
    algebraic[18] = states[5]/constants[6]
    algebraic[24] = constants[32]*states[2]
    algebraic[51] = algebraic[24]/(1.00000+constants[38]/algebraic[18]+constants[43]/algebraic[47])
    algebraic[53] = constants[87]*algebraic[51]
    algebraic[56] = constants[89]*states[2]
    algebraic[57] = algebraic[56]/((1.00000+constants[91]/algebraic[47])*(1.00000+algebraic[18]/constants[92]+algebraic[11]/constants[93]))
    algebraic[52] = constants[90]*algebraic[33]
    algebraic[55] = constants[166]*states[11]
    rates[11] = algebraic[52]-(algebraic[53]+algebraic[54]+algebraic[57]+algebraic[55])
    algebraic[61] = constants[177]*states[1]*constants[47]
    algebraic[63] = constants[50]*algebraic[61]
    algebraic[25] = constants[160]*states[6]
    rates[6] = (constants[182]+algebraic[63])-algebraic[25]
    algebraic[66] = constants[178]*states[12]*constants[47]
    algebraic[34] = states[10]/constants[6]
    algebraic[43] = constants[75]*states[1]
    algebraic[44] = algebraic[43]/(1.00000+constants[73]/algebraic[34])
    algebraic[65] = constants[97]*algebraic[44]
    algebraic[70] = constants[175]*states[12]*constants[47]
    algebraic[68] = constants[168]*states[12]*(1.00000-constants[47])
    rates[12] = algebraic[65]-(algebraic[66]+algebraic[68]+algebraic[70])
    algebraic[58] = states[1]/constants[6]
    algebraic[69] = states[2]/constants[6]
    algebraic[74] = (constants[100]*states[1]*constants[47]*algebraic[69])/(algebraic[69]+algebraic[58]*(1.00000-constants[47]))
    algebraic[75] = algebraic[74]/(1.00000+constants[101]/(algebraic[69]+algebraic[58]*(1.00000-constants[47])))
    algebraic[71] = constants[98]*algebraic[51]
    algebraic[72] = constants[99]*algebraic[49]
    algebraic[73] = constants[169]*states[2]
    rates[2] = (algebraic[71]+algebraic[72])-(algebraic[75]+algebraic[73])
    algebraic[15] = constants[9]*states[2]
    algebraic[48] = algebraic[15]/(1.00000+constants[18]/algebraic[11]+algebraic[47]/constants[24])
    algebraic[16] = constants[10]*states[1]
    algebraic[36] = algebraic[16]/(1.00000+constants[19]/algebraic[11]+constants[21]/algebraic[34])
    algebraic[14] = constants[9]*states[1]
    algebraic[35] = algebraic[14]/(1.00000+constants[18]/algebraic[11]+algebraic[34]/constants[23])
    algebraic[12] = constants[14]*algebraic[10]
    algebraic[62] = constants[15]*algebraic[61]
    algebraic[76] = algebraic[75]*(1.00000-(1.00000/(1.00000+algebraic[34]/constants[26])+1.00000/(1.00000+constants[8]/algebraic[34])))
    algebraic[78] = constants[16]*algebraic[76]
    algebraic[13] = constants[156]*states[3]
    rates[3] = (constants[176]+algebraic[12]+algebraic[62]+constants[179]+algebraic[78])-(algebraic[35]+algebraic[48]+algebraic[36]+algebraic[49]+algebraic[13])
    algebraic[23] = constants[31]*states[1]*(1.00000-constants[47])
    algebraic[38] = algebraic[23]/(1.00000+constants[37]/algebraic[18]+constants[42]/algebraic[34])
    algebraic[21] = constants[29]*constants[6]*(constants[48]/(1.00000+algebraic[18]/constants[44]))
    algebraic[22] = constants[34]*algebraic[21]
    algebraic[37] = constants[35]*algebraic[35]
    algebraic[50] = constants[35]*algebraic[48]
    algebraic[77] = (1.00000*algebraic[75])/(1.00000+algebraic[34]/constants[26])
    algebraic[79] = constants[36]*algebraic[77]
    algebraic[19] = constants[181]/(1.00000+constants[39]/algebraic[18])
    algebraic[20] = constants[159]*states[5]
    rates[5] = (constants[180]+algebraic[37]+algebraic[50]+algebraic[22]+algebraic[79])-(algebraic[19]+algebraic[38]+algebraic[51]+algebraic[20])
    algebraic[80] = algebraic[75]/(1.00000+constants[8]/algebraic[34])
    algebraic[82] = constants[72]*algebraic[80]
    algebraic[40] = constants[70]*algebraic[38]
    algebraic[41] = constants[71]*algebraic[36]
    algebraic[45] = constants[76]*states[1]
    algebraic[46] = algebraic[45]*((1.00000-constants[47])/((1.00000+constants[74]/algebraic[34])*(1.00000+algebraic[18]/constants[85])*(algebraic[11]/constants[86])))+(algebraic[45]*constants[47])/(1.00000+constants[74]/algebraic[34])
    algebraic[39] = constants[80]*algebraic[29]
    algebraic[67] = constants[81]*algebraic[66]
    algebraic[42] = constants[165]*states[10]
    rates[10] = (constants[187]+constants[188]+algebraic[39]+algebraic[67]+constants[189])-(algebraic[40]+algebraic[41]+algebraic[82]+algebraic[44]+algebraic[46]+algebraic[42])
    algebraic[59] = constants[94]*algebraic[38]
    algebraic[60] = constants[95]*algebraic[36]
    algebraic[81] = constants[96]*algebraic[80]
    algebraic[64] = constants[175]*states[1]*constants[47]
    rates[1] = (algebraic[59]+algebraic[60]+algebraic[81])-(algebraic[61]+algebraic[80]+algebraic[64])
    algebraic[111] = constants[113]*algebraic[40]
    algebraic[147] = (constants[104]*constants[187]+constants[191]*constants[189]+constants[106]*(constants[188]+algebraic[39]+algebraic[67]))/(constants[187]+constants[189]+constants[188]+algebraic[39]+algebraic[67])
    algebraic[155] = algebraic[147]
    algebraic[159] = algebraic[155]*algebraic[111]
    algebraic[115] = constants[114]*algebraic[53]
    algebraic[119] = constants[194]*algebraic[115]
    algebraic[123] = constants[115]*algebraic[41]
    algebraic[163] = algebraic[147]
    algebraic[167] = algebraic[163]*algebraic[123]
    algebraic[127] = constants[116]*algebraic[54]
    algebraic[131] = constants[195]*algebraic[127]
    algebraic[135] = constants[117]*algebraic[44]
    algebraic[171] = algebraic[147]
    algebraic[175] = algebraic[171]*algebraic[135]
    algebraic[151] = algebraic[147]*algebraic[46]
    algebraic[87] = constants[192]*algebraic[57]
    algebraic[91] = constants[197]*algebraic[35]
    algebraic[95] = constants[197]*algebraic[48]
    algebraic[139] = constants[118]*algebraic[82]
    algebraic[143] = constants[196]*algebraic[139]
    algebraic[99] = constants[198]*algebraic[77]
    algebraic[83] = states[13]/constants[6]
    algebraic[103] = constants[199]/(1.00000+constants[102]/algebraic[83])
    algebraic[107] = constants[170]*states[13]
    rates[13] = (constants[190]+algebraic[159]+algebraic[119]+algebraic[167]+algebraic[131]+algebraic[175]+algebraic[151]+algebraic[87]+algebraic[91]+algebraic[95]+algebraic[143]+algebraic[99])-(algebraic[103]+algebraic[107])
    algebraic[112] = constants[113]*algebraic[40]
    algebraic[148] = (constants[123]*constants[187]+constants[201]*constants[189]+constants[125]*(constants[188]+algebraic[39]+algebraic[67]))/(constants[187]+constants[189]+constants[188]+algebraic[39]+algebraic[67])
    algebraic[156] = algebraic[148]
    algebraic[160] = algebraic[156]*algebraic[112]
    algebraic[116] = constants[114]*algebraic[53]
    algebraic[120] = constants[204]*algebraic[116]
    algebraic[124] = constants[115]*algebraic[41]
    algebraic[164] = algebraic[148]
    algebraic[168] = algebraic[164]*algebraic[124]
    algebraic[128] = constants[116]*algebraic[54]
    algebraic[132] = constants[205]*algebraic[128]
    algebraic[136] = constants[117]*algebraic[44]
    algebraic[172] = algebraic[148]
    algebraic[176] = algebraic[172]*algebraic[136]
    algebraic[152] = algebraic[148]*algebraic[46]
    algebraic[88] = constants[202]*algebraic[57]
    algebraic[92] = constants[207]*algebraic[35]
    algebraic[96] = constants[207]*algebraic[48]
    algebraic[140] = constants[118]*algebraic[82]
    algebraic[144] = constants[206]*algebraic[140]
    algebraic[100] = constants[208]*algebraic[77]
    algebraic[84] = states[14]/constants[6]
    algebraic[104] = constants[209]/(1.00000+constants[121]/algebraic[84])
    algebraic[108] = constants[171]*states[14]
    rates[14] = (constants[200]+algebraic[160]+algebraic[120]+algebraic[168]+algebraic[132]+algebraic[176]+algebraic[152]+algebraic[88]+algebraic[92]+algebraic[96]+algebraic[144]+algebraic[100])-(algebraic[104]+algebraic[108])
    algebraic[113] = constants[113]*algebraic[40]
    algebraic[149] = (constants[134]*constants[187]+constants[211]*constants[189]+constants[136]*(constants[188]+algebraic[39]+algebraic[67]))/(constants[187]+constants[189]+constants[188]+algebraic[39]+algebraic[67])
    algebraic[157] = algebraic[149]
    algebraic[161] = algebraic[157]*algebraic[113]
    algebraic[117] = constants[114]*algebraic[53]
    algebraic[121] = constants[214]*algebraic[117]
    algebraic[125] = constants[115]*algebraic[41]
    algebraic[165] = algebraic[149]
    algebraic[169] = algebraic[165]*algebraic[125]
    algebraic[129] = constants[116]*algebraic[54]
    algebraic[133] = constants[215]*algebraic[129]
    algebraic[137] = constants[117]*algebraic[44]
    algebraic[173] = algebraic[149]
    algebraic[177] = algebraic[173]*algebraic[137]
    algebraic[153] = algebraic[149]*algebraic[46]
    algebraic[89] = constants[212]*algebraic[57]
    algebraic[93] = constants[217]*algebraic[35]
    algebraic[97] = constants[217]*algebraic[48]
    algebraic[141] = constants[118]*algebraic[82]
    algebraic[145] = constants[216]*algebraic[141]
    algebraic[101] = constants[218]*algebraic[77]
    algebraic[85] = states[15]/constants[6]
    algebraic[105] = constants[219]/(1.00000+constants[132]/algebraic[85])
    algebraic[109] = constants[172]*states[15]
    rates[15] = (constants[210]+algebraic[161]+algebraic[121]+algebraic[169]+algebraic[133]+algebraic[177]+algebraic[153]+algebraic[89]+algebraic[93]+algebraic[97]+algebraic[145]+algebraic[101])-(algebraic[105]+algebraic[109])
    algebraic[114] = constants[113]*algebraic[40]
    algebraic[150] = (constants[145]*constants[187]+constants[221]*constants[189]+constants[147]*(constants[188]+algebraic[39]+algebraic[67]))/(constants[187]+constants[189]+constants[188]+algebraic[39]+algebraic[67])
    algebraic[158] = algebraic[150]
    algebraic[162] = algebraic[158]*algebraic[114]
    algebraic[118] = constants[114]*algebraic[53]
    algebraic[122] = constants[224]*algebraic[118]
    algebraic[126] = constants[115]*algebraic[41]
    algebraic[166] = algebraic[150]
    algebraic[170] = algebraic[166]*algebraic[126]
    algebraic[130] = constants[116]*algebraic[54]
    algebraic[134] = constants[225]*algebraic[130]
    algebraic[138] = constants[117]*algebraic[44]
    algebraic[174] = algebraic[150]
    algebraic[178] = algebraic[174]*algebraic[138]
    algebraic[154] = algebraic[150]*algebraic[46]
    algebraic[90] = constants[222]*algebraic[57]
    algebraic[94] = constants[227]*algebraic[35]
    algebraic[98] = constants[227]*algebraic[48]
    algebraic[142] = constants[118]*algebraic[82]
    algebraic[146] = constants[226]*algebraic[142]
    algebraic[102] = constants[228]*algebraic[77]
    algebraic[86] = states[16]/constants[6]
    algebraic[106] = constants[229]/(1.00000+constants[143]/algebraic[86])
    algebraic[110] = constants[173]*states[16]
    rates[16] = (constants[220]+algebraic[162]+algebraic[122]+algebraic[170]+algebraic[134]+algebraic[178]+algebraic[154]+algebraic[90]+algebraic[94]+algebraic[98]+algebraic[146]+algebraic[102])-(algebraic[106]+algebraic[110])
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[2] = constants[158]*states[4]
    algebraic[5] = constants[164]*states[9]
    algebraic[0] = states[0]/constants[6]
    algebraic[9] = constants[0]*(states[1]+states[2])
    algebraic[10] = algebraic[9]/(1.00000+constants[174]/algebraic[0])
    algebraic[8] = constants[154]*states[0]
    algebraic[26] = states[7]/constants[6]
    algebraic[28] = constants[54]*states[1]
    algebraic[29] = algebraic[28]/(1.00000+constants[184]/algebraic[26])
    algebraic[27] = constants[161]*states[7]
    algebraic[30] = states[8]/constants[6]
    algebraic[32] = constants[60]*states[2]*((1.00000-(voi*constants[67])/1.00000)+((voi*constants[67])/1.00000)/(1.00000+power(constants[65]/constants[66], constants[64])))
    algebraic[33] = algebraic[32]/(1.00000+constants[186]/algebraic[30])
    algebraic[31] = constants[162]*states[8]
    algebraic[11] = states[3]/constants[6]
    algebraic[17] = constants[11]*states[2]
    algebraic[47] = states[11]/constants[6]
    algebraic[49] = algebraic[17]/(1.00000+constants[20]/algebraic[11]+constants[22]/algebraic[47])
    algebraic[54] = constants[88]*algebraic[49]
    algebraic[18] = states[5]/constants[6]
    algebraic[24] = constants[32]*states[2]
    algebraic[51] = algebraic[24]/(1.00000+constants[38]/algebraic[18]+constants[43]/algebraic[47])
    algebraic[53] = constants[87]*algebraic[51]
    algebraic[56] = constants[89]*states[2]
    algebraic[57] = algebraic[56]/((1.00000+constants[91]/algebraic[47])*(1.00000+algebraic[18]/constants[92]+algebraic[11]/constants[93]))
    algebraic[52] = constants[90]*algebraic[33]
    algebraic[55] = constants[166]*states[11]
    algebraic[61] = constants[177]*states[1]*constants[47]
    algebraic[63] = constants[50]*algebraic[61]
    algebraic[25] = constants[160]*states[6]
    algebraic[66] = constants[178]*states[12]*constants[47]
    algebraic[34] = states[10]/constants[6]
    algebraic[43] = constants[75]*states[1]
    algebraic[44] = algebraic[43]/(1.00000+constants[73]/algebraic[34])
    algebraic[65] = constants[97]*algebraic[44]
    algebraic[70] = constants[175]*states[12]*constants[47]
    algebraic[68] = constants[168]*states[12]*(1.00000-constants[47])
    algebraic[58] = states[1]/constants[6]
    algebraic[69] = states[2]/constants[6]
    algebraic[74] = (constants[100]*states[1]*constants[47]*algebraic[69])/(algebraic[69]+algebraic[58]*(1.00000-constants[47]))
    algebraic[75] = algebraic[74]/(1.00000+constants[101]/(algebraic[69]+algebraic[58]*(1.00000-constants[47])))
    algebraic[71] = constants[98]*algebraic[51]
    algebraic[72] = constants[99]*algebraic[49]
    algebraic[73] = constants[169]*states[2]
    algebraic[15] = constants[9]*states[2]
    algebraic[48] = algebraic[15]/(1.00000+constants[18]/algebraic[11]+algebraic[47]/constants[24])
    algebraic[16] = constants[10]*states[1]
    algebraic[36] = algebraic[16]/(1.00000+constants[19]/algebraic[11]+constants[21]/algebraic[34])
    algebraic[14] = constants[9]*states[1]
    algebraic[35] = algebraic[14]/(1.00000+constants[18]/algebraic[11]+algebraic[34]/constants[23])
    algebraic[12] = constants[14]*algebraic[10]
    algebraic[62] = constants[15]*algebraic[61]
    algebraic[76] = algebraic[75]*(1.00000-(1.00000/(1.00000+algebraic[34]/constants[26])+1.00000/(1.00000+constants[8]/algebraic[34])))
    algebraic[78] = constants[16]*algebraic[76]
    algebraic[13] = constants[156]*states[3]
    algebraic[23] = constants[31]*states[1]*(1.00000-constants[47])
    algebraic[38] = algebraic[23]/(1.00000+constants[37]/algebraic[18]+constants[42]/algebraic[34])
    algebraic[21] = constants[29]*constants[6]*(constants[48]/(1.00000+algebraic[18]/constants[44]))
    algebraic[22] = constants[34]*algebraic[21]
    algebraic[37] = constants[35]*algebraic[35]
    algebraic[50] = constants[35]*algebraic[48]
    algebraic[77] = (1.00000*algebraic[75])/(1.00000+algebraic[34]/constants[26])
    algebraic[79] = constants[36]*algebraic[77]
    algebraic[19] = constants[181]/(1.00000+constants[39]/algebraic[18])
    algebraic[20] = constants[159]*states[5]
    algebraic[80] = algebraic[75]/(1.00000+constants[8]/algebraic[34])
    algebraic[82] = constants[72]*algebraic[80]
    algebraic[40] = constants[70]*algebraic[38]
    algebraic[41] = constants[71]*algebraic[36]
    algebraic[45] = constants[76]*states[1]
    algebraic[46] = algebraic[45]*((1.00000-constants[47])/((1.00000+constants[74]/algebraic[34])*(1.00000+algebraic[18]/constants[85])*(algebraic[11]/constants[86])))+(algebraic[45]*constants[47])/(1.00000+constants[74]/algebraic[34])
    algebraic[39] = constants[80]*algebraic[29]
    algebraic[67] = constants[81]*algebraic[66]
    algebraic[42] = constants[165]*states[10]
    algebraic[59] = constants[94]*algebraic[38]
    algebraic[60] = constants[95]*algebraic[36]
    algebraic[81] = constants[96]*algebraic[80]
    algebraic[64] = constants[175]*states[1]*constants[47]
    algebraic[111] = constants[113]*algebraic[40]
    algebraic[147] = (constants[104]*constants[187]+constants[191]*constants[189]+constants[106]*(constants[188]+algebraic[39]+algebraic[67]))/(constants[187]+constants[189]+constants[188]+algebraic[39]+algebraic[67])
    algebraic[155] = algebraic[147]
    algebraic[159] = algebraic[155]*algebraic[111]
    algebraic[115] = constants[114]*algebraic[53]
    algebraic[119] = constants[194]*algebraic[115]
    algebraic[123] = constants[115]*algebraic[41]
    algebraic[163] = algebraic[147]
    algebraic[167] = algebraic[163]*algebraic[123]
    algebraic[127] = constants[116]*algebraic[54]
    algebraic[131] = constants[195]*algebraic[127]
    algebraic[135] = constants[117]*algebraic[44]
    algebraic[171] = algebraic[147]
    algebraic[175] = algebraic[171]*algebraic[135]
    algebraic[151] = algebraic[147]*algebraic[46]
    algebraic[87] = constants[192]*algebraic[57]
    algebraic[91] = constants[197]*algebraic[35]
    algebraic[95] = constants[197]*algebraic[48]
    algebraic[139] = constants[118]*algebraic[82]
    algebraic[143] = constants[196]*algebraic[139]
    algebraic[99] = constants[198]*algebraic[77]
    algebraic[83] = states[13]/constants[6]
    algebraic[103] = constants[199]/(1.00000+constants[102]/algebraic[83])
    algebraic[107] = constants[170]*states[13]
    algebraic[112] = constants[113]*algebraic[40]
    algebraic[148] = (constants[123]*constants[187]+constants[201]*constants[189]+constants[125]*(constants[188]+algebraic[39]+algebraic[67]))/(constants[187]+constants[189]+constants[188]+algebraic[39]+algebraic[67])
    algebraic[156] = algebraic[148]
    algebraic[160] = algebraic[156]*algebraic[112]
    algebraic[116] = constants[114]*algebraic[53]
    algebraic[120] = constants[204]*algebraic[116]
    algebraic[124] = constants[115]*algebraic[41]
    algebraic[164] = algebraic[148]
    algebraic[168] = algebraic[164]*algebraic[124]
    algebraic[128] = constants[116]*algebraic[54]
    algebraic[132] = constants[205]*algebraic[128]
    algebraic[136] = constants[117]*algebraic[44]
    algebraic[172] = algebraic[148]
    algebraic[176] = algebraic[172]*algebraic[136]
    algebraic[152] = algebraic[148]*algebraic[46]
    algebraic[88] = constants[202]*algebraic[57]
    algebraic[92] = constants[207]*algebraic[35]
    algebraic[96] = constants[207]*algebraic[48]
    algebraic[140] = constants[118]*algebraic[82]
    algebraic[144] = constants[206]*algebraic[140]
    algebraic[100] = constants[208]*algebraic[77]
    algebraic[84] = states[14]/constants[6]
    algebraic[104] = constants[209]/(1.00000+constants[121]/algebraic[84])
    algebraic[108] = constants[171]*states[14]
    algebraic[113] = constants[113]*algebraic[40]
    algebraic[149] = (constants[134]*constants[187]+constants[211]*constants[189]+constants[136]*(constants[188]+algebraic[39]+algebraic[67]))/(constants[187]+constants[189]+constants[188]+algebraic[39]+algebraic[67])
    algebraic[157] = algebraic[149]
    algebraic[161] = algebraic[157]*algebraic[113]
    algebraic[117] = constants[114]*algebraic[53]
    algebraic[121] = constants[214]*algebraic[117]
    algebraic[125] = constants[115]*algebraic[41]
    algebraic[165] = algebraic[149]
    algebraic[169] = algebraic[165]*algebraic[125]
    algebraic[129] = constants[116]*algebraic[54]
    algebraic[133] = constants[215]*algebraic[129]
    algebraic[137] = constants[117]*algebraic[44]
    algebraic[173] = algebraic[149]
    algebraic[177] = algebraic[173]*algebraic[137]
    algebraic[153] = algebraic[149]*algebraic[46]
    algebraic[89] = constants[212]*algebraic[57]
    algebraic[93] = constants[217]*algebraic[35]
    algebraic[97] = constants[217]*algebraic[48]
    algebraic[141] = constants[118]*algebraic[82]
    algebraic[145] = constants[216]*algebraic[141]
    algebraic[101] = constants[218]*algebraic[77]
    algebraic[85] = states[15]/constants[6]
    algebraic[105] = constants[219]/(1.00000+constants[132]/algebraic[85])
    algebraic[109] = constants[172]*states[15]
    algebraic[114] = constants[113]*algebraic[40]
    algebraic[150] = (constants[145]*constants[187]+constants[221]*constants[189]+constants[147]*(constants[188]+algebraic[39]+algebraic[67]))/(constants[187]+constants[189]+constants[188]+algebraic[39]+algebraic[67])
    algebraic[158] = algebraic[150]
    algebraic[162] = algebraic[158]*algebraic[114]
    algebraic[118] = constants[114]*algebraic[53]
    algebraic[122] = constants[224]*algebraic[118]
    algebraic[126] = constants[115]*algebraic[41]
    algebraic[166] = algebraic[150]
    algebraic[170] = algebraic[166]*algebraic[126]
    algebraic[130] = constants[116]*algebraic[54]
    algebraic[134] = constants[225]*algebraic[130]
    algebraic[138] = constants[117]*algebraic[44]
    algebraic[174] = algebraic[150]
    algebraic[178] = algebraic[174]*algebraic[138]
    algebraic[154] = algebraic[150]*algebraic[46]
    algebraic[90] = constants[222]*algebraic[57]
    algebraic[94] = constants[227]*algebraic[35]
    algebraic[98] = constants[227]*algebraic[48]
    algebraic[142] = constants[118]*algebraic[82]
    algebraic[146] = constants[226]*algebraic[142]
    algebraic[102] = constants[228]*algebraic[77]
    algebraic[86] = states[16]/constants[6]
    algebraic[106] = constants[229]/(1.00000+constants[143]/algebraic[86])
    algebraic[110] = constants[173]*states[16]
    algebraic[1] = states[4]/constants[6]
    algebraic[3] = states[6]/constants[6]
    algebraic[4] = states[9]/constants[6]
    algebraic[6] = constants[167]*states[1]*(1.00000-constants[47])
    algebraic[7] = states[12]/constants[6]
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
        self.v_PdPs_star = 0.0576
        self.M_Pd_PdPs_star = 0.264
        self.Y_Pd_InPd = 0.0091
        self.D_Pd = 1.000
        self.T_Pd = 1.000
        self.T_Pd_star = 0.66
        self.V_Ru = 1.000
        self.k_SoEx = 1.000
        self.M_Ha_McMa = 0.0248
        self.v_PsAm_star = 0.0144
        self.v_PsMa_star = 0.0576
        self.v_PsMc_star = 0.0576
        self.Y_Ps_InPs = 0.0091
        self.Y_Ps_SaPs = 0.0010
        self.Y_Ps_PdPs = 1.0
        self.Y_Ps_MaMd = 0.0067
        self.Y_Ps_McPs = 0.0067
        self.D_Ps = 1.000
        self.M_Ps_PsAm = 0.0289
        self.M_Ps_PsMa = 0.0224
        self.M_Ps_PsMc = 0.0224
        self.M_Ha_PsMa = 0.0248
        self.M_Hc_PsMc = 0.0248
        self.J_Ha_PsAm = 0.0165
        self.J_Hc_PsAm = 0.0165
        self.k_FlEx = 1.000
        self.J_Ha_McAm = 0.0165
        self.Y_Pu_InPu = 0.0091
        self.D_Pu = 1.000
        self.v_UeAm_star = 0.00165
        self.v_AmAb_star = 1.10
        self.v_AmMa_star = 0.0528
        self.v_AmMc_star = 0.0528
        self.Y_Am_InAm = 0.0588
        self.Y_Am_UeAm = 2.0
        self.Y_Am_PsAm = 1.257
        self.Y_Am_McAm = 0.0084
        self.M_Am_AmMa = 0.00135
        self.M_Am_AmMc = 0.00135
        self.M_Am_AmAb = 0.0132
        self.M_pH_AmAb = 7.5
        self.phi_pH_AmAb = 7.85
        self.M_Ha_AmMa = 0.0159
        self.M_Hc_AmMc = 0.0159
        self.J_Am_UeAm = 0.00621
        self.D_Am = 1.000
        self.pH = 7.000
        self.f_Po_Ma = 0.35
        self.f_Ni_Fe = 1.000
        self.Y_Li_InLi = 0.0015
        self.Y_Li_MaMd = 0.00021
        self.D_Li = 1.000
        self.Y_Sd_InSd = 0.0062
        self.D_Sd = 1.000
        self.v_SdHa_star = 0.2179
        self.M_Sd_SdHa_star = 0.416
        self.T_Sd = 1.000
        self.T_Sd_star = 1.04
        self.Y_Fd_InFd = 0.0062
        self.D_Fd = 1.000
        self.v_FdHc_star = 0.1646
        self.M_Fd_FdHc_star = 0.332
        self.T_Fd = 1.000
        self.T_Fd_star = 0.83
        self.phi_pH_FdHc = 22.9
        self.M_pH_FdHc = 5.97
        self.pm = 1.000
        self.f = 1.000
        self.Y_Fu_InFu = 0.0062
        self.D_Fu = 1.000
        self.R_Ha_AmMa = 1.793
        self.R_Ha_PsMa = 1.291
        self.R_Ha_McMa = 0.0086
        self.M_Ha_HaAs = 0.0268
        self.M_Ha_HaVa = 0.055
        self.v_HaAs_star = 0.053
        self.v_HaVa_star = 0.1646
        self.Y_Ha_WrHa = 0.0062
        self.Y_Ha_SrHa = 0.0062
        self.Y_Ha_LaHa = 0.0025
        self.Y_Ha_SdHa = 1.0
        self.Y_Ha_MaMd = 0.0062
        self.D_Wr = 1.000
        self.D_Sr = 1.000
        self.D_La = 1.000
        self.J_Am_HaVa = 0.00861
        self.J_Ps_HaVa = 0.01465
        self.R_Hc_AmMc = 1.793
        self.R_Hc_PsMc = 1.291
        self.v_HcVa_star = 0.1646
        self.Y_Hc_FdHc = 1.0
        self.M_Hc_HcVa = 0.055
        self.J_Am_HcVa = 0.00861
        self.J_Ps_HcVa = 0.01465
        self.Y_Ma_AmMa = 118.91
        self.Y_Ma_PsMa = 149.48
        self.Y_Ma_McMa = 149.48
        self.Y_As_HaAs = 112.5
        self.Y_Mc_AmMc = 118.91
        self.Y_Mc_PsMc = 149.48
        self.v_McEg_star = 15.439
        self.M_Mc_McEg = 34.694
        self.M_Ac_AcAb = 0.338
        self.v_AcAb_star = 7.86
        self.Y_Ac_WrAc = 1.000
        self.Y_Ac_InAc = 0.0167
        self.Y_Ac_StAc = 1.000
        self.Y_Ac_CeAc = 1.000
        self.Y_Ac_HeAc = 1.000
        self.Y_Ac_PsAc = 1.000
        self.D_Ac = 1.000
        self.J_pH_AcAb = 6.45
        self.phi_pH_AcAb = 6.48
        self.f_Hf_AmMa = 0.526
        self.f_Hf_AmMc = 0.526
        self.f_Hf_PsMa = 0.711
        self.f_Hf_PsMc = 0.711
        self.f_Hf_HaAs = 0.306
        self.f_Hf_McMa = 0.711
        self.f_Lc_Le = 2.250
        self.f_Ce_Fd = 1.000
        self.M_Pr_PrAb = 0.338
        self.v_PrAb_star = 7.86
        self.Y_Pr_WrPr = 1.000
        self.Y_Pr_InPr = 0.0135
        self.Y_Pr_StPr = 1.000
        self.Y_Pr_CePr = 1.000
        self.Y_Pr_HePr = 1.000
        self.Y_Pr_PsPr = 1.000
        self.D_Pr = 1.000
        self.phi_pH_PrAb = 6.48
        self.J_pH_PrAb = 6.45
        self.M_Bu_BuAb = 0.338
        self.v_BuAb_star = 7.86
        self.Y_Bu_WrBu = 1.000
        self.Y_Bu_InBu = 0.0114
        self.Y_Bu_StBu = 1.000
        self.Y_Bu_CeBu = 1.000
        self.Y_Bu_HeBu = 1.000
        self.Y_Bu_PsBu = 1.000
        self.D_Bu = 1.000
        self.phi_pH_BuAb = 6.48
        self.J_pH_BuAb = 6.45
        self.M_Vl_VlAb = 0.338
        self.v_VlAb_star = 7.86
        self.Y_Vl_WrVl = 1.000
        self.Y_Vl_InVl = 0.0098
        self.Y_Vl_StVl = 1.000
        self.Y_Vl_CeVl = 1.000
        self.Y_Vl_HeVl = 1.000
        self.Y_Vl_PsVl = 1.000
        self.D_Vl = 1.000
        self.phi_pH_VlAb = 6.48
        self.J_pH_VlAb = 6.45

    def to_dict(self):
        return {
            "v_PdPs_star": self.v_PdPs_star,
            "M_Pd_PdPs_star": self.M_Pd_PdPs_star,
            "Y_Pd_InPd": self.Y_Pd_InPd,
            "D_Pd": self.D_Pd,
            "T_Pd": self.T_Pd,
            "T_Pd_star": self.T_Pd_star,
            "V_Ru": self.V_Ru,
            "k_SoEx": self.k_SoEx,
            "M_Ha_McMa": self.M_Ha_McMa,
            "v_PsAm_star": self.v_PsAm_star,
            "v_PsMa_star": self.v_PsMa_star,
            "v_PsMc_star": self.v_PsMc_star,
            "Y_Ps_InPs": self.Y_Ps_InPs,
            "Y_Ps_SaPs": self.Y_Ps_SaPs,
            "Y_Ps_PdPs": self.Y_Ps_PdPs,
            "Y_Ps_MaMd": self.Y_Ps_MaMd,
            "Y_Ps_McPs": self.Y_Ps_McPs,
            "D_Ps": self.D_Ps,
            "M_Ps_PsAm": self.M_Ps_PsAm,
            "M_Ps_PsMa": self.M_Ps_PsMa,
            "M_Ps_PsMc": self.M_Ps_PsMc,
            "M_Ha_PsMa": self.M_Ha_PsMa,
            "M_Hc_PsMc": self.M_Hc_PsMc,
            "J_Ha_PsAm": self.J_Ha_PsAm,
            "J_Hc_PsAm": self.J_Hc_PsAm,
            "k_FlEx": self.k_FlEx,
            "J_Ha_McAm": self.J_Ha_McAm,
            "Y_Pu_InPu": self.Y_Pu_InPu,
            "D_Pu": self.D_Pu,
            "v_UeAm_star": self.v_UeAm_star,
            "v_AmAb_star": self.v_AmAb_star,
            "v_AmMa_star": self.v_AmMa_star,
            "v_AmMc_star": self.v_AmMc_star,
            "Y_Am_InAm": self.Y_Am_InAm,
            "Y_Am_UeAm": self.Y_Am_UeAm,
            "Y_Am_PsAm": self.Y_Am_PsAm,
            "Y_Am_McAm": self.Y_Am_McAm,
            "M_Am_AmMa": self.M_Am_AmMa,
            "M_Am_AmMc": self.M_Am_AmMc,
            "M_Am_AmAb": self.M_Am_AmAb,
            "M_pH_AmAb": self.M_pH_AmAb,
            "phi_pH_AmAb": self.phi_pH_AmAb,
            "M_Ha_AmMa": self.M_Ha_AmMa,
            "M_Hc_AmMc": self.M_Hc_AmMc,
            "J_Am_UeAm": self.J_Am_UeAm,
            "D_Am": self.D_Am,
            "pH": self.pH,
            "f_Po_Ma": self.f_Po_Ma,
            "f_Ni_Fe": self.f_Ni_Fe,
            "Y_Li_InLi": self.Y_Li_InLi,
            "Y_Li_MaMd": self.Y_Li_MaMd,
            "D_Li": self.D_Li,
            "Y_Sd_InSd": self.Y_Sd_InSd,
            "D_Sd": self.D_Sd,
            "v_SdHa_star": self.v_SdHa_star,
            "M_Sd_SdHa_star": self.M_Sd_SdHa_star,
            "T_Sd": self.T_Sd,
            "T_Sd_star": self.T_Sd_star,
            "Y_Fd_InFd": self.Y_Fd_InFd,
            "D_Fd": self.D_Fd,
            "v_FdHc_star": self.v_FdHc_star,
            "M_Fd_FdHc_star": self.M_Fd_FdHc_star,
            "T_Fd": self.T_Fd,
            "T_Fd_star": self.T_Fd_star,
            "phi_pH_FdHc": self.phi_pH_FdHc,
            "M_pH_FdHc": self.M_pH_FdHc,
            "pm": self.pm,
            "f": self.f,
            "Y_Fu_InFu": self.Y_Fu_InFu,
            "D_Fu": self.D_Fu,
            "R_Ha_AmMa": self.R_Ha_AmMa,
            "R_Ha_PsMa": self.R_Ha_PsMa,
            "R_Ha_McMa": self.R_Ha_McMa,
            "M_Ha_HaAs": self.M_Ha_HaAs,
            "M_Ha_HaVa": self.M_Ha_HaVa,
            "v_HaAs_star": self.v_HaAs_star,
            "v_HaVa_star": self.v_HaVa_star,
            "Y_Ha_WrHa": self.Y_Ha_WrHa,
            "Y_Ha_SrHa": self.Y_Ha_SrHa,
            "Y_Ha_LaHa": self.Y_Ha_LaHa,
            "Y_Ha_SdHa": self.Y_Ha_SdHa,
            "Y_Ha_MaMd": self.Y_Ha_MaMd,
            "D_Wr": self.D_Wr,
            "D_Sr": self.D_Sr,
            "D_La": self.D_La,
            "J_Am_HaVa": self.J_Am_HaVa,
            "J_Ps_HaVa": self.J_Ps_HaVa,
            "R_Hc_AmMc": self.R_Hc_AmMc,
            "R_Hc_PsMc": self.R_Hc_PsMc,
            "v_HcVa_star": self.v_HcVa_star,
            "Y_Hc_FdHc": self.Y_Hc_FdHc,
            "M_Hc_HcVa": self.M_Hc_HcVa,
            "J_Am_HcVa": self.J_Am_HcVa,
            "J_Ps_HcVa": self.J_Ps_HcVa,
            "Y_Ma_AmMa": self.Y_Ma_AmMa,
            "Y_Ma_PsMa": self.Y_Ma_PsMa,
            "Y_Ma_McMa": self.Y_Ma_McMa,
            "Y_As_HaAs": self.Y_As_HaAs,
            "Y_Mc_AmMc": self.Y_Mc_AmMc,
            "Y_Mc_PsMc": self.Y_Mc_PsMc,
            "v_McEg_star": self.v_McEg_star,
            "M_Mc_McEg": self.M_Mc_McEg,
            "M_Ac_AcAb": self.M_Ac_AcAb,
            "v_AcAb_star": self.v_AcAb_star,
            "Y_Ac_WrAc": self.Y_Ac_WrAc,
            "Y_Ac_InAc": self.Y_Ac_InAc,
            "Y_Ac_StAc": self.Y_Ac_StAc,
            "Y_Ac_CeAc": self.Y_Ac_CeAc,
            "Y_Ac_HeAc": self.Y_Ac_HeAc,
            "Y_Ac_PsAc": self.Y_Ac_PsAc,
            "D_Ac": self.D_Ac,
            "J_pH_AcAb": self.J_pH_AcAb,
            "phi_pH_AcAb": self.phi_pH_AcAb,
            "f_Hf_AmMa": self.f_Hf_AmMa,
            "f_Hf_AmMc": self.f_Hf_AmMc,
            "f_Hf_PsMa": self.f_Hf_PsMa,
            "f_Hf_PsMc": self.f_Hf_PsMc,
            "f_Hf_HaAs": self.f_Hf_HaAs,
            "f_Hf_McMa": self.f_Hf_McMa,
            "f_Lc_Le": self.f_Lc_Le,
            "f_Ce_Fd": self.f_Ce_Fd,
            "M_Pr_PrAb": self.M_Pr_PrAb,
            "v_PrAb_star": self.v_PrAb_star,
            "Y_Pr_WrPr": self.Y_Pr_WrPr,
            "Y_Pr_InPr": self.Y_Pr_InPr,
            "Y_Pr_StPr": self.Y_Pr_StPr,
            "Y_Pr_CePr": self.Y_Pr_CePr,
            "Y_Pr_HePr": self.Y_Pr_HePr,
            "Y_Pr_PsPr": self.Y_Pr_PsPr,
            "D_Pr": self.D_Pr,
            "phi_pH_PrAb": self.phi_pH_PrAb,
            "J_pH_PrAb": self.J_pH_PrAb,
            "M_Bu_BuAb": self.M_Bu_BuAb,
            "v_BuAb_star": self.v_BuAb_star,
            "Y_Bu_WrBu": self.Y_Bu_WrBu,
            "Y_Bu_InBu": self.Y_Bu_InBu,
            "Y_Bu_StBu": self.Y_Bu_StBu,
            "Y_Bu_CeBu": self.Y_Bu_CeBu,
            "Y_Bu_HeBu": self.Y_Bu_HeBu,
            "Y_Bu_PsBu": self.Y_Bu_PsBu,
            "D_Bu": self.D_Bu,
            "phi_pH_BuAb": self.phi_pH_BuAb,
            "J_pH_BuAb": self.J_pH_BuAb,
            "M_Vl_VlAb": self.M_Vl_VlAb,
            "v_VlAb_star": self.v_VlAb_star,
            "Y_Vl_WrVl": self.Y_Vl_WrVl,
            "Y_Vl_InVl": self.Y_Vl_InVl,
            "Y_Vl_StVl": self.Y_Vl_StVl,
            "Y_Vl_CeVl": self.Y_Vl_CeVl,
            "Y_Vl_HeVl": self.Y_Vl_HeVl,
            "Y_Vl_PsVl": self.Y_Vl_PsVl,
            "D_Vl": self.D_Vl,
            "phi_pH_VlAb": self.phi_pH_VlAb,
            "J_pH_VlAb": self.J_pH_VlAb,
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
        y0=[1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "dijkstra_1992"
        self.curve_names = [
            "Q_Pd",
            "Q_Ma",
            "Q_Mc",
            "Q_Ps",
            "Q_Pu",
            "Q_Am",
            "Q_Li",
            "Q_Sd",
            "Q_Fd",
            "Q_Fu",
            "Q_Ha",
            "Q_Hc",
            "Q_As",
            "Q_Ac",
            "Q_Pr",
            "Q_Bu",
            "Q_Vl",
        ]
        self.state_names = ['Q_Pd', 'Q_Ma', 'Q_Mc', 'Q_Ps', 'Q_Pu', 'Q_Am', 'Q_Li', 'Q_Sd', 'Q_Fd', 'Q_Fu', 'Q_Ha', 'Q_Hc', 'Q_As', 'Q_Ac', 'Q_Pr', 'Q_Bu', 'Q_Vl']
        self.algebraic_names = ['C_Pd', 'C_Pu', 'U_Pu_PuEx', 'C_Li', 'C_Fu', 'U_Fu_FuEx', 'U_Ma_MaEx', 'C_As', 'U_Pd_PdEx', 'v_PdPs', 'U_Pd_PdPs', 'C_Ps', 'P_Ps_PdPs', 'U_Ps_PsEx', 'v_Ma_PsAm', 'v_Mc_PsAm', 'v_PsMa', 'v_PsMc', 'C_Am', 'U_Am_AmAb', 'U_Am_AmEx', 'v_UeAm', 'P_Am_UeAm', 'v_AmMa', 'v_AmMc', 'U_Li_LiEx', 'C_Sd', 'U_Sd_SdEx', 'v_SdHa', 'U_Sd_SdHa', 'C_Fd', 'U_Fd_FdEx', 'v_FdHc', 'U_Fd_FdHc', 'C_Ha', 'U_MaPs_PsAm', 'U_Ps_PsMa', 'P_MaAm_PsAm', 'U_Am_AmMa', 'P_Ha_SdHa', 'U_Ha_AmMa', 'U_Ha_PsMa', 'U_Ha_HaEx', 'v_HaAs', 'U_Ha_HaAs', 'v_HaVa', 'U_Ha_HaVa', 'C_Hc', 'U_McPs_PsAm', 'U_Ps_PsMc', 'P_McAm_PsAm', 'U_Am_AmMc', 'P_Hc_FdHc', 'U_Hc_AmMc', 'U_Hc_PsMc', 'U_Hc_HcEx', 'v_HcVa', 'U_Hc_HcVa', 'C_Ma', 'P_Ma_AmMa', 'P_Ma_PsMa', 'U_Ma_MaMd', 'P_Ps_MaMd', 'P_Li_MaMd', 'U_Ma_PoEx', 'P_As_HaAs', 'U_As_MaMd', 'P_Ha_MaMd', 'U_As_AsEx', 'C_Mc', 'U_As_PoEx', 'P_Mc_AmMc', 'P_Mc_PsMc', 'U_Mc_McEx', 'v_McEg', 'U_Mc_McEg', 'U_Mc_McPs', 'U_Mc_McAm', 'P_Ps_McPs', 'P_Am_McAm', 'U_Mc_McMa', 'P_Ma_McMa', 'U_Ha_McMa', 'C_Ac', 'C_Pr', 'C_Bu', 'C_Vl', 'P_Ac_HcVa', 'P_Pr_HcVa', 'P_Bu_HcVa', 'P_Vl_HcVa', 'P_MaAc_PsAm', 'P_MaPr_PsAm', 'P_MaBu_PsAm', 'P_MaVl_PsAm', 'P_McAc_PsAm', 'P_McPr_PsAm', 'P_McBu_PsAm', 'P_McVl_PsAm', 'P_Ac_McAm', 'P_Pr_McAm', 'P_Bu_McAm', 'P_Vl_McAm', 'U_Ac_AcAb', 'U_Pr_PrAb', 'U_Bu_BuAb', 'U_Vl_VlAb', 'U_Ac_AcEx', 'U_Pr_PrEx', 'U_Bu_BuEx', 'U_Vl_VlEx', 'U_Hf_AmMa', 'U_Hf_AmMa_1', 'U_Hf_AmMa_2', 'U_Hf_AmMa_3', 'U_Hf_AmMc', 'U_Hf_AmMc_1', 'U_Hf_AmMc_2', 'U_Hf_AmMc_3', 'P_Ac_AmMc', 'P_Pr_AmMc', 'P_Bu_AmMc', 'P_Vl_AmMc', 'U_Hf_PsMa', 'U_Hf_PsMa_1', 'U_Hf_PsMa_2', 'U_Hf_PsMa_3', 'U_Hf_PsMc', 'U_Hf_PsMc_1', 'U_Hf_PsMc_2', 'U_Hf_PsMc_3', 'P_Ac_PsMc', 'P_Pr_PsMc', 'P_Bu_PsMc', 'P_Vl_PsMc', 'U_Hf_HaAs', 'U_Hf_HaAs_1', 'U_Hf_HaAs_2', 'U_Hf_HaAs_3', 'U_Hf_McMa', 'U_Hf_McMa_1', 'U_Hf_McMa_2', 'U_Hf_McMa_3', 'P_Ac_McMa', 'P_Pr_McMa', 'P_Bu_McMa', 'P_Vl_McMa', 'Y_Ac_HaVa', 'Y_Pr_HaVa', 'Y_Bu_HaVa', 'Y_Vl_HaVa', 'P_Ac_HaVa', 'P_Pr_HaVa', 'P_Bu_HaVa', 'P_Vl_HaVa', 'Y_Ac_AmMa', 'Y_Pr_AmMa', 'Y_Bu_AmMa', 'Y_Vl_AmMa', 'P_Ac_AmMa', 'P_Pr_AmMa', 'P_Bu_AmMa', 'P_Vl_AmMa', 'Y_Ac_PsMa', 'Y_Pr_PsMa', 'Y_Bu_PsMa', 'Y_Vl_PsMa', 'P_Ac_PsMa', 'P_Pr_PsMa', 'P_Bu_PsMa', 'P_Vl_PsMa', 'Y_Ac_HaAs', 'Y_Pr_HaAs', 'Y_Bu_HaAs', 'Y_Vl_HaAs', 'P_Ac_HaAs', 'P_Pr_HaAs', 'P_Bu_HaAs', 'P_Vl_HaAs']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 230
        p = self.params

        # direct mapping
        c[0] = p.v_PdPs_star
        c[1] = p.M_Pd_PdPs_star
        c[2] = p.Y_Pd_InPd
        c[3] = p.D_Pd
        c[4] = p.T_Pd
        c[5] = p.T_Pd_star
        c[6] = p.V_Ru
        c[7] = p.k_SoEx
        c[8] = p.M_Ha_McMa
        c[9] = p.v_PsAm_star
        c[10] = p.v_PsMa_star
        c[11] = p.v_PsMc_star
        c[12] = p.Y_Ps_InPs
        c[13] = p.Y_Ps_SaPs
        c[14] = p.Y_Ps_PdPs
        c[15] = p.Y_Ps_MaMd
        c[16] = p.Y_Ps_McPs
        c[17] = p.D_Ps
        c[18] = p.M_Ps_PsAm
        c[19] = p.M_Ps_PsMa
        c[20] = p.M_Ps_PsMc
        c[21] = p.M_Ha_PsMa
        c[22] = p.M_Hc_PsMc
        c[23] = p.J_Ha_PsAm
        c[24] = p.J_Hc_PsAm
        c[25] = p.k_FlEx
        c[26] = p.J_Ha_McAm
        c[27] = p.Y_Pu_InPu
        c[28] = p.D_Pu
        c[29] = p.v_UeAm_star
        c[30] = p.v_AmAb_star
        c[31] = p.v_AmMa_star
        c[32] = p.v_AmMc_star
        c[33] = p.Y_Am_InAm
        c[34] = p.Y_Am_UeAm
        c[35] = p.Y_Am_PsAm
        c[36] = p.Y_Am_McAm
        c[37] = p.M_Am_AmMa
        c[38] = p.M_Am_AmMc
        c[39] = p.M_Am_AmAb
        c[40] = p.M_pH_AmAb
        c[41] = p.phi_pH_AmAb
        c[42] = p.M_Ha_AmMa
        c[43] = p.M_Hc_AmMc
        c[44] = p.J_Am_UeAm
        c[45] = p.D_Am
        c[46] = p.pH
        c[47] = p.f_Po_Ma
        c[48] = p.f_Ni_Fe
        c[49] = p.Y_Li_InLi
        c[50] = p.Y_Li_MaMd
        c[51] = p.D_Li
        c[52] = p.Y_Sd_InSd
        c[53] = p.D_Sd
        c[54] = p.v_SdHa_star
        c[55] = p.M_Sd_SdHa_star
        c[56] = p.T_Sd
        c[57] = p.T_Sd_star
        c[58] = p.Y_Fd_InFd
        c[59] = p.D_Fd
        c[60] = p.v_FdHc_star
        c[61] = p.M_Fd_FdHc_star
        c[62] = p.T_Fd
        c[63] = p.T_Fd_star
        c[64] = p.phi_pH_FdHc
        c[65] = p.M_pH_FdHc
        c[66] = p.pm
        c[67] = p.f
        c[68] = p.Y_Fu_InFu
        c[69] = p.D_Fu
        c[70] = p.R_Ha_AmMa
        c[71] = p.R_Ha_PsMa
        c[72] = p.R_Ha_McMa
        c[73] = p.M_Ha_HaAs
        c[74] = p.M_Ha_HaVa
        c[75] = p.v_HaAs_star
        c[76] = p.v_HaVa_star
        c[77] = p.Y_Ha_WrHa
        c[78] = p.Y_Ha_SrHa
        c[79] = p.Y_Ha_LaHa
        c[80] = p.Y_Ha_SdHa
        c[81] = p.Y_Ha_MaMd
        c[82] = p.D_Wr
        c[83] = p.D_Sr
        c[84] = p.D_La
        c[85] = p.J_Am_HaVa
        c[86] = p.J_Ps_HaVa
        c[87] = p.R_Hc_AmMc
        c[88] = p.R_Hc_PsMc
        c[89] = p.v_HcVa_star
        c[90] = p.Y_Hc_FdHc
        c[91] = p.M_Hc_HcVa
        c[92] = p.J_Am_HcVa
        c[93] = p.J_Ps_HcVa
        c[94] = p.Y_Ma_AmMa
        c[95] = p.Y_Ma_PsMa
        c[96] = p.Y_Ma_McMa
        c[97] = p.Y_As_HaAs
        c[98] = p.Y_Mc_AmMc
        c[99] = p.Y_Mc_PsMc
        c[100] = p.v_McEg_star
        c[101] = p.M_Mc_McEg
        c[102] = p.M_Ac_AcAb
        c[103] = p.v_AcAb_star
        c[104] = p.Y_Ac_WrAc
        c[105] = p.Y_Ac_InAc
        c[106] = p.Y_Ac_StAc
        c[107] = p.Y_Ac_CeAc
        c[108] = p.Y_Ac_HeAc
        c[109] = p.Y_Ac_PsAc
        c[110] = p.D_Ac
        c[111] = p.J_pH_AcAb
        c[112] = p.phi_pH_AcAb
        c[113] = p.f_Hf_AmMa
        c[114] = p.f_Hf_AmMc
        c[115] = p.f_Hf_PsMa
        c[116] = p.f_Hf_PsMc
        c[117] = p.f_Hf_HaAs
        c[118] = p.f_Hf_McMa
        c[119] = p.f_Lc_Le
        c[120] = p.f_Ce_Fd
        c[121] = p.M_Pr_PrAb
        c[122] = p.v_PrAb_star
        c[123] = p.Y_Pr_WrPr
        c[124] = p.Y_Pr_InPr
        c[125] = p.Y_Pr_StPr
        c[126] = p.Y_Pr_CePr
        c[127] = p.Y_Pr_HePr
        c[128] = p.Y_Pr_PsPr
        c[129] = p.D_Pr
        c[130] = p.phi_pH_PrAb
        c[131] = p.J_pH_PrAb
        c[132] = p.M_Bu_BuAb
        c[133] = p.v_BuAb_star
        c[134] = p.Y_Bu_WrBu
        c[135] = p.Y_Bu_InBu
        c[136] = p.Y_Bu_StBu
        c[137] = p.Y_Bu_CeBu
        c[138] = p.Y_Bu_HeBu
        c[139] = p.Y_Bu_PsBu
        c[140] = p.D_Bu
        c[141] = p.phi_pH_BuAb
        c[142] = p.J_pH_BuAb
        c[143] = p.M_Vl_VlAb
        c[144] = p.v_VlAb_star
        c[145] = p.Y_Vl_WrVl
        c[146] = p.Y_Vl_InVl
        c[147] = p.Y_Vl_StVl
        c[148] = p.Y_Vl_CeVl
        c[149] = p.Y_Vl_HeVl
        c[150] = p.Y_Vl_PsVl
        c[151] = p.D_Vl
        c[152] = p.phi_pH_VlAb
        c[153] = p.J_pH_VlAb

        # derived constants
        c[154] = c[7]
        c[155] = c[2]*c[3]
        c[156] = c[25]
        c[157] = c[27]*c[28]
        c[158] = c[7]
        c[159] = c[25]
        c[160] = c[25]
        c[161] = c[7]
        c[162] = c[7]
        c[163] = c[68]*c[69]
        c[164] = c[7]
        c[165] = c[25]
        c[166] = c[25]
        c[167] = c[25]
        c[168] = c[25]
        c[169] = c[7]
        c[170] = c[25]
        c[171] = c[25]
        c[172] = c[25]
        c[173] = c[25]
        c[174] = c[1]*(c[4]/c[5])
        c[175] = c[7]/2.00000
        c[176] = c[12]*c[17]
        c[177] = c[167]-c[175]
        c[178] = c[167]-c[175]
        c[179] = c[13]*c[17]
        c[180] = c[33]*c[45]
        c[181] = c[30]*(power(1.00000, 0.250000))*(power(c[6], 0.750000))*(1.00000+power(c[40]/c[46], c[41]))
        c[182] = c[49]*c[51]
        c[183] = c[52]*c[53]
        c[184] = c[55]*(c[56]/c[57])
        c[185] = c[58]*c[59]
        c[186] = c[61]*(c[62]/c[63])
        c[187] = c[77]*c[82]
        c[188] = c[78]*c[83]
        c[189] = c[79]*c[84]
        c[190] = c[105]*c[110]
        c[191] = c[119]*c[104]
        c[192] = c[120]*c[107]+(1.00000-c[120])*c[108]
        c[193] = c[109]
        c[194] = c[192]
        c[195] = c[192]
        c[196] = c[192]
        c[197] = c[193]
        c[198] = c[193]
        c[199] = c[103]*(power(1.00000, 0.250000))*((power(c[6], 0.750000))/(1.00000+power(c[46]/c[111], c[112])))
        c[200] = c[124]*c[129]
        c[201] = c[119]*c[123]
        c[202] = c[120]*c[126]+(1.00000-c[120])*c[127]
        c[203] = c[128]
        c[204] = c[202]
        c[205] = c[202]
        c[206] = c[202]
        c[207] = c[203]
        c[208] = c[203]
        c[209] = c[122]*(power(1.00000, 0.250000))*((power(c[6], 0.750000))/(1.00000+power(c[46]/c[131], c[130])))
        c[210] = c[135]*c[140]
        c[211] = c[119]*c[134]
        c[212] = c[120]*c[137]+(1.00000-c[120])*c[138]
        c[213] = c[139]
        c[214] = c[212]
        c[215] = c[212]
        c[216] = c[212]
        c[217] = c[213]
        c[218] = c[213]
        c[219] = c[133]*(power(1.00000, 0.250000))*((power(c[6], 0.750000))/(1.00000+power(c[46]/c[142], c[141])))
        c[220] = c[146]*c[151]
        c[221] = c[119]*c[145]
        c[222] = c[120]*c[148]+(1.00000-c[120])*c[149]
        c[223] = c[150]
        c[224] = c[222]
        c[225] = c[222]
        c[226] = c[222]
        c[227] = c[223]
        c[228] = c[223]
        c[229] = c[144]*(power(1.00000, 0.250000))*((power(c[6], 0.750000))/(1.00000+power(c[46]/c[153], c[152])))

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
