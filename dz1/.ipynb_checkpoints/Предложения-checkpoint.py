with open("input.txt", encoding='utf-8') as f:
    scale = f.read()
    count=1
    for i in range(len(scale)-1):
        if (scale[i]=='!' or scale[i]=='?' or scale[i]=='.' ) and (scale[i+1]==' '):
            count+=1
    print(count)
