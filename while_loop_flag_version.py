import random

def get_starting_number():
    return int(input("How many bottles do you want to start with?"))

def sing(number):
    keep_singing = True
    while keep_singing:
        if number == 1:
            print(f"{number} bottle of beer on the wall, {number} bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall.")
            keep_singing = False
        else:
            print(f"{number} bottles of beer on the wall, {number} bottles of beer.")
            new_num = number - 1
            if new_num == 1:
                print(f"Take one down, pass it around, {new_num} bottle of beer on the wall.")
            else:
                print(f"Take one down, pass it around, {new_num} bottles of beer on the wall.")
            number -= 1