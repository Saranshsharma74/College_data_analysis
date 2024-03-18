import pyodbc
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sql_connection import connect_sql



conn = connect_sql()

query_college = """
select * from Courses 
"""
query_staff_Courses = """ SELECT c.CourseName, s.Name FROM Courses c INNER JOIN enrollments e ON c.CourseID = e.courseid
INNER JOIN Staff s ON e.enrollmentid = s.StaffID ORDER BY c.CourseName, s.Name """

students_df = pd.read_sql(query_staff_Courses, conn)

print(students_df.head())
print(students_df.info())
print(students_df.describe())

plt.figure(figsize=(6, 4))
sns.countplot(x='CourseName', data=students_df)
plt.title('Enrollment Counts by Department')
plt.xlabel('Department')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

conn.close()