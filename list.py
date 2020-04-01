=> sequence of various type of data
=>  list can be defined as a collection of values or items of different types
=> Mutable
===================================================

L1 = ["John", 102, "USA"]  
L2 = [1, 2, 3, 4, 5, 6]  
L3 = ["Mallic", "Ryan"] 

print(L1) => ['John', 102, 'USA']
L1[-1] => 'USA' // reverse indexing in action
L1[0] => 'John'

# Assignment 
L1 = ["John", 102, "USA"] 
L1[0] = "Manish"
Print(L1) => ['Manish', 102, 'USA']

# Concatenation
L1 = ['Manish', 102, 'USA']
L2 = ["Singh",103,"INDIA"]
l2 = L1+L2  = > ['Manish', 102, 'USA', 'Singh', 103, 'INDIA']

# Repitation
L2 = ["Singh",103,"INDIA"]
l3 = L2*2 = > ['Singh', 103, 'INDIA', 'Singh', 103, 'INDIA']

# Del from List
L1 = ["Singh",103,"INDIA"]
del(L1[0]) => [103, 'INDIA']
##
L2 = ["Singh",103,"INDIA"]
print("Singh" in L2) prints True.

## Iterate over List
l4 = ["Manish","Singh","is","good","boy"]
for item in l4:
    print(item) 

## append() in the list  - Appends value at last 
l5 = []
l5.append("Mansih")
print(l5)
l5.append("Singh")
print(l5)

['Mansih']
['Mansih', 'Singh']

## Tuples inside list 

Employees = [(101, "Ayush", 22), (102, "john", 29), (103, "james", 45), (104, "Ben", 34)]  
for i in Employees:
    print(i)

=========================== Some useful methods===============

list.append(obj)		The element represented by the object obj is added to the list.
list.clear()			It removes all the elements from the list.
List.copy()				It returns a shallow copy of the list.
list.count(obj)			It returns the number of occurrences of the specified object in the list.
list.index(obj)			It returns the lowest index in the list that object appears.
list.insert(index, obj)	The object is inserted into the list at the specified index.
list.pop(obj=list[-1])	It removes and returns the last object of the list.
list.remove(obj)		It removes the specified object from the list.
list.reverse()			It reverses the list.
list.sort([func])		It sorts the list by using the specified compare function if given.



