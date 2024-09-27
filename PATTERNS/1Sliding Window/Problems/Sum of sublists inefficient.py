#K = number of elemenet to find average of
#arr = input numbers

#METHOD 1 : IN EFFICIENT
def  find_averages_of_subarrays(K,arr):
    result = []
    #end sublist with fir index arr[4]. Range doesnot include arr[5]
    for i in range (len(arr)- K +1):
        #find sum of next K elements
        _sum = 0.0 #avoid overwriting in built function sum
        for j in range (i, i+K):
            _sum += arr[j]
        result.append(_sum/K) #calculatr average
    return result




if __name__ == '__main__':
    arr = [1,3,2,6,-1,4,1,8,2]
    K= 5
    print(find_averages_of_subarrays(K,arr))