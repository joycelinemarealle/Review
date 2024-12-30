def conflicting_appointments(intervals):
    #1Initialization of variables
    conflicting_appointments = []
    start, end = 0,1

    # 2sort the intervals
    intervals.sort(key=lambda x: x[0])

    #3Travers through list of intervals to find overlapping b.start < a.end (previous interval
    for i in range(1,len(intervals)):
        #if two intervals overlap
        if intervals[i][start] < intervals[i-1][end]:
            conflicting_appointments.append(intervals[i])

        #if two intervals overlap store in new list

    #return new list
    return conflicting_appointments

def main ():
    print("Conflicting appointments are " + str(conflicting_appointments([[4,5], [2,3], [3,6], [5,7], [7,8]])))

main()