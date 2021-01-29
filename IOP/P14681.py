hour, minute = input().split()
hour = int(hour)
minute = int(minute)

if minute < 45 :
    if hour == 0 :
        hour = 23
    else :
        hour -= 1;
    minute = 60 + minute - 45
else :
    minute = minute - 45

print(hour, minute)