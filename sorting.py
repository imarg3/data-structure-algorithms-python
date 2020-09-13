"""
Sorting Algorithms
"""


def selection_sort(arr):
    # select i th element
    for i in range(len(arr) - 1):
        # compare selected element with all elements after that
        for j in range(i+1, len(arr)):
            # if i th element > j th element, swap them
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]


def bubble_sort(arr):
    # run n-1 passes for bubble sort
    for i in range(len(arr) - 1):
        # compare all consecutive elements of the array
        for j in range(len(arr) - 1):
            # if j th element > j+1 th element, swap them
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def main():
    arr = [25, 14, 22, 43, 68, 14]
    # selection_sort(arr)
    bubble_sort(arr)
    print(arr)


if __name__ == "__main__":
    main()
