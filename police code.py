n=int(input())
availableOfficers=0
untreatedCrimes=0
eventList=list(map(int,input().split()))
for event in eventList:
    if event == -1:
        if availableOfficers > 0:
            availableOfficers -= 1
        else:
            untreatedCrimes += 1
    else:
        availableOfficers += event
print(untreatedCrimes)
