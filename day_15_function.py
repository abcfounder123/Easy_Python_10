
"""


Function 

1. Introduction
   - print(), input(), len(), int(input())
   - Function call =>  print, print()
   - Why?
     - Readability, reuse
     - Decomposition
   - Where?
     1. built-in module
     2. preinstalled module  tkinter.py, math.py, .....
     3. external module      PyQt5, numpy
     4. custom function

2. module, package, framwork
   - function (collection of program)         (one purpose - add(), sqrt() )
   - module   (file)   (collection of fun)    (one work - math.py, login.py)
   - package  (folder) (collection of module) (one group - frontend folder)
   - framework(folder) (collection of package)(one project - Django)

3. Function name
   - naming rules
   - same name (last one)
   - should not give the same name

4. Parameterized function
   - parameterized function   => def add(x, y):
   - parameter list           => (x, y), tuple
   - first parameter          => x

5. Arguments(7)
   - value passed by function
   - positional argument  =>  add(1, 2)
   - keyword argument     =>  add(x=1, y=2)
   - ...

6. Local, Global, Built-in
   Local          => local
   Global         => all (local file)
   Built-in       => all file

7. Standrd form(3)

8. Types of parameters(6)

9. Passing correct values to function

10. Checking Parameters

11. Components of function (8)

12. help(), doc

13. Types of function

14. Pure function

15. Exercises(27)

##########################################

Decomposition

     .    .
   X .    .  O
 ----------------
     . X  .  O
 ----------------
     .    .  X
     .    .


Board
draw X
draw O
check win
check tie
marks

##########################################

9. Passing correct values to function

a = 20
b = 10
c = 30
args = (1000, 700, 1100)
user_name = "Mg Mg"
password  = "12345"
kw        = {country: "Myanmar", "age": 10}


a, b, c,                pos
*args                   all pos
user_name, password     keyword
**kw                    all items


def f(a, b, c, /, *args, user_name, password, **kw):
    print(a, b, c)
    print(args)
    print(user_name, password)
    print(kw)


f(20, 10, 30, 1000, 700, 1100, user_name="Mg Mg", password="12345", country="Myanmar", age=10)

##########################################

10. Checking Parameters

No.5 + (No.2 + 4)
help(print)   =>   def print(*args, sep=' ', end='\n', file=None, flush=False):

No.2 + No.3
help(input)   =>   def input(prompt='', /):

No.3
help(len)     =>   def len(obj, /):

##########################################

11. Components of function (8)

1. Function define      =>   def
2. Function name        =>   dollar_kayat
3. Parameter list       =>   (dollar)            
4. Parameters           =>   dollar
5. Code block           =>   :
6. Documentation string =>   triple quotes
7. Function body        =>   programs 
8. return statement     =>   stop, return value


def dollar_kayat(dollar):
    '''This is dollar kayat function.
    eg.
    >> dollar_kayat(1)
    >> 5000

    '''
    kyat = dollar * 5000
    return kyat


##########################################

12. help(), doc

help()
1. function name
2. parameter list
3. documentation string

doc 
1. documentation string

################################################

13. Types of function
1. effect only function    =>  difference_update()
2. result only function    =>  difference()
3. effect and result       =>  pop()

################################################

difference_update
effect = Remove all elements of another set from this set.
result = None

difference
effect = -
result = Return the difference of two or more sets as a new set.

pop
effect = Remove an arbitrary set element
result = return an arbitrary set element

    
len 
effect =  -
result = the number of items in a container   
   
################################################ 

14. Pure function (no side-effect) (result only function) 

Three steps of function


def celsius_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    print(fahrenheit)


def celsius_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32        
    return fahrenheit


def celsius_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32        


################################################

15. Exercises (27)

1. is_even (တန်ဖိုးတစ်ခုခုကို 2 နဲ့စားလို့ အကြွင်း 0 ရရင် စုံကိန်းဖြစ်ပါတယ်။)( n % 2 == 0)

------------------------------------------

2. is_odd (တန်ဖိုးတစ်ခုခုကို 2 နဲ့စားလို့ အကြွင်း 1 ရရင် မကိန်းဖြစ်ပါတယ်။) ( n % 2 == 1 )
    
------------------------------------------

3. is_number (0 1 2 3 4 5 6 7 8 9 စတာတွေဟာ နံပါတ်တွေဖြစ်ကြပါတယ်။) ( c in "0123456789" )

------------------------------------------

4. is_lower (a to z တွေက lower case characterဖြစ်ပါတယ်။)

------------------------------------------

5. is_upper (A to Z တွေက upper case characterဖြစ်ပါတယ်။)

------------------------------------------

6. is_alphabet (a to z တွေက english အက္ခရာဖြစ်ပါတယ်။)

------------------------------------------

7. palindrome (နောက်ပြန်ဖတ်လျှင်လည်း ထပ်တူညီသော စကား) eg. madam ( str == str[::-1] )

------------------------------------------

8. greater number (ပိုကြီးတဲ့ နံပါတ်) ( n1 > n2 )

------------------------------------------

9. less number ( n1 < n2 )

------------------------------------------

10. leap year (ရက်ထပ်နှစ်) (Julian calendar)
 >> divisible by 4  (y % 4 == 0)

------------------------------------------

11. leap year (ရက်ထပ်နှစ်) (Gregorian calendar)
>> divisible by 400 ( eg. 2000, 1600 )       ( y % 400 == 0 )
>> divisible by 4 and not divisible by 100   ( y % 4 == 0 and y % 100 != 0 )
>> Rule.1 or Rule.2

------------------------------------------

12. leap year (ရက်ထပ်နှစ်) Modern calendar
>> divisible by 400 and not divisible by 3200  ( y % 400 == 0 and y % 3200 != 0 )
>> divisible by 4 and not divisible by 100     ( y % 4 == 0 and y % 100 != 0 )

------------------------------------------

Summary
=> +1 days by 4 years                     <---  Julian
=> -3 days by 400 years                   <---  Gregorian
=> -1 days by 3200 years                  <---  Modern

------------------------------------------

13. summation
    => summation of 5 = 1 + 2 + 3 + 4 + 5 = 15

------------------------------------------

14. factorial(n) (မြှောက်ဖော်ကိန်း)
    => factorial of 5 = 1 * 2 * 3 * 4 * 5 = 120

------------------------------------------

15. reverse_string(s) (string ကိုနောက်ကစပြီး ပြောင်းပြန်ရေးခြင်း။) ( [::-1] )
    - "I go to school."
    - ".loohcs ot og I"

------------------------------------------

16. count_vowels(s) (စာလုံးထဲက a, e, i, o, u ရေတွက်ခြင်း။)

------------------------------------------

17. count_vowels(s) (စာလုံးထဲက a, e, i, o, u ဘယ်နှစ်လုံးရှိလဲရေတွက်ခြင်း။)

Add item to dict
d["I"] = 1

Access dict value
d["I"]

Update dict value
d["I"] = 2
d["I"] += 1

------------------------------------------

18. sum_of_list(lst) (စာရင်းထဲက နံပါတ်တွေကို ပေါင်းခြင်း။)

------------------------------------------

19. max(lst) (အများဆုံးတန်ဖိုး ရှာခြင်း။)

------------------------------------------

20. min(lst) (အနည်းဆုံးတန်ဖိုး ရှာခြင်း။)

------------------------------------------

21. find_max_min(lst) အများဆုံးနဲ့ အနည်းဆုံးတန်ဖိုး ရှာခြင်း။

------------------------------------------

22. Lower case to upper case

------------------------------------------

23. Upper case to lower case 

------------------------------------------

24. upper()

------------------------------------------

25. lower()

------------------------------------------

26. Linear search

------------------------------------------

27. Binary search

------------------------------------------------------------------------------------

Answers

1. is_even (တန်ဖိုးတစ်ခုခုကို 2 နဲ့စားလို့ အကြွင်း 0 ရရင် စုံကိန်းဖြစ်ပါတယ်။)( n % 2 == 0)


def is_even(n):
    return n % 2 == 0


------------------------------------------

2. is_odd (တန်ဖိုးတစ်ခုခုကို 2 နဲ့စားလို့ အကြွင်း 1 ရရင် မကိန်းဖြစ်ပါတယ်။) ( n % 2 == 1 )


def is_odd(n):
    return n % 2 == 1


------------------------------------------

def is_even(n):
    return n % 2 == 0


numbers = [100, 105, 3, 9, 1000, 4, 8, 6]
even = []

for number in numbers:
    if is_even(number):
        even.append(number)

print(even)

------------------------------------------

3. is_number (0 1 2 3 4 5 6 7 8 9 စတာတွေဟာ နံပါတ်တွေဖြစ်ကြပါတယ်။) ( c in "0123456789" )

"a"
"6"


def is_number(c):
    return c in "0123456789"


------------------------------------------


def is_number(c):
    return c in "0123456789"


x = '''whgfjew dhu 38dhgjhwgd 383djcgw c8'''
n = 0

for c in x:
    if is_number(c):
        print(f"We found {c}")
        n += 1

print(n)

------------------------------------------

4. is_lower (a to z တွေက lower case characterဖြစ်ပါတယ်။)


def is_lower(c):
    return c in "abcdefghijklmnopqrstuvwxyz"


------------------------------------------

5. is_upper (A to Z တွေက upper case characterဖြစ်ပါတယ်။)


def is_upper(c):
    return c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


------------------------------------------

6. is_alphabet (a to z တွေက english အက္ခရာဖြစ်ပါတယ်။)


def is_alphabet(c):
    return c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


------------------------------------------

7. palindrome (နောက်ပြန်ဖတ်လျှင်လည်း ထပ်တူညီသော စကား) eg. madam ( str == str[::-1] )


def palindrome(s):
    return s == s[::-1]


------------------------------------------

8. greater number (ပိုကြီးတဲ့ နံပါတ်) ( n1 > n2 )


def greater_number(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2


------------------------------------------

9. less number ( n1 < n2 )


def less_number(n1, n2):
    if n1 < n2:
        return n1
    else:
        return n2


------------------------------------------

"Three steps of greater number"

greater_number(2, 1)   =>  2      <-- n1      
greater_number(1, 2)   =>  2      <-- n2           
greater_number(2, 2)   =>  2      <-- n1 or n2  


def greater_number(n1, n2):
    if n1 > n2:
        return n1
    elif n2 > n1:
        return n2
    elif n1 == n2:
        return n2


def greater_number(n1, n2):
    if n1 > n2:
        return n1
    elif n2 > n1:
        return n2
    else:
        return n2


def greater_number(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2

------------------------------------------

"""
