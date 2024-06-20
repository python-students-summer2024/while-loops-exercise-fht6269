import random

def get_starting_number():
    return random.randint(1,99)

def sing(number):
    for i in range(number, 0, -1):
        if i == 1:
            print(f"{i} bottle of beer on the wall, {i} bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall.")
        else:
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            new_num = i - 1
            if new_num == 1:
                print(f"Take one down, pass it around, {new_num} bottle of beer on the wall.")
            else:
                print(f"Take one down, pass it around, {new_num} bottles of beer on the wall.")