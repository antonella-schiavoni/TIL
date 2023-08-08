# https://leetcode.com/problems/merge-intervals/description/

def merge(intervals: List[List[int]]) -> List[List[int]]:
    if not intervals:
        return []

    # Sort the intervals by the start marker
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for current in intervals:
        # If the current interval overlaps with the last merged interval, update the end marker of the last merged interval
        if current[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], current[1])
        else:
            # If not, add the current interval to the merged list
            merged.append(current)

    return merged
