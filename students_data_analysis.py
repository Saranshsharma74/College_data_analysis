import pyodbc
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sql_connection import connect_sql

# Connect to the database
#conn = pyodbc.connect('DRIVER={YourDriver};SERVER=YourServer;DATABASE=YourDatabase;UID=YourUsername;PWD=YourPassword')
conn = connect_sql()
# Define SQL queries
query_students = """
select * from students
"""
query_courses_Student = """ SELECT c.CourseName , s.Name FROM Courses c INNER JOIN enrollments e ON c.CourseID = e.courseid INNER JOIN Students s ON e.studentid = s.StudentID 
ORDER BY c.CourseName, s.StudentID """

# Execute SQL queries and fetch data into pandas DataFrames
students_df = pd.read_sql(query_courses_Student, conn)

# Data Exploration
print(students_df.head())
print(students_df.info())
print(students_df.describe())

# Data Analysis
# Example: Calculate average marks(%ge) of students in each department

# Visualizations
# Example: Bar chart showing enrollment counts by department
plt.figure(figsize=(6, 4))
sns.countplot(x='Name', data=students_df)
plt.title('Enrollment Counts by Department')
plt.xlabel('Department')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# Close the database connection
conn.close()