import requests #파이썬에서 웹 브라우저에 요청을 보낼수 있도록 해주는 라이브러리
from bs4 import BeautifulSoup #requests.get(url)로 가져온 body의 데이터를 html형태로 트리 형태로 가져옴. 

#?정적 스크래핑은 해당하는 페이지에의 데이터만 가져오지만 빠르고 성능이 좋음.

#input 내장 함수를 통해 키워드를 입력받고, 그 키워드와 관련 블로그 내용을 스크래핑하는 형태로 개선을 해주세요
A = input()
url = f'https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query={A}'

#url에 요청 메서드를 GET으로 보내서 req에 담기
req = requests.get(url)

# 응답 헤더 뜯어서 text로 불러오기
html = req.text # 소스 코드를 변수에 담기

# 분석데이터를 넣고 "html.parser"을 매개변수로 줌.
soup = BeautifulSoup(html, "html.parser") 

# select, find 문법으로 찾아낸 결과는 
# list와 동일한 데이터 타입으로 반환. select 클래스명에 해당되는 모든 데이터를 문자로
result = soup.select(".view_wrap")

# 토막을 내고 그걸 리스트에 담아서 1개씩 for문으로 출력
for i in result:
        ad = i.select_one(".spblog.ico_ad")# 클래스 2개면 .으로 구분, 
        title = i.select_one(".title_link").text #타이틀 텍스트 가져오기
        link = i.select_one(".title_link")["href"] #링크 가져오기
        writer = i.select_one(".name").text 
        dsc = i.select_one(".dsc_link").text
        if not ad:
            print(f'제목 : {title}')
            print(f'작성자 : {writer}')
            print(f'요약 : {dsc}')
            print(f'링크 : {link}')
            print()


# http method : 사용자 요청의 종류. GET POST UPDATE DELETE
# 요청을 보낼 때 헤더를 붙여서 
# 사이트 분석의 영역
