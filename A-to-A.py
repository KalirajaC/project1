l=['A','B','C','E','A','C']
count=0
for i in l:
    if i=='A':
        count=count+1 
        continue 
    if count==2:    
        break
    print(i) 
        