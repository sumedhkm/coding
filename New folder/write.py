
#captcha

from captcha.image import ImageCaptcha

k=ImageCaptcha()

Image=k.generate('245f')
k.write('245f','captcha_sample.png')

#screenshot

from captcha.image import ImageCaptcha

k=ImageCaptcha()

Image=k.generate('245f')
k.write('245f','captcha_sample.png')

# vedio to audio

import moviepy.editor as kkr

change = kkr.VideoFileClip ('sumedh.mp4')

change.audio.write_audiofile('audio.mp3')

import datetime
k=datetime.datetime.now()
print(k)

#image format changer

from PIL import Image
k= Image.open('sumedh.jpg')
k.save('photo-save.png')

#funny moddle

import cowsay
cowsay.pig("sumedh")



#font changer

import pyfiglet
text=input('enter a word:')
k= pyfiglet.figlet_format(text)
print(k)

#wallpaper

import ctypes
path='vlcsnap-2023-04-17-11h29m15s652.png'
ctypes.windll.user32.SystemParametersInfoW(20,0,path,3)

#table
-
from prettytable import PrettyTable
new_table= PrettyTable(["s.no","name","city","age"])
new_table.add_row(["1","sumedh","erode","32"])
new_table.add_row(["2","smith","salem","43"])
print(new_table)