Giving only one value to a css property like padding or margin (properties that can change each side of a HTML element individually), will set that value to all 4 sides of the HTML element. E.g.:

```css
.big-padding {
	padding: 3em;
}
```

is the same as

```css
.big-padding {
	padding: 3em 3em 3em 3em;
}
```
This sets the padding property of the top, right, bottom and left sides of any HTML element with the attribute `<class="big-padding">` to 3em.
--------------

# Custom CSS Properties (or Custom CSS Variables)

Syntax:
```css
.selector-name {
	--custom-var-name: custom-var-value;
}
```
Example:
```css
.colors {
	--warning-color: red;
}

#delete-account-button {
	color: var(--warning-color, black);
}

.negative-choice {
	color: var(--warning-color, black);
}
```
CSS variables are like any other variable in any other programming language, they store a value to be used as many times as the developer wishes throughout the code.

It's a handy tool, especially in a large project, for it allows the developer to change the property of multiple elements by changing just the variable's value from which those elements' properties receive their value.

Following the above example, if I wanted to change the color of both elements, I wouldn't have to change each individually (imagine a project with thousands of elements), as I would have the option to simply change the --warning-color CSS variable value to the color I want and it would apply to all css selectors that use that variable's value.

Note: the "black" as the second argument for the var() function, serves the purpose of a fallback value. Basically, if the browser can't find the variable or there is some problem with it, it will use the fallback value, in this case, "black". So the color would be black, and not red.

I read around about css custom properties. It's supported in all major modern browsers. You can also use a custom property as the value for another custom property as many times as you wish. E.g.:

```css
:root {
	--red-color: red;
}

.colors {
	--warning-color: var(--red-color, black);
}

.negative-choice {
	color: var(--warning-color, black);
}
```

~~I'm not sure where this would be useful, but I'm sure it has some use, right?~~

EDIT: Just learned how this actually works.

Apparently, it's good practice to define CSS custom variables inside the :root pseudo-class, because it's like defining a global variable. The scope of the :root pseudo-class is global, so any other selector can call the variables from :root.

Then, if you don't like the selector name ":root" because it's not meaningful as an identifier, you can create another selector, say ".colors" like I did above and then create another custom CSS property and the value of this property will be a call to the variable defined in the :root css definition. Just like I wrote in the above example.

Ah yes, it feels good to finally understand something you were previously confused about. Also, I didn't know what :root was, now I know, and I know a good use-case for it already, I learned it as a "side-effect" of researching about custom css variables.

--
:root is a pseudo-class that is like the biggest box in which all the other boxes (selectors) are in. It has one of the highest priorities in css cascading or specificity when calculating css precedence rules, thus defining a custom css variable inside it is optimal, as it makes the variable "global", enabling all other selectors to use the variables defined inside :root. I think it only loses to the "!important" keyword that you can place after a property's value and maybe inline style.

:root can be used to represent the "biggest box" (the tag in which all other tags are nested in) in many types of documents, not just html/css. In the case of html/css, it represents the <html> tag, although :root has higher specificity than <html>.

In SVG, :root would represent <svg> and so on.