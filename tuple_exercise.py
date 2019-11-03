empty_tuple = ()
empty_tuple = tuple()
# 以上两种方法都可以创建空白元祖

one_tuple = 'apple',
# 逗号 ',' 才是元祖的标志，没有逗号，变量类型将变成字符串，即使添加小括号('apple')也不能例外。

fruit_tuple = 'apple', 'banana', 'cherry'
a, b, c, = fruit_tuple
# 元祖可以一次赋值给多个变量，这个过程叫做元祖解包(与元祖相似的列表却不可以！！！)
print(a, b, c)
d_tuple = fruit_tuple[0]
e_tuple = fruit_tuple[:1]

print(d_tuple)
print(e_tuple) 
print(type(d_tuple))
print(type(e_tuple))