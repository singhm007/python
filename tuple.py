=> Tuple is used to store the sequence of immutable python objects
=> immutable and the value of the items stored in the tuple can not be changed.
=> Indexing and slicing is same like List/other collection objects

t1= ("Manish",102,"Singh")
print(t1) => ('Manish', 102, 'Singh') 
T2 = ("Apple", "Banana", "Orange")  

## Some printings 
t2 =  ("Manish","India","Bangalore")
count =0
for i in t2:
    print("Tuple[%d]= %s"%(count,i))
    count = count+1

Tuple[0]= Manish
Tuple[1]= India
Tuple[2]= Bangalore

# Item Assignment
t2 =  ("Manish","India","Bangalore")
t2[1]= "Test" => Error : 'tuple' object does not support item assignment

# Item Delition 
t2 =  ("Manish","India","Bangalore")
del(t2[0]) => TypeError : 'tuple' object doesn't support item deletion

#









