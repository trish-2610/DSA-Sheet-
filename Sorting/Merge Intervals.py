def merge_intervals(intervals):

    ## sort based on 0 (first) index
    intervals.sort(key = lambda x : x[0])

    ## result 
    result = [intervals[0]]

    for i in range(1,len(intervals)): ## start from fist index
        current = intervals[i]
        last = result[-1]

        if current[0] <= last[1]:
            ## Overlap exists 
            last[1] = max(last[1],current[1]) ## this changes will also be reflected in result
        else:
            ## NO overlap exists 
            result.append(current)
    return result

arr = [[1,3],[2,6],[8,10],[15,18]]
print(merge_intervals(arr))