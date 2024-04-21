from ComixUtils import*

class ComixElement:
    _left = 0
    _right = 0
    _top = 0
    _bottom = 0
    _transformation = ElementTransform()
    _anchorPoint = ComixLocation()
    _name = ""
    _animationID = ""

    def get_left(self):
        return self._left

    def get_right(self):
        return self._right

    def get_top(self):
        return self._top

    def get_bottom(self):
        return self._bottom

    def get_transforamtion(self):
        return self._transformation

    def get_anchorPoint(self):
        return self._anchorPoint

    def get_name(self):
        return self._name

    def get_animationId(self):
        return self._animationID




    def set_left(self, left):
        self._left = left

    def set_right(self , right):
        self._right = right

    def set_top(self, top):
        self._top = top

    def set_bottom(self, bottom):
        self._bottom = bottom

    def set_transforamtion(self, trans):
        self._transformation = trans

    def set_anchorPoint(self, anchorpoint):
        self._anchorPoint = anchorpoint

    def set_name(self, name):
        self._name = name

    def set_animationId(self, animationid):
        self._animationID = animationid


class ImgElement(ComixElement):
    _imagelocation = ""

    def getimageloc(self):
        return self._imagelocation

    def __init__(self, imageloc):
        self._imagelocation = imageloc


class GroupElement(ComixElement):
    _elements = []

    def getimageloc(self):
        return self._elements

    def __init__(self, elements):
        self._elements = elements


class initElement():
    _name = ""
    _AnimationID = ""

    def get_name(self):
        return self._name

    def get_AnimationID(self):
        return self._AnimationID

    def set_name(self, nam):
        self._name = nam
    def set_AnimationID(self, Animation):
        self._AnimationID = Animation


class initImage(initElement):
    _imageloc = ""

    def get_image(self):
        return self._imageloc

    def set_image(self, image):
        self._imageloc = image


class initGroup(initElement):
    _elements = []

    def get_Elements(self):
        return self._elements

    def set_Elements(self, elements):
        self._elements = elements

    def add_Element(self, element):
        self._elements.append(element)