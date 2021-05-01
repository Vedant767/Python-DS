def swap (a, b, elements):
    if a != b:
        elements[a], elements[b] = elements[b], elements[a]


def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]
    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start += 1
        while elements[end] > pivot:
            end -= 1
        if start < end:
            swap(start, end, elements)
    swap(pivot_index, end, elements)
    
    return end

def quicksort(elements, start, end):
    if start < end:
        pi = partition(elements, start, end)
        quicksort(elements, start, pi-1)
        quicksort(elements, pi+1, end)

elements = [5, 6, 2, 1, 0, 21, 15, 12]
quicksort(elements, 0, len(elements)-1)