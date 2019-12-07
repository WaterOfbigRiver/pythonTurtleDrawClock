# -*- coding: utf-8 -*-
# @Time    : 2019/12/7 13:41
# @Author  : River.big


import turtle as t
from datetime import *

"""
绘制时钟 :
版本四（优化代码）设置为logo模式
"""

def Skip(step):
    t.penup()
    t.forward(step)
    t.pendown()


def Date(tim):
    y = tim.year
    m = tim.month
    d = tim.day
    return "%s %d% d" % (y, m, d)


def Week(tim):
    week = ["星期一", "星期二", "星期三", "星期四", "星期五",
            "星期六", "星期日"]
    return week[tim.weekday()]  # 用星期的值作为下标选择列表值


# 建立表的外框
def SetupClock():

    """
    两者模式对比：

    标准模式  logo 模式
     0 -东     0 - 北
    90 -北    90 - 东
    180-西   180 - 南
    270-南   270 - 西
    """
    t.mode("logo")  # 设置为logo模式，不设置时默认是标准模式


    """
    关于setup有明确的定义，它包括4个参数width,height,startx,starty,
    即定义了窗体的大小和相对于桌面的起始点的坐标以及窗口的宽度高度，缺省是居中占整个屏幕的一半
    screensize包括3个参数，定义了画布的大小和背景色
    需要注意的是，screensize定义画布大小，缺省是400,300
    """

    t.setup(600, 600, 10, 100)  # 大小600*600的画布 和 相对于桌面的起始点的坐标以及窗口的宽度高度，
    # t.screensize(600,600)

    # #测试用
    # t.tracer(False)  # 不显示绘制的过程，直接显示绘制结果

    t.dot(10)  # 在中心画个点

    t.seth(-90)  # 非logo模式时 方向朝下 ，用了logo模式方向朝左
    # t.seth(180)  # 方向朝下（logo模式），非logo模式是朝左
    Skip(200)

    t.pensize(3)
    t.seth(0)  # 方向朝右
    t.circle(-200)  #钟表外框半径是 200

    # 上移50
    t.seth(90)  # 方向朝上
    Skip(50)  #内框圆半径是150=200-50
    t.dot(5)  # 画一个点

    t.seth(0)  # 方向朝右
    # 间隔性的画第二层的小点
    for _ in range(59):
        t.pu()
        t.circle(-150, 6)  # 移动60弧度
        t.pd()
        t.dot(5)  # 画一个点

    t.pu()

    # #测试用
    # t.tracer(True)  #

    # 画12个线段 并写上对应的时间数字
    t.home()  # 回到起始圆点和状态
    t.pensize(5)
    t.seth(30)

    for i in range(12):
        t.fd(150)  # 前进150
        t.pd()  # 落笔
        t.fd(10)  # 前进10

        if(i<2 or i>8):
            Skip(5)
        elif(i==2 or i==8):  # 对应3和9 因为i+1
            Skip(10)
        elif (i == 3 or i == 7):  # 对应4和8 因为i+1
            Skip(20)
        else:
            Skip(25)

        t.write(i + 1, align="center", font=('Courier', 15, 'bold'))  # 写上对应的时间数字

        t.up()  # 起笔
        t.setx(0)  # 回来
        t.sety(0)  # 回来
        t.rt(30)  # 右转30度
        # 再前进 ……



#制作指针 秒 分 时 针的形状
def makePoint(pointName,length):
    #说明，此函数中没必要带size和color参数，因为这里只是注册形状，大小和颜色后期可重新设置，
    # 方向也一样，所以后期只需要修改指针方向就可以实现运动了，且无表框的跳跃感

    t.home() #先回到原点

    t.pu()  # 抬起笔

    t.begin_poly()

    t.back(0.1 * length)
    t.forward(length * 1.1)
    # t.fd(length)
    t.end_poly()

    poly = t.get_poly()
    t.register_shape(pointName, poly)    # 注册为一个shape

    t.home()  # 最后再回到原点



def drawPoint():  # 画指针

    global hourPoint, minPoint, secPoint, fontWriter
    makePoint("HourPoint",80,)
    makePoint("MinutePoint", 110)
    makePoint("secondPoint", 140)
    t.hideturtle() #隐藏旧的光标

    hourPoint = t.Pen()  # 每个指针是一只新turtle  #新定义一个笔，专门管理时针的各个属性（后面主要是改变heading朝向
    hourPoint.shape("HourPoint")
    hourPoint.shapesize(1, 1, 4) #设置时针的宽，长和轮廓  #指针的实际宽度与轮廓关系最明显
    """
    解说shapesize函数：
    turtle.shapesize(stretch_wid=None, stretch_len=None, outline=None)
    参数：
    stretch_wid -- 正数值
    stretch_len -- 正数值
    outline -- 正数值 
    
    stretch_wid 为垂直于其朝向的宽度拉伸因子，stretch_len 为平等于其朝向的长度拉伸因子，决定形状轮廓线的粗细。
    """

    minPoint = t.Pen() #新定义一个笔，专门管理分针的各个属性（后面主要是改变heading朝向）
    minPoint.shape("MinutePoint")
    minPoint.shapesize(1, 1, 3)

    secPoint = t.Pen() #新定义一个笔，专门管理秒针的各个属性（后面主要是改变heading朝向）
    secPoint.shape("secondPoint")
    secPoint.shapesize(1, 1, 2)
    secPoint.pencolor('red')

    fontWriter = t.Pen() #新定义一个笔，专门管理write项的属性（后面主要是用于清空以前输出的时间值，）
    # fontWriter.pencolor('gray')
    fontWriter.hideturtle()


# 写时间及绘制指针
def ShowTime():

    tim = datetime.today() # 今天的日期2018-01-11

    curr = datetime.now()  # 日期-时间（精确到微秒，小数点后6位） 如 2018-01-11 20:19:34.794000

    curr_hour = curr.hour
    curr_minute = curr.minute
    curr_second = curr.second


    #解决文字闪动的关键语句，不要改变的过程，直接给结果就可以了
    t.tracer(False)  # 不显示绘制的过程，直接显示绘制结果

    hourPoint.setheading(curr_hour*30+ 30 / 60 * curr_minute)
    minPoint.setheading(curr_minute*6)
    secPoint.setheading(curr_second*6)

    # fontWriter.reset()  #重置写字的pen ,注意不是绘制表框的那只笔t ； #方向和位置等状态也回到起始状态（所以fontWriter的隐藏状态又消失了）
    fontWriter.clear() #清空指定笔的历史绘图，方向和位置等状态不改变

    fontWriter.up()  # 起笔（移动时不留下痕迹）

    # 写日期
    # 定位到(0,-50)
    fontWriter.setx(0)
    fontWriter.sety(-50)
    # # 或者用fd(-50)实现 ，前进-50
    # fontWriter.home() #回到原点
    # fontWriter.fd(-50) # forward的简写
    # # 也可以用bk(50)后退50
    # fontWriter.home()  # 回到原点
    # fontWriter.bk(50)  # back的简写

    #废弃了，write时没必要
    # fontWriter.pd()  # 放下笔（用write时无需使用用pendown（）改变笔的起落状态）
    """
    .write用法：
    turtle.write(s [,font=("font-name",font_size,"font_type")])
    """
    # fontWriter.write("2019 12 06",font=('Arial', 15, 'normal'))
    fontWriter.write(Date(tim), align="center", font=("Courier", 15, "bold"))

    # 废弃了，没有落下，就不必抬起了
    # fontWriter.pu()  # 抬起笔

    # 写时间
    fontWriter.setx(0)
    fontWriter.sety(-70)
    # 定位到(-40,-70)

    # 废弃了，同上
    # fontWriter.pd()  # 放下笔
    fontWriter.write(str(tim.hour) + ":" + str(tim.minute) + ":" + str(tim.second), align="center", font=("Courier", 15, "bold"))
    # 废弃了，同上
    # fontWriter.pu()  # 抬起笔

    # 写星期
    fontWriter.setx(0)
    fontWriter.sety(60)
    # 定位到(-20,60)

    # 废弃了，同上
    # fontWriter.pd()  # 放下笔
    fontWriter.write(Week(tim), align="center", font=("Courier", 15, "bold"))

    # 废弃了，同上
    # fontWriter.pu()  # 抬起笔


    t.tracer(True)
    # 1000ms后继续调用tick ,即1秒
    t.ontimer(ShowTime, 100)

########################


def drawClock(radius):  # 画表盘方式2
    t.setup(600, 600, 10, 100)  # 大小和 和相对于桌面的起始点的坐标以及窗口的宽度高度，
    t.speed(0)
    t.mode("logo")  # 以Logo坐标、角度方式
    t.hideturtle()  #光标隐藏  ---调试时可以屏蔽，查看绘制过程
    t.pensize(7)
    t.home()  # 回到圆点
    for j in range(60):
        Skip(radius)
        if (j % 5 == 0):
            t.forward(20)
            Skip(-radius - 20)
        else:
            t.dot(5)
            Skip(-radius)
        t.right(6)


##################################

def main():
    t.tracer(False) # 不显示绘制的过程，直接显示绘制结果 ---调试时可以屏蔽，查看绘制过程
    SetupClock()  #绘制表框
    # drawClock(160)  #第二种绘制表框的方法 ，半径160

    drawPoint()
    t.tracer(True)  # 显示绘制的过程

    ShowTime()

    t.done() # 和 t.mainloop()等价


if __name__ == "__main__":
    main()



