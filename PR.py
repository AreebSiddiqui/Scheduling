
print("\t\t\t\t\t\t\t\t Priority Scheduling Algorithm \n\t\t\t\t\t\t\t\t\t\t(Non Preemptive)")
bt = []   # BurstTime
at = []   # Arrival time
ct = []   # Completion time
wt = []   # Waiting time
tat = []  # TurnAround time
pro = []  # Processes
pri = []  # Priority
stat = 0
m = 0

n = int(input("Enter Number of processes:"))

for i in range(0, n):
    pro.insert(i, i+1)
# Arrival-Time-Input
at = int(input("Enter Arrival Time:"))
# Priority-time-Input
pri = list(map(int, input("Enter Priority :").strip().split()))

# Burst-time-Input
bt = list(map(int, input("Enter Burst Time:").strip().split()))

# BT-PR-PROCESS-sorted
for i in range(0, len(pri)):
    for j in range(0, len(pri)-1):
        if pri[j] > pri[j+1]:
            temp = pri[j]
            pri[j] = pri[j + 1]
            pri[j + 1] = temp

            temp = bt[j]
            bt[j] = bt[j + 1]
            bt[j + 1] = temp

            temp = pro[j]
            pro[j] = pro[j + 1]
            pro[j + 1] = temp


# Completion-Time
for i in range(0, n):
    stat = stat+bt[i]
    ct.insert(i, stat)

# TurnAround-Time
for i in range(0, n):
    tat.insert(i, ct[i] - at)


print("\nProcess\t\tArrival Time\tPriority\tBurst Time\tCompletion Time\t TurnAround Time  ")
for i in range(n):
    print(str(pro[i]) + "\t\t\t" + str(at) + "\t\t\t\t" + str(pri[i]) + "\t\t\t" + str(bt[i]) + "\t\t\t" + str(ct[i]) + "\t\t\t\t " + str(tat[i]))

    Avgct = + ct[i]
    Avgtat = + tat[i]
    Avgct = float(Avgct/n)
    Avgtat = float(Avgtat/n)

print("Average Completion Time is:", Avgct)
print("Average Turnaround Time is:", Avgtat)

print("\nGantt Chart")
for i in range(len(pro)):
    print(" --->P"+str(pro[i]), end="")





