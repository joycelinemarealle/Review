#Hash Table (dictionaries) since key-value pair needed

#empty dictionary
weather_data = {}

#add values in dictionaries

#open file
with open('nyc_weather.csv', 'r') as csvfile:
    next(csvfile)
    for line in csvfile:
        data = line.split(',')
        day = data[0]
        temp = int( data[1])
        weather_data[day] = temp
print(weather_data)

# iWhat was the temperature on Jan 9?
print('Temp on Jan 9',weather_data['Jan 9'])

#ii What was the temperature on Jan 4?
print('Temp on Jan 4',weather_data['Jan 4'])