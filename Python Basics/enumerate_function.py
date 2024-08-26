# The enumerate function is a built-in function in Python that allows you to loop over a sequence (such as a list, tuple, or string) and get the index and value of each element in the sequence at the same time. Here's a basic example of how it works:



# # Loop over a list and print the index and value of each element
# fruits = ['apple', 'banana', 'mango']
# for fruit in fruits:
#     print(fruit,fruit[0])

fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits):
    print(index, fruit)


## if we prefer to get the index number without the enumerate function

fruits = ['apple', 'banana', 'mango']
index = 0
for fruit in fruits:
    print(index, fruit)
    index+=1

# Loop over a list and print the index (starting at 1) and value of each element
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)



 

