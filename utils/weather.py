import geocoder
import requests
import json
import csv
import os

from utils.file_location import get_project_root

class Geolocation:
    def __init__(self, ak):
        self.ak = ak
        self.url = "https://api.map.baidu.com/reverse_geocoding/v3"

    def get_location(self):
        """获取当前设备的地理定位（通过 IP 地址）"""
        g = geocoder.ip('me')
        location = g.latlng  # 返回 [纬度, 经度]
        return location

    def get_province(self, lat, lng):
        """根据经纬度获取省份信息"""
        params = {
            "ak": self.ak,
            "output": "json",
            "coordtype": "wgs84ll",
            "extensions_poi": "0",
            "location": f"{lat}, {lng}",
        }

        response = requests.get(url=self.url, params=params)
        if response.status_code == 200:
            data = json.loads(response.text)
            province = data["result"]["addressComponent"]["city"]
            return province
        else:
            return None
class wea:
    """
    参数： ak , 地区信息
    根据省份获取地区代码，然后根据代码获取天气信息
    """
    def __init__(self, ak, loaction):
        self.ak = ak
        self.url = "https://api.map.baidu.com/weather/v1/"
        self.location = loaction
        self.project_root = get_project_root()
        self.csv_file = os.path.join(self.project_root, 'resources', 'weather_district_id.csv')

    def loctionToId(self):
        """将省份转换为地区代码"""
        with open(self.csv_file, mode="r",encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["city"] == self.location:
                    return row["code"]
        return None
    
    def weatherCheck(self):
        """获取天气信息,台湾各市无法查询"""
        district_id = self.loctionToId()
        params = {
            "district_id":    district_id,
            "data_type":    "all",
            "ak":       self.ak,
        }
        # 获取天气信息
        response = requests.get(url=self.url, params=params)
        data = json.loads(response.text)
        if data["message"] != "success":   # 获取天气信息失败
            print("获取天气信息失败！", data["message"])
            return
        # 当前天气信息
        self.weather_now = data["result"]["now"]  # 字典
        # 未来七天天气列表，包含今天
        self.weather_list = data["result"]["forecasts"]
        return self.weather_now,self.weather_list


# 使用示例
if __name__ == "__main__":
    ak = "7K7jyGHsl1FOO6RZg87jnf5gsuS3xPiy"
    geo = Geolocation(ak)

    # 获取当前位置
    location = geo.get_location()

    # 根据经纬度获取省份
    province = geo.get_province(location[0], location[1])

    wea = wea(ak, province)
    wea.weatherCheck()