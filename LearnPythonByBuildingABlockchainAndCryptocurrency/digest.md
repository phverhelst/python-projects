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

### Variable Scope

Global

    name = 'Max'
    def greet():
        print('Hi ' + name)
    greet()

Local  

    name = 'Max'
    def greet()
        age = '29'
        print('Hi ' + name + ', I am ' + age )
    greet()

### Understanding Python Syntax

**Indentation** structure Code  
Block statements nedd a **:**  
Functions defined with **def**  
Follow **PEP 8** Code Style  

### Module Summary

#### Data Types
- **Numbers** (Integers & Floats)
- **Strings**
- **Booleans**

#### Operators
- **Base Arithmetic:** +, -, *, /  
- **Modulus:** % (15 % 10 = 5)
- **Floor Division:** // (15 // 10 = 1)
- **Power:** ** ( 2 ** 3 = 8)
- **Strings** can be **added** and **multiplied** (with integers)

#### Lists
- **Create** Lists
- **Add Items** via append()
- Access Items **via Index** (wich **starts at 0!**)
- Other List Operations (pop(), ...)

#### Functions
- Use **Indentations** and: **:** to define Code Block
- Can use **Arguments**
- Can **return** Values
- Can use **Default Arguments**
- **Keyword Arguments** allow you to re-order or skip arguments

#### Scope
- **Global:** Variables defined outside of Functions
- **Local:** Variables defined inside of Functions

### Blochain Status
- Chain of Data **Basic Implementation**
- Mine new Blocks **Basic Implementation**
- Block Hashing **Basic Implementation**
- Analyze & Verify Chain
- Real Transaction
- Store Chain to Disk
- Node Network
- Share Data, Resolve Conflicts
- Wallets
## Section 3: Working with Loops & Conditionals

### Loops & Conditionals
Repeat & Check

#### Module Overview
- Loops - for and while
- Conditional Statements (if)
- Boolean Operators
- Controlling Loops

#### What about the Blockchain

- Verify our Blockchain
- Create a User Input Interface

### Loops

#### For
    for elements in list:
        print(element)

A for Loop allows you to iterae trough **the elements of an Iterable** (e.g. a List)  
**Changing** the Iterable as part of the Loop is **NOT** recommended  

#### while
    while True:
        print('Infinity')

A while Loop allows you to repeat code as long as its **condition is True**  
Make sure to provide an exit condition,  **otherwise CTRL + Z** has to be used

#### if-else

    User Input
        "Max"
            create_user()
        ""
            empty()

### Booleans
#### True or False  
True
False
#### Used in Conditional Checks (if)
#### Result from Boolean Operators
    ==
    !=
    >=
    <=
    is
    in
    >
    <

### if-elif-else

    User Iput
        if
            "Max"
                create_user()
            ""
                empty()
        elif
            "M"
                too_short()

### Loops

use **break** to **exit the Loop** before it's finished

#### There is no switch-case Staement

### Manipulating the Blockchain
Edit Transaction  
Invalid Previous Hash
### Checking Our Blockchain
    [1], 3.5
        [[[1], 3.5], 5.8]
            [[[[1], 3.5], 5.8], 1.0]

Does the value contain the LAST value as a First Element?

#### There is no for ( i = 0; i < 10; i++) Loop !
#### But there's range()

### Module Summary
#### Loops
- **for:** Loop trough List (Iterable) Elements
- **while:** Loop as long as Condition is True
#### if-elif-else
- **if:** Check wether a certain **Condition** is Fulfilled
- **else:** Execute Code in Case Condition is **NOT Fulfilled**
- **elif:** Permform an **additional check** in case Condition is NOT Fulfilled
#### Boolean Operators
- **==:** Are two Values Equal?
- **!=:** Are two Values NOT Equal?
- **>:** Is Value 1 greater than Value 2?
- **<:** Is Value 1 lower than Value 2?
- **>=:** Is Value 1 greater or equal than Value 2?
- **<=:** Is Value 1 lower or equal than Value 2?
- **is:** Is Value True?
- **not:** Is Value NOT True?
### Blochain Status
- Chain of Data **Basic Implementation**
- Mine new Blocks **With User Interface**
- Block Hashing **Basic Implementation**
- Analyze & Verify Chain **Basic Implementation**
- Real Transaction
- Store Chain to Disk
- Node Network
- Share Data, Resolve Conflicts
- Wallets
## Section 4: Understanding Complex Data Structures
### Beyond Lists, Numbers, Strings & Booleans
### Module Overview
- Tuples, Sets & Dictionaries
- Iterable Function & Behaviors
- List Comprehensions
- By Reference vs By value
### What about the Blockchain
- Send Transactions from A to B
- Outstanding Transactions & Mining
### A Transaction
sender  
recipient  
amount  
- We need a data structure wich stores key-values pairs, order doesn't matter
- we need a data structure wich stores a mutable (editable) list of values, order doesn't matter
- We need a data structure wich stores a mutable (editable) list of values, order does matter
#### Mining a new Block
### A Block
- Hash
- Index
- Transactions
### Managing a List of Participants

    sender      Max     Chris   Manuel
    recipient   Annal   Manuel  Max
    amount      3.5     5.0     8.9

    Sender & Recipients
        Max
        Anna
        Chris
        Manuel
Should only be included once !  
We need a data structure wich stores unique values, order doesn't matter

## Iterables Overview

    List    ['Milk', 'Honey', 'Milk']
    
Mutable, ordered list, duplicates allowed, mostly only one type

    Set     {'Milk', 'Honey'}

Mutable, **unorderd** list, **no duplicates**, mostly only one type

    Tuple   ('Milk', 'Honey')

** Immutable**, **ordered** list, **duplicates allowed**, often **mixed types**

    Dictionary  {'name': 'Milk', 'n': 2}

Mutable, **unordered map**, **no duplicate keys**, often mixed types



