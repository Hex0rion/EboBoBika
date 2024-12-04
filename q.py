def partition(l1, l2, low, high):
    i = low
    j = low
    while j < high:
        if l1[j] > l1[high]:
            l1[i], l1[j] = l1[j], l1[i]
            l2[i], l2[j] = l2[j], l2[i]
            i += 1
        j += 1
    l1[i], l1[high] = l1[high], l1[i]
    l2[i], l2[high] = l2[high], l2[i]
    return i, l1, l2

def qsort_rec(l1, l2, low, high):
    if low < high:
        q, l1, l2 = partition(l1, l2, low, high)
        l1, l2 = qsort_rec(l1, l2, low, q-1)
        l1, l2 = qsort_rec(l1, l2, q+1, high)
    return l1, l2

def qsort(l1, l2):
    return qsort_rec(l1, l2, 0, len(l1)-1)
