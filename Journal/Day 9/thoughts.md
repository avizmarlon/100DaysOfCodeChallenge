The `float` property goes hand in hand with the `clear` property.

`float` is like another value for the `display` property (but not really), because it kinda of creates its own layer on the document flow. The element that receives the `float` property is removed from the normal flow of the document and is placed on the "float-level" layer of the page. Similar to an element that receives `position:absolute` or has their `display` property changed.

When the element receives `float:left;`, it is removed from the normal document flow, elements below it will go up 1 line and be placed either underneath it or at its side depending on factors like their `display` and `clear` properties.

If the element below it also receives the `float:left;` rule, it will enter the "float-level" layer of the page and join the other float elements. In this case, since the above element is float, this second element will be placed at its right side. Similar to what happens when two inline-level elements are placed one after the other in the document flow.

You can use `width` to determine how much space of its parent element the floated element should take. This essentially allows the creation of columns. E.g.:

```html
<style>
.container {
	padding: 2px;
	margin: 2px;
	width: 1000px;
}

.floated {
	float: left;
	width: 32%;
	margin: 2px;
}
</style>

<div>
	<img src="cat.png" class="floated">
	<img src="dog.png" class="floated">
	<img src="bird.png" class="floated">
</div>
```

In this example, the 3 images will be placed next to one another, each consuming 32% of its parent total width, resulting in 96% consumption of the parent's total width. Since the parent's width is set to 1000px, each img will use 320px.

The `clear` property defines which sides of the element are not allowed to have a float element.

Using the example above:

```html
<style>
.container {
	padding: 2px;
	margin: 2px;
	width: 1000px;
}

.floated {
	float: left;
	width: 32%;
	margin: 2px;
}

.clear-left {
	clear: left;
}
</style>

<div>
	<img src="cat.png" class="floated">
	<img src="dog.png" class="floated clear-left">
	<img src="bird.png" class="floated">
</div>
```

The dog img is using the `clear: left;` property, so its left side is not allowed to have a float element. Since the cat img is a float element, it cannot be at the left side of the dog img like it normally would, so the dog img goes below the cat img instead of being placed at its right side.

This can be used to essentially create a grid layout, with controllable columns and rows.

To make use of the whole containt element width, while using float elements, the width of each element should be equal to the total parent width divided by the number of float elements on that line. Using percentage makes this easier. E.g.:

If you want to make a 6x3 grid (6 columns; 3 rows), you would place 6 elements side by side on the first line (row) with `float: left;` and `width: calc(100% / 6)`. Then do the same on the second and third line.

You can create a custom css property like `--num_cols: 6` and use it like `width: calc(100% / var(--num_cols))`, this way, if you decide to change the number of columns, you only have to change the variable value, instead of changing every ocurrence of the `width` property individually.