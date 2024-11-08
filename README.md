
2.  **\
    Evolving Fractal** (2 People): In order to draw the Sierpinski
    triangle, and some variations thereof, we are going to control a
    plotter through rotations and translations. This process needs to be
    self-similar, therefore we are going to use recursive functions to
    repeat the procedure over and over.

    a.  Consider the cartesian axes as the reference ones in 2D. The
        basic op- erations are 3:

        i.  Draw a point at distance *l* from the origin *O* along the
            *x* axis (rotation angle 0)

        ii. Rotate by *α* = *π/*3 counter clockwise with respect to *x*
            and draw another point again at distance *l*

        iii. Rotate by *α* = *π/*3 clockwise with respect to *x* and
             draw another point again at distance *l*

 Starting with *O* = (0*,* 0) and *l* = 1, this draws the first
 vertices of a triangle. To be fractal, every time you draw a point,

i.  Set a new origin *O*^′^ at distance *l/*2 along the drawing
    direction.

This direction is going to be your new horizontal axis *x*^′^

ii. Now redo the 3 basic operations above using *l*^′^ = *l/*2

 You can do this calling the same function recursively passing as argu-
 ments the *l* to use, the position of the origin *O* and an initial
 rotation angle with respect to an absolute reference system.

 Remember to track the *recursion depth* and stop at some maximum value
 (7 recursions should be enough for a nice picture). Use a small dot
 ('.' for example) to have a less cluttered picture.

a.  Now repeat the same procedure, but change the value of the angle *α*

 for the side vertices.

 Try a series of 4 configurations with *α* equally spaced between *π/*3
 and

 *π/*2, inclusive.

 What do you obtain?

b.  You can repeat all the above *α* configurations, but this time set
    the new origin *O*^′^ at a distance *l*(*β −* 1)*/β* and use a new
    distance *l*^′^ = *l/β*. You can try *β* = 2*.*5*,* 3*.*5.

What do you obtain?

c.  Bonus: if instead of using the same *α* clock- and counterclock-wise
    you try different angles *α*~1~ and *α*~2~ of your choice, what do
    you see?

