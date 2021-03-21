sentence = input()
alphabet_of_list = [0 for _ in range(26)]

for tmp in sentence:
    alphabet_of_list[ord(tmp)-97] += 1

print(' '.join(map(str, alphabet_of_list)))