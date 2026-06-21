# Size of variable arrays:
sizeAlgebraic = 64
sizeStates = 36
sizeConstants = 125
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (s)"
    legend_states[0] = "NAn in component NAn (mM)"
    legend_algebraic[0] = "Vn_leak_Na in component Vn_leak_Na (mM_per_s)"
    legend_algebraic[3] = "Vn_pump in component Vn_pump (mM_per_s)"
    legend_algebraic[39] = "Vn_stim in component Vn_stim (mM_per_s)"
    legend_states[1] = "GLCn in component GLCn (mM)"
    legend_algebraic[4] = "V_en_GLC in component V_en_GLC (mM_per_s)"
    legend_algebraic[5] = "Vn_hk in component Vn_hk (mM_per_s)"
    legend_states[2] = "G6Pn in component G6Pn (mM)"
    legend_algebraic[6] = "Vn_pgi in component Vn_pgi (mM_per_s)"
    legend_states[3] = "F6Pn in component F6Pn (mM)"
    legend_algebraic[7] = "Vn_pfk in component Vn_pfk (mM_per_s)"
    legend_states[4] = "GAPn in component GAPn (mM)"
    legend_algebraic[47] = "Vn_pgk in component Vn_pgk (mM_per_s)"
    legend_states[5] = "PEPn in component PEPn (mM)"
    legend_algebraic[49] = "Vn_pk in component Vn_pk (mM_per_s)"
    legend_states[6] = "PYRn in component PYRn (mM)"
    legend_algebraic[40] = "Vn_ldh in component Vn_ldh (mM_per_s)"
    legend_algebraic[50] = "Vn_mito in component Vn_mito (mM_per_s)"
    legend_states[7] = "LACn in component LACn (mM)"
    legend_algebraic[8] = "Vne_LAC in component Vne_LAC (mM_per_s)"
    legend_states[8] = "NADHn in component NADHn (mM)"
    legend_states[9] = "ATPn in component ATPn (mM)"
    legend_constants[0] = "nOP in component model_parameters (dimensionless)"
    legend_algebraic[9] = "Vn_ATPase in component Vn_ATPase (mM_per_s)"
    legend_algebraic[51] = "Vn_ck in component Vn_ck (mM_per_s)"
    legend_algebraic[55] = "dAMP_dATPn in component dAMP_dATPn (dimensionless)"
    legend_states[10] = "PCrn in component PCrn (mM)"
    legend_states[11] = "O2n in component O2n (mM)"
    legend_constants[1] = "NAero in component model_parameters (dimensionless)"
    legend_algebraic[10] = "Vcn_O2 in component Vcn_O2 (mM_per_s)"
    legend_states[12] = "GLUn in component GLUn (mM)"
    legend_constants[2] = "Rng in component model_parameters (dimensionless)"
    legend_algebraic[28] = "Vg_gs in component Vg_gs (mM_per_s)"
    legend_algebraic[42] = "Vn_stim_GLU in component Vn_stim_GLU (mM_per_s)"
    legend_states[13] = "NAg in component NAg (mM)"
    legend_algebraic[11] = "Vg_leak_Na in component Vg_leak_Na (mM_per_s)"
    legend_algebraic[12] = "Vg_pump in component Vg_pump (mM_per_s)"
    legend_algebraic[29] = "Veg_GLU in component Veg_GLU (mM_per_s)"
    legend_states[14] = "GLCg in component GLCg (mM)"
    legend_algebraic[14] = "Vcg_GLC in component Vcg_GLC (mM_per_s)"
    legend_algebraic[13] = "Veg_GLC in component Veg_GLC (mM_per_s)"
    legend_algebraic[15] = "Vg_hk in component Vg_hk (mM_per_s)"
    legend_states[15] = "G6Pg in component G6Pg (mM)"
    legend_algebraic[16] = "Vg_pgi in component Vg_pgi (mM_per_s)"
    legend_algebraic[18] = "Vg_glys in component Vg_glys (mM_per_s)"
    legend_algebraic[24] = "Vg_glyp in component Vg_glyp (mM_per_s)"
    legend_states[16] = "F6Pg in component F6Pg (mM)"
    legend_algebraic[17] = "Vg_pfk in component Vg_pfk (mM_per_s)"
    legend_states[17] = "GAPg in component GAPg (mM)"
    legend_algebraic[56] = "Vg_pgk in component Vg_pgk (mM_per_s)"
    legend_states[18] = "PEPg in component PEPg (mM)"
    legend_algebraic[58] = "Vg_pk in component Vg_pk (mM_per_s)"
    legend_states[19] = "PYRg in component PYRg (mM)"
    legend_algebraic[43] = "Vg_ldh in component Vg_ldh (mM_per_s)"
    legend_algebraic[59] = "Vg_mito in component Vg_mito (mM_per_s)"
    legend_states[20] = "LACg in component LACg (mM)"
    legend_algebraic[19] = "Vge_LAC in component Vge_LAC (mM_per_s)"
    legend_algebraic[21] = "Vgc_LAC in component Vgc_LAC (mM_per_s)"
    legend_states[21] = "NADHg in component NADHg (mM)"
    legend_states[22] = "ATPg in component ATPg (mM)"
    legend_algebraic[23] = "Vg_ATPase in component Vg_ATPase (mM_per_s)"
    legend_algebraic[60] = "Vg_ck in component Vg_ck (mM_per_s)"
    legend_algebraic[63] = "dAMP_dATPg in component dAMP_dATPg (dimensionless)"
    legend_states[23] = "PCrg in component PCrg (mM)"
    legend_states[24] = "O2g in component O2g (mM)"
    legend_algebraic[25] = "Vcg_O2 in component Vcg_O2 (mM_per_s)"
    legend_states[25] = "GLYg in component GLYg (mM)"
    legend_states[26] = "GLUg in component GLUg (mM)"
    legend_states[27] = "GLCe in component GLCe (mM)"
    legend_constants[3] = "Reg in component model_parameters (dimensionless)"
    legend_constants[4] = "Ren in component model_parameters (dimensionless)"
    legend_algebraic[26] = "Vce_GLC in component Vce_GLC (mM_per_s)"
    legend_states[28] = "LACe in component LACe (mM)"
    legend_algebraic[27] = "Vec_LAC in component Vec_LAC (mM_per_s)"
    legend_states[29] = "GLUe in component GLUe (mM)"
    legend_states[30] = "O2c in component O2c (mM)"
    legend_constants[5] = "Rcn in component model_parameters (dimensionless)"
    legend_constants[6] = "Rcg in component model_parameters (dimensionless)"
    legend_algebraic[33] = "Vc_O2 in component Vc_O2 (mM_per_s)"
    legend_states[31] = "GLCc in component GLCc (mM)"
    legend_constants[7] = "Rce in component model_parameters (dimensionless)"
    legend_algebraic[34] = "Vc_GLC in component Vc_GLC (mM_per_s)"
    legend_states[32] = "LACc in component LACc (mM)"
    legend_algebraic[35] = "Vc_LAC in component Vc_LAC (mM_per_s)"
    legend_states[33] = "CO2c in component CO2c (mM)"
    legend_algebraic[52] = "Vnc_CO2 in component Vnc_CO2 (mM_per_s)"
    legend_algebraic[32] = "Vc_CO2 in component Vc_CO2 (mM_per_s)"
    legend_algebraic[61] = "Vgc_CO2 in component Vgc_CO2 (mM_per_s)"
    legend_states[34] = "Vv in component Vv (dimensionless)"
    legend_algebraic[30] = "Fin_t in component Fin_t (per_s)"
    legend_algebraic[36] = "Fout_t in component Fout_t (per_s)"
    legend_states[35] = "dHb in component dHb (mM)"
    legend_constants[8] = "O2a in component model_parameters (mM)"
    legend_constants[9] = "gn_NA in component Vn_leak_Na (mS_per_cm2)"
    legend_constants[10] = "Sm_n in component model_parameters (per_cm)"
    legend_constants[11] = "Vm in component model_parameters (mV)"
    legend_constants[12] = "Vn in component model_parameters (dimensionless)"
    legend_constants[13] = "RT in component model_parameters (mV_C_per_mol)"
    legend_constants[14] = "F in component model_parameters (C_per_mole)"
    legend_constants[15] = "NAe in component model_parameters (mM)"
    legend_constants[16] = "kpump in component model_parameters (cm_per_mM_per_s)"
    legend_constants[17] = "Km_pump in component model_parameters (mM)"
    legend_algebraic[37] = "v_stim in component v_stim (mM_per_s)"
    legend_constants[18] = "Km_en_GLC in component V_en_GLC (mM)"
    legend_constants[19] = "Vm_en_GLC in component V_en_GLC (mM_per_s)"
    legend_constants[20] = "Vmax_n_hk in component Vn_hk (mM_per_s)"
    legend_constants[21] = "Km_GLC in component model_parameters (mM)"
    legend_constants[22] = "G6P_inh_hk in component model_parameters (mM)"
    legend_constants[23] = "aG6P_inh_hk in component model_parameters (dimensionless)"
    legend_constants[24] = "Vmaxf_n_pgi in component Vn_pgi (mM_per_s)"
    legend_constants[25] = "Vmaxr_n_pgi in component Vn_pgi (mM_per_s)"
    legend_constants[26] = "Km_G6P in component model_parameters (mM)"
    legend_constants[27] = "Km_F6P_pgi in component model_parameters (mM)"
    legend_constants[28] = "kn_pfk in component Vn_pfk (per_s)"
    legend_constants[29] = "Km_F6P_pfk in component model_parameters (mM)"
    legend_constants[30] = "Ki_ATP in component model_parameters (mM)"
    legend_constants[31] = "nH in component model_parameters (dimensionless)"
    legend_constants[32] = "kn_pgk in component Vn_pgk (per_mM_per_s)"
    legend_algebraic[46] = "ADPn in component ADPn (mM)"
    legend_algebraic[38] = "NADn in component NADn (mM)"
    legend_constants[33] = "kn_pk in component Vn_pk (per_mM_per_s)"
    legend_constants[34] = "kfn_ldh in component Vn_ldh (per_mM_per_s)"
    legend_constants[35] = "krn_ldh in component Vn_ldh (per_mM_per_s)"
    legend_constants[36] = "Vmax_n_mito in component Vn_mito (mM_per_s)"
    legend_constants[37] = "Km_O2 in component model_parameters (mM)"
    legend_constants[38] = "Km_ADP in component model_parameters (mM)"
    legend_constants[39] = "Km_PYR in component model_parameters (mM)"
    legend_constants[40] = "rATP_mito in component model_parameters (dimensionless)"
    legend_constants[41] = "aATP_mito in component model_parameters (dimensionless)"
    legend_constants[42] = "Vmax_ne_LAC in component Vne_LAC (mM_per_s)"
    legend_constants[43] = "Km_ne_LAC in component Vne_LAC (mM)"
    legend_constants[44] = "Vmax_n_ATPase in component Vn_ATPase (mM_per_s)"
    legend_constants[45] = "krn_ck in component Vn_ck (per_mM_per_s)"
    legend_constants[46] = "kfn_ck in component Vn_ck (per_mM_per_s)"
    legend_algebraic[44] = "CRn in component CRn (mM)"
    legend_constants[47] = "nh_O2 in component Vcn_O2 (dimensionless)"
    legend_constants[48] = "PScapn in component Vcn_O2 (per_s)"
    legend_constants[49] = "Ko2 in component model_parameters (mM)"
    legend_constants[50] = "HbOP in component model_parameters (mM)"
    legend_constants[51] = "gg_NA in component Vg_leak_Na (mS_per_cm2)"
    legend_constants[52] = "Sm_g in component model_parameters (per_cm)"
    legend_constants[53] = "Vg in component model_parameters (dimensionless)"
    legend_constants[54] = "Km_eg_GLC in component Veg_GLC (mM)"
    legend_constants[55] = "Vm_eg_GLC in component Veg_GLC (mM_per_s)"
    legend_constants[56] = "KO1 in component model_parameters (dimensionless)"
    legend_constants[57] = "Km_cg_GLC in component Vcg_GLC (mM)"
    legend_constants[58] = "Vm_cg_GLC in component Vcg_GLC (mM_per_s)"
    legend_constants[59] = "Vmax_g_hk in component Vg_hk (mM_per_s)"
    legend_constants[60] = "Vmaxf_g_pgi in component Vg_pgi (mM_per_s)"
    legend_constants[61] = "Vmaxr_g_pgi in component Vg_pgi (mM_per_s)"
    legend_constants[62] = "kg_pfk in component Vg_pfk (per_s)"
    legend_constants[63] = "kg_pgk in component Vg_pgk (per_mM_per_s)"
    legend_algebraic[54] = "ADPg in component ADPg (mM)"
    legend_algebraic[41] = "NADg in component NADg (mM)"
    legend_constants[64] = "kg_pk in component Vg_pk (per_mM_per_s)"
    legend_constants[65] = "kfg_ldh in component Vg_ldh (per_mM_per_s)"
    legend_constants[66] = "krg_ldh in component Vg_ldh (per_mM_per_s)"
    legend_constants[67] = "Vmax_g_mito in component Vg_mito (mM_per_s)"
    legend_constants[68] = "Vmax_ge_LAC in component Vge_LAC (mM_per_s)"
    legend_constants[69] = "Km_ge_LAC in component Vge_LAC (mM)"
    legend_constants[70] = "Vmax_gc_LAC in component Vgc_LAC (mM_per_s)"
    legend_constants[71] = "Km_gc_LAC in component Vgc_LAC (mM)"
    legend_constants[72] = "Vmax_g_ATPase in component Vg_ATPase (mM_per_s)"
    legend_constants[73] = "krg_ck in component Vg_ck (per_mM_per_s)"
    legend_constants[74] = "kfg_ck in component Vg_ck (per_mM_per_s)"
    legend_algebraic[45] = "CRg in component CRg (mM)"
    legend_constants[75] = "PScapg in component Vcg_O2 (per_s)"
    legend_constants[76] = "nh_O2 in component model_parameters (dimensionless)"
    legend_constants[77] = "Vc in component model_parameters (dimensionless)"
    legend_constants[78] = "GLCa in component model_parameters (mM)"
    legend_constants[79] = "Km_ce_GLC in component Vce_GLC (mM)"
    legend_constants[80] = "Vm_ce_GLC in component Vce_GLC (mM_per_s)"
    legend_constants[81] = "LACa in component model_parameters (mM)"
    legend_constants[82] = "Km_ec_LAC in component Vec_LAC (mM)"
    legend_constants[83] = "Vm_ec_LAC in component Vec_LAC (mM_per_s)"
    legend_constants[84] = "R_GLU_NA in component model_parameters (dimensionless)"
    legend_constants[85] = "Km_GLU in component model_parameters (mM)"
    legend_constants[86] = "KO2 in component model_parameters (dimensionless)"
    legend_constants[87] = "Vmax_g_gs in component Vg_gs (mM_per_s)"
    legend_constants[88] = "Km_ATP in component model_parameters (mM)"
    legend_constants[89] = "Vmax_eg_GLU in component Veg_GLU (mM_per_s)"
    legend_constants[90] = "CO2a in component model_parameters (mM)"
    legend_constants[91] = "Vmax_glys in component Vg_glys (mM_per_s)"
    legend_constants[92] = "Km_G6P_glys in component Vg_glys (mM)"
    legend_constants[93] = "GLY_inh in component model_parameters (mM)"
    legend_constants[94] = "aGLY_inh in component model_parameters (dimensionless)"
    legend_constants[95] = "Vmax_glyp in component Vg_glyp (mM_per_s)"
    legend_constants[96] = "Km_GLY in component Vg_glyp (mM)"
    legend_algebraic[22] = "deltaVt_GLY in component Vg_glyp (dimensionless)"
    legend_algebraic[20] = "unitstepSB2 in component unitstepSB2 (dimensionless)"
    legend_constants[97] = "stim in component model_parameters (dimensionless)"
    legend_constants[98] = "to in component model_parameters (s)"
    legend_constants[99] = "to_GLY in component model_parameters (s)"
    legend_constants[100] = "tend_GLY in component model_parameters (s)"
    legend_constants[101] = "sr_GLY in component model_parameters (dimensionless)"
    legend_constants[102] = "t1 in component model_parameters (s)"
    legend_constants[103] = "delta_GLY in component model_parameters (dimensionless)"
    legend_constants[104] = "KO3 in component model_parameters (dimensionless)"
    legend_constants[105] = "CBF0 in component Fin_t (per_s)"
    legend_constants[106] = "tend in component model_parameters (s)"
    legend_constants[107] = "sr in component model_parameters (dimensionless)"
    legend_constants[108] = "deltaf in component model_parameters (dimensionless)"
    legend_constants[109] = "CBF0 in component model_parameters (per_s)"
    legend_constants[110] = "Vv0 in component model_parameters (dimensionless)"
    legend_constants[111] = "tv in component model_parameters (s)"
    legend_constants[112] = "NADH_n_tot in component NADn (mM)"
    legend_constants[113] = "NADH_g_tot in component NADg (mM)"
    legend_constants[114] = "PCrn_tot in component CRn (mM)"
    legend_constants[115] = "PCrg_tot in component CRg (mM)"
    legend_constants[116] = "ATPtot in component model_parameters (mM)"
    legend_constants[117] = "qak in component model_parameters (dimensionless)"
    legend_algebraic[53] = "u_n in component u_n (dimensionless)"
    legend_algebraic[62] = "u_g in component u_g (dimensionless)"
    legend_algebraic[48] = "AMPn in component AMPn (mM)"
    legend_algebraic[57] = "AMPg in component AMPg (mM)"
    legend_algebraic[1] = "BOLD in component BOLD (dimensionless)"
    legend_constants[118] = "k1 in component model_parameters (dimensionless)"
    legend_constants[119] = "k2 in component model_parameters (dimensionless)"
    legend_constants[120] = "k3 in component model_parameters (dimensionless)"
    legend_constants[121] = "dHb0 in component model_parameters (mM)"
    legend_algebraic[31] = "unitpulseSB in component v_stim (dimensionless)"
    legend_constants[122] = "t_n_stim in component model_parameters (s)"
    legend_constants[123] = "v1_n in component model_parameters (mM_per_s)"
    legend_constants[124] = "v2_n in component model_parameters (mM_per_s)"
    legend_algebraic[2] = "unitstepSB in component unitstepSB (dimensionless)"
    legend_rates[0] = "d/dt NAn in component NAn (mM)"
    legend_rates[1] = "d/dt GLCn in component GLCn (mM)"
    legend_rates[2] = "d/dt G6Pn in component G6Pn (mM)"
    legend_rates[3] = "d/dt F6Pn in component F6Pn (mM)"
    legend_rates[4] = "d/dt GAPn in component GAPn (mM)"
    legend_rates[5] = "d/dt PEPn in component PEPn (mM)"
    legend_rates[6] = "d/dt PYRn in component PYRn (mM)"
    legend_rates[7] = "d/dt LACn in component LACn (mM)"
    legend_rates[8] = "d/dt NADHn in component NADHn (mM)"
    legend_rates[9] = "d/dt ATPn in component ATPn (mM)"
    legend_rates[10] = "d/dt PCrn in component PCrn (mM)"
    legend_rates[11] = "d/dt O2n in component O2n (mM)"
    legend_rates[12] = "d/dt GLUn in component GLUn (mM)"
    legend_rates[13] = "d/dt NAg in component NAg (mM)"
    legend_rates[14] = "d/dt GLCg in component GLCg (mM)"
    legend_rates[15] = "d/dt G6Pg in component G6Pg (mM)"
    legend_rates[16] = "d/dt F6Pg in component F6Pg (mM)"
    legend_rates[17] = "d/dt GAPg in component GAPg (mM)"
    legend_rates[18] = "d/dt PEPg in component PEPg (mM)"
    legend_rates[19] = "d/dt PYRg in component PYRg (mM)"
    legend_rates[20] = "d/dt LACg in component LACg (mM)"
    legend_rates[21] = "d/dt NADHg in component NADHg (mM)"
    legend_rates[22] = "d/dt ATPg in component ATPg (mM)"
    legend_rates[23] = "d/dt PCrg in component PCrg (mM)"
    legend_rates[24] = "d/dt O2g in component O2g (mM)"
    legend_rates[25] = "d/dt GLYg in component GLYg (mM)"
    legend_rates[26] = "d/dt GLUg in component GLUg (mM)"
    legend_rates[27] = "d/dt GLCe in component GLCe (mM)"
    legend_rates[28] = "d/dt LACe in component LACe (mM)"
    legend_rates[29] = "d/dt GLUe in component GLUe (mM)"
    legend_rates[30] = "d/dt O2c in component O2c (mM)"
    legend_rates[31] = "d/dt GLCc in component GLCc (mM)"
    legend_rates[32] = "d/dt LACc in component LACc (mM)"
    legend_rates[33] = "d/dt CO2c in component CO2c (mM)"
    legend_rates[34] = "d/dt Vv in component Vv (dimensionless)"
    legend_rates[35] = "d/dt dHb in component dHb (mM)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 15.533
    states[1] = 0.2633
    states[2] = 0.7275
    states[3] = 0.1091
    states[4] = 0.0418
    states[5] = 0.0037
    states[6] = 0.0388
    states[7] = 0.3856
    states[8] = 0.0319
    states[9] = 2.2592
    constants[0] = 15.0
    states[10] = 4.2529
    states[11] = 0.0975
    constants[1] = 3.0
    states[12] = 3.0
    constants[2] = 1.8
    states[13] = 13.36
    states[14] = 0.1656
    states[15] = 0.7326
    states[16] = 0.1116
    states[17] = 0.0698
    states[18] = 0.0254
    states[19] = 0.1711
    states[20] = 0.4651
    states[21] = 0.0445
    states[22] = 2.24
    states[23] = 4.6817
    states[24] = 0.1589
    states[25] = 2.5
    states[26] = 0.0
    states[27] = 0.3339
    constants[3] = 0.8
    constants[4] = 0.4444444444444444
    states[28] = 0.3986
    states[29] = 0.0
    states[30] = 7.4201
    constants[5] = 0.01222
    constants[6] = 0.022
    states[31] = 4.6401
    constants[7] = 0.0275
    states[32] = 0.3251
    states[33] = 2.12
    states[34] = 0.0237
    states[35] = 0.0218
    constants[8] = 8.34
    constants[9] = 0.0039
    constants[10] = 40500
    constants[11] = -70
    constants[12] = 0.45
    constants[13] = 2577340
    constants[14] = 96500
    constants[15] = 150.0
    constants[16] = 3.17e-7
    constants[17] = 0.4243
    constants[18] = 5.32
    constants[19] = 0.50417
    constants[20] = 0.0513
    constants[21] = 0.105
    constants[22] = 0.6
    constants[23] = 20.0
    constants[24] = 0.5
    constants[25] = 0.45
    constants[26] = 0.5
    constants[27] = 0.06
    constants[28] = 0.55783
    constants[29] = 0.18
    constants[30] = 0.7595
    constants[31] = 4.0
    constants[32] = 0.4287
    constants[33] = 28.6
    constants[34] = 5.30
    constants[35] = 0.1046
    constants[36] = 0.05557
    constants[37] = 0.0029658
    constants[38] = 0.00107
    constants[39] = 0.0632
    constants[40] = 20.0
    constants[41] = 5.0
    constants[42] = 0.1978
    constants[43] = 0.09314
    constants[44] = 0.04889
    constants[45] = 0.015
    constants[46] = 0.0524681
    constants[47] = 2.7
    constants[48] = 0.2202
    constants[49] = 0.089733
    constants[50] = 8.6
    constants[51] = 0.00325
    constants[52] = 10500
    constants[53] = 0.25
    constants[54] = 3.53
    constants[55] = 0.038089
    constants[56] = 1.0
    constants[57] = 9.92
    constants[58] = 0.0098394
    constants[59] = 0.050461
    constants[60] = 0.5
    constants[61] = 0.45
    constants[62] = 0.403
    constants[63] = 0.2514
    constants[64] = 2.73
    constants[65] = 6.2613
    constants[66] = 0.54682
    constants[67] = 0.008454
    constants[68] = 0.086124
    constants[69] = 0.22163
    constants[70] = 0.00021856
    constants[71] = 0.12862
    constants[72] = 0.035657
    constants[73] = 0.02073
    constants[74] = 0.0243
    constants[75] = 0.2457
    constants[76] = 2.7
    constants[77] = 0.0055
    constants[78] = 4.8
    constants[79] = 8.4568
    constants[80] = 0.0489
    constants[81] = 0.313
    constants[82] = 0.764818
    constants[83] = 0.0325
    constants[84] = 0.075
    constants[85] = 0.05
    constants[86] = 1
    constants[87] = 0.3
    constants[88] = 0.01532
    constants[89] = 0.0208
    constants[90] = 1.2
    constants[91] = 0.0001528
    constants[92] = 0.5
    constants[93] = 4.2
    constants[94] = 20.0
    constants[95] = 4.922e-5
    constants[96] = 1.0
    constants[97] = 1
    constants[98] = 200
    constants[99] = 83
    constants[100] = 440
    constants[101] = 4
    constants[102] = 2
    constants[103] = 62
    constants[104] = 1
    constants[105] = 0.012
    constants[106] = 300
    constants[107] = 4.59186
    constants[108] = 0.42
    constants[109] = 0.012
    constants[110] = 0.0236
    constants[111] = 35.0
    constants[112] = 0.22
    constants[113] = 0.22
    constants[114] = 5.0
    constants[115] = 5.0
    constants[116] = 2.379
    constants[117] = 0.92
    constants[118] = 2.22
    constants[119] = 0.46
    constants[120] = 0.43
    constants[121] = 0.064
    constants[122] = 2
    constants[123] = 0.041
    constants[124] = 2.55
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[4] = constants[19]*(states[27]/(states[27]+constants[18])-states[1]/(states[1]+constants[18]))
    algebraic[5] = constants[20]*states[9]*(states[1]/(states[1]+constants[21]))*(1.00000-1.00000/(1.00000+exp(-constants[23]*(1.00000*(states[2]-constants[22])))))
    rates[1] = algebraic[4]-algebraic[5]
    algebraic[6] = constants[24]*(states[2]/(states[2]+constants[26]))-constants[25]*(states[3]/(states[3]+constants[27]))
    rates[2] = algebraic[5]-algebraic[6]
    algebraic[7] = constants[28]*states[9]*(states[3]/(states[3]+constants[29]))*(power(1.00000+power(states[9]/constants[30], constants[31]), -1.00000))
    rates[3] = algebraic[6]-algebraic[7]
    algebraic[14] = constants[58]*(states[31]/(states[31]+constants[57])-states[14]/(states[14]+constants[57]))
    algebraic[13] = constants[56]*constants[55]*(states[27]/(states[27]+constants[54])-states[14]/(states[14]+constants[54]))
    algebraic[15] = constants[59]*states[22]*(states[14]/(states[14]+constants[21]))*(1.00000-1.00000/(1.00000+exp(-constants[23]*(1.00000*(states[15]-constants[22])))))
    rates[14] = (algebraic[14]+algebraic[13])-algebraic[15]
    algebraic[16] = constants[60]*(states[15]/(states[15]+constants[26]))-constants[61]*(states[16]/(states[16]+constants[27]))
    algebraic[17] = constants[62]*states[22]*(states[16]/(states[16]+constants[29]))*(power(1.00000+power(states[22]/constants[30], constants[31]), -1.00000))
    rates[16] = algebraic[16]-algebraic[17]
    algebraic[18] = constants[91]*(states[15]/(states[15]+constants[92]))*(1.00000-1.00000/(1.00000+exp(-constants[94]*(1.00000*(states[25]-constants[93])))))
    algebraic[20] = custom_piecewise([greater_equal(voi-(constants[100]+constants[98]+constants[99]) , 0.00000), 1.00000 , True, 0.00000])
    algebraic[22] = 1.00000+constants[97]*(constants[103]*constants[104]*(1.00000/(1.00000+exp(1.00000*-constants[101]*(voi-(constants[98]+constants[99])))))*(1.00000-algebraic[20]))
    algebraic[24] = constants[95]*(states[25]/(states[25]+constants[96]))*algebraic[22]
    rates[15] = (algebraic[15]+algebraic[24])-(algebraic[16]+algebraic[18])
    rates[25] = algebraic[18]-algebraic[24]
    algebraic[26] = constants[80]*(states[31]/(states[31]+constants[79])-states[27]/(states[27]+constants[79]))
    rates[27] = algebraic[26]-(algebraic[13]*(1.00000/constants[3])+algebraic[4]*(1.00000/constants[4]))
    algebraic[8] = constants[42]*(states[7]/(states[7]+constants[43])-states[28]/(states[28]+constants[43]))
    algebraic[19] = constants[68]*(states[20]/(states[20]+constants[69])-states[28]/(states[28]+constants[69]))
    algebraic[27] = constants[83]*(states[28]/(states[28]+constants[82])-states[32]/(states[32]+constants[82]))
    rates[28] = (algebraic[8]*(1.00000/constants[4])+algebraic[19]*(1.00000/constants[3]))-algebraic[27]
    algebraic[11] = (constants[52]/constants[53])*(constants[51]/constants[14])*((constants[13]/constants[14])*log(constants[15]/states[13])-constants[11])
    algebraic[12] = (constants[52]/constants[53])*constants[16]*states[22]*states[13]*(power(1.00000+states[22]/constants[17], -1.00000))
    algebraic[29] = constants[89]*(states[29]/(states[29]+constants[85]))
    rates[13] = (algebraic[11]+3.00000*algebraic[29])-3.00000*algebraic[12]
    algebraic[28] = constants[87]*((states[26]/(states[26]+constants[85]))*(states[22]/(states[22]+constants[88])))
    rates[26] = algebraic[29]-algebraic[28]
    algebraic[10] = (constants[48]/constants[12])*(constants[49]*(power(constants[50]/states[30]-1.00000, -1.00000/constants[47]))-states[11])
    algebraic[25] = (constants[75]/constants[53])*(constants[49]*(power(constants[50]/states[30]-1.00000, -1.00000/constants[76]))-states[24])
    algebraic[30] = constants[105]+(constants[97]*constants[105]*constants[108]*(1.00000/(1.00000+exp((1.00000*-constants[107])*(voi-((constants[98]+constants[102])-3.00000)))))-constants[97]*constants[105]*constants[108]*(1.00000/(1.00000+exp((1.00000*-constants[107])*(voi-(constants[98]+constants[106]+constants[102]+3.00000))))))
    algebraic[33] = 2.00000*(algebraic[30]/constants[77])*(constants[8]-states[30])
    rates[30] = algebraic[33]-(algebraic[10]*(1.00000/constants[5])+algebraic[25]*(1.00000/constants[6]))
    algebraic[34] = 2.00000*(algebraic[30]/constants[77])*(constants[78]-states[31])
    rates[31] = algebraic[34]-(algebraic[26]*(1.00000/constants[7])+algebraic[14]*(1.00000/constants[6]))
    algebraic[21] = constants[70]*(states[20]/(states[20]+constants[71])-states[32]/(states[32]+constants[71]))
    algebraic[35] = 2.00000*(algebraic[30]/constants[77])*(constants[81]-states[32])
    rates[32] = algebraic[35]+(algebraic[27]*(1.00000/constants[7])+algebraic[21]*(1.00000/constants[6]))
    algebraic[36] = constants[109]*((power(states[34]/constants[110], 2.00000)+constants[111]*(power(states[34]/constants[110], -0.500000))*(algebraic[30]/constants[110]))/(1.00000+constants[109]*constants[111]*(power(states[34]/constants[110], -0.500000))*(1.00000/constants[110])))
    rates[34] = algebraic[30]-algebraic[36]
    rates[35] = algebraic[30]*(constants[8]-states[30])-algebraic[36]*(states[35]/states[34])
    algebraic[0] = (constants[10]/constants[12])*(constants[9]/constants[14])*((constants[13]/constants[14])*log(constants[15]/states[0])-constants[11])
    algebraic[3] = (constants[10]/constants[12])*constants[16]*states[9]*states[0]*(power(1.00000+states[9]/constants[17], -1.00000))
    algebraic[31] = custom_piecewise([greater_equal(voi , constants[98]) & less_equal(voi , constants[98]+constants[106]), 1.00000 , True, 0.00000])
    algebraic[37] = constants[97]*(constants[123]+constants[124]*((voi-constants[98])/constants[122])*exp(-((voi-constants[98])*(algebraic[31]/constants[122]))))*algebraic[31]
    algebraic[39] = algebraic[37]
    rates[0] = (algebraic[0]+algebraic[39])-3.00000*algebraic[3]
    algebraic[38] = constants[112]-states[8]
    algebraic[40] = constants[34]*states[6]*states[8]-constants[35]*states[7]*algebraic[38]
    rates[7] = algebraic[40]-algebraic[8]
    algebraic[42] = algebraic[39]*constants[84]*constants[86]*(states[12]/(states[12]+constants[85]))
    rates[12] = algebraic[28]*(1.00000/constants[2])-algebraic[42]
    rates[29] = algebraic[42]*(1.00000/constants[4])-algebraic[29]*(1.00000/constants[3])
    algebraic[41] = constants[113]-states[21]
    algebraic[43] = constants[65]*states[19]*states[21]-constants[66]*states[20]*algebraic[41]
    rates[20] = algebraic[43]-(algebraic[19]+algebraic[21])
    algebraic[46] = (states[9]/2.00000)*(-constants[117]+power(power(constants[117], 2.00000)+4.00000*constants[117]*(constants[116]/states[9]-1.00000), 1.0/2))
    algebraic[47] = constants[32]*states[4]*algebraic[46]*(algebraic[38]/states[8])
    rates[4] = 2.00000*algebraic[7]-algebraic[47]
    algebraic[49] = constants[33]*states[5]*algebraic[46]
    rates[5] = algebraic[47]-algebraic[49]
    algebraic[50] = constants[36]*(states[11]/(states[11]+constants[37]))*(algebraic[46]/(algebraic[46]+constants[38]))*(states[6]/(states[6]+constants[39]))*(1.00000-1.00000/(1.00000+exp(-constants[41]*(1.00000*(states[9]/algebraic[46]-1.00000*constants[40])))))
    rates[6] = algebraic[49]-(algebraic[40]+algebraic[50])
    rates[8] = algebraic[47]-(algebraic[40]+algebraic[50])
    rates[11] = algebraic[10]-constants[1]*algebraic[50]
    algebraic[44] = constants[114]-states[10]
    algebraic[51] = constants[46]*states[10]*algebraic[46]-constants[45]*algebraic[44]*states[9]
    rates[10] = -algebraic[51]
    algebraic[9] = constants[44]*(states[9]/(states[9]+0.00100000))
    algebraic[53] = power(constants[117], 2.00000)+4.00000*constants[117]*(constants[116]/states[9]-1.00000)
    algebraic[55] = (constants[117]/2.00000+constants[117]*(constants[116]/(states[9]*(power(algebraic[53], 1.0/2)))))-(1.00000+0.500000*(power(algebraic[53], 1.0/2)))
    rates[9] = ((algebraic[47]+algebraic[49]+constants[0]*algebraic[50]+algebraic[51])-(algebraic[5]+algebraic[7]+algebraic[9]+algebraic[3]))*(power(1.00000-algebraic[55], -1.00000))
    algebraic[54] = (states[22]/2.00000)*(-constants[117]+power(power(constants[117], 2.00000)+4.00000*constants[117]*(constants[116]/states[22]-1.00000), 1.0/2))
    algebraic[56] = constants[63]*states[17]*algebraic[54]*(algebraic[41]/states[21])
    rates[17] = 2.00000*algebraic[17]-algebraic[56]
    algebraic[58] = constants[64]*states[18]*algebraic[54]
    rates[18] = algebraic[56]-algebraic[58]
    algebraic[59] = constants[67]*(states[24]/(states[24]+constants[37]))*(algebraic[54]/(algebraic[54]+constants[38]))*(states[19]/(states[19]+constants[39]))*(1.00000-1.00000/(1.00000+exp(1.00000*-constants[41]*(states[22]/algebraic[54]-1.00000*constants[40]))))
    rates[19] = algebraic[58]-(algebraic[43]+algebraic[59])
    rates[21] = algebraic[56]-(algebraic[43]+algebraic[59])
    rates[24] = algebraic[25]-constants[1]*algebraic[59]
    algebraic[45] = constants[115]-states[23]
    algebraic[60] = constants[74]*states[23]*algebraic[54]-constants[73]*algebraic[45]*states[22]
    rates[23] = -algebraic[60]
    algebraic[52] = 3.00000*algebraic[50]
    algebraic[32] = 2.00000*(algebraic[30]/constants[77])*(states[33]-constants[90])
    algebraic[61] = 3.00000*algebraic[59]
    rates[33] = (algebraic[52]*(1.00000/constants[5])+algebraic[61]*(1.00000/constants[6]))-algebraic[32]
    algebraic[23] = constants[72]*(states[22]/(states[22]+0.00100000))
    algebraic[62] = power(constants[117], 2.00000)+4.00000*constants[117]*(constants[116]/states[22]-1.00000)
    algebraic[63] = (constants[117]/2.00000+constants[117]*(constants[116]/(states[22]*(power(algebraic[62], 1.0/2)))))-(1.00000+0.500000*(power(algebraic[62], 1.0/2)))
    rates[22] = ((algebraic[56]+algebraic[58]+constants[0]*algebraic[59]+algebraic[60])-(algebraic[15]+algebraic[17]+algebraic[23]+algebraic[12]+algebraic[28]))*(power(1.00000-algebraic[63], -1.00000))
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[4] = constants[19]*(states[27]/(states[27]+constants[18])-states[1]/(states[1]+constants[18]))
    algebraic[5] = constants[20]*states[9]*(states[1]/(states[1]+constants[21]))*(1.00000-1.00000/(1.00000+exp(-constants[23]*(1.00000*(states[2]-constants[22])))))
    algebraic[6] = constants[24]*(states[2]/(states[2]+constants[26]))-constants[25]*(states[3]/(states[3]+constants[27]))
    algebraic[7] = constants[28]*states[9]*(states[3]/(states[3]+constants[29]))*(power(1.00000+power(states[9]/constants[30], constants[31]), -1.00000))
    algebraic[14] = constants[58]*(states[31]/(states[31]+constants[57])-states[14]/(states[14]+constants[57]))
    algebraic[13] = constants[56]*constants[55]*(states[27]/(states[27]+constants[54])-states[14]/(states[14]+constants[54]))
    algebraic[15] = constants[59]*states[22]*(states[14]/(states[14]+constants[21]))*(1.00000-1.00000/(1.00000+exp(-constants[23]*(1.00000*(states[15]-constants[22])))))
    algebraic[16] = constants[60]*(states[15]/(states[15]+constants[26]))-constants[61]*(states[16]/(states[16]+constants[27]))
    algebraic[17] = constants[62]*states[22]*(states[16]/(states[16]+constants[29]))*(power(1.00000+power(states[22]/constants[30], constants[31]), -1.00000))
    algebraic[18] = constants[91]*(states[15]/(states[15]+constants[92]))*(1.00000-1.00000/(1.00000+exp(-constants[94]*(1.00000*(states[25]-constants[93])))))
    algebraic[20] = custom_piecewise([greater_equal(voi-(constants[100]+constants[98]+constants[99]) , 0.00000), 1.00000 , True, 0.00000])
    algebraic[22] = 1.00000+constants[97]*(constants[103]*constants[104]*(1.00000/(1.00000+exp(1.00000*-constants[101]*(voi-(constants[98]+constants[99])))))*(1.00000-algebraic[20]))
    algebraic[24] = constants[95]*(states[25]/(states[25]+constants[96]))*algebraic[22]
    algebraic[26] = constants[80]*(states[31]/(states[31]+constants[79])-states[27]/(states[27]+constants[79]))
    algebraic[8] = constants[42]*(states[7]/(states[7]+constants[43])-states[28]/(states[28]+constants[43]))
    algebraic[19] = constants[68]*(states[20]/(states[20]+constants[69])-states[28]/(states[28]+constants[69]))
    algebraic[27] = constants[83]*(states[28]/(states[28]+constants[82])-states[32]/(states[32]+constants[82]))
    algebraic[11] = (constants[52]/constants[53])*(constants[51]/constants[14])*((constants[13]/constants[14])*log(constants[15]/states[13])-constants[11])
    algebraic[12] = (constants[52]/constants[53])*constants[16]*states[22]*states[13]*(power(1.00000+states[22]/constants[17], -1.00000))
    algebraic[29] = constants[89]*(states[29]/(states[29]+constants[85]))
    algebraic[28] = constants[87]*((states[26]/(states[26]+constants[85]))*(states[22]/(states[22]+constants[88])))
    algebraic[10] = (constants[48]/constants[12])*(constants[49]*(power(constants[50]/states[30]-1.00000, -1.00000/constants[47]))-states[11])
    algebraic[25] = (constants[75]/constants[53])*(constants[49]*(power(constants[50]/states[30]-1.00000, -1.00000/constants[76]))-states[24])
    algebraic[30] = constants[105]+(constants[97]*constants[105]*constants[108]*(1.00000/(1.00000+exp((1.00000*-constants[107])*(voi-((constants[98]+constants[102])-3.00000)))))-constants[97]*constants[105]*constants[108]*(1.00000/(1.00000+exp((1.00000*-constants[107])*(voi-(constants[98]+constants[106]+constants[102]+3.00000))))))
    algebraic[33] = 2.00000*(algebraic[30]/constants[77])*(constants[8]-states[30])
    algebraic[34] = 2.00000*(algebraic[30]/constants[77])*(constants[78]-states[31])
    algebraic[21] = constants[70]*(states[20]/(states[20]+constants[71])-states[32]/(states[32]+constants[71]))
    algebraic[35] = 2.00000*(algebraic[30]/constants[77])*(constants[81]-states[32])
    algebraic[36] = constants[109]*((power(states[34]/constants[110], 2.00000)+constants[111]*(power(states[34]/constants[110], -0.500000))*(algebraic[30]/constants[110]))/(1.00000+constants[109]*constants[111]*(power(states[34]/constants[110], -0.500000))*(1.00000/constants[110])))
    algebraic[0] = (constants[10]/constants[12])*(constants[9]/constants[14])*((constants[13]/constants[14])*log(constants[15]/states[0])-constants[11])
    algebraic[3] = (constants[10]/constants[12])*constants[16]*states[9]*states[0]*(power(1.00000+states[9]/constants[17], -1.00000))
    algebraic[31] = custom_piecewise([greater_equal(voi , constants[98]) & less_equal(voi , constants[98]+constants[106]), 1.00000 , True, 0.00000])
    algebraic[37] = constants[97]*(constants[123]+constants[124]*((voi-constants[98])/constants[122])*exp(-((voi-constants[98])*(algebraic[31]/constants[122]))))*algebraic[31]
    algebraic[39] = algebraic[37]
    algebraic[38] = constants[112]-states[8]
    algebraic[40] = constants[34]*states[6]*states[8]-constants[35]*states[7]*algebraic[38]
    algebraic[42] = algebraic[39]*constants[84]*constants[86]*(states[12]/(states[12]+constants[85]))
    algebraic[41] = constants[113]-states[21]
    algebraic[43] = constants[65]*states[19]*states[21]-constants[66]*states[20]*algebraic[41]
    algebraic[46] = (states[9]/2.00000)*(-constants[117]+power(power(constants[117], 2.00000)+4.00000*constants[117]*(constants[116]/states[9]-1.00000), 1.0/2))
    algebraic[47] = constants[32]*states[4]*algebraic[46]*(algebraic[38]/states[8])
    algebraic[49] = constants[33]*states[5]*algebraic[46]
    algebraic[50] = constants[36]*(states[11]/(states[11]+constants[37]))*(algebraic[46]/(algebraic[46]+constants[38]))*(states[6]/(states[6]+constants[39]))*(1.00000-1.00000/(1.00000+exp(-constants[41]*(1.00000*(states[9]/algebraic[46]-1.00000*constants[40])))))
    algebraic[44] = constants[114]-states[10]
    algebraic[51] = constants[46]*states[10]*algebraic[46]-constants[45]*algebraic[44]*states[9]
    algebraic[9] = constants[44]*(states[9]/(states[9]+0.00100000))
    algebraic[53] = power(constants[117], 2.00000)+4.00000*constants[117]*(constants[116]/states[9]-1.00000)
    algebraic[55] = (constants[117]/2.00000+constants[117]*(constants[116]/(states[9]*(power(algebraic[53], 1.0/2)))))-(1.00000+0.500000*(power(algebraic[53], 1.0/2)))
    algebraic[54] = (states[22]/2.00000)*(-constants[117]+power(power(constants[117], 2.00000)+4.00000*constants[117]*(constants[116]/states[22]-1.00000), 1.0/2))
    algebraic[56] = constants[63]*states[17]*algebraic[54]*(algebraic[41]/states[21])
    algebraic[58] = constants[64]*states[18]*algebraic[54]
    algebraic[59] = constants[67]*(states[24]/(states[24]+constants[37]))*(algebraic[54]/(algebraic[54]+constants[38]))*(states[19]/(states[19]+constants[39]))*(1.00000-1.00000/(1.00000+exp(1.00000*-constants[41]*(states[22]/algebraic[54]-1.00000*constants[40]))))
    algebraic[45] = constants[115]-states[23]
    algebraic[60] = constants[74]*states[23]*algebraic[54]-constants[73]*algebraic[45]*states[22]
    algebraic[52] = 3.00000*algebraic[50]
    algebraic[32] = 2.00000*(algebraic[30]/constants[77])*(states[33]-constants[90])
    algebraic[61] = 3.00000*algebraic[59]
    algebraic[23] = constants[72]*(states[22]/(states[22]+0.00100000))
    algebraic[62] = power(constants[117], 2.00000)+4.00000*constants[117]*(constants[116]/states[22]-1.00000)
    algebraic[63] = (constants[117]/2.00000+constants[117]*(constants[116]/(states[22]*(power(algebraic[62], 1.0/2)))))-(1.00000+0.500000*(power(algebraic[62], 1.0/2)))
    algebraic[1] = constants[110]*((constants[118]+constants[119])*(1.00000-states[35]/constants[121])-(constants[119]+constants[120])*(1.00000-states[34]/constants[110]))
    algebraic[2] = custom_piecewise([greater_equal(voi-(constants[106]+constants[98]) , 0.00000), 1.00000 , True, 0.00000])
    algebraic[48] = constants[116]-(states[9]+algebraic[46])
    algebraic[57] = constants[116]-(states[22]+algebraic[54])
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
        self.nOP = 15.0
        self.NAero = 3.0
        self.Rng = 1.8
        self.Reg = 0.8
        self.Ren = 0.4444444444444444
        self.Rcn = 0.01222
        self.Rcg = 0.022
        self.Rce = 0.0275
        self.O2a = 8.34
        self.gn_NA = 0.0039
        self.Sm_n = 40500
        self.Vm = -70
        self.Vn = 0.45
        self.RT = 2577340
        self.F = 96500
        self.NAe = 150.0
        self.kpump = 3.17e-7
        self.Km_pump = 0.4243
        self.Km_en_GLC = 5.32
        self.Vm_en_GLC = 0.50417
        self.Vmax_n_hk = 0.0513
        self.Km_GLC = 0.105
        self.G6P_inh_hk = 0.6
        self.aG6P_inh_hk = 20.0
        self.Vmaxf_n_pgi = 0.5
        self.Vmaxr_n_pgi = 0.45
        self.Km_G6P = 0.5
        self.Km_F6P_pgi = 0.06
        self.kn_pfk = 0.55783
        self.Km_F6P_pfk = 0.18
        self.Ki_ATP = 0.7595
        self.nH = 4.0
        self.kn_pgk = 0.4287
        self.kn_pk = 28.6
        self.kfn_ldh = 5.30
        self.krn_ldh = 0.1046
        self.Vmax_n_mito = 0.05557
        self.Km_O2 = 0.0029658
        self.Km_ADP = 0.00107
        self.Km_PYR = 0.0632
        self.rATP_mito = 20.0
        self.aATP_mito = 5.0
        self.Vmax_ne_LAC = 0.1978
        self.Km_ne_LAC = 0.09314
        self.Vmax_n_ATPase = 0.04889
        self.krn_ck = 0.015
        self.kfn_ck = 0.0524681
        self.nh_O2 = 2.7
        self.PScapn = 0.2202
        self.Ko2 = 0.089733
        self.HbOP = 8.6
        self.gg_NA = 0.00325
        self.Sm_g = 10500
        self.Vg = 0.25
        self.Km_eg_GLC = 3.53
        self.Vm_eg_GLC = 0.038089
        self.KO1 = 1.0
        self.Km_cg_GLC = 9.92
        self.Vm_cg_GLC = 0.0098394
        self.Vmax_g_hk = 0.050461
        self.Vmaxf_g_pgi = 0.5
        self.Vmaxr_g_pgi = 0.45
        self.kg_pfk = 0.403
        self.kg_pgk = 0.2514
        self.kg_pk = 2.73
        self.kfg_ldh = 6.2613
        self.krg_ldh = 0.54682
        self.Vmax_g_mito = 0.008454
        self.Vmax_ge_LAC = 0.086124
        self.Km_ge_LAC = 0.22163
        self.Vmax_gc_LAC = 0.00021856
        self.Km_gc_LAC = 0.12862
        self.Vmax_g_ATPase = 0.035657
        self.krg_ck = 0.02073
        self.kfg_ck = 0.0243
        self.PScapg = 0.2457
        self.nh_O2_1 = 2.7
        self.Vc = 0.0055
        self.GLCa = 4.8
        self.Km_ce_GLC = 8.4568
        self.Vm_ce_GLC = 0.0489
        self.LACa = 0.313
        self.Km_ec_LAC = 0.764818
        self.Vm_ec_LAC = 0.0325
        self.R_GLU_NA = 0.075
        self.Km_GLU = 0.05
        self.KO2 = 1
        self.Vmax_g_gs = 0.3
        self.Km_ATP = 0.01532
        self.Vmax_eg_GLU = 0.0208
        self.CO2a = 1.2
        self.Vmax_glys = 0.0001528
        self.Km_G6P_glys = 0.5
        self.GLY_inh = 4.2
        self.aGLY_inh = 20.0
        self.Vmax_glyp = 4.922e-5
        self.Km_GLY = 1.0
        self.stim = 1
        self.to = 200
        self.to_GLY = 83
        self.tend_GLY = 440
        self.sr_GLY = 4
        self.t1 = 2
        self.delta_GLY = 62
        self.KO3 = 1
        self.CBF0 = 0.012
        self.tend = 300
        self.sr = 4.59186
        self.deltaf = 0.42
        self.CBF0_1 = 0.012
        self.Vv0 = 0.0236
        self.tv = 35.0
        self.NADH_n_tot = 0.22
        self.NADH_g_tot = 0.22
        self.PCrn_tot = 5.0
        self.PCrg_tot = 5.0
        self.ATPtot = 2.379
        self.qak = 0.92
        self.k1 = 2.22
        self.k2 = 0.46
        self.k3 = 0.43
        self.dHb0 = 0.064
        self.t_n_stim = 2
        self.v1_n = 0.041
        self.v2_n = 2.55

    def to_dict(self):
        return {
            "nOP": self.nOP,
            "NAero": self.NAero,
            "Rng": self.Rng,
            "Reg": self.Reg,
            "Ren": self.Ren,
            "Rcn": self.Rcn,
            "Rcg": self.Rcg,
            "Rce": self.Rce,
            "O2a": self.O2a,
            "gn_NA": self.gn_NA,
            "Sm_n": self.Sm_n,
            "Vm": self.Vm,
            "Vn": self.Vn,
            "RT": self.RT,
            "F": self.F,
            "NAe": self.NAe,
            "kpump": self.kpump,
            "Km_pump": self.Km_pump,
            "Km_en_GLC": self.Km_en_GLC,
            "Vm_en_GLC": self.Vm_en_GLC,
            "Vmax_n_hk": self.Vmax_n_hk,
            "Km_GLC": self.Km_GLC,
            "G6P_inh_hk": self.G6P_inh_hk,
            "aG6P_inh_hk": self.aG6P_inh_hk,
            "Vmaxf_n_pgi": self.Vmaxf_n_pgi,
            "Vmaxr_n_pgi": self.Vmaxr_n_pgi,
            "Km_G6P": self.Km_G6P,
            "Km_F6P_pgi": self.Km_F6P_pgi,
            "kn_pfk": self.kn_pfk,
            "Km_F6P_pfk": self.Km_F6P_pfk,
            "Ki_ATP": self.Ki_ATP,
            "nH": self.nH,
            "kn_pgk": self.kn_pgk,
            "kn_pk": self.kn_pk,
            "kfn_ldh": self.kfn_ldh,
            "krn_ldh": self.krn_ldh,
            "Vmax_n_mito": self.Vmax_n_mito,
            "Km_O2": self.Km_O2,
            "Km_ADP": self.Km_ADP,
            "Km_PYR": self.Km_PYR,
            "rATP_mito": self.rATP_mito,
            "aATP_mito": self.aATP_mito,
            "Vmax_ne_LAC": self.Vmax_ne_LAC,
            "Km_ne_LAC": self.Km_ne_LAC,
            "Vmax_n_ATPase": self.Vmax_n_ATPase,
            "krn_ck": self.krn_ck,
            "kfn_ck": self.kfn_ck,
            "nh_O2": self.nh_O2,
            "PScapn": self.PScapn,
            "Ko2": self.Ko2,
            "HbOP": self.HbOP,
            "gg_NA": self.gg_NA,
            "Sm_g": self.Sm_g,
            "Vg": self.Vg,
            "Km_eg_GLC": self.Km_eg_GLC,
            "Vm_eg_GLC": self.Vm_eg_GLC,
            "KO1": self.KO1,
            "Km_cg_GLC": self.Km_cg_GLC,
            "Vm_cg_GLC": self.Vm_cg_GLC,
            "Vmax_g_hk": self.Vmax_g_hk,
            "Vmaxf_g_pgi": self.Vmaxf_g_pgi,
            "Vmaxr_g_pgi": self.Vmaxr_g_pgi,
            "kg_pfk": self.kg_pfk,
            "kg_pgk": self.kg_pgk,
            "kg_pk": self.kg_pk,
            "kfg_ldh": self.kfg_ldh,
            "krg_ldh": self.krg_ldh,
            "Vmax_g_mito": self.Vmax_g_mito,
            "Vmax_ge_LAC": self.Vmax_ge_LAC,
            "Km_ge_LAC": self.Km_ge_LAC,
            "Vmax_gc_LAC": self.Vmax_gc_LAC,
            "Km_gc_LAC": self.Km_gc_LAC,
            "Vmax_g_ATPase": self.Vmax_g_ATPase,
            "krg_ck": self.krg_ck,
            "kfg_ck": self.kfg_ck,
            "PScapg": self.PScapg,
            "nh_O2_1": self.nh_O2_1,
            "Vc": self.Vc,
            "GLCa": self.GLCa,
            "Km_ce_GLC": self.Km_ce_GLC,
            "Vm_ce_GLC": self.Vm_ce_GLC,
            "LACa": self.LACa,
            "Km_ec_LAC": self.Km_ec_LAC,
            "Vm_ec_LAC": self.Vm_ec_LAC,
            "R_GLU_NA": self.R_GLU_NA,
            "Km_GLU": self.Km_GLU,
            "KO2": self.KO2,
            "Vmax_g_gs": self.Vmax_g_gs,
            "Km_ATP": self.Km_ATP,
            "Vmax_eg_GLU": self.Vmax_eg_GLU,
            "CO2a": self.CO2a,
            "Vmax_glys": self.Vmax_glys,
            "Km_G6P_glys": self.Km_G6P_glys,
            "GLY_inh": self.GLY_inh,
            "aGLY_inh": self.aGLY_inh,
            "Vmax_glyp": self.Vmax_glyp,
            "Km_GLY": self.Km_GLY,
            "stim": self.stim,
            "to": self.to,
            "to_GLY": self.to_GLY,
            "tend_GLY": self.tend_GLY,
            "sr_GLY": self.sr_GLY,
            "t1": self.t1,
            "delta_GLY": self.delta_GLY,
            "KO3": self.KO3,
            "CBF0": self.CBF0,
            "tend": self.tend,
            "sr": self.sr,
            "deltaf": self.deltaf,
            "CBF0_1": self.CBF0_1,
            "Vv0": self.Vv0,
            "tv": self.tv,
            "NADH_n_tot": self.NADH_n_tot,
            "NADH_g_tot": self.NADH_g_tot,
            "PCrn_tot": self.PCrn_tot,
            "PCrg_tot": self.PCrg_tot,
            "ATPtot": self.ATPtot,
            "qak": self.qak,
            "k1": self.k1,
            "k2": self.k2,
            "k3": self.k3,
            "dHb0": self.dHb0,
            "t_n_stim": self.t_n_stim,
            "v1_n": self.v1_n,
            "v2_n": self.v2_n,
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
        y0=[15.533, 0.2633, 0.7275, 0.1091, 0.0418, 0.0037, 0.0388, 0.3856, 0.0319, 2.2592, 4.2529, 0.0975, 3.0, 13.36, 0.1656, 0.7326, 0.1116, 0.0698, 0.0254, 0.1711, 0.4651, 0.0445, 2.24, 4.6817, 0.1589, 2.5, 0.0, 0.3339, 0.3986, 0.0, 7.4201, 4.6401, 0.3251, 2.12, 0.0237, 0.0218],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "cloutier_2009"
        self.curve_names = [
            "NAn",
            "GLCn",
            "G6Pn",
            "F6Pn",
            "GAPn",
            "PEPn",
            "PYRn",
            "LACn",
            "NADHn",
            "ATPn",
            "PCrn",
            "O2n",
            "GLUn",
            "NAg",
            "GLCg",
            "G6Pg",
            "F6Pg",
            "GAPg",
            "PEPg",
            "PYRg",
            "LACg",
            "NADHg",
            "ATPg",
            "PCrg",
            "O2g",
            "GLYg",
            "GLUg",
            "GLCe",
            "LACe",
            "GLUe",
            "O2c",
            "GLCc",
            "LACc",
            "CO2c",
            "Vv",
            "dHb",
        ]
        self.state_names = ['NAn', 'GLCn', 'G6Pn', 'F6Pn', 'GAPn', 'PEPn', 'PYRn', 'LACn', 'NADHn', 'ATPn', 'PCrn', 'O2n', 'GLUn', 'NAg', 'GLCg', 'G6Pg', 'F6Pg', 'GAPg', 'PEPg', 'PYRg', 'LACg', 'NADHg', 'ATPg', 'PCrg', 'O2g', 'GLYg', 'GLUg', 'GLCe', 'LACe', 'GLUe', 'O2c', 'GLCc', 'LACc', 'CO2c', 'Vv', 'dHb']
        self.algebraic_names = ['Vn_leak_Na', 'BOLD', 'unitstepSB', 'Vn_pump', 'V_en_GLC', 'Vn_hk', 'Vn_pgi', 'Vn_pfk', 'Vne_LAC', 'Vn_ATPase', 'Vcn_O2', 'Vg_leak_Na', 'Vg_pump', 'Veg_GLC', 'Vcg_GLC', 'Vg_hk', 'Vg_pgi', 'Vg_pfk', 'Vg_glys', 'Vge_LAC', 'unitstepSB2', 'Vgc_LAC', 'deltaVt_GLY', 'Vg_ATPase', 'Vg_glyp', 'Vcg_O2', 'Vce_GLC', 'Vec_LAC', 'Vg_gs', 'Veg_GLU', 'Fin_t', 'unitpulseSB', 'Vc_CO2', 'Vc_O2', 'Vc_GLC', 'Vc_LAC', 'Fout_t', 'v_stim', 'NADn', 'Vn_stim', 'Vn_ldh', 'NADg', 'Vn_stim_GLU', 'Vg_ldh', 'CRn', 'CRg', 'ADPn', 'Vn_pgk', 'AMPn', 'Vn_pk', 'Vn_mito', 'Vn_ck', 'Vnc_CO2', 'u_n', 'ADPg', 'dAMP_dATPn', 'Vg_pgk', 'AMPg', 'Vg_pk', 'Vg_mito', 'Vg_ck', 'Vgc_CO2', 'u_g', 'dAMP_dATPg']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 125
        p = self.params

        # direct mapping
        c[0] = p.nOP
        c[1] = p.NAero
        c[2] = p.Rng
        c[3] = p.Reg
        c[4] = p.Ren
        c[5] = p.Rcn
        c[6] = p.Rcg
        c[7] = p.Rce
        c[8] = p.O2a
        c[9] = p.gn_NA
        c[10] = p.Sm_n
        c[11] = p.Vm
        c[12] = p.Vn
        c[13] = p.RT
        c[14] = p.F
        c[15] = p.NAe
        c[16] = p.kpump
        c[17] = p.Km_pump
        c[18] = p.Km_en_GLC
        c[19] = p.Vm_en_GLC
        c[20] = p.Vmax_n_hk
        c[21] = p.Km_GLC
        c[22] = p.G6P_inh_hk
        c[23] = p.aG6P_inh_hk
        c[24] = p.Vmaxf_n_pgi
        c[25] = p.Vmaxr_n_pgi
        c[26] = p.Km_G6P
        c[27] = p.Km_F6P_pgi
        c[28] = p.kn_pfk
        c[29] = p.Km_F6P_pfk
        c[30] = p.Ki_ATP
        c[31] = p.nH
        c[32] = p.kn_pgk
        c[33] = p.kn_pk
        c[34] = p.kfn_ldh
        c[35] = p.krn_ldh
        c[36] = p.Vmax_n_mito
        c[37] = p.Km_O2
        c[38] = p.Km_ADP
        c[39] = p.Km_PYR
        c[40] = p.rATP_mito
        c[41] = p.aATP_mito
        c[42] = p.Vmax_ne_LAC
        c[43] = p.Km_ne_LAC
        c[44] = p.Vmax_n_ATPase
        c[45] = p.krn_ck
        c[46] = p.kfn_ck
        c[47] = p.nh_O2
        c[48] = p.PScapn
        c[49] = p.Ko2
        c[50] = p.HbOP
        c[51] = p.gg_NA
        c[52] = p.Sm_g
        c[53] = p.Vg
        c[54] = p.Km_eg_GLC
        c[55] = p.Vm_eg_GLC
        c[56] = p.KO1
        c[57] = p.Km_cg_GLC
        c[58] = p.Vm_cg_GLC
        c[59] = p.Vmax_g_hk
        c[60] = p.Vmaxf_g_pgi
        c[61] = p.Vmaxr_g_pgi
        c[62] = p.kg_pfk
        c[63] = p.kg_pgk
        c[64] = p.kg_pk
        c[65] = p.kfg_ldh
        c[66] = p.krg_ldh
        c[67] = p.Vmax_g_mito
        c[68] = p.Vmax_ge_LAC
        c[69] = p.Km_ge_LAC
        c[70] = p.Vmax_gc_LAC
        c[71] = p.Km_gc_LAC
        c[72] = p.Vmax_g_ATPase
        c[73] = p.krg_ck
        c[74] = p.kfg_ck
        c[75] = p.PScapg
        c[76] = p.nh_O2_1
        c[77] = p.Vc
        c[78] = p.GLCa
        c[79] = p.Km_ce_GLC
        c[80] = p.Vm_ce_GLC
        c[81] = p.LACa
        c[82] = p.Km_ec_LAC
        c[83] = p.Vm_ec_LAC
        c[84] = p.R_GLU_NA
        c[85] = p.Km_GLU
        c[86] = p.KO2
        c[87] = p.Vmax_g_gs
        c[88] = p.Km_ATP
        c[89] = p.Vmax_eg_GLU
        c[90] = p.CO2a
        c[91] = p.Vmax_glys
        c[92] = p.Km_G6P_glys
        c[93] = p.GLY_inh
        c[94] = p.aGLY_inh
        c[95] = p.Vmax_glyp
        c[96] = p.Km_GLY
        c[97] = p.stim
        c[98] = p.to
        c[99] = p.to_GLY
        c[100] = p.tend_GLY
        c[101] = p.sr_GLY
        c[102] = p.t1
        c[103] = p.delta_GLY
        c[104] = p.KO3
        c[105] = p.CBF0
        c[106] = p.tend
        c[107] = p.sr
        c[108] = p.deltaf
        c[109] = p.CBF0_1
        c[110] = p.Vv0
        c[111] = p.tv
        c[112] = p.NADH_n_tot
        c[113] = p.NADH_g_tot
        c[114] = p.PCrn_tot
        c[115] = p.PCrg_tot
        c[116] = p.ATPtot
        c[117] = p.qak
        c[118] = p.k1
        c[119] = p.k2
        c[120] = p.k3
        c[121] = p.dHb0
        c[122] = p.t_n_stim
        c[123] = p.v1_n
        c[124] = p.v2_n

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
