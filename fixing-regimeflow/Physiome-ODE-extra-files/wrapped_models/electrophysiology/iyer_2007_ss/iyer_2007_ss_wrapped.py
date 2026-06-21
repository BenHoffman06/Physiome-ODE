# Size of variable arrays:
sizeAlgebraic = 256
sizeStates = 67
sizeConstants = 186
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (ms)"
    legend_constants[0] = "iso in component environment (dimensionless)"
    legend_constants[1] = "CSQN2 in component environment (dimensionless)"
    legend_constants[2] = "RyR2 in component environment (dimensionless)"
    legend_constants[155] = "a1 in component COMPUTE_CONCENTRATION_AND_VOLTAGE_DERIVATIVES (F_M_per_coulomb)"
    legend_constants[160] = "a2 in component COMPUTE_CONCENTRATION_AND_VOLTAGE_DERIVATIVES (F_M_per_coulomb)"
    legend_constants[3] = "Faraday in component COMPUTE_CONCENTRATION_AND_VOLTAGE_DERIVATIVES (coulomb_per_millimole)"
    legend_constants[4] = "Temp in component COMPUTE_CONCENTRATION_AND_VOLTAGE_DERIVATIVES (kelvin)"
    legend_constants[5] = "Rgas in component COMPUTE_CONCENTRATION_AND_VOLTAGE_DERIVATIVES (joule_per_mole_kelvin)"
    legend_constants[124] = "RT_over_F in component COMPUTE_CONCENTRATION_AND_VOLTAGE_DERIVATIVES (mV)"
    legend_constants[6] = "Acap in component COMPUTE_CONCENTRATION_AND_VOLTAGE_DERIVATIVES (cm2)"
    legend_constants[135] = "C in component COMPUTE_CONCENTRATION_AND_VOLTAGE_DERIVATIVES (mF)"
    legend_constants[7] = "Vmyo in component COMPUTE_CONCENTRATION_AND_VOLTAGE_DERIVATIVES (uL)"
    legend_constants[8] = "VJSR in component COMPUTE_CONCENTRATION_AND_VOLTAGE_DERIVATIVES (uL)"
    legend_constants[9] = "VNSR in component COMPUTE_CONCENTRATION_AND_VOLTAGE_DERIVATIVES (uL)"
    legend_constants[10] = "VSS in component COMPUTE_CONCENTRATION_AND_VOLTAGE_DERIVATIVES (uL)"
    legend_states[0] = "Nai in component COMPUTE_CONCENTRATION_AND_VOLTAGE_DERIVATIVES (mM)"
    legend_states[1] = "Ki in component COMPUTE_CONCENTRATION_AND_VOLTAGE_DERIVATIVES (mM)"
    legend_states[2] = "Cai in component COMPUTE_CONCENTRATION_AND_VOLTAGE_DERIVATIVES (mM)"
    legend_states[3] = "CaSS in component COMPUTE_CONCENTRATION_AND_VOLTAGE_DERIVATIVES (mM)"
    legend_states[4] = "CaJSR in component COMPUTE_CONCENTRATION_AND_VOLTAGE_DERIVATIVES (mM)"
    legend_states[5] = "CaNSR in component COMPUTE_CONCENTRATION_AND_VOLTAGE_DERIVATIVES (mM)"
    legend_states[6] = "V in component COMPUTE_CONCENTRATION_AND_VOLTAGE_DERIVATIVES (mV)"
    legend_algebraic[131] = "INa in component COMPUTE_INa_IKr_IKs_Ito1_IK1_INab_IKp (uA_per_uF)"
    legend_algebraic[228] = "INab in component COMPUTE_INa_IKr_IKs_Ito1_IK1_INab_IKp (uA_per_uF)"
    legend_algebraic[243] = "INaCa in component COMPUTE_INaK_INaCa_ICab_IpCa (uA_per_uF)"
    legend_algebraic[239] = "INaK in component COMPUTE_INaK_INaCa_ICab_IpCa (uA_per_uF)"
    legend_algebraic[206] = "IKv14_Na in component COMPUTE_INa_IKr_IKs_Ito1_IK1_INab_IKp (uA_per_uF)"
    legend_algebraic[135] = "IKr in component COMPUTE_INa_IKr_IKs_Ito1_IK1_INab_IKp (uA_per_uF)"
    legend_algebraic[139] = "IKs in component COMPUTE_INa_IKr_IKs_Ito1_IK1_INab_IKp (uA_per_uF)"
    legend_algebraic[226] = "IK1 in component COMPUTE_INa_IKr_IKs_Ito1_IK1_INab_IKp (uA_per_uF)"
    legend_algebraic[254] = "ICaK in component COMPUTE_ICa_ICaK (uA_per_uF)"
    legend_algebraic[249] = "ICa in component COMPUTE_ICa_ICaK (uA_per_uF)"
    legend_algebraic[220] = "Ito1 in component COMPUTE_INa_IKr_IKs_Ito1_IK1_INab_IKp (uA_per_uF)"
    legend_algebraic[11] = "i_Stim in component I_stimulus (uA_per_uF)"
    legend_algebraic[144] = "IKv43 in component COMPUTE_INa_IKr_IKs_Ito1_IK1_INab_IKp (uA_per_uF)"
    legend_algebraic[188] = "IKv14_K in component COMPUTE_INa_IKr_IKs_Ito1_IK1_INab_IKp (uA_per_uF)"
    legend_algebraic[230] = "ICab in component COMPUTE_INaK_INaCa_ICab_IpCa (uA_per_uF)"
    legend_algebraic[232] = "IpCa in component COMPUTE_INaK_INaCa_ICab_IpCa (uA_per_uF)"
    legend_algebraic[60] = "Jxfer in component COMPUTE_INTRACELLULAR_CALCIUM_FLUXES (mM_per_ms)"
    legend_algebraic[42] = "Jup in component COMPUTE_INTRACELLULAR_CALCIUM_FLUXES (mM_per_ms)"
    legend_algebraic[91] = "Jtrpn in component COMPUTE_Jtrpn_and_BUFFER_SCALE_FACTORS (mM_per_ms)"
    legend_algebraic[51] = "Jrel in component COMPUTE_INTRACELLULAR_CALCIUM_FLUXES (mM_per_ms)"
    legend_algebraic[61] = "Jtr in component COMPUTE_INTRACELLULAR_CALCIUM_FLUXES (mM_per_ms)"
    legend_algebraic[101] = "beta_SS in component COMPUTE_Jtrpn_and_BUFFER_SCALE_FACTORS (dimensionless)"
    legend_algebraic[71] = "beta_JSR in component COMPUTE_Jtrpn_and_BUFFER_SCALE_FACTORS (dimensionless)"
    legend_algebraic[111] = "beta_i in component COMPUTE_Jtrpn_and_BUFFER_SCALE_FACTORS (dimensionless)"
    legend_algebraic[255] = "i_tot in component COMPUTE_CONCENTRATION_AND_VOLTAGE_DERIVATIVES (uA_per_uF)"
    legend_constants[11] = "Ko in component COMPUTE_CONCENTRATION_AND_VOLTAGE_DERIVATIVES (mM)"
    legend_constants[12] = "Nao in component COMPUTE_CONCENTRATION_AND_VOLTAGE_DERIVATIVES (mM)"
    legend_constants[13] = "Cao in component COMPUTE_CONCENTRATION_AND_VOLTAGE_DERIVATIVES (mM)"
    legend_constants[14] = "stim_period in component I_stimulus (ms)"
    legend_constants[15] = "stim_duration in component I_stimulus (ms)"
    legend_constants[16] = "stim_amplitude in component I_stimulus (uA_per_uF)"
    legend_constants[17] = "stim_offset in component I_stimulus (ms)"
    legend_algebraic[0] = "past in component I_stimulus (ms)"
    legend_algebraic[22] = "fb in component COMPUTE_INTRACELLULAR_CALCIUM_FLUXES (dimensionless)"
    legend_constants[18] = "Kfb in component COMPUTE_INTRACELLULAR_CALCIUM_FLUXES (mM)"
    legend_constants[19] = "Nfb in component COMPUTE_INTRACELLULAR_CALCIUM_FLUXES (dimensionless)"
    legend_algebraic[33] = "rb in component COMPUTE_INTRACELLULAR_CALCIUM_FLUXES (dimensionless)"
    legend_constants[20] = "Krb in component COMPUTE_INTRACELLULAR_CALCIUM_FLUXES (mM)"
    legend_constants[21] = "Nrb in component COMPUTE_INTRACELLULAR_CALCIUM_FLUXES (dimensionless)"
    legend_constants[22] = "KSR in component COMPUTE_INTRACELLULAR_CALCIUM_FLUXES (mM)"
    legend_constants[23] = "vmaxf in component COMPUTE_INTRACELLULAR_CALCIUM_FLUXES (per_ms)"
    legend_constants[24] = "vmaxr in component COMPUTE_INTRACELLULAR_CALCIUM_FLUXES (per_ms)"
    legend_constants[25] = "v1 in component COMPUTE_INTRACELLULAR_CALCIUM_FLUXES (per_ms)"
    legend_states[7] = "O1_RyR in component COMPUTE_DERIVATIVES_OF_RyR_RECEPTOR_STATES (dimensionless)"
    legend_states[8] = "O2_RyR in component COMPUTE_DERIVATIVES_OF_RyR_RECEPTOR_STATES (dimensionless)"
    legend_constants[26] = "tautr in component COMPUTE_INTRACELLULAR_CALCIUM_FLUXES (ms)"
    legend_constants[27] = "tauxfer in component COMPUTE_INTRACELLULAR_CALCIUM_FLUXES (ms)"
    legend_constants[28] = "LTRPNtot in component COMPUTE_Jtrpn_and_BUFFER_SCALE_FACTORS (mM)"
    legend_constants[29] = "HTRPNtot in component COMPUTE_Jtrpn_and_BUFFER_SCALE_FACTORS (mM)"
    legend_constants[30] = "khtrpn_plus in component COMPUTE_Jtrpn_and_BUFFER_SCALE_FACTORS (per_mM_per_ms)"
    legend_constants[31] = "khtrpn_minus in component COMPUTE_Jtrpn_and_BUFFER_SCALE_FACTORS (per_ms)"
    legend_constants[32] = "kltrpn_plus in component COMPUTE_Jtrpn_and_BUFFER_SCALE_FACTORS (per_mM_per_ms)"
    legend_constants[33] = "kltrpn_minus in component COMPUTE_Jtrpn_and_BUFFER_SCALE_FACTORS (per_ms)"
    legend_constants[34] = "CMDNtot in component COMPUTE_Jtrpn_and_BUFFER_SCALE_FACTORS (mM)"
    legend_constants[125] = "CSQNtot in component COMPUTE_Jtrpn_and_BUFFER_SCALE_FACTORS (mM)"
    legend_constants[35] = "EGTAtot in component COMPUTE_Jtrpn_and_BUFFER_SCALE_FACTORS (mM)"
    legend_constants[36] = "KmCMDN in component COMPUTE_Jtrpn_and_BUFFER_SCALE_FACTORS (mM)"
    legend_constants[37] = "KmCSQN in component COMPUTE_Jtrpn_and_BUFFER_SCALE_FACTORS (mM)"
    legend_constants[38] = "KmEGTA in component COMPUTE_Jtrpn_and_BUFFER_SCALE_FACTORS (mM)"
    legend_algebraic[70] = "dLTRPNCa in component COMPUTE_Jtrpn_and_BUFFER_SCALE_FACTORS (per_ms)"
    legend_algebraic[81] = "dHTRPNCa in component COMPUTE_Jtrpn_and_BUFFER_SCALE_FACTORS (per_ms)"
    legend_states[9] = "LTRPNCa in component COMPUTE_Jtrpn_and_BUFFER_SCALE_FACTORS (dimensionless)"
    legend_states[10] = "HTRPNCa in component COMPUTE_Jtrpn_and_BUFFER_SCALE_FACTORS (dimensionless)"
    legend_constants[39] = "kaplus in component COMPUTE_DERIVATIVES_OF_RyR_RECEPTOR_STATES (per_uM4_per_ms)"
    legend_constants[40] = "kaminus in component COMPUTE_DERIVATIVES_OF_RyR_RECEPTOR_STATES (per_ms)"
    legend_constants[41] = "kbplus in component COMPUTE_DERIVATIVES_OF_RyR_RECEPTOR_STATES (per_uM3_per_ms)"
    legend_constants[42] = "kbminus in component COMPUTE_DERIVATIVES_OF_RyR_RECEPTOR_STATES (per_ms)"
    legend_constants[43] = "kcplus in component COMPUTE_DERIVATIVES_OF_RyR_RECEPTOR_STATES (per_ms)"
    legend_constants[44] = "kcminus in component COMPUTE_DERIVATIVES_OF_RyR_RECEPTOR_STATES (per_ms)"
    legend_constants[45] = "ncoop in component COMPUTE_DERIVATIVES_OF_RyR_RECEPTOR_STATES (dimensionless)"
    legend_constants[46] = "mcoop in component COMPUTE_DERIVATIVES_OF_RyR_RECEPTOR_STATES (dimensionless)"
    legend_constants[47] = "kryr in component COMPUTE_DERIVATIVES_OF_RyR_RECEPTOR_STATES (dimensionless)"
    legend_algebraic[1] = "klumenC1O1 in component COMPUTE_DERIVATIVES_OF_RyR_RECEPTOR_STATES (dimensionless)"
    legend_algebraic[12] = "klumenO1C2 in component COMPUTE_DERIVATIVES_OF_RyR_RECEPTOR_STATES (dimensionless)"
    legend_algebraic[23] = "klumenC2O1 in component COMPUTE_DERIVATIVES_OF_RyR_RECEPTOR_STATES (dimensionless)"
    legend_constants[48] = "HmaxC1O1 in component COMPUTE_DERIVATIVES_OF_RyR_RECEPTOR_STATES (dimensionless)"
    legend_constants[126] = "HmaxO1C2 in component COMPUTE_DERIVATIVES_OF_RyR_RECEPTOR_STATES (dimensionless)"
    legend_constants[49] = "HmaxC2O1 in component COMPUTE_DERIVATIVES_OF_RyR_RECEPTOR_STATES (dimensionless)"
    legend_constants[50] = "Hmin in component COMPUTE_DERIVATIVES_OF_RyR_RECEPTOR_STATES (dimensionless)"
    legend_constants[51] = "H50C1O1 in component COMPUTE_DERIVATIVES_OF_RyR_RECEPTOR_STATES (mM)"
    legend_constants[52] = "H50O1C2 in component COMPUTE_DERIVATIVES_OF_RyR_RECEPTOR_STATES (mM)"
    legend_constants[127] = "H50C2O1 in component COMPUTE_DERIVATIVES_OF_RyR_RECEPTOR_STATES (mM)"
    legend_constants[53] = "HN in component COMPUTE_DERIVATIVES_OF_RyR_RECEPTOR_STATES (dimensionless)"
    legend_algebraic[34] = "dC1_RyR in component COMPUTE_DERIVATIVES_OF_RyR_RECEPTOR_STATES (per_ms)"
    legend_algebraic[43] = "dO2_RyR in component COMPUTE_DERIVATIVES_OF_RyR_RECEPTOR_STATES (per_ms)"
    legend_algebraic[52] = "dC2_RyR in component COMPUTE_DERIVATIVES_OF_RyR_RECEPTOR_STATES (per_ms)"
    legend_algebraic[62] = "dO1_RyR in component COMPUTE_DERIVATIVES_OF_RyR_RECEPTOR_STATES (per_ms)"
    legend_states[11] = "C1_RyR in component COMPUTE_DERIVATIVES_OF_RyR_RECEPTOR_STATES (dimensionless)"
    legend_states[12] = "C2_RyR in component COMPUTE_DERIVATIVES_OF_RyR_RECEPTOR_STATES (dimensionless)"
    legend_constants[54] = "fL in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (per_ms)"
    legend_constants[55] = "gL in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (per_ms)"
    legend_constants[56] = "bL in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (dimensionless)"
    legend_constants[57] = "aL in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (dimensionless)"
    legend_algebraic[53] = "C0_to_C1 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (per_ms)"
    legend_algebraic[63] = "C1_to_C2 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (per_ms)"
    legend_algebraic[72] = "C2_to_C3 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (per_ms)"
    legend_algebraic[82] = "C3_to_C4 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (per_ms)"
    legend_algebraic[124] = "C1_to_C0 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (per_ms)"
    legend_algebraic[128] = "C2_to_C1 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (per_ms)"
    legend_algebraic[132] = "C3_to_C2 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (per_ms)"
    legend_algebraic[136] = "C4_to_C3 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (per_ms)"
    legend_algebraic[92] = "CCa0_to_CCa1 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (per_ms)"
    legend_algebraic[102] = "CCa1_to_CCa2 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (per_ms)"
    legend_algebraic[112] = "CCa2_to_CCa3 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (per_ms)"
    legend_algebraic[120] = "CCa3_to_CCa4 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (per_ms)"
    legend_algebraic[140] = "CCa1_to_CCa0 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (per_ms)"
    legend_algebraic[145] = "CCa2_to_CCa1 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (per_ms)"
    legend_algebraic[151] = "CCa3_to_CCa2 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (per_ms)"
    legend_algebraic[159] = "CCa4_to_CCa3 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (per_ms)"
    legend_algebraic[169] = "C0_to_CCa0 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (per_ms)"
    legend_algebraic[178] = "C1_to_CCa1 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (per_ms)"
    legend_algebraic[189] = "C2_to_CCa2 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (per_ms)"
    legend_algebraic[200] = "C3_to_CCa3 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (per_ms)"
    legend_algebraic[207] = "C4_to_CCa4 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (per_ms)"
    legend_constants[143] = "CCa0_to_C0 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (per_ms)"
    legend_constants[159] = "CCa1_to_C1 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (per_ms)"
    legend_constants[162] = "CCa2_to_C2 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (per_ms)"
    legend_constants[168] = "CCa3_to_C3 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (per_ms)"
    legend_constants[173] = "CCa4_to_C4 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (per_ms)"
    legend_algebraic[2] = "alpha in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (per_ms)"
    legend_algebraic[13] = "beta in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (per_ms)"
    legend_algebraic[24] = "alpha_prime in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (per_ms)"
    legend_algebraic[35] = "beta_prime in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (per_ms)"
    legend_algebraic[44] = "gamma in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (per_ms)"
    legend_constants[128] = "omega in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (per_ms)"
    legend_algebraic[179] = "a1_Ca0 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (per_ms)"
    legend_algebraic[190] = "a2_Ca0 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (per_ms)"
    legend_algebraic[191] = "a1_Ca1 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (per_ms)"
    legend_algebraic[201] = "a2_Ca1 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (per_ms)"
    legend_algebraic[202] = "a1_Ca2 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (per_ms)"
    legend_algebraic[208] = "a2_Ca2 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (per_ms)"
    legend_algebraic[209] = "a1_Ca3 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (per_ms)"
    legend_algebraic[214] = "a2_Ca3 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (per_ms)"
    legend_algebraic[215] = "a1_Ca4 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (per_ms)"
    legend_algebraic[221] = "a2_Ca4 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (per_ms)"
    legend_algebraic[180] = "a1_C0 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (per_ms)"
    legend_algebraic[192] = "a2_C0 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (per_ms)"
    legend_algebraic[193] = "a1_C1 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (per_ms)"
    legend_algebraic[203] = "a2_C1 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (per_ms)"
    legend_algebraic[204] = "a1_C2 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (per_ms)"
    legend_algebraic[210] = "a2_C2 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (per_ms)"
    legend_algebraic[211] = "a1_C3 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (per_ms)"
    legend_algebraic[216] = "a2_C3 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (per_ms)"
    legend_algebraic[217] = "a1_C4 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (per_ms)"
    legend_algebraic[222] = "a2_C4 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (per_ms)"
    legend_states[13] = "C0 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (dimensionless)"
    legend_states[14] = "C1 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (dimensionless)"
    legend_states[15] = "C2 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (dimensionless)"
    legend_states[16] = "C3 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (dimensionless)"
    legend_states[17] = "C4 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (dimensionless)"
    legend_states[18] = "CCa0 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (dimensionless)"
    legend_states[19] = "CCa1 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (dimensionless)"
    legend_states[20] = "CCa2 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (dimensionless)"
    legend_states[21] = "CCa3 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (dimensionless)"
    legend_states[22] = "CCa4 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (dimensionless)"
    legend_states[23] = "Open in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (dimensionless)"
    legend_states[24] = "yCa in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (dimensionless)"
    legend_constants[129] = "a1_Cainf in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (dimensionless)"
    legend_algebraic[3] = "yCa_inf in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (dimensionless)"
    legend_algebraic[14] = "tau_yCa in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (ms)"
    legend_algebraic[4] = "alpha_act43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (per_ms)"
    legend_algebraic[15] = "beta_act43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (per_ms)"
    legend_algebraic[25] = "alpha_inact43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (per_ms)"
    legend_algebraic[36] = "beta_inact43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (per_ms)"
    legend_algebraic[45] = "C0Kv43_to_C1Kv43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (per_ms)"
    legend_algebraic[54] = "C1Kv43_to_C2Kv43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (per_ms)"
    legend_algebraic[64] = "C2Kv43_to_C3Kv43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (per_ms)"
    legend_algebraic[73] = "C3Kv43_to_OKv43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (per_ms)"
    legend_algebraic[83] = "CI0Kv43_to_CI1Kv43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (per_ms)"
    legend_algebraic[93] = "CI1Kv43_to_CI2Kv43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (per_ms)"
    legend_algebraic[103] = "CI2Kv43_to_CI3Kv43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (per_ms)"
    legend_algebraic[113] = "CI3Kv43_to_OIKv43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (per_ms)"
    legend_algebraic[121] = "C1Kv43_to_C0Kv43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (per_ms)"
    legend_algebraic[125] = "C2Kv43_to_C1Kv43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (per_ms)"
    legend_algebraic[129] = "C3Kv43_to_C2Kv43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (per_ms)"
    legend_algebraic[133] = "OKv43_to_C3Kv43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (per_ms)"
    legend_algebraic[137] = "CI1Kv43_to_CI0Kv43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (per_ms)"
    legend_algebraic[142] = "CI2Kv43_to_CI1Kv43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (per_ms)"
    legend_algebraic[147] = "CI3Kv43_to_CI2Kv43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (per_ms)"
    legend_algebraic[153] = "OIKv43_to_CI3Kv43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (per_ms)"
    legend_algebraic[141] = "C0Kv43_to_CI0Kv43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (per_ms)"
    legend_algebraic[146] = "C1Kv43_to_CI1Kv43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (per_ms)"
    legend_algebraic[152] = "C2Kv43_to_CI2Kv43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (per_ms)"
    legend_algebraic[160] = "C3Kv43_to_CI3Kv43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (per_ms)"
    legend_algebraic[161] = "OKv43_to_OIKv43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (per_ms)"
    legend_algebraic[148] = "CI0Kv43_to_C0Kv43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (per_ms)"
    legend_algebraic[154] = "CI1Kv43_to_C1Kv43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (per_ms)"
    legend_algebraic[162] = "CI2Kv43_to_C2Kv43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (per_ms)"
    legend_algebraic[170] = "CI3Kv43_to_C3Kv43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (per_ms)"
    legend_algebraic[171] = "OIKv43_to_OKv43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (per_ms)"
    legend_states[25] = "C0Kv43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (dimensionless)"
    legend_states[26] = "C1Kv43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (dimensionless)"
    legend_states[27] = "C2Kv43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (dimensionless)"
    legend_states[28] = "C3Kv43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (dimensionless)"
    legend_states[29] = "OKv43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (dimensionless)"
    legend_states[30] = "CI0Kv43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (dimensionless)"
    legend_states[31] = "CI1Kv43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (dimensionless)"
    legend_states[32] = "CI2Kv43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (dimensionless)"
    legend_states[33] = "CI3Kv43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (dimensionless)"
    legend_states[34] = "OIKv43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (dimensionless)"
    legend_algebraic[155] = "a1_C043 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (per_ms)"
    legend_algebraic[163] = "a2_C043 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (per_ms)"
    legend_algebraic[164] = "a1_C143 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (per_ms)"
    legend_algebraic[172] = "a2_C143 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (per_ms)"
    legend_algebraic[173] = "a1_C243 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (per_ms)"
    legend_algebraic[181] = "a2_C243 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (per_ms)"
    legend_algebraic[182] = "a1_C343 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (per_ms)"
    legend_algebraic[194] = "a2_C343 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (per_ms)"
    legend_algebraic[183] = "a1_O43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (per_ms)"
    legend_algebraic[195] = "a2_O43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (per_ms)"
    legend_algebraic[156] = "a1_I043 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (per_ms)"
    legend_algebraic[165] = "a2_I043 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (per_ms)"
    legend_algebraic[166] = "a1_I143 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (per_ms)"
    legend_algebraic[174] = "a2_I143 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (per_ms)"
    legend_algebraic[175] = "a1_I243 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (per_ms)"
    legend_algebraic[184] = "a2_I243 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (per_ms)"
    legend_algebraic[185] = "a1_I343 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (per_ms)"
    legend_algebraic[196] = "a2_I343 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (per_ms)"
    legend_algebraic[186] = "a1_OI43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (per_ms)"
    legend_algebraic[197] = "a2_OI43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (per_ms)"
    legend_constants[58] = "alphaa0Kv43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (per_ms)"
    legend_constants[59] = "aaKv43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (per_mV)"
    legend_constants[60] = "betaa0Kv43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (per_ms)"
    legend_constants[61] = "baKv43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (per_mV)"
    legend_constants[62] = "alphai0Kv43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (per_ms)"
    legend_constants[63] = "aiKv43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (per_mV)"
    legend_constants[64] = "betai0Kv43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (per_ms)"
    legend_constants[65] = "biKv43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (per_mV)"
    legend_constants[66] = "f1Kv43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (dimensionless)"
    legend_constants[67] = "f2Kv43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (dimensionless)"
    legend_constants[68] = "f3Kv43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (dimensionless)"
    legend_constants[69] = "f4Kv43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (dimensionless)"
    legend_constants[70] = "b1Kv43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (dimensionless)"
    legend_constants[71] = "b2Kv43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (dimensionless)"
    legend_constants[72] = "b3Kv43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (dimensionless)"
    legend_constants[73] = "b4Kv43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (dimensionless)"
    legend_constants[74] = "f1Kv14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (dimensionless)"
    legend_constants[75] = "f2Kv14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (dimensionless)"
    legend_constants[76] = "f3Kv14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (dimensionless)"
    legend_constants[77] = "f4Kv14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (dimensionless)"
    legend_constants[78] = "b1Kv14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (dimensionless)"
    legend_constants[79] = "b2Kv14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (dimensionless)"
    legend_constants[80] = "b3Kv14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (dimensionless)"
    legend_constants[81] = "b4Kv14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (dimensionless)"
    legend_constants[82] = "alphaa0Kv14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (per_ms)"
    legend_constants[83] = "aaKv14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (per_mV)"
    legend_constants[84] = "betaa0Kv14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (per_ms)"
    legend_constants[85] = "baKv14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (per_mV)"
    legend_constants[86] = "alphai0Kv14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (per_ms)"
    legend_constants[87] = "betai0Kv14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (per_ms)"
    legend_algebraic[5] = "alpha_act14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (per_ms)"
    legend_algebraic[16] = "beta_act14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (per_ms)"
    legend_constants[130] = "alpha_inact14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (per_ms)"
    legend_constants[131] = "beta_inact14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (per_ms)"
    legend_algebraic[26] = "C0Kv14_to_C1Kv14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (per_ms)"
    legend_algebraic[37] = "C1Kv14_to_C2Kv14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (per_ms)"
    legend_algebraic[46] = "C2Kv14_to_C3Kv14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (per_ms)"
    legend_algebraic[55] = "C3Kv14_to_OKv14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (per_ms)"
    legend_algebraic[27] = "CI0Kv14_to_CI1Kv14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (per_ms)"
    legend_algebraic[38] = "CI1Kv14_to_CI2Kv14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (per_ms)"
    legend_algebraic[47] = "CI2Kv14_to_CI3Kv14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (per_ms)"
    legend_algebraic[56] = "CI3Kv14_to_OIKv14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (per_ms)"
    legend_algebraic[65] = "C1Kv14_to_C0Kv14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (per_ms)"
    legend_algebraic[74] = "C2Kv14_to_C1Kv14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (per_ms)"
    legend_algebraic[84] = "C3Kv14_to_C2Kv14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (per_ms)"
    legend_algebraic[94] = "OKv14_to_C3Kv14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (per_ms)"
    legend_algebraic[66] = "CI1Kv14_to_CI0Kv14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (per_ms)"
    legend_algebraic[75] = "CI2Kv14_to_CI1Kv14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (per_ms)"
    legend_algebraic[85] = "CI3Kv14_to_CI2Kv14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (per_ms)"
    legend_algebraic[95] = "OIKv14_to_CI3Kv14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (per_ms)"
    legend_constants[144] = "C0Kv14_to_CI0Kv14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (per_ms)"
    legend_constants[145] = "C1Kv14_to_CI1Kv14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (per_ms)"
    legend_constants[146] = "C2Kv14_to_CI2Kv14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (per_ms)"
    legend_constants[147] = "C3Kv14_to_CI3Kv14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (per_ms)"
    legend_constants[148] = "OKv14_to_OIKv14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (per_ms)"
    legend_constants[149] = "CI0Kv14_to_C0Kv14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (per_ms)"
    legend_constants[150] = "CI1Kv14_to_C1Kv14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (per_ms)"
    legend_constants[151] = "CI2Kv14_to_C2Kv14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (per_ms)"
    legend_constants[152] = "CI3Kv14_to_C3Kv14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (per_ms)"
    legend_constants[153] = "OIKv14_to_OKv14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (per_ms)"
    legend_algebraic[76] = "a1_C0 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (per_ms)"
    legend_algebraic[86] = "a2_C0 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (per_ms)"
    legend_states[35] = "C0Kv14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (dimensionless)"
    legend_algebraic[87] = "a1_C1 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (per_ms)"
    legend_algebraic[96] = "a2_C1 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (per_ms)"
    legend_states[36] = "C1Kv14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (dimensionless)"
    legend_algebraic[97] = "a1_C2 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (per_ms)"
    legend_algebraic[104] = "a2_C2 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (per_ms)"
    legend_states[37] = "C2Kv14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (dimensionless)"
    legend_algebraic[105] = "a1_C3 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (per_ms)"
    legend_algebraic[114] = "a2_C3 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (per_ms)"
    legend_states[38] = "C3Kv14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (dimensionless)"
    legend_algebraic[106] = "a1_O in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (per_ms)"
    legend_algebraic[115] = "a2_O in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (per_ms)"
    legend_states[39] = "OKv14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (dimensionless)"
    legend_algebraic[77] = "a1_CI0 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (per_ms)"
    legend_algebraic[88] = "a2_CI0 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (per_ms)"
    legend_states[40] = "CI0Kv14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (dimensionless)"
    legend_algebraic[89] = "a1_CI1 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (per_ms)"
    legend_algebraic[98] = "a2_CI1 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (per_ms)"
    legend_states[41] = "CI1Kv14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (dimensionless)"
    legend_algebraic[99] = "a1_CI2 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (per_ms)"
    legend_algebraic[107] = "a2_CI2 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (per_ms)"
    legend_states[42] = "CI2Kv14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (dimensionless)"
    legend_algebraic[108] = "a1_CI3 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (per_ms)"
    legend_algebraic[116] = "a2_CI3 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (per_ms)"
    legend_states[43] = "CI3Kv14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (dimensionless)"
    legend_algebraic[109] = "a1_OI in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (per_ms)"
    legend_algebraic[117] = "a2_OI in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (per_ms)"
    legend_states[44] = "OIKv14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (dimensionless)"
    legend_algebraic[119] = "ENa in component COMPUTE_REVERSAL_POTENTIALS (mV)"
    legend_algebraic[123] = "EK in component COMPUTE_REVERSAL_POTENTIALS (mV)"
    legend_algebraic[17] = "EKs in component COMPUTE_REVERSAL_POTENTIALS (mV)"
    legend_algebraic[127] = "ECa in component COMPUTE_REVERSAL_POTENTIALS (mV)"
    legend_constants[154] = "a1 in component COMPUTE_REVERSAL_POTENTIALS (mM)"
    legend_algebraic[6] = "a2 in component COMPUTE_REVERSAL_POTENTIALS (mM)"
    legend_constants[88] = "GKr in component COMPUTE_INa_IKr_IKs_Ito1_IK1_INab_IKp (mS_per_uF)"
    legend_constants[89] = "GKs in component COMPUTE_INa_IKr_IKs_Ito1_IK1_INab_IKp (mS_per_uF)"
    legend_constants[90] = "GK1 in component COMPUTE_INa_IKr_IKs_Ito1_IK1_INab_IKp (mS_per_uF)"
    legend_constants[91] = "GNa in component COMPUTE_INa_IKr_IKs_Ito1_IK1_INab_IKp (mS_per_uF)"
    legend_constants[92] = "GNab in component COMPUTE_INa_IKr_IKs_Ito1_IK1_INab_IKp (mS_per_uF)"
    legend_constants[93] = "KvScale in component COMPUTE_INa_IKr_IKs_Ito1_IK1_INab_IKp (dimensionless)"
    legend_constants[94] = "Kv43Frac in component COMPUTE_INa_IKr_IKs_Ito1_IK1_INab_IKp (dimensionless)"
    legend_constants[132] = "GKv43 in component COMPUTE_INa_IKr_IKs_Ito1_IK1_INab_IKp (mS_per_uF)"
    legend_constants[133] = "PKv14 in component COMPUTE_INa_IKr_IKs_Ito1_IK1_INab_IKp (litre_per_farad_second)"
    legend_states[45] = "na6 in component INa (dimensionless)"
    legend_states[46] = "na7 in component INa (dimensionless)"
    legend_states[47] = "OHerg in component IKr (dimensionless)"
    legend_states[48] = "O1ks in component IKs (dimensionless)"
    legend_states[49] = "O2ks in component IKs (dimensionless)"
    legend_constants[134] = "fKo in component COMPUTE_INa_IKr_IKs_Ito1_IK1_INab_IKp (dimensionless)"
    legend_algebraic[150] = "VF_over_RT in component COMPUTE_INa_IKr_IKs_Ito1_IK1_INab_IKp (dimensionless)"
    legend_algebraic[158] = "VFsq_over_RT in component COMPUTE_INa_IKr_IKs_Ito1_IK1_INab_IKp (coulomb_per_millimole)"
    legend_algebraic[168] = "a1_K in component COMPUTE_INa_IKr_IKs_Ito1_IK1_INab_IKp (mM)"
    legend_algebraic[177] = "a2 in component COMPUTE_INa_IKr_IKs_Ito1_IK1_INab_IKp (dimensionless)"
    legend_algebraic[199] = "a1_Na in component COMPUTE_INa_IKr_IKs_Ito1_IK1_INab_IKp (mM)"
    legend_algebraic[224] = "K1_inf in component COMPUTE_INa_IKr_IKs_Ito1_IK1_INab_IKp (dimensionless)"
    legend_algebraic[213] = "IKv14 in component COMPUTE_INa_IKr_IKs_Ito1_IK1_INab_IKp (uA_per_uF)"
    legend_constants[95] = "kNaCa in component COMPUTE_INaK_INaCa_ICab_IpCa (uA_per_uF)"
    legend_constants[96] = "KmNa in component COMPUTE_INaK_INaCa_ICab_IpCa (mM)"
    legend_constants[97] = "KmCa in component COMPUTE_INaK_INaCa_ICab_IpCa (mM)"
    legend_constants[98] = "ksat in component COMPUTE_INaK_INaCa_ICab_IpCa (dimensionless)"
    legend_constants[99] = "eta in component COMPUTE_INaK_INaCa_ICab_IpCa (dimensionless)"
    legend_constants[100] = "INaKmax in component COMPUTE_INaK_INaCa_ICab_IpCa (uA_per_uF)"
    legend_constants[101] = "KmNai in component COMPUTE_INaK_INaCa_ICab_IpCa (mM)"
    legend_constants[102] = "KmKo in component COMPUTE_INaK_INaCa_ICab_IpCa (mM)"
    legend_constants[103] = "IpCamax in component COMPUTE_INaK_INaCa_ICab_IpCa (uA_per_uF)"
    legend_constants[104] = "KmpCa in component COMPUTE_INaK_INaCa_ICab_IpCa (mM)"
    legend_constants[105] = "GCab in component COMPUTE_INaK_INaCa_ICab_IpCa (mS_per_uF)"
    legend_algebraic[234] = "VF_over_RT in component COMPUTE_INaK_INaCa_ICab_IpCa (dimensionless)"
    legend_constants[163] = "sigma in component COMPUTE_INaK_INaCa_ICab_IpCa (dimensionless)"
    legend_algebraic[235] = "a1_Na in component COMPUTE_INaK_INaCa_ICab_IpCa (dimensionless)"
    legend_algebraic[236] = "a2_Na in component COMPUTE_INaK_INaCa_ICab_IpCa (dimensionless)"
    legend_algebraic[237] = "fNaK in component COMPUTE_INaK_INaCa_ICab_IpCa (dimensionless)"
    legend_constants[167] = "a1_K in component COMPUTE_INaK_INaCa_ICab_IpCa (dimensionless)"
    legend_algebraic[238] = "a2_K in component COMPUTE_INaK_INaCa_ICab_IpCa (dimensionless)"
    legend_algebraic[240] = "a1_ncx in component COMPUTE_INaK_INaCa_ICab_IpCa (mM4)"
    legend_algebraic[241] = "a2_ncx in component COMPUTE_INaK_INaCa_ICab_IpCa (mM4)"
    legend_algebraic[242] = "a3_ncx in component COMPUTE_INaK_INaCa_ICab_IpCa (dimensionless)"
    legend_constants[172] = "a4_ncx in component COMPUTE_INaK_INaCa_ICab_IpCa (mM)"
    legend_constants[175] = "a5_ncx in component COMPUTE_INaK_INaCa_ICab_IpCa (mM3)"
    legend_algebraic[251] = "PKprime in component COMPUTE_ICa_ICaK (litre_per_farad_second)"
    legend_algebraic[244] = "VF_over_RT in component COMPUTE_ICa_ICaK (dimensionless)"
    legend_algebraic[245] = "VFsq_over_RT in component COMPUTE_ICa_ICaK (coulomb_per_millimole)"
    legend_algebraic[246] = "a1_Ca in component COMPUTE_ICa_ICaK (mM)"
    legend_algebraic[247] = "a2_Ca in component COMPUTE_ICa_ICaK (dimensionless)"
    legend_algebraic[252] = "a1_K in component COMPUTE_ICa_ICaK (mM)"
    legend_algebraic[253] = "a2_K in component COMPUTE_ICa_ICaK (dimensionless)"
    legend_algebraic[248] = "ICamax in component COMPUTE_ICa_ICaK (uA_per_uF)"
    legend_algebraic[250] = "Icabar in component COMPUTE_ICa_ICaK (uA_per_uF)"
    legend_constants[156] = "PCa in component COMPUTE_ICa_ICaK (litre_per_farad_second)"
    legend_constants[136] = "PK in component COMPUTE_ICa_ICaK (litre_per_farad_second)"
    legend_constants[106] = "ICahalf in component COMPUTE_ICa_ICaK (uA_per_uF)"
    legend_constants[107] = "Pscale in component COMPUTE_ICa_ICaK (dimensionless)"
    legend_constants[161] = "Temp_Scale in component INa (dimensionless)"
    legend_algebraic[7] = "alpha1 in component INa (per_ms)"
    legend_algebraic[18] = "beta1 in component INa (per_ms)"
    legend_algebraic[28] = "gamma1 in component INa (per_ms)"
    legend_algebraic[39] = "Delta1 in component INa (per_ms)"
    legend_algebraic[48] = "On in component INa (per_ms)"
    legend_algebraic[57] = "Of in component INa (per_ms)"
    legend_algebraic[67] = "GammaGamma in component INa (per_ms)"
    legend_algebraic[78] = "DeltaDelta in component INa (per_ms)"
    legend_constants[165] = "epsilon in component INa (per_ms)"
    legend_constants[166] = "omega_na in component INa (per_ms)"
    legend_algebraic[90] = "rho in component INa (per_ms)"
    legend_algebraic[100] = "mu in component INa (per_ms)"
    legend_constants[164] = "Cn in component INa (per_ms)"
    legend_constants[169] = "Cf in component INa (per_ms)"
    legend_constants[174] = "parameter_a in component INa (dimensionless)"
    legend_algebraic[110] = "k12 in component INa (per_ms)"
    legend_algebraic[118] = "k23 in component INa (per_ms)"
    legend_algebraic[122] = "k34 in component INa (per_ms)"
    legend_algebraic[126] = "k45 in component INa (per_ms)"
    legend_algebraic[130] = "k56 in component INa (per_ms)"
    legend_constants[170] = "k67 in component INa (per_ms)"
    legend_algebraic[134] = "k89 in component INa (per_ms)"
    legend_algebraic[138] = "k910 in component INa (per_ms)"
    legend_algebraic[143] = "k1011 in component INa (per_ms)"
    legend_algebraic[149] = "k1112 in component INa (per_ms)"
    legend_algebraic[157] = "k1213 in component INa (per_ms)"
    legend_algebraic[167] = "k57 in component INa (per_ms)"
    legend_algebraic[176] = "k21 in component INa (per_ms)"
    legend_algebraic[187] = "k32 in component INa (per_ms)"
    legend_algebraic[198] = "k43 in component INa (per_ms)"
    legend_algebraic[205] = "k54 in component INa (per_ms)"
    legend_algebraic[212] = "k65 in component INa (per_ms)"
    legend_constants[171] = "k76 in component INa (per_ms)"
    legend_algebraic[218] = "k98 in component INa (per_ms)"
    legend_algebraic[223] = "k109 in component INa (per_ms)"
    legend_algebraic[225] = "k1110 in component INa (per_ms)"
    legend_algebraic[227] = "k1211 in component INa (per_ms)"
    legend_algebraic[229] = "k1312 in component INa (per_ms)"
    legend_algebraic[219] = "k75 in component INa (per_ms)"
    legend_constants[176] = "k81 in component INa (per_ms)"
    legend_constants[178] = "k92 in component INa (per_ms)"
    legend_constants[180] = "k103 in component INa (per_ms)"
    legend_constants[182] = "k114 in component INa (per_ms)"
    legend_constants[184] = "k125 in component INa (per_ms)"
    legend_algebraic[231] = "k136 in component INa (per_ms)"
    legend_constants[177] = "k18 in component INa (per_ms)"
    legend_constants[179] = "k29 in component INa (per_ms)"
    legend_constants[181] = "k310 in component INa (per_ms)"
    legend_constants[183] = "k411 in component INa (per_ms)"
    legend_constants[185] = "k512 in component INa (per_ms)"
    legend_algebraic[233] = "k613 in component INa (per_ms)"
    legend_states[50] = "na1 in component INa (dimensionless)"
    legend_states[51] = "na2 in component INa (dimensionless)"
    legend_states[52] = "na3 in component INa (dimensionless)"
    legend_states[53] = "na4 in component INa (dimensionless)"
    legend_states[54] = "na5 in component INa (dimensionless)"
    legend_states[55] = "na8 in component INa (dimensionless)"
    legend_states[56] = "na9 in component INa (dimensionless)"
    legend_states[57] = "na10 in component INa (dimensionless)"
    legend_states[58] = "na11 in component INa (dimensionless)"
    legend_states[59] = "na12 in component INa (dimensionless)"
    legend_states[60] = "na13 in component INa (dimensionless)"
    legend_constants[108] = "TNa in component INa (kelvin)"
    legend_constants[137] = "KToverH in component INa (per_ms)"
    legend_constants[158] = "FoverRT in component INa (per_mV)"
    legend_constants[157] = "RTNa in component INa (joule_per_mole)"
    legend_constants[138] = "RTNaF in component INa (mV)"
    legend_constants[109] = "T_Const_HERG in component IKr (dimensionless)"
    legend_constants[110] = "A0_HERG in component IKr (per_ms)"
    legend_constants[111] = "B0_HERG in component IKr (per_mV)"
    legend_constants[112] = "A1_HERG in component IKr (per_ms)"
    legend_constants[113] = "B1_HERG in component IKr (per_mV)"
    legend_constants[114] = "A2_HERG in component IKr (per_ms)"
    legend_constants[115] = "B2_HERG in component IKr (per_mV)"
    legend_constants[116] = "A3_HERG in component IKr (per_ms)"
    legend_constants[117] = "B3_HERG in component IKr (per_mV)"
    legend_constants[118] = "A4_HERG in component IKr (per_ms)"
    legend_constants[119] = "B4_HERG in component IKr (per_mV)"
    legend_constants[120] = "A5_HERG in component IKr (per_ms)"
    legend_constants[121] = "B5_HERG in component IKr (per_mV)"
    legend_constants[122] = "A6_HERG in component IKr (per_ms)"
    legend_constants[123] = "B6_HERG in component IKr (per_mV)"
    legend_constants[139] = "C2H_to_C3H in component IKr (per_ms)"
    legend_constants[140] = "C3H_to_C2H in component IKr (per_ms)"
    legend_algebraic[8] = "C1H_to_C2H in component IKr (per_ms)"
    legend_algebraic[19] = "C2H_to_C1H in component IKr (per_ms)"
    legend_algebraic[9] = "C3H_to_OH in component IKr (per_ms)"
    legend_algebraic[20] = "OH_to_C3H in component IKr (per_ms)"
    legend_algebraic[29] = "OH_to_IH in component IKr (per_ms)"
    legend_algebraic[40] = "IH_to_OH in component IKr (per_ms)"
    legend_algebraic[49] = "C3H_to_IH in component IKr (per_ms)"
    legend_algebraic[58] = "IH_to_C3H in component IKr (per_ms)"
    legend_states[61] = "C1Herg in component IKr (dimensionless)"
    legend_algebraic[30] = "a1_C2 in component IKr (per_ms)"
    legend_algebraic[41] = "a2_C2 in component IKr (per_ms)"
    legend_states[62] = "C2Herg in component IKr (dimensionless)"
    legend_algebraic[68] = "a1_C3 in component IKr (per_ms)"
    legend_algebraic[79] = "a2_C3 in component IKr (per_ms)"
    legend_states[63] = "C3Herg in component IKr (dimensionless)"
    legend_algebraic[50] = "a1_O in component IKr (per_ms)"
    legend_algebraic[59] = "a2_O in component IKr (per_ms)"
    legend_algebraic[69] = "a1_I in component IKr (per_ms)"
    legend_algebraic[80] = "a2_I in component IKr (per_ms)"
    legend_states[64] = "IHerg in component IKr (dimensionless)"
    legend_constants[141] = "C0ks_C1ks in component IKs (per_ms)"
    legend_constants[142] = "C1ks_O1ks in component IKs (per_ms)"
    legend_algebraic[10] = "O1ks_O2ks in component IKs (per_ms)"
    legend_algebraic[21] = "O1ks_C1ks in component IKs (per_ms)"
    legend_algebraic[31] = "O2ks_O1ks in component IKs (per_ms)"
    legend_algebraic[32] = "C1ks_C0ks in component IKs (per_ms)"
    legend_states[65] = "C0ks in component IKs (dimensionless)"
    legend_states[66] = "C1ks in component IKs (dimensionless)"
    legend_rates[0] = "d/dt Nai in component COMPUTE_CONCENTRATION_AND_VOLTAGE_DERIVATIVES (mM)"
    legend_rates[1] = "d/dt Ki in component COMPUTE_CONCENTRATION_AND_VOLTAGE_DERIVATIVES (mM)"
    legend_rates[2] = "d/dt Cai in component COMPUTE_CONCENTRATION_AND_VOLTAGE_DERIVATIVES (mM)"
    legend_rates[3] = "d/dt CaSS in component COMPUTE_CONCENTRATION_AND_VOLTAGE_DERIVATIVES (mM)"
    legend_rates[4] = "d/dt CaJSR in component COMPUTE_CONCENTRATION_AND_VOLTAGE_DERIVATIVES (mM)"
    legend_rates[5] = "d/dt CaNSR in component COMPUTE_CONCENTRATION_AND_VOLTAGE_DERIVATIVES (mM)"
    legend_rates[6] = "d/dt V in component COMPUTE_CONCENTRATION_AND_VOLTAGE_DERIVATIVES (mV)"
    legend_rates[9] = "d/dt LTRPNCa in component COMPUTE_Jtrpn_and_BUFFER_SCALE_FACTORS (dimensionless)"
    legend_rates[10] = "d/dt HTRPNCa in component COMPUTE_Jtrpn_and_BUFFER_SCALE_FACTORS (dimensionless)"
    legend_rates[11] = "d/dt C1_RyR in component COMPUTE_DERIVATIVES_OF_RyR_RECEPTOR_STATES (dimensionless)"
    legend_rates[8] = "d/dt O2_RyR in component COMPUTE_DERIVATIVES_OF_RyR_RECEPTOR_STATES (dimensionless)"
    legend_rates[12] = "d/dt C2_RyR in component COMPUTE_DERIVATIVES_OF_RyR_RECEPTOR_STATES (dimensionless)"
    legend_rates[7] = "d/dt O1_RyR in component COMPUTE_DERIVATIVES_OF_RyR_RECEPTOR_STATES (dimensionless)"
    legend_rates[13] = "d/dt C0 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (dimensionless)"
    legend_rates[14] = "d/dt C1 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (dimensionless)"
    legend_rates[15] = "d/dt C2 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (dimensionless)"
    legend_rates[16] = "d/dt C3 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (dimensionless)"
    legend_rates[17] = "d/dt C4 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (dimensionless)"
    legend_rates[23] = "d/dt Open in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (dimensionless)"
    legend_rates[18] = "d/dt CCa0 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (dimensionless)"
    legend_rates[19] = "d/dt CCa1 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (dimensionless)"
    legend_rates[20] = "d/dt CCa2 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (dimensionless)"
    legend_rates[21] = "d/dt CCa3 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (dimensionless)"
    legend_rates[22] = "d/dt CCa4 in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (dimensionless)"
    legend_rates[24] = "d/dt yCa in component COMPUTE_DERIVATIVES_OF_LTYPE_CHANNEL_STATES (dimensionless)"
    legend_rates[25] = "d/dt C0Kv43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (dimensionless)"
    legend_rates[26] = "d/dt C1Kv43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (dimensionless)"
    legend_rates[27] = "d/dt C2Kv43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (dimensionless)"
    legend_rates[28] = "d/dt C3Kv43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (dimensionless)"
    legend_rates[29] = "d/dt OKv43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (dimensionless)"
    legend_rates[30] = "d/dt CI0Kv43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (dimensionless)"
    legend_rates[31] = "d/dt CI1Kv43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (dimensionless)"
    legend_rates[32] = "d/dt CI2Kv43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (dimensionless)"
    legend_rates[33] = "d/dt CI3Kv43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (dimensionless)"
    legend_rates[34] = "d/dt OIKv43 in component COMPUTE_DERIVATIVES_OF_Kv4_3_CHANNEL_STATES (dimensionless)"
    legend_rates[35] = "d/dt C0Kv14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (dimensionless)"
    legend_rates[36] = "d/dt C1Kv14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (dimensionless)"
    legend_rates[37] = "d/dt C2Kv14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (dimensionless)"
    legend_rates[38] = "d/dt C3Kv14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (dimensionless)"
    legend_rates[39] = "d/dt OKv14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (dimensionless)"
    legend_rates[40] = "d/dt CI0Kv14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (dimensionless)"
    legend_rates[41] = "d/dt CI1Kv14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (dimensionless)"
    legend_rates[42] = "d/dt CI2Kv14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (dimensionless)"
    legend_rates[43] = "d/dt CI3Kv14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (dimensionless)"
    legend_rates[44] = "d/dt OIKv14 in component COMPUTE_DERIVATIVES_OF_Kv1_4_CHANNEL_STATES (dimensionless)"
    legend_rates[50] = "d/dt na1 in component INa (dimensionless)"
    legend_rates[51] = "d/dt na2 in component INa (dimensionless)"
    legend_rates[52] = "d/dt na3 in component INa (dimensionless)"
    legend_rates[53] = "d/dt na4 in component INa (dimensionless)"
    legend_rates[54] = "d/dt na5 in component INa (dimensionless)"
    legend_rates[45] = "d/dt na6 in component INa (dimensionless)"
    legend_rates[46] = "d/dt na7 in component INa (dimensionless)"
    legend_rates[55] = "d/dt na8 in component INa (dimensionless)"
    legend_rates[56] = "d/dt na9 in component INa (dimensionless)"
    legend_rates[57] = "d/dt na10 in component INa (dimensionless)"
    legend_rates[58] = "d/dt na11 in component INa (dimensionless)"
    legend_rates[59] = "d/dt na12 in component INa (dimensionless)"
    legend_rates[60] = "d/dt na13 in component INa (dimensionless)"
    legend_rates[61] = "d/dt C1Herg in component IKr (dimensionless)"
    legend_rates[62] = "d/dt C2Herg in component IKr (dimensionless)"
    legend_rates[63] = "d/dt C3Herg in component IKr (dimensionless)"
    legend_rates[47] = "d/dt OHerg in component IKr (dimensionless)"
    legend_rates[64] = "d/dt IHerg in component IKr (dimensionless)"
    legend_rates[65] = "d/dt C0ks in component IKs (dimensionless)"
    legend_rates[66] = "d/dt C1ks in component IKs (dimensionless)"
    legend_rates[48] = "d/dt O1ks in component IKs (dimensionless)"
    legend_rates[49] = "d/dt O2ks in component IKs (dimensionless)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    constants[0] = 0
    constants[1] = 0
    constants[2] = 0
    constants[3] = 96.5
    constants[4] = 310
    constants[5] = 8.315
    constants[6] = 0.0001534
    constants[7] = 2.584e-5
    constants[8] = 1.6e-7
    constants[9] = 2.1e-6
    constants[10] = 1.2e-9
    states[0] = 9.85573275838928
    states[1] = 125.427082712469
    states[2] = 0.000363968672182656
    states[3] = 0.000506604278037024
    states[4] = 0.421936980515042
    states[5] = 0.423551621440241
    states[6] = -86.7261544519706
    constants[11] = 4
    constants[12] = 138
    constants[13] = 2
    constants[14] = 500
    constants[15] = 3
    constants[16] = -15
    constants[17] = 100
    constants[18] = 0.000168
    constants[19] = 1.2
    constants[20] = 3.29
    constants[21] = 1
    constants[22] = 1.2
    constants[23] = 7.48e-5
    constants[24] = 0.000318
    constants[25] = 1.8
    states[7] = 0.00113684728532807
    states[8] = 3.11350788541838e-7
    constants[26] = 0.5747
    constants[27] = 26.7
    constants[28] = 0.07
    constants[29] = 0.14
    constants[30] = 20
    constants[31] = 6.6e-5
    constants[32] = 40
    constants[33] = 0.04
    constants[34] = 0.05
    constants[35] = 0
    constants[36] = 0.00238
    constants[37] = 0.8
    constants[38] = 0.00015
    states[9] = 0.280466039150394
    states[10] = 0.99347761599363
    constants[39] = 0.01215
    constants[40] = 0.576
    constants[41] = 0.00405
    constants[42] = 1.93
    constants[43] = 0.1
    constants[44] = 0.0008
    constants[45] = 4
    constants[46] = 3
    constants[47] = 1
    constants[48] = 0.5
    constants[49] = 0.5
    constants[50] = 5
    constants[51] = 1
    constants[52] = 1
    constants[53] = 2.5
    states[11] = 0.132070890861418
    states[12] = 0.866791951404883
    constants[54] = 0.3
    constants[55] = 4
    constants[56] = 2
    constants[57] = 2
    states[13] = 0.465679150104636
    states[14] = 0.00834457719966281
    states[15] = 5.60736209083906e-5
    states[16] = 1.6747092904465e-7
    states[17] = 1.87571666668874e-10
    states[18] = 0.489846779190386
    states[19] = 0.035111008610982
    states[20] = 0.000943745917866092
    states[21] = 1.12741202215634e-5
    states[22] = 5.05056944609524e-8
    states[23] = 1.40806027419488e-11
    states[24] = 0.995434385054729
    states[25] = 0.908189132330738
    states[26] = 0.0343385704915328
    states[27] = 0.000487654173162347
    states[28] = 3.11550715247964e-6
    states[29] = 7.42911977991342e-9
    states[30] = 0.0349937004781012
    states[31] = 0.0171163265867255
    states[32] = 0.00428471710061031
    states[33] = 0.000564724236640674
    states[34] = 2.19603439704397e-5
    constants[58] = 0.543708
    constants[59] = 0.028983
    constants[60] = 0.080185
    constants[61] = 0.0468437
    constants[62] = 0.0498424
    constants[63] = 0.000373016
    constants[64] = 0.000819482
    constants[65] = 5.374e-8
    constants[66] = 1.8936
    constants[67] = 14.224647456
    constants[68] = 158.574378389
    constants[69] = 142.936645351
    constants[70] = 6.77348
    constants[71] = 15.6212705152
    constants[72] = 28.7532603313
    constants[73] = 524.576206679
    constants[74] = 0.52465073996
    constants[75] = 17.51885408639
    constants[76] = 938.58764534556
    constants[77] = 54749.194733326
    constants[78] = 1.00947847105
    constants[79] = 1.17100540567
    constants[80] = 0.63902768758
    constants[81] = 2.12035379095
    constants[82] = 1.84002414554
    constants[83] = 0.00768548031
    constants[84] = 0.0108174834
    constants[85] = 0.07793378174
    constants[86] = 0.00305767916
    constants[87] = 2.44936e-6
    states[35] = 0.149374350989705
    states[36] = 0.0606794865684932
    states[37] = 0.00930314185504921
    states[38] = 0.000676403999474111
    states[39] = 3.85187206387239e-5
    states[40] = 0.0442722560882536
    states[41] = 0.00952432663172288
    states[42] = 0.0567396669678271
    states[43] = 0.113122845136053
    states[44] = 0.556269044084734
    constants[88] = 0.0186
    constants[89] = 0.0035
    constants[90] = 0.125305126118808
    constants[91] = 56.32
    constants[92] = 0.001
    constants[93] = 0.872
    constants[94] = 0.889
    states[45] = 1.02118700961583e-7
    states[46] = 1.93499158844817e-8
    states[47] = 0.00120284688677794
    states[48] = 5.65460174551007e-7
    states[49] = 0.0258818770122187
    constants[95] = 0.44
    constants[96] = 87.5
    constants[97] = 1.38
    constants[98] = 0.2
    constants[99] = 0.35
    constants[100] = 2.387
    constants[101] = 20
    constants[102] = 1.5
    constants[103] = 0.05
    constants[104] = 0.0005
    constants[105] = 7.684e-5
    constants[106] = -0.265
    constants[107] = 7
    states[50] = 0.111284526171411
    states[51] = 0.0481019786429977
    states[52] = 0.00779692701457915
    states[53] = 0.000561699600929369
    states[54] = 1.51746424723121e-5
    states[55] = 0.368582741846592
    states[56] = 0.312463212648791
    states[57] = 0.0993398770493615
    states[58] = 0.0140431688972267
    states[59] = 0.000750073829883749
    states[60] = 0.0370604970714329
    constants[108] = 294.16
    constants[109] = 5.320000001
    constants[110] = 0.017147641733086
    constants[111] = 0.03304608038835
    constants[112] = 0.03969328381141
    constants[113] = -0.0430605416398
    constants[114] = 0.02057448605977
    constants[115] = 0.02617412715118
    constants[116] = 0.00134366604423
    constants[117] = -0.02691385498399
    constants[118] = 0.10666316491288
    constants[119] = 0.00568908859717
    constants[120] = 0.00646393910049
    constants[121] = -0.04536642959543
    constants[122] = 8.039374403e-5
    constants[123] = 6.9808924e-7
    states[61] = 0.994948338598163
    states[62] = 0.000595653663190548
    states[63] = 0.000228183228829573
    states[64] = 0.000243789721526602
    states[65] = 0.938064990549233
    states[66] = 0.0360525668093578
    constants[124] = (constants[5]*constants[4])/constants[3]
    constants[125] = custom_piecewise([equal(constants[2] , 1.00000), 15.0000 , True, 0.500000*15.0000])
    constants[126] = custom_piecewise([equal(constants[1] , 1.00000), 0.200000 , True, 0.500000])
    constants[127] = custom_piecewise([equal(constants[1] , 1.00000), 0.500000 , True, 1.00000])
    constants[128] = 0.250000*0.0100000
    constants[129] = 0.820000
    constants[130] = constants[86]
    constants[131] = constants[87]
    constants[132] = constants[94]*constants[93]*0.100000
    constants[133] = (1.00000-constants[94])*constants[93]*4.29860e-07
    constants[134] = power(constants[11]/4.00000, 1.0/2)
    constants[135] = constants[6]*0.00100000
    constants[136] = constants[107]*4.57400e-07
    constants[137] = (1.38100e-23*constants[108])/6.62600e-31
    constants[138] = (constants[5]*constants[108])/constants[3]
    constants[139] = constants[109]*0.0260836
    constants[140] = constants[109]*0.148330
    constants[141] = 0.00795601
    constants[142] = 0.0396672
    constants[143] = constants[128]
    constants[144] = constants[131]
    constants[145] = constants[74]*constants[131]
    constants[146] = constants[75]*constants[131]
    constants[147] = constants[76]*constants[131]
    constants[148] = constants[77]*constants[131]
    constants[149] = constants[130]
    constants[150] = constants[130]/constants[78]
    constants[151] = constants[130]/constants[79]
    constants[152] = constants[130]/constants[80]
    constants[153] = constants[130]/constants[81]
    constants[154] = constants[11]+0.0183300*constants[12]
    constants[155] = constants[135]/(constants[7]*constants[3])
    constants[156] = custom_piecewise([equal(constants[0] , 0.00000), constants[107]*0.000246900 , True, 1.50000*constants[107]*0.000246900])
    constants[157] = constants[5]*constants[108]
    constants[158] = 1.00000/constants[124]
    constants[159] = constants[143]/constants[56]
    constants[160] = constants[135]/(2.00000*constants[10]*constants[3])
    constants[161] = 1.38862
    constants[162] = constants[159]/constants[56]
    constants[163] = (exp(constants[12]/67.3000)-1.00000)/7.00000
    constants[164] = constants[161]*constants[137]*exp(-287913./constants[157]+786.217/constants[5])
    constants[165] = constants[161]*constants[137]*exp(-85800.4/constants[157]+70.0780/constants[5])
    constants[166] = constants[161]*constants[137]*exp(-121955./constants[157]+225.175/constants[5])
    constants[167] = constants[11]/(constants[11]+constants[102])
    constants[168] = constants[162]/constants[56]
    constants[169] = constants[161]*constants[137]*exp(-59565.2/constants[157]+0.00711000/constants[5])
    constants[170] = constants[165]
    constants[171] = constants[166]
    constants[172] = constants[97]+constants[13]
    constants[173] = constants[168]/constants[56]
    constants[174] = 1.40043
    constants[175] = (power(constants[96], 3.00000)+power(constants[12], 3.00000))/5000.00
    constants[176] = constants[169]
    constants[177] = constants[164]
    constants[178] = constants[176]/constants[174]
    constants[179] = constants[177]*constants[174]
    constants[180] = constants[178]/constants[174]
    constants[181] = constants[179]*constants[174]
    constants[182] = constants[180]/constants[174]
    constants[183] = constants[181]*constants[174]
    constants[184] = constants[182]/constants[174]
    constants[185] = constants[183]*constants[174]
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[23] = constants[54]*states[17]-constants[55]*states[23]
    algebraic[3] = (constants[129]/(1.00000+exp((states[6]+28.5000)/7.80000))+1.00000)-constants[129]
    algebraic[14] = 1.00000/(0.00336336/(0.500000+exp(states[6]/-5.53900))+0.00779047*exp(states[6]/-49.5104))
    rates[24] = (algebraic[3]-states[24])/algebraic[14]
    algebraic[8] = constants[109]*constants[110]*exp(constants[111]*states[6])
    algebraic[19] = constants[109]*constants[112]*exp(constants[113]*states[6])
    rates[61] = algebraic[19]*states[62]-algebraic[8]*states[61]
    algebraic[32] = 0.216256*exp(-1.88912e-05*states[6])
    rates[65] = -constants[141]*states[65]+algebraic[32]*states[66]
    algebraic[21] = 0.00700807*exp(-0.149998*states[6])
    rates[66] = (constants[141]*states[65]-(algebraic[32]+constants[142])*states[66])+algebraic[21]*states[48]
    algebraic[10] = 0.00767254*exp(0.0866295*states[6])
    algebraic[31] = 0.00379738*exp(-0.0142567*states[6])
    rates[48] = (constants[142]*states[66]-(algebraic[21]+algebraic[10])*states[48])+algebraic[31]*states[49]
    rates[49] = algebraic[10]*states[48]-algebraic[31]*states[49]
    algebraic[1] = constants[48]-(constants[48]-constants[50])/(1.00000+power(constants[51]/states[4], constants[53]))
    algebraic[34] = -constants[39]*algebraic[1]*(power(states[3]*1000.00, constants[45]*constants[47]))*states[11]+constants[40]*states[7]
    rates[11] = algebraic[34]
    algebraic[30] = algebraic[8]*states[61]+constants[140]*states[63]
    algebraic[41] = (algebraic[19]+constants[139])*states[62]
    rates[62] = algebraic[30]-algebraic[41]
    algebraic[43] = constants[41]*(power(states[3]*1000.00, constants[46]*constants[47]))*states[7]-constants[42]*states[8]
    rates[8] = algebraic[43]
    algebraic[12] = constants[126]-(constants[126]-constants[50])/(1.00000+power(constants[52]/states[4], constants[53]))
    algebraic[23] = constants[49]-(constants[49]-constants[50])/(1.00000+power(constants[127]/states[4], constants[53]))
    algebraic[52] = (constants[43]/algebraic[12])*states[7]-constants[44]*algebraic[23]*states[12]
    rates[12] = algebraic[52]
    algebraic[9] = constants[109]*constants[114]*exp(constants[115]*states[6])
    algebraic[40] = constants[109]*constants[120]*exp(constants[121]*states[6])
    algebraic[50] = algebraic[9]*states[63]+algebraic[40]*states[64]
    algebraic[20] = constants[109]*constants[116]*exp(constants[117]*states[6])
    algebraic[29] = constants[109]*constants[118]*exp(constants[119]*states[6])
    algebraic[59] = (algebraic[20]+algebraic[29])*states[47]
    rates[47] = algebraic[50]-algebraic[59]
    algebraic[22] = power(states[2]/constants[18], constants[19])
    algebraic[33] = power(states[5]/constants[20], constants[21])
    algebraic[42] = custom_piecewise([equal(constants[0] , 0.00000), (constants[22]*(constants[23]*algebraic[22]-constants[24]*algebraic[33]))/(1.00000+algebraic[22]+algebraic[33]) , True, (1.50000*constants[22]*(constants[23]*algebraic[22]-constants[24]*algebraic[33]))/(1.00000+algebraic[22]+algebraic[33])])
    algebraic[61] = (states[5]-states[4])/constants[26]
    rates[5] = (algebraic[42]*constants[7])/constants[9]-(algebraic[61]*constants[8])/constants[9]
    algebraic[62] = -(algebraic[34]+algebraic[43]+algebraic[52])
    rates[7] = algebraic[62]
    algebraic[51] = constants[25]*(states[7]+states[8])*(states[4]-states[3])
    algebraic[71] = 1.00000/(1.00000+(constants[125]*constants[37])/(power(states[4]+constants[37], 2.00000)))
    rates[4] = algebraic[71]*(algebraic[61]-algebraic[51])
    algebraic[70] = constants[32]*states[2]*(1.00000-states[9])-constants[33]*states[9]
    rates[9] = algebraic[70]
    algebraic[49] = constants[109]*constants[122]*exp(constants[123]*states[6])
    algebraic[58] = (algebraic[20]*algebraic[40]*algebraic[49])/(algebraic[9]*algebraic[29])
    algebraic[68] = constants[139]*states[62]+algebraic[20]*states[47]+algebraic[58]*states[64]
    algebraic[79] = (algebraic[49]+algebraic[9]+constants[140])*states[63]
    rates[63] = algebraic[68]-algebraic[79]
    algebraic[69] = algebraic[49]*states[63]+algebraic[29]*states[47]
    algebraic[80] = (algebraic[58]+algebraic[40])*states[64]
    rates[64] = algebraic[69]-algebraic[80]
    algebraic[81] = constants[30]*states[2]*(1.00000-states[10])-constants[31]*states[10]
    rates[10] = algebraic[81]
    algebraic[5] = constants[82]*exp(constants[83]*states[6])
    algebraic[26] = 4.00000*algebraic[5]
    algebraic[76] = (algebraic[26]+constants[144])*states[35]
    algebraic[16] = constants[84]*exp(-constants[85]*states[6])
    algebraic[65] = algebraic[16]
    algebraic[86] = algebraic[65]*states[36]+constants[149]*states[40]
    rates[35] = algebraic[86]-algebraic[76]
    algebraic[27] = 4.00000*constants[78]*algebraic[5]
    algebraic[77] = (constants[149]+algebraic[27])*states[40]
    algebraic[66] = algebraic[16]/constants[74]
    algebraic[88] = constants[144]*states[35]+algebraic[66]*states[41]
    rates[40] = algebraic[88]-algebraic[77]
    algebraic[37] = 3.00000*algebraic[5]
    algebraic[87] = (algebraic[37]+algebraic[65]+constants[145])*states[36]
    algebraic[74] = 2.00000*algebraic[16]
    algebraic[96] = algebraic[74]*states[37]+constants[150]*states[41]+algebraic[26]*states[35]
    rates[36] = algebraic[96]-algebraic[87]
    algebraic[38] = (3.00000*constants[79]*algebraic[5])/constants[78]
    algebraic[89] = (algebraic[38]+constants[150]+algebraic[66])*states[41]
    algebraic[75] = (2.00000*constants[74]*algebraic[16])/constants[75]
    algebraic[98] = algebraic[75]*states[42]+constants[145]*states[36]+algebraic[27]*states[40]
    rates[41] = algebraic[98]-algebraic[89]
    algebraic[46] = 2.00000*algebraic[5]
    algebraic[97] = (algebraic[46]+algebraic[74]+constants[146])*states[37]
    algebraic[84] = 3.00000*algebraic[16]
    algebraic[104] = algebraic[84]*states[38]+constants[151]*states[42]+algebraic[37]*states[36]
    rates[37] = algebraic[104]-algebraic[97]
    algebraic[47] = (2.00000*constants[80]*algebraic[5])/constants[79]
    algebraic[99] = (algebraic[47]+constants[151]+algebraic[75])*states[42]
    algebraic[85] = (3.00000*constants[75]*algebraic[16])/constants[76]
    algebraic[107] = algebraic[85]*states[43]+constants[146]*states[37]+algebraic[38]*states[41]
    rates[42] = algebraic[107]-algebraic[99]
    algebraic[55] = algebraic[5]
    algebraic[105] = (algebraic[55]+algebraic[84]+constants[147])*states[38]
    algebraic[94] = 4.00000*algebraic[16]
    algebraic[114] = algebraic[94]*states[39]+constants[152]*states[43]+algebraic[46]*states[37]
    rates[38] = algebraic[114]-algebraic[105]
    algebraic[106] = (algebraic[94]+constants[148])*states[39]
    algebraic[115] = algebraic[55]*states[38]+constants[153]*states[44]
    rates[39] = algebraic[115]-algebraic[106]
    algebraic[56] = (constants[81]*algebraic[5])/constants[80]
    algebraic[108] = (algebraic[56]+constants[152]+algebraic[85])*states[43]
    algebraic[95] = (4.00000*constants[76]*algebraic[16])/constants[77]
    algebraic[116] = algebraic[95]*states[44]+constants[147]*states[38]+algebraic[47]*states[42]
    rates[43] = algebraic[116]-algebraic[108]
    algebraic[109] = (constants[153]+algebraic[95])*states[44]
    algebraic[117] = constants[148]*states[39]+algebraic[56]*states[43]
    rates[44] = algebraic[117]-algebraic[109]
    algebraic[4] = constants[58]*exp(constants[59]*states[6])
    algebraic[45] = 4.00000*algebraic[4]
    algebraic[36] = constants[64]*exp(constants[65]*states[6])
    algebraic[141] = algebraic[36]
    algebraic[155] = (algebraic[45]+algebraic[141])*states[25]
    algebraic[15] = constants[60]*exp(-constants[61]*states[6])
    algebraic[121] = algebraic[15]
    algebraic[25] = constants[62]*exp(-constants[63]*states[6])
    algebraic[148] = algebraic[25]
    algebraic[163] = algebraic[121]*states[26]+algebraic[148]*states[30]
    rates[25] = algebraic[163]-algebraic[155]
    algebraic[83] = 4.00000*constants[70]*algebraic[4]
    algebraic[156] = (algebraic[148]+algebraic[83])*states[30]
    algebraic[137] = algebraic[15]/constants[66]
    algebraic[165] = algebraic[141]*states[25]+algebraic[137]*states[31]
    rates[30] = algebraic[165]-algebraic[156]
    algebraic[54] = 3.00000*algebraic[4]
    algebraic[146] = constants[66]*algebraic[36]
    algebraic[164] = (algebraic[54]+algebraic[121]+algebraic[146])*states[26]
    algebraic[125] = 2.00000*algebraic[15]
    algebraic[154] = algebraic[25]/constants[70]
    algebraic[172] = algebraic[125]*states[27]+algebraic[154]*states[31]+algebraic[45]*states[25]
    rates[26] = algebraic[172]-algebraic[164]
    algebraic[93] = (3.00000*constants[71]*algebraic[4])/constants[70]
    algebraic[166] = (algebraic[93]+algebraic[154]+algebraic[137])*states[31]
    algebraic[142] = (2.00000*constants[66]*algebraic[15])/constants[67]
    algebraic[174] = algebraic[142]*states[32]+algebraic[146]*states[26]+algebraic[83]*states[30]
    rates[31] = algebraic[174]-algebraic[166]
    algebraic[7] = constants[161]*constants[137]*exp(-114007./constants[157]+224.114/constants[5]+(0.286374*states[6])/constants[138])
    algebraic[110] = 4.00000*algebraic[7]
    algebraic[18] = constants[161]*constants[137]*exp(-272470./constants[157]+708.146/constants[5]+(-2.28528*states[6])/constants[138])
    algebraic[176] = algebraic[18]
    rates[50] = -(constants[177]+algebraic[110])*states[50]+algebraic[176]*states[51]+constants[176]*states[55]
    algebraic[64] = 2.00000*algebraic[4]
    algebraic[152] = constants[67]*algebraic[36]
    algebraic[173] = (algebraic[64]+algebraic[125]+algebraic[152])*states[27]
    algebraic[129] = 3.00000*algebraic[15]
    algebraic[162] = algebraic[25]/constants[71]
    algebraic[181] = algebraic[129]*states[28]+algebraic[162]*states[32]+algebraic[54]*states[26]
    rates[27] = algebraic[181]-algebraic[173]
    algebraic[103] = (2.00000*constants[72]*algebraic[4])/constants[71]
    algebraic[175] = (algebraic[103]+algebraic[162]+algebraic[142])*states[32]
    algebraic[147] = (3.00000*constants[67]*algebraic[15])/constants[68]
    algebraic[184] = algebraic[147]*states[33]+algebraic[152]*states[27]+algebraic[93]*states[31]
    rates[32] = algebraic[184]-algebraic[175]
    algebraic[118] = 3.00000*algebraic[7]
    algebraic[187] = 2.00000*algebraic[18]
    rates[51] = (algebraic[110]*states[50]-(algebraic[176]+algebraic[118]+constants[179])*states[51])+algebraic[187]*states[52]+constants[178]*states[56]
    algebraic[2] = 4.00000*1.20000*0.416000*exp(0.0120000*(states[6]-35.0000))
    algebraic[53] = 4.00000*algebraic[2]
    algebraic[44] = 0.600000*0.0923300*states[3]
    algebraic[169] = algebraic[44]
    algebraic[180] = (algebraic[53]+algebraic[169])*states[13]
    algebraic[13] = 4.00000*0.450000*0.0490000*exp(-0.0650000*(states[6]-22.0000))
    algebraic[124] = algebraic[13]
    algebraic[192] = algebraic[124]*states[14]+constants[143]*states[18]
    rates[13] = algebraic[192]-algebraic[180]
    algebraic[24] = constants[57]*algebraic[2]
    algebraic[92] = 4.00000*algebraic[24]
    algebraic[179] = (algebraic[92]+constants[143])*states[18]
    algebraic[35] = algebraic[13]/constants[56]
    algebraic[140] = algebraic[35]
    algebraic[190] = algebraic[140]*states[19]+algebraic[169]*states[13]
    rates[18] = algebraic[190]-algebraic[179]
    algebraic[73] = algebraic[4]
    algebraic[160] = constants[68]*algebraic[36]
    algebraic[182] = (algebraic[73]+algebraic[129]+algebraic[160])*states[28]
    algebraic[133] = 4.00000*algebraic[15]
    algebraic[170] = algebraic[25]/constants[72]
    algebraic[194] = algebraic[133]*states[29]+algebraic[170]*states[33]+algebraic[64]*states[27]
    rates[28] = algebraic[194]-algebraic[182]
    algebraic[161] = constants[69]*algebraic[36]
    algebraic[183] = (algebraic[133]+algebraic[161])*states[29]
    algebraic[171] = algebraic[25]/constants[73]
    algebraic[195] = algebraic[73]*states[28]+algebraic[171]*states[34]
    rates[29] = algebraic[195]-algebraic[183]
    algebraic[113] = (constants[73]*algebraic[4])/constants[72]
    algebraic[185] = (algebraic[113]+algebraic[170]+algebraic[147])*states[33]
    algebraic[153] = (4.00000*constants[68]*algebraic[15])/constants[69]
    algebraic[196] = algebraic[153]*states[34]+algebraic[160]*states[28]+algebraic[103]*states[32]
    rates[33] = algebraic[196]-algebraic[185]
    algebraic[186] = (algebraic[171]+algebraic[153])*states[34]
    algebraic[197] = algebraic[161]*states[29]+algebraic[113]*states[33]
    rates[34] = algebraic[197]-algebraic[186]
    algebraic[122] = 2.00000*algebraic[7]
    algebraic[198] = 3.00000*algebraic[18]
    rates[52] = (algebraic[118]*states[51]-(algebraic[187]+algebraic[122]+constants[181])*states[52])+algebraic[198]*states[53]+constants[180]*states[57]
    algebraic[63] = 3.00000*algebraic[2]
    algebraic[178] = constants[57]*algebraic[169]
    algebraic[193] = (algebraic[124]+algebraic[63]+algebraic[178])*states[14]
    algebraic[128] = 2.00000*algebraic[13]
    algebraic[203] = algebraic[53]*states[13]+algebraic[128]*states[15]+constants[159]*states[19]
    rates[14] = algebraic[203]-algebraic[193]
    algebraic[102] = 3.00000*algebraic[24]
    algebraic[191] = (algebraic[140]+algebraic[102]+constants[159])*states[19]
    algebraic[145] = 2.00000*algebraic[35]
    algebraic[201] = algebraic[92]*states[18]+algebraic[145]*states[20]+algebraic[178]*states[14]
    rates[19] = algebraic[201]-algebraic[191]
    algebraic[126] = algebraic[7]
    algebraic[205] = 4.00000*algebraic[18]
    rates[53] = (algebraic[122]*states[52]-(algebraic[198]+algebraic[126]+constants[183])*states[53])+algebraic[205]*states[54]+constants[182]*states[58]
    algebraic[72] = 2.00000*algebraic[2]
    algebraic[189] = constants[57]*algebraic[178]
    algebraic[204] = (algebraic[128]+algebraic[72]+algebraic[189])*states[15]
    algebraic[132] = 3.00000*algebraic[13]
    algebraic[210] = algebraic[63]*states[14]+algebraic[132]*states[16]+constants[162]*states[20]
    rates[15] = algebraic[210]-algebraic[204]
    algebraic[112] = 2.00000*algebraic[24]
    algebraic[202] = (algebraic[145]+algebraic[112]+constants[162])*states[20]
    algebraic[151] = 3.00000*algebraic[35]
    algebraic[208] = algebraic[102]*states[19]+algebraic[151]*states[21]+algebraic[189]*states[15]
    rates[20] = algebraic[208]-algebraic[202]
    algebraic[82] = algebraic[2]
    algebraic[200] = constants[57]*algebraic[189]
    algebraic[211] = (algebraic[132]+algebraic[82]+algebraic[200])*states[16]
    algebraic[136] = 4.00000*algebraic[13]
    algebraic[216] = algebraic[72]*states[15]+algebraic[136]*states[17]+constants[168]*states[21]
    rates[16] = algebraic[216]-algebraic[211]
    algebraic[120] = algebraic[24]
    algebraic[209] = (algebraic[151]+algebraic[120]+constants[168])*states[21]
    algebraic[159] = 4.00000*algebraic[35]
    algebraic[214] = algebraic[112]*states[20]+algebraic[159]*states[22]+algebraic[200]*states[16]
    rates[21] = algebraic[214]-algebraic[209]
    algebraic[28] = constants[161]*constants[137]*exp(-196337./constants[157]+529.952/constants[5]+(2.78085*states[6])/constants[138])
    algebraic[130] = algebraic[28]
    algebraic[90] = constants[161]*constants[137]*exp(-147814./constants[157]+338.915/constants[5]+(2.13600*states[6])/constants[138])
    algebraic[167] = algebraic[90]
    algebraic[39] = constants[161]*constants[137]*exp(-133690./constants[157]+229.205/constants[5]+(-1.55804*states[6])/constants[138])
    algebraic[212] = algebraic[39]
    algebraic[100] = constants[161]*constants[137]*exp(-121322./constants[157]+193.265/constants[5]+(-1.74290*states[6])/constants[138])
    algebraic[219] = algebraic[100]
    rates[54] = (algebraic[126]*states[53]-(algebraic[205]+algebraic[130]+algebraic[167]+constants[185])*states[54])+algebraic[212]*states[45]+algebraic[219]*states[46]+constants[184]*states[59]
    rates[46] = (algebraic[167]*states[54]+constants[170]*states[45])-(algebraic[219]+constants[171])*states[46]
    algebraic[134] = algebraic[110]*constants[174]
    algebraic[218] = algebraic[176]/constants[174]
    rates[55] = (constants[177]*states[50]-(constants[176]+algebraic[134])*states[55])+algebraic[218]*states[56]
    algebraic[207] = constants[57]*algebraic[200]
    algebraic[217] = (algebraic[136]+constants[54]+algebraic[207])*states[17]
    algebraic[222] = algebraic[82]*states[16]+constants[55]*states[23]+constants[173]*states[22]
    rates[17] = algebraic[222]-algebraic[217]
    algebraic[215] = (algebraic[159]+constants[173])*states[22]
    algebraic[221] = algebraic[120]*states[21]+algebraic[207]*states[17]
    rates[22] = algebraic[221]-algebraic[215]
    algebraic[138] = algebraic[118]*constants[174]
    algebraic[223] = algebraic[187]/constants[174]
    rates[56] = ((constants[179]*states[51]+algebraic[134]*states[55])-(algebraic[218]+constants[178]+algebraic[138])*states[56])+algebraic[223]*states[57]
    algebraic[143] = algebraic[122]*constants[174]
    algebraic[225] = algebraic[198]/constants[174]
    rates[57] = ((constants[181]*states[52]+algebraic[138]*states[56])-(algebraic[143]+constants[180]+algebraic[223])*states[57])+algebraic[225]*states[58]
    algebraic[149] = algebraic[126]*constants[174]
    algebraic[227] = algebraic[205]/constants[174]
    rates[58] = ((constants[183]*states[53]+algebraic[143]*states[57])-(algebraic[225]+constants[182]+algebraic[149])*states[58])+algebraic[227]*states[59]
    algebraic[67] = constants[161]*constants[137]*exp(116431./constants[157]+-578.317/constants[5]+(0.764126*states[6])/constants[138])
    algebraic[157] = algebraic[67]
    algebraic[78] = constants[161]*constants[137]*exp(-55700.7/constants[157]+-130.639/constants[5]+(-3.64982*states[6])/constants[138])
    algebraic[229] = algebraic[78]
    rates[59] = ((constants[185]*states[54]+algebraic[149]*states[58])-(algebraic[227]+constants[184]+algebraic[157])*states[59])+algebraic[229]*states[60]
    algebraic[57] = constants[161]*constants[137]*exp(-97657.8/constants[157]+1.51000/constants[5]+(0.0684862*states[6])/constants[138])
    algebraic[231] = algebraic[57]
    algebraic[48] = constants[161]*constants[137]*exp(-62123.1/constants[157]+39.2950/constants[5]+(0.288816*states[6])/constants[138])
    algebraic[233] = algebraic[48]
    rates[45] = (algebraic[130]*states[54]-(algebraic[212]+constants[170]+algebraic[233])*states[45])+constants[171]*states[46]+algebraic[231]*states[60]
    rates[60] = (algebraic[233]*states[45]+algebraic[157]*states[59])-(algebraic[229]+algebraic[231])*states[60]
    algebraic[119] = constants[124]*log(constants[12]/states[0])
    algebraic[131] = constants[91]*(states[45]+states[46])*(states[6]-algebraic[119])
    algebraic[228] = constants[92]*(states[6]-algebraic[119])
    algebraic[234] = states[6]/constants[124]
    algebraic[240] = exp(constants[99]*algebraic[234])*(power(states[0], 3.00000))*constants[13]
    algebraic[241] = exp((constants[99]-1.00000)*algebraic[234])*(power(constants[12], 3.00000))*states[2]
    algebraic[242] = 1.00000+constants[98]*exp((constants[99]-1.00000)*algebraic[234])
    algebraic[243] = (constants[95]*(algebraic[240]-algebraic[241]))/(constants[172]*algebraic[242]*constants[175])
    algebraic[235] = 1.00000+0.124500*exp(-0.100000*algebraic[234])
    algebraic[236] = 0.0365000*constants[163]*exp(-1.33000*algebraic[234])
    algebraic[237] = 1.00000/(algebraic[235]+algebraic[236])
    algebraic[238] = 1.00000+power(constants[101]/states[0], 1.50000)
    algebraic[239] = (constants[100]*algebraic[237]*constants[167])/algebraic[238]
    algebraic[150] = states[6]/constants[124]
    algebraic[158] = 1000.00*constants[3]*algebraic[150]
    algebraic[177] = exp(algebraic[150])-1.00000
    algebraic[199] = states[0]*exp(algebraic[150])-constants[12]
    algebraic[206] = (0.0200000*constants[133]*states[39]*algebraic[158]*algebraic[199])/algebraic[177]
    rates[0] = -(algebraic[131]+algebraic[228]+3.00000*(algebraic[243]+algebraic[239])+algebraic[206])*constants[155]
    algebraic[127] = 0.500000*constants[124]*log(constants[13]/states[2])
    algebraic[230] = constants[105]*(states[6]-algebraic[127])
    algebraic[232] = (constants[103]*states[2])/(constants[104]+states[2])
    algebraic[60] = (states[3]-states[2])/constants[27]
    algebraic[91] = constants[28]*algebraic[70]+constants[29]*algebraic[81]
    algebraic[111] = 1.00000/(1.00000+(constants[34]*constants[36])/(power(states[2]+constants[36], 2.00000))+(constants[35]*constants[38])/(power(states[2]+constants[38], 2.00000)))
    rates[2] = algebraic[111]*(((algebraic[60]-algebraic[42])-algebraic[91])-((algebraic[230]-2.00000*algebraic[243])+algebraic[232])*0.500000*constants[155])
    algebraic[244] = states[6]/constants[124]
    algebraic[245] = 1000.00*constants[3]*algebraic[244]
    algebraic[246] = 0.00100000*exp(2.00000*algebraic[244])-constants[13]*0.341000
    algebraic[247] = exp(2.00000*algebraic[244])-1.00000
    algebraic[248] = (constants[156]*4.00000*algebraic[245]*algebraic[246])/algebraic[247]
    algebraic[249] = algebraic[248]*states[24]*states[23]
    algebraic[101] = 1.00000/(1.00000+(constants[34]*constants[36])/(power(states[3]+constants[36], 2.00000))+(constants[35]*constants[38])/(power(states[3]+constants[38], 2.00000)))
    rates[3] = algebraic[101]*(((algebraic[51]*constants[8])/constants[10]-(algebraic[60]*constants[7])/constants[10])-algebraic[249]*constants[160])
    algebraic[123] = constants[124]*log(constants[11]/states[1])
    algebraic[135] = constants[88]*constants[134]*states[47]*(states[6]-algebraic[123])
    algebraic[139] = constants[89]*(states[48]+states[49])*(states[6]-algebraic[123])
    algebraic[224] = 1.00000/(0.940000+exp((1.26000/constants[124])*(states[6]-algebraic[123])))
    algebraic[226] = constants[90]*(power(constants[11]/1.00000, 1.0/2))*algebraic[224]*(states[6]-algebraic[123])
    algebraic[250] = custom_piecewise([greater_equal(algebraic[248] , 0.00000), 0.00000 , True, algebraic[248]])
    algebraic[251] = constants[136]/(1.00000+algebraic[250]/constants[106])
    algebraic[252] = states[1]*exp(algebraic[244])-constants[11]
    algebraic[253] = exp(algebraic[244])-1.00000
    algebraic[254] = (algebraic[251]*states[23]*states[24]*algebraic[245]*algebraic[252])/algebraic[253]
    algebraic[0] = floor(voi/constants[14])*constants[14]
    algebraic[11] = custom_piecewise([greater_equal(voi-algebraic[0] , constants[17]) & less_equal(voi-algebraic[0] , constants[17]+constants[15]), constants[16] , True, 0.00000])
    algebraic[144] = constants[132]*states[29]*(states[6]-algebraic[123])
    algebraic[168] = states[1]*exp(algebraic[150])-constants[11]
    algebraic[188] = (constants[133]*states[39]*algebraic[158]*algebraic[168])/algebraic[177]
    rates[1] = -(((algebraic[135]+algebraic[139]+algebraic[226]+algebraic[254]+algebraic[11])-2.00000*algebraic[239])+algebraic[144]+algebraic[188])*constants[155]
    algebraic[213] = algebraic[188]+algebraic[206]
    algebraic[220] = algebraic[144]+algebraic[213]
    algebraic[255] = algebraic[131]+algebraic[249]+algebraic[254]+algebraic[135]+algebraic[139]+algebraic[226]+algebraic[243]+algebraic[239]+algebraic[220]+algebraic[232]+algebraic[230]+algebraic[228]+algebraic[11]
    rates[6] = -algebraic[255]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[3] = (constants[129]/(1.00000+exp((states[6]+28.5000)/7.80000))+1.00000)-constants[129]
    algebraic[14] = 1.00000/(0.00336336/(0.500000+exp(states[6]/-5.53900))+0.00779047*exp(states[6]/-49.5104))
    algebraic[8] = constants[109]*constants[110]*exp(constants[111]*states[6])
    algebraic[19] = constants[109]*constants[112]*exp(constants[113]*states[6])
    algebraic[32] = 0.216256*exp(-1.88912e-05*states[6])
    algebraic[21] = 0.00700807*exp(-0.149998*states[6])
    algebraic[10] = 0.00767254*exp(0.0866295*states[6])
    algebraic[31] = 0.00379738*exp(-0.0142567*states[6])
    algebraic[1] = constants[48]-(constants[48]-constants[50])/(1.00000+power(constants[51]/states[4], constants[53]))
    algebraic[34] = -constants[39]*algebraic[1]*(power(states[3]*1000.00, constants[45]*constants[47]))*states[11]+constants[40]*states[7]
    algebraic[30] = algebraic[8]*states[61]+constants[140]*states[63]
    algebraic[41] = (algebraic[19]+constants[139])*states[62]
    algebraic[43] = constants[41]*(power(states[3]*1000.00, constants[46]*constants[47]))*states[7]-constants[42]*states[8]
    algebraic[12] = constants[126]-(constants[126]-constants[50])/(1.00000+power(constants[52]/states[4], constants[53]))
    algebraic[23] = constants[49]-(constants[49]-constants[50])/(1.00000+power(constants[127]/states[4], constants[53]))
    algebraic[52] = (constants[43]/algebraic[12])*states[7]-constants[44]*algebraic[23]*states[12]
    algebraic[9] = constants[109]*constants[114]*exp(constants[115]*states[6])
    algebraic[40] = constants[109]*constants[120]*exp(constants[121]*states[6])
    algebraic[50] = algebraic[9]*states[63]+algebraic[40]*states[64]
    algebraic[20] = constants[109]*constants[116]*exp(constants[117]*states[6])
    algebraic[29] = constants[109]*constants[118]*exp(constants[119]*states[6])
    algebraic[59] = (algebraic[20]+algebraic[29])*states[47]
    algebraic[22] = power(states[2]/constants[18], constants[19])
    algebraic[33] = power(states[5]/constants[20], constants[21])
    algebraic[42] = custom_piecewise([equal(constants[0] , 0.00000), (constants[22]*(constants[23]*algebraic[22]-constants[24]*algebraic[33]))/(1.00000+algebraic[22]+algebraic[33]) , True, (1.50000*constants[22]*(constants[23]*algebraic[22]-constants[24]*algebraic[33]))/(1.00000+algebraic[22]+algebraic[33])])
    algebraic[61] = (states[5]-states[4])/constants[26]
    algebraic[62] = -(algebraic[34]+algebraic[43]+algebraic[52])
    algebraic[51] = constants[25]*(states[7]+states[8])*(states[4]-states[3])
    algebraic[71] = 1.00000/(1.00000+(constants[125]*constants[37])/(power(states[4]+constants[37], 2.00000)))
    algebraic[70] = constants[32]*states[2]*(1.00000-states[9])-constants[33]*states[9]
    algebraic[49] = constants[109]*constants[122]*exp(constants[123]*states[6])
    algebraic[58] = (algebraic[20]*algebraic[40]*algebraic[49])/(algebraic[9]*algebraic[29])
    algebraic[68] = constants[139]*states[62]+algebraic[20]*states[47]+algebraic[58]*states[64]
    algebraic[79] = (algebraic[49]+algebraic[9]+constants[140])*states[63]
    algebraic[69] = algebraic[49]*states[63]+algebraic[29]*states[47]
    algebraic[80] = (algebraic[58]+algebraic[40])*states[64]
    algebraic[81] = constants[30]*states[2]*(1.00000-states[10])-constants[31]*states[10]
    algebraic[5] = constants[82]*exp(constants[83]*states[6])
    algebraic[26] = 4.00000*algebraic[5]
    algebraic[76] = (algebraic[26]+constants[144])*states[35]
    algebraic[16] = constants[84]*exp(-constants[85]*states[6])
    algebraic[65] = algebraic[16]
    algebraic[86] = algebraic[65]*states[36]+constants[149]*states[40]
    algebraic[27] = 4.00000*constants[78]*algebraic[5]
    algebraic[77] = (constants[149]+algebraic[27])*states[40]
    algebraic[66] = algebraic[16]/constants[74]
    algebraic[88] = constants[144]*states[35]+algebraic[66]*states[41]
    algebraic[37] = 3.00000*algebraic[5]
    algebraic[87] = (algebraic[37]+algebraic[65]+constants[145])*states[36]
    algebraic[74] = 2.00000*algebraic[16]
    algebraic[96] = algebraic[74]*states[37]+constants[150]*states[41]+algebraic[26]*states[35]
    algebraic[38] = (3.00000*constants[79]*algebraic[5])/constants[78]
    algebraic[89] = (algebraic[38]+constants[150]+algebraic[66])*states[41]
    algebraic[75] = (2.00000*constants[74]*algebraic[16])/constants[75]
    algebraic[98] = algebraic[75]*states[42]+constants[145]*states[36]+algebraic[27]*states[40]
    algebraic[46] = 2.00000*algebraic[5]
    algebraic[97] = (algebraic[46]+algebraic[74]+constants[146])*states[37]
    algebraic[84] = 3.00000*algebraic[16]
    algebraic[104] = algebraic[84]*states[38]+constants[151]*states[42]+algebraic[37]*states[36]
    algebraic[47] = (2.00000*constants[80]*algebraic[5])/constants[79]
    algebraic[99] = (algebraic[47]+constants[151]+algebraic[75])*states[42]
    algebraic[85] = (3.00000*constants[75]*algebraic[16])/constants[76]
    algebraic[107] = algebraic[85]*states[43]+constants[146]*states[37]+algebraic[38]*states[41]
    algebraic[55] = algebraic[5]
    algebraic[105] = (algebraic[55]+algebraic[84]+constants[147])*states[38]
    algebraic[94] = 4.00000*algebraic[16]
    algebraic[114] = algebraic[94]*states[39]+constants[152]*states[43]+algebraic[46]*states[37]
    algebraic[106] = (algebraic[94]+constants[148])*states[39]
    algebraic[115] = algebraic[55]*states[38]+constants[153]*states[44]
    algebraic[56] = (constants[81]*algebraic[5])/constants[80]
    algebraic[108] = (algebraic[56]+constants[152]+algebraic[85])*states[43]
    algebraic[95] = (4.00000*constants[76]*algebraic[16])/constants[77]
    algebraic[116] = algebraic[95]*states[44]+constants[147]*states[38]+algebraic[47]*states[42]
    algebraic[109] = (constants[153]+algebraic[95])*states[44]
    algebraic[117] = constants[148]*states[39]+algebraic[56]*states[43]
    algebraic[4] = constants[58]*exp(constants[59]*states[6])
    algebraic[45] = 4.00000*algebraic[4]
    algebraic[36] = constants[64]*exp(constants[65]*states[6])
    algebraic[141] = algebraic[36]
    algebraic[155] = (algebraic[45]+algebraic[141])*states[25]
    algebraic[15] = constants[60]*exp(-constants[61]*states[6])
    algebraic[121] = algebraic[15]
    algebraic[25] = constants[62]*exp(-constants[63]*states[6])
    algebraic[148] = algebraic[25]
    algebraic[163] = algebraic[121]*states[26]+algebraic[148]*states[30]
    algebraic[83] = 4.00000*constants[70]*algebraic[4]
    algebraic[156] = (algebraic[148]+algebraic[83])*states[30]
    algebraic[137] = algebraic[15]/constants[66]
    algebraic[165] = algebraic[141]*states[25]+algebraic[137]*states[31]
    algebraic[54] = 3.00000*algebraic[4]
    algebraic[146] = constants[66]*algebraic[36]
    algebraic[164] = (algebraic[54]+algebraic[121]+algebraic[146])*states[26]
    algebraic[125] = 2.00000*algebraic[15]
    algebraic[154] = algebraic[25]/constants[70]
    algebraic[172] = algebraic[125]*states[27]+algebraic[154]*states[31]+algebraic[45]*states[25]
    algebraic[93] = (3.00000*constants[71]*algebraic[4])/constants[70]
    algebraic[166] = (algebraic[93]+algebraic[154]+algebraic[137])*states[31]
    algebraic[142] = (2.00000*constants[66]*algebraic[15])/constants[67]
    algebraic[174] = algebraic[142]*states[32]+algebraic[146]*states[26]+algebraic[83]*states[30]
    algebraic[7] = constants[161]*constants[137]*exp(-114007./constants[157]+224.114/constants[5]+(0.286374*states[6])/constants[138])
    algebraic[110] = 4.00000*algebraic[7]
    algebraic[18] = constants[161]*constants[137]*exp(-272470./constants[157]+708.146/constants[5]+(-2.28528*states[6])/constants[138])
    algebraic[176] = algebraic[18]
    algebraic[64] = 2.00000*algebraic[4]
    algebraic[152] = constants[67]*algebraic[36]
    algebraic[173] = (algebraic[64]+algebraic[125]+algebraic[152])*states[27]
    algebraic[129] = 3.00000*algebraic[15]
    algebraic[162] = algebraic[25]/constants[71]
    algebraic[181] = algebraic[129]*states[28]+algebraic[162]*states[32]+algebraic[54]*states[26]
    algebraic[103] = (2.00000*constants[72]*algebraic[4])/constants[71]
    algebraic[175] = (algebraic[103]+algebraic[162]+algebraic[142])*states[32]
    algebraic[147] = (3.00000*constants[67]*algebraic[15])/constants[68]
    algebraic[184] = algebraic[147]*states[33]+algebraic[152]*states[27]+algebraic[93]*states[31]
    algebraic[118] = 3.00000*algebraic[7]
    algebraic[187] = 2.00000*algebraic[18]
    algebraic[2] = 4.00000*1.20000*0.416000*exp(0.0120000*(states[6]-35.0000))
    algebraic[53] = 4.00000*algebraic[2]
    algebraic[44] = 0.600000*0.0923300*states[3]
    algebraic[169] = algebraic[44]
    algebraic[180] = (algebraic[53]+algebraic[169])*states[13]
    algebraic[13] = 4.00000*0.450000*0.0490000*exp(-0.0650000*(states[6]-22.0000))
    algebraic[124] = algebraic[13]
    algebraic[192] = algebraic[124]*states[14]+constants[143]*states[18]
    algebraic[24] = constants[57]*algebraic[2]
    algebraic[92] = 4.00000*algebraic[24]
    algebraic[179] = (algebraic[92]+constants[143])*states[18]
    algebraic[35] = algebraic[13]/constants[56]
    algebraic[140] = algebraic[35]
    algebraic[190] = algebraic[140]*states[19]+algebraic[169]*states[13]
    algebraic[73] = algebraic[4]
    algebraic[160] = constants[68]*algebraic[36]
    algebraic[182] = (algebraic[73]+algebraic[129]+algebraic[160])*states[28]
    algebraic[133] = 4.00000*algebraic[15]
    algebraic[170] = algebraic[25]/constants[72]
    algebraic[194] = algebraic[133]*states[29]+algebraic[170]*states[33]+algebraic[64]*states[27]
    algebraic[161] = constants[69]*algebraic[36]
    algebraic[183] = (algebraic[133]+algebraic[161])*states[29]
    algebraic[171] = algebraic[25]/constants[73]
    algebraic[195] = algebraic[73]*states[28]+algebraic[171]*states[34]
    algebraic[113] = (constants[73]*algebraic[4])/constants[72]
    algebraic[185] = (algebraic[113]+algebraic[170]+algebraic[147])*states[33]
    algebraic[153] = (4.00000*constants[68]*algebraic[15])/constants[69]
    algebraic[196] = algebraic[153]*states[34]+algebraic[160]*states[28]+algebraic[103]*states[32]
    algebraic[186] = (algebraic[171]+algebraic[153])*states[34]
    algebraic[197] = algebraic[161]*states[29]+algebraic[113]*states[33]
    algebraic[122] = 2.00000*algebraic[7]
    algebraic[198] = 3.00000*algebraic[18]
    algebraic[63] = 3.00000*algebraic[2]
    algebraic[178] = constants[57]*algebraic[169]
    algebraic[193] = (algebraic[124]+algebraic[63]+algebraic[178])*states[14]
    algebraic[128] = 2.00000*algebraic[13]
    algebraic[203] = algebraic[53]*states[13]+algebraic[128]*states[15]+constants[159]*states[19]
    algebraic[102] = 3.00000*algebraic[24]
    algebraic[191] = (algebraic[140]+algebraic[102]+constants[159])*states[19]
    algebraic[145] = 2.00000*algebraic[35]
    algebraic[201] = algebraic[92]*states[18]+algebraic[145]*states[20]+algebraic[178]*states[14]
    algebraic[126] = algebraic[7]
    algebraic[205] = 4.00000*algebraic[18]
    algebraic[72] = 2.00000*algebraic[2]
    algebraic[189] = constants[57]*algebraic[178]
    algebraic[204] = (algebraic[128]+algebraic[72]+algebraic[189])*states[15]
    algebraic[132] = 3.00000*algebraic[13]
    algebraic[210] = algebraic[63]*states[14]+algebraic[132]*states[16]+constants[162]*states[20]
    algebraic[112] = 2.00000*algebraic[24]
    algebraic[202] = (algebraic[145]+algebraic[112]+constants[162])*states[20]
    algebraic[151] = 3.00000*algebraic[35]
    algebraic[208] = algebraic[102]*states[19]+algebraic[151]*states[21]+algebraic[189]*states[15]
    algebraic[82] = algebraic[2]
    algebraic[200] = constants[57]*algebraic[189]
    algebraic[211] = (algebraic[132]+algebraic[82]+algebraic[200])*states[16]
    algebraic[136] = 4.00000*algebraic[13]
    algebraic[216] = algebraic[72]*states[15]+algebraic[136]*states[17]+constants[168]*states[21]
    algebraic[120] = algebraic[24]
    algebraic[209] = (algebraic[151]+algebraic[120]+constants[168])*states[21]
    algebraic[159] = 4.00000*algebraic[35]
    algebraic[214] = algebraic[112]*states[20]+algebraic[159]*states[22]+algebraic[200]*states[16]
    algebraic[28] = constants[161]*constants[137]*exp(-196337./constants[157]+529.952/constants[5]+(2.78085*states[6])/constants[138])
    algebraic[130] = algebraic[28]
    algebraic[90] = constants[161]*constants[137]*exp(-147814./constants[157]+338.915/constants[5]+(2.13600*states[6])/constants[138])
    algebraic[167] = algebraic[90]
    algebraic[39] = constants[161]*constants[137]*exp(-133690./constants[157]+229.205/constants[5]+(-1.55804*states[6])/constants[138])
    algebraic[212] = algebraic[39]
    algebraic[100] = constants[161]*constants[137]*exp(-121322./constants[157]+193.265/constants[5]+(-1.74290*states[6])/constants[138])
    algebraic[219] = algebraic[100]
    algebraic[134] = algebraic[110]*constants[174]
    algebraic[218] = algebraic[176]/constants[174]
    algebraic[207] = constants[57]*algebraic[200]
    algebraic[217] = (algebraic[136]+constants[54]+algebraic[207])*states[17]
    algebraic[222] = algebraic[82]*states[16]+constants[55]*states[23]+constants[173]*states[22]
    algebraic[215] = (algebraic[159]+constants[173])*states[22]
    algebraic[221] = algebraic[120]*states[21]+algebraic[207]*states[17]
    algebraic[138] = algebraic[118]*constants[174]
    algebraic[223] = algebraic[187]/constants[174]
    algebraic[143] = algebraic[122]*constants[174]
    algebraic[225] = algebraic[198]/constants[174]
    algebraic[149] = algebraic[126]*constants[174]
    algebraic[227] = algebraic[205]/constants[174]
    algebraic[67] = constants[161]*constants[137]*exp(116431./constants[157]+-578.317/constants[5]+(0.764126*states[6])/constants[138])
    algebraic[157] = algebraic[67]
    algebraic[78] = constants[161]*constants[137]*exp(-55700.7/constants[157]+-130.639/constants[5]+(-3.64982*states[6])/constants[138])
    algebraic[229] = algebraic[78]
    algebraic[57] = constants[161]*constants[137]*exp(-97657.8/constants[157]+1.51000/constants[5]+(0.0684862*states[6])/constants[138])
    algebraic[231] = algebraic[57]
    algebraic[48] = constants[161]*constants[137]*exp(-62123.1/constants[157]+39.2950/constants[5]+(0.288816*states[6])/constants[138])
    algebraic[233] = algebraic[48]
    algebraic[119] = constants[124]*log(constants[12]/states[0])
    algebraic[131] = constants[91]*(states[45]+states[46])*(states[6]-algebraic[119])
    algebraic[228] = constants[92]*(states[6]-algebraic[119])
    algebraic[234] = states[6]/constants[124]
    algebraic[240] = exp(constants[99]*algebraic[234])*(power(states[0], 3.00000))*constants[13]
    algebraic[241] = exp((constants[99]-1.00000)*algebraic[234])*(power(constants[12], 3.00000))*states[2]
    algebraic[242] = 1.00000+constants[98]*exp((constants[99]-1.00000)*algebraic[234])
    algebraic[243] = (constants[95]*(algebraic[240]-algebraic[241]))/(constants[172]*algebraic[242]*constants[175])
    algebraic[235] = 1.00000+0.124500*exp(-0.100000*algebraic[234])
    algebraic[236] = 0.0365000*constants[163]*exp(-1.33000*algebraic[234])
    algebraic[237] = 1.00000/(algebraic[235]+algebraic[236])
    algebraic[238] = 1.00000+power(constants[101]/states[0], 1.50000)
    algebraic[239] = (constants[100]*algebraic[237]*constants[167])/algebraic[238]
    algebraic[150] = states[6]/constants[124]
    algebraic[158] = 1000.00*constants[3]*algebraic[150]
    algebraic[177] = exp(algebraic[150])-1.00000
    algebraic[199] = states[0]*exp(algebraic[150])-constants[12]
    algebraic[206] = (0.0200000*constants[133]*states[39]*algebraic[158]*algebraic[199])/algebraic[177]
    algebraic[127] = 0.500000*constants[124]*log(constants[13]/states[2])
    algebraic[230] = constants[105]*(states[6]-algebraic[127])
    algebraic[232] = (constants[103]*states[2])/(constants[104]+states[2])
    algebraic[60] = (states[3]-states[2])/constants[27]
    algebraic[91] = constants[28]*algebraic[70]+constants[29]*algebraic[81]
    algebraic[111] = 1.00000/(1.00000+(constants[34]*constants[36])/(power(states[2]+constants[36], 2.00000))+(constants[35]*constants[38])/(power(states[2]+constants[38], 2.00000)))
    algebraic[244] = states[6]/constants[124]
    algebraic[245] = 1000.00*constants[3]*algebraic[244]
    algebraic[246] = 0.00100000*exp(2.00000*algebraic[244])-constants[13]*0.341000
    algebraic[247] = exp(2.00000*algebraic[244])-1.00000
    algebraic[248] = (constants[156]*4.00000*algebraic[245]*algebraic[246])/algebraic[247]
    algebraic[249] = algebraic[248]*states[24]*states[23]
    algebraic[101] = 1.00000/(1.00000+(constants[34]*constants[36])/(power(states[3]+constants[36], 2.00000))+(constants[35]*constants[38])/(power(states[3]+constants[38], 2.00000)))
    algebraic[123] = constants[124]*log(constants[11]/states[1])
    algebraic[135] = constants[88]*constants[134]*states[47]*(states[6]-algebraic[123])
    algebraic[139] = constants[89]*(states[48]+states[49])*(states[6]-algebraic[123])
    algebraic[224] = 1.00000/(0.940000+exp((1.26000/constants[124])*(states[6]-algebraic[123])))
    algebraic[226] = constants[90]*(power(constants[11]/1.00000, 1.0/2))*algebraic[224]*(states[6]-algebraic[123])
    algebraic[250] = custom_piecewise([greater_equal(algebraic[248] , 0.00000), 0.00000 , True, algebraic[248]])
    algebraic[251] = constants[136]/(1.00000+algebraic[250]/constants[106])
    algebraic[252] = states[1]*exp(algebraic[244])-constants[11]
    algebraic[253] = exp(algebraic[244])-1.00000
    algebraic[254] = (algebraic[251]*states[23]*states[24]*algebraic[245]*algebraic[252])/algebraic[253]
    algebraic[0] = floor(voi/constants[14])*constants[14]
    algebraic[11] = custom_piecewise([greater_equal(voi-algebraic[0] , constants[17]) & less_equal(voi-algebraic[0] , constants[17]+constants[15]), constants[16] , True, 0.00000])
    algebraic[144] = constants[132]*states[29]*(states[6]-algebraic[123])
    algebraic[168] = states[1]*exp(algebraic[150])-constants[11]
    algebraic[188] = (constants[133]*states[39]*algebraic[158]*algebraic[168])/algebraic[177]
    algebraic[213] = algebraic[188]+algebraic[206]
    algebraic[220] = algebraic[144]+algebraic[213]
    algebraic[255] = algebraic[131]+algebraic[249]+algebraic[254]+algebraic[135]+algebraic[139]+algebraic[226]+algebraic[243]+algebraic[239]+algebraic[220]+algebraic[232]+algebraic[230]+algebraic[228]+algebraic[11]
    algebraic[6] = states[1]+0.0183300*states[0]
    algebraic[17] = constants[124]*log(constants[154]/algebraic[6])
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
        self.iso = 0
        self.CSQN2 = 0
        self.RyR2 = 0
        self.Faraday = 96.5
        self.Temp = 310
        self.Rgas = 8.315
        self.Acap = 0.0001534
        self.Vmyo = 2.584e-5
        self.VJSR = 1.6e-7
        self.VNSR = 2.1e-6
        self.VSS = 1.2e-9
        self.Ko = 4
        self.Nao = 138
        self.Cao = 2
        self.stim_period = 500
        self.stim_duration = 3
        self.stim_amplitude = -15
        self.stim_offset = 100
        self.Kfb = 0.000168
        self.Nfb = 1.2
        self.Krb = 3.29
        self.Nrb = 1
        self.KSR = 1.2
        self.vmaxf = 7.48e-5
        self.vmaxr = 0.000318
        self.v1 = 1.8
        self.tautr = 0.5747
        self.tauxfer = 26.7
        self.LTRPNtot = 0.07
        self.HTRPNtot = 0.14
        self.khtrpn_plus = 20
        self.khtrpn_minus = 6.6e-5
        self.kltrpn_plus = 40
        self.kltrpn_minus = 0.04
        self.CMDNtot = 0.05
        self.EGTAtot = 0
        self.KmCMDN = 0.00238
        self.KmCSQN = 0.8
        self.KmEGTA = 0.00015
        self.kaplus = 0.01215
        self.kaminus = 0.576
        self.kbplus = 0.00405
        self.kbminus = 1.93
        self.kcplus = 0.1
        self.kcminus = 0.0008
        self.ncoop = 4
        self.mcoop = 3
        self.kryr = 1
        self.HmaxC1O1 = 0.5
        self.HmaxC2O1 = 0.5
        self.Hmin = 5
        self.H50C1O1 = 1
        self.H50O1C2 = 1
        self.HN = 2.5
        self.fL = 0.3
        self.gL = 4
        self.bL = 2
        self.aL = 2
        self.alphaa0Kv43 = 0.543708
        self.aaKv43 = 0.028983
        self.betaa0Kv43 = 0.080185
        self.baKv43 = 0.0468437
        self.alphai0Kv43 = 0.0498424
        self.aiKv43 = 0.000373016
        self.betai0Kv43 = 0.000819482
        self.biKv43 = 5.374e-8
        self.f1Kv43 = 1.8936
        self.f2Kv43 = 14.224647456
        self.f3Kv43 = 158.574378389
        self.f4Kv43 = 142.936645351
        self.b1Kv43 = 6.77348
        self.b2Kv43 = 15.6212705152
        self.b3Kv43 = 28.7532603313
        self.b4Kv43 = 524.576206679
        self.f1Kv14 = 0.52465073996
        self.f2Kv14 = 17.51885408639
        self.f3Kv14 = 938.58764534556
        self.f4Kv14 = 54749.194733326
        self.b1Kv14 = 1.00947847105
        self.b2Kv14 = 1.17100540567
        self.b3Kv14 = 0.63902768758
        self.b4Kv14 = 2.12035379095
        self.alphaa0Kv14 = 1.84002414554
        self.aaKv14 = 0.00768548031
        self.betaa0Kv14 = 0.0108174834
        self.baKv14 = 0.07793378174
        self.alphai0Kv14 = 0.00305767916
        self.betai0Kv14 = 2.44936e-6
        self.GKr = 0.0186
        self.GKs = 0.0035
        self.GK1 = 0.125305126118808
        self.GNa = 56.32
        self.GNab = 0.001
        self.KvScale = 0.872
        self.Kv43Frac = 0.889
        self.kNaCa = 0.44
        self.KmNa = 87.5
        self.KmCa = 1.38
        self.ksat = 0.2
        self.eta = 0.35
        self.INaKmax = 2.387
        self.KmNai = 20
        self.KmKo = 1.5
        self.IpCamax = 0.05
        self.KmpCa = 0.0005
        self.GCab = 7.684e-5
        self.ICahalf = -0.265
        self.Pscale = 7
        self.TNa = 294.16
        self.T_Const_HERG = 5.320000001
        self.A0_HERG = 0.017147641733086
        self.B0_HERG = 0.03304608038835
        self.A1_HERG = 0.03969328381141
        self.B1_HERG = -0.0430605416398
        self.A2_HERG = 0.02057448605977
        self.B2_HERG = 0.02617412715118
        self.A3_HERG = 0.00134366604423
        self.B3_HERG = -0.02691385498399
        self.A4_HERG = 0.10666316491288
        self.B4_HERG = 0.00568908859717
        self.A5_HERG = 0.00646393910049
        self.B5_HERG = -0.04536642959543
        self.A6_HERG = 8.039374403e-5
        self.B6_HERG = 6.9808924e-7
        self.omega = 0.250000*0.0100000
        self.a1_Cainf = 0.820000
        self.C0ks_C1ks = 0.00795601
        self.C1ks_O1ks = 0.0396672
        self.Temp_Scale = 1.38862
        self.parameter_a = 1.40043

    def to_dict(self):
        return {
            "iso": self.iso,
            "CSQN2": self.CSQN2,
            "RyR2": self.RyR2,
            "Faraday": self.Faraday,
            "Temp": self.Temp,
            "Rgas": self.Rgas,
            "Acap": self.Acap,
            "Vmyo": self.Vmyo,
            "VJSR": self.VJSR,
            "VNSR": self.VNSR,
            "VSS": self.VSS,
            "Ko": self.Ko,
            "Nao": self.Nao,
            "Cao": self.Cao,
            "stim_period": self.stim_period,
            "stim_duration": self.stim_duration,
            "stim_amplitude": self.stim_amplitude,
            "stim_offset": self.stim_offset,
            "Kfb": self.Kfb,
            "Nfb": self.Nfb,
            "Krb": self.Krb,
            "Nrb": self.Nrb,
            "KSR": self.KSR,
            "vmaxf": self.vmaxf,
            "vmaxr": self.vmaxr,
            "v1": self.v1,
            "tautr": self.tautr,
            "tauxfer": self.tauxfer,
            "LTRPNtot": self.LTRPNtot,
            "HTRPNtot": self.HTRPNtot,
            "khtrpn_plus": self.khtrpn_plus,
            "khtrpn_minus": self.khtrpn_minus,
            "kltrpn_plus": self.kltrpn_plus,
            "kltrpn_minus": self.kltrpn_minus,
            "CMDNtot": self.CMDNtot,
            "EGTAtot": self.EGTAtot,
            "KmCMDN": self.KmCMDN,
            "KmCSQN": self.KmCSQN,
            "KmEGTA": self.KmEGTA,
            "kaplus": self.kaplus,
            "kaminus": self.kaminus,
            "kbplus": self.kbplus,
            "kbminus": self.kbminus,
            "kcplus": self.kcplus,
            "kcminus": self.kcminus,
            "ncoop": self.ncoop,
            "mcoop": self.mcoop,
            "kryr": self.kryr,
            "HmaxC1O1": self.HmaxC1O1,
            "HmaxC2O1": self.HmaxC2O1,
            "Hmin": self.Hmin,
            "H50C1O1": self.H50C1O1,
            "H50O1C2": self.H50O1C2,
            "HN": self.HN,
            "fL": self.fL,
            "gL": self.gL,
            "bL": self.bL,
            "aL": self.aL,
            "alphaa0Kv43": self.alphaa0Kv43,
            "aaKv43": self.aaKv43,
            "betaa0Kv43": self.betaa0Kv43,
            "baKv43": self.baKv43,
            "alphai0Kv43": self.alphai0Kv43,
            "aiKv43": self.aiKv43,
            "betai0Kv43": self.betai0Kv43,
            "biKv43": self.biKv43,
            "f1Kv43": self.f1Kv43,
            "f2Kv43": self.f2Kv43,
            "f3Kv43": self.f3Kv43,
            "f4Kv43": self.f4Kv43,
            "b1Kv43": self.b1Kv43,
            "b2Kv43": self.b2Kv43,
            "b3Kv43": self.b3Kv43,
            "b4Kv43": self.b4Kv43,
            "f1Kv14": self.f1Kv14,
            "f2Kv14": self.f2Kv14,
            "f3Kv14": self.f3Kv14,
            "f4Kv14": self.f4Kv14,
            "b1Kv14": self.b1Kv14,
            "b2Kv14": self.b2Kv14,
            "b3Kv14": self.b3Kv14,
            "b4Kv14": self.b4Kv14,
            "alphaa0Kv14": self.alphaa0Kv14,
            "aaKv14": self.aaKv14,
            "betaa0Kv14": self.betaa0Kv14,
            "baKv14": self.baKv14,
            "alphai0Kv14": self.alphai0Kv14,
            "betai0Kv14": self.betai0Kv14,
            "GKr": self.GKr,
            "GKs": self.GKs,
            "GK1": self.GK1,
            "GNa": self.GNa,
            "GNab": self.GNab,
            "KvScale": self.KvScale,
            "Kv43Frac": self.Kv43Frac,
            "kNaCa": self.kNaCa,
            "KmNa": self.KmNa,
            "KmCa": self.KmCa,
            "ksat": self.ksat,
            "eta": self.eta,
            "INaKmax": self.INaKmax,
            "KmNai": self.KmNai,
            "KmKo": self.KmKo,
            "IpCamax": self.IpCamax,
            "KmpCa": self.KmpCa,
            "GCab": self.GCab,
            "ICahalf": self.ICahalf,
            "Pscale": self.Pscale,
            "TNa": self.TNa,
            "T_Const_HERG": self.T_Const_HERG,
            "A0_HERG": self.A0_HERG,
            "B0_HERG": self.B0_HERG,
            "A1_HERG": self.A1_HERG,
            "B1_HERG": self.B1_HERG,
            "A2_HERG": self.A2_HERG,
            "B2_HERG": self.B2_HERG,
            "A3_HERG": self.A3_HERG,
            "B3_HERG": self.B3_HERG,
            "A4_HERG": self.A4_HERG,
            "B4_HERG": self.B4_HERG,
            "A5_HERG": self.A5_HERG,
            "B5_HERG": self.B5_HERG,
            "A6_HERG": self.A6_HERG,
            "B6_HERG": self.B6_HERG,
            "omega": self.omega,
            "a1_Cainf": self.a1_Cainf,
            "C0ks_C1ks": self.C0ks_C1ks,
            "C1ks_O1ks": self.C1ks_O1ks,
            "Temp_Scale": self.Temp_Scale,
            "parameter_a": self.parameter_a,
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
        y0=[9.85573275838928, 125.427082712469, 0.000363968672182656, 0.000506604278037024, 0.421936980515042, 0.423551621440241, -86.7261544519706, 0.00113684728532807, 3.11350788541838e-7, 0.280466039150394, 0.99347761599363, 0.132070890861418, 0.866791951404883, 0.465679150104636, 0.00834457719966281, 5.60736209083906e-5, 1.6747092904465e-7, 1.87571666668874e-10, 0.489846779190386, 0.035111008610982, 0.000943745917866092, 1.12741202215634e-5, 5.05056944609524e-8, 1.40806027419488e-11, 0.995434385054729, 0.908189132330738, 0.0343385704915328, 0.000487654173162347, 3.11550715247964e-6, 7.42911977991342e-9, 0.0349937004781012, 0.0171163265867255, 0.00428471710061031, 0.000564724236640674, 2.19603439704397e-5, 0.149374350989705, 0.0606794865684932, 0.00930314185504921, 0.000676403999474111, 3.85187206387239e-5, 0.0442722560882536, 0.00952432663172288, 0.0567396669678271, 0.113122845136053, 0.556269044084734, 1.02118700961583e-7, 1.93499158844817e-8, 0.00120284688677794, 5.65460174551007e-7, 0.0258818770122187, 0.111284526171411, 0.0481019786429977, 0.00779692701457915, 0.000561699600929369, 1.51746424723121e-5, 0.368582741846592, 0.312463212648791, 0.0993398770493615, 0.0140431688972267, 0.000750073829883749, 0.0370604970714329, 0.994948338598163, 0.000595653663190548, 0.000228183228829573, 0.000243789721526602, 0.938064990549233, 0.0360525668093578],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "iyer_2007_ss"
        self.curve_names = [
            "Nai",
            "Ki",
            "Cai",
            "CaSS",
            "CaJSR",
            "CaNSR",
            "V",
            "O1_RyR",
            "O2_RyR",
            "LTRPNCa",
            "HTRPNCa",
            "C1_RyR",
            "C2_RyR",
            "C0",
            "C1",
            "C2",
            "C3",
            "C4",
            "CCa0",
            "CCa1",
            "CCa2",
            "CCa3",
            "CCa4",
            "Open",
            "yCa",
            "C0Kv43",
            "C1Kv43",
            "C2Kv43",
            "C3Kv43",
            "OKv43",
            "CI0Kv43",
            "CI1Kv43",
            "CI2Kv43",
            "CI3Kv43",
            "OIKv43",
            "C0Kv14",
            "C1Kv14",
            "C2Kv14",
            "C3Kv14",
            "OKv14",
            "CI0Kv14",
            "CI1Kv14",
            "CI2Kv14",
            "CI3Kv14",
            "OIKv14",
            "na6",
            "na7",
            "OHerg",
            "O1ks",
            "O2ks",
            "na1",
            "na2",
            "na3",
            "na4",
            "na5",
            "na8",
            "na9",
            "na10",
            "na11",
            "na12",
            "na13",
            "C1Herg",
            "C2Herg",
            "C3Herg",
            "IHerg",
            "C0ks",
            "C1ks",
        ]
        self.state_names = ['Nai', 'Ki', 'Cai', 'CaSS', 'CaJSR', 'CaNSR', 'V', 'O1_RyR', 'O2_RyR', 'LTRPNCa', 'HTRPNCa', 'C1_RyR', 'C2_RyR', 'C0', 'C1', 'C2', 'C3', 'C4', 'CCa0', 'CCa1', 'CCa2', 'CCa3', 'CCa4', 'Open', 'yCa', 'C0Kv43', 'C1Kv43', 'C2Kv43', 'C3Kv43', 'OKv43', 'CI0Kv43', 'CI1Kv43', 'CI2Kv43', 'CI3Kv43', 'OIKv43', 'C0Kv14', 'C1Kv14', 'C2Kv14', 'C3Kv14', 'OKv14', 'CI0Kv14', 'CI1Kv14', 'CI2Kv14', 'CI3Kv14', 'OIKv14', 'na6', 'na7', 'OHerg', 'O1ks', 'O2ks', 'na1', 'na2', 'na3', 'na4', 'na5', 'na8', 'na9', 'na10', 'na11', 'na12', 'na13', 'C1Herg', 'C2Herg', 'C3Herg', 'IHerg', 'C0ks', 'C1ks']
        self.algebraic_names = ['past', 'klumenC1O1', 'alpha', 'yCa_inf', 'alpha_act43', 'alpha_act14', 'a2', 'alpha1', 'C1H_to_C2H', 'C3H_to_OH', 'O1ks_O2ks', 'i_Stim', 'klumenO1C2', 'beta', 'tau_yCa', 'beta_act43', 'beta_act14', 'EKs', 'beta1', 'C2H_to_C1H', 'OH_to_C3H', 'O1ks_C1ks', 'fb', 'klumenC2O1', 'alpha_prime', 'alpha_inact43', 'C0Kv14_to_C1Kv14', 'CI0Kv14_to_CI1Kv14', 'gamma1', 'OH_to_IH', 'a1_C2', 'O2ks_O1ks', 'C1ks_C0ks', 'rb', 'dC1_RyR', 'beta_prime', 'beta_inact43', 'C1Kv14_to_C2Kv14', 'CI1Kv14_to_CI2Kv14', 'Delta1', 'IH_to_OH', 'a2_C2', 'Jup', 'dO2_RyR', 'gamma', 'C0Kv43_to_C1Kv43', 'C2Kv14_to_C3Kv14', 'CI2Kv14_to_CI3Kv14', 'On', 'C3H_to_IH', 'a1_O', 'Jrel', 'dC2_RyR', 'C0_to_C1', 'C1Kv43_to_C2Kv43', 'C3Kv14_to_OKv14', 'CI3Kv14_to_OIKv14', 'Of', 'IH_to_C3H', 'a2_O', 'Jxfer', 'Jtr', 'dO1_RyR', 'C1_to_C2', 'C2Kv43_to_C3Kv43', 'C1Kv14_to_C0Kv14', 'CI1Kv14_to_CI0Kv14', 'GammaGamma', 'a1_C3', 'a1_I', 'dLTRPNCa', 'beta_JSR', 'C2_to_C3', 'C3Kv43_to_OKv43', 'C2Kv14_to_C1Kv14', 'CI2Kv14_to_CI1Kv14', 'a1_C0', 'a1_CI0', 'DeltaDelta', 'a2_C3', 'a2_I', 'dHTRPNCa', 'C3_to_C4', 'CI0Kv43_to_CI1Kv43', 'C3Kv14_to_C2Kv14', 'CI3Kv14_to_CI2Kv14', 'a2_C0', 'a1_C1', 'a2_CI0', 'a1_CI1', 'rho', 'Jtrpn', 'CCa0_to_CCa1', 'CI1Kv43_to_CI2Kv43', 'OKv14_to_C3Kv14', 'OIKv14_to_CI3Kv14', 'a2_C1', 'a1_C2_1', 'a2_CI1', 'a1_CI2', 'mu', 'beta_SS', 'CCa1_to_CCa2', 'CI2Kv43_to_CI3Kv43', 'a2_C2_1', 'a1_C3_1', 'a1_O_1', 'a2_CI2', 'a1_CI3', 'a1_OI', 'k12', 'beta_i', 'CCa2_to_CCa3', 'CI3Kv43_to_OIKv43', 'a2_C3_1', 'a2_O_1', 'a2_CI3', 'a2_OI', 'k23', 'ENa', 'CCa3_to_CCa4', 'C1Kv43_to_C0Kv43', 'k34', 'EK', 'C1_to_C0', 'C2Kv43_to_C1Kv43', 'k45', 'ECa', 'C2_to_C1', 'C3Kv43_to_C2Kv43', 'k56', 'INa', 'C3_to_C2', 'OKv43_to_C3Kv43', 'k89', 'IKr', 'C4_to_C3', 'CI1Kv43_to_CI0Kv43', 'k910', 'IKs', 'CCa1_to_CCa0', 'C0Kv43_to_CI0Kv43', 'CI2Kv43_to_CI1Kv43', 'k1011', 'IKv43', 'CCa2_to_CCa1', 'C1Kv43_to_CI1Kv43', 'CI3Kv43_to_CI2Kv43', 'CI0Kv43_to_C0Kv43', 'k1112', 'VF_over_RT', 'CCa3_to_CCa2', 'C2Kv43_to_CI2Kv43', 'OIKv43_to_CI3Kv43', 'CI1Kv43_to_C1Kv43', 'a1_C043', 'a1_I043', 'k1213', 'VFsq_over_RT', 'CCa4_to_CCa3', 'C3Kv43_to_CI3Kv43', 'OKv43_to_OIKv43', 'CI2Kv43_to_C2Kv43', 'a2_C043', 'a1_C143', 'a2_I043', 'a1_I143', 'k57', 'a1_K', 'C0_to_CCa0', 'CI3Kv43_to_C3Kv43', 'OIKv43_to_OKv43', 'a2_C143', 'a1_C243', 'a2_I143', 'a1_I243', 'k21', 'a2_1', 'C1_to_CCa1', 'a1_Ca0', 'a1_C0_1', 'a2_C243', 'a1_C343', 'a1_O43', 'a2_I243', 'a1_I343', 'a1_OI43', 'k32', 'IKv14_K', 'C2_to_CCa2', 'a2_Ca0', 'a1_Ca1', 'a2_C0_1', 'a1_C1_1', 'a2_C343', 'a2_O43', 'a2_I343', 'a2_OI43', 'k43', 'a1_Na', 'C3_to_CCa3', 'a2_Ca1', 'a1_Ca2', 'a2_C1_1', 'a1_C2_2', 'k54', 'IKv14_Na', 'C4_to_CCa4', 'a2_Ca2', 'a1_Ca3', 'a2_C2_2', 'a1_C3_2', 'k65', 'IKv14', 'a2_Ca3', 'a1_Ca4', 'a2_C3_2', 'a1_C4', 'k98', 'k75', 'Ito1', 'a2_Ca4', 'a2_C4', 'k109', 'K1_inf', 'k1110', 'IK1', 'k1211', 'INab', 'k1312', 'ICab', 'k136', 'IpCa', 'k613', 'VF_over_RT_1', 'a1_Na_1', 'a2_Na', 'fNaK', 'a2_K', 'INaK', 'a1_ncx', 'a2_ncx', 'a3_ncx', 'INaCa', 'VF_over_RT_2', 'VFsq_over_RT_1', 'a1_Ca', 'a2_Ca', 'ICamax', 'ICa', 'Icabar', 'PKprime', 'a1_K_1', 'a2_K_1', 'ICaK', 'i_tot']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 186
        p = self.params

        # direct mapping
        c[0] = p.iso
        c[1] = p.CSQN2
        c[2] = p.RyR2
        c[3] = p.Faraday
        c[4] = p.Temp
        c[5] = p.Rgas
        c[6] = p.Acap
        c[7] = p.Vmyo
        c[8] = p.VJSR
        c[9] = p.VNSR
        c[10] = p.VSS
        c[11] = p.Ko
        c[12] = p.Nao
        c[13] = p.Cao
        c[14] = p.stim_period
        c[15] = p.stim_duration
        c[16] = p.stim_amplitude
        c[17] = p.stim_offset
        c[18] = p.Kfb
        c[19] = p.Nfb
        c[20] = p.Krb
        c[21] = p.Nrb
        c[22] = p.KSR
        c[23] = p.vmaxf
        c[24] = p.vmaxr
        c[25] = p.v1
        c[26] = p.tautr
        c[27] = p.tauxfer
        c[28] = p.LTRPNtot
        c[29] = p.HTRPNtot
        c[30] = p.khtrpn_plus
        c[31] = p.khtrpn_minus
        c[32] = p.kltrpn_plus
        c[33] = p.kltrpn_minus
        c[34] = p.CMDNtot
        c[35] = p.EGTAtot
        c[36] = p.KmCMDN
        c[37] = p.KmCSQN
        c[38] = p.KmEGTA
        c[39] = p.kaplus
        c[40] = p.kaminus
        c[41] = p.kbplus
        c[42] = p.kbminus
        c[43] = p.kcplus
        c[44] = p.kcminus
        c[45] = p.ncoop
        c[46] = p.mcoop
        c[47] = p.kryr
        c[48] = p.HmaxC1O1
        c[49] = p.HmaxC2O1
        c[50] = p.Hmin
        c[51] = p.H50C1O1
        c[52] = p.H50O1C2
        c[53] = p.HN
        c[54] = p.fL
        c[55] = p.gL
        c[56] = p.bL
        c[57] = p.aL
        c[58] = p.alphaa0Kv43
        c[59] = p.aaKv43
        c[60] = p.betaa0Kv43
        c[61] = p.baKv43
        c[62] = p.alphai0Kv43
        c[63] = p.aiKv43
        c[64] = p.betai0Kv43
        c[65] = p.biKv43
        c[66] = p.f1Kv43
        c[67] = p.f2Kv43
        c[68] = p.f3Kv43
        c[69] = p.f4Kv43
        c[70] = p.b1Kv43
        c[71] = p.b2Kv43
        c[72] = p.b3Kv43
        c[73] = p.b4Kv43
        c[74] = p.f1Kv14
        c[75] = p.f2Kv14
        c[76] = p.f3Kv14
        c[77] = p.f4Kv14
        c[78] = p.b1Kv14
        c[79] = p.b2Kv14
        c[80] = p.b3Kv14
        c[81] = p.b4Kv14
        c[82] = p.alphaa0Kv14
        c[83] = p.aaKv14
        c[84] = p.betaa0Kv14
        c[85] = p.baKv14
        c[86] = p.alphai0Kv14
        c[87] = p.betai0Kv14
        c[88] = p.GKr
        c[89] = p.GKs
        c[90] = p.GK1
        c[91] = p.GNa
        c[92] = p.GNab
        c[93] = p.KvScale
        c[94] = p.Kv43Frac
        c[95] = p.kNaCa
        c[96] = p.KmNa
        c[97] = p.KmCa
        c[98] = p.ksat
        c[99] = p.eta
        c[100] = p.INaKmax
        c[101] = p.KmNai
        c[102] = p.KmKo
        c[103] = p.IpCamax
        c[104] = p.KmpCa
        c[105] = p.GCab
        c[106] = p.ICahalf
        c[107] = p.Pscale
        c[108] = p.TNa
        c[109] = p.T_Const_HERG
        c[110] = p.A0_HERG
        c[111] = p.B0_HERG
        c[112] = p.A1_HERG
        c[113] = p.B1_HERG
        c[114] = p.A2_HERG
        c[115] = p.B2_HERG
        c[116] = p.A3_HERG
        c[117] = p.B3_HERG
        c[118] = p.A4_HERG
        c[119] = p.B4_HERG
        c[120] = p.A5_HERG
        c[121] = p.B5_HERG
        c[122] = p.A6_HERG
        c[123] = p.B6_HERG
        c[128] = p.omega
        c[129] = p.a1_Cainf
        c[141] = p.C0ks_C1ks
        c[142] = p.C1ks_O1ks
        c[161] = p.Temp_Scale
        c[174] = p.parameter_a

        # derived constants
        c[124] = (c[5]*c[4])/c[3]
        c[125] = (15.0000 if equal(c[2] , 1.00000) else 0.500000*15.0000)
        c[126] = (0.200000 if equal(c[1] , 1.00000) else 0.500000)
        c[127] = (0.500000 if equal(c[1] , 1.00000) else 1.00000)
        c[130] = c[86]
        c[131] = c[87]
        c[132] = c[94]*c[93]*0.100000
        c[133] = (1.00000-c[94])*c[93]*4.29860e-07
        c[134] = power(c[11]/4.00000, 1.0/2)
        c[135] = c[6]*0.00100000
        c[136] = c[107]*4.57400e-07
        c[137] = (1.38100e-23*c[108])/6.62600e-31
        c[138] = (c[5]*c[108])/c[3]
        c[139] = c[109]*0.0260836
        c[140] = c[109]*0.148330
        c[143] = c[128]
        c[144] = c[131]
        c[145] = c[74]*c[131]
        c[146] = c[75]*c[131]
        c[147] = c[76]*c[131]
        c[148] = c[77]*c[131]
        c[149] = c[130]
        c[150] = c[130]/c[78]
        c[151] = c[130]/c[79]
        c[152] = c[130]/c[80]
        c[153] = c[130]/c[81]
        c[154] = c[11]+0.0183300*c[12]
        c[155] = c[135]/(c[7]*c[3])
        c[156] = (c[107]*0.000246900 if equal(c[0] , 0.00000) else 1.50000*c[107]*0.000246900)
        c[157] = c[5]*c[108]
        c[158] = 1.00000/c[124]
        c[159] = c[143]/c[56]
        c[160] = c[135]/(2.00000*c[10]*c[3])
        c[162] = c[159]/c[56]
        c[163] = (exp(c[12]/67.3000)-1.00000)/7.00000
        c[164] = c[161]*c[137]*exp(-287913./c[157]+786.217/c[5])
        c[165] = c[161]*c[137]*exp(-85800.4/c[157]+70.0780/c[5])
        c[166] = c[161]*c[137]*exp(-121955./c[157]+225.175/c[5])
        c[167] = c[11]/(c[11]+c[102])
        c[168] = c[162]/c[56]
        c[169] = c[161]*c[137]*exp(-59565.2/c[157]+0.00711000/c[5])
        c[170] = c[165]
        c[171] = c[166]
        c[172] = c[97]+c[13]
        c[173] = c[168]/c[56]
        c[175] = (power(c[96], 3.00000)+power(c[12], 3.00000))/5000.00
        c[176] = c[169]
        c[177] = c[164]
        c[178] = c[176]/c[174]
        c[179] = c[177]*c[174]
        c[180] = c[178]/c[174]
        c[181] = c[179]*c[174]
        c[182] = c[180]/c[174]
        c[183] = c[181]*c[174]
        c[184] = c[182]/c[174]
        c[185] = c[183]*c[174]

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
