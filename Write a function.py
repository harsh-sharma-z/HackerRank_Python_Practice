def is_leap(year):
     if year%100!=0 and year%4==0 :
        leap=True
     elif  year%100==0 and year%400==0:
        leap=True
     else:
        leap=False
  
    
     return leap

