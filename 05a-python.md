# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists and tuples are both stores of values, the main difference being that lists are mutable (can be changed and edited throughout the program) while tuples are immutable (have the same value throughout the program and cannot be changed).  Lists are signified with brackets [] while tuples parentheses ().  Tuples will work as dictionary keys but not lists, as dictionary keys must be immutable.  The reason for this is that dictionary keys have a unique value (hash) that makes it faster to find key:value pairs when searching a dictionary (searching for the same value pair in a list could take a long time if the list is long as it would have to iterate over the entire list).  If the keys were mutable and could be changed, the hash would change and the original pairing would disappear.  Thus keys have to be immutable and can work as tuples. 

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists and sets are both stores of value but lists can have the same values repeatedly while sets cannot:

>> + Example of list:  list_numbers = [1, 2, 3, 3, 4, 4, 5, 5, 6]
>> + Example of set:    set_numbers = [1, 2, 3, 4, 5, 6]
>> + Using python code to turn list_numbers into a set would be set_numbers = set(list_numbers) and we would get the above output of the single numbers and not the duplicates from list_numbers.

>> Some other differences are lists (use []) are ordered and can be sorted while sets (use {}) are unordered.  Sets are also hashable while lists are not.

>> That last point is why sets are much faster at finding elements than lists.  To find an element in a list, a loop needs to look at the entire list, which could take a long time the bigger the list gets.  Sets use hash tables, however, so that finding an element is much quicker.  The best example I saw on this was from this [StackOverflow link](http://stackoverflow.com/questions/8929284/what-makes-sets-faster-than-lists-in-python) where the question was what if we had to find a lost sock.  If you had to look through your entire closet (list) it would take a long time but if you knew the sock was in the 3rd drawer of the closet (set), it would be much faster.
---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Lambda is a 1-line function in Python that can replace or be used instead of the more common way of writing functions using *def()*. As it is a shorter way to write a function, this can be useful when the function is relatively simple or it is only going to be used once (1-line fucntion for 1-off occurrence).  An example could be multiplying two numbers together:
>> + A function using *def* would be: 
>> 1. def multiply(x, y):
>> 2. return x * y

>> + This same fucntion could be written on one line as:
>> 1. lambda x,y:  x * y

>> Another example would be trying to sort lists or dictionaries using the *sorted* function.  If I have a list containing three tuples of baseball teams and the last year they won the World Series, here is how I would sort them:
>> + baseball_teams = [('Baltimore', 'Orioles', '1983'), ('Chicago', 'Cubs', '2017'),
                       ('Oakland', 'A\'s', '1989')]
     sorted(baseball_teams, key = lambda x:x[1])
     
>> The *sorted* function asks for the sequence to sort (in this case the list baseball_teams) and then assigns the key with which to sort by using *lambda*.  In this case, the second part of the lambda function asks for the 1-index or 2nd value in the tuple to sort by.  We could make that number 0 or 2 and the 1st and 3rd would become the sort keys respectively.

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions are efficient ways to create lists using a *for loop* to iterate over a group and create a list for whatever the condition is.  A simple example would be:

>> + list = [x for x in range(101) if x % 5 == 0]

>> This line says iterate over every number in the range 0-100 and create a list of all numbers divisible by 5.  You can also do this using the *map* and *filter* functions, which have a different format of first calling a function and then a sequence on which to apply the function.  Using the example from above with *map* and *filter*:

>> 1. y = range(101)
>> 2. list_map = map(lambda z: z % 5 == 0, y)

>> In this example, I am using lambda to create the 1-line function of finding items in the sequence 'y' that are divisible by 5. *Filter* is used in a similar way for map, only instead of running the sequence through a function, you are filtering the sequence for a unique set of values.  Below is the expression we'd use for filter in this example, filtering all numbers from the range 0-100 for numbers that are divisible by 5. 

>> 1.  list_filter = filter(lambda x: x ** 5 == 0, y)

>> On balance, it is split when to use a list comprehension and when the map/filter commands.  List Comprehensions are shorter to write and very clean, making them very efficient when creating simple lists, but as they iterate over an entire sequence, they can take a long time when the sequence is lengthy.  Map and Filter work faster but are not as clean and more complex to write.
>> Set and dictionary comprehensions are simply extensions of list comprehensions and used when the end result required is a set or dictionary respectively.  Below are two simple examples:

>> 1. #Create a Dictionary where x is the key and the value x squared.  
>> 2. x = {x: x ** 2 for x in range(11)}
>>
>> 3. #Create a set where the sequence of numbers are unique with no dupes.
>> 4. x = {s for s in '1233445568977'}


---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





