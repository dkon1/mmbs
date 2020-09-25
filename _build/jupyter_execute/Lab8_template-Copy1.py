# Lab 8 - limit cycles and bifurcations

### Name: 
### Lab section:

#Necessary imports
import numpy as np #package for work with arrays and matrices
import matplotlib.pyplot as plt #package with plotting capabilities
from scipy.integrate import ode #ode solver package

### Assignment Overview:

We learned about limit cycles, which are isolated closed orbits in the phase plane. The Poincare-Bendixson (PB) theorem states that "a region of the plane which contains a single unstable fixed point, and for which the direction of the flow everywhere on the boundary is inward, must contain a limit cycle." In today's lab, you will use the theorem to analyze the FitzHugh Nagumo (FHN) model. 

First, a quick summary of action potential dynamics. In the simplest terms, for a resting neuron there is a resting membrane potential at which level the neuron is 'quiet' (i.e., the inward and outward currents are balanced). This potential is negative, which means that there is more negative charge inside the neuron than outside. A neuron can be perturbed from its resting state by several mechanisms, the most classic of which is a depolarization in which the membrane potential decreases (i.e., the difference between the inside of the cell and outside of the cell decreases). If this depolarization reaches a certain 'threshold', then a cascade of events starts that will end up giving us the classical action potential. First, voltage gated $Na^+$ channels open, which allows the influx of $Na^+$ ions and the further depolarization of the neuron (this is the upstroke) that results in a positive feedback until the maximal number of $Na^+$ ion channels are open, at which point they enter an inactive period. This inactivation reduces the inward flow of $Na^+$ ions. The $K^+$ channels are now open, which allows an outward flow of positive charge. Both of these lead to the neuron repolarizing (the downstroke). Typically, the neuron will then enter a refractory period in which it may not be able to generate another action potential for some period. The classic Hodgkin-Huxley model takes all of these factors, and more, into account, which is one of the reasons it ends up being a system of four equations.

The FHN model has only two variables, which allows us to graph the system in the plane and thereby to visualize its properties. While it gives up biological realism, it still captures many of the dynamics of an action potential. In this lab you will also be asked to relate voltage traces (against time) to a phase portrait. 

The FHN is defined as:

$$    dV/dt = V(a-V)(V-1) - w + I $$
$$    dw/dt = bV - cw $$


 * $V$ mimics the membrane voltage
 * $w$ mimics the outward current; sometimes called the recovery variable
 * $a$ determines the shape of the cubic nullcline
 * $b$ and $c$  determine the kinetics of $w$ ($b>0, c>=0$)
 * $I$ is the injection current.

**Part 1: FHN model with no applied current**

Set the applied current $I$ to zero and analyze the FHN model with different parameter values by doing the following:

 1. Plot the *global* phase plane flow by picking a range that includes all the fixed points. Overlay the nullclines using different colors for the V-nullcline and the w-nullcline. 
 2. Solve the FHN ODE using the ode solver and plot 4 solution trajectories (with different initial conditions) on top of the phase plane portrait. Describe the behavior of the solution trajectories you plotted.
 3. Describe the global phase portrait by 1) noting all the fixed points and their stability; 2) noting the presence of trapping regions and limit cycles; 3) describing what happens for different solutions in the long run. 


**Q1.1:** Use $a=4; b=5; c=1; I=0$

#your code goes here

(your written answer goes here)

**Q1.2:** Keeping the other parameters the same, gradually decrease $b$ from 5 to 0 and describe the type of bifurcation that occurs and how it changes the global phase plan flow. Report (appoximately) the critical value of $b_c$, and do tasks 1 through 3 above for some value of $b$ below the critical value. Are oscillation possible for these parameters?

#your code goes here

(your written answer goes here)

### Part 2: FHN model with applied current
In this part you will experiment with increasing the applied current I in the model. Once again, do the following tasks:

 1. Plot the *global* phase plane flow by picking a range that includes all the fixed points. Overlay the nullclines using different colors for the V-nullcline and the w-nullcline. 
 2. Solve the FHN ODE using the ode solver and plot 4 solution trajectories (with different initial conditions) on top of the phase plane portrait. Describe the behavior of the solution trajectories you plotted.
 3. Describe the global phase portrait by 1) noting all the fixed points and their stability; 2) noting the presence of trapping regions and limit cycles; 3) describing what happens for different solutions in the long run. 

**Q2.1:** Starting with the same parameter values as in 1.1, increase the current $I$ gradually until you observe a bifurcation in the phase portrait. (Hint: you will need to adjust the limits of the phase plane window to see the change.) Report the critical value $I_c$ (approximately) at which this occurs and classify the bifurcation.  For a value $I$ above the critical value, do tasks 1 through 3 above. Are oscillation possible in this regime?

#your code goes here

(your written answer goes here)

**Q2.2:** Now increase $I$ further until you observe another bifurcation. Report the second critical value $I_{c2}$ (approximately) at which this occurs and classify the bifurcation.   For a value $I$ above the second critical value, do tasks 1 through 3 above. Are oscillation possible in this regime? 

#your code goes here

(your written answer goes here)

**Q2.3:**  For some set of parameter values that produce oscillatory dynamics, compare the solution trajectory and the plot of potential over time.  What part of the trajectory in the phase plane corresponds to the upstroke in the action potential (inward current)? What part corresponds to the downstroke (outward current)?

Use your code from the Fourier transform assignment to plot the power spectrum of the membrane potential solution that you produced and report the frequency peak you see. Vary the parameter $a$ (gradually, so that the oscillations are not destroyed) and describe whether it has an effect on the frequency of the oscillations in the power spectrum. Do the same for applied current $I$ (again, change it gradually in both directions) and report whether and how it affects the frequency in the power spectrum.

#your code goes here

(your written answer goes here)

### Rubric:

**Part 1:** 

 1.1 6 pts (2 pts per task)
 
 1.2 8 pts (2 pts for bifurcation + 2 pts per task)

**Part 2:** 

2.1 8 pts (2 pts for bifurcation + 2 pts per task)

2.2 8 pts (2 pts for bifurcation + 2 pts per task)

2.2 8 pts (2 pts for answers about voltage plot + 2 pts per power spectrum analysis + 2 points for analysis of $a$ dependence + 2 pts for analysis of $I$ dependence)

**Total: 38 pts**