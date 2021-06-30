from DataCapture import DataCapture

import os


### FUNCTIONS ###

def display_title_bar():
              
    print("**********************************************")
    print("***  Welcome to the system  ***")
    print("**********************************************")

def validate_positive_integer(value):
    while value < 0:
        value = int(input("Sorry, the value should be greater or equal than 0, please insert a new value. \n"))
    return value
    
def start_game():
    """ Set up a loop where users can choose what they'd like to do. """
    choice = ''
    display_title_bar()
    searching = False
    stats = None
    capture = DataCapture()
    while choice != 'q':    
        
        """Let users know what they can do."""
        if searching == False:
            print("\n[1] Add new value to the system.")
            print("[2] Start searching.")
        else:
            print("\n[3] Less than.")
            print("[4] Greater than.")
            print("[5] Between.")

        print("[test] Fast test.")
        print("[q] Quit.")
        
        choice = input("What would you like to do? ")
        
        if choice == '1' and not searching:
            value = int(input("Give me the new value. \n"))
            value = validate_positive_integer(value)
            # while value < 0:
            #     value = int(input("Sorry, the value should be greater or equal than 0, please insert a new value. \n"))
            capture.add(value)
        elif choice == '2' and not searching:
            searching = True
            stats = capture.build_stats()
        elif choice == "3":
            value = int(input("Give me the value to search how many values are less than it. \n"))
            value = validate_positive_integer(value)
            print(f"The values inside the array less than {value} are {stats.less(value)}")
        elif choice == "4":
            value = int(input("Give me the value to search how many values are greater than it. \n"))
            value = validate_positive_integer(value)
            print(f"The values inside the array greater than {value} are {stats.greater(value)}")
        elif choice == "5":
            value_one = int(input("Give me the first value to search. \n"))
            value_one = validate_positive_integer(value_one)
            value_two = int(input("Give me the first value to search. \n"))
            value_two = validate_positive_integer(value_two)
            while value_one > value_two:
                value_one = int(input("The first value should be less than the second, please give me again the first value. \n"))
                value_one = validate_positive_integer(value_one)
                value_two = int(input("Give me the second value again. \n"))
                value_two = validate_positive_integer(value_two)
            print(f"The values inside the array between {value_one} and {value_two} are {stats.between(value_one, value_two)}")
        elif choice == 'test':
            fast_test()
        elif choice == 'q':
            print("\nThanks for playing. Bye.")
        else:
            print("\nI didn't understand that choice.\n")

def fast_test():
    capture = DataCapture()
    capture.add(3)
    capture.add(9)
    capture.add(3)
    capture.add(4)
    capture.add(6)
    stats = capture.build_stats()
    print("The values inside the array less than 4 are ", stats.less(4))
    print("The values inside the array between 3 and 6 ", stats.between(3, 6))
    print("The values inside the array less greter 4 are ", stats.greater(4))
    # print(stats.between(3, 6))
    # print(stats.greater(4))


if __name__ == "__main__":
    # fast_test()
    start_game()