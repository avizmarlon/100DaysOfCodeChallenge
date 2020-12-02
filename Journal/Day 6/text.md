# Day 6

I used my session today to start a pet project using what I've learned so far. I call it Color Trivia. Just a website to share trivia facts about colors and also interesting statistical data on the usage of colors throughout the web and history.

I was creating the logo area and I wanted to center the logo image and the logo text, while also making them clickable with anchor elements.

I spent quite some time learning in=depth how the display property works, because I needed to make my `<img>` a block element to centralize it with the `margin: 0 auto` property, which makes both sides of the element have the same space, essentially centralizing it. I set the img size by limiting how much of the horizontal space the img can use. The height adjusts automatically I think, maintaining aspect ratio.

Since I wanted to make the img an anchor link as well, I put the img tag inside the anchor tag, but the whole horizontal space was clickable. I wanted JUST the image and the logo text to be clickable. After researching, and, unsurprisingly, stumbling into a stackoverflow question, I discovered I had to put all of those elements (img, anchor, h1) inside a div container and create a class for the container with the text-align property set to center. The text-align property works, because, by default, elements are set to be displayed as blocks (`display:block`), like `<p>` tags, in which, text-align is known to work.

I also learned about the inline and inline-block values for the display property. `display:inline` allows elements to be placed side by side in the horizontal space they are in, as if no line-break was placed after the element, margin and padding can still be modified, but they only increase the distance to the adjacent elements horizontally, can't modify height and width. `display:block` acts as if a line-break was added after the element, making other elements placed after it go below it, they allow modifications to the width and height properties. `display:inline-block` is a mix of the previous two, it allows you to have elements placed side by side as if no line-break was placed after the element, while also allowing the properties width and height to be freely modified.

While learning all this, I create a pretty cool thing, like a color pie. Images of the color pie and the html/css code is in the same folder this file is in.

Basically I created a rectangular div element with an absolute height and relative width. Then I created 4 children divs, giving them all the display property of inline-block so that I could place them side by side and modify their width and height. Then I increased their width with relative values so that only two divs could fit in one line. So I had a 2x2 formation in the end. I colored each div with one of the primary colors. First row -- red, blue; second row -- yellow, green.

Then I had the idea to turn this box into a pie (similar to those pie graphs). I had learned about the border-radius property in a FCC earlier lesson already. But I was wondering if I could apply that property to only one edge of the element, and as I was wondering this, I wrote border-radius in my text editor (sublime 3) and it suggested many autocompletes for the border-radius and I saw border-top-right-radius and the 3 others. Exactly what I needed. Really cool stuff. At least for me, as a newbie.
