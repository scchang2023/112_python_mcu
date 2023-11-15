i=1
sum=0
f1=open("file2.txt","w")
with open("file1.txt","r") as f:
    contents=f.readlines() 
    for content in contents:
        f1.write(f"{i} {content}")        
        i+=1
        sum+=len(content)
    f1.write(f"Total:{sum}")        
f1.close()    
