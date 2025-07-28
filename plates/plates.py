def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(p):
       if 2 <= len(s) > 6: # correct length
        return False

       if not s[:2].isalpha(): # first 2 chars letter
            return False

        if s.isalnum(): # no puncuation
           return True
        else:
           return False


main()
