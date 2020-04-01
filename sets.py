=> unordered collection of various items
=> elements of the set can not be duplicate
=> there is no index attached to the elements of the set


Days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}  

## Add 
Months = {"January","February", "March", "April", "May", "June"}
Months.add("July") => Add one item in set 


Months = {"January","February", "March", "April", "May", "June"}
Months.update(["Sep","Oct"])

## Removing set values 
Months = set(["January","February", "March", "April", "May", "June"])  
Months.discard("January") // Months.remove("January") => Removes item from set

Months.clear()   => Clears all items from set

## Union operation

Days1 = {"Monday","Tuesday","Wednesday","Thursday"}  
Days2 = {"Friday","Saturday","Sunday"}  
print(Days1|Days2)
{'Thursday', 'Tuesday', 'Friday', 'Wednesday', 'Monday', 'Saturday', 'Sunday'}

print(Days1.union(Days2))
{'Thursday', 'Tuesday', 'Friday', 'Wednesday', 'Monday', 'Saturday', 'Sunday'}

## Intersection 

s1= {"Manish","Kumar","Singh"}
s2 = {"Manish"}
print(s1&s2)
print(s1.intersection(s2))
{'Manish'}

## Difference 
Days1 = {"Monday",  "Tuesday", "Wednesday", "Thursday"}  
Days2 = {"Monday", "Tuesday", "Sunday"}
print(Days1-Days2)
print(Days1.difference(Days2))
{'Thursday', 'Wednesday'}


## FrozenSets
=>the items of the frozen set can not be changed
=> The elements of the frozen set can not be changed after the creation
=> We cannot change or append the content of the frozen sets by using the methods like add() or remove().

Frozenset = frozenset([1,2,3,4,5])   

Frozenset.add(6)  => gives an error .


