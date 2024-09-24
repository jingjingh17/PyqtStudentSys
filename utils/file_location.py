# /utils/file_location.py

import os

def get_project_root():
    """
    返回项目的根目录路径。
    """
    # 获取当前脚本的绝对路径
    current_file_path = os.path.abspath(__file__)
    # 获取当前脚本所在目录
    current_dir = os.path.dirname(current_file_path)
    # 倒推到项目根目录
    project_root = os.path.dirname(current_dir)
    return project_root

def getSysIconPath():
    return os.path.join(get_project_root(), 'resources', 'images', 'system.png')

def getUserIconPath():
    return os.path.join(get_project_root(), 'resources', 'icons', 'avatar.svg')

# 测试函数是否正确返回了根目录
if __name__ == "__main__":
    print("项目根目录:", get_project_root())