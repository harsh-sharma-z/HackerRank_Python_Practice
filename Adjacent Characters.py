s=input()
l=len(s)
if(l%2==0):
    for i in range (0,l,2):
        print(s[i+1],s[i],sep="",end="")
else:
    print("Odd length.")
