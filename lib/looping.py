#!/usr/bin/env python3

def happy_new_year():
    number = 10
    # code goes here!
    while number >= 1:
        print(number)
        number -= 1
    print("Happy New Year!")
    pass

def square_integers(int_list):
    # code goes here!
    squared_intergers = []
    for num in int_list:
        squared_intergers.append(num**2)
    print(int_list,squared_intergers)
    return squared_intergers

    pass
square_integers([1,2,3,4,5])
def fizzbuzz():
    # code goes here!
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
        
    pass
fizzbuzz()