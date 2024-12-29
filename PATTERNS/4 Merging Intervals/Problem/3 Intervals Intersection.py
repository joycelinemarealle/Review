def merge(intervals_a, intervals_b):
    #1 Initialize variables
    result = []
    i,j,start,end = 0,0,0,1 #start and end indices of intervals

    #2 Traverse both lists of intervals
    while i < len (intervals_a) and j < len(intervals_b):

    #3 Check for overlaps
    #check if intervals overlap and interval_a[i]'s start time within in interval_b[j]
        a_overlaps_b =  intervals_a[i][start] >= intervals_b[j][start] and intervals_a[i][start] <= intervals_b[j][end]
        # check if intervals overlap and interval_a[i]'s start time within in interval_b[j]
        b_overlaps_a = intervals_b[j][start] >= intervals_a[i][start] and intervals_b[j][start] <= intervals_a[i][end]

        #Store the intersection part
        if(a_overlaps_b or b_overlaps_a):
            overlap_start = max (intervals_a[i][start], intervals_b[j][start])
            overlap_end = min (intervals_a[i][end], intervals_b[j][end])
            result.append([overlap_start,overlap_end])

        #Move pointer for thw interval finishing first
         #to ensure all intersection are checked and overlaps missed no point of continue if one interval over
        if intervals_a[i][end] < intervals_b[j][end]:
            i+=1
        else:
            j+=1

    return result


def main():
    print("Intervals Intersection " + str(merge([[1,3],[5,6],[7,9]], [[2,3], [5,7]])))
    print("Intervals intersection : " + str (merge([[1,3], [5,7], [9,12]], [[5,10]])))

main()