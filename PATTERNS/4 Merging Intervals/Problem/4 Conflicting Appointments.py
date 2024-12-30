def can_attend_all_appointments(intervals):
    #TOD write code
    # sort the intervals
    #check if two intervals overlap

    #1 Initialization
    start,end = 0,1

    # 2 Sort intervals by start value
    intervals.sort(key = lambda x : x[0]) #start is at index 0

    #3 loop through intervals to find overlap
    for i in range(1, len(intervals)):
        if intervals[i][start] < intervals[i-1][end]: #compare start of current to previous end to see overlap b.start < a.end
        # #"<" not "<=" comparision as we will be merging the two intervals having conditions #
        # #such interval not conflicting since appointment start right after the other
         return False
    return True

def main ():
    print("Can attend all appointment " + str( can_attend_all_appointments([[1,4], [2,5], [7,9]] )))
    print("Can attend all appointment " + str(can_attend_all_appointments([[6,7], [2,4], [8,12]])))

main()