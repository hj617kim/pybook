#!/usr/bin/env python
# coding: utf-8

# # 딕셔너리

# 파이썬에 내장되어 있는 컬렉션 자료형 중 딕셔너리에 대해서 알아보자.   
# 
# **딕셔너리**(dictionary)는 키(keys)와 값(values)로 이루어진 쌍(pairs)들의 집합으로, 사전에서 단어의 뜻을 확인하는 방식과 유사하게 활용할 수 있는 자료구조를 가지고 있다. 예를 들어, 영어 사전에서 'world'란 단어의 뜻을 물으면 '세계'라는 뜻을 알려주는데, 이때 'world'는 키(key)에 해당하고, '세계'는 값(value)에 해당한다.  
# 
# 딕셔너리의 형식은 아래와 같다. 
# > { key1 : value1, key2 : value2, key3 : value3, ... }  
# 
# `key : value` 형태로 이루어진 여러 개의 쌍들이 중괄호(`{}`)로 묶여있고, 각 쌍들은 콤마(`,`)로 구분한다.   
# 
# 예를 들어, key가 `'hello'`, `'world'`이고, 각각의 key에 해당하는 value가 `'안녕'`, `'세계'`인 딕셔너리 `dic`를 만드는 코드는 아래와 같다. 
# 
# 

# In[1]:


dic = {'hello' : '안녕', 'world' : '세계'}
dic


# 참고)
# * key로는 불변자료형 사용. ex) 정수, 문자열 등등
# * value로는 불변자료형과 가변자료형 모두 사용 가능. ex) 정수, 문자열, 리스트 등등

# :::{admonition} 주의   
# :class: caution  
# 리스트는 key로 사용할 수 없다. 리스트는 가변자료형이다.
# 
# ```python
# >>> {[1, 2] : '안녕'}
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-74-f085c9caea6b> in <module>()
# ----> 1 {[1, 2] : '안녕'}
# 
# TypeError: unhashable type: 'list'
# ```
# ::: 

# 키와 값으로 이루어진 쌍을 딕셔너리의 항목(item)이라 부른다.  
# 딕셔너리에서 항목의 순서는 중요하지 않다. 그보다 어떤 key가 사용되었는지가 중요하다. 

# ## 인덱싱 
# 
# 딕셔너리에서 인덱싱은 키를 이용한다.  
# 예를 들어, `'hello'`에 대응하는 value을 확인하고자 하면 다음과 같이 대괄호를 사용하는 인덱싱을 이용한다. 
# 

# In[2]:


print(dic['hello'])


# `world`에 대응하는 value는 아래와 같이 확인할 수 있다.

# In[3]:


print(dic['world'])


# 만약, 존재하지 않는 key로 값을 추출하려고 하면, 에러가 발생한다. 
# 
# ```python
# >>> dic['one']
# ---------------------------------------------------------------------------
# KeyError                                  Traceback (most recent call last)
# <ipython-input-77-0af10b7cadba> in <module>()
# ----> 1 dic['one']
# 
# KeyError: 'one'
# ```

# **빈 딕셔너리**  
# 빈 딕셔너리는 아무것도 포함하지 않는 딕셔너리를 의미한다. 빈 딕셔너리를 생성하려면 `dict` 함수나 중괄호(`{}`)를 사용하면 된다. 

# In[4]:


dic1 = dict()
dic1


# In[5]:


dic2 = {}
dic2


# ### 항목(item) 추가  
# 
# 딕셔너리에 item을 추가하려면 대괄호를 사용한다.   
# > 딕셔너리변수명[key] = value
# 
# 예를 들어, 딕셔너리 `dic1`에 key와 value가 각각 `1`과 `'a'`인 항목을 추가하는 코드는 아래와 같다.

# In[6]:


dic1[1] = 'a'
dic1


# 아래의 항목을 더 추가해보자.  
# 
# |key|value|
# |:---:|:-----:|
# | 2 | 'b' |
# | 3 | [1, 2, 3] |
# | 'one' | '일' |

# In[7]:


dic1[2] = 'b'
dic1[3] = [1, 2, 3]
dic1['one'] = '일'

dic1


# 이미 사용하고 있는 key를 가진 항목을 추가하면, 그 key로 저장된 이전 value는 사라진다. 

# In[8]:


print('이전 dic1', dic1)
dic1[2] = 'abc'
print('이후 dic1', dic1)


# ### 항목(item) 삭제  
# 
# 항목은 `del` 함수를 이용해서 삭제할 수 있다.

# In[9]:


print(dic1)


# In[10]:


del dic1['one']


# In[11]:


print(dic1)


# ## 딕셔너리의 길이(len)
# 
# 딕셔너리의 길이는 `len()` 함수를 이용해서 확인할 수 있다. 

# In[12]:


len({1:2})


# In[13]:


dic3 = {'a' : 1, 'b' : 2, 'c' : 3}
print(dic3)
print(len(dic3))


# ## `in` 연산자
# 
# 특정 key가 사전에 사용되었는지 여부를 확인하기 위해 `in` 연산자를 사용할 수 있다.  
# 
# 주의) key로 사용되었는가 여부만 판단한다.

# In[14]:


'b' in dic3


# In[15]:


'k' in dic3


# ## 딕셔너리 관련 메소드

# * `keys` 메소드는 사전에 사용된 key들을 모두 모아서 리스트와 비슷한 자료형을 만들어서 리턴한다.  
# 주의) 리스트와 다르지만 매우 비슷하다. 단, `append()`, `remove()` 등과 같은 리스트 메소드를 사용할 수 없다. 

# In[16]:


dic3_keys = dic3.keys()
print(dic3_keys)


# 아래 두 코드는 동일한 일을 수행한다. 

# In[17]:


'a' in dic3 


# In[18]:


'a' in dic3.keys()


# * `values` 메소드는 사전에 사용된 value들을 모두 모아서 리스트와 비슷한 자료형을 만들어서 리턴한다.  
# 주의) 리스트와는 다르지만 매우 비슷하다.  단, `append()`, `remove()` 등과 같은 리스트 메소드를 사용할 수 없다.  

# In[19]:


dic3_values = dic3.values()
print(dic3_values)


# value로 사용되었는가 여부를 확인하려면, `values` 메소드를 활용하면 된다. 

# In[20]:


3 in dic3.values()


# In[21]:


'삼' in dic3.values()


# * `items()` 메소드는 사전에 사용된 key와 value의 쌍을 튜플로 묶어 리스트와 비슷한 자료형으로 만들어서 리턴한다. 
# 
# 참고) 튜플은 뒤에서 다룬다. 

# In[22]:


dic3_items = dic3.items()
dic3_items


# * `get()` 메소드는 key에 대응되는 value를 리턴한다. 

# In[23]:


dic3


# In[24]:


dic3.get('c')


# 인덱싱과 달리 `get()`메소드는 존재하지 않는 key를 사용했을 때 `None`을 리턴한다.
# 
# ```python
# >>> print(dic3['h'])
# ---------------------------------------------------------------------------
# KeyError                                  Traceback (most recent call last)
# <ipython-input-99-6145c62fb0a4> in <module>()
# ----> 1 print(dic3['h'])
# 
# KeyError: 'h'
# ```

# In[25]:


print(dic3.get('h'))


# * `update()` 메소드는 하나의 딕셔너리를 다른 자료형과 합칠 수 있다. 

# In[26]:


print("dic1", dic1)
print("dic3", dic3)


# In[27]:


dic3.update(dic1)
dic3


# * `pop()` 메소드는 key에 해당하는 항목을 삭제한다.

# In[28]:


dic3


# In[29]:


dic3.pop('a')
dic3


# key가 존재하지 않으면 에러가 발생한다.   
# 
# ```python
# >>> dic3.pop('j')
# ---------------------------------------------------------------------------
# KeyError                                  Traceback (most recent call last)
# <ipython-input-105-85ca1bd838c3> in <module>()
# ----> 1 dic3.pop('j')
# 
# KeyError: 'j'
# ```

# * `clear()` 메소드는 딕셔너리 안의 모든 항목들을 삭제하여 빈 딕셔너리를 만든다.

# In[30]:


dic3


# In[31]:


dic3.clear()


# In[32]:


dic3


# ## 딕셔너리 자료형 반복문
# 
# 딕셔너리를 반복문에 활용할 수 있다.  
# 
# 예제를 통해 살펴보자. 아래는 서울, 수원, 제주의 현재 온도 정보를 담은 딕셔너리다. 

# In[33]:


city_temp = {'Seoul' : 17, 'Suwon' : 19, 'Jeju' : 24}
city_temp


# 다음과 같이 도시와 온도를 반복문을 사용하여 보여줄 수 있다.

# In[34]:


for key in city_temp.keys() :
    print(key, "의 온도는 ", city_temp[key], "도 이다.")


# 이때 `keys` 메소드를 사용하지 않아도 된다. 

# In[35]:


for key in city_temp :
    print(key, "의 온도는 ", city_temp[key], "도 이다.")


# ````{prf:example}
# :label: dict_ex01
# 아래 `game_score`에는 어느 경기에 참여한 선수들의 점수가 담겨 있다.  
# 
# ```
# game_score = "playerA 90, playerB 75, playerC 97, playerD 69, playerE 85, playerF 88, playerG 87"
# ```
# 
# 점수 순으로 정렬하여 아래의 형식으로 말하여라. 
# 
# >`O등은 playerO이고, 점수는 OO점입니다.`
# 
# ````
# 

# 참고) `sorted()`함수는 원래의 리스트를 건드리지 않으면서 정렬된 리스트를 생성해준다. 이때 만약 내림차순으로 정렬하려면 `reverse = True`라는 키워드 인자를 추가한다.

# In[36]:


game_score = "playerA 90, playerB 75, playerC 97, playerD 69, playerE 85, playerF 88, playerG 87"
game_score_dic = {}

for i in game_score.split(", ") :
    player, score = i.split()
    game_score_dic[int(score)] = player

sorted_keys = sorted(game_score_dic.keys(), reverse = True)

count = 1
for key in sorted_keys :
    print(count,"등은",game_score_dic[key], "이고, 점수는 ", key, "입니다.")
    count += 1


# In[ ]:




