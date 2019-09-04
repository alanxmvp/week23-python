from arepl_dump import dump

arr = [7, 9, 21, 42, 58, 67, 88]


def bsearch(arr, low, high, x):

    # Check base case
    while high >= low:
        mid = low + (high - low) / 2
        mid = int(mid)

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return bsearch(arr, low, mid - 1, x)
            mid - 1
        # Else the element can only be present in right subarray
        else:
            return bsearch(arr, mid + 1, high, x)
            mid + 1
    else:
        # Element is not present in the array
        print("Element is not present in array")
        return -1


print(bsearch(arr, 0, len(arr) - 1, 67) == 5)
print(bsearch(arr, 0, len(arr) - 1, 9) == 1)

