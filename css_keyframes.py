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

def keyframe(test_str):
    keyframes = {}
    css_str = test_str.replace('{', '').replace('}', '').replace('\n', '').strip()
    animations = css_str.split(';')
    animations[0] = animations[0].split(" ",1)
    name = animations[0][0]
    animations[0] = animations[0].pop(-1)
    animations=animations[:-1]
    list_key = []
    list_value = []
    for animation in animations:
        dict_values = {}
        key = animation.split('%')
        if key[0].isdigit():
            key[0]=int(key[0])
        props = key[1].split(": ")
        props[1] = props[1].split()
        props[1][0] = props[1][0].replace('(','').replace(')','')
        if len(props[1]) == 2:
            props[1][1] = props[1][1].replace('(','').replace(')','')
        if props[1][0][:3] == 'rot':
            props[1][0] = props[1][0][6:-3]
            props[1][0] = int(props[1][0])
        if len(props[1]) == 2:
            if props[1][1][:3] == 'sca':
                props[1][1] = props[1][1][5:]
                props[1][1] = float(props[1][1])
        dict_values[props[0]] = props[1]
        key[1] = dict_values
        list_key.append(key[0])
        list_value.append(key[1])
    dict_levels = dict(zip(list_key, list_value))
    return [name, dict_levels]
def get_css_keyframes(example_css):
    css_list = example_css.split("@keyframes", 1)
    keyframes_list = css_list[1].replace('\n', '')
    keyframes_list = keyframes_list.split("@keyframes")
    keyframes = {}
    for frame in keyframes_list:
        new_list = keyframe(frame)
        keyframes[new_list[0]] = new_list[1]
    return keyframes
print(get_css_keyframes(f_css))