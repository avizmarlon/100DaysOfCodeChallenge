When using some tags like `<u>`, `<strong>` and some others, the browser is applying the respective css styling to the content that is inside the tags.

`<u>` = `text-decoration: underline;` **u**nderline
`<strong>` = `font-weight: bold;` "He's bold, and strong."
`<em>` = `font-style: italic;` **em**phasis
`<s>` = `text-decoration: line-through;` **s**trikethough

`<hr>` adds a **h**orizontal **r**ule across the width of its containing element; used to indicate a change of topic or content or to visually separate groups of content.


### `rgba(r, g, b, a)`

Same as `rgb(r, g b)`, with the added argument "a", which stands for "alpha", used to define the opacity level of the color. Accepted values range from 0 (fully transparent) to 1 (fully opaque).

# `box-shadow` property

This property can be used to make some really cool stuff. Aside from using it to cast shadows on any elements and make they look like they're floating on the webpage. It can be used to make elements "shiny", as if colored lights were emanating from them.

### `text-transform` property

This property can be used to modify text appearance without having to touch the text itself. For instance, it's possible to modify any text affected by this property so that it looks all UPPERCASE or lowercase, or Capitalize Every Word etc.

- Some values for the property:
- - lowercase;
- - uppercase;
- - capitalize;
- - initial; (use default value)
- - inherit;
- - none;

---

The `font-weight` property modifies how thick or thin a text content should be.

The `line-height` property modifies the height of each line of text, so that it takes more, or less, vertical space.

## Gradient text

*The colors and gradient values below are the ones I used on my logo text in my Color Trivia pet project.*

```css
.gradient-text {
	background: rgb(255,98,0);
	background: linear-gradient(90deg, rgba(255,98,0,1) 0%, rgba(0,255,175,1) 52%, rgba(154,0,255,1) 100%);
	-webkit-text-fill-color: transparent;
	-webkit-background-clip: text;
	-moz-text-fill-color: transparent;
	-moz-background-clip: text;
}
```