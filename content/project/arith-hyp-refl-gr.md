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


## Existence and Finiteness Theorems

1. (Nikulin, 2007) There are only finitely many of arithmetic maximal hyperbolic reflection groups. See [Nik07].
2. (Vinberg, 1984) In Lobachevsky spaces $\mathbb{H}^n$ of dimension $n \ge 30$ there are no arithmetic hyperbolic reflection groups. See [Vin84].
3. (Vinberg, 1984) In Lobachevsky spaces $\mathbb{H}^n$ of dimension $n \ge 22$  there are no arithmetic hyperbolic reflection groups with a ground field other than $\Q(\sqrt{2})$, $\Q(\sqrt{5})$ and $\Q(\cos(2\pi/7))$. See [Vin84].
4. (Vinberg, 1984) In Lobachevsky spaces $\mathbb{H}^n$ of dimension $n \ge 14$  there are no arithmetic hyperbolic reflection groups with a ground field other than $\mathbb{Q}(\sqrt{2})$, $\mathbb{Q}(\sqrt{3})$, $\mathbb{Q}(\sqrt{5})$, $\mathbb{Q}(\sqrt{6})$, $\mathbb{Q}(\sqrt{2}, \sqrt{3})$, $\mathbb{Q}(\sqrt{2}, \sqrt{5})$ and $\mathbb{Q}(\cos(2\pi/m))$, where $m=7,9,11,15,16,$ or $20$. See [Vin84].
5. (Nikulin, 2011) In the Lobachevsky spaces $\mathbb{H}^n$ of dimension $4 \leq n \leq 13$ the degree $d = [\mathbb{F} : \mathbb{Q}]$ is at most $25$. See [Nik11].
6. (Belolipetsky, 2011) In the Lobachevsky space $\mathbb{H}^3$ the degree $d$ is at most $9$. See [Bel11].
7. (Linowitz, 2017) In the Lobachevsky plane $\mathbb{H}^2$ the degree $d$ is at most $7$. See [Lin17].


## Vinberg's Algorithm
- See here the [brief](VA-Descr.pdf) description.
- R. Guglielmetti's implementation for hyperbolic lattices (over a series of ground fields) with an orthogonal basis (the program with the documentation is available here, and also some information you can find in [Gugl17])
- Sowtware implementation by Bogachev and Perepechko for arbitrary integral hyperbolic lattices (the [program](https://github.com/aperep/vinberg-algorithm), some [brief description](VA-Implementation)). See also the paper [BP18].

## Classification results

1. $K = \mathbb{Q}$
  + V.V. Nikulin, 1981,1984. $2$-reflective hyperbolic lattices (for all $1 < n < 21$ and $n \ne 4$). 
  + E.Vinberg, 1972. Unimodular reflective hyperbolic lattices (reflective for all $n \le 19$).
  

  - $n=2$.

     + V. Nikulin, 2000. Classification of reflective lattices of rank $3$ with square free discriminants. See [Nik00]
     + D. Allcock, 2012. Full classification of Reflective Lorentzian Lattices of Rank $3$. See [All12]

  - $n=3$.
     + E.B. Vinberg, 2007. $2$-reflective hyperbolic lattices of rank $4$
     + R. Scharlau, 1989. Reflective isotropic hyperbolic lattices. See [Sch89]
     + N.V. Bogachev, 2016-2017. $(1.2)$-reflective anisotropic hyperbolic lattices of rank $4$. See [B17] and [B18].
     + Anisotropic case:  $\textbf{Open Problem}$
  - $n=4$. C. Walhorn. See [SW92] and [Wal93].
  - $n=5$.I. Turkalj. Classification of Relective Lorentzian Lattices of Signature $(5,1)$.
  - $n \ge 6$. $\quad \textbf{Open Problem}$
     
2. $K = \mathbb{Q}[\sqrt{2}]$.

  - $n=2$. A. Mark. Classification of Reflective Hyperbolic Lattices of rank $3$.
  - $n \ge 3$. $\quad \textbf{Open Problem}$

3. $K = \mathbb{Q}[\sqrt{5}]$
4. $K = \mathbb{Q}[\cos(2\pi/7)]$
5. Other Fields. $\textbf{Open Problem}$.


## Open Problems

1. Classification of reflective hyperbolic lattices with ground fields other than Q.

2. Find the list of all possible ground fields of arithmetic hyperbolic reflection groups.

3. Improve the upper bounds for degrees of ground fields of arithmetic hyperbolic reflection groups.

4. Classification of reflective anisotropic hyperbolic lattices over Q of rank 4. 

5. Classification of reflective anisotropic hyperbolic lattices over Q of ranks more than 6. 

6. Efficient software implementation of Vinberg's Algorithm.


## References

[Agol06] Ian Agol, 

[All12] D.~Allcock, The Reflective Lorentzian Lattices of Rank $3$, in Mem.Amer.Math.Soc.
(Amer.Math.Soc., Providence, RI, 2012), Vol. 220, No. 1033.

[Bel11]

[[Bel16]](http://www.ams.org/journals/bull/2016-53-03/S0273-0979-2016-01530-8/S0273-0979-2016-01530-8.pdf)
M. Belolipetsky --- Arithmetic hyperbolic reflection groups

[[B17]](http://www.turpion.org/php/paper.phtml?journal_id=rm&paper_id=5044)
N.V. Bogachev --- Reflective anisotropic hyperbolic lattices of rank 4, 
Russian Mathematical Surveys, 2017, vol. 1 (433), p. 179 - 181.

[B18] N.V. Bogachev --- The classification of $(1.2)$-reflective anisotropic hyperbolic
lattices of rank $4$. Izv.Math., 2018.

[BP18] N.V. Bogachev, A.Ju. Perepechko --- Vinberg's Algorithm for Hyperbolic Lattices.

[LMR06]

[Lin17] Linowitz

[Nik79]

[Nik80]

[Nik81]

[Nik00]

[Nik07]

[Nik08]

[Nik09]

[Nik11]

[Sch89]

[SW92]

[Wal93]

[Ven37] B.A. Venkov. 

[[Vin85]](http://iopscience.iop.org/article/10.1070/RM1985v040n01ABEH003527/meta)
E.B. Vinberg --- Hyperbolic reflection groups, Russian Mathematical Surveys, 1985, vol. 40, p. 31 - 75.

[[Vin93]](http://www.springer.com/us/book/9783540520009)  E.B. Vinberg(ed) --- Spaces of constant curvature,
Geom. II,  vol. 29, Encyclopaedia of Math. Sciences, Springer-Verlag, Berlin, 1993. 

[Vin07]

[Vin14]

