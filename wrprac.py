#f = open("test.txt", "w", encoding="utf-8")

#i=0
#for i in range(5):
#   f.write(f"{i}번째 줄이에요. 안녕,스파르타!\n")
#   i+=1

#f.close()
from wordcloud import WordCloud
from PIL import Image
import numpy as np

text=''
with open("가족.txt", "r", encoding="utf-8") as f:
   lines = f.readlines()
   for line in lines[5:]:
       if '] [' in line:
           text+=line.split('] ')[2].replace('ㅋ','').replace('ㅠ','').replace('ㅜ','').replace('이모티콘\n','').replace('사진','').replace('삭제된 메시지입니다','')
print(text)


wc = WordCloud(font_path='/System/Library/Fonts/Supplemental/AppleGothic.ttf', background_color="white", width=600, height=400)
wc.generate(text)
wc.to_file("가족.png")


import matplotlib.font_manager as fm

# 이용 가능한 폰트 중 '고딕'만 선별
for font in fm.fontManager.ttflist:
    if 'Gothic' in font.name:
        print(font.name, font.fname)

mask = np.array(Image.open('cloud.png'))
wc = WordCloud(font_path='/System/Library/Fonts/Supplemental/AppleGothic.ttf', background_color="white", mask=mask)
wc.generate(text)
wc.to_file("가족.png")