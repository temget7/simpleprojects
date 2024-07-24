l5=[]
input=input("enter a word:")
for k in range(len(input)):
    if not input[k] in l5:
        l5.append(input[k])
print(l5,"length==>",len(l5))