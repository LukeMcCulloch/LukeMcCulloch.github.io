# LukeMcCulloch.github.io
pages static site

In support of the PhD I completed at the University of New Orleans.
The code is [here.](https://github.com/LukeMcCulloch/feasible-form-parameter-design)

copyright 2019 Thomas Luke McCulloch

All Rights Reserved

(until I can figure out what to do with this code.)

The dissertation describing what I've done is [here.](https://scholarworks.uno.edu/td/2552/)

A paper my advisor and I wrote detailing some of the first
things I came up and built with for the project [here.](https://www.sciencedirect.com/science/article/abs/pii/S0167839617301474?via%3Dihub)

I hope to post a pre-print for this somewhere soon.

There is a new paper to be given at a constraint programming conference,
briefly summarizing the details of the constraint programming system.  This paper will be part of the 12th International Workshop
on Constraint Programming and Decision Making [here](https://interval.louisiana.edu/IFSA-NAFIPS/CoProD2019.html)
and [here.](http://coprod.constraintsolving.com/)

As for this web page, well, a blog belongs here.  Unfortunately I am in the process of
fixing up many long neglected projects.  This one is not yet
first in line!

These days I am chiefly working on two or three things:  algorithms inspired by geometric physics, understanding geometric physics, and high performance computing.  The ongoing projects related to this research are here:
* [differential geometry, topology, and exterior calculus for mesh processing and geometric design](https://github.com/LukeMcCulloch/Python-discrete-differential-geometry)
* [c++ expression templates and gpu programming for PDE modeling](https://github.com/LukeMcCulloch/cpp-cuda-flow-solver-1)

There are several points to this research --- much of which is self-educational, as required by my cross disciplinary mind-set.  

First, there are cross disciplinary reasons to get into discrete differential geometry 
research.  The algorithms are inspired by the more beautiful and topological side of physics and the idea is to re-purpose 
the research that is out there now to do more expressive, more powerful, 
and more efficient constrained variational design of, e.g. ship hulls and other complicated shapes.  In this way it is an outgrowth of my PhD research.  Or at any rate, 
the eventual goal is to tie the two things together.

With the C++ expression templates and CUDA programming project, I have several goals:
* Understand and implement the basic (general) ideas behind world class high performance C++ linear algebra libraries.  (not the specific cache aware, high detail stuff a la Kazushige. Goto.  This is educational.  I can use a library as well as the next guy)
* Combine sophisticated, efficient, C++ numerics with GPU programming techniques.  This is where I think the educational stuff may pay off.  I'd like to program the GPU not only for maximum performance, but to maximize the expressiveness of my code.
* Build these into a lightweight CFD package, eventually incorporating approximate 
Riemann solvers and other high resolution shock capture techniques for hyperbolic conservation laws.

So far, I have successfully implemented the basic techniques for expression templates, including a few element wise operations on matrices (heap arrays) and, for educational purposes, extended this to matrix multiplication.  Immediately on getting it right for matmul, I took it out of the code base and replaced it with matrix caching.  Now the chief things it lacks are smart caching based on the operand types across the entire computational tree, and smart algorithm picking based on available hardware, available software libraries, and the like.  (The literature, or the docs for a good well documented code-base like Blaze, Eigen, MTL4, or ETL) should clarify some of what I am saying here.  Sometimes, still, the best simple thing to do is to call out to Fortran, what can I say?

Alright, now I want to tie this, too, back to my PhD research.  In developing the 
logical, relational rules processing engine for my automated ship hull design 
geometry optimizing code-base, I needed something that would automatically turn 
simple Python/NumPy math into relational rules.  I didn't realize it at the time, 
but what I implemented for parsing the mathematical expressions into a binary 
syntax tree, and in processing that tree into a relational, connected, rules base, 
I was following a pattern that repeats itself again and again throughout 
computer science --- the interpreter pattern.  

From Norvig to SICP, and from C++ expression templates to a n-ary logical rules, and finally in Tensor Flow, Theano, and no doubt in other machine learning libraries, 
the interpreter pattern keeps showing up.  

Here is how this pattern appears in my work:
* In my PhD I have a class which overloads math to store up an expression tree.
* I then parse said expression tree and construct simple logical rules that 
implement the same procedural mathematics in relational style.
* Here I deliberately created explicitly temporaries that I could process easily into 
another computational form.


On the other hand, for expression template programming in C++, 
the interpreter pattern shows up in the following way:
* One implements classes which overload mathematical expression so as to store 
up the computation tree instead of performing the computations eagerly.
* Then, when all computations in an expression are known, the program can 
make the best decision about the order in which to compute them, 
and can avoid expensive creation of temporary objects to hold 
temporary results.
* Since all this is done in templates, all this fancy footwork happens at compile time, which is usually a good place to offload extra work, though not always, but I digress.  (I maintain old, huge code-bases for a living right now.  They compile slowly.)
* In the end, many operations can be combined into more efficient loops by the compiler.  These would have been ugly to maintain if written explicitly.  (This aestheticism is the chief purpose of the exercise.)