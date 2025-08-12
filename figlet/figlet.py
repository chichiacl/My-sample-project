from pyfiglet import Figlet
import random
import sys

figlet = Figlet() # object
font_List = figlet.getFonts() # list of all the fonts

if len(sys.argv) == 1:
    #zero, choose random font
    s = input("Input: ")
    f = random.choice(font_List)
    figlet.setFont(font=f)
    print("Output:")
    print(figlet.renderText(s))
elif len(sys.argv) == 3:
    
    # @ promt user chooses font
else:
    ...


"""
figlet.setFont(font=f)
print(figlet.renderText(s))
"""
