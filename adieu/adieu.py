import inflect

names = []
while True:
    try:
        names += input("Names: ")
    except EOFError:
        ...
