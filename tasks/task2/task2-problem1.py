
def sortt(my_list):
    for i in range(len(my_list)):
       for j in range(i + 1, len(my_list)):

            if my_list[i] > my_list[j]:
                temp=my_list[i]
                my_list[i]=my_list[j]
                my_list[j]=temp

def f_l_app(lst,target):
    first = -1
    last = -1
    for i in range(len(lst)):
        if (target != lst[i]):
            continue
        if (first == -1):
            first = i
        last = i
 
    if (first != -1):
        print( first, last)
    else:
        print("Not Found")
    

lst=[]
lst=list(map(int,input().split()))
target=int(input())
f_l_app(lst, target)