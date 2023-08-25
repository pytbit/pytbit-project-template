from pytbit_modules.pytbit import Element, Tags, Page


e = Element(Tags.h1, "home")
p = Page("home", e)
p.compile()
