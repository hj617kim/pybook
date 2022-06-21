#!/usr/bin/env python
# coding: utf-8

# # 기본자료형

# 자료형<font size = "2">Data Type</font>은 컴파일러나 인터프리터에게 데이터를 어떻게 사용할 것인지 알려주는 데이터 속성 중 하나다.   
# 이번 장에서는 파이썬 프로그래밍 언어에서 사용되는 기본 자료형을 간단히 살펴보자. 
# 
# * 정수 <font size = "2">`int`</font> 
# * 부동소수점 <font size = "2">`float`</font> 
# * 불리언 <font size = "2">`bool`</font>
# * 문자열 <font size = "2">`str`</font>

# ## 정수

# 일반적으로 알고 있는 정수(자연수, 0, 음의 정수)들의 자료형이다. 정수형으로 나타내면 덧셈, 뺄셈, 곱셈, 나눗셈 등의 기본 연산이 가능하다.  
# 예를 들어, ..., -3, -2, -1, 0, 1, 2, 3, ...은 모두 정수형(`int`)이다. 

# ## 부동 소수점

# 부동소수점은 원래 실수를 컴퓨터에서 다루기 위해 개발되었으나 실제로는 유리수 일부만을 다룬다. 무리수인 원주율 $\pi$의 경우에도 컴퓨터의 한계로 인해 소수점 이하 적당한 자리에서 끊어서 사용한다. 예를 들어, 1.2, 0.333, -1.2, -3.7680, 4.0 등은 모두 부동소수점형(`float`)이다.  

# ### 기본 연산

# 파이썬의 기본 연산을 표로 정리하면 아래와 같다. 

# |연산 기호|의미|예시|실행 결과|
# |:----------:|:----------:|:----------:|:--------:|
# |`+`|덧셈| `3 + 4` |`7`|
# |`-`|뺄셈| `7 - 2` | `5`|
# |`*`|곱셈| `2 * 6` | `12`|
# |`/`|나눗셈|`14 / 4`|`3.5`|
# |`**`|지수|`2 ** 3`|`8`|
# |`//`|몫|`9 // 2`|`4`|
# |`%`|나머지|`3 % 2`|`1`|

# * 지수승을 나타내는 기호는 `**`이다. 예를 들어, 2의 세제곱을 계산하고자 할 때 사용한다. 

# In[1]:


2 ** 3


# In[2]:


9 ** 0.5


# * 몫을 계산하는 연산자는 `//`이다. 

# In[3]:


7 // 5


# In[4]:


7.0 // 5


# In[5]:


-7 // 5


# In[6]:


-7.0 // 5


# * 나머지를 계산하는 연산자는 `%`이다. 

# In[7]:


7 % 5


# In[8]:


-7 % 5


# :::{admonition} 참고 
# :class: info
# 
# (a // b) * b + a % b 를 구하면 a이다. 
# :::

# In[9]:


7 == (7 // 3) * 3 + 7 % 3


# In[10]:


-5 == (-5 // 2) * 2 + (-7 % 2)


# ## 문자열 

# 문자들을 나열한 값들을 일컫는 자료형으로 작은 따옴표(`'`) 또는 큰 따옴표(`"`)를 사용한다. 

# In[11]:


'Hello, World'


# In[12]:


"Hello, World"


# :::{admonition} 문자열 `''`과 문자의 `' '` 차이첨 
# :class: info
# 
# 빈 문자열<font size = "2">empty string</font> `''`는 아무런 문자도 포함하지 않았기 때문에 문자열의 길이 즉, 문자열에 포함된 문자의 개수가 0이다.   
# 반면 `' '`는 눈에 보이지는 않지만 공백 문제 하나를 포함하는 문자열이며 길이가 1이다. 
# :::

# ````{prf:example}
# :label: my-example
# 
# `Hello, "World"`를 보이는 그대로 출력하는 코드를 작성하여라. 
# ````

# 문자열 내부에서 큰 따옴표를 사용하고 싶을 때는 작은 따옴표로 문자열을 감싸면 된다. 

# In[13]:


print('Hello, "World"')


# 백슬래시(`\`, 한글 키보드에서는 원화기호￦를 사용)를 사용하여 문자열 내부에서 사용되는 따옴표의 특수 역할을 해제<font size = "2">escape</font>할 수 있다. 

# In[14]:


print("Hello, \"World\"")


# 반대로 문자열 내부에서 작은 따옴표를 사용하고 싶을 때는 큰 따옴표로 문자열을 감싸면 된다.

# In[15]:


print("I'm a student")


# 여러 줄로 이루어진 문자열은 삼중 따옴표(`''' '''` 또는 `""" """`)를 사용할 수 있다. 

# In[16]:


print('''
Hello,
 World
''')


# In[17]:


print("""
Hello,
 World
""")


# ### 기본 연산

# |연산 기호|의미|예시|실행 결과|
# |:----------:|:----------:|:----------:|:--------:|
# |`+`|덧셈| `'Hello ' + 'python'` |`'Hello python'`|
# |`*`|곱셈| `3*'Hello '` | `Hello Hello Hello `|

# In[18]:


name = "강현"
print("안녕, " + name)


# In[19]:


"Hello " * 3


# In[20]:


2 * "Hi "


# :::{admonition} 주의 
# :class: caution  
# 변수에 할당된 값의 자료형에 따라 연산의 가능 여부가 결정된다. 예를 들어, 숫자와 문자열의 합은 정의되지 않으며, 실행할 경우 오류가 발생한다.  
# 
# ```python
# >>> 2 + name
# TypeError                                 Traceback (most recent call last)
# /tmp/ipykernel_279/3370966941.py in <module>
# ----> 1 2 + name
# 
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# ```
# :::

# ### 문자열에 특수 문자 활용하기

# 백슬래시(￦), 줄바꾸기(￦n), 탭(￦t) 등은 문자열에 사용될 경우 특수한 기능을 갖는다. 그리고 백슬래시(`\`)기호를 붙여서 특수 기능을 해제<font size= "2">escape</font>할 수 있다.

# In[21]:


print("Hello\\n World")


# In[22]:


print("Hello\\t World")


# In[23]:


print("Good\\night")


# 연속된 백슬래시 두 개를 출력하려면 아래와 같이 해야 한다.

# In[24]:


print("\\\\")


# :::{admonition} 주의
# :class: caution
# 
# 아래와 같이 코드를 작성하면 오류가 발생하므로 주의해야 한다.
# ```python
# >>> print("\\\")
#   File "/tmp/ipykernel_76/2337434698.py", line 1
#     print("\\\")
#                 ^
# SyntaxError: EOL while scanning string literal
# ```

# :::{admonition} 참고 
# :class: info  
# **순수 문자열**
# '가공되지 않은'의 의미를 갖는 'raw' 단어의 첫 글자인 'r'을 문자열 앞에 두면 특수 기능이 사라진다.
# :::

# In[25]:


print(r"Hello\n World")


# In[26]:


print(r"Hello\t World")


# In[27]:


print(r"Hello\ World")


# ## 불리언

# 불리언<font size = "2"> bool </font>은 참(`True`)과 거짓(`False`)를 나타내는 자료형이다. 파이썬에서 불리언 자료형은 `int` 형의 자식형<font size = "2"> subtype</font>이고, 대부분의 상황에서 `True`와 `False`는 각각 `1`과 `0`처럼 동작한다. 

# ### 논리 연산자

# |연산 기호|의미|예시|실행 결과|
# |:----------:|:----------:|:----------:|:--------:|
# |`and`|그리고|`True and False`|`False`|
# |`or`|또는|`True or False`|`True`|
# |`not`|부정|`not False`|`True`|

# :::{admonition} 참고 
# :class: info
# 
# `x and y`는 `x`가 참일 때만 `y`를 확인한다.  
# `x or y`는 `x`가 거짓일 때만 `y`를 확인한다.
# 
# 예를 들어, 아래와 같이  `False and 3/0`를 실행하면 `False`가 나온다. 
# ```python
# >>> False and 3/0
# ```
# 
# 하지만 반대로 `3/0 and False`를 실행하면 오류가 발생한다. 
# ```python
# >>> False and 3/0
# ZeroDivisionError                         Traceback (most recent call last)
# /tmp/ipykernel_422/2156724109.py in <module>
# ----> 1 True and 3/0
# 
# ZeroDivisionError: division by zero
# ```
# :::

# ### 비교 연산자

# |연산 기호|의미|예시|실행 결과|
# |:----------:|:----------:|:----------:|:--------:|
# |`<`|작다|`2 < 1`|`False`|
# |`<=`|작거나 같다|`1 <= 2`|`True`|
# |`>`|크다|`2 > 1`|`True`|
# |`>=`|크거나 같다|`1 >= 2`|`False`|
# |`==`|같다|`1 == '1'`|`False`|
# |`!=`|같지 않다|`1 != '1'`|`True`|

# 서로 다른 숫자형을 제외하고는 서로 다른 형은 같다고 비교되지 않는다. 

# 예를 들어, 정수 `1`와 부동소수점 `1.0`이 같은지 여부를 확인해보자.

# In[28]:


1 == 1.0


# 반면, 정수 `1`과 문자열 `'1'`은 형<font size = "2">type</font>이 달라서 같은지 여부를 확인해보면, `False`가 나온다.

# In[29]:


1 == '1'


# In[30]:


1 == 1.0


# 문자열도 비교연산자를 사용할 수 있다.   
# 크기 비교 연산자들은 영어 사전식의 알파벳 순서를 사용한다. 

# In[31]:


'apple' == 'pineapple'


# In[32]:


'apple' < 'banana'


# :::{admonition} 참고 
# :class: info
# 영어 알파벳의 경우 대문자가 소문자보다 작다고 판단한다.
# :::

# ## 형변환 함수

# 형변환<font size = "2"> type casting</font>은 자료형을 변환하는 것으로, 파이썬은 다양한 형변환 함수를 제공한다.   
# 
# * `int()` : 정수형으로 변환. 부동소수점을 정수로 변환할 때, 소수점 이하는 버려진다. 
# * `float()` 부동소수점형으로 변환.
# * `str()` : 문자열형으로 변환.
# * `bool()` : 불리언형으로 변환  

# In[33]:


int(4.8)


# In[34]:


int('5')


# In[35]:


int(True)


# In[36]:


float(3)


# In[37]:


float('7.9')


# In[38]:


str(6)


# :::{admonition} 주의 
# :class: caution  
# `int()`함수의 인자로 문자열을 사용할 때는 그 모양이 정수모양이어야 하고, `float()` 함수의 인자로 문자열을 사용할 때는 그 모양이 정수 또는 부동소수점 모양이어야 한다. 
# 
# ```python
# >>> int('5.0')
# ValueError                                Traceback (most recent call last)
# /tmp/ipykernel_279/3485297474.py in <module>
# ----> 1 int('5.0')
# 
# ValueError: invalid literal for int() with base 10: '5.0'
# ```
# ```python
# >>> float('5GB')
# ValueError                                Traceback (most recent call last)
# /tmp/ipykernel_279/814975516.py in <module>
# ----> 1 float('5GB')
# 
# ValueError: could not convert string to float: '5GB'
# ```
# :::

# :::{admonition} 참고 
# :class: info
# `bool()` 함수는 `0`, `0.0`, `''`(빈 문자열)처럼 0이거나 비어 있는 값을 인자로 사용하면 `False`를 반환한다.  
# :::

# In[39]:


print(bool(0))
print(bool(0.0))
print(bool(''))
print(bool(2))
print(bool(4.2))
print(bool('Hello'))


# :::{admonition} 주의 
# :class: caution 
# 변수를 형변환한다고 해서 변수에 할당된 값이 변하는 것은 아니다. 다만, 형변환한 값을 다른 변수에 저장해서 사용할 수는 있다. 
# :::

# In[40]:


basic_int = 2
print(float(basic_int))
print(type(basic_int))


# In[41]:


float_basic_int = float(basic_int)
print(float_basic_int)
print(type(float_basic_int))

