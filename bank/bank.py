string = input("Greeting: ")
greeting = string.strip().split()
greeting = greeting[0]
if greeting.lower() == "hello" or greeting.lower() == "hello,":
    print("$0")
elif greeting[0].lower() == 'h':
    print("$20")
else:
    print("$100")


