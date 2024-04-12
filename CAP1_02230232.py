################################
# Yeshey Wangdi
# 1 ICE
# 02230232
################################
# REFERENCES
# https://www.w3schools.com/python/
# https://codefinity.com/get-started/spa/v16/spv16/quarter?utm_source=google&utm_medium=cpc&utm_campaign=20955067105&utm_content=158406843512&utm_term=best%20python%20bootcamp&gad_source=1&gclid=CjwKCAjwt-OwBhBnEiwAgwzrUs61Mvz6iZbJJevHlcobPdVMYhokqYtZwS81zO-XIMKsqG6Vnn18SRoC3lgQAvD_BwE
# https://codefinity.com/get-started/spa/v16/spv16/quarter?utm_source=google&utm_medium=cpc&utm_campaign=20955067105&utm_content=158406843512&utm_term=best%20python%20bootcamp&gad_source=1&gclid=CjwKCAjwt-OwBhBnEiwAgwzrUs61Mvz6iZbJJevHlcobPdVMYhokqYtZwS81zO-XIMKsqG6Vnn18SRoC3lgQAvD_BwE
################################
# SOLUTION
# Your Solution Score:49801
# 49801
################################
def read_input(input_user):
    play_turn= []
    with open(input_user, 'r') as file:
        for line in file:
            choice, results = line.strip().split()
            play_turn.append((choice, results))
    return play_turn
#The function creates an empty list play_turn, opens the input file in read mode, 
#separates lines into choices and results, appends a tuple, and returns the list with the choices and results.

def calculate_score(play_turn):
    point = 0
    for choice, results in  play_turn:
        if choice == "A":
            if results== "X":
                 choice_point = 3
            elif results == "Y":
                 choice_point = 4
            else:
                 choice_point = 8
        elif choice == "B":
            if results == "X":
                 choice_point = 1
            elif results == "Y":
                 choice_point = 5
            else:
                 choice_point = 9
        else:
            if results == "X":
                 choice_point = 2
            elif results == "Y":
                 choice_point = 6
            else:
                 choice_point = 7

        point += choice_point

    return point
#The function creates an empty list play_turn, opens the input file in read mode, separates lines into choices and results,
# appends a tuple, and returns the list with the choices and results.

# Main program
input_user = "input_2_cap1.txt"  # Replace with the path to your input file
play_turn = read_input(input_user)
total_score = calculate_score(play_turn)
print("Total Score:", total_score)
#The code initializes the input_user variable, reads input files, 
#saves the results in the play_turn list, computes the total score, and prints it to console.
