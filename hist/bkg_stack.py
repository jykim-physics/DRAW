import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
import b2plot as bp
import ROOT

import seaborn as sns
try:
    #plt.style.use('belle2')
    plt.style.use('belle2_serif')
    #plt.style.use('belle2_modern')
except OSError:
    print("Please install belle2 matplotlib style")   
    
print(plt.style.available)
#px = 1/plt.rcParams['figure.dpi']

def make_df(f=None, sample=None,tree='tree',base_filter=None,true_filter=None, false_filter=None,variables=None):
    ROOT_df_start = ROOT.RDataFrame(tree, f)
    ROOT_df       = ROOT_df_start.Filter(base_filter)
    
    
    ROOT_df_true  = ROOT_df_start.Filter(true_filter)                        
    ROOT_df_false = ROOT_df_start.Filter(false_filter)

    col_dict       = ROOT_df.AsNumpy(variables)    
    col_dict_true  = ROOT_df_true.AsNumpy(variables)
    col_dict_false = ROOT_df_false.AsNumpy(variables)   

    pd_df       = pd.DataFrame(col_dict)
    pd_df_true  = pd.DataFrame(col_dict_true)
    pd_df_false = pd.DataFrame(col_dict_false)  

    pd_df['class'] = sample
    pd_df_true['class'] = 'signal'
    if sample=='ccbar':
        pd_df_false['class'] = 'ccbar_bkg'  
    else:
        pd_df_false['class'] = sample

    return pd_df, pd_df_true, pd_df_false  

def get_data_in_module(file='file', sample=None, tree='tree', base_filter=None,variables=None):
    
    tree=tree
    f = file
    base_filter  = base_filter    
    
    ROOT_df_start = ROOT.RDataFrame(tree, f)  

    
    if base_filter !=None:
        ROOT_df_filtered  = ROOT_df_start.Filter(base_filter)                            
        col_dict  = ROOT_df_filtered.AsNumpy(variables)
    else:
        col_dict  = ROOT_df_start.AsNumpy(variables)
    
    pd_df  = pd.DataFrame(col_dict)
    pd_df['class'] = sample
    
    return pd_df

def generic_ntuple(loc=None,all_stack=None,file='file', vector='type', figname='name',option=None, add_base_filter=None, add_t_filter=None, add_f_filter=None, bins=None, variables_dict=None, sample_location=None):


    px = 1/plt.rcParams['figure.dpi'] 
    tree=vector

#     var=list(variables_dict.keys())
    
    variables = variables_dict['vars']


    base_filter = '(D0_M>1.665 && D0_M<2.065) && (gamma_E>0.1)'  
    
    true_filter = ' && (Dstarp_isSignal==1)'
    false_filter = ' && (Dstarp_isSignal!=1)'
    true_filter  = base_filter + true_filter
    false_filter = base_filter + false_filter

    if add_base_filter != None:
        base_filter = base_filter + ' && ' + add_base_filter
        true_filter = true_filter + ' && ' + add_base_filter
        false_filter = false_filter + ' && ' + add_base_filter
        print(true_filter)
        print(false_filter)

    if add_t_filter != None and add_f_filter != None:
        true_filter = true_filter + ' && ' + add_t_filter
        flase_filter = false_filter + ' && ' + add_f_filter


    if vector == 'omega':
        plot_title = r"$\omega$ mode"
        variables.append("D0_cosHel_2")
        variables.append("Omega_InvM")
    elif vector == 'phi':
        plot_title = r"$\phi$ mode"
        variables.append("Phi_InvM")
        variables.append("D0_cosHel_0")
    elif vector == 'rho':
        plot_title = r"$\rho^0$ mode"
        variables.append("Rho_InvM")
        variables.append("D0_cosHel_0")
    elif vector == 'antiKstar':
        plot_title = r"$\bar{K}^{*0}$ mode"
        variables.append("antiKstar_InvM")
        variables.append("D0_cosHel_0")
    print(variables) 
    List = ['ccbar', 'charged','mixed', 'uubar', 'ddbar', 'ssbar','taupair'] 
    for f_type in List:
        if f_type=='ccbar':
            file = sample_location[f_type]
            ccbar_pd_df = get_data_in_module(file=file, sample=f_type, tree=tree,variables=variables)
        elif f_type=='charged':
            file = sample_location[f_type]
            charged_pd_df = get_data_in_module(file=file, sample=f_type, tree=tree,variables=variables)
        elif f_type=='mixed':
            file = sample_location[f_type]
            mixed_pd_df = get_data_in_module(file=file, sample=f_type, tree=tree,variables=variables)
        elif f_type=='uubar':
            file = sample_location[f_type]
            uubar_pd_df = get_data_in_module(file=file, sample=f_type, tree=tree,variables=variables)        
        elif f_type=='ddbar':
            file = sample_location[f_type]
            ddbar_pd_df = get_data_in_module(file=file, sample=f_type, tree=tree,variables=variables)            
        elif f_type=='ssbar':
            file = sample_location[f_type]
            ssbar_pd_df = get_data_in_module(file=file, sample=f_type, tree=tree,variables=variables)            
        elif f_type=='taupair':
            file = sample_location[f_type]
            taupair_pd_df = get_data_in_module(file=file, sample=f_type, tree=tree,variables=variables)
            
    pd_merge_df = pd.concat([ ccbar_pd_df, mixed_pd_df, charged_pd_df, uubar_pd_df, ddbar_pd_df, ssbar_pd_df, taupair_pd_df])

    return pd_merge_df

