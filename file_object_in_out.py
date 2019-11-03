
# 写入文件 write()方法
poem = """There was a young lady named Bright,
Whose speed was far faster than light:
She started one day
In a relative way,
And returned on the previous night."""

len(poem)

fout = open('relativity', 'wt') # 以强制写入模式，打开文件名为 relativity的 txt文件 并赋值给对象fout
fout.write(poem) # 将 poem对象 写入 fout对象所对应的的文件
fout.close() # 关闭 fout对象所对应的的文件