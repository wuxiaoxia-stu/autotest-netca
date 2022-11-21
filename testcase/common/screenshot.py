
from PIL import ImageGrab
from time import strftime
import os

def screenshot(picturename):
    now = strftime("%Y-%m-%d")  #获取当前时间
    path = './output/screenshots/' + now + 'screenshots/'
    if not os.path.exists(path):
        os.mkdir(path)
    im = ImageGrab.grab()
    im.save(path + picturename + ".jpeg")