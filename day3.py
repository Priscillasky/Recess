#Basic operators

"""
Arithmetic
+Addition
-Subtraction
*Multiplication
/Division
//Divide
%Modulo
**Exponentiation

Comparison operators
 ==Equal to
 != Not equal !==
 >Greater than
 <less than
 >=Greater than or equal to
 <=Less than or equal to

 Logical operators
 Logical AND 'and' or 'or'
 Logical NOT: 'not'

 Assignment operators
 Assign value: '='
 Add value: '+'
 Add and assign value: ' +='
 Subtract value: '-'
 Subtract and assign value: ' -='
 Multiply value: '*'
 Multiply and assign value: ' *='
 Divide value: '/'
 Divide and assign value: ' /='
 Modulo value: '%'
 Modulo and assign value: '%='
 Exponentiate value: '**'
 Exponentiate and assign value: '**='

 Membership operators
 In :'in' operator:checks if value exists in a sequence
 Not in :'not in' operator:checks if value does not exist in a sequence

 Identity operators
 Is :'is' operator:checks if two values are the same object


"""
"""x = 50 +45 
print(x)

y = 50 * 45 
print(y)

z = 50 - 45 
print(z)

p = 50/45 
print(x)

#Wxamples of comparison operators
a = 15
b = 9

#Greater than
if(a > b):
    print("a is greater than b")
    print(a > b)
#Less than
if(a > b):
    print("a is less than b")
    print(a < b)

#Greater than or equal to
if(a >= b):
    print("a is greater than or equal to b")
    print(a >= b)

#Less than or equal to 
if(a <= b):
    print("a is less than or equal to b")
    print(a <= b)

#Equal to 
if(a == b):
    print("a is equal to b")
    print(a == b)

#Not equal to
if(a != b):
    print("a is not equal to b")
    print(a != b)

#Less than or equals to
print(a <= b)

#equal to
print ( a == b)


#Examples on Logical operators
a = True
b = False

#Logical AND
print(a and b)

#Logical NOT
print(not b)
print(not a)

#LOGICAL OR
print(a or b)

#Assignment operators

#subtarct and assign
b = 19
b -+ 5
print(b)

#multiply and assign
c = 19
c *= 5
print(c)

#divide and assign

d = 19
d /= 5
print(d)

#module and assign
e = 19
e %= 5
print(e)

#Exponentiate and assign
f = 19
f **= 5
print(f)


#membership assignment operators
cars = ['prado', 'volvo','Prado']

if 'prado' in cars :
    print('jeep is in the list')
    print('jeep is in the list')
    print('toyota is not in the list')

#identity operators
a = 5
b = 5
print(a is b)
print(a is not b)
print(a == b)
print(a != b)

#List
z = [1,2,3,4,5,6,7]
w = [1,2,3,4,5,6,7]

print(z is not w)

#Bitwise operators
#bitwise operators are used to perform operations on individual bits in of binary numbers.

#Bitwise AND('&'):Perform a bitwise AND operation between the corresponding bits of two integers
#Bitwise OR ('|'):Perform a bitwise OR operation between the corresponding bits of two integers
#Bitwise XOR ('^'):Performs a bitwise XOR operation
#Bitwise NOT ('-'):Performs a bitwise NOT operation between the corresponding
#Bitwise leftShift ('<<'):Performs a bitwise left shift operation
#Bitwise rigtShift ('>>'):Performs a bitwise right shift operation

#Examples of Bitwise operations
a = 10
b = 20

#Bitwise AND operations
result_and = a & b
print(result_and)

#Bitwise NOT operations
result_and = a - b
print(result_and)

#Bitwise OR operations
result_and = a | b
print(result_and)

#Bitwise XOR operations
result_and = a ^ b
print(result_and)

#Bitwise leftShift operations
result_and = a << b
print(result_and)

#Bitwise rightShift operations
result_and = a >> b
print(result_and)
"""


#Example and assignment
#Simple calculator function to calculate (add,subtract,multiply,divide )
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def main():
    print('Gum simple calculator')
    number1 = float(input("Enter the first number:"))
    number2 = float(input("Enter the second number:"))
    operator = input("Enter the operator '+, -, *,/")

    if operator == '+':
        result = add(number1, number2)
    elif operator == '-':
        result = subtract(number1, number2)
    elif operator == '*':
        result = multiply(number1, number2)
    elif operator == '/':
        result = divide(number1, number2)
    else:
        print('Invalid operator')
        return
    print('The result is:', result)
    
    
if __name__ == '__main__':
    main()

    """print("Addition:" ,add(a,b))
    print("Subtraction:" ,subtract(a,b))
    print("Multiplication:" ,multiply(a,b))
    print("Division:" ,divide(a,b))
    """


