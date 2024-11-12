def triplets_smaller_sum(arr, target):
    #sort array before using two points
    arr.sort()
    #initialization
    count = 0

    #iterate through the array len(arr)-2 left i+1 and right len(arr)-1
    for i in range (len(arr)-2):
        count += search_pair(arr, target - arr[i], i+1)
        return count
def search_pair(arr,target_sum, left):
    count = 0
    right =  len(arr) -1
    while (left < right):
        if arr[left] + arr[right] < target_sum: #found the triplet
            count += right -left #since arr[right] >= arr[left], we can replace arr[right]by any number
            #between left and right to get sum less thant target sum
            left +=1
        else:
            right -=1 #need pair with smaller sum

    #return count
    return count

if __name__ == '__main__':
    print (triplets_smaller_sum([-1,0,2,3] ,3))