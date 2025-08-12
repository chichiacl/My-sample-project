from pyfiglet import Figlet
import random
import sys

figlet = Figlet() # object
figlet.getFonts() # list of all the fonts
if len(sys.argv) == 1:
    #zero, choose random font
elif len(sys.argv) == 3:
    # @ promt user chooses font
else:
    ...


"""
figlet.setFont(font=f)
print(figlet.renderText(s))
"""
