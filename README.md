# Data enumerator lib
This library helps to manipulate the 2d arrays. User can execute functions like addition, substraction, multipliaction and other operations on square matrix and determinant. It also helps user to get equation of graph using arrays, which helps to predict the next value.

## Functionality:-
*	Used to collect user data and process it according to user requirements.
*	Can be used in create recommendation system.
*	Used in deep learning model training.
*	Used in unsupervised machine learning projects.
* Used in predicting data

## Installation
* Run the following command
```
git clone https://github.com/abhineetraj1/dataEnumerator
cd dataEnumerator
```
* Save the test file in this folder in order to import class and functions from enumerator

## Docs :-

### To add two matrix

```
from enumerator import matrix

A=[[1,2],
  [3,4]]
B=[[9,2],
  [3,8]]

C = matrix.add(A,B)

print(C)
```

Output :-
```
[[10,4],
[6,12]]
```
### To substract two matrix

```
from enumerator import matrix

A=[[1,18],
  [3,14]]
B=[[9,2],
  [3,8]]

C = matrix.substract(A,B)

print(C)
```

Output :-
```
[[-8,16],
[0,6]]
```
### To multiply two matrix

```
from enumerator import matrix

A=[[1,2],
  [3,4]]
B=[[0,1],
  [1,0]]

C = matrix.multiply(A,B)

print(C)
```

Output :-
```
[[1,2],
[3,4]]
```
### To get transpose of matrix

```
from enumerator import matrix

A=[[1,2],
  [3,4]]

C = matrix.transpose(A)

print(C)
```

Output :-
```
[[1,3],
[2,4]]
```

### To substract particular number with all the elements of determinant
```
from enumerator import determinant
A = [[2,4],
  [6,7]]

B = determinant.substractNum(2)
print(B)
```
Output :-
```
[[0,2],
[4,5]]
```
### To add particular number with all the elements of determinant
```
from enumerator import determinant
A = [[2,4],
  [6,7]]

B = determinant.addNum(1)
print(B)
```
Output :-
```
[[3,5],
[7,8]]
```
### To divide particular number with all the elements of determinant
```
from enumerator import determinant
A = [[3,9],
  [6,12]]

B = determinant.divideNum(2)
print(B)
```
Output :-
```
[[1,3],
[2,4]]
```
### To multiply particular number with all the elements of determinant
```
from enumerator import determinant
A = [[2,4],
  [6,7]]

B = determinant.substractNum(5)
print(B)
```
Output :-
```
[[10,20],
[30,35]]
```
### Graphical equation handling
```
x_data = [1, 2, 3, 4, 5]
y_data = [2, 4, 6, 8, 10]

graph_fitter = graphEQ(x_data, y_data)

graph_fitter.fit_linear()
print(graph_fitter.get_equation())  # Output: y = 2.00x

graph_fitter.fit_polynomial(2)
print(graph_fitter.get_equation())  # Output: y = 0.00x^2 + 2.00x
```

## Languages used:
<a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>

## Developer
*	[abhineetraj1](http://github.com/abhineetraj1)
