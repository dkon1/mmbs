---
## higher order difference equations


So far we have dealt with difference equations in which the value of the dependent variable at the next time step $x_{t+1}$ depends solely on the variable at the present time $x_t$. These are known as *first order* difference equations because they only require one step from the present to the future. We will now examine difference equations where the future value depends not only on the present value $x_t$, but also on the past values: $x_{t-1}$, etc. The number of time steps that the equation looks into the past is the the order of the scheme.

### the Fibonacci model and sequence

The Italian mathematician Leonardo Fibonacci, who lived in the late 12th - early 13th centuries, contributed greatly to the development of mathematics in the western world. For starters, he introduced the Hindu-Arabic numerals we use today, in place of the cumbersome Roman numerals. He also constructed an early model of population growth, which considered a population of individuals that lived for two generations. The first generation does not reproduce, but in the second generation each individual produces a single offspring (or each pair produces a new pair) and then dies. Then the total number of individuals at the next time step is the sum of the individuals in the previous two time steps ({numref}`fig-fib-rabbits`) This is described by the following second order difference equation: 

$$
N_{t+1} = N_t + N_{t-1}
$$ (fibonacci)

The famous Fibonacci sequence is a solution of this equation. For a second-order equations, two initial conditions are required, and if we take $N_0 = 0$ and $N_1 = 1$, then the resulting sequence will look as follows:

$$
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
$$

The Fibonacci sequence is famously found in many natural phenomena, including in phyllotaxis (arrangement of parts in plants), and spirals on some mollusk shells, e.g. *Nautilus pompilius* ({numref}`fig-fib-rabbits`). It may be observed by counting the number of spirals that can be drawn between plant units (such as seeds or petals), and observing that alternating the right-handed and left-handed spirals, while moving away from the center, often results in the Fibonacci sequence. The precise reason for this is unclear, although explanations exist, for instance that this pattern provides the most efficient packing of seeds.

```{figure} images/fibonacci-rabbits.png
name: fig-fib-rabbits
---
The Fibbonaci model with each pair of individuals waiting one generation before producing another pair each subsequent generation <https://artblot.wordpress.com/2013/05/10/rich-with-fibonacci-gold/>
```

```{figure} images/fibo_nautilus.jpg
---
name: fig-fib-spiral
---
The shell of the *Nautilus pompilius* mollusk has the shape of a Fibonacci spiral, shown here filled with squares of the corresponding size <http://mathforum.org/mathimages>
```


### matrix representation of discrete time models

The Fibonacci model above can be represented by two equations instead of one, if we consider two dependent variables. Let us represent the number of rabbits in generation 1 (young) by $x$ and in generation 2 (old) by$y$. The new generation at the next time ($t+1$) is comprised of offspring of the young and old generations at time $t$, while the old generation at the next time is simply is young generation at the current time. This gives the following set of equations: 

$$\begin{aligned}
 x_{t+1} & = & x_t + x_{t-1}\\
 x_{t} & = & x_t\end{aligned}
$$
The advantage of re-writing a single equation as two is that the new system is first order, that is, only relies on the values of the variables at the current time $t$. These equations can also be written in *matrix* form:

$$
\left(\begin{array}{c}x_{t+1} \\x_{t}\end{array}\right) = \left(\begin{array}{c}x_t + x_{t-1} \\x_ t \end{array}\right) =   \left(\begin{array}{cc}1 & 1\\1 & 0\end{array}\right) \left(\begin{array}{c}x_t \\ x_{t-1} \end{array}\right)
$$

This representation is convenient and leads to a set of rules for matrix manipulation. We wrote the write-hand side as a product of a matrix containing the coefficients of $x_t$ and $y_t$ and the vector with the two variables. The product of the matrix and the vector is equal to the original vector.


## Solutions for linear higher order difference equations


### solutions of linear difference equations

Solutions for first order linear difference equations are exponential in form. The solutions for second order linear difference equations consist of a sum of two exponentials with different bases. For the following general linear second order difference equation:

$$
x_{t+1} = ax_{t} + b x_{t-1}
$$

The solution can be written as follows:

$$
x_t  = A \lambda_1^t + B \lambda_2^t
$$

The solution for a second order difference equation is a sum of two terms that look like solutions to first order difference equations. There are two different types of constants in the solution: the bases of the exponential $\lambda_1, \lambda_2$ and the multiplicative constants $A$ and $B$. They are different because the exponential parameters depend on the equation itself, but not on the initial conditions, while the multiplicative constants depend only on the initial conditions. Therefore, they can be determined separately:


```{admonition} Outline for solving a second order linear difference equation
:class: tip 
1.  Substitute the solution $x_t = \lambda^t$ into the difference equation. For the general difference equation, we obtain a the
    following quadratic relation by dividing everything by $\lambda^{t-1}$:
$$
\lambda^{t+1} = a \lambda^{t} + b \lambda^{t-1} \Rightarrow \lambda^2 = a\lambda + b
$$

2.  Solve the quadratic equation for values of $\lambda$ which satisfy the difference equation:

$$
\lambda_{1,2} = \frac{a \pm \sqrt {a^2  + 4b} }{2}
$$

If $a^2  + 4b > 0$, this gives two values of $\lambda$; if $a^2  + 4b = 0$, there is a single value, and if $a^2  + 4b < 0$, then no real values of $\lambda$ satisfy the difference equation.

3.  Once we have found the values $\lambda_1$ and $\lambda_2$, use the initial conditions (e.g. some values $x_0$ and $x_1$) to solve for the multiplicative constants:

$$
x_0 = A + B ; \; x_1 = A\lambda_1 + B\lambda_2
$$

Use $A = x_0 - B$ to plug into the second equation: $x_1 = (x_0 - B) \lambda_1 + B \lambda_2$

4.  The general solution for $A$ and $B$ is the following, provided $\lambda_2 \neq \lambda_1$:

$$
B = \frac{x_1 -x_0 \lambda_1}{\lambda_2 - \lambda_1}; \; A =  \frac{x_0\lambda_2 - x_1}{\lambda_2 - \lambda_1}
$$
```

Let us apply this approach to solving the Fibonacci difference equation {eq}`fibonacci`:

$$
\lambda^{2}= \lambda + 1 \Longrightarrow \;  \lambda^2-\lambda-1= 0
$$

We find the solutions by the quadratic formula: $\lambda_{1,2} = (1\pm \sqrt 5)/2 $.

Now let us use the initial conditions $N_0 = 0$ and $N_1 = 1$. The two multiplicative constants must then satisfy the following:

$$
0 = A + B; \; 1 = A\lambda_1 + B\lambda_2
$$

By the formula we found above, the initial conditions are:

$$
A =  \frac{-1}{\lambda_2 - \lambda_1} =  \frac{1}{\sqrt 5} ; \; B = \frac{1}{\lambda_2 - \lambda_1} = \frac{-1}{\sqrt 5}
$$

The complete solution, which gives the $t$-th number in the Fibonacci sequence is:

$$
N_t =  \frac{1}{\sqrt 5}\left( \frac{1+ \sqrt 5}{2}\right)^t - \frac{1}{\sqrt 5}\left(\frac{1- \sqrt 5}{2}\right)^t
$$

There are several remarkable things about this formula. First is the fact that despite the abundance of irrational numbers, for each integer $t$ the number $N_t$ is an integer. One can check this by programming the formula in your favorite language, and plugging in any value of $t$.

Second, an important feature of the Fibonacci sequence is the ratio between successive terms in the sequence. Notice that of the two terms in the formula, $(\frac{1+ \sqrt 5}{2})^t$ grows as $t$ increases, while $(\frac{1- \sqrt 5}{2})^t$ decreases to zero, because the first number is greater than 1, while the second is less than 1. This means that for large $t$, the terms in the Fibonacci sequence are approximately equal to:

$$
N_t \approx \frac{1}{\sqrt 5}\left( \frac{1+ \sqrt 5}{2}\right)^t
$$

Since each successive term is multiplied by $(1+\sqrt5)/2$, the ratio between successive terms, $\phi = N_{t+1}/N_t$ approaches the value $\phi=(1+\sqrt5)/2 \approx 1.618$ for increasing $t$.

This number $(1+\sqrt 5)/2$ is called the *golden ratio* or *golden section*, and was known from antiquity as the most aesthetically pleasing proportion in architecture and art, when used as a ratio between the height and width of the piece of art. Algebraically, the golden ratio is defined to be the number that is both the ratio between two quantities, e.g. $a$ and $b$, and also the ratio between the sum of the two quantities ($a+b$) and the larger of the quantities e.g. $b$ ({numref}`fig-gold-ratio`). Geometrically, the golden ratio can be constructed as the ratio between two sides of a rectangle, $a$ and $b$, which are also part of the larger rectangle with sides $a+b$ and $a$. This construction is shown in {numref}`fig-gold-rect`.

```{figure} images/golden_ratio_line.png
---
name: fig-gold-ratio
---
Line segments that are in golden proportion to each other <http://en.wikipedia.org/wiki/Golden_ratio>
```


```{figure} images/gold_rect_const.png
---
name: fig-gold-rect
---
Cnstruction of a rectangle with the golden ratio between its sides <http://en.wikipedia.org/wiki/Golden_ratio>
```

To show that the geometric golden ratio is the same as the ratio that appears in the Fibonacci sequence, let us write down the algebraic condition stated above. Because we are interested in the ratio, let the smaller quantity be 1 and the larger one be $\phi$; by the definition we obtain the following. $\phi = (\phi+1)/\phi$, thus $\phi^2-\phi-1 = 0$. This is the same quadratic equation that we derived for the exponential bases of the solution above. The solution to this equation (by the quadratic formula) is $\phi=(1\pm\sqrt5)/2$, and the positive solution is the golden ratio.

### elementary matrix operations

Now is a good time to properly define what matrices are and how we can operate on them. We have already seen transition matrices, but just to make sure all of the terms are clear:

A *matrix* $A$ is a rectangular array of *elements* $A_{ij}$, in which $i$ denotes the row number (index), counted from top to bottom, and $j$ denotes the column number (index), counted from left to right. The *dimensions* of a matrix are defined by the number of rows and columns, so an *n by m matrix* contains $n$ rows and $m$ columns.

Elements of a matrix are not all created equal, they are divided into two types:

The elements of a matrix $A$ which have the same row and column index, e.g. $A_{33}$ are called the *diagonal elements*. Those which do not lie on the diagonal are called the *off-diagonal* elements.

For instance, in the 3 by 3 matrix below, the elements $a, e, i$ are the diagonal elements:
$$
A = \left(\begin{array}{ccc}a & b & c \\d & e & f \\g & h & i\end{array}\right)
$$

Matrices can be added together if they have the same dimensions. Then matrix addition is defined simply as adding up corresponding elements, for instance the element in the second row and first column of matrix $A$ is added with the element in the second row and first column of matrix $B$ to give the element in the second row and first column of matrix $C$. Recall from the previous chapter that rows in matrices are counted from top to bottom, while the columns are counted left to right.

Matrices can also be multiplied, but this operation is trickier. For mathematical reasons, multiplication of matrices $A \times B$ does not mean multiplying corresponding elements. Instead, the definition seeks to capture the calculation of simultaneous equations, like the one in the previous section. Here is the definition of matrix multiplication, in words and in a formula [@strang_linear_2005]:

The *product of matrices $A$ and $B$* is defined to be a matrix $C$, whose element $c_{ij}$ is the **dot product of the i-th row of $A$ and the j-th column of $B$**:

$$
c_{ij} = a_{i1}b_{1j} + a_{i2}b_{2j} + ... + a_{iN}b_{Nj} = \sum_{k=1}^q a_{ik} b_{kj}
$$

This definition is possible only if the length of the rows of $A$ and the length of columns of $B$ are the same, since we cannot compute the dot product of two vectors of different lengths. Matrix multiplication is defined only if $A$ is $n$ by $q$ and $B$ is $q$ by $m$, for any integers $n$, $q$, and $m$ and the resulting matrix $C$ is a matrix with $n$ rows and $m$ columns. In other words, **the inner dimensions of matrices have to match** in order for matrix multiplication to be possible. This is illustrated in {numref}`fig-mat-mult`

```{figure} images/matrix_multiplication_tikz.png
---
name: fig-mat-mult
---
Multiplication of two matrices $A$ and $B$ results in a new matrix $C$
```

**Example.** Let us multiply two matrices to illustrate how it’s done. Here both matrices are 2 by 2, so their inner dimensions match and the resulting matrix is 2 by 2 as well:

$$
\left(\begin{array}{cc}1 & 3 \\ 6 & 1\end{array}\right) \times \left(\begin{array}{cc}4 & 1 \\5 & -1 \end{array}\right) = \left(\begin{array}{cc}1 \times 4 + 3 \times 5 & 1 \times 1 +3 \times (-1) \\ 6 \times 4+ 1 \times 5 & 6 \times 1+1 \times (-1) \end{array}\right) = \left(\begin{array}{cc}19 & -2 \\ 29 & 5 \end{array}\right)
$$

One important consequence of this definition is that **matrix multiplication is not commutative**. If you switch the order, e.g.
$B \times A$, the resulting multiplication requires dot products of the rows of $B$ by the columns of $A$, and except in very special circumstances, they are not the same. In fact, unless $m$ and $n$ are the same integer, the product of $B \times A$ may not be defined at all.

In the example above of the matrix representation of the Fibonacci model, we implicitly used the conventional rules for multiplying matrices and vectors. Each row of the matrix

$$
\left(\begin{array}{cc}1 & 1\\1 & 0\end{array}\right)
$$

contains the numbers that multiply the two elements of the vector

$$
\left(\begin{array}{c}x_t \\ x_{t-1} \end{array}\right)
$$ 

in order to generate the two equations $x_{t+1} = x_t + x_{t-1}$ and $x_t = x_t$.

Take the matrix equation for the Fibonacci difference equation above. Put the first two values $0$ and $1$ into the vector. Then perform the multiplication of the matrix and the vector:

$$
\left(\begin{array}{cc}1 & 1\\1 & 0\end{array}\right)\left(\begin{array}{c}1\\ 0\end{array}\right) = \left(\begin{array}{c}0+ 1 \\ 1 \end{array}\right)  = \left(\begin{array}{c}1 \\ 1 \end{array}\right)
$$

We can take the resulting vector and apply the matrix again, to propagate the sequence for one more step:

$$
\left(\begin{array}{cc}1 & 1\\1 & 0\end{array}\right)\left(\begin{array}{c}1\\ 1\end{array}\right) = \left(\begin{array}{c}1+ 1 \\ 1 \end{array}\right)  = \left(\begin{array}{c}2 \\ 1 \end{array}\right)
$$

Multiplying matrices and vectors is a basic operation that depends on the orientation of the vector. One can only multiply a square matrix by a column vector on the left, as we saw above, not on the right. By the same token, a row vector can only multiply a matrix on the right, and not the left, because we must use the *rows* of the matrix on the left to multiply the *columns* of the matrix on the right. This underscores the important fact that matrix multiplication is not commutative.

## Age-structured population models

It is often useful to divide a population into different groups by age in order to better describe the population dynamics. Typically, individuals at different life stages have distinct mortality and reproductive rates. The total population is represented as a vector, where each component denotes the size of the corresponding age group. The matrix $A$ that multiplies this vector defines the dynamics of the higher order difference equation: 

$$
\vec x_{t+1} = A \vec x_t
$$

We will now analyze two common *age-structured models* used by biologists and demographers.

### Leslie models

One type of age-structured model used to describe population dynamics is called the *Leslie model*
[@edelstein-keshet_mathematical_2005; @allman_mathematical_2003]. In this model, there are several different age groups, and after a single time step, individuals in each one all either advance to the next oldest age group or die. This type of can be described in general using the following matrix (called a Leslie matrix):

$$
L = \left(\begin{array}{cccc}f_1 & f_2 & ... & f_n \\s_1 & 0 & ... & 0 \\... & ... &...& ... \\0 & ... & s_{n-1}& 0\end{array}\right)
$$

where $f_i$ is the fecundity (number of offspring produced by an  individual) of the $i$-th age group, and $s_i$ is the survival rate of the $i$-th age group (the fraction of the group that survives and becomes the next age group). Population of the next generation is given by multiplying the age-structure vector of the previous generation: $\vec x_{t+1} = L \vec x_t $. Note that each age group proceeds straight to the next age group (multiplied by the survival rate) but no individuals stay in the same age group after one time step. Biologically, this assumes a clear, synchronized maturation of every age group in the population. Mathematically, this means that the *diagonal elements* of the matrix (those in the $i$-th row and $i$-th column) are 0.

Let us model a hypothetical population in which there are two age groups: a young age group which does not reproduce, with survival rate of 0.4 to become mature, and a mature age group which reproduces with mean fecundity of 2, and then dies. Let $j_t$ be the population of the juveniles at time $t$, and $m_t$ be the population of mature adults. Then the following Leslie matrix describes this model:

$$
\left(\begin{array}{c}j_{t+1}\\ m_{t+1}\end{array}\right) =  \left(\begin{array}{cc}0 & 2 \\0.4 & 0\end{array}\right) \left(\begin{array}{c}j_{t}\\ m_{t}\end{array}\right)
$$

We can also express this model as a single difference equation, with the variable of total population. Because it takes two time steps for a young individual to reproduce, we need to consider the population in two previous time steps. The matrix equation above can be written as the following two equations: 

$$
j_{t+1} = 2 m_t ; \; m_{t+1} = 0.4 j_t
$$

This two-dimensional model can be turned into a second-order model by a simple substitution. The first equation can be written as $j_t = 2 m_{t-1}$, and then substitute it into second one to, to obtain:

$$
m_{t+1} = 0.8m_{t-1}
$$

We can solve this equation using the tools from the analytical section. First, let us find the exponential bases
$\lambda$: 

$$
\lambda^2 = 0.8 \Rightarrow \lambda = \pm \sqrt{0.8}
$$

To solve the dynamical system completely, let us suppose we have the initial conditions $m_0$ and $m_1$. Then we have the following equations to solve:

$$
A + B = m_0; \; A\sqrt 0.8 - B \sqrt 0.8 = m_1\Rightarrow (m_0 - B) \sqrt 0.8 - B \sqrt 0.8 = m_1 \Rightarrow B =m_0 - \frac{m_1}{\sqrt 8}; \; A = \frac{m_1}{\sqrt 8}
$$

We have the following analytic solution of the difference equation:

$$
m_t = \frac{m_1}{\sqrt 8} \sqrt 8^t - \left(m_0 - \frac{m_1}{\sqrt 8} \right)  \sqrt 8^t = 2m_1 \sqrt 8^{t-1}  - m_0 \sqrt 8^{t}
$$

This solution can be used to predict the long-term dynamics of the population model. Since the bases of the exponentials are less than 1, the total number of individuals will decline to zero. This solution can be verified via a numerical solution of this model. {numref}`fig-leslie` shows the population over 20 time steps, starting with 10 individuals both for $m_0$ and $m_1$.

```{figure} images/leslie_dynamics.png
---
name: fig-leslie
---
A plot of the total population in the Leslie model shown above, showing an oscillatory decay to 0.
```


### Usher models

Usher models are a modification of the Leslie model, where individuals are allowed to remain in the same age group after one time step. Thus, the form of an Usher matrix is:

$$
U = \left(\begin{array}{cccc}f_1 & f_2 & ... & f_n \\s_1 & r_2 & ... & 0 \\... & ... &...& ... \\0 & ... & s_{n-1} & r_n\end{array}\right)
$$

where $r_i$ is the rate of remaining in the same age cohort.

For instance, it the population model above, we can introduce a rate of adults remaining adults (rather than dead) after a time step (let it be 0.2):

$$
U =  \left(\begin{array}{cc}0 & 2 \\0.4 & 0.2\end{array}\right)
$$

$$
j_{t+1} = 2 m_t ; \; m_{t+1} = 0.4 j_t +0.2m_t
$$

Once again, we can find the solution for this model by recasting it as a single second-order equation. Let us substitute $2m_{t-1}$ for $j_t$ to obtain the following: 

$$
m_{t+1} = 0.4(2 m_{t-1} )+ 0.2 m_t
$$

We can solve this second-order equation in the same fashion as above:

$$
\lambda^2 = 0.2 \lambda + 0.8 \Rightarrow \lambda = (0.2 \pm \sqrt {0.04+3.2})/2 = (0.2 \pm 1.8)/2 = 1, -0.8
$$

The two exponential bases are 1 and -0.8, and therefore the solution has the general form $m_t = A + B(-0.8)^t$. The behavior of the solution over the long term is going to stabilize at some level $A$, determined by the initial conditions, because the term $B(-0.8)^t$, when raised to progressively larger powers, will decay to 0.

We can run a computer simulation to test this prediction, and see that the total population indeed approaches a constant. Starting with population of 10 individuals in the first two time steps, the time course of the population is plotted in {numref}`fig-usher`.


```{figure} images/usher_dynamics.png
---
name: fig-usher
---
The total population of the Usher model shown above, showing oscillation and converging to a single value.
```
