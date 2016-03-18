from sys import argv
import random
import logging

logging.basicConfig(format='%(asctime)s:%(module)s:%(funcName)s:%(lineno)d:%(levelname)s:%(message)s'
,level = logging.ERROR)
logger = logging.getLogger(__name__)
logger.debug('hi')

prompt = '> '
userName = 'default'

try:
    script = argv[0]
    userName = argv[1]
except IndexError:
    pass


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

        logger.debug(type(ans))
        logger.debug(type(expected))

        if ans == str(expected):
            print('Correct!')
        else:
            print("Incorrect, the correct answer is " + str(expected) + " not "
            + str(ans) + "!")

# The method that is run if this module is executed at the cmd line (kind of
# like the main method in Java)
if __name__ == '__main__':
    init_conversation()
