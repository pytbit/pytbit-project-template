from pytbit_modules.pytbit import Element, Tags, Page
import sys


e = Element(Tags.h1, "about")
p = Page("about", e)
p.compile()
