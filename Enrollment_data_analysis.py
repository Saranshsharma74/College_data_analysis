import pyodbc
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sql_connection import connect_sql


conn = connect_sql()

query_Enrollemnts = """
select * from enrollments
"""

query_Enrollments = """ SELECT 
    YEAR(Dateofregistration) AS EnrollmentYear,
    CASE 
        WHEN MONTH(Dateofregistration) BETWEEN 1 AND 6 THEN 'Spring'
        WHEN MONTH(Dateofregistration) BETWEEN 7 AND 12 THEN 'Fall'
    END AS EnrollmentSemester,
    COUNT(*) AS EnrollmentCount
FROM enrollments
GROUP BY 
    YEAR(Dateofregistration),
    CASE 
        WHEN MONTH(Dateofregistration) BETWEEN 1 AND 6 THEN 'Spring'
        WHEN MONTH(Dateofregistration) BETWEEN 7 AND 12 THEN 'Fall'
    END """

students_df = pd.read_sql(query_Enrollments, conn)

print(students_df.head())
print(students_df.info())
print(students_df.describe())

plt.figure(figsize=(6, 4))
sns.countplot(x='EnrollmentCount', data=students_df)
plt.title('Enrollment Counts by Department')
plt.xlabel('CourseName')
plt.ylabel('Depatmentname')
plt.xticks(rotation=45)
plt.show()

conn.close()