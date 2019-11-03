# 处理错误
shot_list =[1, 2, 3]
position = 5
try:
    shot_list[position]
except:
    print('Need a position between 0 and ', len(shot_list)-1, ' but got ', position)
    