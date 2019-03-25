#coding=utf-8

#@time:2019/3/14 14:27
#@author: Sheng Guangxiao

#用python代码，为自己画了一个喵表

#todo demo4

#todo 生成一个动态的猫咪小秒表

import numpy as np
import winsound
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.image as image
from matplotlib.font_manager import FontProperties
import threading,math

fig=plt.figure(figsize=(6,6))
ax=plt.gca()
ax.grid()

newims=[]

for i in range(6):
    im = image.imread(r'C:\Users\esa72\PycharmProjects\sgx\Date\201903\ProcessGif\image\{}.png'.format(i%6))

    newim=[]

    for m in range(len(im[0])):
        item=[]

        for n in range(len(im)):
            item.append(im[n][m])

        newim.append(item)
    newims.append(np.array(newim))

precolor='#77AAAD'

ln1,=ax.plot([],[],'-',lw=4)
ln2,=ax.plot([],[],'-',color=precolor,lw=1.05)
ln3,=ax.plot([],[],'-',color=precolor,lw=1.05)
ln4,=ax.plot([],[],'-',color=precolor,lw=1.05)
ln5,=ax.plot([],[],'-',color=precolor,lw=1.05)
ln6,=ax.plot([],[],'-',color=precolor,lw=1.05)
ln7,=ax.plot([],[],'-',color=precolor,lw=1.05)
ln8,=ax.plot([],[],'-',color=precolor,lw=1.05)
ln9,=ax.plot([],[],'-',color=precolor,lw=1.05)
ln10,=ax.plot([],[],'-',color=precolor,lw=1.05)

figcat = fig.figimage(np.zeros(newims[0].shape), 250, 290, zorder=1)

anchor,=plt.plot([],[],'-',color=precolor,lw=1.8)
anchor_ratio=0.88
theta=np.linspace(2*np.pi,0,60,endpoint=False)
r_out=2
interval_time=1000

def loop():
    winsound.Beep(500,interval_time)

def init():
    font=FontProperties()
    font.set_family('fantasy')
    font.set_size('x-large')
    font.set_weight('semibold')

    ax.text(1.85, 0, "3",color='#791E94',fontsize=18,ha="center",va="center",fontproperties=font)
    ax.text(-1.85, 0, "9",color='#791E94',fontsize=18,ha="center",va="center",fontproperties=font)
    ax.text(0.05, 1.85, "12",color='#791E94',fontsize=18,ha="center",va="center",fontproperties=font)
    ax.text(0.05, -1.85, "6",color='#791E94',fontsize=18,ha="center",va="center",fontproperties=font)

    ax.set_xlim(-2,2)
    ax.set_ylim(-2,2)
    x_out=[r_out*np.cos(theta[i]) for i in range(len(theta))]
    y_out=[r_out*np.sin(theta[i]) for i in range(len(theta))]
    ln1.set_data(x_out,y_out)
    return ln1,

def update(i):
    if i%10==0:
        t=threading.Thread(target=loop)
        t.start()

    print(i)
    r_in = 0.3

    figcat.set_data(newims[i%6])

    anchor.set_data([0,anchor_ratio*math.cos(theta[i])*(r_out-2*r_in)],[0,anchor_ratio*math.sin(theta[i])*(r_out-2*r_in)])

    x_in = [anchor_ratio*((r_out - r_in) * np.cos(theta[i]) + r_in * np.cos(theta[j])) for j in range(len(theta))]
    y_in = [anchor_ratio*((r_out - r_in) * np.sin(theta[i]) + r_in * np.sin(theta[j])) for j in range(len(theta))]
    ln2.set_data(x_in, y_in)

    ratio=1.12

    r_in=r_in/ratio
    x_in = [anchor_ratio * ((r_out - r_in) * np.cos(theta[i]) + r_in * np.cos(theta[j])) for j in range(len(theta))]
    y_in = [anchor_ratio * ((r_out - r_in) * np.sin(theta[i]) + r_in * np.sin(theta[j])) for j in range(len(theta))]
    ln3.set_data(x_in, y_in)

    r_in = r_in / ratio
    x_in = [anchor_ratio * ((r_out - r_in) * np.cos(theta[i]) + r_in * np.cos(theta[j])) for j in range(len(theta))]
    y_in = [anchor_ratio * ((r_out - r_in) * np.sin(theta[i]) + r_in * np.sin(theta[j])) for j in range(len(theta))]
    ln4.set_data(x_in, y_in)

    r_in = r_in / ratio
    x_in = [anchor_ratio * ((r_out - r_in) * np.cos(theta[i]) + r_in * np.cos(theta[j])) for j in range(len(theta))]
    y_in = [anchor_ratio * ((r_out - r_in) * np.sin(theta[i]) + r_in * np.sin(theta[j])) for j in range(len(theta))]
    ln5.set_data(x_in, y_in)

    r_in = r_in / ratio
    x_in = [anchor_ratio * ((r_out - r_in) * np.cos(theta[i]) + r_in * np.cos(theta[j])) for j in range(len(theta))]
    y_in = [anchor_ratio * ((r_out - r_in) * np.sin(theta[i]) + r_in * np.sin(theta[j])) for j in range(len(theta))]
    ln6.set_data(x_in, y_in)

    r_in = r_in / ratio
    x_in = [anchor_ratio * ((r_out - r_in) * np.cos(theta[i]) + r_in * np.cos(theta[j])) for j in range(len(theta))]
    y_in = [anchor_ratio * ((r_out - r_in) * np.sin(theta[i]) + r_in * np.sin(theta[j])) for j in range(len(theta))]
    ln7.set_data(x_in, y_in)

    r_in = r_in / ratio
    x_in = [anchor_ratio * ((r_out - r_in) * np.cos(theta[i]) + r_in * np.cos(theta[j])) for j in range(len(theta))]
    y_in = [anchor_ratio * ((r_out - r_in) * np.sin(theta[i]) + r_in * np.sin(theta[j])) for j in range(len(theta))]
    ln8.set_data(x_in, y_in)

    r_in = r_in / ratio
    x_in = [anchor_ratio * ((r_out - r_in) * np.cos(theta[i]) + r_in * np.cos(theta[j])) for j in range(len(theta))]
    y_in = [anchor_ratio * ((r_out - r_in) * np.sin(theta[i]) + r_in * np.sin(theta[j])) for j in range(len(theta))]
    ln9.set_data(x_in, y_in)

    r_in = r_in / ratio
    x_in = [anchor_ratio * ((r_out - r_in) * np.cos(theta[i]) + r_in * np.cos(theta[j])) for j in range(len(theta))]
    y_in = [anchor_ratio * ((r_out - r_in) * np.sin(theta[i]) + r_in * np.sin(theta[j])) for j in range(len(theta))]
    ln10.set_data(x_in, y_in)

    return ln2

ani=animation.FuncAnimation(fig,update,range(len(theta)),init_func=init,interval=interval_time)
plt.axis('off')
plt.show()




