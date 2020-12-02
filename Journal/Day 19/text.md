# Day 19

## IDEs

I dedicated some hours to research the state of the art tools to web-developing and oh my god... I don't know how I was coding without these tools before. I am SO HAPPY that I found VS Code, it's like a holy gift sent by the gods of code (lol) to make solving problems with code more enjoyable than it already is. I also installed visual studio, android studio and pycharm as I plan in using many other languages after I become proficient with web-dev languages, frameworks etc.

VS Code is definetely my favorite thing right now. It has git support, project management and a GAZILLION extensions to make everything better. I already installed the live server extension so that I can see the changes I make in my code in real time on a webpage using a local server. This is one of the things I wanted the most and so I am really really happy. It was annoying have to alt-tab and ctrl+r to update the website after any relevant changes I wanted to review.

And the linting, multiple column selection, multiple cursor selection, and so many powerful things, I feel like a problem-solver with superpowers now!

---

## transform property

Ok, now I'm getting to one of my favorite parts -- interactivity. Not quite there, cause the main stuff wil come with JS I think, but this is good enough for now.

This property is used to modify 2D and 3D aspects of an element, you can do thigs like rotate, scale, skew move etc in one or more dimensions of an element.

Using pseudo-classes like `:hover` allows me to dynamically change an element based on its state (in this case, when the user hovers over the element).

So I can make an element scale up (increase in size) when the user hovers it. Like a button that increases in sice when the user hovers it. We see this in many great websites and I really love that. The size modification can be done with the scale() function of the `transform` property, e.g.:

```css
.some-selector:hover {
    transform: scale(2);
}
```

This will double the element's size when the user hovers it. It's really cool. I love it.

Note: *You can use multiple functions for the value of a transform property, you just need to separate the functions with a whitespace*

### transform-origin

This property defines the point used as reference for the transformations made by the transform property.

For example: when you use the rotate() function, you're telling the element to rotate around a fixed point, which, if undetermined by the transform-origin property, defaults to the center of the element. So, if you set the `transform-origin` to 0, the rotation would happen around the top-left corner of the element, giving a "falling" effect, which looks interesting in photos, especially with animated `@keyframes`.

---

## pseudo-classes, pseudo-elements and :: vs : selectors

### **pseudo-classes**

They represent different states of an element, so you can apply css rules to an element that is in a specific state. There are many pseudo-classes like:

:hover  
:checked
:empty  
:focus  
:visited

And many others.

For example, you can make an element scale up it's size when the user hovers it by applying css rules to that element with the :hover pseudo-class:

```css
.btn {
    height: 20px;
    width: 40px;
}

.btn:hover {
    transform: scale(1.2);
}
```

This will scale all elements with the `.btn` class exactly 1.2 times (20%) whenever those elements are hovered.

So, basically, pseudo-classes are useful when you want to stylize an element when its in a specific state.

*pseudo-classes are separated from the selector itself by a single colon ":" (without the quotes).*

### **pseudo-elements**

They are used to style specific parts of an element or even "create" a pseudo-element. For example, `::first-line` can be used to stylize the first line of a paragraph, while `::before` creates a pseudo-element right before the selected element.

The `::before` and `::after` pseudo-elements can be used with the `content: ""` declaration to create pseudo-elements, which are useful to create shapes.

Contrary to pseudo-classes, the pseudo-elements are separated from selectors by two colons "::" (without quotes) instead of one. E.g.: `div.container::before`.

`::before` creates a pseudo-element that is the first child of the selected element, while `::after` creates a pseudo-element that is the last child of the selected element.

### **:: vs :**

Double colon and single colon exist to help distinguish pseudo-classes from pseudo-elements. It's considered good practice to keep this pseudo-class vs pseudo-elements distinction consistently throughout the code.
