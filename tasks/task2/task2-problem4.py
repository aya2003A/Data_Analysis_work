
ze_dict={
}
total = 0
count=0
oldest=2023
highest=-1
st=''
id_old=0
fileIn = open(r"C:\\Users\alaa\Downloads\grades.txt")
ze_lines = fileIn.read().splitlines()
for line in ze_lines:
    ze_tokens = line.split()
    #ze_dict[ze_tokens[0]] = ze_tokens[0] #id
    #ze_dict[ze_tokens[1]] = ze_tokens[1] #name
    #ze_dict[ze_tokens[2]] = ze_tokens[2] #grade
    #ze_dict[ze_tokens[3]] = ze_tokens[3] #-
    #ze_dict[ze_tokens[4]] = ze_tokens[4] #birthyear
    #ze_dict[ze_tokens[5]] = ze_tokens[5] #:
    #ze_dict[ze_tokens[6]] = ze_tokens[6] #f/m
    try :
      if ze_tokens[2] != 'N/A':
       idd=int(float(ze_tokens[0]))
       name=ze_tokens[1]
       grade=int(float(ze_tokens[2]))
       total=total+grade
       count=count+1
       birthyear=int(float(ze_tokens[4]))
       if(birthyear<oldest):
           oldest=birthyear
           id_old=idd
       gender=ze_tokens[6]
       if(grade>highest) :
           st=gender
         
       ze_dict[idd]={
        'name':name,
        'grade':grade,
        'birthyear':birthyear,
        'gender':gender
        }
    except :
        continue
    
print(ze_dict) 
score=total/count 
print("the average score",score)
print("the oldest ",id_old)
print("gender of the highest score",st)  
fileIn.close()