# import modelname 导入整个模块，函数调用要加上模块名前缀
# from modelname import funcname 导入模块中函数，注意现有程序中不能出现重名函数
# 下面两种导入方式，都是函数内部导入

def get_description1():
    import random #导入方式 1 导入整个模块，函数调用需要添加模块名前缀
    possibilities =['rain', 'snow', 'sleet', 'fog', 'sun', 'who know']
    return random.choice(possibilities)

def get_description2():
    from random import choice #导入方式 2，导入模块的指定函数，需要注意函数重名问题
    possibilities =['rain', 'snow', 'sleet', 'fog', 'sun', 'who know']
    return choice(possibilities)


# 如果导入代码需要多次使用应考虑在函数外部导入
import random #导入方式 3，在函数外部导入，可多次使用
def get_description3():
    possibilities =['rain', 'snow', 'sleet', 'fog', 'sun', 'who know']
    return random.choice(possibilities)


# 使用别名导入函数
# 使用别名 wr导入整个 report模块, 简化函数调用时的前缀
import report as wr 
description = wr.get_description()
print("Today's weather:", description)

# 使用别名 do_it从 report模块导入函数 get_description，可防止代码内含有重名函数
from report import get_description as do_it
description = do_it()
print("Today's weather:", description)
