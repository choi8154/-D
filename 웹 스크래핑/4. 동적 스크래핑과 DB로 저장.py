from selenium import webdriver
from selenium.webdriver.chrome.options import Options #Options -> 클래스
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import pymysql

from bs4 import BeautifulSoup

keyword = input("브랜드 또는 제품명을 입력해주세요 : ")

url = "https://kream.co.kr"

option_ = Options()
option_.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=option_)
driver.get(url) # 크롬 화면이 켜지는 코드이기 때문에 결과를 변수에 담지 않아도 됩니다.
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, ".btn_search.header-search-button.search-button-margin").click()
time.sleep(2)

driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys(keyword) #.send_keys("슈프림")
time.sleep(2)

driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys(Keys.ENTER) #.send_keys("슈프림")
time.sleep(2)

for item in range(20):
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)

html = driver.page_source

soup = BeautifulSoup(html, "html.parser")

datas = soup.select(".item_inner")

product_list=[]
for data in datas:
    product_name = data.select_one(".translated_name").text
    if "후드" in product_name: 
        category = "상의"
        product_name = data.select_one(".translated_name").text
        product_brand = data.select_one(".brand-name").text
        product_price = data.select_one(".bold.text-lookup.display_paragraph.line_break_by_truncating_tail").text
        product = [category, product_brand, product_name, product_price]
        product_list.append(product)

# 우리가 추출한 데이터를 ssql문 중 insert문에 활용하기 좋게 리스트 형태로 담는다.(완료)
# 데이터베이스에 실행해서 추출한 데이터를 집어넣을 수 있는 테이블을 만든다. (완료)
# vscode 파이썬 문법으로 데이터베이스의 접속을 시도합니다. <

conn = pymysql.connect( # 접속을 하기위핸 데이터를 conn으로 만듦
    host="127.0.0.1",
    user="root",
    passwd="dain8154",
    db = "kream",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor
)
def excute_qury(conn, query, args=None): #args -> ("카테고리", "브랜드", "제품명", "가격")
    with conn.cursor() as cur:
        cur.execute(query, args or ()) #문을 이용해서 데이터를 보낼때 None은 에러로 해버림.
        if query.strip().upper().startswith('SELECT'): #"SELECT로 시작하는 문자열을 찾아냄"
            return cur.fetchall()
        else:
            conn.commit()

for product in product_list:
    excute_qury(conn, "INSERT INTO product(category, brand, product_name, price) VALUES (%s, %s, %s, %s)", (product[0], product[1], product[2], product[3]))
    
conn.close()







# https://zep.us/play/pnMwWE : pymysql을 사용하는 방법 공식문서.