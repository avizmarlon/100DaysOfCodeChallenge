There are 3 ways to build a grid layout, that I've found:

- `float;`
- `display: inline-block;`
- `display: flex;`

A float layout is built by creating elements with the `float: left;` property. They will 
be positioned side by side in the top-left of its parent. To create a break, so that the next float element goes in the line below in the document flow, the `clear: left;` rule is used, so that the element with such property can't have a floated element to its left, forcing it to go down to the next line in the document flow. Centering a float layout can be done with `display: table; margin: 0 auto;` in the container.

Layouts using inline-block follow the normal document flow of inline-level elements. They will be placed side by side until a block-level element comes in the document flow. So, you can create a div and place your inline-block elements inside it, then create another div (for the other row) and place other inline-block elements in it. Divs by default are block-level elements, so they can't be placed in the same line, so you have 1 div in each line and inside each div you have multiple inline-block elements and since they aren't blocks, they are positioned side by side. Centering an inline-block layout can be done with `text-align: center` in the container. **NOTE:** Inline-block elements behave similar to text (hence why text-align works), so they have natural whitespace. To get rid of it, use `font-size: 0;` in the container to remove it and restore the property in the child, in case it's needed.

*In all cases, a width should be carefully set to make sure you have as many elements in each row as you want.*

*Technically, inline can be used as well, but inline-block has the same features, plus a few extra important ones like allowing you to change the width and height of the elements.*

The flex grid seems more future-proof, though not supported in all browser versions. I don't know much about this one, as I haven't learned about it yet, I just know grid layouts can be done with it and it provides a lot more functionality and control. Looking forward to learn it eventually.

## inline-block code example
```
<head>
<style>
	.container {
		padding: 5px;
		margin: 0 auto;
		border: 5px solid black;
		text-align: center;
		max-width: 600px;
		min-width: 600px;
	}

	.row {
		margin: 5px;
		border: 5px solid blue;
		font-size: 0;

	}

	.row-item {
		display: inline-block;
		margin: 3px;
		width: 22%;
		height: 100px;
		background-color: red;
		border: 5px solid black;

	}
</style>
</head>
<body>
<div class="container">
	<div class="row">
		<div class="row-item">row-item</div>
		<div class="row-item">row-item</div>
		<div class="row-item">row-item</div>
		<div class="row-item">row-item</div>
	</div>
	<div class="row">
		<div class="row-item">row-item</div>
		<div class="row-item">row-item</div>
		<div class="row-item">row-item</div>
		<div class="row-item">row-item</div>
	</div>
	<div class="row">
		<div class="row-item">row-item</div>
		<div class="row-item">row-item</div>
		<div class="row-item">row-item</div>
		<div class="row-item">row-item</div>
	</div>
</div>

</body>
```