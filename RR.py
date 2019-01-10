
print("\t\t\t\t\t\t\tRound Robbin Scheduling Algorithm \n\t\t\t\t\t\t\t\t\t\t(Same Arrival-Time)")
bt = []   # BurstTime
at = []   # Arrival time
ct = [0]   # Completion time
wt = []   # Waiting time
tat = []  # TurnAround time
pro = []  # Processes
pri = []  # Priority
stat = 0
m = 0
qt = 0    # quantum time
rem_bt = []
t = 0
n = int(input("Enter Number of processes:"))

ghcr = []
for i in range(0, n):
    pro.insert(i, i+1)


# Arrival-Time-Input
at = int(input("Enter Arrival Time:"))

# Quantum Time
qt = int(input("Enter Quantum Time:"))

# Burst-time-Input
bt = list(map(int, input("Enter Burst Time:").strip().split()))



for i in range(len(bt)):
    rem_bt.insert(i, bt[i])
hj = 0
a = 0
while 1:
    for i in range(0, n):
        flag = True
        if rem_bt[i] > qt:
            flag = False
            rem_bt[i] -= qt
            t += qt
            ghcr.append(pro[i])

        else:
            t = t + rem_bt[i]
            ct.append(t)

            if rem_bt[i] != 0:
                ghcr.append(pro[i])
            rem_bt[i] = 0



    if flag == True:
        break

print("\n\n\n\nCompletion time =", ct.pop())
print("\n Gantt Chart")
for i in range(len(ghcr)):
    print(" --->P"+str(ghcr[i]), end="")



