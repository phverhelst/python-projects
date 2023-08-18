# Learn Python by Building a Blockchain and Cryptocurrency

## Section 1: Getting Started


### What is Python?

"Python is a **powerful**, **easy to use**, **object-orientated** programming language"

It's performant, it runs on all operating systems and it's extremely versatile.  

Python has a clean and simple syntax, it follows a "batteries included" approach and offers great documentation.

Python embraces objects, classes, inheritance and allows you to easily work with complex data structures.

### Python's Versatility

#### Scripts & Programs
Use it like a calculator (from the command line)  
Write simple (utility) scripts or complex programs  
Add UI to create desktop applications

#### Web Development
Use Python as a server-side language  
Build fullstack apps or REST APIs  
Use framework like Django or Flask

#### Data Science
Use riche set of third-party packages  
Gather, import and clean data  
Do statistical analyses, plotting, machine learning  

### What's a Blockchain?

A distributed **data storage** consisting of **containers** (blocks) wich are **connected**.  

### What's a Cryptocurrency?

If the data you store in a block is a **list of transactions**, the coins transferred in the the transaction form your cryptocurrency.  

## Section 2: Diving Into the Basics of Python

### The REPL
**R**ead  
**E**valuate  
**P**rint  
**L**oop

### Blockchain Big Picture

#### The Data :  
A number  
A string  
A bolean  
Complex Structure  

#### The Chain :  
A List  

### Python Data Types

#### Numbers :  
Integer  
Float

#### Booleans :  
True  
False  

#### Strings :  
'Hi there!'  
"Hi there!"

#### Complex Types like Dictionnaries & Objects

### Numbers

#### Integer
As big (small) as supported by your Memory and Operating System  
Convert other types to integer with **int()**

#### Float
As big (small) as supported by your Memory and Operating System  
Convert other types to Float with **float()**

Write long numbers in easily readable way: 1_000_000.0

### Operators

#### Addition +
5 + 10  
15  
Works with Strings  
#### Substratction - 
5 - 10  
-5  
#### Multiplication *
5 * 10  
50  
Works with Strings  
#### Division /
5/10  
0.5  
Float  
#### Floor Division //
5 // 10  
0
#### Exponentation **
5 ** 10  
9765625
#### Modulus %
5 % 10  
5

### Lists

index   0   1   2   3  
[ "some text",  12.9,   True,   ["nested!", 8]  ]  
length = 4  

### Our Blockchain

The Chain
[ [1], [1, 'hi'], [1, 'hi', True] ]   
The Block, The Value, Previous Values, New Value  

"Coins"  
[ [1.3], [1.3, 0.5], [1.3, 0.5, 0.65] ]  

### Functions

Define Code wich is executed Later (and possibly Multiple Times)  

    def greet():
        print('Hello')
    greet()
    greet()

Can receive Arguments

    def greet(name):
        print('Hello ' + name)
    greet('Max')

Can return Values

    def sum(a, b):
        return a + b
    print(sum(2, 5))

Default Arguments

    def greet(name, age=29):
        print('Hello ' + name + ', I am ' + age)
    greet('Max')


keyword Arguments (kwargs)

    def greet(name, age):
        print('Hello ' + name + ' I am' + age)

    greet(age=29, name='Max')


