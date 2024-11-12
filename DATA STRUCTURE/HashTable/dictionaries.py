from plotly.data import stocks

stock_prices =[]

#to read every line in file
with open ("stock_prices.csv", "r") as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        prices = float(tokens[1])
        stock_prices.append([day,prices])
print("List",stock_prices)

#What is the price on March 9
for element in stock_prices:
    if element[0] == "March 9":
        print(element[1])

#Dictionary more efficiency

stock_prices = {}

with open ("stock_prices.csv", "r") as f:
    for line in f:
        tokens =  line.split(',')
        day = tokens[0]
        price = float(tokens[1])
        stock_prices[day] = price
print("Dictionaries",stock_prices)

#Find price on March 9
print(stock_prices["march 9"])
