import random

#check left for a building, return true if building is found
def check_left(city_allignment, assigned_row, assigned_col):
    try:
        if len(city_allignment[assigned_row][assigned_col-1]) > 1:
            return True
        else:
            return False
    except: 
       return False

#check top for a building, return true if building is found
def check_top(city_allignment, assigned_row, assigned_col):
    try:
        if len(city_allignment[assigned_row-1][assigned_col]) > 1:
            return True
        else:
            return False
    except:
        return False

#check right for a building, return true if building is found
def check_right(city_allignment, assigned_row, assigned_col):
    try:
        if len(city_allignment[assigned_row][assigned_col+1]) > 1:
            return True
        else:
            return False
    except:
        return False

#check bottom for a building, return true if building is found
def check_bottom(city_allignment, assigned_row, assigned_col):
    try:
        if len(city_allignment[assigned_row+1][assigned_col]) > 1:
            return True
        else:
            return False
    except:
        return False

# This function validates User input using try and except
# Try is converting the input into integer and returning it
# Otherwise except is ran and an error code of -1 is used to identify a wrong integer conversion
def check_user_int(input_check):
    try:
        outcome = int(input_check)
        return outcome
    except: 
        return -1

# This function validates User input using try and except
# Try is converting the input into string and returning it
# Otherwise except is ran and an error code of -2 is used to identify a wrong string conversion
def check_user_str(input_checking):
    try:
        result = str(input_checking)
        return result
    except:
        return -2

#This function checks for the validity of the user's input
def check_input_validity(building_position, city_structure):
    #check if user input is more than 3 string
    try:
        if len(building_position) > 3 or len(building_position) == 1:
            return -1, -1
        
        building_location = building_position.upper()
        #Check if there is a alphabet in user input
        alpha_check = building_location[0].isalpha()
        if alpha_check == True:
            converted_col = ord(building_location[0])-65 #This is changing the building_location[0] to an ascii number
            if converted_col < 0 or converted_col > 25:
                return -1,-1
        else:
            return -1,-1

        conversion = str(building_location[1])
        conversion2 = str(building_location[2])

        add = conversion + conversion2

        converted_row_int = int(add)
        #Check interger versus city size, return error code if it exceeds city size
        converted_row = check_user_int(converted_row_int)
        if converted_row > len(city_structure):
            return -1,-1
        return converted_row, converted_col
        
    except:
        print("Please enter a proper position.")
        return -1,-1

#This is the function for checking if the user's intended building location have any adjacent buildings
#city_outline[0] is col
#city_outline is row
def check_adj_buildings(given_row, given_col, city_outline):

    if given_col > len(city_outline[0])-1 or given_row > len(city_outline)-1: #checks if the user input is within city range. If it is not, return False
        return False
    elif given_col < 0 or given_row < 0:
        return False

    if len(city_outline[given_row][given_col]) > 1: #checks if the user inputed the same input twice in a row
        return False
 
    #check for left
    if check_left(city_outline, given_row, given_col):
        return True
    #Check for top
    if check_top(city_outline, given_row, given_col):
        return True
    #Check for right
    if check_right(city_outline, given_row, given_col):
        return True
    #check for bottom
    if check_bottom(city_outline, given_row, given_col):
        return True
    
    return False

def print_city_grid(city_data, buildings_selected, remaining_buildings):
    assigned_alpha = 65
    print(" "*3, end = '')
    for cols in range(len(city_data[0])):
        print('{:^5}'.format(chr(assigned_alpha)), end = " ") 
        assigned_alpha += 1
    ##for i in range(len(buildings_selected)):
        ##print("{:>5}".format(buildings_selected[i]), end = " ")
    print()
    print("  +" +(( "-"*5 + '+')* len(city_data[0])), end = " ")
    for i in range(len(buildings_selected)):
        current_building_amount = remaining_buildings.count(buildings_selected[i])
        ##print("{:^5}".format(current_building_amount), end = " ")
    print()

    # Starting out, we label the rows of the city and we used to range 1 in order to start from 1 instead of 0
    # We then print the row number onto the side of the city, etc. 1, 2, 3, 4...
    # We then print out the rest of the city using the for loop for each specific space of the city, relative to size of city (len(city_list))
    for rows in range(len(city_data)):
        print(" {:1}|".format(rows+1), end='')
        for cols in range(len(city_data[0])):
            print("{:^5}|".format(city_data[rows][cols]), end = "")
        print()
        print("  +" +(( "-"*5 + "+")* len(city_data[0])))

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

def see_remaining_buildings():

    return

def save_current_game():

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

def display_current_score():

    return

# This function lets the user choose the city size
def choose_city_size(city_grid):
    row_list = []

    ask_user_col = check_user_int(input("Please enter the width of the city: "))
    ask_user_row = check_user_int(input("Please enter the length of the city: "))

    ##if ask_user_col*ask_user_col > 30:
      ## print("City size is too large (Max area is 30)") #Max size is implemented in order to not exceed the total buildings available for selection
       ##return city_grid

    for i in range(ask_user_col):
        col_list = []
        for j in range(ask_user_row):
            col_list.append(" ")
        row_list.append(col_list) #Appending a list to a list to create a nested list for the city
        
    return row_list

def build_building(building_data,city_layout,current_turn):
    building_location = check_user_str(input("Choose where to build. "))
    converted_row, converted_col = check_input_validity(building_location, city_layout)
    if converted_row and converted_col == -1:
        print("You have entered a value out of range of the city.")
        return False, city_layout
    if current_turn == 1:   
        try:
            city_layout[converted_row-1][converted_col] = building_data
            return True, city_layout
        except:
            print("You have entered a value out of range of the city.")
            return False, city_layout
    else:
        adj = check_adj_buildings(converted_row-1, converted_col, city_layout)
        if adj == True:
            city_layout[converted_row-1][converted_col] = building_data
            return True, city_layout
        else:
            print("You cannot build at places without an adjacent building!")
            return False, city_layout

def start_game(city_content, building_content, current_turn):
    local_building_content = [] #Creates a empty list for deep copy of building_content
    for building_copy in building_content:
        local_building_content.append(building_copy)
    number_of_buildings = []
    for buildings in building_content:
        for index in range(8):
            number_of_buildings.append(buildings)

    #Removal of buildings from saved game to balance out no. of buildings available
    for rows in city_content:
        for cols in rows:
            if len(cols) > 1:
                number_of_buildings.remove(cols)

    result = False
    random.shuffle(local_building_content) #This is to randomise the selection of the 2 buildings
    submenu_list = ["See remaining buildings","See current score\n","Save game"]
    print("Turn {}".format(current_turn)) #Display of turn
    print_city_grid(city_content, building_content, number_of_buildings)

    building_selection1 = "Build a " + str(local_building_content[0])
    building_selection2 = "Build a " + str(local_building_content[1])
    submenu_list.insert(0, building_selection1)
    submenu_list.insert(1, building_selection2)
    
    while current_turn < len(city_content)*len(city_content[0]) + 1:  
        user_sub_selection = print_menu(submenu_list, False) #The False is important here, it determines whether the Exit is a exit to main menu or exiting
        if user_sub_selection == 1:
            result, city_content = build_building(local_building_content[0],city_content,current_turn)     
        elif user_sub_selection == 2: 
            result, city_content = build_building(local_building_content[1],city_content,current_turn)    
        elif user_sub_selection == 3:
            see_remaining_buildings(number_of_buildings, building_content)
        elif user_sub_selection == 4:
            score = display_current_score(city_content, building_content)
        elif user_sub_selection == 5:
            save_current_game(city_content, current_turn, building_content) 
            print("Game Saved") 
        elif user_sub_selection == 0:
            for i in range(len(city_content)):
                for j in range(len(city_content[0])):
                    city_content[i][j] = ' '
            return
        else:
            print("You have entered an invalid selection!\nThe error code is {}. \nPlease try again.\n".format(user_sub_selection))

        if result == True: 
            current_turn += 1
            number_of_buildings.remove(local_building_content[user_sub_selection-1])
            for i in range(len(building_content)):  
                if number_of_buildings.count(building_content[i]) == 0 and local_building_content.count(building_content[i]) > 0:
                    local_building_content.remove(building_content[i])
                    
            random.shuffle(local_building_content)
            building_selection1 = "Build a " + str(local_building_content[0])
            building_selection2 = "Build a " + str(local_building_content[1])
            submenu_list.clear()
            submenu_list = ["See remaining buildings","See current score\n","Save game"]
            submenu_list.insert(0, building_selection1)
            submenu_list.insert(1, building_selection2)

        print("\nTurn {}".format(current_turn))
        print_city_grid(city_content, building_content, number_of_buildings)
        result = False
    
    display_current_score(city_content, building_content)

    length_of_city = len(city_content[0])
    width_of_city = len(city_content)
    city_content.clear()
    for i in range(width_of_city):
        col_list = []
        for c in range(length_of_city):
            col_list.append(" ")
        city_content.append(col_list)
        
    return city_content

# This functions calls the main menu and depending on the choice of the user
# it then runs the corresponding function
def main_menu():
    menu_list = ["Start new game","Load saved game","Show high scores","Choose city size","Choose building pool"]
    building_list = ["R","I","C","O","*"]
    new_turn = 1
    city_list =[[" "," "," "," "],[" "," "," "," "],[" "," "," "," "],[" "," "," "," "]]

    while True:    
        print("\nWelcome to Simp City!")
        print("-"*21)     
        user_selection = print_menu(menu_list, True)
        if user_selection == 1:
            start_game(city_list, building_list, new_turn)
        elif user_selection == 2:
            load_saved_game() 
        elif user_selection == 3:
            high_score() 
        elif user_selection == 4:
            city_list = choose_city_size(city_list)
        elif user_selection == 0:
            exit()
        else:
            print("You have entered an invalid selection!\nThe error code is {}. \nPlease try again.\n".format(user_selection))
      
# This just loops the entire code
main_menu()