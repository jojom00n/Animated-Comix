from ComixUtils import*
from ComixAnimation import*

class ComixElement:
    _left = 0
    _right = 0
    _top = 0
    _bottom = 0
    _transformation = ElementTransform()
    _anchorPoint = ComixLocation()
    _tag = ""
    _content = []
    _name = ""
    _animationID = ""
    _animation = Animation(_animationID)

    def __init__(self, tag=""):
        self._tag = tag

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
    
    def get_tag(self):
        return self._tag
    
    def get_content(self):
        return self._content

    def get_name(self):
        return self._name

    def get_animationId(self):
        return self._animationID
    
    def print(self):
        print(self.get_tag())




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

    def set_tag(self, tag):
        self._tag = tag

    def set_content(self, content):
        self._content = content

    def set_name(self, name):
        self._name = name

    def set_animationId(self, animationid):
        self._animationID = animationid

    def append(self, new_content_elem):
        self._content.append(new_content_elem)


class ImgElement(ComixElement):
    _tag = "img"
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