"""
/*
 * @Author: zuofanxiu 
 * @Date: 2018-08-11 11:32:54 
 * @Last Modified by: zuofanxiu
 * @Last Modified time: 2018-08-11 12:26:03
 */
 #将图片转化为字符表示的图片
"""
from PIL import Image
IMG = "C:/Users/Administrator/Pictures/Camera Roll/photo.jpg"
WIDTH = 40
HEIGHT = 30
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

#将256灰度映射到70个字符上
def getChar(r, g, b, alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]

if __name__ == '__main__':

    im = Image.open(IMG)
    im = im.resize((WIDTH,HEIGHT), Image.NEAREST)
    txt = ""

    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += getChar(*im.getpixel((j,i)))
        txt += '\n'

    print(txt)

    #字符画输出到文件
    with open("C:/Users/Administrator/Pictures/Camera Roll/output.txt",'w') as f:
        f.write(txt)