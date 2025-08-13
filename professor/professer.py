import random


def main():
for n in range(10):

     integers = generate_integer(get_level()) # (x,y) hopefully 10 (2,8)
     x = integers[0] # 2
     y = integers[1] # 8
     sum = x + y #10
     ipoint = 0
     icount = 0

     while True:
          try:
              response = int(input(str(x)+" + "+str(y)+" = ")) # 2 + 8 = 10
              if response == sum:    # 10 == 10
                  ipoint = ipoint + 1
                  break
              elif icount == 3 :     # 0 == 3
                  print(f"{x} + {y} = {sum}")
                  break
              else:
                  icount = icount + 1 # 1
                  continue
            except V
#score = all points


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n in [1,2,3]:
                return n
            else:
                continue
        except ValueError:
            continue

def generate_integer(level):
    if level == 1 :
        x = random.randint(0,9)
        y = random.randint(0,9)

    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)

    elif level == 3:
        x = random.randint(100,999)
        y = random.randint(100,999)
    else:
        raise ValueError
    return (x,y)


if __name__ == "__main__":
    main()
