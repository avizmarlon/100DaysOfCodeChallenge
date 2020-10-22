DOM = Document Object Model
Used by CSS, JS and probably other technologies as a way to structure web document.
-----

CSS Clockwise Notation
Sets a CSS property for all sides of an element in a single line. E.g.:

```css
.big-margin {
	margin: 10px 5px 10px 5px;
}
```

This selects any HTML element with the class `big-margin` and set its top and bottom margin to 10px, and the left and right margin to 5px.
--------

CSS Selectors

Class:

```css
.class-name {
	css_property:property_value;
}
```


ID:

```css
#id_name {
	css_property:property_value;
}
```


Attribute:

```css
[attribute_name=attribute_value] {
	css_property:property_value;
}
```
Attribute Selector Example:

```css
[type="checkbox"] {
	margin-top: 10px;
	margin-bottom: 10px;
}
```

This selects all HTML elements that have the attribute `type` with this attribute's value set to `checkbox` (e.g.: `<input type="checkbox`>) and changes the top and bottom margin to 10px.
----------------------

font-family Degrade

```css
.lobster-font {
	font-family: "lobster", monospace;
}
```

If the `lobster` font-family is not available, it will degrade to the next available font -- in this case the generic font `monospace`. Note that generic fonts SHOULD NOT have quotes (`"monospace"`), or they won't work.