N, M = map(int, input().split())

noListen = set()
noSee = set()

for i in range(N) :
    noListen.add(input())

for i in range(M) :
    noSee.add(input())

noListenSee = list(noListen & noSee)


print(len(noListenSee))

for ch in sorted(noListenSee):
    print(ch)



