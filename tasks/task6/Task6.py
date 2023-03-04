import numpy as np

problem1=np.diag([9,9,9])

even=np.arange(2,33,2)
problem2=np.reshape(even,(4,4))
upperbound=np.mean(problem2)+0.5*np.std(problem2)
lowerbound=np.mean(problem2)-0.5*np.std(problem2)
st=[]
for i in range(4):
      for j in range(4):
          if problem2[i][j]>=lowerbound and problem2[i][j]<=upperbound:
               st.append(problem2[i][j])
           
problem3=np.zeros((9,9),dtype=int)

n=int(input())
a=np.indices((n+1,n+1))
a=a[1]
problem4=a[1:, 1:]

print(problem1,'\n')
print(problem2,'\n')
print(st,'\n')
print(problem3,'\n')
print(problem4)