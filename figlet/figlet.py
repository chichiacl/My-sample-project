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
    if (sys.argv[1] != "-f") or (sys.argv[1] != "--font") :
        print("Invalid usage")
        sys.exit
    if sys.argv[2] not in font_list:
        print("Invalid usage")
        sys.exit
    


"""
figlet.setFont(font=f)
print(figlet.renderText(s))
"""
