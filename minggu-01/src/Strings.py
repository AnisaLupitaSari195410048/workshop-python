'spam eggs'
#single quotes

'doesn\'t'
#use \' to escape the single quote...

"doesn\'t" 
#...or use double quotes instead

'"Yes," they said.'
#double quotes

"\"Yes,\" they said."
#use \\' to escape the double quote...

'"Isn\'t, " they said.'
#use \' to escape the double quote...

'"Isn\'t," they said.'
#use \' to escape the double quote...

print('"Isn\'t," they said.')
#use \' to escape the double quote...

s = 'First line.\nSecond line.'
# \n means newline

s
# without print(), \n is included in the output

print(s) 
# with print(), \n produces a new line

print('C:\some\name')
# here \n means newline!

print(r'C:\some\name')
# note the r before the quote

# 3 times 'un', followed by 'ium'
 3 * 'un' + 'ium'

 'Py' 'thon'
#Two or more string literals

text = ('Put several strings within parentheses '
...         'to have them joined together.'
text 
#'Put several strings within parentheses to have them joined together.'

prefix = 'Py'
prefix 'thon'  # can't concatenate a variable and a string literal
  File "<stdin>", line 1
    prefix 'thon'
                ^
SyntaxError: invalid syntax
('un' * 3) 'ium'
  File "<stdin>", line 1
    ('un' * 3) 'ium'
                   ^
SyntaxError: invalid syntax
#berfungsi dengan dua literal, tidak dengan variabel atau ekspresi 

prefix + 'thon'
'Python'
#menggabungkan variabel atau variabel dan literal, gunakan + 

word = 'Python'
word[0]  # character in position 0
'P'
>>> word[5]  # character in position 5
'n'
#String dapat diindeks (berlangganan), dengan karakter pertama memiliki indeks 0

word[-1]  # last character
'n'
word[-2]  # second-last character
'o'
word[-6]
'P'
#Indeks juga bisa berupa angka negatif, untuk mulai menghitung dari kanan

word[0:2]  # characters from position 0 (included) to 2 (excluded)
'Py'
>>> word[2:5]  # characters from position 2 (included) to 5 (excluded)
'tho'
#In addition to indexing, slicing is also supported

word[:2]   # character from the beginning to position 2 (excluded)
'Py'
word[4:]   # characters from position 4 (included) to the end
'on'
word[-2:]  # characters from the second-last (included) to the end
'on'
#Slice indices have useful defaults

word[:2] + word[2:]
'Python'
word[:4] + word[4:]
'Python'
#Note how the start is always included, and the end always excluded

 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
#One way to remember how slices work is to think of the indices as pointing between characters

word[42]  # the word only has 6 characters
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
#Attempting to use an index that is too large will result in an error

word[4:42]
'on'
word[42:]
''
#out of range slice indexes are handled gracefully when used for slicing

word[0] = 'J'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> word[2:] = 'py'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
#Python strings cannot be changed — they are immutable

'J' + word[1:]
'Jython'
word[:2] + 'py'
'Pypy'
#If you need a different string, you should create a new one

s = 'supercalifragilisticexpialidocious'
len(s)
34
#The built-in function len() returns the length of a string

