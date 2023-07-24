#!/usr/bin/env python
# coding: utf-8

# # 함수

# 함수<font size="2">Function</font>는 특정 값들을 입력받아 그 값들을 조작한 다음에 그 결과값을 되돌려 주는 것으로, 그동안 여러 함수들(`type`, `int`, `float`, `input` 등등)을 살펴봤다. 이러한 함수들은 파이썬에서 이미 누군가에 의해 정의된 함수로, 파이썬 **내장함수**라고 부른다.

# ## 함수 정의하기
# 
# 한편, 사용자가 필요에 따라 함수를 임의로 정의할 수도 있다. 파이썬에서는 함수를 정의하기 위해 `def`라는 키워드를 이용하며, 아래의 형식을 따른다.
# 
# ```
# def 함수이름(매개변수1, 매개변수2,..., 매개변수n) :
#     함수본문
#     return 리턴값
# ```
# **매개변수**는 함수에 입력으로 전달되는 값을 받는 변수이다.
# 함수본문에서 **`return`** 이라는 키워드에 도달하면 함수의 실행은 그 지점에서 중단되고, 리턴(return)값이 있는 경우에는 함수를 실행한 곳에 그 값을 반환한다. 이때, 리턴값은 `return` 바로 뒤에 오는 값이며, 함수가 특정 인자와 함께 실행되면 함수본문의 코드에 맞게 값을 조작한 후 최종적으로 돌려주는 값을 가리킨다.
# 
# 
# 주의사항 :
# * 콜론(`:`)을 반드시 사용해야 함.
# * 함수본문은 들여쓰기를 해야 함.
# * 들여쓰기는 선택이 아닌 의무사항. 
# 
# 
# 
# 
# 

# 예를 들어, 인자 두 개를 입력받아 합을 리턴하는 함수인 `mySum` 함수는 다음과 같이 정의한다. 함수의 이름은 임의로 정할 수 있지만 함수의 기능에 맞게 정하는 것이 좋다. 

# In[1]:


def mySum(a, b) :
    return a + b


# ##  함수 호출하기
# 
# 함수를 정의한 후에 사용하려면 **함수를 호출**해야 한다.  
# **함수를 호출한다**는 말은 필요한 만큼의 값을 인자로 사용하여 함수를 실행한다는 의미이다. 즉, 함수 호출은 아래 모양의 코드를 실행하는 것이다.  
# 
# 함수를 호출할 때 전달하는 입력값들은 **인자**라고 부른다.  
# ```
# 함수이름(인자1, 인자2,..., 인자n)
# ```

# 예를 들어, 2와 3을 더하려면 `mySum` 함수를 아래와 같은 모양으로 실행하면 된다.  
# `mySum(2, 3)`  
# 
# 물론 변수를 인자로 사용할 수도 있으며, 리턴값을 다른 변수에 저장할 수도 있다. 

# In[2]:


x = 2
y = 3
z = mySum(x, y)


# In[3]:


print(z)


# :::{admonition} 주의   
# :class: caution  
# 매개변수의 개수와 인자의 개수가 맞지 않으면 에러가 발생한다.
# 
# ```python
# >>> mySum(3)
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-26-c1839d4999a5> in <module>()
# ----> 1 mySum(3)
# 
# TypeError: mySum() missing 1 required positional argument: 'b'
# ```
# 
# ```python
# >>> mySum(3, 7, 4)
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-27-a3eeeb0c62f1> in <module>()
# ----> 1 mySum(3, 7, 4)
# 
# TypeError: mySum() takes 2 positional arguments but 3 were given
# ```
# :::
# 

# ## 입력값이 없는 함수
# 
# 입력값이 없다면, 아래와 같이 함수 이름 뒤의 괄호를 비워두면 된다. 
# 
# ```
# def 함수이름() :
#     함수본문
# ```
# 

# 예를 들어, 입력값은 없고 `Hello Python`을 리턴하는 함수인 `say`함수는 다음과 같이 정의한다.

# In[4]:


def say() :
    return "Hello Python"


# `say` 함수를 호출은 아래와 같이 하면 된다. 

# In[5]:


say()


# 함수의 리턴값은 다른 변수에 저장하여 사용할 수도 있다.  
# 예를 들어, 아래와 같이 코드를 작성하면, `a`에 문자열`Hello Python`이 대입된다.    
# ```a = say()``` 

# In[6]:


a = say()

print(a)
print(type(a))


# :::{admonition} 주의   
# :class: caution  
# 입력값이 없는 `say()`함수를 호출할 때는 괄호 안에 아무 값도 넣어서는 안된다.
# 
# ```python
# >>> say("a")
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-7-d9cf60effed3> in <module>()
# ----> 1 say("a")
# 
# TypeError: say() takes 0 positional arguments but 1 was given
# ```
# :::
# 

# ## 리턴값이 없는 함수
# 
# 리턴값이 명시되지 않은 대표적인 함수는 `print` 함수이다. 리턴값이 명시되지 않은 함수의 리턴값은 항상 `None`이다. `None`은 사실상 아무런 의미를 갖지 않는 값이며 어떠한 재활용도 불가능하다. 

# `print` 함수가 리턴하는 값을 확인해보자.  

# In[7]:


x = print("a")
print(x)


# :::{admonition} 주의  
# :class: caution  
# 위 코드를 실행한 결과의 첫째 줄에서 보이는 a는 `print` 함수의 리턴값이 아니라 `print("a")`를 실행한 결과이다.   
# :::

# 예를 들어, `mySum`함수를 아래와 같이 리턴값이 명시되지 않은 함수로 정의할 수도 있다. 

# In[8]:


def mySum_noReturn(a, b) :
    c = a + b
    print(c)


# 위 함수를 이용하여 5와 7를 더한 값을 확인하고자 하면 다음과 같다.

# In[9]:


mySum_noReturn(5, 7)


# 위 코드를 보면 마치 12를 리턴하는 것처럼 보이지만 사실은 `print`함수가 화면에 출력한 결과를 보여주는 것에 불과하다. 실제로 아래와 같이 리턴값을 활용하려면 제대로 동작하지 않는다. 

# In[10]:


ans_noReturn = mySum_noReturn(5, 7)
print(ans_noReturn)


# 파이썬에서 다루는 값은 모두 자료형을 갖고 있으며, `None`의 자료형은 `NoneType`이라 부른다.

# In[11]:


type(ans_noReturn)


# 물론, 입력값도 리턴값도 없는 함수도 만들 수 있다.

# In[12]:


def say_noReturn() :
    print("Hello Python")


# In[13]:


say_noReturn()


# ## 지역변수와 전역변수
# 
# 변수들은 어디에서 정의되었는가에 따라 지역변수(local variable) 또는 전역변수(global variable)라 불린다. 
# 
# 함수 내부에서 선언되는 변수는 함수가 실행되는 동안에만 의미를 갖는 변수들이며, 이런 변수들을 **지역변수**라 부른다.   
# 반면에 함수 외부에서 정의된 변수는 **전역변수**이다.  
# 
# 예를 들어, 아래의 코드에서 `global_var`는 전역변수이고, `local_var`는 지역변수이다.

# In[14]:


global_var = 3

def myAdd(a, b) :
    local_var = a + b
    return local_var


# In[15]:


myAdd(1, 2)


# 지역변수들은 함수 밖에서는 어떤 의미도 갖지 않는다. 예를 들어, 아래의 코드를 실행하면 오류가 발생한다.  
# 
# ```python
# >>> print(local_var)
# ---------------------------------------------------------------------------
# NameError                                 Traceback (most recent call last)
# <ipython-input-3-3bfff76e6cd3> in <module>()
# ----> 1 print(local_var)
# 
# NameError: name 'local_var' is not defined
# ```
# 

# 함수 내부에서 선언된 지역변수를 전역변수처럼 사용하려면 `global` 키워드를 사용한다. 

# In[16]:


global_var = 3

def myAdd(a, b) :
    global local_var  
    local_var = a + b
    return local_var


# In[17]:


myAdd(1, 2)


# In[18]:


print(local_var)


# ## 문서화 문자열(docstring) 활용
# 
# * 프로그래밍 코드를 저장한 파일에는 코드 이외에 코드와 관련된 주석을 적절하게 포함하고 있어야 한다. 이를 "문서화"라고 한다. 
# * 문서화는 코드 이상으로 중요하다. 문서화가 제대로 되어있지 않은 경우 코드 개발 및 관리를 매우 어렵게 만든다.
# * 문서화의 기본은 함수에 주석을 추가하는 것이다. 함수 정의에 사용되는 주석을 **docstring(문서화 문자열)** 이라 부른다.
# * 큰따옴표 세 개("""...""") 또는 작은따옴표 세 개('''...''')로 둘러싸인 부분이 문서화를 위해 사용되며 주석으로 처리된다. 
# * 함수에 주석을 달아주면 `help` 함수를 이용하여 해당 함수의 역할 및 사용법을 확인할 수 있다. 

# 예를 들어, 입력값의 절댓값을 리턴하는 함수인 `abs` 함수에 대한 정보를 확인하기 위해 아래와 같이 코드를 작성하고 실행해보자. 
# > `help(abs)`
# 

# In[19]:


help(abs)


# 출력된 내용을 살펴보면, 다음과 같다.
# 
# * abs는 `builtins`이라는 모듈에 정의된 내장 함수이다. 
# * 인자의 절댓값을 리턴한다. 즉, 어떤 값을 리턴하는지 설명한다.

# 이제 앞에서 정의한 `mySum` 함수에 문서화 문자열(docstring)을 추가해 보자.

# In[20]:


def mySum(a, b) :
    """
    두 개의 숫자를 입력받아, 그 합을 되돌려준다.
    """
    return a + b


# `mySum` 함수에 대한 정보를 확인하기 위해 `help()` 함수를 사용해보자. 그러면 `mySum` 함수를 정의할 때 함께 적은 docstring이 보여진다.

# In[21]:


help(mySum)


# ````{prf:example}
# :label: func_ex01
# 주어진 자연수 `n`이 짝수면 `True`를, 홀수면 `False`를 리턴하는 함수 `even_test(n)`를 구현하여라.
# ````

# In[22]:


def even_test(n):
    if n%2 == 0:
        return True
    else:
        return False


# In[23]:


even_test(10)


# In[24]:


even_test(17)


# :::{admonition} 참고  
# :class: info  
# 정수 1과 0은 각각 `True`와 `False`의 의미를 가질 수 있다.
# :::

# In[25]:


def even_test1(n):
    if not n%2:
        return True
    else:
        return False


# In[26]:


even_test1(16)


# In[27]:


even_test1(21)


# ````{prf:example}
# :label: func_ex02
# 자연수 `n`이 주어졌을 때, 1부터 n까지의 모든 자연수의 곱을 리턴하는 함수 `factorial(n)`을 구현하여라.
# ````

# In[28]:


def factorial(n) :
    result = 1
    for i in range(1, n+1) :
        result *= i
    return result


# In[29]:


print(factorial(0))
print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(10))
print(factorial(30))


# 재귀(recursion)는 "본래 있던 곳으로 다시 돌아온다"는 의미로, 재귀를 이용하여 구현한 함수를 재귀함수(recursive function)라 부른다.  
# 
# 아래는 재귀를 이용하여 구현한 `factorial_func` 함수이다.

# In[30]:


def factorial_func(n) :
    if n == 0 or n == 1 :
        return 1
    else:
        return n*factorial_func(n-1)


# In[31]:


print(factorial_func(0))
print(factorial_func(1))
print(factorial_func(2))
print(factorial_func(3))
print(factorial_func(10))
print(factorial_func(30))


# # 모듈
# 
# 모듈<font size="2">Module</font>은 우선 단순한 파이썬 코드를 담고 있는, 확장자가 `py`인 파일이다. 그리고 하나의 모듈에는 관련된 일을 처리할 때 사용하는 여러 프로그램 코드들이 포함되어 있다. 
# 
# 예를 들어, `math` 모듈은 `sin`, `cos`, `log` 등 수학에서 매우 중요한 역할을 하는 함수들이 정의되어 있다. 그리고 `time` 모듈에는 `sleep` 함수처럼 시간 활용과 관련된 다양한 함수가 포함되어 있다. 
# 
# 참고) 파일 확장자는 파일의 형식이나 종류를 표시하기 위해 파일명 뒤에 사용하는 것이다.   
# 예를 들어, 확장자가 `hwp`라면 한글 문서 파일인 것을 알 수 있다. 

# ## 모듈 사용법
# 
# 특정 모듈에 포함된 코드(예를 들어, 함수)를 사용하려면 먼저 해당 모듈을 `import` 해야 한다.  
# 
# 모듈을 임포트하는 방법을 살펴보자. 

# **모듈 임포트 방법1**
# 
# > `import 모듈이름`
# 
# 예를 들어, `math` 모듈을 임포트하고 싶다면, 아래와 같이 코드를 작성하고 실행하면 된다. 

# In[32]:


import math


# 그러면 `math` 모듈에 포함된 코드를 사용할 수 있다.  
# 예를 들어, `math` 모듈에 포함된 `pi` 값과 `sin` 함수는 아래와 같이 사용할 수 있다.

# In[33]:


math.pi


# In[34]:


math.sin(math.pi/ 2)


# **모듈 임포트 방법2**
# 
# 모듈의 이름이 길 경우, 별칭을 줄 수 있다. 
# 
# > `import 모듈이름 as 별칭`
# 

# In[35]:


import math as m


# In[36]:


m.pi


# In[37]:


m.sin(m.pi/2)


# **모듈 임포트 방법3**
# 
# 모듈에서 원하는 코드만 가져올 수 있다. 이 경우 모듈 이름을 추가로 붙일 필요가 없어진다.   
# 이 방식은 특정 코드를 자주 활용해야 할 경우 추천한다.
# 
# > `from 모듈이름 import 특정코드`

# In[38]:


from math import pi, sin


# In[39]:


pi


# In[40]:


sin(pi/2)


# 주의 : 이 경우 `math` 모듈에 포함된 다른 코드는 사용할 수 없다. 

# **모듈 임포트 방법4**
# 
# 특정 모듈에 포함된 코드 전체를 한꺼번에 임포트할 수도 있다. 다만 일반적으로 추천되는 방식은 아니다.  
# 
# > `from 모듈이름 import *`
# 
# 아래와 같이 `math` 모듈을 임포트하면, 그 안에 포함된 모든 코드를 모듈 이름을 언급할 필요 없이 호출할 수 있다. 

# In[41]:


from math import *


# In[42]:


cos(0)


# In[43]:


exp(1)


# **모듈 내용 확인하기**
# 
# 특정 모듈에 포함된 함수 등을 확인하기 위해 `help` 함수를 사용할 수 있다. 
# 
# > `help(모듈이름)`
# 
# 예를 들어, `math` 모듈에 포함되어 있는 함수들을 확인해보자.

# In[44]:


help(math)


# 만약 `math` 모듈에 포함되어 있는 `sqrt` 함수에 대한 정보를 얻고 싶다면, 다음과 같이 코드를 작성하면 된다. 

# In[45]:


help(math.sqrt)


# ex) 1~100 사이의 정수 맞히기 게임을 만들어라. 

# 참고) 파이썬에서 난수(random number)를 생성하기 위해 `random` 모듈을 사용한다.   
# `random` 모듈의 `randint(a, b)` 함수는 a부터 b사이(끝값 포함)의 임의의 정수를 리턴한다.  
# 예를 들어, `randint(1, 100)`은 1부터 100사이(1과 100포함)의 임의의 정수를 리턴한다.  

# ```python
# import random
# 
# count_trial = 0
# answer = random.randint(1, 100)
# #print(answer)
# 
# while True:
#   
#     try :
#     
#         num_input = input("1에서 100사이의 정수를 입력하세요 :")
#         count_trial = count_trial + 1
#         num_input = int(num_input)
# 
#         if 0 <= num_input <= 100:
# 
#             print("입력하신 정수는", num_input, "입니다.")
# 
#             if num_input == answer:
#                 print("You win!")
#                 print("시도하신 횟수는: ", count_trial, '번 입니다.')
#                 break
# 
#             elif num_input > answer:
#                 print("You lose!")
#                 print("너무 커요(Too high)") 
#             else: 
#                 print("You lose!")
#                 print("너무 작아요(Too low)") 
# 
#         else:
#             print("1에서 100사이의 정수만 입력해야 합니다")
#   
# 
#     except ValueError:
#         print("정수를 입력하세요")
# ```
