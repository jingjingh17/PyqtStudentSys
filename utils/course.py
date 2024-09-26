"""
课程信息数据库
"""

import sqlite3
from utils.file_location import get_project_root

class course:
    def __init__(self):
        self.root = get_project_root()
        self.dbPath = self.root + '\\db\\Maindb.db'

        self.conn = sqlite3.connect(self.dbPath)
        
    def inquireCourse(self):
        """
        查询课程信息，包含开放未开放
        """
        cursor = self.conn.execute(
            """
            SELECT 
            courses.course_id,
            courses.course_num,
            courses.course_name,
            courses.course_college,
            courses.course_quality,
            courses.course_sele_quality,
            courses.course_state,
            courses.credits,
            teachers.username AS teacher_name,
            teachers.teacherid
            FROM 
                courses
            INNER JOIN 
                teachers ON courses.teacher_id = teachers.teacherid;
            
            """
        )
        result = cursor.fetchall()
        return result
    
    def seleCourse(self,studentId,courseId):
         # 检查是否已经选课
         cursor = self.conn.execute(
            """
            SELECT * FROM Enrollments WHERE student_id = ? AND course_id = ?;
            """,
            (studentId, courseId)
        )
        
         # 检查课是否已满
         cursor2 = self.conn.execute(
            """
            SELECT course_quality,course_sele_quality FROM Courses WHERE course_id = ?;
            """,
            (courseId,)
        )
         result = cursor2.fetchone()

         # 课满
         if result[0] <= result[1]:
             return "课满"

         # 重复选课
         if cursor.fetchone():
             return "重复选课"
         else:
             self.conn.execute(
                """
                INSERT INTO Enrollments (student_id, course_id) VALUES (?, ?);
                """,
                (studentId, courseId)
            )
             self.conn.commit()
             return True
            
         pass

    
    def myCourse(self,studentId):
         studen_id = studentId
         cursor = self.conn.execute(
            """
            SELECT 
            Enrollments.student_id,
            Courses.course_id,
            Courses.course_num,
            Courses.course_name,
            Courses.course_college,
            Courses.course_quality,
            Courses.course_state,
            Courses.credits,
            Teachers.username AS teacher_name,
            Teachers.teacherid
            FROM Enrollments
            INNER JOIN Courses ON Enrollments.course_id = Courses.course_id
            INNER JOIN Teachers ON Courses.teacher_id = Teachers.teacherid
            WHERE Enrollments.student_id = ?;
           """,
           (studen_id,)
         )
         result = cursor.fetchall()
         return result
    
if __name__ == "__main__":
    res = course().myCourse(42)
    print(res)
    

    