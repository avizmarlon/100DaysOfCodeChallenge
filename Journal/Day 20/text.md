# Day 20

## \#keyframes animation

```css
div.i-am-animated {
    display: inline-block;
    height: 20px;
    background-color: red;
    animation-name: increase-width;
    animation-duration: 5s;
}

@keyframes increase-width {
    0% {
        width: 0%;
    }
    50% {
        width: 50%;
    }
    100% {
        width: 100%;
    }
}
```
