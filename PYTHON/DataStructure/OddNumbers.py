#Ask user for input
user = int (input("Enter a number :"))

#Create a list of all odd numbers between 1.py and a max number.
# Max number is something you need to take from a user using input() function

odd_list = []
for i in range( 1, user):
    if i%2 !=0:
        odd_list.append(i)
print(odd_list)


