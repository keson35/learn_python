empty_list = []
empty_list = list()
# 以上两种方法都可以用于创建空列表, list()可以将其他类型 ***可迭代对象*** 转换成列表
print(empty_list)

first_list = list('exercise')
print(first_list)
first_tuple = ('I', 'like', 'programing')
second_tuple = 'I',
# 元祖是不可变的列表，采用逗号',' 表示
print(first_tuple)
print(second_tuple)
second_list = list(first_tuple)
# list() 还可以用于将其他类型文件转换成列表,也可以将列表转换成列表，即：复制列表
print(second_list)

fruit = ['apple', 'banana', 'cherry', 'strawberry','watermelon']
print(fruit)
house = ['floor','window', 'door', 'room']
house_and_fruit = [house, fruit]
print(house_and_fruit)
a_fruit = house_and_fruit[1][2]
# 对嵌套列表 house_and_fruit使用双重索引提取元素——[1][2]，必须两个[][]中括号
print(a_fruit)
fruit[1] = 'peach'
house_and_fruit[1][2] = 'pear'
# 因为列表是可变数据类型，可以通过给提取元素赋值来修改列表中元素 
print(fruit)
print(house_and_fruit)

fruit = ['apple', 'banana', 'cherry', 'strawberry','watermelon']
fruit.append('blueberry')
print(fruit)
# list.append(object)方法将对象添加进列表尾部

fruit = ['apple', 'banana', 'cherry', 'strawberry','watermelon']
other_fruit = ['orange','pitaya','apricot','plum']
fruit.extend(other_fruit)
# list1.exten.list2 将 list2中的元素合并到 list1
print(fruit)

fruit = ['apple', 'banana', 'cherry', 'strawberry','watermelon']
fruit.insert(1, 'mango')
# 在索引数字 1之前插入元素
print(fruit)

del fruit[0]
# 通过[]提取方法，删除指定索引值对应的元素
print(fruit)

fruit.remove('mango')
# 删除列表中具有指定值的元素
print(fruit)

last_fruit = fruit.pop()
# pop 方法无参数，默认获取并删除列表最后一个元素
print(last_fruit)

fruit = ['apple', 'banana','pear', 'peach','mango', 'cherry', 'strawberry', 'watermelon']
sec_fruit = fruit.pop(1)
# 获取并删除指定索引值得元素
print(sec_fruit)

fruit = ['apple', 'banana','pear', 'peach','mango', 'cherry', 'strawberry', 'watermelon']
fruit_index = fruit.index('pear')
# 查询列表内指定值元素的索引值——即位置
print(fruit_index)

fruit = ['apple', 'banana','pear', 'peach','mango', 'cherry', 'strawberry', 'watermelon']
banana_in_fruit = 'banana' in fruit
# 判断特定元素是否在列表中
print(banana_in_fruit)

one_fruit_count = fruit.count('apple')
# 记录特定元素出现在列表中的次数
print(one_fruit_count)

star_str = ' * '
str_list = star_str.join(fruit)
# 使用粘接符'*'对列表进行合并，最终成为长字符串
print(str_list)

fruit = ['apple', 'banana','pear', 'peach','mango', 'cherry', 'strawberry', 'watermelon']
fruit.sort()
# 使用sort()方法对愿列表进行重新排列
print(fruit)

fruit = ['apple', 'banana','pear', 'peach','mango', 'cherry', 'strawberry', 'watermelon']
new_fruit = sorted(fruit)
print(new_fruit)

new_fruit[1] = 'grape'
# '=' 可以用于给提取出的元素赋值
print(new_fruit)



new_fruit_1 = fruit.copy()
new_fruit_2 = list(fruit)
new_fruit_3 = fruit[:]
# 以上三种方法都可以用于复制列表
print(new_fruit_1, new_fruit_2, new_fruit_3)

print(len(fruit))
# len(fruit) 函数作用是获取列表长度



