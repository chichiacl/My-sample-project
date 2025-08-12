from pyfiglet import Figlet
import random
import sys

figlet = Figlet() # object
font_List = figlet.getFonts() # list of all the fonts

if len(sys.argv) == 1:
    #zero, choose random font
    s = input("Input: ")
    f = random.choice(font_List)
    figlet.setFont(font = f)
    print("Output:")
    print(figlet.renderText(s))
elif len(sys.argv) == 3:
    # @ promt user chooses font
    s = input("Input: ")
    if sys.argv[1] not in ["-f","--font"] :
        print("Invalid usage")
        sys.exit
    if sys.argv[2] not in font_List:
        print("Invalid usage")
        sys.exit
    figlet.setFont(font = sys.argv[2])
    print("Output:")
    print(figlet.renderText(s))
else:
    print("Invalid usage")

