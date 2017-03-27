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

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

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





