#!/usr/bin/env python
# coding: utf-8

# # 웹 사이트에서 데이터 가져오기

# 웹 사이트에서 원하는 데이터를 확인하는 방법을 살펴보자.  
# 
# 
# 파이썬은 웹 사이트에 있는 데이터를 다루기 위해 다양한 함수를 제공하는데, 여기서는 `urllib.request` 모듈의 `urlopen` 함수를 소개한다. 
# 
# 참고) `urllib`는 URL 작업을 위한 여러 모듈을 모은 패키지로, 그중에서 `urllib.request` 모듈은 URL에서 데이터를 가져오는 기능을 제공한다. 
# 
# 참고) URL(Uniform Resource Locator)은 인터넷에서 웹 페이지, 이미지, 비디오 등 리소스의 위치를 가리키는 문자열을 말한다.   
# 예를 들어, 아래와 같은 것들이 URL이다.  
# ex) https://movie.naver.com/movie/sdb/rank/rmovie.naver
# 
# 
# 참고) 패키지와 모듈
# * 특정 분야와 연관된 함수들을 기능별로 분류하여 분류된 함수들끼리 하나의 파이썬 코드 파일에 저장.  
# 이렇게 저장된 코드파일을 **모듈**이라 부름.
# * **패키지**(package) : 특정 분야와 연관된 모듈을 모아놓은 폴더. 라이브러리라고도 부름.

# ## `urllib.request` 모듈의 `urlopen` 함수
# 
# * `urlopen()` 함수는 지정된 웹 페이지의 소스코드를 가져와서 리턴값으로 내주는 함수. 
# 

# `urlopen` 함수를 이용하여 <a ref = "https://movie.naver.com/movie/sdb/rank/rmovie.naver">네이버 영화</a>의 웹 페이지 소스코드를 확인해보자.  
# 
# 웹 페이지 주소는 아래와 같다. 
# > https://movie.naver.com/movie/sdb/rank/rmovie.naver

# ### 웹 페이지 HTML 소스코드
# 
# 웹 페이지의 소스코드는 무엇일까? 예를 들어, <a ref = "https://movie.naver.com/movie/sdb/rank/rmovie.naver">네이버 영화</a>에 방문했을 때 웹 브라우저가 우리에게 보여주는 것은 **HTML**이라는 웹 페이지 개발 전용 프로그래밍 언어로 작성된 해당 웹 페이지의 **소스코드**(source code)를 예쁘게 포장해서 보여주는 것이다.   
# 
# 웹 페이지 소스코드 확인법은 웹 브라우저에 따라 다르다. 크롬 브라우저의 경우, 마우스 오른쪽 버튼을 누른 후 '페이지 소스 보기(V)'를 선택하여 확인하거나 F12를 눌러 확인할 수 있다.

# <div align="center"><img src="https://raw.githubusercontent.com/hj617kim/pybook/master/images/ch15/movie01.png" style="width:700px;"></div>

# 네이버 영화의 웹페이지 소스코드는 아래와 같다.   
# <div align="center"><img src="https://raw.githubusercontent.com/hj617kim/pybook/master/images/ch15/movie02.png" style="width:700px;"></div>  
# 
# 위 그림에서 보이는 소스코드는 영화 제목 정보뿐만 아니라 `<html>, <head>, <title>, <link>, <h2>, <p>` 등 폰트, 글자 크기, 주소 링크, 문단 구성 등과 관련된 웹 페이지 설정 옵션 지정을 위한 HTML 언어 명령문도 포함하고 있다.  
# 이렇듯 웹 브라우저는 소스코드에 포함된 정보와 웹 페이지 설정 옵션을 함께 고려하여 적절한 방식으로 내용을 사용자에게 전달한다. 

# ### 웹 페이지 소스코드 가져오기
# 
# `urlopen()` 함수를 사용하려면, 먼저 `urllib.request` 모듈을 임포트해야 한다.

# In[1]:


import urllib.request


# `urlopen()` 함수를 사용하여 웹 페이지의 HTML 소스코드를 가져오는 코드는 아래와 같다.

# In[2]:


# 웹 페이지 주소 저장
url = "https://movie.naver.com/movie/sdb/rank/rmovie.naver"

# 웹 페이지 소스코드 가져오기
page = urllib.request.urlopen(url)


# 이제 page 변수에는 urlopen 함수가 읽어와서 내주는 값이 저장된다. 이 내주는 값에는 웹 사이트의 HTML 소스코드가 포함되어 있다.   
# 
# 내용을 확인해보자. 

# In[3]:


# utf8로 디코딩해서 html 소스코드를 하나의 문자열로 저장
text = page.read().decode('utf8')
# text


# 참고)  
# * 디코드(decode) : 보통 암호를 푼다. 즉, 원래대로 돌려놓는다는 의미로 사용.
# * utf8 : 문자 인코딩(암호화)하는 방식으로, 프로그래밍 언어 분야에서 거의 표준으로 사용되는 인코딩 방식.  
# * 최근 utf8을 사용하는 것을 권장하나 아직 euc-kr(혹은 cp949)을 사용하는 경우도 있다.

# `print()` 함수를 사용하면, 문자열 자료형을 나타내는 따옴표를 보여주지 않는다.  
# 또, 줄바꿈 기호(\n) 등을 직접 보여주는 대신에 실제로 줄바꿈을 하여 격식을 갖춘 문장으로 보여준다. 

# In[4]:


# print(text)


# ### 문자열로 저장된 데이터에서 필요한 정보 확인하기
# 
# 앞서 `text` 변수에 할당된 HTML 소스코드도 하나의 문자열이다. 

# In[5]:


type(text)


# 따라서 문자열 인덱싱, 슬라이싱 또는 여러 문자열 메소드를 사용하여 HTML 소스코드에서 필요한 정보를 확인할 수 있다.  
# 
# 예를 들어, 위 문자열에서 1위 영화 제목을 추출해보자.  
# 주의 : 영화 순위는 변할 수 있다.  

# **슬라이싱**   
# `<html` 부터 0, 1, 2, 3, 4, ... 등으로 하나씩 인덱스를 세어보면, 영화 제목은 13235번 인덱스 값부터 시작하여 13242번 인덱스 값인 것을 알 수 있다.  
# 이제 슬라이싱을 사용하여, 영화 제목을 확인하면 아래와 같다.  

# In[6]:


text[13235:13242]


# 그런데 위와 같이 수동으로 인덱스를 확인하는 방식에는 다음과 같은 문제가 있다.  
# * 셈이 틀릴 수 있다. 
# * 문자열이 길 경우 셈 자체가 불가능할 수 있다. 
# * 문자열이 조금만 변경되어도 새로 처음부터 세어야 하기 때문에 재활용이 불가능하다.

# **find 메소드 활용**  
# 
# 수동으로 인덱스를 확인하는 방법의 한계를 극복하기 위해서 `find`라는 문자열 메소드를 사용할 수도 있다. 
# 
# * `str.find(sub[, start [, end]])` 메소드는 부분 문자열 `sub`가 `str[start:end]` 내에 등장하는 가장 작은 문자열의 인덱스를 돌려준다.   
# `start`와 `end`는 생략 가능하다. `sub`이 없으면, -1를 돌려준다.
# 
# 
# 참고) `find()`메소드는 주로 `sub` 의 위치를 알아야 할 경우에 사용한다. `sub`가 부분 문자열인지 확인하고 싶다면, `in` 연산자를 사용한다.  
# 

# In[7]:


words = "Python is a general purpose programming language."

print(words.find('is')) # words 내에 is가 등장하는 가장 작은 문자열의 인덱스를 돌려줌.  
print(words.find('fun')) # words 내에 fun은 없으므로 -1를 돌려줌.
print(words.find('o'))  # 여러 번 등장하면 가장 작은 인덱스를 돌려줌.
print(words.find('o', 5))  # 콤마(,) 뒤에 숫자가 하나면 start를 의미. 'o'가 words[5:] 내에 등장하는 가장 작은 문자열의 인덱스를 돌려줌. 
print(words.find('o', 5, 9)) # 'o'가 words[5:9] 내에 등장하는 가장 작은 문자열의 인덱스를 돌려줌. 없다면, -1를 돌려줌.


# ## `BeautifulSoup`   
# 
# HTML에서 원하는 데이터를 추출하기 위해 `bs4`모듈의 `BeautifulSoup` 클래스를 소개한다. 
# 
# 여기서 클래스에 대한 자세한 설명은 하지 않는다. 예제를 통해서 `BeautifulSoup`의 기본적인 사용법을 살펴보자.
# 
# > `BeautifulSoup(html, 'html.parser')`  
# 
# `BeautifulSoup`의 첫 번째 매개변수에는 분석하고 싶은 HTML를, 두 번째 매개변수에는 분석할 분석기(parser)의 종류를 지정한다.  
# 여기서는 HTML를 분석하기 위해 `html.parser`를 사용한다.
# 
# 참고) Beautiful Soup(줄여서 bs)은 HTML를 분석해주는 라이브러리이다. 이 라이브러리를 이용하여 HTML에서 원하는 데이터를 추출할 수 있다. 
# 
# 참고) Google Colab에는 Beautiful Soup이 이미 설치되어 있다.  
# 
# 우선, `BeautifulSoup`을 임포트하자.

# In[8]:


from bs4 import BeautifulSoup


# 분석할 HTML을 지정하자. 
# 여기서는 웹 사이트로부터 HTML를 가져오는 것이 아니라 문자열로 만들어서 사용한다.

# In[9]:


html = """
<html><head><title>컴퓨팅 기초</title></head>
<body>
<p class="title"><b>컴퓨팅 기초</b></p>

<p class="body"> 컴퓨터 과학을 처음 접하는 학생들에게 프로그래밍의 기초와 컴퓨팅 사고력, 그리고 데이터 처리를 소개한다. 
<a href="http://example.com/a" class="item" id="link1">기본 <strong>자료형</strong></a>
<a href="http://example.com/b" class="item" id="link2">조건문과 반복문</a>
<a href="http://example.com/c" class="item" id="link3">오류 및 예외처리</a>
이하 생략
</p>
<p class="body">...</p>
</body></html>
"""


# `BeautifulSoup`을 사용하여 HTML를 분석하자.

# In[10]:


soup = BeautifulSoup(html, 'html.parser')
soup


# 이제 원하는 부분을 추출해보자. 마침표(.)를 이용해서 원하는 값에 접근할 수 있다. 
# 
# 예를 들어, `soup.b` 이라고 하면, `<b>` 태그에 접근한 것이다. 

# In[11]:


b_tag = soup.b
b_tag


# ### `string` 
# 
# 태그 안에 있는 텍스트를 출력하려면, `.string`을 해주면 된다.  
# 예를 들어, 위의 `<b>`안에 있는 텍스트를 출력하려면 아래와 같이 코드를 작성하면 된다. 

# In[12]:


print(b_tag.string)
print(type(b_tag.string)) #타입은 NavigableString이다.


# 자료형을 `NavigableString`에서 `str`로 변경하고 싶다면, `str()` 함수를 사용하면 된다. 

# In[13]:


b_tag_str = str(b_tag.string)
print(b_tag_str)
print(type(b_tag_str))


# 한 문자열을 다른 문자열로 변경하고 싶다면, `replace_with()`를 사용하면 된다.

# In[14]:


print('기존 : ', b_tag.string)
b_tag.string.replace_with('컴퓨팅 핵심')
print('변경 : ', b_tag.string)


# In[15]:


soup


# 조금 더 연습해보자. 예를 들어, `<head>` 에 접근하려면 어떻게 하면 될까?  
# 아래와 같이 코드를 작성하면 된다.  

# In[16]:


soup.head


# 비슷하게 `<title>` 에 접근하려면, 아래와 같이 하면 된다.

# In[17]:


soup.title


# 특정 태그 아래에 있는 태그에 접근할 수도 있다.   
# 예를 들어, `soup.body.b`는 `<body>` 아래 `<b>`에 접근한 것이다.  

# In[18]:


soup.body.b


# 만약 해당 태그가 여러 개 있다면, 가장 앞에 있는 태그를 추출한다.   
# 예를 들어, `<a>` 태그는 여러 개 있는데 `soup.a`라고 접근하면 가장 앞에 있는 값에 접근하는 것을 볼 수 있다. 

# In[19]:


soup.a


# ### `find_all()`

# 여러 개의 `<a>` 태그를 한 번에 가져오고 싶다면, `find_all()` 를 사용하면 된다.

# In[20]:


soup.find_all('a')


# In[21]:


type(soup.find_all('a')) #타입은 ResultSet으로, 리스트와 비슷하게 다루면 된다.


# In[22]:


#예를 들어, 1번 인덱스 값을 가져오고 싶다면 아래와 같이 코드를 작성하면 된다.
soup.find_all('a')[1]


# 
# ### `contents`

# `contents`를 사용하면 자식 태그를 담은 리스트를 반환한다. 
# 
# 참고) 아래와 같이 한 태그(`<parent>`)가 다른 태그(`<child>`)를 감싸고 있다면, 감싼 태그`<parent>`를 부모 태그, 감싸진 태그`<child>`를 자식 태그라고 말한다.  
# ```
# <parent>
#     <child></child>
# </parent>
# ```
# 주의) `<parent>`와 `<child>`는 설명을 위해 적은 것으로, 이런 이름의 태그는 없다. 

# In[23]:


print(soup.a)
print(soup.a.contents)


# In[24]:


soup.a.contents[0]


# In[25]:


soup.a.contents[1].string


# `soup.a`로 접근한 요소 안의 텍스트를 확인해보자.   
# 참고) `.string`을 사용하면 태그 안의 텍스트를 확인할 수 있지만, 태그 안에 다른 태그가 있다면 `None`을 반환한다.

# In[26]:


print(soup.a)
print(soup.a.string)


# ### `strings`

# 태그 안에 다른 태그가 있을 때, 태그 안의 텍스트를 확인하고 싶다면 아래와 같이 `for... in`과 함께 `strings`를 사용하면 된다. 

# In[27]:


for string in soup.a.strings :
    print(repr(string))


# `soup`에 있는 텍스트도 확인해보자. 

# In[28]:


# repr함수를 사용하여, 특수 문자들의 기능을 제거한 채로 출력하자.
for string in soup.strings :
    print(repr(string))


# ### `stripped_strings`

# 위의 출력된 결과를 보면, 줄바꿈(\n)이나 스페이스와 같은 `whitespace`가 포함되어 있다.   
# 이를 제거하여 출력하고 싶다면, `strings` 대신 `stripped_strings`를 사용하면 된다. 

# In[29]:


for string in soup.stripped_strings :
    print(repr(string))


# ### `next_sibling`과 `previous_sibling`
# 
# 어느 태그의 형제 태그에 접근하고 싶다면, `next_sibling`과 `previous_sibling`을 사용하면 된다. 
# 
# 참고) 같은 부모 태그를 갖는 태그들을 형제(sibling)이라고 말한다.
# 

# In[30]:


print(soup.a)
print(soup.a.next_sibling) # </a> 뒤에 줄바꿈 또는 공백있다면, 그것이 추출된다. 
print(soup.a.next_sibling.next_sibling)# next_sibling을 한 번 더 사용하면 두 번째 <a> 태그를 추출


# In[31]:


print(soup.a.previous_sibling) # previous_sibling를 사용하면 이전 형제에 접근한다. 


# 원하는 값에 접근하는 다른 방법을 계속 살펴보자.

# ### id로 요소를 찾는 방법 - `find()`

# `find()` 에 `id = '값'` 형태로 매개변수를 지정해서 원하는 값에 접근할 수도 있다. 
# 
# 참고) 태그에는 class와 id라는 속성을 사용할 수도 있다.   
# 예를 들어, 아래 `<a>`태그의 class는 item이고, id는 link1이다.   
# ```
# <a class="item" href="http://example.com/a" id="link1">기본 <strong>자료형</strong></a>
# ```

# In[32]:


# 아래 a태그의 id는 link1이다.
soup.a


# In[33]:


print(soup.find(id = 'link1'))
print(soup.find(id = 'link2'))
print(soup.find(id = 'link2').string)


# 해당 id를 가진 요소를 찾지 못하면 `None`를 반환한다.

# In[34]:


print(soup.find(id = 'snu'))


# ### CSS 선택자 사용하기 - `select_one()`, `select()`

# CSS 선택자를 사용하여 원하는 값에 접근할 수 있다. 
# 
# 참고) CSS(Cascading Style Sheets)는 웹 페이지를 꾸미려고 작성하는 코드이다.  
# 참고) CSS 선택자(selector)는 CSS를 적용하고자 하는 HTML 요소를 말한다.   
# 참고) 예를 들어,
# * `a` : 모든 `<a>`태그를 가리키는 선택자 
# * `.item` : class가 `item`인 모든 태그를 가리키는 선택자
# * `#link1` : id가 `link1`인 태그를 가리키는 선택자
# 
# 이를 위해 `select_one()`나 `select()` 메소드를 사용할 수 있다.  
# 
# * `soup.select_one(선택자)` : CSS 선택자로 요소 하나를 추출
# * `soup.select(선택자)` : CSS 선택자로 요소 여러 개를 리스트로 추출  
# 
# 
# 개발자 도구(F12)에서 CSS 선택자를 확인할 수도 있다. 태그를 선택한 상태에서 마우스 오른쪽 버튼을 클릭하면 팝업 창이 뜬다. 여기서 Copy > Copy selector 를 클릭하면 선택한 요소의 CSS 선택자가 복사된다.
# 
# 
# 예를 들어, 복사된 CSS 선택자가 
# * `body > h2` : `<body>`태그의 자식 태그 중 `<h2>`태그를 선택
# * `body > p:nth-child(3)` : `<body>`태그의 자식 태그 중 3번째이면서 `<p>`태그인 것을 선택  
# 
# 참고) `nth-child(n)`라는 것은 n번째 자식 요소를 의미한다.  
# 참고) CSS 선택자에서 콜론(:) 뒤에 붙은 것의 대다수는 BeautifulSoup에서 지원하지 않는다.  
# `nth-of-type(n)`은 지원하는데, 예를 들어, `p:nth-of-type(n)`는 n번째 `<p>`라는 의미이다.
# 

# 이제 예제와 함께 `select_one()`를 살펴보자. 

# In[35]:


soup


# In[36]:


print(soup.select_one('p'))
print(soup.select_one('p.title')) #p 다음에 공백이 없다.


# In[37]:


print(soup.select_one('p.body'))


# 만약 해당 태그가 여러 개 있다면, 가장 앞에 있는 태그를 추출한다.

# In[38]:


print(soup.select_one('a.item'))  #a 다음에 공백이 없다.


# 여러 개의 `<a>` 태그를 한 번에 가져오고 싶다면, `select()`를 사용한다. 

# In[39]:


print(soup.select('a.item'))


# In[40]:


item_list = soup.select('a.item')
for li in item_list :
    print(li)


# In[41]:


for i in soup.select('p .item'):  #p 다음에 공백이 있다.
    print(i)


# In[42]:


# 아래의 코드를 실행하면 어떤 요소가 선택될까?
print(soup.select_one('p.body > #link2'))


# # 요약    
# 
# * 웹페이지의 소스코드 가져오는 방법
# ```
# import urllib.request # 모듈 임포트
# url = 웹페이지 주소를 문자열로 저장  
# page = urllib.request.urlopen(url)  # 웹 페이지 소스코드 가져오기  
# text = page.read().decode('utf8') # 오류 발생시 utf8 대신 euc-kr 또는 cp949   사용  
# ```
# 
# * `BeautifulSoup`
# ```
# from bs4 import BeautifulSoup # 모듈 임포트
# soup = BeautifulSoup(html, 'html.parser') # html에는 분석할 소스코드  
# ```
#   * 마침표(`.`)을 이용하여 원하는 값에 접근. ex) `soup.b`하면 b태그에 접근함.
#   * `.string`을 하면, 태그 안의 텍스트 확인 가능. ex) `soup.b.string`
#   * `find_all()` : 인자로 들어온 태그를 모두 가져옴. ex) `soup.find_all('a')`하면 a태그를 모두 가져와서 리스트로 반환.
#   * `.contents` 사용하면 자식 태그를 담은 리스트 반환. ex) `soup.a.contents`
#   * `for..in`과 함께 `strings` 사용하면, 태그 안에 다른 태그가 있어도 텍스트 확인 가능. ex) `for s in soup.a.strings : print(repr(s))`
#   * `repr()` : 특수 문자들의 기능을 제거한 채로 출력  
#   * `for..in`과 함께 `stripped_strings`사용하면, 공백들을 제거하여 출력함. ex) `for s in soup.a.stripped_strings : print(repr(s))`  
#   * `next_sibling`과 `previous_sibling`은 어느 태그의 형제 태그에 접근  
#   * `find()`에 `id = '값'` 형태로 원하는 값에 접근 가능. ex) `soup.find(id = 'link1')`  
#   * `soup.select_one(선택자)` : CSS 선택자로 요소 하나를 추출. ex) `soup.select_one('a.item')`
#   * `soup.select(선택자)` : CSS 선택자로 요소 여러 개를 리스트로 추출. ex) `soup.select('a.item')`
