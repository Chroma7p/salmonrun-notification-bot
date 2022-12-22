import cv2
import numpy as np
from datetime import datetime
import json
from PIL import Image,ImageDraw,ImageFont
import requests
from io import BytesIO
import time

font="/System/Library/Fonts/ヒラギノ角ゴシック W4.ttc"
font="/Library/Application Support/.FontworksFonts/FOT-RowdyStd-EB.otf"
blockw=400
blockh=160

def cv2_putText2(img, text, org, fontFace, fontScale, color):
    x, y = org
    imgPIL = Image.fromarray(img)
    draw = ImageDraw.Draw(imgPIL)
    fontPIL = ImageFont.truetype(font = fontFace,size = fontScale)
    w, h = draw.textsize(text, font = fontPIL)
    draw.text(xy = (x,y-h), text = text, fill = color, font = fontPIL)
    return np.array(imgPIL, dtype = np.uint8)

def make_image(obj,path):
    img=np.full(shape=(blockh*len(obj),blockw,3),fill_value=255,dtype=np.uint8)#width,height,color
    for i,res in enumerate(obj):
        start:datetime=datetime.strptime(res["start_time"],"%Y-%m-%dT%H:%M:%S%z")
        end:datetime=datetime.strptime(res["end_time"],"%Y-%m-%dT%H:%M:%S%z")
        stage=res["stage"]["name"]
        weapons=res["weapons"]
        img=cv2_putText2(img,f"{start.strftime('%Y-%m-%d %H:%M')}~{end.strftime('%Y-%m-%d %H:%M')}",(5,i*blockh+30),font,15,(0,0,0))
        img=cv2_putText2(img,f"{stage}",(10,i*blockh+50),font,15,(0,0,0))
        for j,weapon in enumerate(weapons):
            time.sleep(0.5)
            res=requests.get(weapon["image"])
            with BytesIO(res.content) as buf:
                x = Image.open(buf)             # PIL.Imageで読込む
                x.save(f"onetime.png") 
            wimg=cv2.imread("onetime.png")
            wimg=cv2.resize(wimg,(70,70))
            print(wimg.shape)
            img[i*blockh+60:i*blockh+60+70,j*90+20:j*90+20+70,:]=wimg
            img=cv2_putText2(img,f"{weapon['name']}",(j*90+20,i*blockh+150),font,8,(0,0,0))

    cv2.imwrite(path,img)

"""
with open("res_example.json","r")as f:
    obj=json.load(f)
    make_image(obj["results"],"scheduletest.png")
    """