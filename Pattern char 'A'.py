h=int(input())
l=int(input())

for i in range (1,(h+1)):
    if(i==l):
        for j in range (1,(2*h)):
            if((j>=(h-i+1)) and (j<=(h+i-1))):
                print("*",end="")
            else:
                print(" ",end="")
    else:
        for j in range (1,(h*2)):
            if i==1:
                if j==h:
                    print("*",end="")
                else:
                    print(" ",end="")
            else:
                if((j==(h-i+1)) or (j==(h+i-1))):
                    print("*",end="")
                else:
                    print(" ",end="")
    print("")
