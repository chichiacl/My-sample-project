def convert(string):
    cstring = string.replace(":)","🙂")
    cstring = cstring.replace(":(","🙁")
    return cstring

def main():
    phrase = input()
    print(convert(phrase))

main()



