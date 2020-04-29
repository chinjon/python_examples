1. Which of the following are operators, and which are values?

```py
*  # operator
'hello'  # value
-88.8  # value
-  # operator
/  # operator
+  # operator
5  # value
```

2. Which of the following is a variable, and which is a string?

```py
spam  # variable
'spam'  # string
```

3. Name three data types

```
1. String
2. Integer
3. Floating-point
```

4. What is an expression made up of? What do all expressions do?

```
A value and an operator
```

5. This chapter introduced assignment statements, like `spam = 10`. What is the difference between an expression and a statement?

```
A statement assigns a value to a variable
```

6. What does the variable `bacon` contain after the following code runs?
  
```py
bacon = 20
bacon + 1  # 21
```

7. What should the following two expressions evaluate to?

```py
'spam' + 'spamspam'  # 'spamspamspam'
'spam' * 3  # spamspamspam
```

8. Why is `eggs` a valid variable name while `100` is invalid?

```txt
`eggs` does not start with an integer or an underscore
`100` starts with an integer
```

9. What three functions can be used to get the integer, floating-point
number, or string version of a value?

```py
int()
str()
float()
```

10. Why does this expression cause an error? How can you fix it?

```py
'I have eaten ' + 99 + ' burritos.'

# 99 is an integer and not a string
# To fix, str(99) must be used

'I have eaten ' + str(99) + ' burritos.'
```