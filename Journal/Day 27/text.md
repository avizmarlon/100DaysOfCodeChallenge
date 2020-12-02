# Day 27

I finally figured out how to do an elliptical movement in my very specific scenario.

So, first I created a circle using a div with `border-radius: 50%;`. This is the orbit line. Then I made another circle, this one with a `background-color` -- this is the planet.

I had to make sure the planet would rotate along the orbit line, no matter what I did to the orbit line (change dimensions, position, transform etc.). Basically, I had to lock the planet to the orbit line.

Now, WHY did I have to do it this way? Because, obviously, I wanted an ellipse instead of a circle to represent the orbit lines. At first I thought: "Well, I can just make a circle and increase the width, and it will turn into an ellipse." I did that, but I quickly realized this was a mistake. Here's why:

After making the ellipse by simply increasing the width of a circle, I went on and tried to make the planet move along the orbit line. The only way I thought of doing this reliably was using the translate function of the transform property. But, think about it, I would have to hardcode every single frame of the movement for the whole animation duration, until it completed a 360 degrees rotation around the center. That is MADNESS. **Time is a valuable resource, one of the only resources we can't increase or get back what was already spent, so I must be efficient.**

So I had the idea of first making sure the planet would move perfectly along the whole orbit line. This was easy. I only had to use relative units to position the planet at a 12 o'clock position. The rotation would be made with `transform: rotate(1turn)` (remember the unit turn is equivalent to a full rotation of 360 degrees; 0.5turn = 180deg etc.).

Now the planet is rotating around itself, which is not what I want -- I want it to rotate around the star. So I played with the transform-origin values until the transform-origin was set at the center of the orbit line (kinda where the star is). Transform-origin basically tells the rotate() function what is the point of reference to be used for the rotation, which in my case is the center of the orbit line where the star is.

The planet is now moving perfectly along the orbit line. Great, but what about the circular orbit line? It's supposed to be elliptical. Well, I had another eureka moment here. I was thinking about 3D space and had the idea of transforming a circle into an ellipse by rotating the circle 75 degrees clockwise around a horizontal (X) axis. There you go, an ellipse is "made" and the planet is still moving perfectly, because it's a child element of the orbit line element and it's locked to it, so the properties of the orbit line element are inherited by the planet element. However, this creates a problem.

Since, the planet also got rotated together with the orbit line, the planet ALSO became an ellipse, and this is madness. It should be perfectly circular (equal diameter), maybe just a BIT elliptical.

Believe it or not, it took me quite a while to figure out a solution to this, but, in the end, all I had to do was increase the height of the planet to achieve a 1:3 ratio between width and height. This would create the illusion that the planet is a circle, but, obviously, if you remove the horizontal rotation, you would see an ellipse.

That's the point though, right? You rotate a circle in the X axis and it becomes an ellipse; you rotate an ellipse in the X axis it becomes a circle (would have to rotate just enough until the width becomes the same as the height).

That's it? Nope. The planet was rotation was somewhat weird. The planet would rotate around the center of the ellipse, but the planet itself should not rotate around itself. Well, actually, the bottom of the planet was fixated on the center and as it rotated along the orbit line, that bottom part of the planet would always be pointing towards the center and since the planet is actually an ellipse rotated 75deg in the X axis, the elliptical shape would become very evident in some parts of the rotation.

To fix this, I had to make a wrapper div for the planet to make the planet rotate around itself in the opposite direction (counter-clockwise or -360deg; -1turn). I couldn't make this transform in the planet element itself, because of the transform-origin, which was set at the center of the orbit line, and this time I needed a reference point on the center of the planet itself, so that's why I needed a wrapper div.

Honestly, maybe it's just me, but it seems overly complicated and there are probably a gazillions ways of doing this whole thing better. I didn't even lear JavaScript yet, I'm barely scracthing the surface at applied visual design with css. I made this with a very limited amount of knowledge. Maybe in the future, when I acquire more knowledge I will make a better one. It's just that I had the idea of making an animated star system and I COULD'NT let go of it. I had to scratch that itch.
