from htmlparcing import *
import requests

f_html2 = """
<!doctype html>
<html>

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>Ученый</title>
</head>

<body>
    <div class="container">
        <div class="parallax">
            <div class="parallax-layer background">
                <img src="imgs/%D1%84%D0%BE%D0%BD.png" />
            </div>
            <div class="parallax-layer group_body group_body_animation">
                <div class="parallax-layer second-hand">
                    <img src="imgs/%D0%BF%D1%80%D0%B0%D0%B2%D0%B0%D1%8F%20%D1%80%D1%83%D0%BA%D0%B0.png" />
                </div>
                <div class="parallax-layer second-hand">
                    <img src="imgs/%D0%BF%D1%80%D0%B0%D0%B2%D0%B0%D1%8F%20%D1%80%D1%83%D0%BA%D0%B0.png" />
                </div>
            </div>
        </div>
    </div>
    <script src="js/script.js"></script>
</body></html>
"""

f_html = """
<!doctype html>
<html>

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>Ученый</title>
</head>

<body>
    <div class="container">
        <div class="parallax">
            <div class="parallax-layer background">
                <img src="imgs/%D1%84%D0%BE%D0%BD.png" />
            </div>
            <div class="parallax-layer body_animation">
                <div class="parallax-layer body">
                    <img src="imgs/%D1%82%D0%B5%D0%BB%D0%BE.png" />
                </div>
                <div class="parallax-layer hand1_group_animation">
                    <div class="parallax-layer hand1">
                        <img src="imgs/%D0%BF%D0%BB%D0%B5%D1%87%D0%BE.png" />
                    </div>
                    <div class="parallax-layer hand2_group_animation">
                        <div class="parallax-layer hand2">
                            <img src="imgs/%D0%BA%D0%B8%D1%81%D1%82%D1%8C2.png" />
                        </div>
                    </div>
                </div>
                <div class="parallax-layer head_group_animation">
                    <div class="parallax-layer head">
                        <img src="imgs/%D0%B3%D0%BE%D0%BB%D0%BE%D0%B2%D0%B0.png" />
                    </div>
                </div>
                <div class="parallax-layer Collar">
                    <img src="imgs/%D0%B2%D0%BE%D1%80%D0%BE%D1%82%D0%BD%D0%B8%D0%BA.png" />
                </div>
            </div>
            <div class="parallax-layer table">
                <img src="imgs/%D1%81%D1%82%D0%BE%D0%BB.png" />
            </div>
            <div class="parallax-layer body_animation">
                <div class="parallax-layer second-hand">
                    <img src="imgs/%D0%BF%D1%80%D0%B0%D0%B2%D0%B0%D1%8F%20%D1%80%D1%83%D0%BA%D0%B0.png" />
                </div>
                <div class="parallax-layer hand1_group_animation">
                    <div class="parallax-layer hand2_group_animation">
                        <div class="parallax-layer hand3">
                            <img src="imgs/%D0%BA%D0%B8%D1%81%D1%82%D1%8C.png" />
                        </div>
                    </div>
                </div>
            </div>
            <div class="parallax-layer background2">
                <img src="imgs/%D1%84%D0%BE%D0%BD%202.png" />
            </div>
            <div class="parallax-layer portal2 portal2_animation">
                <img src="imgs/%D0%9F%D0%BE%D1%80%D1%82%D0%B0%D0%BB%202.png" />
            </div>
            <div class="parallax-layer body2_animation">
                <div class="parallax-layer body2">
                    <img src="imgs/%D1%82%D0%B5%D0%BB%D0%BE%202.png" />
                </div>
                <div class="parallax-layer head2_animation">
                    <div class="parallax-layer head2">
                    </div>
                    <img src="imgs/%D0%B3%D0%BE%D0%BB%D0%BE%D0%B2%D0%B0%202.png" />
                </div>
                <div class="parallax-layer arm1">
                    <img src="imgs/%D0%BB%D0%B5%D0%B2%D0%B0%D1%8F%20%D1%80%D1%83%D0%BA%D0%B0%202.png" />
                </div>
                <div class="parallax-layer arm2">
                    <img src="imgs/%D0%BF%D1%80%D0%B0%D0%B2%D0%B0%D1%8F%20%D1%80%D1%83%D0%BA%D0%B0%202.png" />
                </div>
                <div class="parallax-layer collar2">
                    <img src="imgs/%D0%B2%D0%BE%D1%80%D0%BE%D1%82%D0%BD%D0%B8%D0%BA%202.png" />
                </div>
            </div>
        </div>
    </div>
    <script src="js/script.js"></script>
</body></html>
"""

f_css = """
::-webkit-scrollbar {
    width: 0;
}

*,
*::before,
*::after {
    padding: 0;
    margin: 0;
    border: 0;
    box-sizing: border-box;
}

a {
    text-decoration: none;
}

ul,
ol,
li {
    list-style: none;
}

img {
    vertical-align: top;
}

h1,
h2,
h3,
h4,
h5,
h6 {
    font-weight: inherit;
    font-size: inherit;
}

html,
body {
    line-height: 0;
    font-size: 16px;
    background-color: black;
}

.container {
    max-width: 500px;
    max-height: 1080px;
    margin: auto;
    background-color: black
}

.parallax {
    height: 100vh;
    background-color: black;
    overflow-x: hidden;
    perspective: 10px;
}

.parallax-layer {
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
}

.background {
    transform: scale(0.36) translateZ(-1.1px);
    top: 0px;
    left: -230px;
}

.body {
    top: 0px;
    transform: scale(0.36);
    left: -230px;
}

.table {
    transform: scale(0.36) translateZ(-1px);
    top: 0px;
    left: -230px;
}

.hand1 {
    top: 0px;
    transform: scale(0.36);
    left: -230px;
}

.hand2 {
    top: 0px;
    transform: scale(0.36);
    left: -230px;
}

.hand3 {
    top: 0px;
    transform: scale(0.36);
    left: -230px;
}

.second-hand {
    top: 0px;
    transform: scale(0.36);
    left: -230px;
}

.head {
    top: 0px;
    transform: scale(0.36);
    left: -230px;
}

.Collar {
    top: 0px;
    transform: scale(0.36);
    left: -230px;
}


.body_animation {
    transform-origin: 250px 700px;
    animation-name: full-body-animation;
    animation-duration: 1s;
    animation-iteration-count: infinite;
    animation-timing-function: ease;
}

.hand1_group_animation {
    transform-origin: 240px 600px;
    animation-name: hand1-animation;
    animation-duration: 1s;
    animation-iteration-count: infinite;
    animation-timing-function: ease;
}

.hand2_group_animation {
    transform-origin: 335px 660px;
    animation-name: hand2-animation;
    animation-duration: 1s;
    animation-iteration-count: infinite;
    animation-timing-function: ease;
}

.head_group_animation {
    transform-origin: 200px 650px;
    animation-name: head-animation;
    animation-duration: 1s;
    animation-iteration-count: infinite;
    animation-timing-function: ease;
}

.background2 {
    transform: scale(0.32);
    left: -270px;
    top: 1100px;
}

.portal2{
    transform: scale(0.32);
    left: -530px;
    top: 350px;
}

.body2{
    transform: scale(0.32);
    left: -270px;
    top: 1100px;
}

.head2{
    transform: scale(0.32);
    left: -270px;
    top: 1100px;
}

.arm1{
    transform: scale(0.32);
    left: -270px;
    top: 1100px;
}

.arm2{
    transform: scale(0.32);
    left: -270px;
    top: 1100px;
}

.collar2{
    transform: scale(0.32);
    left: -270px;
    top: 1100px;
}

.portal2_animation{
    transform-origin: 770px 1090px;
    animation-name: portal-animation;
    animation-duration: 30s;
    animation-iteration-count: infinite;
    animation-timing-function: linear;
}

.body2_animation{
    transform-origin: 770px 1090px;
    animation-name: body2-animation;
    animation-duration: 1s;
    animation-iteration-count: infinite;
    animation-timing-function: linear;
}
"""

css_not_parsable = """
@keyframes full-body-animation {
    0% {
        transform: rotate(0deg) translateZ(-1.5px);
    }

    50% {
        transform: rotate(2deg) translateZ(-1.5px);
    }

    100%{
        transform: rotate(0deg) translateZ(-1.5px);
    }
}

@keyframes hand1-animation {
    0% {
        transform: rotate(0deg);
    }

    50% {
        transform: rotate(2deg);
    }
}

@keyframes hand2-animation {
    0% {
        transform: rotate(0deg);
    }

    50% {
        transform: rotate(-2deg);
    }
}

@keyframes head-animation {
    0% {
        transform: rotate(0deg);
    }

    50% {
        transform: rotate(-4deg);
    }
}
@keyframes portal-animation {
    0% {
        transform: rotate(0deg) scale(0.4);
    }

    100% {
        transform: rotate(-360deg) scale(0.4);
    }
}

@keyframes body2-animation {
    0% {
        transform: rotate(0deg) scale(0.32);
    }

    50% {
        transform: rotate(2deg) scale(0.32);
    }
    100%{
        transform: rotate(0deg) scale(0.32);
    }
}
"""
parcer = htmlparcing()
parcer.readHTML(f_html2)
print()

