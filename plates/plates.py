def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(p):
    if two_letter(p) == True and 4 <= len(p) <= 6 and number(p) :
        return True
    else:
        return False

def two_letter(s):
    s[0:2].isalpha()

def number(n):
    








main()
