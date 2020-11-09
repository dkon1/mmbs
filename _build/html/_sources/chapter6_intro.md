# Classification of 2-variables linear ODEs


In chapter 3 we introduced and analyzed discrete-time models with multiple variables representing different demographic groups. In those models, the populations at the next time step depend on the population at the current time step in a linear fashion. More generally, any model with only linear dependencies can be represented in matrix form. In this chapter we will learn how to analyze the behavior of these models, and identify all possible classes of linear dynamical systems.

The main concept of this chapter are the special numbers and vectors associated with a matrix, called eigenvalues and eigenvectors. Any matrix can be thought of as an operator acting on vectors, and transforming them in certain ways. Loosely speaking, this transformation can be expressed in terms of special directions (eigenvectors) and special numbers that describe what happens along those special directions. Finding the eigenvalues and eigenvectors of a matrix allows us to understand the dynamics of biological models by classifying them into distinct categories.

In the modeling section, we will develop some intuition for modeling activators and inhibitors of biochemical reactions. We will then learn how to draw the flow of two-dimensional dynamical systems in the plane. In the analytical section, we will define eigenvectors and eigenvalues, and use this knowledge to find the general solution of linear multi-variable systems. In the computational section, numerical solutions of eigenvalues and eigenvectors will be applied to classifying all linear multi-dimensional systems, and to plotting the solutions, both over time and in the plane. Finally, in the synthesis section we will use a light-hearted model of relationship dynamics to illustrate how to analyze linear dynamical systems.