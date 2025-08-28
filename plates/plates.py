def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not s[0:2].isalpha():
        return False

    if len(s) not in [2,3,4,5,6]:
        return False

    if not s.isalnum():
        return False

    bnumber = False
    for n in s:
        if n.isdigit():
            if (int(n) == 0) and (bnumber == False):
                return False
            else:
                bnumber = True

    for n in s:
        if n.isdigit():
            number_index = s.find(n)
            inumber = s[number_index:]
            if not inumber.isdigit():
                return False
            
    return True

if __name__ == "__main__":
    main()

