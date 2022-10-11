Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> student{"name": "John", "age": 25, "courses": ["Math", "CompSci"]}
SyntaxError: invalid syntax
>>> student = {"name": "John", "age": 25, "courses": ["Math", "CompSci"]}
>>> print(student)
{'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
>>> print(student["name"])
John
>>> print(student["age"])
25
>>> print(student["courses"])
['Math', 'CompSci']
>>> print(student.get("name"))
John
>>> print(student.get("phone"))
None
>>> print(student["phone"])
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print(student["phone"])
KeyError: 'phone'
>>> print(student.get("phone", "Not Found"))
Not Found
>>> student["phone"] = "555-5555"
>>> print(student.get("phone", "Not Found"))
555-5555
>>> student.update({"name": "Jane", "age" 26, "phone": "555-5555"})
SyntaxError: invalid syntax
>>> student.update({"name": "Jane", "age": 26, "phone": "555-5555"})
>>> print(student)
{'name': 'Jane', 'age': 26, 'courses': ['Math', 'CompSci'], 'phone': '555-5555'}
>>> del student["age"]
>>> print(student)
{'name': 'Jane', 'courses': ['Math', 'CompSci'], 'phone': '555-5555'}
>>> age = student.pop("age")
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    age = student.pop("age")
KeyError: 'age'
>>> student.update("age": 26)
SyntaxError: invalid syntax
>>> student.update({"age": 26})
>>> print(student)
{'name': 'Jane', 'courses': ['Math', 'CompSci'], 'phone': '555-5555', 'age': 26}
>>> age = student.pop("age")
>>> print(student)
{'name': 'Jane', 'courses': ['Math', 'CompSci'], 'phone': '555-5555'}
>>> print(age)
26
>>> student.update({"age": 26})
>>> print(student)
{'name': 'Jane', 'courses': ['Math', 'CompSci'], 'phone': '555-5555', 'age': 26}
>>> print(len(student))
4
>>> print(student.keys())
dict_keys(['name', 'courses', 'phone', 'age'])
>>> print(student.values())
dict_values(['Jane', ['Math', 'CompSci'], '555-5555', 26])
>>> print(student.items())
dict_items([('name', 'Jane'), ('courses', ['Math', 'CompSci']), ('phone', '555-5555'), ('age', 26)])
>>> for key in student:
	print(key)

	
name
courses
phone
age
>>> for key, value in student.items():
	print(key)

	
name
courses
phone
age
>>> for key, value in student:
	print(key)

	
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    for key, value in student:
ValueError: too many values to unpack (expected 2)
>>> for key, value in student.items():
	print(key, value)

	
name Jane
courses ['Math', 'CompSci']
phone 555-5555
age 26
>>> 
>>> 
>>> courses = ["History", "Math", "Physics", "CompSci"]
>>> print(courses[0:2])
['History', 'Math']
>>> print(courses[:2])
['History', 'Math']
>>> print(courses[2:])
['Physics', 'CompSci']
>>> courses.append("Art")
>>> print(courses)
['History', 'Math', 'Physics', 'CompSci', 'Art']
>>> courses.insert(0, "Bio")
>>> print(courses)
['Bio', 'History', 'Math', 'Physics', 'CompSci', 'Art']
>>> courses_2 = ["Music", "HomeEc"]
>>> courses.insert(0, courses_2)
>>> print(courses)
[['Music', 'HomeEc'], 'Bio', 'History', 'Math', 'Physics', 'CompSci', 'Art']
>>> courses.remove([0])
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    courses.remove([0])
ValueError: list.remove(x): x not in list
>>> courses.extend(0, courses_2)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    courses.extend(0, courses_2)
TypeError: extend() takes exactly one argument (2 given)
>>> courses.extend(courses_2)
>>> print(courses)
[['Music', 'HomeEc'], 'Bio', 'History', 'Math', 'Physics', 'CompSci', 'Art', 'Music', 'HomeEc']
>>> course.remove(["Music", "HomeEc"])
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    course.remove(["Music", "HomeEc"])
NameError: name 'course' is not defined
>>> courses.remove(["Music", "HomeEc"])
>>> print(courses)
['Bio', 'History', 'Math', 'Physics', 'CompSci', 'Art', 'Music', 'HomeEc']
>>> popped = courses.pop()
>>> print(popped)
HomeEc
>>> gone = courses.pop("Bio")
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    gone = courses.pop("Bio")
TypeError: 'str' object cannot be interpreted as an integer
>>> gone - courses.pop([0])
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    gone - courses.pop([0])
NameError: name 'gone' is not defined
>>> gone = courses.pop([0])
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    gone = courses.pop([0])
TypeError: 'list' object cannot be interpreted as an integer
>>> gone = courses.pop(0)
>>> print(gone)
Bio
>>> print(courses)
['History', 'Math', 'Physics', 'CompSci', 'Art', 'Music']
>>> courses.reverse()
>>> courses.sort()
>>> print(courses)
['Art', 'CompSci', 'History', 'Math', 'Music', 'Physics']
>>> nums = [1, 5, 4, 3, 2, 8]
>>> courses.sort()
>>> numbs.sort()
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    numbs.sort()
NameError: name 'numbs' is not defined
>>> nums.sort()
>>> print(nums)
[1, 2, 3, 4, 5, 8]
>>> nums.sort(reverse=True)
>>> print(numbs)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    print(numbs)
NameError: name 'numbs' is not defined
>>> print(nums)
[8, 5, 4, 3, 2, 1]
>>> letters = ["a", "e", "f", "g"]
>>> letters.extend["j", "z", "x", "b"]
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    letters.extend["j", "z", "x", "b"]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> letters.extend(["j", "z", "x", "b"])
>>> 
>>> print(letters)
['a', 'e', 'f', 'g', 'j', 'z', 'x', 'b']
>>> sorted(letters)
['a', 'b', 'e', 'f', 'g', 'j', 'x', 'z']
>>> print(letters)
['a', 'e', 'f', 'g', 'j', 'z', 'x', 'b']
>>> sorted_letters = sorted(letters)
>>> print(sorted_letters)
['a', 'b', 'e', 'f', 'g', 'j', 'x', 'z']
>>> print(min(nums))
1
>>> print(max(nums))
8
>>> a = max(nums)
>>> print(a)
8
>>> print(letters)
['a', 'e', 'f', 'g', 'j', 'z', 'x', 'b']
>>> print(letters.index("f"))
2
>>> print("w" in letters)
False
>>> print("a" in letters)
True
>>> for item in letters:
	print(item)

	
a
e
f
g
j
z
x
b
>>> for index, letter in enumerate(letters):
	print(index, letter)

	
0 a
1 e
2 f
3 g
4 j
5 z
6 x
7 b
>>> for index, letter in enumerate(letters, start=2):
	print(index, letter)

	
2 a
3 e
4 f
5 g
6 j
7 z
8 x
9 b
>>> nums = [2, 3, 4, 1, 2, 5]
>>> letters_str = ",".join(letters)
>>> 
>>> print(letters_str)
a,e,f,g,j,z,x,b
>>> letters_str2 = "-".join(letters)
>>> print(letters_str2)
a-e-f-g-j-z-x-b
>>> new_list = letters_str.split("-")
>>> 
>>> print(new_list)
['a,e,f,g,j,z,x,b']
>>> tuple_1 = ("red", "green", "purple")
>>> print(tuple_1)
('red', 'green', 'purple')
>>> print(tuple_1)
('red', 'green', 'purple')
>>> set1 = {"hi", "hello", "howdy", "hola"}
>>> print("hello" in set1)
True
>>> print("hey" in set1)
False
>>> set2("hey", "hiya", "yo", "holla")
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    set2("hey", "hiya", "yo", "holla")
NameError: name 'set2' is not defined
>>> print(set2.intersection(set1))
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    print(set2.intersection(set1))
NameError: name 'set2' is not defined
>>> set2 = ("hey", "hiya", "yo", "holla")
>>> print(set2.intersection(set1))
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    print(set2.intersection(set1))
AttributeError: 'tuple' object has no attribute 'intersection'
>>> 
