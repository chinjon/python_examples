# Intro To Python

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
* semantics is the meaning assiciated with a syntatically correct stirng of symbols with not static semantic errors
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