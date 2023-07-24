#!/usr/bin/env python
# coding: utf-8

# # 오류 및 예외처리

# 아래의 코드는 정수를 입력받아 그 정수의 제곱을 출력하는 내용을 담고 있다. 코드를 실행하면 숫자를 입력하라는 창이 나오고, 여기에 정수 6을 입력하면 정상적으로 작동한다. 하지만, 예를 들어, 3.5를 입력하면 값 오류(value error)가 발생한다. `int()` 함수는 정수모양의 문자열에만 사용할 수 있기 때문이다.  
# 
# ```python
# >>> int_num = int(input("정수를 입력하세요 : "))
# 정수를 입력하세요 : 6
# >>> print("입력한 정수", int_num, "의 제곱은", int_num**2, "입니다.")
# 입력한 정수 6 의 제곱은 36 입니다.
# ```
# 
# ```python
# >>> int_num = int(input("정수를 입력하세요 : "))
# 정수를 입력하세요 : 3.5
# ---------------------------------------------------------------------------
# ValueError                                Traceback (most recent call last)
# <ipython-input-16-451164c00bbc> in <module>()
# ----> 1 int_num = int(input("정수를 입력하세요 : "))
#       2 print("입력한 정수", int_num, "의 제곱은", int_num**2, "입니다.")
# 
# ValueError: invalid literal for int() with base 10: '3.5'
# ```
# 

# 프로그램을 만들다보면 여러 오류가 발생할 수 있다. 파이썬은 오류가 발생하면 오류 메시지를 보여주며 프로그램을 중단한다. 하지만 때로는 오류를 다른 방식으로 처리하고 싶을 때도 있다. 여기서 그에 대한 해결책을 다루고자 한다. 

# ## 오류
# 
# 

# 오류를 처리하는 방법을 살펴보기 전에, 발생할 수 있는 오류 몇 가지를 살펴보자. 오류의 종류를 파악하면 어디서 왜 오류가 발생하였는지를 보다 쉽게 파악하여 코드를 수정할 수 있게 된다.  
# 
# 다음의 코드들은 모두 오류를 발생시킨다.

# **문법 오류** 
# 
# > `"Hello, world`
# 
# 주의) 문자열 양 끝의 큰따옴표(또는 작은따옴표)가 짝이 맞아야 한다.  
# 
# ```python
# >>> "Hello, world
#   File "<ipython-input-19-a5674619cc6b>", line 1
#     "Hello, world
#                  ^
# SyntaxError: EOL while scanning string literal
# ```

# 오류 메시지를 간단히 살펴보자. 
# 
# * `File "<ipython-input-19-a5674619cc6b>", line 1`  
# 1번 줄에서 오류 발생
# 
# * 
# ```
#     "Hello, world
#                  ^
# ```
# 오류 발생 위치 명시
# 
# * `SyntaxError: EOL while scanning string literal`  
# 오류 종류 표시 : 문법 오류(SyntaxError) 

# **0으로 나누기 오류**
# > `3 / 0` 
# 
# 주의) 0으로 나눌 수 없다.

# ```python
# >>> print(3/0)
# ---------------------------------------------------------------------------
# ZeroDivisionError                         Traceback (most recent call last)
# <ipython-input-18-01a2217119a3> in <module>()
# ----> 1 print(3/0)
# 
# ZeroDivisionError: division by zero
# ```

# **들여쓰기 문법 오류**
# 
# >
# ```
# for i in range(5) :
#   i -= 2
#     print(i)
# ```
# 
# 주의) 2번 줄과 3번 줄의 들여쓰기 정도가 동일해야 한다.

# ```python
# >>> for i in range(5) :
#       i -= 2
#         print(i)
#   File "<ipython-input-22-2f6d86e4660a>", line 3
#     print(i)
#     ^
# IndentationError: unexpected indent
# ```

# **자료형 오류**
# 
# 아래의 연산은 모두 오류를 발생시킨다.
# 
# >
# ```
# 'cat' - 'dog'
# 'cat' * 'dog'
# 'cat' / 'dog'  
# ```
# >
# ```
# 'cat' + 2
# 'cat' - 2
# 'cat' / 2
# ```
# 
# 주의) 문자열끼리의 합, 문자열과 정수의 곱셈만 정의되어 있다.

# ```python
# >>> 'cat' - 'dog'
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-23-47e5dc8c518e> in <module>()
# ----> 1 'cat' - 'dog'
# 
# TypeError: unsupported operand type(s) for -: 'str' and 'str'
# ```

# **이름 오류**
# 
# >`print(dog)`
# 
# 주의) 미리 선언된 변수만 사용할 수 있다.

# ```python
# >>> print(dog)
# ---------------------------------------------------------------------------
# NameError                                 Traceback (most recent call last)
# <ipython-input-24-6857f2fb20da> in <module>()
# ----> 1 print(dog)
# 
# NameError: name 'dog' is not defined
# ```

# **인덱스 오류**
# 
# >
# ```
# a_word = "hello"
# a_word[20]
# ```
# 
# 주의) 인덱스는 문자열의 길이보다 작은 수만 사용할 수 있다.

# ```python
# >>> a_word = "hello world"
# >>> a_word[20]
# ---------------------------------------------------------------------------
# IndexError                                Traceback (most recent call last)
# <ipython-input-27-d2dfe20b8f53> in <module>()
#       1 a_word = "hello world"
# ----> 2 a_word[20]
# 
# IndexError: string index out of range
# ```

# **값 오류**
# >`int(a_word)`
# 
# 주의) `int()` 함수는 정수모양의 문자열만 처리할 수 있다.

# ```python
# >>> int(a_word)
# ---------------------------------------------------------------------------
# ValueError                                Traceback (most recent call last)
# <ipython-input-28-412cfee654a9> in <module>()
# ----> 1 int(a_word)
# 
# ValueError: invalid literal for int() with base 10: 'hello world'
# ```

# **속성 오류**
# 
# >`a_word.split().strip()`
# 
# 주의) `a_word`는 문자열이지만, `a_word.split()`는 리스트이다.  
# 리스트에는 `strip()` 메소드가 없다. 리스트는 이후에 다룬다.

# ```python
# >>> a_word.split().strip()
# ---------------------------------------------------------------------------
# AttributeError                            Traceback (most recent call last)
# <ipython-input-30-09c69b8a8996> in <module>()
# ----> 1 a_word.split().strip()
# 
# AttributeError: 'list' object has no attribute 'strip'
# ```

# 지금 살펴본 오류 외에도 다양한 오류가 발생할 수 있다. 그때마다 스스로 오류의 내용과 원인을 확인해 나가는 과정이 필요하다.

# ## 예외처리
# 
# 프로그램 중간에 오류가 발생할 수 있는 경우를 미리 생각하여 대비하는 과정을 **예외처리(exception handling)** 라고 부른다.  
# 
# 예를 들어, 오류가 발생하더라도 오류발생 이전까지 생성된 정보들을 저장하거나, 오류발생 이유를 조금 더 자세히 다루거나, 아니면 오류발생에 대한 보다 자세한 정보를 사용자에게 알려주기 위해 예외처리를 사용한다.  
# 
# 사용방식은 다음과 같다.
# >
# ```
# try :
#     코드1
# except :
#     코드2
# ```
# 
# * 먼저 코드1 부분을 실행한다.
# * 코드1 부분이 실행되면서 오류가 발생하지 않으면 코드2 부분은 무시하고 다음으로 넘어간다.
# * 코드1 부분이 실행되면서 오류가 발생하면 더이상 진행하지 않고 바로 코드2 부분을 실행한다.

# 예시를 통해 살펴보자.  
# 
# 아래의 코드는 문법적 오류는 없지만, 정수가 아닌 값을 입력하면 값 오류(value error)가 발생한다. 

# ```python
# >>> int_num = int(input("정수를 입력하세요 : "))
# 정수를 입력하세요 : 3.5
# ---------------------------------------------------------------------------
# ValueError                                Traceback (most recent call last)
# <ipython-input-31-451164c00bbc> in <module>()
# ----> 1 int_num = int(input("정수를 입력하세요 : "))
#       2 print("입력한 정수", int_num, "의 제곱은", int_num**2, "입니다.")
# 
# ValueError: invalid literal for int() with base 10: '3.5'
# ```

# 이런 경우, `try...except` 문을 이용하여 예외처리를 할 수 있다.  
# 
# 예를 들어, 정수가 아닌 값을 입력하면, `"정수를 입력해야 합니다."`라는 문구를 출력할 수 있다.

# ```python
# >>> num = input("정수를 입력하세요: ")
# 정수를 입력하세요: 6
# >>> try :
#         int_num = int(num)
#         print("입력한 정수", int_num, "의 제곱은", int_num**2, "입니다.")
#     except :
#         print("정수를 입력해야 합니다.")
# 입력한 정수 6 의 제곱은 36 입니다.
# ```

# ```python
# >>> num = input("정수를 입력하세요: ")
# 정수를 입력하세요: 3.5
# >>> try :
#         int_num = int(num)
#         print("입력한 정수", int_num, "의 제곱은", int_num**2, "입니다.")
#     except :
#         print("정수를 입력해야 합니다.")
# 정수를 입력해야 합니다.
# ```

# 올바른 값이 나올 때까지 입력을 요구할 수도 있다. 

# ```python
# >>> while True :
#         try :
#             int_num = int(input("정수를 입력하세요: "))
#             print("입력한 정수", int_num, "의 제곱은", int_num**2, "입니다.")
#             break
#         except :
#             print("정수를 입력해야 합니다.")
# 정수를 입력하세요: 3.5
# 정수를 입력해야 합니다.
# 정수를 입력하세요: 3.7
# 정수를 입력해야 합니다.
# 정수를 입력하세요: 6
# 입력한 정수 6 의 제곱은 36 입니다.
# ```

# 참고) `break`는 가장 가까이서 둘러싸는 하나의 `for`나 `while` 루프로부터 빠져나가게 만든다. 

# 오류 종류에 맞추어 다양한 대처를 하기 위해서는 오류의 종류를 명시하여 예외처리를 하면된다. 예제를 통해 살펴보자.
# 예제는 0이 아닌 정수를 입력받아 10을 입력받은 수로 나눈 값을 출력하는 코드로, 입력 값에 따라 다른 오류가 발생하고 그에 상응하는 방식으로 예외처리를 한다. 

# **값 오류(ValueError)의 경우**

# ```python
# >>> num = input("0이 아닌 정수를 입력하세요 : ")
# 0이 아닌 정수를 입력하세요 : 3.5
# >>> try :
#         int_num = int(num)
#         ans = 10 /int_num
#         print("결과는", ans, "입니다.")
#     except ValueError:
#         print("정수를 입력하세요.")
#     except ZeroDivisionError:
#         print("0은 입력할 수 없습니다. ")
# 정수를 입력하세요.
# ```

# **0으로 나누기 오류(ZeroDivisionError)의 경우**

# ```python
# >>> num = input("0이 아닌 정수를 입력하세요 : ")
# 0이 아닌 정수를 입력하세요 : 0
# >>> try :
#         int_num = int(num)
#         ans = 10 /int_num
#         print("결과는", ans, "입니다.")
#     except ValueError:
#         print("정수를 입력하세요.")
#     except ZeroDivisionError:
#         print("0은 입력할 수 없습니다. ")
# 0은 입력할 수 없습니다. 
# ```

# 주의) 오류의 종류를 틀리게 명시하면 예외처리가 제대로 동작하지 않는다.

# ```python
# >>> try :
#         a = 3 / 0
#     except ValueError :
#         print("This program stops here.")
# ---------------------------------------------------------------------------
# ZeroDivisionError                         Traceback (most recent call last)
# <ipython-input-39-c743ddb96f59> in <module>()
#       1 try :
# ----> 2   a = 3 / 0
#       3 except ValueError :
#       4   print("This program stops here.")
# 
# ZeroDivisionError: division by zero
# ```

# ## 예외 일으키기
# 
# 강제로 오류를 발생시키고 싶다면 `raise` 명령어를 사용하면 된다. 
# 

# ```python
# >>> raise
# ---------------------------------------------------------------------------
# RuntimeError                              Traceback (most recent call last)
# <ipython-input-10-9c9a2cba73bf> in <module>()
# ----> 1 raise
# 
# RuntimeError: No active exception to reraise
# ```

# ```python
# >>> raise ValueError
# ---------------------------------------------------------------------------
# ValueError                                Traceback (most recent call last)
# <ipython-input-6-e4c8e09828d5> in <module>()
# ----> 1 raise ValueError
# 
# ValueError: 
# ```

# ```python
# >>> raise NameError('name_err')
# ---------------------------------------------------------------------------
# NameError                                 Traceback (most recent call last)
# <ipython-input-7-53219af79342> in <module>()
# ----> 1 raise NameError('name_err')
# 
# NameError: name_err
# ```

# ## 코드의 안전성 문제
# 
# 문법 오류 또는 실행 중 오류가 발생하지 않더라도 **코드의 안전성**이 보장되지는 않는다. 즉, 오류가 발생하지 않더라도 코드를 실행했을 때 기대하는 결과가 나오지 않을 수도 있으니 주의해야 한다. 

# 아래의 코드는 입력받은 정수의 제곱을 출력해주는 코드를 제대로 구현하지 못한 경우를 다룬다. 

# ```python
# >>> int_num = int(input("정수를 입력하세요 : "))
# 정수를 입력하세요 : 3
# >>> print("입력한 정수", int_num, "의 제곱은", int_num, "입니다.")
# 입력한 정수 3 의 제곱은 3 입니다.
# ```
