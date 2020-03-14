a = 7
print(a)
# 转换
s = '我爱%s'
print(s % 'python')
#下表
s = 'python.org.test'
print(s[2 : 6 : 3])
print(len(s))
print(min(s))
print(max(s))

#方法.字符转换
print(s.upper())
print(s.lower())
print(s.title())

#删除空白
k =  ' python.org.test.ok '
print(k.strip())
print(k.lstrip())
print(k.rstrip())

s = 'affgaggsg'
print(s.find("a"))

s='fkjava.awe'
print(s.split("."))
#join用于连接
print('='.join(s.split(".")))
'''help("str.join")

a = input("请输入：")
print(a)
'''
div = 3%-4
print(div)