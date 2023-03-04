
n=int(input())
lst=list(map(int,input().split()))
score1=0
score2=0
num="1"
indexFirstRight=0
indexFirstLeft=-1
for i in range(len(lst)):
    score='score'
    score=score+num
    if(score=='score1'):
        if(lst[indexFirstRight]>lst[indexFirstLeft]):
              score1+=lst[indexFirstRight]
              indexFirstRight+=1
        else:
              score1+=lst[indexFirstLeft]
              indexFirstLeft-=1
    else:
        if(lst[indexFirstRight]>lst[indexFirstLeft]):
              score2+=lst[indexFirstRight]
              indexFirstRight+=1
        else:
              score2+=lst[indexFirstLeft]
              indexFirstLeft-=1 
    if(num=='2'):
        num='1'
        continue
    else :
        num='2'

print(score1,score2)