# If else statement in python
num1 = 50
num2 = 150
if num1 > num2:
    print(num1,"is greater than",num2)
elif num2 > num1:
    print(num2,"is greater than",num1)
else:
    print("Both numbers are equal")

num3 = 700
num4 = 500
if num3 > num4:
        print(num3,"is greater",num4)

# Multiple statements in one line
w = 6; l=14
print("area of rectangle",w*l)

# The return statement
def addition(num1,num2):
     return num1+num2
result =addition(30,40)
print(result)

# Exercise 1: Calculate the multiplication and sum of two numbers
# Given two integer numbers return their product only if the product is equal to
# or lower than 1000, else return their sum.

def multiplication_sum(num3,num4):
     product = num3 * num4
     if product <= 1000:
          return product
     else:
          return num3 + num4
     
result = multiplication_sum(30,50)
print(result)

result = multiplication_sum(20,34)
print(result)


# Exercise 2: Print the sum of the current number and the previous number
# Write a program to iterate the first 10 numbers and in each iteration, print the 
# sum of the current and previous number.

previous_num = 0
for i in range (1,10):
     sum = previous_num+1
     print(sum)

# Display numbers divisible by 5 from a list
# Iterate the given list of numbers and print only those numbers which are divisible by 5

# Given list is [10,20,33,46,55]

lists = [10,20,33,46,55]
for list in lists:
     if list % 5 == 0:
          print(list)

#  Return the count of a given substring from a string
# Write a program to find how many times substring “sea” appears in the given string.

sentence = "she sells sea shells at the sea shores"
const = sentence.count("sea")
print(const)

# Dictionary Exercise
#  Convert two lists into a dictionary
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

keys = ["Ten","Twenty","Thirty"]
values = [10,20,30]

# dict()--creates a dictionary
# zip()--Used to aggregate two lists

dictionary = dict(zip(keys,values))
print(dictionary)

# Merge two Python dictionaries into one
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict1 = {"Ten":10,"Twenty":20,"Thirty":30}
dict2 = {"Thirty":30,"Fourty":40,"Fifty":50}

dict3 = {**dict1,**dict2}
print(dict3)

# Initialize dictionary with default values
# Given:
# workers = ['Lynet', 'Irene']
# defaults = {"designation": 'Developer', "salary": 8000}

workers = ["Lynet","Irene"]
defaults = {"designation":"Developer","salary":60000}

# fromkeys creates a new dictionary from the given sequence of elements with the 
# elements given by the user.

newdict = dict.fromkeys(workers,defaults)
print(newdict)

# Delete a list of keys from a dictionary
# # sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }

# # Keys to remove
# keys = ["name", "salary"]

dictionary_main ={"name":"Kelly","age":25,"salary":8000,"city":"New york"}

# pop()removes the item with the specified key name

dictionary_main.pop("name","salary")
print(dictionary_main)

# popitem
dictionary_main.popitem
print(dictionary_main)

# Check if a value exists in a dictionary
# Write a Python program to check if value 200 exists in the following dictionary.
# sample_dict = {'a': 100, 'b': 200, 'c': 300}

sample_dict = {"a":100,"b":200,"c":300}
if 200 in sample_dict.values():
     print("200 is present in the dictionary")



          
         

