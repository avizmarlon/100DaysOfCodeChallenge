# Day 13

The `z-index` property only works on elements that have a `position` property. It changes the order of the elements in the z-axis (which elements appear on top of the other). Normally whatever element comes last in the normal document flow appears on top, when it overlaps with another element, but this can be changed with the `z-index` property.

I'm starting to think it's a good idea to always set a `position` property in all elements, probably with the `relative` value. The reason is that I noticed a lot of positioning-related properties only works in elements that have a `position` property set. Although every element is static by default, the `static` value doesn't seem to be taken into consideration when trying to use properties that require a `position` property set. `position: absolute;` and `z-index` comes to mind when thinking of css rules that function based on whether the element has a `position` set or not, and there's probably more rules than these two.

**Color harmony** is the art of creating a sense of order and equilibrium out of color combinations.

Color wheels are useful to visualizing color formulas. Many are available freely online. I personally like using the [adobe color wheel](https://color.adobe.com/create/color-wheel).

There are some color schemes based on different color wheel sizes.

- Analogous colors
- Complementary colors
etc.

Nature is a great source of inspiration as it has many ways of demonstrating powerful and beautiful color combinations without necessarily fitting into a mathematical formula.
