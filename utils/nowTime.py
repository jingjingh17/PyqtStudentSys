import time

class Time:
    def __init__(self):
        # 获取当前时间戳
        current_time = time.time()
        # 将时间戳转换为本地时间
        
    def get_current_time(self, format="%Y %m/%d %A"):
        """
        返回当前时间的字符串表示。
        参数:
            format (str): 时间格式化字符串，默认为 "%Y %m/%d %A"。
        返回:
            str: 格式化后的时间字符串。
        """
        # 使用strftime将时间元组格式化为字符串
        return time.strftime(format, time.localtime())

# 创建 Time 类的实例
current_time = Time()

# 打印当前时间
print(current_time.get_current_time())