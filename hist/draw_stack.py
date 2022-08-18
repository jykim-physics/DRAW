import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def b2blues(n=5):
    return sns.color_palette("PuBuGn_d", n)

def b2greens(n=3):
    return sns.color_palette("summer", n)

def b2helix(n):
    return sns.cubehelix_palette(n, start=1.5, rot=1.5, dark=0.3, light=.8, reverse=True)

def lumi(l="$1\; \mathrm{ab}^{-1}$", px=0.7, py=0.900,  *args, **kwargs):
    plt.text(px, py, "$\int\,L\,\mathrm{dt}\;=\;$" + l, transform=plt.gca().transAxes, *args, **kwargs )

def watermark(t=None,logo="Belle II", px=0.033, py=0.915, fontsize=16, alpha=0.8, alpha_logo=0.95, shift=0.15, bstyle='italic', *args, **kwargs):
    """

    Args:
        t:
        logo:
        px:
        py:
        fontsize:
        alpha:
        shift:
        *args:
        **kwargs:

    Returns:

    """
    if t is None:
        import datetime
        t = " %d (group)" % datetime.date.today().year

    plt.text(px, py, logo, ha='left',
             transform=plt.gca().transAxes,
             fontsize=fontsize,
             style=bstyle,
             alpha=alpha_logo,
             weight='bold',
             *args, **kwargs,
             # fontproperties=font,
             # bbox={'facecolor':'#377eb7', 'alpha':0.1, 'pad':10}
             )
    plt.text(px + shift, py, t, ha='left',
             transform=plt.gca().transAxes,
             fontsize=fontsize,
             #          style='italic',
             alpha=alpha,  *args, **kwargs
             #          fontproperties=font,
             # bbox={'facecolor':'#377eb7', 'alpha':0.1, 'pad':10}
             )    
def var_name_unit_correct(var_unit=dict(), var_name=dict(), variables=list()):
        #variables = list(df.columns)
        for var in variables:
            if var not in list(var_name.keys()):
                var_unit[var] = ""
                var_name[var] = var.replace("_", " \; ")
            else:
                var_unit[var] = var_unit[var].replace("mathrm{GeV}", "\mathrm{GeV}" )

                var_name[var] = var_name[var].replace("mathrm{cos}Hel_0", r"\mathrm{cos} \theta_{H}" )
                var_name[var] = var_name[var].replace("M(/phi)", "M(\phi)" )
                var_name[var] = var_name[var].replace("M(/rho^0)", "M(\rho^0)" )
                var_name[var] = var_name[var].replace("M(/omega)", "M(\omega)" )
                var_name[var] = var_name[var].replace("M(/bar{K}^{*0})", "M(\bar{K}^{*0})" )
                var_name[var] = var_name[var].replace("gamma", r"\gamma" )
            

        
        return var_unit, var_name

def draw_stack_include_signal(df=None, df_no_signal=None, vector=None,bins=None, var_unit=dict(), var_name=dict(),plot_title=None):
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
    
    
    variables.remove('class')
    #colors=sns.cubehelix_palette(8, start=1.5, rot=1.5, dark=0.3, light=.8, reverse=True)
    colors=b2helix(n=8)
    var_unit, var_name = var_name_unit_correct(var_unit=var_unit, var_name=var_name, variables=variables)
    for var in variables:
        labels = ['mixed', 'charged', 'uubar', 'ddbar', 'ssbar', 'taupair','ccbar', 'signal' ]
        data_list[vector][var]  = [mixed_bkg[var], charged_bkg[var], uubar_bkg[var], ddbar_bkg[var], ssbar_bkg[var], taupair_bkg[var], ccbar_bkg[var], signal[var] ] 
        
        data_merge_pd = pd.concat([mixed_bkg[var], charged_bkg[var], uubar_bkg[var], ddbar_bkg[var], ssbar_bkg[var], taupair_bkg[var], ccbar_bkg[var], signal[var] ], ignore_index=True)
        
        #colors=sns.cubehelix_palette(8, start=1.5, rot=1.5, dark=0.3, light=.8, reverse=True)
            
            
        plt.hist(data_list[vector][var], bins=bins, histtype='stepfilled', stacked=True,label=labels,color=colors,edgecolor='black')
        plt.legend(bbox_to_anchor=(1,1))
        ax = plt.gca()
        
        lumi()
        watermark(t="(group)")
        #print(df.columns)
        

        if var_unit[var]=="":
            
            xlabel = "$" + var_name[var] + "$"
        else:    
            xlabel = "$" + var_name[var] + "$ $[" + var_unit[var] + "]$"
        ax.set_xlabel(xlabel)

        x_axis = ax.get_xbound()
        width = (x_axis[1] - x_axis[0])/bins  
        
        
        #print(width)
        if var == "Dstarp_Q":
            ax.set_ylabel('Entries'+' /' + '$(' + ' '  + "{0:.5f}".format(width).rstrip('0').rstrip('.') + var_unit[var] + ' )$')
        else:
            ax.set_ylabel('Entries'+' /' + '$(' + ' '  + "{0:.3f}".format(width).rstrip('0').rstrip('.') + var_unit[var] + ' )$')
        exceptlist = ['__ncandidates__','__experiment__','__run__', '__event__'] 
        if var in exceptlist:
            pass
        else:
            ax.set_xlim(data_merge_pd.min(), data_merge_pd.max())            
        
        plt.title(plot_title)
        plt.show()
        plt.clf()
        
        
    print(data_list.keys())

    

    

def draw_stack_except_signal(df=None, df_no_signal=None, vector=None,bins=None, var_unit=None, var_name=None,plot_title=None):
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
    
    colors=b2helix(7)
    
    var_unit, var_name = var_name_unit_correct(var_unit=var_unit, var_name=var_name, variables=variables)
    
    for var in variables:
        labels = ['mixed', 'charged', 'uubar', 'ddbar', 'ssbar', 'taupair','ccbar']
        data_list[vector][var]  = [mixed_bkg[var], charged_bkg[var], uubar_bkg[var], ddbar_bkg[var], ssbar_bkg[var], taupair_bkg[var], ccbar_bkg[var]]         
        data_merge_pd = pd.concat([mixed_bkg[var], charged_bkg[var], uubar_bkg[var], ddbar_bkg[var], ssbar_bkg[var], taupair_bkg[var], ccbar_bkg[var] ], ignore_index=True)
        
        
            
            
        plt.hist(data_list[vector][var], bins=bins, histtype='stepfilled', stacked=True,label=labels,color=colors,edgecolor='black')
        plt.legend(bbox_to_anchor=(1.078,1))
        ax = plt.gca()
        
        
        lumi()
        watermark()    
        
        if var_unit[var]=="":
            
            xlabel = "$" + var_name[var] + "$"
        else:    
            xlabel = "$" + var_name[var] + "$ $[" + var_unit[var] + "]$"
        ax.set_xlabel(xlabel)

        x_axis = ax.get_xbound()
        width = (x_axis[1] - x_axis[0])/bins  
        
        
        ax2 = ax.twinx()

        

        if var == "Dstarp_Q":
            ax.set_ylabel('Entries'+' /' + '$(' + ' '  + "{0:.5f}".format(width).rstrip('0').rstrip('.') + var_unit[var] + ' )$')
        else:
            ax.set_ylabel('Entries'+' /' + '$(' + ' '  + "{0:.3f}".format(width).rstrip('0').rstrip('.') + var_unit[var] + ' )$')
            
        exceptlist = ['__ncandidates__','__experiment__','__run__', '__event__','D0_isSignal','Dstarp_isSignal'] 
        if var in exceptlist:
            pass
        else:
            ax.set_xlim(data_merge_pd.min(), data_merge_pd.max())  
            ax2.set_xlim(data_merge_pd.min(), data_merge_pd.max())  

        

        ax2.hist(signal[var], label=r'signal', bins=bins, color='tab:blue', histtype='step')

        ax2.tick_params(axis='y', labelcolor='tab:blue')            
        plt.legend(bbox_to_anchor=(1.078,0.4))            
            
        plt.title(plot_title)
        plt.show()
        plt.clf()
        
        
    print(data_list.keys())


def draw_stack_no_signal(df=None, vector=None,bins=None, var_unit=None, var_name=None,plot_title=None, total_lumi=None):
    variables = list(df.columns)
    px = 1/plt.rcParams['figure.dpi']
    plt.figure(figsize=(576*px, 396*px))
    
    ccbar_bkg = df[df['class']=='ccbar']
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
    
    colors=b2helix(7)
    
    var_unit, var_name = var_name_unit_correct(var_unit=var_unit, var_name=var_name, variables=variables)
    
    for var in variables:
        labels = ['mixed', 'charged', 'uubar', 'ddbar', 'ssbar', 'taupair','ccbar']
        data_list[vector][var]  = [mixed_bkg[var], charged_bkg[var], uubar_bkg[var], ddbar_bkg[var], ssbar_bkg[var], taupair_bkg[var], ccbar_bkg[var]]         
        data_merge_pd = pd.concat([mixed_bkg[var], charged_bkg[var], uubar_bkg[var], ddbar_bkg[var], ssbar_bkg[var], taupair_bkg[var], ccbar_bkg[var] ], ignore_index=True)
        
        
            
            
        plt.hist(data_list[vector][var], bins=bins, histtype='stepfilled', stacked=True,label=labels,color=colors,edgecolor='black')
        plt.legend(bbox_to_anchor=(1.078,1))
        ax = plt.gca()
        
        
        lumi(l=total_lumi)
        watermark()    
        
        if var_unit[var]=="":
            
            xlabel = "$" + var_name[var] + "$"
        else:    
            xlabel = "$" + var_name[var] + "$ $[" + var_unit[var] + "]$"
        ax.set_xlabel(xlabel)

        x_axis = ax.get_xbound()
        width = (x_axis[1] - x_axis[0])/bins  
        
        
        ax2 = ax.twinx()

        

        if var == "Dstarp_Q":
            ax.set_ylabel('Entries'+' /' + '$(' + ' '  + "{0:.5f}".format(width).rstrip('0').rstrip('.') + var_unit[var] + ' )$')
        else:
            ax.set_ylabel('Entries'+' /' + '$(' + ' '  + "{0:.3f}".format(width).rstrip('0').rstrip('.') + var_unit[var] + ' )$')
            
        exceptlist = ['__ncandidates__','__experiment__','__run__', '__event__','D0_isSignal','Dstarp_isSignal'] 
        if var in exceptlist:
            pass
        else:
            ax.set_xlim(data_merge_pd.min(), data_merge_pd.max())  
              

           
            
        plt.title(plot_title)
        plt.show()
        plt.clf()
        
        
    print(data_list.keys())
