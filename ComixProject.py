class ComixProject:
    _name = ""
    _items = []
    _width = 0
    _backgrOutColor = ""
    _backgrInColor = ""
    _perspective = 0

        
    
    def setParam(self, name, items, width, backgrColOut, backgrColIn, perspect):
        self._name = name
        self._items = items
        self._width = width
        self._backgrOutColor = backgrColOut
        self._backgrInColor = backgrColIn
        self._perspective = perspect


    def appendElement(self, element):
        self._items.append(element)

    def get_name(self):
        return self._name

    def get_items(self):
        return self._items
    
    def get_width(self):
        return self._width
    
    def get_backgrOutColor(self):
        return self._backgrOutColor
    
    def get_backgrInColor(self):
        return self._backgrInColor
    
    def get_perspective(self):
        return self._perspective
    


    def set_name(self, name):
        self._name = name

    def set_items(self, items):
        self._items = items
    
    def set_width(self, width):
        self._width = width
    
    def set_backgrOutColor(self, color):
        self._backgrOutColor = color
    
    def set_backgrInColor(self, color):
        self._backgrInColor = color
    
    def set_perspective(self, pers):
        self._perspective = pers


class InitComix():
    _name = "None"
    _initElements = []
    _backgrOutColor = "Black"
    _backgrInColor = "Black"
    _width = 500
    _perspective = 10

    def get_name(self):
        return self._name

    def get_initElements(self):
        return self._initElements

    def set_name(self, name):
        self._name = name

    def set_elements(self, elements):
        self._initElements = elements

    def get_backgrOutColor(self):
        return self._backgrOutColor

    def get_backgrInColor(self):
        return self._backgrInColor

    def set_backgrOutColor(self, color): #Получаем из body
        self._backgrOutColor = color

    def set_backgrInColor(self, color): #Получаем из parallax
        self._backgrInColor = color

    def get_width(self):
        return self._width

    def set_width(self, width): #Получаем из container
        self._width = width

    def get_perspective(self):
        return self._perspective
    def set_perspective(self, pers): #Получаем из parallax
        self._perspective = pers