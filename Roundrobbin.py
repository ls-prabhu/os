def findwt(processes,n,bt,wt,quantum):
    rem_bt = [0]*n
    for i in range(n):
        rem_bt[i]=bt[i]
    t = 0
    while(1):
        done = True
        for i in range(n):
            if(rem_bt[i]>0):
                done = False
                if(rem_bt[i]>quantum):
                    t+=quantum
                    rem_bt[i] = quantum
                else:
                    t = t+rem_bt[i]
                    wt[i] = t-wt[i]
                    rem_bt[i] = 0
        if done:
            break
def findtat(processes,n,bt,wt,tat):
    for i in range(n):
        tat[i] = bt[i] + wt[i]
def findavgtime(processes,n,bt,quantum):
    wt =[0]*n
    tat = [0]*n
    findwt(processes,n,bt,wt,quantum)
    findtat(processes,n,bt,wt,tat)
    totalwt = 0
    totaltat = 0
    print("processes\t|burst time\t|waiting time\t|turn around time")
    print("-"*65)
    for i in range(n):
        totalwt+=wt[i]
        totaltat+=tat[i]
        print(i+1,"\t\t|",bt[i],"\t\t|",wt[i],"\t\t|",tat[i])
    print(f"Average waiting time = %.5f"%(totalwt/n))
    print(f"Average turnaround time = %.5f"%(totaltat/n))
if __name__ == "__main__":
          process = [1,2,3]
          n = len(process)
          burst_time = [24,3,3]
          quantum= 4
          findavgtime(process,n,burst_time,quantum)