l=[]
for i in range (4):
    l.append(input())
if((l[2]=="Rock" and l[3]=="Scissor") or (l[2]=="Scissor" and l[3]=="Paper") or (l[2]=="Paper"and l[3]=="Rock")):
    print(l[0],"Win")
else:
    print(l[1],"Win")
