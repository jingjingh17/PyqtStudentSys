"""
返回开放选课的信息和未开放选课的信息--模拟数据
"""
import random

class courseData:
    def __init__(self):
        self.openData = []
        self.noOpenData = []

    def generate_random_data(self, num_courses=10):
        # 定义一些中文数据
        course_names = ["数学", "物理", "化学", "生物", "计算机科学", "机械工程", "电气工程", "土木工程", "环境科学", "材料科学"]
        colleges = ["理学院", "工学院", "文学院", "商学院", "法学院", "医学院", "艺术学院", "教育学院", "信息学院", "管理学院"]
        teachers = ["张教授", "李教授", "王教授", "赵教授", "陈教授", "周教授", "吴教授", "郑教授", "孙教授", "胡教授"]
        credits = [3, 4, 5]

        # 生成开放课程数据
        for _ in range(num_courses):
            self.openData.append({
                'id': random.randint(100000, 999999),
                'name': random.choice(course_names),
                'college': random.choice(colleges),
                'teacher': random.choice(teachers),
                'coursesNum': random.randint(100, 150),
                'nowNum': random.randint(0, 99),
                'is_open': '是',
                'is_finished': '否',
                'credit': random.choice(credits)
            })

        # 生成未开放课程数据
        for _ in range(num_courses):
            self.noOpenData.append({
                'id': random.randint(100000, 999999),
                'name': random.choice(course_names),
                'college': random.choice(colleges),
                'teacher': random.choice(teachers),
                'coursesNum': random.randint(100, 150),
                'nowNum': '0',
                'is_open': '否',
                'is_finished': '否',
                'credit': random.choice(credits)
            })

    def openCoursedata(self):
        self.generate_random_data(10)
        return self.openData

    def noOpenCoursedata(self):
        return self.noOpenData

# 示例
if __name__ == '__main__':
    data_manager = courseData()
    data_manager.generate_random_data(10)

    print("开放课程数据:")
    print(data_manager.openCoursedata())

    print("\n未开放课程数据:")
    print(data_manager.noOpenCoursedata())