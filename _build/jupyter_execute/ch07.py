#!/usr/bin/env python
# coding: utf-8

# # 제어문

# ## 조건문

# 
# 
# 어떤 일은 특정 조건 하에서만 할 수 있는 경우가 있다.  
# 
# 예를 들어, 주어진 숫자 `num`이 홀수인 경우에만 그 값에 1을 더하라고 할 수 있다.  
# 
# 위 문장을 코드로 나타내려면 아래의 요소들이 필요하다.
# * 주어진 숫자 `num`이 홀수인지 판별하기
# * 이런저런 경우에만 무엇무엇을 하기
# * 주어진 숫자 `num`에 1을 더하기
# 
# <br>  
#   
#   
# * "주어진 `num`가 홀수인지 판별하기"는 아래 수식으로 표현된다.  
# `num % 2 == 1`
# 
# * "이런저런 경우에만 무엇무엇을 해라"는 `if`문으로 나타내며, 아래의 형식을 따른다.
# ```
#     if 이런저런(조건문) :
#         무엇
#         무엇
# ```
# 
# 주의) `if` 조건문 뒤에 반드시 콜론(:)을 써야 한다.  
# 주의) 무엇무엇은 반드시 들여쓰기 해야 한다. 들여쓰기를 하지 않으면 오류가 발생한다.
# 
# * "주어진 숫자 `num`에 1을 더하기"는 아래 수식으로 표현된다.   
# `num + 1`

# ex1) 주어진 숫자 `num`이 홀수인 경우에만 그 값에 1을 더한 값을 출력하여라.

# In[1]:


num = 5 # 다른 값으로 변경 가능

if num % 2 == 1 :
    print(num + 1)


# ex2) 숫자 `num1`이 5보다 큰 경우에만 `num1`을 3으로 나누었을 때의 나머지를 출력하여라.

# In[2]:


num1 = 7  # 다른 값으로 변경 가능

if num1 > 5 :
    print(num1 % 3)


# ex3) 숫자 `num2`가 주어졌을 때, 만약 `num2`가 3의 배수이거나 3으로 끝나는 숫자일 경우에만 `num2`에 5를 더한 값을 출력하여라.
# 
# 참고) "숫자가 3으로 끝난다"는 문자열 메소드 `endswith()`를 활용하면 된다.  
# 참고) `str()` 함수는 숫자를 문자열로 형변환시키는 함수이다.

# In[3]:


num2 = 123

if (num2 % 3 == 0) or (str(num2).endswith('3')) :
    print(num2 + 5)


# 조건문이 참이면 무엇무엇1을 하고, 조건문이 거짓이면 무엇무엇2을 수행하라고 할 때는 `if...else`문을 이용한다. `if...else`문은 아래의 형식을 따른다.   
# ```
#   if 조건문 :
#       무엇무엇1
#   else :
#       무엇무엇2
# ```
# 
# 예제를 통해 살펴보자.

# ex4) `weather`에 `비`가 포함되어 있다면,  
# > 오늘 비가 내립니다.  
# > 우산을 챙기세요! 
# 
# 를 출력하고, `비`가 포함되어 있지 않다면,
# > 비 소식은 없습니다.  
# 
# 를 출력하는 코드를 작성하여라.

# :::{admonition} 참고  
# :class: info
# 문자열에 특정 문자열이 부분 문자열로 포함되어 있는지를 판단해야 하는데, 이때는 `in`을 이용할 수 있다.
# :::

# In[4]:


weather = "오늘 서울 등 중북부지역에는 비가 내립니다." #다른 값으로 변경 가능

if '비' in weather :
    print('오늘 비가 내립니다.')
    print('우산을 챙기세요!')
else:
    print('비 소식은 없습니다.')


# ## 중첩 조건문과 다중 조건문
# 
# 반면에, 예를 들어, 크거나 같거나 작거나 등 세 가지 이상의 경우를 처리하려면 `if...else`문을 중첩해서 사용하거나 `if...elif...elif...else`처럼 다중 조건문을 사용할 수 있다. 
# 
# 예제를 통해 중첩 조건문과 다중 조건문을 살펴보자. 아래는 두 개의 숫자 `num1`과 `num2`가 주어졌을 때, 두 숫자의 크기 비교 결과를 출력해주는 프로그램이다.  
# 

# * 중첩 조건문 활용 예제

# In[5]:


num1 = 5  # 다른 값으로 변경 가능
num2 = 10  # 다른 값으로 변경 가능

if num1 < num2 :
    print("num1이 num2보다 작다.")
else :
    if num1 == num2 :
        print("num1이 num2와 같다.")
    else:
        print("num1이 num2 보다 크다.")


# * 다중 조건문 활용 예제

# In[6]:


num1 = 5 # 다른 값으로 변경 가능
numm2 = 10 # 다른 값으로 변경 가능

if num1 < num2 :
    print("num1이 num2보다 작다.")
elif num1 == num2 :
    print("num1이 num2와 같다.")
else:
    print("num1이 num2보다 크다.")


# 주의) `if` 문의 중첩 정도는 임의로 복잡해질 수 있다. 따라서 가능하면 다중 조건문을 사용한 것이 좋다. 

# # 2. 반복문
# 
# 반복문(루프)은 동일한 코드를 반복해서 실행시킬 때 사용한다. 반복문을 만들기 위해 `while`문과 `for`문을 사용한다.
# 
# 여기서는 먼저 `while` 반복문을 살펴보고 이후에 `for` 반복문을 살펴본다.

# ## `while` 반복문
# 
# `while` 반복문은 항상 아래의 형식을 따른다.
# ```
#   while 조건 :
#       본문코드1
#       본문코드2
#       ...
# ```
# 
# 조건이 참이 되는 동안 본문 코드들이 실행된다.

# ex5) `while`문을 사용해서 다음을 출력하는 프로그램을 작성하여라.
# 
# > 박수 1번 짝  
# > 박수 2번 짝짝  
# > 박수 3번 짝짝짝  
# > 박수 4번 짝짝짝짝  
# > 박수 5번 짝짝짝짝짝

# In[7]:


n = 1

while n < 6 :
    print("박수 ", n, "번 " + "짝" * n)
    n += 1


# 참고) `n += 1`은 `n = n + 1`이다.

# ex6) 정수들을 나누어 몫을 구하는 코드를 작성해보자.   
# 
# 몫을 어떻게 구현할까?  이를 위해
# * 먼저 몫이 어떤 의미인가를 알아야 한다.
# * 그 다음에 그 의미를 구현하는 코드를 작성한다.  
# 
# 어떤 정수 `a`를 다른 정수 `b`로 나누었을 때의 몫은 `a`에서 `b`를 몇 번 뺄 수 있는가와 동일한 의미를 갖는다. 즉, `a`에서 `b`를 반복해서 빼주는 과정이 필요하고 이 과정을 음수가 되지 않을 때까지 반복해야 한다.  
# 
# 예를 들어, 43을 7로 나누었을 때의 몫은 다음과 같이 구할 수 있다.  

# `while` 반복문을 작성할 때 조건문이 언젠가는 만족되지 않아서 더 이상 루프가 돌지 않도록 코드를 작성하는 것이 가장 중요하다. 

# ## `for ` 반복문
# 
# 몇 번 반복되어야 하는지를 아는 경우 `for` 반복문을 사용할 수 있으며, 아래의 형식을 따른다. 
# 
# ```
#   for 변수 in 문자열(또는 리스트, 튜플) :
#       코드1
#       코드2
#       ...
# ```
# 
# 

# ### 문자열과 `for`문
# 
# 아래 코드는 문자열에 포함된 문자 각각을 출력한다.

# In[8]:


for char in "seoul" :
    print(char)


# 이때 `char`를 다른 것으로 변경해도 된다.

# In[9]:


for i in "seoul" :
    print(i)


# ex7) 문자열에 있는 소문자 `p`를 대문자 `P`로 변경하여 새로운 문자열을 생성하는 코드를 작성하여라. 
# 예를 들어, "pineapple"을 이용하여 "PineaPPle"를 생성하는 코드를 작성하여라. 

# In[10]:


a_word = "pineapple"
new_word = ""

for char in a_word :
    if char == 'p' :
        new_word = new_word + "P"
    else :
        new_word = new_word + char

print(new_word)


# ### `range()` 함수와 `for` 문
# 
# `range()` 함수는 일정한 규칙에 따라 나열된 수열을 생성한다.

# In[11]:


a_range = range(10)

print(a_range)


# 참고) 파이썬에서 `range()` 함수의 리턴값은 `range`라는 자료형이다. 뒤에서 다룰 리스트와 거의 비슷하다는 정도만 기억하고 넘어가자. 

# In[12]:


type(a_range)


# `range()` 함수는 인자를 최대 세 개까지 받을 수 있다. 각 인자들의 역할은 슬라이싱에 사용되는 세 개의 인자들의 역할과 동일하다.
# 
# * `range([start, ] stop [, step])`
# * `start`의 경우 주어지지 않으면 `0`을 기본값으로 갖는다.
# * `step`의 경우 주어지지 않으면 `1`을 기본값으로 갖는다.

# In[13]:


a_range_1 = range(3, 10)
a_range_1


# In[14]:


a_range_2 = range(3, 10, 2)
a_range_2


# `range` 함수는 `for` 문에서 유용하게 활용된다. 

# In[15]:


for i in range(6) :
    print(i, "의 제곱은", i**2, "이다.") 


# In[16]:


for i in range(0, 6, 2) :
    print(i, "의 제곱은", i**2, "이다.") 


# 단순한 카운트 역할을 수행하는 용도로 `range` 함수를 활용할 수도 있다. 즉, 어떤 일을 특정 횟수만큼 반복하고자 할 때 사용한다.

# In[17]:


for i in range(5) :
    print("다섯 번 출력합니다.")


# `range()` 함수와 문자열 인덱싱을 활용하면 문자열에 대해 `for` 문을 직접 활용하는 것과 동일한 일을 할 수 있다. 

# 예를 들어, 문자열 인덱싱과 `range()` 함수를 다음처럼 활용할 수 있다.

# In[18]:


a_word = "hamster"

for i in range(7) :
    print(a_word[i])


# In[19]:


a_word = "hamster"

for i in a_word :
    print(i)


# :::{admonition} 주의
# :class: caution  
# 문자열의 길이가 `range()` 함수에 사용되는 인자보다 작으면 오류가 발생한다. 이유는 문자열의 길이보다 큰 인덱스가 사용되기 때문이다. 
# 
# ```python
# >>> for i in range(8) :
#         print(a_word[i])
# h
# a
# m
# s
# t
# e
# r
# ---------------------------------------------------------------------------
# IndexError                                Traceback (most recent call last)
# <ipython-input-21-7b52045b976d> in <module>()
#       1 for i in range(8) :
# ----> 2   print(a_word[i])
# 
# IndexError: string index out of range
# ```
# 
# :::
# 
# 
# 

# 참고) `len()` 함수는 문자열의 길이를 구해준다. 

# In[20]:


for i in range(len(a_word)) :
    print(a_word[i])

