from pytbit_modules.pytbit import Element, Tags, Page


e = Element(Tags.h1, "help")
p = Page("help", e)
p.compile()
