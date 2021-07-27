for _ in range (int(input())):
    a,b=set(input().upper()),set(input())
    if(b.issubset(a)):
        print("YES")
    else:
        print("NO")
