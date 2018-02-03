while True:
    data = input().split(" ")
    data.sort()
    a,b,c = list(map(lambda x: int(x),data))[:]
    print(a,b,c)
    if (a + b) <= c:
        print("No")
    else:
        d = a * a + b * b
        cc = c*c
        if d < cc:
            print("Obtuse")
        elif d == cc:
            print("Right")
        else:
            print("Acute")
            
