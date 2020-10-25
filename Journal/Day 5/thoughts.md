Using % as a length unit in property values when defining properties such as `width`, will set the element's width to a % of its parent element (such as a div), or the total webpage width when there is no parent containing element. E.g.:

```html
<style>
	.main-box {
		width: 100%;
	}

	.text-box {
		width: 50%;
	}

	.footer-box {
		width: 75%;
	}
</style>

<div class="main-box">
	<div class="text-box">
		<p>Ipsum Ipsum?</p>
	</div>
	<div class="footer-box">
		<p>Copyright</p>
	</div>
</div>
```

In this example, we would have a main box div with a width equal to the user's viewport (because it has no parent containing element) and two boxes inside it.

The text-box has a width set to half of its containing parent `<div>` element.
The footer-box's width is equal to 3/4 of its containing parent `<div>` element.

By reducing the viewport for testing, such as resizing the window, the main-box will reduce its width, which in turn, will reduce the text-box and footer-box width, but they will always be 1/2 and 3/4 of the main-box width because they are children of main-box and their css rules determine their width with a relative length unit (%).