inp1=input()
a1=[inp1[i] for i in range(len(inp1)) if i%2==0]
b1=[inp1[i] for i in range(len(inp1)) if i%2!=0]
for j in range(len(inp1)//2):
  print(b1[j]+a1[j],end="")
