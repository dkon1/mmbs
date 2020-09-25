# Lab 4 - Linear ODEs in the plane (routine)
### Solutions

#Necessary imports
import numpy as np #package for work with arrays and matrices
import matplotlib.pyplot as plt #package with plotting capabilities
from scipy.integrate import odeint

## Part 1: Analysis through eigenvalues

For each of the six two-variable ODEs in problem set 4 do the following:

 - Produce a phase plane plot
 - Find the eigenvalues of the defining matrix and 
 - Classify the phase plane according to the eigenvalues.

**Q1.1:** matrix 1 from problem set 4

xmin = -1.5 #change the parameters here to control the range of the axes
xmax = 1.5
ymin = -1.5
ymax = 1.5
dx = 0.2 #set the size of the x-step on the grid
dy = 0.2 #set the size of the y-step on the grid
X = np.arange(xmin, xmax, dx)
Y = np.arange(ymin, ymax, dy)
x, y = np.meshgrid(X, Y);  #create a grid
    
#Define the functions that define the ODE in order to compute
#the flow vectors on that grid. Here is a linear example:
a = 1
b = 1
c = 4
d = -2
dx = a*x+b*y
dy = c*x+d*y

#Then plot the arrows given by arrays dx,dy at points x,y:
fig, ax = plt.subplots()
q = ax.quiver(x, y, dx, dy)
plt.xlabel('x') #use more informative labels for a real model
plt.ylabel('y')
plt.title('Q1.1: Phase plane')
plt.show()

    
#find the eigenvalues
A = np.array([[a, b], [c, d]])
evals, evecs = np.linalg.eig(A)
print(evals)
    

Answer: The eigenvalues and 2 and -3, which means the model has a saddle
point (at the origin).

**Q1.2:** matrix 2 from problem set 4

xmin = -1.5 #change the parameters here to control the range of the axes
xmax = 1.5
ymin = -1.5
ymax = 1.5
dx = 0.2 #set the size of the x-step on the grid
dy = 0.2 #set the size of the y-step on the grid
X = np.arange(xmin, xmax, dx)
Y = np.arange(ymin, ymax, dy)
x, y = np.meshgrid(X, Y);  #create a grid
    
#Define the functions that define the ODE in order to compute
#the flow vectors on that grid. Here is a linear example:
a = 2
b = 1
c = 1
d = 2
dx = a*x+b*y
dy = c*x+d*y

#Then plot the arrows given by arrays dx,dy at points x,y:
fig, ax = plt.subplots()
q = ax.quiver(x, y, dx, dy)
plt.xlabel('x') #use more informative labels for a real model
plt.ylabel('y')
plt.title('Q1.2: Phase plane')
plt.show()

    
#find the eigenvalues
A = np.array([[a, b], [c, d]])
evals, evecs = np.linalg.eig(A)
print(evals)

Answer: The eigenvalues are 1 and 3, which means the model has an ustable
node (at the origin).

**Q1.3:** matrix 3 from problem set 4

xmin = -1.5 #change the parameters here to control the range of the axes
xmax = 1.5
ymin = -1.5
ymax = 1.5
dx = 0.2 #set the size of the x-step on the grid
dy = 0.2 #set the size of the y-step on the grid
X = np.arange(xmin, xmax, dx)
Y = np.arange(ymin, ymax, dy)
x, y = np.meshgrid(X, Y);  #create a grid
    
#Define the functions that define the ODE in order to compute
#the flow vectors on that grid. Here is a linear example:
a = 1
b = 2
c = -2
d = -4
dx = a*x+b*y
dy = c*x+d*y

#Then plot the arrows given by arrays dx,dy at points x,y:
fig, ax = plt.subplots()
q = ax.quiver(x, y, dx, dy)
plt.xlabel('x') #use more informative labels for a real model
plt.ylabel('y')
plt.title('Q1.3: Phase plane')
plt.show()

    
#find the eigenvalues
A = np.array([[a, b], [c, d]])
evals, evecs = np.linalg.eig(A)
print(evals)

Answer: The eigenvalues and 0 and -3, which means there is a line of fixed
points corresponding to the eigenvector with 0 eigenvalue, and all
solutions approach it  

**Q1.4:** matrix 4 from problem set 4

xmin = -1.5 #change the parameters here to control the range of the axes
xmax = 1.5
ymin = -1.5
ymax = 1.5
dx = 0.2 #set the size of the x-step on the grid
dy = 0.2 #set the size of the y-step on the grid
X = np.arange(xmin, xmax, dx)
Y = np.arange(ymin, ymax, dy)
x, y = np.meshgrid(X, Y);  #create a grid
    
#Define the functions that define the ODE in order to compute
#the flow vectors on that grid. Here is a linear example:
a = -2
b = 1
c = 3
d = -4
dx = a*x+b*y
dy = c*x+d*y

#Then plot the arrows given by arrays dx,dy at points x,y:
fig, ax = plt.subplots()
q = ax.quiver(x, y, dx, dy)
plt.xlabel('x') #use more informative labels for a real model
plt.ylabel('y')
plt.title('Q1.4: Phase plane')
plt.show()

    
#find the eigenvalues
A = np.array([[a, b], [c, d]])
evals, evecs = np.linalg.eig(A)
print(evals)

Answer: The eigenvalues and -1 and -5, which means the model is a stable node (at
the origin)

**Q1.5:** matrix 5 from problem set 4

xmin = -1.5 #change the parameters here to control the range of the axes
xmax = 1.5
ymin = -1.5
ymax = 1.5
dx = 0.2 #set the size of the x-step on the grid
dy = 0.2 #set the size of the y-step on the grid
X = np.arange(xmin, xmax, dx)
Y = np.arange(ymin, ymax, dy)
x, y = np.meshgrid(X, Y);  #create a grid
    
#Define the functions that define the ODE in order to compute
#the flow vectors on that grid. Here is a linear example:
a = 5
b = 10
c = -1
d = -1
dx = a*x+b*y
dy = c*x+d*y

#Then plot the arrows given by arrays dx,dy at points x,y:
fig, ax = plt.subplots()
q = ax.quiver(x, y, dx, dy)
plt.xlabel('x') #use more informative labels for a real model
plt.ylabel('y')
plt.title('Q1.5: Phase plane')
plt.show()

    
#find the eigenvalues
A = np.array([[a, b], [c, d]])
evals, evecs = np.linalg.eig(A)
print(evals)

Answer: The eigenvalues and 2+i and 2-i, which means there is an unstable spiral
at the origin.

**Q1.6:** matrix 6 from problem set 4

xmin = -1.5 #change the parameters here to control the range of the axes
xmax = 1.5
ymin = -1.5
ymax = 1.5
dx = 0.2 #set the size of the x-step on the grid
dy = 0.2 #set the size of the y-step on the grid
X = np.arange(xmin, xmax, dx)
Y = np.arange(ymin, ymax, dy)
x, y = np.meshgrid(X, Y);  #create a grid
    
#Define the functions that define the ODE in order to compute
#the flow vectors on that grid. Here is a linear example:
a = -3
b = -4
c = 1
d = 1
dx = a*x+b*y
dy = c*x+d*y

#Then plot the arrows given by arrays dx,dy at points x,y:
fig, ax = plt.subplots()
q = ax.quiver(x, y, dx, dy)
plt.xlabel('x') #use more informative labels for a real model
plt.ylabel('y')
plt.title('Q1.6: Phase plane')
plt.show()

    
#find the eigenvalues
A = np.array([[a, b], [c, d]])
evals, evecs = np.linalg.eig(A)
print(evals)

Answer: The eigenvalues and -1 and -1, which means this is a degenearate node.

### Part 2: Solutions in the phase plane

Modify the code provided in examples notebook to solve the ODEs, then put a *for loop* around the code in order to plot 6 separate solution trajectories starting from six initial
conditions which you set as two vectors before the loop begins. Your
results for each model should include: 
 
 - overlay the phase portrait with 6 different trajectories
 - plot 6 solutions of X in one window and 6 solutions of Y in another
 - comment on where *each variable* (X and Y) of the solution ends up, and whether/how it depends on the intial values
 - comment on how the classification you provided in part 1 is reflected in the dynamics of the solution trajectories
 
 Q2.1-6: Use the same models that you used in Q1.1-6.

**Q2.1:**

def fun(xy, t, a, b, c, d):
    newxy = [a*xy[0]+b*xy[1], c*xy[0]+d*xy[1]]
    return newxy

# Set the parameters
a = 1
b = 1
c = 4
d = -2


xmin = -1.5 #change the parameters here to control the range of the axes
xmax = 1.5
ymin = -1.5
ymax = 1.5
dx = 0.2 #set the size of the x-step on the grid
dy = 0.2 #set the size of the y-step on the grid
X = np.arange(xmin, xmax, dx)
Y = np.arange(ymin, ymax, dy)
x, y = np.meshgrid(X, Y);  #create a grid

dx = a*x+b*y
dy = c*x+d*y

#Then plot the arrows given by arrays dx,dy at points x,y:
fig, ax = plt.subplots()
q = ax.quiver(x, y, dx, dy)
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.title('Q2.1: Phase plane')
plt.xlabel('x')
plt.ylabel('y')

# set the initial condition vectors
Xinit = [0, 0, 1, 1, -1, -1]
Yinit = [1, -1, 1, -1, 1, -1]
for j in range(6):
    # Set different initial values, the vector of times, and call the ODE solver again
    init = [Xinit[j], Yinit[j]] #[intial x, initial y]
    t = np.linspace(0, 10, 101) # create time vector 
    sol = odeint(fun, init, t, args=(a, b, c, d)) # calculate numeric solution of ODE defined in fun

    # Plot the solution...
    plt.figure(1)
    plt.plot(sol[:,0], sol[:,1])    
    
    plt.figure(2)
    plt.plot(t, sol[:,0])
    plt.xlabel('t')
    plt.ylabel('x')
    plt.title('Q2.1: x')

    plt.figure(3)
    plt.plot(t, sol[:,1])
    plt.xlabel('t')
    plt.ylabel('y')
    plt.title('Q2.1: y')
plt.show()

Answer: All solutions end up diverging from the origin along the direction of the
eigenvector with positive eigenvalue. Eventually the solutions go to
either negative infinity for both x and y, or positive infinity for
both. This is consistent with the saddle point classification.

**Q2.2:**

# Set the parameters
a = 2
b = 1
c = 1
d = 2
xmin = -1.5 #change the parameters here to control the range of the axes
xmax = 1.5
ymin = -1.5
ymax = 1.5
dx = 0.2 #set the size of the x-step on the grid
dy = 0.2 #set the size of the y-step on the grid
X = np.arange(xmin, xmax, dx)
Y = np.arange(ymin, ymax, dy)
x, y = np.meshgrid(X, Y);  #create a grid

dx = a*x+b*y
dy = c*x+d*y

#Then plot the arrows given by arrays dx,dy at points x,y:
fig, ax = plt.subplots()
q = ax.quiver(x, y, dx, dy)
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.title('Q2.2: Phase plane')
plt.xlabel('x')
plt.ylabel('y')

# set the initial condition vectors
Xinit = [0, 0, 1, 1, -1, -1]
Yinit = [1, -1, 1, -1, 1, -1]
for j in range(6):
    # Set different initial values, the vector of times, and call the ODE solver again
    init = [Xinit[j], Yinit[j]] #[intial x, initial y]
    t = np.linspace(0, 10, 101) # create time vector 
    sol = odeint(fun, init, t, args=(a, b, c, d)) # calculate numeric solution of ODE defined in fun

    # Plot the solution...
    plt.figure(1)
    plt.plot(sol[:,0], sol[:,1])    
    
    plt.figure(2)
    plt.plot(t, sol[:,0])
    plt.xlabel('t')
    plt.ylabel('x')
    plt.title('Q2.2: x')

    plt.figure(3)
    plt.plot(t, sol[:,1])
    plt.xlabel('t')
    plt.ylabel('y')
    plt.title('Q2.2: y')
plt.show()

Answer: All solutions end up diverging from the origin, ending up parallel to
the "fast" eigenvector (1,1), unless they start on the "slow"
eigenvector (1,-1). Those parallel to the fast eigenvector will end up going to
either negative infinity for both x and y, or positive infinity for
both; those with initial values exactly on the slow eigenvector go to
+infinity for one variable, a -infinity for the other. This is
consistent with the unstable node classification. 

**Q2.3:**

# Set the parameters
a = 1
b = 2
c = -2
d = -4
xmin = -1.5 #change the parameters here to control the range of the axes
xmax = 1.5
ymin = -1.5
ymax = 1.5
dx = 0.2 #set the size of the x-step on the grid
dy = 0.2 #set the size of the y-step on the grid
X = np.arange(xmin, xmax, dx)
Y = np.arange(ymin, ymax, dy)
x, y = np.meshgrid(X, Y);  #create a grid

dx = a*x+b*y
dy = c*x+d*y

#Then plot the arrows given by arrays dx,dy at points x,y:
fig, ax = plt.subplots()
q = ax.quiver(x, y, dx, dy)
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.title('Q2.3: Phase plane')
plt.xlabel('x')
plt.ylabel('y')

# set the initial condition vectors
Xinit = [0, 0, 1, 1, -1, -1]
Yinit = [1, -1, 1, -1, 1, -1]
for j in range(6):
    # Set different initial values, the vector of times, and call the ODE solver again
    init = [Xinit[j], Yinit[j]] #[intial x, initial y]
    t = np.linspace(0, 10, 101) # create time vector 
    sol = odeint(fun, init, t, args=(a, b, c, d)) # calculate numeric solution of ODE defined in fun

    # Plot the solution...
    plt.figure(1)
    plt.plot(sol[:,0], sol[:,1])    
    
    plt.figure(2)
    plt.plot(t, sol[:,0])
    plt.xlabel('t')
    plt.ylabel('x')
    plt.title('Q2.3: x')

    plt.figure(3)
    plt.plot(t, sol[:,1])
    plt.xlabel('t')
    plt.ylabel('y')
    plt.title('Q2.3: y')
plt.show()

Answer: All solutions approach the line of fixed points (eigenvector (2,-1)).
X and Y don't have a single destination in the long run, they
converge to the neareast point on the fixed line. This is consistent
with the fixed line classification.

**Q2.4:**

# Set the parameters
a = -2
b = 1
c = 3
d = -4
xmin = -1.5 #change the parameters here to control the range of the axes
xmax = 1.5
ymin = -1.5
ymax = 1.5
dx = 0.2 #set the size of the x-step on the grid
dy = 0.2 #set the size of the y-step on the grid
X = np.arange(xmin, xmax, dx)
Y = np.arange(ymin, ymax, dy)
x, y = np.meshgrid(X, Y);  #create a grid

dx = a*x+b*y
dy = c*x+d*y

#Then plot the arrows given by arrays dx,dy at points x,y:
fig, ax = plt.subplots()
q = ax.quiver(x, y, dx, dy)
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.title('Q2.4: Phase plane')
plt.xlabel('x')
plt.ylabel('y')

# set the initial condition vectors
Xinit = [0, 0, 1, 1, -1, -1]
Yinit = [1, -1, 1, -1, 1, -1]
for j in range(6):
    # Set different initial values, the vector of times, and call the ODE solver again
    init = [Xinit[j], Yinit[j]] #[intial x, initial y]
    t = np.linspace(0, 10, 101) # create time vector 
    sol = odeint(fun, init, t, args=(a, b, c, d)) # calculate numeric solution of ODE defined in fun

    # Plot the solution...
    plt.figure(1)
    plt.plot(sol[:,0], sol[:,1])    
    
    plt.figure(2)
    plt.plot(t, sol[:,0])
    plt.xlabel('t')
    plt.ylabel('x')
    plt.title('Q2.4: x')

    plt.figure(3)
    plt.plot(t, sol[:,1])
    plt.xlabel('t')
    plt.ylabel('y')
    plt.title('Q2.4: y')
plt.show()

Answer: All solutions approach the origin, first along the "fast" eigenvector and
then ending up parallel to the "slow" eigenvector (1,1). Both x and y
approach 0 in the long run. This is consistent with the stable node
classification. 

**Q2.5:**

# Set the parameters
a = 5
b = 10
c = -1
d = -1

xmin = -1.5 #change the parameters here to control the range of the axes
xmax = 1.5
ymin = -1.5
ymax = 1.5
dx = 0.2 #set the size of the x-step on the grid
dy = 0.2 #set the size of the y-step on the grid
X = np.arange(xmin, xmax, dx)
Y = np.arange(ymin, ymax, dy)
x, y = np.meshgrid(X, Y);  #create a grid

dx = a*x+b*y
dy = c*x+d*y

#Then plot the arrows given by arrays dx,dy at points x,y:
fig, ax = plt.subplots()
q = ax.quiver(x, y, dx, dy)
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.title('Q2.5: Phase plane')
plt.xlabel('x')
plt.ylabel('y')

# set the initial condition vectors
Xinit = [0, 0, 1, 1, -1, -1]
Yinit = [1, -1, 1, -1, 1, -1]
for j in range(6):
    # Set different initial values, the vector of times, and call the ODE solver again
    init = [Xinit[j], Yinit[j]] #[intial x, initial y]
    t = np.linspace(0, 10, 101) # create time vector 
    sol = odeint(fun, init, t, args=(a, b, c, d)) # calculate numeric solution of ODE defined in fun

    # Plot the solution...
    plt.figure(1)
    plt.plot(sol[:,0], sol[:,1])    
    
    plt.figure(2)
    plt.plot(t, sol[:,0])
    plt.xlabel('t')
    plt.ylabel('x')
    plt.title('Q2.5: x')

    plt.figure(3)
    plt.plot(t, sol[:,1])
    plt.xlabel('t')
    plt.ylabel('y')
    plt.title('Q2.5: y')
plt.show()

Answer: All solutions diverge from the origin in a oscillatory fashion - 
which can be seen by plotting the two variables separately, because the
oscillations are not easy to see in the phase plane.
The variables x and y both oscillate with increasing amplitudes. This
is consistent with the unstable spiral.

**Q2.6:**

# Set the parameters
a = -3
b = -4
c = 1
d = 1
xmin = -1.5 #change the parameters here to control the range of the axes
xmax = 1.5
ymin = -1.5
ymax = 1.5
dx = 0.2 #set the size of the x-step on the grid
dy = 0.2 #set the size of the y-step on the grid
X = np.arange(xmin, xmax, dx)
Y = np.arange(ymin, ymax, dy)
x, y = np.meshgrid(X, Y);  #create a grid

dx = a*x+b*y
dy = c*x+d*y

#Then plot the arrows given by arrays dx,dy at points x,y:
fig, ax = plt.subplots()
q = ax.quiver(x, y, dx, dy)
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.title('Q2.6: Phase plane')
plt.xlabel('x')
plt.ylabel('y')

# set the initial condition vectors
Xinit = [0, 0, 1, 1, -1, -1]
Yinit = [1, -1, 1, -1, 1, -1]
for j in range(6):
    # Set different initial values, the vector of times, and call the ODE solver again
    init = [Xinit[j], Yinit[j]] #[intial x, initial y]
    t = np.linspace(0, 10, 101) # create time vector 
    sol = odeint(fun, init, t, args=(a, b, c, d)) # calculate numeric solution of ODE defined in fun

    # Plot the solution...
    plt.figure(1)
    plt.plot(sol[:,0], sol[:,1])    
    
    plt.figure(2)
    plt.plot(t, sol[:,0])
    plt.xlabel('t')
    plt.ylabel('x')
    plt.title('Q2.6: x')

    plt.figure(3)
    plt.plot(t, sol[:,1])
    plt.xlabel('t')
    plt.ylabel('y')
    plt.title('Q2.6: y')
plt.show()

Answer: All solutions end up approaching the origin along the solitary
eigenvector. In the long run, both x and y approach 0, and although they
look like they're starting to oscillate, they never complete a period.
This is consistent with the degenerate stable node classification.   

### Rubric

**Part 1**
 - Q1.1-6: 2 pts each: code and plot (1), classification of ODE (1)

**Part 2**
 - Q2.1-6: 4 pts each: code (1), phase plots with 6 trajectories (1), plot of 6 x and y solutions (2), description of where each coordinate ends up (1)


*Total: 36 points*

MAKE SURE YOUR CODE RUNS BEFORE SUBMITTING IT

