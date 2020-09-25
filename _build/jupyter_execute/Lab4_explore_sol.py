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

Suppose $R$ and $J$ are both totally and identically self-absorbed, that is $a=d$ and $b=c=0$. Investigate the dynamics of the model under these conditions, and plot solutions separately for positive self-awareness ($a=d >0$) and for negative self-awareness ($a = d <0$). Describe verbally the predicted fate of the relationship in each scenario.

def fun(xy, t, a, b, c, d):
    newxy = [a*xy[0]+b*xy[1], c*xy[0]+d*xy[1]]
    return newxy

# Set the parameters
a = -0.3
b = 0
c = 0
d = a
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
plt.title('Phase plane for self-absorbed lovers with negative a and d')
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

    plt.figure(3)
    plt.plot(t, sol[:,1])


plt.figure(2)
plt.xlabel('t')
plt.ylabel('R feelings')
plt.title('Self-absorbed lovers with positive a and d')

plt.figure(3)
plt.xlabel('t')
plt.ylabel('J feelings')
plt.title('Self-absorbed lovers with positive a and d')
plt.show()

# Set the parameters
a = 0.3
b = 0
c = 0
d = a
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
plt.title('Phase plane for self-absorbed lovers with positive a and d')
plt.xlabel('R')
plt.ylabel('J')

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

    plt.figure(3)
    plt.plot(t, sol[:,1])


plt.figure(2)
plt.xlabel('t')
plt.ylabel('R feelings')
plt.title('Self-absorbed lovers with positive a and d')

plt.figure(3)
plt.xlabel('t')
plt.ylabel('J feelings')
plt.title('Self-absorbed lovers with positive a and d')
plt.show()

For identical lovers with negative self-awareness (tamping down their own emotions) the feelings of both R and J eventually converge to zero (indifference). For positive values of self-awareness (getting excited by their own emotions) the feelings for R and J grow either to positive infinity or negative infinity, depending on initial values.

Suppose $R$ and $J$ are again identical, but now they are totally not self-aware that is $a=d=0$ and identically responsive to each other $b=c$. Investigate the dynamics of the model under these conditions, and plot solutions separately for positive responsiveness($b = c >0$) and for negative responsiveness ($b = c <0$). Describe verbally the predicted fate of the relationship in each scenario.

def fun(xy, t, a, b, c, d):
    newxy = [a*xy[0]+b*xy[1], c*xy[0]+d*xy[1]]
    return newxy

# Set the parameters
a = 0
b = 0.5
c = b
d = a
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
plt.title('Not self-aware lovers with positive b and c')
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

    plt.figure(3)
    plt.plot(t, sol[:,1])


plt.figure(2)
plt.xlabel('t')
plt.ylabel('R feelings')
plt.title('Not self-aware lovers with positive b and c')

plt.figure(3)
plt.xlabel('t')
plt.ylabel('J feelings')
plt.title('Not self-aware lovers with positive b and c')
plt.show()

# Set the parameters
a = 0
b = -0.5
c = b
d = a
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
plt.title('Phase plane for not self-aware lovers with negative b and c')
plt.xlabel('R')
plt.ylabel('J')

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

    plt.figure(3)
    plt.plot(t, sol[:,1])


plt.figure(2)
plt.xlabel('t')
plt.ylabel('R feelings')
plt.title('Not self-aware lovers with negative b and c')

plt.figure(3)
plt.xlabel('t')
plt.ylabel('J feelings')
plt.title('Not self-aware lovers with negative b and c')
plt.show()

For identical lovers with positive responsiveness (feeding off the other) the feelings of both R and J run away either toward love or hate together. For negative values of responsiveness (turning each other off) the feelings for R and J grow either to positive infinity or negative infinity, in opposite directions.

Suppose $R$ and $J$ are instead polar opposites, with $a= - d$ and $b = -c$. Investigate the dynamics of the model under these conditions for different parameter values and report all possible relationship dynamics that are possible, with plots and explanations for each scenario.

def fun(xy, t, a, b, c, d):
    newxy = [a*xy[0]+b*xy[1], c*xy[0]+d*xy[1]]
    return newxy

# Set the parameters
a = 2
b = -0.5
c = -b
d = -a
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
plt.title('Opposite lovers with a='+str(a)+' and b='+str(b))
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

    plt.figure(3)
    plt.plot(t, sol[:,1])


plt.figure(2)
plt.xlabel('t')
plt.ylabel('R feelings')
plt.title('Opposite lovers with a='+str(a)+' and b='+str(b))

plt.figure(3)
plt.xlabel('t')
plt.ylabel('J feelings')
plt.title('Opposite lovers with a='+str(a)+' and b='+str(b))
plt.show()

# Set the parameters
a = -0.2
b = -0.6
c = -b
d = -a
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
plt.title('Opposite lovers with a='+str(a)+' and b='+str(b))
plt.xlabel('R')
plt.ylabel('J')

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

    plt.figure(3)
    plt.plot(t, sol[:,1])


plt.figure(2)
plt.xlabel('t')
plt.ylabel('R feelings')
plt.title('Opposite lovers with a='+str(a)+' and b='+str(b))

plt.figure(3)
plt.xlabel('t')
plt.ylabel('J feelings')
plt.title('Opposite lovers with a='+str(a)+' and b='+str(b))
plt.show()

There are two fundamentally different scenarios: 
1) $ 3a^2 > 4 a^2$ and 
2) $ 3a^2 < 4a^2$. 
The first set of plots illustrates the first scenario, in which the solutions for $R$ and $J$ diverge to positive and negative infinities (in opposite directions if the signs of $a$ and $b$ are the same, and in the same direction if the signs of $a$ and $b$ are different.)

The second set of plots illustrates the second scenario, in which solutions oscillate around 0 forever in love-hate cycles.