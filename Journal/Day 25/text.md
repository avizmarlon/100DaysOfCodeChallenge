# Day 25

Continuing the animated star system.

I added some layers of box-shadow to the star to give some lights effects. I also animated the "light" blur and spread radius to make it look like it's "alive".

Before moving on, I want to make sure I will be able to make the planets rotate counter-clockwise and elliptically around the star, while also adjusting the z-index on the fly to make the planet look like it's behind the sun when it's supposed to. I want to make it look really 3D.

---

I'm having trouble figuring out how to make the planet move along the elliptic orbit lines.

My current solution is to create a circle representing a planet as the child element of the element representing the orbit and lock the planet element to its parent, setting the transform-origin to the center of the circular orbit line, then rotate the planet 360deg along the orbit line. Then I "convert" the circular shape of the orbit line into an ellipse by using `transform: skew()` and `transform: rotate()`.

The problem is that the planet is also affected by the transforms and so it looks really weird.
