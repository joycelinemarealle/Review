#Create a dictionary holding expenses
expense = {
                   "Jan": 2200,
                   "Feb" : 2350,
                   "Mar" : 2600,
                  " Apr" : 2130,
                   "May": 2190}
print()
expense1 = {
                   1: 2200,
                   2 : 2350,
                   3 : 2600,
                   4 : 2130,
                   5: 2190}
print ("Monthly expenses",expense1)
print()

# 1 In Feb, how many dollars you spent extra compare to January?
amount = expense["Feb"] - expense["Jan"]
print( "Spent $ in February ",amount, "than January")

# 2. Find out your total expense in first quarter (first three months) of the year.
    #dictionaries are not sequences so store in numbers so it is easier to sort
    #Get list of keys and sort them
Ks = list(expense1.keys())
Ks.sort()
print()

    #loop through first 3 keys and sum
sum = 0
current_index = 0
for i in Ks:
    current_index += 1
    sum += expense1[i]
    if current_index == 3 :
        break
print("The first quarter expense :$", sum)
print()

# 3. Find out if you spent exactly 2000 dollars in any month
for i in Ks:
    if expense1[i] == 2000:
        print ("There is a month where I spent exactly $", 2000)
    #
print (2000 in expense1,", No month expense of $2000")
print()

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
expense1[6] = 1980
print ("June month expense added",expense1)
print()

# 5. You returned an item that you bought in a month of April and
   # got a refund of 200$. Make a correction to your monthly expense list based on this
expense1[4] = expense1[4] -200
print("New expenses after April refund",expense1)
print()