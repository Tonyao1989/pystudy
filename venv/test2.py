import turtle

t = turtle.Pen()
turtle.bgcolor("black")
# sides = eval(str(input("输入要绘制的边的数目，请输入2-6Dev数字！ ")))
sides = 6
colors = ["red", "yellow", "green", "blue", "orange", "purple"]
for x in range(360):
    t.pencolor(colors[x % sides])  # 随机颜色
    t.speed("fast")
    t.forward(x * 3 / sides + x)  # 六边形长度依次增加
    t.left(360 / sides + 1)  # 转动角度依次变化
    t.width(x * sides / 180)
    t.left(91)

print("结束")