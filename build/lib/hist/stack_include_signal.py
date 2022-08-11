import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pds

def draw_stack_include_signal(df=None, df_no_signal=None, vector=None,bins=None):
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
    data_list['phi'] = dict()
    data_list['rho'] = dict()
    data_list['antiKstar'] = dict()
    data_list['omega'] = dict()
    
    labels = ['mixed', 'charged', 'uubar', 'ddbar', 'ssbar', 'taupair','ccbar', 'signal', ]
    variables.remove('class')
    for var in variables:
        data_list[vector][var]  = [mixed_bkg[var], charged_bkg[var], uubar_bkg[var], ddbar_bkg[var], ssbar_bkg[var], taupair_bkg[var], ccbar_bkg[var], signal[var] ] 
        colors=sns.cubehelix_palette(8, start=1.5, rot=1.5, dark=0.3, light=.8, reverse=True)
    
        plt.hist(data_list[vector][var], bins=bins, histtype='stepfilled', stacked=True,label=labels,color=colors,edgecolor='black')
        
        plt.show()
        plt.clf()
    print(data_list.keys())