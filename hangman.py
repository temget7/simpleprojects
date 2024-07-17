import random
word=[]
redlist=[]
new=[]
for i in range(6):
    a=random.randrange(65,91)
    word.append(chr(a))
    new.append('__')
print(word)
for i in range(12):
    letter=input('guess a letter(must be capital):')
    if letter in word:  
        for j in range(6):
            if word[j]==letter:
                new.pop(j)
                new.insert(j,letter)
                print(new)
        if new==word:
            print('🥳🥳🥳congratulations you have leveled up🥳🥳🥳')
            break
    elif len(redlist)<6:
        redlist.append(letter)
        print('REDLIST=',redlist)
    elif len(redlist)==6:
        print('game over,try again')
        break     
                
        