# Lab 7 -  Act locally: linearize!

### Name: 
### Lab section:

#Necessary imports
import numpy as np #package for work with arrays and matrices
import matplotlib.pyplot as plt #package with plotting capabilities
from scipy.integrate import ode #ode solver package

### Assignment Overview:

In this lab, we will *linearize*  nonlinear systems and classify the dynamics near the fixed points. To do this, we use the Jacobian matrix to define a linear system to approximate the dynamics of the nonlinear system in the neighborhood of a fixed point. This allows us to classify the flow around the fixed point using the eigenvectors and eigenvalues of the Jacobian.

Here is what you will need to do for each of the models given below:

1.  Find the nullclines and the fixed points of the ODE on paper for the specified parameter values and compute the Jacobian matrix for each fixed point using the specified parameter values (this is also a part of the problem set for this week). Write down the results in your answer. Compute the eigenvalues and of the Jacobian with the specified parameter values using python code and classify the flow around each fixed point in your answer.

2. Plot the phase portrait of the ODE (using the code from lab 5), and set the size of the window so that your plot includes all the fixed points. Overlay the nullcline plots onto the phase portrait using different colors for different types of nullcline. (Hint: you'll need to create two vectors of "x" and "y" coordinates for each nullcline to plot them.) 

3. Use the same code from lab 5 to create a *local* plot of the flow around each fixed point (e.g. using window size of +/- 0.1 in each direction around the fixed point) and compare its appearance with the classification based on the Jacobian in your answer. (Describe whether the flow converges or diverge from the fixed point, whether there is rotation/oscillations in the flow, etc.)



**Part 1: Competition between species**

Two species (figuratively called sheep and rabbits) occupy the same ecological niche and compete with each other. This is represented by the following model:

$$ dS/dt = S*(a-S-b*R) $$
$$ dR/dt = R*(c-R-d*S) $$


**Q1.1:**  use a=2; b=1; c=3; d=2

#your code goes here

(your written answer goes here)

**Q1.2:** use a=2; b=0.5; c=3; d=1

#your code goes here

(your written answer goes here)

### Part 2: Symbiotic relationship between species:
A model for two species that interact in a mutually beneficial manner.  Species X dies out in the absence of species Y, while species Y reaches a carrying capacity in the absence of species X:

$$  dX/dt = -a*X + b*X*Y $$
$$  dY/dt = c*Y*(1-Y) + d*X*Y $$

**Q2.1:** use a=1, b=2, c=1, d=3

#your code goes here

(your written answer goes here)

**Q2.2:** use a=2, b=1, c=1, d=2

#your code goes here

(your written answer goes here)

### Lotka-Volterra predator-prey model:
The following famous model describes dynamics of two species, one of which preys on the other. Assume the prey grows without bound without the predator, and the predators die without the prey. The interaction of predators and prey has a positive effect on the predators, and a negative effect on the prey:

$$   dP/dt = -d*P + a*P*R $$
$$   dR/dt = c*R - b*P*R $$

**Q3.1** use c=2; d=5; a=0.5; b=0.4

#your code goes here

(your written answer goes here)

**Q3.2** use c=10; d=5; a=0.5; b=0.4

#your code goes here

(your written answer goes here)

### Rubric:

**Part 1:** 
6 pts per question (2 pts per task)

**Part 2:** 
6 pts per question (2 pts per task)

**Part 3:**
6 pts per question (2 pts per task)

**Total: 36 pts**