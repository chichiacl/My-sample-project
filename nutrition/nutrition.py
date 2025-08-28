items = {"apple": 130,
         "avocado":50 ,
         "banana":110,
         "cantaloupe":50,
         "grapefruit":90,
         "grapes":80,
         "honeydew melon":50,
         "kiwifruit":90,
         "lemon":15,
         "lime":20,
         "nectarine":60,
         "orange":80,
         "peach":60,
         "pear":100,
         "pineapple":50,
         "plums":70,
         "strawberries":50,
         "sweet cherries":100,
         "tangerine":50,
         "Watermelon":80
         }
item = input("Item: ")
if item.lower().strip() in items:
    print("Calories:",items[item.lower().strip()])


