import PIL.ImageGrab as a
import getpass
import os

b2=getpass.getuser()
b1='c:\\Users\\'
b3='\\Desktop\\'
b=b1+b2+b3
os.chdir(b)
obj=a.grab()
obj.save("Screenshot.png","png")
