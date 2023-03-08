 
n=int(input("The number of flips: "))
H_T=input("Head or Tail? ")
if(H_T=="Tail".lower()):
    numOfTail=int(input("The number of tail appearance: "))
    probOfTail=float(input("The probability of tail (< 1) :" ))
    p=1
    if(numOfTail==n or probOfTail==1 ):
        for i in range(n):
            p*=probOfTail
        print("The answer is: ",p)
    else :
       for i in range(numOfTail):
           p*=probOfTail
       for i in range(n-numOfTail):
           p*=(1-probOfTail)
       print("The answer is: ",n*p)
else:
    numOfHead=int(input("The number of head appearance: "))
    probOfHead=float(input("The probability of head (< 1) :" ))
    p=1
    if(numOfHead==n or probOfHead==1 ):
        for i in range(n):
            p*=probOfHead
        print("The answer is: ",p)
    else :
        for i in range(numOfHead):
           p*=probOfHead
        for i in range(n-numOfHead):
           p*=(1-probOfHead)
        print("The answer is: ",n*p)

