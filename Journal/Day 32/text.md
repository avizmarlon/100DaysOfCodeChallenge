# Day 32

## Eclipse Animation

### Basic Structure

I used divs to represent 3 things: the sky, the sun and the moon.

The sky covers the whole viewport and has a color that resembles the sky viewed from Earth (#2f72d0).

The sun is a white circle (`border-radius: 50%`) placed right in the middle of the page with top and left set to 50% and the translate() function set to (-50%, -50%). The dimensions are 41x41vmin.

The light is made with box-shadow using a multiple-layering technique and exponentially increasing values for the `blur` and `spread` parameters, as follows:

```css
    .sun {
        box-shadow:
            0vmin 0vmin 1.5vmin 1.5vmin hsla(46, 100%, 98%, 1.0),
            0vmin 0vmin 3.0vmin 3.0vmin hsla(0, 0%, 100%, 0.85),
            0vmin 0vmin 6.0vmin 6.0vmin hsla(0, 0%, 100%, 0.75),
            0vmin 0vmin 12.0vmin 12.0vmin hsla(0, 0%, 100%, 0.65),
            0vmin 0vmin 24.0vmin 24.0vmin hsla(0, 0%, 100%, 0.15),
            0vmin 0vmin 48.0vmin 48.0vmin hsla(0, 0%, 100%, 0.15);
    }
```

The moon is also a circle, but gray. Dimensions are 39x39vmin. The position is vertically centered, but horizontally it's positioned to the far right, outside the screen -- I'll explain why soon.

### Animation

The animation is relatively simple.

First, the **moon** moves to the left, stopping right in front of the sun to show the eclipse effect, then it proceeds to the left, going all the way outside the screen and then it resets to its initial position.

The sun animation consists of reducing the box-shadow's `blur` and `spread` parameters' values to mimic the effect created by a solid, opaque object moving in front of a light source.

Then, the sky is also animated. I only animate the sky colors to transition from normal sky blue to a shade -- dark blue, almost black.

The transitions (sun's reduced light and sky becoming almost black) happens at the keyframes where the moon is in front of the sun. As soon the border of the moon starts approaching the sun's border, the sun's lights start to "weaken" and the sky starts to become darker. The opposite happens as soon as the moon starts leaving from the front of the sun.
