
s=input()
a=""
if s==" " or len(s)==1 :
    print("true")
else :
    for i in range(len(s)):
       if s[i].isalpha() or s[i].isdigit():
          a+=s[i]
    if len(a)%2==0 :
        split1=a[0:len(a)//2]
        tmp=a[len(a)//2:]
        split2=tmp[::-1]
    else :
        split1=a[0:len(a)//2]
        tmp=a[(len(a)//2)+1:]
        split2=tmp[::-1]
    if(split1.lower()==split2.lower()):
         print("true")
    else:
         print("false")
