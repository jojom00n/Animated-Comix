from htmlparcing import *

from ComixProject import *

f_css = """

.body {
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

.img_background_frame_1 {
    transform: scale(0.36) translateZ(-1.1px);
    top: 10px;
    left: -230px;
}

.group_body_frame_1 {
    top: 110px;
    transform: scale(0.36);
    left: -230px;
}

.img_body_frame_1 {
    transform: scale(0.36) translateZ(-1px);
    top: 320px;
    left: -230px;
}

.group_lefthand_frame_1 {
    transform-origin: 240px 600px;
    top: 3210px;
    transform: scale(0.36);
    left: -230px;
}

.img_lefthand_one_frame_1 {
    top: 3240px;
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

f_html2 = """
<!doctype html>
<html>

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="/style.css">
    <title>Ученый</title> <!--Название комикса-->
</head>

<body>
    <div class="container"> <!--Выравнивающий контейнер-->
        <div class="parallax"> <!--Контейнер параллакса-->
            <div class="parallax-layer img_background_frame_1"> <!--Элемент комикса (В данном случае изображение)-->
                <img src="imgs/img_background_frame_1.png" /> <!--Путь к изображению-->
            </div>
            <div class="parallax-layer group_body_frame_1 group_body_frame_1_animation"> <!--Элемент комикса (В данном случае группа элементов)-->
                <div class="parallax-layer img_body_frame_1"> <!--Элемент группы-->
                    <img src="imgs/img_body_frame_1.png" />
                </div>
                <div class="parallax-layer group_lefthand_frame_1 lefthand_one_frame_1_animation"> <!--Элемент группы (группа в группе тоже может быть)-->
                    <div class="parallax-layer img_lefthand_one_frame_1">
                        <img src="imgs/img_lefthand_one_frame_1.png" />
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>

</html>
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

parcer = htmlparcing()
parcer.read_html(f_html2)
parcer.read_css(f_css)
project = ComixProject()
com = parcer.setup_com_project(project)
print(com)

