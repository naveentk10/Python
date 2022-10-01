import string


def count(x):
    if type(x)== str:
        lst=list(x)
        print(lst)
        a=0
        b=0
        for i in lst:
            if i=='x' or i=='X':
                a=a+1
            elif i=='o' or i=='O':
                b=b+1
    
        print(a,b)
        print (a==b)
    else:
        print("Enter a string ")


word=input("Enter a word: \n")
print(type(word))
count(word)
