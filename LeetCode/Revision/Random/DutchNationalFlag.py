def sort_array(nums, pivot = 1):
    i = 0
    j = 0
    k = len(nums) - 1

    while j<=k:
        if nums[j] < pivot:
            swap(nums, i, j)   #Swapping
            i += 1
            j += 1
        elif nums[j] > pivot:
            swap(nums, j, k)
            k -= 1
        else:
            j += 1

def swap(data, i, j):
    data[i], data[j] = data[j], data[i]

if __name__ == '__main__':
    ar = [1,2,0,0,2,1,1,0,2]
    print(ar)
    sort_array(ar)
    print(ar)