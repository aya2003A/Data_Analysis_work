n=int(input())
listt=[]
for i in range(0,n):
    ele=input()
    listt.append(ele)
symmetric= True
j=n
for i in range(0,int(n/2)):
   if listt[i]!=listt[j-1]:
       symmetric= False
       break
   j=j-1

print(symmetric)