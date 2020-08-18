#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 04:57:33 2020

@author: gracexie
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 16:54:04 2020

@author: gracexie
"""

import uproot
#from pylab import *
import matplotlib.pyplot as plt
#import pandas as pd
import scipy.constants as const
import numpy as np

me = const.value('electron mass energy equivalent in MeV')*1e-3

def invariant_m(pt, eta, phi):
    
    px1 = pt[0] * np.cos(phi[0])
    px2 = pt[1] * np.cos(phi[1])
    px = px1 + px2

            
    py1 = pt[0] * np.sin(phi[0])
    py2 = pt[1] * np.sin(phi[1])
    py = py1 + py2
            
            
    pz1 = pt[0] * np.sinh(eta[0])
    pz2 = pt[1] * np.sinh(eta[1])
    pz = pz1 + pz2
            
    p1_sq = px1**2 + py1**2 + pz1**2
    p2_sq = px2**2 + py2**2 + pz2**2
            
    E1 = np.sqrt(me**2 + p1_sq)
    E2 = np.sqrt(me**2 + p2_sq)
            
    p_sq = px**2 + py**2 + pz**2
            
    E_sq = (E1+E2)**2
            
    m = np.sqrt(E_sq-p_sq)
    
    return m

def reorder(pt, eta, phi):
    
    pt_new = []
    eta_new = []
    phi_new = []
    
    a = pt.argmax()
    pt_new.append(pt[a])
    eta_new.append(eta[a])
    phi_new.append(phi[a])
    np.delete(pt, a)
    np.delete(eta, a)
    np.delete(phi, a)

    
    b = pt.argmax()
    pt_new.append(pt[b])
    eta_new.append(eta[b])
    phi_new.append(phi[b])
    
    return pt_new, eta_new, phi_new
    
    
    


fileName = "/Users/gracexie/Documents/Northwestern/CMS/from_server/tag_1_delphes_events.root"
file = uproot.open(fileName)
#all_ttrees = dict(file.allitems(filterclass=lambda cls: issubclass(cls, uproot.tree.TTreeMethods)))
#print(all_ttrees)
#print(file)
events = uproot.open(fileName)["Delphes"]
#print(events.keys())
#print(events['Electron_size'].keys())
#[b'Event', b'Event_size', b'Particle', b'Particle_size', b'Track', b'Track_size', b'Tower', b'Tower_size', b'EFlowTrack', b'EFlowTrack_size', b'EFlowPhoton', b'EFlowPhoton_size', b'EFlowNeutralHadron', b'EFlowNeutralHadron_size', b'GenJet', b'GenJet_size', b'GenMissingET', b'GenMissingET_size', b'Jet', b'Jet_size', b'Electron', b'Electron_size', b'Photon', b'Photon_size', b'Muon', b'Muon_size', b'FatJet', b'FatJet_size', b'MissingET', b'MissingET_size', b'ScalarHT', b'ScalarHT_size']

z_mass = []
features = ['Electron.PT','Electron.Eta','Electron.Phi']
for data in events.iterate(features, namedecode="utf-8"):
    
    pt_list = data['Electron.PT']
    eta_list = data['Electron.Eta']
    phi_list = data['Electron.Phi']
    
    
   
    for i in range(len(pt_list)):
        
        if len(pt_list[i]) >= 2:
            
            pt, eta, phi = reorder(pt_list[i], eta_list[i], phi_list[i])
            m = invariant_m(pt, eta, phi)
            z_mass.append(m)
            
            
            
plt.hist(z_mass, bins = 200)

plt.show()            
#            
#            
#            
#            
#
#

            
            
        
   