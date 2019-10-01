from BinaryFind import binaryFind


def findThreeNumbers(arr, P):
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if i != j:
                x = P - arr[i] - arr[j]
                result = binaryFind(arr, x, i, j)

                if result != -1:
                    return [arr[i], arr[j], result]


