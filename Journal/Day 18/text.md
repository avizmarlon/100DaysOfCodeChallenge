# Gradient css functions

So, I've learned about the `linear-gradient` and `repeating-linear-gradient` functions.

Apparently any gradient pattern can be made using gradient-related functions. I saw that there are conic, gradial etc. patterns for a gradient function, so the developer's creativity is the limimt I guess.

I had a little trouble understanding the repeating version of the gradients, but now I understand and it seems SO DAMN EASY. It's amazing how something that was seemingly confusing becomes so easy and intuitive once you think about it, read from other sources, watch videos, play with the code, break it, change it and see what happens -- all of this helps understanding a concept. I'm glad I did the Coursera's course "Learning how to Learn" by Barbara Oakley. Learning is much easier with her methods, but I digress.

### linear-gradient()

It's used to make non-repeating smooth transitions between two or more colors. If undefined, the direction argument will default to the equivalent of `180deg` (or top to bottom). The direction argument is usually the first argument for the linear-gradient() function. All other arguments are color and their position stops.

The direction value can range from 0deg to 360deg, so the transition goes from a starting point to the specified angle. *Negative values can be used.*

The color values can be any valid way to pick a color, like rgb(), rgba(), hsl(), hsla(), color name, hex code etc. The color values are separated by a comma (,).

The color stop comes right after the color, separated from the color value by a single whitespace (e.g.: red 20px). This value is used to determine at which point of the container the color stops in the transition.

For example:

```css
.some-class-selector {
    background: linear-gradient(
                90deg,
                red,
                blue 50%,
                green 80%
                );
}
```

So, notice I didn't set a position value for the red color. When that happens, it defaults to a position value that will try to equalize the distance between the adjacent colors, essentially defaulting the value to the middle point between the previous and the next colors in the transition. In our example, if blue didn't have the 50% stop value defined, and it was empty/undefined, it would default to 40%, since that's the middle point between red (0%) and green (80%). In red's case, since it's the first color value, it defaults to 0. If the last color (green) didn't have a stop value set, it would default to 100%.

Blue is set to 50%, that means a transition from red to blue will occur from point 0 (red position) to the 50% point of the container, where blue stops. So it will start red and transition to blue up to the middle of the container (because it's 50%).

Then, since green stops at 80%, the blue color will transition from the 50% point of the container to the 80% point of the container, where the green color stops.

In linear-gradient(), if the last color-stop is less than 100%, the rest of the container will fill with this last color. In our example, since green stop is specified as 80%, the rest of the 20% will be filled with green. In the repeating-linear-gradient() case, instead of filling the remaining space with the last color, it will loop the gradient and start a new transition, basically repeating the transition that happened before. In our example, it would start again red 0 -> blue 50% -> green 80%, then from the 80% point it would loop again red 0 -> blue 50% -> green 80% and so on, until there is no space left in the container. In fact, if you set the last color-stop to 100% in a repeating-linear-gradient(), there will be no space for a new iteration of the gradient transition to occur, so it will display like a regular linear-gradient(), cause there is no room to repeat the gradient pattern. In the case of the last color stop at 80%, there will be no room for more than 1 repetition, in fact, the second repetion won't even have space to go all the way to green again.

### repeating-linear-gradient

It's almost the same as the linear-gradient(), with the difference that instead of ending the transition at the last color-stop, it will repeat the whole transition again (if there is enough space, like mentioned before). So, obviously, if you want a repeating pattern to occur, you can't set the last color to stop at 100%, cause there will be no space for repetition.

To make stripes, you set two adjacent color stops to the same color every two colors (or more depending on the pattern you want). E.g.: red 0px, red 40px. This will make red go from 0px to 40px, but there will be no transition, cause it's impossible to transition from red to red, it's the same color. Then, to make a stripe, you create a second color following this same pattern. E.g.: red 0px, red 40px, blue 40px, blue 80px. The second color should have the same color stop as the previous color stop so that there is no noticeable transition (which would remove the purpose of making a stripes pattern). Now, red will go from 0px to 40px, then blue will go from 40px to 80px and from 80px it will loop and repeat the pattern (red to red to blue to blue), essentialy making a red and blue stripe pattern. Code view example:

```css
background: repeating-linear-gradient(
    90deg,
    red 0px,
    red 40px,
    blue 40px,
    blue 80px
)
```
