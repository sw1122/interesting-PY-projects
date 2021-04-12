'''
@author: wsw
PY project1:yinxing
'''

import turtle
import random
from math import *

def Fibonacci_Recursion_tool(n):  #斐波那契数列方法
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci_Recursion_tool(n - 1) + Fibonacci_Recursion_tool(n - 2)


def Fibonacci_Recursion(n):     #生成斐波那契数列，并存入列表
    result_list = []
    for i in range(1, n + 3):
        result_list.append(Fibonacci_Recursion_tool(i))
    return result_list


def leaf(x, y, node):#定义画叶子的方法
    til = turtle.heading()
    i = random.random()
    an = random.randint(10, 180)
    ye = random.randint(6, 9)/10
    turtle.color(ye, ye*0.9, 0)
    turtle.fillcolor(ye+0.1, ye+0.05, 0)
    turtle.pensize(1)
    turtle.pendown()
    turtle.setheading(an + 90)
    turtle.forward(8*i)
    px = turtle.xcor()
    py = turtle.ycor()
    turtle.begin_fill()
    turtle.circle(7.5*i, 120)  # 画一段120度的弧线
    turtle.penup()  # 抬起笔来

    turtle.goto(px, py)  # 回到圆点位置
    turtle.setheading(an + 90)  # 向上画
    turtle.pendown()  # 落笔，开始画
    turtle.circle(-7.5*i, 120)  # 画一段120度的弧线
    turtle.setheading(an + 100)
    turtle.circle(10.5*i, 150)
    turtle.end_fill()  # 画一段150度的弧线
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(til)
    turtle.pensize(node / 2 + 1)


def draw(node, length, level, yu, button):  #定义画树的方法
    turtle.pendown()
    t = cos(radians(turtle.heading()+5)) / 8 + 0.25
    turtle.pencolor(t*1.6, t*1.2, t*1.4) #(r, g, b)颜色对应的RGB值
    turtle.pensize(node/1.2)  #画笔的尺寸
    x = random.randint(0, 10)  #生成随机数决定要画树枝还是画飘落的叶子

    if level == top and x > 6:  #此时画飘落的叶子，x范围太大会导致树太秃
        turtle.forward(length)  # 画树枝
        yu[level] = yu[level] - 1
        c = random.randint(2, 10)
        for i in range(1, c):
            leaf(turtle.xcor(), turtle.ycor(), node)
           # 添加0.3倍的飘落叶子
            if random.random() > 0.3:
                turtle.penup()
               # 飘落
                t1 = turtle.heading()
                an1 = -40 + random.random() * 40
                turtle.setheading(an1)
                dis = int(800 * random.random() * 0.5 + 400 * random.random() * 0.3 + 200 * random.random() * 0.2)
                turtle.forward(dis)
                turtle.setheading(t1)

                turtle.right(90)
               # 画叶子
                leaf(turtle.xcor(), turtle.ycor(), node)
                turtle.left(90)
               # 返回
                t2 = turtle.heading()
                turtle.setheading(an1)
                turtle.backward(dis)
                turtle.setheading(t2)


    elif level==top and x < 7 : #此时画枝叶，x范围太大会导致飘落的叶子太少
        turtle.penup()
        turtle.forward(length)


    elif level>3 and (x>6) :#三级树枝以上，有40%的概率执行以下策略
        turtle.pendown()
        turtle.forward(length)
        c = random.randint(4, 6)
        for i in range(3, c):
            leaf(turtle.xcor(), turtle.ycor(),node)
        leaf(turtle.xcor(), turtle.ycor(),node)
        button=1# jump"""
    else:
        turtle.forward(length)  # 画树枝
        yu[level] = yu[level] -1
    if node > 0 and button == 0:

        # 计算右侧分支偏转角度,在固定角度偏转增加一个随机的偏移量
        right = random.random() * 5 + 17
        # 计算左侧分支偏转角度,在固定角度偏转增加一个随机的偏移量
        left = random.random() * 20 + 19
        # 计算下一级分支的长度
        child_length = length * (random.random() * 0.25 + 0.7)
        # 右转一定角度,画右分支
        r=random.randint(0, 1)
        if r==1:
          turtle.right(right)
          level = level + 1
          #print("level", level)
        else:
          turtle.left(right)
          level = level + 1
          #print("level", level)
        draw(node - 1, child_length,level,yu,button)

        yu[level] = yu[level] +1

        if yu[level] > 1:
            # 左转一定角度，画左分支

            if r==1:
               turtle.left(right + left)
               draw(node - 1, child_length, level, yu,button)
               # 将偏转的角度，转回
               turtle.right(left)

               yu[level] = yu[level] - 1
            else:
                turtle.right(right + left)
                draw(node - 1, child_length, level, yu,button)
                # 将偏转的角度，转回
                turtle.left(left)

                yu[level] = yu[level] - 1
        else:
            if r==1:
              turtle.left(right + left)
              turtle.right(left)

            else:
                turtle.right(right + left)
                turtle.left(left)

    turtle.penup()
    #退回到上一级节点顶部位置
    turtle.backward(length)


if __name__ == '__main__':
    turtle.setup(width=1.0, height=1.0) #设置全屏显示
    turtle.hideturtle()  # 隐藏turtle
    turtle.speed(0)  # 设置画笔移动的速度，0-10 值越小速度越快
    # turtle.tracer(0,0)      #设置动画的开关和延迟，均为0
    turtle.penup()  # 抬起画笔
    turtle.left(90)  # 默认方向为朝x轴的正方向，左转90度则朝上
    turtle.backward(300)  # 设置turtle的位置，朝下移动300
    top = 9  #树高
    yu = Fibonacci_Recursion(top)  #生成斐波契那数列
    yu.remove(yu[0])
    #print(yu) 打印斐波那契数列
    button = 0
    draw(top, 120, 0, yu, button)  # 调用函数开始绘制
    turtle.write("      wsw", font=("微软雅黑", 14, "normal")) #生成签名

    turtle.done()

