import sys
input = sys.stdin.readline

N = int(input())
numbers = [int(input()) for _ in range(N)]

def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr)//2
    low = merge_sort(arr[:mid])
    high = merge_sort(arr[mid:])

    l,h = 0,0
    merge = []
    while l < len(low) and h < len(high):
        if low[l] < high[h]:
            merge.append(low[l])
            l += 1
        else:
            merge.append(high[h])
            h += 1
    
    merge += low[l:]
    merge += high[h:]
    return merge

result = merge_sort(numbers)
print(*result, sep="\n")