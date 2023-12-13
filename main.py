def new_game():
    guesses = []
    correct_guess = 0
    question_num = 1
    for key in questions:
        print("------------------------")
        print(key)
        for i in options[question_num - 1]:
            print(i)
        guess = input("Enter (A,B,C or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guess += check_answer(questions.get(key), guess)
        question_num += 1
    display_score(correct_guess, guesses)


# ------------------------
def check_answer(answer, guess):
    if answer == guess:
        print("Correct")
        return 1
    else:
        print("wrong")
        return 0


# ------------------------
def display_score(correct_guesses, guesses):
    print("--------------")
    print("Results")
    print("--------------")
    print("Ansers: ", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is " + str(score)+"%")


# ------------------------
def play_again():
    reponse = input("Do you want to play again ?:  Yes/No")
    reponse = reponse.upper()
    if reponse == "YES":
        return True
    else:
        return False


# ------------------------
questions = {
    "who created Python?": "A",
    "What year was Python Created?  ": "B",
    "Python is tributed to which comedy group: ": "C",
    "is the Earth round?: ": "A"
}

options = [["A. Guido van Rossum", "B. Ellon musk", "C. Bill Gates", "D.Mark Zuker"],
           ["A. 1989", "B. 1991", "C. 2000", "D.2016"],
           ["A. Lovely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
           ["A. True", "B. False", "C. Sometimes", "D. What is Earth"]]

new_game()

while play_again():
    new_game()

print("Bye")