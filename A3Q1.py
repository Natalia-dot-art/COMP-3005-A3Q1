import psycopg2

#Connect to an existing database
conn = psycopg2.connect(dbname="A3DB", user="postgres", password="postgres")

#Open a cursor to perform database operations
cur = conn.cursor()

#Retrieves and displays all records from the students table.
def getAllStudents():

    cur.execute("SELECT * FROM students;")
    return print (cur.fetchall())

#Inserts a new student record into the students table.
#def addStudent(first_name, last_name, email, enrollment_date):
#Updates the email address for a student with the specified student_id.
#def updateStudentEmail(student_id, new_email):
#Deletes the record of the student with the specified student_id
#deleteStudent(student_id):

def main():

    getAllStudents()

main()

#Make the changes to the database persistent
conn.commit()
# Close communication with the database
cur.close()
conn.close()