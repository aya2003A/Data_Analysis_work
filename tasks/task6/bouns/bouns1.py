
row,col=list(map(int,input().split()))
x =True
for i in range(row):          # A for loop for row entries
    arr=list(input().split())
    for j in range(col):      # A for loop for column entries
         if(arr[j]=='C' or arr[j]=='M' or arr[j]=="Y"):
             x=False

if x==False:
    print("#Color")
else:
    print("#Black&White")