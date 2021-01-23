'''
time
'''
import turtle as t
import datetime
import time
t.tracer(False)

def Gap():
    t.penup()
    t.forward(5)
    t.pendown()
def Drawline(bl):
    if bl:
        t.pendown()
    else:
        t.penup()
    t.forward(length)
    Gap()
def qp(num):
    number = {
        0:'234567',
        1:'27',
        2:'13467',
        3:'12367',
        4:'1257',
        5:'12356',
        6:'123456',
        7:'267',
        8:'1234567',
        9:'123567',
        }
    for digit in num:
        if digit == '=' or digit == '+' or digit == '-' or digit == '&' or digit == '#' or digit == '@':
            t.penup()
            t.seth(0)
            t.forward(35)
            if digit == '=':
                t.write('Y',font = ('微软雅黑Light',20,'bold'))
            elif digit == '+':
                t.write('M',font = ('微软雅黑Light',20,'bold'))
            elif digit == '-':
                t.write('D',font = ('微软雅黑Light',20,'bold'))
            elif digit == '&':
                t.write('H',font = ('微软雅黑Light',20,'bold'))
            elif digit == '#':
                t.write('Min',font = ('微软雅黑Light',20,'bold'))
            elif digit == '@':
                t.write('Sec',font = ('微软雅黑Light',20,'bold'))
            t.forward(50)
            t.pendown()
        else:
            for i in range(7):
                d = number[eval(digit)]
                if str(i+1) in d:
                    Drawline(True)
                    if i+1 in [1,2,3,5,6]:
                        t.right(90)
                        Gap()
                    else:
                        Gap()
                else:
                    Drawline(False)
                    if i+1 in [1,2,3,5,6]:
                        t.right(90)
                        Gap()
                    else:
                        Gap()
            t.penup()
            t.backward(5)
            t.seth(0)
            t.forward(15)
            t.pendown()
t.title('Welcome, the time now is...')
t.setup(775,350,758,-476)
t.tracer(False)
t.speed(100)

while 1:
    t.penup()
    t.left(90)
    t.forward(75)
    t.pendown()
    t.seth(0)
    t.penup()
    t.backward(350)
    t.pendown()
    t.width(5)
    length = 40
    qp(datetime.datetime.now().strftime('%Y=%m+%d-'))
    t.right(90)
    t.penup()
    t.forward(175)
    t.seth(0)
    t.backward(600)
    length = 10
    qp(datetime.datetime.now().strftime('%H&%M#%S@'))
    t.pencolor('black')
    t.penup()
    t.goto(-290,-145)
    t.width(5)
    t.pendown()
    t.begin_fill()
    t.circle(50)
    t.fillcolor('#90EE90')
    t.end_fill()
    t.left(90)
    t.penup()
    t.forward(50)
    t.pendown()
    t.seth(0)
    t.left(90)
    if datetime.datetime.now().strftime('%H').lstrip('0') == '00':
        t.right(0)
    else:
        t.right(eval(datetime.datetime.now().strftime('%H').lstrip('0'))*30)
    t.width(5)
    t.pencolor('blue')
    t.forward(30)
    t.backward(30)
    t.seth(0)
    t.left(90)
    if datetime.datetime.now().strftime('%M') == '00':
        t.right(0)
    else:
        t.right(eval(datetime.datetime.now().strftime('%M').lstrip('0'))*6)
    t.width(3)
    t.pencolor('green')
    t.forward(38)
    t.backward(38)
    t.seth(0)
    t.left(90)
    if datetime.datetime.now().strftime('%S') == '00':
        t.right(0)
    else:
        t.right(eval(datetime.datetime.now().strftime('%S').lstrip('0'))*6)
    t.width(2)
    t.pencolor('red')
    t.forward(48)
    t.backward(48)
    t.update()
    time.sleep(1)
    t.clear()
    t.pencolor('black')
    t.seth(0)
    t.penup()
    t.goto(0,0)
