from pytbit_modules.pytbit import Element, Tags, Page


e = Element(Tags.h1, "about")
p = Page("about", e)
p.compile()
