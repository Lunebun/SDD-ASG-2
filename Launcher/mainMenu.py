def check_user_int(input_check):
    try:
        outcome = int(input_check)
        return outcome
    except: 
        return -1

def load_saved_game():

    return

def high_score():

    return

def start_game():

    return 

def print_menu(print_content, menu_level):
    for choice, menu_selection in enumerate(print_content, start = 1):
        print("{}. {}".format(choice,menu_selection))

    if menu_level == True:
        print("\n0. Exit")
    else:
        print("0. Exit to main menu")

    user_input = check_user_int(input("\nYour Choice? "))
    return user_input

# This functions calls the main menu and depending on the choice of the user
# it then runs the corresponding function
def main_menu():
    menu_list = ["Start new game","Load saved game","Show high scores","Choose city size","Choose building pool"]
    building_list = ["HSE","BCH","SHP","FAC","HWY"]
    new_turn = 1
    city_list =[[" "," "," "," "],[" "," "," "," "],[" "," "," "," "],[" "," "," "," "]]

    while True:    
        print("\nWelcome to Simp City!")
        print("-"*21)     
        user_selection = print_menu(menu_list, True)
        if user_selection == 1:
            start_game()
        elif user_selection == 2:
            load_saved_game() 
        elif user_selection == 3:
            high_score() 
        elif user_selection == 0:
            exit()
        else:
            print("You have entered an invalid selection!\nThe error code is {}. \nPlease try again.\n".format(user_selection))
      
# This just loops the entire code
main_menu()