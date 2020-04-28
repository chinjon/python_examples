# Chapter One

Math Operators from Highest to Lowest Precedence

| Operator | Operation                         | Example   | Evaluates to... |
| -------- | --------------------------------- | --------- | --------------- |
| `**`     | Exponent                          | `2 ** 3`  | `8`             |
| `%`      | Modulus/remainder                 | `22 % 8`  | `6`             |
| `//`     | Integer division/floored quotient | `22 // 8` | 2               |
| /        | Division                          | `22 / 8`  | 2.75            |
| `*`      | Multiplication                    | `3 * 5`   | 15              |
| `-`      | Subtraction                       | `5 - 2`   | 3               |
| `+`      | Addition                          | `2 + 2`   | 4               |

***

## Data Types

_Data type_ is a category for values, and every value belongs to exactly one data type.

| Data Type              | Examples                               |
| ---------------------- | -------------------------------------- |
| Integers               | -1, 0, 1, 2, 3, 4, 5                   |
| Floating-point numbers | -1.25, -1.0, -0.5, 0.0, 0.5, 1.0, 1.25 |
| Strings                |                                        |

***

## Storing Values in Variables

* a _variable_ is like a box in the computer's memory where you can store a single value

* values are stored in variables with an _assigned statement_

* a variable is _initialized_ the first time a value is stored in it

  * after that you can use it expressions with other variables and values

* when naming variables they:

  * can only be one word with no spaces
  * only letters, numbers and the underscore character
  * can not begin with a number

* variables are case sensitive

  * camelcasing is recommended

  ***

## Your First Program

### `print()`

* the `print()` function displays the string value inside its parentheses on the screen

```
print('Hello World')
```

