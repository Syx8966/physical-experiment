import math as mt
# 以下为计算时用到的物理参数
# ----------------------------
e = 1.60e-19  # 标准元电荷
ro = 981    # 油滴密度-空气密度
b = 6.17e-6       # 修正粘滞系数时的修正常数
p = 76       # 修正粘滞系数时的大气压力
d = 5e-3           # 版间距
g = 9.795          # 重力加速度
ne = 1.83e-5       # 修正前粘滞系数
l = 2e-3         # 油滴运动距离
# ----------------------------
v = float(input('请输入电压:'))
t = []
t1, t2, t3, t4, t5 = map(float, input('请输入5组下落时间，以空格分隔:').split())
sum = t1 + t2 + t3 + t4 + t5
av_t = sum / 5     # 计算下落时间平均值
print('下落时间平均值:'+str(av_t))
vg = l / av_t      # 计算下落速度
a = mt.sqrt((9 * ne * vg) / (2 * ro * g))  # 计算油滴半径13
print('油滴半径:'+str(a))
ne_x = ne / (1 + b / (p * a))  # 计算修正后粘滞系数
q = (18 * mt.pi * d) * pow(ne_x * vg, 1.5) / (mt.sqrt(2 * ro * g) * v)  # 静止法算电荷

print('总电荷:'+str(q))
if (q % e < 0.5 * e):
    qn = q // e
else:
    qn = (q // e) + 1  # 计算油滴带元电荷数
print('油滴带元电荷数:'+str(qn))
ca_e = q / qn  # 计算实验得元电荷值
print('由本组实验数据得元电荷值:'+str(ca_e))
er = abs(ca_e - e) / e * 100  # 计算误差百分比
print('误差百分比'+str(er) + '%')