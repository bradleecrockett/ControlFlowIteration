import os
def main():
    # Warm Up

    print('\nWARM UP\n')

    if (2/3 + 1 == 5 / 3):
        print('All things are balanced.')
    else:
        print('Things are out of whack.')

    ########################

    selection = menu()
    while (selection != 'exit'):
        if (selection == 'a'):
            example_A()
        elif (selection == 'b'):
            example_B()
        elif (selection == 'c'):
            example_C()
        elif (selection == 'd'):
            example_D()
        elif (selection == 'e'):
            example_E()
        elif (selection == 'f'):
            example_F()
        elif (selection == 'g'):
            example_G()
        elif (selection == 'h'):
            example_H()
        elif (selection == 'i'):
            example_I()
        elif (selection == 'j'):
            example_J()
        elif (selection == 'k'):
            example_K()
        elif(selection == 'l'):
            example_L()
        elif (selection == 'm'):
            example_M()
        elif (selection == 'exit'):
            break
        else:
            print("Invalid Selection")
        
        selection = menu()
        clear() # clear the screen


def example_A():
    print("\nEXAMPLE A\n")
    x = 0.0037 / 100
    # These numbers look equal!
    y = 0.000037
    # But they aren't exactly equal!
    print("x = ", x)
    print("y = ", y)
    if (x == y):
        print("Equal!")
    else:
        print("Unequal!")

    # end of example_A


def example_B():
    print("\nEXAMPLE B\n")
    x = 0.0037 / 100
    # These numbers look equal!
    y = 0.000037
    # But they aren't exactly equal!
    print("x = ", x)
    print("y = ", y)
    # ... But they are approximately equal
    # (to five decimal places)!
    if (round(x, 5) == round(y, 5)):
        print("Approximately equal!")
    else:
        print("Not approximately equal!")

    # End of example_B


def example_C():
    print("\nEXAMPLE C\n")
    # This for loop prints 0 - 9
    for i in range(10): # 
        print(i)

    # end of example_C


def example_D():
    print("\nEXAMPLE D\n")
    # This for loop only prints 0 through 4.
    for i in range(10):  # 
        if (i == 5):
            break
        print(i)

    # end of example_D


def example_E():
    print("\nEXAMPLE E\n")
    # we skip back to the top of the for loop
    for i in range(10):
        if (i == 5):
            continue
        print(i)
    # end of example_E


def example_F():
    print("\nEXAMPLE F\n")
    x = 0
    while (x < 10):
        print(x)
        x += 1 # Adds 1 to the value of x 
    print("after the loop x is: ", x)
    # end of example_F


def example_G():
    print("\nEXAMPLE G\n")
    while True:
        print("That was dumb.")
        # control + c is the keyboard interrupt to stop the madness.
    # end of example_G



def example_H():
    print("\nEXAMPLE H\n")
    while True: # infinite loop
        number = int(input("Enter any number but not 3: "))
        if (number == 3):
            print("Goodbye!")
            break
        # The next line is NOT reached if the condition is true
        print("Try again!")
    # end of example_H


def example_I():
    print("\nEXAMPLE I\n")
    while (True):
        try:
            num = int(input("Enter a positive 'number': "))
            if (num < 1):
                continue
            else:
                break
        except ValueError:
            print("That was not a number.")
            continue
    print("The positive number is: ", num)
    # end of example_I


def example_J():
    print("\nEXAMPLE J\n")
    size = 5
    for a in range(size):  # 
        for b in range(size):  # 
            print(a, b)
    # end of example_J


def example_K():
    print("\nEXAMPLE K\n")
    total = 0
    for c in range(5):
        d = 1
        while d <= c:
            total = total + d
            d += 1

    print(total)
    # end of example_K


def example_L():
    print("\nEXAMPLE L\n")
    power2 = 1
    while (power2 != 20):  # 
        print(power2)
        power2 *= 2
		
    # end of example_L

def example_M():
    print("\nEXAMPLE M\n")
    power2 = 1
    while (power2 < 20):  # 
        print(power2)
        power2 *= 2
    # end of example_M

def clear():
    # for windows
    if os.name == 'nt':
        os.system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        os.system('clear')# Linux operating systems

def menu():
    m = '\nMenu - Select the Example that you want to test by letter\n-----------------------\na-Example A\nb-Example B\nc-Example C\nd-Example D\ne-Example E\nf-Example F\ng-Example G (Don\'t do it)\nh-Example H\ni-Example I\nj-Example J\nk-Example K\nl-Example L\nexit - to quit\n'

    s = input(m)
    return s.lower()


if __name__ == "__main__":
    main()
