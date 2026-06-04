### when "continue" come

continue may only occur syntactically nested in a for or while loop, but not nested in a function or class definition within that loop. It continues with the next cycle of the nearest enclosing loop.

### when "break" come

break may only occur syntactically nested in a for or while loop, but not nested in a function or class definition within that loop.

It terminates the nearest enclosing loop, skipping the optional else clause if the loop has one.

If a for loop is terminated by break, the loop control target keeps its current value.

When break passes control out of a try statement with a finally clause, that finally clause is executed before really leaving the loop.

### "exceptions"

Errors detected during execution are called exceptions and are not unconditionally fatal:

### "try....except"

You should use try...except blocks in Python when you have code that might raise an exception which you expect could occur and want to handle gracefully rather than letting the program crash

Input validation using try...except in Python relies on catching exceptions like ValueError that occur when built-in functions (e.g., int(), float()) fail to convert user input into the expected data type

### validation

Real-world validation is usually about:

constraints
format
domain rules
business logic

### validation Loop

Actually conversion itself is often PART of validation.

A validation loop usually has:

Entry Condition: Need valid input.
Retry Path : Input invalid.
Exit Condition : Input valid.

### A retry-validation loop is:

state = invalid

while state is invalid:
ask again

validate again
continue program

#### learning

What exact condition keeps loop alive?
What exact event exits loop?
What variables change each iteration?

### Dict

if you have dynamic key inside nested dict, you must convert to that exact value to list and then get the value using: can put any value in place of zero to get the idex
list(dict["dynamic_key"].values())[0]

### ValueError: too many values to unpack (expected 2)

occurs when you attempt to assign elements from an iterable (like a list, tuple, or string) to variables, but the iterable contains more items than there are variables defined on the left side of the assignment.

## List/Sequence Unpacking:

Assigning a list with more than two elements to two variables. Fix: Add a third variable or use an underscore _ as a throwaway variable for the extra item (e.g., a, b, _ = [1, 2, 3]).

## Dictionary Iteration:

Iterating over a dictionary directly in a for loop (e.g., for k, v in my_dict:) yields only keys. If a key is a string with more than two characters, Python tries to unpack the characters into two variables. Fix: Use the .items() method (e.g., for k, v in my_dict.items()

## Function Returns:

A function returns a tuple or list with more than two items, but you only capture two. Fix: Capture all returned values or use the asterisk * operator to collect extras into a list (e.g., a, b, *rest = func()).

## String Unpacking:

Attempting to unpack a string directly splits it into individual characters. Fix: Split the string first using .split(',') if it contains delimited values.
