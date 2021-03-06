# -*- coding: utf-8 -*-
# @Time    : 2019/12/6 18:24
# @Author  : River.big


import turtle as t
from datetime import *

"""
绘制时钟 :
版本一(静态的)
"""

tim=datetime.today()
def Date(tim):
    y=tim.year
    m=tim.month
    d=tim.day
    return "%s %d% d"%(y,m,d)

def Week(tim):
    week=["星期一","星期二","星期三","星期四","星期五",
          "星期六","星期日"]
    return  week[tim.weekday()]  #用星期的值作为下标选择列表值


"""
关于setup有明确的定义，它包括4个参数width,height,startx,starty,
即定义了窗体的大小和相对于桌面的起始点的坐标以及窗口的宽度高度，缺省是居中占整个屏幕的一半

screensize包括3个参数，定义了画布的大小和背景色
需要注意的是，screensize定义画布大小，缺省是400,300
"""
t.setup(600,600,10,50) #大小和 和相对于桌面的起始点的坐标以及窗口的宽度高度，
# t.screensize(600,600)
t.dot(10) #在中心画个点

t.pu()
t.sety(-200) #定位到（-200,0） 下方200
t.pd()


t.pensize(3)
t.circle(200)

t.pu() #抬起笔

#上移50
t.seth(90) #方向朝上
t.fd(50) #上移50 ，即定为到（-150,0）

t.pd() #放下笔
t.dot(5) #画一个点

t.seth(0) #方向朝右
#间隔性的画第二层的小点
for _ in range(59):
    t.pu()
    t.circle(150,6) #移动60弧度
    t.pd()
    t.dot(5) #画一个点

t.pu()

#写日期
t.setx(-40)
t.sety(-50)
#定位到(-40,-50)
t.pd() #放下笔
"""
turtle.write(s [,font=("font-name",font_size,"font_type")])
"""
# t.write("2019 12 06",font=('Arial', 15, 'normal'))
t.write(Date(tim),font=('Arial', 15, 'normal'))
t.pu() #抬起笔

# 写时间
t.setx(-30)
t.sety(-70)
#定位到(-40,-70)
t.pd() #放下笔
t.write(str(tim.hour)+":"+str(tim.minute)+":"+str(tim.second),font=('Arial', 13, 'normal'))
t.pu() #抬起笔


#写星期
t.setx(-20)
t.sety(60)
#定位到(40,50)
t.pd() #放下笔
t.write(Week(tim),font=('Arial', 15, 'normal'))
t.pu() #抬起笔



#画12个线段
t.home() #回到起始圆点和状态
t.pensize(5)
t.seth(60)

for i in range(12):
    t.fd(150)  # 前进150
    t.pd()  # 落笔
    t.fd(10) #前进10
    t.up()  # 起笔
    t.fd(5)  # 前进5
    t.pd()  # 落笔
    t.write(i+1, font=('Arial', 15, 'normal'))
    t.up() #起笔
    t.setx(0)  #回来
    t.sety(0)  # 回来
    t.rt(30)  # 右转30度
    # 再前进 ……

#绘指针（时针和分针）
t.home() #回到起始状态
t.lt(90) #起始指向是12，即0点，此时角度是90度

t.rt(tim.hour*30 +30 / 60 * tim.minute) #向右转的角度
#时针的粗细3 长度80
t.pensize(3)
t.pd()  # 落笔
t.fd(80)


#分针
t.up() #起笔


t.home() #回到起始状态
t.lt(90) #起始指向是12，即0点，此时角度是90度

t.rt(tim.minute*6) #向右转的角度
#分针的粗细2 长度110
t.pensize(2)
t.pd()  # 落笔
t.fd(110)


#秒针
t.up() #起笔


t.home() #回到起始状态
t.lt(90) #起始指向是12，即0点，此时角度是90度

t.rt(tim.second*6) #向右转的角度
#分针的粗细1 长度140
t.pensize(1)
t.pd()  # 落笔
t.fd(140)



# t.hideturtle() #隐藏光标
t.done()  # 和 t.mainloop()等价


# 问题1：表是静止的，不能动
# 问题2：数字显示位置有偏差