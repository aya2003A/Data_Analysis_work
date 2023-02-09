
dictionary={
}
total = 0
count=0
fileIn = open(r"C:\\Users\alaa\Downloads\grades.txt")
for i in fileIn :
  listt=i.split()
  ID=int(listt[0])
  name=listt[1]
  score=int(listt[2])
  birth=int(listt[4])
  gender=listt[6]
  dictionary[i]={
      ID:'ID',
      'name':name,
      'score':score,
      'birth':birth,
      'gender':gender
      }
print(dictionary)
fileIn.close()

