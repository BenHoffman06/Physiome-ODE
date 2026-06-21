# Size of variable arrays:
sizeAlgebraic = 34
sizeStates = 15
sizeConstants = 59
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (second)"
    legend_algebraic[0] = "L_iso in component beta_1_adrenergic_parameters (uM)"
    legend_constants[0] = "K_H in component beta_1_adrenergic_parameters (uM)"
    legend_constants[1] = "K_L in component beta_1_adrenergic_parameters (uM)"
    legend_constants[2] = "K_C in component beta_1_adrenergic_parameters (uM)"
    legend_algebraic[1] = "L_ach in component muscarinic_parameters (uM)"
    legend_constants[3] = "K_H in component muscarinic_parameters (uM)"
    legend_constants[4] = "K_L in component muscarinic_parameters (uM)"
    legend_constants[5] = "K_C in component muscarinic_parameters (uM)"
    legend_constants[6] = "k_PDE2 in component PDE_parameters (per_sec)"
    legend_constants[7] = "Km_PDE2 in component PDE_parameters (uM)"
    legend_constants[8] = "k_PDE3 in component PDE_parameters (per_sec)"
    legend_constants[9] = "Km_PDE3 in component PDE_parameters (uM)"
    legend_constants[10] = "k_PDE4 in component PDE_parameters (per_sec)"
    legend_constants[11] = "Km_PDE4 in component PDE_parameters (uM)"
    legend_constants[12] = "k_act1 in component G_s_parameters (per_sec)"
    legend_constants[13] = "k_act2 in component G_s_parameters (per_sec)"
    legend_constants[14] = "k_hydr in component G_s_parameters (per_sec)"
    legend_constants[15] = "k_reas in component G_s_parameters (per_uM_per_sec)"
    legend_constants[16] = "k_act1 in component G_i_parameters (per_sec)"
    legend_constants[17] = "k_act2 in component G_i_parameters (per_sec)"
    legend_constants[18] = "k_hydr in component G_i_parameters (per_sec)"
    legend_constants[19] = "k_reas in component G_i_parameters (per_uM_per_sec)"
    legend_algebraic[12] = "R in component caveolar_beta_1_adrenergic_receptor_module (uM)"
    legend_algebraic[13] = "LR in component caveolar_beta_1_adrenergic_receptor_module (uM)"
    legend_algebraic[14] = "LRG in component caveolar_beta_1_adrenergic_receptor_module (uM)"
    legend_algebraic[15] = "RG in component caveolar_beta_1_adrenergic_receptor_module (uM)"
    legend_constants[20] = "R_Total in component caveolar_beta_1_adrenergic_receptor_module (uM)"
    legend_algebraic[5] = "Gs_alpha_beta_gamma in component caveolar_G_s_protein_activation_module (uM)"
    legend_algebraic[16] = "R in component caveolar_muscarinic_receptor_module (uM)"
    legend_algebraic[17] = "LR in component caveolar_muscarinic_receptor_module (uM)"
    legend_algebraic[18] = "LRG in component caveolar_muscarinic_receptor_module (uM)"
    legend_algebraic[19] = "RG in component caveolar_muscarinic_receptor_module (uM)"
    legend_constants[21] = "R_Total in component caveolar_muscarinic_receptor_module (uM)"
    legend_algebraic[6] = "Gi_alpha_beta_gamma in component caveolar_G_i_protein_activation_module (uM)"
    legend_states[0] = "Gs_alpha_GTP in component caveolar_G_s_protein_activation_module (uM)"
    legend_states[1] = "Gs_beta_gamma in component caveolar_G_s_protein_activation_module (uM)"
    legend_states[2] = "Gs_alpha_GDP in component caveolar_G_s_protein_activation_module (uM)"
    legend_constants[22] = "Gs_Total in component caveolar_G_s_protein_activation_module (uM)"
    legend_states[3] = "Gi_alpha_GTP in component caveolar_G_i_protein_activation_module (uM)"
    legend_states[4] = "Gi_beta_gamma in component caveolar_G_i_protein_activation_module (uM)"
    legend_states[5] = "Gi_alpha_GDP in component caveolar_G_i_protein_activation_module (uM)"
    legend_constants[23] = "Gi_Total in component caveolar_G_i_protein_activation_module (uM)"
    legend_algebraic[20] = "R in component extracaveolar_beta_1_adrenergic_receptor_module (uM)"
    legend_algebraic[21] = "LR in component extracaveolar_beta_1_adrenergic_receptor_module (uM)"
    legend_algebraic[22] = "LRG in component extracaveolar_beta_1_adrenergic_receptor_module (uM)"
    legend_algebraic[23] = "RG in component extracaveolar_beta_1_adrenergic_receptor_module (uM)"
    legend_constants[24] = "R_Total in component extracaveolar_beta_1_adrenergic_receptor_module (uM)"
    legend_algebraic[7] = "Gs_alpha_beta_gamma in component extracaveolar_G_s_protein_activation_module (uM)"
    legend_algebraic[24] = "R in component extracaveolar_muscarinic_receptor_module (uM)"
    legend_algebraic[25] = "LR in component extracaveolar_muscarinic_receptor_module (uM)"
    legend_algebraic[26] = "LRG in component extracaveolar_muscarinic_receptor_module (uM)"
    legend_algebraic[27] = "RG in component extracaveolar_muscarinic_receptor_module (uM)"
    legend_constants[25] = "R_Total in component extracaveolar_muscarinic_receptor_module (uM)"
    legend_algebraic[8] = "Gi_alpha_beta_gamma in component extracaveolar_G_i_protein_activation_module (uM)"
    legend_states[6] = "Gs_alpha_GTP in component extracaveolar_G_s_protein_activation_module (uM)"
    legend_states[7] = "Gs_beta_gamma in component extracaveolar_G_s_protein_activation_module (uM)"
    legend_states[8] = "Gs_alpha_GDP in component extracaveolar_G_s_protein_activation_module (uM)"
    legend_constants[26] = "Gs_Total in component extracaveolar_G_s_protein_activation_module (uM)"
    legend_states[9] = "Gi_alpha_GTP in component extracaveolar_G_i_protein_activation_module (uM)"
    legend_states[10] = "Gi_beta_gamma in component extracaveolar_G_i_protein_activation_module (uM)"
    legend_states[11] = "Gi_alpha_GDP in component extracaveolar_G_i_protein_activation_module (uM)"
    legend_constants[27] = "Gi_Total in component extracaveolar_G_i_protein_activation_module (uM)"
    legend_algebraic[9] = "dcAMP_AC_56_dt in component AC56_module (uM_per_sec)"
    legend_algebraic[2] = "k_AC56 in component AC56_module (per_sec)"
    legend_constants[28] = "AC_56 in component AC56_module (uM)"
    legend_constants[29] = "AF56 in component AC56_module (dimensionless)"
    legend_constants[30] = "MW_AC56 in component AC56_module (kDa)"
    legend_constants[31] = "ATP in component AC56_module (uM)"
    legend_constants[32] = "Km_ATP in component AC56_module (uM)"
    legend_algebraic[10] = "dcAMP_AC_47_ecav_dt in component AC47_ecav_module (uM_per_sec)"
    legend_algebraic[3] = "k_AC47_ecav in component AC47_ecav_module (per_sec)"
    legend_constants[33] = "AC_47_ecav in component AC47_ecav_module (uM)"
    legend_constants[34] = "AF47 in component AC47_ecav_module (dimensionless)"
    legend_constants[35] = "MW_AC47 in component AC47_ecav_module (kDa)"
    legend_constants[36] = "ATP in component AC47_ecav_module (uM)"
    legend_constants[37] = "Km_ATP in component AC47_ecav_module (uM)"
    legend_constants[55] = "dcAMP_AC_47_cyt_dt in component AC47_cyt_module (uM_per_sec)"
    legend_constants[38] = "k_AC47_cyt in component AC47_cyt_module (per_sec)"
    legend_constants[39] = "AC_47_cyt in component AC47_cyt_module (uM)"
    legend_constants[40] = "AF47 in component AC47_cyt_module (dimensionless)"
    legend_constants[41] = "ATP in component AC47_cyt_module (uM)"
    legend_constants[42] = "Km_ATP in component AC47_cyt_module (uM)"
    legend_algebraic[28] = "dcAMP_cav_PDE2_dt in component caveolar_PDE_module (uM_per_sec)"
    legend_algebraic[31] = "dcAMP_cav_PDE3_dt in component caveolar_PDE_module (uM_per_sec)"
    legend_algebraic[33] = "dcAMP_cav_PDE4_dt in component caveolar_PDE_module (uM_per_sec)"
    legend_states[12] = "cAMP_cav in component cAMP_flux_module (uM)"
    legend_constants[43] = "PDE2 in component caveolar_PDE_module (uM)"
    legend_constants[44] = "PDE3 in component caveolar_PDE_module (uM)"
    legend_constants[45] = "PDE4 in component caveolar_PDE_module (uM)"
    legend_algebraic[29] = "dcAMP_ecav_PDE2_dt in component extracaveolar_PDE_module (uM_per_sec)"
    legend_algebraic[32] = "dcAMP_ecav_PDE4_dt in component extracaveolar_PDE_module (uM_per_sec)"
    legend_states[13] = "cAMP_ecav in component cAMP_flux_module (uM)"
    legend_constants[46] = "PDE2 in component extracaveolar_PDE_module (uM)"
    legend_constants[47] = "PDE4 in component extracaveolar_PDE_module (uM)"
    legend_algebraic[4] = "dcAMP_cyt_PDE2_dt in component bulk_cytoplasmic_PDE_module (uM_per_sec)"
    legend_algebraic[11] = "dcAMP_cyt_PDE3_dt in component bulk_cytoplasmic_PDE_module (uM_per_sec)"
    legend_algebraic[30] = "dcAMP_cyt_PDE4_dt in component bulk_cytoplasmic_PDE_module (uM_per_sec)"
    legend_states[14] = "cAMP_cyt in component cAMP_flux_module (uM)"
    legend_constants[48] = "PDE2 in component bulk_cytoplasmic_PDE_module (uM)"
    legend_constants[49] = "PDE3 in component bulk_cytoplasmic_PDE_module (uM)"
    legend_constants[50] = "PDE4 in component bulk_cytoplasmic_PDE_module (uM)"
    legend_constants[56] = "V_cav in component cAMP_flux_module (liter)"
    legend_constants[57] = "V_ecav in component cAMP_flux_module (liter)"
    legend_constants[58] = "V_cyt in component cAMP_flux_module (liter)"
    legend_constants[51] = "V_cell in component cAMP_flux_module (liter)"
    legend_constants[52] = "J_cav_ecav in component cAMP_flux_module (liters_per_second)"
    legend_constants[53] = "J_cav_cyt in component cAMP_flux_module (liters_per_second)"
    legend_constants[54] = "J_ecav_cyt in component cAMP_flux_module (liters_per_second)"
    legend_rates[0] = "d/dt Gs_alpha_GTP in component caveolar_G_s_protein_activation_module (uM)"
    legend_rates[1] = "d/dt Gs_beta_gamma in component caveolar_G_s_protein_activation_module (uM)"
    legend_rates[2] = "d/dt Gs_alpha_GDP in component caveolar_G_s_protein_activation_module (uM)"
    legend_rates[3] = "d/dt Gi_alpha_GTP in component caveolar_G_i_protein_activation_module (uM)"
    legend_rates[4] = "d/dt Gi_beta_gamma in component caveolar_G_i_protein_activation_module (uM)"
    legend_rates[5] = "d/dt Gi_alpha_GDP in component caveolar_G_i_protein_activation_module (uM)"
    legend_rates[6] = "d/dt Gs_alpha_GTP in component extracaveolar_G_s_protein_activation_module (uM)"
    legend_rates[7] = "d/dt Gs_beta_gamma in component extracaveolar_G_s_protein_activation_module (uM)"
    legend_rates[8] = "d/dt Gs_alpha_GDP in component extracaveolar_G_s_protein_activation_module (uM)"
    legend_rates[9] = "d/dt Gi_alpha_GTP in component extracaveolar_G_i_protein_activation_module (uM)"
    legend_rates[10] = "d/dt Gi_beta_gamma in component extracaveolar_G_i_protein_activation_module (uM)"
    legend_rates[11] = "d/dt Gi_alpha_GDP in component extracaveolar_G_i_protein_activation_module (uM)"
    legend_rates[12] = "d/dt cAMP_cav in component cAMP_flux_module (uM)"
    legend_rates[13] = "d/dt cAMP_ecav in component cAMP_flux_module (uM)"
    legend_rates[14] = "d/dt cAMP_cyt in component cAMP_flux_module (uM)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    constants[0] = 0.035
    constants[1] = 0.386
    constants[2] = 8.809
    constants[3] = 0.16
    constants[4] = 11
    constants[5] = 30
    constants[6] = 20
    constants[7] = 50
    constants[8] = 1.25
    constants[9] = 0.08
    constants[10] = 2.5
    constants[11] = 2.2
    constants[12] = 5
    constants[13] = 0.1
    constants[14] = 0.8
    constants[15] = 1.21e3
    constants[16] = 2.5
    constants[17] = 0.05
    constants[18] = 0.8
    constants[19] = 1.21e3
    constants[20] = 0.633
    constants[21] = 0.633
    states[0] = 0.041983438
    states[1] = 0.042634499
    states[2] = 0.000651061
    constants[22] = 10
    states[3] = 0.012644961
    states[4] = 0.013274751
    states[5] = 0.00062979
    constants[23] = 20
    constants[24] = 0.633
    constants[25] = 0.633
    states[6] = 0.083866891
    states[7] = 0.084522918
    states[8] = 0.000656025
    constants[26] = 10
    states[9] = 0.001018705
    states[10] = 0.001475253
    states[11] = 0.000456548
    constants[27] = 1
    constants[28] = 3.379
    constants[29] = 500
    constants[30] = 130
    constants[31] = 5000
    constants[32] = 315
    constants[33] = 0.2
    constants[34] = 130
    constants[35] = 130
    constants[36] = 5000
    constants[37] = 315
    constants[38] = 1.08e-3
    constants[39] = 0.136
    constants[40] = 130
    constants[41] = 5000
    constants[42] = 315
    states[12] = 0.11750433
    constants[43] = 4.5
    constants[44] = 5.6
    constants[45] = 2
    states[13] = 1.092200547
    constants[46] = 0.02
    constants[47] = 0.16
    states[14] = 0.992583576
    constants[48] = 5e-3
    constants[49] = 7.5e-3
    constants[50] = 5e-3
    constants[51] = 38e-12
    constants[52] = 7.5e-15
    constants[53] = 7.5e-14
    constants[54] = 1.5e-17
    constants[55] = (constants[38]*constants[39]*constants[40]*constants[41])/(constants[42]+constants[41])
    constants[56] = 0.0100000*constants[51]
    constants[57] = 0.0200000*constants[51]
    constants[58] = 0.500000*constants[51]
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[2] = states[0]*constants[14]-states[2]*states[1]*constants[15]
    rates[5] = states[3]*constants[18]-states[5]*states[4]*constants[19]
    rates[8] = states[6]*constants[14]-states[8]*states[7]*constants[15]
    rates[11] = states[9]*constants[18]-states[11]*states[10]*constants[19]
    algebraic[0] = custom_piecewise([greater(voi , 120.000) & less_equal(voi , 720.000), 1.00000 , True, 1.00000])
    algebraic[5] = (constants[22]-states[0])-states[2]
    rootfind_0(voi, constants, rates, states, algebraic)
    rates[0] = (algebraic[15]*constants[13]+algebraic[14]*constants[12])-states[0]*constants[14]
    rates[1] = (algebraic[15]*constants[13]+algebraic[14]*constants[12])-states[2]*states[1]*constants[15]
    algebraic[1] = custom_piecewise([greater(voi , 240.000) & less_equal(voi , 540.000), 0.00000 , True, 0.00000])
    algebraic[6] = (constants[23]-states[3])-states[5]
    rootfind_1(voi, constants, rates, states, algebraic)
    rates[3] = (algebraic[19]*constants[17]+algebraic[18]*constants[16])-states[3]*constants[18]
    rates[4] = (algebraic[19]*constants[17]+algebraic[18]*constants[16])-states[5]*states[4]*constants[19]
    algebraic[7] = (constants[26]-states[6])-states[8]
    rootfind_2(voi, constants, rates, states, algebraic)
    rates[6] = (algebraic[23]*constants[13]+algebraic[22]*constants[12])-states[6]*constants[14]
    rates[7] = (algebraic[23]*constants[13]+algebraic[22]*constants[12])-states[8]*states[7]*constants[15]
    algebraic[8] = (constants[27]-states[9])-states[11]
    rootfind_3(voi, constants, rates, states, algebraic)
    rates[9] = (algebraic[27]*constants[17]+algebraic[26]*constants[16])-states[9]*constants[18]
    rates[10] = (algebraic[27]*constants[17]+algebraic[26]*constants[16])-states[11]*states[10]*constants[19]
    algebraic[4] = (constants[6]*constants[48]*states[14])/(constants[7]+states[14])
    algebraic[11] = (constants[8]*constants[49]*states[14])/(constants[9]+states[14])
    algebraic[30] = (constants[10]*constants[50]*states[14])/(constants[11]+states[14])
    rates[14] = (constants[55]-(algebraic[4]+algebraic[11]+algebraic[30]))+(constants[53]*(states[12]-states[14]))/constants[58]+(constants[54]*(states[13]-states[14]))/constants[58]
    algebraic[3] = (((0.0630000+(2.01000*(power(states[6]*1000.00, 1.00430)))/(31.5440+power(states[6]*1000.00, 1.00430)))*(1.00000+((1.00000/3.01000)*49.1000*(power(states[10]*1000.00, 0.892100)))/(25.4400+power(states[10]*1000.00, 0.892100)))*constants[35])/60.0000)*0.00100000
    algebraic[10] = (algebraic[3]*constants[33]*constants[34]*constants[36])/(constants[37]+constants[36])
    algebraic[29] = (constants[6]*constants[46]*states[13])/(constants[7]+states[13])
    algebraic[32] = (constants[10]*constants[47]*states[13])/(constants[11]+states[13])
    rates[13] = ((algebraic[10]-(algebraic[29]+algebraic[32]))+(constants[52]*(states[12]-states[13]))/constants[57])-(constants[54]*(states[13]-states[14]))/constants[57]
    algebraic[2] = (((0.700000+(3.82340*(power(states[0]/1.00000, 0.978700)))/(0.198600+power(states[0]/1.00000, 0.978700)))*(1.00000+((1.00000/1.44320)*-1.00610*(power(states[3]/1.00000, 0.835600)))/(0.191800+power(states[3]/1.00000, 0.835600)))*constants[30])/60.0000)*0.00100000
    algebraic[9] = (algebraic[2]*constants[28]*constants[29]*constants[31])/(constants[32]+constants[31])
    algebraic[28] = (constants[6]*constants[43]*states[12])/(constants[7]+states[12])
    algebraic[31] = (constants[8]*constants[44]*states[12])/(constants[9]+states[12])
    algebraic[33] = (constants[10]*constants[45]*states[12])/(constants[11]+states[12])
    rates[12] = ((algebraic[9]-(algebraic[28]+algebraic[31]+algebraic[33]))-(constants[52]*(states[12]-states[13]))/constants[56])-(constants[53]*(states[12]-states[14]))/constants[56]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = custom_piecewise([greater(voi , 120.000) & less_equal(voi , 720.000), 1.00000 , True, 1.00000])
    algebraic[5] = (constants[22]-states[0])-states[2]
    algebraic[1] = custom_piecewise([greater(voi , 240.000) & less_equal(voi , 540.000), 0.00000 , True, 0.00000])
    algebraic[6] = (constants[23]-states[3])-states[5]
    algebraic[7] = (constants[26]-states[6])-states[8]
    algebraic[8] = (constants[27]-states[9])-states[11]
    algebraic[4] = (constants[6]*constants[48]*states[14])/(constants[7]+states[14])
    algebraic[11] = (constants[8]*constants[49]*states[14])/(constants[9]+states[14])
    algebraic[30] = (constants[10]*constants[50]*states[14])/(constants[11]+states[14])
    algebraic[3] = (((0.0630000+(2.01000*(power(states[6]*1000.00, 1.00430)))/(31.5440+power(states[6]*1000.00, 1.00430)))*(1.00000+((1.00000/3.01000)*49.1000*(power(states[10]*1000.00, 0.892100)))/(25.4400+power(states[10]*1000.00, 0.892100)))*constants[35])/60.0000)*0.00100000
    algebraic[10] = (algebraic[3]*constants[33]*constants[34]*constants[36])/(constants[37]+constants[36])
    algebraic[29] = (constants[6]*constants[46]*states[13])/(constants[7]+states[13])
    algebraic[32] = (constants[10]*constants[47]*states[13])/(constants[11]+states[13])
    algebraic[2] = (((0.700000+(3.82340*(power(states[0]/1.00000, 0.978700)))/(0.198600+power(states[0]/1.00000, 0.978700)))*(1.00000+((1.00000/1.44320)*-1.00610*(power(states[3]/1.00000, 0.835600)))/(0.191800+power(states[3]/1.00000, 0.835600)))*constants[30])/60.0000)*0.00100000
    algebraic[9] = (algebraic[2]*constants[28]*constants[29]*constants[31])/(constants[32]+constants[31])
    algebraic[28] = (constants[6]*constants[43]*states[12])/(constants[7]+states[12])
    algebraic[31] = (constants[8]*constants[44]*states[12])/(constants[9]+states[12])
    algebraic[33] = (constants[10]*constants[45]*states[12])/(constants[11]+states[12])
    return algebraic

initialGuess0 = None
def rootfind_0(voi, constants, rates, states, algebraic):
    """Calculate values of algebraic variables for DAE"""
    from scipy.optimize import fsolve
    global initialGuess0
    if initialGuess0 is None: initialGuess0 = ones(4)*0.1
    if not iterable(voi):
        soln = fsolve(residualSN_0, initialGuess0, args=(algebraic, voi, constants, rates, states), xtol=1E-6)
        initialGuess0 = soln
        algebraic[12] = soln[0]
        algebraic[13] = soln[1]
        algebraic[14] = soln[2]
        algebraic[15] = soln[3]
    else:
        for (i,t) in enumerate(voi):
            soln = fsolve(residualSN_0, initialGuess0, args=(algebraic[:,i], voi[i], constants, rates[:i], states[:,i]), xtol=1E-6)
            initialGuess0 = soln
            algebraic[12][i] = soln[0]
            algebraic[13][i] = soln[1]
            algebraic[14][i] = soln[2]
            algebraic[15][i] = soln[3]

def residualSN_0(algebraicCandidate, algebraic, voi, constants, rates, states):
    resid = array([0.0] * 4)
    algebraic[12] = algebraicCandidate[0]
    algebraic[13] = algebraicCandidate[1]
    algebraic[14] = algebraicCandidate[2]
    algebraic[15] = algebraicCandidate[3]
    resid[0] = (algebraic[12]-(((constants[20]-algebraic[13])-algebraic[14])-algebraic[15]))
    resid[1] = (algebraic[13]-(algebraic[0]*algebraic[12])/constants[1])
    resid[2] = (algebraic[14]-(algebraic[0]*algebraic[12]*algebraic[5])/(constants[0]*constants[2]))
    resid[3] = (algebraic[15]-(algebraic[12]*algebraic[5])/constants[2])
    return resid

initialGuess1 = None
def rootfind_1(voi, constants, rates, states, algebraic):
    """Calculate values of algebraic variables for DAE"""
    from scipy.optimize import fsolve
    global initialGuess1
    if initialGuess1 is None: initialGuess1 = ones(4)*0.1
    if not iterable(voi):
        soln = fsolve(residualSN_1, initialGuess1, args=(algebraic, voi, constants, rates, states), xtol=1E-6)
        initialGuess1 = soln
        algebraic[16] = soln[0]
        algebraic[17] = soln[1]
        algebraic[18] = soln[2]
        algebraic[19] = soln[3]
    else:
        for (i,t) in enumerate(voi):
            soln = fsolve(residualSN_1, initialGuess1, args=(algebraic[:,i], voi[i], constants, rates[:i], states[:,i]), xtol=1E-6)
            initialGuess1 = soln
            algebraic[16][i] = soln[0]
            algebraic[17][i] = soln[1]
            algebraic[18][i] = soln[2]
            algebraic[19][i] = soln[3]

def residualSN_1(algebraicCandidate, algebraic, voi, constants, rates, states):
    resid = array([0.0] * 4)
    algebraic[16] = algebraicCandidate[0]
    algebraic[17] = algebraicCandidate[1]
    algebraic[18] = algebraicCandidate[2]
    algebraic[19] = algebraicCandidate[3]
    resid[0] = (algebraic[16]-(((constants[21]-algebraic[17])-algebraic[18])-algebraic[19]))
    resid[1] = (algebraic[17]-(algebraic[1]*algebraic[16])/constants[4])
    resid[2] = (algebraic[18]-(algebraic[1]*algebraic[16]*algebraic[6])/(constants[3]*constants[5]))
    resid[3] = (algebraic[19]-(algebraic[16]*algebraic[6])/constants[5])
    return resid

initialGuess2 = None
def rootfind_2(voi, constants, rates, states, algebraic):
    """Calculate values of algebraic variables for DAE"""
    from scipy.optimize import fsolve
    global initialGuess2
    if initialGuess2 is None: initialGuess2 = ones(4)*0.1
    if not iterable(voi):
        soln = fsolve(residualSN_2, initialGuess2, args=(algebraic, voi, constants, rates, states), xtol=1E-6)
        initialGuess2 = soln
        algebraic[20] = soln[0]
        algebraic[21] = soln[1]
        algebraic[22] = soln[2]
        algebraic[23] = soln[3]
    else:
        for (i,t) in enumerate(voi):
            soln = fsolve(residualSN_2, initialGuess2, args=(algebraic[:,i], voi[i], constants, rates[:i], states[:,i]), xtol=1E-6)
            initialGuess2 = soln
            algebraic[20][i] = soln[0]
            algebraic[21][i] = soln[1]
            algebraic[22][i] = soln[2]
            algebraic[23][i] = soln[3]

def residualSN_2(algebraicCandidate, algebraic, voi, constants, rates, states):
    resid = array([0.0] * 4)
    algebraic[20] = algebraicCandidate[0]
    algebraic[21] = algebraicCandidate[1]
    algebraic[22] = algebraicCandidate[2]
    algebraic[23] = algebraicCandidate[3]
    resid[0] = (algebraic[20]-(((constants[24]-algebraic[21])-algebraic[22])-algebraic[23]))
    resid[1] = (algebraic[21]-(algebraic[0]*algebraic[20])/constants[1])
    resid[2] = (algebraic[22]-(algebraic[0]*algebraic[20]*algebraic[7])/(constants[0]*constants[2]))
    resid[3] = (algebraic[23]-(algebraic[20]*algebraic[7])/constants[2])
    return resid

initialGuess3 = None
def rootfind_3(voi, constants, rates, states, algebraic):
    """Calculate values of algebraic variables for DAE"""
    from scipy.optimize import fsolve
    global initialGuess3
    if initialGuess3 is None: initialGuess3 = ones(4)*0.1
    if not iterable(voi):
        soln = fsolve(residualSN_3, initialGuess3, args=(algebraic, voi, constants, rates, states), xtol=1E-6)
        initialGuess3 = soln
        algebraic[24] = soln[0]
        algebraic[25] = soln[1]
        algebraic[26] = soln[2]
        algebraic[27] = soln[3]
    else:
        for (i,t) in enumerate(voi):
            soln = fsolve(residualSN_3, initialGuess3, args=(algebraic[:,i], voi[i], constants, rates[:i], states[:,i]), xtol=1E-6)
            initialGuess3 = soln
            algebraic[24][i] = soln[0]
            algebraic[25][i] = soln[1]
            algebraic[26][i] = soln[2]
            algebraic[27][i] = soln[3]

def residualSN_3(algebraicCandidate, algebraic, voi, constants, rates, states):
    resid = array([0.0] * 4)
    algebraic[24] = algebraicCandidate[0]
    algebraic[25] = algebraicCandidate[1]
    algebraic[26] = algebraicCandidate[2]
    algebraic[27] = algebraicCandidate[3]
    resid[0] = (algebraic[24]-(((constants[25]-algebraic[25])-algebraic[26])-algebraic[27]))
    resid[1] = (algebraic[25]-(algebraic[1]*algebraic[24])/constants[4])
    resid[2] = (algebraic[26]-(algebraic[1]*algebraic[24]*algebraic[8])/(constants[3]*constants[5]))
    resid[3] = (algebraic[27]-(algebraic[24]*algebraic[8])/constants[5])
    return resid

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
        self.K_H = 0.035
        self.K_L = 0.386
        self.K_C = 8.809
        self.K_H_1 = 0.16
        self.K_L_1 = 11
        self.K_C_1 = 30
        self.k_PDE2 = 20
        self.Km_PDE2 = 50
        self.k_PDE3 = 1.25
        self.Km_PDE3 = 0.08
        self.k_PDE4 = 2.5
        self.Km_PDE4 = 2.2
        self.k_act1 = 5
        self.k_act2 = 0.1
        self.k_hydr = 0.8
        self.k_reas = 1.21e3
        self.k_act1_1 = 2.5
        self.k_act2_1 = 0.05
        self.k_hydr_1 = 0.8
        self.k_reas_1 = 1.21e3
        self.R_Total = 0.633
        self.R_Total_1 = 0.633
        self.Gs_Total = 10
        self.Gi_Total = 20
        self.R_Total_2 = 0.633
        self.R_Total_3 = 0.633
        self.Gs_Total_1 = 10
        self.Gi_Total_1 = 1
        self.AC_56 = 3.379
        self.AF56 = 500
        self.MW_AC56 = 130
        self.ATP = 5000
        self.Km_ATP = 315
        self.AC_47_ecav = 0.2
        self.AF47 = 130
        self.MW_AC47 = 130
        self.ATP_1 = 5000
        self.Km_ATP_1 = 315
        self.k_AC47_cyt = 1.08e-3
        self.AC_47_cyt = 0.136
        self.AF47_1 = 130
        self.ATP_2 = 5000
        self.Km_ATP_2 = 315
        self.PDE2 = 4.5
        self.PDE3 = 5.6
        self.PDE4 = 2
        self.PDE2_1 = 0.02
        self.PDE4_1 = 0.16
        self.PDE2_2 = 5e-3
        self.PDE3_1 = 7.5e-3
        self.PDE4_2 = 5e-3
        self.V_cell = 38e-12
        self.J_cav_ecav = 7.5e-15
        self.J_cav_cyt = 7.5e-14
        self.J_ecav_cyt = 1.5e-17

    def to_dict(self):
        return {
            "K_H": self.K_H,
            "K_L": self.K_L,
            "K_C": self.K_C,
            "K_H_1": self.K_H_1,
            "K_L_1": self.K_L_1,
            "K_C_1": self.K_C_1,
            "k_PDE2": self.k_PDE2,
            "Km_PDE2": self.Km_PDE2,
            "k_PDE3": self.k_PDE3,
            "Km_PDE3": self.Km_PDE3,
            "k_PDE4": self.k_PDE4,
            "Km_PDE4": self.Km_PDE4,
            "k_act1": self.k_act1,
            "k_act2": self.k_act2,
            "k_hydr": self.k_hydr,
            "k_reas": self.k_reas,
            "k_act1_1": self.k_act1_1,
            "k_act2_1": self.k_act2_1,
            "k_hydr_1": self.k_hydr_1,
            "k_reas_1": self.k_reas_1,
            "R_Total": self.R_Total,
            "R_Total_1": self.R_Total_1,
            "Gs_Total": self.Gs_Total,
            "Gi_Total": self.Gi_Total,
            "R_Total_2": self.R_Total_2,
            "R_Total_3": self.R_Total_3,
            "Gs_Total_1": self.Gs_Total_1,
            "Gi_Total_1": self.Gi_Total_1,
            "AC_56": self.AC_56,
            "AF56": self.AF56,
            "MW_AC56": self.MW_AC56,
            "ATP": self.ATP,
            "Km_ATP": self.Km_ATP,
            "AC_47_ecav": self.AC_47_ecav,
            "AF47": self.AF47,
            "MW_AC47": self.MW_AC47,
            "ATP_1": self.ATP_1,
            "Km_ATP_1": self.Km_ATP_1,
            "k_AC47_cyt": self.k_AC47_cyt,
            "AC_47_cyt": self.AC_47_cyt,
            "AF47_1": self.AF47_1,
            "ATP_2": self.ATP_2,
            "Km_ATP_2": self.Km_ATP_2,
            "PDE2": self.PDE2,
            "PDE3": self.PDE3,
            "PDE4": self.PDE4,
            "PDE2_1": self.PDE2_1,
            "PDE4_1": self.PDE4_1,
            "PDE2_2": self.PDE2_2,
            "PDE3_1": self.PDE3_1,
            "PDE4_2": self.PDE4_2,
            "V_cell": self.V_cell,
            "J_cav_ecav": self.J_cav_ecav,
            "J_cav_cyt": self.J_cav_cyt,
            "J_ecav_cyt": self.J_ecav_cyt,
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
        y0=[0.041983438, 0.042634499, 0.000651061, 0.012644961, 0.013274751, 0.00062979, 0.083866891, 0.084522918, 0.000656025, 0.001018705, 0.001475253, 0.000456548, 0.11750433, 1.092200547, 0.992583576],
    ):
        if param is None:
            raise ValueError("Config requires param=Parameters()")

        self.model_name = "iancu_jones_harvey_2007"
        self.curve_names = [
            "Gs_alpha_GTP",
            "Gs_beta_gamma",
            "Gs_alpha_GDP",
            "Gi_alpha_GTP",
            "Gi_beta_gamma",
            "Gi_alpha_GDP",
            "Gs_alpha_GTP_1",
            "Gs_beta_gamma_1",
            "Gs_alpha_GDP_1",
            "Gi_alpha_GTP_1",
            "Gi_beta_gamma_1",
            "Gi_alpha_GDP_1",
            "cAMP_cav",
            "cAMP_ecav",
            "cAMP_cyt",
        ]
        self.state_names = ['Gs_alpha_GTP', 'Gs_beta_gamma', 'Gs_alpha_GDP', 'Gi_alpha_GTP', 'Gi_beta_gamma', 'Gi_alpha_GDP', 'Gs_alpha_GTP_1', 'Gs_beta_gamma_1', 'Gs_alpha_GDP_1', 'Gi_alpha_GTP_1', 'Gi_beta_gamma_1', 'Gi_alpha_GDP_1', 'cAMP_cav', 'cAMP_ecav', 'cAMP_cyt']
        self.algebraic_names = ['L_iso', 'L_ach', 'k_AC56', 'k_AC47_ecav', 'dcAMP_cyt_PDE2_dt', 'Gs_alpha_beta_gamma', 'Gi_alpha_beta_gamma', 'Gs_alpha_beta_gamma_1', 'Gi_alpha_beta_gamma_1', 'dcAMP_AC_56_dt', 'dcAMP_AC_47_ecav_dt', 'dcAMP_cyt_PDE3_dt', 'R', 'LR', 'LRG', 'RG', 'R_1', 'LR_1', 'LRG_1', 'RG_1', 'R_2', 'LR_2', 'LRG_2', 'RG_2', 'R_3', 'LR_3', 'LRG_3', 'RG_3', 'dcAMP_cav_PDE2_dt', 'dcAMP_ecav_PDE2_dt', 'dcAMP_cyt_PDE4_dt', 'dcAMP_cav_PDE3_dt', 'dcAMP_ecav_PDE4_dt', 'dcAMP_cav_PDE4_dt']
        self.params = param
        self.T = T
        self.T_unit = T_unit
        self.T_N = int(self.T / self.T_unit)
        self.prob_dim = len(y0)
        self.y0 = np.asarray(y0)
        self.t = np.asarray([i * self.T_unit for i in range(self.T_N)])
        self.truth = odeint(self.pend, self.y0, self.t) if calculate else None

    def _build_constants(self):
        c = [0.0] * 59
        p = self.params

        # direct mapping
        c[0] = p.K_H
        c[1] = p.K_L
        c[2] = p.K_C
        c[3] = p.K_H_1
        c[4] = p.K_L_1
        c[5] = p.K_C_1
        c[6] = p.k_PDE2
        c[7] = p.Km_PDE2
        c[8] = p.k_PDE3
        c[9] = p.Km_PDE3
        c[10] = p.k_PDE4
        c[11] = p.Km_PDE4
        c[12] = p.k_act1
        c[13] = p.k_act2
        c[14] = p.k_hydr
        c[15] = p.k_reas
        c[16] = p.k_act1_1
        c[17] = p.k_act2_1
        c[18] = p.k_hydr_1
        c[19] = p.k_reas_1
        c[20] = p.R_Total
        c[21] = p.R_Total_1
        c[22] = p.Gs_Total
        c[23] = p.Gi_Total
        c[24] = p.R_Total_2
        c[25] = p.R_Total_3
        c[26] = p.Gs_Total_1
        c[27] = p.Gi_Total_1
        c[28] = p.AC_56
        c[29] = p.AF56
        c[30] = p.MW_AC56
        c[31] = p.ATP
        c[32] = p.Km_ATP
        c[33] = p.AC_47_ecav
        c[34] = p.AF47
        c[35] = p.MW_AC47
        c[36] = p.ATP_1
        c[37] = p.Km_ATP_1
        c[38] = p.k_AC47_cyt
        c[39] = p.AC_47_cyt
        c[40] = p.AF47_1
        c[41] = p.ATP_2
        c[42] = p.Km_ATP_2
        c[43] = p.PDE2
        c[44] = p.PDE3
        c[45] = p.PDE4
        c[46] = p.PDE2_1
        c[47] = p.PDE4_1
        c[48] = p.PDE2_2
        c[49] = p.PDE3_1
        c[50] = p.PDE4_2
        c[51] = p.V_cell
        c[52] = p.J_cav_ecav
        c[53] = p.J_cav_cyt
        c[54] = p.J_ecav_cyt

        # derived constants
        c[55] = (c[38]*c[39]*c[40]*c[41])/(c[42]+c[41])
        c[56] = 0.0100000*c[51]
        c[57] = 0.0200000*c[51]
        c[58] = 0.500000*c[51]

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
