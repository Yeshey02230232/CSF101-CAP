################################
# Yeshey wangdi
# 1-ICE
# 02230232
################################
# REFERENCES
# Links that you referred while solving
# the problem
#https://www.w3schools.com/python/
#https://www.geeksforgeeks.org/python3-tutorial/
#https://www.tutorialspoint.com/python/index.htm
#https://www.codecademy.com/learn/learn-python-3
################################
# SOLUTION
# Your Solution Score:49903
# 02230232
################################
def read_input_file(file_path):
    """
    Reads the input file[02230232->2] and returns a list of tuples containing the shape and outcome for each round as per the demand.
    """#This function reads a text file specified by file_path(input_2_cap1.txt)
    rounds = []
    with open(file_path, 'r') as file:
#It reads each line in the file, splits it into a shape and an outcome (assuming they are separated by a space), 
#and adds them as a tuple to the rounds list.
        for line in file:
            shape, outcome = line.strip().split()
            rounds.append((shape, outcome))
    return rounds#Finally, it returns the list of rounds.

def calculate_score(rounds):
    """
    Calculating the total score based on the rounds played.
    """
#The function calculates the total score based on rounds played, initializing the score variable to 0. 
#It creates dictionaries, shapes_scores and outcome_scores, iterates over rounds,
# finds shape and outcome scores, adds them, and returns the total score.
    score = 0
    shape_scores = {"A": 1, "B": 2, "C": 3}
    outcome_scores = {"X": 0, "Y": 3, "Z": 6}

    for shape, outcome in rounds:
        shape_score = shape_scores.get(shape, 0)
        outcome_score = outcome_scores.get(outcome, 0)
        score += shape_score + outcome_score

    return score

# Main program
#The code sets the file_path variable to the input file, 
#reads rounds from it, calculates the total score, and prints the total score.
file_path = "input_2_cap1.txt" 
rounds = read_input_file(file_path)
total_score = calculate_score(rounds)
print("Total Score:", total_score)