I learned a really cool property today -- `box-shadow`. Omg, I really love this property. I applied to my color pie and modified it so that it looks shiny with neon lights. I loooove it. I can imagine some really cool stuff that can be made with it.

Now I messed around with border-radius on specific edges and the color pie transformed into a neon colorful flower.

I wanted to make my logo text gradient so I went ahead and researched how to do it. The technique is pretty smart. It created a gradient background image behind the text element, then clips the background with the text so that the background only appears where there are letters/text and then changes the transparency of the text so that the text gets filled with whatever is behind it, in this case, the gradient background image. Code is as follows:

```css
.gradient-text {
	background: rgb(255,98,0);
	background: linear-gradient(90deg, rgba(255,98,0,1) 0%, rgba(0,255,175,1) 52%, rgba(154,0,255,1) 100%);
	-webkit-text-fill-color: transparent;
	-webkit-background-clip: text;
	-moz-text-fill-color: transparent;
	-moz-background-clip: text;
}
```

I'm not 100% sure how the linear-gradient function works yet, as I copied the value from a gradient color generator website. But I have an idea. I think the first value is the direction of the color gradient effect, the second is the first color followed by the percentage of the space where it starts, then comes the second color located at the "position" 52% of the space and the third color at the end (100%). I will eventually read in-depht about it and see if I was right.