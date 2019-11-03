str_a = "exercise me!"
str_aa =str_a[0]
#str_a[0] = 'E' 字符串不可变，所以不能通过赋值方式改变原有字符串内容
# 可以通过[index]选取字符串对应的元素。
print(str_aa)
str_b = str_a.replace('e', 'a', 2)
# 把指定旧字符，替换为指定新字符，然后赋值给变量，原有字符串不变，
# 第三个参数为可选，代表要进行的替换次数
print(str_a)
print(str_b)
print(type(str_a))
print(type(str_b))
print(len(str_b))
print(str_a.split(" "))
str_list = str_a.split("e")
# 采用指定字符 '空格'做分隔符，将字符变量 a 分隔成元素,存入列表变量 str_list
d = 'e'.join(str_list)
# 对指定的粘合字符串 'e' 调用合并方法，对 列表变量 str_list 进行粘合，
# 使之还原成字符串
print(d)
result_1 = str_a.startswith('e')
# 是否以指定字符开始
result_2 = str_a.endswith('w')
# 是否以指定字符结尾
result_3 = str_a.find('r')
# 查找第一次出现指定字符的偏移量
result_4 = str_a.rfind('e')
# 查找最后一次出现指定字符的偏移量
result_5 = str_a.count('e')
# 统计出现指定字符的次数
result_6 = str_a.isalnum()
# 是否全部是字母数字
result_7 = str_a.strip('ex')
# 删除字符串开头或结尾的指定字符，不能删除中间的字符
result_8 = str_a.capitalize()
# 字符串首字母变成大写
result_9 = str_a.title()
# 字符串所有单词首字母变成大写
result_10 = str_a.upper()
# 字符串所有字母变成大写
result_11 = result_10.lower()
# 所有字母变成小写  
result_12 = result_9.swapcase()
# 字符串所有字母大小写转换
result_13 = str_a.center(21)
# 字符串在指定长度内居中
result_14 = str_a.ljust(21)
# 字符串在指定长度内靠左
result_15 = str_a.rjust(21)
# 字符串在指定长度内靠右
print(result_1)
print(result_2)
print(result_3)
print(result_4)
print("I find 'e' " + str(result_5) + " times in 'exercise'.")
# print函数参数必须是字符串格式，拼接字符串前需要将其他类型数据转换为字符串
print(result_6)
print(result_7)
print(result_8)
print(result_9)
print(result_10)
print(result_11)
print(result_12)
print(result_13)
print(result_14)
print(result_15)
print(5) 
# print()屏幕打印前会自动调用str()函数将数据转换成字符串