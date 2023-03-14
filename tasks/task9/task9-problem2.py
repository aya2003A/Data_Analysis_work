
#lst=[]
#lst=list(map(int,input().split(',')))
#ans=[]
#maxElement= lst[-1]
#i=len(lst)-2
#while(i>=0):
#    temp=lst[i]
#    ans.append(maxElement)
#    if(maxElement<temp):
#        maxElement=temp
#    i=i-1
#ans.reverse()
#ans.append(-1)
#print(ans)
class Solution(object):
    def replaceElements(self, arr):
        ans=[]
        maxElement= arr[-1]
        i=len(arr)-2
        while(i>=0):
            temp=arr[i]
            ans.append(maxElement)
            if(maxElement<temp):
                  maxElement=temp
            i=i-1
        ans.reverse()
        ans.append(-1)
        return ans