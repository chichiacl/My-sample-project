grocery_dict = {}
while True:
    try:
        item = input("")
        if item in grocery_dict:
            grocery_dict[item] += 1
        else:
            grocery_dict[item] = 1
    except EOFError:
        print()
        sorted_list = sorted(grocery_dict.items())
        sorted_dict = dict(sorted_list)
        for i in sorted_dict:
             print(f"{sorted_dict[i]} {i.upper()}")
        break


