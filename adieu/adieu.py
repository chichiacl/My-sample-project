import inflect

names = []
while True:
    try:
        names.append(input("Names: "))
    except EOFError:
        
