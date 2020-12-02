# Day 8

## `position: static;`, `position: absolute;`, `position: relative;`, `position: fixed;` and `position: sticky;`

## `position:static;`

Default value for all elements when no position property is manually set.

The element simply follows the normal flow of the document structure.

## `position:absolute;`

The element with this property is removed from the normal flow of the document structure. Elements below it, will go up 1 line.

When changing the side values (top, bottom, left, right), the reference point will be the containing element with a position property set. If the immediate containing element doesn't have a position property set, it will go up in the hierarchy until it finds a parent that has the position property set, up to the `<html>` tag.

## `position: relative;`

Doesn't lose it's normal flow position. It moves relative to it's own original starting position.

## `position: fixed;`

The element will break out of the normal flow of the document and be fixed in the position determined by top, left, right and/or bottom properties using the viewport as reference or positioning context (containing element) and stay there even after scrolling the page to any direction.

## `position: sticky;`

A mix between `position: relative;` and `position: sticky;`.

The element will follow the normal flow of the document, but once it reaches (while scrolling) the defined top, left, bottom or right property values set in the CSS, it will stick to that position and stay there until the page is scrolled back to the relative/original position of the element or until the page is scrolled past the element's parent space.

---

The `top`, `right`, `bottom` and `left` properties can be easily remembered as follows:
The element being affected by these properties and the properties themselves can be imagined as magnets, where the properties have the opposite pole and are always repelling the element. So if you set top to 10px, the element will move 10px away from the top property, essentially moving down.

If you use negative values to these properties, then the opposite happens, the element will be "attracted" to that side. E.g.: Setting the top to -10px, will make the element move TOWARDS that side, essentially moving up.

## document flow

Refers to the way the elements are ordered in the HTML document.

A normal flow means the elements are positioned as they were declared in the HTML document and according to their default display property value (block or inline). A block-level element written on line 1 will appear above the element written on line 2 and so on. Same applies for nested elements (parent-children element relationship). An inline-level element, `<em>` for example, written on line 1, before another in-line element, `<span>` for example, will visually appear in the same line 1 and before the `<span>` element.
