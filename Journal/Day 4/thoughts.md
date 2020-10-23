# Fallback for browser compatibility

Sometimes a browser won't understand a css declaration, for being not updated (old version) or simply lack the necessary technology to interpret it. In this case, it's ideal to set a more widely accepted css declaration, be it the property, the selector or the property value.

E.g.:

```css
:root {
	--big-font: 8em;
}

.main-font {
	font-size: 8em;
	font-size: var(--big-font, 8em);
}
```

So, in this case, if the browser can't interpret a custom CSS variable, `font-size: var(--big-font, 8em);`, then the browser will use the declaration that it can interpret, in this case: `font-size: 8em;`. In a more modern browser, which can interptet custom CSS variables, it will simply use whatever declaration it can interpret comes last in the cascade, based on the precedence rules, in this case, the last declaration (the one that takes the highest priority in the precedence rules) is `font-size: var(--big-font, 8em);`.

---

By the way, I had no idea what a media query was when FCC just threw the term at me (was I supposed to know?), although I kinda of deduced the meaning by reading the code. Still, I researched about it and found out I was right. It's a way of analyzing the user's device to find information such as viewport width and height, device width and height, resolution, if a mobile is rotated (portrait or landscape) and many other features. Then, based on the information acquired through the media query, using the `@media` rule, styling can be applied, conditionally, to the webpage based on this information.

Simple responsive web-design stuff I suppose. Like, resizing a webpage banner image based in the user's viewport. By the way, I also didn't know what viewport was, but I learned while researching about media queries. viewport is just the user's visible area of the webpage. Logically, the viewport is smaller on mobile devices when compared to desktop computers. So, you can set a `@media` rule to style the webpage differently if the viewport is small enough. Like, resizing everything to smaller sizes to fit in a mobile screen, putting the navbar in the three-lines icon that is popular technique used in many responsive web-pages. E.g.:

```css
:root {
	--banner-size: 300px;
}

@media (max-width: 300px) {
	:root {
	--banner-size: 100px;
	}
}
```

The browser will set the property's values that use the `--banner-size` custom property's value to 100px if the user's viewport is 300px or less. Otherwise, it will use 300px as the value for whatever property used the `--banner-size` custom property's value. So, basically, it says "reduce the banner size from 300px to 100px if the user's screen is equal to or less than 300px." (I think I was very redundant here. Well, English isn't my native language, I'm trying here ok?)