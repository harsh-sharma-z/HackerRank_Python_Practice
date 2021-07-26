lst=input()
lst=lst.split(' ')
a=int(lst[0])
b=int(lst[2])
c=0
for i in range (0,a):
    for j in range (0,b):
        if (i+j)%2!=0:
            c+=1
print(c)
