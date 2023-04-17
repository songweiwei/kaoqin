from loguru import logger
from datetime import datetime, timedelta, date
from chinese_calendar import is_workday


def isWorkdays(date_value):
    """
    # 判断是否是法定节假日
    """
    if is_workday(date_value):
        print("{}是工作日".format(date_value))
        return True
    else:
        print("{}是休息日".format(date_value))
        return False


# 2、获取上一个工作日
def get_last_work_day(time_day):
    """
    # 获取上一个工作日
    """
    last_worker_day = ""

    # 最多查询20次
    query_time = 0

    while True:
        time_day = time_day - timedelta(days=1)

        if is_workday(time_day):
            last_worker_day = time_day.strftime("%Y-%m-%d")
            break
        elif query_time > 20:
            break
        query_time += 1

    return last_worker_day


if __name__ == '__main__':
    april_last = date(2023, 4, 16)

    # 或者在判断的同时，获取节日名
    import chinese_calendar as calendar  # 也可以这样 import

    on_holiday, holiday_name = calendar.get_holiday_detail(april_last)
    print(on_holiday, holiday_name)

    # 当前日期
    date_1 = datetime.now().date()
    print("date_1: {}, type: {}".format(date_1, type(date_1)))

    isWorkdays(date_1)

    # 人工输入日期
    date_2 = datetime.strptime("2022-03-19", '%Y-%m-%d').date()
    print("date_2: {}, type: {}".format(date_2, type(date_2)))

    isWorkdays(date_2)

    # 日期
    time_day = date.today()

    # 判断是工作日
    if is_workday(time_day):
        logger.info("{}是工作日！".format(time_day))
    else:
        logger.info("{}不是工作日！".format(time_day))

    last_work_day = get_last_work_day(time_day)
    logger.info("上一个工作日是: {}".format(last_work_day))
