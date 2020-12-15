# Day 33

I studied more of the FCC course, section "Applied Visual Design". It's almost complete (close to 100%).

I knew most of the things, because I learned them on my own while creating the animated star system.

However, here's what I actually learned that I didn't know how it exactly worked (everything I type here is from my mind. I don't copy-paste anything, because I think that doesn't help in the learning process, I do use external sources to review what I type here just to make sure I'm not typing incorrect information for future references):

- `animation-fill-mode`: This property allows me to "freeze" the animation before it starts (`backwards` or after it ends (`forwards`).
  - `backwards`:  The element will have the same style as the 0% keyframe until the animation begins. So, unless the `animation-delay` is set, the `backwards` value won't have a visible effect, because the animation will start instantly. So, to use `backwards` as the `animation-fill-mode` value, the `animation-delay` must have a value of time that allows the `backwards` effect to be noticeable.
  - `forwards`: After the animation ends, the element will use the same style as the 100% keyframe, essentially "freezing" the animation at the 100% keyframe to preserve the last keyframe's style. One example usage where this might be useful is an animated hover state of a button that changes it's `background-color`. You don't want the color to revert back to it's original value while the user still has it's mouse cursor hovering the button, so you want the color to be "frozen" when the animation ends. This way the button will remain with the color defined in the keyframes until the user moves the mouse cursor away from the button (because the animation is applied only to the `:hover` state of the button).

- `animation-timing-function`: This defines how the animation should flow throughout its duration. I had a basic idea of how this worked, but now I understand it better. Before studying it, I would try random values until I liked the effect, now I know the values I want without having to do trial-and-error testing. Well, not entirely. I didn't learn about the bezier curve yet, but that's the next topic in the course.
  - `ease` is the default value.
  - `ease-in`: animation starts slow and accelerates towards the last keyframe.
  - `ease-out`: animations starts fast and slows down towards the last keyframe.
  - `ease-in-out`: mix between ease-in and ease-out; starts slow, accelerates towards the middle keyframe (50%), then slows down towards the last keyframe.
  - `linear`: keeps the same speed throughout the whole animation, from the 0% keyframe to the 100% keyframe.
