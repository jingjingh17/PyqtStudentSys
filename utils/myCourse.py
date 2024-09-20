"""
返回课程数据：课程总数，课程详情信息
返回学分数据：计算已选修学分，总学分
"""
import random


class myCourse:
    def __init__(self):

        self.course_names = [
            "Python编程基础", "Java编程", "Web前端开发", "数据库设计", "算法与数据结构",
            "操作系统原理", "计算机网络", "人工智能导论", "机器学习", "深度学习"
        ]
        self.colleges = ["计算机科学与技术学院", "软件工程学院", "信息工程学院", "自动化学院"]
        self.teachers = [
            "张老师", "李老师", "王老师", "赵老师", "陈老师", "刘老师", "杨老师", "黄老师", "周老师", "吴老师"
        ]
        self.is_open_options = ['是', '否']
        self.is_finished_options = ['是', '否']
        self.credits = [2, 3, 4]
        
        self.courseNum = 0
        self.courseList = []

        self.score = 0
        self.totalScore = 35
        
    def getCourse(self):
        self.courseNum = random.randint(5, 15)
        for _ in range(self.courseNum):
            self.courseList.append({
                'id': random.randint(100000, 999999),
                "name": random.choice(self.course_names),
                "college": random.choice(self.colleges),
                "teacher": random.choice(self.teachers),
                "coursesNum": random.randint(10, 30),
                "is_open": random.choice(self.is_open_options),
                "is_finished": random.choice(self.is_finished_options),
                "credit": random.choice(self.credits)
            })
        
        for i in range(len(self.courseList)):
            self.score += self.courseList[i]["credit"]
            
        return self.courseNum,self.score,self.courseList
    
    def getColleges(self,courseList):
         colleges = [course["college"] for course in courseList]
         uniqueColleges = list(set(colleges))
         return uniqueColleges
         



if __name__ == "__main__":
    myCourse = myCourse()
    a,b,c = myCourse.getCourse()
    list1 = myCourse.getColleges()
    print(list1)
                