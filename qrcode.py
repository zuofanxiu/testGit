"""
 * @Author: zuofanxiu 
 * @Date: 2018-08-10 20:02:18 
 * @Last Modified by:   zuofanxiu 
 * @Last Modified time: 2018-08-10 20:02:18 

 """
from MyQR import myqr
import os

#生成普通二维码
#import qrcode
#qrcode.make("哒哒哒哒哒哒").get_image().show()

#二维码和图片的重叠
version, level, qr_name = myqr.run(
    #扫码后显示的字段
    words="图图进化中......",
    version=1,
    #控制纠错水平
    level="H",
    #和二维码重叠的图片文件
    picture="C://Users//Administrator//Pictures//Camera Roll//tutu.png",
    #设置（黑白）图片彩色
    colorized=True,
    contrast=1.0,
    brightness=1.0,
    #生成的二维码文件名，默认位置为当前工作目录
    save_name="QR_code.png",
    save_dir=os.getcwd()
)
