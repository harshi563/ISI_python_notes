'''1.Introduction to python
Python is a high-level, interpreted, general-purpose programming language.
It is known for its simple syntax, readability, and versatility.
Developed by Guido van Rossum
First released in 1991
Used in:
Web Development
Data Science
Artificial Intelligence
Automation
Software Development
Features of Python
Easy to learn
Platform independent
Dynamically typed
Large standard library
Supports object-oriented programming'''

'''2.Output statements
 print() function is used to display output
 end=' ' prevents a new line after printing'''
print('hi') 
print('Good Morning!') 
print("It is a rainy today") 
print('Good Morning!', end=' ') 
print("It is a rainy today") 

'''3. Keywords in Python 
Keywords are reserved words
They cannot be used as variable names'''
import keyword 
print(keyword.kwlist) 

''' 4. Variables 
Variables are containers for storing data values.
Python allows dynamic reassignment 
One variable can store one value at a time'''
var1 = 'John' 
print(var1) 
var1 = 'Sam' 
print(var1) 
var1 = 'Matt' 
print(var1) 

'''5. Data Type
Python is dynamically typed, meaning you don't need to declare the type. 
We use type() to check the data category.
int: Whole numbers
float: Decimals
str: Text
bool: True/False'''
a = 10 
print(type(a)) 
b = 10.5 
print(type(b)) 
c = 'Sneha' 
print(type(c)) 
d = True 
print(type(d)) 

'''6. Input Statements 
In Python, the input() function always accepts user input in string format.
When numerical operations are required, the input must be converted into the 
appropriate data type using type casting.
This conversion can be done immediately by wrapping the input() function inside 
data type constructors such as int() or float().'''
name = input('Enter your Name : ') 
print('hi ', name) 
# Integer input
a = int(input('Enter the value of A  : ')) 
print(type(a)) 
b = int(input('Enter the value of B : ')) 
print(type(b)) 
c = a + b 
print(c) 
# Float input
a = float(input('Enter the value for A  : ')) 
b = float(input('Enter the value for B : ')) 
c = a + b 
print(c) 
# Multiple values in single line
name1, name2, name3 = input('Enter 3 names: ').split() 
print('Name1 : ', name1) 
print('Name2 : ', name2) 
print('Name3 : ', name3) 

name1, name2, name3 = input('Enter 3 names: ').split(',') 
print('Name1 : ', name1) 
print('Name2 : ', name2) 
print('Name3 : ', name3) 

'''7. Calendar Module
calendar is a built-in module
Used to display month/year formats'''
import calendar 
year = int(input('Enter the year: ')) 
month = int(input('Enter the month: ')) 
print(calendar.month(year, month)) 

'''8. String Operations 
Common String Functions
in : output is boolean
count()
endswith() : output is boolean
find()
replace()'''
s = "Life iS beaUtiful !!! " 
print("Life" in s) 
print(s.count('!')) 
print(s.endswith('l')) 
print(s.find("b")) 
print(s.replace('f', 'v')) 

'''9. String Concatenation 
a + b → concatenates (joins) strings
print(a,b) → prints multiple strings separated by a space'''
a = 'life is beautiful' 
b = ' live happily' 
print(a, b) 
print(a + b) 

'''10. String Formatting
Using format()
{} → values are filled in order
{0}, {1} → values are filled by index
{a}, {b}, {c} → values are filled by name (keywords)'''
print('{} and {} are best friends'.format('Ram', 'Sam')) 
print('{0} and {1} are best friends'.format('Ram', 'Sam')) 
print('{1} and {0} are best friends'.format('Ram', 'Sam')) 
print('{a},{b},{c}'.format(a='James', b='peter', c='Rocky')) 

quantity = 3 
itemno = 567 
price = 49.95 
myorder = "I want {} pieces of item {} for {} dollars." 
print(myorder.format(quantity, itemno, price)) 

age = 36 
txt = "My name is John, and I am {}" 
print(txt.format(age)) 

# 11. Conditional Statements 
# Even or odd
num = int(input('Enter the number : ')) 
if(num % 2 == 0): 
    print('Even') 
else: 
    print('odd') 
'''This program checks whether a given number is even or odd using 
the if–elseconditional statement.The number entered by the user is first 
converted from string to integer using int()The modulus operator % is used to 
find the remainder
If a number is divisible by 2, it is Even
Otherwise, it is Odd'''

# Biggest of 3 numbers
a = int(input('Enter A : ')) 
b = int(input('Enter B : ')) 
c = int(input('Enter C : ')) 

if(a > b and a > c): 
    print('A is the biggest number') 
if(b > a and b > c): 
    print('B is the biggest number') 
if(c > a and c > b): 
    print('C is the biggest number') 

# Vote eligibility
print("Check the person is eligible to vote or not") 
age = int(input("Enter your Age : ")) 
if age < 18: 
    print("Sorry, You are not eligible to Vote") 
else: 
    print("You are eligible to vote") 

# Guess a number
print("Guess a Number: ") 
num = int(input()) 
if num > 10 and num < 20: 
    print("\nCorrect Guess!") 
else: 
    print("\nIncorrect Guess!") 

# Register number check
regno = int(input("Enter Register no : ")) 
if regno in [101, 105, 109, 106]: 
    print("pass") 
else: 
    print("Fail")
