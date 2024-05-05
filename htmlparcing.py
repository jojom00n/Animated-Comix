import cssutils
import re
from bs4 import *

from ComixElement import initGroup, initImage, GroupElement, ImgElement
from ComixProject import InitComix
from ComixUtils import ElementTransform, ComixLocation


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
                group.set_animationId(layer["class"][2])
            for groupEl in layer.findAll("div"):
                index += 1
                group.get_Elements().append(self._initelement(index, layers))
            return group
        elif "img" in layer["class"][1]:
            img = initImage()
            img.set_name(layer["class"][1])
            if len(layer["class"]) == 3:
                img.set_animationId(layer["class"][2])
            img.set_image(layer.find('img')["src"][0])
            return img

    def read_html(self, text):
        soup = BeautifulSoup(text, "html.parser")
        self._init_comix.set_name(soup.find('title').text)  # Считываем имя инициализирующемуся комиксу
        layers = soup.findAll("div", {"class": "parallax-layer"})
        initelements = []
        for index in range(0, len(layers), 1):
            initelements.append(self._initelement(index, layers))
        self._init_comix.set_elements(initelements)


    def read_css(self, text):
        parser = cssutils.parseString(text).cssRules
        styles = {}
        for rule in parser:
            if rule.selectorText[0] == ".":
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
            if not element.get_name() in styles.keys(): break
            if styles[element.get_name()].getPropertyValue("top") != "":
                element.set_top(styles[element.get_name()].getPropertyValue("top"))
            if styles[element.get_name()].getPropertyValue("left") != "":
                element.set_left(styles[element.get_name()].getPropertyValue("left"))
            if styles[element.get_name()].getPropertyValue("transform") != "":
                element.set_transformation(styles[element.get_name()].getPropertyValue("transform"))
            if styles[element.get_name()].getPropertyValue("transform-origin") != "":
                element.set_anchorPoint(styles[element.get_name()].getPropertyValue("transform-origin"))

    def setup_com_project(self, comix):
        comix.set_name(self._init_comix.get_name())
        comix.set_backgrOutColor(self._init_comix.get_backgrOutColor())
        comix.set_backgrInColor(self._init_comix.get_backgrInColor())
        for element in self._init_comix.get_initElements():
            comix.appendElement(self._setup_element(element))
        return comix

    def _setup_element(self, inel):
        if isinstance(inel, initGroup):
            newel = GroupElement()
            newel.set_name(inel.get_name())
            newel.set_animationId(inel.get_name())
            newel.set_top(int(inel.get_top()[:-2]))
            newel.set_left(int(inel.get_left()[:-2]))
            newel.set_transformation(self._init_transorm(inel.get_transformation()))
            newel.set_anchorPoint(self._init_loc(inel.get_anchorPoint()))
            return newel
        else:
            newel = ImgElement()
            newel.set_name(inel.get_name())
            newel.set_animationId(inel.get_name())
            newel.set_top(int(inel.get_top()[:-2]))
            newel.set_left(int(inel.get_left()[:-2]))
            newel.set_transformation(self._init_transorm(inel.get_transformation()))
            newel.set_anchorPoint(self._init_loc(inel.get_anchorPoint()))
            return newel

    def _init_transorm(self, trans):
        tr = ElementTransform()
        strs = trans.split()
        for st in strs:
            if "translateZ" in st: tr.set_zaxis(float(re.findall(r'\(.*?\)', st)[0][1:-1][:-2]))
            if "scale" in st: tr.set_scale(float(re.findall(r'\(.*?\)', st)[0][1:-1]))
            if "rotate" in st: tr.set_rotation(float(re.findall(r'\(.*?\)', st)[0][1:-1][:-3]))
        return tr

    def _init_loc(self, loc):
        l = ComixLocation()
        strs = loc.split()
        if len(strs) == 2:
            l.set_x(int(strs[0][:-2]))
            l.set_y(int(strs[1][:-2]))
        return l