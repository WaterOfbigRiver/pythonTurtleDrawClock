# -*- coding: utf-8 -*-
# @Time    : 2019/12/6 18:24
# @Author  : River.big


import turtle as t
from datetime import *

"""
绘制时钟 :
版本三：优化（解决闪动问题）
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
    关于setup有明确的定义，它包括4个参数width,height,startx,starty,
    即定义了窗体的大小和相对于桌面的起始点的坐标以及窗口的宽度高度，缺省是居中占整个屏幕的一半
    screensize包括3个参数，定义了画布的大小和背景色
    需要注意的是，screensize定义画布大小，缺省是400,300
    """
    t.setup(600, 600, 10, 100)  # 大小和 和相对于桌面的起始点的坐标以及窗口的宽度高度，
    # t.screensize(600,600)
    t.dot(10)  # 在中心画个点

    t.seth(-90)  # 方向朝下
    Skip(200)
    # t.pu()
    # t.sety(-200)  # 定位到（-200,0） 下方200
    # t.pd()

    t.pensize(3)
    t.seth(0)  # 方向朝右
    t.circle(200)

    # t.pu()  # 抬起笔

    # 上移50
    t.seth(90)  # 方向朝上
    Skip(50)
    # t.fd(50)  # 上移50 ，即定为到（-150,0）

    # t.pd()  # 放下笔

    t.dot(5)  # 画一个点

    t.seth(0)  # 方向朝右
    # 间隔性的画第二层的小点
    for _ in range(59):
        t.pu()
        t.circle(150, 6)  # 移动60弧度
        t.pd()
        t.dot(5)  # 画一个点

    t.pu()

    # 画12个线段
    t.home()  # 回到起始圆点和状态
    t.pensize(5)
    t.seth(60)

    for i in range(12):
        t.fd(150)  # 前进150
        t.pd()  # 落笔
        t.fd(10)  # 前进10

        Skip(5)
        # t.up()  # 起笔
        # t.fd(5)  # 前进5
        # t.pd()  # 落笔

        t.write(i + 1, font=('Courier', 15, 'bold'))
        t.up()  # 起笔
        t.setx(0)  # 回来
        t.sety(0)  # 回来
        t.rt(30)  # 右转30度
        # 再前进 ……

#设置指针 秒 分 时 针的长度和粗细
def makePoint(pointName,length,size,color):
    t.home() #先回到原点



    t.pu()  # 抬起笔  #注册图形时不是真的画，而是记录路径，所以笔是抬起的
    # t.pd()  # 放下笔

    t.begin_poly()

    t.pencolor(color) #实际上无用， 事后发现size和color并不能记录在内，所以后期还需要重新设置
    t.pensize(size) #实际上无用， 事后发现size和color并不能记录在内，所以后期还需要重新设置

    t.fd(length)
    t.end_poly()

    # t.pu()  # 抬起笔

    poly = t.get_poly()
    t.register_shape(pointName, poly)    # 注册为一个shape



def drawPoint():  # 画指针
    #全局变量，另外4个pen
    global hourPoint, minPoint, secPoint, fontWriter

    makePoint("HourPoint",80,3,"black")
    makePoint("MinutePoint", 110, 2, "black")
    makePoint("secondPoint", 140, 1, "red")
    t.hideturtle() #隐藏旧的光标

    hourPoint = t.Pen()  # 每个指针是一只新turtle
    hourPoint.shape("HourPoint")
    # hourPoint.shapesize(1, 1, 6)

    minPoint = t.Pen()
    minPoint.shape("MinutePoint")
    # minPoint.shapesize(1, 1, 4)

    secPoint = t.Pen()
    secPoint.shape("secondPoint")
    # secPoint.pencolor('red')

    fontWriter = t.Pen()
    fontWriter.pencolor('gray')
    fontWriter.hideturtle()


# 写时间及绘制指针
def ShowTime():

    tim = datetime.today() # 今天的日期2018-01-11

    curr = datetime.now()  # 日期-时间（精确到微秒，小数点后6位） 如 2018-01-11 20:19:34.794000
    curr_hour = curr.hour
    curr_minute = curr.minute
    curr_second = curr.second

    # t.pencolor("black")

    # t.tracer(False) #不显示绘制的过程，直接显示绘制结果

    # 绘指针（时针和分针）
    # t.home()  # 回到起始状态
    # t.lt(90)  # 起始指向是12，即0点，此时角度是90度

    # t.rt(tim.hour * 30)  # 向右转的角度

    # hourPoint.setheading(curr_hour%12 * 30*-1+180)  #因为此版本没有使用logo模式，所以默认是逆时针旋转，所以需要乘以-1
    #或者用
    hourPoint.setheading(180-(curr_hour % 12 * 30 +30 / 60 * curr_minute))  # 因为此版本没有使用logo模式，所以默认是逆时针旋转，

    # 时针的粗细3 长度80
    # t.pensize(3)
    # t.pd()  # 落笔
    # t.fd(80)

    #-- makePoint("HourPoint",80,3,"black")

    # 分针
    # t.up()  # 起笔

    # t.home()  # 回到起始状态
    # t.lt(90)  # 起始指向是12，即0点，此时角度是90度

    # t.rt(tim.minute * 6)  # 向右转的角度

    # minPoint.setheading(curr_minute * 6*-1+180)#因为此版本没有使用logo模式，所以默认是逆时针旋转，所以需要乘以-1
    # 或者用
    minPoint.setheading(180-curr_minute * 6)  # 因为此版本没有使用logo模式，所以默认是逆时针旋转

    # 分针的粗细2 长度110
    # t.pensize(2)
    # t.pd()  # 落笔
    # t.fd(110)

    #-- makePoint("MinutePoint", 110, 2, "black")

    # 秒针
    # t.up()  # 起笔

    # t.pencolor("red")

    # t.home()  # 回到起始状态
    # t.lt(90)  # 起始指向是12，即0点，此时角度是90度

    # t.rt(tim.second * 6)  # 向右转的角度

    # secPoint.setheading(curr_second * 6*-1+180)#因为此版本没有使用logo模式，所以默认是逆时针旋转，所以需要乘以-1
    # 或者用
    secPoint.setheading(180-curr_second * 6)  # 因为此版本没有使用logo模式，所以默认是逆时针旋转

    # 秒针的粗细1 长度140
    # t.pensize(1)
    # t.pd()  # 落笔
    # t.fd(140)

    #-- makePoint("secondPoint", 110, 1, "red")

    # t.pu()  # 抬起笔


    t.tracer(False) # 不显示绘制的过程，直接显示绘制结果

    fontWriter.reset()  #重置笔  #方向和位置等状态也回到起始状态（所以fontWriter的隐藏状态又消失了）
    #reset后需要重新设置笔的光标的隐藏
    fontWriter.hideturtle()

    #与上面的相同实现的写法
    # fontWriter.clear() #清空笔的历史笔迹，方向和位置等状态不改变，笔的隐藏状态依旧存在，所以不用再写fontWriter.hideturtle()

    fontWriter.pu()  # 抬起笔


    # 写日期
    fontWriter.setx(0)
    fontWriter.sety(-50)
    # 定位到(0,-50)
    fontWriter.pd()  # 放下笔
    """
    turtle.write(s [,font=("font-name",font_size,"font_type")])
    """
    # t.write("2019 12 06",font=('Arial', 15, 'normal')) #默认从左边开始写
    fontWriter.write(Date(tim), align="center", font=("Courier", 15, "bold"))  #字体自动居中
    fontWriter.pu()  # 抬起笔

    # 写时间
    fontWriter.setx(0)
    fontWriter.sety(-70)
    # 定位到(0,-70)
    fontWriter.pd()  # 放下笔
    fontWriter.write(str(tim.hour) + ":" + str(tim.minute) + ":" + str(tim.second), align="center", font=("Courier", 15, "bold"))
    fontWriter.pu()  # 抬起笔

    # 写星期
    fontWriter.setx(0)
    fontWriter.sety(60)
    # 定位到(0,60)
    fontWriter.pd()  # 放下笔
    fontWriter.write(Week(tim), align="center", font=("Courier", 15, "bold"))
    fontWriter.pu()  # 抬起笔


    t.tracer(True)

    # 1000ms后继续调用tick ,即1秒
    t.ontimer(ShowTime, 100)


def main():
    t.tracer(False) # 不显示绘制的过程，直接显示绘制结果
    SetupClock()  #绘制表框
    drawPoint()
    t.tracer(True)  # 显示绘制的过程

    ShowTime()


    # # 1000ms后继续调用 ,即1秒
    # t.ontimer(main, 1000)
    t.done() # 和 t.mainloop()等价


if __name__ == "__main__":
    main()


#初步总结：图形注册只能记录基本的形状，其他设置只能后期再设置，所以makePoint函数没必要待size和color参数
# 下次优化可写成 makePoint(pointName,length):
# 另外用.write时不用计较笔的状态，不需要先设置pendown()

#闪动问题解决了，主要在于创建了多个笔，每个笔对应不同的作用，所以reset时只需要重置对应的笔即可，
# 其他笔（指针）只需要修改其状态值（方向）即可实现指针的运动（没有重绘）。 2版中是一只笔共用，所以会闪动（因为需要重绘）

# 问题2的数字显示位置有偏差暂还未解决