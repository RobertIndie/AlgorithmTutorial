print('欢迎使用GPA计算器')
print('请输入你的成绩等级，一行一个。')
print('输入为空代表结束')
# 将成绩等级映射到成绩绩点
points = {'A+':4.0, 'A':4.0, 'A-':3.67, 'B+':3.33, 'B':3.0, 'B-':2.67,
          'C+':2.33, 'C':2.0, 'C':1.67, 'D+':1.33, 'D':1.0, 'F':0.0}
num_courses = 0
total_points = 0
done = False
while not done:
    grade = input()                          # 读取控制台输入
    if grade == '':                          # 检测到输入为空
        done = True
    elif grade not in points:                # 未被识别的成绩
        print("未知成绩 {0}".format(grade))
    else:
        num_courses += 1
        total_points += points[grade]
if num_courses > 0:                        # 避免除以0
    print('你的GPA： {0:.3}'.format(total_points / num_courses))