nums = [0,1,2,4,5,7]

["0->2","4->5","7"]


def find_summary_ranges(nums):
    ranges = []
    start = end = nums[0]

    for i in range(1, len(nums)):
        if nums[i] - nums[i-1] == 1:
            end = nums[i]
        else:
            if start == end:
                ranges.append(str(start))
            else:
                ranges.append(str(start) + "->" + str(end))
            start = end = nums[i]

    if start == end:
        ranges.append(str(start))
    else:
        ranges.append(str(start) + "->" + str(end))

    return ranges