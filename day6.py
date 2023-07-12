#Regular expressions
"""
\d:Matches any character between (0-9)
\w:Matches any alphanumeric character between (A-Z,0-9,a-z, and underscore)
\s:Matches any white space character
.:Matches any character except a nwe line
*:Matches zero or more whitespace characters

Matching and searching
NB:A RegEx /regular expression is a sequence of characters that forms a search pattern.
regex.re.match() ,re.search(),re.findall()

findall	- Returns a list containing all matches
search -Returns a Match object if there is a match anywhere in the string
split -	Returns a list where the string has been split at each match
sub	Replaces one or many matches with a string
"""
#Example 1- demonstrating RegEx |match First Word, match all numbers,match group word
import re
text = "My name is Gum Priscilla .I am a programmer with 30 years experience."

#Match first word
match = re.search(r"\b\w+\b", text)

if match :
    print(match.group())

#Match all numbers
match = re.search(r"\d+", text)

if match :
    print(match.group())

matches = re.findall(r"\d+", text)
print(matches)



#Example 2 - validating email format or email address
def validated_email(email):
    pattern = r'^[\w\. -]+ @[\w\. -]+\.\w+$'
    if re.match(pattern, email):
        return True
    
    else:
        return False
    
#Example usage
email1 = "priscilla@gmail.com"
email2 = "priscilla_gum@gmail.com"

print(validated_email(email1))
print(validated_email(email2))


#Generators and Iterators
#An iterator is an object that can be iterated upon meaning you can traverse through all values
#An iterator is an object that contains a countable number of values
#i.e __iter__() and __next__()
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

#Generators
#Agenerator function uses the yield keyword to generate a value
"""def gen():
    yield "apple"
    yield "banana"
    yield "cherry"

for value in gen():
    print(value)

def factorial(n):
    if n ==0 or n ==1:
        return 1
    else:
        fact = 1
        for i in range(1, n+1):
            fact *=i
        yield fact
    
    #print factorial of a number from 1 to 10
for i in range(1,10):
    print(factorial(i))"""

#Example 3
def squares():
    for i in range(1, 10):
        yield i ** 2

#create an iterator object 

squares_iterator = squares()

for i in range(5):
    print(next(squares_iterator))

#decorators in python
def my_decorator(func):
    def inner():
        print("This is my decorator")
        func()
        return inner
    
@my_decorator
def outer_decorator():
    print("This is my function")

outer_decorator()



