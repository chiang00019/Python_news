import requests
from bs4 import BeautifulSoup
import shutil

# 設定目標網址
url = "https://www.ithome.com.tw/news/152373"

# 發送 HTTP 請求並取得網頁內容
response = requests.get(url)
html_content = response.text
import os

soup = BeautifulSoup(html_content, "lxml")

article = soup.select('div.field-item, h1.page-header, div.content-summary')
with open("output.txt", "w", encoding="utf-8") as f:
    for element in article:
        f.write(element.text + "\n")

# 爬取圖片

def download_img_from_article(img_url, img_name):
    #建立一個放圖片的資料夾
    path = './Images'
    if not os.path.isdir(path):
        os.makedirs(path)
    
    r = requests.get(img_url, stream=True)
    file_name = str(img_name + 1)
    print( 'save img to  ./image/'+ file_name + '.png')
    try:
        with open('./Images/' + file_name + '.png', 'wb') as out_file:
            shutil.copyfileobj(r.raw, out_file)
    except:
        print('can not save img', img_url)

# 找圖片
image_count = 0
imgs = soup.select('p img')

for img in imgs:
    if '.png' in img['src']:
        download_img_from_article(img_url=img['src'], img_name = image_count)
        image_count += 1
                

