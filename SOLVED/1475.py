number_set = list(0 for _ in range(10))
room_number = input()

for tmp in room_number:
    if tmp == '6' or tmp == '9':
        if number_set[6] != number_set[9]:
            if number_set[6] > number_set[9]:
                number_set[9] += 1
            else:
                number_set[6] += 1
        else:
            number_set[int(tmp)] += 1
    else:
        number_set[int(tmp)] += 1

print(max(number_set))