import sys
dict1 = {
  "A" :[20,30,100,49],
  "B" :[00,199,201,29],
  "C" :[40,90,69,18]
 }
result=-sys.maxsize -1
p=0;
for i in dict1:
    com = max(dict1[i])-min(dict1[i])
    if result<com :
         result=com
         p=i
         
print(dict1[i])
             
