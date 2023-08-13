import os
from enum import Enum


class Tags(Enum):
    div = "div"
    h1 = "h1"
    h2 = "h2"
    h3 = "h3"
    h4 = "h4"
    h5 = "h5"
    h6 = "h6"
    p = "p"
    nav = "nav"


class Element:
    def __init__(self, tagName: Tags, value: str):
        self.tagName = tagName.name
        self.value = value

    def setValue(self, v):
        self.value = v

    def concatValue(self, v):
        self.value += v

    def newChild(self, child):
        self.concatValue(child.getElement())

    def getValue(self):
        return self.value

    def clearValue(self):
        self.value = ""

    def getElement(self):
        return "<" + self.tagName + ">" + self.value + "</" + self.tagName + ">"


class Page:
    def __init__(self, name: str, element: Element):
        self.name = name
        self.element = element

    def compile(self):
        f = open(os.getcwd() + "\\build\\" + self.name + ".html", "w")
        f.write(self.element.getElement())
