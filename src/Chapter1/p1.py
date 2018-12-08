####################################################
## 变量与表达式
####################################################

temperature = 98.6

original = temperature

temperature = temperature + 5.0

# 对象实例化
data = [3, 2, 1]

# 方法调用
data.sort()

value_bool = bool()  # 默认为False
value_int = int(3.14)  # ->3
value_int = int(-3.9)  # ->-3
value_int = int('127')  # 127
value_int = int('7f', 16)  # ->127
value_float = float()  # 0.0
value_float = float(3.14)  # 3.14
value_float = float('3.14')  # 3.14
value_float = float(6.022e23)

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]  # 引用型数组

value_tuple = (17,)

value_str = "SAMPLE"  # 索引型数组

# 比较大小
1 < 10  # => True
1 > 10  # => False
2 <= 2  # => True
2 >= 2  # => True

# 大小比较可以连起来！
1 < 2 < 3  # => True
2 < 3 < 2  # => False

# 字符串用单引双引都可以
"这是个字符串"
'这也是个字符串'

print("""看我的多行输出！这是第一行
第二行
第三行
""")

value_set = {12, 23, 34}
value_dict = {}
value_dict = {'name': 'robert', 'workIn': 'LinkWorld'}
value_dict = dict([('name', 'robert'), ('workIn', 'LinkWorld')])

print(True and True)  # and not or

a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)  # False
print(a == b)  # True

print(27/4)  # 6.75
# 27 = 6 * 4 + 3
print(27//4)  # 6
print(27 % 4)  # 3

# x的y次方
2**4 # => 16

data = [1, 2, 3, 4, 5, 6]
data1 = data[0:5:2]
0 in data  #  True

print(1 <= 2 < 3)  # True
print(1 <= 2 and 2 < 3)  # True


####################################################
## 流程控制
####################################################

# 先随便定义一个变量
some_var = 5
# 这是个if语句。注意缩进在Python里是有意义的
# 印出"some_var比10小"
if some_var > 10:
    print("some_var比10大")
elif some_var < 10:    # elif句是可选的
    print("some_var比10小")
else:                  # else也是可选的
    print("some_var就是10")

"""
用for循环语句遍历列表
打印:
    dog is a mammal
    cat is a mammal
    mouse is a mammal
"""
for animal in ["dog", "cat", "mouse"]:
    print("{} is a mammal".format(animal))

"""
"range(number)"返回数字列表从0到给的数字
打印:
    0
    1
    2
    3
"""
for i in range(4):
    print(i)

"""
while循环直到条件不满足
打印:
    0
    1
    2
    3
"""
x = 0
while x < 4:
    print(x)
    x += 1  # x = x + 1 的简写

# 用try/except块处理异常状况
try:
    # 用raise抛出异常
    raise IndexError("This is an index error")
except IndexError as e:
    pass    # pass是无操作，但是应该在这里处理错误
except (TypeError, NameError):
    pass    # 可以同时处理不同类的错误
else:   # else语句是可选的，必须在所有的except之后
    print("All good!")   # 只有当try运行完没有错误的时候这句才会运行

####################################################
## 函数
####################################################

# 用def定义新函数
def add(x, y):
    print("x is {} and y is {}".format(x, y))
    return x + y    # 用return语句返回

# 调用函数
add(5, 6)   # => 印出"x is 5 and y is 6"并且返回11

# 也可以用关键字参数来调用函数
add(y=6, x=5)   # 关键字参数可以用任何顺序

# 函数作用域
x = 5

def setX(num):
    # 局部作用域的x和全局域的x是不同的
    x = num # => 43
    print (x) # => 43

def setGlobalX(num):
    global x
    print (x) # => 5
    x = num # 现在全局域的x被赋值
    print (x) # => 6

setX(43)
setGlobalX(6)

print('End')
