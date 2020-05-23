a=input("please enter")
b=reversed(a)
y=list(b)
print(b)
x=list(a)
b="".join(xx for xx in y)


def check_word(word_check):
    rev_word=reversed(word_check)
    if(list(word_check)==list(rev_word)):
        return 1
    else:
        return 2
    

print(len(x))
m=0
for k in range(len(x)):
 for i in range(0,len(x)+1,2):
    if(i==0):
     print(i)
     word=a[m:k+1]+a
     word=word.casefold()
     print(word)
     o=check_word(word)
     if(o==1):
         print(f"found with {word}")
     
    elif (i==len(x)):
        print(i)
        word=a[:]+a[m:k+1]
        word=word.casefold()
        print(word)
        o=check_word(word)
        if(o==1):
         print(f"found with {word}")
    else:
        print(i)
        word=a[:i]+a[m:k+1]+a[i:]
        print(word)
        word=word.casefold()
        o=check_word(word)
        if(o==1):
         print(f"found with {word}")
print("done")         
m=0
for k in range(len(y)):
 for i in range(0,len(y)+1,2):
    if(i==0):
     print(i)
     word=b[m:k+1]+a
     word=word.casefold()
     print(word)
     o=check_word(word)
     if(o==1):
         print(f"found with {word}")
     
    elif (i==len(x)):
        print(i)
        word=a[:]+b[m:k+1]
        word=word.casefold()
        print(word)
        o=check_word(word)
        if(o==1):
         print(f"found with {word}")
    else:
        print(i)
        word=a[:i]+b[m:k+1]+a[i:]
        print(word)
        word=word.casefold()
        o=check_word(word)
        if(o==1):
         print(f"found with {word}")
         
         
