# Models with one variable in discrete time


## Introduction

All living things change over time, and this evolution can be quantitatively measured and analyzed. Mathematics makes use of equations to define models that change with time, known as *dynamical systems*. In this unit we will learn how to construct models that describe the time-dependent behavior of some measurable quantity in life sciences. Numerous fields of biology use such models, and in particular we will consider changes in population size, the progress of biochemical reactions, the spread of infectious disease, and the spikes of membrane potentials in neurons, as some of the main examples of biological dynamical systems.

Many processes in living things happen regularly, repeating with a fairly constant time period. One common example is the reproductive cycle in species that reproduce periodically, whether once a year, or once an hour, like certain bacteria that divide at a relatively constant rate under favorable conditions. Other periodic phenomena include circadian (daily) cycles in physiology, contractions of the heart muscle, and waves of neural activity. For these processes, theoretical biologists use models with *discrete time*, in which the time variable is restricted to the integers. For instance, it is natural to count the
generations in whole numbers when modeling population growth.

This chapter is devoted to analyzing dynamical systems in which time is measured in discrete steps. It supposes that you have been exposed to linear one-variable difference equations before, and the first section briefly summarizes building and solving linear difference equations.

## Linear discrete time population models 

Let us construct our first models of biological systems. We will start by considering a population of some species, with the goal of tracking its growth or decay over time. The variable of interest is the number of individuals in the population, which we will call $N$. This is called the dependent variable, since its value changes depending on time; it would make no sense to say that time changes depending on the population size. Throughout the study of dynamical systems, we will denote the independent variable of time by $t$. To denote the population size at
time $t$, we can write $N(t)$ but sometimes use $N_t$.

### static population

In order to describe the dynamics, we need to write down a rule for how the population changes. Consider the simplest case, in which the population stays the same for all time. (Maybe it is a pile of rocks?) Then the following equation describes this situation: 

$$
N(t+1) = N(t)
$$

This equation mandates that the population at the next time step be the same as at the present time $t$. This type of equation is generally called a *difference equation*, because it can be written as a difference between the values at the two different times:

$$
N(t+1) - N(t) = 0
$$ 

This version of the model illustrates that a difference equation at its core describes the *increments* of $N$ from one time step to the next. In this case, the increments are always 0, which makes it plain that the population does not change from one time
step to the next.

### exponential population growth

Let us consider a more interesting situation: as a colony of dividing bacteria. such as *E. coli*, shown in {numref}`fig-cell-div`. We assume that each bacterial cell divides and produces two daughter cells at fixed intervals of time, and let us further suppose that bacteria never die. Essentially, we are assuming a population of immortal bacteria with clocks. This means that after each cell division the population size doubles. As before, we denote the number of cells in each generation by $N(t)$, and obtain the equation describing each successive generation: 

$$
N(t+1) = 2N(t)
$$

It can also be written in the difference form, as above: 

$$
N(t+1) - N(t) = N(t)
$$ 

The increment in population size is determined by the current population size, so the population in this model is forever growing. This type of behavior is termed *exponential growth* and we will see how to express the solution algebraically in the next section.


```{figure} images/Ecoli_dividing.png
---
name: fig-cell-div
---
Scanning electron micrograph of a dividing *Escherichia coli* bacteria (image by Evangeline Sowers, Janice Haney Carr (CDC) in public domain via Wikimedia Commons)
```


### example with birth and death

Suppose that a type of fish lives to reproduce only once after a period of maturation, after which the adults die. In this simple scenario, half of the population is female, a female always lays 1000 eggs, and of those, 1% survive to maturity and reproduce. Let us set up the model for the population growth of this idealized fish population. The general idea, as before, is to relate the population size at the next time step $N(t+1)$ to the population at the present time $N(t)$.

Let us tabulate both the increases and the decreases in the population size. We have $N(t)$ fish at the present time, but we know they all die after reproducing, so there is a decrease of $N(t)$ in the population. Since half of the population is female, the number of new offspring produced by $N(t)$ fish is $500N(t)$. Of those, only 1% survive to maturity (the next time step), and the other 99% ($495N(t)$) die. We can add all the terms together to obtain the following difference equation:

$$
N(t+1) = N(t) - N(t) + 500N(t) - 495 N(t)  = 5N(t)
$$

The number 500 in the expression is the *birth rate* of the population per individual, and the negative terms add up to the *death rate* of 496 per individual. We can re-write the equation in difference form: 

$$
N(t+1) - N(t) = 4N(t)
$$

This expression again generates growth in the population, because the birth rate outweighs the death rate. [@allman_mathematical_2003]

### dimensions of birth and death rates

What distinguishes a mathematical model from a mathematical equation is that the quantities involved have a real-world meaning. Each quantity represents a measurement, and associated with each one are the *units* of measurement, which are familiar from science courses. In addition to units, each variable and parameter has a meaning, which is called the *dimension* of the quantity. For example, any measurement of length or distance has the same dimension, although the units may vary. The value
of a quantity depends on the units of measurement, but its essential dimensionality does not. One can convert a measurement in meters to that in light-years or cubits, but one cannot convert a measurement in number of sheep to seconds - that conversion has no meaning.

Thus leads us to the fundamental rule of mathematical modeling: **terms that are added or subtracted must have the same dimension**. This gives mathematical modelers a useful tool called *dimensional analysis*, which involves replacing the quantities in an equation with their dimensions. This serves as a check that all dimensions match, as well as allowing to deduce the dimensions of any parameters for which the dimension was not specified.

In the case of population models, the birth and death rates measure the number of individuals that are born (or die) within a reproductive cycle for every individual at the present time. Their dimensions must be such that the terms in the equation all match:

$$
[N(t+1) - N(t)] = [population] = [r] [N(t)] = [r] *[population]
$$ 

This implies that $[r]$ is algebraically dimensionless. However, the meaning of $r$ is the rate of change of population over one (generation) time step. $r$ is the birth or death rate of the population *per generation*, which is what makes is dimensionless. If the length of the generation were to change, but the reproduction and death per generation remain the same, then the paramter $r$ would be the same, because it had been *rescaled* by the length of the generation. If they were to be reported in *absolute* units (e.g. individuals per year) then the rate would be different.

### general demographic model

We will now write a general difference equation for any population with constant birth and death rates. This will allow us to substitute arbitrary values of the birth and death rates to model different biological situations. Suppose that a population has the birth rate of $b$ per individual, and the death rate $d$ per individual. Then the general model of the population size is: 

$$
N(t+1) = (1 + b - d)N(t)
$$

The general equation also allows us to check the dimensions of birth and death rates, especially as written in the
incremental form: $N(t+1) - N(t) = (b - d)N(t)$. The change in population rate over one reproductive cycle is given by the current population size multiplied by the difference of birth and death rates, which as we saw are algebraically dimensionless. The right hand side of the equation has the dimensions of population size, matching the difference on the left hand side. [@edelstein-keshet_mathematical_2005]

## Solutions of linear difference models 


### simple linear difference models

Having set up the difference equation models, we would naturally like to solve them to find out how the dependent variable, such as population size, varies over time. A solution may be *analytic*, meaning that it can be written as a formula, or *numeric*, in which case it is generated by a computer in the form of a sequence of values of the dependent variable over a period of time. In this section, we will find some simple analytic solutions and learn to analyze the behavior of difference equations which we cannot solve exactly.

A function $N(t)$ is a *solution* (over some time period $a < t < b$) of a difference equation $N(t+1) = f(N(t))$ if it satisfies that equation (over some time period $a < t < b$). \[def:math14\_sol\]

For instance, let us take our first model of the static population, $ N(t+1) = N(t)$. Any constant function is a solution, for example, $N(t) = 0$, or $N(t) = 10$. There are actually as many solutions as there are numbers, that is, infinitely many! In order to specify exactly what happens in the model, we need to specify the size of the population at some point, usually, at the “beginning of time”, $t = 0$. This is called the *initial condition* for the model, and for a well-behaved difference equation it is enough to determine a unique solution. For the
static model, specifying the initial condition is the same as specifying the population size for all time.

Now let us look at the general model of population growth with constant birth and death rates. We saw in equation \[linear\_pop\] above that these can be written in the form $N(t+1) = (1 + b - d) N(t)$. To simplify, let us combine the numbers into one growth parameter $r = 1 + b - d$, and write down the general equation for population growth with constant growth rate: 

$$
N(t+1) =  rN(t)
$$

To find the solution, consider a specific example, where we start with the initial population size $N_0 = 1$, and the growth rate $r=2$. The sequence of population sizes is: 1, 2, 4, 8, 16, etc. This is described by the formula $N(t) = 2^t$.

In the general case, each time step the solution is multiplied by $r$, so the solution has the same exponential form. The initial condition $N_0$ is a multiplicative constant in the solution, and one can verify that when $t=0$, the solution matches the initial value:

$$
N(t)  = r^t N_0
\label{eq:lin_discrete_sol}
$$

I would like the reader to pause and consider this remarkable formula. No matter what the birth and death parameters are selected, this solution predicts the population size at
any point in time $t$.

In order to verify that the formula for $N(t)$ is actually a solution in the meaning of definition \[def:math14\_sol\], we need to check that it actually satisfies the difference equation for all $t$, not just a few time steps. This can be done algebraically by plugging in $N(t+1)$ into the left side of the dynamic model and $N(t)$ into the right side and checking whether they match. For $N(t)$ given by equation \[eq:lin\_discrete\_sol\], $N(t+1) = r^{t+1} N_0$, and thus the dynamic model becomes: 

$$
r^{t+1} N_0 = r \times r^t N_0
$$

Since the two sides match, this means the solution is correct.

The solutions in formula \[eq:lin\_discrete\_sol\] are exponential functions, which have a limited menu of behaviors, depending on the value of $r$. If $r > 1$, multiplication by $r$ increases the size of the population, so the solution $N(t)$ will grow (see {numref}`fig-exp-growth`. If $r < 1$, multiplication by $r$ decreases the size of the population, so the solution $N(t)$ will decay (see {numref}`fig-exp-decay`). Finally, if $r=1$, multiplication by $r$ leaves the population size unchanged, like in the pile of rocks model. Here is the complete classification of the behavior of population models with constant birth and death rates (assuming $r>0$):

*   $|r| > 1$: $N(t)$ grows without bound

*   $|r| < 1$: $N(t)$ decays to 0

*   $|r| = 1 $: the absolute value of $N(t)$ remains constant

Figure  shows examples of graphs of solutions of such
equations with $r$ greater than 1 and $r$ less than 1.

```{figure} images/ch1_exp_growth.png
---
name: fig-exp-growth
---
Growth of a population that doubles every generation over 6 generations.
```

```{figure} images/ch1_exp_decay.png
---
name: fig-exp-decay
---
Decay of a population in which half the individuals die every time step over 6 generations
```


### linear difference models with a constant term

Now let us consider a dynamic model that combines two different rates: a proportional rate ($rN$) and a constant rate which does not depend on the value of the variable $N$. We can write such a generic model as follows: 

$$
N(t+1) =  rN(t) + a
$$

The right-hand-side of this equation is a linear function of $N$, so this is a linear difference equation with a constant term. What function $N(t)$ satisfies it? One can quickly check that that the same solution $N(t) = r^t N_0$ does not work because of
the pesky constant term $a$: 

$$
r^{t+1} N_0 \neq r \times r^t N_0 + a
$$

To solve it, we need to try a different form: specifically, an
exponential with an added constant. The exponential can be reasonably surmised to have base $r$ as before, and then leave the two constants as unknown: $N(t) = c_1 r^t + c_2$. To figure out whether this is a solution, plug it into the linear difference equation above and check whether a choice of constants can make the two sides agree:

$$
N(t+1) =  c_1 r^{t +1} + c_2 = rN(t) + a  = rc_1 r^t + rc_2+ a
$$ 

This equation has the same term $c_1 r^{t +1}$ on both sides, so they can be subtracted out. The remaining equation involves only $c_2$, and its solution is $c_2 = a/(1-r)$. Therefore, the general solution of this linear difference equation is the following expreis which is determined from the initial value by plugging $t=0$ and solving for $c$.

$$
N(t) = c r^t  + \frac{a}{1-r}
\label{eq:ch14_sol_wconst}
$$

**Example.** Take the difference equation $N(t+1) = 0.5 N(t) + 40$ with initial value $N(0)= 100$. The solution, according to our formula is $N(t) = c 0.5^t + 80$. At $N(0) = 100 = c+80$, so $c=20$. Then the compete solution is  $N(t) = 20*0.5^t + 80$. To check that this actually works, plug this solution back into the difference equation:

$$
N(t+1) = 20 \times 0.5^{t+1} + 80 = 0.5 \times (20 \times 0.5^t + 80) + 40 =  20 \times 0.5^{t+1} + 80
$$
The equation is satisfied and therefore the solution is correct.

### logistic population model

Linear population growth models assume that the per capita birth and death rates are constant, that is, they stay the same regardless of population size. The solutions for these models either grow or decay exponentially, but in reality, populations cannot grow without bounds. It is generally true that the larger a population grows, the more scarce the resources, and survival becomes more difficult. For larger populations, this could lead to higher death rates, or lower birth rates, or both. 

To incorporate this effect into a quantitative model we will assume there are separate birth and death rates, and that the birth rate declines as the population grows, while the death rate increases:

$$
b =  b_1 - b_2 N(t) ; \;   d = d_1 + d_2 N(t)
$$

To model the rate of change of the population, we need to multiply the rates $b$ and $d$ by the population size $N$, since each individual can reproduce or die. Also, since the death rate $d$ decreases the population, we need to put a negative sign on it. The resulting model is:


$$
N(t+1) - N(t) = (b -d)N(t) = [(b_1 - d_1) - (b_2 + d_2)N(t)] N(t)
$$

A simpler way of writing this equation is to let $r = 1 + b_1 - d_1$ and $K = b_2 + d_2$, leading to the following iterated map:

$$
N(t+1) = (r - K N(t)) N(t)
\label{discrete_logistic}
$$ 

This is called the *logistic model* of population growth. As you see, it has two different parameters, $r$ and $K$. If $K = 0$, the equation reduces to the old linear population model. Intuitively, $K$ is the parameter describing the effect of increasing population on the population growth rate. Let us analyze the
dimensions of the two parameters, by writing down the dimensions of the variables of the difference equation. The dimensional equation is:

$$
N(t+1) = [population]= [r- K N(t)] N(t) =
= ([r]  - [K] \times [population]) \times [population]
$$ 

Matching the dimensions on the two sides of the equation leads us to conclude that the dimensions of $r$ and $k$ are different:

$$
[r] = 1 ; \; [K] =  \frac{1}{[population]}
$$ 

The difference equation for the logistic model is *nonlinear*, because it includes a second power of the dependent variable. In general, it is difficult to solve nonlinear equations, but we can still say a lot about this model’s behavior without knowing its explicit solution.

## Qualitative analysis of difference equations 


### equilibrium values or fixed points

We have seen that the solutions of difference equations depend on the initial value of the dependent variable. In the examples we have seen so far, the long-term behavior of the solution does not depend dramatically on the initial condition. In more complex systems that we will encounter, there are special values of the dependent variable for which the dynamical system is constant, like in the pile of rocks model.

For a difference equation $X(t+1) = f(X(t))$, a point $X^*$ which
satisfies $f(X^*)=X^*$ is called a *fixed point* or *equilibrium*. If the initial condition is a fixed point, $X_0=X^*$, the solution will stay at the same value for all time, $X(t)=X^*$.

The reason these special points are also known as equilibria is due to the precise balance between growth and decay that is mandated at a fixed point. In terms of population modeling, at an equilibrium the birth rates and the death rates are equal. Speaking analytically, in order to find the fixed points of a difference equation, one must solve the equation $f(X^*) = X^*$. It may have none, or one, or many solutions.

**Example.** The linear population models which we analyzed in the previous sections have the mathematical form $N(t+1)= r N(t)$ (where $r$ can be any real number). Then the only fixed point of those models is $N^* = 0$, that is, a population with no individuals. If there are any individuals present, we know that the population will grow to infinity if $|r| > 1$, and decay to 0 if $|r| < 1$. This is true even for the smallest population size, as long as it is not exactly zero.

**Example.** Let us go back to the example of a linear difference
equation with a constant term. The equation is $ N(t+1) = -0.5N(t) +10$, and we saw that the numerical solutions all converged to the same value, regardless of the initial value. Let us find the equilibrium value of this model using the definition:

$$
N^* = -0.5N^* +10 \Rightarrow 1.5 N^* = 10  \Rightarrow N^* = 10/1.5 = 20/3
$$

If the initial value is equal to the equilibrium, $N(0)= 20/3$, then the solution will remain constant for all time, since the next value $N(t+1) = -0.5*20/3+10 = 20/3$ remains the same.

**Example: discrete logistic model.** Let us use the simplified version of the logistic equation $N(t+1) = r(1 - N(t)) N(t)$ and set the right-hand side function equal to the variable $N$ to find the fixed points $N^*$: $$r(1 - N^*) N^* = N^*$$ There are two solutions to this equation, $N^* = 0$ and $N^* = (r-1)/r$. These are the fixed points or the equilibrium population sizes for the model, the first being the obvious case when the population is extinct. The second equilibrium is more interesting, as it describes the *carrying capacity* of a population in a particular environment. If the initial value is equal to either of the two fixed points, the solution will remain at that same value for all time. But what happens to solutions which do not start a fixed point? Do they converge to a fixed point, and if so, to which one?

### stability criteria for fixed points

What happens to the solution of a dynamical system if the initial
condition is very close to an equilibrium, but not precisely at it? Put another way, what happens if the equilibrium is *perturbed*? To answer the question, we will no longer confine ourselves to the integers, to be interpreted as population sizes. We will instead consider, abstractly, what happens if the smallest perturbation is added to a fixed point. Will the solution tend to return to the fixed point or tend to move away from it? The answer to this question is formalized in the following definition [@strogatz_nonlinear_2001]:

For a difference equation $X(t+1) = f(X(t))$, a fixed point $X^*$ is *stable* if for a sufficiently small number $\epsilon$, the solution $X(t)$ with the initial condition $X_0 = X^* + \epsilon$ approaches the fixed point $X^*$ as $t \rightarrow \infty$. If the solution $X(t)$ does not approach $X^*$ for any nonzero $\epsilon$, the fixed point is called *unstable*.

The notion of stability is central to the study of dynamical systems. Typically, models more complex than those we have seen cannot be solved analytically. Finding the fixed points and determining their stability can help us understand the general behavior of solutions without writing them down. For instance, we know that solutions never approach an unstable fixed point, whereas for a stable fixed point the solutions will tend to it, from some range of initial conditions.

There is a mathematical test to determine the stability of a fixed
point. From standard calculus comes the Taylor expansion, which
approximates the value of a function near a given point. Take a general difference equation written in terms of some function
$X(t+1) = f(X(t))$. Let us define the *deviation* from the fixed point $X^*$ at time $t$ to be $\epsilon(t) = x_{t} - X^*$. Then we can use the linear (first-order) Taylor approximation at the fixed point and write down the following expression:

$$ 
X(t+1) = f(X^*) + \epsilon(t) f'(X^*) + ...
$$ 

The ellipsis means that the expression is approximate, with terms of order $\epsilon(t)^2$ and higher swept under the rug. Since we take $\epsilon(t)$ to be small, those terms are very small and can be neglected. Since $X^*$ is a fixed point, $f(X^*) = X^*$. Thus, we can write the following difference equation to describe the behavior of the deviation from the fixed point $X^*$:

$$
X(t+1) -  X^* =  \epsilon(t+1)= \epsilon(t) f'(X^*)
$$

We see that we started out with a general function defining the difference equation and transformed it into a linear equation for the deviation $\epsilon(t)$. Note that the multiplicative constant here is the derivative of the function at the fixed point: $f'(X^*)$. This is called the *linearization* approach, which is an approximation of a dynamical system near a fixed point with a linear equation for the small perturbation.

We found the solution to simple linear equations, which we can use
describe the behavior of the perturbation to the fixed point. The
behavior **depends on the value of the derivative of the updating function** $f'(X^*)$:

 * $|f'(X^*)| > 1$: the deviation $\epsilon(t)$ grows, and the solution moves away from the fixed point; fixed point is *unstable*

 * $|f'(X^*)| < 1$: the deviation $\epsilon(t)$ decays, and the solution approaches the fixed point; fixed point is *stable*

 * $|f'(X^*)| = 1 $: the fixed point may be stable or unstable, and more information is needed

We now know how to determine the stability of a fixed point, so let us apply this method to some examples.

**Example: linear difference equations.** Let us analyze the stability of the fixed point of a linear difference equation, e.g.
$ N(t+1) = -0.5N(t) +10$. The derivative of the updating function is equal to -0.5. Because it is less than 1 in absolute value, the fixed point is stable, so solutions converge to this equilibrium. We can state more generally that any linear difference equation of the form $N(t+1) = aN(t) + b$ has one fixed point, which is equal to $N^* = b/(1-a)$. This fixed point is stable if $|a| <1$ and unstable if $|a|>1$.

**Example: discrete logistic model.** In the last subsection we found the fixed points of the simplified logistic model. To determine what happens to the solution, we need to determine the stability of both equilibria. Since the stability of fixed points is determined by the derivative of the defining function at the fixed points, we compute the derivative of $f(N) = rN-rN^2$ to be $f'(N) = r-2rN$, and evaluate it at the two fixed points $N^* = 0$ and $N^* = (r-1)/r$:

$$
f'(0) = r; \; \; f'((r-1)/r) = r-2(r-1) = 2-r
$$ 

Because the intrinsic death rate cannot be greater than the birth rate, we know that $r>0$. Therefore, we have the following *stability conditions* for the two fixed points:

 * the fixed point $N^*=0$ is stable for $r<1$, and unstable for $r>1$;

 * the fixed point $N^*= (r-1)/r$ is stable for $1<r<3$, and unstable otherwise.

## Numeric solutions and graphical methods


### numeric solution of a discrete model

Difference equations, as we saw above, can be written in the form of $x_{t+1} = f(x_t)$. At every step, the model takes the current value of the dependent variable $x_t$, feeds it into the function $f(x)$, and takes the output as the next value $x_{t+1}$. The same process repeats every iteration, which is why difference equations written in this form are called *iterated maps*.

Computers are naturally suited for precise, repetitive operations. In our first example of a computational algorithm, we will iterate a given function to produce a sequence of values of the dependent variable $x$. We only need two things: to specify a computer function $f(x)$, which returns the value of the iterated map for any input value $x$, and the initial value $x_0$. Then it is a matter of repeating the operation of evaluating $f(x_t)$ and storing it as the next value $x_{t+1}$. Below is the pseudocode for the algorithm. Note that I will use arrows to indicated variable assignment, square brackets $[]$ for indexing of
vector, and start indexing at 0, consistent with python convention.

```{topic} Algorithm: Iterative solution of difference equations
 * define the iterated map function $F(x)$ 
 * set $N$ to be the number of iterations (time steps) 
 * set the initial condition $x_0$
 * initialize array $x$ with initial value $x_0$
 * for $i$ from 0 to $N-1$
   - $x[i+1] \gets F(x[i])$
```

The resulting sequence of values $x_0, x_1, x_2, ... , x_N$ is called a *numeric solution* of the given difference equation. It has two disadvantages compared to an analytic solution: first, the solution can only be obtained for a specific initial value and number of iterations, and second, any computer simulation inevitably introduces some errors, for instance from round-off. In practice, however, most complex dynamical systems have to solved numerically, as analytical solutions are difficult or impossible to find.

### cobweb plots

In addition to calculating numeric solutions, computational tools can be used to analyze dynamical systems graphically. A lot of information can be gleaned by plotting the graph of the defining function of an iterated map $X_{t+1} = f(X_t)$. We have already seen some of the concepts in the previous analytical section. Here is a summary of what we can learn from the graph of the function $f(x)$:

1.  The location of the fixed points of the iterated map. Since the condition for a fixed point is $f(x) = x$, they can be found at the intersections of the graph of $y=f(x)$ and $y=x$ (the identity straight line).

2.  The stability of fixed points. We learned that the derivative of $f(x)$ at a fixed point determines its stability. Graphically, this means that the slope of $f(x)$ at the point of intersection with $y=x$ can be used for this purpose; if it is steeper (in absolute value) than the straight line $y=x$, then the fixed point is unstable, but if its slope is less than one in absolute value, the equilibrium is stable.

3.  Graphical iteration of the difference equation. The value of the function $f(x)$ gives the value of $x$ at the next time step, and this fact can be used to produce a graph of successive values of the dependent variable: $x_0, x_1, x_2, ...$

Let us exploit the idea in the third point for graphical analysis of an iterated map. Starting with some initial condition $x_0$, the value of $x_1$ is given by $f(x_0)$. To show this graphically, starting the point $x_0$ on the axis, draw a vertical line to $y=f(x_0)$. Next, draw a horizontal line to the graph of $y=x$. Since the $y$ and $x$ coordinates are equal, we now have the value of $x_1 = f(x_0)$ as the x coordinate. Then, repeat the process by drawing a vertical line to $y=f(x_1)$, and the a horizontal line $y=x$, etc. The resulting sequence of x coordinates is a quick way of assessing the dynamics of the iterated map. For instance, the values may converge to a fixed point, or grow to infinity, or bounce around without settling down. The resulting graph of alternating vertical and horizontal line segments is called a cobweb plot, and we will see its usefulness in the synthesis section. 

We now have at our disposal analytical, numerical, and graphical tools to analyze and predict the behavior of a dynamical system. In the next section we will use all three to analyze a more complex model of population growth.

## Analysis of logistic population model

### rescaling the logistic model

First, let us do one more modification of the model, by taking the
parameter $r$ as the common multiple:

$$
N_{t+1} = r(1 - \frac{K}{r} N_t) N_t
\label{discrete_logistic2}
$$

As we saw, the parameter $K$ has dimension of inverse population size, and that the parameter $r$ is dimensionless. We can now use rescaling of the variable $N$ to simplify the logistic model. The goal is to reduce the number of parameters, by canceling some, and bringing the rest into one place, where they can be combined into a *dimensionless group*. Here is how this is accomplished for this
model:

1.  Pick a number of the same dimension as the variable, called the scale, and divide the variable by it. In this case, let the scale for population be $r/K$, so then the new variable is

$$
\tilde N = \frac{NK}{r}  \Longrightarrow N = \frac{\tilde N r}{ K }
$$

Since the parameter $K$ has dimension of inverse population size, $NK$ is in the dimensionless variable $\tilde N$.

2.  Substitute $ \tilde N / K $ for $N$ in the equation:

$$
\frac{\tilde N_{t+1}r }{ K} = r\left(1  -\frac{ K \tilde N_t  r}{rK} \right) \frac{\tilde N_t r} {K}
$$

3.  Canceling all the parameters on both sides, we just have the dimensionless growth rate $r$, as our only parameter:

$$
\tilde N_{t+1}  = r(1 -\tilde N_t)\tilde N_t
$$

On the surface, we merely used algebraic trickery to simplify the equation, but the result is actually rather deep. By changing the dimension of measurement of the population from individuals ($N$) to the dimensionless fraction of the carrying capacity ($\tilde N$) we found that there is only one parameter $r$ that governs the behavior of this model. We will see in the next two section that varying this parameter leads to dramatic changes in the dynamics of the model population. [@edelstein-keshet_mathematical_2005]

### fixed point analysis

The first step for qualitative analysis of a nonlinear model is to find the fixed points. We use the dimensionless version of the logistic equation, and the right-hand side function equal to the value of the special values $N^*$ (fixed points):

$$
r(1 - N^*) N^* = N^*
$$

There are two solutions to this equation, $N^* = 0$ and $N^* = (r-1)/r$. These are the fixed points or the equilibrium population sizes for the model, the first being the obvious case when the population is extinct. The second equilibrium is more interesting, as it describes the *carrying capacity* of a population in a particular environment. To determine what happens to the solution, we need to evaluate the stability of both equilibria.

We have seen in the analytical section that the stability of fixed points is determined by the derivative of the defining function at the fixed points. The derivative of $f(N) = rN-rN^2$ is $f'(N) = r-2rN$, and we evaluate it at the two fixed points:

$$
f'(0) = r; \; \; f'((r-1)/r) = r-2(r-1) = 2-r
$$

Because the intrinsic death rate cannot be greater than the birth rate, we know that $r>0$. Therefore, we have the following stability conditions for the two fixed points:

 * the fixed point $N^*=0$ is stable for $r<1$, and unstable for $r>1$;

 * the fixed point $N^*= (r-1)/r$ is stable for $1<r<3$, and unstable otherwise.

We can plot the solution for the population size of the logistic model population over time. We see that, depending on the value of the parameter $r$ (but not on $k$), the behavior is dramatically different:

**Case 1: $r < 1$.** The fixed point at $N^*= 0$ is stable and the fixed point is unstable $N^* = (r-1)/r$. The solution tends to 0, or extinction, regardless of the initial condition, which is illustrated in figure \[fig:sol\_logistic\_2\] for $r=0.8$.

**Case 2: $1 < r < 3$.** The extinction fixed point $N^*= 0$ is unstable, but the carrying capacity fixed point $N^* = (r-1)/r$ is stable. We can conclude that the solution will approach the carrying capacity for most initial conditions. This was shown in figure \[fig:sol\_logistic\_1\] for $r=1.5$ and is illustrated in figure \[fig:sol\_logistic\_3\] for $r=2.8$. Notice that although the solution approaches the carrying capacity equilibrium in both cases, when $r>2$, the solution oscillates while converging to its asymptotic value, foreshadowing the behavior when $r>3$.

**Case 3: $ r > 3$.** Strange things happen: there are no stable fixed points, so there is no value for the solution to approach. As we saw in the previous section, the solution can undergo so-called period two oscillations, which are shown in figure \[fig:sol\_logistic\_4\] with $r=3.3$. However, even stranger behavior is observed when the parameter $r$ crosses the threshold of about $3.59$. Figure \[fig:sol\_logistic\_5\] shows the behavior of the solution for $r=3.6$, which is no longer periodic, and instead seems to bounce around without any discernible pattern. This dynamics is known as *chaos*.

### graphical analysis of the logistic model

As we saw in section 1.4, we can learn a lot about the behavior of a dynamical system from analyzing the graph of the defining function. Let us consider two quadratic functions for the logistic model: $f(N) = 2N(1-N/2)$ and $f(N) = 4N(1-N/4)$ .

First, plotting the graphs of $y=f(N)$ and $y=N$, allows us to find the fixed points of the logistic model. Since it is a , we see that there are fixed points at $N = 0$ for both functions, and carrying capacity sizes at $N=2$ and $N=3$, respectively. The reader should check that this is in agreement with the analytic prediction of $N^* = (r-1)/r$.

Second, we can obtain information about stability of the two fixed points by considering the slope of the curve $y=f(N)$ at the points where it crosses $y=N$. On the graph of the first function, the slope is clearly 0, which indicates that the fixed point is stable, in agreement with the analytical prediction. On the graph of the second function, the slope is negative and steeper than -1. This indicates that the fixed point is unstable, again consistent with our analysis above.

Third, we graph a few iterations of the cobweb plot to obtain an idea about the dynamics of the population over time. As expected, for the first function with $r=2$, the solution quickly approaches the carrying capacity ({numref. In the second function, however, $r = 4$ and the carrying capacity is unstable. In {numref}`fig-cobweb2` we observe a wild pattern of jumps that never approach any particular value.


```{figure} images/ch1_cobweb_1.png
---
name: fig-cobweb1
---
Cobweb plot of the logistic model with $r=2$, showing a solution converging to the stable fixed point at the intersection of the graphs of the function and the identity line
```



```{figure} images/ch1_cobweb_2.png
---
name: fig-cobweb2
---
Cobweb plot of the logistic model with $r=4$, showing a as solution bouncing around the unstable fixed point
```

We have seen how graphical tools can be used to analyze and predict the behavior of a dynamical system. In the case of the logistic model, we never found the analytic solution, because it frequently does not exist as a formula. Finding the fixed points and analyzing their stability, in conjunction with looking at the behavior of a cobweb plot, allowed us to describe the dynamics of population growth in the logistic model, without doing any “mathematics”. Together, the analytical and graphical
analysis provide complementary tools for biological modelers.

### chaos in discrete dynamical systems

In this chapter we learned to analyze the dynamics of solutions of
nonlinear discrete-time dynamical systems without solving them on paper. In the last two sections we focused on the logistic difference equation as a simple nonlinear model with a rich array of dynamic behaviors. In this section we will summarize the analysis and draw conclusions for difference equation models in biology. This behavior was brought to the attention of biologists by John Maynard Smith [@smith_mathematical_1968] and Robert May [@may_bifurcations_1976].

Why does the logistic model behave so strangely in the second example above? We can use numerical simulations to plot the long-term solutions for the dependent variable for a range of parameter values, let us say between $2.5 < r < 4$. Then we plot the values to which the simulation converged (whether it is one, two, or many) on the y-axis, and the value of the parameter $r$ on the x-axis. The resulting *bifurcation diagram* in shown in figure. The value of the parameter $r$ is plotted on the horizontal axis, and the set of values that the dependent variable takes in the long run is shown on the vertical axis. There is only one stable fixed point for $r<3$, then we see a 2-cycle appear for $3<r<3.45$. For values of $r$ greater than about 3.45, a series of period-doubling bifurcations occur with shorter and shorter intervals of $r$. This is called a *period-doubling cascade*, which culminates at the value of $r \approx 3.57$, where the number of points in the cycle becomes essentially infinite. The sequence of values of $r$ at which period-doubling occurs is approximately:

*   period 2; $r_1 = 3$

*   period 4; $r_2 \approx 3.449$

*   period 8; $r_3 \approx  3.544$

*   period 16; $r_4 \approx  3.564$

*   period 32; $r_5 \approx 3.569$

*   period $\infty$ (chaos); $r_\infty \approx  3.570$

![Bifurcation diagram for the logistic map $N(t+1)  = r(1 - N(t)) N(t)$, with the parameter $r$ on the horizontal axis and the vertical axis showing the values of the stable fixed point (for $r<3$), then the values of the period two oscillation, the period four oscillation, etc., and for $r$ greater than the critical value shows some of the values the solution chaotically jumps
through.](images/logistic_bifurc.png)

For $r > r_\infty$, we observe a remarkable behavior found only in
nonlinear dynamical systems, called *chaos*. Chaos is characterized by two qualities:

1.  **Aperiodic behavior**: the dependent variable never repeats a value exactly, instead bouncing around an infinite set of values for all time

2.  **Sensitive dependence on initial conditions**: no matter how close two initial conditions in a chaotic system, given enough time the two trajectories will diverge and lose any resemblance

What is especially surprising about chaos is that for a given initial condition a chaotic model gives a completely predictable and reproducible sequence of values of the dependent variable. However, given finite machine precision, or any error in initial conditions, a chaotic system is practically unpredictable and irreproducible. But there is a fundamental difference between deterministic chaos and a stochastic system, e.g. the model of coin tosses where knowing the previous result of the coin flip does not allow us to predict the next result, even under ideal conditions.

Notice in figure , that for $r > r_\infty$, chaotic behavior is observed only for some values of $r$. As you can see in figure , there are “bands of periodicity”, where the attractor is a  sequence of $n$ numbers (and periods of 3,5, etc. are observed), alternating with bands of chaos. This illustrates that even the simplest nonlinear discrete dynamical systems can have incredibly complex behavior. When these results were first published by May in the 1970s, they revolutionized both the mathematical understanding of dynamical systems, and the field of theoretical biology. In one-variable dynamic systens, chaos occurs only in discrete-time dynamical models, but for three or more variables continuous time (ODE) dynamical systems also can behavechaotically.

As a mathematical side-note, if one looks at the differences between successive values of $r_n$, they behave like a geometric sequence, getting smaller and smaller by a constant fraction:

$$
\delta_n = \frac{r_{n}-r_{n-1}}{r_{n+1}-r_{n}}
$$

It is a remarkable fact that $\delta_n$ approaches a constant value when $n$ gets large, $4.6692...$, known as the Feigenbaum constant. It can be proven that this constant is the same for other iterated maps with the same shape as the downward parabola of the logistic map (e.g. $f(x) = \sin(x)$). Explaining why this deep mathematical fact is true is far outside the bounds of this course. [@strogatz_nonlinear_2001]

Chaos was a popular topic back in the 1980s and 90s, and even inspired popular books [@gleick_chaos:_1988]. It is in fact remarkable that very simple difference equations can have solutions of apparently great complexity. This is intriguing because it appeals to a fairly universal human desire for simple explanations for complicated phenomena. The popular exposure to what was dubbed “chaos theory” (which is not an actual mathematical topic) spawned some inaccurate cliches, such as “a butterfly flapping its wings in South America can cause a hurricane to form and hit Florida”. The image refers to the phenomenon of sensitive dependence on initial conditions, but of course it is utterly ridiculous to draw a causal arrow between a butterfly (one of an enumerable number of things changing the “initial conditions”) and large-scale atmospheric phenomena. While there is some evidence that weather patters are complex systems that exhibit chaotic behavior, we lack the ability to isolate and control all influences that may perturb it, so pinning it on a butterfly is pretty unfair.

Despite the initial flurry of excitement, so-called chaos theory has
failed to make a big impact on our understanding of complex biological
systems. Although it is still quite fascinating intellectually, a simple
model like the logistic model is not an adequate model for any realistic
population, particularly for large values of $r$ where the chaotic
behavior occurs. We now appreciate that the essential complexity of
biological system requires multiple interacting variables which cannot
be reduced to a single equation. However, there has been some successful
observation of chaotic behavior in a population of flour beetles, which
seemed to agree with predictions of a three-variable difference equation
model [@costantino_chaotic_1997].

We have seen how graphical tools can be used to analyze and predict the
behavior of a discrete-time dynamical system. We investigated the
logistic model by finding the fixed points and analyzing their
stability. Together with analysis of the graph of the updating function
and making a cobweb plot, this allowed us to describe the dynamics of
population growth in the logistic model, without doing any “math”.
Together, analytical and graphical analysis provide powerful tools for
biological modelers.
