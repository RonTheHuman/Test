from random import randint
from random import shuffle
from functools import reduce
from time import sleep

# extract data from file
with open("quiz_data.txt", encoding="utf8") as f:
    quiz_data = f.read()
quiz_data = list(q.split("\n") for q in quiz_data.split("\n\n"))
# questions first, then reactions
questions = quiz_data[:-2]
incorr_react = quiz_data[-2]
corr_react = quiz_data[-1]
shuffle(questions)
shuffle(incorr_react)
shuffle(corr_react)
# opening linessssss
print("LADIESSS AND GENTLEMEN, WELCOME TO THE wOuNdErFuL PyThOn qUiZ!1!!1")
sleep(0.5)
print("...")
sleep(0.5)
print("...")
sleep(0.5)
print("pleassse do not feed the pythonsss.\n")
sleep(1.5)

for j, question in enumerate(questions):
    '''
    Saves all answers but the first, which is always
    the correct one. Shuffles the list and then
    randomly inserts the first into it, saving the position.
    '''
    answers = question[2:-1]
    shuffle(answers)
    correct_ans = randint(1, len(answers))
    answers.insert(correct_ans - 1, question[1])
    '''
    Prints the question number, with an increasing amount of
    exclamation marks. Then prints the question, and
    "Enter 1/2/3/.." according to the number of answers.
    '''
    print(f"QUESTION {j + 1}{'!'*((j + 1)*(j + 1))}")
    answer_options = reduce(lambda a, b: str(a) + '/' + str(b),
                           range(1, len(answers) + 1))
    # I can do lambdas, right? I don't remember what we learnt until then.
    print(f"{question[0]}\nEnter " \
          f"{answer_options}")
    
    correct = False
    for i, answer in enumerate(answers):
        print(f"{i + 1}: {answer}")
        hint = False
    while (not correct):
        input_ans = input()
        # checks if the input is one of the answer numbers
        while input_ans not in  \
                list(str(x) for x in range(1, len(answers) + 1)):
            print("Input must be an answer number!")
            input_ans = input()
        input_ans = int(input_ans)
        # correct answer position saved from earlier
        if (input_ans == correct_ans):
            correct = True
        else:
            print(f"Incorrect! {incorr_react[0]}")
            incorr_react += [incorr_react.pop(0), ]
            # makes the random answers loop once they ran out
            if not hint:
                print(f"Hint: {question[-1]}")
                hint = True
    print(f"Correct! {corr_react[0]}\n")
    corr_react += [corr_react.pop(0), ]

print("YOU HAVE COMPLETED THE QUIZ! MAY YOU HAVE A FANTASSSSSTIC DAY!")
