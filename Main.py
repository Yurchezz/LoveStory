from MergeSort import mergeSort
from SummOfThree import findThreeNumbers


def main():
    arr = [1, 8, 3, 5, 4, 3]
    P = 100
    mergeSort(arr)
    print(arr)

    if findThreeNumbers(arr, P) is None:
        print("Not this time, Ilona")
    else:
        print(findThreeNumbers(arr, P))


if __name__ == '__main__':
    main()
