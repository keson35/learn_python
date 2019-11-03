# 函数,如果函数不显式的调用 return函数，默认返回 None
def do_nothing():
    pass

print(do_nothing()) # print打印函数调用的结果是 None
# 没有参数但使用 return返回值
def agree():
    return True

result = agree()
result
print(result)


# 位置形参
# wine, entree, dessert 三个是位置形参,定义函数 menu()时，用于表明函数所需要传递的参数
def menu(wine, entree, dessert):
    return{'wine': wine, 'entree': entree, 'dessert': dessert}

menu('beef', 'bagel', 'bordeaux')
# 位置实参'beef', 'bagel', 'bordeaux'直接按照位置形参顺序提供，实参值分别存储到对应位置的形参内


# 关键字参数(函数调用时确定)
# 调用函数时，直接通过形参关键字确定与实参的对应关系
# 传递给函数的实参值直接存储在对应形参entree、dessert、wine之中
menu(entree='beef', dessert='bagel', wine='bordeaux')

# 默认参数(函数定义时确定)
# 定义函数时直接确定该形参的默认值，如果调用函数时不再对形参赋值，则保留其默认值
# 因为函数首次定义时，已经把默认值赋值给形参，如果默认值是可变对象，任何对默认形参的改变，
# 将影响下次函数调用时默认参数的值。所以建议默认参数的值设定为不可变对象，例如字符串或 None
def menu_2(wine, entree, dessert='pudding'):
    return{'wine': wine, 'entree': entree, 'dessert': dessert}


# 可变位置参数
# 以星号 * 将一组可变数量的参数集合成一个参数值的元祖
def print_args(*args):
    print('positional argument tuple: ', args)

print_args('arg1','arg2','arg3','arg4')
# 调用函数 print_args(*args) 结果：
#  positional argument tuple:  ('arg1', 'arg2', 'arg3', 'arg4')


# 可变关键字参数
# 以双兴号 ** 将一组可变数量的关键字参数集合成一个由关键字和实参为键值对的字典
def print_kwargs(**kwargs):
    print('Keyword argument: ', kwargs)

print_kwargs(entree='beef', dessert='bagel', wine='bordeaux')
# 调用函数print_kwargs(**kwargs)结果:
# Keyword argument:  {'entree': 'beef', 'dessert': 'bagel', 'wine': 'bordeaux'}


# 文档字符串
#  建议在函数体开始部分附上函数定义的说明文档，用三引号 '''  '''包裹，可拆分多行
#  help()函数可以打印函数的文档字符串


# 函数
# 函数的返回值可以赋值给变量例如：result = agree()
# 函数可以作为参数被其他函数调用
def add_args(arg1, arg2):
    print(arg1 + arg2)

def run_somethins_with_args(func, arg1, arg2):
    func(arg1, arg2)

run_somethins_with_args(add_args, 5, 9)
# 将add_args函数当做参数传入函数run_somethins_with_args，并存储在形参func中


# 内部函数
# 在函数中定义另一个函数
def outer(a, b):
    def inner(c, d):
        return(c + d)
    return inner(a, b)

outer(4, 7)
# 当需要在函数内部多次执行复杂任务时，内部函数很有用


# 内部函数可以看做一个闭包，闭包是一个由另一个函数动态生成的函数
def knight2(saying):
    def inner2():
        return("We are the knights who say: '%s'" % saying)
    return inner2
# inner2 就是一个闭包，一个被动态创建的可以记录外部变量 saying的函数

a = knight2('Duck')
b = knight2('Hasenpfeffer')
type(a)
type(b)
a()
b()


# 匿名函数 lambda()
# 匿名函数不需要定义过程，只需要一个语句表达，用来代替小函数
# 主函数，调用列表 words和函数 func作为参数，对列表的元素进行迭代并输入 func内，
# 作为函数的参数调用 func，最后打印结果
def edit_story(words, func):
    for word in words:
        print(func(word))

# 待调用的列表 things
things = ['apple', 'banana', 'watermelon','mango','grap']
# 显式定义函数 enliven()
def enliven(word):
    return word.capitalize() + '!'
# 调用主函数，以列表 things 和函数 enliven作为参数
edit_story(things, enliven)

# 待调用的列表 things
things = ['apple', 'banana', 'watermelon','mango','grap']
# 调用主函数，以匿名函数 lambda代替预定义函数enliven
# 冒号'：'后是匿名函数lambda的定义
edit_story(things, lambda word: word.capitalize() + '!')


# 生成器
# 生成器是用来创建python序列的对象，可以迭代庞大的序列，且不需要在内存中创建和存储序列
# 生成器推导式，其中 range()为可迭代对象，number_things为生成器
# 要打印生成器就必须对生成器进行迭代：使用 for循环或迭代器list()
# 生成器定义后只能使用一次，内存内不会存储，不能二次调用
number_things = (number for number in range(6))
# 等号'=' 右侧括号内是生成器推导式
for number in number_things:
    print(number)

number_things = (number for number in range(6))    
print(list(number_things))


# 生成器函数
# 生成器函数返回值以 yield声明，不使用return
# 创建 my_range()生成器函数，调用函数将创建生成器对象
def my_range( last, first=0, step=1):
    number = first
    while number < last:
        yield number
        number += 1
# 调用生成器函数创建生成器对象： my_range(6)并指向 range变量
ranger = my_range(6)
# 分别使用for循环和list()对生成器进行迭代
for x in ranger:
    print(x)   
list(ranger)


# 装饰器
# 装饰器是一个函数，它把 一个函数作为输入，并且返回另一个函数
# 装饰器函数内部会定义一个新的内部函数

# 平方装饰器
def squae_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        print('!',result) # 便于分辨 result 数值来源的标记
        return result * result
    return new_function

# 文档装饰器
def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        print('!!',result) # 便于分辨 result 数值来源的标记 
        return result
    return new_function

# 添加装饰器的函数
# 添加装饰器函数就相当于给函数套壳，对于两个以上连续添加的装饰器
# 函数就相当于自底向上，先套第一个装饰器生成新函数，然后再套第二个装饰器
# 添加装饰器的顺序会影响最终结果
@document_it
@squae_it
def add_ints(a, b):
    return a + b

# 调用已添加装饰器的函数
add_ints(3, 5)

# 变更装饰器添加顺序后的结果
def squae_it_2(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        print('!',result) # 便于分辨 result 数值来源的标记
        return result * result   
    return new_function

# 文档装饰器
def document_it_2(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        print('!!',result) # 便于分辨 result 数值来源的标记 
        return result   
    return new_function

@squae_it_2
@document_it_2
def add_ints_2(a, b):
    return a + b

# 调用已添加装饰器的函数
add_ints_2(3, 5)


# 每个程序的主要部分定义了：全局命名空间，在这个命名空间的变量是：全局变量
# 每个函数定义自己的命名空间，在函数内的变量是：局部变量
# 可以在函数内读取某个全局变量

# animal = 'fruitbat'
def print_global():
    print('inside print_global:', animal)

print('at the top level:', animal)
print_global()

# 如果函数外程序主要部分未定义全局变量，函数change_and_print_global()内
# 局部变量 animal赋值前引用，会提示错误 
# 只有声明读取全局变量(global animal)后，才可以在函数内修改全局变量
animal = 'fruitbat'
def change_and_print_global():
    global animal # 声明读取函数外全局变量
    animal = 'wombat' 
    print('inside change_and_print_global:', animal)
    
animal     
change_and_print_global()
animal

# locals()返回局部命名空间内容的字典，globals()返回全局命名空间内容的字典

def change_local():
    animal = 'wombat'
    print('locals:',locals())
    
animal = 'fruitbat'
change_local()
print('globals:', globals())
# 两个下划线__开始和结束的名称都是保留用法，用于python预定义变量，自定义变量不能使用它们
# 例如 __name__, __main__, __doc__等等，


