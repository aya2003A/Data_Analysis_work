#lst=[]
#lst=list(map(int,input().split()))
#for i in range(0,len(lst)):
dic ={
      
}
#f = open("C:\\Users\alaa\Downloads\grades.txt", "r")
with open(r'C:\\Users\alaa\Downloads\grades.txt') as f: 
  lines = f.readlines() 
file_dict = {} 
for line in lines: 
  key, value = line.split(':') 
  key = key.strip() 
  value = value.strip() 
  file_dict[key] = value  
print(file_dict) 
