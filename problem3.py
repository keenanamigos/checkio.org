#Median
x = [1,2,3,4,5]
def test():
   numbers = [1,2,3,4]
   list = sorted(numbers)
   if len(list) < 1:
      return None
   if len(list) % 2 == 1:
      return float(list[len(list)/2])
   else:
      highnum = float(list[len(list)/2-1])
      lownum =  float(list[len(list)/2])
      return (highnum + lownum)/2

def checkio(): 
   y = [1,2,3,4,5]
   list = sorted(y)
   if len(list) < 1:
      return None
   if len(list) % 2 == 1:
      return list[(len(list)+1)/2-1]
   else:
      highnum = list[len(list)/2-1] 
      lownum =  list[len(list)/2]
      return (highnum + lownum)/2 
#Checkio didn't allow list indices to be floats
#Unfinished



      
      
 
