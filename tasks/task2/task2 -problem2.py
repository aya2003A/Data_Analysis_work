
              
    
    
lst=[]
count=0
lst=list(map(int,input().split()))
for i in range(0,len(lst)):
   even = len(list(filter(lambda x: (x%2 == 0) , lst)))
print(even)
