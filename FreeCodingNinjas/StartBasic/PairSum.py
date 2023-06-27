from array import array as arr

def pair_sum(arr2, k):
    seen = set()
    output = set()
    for num in arr2:
        target = k - num
        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num,target),max(num,target)))
    return output, len(output)

arr1 = arr('i',[1,1,1,1])
k = 2
print(pair_sum(arr1, k))