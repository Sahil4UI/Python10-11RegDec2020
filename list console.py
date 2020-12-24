Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = [1,2,3,4,"hi"]
>>> #indexing & slicing
>>> x[0]
1
>>> x[-1]
'hi'
>>> x=[ 1,2,[3,4,[5,6,7,[8,9,10]]]]
>>> x[2][2][3][1]
9
>>> x = [1,2,3,4,5]
>>> x[:]
[1, 2, 3, 4, 5]
>>> x[0:4]
[1, 2, 3, 4]
>>> x[0:4:2]
[1, 3]
>>> x
[1, 2, 3, 4, 5]
>>> x[::-1]
[5, 4, 3, 2, 1]
>>> len(x)
5
>>> for i in range(len(x)):
	print(x[i])

1
2
3
4
5
>>> for data in x:
	print(data)

1
2
3
4
5
>>> x = [-100,-50,-43,-32,24,56,8,43,223]
>>> 