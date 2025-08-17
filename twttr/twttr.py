def main():
    phrase = input("Input: ")
    result = shorten(phrase)
    print("Output:", result)

def shorten(word):
    output = ""
    for v in word:
        if v in ["A","E","I","O","U","a","e","i","o","u"]:
            None
        else:
            output = output + v
    return output

if __name__ == "__main__":
    main()
