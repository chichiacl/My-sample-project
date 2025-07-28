def main():
    n = convert(input("What time is it? ")) # 7:30 = 7.5
    if 7<=n<8:
        print("breakfast time")
    elif 12<n<=13:
        print("lunch time")
    elif 18<n<19:
        print("dinner time")
    else:
        print("")

def convert(time):
    hours, minutes = time.split(":") # hours = 7 minutes = 30
    total_hours = float(hours) + (float(minutes)/60) # 7 + 30/60 = 7.5 hours
    return total_hours


if __name__ == "__main__":
    main()
