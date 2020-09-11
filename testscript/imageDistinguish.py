# -*- coding: utf-8 -*-
# @Time    : 2019/10/28 17:00
# @Author  : yangxue
# @Email   : yangxue@xiyun.com.cn
# @File    : imageDistinguish.py

from PIL import Image
import pytesseract

class Distinguish:
    def __init__(self):
        pass

    def distinguish(self):
        im=Image.open(r'C:\Users\Think\Desktop\img\20180824114156832.jpg')
        print(pytesseract.image_to_string(im,lang='chi_sim'))



d=Distinguish()
d.distinguish()