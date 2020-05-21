from datetime import datetime
from termcolor import colored

def printMatchingLine(filehandle, keyword, color):
    line = filehandle.readline()
    if keyword in line:
        now = datetime.now()
        timestamp = now.strftime('%Y%m%d-%H%M%S.%f')

        output = '[{}]: {}'.format(timestamp, line)
        print(colored(output,color))


if __name__ == '__main__':
    firstfile = open('D:/Pycharm Projects/Testing_Python/datalog', 'rt')

    while True:
        printMatchingLine(firstfile,'Incoming', 'blue' )