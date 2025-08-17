def main():
    string = input("Greeting: ")
    amount = value(string)
    print(f"${amount}")

def value(greeting):
    result = greeting.strip().split()
    result = result[0]
    if result.lower() == "hello" or result.lower() == "hello," or result.lower() == "hello!":
        return 0
    elif result[0].lower() == 'h':
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
