my_array = [1,2,3,4,5,6,7,8,9,0]
minVal = my_array[0]

for i in my_array:
    if i < minVal:
      minVal = i
print('The lowest ',minVal)
