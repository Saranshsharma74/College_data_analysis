import pyodbc
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sql_connection import connect_sql

conn = connect_sql()

query_Department = """
select * from department
"""



query_courses_Department = """ SELECT d.departmentname, c.CourseName FROM department d INNER JOIN Courses c ON d.departmentid = c.DepartmentID
ORDER BY d.departmentname, c.CourseName """

students_df = pd.read_sql(query_courses_Department, conn)

print(students_df.head())
print(students_df.info())
print(students_df.describe())

plt.figure(figsize=(6, 4))
sns.countplot(x='departmentname', data=students_df)
plt.title('Enrollment Counts by Department')
plt.xlabel('CourseName')
plt.ylabel('Depatmentname')
plt.xticks(rotation=45)
plt.show()

conn.close()