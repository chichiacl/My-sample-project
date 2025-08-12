import inflect

p = inflect.engine()
names = []
while True:
    try:
        names.append(input("Names:"))
    except EOFError:
        print(f"Adieu, adieu to {p.join((names),sep=",")}")
        break

