# 多行代码，使用连接符 '\'放在一行的结尾，python仍然将其解释为一行

# 使用 if， elif， else 进行判断，语句末尾要加上冒号(:)

# 使用 while 进行循环,，语句末尾要加上冒号(:)
# 使用break跳出循环，使用continue跳到循环开始

# 使用 for 进行迭代，语句末尾要加上冒号(:)

# 对 while、for 代码段后追加 else代码段可以用来判断循环是否正常结束

fruit_dict = {'1':'apple', '2': 'banana', '3': 'cherry', '4': 'strawberry', '5': 'watermelon','6': 'pear', '7': 'buleberry'}
for key in fruit_dict:
    print(key)
# 对字典进行迭代将返回字典的键,等同于对字典使用 keys() 函数 
# for key in dict: 等同于 for key in dict.keys():

fruit_dict = {'1':'apple', '2': 'banana', '3': 'cherry', '4': 'strawberry', '5': 'watermelon','6': 'pear', '7': 'buleberry'}
for value in fruit_dict.values():
    print(value)
# 对字典的值进行迭代需要 : for value in dict.values(): 这种格式，使用 values()函数

fruit_dict = {'1':'apple', '2': 'banana', '3': 'cherry', '4': 'strawberry', '5': 'watermelon','6': 'pear', '7': 'buleberry'}
for item in fruit_dict.items():
    print(item)

# 并行迭代
number1 = [1, 2, 3, 4]
number2 = ['one', 'two', 'three', 'four']
iterator = zip(number2, number2)
# zip()函数创建的是可迭代对象，不是元祖或者列表,zip()对象不能直接使用print()打印，
# 需要使用for函数遍历整个迭代对象后打印。
for number_1, number_2 in zip(number1, number2):
    print(number_1, ':',number_2)
# 打印结果：
# 1 : one
# 2 : two
# 3 : three
# 4 : four
list(zip(number1, number2))

# range(start，stop，step)生成自然数序列，并且和zip()相同，生成的是可迭代对象
# step默认值是 1，当step是-1时，创建反向自然数序列
list(range(5))
for x in range(0, 3):
    print(x)
# 与zip()命令相同，range()是可迭代对象，也不能直接使用print()命令打印
# 需要使用for函数遍历整个迭代对象后打印

# 列表推导式
number_list = [number for number in range(0,6)]
number_list
# 列表推导式也可以加上条件
number_list1 = [number for number in range(0,6) if number % 2 == 1] 
number_list1
# 列表推导式可以推倒双值元祖的列表、双值列表的列表，同样每个遍历都可以添加自己的条件
number_set = [(small_number,big_number) for small_number in range(0,6) for big_number in range(6,11) if small_number % 2 == 1 if big_number % 2 == 0]
print(number_set)
number_list2 = [[small_number,big_number] for small_number in range(0,6) for big_number in range(6,11)]
print(number_list2)

# 字典推导式
# 格式：{key:value for expression in iterable}
word = 'letters'
letters_counts ={letter:word.count(letter) for letter in set(word)}
letters_counts

# 生成器推导式，使用()包裹，生成一个 generator对象，惰性，不直接生成所有元素，
# 需要通过使用for循环实现所有元素迭代
# 没有元祖推导式，只有列表、字典、生成器推导式
number_thing = (number for number in range(1,6))
for x in number_thing:
    print(x)
number_thing = (number for number in range(1,6))   
number_list3 = list(number_thing)
number_list3
list(number_thing) # number_thing生成器第二次使用时，生成器被擦除，list()函数变成空列表
