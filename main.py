def binarySearch(sequence, item):
    start = 0
    last = len(sequence)

    while start <= last:
        midpoint = start + (last - start) // 2
        midpoint = sequence[midpoint]
        if midpoint == item:
            return midpoint

        elif item < midpoint:
            last = midpoint - 1

        else:
            start = midpoint + 1

    return None


mySequence = [1, 3, 5, 7, 9, 11, 13, 15, 17, 21, 23, 25, 27]
val = 11

print(binarySearch(mySequence, val))
