"""
Searching Algorithm
"""


# sequential access
def linear_search(a, key):
    for i in range(len(a)):
        if a[i] == key:
            return i

    return -1


# works for sorted array only
# divide and conquer algorithm (random access)
# Space Complexity : O(1) - best case, O(log n) - worst case
def binary_search(arr, key):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = int((left + right) / 2)

        if key == arr[mid]:
            return mid

        if key < arr[mid]:
            right = mid - 1

        if key > arr[mid]:
            left = mid + 1

    return -1  # element not found


def recursive_binary_search(arr, left, right, key):
    if left > right:
        return -1

    # should be typecast to int otherwise it returns float
    mid = int((left + right) / 2)

    if key == arr[mid]:
        return mid

    if key < arr[mid]:
        index = recursive_binary_search(arr, left, mid - 1, key)
    else:
        index = recursive_binary_search(arr, mid + 1, right, key)

    return index


def main():
    arr = [88, 33, 66, 99, 11, 77, 22, 55, 11]
    num = int(input("Enter number to be searched: "))
    # index = linear_search(arr, num)
    # index = binary_search(arr, num)
    index = recursive_binary_search(arr, 0, len(arr) - 1, num)
    if index == -1:
        print(f"Element {num} is not found.")
    else:
        print(f"Element {num} found at index {index}")


if __name__ == '__main__':
    main()
