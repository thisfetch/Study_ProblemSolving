test = input().lower()
test_set = set(test)
test_set = list(test_set)
# clean coding -> test_set = list(set(test))
mylist = [0] * len(test_set)

for i in range(len(test_set)) :
    for j in range(len(test)) :
        if test_set[i] == test[j] : 
            mylist[i] += 1

if mylist.count(max(mylist)) != 1 :
    print("?")
else :
    print(test_set[mylist.index(max(mylist))].upper())