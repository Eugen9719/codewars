def is_valid_walk(walk):
    k=[0,0]
    for i in walk:
        if i == 'n':
            k[0] +=1
        elif i == 's':
            k[0]-=1
        elif i == 'w':
            k[1]+=1
        else:
            k[1]-=1

    return  k[0]==0 and k[1]==0 and len(walk) ==10








print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s'])) # True,
print(is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e'])) # False
print(is_valid_walk(['w'])) # False,
print(is_valid_walk(['n','n','n','s','n','s','n','s','n','s']))# False,