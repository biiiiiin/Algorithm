import datetime

count = int(input())

arr = []

for i in range(count):
    addArr = []
    subject, year, month, day = input().split()
    date = datetime.date(int(year), int(month), int(day))

    
    addArr.append(subject)
    addArr.append(date)
    
    arr.append(addArr)


arr.sort(key=lambda x:x[1])

for i in range(count):
    print(arr[i][0])