
import math 
def digPow(n,p):
   int h=0:
    l=[]
    for i in range(len(str(n))):
        l[i]=int(str(n)[i])
    
    for j in range(len(l)):
        h+=pow(l[j],j+p)
    if h%n!=0:
        return -1
    else :
        return h/n

        
    
