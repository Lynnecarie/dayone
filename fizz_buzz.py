def fizz_buzz(t):
  if t%3==0 and t%5==0:
    return "FizzBuzz"
    
  elif t%3==0 and t%5!=0:
    return "Fizz"
    
  elif t%3!=0 and t%5==0:
    return "Buzz"
    
  else:
    return t
      
    
