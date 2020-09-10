
# Introduction


In this book you will find a collection of mathematical ideas, computational methods, and modeling tools for describing biological systems quantitatively. Biological science, like all natural sciences, is driven by experimental results. As with other sciences, there comes a point when accumulated data needs to be analyzed quantitatively, in order to formulate and test explanatory hypotheses. Biology has reached this stage, thanks to an explosion of data from molecular biology techniques, such as large-scale DNA sequencing, protein structure determination, data on gene regulatory networks, and signaling pathways. Quantitative skills have become necessary for anyone hoping to make sense of biological research.

Mathematical modeling necessarily involves making simplifying assumptions. Reality is generally too complex to be captured in a few equations, and this is especially true for living systems. Simplicity in modeling has at least two virtues: first, simple models can be grasped by our limited minds, and second, it allows for meaningful testing of the assumptions against the evidence. A complex model that fits the data may not provide any insights about how the system works, whereas a simple model which does not fit all the data can indicate where the assumptions break down. We will learn how to construct progressively more sophisticated models, beginning with the ridiculously simple.


```{figure} images/physicists_xkcd.png
---
name: fig-xkcd-phys
---
Beware: a little knowledge of mathematical modeling can lead to
arrogance. <http://xkcd.com/793/>
```

## modeling assumptions: theoretical and empirical

A mathematical model postulates a precise relationship between several quantities, attempting to mimic the behavior of a real system. All models rest on a set of assumptions, postulating how various quantities are interrelated. These assumptions generally come from two sources: a scientific theory, or experimental observations. For instance, a model of molecular motion may rest on the assumption that Newton’s laws hold true. On the other hand, the observation that a drug injected into the bloodstream of a mammal is metabolized with an exponential time dependence is empirical. The benefit of models based on well-established theories, sometimes known as “first-principles models”, is that they can be constructed without prior experimental knowledge of a particular system. Newton’s laws apply to all sorts of classical mechanics objects, ranging in size from molecules to planets. Some prefer first-principles models, because they rely on well-established scientific principles, while others will argue that an empirical model more accurately reflects the behavior of the system at hand. From a mathematical standpoint, there is no difference between the two types of models. We will use the
same tools to construct and analyze models, regardless of their origin.

A stated assumption can be written as a mathematical relationship,
usually in the form of an equation relating quantities of interest. A postulated assumption may be expressed in words as “$X$ is proportional to $Y$”, and can be written as the following equation: $X = aY$. Another model may postulate a relationship “$X$ is inversely proportional to the product of $Y$ and $Z$”, which is expressed as  $X = a/YZ$.

Suppose we want to model the relationship between the height of
individuals ($H$) and their weight ($W$). Measuring those quantities in some population results in the observation that the weight is proportional to the height, with an additive correction. Then we can write the following mathematical model, based on the empirical evidence: $W = a H + c$

In electricity, Ohm’s law governs the relationship between the flow of charged particles, called current ($I$), the electric potential ($V$) and the resistance of a conductor ($R$). This law states that the current through a conductor is proportional to the potential and inversely proportional to the resistance, and thus can be mathematically formulated: 
$$
I = \frac{V}{R}
$$

## variables and parameters

Mathematical models formulate relationships between different quantities that can be measured in real systems. There are two different types of quantities in models: *variables* and *parameters*. The same measurable quantity can be a variable or a parameter, depending on the role it plays in the model. A variable typically varies, either in time or in space, and the model tracks the changes in its value. On the other hand, a parameter typically usually stays the same for a particular manifestation of the model, e.g. an individual or a specific population. However, parameters can vary from individual to individual, or from
population to population.

In the height and weight model above, the numbers $H$ are $W$ are the variables, which can change between different individuals. The
parameters $a$ and $c$ can either be estimated from data for various subpopulations. Perhaps the values of the parameters are different for young people than for older people, or they are different for those who exercise regularly versus those who do not. Once the parameters have been set, one can predict $W$ given $H$, or vice versa. Of course, since this is a model, it is only an approximation of reality. The deviations of predictions of the model from actual height or weight for an individual may tell us something interesting about the physiology of the individual.

There are three quantities in the equation for Ohm’s law, and the
distinction between variables and parameters depends on the actual
system that is being modeled. In order to distinguish between the two, consider which quantity is set prior to the experiment, and which one may vary over the course of the situation we are trying to model. For instance, if voltage is being applied to a material with constant resistance, and the potential may be varied, then $V$ is the independent variable, $I$ is the dependent variable, and $R$ is a parameter. On the other hand, if the setup uses a variable resistor (known as a potentiometer or pot), and the voltage remains constant, then $V$ is a parameter, while $I$ and $R$ are variables. If both the voltage $V$ and the resistance $R$ can vary at the same time, then all three quantities are variables.

## units and dimensions

Each variable and parameter has its own *dimension*, which describes the physical or biological meaning of the quantity. Examples are time, length, number of individuals, or concentration per time. It is important to distinguish the dimension of a quantity from the *units* of measurement. The same quantity can be measured in different units: length can be in meters or feet, population size can be expressed in individuals or millions of individuals. The value of a quantity depends on the units of measurement, but its essential dimensionality does not.

There is a fundamental requirement of mathematical modeling: all the terms in an equation must agree in dimensionality; e.g. time cannot be added to number of sheep, since this sum has no biological meaning. In order to express this rule, we will write the dimension of a quantity $X$ as $[X]$. While $X$ refers to a numerical value, $[X]$ describes its physical meaning. Then the above statement can be illustrated by the following example: 
$$
aX = bY^2 \; => \; [aX] = [bY^2]
$$

In the equation $W = a H + c $ all the terms must have the dimension of weight, because that is the meaning of the left hand side of the equation. Therefore, $c$ has the dimensions of weight as well. $H$ of course has the dimension of length, so this implies that the parameter $a$ has dimensions of weight divided by length. This can be summed up as follows:

$$
[W] = [c] = weight ; \; [H] = length ; \; [a] = \frac{weight }{length}
$$

While the dimensions are set by the equation, the units of these
quantities can vary. Weight can be expressed in pounds, kilograms, or stones, and length can be represented in inches, meters, or light years.

The dimensions of current are defined to be the amount of charge moving per unit of time, and the dimensions of voltage are energy per unit of charge. This allows us to find the dimensions of resistance by the following basic algebra:

$$
[V] = \frac{energy}{charge} = \frac{[I]}{[R]} = \frac{charge/time}{[R]} \; => \; [R] = \frac{charge^2}{energy *time}
$$

Electric potential is measured in volts, and current in amperes. The standard unit of resistance is the Ohm, which is defined as one volt per ampere. But regardless of the choice of units, the dimensions of these quantities remains.

A quantity may be made *dimensionless* by expressing it in terms of particular *scale*. For instance, we can express the height of a person as a fraction of the mean height of the population. A tall person will have height expressed as a number greater than 1, and a short one will have height less than 1. Note that this dimensionless height has no units - they have been divided out by scaling the height by the mean height. In fact, the word dimensionless is somewhat misleading: while such quantities have no scale in the context of the algebraic relationship, a quantity retains its physical significance after rescaling: height expressed as a fraction of some chosen length still represents height. Nevertheless, the accepted term in dimensionless quantity, and we will stick with this convention. Later in the book we will learn how to use the technique of rescaling to simplify and analyze
dynamic models.