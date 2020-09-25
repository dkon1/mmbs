# Discrete models of higher order


It is not unusual for biological systems to have multiple variables which influence each other, and thus need to be accounted in any model that aims to be useful. In this unit we will learn how to construct such models, and the methods for analyzing, solving, and numerically simulating them. We will see how models with two or more variables are used in a variety of biological fields: to describe population demographics, motility of cochlear cells, psychology of human relationships, gene regulation, and motion of molecular structures.

We will need new mathematical tools in order to analyze models with multiple variables. These methods are primarily from the realm of linear algebra. We will express multiple equations in terms of matrices and vectors, and learn how to operate on these objects. The dynamics of these models can be analyzed by doing calculations with the matrices, specifically finding special numbers and vectors known as eigenvalues and eigenvectors. These concepts, which will be introduced later, are absolutely central to all of applied mathematics, and to computational biology in particular.

In this chapter, the section on modeling is devoted to an old model of a population where individuals live for two generations, known as the Fibonacci model. We then describe how this model can be written down either as a single difference equation of second order, or as two equation of the first order, which may be represented in matrix form. In the analytical section, we will learn to solve second order difference equations with an explicit formula, and then introduce some elementary matrix operations. In the computational section we will use the matrix notation to compute numerical solutions for higher order difference equations. Finally, in the synthesis section we will analyze two demographic population models, in which the population is broken into age groups. The matrix notation will be important for concisely representing different parameters for each age group. 

In this chapter you will learn to:

* build higher order population models
* express age-structured models in matrix form
* analyze solutions of these models on paper
* use Python for matrix operations
* classify the behavior of solutions of these models