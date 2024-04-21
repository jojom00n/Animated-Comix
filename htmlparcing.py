import cssutils as cssutils
from bs4 import *
from yattag import *

from ComixElement import initGroup, initElement, initImage
from ComixProject import InitComix


# Получаем данные из css строки
class htmlparcing():
    _init_comix = InitComix()


    def get_initComix(self):
        return self._init_comix

    def _initelement(self, index, layers):
        layer = layers[index]
        if "group" in layer["class"][1]:
            group = initGroup()
            group.set_name(layer["class"][1])
            if len(layer["class"]) == 3:
                group.set_AnimationID(layer["class"][2])
            for groupEl in layer.findAll("div"):
                index += 1
                group.get_Elements().append(self._initelement(index, layers))
            return group
        elif "img" in layer["class"][1]:
            img = initImage()
            img.set_name(layer["class"][1])
            if len(layer["class"]) == 3:
                img.set_AnimationID(layer["class"][2])
            img.set_image(layer.find('img')["src"][0])
            return img



    def readHTML(self, text):
        soup = BeautifulSoup(text, "html.parser")
        self._init_comix.set_name(soup.find('title').text) #Считываем имя инициализирующемуся комиксу
        layers = soup.findAll("div", {"class": "parallax-layer"})
        initelements = []
        for index in range(0, len(layers), 1):
            initelements.append(self._initelement(index, layers))
            print(len(initelements))
        self._init_comix.set_elements(initelements)

