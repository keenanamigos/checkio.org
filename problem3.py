#Median

def test():
   numbers = [1,2,3,4,5]
   list = sorted(numbers)
   if len(list) < 1:
      return None
   if len(list) % 2 == 1:
      return list[len(list)//2]
   else:
      highnum = list[len(list)//2]
      lownum =  list[len(list)//2-1]
      return (highnum + lownum)/2.0 #Allow for floats

def checkio(data):
   list = sorted(data) #Need to sort the list in order to eventually find the median
   if len(list) < 1:
      return None
   if len(list) % 2 == 1:
      return list[len(list)//2] #Will round up to the correct number because it returns an int (keeps the indicies as ints)
   else:
      highnum =  list[len(list)// 2] #Keeps list indices as ints, returns "higher" number to be added then divided
      lownum = list[len(list)// 2-1] #Keeps list indices as ints, returns "lower" number to be added then divided
      return (highnum + lownum)/ 2.0 #Will be able to return floats for the even values



      
      
 
 
