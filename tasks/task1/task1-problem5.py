
n = int(input("number of element"))
listt=[] 

for i in range(0, n):
    ele =input()
    listt.append(ele)
firstindex=0
secindex=0
target=int(input())
for i in range(0, n):
    for j in range (i+1,n):
              if int(listt[i])+int(listt[j])==target:
                  firstindex=i
                  secindex=j
                  break;
print(firstindex)
print(secindex)
              
        
