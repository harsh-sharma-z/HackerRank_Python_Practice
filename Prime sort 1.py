def isprime(n):
    if(n==0 or n==1):
        return False
    else:
        count=0
        for i in range(2,n):
            if(n%i==0):
                count+=1
        if(count==0):
            return True
        else:
            return False
        
        
    
s=eval(input())
prime=""
notprime=""
for i in range (0,len(s)):
    if(isprime(int(s[i]))):
        prime=prime+s[i]
    else:
        notprime=notprime+s[i]
prime = ''.join(sorted(prime))
print('"',prime+notprime,'"',sep="")
    
    
