# Python Basics

## Knowledge

- computers know what you tell them
- **declarative knowledge**
  - is the statements of fact
- **imperative knowledge**
  - a recipe or a "how-to"
  - _only of value for programming_
    - applies to algorithms
- what is a recipe?
  - a sequence of simple steps
  - flow of control
    - process that specifies when each step is executed
    - a means of determining when to stop
- an algorithm is a conceptual idea
- a program is a concrete instantiation of an algorithm
- A computational mode of thinking means that everything can be viewed as a math problem involving numbers and formulas.

***

## Machines

* **fixed program computer**
  * computer designed to calculate a specific computation
* **stored program computer**
  * machine stores and executes instructions
    * can load a sequence of instructions
      * built from predefined set of primitive instructions:
        * arithmetic and logic
        * simple tests
        * moving data
      * special program (interpreter) executes each instruction in order:
        * use tests to change flow of control through sequence 
        * stop when done
    * has series of parts that will execute instructions
    * interpretor - runs through sequence of instructions
    * advantage: load in another set of instructions
      * gives infinite range of ability to do many things
* **Basic Machine Architecture**
  * memory
    * storage for: 
      * data
      * sequence of instructions (mechanical set of steps)
  * inside:
    * arithemtic logic unit
      * takes information from memory
        * do primitive operation
      * stores back into memory
    * control unit
      * keeps track of each specific operation at any moment
      * contains: program counter
        * loads sequence of instructions
          * points to first instruction
            * cause operation to take place
              * adds to counter
          * arrives at test: determines true or false
        * loops until sequence is complete
  * input
  * output

* Basic Primitives
  * Anything can be computed with 6 primitives
    * move left
    * move right
    * scan 
    * read 
    * write
    * do nothing
  * modern programming languages come with more convient set of primitves
    * can abstract methods to create new primitives
  * anything that is computable in one language can be computable in any other programming language
    * some programs are harder to do things than other programming languages

***

## Languages

* a programming language provides a set of primitive operations
* expressions are complex but legal comibcations of primitives in a programming language
* expression and computations have values and meanings in a programming language
  * value is the meaning of the expression
    * understand how to arrive at that computation
* every programming language could be thought of as consisting a set of primitives
  * a means of combination 
  * a way of putting those primitives together to create new expressions and a means of abstraction
    * a way of taking some complex expression and treating it as its a primitive
* Example of primitive constructs:
  * english: words
  * programming language: numbers, strings, simple operators
* Example of syntax:
  * determines whether a string is legal
  * English: 
    * "cat dog boy" => not syntactically valid
    * "cat hugs boy" => syntactically valid
  * programming language:
    * "hi"5 => not syntactically valid
      * string followed by number = not a legal expression
    * `3.2*5` => syntactically valid
* Example of static semantics: 
  * which syntactically valid strings have meaning
  * English:
    * "I are hungry"
      * syntactically valid but static semantic error
        * put together properly
        * semantically, it does not make sense
  * programming language:
    * `3.2*5` => syntatically valid
    * `3+"hi"` => static semantic error
      * semantically does not make sense
      * sytantically valid
* Example of semantics:
  * the meaning assiciated with a syntatically correct stirng of symbols with not static semantic errors
  * English: semantic sentences can have mulitiple meanings
  * programming languages: have only one meaning but may not be what programmer intended
* Where Things Go Wrong
  * syntactic errors
    * common and easily caught
  * static semantic errors
    * some languages are strict and will make checks before execution
      * python makes checks on the fly
        * will stop at semantic errors
  * no semantic errors but different meaning than what programmer intended
    * program crashes
    * recursion
    * program gives unexpected answer

***

## Types

* program
  * a sequence of definitions and commands 
    * definitions 
      * are evaluated
      * are ways of either assiging names to values 
      * are ways of creating procedures that will be treated as primitives
* commands
  * commands are executed by Python interpreter in a shell
  * are simpler expressions that can execute directly within Python
  * shell
    * a window into the interpretor
  * file
    * stores commands
    * gets read by shell
* Objects
  * programs manipulate data objects
  * objects have a **type** that defines the kinds of things programs can do to them
    * types tell programs whether they can act on it or not
  * objects are:
    * scalar - can not be subdivided
    * non-scalar - have internal structures that can be addressed
* Scalar Objects
  * int - represent integers
    * ex: 5
  * float - represent real numbers 
    * ex: 4.28
  * bool - represent Boolean values
    * ex: True or False
  * NoneType - special and has one value
    * ex: None
  * `type()`
    * method that can see type of object
* Type Conversions (Cast)
  * can covert object of type to another
    * `float(3)` converts integer `3` to float `3.0`
    * `int(3.9)` converts float `3.9` to integer `3`
* Expressions
  * combine objects and operators to form expressions
  * an expression has a value
    * this is a type
  * syntax for a simple expression `<object> <operator> <object>`

***

## Variables

* abstraction: ways of giving names to things 
* equal sign `=` is an assignment of a value to a variable name
* value stored in computer memory
  * stored in a `name table` which maps association of variable names to values
* an assignment binds name to value
* retrieve value associated with name or variable by invoking the name
* names to values allow for reuse of values
  * gives representation with name
* easier to change code later
  * EX:
    * `pi = 3.14159`
    * `radius = 2.2`
    * `area = pi * (radius ** 2)`
* changing bindings
  * can re-bind variable names using new assignment statements
  * a previous value may still be stored in memory but lost the handle for it

***

## Operators and Branching

* ways of testing
* Examples
  * i > j
  * i >= j
  * i < j
  * i <= j
  * i == j
  * i != j
* logical operators on bools
  * a and b are any variable names
    * not a:
      * True if a is False
      * False if a is True
    * a and b:
      * True if both are True
    * a or b:
      * True if either or both are True
* branching programs
  * the simplest branching statement is a conditional
  * a test
    * expression that evalues to True or False
  * a block of code to execute if the test is True
  * an optional block of code to execute if the test is False
* indentation
  * matters in Python
  * how you denote blocks of code
* branching programs allw us to make choices and do different things
* each statement gets executed once
* maximum time to run the program depends only on the length of the program
* these programs run in constant time

***

## Bindings

* names used to associate with values
* names give descriptions to values
  * can be:
    * descriptive
    * meaningful
    * helps you read cod
* values
  * can be:
    * infomration stored
    * can be updated
* keywords can not be used to naem variables
* compute the right hand side => value
  * store it (aka bind it) in the left hand side => variable
* left hand side will be replaced with new value
* `=` is called assignment

***

## Strings

* a sequence of special characters, spaces, digits
* enclose inj quotation marks or single quotes
  * `hi = "hello there"`
* concatenate strings
  * `name = Joe`
  * `greet = hi + name
* operations on strings
  * `'ab' + 'cd'` => concatenation

***

## Input/Output

* `print` - method used to display data in console
* `input` - takes a single argument
  * will evaluate anything inside statement
  * can store into a variable

***

## Control Flow



***

## Guess and Check

* systematic method of guessing the right answer
  * you are able to guess a value for solution
  * you are able to check if the solution is correct
  * keep guessing until find solution or guess all values
  * the process is exhaustive enumeration 
    * exhuast all possible solutions
* done in an iterative manner
* Loop characteristics:
  * needs a loop variable
  * initialized outside loop
  * changes within loop
  * test for termination depends on variable