l1=[1,2]
l2=[4,3]
l3=l1+l2
l3.sort()
if len(l3)%2==0:
    print((l3[int(len(l3)/2)-1]+l3[int(len(l3)/2)])/2)
else:
    print(l3[int((len(l3)+1)/2)-1])