from pyfiglet import Figlet
import random
import sys

figlet = Figlet()
figlet.getFonts() # list of all the fonts
"""
figlet.setFont(font=f)
print(figlet.renderText(s))
"""
print(Figlet().getFonts())
