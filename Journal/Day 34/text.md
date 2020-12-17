# Day 34

Made an animated bouncing liquid ball. I was doing the FCC applied visual design section and they were teaching about `animation-timing-function` using bouncing balls as examples and that made me want to make my own bouncing ball, but better.

The circle-shaped figure receives some shading, done with radial-gradient() functions. The first layer adds a radial gradient circle at the center with the color stops:

```css
radial-gradient(
    circle at center,
    transparent 0% 90%,
    black 100%
)
```

This adds a slight transition to black at the edges of the circle to mimic a shadow effect.

Then, the second radial-gradient() layer adds the base color of the circle and transitions into a shade towards the extremities, again, with the same purpose of replicating a shadow effect. The colors are custom properties defined in the :root pseudo-class. The color stops are:

```css
radial-gradient(
    circle at center,
    var(--color1) 0%,
    var(--color2) 100%,
)
```

The shading and color are done. Now the movement.

The ball moves from point A (top) to point B (bottom) to point A. To replicate the physics of a falling bouncy ball, the animation-timing-function is set to ease-in-out. This makes the animation start slow (when the ball starts falling), speeds up towards the middle keyframes (which covers the moment the ball hits point B) and then slows down again towards the end (when the ball is moving back up, against gravity, when it should deccelerate).

The ball's dimensions are modified when the ball hits point B, so that it actually looks "bouncy". When it hits point B, the width:height ratio changes, so the width:height changes from 20vmin/20vmin to 30vmin/14vmin.

After it starts moving back to point A, the width:height inverts, so the height becomes greater than the width.

Then, the ball's dimensions transition back to their original values, while moving back towards point A.

I also made a statically positioned shadow, almost fully transparent, with an opacity factor of 0.10, that mimics the ball's dimensions' modifications.
