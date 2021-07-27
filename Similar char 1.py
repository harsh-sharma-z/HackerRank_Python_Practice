len,s,q=int(input()),input(),int(input())
for i in range (q):
    p=int(input())
    c=0
    for i in range (p-1):
        if(s[p-1]==s[i]):
            c+=1
    print(c)
        
