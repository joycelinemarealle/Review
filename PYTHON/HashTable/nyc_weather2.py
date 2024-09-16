#Hash Table since key-value pair needed

#empty dictionary
weather_data = {}

#add values in dictions

#open file
with open('nyc_weather.csv', 'r') as csvfile:
    next(csvfile)
    for line in csvfile:
        data = line.split(',')
        day = data[0]
        temp = data[1]
        weather_data.
print(weather_data)