from pytbit_modules.pytbit import Element, Tags, Page
import sys


e = Element(Tags.h1, "help")
p = Page("help", e)
p.compile()
