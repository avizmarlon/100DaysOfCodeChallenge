# HSL

HSL is an alternative method to represent a color. RGB declares a color by setting the brightness intensity of each of the primary colors -- **r**ed, **b**lue and **g**reen, but HSL uses hue, saturation and lightness.

Hue is the color itself, but it's a value between 0 and 360, representing an angle in a color wheel (a circle).

The primary colors (red, green and blue) are positioned in a triangle pattern in the color wheel, red being at 0 degrees, green being at 120 degrees and blue being at 240 degrees. Each primary color is separated by 120 degrees. In the middle of each of them are the secondary colors, which are a result of combining two primary colors. Red and green creates yellow, so between them, at the 60 degrees position, which is the exact middle point between 0 degrees (red) and 120 degrees (green) is the yellow color. The same applies to the other secondary colors (cyan and magenta).

Saturation is the amount of gray in the color. The values range from 0% to 100%, with 0% having no saturation at all, essentially becoming completely gray and 100% having no saturation at all, being the normal color.

Lightness refers to the amount of white or black in the color. Values range from 0% to 100%, where 0% is completely black, 100% is completely white and 50% is the normal color.

---

I think hsl() is a better way to memorize a system of color code when compared to rgb(), because you only have to memorize the color wheel and then use the angle (0 to 360) to pick the color. E.g.: red is at the very top, at 12 o' clock, so to speak, or simply at 0 degrees (or 360 degrees), so you can pick red by writing `hsl(0, 100%, 50%);` or `hsl(360, 100%, 50%);`. Note that red is the only color that can be picked with one of two different hue values, since 0 degrees = 360 degrees.

To pick black, choose any hue value and any saturation value, but use 0% as the lightness value. The opposite (100%) if you want white.

To use different tones of gray, use any hue value; 0% for saturation and adjust the lightness color to get the gray tone you want.

Adjusting the lightness level to a vlaue greater than 50% allows you to make a shade of the hue (color) by adding black to it; adjusting it to a value less than 50% allows you to make a tint of the color, by adding white to it.

Making a tone of the color can be done adjusting the saturation value. The smaller the saturation value, the more gray the color will have.

Combining different saturation and lightness values allows for a lot of possible variations of a hue (color).

Changing lightness and/or saturation while keeping the same hue is useful to create accent colors. E.g.: you pick a hue to be the dominant color and then use the same hue, but with different saturation and lightness levels in other parts of the website to accentuate them in relation to the dominant color.
