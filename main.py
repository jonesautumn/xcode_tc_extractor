import constants
import argparse
from colors import cprint

parser = argparse.ArgumentParser()
parser.add_argument('--input-file', type=str, dest='input_file',
                    default=constants.DEFAULT_INPUT_FILE)
parser.add_argument('--output-file', type=str, dest='output_file',
                    default=constants.DEFAULT_OUTPUT_FILE)
parser.add_argument('--substring-checker', type=str, dest='substring_checker',
                    default=constants.DEFAULT_SUBSTRING_CHECKER)
args = parser.parse_args()

inputFile = open(args.input_file, "r")
lines = inputFile.readlines()

outputFile = open(args.output_file, "w")
outputFile.write('TC ID,TC Name,TC Jira Link,Commented?\n')


def getFunctionName(line):
    tcStarter = constants.TEST_CASE_NAME_STARTING_FUNCTION

    def getOpeningBracket():
        index = len(line) - 1
        while index >= 0 and line[index] != '(':
            index -= 1
        return index

    funcStartIndex = line.index(tcStarter) + len(tcStarter)
    funcEndIndex = getOpeningBracket()

    isCommented = line[:2] == '/*'

    return line[funcStartIndex:funcEndIndex], isCommented


def getTestCaseId(line, tcId):
    tcStartIndex = line.index(tcId)
    tcEndIndex = tcStartIndex + constants.TEST_CASE_ID_LENGTH
    return line[tcStartIndex: tcEndIndex]


resultArray = []

for index in range(1, len(lines)):
    line = lines[index].strip()
    tcId = constants.TEST_CASE_ID_IDENTIFIER

    if args.substring_checker in line and tcId in line:
        testCaseId = getTestCaseId(line, tcId)
        functionName, isCommented = getFunctionName(lines[index - 1].strip())
        printColor = 'warning' if isCommented else 'success'
        cprint('{} - {}'.format(testCaseId, functionName), printColor)

        jiraLink = constants.JIRA_TC_LINK + testCaseId
        resultLine = f'{testCaseId},{jiraLink},{functionName},{isCommented}\n'
        outputFile.writelines(resultLine)

outputFile.close()
