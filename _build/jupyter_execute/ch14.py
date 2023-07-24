#!/usr/bin/env python
# coding: utf-8

# # 파일 다루기

# 데이터 분석을 하기 위해 파일을 다뤄야 하는 경우가 많다.  
# 여기서는 Google Colab에서 파일에 저장된 데이터를 불러오거나 파일에 데이터를 저장하는 방법을 살펴보자.

# ## `open()` 함수  
# 
# `open()` 함수는 파이썬 내장 함수로, 주로 두 개의 인자 `filename`과 `mode`를 받아 파일과 관련된 모든 정보를 저장한 파일 객체를 리턴한다.  
# 
# > `open(filename, mode)`
# 
# 첫 번째 인자는 파일 이름을 담은 문자열이고, 두 번째 인자는 파일이 사용될 방식을 설명하는 문자열이다. 
# 
# `mode`의 기본값은 `r`로, 
# * `r`은 읽기 위해 파일을 여는 것을 의미한다. 
# * `w`은 쓰기 위해 파일을 여는 것을 의미한다. 이때 같은 이름의 파일이 이미 존재하면, 그 파일의 내용은 모두 사라지고, 존재하지 않으면 새로운 파일이 생성된다.
# * `a`은 덧붙여 쓰기 위해 파일을 여는 것을 의미한다. 즉, 파일의 마지막에 새로운 내용을 추가시킬 때 사용한다. 
# 
# 
# 
# 참고) 저장된 파일은 파일 내용과 더불어 파일의 크기, 작성 시간, 작성자, 수정 시간, 사용자 권한 등 다양한 정보도 함께 포함한다. 

# ## 새 파일에 쓰기
# 
# * 새 파일을 생성한 후에 내용을 적어 넣으려면, `open` 함수를 쓰기 모드(w-모드)를 이용하여, 아래 형식으로 호출하면 된다.  
# > `open('파일경로를 포함한 파일이름', 'w')`
# 
# 주의) 쓰기 모드로 파일을 열 때, 기존에 있는 파일이름을 사용하면 해당 파일내용이 삭제됨을 주의해야 한다. 
# 
# * 생성된 파일에 내용을 추가하려면, `write()` 메서드를 활용한다. 
# > `파일객체.write(추가내용)`
# 
# * 생성된 파일에 내용추가하기가 종료되었으면 해당 파일객체를 닫아야 한다. 파일 객체를 닫는 것이 예상치 못한 오류를 방지할 수 있다.
# > `파일객체.close()`

# 예제를 통해 살펴보자.  
# ex) `say.txt`라는 파일을 생성한 후 아래의 내용을 저장해보자. 
# 
# ```
# hello
# ```
# 
# 참고) `txt`라는 확장자를 가진 파일은 순수한 텍스트 파일이라 부른다. 반면에 아래한글 파일, 워드 파일 등은 순수한 텍스트 파일이 아니다. 아래한글 파일은 표, 그림 등을 다룰 뿐만 아니라 수식처리 및 계산 등을 동시에 다룰 수 있다. 반면에 순수한 텍스트 파일은 글자를 보여주는 것 이외에는 어떤 기능도 가지고 있지 않는다. 

# In[1]:


# 파일을 생성하기 위해 open 함수를 w모드로 사용한다. 
f = open('say.txt', 'w')

# 파일에 내용을 추가하기 위해 write 메소드를 사용한다.
f.write('hello')

# 파일 내용 추가가 완료되면 닫아 주어야 한다.
f.close()


# ## 기존 파일에 내용 추가하기
# 
# * 기존 파일에 내용을 추가하려면, `open` 함수를 추가 모드(a-모드)를 이용하여, 아래 형식으로 호출하면 된다.
# > `open('파일경로를 포함한 파일이름', 'a')`

# 예제를 통해 살펴보자.  
# 앞에서 만든 `say.txt`에 아래의 내용을 추가하기 위해 코드를 다음과 같이 작성하면 어떻게 될까? 
# 
# ```
# 1. 안녕하세요.
# 2. 안녕하세요.
# 3. 안녕하세요.
# 4. 안녕하세요.
# 5. 안녕하세요. 
# 
# ```

# In[2]:


f = open('say.txt', 'w')

for i in range(5) :
    f.write(str(i+1)+'. 안녕하세요.\n') 

f.close()


# 파일을 확인하면, 기존 파일 내용은 삭제되고 새로운 내용이 저장된 것을 볼 수 있다.

#  ex) `say.txt`에 아래의 내용을 추가해보자.  
# 
# ```
# 6. 안녕하세요.
# 7. 안녕하세요.
# 8. 안녕하세요.
# 9. 안녕하세요.
# 10. 안녕하세요. 
# 
# ```
# 
# 기존 파일에 내용을 추가하려면 a-모드를 사용한다.

# In[3]:


f = open('say.txt', 'a')

for i in range(6, 11) :
    f.write(str(i)+'. 안녕하세요.\n') 

f.close()


# ## 파일 읽기

# * 파일을 읽으려면, `open` 함수를 읽기 모드(r-모드)를 이용하여, 아래 형식으로 호출하면 된다.
# > `open('파일경로를 포함한 파일이름', 'r')`

# 예제를 통해 살펴보자.  
# 
# ex) `say.txt` 파일 내용을 확인해보자.

# In[4]:


f = open('say.txt', 'r')

# 또는 아래와 같이 코드를 작성할 수 있다.
#f = open('say.txt')


# `print()` 함수로는 파일 내용을 확인할 수 없다.

# In[5]:


print(f)
f.close()


# 파일 내용을 `for` 반복문을 이용하여 확인할 수 있다.

# In[6]:


f = open('say.txt')

for line in f :
    print(line)

f.close()


# 줄 사이에 새로운 줄이 포함된 이유는 각 줄 맨끝에 줄바꿈(\n) 기호가 포함되었기 때문이다. 따라서 줄바꿈을 한 번 더 하는 것을 방지하기 위해서 `strip()` 메서드를 활용하는 것이 좋다.

# In[7]:


f = open('say.txt')

for line in f :
    print(line.strip())

f.close()


# ### `readline()` 메서드
# 
# `readline()` 메서드는 파일에 저장된 내용을 한 줄씩 읽어 들여 문자열로 리턴한다. 
# 
# > `파일객체.readline()`

# In[8]:


f = open('say.txt')

f.readline()


# In[9]:


f.readline()


# In[10]:


f.readline()


# * `readline()` 메서드는 몇 번째 줄까지 읽었는지 기억한다.  
# * 줄의 끝은 줄바꿈(newline)을 의미하는 문자 '\n'의 존재여부로 확인한다.
#   * 줄바꿈 기호는 엔터키를 누를 때 만들어지지만 보통의 문서 편집기는 보여주지 않는다.
#   * 하지만 사람 눈에 보이지 않을 뿐 컴퓨터에게는 엔터키가 눌렸다는 정보를 줄바꿈 기호로 표시해 둔다.
# * 위에서 각각의 `안녕하세요.` 끝에 줄바꿈 문자(\n)가 존재함을 볼 수 있다.  
# 
# 줄바꿈 문자를 제거하면 보다 자연스럽게 출력할 수 있다. 이를 위해 `strip()`이라는 문자열 메서드를 활용하면 된다. 

# In[11]:


line = f.readline()
word = line.strip()
print(word)


# 파일 내용 전체를 한꺼번에 리턴하는 두 가지 메서드가 존재한다. `readlines()` 메서드와 `read()` 메서드를 살펴보자. 

# ### `readlines()` 메서드  
# 
# `readlines()` 메서드는 파일에 저장된 내용의 각 줄을 항목으로 갖는 리스트를 리턴한다. 
# 
# > `파일객체.readlines()`

# In[12]:


f = open('say.txt')
print(type(f.readlines()))
f.close()


# In[13]:


f = open('say.txt')
print(type(f.readlines()[0]))
f.close()


# In[14]:


f = open('say.txt')
print(f.readlines())
f.close()


# ### `read()` 메서드  
# 
# `read()` 메서드는 파일에 저장된 내용 전체를 하나의 문자열로 리턴한다.
# > `파일객체.read()`

# In[15]:


f = open('say.txt')
print(type(f.read()))
f.close()


# In[16]:


f = open('say.txt')
print(f.read())
f.close()


# 특수 문자들의 기능을 제거한 채로 출력하고 싶다면 `repr()` 함수를 이용하면 된다.

# In[17]:


f = open('say.txt')
print(repr(f.read()))
f.close()


# ## `with` 문
# 
# 지금까지 `open` 함수를 사용하여 파일을 열고, `close()`를 사용하여 파일을 닫았는데,   
# `with` 문을 사용하면 `close()`를 사용하지 않아도 열린 파일을 자동으로 닫아준다.  
# 

# 다음 형식은 
# > 
# ```
# with open('say.txt') as f :
#     코드
# ```
# 
# 

# 아래 코드에 대응한다. 
# >
# ```
# f = open('say.txt')
# 코드
# f.close()
# ```

# 예제를 하나 살펴보자. 
# 
# ex) `subject_score.txt` 파일은 수학, 영어, 과학 점수를 담고 있다. 
# 
# ```
# subject score
# math 95
# eng 86
# science 90
# ```
# 
# 위 파일로부터 과목명과 점수를 아래와 같이 확인하는 코드를 작성하여라. 
# 
# ```
# math 의 점수는  95 이다.
# science 의 점수는  90 이다.
# eng 의 점수는  86 이다.
# ```

# 저장된 파일에서 데이터를 불러와서 한 줄씩 확인하는 방법은 다음과 같다.

# In[18]:


f = open('subject_score.txt')  # 파일 열기

for line in f :    # 각 줄 내용 출력하기
    print(line.strip())

f.close()   #파일닫기


# 파일내용을 확인하면, 과목명과 점수가 공백을 사이로 두고 각 줄에 적혀있다. 따라서 아래와 같이 `split()` 메서드를 사용하여 각 줄을 쪼개야 한다.

# In[19]:


f = open('subject_score.txt') 

for line in f :    
    print(line.strip().split())

f.close()   


# 과목명과 점수를 연동하여 점수순으로 정렬해야 한다. 이를 위해 딕셔너리 자료형을 활용한다. 

# In[20]:


f = open('subject_score.txt') 

score_dict = {}

for line in f :    
    (subject, score) = line.strip().split()
    score_dict[score] = subject   #점수와 과목명을 사전에 추가

f.close()   

print(score_dict)


# 첫째 줄 내용은 점수를 비교하는데 필요없다. `try...except`를 사용하여 첫 줄을 제외하자.

# In[21]:


f = open('subject_score.txt') 

score_dict = {}

for line in f :    
    (subject, score) = line.strip().split()
    try :          # 첫 줄 제외 용도
        score_dict[int(score)] = subject    
    except :
        continue

f.close()   

print(score_dict)


# 이제 `sorted()` 함수를 사용하여, 점수를 정렬한 후에 그 순서대로 value를 읽으면 된다. 

# In[22]:


f = open('subject_score.txt') 

score_dict = {}

for line in f :    
    (subject, score) = line.strip().split()
    try :
        score_dict[int(score)] = subject
    except :
        continue

f.close()   

score_keys = sorted(score_dict.keys(), reverse=True)

for key in score_keys :
    print(score_dict[key], "의 점수는 ", key, "이다.")


# :::{admonition} `continue` 문  
# :class: info  
# `continue`문은 반복문(루프)의 다음 반복을 계속하게 만든다.  
# 
# ```python
# >>> i = 0
# >>> while i < 5 :
#         i += 1
#         if i == 3 :   
#             continue  #continue를 실행하면, continue 아래 코드는 실행하지 않고 다음 반복을 시작.
#         print(i)
# 1
# 2
# 4
# 5
# ```
# 
# :::
# 
