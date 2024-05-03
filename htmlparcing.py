import cssutils
from bs4 import *
from cssutils import *
from cssutils.css import CSSStyleDeclaration
from yattag import *

from ComixElement import initGroup, initElement, initImage
from ComixProject import InitComix, ComixProject


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
        self._init_comix.set_elements(initelements)


    def readCSS(self, text):
        parser = cssutils.parseString(text).cssRules
        styles = {}
        for rule in parser:
            if rule.selectorText[0] == ".":
                print(rule.selectorText[1:], "/", rule.style.getPropertyValue("background-color"))
                styles[rule.selectorText[1:]] = rule.style
        if "body" in styles.keys():
            self._init_comix.set_backgrOutColor(styles["body"].getPropertyValue("background-color"))
        if "parallax" in styles.keys():
            self._init_comix.set_backgrInColor(styles["parallax"].getPropertyValue("background-color"))
#           self._init_comix.set_perspective(rule.style.getPropertyValue("perspective"))
#       if "container" in styles.keys():
#           self._init_comix.set_width(rule.style.getPropertyValue("max-width"))
#           break
        for element in self._init_comix.get_initElements():
            if styles[element.get_name()].getPropertyValue("top") != "":
                element.set_top(styles[element.get_name()].getPropertyValue("top"))
            if styles[element.get_name()].getPropertyValue("left") != "":
                element.set_left(styles[element.get_name()].getPropertyValue("left"))
            if styles[element.get_name()].getPropertyValue("transform") != "":
                element.set_transformation(styles[element.get_name()].getPropertyValue("transform"))

    def SetupComProject(self, comix):
        comix.set_name(self._init_comix.get_name())
        comix.set_backgrOutColor(self._init_comix.get_backgrOutColor())
        comix.set_backgrInColor(self._init_comix.get_backgrInColor())
        return comix