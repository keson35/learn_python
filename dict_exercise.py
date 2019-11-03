empty_dict = {}
#{}大括号将一系列由逗号分隔的键值对 key：value 包裹起来形成字典，key通常是字符串或者其他不可变类型对象
print(empty_dict)
ordered_fruit = [['1', 'apple'], ['2', 'banana'], ['3', 'cherry'], ['4', 'strawberry'],['5', 'watermelon']]
fruit_dict = dict(ordered_fruit)
# dict(object) 方法将其他双值对象转换成字典，如：双值元祖的列表，双值列表的元祖，双字符串组成的列表或者元祖
print(fruit_dict)


fruit_dict['4'] = 'grape'
# 字典也可以对选取的[key]的方式修改key对应的value值，和列表相同
# 字典的key必须互不相同，如果一个键出现两次，后一个出现的键值对会替换前一个
print(fruit_dict)

orther_fruit_dict = {'5': 'pear', '6': 'buleberry'}
fruit_dict.update(orther_fruit_dict)
# dict1.update(dict2) 将dict2中的元素合并至dict1，与list的extend方法功能相同
print(fruit_dict)

fruit_dict = {'1':'apple', '2': 'banana', '3': 'cherry', '4': 'strawberry', '5': 'watermelon','6': 'pear', '7': 'buleberry'}
del fruit_dict['1']
# 删除字典指定键所对应的元素
fruit_dict

fruit_dict.clear()
# 删除字典的所有元素
print(fruit_dict)

fruit_dict = {'1':'apple', '2': 'banana', '3': 'cherry', '4': 'strawberry', '5': 'watermelon','6': 'pear', '7': 'buleberry'}
resout = '1' in fruit_dict
# 判断特定键是否在字典中
print(resout)

fruit2 = fruit_dict['2']
# [key]方法可用于提取字典键所对应的值
print(fruit2)
fruit3 = fruit_dict.get('2')
# dict.get(key)方法也可用于提取字典键所对应的的值
fruit8 = fruit_dict.get('8', "Don't have that fruit.")
#dict.get(key, default_value)方法中的defaut_value用于找不到指定键时输出默认值
print(fruit3)
print(fruit8)

all_keys = fruit_dict.keys()
# 使用dict.keys()获取字典所有的键
print(type(all_keys))
list(all_keys)

all_values = fruit_dict.values()
# 使用dict.values()获取字典的所有值
all_values
list(all_values)

all_items = fruit_dict.items()
# 使用dict.items()获取字典的所有键值对
all_items
list(all_items)
dict(list(all_items))

fruit_dict = {'1':'apple', '2': 'banana', '3': 'cherry', '4': 'strawberry', '5': 'watermelon','6': 'pear', '7': 'buleberry'}
new_fruit_dict = fruit_dict
# 赋值操作并不会产生dict的副本，只是将dict对象映射到两个变量名
fruit_dict['1'] = 'grape'
fruit_dict
new_fruit_dict

fruit_dict = {'1':'apple', '2': 'banana', '3': 'cherry', '4': 'strawberry', '5': 'watermelon','6': 'pear', '7': 'buleberry'}
new_fruit_dict = fruit_dict.copy()
# dict.copy()方法才会创建dict副本对象，避免更改对象后副本对象也同时发生变化
fruit_dict['1'] = 'plum'
fruit_dict
new_fruit_dict

