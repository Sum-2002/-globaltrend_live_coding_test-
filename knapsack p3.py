def knapsack(wt,val,w,n):
    if n==0 or w==0:
        return 0
    if t[n][w] != -1:
        returnt[n][w]

    if wt[n-1]<=w:
        t[n][w]=max(val[n-1]+knapsack(wt,val,w-wt[n-1],n-1),knapsack(wt,val,w,n-1))
        return t[n][w]


weight = [1, 2, 3]
values= [10, 15, 40]
capacity= 6
n=len(values)
t=[[-1 for i in range(capacity + 1)]for j in range(n+1)]
print(knapsack(weight,values,capacity,n))
