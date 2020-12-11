Python 3.9.0 (v3.9.0:9cf6752276, Oct  5 2020, 11:29:23) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #functions-user defined, method-pre defined
>>> #String methods
>>> x = "Python"
>>> x.upper()
'PYTHON'
>>> #string- immutable->which cannot be changed
>>> x
'Python'
>>> x = x.upper()
>>> x
'PYTHON'
>>> x
'PYTHON'
>>> x.lower()
'python'
>>> x
'PYTHON'
>>> x.casefold() #lower
'python'
>>> x= "HeLLo"
>>> x.swapcase()
'hEllO'
>>> x="functions  -> user defined, method -> pre defined"
>>> x.capitalize() #string-> very first alphabet
'Functions  -> user defined, method -> pre defined'
>>> x.title()
'Functions  -> User Defined, Method -> Pre Defined'
>>> x = "Sahil kumar"
>>> x.replace("kumar","Sharma")
'Sahil Sharma'
>>> x
'Sahil kumar'
>>> x = "aaabbbcccxxxxxxxxxxxx"
>>> x.replace("x","y")
'aaabbbcccyyyyyyyyyyyy'
>>> x.replace("x","y",1)
'aaabbbcccyxxxxxxxxxxx'
>>> x.replace("x","y",5)
'aaabbbcccyyyyyxxxxxxx'
>>> x= "SAhil"
>>> x.center(5)
'SAhil'
>>> x.center(2)
'SAhil'
>>> len(x)
5
>>> x.center(6)
'SAhil '
>>> x.center(7)
' SAhil '
>>> x.center(20)
'       SAhil        '
>>> x.center(20,"*")
'*******SAhil********'
>>> x.center(20,"-")
'-------SAhil--------'
>>> x = x.center(20)
>>> x
'       SAhil        '
>>> x.strip()
'SAhil'
>>> x.lstrip()
'SAhil        '
>>> x.rstrip()
'       SAhil'
>>> x = '-------SAhil--------'
>>> x.strip()
'-------SAhil--------'
>>> x.strip("-")
'SAhil'
>>> x = "@@@@@@@s@ahil@@@@@@@"
>>> x.strip("@")
's@ahil'
>>> x
'@@@@@@@s@ahil@@@@@@@'
>>> x = x.strip("@")
>>> x
's@ahil'
>>> x.zfill(7) #zero fill
'0s@ahil'
>>> x.zfill(20)
'00000000000000s@ahil'
>>> x ='00000000000000s@ahil'
>>> x.count('0')
14
>>> x = "Xyzxyzxyzxyzdsfnkdsl"
>>> x.count('z')
4
>>> x = "String methods"
>>> x.index('S')
0
>>> x.index('t')
1
>>> x.index('t',2)
9
>>> x[9]
't'
>>> x.find('S')
0
>>> x.find('t')
1
>>> x.rfind('t') #reverse find
9
>>> x.find('t',2)
9
>>> x.index("X")
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    x.index("X")
ValueError: substring not found
>>> x.find("X")
-1
>>> #-1 means substring not found
>>> x = "sahil"
>>> x.isalpha()
True
>>> x.isalnum()
True
>>> x.isdigit()
False
>>> x="34"
>>> x.isdigit()
True
>>> x="32432sad"
>>> x.isdigit()
False
>>> x = "hello everyone how are you"
>>> x.split()
['hello', 'everyone', 'how', 'are', 'you']
>>> x = x.split()
>>> x
['hello', 'everyone', 'how', 'are', 'you']
>>> x[0]
'hello'
>>> x[1]
'everyone'
>>> x[-1]
'you'
>>> x = [1,2,45.45,"string",True]
>>> x
[1, 2, 45.45, 'string', True]
>>> x = "hello everyone how are you"
>>> x.split('e')
['h', 'llo ', 'v', 'ryon', ' how ar', ' you']
>>> x
'hello everyone how are you'
>>> y = " Ram"
>>> x+y
'hello everyone how are you Ram'
>>> x = "1"
>>> y = "2"
>>> x+y
'12'
>>> x-y
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    x-y
TypeError: unsupported operand type(s) for -: 'str' and 'str'
>>> x*y
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    x*y
TypeError: can't multiply sequence by non-int of type 'str'
>>> x/y
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    x/y
TypeError: unsupported operand type(s) for /: 'str' and 'str'
>>> x
'1'
>>> x+1
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    x+1
TypeError: can only concatenate str (not "int") to str
>>> x-1
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    x-1
TypeError: unsupported operand type(s) for -: 'str' and 'int'
>>> x/2
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    x/2
TypeError: unsupported operand type(s) for /: 'str' and 'int'
>>> x*1
'1'
>>> x*10
'1111111111'
>>> x = " 1 "
>>> x*10
' 1  1  1  1  1  1  1  1  1  1 '
>>> #AScii ->American standard code for information interchange
>>> "#A"-65
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    "#A"-65
TypeError: unsupported operand type(s) for -: 'str' and 'int'
>>> #chr - character, ord-ordinal function
>>> ord('A')
65
>>> chr(65)
'A'
>>> x = "हेलो क्या  हाल है?"
>>> x
'हेलो क्या  हाल है?'
>>> print(x)
हेलो क्या  हाल है?
>>> x.encode()
b'\xe0\xa4\xb9\xe0\xa5\x87\xe0\xa4\xb2\xe0\xa5\x8b \xe0\xa4\x95\xe0\xa5\x8d\xe0\xa4\xaf\xe0\xa4\xbe  \xe0\xa4\xb9\xe0\xa4\xbe\xe0\xa4\xb2 \xe0\xa4\xb9\xe0\xa5\x88?'
>>> x
'हेलो क्या  हाल है?'
>>> x = x.encode()
>>> x
b'\xe0\xa4\xb9\xe0\xa5\x87\xe0\xa4\xb2\xe0\xa5\x8b \xe0\xa4\x95\xe0\xa5\x8d\xe0\xa4\xaf\xe0\xa4\xbe  \xe0\xa4\xb9\xe0\xa4\xbe\xe0\xa4\xb2 \xe0\xa4\xb9\xe0\xa5\x88?'
>>> x.decode()
'हेलो क्या  हाल है?'
>>> 