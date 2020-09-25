# Lab 5 - Linear oscillations and forces (routine)

### Name: 

### Lab section:

#Necessary imports
import numpy as np #package for work with arrays and matrices
import matplotlib.pyplot as plt #package with plotting capabilities
from scipy.integrate import odeint

### Assignment Overview:


In this week's lab, you will use ode solutions to investigate linear oscillator models. In part 1, you will see models of a simple harmonic oscillator and in part 2, you will add damping and analyze the resulting dynamics. You will need to modify and use the code given to you in lab 4 to solve the second-order ODEs. 

**Part 1: Harmonic oscillator**

We saw in class that we can write the 2nd order harmonic oscillator ODE 

$$m \ddot x  = -k x $$

as two 1st order ODEs (setting mass to 1):

$$ dy/dt = -k x $$
$$ dx/dt = y $$

Take the code for definingn and solving ODE from part 2 of lab 4 and modify it to represent the harmonic oscillator ODE above (remember to change all the parameters to match the ones used in this ODE.)  Use the code from lab 4 as a template to do these tasks with the following parameters: 

 - Calulate the eigenvalues of the defining matrix of the 2-variable ODE, and classify the dynamics of the solutions 
 - Make a phase plane plot for a harmonic oscillator and plot four solution rajectories, starting at different initial values (use a for loop, like you did in lab 4)
 - Plot the solutions for displacement and velocity as a function of time and report the period of oscillations.
 
**Important hint:** If your ODE function has only one parameter, e.g. k; in order for the args input to work in the odeint function call, you need to turn it into a tuple, e.g. args = (k,)

**Q1.1:** set $k = \pi^2$



**Q1.2:** set $k = 4*\pi^2$



**Q1.3:** set $k = 0.25*\pi^2$



**Q1.4:** Based on your observations, determine the value of k that would produce oscillations with period 5. Repeat the same calculations performed above and confirm the period by the plots of the solutions over time.



### Part 2: Damped harmonic oscillator
For an oscillator with a frictional force which acts in the opposite direction of motion with a constant b, we get the following equation:
 $$ dy/dt = -kx -by$$
 $$ dx/dt = y $$

Use the code from lab 4 as a template to do these tasks with the following parameters: 

 - Calulate the eigenvalues of the defining matrix of the 2-variable ODE, and classify the dynamics of the solutions 
 - Make a phase plane plot for a harmonic oscillator and plot four solution rajectories, starting at different initial values (use a for loop, like you did in lab 4)
 - Plot the solutions for displacement and velocity as a function of time and report the period of oscillations.

**Q2.1:** Set $k = \pi^2$ and choose a value of b so that the oscillator is *underdamped*. 



**Q2.2:** Set $k = \pi^2$ and choose a value of b so that the oscillator is  *overdamped*. 



**Q2.3:** Set $k = \pi^2$ and choose a value of b so that the oscillator is *critically damped*. 



**Q2.4:** Set $k = 4* \pi^2$ and choose a value of b so that the oscillator is *underdamped*. 



**Q2.5:** Set $k = 4* \pi^2$ and choose a value of b so that the oscillator is  *overdamped*. 



**Q2.6:** $k = 4* \pi^2$ and choose a value of b so that the oscillator is critically damped.



### Rubric:

**Part 1:** 
3 pts per question: eigenvalues, phase plane, time plot

**Part 2:** 
3 pts per question: eigenvalues, phase plane, time plot

**Total: 30 pts**
