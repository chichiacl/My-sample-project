def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(p):
       if len(p) < 2 or len(p) > 6: # correct length
        return False

       if not p[:2].isalpha(): # first 2 chars letter
            return False

        if not p.isalnum(): # no puncuation
           return False

       for i in range(len(p))


main()
