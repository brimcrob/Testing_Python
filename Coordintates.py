#this is from a webinar that was to with testing python not my original code!

# creates the variables to use in the file
import random

latitude = 58
longitude = 18

#creates the file and how I am writing to that file
fh = open('coordinates.csv','wt')
fh.write('type,py latitude, longitude\n')

#creates the data multipe times
for i in range(10):

    lat_direction = random.choice(['North', 'South'])
    long_direction = random.choice(['East', 'West'])

    #diff creates a float number between 0 & 1
    diff = random.random()

    if lat_direction == 'North':
        latitude += diff
    else:
        latitude -= diff

    if long_direction == 'East':
        longitude += diff
    else:
        longitude -= diff

    output = "T,{},{}\n".format(latitude, longitude)
    fh.write(output)

fh.close()