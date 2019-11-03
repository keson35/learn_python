# 命名元祖 
# 可以通过名称(.name)来访问其中的值，也可以通过位置[]提取进行访问
from collections import namedtuple
# 一种创建命名元祖的方法 —— 使用 namedtuple()方法
Duck = namedtuple('Duck', 'bill tail')
duck = Duck('wild orange', 'long')
 
# 另一种创建命名元祖的方法 —— 利用字典来构造
parts = {'bill':'wild orange', 'tail':'long'}
duck2 = Duck(**parts)
duck.bill
duck.tail
duck[0]
duck[1]
print(duck)
# >>> print(duck)
# Duck(bill='wild orange', tail='long') 命名元祖的格式