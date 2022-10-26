#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
import sys
#import uproot
#from b2plot import hist
#import b2plot as bp
import ROOT
#from root_pandas import read_root

#import seaborn as sns
#try:
#    plt.style.use('belle2')
#plt.style.use('belle2_serif')
#plt.style.use('belle2_modern')
#except OSError:
#    print("Please install belle2 matplotlib style")   

#print(plt.style.available)


# In[2]:


from ROOT import TLorentzVector, TObject




from ROOT import Math, TFile
from array import array 


input_path = sys.argv[1]
#input_path = '/group/belle/users/jaeyoung/storage/01_recon/omega/test_dalitz_omega.root'

myfile = TFile(input_path, 'update')
mytree = myfile.omega



omega_Pip_px = array('d',[0])
omega_Pip_py = array('d',[0])
omega_Pip_pz = array('d',[0])
omega_Pip_E = array('d',[0])
omega_Pip_p = array('d',[0])

omega_Pim_px = array('d',[0])
omega_Pim_py = array('d',[0])
omega_Pim_pz = array('d',[0])
omega_Pim_E = array('d',[0])
omega_Pim_p = array('d',[0])

Pi0_px = array('d',[0])
Pi0_py = array('d',[0])
Pi0_pz = array('d',[0])
Pi0_E = array('d',[0])
Pi0_p = array('d',[0])

cos_dalitz_pip = array('d',[0])
cos_dalitz_pim = array('d',[0])


gamma_px = array('d',[0])
gamma_py = array('d',[0])
gamma_pz = array('d',[0])
gamma_E = array('d',[0])
gamma_p = array('d',[0])


D0_px = array('d',[0])
D0_py = array('d',[0])
D0_pz = array('d',[0])
D0_E = array('d',[0])
D0_p = array('d',[0])

cos_hel = array('d',[0])

branch_Pip_px = mytree.Branch('boosted_Pip_px', omega_Pip_px, 'boosted_Pip_px/D')
branch_Pip_py = mytree.Branch('boosted_Pip_py', omega_Pip_py, 'boosted_Pip_py/D')
branch_Pip_pz = mytree.Branch('boosted_Pip_pz', omega_Pip_pz, 'boosted_Pip_pz/D')
branch_Pip_E = mytree.Branch('boosted_Pip_E', omega_Pip_E, 'boosted_Pip_E/D')
branch_Pip_p = mytree.Branch('boosted_Pip_p', omega_Pip_p, 'boosted_Pip_p/D')

branch_Pim_px = mytree.Branch('boosted_Pim_px', omega_Pim_px, 'boosted_Pim_px/D')
branch_Pim_py = mytree.Branch('boosted_Pim_py', omega_Pim_py, 'boosted_Pim_py/D')
branch_Pim_pz = mytree.Branch('boosted_Pim_pz', omega_Pim_pz, 'boosted_Pim_pz/D')
branch_Pim_E = mytree.Branch('boosted_Pim_E', omega_Pim_E, 'boosted_Pim_E/D')
branch_Pim_p = mytree.Branch('boosted_Pim_p', omega_Pim_p, 'boosted_Pim_p/D')

branch_Pi0_px = mytree.Branch('boosted_Pi0_px', Pi0_px, 'boosted_Pi0_px/D')
branch_Pi0_py = mytree.Branch('boosted_Pi0_py', Pi0_py, 'boosted_Pi0_py/D')
branch_Pi0_pz = mytree.Branch('boosted_Pi0_pz', Pi0_pz, 'boosted_Pi0_pz/D')
branch_Pi0_E = mytree.Branch('boosted_Pi0_E', Pi0_E, 'boosted_Pi0_E/D')
branch_Pi0_p = mytree.Branch('boosted_Pi0_p', Pi0_p, 'boosted_Pi0_p/D')

branch_cos_dalitz_pip = mytree.Branch('cos_dalitz_pip', cos_dalitz_pip, 'cos_dalitz_pip/D')
branch_cos_dalitz_pim = mytree.Branch('cos_dalitz_pim', cos_dalitz_pip, 'cos_dalitz_pim/D')


branch_gamma_px = mytree.Branch('boosted_gamma_px', gamma_px, 'boosted_gamma_px/D')
branch_gamma_py = mytree.Branch('boosted_gamma_py', gamma_py, 'boosted_gamma_py/D')
branch_gamma_pz = mytree.Branch('boosted_gamma_pz', gamma_pz, 'boosted_gamma_pz/D')
branch_gamma_E = mytree.Branch('boosted_gamma_E', gamma_E, 'boosted_gamma_E/D')
branch_gamma_p = mytree.Branch('boosted_gamma_p', gamma_p, 'boosted_gamma_p/D')


branch_D0_px = mytree.Branch('boosted_D0_px', D0_px, 'boosted_D0_px/D')
branch_D0_py = mytree.Branch('boosted_D0_py', D0_py, 'boosted_D0_py/D')
branch_D0_pz = mytree.Branch('boosted_D0_pz', D0_pz, 'boosted_D0_pz/D')
branch_D0_E = mytree.Branch('boosted_D0_E', D0_E, 'boosted_D0_E/D')
branch_D0_p = mytree.Branch('boosted_D0_p', D0_p, 'boosted_D0_p/D')

branch_cos_hel = mytree.Branch('boosted_chs_hel', cos_hel, 'boosted_cos_hel/D')

data = []
data2 =[]
for entry in mytree:

	Pip_px = entry.omega_Pip_px
	Pip_py = entry.omega_Pip_py
	Pip_pz = entry.omega_Pip_pz
	Pip_E = entry.omega_Pip_E

	Pim_px = entry.omega_Pim_px
	Pim_py = entry.omega_Pim_py
	Pim_pz = entry.omega_Pim_pz
	Pim_E = entry.omega_Pim_E

	v_Pi0_px = entry.Pi0_px
	v_Pi0_py = entry.Pi0_py
	v_Pi0_pz = entry.Pi0_pz
	v_Pi0_E = entry.Pi0_E

	v_gamma_px = entry.gamma_px
	v_gamma_py = entry.gamma_py
	v_gamma_pz = entry.gamma_pz
	v_gamma_E = entry.gamma_E

	v_D0_px = entry.D0_px
	v_D0_py = entry.D0_py
	v_D0_pz = entry.D0_pz
	v_D0_E = entry.D0_E

	VecPip = Math.LorentzVector('ROOT::Math::PxPyPzE4D<double>')(Pip_px, Pip_py, Pip_pz, Pip_E)
	VecPim = Math.LorentzVector('ROOT::Math::PxPyPzE4D<double>')(Pim_px, Pim_py, Pim_pz, Pim_E)
	VecPi0 = Math.LorentzVector('ROOT::Math::PxPyPzE4D<double>')(v_Pi0_px, v_Pi0_py, v_Pi0_pz, v_Pi0_E)
	Vecgamma = Math.LorentzVector('ROOT::Math::PxPyPzE4D<double>')(v_gamma_px, v_gamma_py, v_gamma_pz, v_gamma_E)
	VecD0 = Math.LorentzVector('ROOT::Math::PxPyPzE4D<double>')(v_D0_px, v_D0_py, v_D0_pz, v_D0_E)

	frame = VecPip + VecPim + VecPi0
	cm = frame.BoostToCM()

	boostedPip = ROOT.Math.VectorUtil.boost(VecPip, cm)
	boostedPim = ROOT.Math.VectorUtil.boost(VecPim, cm)
	boostedPi0 = ROOT.Math.VectorUtil.boost(VecPi0, cm)
	boostedgamma = ROOT.Math.VectorUtil.boost(Vecgamma, cm)
	boostedD0    = ROOT.Math.VectorUtil.boost(VecD0, cm)


	#print((boostedPip.Px()*boostedPi0.Px()+boostedPip.Py()*boostedPi0.Py()+boostedPip.Pz()*boostedPi0.Pz() ) / (boostedPip.P() * boostedPi0.P()) )
	#data.append((boostedPip.Px()*boostedPi0.Px()+boostedPip.Py()*boostedPi0.Py()+boostedPip.Pz()*boostedPi0.Pz() ) / (boostedPip.P() * boostedPi0.P()) )
	#data2.append((boostedPim.Px()*boostedPi0.Px()+boostedPim.Py()*boostedPi0.Py()+boostedPim.Pz()*boostedPi0.Pz() ) / (boostedPim.P() * boostedPi0.P()) )


	omega_Pip_px[0] = boostedPip.Px()
	branch_Pip_px.Fill()
	omega_Pip_py[0] = boostedPip.Py()
	branch_Pip_py.Fill()
	omega_Pip_pz[0] = boostedPip.Pz()
	branch_Pip_pz.Fill()
	omega_Pip_E[0] = boostedPip.E()
	branch_Pip_E.Fill()
	omega_Pip_p[0] = boostedPip.P()
	branch_Pip_p.Fill()

	omega_Pim_px[0] = boostedPim.Px()
	branch_Pim_px.Fill()
	omega_Pim_py[0] = boostedPim.Py()
	branch_Pim_py.Fill()
	omega_Pim_pz[0] = boostedPim.Pz()
	branch_Pim_pz.Fill()
	omega_Pim_E[0] = boostedPim.E()
	branch_Pim_E.Fill()
	omega_Pim_p[0] = boostedPim.P()
	branch_Pim_p.Fill()

	Pi0_px[0] = boostedPi0.Px()
	branch_Pi0_px.Fill()
	Pi0_py[0] = boostedPi0.Py()
	branch_Pi0_py.Fill()
	Pi0_pz[0] = boostedPi0.Pz()
	branch_Pi0_pz.Fill()
	Pi0_E[0] = boostedPi0.E()
	branch_Pi0_E.Fill()
	Pi0_p[0] = boostedPi0.P()
	branch_Pi0_p.Fill() 

	cos_dalitz_pip[0] =    (boostedPip.Px()*boostedPi0.Px() + boostedPip.Py()*boostedPi0.Py() + boostedPip.Pz()*boostedPi0.Pz())/(boostedPip.P()*boostedPi0.P())
	branch_cos_dalitz_pip.Fill()
	cos_dalitz_pim[0] =    (boostedPim.Px()*boostedPi0.Px() + boostedPim.Py()*boostedPi0.Py() + boostedPim.Pz()*boostedPi0.Pz())/(boostedPim.P()*boostedPi0.P())
	branch_cos_dalitz_pim.Fill()

	gamma_px[0] = boostedgamma.Px()
	branch_gamma_px.Fill()
	gamma_py[0] = boostedgamma.Py()       
	branch_gamma_py.Fill()
	gamma_pz[0] = boostedgamma.Pz()       
	branch_gamma_pz.Fill()
	gamma_E[0] = boostedgamma.E()       
	branch_gamma_E.Fill()
	gamma_p[0] = boostedgamma.P()       


	D0_px[0] = boostedD0.Px()       
	branch_D0_px.Fill()
	D0_py[0] = boostedD0.Py()       
	branch_D0_py.Fill()
	D0_pz[0] = boostedD0.Pz()       
	branch_D0_pz.Fill()
	D0_E[0] = boostedD0.E()       
	branch_D0_E.Fill()
	D0_p[0] = boostedD0.P()       
	branch_D0_p.Fill()

	omega_Pim_vec = ROOT.TVector3( boostedPim.Px(), boostedPim.Py() , boostedPim.Pz())
	omega_Pip_vec = ROOT.TVector3( boostedPip.Px(), boostedPip.Py() , boostedPip.Pz())
	#omega_Pim_vec = ROOT.vector("double")([ boostedPim.Px(), boostedPim.Py() , boostedPim.Pz()])
	#omega_Pip_vec = ROOT.vector("double")([ boostedPip.Px(), boostedPip.Py() , boostedPip.Pz()])
	print(omega_Pim_vec)

	normal_vec = omega_Pim_vec.Cross(omega_Pip_vec)
	#normal_vec = ROOT.vector("double")
	#normal_vec = ROOT.Math.Cross(omega_Pim_vec, omega_Pip_vec) 
	gamma_vec  = ROOT.TVector3( boostedgamma.Px(),boostedgamma.Py(), boostedgamma.Pz())

	omega_cosHel = normal_vec.Dot(gamma_vec)
	cos_hel[0] = omega_cosHel
	branch_cos_hel.Fill()

myfile.Write("",TObject.kOverwrite)
myfile.Close()



