from sys import argv
import random
import logging

logging.basicConfig(level = logging.DEBUG)
logger = logging.getLogger(__name__)

prompt = '> '

try:
    script = argv[0]
    userName = argv[1]
except IndexError:
    userName = 'default'


def init_conversation():
    """ Handles the conversation """
    print("Hi ", userName, ", I am the ", script, " script.")

    hasNumQuestions = False
    numQuestions = -1

    while hasNumQuestions == False:
        print("How many questions would you like to answer?")
        numQuestionsStr = input(prompt)

        try:
            numQuestions = int(numQuestionsStr)
            hasNumQuestions = True
        except:
            print("Unable to parse \'" + numQuestionsStr +
            "\' as an integer, please enter an integer")
            pass
    print("Preparing " + str(numQuestions) + " questions.")

    for i in range(0, numQuestions):
        questionStr = str(i) + ' + ' + str(random.randint(0, numQuestions))
        print('Question ' + str(i + 1) + ': ' + questionStr)
        ans = input(prompt)

        expected = eval(questionStr)

        print(type(ans))
        print(type(expected))

        if ans == str(expected):
            print('Correct!')
        else:
            print("Incorrect, the correct answer is " + str(expected) + " not "
            + str(ans) + "!")

if __name__ == '__main__':
    init_conversation()
