import time
import threading


def calc_square(numbers):
    print('calculate square numbers')
    for n in numbers:
        time.sleep(0.2)
        print('square', n*n)

def calc_cube(numbers):
    print('calculate cube of numbers')
    for n in numbers:
        time.sleep(0.2)
        print('cube', n*n*n)

arr = [2,3,8,9]
#how long it took to execute program just before calculations
t = time.time()

#assign task to threads
t1 = threading.Thread(target =calc_square, args = (arr,))
t2 = threading.Thread(target = calc_cube, args=(arr,))

#start threads in parallel
t1.start()
t2.start()

#when programs done the threads join the main program
t1.join()
t2.join()

print('done in : "', time.time()-t)
print("Hah... I am done with all my work now!")
