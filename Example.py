'''
Example run of FunctionalNetwork
@ Frankie Yeung (2021 May)

1. load spike time stamps
2. FNCCH reconstruction
3. filter unphysical reconstructions
'''
import FunctionalNetwork as fn
w = 200
n = fn.FunctionalNetwork('DIV25_spks.txt')
n.reconstruct(w=w)
n.applyPhysicalFilter(w=w,deltaT=1/7.06,deltaD=42,tThres=1,vThres=400)
