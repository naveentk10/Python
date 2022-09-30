def count(n):
    m=n.lower()
    ar=list(m)
    print(ar)
    x=0

    for i in ar:
        if i == "a" or i=="e" or i=="i" or i=="o" or i=="u": 
            x=x+1

    print(x)


word= input ("Enter a word :\n")
count(word)




