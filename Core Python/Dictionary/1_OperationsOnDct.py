"""
Agenda:
    # How to create Dictionary?
    # How to access data from the dictionary?
    # How to update dictionaries?
    # How to delete elements from dictionary?

"""

# How to create Dictionary?

d = {} 
# d = dict()

# we are creating empty dictionary. We can add entries as follows
d[100] = "durga"
d[200] = "ravi"
d[300] = "shiva"

print(d) #{100: 'durga', 200: 'ravi', 300: 'shiva'}
print(d[100]) # durga

# d={key:value, key:value}



# How to access data from the dictionary?

# We can access data by using keys.

d = {100: 'durga', 200: 'ravi', 300: 'shiva'}
print(d[100])  #durga
print(d[200]) #shiva

# If the specified key is not available then we will get KeyError
# print(d[400]) # KeyError: 400

# We can prevent this by checking whether key is already available or not by using 
# has_key() function or by using in operator.

# d.has_key(400) ==> returns 1 if key is available otherwise returns 0

# Q. Write a program to enter name and percentage marks in a dictionary and 
# display information on the screen
"""

rec = {}
n = int(input("enter number of students: "))
i = 1
while i <=n:
    name = input("Enter student Name: ")
    marks = int(input("Enter the marks: "))
    rec[name] = marks
    i+=1

print(rec)

for x in rec:
    print("\t",x, "\t\t",rec[x])
"""



# How to update dictionaries?

# d[key] = value 
"""
- If the key is not available then a new entry will be added to the dictionary with the 
    specified key-value pair
- If the key is already available then old value will be replaced with new value.
"""

d = {100: 'durga', 200: 'ravi', 300: 'shiva'}
print(d)

d[400] = "pawan"
print(d)

d[100] = "sunny"
print(d)


# How to delete elements from dictionary?

"""
del d[key]
 - It deletes entry associated with the specified key.
 - If the key is not available then we will get KeyError
"""

d={100:"durga",200:"ravi",300:"shiva"}
print(d) # {100: 'durga', 200: 'ravi', 300: 'shiva'}

del d[100]
print(d) #{200: 'ravi', 300: 'shiva'}

del d[400]
print(d) #KeyError: 400