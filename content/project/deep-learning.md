+++
# Date this page was created.
date = "2016-04-27"

# Project title.
title = "Arithmetic Hyperbolic Reflection Groups"

# Project summary to display on homepage.
summary = " "

# Optional image to display on homepage (relative to `static/img/` folder).
#image_preview = "bubbles.jpg"

# Tags: can be used for filtering projects.
# Example: `tags = ["machine-learning", "deep-learning"]`
tags = ["refl"]

# Optional external URL for project (replaces project detail page).
#external_link = ""

# Does the project detail page use math formatting?
math = true

# Optional featured image (relative to `static/img/` folder).
[header]
#image = "headers/bubbles-wide.jpg"
caption = "My caption :smile:"

#\newtheorem{theorem}{Theorem}

+++


## Basic definitions and facts

  - Suppose $K$ is a totally real number field with the ring of integers $A$. Suppose $f(x)$ is a quadratic forms of signature $(n,1)$ defined over $K$ such that for every non-identity embedding $\sigma \colon K \to \mathbb{R}$ the form $f^{\sigma}$ is positive definite. Such forms $f(x)$ are said to be admissible. 

  - Suppose $O'(f, A)$ is the group of integral automorphisms (i.e. the automorphisms  with coefficients from $A$) of the form $f(x)$, preserving the $n$-dimensional Lobachevsky (hyperbolic) space $\mathbb{H^n}$.
  
  - By the result of A. Borel and Harish-Chandra (see [BHC62]) or G. Mostow and Tamagawa (see [MT62]), the group $O'(f, A)$ is the cocompact discrete group of motions of the space $\mathbb{H}^n$ with an exception of the field $K = \mathbb{Q}$, when such group could be of cofinite volume, but not cocompact. The case $K = \mathbb{Q}$ was studied by Venkov in 1937 (see [Ven37]).


## Existence Theorems

1. Arithmetic hyperbolic reflection groups do not exist for dimensions $n \geq 30$.
2. Arithmetic
3. 

## Vinberg's Algorithm
- See here the brief description.
- R. Guglielmetti's implementation for hyperbolic lattices with an orthogonal basis (the program with the documentation is available here, and also some information you can find in [Gugl17])
- Sowtware implementation by Bogachev and Perepechko for arbitrary integral hyperbolic lattices (the program, some brief description). See also the paper [BP18].

## Classification results

1. $K = \mathbb{Q}$
  + V.V. Nikulin, 1981,1984. $2$-reflective hyperbolic lattices (for all $1 < n < 21$ and $n \ne 4$) 
  + E.Vinberg, 1972. Unimodular reflective hyperbolic lattices (reflective for all $n \le 19$)
  

  - $n=2$.

     + V. Nikulin, 2000 
     + D. Allcock, 2012

  - $n=3$.
     + E.B. Vinberg, 2007. $2$-reflective hyperbolic lattices of rank $4$
     + R. Scharlau, 1989. Reflective isotropic hyperbolic lattices
     + N.V. Bogachev, 2016-2017. $(1.2)$-reflective anisotropic hyperbolic lattices of rank $4$
     + Anisotropic case:  $\textbf{Open Problem}$
  - $n=4$.
  - $n=5$.
  - $n \ge 6$. $\quad \textbf{Open Problem}$
     
2. $K = \mathbb{Q}[\sqrt{2}]$
3. $K = \mathbb{Q}[\sqrt{5}]$
4. $K = \mathbb{Q}[\cos(2\pi/7)]$
5. Other Fields. $\textbf{Open Problem}$.


## References

[All12] D.Allcock

[[Bel16]](http://www.ams.org/journals/bull/2016-53-03/S0273-0979-2016-01530-8/S0273-0979-2016-01530-8.pdf)
M. Belolipetsky --- Arithmetic hyperbolic reflection groups

[[B17]](http://www.turpion.org/php/paper.phtml?journal_id=rm&paper_id=5044)
N.V. Bogachev --- Reflective anisotropic hyperbolic lattices of rank 4, 
Russian Mathematical Surveys, 2017, vol. 1 (433), p. 179 - 181.

[B18] N.V. Bogachev --- The classification of $(1.2)$-reflective anisotropic hyperbolic
lattices of rank $4$. Izv.Math., 2018.

[BP18] N.V. Bogachev, A.Ju. Perepechko --- Vinberg's Algorithm for Hyperbolic Lattices.

[Nik80]

[Nik81]

[Nik00]

[Nik07]

[Ven37] B.A. Venkov. 

[[Vin85]](http://iopscience.iop.org/article/10.1070/RM1985v040n01ABEH003527/meta)
E.B. Vinberg --- Hyperbolic reflection groups, Russian Mathematical Surveys, 1985, vol. 40, p. 31 - 75.

[[Vin93]](http://www.springer.com/us/book/9783540520009)  E.B. Vinberg(ed) --- Spaces of constant curvature,
Geom. II,  vol. 29, Encyclopaedia of Math. Sciences, Springer-Verlag, Berlin, 1993. 

[Vin07]

[Vin14]

