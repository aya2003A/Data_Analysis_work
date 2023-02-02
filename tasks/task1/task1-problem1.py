
n = int(input("number of element"))
listt=[] 
temp=[]
for i in range(0, n):
    ele = int(input())
    listt.append(ele)
for i in range(0, n):
    temp.append(0)
k= int(input())
for i in range(0,n):
    if i+k< n:
        temp[i+k]=listt[i]
    else :
            if i+k<10 :
             temp[i+1-k]=listt[i]
            else :
             temp[(i+k)%n]=listt[i]

print(temp)
        
        