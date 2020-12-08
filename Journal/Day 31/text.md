# Day 31

I made another loading animation -- a star-clock.

One circle and 3 thin rounded rectangles. I placed the circle in the middle and the middle point of two of the three rectangles in the middle of the circle. The other rectangle had its bottom placed in the middle of the rectangle so that it wouldn't traverse the circle like the other two rectangles did.

I rotated two of the rectangles (52deg and the other -52deg). Added 4 layers of box-shadow to create a smooth light effect. Then created an animation that varies the intensity of the box-shadow values (for a glowing effect) and further rotated the same two rectangles (360deg for one and -720deg for the other) so that it looks like a moving clock pointer.

Also added a rotating wrap around the group of elements that make up the star to add a little rotation near the end of the animation.

I don't know if the names are correct; English isn't my native language.

I also added a basic linear-gradient from purple to green angled at 25 degrees to the background, because why not? It looks cool.
