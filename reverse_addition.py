l1=[1,2]
l2=[4,3]
l4=[]
c=0
b=0
for i in range(len(l1)):
    c=c+l1[len(l1)-(i+1)]*(10**(len(l1)-(i+1)))
for j in range(len(l2)):
    b=b+l2[len(l2)-(j+1)]*(10**(len(l2)-(j+1)))
l3=list(str(c+b))
for k in range(len(l3)):
    l4.append(int(l3[len(l3)-(k+1)]))
print(l4)
