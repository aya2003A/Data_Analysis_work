
n = int(input("number of element"))
listt=[] 
firsthalf=[]
sechalf=[]

for i in range(0, n):
    ele =input()
    listt.append(ele)
for i in range(0, n):
    if len(listt[i])%2==0 :
        str1=listt[i]
        str2=listt[i]
        firsthalf.append(str1[0:(len(listt[i])//2)])
        sechalf.append(str2[(len(listt[i])//2):])
    else:
        str1=listt[i]
        str2=listt[i]
        firsthalf.append(str1[0:(len(listt[i])//2+1)])
        sechalf.append(str2[(len(listt[i])//2+1):])


print(firsthalf)
print(sechalf)

