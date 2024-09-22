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
    

if __name__ == "__main__":
    res = course().inquireCourse()
    for i in range(len(res)):
            row_data = res[i]
            for j in range(len(row_data)):
                 print(row_data[j], end=" ")
    

    