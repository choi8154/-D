# selenium : 구글의 엔지니어가 만들었고 세계의 여러 개발자들이 개발하여 만들어냄
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup


keyword = input("검색어를 입력해주세요.")
url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query=" + keyword

option_ = Options()
option_.add_experimental_option("detach", True) # 브라우저가 자동으로 닫히지 않음
# option_.add_argument("headless")

driver = webdriver.Chrome(options=option_) # webdriver야 크롬 브라우저를 들고 나와라
driver.get(url) # 크롬 브라우저가 열리고 정보를 보여줬지만 우리눈이 따라가지 못함 그리고 밑에 코드가 없어서 자동 종료
time.sleep(1) #페이지에서 로그가 남는데 밴당하지 않도록 하기위해 설정
#body의 뷰포트 총 높이의 아래까지 드레그바를 내려서 데이터를 불러옴

for i in range(5):
    #윈도우 스크롤에 html body 태그에 스크롤 높이를 가져옴
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)") #파이썬 코드로 자바스크립트 기능을 이용하겠다.
    time.sleep(0.5) # 한번에 스크롤이 내려가면 데이터를 가져올 시간 없이 종료되기에 설정

html = driver.page_source #소스코드의 결괄르 생성하여 html변수에 담기

source = BeautifulSoup(html, "html.parser")
datas = source.select(".view_wrap")

for i in datas:
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

driver.quit()