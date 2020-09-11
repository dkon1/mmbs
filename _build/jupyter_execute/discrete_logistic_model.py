## Logistic Growth: Plotting solutions for different parameter values
The second population model that we encountered this week was the logistic model, which is defined by the dynamic model 

$$N(t+1)=r(1-N(t))N(t)$$

# Import packages
import numpy as np # package for work with arrays and matrices
import matplotlib.pyplot as plt # package with plotting capabilities

**Q3.1:** For the logistic model with an initial population of 0.5 and $r=1.1$, 
compute the first 50 iterations using the same for loop iteration
you used above and plot the solution against time. 

numsteps = 50 #set number of iterations
r = 1.8 #set parameter
N = np.zeros(numsteps+1) #initialize solution vector
N[0]=.5 #initial value
t = range(numsteps+1) #initialze time vector
a = -10
for i in range(numsteps):
    N[i+1] = r*N[i]*(1-N[i]) #logistic population model
plt.plot(t,N) #plot solution
plt.xlabel('time')
plt.ylabel('population')
plt.title('Q3.1: Logistic growth')
plt.show()
 

**Q3.2:** Change the parameter $r$ to the following values: 0.5, 2.0, and 3.2,
and in each case plot the solutions against time in separate figures.
Describe each plot with a sentence.

numsteps = 50 #set number of iterations
r = .5 #set parameter
N = np.zeros(numsteps+1) #initialize solution vector
N[0]=.5 #initial value
t = range(numsteps+1) #initialze time vector
a = -10
for i in range(numsteps):
    N[i+1] = r*N[i]*(1-N[i]) #linear population model
plt.plot(t,N) #plot solution
plt.xlabel('time')
plt.ylabel('population')
plt.title('Q3.2: Logistic growth, r=0.5')
plt.show()

numsteps = 50 #set number of iterations
r = 2.0 #set parameter
N = np.zeros(numsteps+1) #initialize solution vector
N[0]=0.75 #initial value
t = range(numsteps+1) #initialze time vector
a = -10
for i in range(numsteps):
    N[i+1] = r*N[i]*(1-N[i]) #linear population model
plt.plot(t,N) #plot solution
plt.xlabel('time')
plt.ylabel('population')
plt.title('Q3.2: Logistic growth, r=2.0')
plt.show()

numsteps = 50 #set number of iterations
r = 3.2 #set parameter
N = np.zeros(numsteps+1) #initialize solution vector
N[0]=.5 #initial value
t = range(numsteps+1) #initialze time vector
a = -10
for i in range(numsteps):
    N[i+1] = r*N[i]*(1-N[i]) #linear population model
plt.plot(t,N) #plot solution
plt.xlabel('time')
plt.ylabel('population')
plt.title('Q3.2: Logistic growth, r=3.2')
plt.show()

Answer:
 - The solution for r=0.5 decreases to zero
 - The solution for r=2.0 stays at the fixed point of 0.5
 - The solution for r=3.2 oscillates between two values indefinitely

**Q3.3:** Increase the parameter $r$ further until you see strange, aperiodic 
behavior called chaos. Report at least one value of $r$ at which you see
chaotic dynamics.

numsteps = 100 #set number of iterations
r = 3.7 #set parameter
N = np.zeros(numsteps+1) #initialize solution vector
N[0]=.7 #initial value
t = range(numsteps+1) #initialze time vector
a = -10
for i in range(numsteps):
    N[i+1] = r*N[i]*(1-N[i]) #linear population model
plt.plot(t, N, label = 'N0 =' + str(N[0]))

numsteps = 100 #set number of iterations
r = 3.7 #set parameter
N = np.zeros(numsteps+1) #initialize solution vector
N[0]=.701 #initial value
t = range(numsteps+1) #initialze time vector
a = -10
for i in range(numsteps):
    N[i+1] = r*N[i]*(1-N[i]) #linear population model
plt.plot(t,N, label = 'N0 =' + str(N[0])) #plot solution

plt.xlabel('time')
plt.ylabel('population')
plt.title('Q3.3: Logistic growth, r=3.7')
plt.legend()
plt.show()

Answer: At r=3.7 the solution bounces around without any apparent pattern, which is called chaos.