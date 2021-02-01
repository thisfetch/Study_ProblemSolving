test = input().split()
ascending_arr = ["1", "2", "3", "4", "5", "6", "7", "8"]
descending_arr = ["8", "7", "6", "5", "4", "3", "2","1"]

if test == ascending_arr:
    print("ascending")
elif test == descending_arr:
    print("descending")
else:
    print("mixed")