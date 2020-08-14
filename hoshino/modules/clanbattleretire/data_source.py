import sqlite3
import pandas as pd
from PIL import Image,ImageFont,ImageDraw
from os import path

font_path = path.join(path.dirname(__file__), 'msyh.ttf')
db_path = path.expanduser('~/.hoshino/clanbattle.db')

def add_text(img: Image,text:str,textsize:int,font=font_path,textfill='white',position:tuple=(0,0)):
    #textsize 文字大小
    #font 字体，默认微软雅黑
    #textfill 文字颜色，默认白色
    #position 文字偏移（0,0）位置，图片左上角为起点
    img_font = ImageFont.truetype(font=font,size=textsize)
    draw = ImageDraw.Draw(img)
    draw.text(xy=position,text=text,font=img_font,fill=textfill)
    return img

def get_data(gid: int, year:int, month: int) -> (str,pd.DataFrame):

    conn = sqlite3.connect(db_path)

    month = str(month) if month>=10 else "0"+str(month)

    # get name
    command = f'SELECT * from clan'
    dt = pd.read_sql(command, conn)
    name = dt[dt["gid"]==gid]["name"].iloc[0]

    command = f'SELECT * FROM battle_{gid}_1_{year}{month}'
    dat = pd.read_sql(command, conn)

    conn.close()
    return name,dat

def get_person(gid: int, uid: int, year:int, month: int) -> (str,pd.DataFrame):

    name,dat = get_data(gid, year, month)
    dat = dat[dat["uid"] == uid]

    challenges = dat[["boss","dmg","flag"]]

    return name,challenges





