import sys

number = int(input())
my_set = []

for i in range(number) :
    my_set.append(sys.stdin.readline())
my_set = list(set(my_set))

my_set.sort(key = len)

for i in range(len(my_set) - 1) :
    for j in range(1, len(my_set)) :
        if len(my_set[i]) == len(my_set[j]) :
            if my_set[j] > my_set[i] :
                my_set[i], my_set[j] = my_set[j], my_set[i]

print("".join(my_set))
