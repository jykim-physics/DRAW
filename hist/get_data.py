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

def get_data(file='file', sample=None, tree='tree', base_filter=None,variables=None):

    tree=tree
    f = file
    base_filter  = base_filter

    ROOT_df_start_0 = ROOT.RDataFrame(tree, f)
    ROOT_df_start   = ROOT_df_start_0.Filter('Dstarp_isSignal!=1')

    if base_filter !=None:
        ROOT_df_filtered  = ROOT_df_start.Filter(base_filter)
        col_dict  = ROOT_df_filtered.AsNumpy(variables)
    else:
        col_dict  = ROOT_df_start.AsNumpy(variables)

    pd_df  = pd.DataFrame(col_dict)
    pd_df['class'] = sample

    return pd_df
