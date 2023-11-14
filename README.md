## muscle3playground

This is a companion to MUSCLE3's [tutorial](https://muscle3.readthedocs.io/en/latest/index.html) and [training materials](https://esciencecenter-digital-skills.github.io/lesson-model-coupling/01-introduction.html). `reaction_diffusion.py`, and all the files it depends on, have been taken from them.

### Lotka-Volterra competition model

The `predator_prey.py` and the files it depends on implement a Lotka-Volterra competition model, also known as predator-prey equation. Namely:

$$
\begin{equation}
\begin{cases}
\dot x = ax - bxy \\
\dot y = cxy - dy
\end{cases}
\end{equation}
$$

where $x$ and $y$ represent, respectively, the prey and predator populations.

We use MUSCLE3 to split the coupled model into two submodels, where the other variable is treated as a parameter. The purpose of solving this system in such a strange way is purely pedagogical.
