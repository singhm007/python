


# simple functions with default values
def print_name(name="Singh"):
    print(f"My name is : {name}")

print_name("Ram") => My name is : Ram


def add_num(n1=4,n2=6):
    return n1+n2
add_num()
add_num(3)
add_num(3,5)

# Palendrome check
def check_palendrome(mystr):
    return mystr == mystr[::-1]
val = input("Input your string :")
check_palendrome(val)


# function to chweck Pig Latin
def pig_latin(mystr):
    if mystr[0] in "aeiou":
        pig_word = mystr[1:]+mystr[0]+'py'
    else:
        pig_word = mystr+'py'
    return pig_word
pig_latin("Manish")


# Check even number
def check_even(num):
    return int(num)%2==0
check_even(7)

# function which takes variable length input parameter
def myfunc(*args): => *args : This denotes variable length. Python take input in form of tuple
    length = len(args)
    for item in range(length):
        print(args[item])

myfunc(20,10,20,20)

# Function which takes variable length dictionary 
def myfuncion(*args,**kwargs): => **kwargs : This denotes function can take dictionaru value of varibale length
    print(f"I would like to have {args[0]} {kwargs['food']}")
myfuncion(10,20,30,30,fruit='Apple',food='eggs')

# Function takes arbitary no and returns list with even no 
def myfunc(*args):
    mylist = []
    for item in args:
        if (item %2 ==0):
            mylist.append(item)
    return mylist
print(myfunc(3,4,6,12,23,44)) => [4, 6, 12, 44]


## Lambda expression :
= anonymous function , one time use , no name 




