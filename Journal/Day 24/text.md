# Day 24

Started working on the animated star system.

It's proving to be harder than I expected, probably because I'm trying to make 2D elements look 3D.

I haven't got to the planets moving and resizing based on perspective etc., but I was having trouble making 3D-looking orbit lines.

I tried radial-gradient, but they would cut in the content-border if I did some kind of transform().

I tried multiple box-shadow layers in an element with an elliptic shape, but felt limiting.

So I ended using multiple nested divs for each orbit line. This way I was able to fine-tune each orbit line individually to my like and do all kinds of transforms.

It was also key to use relative units instead of absolute units, because everything would fall out of place when resizing the window, so I started using relative values. I think the only property using absolute value is the border (which makes the orbit line) and some "draft" borders that I use while "drawing" the project in the browser.

I'm using the vmin relative unit, but I have a feeling I will have to change to vw and vh. The reason is that when I resized (decreased) the window horizontally the elements would go up in an unpleasant way. 

Will test tomorrow and see the differences. For today, I think it's enough. Gotta sleep too.
