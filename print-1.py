inp1=int(input())
inp2=list(map(int,input().split()))
inp3=[]
for i in range(len(inp2)):
    if i==inp2[i]:
        inp3.append(i)
        
if len(inp3)>=1:
    print(*inp3)
else:
    print(-1)
