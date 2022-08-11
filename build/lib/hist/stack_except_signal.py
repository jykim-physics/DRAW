import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pds

def draw_stack_except_signal(df=None, df_no_signal=None, vector=None):
    variables = list(df.columns)
    
    ccbar_bkg = df_no_signal[df_no_signal['class']=='ccbar']
    signal    = df[df['Dstarp_isSignal']==1]
    
    charged_bkg = df[df['class']=='charged']
    mixed_bkg = df[df['class']=='mixed']
    uubar_bkg = df[df['class']=='uubar']
    ddbar_bkg = df[df['class']=='ddbar']
    ssbar_bkg = df[df['class']=='ssbar']
    taupair_bkg = df[df['class']=='taupair']
    
    data_list = {}
    labels = ['signal', 'ccbar', 'charged', 'mixed', 'uubar', 'ddbar', 'ssbar', 'taupair']
    for var in variables:
        data_list[var]  = [signal[var], ccbar_bkg[var], charged_bkg[var], mixed_bkg[var], uubar_bkg[var], ddbar_bkg[var], ssbar_bkg[var], taupair_bkg[var] ] 
        colors=sns.cubehelix_palette(8, start=1.5, rot=1.5, dark=0.3, light=.8, reverse=True)
    
        plt.hist(data_list[var], bins=bins, histtype='stepfilled', stacked=True,label=labels,color=colors,edgecolor='black')