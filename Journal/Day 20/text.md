# Day 20

## \#keyframes animation

Animation of html elements can be done with the combination of the `animation` property and the `@keyframes` at-rule.

`animation` is a shorthand for all the `animation-` properties, like `animation-name`, `animation-duration`, `animation-delay` etc. The order of the values in the shorthand is important. For example, there are two properties that use the same type of value (\<time\>), which are `animation-duration` and `animation-delay`, and the first value in the `animation` shorthand property always refers to the `animation-duration`, while the second refers to `animation-delay`.

While using the shorthand `animation` property, care should also be taken when choosing a value for the `animation-name`, so that you don't choose a value that happens to be a keyword for another property, for example: the "infinite" keyword is a valid value for the `animation-iteration-count` property, so setting the `animation-name` to "infinite" will cause conflicts and the `animation-name` will be invalidated and treated as if it had no value, thus making you unable to use the animation.

All animations must include a `animation-duration` property value or it won't work (there will be no motion).

`@keyframes` is an at-rule used to apply styles to specific points of the animation timeline. These specific points are defined as percentages of the total duration of the animation.

You associate the subset of rules inside the `@keyframes` at-rule by typing the `animation-name` value of the property that you want to animate after the `@keyframes` separated by a whitespace. E.g.:

```css
div.animate-me {
    position: relative;
    top: 0;
    left: 0;
    width: 50px;
    height: 50px;
    background-color: blue;
    animation-name: moveUpAndDown 4s infinite;
}

@keyframes moveUpAndDown {
    0% {
        top: 0;
    }

    25% {
        top: -50px;
    }

    50% {
        top: 0;
    }

    75% {
        top: 50px;
    }

    100% {
        top: 0;
    }
}
```

The above example selects all divs with the `.animate-me` class and makes it into a 50px x 50px blue square moving up and down animation with a duration of 4s, looping infinitely.

Although it lasts for an infinite amount of time, the duration is still important so that you can style the animation at specific points of the animation timeline. The percentages refer to a point in the timeline of the animation. For example, in an animation with a duration of 4s, a 50% keyframe would refer to the 2 second point of the timeline, so the styles under the 50% sub-rule would be applied when the animation reached the 2 second mark, in our example, it would set the `top` property to `0`.

Here's another example:

```css
div.i-am-animated {
    display: inline-block;
    height: 20px;
    background-color: red;
    animation-name: increase-width;
    animation-duration: 6s;
}

@keyframes increase-width {
    0% {
        width: 0%;
    }
    50% {
        width: 50%;
    }
    100% {
        width: 100%;
    }
}
```

In this example, a css rule will select all div elements with the class `i-am-animated` and make a red 20px high shape, with no width determined increase in width, up to 100% of the viewport width in the duration of 6s.

It starts with 0 width, then it transitions into 50% width in the 50% point of the animation timeline -- since the total animation duration is 6s, the 50% point refers to the 3 second mark of the animation timeline -- and then it transitions all the way to 100% width until it reaches the 100% mark in the timeline. Essentially, creating an increasing horizontal bar that could be used as a loading bar.
