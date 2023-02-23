array = list(map(int, input().split()))

def quic_sort(arr):
    if len(arr) <= 1:
        return arr
    pv = arr[len(arr) // 2]
    less, equal, greater = [], [], []
    for n in arr:
        if n < pv:
            greater.append(n)
        elif n > pv:
            less.append(n)
        else:
            equal.append(n)
    return quic_sort(less) + equal + quic_sort(greater)

print(quic_sort(array))