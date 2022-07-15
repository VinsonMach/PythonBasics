# Vinson Mach 7/15/2022
# This program will print numbers from 1 to 100
# For multiples of 3, the program will print "Fizz" and "Buzz" for multiples of 5
# For multiples of both 3 and 5, the program will print "FizzBuzz"

if __name__ == '__main__':

    for i in range(1, 101):
        if (i % 3 == 0):
            if (i % 5 == 0):
                print("FizzBuzz")
            else:
                print("Fizz")
        elif (i % 5 == 0):
            print("Buzz")
        else:
            print(i)