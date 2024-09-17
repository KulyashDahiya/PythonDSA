def BinarySearch(arr, x):
    lower_bound = 0
    upper_bound = len(arr) - 1
    
    while lower_bound < upper_bound:
        mid = (lower_bound + upper_bound) // 2
        if arr[mid] == x:
            return f"Element is present at index : {x}"
        elif x < arr[mid]:
            upper_bound = mid - 1
        else:
            lower_bound = mid + 1
    
    return "Element Not Found in Given Array"

def RecursiveBinarySearch(arr, x, l, u):
    mid = (l+u) // 2

    if x == arr[mid] :
        return mid
    elif x < arr[mid] :
        return RecursiveBinarySearch(arr, x, l, mid - 1)
    elif x > arr[mid] :
        return RecursiveBinarySearch(arr, x, mid + 1, u)
    else :
        return -1
    



if __name__ == "__main__":
    arr = [6,23,56,1,465,7,43,234,55,22,12]
    n = len(arr)
    x = 465
    arr.sort()
    print(f"Given array Sorted : {arr}")
    # print(BinarySearch(arr, x))

    print(RecursiveBinarySearch(arr, x, 0, n-1))



