# Python vs. JavaScript

Document outlines personal findings of the differences between languages as a JavaScript developer.

## Basics

### Boolean

In `python` `True` and `False` are formatted with capitol letters.

In `javascript` they are lower case, `true`, `false` (??)

### Syntax

In `javascript`, `semicolons` are optional syntax items that signal to developers that it is the end of a statement. This is total optional due to [automatic semicolon injection](https://flaviocopes.com/javascript-automatic-semicolon-insertion/).

In `python`, have not encountered a `semicolon` equivalent, yet.

To declare a variable in `javascript`, keywords such as `var`, `let`, or `const` must be used for assignment.

In `python`, to declare a variable a name is used without any keywords.

### Modules

In `javascript` or with `node`, developers can take use of native libraries or modules.

```js
const fs = require('fs')
```

In `python`, developers can also take use of native libraries or modules.

```py
from sys import argv
```

### Functions

In `javascript` keyword reserved for declaring a function is `function`. Though there are a few ways to "declare" a function.

```js
function exampleJavaScriptFunction() {
  // do something
}
```

In `python` the `def` keyword is used to declare a function.

```py
def examplePythonFunction():
  # do something here
```