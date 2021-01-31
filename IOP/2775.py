for _ in range(int(input())):
    k = int(input())
    n = int(input())
    citizen = [i for i in range(1, n + 1)]
    for _ in range(k):
        for j in range(1, n):
            citizen[j]+=citizen[j - 1]
    print(citizen[n-1])