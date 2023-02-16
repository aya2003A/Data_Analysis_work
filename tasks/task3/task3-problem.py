def mean(lst):
    summ = sum(lst)
    mean = summ /len(lst)
    return mean
def median(lst):

    lst.sort()
    if len(lst) % 2 == 0:
        median1 = lst[len(lst) //2]
        median2 = lst[len(lst) //2 - 1]
        median = (median1 + median2)/2
    else:
        median = lst[len(lst) //2]
    return median
    
def mode(lst):
    frequency={}
    for i in lst:
        frequency.setdefault(i,0)
        frequency[i]+=1
    mod=max(frequency.values())
    mod_lst=[]
    if(mod==1):
       return "there is no mode"
    else:
       for value,freq in frequency.items():
            if freq==mod :
                mod_lst.append(value)
       return mod_lst
    
lst=[]
lst=list(map(int,input().split()))
a=mean(lst)
b=median(lst)
c=mode(lst)
print('mean : ',a)
print('median : ',b)
print('mode : ',c)