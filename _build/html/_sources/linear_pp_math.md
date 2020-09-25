## Flow in the phase plane


### activators and inhibitors in biochemical reactions

Suppose two gene products (proteins) regulate each others’ expression. Activator protein $A$ binds to the promoter of the gene for $I$ and activates its expression, while inhibitor protein $I$ binds to the promoter of the gene for $A$ and inhibits its expression (here the variables stand for concentrations of the two proteins in the cell):

$$
\begin{aligned}
\dot  A & = & - \alpha I\\
\dot  I & = & \beta A\end{aligned}
$$ 

$\alpha$ and $\beta$ are positive rate constants. They represent the rate of inhibition of $A$ by $I$, and of activation of $I$ by $A$, respectively. Let us now complicate the model by adding self-inhibition. It is common for regulatory proteins to
inhibit their own production. Then, we have the following system of equations: 

$$
\begin{aligned}
\dot  A & = & - \gamma A - \alpha I\\
\dot  I & = & \beta A - \delta I
\end{aligned}
$$ 

Here we have added two rates of self-inhibition $\gamma$ and $\delta$. This is a system of two coupled ODEs, and we will learn how to analyze these models both analytically and graphically.

### phase plane portraits

Before we learn about the analytical tools of linear algebra, let us think intuitively about the effect of the variables on each other. The best way to describe this is through plotting the geometry of the *flow* prescribed by the differential equations. As we saw, for one-dimensional ODEs the direction of the change of the dependent variable (also known as the flow) could be shown as arrows on a line. A single variable can only increase, decrease, or stay the same (at a fixed point). In two dimensions there is more freedom. The flow is plotted on the *phase plane*, where for any combination of the two variables (say $x,y$) the ODE gives the derivatives of $x$ and $y$. This vector gives the flow, or the rate of change at the particular point in the plane. Intuitively, the flow describes the direction in which the system is pulling the 2-dimensional solution. If we plot the progress of a solution of ODE (all the values of $x$ and $y$ starting with the initial condition) we will obtain a *trajectory* in the phase plane. The arrows of the flow are tangent to any trajectory curve, since they plot the derivatives of $x,y$.

**Example: positive relationship between the variables** Consider the following system of differential equations: 

$$
\\begin{aligned}
\dot x & = & x + y \\
\dot y & = & x + 2y 
\end{aligned}
$$ (eq-ode1)

This is system is coupled, with $x$ having an effect on $y$ and vice versa. Specifically, the signs of the constants mean that positive values of $x$ have the effect of increasing $y$ (and vice versa), while negative values of $x$ have the effect of decreasing $y$ (and vice versa). For any pair of values of $(x,y)$, there is a flow prescribed by the ODEs. E.g., when $x=1, y=1$, the derivatives are $\dot x = 2, \dot y = 3$. This means that the flow at that point is given by the vector $(2,3)$, and can be plotted in the $x,y$ phase plane. This can be done for any pair of values of $x$ and $y$, and plotted to give the phase plane portrait in figure {numref}`fig-ode1`.


```{figure} images/week6_pp5.png
---
name: fig-ode1
---
Phase plane flow for the system in {eq}`eq-ode1`
```


Observe that the overall dynamics of the systems are directed outward from the origin, as we expect from the ODEs. The blue lines on the plot are some sample trajectories. The solution over time for both $x$ and $y$ will either grow toward positive infinity, or decay to negative infinity.

**Example: negative relationship between the variables** Consider the following system of differential equations, where $y$ has an effect on $\dot x$ opposite of its own sign. That is, negative values of $y$ contribute to the growth of $x$, and vice versa. 

$$
\begin{aligned}
\dot x & = & -y \\
\dot y & = & x  
\end{aligned}
$$ (eq-ode2)

As above, the flow at any one point is given by the ODEs. E.g. at $(0,1)$ the two derivatives prescribe flow in the $(1,0)$ (up) direction, while at $(1,0)$ the flow is in the $(0,-1)$ direction. Figure {numref}`fig-ode2` shows the arrows of flow in the phase plane around the origin. Note that the arrows go around in a circular pattern around the origin - this shows oscillatory flow of solutions.

```{figure} images/week6_pp2.png
---
name: fig-ode2
---
Phase plane flow for the system in {eq}`eq-ode2`
```

Let us consider the trajectories of $x$ and $y$ in time. The blue curves in the phase plane plot demonstrate the solutions go around the origin and return to the same point. This means that the behavior of the solutions over time is *periodic*, with oscillations going from positive to negative numbers and back forever.

## Eigenvectors and eigenvalues


### basic linear algebra terminology

We have seen matrix notation introduced in the previous chapter, along with the definition of matrix multiplication. One basic advantage of this notation is that it makes it possible to write any set of *linear equations* as a single matrix equation. By linear equations we mean those that contain only constants or first powers of the variables. The field of mathematics studying matrices and their generalizations is called *linear algebra*; it is fundamental to both pure and applied mathematics. In this section we will learn some basic facts about matrices and their properties. First of all, let us define some basic terms:

```{admonition} Matrix definition

*  A matrix $A$ is a rectangular array of *elements* $A_{ij}$, in which $i$ denotes the row number (index), counted from the top, and $j$ denotes the column number (index), counted from left to right.

*  The elements of a matrix $A$ which have the same row and column index, e.g. $A_{33}$ are called the *diagonal elements*. Those which do not lie on the diagonal are called the *off-diagonal* elements. 

* The *trace* $\tau$ of a matrix $A$ is the sum of the diagonal elements: $\tau = \sum_i A_{ii}$

* The *determinant* $\Delta$ of a 2x2 matrix $A$ is given by the following: $\Delta = ad - bc$, where

$$
A = \left(\begin{array}{cc}a & b \\c & d\end{array}\right)
$$ 

For larger matrices, the determinant is defined recursively, in terms of 2x2 submatrices of the larger matrix, but we will not give the full definition here.
```

For example, in the 3 x 3 matrix below, the elements $a, e, i$ are the diagonal elements:
    
$$
A = \left(\begin{array}{ccc}a & b & c \\d & e & f \\g & h & i\end{array}\right)
$$


In chapter 3 you learned the rule of matrix multiplication, and we can write $C = A \times B$, so long as the number of columns in $A$ matches the number of rows in $B$. However, what if we want to reverse the process? If we know the resulting matrix $C$, and one of the two matrices, e.g. $A$, how can we find $B$? Naively, we would like to be able to divide both sides by the matrix $A$, and find $B = C/A$. However, things are more complicated for matrices.

Properly speaking, we need to introduce the *inverse* of a matrix $A$. If we think about inverses of real numbers, $a^{-1}$ is a number that when it multiplies $a$, results in one. In order to define the equivalent for matrices, we first need to introduce the unity of matrix multiplication.

```{admonition} Definition 
The *identity* matrix is an $n$ by $n$ matrix that does not change another $n$ by $n$ matrix by multiplication:

$$
A \times I = I \times A  = A
$$ 

The diagonal elements of the identity matrix are 1s and all off-diagonal elements are zero.
```

**Example:** Useing the definition of matrix multiplication from chapter 3, we can verify that this definition works for any 2 by 2 matrix:


$$
\begin{pmatrix}-6 & -2 \\ 12 & -1 \end{pmatrix} \times \begin{pmatrix} 1 & 0 \\ 0 & 1\end{pmatrix} = 
\begin{pmatrix}-6\times 1 + -2\times 0 & -6\times 0 + -2\times 1  \\ 12\times 1 -1 \times 0 & 12\times 0 -1 \times 1  \end{pmatrix} = \begin{pmatrix}-6 & -2 \\ 12 & -1 \end{pmatrix}
$$


Now that we have specified the identity, we can define the matrix inverse:
```{admonition} Definition 
A square matrix $A$ has an *inverse matrix* $A^{-1}$ if it satisfies the following: 

$$
A^{-1} A = A A^{-1} = I
$$
```

Finding the inverse of a matrix is not simple, and we will be content to let computers handle the dirty work. In fact, not every matrix possesses an inverse. There is a test for existence of an inverse of $A$, and it depends on the determinant [@strang_linear_2005]:

A square matrix $A$ possesses an inverse $A^{-1}$ and is called *invertible* if and only if its determinant is not zero.

### matrices transform vectors

In this section we will learn to characterize square matrices by finding special numbers and vectors associated with them. At the core of this analysis lies the concept of a matrix as an *operator* that transforms vectors by multiplication, as we defined in chapter 3. To be clear, in this section we take as default that the matrices $A$ are square, and that vectors $\vec v$ are column vectors, and thus will multiply the matrix on the right: $A \times  \vec v$.

A matrix multiplied by a vector produces another vector, provided the number of columns in the matrix is the same as the number of rows in the vector. This can be interpreted as the matrix transforming the vector $\vec v$ into another one: $ A  \times  \vec v = \vec u$. The resultant vector $\vec u$ may or may not resemble $\vec v$, but there are special vectors for which the transformation is very simple.

**Example.** Let us multiply the following matrix and vector (specially chosen to make a point):

$$
\left(\begin{array}{cc}2 & 1 \\ 2& 3\end{array}\right)\left(\begin{array}{c}1 \\ -1 \end{array}\right) = \left(\begin{array}{c}2 -1 \\ 2 - 3 \end{array}\right) =  \left(\begin{array}{c} 1 \\ -1 \end{array}\right)
$$

We see that this particular vector is unchanged when multiplied by this matrix, or we can say that the matrix multiplication is equivalent to multiplication by 1. Here is another such vector for the same matrix:

$$
\left(\begin{array}{cc}2 & 1 \\ 2& 3\end{array}\right)\left(\begin{array}{c}1 \\ 2 \end{array}\right) = \left(\begin{array}{c}2 +2 \\ 2 + 6 \end{array}\right) =  \left(\begin{array}{c} 4 \\ 8 \end{array}\right)
$$

In this case, the vector is changed, but only by multiplication by a constant (4). Thus the geometric direction of the vector remained unchanged.

Generally, a square matrix has an associated set of vectors for which multiplication by the matrix is equivalent to multiplication by a constant. This can be written down as a definition:

```{admonition} Definition 
An *eigenvector* of a square matrix $A$ is a vector $\vec v$ for which matrix multiplication by $A$ is equivalent to multiplication by a constant. This constant $\lambda$ is called its *eigenvalue* of $A$ corresponding the the eigenvector $\vec v$. The relationship is summarized in the following equation:

$$
A  \times  \vec v = \lambda \vec v
$$ (def-eigen)
```

Note that this equation combines a matrix ($A$), a vector ($\vec v$) and a scalar $\lambda$, and that both sides of the equation are column vectors. This definition is illustrated in {numref}`fig-eig-vec`, showing a vector ($v$) multiplied by a matrix $A$, and the resulting vector $\lambda v$, which is in the same direction as $v$, due to scalar multiplying all elements of a vector, thus either stretching it if $\lambda>1$ or compressing it if $\lambda < 1$. This assumes that $\lambda$ is a real number, which is not always the case, but we will leave that complication aside for the purposes of this chapter.


```{figure} images/Eigenvalue_equation.png
---
name: fig-eig-vec
---
Illustration of the geometry of a matrix $A$ multiplying its eigenvector $v$, resulting in a vector in the same direction
$\lambda v$. (Figure by Lantonov under CC BY-SA 4.0 via Wikimedia Commons)
```

The definition does not specify how many such eigenvectors and eigenvalues can exist for a given matrix $A$. There are usually as many such vectors $\vec v$ and corresponding numbers $\lambda$ as the number of rows or columns of the square matrix $A$, so a 2 by 2 matrix has two eigenvectors and two eigenvalues, a 5x5 matrix has 5 of each, etc. One ironclad rule is that there cannot be more distinct eigenvalues than the matrix dimension. Some matrices possess fewer eigenvalues than the matrix dimension, those are said to have a *degenerate* set of eigenvalues, and at least two of the eigenvectors share the same eigenvalue.

The situation with eigenvectors is trickier. There are some matrices for which any vector is an eigenvector, and others which have a limited set of eigenvectors. What is difficult about counting eigenvectors is that an eigenvector is still an eigenvector when multiplied by a constant. You can show that for any matrix, multiplication by a constant is commutative: $cA = Ac$, where $A$ is a matrix and $c$ is a constant. This leads us to the important result that if $\vec v$ is an eigenvector with eigenvalue $\lambda$, then any scalar multiple $c \vec v$ is also an eigenvector with the same eigenvalue. The following demonstrates this algebraically:

$$
A  \times  (c \vec v) = c A  \times  \vec v = c \lambda \vec v =  \lambda (c \vec v)
$$

This shows that when the vector $c \vec v$ is multiplied by the matrix $A$, it results in its being multiplied by the same number $\lambda$, so by definition it is an eigenvector. Therefore, an eigenvector $\vec v$ is not unique, as any constant multiple $c \vec v$ is also an eigenvector. It is more useful to think not of a single eigenvector $\vec v$, but of a **collection of vectors that can be interconverted by scalar multiplication** that are all essentially the same eigenvector. Another way to represent this, if the eigenvector is real, is that an eigenvector as a **direction that remains unchanged by multiplication by the matrix**, such as direction of the vector $v$ in figure . As mentioned above, this is true only for real eigenvalues and eigenvectors, since complex eigenvectors cannot be used to define a direction in a real space.

To summarize, eigenvalues and eigenvectors of a matrix are a set of numbers and a set of vectors (up to scalar multiple) that describe the action of the matrix as a multiplicative operator on vectors. “Well-behaved” square $n$ by $n$ matrices have $n$ distinct eigenvalues and $n$ eigenvectors pointing in distinct directions. In a deep sense, the collection of eigenvectors and eigenvalues defines a matrix $A$, which is why an older name for them is characteristic vectors and values.

### calculating eigenvalues

Finding the eigenvalues and eigenvectors analytically, that is on paper, is quite laborious even for 3 by 3 or 4 by 4 matrices and for larger ones there is no analytical solution. In practice, the task is outsourced to a computer, and MATLAB has a number of functions for this purpose. Nevertheless, it is useful to go through the process in 2 dimensions in order to gain an understanding of what is involved. From the definition \[def:eigen\] of eigenvalues and eigenvectors, the condition can be written in terms of the four elements of a 2 by 2 matrix:

$$
\left(\begin{array}{cc}a & b \\c & d\end{array}\right)\left(\begin{array}{c}v_1 \\ v_2 \end{array}\right) = \left(\begin{array}{c}av_1 +b v_2\\ cv_1+ dv_2 \end{array}\right) = \lambda \left(\begin{array}{c}v_1 \\ v_2 \end{array}\right)
$$

This is now a system of two linear algebraic equations, which we can solve by substitution. First, let us solve for $v_1$ in the first row, to get 

$$
v_1 = \frac{-bv_2}{a-\lambda}
$$ 

Then we substitute this into the second equation and get:

$$
\frac{-bcv_2}{a-\lambda} +(d-\lambda)v_2 = 0
$$ 

Since $v_2$ multiplies both terms, and is not necessarily zero, we require that its multiplicative factor be zero. Doing a little algebra, we obtain the following, known as the *characteristic equation* of the matrix:

$$
-bc +(a-\lambda)(d-\lambda) = \lambda^2-(a+d)\lambda +ad-bc = 0
$$ 

This equation can be simplified by using two quantities we defined at the beginning of the section: the sum of the diagonal elements called the trace $\tau = a+d$, and the determinant $\Delta = ad-bc$. The quadratic equation has two solutions, dependent solely on $\tau$ and $\Delta$:

$$
\lambda = \frac{\tau \pm \sqrt{\tau^2-4\Delta}}{2}
$$ 

This is the general expression for a 2 by 2 matrix, showing there are two possible eigenvalues. Note that if $\tau^2-4\Delta>0$, the eigenvalues are real, if $\tau^2-4\Delta<0$, they are complex (have real and imaginary parts), and if $\tau^2-4\Delta=0$, there is only one eigenvalue. This situation is known as degenerate, because two eigenvectors share the same eigenvalue.

**Example.** Let us take the same matrix we looked at in the previous subsection:

$$
A = \left(\begin{array}{cc}2 & 1 \\ 2& 3\end{array}\right)
$$ 

The trace of this matrix is $\tau = 2+3 =5$ and the determinant is $\Delta = 6 - 2 = 4$. Then by our formula, the eigenvalues are:

$$
\lambda = \frac{5 \pm \sqrt{5^2-4 \times 4}}{2}  =  \frac{5 \pm 3}{2}  = 4, 1
$$

These are the multiples we found in the example above, as expected.

A real matrix can have complex eigenvalues and eigenvectors, but whenever it acts on a real vector, the result is still real. This is because the complex numbers cancel each other’s imaginary parts. For discrete time models, it is enough to consider the absolute value of a complex eigenvalue, which is defined as following: $|a +b i|= \sqrt{a^2 + b^2}$. As before, the eigenvalue with the largest absolute value “wins” in the long term.

### calculation of eigenvectors on paper

The surprising fact is that, as we saw in the last subsection, the eigenvalues of a matrix can be found without knowing its eigenvectors! However, the converse is not true: to find the eigenvectors, one first needs to know the eigenvalues. Given an eigenvalue $\lambda$, let us again write down the defining equation of the eigenvector for a generic 2 by 2 matrix:

$$
\left(\begin{array}{cc}a & b \\c & d\end{array}\right)\left(\begin{array}{c}v_1 \\ v_2 \end{array}\right) = \left(\begin{array}{c}av_1 +b v_2\\ cv_1+ dv_2 \end{array}\right) = \lambda \left(\begin{array}{c}v_1 \\ v_2 \end{array}\right)
$$

This vector equation is equivalent to two algebraic equations:

$$
\begin{aligned}
av_1 + b v_2 &= \lambda v_1 \\
cv_1 + d v_2 &= \lambda v_2 
\end{aligned}
$$ 

Since we’ve already found $\lambda$ by solving the characteristic equation, this is two linear equations with two unknowns ($v_1$ and $v_2$). You may remember from advanced algebra that such equations may either have a single solution for each unknown, but sometimes they may have none, or infinitely many solutions. Since there are unknowns on both sides of the equation, we can make both equations be equal to zero: 

$$\begin{aligned}
(a-\lambda)v_1 + b v_2 &= 0 \\
cv_1 + (d-\lambda ) v_2 &=0
\end{aligned}
$$ 

So the first equation yields the relationship $v_1 = -v_2 b/(a-\lambda)$ and the second equation is $v_1 = -v_2(d-\lambda)/c$, which we already obtained in the last subsection. We know that these two equations must be the same, since the ratio of $v_1$ and $v_2$ is what defines the eigenvector. So we can use either expression to find the eigenvector.

**Example.** Let us return to the same matrix we looked at in the previous subsection:

$$
A = \left(\begin{array}{cc}2 & 1 \\ 2& 3\end{array}\right)
$$ 

The eigenvalues of the matrix are 1 and 4. Using our expression above, where the element $a=2$ and $b=1$, let us find the eigenvector corresponding to the eigenvalue 1: 

$$
v_1 = - v_2 \times  1/(2-1) = - v_2
$$ 

Therefore the eigenvector is characterized by the first and second elements being negatives of each other. We already saw in the example two subsections above that the vector $(1,-1)$ is such as eigenvector, but it is also true of the vectors $(-1,1)$, $(-\pi, \pi)$ and $(10^6, -10^6)$. This infinite collection of vectors, all along the same direction, can be described as the eigenvector (or eigendirection) corresponding to the eigenvalue 1.

Repeating this procedure for $\lambda = 4$, we obtain the linear relationship: $$v_1 = - v_2 \times  1/(2-4) = 0.5 v_2$$ Once again, the example vector we saw two subsections $(2,1)$ is in agreement with our calculation. Other vectors that satisfy this relationship include $(10,5)$, $(-20,-10)$, and $(-0.4,-0.2)$. This is again a collection of vectors that are all considered the same eigenvector with eigenvalue 4 which are all pointing in the same direction, with the only difference being their length.


## Solutions of linear two-variable ODEs


Let us start by considering two variable ODEs that do not affect each other: 

**Example: two uncoupled ODEs**  In general, for a two-variable system, the value of one variable affects the other. In the equations above, the terms with the constants $b$ and $c$ provide what is known as *coupling* between the two variables. Let us look at the primitive situation where the two variables are uncoupled, as an illustration of solving two-dimensional ODEs. If we set the coupling constants $b$ and $c$ to 0, we get: 

$$
\begin{aligned}
\dot x & = & ax \\
\dot y & = & dy
\end{aligned}
$$ 

Using our knowledge of 1D linear ODE, we can solve the two equations independently to get the following: $x(t) = x_0 e^{at}$ and $y(t) = y_0 e^{dt}$. The solutions can be written in vector form:

$$
\left(\begin{array}{c}x(t) \\y(t)\end{array}\right) =
x_0 e^{at} \left(\begin{array}{c}1 \\0\end{array}\right)+y_0 e^{dt}\left(\begin{array}{c}0\\1\end{array}\right)
$$

This is another way of writing that the dynamics of variable $x$ is exponential growth (or decay) with rate $a$, and ditto $y$, with rate $d$. Given the initial conditions $(x_0, y_0)$, we can divide the behavior of the solutions into a sum of two vectors, each growing or decaying at its own rate.

Linear algebra allows us to find the solution for two-dimensional ODEs where the variables are interdependent using the same idea. The general (homogeneous) ODE with two dependent variables can be written as follows: 

$$
\begin{aligned}
\dot x & = & ax + by \\
\dot y & = & cx + dy
\end{aligned}
$$ 

We can write this in matrix form like this:

$$
\left(\begin{array}{c}\dot x \\ \dot y \end{array}\right) = \left(\begin{array}{cc}a & b \\c & d\end{array}\right)\left(\begin{array}{c}x \\ y \end{array}\right)
$$

Let us call the matrix $A$, and represent the vector $(x,y)$ as $\vec {x}$, then the general linear equation can be written like this: 

$$
\dot{ \vec{ x}} = A \vec{x}
$$ (gen-lin-mult)

This notation is intended to make plain the similarity with the linear 1D ODE: $\dot x = a x$. This similarity is deep and substantial, in that linear equations in multiple dimensions share the same basic exponential form. In general, all solutions of linear equations can be written as a sum of exponentials multiplying different vectors:

```{admonition} General solution of linear 2-variable ODEs
:class: tip
$$
\left(\begin{array}{c} x(t) \\  y(t) \end{array}\right) =C_1e^{\lambda_1 t} \left(\begin{array}{c}x_1\\y_1\end{array}\right)+C_2 e^{\lambda_2 t}\left(\begin{array}{c}x_2\\y_2\end{array}\right)
$$ (gen-sol-2var)

The constants $C_1, C_2$ are determined by the initial conditions, while the constants $\lambda_1, \lambda_2$ are the eigenvalues and the vectors $(x_1,y_1)$ and $(x_2,y_2)$ are the eigenvectors of the matrix $A$. We will now consider the application of this general result using computational tools.
```

## Classification of linear systems

We have seen that linear algebra allows us to write down the solution of a multivariable dynamical system into a sum of exponential terms. In this section we use computational techniques to find the eigenvalues and eigenvectors of a system, and then produce the *phase portraits* of the linear systems. There are only a few different types of flow possible for linear systems, and we will classify them.


### real eigenvalues

Let us consider the fixed points of the linear system: since both $\dot x =0 $ and $\dot y = 0$ must be zero, the only fixed point is the origin $(0,0)$. We will see that the stability of the fixed point depends on the sign of the real part of the eigenvalue.

Suppose we have a positive real eigenvalue. The solution in the direction of the corresponding eigenvector is then described by $Ce^{\lambda t}$, $\lambda > 0$, which is exponential growth. The means that the solution is going to grow in the direction of the eigenvector away from the origin, and thus the origin is an unstable fixed point (in this direction). This type of fixed point is called an *unstable node*.

On the other hand, if $\lambda < 0$ for both eigenvalues, the solution decays exponentially and thus approaches the origin, so the fixed point is stable. This type of fixed point is called a *stable node*.

Since there are two different eigenvalues, one may be positive while another is negative. In this case, the fixed point is is called a *saddle point* for geometric reasons: solutions flow toward it in one direction, like a marble along the forward-backward axis of a saddle on a horse and flow away from it along the sideways direction on a saddle. Then, the fixed point is stable when approached along one eigenvector, but unstable along the other. What happens if the initial condition is not on either eigenvector? I will use a fact of linear algebra that given any two (non-colinear) 2D vectors, any vector in the plane can represented as a sum (with some coefficients) of these two. Thus, the general solution can be written as follows:


$$
\left(\begin{array}{c} x(t) \\  y(t) \end{array}\right) =C_1e^{at} \left(\begin{array}{c}v_1\\v_2\end{array}\right)+C_2 e^{-bt}\left(\begin{array}{c}u_1\\u_2\end{array}\right)
$$


```{figure} images/week6_pp1.png
---
name: fig-saddle
---
Phase plane flow for a linear system with a saddle point
```


where $a,b>0$. Then we see that the component in the direction of the first eigenvector will grow, while the component along the second eigenvector will decay. Thus, as $t \rightarrow \infty$, all solutions will approach the vector with the unstable eigenvalue, except those with initial conditions right on the eigenvector corresponding to the stable eigenvalue. This means that the fixed point is essentially unstable, because only trajectories which start exactly along the stable direction approach the fixed point in the long run, while others, may approach the fixed point for a finite time, flow away when the unstable component with the positive eigenvalue takes over, as shown in figure .


### complex eigenvalues

If the argument of the square root is negative, eigenvalues may be complex numbers, which we can write like this: $a+bi$. Using Euler’s formula, we can write down the time-dependent part of the solutions as the following:

$$
e^{(a + bi)t} = e^{at}e^{bit}= e^{at}(\cos(bt)+i\sin(bt))
$$ 

The behavior of these solutions combines exponential growth or decay from the real part, with the oscillations produced by the imaginary part. This describes either exponentially growing or decaying oscillations, which look like decaying waves in time, or as a spiral in the phase plane:


```{figure} images/lec7_exp_osc.png
---
name: fig-exp-decay
---
Exponentially decaying oscillations in the time plot of the solution $x(t)$
```


```{figure} images/lec7_pp1.png
---
name: fig-stab-spiral
---
Phase plane portrait of a stable spiral
```


Thus we see that the stability of the fixed point with complex eigenvalues depends on the sign of the real part. Purely imaginary eigenvalues produce periodic oscillations, which keep the same amplitude, as we saw in the example in the modeling section.

### classification of linear systems

 Stability | positive real parts |  negative real parts | one positive, one negative | zero real part
-----------|---------------------|----------------------|----------------------------|-----------------
 real:     |    unstable node    |     stable node      |      saddle point          |  fixed line
 complex:  |    unstable spiral  |     stable spiral    |        N/A                 |  center point


Eigenvalues of linear ODEs define type of phase plane


The table above summarizes all the different types of flows in the phase plane possible for linear systems, in terms of the behavior of solutions relative to the fixed point at the origin. If the eigenvalues are real, the solutions will be exponential in nature. There are three possibilities for nonzero eigenvalues: *stable node* (both eigenvalues are negative), *unstable node* (both eigenvalues are positive), and a *saddle point* (mixed signs). If one of the eigenvalues is zero, this means that there is not flow along one direction, so there is a *line of fixed points* in the direction of the corresponding eigenvector (if both
eigenvalues are zero, there is no flow at all.)

For complex eigenvalues, there are three possibilities: if the real part is positive, the solution will grow and oscillate (oscillations with exponentially increasing amplitude), if the real part is negative, the solution will decay and oscillation (oscillations with exponentially increasing amplitude), and if the real part is zero (pure imaginary\ eigenvalues) the solution will oscillate with constant amplitude. The first type is called an *unstable spiral*, the second a *stable spiral*, and the third a *center*. It is not possible for complex eigenvalues of two-dimensional systems to have different signs of real parts, because as the formula shows, the real part is the same for both and is equal to the trace divided by two.

## Dynamics of romantic relationships


We examine a model, taken from [@strogatz_nonlinear_2001], that applies dynamical systems modeling to a pressing concern for many humans: the prediction of dynamics of a romantic relationship. There are several unrealistic assumptions involved in the following model: first, that love or affection can be quantified, second, that any changes in relationship depend only on the emotions of the two people involved, and third, that the rate of change of the two love variables depend linearly on each other.

If we can give those assumptions the benefit of the doubt (which is how all relationships begin), we can write down a system of ODEs to describe a romantically involved couple. Here $X$ and $Y$ are dynamic variables that quantify the emotional states of the two lovers: 

$$\
begin{aligned}
\dot  X & = & aX+ bY \\
\dot  Y & = & cX + dY
\end{aligned}
$$ 

Let us denote positive feelings (love) with positive values of $X,Y$, while negative values signify negative feelings (hate.) The significance of the parameters can be interpreted as follows: $a,d$ describe the response of the two people to their own feelings, while $b,c$ correspond to the effect the other person’s feeling has on their own. For example, a person whose feeling grow as the other person’s affection increases can be modeled with a positive value of $b$ (or $c$). On the other hand, a person whose own feelings are dampened by the other one’s excessively positive emotions, can be decribed by a negative value of $b$ or $c$. Their own feelings can also play a role, either positive or negative, reflected in the sign of the constants $a$ and $d$.

Using mathematical modeling, we can answer the following basic questions:

1.  Given a set of values for parameters $a, b, c, d$, predict the  dynamic behavior of the model relationship.

2.  Find conditions for stability and existence of oscillations in the dynamical system, expressed as a function of the parameters.

To address the first question, here are some simplified scenarios for our two lovers in the model.

**Detached lovers:** Let the emotional state of the two lovers depend only on their own emotions, for example: 

$$
\begin{aligned}
\dot  X & = & X \\
\dot  Y & = &  -Y
\end{aligned}
$$ 

To classify the behavior of the model, we find the eigenvalues of the system. In this case, they are the diagonal elements of the matrix, 1 and -1. This mean that the origin is a saddle point, and therefore it is unstable. In the $X$ direction, the emotions are going to grow without bound, either in the love or hate direction, while in the $Y$ direction, the emotions are going to decay to zero (indifference). This should be no surprise, that since the two equations are independent, the lovers have no emotional effect on each other.

**Lovers with no self-awareness:** Here is an alternate situation: suppose two lovers were not influenced by their own emotions, but were instead attuned to the emotional state of the other. Then we might have the following model, in which lover $X$ reacts in the opposite way by emotions of lover $Y$, but lover $Y$ is, contrariwise, spurred by the love or hate of $X$ in the same direction: 

$$
\begin{aligned}
\dot  X & = & -Y \\
\dot  Y & = &  X
\end{aligned}
$$ 

We find the eigenvalues of the system by using the expression in equation \[eg:2D\_eig\]: $\lambda =  (0 \pm \sqrt{-4})/2 = \pm i$. Pure imaginary eigenvalues tell us that the origin is a center point, with the solutions periodic orbits around the origin. Psychologically, we can interpret this scenario as cycles of love and hate, never growing and never decaying. The magnitude of these oscillations depends on the initial state of the system, that is, the feelings the lovers had at the beginning of the relationship.

We can now address the second question, and find under what circumstances different types of dynamic behaviors occur. We consider the general model, and ask what kinds of eigenvalues are possible for different parameter values. First, we write down the general expression for the eigenvalues, from equation \[eg:2D\_eig\]:


$$
\lambda =  \frac{a+d \pm \sqrt{(a+d)^2-4(ad-bc)}}{2}
$$ 

There are two properties we are interested in: stability and existence of oscillations. Recall that stability is determined by the sign of the real part of the eigenvalues. If the square root is imaginary, then the real part is simply the trace ($a+d$), but if the square root is real, we have to consider the whole expression to determine stability. So let us first state the condition for existence of oscillations (imaginary square root):

1.  Complex eigenvalues: oscillatory solutions $4(ad-bc) > (a+d)^2$. If this expression holds, the square root is imaginary, and the stability is determined by the sign of the trace. That is, if $a+d > 0$, the system is unstable, and will grow into unbounded love or hate, but if $a+d < 0$, then the system is stable, and will spiral to indifference. The special case $a+d = 0$, such as we saw above, means that strictly periodic love/hate cycles are the solutions.

2.  Real eigenvalues: exponential growth and/or decay $4(ad-bc) < (a+d)^2$. In this case, the square root is real, and no oscillatory solutions exist. In order to determine whether this implies exponential growth, decay, or a combination, we must weigh the relative sizes of $(a+d)$ and $\sqrt{(a+d)^2-4(ad-bc)}$. If $|a+d| > \sqrt{(a+d)^2-4(ad-bc)}$, then adding or subtracting the square root does not change the sign of $(a+d)$: if it is negative, both eigenvalues are negative, and the origin is a stable node, and if the trace is positive, the origin is an unstable node. However, if the absolute value of the root outweighs the absolute value of the trace $|a+d| < \sqrt{(a+d)^2-4(ad-bc)}$ , then either adding or subtracting the root will change the sign of the eigenvalues. Therefore, one eigenvalue is positive and the other is negative, and the origin is a saddle point. The emotions will run unchecked in some preferred direction, possibly combining love and hate of the two lovers.

These conditions are not intuitive, and it took some work to express them. The benefit is that now, given any values of the self-involvement parameters $a,d$ and the sensitivity parameters $b,c$ we can predict the long-term dynamics of the model relationship. Whether the results have any bearing on reality, of course, depends on how well the reality is described by these primitive assumptions.
