f=open("Q4.txt","r")
f1=open("delhi.txt","w")
f2=open("shimla.txt","w")
f3=open("other.txt","w")
data=f.read()
data1=data.split("\n")
print(data1)
for i in range(0,len(data1)):
    if "delhi"in data1[i]:
        f1.write(data1[i])
        f1.write("\n")
    if"shimla"in data1[i]:
        f2.write(data1[i])
        f2.write("\n")
    if "delhi" not in data1[i]and "shimla"not in data1[i]:
        f3.write(data1[i])
        f3.write("\n")
f1.close()
f2.close()
f3.close()
f.close()



