Title: Introduction to the Form Parameter Ship Hull Design and Optimization Problem
Date: 2017-02-12 21:07
Category: Naval Architecture
Tags: Parametric Design, Optimization, automation, python
Authors: Luke McCulloch



[Over here]({filename}/introduce_the_context.md), we introduced the ship hull design and optimization automation problem as a specific instance of the broader push to automate many tasks using machine intelligence, optimization, and similar techniques.  This time, I'd like to outline the problem specifically in the context of naval architecture.

#### So What's the problem?  And why would you care?
	Current CAD/CAE systems have developed to the point where they not only
	serve as replacement for the drawing board but also provide complete 
	product documentation for the whole life cycle of the system.
	The next logical step in the development of CAD and CAE methods is
	their comprehensive integration with engineering analysis and exploiting
	analysis results in product optimization and design space exploration.
	One of the most promising geometric design methods for computer aided
	design of complex hydrodynamic or aerodynamic hull like ships, cars, and
	aircraft is so called "form parameter design".  
	In this technique, complex shapes are computed to user specifications
	rather than approximating specifications by manual adjustments to the
	design. 

    So, the problem is an important one for the direction of engineering ship deign.  The problem is not an easy one.  Current implementations suffer from a number of drawbacks.
    *  It's easy to specify inconsistent constraints
    *  This makes the systems hard for users to use
    *  This is the perfect opportunity for a smart assistant.


#### How could solutions to this problem effect the idustry?
    *  Ship hull design is a bottleneck in the ship design process.  In the design spiral, the portion of the design that is most timeconsuming, per iteration, is often the hull design, simply because of the interplay of a large number of constraints.  Automating the design of a ship hull greatly reduced the burden on the engineer in producing any ship design.
    *  Automation opens the door for hands free optimization.  Free of the exense of manual design manipulation by engineers, relatively cheap computations can be spent simply making better designs. Optimization could thus improve
        *  decreasing production costs via optimizing the amount and placement of curved plate required.
        *  increasing fuel efficiency
        *  better seakeeping qualities for reduced downtime and increased safety of operation.
        *  better stability and damage stability qualities

    Automation and optimzation techniques are especially noteworthy in ship design because of the one-of-a-kind nature of ship designs.
    In the past, optimization was only economical when production runs achieved economies of scale, since the great numbers of a product that would be produced made the most of any advantage which could be confered, even at large up front costs, as such high up front design costs could be spread out over the large volume produced.
    In contrast, the one-off designs of the ship building industry necessitate a very efficient design process indeed, if there is to be any room left over for the optimization of a design that will see life only in one single instance.  Because of such cost considerations, only the efficiencies enabled by automation allow designers to finally tap the full potential of the computer for optimzition.  


#### What drawbacks have prevented the uptake of automation/optimization solutions to date?

    A primary difficulty that all automated ship hull design tools have to overcome is interplay of large numbers of constraints acting across hierarchical levels of a design.  
   *  A design is more easily specified via a design hierarchy.
   *  Unfortunately, some constraints refuse to act only on their local level of that hierarchy.
