array = [7, 6, 10, 5, 9, 2, 1, 15, 7]


def quick_sort(arr):
    # choose a pivot element whether first, middle or last
    # partioning of the array is backbone of quicksort
    # pivot can also be called key element
    # left all elements less than pivot go to left
    # right --> all elements bigger than pivot
    pivot = arr[0]
    left = []
    right = []


print(quick_sort(array))

def quick_sort_2(sequence):
    length = len(sequence)

    if length <=1 :
        return sequence
    else:
        pivot = sequence.pop()
    
    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return quick_sort_2(items_lower) + [pivot] + quick_sort_2(items_greater)


print(quick_sort_2([5,2,3,9,1,10,12]))
