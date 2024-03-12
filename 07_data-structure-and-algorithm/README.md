Nama: Erista Disti Kirani 

Summary Data Structure & Algorithm 

What is Data Structure 

“Data structure is a way to organize and store data so that it can be accessed and used efficiently. 

Data structure define the relationship between data and the operations that can be performed on the data.” 

Why we need Data Structure? 

1. Organization: Data structure helps us neatly arrange data so it’s easy to find and use. 
1. Efficiency: They make our programs faster by allowings us to quickly find and manipulate data. 
1. Solving Problems: For complex tasks, data structures are like puzzle pieces that help us solve big problems step by step. 
1. Not Wasting Resources: They helps us use computer memory wisely, preventing waste and errors. 
1. Keep Code Neat: They make our code organized and easier to read and understand. 
1. Working Together: Different data structures are good for different jobs, so we pick the right one for each task. 

Illustration: Locker Room 

- A Room with Large Cabinets. 
- The large cabinets is divided into smaller cabinet for storing items. 
- Each small cabinet has varying sizes and a sequential number (identifier). 

Data Structure in Python 

- List 
- Dictionary 
- Tuple 
- Set 

List 

A list is a simple array/collection of objects that is order (with indices starting from 0) and has mutable properties (not permanent - its items can be change). 

List of Frequently Used Methods: 

append - remove - index 

extend - pop - copy 

insert - clear (python3) - sort 



Tuple 

A tuple is an array/collecttion of objects that is similar to a List, but it is ‘immutable’ (permanent - you cannot change or add new items after it’s defined) . Tuples havemethods similar to those in a List but are limited to methods that do not modify the array/collection. 

Set 

A set is a simple array/collection of objects that is unordered (has no index) and does not alow duplicate items. Each item that has been defined is immutable, but the Set as a whole is mutable. sets are also used for mathematical operations such as union, intersection, difference, and symmetric-defference. 

Listof Frequently Used Methods: 

add - remove - issuperset 

union - intersection - difference 

Dictionary 

A dictionary is an data structure that store of key-value pairs where each key must be unique (non-redundant).

List of Frequentlyu Used Methods; 

items - keys - values - setdefault 

get - has\_key (python2) -clear - copy 

Searching: is the process of finding a given value position in a list of values. 

Sorting: sorting is the process of arranging data in a certain order. Usually, we sort by the value of the statements. We can sort numbers, words, pairs, etc. For example, we can sort students by their height, and we can sort cities in alphabetical order or by their numbers of citizens. The most-used orders are numerical order and alphabetical order. 

Selection sort - O (n^2) 

The idea: Find the minimal element and swap it with the first element of an array. Next, just sort the rest of the array, without the first element, in the same way. 

Notice that after k iterations (repetition of everything inside the loop) the first k elements will be sorted in the right order (this type of a property is called the loop invariant). 

Counting sort - O  (n + k ) 

The idea: First, count the elements in the array of counters. Next, just iterate through the array of counters in increasing order. Notice that we have to know the range of the sorted value. if all the the elements are in the set {0, 1, …, k}, then  the array used for counting should  


