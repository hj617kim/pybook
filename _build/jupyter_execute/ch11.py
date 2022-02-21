#!/usr/bin/env python
# coding: utf-8

# # 모음 자료형

# 이번 장에서는 여러 개의 값을 묶어 하나의 값으로 다루는 기본 모음 자료형<font size = "2">Collection Data Types</font>에 대해서 살펴보자.  
# 
# * 시퀀스형 <font size = "2">Sequence Tpyes</font>
#     * 불변 시퀀스 <font size = "2">Immutable Sequences</font>
#         * 문자열 <font size = "2">`str`</font>
#         * 튜플 <font size = "2">`tuple`</font> 
#     * 가변 시퀀스 <font size = "2">Mutable Sequence</font>
#         * 리스트 <font size = "2">`list`</font>
# * 집합형 <font size = "2">Set Types</font>
#     * 집합 <font size = "2">`set`</font>  
#   
# * 매핑형 <font size = "2">Mapping Types</font>
#     * 사전 <font size = "2">`dict`</font>

# :::{admonition}  
# :class: info    
# 한 번 정해지면 절대 변경이 불가능한 자료형을 불변<font size = "2">immutable</font> 자료형, 변경이 가능한 자료형을 가변<font size = "2">mutable</font> 자료형이라 부른다.   
# 
# |자료형|불변/가변|
# |:----------:|:----------:|
# |정수 `int`|불변|
# |부동소수점 `float`|불변|
# |불리언 `bool`|불변|
# |문자열 `str`|불변|
# |리스트 `list`|가변|
# |튜플 `tuple`|불변|
# |집합 `set`|가변|
# |사전 `dict`|가변|  
# 
# :::

# ## 시퀀스형

# 시퀀스형 <font size = "2">Sequence Types 또는 순차 자료형</font>은 값들 사이에 순서를 가지고 있고, 항목의 중복 사용을 허용하는 모음 자료형이다.  
# 예를 들어, 문자열 `str`, 리스트 `list`, 튜플 `tuple` 등이 시퀀스형이다.  

# ### 문자열 `str`

# 문자들을 나열한 값들을 일컫는 자료형으로 작은 따옴표(`'`) 또는 큰 따옴표(`"`)를 사용한다. 

# In[1]:


'Hello, Python!'


# In[2]:


"Hello, Python!"


# #### **빈 문자열**
# 빈 문자열<font size = "2">empty string</font>은 아무것도 포함하지 않는 문자열을 의미한다. 빈 문자열을 만드는 방법은 아래와 같다. 

# In[3]:


empty_str = '' # 또는 ""
empty_str = str()
empty_str


# :::{admonition} `''`과 `' '`의 차이  
# :class: info  
# `''`은 빈문자열로 어떠한 문자도 포함하고 있지 않다. 반면 `' '`은 눈에 보이지는 않지만 공백 문자 하나를 포함하는 문자열이다.
# :::

# #### **부분 문자열 여부 연산자** 
# * `in` : 연산자 왼쪽에 있는 문자열이 오른쪽에 있는 문자열의 부분 문자열로 등장하는지 여부를 알려주는 논리 연산자
# * `not in` : 연산자 왼쪽에 있는 문자열이 오른쪽에 있는 문자열의 부분 문자열로 등장하지 않는지 여부를 알려주는 논리 연산자

# In[4]:


'app' in 'apple'


# In[5]:


'h' in 'banana' 


# In[6]:


'a' not in 'coconut'


# #### `len()` 함수
# `len()`함수 : 문자열의 길이 확인

# In[7]:


len('apple')


# In[8]:


len('hello, world!')


# #### 최대, 최소 함수  
# * `max()` 함수 : 최댓값 확인

# :::{admonition}    
# :class: info  
# 문자열은 사전식의 순서를 사용하며, 공백문자가 가장 작고,  
# 영어 알파벳의 경우 대문자가 소문자보다 작다고 판단한다.
# :::

# In[9]:


max('apple')


# In[10]:


max('Hello, World!')


# * `min()` 함수 : 최솟값 확인

# In[11]:


min('banana')


# In[12]:


min('Hello, World!')


# #### **인덱싱** 

# 문자열에 사용되는 모든 문자는 인덱스<font size = "2">index</font>라는 고유한 번호를 갖는다. 
# 
# * 인덱스는 0부터 시작하며, 오른쪽으로 한 문자씩 이동할 때마다 증가한다.  
# 
# 문자열의 특정 문자를 가져오고 싶을 때는 인덱싱<font size = "2">Indexing</font>을 사용한다. 인덱싱은 다음과 같이 실행한다. 
# 
# ```python
# 문자열변수명[인덱스]
# ```
# 
# * 특정 인덱스 값의 문자 정보를 확인할 때는 대괄호(`[]`)를 사용한다. 

# In[13]:


colors = 'red, blue, yellow'
print(colors[0]) #0번 인덱스 값
print(colors[5]) #3번 인덱스 값


# :::{admonition}  
# :class: caution  
# 
# 문자열의 길이와 같거나 큰 인덱스를 사용하면 오류가 발생한다. 
# ```python
# >>> len(colors)
# 17
# >>> colors[50]
# IndexError                                Traceback (most recent call last)
# /tmp/ipykernel_1817/3232567937.py in <module>
# ----> 1 colors[50]
# 
# IndexError: string index out of range
# ```
# :::

# * 인덱스 값으로 음의 정수를 사용할 수 있다. 파이썬에서는 -1을 마지막 문자의 인덱스로 사용하고, 왼쪽으로 한 문자씩 이동할 때마다 감소한다.  

# In[14]:


colors[-1]


# In[15]:


colors[-2]


# #### 슬라이싱 
# 문자열의 하나의 문자가 아닌 특정 구간 및 부분을 가져올 때는 슬라이싱<font size = "2">Slicing</font>을 사용한다.   
# 슬라이싱은 다음과 같이 실행한다.  
# * 시작인덱스 : 해당 인덱스부터 문자를 추출한다.   
# * 끝인덱스 : 해당 인덱스 전까지의 문자를 추출한다.   
# * 계단<font size = "2"></font> : 시작인덱스부터 몇 계단씩 건너뛰며 문자를 추출할지 결정한다. 예를 들어, 계단값이 2라면 하나 건너 추출한다.   
# 
# ```python
# 문자열변수명[시작인덱스 : 끝인덱스 : 계단(step)]
# ```  
#     

# In[16]:


colors = 'red, blue, yellow'


# `colors`에서 `red`를 추출하고 싶다면 다음과 같이 하면 된다. 

# In[17]:


colors[0 : 3 : 1]


# `colors`에서 `b`부터 끝까지 하나씩 건너서 추출하려면 다음과 같이 하면 된다. 

# In[18]:


colors[5 : len(colors) : 2]


# 양의 정수와 음의 정수를 섞어서 인덱스로 사용할 수 있다.

# In[19]:


colors[5 : -1 : 2]


# * 시작인덱스, 끝인덱스, 계단 각각의 인자는 경우에 따라 생략될 수도 있다. 그럴 때는 각각의 위치에 기본값<font size = "2">default</font>이 들어 있는 것으로 처리되며, 기본값은 다음과 같다.  
#     * `시작인덱스`의 기본값 : `0`  
#     * `끝인덱스`의 기본값 : 문자열의 길이  
#     * `계단`의 기본값 : `1`

# In[20]:


colors[ : 3 : ]


# In[21]:


colors[ : 3] #계단을 생략할 떄는 콜론(:)도 함께 생략가능


# In[22]:


colors[5 : : 2]


# :::{admonition}  
# :class: info   
# 슬라이싱은 기본적으로 작은 인덱스에서 큰 인덱스 방향으로 확인한다. 역순으로 추출하고자 한다면 계단<font size = "2">step</font>에 음의 정수를 사용하면 된다.   
# 
# 단, 계단이 `-1`일 때 시작인덱스와 끝인덱스를 생략하면 각각 `0`과 문자열의 길이가 들어 있는 것으로 처리되지 않고, 문자열을 역순으로 가져온다.  
# ```python 
# >>> colors[ : : -1]
# 'wolley ,eulb ,der'
# ```
# :::

# #### 문자열 메서드 
# 
# 문자열 자료형에만 사용하는 함수들이 있다. 이와같이 특정 자료형에만 사용하는 함수들을 메서드<font size = "2">method</font>라 부른다.   
# 
# 메서드는 일반적인 함수들과는 달리, 특정 자료형의 값을 먼저 언급하고 바로 이어서 점(`.`)을 찍은 다음 호출한다.
# 
# ```python
# 문자열변수명.메서드
# ```

# 문자열 자료형이 제공하는 주요 메서드는 아래 표와 같다. 

# In[23]:


words = ' My life is so cool, my life is so cool '
words


# |메서드|설명|예시|실행결과|
# |:----------:|:----------:|:----------:|:----------:|
# |`str.count()`|지정된 문자열이 등장한 횟수 반환|`words.count('so')`|`2`|
# |`str.find()`|지정된 문자열이 처음 등장한 위치 반환. 지정된 문자열이 없다면 -1반환|`words.find('life')`|`4`|
# |`str.index()`|지정된 문자열이 처음 등장한 위치 반환. 지정된 문자열이 없다면 오류발생|`words.index('My')`|`1`|
# |`str.lower()`|문자열에 사용된 문자를 모두 소문자로 변환하여 반환|`words.lower()`|`' my life is so cool, my life is so cool '`|
# |`str.upper()`|문자열에 사용된 문자를 모두 대문자로 변환하여 반환|`words.upper()`|`' MY LIFE IS SO COOL, MY LIFE IS SO COOL '`|
# |`str.replace()`|하나의 문자열을 다른 문자열로 대체하여 반환|`words.replace('so ', '')`|`' My life is cool, my life is cool '`|
# |`str.lstrip()`|문자열 왼쪽에 지정된 문자열을 삭제하여 반환. 지정된 문자열이 없는 경우 왼쪽 공백들을 삭제하여 반환|`words.lstrip()`|`'My life is so cool, my life is so cool '`|
# |`str.rstrip()`|문자열 오른쪽에 지정된 문자열을 삭제하여 반환. 지정된 문자열이 없는 경우 오른쪽 공백들을 삭제하여 반환|`words.rstrip()`|`' My life is so cool, my life is so cool'`|
# |`str.strip()`|문자열 양쪽에 지정된 문자열을 삭제하여 반환. 지정된 문자열이 없는 경우 양쪽 공백들을 삭제하여 반환|`words.strip()`|`'My life is so cool, my life is so cool'`|
# |`str.split()`|지정된 문자열을 기준으로 쪼개진 문자열들의 리스트 반환. 지정된 문자열이 없는 경우 공백을 기준으로 쪼개진 문자열의 리스트 반환|`words.split()`|`['My', 'life', 'is', 'so', 'cool,', 'my', 'life', 'is', 'so', 'cool']`|
# |`str.join()`|지정된 문자열의 각각 문자 사이에 문자를 삽입하여 반환|`'-'.join('Hello')`|`'H-e-l-l-o'`|
# |`str.format()`|문자열 포매팅|`'My {} is so cool'.format('life')`|`'My life is so cool'`|

# ### 리스트 `list`

# 리스트는 파이썬에서 사용할 수 있는 임의의 값들을 모아서 하나의 값으로 취급하는 자료형으로, 리스트의 형식은 다음과 같다. 

# `[항목1, 항목2, 항목3, ..., 항목n]`

# 대괄호(`[]`)를 사용하고, 각 항목은 콤마(`,`)로 구분한다. 

# In[24]:


[1, 2, 3, 4, 5]


# In[25]:


['a', 'b', 'c']


# 리스트는 아래와 같은 방식으로 타입 힌트를 추가한다.  
# 기본 자료형의 정의는 타이핑<font size = "2">typing</font> 모듈에 포함되어 있다. 

# In[26]:


from typing import List
a_list : List[int] = [5, 10, 15, 20]


# 리스트는 아래와 같이 서로 다른 자료형의 항목들을 포함할 수 있지만 항목들이 모두 같은 자료형인 경우를 많이 사용한다. 

# In[27]:


mixed_list = [1, 2.3, 'abc', True, [1, 2], ('a', 'b')]
mixed_list


# :::{admonition}  
# :class: info  
# 
# 리스트에 포함된 항목들 사이의 순서는 중요하다. 리스트 항목의 순서 또는 개수가 다르면 서로 다른 리스트로 처리된다.  
# 
# ```python 
# >>> [1, 2] == [2, 1]
# False
# >>> [1] == [1, 1]
# True
# ``` 
# :::

# #### 빈 리스트
# 빈 리스트<font size = "2">empty list</font>는 아무것도 포함하지 않는 리스트를 의미한다. 빈 리스트를 만드는 방법은 아래와 같다. 

# In[28]:


empty_list = []
empty_list = list()
empty_list


# :::{admonition}  
# :class: caution  
# 아래 `a_singleton`은 빈 리스트가 아니라 빈 리스트를 포함하는 리스트이다. 
# 
# ```python
# >>> a_singleton = [[]]
# >>> print(a_singleton)
# [[]]
# ```
# :::

# :::{admonition}  
# :class: info  
# 
# 변수 `a`와 `b`에 각각 빈 리스트를 할당하면, 두 개는 서로 다르고 독립적이다.  
# 반면 `c = a`라고 하면, `a`와 `c`는 동일하다. 예를 들어, `a`에 정수 `1`를 추가하면
# `c`에도 `1`이 추가된다. 
# 
# ```python
# >>> a = []
# >>> b = []
# >>> c = a
# >>> a.append(1)
# >>> print(a)
# [1]
# >>> print(b)
# []
# >>> print(c)
# [1]
# ```
# 
# <div align="center">
#     <img src="https://raw.githubusercontent.com/hj617kim/pybook/master/images/ch11/list01.png" style="width:400px;">
#     <img src="https://raw.githubusercontent.com/hj617kim/pybook/master/images/ch11/list02.png" style="width:400px;">
# </div>
# 
# 아래와 같이 `a = c = []`라고 코드를 작성해도, `a`와 `c`는 동일하다. 
# ```python 
# >>> a = c = []
# >>> print( a is c)
# True
# ```
# 
# :::

# #### 항목 포함 여부 연산자 
# * `in` :  연산자 왼쪽에 있는 값이 오른쪽에 있는 리스트의 항목으로 등장하는지 여부를 알려주는 논리 연산자
# * `not in` : 연산자 왼쪽에 있는 값이 오른쪽에 있는 리스트의 항목으로 등장하지 않는지 여부를 알려주는 논리 연산자

# In[29]:


3 in [1, 2, 3, 4, 5]


# In[30]:


'a' in [1, 2, 3, 4, 5]


# In[31]:


'a' not in [1, 2, 3, 4, 5]


# #### 리스트 연산  
# 리스트는 사칙연산 중 덧셈과 곱셈 연산자를 사용할 수 있다. 

# In[32]:


['a', 'b'] + ['b', 'c', 'd']


# In[33]:


['a', 'b'] * 2


# #### `len()`함수   
# `len()`함수 : 리스트의 길이 확인

# In[34]:


a_list = [3, 15, 9, 12]
print(len(a_list))


# #### 최대, 최소 함수
# 
# * `max()` 함수 : 최댓값 확인

# In[35]:


a_list = [3, 15, 9, 12]
max(a_list)


# * `min()` 함수 : 최솟값 확인

# In[36]:


a_list = [3, 15, 9, 12]
min(a_list)


# #### 인덱싱과 슬라이싱 
# 
# 리스트도 문자열처럼 인덱싱<font size = "2">Indexing</font>과 슬라이싱이 가능하다. 

# In[37]:


a_list = [3, 15, 9, 12, 7, 14, 10]
print(a_list[0])
print(a_list[-1])
print(a_list[2:6:2])


# 리스트는 가변 자료형이라 값을 수정할 수 있다. 인덱싱과 슬라이싱을 사용하여 수정해보자.  

# In[38]:


a_list = [3, 15, 9, 12, 7, 14, 10]


# 예를 들어, 인덱싱을 사용하여 `a_list[3]`을 `12`에서 `100`으로 변경할 수 있다. 

# In[39]:


print(a_list)
a_list[3] = 100
print(a_list)


# 이번에는 슬라이싱을 사용하여 2번 인덱스 값부터 5번 인덱스 값 전까지를 1과 11로 변경해보자. 

# In[40]:


print(a_list)
a_list[2 : 5] = [1, 11]
print(a_list)


# `del` 명령어를 사용하여 리스트의 일부 또는 전체를 삭제할 수 있다. 

# In[41]:


print(a_list)
del a_list[0]
print(a_list)


# :::{admonition}  
# :class: caution  
# `del`은 매우 주의해서 사용해야 한다. 잘못하면 데이터 자체를 메모리에서 삭제시킬 수도 있다. 
# :::

# :::{admonition}  
# :class: caution  
# 문자열은 불변 자료형이라 인덱싱과 슬라이싱을 사용하여 값을 변경할 수 없다.  
# ```python
# >>> a_word = 'hello'
# >>> a_word[0] = 'H'
# TypeError                                 Traceback (most recent call last)
# /tmp/ipykernel_1817/217255829.py in <module>
#       1 a_word = 'hello'
# ----> 2 a_word[0] = 'H'
# 
# TypeError: 'str' object does not support item assignment
# ```
# :::

# #### 리스트 메서드 
# 리스트 자료형이 제공하는 주요 메서드는 아래와 같다.

# |메서드|설명|
# |:----------:|:----------:|
# |`list.append()`|리스트 끝에 항목 추가. 반환값은 `None`|
# |`list.extend()`|리스트를 연결하여 확장. 반환값은 `None`|
# |`list.insert()`|지정된 인덱스에 항목 추가. 반환값은 `None`|
# |`list.pop()`|지정된 인덱스의 항목 삭제 후 삭제된 값 반환. 지정된 인덱스가 없다면 마지막 항목 삭제 후 삭제된 값 반환|
# |`list.remove()`|지정된 항목이 처음으로 사용된 위치에서 삭제. 반환값은 `None`|
# |`list.sort()`|리스트의 항목을 크기 순으로 정렬. 반환값은 `None`|
# |`list.reverse()`|리스트의 항목들 순서 뒤집기. 반환값은 `None`|
# |`list.index()`|지정된 항목이 처음 위치한 인덱스 반환|
# |`list.count()`|지정된 항목이 등장한 횟수 반환|
# 
# 

# In[42]:


food = ['banana', 'apple', 'coconut', 'apple']


# * `append()`  : 리스트 끝에 항목 추가. 반환값은 `None`   
# 
# 예를 들어, `append()`메서드를 사용하여 리스트 `food` 끝에 `'durian'`을 추가해보자. `append()`메서드의 반환값은 `None`이다. 

# In[43]:


print(food.append('durian'))


# In[44]:


print(food)


# 리스트 끝에 `eggplant`와 `fig`를 아래와 같이 추가해보자. 

# In[45]:


food.append(['eggplant', 'fig'])
food


# 그러면 `food` 리스트 끝에 두 개의 항목이 추가되는 것이 아니라 `['eggplant', 'fig']`리스트가 추가된 것을 볼 수 있다.  
# 지금은 `del`을 사용하여 추가된 마지막 항목을 삭제한다. 

# In[46]:


del food[-1]


# 두 개의 항목을 리스트에 추가하고자 한다면 `append()` 메서드를 두 번 적용하거나 `extend()` 메서드를 사용하면 된다.  

# * `extend()` : 리스트를 연결하여 확장. 반환값은 `None`

# In[47]:


food.extend(['eggplant', 'fig'])
food


# :::{admonition}  
# :class: info  
# 두 개의 리스트를 덧셈 기호를 이용하여 확장할 수도 있지만, 원래의 리스트를 변경하는 것이 아니라 새로운 리스트를 생성한다.
# :::

# * `insert()` : 지정된 인덱스에 항목 추가. 반환값은 `None`

# In[48]:


food.insert(1, 'blueberry')
food


# * `pop()` : 지정된 인덱스의 항목 삭제 후 삭제된 값 반환. 지정된 인덱스가 없다면 마지막 항목 삭제 후 삭제된 값 반환.

# In[49]:


food.pop()


# In[50]:


food


# In[51]:


food.pop(0)


# In[52]:


food


# * `remove()` : 지정된 항목이 처음으로 사용된 위치에서 삭제. 반환값은 `None`

# In[53]:


food.remove('apple')
food


# * `sort()` : 리스트의 항목을 크기 순으로 정렬. 반환값은 None  
#     * 숫자의 경우, 크기 순서대로
#     * 문자의 경우, 사전식으로

# In[54]:


food.sort()


# In[55]:


food


# * `reverse()` : 리스트의 항목들 순서 뒤집기. 반환값은 None

# In[56]:


food.reverse()


# In[57]:


food


# * `index()` : 지정된 항목이 처음 위치한 인덱스 반환.

# In[58]:


food.index('coconut')


# * `count()` : 지정된 항목이 등장한 횟수 반환

# In[59]:


food.count('apple')


# ### 튜플 `tuple`

# 튜플은 리스트와 거의 비슷하지만, 수정 불가능<font size = "2">immutable</font>하다는 점이 다르다. 튜플의 형식은 아래와 같다. 

# `(항목1, 항목2, 항목3, ..., 항목n)`

# 소괄호(`()`)를 사용하고, 각 항목은 콤마(`,`)로 구분한다. 

# In[60]:


(1, 2, 3, 4, 5)


# In[61]:


('a','b', 'c', 'd')


# 튜플은 아래와 같은 방식으로 타입 힌트를 추가한다.  

# In[62]:


from typing import Tuple 
a_tuple : Tuple[int, int, str] = (2022, 12345, '강현')
a_tuple


# 튜플은 아래와 같이 서로 다른 자료형의 항목들을 포함할 수 있지만, 일반적으로 항목들이 모두 같은 자료형인 경우를 많이 사용한다. 

# In[63]:


mixed_tuple = (1, 2.3, 'abc', False, ['ab', 'c'], (2, 4))
mixed_tuple


# #### 빈 튜플
# 빈 튜플<font size = "2">empty tuple</font>은 아무것도 포함하지 않는 튜플을 의미한다. 빈 튜플를 만드는 방법은 아래와 같다. 

# In[64]:


empty_tuple = ()
empty_tuple = tuple()
empty_tuple


# #### 항목 포함 여부 연산자 
# * `in` :  연산자 왼쪽에 있는 값이 오른쪽에 있는 튜플의 항목으로 등장하는지 여부를 알려주는 논리 연산자
# * `not in` : 연산자 왼쪽에 있는 값이 오른쪽에 있는 튜플의 항목으로 등장하지 않는지 여부를 알려주는 논리 연산자

# In[65]:


'1' in ('a', 'bc', 'd', 'e')


# In[66]:


'd' in ('a', 'bc', 'd', 'e')


# In[67]:


'f' not in ('a', 'bc', 'd', 'e')


# #### 튜플 연산  
# 튜플은 사칙연산 중 덧셈과 곱셈 연산자를 사용할 수 있다. 

# In[68]:


('a', 'b') + ('b', 'c', 'd')


# In[69]:


('a', 'b') * 2


# #### `len()`함수  
# len()함수 : 튜플의 길이 확인

# In[70]:


len(('a', 'b', 'c', 'd'))


# #### 최대, 최소 함수
# 
# * `max()` 함수 : 최댓값 확인

# In[71]:


max((2, 9, 11, 20, 3))


# * `min()` 함수 : 최솟값 확인

# In[72]:


min((2, 9, 11, 20, 3))


# #### 인덱싱과 슬라이싱

# 튜플도 문자열과 리스트처럼 인덱싱과 슬라이싱이 가능하다. 

# In[73]:


a_tuple = (3, 15, 9, 12, 7, 14, 10)
print(a_tuple[0])
print(a_tuple[-1])
print(a_tuple[2:6:2])


# :::{admonition}  
# :class: caution  
# 튜플은 불변 자료형이라 값을 수정할 수 없다. 예를 들어, 아래와 같이 인덱싱을 사용하여 튜플의 항목을 변경하려고 하면 오류가 발생한다.   
# 
# ```python
# >>> a_tuple = (3, 15, 9, 12, 7, 14, 10)
# >>> a_tuple[0] = 100
# TypeError                                 Traceback (most recent call last)
# /tmp/ipykernel_1817/347940049.py in <module>
#       1 a_tuple = (3, 15, 9, 12, 7, 14, 10)
# ----> 2 a_tuple[0] = 100
# 
# TypeError: 'tuple' object does not support item assignment
# ```
# :::

# :::{admonition}  
# :class: info  
# 
# 튜플이 변경 불가능한 자료형이라고 해서 튜플의 모든 항목이 모두 변경 불가능해야 하는 것은 아니다. 예를 들어, `tup`의 첫번째 항목은 `[1, 2]`이고, 리스트는 변경가능한 자료형이다. 따라서 아래와 같이 첫번째 항목 자체는 변경이 가능하다. 
# ```python
# >>> tup = ([1, 2], 10, 100)
# >>> tup[0].append(3)
# >>> print(tup)
# ([1, 2, 3], 10, 100)
# ```
# 
# 이러한 성질이 가능한 이유는 아래와 같다.  
# `tup`은 `([1, 2], 10, 100)`을 참조한다. 그리고 첫번째 항목인 `[1, 2]` 또한 참조 형태로 다른 메모리에 저장된다. 즉, `tup`의 첫번째 항목은 `[1, 2]`가 저장된 위치의 주소이다. 그런데 `[1, 2]`가 변경되어도 주소 자체는 변하지 않는다. 따라서 `tup` 입장에서는 변한 것이 하나도 없다. 
# 
# <div align="center">
#     <img src="https://raw.githubusercontent.com/hj617kim/pybook/master/images/ch11/tuple01.png" style="width:400px;">
#     <img src="https://raw.githubusercontent.com/hj617kim/pybook/master/images/ch11/tuple02.png" style="width:400px;">
# </div>
# 
# 
# :::

# #### 튜플 메서드

# 튜플은 불변 자료형이라 메서드가 별로 없다. 많이 사용되는 두 개의 메소드를 살펴보자.   
# 
# |메서드|설명|
# |:----------:|:----------:|
# |`tuple.count()`|지정된 항목이 등장한 횟수 반환|
# |`tuple.index()`|지정된 항목이 처음 위치한 인덱스 반환|

# In[74]:


num_tuple = (1, 2, 3, 1, 3, 5, 5, 10, 15)
print(num_tuple.count(1))
print(num_tuple.index(5))


# ### `zip()` 함수 

# 시퀀스(예, 문자열, 리스트, 튜플) 여러 개의 항목을 순서대로 짝지어 튜플의 리스트 형식의 객체를 생성한다. 자료형이 달라도 된다. 단, `zip()` 함수의 반환값은 구체적으로 명시되지 않는다. 

# In[75]:


zip("abc", [1, 2, 3])


# `list()`함수를 이용하여 리스트로 변환하면, 쉽게 내용을 확인할 수 있다. 

# In[76]:


list(zip("abc", [1, 2, 3]))


# 여러 개를 짝짓는 것도 가능하며, 각 자료형의 길이가 다르면 짧은 길이에 맞춰서 짝을 짓는다. 

# In[77]:


list(zip("abcdefgh",(1, 2, 3, 4, 5), [5, 10, 15]))


# ### 해체 방법

# 시퀀스 항목 각각을 변수에 지정하고자 할 때는 해체하는 방법을 사용한다. 단, 사용되는 변수의 수는 항목의 수와 일치해야 한다.   
# 예를 들어, 세 개의 항목을 갖는 시퀀스를 해체하려면 세 개의 변수가 필요하다. 

# In[78]:


a, b = "12"
c, d, e = [3, 4, 5]
f, g = (6, 7)
print(a) 
print(type(a)) # 타입은 문자열이다.
print(b) #타입 - str
print(c) #타입 - int
print(d) #타입 - int
print(e) #타입 - int
print(f) #타입 - int
print(g) #타입 - int


# 굳이 이름을 주지 않아도 되는 항목이 있다면 변수 대신에 밑줄<font size = "2">underscore</font>(`_`) 기호를 사용한다.   
# 예를 들어, 변수 `d`가 필요없다면 아래와 같이 해체할 수 있다. 

# In[79]:


c, _, e = [3, 4, 5]
print(c + e)


# :::{admonition}  
# :class: caution  
# 시퀀스 항목 각각을 변수에 지정하고자 할 때는 사용되는 변수의 수와 항목의 수는 일치해야 한다.
# 
# ```python
# >>> c, e = [3, 4, 5]
# ValueError                                Traceback (most recent call last)
# /tmp/ipykernel_1817/4065688922.py in <module>
# ----> 1 c, e = [3, 4, 5]
#       2 print(c + e)
# 
# ValueError: too many values to unpack (expected 2)
# ```
# :::

# 반면에 앞에 몇 개만 변수에 할당하고 나머지는 하나의 리스트로 묶을 수도 있다. 이를 위해 별표 기호<font size = "2">asterisk</font>(`*`)를 하나의 변수명과 함께 사용한다. 

# In[80]:


values = (1, 2, 3, 4, 5)
a, b, *rest = values
print(a)
print(b)
print(rest)


# 나머지 항목들을 무시하고 싶다면, 별표와 밑줄을 함께 사용한다. 

# In[81]:


a, b, *_ = values
print(a)
print(b)


# ## 집합형

# ### 집합

# 집합<font size = "2">set</font>형은 수학에서 다루는 집합과 비슷한 자료형으로 형식은 아래와 같다.  

# `{항목1, 항목2, 항목3, ..., 항목n}`

# 중괄호(`{}`)를 사용하고, 각 항목은 콤마(`,`)로 구분한다.

# 집합은 항목의 중복을 허용하지 않고, 항목들 사이의 순서는 무시된다. 

# In[82]:


a_set = {4, 9.2, "apple", True, 4}
a_set


# :::{admonition}  
# :class: info  
# 집합의 원소는 모두 해시 가능이어야 한다. 즉, 리스트는 집합의 원소가 될 수 없다. 
# ```python
# >>> {[1, 3], 4}
# TypeError                                 Traceback (most recent call last)
# /tmp/ipykernel_1817/2739416386.py in <module>
# ----> 1 {[1, 3], 4}
# 
# TypeError: unhashable type: 'list'
# ```
# :::

# :::{admonition} 해시 가능 <font size = "2">hashable</font>
# :class: info  
# 
# 어떤 객체가 변하지 않는 해시값을 갖고, 다른 객체와 비교될 수 있으면 해시 가능이라고 한다.  
# 파이썬의 모든 불변 내장 객체들은 해시 가능하다. 반면 리스트나 딕셔너리와 같은 가변 객체들은 해시 불가능이다.  
# 집합의 원소나 딕셔너리의 키는 해시 가능한 것만 사용할 수 있다. 
# 
# 
# `hash()` 함수를 사용하여 해시 가능 여부를 확인할 수 있다.   
# `hash()` 함수는 해시 가능일 때는 특정 정수를 반환하고, 불가능일 때는 오류가 발생한다.  
# ```python
# >>> hash(1)
# 1
# >>> hash([1, 2])
# TypeError                                 Traceback (most recent call last)
# /tmp/ipykernel_1817/3864786969.py in <module>
# ----> 1 hash([1, 2])
# 
# TypeError: unhashable type: 'list'
# ```
# 
# :::

# :::{admonition}  
# :class: caution  
# 집합은 순서가 없는 자료형이라 인덱싱이나 슬라이싱을 지원하지 않는다.   
# ```python
# >>> a_set[0]
# TypeError                                 Traceback (most recent call last)
# /tmp/ipykernel_1817/3483571857.py in <module>
# ----> 1 a_set[0]
# 
# TypeError: 'set' object is not subscriptable
# ```
# :::

# 집합은 아래와 같은 방식으로 타입 힌트를 추가한다.  

# In[83]:


from typing import Set 
a_set : Set[int] = {1, 5, 9, 7}
a_set


# #### 빈 집합

# 빈 집합<font size = "2">empty set</font>은 아무것도 포함하지 않는 집합을 의미한다. 빈 집합를 만드는 방법은 아래와 같다. 

# In[84]:


empty_set = set()
empty_set


# :::{admonition}  
# :class: caution  
# 
# 빈 집합을 만들 때는 `set()`을 사용해야 한다. `{}`은 빈 딕셔너리이다. 
# ```python
# >>> a = {}
# >>> type(a)
# dict
# ```
# :::

# #### 항목 포함 여부 연산자 
# * `in` :  연산자 왼쪽에 있는 값이 오른쪽에 있는 집합의 항목으로 등장하는지 여부를 알려주는 논리 연산자
# * `not in` : 연산자 왼쪽에 있는 값이 오른쪽에 있는 집합의 항목으로 등장하지 않는지 여부를 알려주는 논리 연산자

# In[85]:


1 in {1, 2, 3, 9, 4}


# In[86]:


'a' not in {1, 'b', True, 9}


# #### 집합 연산

# 집합에서 사용할 수 있는 연산자는 아래와 같다. 

# |연산자|설명|예시|실행결과|
# |:----------:|:----------:|:----------:|:----------:|
# |`\|`|합집합|`{1, 2} \| {2, 4}`|`{1, 2, 4}`|
# |`&`|교집합|`{1, 2} & {2, 4}`|`{2}`|
# |`-`|차집합|`{1, 2} - {2, 4}`|`{1}`|
# |`<=`|부분집합 여부|`{1, 2} <= {2, 4}`|`False`|

# In[87]:


{1, 2, 3, 4, 5} | {2, 4, 6}


# In[88]:


{1, 2, 3, 4, 5} & {2, 4, 6}


# In[89]:


{1, 2, 3, 4, 5} - {2, 4, 6}


# In[90]:


{1, 2, 3, 4, 5} <= {2, 4, 6}


# In[91]:


{1, 2} <= {1, 2, 3, 4, 5}


# :::{admonition}  
# :class: caution  
# 
# 집합은 덧셈과 곱셈 연산자를 사용할 수 없다. 
# 
# ```python 
# >>> {1, 2} + {3, 4, 5}
# TypeError                                 Traceback (most recent call last)
# /tmp/ipykernel_1817/437379440.py in <module>
# ----> 1 {1, 2} + {3, 4, 5}
# 
# TypeError: unsupported operand type(s) for +: 'set' and 'set'
# 
# >>> {1, 2} * 2
# TypeError                                 Traceback (most recent call last)
# /tmp/ipykernel_1817/650599529.py in <module>
# ----> 1 {1, 2} * 2
# 
# TypeError: unsupported operand type(s) for *: 'set' and 'int'
# ```
# :::

# #### `len()` 함수  
# len()함수 : 집합의 길이 확인

# In[92]:


len({1, 3, 5, 7, 9})


# #### 최대, 최소 함수
# 
# * `max()` 함수 : 최댓값 확인

# In[93]:


max({1, 3, 5, 7, 9})


# * `min()` 함수 : 최솟값 확인

# In[94]:


min({1, 3, 5, 7, 9})


# #### 집합 메서드  
# 집합 자료형이 제공하는 주요 메서드는 아래와 같다.

# |메서드|설명|예시|실행결과|
# |:----------:|:----------:|:----------:|:----------:|
# |`set.union()`|합집합 반환|`{1, 2}.union({3, 4})`|`{1, 2, 3, 4}`|
# |`set.intersection()`|교집합 반환|`{1, 2, 3}.intersection({3, 4})`|`{3}`|
# |`set.difference()`|차집합 반환|`{1, 2, 3}.difference({3, 4})`|`{1, 2}`|
# |`set.issubset()`|부분 집합 여부를 판단하여 반환|`{1, 2, 3}.issubset({3, 4})`|`False`|
# |`set.add()`|항목추가. 반환값은 `None`|||
# |`set.remove()`|특정 항목 삭제. 반환값은 `None`|||
# |`set.pop()`|임의의 항목 삭제. 반환값은 삭제하는 항목. 빈 집합에 사용하면 오류 발생|||
# |`set.clear()`|모든 항목을 삭제. 반환값은 `None`|||
# |`set.update()`|여러 개의 항목 한번에 추가. 반환값은 `None`|||

# In[95]:


a_set = {1, 2, 3}
a_set.add(8)
print(a_set)


# In[96]:


a_set.remove(1)
print(a_set)


# In[97]:


print(a_set.pop())
print(a_set)


# In[98]:


a_set.clear()
print(a_set)


# In[99]:


a_set.update({5, 10, 15})
print(a_set)


# ## 매핑형

# ### 사전  
# 사전형 또는 딕셔너리<font size = "2">dictionary</font> 자료형은 키<font size = "2">keys</font>와 값<font size = "2">values</font>으로 이루어진 항목<font size = "2">items</font>들의 집합으로, 사전에서 단어의 뜻을 확인하는 방식과 유사하게 활용할 수 있는 자료구조를 가지고 있다. 예를 들어, 영어 사전에서 `world`란 단어의 뜻을 물으면 `세계`라는 뜻을 알려주는 데, 이때 `world`는 키<font size = "2">key</font>에 해당하고, `세계`는 값<font size = "2">value</font>에 해당한다.   
# 
# 딕셔너리의 형식은 아래와 같다.   
# 
# `{key1 : value1, key2 : value2, key3 : value3, ...}`  
# 
# `key : value` 형태로 이루어진 여러 개의 항목들이 중괄호(`{}`)로 묶여있고, 각 항목들은 콤마(`,`)로 구분한다.  
# 
# 예를 들어, key가 `'Hello'`, `'World'`이고, 각각의 key에 해당하는 value가 `'안녕'`, `'세계'`인 딕셔너리 `dic`를 만드는 코드를 아래와 같다. 

# In[100]:


dic = {'Hello' : '안녕', 'World' : '세계'}
dic


# :::{admonition}  
# :class: info  
# 해시 가능한 것만 딕셔너리의 키로 사용될 수 있다. 예를 들어, 정수, 실수, 문자열, 튜플 등이다.  
#  
# ```python
# >>> dic = {1 : 5, 2.5 : [3, 4], 'a' : (2, 7, 4), (1, 2) : 'd'}
# >>> print(dic)
# {1: 5, 2.5: [3, 4], 'a': (2, 7, 4), (1, 2): 'd'}
# ```
# 
# 단, 키로 사용되는 튜플의 항목에 리스트 등 변경 가능한 값이 사용되지 않아야 한다. 
# ```python
# >>> {([1, 2], 3): 1}
# TypeError                                 Traceback (most recent call last)
# /tmp/ipykernel_1817/230770617.py in <module>
# ----> 1 {([1, 2], 3): 1}
# 
# TypeError: unhashable type: 'list'
# ```
# :::

# 사전은 아래와 같은 형식으로 타입 힌트를 추가한다. 

# In[101]:


from typing import Dict
a_dict : Dict[str, str] = {"name": "강현", "age": "3"}


# #### 빈 사전

# 빈 사전 또는 빈 딕셔너리<font size = "2">empty dictionary</font>는 아무것도 포함하지 않는 사전을 의미한다. 빈 사전를 만드는 방법은 아래와 같다. 

# In[102]:


empty_dict = {}
empty_dict = dict()
empty_dict


# #### 항목 포함 여부 연산자 
# * `in` :  연산자 왼쪽에 있는 값이 오른쪽에 있는 사전의 키로 등장하는지 여부를 알려주는 논리 연산자
# * `not in` : 연산자 왼쪽에 있는 값이 오른쪽에 있는 사전의 키로 등장하지 않는지 여부를 알려주는 논리 연산자

# In[103]:


'city' in {"name": "강현", "age": "3"} 


# In[104]:


'city' not in {"name": "강현", "age": "3"} 


# #### `len()` 함수 
# len()함수 : 사전에서 항목의 길이 확인

# In[105]:


len({"name": "강현", "age": "3"}) 


# #### 최대, 최소 함수
# 
# * `max()` 함수 : 사전의 키의 최댓값 확인

# In[106]:


max({1 : 'one', 2 : 'two', 3 : 'three'})


# * `min()` 함수 : 사전의 키의 최솟값 확인

# In[107]:


min({1 : 'one', 2 : 'two', 3 : 'three'})


# #### 인덱싱  
# 딕셔너리에서 항목의 순서는 중요하지 않다. 그보다 어떤 키<font size = "2">key</font>가 사용되었는지가 중요하다.  
# 딕셔너리에서 인덱싱은 키를 이용한다. 예를 들어, 아래 딕셔너리 `dic`에서 `'Hello'`에 대응하는 값을 확인하고자 하면  
# 다음과 같이 대괄호를 사용하는 인덱싱을 이용한다. 

# In[108]:


dic = {'Hello' : '안녕', 'World' : '세계'}
dic['Hello']


# :::{admonition}  
# :class: caution  
# 
# 존재하지 않는 키로 값을 추출하려고 하면, 오류가 발생한다. 
# ```python
# >>> dic = {'Hello' : '안녕', 'World' : '세계'}
# >>> dic['Python']
# KeyError                                  Traceback (most recent call last)
# /tmp/ipykernel_1817/1517958361.py in <module>
# ----> 1 dic['Python']
# 
# KeyError: 'Python'
# ```
# :::

# #### 항목의 추가와 삭제  
# * 아래와 같은 형식으로 사전에 항목을 추가한다.  
# `사전변수명[key] = value`   
# 
# 예를 들어, `dic`에 key와 value가 각각 `Python`과 `파이썬`인 항목을 추가하는 코드는 아래와 같다.   

# In[109]:


dic = {'Hello' : '안녕', 'World' : '세계'}
print(dic)
dic['Python'] = '파이썬'
print(dic)


# :::{admonition}  
# :class: caution  
# 이미 사용하고 있는 키를 가진 항목을 추가하려고 하면, 그 키로 저장된 이전 값은 사라진다.  
# ```python
# >>> dic = {'Hello' : '안녕', 'World' : '세계'}
# >>> print(dic)
# {'Hello': '안녕', 'World': '세계'}
# >>> dic['World'] = '세상'
# >>> print(dic)
# {'Hello': '안녕', 'World': '세상'}
# ```
# :::

# * 사전의 항목은 `del` 명령어를 사용하여 삭제할 수 있다. 

# In[110]:


dic = {'Hello' : '안녕', 'World' : '세계'}
print(dic)
del dic['World']
print(dic)


# #### 사전 메서드  
# 집합 자료형이 제공하는 주요 메서드는 아래와 같다.

# |메서드|설명|예시|실행결과|
# |:----------:|:----------:|:----------:|:----------:|
# |`dict.keys()`||``|``|
# |`dict.values()`||``|``|
# |`dict.items()`||``|``|
# |`dict.get()`||``|``|
# |`dict.clear()`||``|``|
