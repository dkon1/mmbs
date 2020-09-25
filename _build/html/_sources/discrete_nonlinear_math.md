## Logistic population model

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
$$ (discr-log)

This is called the *logistic model* of population growth. As you see, it has two different parameters, $r$ and $K$. If $K = 0$, the equation reduces to the old linear population model. Intuitively, $K$ is the parameter describing the effect of increasing population on the population growth rate. Let us analyze the dimensions of the two parameters, by writing down the dimensions of the variables of the difference equation. The dimensional equation is:

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

### fixed points or equilibria

We have seen that the solutions of difference equations depend on the initial value of the dependent variable. In the examples we have seen so far, the long-term behavior of the solution does not depend dramatically on the initial condition. In more complex systems that we will encounter, there are special values of the dependent variable for which the dynamical system is constant, like in the pile of rocks model.

```{admonition} Definition
For a difference equation in recurrent form $x(t+1) = f(X(t))$, a point $x^*$ which satisfies $f(x^*)=x^*$ is called a *fixed point* or *equilibrium*. If the initial condition is a fixed point, $x_0=x^*$, the solution will stay at the same value for all time, $x(t)=x^*$.
```

The reason these special points are also known as equilibria is due to the precise balance between growth and decay that is mandated at a fixed point. In terms of population modeling, at an equilibrium the birth rates and the death rates are equal. Speaking analytically, in order to find the fixed points of a difference equation, one must solve the equation $f(x^*) = x^*$. It may have none, or one, or many solutions.

**Example.** The linear population models which we analyzed in the previous sections have the mathematical form $N(t+1)= r N(t)$ (where $r$ can be any real number). Then the only fixed point of those models is $N^* = 0$, that is, a population with no individuals. If there are any individuals present, we know that the population will grow to infinity if $|r| > 1$, and decay to 0 if $|r| < 1$. This is true even for the smallest population size, as long as it is not exactly zero.

**Example.** Let us go back to the example of a linear difference equation with a constant term. The equation is $ N(t+1) = -0.5N(t) +10$, and we saw that the numerical solutions all converged to the same value, regardless of the initial value. Let us find the equilibrium value of this model using the definition:

$$
N^* = -0.5N^* +10 \Rightarrow 1.5 N^* = 10  \Rightarrow N^* = 10/1.5 = 20/3
$$

If the initial value is equal to the equilibrium, $N(0)= 20/3$, then the solution will remain constant for all time, since the next value $N(t+1) = -0.5*20/3+10 = 20/3$ remains the same.

**Example: discrete logistic model.** Let us use the simplified version of the logistic equation $N(t+1) = r(1 - N(t)) N(t)$ and set the right-hand side function equal to the variable $N$ to find the fixed points $N^*$: $$r(1 - N^*) N^* = N^*$$ There are two solutions to this equation, $N^* = 0$ and $N^* = (r-1)/r$. These are the fixed points or the equilibrium population sizes for the model, the first being the obvious case when the population is extinct. The second equilibrium is more interesting, as it describes the *carrying capacity* of a population in a particular environment. If the initial value is equal to either of the two fixed points, the solution will remain at that same value for all time. But what happens to solutions which do not start a fixed point? Do they converge to a fixed point, and if so, to which one?

### stability criteria for fixed points

What happens to the solution of a dynamical system if the initial condition is very close to an equilibrium, but not precisely at it? Put another way, what happens if the equilibrium is *perturbed*? To answer the question, we will no longer confine ourselves to the integers, to be interpreted as population sizes. We will instead consider, abstractly, what happens if the smallest perturbation is added to a fixed point. Will the solution tend to return to the fixed point or tend to move away from it? The answer to this question is formalized in the following definition [@strogatz_nonlinear_2001]:

```{admonition} Definition
For a difference equation $x(t+1) = f(x(t))$, a fixed point $x^*$ is *stable* if for a sufficiently small number $\epsilon$, the solution $x(t)$ with the initial condition $x_0 = x^* + \epsilon$ approaches the fixed point $x^*$ as $t \rightarrow \infty$. If the solution $x(t)$ does not approach $x^*$ for any nonzero $\epsilon$, the fixed point is called *unstable*.
```

The notion of stability is central to the study of dynamical systems. Typically, models more complex than those we have seen cannot be solved analytically. Finding the fixed points and determining their stability can help us understand the general behavior of solutions without writing them down. For instance, we know that solutions never approach an unstable fixed point, whereas for a stable fixed point the solutions will tend to it, from some range of initial conditions.

There is a mathematical test to determine the stability of a fixed point. From standard calculus comes the Taylor expansion, which approximates the value of a function near a given point. Take a general difference equation written in terms of some function $x(t+1) = f(x(t))$. Let us define the *deviation* from the fixed point $x^*$ at time $t$ to be $\epsilon(t) = x_{t} - x^*$. Then we can use the linear (first-order) Taylor approximation at the fixed point and write down the following expression:

$$ 
x(t+1) = f(x^*) + \epsilon(t) f'(x^*) + ...
$$ 

The ellipsis means that the expression is approximate, with terms of order $\epsilon(t)^2$ and higher swept under the rug. Since we take $\epsilon(t)$ to be small, those terms are very small and can be neglected. Since $x^*$ is a fixed point, $f(x^*) = x^*$. Thus, we can write the following difference equation to describe the behavior of the deviation from the fixed point $X^*$:

$$
x(t+1) -  x^* =  \epsilon(t+1)= \epsilon(t) f'(x^*)
$$

We see that we started out with a general function defining the difference equation and transformed it into a linear equation for the deviation $\epsilon(t)$. Note that the multiplicative constant here is the derivative of the function at the fixed point: $f'(x^*)$. This is called the *linearization* approach, which is an approximation of a dynamical system near a fixed point with a linear equation for the small perturbation.

We found the solution to simple linear equations, which we can use describe the behavior of the perturbation to the fixed point. The behavior **depends on the value of the derivative of the updating function** $f'(X^*)$:

```{admonition} Important Fact
:class: tip
For a difference equation $x(t+1) = f(x(t))$, a fixed point $x^*$ can be classified as follows:

 * $|f'(x^*)| > 1$: the deviation $\epsilon(t)$ grows, and the solution moves away from the fixed point; fixed point is *unstable*

 * $|f'(x^*)| < 1$: the deviation $\epsilon(t)$ decays, and the solution approaches the fixed point; fixed point is *stable*

 * $|f'(x^*)| = 1 $: the fixed point may be stable or unstable, and more information is needed
```

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



## Analysis of logistic population model

### rescaling the logistic model

First, let us do one more modification of the model, by taking the parameter $r$ as the common multiple:

$$
N_{t+1} = r(1 - \frac{K}{r} N_t) N_t
$$

As we saw, the parameter $K$ has dimension of inverse population size, and that the parameter $r$ is dimensionless. We can now use rescaling of the variable $N$ to simplify the logistic model. The goal is to reduce the number of parameters, by canceling some, and bringing the rest into one place, where they can be combined into a *dimensionless group*. Here is how this is accomplished for this
model:

1.  Pick a number of the same dimension as the variable, called the scale, and divide the variable by it. In this case, let the scale for population be $r/K$, so then the new variable is

$$
\tilde N = \frac{NK}{r}  \Longrightarrow N = \frac{\tilde N r}{ K }
$$

Since the parameter $K$ has dimension of inverse population size, $NK$ is in the dimensionless variable $\tilde N$.

2.  Substitute $\tilde N / K $ for $N$ in the equation:

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
