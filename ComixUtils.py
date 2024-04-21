class ComixLocation:
    _x = 0;
    _y = 0;

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def set_x(self, x):
        self._x=x

    def set_y(self, y):
        self._y=y


class ElementTransform:
    _zaxis = 0
    _rotation = 0
    _scale = 1

    def get_zaxis(self):
        return self._zaxis

    def get_rotation(self):
        return self._rotation

    def get_scale(self):
        return self._scale