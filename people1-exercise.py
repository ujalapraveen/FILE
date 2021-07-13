f=open("people1_exercise.txt","r")
c=0
for i in (f):
    c+=1
    print(i)
    print(c)
f.close()