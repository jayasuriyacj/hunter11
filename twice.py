inp1=int(input())
a1=list(map(int,input().split()))
for i in range(len(a1)):
    if a1.count(a1[i])==1:
        print(a1[i])
