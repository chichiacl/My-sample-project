months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    d = input("Date: ").strip()
    if d.count("/") == 2 :
        date = d.split("/") # 23, 6, 1912 1/50/2000
        if  date[0].isnumeric():  #
            if int(date[0]) <= 12:
                if int(date[1]) <= 31:
                    print(f"{int(date[2])}-{int(date[0]):02}-{int(date[1]):02}")
                    break
    elif d.split(" ")[0] in months:
        date = d.split(" ") # December 80, 1980
        if int(date[1].split(",")[0]) <= 31:
            if "," in date[1]:
                print(f"{int(date[2])}-{months.index(date[0])+1:02}-{int(date[1].split(",")[0]):02}")
                break



