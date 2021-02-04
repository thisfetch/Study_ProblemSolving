num = int(input())
count = num

for _ in range(num):
    word = input()
    sarr = set()
    for i in range(len(word)):
        if i != 0 and word[i] in sarr and word[i] != word[i - 1]:
            count = count - 1
            break
        sarr.add(word[i])


print(count)
