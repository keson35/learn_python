# 从包 sources 中导入 模块 daily, weekly
from sources import daily, weekly
   
print("Daily forecast:",daily.forecast())
print("Weekly forecast:")
for number, outlook in enumerate(weekly.forecast(), 1):
    print(number, outlook)
