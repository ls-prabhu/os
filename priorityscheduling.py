def findwt(p,n,wt):
    wt[0]=0
    for i in range(1,n):
        wt[i] = p[i-1][1]+wt[i-1]
def findtat(p,n,wt,tat):
    for i in range(n):
        tat[i] = p[i][1]+wt[i]
def avgtime(p,n):
    wt = [0]*n
    tat = [0]*n
    totwt = 0
    tottat = 0
    findwt(p,n=n,wt=wt)
    findtat(p,n,wt,tat)
    print(wt)
    print("processes\t|burst time\t|waiting time\t|turn around time")
    print("-"*65)
    for i in range(n):
        totwt += wt[i]
        tottat += tat[i]
        print(p[i][0],"\t\t|",p[i][1],"\t\t|",wt[i],"\t\t|",tat[i])
    print("average waiting time :", round(totwt/n,2))
    print("average turnarround time :", round(tottat/n,2))
def psec(lst):
    n = len(lst)
    print("available processes\n",[i for i in lst],"\t")
    lst = sorted(lst,key=lambda lst:lst[2],reverse=True)
    print("sorted based on priority processes\n",[i for i in lst],"\t")
    avgtime(lst,n)
if __name__ == "__main__":
    processes = [[1,10,1],[2,5,0],[3,8,1]]
    print("priority scheduling ")
    psec(processes)