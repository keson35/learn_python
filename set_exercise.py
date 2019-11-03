empty_set = set()
# set()创建集合，也可以将其他类型对象转换成集合，重复的值将被舍弃
# 与字典的键一样，集合是无序的
fruit_dict = {'1':'apple', '2': 'banana', '3': 'cherry', '4': 'strawberry', '5': 'watermelon','6': 'pear', '7': 'buleberry'}
fruit_set = set(fruit_dict)
# 将字典作为参数传入set()时，只有键会被传入，值则被忽略

# a & b  a.intersection(b)   交集

# a | b  a.union(b)          并集

# a - b  a.difference(b)     差集

# a ^ b  a.symmetric(b)      异或集

# a <= b  a.issubset(b)      子集

# a < b                      真子集

# a >= b  a.issuperset(a)    超集

# a > b                      真超集


