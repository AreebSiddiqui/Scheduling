
print("\t\t\t\t\t\t\t\tSJF Scheduling Algorithm \n\t\t\t\t\t\t\t\t\t(Non Preemptive)")

at = []  # Arrival time
ct = []  # Completion time
wt = []  # Waiting time
tat = []  # TurnAround time
pro = []  # Processes
stat = 0
m = 0

n = int(input("Enter Number of processes:"))

for i in range(0, n):
    pro.insert(i, i+1)
# Arrival-Time-Input
at = int(input("Enter Arrival Time:"))
# Burst-time-Input
bt = list(map(int, input("Enter Burst Time:").strip().split()))


# Arrival-Time-Sorted
bt.sort()

# Completion-Time
for i in range(0, n):
    stat = stat+bt[i]
    ct.insert(i, stat)

# TurnAround-Time
for i in range(0, n):
    tat.insert(i, ct[i] - at)

print("\nProcess\t\tArrival Time\tBurst Time\tCompletion Time\t TurnAround Time  ")
for i in range(n):
    print(str(pro[i]) + "\t\t\t" + str(at) + "\t\t\t\t" + str(bt[i]) + "\t\t\t" + str(ct[i]) + "\t\t\t\t " + str(tat[i]))

    Avgct = + ct[i]
    Avgtat = + tat[i]
    Avgct = float(Avgct/n)
    Avgtat = float(Avgtat/n)

print("Average Completion Time is:", Avgct)
print("Average Trunaround Time is:", Avgtat)





