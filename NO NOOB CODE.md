
# Some mistakes that tell you are a Noobs python coder

## Using import *
Avoid `from xyz import *`
This isn’t a good practice for many reasons, it's inefficient mainly if the module have a lot object; can cause a conflict between variable name, when * used you don't know which objects you are importing as well their name.

```python
# Using import *
# Bad
from math import *

print(floor(2.4))
print(ceil(2.4))
print(pi)

# Good
import math
from math import pi

print(math.floor(2.4))
print(math.ceil(2.4))
print(pi)
```

## Try/Except: Not specifying the exception in the “except” clause

This isn’t recommended in the PEP 8 guidelines; the problem with a bare `except` is that it will catch SystemExit and KeyboardInterrupt exceptions, making it harder to interrupt a program with Control-C.
Always specify the exception in the `except` clause.

```python
# Try - except
# Bad
try:
    driver.find_element(...)
except:
    print("Which exception?")

# Good
try:
    driver.find_element(...)
except NoSuchElementException:
    print("It's giving NoSuchElementException")
except ElementClickInterceptedException:
    print("It's giving ElementClickInterceptedException")
```

## Not using Numpy for math computations
Often we forget that there are packages that can make our life easier and more productive in Python.

One of those packages you should use for math computations is Numpy. Numpy could help you solve math operations faster than `for` loops.

Say we have an array of `random_scores` and we want to get the average score of those who failed the exam (score<70). Let’s try to solve this with a `for` loop.

```python
import numpy as np

random_scores = np.random.randint(1, 100, size=10000001)

# Bad (solving problem with a for loop)
count_failed = 0
sum_failed = 0
for score in random_scores:
    if score < 70:
        sum_failed += score
        count_failed += 1

print(sum_failed/count_failed)
```

With numpy:
```python
# Good (solving problem using vector operations)
mean_failed = (random_scores[random_scores < 70]).mean()
print(mean_failed)
```

Numpy is faster because vectorizes our operations.

## Not closing a file previously opened
A good practice everyone knows is that every file we open with Python must be closed.

This is why we use the `open` , `write/read`, `close` whenever we work with files. That’s OK, but if the `write/read` methods throw an exception, the file won’t be closed.

To avoid this issue, we have to use the `with` statement. This will close the file even if there’s an exception.
```python
# Bad
f = open('dataset.txt', 'w')
f.write('new_data')
f.close()

# Good
with open('dataset.txt', 'w') as f:
    f.write('new_data')
```

## Not following PEP8
PEP8 is a document everyone learning Python should read. It provides guidelines and best practices on how to write Python code (some of the advice in this notes comes from PEP8)

This guideline might be intimidating for those new to Python. Fortunately, some PEP8 rules are incorporated in IDEs, so all PEP8 guidelines mistake are signed by IDE and/or linter with signs.

For example, missing space between the keys in a list or dict definitions.

```python
# Good
my_list = [1, 2, 3, 4, 5]
my_dict = {'key1': 'value1', 'key2': 'value2'}

my_name = "Fabio"
```

## Not using .keys and .values methods properly when working with dictionaries
I think most of you know what the `.keys` and `.values` methods do when working with dictionaries.

In case you don’t know, let’s have a look.

```
dict_countries = {'USA': 329.5, 'UK': 67.2, 'Canada': 38}
>>>dict_countries.keys()
dict_keys(['USA', 'UK', 'Canada'])
>>>dict_countries.values()
dict_values([329.5, 67.2, 38])
```

The problem here is that we sometimes don’t use them properly.

Say we want to loop through the dictionary and obtain the keys. You might use the `.keys` method, but did you know you could obtain the keys just by looping through the dictionary? In this case, using `.keys` will be unnecessary.

```python
# Not using .keys() properly
# Bad
for key in dict_countries.keys():
    print(key)
    
# Good
for key in dict_countries:
    print(key)
```

Also, we might come up with workarounds to get the values of a dictionary, but that could be easily obtained with the .items() method.

```python
# Not using .items()
# Bad
for key in dict_countries:
    print(dict_countries[key])
    
# Good
for key, value in dict_countries.items():
    print(key)
    print(value)
```


## Never using comprehensions (or using them all the time)
Comprehension offers a shorter syntax when you want to create a new sequence (list, dictionary, etc) based on a sequence that is already defined.

Say we want to lowercase all the elements in our `countries` list.

Although you could do this with a `for` loop, you could simplify things with a list comprehension.

```python
# Bad
countries = ['USA', 'UK', 'Canada']

lower_case = []
for country in countries:
    lower_case.append(country.lower())

# Good (but don't overuse it!)
lower_case = [country.lower() for country in countries]
```

Comprehensions are very useful, but don’t overuse them! Remember the [Zen of Python](https://peps.python.org/pep-0020/): “Simple is better than complex”.


## Using range(len())
One of the first functions we learned as beginners are the `range` and `len`, so no wonder why most people have the bad habit to write `range(len())` when looping through lists.

Say we have a `countries` and `populations` lists. If we want to iterate through both lists at the same time, you’d probably use `range(len())`.

```python
# Using range(len())
countries = ['USA', 'UK', 'Canada']
populations = [329.5, 67.2, 38]

# Bad
for i in range(len(countries)):
    country = countries[i]
    population = populations[i]
    print(f'{country} has a population of {population} million people')
```

Although that gets the job done, you could simplify things using `enumerate` (or even better, use the `zip` function to pair elements from both lists)


```python
# OK
for i, country in enumerate(countries):
    population = populations[i]
    print(f'{country} has a population of {population} million people')

# Much Better
for country, population in zip(countries, populations):
    print(f'{country} has a population of {population} million people')
```

## Formatting with the + operator
Probably one of the first things we learn in Python is how to join strings with the `+` operator.

This is a useful, yet inefficient way to join strings in Python. Besides, it’s not so good-looking — the more strings you need to join, the more + you’ll use.

Instead of using this operator, you can use the f-string.

_Questo è un tipico esempio per quelli che in gioventù hanno imparato a scrivere codice con il Basic... come me..._ ::smiley::
```python
# Formatting with + operator
# Bad
name = input("Introduce Name: ")
print("Good Morning, " + name + "!")

# Good
name = input("Introduce Name: ")
print(f'Good Morning, {name}')
```
The best part about f-strings is that it’s not only useful for concatenation but has [different applications](https://martinheinz.dev/blog/70).  _A questo blog ci sono altre informazioni utili..._


## Using default mutable values
If you include a mutable value (like a list) as a default parameter of a function, you’d see some unexpected behavior.
```
# Bad
def my_function(i, my_list=[]):
    my_list.append(i)
    return my_list
>>> my_function(1)
[1]
>>> my_function(2)
[1, 2]
>>> my_function(3)
[1, 2, 3]
```
In the code above, every time we call the `my_function` function, the list `my_list` keeps saving the values from previous calls (most likely we want to initiate an empty list every time we call the function)

To avoid this behavior, we should set this `my_list` parameter equal to `None` and include the `if` clause below.

```
# Good
def my_function(i, my_list=None):
    if my_list is None: 
        my_list = []
    my_list.append(i)
    return my_list
>>> my_function(1)
[1]
>>> my_function(2)
[2]
>>> my_function(3)
[3]
```

