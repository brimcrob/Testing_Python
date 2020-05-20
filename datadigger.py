from datetime import datetime

def printMatchingLine(filehandle, keyword,color):
    line = filehandle.readline()
    if keyword in line:
        now = datetime.now()
        timestamp = now.strftime('%Y%m%d-%H%M%S.%f')

        print(('[{}]: {}'.format(timestamp, line)))


if __name__ == '__main__':
    firstfile = open('file://D:/Pycharm Projects/Testing_Python/coordinates.csv', 'rt')

    while True:
        printMatchingLine(firstfile,'58.', 'blue' )