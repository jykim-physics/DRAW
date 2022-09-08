#import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#import math
#import uproot
#from b2plot import hist
#import b2plot as bp
import ROOT
#from root_pandas import read_root

import seaborn as sns
#%matplotlib inline
#px = 1/plt.rcParams['figure.dpi']



def get_data(file='file', figname='name', tree='tree', base_filter=None,variables=None):
    
    tree=tree
    f = file
    base_filter  = base_filter    
    
    ROOT_df_start = ROOT.RDataFrame(tree, f)  
    
    col_dict  = ROOT_df_start.AsNumpy(variables)
    
    if base_filter !=None:
        ROOT_df_filtered  = ROOT_df_start.Filter(base_filter)                            
        col_dict  = ROOT_df_filtered.AsNumpy(variables)
    
    pd_df  = pd.DataFrame(col_dict)
    
    return pd_df