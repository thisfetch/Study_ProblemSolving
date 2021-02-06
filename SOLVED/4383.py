while True:
    try:
        jolly = list(map(int, input().split()))
        jolly_list = []
        if jolly[0] == 1:
            print("Jolly")
        elif jolly[0] == len(jolly) - 1:
            for i in range(1, len(jolly) - 1):
                jolly_list.append(abs(jolly[i] - jolly[i + 1]))
            jolly_list.sort()
            for i in range(1, jolly[0]):
                if jolly_list[i - 1] == i and i == len(jolly_list):
                    print("Jolly")
                    break
                elif jolly_list[i - 1] == i:
                    pass
                else:
                    print("Not jolly")
                    break
    except:
        break