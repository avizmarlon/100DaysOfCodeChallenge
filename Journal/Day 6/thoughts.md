## To place elements side by side, while also allowing to modify width and height properties, use the `display:inline-block` css declaration.

---

## Differences between inline, block and inline-block values for the display property:

- inline: allows elements to be placed side by side, as if no line-break was placed after the element. Can't modify height and width. Can modify padding and margin, but only affects horizontal space. (only padding-left, padding-right, margin-left and margin-right)
- block: acts as if a line-break was added after the element, so other elements placed after it will go below it. Can modify width, height. Can modify padding and margin in both horizontal and vertical planes.
- inline-block: mix of the above two options. No line-breaks after the element, allowing side-by-side positioning. Can modify width and height. Can modify padding and margin in both horizontal and vertical planes.

---

## To centralize an image, use:

```css
.center-image {
	display: block;
	margin: 0 auto;
}
```

First margin value is for top and bottom, second is for left and right. Setting auto makes it use same space on both sides, essentially centering the element.

---

## To curve only one edge of a element, use the properties `border-top-left-radius`, `border-top-right-radius`, `border-bottom-right-radius` or `border-bottom-left-radius`.

