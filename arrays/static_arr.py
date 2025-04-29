import random

myarray = [1,3,5]
random_index = random.randint(0,len(myarray)-1)

print(myarray[random_index])

# iterate using for and while loop

for i in range(len(myarray)):
    print(myarray[i])

i = 0
while i < len(myarray):
    print(myarray[i])
    i+=1

# Remove from the last position in the array if the array
# is not empty (i.e. length is non-zero).
def removeEnd(arr, length):   
    # Overwrite last element with some default value.
        # We would also consider the length to be decreased by 1.
        arr[length-1] = 0
        length -=1

# Remove value at index i before shifting elements to the left.
# Assuming i is a valid index.
def removeMiddle(arr, i, length):
    # iterate thorugh arr starting from i + 1
    # shift left by acessing left val i-1 with current i then assiging i-1 to i
    for i in range(i+1,len(arr)):
         arr[i-1] = arr[i]
    
    arr[len(arr)-1] = 0
    length -=1

# Insert n into arr at the next open position.
# Length is the number of 'real' values in arr, and capacity
# is the size (aka memory allocated for the fixed size array).
def insertEnd(arr, n, length, capacity):
    # insert n value to length - 1 index of arr if length is less than capacity
    if length < capacity:
         arr[length-1] = n

# Insert n into index i after shifting elements to the right.
# Assuming i is a valid index and arr is not full.
def insertMiddle(arr, i, n, length):
   # iterate through arr reverse, from that index access i + 1 then assign it to i value
    for i in range(length-1, i -1, -1):
        arr[i+1] = arr[i]
    arr[i] = n 

print("Test removeEnd")
myarray = [1,8,11,56,90,78,100]
removeEnd(myarray, len(myarray))
print(myarray)

print("Test removeMiddle")
myarray = [1,8,11,56,90,78,100]
removeMiddle(myarray,4,len(myarray))
print(myarray)

print("Test insertEnd")
myarray = [1,8,11,56,90,78,100, None]
insertEnd(myarray,1000,len(myarray),1000)
print(myarray)

print("Test insertMiddle")
myarray = [1,8,11,56,90,78,100,None]
insertMiddle(myarray,0,-1,7)
print(myarray)