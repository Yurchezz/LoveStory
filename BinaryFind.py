def binaryFind(arr, x, index1, index2):
    begin = 0
    end = len(arr)
    while begin < end:
        middle = (begin + end) // 2
        if x <= arr[middle]:
            end = middle
        else:
            begin = middle + 1

    if begin == len(arr) or arr[begin] != x:

        return -1

    if begin == index1 or begin == index2:
        return -1

    return arr[begin]
