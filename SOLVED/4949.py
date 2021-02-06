stack = []
table = {
    ')': '(',
    ']': '['
}

while True:
    flag = True
    stack.clear()
    sen = input()
    if sen == '.':
        break
    for char in sen:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')' or char == ']':
            if len(stack) == 0 or table[char] != stack.pop():
                flag = False
                break
    if not stack and flag == True:
        print('yes')
    elif len(stack) != 0 or flag == False:
        print('no')
