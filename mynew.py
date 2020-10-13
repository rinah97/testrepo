from openpyxl import Workbook
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')

url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%ED%8A%B8%EB%9F%BC%ED%94%84"

driver.get(url)
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

#####################
articles=soup.select('#main_pack > div > ul>li')

wb=Workbook()
ws1=wb.active
ws1.title="news"
ws1.append(["제목","링크","신문사","썸네"])

for article in articles:
    title=article.select_one('dl>dt>a').text
    url=article.select_one('dl>dt>a')['href']
    comp = article.select_one('span._sp_each_source').text.split(' ')[0].split('언론사')[0]
    thumb=article.select_one('div > a > img')['src']

    ws1.append([title, url,comp,thumb])

#####################
driver.quit()
wb.save(filename="mynews.xlsx")