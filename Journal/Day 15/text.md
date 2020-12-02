# Day 15

I learned a really cool shadow layering technique on [tobiasahlin's blog](https://tobiasahlin.com/blog/layered-smooth-box-shadows/).

By using multiple layers of the `box-shadow` property with exponentially increasing offset and blur values, we can render a more smooth and realistic shadow, with increased control over its details. E.g.:

```css
.smooth-shadow {
    box-shadow: 0px 1px 1px rgba(0, 0, 0, 0.20),
    box-shadow: 0px 2px 2px rgba(0, 0, 0, 0.20),
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.20),
    box-shadow: 0px 8px 8px rgba(0, 0, 0, 0.20),
    box-shadow: 0px 16px 16px rgba(0, 0, 0, 0.20),
    box-shadow: 0px 32px 32px rgba(0, 0, 0, 0.20);
}
```

I already applied this technique to the buttons in my soundboard pet project. I also added a red colored shadow to the hover pseudoclass of these buttons so that they look like they're glowing when the user hovers over them.

---

Also discovered how to remove the annoying outline appearing on my buttons when I click them. They look weird because the button have `border-radius: 50%;` and the outline is square, so... yikes. Setting `outline: none;` removed the outline. Feels better.

---

I've become fascinated by color theory. I played a lot with different color wheels across the Internet. Really like the adobe, canva and paletton wheels.

I find myself observing objects in real life and figuring out which color scheme it uses (monochromatic, analogous, complementary, triadic, tetradic/square, double split complementary etc.), why it uses such scheme and if it would look better with another color combination.
