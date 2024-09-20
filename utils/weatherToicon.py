from  utils.file_location import get_project_root
from utils.weather import Geolocation, wea
import os

class weatherToicon:
    """输入天气，输出对应的图标"""
    def __init__(self):
        self.project_root = get_project_root()
        self.images_path= os.path.join(self.project_root, 'resources', 'images')
        self.common_weather_conditions = [
            "晴", 
            "多云", 
            "阴", 
            "阵雨", 
            "雷阵雨", 
            "雷阵雨伴有冰雹", 
            "雨夹雪", 
            "小雨", 
            "中雨", 
            "大雨", 
            "暴雨", 
            "大暴雨", 
            "特大暴雨", 
            "阵雪", 
            "小雪", 
            "中雪", 
            "大雪", 
            "暴雪", 
            "雾", 
            "冻雨", 
            "沙尘暴"
        ]
        
        self.ak = "7K7jyGHsl1FOO6RZg87jnf5gsuS3xPiy"
        self.geo = Geolocation(self.ak)

        # 获取当前位置
        self.location = self.geo.get_location()

        # 省份信息
        self.province = self.geo.get_province(self.location[0], self.location[1])

        self.wea = wea(self.ak, self.province)

        # 今日天气和预报天气
        self.weather_now,self.weather_list = self.wea.weatherCheck()
        self.iconPath = self.batch_get_icon_path(self.weather_list)
    def get_icon_path(self,weather):
        '''返回对应天气图标路径'''
        if weather in self.common_weather_conditions:
            return os.path.join(self.images_path, weather + ".svg")
        else:
            return ('N/A')
        
    def batch_get_icon_path(self,weather_list):
        '''批量返回对应天气图标路径'''
        return [self.get_icon_path(weather["text_day"]) for weather in weather_list]
        
if __name__ == "__main__":
    w = weatherToicon()