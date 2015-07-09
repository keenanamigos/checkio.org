def checkio(number):
   x = number % 3 == 0
   y = number % 5 == 0
   if (x & y):
      return "Fizz Buzz"
   elif (x):
      return "Fizz"
   elif (y):
      return "Buzz"
   else:
      return (str(number))
      
