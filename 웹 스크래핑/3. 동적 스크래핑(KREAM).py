from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By #클릭을 하도록
from selenium.webdriver.common.keys import Keys #클릭을 하도록
import time

keyword = input("브랜드 또는 제품명을 입력하세요")
url = "https://kream.co.kr/"

option_ = Options()
option_.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=option_)
driver.get(url)
time.sleep(1)

# 검색창 클릭
driver.find_element(By.CSS_SELECTOR, ".btn_search.header-search-button.search-button-margin").click()
time.sleep(2)

# 검색창에 텍스트 추가
driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys(keyword + '\n')
time.sleep(2)

for item in range(20):
    #화면에 있는 뷰포트로
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)

html = driver.page_source

source = BeautifulSoup(html, "html.parser")
html = source.select("")


# 검색창 ENTER하기
# driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys(Keys.ENTER)
# time.sleep(2)


driver.quit()
# for i in range(5):
#     driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#     time.sleep(0.5)

# html = driver.page_source

# source = BeautifulSoup(html, "html.parser")
# datas = source.select("item_inner")
