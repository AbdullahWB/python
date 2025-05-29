import random

def game():
    print("Welcome to playing a game!")
    currentScore = random.randint(0, 6)
    print(f"Your score is {currentScore}.")
    
    with open("hiScore.txt", "a") as file:
        file.write(str(currentScore))
        file.write(" ")
    
    
def totalScore():
    try:
        # Open the file in read mode to read all scores
        with open("hiScore.txt", "r") as file:
            score = file.read()
        
        # Convert the score string to a list of integers
        score_list = list(map(int, score.split()))
        
        # Calculate the total sum of the scores
        total_score = sum(score_list)
        
        # Print the total score
        print(f"Your total score is {total_score}.")
    except FileNotFoundError:
        print("The file 'hiScore.txt' does not exist. Please play the game first.")
        
        
for i in range(1, 300):
    game()
    
totalScore()