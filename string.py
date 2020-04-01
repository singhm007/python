# Lines that start with hashtags are comments

print("Manish Singh")

"Manish singh's is a good boy" - Valid string

len("Singh") - Prints the length of the string

print("Hello \n Python") 

mystr = "Manish Singh"
print (mystr[0]) => M  - Prints the first letter
print(mystr[-1]) => h - Prints the last letter , Negative indexing (-1,-2, ......0)

# String Slicing
mystr = "abcdefgh"
mystr[2:] => 'cdefgh' - prints string value starting index value from 2(including index value) to end of string
mystr[:2] => 'ab' - prints string value from strating till index value 2 exluding 2nd index.
mystr[2:5] => 'cde' - prints from index 2(including) upto index 5(excluding)


mystr[2:7:2] => 'ceg' - Last column value indicates step size . That means it will jump 2 values between index 2 and 7.

mystr[::-1] => Revrses the string

# String ummutability 

mystr = "Manish"
mystr[0]= "K" => Will throw error

# String Concatenation
fname = "Manish"
lname = "Singh"

name = fname+lname => Manish Singh

letter = z 
letter*10 => zzzzzzzzzz - Prints z 10 times.

"2" + "3" => 23 - Remember its string Concatenation

mystr = "Hello, This is a beautiful world"
mystr.split()  - Returns a list of Strings. 
['Hello,', 'This', 'is', 'a', 'beautiful', 'world']

# Multiple line string  - """  """
""" Hi this is example 
of multiline String """

===========================================String Operators===================================

+	concatenation operator used to join the strings
*	repetition operator. t concatenates the multiple copies of the same string.
[]	slice operator. It is used to access the sub-strings of a particular string.
[:]	range slice operator. It is used to access the characters from the specified range.
in/not in 	It is known as membership operator. returns True/False based on search result.
%	It is used to perform string formatting. 

# Format Specifiers 
integer = 10
Float = 3.7
String = "Manish"
print("Integer Value : %d \nFloat Value : %f\nString Value : %s"%(integer,Float,String))

Integer Value : 10 
Float Value : 3.700000
String Value : Manish

