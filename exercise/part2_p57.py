import random as r

m_cnt=c_cnt=p_cnt=0
while(True):
    my=int(input("請輸入1,2,3:(0結束)"))
    if(my==0):
        break
    com=r.randint(1,3)
    print(f"電腦輸入{com}")
    if(my==com):
        p_cnt+=1
        continue
    if(my==1 and com==2):
        c_cnt+=1
        continue
    else:
        m_cnt+=1
        continue
    if(my==2 and com==3):
        c_cnt+=1
        continue
    else:
        m_cnt+=1  
        continue
    if(my==3 and com==1):
        c_cnt+=1
        continue
    else:
        m_cnt+=1  
        continue
        
print(f"我贏{m_cnt}次，電腦贏{c_cnt}次，平手{p_cnt}次")
    

