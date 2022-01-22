import requests #사용할 모듈 명시!
from bs4 import BeautifulSoup # from 모듈이름 import 쓸 기능 => 즉, BeautifulSoup는 모듈이름이 아니라 bs4라는 모듈에 있는 기능 이름!
from datetime import datetime

#print(requests.get)

# requests module 
# get 함수 : return 응답값을 파이썬에 돌려주는 함수!
# requests.get : request 모듈 안에 있는 get 요청을 보내는 get 함수
# server : 요청에 '응답'하는 역할 // client : 필요한 정보를 '요청'하는 역할

# requests.get(url) => 'url' is not defined 오류 발생

'''
url = "https://www.nate.com/"
requests.get(url) # => 오류 발생 x
print(requests.get(url))    # => <Response [200]> 이라는 결과 (200 : 성공을 의미함)
'''

# url 주소에 해당하는 사이트를 요청해서 그 중 text(즉 html 코드)를 출력
url = "https://www.nate.com/"
response = requests.get(url)
#print(type(response.text))  # 출력값: <class 'str'>

#print(response.text)
#print(response.url)
#print(response.content)
#print(response.encoding)
#print(response.headers)
#print(response.json)
#print(response.links)
#print(response.ok)
#print(response.status_code)


# BeautifulSoup(데이터, 파싱방법)
#print(BeautifulSoup(response.text, 'html.parser'))
#print(type(BeautifulSoup(response.text, 'html.parser'))) # 출력값 : <class 'bs4.BeautifulSoup'>
 
soup = BeautifulSoup(response.text, 'html.parser')
#print(soup.title)
#print(soup.title.string)
#print(soup.span)
#print(soup.findAll('span'))

'''
file = open("nate.html","w",encoding="UTF-8")
file.write(response.text)
file.close()
'''

# html 문서에서 모든 a태그 중 ik 클래스를 가져오는 코드
# print(soup.findAll('a','ik'))

print(datetime.today().strftime("%Y년 %m월 %d일의 실시간 검색어 순위입니다.".encode('unicode-escape').decode()).encode().decode('unicode-escape'))

search_rank_file = open("rankresult.txt","w",encoding="UTF-8")
results = soup.findAll('span', 'txt_rank')
rank = 1

for result in results:
    search_rank_file.write(str(rank)+"위:"+result.get_text()+"\n")
    print(rank,"위:",result.get_text(), "\n")
    rank += 1
