def findingwt(processes,n,bt,wt):
    wt[0] = 0
    for i in range(1,n):
        wt[i] = bt[i-1]+wt[i-1]
def findtat(processes,n,bt,wt,tat):
    for i in range(n):
        tat[i] = bt[i]+wt[i]
def findavgtime(processes,n,bt):
    wt = [0]*n
    tat = [0]*n
    total_tat =0
    total_wt = 0
    findingwt(processes,n,bt,wt)
    findtat(processes,n,bt,wt,tat)
    print("processes time - burst time - waiting time - turn around time ")
    for i in range(n):
        total_wt = total_wt+wt[i]
        total_tat+=tat[i]
        print(""+str(i+1)+"\t\t"+str(bt[i])+"\t\t"+str(wt[i])+"\t\t"+str(tat[i]))
    print("average waiting time = "+str(total_wt/n))
    print("average turnaround time = "+str(total_tat/n))
if __name__=="__main__":
    processes = [1,2,3]
    n = len(processes)
    bursttime = [24,3,6]
    findavgtime(processes,n,bursttime)