from wordcloud import WordCloud
from PIL import Image
import numpy as np

text=''
with open("16141.txt", "r", encoding="utf-8") as f:
   lines = f.readlines()
   for line in lines:
       if ' : ' in line:
           text+=line.split(' : ')[1].replace('201','').replace('ㅋ','').replace('ㅠ','').replace('ㅜ','').replace('이모티콘','').replace('사진','').replace('동영상','').replace('삭제된 메시지입니다','').replace('ㅎ','').replace('그리고','').replace('근데','').replace('ㅇ','').replace('그냥','').replace('너무','')
print(text)

wc = WordCloud(font_path='/System/Library/Fonts/Supplemental/AppleGothic.ttf', background_color="black", width=600, height=400)
wc.generate(text)
wc.to_file("16141.png")

import matplotlib.font_manager as fm

for font in fm.fontManager.ttflist:
    if 'Gothic' in font.name:
        print(font.name, font.fname)



mask = np.array(Image.open('cloud.png'))
wc = WordCloud(font_path='/System/Library/Fonts/Supplemental/AppleGothic.ttf', background_color="white", mask=mask)
wc.generate(text)
wc.to_file("16141.png")