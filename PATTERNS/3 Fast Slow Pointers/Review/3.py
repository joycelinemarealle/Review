
def find_happy_number(num):
    slow , fast = num, num
    while True:
        slow = find_square_sum(slow) #move one step
        fast = find_square_sum(find_square_sum(fast)) #move two steps
        if slow == fast:#found cycl
          break
        return slow ==1 #see if cycle stuck at q=1

def find_square_sum(num):
    sum_of_digits = 0
    while num > 0:
        # extract last digit == remainder after dividing by 10
        digit = num %10
        # sum the squares of digit
        square_of_digit = digit **2
        sum_of_digits += square_of_digit
        #remove last digit by floor division by 10
        num //=10
    return sum_of_digits

def main ():
    print( "Happy number "+ str(find_happy_number(23)))

main ()


#cycle slow and fast pointers ( if cycle then  happy since slow stuck at 1
#need spplit number into digits
#loop repeatedly
#square each digit
#take sum
#then repeat
#if get 1 then happy number


#split number
    #extract last digit by 23 %10
    # square it
    #track sum
    # remove last digit num = 23//10( save first digit )
    #loop