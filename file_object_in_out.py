# 写入文件 write()方法
poem = """There was a young lady named Bright,
Whose speed was far faster than light:
She started one day
In a relative way,
And returned on the previous night."""

len(poem)

# 创建并打开文件
fout = open('relativity', 'wt') # 以创建或替换模式打开 relativity文件，赋值给对象 fout
                                # wt代表写入文本文件 
# 'r' 读取 例如'rt'
# 'w' 创建后写入或替换已有内容 例如'wt'
# 'x' 创建后写入内容，不能替换已有内容 例如'xt'
# 'a'  在文件末尾追加内容 例如'at'
# 't'  文本类型
# 'b'  二进制类型 例如 'wb'

# 使用 write()写入文件
fout.write(poem) # 将 poem对象 写入 fout对象所对应的的文件 relativity

# 关闭 fout对象所对应的文件 relativity
fout.close()

poem2 = """There was a young lady named Bright,
Whose speed was far faster than light:
She started one day
In a relative way,
And returned on the previous night."""

fout2 = open('relativity2', 'wt')
print(poem2, file=fout2) # poem2参数是要打印输出的对象，file参数是要写入的文件对象
fout2.close()

# 文件分块写入
poem3 = """There was a young lady named Bright,
Whose speed was far faster than light:
She started one day
In a relative way,
And returned on the previous night."""

fout3 = open('relativity', 'wt')
size = len(poem3)
offset = 0
chunk = 100
while True:
    if offset > size:
        break
    fout3.write(poem3[offset:offset+chunk])
    offset += chunk

fout3.close


# 使用 read()、readline()、readlines()读取文本文件

# 以读取模式打开 relativity文件
fin = open('relativity', 'rt')
poem = fin.read() # 对 fin对象调用 read()方法
fin.close() # 关闭对象 fin
len(poem) # 计算 poem对象的字符长度

# 设置最大读入字符限制
poem = ''
fin = open('relativity', 'rt')
chunk = 100 # chunk对象的数值就是读入上限
while True: # while 循环 read()方法自动读取后续内容
    fragment = fin.read(chunk) # chunk 是传入read()方法的字符数量参数
    if not fragment:
        break
    poem += fragment
fin.close()
len(poem)
print(poem)

# readline()方法，每次读入文件的一行
poem = ''
fin = open('relativity', 'rt')
while True: 
    fragment = fin.readline()
    if not fragment:
        break
    poem += fragment
fin.close()
len(poem)
type(poem)

# 读取文件的最简单方式是使用一个迭代器
poem = ''
fin = open('relativity', 'rt')
for line in fin:
    poem += line
fin.close()
len(poem)
type(poem)

# readlines()方法读取后返回的是由单行字符串所构成的列表
fin = open('relativity', 'rt')
lines = fin.readlines() 
fin.close()
print(len(lines), 'lines read')
print(lines) # 正常打印单行字符串列表，不换行
for line in lines: # 删除换行符，逐行打印字符串列表
    print(line, end='') 
type(lines) # lines 是个列表，如下：
#['There was a young lady named Bright,\n', 'Whose speed was far faster than light:\n', 'She started
# one day\n', 'In a relative way,\n', 'And returned on the previous night.']


# 使用 write()写二进制文件
bdata = bytes(range(0, 256)) # 创建二进制文件
len(bdata)

fout = open('bfile', 'wb') # 创建或重写模式打开文件 bfile，并指向对象fout
fout.write(bdata) # 将 bdata内容写入fout对象所对应的文件 bfile
fout.close()


# 使用 read()读二进制文件
fin = open('bfile', 'rb')
bdata = fin.read()
len(bdata)
fin.close()


# 使用 with 自动关闭文件
with open('relativity', 'wt') as fout:
    fout.write(poem)
