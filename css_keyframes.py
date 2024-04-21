test_str = "@keyframes portal-animation {0% {transform: rotate(0deg) scale(0.4);}100% {transform: rotate(-360deg) scale(0.4);}}"
def get_css_keyframes(test_str):
    keyframes = {}
    css_str = test_str.replace('@keyframes ', '').replace('{', '').replace('}', '').strip()
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
        props[1][1] = props[1][1].replace('(','').replace(')','')
        if props[1][0][:3] == 'rot':
            props[1][0] = props[1][0][6:-3]
            props[1][0] = int(props[1][0])
        if props[1][1][:3] == 'sca':
            props[1][1] = props[1][1][5:]
            props[1][1] = float(props[1][1])
        dict_values[props[0]] = props[1]
        key[1] = dict_values
        list_key.append(key[0])
        list_value.append(key[1])
    dict_levels = dict(zip(list_key, list_value))
    keyframes[name] = dict_levels
    return keyframes