import inflect

names = []
while True:
    try:
        names.append(input("Names: "))
    except EOFError:
        print(f"Adieu, adieu to {p.join(names)}")
        break

