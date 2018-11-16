import time
import calendar

#获取时间戳
ticks = time.time()
print(ticks)

#获取当前时间(时间元组，年 月 日 时 分 秒 周几+1 天 夏令时)
local_time = time.localtime(ticks)
print("本地时间为：",local_time)

#获取格式化时间
local_time = time.asctime(local_time)
print("格式化本地时间：",local_time)

#格式化日期
"""
    %y 两位数的年份表示（00-99）
    %Y 四位数的年份表示（000-9999）
    %m 月份（01-12）
    %d 月内中的一天（0-31）
    %H 24小时制小时数（0-23）
    %I 12小时制小时数（01-12）
    %M 分钟数（00=59）
    %S 秒（00-59）
    %a 本地简化星期名称
    %A 本地完整星期名称
    %b 本地简化的月份名称
    %B 本地完整的月份名称
    %c 本地相应的日期表示和时间表示
    %j 年内的一天（001-366）
    %p 本地A.M.或P.M.的等价符
    %U 一年中的星期数（00-53）星期天为星期的开始
    %w 星期（0-6），星期天为星期的开始
    %W 一年中的星期数（00-53）星期一为星期的开始
    %x 本地相应的日期表示
    %X 本地相应的时间表示
    %Z 当前时区的名称
    %% %号本身
"""

print(time.strftime("%Y-%m-%d %I:%M:%S %p",time.localtime(time.time())))


#获取2018年8月月历
cal_8 = calendar.month(2018,8)
print(cal_8)

#判断是不是闰年
bFlag = calendar.isleap(2018)
print(bFlag)