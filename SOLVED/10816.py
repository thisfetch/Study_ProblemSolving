def is_exist(arr, target):  # binary search
    start = 0
    end = N-1
    while start <= end:
        mid = (start + end) // 2
        if target == arr[mid]:
            return 1
        if target < arr[mid]:
            end = mid-1
        else:
            start = mid+1

    return 0

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
A.sort()
for i in B:
    print(is_exist(A,i))    