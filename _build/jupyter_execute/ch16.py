#!/usr/bin/env python
# coding: utf-8

# # 넘파이(Numpy)
# 

# Numpy는 Numerical Python의 줄임말로, 다음의 특징을 가지고 있다.  
# 
# * 다차원 어레이(array) 지원
# * 빠른 처리 속도
# * 과학용 수치 계산에 활용 용이
# 
# 여기서는 넘파이 모듈의 기본 사용법을 소개한다. 

# ## numpy 모듈 임포트하기  
# 
# 넘파이 모듈을 사용하려면 먼저 numpy 모듈을 추가 설치해야 한다. 하지만 구글 코랩에는 numpy가 이미 설치되어 있고, 넘파이 모듈을 임포트하기만 하면 된다.  
# 
# numpy 모듈의 약칭으로 np를 관례적으로 사용한다.  

# In[1]:


import numpy as np


# ## 넘파이 어레이(Array)
# 
# 넘파이 모듈에서 가장 주요한 요소는 어레이(array)이다. 어레이의 사용법은 기본적으로 리스트와 비슷하다.  
# 

# ### 어레이 생성하기  
# 
# **수동 생성**  
# 
# 수동으로 1차원 어레이 생성하기   
# 
# 예를 들어, 0, 1, 2, 3으로 구성된 어레이를 생성하고자 하면 `array` 함수를 사용하면 된다.  

# In[2]:


a_1dim = np.array([0, 1, 2, 3])


# 어레이의 모양과 활용은 리스트와 비슷하다.

# In[3]:


print(a_1dim)


# 하지만 자료형은 넘파이 모듈에서 정의된 ndarray이다. 

# In[4]:


print(type(a_1dim))


# `array` 함수는 리스트와 더불어 튜플도 입력받는다. 리스트와 튜플 중 어느 것을 써도 리턴값은 언제나 어레이이다. 

# In[5]:


a = np.array((0, 1, 2, 3))
print(a)
print(type(a))


# `a_1dim`과 `a`가 동일한 항목으로 구성된 어레이임을 아래와 같이 확인할 수 있다. 

# In[6]:


b = (a_1dim == a)
b


# 주의) 어레이 사이의 비교는 각 항목별로 실행된다. `a_1dim == a`의 실행 결과는 새로운 어레이이며, 각 항목별로 비교한 결과인 불리언(bool) 값을 갖게 된다.   
# 
# 주의) 리스트나 튜플과는 달리, 어레이의 각 항목들은 모두 동일한 자료형이어야 한다.  
# 
# **어레이 항목의 자료형**  
# 어레이 항목의 자료형은 `dtype` 속성을 이용하여 확인할 수 있다. 
# 

# In[7]:


print(a_1dim.dtype) #변수 a_1dim에 할당된 어레이에는 int형 숫자들이 들어 있음.
print(a.dtype) 
print(b.dtype) #변수 b에 할당된 어레이에는 불리언(bool) 값들이 들어 있음. 


# 어레이를 생성할 때, 아래와 같이 `dtype`을 사용하여 어레이 항목의 자료형을 지정할 수도 있다. 

# In[8]:


c = np.array(('0', '1', '2', '3'), dtype = 'int')
print(c)
print(c.dtype)


# **생성된 어레이의 차원 확인**  
# `a_1dim`에는 1차원 어레이가 할당되었다. 차원 정보는 `ndim`이라는 속성에 담겨져 있다. 

# In[9]:


a_1dim.ndim


# **생성된 어레이의 모양(shape) 확인**  
# 생성된 어레이의 모양(shape)은 `shape`이라는 속성을 이용하여 확인한다. 

# In[10]:


a_1dim.shape


# 변수 `a_1dim`에 할당된 어레이인 `array([0, 1, 2, 3])`는 1차원 어레이이며, 길이가 4이다. 

# **수동으로 2차원 어레이 생성하기**  
# 
# 예를 들어, 아래와 같은 3×2 행렬을 2차원 어레이로 구현할 수 있다.  
# 
# $$\begin{pmatrix} 0 & 1 \\ 2 & 3 \\ 4 & 5 \end{pmatrix}$$
# 
# 

# In[11]:


a_2dim = np.array([[0, 1], [2, 3], [4, 5]])
a_2dim


# 즉, 앞서 언급된 행렬의 첫째 행이 위 어레이의 첫 번째 리스트로, 그리고 둘째 행이 어레이의 두 번째 리스트에 해당한다.  
# 
# `ndim` 을 이용하여 어레이의 차원을 확인해보자. 

# In[12]:


a_2dim.ndim


# 변수 `a_2dim`에 할당된 어레이의 모양(shape)은 3×2 행렬에 해당하는 (3, 2)이다. 

# In[13]:


a_2dim.shape


# 주의) `len` 함수는 마치 리스트의 길이를 리턴해주는 것처럼 어레이 인자를 받으면, 첫 번째 차원의 길이를 리턴한다. 

# In[14]:


print(a_2dim)
print(len(a_2dim))


# 주의) 넘파이 모듈에는 어레이 모양 정보를 리턴하는 `shape()`라는 함수가 따로 존재한다. 이 함수는 어레이의 `shape` 속성 정보를 리턴한다. 

# In[15]:


np.shape(a_2dim)


# ex) `len()` 함수와 `np.shape()` 함수, 그리고 `ndim` 사이에는 어떤 관계가 있을까?

# * `np.shape()` 함수의 리턴값의 첫 번째 인자가 `len()` 함수의 리턴값과 동일하다. 

# In[16]:


np.shape(a_2dim)[0] == len(a_2dim)


# * `ndim` 속성 값은 `np.shape()` 함수의 리턴값인 튜플의 길이와 동일하다. 

# In[17]:


len(np.shape(a_2dim)) == a_2dim.ndim


# **자동 생성**  
# 
# 실제로 우리가 사용하는 데이터는 매우 크기 때문에 수동으로 어레이를 생성하는 방법은 실전에서는 거의 사용하지 못한다. 이제 보다 간단하게 원하는 어레이를 생성하는 방법을 살펴보자.  
# 

# **arange() 함수 활용**  
# 넘파이의 `arange()` 함수는 `range()`함수와 기본적으로 동일하게 작동한다. 다만 리스트가 아닌 어레이를 리턴한다. 

# In[18]:


a = np.arange(10)  # range(10)와 동일
a 


# In[19]:


b = np.arange(1, 9, 2) # range(1, 9, 2)와 동일
b


# **linspace() 함수 활용**  
# `linspace()`함수를 사용하여 특정 구간을 일정한 크기로 쪼개어 어레이를 생성할 수 있다. 예를 들어, 0과 1 구간을 6개의 점으로 균등하게 쪼개어 어레이를 만들려면 아래와 같이 실행하면 된다. 

# In[20]:


d = np.linspace(0, 1, 6)
d


# 반면에 구간의 오른쪽 끝을 제외하고 6개의 점으로 균등하게 쪼개어 어레이를 만들려면 아래와 같이 실행하면 된다. 

# In[21]:


e = np.linspace(0, 1, 6, endpoint = False)
e


# 주의) 위의 결과는 아래 결과에서 마지막 구간을 생략한 결과와 동일하다. 
# 

# In[22]:


f = np.linspace(0, 1, 7)
f


# **1로 채워진 어레이 생성**  
# `ones()` 함수는 원하는 모양의 어레이를 생성한다. 다만, 모든 항목은 1로 채워진다. 예를 들어, 1로 채워진 3×4 모양의 2차원 행렬에 대응하는 어레이는 아래와 같이 생성한다.  
# 
# 주의) 인자는 원하는 모양(shape)의 튜플을 사용한다. 

# In[23]:


g = np.ones((3, 4))
g


# **0으로 채워진 어레이 생성**  
# `zeros()` 함수는 원하는 모양의 어레이를 생성한다. 다만, 모든 항목은 0으로 채워진다. 예를 들어, 0으로 채워진 2×3 모양의 2차원 행렬에 대응하는 어레이는 아래와 같이 생성한다.  
# 
# 주의) 인자는 원하는 모양(shape)의 튜플을 사용한다. 

# In[24]:


h = np.zeros((2, 3))
h


# **단위행렬 생성**  
# 선형대수에서 중요한 역할을 수행하는 단위행렬(unit matrix)은 대각선은 1로 채우고 나머지는 모두 0으로 채워진다. `eye()` 함수를 이용하여 원하는 모양의 단위행렬에 해당하는 어레이를 생성할 수 있다.  
# 
# 주의) 인자는 원하는 모양(shape)의 어레이의 길이(len)를 사용한다. 

# In[25]:


i = np.eye(4)
i


# **`diag()`함수 활용**  
# 
# 숫자들의 리스트가 주어졌을 경우, 리스트(또는 튜플, 1차원 어레이)의 항목들을 대각선 값으로 갖는 어레이를 구현할 수 있다. 

# In[26]:


j1 = np.diag([1, 2, 3, 4])
j1


# In[27]:


j2 = np.diag((1, 2, 3, 4))
j2


# In[28]:


j3 = np.diag(np.arange(1, 5))
j3


# 생성된 어레이는 모두 동일하다. 

# In[29]:


j1 == j2


# In[30]:


j2 == j3


# **난수로 구성된 어레이**  
# 
# 난수(random number)로 구성된 어레이를 생성하기 위해 `numpy.random` 모듈에 있는 `rand()`, `randn()` 함수를 활용할 수 있다.  
# * `numpy.random.rand()` 함수 : 균등분포를 사용하여 지정된 수만큼 [0,1) 구간에서 난수를 구한다.  
# * `numpy.random.randn()` 함수 : 표준정규분포 방식을 사용하여 지정된 수만큼 난수를 구한다.  
# 
# 각 함수의 인자는 원하는 모양(shape)에 해당하는 튜플이다. 
# 
# 주의) `numpy.ones()` 또는 `numpy.zeros()` 함수들과는 달리 추가로 괄호를 사용하지 않는다. 

# * 1차원 난수 어레이 생성

# In[31]:


k = np.random.rand(4)
k


# * 2차원 난수 어레이 생성

# In[32]:


k1 = np.random.rand(2, 3)
k1


# 동일한 일을 `np.random.randn()` 함수를 활용하여 할 수 있다. 

# In[33]:


l = np.random.randn(4)
l


# In[34]:


l1 = np.random.randn(2, 3)
l1


# ### 넘파이 어레이의 장점 : 빠른 처리 속도  
# 
# 어레이는 리스트보다 빠르게 데이터를 처리한다. 아래의 예제는 5천만 개의 홀수들의 제곱으로 이루어진 리스트와 어레이를 조작하는 속도를 비교한 것이다. 어레이를 이용하는 경우가 몇 십배 이상 빠름을 확인할 수 있다.  

# In[35]:


import time

start_time = time.time()
a_list = range(0, 100000000, 2)
a_list_square = [i**2 for i in a_list]
end_time = time.time()

list_time = end_time - start_time
print(list_time)


# In[36]:


import time

start_time = time.time()
an_array = np.arange(0, 100000000, 2)
an_array**2
end_time = time.time()

array_time = end_time - start_time
print(array_time)


# 주의) 어레이 관련 연산은 기본적으로 각 항목별로 실행된다. 따라서 `a**2`은 각 항목을 제곱하라는 의미이다. 

# ### 어레이 연산

# 참고) `reshape()`는 어레이의 모양을 변경할 때 사용한다. 

# In[37]:


arr1 = np.arange(6).reshape((2, 3))
arr1


# In[38]:


arr2 = np.arange(6, 12).reshape((2, 3))
arr2


# In[39]:


arr1 + arr2


# In[40]:


arr1 - arr2


# In[41]:


arr1 * arr2


# In[42]:


arr1 /arr2


# In[43]:


arr1 + 2


# In[44]:


arr1 - 2


# In[45]:


arr1 * 2


# In[46]:


arr1 / 2


# ### 어레이 인덱싱과 슬라이싱  
# 
# 
# **1차원 어레이**

# In[47]:


arr = np.arange(10)
arr


# In[48]:


arr[7]


# In[49]:


arr[1 : 5]


# In[50]:


arr[1 : 5] = 10
arr


# In[51]:


arr_copy = arr.copy()
arr_copy[1 : 5] = 30
print('arr : ', arr)
print('arr_copy : ', arr_copy)


# **2차원 어레이**

# In[52]:


arr2d = np.arange(25).reshape((5, 5))
arr2d


# In[53]:


arr2d[1]


# In[54]:


print(arr2d[1][2])
print(arr2d[1, 2])


# In[55]:


arr2d[1:4]


# In[56]:


arr2d[:2, 3:]


# **불리언 인덱싱과 슬라이싱**

# In[57]:


arr = np.arange(10)
print(arr)
print(arr < 5)
print(arr[arr < 5])
arr[arr < 5] = 100
print(arr)


# 여러 개의 불리언 조건을 조합하여 사용할 때는 `and`와 `or` 대신 `&` 와  `|`을 사용해야 한다. 

# ```python
# >>> (arr < 10) and (arr > 6)
# 
# ---------------------------------------------------------------------------
# ValueError                                Traceback (most recent call last)
# <ipython-input-57-477c5a4f8d5c> in <module>()
# ----> 1 (arr < 10) and (arr > 6)
# 
# ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
# ```

# In[58]:


(arr < 10) & (arr > 6)


# ### 전치(transpose)함수  
# 
# 전치함수는 행과 열을 서로 바꾼다.

# In[59]:


arr = np.arange(12).reshape((4, 3))
arr


# In[60]:


arr.T


# ## 넘파이 활용 : 함수 그래프 그리기  
# 
# 예제) $y = x^2$ 그래프를 그려보자.  
# 
# 

# 그래프를 그리기 위해 `matplotlib.pyplot`이라는 모듈을 이용한다. 이 모듈은 보통 `plt`라고 줄여서 부른다. 

# In[61]:


import matplotlib.pyplot as plt

# 그림을 그리기 위한 도화지 준비
fig = plt.figure()


# 그래프는 x좌표와 y좌표로 이루어진 점들을 연결하여 만들려고 한다. 점을 많이 찍을 수록 보다 정확한 그래프를 그릴 수 있다.     
# 이를 위해 x축의 구간을 정한다. 예를 들어, `[-1, 1]`구간으로 하자. 이제 그 구간을 균등하게 쪼개어 x축 상에 30개의 x좌표를 구해보자. 

# In[62]:


xs = np.linspace(-1, 1, 30)
xs


# 이제 $y = x^2$ 함수를 정의하자. 

# In[63]:


def square(x) :
    return x ** 2


# 이제 x 좌표값들에 대응하는 y좌표값들을 구하자. 

# In[64]:


ys = square(xs)
ys


# 주의) `ys`를 아래와 같이 선언할 수도 있다. 

# In[65]:


ys = xs ** 2
ys


# 이제 각각 `xs`와 `ys`로 이루어진 x좌표값과 y좌표값들을 이용하여 제곱함수의 그래프를 그려보자. 

# In[66]:


plt.plot(xs, ys)
plt.plot(xs, ys, 'o')
plt.show()


# # 판다스(Pandas)

# Pandas는 데이터 분석을 위한 라이브러리로, 구조화된 데이터를 빠르고 쉽게 가공할 수 있는 함수들을 제공한다. 

# ## pandas 모듈 임포트하기  
# 
# 구글 코랩에는 pandas가 이미 설치되어 있다. 사용하기 위해 판다스 모듈을 임포트하자.  
#  
#  pandas 모듈의 약칭으로 pd를 관례적으로 사용한다.  

# In[67]:


import pandas as pd


# ## 판다스 시리즈(Series)   
# 
# Series는 넘파이에서 제공하는 1차원 배열과 비슷하지만, 인덱스(index)라고 하는 배열의 데이터에 연관된 이름을 가지고 있다.  
# 
# 

# ### 시리즈 생성하기  
# 
# 예를 들어, 1, 3, 6, 5으로 구성된 시리즈를 생성하고자 하면 `Series()`를 사용하면 된다. 

# In[68]:


sr = pd.Series([1, 3, 6, 5]) 
sr


# In[69]:


type(sr)


# **values와 index**  
# 
# 시리즈의 배열과 인덱스는 `values`와 `index` 속성을 통해 얻을 수 있다. 

# In[70]:


sr.values


# In[71]:


sr.index


# **인덱스**  
# 
# 인덱스를 지정하지 않으면, 기본 인덱스는 0에서 n-1 (n은 데이터의 길이)까지의 정수가 된다. 인덱스는 아래와 같이 시리즈를 생성할 때 지정할 수도 있다.

# In[72]:


sr1 = pd.Series([1, 3, 6, 5], index = ['b', 'c', 'a', 'd'])
sr1


# 인덱스를 이용해서 값에 접근하거나 추가할 수 있다. 

# In[73]:


sr1['a']


# In[74]:


sr1['k'] = 10
sr1


# In[75]:


sr1['c':'d'] #주의) 끝 값을 포함!


# In[76]:


sr1[['c', 'b']]


# **불리언 인덱싱**  
# 
# 불리언으로 값을 선택할 수도 있다. 

# In[77]:


sr1 > 3


# In[78]:


sr1[sr1 > 3]


# Series를 생성하는 방법을 계속 살펴보자. 
# 
# 

# In[79]:


#튜플로도 Series 생성 가능
sr2 = pd.Series((1, 3, 6, 5))
sr2


# In[80]:


#넘파이 어레이로도 Series 생성 가능
sr3 = pd.Series(np.array([1, 3, 6, 5]))
sr3


# In[81]:


# 딕셔너리로도 Series 생성 가능
# key는 인덱스, value는 값 
sdata = {'b' : 1, 'c' : 3, 'a' : 6, 'd' : 5}
sr4 = pd.Series(sdata)
sr4


# In[82]:


# 딕셔너리로 Series를 생성할 때 
# 인덱스를 지정하면, 원하는 데이터를 추출할 수 있다. 
# 
# 예제에서는 sdata에 e는 key가 아니므로 NaN으로 표시된다.
my_index = ['a', 'b', 'c', 'd', 'e']
sr5 = pd.Series(sdata, index = my_index)
sr5


# 참고) `NaN`은 not a number로, pandas에서는 누락된 값(결측치)을 의미한다. 
# 

# **isnull과 notnull**  
# 
# `isnull`과 `notnull`은 누락된 데이터를 찾을 때 사용한다. 
# * `isnull()` : 누락된 데이터는 `True`, 아니면 `False`를 반환
# * `notnull()` : 누락된 데이터는 `False`, 아니면 `True`를 반환

# In[83]:


pd.isnull(sr5)


# In[84]:


pd.notnull(sr5)


# `isnull()`과 `notnull()` 메소드를 사용해도 같은 결과가 나온다. 

# In[85]:


sr5.isnull()


# In[86]:


sr5.notnull()


# ## 판다스 데이터프레임(DataFrame)

# DataFrame은 스프레드 시트처럼 2차원 데이터 구조로 여러 개의 열(column)을 가지고 있는데, 각 열은 숫자, 문자열, 불리언 등을 담을 수 있다. 

# ### 데이터프레임 생성하기  
# 
# 데이터프레임을 생성하고 싶다면, `DataFrame()`을 사용하면 된다.  
# 아래는 딕셔너리를 이용하여 데이터프레임을 생성하는 예시이다. 
# 

# In[87]:


data = {'col1' : [1, 2, 3, 4], 'col2' : [5, 6, 7, 8], 'col3' : [9, 10, 11, 12]}
df = pd.DataFrame(data)
df


# **dtypes**  
# 각 열의 자료형은 `dtypes` 속성을 이용하여 확인할 수 있다.

# In[88]:


df.dtypes


# **columns**  
# 원하는 순서로 `columns`를 지정하면 원하는 순서를 가진 데이터프레임이 만들어진다. 

# In[89]:


df1 = pd.DataFrame(data, columns = ['col1', 'col2'])
df1


# 이때 `columns`에 `data`의 key가 아닌 값을 넣으면 `NaN`이 저장된다.

# In[90]:


df2 = pd.DataFrame(data, columns = ['col1', 'col2', 'col4'])
df2


# 데이터프레임의 칼럼들은 `columns` 속성을 이용하여 얻을 수 있다. 

# In[91]:


df2.columns


# 중첩된 딕셔너리를 이용하여 데이터프레임을 생성할 수도 있는데,   
# 이때는 바깥에 있는 딕셔너리의 key가 열(column)이 되고, 안에 있는 딕셔너리의 키는 행(row)이 된다. 

# In[92]:


data1 = {'one' : {2019:1, 2020:11, 2021:111}, 'two' : {2020:22, 2021:222}}
df3 = pd.DataFrame(data1)
df3


# 넘파이 어레이를 사용해서 아래와 같이 데이터프레임을 생성할 수도 있다.  
# `columns`를 지정하지 않으면, 열의 이름은 0에서 n-1 (n은 열의 길이)까지의 정수가 된다

# In[93]:


df4 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
df4


# In[94]:


df4 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'])
df4


# 여러 개의 리스트를 합하여 데이터프레임을 생성할 수도 있다.  
# 
# 아래의 코드에서는 두 개의 리스트를 합하여 이름과 점수를 쌍으로 묶기 위해서 `zip` 함수를 이용한다. 
# 
# * `zip` 함수의 리턴값은 `zip` 클래스의 객체이다.
#   * `zip` 객체는 순서쌍들의 리스트와 비슷하다. 
#   * 다만 리스트처럼 색인을 사용하여 직접 항목을 선택할 수는 없다. 
# * `zip` 객체를 리스트 자료형으로 형변환하면 쌍들의 리스트로 활용할 수 있으며, 여기서는 이 기능을 활용한다. 

# In[95]:


name = ['Alice', 'Bob', 'Carol', 'David']
score = [84, 25, 55, 98, 59]

dataSet = list(zip(name, score))
print(dataSet)

df5 = pd.DataFrame(dataSet, columns = ['name', 'score'])
print(df5)


# **index**  
# 
# Series와 마찬가지로 DataFrame도 인덱스를 지정할 수 있다. 

# In[96]:


name = ['Alice', 'Bob', 'Carol', 'David']
score = [84, 25, 55, 98, 59]
idx = ['one', 'two', 'three', 'four']

dataSet = list(zip(name, score))
print(dataSet)

df6 = pd.DataFrame(dataSet, columns = ['name', 'score'], index = idx)
print(df6)


# 데이터프레임의 값에 접근하는 방법을 살펴보자.  

# In[97]:


df


# 데이터프레임의 열은 아래와 같이 딕셔너리 형식의 표기법이나 속성 형식으로 접근할 수 있다.   
# 
# > `데이터프레임명[열의이름]`   
# > `데이터프레임명.열의이름`

# In[98]:


df['col2']


# In[99]:


df.col2


# **loc**  
# 
# loc를 이용해서 행(row) 또는 열(column)에 접근하는 방법을 살펴보자.  
# 
# `df.loc[인덱스명]` 은 인덱스명에 해당하는 행을 추출하라는 의미이다.   

# In[100]:


df.loc[2]


# `df6`의 인덱스는 one, two, three, four이다. 

# In[101]:


df6.index


# `df6.loc['three']` 를 하면 인덱스명이 three인 행을 추출할 수 있다. 
# 

# In[102]:


print(df6)
print('=========================')
print(df6.loc['three'])


# `df.loc[인덱스명, 열의이름]` 을 하면, 해당 인덱스와 열의 값을 추출할 수 있다. 

# In[103]:


df.loc[2, 'col2']


# 여러 개의 행과 열을 선택하고 싶다면, 슬라이싱이나 리스트를 이용하면 된다. 

# In[104]:


df.loc[1:3, 'col2']  #주의) 끝포함


# In[105]:


df.loc[[1, 2, 3], 'col2']


# In[106]:


df.loc[1:3, 'col2' : 'col3']


# In[107]:


df.loc[1:3, ['col2', 'col3']]


# **불리언 인덱싱**  
# 
# Series처럼 불리언으로 값을 선택할 수도 있다.  
# 

# In[108]:


print(df)
print('=============================')
print(df > 10)
print('=============================')
print(df.col3 > 10)
print('=============================')
print(df[df.col3 > 10])


# **len() 함수**  
#   
# 데이터프레임의 길이는 `len()` 함수로 구할 수 있다.

# In[109]:


len(df)


# **head와 tail**  
# 
# 데이터를 확인하기 위해 `head`와 `tail`를 사용할 수 있다. 
# 
# * `head()` : 처음 5개의 행을 보여준다. 인자를 입력하면, 처음부터 그 만큼의 행을 보여준다.   
# * `tail()` : 끝 5개의 행을 보여준다. 인자를 입력하면, 끝에서부터 그 만큼의 행을 보여준다. 

# In[110]:


df.head(2)


# In[111]:


df.tail(3)


# **sum()**  
# 
# `sum()`은 합을 계산해주는 메소드로, 각 열별 합을 보여준다.  
# 이 메소드에 아래와 같이 `axis`를 1로 주면, 행을 합을 보여준다.  
# 

# In[112]:


print(df.sum()) #열의 합
print('==============')
print(df.col1.sum()) # col1 열의 합
print('==============')
print(df.sum(axis = 1)) #행의 합


# **열(column) 추가**  
# 
# 열을 추가하는 연습을 해보자.  
# 
# 모든 행이 같은 값을 갖는 열을 추가하려면 아래와 같이 하면 된다.   
# 
# > `데이터프레임명[열의이름] = 값`  
# 
# 예를 들어, 모든 행이 10인 col4열과 모든 행이 NaN인 col5열을 추가하는 코드는 아래와 같다.  

# In[113]:


df['col4'] = 10
df['col5'] = np.nan
df


# 위에서 값 대신 배열을 대입하면, 행 각각의 값은 배열 각각의 값이 된다. 

# In[114]:


df['col6'] = np.arange(1, 5)
df['col7'] = np.array([5, 4, 3, 2])
df


# 물론 `loc`을 이용하여 데이터프레임의 일부를 선택한 다음 값을 변경할 수도 있다.  
# 예를 들어, 인덱스가 1, 2인 행과 col3인 열의 값을 NaN으로 변경하려면 아래와 같이 코드를 작성하면 된다.   
# 
# 주의) 슬라이싱에서 끝 값이 포함되는 것을 주의하자.

# In[115]:


df.loc[1:2, 'col3'] = np.nan
df


# **isnull과 notnull**  
# 
# Series과 마찬가지로 `isnull()`과 `notnull()`을 사용하여 누락된 데이터를 확인할 수 있다. 

# In[116]:


df.isnull()


# In[117]:


df.notnull()


# 열별 누락된 데이터의 개수가 궁금하다면, `df.notnull().sum()`을 하면 된다. 

# In[118]:


df.notnull().sum()


# 예제를 살펴보자. 
# 
# 예제) 아래의 딕셔너리 `data`를 이용해 데이터프레임 `df`를 생성하여라. 
# 
# ```
# data = {'A' : [1, 2, 3, 4, 5, 6], 'B' : [0, 2, 4, 6, 8, 10], 'C' : [2, 2, 2, 2, 2, 2]}
# ```
# 

# In[119]:


data = {'A' : [1, 2, 3, 4, 5, 6], 'B' : [0, 2, 4, 6, 8, 10], 'C' : [2, 2, 2, 2, 2, 2]}
df1 = pd.DataFrame(data)
df1


# * 데이터프레임을 복사한 다음 사용하고 싶다면, `copy()`를 사용하면 된다. 

# In[120]:


df = df1.copy()
df


# 예제) 위에서 만든 `df`에서 인덱스는 4, 5이면서 열은 A인 값들을 `np.nan`으로 변경하여라. 

# In[121]:


df.loc[4:5, 'A'] = np.nan
df


# 예제) 위에서 만든 `df`에서 인덱스는 2, 3, 4, 5이면서 열은 C인 값들을 `np.nan`으로 변경하여라. 

# In[122]:


df.loc[2:5, 'C'] = np.nan
df


# 예제) 위에서 만든 `df`에서 누락된 값이 2개 이하인 열을 추출하여라. 

# In[123]:


df.isnull()


# In[124]:


df.isnull().sum()


# In[125]:


df.loc[:, df.isnull().sum() < 3]


# # 넘파이Numpy 요약
# 
# * 넘파이 <font color="red">모듈 임포트</font> : `import numpy as np`
# * 넘파이 <font color="red">어레이 생성</font>
#     * 수동 생성 : `np.array()` 이용. 인자로는 리스트, 튜플 사용 가능
#     * 자동 생성  
#       * `np.arange()` : `range()`함수와 사용법 비슷. 예) `np.arange(3)` #[0, 1, 2]    
#       * `np.ones()` : 1로 채워진 어레이 생성. 예) `np.ones((3, 4))` #모든 항목이 1인 3*4모양의 2차원 행렬에 대응하는 어레이   
#       * `np.zeros()` : 0으로 채워진 어레이 생성. 예) `np.zeros((3, 4))`  #모든 항목이 0인 3*4모양의 2차원 행렬에 대응하는 어레이  
#       * `np.eye()` : 대각선은 1이고, 나머지는 0인 단위행렬에 해당하는 어레이 생성. 예) `np.eye(3)`  
#       * `np.diag()` : 대각선 외에는 모두0인 대각행렬에 해당하는 어레이 생성. 인자로는 리스트, 튜플, 넘파이 어레이 사용 가능. 예) `np.diag([1, 2, 3, 4])`  
#       * `np.random.rand()` : 균등분포 방식 사용한 난수로 구성된 어레이 생성. 예) `np.random.rand(3)` 또는 `np.random.rand(2, 3)`  
#       * `np.random.randn()` : 표준정규분포 방식 사용한 난수로 구성된 어레이 생성. 예) `np.random.randn(3)` 또는 `np.random.randn(2, 3)`  
# 
# * 넘파이 어레이 항목의 <font color="red">자료형 확인</font> : `dtype`속성 이용. 예) `arr.dtype`
# * 넘파이 어레이 <font color="red">차원 확인</font> : `shape`속성 확인 또는 `np.shape()`함수 사용. 예) `arr.shape` 또는 `np.shape(arr)`
# 
# * 넘파이 어레이 <font color="red">모양 변경</font> : `reshape()`. 예) `arr.reshape((2, 3))` #어레이를 2*3모양으로 변경 
# * 넘파이 <font color="red">어레이 연산</font> : `+`, `-`, `*`, `/` 가능. 각 항목별로 연산함. 
# * 넘파이 어레이 <font color="red">인덱싱과 슬라이싱</font> : `[]`사용. <font color="blue">슬라이싱에서는 끝점 모두 포함!!!</font> 예) 2차원 어레이 `arr2d`에서 `arr2d[1:4]`는 1번 행부터 4번 행까지 추출, `arr2d[:2, 3:]`는 행은 처음부터 2행이고, 열은 3열부터 끝까지를 반복하는 항목 추출. 
# * 넘파이 어레이 <font color="red">불리언 인덱싱</font> : 예) `arr < 5`는 어레이의 항목이 5보다 작으면 `True` 아니면 `False`반환. `arr[arr < 5]`를 하면, `arr < 5`가 True인 항목 추출   
#   * <font color="red">여러 개의 불리언 조건을 조합</font>할 때는 `and`, `or` 대신 `&`와 `|` 사용. 
# 
# * 넘파이 어레이의 <font color="red">행과 열을 서로 바꿀 때</font>는 `T` 사용. 예) `arr.T`
# 
# * 넘파이 어레이 <font color="red">복사</font> : `copy()` 메서드 사용. 예) `arr.copy()`

# # 판다스Pandas 요약[시리즈]
# 
# * 판다스 <font color="red">모듈 임포트</font> : `import pandas as pd`
# * <font color="red">시리즈 생성</font> : `pd.Series()`이용. 인자로는 리스트, 튜플, 넘파이 어레이, 딕셔너리 사용 가능. 시리즈 생성할 때, 인덱스를 지정하지 않으면 0에서 n-1의 기본 인덱스로 지정. 예) `pd.Series(자료)`
#   * `pd.Series([1, 2, 3])` 
#   * `pd.Series((1, 2, 3), index = ['a', 'b', 'c'])`
#   * `pd.Series({'b' : 1, 'c' : 3, 'a' : 6, 'd' : 5})` : key는 인덱스, value는 값
# 
# 
# * 시리즈 <font color="red">배열과 인덱스 가져오기</font> : `values`와 `index` 속성 이용. 예) `sr.values`, `sr.index` 
# * 시리즈 <font color="red">인덱싱과 슬라이싱</font> : 인덱스 이용. 예) `sr[인덱스]` 
#   * `sr['a']` : `a`가 인덱스인 경우 
#   * `sr[0]` : `0`이 인덱스인 경우 
#   * `sr[['c', 'd']]` : 리스트로 여러 개 인덱스 사용 가능 
#   * `sr['c' : 'd']` : 인덱스 `c`부터 `d`까지. 끝 값 포함!!!.
# * 시리즈 <font color="red">불리언 인덱싱</font> : `sr[sr > 3]` # `sr`의 항목이 3보다 큰 항목을 가져옴.  
# * `NaN` : not a number로 누락된 값 또는 <font color="red">결측치</font>를 의미함.  
# * `pd.isnull()` 또는 `isnull()`메서드: 누락된 데이터는 `True`, 아니면 `False`를 반환. 예) `pd.isnull(sr)` 또는 `sr.isnull()`
# * `pd.notnull()` 또는 `notnull()`메서드: 누락된 데이터는 `False`, 아니면 `True`를 반환. 예) `pd.notnull(sr)` 또는 `sr.notnull()`
# * 시리즈 <font color="red">복사</font> : `copy()` 메서드 사용. 예) `sr.copy()`

# # 판다스Pandas 요약[데이터프레임]
# 
# * 판다스 <font color="red">모듈 임포트</font> : `import pandas as pd`
# * <font color="red">데이터프레임 생성</font> : `pd.DataFrame()` 이용. 예) `pd.DataFrame(자료)`  
#   * `pd.DataFrame({'col1' : [1, 2, 3, 4], 'col2' : [5, 6, 7, 8], 'col3' : [9, 10, 11, 12]})` : key는 열column이름, value는 각 열의 값. 
#   * `pd.DataFrame({'one' : {2019:1, 2020:11, 2021:111}, 'two' : {2020:22, 2021:222}})` : 바깥에 있는 딕셔너리의 key가 데이터 프레임의 열column이 되고, 안에 있는 딕셔너리의 키는 딕셔너리의 행row(인덱스).  
#   * 여러 개의 리스트를 합하여 데이터프레임 생성하는 방법 : `zip()` 함수 이용. 
#     * `pd.DataFrame(zip(리스트1, 리스트2, ..., 리스트n))`
#     
# 
# * 데이터 프레임의 각 <font color="red">열의 자료형 확인</font> : `dtypes` 속성 이용. 예) `df.dtypes`
# * 데이터 프레임의 <font color="red">열 이름 확인</font> : `columns` 속성 이용. 예) `df.columns`  
# * 원하는 <font color="red">열 지정하기</font> : `columns` 속성 지정. 예)  `pd.DataFrame(data, columns = ['col1', 'col2'])`   
# 
# * 데이터프레임의 <font color="red">인덱스 확인</font> : `index` 이용. 예) `df.index`  
# * <font color="red">인덱스 지정하기</font> : `index` 속성 지정. 예)  `pd.DataFrame(data, index = ['a', 'b', 'c'])`   
# 
# * 데이터프레임의 <font color="red">특정 열에 접근</font>하기
#   * `df[열의이름]`  예) `df['col2']`
#   * `df.열의이름`   예) `df.col2`   #열의 이름에 공백이 있을 때는 이 방식 사용 못함. 
# 
# * 데이터프레임의 <font color="red">특정 행(인덱스) 또는 열에 접근</font>하기 : `loc[]`이용
#   * `df.loc[인덱스명]` : 인덱스명에 해당하는 행 추출. 예) `df.loc[2]`, `df.loc['two']`
#   * `df.loc[인덱스명, 열의이름]` : 해당 인덱스와 열인 값을 추출. 예) `df.loc[2, 'col2']` 
#   * 여러 개의 행(인덱스)과 열을 선택하고 싶다면, 슬라이싱이나 리스트 이용. 예) `df.loc[1:3, 'col2']` : 행은 1부터 3이면서 열은 col2인 값을 선택 , `df.loc[[1, 2], ['col1', 'col2']]`
# 
# * <font color="red">불리언 인덱싱</font>
#   * `df[df.col3 > 10]` : `df`의 col3열의 10보다 큰 자료들을 추출
# 
# * 데이터프레임 <font color="red">열 추가</font>: `데이터프레임명[열의이름] = 값`
# 
# * 데이터프레임 <font color="red">길이 확인</font> : `len()` 함수 이용. 예) `len(df)`
# * <font color="red">데이터 확인</font> 
#   * `head()` : 처음 5개의 행을 보여준다. 인자를 입력하면, 처음부터 그 만큼의 행을 보여준다. 예) `df.head()` 또는 `df.head(10)`  
#   * `tail()` : 끝 5개의 행을 보여준다. 인자를 입력하면, 끝에서부터 그 만큼의 행을 보여준다. 예) `df.tail()`  
#   * 인덱싱, 슬라이싱으로도 확인 가능. 예) `df[:10]`
# 
# * 데이터프레임의 <font color="red">열 또는 행의 합 구하기</font> : `sum()` 메서드
#   * `df.sum()` : 열의 합
#   * `df.sum(axis = 1)` : 행의 합
# 
# * `pd.isnull()` 또는 `isnull()`메서드: <font color="red">누락된 데이터</font>는 `True`, 아니면 `False`를 반환. 예) `pd.isnull(df)` 또는 `df.isnull()`
# * `pd.notnull()` 또는 `notnull()`메서드: 누락된 데이터는 `False`, 아니면 `True`를 반환. 예) `pd.notnull(df)` 또는 `df.notnull()`
# 
# * 열별로 <font color="red">누락된 데이터의 개수</font>가 궁금하면 : `df.notnull().sum()`
# 
# * 데이터프레임 <font color="red">복사</font> : `copy()` 메서드 사용. 예) `df.copy()`
# 
