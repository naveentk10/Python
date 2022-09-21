def value():
    n=[]
    m=int(input("Enter the total number: "))
    print("Enter the numbers")

    for i in range(0,m):
        ls= input()
        n.append(ls)

    print (n)

    a = "1. asc"
    d = "2. desc"
    o = "3. no change"

    options = print(a,d,o)

    select = int(input("Chose any one option to process the list: "))

    if select == 1:
        x=sorted(n)
        print (x)
    elif select == 2:
        x=sorted(n,reverse= True)
        print(x)
    elif select == 3:
        print(n)
    else:
        print("invalid input")

value()

