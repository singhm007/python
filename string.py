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