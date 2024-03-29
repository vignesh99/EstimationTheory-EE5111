# -*- coding: utf-8 -*-
"""EE5111 Take home.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SzZZV9mNu_RYG76EPlRTOtQSUO4HOV1Z
"""

#Import libraries
from pylab import *
import random as rn
from scipy.stats import norm

#Demand plots
                                    #Buying
X = np.arange(-50,50.25,0.25)
g1 = norm.pdf(X,loc=-12,scale=12)
g1 = g1/sum(g1)
g2 = norm.pdf(X,loc=20,scale=16)
g2 = g2/sum(g2)

plt.plot(X,g1,"b",label="High R value")
plt.plot(X,g2,"r",label="Low R value")
plt.grid()
plt.title("Demand for stock buying")
plt.ylabel("P(d|r) (prbability density)")
plt.xlabel("D|R=r (demand given revenue)")
plt.legend()
plt.show()

                                    #Selling
X = np.arange(-50,50.25,0.25)
g1 = norm.pdf(X,loc=-10,scale=5)
g1 = g1/sum(g1)
g2 = norm.pdf(X,loc=15,scale=7)
g2 = g2/sum(g2)

plt.plot(X,g2,"b",label="High R value")
plt.plot(X,g1,"r",label="Low R value")
plt.grid()
plt.title("Demand for stock Selling")
plt.ylabel("P(d|r) (prbability density)")
plt.xlabel("D|R=r (Demand given revenue)")
plt.legend()
plt.show()

#Gossip curves
                                    #Unerliable source
X = np.arange(-50,50.25,0.25)
g1 = norm.pdf(X,loc=-2,scale=15)    #Gossip
g1 = g1/sum(g1)
g2 = norm.pdf(X,loc=20,scale=16)     #High-demand curve (low R)
g2 = g2/sum(g2)
g = g1*g2
g = g/sum(g)

plt.plot(X,g1,"g",label="Gossip price prediction")
plt.plot(X,g,"b",label="Likelihood")
plt.grid()
plt.vlines(12,0,g1[np.where(X==12)[0]],linestyles="dashed",colors="g",label="Gossip revenue")
plt.vlines(2,0,g1[np.where(X==2)[0]],linestyles="dashed",colors="r",label="True revenue")
plt.title("Gossip price for unreliable source")
plt.ylabel("P(g|r) (prbability density)")
plt.xlabel("G|R=r (Gossip price given revenue)")
plt.legend()
plt.show()

                                    #Reliable source
X = np.arange(-50,50.25,0.25)
g1 = norm.pdf(X,loc=15,scale=7)     #Demand-high curve (high R)
g1 = g1/sum(g1)
g2 = norm.pdf(X,loc=25,scale=7)     #Current gossip
g2 = g2/sum(g2)
g3 = norm.pdf(X,loc=-2,scale=8)      #Future gossip
g3 = g3/sum(g3)
g = g1*g2
g = g/sum(g)

plt.plot(X,g2,"g",label="Current gossip prediction")
plt.plot(X,g3,"r",label="Future gossip prediction")
plt.plot(X,g,"b",label="Current Likelihood")
plt.vlines(24,0,g2[np.where(X==24)[0]],linestyles="dashed",colors="g",label="Gossip revenue")
plt.vlines(27,0,g2[np.where(X==27)[0]],linestyles="dashed",colors="r",label="True revenue")
plt.grid()
plt.title("Gossip price for reliable source")
plt.ylabel("P(g|r) (prbability density)")
plt.xlabel("G|R=r (Gossip price given revenue)")
plt.legend()
plt.show()

#Prior curves
                                    #Volatile buying
X = np.arange(-50,50.25,0.25)
g1 = norm.pdf(X,loc=-16,scale=7)
g1 = g1/sum(g1)
g2 = norm.pdf(X,loc=20,scale=9)
g2 = g2/sum(g2)
h = g1+g2
h = h/sum(h)

plt.plot(X,h,"b")
plt.grid()
plt.title("Prior for volatile stock (GMM)")
plt.ylabel("$\pi(r)$ (prbability density)")
plt.xlabel("$r_{\pi}$ (prior revenue)")
plt.show()

                                    #Non-volatile selling
X = np.arange(-50,50.25,0.25)
g1 = norm.pdf(X,loc=0,scale=7)
g1 = g1/sum(g1)
g2 = norm.pdf(X,loc=16,scale=9)
g2 = g2/sum(g2)

plt.plot(X,g1,"r",label="Future prior")
plt.plot(X,g2,"g",label="Current prior")
plt.grid()
plt.title("Prior for non-volatile stock")
plt.ylabel("$\pi(r)$ (prbability density)")
plt.xlabel("$r_{\pi}$ (prior revenue)")
plt.legend()
plt.show()

X = np.arange(-50,50.25,0.25)
g1 = norm.pdf(X,loc=-2,scale=15)    #Gossip
g1 = g1/sum(g1)
g2 = norm.pdf(X,loc=20,scale=16)     #High-demand curve (low R)
g2 = g2/sum(g2)
g = g1*g2
g = g/sum(g)
g1 = norm.pdf(X,loc=-16,scale=7)
g1 = g1/sum(g1)
g2 = norm.pdf(X,loc=20,scale=9)
g2 = g2/sum(g2)
h = g1+g2
h = h/sum(h)
f = g*h
f = f/sum(f)
rth = 5
indRth = np.where(X==rth)[0][0]

plt.plot(X,f,"b",label="Psoterior R|E")
plt.plot(X,h,"g",label="Prior R")
plt.grid()
plt.title("Posterior curve")
plt.ylabel("$P_{R|E}$ (prbability density)")
plt.xlabel("$R|E$ (posterior revenue)")
plt.vlines(rth,0,f[indRth],linestyles="dashed",colors="r",label="$r_{th}$")
plt.fill_between(X[indRth:],f[indRth:],color="orange")
plt.legend()
plt.show()

                                    #Selling posterior
X = np.arange(-50,50.25,0.25)
g1 = norm.pdf(X,loc=15,scale=7)     #Demand-high curve (high R)
g1 = g1/sum(g1)
g2 = norm.pdf(X,loc=25,scale=7)     #Current gossip
g2 = g2/sum(g2)
g = g1*g2
g = g/sum(g)
f = norm.pdf(X,loc=16,scale=9)
f = f/sum(f)
h = f*g
h = h/sum(h)
rth = 5
indRth = np.where(X==rth)[0][0]

plt.subplot(211)
plt.plot(X,f,"b",label="Psoterior R|E")
plt.plot(X,h,"g",label="Prior R")
plt.grid()
plt.title("Posterior curve for current (above) and future (below)")
plt.vlines(rth,0,f[indRth],linestyles="dashed",colors="r",label="$r_{th}$")
plt.fill_between(X[indRth:],f[indRth:],color="orange")
plt.legend()

g1 = norm.pdf(X,loc=15,scale=7)     #Demand-high curve (high R)
g1 = g1/sum(g1)
g2 = norm.pdf(X,loc=-2,scale=8)      #Future gossip
g2 = g2/sum(g2)
g = g1*g2
g = g/sum(g)
f = norm.pdf(X,loc=0,scale=7)
f = f/sum(f)
h = f*g
h = h/sum(h)
rth = 5
indRth = np.where(X==rth)[0][0]

plt.subplot(212)
plt.plot(X,f,"b",label="Psoterior R|E")
plt.plot(X,h,"g",label="Prior R")
plt.grid()
plt.ylabel("$P_{R|E}$ (prbability density)")
plt.xlabel("$R|E$ (posterior revenue)")
plt.vlines(rth,0,f[indRth],linestyles="dashed",colors="r",label="$r_{th}$")
plt.fill_between(X[indRth:],f[indRth:],color="orange")
plt.legend()

plt.show()

