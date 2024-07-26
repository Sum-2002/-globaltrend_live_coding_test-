def lcs(x,y,m,n):
    l=[[0 for i in range (n+1)]for j in range (m+1)]
    for i in range (m+1):
        for j in range (n+1):
            if i==0 or j==0:
                l[i][j]=0
            elif x[i-1]==y[j-1]:
                l[i][j]=l[i-1][j-1]+1
            else:
                l[i][j]=max(l[i-1][j],l[i][j-1])
        

    lcs=""
    i=m
    j=n
    while i>0 and j>0:
        if x[i-1]==y[j-1]:
            lcs += x[i-1]
            i -= 1
            j -= 1
        elif l[i-1][j]>l[i][j-1]:
             i -= 1
        else:
             j -= 1
    lcs=lcs[::-1]
    print(lcs)

x="abcde"
y="ace"
m=len(x)
n=len(y)
lcs(x,y,m,n)
