=>  key-value pair
=> dictionary is the collection of key-value pairs where the value can be any python object 
	whereas the keys are the immutable python object, i.e., Numbers, string or tuple.

emp = {"Name": "Manish", "Age": 35, "salary":25000,"Company":"GOOGLE"}  

emp = {"name":"Manish","age":35,"company":"Google"}
print(emp)
print(emp["name"]) = > Manish

emp["name"] = "Singh"
{'name': 'Singh', 'age': 35, 'company': 'Google'}

## iterarting over Dictionary
emp = {"name":"Manish","age":35,"company":"Google"}
for x in emp:  
    print(x);  
 =>name
age
company

for x in emp:
    print(emp[x])

Singh
35
Google

for x in emp.values():
    print(x)
 Singh
35
Google

for x in emp.items():
    print(x)

 ('name', 'Singh')
('age', 35)
('company', 'Google')

for x,y in emp.items():
    print(x,y)

name Singh
age 35
company Google




