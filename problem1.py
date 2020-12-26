
import math 
def digPow(n,p):
   
   h=0
   ch=0
   l=[]
   for i in range(len(str(n))):
      
      l[i]=int(str(n)[i])
    
    for j in range(len(l)):
                  
         h+=pow(l[j],j+p)
    if h%n!=0:
      ch=-1
           
      return ch
    else :
         ch=h/n        
         return ch

        
    
