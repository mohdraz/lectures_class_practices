'''
Time Complexity: 
O(n+k) --> O(n) --> linear time
'''
def count_sort(arr):
    maxValue = int(max(arr))
    size = len(arr)
    count = [0 for i in range(maxValue+1)]
    output=[0 for i in range(len(arr))]
    print(f"initiate: {count} ")

    for i in range(len(arr)):
        count[arr[i]] += 1

    print(f"updateCount: {count} ")

    for i in range(1, len(count)):
        count[i] = count[i] + count[i-1]
    
    print(f"updatePosition: {count} ")

    while size >= 0:
        pos = count[arr[size-1]]
        output[pos-1] = arr[size-1]
        count[arr[size-1]] -= 1
        size -= 1
    return output





array = [2,1,1,0,2,5,4,0,2,8,7,7,9,2,0,1,9]
print(count_sort(array))