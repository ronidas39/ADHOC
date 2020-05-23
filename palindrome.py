a=input("please enter")
b=reversed(a)
y=list(b)
#print(b)
x=list(a)
b="".join(xx for xx in y)
final_list=[]

def check_word(word_check):
    rev_word=reversed(word_check)
    if(list(word_check)==list(rev_word)):
        return 1
    else:
        return 2
    
found=0
#print(len(x))
m=0
for k in range(len(x)):
 
 if(found==1):
    break
 for i in range(0,len(x)+1,2):
    if(i==0):
     #print(i)
     word=a[m:k+1]+a
     word=word.casefold()
     #print(word)
     o=check_word(word)
     if(o==1):
         #print(f"found with {word}")
         final_list.append(word)
         
         found=1
         break
     
    elif (i==len(x)):
        #print(i)
        word=a[:]+a[m:k+1]
        word=word.casefold()
        #print(word)
        o=check_word(word)
        if(o==1):
         #print(f"found with {word}")
         final_list.append(word)
         found=1
         break
    else:
        #print(i)
        word=a[:i]+a[m:k+1]+a[i:]
        #print(word)
        word=word.casefold()
        o=check_word(word)
        if(o==1):
         #print(f"found with {word}")
         final_list.append(word)
         found=1
         break

         
m=0
for k in range(len(y)):
 if(found==1):
  break
 for i in range(0,len(y)+1,2):
    if(i==0):
     #print(i)
     word=b[m:k+1]+a
     word=word.casefold()
     #print(word)
     o=check_word(word)
     if(o==1):
         #print(f"found with {word}")
         final_list.append(word)
         found=1
         break
     
    elif (i==len(x)):
        #print(i)
        word=a[:]+b[m:k+1]
        word=word.casefold()
        #print(word)
        o=check_word(word)
        if(o==1):
         #print(f"found with {word}")
         final_list.append(word)
         found=1
         break
    else:
        #print(i)
        word=a[:i]+b[m:k+1]+a[i:]
        #print(word)
        word=word.casefold()
        o=check_word(word)
        if(o==1):
         #print(f"found with {word}")
         final_list.append(word)
         found=1
         break
if(len(final_list)>1):
    if(len(final_list[0]) > len(final_list[1])):
     print(a[1])
    elif (len(final_list[0]) < len(final_list[1])):
     print(final_list[0])
    else:
     print(final_list)
else:
    print(final_list)
           
        
