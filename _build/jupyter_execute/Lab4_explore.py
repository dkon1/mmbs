# Lab 4 - Explore linear models of romantic relationships

### Name: 
### Lab section:

#Necessary imports
import numpy as np #package for work with arrays and matrices
import matplotlib.pyplot as plt #package with plotting capabilities
from scipy.integrate import odeint

Suppose person $R$ and person $J$ are in a romantic relationship and their
feelings (positive or negative) are described by the system of linear ODEs:

$$
dR/dt = a*R + b*J \\
dJ/dt = c*R + d*J
$$

in which $a$ and $d$ are the self-awareness parameters and $b$ and $c$ are the
parameters of responsiveness to the other. 

Suppose $R$ and $J$ are both totally and identically self-absorbed, that is $a=d$ and $b=c=0$. Investigate the dynamics of the model under these conditions, and plot solutions separately for positive self-awareness ($a=d >0$) and for negative self-awareness ($a = d <0$). Describe verbally the predicted fate of the relationship.

#your code goes here

(your written answer goes here)

Suppose $R$ and $J$ are again identical, but now they are totally not self-aware that is $a=d=0$ and identically responsive to each other $b=c$. Investigate the dynamics of the model under these conditions, and plot solutions separately for positive responsiveness($b = c >0$) and for negative responsiveness ($b = c <0$). Describe verbally the predicted fate of the relationship.

#your code goes here

(your written answer goes here) 

Suppose $R$ and $J$ are instead polar opposites, with $a= - d$ and $b = -c$. Investigate the dynamics of the model under these conditions for different parameter values and report all possible relationship dynamics that are possible, with plots and explanations for each scenario.

#your code goes here

(your written answer goes here)