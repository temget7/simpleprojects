s=input("enter a word:")
S=s[::-1]
list=[]
for i in range(len(s)+1):
    for j in range(len(s)+1):
        if s[i:j]==S[len(s)-j:len(s)-i] and len(s[i:j])!=0 and len(s[i:j])!=1:
            list.append(s[i:j])
if len(list)!=0:
    print(max(list))
else:
    print("no palindromic content")