def main():
    string = input("Greeting: ")
    amount = value(string)
    print(f"${amount}")

def value(greeting):
    greeting = string.strip().split()
    greeting = greeting[0]
    if greeting.lower() == "hello" or greeting.lower() == "hello,":
        return 0
    elif greeting[0].lower() == 'h':
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
