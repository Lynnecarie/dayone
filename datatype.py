def data_type(m): 
    
  if m == None:
    return 'no value'
  
  if type(m)==str:
    return len(m)
    
  elif type(m)==bool:
    return m
  
  elif type(m)==int:
    if m < 100:
      return 'less than 100'
      
    elif m > 100:
      return 'more than 100'
      
    else:
      return 'equal to 100'
      
  elif type(m)==list:
    if len(m)<3:
      return None
    
    else:
      return m[2]