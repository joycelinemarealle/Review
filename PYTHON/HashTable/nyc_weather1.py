#the array List data structure works
#need to open file
#split and save the second part of element which is data
#analyze data in array


#empty array to capture the file details
weather_data = []

#open file
#skip reading the header
with open('nyc_weather.csv', 'r') as csvfile:
    next(csvfile) #skips the header line
    for line in csvfile:
        data = line.split(',')
        temp = float(data[1])
        weather_data.append(temp)
print(weather_data)

#OR#
array = []
with open('nyc_weather.csv', 'r') as csvfile:
    for line in csvfile:
        data = line.split(',')
        try:
            temp = float(data[1])
            array.append(temp)
        except:
            print('Invalid temperature.Ignore the row')
print(array)




#1iWhat was the average temperature in first week of Jan
total = 0.0 #dont use sum since overides built in function
count = 7
for i in range(7):
    total += weather_data[i]
average = total/count
print('The average temperature of first week of Jan',average)

#OR#
print(((sum(weather_data[0:7]))/len(weather_data[0:7])))

#ii What was the maximum temperature in first 10 days of Jan
maximum = 0 #dont use max since overides built in function
for i in range(10):
    for element in weather_data:
        if element > maximum:
            maximum = element
print ('Maximum temperature in first 10 days of Jan',maximum)

#OR#
new_array = array[0:10]
print(max(new_array))