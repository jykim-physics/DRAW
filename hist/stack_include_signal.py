import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def draw_stack_include_signal(df=None, df_no_signal=None, vector=None,bins=None, var_unit=None, var_name=None,plot_title=None):
    variables = list(df.columns)
    px = 1/plt.rcParams['figure.dpi']
    plt.figure(figsize=(576*px, 396*px))
    
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
        
        ax = plt.gca()
        
        
        var_unit[var] = var_unit[var].replace("mathrm{GeV}", "\mathrm{GeV}" )
        var_name[var] = var_name[var].replace("mathrm{cos}Hel_0", "\mathrm{cos} \theta_{H}" )
        var_name[var] = var_name[var].replace("M(/phi)", "M(\phi)" )
        var_name[var] = var_name[var].replace("M(/rho^0)", "M(\rho^0)" )
        var_name[var] = var_name[var].replace("M(/omega)", "M(\omega)" )
        var_name[var] = var_name[var].replace("M(/bar{K}^{*0})", "M(\bar{K}^{*0})" )
        
        var_name[var] = var_name[var].replace("gamma", r"\gamma" )
        if var_unit[var]=="":
            
            xlabel = "$" + var_name[var] + "$"
        else:    
            xlabel = "$" + var_name[var] + "$ $[" + var_unit[var] + "]$"
        ax.set_xlabel(xlabel)

        x_axis = ax.get_xbound()
        width = (x_axis[1] - x_axis[0])/bins  
        #print(width)
#         ax.set_ylabel('Entries'+' /' + '$(' + ' '  + "{0:.3f}".format(width).rstrip('0').rstrip('.') + var_unit[var] + ' )$')
        
        plt.title(plot_title)
        plt.show()
        plt.clf()
    print(data_list.keys())