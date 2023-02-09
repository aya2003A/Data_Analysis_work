
              
    
    
lst=[]
sub_great=[]
sub_small=[]
greatest=0
smallest=0
count=0
lst=list(map(int,input().split()))
for i in range(0,len(lst)):
   if lst[i]>=0 :
       sub_great.append(lst[i])
       greatest=greatest+int(lst[i])
   else:
       sub_small.append(lst[i])
       smallest=smallest+lst[i]
       
lst.sort()       
if len(sub_small)<2:
    sub_small.append(lst[1])
    smallest=smallest+int(lst[1])
if len(sub_great)<2:
    sub_great.append(lst[-2])
    greatest=greatest+int(lst[-2])   

print(sub_great,"(",greatest,")")
print(sub_small,"(",smallest,")")
    
   
