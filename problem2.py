#Non-unique Elements--The task was take any list and return only the non-unique values of that list. The checkio function gets that solution.
import collections

def test():
   list = [1,1,6,6,2,4,5,6,0,0,10,11,15]
   i = collections.Counter(list) #Creates a dictionary with key:value pairs with the key being the element and the value being how often that element appears
   return [x for x in i if i[x] > 1] #If key value is > 1 (meaning it's a duplicate), return an array of element i 
   #Returns which values have duplicates

def checkio(data):
   x = collections.Counter(data) #Creates a dictionary with key:value pairs with the key being the element and the value being how often that element appears
   y = [i for i in x if x[i] > 1] #If key value is > 1 (meaning it's a duplicate), return an array of element i 
   duplist = [a for a in data if a in y] #If element is found in data (the list), and found to be a duplicate in y, becomes an array of ALL the values minus those that are not duplicates
   return duplist #Returns only the non-unique values 

print checkio([1,2,3,1,3])
