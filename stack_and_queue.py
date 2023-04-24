# import regular expression module
import re

# Declare the empty Lists
stack = []
queue = []

def push(list, item):
    list.append(item)

def insert(list, item):
    list.insert(0, item)

def pop(list):
    if list:
        return list.pop()
    else:
        print("\nList is empty.\n")

def stack_or_queue_option():
    welcoming_message = "Hello, welcome to our app!"
    print(f"***{welcoming_message}***")
    print("For the Stack implementation press '1'.")
    print("For the Queue implementation press '2'.")

    while True:
        user_choice = input()
        if user_choice == '1' or user_choice =='2':
            break
        else:
            print("Not a valid selection. Please select again: ")
            continue

    user_choice = int(user_choice)      # Typecast the user's input from string to integer.

    if user_choice == 1:
        print("\nExcellent! You chose the Stack.")
    elif user_choice == 2:
        print("\nVery well! Queue it is then.")
    return user_choice

def print_menu_for_stack():
    print("1. Insert on top.")
    print("2. Get from top.")
    print("3. q/Q for Exit.")

def print_menu_for_queue():
    print("1. Insert at the end.")
    print("2. Get from start.")
    print("3. q/Q for Exit.")

def get_choice():
    return input("Please provide a choice: ")

def main():
    choice = 0
    num = 0
    out_num = 0
    QUEUE_OR_STACK_CHOICE = stack_or_queue_option()

    if QUEUE_OR_STACK_CHOICE == 1:
        user_chose_stack = True
    else:
        user_chose_stack = False

    while True:
        if user_chose_stack:
            print_menu_for_stack()
        else:
            print_menu_for_queue()
        
        choice = get_choice()

        if not choice:    # 0 or None
            continue
        
        if choice == 'q' or choice == 'Q':
            break
        
        pattern = r'^\d+$'
        match = re.match(pattern, choice)

        if not match:
            print("Error in choice. Type again.\n")
            continue

        choice = int(choice)

        match choice:
            case 1:
                num = input("Please insert a num: ")
                match = re.match(pattern, num)

                if not match:
                    print("Error in number input.")
                    continue
                
                num = int(num)    # Typecast the user's input from string to integer.
                if user_chose_stack:
                    push(stack, num)
                    print(f"\n{num} was inserted successfully.\n")
                else:
                    insert(stack, num)
                    print(f"\n{num} was inserted successfully.\n")

            case 2:
                out_num = pop(stack)
                if out_num != None:
                    print("\nYou extracted:", out_num, "\n")
                    
            case _:
                print("Not a valid choice.\n")

    print("GoodBye!")

if __name__ == '__main__':
    main()
